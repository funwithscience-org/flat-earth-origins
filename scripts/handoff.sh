#!/usr/bin/env bash
# handoff.sh — package unpushed commits for transport out of a Cowork session.
#
# WHY THIS EXISTS
#   Cowork cloud sessions cannot push to GitHub. The sandbox git proxy returns
#   403 for any repo not in the session's "authorized repository set", and it
#   does so even when we supply our own valid PAT — GitHub never sees the token.
#   Reads work; writes do not. There is no UI to add a repo to the sources and
#   no `add_repo` command in the sandbox.
#
#   Tracked at: https://github.com/anthropics/claude-code/issues/76248
#   (open, area:cowork, has repro, no maintainer response as of 2026-08-08)
#
#   Do NOT "fix" this by clearing http.proxy/https.proxy to route around the
#   proxy. It is an access-control decision, not a routing accident, and no
#   Anthropic-endorsed workaround exists. Use the bundles.
#
# USAGE
#   tests/run.sh && scripts/handoff.sh          # verify, then package
#
# OUTPUT (in ./handoff/)
#   feo-unpushed.bundle  incremental from the last commit GitHub has
#   feo-full.bundle      complete history; clones from nothing
#   HANDOFF.md           what is in them and how to push from a real machine
#
# Then: send the three files to the user and write them to the connected
# folder. They push from their own machine.

set -euo pipefail
cd "$(dirname "$0")/.."

REMOTE="https://github.com/funwithscience-org/flat-earth-origins.git"
OUT="handoff"
mkdir -p "$OUT"

LOCAL=$(git rev-parse HEAD)
echo "local HEAD : ${LOCAL:0:7}"

# Reads still work, so ask GitHub what it actually has rather than assuming.
if REMOTE_SHA=$(git ls-remote "$REMOTE" main 2>/dev/null | cut -f1) && [ -n "$REMOTE_SHA" ]; then
    echo "github main: ${REMOTE_SHA:0:7}"
else
    echo "github main: UNREACHABLE — falling back to a full bundle only" >&2
    REMOTE_SHA=""
fi

if [ "$REMOTE_SHA" = "$LOCAL" ]; then
    echo "Nothing to hand off — GitHub is already at HEAD."
    exit 0
fi

if [ -n "$REMOTE_SHA" ] && git cat-file -e "$REMOTE_SHA^{commit}" 2>/dev/null; then
    git bundle create "$OUT/feo-unpushed.bundle" "$REMOTE_SHA..HEAD" >/dev/null 2>&1
    BASE="$REMOTE_SHA"
else
    # GitHub has a commit we do not, or is unreachable. An incremental bundle
    # would be a lie, so skip it rather than emit one that cannot be applied.
    rm -f "$OUT/feo-unpushed.bundle"
    BASE=""
    echo "NOTE: no usable base commit — incremental bundle skipped." >&2
fi
git bundle create "$OUT/feo-full.bundle" --all >/dev/null 2>&1

# Verify before shipping. An unverified bundle is worse than no bundle.
git bundle verify "$OUT/feo-full.bundle" >/dev/null 2>&1 || { echo "FULL BUNDLE FAILED VERIFY" >&2; exit 1; }

COMMITS=$(if [ -n "$BASE" ]; then git log --oneline "$BASE..HEAD"; else git log --oneline -20; fi)

cat > "$OUT/HANDOFF.md" <<EOF
# Handoff — flat-earth-origins

Generated from a Cowork session that cannot push. See
<https://github.com/anthropics/claude-code/issues/76248>.

    local HEAD  ${LOCAL:0:7}
    github main ${REMOTE_SHA:0:7}

## Commits that exist only here

\`\`\`
$COMMITS
\`\`\`

## Push from your own machine

Existing clone:

    git fetch /path/to/feo-unpushed.bundle main:incoming
    git merge --ff-only incoming
    git push origin main
    git branch -d incoming

\`--ff-only\` is deliberate: if it refuses, something diverged and you want to
know rather than have git merge it quietly.

No clone:

    git clone /path/to/feo-full.bundle flat-earth-origins
    cd flat-earth-origins
    git remote set-url origin $REMOTE
    git push origin main

## Confirm it landed

Pages redeploys in about a minute. The live page should then carry:

* an "Under construction" block on Overview
* "Refute the source, not the summary" on Method
* ARG-A10 titled "No wind or drag is felt from the Earth's motion" —
  if it still says "atmosphere can't co-rotate", the deploy has not taken
EOF

echo
ls -lh "$OUT"
echo
echo "Ready. Send these to the user and write them to the connected folder."
