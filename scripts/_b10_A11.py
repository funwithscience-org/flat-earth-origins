# -*- coding: utf-8 -*-
"""Batch 10 — A11. "Michelson-Pease null rotation detection."

ONE item, not three: item 10, "Michelson–Pease null rotation detection." Cluster verdict
STANDARD PHYSICS. A verdict_challenge IS filed — SELF-CONTRADICTED — see note 9; it turns
on a fact about the source, not on the physics, and the refutation stands under either
verdict.

Research notes for whoever picks this up next.

1. THE COUNT IS WRONG IN THE BATCH METADATA, NOT IN THE DATASET. This target was handed
   over as "3 items". `assign.py` maps exactly one item to A11 (item 10) and
   `review/triage.json` records `"items": 1`. Nothing here is written as if there were
   three. Reported up; not edited (this agent owns one file).

2. THE FINDING, AND IT IS THE WHOLE ENTRY. The list calls the 1929 experiment a NULL. The
   text our record names as its origin says the opposite in terms. Galileo Was Wrong
   Vol. I, ch. 6 ("What Did Michelson-Morley Actually Demonstrate?"), at printed p. 387 of
   the archive.org OCR:

     "In fact, Michelson proved this in two ways. The first was by the Michelson-Gale
      experiment in 1925 that measured the same absolute motion that Sagnac discovered in
      1913; the second, by the Michelson-Pease-Pearson experiment which showed an ether
      drift against the Earth, and that the speed of light was affected by it."

   And at p. 386: "Thus, it is no surprise that, in this third try, Michelson indeed found
   significant fringe shifting". The ONE place in the reachable text where the book uses
   the word "null" of this experiment is p. 353 — "declared again that he produced a
   'null' result" — and the word is inside the book's own scare quotes, in a paragraph
   whose next thirty pages argue that it was not one. So the compressed item is not a
   hardened version of the source. It is the source's opposite, and it agrees with the
   physics literature the source is attacking. drift_type = reversed. Note in passing
   that the seventh edition hardens ONE sentence of the surrounding argument on its own:
   2006 reads "the news that the Earth may not be moving at all", the 7th-ed scan reads
   "the news that the Earth is not moving at all". One word, in two OCR texts, neither
   checked against print — say it that carefully or not at all.

3. THE CHAIN, FULLY DOCUMENTED, FIVE LINKS. (a) Michelson, Pease & Pearson, "Repetition
   of the Michelson-Morley Experiment", Nature 123:88 (19 Jan 1929) and J. Opt. Soc. Am.
   18(3):181 (Mar 1929). (b) Hector Munera, Apeiron 5(1-2):45-48 (1998), who rereads the
   classic nulls as small positives. (c) James DeMeo, "Dayton Miller's Ether-Drift
   Experiments: A Fresh Look" (orgonelab.org/miller.htm), whose three-experiment
   narrative, figures and captions Sungenis follows almost sentence for sentence — the
   book cites "DeMeo, p. 17" and "p. 18" in its own footnotes 751 and 754. (d) Sungenis &
   Bennett 2006, which imports DeMeo's reading into the geocentric canon and adds the
   motive claims DeMeo does not make. (e) item 10. DeMeo is not a geocentrist; he is an
   orgone researcher defending Miller. The geocentric content is added at link (d), which
   is why the originator field is defensible as it stands. A keyword search of the
   De Labore Solis PDF at geocentricity.com (van der Kamp 1988) returned zero hits for
   "Pease" and zero for "Pearson" on 2026-08-10; Bouw's Geocentricity (1992) was not
   reachable, so the origination claim is "earliest located", not "first".

4. THE ERROR THAT DOES ALL THE WORK IS A SQUARE ROOT. The reported sentence is a BOUND:
   "The results gave no displacement as great as one-fifteenth of that to be expected on
   the supposition of an effect due to a motion of the solar system of three hundred
   kilometers per second." DeMeo converts it as "One fifteenth of 300 km/sec. is 20
   km/sec." and captions his figure "their successful detection of an ether-drift of some
   unspecified quantity just under 20 km/sec." Sungenis reproduces the arithmetic on p. 387, not p.
   386 as this file previously said — the paragraph begins at the foot of 386 and the
   division sentence falls on 387; page markers in this OCR sit at the FOOT of their page,
   verified across the 384-388 run — and matches it to Kennedy-Thorndike's 10 +/- 10 km/s.
   But the Michelson-Morley
   fringe shift goes as v^2, so a shift one-fifteenth of the shift expected for 300 km/s
   bounds the speed at 300/sqrt(15) = 77.5 km/s, not 300/15 = 20. The book's OWN footnote
   689 quotes Munera doing it correctly — "the corresponding solar velocity is then
   300(1/15)^{1/2} = 77.5 km/s" — and its footnote 759 passes on Galaev's 6,000 m/s, which
   is 300/50 done linearly again. Three velocities for one sentence, in one chapter, from
   three cited authorities, and the book reconciles none of them. Two separate defects
   there: the linear conversion, and the conversion of an upper limit into a measurement.
   The second is the one that matters and it needs no physics to see.

5. THE 1/15 vs 1/50 QUESTION IS NOT SETTLED THE WAY THE BOOK SETTLES IT — AND NOT THE WAY
   AN EARLIER DRAFT OF THIS ENTRY SETTLED IT EITHER. Footnote 753
   says "Some commentaries say the multiplier was one-fiftieth as opposed to one-fifteenth,
   but the former appears to be in error." Swenson, The Ethereal Aether (1972), p. 222,
   reports that both figures are in print, one in each paper, and his sentence runs on past
   the point this entry used to cut it: "Later, in March, the Journal of the Optical Society
   of America reported that nothing was observed within one-fiftieth of the expected shift,
   based on Sternberg's estimate of the solar system's resultant velocity of about three
   thousand kilometers per second." That trailing clause gives the JOSA ratio a DIFFERENT
   velocity basis from the 300 km/s the Nature sentence names, and Munera's 42.4 km/s for
   the JOSA printing is 300/sqrt(50), i.e. it carries the Nature basis across. So Swenson
   and Munera do not in fact "say the same thing", as this file previously asserted.
   Three further cautions for whoever gets the printings. (i) "Sternberg" is almost
   certainly Gustaf Stromberg, the Mount Wilson astronomer Swenson names at p. 221 as
   having set the observing schedule with Miller; quoted as printed here, without
   correction. (ii) "three thousand" may itself be Swenson's slip for three hundred —
   300/sqrt(50) = 42.4 is exactly Munera's figure, which is suggestive but proves nothing.
   (iii) NEITHER 1929 PRINTING WAS REACHED, so this page does not adjudicate; the refutation
   says so in the same paragraph and nothing on the page turns on the answer. Swenson then asks whether the difference
   was "simply a refinement of the data ... or a change in judgment", answers that "to most
   physicists these figures were clearly null results either way", and adds that "Miller or
   his partisans could capitalize on such discrepancies" — written in 1972, twenty-six
   years before Munera and thirty-four before Sungenis.

6. THE ALTITUDE PREMISE IS FALSE, AND IT IS LOAD-BEARING. Sungenis, p. 386: the third run
   went to a "well-sheltered basement room of the Mount Wilson laboratory", and "This
   higher altitude and longer light-path came closer to Miller's specifications. Thus, it
   is no surprise that ... Michelson indeed found significant fringe shifting." Swenson,
   pp. 220-221: the apparatus lived in the Mount Wilson Observatory's PASADENA optical
   shops, built on the 7,000-pound cast-iron bedplate used to polish the 100-inch Hooker
   mirror, and "in the summer of 1928, they removed the superstructure and put the basic
   apparatus in a well of the Pasadena Laboratory", enlarging the path to eighty-five feet.
   The instrument went up the mountain in the SUMMER OF 1930, into the base of the
   100-inch telescope (Swenson p. 225) — eighteen months after the paper. AND NO RESULT
   FROM THAT INSTALLATION IS REPORTED IN SWENSON'S ACCOUNT OF IT; his note 29 on the same
   page cites January 1930 correspondence (Gale to Adams) "indicat[ing] that Michelson had
   lost interest by then and that the latest observational data was not suitable for
   publication". That correspondence PREDATES the summer move, so it is context and not a
   report on the mountain data — do not let a future edit turn it into one. What it does
   mean is that the mountain run cannot be quoted against Miller by either side, and the
   steelman answer now concedes that before naming Joos as the replication that does the
   work (Swenson p. 226: the Jena instrument was built "in direct response to Miller's 1925
   announcement" and reported in September 1930 after a year's running). So "the Mount
   Wilson laboratory" is the observatory's Pasadena laboratory, at roughly 250 m, not the
   1,742 m summit. The longer light path is real; the altitude is not. Careful with this
   one in both directions: it also means the 1928 run WAS the most shielded, lowest
   configuration in the series, which is a point for the defender and is conceded in the
   advocate block.

7. THE ARITHMETIC, ALL OF IT REPRODUCED HERE 2026-08-10 (lambda = 570 nm,
   Omega = 7.292115e-5 rad/s, R = 6.371e6 m, c = 2.99792458e8 m/s, fringes =
   2 L v^2 / (lambda c^2)):
   (a) Sanity check on the published expectation. L = 25.9 m (85 ft), v = 30 km/s ->
       0.910 fringes. Matches the 0.9 in Wikipedia's comparison table and in our own
       cluster note, so the table's "arm length 25.9 m" is the one-way path.
   (b) The bound. 0.01 fringe at that path length -> v <= 3.1 km/s.
   (c) ROTATION. Surface speed at Pasadena (lat 34.15 deg) = Omega R cos(lat) = 384.5 m/s;
       at the Mount Wilson summit, 384.1 m/s. Fringe shift for 384.5 m/s at L = 25.9 m =
       1.49e-4 fringes — about 1/67 of the 0.01-fringe bound. An instrument of this design
       could not have detected the Earth's rotation on ANY cosmology.
   (d) Why: a Michelson interferometer's two beams retrace their own paths, so the closed
       circuit they form encloses no area and the first-order rotation (Sagnac) term
       cancels. That is exactly why Michelson, who proposed a rotation experiment in
       Phil. Mag. 8:716 (1904), did not use this instrument for it in 1925 but laid out an
       evacuated rectangle 2010 x 1113 ft = 0.208 km^2. Recomputed:
       4 A Omega sin(41 deg 46') / (lambda c) = 0.2363, against the published prediction
       0.236 +/- 0.002 and observation 0.230 +/- 0.005.
   (e) The geocentric explanation's own magnitude problem. Footnote 752 says "it is
       precisely the rotation of the ether every 24 hours that accounts for the small
       positive results of all the interferometer experiments at the surface of the Earth."
       An ether rigidly circling a fixed Earth once a sidereal day streams past Pasadena at
       the same 384.5 m/s — the relative velocity is identical, which is the point — so it
       predicts the same 1.5e-4 fringes. Against Miller's claimed ~10 km/s that is short by
       (10000/384.5)^2 = 676 in fringe shift; against the book's own inferred 20 km/s, by
       2,705.

8. WHAT MICHELSON ACTUALLY DID WITH THE RESULT. He held a press conference. Swenson p. 222
   quotes the New York Times of 3 Nov 1928: "the results of my experiment conducted with
   greater scientific care, improved apparatus and refined technique, with the intention of
   eliminating every possible source of error, are again negative.... It is for physicists
   to study and explain these results and reconcile them with the existence of the
   hypothetical ether." Miller was in the room and conceded that periodic temperature
   fluctuations might explain his own positives, while maintaining them. That is the
   answer to "Michelson obfuscates his results" and to "too blinded by whatever was
   prohibiting him from telling the whole truth" — and it is better than an argument,
   because it is the man's own words at the moment in question.

9. THE VERDICT CHALLENGE. STANDARD PHYSICS is not wrong about the experiment: a
   Michelson-Morley repeat returning a limit is real, explained and non-discriminating,
   which is exactly A01's status and why the cluster note points there. But it misses what
   is actually true of THIS item, and the rubric has a value for it:
   SELF-CONTRADICTED — "the claim's own source, or another item on the same list, points
   the other way." The claim's own source does point the other way, at p. 387, in a
   sentence with no hedge in it. The challenge is filed with its own weak point named: it
   depends on the originator attribution, and the specimen carries no citations, so we
   cannot show which text the compiler read. If an operator judges that too thin to carry
   "the claim's own source", STANDARD PHYSICS should stay and nothing else in this entry
   changes. Do not resolve it by weakening the refutation, which answers both readings.

10. QUOTE PROVENANCE AND THE LIMITS OF THIS PASS.
   - Book quotations: archive.org OCR of item `GallileoWasWrong`, whose title page is
     Vol. I, The Scientific Evidence. Printed pages as they appear in that OCR: the
     "null" mention at 353, the three-experiment narrative at 385-386, Michelson's quoted
     paragraph at 386, the "two ways" sentence at 387, footnotes 689 / 751-755 at the feet
     of those pages. Cross-read against the seventh-edition scan
     (`galileo-was-wrong-the-church-was-right-sungenis-vol-1-3-complete`), where the same
     material sits in "Chapter 5: More Experiments Point to Geocentrism" around printed
     p. 662; the sentences quoted here are identical there except for the one word in
     note 2. No print copy was consulted and the locator says so.
   - The 1929 papers themselves were NOT reached. Nature 123:88 is paywalled, the JOSA
     record carries no abstract, and HathiTrust returned 403 on 2026-08-10. Michelson's
     sentence is quoted here as it appears in DeMeo and in the book, which agree word for
     word, and as Swenson paraphrases it. Anyone who gets the printings should re-check
     the one-fiftieth wording in JOSA before making it load-bearing.
   - Munera's Apeiron paper was not retrieved either (ResearchGate returned 403); he is
     quoted from the book's footnote 689, which is the only role he plays here.
   - Swenson was read in a full-text copy of the 1972 University of Texas Press edition;
     page numbers are as printed in that copy.

11. DEFECTS IN OUR OWN RECORD, reported up, NOT edited here:
   (a) the "3 items" in the batch metadata, above;
   (b) THE CLUSTER NOTE IS WRONG ON TWO OF ITS THREE FACTS AND IT RENDERS AS THE SUMMARY
       LINE ABOVE THIS CARD (build.py maps note -> basis; render.py prints basis at the head
       of the refutation section). It currently reads "...run by Michelson at Mount Wilson
       specifically to test Miller", directly above a refutation whose section 2 is headed
       "The higher altitude did not happen" and says the site was Pasadena. Pease and Pearson
       did the observing under Michelson's supervision, and the site was the observatory's
       Pasadena laboratory. A reader who never expands the card sees only the wrong version.
       OPERATOR: this needs an edit in clusters.py, which this agent does not own. Anchor on
       the cluster key "A11", never on the originator= line. Exact replacement text:
         note="A high-precision repeat of Michelson-Morley (expected 0.9 fringe, measured "
              "0.01), run by Pease and Pearson under Michelson at the Mount Wilson "
              "Observatory's Pasadena laboratory, specifically to test Miller. Same "
              "non-discriminating status as A01."
       (em dash in "Michelson-Morley" as the surrounding file uses it.) This was reported in
       an earlier pass and not applied; it is the one fact this entry is distinctive for.
   (c) the cluster's real_source cites only JOSA 18(3):181, but the sentence the whole
       downstream tradition quotes is the Nature note of 19 Jan 1929, and the two printings
       give different ratios AND, on Swenson's account, different velocity bases. OPERATOR:
       real_source should carry both printings — Nature 123:88 (19 Jan 1929) and J. Opt.
       Soc. Am. 18(3):181-182 (Mar 1929). Also in clusters.py, not editable here;
   (d) render.py hard-codes the compression heading "The list overstates its own source".
       On a `reversed` drift where the list is the more cautious party, that heading
       misdescribes the finding, so this entry's note says which way the gap runs in its
       first sentence rather than relying on the heading;
   (e) `_b10_R11.py` and `_b11_R11.py` both define R11, and deep.py's loader asserts on
       collision — whoever wires batch 10 in will hit it.

12. FIXES APPLIED IN THIS FILE ON 2026-08-11, and what each replaced:
   (a) tldr: "the chain that carried it to this list" -> "the geocentric literature this
       item is traced to". The body (gloss, compression note, verdict_challenge) all decline
       to claim a delivery path to the compiler; the TLDR was claiming one.
   (b) steelman.why_it_doesnt_save_claim: the sentence "The entrainment hypothesis got its
       altitude and its independent replication, and neither produced Miller's signal"
       asserted an outcome for the 1930 mountain installation that no source we have reports.
       Rewritten to concede that first and rest the answer on Joos. See note 6.
   (c) refutation section 1: the Swenson quotation is now carried through the clause that
       gives the JOSA ratio its velocity basis, instead of being cut at "expected shift".
       "the record is clear" is gone; the record is documented, not clear. See note 5.
   (d) refutation section 6: "fifteen orders of magnitude past 1929" was comparing a fringe
       shift (0.01) with a fractional anisotropy (1e-17). In the same units, 1929's
       v <= 3.1 km/s is (v/c)^2 ~ 1.07e-10, so the modern cavity bounds are seven and eight
       orders past it. Recomputed 2026-08-11.
   (e) refutation section 6 and sources: the Wettzell claim about length-of-day and VLBI was
       hung on Eur. Phys. J. C 82 (2022), which supports only the rotation-rate bound — that
       paper mentions neither VLBI nor length-of-day and calls its diurnal-polar-motion
       corrections preliminary (checked 2026-08-11). The rate claim now cites it and only it;
       length-of-day now cites Schreiber et al., Nature Photonics 17:1054 (2023), and the
       VLBI comparison now cites Bohm et al., Adv. Geosci. 50:9 (2019), CONT17.
   (f) compression.note: "Nothing in its pages on Michelson-Pease-Pearson locates a rotation
       claim" contradicted our own refutation section 5, which quotes footnote 752 — at the
       foot of p. 387, inside those pages — crediting "the rotation of the ether every 24
       hours" with all the interferometer positives. The absence claim is now the narrow one
       that is true (no claim that this EXPERIMENT measured the Earth's rotation), scoped to
       the OCR and to named pages, with footnote 752 named as what does appear.
   (g) page correction: the "20 km/sec" division is on p. 387, not p. 386. See note 4.
   (h) the Miller shielding quotation in the steelman now carries its opening ellipsis and
       both of its "it would seem" hedges, rather than starting mid-sentence unmarked.
   NOT changed: the verdict, the verdict_challenge, the cluster note (owner: clusters.py),
   and the advocate's survives=3.
"""

ENTRY = {

"A11": dict(

    tldr=("The 1929 experiment reported an upper limit — no displacement as great as "
          "one-fifteenth of the expected one, and one-fiftieth in the second of its two "
          "printings — and the geocentric literature this item is traced to turned that "
          "into a detection of 20 km/s by dividing 300 by 15, when a Michelson-Morley fringe "
          "shift goes as the square of the speed. The book the item is traced to says the "
          "experiment “showed an ether drift against the Earth”; where it does call the "
          "result null, the word is inside its own quotation marks, in a paragraph the "
          "next thirty pages retract. So on this argument the list is the more orthodox "
          "party. And "
          "neither reading reaches the Earth's rotation: an instrument of that design "
          "encloses no area, so its rotation signal is about 1.5 ten-thousandths of a "
          "fringe, roughly seventy times below the limit it could set — which is why "
          "Michelson tested rotation in 1925 with a fifth of a square kilometre of "
          "evacuated pipe instead, and measured 0.230 ± 0.005 fringes against a "
          "rotating-Earth prediction of 0.236 ± 0.002."),

    passage=dict(
        work="WRK-SUNGENIS-2006",
        pd=False,
        locator=("Vol. I, ch. 6 “What Did Michelson-Morley Actually Demonstrate?”, section "
                 "“The Dayton Miller Experiments”, at printed p. 387 of the archive.org OCR "
                 "text (item GallileoWasWrong, the CD-ROM issue whose title page reads "
                 "Volume I / The Scientific Evidence). The same sentences appear in the "
                 "seventh-edition scan at ch. 5, printed p. 662. Not checked against a print copy"),
        quote=("Michelson proved this in two ways. The first was by the Michelson-Gale "
               "experiment in 1925 that measured the same absolute motion that Sagnac "
               "discovered in 1913; the second, by the Michelson-Pease-Pearson experiment "
               "which showed an ether drift against the Earth, and that the speed of light "
               "was affected by it."),
        gloss="""<p><strong>Read that against the item before anything else.</strong> The item says <em>null</em>. The source says the experiment <em>showed an ether drift</em>. This is not a hedge that has been dropped in transit; it is the other side of the question, and the list has taken the side the physics literature is on.</p>
<p><strong>The book uses the word &ldquo;null&rdquo; of this experiment once in the text reachable here, and puts it in quotation marks.</strong> At printed p. 353, in a paragraph listing the repetitions that followed 1905, Michelson &ldquo;teamed up with F. G. Pease and F. Pearson and declared again that he produced a &lsquo;null&rsquo; result&rdquo;. The scare quotes are the book&rsquo;s. Thirty pages later it explains what it thinks really happened: the 1928 run, it says, was the one where &ldquo;Michelson indeed found significant fringe shifting&rdquo; (p. 386), and Michelson then &ldquo;obfuscates his results&rdquo; by comparing them to a supposed 300 km/s motion of the solar system. So a reader who took &ldquo;null&rdquo; from p. 353 took a word the same chapter spends thirty pages retracting.</p>
<p><strong>Where the claim comes from, link by link.</strong> The reading is not original to this book and the book does not pretend it is. Its footnotes 751 and 754 cite James DeMeo, <em>&ldquo;Dayton Miller&rsquo;s Ether-Drift Experiments: A Fresh Look&rdquo;</em>, and the narrative here follows DeMeo&rsquo;s almost sentence for sentence &mdash; the three attempts, the 22-metre and 32-metre paths, the same block quotation of Michelson, the same 20 km/s. DeMeo&rsquo;s own caption calls it &ldquo;their successful detection of an ether-drift of some unspecified quantity just under 20 km/sec.&rdquo; Behind DeMeo stands H&eacute;ctor Mu&ntilde;era&rsquo;s 1998 <em>Apeiron</em> paper, quoted at length in this book&rsquo;s footnote 689, which rereads the classic null results as small positives. DeMeo is not a geocentrist and Mu&ntilde;era is not arguing for a stationary Earth; the geocentric conclusion is added here, at this link in the chain, which is why the argument is recorded under this book and not under theirs.</p>
<p><strong>One number, three answers, in one chapter.</strong> The sentence everybody is quoting is a bound: <em>&ldquo;The results gave no displacement as great as one-fifteenth of that to be expected on the supposition of an effect due to a motion of the solar system of three hundred kilometers per second.&rdquo;</em> The main text divides, across pp. 386&ndash;387: &ldquo;if one multiplies his &lsquo;three hundred kilometers per second&rsquo; by &lsquo;one-fifteenth,&rsquo; the result is 20 km/sec&rdquo;. Footnote 689, at the foot of p. 353, quotes Mu&ntilde;era taking the square root instead &mdash; &ldquo;the corresponding solar velocity is then 300(1/15)<sup>1/2</sup> = 77.5 km/s, which is not null by any means&rdquo; &mdash; and reporting 42.4 km/s for the <em>JOSA</em> printing&rsquo;s one-fiftieth, which is 300/&radic;50 and so carries the 300 km/s basis over to the second printing; Swenson&rsquo;s history attaches a different velocity basis to that printing, and neither 1929 paper was reached here to settle which is right. Footnote 759 passes on Galaev&rsquo;s 6,000 m/s, which is the same division done on one-fiftieth. Three velocities, three cited authorities, no reconciliation. Which arithmetic is right is settled in the refutation; that the book prints all three is visible without any physics at all.</p>
<p><strong>What this passage is being cited as.</strong> The earliest text located that puts this experiment into a geocentric argument. A keyword search of the <em>De Labore Solis</em> PDF at geocentricity.com returned zero hits for <em>Pease</em> and zero for <em>Pearson</em> on 2026-08-10; Bouw&rsquo;s <em>Geocentricity</em> (1992) was not reachable. So this is the earliest located, not the first, and the specimen carries no citation for item 10 &mdash; it carries none for any of its 461 &mdash; so which text its compiler read is not something this page can show.</p>"""),

    steelman=dict(
        description="""<p><strong>SURFACE (weak &mdash; do not use).</strong> &ldquo;The 1929 experiment was a null, so the item is simply correct and there is nothing to discuss.&rdquo; That concedes the interesting half of the case and walks past the fact that the tradition the item comes from says the opposite. It also invites the reply that a &ldquo;null&rdquo; in this literature never meant a measured zero &mdash; which is true.</p>
<p><strong>DEEPER.</strong> The experiment really did not return zero, and nobody claimed it did. What Michelson, Pease and Pearson published was a ratio: no displacement as great as one-fifteenth of the expected one. Reported limits are not measured zeros, the two 1929 papers do not give the same limit &mdash; <em>Nature</em> in January said one-fifteenth, <em>JOSA</em> in March said one-fiftieth &mdash; and a reader entitled to ask what the residual actually was is asking a fair question that the two-page papers do not answer.</p>
<p><strong>KERNEL.</strong> The strongest form is about the shielding, and it was put by Dayton Miller at the time rather than invented later. Miller&rsquo;s claim was an <em>entrained</em> ether: one dragged along near massive bodies, so that a drift would show up out in the open air on a mountain and be suppressed indoors. On that hypothesis the 1929 apparatus was the worst possible test, and this is not hindsight &mdash; it is where the instrument actually was. Loyd Swenson&rsquo;s history has the team, in the summer of 1928, removing the superstructure and putting the apparatus &ldquo;in a well of the Pasadena Laboratory&rdquo; inside an improvised constant-temperature room. Miller&rsquo;s printed objection follows exactly, hedges and all: &ldquo;&hellip; it would seem that such massive and opaque shielding is not justifiable &hellip; it would seem to be essential that there should be the least possible obstruction between the free ether and the light path &hellip;&rdquo; A defender who says <em>your best null came out of a hole in the ground under a temperature-controlled ceiling, and the one instrument that was in the open air is the one that kept showing something</em> has said something true, specific and awkward.</p>""",
        why_it_doesnt_save_claim="""<p>Because the objection was <strong>acted on</strong> &mdash; though not, in the end, by the run that went up the mountain &mdash; and because the version of it in this book contradicts the version that makes it good.</p>
<p>Acted on, and the loose end named first: in the summer of 1930 Pease and Pearson had the instrument transported up the mountain and installed in the base of the 100-inch telescope, the elevation Miller had asked for, though still not the open air he wanted (Swenson, p. 225). <strong>No result from that installation is reported in Swenson&rsquo;s account of it</strong>, and his note on the same page records correspondence of January 1930 indicating that Michelson had by then lost interest and that the latest observational data was &ldquo;not suitable for publication&rdquo;. So the mountain run is not available to be quoted against Miller, and this page does not quote it. What did answer the objection independently was Georg Joos: an automated 21-metre interferometer, built at the Zeiss works in Jena in direct response to Miller&rsquo;s 1925 announcement, reported in September 1930 after a year of running, which bounded any effect below a thousandth of a fringe width and any aether wind under 1.5 km/s. The entrainment hypothesis got its independent replication at full instrumental strength, and it did not produce Miller&rsquo;s signal.</p>
<p>Contradicted: the entrainment argument works only if the 1929 run was <em>shielded and low</em>. The book needs the opposite. Its explanation of why the third attempt supposedly showed something is that &ldquo;This higher altitude and longer light-path came closer to Miller&rsquo;s specifications&rdquo; (p. 386) &mdash; and there was no higher altitude. The observatory&rsquo;s laboratory is in Pasadena. A defender may have the shielding point or the higher-altitude point; the two cancel, and only one of them is in the source.</p>"""),

    refutation="""<p><strong>Three things have to be kept apart here, because the item and its source disagree about the first of them.</strong> What the 1929 papers reported. What the geocentric literature says they reported. And what an instrument of that design could ever have said about the Earth&rsquo;s rotation, which is the word the item actually uses.</p>

<h4>1. The reported quantity is a limit, and the chain converted it into a measurement</h4>

<p>The sentence everyone quotes reads: <em>&ldquo;The results gave no displacement as great as one-fifteenth of that to be expected on the supposition of an effect due to a motion of the solar system of three hundred kilometers per second.&rdquo;</em> That is the ordinary grammar of an experimental bound &mdash; <em>no displacement as great as</em> &mdash; and it is how limits have been stated since limits have been stated. DeMeo&rsquo;s figure caption renders it as &ldquo;their successful detection of an ether-drift of some unspecified quantity just under 20 km/sec&rdquo;, and <em>Galileo Was Wrong</em> takes that over: the experiment &ldquo;showed an ether drift against the Earth&rdquo;. An upper bound of X is not a detection at X. If it were, every non-detection in physics would be its own discovery, reported at the threshold.</p>

<p>The 20 km/s is also arithmetically wrong, and the book contains the correction. A Michelson-Morley fringe displacement goes as the <em>square</em> of the speed &mdash; &Delta; = 2<em>Lv</em><sup>2</sup>/&lambda;<em>c</em><sup>2</sup> &mdash; so a shift one-fifteenth of the shift expected for 300 km/s corresponds to 300/&radic;15 = <strong>77.5 km/s</strong>, not 300/15 = 20. That is exactly the calculation the book&rsquo;s own footnote 689 reproduces from Mu&ntilde;era, alongside 42.4 km/s for the <em>JOSA</em> printing&rsquo;s one-fiftieth; footnote 759 then passes on Galaev&rsquo;s 6,000 m/s, which is 300/50 divided linearly again. One sentence of Michelson&rsquo;s, three incompatible velocities, all three printed in the same chapter as support for the same conclusion. Only one of them is even the right kind of arithmetic, and the one the main text builds its match to Kennedy-Thorndike on is not it.</p>

<p>On the discrepancy itself, the documentation is older than the argument, and it is messier than either side has use for. Loyd Swenson&rsquo;s history reports that the two 1929 papers did not agree: <em>Nature</em> on 19 January carried a note that no displacement as great as one-fifteenth of the expected one was found, while in March the <em>Journal of the Optical Society of America</em> reported that &ldquo;nothing was observed within one-fiftieth of the expected shift, based on Sternberg&rsquo;s estimate of the solar system&rsquo;s resultant velocity of about three thousand kilometers per second&rdquo; (p. 222; Swenson names Gustaf Str&ouml;mberg, the Mount Wilson astronomer who set the observing schedule with Miller, at p. 221). That trailing clause matters here, because it attaches the second ratio to a different velocity basis from the three hundred km/s the <em>Nature</em> sentence names &mdash; and Mu&ntilde;era&rsquo;s 42.4 km/s for the <em>JOSA</em> printing is 300/&radic;50, which carries the first basis over to the second. Neither 1929 printing was reached for this entry: the ratios and the bases are as reported by Swenson and by Mu&ntilde;era, who do not agree, and nothing on this page turns on which of them has it right. What both do settle is that the book&rsquo;s footnote 753 &mdash; the one-fiftieth figure &ldquo;appears to be in error&rdquo; &mdash; sits badly beside its own footnote 689, which quotes Mu&ntilde;era reporting both printings and converting both, though Mu&ntilde;era too breaks off to wonder in parenthesis whether the <em>JOSA</em> figure is a misprint. Swenson, writing in 1972, asked whether the change was a refinement of the data or a change of judgment, concluded that &ldquo;to most physicists these figures were clearly null results either way&rdquo;, and added that &ldquo;Miller or his partisans could capitalize on such discrepancies&rdquo; &mdash; twenty-six years before Mu&ntilde;era and thirty-four before this book.</p>

<h4>2. The higher altitude did not happen</h4>

<p>The book&rsquo;s explanation of why the third attempt allegedly showed something is causal and checkable: the run moved to a &ldquo;well-sheltered basement room of the Mount Wilson laboratory&rdquo;, the light path went to 52 metres, and &ldquo;This higher altitude and longer light-path came closer to Miller&rsquo;s specifications.&rdquo; The path length is right. The altitude is a misreading of a name. The Mount Wilson Observatory&rsquo;s laboratory and optical shops were in <em>Pasadena</em>, on the valley floor, and that is where this instrument was built &mdash; on the seven-thousand-pound cast-iron bedplate that had been used to polish the 100-inch Hooker mirror. Swenson records that in the summer of 1928, still losing the fight against temperature drift and asymmetrical strains, the team stripped off the superstructure, sank the basic apparatus into a well of the Pasadena laboratory, improvised a constant-temperature room, floated the optics on a mercury bath, enlarged the path length to eighty-five feet, and roofed the whole assembly over so that the observer could sit above the ceiling while the sealed system rotated beneath him (pp. 220&ndash;221). The instrument was carried up the mountain in the summer of <strong>1930</strong>, into the base of the 100-inch telescope &mdash; eighteen months after the paper the argument rests on.</p>

<p>So the third run was not nearer to Miller&rsquo;s conditions than the first two. It was further away: deeper, more thermally sealed, and 1,500 metres lower than Miller&rsquo;s canvas house on the summit. Which is a real point for the other side &mdash; it is Miller&rsquo;s own objection, and this page grants it in the steelman &mdash; but it is the opposite of the reason the book gives, and the two cannot both be run.</p>

<h4>3. Michelson announced the result at a press conference</h4>

<p>The framing around all of this is that Michelson knew and concealed: he &ldquo;obfuscates his results&rdquo;, he was &ldquo;too blinded by whatever was prohibiting him from telling the whole truth&rdquo;, he &ldquo;went to his grave&rdquo; unaware of what he had proved. What Michelson did with the result was to report it to the Optical Society of America at the Michelson Meeting in November 1928 and then take questions from reporters. The <em>New York Times</em> of 3 November 1928 quotes him: <em>&ldquo;the results of my experiment conducted with greater scientific care, improved apparatus and refined technique, with the intention of eliminating every possible source of error, are again negative.... It is for physicists to study and explain these results and reconcile them with the existence of the hypothetical ether.&rdquo;</em> Miller was in the room, said his own experiments had been conducted &ldquo;in the honest hope of arriving at a negative result also&rdquo;, conceded that periodic temperature fluctuations might account for his positives, and maintained them anyway. That is what the disagreement looked like from inside: two men stating their results and their doubts in public, on the same afternoon.</p>

<h4>4. The word in the item is &ldquo;rotation&rdquo;, and this instrument has no purchase on it</h4>

<p>A Michelson interferometer sends each beam out and back along its own arm. The closed circuit formed by the two interfering paths therefore encloses no area, and the first-order rotation term &mdash; the Sagnac term, which is proportional to the enclosed area times the rotation rate &mdash; cancels. All that remains of the Earth&rsquo;s spin is second order in the surface speed. Put the numbers in. At Pasadena&rsquo;s latitude the surface moves at &Omega;<em>R</em>cos&phi; = <strong>384.5 m/s</strong>; at the summit, 384.1 m/s. With the 1928 path length of 25.9 m that is</p>

<p style="margin-left:1.5em">&Delta; = 2<em>Lv</em><sup>2</sup>/&lambda;<em>c</em><sup>2</sup> = <strong>1.5 &times; 10<sup>&minus;4</sup> fringes</strong>,</p>

<p>about one sixty-seventh of the 0.01 fringe the experiment could bound. (Recomputed here 2026-08-10; the same formula returns 0.91 fringes for 30 km/s at that path length, which is the 0.9 the standard comparison tables give, so the constants are the tables&rsquo;.) A null rotation result at this instrument is not evidence about the Earth. It is what every party to the dispute should have predicted, and nobody in 1929 claimed otherwise.</p>

<p><strong>Michelson knew this, which is why his rotation experiment looked nothing like this one.</strong> He had proposed a closed-circuit test in <em>Philosophical Magazine</em> in 1904, and in 1925 he and Henry Gale, assisted by Fred Pearson &mdash; the same Fred Pearson &mdash; laid out an evacuated pipe rectangle 2,010 by 1,113 feet at Clearing, Illinois, enclosing <strong>0.208 km<sup>2</sup></strong>, because area is the thing a rotation measurement needs and a laboratory interferometer has none. The predicted shift for a rotating Earth was 0.236 &plusmn; 0.002 fringes and the observed shift was 0.230 &plusmn; 0.005. Recomputing 4<em>A</em>&Omega;sin&phi;/&lambda;<em>c</em> from the published dimensions and latitude gives 0.2363 &mdash; the prediction was not fitted to the data. Within four years, two Michelson interferometers with two different geometries gave the two answers each geometry can give: the one enclosing no area saw no rotation, and the one enclosing a fifth of a square kilometre measured it, the paper reporting that the observed displacement agreed with the computed value &ldquo;within the limits of experimental error&rdquo;.</p>

<h4>5. The geocentric explanation cannot produce the residuals it is invoked to explain</h4>

<p>Take the book&rsquo;s own mechanism seriously, because it states one. Footnote 752: &ldquo;It is precisely the rotation of the ether every 24 hours that accounts for the small positive results of all the interferometer experiments at the surface of the Earth.&rdquo; An ether circling a fixed Earth once a sidereal day passes a Pasadena laboratory at the same 384.5 m/s that a rotating Earth carries the laboratory through a fixed ether &mdash; the relative velocity is the same vector, which is exactly why no laboratory interferometer can tell the two apart. But the same identity fixes the size. The predicted shift is the same 1.5 &times; 10<sup>&minus;4</sup> fringes. Miller&rsquo;s claimed drift of about 10 km/s is 26 times that speed and therefore <strong>676 times</strong> that fringe shift; the 20 km/s the book infers for Michelson is <strong>2,705 times</strong> it. The hypothesis offered to explain the small positive results under-predicts them by between two and three orders of magnitude in velocity. A defender can reach for a partially entrained ether with a velocity gradient, and the book quotes Galaev doing exactly that &mdash; but an entrained ether is a different explanation, it is Miller&rsquo;s and not the 24-hour one, and it predicts the effect grows with altitude, which returns us to the fact that the 1928 run was in a well in Pasadena.</p>

<h4>6. What has happened since, on both instruments</h4>

<p>Both lines were continued and both kept giving the same answers. On the translation side: Joos at Jena in 1930 bounded any drift below a thousandth of a fringe, under 1.5 km/s; the modern descendants are rotating optical cavities, which bound the anisotropy of the speed of light at &Delta;<em>c</em>/<em>c</em> &asymp; 10<sup>&minus;17</sup> (Herrmann et al. 2009) and 10<sup>&minus;18</sup> (Nagel et al. 2015). Set that against 1929 in the same units rather than in fringes: a bound of <em>v</em> &le; 3 km/s is a bound on the fractional anisotropy of about (<em>v</em>/<em>c</em>)<sup>2</sup> &asymp; 10<sup>&minus;10</sup>, so the modern experiments are seven and eight orders of magnitude past it &mdash; still null, still exactly what relativity predicts for an Earth in motion. On the rotation side: the ring laser at Wettzell, the direct descendant of the 1925 rectangle, resolves the Earth&rsquo;s rotation rate to better than one part in 10<sup>9</sup> after about 10<sup>4</sup> seconds of integration (Eur. Phys. J. C 82, 2022); a 120-day continuous run of a large ring laser resolved length-of-day fluctuations to a few milliseconds, about five parts in 10<sup>9</sup>, at three hours per data point (Schreiber et al. 2023); and during the CONT17 campaign the Wettzell ring laser was run alongside very-long-baseline interferometry, where folding the two together improved the &delta;UT1 and polar-motion solutions rather than contradicting them (B&ouml;hm et al. 2019). The instrument that cannot see rotation still cannot. The instrument that can, does, continuously, to nine figures.</p>

<h4>7. What the verdict ranges over</h4>

<p>Not &ldquo;the 1929 experiment was a fraud&rdquo; and not &ldquo;the residual was exactly zero&rdquo;. The experiment was careful, it reported a limit rather than a zero, and the two papers stating that limit disagree with each other &mdash; all of which is conceded above. What fails is the use. As the list states it, the item describes a null in an instrument that could not have detected the Earth&rsquo;s rotation on any cosmology, and so discriminates nothing. As its source states it, the claim is a detection, and it is built on an upper limit read as a measurement, a linear conversion of a square-law quantity, and an altitude the apparatus did not have. The two readings are each other&rsquo;s contradiction, and the list is holding the one its own authority spent a chapter arguing against.</p>""",

    advocate=dict(
        best_defense=(
            "Four moves. First, you have conceded my best point in your own steelman and "
            "then walked past it: the 1929 result came out of a well in a "
            "temperature-controlled room, which on an entrained-ether hypothesis is the "
            "one configuration guaranteed to see nothing. You correct Sungenis's altitude "
            "and think this hurts me. It helps me. The most shielded run in the series is "
            "the one everybody quotes as decisive. Second, your rotation arithmetic is a "
            "man of straw with a square root in its hand. Nobody in this tradition claims "
            "the 1929 apparatus measured the Earth's rotation — the claim is that it "
            "failed to find the 300 km/s translation that the astronomy of the day "
            "required, and on YOUR numbers it failed by a factor of a hundred: a 3 km/s "
            "bound against a 300 km/s prediction. You report that as a triumph for a "
            "moving Earth. It was a hundredfold discrepancy that had to be absorbed by "
            "postulating that lengths contract by exactly the amount needed to hide it. "
            "Third, your own paragraph 5 gives the game away. You say the rotating-ether "
            "and rotating-Earth pictures produce 'the same vector, which is exactly why no "
            "laboratory interferometer can tell the two apart.' That is my thesis, in your "
            "words, on your page. Fourth, Miller. His sidereal periodicity was never "
            "explained to everyone's satisfaction; Shankland's temperature analysis has "
            "been contested in print by Munera, by Allais — a Nobel laureate — and by "
            "Cahill, and 'his own student re-examined the data sheets' is a character "
            "reference, not a refutation. You are ridiculing an arithmetic slip in a "
            "footnote while the experimental record you rely on is thinner than you say."),
        survives=3,
        preemptive=(
            "Three, and it is earned by the second and third moves; the first is already "
            "conceded in our own voice and must stay conceded. Concretely, four things in "
            "the text are load-bearing and must not be edited out. (1) The steelman's "
            "shielding paragraph and its Swenson citation stay where they are, ABOVE the "
            "refutation, so no reader meets our altitude correction without first meeting "
            "the point it costs us; and the answer to it stays factual rather than "
            "rhetorical, and it concedes the loose end before the defender reaches it — "
            "the instrument did go up the mountain in summer 1930, but no result from that "
            "installation is reported anywhere we have reached, so what actually met the "
            "objection was Joos's independent replication at Jena. Do not restore the "
            "earlier wording, which credited the mountain installation with an outcome "
            "nobody can cite. "
            "(2) Section 4 must keep its opening sentence naming the word 'rotation' as "
            "the ITEM's word, not the source's, because that is what makes the arithmetic "
            "responsive rather than a straw man: the list says rotation, the source does "
            "not, and both are answered in different sections. Do not let an editor merge "
            "them. (3) The 300 km/s point belongs to A01 and the text must not be "
            "rewritten to fight it here; if it is raised, the answer is that special "
            "relativity predicts the null for any translational speed whatever, that "
            "length contraction was not invented to save this result but was already "
            "Lorentz's 1892 response to 1887, and that the contraction hypothesis makes "
            "further predictions — Kennedy-Thorndike, Ives-Stilwell, modern cavity and "
            "clock-comparison bounds — which were tested separately and held. Adding that "
            "to this entry would duplicate A01; the cross-reference is the fix, not a new "
            "section. (4) Paragraph 5's concession that the two pictures give the same "
            "relative velocity must keep the sentence that immediately follows it, which "
            "converts the concession into the magnitude argument. Isolated, it reads as "
            "our own case for underdetermination — that is R01's argument and it is "
            "answered there; here it is the premise of a quantitative failure, and the two "
            "sentences must never be separated by so much as a paragraph break."),
    ),

    straw_man=dict(
        identified=True,
        detail=("The recurring move in this chapter, and it is quoted approvingly rather "
                "than argued for, is Múnera's: that the interferometer papers “exhibit "
                "an inconsistency between observation (a non-zero velocity) and "
                "interpretation (a null result)” (quoted at the book's footnote 687). "
                "That treats “null” as a claim of measured zero, so that any "
                "non-zero residual becomes a contradiction the experimenters covered up. It "
                "is not what the word means and never was: a null result is a result "
                "consistent with zero within the uncertainty of the measurement, which is "
                "why the 1929 papers state a ratio to an expected value rather than a "
                "velocity, and why Michelson told the press the results were "
                "“again negative” while inviting physicists to explain them. "
                "The book builds a motive on top of the misreading — Michelson "
                "“obfuscates his results”, physicists “perpetuated a "
                "misinterpretation of Michelson-Morley to save themselves” — and "
                "the motive is doing work the arithmetic cannot. Two things this page does "
                "NOT file as straw men, because they are fair: the observation that the two "
                "1929 papers give different limits, which is true and is in Swenson; and "
                "Miller's shielding objection, which is his own, was made at the time, and "
                "is answered in the steelman on its merits.")),

    compression=dict(
        assessed=True, drifted=True,
        list_phrasing="Michelson–Pease null rotation detection.",
        source_wording=("&ldquo;… the second, by the Michelson-Pease-Pearson experiment which "
                        "showed an ether drift against the Earth, and that the speed of light "
                        "was affected by it.&rdquo;"),
        drift_type="reversed",
        note=("<strong>The gap here runs the other way from the usual one.</strong> On most "
              "arguments on this page the list is firmer than its source. On this one the list "
              "is the more orthodox party: it calls the 1929 experiment a null, which is what "
              "the physics literature calls it, while the text our record names as the "
              "argument's origin says the experiment &ldquo;showed an ether drift against the "
              "Earth&rdquo; and spends thirty pages arguing that the null was manufactured. "
              "The one place the reachable text applies the word &ldquo;null&rdquo; to this "
              "experiment, at printed p. 353, it is inside the book's own quotation marks.<br><br>"
              "<strong>Two smaller gaps travel with it.</strong> <em>The word "
              "&ldquo;rotation&rdquo; is the list's.</em> The book treats this experiment as a "
              "Michelson-Morley repetition about translation through the ether, and puts "
              "rotation elsewhere &mdash; in Michelson-Gale and Sagnac, where it concedes the "
              "measurement and reassigns the motion to the ether. No claim that this "
              "experiment measured the Earth's rotation is located in the archive.org OCR's "
              "pages on Michelson-Pease-Pearson (printed pp. 385&ndash;387) or at the "
              "&ldquo;null&rdquo; mention on p. 353. Rotation does appear on those pages, but "
              "as the book's own explanation rather than as the experiment's subject: footnote "
              "752, at the foot of p. 387, credits &ldquo;the rotation of the ether every 24 "
              "hours&rdquo; with the small positive results of all the interferometer "
              "experiments &mdash; a mechanism answered on its own numbers in the refutation. "
              "<em>And the item is one "
              "item.</em> It is the only member of this cluster, which is worth saying on a "
              "page about how 461 items compress: a claim can circulate as a single line with "
              "no relatives and still carry a reading of the primary literature that its own "
              "tradition rejects.<br><br>"
              "<code>reversed</code> is recorded because that is what the comparison shows, "
              "but the enum was built on the assumption that the item is a derivative of the "
              "source, and here the derivative agrees with the papers and contradicts the "
              "source &mdash; a shape none of the seven values quite names. The specimen "
              "carries no citation for item 10, so which text its compiler read is not "
              "something this page can establish; both texts are printed above and the reader "
              "can see the distance between them.<br><br>"
              "<strong>The refutation answers the source, not the fragment.</strong> It takes "
              "the book's claim at full strength &mdash; a detection of an ether drift, at 20 "
              "km/s, in a run said to have been made at higher altitude &mdash; and answers "
              "each part: the quoted sentence states an upper bound rather than a measurement; "
              "the conversion of that bound is linear where the fringe shift goes as the square "
              "of the speed, as the book's own footnote 689 shows by doing it correctly; and "
              "the 1928 apparatus sat in a well of the observatory's Pasadena laboratory, going "
              "up the mountain only in the summer of 1930. The list's own phrasing is answered "
              "separately, in section 4, where the arithmetic shows that an instrument of that "
              "geometry has a rotation signal about seventy times below the limit it could set.")),

    verdict_challenge=dict(
        challenged=True,
        proposed_verdict="SELF-CONTRADICTED",
        reasoning=(
            "STANDARD PHYSICS is defensible on the experiment and is what A01 carries for "
            "the 1887 original: a real, explained, non-discriminating null. But the legend "
            "defines SELF-CONTRADICTED as the case where \"the claim's own source, or "
            "another item on the same list, points the other way\", and that is this item "
            "exactly. The item asserts a null; the work our record names as its originator "
            "asserts at printed p. 387 that the same experiment \"showed an ether drift "
            "against the Earth\", with no hedge in the sentence, and uses \"null\" of it "
            "once, in its own scare quotes, in a paragraph it then spends thirty pages "
            "retracting. Filing it as STANDARD PHYSICS records the least interesting true "
            "thing about it and loses the provenance finding, which is the product of this "
            "review. THE WEAK POINT, STATED SO IT CANNOT BE MINED: the challenge depends on "
            "the originator attribution, and the specimen carries no citation for item 10, "
            "so we cannot show the compiler read this book rather than a textbook table "
            "that calls the result null. If an operator judges that too thin to carry \"the "
            "claim's own source\", STANDARD PHYSICS should stand and nothing else in this "
            "entry changes: the refutation answers both readings in separate sections and "
            "does not depend on which verdict chip sits above it.")),

    people=["PER-SUNGENIS"],
    related=["A01", "A02", "A03", "A07", "A12", "R01"],

    sources=[
        dict(label="Michelson, Pease & Pearson, “Repetition of the Michelson-Morley "
                   "Experiment”, Nature 123:88 (19 January 1929) — the printing that carries "
                   "the “no displacement as great as one-fifteenth” sentence quoted by every "
                   "downstream author here; the full text was not reached (paywalled, checked "
                   "2026-08-10)",
             url="https://www.nature.com/articles/123088a0"),
        dict(label="Michelson, Pease & Pearson, “Repetition of the Michelson-Morley "
                   "Experiment”, J. Opt. Soc. Am. 18(3):181–182 (March 1929) — the second "
                   "printing, which Swenson and Múnera both report as giving one-fiftieth "
                   "rather than one-fifteenth; the record carries no abstract and the text was "
                   "not reached",
             url="https://opg.optica.org/josa/abstract.cfm?uri=josa-18-3-181_1"),
        dict(label="Loyd S. Swenson Jr., The Ethereal Aether: A History of the "
                   "Michelson-Morley-Miller Aether-Drift Experiments, 1880–1930 (University of "
                   "Texas Press, 1972), ch. “Michelson Reaffirms the Null, 1925–1930”, pp. "
                   "216–227 — the Pasadena laboratory and the well (pp. 220–221), the 1930 move "
                   "up the mountain into the base of the 100-inch, with no result from it "
                   "reported and note 29 recording that correspondence of January 1930 shows "
                   "Michelson’s interest had lapsed and the latest data was judged unfit to "
                   "publish (p. 225), Joos at Jena (p. 226), the one-fifteenth / one-fiftieth "
                   "discrepancy with its “Sternberg”/Strömberg velocity basis and Michelson’s "
                   "press conference (pp. 222–223)",
             url="https://www.jstor.org/stable/10.7560/720008"),
        dict(label="James DeMeo, “Dayton Miller’s Ether-Drift Experiments: A Fresh Look” "
                   "(Pulse of the Planet 5, 2002; web version at orgonelab.org) — the "
                   "intermediary Galileo Was Wrong cites as “DeMeo, p. 17” and “p. 18”; source "
                   "of the three-attempt narrative, the 20 km/s conversion and the caption "
                   "“their successful detection of an ether-drift”",
             url="http://www.orgonelab.org/miller.htm"),
        dict(label="Héctor Múnera, “Michelson-Morley Experiments Revisited: Systematic Errors, "
                   "Consistency Among Different Experiments, and Compatibility with Absolute "
                   "Space”, Apeiron 5(1–2), 1998 — quoted here only as it appears in Galileo Was "
                   "Wrong Vol. I n. 689 (300(1/15)^½ = 77.5 km/s; 42.4 km/s for the JOSA "
                   "figure); the original returned 403 on 2026-08-10 and was not retrieved",
             url="https://www.researchgate.net/profile/Hector-Munera-2"),
        dict(label="Michelson & Gale, assisted by Pearson, “The Effect of the Earth’s Rotation "
                   "on the Velocity of Light”, Astrophys. J. 61:140 (1925) — rectangle 2010 × "
                   "1113 ft at latitude 41°46′, predicted 0.236 ± 0.002 fringes, observed 0.230 "
                   "± 0.005",
             url="https://paulba.no/paper/Michelson_Gale_II.pdf"),
        dict(label="Michelson, “Relative motion of Earth and aether”, Phil. Mag. 8:716–719 "
                   "(1904) — the closed-circuit rotation experiment proposed twenty-one years "
                   "before it was built",
             url="https://doi.org/10.1080/14786440409463244"),
        dict(label="Herrmann et al., “Rotating optical cavity experiment testing Lorentz "
                   "invariance at the 10⁻¹⁷ level”, Phys. Rev. D 80:105011 (2009) — the modern "
                   "descendant of the translation experiment; Δc/c ≈ 1 × 10⁻¹⁷",
             url="https://arxiv.org/abs/1002.1284"),
        dict(label="Nagel et al., “Direct terrestrial test of Lorentz symmetry in "
                   "electrodynamics to 10⁻¹⁸”, Nature Communications 6:8174 (2015)",
             url="https://arxiv.org/abs/1412.6954"),
        dict(label="“Overcoming 1 part in 10⁹ of earth angular rotation rate measurement with "
                   "the G Wettzell data”, Eur. Phys. J. C 82 (2022) — the descendant of the 1925 "
                   "rectangle; the Allan deviation of the rotation-rate measurement drops below "
                   "one part in 10⁹ after about 10⁴ s of integration. This paper covers the rate "
                   "measurement only: it does not mention VLBI or length-of-day, and treats "
                   "diurnal polar motion as a modelled correction it calls preliminary",
             url="https://link.springer.com/article/10.1140/epjc/s10052-022-10798-9"),
        dict(label="Schreiber, Kodet, Hugentobler, Klügel & Wells, “Variations in the Earth’s "
                   "rotation rate measured with a ring laser interferometer”, Nature Photonics "
                   "17:1054–1058 (2023) — length-of-day fluctuations resolved continuously over "
                   "120 days at a few parts in 10⁹, three hours per data point",
             url="https://doi.org/10.1038/s41566-023-01286-x"),
        dict(label="Böhm, Schartner, Gebauer, Klügel, Schreiber & Schüler, “Earth rotation "
                   "variations observed by VLBI and the Wettzell ‘G’ ring laser during the "
                   "CONT17 campaign”, Adv. Geosci. 50:9–15 (2019) — the ring laser run alongside "
                   "VLBI; combining them reduced the scatter in δUT1 and polar motion against "
                   "the VLBI benchmark. This is the citation for the VLBI comparison, which the "
                   "2022 paper above does not make",
             url="https://doi.org/10.5194/adgeo-50-9-2019"),
        dict(label="Michelson-Morley experiment — the standard comparison table of repetitions, "
                   "whose 1929 row (path 25.9 m, expected 0.9 fringe, measured ≤ 0.01, limit ~3 "
                   "km/s) is where this cluster’s recorded figures match; the arithmetic was "
                   "reproduced independently here",
             url="https://en.wikipedia.org/wiki/Michelson%E2%80%93Morley_experiment"),
        dict(label="Sungenis & Bennett, Galileo Was Wrong Vol. I — archive.org scan, item "
                   "GallileoWasWrong; ch. 6 “What Did Michelson-Morley Actually Demonstrate?”, "
                   "the “null” mention at printed p. 353, the three attempts at pp. 385–386, "
                   "Michelson’s quoted paragraph at p. 386, the “two ways” sentence at p. 387, "
                   "footnotes 689 and 751–759 at the feet of those pages",
             url="https://archive.org/download/GallileoWasWrong/Gallileo%20was%20wrong_djvu.txt"),
        dict(label="Sungenis & Bennett, Galileo Was Wrong, seventh edition, Vols 1–3 — the "
                   "cross-read scan; the same material at ch. 5 “More Experiments Point to "
                   "Geocentrism”, around printed p. 662",
             url="https://archive.org/details/galileo-was-wrong-the-church-was-right-sungenis-vol-1-3-complete"),
    ],
),

}
