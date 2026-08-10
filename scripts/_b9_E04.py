# -*- coding: utf-8 -*-
"""
Batch 9 — ARG-E04, "Quasar polarization alignment and large quasar groups".
4 items (90, 117, 321, 322), lane E, verdict MISLEADING, originator recorded null.

Research notes for whoever picks this up next. Five things, in order of how much
they change the entry.

1. THE CLUSTER IS TWO UNRELATED ARGUMENTS, welded by one sentence
   in the source. Item 90 is Varshni's 1976 concentric quasar SHELLS — perfect
   spherical symmetry about the Earth. Items 117/321/322 are the Hutsemekers
   polarization ALIGNMENT — a preferred axis. DO NOT say these are mutually
   exclusive: the geocentrism this book argues for is a universe ROTATING about a
   fixed Earth once a day (Vol. I ch. 2, the Foucault/equatorial-bulge answers), and
   such a universe has a centre AND an axis. An earlier draft of this entry claimed
   the source's model "predicts no preferred direction at all"; that was false about
   the source and has been withdrawn. What survives is that the two results rest on
   different data and different physics and are joined by nothing but "in other
   words" — and that the axis must then be answered on the measurements, which is
   what IV(a), (c) and (d) do. The weld is
   Galileo Was Wrong Vol. I, p. 414: "In other words, quasar distribution is
   centered around the Earth, just as Varshni had discovered thirty-six years
   earlier." That sentence is the passage quoted in this entry, and the whole
   refutation hangs off separating what it joins.

2. THE RECORD SAID UNTRACED; THREE OF THE FOUR ITEMS ARE IN SUNGENIS & BENNETT.
   Located in the seventh edition (2013) three-volume Internet Archive scan
   'galileo-was-wrong-the-church-was-right-sungenis-vol-1-3-complete', Vol. I,
   chapter 3 ("Evidence Earth is in the Center of the Universe"): Varshni at printed
   pp. 403-405, and the Urban & Zhitnitsky / Hutsemekers material at pp. 412-414.
   That is the same paragraph ARG-E13 traced item 194
   ("Photon spin alignment") to; 194 and 321 descend from one page. clusters.py was
   NOT touched — reported up instead. The fields worth the integrator's attention
   there are `originator`/`originator_work`/`year` (all null) and `real_source`,
   which names Hutsemekers and Clowes but not Varshni 1976, the ancestor of item 90.

3. THE URBAN & ZHITNITSKY PAPER IS IDENTIFIED, closing a question E13's curmudgeon
   pass left open ("we have not identified which Urban and Zhitnitsky paper is being
   quoted"). It is "The P-Odd Universe, Dark Energy and QCD", arXiv:1011.2425v2,
   dated 12 July 2011 — Sungenis's footnote gives 13 July 2011, p. 2, which matches
   the v2 posting to within a day. Both quoted passages are on p. 2 of that version,
   but in DIFFERENT subsections: the quasar paragraph is section II.A "Optical
   wavelengths", the ecliptic sentence is section II.C "Micro wavelengths". The
   ellipsis in Sungenis's quotation deletes the subject of "point all in the same
   direction" — "the normal vectors to the planes determined by the quadrupole and
   the octopole" — i.e. it deletes the CMB, and the interpolation "[sun-earth]"
   re-describes the ecliptic as an Earth-Sun structure.
   THAT IS ALL THAT SURVIVES, AND AN EARLIER DRAFT OVERREACHED IT. Do not say the
   book changes the subject from the CMB to quasars behind the reader's back. One
   sentence earlier, on printed p. 413, the book writes in its own voice: "Lastly, a
   team studying the orientation of quasars has discovered that they have a preferred
   axis, the same as they found for radio wavelengths and micro wavelengths (i.e.,
   the CMB)." And Urban & Zhitnitsky do argue for one common axis: II.A has the
   quasar vectors "closely align with the direction of the cosmological dipole",
   II.B has P-odd radio statistics "single out a preferred axis, again coinciding
   with the cosmological dipole", II.C has the CMB multipole normals. So item 117 is
   a real claim and section V answers it rather than dismissing it as a misquotation.
   Two numbers for that answer, both from astro-ph/0507274 footnote 9: quasar
   A1-A3 axis (lII = 267, bII = 69), CMB dipole (lII = 264, bII = 48).
   Also: the word "ecliptic" does not occur anywhere in the text of Hutsemekers et
   al. 2005 as searched here — that paper works in equatorial, galactic and
   supergalactic frames only, so IV(d) rebuts an equatorial-frame axis and no
   ecliptic-frame test is reported either way in the papers cited on this page.

4. VARSHNI 1976 IS A REDUCTIO AND THE FOOTNOTE PROVES SUNGENIS KNEW. Read Ap&SS
   43:3-8 to the last paragraph: three candidate explanations, the third is a
   central Earth, and Varshni then writes that before accepting "such an unaesthetic
   possibility" we must ask whether the red shifts are real, pointing at his own
   laser-star model, which "does not require any red shifts". His argument is that
   quasars are NOT at cosmological distances. The footnote on p. 404 of Galileo Was
   Wrong prints that escape hatch verbatim while the body text above it presents the
   shells as a discovery. (Do not cite a footnote NUMBER from that scan: the
   superscripts are OCR-degraded to degree signs and any number you read off them is
   a guess. Cite the printed page.) So
   the reversal happens at the Varshni -> Sungenis link and the hedge-drop at the
   Sungenis -> list link; `drift_type` has one slot and the note carries both.

5. NUMBERS RECOMPUTED IN-SESSION (2026-08-09), seed 20260809, 4 000 realisations
   each: 384 redshifts drawn uniformly on 0.2-3.53 give 37.8 +/- 4.9 groups sharing
   a fixed 0.002-wide bin and 64.1 +/- 5.3 clumps of two or more within 0.002 of one
   another; drawn from a realistically peaked n(z) (beta(2,3) over the same range)
   those rise to 48.4 +/- 5.1 and 76.7 +/- 5.3. Varshni found 57 groups. The uniform
   draw is the CONSERVATIVE null — clustering the parent distribution makes
   coincidences commoner, not rarer — and the body says so, because that is the
   first objection a numerate defender makes.

Item 322, "Large quasar groups ecliptic", was not matched to any sentence. Searched
the same three-volume scan for "Clowes", "LQG", "large quasar" and "quasar group":
no hits in that text. Recorded as unmapped rather than as an unsourced addition,
following the discipline set at ARG-E03 — an addition is something we would have to
demonstrate, not suspect.
"""

ENTRY = {

"E04": dict(

    tldr=("Two unrelated arguments were welded together here by the words “in other words”. "
          "Varshni's 1976 quasar shells were a reductio in his own paper — his conclusion was "
          "that if quasar redshifts are cosmological you get an absurdity, so they are not "
          "cosmological — and 384 redshifts scattered at random produce about as many "
          "near-coincidences as he found. The polarization alignment is the other kind of "
          "case: a real, replicated signal whose gigaparsec-scale coherence is not fully "
          "explained, but whose preferred direction rotates about 30° per gigaparsec, whose "
          "apparent axis is read off a sky map the measuring team called “definitely affected "
          "by observational biases”, and whose more natural reference frame, in those same "
          "authors' words, is the Local Supercluster's. "
          "That is a set of directions, and a direction on its own does not locate a centre."),

    passage=dict(
        work="WRK-SUNGENIS-2006",
        pd=False,
        locator=("Vol. I, ch. 3 (“Evidence Earth is in the Center of the Universe”), printed "
                 "p. 414 of the seventh edition, 2013, as it appears in the Internet Archive "
                 "three-volume scan galileo-was-wrong-the-church-was-right-sungenis-vol-1-3-"
                 "complete. The footnote to the quoted sentence cites “The P-Odd Universe, "
                 "Dark Energy and QCD,” Federico R. Urban and Ariel R. Zhitnitsky, Univ. of "
                 "British Columbia, July 13, 2011, p. 2. Retrieved from the OCR text layer of "
                 "that scan; not checked against a print copy."),
        quote=("Urban adds that the “identifiable preferred axis, the cosmological "
               "dipole…point all in the same direction, that of the [sun-earth] ecliptic or "
               "equinox.” In other words, quasar distribution is centered around the Earth, "
               "just as Varshni had discovered thirty-six years earlier."),
        gloss="""<p>Four findings. The first one decides the shape of everything below it.</p>

<p><strong>1. The three words that do the work are &ldquo;in other words&rdquo;.</strong> They join two results that have nothing to do with one another. Varshni&rsquo;s result, set out nine pages earlier at pp.&nbsp;403&ndash;405, is that quasars sit on <em>concentric spherical shells</em> centred on the Earth &mdash; perfect spherical symmetry, no preferred direction anywhere. The Urban and Zhitnitsky material on this page is about a <em>preferred axis</em> &mdash; one direction singled out of all the others. It would be a cheap win to call those mutually exclusive, and this entry does not: the geocentrism this book argues for is a universe that turns about a fixed Earth once a day, and such a universe has a centre <em>and</em> an axis. What the two results are is unrelated &mdash; different objects, different instruments, different physics &mdash; and what joins them is the phrase &ldquo;in other words&rdquo; and nothing else. The list inherited both and files them four items apart (item&nbsp;90 and item&nbsp;117), so a reader meets them as two independent witnesses when neither is a witness for the other.</p>

<p><strong>2. The ellipsis deletes the subject of the sentence &mdash; and the book names the CMB anyway.</strong> Urban and Zhitnitsky&rsquo;s sentence, in section II.C of their paper, headed <em>Micro wavelengths</em>, reads in full: <em>&ldquo;there is a very easily identifiable preferred axis, the cosmological dipole once again; that is, the normal vectors to the planes determined by the quadrupole and the octopole (there are four of them) point all in the same direction, that of the ecliptic or equinox.&rdquo;</em> The quadrupole and the octopole are multipoles of the <strong>microwave background</strong>. Sungenis&rsquo;s ellipsis removes them, so the verb loses its subject, and his bracketed <em>&ldquo;[sun-earth]&rdquo;</em> re-describes the ecliptic as an Earth&ndash;Sun structure; item&nbsp;117, <em>&ldquo;Quasar alignment with ecliptic&rdquo;</em>, is what comes out the far end. <strong>That is where the complaint stops.</strong> One sentence before the block quotation, on printed p.&nbsp;413, the book says in its own voice that the quasar team found <em>&ldquo;a preferred axis, the same as they found for radio wavelengths and micro wavelengths (i.e., the CMB)&rdquo;</em> &mdash; the subject the ellipsis removed is named, and named as the CMB, on the preceding page. And one axis common to optical, radio and micro is the quoted paper&rsquo;s own thesis, not something manufactured here. So this is not a subject swapped behind the reader&rsquo;s back; it is a real claim, and it is answered as one in section&nbsp;V.</p>

<p><strong>3. The book prints Varshni&rsquo;s escape hatch in its own footnote.</strong> At p.&nbsp;404 the footnote to that passage reproduces the sentences in which Varshni declines the geocentric reading and points instead at his laser-star model, which in his words <em>&ldquo;does not require any redshifts.&rdquo;</em> So the source is not concealing the reversal &mdash; it is carrying it, in small type, under a body text that presents the shells as a discovery. That is the single most useful fact in this entry for the hedge rule: the qualification survives as far as the footnote and dies between the footnote and the list.</p>

<p><strong>4. What our own record held.</strong> E04 was recorded with a null originator, null work and null year. Three of the four items were then located in the seventh edition (2013) of <em>Galileo Was Wrong</em>, Volume&nbsp;I, chapter&nbsp;3: the Varshni material at printed pp.&nbsp;403&ndash;405 and the Urban / Hutsem&eacute;kers material at pp.&nbsp;412&ndash;414. The same page&nbsp;413 paragraph is where <a href="#ARG-E13">ARG-E13</a> traced item&nbsp;194, so items 194 and 321 descend from one page of one chapter. Item&nbsp;322, <em>&ldquo;Large quasar groups ecliptic&rdquo;</em>, was not matched: searching that three-volume scan for &ldquo;Clowes&rdquo;, &ldquo;LQG&rdquo;, &ldquo;large quasar&rdquo; and &ldquo;quasar group&rdquo; returned no hits in that text, and the item is recorded here as unmapped rather than as an addition, which would have to be demonstrated rather than suspected.</p>"""),

    steelman=dict(
        description="""<p><strong>SURFACE (weak &mdash; do not use).</strong> &ldquo;Quasar polarization alignment is just dust in our own Galaxy.&rdquo; This is the reflex answer and it has been tested and found wanting. Pelgrims (<em>A&amp;A</em> 622:A145, 2019) took the Planck full-sky dust polarization maps to the 355 sightlines and found signatures of Galactic dust contamination at the two-sigma level for about 30% of them, with the other ~70% showing none, concluding that thermal dust &ldquo;cannot fully account for the reported quasar optical polarization alignments&rdquo;. Anyone who opens with dust will be handed that paper.</p>

<p><strong>DEEPER.</strong> The effect is real and it has survived independent statistics. Hutsem&eacute;kers, Cabanac, Lamy and Sluse (<em>A&amp;A</em> 441:915, 2005) measured 355 polarized quasars and reported that the polarization vectors are &ldquo;not randomly oriented over the sky with a probability often in excess of 99.9%&rdquo;, coherent over ~1&nbsp;Gpc regions. Pelgrims and Cudell (<em>MNRAS</em> 442:1239, 2014) built a different estimator from scratch and found the probability that one redshift region&rsquo;s polarization directions are random to be &ldquo;as low as 0.003%&rdquo;. This is not a marginal result being kept alive by one group&rsquo;s method.</p>

<p><strong>THE COMMON-AXIS CLAIM, WHICH IS ITEM&nbsp;117 AT ITS BEST.</strong> Do not let the ecliptic item be reduced to a mangled quotation. Put at full strength it says: three independent observational channels have been reported picking out one region of sky. Urban and Zhitnitsky assemble exactly that list on their p.&nbsp;2 &mdash; optical quasar polarization vectors that &ldquo;tend to identify an axis in the sky which closely align with the direction of the cosmological dipole&rdquo;; P-odd radio statistics that &ldquo;single out a preferred axis, again coinciding with the cosmological dipole&rdquo;; and CMB quadrupole and octopole normals pointing along &ldquo;the ecliptic or equinox&rdquo;. Hutsem&eacute;kers et al. corroborate the geometry in their own footnote: the quasar A1&ndash;A3 axis at l<sup>II</sup>&nbsp;=&nbsp;267&deg;, b<sup>II</sup>&nbsp;=&nbsp;69&deg;, the CMB dipole at l<sup>II</sup>&nbsp;=&nbsp;264&deg;, b<sup>II</sup>&nbsp;=&nbsp;48&deg;, and region A1 lying towards Virgo. A defender who says &ldquo;several unrelated measurements keep landing in the same part of the sky, and one of the planes that part of the sky is near is the plane of the Earth&rsquo;s orbit&rdquo; is saying something the literature says too. Concede the assembly. The argument is about what it licenses.</p>

<p><strong>KERNEL.</strong> The strongest form of this argument is not about quasars pointing at us. It is that <em>coherent orientation on gigaparsec scales is not predicted by anything, and the mechanism on offer does not fully cover it.</em> The accepted astrophysics &mdash; quasar spin axes aligning with the large-scale structure they grew in (Hutsem&eacute;kers et al., <em>A&amp;A</em> 572:A18, 2014; independently in radio, Pelgrims &amp; Hutsem&eacute;kers, <em>A&amp;A</em> 590:A53, 2016) &mdash; explains alignment <em>relative to a filament</em>. It does not explain why the filaments themselves should be correlated across a billion parsecs, and when Friday, Clowes and Williger went looking for exactly that (<em>MNRAS</em> 511:4159, 2022) they reported correlated large-quasar-group axes at typical separations of ~1.6&nbsp;Gpc and wrote that if real it is &ldquo;at least an order of magnitude larger than any so far observed&rdquo; alignment of structure. And Varshni has a kernel of his own, which deserves saying plainly: his reasoning that a structure arranged in shells about our position would falsify the cosmological principle is <em>correct reasoning</em>, and it is the same reasoning cosmologists use when they test homogeneity rather than assume it. Concede all of that.</p>""",
        why_it_doesnt_save_claim="""<p><strong>Not because a centre and an axis are incompatible.</strong> That reply is available and this page declines it: the geocentrism being defended is a universe rotating about a fixed Earth once a day, which has a centre and an axis both, so &ldquo;you cannot claim a preferred direction&rdquo; is a technicality the source never walked into. The true objection is weaker and sufficient. The two halves of the cluster are unrelated measurements joined by an &ldquo;in other words&rdquo;; the shells half fails on Varshni&rsquo;s own argument and on the arithmetic; and the axis half has to be met on what was actually measured &mdash; which is done, in section&nbsp;IV.</p>

<p><strong>And what was measured is not one direction.</strong> The 2005 paper&rsquo;s own abstract says the aligned regions sit at both z&nbsp;~&nbsp;0.5 and z&nbsp;~&nbsp;1.5 and are &ldquo;characterized by different preferred directions&rdquo;; that the mean polarization angle &ldquo;appears to rotate with redshift at the rate of ~30&deg; per Gpc&rdquo;; and that there is a &ldquo;regular alternance&rdquo; of aligned and randomly oriented regions along the line of sight on a scale of about 1.5&nbsp;Gpc. A single axis fixed in the sky and running through the Earth predicts one direction, holding at all distances. This is a quantity that changes as you go out, and turns back into noise and out of it again.</p>

<p><strong>The authors state the selection bias themselves.</strong> On the question of whether the aligned regions define an axis, the 2005 paper says the distribution &ldquo;is definitely affected by observational biases&rdquo;, explains that the alignments were first found near the celestial equator and that follow-up observation was then concentrated there, and adds that &ldquo;it is not unexpected that the highest quasar densities and the highest significances do appear in these regions&rdquo;. Only 46 of the 355 quasars lie in the third of the sky opposite the high-significance regions, and the paper closes the section by saying that whether alignments exist away from that axis &ldquo;is still to be demonstrated&rdquo;.</p>

<p><strong>Finally, on Varshni: his own paper spends the result rather than banking it,</strong> and the arithmetic does not survive. Both points are worked below.</p>"""),

    refutation="""<p>This cluster carries two claims with two different ancestors and two different failure modes. Take them apart first, because the source&rsquo;s own sentence is what glues them: <em>&ldquo;In other words, quasar distribution is centered around the Earth, just as Varshni had discovered.&rdquo;</em> One half says the quasars are arranged with perfect spherical symmetry about us. The other half says they single out a direction. It is tempting to stop there and call that a contradiction, and it is not one: the model this book argues for is a universe rotating about a fixed Earth once a day, and a rotating universe has a centre and an axis together. What the sentence does is not contradict itself. It splices. The two results come from different objects, different instruments and different physics, and the only thing holding them together is the phrase <em>in other words</em>. So they are separated here and answered one at a time.</p>

<h4>I. Varshni 1976 is an argument that quasar redshifts are <em>not</em> cosmological</h4>

<p>The paper is Y. P. Varshni, &ldquo;The Red Shift Hypothesis for Quasars: Is the Earth the Center of the Universe?&rdquo;, <em>Astrophysics and Space Science</em> 43:3&ndash;8 (1976), received 10 September 1975. Note the question mark, and note the abstract&rsquo;s framing: the cosmological interpretation of quasar redshifts &ldquo;leads to <strong>yet another paradoxical result</strong>&rdquo;. <em>Another</em> &mdash; this is one entry in a list of things Varshni thought were wrong with the redshift hypothesis, and it is offered as a cost of that hypothesis, not as a discovery about the Earth.</p>

<p>The structure is a disjunctive syllogism. Varshni takes 384 quasars with 0.2 &le; z &le; 3.53 as of June 1975, identifies 57 groups whose members have closely coincident redshifts and similar spectra, and lists three ways the coincidences could arise: clustering, a crystal-lattice arrangement, or a central Earth. He eliminates the first two, then reaches possibility three, and here is the whole paper in two sentences: <em>&ldquo;We are essentially left with only one possibility &ndash; No.&nbsp;3 in the cosmological red-shift interpretation. However, before we accept such an unaesthetic possibility, we must raise the question: Are the &lsquo;red shifts&rsquo; real?&rdquo;</em> He answers his own question by pointing at the model he had been publishing since 1973, in which quasar spectral lines come from laser action in stellar envelopes and which, in his words, <em>&ldquo;does not require any red shifts, and has no basic difficulty&rdquo;</em>. The epigraph he chose for the paper is Holton on Einstein&rsquo;s two criteria for a theory, external confirmation and inner perfection. It is a theory-choice paper. Its conclusion is that quasars are not at cosmological distances.</p>

<p>So the list&rsquo;s item&nbsp;90 asserts as a proof the horn of a dilemma that the man who drew the dilemma rejected, in print, in the same paragraph. And the book that carries the item to the list <strong>prints his rejection in its own footnote</strong> on p.&nbsp;404 while the body text above it presents the shells as a finding. Nothing was concealed. The qualification simply did not survive the last step of the chain.</p>

<h4>II. The 57 groups are what 384 redshifts do on their own</h4>

<p>Varshni&rsquo;s probability comes from a formula of Burbidge&rsquo;s for the chance that <em>k</em> of <em>r</em> redshifts fall inside one box of width &Delta;z, with the box width set at 0.002 by measurement error. He computes that probability for each of his 57 groups and multiplies: <em>&ldquo;the probability of these 57 sets of coincidences occurring in this system of 384 QSOs is &asymp; 3 &times; 10<sup>&minus;85</sup>&rdquo;</em>, and adds that he hopes the number will convince the reader the coincidences are real.</p>

<p>The error is that the boxes were drawn after the data were seen. Varshni says so in the method: the width of each group was defined as <em>z</em>(highest) &minus; <em>z</em>(lowest) + 0.002. A probability computed for a box fitted to the points inside it is not the probability of anything happening; and multiplying 57 such numbers compounds the mistake 57 times. The question that has an answer is different: <strong>how many such groups does a random catalogue of 384 quasars produce?</strong></p>

<p>Recomputed here, 4&nbsp;000 realisations, seed recorded in this file&rsquo;s notes. Draw 384 redshifts uniformly on 0.2&ndash;3.53 and count how often two or more land in the same fixed 0.002-wide bin: <strong>37.8&nbsp;&plusmn;&nbsp;4.9 groups</strong>. Count instead clumps of two or more objects lying within 0.002 of each other, which is closer to what Varshni actually did: <strong>64.1&nbsp;&plusmn;&nbsp;5.3</strong>. He found 57. It sits between the two ways of counting the same null.</p>

<p><strong>Deal with the obvious objection before it is raised,</strong> because it is a good one and it runs the wrong way for the argument. Real quasar redshifts are not uniformly distributed; they pile up around z&nbsp;~&nbsp;1&ndash;2. Any concentration of the parent distribution makes near-coincidences <em>more</em> common, not fewer. Drawing the same 384 objects from a realistically peaked n(z) over the same range raises the counts to 48.4&nbsp;&plusmn;&nbsp;5.1 fixed-bin groups and 76.7&nbsp;&plusmn;&nbsp;5.3 clumps. The uniform draw was the conservative choice. Nor does the second selection criterion help: Varshni notes that his table &ldquo;is based more on the similarities in the spectra of the quasars constituting a group, than on the nearness of their red shifts&rdquo;, but the probability he quotes is computed purely from redshift proximity, so choosing which coincidences to keep on a second, independent criterion widens the search rather than narrowing it.</p>

<p>One thing to be precise about, because it is a boundary this review polices elsewhere: this is <em>not</em> the Tifft-style redshift quantization argued at <a href="#ARG-E12">ARG-E12</a>. Varshni says so himself &mdash; his coincidences &ldquo;are to be clearly distinguished from the &lsquo;peaks&rsquo; that some authors have claimed in the red shift distribution&rdquo;. Two different claims, two different refutations, and running them together would be the same error this entry is documenting.</p>

<h4>III. Both horns have since been settled, and neither settles the geocentrist&rsquo;s way</h4>

<p>Varshni&rsquo;s dilemma was: either the Earth is central, or quasar redshifts are not cosmological. The second horn is the one he took, and it is the one that died. Quasar variability is time-dilated: Lewis and Brewer (<em>Nature Astronomy</em> 7:1265, 2023) monitored 190 quasars over two decades in multiple bands and detected the redshift-dependent slowing that expansion requires, concluding that the properties of quasars are &ldquo;consistent with them being truly cosmologically distant sources&rdquo;. A laser-star inside our own Galaxy has no mechanism for running slow in proportion to its redshift. And the first horn dissolved as the samples grew: the SDSS DR16 quasar catalogue (Lyke et al., <em>ApJS</em> 250:8, 2020) contains 750&nbsp;414 spectroscopically confirmed quasars, roughly two thousand times Varshni&rsquo;s 384, estimated 99.8% complete. Shells drawn from 384 objects that were consistent with chance in 1976 have not been recovered from a catalogue three orders of magnitude larger.</p>

<h4>IV. The polarization alignment, at full strength, and what it is an alignment of</h4>

<p>Now the half of the cluster that rests on something real. Hutsem&eacute;kers, Cabanac, Lamy and Sluse mapped the optical linear polarization of 355 quasars and confirmed that the vectors are &ldquo;not randomly oriented over the sky with a probability often in excess of 99.9%&rdquo;, coherently oriented over regions ~1&nbsp;Gpc across. Pelgrims and Cudell later built an independent estimator and got a probability as low as 0.003% for one region. Pelgrims tested the obvious foreground against Planck&rsquo;s dust maps and found dust cannot fully account for it. <strong>The effect is real, replicated and not fully explained, and this page says so without hedging.</strong></p>

<p>What the effect will not do is point at anybody. Four things about the measurement, all from the paper the argument cites. The second is a feature this entry declines to use, and the reason is worth as much as the other three.</p>

<p><strong>(a) The preferred direction changes with distance.</strong> The aligned regions sit at low (z&nbsp;~&nbsp;0.5) and high (z&nbsp;~&nbsp;1.5) redshift and are &ldquo;characterized by different preferred directions&rdquo;, with the mean angle rotating at ~30&deg; per Gpc. Along a single line of sight the paper finds a &ldquo;regular alternance&rdquo; of aligned and randomly oriented regions on a scale of about 1.5&nbsp;Gpc. That is a corkscrew, not a spoke.</p>

<p><strong>(b) The handedness flip, and why it is not used here.</strong> The abstract does state it flatly &mdash; the mean angle rotating clockwise with increasing redshift in the North Galactic cap and counter-clockwise in the South &mdash; and an earlier version of this page leaned on it, arguing that a mirror symmetry about the Galactic plane must be a fact about our position in the Milky Way and so the work of some Galactic or local mechanism. That argument is withdrawn, for two reasons, both in the same paper. First, the paper says the opposite about local mechanisms: these characteristics, the abstract writes, &ldquo;make the alignment effect difficult to explain in terms of local mechanisms, namely a contamination by interstellar polarization in our Galaxy&rdquo;. Second, the body hedges the flip in ways the abstract does not. The mirror-like (S1) relation is &ldquo;the best defined and the most significant&rdquo;, but &ldquo;a counter-clockwise rotation in both the South and North Galactic Caps (S2 symmetry) cannot be totally excluded&rdquo;; &ldquo;both the slope and the constant of the linear fit depend on the coordinate system&rdquo;; &ldquo;due to the 180&deg; uncertainty, several other complicated or asymmetric solutions&rdquo; to the same relation &ldquo;could be imagined&rdquo;; and a step-like discontinuity at z&nbsp;=&nbsp;0 is expected in general, the authors explain, simply from the way position angles are defined for a structure crossing the observer. And the authors&rsquo; own reading of the symmetry, if it holds, runs the other way: it &ldquo;would be accounted for by a rotation axis close to the A1&ndash;A3 axis&rdquo; &mdash; a global rotation of the universe, which is nearer the defender&rsquo;s picture than to ours. So this page does not spend it. The weight of section&nbsp;IV sits on (a), (c) and (d), which do not turn on a choice of coordinates.</p>

<p><strong>(c) The mechanism now on the table is about filaments, not about us.</strong> Hutsem&eacute;kers and colleagues measured polarization for quasars inside gigaparsec-scale quasar groups and found the vectors &ldquo;either parallel or perpendicular to the directions of the large-scale structures to which they belong&rdquo;, with the parallel/perpendicular split tracking emission-line width &mdash; that is, viewing inclination &mdash; and concluded that quasar spin axes are likely parallel to their host structures. Pelgrims and Hutsem&eacute;kers reproduced the correlation independently using radio polarization for quasars in a much larger sample of groups. The physical claim is that supermassive black holes end up spinning along the filaments they grew in, which is a statement about how structure forms and contains no reference to the observer.</p>

<p><strong>(d) The Earth-frame alignment is a sampling artefact the authors flagged, and the natural frame is the local supercluster&rsquo;s.</strong> Asked directly whether the aligned regions define an axis, the 2005 paper answers that the map &ldquo;is definitely affected by observational biases&rdquo;: the first alignments were found near the celestial equator, follow-up observing was then concentrated there, and quasars are surveyed in equatorial fields anyway, so &ldquo;it is not unexpected that the highest quasar densities and the highest significances do appear in these regions&rdquo;. Only 46 of 355 objects lie in the opposite third of the sky. The same paper reports that the statistical significance is &ldquo;not extreme in the equatorial coordinate system&rdquo; and that many other coordinate systems do better &mdash; the opposite of what an Earth-oriented effect would give. And when the authors extrapolate the mean polarization angle to z&nbsp;=&nbsp;0 they get 90&deg; in equatorial coordinates, which they call &ldquo;an unpleasant coincidence&rdquo;, noting that the same value is 0&deg; in the <em>supergalactic</em> frame &mdash; the plane of the Local Supercluster. The frame in which the number comes out simple is the one defined by the nearby matter, not by the Earth&rsquo;s spin axis or its orbit.</p>

<h4>V. The ecliptic sentence is about the microwave background &mdash; and the book says so a page earlier</h4>

<p>Item&nbsp;117 says &ldquo;Quasar alignment with ecliptic.&rdquo; Its ancestor is the sentence quoted at the top of this entry, and two pieces of editing in that sentence are worth naming. Urban and Zhitnitsky wrote, in the subsection of their paper headed <em>Micro wavelengths</em>: <em>&ldquo;there is a very easily identifiable preferred axis, the cosmological dipole once again; that is, the normal vectors to the planes determined by the quadrupole and the octopole (there are four of them) point all in the same direction, that of the ecliptic or equinox.&rdquo;</em> The quadrupole and the octopole are multipoles of the CMB. The quotation cuts the clause between the semicolon and &ldquo;point&rdquo;, so the verb loses its subject; and the interpolation <em>&ldquo;[sun-earth]&rdquo;</em> re-describes the ecliptic, which is the plane of the Earth&rsquo;s orbit about the Sun, as a structure belonging to the pair of them.</p>

<p><strong>And that is where the complaint has to stop, because the book is not hiding the subject.</strong> One sentence before the block quotation, on printed p.&nbsp;413, <em>Galileo Was Wrong</em> writes in its own voice that a team studying quasar orientations found &ldquo;a preferred axis, the same as they found for radio wavelengths and micro wavelengths (i.e., the CMB)&rdquo;. The microwave background is named, and glossed as the CMB, before the quotation begins. Nor is a single axis spanning the three bands an invention of the book&rsquo;s: it is the quoted paper&rsquo;s thesis. Section II.A reports that the optical polarization vectors &ldquo;tend to identify an axis in the sky which closely align with the direction of the cosmological dipole&rdquo;; II.B reports P-odd radio statistics that &ldquo;single out a preferred axis, again coinciding with the cosmological dipole&rdquo;; II.C is the ecliptic sentence. Item&nbsp;117 is therefore a claim to answer, not a misquotation to expose. Here is the answer, in three parts.</p>

<p><strong>First, the CMB half is real and is argued elsewhere.</strong> The quadrupole&ndash;octopole planarity and its proximity to the ecliptic are a genuinely unsettled question, they are not disposed of by this page, and this review takes them at full strength at <a href="#ARG-E01">ARG-E01</a>. What they are not is a measurement of quasars.</p>

<p><strong>Second, &ldquo;the same axis&rdquo; is the same to a couple of dozen degrees, and the authors say so.</strong> Hutsem&eacute;kers et al. put the numbers in a footnote: the quasar A1&ndash;A3 axis at l<sup>II</sup>&nbsp;=&nbsp;267&deg;, b<sup>II</sup>&nbsp;=&nbsp;69&deg;, the CMB dipole at l<sup>II</sup>&nbsp;=&nbsp;264&deg;, b<sup>II</sup>&nbsp;=&nbsp;48&deg;, which they describe as &ldquo;not far from&rdquo; each other and offer as a <em>possible</em> coincidence worth investigating. The same paper says the sky distribution the axis is read off &ldquo;is definitely affected by observational biases&rdquo;, and that whether alignments exist away from that axis &ldquo;is still to be demonstrated&rdquo;. An axis established that way will not carry a conclusion about where the universe is centred.</p>

<p><strong>Third, the authors being cited decline the coincidence themselves.</strong> Urban and Zhitnitsky&rsquo;s footnote&nbsp;2, hung on the quasar paragraph, notes that the non-local character of the effect &ldquo;is somewhat at odds with the preferred axis coinciding with the local Doppler dipole; for the time being and for our discussion this is taken to be mere coincidence&rdquo;. And their own model is a <em>parity-odd universe</em>, in which a pseudoscalar field related to dark energy rotates the polarization of light crossing it: a mechanism with an axis and no centre. They are proposing new physics for the direction, not a location for the Earth.</p>

<p><strong>One gap here is ours, and it is recorded as a gap.</strong> Item&nbsp;117 names the <em>ecliptic</em>. The word does not occur anywhere in the text of Hutsem&eacute;kers et al. 2005 as searched for this entry; that paper works in equatorial, galactic and supergalactic frames, and section&nbsp;IV(d) above accordingly rebuts an equatorial-frame axis rather than an ecliptic one. No test of the quasar polarization alignment against the ecliptic plane is reported in any of the papers cited on this page, in either direction. The ecliptic in item&nbsp;117 arrives from the CMB sentence, and it is answered where the CMB is answered.</p>

<h4>VI. Large quasar groups: a live disagreement, and it is not about the ecliptic</h4>

<p>Item&nbsp;322 invokes large quasar groups. The underlying work is Clowes et al. (<em>MNRAS</em> 429:2910, 2013), who identified the Huge-LQG in the SDSS DR7 quasar catalogue: 73 quasars, characteristic size ~500&nbsp;Mpc, longest dimension ~1240&nbsp;Mpc at &lt;z&gt;&nbsp;=&nbsp;1.27, which they said &ldquo;challenges the assumption of the cosmological principle&rdquo;. That is a real claim in a real journal and it should be stated at that strength.</p>

<p>It was answered the same year, and the answer is the one that matters here. Nadathur (<em>MNRAS</em> 434:398, 2013) ran the first fractal-dimension analysis of the DR7 quasar catalogue, found it homogeneous above scales of at most 130&nbsp;<em>h</em><sup>&minus;1</sup>&nbsp;Mpc, and &mdash; the decisive part &mdash; showed that the friends-of-friends algorithm used to find the Huge-LQG &ldquo;regularly finds even larger clusters of points, extending over Gpc scales, in explicitly homogeneous simulations of a Poisson point process with the same density as the quasar catalogue&rdquo;. Structures that an algorithm finds just as readily in noise are not evidence about homogeneity. The argument has continued: Friday, Clowes and Williger (<em>MNRAS</em> 511:4159, 2022) reported that LQG axes themselves are correlated, at a maximum significance of ~0.8% (2.4&sigma;) over ~1.6&nbsp;Gpc; Fujii (<em>MNRAS</em> 527:1982, 2024) reproduced their sample, applied Sobolev tests to the orientation axes in redshift space, &ldquo;found no departure from uniformity&rdquo;, and concluded that the LQG sample &ldquo;is a collection of unphysical chance associations and should not be used for any cosmological studies&rdquo;. That exchange is open, and this page is not going to pretend otherwise.</p>

<p>What can be said flatly is what the item adds. In the abstracts and stated conclusions of the four papers cited in this section &mdash; Clowes 2013, Nadathur 2013, Friday 2022, Fujii 2024 &mdash; the claims are put in terms of homogeneity scales, position angles and redshift-space uniformity, and the ecliptic is not among the terms used. The ecliptic arrived from the sentence dissected in section&nbsp;V, one cluster over.</p>

<h4>VII. A prediction was made from this material, and it was tested</h4>

<p>The book quotes John Ralston&rsquo;s <em>Question Isotropy</em> at p.&nbsp;414, including a forecast: the Planck polarization data were awaited, and &ldquo;spontaneous alignment of polarizations will occur along the axis of Virgo&rdquo;. Planck 2018 results VII (<em>A&amp;A</em> 641:A7) was the first comprehensive analysis of the statistics of the polarization signal, and it reports that in the regime where the null tests are clean &mdash; multipoles below about 400 &mdash; &ldquo;no unambiguous detections of cosmological non-Gaussianity, or of anomalies corresponding to those seen in temperature, are claimed&rdquo;, while confirming the temperature anomalies themselves. Represent the caveat honestly, because it is in the paper: residual systematics still limit some large-angle polarization tests. But a prediction was made from the axis material, the measurement came in, and it did not go the way the prediction said.</p>

<h4>VIII. Verdict</h4>

<p><strong>Misleading, and precisely in the sense the word is for.</strong> Every measurement in this cluster is somebody else&rsquo;s, taken for other purposes, and three of the four are correctly reported as far as they go. What is added is the inference, and the inference has two failures rather than one. The Varshni half takes a reductio for a result and rests on a probability computed after the boxes were drawn round the points. The alignment half takes a set of directions &mdash; rotating with distance, alternating in and out of coherence along the line of sight, explained so far as it is explained by black-hole spins tracking their filaments &mdash; and reads them as an arrow pointing here. A direction is not an origin, which is the same structural inversion recorded at <a href="#ARG-E03">ARG-E03</a> for the dipole and at <a href="#ARG-A03">ARG-A03</a> for aberration. The model these items are marshalled for does have an axis of its own to offer &mdash; a universe rotating about a fixed Earth once a day &mdash; and that is why the answer here is not a logical objection but a measurement one: the axis that was actually found does not point at the Earth, it changes direction with distance, the sky map it is read off is on its own authors&rsquo; account biased by where they chose to observe, and the frame in which its numbers come out simple is the Local Supercluster&rsquo;s.</p>""",

    advocate=dict(
        best_defense=(
            "You have done good work on Varshni and I will give you item 90 without a fight — "
            "he did prefer the laser-star model and that model is dead. Now notice what you "
            "have left yourself. You concede the polarization alignment is real. You concede "
            "it survived an independent estimator at 0.003%. You concede Planck dust maps "
            "cannot account for it. You concede the LQG orientation question is open and that "
            "the people who say it is noise and the people who say it is structure are still "
            "arguing. You concede coherence over a gigaparsec is not predicted by any "
            "simulation. So the sum of your position is: there is a large-scale organisation "
            "of the universe that your cosmology did not predict, cannot presently explain, "
            "and keeps finding in a direction near the one your own dipole picks out. And do "
            "not try to reduce item 117 to a mangled quotation: your own section V now admits "
            "our book named the microwave background in its own voice a page before the "
            "quotation, and that the paper we quoted argues for one axis running through "
            "optical polarization, radio and the CMB multipoles alike, all of it near the "
            "cosmological dipole. Three separate channels, one patch of sky, and one of the "
            "planes that patch lies near is the plane of the Earth's orbit. Your "
            "reply is that a direction is not a centre. Fine — but 'not a centre' is not an "
            "explanation either, and you are using a logical point to stand in for a physical "
            "one you do not have. On the rotation with redshift: you present 30° per Gpc as "
            "though it embarrassed us. It is a rotation about an axis. An axis is what we "
            "claimed. On the hemispheric flip: mirror symmetry about the observer's own "
            "galactic plane is a strange thing for a universe with no special observer to "
            "produce, and you have quoted it as if it settled something. And your Monte Carlo "
            "is a null for redshift coincidences, not for Varshni's actual selection, which "
            "used spectral similarity — you admit this in a subordinate clause and then move "
            "on. Finally: Hutsemékers said the axis question 'is still to be demonstrated' in "
            "2005. Twenty years later it has not been demonstrated either way, and you are "
            "presenting an open question as a closed one whenever the opening runs against "
            "you."),
        survives=3,
        preemptive=(
            "Three, not four: the defence is well aimed but it argues for a live anomaly, and "
            "the cluster's claim is a central Earth, which the anomaly cannot reach. Still, "
            "three concrete things, all now carried in the body. (a) The 'you have no "
            "explanation either' hit must not be answered by pretending we do. Section IV "
            "says the effect is 'real, replicated and not fully explained, and this page says "
            "so without hedging', and section VI leaves the Friday/Fujii exchange open in "
            "terms; both must stay. The answer to the hit is not that we can explain the "
            "coherence but that an unexplained direction and a claimed centre are different "
            "propositions, and the second does not follow from the first — which is stated in "
            "the verdict rather than left implicit. Note too that 'a rotation about an axis is "
            "what we claimed' is a fair hit and must NOT be met with the logical objection "
            "that a direction is not a centre: the geocentrism in this book is a universe "
            "rotating about a fixed Earth, so it does claim an axis, and saying otherwise "
            "misdescribes the source. It is met on the measurements, in IV(a), (c) and (d) — "
            "the axis does not point at the Earth, its direction changes with distance, the "
            "map it is read off is biased by the authors' own observing choices, and the frame "
            "in which it comes out simple is the Local Supercluster's. (b) The hemispheric "
            "mirror symmetry is the defender's cleverest move and an earlier version of this "
            "entry answered it WRONGLY, by claiming a Galactic or local mechanism could "
            "produce it. The paper cited for the fact says the reverse in its own abstract: "
            "these characteristics make the effect 'difficult to explain in terms of local "
            "mechanisms, namely a contamination by interstellar polarization in our Galaxy'. "
            "The same paper reads the mirror symmetry, if it holds, as the signature of a "
            "global rotation about an axis near A1-A3 — nearer the defender's picture than "
            "ours — and hedges it in the body (S2 not totally excluded; slope and constant "
            "coordinate-dependent; a z=0 discontinuity expected from how position angles are "
            "defined). Do not reinstate the deleted line. IV(b) now records those hedges and "
            "the section rests on (a), (c) and (d) instead. "
            "(c) The Monte Carlo objection is pre-answered in the body — spectral similarity "
            "is a SECOND selection criterion applied to the same data, which widens the search "
            "rather than narrowing it, and Varshni's own quoted probability is computed purely "
            "from redshift proximity. Resist adding a claim that the peaked-n(z) run models "
            "the real catalogue: it does not, it is a sensitivity check, and the body says so. "
            "One thing this entry must never do is describe the quasar polarization alignment "
            "as explained or as a known systematic. It is neither."),
    ),

    straw_man=dict(
        identified=True,
        detail=("Two, and the first is ours. OURS: the easy version of this entry would treat the "
                "polarization alignment as a resolved foreground problem and the LQG question as "
                "closed. Neither is true. The 2005 result has been reproduced with an independent "
                "estimator, tested against Planck dust maps and not explained away; the coherence "
                "scale is larger than simulations predict; and the Friday/Fujii disagreement about "
                "whether large quasar groups are physical is unresolved. The verdict here attaches "
                "to the inference from anisotropy to a central Earth, not to the state of that "
                "literature. THEIRS: the source represents working astronomers as evading their "
                "own data. Varshni's 57 groups are said to be known to astronomers as 'the quasar "
                "distribution problem', a phrase presented as the field's own name for a result it "
                "finds awkward; the reference given is to Varshni's paper rather than to anyone "
                "using the phrase. Longo's 2012 quasar-magnitude anomaly is quoted and then "
                "characterised as an author who 'seeks to explain away these anomalies' by "
                "proposing a bubble universe and gravitational lensing - that is what proposing a "
                "physical mechanism looks like, and it is what Hutsemekers, Pelgrims, Nadathur and "
                "Fujii were all doing too. The heaviest instance is NOT the ellipsis dissected in "
                "the gloss - the book names the microwave background in its own voice a page "
                "before the quotation, so a charge of subject-swapping does not hold - but the "
                "use made of the authors: Urban and Zhitnitsky are cited in support of a "
                "conclusion, a central Earth, that their own parity-odd model does not contain, "
                "and their footnoted decision to treat the dipole coincidence as 'mere "
                "coincidence' is not carried across with the quotation."),
    ),

    compression=dict(
        assessed=True, drifted=True,
        list_phrasing=("Quasar distribution symmetry. / Quasar alignment with ecliptic. / "
                       "Quasar polarization alignment. / Large quasar groups ecliptic."),
        source_wording=("“Varshni concludes that if his analysis is correct for quasars, then… The "
                        "Earth is indeed the center of the Universe.” · footnote: “before we accept "
                        "such an unaesthetic possibility, we must raise the question: Are the "
                        "redshifts real? … we have proposed an alternative explanation of the "
                        "spectra of quasars … does not require any redshifts.” · “Urban adds that "
                        "the ‘identifiable preferred axis, the cosmological dipole…point all in the "
                        "same direction, that of the [sun-earth] ecliptic or equinox.’ In other "
                        "words, quasar distribution is centered around the Earth.”"),
        drift_type="hedge_dropped",
        note="""<p><strong>The chain has two links and the enum has one slot, so take the links in order.</strong></p>

<p><strong>Link one, Varshni to the book: a reversal.</strong> <em>Astrophysics and Space Science</em> 43:3&ndash;8 argues that <em>because</em> the cosmological reading of quasar redshifts implies a central Earth, the cosmological reading should be doubted. Varshni&rsquo;s last paragraph declines the geocentric horn as &ldquo;unaesthetic&rdquo; and points at his own laser-star model, which &ldquo;does not require any red shifts&rdquo;. <em>Galileo Was Wrong</em> presents the same result as a discovery about the Earth. That is the largest single move in this cluster, and it is <strong>not</strong> the drift recorded in this field, because this field compares the list against its own source and the reversal happened one link upstream of it.</p>

<p><strong>Link two, the book to the list: the hedge is dropped.</strong> This is what <code>drift_type</code> records. The book&rsquo;s body carries a conditional &mdash; &ldquo;Varshni concludes that <em>if his analysis is correct</em> for quasars, then&hellip;&rdquo; &mdash; and the footnote on p.&nbsp;404 prints Varshni&rsquo;s refusal in his own words. Item&nbsp;90 reads &ldquo;Quasar distribution symmetry.&rdquo; The antecedent, the attribution and the author&rsquo;s stated preference for the other horn all go. The same happens on the alignment items: the source&rsquo;s underlying paper says the aligned regions have <em>different</em> preferred directions at different redshifts, that the map is &ldquo;definitely affected by observational biases&rdquo;, and that whether an axis exists &ldquo;is still to be demonstrated&rdquo;; item&nbsp;321 reads &ldquo;Quasar polarization alignment.&rdquo;</p>

<p><strong>Item 117 is a third thing and the enum has no word for it.</strong> &ldquo;Quasar alignment with ecliptic&rdquo; is faithful to the book&rsquo;s sentence, and the book&rsquo;s sentence has been edited twice over: the ellipsis removes &ldquo;the normal vectors to the planes determined by the quadrupole and the octopole&rdquo;, which is what Urban and Zhitnitsky said points along the ecliptic, and the interpolation &ldquo;[sun-earth]&rdquo; re-describes the ecliptic as an Earth&ndash;Sun structure. What this is <em>not</em> is a subject changed behind the reader&rsquo;s back: a page earlier the book names the microwave background itself, and one axis common to optical, radio and micro is the quoted paper&rsquo;s own thesis. So the drift recorded here is the elision plus the gloss, and the claim underneath it is answered on its merits in section&nbsp;V rather than treated as a misquotation. Recorded here rather than forced into the nearest box, per the standing instruction that the seven values are a convenience and not a theory.</p>

<p><strong>The refutation above answers the source, not the fragment.</strong> It takes Varshni&rsquo;s statistics at the strength he claimed them and refutes the probability calculation on its own terms; it concedes the polarization alignment at the strength the 2005 paper and its independent replications give it, including that it is unexplained; and it leaves the large-quasar-group question open where the literature leaves it open. Item&nbsp;322 was not matched to any sentence in the seventh-edition scan searched, and is recorded as unmapped rather than counted as an unsourced addition.</p>""",
    ),

    verdict_challenge=dict(
        challenged=False, proposed_verdict=None,
        reasoning=("Considered REFUTED and rejected it, for a reason worth recording because the "
                   "cluster is not homogeneous. Item 90 on its own would carry REFUTED without "
                   "difficulty: Varshni's paper argues the opposite of what the item asserts, and "
                   "his probability collapses once the post-hoc box-fitting is undone — 384 "
                   "redshifts drawn at random produce 38-64 groups of the kind he counted 57 of. "
                   "But items 117, 321 and 322 rest on measurements that are real, replicated and "
                   "in part unexplained. The 2005 polarization alignment survived an independent "
                   "estimator at the 0.003% level and survived a Planck-based dust test; whether "
                   "large quasar groups are physical structures is being argued in MNRAS as "
                   "recently as 2024. Calling that literature REFUTED would overstate it, and "
                   "would repeat on our side the error this entry documents on theirs. MISLEADING "
                   "is also the more exact word for what actually happens here: nobody falsified "
                   "data, three of four items report other people's results correctly, and the "
                   "damage is done by the inference and by an ellipsis. Two structural problems "
                   "with the cluster were noted and left alone, since neither is a verdict "
                   "question: the cluster name and cited real sources do not mention Varshni 1976, "
                   "which is item 90's ancestor; and items 90 and 117 rest on unrelated results "
                   "in different geometries — spherical symmetry and a preferred axis — joined "
                   "by nothing but the source's 'in other words', which is arguably grounds for "
                   "a split of the kind pending at A09. They are not, to be clear, formally "
                   "incompatible: the universe this book has rotating about a fixed Earth once a "
                   "day possesses a centre and an axis both, and an earlier draft of this entry "
                   "wrongly asserted that the source's model 'predicts no preferred direction at "
                   "all'. That claim has been withdrawn throughout.")),

    people=["PER-SUNGENIS"],
    related=["E01", "E03", "E12", "E13", "E17", "R01", "A03"],

    sources=[
        dict(label="Sungenis & Bennett, Galileo Was Wrong, 7th ed. 2013 — complete three-volume "
                   "scan; Vol. I ch. 3, Varshni at printed pp. 403–405, the Urban / Hutsemékers / "
                   "Ralston material and the “In other words” sentence at pp. 412–414",
             url="https://archive.org/details/galileo-was-wrong-the-church-was-right-sungenis-vol-1-3-complete"),
        dict(label="Varshni, “The Red Shift Hypothesis for Quasars: Is the Earth the Center of the "
                   "Universe?”, Astrophysics and Space Science 43:3–8 (1976) — the three "
                   "possibilities, the 3 × 10⁻⁸⁵ product, and the closing refusal of the "
                   "geocentric horn in favour of a model that “does not require any red shifts”",
             url="https://articles.adsabs.harvard.edu/pdf/1976Ap%26SS..43....3V"),
        dict(label="Varshni 1976 — publisher record (Springer), title and abstract",
             url="https://link.springer.com/article/10.1007/BF00640549"),
        dict(label="Hutsemékers, Cabanac, Lamy & Sluse, “Mapping extreme-scale alignments of "
                   "quasar polarization vectors”, A&A 441:915 (2005) — 355 quasars, >99.9%, "
                   "different preferred directions by redshift, ~30°/Gpc rotation, the "
                   "observational-bias passage, the supergalactic-frame note, the S2 and "
                   "coordinate-dependence caveats on the mirror symmetry, and footnote 9 giving "
                   "the A1–A3 axis at (lII 267°, bII 69°) against the CMB dipole at (264°, 48°)",
             url="https://arxiv.org/abs/astro-ph/0507274"),
        dict(label="Hutsemékers et al. 2005 — journal record, A&A 441:915–930",
             url="https://www.aanda.org/articles/aa/abs/2005/39/aa3337-05/aa3337-05.html"),
        dict(label="Pelgrims & Cudell, “A new analysis of quasar polarisation alignments”, MNRAS "
                   "442:1239 (2014) — independent estimator, probability “as low as 0.003%”",
             url="https://arxiv.org/abs/1402.4313"),
        dict(label="Hutsemékers, Braibant, Pelgrims & Sluse, “Alignment of quasar polarizations "
                   "with large-scale structures”, A&A 572:A18 (2014) — polarization parallel or "
                   "perpendicular to the host structure; quasar spin axes parallel to their host "
                   "large-scale structures",
             url="https://arxiv.org/abs/1409.6098"),
        dict(label="Pelgrims & Hutsemékers, “Evidence for the alignment of quasar radio "
                   "polarizations with large quasar group axes”, A&A 590:A53 (2016) — independent "
                   "confirmation at radio wavelengths",
             url="https://arxiv.org/abs/1604.03937"),
        dict(label="Pelgrims, “Cosmological-scale coherent orientations of quasar optical "
                   "polarization vectors in the Planck era”, A&A 622:A145 (2019) — dust "
                   "contamination at 2σ for ~30% of sightlines, none detected for the other ~70%",
             url="https://arxiv.org/abs/1709.10271"),
        dict(label="Urban & Zhitnitsky, “The P-Odd Universe, Dark Energy and QCD”, arXiv:1011.2425v2 "
                   "(12 July 2011) — the quasar paragraph in §II.A and the quadrupole/octopole "
                   "ecliptic sentence in §II.C, both on p. 2",
             url="https://arxiv.org/abs/1011.2425"),
        dict(label="Ralston, “Question Isotropy”, arXiv:1011.2240 (2010) — quoted at Galileo Was "
                   "Wrong Vol. I p. 414, including the forecast for Planck polarization",
             url="https://arxiv.org/abs/1011.2240"),
        dict(label="Clowes, Harris, Raghunathan, Campusano, Söchting & Graham, “A structure in the "
                   "early universe at z ~ 1.3 that exceeds the homogeneity scale of the R-W "
                   "concordance cosmology”, MNRAS 429:2910 (2013) — the Huge-LQG",
             url="https://arxiv.org/abs/1211.6256"),
        dict(label="Nadathur, “Seeing patterns in noise: gigaparsec-scale ‘structures’ that do not "
                   "violate homogeneity”, MNRAS 434:398 (2013) — the algorithm finds larger "
                   "clusters in explicitly homogeneous Poisson simulations",
             url="https://arxiv.org/abs/1306.1700"),
        dict(label="Friday, Clowes & Williger, “Correlated orientations of the axes of large quasar "
                   "groups on Gpc scales”, MNRAS 511:4159 (2022) — maximum significance ≃0.8% "
                   "(2.4σ) at ~1.6 Gpc separations",
             url="https://arxiv.org/abs/2201.11474"),
        dict(label="Fujii, “Critical assessment of the recent report on the gigaparsec-scale "
                   "correlation of the orientations of large quasar groups”, MNRAS 527:1982 "
                   "(2024) — “no departure from uniformity”; the LQG sample called “a collection "
                   "of unphysical chance associations”",
             url="https://academic.oup.com/mnras/article/527/2/1982/7337344"),
        dict(label="Lewis & Brewer, “Detection of the cosmological time dilation of high-redshift "
                   "quasars”, Nature Astronomy 7:1265 (2023) — 190 quasars over two decades; "
                   "quasars are “truly cosmologically distant sources”",
             url="https://arxiv.org/abs/2306.04053"),
        dict(label="Lyke et al., “The Sloan Digital Sky Survey Quasar Catalog: Sixteenth Data "
                   "Release”, ApJS 250:8 (2020) — 750,414 quasars, ~99.8% complete",
             url="https://arxiv.org/abs/2007.09001"),
        dict(label="Planck 2018 results VII, “Isotropy and Statistics of the CMB”, A&A 641:A7 "
                   "(2020) — first comprehensive analysis of the polarization statistics; no "
                   "anomalies in polarization corresponding to those in temperature",
             url="https://arxiv.org/abs/1906.02552"),
    ]),
}
