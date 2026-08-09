# One-time setup for the local commit agent

Three things, once. After that, pushing is: cloud session stages → you fire the task.

---

## 1. Put the token where the agent can read it

**I cannot do this step.** I do not hold the PAT — it has never been in a cloud container, and
that is the property worth keeping. You paste it locally.

The script looks in three places, first hit wins. **Use the first one.**

### Preferred — private to the local VM, not synced

```sh
mkdir -p ~/.config/flat-earth-review
printf '%s' 'github_pat_XXXXXXXX' > ~/.config/flat-earth-review/github-pat
chmod 600 ~/.config/flat-earth-review/github-pat
```

Run that inside a **local Cowork session** (so `~` is the local workspace home, the same place
the KEV project keeps its token). It survives across sessions and is not iCloud-synced.

### Fallback — dome parity, in the connected folder

This is the shape you asked for, and it works. It is second choice for one reason, stated plainly
below. `.gitcred/flat-earth-origins.config` is pre-created with a placeholder:

```sh
cd "$HOME/mnt/flat earth source"
sed -i '' 's#REPLACE_WITH_PAT#github_pat_XXXXXXXX#' .gitcred/flat-earth-origins.config
```

The script also accepts `flat-earth-origins/.git/config` for exact dome parity, if you would
rather keep one habit across both projects.

### Why I recommend the first one

Your own KEV rule says it, and it applies here unchanged: *anything iCloud-mirrored leaks to
every Cowork session*. A token in the connected folder is readable by any session that has that
folder attached, including sessions doing unrelated work, and it syncs to Apple's servers. The
private path costs one extra command and removes that whole class.

**The counter-argument, honestly:** the blast radius here is genuinely small. The token is
fine-grained, single-repo, Contents-only, and expires 2026-09-07. The repo is public, so its
contents are not secret. Every push it can make is fast-forward-only, so history cannot be
rewritten and nothing is unrecoverable. Dome has run this way for months without incident. If
folder-based storage is what makes you actually use the agent, that is a better outcome than a
purer scheme you skip — the manual route is where the real errors have come from. Your call; the
script supports both.

**Either way: the token must never be committed.** `.gitignore` covers `.gitcred/`, and gate 4
of the agent refuses to push any diff containing a PAT-shaped string.

---

## 2. Create the connected-folder layout

```sh
cd "$HOME/mnt/flat earth source"
mkdir -p commit-queue/aborts .gitcred
```

`commit-queue/` is where staged pushes land:

| File | Written by | Meaning |
|---|---|---|
| `pending.json` | the cloud session | a push is queued. Empty file = nothing queued (the normal state) |
| `feo-unpushed.bundle` | the cloud session | the commits themselves |
| `done-<ISO>.json` | the agent | archived manifest, one per successful push |
| `last-push.txt` | the agent | SHA and timestamp of the most recent push |
| `aborts/abort-<ISO>.json` | the agent | a gate tripped; names which one |

---

## 3. Create the scheduled task

Local Cowork instance, schedule-only. The prompt is the contents of `.ops/commit-agent.md` —
paste it whole. It is written to be self-sufficient: it bootstraps a clone using the credential,
then runs `.ops/push-bundle.sh` **from that clone**, so the logic it executes is the reviewed,
version-controlled copy rather than whatever is sitting in the synced folder.

It is a **no-op when nothing is queued**, so a schedule is safe. Hourly is plenty; on-demand is
also fine, since firing it costs nothing when the queue is empty.

---

## Bootstrap — handled, no manual push needed

`.ops/push-bundle.sh` normally comes from the fresh clone, so the agent runs reviewed,
version-controlled code rather than whatever is sitting in a synced folder. But on the very
first run it is not on GitHub yet — it is inside the commits waiting to be pushed, which is
circular.

So a copy also lives at `.ops-bootstrap/push-bundle.sh` in the connected folder, and the agent
uses it **only when the clone has none**. It announces which copy it used. You should see the
`BOOTSTRAP:` line exactly once, on run one; if it appears a second time, the first push did not
actually land and you should read `commit-queue/aborts/`.

After that first successful push, `.ops-bootstrap/` is dead weight and can be deleted — the
clone will always have the real thing. Leaving it costs nothing but is one more copy to keep
in step, so deleting it is tidier.

---

## Checking it worked

```sh
cat "$HOME/mnt/flat earth source/commit-queue/last-push.txt"
ls "$HOME/mnt/flat earth source/commit-queue/aborts/"     # should stay empty
```

Then the live page at <https://funwithscience.net/flat-earth-origins/> — Pages redeploys in
about a minute.

## If the token expires

It expires **2026-09-07**. Gate 0 catches it and aborts with `credential-scope` before touching
git, so the failure is loud and specific rather than a confusing git error. Regenerate at
<https://github.com/settings/personal-access-tokens>: fine-grained, **resource owner
`funwithscience-org`** (it defaults to your personal account — that is the usual mistake),
repository `flat-earth-origins`, **Contents: Read and write**. Then redo step 1.
