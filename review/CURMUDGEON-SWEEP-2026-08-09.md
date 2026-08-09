# Adversarial sweep: flat-earth-origins review

## The headline

The review's corrections log — the single strongest credibility asset on the site — now certifies at least two fixes that were never applied to the row they name, and one of them (the ARG-E03 originator retraction) was pasted into a neighbouring cluster instead, so the Method tab publicly retracts an attribution that the published dataset still asserts across seven rows.

That is the worst class of failure available to a project whose product is provenance, because it converts "we correct ourselves in public" from an asset into evidence that the corrections are cosmetic.

---

## FIX ORDER

Ordered by what a hostile reader meets first, then by how cheaply they can falsify it. Everything in this section is **confirmed** — each item survived an independent attempt to refute it.

### Tier 0 — the corrections mechanism itself (do this before anything else)

Nothing else on the page matters if the log is unreliable.

1. **E03 / E01 — correction applied to the wrong cluster.** `corrections.json` entry 13 says `where = "scripts/clusters.py ARG-E03 - originator_work"`. The edit landed on ARG-E01 (commit `3e5a48c`), carrying E03's justifying comment — including "item 327 traces to DeLano's blog, 18 May 2013", where item 327 is an E03 item. E03 still publishes "The Principle (film) / 2014" on all seven rows; E01 silently acquired ten changed rows with *no* log entry at all, in a log declared append-only. Fix both records, log the misfiling as a new entry, and add a regression test pinning `ARGS["ARG-E03"]["originator_year"]`.
2. **PER-ROWBOTHAM — a retracted sentence is still published.** `people.py` still prints "He took the pseudonym 'Parallax' — naming himself after the measurement he spent his life denying." That exact line was withdrawn on 2026-08-07 and the withdrawal is *rendered on the same HTML file* via the Method tab ("a neat line about a pseudonym that was simply not true"). One document, both statements.
3. **D07 — self-criticism describing a fix that has already been made.** §10 and the compression note tell the reader in the present tense that our record names Blavatsky and carries a Book of Dzyan sentence. `clusters.py` was corrected 2026-08-07; it names Hall/1928 and the Dzyan sentence is gone.
4. **D07 — the corrected originator string breaks the statistics.** `"Manly P. Hall; Helena Blavatsky"` is not a key in `build.py`'s `ORIGINATOR_PID`, so `originator_id` is `None`. Consequences: the card renders "no named originator" one line above a TLDR calling Blavatsky "the originator our record names"; `items_traceable_to_a_named_originator` = 372 while the lineage chart implies 360; the prose "89 untraced" contradicts the chart's 101. The gap is exactly D07's twelve items. One-line map fix, verified end-to-end in a scratch copy. **Add the regression test** asserting every `CLUSTERS` originator string is a key in `ORIGINATOR_PID` — that is what stops recurrence.

### Tier 1 — TLDRs, cluster names, role lines (always visible, never collapsed)

5. **A22 TLDR: "every one of them is true"** — concedes items 34/39/210, which are dome-mechanism claims and false, not merely non-discriminating. The body says only "most". The compression block quoting those items sits a short scroll below.
6. **A02 TLDR: "the one experiment on this entire list that detected something"** — false on our own data (A12 Miller, A06 Foucault, A07 ring laser, A19 gyrocompass, and Sagnac inside A02 itself), and it denies the premise A02's own closing argument runs on. Note the proposed replacement's "the only undisputed one" is *also* false; use "the one the list cites by name as its own evidence".
7. **PER-VANDERKAMP role line: "Coined 'Airy's failure'."** — `works.py` and `claude/source-genealogy.md` both mandate "earliest documented use"; the role line is the one line every People-tab reader sees.
8. **D06 TLDR** — attributes the Latin's purpose clause and "operation of Sol" sign-off to the Arabic, which §1 of the same entry says it must not; and still says the 1908 Kybalion "put the slogan into modern circulation", the exact overcredit retracted 2026-08-07.
9. **R08 cluster note: "The second-largest cluster."** — R08 has 28 items and is the largest; R06's note simultaneously claims to be "the largest single cluster" with 15. Both render.
10. **E13 TLDR** — says two items traced where the gloss, docstring and cluster note all say three; and credits the Lyman-alpha forest with breaking the void model, which the body never claims.
11. **C02 cluster record: `originator="Rob Skiba", year="2015"`** — renders as "first published by Rob Skiba". Bellarmine deploys Ecclesiastes 1:5 against Copernicus on 12 April 1615; Galileo's *Letter to Christina*, which this entry quotes, answers that argument; Schadewald documented the corpus in 1987. **Do not adopt the proposed Bouw substitution** — it repeats the error one step upstream. Either set `originator=None` (the renderer has that branch) or fix the render label so the field can honestly mean "the compilation these items were drawn from".

### Tier 2 — fabricated, misattributed or unlocatable quotations

These are the errors a defender can screenshot without leaving the page. On a provenance site they are disproportionately expensive.

12. **B05 — a paraphrase presented as an ITU quotation.** "allows engineers to plot direct wave paths as straight lines rather than calculating path curvature explicitly" is inside quotation marks, framed as the ITU's own words, and does not occur in R-HDB-54. The real §3.3 text is available and says the same thing better.
13. **C07 — Chrysostom quotation with no source and no locatable original.** "turns not, but stands firm" is not in Homily XII, not in the standard patristic-geocentrism collections, and returns nothing on exact-phrase search. The module docstring explicitly promises "every quotation below traces to an entry in `sources`". Swap in the verified "the earth is fixed, but the waters are continually in motion" and add the New Advent source.
14. **PER-VANDERKAMP legacy — "Bouw's obituary credits the coinage by name."** The obituary's only relevant sentence credits the *work* ("pioneering work in pointing out the geocentric nature of Airy's failure"), not the word. A targeted sweep for coin/termed/named/dubbed returns one unrelated hit. Same misattribution propagates to `deep.py:106` and to a **source label** at `deep.py:216`.
15. **A05 — "as wide as Saturn's orbit, on Graney and Grayson's reconstruction."** "Saturn" does not appear in arXiv 1003.4918 at all (except a bibliography entry), and Graney's unit throughout is Earth's orbit. Two occurrences. A fabricated quantitative attribution to a named living scholar.
16. **A03 passage — work/quote mismatch.** The block renders the Sungenis & Bennett sentence under "De Labore Solis, 1988 … p. 52", with our own gloss one line below saying it came from a different book by different authors. The quote itself is genuine (located at scan p. 853). **Do not use the proposed `p. 249` locator** — the quote is roughly 590 pages from there.
17. **E13 sources — "searched; contains none of these six topics"** on the Sungenis 2011 NPA paper, which carries the supernova-void alternative at length, quoting Clifton and Ellis. The correction runs in our favour (a second ancestor for item 334).
18. **C04 — "worthy of all commendation…" attributed to Aquinas.** They are Augustine's words, reported by Aquinas, and we truncate "and believed" without ellipsis.

### Tier 3 — false claims about what a source does or does not contain

The single most recurrent failure mode in this sweep. See PATTERN below.

19. **A05 refutation — "No experiment follows. No apparatus…"** Rowbotham describes the apparatus in full seven pages earlier in the same chapter (two six-foot bored tubes "one yard asunder", parallel axes, two observers, knock signals). One yard is three feet. The false claim appears **six times**, including TLDR and verdict. The true refutation is stronger: the rig is ~13 orders of magnitude too coarse to resolve the angle, so its "distinct period of time" measures the misalignment of its own tubes. (Fix the proposed replacement's "ten orders of magnitude" — it is thirteen.)
20. **PER-ROWBOTHAM `ignored` — "He did not engage it."** The 3rd ed. General Index lists "Stars, north and south, motion of [284]" and "Southern Cross [287]"; za48.htm argues the point for six pages citing Ross, Humboldt, von Spix and von Martius. He engaged it and disqualified the witnesses — which is a *better* finding. Same field files refraction under `ignored` when his index shows experiments at pp. 31–36 and our own ARG-B04 says he "concedes refraction outright, quantifies it, applies it".
21. **PER-VANDERKAMP `ignored` — "passed over stellar aberration."** *De Labore Solis*, the only work on his card, is a book about stellar aberration. The card also renders ARG-A04 ("Stellar aberration is optical/parallax…") under "Arguments originating here". The field's rendered heading is "This is the difference between being wrong and being unserious."
22. **A03 refutation — "On a stationary Earth there is no relative velocity…"** Van der Kamp's dome revolves; he has a positive (wrong) account of aberration and shrank the universe to 60 light-days to keep it sub-luminal — recorded in the Bouw obituary *we already link*. Our "this is the step the argument never takes" is false of a book with a chapter titled after that step. (Also: the proposed replacement miscites de Sitter 1913.)
23. **R08 — "They do not cite GPS… no instrument is named at all."** Vol. II ch. 10 has a subsection "Global Positioning System: Claims and Responses" at p. 204. **Caveat:** the corroborating 2010 Plait-reply quotation could not be verified this pass (search budget exhausted) — fix using the ch. 10 heading alone and do not publish the unverified quote.
24. **B04 gloss — "none of them is in Rowbotham."** Proof 63's telescope claim is in Rowbotham 1881 ch. XIV, *with a calm-water condition Carpenter drops and the TFES wiki still omits*. That is the best `hedge_dropped` specimen in the cluster and we currently miss it.
25. **R06 — "not located in the scanned text of Vol. I."** The scan searched is Vol. II, chs 7–13. The volume our cluster record names was never searched. Our headline provenance finding names the wrong volume.
26. **C04 gloss — "we have no evidence that he did."** Skiba's own document names Schadewald, gives the copyright line, block-quotes several paragraphs and tells readers to go read it. ARG-C05 already says so and cross-references C04 for the opposite. Fixing C04 requires revising C05's finding 2 in the same pass.

### Tier 4 — physics and arithmetic errors

27. **Foucault precession given as `2Ωsinφ`** in **both A10 and A22**. The rate is `Ωsinφ`; `2Ωsinφ` is the Coriolis parameter. A22 line 341 is self-refuting — it quotes the correct 11.3°/hr and attributes it to a formula yielding 22.7. **Do not global-replace:** A10 line 365 uses `f = 2Ωsinφ` correctly, for air deflection.
28. **B04 — "the 491-foot curvature term."** 491 ft is the curvature drop *less the light's own 150 ft*, as six rows of Rowbotham's own table confirm. Curvature term is ~641 ft; one-seventh is ~90 not 70; the strong-refraction day is ~130 not "more than 90"; "five times too small" should be about seven. This is in the paragraph headed "The source contains the correction. This is the finding."
29. **B01 — "It never meant 'planar'."** Etymonline gives "having an even surface" from early 15c and "lying in the same horizontal plane" from the 1550s. Contradicts our own steelman *and* section 3 of the same refutation, which charges equivocation between two senses one of which the paragraph says never existed.

### Tier 5 — bibliographic labels (systemic, low individual impact)

30. **The Vol. I / Vol. II mislabel of archive item `…Bennett4276`** — live at A02 (locator + sources), R01 (sources), R06 (locator + sources + straw_man + compression + cluster record), C07 (impossible "Vol. III, 2006" pairing, ten CSV rows), E13 (work record imprint), and the `WRK-SUNGENIS-2006` imprint itself ("Vol. II historical; 10th ed. 2013" — it is chs 7–13, technical, 7th ed.). **Fix the work record first**, then the citations, or you rearm the trap for the next entry.
31. **R01 — eight items dated to a 1968 booklet nobody has read** while every quotation comes from the 1988 book. Fourth instance of the failure class already logged three times.

---

## Confirmed vs. unverified — the line

**Confirmed (39 findings).** Everything numbered above. Each was re-checked against the primary source, or against repo state where the claim was about repo state, by an agent instructed to refute it. Several were downgraded in the process (14 of 39 came back below the severity first assigned), and three had their proposed *fixes* rejected as introducing new errors — noted inline at items 6, 11, 16, 19, 22, 23.

**Unverified leads (~90 findings, moderate and minor).** These were **not** independently checked. They are listed in the raw output but should be treated as hypotheses. Several look strong and cheap — the A02 candour gap about never having reached the Sungenis body text at sentence level; the E17 steelman missing Ellis's own 1995 *Scientific American* concession, which is the single most-circulated sentence supporting that cluster; the B04 quotation that starts one sentence too late and thereby hides the source's own care; the E13 `147 Mpc` radius-vs-diameter slip. Others may dissolve on contact. **Do not act on any of them without verifying first.** Three of the confirmed findings above began life as moderate leads and grew; at least as many confirmed findings had their supporting evidence partly refuted.

A specific caution: several unverified leads propose replacement text containing *new* factual claims (the C04 `real_source` rewrite, the E17 Ellis material, the R08 Kind-8 ground-track paragraph). Those replacements need the same verification as the findings.

---

## PATTERNS

Four, and they matter more than the individual items because they predict where the 77 unaudited arguments are also wrong.

**1. Asserting absence from a source on the strength of one passage.** By far the dominant failure. Confirmed at A05 ("no apparatus"), R08 ("they do not cite GPS"), B04 ("none of them is in Rowbotham"), C04 ("no evidence he did"), E13 ("contains none of these six topics"), PER-ROWBOTHAM ("he did not engage it"), PER-VANDERKAMP ("passed over aberration"), R06 (wrong volume searched), A03 ("the step the argument never takes"). `corrections.json` already logs this class three times. **The rule that would have caught all nine: never write "the source does not contain X"; write "X is not located in [the specific text searched]".** R06 already discovered this formulation and then failed to apply it to itself. Suggest making it a lint check on the corpus for `never|nowhere|no .* at all|does not cite|did not engage`.

**2. TLDRs that overstate or contradict their own bodies.** A22 ("every one of them is true" vs body's "most"), A02 (uniqueness claim vs own closing argument), E13 (two vs three; Lyman-alpha), D06 (Arabic grammar; retracted Kybalion credit), E03 ("our own velocity" stated as settled where body hedges), B01 ("gravitational potential" where the refutation correctly says gravity potential), B04 ("7/6 … radio engineers"). The TLDR is written last, from memory of the argument rather than from the argument, and nothing tests it against the body. **Cheapest systemic fix on this list:** a build-time check that the TLDR's quantifiers and counts agree with the compression block's tallies.

**3. Edition and volume dating.** Six confirmed instances plus the whole of Tier 5. Two sub-traps: Rowbotham 1865 vs the enlarged 1881 third edition (A05, A10, B01, B04), and Sungenis Vol. I vs Vol. II vs the 7th-ed-2013 three-volume rearrangement (A02, R01, R06, C07, E13, `works.py`). The Sungenis one is a single bad work record propagating to six entries.

**4. Self-criticism written in the future tense and never converted.** D07 §10 and its compression note, E03's announced works.py fixes, C07's three diagnosed-but-unapplied record errors, R06's retired-but-still-published caveat, A10's stale compression note, the batch-7 commit message listing fixes under "Still to apply". The pattern is: an agent finds a defect, writes an accurate paragraph *recommending* the fix, and ships the recommendation as prose. A commit-message TODO is invisible to a reader of the published page. **Suggest a convention: findings about our own record are written in past tense after the edit lands, or not at all.**

---

## What this sweep did NOT cover

State this plainly, because the coverage is thin.

- **21 of 98 arguments were reviewed.** The other 77 have no full treatment and were not examined at all — not their verdicts, not their citations, not their cluster records. Given pattern 1 above, expect absence-claims in them at roughly the rate found here.
- **2 of 19 biographies were reviewed** (PER-ROWBOTHAM, PER-VANDERKAMP). The other 17 are stubs and were untouched. Both reviewed biographies came back with critical findings; that is a 100% hit rate on a sample of two, and the stubs are not obviously safer.
- **Moderate and minor findings were not verified**, as stated above. ~90 of them.
- **No verdict was challenged.** Not one of the 21 targets produced a proposal to change a verdict. Every REFUTED, MISLEADING, UNFALSIFIABLE, NOT DEMONSTRATED and STANDARD PHYSICS call examined survived. That is genuinely reassuring about the analysis and says nothing about the 77 unexamined ones.
- **Several checks failed for access rather than for substance** and are recorded as unknown, not clean: the Sungenis body text was never reached at sentence level on any pass (three archive copies, four routes — so A02's six verbatim excerpts remain unverified transcriptions); the R08 Plait reply; the English tracing-board rituals for D07; Schadewald's *Plane Truth* ch. 1; several R06 term counts. Web-search budget was exhausted mid-sweep on at least three targets.
- **The hedge rule was recorded as failing on 9 of 21 targets** (A02, A03, A22, C02, E01, E17, R08, and both biographies) — i.e. the refutation aims at the list's compressed fragment rather than at the source's hedged claim. That is the rule the project exists to enforce.

---

## Is the review in good shape?

Mostly yes on substance, and not yet on discipline.

The physics is in genuinely good condition. I recomputed dozens of figures across A02, A05, A10, A22, B01, B04, B05, E03, E13 and R06 — Michelson–Gale's 0.236 vs 0.230, the Sagnac arithmetic, Ashby's 207.4 ns, WGS 84's defining constants, the Planck dipole chain, the BAO and kSZ void exclusions, the Suez sagitta, the Gotthard closure — and found two errors, both the same Foucault factor-of-two. The steelmen are real: C07, C02, E13, E17, R01 and B01 all state the opposing case at a strength that would satisfy its holders, and several concede more than they had to. No verdict moved. The four-tier severity discipline held up: reviewers downgraded their own findings more often than they inflated them, and rejected three proposed fixes for introducing fresh errors.

What is not in good shape is everything *around* the arguments — the corrections log, the cluster records, the source labels, the work records, the biographies, and the TLDRs. That is precisely the layer this project sells. A reader who never opens a `<details>` block meets only cluster names, TLDRs and role lines, and those are where the confirmed error density is highest. A reader who does open one and clicks a source link lands, on six entries, on a title page reading "Volume II, Seventh edition, 2013" under a label saying "Vol. I (2006)".

The most damaging thing found is not any single error. It is that the mechanism designed to catch errors — the public corrections log — is itself carrying two false entries and a misapplied edit. Fix Tier 0 before touching anything else; the rest of this list is worth much less if the log cannot be trusted.

One thing worth saying in the review's favour: nearly every confirmed finding here was refutable *from the review's own files*. The project knows about the Vol. II identity, knows Skiba quotes Schadewald, knows Rowbotham conceded refraction, knows the pseudonym line was withdrawn. The information is present and correctly stated somewhere on the page. It is the propagation that fails, not the research.