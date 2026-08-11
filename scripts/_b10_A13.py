# -*- coding: utf-8 -*-
"""Batch 10 — A13. "No centrifugal effects felt; equatorial bulge has another cause."

Four items: 55 "Equatorial bulge alternative cause.", 105 "Stable equatorial bulge.",
180 "No felt centrifugal force.", 257 "No equatorial centrifugal relief."
Verdict REFUTED, kept. Research notes for whoever picks this up next.

1. THE FOUR ITEMS SPLIT TWO WAYS AND THE CLUSTER NAME ONLY DESCRIBES ONE HALF.
   Items 55 and 105 concede a bulge and dispute its cause. Items 180 and 257 deny that
   any centrifugal effect is there to have a cause. Those are not the same claim, and
   the second pair contradicts the first: an equatorial bulge with "another cause" is
   still an equatorial bulge. Read the four together and the cluster is asserting both
   that the effect exists and that it does not. That is worth saying out loud in the
   entry, because it is the shortest route into the whole argument.

2. THE RECORD'S ORIGINATOR IS HALF RIGHT, AND — unusually for this project — THE
   EDITION IS RIGHT. `clusters.py` says Rowbotham, *Earth Not a Globe*, 1865. Verified
   against the Project Gutenberg transcription of the 1865 FIRST BOOK EDITION (ebook
   #69892, "Original publication: United Kingdom: Simpkin, Marshall, and co., 1865"):
   the oblate-spheroid material and the seconds-pendulum table are both in Section I,
   and the argument is reproduced with a third alternative cause added in the 1881 third
   edition (sacred-texts za39.htm, ch. XIV, "Variability of Pendulum Vibrations"). Given
   the project's standing 1865/1881 blind spot, that is a positive result and the entry
   says which edition carries what.
   BUT: Rowbotham does not offer an alternative CAUSE for the bulge. He denies the bulge
   is established at all (the meridian arcs disagree; some suggest an *oblong* figure).
   The "another cause" formulation the cluster is named for is the Machian one, and its
   earliest text located that carries it is Sungenis & Bennett. Two lineages, one cluster.

3. THE MODERN SOURCE CONCEDES BOTH PHENOMENA, IN FOUR SEPARATE PLACES, AND THIS IS THE
   ENTRY'S SPINE. All in *Galileo Was Wrong* Vol. I, archive.org item GallileoWasWrong
   (the CD-ROM issue our `works.py` record describes), printed page numbers as they
   appear on the page images of that scan (see §10 — every one was re-read from the
   footer of its own leaf on 2026-08-11, and seven were one low before that):
     - ch. 12 (Bennett, "Technical and Summary Analysis of Geocentric Cosmology"),
       p. 710 — the chapter OPENS on that page: the geokinetic claim is stated as
       "Centrifugal forces cause the water and air near the equator to rise ... the polar
       flattening and equatorial bulge. This also explains why the acceleration of gravity
       is less at the equator." READ THE FRAME. That sentence is item #2 in a numbered
       list introduced as "there are three geokinetic claims for terrestrial motion" and
       "All claims center on the inertial forces called centrifugal and Coriolis that
       explain the following effects ... based on the presumption of Earth's rotation".
       It is the opponent's claim as Bennett states it before answering it, not a
       free-standing assertion of his own, and anything that quotes it must say so.
       The Response at p. 711 does not deny any of it: "All the various effects noted
       above depend on the assumption that the inertial effects can only be caused by the
       Earth's rotation." The dispute is over attribution, not existence.
       CAUTION, same page 711. Restating Barbour and Bertotti, Bennett writes that "An
       object at the center of the hollow sphere will not be affected by the inertial
       forces. The space around the Earth will exhibit the inertial effects of the distant
       sphere, but not the Earth itself, if it is centrally located." That is the nearest
       thing to a source for item 180 found in any passage read for this entry; it sits a few
       lines BELOW the Response on the same p. 711 and pulls against it, and it is answered in
       section 5 of the refutation. Do NOT write "neither book asserts item 180" without
       reckoning with it — an earlier draft did, and it was wrong.
     - ch. 4, p. 204: "The same goes for the appeal to the Coriolis force or the
       oblateness of the Earth as proofs of the Earth's rotation. The only fact these
       particular phenomena prove is that there is a force causing their effect, not that
       a rotation of the Earth is the force." Again: the effect is granted.
     - ch. 1, p. 49: the book quotes Bertrand Russell listing "the flattening of the
       Earth at the poles, and the fact that bodies are heavier there than at the
       equator" — i.e. it prints the equatorial relief item 257 denies.
     - ch. 5, p. 239, n. 492, glossing Einstein 1911: "The Earth's poles would flatten
       from either reference frame."
   So the drift on items 180 and 257 is `reversed`, and it is reversed against BOTH
   candidate sources, since Rowbotham prints the pendulum numbers too.

4. THE MACH QUOTATION — DO NOT ACCUSE THEM OF TRUNCATING IT. At Vol. I p. 204 the book
   quotes Mach ("... there is no flattening of the Earth, no Foucault's experiment, and
   so on...") and stops at the ellipsis, which is exactly where the qualifying clause
   begins. (That is the SAME PAGE as the "not that a rotation of the Earth is the force"
   sentence above — the two are consecutive paragraphs on printed p. 204, and an earlier
   draft numbered them 203 and 204 as though they were separate pages.)
   An earlier draft of this entry was going to call that a suppressed hedge. It
   is not. At ch. 7, p. 460 the SAME VOLUME prints the passage in full — "at least
   according to our usual conception of the law of inertia. Now one can solve the
   difficulty in two ways. Either all motion is absolute, or our law of inertia is
   wrongly expressed. I prefer the second way" — and then says plainly that geocentrists
   take the first option. Check both occurrences before writing anything about this. The
   real observation is a different one and it survives: Mach's two ways are exclusive,
   the book's ch. 7 takes "all motion is absolute" while its ch. 12 leans on Mach's
   Principle, which is the other horn. The entry states that as a tension, not a gotcha,
   and notes that ch. 12's own preferred cause is an ether rather than pure relationism.

5. THE ARITHMETIC THAT KILLS ROWBOTHAM'S HALF IS INSIDE HIS OWN TWO QUOTED SOURCES, AND
   THAT IS WHY IT IS THE CENTREPIECE. He prints (a) a temperature table from Phillips's
   *Million of Facts*, p. 475 — mean annual temperature 84.2 degF at the equator falling
   to 0 degF at the pole — and (b) a thermal-expansion figure from Noad's *Lectures on
   Chemistry*, p. 41: "a change of temperature equal to 30 deg Fah. will alter its length
   1/5000th part". Multiply them out: 84.2 x (1/150000) = 5.61e-4, i.e. 0.056%. The
   variation he has to explain away, from his own pendulum figures, is
   (39.197 - 39.027)/39.027 = 0.436%. Thermal expansion is short by a factor of 7.8.
   Against the modern figure (0.530%) it is short by 9.4. And his coefficient is not a
   bad 19th-century number: 1/150000 per degF = 6.67e-6/degF, against 11.7e-6/degC =
   6.5e-6/degF for steel today. He quoted a good coefficient and did not multiply it out.
   DO NOT run this argument on the SIGN of the effect. His mechanism has the right sign
   for a fixed physical rod, and a sign argument invites a long dispute about whether the
   tabulated "length of a seconds pendulum" is a measured rod or a derived quantity.
   Magnitude is unambiguous and needs no such distinction. Stay on magnitude.
   BONUS, verified verbatim in the 1881 third-edition PDF (archive.org item
   zeteticastronomy-earthnotaglobe, printed pp. 185-186 of that scan): the enlarged edition adds
   General Sabine's 131 pendulum experiments and rests on the 23 outliers — then quotes
   Sabine saying the discrepancies are "due in a far greater degree to local peculiarities
   than to what may be more strictly called errors of observation" and Baily saying the
   vibrations "are powerfully affected, in many places, by the local attraction of the
   substratum on which it is swung". He prints the correct explanation of his own residual
   scatter. Same shape as the ARG-B06 finding about the Britannica "Levelling" article.
   (B06, NOT B05. B05 is Carpenter's canals-and-railways cluster and has no Britannica
   material in it; B06 is the Rowbotham cluster whose record note reads "He quoted the
   correction and then denied the thing it corrects for". B07 — refraction invoked ad hoc
   — quotes the same Britannica extract but for its refraction coefficient, which is a
   different finding. An earlier draft pointed the anchor at B05.)

6. THE ARC-MEASUREMENT HALF: HIS FACTS ARE MOSTLY RIGHT AND THE STEELMAN MUST SAY SO.
   The Ordnance Survey table showing degrees DECREASING northward is quoted accurately
   from Hugh Murray's *Encyclopaedia of Geography*; the Lapland degree of 57,422 toises
   is a real published figure matching the standard account of the Maupertuis expedition;
   and the later
   Swedish re-measurement in Bothnia (Svanberg and colleagues, 1801-1803) really did find
   Maupertuis's arc too long — Rowbotham himself prints the correction, "196 toises more
   than the true length".
   BUT HIS PERU DEGREE DOES NOT CHECK OUT, and an earlier draft of this entry certified
   it alongside the Lapland one. He gives "the first degree of the meridian from the
   equator as 56,653 toises". The 1911 Britannica article already cited in `sources`
   gives the Peruvian arc as 176,945 toises over 3° 7′ 3″, i.e. about 56,760 toises per
   degree for an arc centred near 1.5°S; reducing that to the equator moves it by only
   about ten toises, so the published value is near 56,750 and his figure is roughly 100
   toises (some 200 m) low. Treat it exactly as the Huygens ratio below is treated: a
   wrong number taken from a secondary source, not a fabrication — but a second one, and
   both of them inflate the disagreement his argument runs on. No search was made for a
   nineteenth-century secondary source that prints 56,653; if one turns up, say so rather
   than dropping the point.
   What the entry adds on Lapland is the direction of travel: Maupertuis's
   Lapland result implied a flattening near 1/179, far MORE oblate than the truth, so
   shortening his degree moves the number toward the modern 1/298.257, not toward zero.
   Svanberg's own published flattening was not located in the sources reached for this
   entry, so the entry gives the direction as our inference and labels it as such.
   ONE CAUTION. Rowbotham's line "Huygens gave the proportion as 577 to 875, or a
   difference of about one-third of the whole diameter" is a corrupt figure: Huygens's
   value was 577:578 (the 1911 Britannica gives 578:579), a flattening near 1/578. Note
   the digits — 578 has been scrambled to 875, and the "one-third" is then computed off
   the corruption. The same sentence stands in the 1881 third edition, so it is not a
   one-off 1865 misprint. Handle this WITHOUT calling it dishonest: it is a wrong number
   in a book, it inflates the disagreement his argument runs on, and the honest reading
   is that he took it from a secondary source and did not sanity-check it. The point that
   matters is the one underneath: Newton's 1/230 and Huygens's 1/578 differ because they
   assumed different interior density distributions, which is exactly why measuring the
   flattening became a way to measure the interior.

7. THE NUMBERS, ALL RECOMPUTED 2026-08-10 FROM GRS80 CONSTANTS (a = 6378137 m,
   1/f = 298.257222101, omega = 7.292115e-5 rad/s, gamma_e = 9.7803267715,
   gamma_p = 9.8321863685 m/s^2):
     omega^2 a = 0.0339157 m/s^2 = 0.3468% of gamma_e
     omega a   = 465.1 m/s at the equator
     gamma_p - gamma_e = 0.0518596 m/s^2 = 0.5302%; centrifugal share 65.4%, figure 34.6%
     100.00 kg weighed at the pole reads 99.47 kg at the equator
     a - b = 21384.7 m
     Clairaut: m = omega^2 a / gamma_e = 0.00346775; (5/2)m - f = 0.0053166 against the
       observed beta = 0.0053024 — agreement to 0.27%, which is the expected size of the
       second-order terms Clairaut's first-order theorem drops.
     seconds pendulum L = g/pi^2: 39.014 in at the equator, 39.221 in at the pole. Against
       Rowbotham's 39.027 and 39.197 — his table is within 0.034% and 0.061% of the
       rotating-Earth prediction at the two ends, while the effect he is explaining away
       is 0.436%.
     c/omega = 4.111e12 m = 27.5 AU (inside Neptune's orbit, outside Uranus's)
   Every one of these is a two-line calculation and the entry publishes the inputs so a
   reader can redo them.

8. WHAT IS OPEN AND MUST STAY OPEN — E01 precedent. The bulge is NOT in hydrostatic
   equilibrium and the excess is not fully explained. Chambat, Ricard & Valette, GJI
   183:727 (2010), correcting Nakiboglu: "The difference between the polar and equatorial
   radii appears to be 113 +/- 1 m (instead of 98 m) larger than the hydrostatic value."
   That is 0.53% of the 21.4 km bulge. It is attributed to mantle density structure plus
   delayed viscous relaxation from Pleistocene deglaciation, and that attribution is a
   modelling result, not a closed case. Related and equally live: J2 was decreasing
   secularly from post-glacial rebound and then reversed around 1998 (Cox & Chao,
   *Science* 297:831, 2002; Dickey et al., *Science* 298(5600):1975, 2002 — note the two
   are different volumes of the same year, an easy citation to get wrong), and the
   decadal behaviour is still being worked on (Chao 2020, doi 10.1029/2020JB019421). Say all of that
   plainly.
   BUT DO NOT USE THE VARIATIONS AS THE ANSWER TO ITEM 105, and publish their sizes when
   you mention them. The body tide is ~30 cm against a 21.4 km bulge (1 part in 70,000)
   and the J2 secular trend is a fractional ~1e-8 per year, sub-millimetre a year on the
   polar-equatorial radius difference. Answering "stable" with those, in an entry whose
   governing discipline is magnitude and which three paragraphs earlier calls a 113 m
   excess negligible at half a per cent, is the double standard the advocate block already
   anticipates for the 113 m. The variations belong in the entry as evidence that the
   figure is a deformation under load; the answer to item 105 is the Clairaut tie-in.

9. VERDICT. REFUTED was tested against MISLEADING, which is what R02 and R05 carry for
   the Machian and frame-dragging arguments. Kept REFUTED, because two of the four items
   assert an empirical negative that measurement contradicts, and because the two that
   do not — 55 and 105 — are answered by the same fact rather than by a philosophical
   dispute: the alternative cause is the same relative rotation rate, so it changes no
   number. If the cluster were ever split, item 55's Machian half would belong beside
   R02/R05 at MISLEADING and items 180/257 would stay REFUTED. Recorded here as an
   observation; no verdict_challenge filed.

10. QUOTE PROVENANCE. Rowbotham is public domain and quoted at length from the Gutenberg
    transcription of the 1865 edition (#69892). The 1881 chapter was located through
    sacred-texts za39.htm, but every 1881 phrase inside quotation marks in this entry —
    the electric/magnetic third cause, the Sabine and Baily sentences, "577 to 875" — was
    transcribed from the third-edition PDF at archive.org item
    zeteticastronomy-earthnotaglobe, printed pp. 182-186, and not from the sacred-texts
    rendering. (Page markers in that PDF: the Newton/Huygens proportions at p. 182, the
    electric-and-magnetic third cause at p. 184, Sabine and Baily at pp. 185-186.)
    Sungenis & Bennett is in copyright and
    every excerpt here is short; the page numbers are the printed numbers read off the
    page images of the named scan (item GallileoWasWrong), leaf by leaf, on 2026-08-11 —
    the footer sits at the FOOT of its own leaf in this scan, so the number under a block
    of text is that text's page. The eight citations sit on leaves 61 (p. 49), 216
    (p. 204), 251 (p. 239), 472 (p. 460), 711 (p. 699), 722 (p. 710), 723 (p. 711) and
    1040 (p. 1028). Seven of the eight were previously recorded one page low, from a
    reading that took the marker above a block of text as belonging to it. They are still
    not checked against a print copy, but the scan's own footers are now the evidence.
    NOTE THE VOLUME
    TRAP: Bennett's technical chapter is chapter 12 at pp. 710f in the Vol. I CD-ROM
    scan and chapter 10 at pp. 157f in the Bennett4276 scan the project has settled is
    Vol. II. Do not merge the two page ranges. Cite Vol. I here — it is the scan
    `works.py` describes for WRK-SUNGENIS-2006.

11. DEFECTS IN OUR OWN RECORD, reported up, NOT edited here (this agent owns one file):
    (a) A13 `real_source=None`, though two sources are now located and quoted;
    (b) `originator="Samuel Rowbotham"` covers the pendulum/oblateness half only — the
        "has another cause" wording in the cluster NAME is Bennett's Machian argument,
        and the name and the originator field therefore point at different books;
    (c) A15 ("Torsion balances, gravimeters and pendulum clocks show no variation",
        NOT DEMONSTRATED, items 232/249/250/398) is the same assertion as item 257 with
        the instruments named. A13 and A15 are answered by one measurement and carry
        different verdicts. Cluster-boundary judgement, flagged not acted on.
"""

ENTRY = {

"A13": dict(

    tldr=("Nobody feels the centrifugal effect, because it is 0.034 m/s² — about 0.35 per cent "
          "of gravity. It is measured constantly: 100.00 kg weighed at the pole "
          "reads 99.47 kg at the equator, and the seconds-pendulum table Rowbotham printed in "
          "1865 to explain it away sits within a tenth of one per cent of what a rotating Earth "
          "predicts, at both ends. The thermal expansion he offers as the cause — his own good "
          "coefficient times his own 84.2 °F equator-to-pole range — comes out about eight times "
          "too small to produce it. And the "
          "geocentric alternative cause — a universe turning instead of the Earth — needs the "
          "same relative rotation rate, so it predicts the same bulge and the same equatorial "
          "relief that two of these four items say are not there."),

    passage=dict(
        work="WRK-ROWBOTHAM-1865",
        pd=True,
        locator=("Section I, in the discussion of the oblate spheroid and the pendulum, from the "
                 "Project Gutenberg transcription of the 1865 first book edition (ebook #69892, "
                 "“Original publication: United Kingdom: Simpkin, Marshall, and co., 1865”). The "
                 "same argument, with a third alternative cause added, is at ch. XIV "
                 "“Variability of Pendulum Vibrations” of the 1881 third edition"),
        quote=("Returning to the pendulum, it will be found to be equally unsatisfactory as a "
               "proof of this peculiar rotundity of the Earth. It is argued that as the length "
               "of a seconds pendulum at the equator is 39,027 inches, and 39,197 inches at the "
               "north pole, that the Earth must be a globe, having a less diameter through its "
               "axis than through its equator. But this proceeds upon the assumption that the "
               "Earth is a globe having a “centre of attraction of gravitation,” towards which "
               "all bodies gravitate or fall … It should also be first proved that no other "
               "cause could operate besides greater proximity to the centre of gravity, to "
               "produce the variable oscillations of a pendulum. This not being attempted, the "
               "whole subject must be condemned as logically insufficient, irregular, and "
               "worthless for its intended purpose. Many philosophers have ascribed the "
               "alterations in the oscillations of a pendulum to the diminished temperature of "
               "the northern centre.\n\n"
               "… Thus there are two distinct and tangible causes which necessarily operate to "
               "produce the variable oscillations of a pendulum, without supposing any "
               "distortion in the supposed rotundity of the Earth."),
        gloss="""<p><strong>He prints the measurement.</strong> The two figures in that sentence &mdash; 39.027 inches at the equator, 39.197 at the north pole; the comma is 1865 typesetting for a decimal point &mdash; <em>are</em> the equatorial relief. The length a pendulum must have to beat seconds is <em>L</em>&nbsp;=&nbsp;<em>g</em>/&pi;&sup2;, so a table of pendulum lengths by latitude is a table of gravity by latitude. Rowbotham does not dispute the numbers. He disputes what they show. Two of the four items in this cluster &mdash; <em>&ldquo;No felt centrifugal force&rdquo;</em> and <em>&ldquo;No equatorial centrifugal relief&rdquo;</em> &mdash; deny the thing his own page tabulates.</p>
<p><strong>What his argument actually is, and it is not a silly one.</strong> Three moves. (i) The inference from a shorter pendulum to a shorter polar radius presupposes a centre of attraction and therefore a globe. (ii) Nobody has shown that <em>no other</em> cause could produce the variation. (iii) Two other causes are available: the pendulum rod contracts in the colder north, and the colder northern air is denser and resists the bob differently. The 1881 third edition adds a third &mdash; &ldquo;electric and magnetic states of the atmosphere.&rdquo; He italicises <em>assumption</em>, <em>is</em> and <em>no other</em>; the emphasis is his.</p>
<p><strong>The alternative causes are testable, and he supplies the numbers to test them with.</strong> On the same pages he quotes a temperature table from Sir Richard Phillips&rsquo;s <em>Million of Facts</em>, p. 475 (mean annual temperature 84.2&nbsp;&deg;F at the equator, 0&nbsp;&deg;F at the pole) and a thermal-expansion figure from Noad&rsquo;s <em>Lectures on Chemistry</em>, p. 41 (&ldquo;a change of temperature equal to 30&deg; Fah. will alter its length 1/5000th part&hellip;&rdquo;). Those two quotations decide the question against him, and the refutation below does the multiplication.</p>
<p><strong>The other half of this cluster comes from a different book and a different century.</strong> Items 55 and 105 concede a bulge and dispute its <em>cause</em>; Rowbotham denies the bulge is established at all, and argues from the disagreement among meridian-arc measurements that the Earth might as well be an <em>oblong</em> spheroid. The &ldquo;another cause&rdquo; formulation is the Machian one, and the earliest text located that carries it in the form the list uses is Sungenis and Bennett, <em>Galileo Was Wrong</em>. In the Vol.&nbsp;I scan (archive.org item GallileoWasWrong), Bennett&rsquo;s ch.&nbsp;12 opens at printed p.&nbsp;710 by setting out the geokinetic case he means to answer &mdash; <em>&ldquo;there are three geokinetic claims for terrestrial motion&rdquo;</em>, of which the second is that centrifugal forces cause the polar flattening and equatorial bulge and <em>&ldquo;This also explains why the acceleration of gravity is less at the equator&rdquo;</em> &mdash; and he answers it at p.&nbsp;711 not by denying any of that but by writing that the effects <em>&ldquo;depend on the assumption that the inertial effects can only be caused by the Earth&rsquo;s rotation.&rdquo;</em> At ch.&nbsp;4, p.&nbsp;204 the same volume says the oblateness proves &ldquo;that there is a force causing their effect, not that a rotation of the Earth is the force.&rdquo; <strong>Both books grant the phenomena.</strong> No assertion of items 180 or 257 was located in the passages of Vol.&nbsp;I read for this entry &mdash; pp.&nbsp;49, 204, 239, 460, 699, 710&ndash;711 and Appendix&nbsp;7 &mdash; and the two sentences that come nearest are both answered below: the satellite-photograph parenthesis at p.&nbsp;699, and the remark at p.&nbsp;711 that in the rotating-shell model <em>&ldquo;an object at the center of the hollow sphere will not be affected by the inertial forces &hellip; but not the Earth itself, if it is centrally located&rdquo;</em>, which pulls against the concession a few lines above it.</p>
<p><strong>The first of those two lines, in full, because it runs the other way and it is fair to note it.</strong> At printed p.&nbsp;699, in ch.&nbsp;11 on Hildegardian geocentrism, a parenthesis has it that the precession is attributed to the equatorial bulge <em>&ldquo;(even though satellite photographs of the Earth do not show an equatorial bulge)&rdquo;</em>. As a remark about photographs that is true and uninteresting: the flattening is 1/298, so on an image 1,000 pixels across the polar diameter is about three pixels shorter than the equatorial one. As an argument it does not survive the same volume&rsquo;s GPS appendix &mdash; Appendix&nbsp;7 in this scan, at printed p.&nbsp;1028 &mdash; which prints the WGS84 flattening as 1/298.257223563 without demur.</p>
<p><strong>What this passage is being cited as.</strong> The earliest text located that carries the pendulum-and-oblateness argument in the form the list compresses, and it confirms the record&rsquo;s edition: the material is in the 1865 first book edition, not only in the enlarged 1881 third. It is an ancestor of two of the four items and it is not evidence of origination for the other two.</p>"""),

    steelman=dict(
        description="""<p><strong>SURFACE (weak &mdash; do not use).</strong> &ldquo;You <em>can</em> feel it, and the bulge proves rotation.&rdquo; Both halves lose. You cannot feel a third of one per cent of your weight, and saying so hands over the only part of the item that is straightforwardly true. And the bulge on its own proves that <em>something</em> is flattening the Earth, which is what the geocentric source says too, in nearly those words.</p>
<p><strong>DEEPER.</strong> Rowbotham is right that the pendulum alone underdetermines the figure of the Earth. A latitude variation in <em>g</em> is a fact about the gravity field, not about the shape; deriving the shape needs an assumption about how mass is distributed inside, and that is exactly what Newton and Huygens disagreed about &mdash; 1/230 against 1/578, from the same data. He is also right that the 18th- and 19th-century meridian arcs disagreed badly, and right that the British arcs he tabulates come out as if the Earth were <em>oblong</em>. Those are real published results, quoted accurately.</p>
<p><strong>KERNEL.</strong> The strongest form is not Rowbotham&rsquo;s at all; it is the one <em>Galileo Was Wrong</em> takes, and it is Mach&rsquo;s. <em>The equatorial bulge and the latitude variation of gravity do not by themselves distinguish a rotating Earth in a fixed sky from a fixed Earth in a rotating sky.</em> That is not a flat-earth evasion invented for the purpose: Mach wrote it, Einstein endorsed it in 1911 and again in the 1920 Leyden address, and it is a theorem &mdash; Thirring showed in 1918 that a rotating mass shell induces Coriolis and centrifugal terms in its interior, and Pfister and Braun (<em>Class. Quantum Grav.</em> 2:909, 1985) showed that with the shell&rsquo;s stresses handled correctly the induced centrifugal force comes out exactly right. Sungenis and Bennett quote Mach&rsquo;s sentence in full at their ch.&nbsp;7, p.&nbsp;460, qualifying clause included, and their conclusion is precisely calibrated: the phenomena prove &ldquo;that there is a force causing their effect, not that a rotation of the Earth is the force.&rdquo; On the narrow question of what the bulge proves about <em>whose</em> rotation, that sentence is correct.</p>""",
        why_it_doesnt_save_claim="""<p>Because it concedes everything the four items deny, and buys nothing back.</p>
<p><strong>Take the kernel at full strength and follow it.</strong> If the sky turns instead of the Earth, the relative rotation rate is the same &mdash; one turn per sidereal day, &omega;&nbsp;=&nbsp;7.292115&nbsp;&times;&nbsp;10<sup>&minus;5</sup>&nbsp;rad/s &mdash; because it is the <em>relative</em> rate that both descriptions have to reproduce. Every number then comes out identical: the same 0.0339&nbsp;m/s&sup2; of centrifugal acceleration at the equator, the same 21.4&nbsp;km bulge, the same 0.53% weight difference between pole and equator. Mach&rsquo;s point is that the two descriptions are the same physics; it is not that one of them has no bulge. So the Machian argument <strong>predicts the equatorial relief</strong> that items 180 and 257 report as absent. It is not an alternative to the measurement. It is an alternative label on the measurement.</p>
<p><strong>And Rowbotham&rsquo;s half is not underdetermination but arithmetic.</strong> He does not stop at &ldquo;the pendulum alone cannot settle the figure&rdquo;, which would have been defensible. He asserts two specific causes, and the numbers on his own page sink both: the expansion coefficient he quotes makes the first about eight times too small, and the air-pump experiment he cites for the second makes it, read at its most generous, some twenty times too small. A hypothesis that names its own mechanism has given up the protection that underdetermination affords.</p>"""),

    refutation="""<p><strong>Start with the two concessions, because both are permanent.</strong> First: you cannot feel it. The centrifugal term at the equator is 0.0339&nbsp;m/s&sup2;, which is 0.35% of gravity, and no human perceives that. Anyone who answers this item by claiming the effect is perceptible has lost the exchange and deserved to. Second: the bulge and the latitude variation of gravity do not, by themselves, tell you whether the Earth turns or the sky does. That is Mach&rsquo;s observation, Einstein agreed with it, and the geocentric source states it accurately. This page is not going to pretend either point away.</p>

<p><strong>What the verdict ranges over.</strong> Not &ldquo;the bulge has been proved to come from the Earth&rsquo;s own rotation rather than the universe&rsquo;s.&rdquo; The cluster&rsquo;s four items make two claims, and they are answered separately: that no centrifugal effect is detectable (items 180, 257), which measurement contradicts; and that the bulge has some other cause (items 55, 105), which turns out to change no measured quantity at all.</p>

<h4>1. The effect is not felt. It is weighed, and it has been since 1672</h4>

<p>Jean Richer took a pendulum clock from Paris to Cayenne, at 4.9&deg;N, in 1672 and found it losing time &mdash; Newton records the rate as 2<sup>m</sup>&nbsp;28<sup>s</sup> a day &mdash; and had to shorten the bob by 1&frac14; lignes to make it beat seconds again. Huygens read that as the centrifugal effect of rotation reducing apparent gravity near the equator; Newton read it as the equator being further from the centre. Both were partly right, and the argument between them is what made the figure of the Earth a research programme.</p>

<p>Modern numbers, from the GRS80 reference ellipsoid, recomputed here 2026-08-10 so a reader can redo them:</p>

<ul>
<li>Normal gravity at the equator 9.7803268&nbsp;m/s&sup2;, at the pole 9.8321864&nbsp;m/s&sup2;. Difference <strong>0.0518596&nbsp;m/s&sup2;, or 0.5302%</strong>.</li>
<li>Centrifugal acceleration at the equator &omega;&sup2;<em>a</em> = (7.292115&nbsp;&times;&nbsp;10<sup>&minus;5</sup>)&sup2;&nbsp;&times;&nbsp;6&thinsp;378&thinsp;137&nbsp;m = <strong>0.0339157&nbsp;m/s&sup2;</strong> &mdash; 65.4% of that difference. The remaining 34.6% is the shape term: the equator sits 21.4&nbsp;km further from the centre.</li>
<li>In practical units: <strong>100.00&nbsp;kg weighed at the pole reads 99.47&nbsp;kg at the equator.</strong> That is half a kilogram, and an ordinary digital scale would show it.</li>
</ul>

<p>It is not measured with bathroom scales. The International Gravity Formula &mdash; <em>g</em>(&phi;) = 9.780327&thinsp;(1 + 0.0053024&thinsp;sin&sup2;&phi; &minus; 0.0000058&thinsp;sin&sup2;2&phi;) &mdash; is the first correction applied to every gravity survey ever run for minerals, oil or geodesy, and the 0.0053024 in it is the number above. A field gravimeter resolves about 0.01&nbsp;mGal; the centrifugal term is 3,392&nbsp;mGal, some 340,000 times larger. Absolute gravimeters of the FG5 class do not use a pendulum at all &mdash; they drop a corner cube in vacuum and time it interferometrically against a rubidium clock, with an accuracy the manufacturer states as <em>&ldquo;2&nbsp;&micro;Gal (observed agreement between FG5-X instruments)&rdquo;</em>. That instrument has no rod to expand and no air to resist it, and it returns the same latitude dependence. So do superconducting gravimeters, which are finer still.</p>

<p>The rotation is not merely detected, it is used. The Earth&rsquo;s surface moves east at &omega;<em>a</em> = <strong>465&nbsp;m/s</strong> at the equator, and that velocity is a free contribution to any eastward launch: 463&nbsp;m/s at Kourou (5.2&deg;N), 409 at Cape Canaveral (28.5&deg;N), 325 at Baikonur (45.6&deg;N). The differences are large enough to drive the siting of launch complexes. And the E&ouml;tv&ouml;s correction &mdash; a ship or aircraft moving east weighs less, by 2&omega;<em>v</em>cos&thinsp;&phi; &mdash; is applied as routine in marine and airborne gravimetry: at 10&nbsp;m/s eastward on the equator it is 146&nbsp;mGal, more than a hundred times the survey noise floor. Set &omega; to zero and every one of those corrections becomes a systematic error that nobody has ever had to make.</p>

<h4>2. Rowbotham&rsquo;s alternative causes, tested with Rowbotham&rsquo;s own coefficients</h4>

<p>This is where the source&rsquo;s version of the argument, which is the one that has to be answered, comes apart &mdash; and it comes apart on its own page. He offers temperature and air density as the causes of the pendulum&rsquo;s variation. He then quotes the two numbers needed to check the first one.</p>

<p>From Phillips&rsquo;s <em>Million of Facts</em> he takes mean annual temperature falling from 84.2&nbsp;&deg;F at the equator to 0&nbsp;&deg;F at the pole. From Noad&rsquo;s <em>Lectures on Chemistry</em> he takes the expansion of a pendulum: 1/5000 of its length for 30&nbsp;&deg;F, that is 1/150,000 per degree. Multiply: 84.2&nbsp;&divide;&nbsp;150,000 = 5.6&nbsp;&times;&nbsp;10<sup>&minus;4</sup>, or <strong>0.056%</strong>. The variation he has to explain, from his own two pendulum figures, is (39.197&nbsp;&minus;&nbsp;39.027)&nbsp;&divide;&nbsp;39.027 = <strong>0.436%</strong>. Thermal expansion is short by a factor of <strong>7.8</strong>. Against the modern value for the same quantity, 0.530%, it is short by 9.4.</p>

<p>The coefficient is not the problem. 1/150,000 per &deg;F is 6.7&nbsp;&times;&nbsp;10<sup>&minus;6</sup>/&deg;F, against a modern figure for steel of 11.7&nbsp;&times;&nbsp;10<sup>&minus;6</sup>/&deg;C = 6.5&nbsp;&times;&nbsp;10<sup>&minus;6</sup>/&deg;F. He quoted a good number and did not multiply it out.</p>

<p><strong>His second cause fails the same way, and it should be tested with the experiment he names, not with a substitute.</strong> The mechanism he states is resistance, not buoyancy: <em>&ldquo;if the pendulum vibrates in the air, which is colder and therefore denser in the north than at the equator, it must be more or less resisted in its passage through it&rdquo;</em>, and his authority is Derham, who compared arcs of vibration in an air-pump receiver at different densities and found the rate differing by <em>&ldquo;two seconds in an hour when the vibrations were longest&rdquo;</em>. Take Derham&rsquo;s number at face value and in Rowbotham&rsquo;s favour. Two seconds in 3,600 is a fractional change in period of 5.6&nbsp;&times;&nbsp;10<sup>&minus;4</sup>, and since <em>T</em>&nbsp;&prop;&nbsp;&radic;<em>L</em> that is 1.1&nbsp;&times;&nbsp;10<sup>&minus;3</sup> on the length of a seconds pendulum &mdash; but that is the whole atmosphere against a vacuum. What Rowbotham needs is the equator-to-pole <em>difference</em>, and on his own temperature table (84.2&nbsp;&deg;F against 0&nbsp;&deg;F) air at constant pressure is denser at the pole by about 18%. Eighteen per cent of 0.11% is <strong>0.02%</strong>, against the <strong>0.436%</strong> he has to explain: short by a factor of about twenty, on the most favourable reading available to him. Computed instead from the physics &mdash; buoyancy plus added mass shift the apparent <em>g</em> by roughly 1.5&thinsp;&rho;<sub>air</sub>/&rho;<sub>bob</sub>, some 2&nbsp;&times;&nbsp;10<sup>&minus;4</sup> for a brass bob in full air, of which the latitude variation is again about a fifth &mdash; it is short by of order a hundred. And Derham&rsquo;s experiment measures the wrong thing for the purpose: damping changes the <em>amplitude</em>, and amplitude reaches the period only through the circular-error term, which is smaller still. And the instrument that settles it has no air in it at all: the FG5 above returns the same latitude dependence with its mass falling in vacuum.</p>

<p><strong>The 1881 edition enlarges the argument and quotes the answer to it.</strong> By the third edition (printed pp.&nbsp;185&ndash;186) Rowbotham has added a survey of General Sabine&rsquo;s pendulum campaign &mdash; 131 observations, from 79&deg;&nbsp;49&prime; north to South Shetland at 62&deg;&nbsp;56&prime; south &mdash; and concludes from the 23 of them that departed markedly from the computed values that &ldquo;the assumption of Sir Isaac Newton that the earth is an oblate spheroid, is not confirmed by experiments made with the pendulum.&rdquo; He then quotes Sabine&rsquo;s own account of why those 23 departed: the discrepancies are &ldquo;due in a far greater degree to local peculiarities than to what may be more strictly called errors of observation&rdquo;, and Francis Baily&rsquo;s judgement that a pendulum&rsquo;s vibrations &ldquo;are powerfully affected, in many places, by the local attraction of the substratum on which it is swung&rdquo;. That is the correct explanation, printed in his own text: the residual scatter about the latitude law is local geology, which is what a gravimeter is <em>for</em>. It is the same move the project records at <a href="#ARG-B06">ARG-B06</a>, where he reprints the <em>Encyclopædia Britannica</em>&rsquo;s article on levelling &mdash; the correction for the difference between the true and the apparent level, which is the curvature term &mdash; and then denies the curvature it corrects for.</p>

<p><strong>And here is the part that decides it.</strong> Take <em>L</em>&nbsp;=&nbsp;<em>g</em>/&pi;&sup2; and the GRS80 gravity values, and the seconds pendulum should be 39.014&nbsp;inches at the equator and 39.221 at the pole. Rowbotham printed 39.027 and 39.197. His table agrees with what a rotating oblate Earth predicts to within 0.034% at one end and 0.061% at the other &mdash; while the effect he was explaining away is 0.436%. He had the right answer on the page in front of him and offered a mechanism eight times too small to displace it.</p>

<h4>3. The meridian arcs: his facts are largely right, and they point the other way</h4>

<p>The disagreements he tabulates are real. The Ordnance Survey series he quotes from Hugh Murray&rsquo;s <em>Encyclopaedia of Geography</em> does show degrees getting <em>shorter</em> going north over southern England, which is the signature of an oblong figure. And the Lapland degree he quotes, 57,422 toises, is the published Maupertuis figure, which did not survive later scrutiny intact: he prints the Swedish re-measurement&rsquo;s verdict himself, that the French had given the degree there &ldquo;196 toises more than the true length&rdquo;.</p>

<p>His Peru degree does not check out. He gives &ldquo;the first degree of the meridian from the equator as 56,653 toises&rdquo;. The published Peruvian arc &mdash; 176,945 toises over 3&deg;&nbsp;7&prime;&nbsp;3&Prime;, in the 1911 <em>Britannica</em> article cited below &mdash; works out at about 56,760 toises to the degree, and reducing that to the equator moves it by only some ten toises. His figure is roughly a hundred toises, about 200&nbsp;m, low. That is a second corrupt number of the same kind as the Huygens ratio below, and it pulls the same way: it widens the disagreement his argument runs on.</p>

<p>What produces those discrepancies is now the most useful thing about them. A meridian arc is measured by combining a triangulated ground distance with astronomically observed latitudes, and astronomical latitude is referred to the local plumb line &mdash; which is pulled sideways by nearby mass. Short arcs are therefore dominated by local gravity anomalies rather than by the Earth&rsquo;s overall figure, which is exactly why the small English arcs scatter into apparent oblongness. The most famous instance is the one that founded a field: in the Great Trigonometrical Survey of India the latitude difference between Kaliana and Kalianpur came out 5.24&Prime; smaller geodetically than astronomically, and when Pratt computed what the Himalaya ought to do to the plumb line he got 15.885&Prime;, more than three times the observed value. Pratt (1855) published the discrepancy and said he could not explain it; Airy (1855) proposed that mountains float on lighter roots, and isostasy was born. The anomaly Rowbotham reads as evidence that the figure of the Earth cannot be measured is the anomaly that told geophysicists what mountains are made of.</p>

<p>Two further points of detail, since he rests weight on both. Maupertuis&rsquo;s Lapland result implied a flattening near 1/179 &mdash; far more oblate than the truth &mdash; so the later Swedish re-measurement in Bothnia, which shortened his arc, moved the computed flattening <em>toward</em> the modern 1/298.257 and not toward zero. (Svanberg&rsquo;s own published flattening was not located in the sources reached here; the direction follows from the geometry and is stated as our inference.) And the Huygens figure he cites &mdash; &ldquo;577 to 875, or a difference of about one-third of the whole diameter&rdquo;, in both the 1865 and the 1881 editions &mdash; is a corrupt number: Huygens&rsquo;s ratio was 577:578, a flattening near 1/578, and 578 has plainly been scrambled into 875, with the &ldquo;one-third&rdquo; then computed off the corruption. That matters because the disagreement is his whole argument: 577&nbsp;:&nbsp;875 implies a flattening of (875&nbsp;&minus;&nbsp;577)/875 = <strong>0.34</strong> &mdash; which is where his &ldquo;about one-third&rdquo; comes from &mdash; against Huygens&rsquo;s actual 1/578 = <strong>0.0017</strong>, so the figure he prints is about <strong>197 times</strong> the one Huygens computed. There is no reason to think he did it deliberately; he took a number from a secondary source and did not check it against the arithmetic he printed beside it.</p>

<p>The underlying point is the one his framing misses. Newton got 1/230 and Huygens 1/578 from the same observations because they assumed different things about the density inside the Earth. The spread was not a failure of the method; it was the method telling them that the flattening measures the interior. Which is what Clairaut then proved.</p>

<h4>4. One number has to do two jobs, and it does</h4>

<p>Clairaut&rsquo;s theorem relates the shape of a rotating equilibrium figure to the gravity on it: (<em>g</em><sub>p</sub>&nbsp;&minus;&nbsp;<em>g</em><sub>e</sub>)/<em>g</em><sub>e</sub> = (5/2)<em>m</em>&nbsp;&minus;&nbsp;<em>f</em>, where <em>f</em> is the flattening and <em>m</em> = &omega;&sup2;<em>a</em>/<em>g</em><sub>e</sub> is the ratio of centrifugal to gravitational acceleration at the equator. Put the measured numbers in. <em>m</em> = 0.0339157/9.7803268 = 0.00346775. With <em>f</em> = 1/298.257222101, (5/2)<em>m</em>&nbsp;&minus;&nbsp;<em>f</em> = <strong>0.0053166</strong>. The observed gravity ratio is <strong>0.0053024</strong>. They agree to 0.27%, which is the size of the second-order terms Clairaut&rsquo;s first-order theorem drops.</p>

<p>That is the check the &ldquo;other cause&rdquo; has to pass. The flattening and the pole-to-equator gravity difference are measured by completely different means &mdash; satellite geodesy and orbit perturbations for one, gravimeters for the other &mdash; and a single parameter, the rotation rate, ties them together to three decimal places. That rotation rate is itself measured independently, by the length of the sidereal day, by ring-laser gyroscopes, and by very-long-baseline interferometry against quasars. Any proposed alternative cause of the bulge inherits an obligation to reproduce both numbers and their relationship, using something other than &omega;. Nothing on offer does.</p>

<h4>5. The rotating universe reproduces all of it, which is the problem</h4>

<p>The geocentric alternative is not a different value of anything. Mach&rsquo;s claim, endorsed by Einstein and made rigorous for a rotating mass shell by Thirring (1918, corrected 1921) and definitively by Pfister and Braun (1985), is that a universe rotating about a fixed Earth induces the same Coriolis and centrifugal fields. Take it seriously and the consequence is immediate: the relative rotation rate must still be one turn per sidereal day, so the induced centrifugal field is still &omega;&sup2; times distance from the axis, so the equilibrium figure is still flattened by 1/298 and gravity is still 0.53% weaker at the equator. <strong>The re-description predicts the equatorial relief that two of these four items deny.</strong> It is the same spacetime in different coordinates, and no observable moves.</p>

<p>What it does cost is a global inertial frame: with the whole sky turning once a sidereal day, the coordinate tangential speed reaches <em>c</em> at <em>c</em>/&omega; = 4.11&nbsp;&times;&nbsp;10<sup>12</sup>&nbsp;m, about 27.5&nbsp;AU &mdash; outside Uranus, inside Neptune. General relativity permits that as a coordinate effect and nothing local exceeds <em>c</em>, which is why this page treats the frame question at <a href="#ARG-R01">ARG-R01</a> and the Machian machinery at <a href="#ARG-R02">ARG-R02</a> and <a href="#ARG-R05">ARG-R05</a> rather than here. For <em>this</em> cluster the relevant fact is narrower and harder: whichever description you adopt, the bulge and the weight difference are exactly where the measurements find them.</p>

<p>There is a further wrinkle inside the source&rsquo;s own statement of the model. At p.&nbsp;711, a few lines below the Response quoted above, Bennett reports from Barbour and Bertotti&rsquo;s rotating-shell result that an object at the centre of the hollow sphere is not affected by the inertial forces, and infers that the space around the Earth shows the effects but not the Earth itself. That is true of a <em>point</em> at the centre, where the net centrifugal force vanishes. It is not true of a body 6,371&nbsp;km in radius: the centrifugal potential grows as the square of the distance from the axis, and it is that variation across the body &mdash; not the force at its centre &mdash; that raises an equatorial bulge. On the version of the model as stated, the effect the argument is trying to re-explain would not appear at all.</p>

<h4>6. The bulge is not rigid, and the part that is unexplained does not help</h4>

<p>Item 105 asserts a stable equatorial bulge; no wording for it was located in either source, so what follows answers the claim as the list states it. The bulge is not rigid, and the ways in which it moves are among the better-measured things in geophysics &mdash; but the honest thing to say first is how big those movements are. The solid Earth flexes about 30&nbsp;cm twice a day under lunar and solar tides: one part in 70,000 of the 21.4&nbsp;km bulge itself. The dynamical oblateness <em>J</em><sub>2</sub> was decreasing secularly through the 1980s and 1990s as the crust rebounds from the last ice age, and then reversed &mdash; Cox and Chao reported the turn around 1998 in <em>Science</em> 297:831 (2002), Dickey and colleagues argued later the same year (<em>Science</em> 298:1975) that ocean and ice mass redistribution accounts for it, and the decadal behaviour is still an active question &mdash; and that secular trend is a fractional change of order 10<sup>&minus;8</sup> a year, which is sub-millimetre a year if it is carried onto the polar&ndash;equatorial radius difference.</p>

<p>Those are small numbers, and saying so is the point rather than a concession. They are the size a <em>responsive</em> rotational figure should show: a body that visibly deforms under the tides, and whose oblateness tracks the redistribution of ice and water on it, is a body whose 21.4&nbsp;km flattening is a deformation under load rather than a fixed shape. What none of them is, is an opening for a non-rotational cause. And the weight of item 105 is on <em>bulge</em>, not on <em>stable</em>: what the argument has to displace is a flattening tied to the rotation rate by Clairaut&rsquo;s theorem to three parts in a thousand, and centimetres of tide do not displace it. This page is not going to answer a four-word item by pointing at the fourth decimal place.</p>

<p>And the bulge is not in hydrostatic equilibrium. Chambat, Ricard and Valette (<em>Geophysical Journal International</em> 183:727, 2010), correcting Nakiboglu&rsquo;s standard calculation, put it plainly: <em>&ldquo;The difference between the polar and equatorial radii appears to be 113 &plusmn; 1 m (instead of 98 m) larger than the hydrostatic value.&rdquo;</em> That is a real excess &mdash; 0.53% of the 21.4&nbsp;km bulge &mdash; and it is <em>not</em> fully accounted for. It is attributed to density structure in the mantle and to delayed viscous relaxation from Pleistocene deglaciation, and that attribution is a modelling result rather than a closed case. This page will keep saying so.</p>

<p>It is also no use to the argument. The excess is half a per cent; the rotational term supplies the other 99.5%, and the excess is defined <em>relative to</em> the hydrostatic figure a rotating Earth predicts. A residual measured against a model is not evidence against the model that generated the residual.</p>

<h4>7. What is left, stated without decoration</h4>

<p>The centrifugal effect at the equator is 0.35% of gravity: imperceptible, and measured continuously by instruments a hundred thousand times more sensitive than it needs. The flattening and the gravity difference are tied together by the rotation rate through Clairaut&rsquo;s theorem to better than three parts in a thousand. Rowbotham&rsquo;s alternative causes are about eight and about twenty times too small, on the coefficient and the experiment he printed himself. The geocentric alternative cause is not an alternative to any measurement; it is the same physics in rotating coordinates, and it predicts the equatorial relief this cluster reports as missing. Two of these four items deny a phenomenon that both of the books behind this cluster affirm.</p>""",

    advocate=dict(
        best_defense=(
            "Four moves. First and biggest: read your own compression block. You have "
            "established that in everything you read, neither Rowbotham nor Sungenis and "
            "Bennett asserts what items "
            "180 and 257 assert. So you have spent a page refuting a list-maker's four-word "
            "fragment, which is the exact offence this website exists to complain about. "
            "Second, on Rowbotham you are anachronistic. In 1865 the arcs really did "
            "disagree, isostasy did not exist as a concept anybody had assimilated, and "
            "'someone should show that no other cause operates' was ordinary "
            "nineteenth-century caution, not a fallacy. You beat him with an FG5 "
            "gravimeter he could not have imagined and call it a refutation. Third, and "
            "this is the substantive one: you concede that the bulge does not tell you "
            "whose rotation it is, you concede Mach, you concede Pfister and Braun, and "
            "then you say the re-description 'changes no number' as though that were a "
            "defeat. It is our entire thesis. We never claimed the bulge would vanish; we "
            "claimed it fails as a proof of terrestrial rotation, and you have just agreed "
            "with us in print. Fourth, you have conceded 113 metres of equatorial radius "
            "that hydrostatic theory cannot produce and that nobody has explained, and "
            "your answer is that it is only half a per cent. It is half a per cent that "
            "your own model does not predict, and you spent six paragraphs arguing that "
            "agreement to 0.27 per cent is decisive evidence. Pick a standard."),
        survives=4,
        preemptive=(
            "Four, driven by the first and third moves. On the FIRST: do not defend "
            "against it, publish it. The gap between the source and the items is the "
            "finding, it is already the spine of the compression block, and the "
            "refutation must be visibly aimed at the sources — the sentence 'both books "
            "grant the phenomena' and the sentence that the Machian re-description "
            "PREDICTS the relief the items deny both have to stay where a skimming "
            "reader meets them. If an editor ever trims section 5 as 'conceding too "
            "much', the entry becomes exactly the straw-man exercise the defender "
            "describes. On the SECOND, the anachronism charge is fair against a modern "
            "instrument and must be answered with a period-appropriate weapon, which is "
            "why the centrepiece is his own quoted expansion coefficient multiplied by "
            "his own quoted temperature range. That paragraph is the load-bearing one; "
            "the FG5 is corroboration and must never be promoted above it. On the THIRD, "
            "agree in public and then be precise about what the cluster claims: the "
            "modest claim (the bulge does not discriminate whose rotation it is) is true "
            "and non-discriminating, exactly as at ARG-A03 and ARG-R01; the specific "
            "claims on the list (no felt centrifugal force, no equatorial relief) are "
            "false, and the list needs the specific ones. On the FOURTH, do not soften "
            "the non-hydrostatic excess and do not let anyone write that it is "
            "'explained' — 'attributed to mantle structure and delayed glacial rebound, "
            "and that attribution is a modelling result' is the correct strength. The "
            "answer to the double-standard charge is already in the text and must stay "
            "adjacent to the concession: the 113 m is a residual measured AGAINST the "
            "rotational figure, so it presupposes the model it is being offered against, "
            "whereas Clairaut's 0.27% is an agreement between two independently measured "
            "quantities. Those are different kinds of number and the paragraph must keep "
            "saying which is which."),
    ),

    straw_man=dict(
        identified=True,
        detail=("Rowbotham characterises the inference from pendulum data to a flattened figure "
                "as proceeding “upon the assumption that the Earth is a globe having a "
                "‘centre of attraction of gravitation’” — that is, as assuming "
                "its conclusion. That misdescribes what the geodesists were doing. The figure of "
                "the Earth was a two-parameter fit, and the two parameters were constrained by "
                "two independent classes of measurement: meridian arcs gave the shape, pendulums "
                "gave the gravity, and Clairaut's theorem of 1743 supplied a relation between "
                "them that either confirms or breaks. A fit with a consistency check between two "
                "independent data sets is not a presupposition, and the disagreement between "
                "Newton's 1/230 and Huygens's 1/578 shows the conclusion was not being assumed: "
                "the two men fed the same observations through different assumptions about the "
                "interior and got answers differing by a factor of two and a half. His companion "
                "demand — that it “should also be first proved that no other cause could "
                "operate” — asks for a universal negative that no empirical inference has "
                "ever supplied, and he did not apply it to his own two proposed causes. Both are "
                "errors of reasoning about method rather than bad faith, and in 1865 the "
                "isostatic explanation of the discrepant arcs was ten years old and not yet "
                "general knowledge.")),

    compression=dict(
        assessed=True, drifted=True,
        list_phrasing="No equatorial centrifugal relief.",
        source_wording=("Rowbotham: &ldquo;It is argued that as the length of a seconds pendulum at the "
                        "equator is 39,027 inches, and 39,197 inches at the north pole, that the Earth "
                        "must be a globe &hellip; It should also be first proved that <em>no other</em> "
                        "cause could operate.&rdquo; &mdash; Sungenis &amp; Bennett, Vol.&nbsp;I ch.&nbsp;12, "
                        "p.&nbsp;710, stating the geokinetic claim they are about to answer: centrifugal "
                        "forces produce &ldquo;the polar flattening and equatorial bulge. This also explains "
                        "why the acceleration of gravity is less at the equator&rdquo; &mdash; and answering "
                        "it at p.&nbsp;711 not by denying those effects but by writing that they &ldquo;depend "
                        "on the assumption that the inertial effects can only be caused by the Earth&rsquo;s "
                        "rotation.&rdquo;"),
        drift_type="reversed",
        note=("<strong>Both books affirm the effect these items deny.</strong> Rowbotham prints the "
              "equatorial relief as a table &mdash; a seconds pendulum of 39.027 inches at the equator "
              "against 39.197 at the pole &mdash; and then argues about its <em>cause</em>. Sungenis and "
              "Bennett set the phenomenon out as the claim they mean to answer and then answer it by "
              "relocating the cause "
              "to a rotating universe, writing at Vol.&nbsp;I p.&nbsp;711 that the effects &ldquo;depend "
              "on the assumption that the inertial effects can only be caused by the Earth&rsquo;s "
              "rotation&rdquo;, and at ch.&nbsp;4, p.&nbsp;204 that the oblateness proves &ldquo;that "
              "there is a force causing their effect, not that a rotation of the Earth is the force.&rdquo; "
              "The same volume quotes Bertrand Russell, at p.&nbsp;49, on &ldquo;the flattening of the "
              "Earth at the poles, and the fact that bodies are heavier there than at the equator&rdquo;, "
              "and glosses Einstein at p.&nbsp;239 as holding that &ldquo;the Earth&rsquo;s poles would "
              "flatten from either reference frame&rdquo;. An argument about attribution has arrived on "
              "the list as an assertion of absence.<br><br>"
              "<strong>The nearest thing to a source for item 180, and it is in the same chapter.</strong> "
              "A few paragraphs below the Response, on that same p.&nbsp;711, Bennett restates Barbour and "
              "Bertotti&rsquo;s rotating-shell result and adds that &ldquo;an object at the center of the "
              "hollow sphere will not be affected by the inertial forces &hellip; but not the Earth itself, "
              "if it is centrally located&rdquo;. Read flat, that is a source statement that no centrifugal "
              "effect acts on the Earth &mdash; close to item 180, and in tension with the concession he "
              "has just made a few lines above. It is answered on the merits in section&nbsp;5 of the "
              "refutation: the "
              "cancellation holds at a <em>point</em> at the centre, and it is the variation of the "
              "centrifugal potential across a body 6,371&nbsp;km in radius, not the force at its centre, "
              "that raises a bulge. Recorded here because a scoped claim about what the sources do and do "
              "not assert has to carry its own counter-instance.<br><br>"
              "<strong>The four items do not agree with each other.</strong> Items 55 and 105 concede a "
              "bulge and dispute its cause; items 180 and 257 deny that there is anything to attribute. "
              "One phrasing is worth flagging as genuinely ambiguous: <em>&ldquo;No equatorial "
              "centrifugal relief&rdquo;</em> can be read as &ldquo;there is no reduction in weight at "
              "the equator&rdquo;, which is false and is what its neighbour item 180 commits it to, or "
              "as &ldquo;the reduction is not centrifugal in origin&rdquo;, which is Rowbotham&rsquo;s "
              "actual position. Four words cannot carry that distinction, and the distinction is the "
              "whole argument. <code>reversed</code> is recorded for the first reading, which is the one "
              "the list&rsquo;s own neighbouring item forces and the one a reader arrives with; the "
              "second reading is answered on the merits in section&nbsp;5 of the refutation.<br><br>"
              "<strong>The refutation answers the sources, not the fragments.</strong> Against Rowbotham "
              "it grants that the pendulum alone underdetermines the figure of the Earth, and then uses "
              "the expansion coefficient and the temperature range he quotes on his own page to show his "
              "named alternative cause is about eight times too small. Against Sungenis and Bennett it "
              "grants Mach, Einstein and the rotating-shell theorem at full strength, and puts the weight "
              "on the consequence: the same relative rotation rate produces the same bulge and the same "
              "0.53% weight difference, so the alternative cause predicts precisely what items 180 and "
              "257 report as absent.<br><br>"
              "<strong>One thing this entry does not claim.</strong> At Vol.&nbsp;I p.&nbsp;204 the book "
              "quotes Mach up to &ldquo;and so on&hellip;&rdquo;, stopping where the qualifying clause "
              "begins. That looks like a dropped hedge and it is not: at ch.&nbsp;7, p.&nbsp;460 the same "
              "volume prints the sentence in full, clause included, together with Mach&rsquo;s statement "
              "that he prefers to reformulate the law of inertia rather than accept absolute motion. On "
              "this argument the books are the careful party and the list is not.")),

    verdict_challenge=dict(challenged=False, proposed_verdict=None, reasoning=None),

    people=["PER-ROWBOTHAM", "PER-SUNGENIS"],
    related=["A09", "A10", "A14", "A15", "A17", "B06", "R01", "R02", "R05"],

    sources=[
        dict(label="Rowbotham (“Parallax”), Earth Not a Globe (1865) — Project Gutenberg ebook "
                   "#69892, the 1865 first book edition; the oblate-spheroid and seconds-pendulum "
                   "passage, with the Phillips temperature table and the Noad expansion figure",
             url="https://www.gutenberg.org/ebooks/69892"),
        dict(label="Rowbotham, Zetetic Astronomy: Earth Not a Globe, 3rd ed. 1881, ch. XIV "
                   "“Variability of Pendulum Vibrations” — the same argument with electricity and "
                   "magnetism added as a third alternative cause",
             url="https://sacred-texts.com/earth/za/za39.htm"),
        dict(label="Sungenis & Bennett, Galileo Was Wrong Vol. I — archive.org item "
                   "GallileoWasWrong; Bennett’s ch. 12 “Technical and Summary Analysis of "
                   "Geocentric Cosmology”, which opens at printed p. 710 (the geokinetic claim "
                   "as stated there — the bulge and the reduced equatorial gravity — and the "
                   "Machian response at p. 711), ch. 4 p. 204 (Mach clipped, and the oblateness "
                   "sentence), ch. 1 p. 49 (Russell), ch. 5 p. 239 n. 492 (Einstein), ch. 7 "
                   "p. 460 (Mach in full), ch. 11 p. 699 (satellite photographs), Appendix 7 "
                   "p. 1028 (WGS84). Printed numbers read from the page images, leaf by leaf",
             url="https://archive.org/details/GallileoWasWrong"),
        dict(label="Clairaut’s theorem — (g_p − g_e)/g_e = (5/2)m − f, and the Somigliana "
                   "normal-gravity formula that superseded it",
             url="https://en.wikipedia.org/wiki/Clairaut%27s_theorem_(gravity)"),
        dict(label="Jean Richer at Cayenne, 1672 — the clock losing 2m 28s a day and the "
                   "1¼-ligne shortening; Huygens attributing it to centrifugal force at the "
                   "equator, Newton to the equatorial bulge",
             url="https://en.wikipedia.org/wiki/Jean_Richer"),
        dict(label="Micro-g LaCoste FG5-X absolute gravimeter — free-fall corner cube in vacuum, "
                   "stated accuracy “2 µGal (observed agreement between FG5-X instruments)”",
             url="https://microglacoste.com/wp-content/uploads/2018/02/FG5-X-Brochure.pdf"),
        dict(label="Chambat, Ricard & Valette, “Flattening of the Earth: further from "
                   "hydrostaticity than previously estimated”, Geophys. J. Int. 183:727 (2010) — "
                   "the polar–equatorial radius difference is “113 ± 1 m … larger than the "
                   "hydrostatic value”",
             url="https://academic.oup.com/gji/article/183/2/727/655480"),
        dict(label="Cox & Chao, “Detection of a Large-Scale Mass Redistribution in the Terrestrial "
                   "System Since 1998”, Science 297:831 (2002) — the reversal of the secular "
                   "decrease in J₂",
             url="https://www.science.org/doi/10.1126/science.1072188"),
        dict(label="Dickey et al., “Recent Earth Oblateness Variations: Unraveling Climate and "
                   "Postglacial Rebound Effects”, Science 298(5600):1975 (2002) — ocean and ice "
                   "mass redistribution offered as the cause of the reversal",
             url="https://syrte.obspm.fr/~bizouard/ipercc/Biblio/dickey_ea_2002.pdf"),
        dict(label="Pfister & Braun, “Induction of correct centrifugal force in a rotating mass "
                   "shell”, Class. Quantum Grav. 2(6):909–918 (1985) — the modern resolution of "
                   "Thirring’s 1918 rotating-shell calculation",
             url="https://pascal-francis.inist.fr/vibad/index.php?action=getRecordDetail&idt=8729257"),
        dict(label="Watts, Isostasy and Flexure of the Lithosphere, ch. 1 — the Kaliana–Kalianpur "
                   "discrepancy (5.24″ observed against Pratt’s computed 15.885″) and the Pratt "
                   "and Airy responses of 1855",
             url="https://geofaculty.uwyo.edu/dueker/GeophysicsClass/watt%20isostasy%20flexure%20chap-1%20HISTORY.pdf"),
        dict(label="French Geodesic Mission to Lapland — Maupertuis’s 57,422-toise degree, the "
                   "figure Rowbotham quotes, and the 1/179 flattening it implied",
             url="https://en.wikipedia.org/wiki/French_Geodesic_Mission_to_Lapland"),
        dict(label="1911 Encyclopædia Britannica, “Earth, Figure of the” — Newton’s 229:230 and "
                   "Huygens’s 578:579, against the “577 to 875” printed in Earth Not a Globe",
             url="https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Earth,_Figure_of_the"),
    ]),
}
