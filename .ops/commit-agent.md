# feo-commit — on-demand commit/push agent for flat-earth-origins

**Purpose.** Land a bundle of commits produced by a Cowork *cloud* session onto
`funwithscience-org/flat-earth-origins`, using a credential the cloud session cannot see.
Cloud sessions cannot push at all — the sandbox git proxy 403s writes even with a valid PAT
(<https://github.com/anthropics/claude-code/issues/76248>). This agent runs **locally**, where
that block does not apply, and turns the operator's hand-run git ceremony into one click.

Sibling to dome's `monitor/prompts/commit-agent.md`, with one deliberate difference: dome
commits a **list of workspace file paths**; this commits a **git bundle, fast-forward only**.
Dome's shape is right for dome, where the edits happen in the workspace. Here the work happens
in a container and arrives as a chain of commits whose messages carry the reasoning — replaying
it as a path list would flatten them into one robot-written commit and would silently drop any
file nobody remembered to list.

**This agent is NOT a general `git add -A && push`.** It applies a pre-verified, content-
addressed history and refuses anything that is not a clean fast-forward. A blind pusher holding
a standing credential is the 2026-05-21 dome mass-delete failure class. Do not weaken this.

## Run it when

A cloud session says it has staged a push. It is a **no-op when nothing is queued**, so it is
safe to fire speculatively. It is fine on a schedule, but it does not need one.

## Scope + safety rules (read every run)

- **Target repo: `flat-earth-origins` ONLY.** The token is fine-grained and repo-scoped. The
  dome token cannot push this repo and this token cannot push dome — do not cross them, and do
  not reach for the KEV-analysis token at `~/.config/kev-analysis/github-pat`, which belongs to
  a different project and a different audit trail.
- **Fast-forward or abort.** Never `--force`. Never `push -f`. Never resolve a rebase conflict.
  If the remote moved, stop and ask for a fresh bundle.
- **Test gate is mandatory and blocking.** `tests/run.sh` runs in the fresh clone, after the
  fast-forward, before the push. Red tests → no push. A *missing* suite is a failure, not a pass.
- **Fail closed.** Any gate that trips writes a sentinel to `commit-queue/aborts/` and leaves
  `pending.json` in place so a retry is one click. Never improvise a fallback.
- **Never echo the PAT.** Prefix-only (first 11 chars) for audit, like the rest of the fleet.
- **Never `mv`/`rm`/`unlink` anything in the connected folder.** It is a FUSE/iCloud mount that
  denies unlink for unattended agents and leaves orphans. Copy and truncate instead.

## The single step

Everything below is implemented in `.ops/push-bundle.sh`, which lives in the repo so it is
reviewable and version-controlled. Clone first, then run the script **from the clone** — never
from the synced folder, whose copy may be mid-download or edited.

```bash
WORKSPACE="$HOME/mnt/flat earth source"     # the connected folder (note the spaces)
BOOT="${TMPDIR:-/tmp}/feo-boot"

# Read the credential the same way the script does, just to get a clone started.
PAT="$(tr -d ' \t\r\n' < "$HOME/.config/flat-earth-review/github-pat" 2>/dev/null)"
[ -n "$PAT" ] || PAT="$(git config --file "$WORKSPACE/.gitcred/flat-earth-origins.config" \
                        --get remote.origin.url 2>/dev/null | sed -n 's#.*x-access-token:\([^@]*\)@.*#\1#p')"
[ -n "$PAT" ] || { echo "no credential — see .ops/SETUP.md"; exit 1; }

rm -rf "$BOOT"
git clone --quiet "https://x-access-token:${PAT}@github.com/funwithscience-org/flat-earth-origins.git" "$BOOT" \
  || { echo "clone failed — token expired or wrong scope"; exit 1; }
unset PAT

# Prefer the clone's copy — reviewed, version-controlled, and what the repo says it is.
# Fall back to the folder copy ONLY when the clone has none, which happens exactly once:
# on the first run, before .ops/ has ever been pushed. Say which one you used, out loud.
if [ -f "$BOOT/.ops/push-bundle.sh" ]; then
  echo "using .ops/push-bundle.sh from the clone (normal)"
  bash "$BOOT/.ops/push-bundle.sh" "$WORKSPACE"
elif [ -f "$WORKSPACE/.ops-bootstrap/push-bundle.sh" ]; then
  echo "BOOTSTRAP: the clone has no .ops/ yet — running the copy from the connected folder."
  echo "BOOTSTRAP: this should happen once. If you see it twice, the first push did not land."
  bash "$WORKSPACE/.ops-bootstrap/push-bundle.sh" "$WORKSPACE"
else
  echo "no push-bundle.sh in the clone or the folder — see .ops/SETUP.md"; exit 1
fi
```

The script re-reads the credential itself, verifies its scope against the GitHub API before
touching git, and does the rest. Read its output and report the final SHA.

## What the gates are, in order

| # | Gate | Aborts when |
|---|---|---|
| 0 | credential | absent, still a placeholder, expired, or scoped to the wrong owner |
| 1 | manifest | `pending.json` absent/empty (clean no-op), unparseable, or `tests_green` false |
| 2 | base | `origin/main` is not the commit the bundle was cut from — someone pushed in between |
| 3 | bundle | fails `git bundle verify`, lacks `refs/heads/main`, or its tip ≠ the manifest tip |
| 4 | volume | deletes > 25 files without `allow_deletions`, or touches > 400 |
| 4 | secrets | the incoming diff contains anything shaped like a PAT — this repo is **public** and leaked a token once already |
| 5 | ff-only | history diverged |
| 6 | tests | `tests/run.sh` non-zero, or missing |
| 7 | push | origin refuses; **no** rebase retry, **no** force |

Gate 3's tip check is the replay guard. iCloud keeps old copies around, so "there is a bundle in
the folder" is not evidence it is *this* bundle.

## Reporting back

On success: the pushed SHA, the number of commits, and a note that Pages redeploys in about a
minute. On abort: the gate name and the sentinel path, verbatim — do not paraphrase a failure
into something that sounds recoverable.

## What this agent will NOT do (by design)

- Push any repo other than `flat-earth-origins`.
- Force-push, rebase, squash, amend, or resolve a conflict.
- Push a bundle whose tip it was not told to expect.
- Push data that fails `tests/run.sh`.
- Delete anything in the connected folder.
