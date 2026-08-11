# Scoped curmudgeon pass — the nineteen biographies (planned 2026-08-11, to run off-peak)

Nineteen biographies (~40,000 words about real people) shipped in commit `826ca7b`
with **no adversarial review**. `tests/run.sh` and `tests/canary.py` verified the
machinery, not the claims: they catch a CDATA wrapper, not a wrong death date.

The prior sweeps were file-scoped on one argument + its primary source. Nineteen
biographies are not that shape, and a flat sweep would mostly re-read Wikipedia,
which is the tier most of these sources sit at. So this is scoped by risk.

## Lane 1 — full curmudgeon, seven targets

Run `review/curmudgeon.md` verbatim, including its **Biography targets** section.
One agent per target, then adversarial verification of every `major`/`critical`.

BLP surface — living, or death not established:

| target | why |
|---|---|
| `PER-DUBAY` | living |
| `PER-SARGENT` | living |
| `PER-SUNGENIS` | living |
| `PER-MARSHALLHALL` | death **not established** — the bio's own agent found "1931–2013" rests on a fixedearth.com retrieval, not an obituary |
| `PER-SKIBA` | d. 2021, "recently-living" per the spec |

Biography contradicts the argument record — these move published figures:

| target | contradiction |
|---|---|
| `PER-WINSHIP` | bio locates item 31 to Winship 1899; `clusters.py` B10 still credits Rowbotham 1865 |
| `PER-VOLIVA` | both originator credits under challenge; if both fall he originates nothing, and the traced/untraced split moves |

## Lane 2 — citation existence only, twelve targets

`PER-ROWBOTHAM` `PER-VANDERKAMP` `PER-CARPENTER` `PER-JOHNSON` `PER-KNODEL`
`PER-BOUW` `PER-BLAVATSKY` `PER-HALL` `PER-ATKINSON` `PER-ELIADE` `PER-PTOLEMY`
`PER-SHENTON`

Mechanical, batched: does each source URL resolve, is it the edition claimed, and
does the specific assertion attributed to it actually appear there. No steelman,
no advocate mode. Three agents, four people each.

## Known inputs, do not re-derive

`review/records-and-bios-2026-08-11.json` already holds **93 source conflicts** and
**100 record problems** the bio agents self-reported. Read it first — a finding
already in there is not a new finding, and the 32 operator-held record decisions
are not the reviewer's to settle.

## Why not review all nineteen

Cost, and the agents were held to the scoped-absence rule and largely complied
(Voliva's named the four catalogues searched and the two it could not reach).
The material is already live, so this is a correction pass, not a gate — which is
an argument for scoping it, not for skipping it.
