# Batch 8 adversarial sweep — operator report

**Every one of the 15 confirmed defects is in the sourcing and attribution layer around the arguments; not one is a defect in the reasoning, the physics, or a verdict — which on a project whose product *is* provenance is the worst place for them to be.**

---

## 1. Did the new rules work?

Partly. The rule that was written down and mechanically checkable held perfectly. The rules that depend on the writer's judgement did not.

| | Sweep 1 (23 targets) | Sweep 8 (12 targets) |
|---|---|---|
| Raised | 214 (9.3/target) | 111 (9.25/target) |
| Confirmed | 45 (1.96/target) | 15 (1.25/target) |
| Confirmation rate of raised | 21.0% | 13.5% |
| Hedge-rule failures | 9 of 21 | **0 of 12** |
| Criticals surviving at critical | 0 | 0 |

**Confirmed defects per target fell 36%.** That is real improvement, not noise: the raise rate per target is essentially identical (9.3 vs 9.25), so the reviewers were looking just as hard and finding less that survived a refutation attempt.

The hedge rule is the unambiguous win: 9 of 21 → 0 of 12, and it held under adversarial pressure — D11, B06, B08 and R03 all answer their sources' own strongest text rather than the list's fragments, and two entries (D08, R04) reach genuine kernel-tier steelmen.

The new rules are the honest disappointment: **4 of 12 targets (33%) failed them** — D04, D13, A07, R04 — and the failure mode is instructive. In every case the unscoped absence claim had *migrated into a field the ratcheting test does not scan*: `compression.note` (A07, D13), a cluster note (B06), a whole-literature claim phrased as "nobody has produced" (R04), "did not treat" (D04). The test scans `tldr`, `refutation`, `untraceable`, `passage.gloss` and matches a "does not contain / never mentions / is absent from" regex. Writers have learned the regex, not the rule. Two mechanical fixes follow: extend `_blocks` to `compression.note` and the cluster `note` field, and add `\bnobody (?:has|in)\b`, `\bno one has\b`, `\bdid not treat\b` to `_ABSENCE`.

Also worth noting on severity: 9 of the 15 confirmed were raised as major and downgraded to moderate on verification. The raise-then-verify loop is doing calibration work, not just filtering.

---

## 2. Fix order, weighted by reader impact

**Tier 1 — rendered before a reader expands anything (TLDR, cluster note, meta line, published dataset). Fix these first regardless of severity label.**

1. **D13 gloss** — "Rick DeLano produced the film with Sungenis, who co-wrote it". False about a named living man's authorship; Variety's credit block, which we cite three inches away, reads *Screenplay by Rick DeLano*, Sungenis executive producer. Fix the gloss and the `_b8_D13.py` docstring in the same pass. Do **not** apply the proposed `originator` change on this evidence.
2. **A07 `clusters.py` note** — publishes the "$20,000" figure the gloss says it is deliberately withholding, and frames Knodel's shielding run as refusal while the refutation credits it as a control. Self-contradiction about a living person on the most screenshottable line on the board. Minimal fix: strike `$20,000`, keep the rest; do not adopt the proposed replacement, which states the shielding-run outcome unhedged where the body hedges it.
3. **A09 TLDR** — "pressure on the Pacific sea floor". Gross 2000 does not contain the word "Pacific". Invented geographic specific adjacent to a named citation, in the field most readers never expand past. Two-word fix; the entry's own verdict paragraph already has the correct wording.
4. **D11 TLDR** — "a table he copied from an encyclopaedia". False, one click from our own source list, and repeated in `people.py`, `_b6_B01.py`, `_b6_B04.py` and `clusters.py`. Fix corpus-wide. Do not take the proposed "at the same canal" clause; the 1849 pamphlet's venue is the New Bedford, the 1881 book's Experiment 1 is the Old Bedford.
5. **B06 `clusters.py` record** — `year="1849"` publishes into five dataset rows (items 47, 223, 382, 383, 395) that the treatment rendered directly below contradicts twice. Anchor the edit on the cluster key, never on the `originator=` line — that line is byte-identical across B02, B06, B07 and D12, which is exactly how the E01/E03 misfile was manufactured. Hedge the item-383/Carpenter inference; use the house title form *Earth Not a Globe*.
6. **B08 gloss** — "the northern half of the cluster is inherited" positively asserts the southern half is not. Rowbotham 1881 (za48.htm, "Motion of Stars North and South") carries the southern-pole denial, the simultaneity objection in Dubay's own comparative form, and the perspective reply. Genealogy is the deliverable; this is the field a defender quotes. Add PER-ROWBOTHAM to `people`.
7. **D02 gloss, opening paragraph** — "the Sun some 93 million miles off" inside "everything Galileo's model contained". First paragraph after the quote. Take the nine-word strike, not the proposed three-sentence excursus on the history of the astronomical unit.

**Tier 2 — body prose, real but reached only by readers who expand.**

8. **D11 §3(c)** — sun at 3,000 miles (it is <4,000 in 1865, 700 in 1881) and the Britannica misattributed as the source of the 8-inch table (its actual citation is refraction, at p. 34 — the ARG-B07 hinge). Both proposed replacements need editing: the first double-predicates; the second asserts Rowbotham took his coefficient from Britannica, which ARG-B07 itself refutes.
9. **C08 `untraceable`** — the false absence claim about Hall's solar chapter, sitting in the block that invites readers to check us. Correct the docstring slug sta12 → sta11. Strike the Dupuis attribution from the proposed replacement; Hall credits an anonymous Balliol treatise.
10. **R04 gloss** — the 2006/2013 chapter mapping is wrong and contradicts our own ARG-E13. 2006 Vol. I ch. 10 → 2013 Vol. II ch. **9**; 2013 Vol. II ch. 10 is a different chapter descending from 2006 ch. 12.
11. **D02 §4 and sources[5]** — the "globe placed in the centre of the heavens" sentence is Jowett's introduction, not the *Phaedo*. Drop the proposed claim that Perseus is robots-blocked; it is reachable.
12. **D02 §6 / gloss §3** — Schadewald is a critic of geocentrism; his equivalence sentence is not an inside-the-tradition concession, and "two of them from inside the tradition" is false. Fix both fields plus the preceding clause.
13. **D08 §7** — "revolving heavens" is asserted by both models; our own corpus carries "Precession from dome rotation". The same defect recurs at §9 and in `why_it_doesnt_save_claim`; fixing §7 alone leaves the knockdown available.
14. **A07 `compression.note`** — "nobody in its own lineage is on record obtaining", contradicted by our own gloss and our own steelman. Rescope using the entry's existing formula ("the sequences the press transcriptions cover"), not the proposed "not in the film".

---

## 3. Patterns — where the 65 unwritten arguments will break

These repeat across enough targets to be predictive:

**A. Secondary sources retro-fitted onto primary ones.** The single largest class. Rowbotham's sun height taken from a modern flat-earth figure via Wikipedia (D11); Sungenis's screenplay credit from Wikipedia's loose prose against a credit block (D13); Jowett's editorial summary quoted as Plato (D02); a debunker's assessment quoted as the movement's concession (D02); the Britannica credited for the wrong thing (D11); Manly Hall's chapter cited by the wrong slug (C08). **Predicted failure in unwritten entries: any claim about what a primary source says that was not verified against the specific edition named in the locator.**

**B. Rowbotham's 1881 third edition is the systematic blind spot.** B06 (1849 vs 1865), B08 (southern strand present in 1881), D11 (two editions conflated, both misquoted), and the already-logged A05/B04/B01 corrections. Any B- or D-lane entry touching *Zetetic Astronomy* should be assumed edition-confused until checked. za48.htm and the General Index at za68.htm settle most of it in minutes.

**C. `clusters.py` renders into the entry and contradicts it.** B06 (year), A07 (the `$20,000` note), B08 (`people[]`, `originator`), R03 (`real_source=None`), D04 (stale docstring claiming an unfixed field). The writing agents do not own that file, report the defect to the parent, and the parent does not apply it. This is the E03 pattern — "recorded, NOT ACTUALLY APPLIED" — for at least the fourth time. It is a process failure, not a writing failure, and it is the highest-leverage thing to fix, because those fields render into the summary line next to the verdict chip.

**D. TLDRs written from memory of the argument.** A09 ("points the same way everywhere" is true of the globe too), A07 (asserts an axis-dependent match the body says it cannot establish), R04 ("whole content is the word *local*" vs the body's "both *operative* clauses"), D04, C08. The TLDR is systematically stronger than the body it summarises.

**E. Fields the ratchet does not scan absorb the banned constructions.** See §1. Structural, and cheap to close.

---

## 4. What this did not cover

- **65 of 98 arguments have no treatment at all.** These twelve plus the first sweep's 23 are 33 of 98. Nothing here says anything about the other two-thirds.
- **17 of 19 biographies are stubs.** Untouched. The B08 finding (PER-ROWBOTHAM missing from a cluster whose argument he originated) is exactly the kind of defect that lives in that gap.
- **Moderate and minor findings went unverified.** Roughly 80 entries in the leads array. They are leads, not conclusions — treat the recommended replacement text in them as a starting draft, not a patch. Verification changed the recommended fix in most of the 15 that *were* checked.
- **Per-target summaries name defects that are not in the confirmed set.** B06's summary asserts a major about a galileolied.com calculation; R03's asserts two majors (van der Kamp's actual position, a question-begging §7); A09's sets `holds=false` on a verdict challenge. None of those appear in the confirmed list. They either failed verification or were never put through it. Do not treat the summaries as findings.
- **Verification was one adversarial pass per finding.** It killed roughly 87% of what was raised, which is a good sign for the survivors, but nothing here has been checked twice.
- **A09's verdict is live.** The reviewer filed a verdict challenge (the six items do not share a fate; the seven-orders-of-magnitude calculation refutes 56 and 113 but 214 is a 2006 attribution for a claim about consumer drones) and the auditor endorsed it. That needs a decision, and it is the only verdict on this board that is contested.

---

## 5. Are these twelve in good shape?

Yes, with one qualification I would not soften.

The arguments are sound. Twelve for twelve on the hedge rule, two kernel-tier steelmen, and under sustained attempts at refutation not a single verdict fell and not a single piece of reasoning or physics was shown wrong — the arithmetic that was re-derived (B08's geometry, A09's seven orders of magnitude and drone numbers, R04's 0.13 m and 27 orders, A07's 348.6 Hz Sagnac beat) all held. Compared with sweep 1 this is a different quality of work.

The qualification: **10 of 12 carry at least one confirmed defect, and every one of those defects is a provenance error.** Wrong number attributed to a named primary source. Editor's summary quoted as the author. Critic quoted as adherent. Wrong chapter, wrong edition, wrong screenplay credit, wrong basin, invented encyclopaedia. On any other project these would be footnote-grade. On this one they are the product failing at the exact thing it convicts its subject of, and each is checkable by a hostile reader in under two minutes from a link we ourselves supply.

Neither of the two clean targets is unambiguously clean either: D04 failed the new rules, and R03's per-target summary claims two majors that did not survive to the confirmed list.

So: ship-quality reasoning, not-yet-ship-quality citation hygiene. Tier 1 is seven edits and closes the reader-facing exposure. The pattern work in §3 — particularly the `clusters.py` application gap and the Rowbotham edition audit — is what stops sweep 9 from reading like this one.