# flat-earth-origins

A **provenance review** of flat-earth and geocentric "proof lists". Sibling to
`dome-model-review`: same design system, same six-verdict rubric, same process.

Published page: `docs/index.html` → intended to serve at
`https://funwithscience.net/flat-earth-origins/`

**Publishing is operator-gated.** Do not push a half-empty page live.

## What this is

Long numbered "proof lists" work by volume: each item reads as an independent witness,
so 461 items feels like a fortress. A claim is not a witness — it has an author, and
authors can be counted. This review sorts one representative specimen (the 461-item list
at `withthesun33.com/about-1`, retrieved 2026-08-02) by **where each claim came from**.

Sorted that way it collapses to **98 distinct arguments** traceable to **20 named people**
in **two lineages that were never reconciled with each other** — plus a body of esoteric
literature whose authors were not making claims about geography at all.

The page reviews published *claims*. It does not target any individual.

| Metric | Value |
|---|---|
| Items in the specimen | 461 |
| Distinct arguments | 98 (4.7× compression) |
| Named originators | 20, covering 372 of 461 items |
| Items that discriminate flat/stationary from the globe | **0** |

Two people account for 43% of the list: **Samuel Rowbotham** (65 items, writing 1849–65)
and **Robert Sungenis** across three bylines (134). The largest single cluster — 28 items —
is one idea restated in eight technical vocabularies.

## Layout

```
docs/index.html      the rendered review page  (GENERATED — do not hand-edit)
data/                the provenance dataset, JSON + CSV  (GENERATED)
scripts/corpus.py    verbatim 461-item corpus; the only place raw claim text lives
scripts/clusters.py  98 cluster definitions: name, originator, work, year,
                     real source cited, verdict, basis.  ← edit verdicts HERE
scripts/assign.py    item number → cluster id
scripts/build.py     corpus + clusters + assign → data/
scripts/render.py    data/ + scripts/_head.html → docs/index.html
scripts/_head.html   the <head> and <style> block  ← edit design HERE
tests/               fail-loud invariants
```

## Working on it

`docs/index.html` and `data/*` are **generated artefacts**. Editing the HTML by hand will
be silently overwritten on the next render. To change something:

| To change | Edit |
|---|---|
| A verdict, attribution or basis line | `scripts/clusters.py` |
| Which cluster an item belongs to | `scripts/assign.py` |
| Page prose, section structure | the `BODY` string in `scripts/render.py` |
| Colours, typography, CSS | `scripts/_head.html` |

Then:

```sh
tests/run.sh        # rebuilds dataset + page, then asserts every published figure
```

**Run the tests before every commit. Blocking, not advisory.** Loosening a tolerance is
almost never the right move — if a number moved, the page text that quotes it moved too.

**Adding a numeric claim to the page → add a check for it in
`tests/test_provenance.py`.** Copy a nearby assertion and narrow it. Claims without tests
rot. The suite is canary-verified: flipping a single item's cluster assignment turns it red.

The suite also carries **attribution guards** — assertions that specific unverified claims
do *not* appear as fact (Carpenter's pamphlet as provably the first numbered list; Nathan
Oakley; Paul Ellwanger as a geocentrist; "Dubay plagiarised"). These exist because those
are the errors a future edit is most likely to reintroduce.

## The hedge rule

**Refute the source's hedged wording, never the list's compressed phrasing.** Standing
rule as of 2026-08-05; it governs every treatment and the curmudgeon pass checks it first.

List items are fragments — *"Airy's failure to detect starlight motion."* The books they
came from qualify, scope to a case, and sometimes concede outright. Beating the fragment
beats nobody, and it is the move we object to when it is done to us. **This is the reason
the project traces claims back to originals at all**, rather than answering the list.

The second clause matters as much: a hedge is not an escape hatch. The compressed version
is what circulates, so where an item claims more than its source did, that gap is
published as a finding on the argument itself — both texts side by side, with what
changed named. Answer the source on the merits *and* show the drift.

Mechanically: every `DEEP` entry carries a `compression` block, `build.py` refuses to
build without one, and the page publishes how many arguments have been checked. See the
schema and the seven `drift_type` values at the top of `scripts/deep.py`; worked cases are
`ARG-R01` (`force_upgraded`) and `ARG-A03` (`category_shifted`). `assessed=False` means
nobody has compared the texts yet — it never means the phrasing is faithful.

## Sourcing standard

Every verdict cites a public source or a reproducible calculation. Engage the strongest
form of each argument. Unfalsifiable claims are named, not ridiculed. Duplicate items are
grouped and scored once per distinct argument, so the "461" headline does not inflate the
work. Provenance attributions trace to a specific publication with a date; where an
attribution could not be established the item is recorded as **untraced rather than
guessed** (89 items, 29 clusters).

**"Untraced" is a claim, not a fact about the list, and it is audited like any other.**
ARG-E13 was recorded as untraced until 2026-08-08, when a search found three of its six
items in Sungenis & Bennett. Two of the 30 have now been tested and one came back the
other way, so treat the remaining 28 as provisional in *both* directions.

Verified attributions, with URLs and an explicit list of what could *not* be verified, live
in the project doc `claude/source-genealogy.md`. **Read it before writing any provenance
claim.** It cost three parallel research passes; do not re-derive it.

## Known limits

- 89 of 461 items could not be traced to a named origin. That is a limit of this pass, not
  evidence of originality — they are mostly one-line assertions with no cited source, which
  is *why* they are unattributable. One cluster has already moved out of this bucket on
  audit, so the figure should be read as an upper bound.
- Cluster boundaries involve judgement. A handful of items could defensibly sit in an
  adjacent cluster; that would move counts by a few units without changing any verdict.
- Carpenter 1885 is the earliest numbered proof-list **identified**, not provably the first —
  his own earlier works were not available to check.
- The corpus was extracted via an intermediary model. Two independent fetches agreed
  character-for-character on a spot-checked range, but re-verify any single item against the
  live page before making its exact wording load-bearing.

## Still open

1. Long-form writeups for the four careful cases: Airy's failure (`A03`), general covariance
   (`R01`/`R06`), Sagnac / Michelson-Gale interferometry detail (`A02`), CMB axis of evil
   (`E01`). The CMB one must not overclaim - that debate is genuinely live.
2. A second pass at the 95 untraced items.
3. Umbrella cross-link (5th card + detail block on the landing page).
4. GitHub Pages source needs pointing at `docs/`; custom-domain behaviour follows the org
   apex CNAME. Verify the served path before requesting indexing.
