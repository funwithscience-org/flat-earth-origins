# -*- coding: utf-8 -*-
"""Batch 11 — D03. "Geocentric/Ptolemaic models made accurate predictions."

Three items: 23 "Ptolemaic predictive accuracy.", 218 "Venus transits epicyclic
math.", 265 "Planet brightness epicycles." Cluster verdict STANDARD PHYSICS — kept,
and no verdict_challenge filed. See note 8 for what was weighed against it.

Research notes for whoever picks this up next.

1. THE RECORD'S VOLUME IS WRONG AND IT IS THE EDITION TRAP AGAIN. `clusters.py` has
   D03 at originator="Robert Sungenis", originator_work="Galileo Was Wrong, Vol. II",
   year="2006". The material is in VOLUME I, in both arrangements of the book, and it
   is not close:
     - 2006 two-volume arrangement, archive.org item `GallileoWasWrong` (title page
       "Volume I / The Scientific Evidence"): the epicycle-count section at printed
       pp. 41-43 (ch. 1), the Ptolemy-can-be-adjusted section at printed pp. 210-212
       (ch. 4, "Isn't it Impossible..." neighbourhood).
     - seventh-edition three-volume arrangement, item
       `galileo-was-wrong-the-church-was-right-sungenis-vol-1-3-complete`: the same
       two blocks at Vol. I ch. 1 printed pp. 40-41 and 55-56, and Vol. I ch. 2
       "Objection #16: Don't the Phases of Venus Disprove Ptolemy?", printed
       pp. ~205-213.
   Vol. II in the project's own settled reading is chapters 7-13, the Michelson/Sagnac/
   Pioneer half. None of this cluster is there. Same shape as the D15 correction of
   2026-08-09. Reported in record_problems, NOT edited here — this agent owns one file.

2. ORIGINATION IS NOT SUNGENIS AND IS PROBABLY NOT ANYBODY MODERN, EITHER. Three
   strands, three ancestries, and each one runs OUT of the movement rather than into it:
     (a) "Copernicus needed more epicycles than Ptolemy; Ptolemy's tables were as good"
         — Sungenis's own footnotes credit Koestler, The Sleepwalkers (1959),
         pp. 194-195 and 579-580, and Owen Gingerich, The Book Nobody Read, pp. 54-59.
         In the seventh edition the accuracy claim is carried by a quotation of
         GINGERICH, at second hand through Lakatos: "in Tycho's observation books, we
         can see occasional examples where the older scheme based on the Alfonsine
         Tables yielded better predictions than could be obtained from the Copernican
         Prutenic Tables" (Science Year 1973, pp. 266-267, as quoted).
     (b) "Venus's phases don't refute Ptolemy; the epicycles just need to be bigger" —
         quoted verbatim from Gerardus Bouw, Geocentricity (1992), pp. 309-310, cited
         in both editions. Bouw is fourteen years earlier than the year in our record.
     (c) the six-free-parameter demonstration that the Tychonic system is "a special
         case of the Ptolemaic one" — quoted from Julian Barbour, Absolute or Relative
         Motion, Vol. I (CUP, 1989), pp. 224-225. This appears in the SEVENTH edition
         and was not located in the 2006 Vol. I scan, whose only Barbour hits are
         Barbour & Bertotti on Machian gravity. Barbour is a working physicist writing
         history, not a geocentrist; he belongs in `real_source`, the D04/Eliade slot,
         never in `originator`.
   Van der Kamp is not the ancestor: De Labore Solis (1988), the PDF at
   geocentricity.com, returns 13 hits for "Ptolem", one for "epicycl" and zero for
   "Venus" or "phases" on the 2026-08-10 search. So the earliest text located in the
   canon is Bouw 1992 for strand (b); strands (a) and (c) are mainstream scholarship
   being quoted. UNTRACED RATHER THAN GUESSED is the honest state for the cluster as a
   whole, and the gloss claims an ancestor and nothing more.

3. THE THREE ITEMS DO NOT MAP ONE-TO-ONE, AND ITEM 218 IS THE PROBLEM.
     23  "Ptolemaic predictive accuracy."   -> the accuracy claim, strand (a). Clean.
     265 "Planet brightness epicycles."     -> the distance/apparent-size material:
         Hawking's lunar objection, Butterfield's footnote on Copernicus being "puzzled
         by the variations he had observed in the brightness of the planet Mars", and
         the "adjust the epicycles" answer. Clean enough.
     218 "Venus transits epicyclic math."   -> AMBIGUOUS, and the ambiguity matters.
         Reading A, Venus crossing the solar disc: "transit of Venus" and "transits of
         Venus" both return ZERO hits in the full-text OCR of the seventh-edition
         complete scan (5.4 MB, searched 2026-08-10), and "Horrock" and "Rudolphine"
         return zero there too. On that reading the item is an unsourced_addition
         relative to everything searched, and it is also false: transits are the one
         prediction pre-Keplerian tables could not make.
         Reading B, Venus passing across / in front of the Sun in the sense of the
         PHASES argument: that material is everywhere in the book, under its own
         heading, and the item sits in the cluster on that reading.
   The entry answers BOTH readings rather than choosing the convenient one. Do not
   quietly settle it in a later edit without going back to the corpus.

4. THE KERNEL, AND IT IS ARITHMETIC RATHER THAN RHETORIC. Ptolemy's epicycle-to-
   deferent ratios are the heliocentric orbital radii. Recomputed here 2026-08-10 from
   the Almagest parameters as tabulated by Linton, From Eudoxus to Einstein, ch. 3
   (deferent = 60):
     Mercury 22;30 -> r/R = 0.3750  vs a = 0.3871 AU   (-3.1%)
     Venus   43;10 -> r/R = 0.7194  vs a = 0.7233 AU   (-0.5%)
     Mars    39;30 -> R/r = 1.5190  vs a = 1.5237 AU   (-0.3%)
     Jupiter 11;30 -> R/r = 5.2174  vs a = 5.2026 AU   (+0.3%)
     Saturn   6;30 -> R/r = 9.2308  vs a = 9.5549 AU   (-3.4%)
   Inferior planets take the ratio directly, superior planets its reciprocal, because
   for the superior planets it is the EPICYCLE that stands in for the Earth's orbit.
   Linton prints Saturn as 6;32, which moves it to 9.18 and -3.9%; use whichever, and
   say which. Mercury's Ptolemaic model has the extra crank mechanism, so treat 0.375
   as an approximation for that planet only. Three of five land inside half a per cent.
   THAT is what "Ptolemaic predictive accuracy" consists of, and it is a measurement of
   the Copernican solar system recorded in geocentric coordinates.
   Second half of the kernel: the epicycle vector of every superior planet stays
   parallel to the Earth-mean-Sun line and completes one turn per YEAR (Linton, same
   chapter). Five separate brute coincidences in Ptolemy; one fact in Copernicus.
   Do not overplay this against a TYCHONIAN — Tycho explains it with a physical Sun
   that carries the planets. It bites the pure Ptolemaic model, which is the one the
   cluster names.

5. WHERE THE GEOCENTRIC MODEL WAS ACTUALLY BEATEN, IN ORDER, AND EVERY STEP IS A
   MEASUREMENT. This is the cluster note's claim and it holds up.
     - The Moon. Ptolemy's own lunar parameters swing the distance from about 33 to
       about 64 Earth radii, so the disc should very nearly double; the observed swing
       is 14 per cent (Linton, ch. 3). This is the one place a geocentric model made a
       checkable distance claim in antiquity, and it was wrong by a factor of about 1.9
       against 1.14.
     - Tycho's 1572 nova and 1577 comet: no measurable diurnal parallax, so both are
       beyond the Moon, so the solid spheres go. Measurement, not decree.
     - 1610, Venus gibbous and full. Kills the PURE Ptolemaic ordering. The source
       concedes this completely and answers with four fixes, of which its own text says
       "Option (c) is essentially the model proposed by Tycho Brahe."
     - 1627 Rudolphine Tables: "generally around thirty times better than those of
       previous and competing tables" (Cambridge HPS, Starry Messenger). 1631, Gassendi
       observes the Mercury transit Kepler predicted; the ingress ran early against
       Kepler's time by close to five hours (Mignard/OCA transit pages), which is the
       scale of the residual error in the BEST tables of the day. 1639, Horrocks
       predicts and he and Crabtree observe the transit of Venus after correcting
       Kepler's Venus orbit.
     - 1728 Bradley's aberration, 1838 Bessel's parallax. Barbour's own qualifying
       clause is where those land — see note 6.
   THE TRANSIT ARITHMETIC, and it is the cleanest thing in the entry: the Sun's
   semi-diameter is about 16'. A latitude error of one degree is 60', i.e. nearly four
   solar radii — the difference between a transit and no transit at all. Pre-Tychonic
   tables carried longitude errors of DEGREES: Ptolemy's Jupiter-Saturn conjunction of
   August 1563 was out by nearly a month and Copernicus's by days (MacTutor, Brahe).
   So a transit prediction is not a thing epicyclic tables were in a position to make,
   and saying so needs no polemic.

6. THE HEDGE RULE ON OUR SIDE — THE ONE SENTENCE THAT MUST NOT BE TRUNCATED. Barbour,
   as the book quotes him: the Tychonic system "is a special case of the Ptolemaic one,
   is kinematically identical to Copernicus's EXCEPT IN ITS RELATION TO THE DISTANT
   STARS." Quoting that to the comma before "except" would be exactly the offence this
   project exists to name. The clause is quoted whole in the gloss, in the steelman and
   in the refutation, and it is also where the discriminator lives: aberration and
   parallax are relations to the distant stars. Note what this does and does not buy —
   it separates Tycho from Copernicus, and it does NOT separate a stationary Earth from
   a moving one all by itself, because a Tychonian can always inflate the errors on the
   parallaxes. The honest form of the point is the CONSISTENCY of aberration across the
   parallax range, which is A03's argument and is cross-linked rather than restated.

7. THE INTERNAL TENSION WITH D14, STATED CAREFULLY BECAUSE IT IS EASY TO OVERSTATE.
   Items 86 and 352 of the same specimen ("Dark matter patchwork like epicycles.",
   "MOND epicycle analogy.") use "epicycle" to mean an ad hoc patch that discredits the
   theory carrying it. Items 23 and 265 use epicyclic astronomy as a predictive success.
   Those two are NOT flatly contradictory — "accurate but ad hoc" is a coherent position
   and is roughly Duhem's. What they cannot both support is the INFERENCE: if the
   predictive success of a fitted model is no evidence for the model (D14's premise),
   then Ptolemaic accuracy is no evidence for geocentrism either. Publish it in that
   conditional form. A curmudgeon will otherwise, correctly, refuse it.

8. VERDICT. STANDARD PHYSICS ("real, already explained, does not discriminate") kept,
   and two alternatives were weighed properly rather than waved at.
   SELF-CONTRADICTED ("the claim's own source, or another item on the same list, points
   the other way") has a real case: the source's own repair of the Ptolemaic model is
   Tycho's, in which every planet orbits the Sun, and its own authority Barbour attaches
   the distant-stars exception. It was rejected because the cluster's HEADLINE claim —
   geocentric models predicted planetary positions well — survives all of that intact
   and is simply true. Scoring it as a self-contradiction would be scoring the repair
   rather than the claim.
   MISLEADING ("real data, wrong conclusion made to look supported") was rejected for
   the same reason plus a tone reason: the source states the accuracy claim at about the
   right strength, quotes a real historian for it, and concedes the Venus problem in its
   own voice. The party doing the overstating is the list, and the compression block is
   the correct place to say so.
   The residue is item 218, which is a bad fit for any verdict because it is a bad fit
   for the cluster. That is an assignment problem, filed in record_problems, not a
   reason to move a verdict that is right about the other two.

9. QUOTE PROVENANCE AND EDITIONS — READ THIS BEFORE CHANGING A PAGE NUMBER.
   Two scans were read in full-text OCR on 2026-08-10:
     (A) `GallileoWasWrong` — 2006, "Volume I, The Scientific Evidence", 3.3 MB OCR.
     (B) `galileo-was-wrong-the-church-was-right-sungenis-vol-1-3-complete` — seventh
         edition, Vols 1-3, 5.4 MB OCR.
   The passage quoted in this entry is present in BOTH, word for word as transcribed:
   (A) ch. 4, printed pp. 211-212; (B) Vol. I ch. 2, printed pp. ~211-212. The Barbour
   material is in (B) only, at Vol. I ch. 1 printed pp. 40-41. Neither was checked
   against a print copy and the locator says so. The chapter NUMBERS move between
   editions while the printed page numbers happen to coincide for the four-fixes
   passage; that coincidence is a trap, so the locator names the chapter title as well.
   OCR notes: (B) renders "scraped" as "scrapped" relative to (A) in the sentence "The
   model itself did not have to be scraped" — (A) has "scraped", (B) has "scrapped".
   Nothing here rests on that word. (B) also renders Al-Zarqali as "Al-Zargali".

10. DEFECTS IN OUR OWN RECORD, reported up, NOT edited here:
    (a) D03 originator_work "Galileo Was Wrong, Vol. II" — the material is Vol. I in
        both arrangements (note 1).
    (b) D03 originator "Robert Sungenis" / year "2006" — Bouw 1992 is the earlier canon
        text for the Venus strand and is quoted by name in the book; Gingerich, Koestler
        and Barbour are the sources of the other two strands and are `real_source`
        material. Withdraw to untraced rather than substituting Bouw: he is quoted for
        one strand of three, which is an ancestor, not an originator.
    (c) D03 real_source=None while the book's accuracy claim rests on a named Gingerich
        publication and its Venus answer on a named Barbour publication.
    (d) item 218's assignment. On the transit reading it belongs nowhere in D03.
"""

ENTRY = {

"D03": dict(

    tldr=("The claim is true, and the source makes it carefully — quoting Owen Gingerich and "
          "Arthur Koestler rather than asserting it: before Kepler, Ptolemaic tables really "
          "were about as good as Copernican ones. What that accuracy is made of is the "
          "giveaway, because Ptolemy's epicycle-to-deferent ratios encode the planets' "
          "distances from the Sun, and they return 0.72, 1.52 and 5.22 AU for Venus, Mars and "
          "Jupiter, within half a per cent of the modern values. The model was not put down by "
          "decree; it was overturned in steps and every step was a measurement, starting with "
          "a Moon that its own parameters require to nearly double in apparent size against an "
          "observed variation of 14 per cent."),

    passage=dict(
        work="WRK-SUNGENIS-2006",
        pd=False,
        locator=("Vol. I, in the section answering the phases-of-Venus objection — ch. 4 at "
                 "printed pp. 211–212 of the archive.org OCR text of the 2006 scan (item "
                 "GallileoWasWrong, title page “Volume I / The Scientific Evidence”), and the "
                 "same wording at Vol. I ch. 2, “Objection #16: Don't the Phases of Venus "
                 "Disprove Ptolemy?”, printed pp. 211–212 of the seventh-edition scan (item "
                 "galileo-was-wrong-the-church-was-right-sungenis-vol-1-3-complete). Neither "
                 "checked against a print copy"),
        quote=("As we noted previously, before Kepler's improvements to the heliocentric "
               "model, Copernicus' system was no more accurate than Ptolemy's, despite the "
               "fact that Copernicus used more epicycles than Ptolemy. … As it stands, there "
               "was a lot of room to make adjustments to Ptolemy's model to fit the "
               "observations, but no one was willing to do so"),
        gloss="""<p><strong>Both halves of that sentence are load-bearing, and the second one is a concession.</strong> The claim is <em>comparative and dated</em> &mdash; Ptolemy against Copernicus, <em>before</em> Kepler &mdash; and it is correct. The claim is not that the Ptolemaic model was accurate full stop, and it is not that it stayed competitive after 1627. Then the book states in its own voice that the adjustments which would have kept it competitive <em>were never made</em>. Everything the list wants from this cluster lives in the gap between those two sentences.</p>
<p><strong>Whose finding the accuracy claim is.</strong> Not the movement&rsquo;s. In the seventh edition it is carried by a quotation of <strong>Owen Gingerich</strong>, reaching the page at second hand through Lakatos: <em>&ldquo;in Tycho&rsquo;s observation books, we can see occasional examples where the older scheme based on the Alfonsine Tables yielded better predictions than could be obtained from the Copernican Prutenic Tables&rdquo;</em> (<em>Science Year</em> 1973, pp. 266&ndash;267, as quoted). The neighbouring material is Koestler&rsquo;s: the count of forty Ptolemaic epicycles against Copernicus&rsquo;s forty-eight comes from <em>The Sleepwalkers</em>, pp. 194&ndash;195 and 579&ndash;580, and the book cites it as such. Gingerich is also the source of the book&rsquo;s own correction to the opposite legend &mdash; that the 1969 <em>Britannica</em> claim of forty to sixty epicycles per planet was one nobody could evidence. The book is reporting real history of science accurately, and the history of science is not on anybody&rsquo;s side here.</p>
<p><strong>What the book proposes instead, in its own words.</strong> The four repairs it offers for the Ptolemaic model are: elliptical paths around the Sun; the Sun&rsquo;s orbit made the deferent with the epicycle radius set to the true Sun&ndash;planet distance; the Sun&rsquo;s motion in one epicycle with the planets&rsquo; epicycles centred on the Sun; or the Earth aligned to the stars rather than the Sun. It then writes: <em>&ldquo;All four solutions would make the paths cycloidal with respect to the Earth and all will account for the phases of Venus. Option (c) is essentially the model proposed by Tycho Brahe.&rdquo;</em> In three of the four, the planets go round the Sun.</p>
<p><strong>The seventh edition adds the strongest version of the point, and it is Julian Barbour&rsquo;s.</strong> At Vol. I ch. 1, printed pp. 40&ndash;41, it quotes <em>Absolute or Relative Motion</em>, Vol. I (Cambridge University Press, 1989), pp. 224&ndash;225: the Ptolemaic theory left six free parameters to be fixed by guesswork, and fixing them so that <em>&ldquo;the deferents of Mercury and Venus were taken equal to the earth-sun distance and the deferents of the superior planets to their actual distances from the sun&rdquo;</em> reproduces the Copernican geometry exactly &mdash; <em>&ldquo;This in fact is the system which Tycho Brahe proposed&hellip; the Tychonic system, which is a special case of the Ptolemaic one, is kinematically identical to Copernicus&rsquo;s except in its relation to the distant stars.&rdquo;</em> That last clause is quoted here in full deliberately. It is the true thing this argument found, it is a working physicist&rsquo;s sentence rather than a movement author&rsquo;s, and it names the exact place the equivalence stops.</p>
<p><strong>What this passage is being cited as.</strong> An ancestor, not an origin. The Venus half is quoted by the book from Gerardus Bouw, <em>Geocentricity</em> (1992), pp. 309&ndash;310, fourteen years earlier; the accuracy half is Gingerich and Koestler; the equivalence half is Barbour, a working physicist writing history. Each of the three strands reaches this book from an earlier named source, and the earliest of them standing inside the geocentric literature itself is Bouw&rsquo;s 1992 chapter &mdash; an ancestor for one strand of three, which is not the same thing as an author for the argument.</p>"""),

    steelman=dict(
        description="""<p><strong>SURFACE (weak &mdash; do not use).</strong> &ldquo;Epicycles were a mess of ad hoc circles piled on circles, and Copernicus swept them away.&rdquo; This is false, it is famously false, and the source has already documented that it is false with a citation the defender will produce. Gingerich traced the &ldquo;forty to sixty epicycles per planet&rdquo; claim to the 1969 <em>Encyclop&aelig;dia Britannica</em> and found nobody able to evidence it; Copernicus&rsquo;s own system needed small epicyclets of its own to replace the equant. Anyone opening with the epicycle sneer is repeating an error that this book corrects.</p>
<p><strong>DEEPER.</strong> The predictive parity is real and it is mainstream. Tycho, aged sixteen, found the August 1563 conjunction of Jupiter and Saturn mistimed by nearly a month in the Ptolemaic tables and by days in the Copernican ones &mdash; both wrong, one worse. Kuhn conceded the parity; Gingerich reports occasional cases where the older Alfonsine scheme beat the Copernican Prutenic Tables outright. A defender who says only this has said nothing a historian of astronomy would contest.</p>
<p><strong>KERNEL.</strong> The strongest form is Barbour&rsquo;s and the book has already found it. The Ptolemaic scheme fixes the <em>ratio</em> of epicycle to deferent from observation but leaves the absolute size of each orbit free &mdash; six free parameters. Fix them at their true values and the Ptolemaic system <em>becomes</em> the Tychonic system, which is <em>&ldquo;kinematically identical to Copernicus&rsquo;s except in its relation to the distant stars.&rdquo;</em> So the accuracy is not a coincidence and not a fudge: the geocentric model was carrying the right geometry all along, in coordinates centred on us, and no amount of positional astronomy inside the solar system can prise the two apart. <em>Given that, on what basis was one of them abandoned?</em></p>""",
        why_it_doesnt_save_claim="""<p>Because the kernel is a statement about <strong>which quantities the two frameworks share</strong>, and it comes with its own boundary marked. Barbour did not write that the systems are identical. He wrote that they are identical <em>except in its relation to the distant stars</em> &mdash; and the two measurements that decided the question, Bradley&rsquo;s aberration in 1728 and Bessel&rsquo;s parallax in 1838, are both relations to the distant stars. The equivalence the argument leans on is precisely bounded away from the evidence that settled the matter.</p>
<p>And the shared geometry is shared in a specific direction. Ptolemy&rsquo;s epicycle-to-deferent ratios return the planets&rsquo; distances <em>from the Sun</em> &mdash; 0.72 for Venus, 1.52 for Mars, 5.22 for Jupiter, against modern 0.7233, 1.5237 and 5.2026 &mdash; and the epicycle vector of every superior planet stays parallel to the Earth&ndash;Sun line, turning once a year. A model that measures the Sun-centred orbit radii to half a per cent and then needs a separate annual coincidence for each planet to hide the fact is not neutral between the two pictures; it is one of them written in the other&rsquo;s coordinates. Tycho&rsquo;s system answers that by making the Sun a physical hub that carries the planets, which is why it survives the point &mdash; but Tycho&rsquo;s system is not the one this cluster names, and it is a <strong>spherical, planets-orbit-the-Sun</strong> model on a list whose headline is a flat Earth.</p>"""),

    refutation="""<p><strong>Start by conceding the whole of it, because the concession is not grudging and the source did not overstate.</strong> Geocentric planetary astronomy really was predictively good. Richard Fitzpatrick, reconstructing the <em>Almagest</em> models, reports that Ptolemy&rsquo;s scheme applied to Mars places the planet against the fixed stars to a maximum error of about 14 arc minutes &mdash; half the width of the Moon &mdash; and that the <em>Almagest</em>&rsquo;s geocentric solar orbit, driven with modern figures, is good to about one arc minute. The harder evidence is institutional: the Alfonsine Tables, computed on Ptolemaic machinery, ran European astronomy for three centuries, and a 301-comparison audit of Alfonsine against Copernican predictions for the 1560s finds Ptolemy ahead on the inferior planets and the Sun while Copernicus is ahead on the superior ones &mdash; a split decision, not a rout. Copernicus did not improve on them: Tycho, at sixteen, watched the August 1563 conjunction of Jupiter and Saturn arrive nearly a month away from the Ptolemaic prediction and days away from the Copernican one, and Gingerich reports occasional cases in Tycho&rsquo;s notebooks where the older scheme simply won. Kuhn moved from &ldquo;measurably superior&rdquo; in 1957 to parity by 1960. Any answer to this cluster that begins by disputing the accuracy is answering a claim the historians settled against it.</p>

<p><strong>What the verdict ranges over.</strong> Not &ldquo;the predictions were bad.&rdquo; They were good. The claim on the table is that their being good is evidence for a fixed, central Earth. It is not, for a reason the accuracy itself supplies.</p>

<h4>1. What the accuracy is made of: the Copernican solar system, written down in geocentric coordinates</h4>

<p>An epicycle model has two free shape parameters per planet, and only their <em>ratio</em> is fixed by the observations &mdash; the retrograde loops determine how big the epicycle is relative to the deferent, and nothing in naked-eye astronomy determines the absolute size of either. So look at what Ptolemy&rsquo;s ratios say. Taking his deferent as 60 and his epicycle radii from the <em>Almagest</em> as tabulated by Linton, and reading the ratio directly for the inferior planets and its reciprocal for the superior ones (recomputed here, 2026-08-10):</p>

<p style="margin-left:1.5em">Mercury 22;30 &rarr; <strong>0.375</strong> (modern 0.3871, &minus;3.1%)<br>
Venus 43;10 &rarr; <strong>0.7194</strong> (modern 0.7233, &minus;0.5%)<br>
Mars 39;30 &rarr; <strong>1.519</strong> (modern 1.5237, &minus;0.3%)<br>
Jupiter 11;30 &rarr; <strong>5.217</strong> (modern 5.2026, +0.3%)<br>
Saturn 6;30 &rarr; <strong>9.231</strong> (modern 9.5549, &minus;3.4%)</p>

<p>Those are the semi-major axes of the planetary orbits <em>about the Sun</em>, in astronomical units, three of the five inside half a per cent. They are sitting in the <em>Almagest</em>, fitted from second-century observations of retrograde arcs, in a book whose author took the Earth to be at rest in the middle. (Mercury is the weakest entry because Ptolemy&rsquo;s Mercury model carries an extra crank mechanism, so 0.375 is an approximation for that planet only; Linton gives Saturn&rsquo;s epicycle as 6;32, which moves it to 9.18 and &minus;3.9%.)</p>

<p>The second half of the same point is older than any of us: the epicycle radius vector of every superior planet stays parallel to the line from the Earth to the mean Sun, and completes exactly one revolution per year. Three planets, three separate annual coincidences, unexplained in Ptolemy. In the heliocentric reading they are not three facts but one, and it is the Earth&rsquo;s own orbit showing through. <strong>The accuracy of the geocentric model is therefore not evidence about where the Earth is. It is evidence that a kinematic scheme fitted to good data reproduces good data</strong> &mdash; and, on inspection, that this particular scheme had the Sun-centred distances in it the whole time.</p>

<h4>2. The one place a geocentric model made a checkable claim about distance, it lost</h4>

<p>Positions were the model&rsquo;s strength. <em>Distances</em> were where it could be caught, and it was caught in antiquity. Ptolemy&rsquo;s lunar model, driven to fit the Moon&rsquo;s motion in longitude, swings the Moon&rsquo;s distance from about 33 to about 64 Earth radii. That requires the lunar disc to grow by a factor of nearly 1.9 between apogee and perigee. The observed variation is <strong>14 per cent</strong>. This is not a modern objection dressed up: it is arithmetic on Ptolemy&rsquo;s own published parameters, and it is why Ibn al-Sh&#257;&#7789;ir and later Copernicus rebuilt the lunar model.</p>

<p>The source&rsquo;s answer to that objection, met in Stephen Hawking&rsquo;s phrasing, is that the textbook diagrams of Ptolemy&rsquo;s system are not drawn to scale and that with the epicycles properly adjusted the correct lunar distance could have been accommodated. The first half is true and irrelevant &mdash; the objection is to the numbers in Book V of the <em>Almagest</em>, not to anybody&rsquo;s illustration. The second half is a promissory note, and the book&rsquo;s own next move is to say the note was never redeemed: <em>&ldquo;there was a lot of room to make adjustments to Ptolemy&rsquo;s model to fit the observations, but no one was willing to do so.&rdquo;</em> A model that could have been made to fit is not a model that fitted.</p>

<h4>3. Venus: the item, both ways it can be read, and the fix that is Tycho&rsquo;s</h4>

<p><em>Item 265, brightness.</em> Concede it, because it is right, and it is the strongest of the three items. Epicycles genuinely do deliver the brightness variation, and this was one of their historical reasons for existing &mdash; the homocentric spheres of Eudoxus and Aristotle cannot vary a planet&rsquo;s distance at all, and were criticised in antiquity for exactly that. Run the numbers on Mars. Ptolemy&rsquo;s parameters &mdash; deferent 60, epicycle 39;30, the Earth offset 6 from the deferent&rsquo;s centre &mdash; put its geocentric distance between 14.5 and 105.5 units, a ratio of <strong>7.28</strong>; modern orbital elements put the true range between 0.365 and 2.683 AU, a ratio of <strong>7.36</strong>. Inverse-square on those gives brightness swings of 53 against 54. The epicycle reproduces the observed swing to about one per cent &mdash; and it does so <em>because</em> the epicycle is the Earth&rsquo;s orbit, which is what makes the distance vary in the first place.</p>

<p><em>Item 218, transits.</em> The item admits two readings and both are answered here rather than the convenient one being chosen. On the reading where &ldquo;transits&rdquo; means Venus crossing the face of the Sun, the phrase &ldquo;transit of Venus&rdquo; is not located anywhere in the full-text OCR of the seventh-edition scan searched for this entry, nor are &ldquo;Horrocks&rdquo; or &ldquo;Rudolphine&rdquo;; and the claim would be false on the history. A transit prediction is a prediction about <em>latitude</em>, at the scale of the solar disc: the Sun&rsquo;s semi-diameter is about 16 arc minutes, so an error of one degree &mdash; 60 arc minutes, nearly four solar radii &mdash; is the difference between a transit and nothing at all. Pre-Tychonic tables were carrying errors measured in degrees and in some cases, as at the 1563 conjunction, in weeks. The first transit prediction on record is Kepler&rsquo;s, of Mercury on 7 November 1631, computed from the Rudolphine Tables &mdash; tables that were elliptical, heliocentric, and about thirty times better than anything before them. Gassendi observed it, and found Mercury had entered early against Kepler&rsquo;s time by close to five hours: that was the residual error in the <em>best</em> tables in the world. The first transit of Venus predicted and seen was Horrocks&rsquo;s, on 4 December 1639, and he got it by correcting Kepler&rsquo;s Venus orbit after Kepler had expected a near miss. Both predictions came out of the mathematics that had just displaced the epicycle, within twelve years of its publication.</p>

<p>On the other reading &mdash; Venus passing in front of the Sun in the sense of the <em>phases</em> argument &mdash; the item does have a home in the source, under its own heading, and the source&rsquo;s answer deserves to be met at full strength. It is right on the history: Galileo&rsquo;s 1610 observation refutes the <em>pure</em> Ptolemaic ordering, in which Venus sits permanently between Earth and Sun and can never be seen more than a crescent, but it does not establish heliocentrism, because the Capellan and Tychonic arrangements produce the same phases. That is the standard scholarly position and the book states it correctly.</p>

<p><strong>Then look at what the repair costs.</strong> The book&rsquo;s four fixes, in its own text, are: elliptical paths around the Sun; the Sun&rsquo;s orbit as the deferent with the epicycle radius set to the true Sun&ndash;planet distance; the Sun&rsquo;s motion in one epicycle with the planets&rsquo; epicycles centred on the Sun; or the Earth aligned to the stars rather than to the Sun. It adds: <em>&ldquo;Option (c) is essentially the model proposed by Tycho Brahe.&rdquo;</em> In three of the four the planets orbit the Sun. The rescue of &ldquo;the Ptolemaic model accounts for Venus&rdquo; is the abandonment of the Ptolemaic model in favour of one in which Venus goes round the Sun &mdash; and it was Galileo&rsquo;s telescope, not a committee, that forced the choice.</p>

<h4>4. Where the equivalence stops, in the words of the source&rsquo;s own authority</h4>

<p>The book&rsquo;s best card is Barbour&rsquo;s: fix the Ptolemaic system&rsquo;s six free parameters at their true values and you get the Tychonic system, which is <em>&ldquo;a special case of the Ptolemaic one&rdquo;</em> and is <em>&ldquo;kinematically identical to Copernicus&rsquo;s except in its relation to the distant stars.&rdquo;</em> Every word of that is correct and it is quoted here whole, because stopping it one clause early would be the same trick this page exists to name.</p>

<p>The clause that finishes it is the answer. Relations to the distant stars are exactly what was measured next. Bradley found stellar aberration in 1728 &mdash; an annual ellipse of about 20.5 arc seconds, the same for every star regardless of its distance. Bessel measured the parallax of 61 Cygni in 1838 at 0.314&Prime; &plusmn; 0.020&Prime;, and <em>Gaia</em> DR3 now publishes parallaxes for about 1.47 billion sources. The two together are the discriminator, and it is their <em>combination</em> rather than either alone: aberration is flat across the whole parallax range while parallax varies by orders of magnitude across it, which is what a moving observer produces and a turning sky cannot &mdash; the argument set out at <a href="#ARG-A03">ARG-A03</a> and <a href="#ARG-A05">ARG-A05</a> rather than restated here. Positional astronomy inside the solar system never could have settled this. That is Barbour&rsquo;s point, and it is why nobody claims it was settled there.</p>

<h4>5. The inference the cluster needs, and the list&rsquo;s own answer to it</h4>

<p>Strip the history away and the argument is: <em>this model predicted well, therefore this model is true</em>. That inference is invalid, and the specimen list knows it is invalid, because it relies on the invalidity elsewhere. Items 86 and 352 &mdash; <em>&ldquo;Dark matter patchwork like epicycles&rdquo;</em>, <em>&ldquo;MOND epicycle analogy&rdquo;</em>, both in <a href="#ARG-D14">ARG-D14</a> &mdash; use &ldquo;epicycle&rdquo; as the standing name for a parameterised patch whose predictive success proves nothing about the world. That is a defensible position. It is not one that can be held at item 86 and dropped at item 23. Either the predictive success of a fitted kinematic model is evidence for the model, in which case the epicycle jibe against modern cosmology collapses, or it is not, in which case Ptolemaic accuracy is not evidence for a stationary Earth. The list needs both answers at once.</p>

<h4>6. And every model in this cluster is a model of a spherical Earth</h4>

<p>Ptolemy&rsquo;s <em>Almagest</em> argues for a spherical Earth at Book I, chapter 4, and does so observationally &mdash; from risings and settings occurring at different local times as one moves east or west, and from the changing altitude of the pole as one moves north or south &mdash; before it goes on in chapters 5 and 7 to argue that the Earth is central and motionless. Sphericity is the earlier and better-supported half of the package. Tycho&rsquo;s system, which is what the source&rsquo;s repairs converge on, is likewise a spherical Earth with the planets circling the Sun. The three items in this cluster appear among 461 collected as evidence that the Earth is not a spinning ball, and they are borrowed from astronomers who thought it was a ball and calculated on that assumption &mdash; the same collision recorded at <a href="#ARG-D02">ARG-D02</a>. On its own terms the cluster is not a flat-earth argument at all; it is a Tychonian one, on loan.</p>

<p><strong>What is left, stated plainly.</strong> Geocentric models predicted planetary positions accurately, they were not beaten on accuracy by Copernicus, and the source says both of those things at about the right strength with real citations behind them. The accuracy consisted of the heliocentric orbital radii recorded in Earth-centred coordinates, to half a per cent. The model was superseded step by step, and every step was a measurement: the lunar diameter that would not double, Tycho&rsquo;s parallax-free comet, Galileo&rsquo;s gibbous Venus, a set of tables thirty times better that could predict a transit, then aberration and parallax. That is the whole of the answer, and none of it depends on the epicycle having been a bad idea. It was a good idea, and what it was good at was measuring the solar system.</p>""",

    advocate=dict(
        best_defense=(
            "You have conceded the argument and then declared victory, so let us be clear "
            "about what is left standing. One: you agree the predictions were accurate and "
            "that Copernicus was no better. Two: you agree the phases of Venus do not "
            "establish heliocentrism. Three: you quote Barbour agreeing that the Tychonic "
            "system is a special case of the Ptolemaic one and kinematically identical to "
            "Copernicus's. That is our case, in your words, with your citations. "
            "Now your two counter-moves. Your epicycle-ratio table is the best thing on the "
            "page and it is also circular: you convert our parameters into 'astronomical "
            "units' — a unit defined by the Earth's orbit — and then announce that they "
            "encode the Earth's orbit. Of course they do; they encode the Sun-planet "
            "separation, which every geocentrist since Tycho has agreed exists, because the "
            "Sun carries the planets. You have measured the solar system and called it a "
            "proof of what the solar system is centred on. Your one-year 'coincidence' is "
            "the same error: in the Tychonic system it is not a coincidence at all, it is "
            "the Sun's annual circuit, and you say so yourself in one line before moving on. "
            "As for the Moon, you are holding a second-century model to a standard you do "
            "not hold your own to. Newton could not predict the lunar motion either; it took "
            "two centuries and Delaunay's 1,800-term series, and lunar theory was in crisis "
            "well into the twentieth century. A parameter that needed adjusting is a "
            "parameter that needed adjusting. Everything reduces, in the end, to aberration "
            "and parallax — 'relations to the distant stars' — which is precisely the ground "
            "we have contested for a hundred and fifty years and which you handle by "
            "pointing at two other pages. And on your last section: yes, this is a "
            "Tychonian argument on a flat-earth list. You have found that the list is "
            "incoherent. You have not found that we are."),
        survives=4,
        preemptive=(
            "Four, and it is earned by the first and last moves, not by the lunar one. "
            "THREE THINGS MUST STAY IN THE TEXT and one must be added if an editor ever "
            "trims. (a) THE UNIT OBJECTION IS PARTLY RIGHT AND THE BODY MUST NOT PRETEND "
            "OTHERWISE. Expressing the ratios in AU does not by itself beat a Tychonian, "
            "because Tycho grants the Sun-planet distances. The paragraph therefore already "
            "says what the ratios establish — that the scheme is 'one of them written in "
            "the other's coordinates' — and stops there, and the steelman's closing "
            "sentences concede in our own voice that Tycho survives the point and that it "
            "bites the PURE Ptolemaic model, which is the model the cluster names. If a "
            "later edit upgrades that paragraph into a proof of heliocentrism, the "
            "defender's charge of circularity becomes correct and the strongest section on "
            "the page becomes the weakest. (b) THE ONE-YEAR COINCIDENCE MUST KEEP ITS "
            "TYCHONIC CAVEAT ADJACENT, for the same reason and in the same sentence, not in "
            "a footnote. (c) THE DISCRIMINATOR MUST NOT BE OUTSOURCED WITHOUT BEING STATED. "
            "The body carries the actual shape of the argument — aberration flat across a "
            "parallax range that varies by orders of magnitude, so that neither measurement "
            "alone does the work — before it links to A03 and A05. A cross-link that "
            "replaces the argument rather than extending it is what lets a defender say the "
            "section ends in a pointer. (d) ON THE MOON, ANSWER THE ANACHRONISM CHARGE "
            "RATHER THAN DROPPING THE POINT: the objection is not that Ptolemy's lunar "
            "model was imperfect, it is that his OWN parameters entail a nearly doubled "
            "disc and the observed swing is 14 per cent — a discrepancy visible to the "
            "naked eye, known in antiquity, and conceded by the source as never repaired. "
            "That is not a demand for modern precision. Finally, on 'you have found the "
            "list is incoherent, not that we are': agree in public and keep the "
            "distinction, exactly as the compression block does. The finding is about the "
            "list. The book is the careful party here and the page says so in its own "
            "voice."),
    ),

    straw_man=dict(
        identified=True,
        detail=("Answering the lunar-distance objection — Ptolemy's own parameters put the Moon "
                "between about 33 and 64 Earth radii, so its disc should nearly double while the "
                "observed swing is 14 per cent — the book replies that the textbook diagrams of "
                "Ptolemy's system are not drawn to scale, that without accurate scales such "
                "diagrams prove nothing “except perhaps a bias against Ptolemy”, and that "
                "Ptolemy's model was “neither drawn to scale nor was ever adjusted for errors.” "
                "The objection is not about anybody's illustration. It is arithmetic on the "
                "numerical parameters Ptolemy publishes in Book V of the Almagest, and it was "
                "raised on those grounds by Ibn al-Shāṭir and by Copernicus centuries before "
                "any textbook diagram existed. The straw man is confined to that reply. The "
                "book's treatment of the phases of Venus is not a straw man and must not be "
                "filed as one: its claim that the phases refute the Ptolemaic ordering without "
                "establishing heliocentrism is the standard scholarly position, and its Barbour "
                "and Gingerich citations are accurate.")),

    compression=dict(
        assessed=True, drifted=True,
        list_phrasing="Ptolemaic predictive accuracy.",
        source_wording=("&ldquo;&hellip;in Tycho&rsquo;s observation books, we can see "
                        "<strong>occasional examples</strong> where the older scheme based on "
                        "the Alfonsine Tables yielded better predictions than could be obtained "
                        "from the Copernican Prutenic Tables&rdquo; &mdash; Owen Gingerich, "
                        "quoted in the book; and in the book&rsquo;s own voice, "
                        "&ldquo;<strong>before Kepler&rsquo;s improvements</strong> to the "
                        "heliocentric model, Copernicus&rsquo; system was no more accurate than "
                        "Ptolemy&rsquo;s&rdquo;."),
        drift_type="scope_widened",
        note=("The source&rsquo;s claim is narrow twice over. It is <em>comparative</em> &mdash; "
              "Ptolemy against Copernicus, not Ptolemy against the sky &mdash; and it is "
              "<em>dated</em>, scoped explicitly to the period before Kepler. Its evidence is a "
              "historian of astronomy reporting <em>occasional examples</em> in one observer&rsquo;s "
              "notebooks. Item 23 keeps the noun and drops the comparison, the date and the "
              "frequency, leaving a standing property of Ptolemaic astronomy. That is the "
              "widening, and it is the whole distance between a true sentence and the use the "
              "list puts it to.<br><br>"
              "<strong>The other two items drift differently, and the enum only has room for "
              "one label.</strong> <em>Item 265, &ldquo;Planet brightness epicycles&rdquo;, and "
              "item 218 on the phases reading:</em> the source&rsquo;s verbs are subjunctive "
              "throughout &mdash; the lunar distance and the phases of Venus &ldquo;could have "
              "been made as prominent and precise as they appear in the improved Keplerian "
              "model <em>if</em>&rdquo; one of four listed changes were adopted &mdash; and it "
              "closes by stating that the adjustments were never made: &ldquo;there was a lot "
              "of room to make adjustments to Ptolemy&rsquo;s model to fit the observations, but "
              "no one was willing to do so.&rdquo; The items state as accomplished what the book "
              "states as forgone. On its own that is <code>hedge_dropped</code>. "
              "<em>Item 218 on the transit reading:</em> &ldquo;transit of Venus&rdquo; and "
              "&ldquo;transits of Venus&rdquo; return zero hits, and &ldquo;Horrocks&rdquo; and "
              "&ldquo;Rudolphine&rdquo; likewise, in the full-text OCR of the seventh-edition "
              "scan searched on 2026-08-10, so on that reading the item would be an "
              "<code>unsourced_addition</code> relative to the text searched &mdash; which is a "
              "statement about that scan and not about the whole literature. "
              "<code>scope_widened</code> is recorded because item 23 carries the cluster and "
              "because the widening is the most checkable of the three: both texts are above.<br><br>"
              "<strong>What travels with the claim in the book and reaches none of the items.</strong> "
              "<em>Whose finding it is:</em> Gingerich&rsquo;s, and Koestler&rsquo;s for the "
              "epicycle counts, both cited by name. <em>The concession:</em> that Ptolemy&rsquo;s "
              "model as it stood could not deliver the phases of Venus, and that the repair which "
              "would have delivered them is, in the book&rsquo;s own sentence, &ldquo;essentially "
              "the model proposed by Tycho Brahe&rdquo; &mdash; a system in which the planets "
              "orbit the Sun. <em>The boundary:</em> Barbour&rsquo;s, that the Tychonic system is "
              "kinematically identical to Copernicus&rsquo;s <em>except in its relation to the "
              "distant stars</em>, which is the one clause that says where the equivalence ends. "
              "The book prints all three. The list prints four words.<br><br>"
              "<strong>The refutation answers the source, not the fragment:</strong> it grants the "
              "predictive parity at full strength and with the source&rsquo;s own citations, "
              "grants that the phases of Venus do not establish heliocentrism, quotes "
              "Barbour&rsquo;s sentence entire rather than to the comma before &ldquo;except&rdquo;, "
              "and puts the weight on what the accuracy is made of and on the measurements that "
              "ended the model.")),

    verdict_challenge=dict(challenged=False, proposed_verdict=None, reasoning=None),

    people=["PER-SUNGENIS", "PER-BOUW", "PER-PTOLEMY"],
    related=["D01", "D02", "D14", "A22", "A05", "R01", "R08"],

    sources=[
        dict(label="Ptolemy, Almagest — Book I ch. 4 argues that the Earth is sensibly "
                   "spherical, before chs 5 and 7 argue that it is central and motionless; "
                   "Books V and IX–XI carry the lunar model and the planetary epicycle "
                   "parameters used here",
             url="https://en.wikipedia.org/wiki/Almagest"),
        dict(label="C. M. Linton, From Eudoxus to Einstein: A History of Mathematical "
                   "Astronomy (CUP, 2004), ch. 3 — the Almagest epicycle radii on a deferent "
                   "of 60 (Mercury 22;30, Venus 43;10, Mars 39;30, Jupiter 11;30, Saturn 6;32), "
                   "the lunar distance running about 33 to 64 Earth radii so that the disc "
                   "should double against an observed 14 per cent, and the superior planets' "
                   "epicycle vector staying parallel to the Earth–mean-Sun line once a year",
             url="https://web.math.princeton.edu/~eprywes/F22FRS/Linton/From_Eudoxus_to_Einstein_A_History_of_Mathematical..._----_(3_The_Ptolemaic_universe).pdf"),
        dict(label="R. Fitzpatrick, “Ptolemy's Almagest: Fact and Fiction” and A Modern "
                   "Almagest (Univ. of Texas) — Ptolemy's scheme applied to Mars good to a "
                   "maximum error of about 14 arc minutes, and the Almagest solar orbit, driven "
                   "with modern figures, good to about 1 arc minute; and the epicycle of a "
                   "superior planet is the Earth's orbit under vector addition",
             url="https://farside.ph.utexas.edu/talks/AlmagestNotes.pdf"),
        dict(label="MacTutor, “Tycho Brahe” — the conjunction of Jupiter and Saturn of August "
                   "1563: “Neither tables based on Copernicus nor on Ptolemy gave the correct "
                   "date for the conjunction, Ptolemy's being out by nearly a month and even "
                   "Copernicus's being out by days”",
             url="https://mathshistory.st-andrews.ac.uk/Biographies/Brahe/"),
        dict(label="Cambridge HPS, Starry Messenger — “Tycho Brahe and Astronomical Tables”: "
                   "Tycho found the planets agreeing with neither the Alphonsine nor the "
                   "Prutenic Tables, and the Rudolphine Tables of 1627 were “generally around "
                   "thirty times better than those of previous and competing tables”",
             url="https://www.sites.hps.cam.ac.uk/starry/tychotables.html"),
        dict(label="Observatoire de la Côte d'Azur, transit pages — Gassendi's observation of "
                   "the Mercury transit of 7 November 1631 predicted by Kepler; ingress timed "
                   "at 5:28 and egress at 10:28, running early against Kepler's assigned time "
                   "by close to five hours",
             url="https://www-n.oca.eu/Mignard/venus2004/HTML/mercury_1631.htm"),
        dict(label="“1639 transit of Venus” — Horrocks alone predicted it, from the Rudolphine "
                   "Tables with his own correction to Venus's orbit after Kepler had expected a "
                   "near miss; observed by Horrocks and Crabtree on 4 December 1639",
             url="https://en.wikipedia.org/wiki/1639_transit_of_Venus"),
        dict(label="Thony Christie (The Renaissance Mathematicus), “The Phases of Venus and "
                   "Heliocentricity: A Rough Guide” — the phases refute the pure Ptolemaic "
                   "ordering but are equally consistent with the Capellan and Tychonic systems, "
                   "so they establish that Venus orbits the Sun and no more",
             url="https://thonyc.wordpress.com/2014/06/09/the-phases-of-venus-and-heliocentricity-a-rough-guide/"),
        dict(label="Thony Christie, “Planetary Tables and Heliocentricity: A Rough Guide” — the "
                   "Prutenic Tables rested on the same corrupted data as the Alfonsine and were "
                   "not better; the Rudolphine Tables' advantage came from Tycho's observations",
             url="https://thonyc.wordpress.com/2014/07/03/planetary-tables-and-heliocentricity-a-rough-guide/"),
        dict(label="Tipler & Bollinger, “Ptolemy versus Copernicus”, Inference — a 301-comparison "
                   "audit of Alfonsine against Prutenic predictions: Copernicus ahead on the "
                   "superior planets, Ptolemy ahead on the inferior planets and the Sun; Kuhn's "
                   "move from “measurably superior” in 1957 to parity by 1960; Gingerich (1973) "
                   "that before Tycho there was “relatively little way to distinguish between "
                   "the accuracy” of the two",
             url="https://inference-review.com/article/ptolemy-versus-copernicus"),
        dict(label="Galileo Was Wrong: The Church Was Right, Vol. I — 2006 scan, archive.org "
                   "item GallileoWasWrong; the epicycle-count material at printed pp. 41–43 and "
                   "the Ptolemy-can-be-adjusted material at printed pp. 210–212, quoting Bouw, "
                   "Geocentricity (1992), pp. 309–310",
             url="https://archive.org/details/GallileoWasWrong"),
        dict(label="Galileo Was Wrong, seventh edition, Vols 1–3 complete — archive.org item "
                   "galileo-was-wrong-the-church-was-right-sungenis-vol-1-3-complete; Vol. I "
                   "ch. 1 pp. 40–41 quotes Barbour, Absolute or Relative Motion, Vol. I (CUP, "
                   "1989), pp. 224–225, and Vol. I ch. 2 “Objection #16” carries the four "
                   "repairs and the Tycho sentence",
             url="https://archive.org/details/galileo-was-wrong-the-church-was-right-sungenis-vol-1-3-complete"),
    ],
),

}
