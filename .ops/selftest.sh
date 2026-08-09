#!/usr/bin/env bash
# .ops/selftest.sh — exercise every gate in push-bundle.sh against a local origin.
#
# WHY THIS EXISTS
#   push-bundle.sh holds a standing credential and pushes to a public repo without a
#   human in the loop. Shipping it unexercised would be the same class of mistake the
#   review itself is about: a mechanism that looks careful and has never been tested
#   against the case it claims to catch. Each scenario below asserts a SPECIFIC gate
#   name in the output, so a gate that silently stops firing turns this red.
#
#   It builds throwaway repos under $TMPDIR. It never touches GitHub, never reads a
#   real credential, and never runs in the connected folder.
#
# Usage:  bash .ops/selftest.sh
#
set -u
SCRIPT="$(cd "$(dirname "$0")" && pwd)/push-bundle.sh"
REPO="$(cd "$(dirname "$0")/.." && pwd)"
LAB="${TMPDIR:-/tmp}/feo-selftest"

# Read the credential pattern OUT OF THE GATE rather than restating it here. A second
# copy would drift, and a drifted copy is worse than none: the tests would go green
# against a pattern the gate does not use.
SECRET_PATTERN="$(sed -n "s/^SECRET_PATTERN='\(.*\)'\$/\1/p" "$SCRIPT")"
if [ -z "$SECRET_PATTERN" ]; then
  echo "FATAL: could not extract SECRET_PATTERN from $SCRIPT — the line format changed."
  echo "       Fix the extraction; do not paste a copy of the pattern in here."
  exit 2
fi
PASS=0; FAIL=0
declare -a FAILED

say()  { echo ""; echo "───── $1"; }
# A scenario passes when the run's exit status matches AND the expected gate name
# (or DONE) appears. Checking only the exit status would let the wrong gate pass.
expect() {
  local name="$1" want_rc="$2" want_str="$3" out rc
  out="$(cd "$LAB" && bash "$SCRIPT" "$LAB/workspace" 2>&1)"; rc=$?
  if [ "$rc" = "$want_rc" ] && printf '%s' "$out" | grep -q -- "$want_str"; then
    echo "  PASS  $name"; PASS=$((PASS+1))
  else
    echo "  FAIL  $name (rc=$rc, wanted $want_rc containing '$want_str')"
    printf '%s\n' "$out" | sed 's/^/        | /' | tail -12
    FAIL=$((FAIL+1)); FAILED+=("$name")
  fi
}

# --- build a miniature repo that looks like ours -----------------------------
rm -rf "$LAB"; mkdir -p "$LAB/workspace/commit-queue"
export FEO_ORIGIN_OVERRIDE="$LAB/origin.git"

git init --quiet --bare --initial-branch=main "$LAB/origin.git" 2>/dev/null \
  || { git init --quiet --bare "$LAB/origin.git"; git -C "$LAB/origin.git" symbolic-ref HEAD refs/heads/main; }
git init --quiet --initial-branch=main "$LAB/work" 2>/dev/null || git init --quiet "$LAB/work"
cd "$LAB/work"
git checkout -q -B main 2>/dev/null || true
git config user.email t@t; git config user.name t
mkdir -p tests docs
# A stand-in suite whose pass/fail we control with a sentinel file, so the "tests
# red" scenario tests the GATE, not a contrived failure of the real suite.
cat > tests/run.sh <<'EOS'
#!/usr/bin/env bash
[ -f tests/FAIL ] && { echo "FAILED: 1 check(s)"; exit 1; }
echo "All checks passed."
EOS
chmod +x tests/run.sh
echo "base" > docs/index.html
for i in 1 2 3 4 5; do echo "x" > "docs/f$i.txt"; done
git add -A; git commit --quiet -m "base"
git push --quiet "$LAB/origin.git" HEAD:main
BASE="$(git rev-parse HEAD)"

# two ordinary commits on top — the happy path payload
echo "changed" > docs/index.html; git add -A; git commit --quiet -m "edit the page"
echo "more"    >> docs/index.html; git add -A; git commit --quiet -m "edit it again"
TIP="$(git rev-parse HEAD)"

Q="$LAB/workspace/commit-queue"
manifest() {  # manifest <base> <tip> <tests_green> [allow_deletions]
  python3 - "$Q/pending.json" "$1" "$2" "$3" "${4:-false}" <<'PY'
import json, sys
out, base, tip, tests, allow = sys.argv[1:6]
json.dump({"bundle": "feo-unpushed.bundle", "base": base, "tip": tip,
           "commits": [{"sha": tip, "subject": "selftest"}],
           "tests_green": tests == "true", "allow_deletions": allow == "true",
           "repo": "funwithscience-org/flat-earth-origins"}, open(out, "w"), indent=2)
PY
}
bundle() { git -C "$LAB/work" bundle create "$Q/feo-unpushed.bundle" "$1..$2" >/dev/null 2>&1; }

# =============================================================================
say "1  empty queue is a clean no-op, not an error"
: > "$Q/pending.json"
expect "empty manifest exits 0" 0 "nothing queued"

say "2  a manifest that never passed tests is refused"
manifest "$BASE" "$TIP" false; bundle "$BASE" main
expect "manifest-untested" 1 "manifest-untested"

say "3  happy path: verify, ff, test, push"
manifest "$BASE" "$TIP" true
expect "clean push" 0 "DONE"
[ "$(git -C "$LAB/origin.git" rev-parse main)" = "$TIP" ] \
  && { echo "  PASS  origin advanced to the tip"; PASS=$((PASS+1)); } \
  || { echo "  FAIL  origin did not advance"; FAIL=$((FAIL+1)); FAILED+=("origin advanced"); }
[ -s "$Q/pending.json" ] \
  && { echo "  FAIL  manifest not truncated after success"; FAIL=$((FAIL+1)); FAILED+=("manifest truncated"); } \
  || { echo "  PASS  manifest truncated (FUSE-safe archive)"; PASS=$((PASS+1)); }

say "4  re-running after a successful push is idempotent"
manifest "$BASE" "$TIP" true
expect "already at tip" 0 "already at the manifest tip"

say "5  someone else pushed in between -> base-moved"
git -C "$LAB/work" checkout --quiet -b side "$BASE"
echo "third party" > docs/other.txt
git -C "$LAB/work" add -A; git -C "$LAB/work" commit --quiet -m "someone else"
git -C "$LAB/work" push --quiet "$LAB/origin.git" +side:main
manifest "$BASE" "$TIP" true; bundle "$BASE" main
expect "base-moved" 1 "base-moved"
git -C "$LAB/work" push --quiet "$LAB/origin.git" +main:main   # restore
git -C "$LAB/work" checkout --quiet main

say "6  a stale bundle in the folder -> bundle-mismatch (the replay guard)"
NEWBASE="$(git -C "$LAB/origin.git" rev-parse main)"
echo "fresh" > "$LAB/work/docs/fresh.txt"
git -C "$LAB/work" add -A; git -C "$LAB/work" commit --quiet -m "fresh work"
NEWTIP="$(git -C "$LAB/work" rev-parse HEAD)"
manifest "$NEWBASE" "$NEWTIP" true
bundle "$BASE" "$NEWBASE"          # deliberately the WRONG (older) bundle
expect "bundle-mismatch" 1 "bundle-mismatch"

say "7  a bundle cut with ..HEAD has no refs/heads/main"
git -C "$LAB/work" bundle create "$Q/feo-unpushed.bundle" "$NEWBASE..HEAD" >/dev/null 2>&1
expect "bundle-no-main" 1 "bundle-no-main"

say "8  a credential in the diff is never pushed"
bundle "$NEWBASE" main
# SYNTHESISED AT RUNTIME, NEVER STORED. The first version of this line held the
# credential-shaped literal directly, and the agent's very first live run refused to
# push because of it — correctly. The commit that introduces a secret scanner cannot
# also introduce the one string the scanner is built to reject.
#
# The fix is not to allowlist this file. A path-shaped hole in a secret scanner is
# permanent and silent: a real token pasted here later would sail through, and this is
# exactly the file where someone debugging the gate would paste one. Adjacent-string
# concatenation gives the runtime the full pattern while the file on disk never
# contains it, so the gate stays absolute and the test still proves it fires.
FAKE_PAT="github""_pat_""11ABCDEFG0123456789abcdefghijklmnopqrstuvwxyz012345"
# Assert the fixture still matches the gate's own pattern, extracted from the script
# rather than copied. Without this the failure mode is a MISLEADING RED, not a silent
# green: a shortened fixture makes the push succeed and scenario 8 fails with "wanted
# rc 1", which points at the gate instead of at the fixture. It can also pass for the
# wrong reason if anything else in the diff happens to match. One line removes both.
if ! printf '%s' "$FAKE_PAT" | grep -qE "$SECRET_PATTERN"; then
  echo "  FAIL  fixture no longer matches the scanner pattern — scenario 8 proves nothing"
  FAIL=$((FAIL+1)); FAILED+=("fixture matches pattern")
else
  echo "  PASS  fixture still matches the gate's own pattern"; PASS=$((PASS+1))
fi
printf 'token: %s\n' "$FAKE_PAT" > "$LAB/work/docs/oops.txt"
git -C "$LAB/work" add -A; git -C "$LAB/work" commit --quiet -m "oops"
LEAKTIP="$(git -C "$LAB/work" rev-parse HEAD)"
manifest "$NEWBASE" "$LEAKTIP" true; bundle "$NEWBASE" main
expect "secret-in-diff" 1 "secret-in-diff"
git -C "$LAB/work" reset --hard --quiet "$NEWTIP"

say "9  a mass delete fast-forwards cleanly and is still refused"
git -C "$LAB/work" rm -q docs/f1.txt docs/f2.txt docs/f3.txt docs/f4.txt docs/f5.txt
git -C "$LAB/work" commit --quiet -m "delete a lot"
DELTIP="$(git -C "$LAB/work" rev-parse HEAD)"
manifest "$NEWBASE" "$DELTIP" true; bundle "$NEWBASE" main
# Ceiling is 25 in production; prove the gate fires by lowering it for this case only.
OUT="$(cd "$LAB" && sed 's/^DELETE_CEILING=25/DELETE_CEILING=2/' "$SCRIPT" > "$LAB/lowered.sh" \
       && bash "$LAB/lowered.sh" "$LAB/workspace" 2>&1)"
printf '%s' "$OUT" | grep -q "deletion-ceiling" \
  && { echo "  PASS  deletion-ceiling fires on a clean fast-forward"; PASS=$((PASS+1)); } \
  || { echo "  FAIL  deletion-ceiling did not fire"; printf '%s\n' "$OUT" | tail -8; FAIL=$((FAIL+1)); FAILED+=("deletion-ceiling"); }

say "10  allow_deletions lets an intended delete through"
manifest "$NEWBASE" "$DELTIP" true true
OUT="$(cd "$LAB" && bash "$LAB/lowered.sh" "$LAB/workspace" 2>&1)"
printf '%s' "$OUT" | grep -q "DONE" \
  && { echo "  PASS  allow_deletions honoured"; PASS=$((PASS+1)); } \
  || { echo "  FAIL  allow_deletions not honoured"; printf '%s\n' "$OUT" | tail -8; FAIL=$((FAIL+1)); FAILED+=("allow_deletions"); }

say "11  red tests block the push"
NEWBASE2="$(git -C "$LAB/origin.git" rev-parse main)"
git -C "$LAB/work" fetch --quiet "$LAB/origin.git" main && git -C "$LAB/work" reset --hard --quiet FETCH_HEAD
touch "$LAB/work/tests/FAIL"
git -C "$LAB/work" add -A; git -C "$LAB/work" commit --quiet -m "break the suite"
REDTIP="$(git -C "$LAB/work" rev-parse HEAD)"
manifest "$NEWBASE2" "$REDTIP" true; bundle "$NEWBASE2" main
expect "tests-red" 1 "tests-red"
[ "$(git -C "$LAB/origin.git" rev-parse main)" = "$NEWBASE2" ] \
  && { echo "  PASS  origin unchanged after a red run"; PASS=$((PASS+1)); } \
  || { echo "  FAIL  origin MOVED despite red tests"; FAIL=$((FAIL+1)); FAILED+=("origin unchanged on red"); }

say "12  a missing suite is a failure, not a pass"
git -C "$LAB/work" reset --hard --quiet "$NEWBASE2"
git -C "$LAB/work" rm -q -r tests
git -C "$LAB/work" commit --quiet -m "remove the suite"
NOTESTTIP="$(git -C "$LAB/work" rev-parse HEAD)"
manifest "$NEWBASE2" "$NOTESTTIP" true; bundle "$NEWBASE2" main
expect "no-test-suite" 1 "no-test-suite"

say "13  the repo's own tracked tree carries no credential-shaped string"
# Added after the agent's first live run refused to push because .ops/selftest.sh held
# a literal fake token. That was found the expensive way — at the push gate, after a
# bundle had been cut, staged, synced and fired. The same scan run here costs a second
# and fails at the moment the string is written. Tracked files only: the gate scans a
# diff, so anything git ignores can never reach it.
#
# FIRST VERSION OF THIS CHECK WAS BROKEN AND THE CANARY IS THE ONLY REASON WE KNOW.
# It piped `git -C "$REPO" ls-files` into a bare `grep`. ls-files prints paths relative
# to the repo root, but by this point the script has cd'd into $LAB/work, so grep looked
# for every path in the wrong directory, found nothing, and `2>/dev/null` swallowed the
# errors. It reported PASS while scanning zero files — the exact "quietly stops testing"
# failure this check was added to prevent, reproduced inside the check itself.
# `git grep` resolves paths against the repo it is given, so there is no cwd to get wrong.
_HITS="$(git -C "$REPO" grep -lE "$SECRET_PATTERN" -- . 2>/dev/null || true)"
if [ -z "$_HITS" ]; then
  echo "  PASS  no credential-shaped string in any tracked file"; PASS=$((PASS+1))
else
  echo "  FAIL  credential-shaped string in tracked file(s):"
  printf '        %s\n' $_HITS
  echo "        Build it at runtime (see FAKE_PAT above). Do NOT allowlist the path —"
  echo "        a path-shaped hole in a secret scanner is permanent and silent."
  FAIL=$((FAIL+1)); FAILED+=("tracked tree clean")
fi

say "14  every abort left a sentinel"
N="$(ls "$Q/aborts" 2>/dev/null | wc -l | tr -d ' ')"
[ "${N:-0}" -ge 7 ] \
  && { echo "  PASS  $N sentinels written"; PASS=$((PASS+1)); } \
  || { echo "  FAIL  only ${N:-0} sentinels"; FAIL=$((FAIL+1)); FAILED+=("sentinels"); }

echo ""
echo "═════════════════════════════════════════"
if [ "$FAIL" = 0 ]; then
  echo "  $PASS passed, 0 failed."
  rm -rf "$LAB"; exit 0
fi
echo "  $PASS passed, $FAIL FAILED:"
printf '    - %s\n' "${FAILED[@]}"
echo "  Lab left at $LAB for inspection."
exit 1
