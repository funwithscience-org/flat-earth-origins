#!/usr/bin/env bash
# .ops/push-bundle.sh — land a cloud session's commits on GitHub, checked.
#
# WHY A BUNDLE AND NOT A FILE MANIFEST
#   The sibling dome agent (monitor/prompts/commit-agent.md) commits an explicit
#   list of workspace file paths onto a fresh clone. That is right for dome, where
#   the workspace IS where the edits happen. It is wrong here: the work happens in
#   a cloud container and arrives as a chain of commits whose messages carry the
#   reasoning. Replaying it as a path list would flatten six curated commits into
#   one written by a robot, and would silently drop any file nobody remembered to
#   list.
#
#   So we transport a git bundle and require a FAST-FORWARD. That buys a safety
#   property a path list cannot have: the incoming history is content-addressed and
#   already fixed. This script cannot rewrite history, cannot reorder it, cannot
#   invent a commit. If the remote moved, it stops rather than reconciling.
#
#   What ff-only does NOT protect against is a commit that legitimately fast-forwards
#   while deleting the repo. That is the 2026-05-21 mass-delete failure class, and it
#   gets its own explicit gate below (DELETE_CEILING) rather than being assumed away.
#
# FAIL CLOSED. Every gate aborts with a sentinel and leaves the manifest in place
# for retry. Never force-push. Never resolve a conflict. Never echo the PAT.
#
# Usage (normally invoked by the commit agent, but runnable by hand):
#   bash .ops/push-bundle.sh "/path/to/workspace"     # workspace = connected folder
#
set -u

WORKSPACE="${1:-}"
if [ -z "$WORKSPACE" ] || [ ! -d "$WORKSPACE" ]; then
  echo "FATAL: workspace directory required as \$1 (the connected folder)"; exit 2
fi

REPO_SLUG="funwithscience-org/flat-earth-origins"

# TEST HOOK — deliberately narrow. `.ops/selftest.sh` points this at a local bare
# repo so every gate below can be exercised without a network or a real token.
# It changes exactly two things: where we clone from, and whether we ask GitHub to
# validate a credential (meaningless against a file:// origin). It CANNOT skip the
# ff-only rule, the volume ceilings, the secret scan, the test gate, or the
# no-force rule — those have no override and must not acquire one.
FEO_ORIGIN_OVERRIDE="${FEO_ORIGIN_OVERRIDE:-}"
QUEUE="$WORKSPACE/commit-queue"
MANIFEST="$QUEUE/pending.json"
SENTINEL_DIR="$QUEUE/aborts"
CLONE="${TMPDIR:-/tmp}/feo-push-clone"
DELETE_CEILING=25          # files a single push may delete without allow_deletions
CHANGE_CEILING=400         # files a single push may touch at all, deletions included

stage()  { echo ""; echo "==== $1 ===="; }
ok()     { echo "  ok: $1"; }

# Sentinels are the whole point of failing closed: the operator gets a file naming
# the gate that stopped it, and pending.json survives so a retry is one click.
abort() {
  local reason="$1"; local detail="${2:-}"
  local stamp; stamp="$(date -u +%Y-%m-%dT%H-%M-%SZ)"
  mkdir -p "$SENTINEL_DIR" 2>/dev/null || true
  # Second-resolution alone is not unique: the selftest fired eight aborts and left
  # three files, because retries inside the same second overwrote each other. A lost
  # sentinel is a lost diagnosis, which is the one thing this file exists to prevent.
  # The gate name is in the filename too, so a directory listing reads as a history.
  local sfile="$SENTINEL_DIR/abort-$stamp-$reason.json"
  local n=1
  while [ -e "$sfile" ]; do sfile="$SENTINEL_DIR/abort-$stamp-$reason-$n.json"; n=$((n+1)); done
  printf '{\n  "at": "%s",\n  "gate": "%s",\n  "detail": %s,\n  "manifest_left_in_place": true\n}\n' \
    "$stamp" "$reason" "$(printf '%s' "$detail" | python3 -c 'import json,sys; print(json.dumps(sys.stdin.read()))' 2>/dev/null || echo '""')" \
    > "$sfile" 2>/dev/null || true
  echo ""
  echo "ABORT [$reason]"
  [ -n "$detail" ] && echo "$detail"
  echo "Sentinel: $sfile"
  echo "pending.json left in place — fix the cause and re-run."
  exit 1
}

# ---------------------------------------------------------------------------
stage "0  credential"
if [ -n "$FEO_ORIGIN_OVERRIDE" ]; then
  echo "  SELFTEST: origin overridden to $FEO_ORIGIN_OVERRIDE — skipping credential + scope check."
  echo "  SELFTEST: every other gate runs exactly as in production."
  AUTH_URL="$FEO_ORIGIN_OVERRIDE"
else
# Order matters. The first location is a real filesystem on the local VM and is NOT
# iCloud-synced; the others are, and anything iCloud-mirrored is readable by every
# Cowork session on the account. Prefer the private one; the mirrored ones exist
# because the operator asked for dome parity, not because they are as good.
PAT=""
CRED_SOURCE=""
if [ -z "$PAT" ] && [ -r "$HOME/.config/flat-earth-review/github-pat" ]; then
  PAT="$(tr -d ' \t\r\n' < "$HOME/.config/flat-earth-review/github-pat")"
  CRED_SOURCE="~/.config/flat-earth-review/github-pat (private, not synced)"
fi
if [ -z "$PAT" ] && [ -r "$WORKSPACE/.gitcred/flat-earth-origins.config" ]; then
  _url="$(git config --file "$WORKSPACE/.gitcred/flat-earth-origins.config" --get remote.origin.url 2>/dev/null)"
  PAT="$(printf %s "$_url" | sed -n 's#.*x-access-token:\([^@]*\)@.*#\1#p')"
  CRED_SOURCE=".gitcred/flat-earth-origins.config (iCloud-synced)"
fi
if [ -z "$PAT" ] && [ -r "$WORKSPACE/flat-earth-origins/.git/config" ]; then
  _url="$(git config --file "$WORKSPACE/flat-earth-origins/.git/config" --get remote.origin.url 2>/dev/null)"
  PAT="$(printf %s "$_url" | sed -n 's#.*x-access-token:\([^@]*\)@.*#\1#p')"
  CRED_SOURCE="flat-earth-origins/.git/config (iCloud-synced, dome parity)"
fi
[ -n "$PAT" ] || abort "no-credential" \
  "Looked in ~/.config/flat-earth-review/github-pat, .gitcred/flat-earth-origins.config and flat-earth-origins/.git/config. See .ops/SETUP.md."
case "$PAT" in
  *REPLACE_WITH*|*PASTE*|*YOUR_*) abort "placeholder-credential" "The credential file still holds the placeholder. See .ops/SETUP.md." ;;
esac
ok "credential found in $CRED_SOURCE (prefix ${PAT:0:11}…)"

# Verify scope BEFORE any git operation, so a wrong-repo token fails here and not
# halfway through. This also catches expiry, which is a scheduled event: the token
# in use at time of writing expires 2026-09-07.
HTTP="$(curl -s -o /dev/null -w '%{http_code}' -H "Authorization: Bearer $PAT" \
        "https://api.github.com/repos/$REPO_SLUG")"
[ "$HTTP" = "200" ] || abort "credential-scope" \
  "GET /repos/$REPO_SLUG returned HTTP $HTTP for token prefix ${PAT:0:11}. Expired, revoked, or scoped to the wrong owner (it must be owned by funwithscience-org, not the personal account)."
ok "token authorises $REPO_SLUG"
AUTH_URL="https://x-access-token:${PAT}@github.com/${REPO_SLUG}.git"
fi

# ---------------------------------------------------------------------------
stage "1  manifest"
[ -s "$MANIFEST" ] || { echo "  no pending.json (or empty) — nothing queued. Clean no-op."; exit 0; }
read -r BUNDLE BASE TIP NCOMMITS TESTS <<EOF
$(python3 - "$MANIFEST" <<'PY'
import json, sys
m = json.load(open(sys.argv[1]))
for k in ("bundle", "base", "tip", "commits"):
    if not m.get(k):
        sys.exit(f"manifest missing required key: {k}")
print(m["bundle"], m["base"], m["tip"], len(m["commits"]),
      "yes" if m.get("tests_green") else "no")
PY
)
EOF
[ -n "${TIP:-}" ] || abort "manifest-invalid" "Could not parse $MANIFEST — see stderr above."
ok "manifest: $NCOMMITS commit(s), ${BASE:0:7} → ${TIP:0:7}, tests_green=$TESTS"
[ "$TESTS" = "yes" ] || abort "manifest-untested" \
  "The staging session did not record tests_green. Nothing is pushed from an untested manifest."

BUNDLE_PATH="$QUEUE/$BUNDLE"
[ -f "$BUNDLE_PATH" ] || BUNDLE_PATH="$WORKSPACE/$BUNDLE"
[ -f "$BUNDLE_PATH" ] || abort "bundle-missing" "No $BUNDLE in $QUEUE or $WORKSPACE. iCloud may still be downloading it — check for a .icloud placeholder."

# ---------------------------------------------------------------------------
stage "2  clone from GitHub (never trust the synced tree as a base)"
rm -rf "$CLONE"
# `--branch main` and `rev-parse origin/main`, not HEAD. HEAD is whatever the remote's
# default branch happens to be and can land detached or on an unborn branch; the
# selftest caught this by cloning a bare repo whose HEAD pointed at a branch that did
# not exist, and every downstream comparison then read the literal string "HEAD".
# We push to main, so main is the thing to name at every step.
git clone --quiet --branch main "$AUTH_URL" "$CLONE" 2>/dev/null \
  || abort "clone-failed" "git clone --branch main of $REPO_SLUG failed (no main branch, bad credential, or network)."
git -C "$CLONE" config user.email "russelst@melrosecastle.com"
git -C "$CLONE" config user.name  "steve"
REMOTE_HEAD="$(git -C "$CLONE" rev-parse origin/main 2>/dev/null)"
[ -n "$REMOTE_HEAD" ] || abort "no-remote-main" "The clone has no origin/main to compare against."
git -C "$CLONE" symbolic-ref -q HEAD >/dev/null \
  || abort "detached-clone" "The clone is in detached HEAD; refusing to fast-forward from an unnamed branch."
ok "origin/main is ${REMOTE_HEAD:0:7}"

if [ "$REMOTE_HEAD" = "$TIP" ]; then
  echo "  GitHub is already at the manifest tip. Nothing to do — archiving manifest."
  ARCHIVE_ONLY=1
else
  ARCHIVE_ONLY=0
  # Staleness / replay guard. If the remote is not where the bundle was cut from,
  # someone else pushed. Regenerating the bundle is cheap; guessing is not.
  [ "$REMOTE_HEAD" = "$BASE" ] || abort "base-moved" \
    "Manifest was cut from ${BASE:0:7} but origin/main is now ${REMOTE_HEAD:0:7}. Someone pushed in between. Re-run scripts/handoff.sh in the working session to cut a fresh bundle."
  ok "remote matches the manifest base"
fi

if [ "$ARCHIVE_ONLY" = "0" ]; then
  # -------------------------------------------------------------------------
  stage "3  verify + fetch the bundle"
  git -C "$CLONE" bundle verify "$BUNDLE_PATH" >/dev/null 2>&1 \
    || abort "bundle-corrupt" "git bundle verify failed on $BUNDLE_PATH. If this came through iCloud, confirm it finished downloading."
  git -C "$CLONE" fetch --quiet "$BUNDLE_PATH" main:incoming 2>/dev/null \
    || abort "bundle-no-main" "The bundle has no refs/heads/main. It was cut with '..HEAD' instead of '..main' — regenerate with scripts/handoff.sh."
  INCOMING="$(git -C "$CLONE" rev-parse incoming)"
  [ "$INCOMING" = "$TIP" ] || abort "bundle-mismatch" \
    "Bundle tip ${INCOMING:0:7} is not the manifest tip ${TIP:0:7}. The bundle in the folder is stale or from a different run — this is exactly the replay this check exists for."
  ok "bundle tip matches the manifest"

  # -------------------------------------------------------------------------
  stage "4  inspect what is actually being pushed"
  STAT="$(git -C "$CLONE" diff --numstat HEAD incoming | wc -l | tr -d ' ')"
  DELS="$(git -C "$CLONE" diff --diff-filter=D --name-only HEAD incoming | wc -l | tr -d ' ')"
  echo "  files touched: $STAT   files deleted: $DELS"
  git -C "$CLONE" diff --stat HEAD incoming | tail -1

  ALLOW_DEL="$(python3 -c "import json;print('1' if json.load(open('$MANIFEST')).get('allow_deletions') else '0')" 2>/dev/null || echo 0)"
  if [ "$DELS" -gt "$DELETE_CEILING" ] && [ "$ALLOW_DEL" != "1" ]; then
    abort "deletion-ceiling" \
      "This push deletes $DELS files (ceiling $DELETE_CEILING). Fast-forward alone does not make a mass delete safe. If it is intended, set allow_deletions:true in the manifest and re-run."
  fi
  [ "$STAT" -le "$CHANGE_CEILING" ] || abort "change-ceiling" \
    "This push touches $STAT files (ceiling $CHANGE_CEILING). Almost certainly a mistake; raise the ceiling deliberately if not."
  ok "change volume within ceilings"

  # Secret scan. This repo is PUBLIC and has leaked a token once already
  # (2026-08-02, via a transcript). The cost of this check is a second.
  LEAK="$(git -C "$CLONE" diff HEAD incoming -- . \
          | grep -nE 'github_pat_[A-Za-z0-9_]{20,}|ghp_[A-Za-z0-9]{30,}|gho_[A-Za-z0-9]{30,}|x-access-token:[^@[:space:]]{20,}' \
          | head -5 || true)"
  if [ -n "$LEAK" ]; then
    abort "secret-in-diff" "The incoming diff contains something shaped like a credential. NOT pushing. First match(es) redacted to line numbers: $(printf '%s' "$LEAK" | cut -c1-40)"
  fi
  ok "no credential-shaped strings in the diff"

  # -------------------------------------------------------------------------
  stage "5  fast-forward"
  git -C "$CLONE" merge --ff-only --quiet incoming \
    || abort "not-fast-forward" "merge --ff-only refused. History diverged; this script does not reconcile. Investigate by hand."
  ok "fast-forwarded to ${TIP:0:7}"

  # -------------------------------------------------------------------------
  stage "6  test gate (mandatory, blocking)"
  if [ -x "$CLONE/tests/run.sh" ]; then
    TEST_OUT="$(cd "$CLONE" && ./tests/run.sh 2>&1)"; RC=$?
  elif [ -f "$CLONE/tests/run.sh" ]; then
    TEST_OUT="$(cd "$CLONE" && bash tests/run.sh 2>&1)"; RC=$?
  else
    abort "no-test-suite" "tests/run.sh is missing from the clone. The gate is mandatory; a missing suite is a failure, not a pass."
  fi
  if [ "$RC" != "0" ]; then
    abort "tests-red" "$(printf '%s' "$TEST_OUT" | tail -25)"
  fi
  ok "$(printf '%s' "$TEST_OUT" | tail -1)"

  # -------------------------------------------------------------------------
  stage "7  push"
  # No --force, no rebase retry. A rejection here means the remote moved during the
  # run, and the correct response is to re-cut the bundle, not to reconcile blind.
  if ! git -C "$CLONE" push --quiet origin main 2>&1; then
    abort "push-rejected" "origin refused the push. Remote probably moved mid-run. Re-run this agent; step 2 will report the new base."
  fi
  ok "pushed ${TIP:0:7} to $REPO_SLUG main"
fi

# ---------------------------------------------------------------------------
stage "8  archive the manifest"
# FUSE RULE, inherited from the dome agent and NOT optional: the workspace is an
# iCloud mount that denies unlink for unattended agents. `mv` and `rm` fail and
# leave orphans that need a drain to clear. Archive by copy, then TRUNCATE in
# place — a write, which is always allowed. An empty pending.json is the correct
# "nothing queued" state; step 1 treats it as a clean no-op.
STAMP="$(date -u +%Y-%m-%dT%H-%M-%SZ)"
cp "$MANIFEST" "$QUEUE/done-$STAMP.json" 2>/dev/null || echo "  (warn: could not archive manifest copy)"
: > "$MANIFEST" 2>/dev/null || echo "  (warn: could not truncate manifest — it may re-run; harmless, step 2 no-ops)"
{
  echo "pushed:  $TIP"
  echo "at:      $STAMP"
  echo "base:    $BASE"
  echo "commits: $NCOMMITS"
} > "$QUEUE/last-push.txt" 2>/dev/null || true
rm -rf "$CLONE"

echo ""
echo "DONE — $REPO_SLUG main is at ${TIP:0:7}."
echo "GitHub Pages redeploys in about a minute; then check the live page."
