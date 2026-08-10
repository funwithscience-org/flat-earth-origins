# -*- coding: utf-8 -*-
"""
Batch 9 — ARG-E05, "Galaxy spin handedness / hemispheric bias".
3 items (189 "Galaxy spin bias.", 323 "Radio galaxy handedness asymmetry.",
329 "Galaxy spin hemisphere bias."), lane E, verdict REFUTED, originator recorded null.

Research notes for whoever picks this up next. Six things, in order of how much they
change the entry.

1. THE RECORD SAID UNTRACED AND TWO OF THE THREE ITEMS ARE IN SUNGENIS & BENNETT.
   Located in the complete seventh-edition (2013) three-volume Internet Archive scan
   `galileo-was-wrong-the-church-was-right-sungenis-vol-1-3-complete`, Vol. I,
   chapter 3 ("Evidence Earth is in the Center of the Universe"), printed pp. 383-387,
   under the section heading "Correlation between the CMB Axis and Preferred Spin
   Direction of Spiral Galaxies"; a condensed version of the same argument is in a
   footnote at Vol. I p. 448 and again at an earlier footnote in the same volume.
   That is the same chapter ARG-E04 traced the Varshni and Hutsemekers material to
   (pp. 403-405, 412-414) — E04's section sits twenty pages after this one.
   clusters.py was NOT touched; reported up. Fields worth the integrator's attention:
   `originator`/`originator_work`/`year`, all null, and `real_source`, which names
   Longo 2011 and Patel & Desmond 2024 but not Land et al. 2008, Hayes et al. 2017 or
   Iye et al. 2021, all three of which do the load-bearing work.

2. DATING THE ENTRY. Neither "Longo" nor "handed" (beyond "handed over to
   metaphysics" and "singlehandedly") occurs in the OCR text of the 2006 printing —
   Internet Archive item `GallileoWasWrong`, file "Gallileo was wrong_djvu.txt",
   3.3 MB, searched in full and case-insensitively. Longo's first paper is July 2007,
   so the material can only have entered in a later edition. That is a dated boundary
   for when this argument joined the corpus, not a claim about editions between the
   two that were not read.

3. THE PHYSICS HINGE IS A FIGURE CAPTION IN LONGO'S OWN PAPER. Fig. 1(a) of
   arXiv:1104.2815: "A hypothetical universe with all galaxies having the same
   handedness. Note that galaxies in one hemisphere would appear to us to be
   right-handed and in the opposite hemisphere left-handed." A single global
   angular-momentum direction produces the hemispheric flip on ANY observer's sky,
   from anywhere. So the observation Sungenis reads as putting "Earth right in the
   middle" is the one observation his own mechanism makes location-independent. Lead
   with this; the replication history is the second argument, not the first.

4. NUMBERS THAT ARE LOAD-BEARING, ALL RECOMPUTED OR READ OFF THE PAPERS IN SESSION
   (2026-08-09). Longo's best-fit axis (alpha, delta) = (217 deg, 32 deg); the centre
   of the SDSS DR6 northern Galactic cap, printed by Longo two pages earlier, is
   (192, 27). Angular separation 22.3 deg, against Longo's own stated axis uncertainty
   of ~35 deg. Separation from the north ecliptic pole 46.4 deg; from the north
   celestial pole 58.0 deg; from the north Galactic pole 21.5 deg; from Land &
   Magueijo's nominal "axis of evil" at (173, 4) 49.8 deg. Spherical cosine rule,
   four lines of Python, anyone can redo it. These kill the "plane of the equinoxes"
   reading in the source, which needs the axis at or near a pole of the ecliptic or
   the equator.

5. THE HEDGE-DROP IS DOCUMENTED TO THE SENTENCE. The book's footnote quotes
   arXiv:0904.2529 on the Iye & Sugai southern catalogue and stops at "...with a
   preponderance of left-handed spirals". Longo's very next sentence in that preprint
   reads: "This provides an independent confirmation of a spin asymmetry at the 1.6
   sigma level." The footnote as printed in the seventh-edition scan (Vol. I p. 384)
   ends with the arXiv URL in parentheses, so this is a closed quotation rather than
   OCR loss. The same footnote also quotes the "signal exceeding 5 sigma / 2.5e-7"
   line, and that is NOT a dropped qualifier — do not charge it as one. That figure
   comes from the sector analysis over pre-chosen RA ranges and it appears in the
   peer-reviewed PLB paper verbatim ("Overall the asymmetry is -0.0607 +/- 0.0118,
   a 5.15 sigma effect with a probability of 2.5x10^-7 for occurring by chance",
   arXiv:1104.2815 full text, read 2026-08-10). The real contrast is within that one
   paper: the unbinned fit that makes "no a priori assumptions about the direction of
   the dipole axis" gives 7.9e-4, about 3.16 sigma (that conversion is Patel &
   Desmond's, their Table 1). 5.15 -> 3.16 sigma is not a halving.

5b. THE CITATIONS DO NOT RESOLVE TO ONE DOCUMENT, and this is the sharper defect.
   Read off the seventh-edition djvu text (leaf offsets located 2026-08-10): the
   footnote closing on printed p. 383 gives the title, "University of Michigan, 2009"
   and the 0707.3793 URL; the footnote closing on p. 384 quotes the 2009 preprint's
   abstract under the 0707.3793 URL, then says "In a slightly different version of the
   same article" and gives 0904.2529; the footnote printed twice, closing on pp. 240
   and 448, reads "'Evidence for a Preferred Handedness of Spiral Galaxies,' Michael
   Longo, Physics Letters B 10.1016, 2009; http://arxiv.org/ftp/arxiv/papers/0904/
   0904.2529.pdf". Both preprints carry the identical title, so no title distinguishes
   a version; what misleads is the journal name plus truncated DOI plus 2009 on a
   paper that appeared in PLB in 2011 as "Detection of a Dipole in the Handedness of
   Spiral Galaxies with Redshifts z ~ 0.04". Page numbers were fixed by the footer
   digit that closes each page block in the OCR, not by the running head.

6. WHAT IS STILL LIVE, AND SAY SO. The parity question is not closed by decree. Lior
   Shamir has continued to publish the asymmetry in refereed venues through 2024-25
   (PASA 41:e038; the JADES paper arXiv:2502.18781) and has replied in print to Patel
   & Desmond (arXiv:2404.13864). What HAS collapsed is the specific thing the list
   needs. Note also that Shamir's own leading candidate explanation is a Doppler-boost
   selection effect from the Milky Way's rotation, peaking at the Galactic pole
   (JADES paper, sec. 5) — a local artefact of our own Galaxy's motion, which is not
   a friendly result for a stationary Earth. E01's restraint rule applies: represent
   the open part as open.

ITEM 323 HAS NO LOCATED REFERENT. "Radio galaxy handedness asymmetry." was searched
for as a published result and none was identified: arXiv API title/abstract searches
for radio galaxies with parity, handedness and spin-direction terms, the full author
listing for Lior Shamir, and a full-text search of the seventh-edition scan for
"radio galax" (which returns Singal's radio source counts at Vol. I p. 388 and the
Nodland-Ralston birefringence discussion at Vol. II pp. 380-381, neither of which is
a handedness claim, and the second of which is ARG-E13's). Recorded as unlocated
rather than guessed.
"""

ENTRY = {

"E05": dict(

    tldr=("Spiral galaxies really were found to prefer one handedness on one side of the "
          "sky and the other handedness opposite. That pattern is what a single cosmic spin "
          "axis looks like from anywhere — Longo's own Figure 1 makes exactly that point — "
          "so it fixes a direction, not a place, and an observer in any galaxy would see the "
          "same flip across their own sky. The signal has also not held up: it falls to about "
          "3.2σ once Longo stops assuming where the axis is, the opposite-sky half of it is "
          "consistent with zero in his own data, and the four independent checks this page "
          "relies on — Galaxy Zoo 2008, Hayes 2017, Iye 2021 and Patel & Desmond 2024, the "
          "third of which took a rival 4.0σ claim down to 0.29σ by deleting duplicated "
          "galaxies — each came back consistent with isotropy. One research group still "
          "reports the asymmetry, and that exchange is open."),

    passage=dict(
        work="WRK-SUNGENIS-2006",
        pd=False,
        locator=("Vol. I, ch. 3 (“Evidence Earth is in the Center of the Universe”), printed "
                 "p. 386, in the section “Correlation between the CMB Axis and Preferred Spin "
                 "Direction of Spiral Galaxies”, which runs pp. 383–387. Complete seventh-edition "
                 "(2013) three-volume scan at Internet Archive item "
                 "galileo-was-wrong-the-church-was-right-sungenis-vol-1-3-complete; page numbers "
                 "read off the printed footers in the OCR text, not checked against a print copy"),
        quote=("There are other astounding facts in Longo's data that puts Earth right in the "
               "middle of the spin axis … It is due to the Coriolis force, only this Coriolis "
               "force is not merely local. It is a universal Coriolis force caused by the "
               "rotation and oscillation of the universe around the Earth."),
        gloss="""<p><strong>What the underlying paper is.</strong> Michael J. Longo, then at the University of Michigan, classified spiral galaxies from the Sloan Digital Sky Survey by winding direction and looked for a preferred handedness. Three versions matter: arXiv:0707.3793 (2007, 2,616 galaxies, axis near &alpha;&nbsp;202&deg;, &delta;&nbsp;25&deg;), arXiv:0904.2529 (2009, 15,158 galaxies), and the peer-reviewed paper, <em>Phys. Lett. B</em> 699 (2011) 224&ndash;229. The book&rsquo;s citations do not resolve to one document. Both preprints carry the same title, so the titles do not distinguish them; what the footnotes do is mix the versions. The footnote on p.&nbsp;384 quotes the 2009 preprint&rsquo;s abstract (&ldquo;The new study uses 15,158 with redshifts &lt;0.085&hellip; a signal exceeding 5&sigma;&rdquo;) under a URL for the 2007 preprint, then introduces the next quotation as coming from &ldquo;a slightly different version of the same article&rdquo; and gives the 2009 URL. The footnote printed twice, at pp.&nbsp;240 and 448, attaches the preprint title, a truncated DOI (&ldquo;<em>Physics Letters B</em> 10.1016&rdquo;) and the year 2009 to a link that resolves to the 2009 preprint PDF &mdash; while the <em>Physics Letters B</em> paper itself appeared in 2011 under a different title, &ldquo;Detection of a Dipole in the Handedness of Spiral Galaxies with Redshifts <em>z</em>&nbsp;~&nbsp;0.04&rdquo;. A reader following either citation lands on a preprint, not on the journal article named.</p>

<p><strong>The two pages either side of this quotation are the ones to read.</strong> On p.&nbsp;385 the book reproduces, in full and without cutting it, Anil Ananthaswamy&rsquo;s <em>New Scientist</em> answer to precisely the inference it is about to draw: &ldquo;<em>Let&rsquo;s start with what that does not mean: Earth is not in a special place</em>&hellip; the original spin axis has expanded with it, so wherever you are in the cosmos, it will be there too, pointing in the same direction.&rdquo; The book calls this &ldquo;specious&rdquo; and answers that a universal axis is &ldquo;universal, not local&rdquo; &mdash; which concedes the point rather than rebutting it. On p.&nbsp;387 it prints Ray Villard asking whether the result &ldquo;might just be a statistical fluke&rdquo; or is &ldquo;somehow biased because we are only looking at the local universe&rdquo;, and observing that &ldquo;the Milky Way&rsquo;s own spin axis roughly aligns to the universe&rsquo;s purported spin axis within just a few degrees.&rdquo; The systematic-origin diagnosis and the Copernican answer are both inside the source, quoted approvingly enough to be reproduced at length, and then set aside.</p>

<p><strong>Where the qualifier goes.</strong> The book&rsquo;s footnote at p.&nbsp;384 quotes Longo&rsquo;s comparison with the Iye &amp; Sugai 1991 southern catalogue and closes with the arXiv URL immediately after &ldquo;with a preponderance of left-handed spirals&rdquo;. Longo&rsquo;s next sentence, in the same paragraph of the same preprint, is: &ldquo;This provides an independent confirmation of a spin asymmetry at the 1.6&sigma; level.&rdquo; The same footnote also carries the preprint&rsquo;s &ldquo;signal exceeding 5&sigma;&rdquo;, and that figure is <em>not</em> a casualty: it is the result of the sector analysis over right-ascension ranges fixed in advance, and it survives into the peer-reviewed paper, which states an overall asymmetry of &minus;0.0607&nbsp;&plusmn;&nbsp;0.0118, &ldquo;a 5.15&sigma; effect with a probability of 2.5&times;10<sup>&minus;7</sup> for occurring by chance.&rdquo; The contrast that is real runs inside that one paper: the unbinned dipole fit, for which &ldquo;no <em>a priori</em> assumptions about the direction of the dipole axis or its magnitude were made&rdquo;, gives 7.9&nbsp;&times;&nbsp;10<sup>&minus;4</sup>, about 3.2&sigma;.</p>

<p><strong>On the work record.</strong> Our cluster record for E05 carries no originator, no work and no year. Two of its three items have a documented ancestor in the pages above. Neither &ldquo;Longo&rdquo; nor &ldquo;handed&rdquo; is located in the OCR text of the 2006 printing (Internet Archive item <code>GallileoWasWrong</code>, file &ldquo;Gallileo was wrong_djvu.txt&rdquo;, 3.3&nbsp;MB, searched in full), and Longo&rsquo;s first paper is July 2007, so the material entered in a later edition. <code>clusters.py</code> is owned by the integrator and was not edited from here; the finding is reported rather than applied.</p>""",
    ),

    steelman=dict(
        description="""<p><strong>SURFACE (weak &mdash; do not use).</strong> &ldquo;Which way a spiral looks like it winds just depends on which side you view it from, so the whole measurement is meaningless.&rdquo; This loses immediately. Longo&rsquo;s handedness is a well-defined observable: spiral arms trail, so the apparent winding fixes the sign of the line-of-sight component of the spin vector, and Iye, Yagi &amp; Fukumoto devoted an entire paper (<em>Spin Parity of Spiral Galaxies I</em>, 2019) to confirming that relationship against 146 galaxies with independent distance and velocity information. Equally weak: &ldquo;it was just human bias.&rdquo; Longo randomly mirrored half his images before displaying them to his five scanners, with no visual cue, which symmetrises any human effect &mdash; including the <em>selection</em> effect that Hayes, Davis &amp; Silva later showed was the real problem with Galaxy Zoo 1.</p>

<p><strong>DEEPER.</strong> The question is a legitimate one and was not invented by geocentrists. Parity is violated in the weak interaction; biology runs on one chirality of amino acid; asking whether the largest scales carry a handedness is a reasonable thing for a physicist to do, and Longo says so in his first paragraph. His paper is careful in ways that are easy to miss: the scanners worked in randomised order with respect to right ascension, declination and redshift, so no scanning drift could imprint a position-dependent bias; he bounded the overall left/right bias at &minus;0.0077&nbsp;&plusmn;&nbsp;0.0062; he computed his significance numerically rather than assuming a &chi;<sup>2</sup> distribution the data cannot have; and he calculated the look-elsewhere penalty by re-running 4&nbsp;&times;&nbsp;10<sup>5</sup> randomised samples over 100 candidate axes. That is better practice than most of what gets called an anomaly.</p>

<p><strong>KERNEL.</strong> The strongest form of the argument is not &ldquo;a signal was found&rdquo; but the coincidence structure that ARG-E01 runs on, applied here: a preferred handedness axis would be a genuinely non-Copernican fact about the universe, and if it landed on the <em>same</em> direction as the microwave background&rsquo;s low-multipole alignments and the quasar polarization axis, then a set of mutually independent probes would be picking out one direction tied to our own orbital plane. Longo himself reaches for this &mdash; his abstract says the axis is &ldquo;close to alignments observed in the WMAP&rdquo; maps, and his conclusion offers the spin result as &ldquo;a unique and completely independent confirmation that the AE is not an artifact in the WMAP data due to foreground contamination.&rdquo; Concede all of that: the measurement is real, the control for human bias is the right one, and the concurrence-of-axes argument is the serious version.</p>""",
        why_it_doesnt_save_claim="""<p><strong>Because a handedness dipole is a direction, and this particular direction does not join the set.</strong> Take the alignment claim first, since it is the one that would do the work. Longo&rsquo;s published best-fit axis is (&alpha;,&nbsp;&delta;)&nbsp;=&nbsp;(217&deg;, 32&deg;). Recomputed here by spherical cosine rule, that sits 21.5&deg; from the north Galactic pole, 22.3&deg; from the centre of the SDSS DR6 northern Galactic cap &mdash; a figure Longo prints himself, (192&deg;, 27&deg;) &mdash; 46.4&deg; from the north ecliptic pole, 49.8&deg; from Land &amp; Magueijo&rsquo;s nominal &ldquo;axis of evil&rdquo; at (173&deg;, 4&deg;), and 58.0&deg; from the north celestial pole. Longo states the uncertainty on the axis direction as roughly 35&deg;. So the two things this axis is nearest are the spin axis of our own Galaxy and the middle of the patch of sky the survey happened to cover, and it is <em>further</em> from the ecliptic pole and the microwave axis than it is from either. The concurrence argument needs this axis to be in the ecliptic frame; it is not.</p>

<p><strong>And the hemispheric flip is a projection, not a location.</strong> This is settled inside the source&rsquo;s own citation. The caption to Fig.&nbsp;1(a) of the PLB paper reads: &ldquo;A hypothetical universe with all galaxies having the same handedness. Note that galaxies in one hemisphere would appear to us to be right-handed and in the opposite hemisphere left-handed.&rdquo; One global angular-momentum direction, no centre anywhere, and every observer sees left-handed spirals on one side of their sky and right-handed on the other, divided by the great circle perpendicular to the axis. That great circle passes through the observer for the same reason every great circle on your own sky does. Nothing about the pattern distinguishes one vantage point from another, which is exactly what Ananthaswamy told the book&rsquo;s authors and what they printed on p.&nbsp;385 before declining it.</p>""",
    ),

    refutation="""<p><strong>First, what was measured, stated at full strength.</strong> Longo classified 15,158 SDSS spirals by winding direction and fitted an unbinned dipole with no assumed axis. He got an amplitude of &minus;0.0408&nbsp;&plusmn;&nbsp;0.011 and a chance probability of 7.9&nbsp;&times;&nbsp;10<sup>&minus;4</sup>, about 3.2&sigma;. His scanners saw randomly mirrored images, so a human preference for one winding could not imprint a direction on the sky; he bounded that overall bias at &minus;0.0077&nbsp;&plusmn;&nbsp;0.0062. This is a real measurement, competently done, published in <em>Physics Letters B</em>, and never retracted. Anyone answering it by saying spiral handedness is not an observable, or that Longo forgot about human bias, is wrong on both counts.</p>

<p><strong>Second, the geometry, which decides the geocentric question on its own.</strong> Suppose the signal is exactly as advertised. What has been detected is a <em>vector</em>: a direction in space along which galactic angular momenta preferentially point. Longo's own Figure&nbsp;1(a) draws the consequence and captions it &mdash; a universe in which every galaxy spins the same way &ldquo;would appear to us to be right-handed&rdquo; in one hemisphere of the sky and left-handed in the other. That appearance is produced by nothing but line of sight. It arises for an observer in the Milky Way, for an observer in Andromeda, and for an observer in a galaxy at the edge of the survey volume, and the dividing great circle runs through each of them because a great circle on your own celestial sphere always does. &ldquo;The bias is centred on us&rdquo; is a statement about spherical coordinates, not about the universe. It is the same error ARG-E01 catches on the microwave axis and ARG-E04 catches on the quasar polarizations, and here the paper being cited prints the refutation as a figure caption.</p>

<p><strong>Third, the mechanism the source proposes defeats the conclusion the source draws.</strong> <em>Galileo Was Wrong</em> does not leave the pattern uninterpreted. It says the northern sky&rsquo;s left-handed excess and the southern sky&rsquo;s right-handed excess are &ldquo;the same phenomena we experience with hurricanes&rdquo;, produced by &ldquo;a universal Coriolis force caused by the rotation and oscillation of the universe around the Earth.&rdquo; Take that seriously for a moment, because it is checkable. Hurricanes reverse across the equator because what steers horizontal flow on the surface of a rotating sphere is the <em>local vertical</em> component of the rotation vector, <em>f</em>&nbsp;=&nbsp;2&Omega;&nbsp;sin&nbsp;&phi;, and that changes sign at the equator. Galaxies are not confined to a surface and have no latitude, so there is no analogue of <em>f</em>. A rigidly rotating universe has velocity field <strong>v</strong>&nbsp;=&nbsp;<strong>&Omega;</strong>&nbsp;&times;&nbsp;<strong>r</strong> and therefore uniform vorticity 2<strong>&Omega;</strong> everywhere in it: it would torque collapsing gas the <em>same</em> way at every location, producing a monopole in true spin direction, not a dipole. The book says as much elsewhere on the page &mdash; &ldquo;the universe spins around its center of mass in only one direction&rdquo;. But a monopole in true spin is precisely the universe of Longo&rsquo;s Figure&nbsp;1(a), and Figure&nbsp;1(a) is location-independent. The proposed dynamics reproduce the observation and erase the centrality claim in the same step.</p>

<p><strong>Fourth, the alignment claim, in numbers.</strong> The book states that the preferred spin direction is &ldquo;centered on the Earth&rsquo;s equinoxes (just as the CMB dipole&hellip;)&rdquo; and &ldquo;differentiated by the plane of the equinoxes&rdquo;, and that &ldquo;Longo&rsquo;s axis is inclined 23.5&deg; to the axis around which the universe itself rotates&rdquo; &mdash; i.e. that it is the pole of the ecliptic, one obliquity away from the celestial pole. The plane that divides the two handedness hemispheres is the plane perpendicular to the dipole axis, so this is arithmetic. With Longo&rsquo;s published axis at (&alpha;,&nbsp;&delta;)&nbsp;=&nbsp;(217&deg;,&nbsp;32&deg;), that dividing plane is inclined 58.0&deg; to the celestial equator and 46.4&deg; to the ecliptic. Neither is the plane of the equinoxes on either reading of the phrase, and 23.5&deg; is not the separation from anything here. What the axis <em>is</em> near is the north Galactic pole (21.5&deg;) and the centre of the SDSS DR6 footprint at (192&deg;,&nbsp;27&deg;) (22.3&deg;), which Longo prints on the page before he fits the dipole. Given his stated axis uncertainty of about 35&deg;, &ldquo;the axis of the universe&rdquo; and &ldquo;the middle of the region I looked at&rdquo; are not separated by this measurement.</p>

<p><strong>Fifth, the hemispheric half of the claim is the weakest half, and Longo says so.</strong> Item 329 is specifically about the two hemispheres carrying opposite signs. In Longo&rsquo;s own SDSS data the sector opposite the signal contains 985 galaxies against 6,212 in the signal sector, and its asymmetry is 0.005&nbsp;&plusmn;&nbsp;0.032 &mdash; consistent with zero, and reported as such in his Table&nbsp;I. The complementary excess therefore does not come from his survey at all; it comes from his re-analysis of Iye &amp; Sugai&rsquo;s 1991 photographic southern catalogue, which gives +0.047&nbsp;&plusmn;&nbsp;0.029, and Longo describes that in the next sentence as &ldquo;independent confirmation of a spin asymmetry at the 1.6&sigma; level.&rdquo; The book quotes the sentence before that one and stops. The popular account it then reproduces upgrades a 1.6&sigma; result to &ldquo;a clear excess this time of right-handed spirals&hellip; the same effect, only in reverse.&rdquo;</p>

<p><strong>Sixth, the replication record, which is where this argument actually ends.</strong> Four independent efforts, none of them run by anyone with a stake in geocentrism, and they converge:</p>
<ul>
<li><strong>Galaxy Zoo (Land et al., <em>MNRAS</em> 388:1686, 2008).</strong> About 37,000 SDSS spirals classified by more than 100,000 volunteers. A large left/right bias was found in the raw votes, measured with a mirrored-image study, and corrected; after correction the winding sense is &ldquo;consistent with statistical isotropy&hellip; no significant dipole signal.&rdquo; Their dipole is about 2&sigma; before a monopole term is allowed and about 1&sigma; after.</li>
<li><strong>Hayes, Davis &amp; Silva (<em>MNRAS</em> 466:3928, 2017).</strong> Diagnosed the Galaxy Zoo 1 bias as a <em>selection</em> effect rather than a chirality-labelling effect &mdash; S-wise votes were being taken from the elliptical and edge-on categories &mdash; and showed it disappears when a provably unbiased machine chooses which objects count as spirals. That is a mechanism, not a shrug.</li>
<li><strong>Iye, Yagi &amp; Fukumoto (<em>ApJ</em> 907:123, 2021).</strong> Reproduced the 4.00&sigma; dipole in Shamir&rsquo;s 2017 SDSS catalogue, then found the catalogue contained large numbers of duplicated galaxies. Removing them left 45% of the sample and a dipole of <strong>0.29&sigma;</strong>. A headline result that survives only while the same objects are counted more than once is not a result.</li>
<li><strong>Patel &amp; Desmond (<em>MNRAS</em> 534:1553, 2024).</strong> Pooled every publicly available spin-classified dataset, <em>including Longo&rsquo;s own 15,158 galaxies</em>, and analysed them both Bayesian and frequentist without assuming Gaussianity. Everything is consistent with isotropy within 3&sigma;. On Longo specifically: when monopole and dipole are inferred jointly rather than separately, &ldquo;both Longo anomalies disappear&rdquo; &mdash; which is the degeneracy Land et al. had warned about in 2008, and which is exactly what an overall labelling or selection bias confined to a partial-sky footprint would produce. Splitting Longo&rsquo;s galaxies into three equal redshift bins gives the same null in each. Their code is public.</li>
</ul>
<p>To that can be added <em>Spin Parity of Spiral Galaxies VI</em> (2026), which annotated 49,494 HSC spirals with spectroscopic redshifts and tested 46,247 search volumes from 20 to 200&nbsp;Mpc: the S/Z imbalances follow the binomial expectation and the number of anomalous volumes matches what random assignment predicts.</p>

<p><strong>Seventh, what is still open, because it is and the page should say so.</strong> One research programme continues to report the asymmetry. Lior Shamir has published it from SDSS, Pan-STARRS, DES, HST, HSC and JWST deep fields, in refereed venues through 2024&ndash;25, and has replied in print to Patel &amp; Desmond, arguing their statistic is insufficiently responsive to a real asymmetry. That exchange is unresolved and this page is not adjudicating it. Two things about it are worth a reader&rsquo;s attention anyway. The claimed asymmetry is now generally reported as being relative to <em>the Milky Way&rsquo;s</em> rotation as seen from Earth, and Shamir&rsquo;s own leading candidate explanation is a Doppler-brightening selection effect: galaxies rotating counter to our Galaxy are slightly brighter, so slightly more of them get detected, and the effect &ldquo;should peak at around the Galactic pole&rdquo; &mdash; which is where the claimed axis has sat since 2007. He notes in the same passage that the naive size of that effect is too small for what he measures. Whichever way that goes, both horns are about our own Galaxy&rsquo;s rotation and our own instruments: a signal produced by the Milky Way&rsquo;s spin is not a signal produced by the Earth&rsquo;s centrality, and it requires the observer to be moving.</p>

<p><strong>Verdict: refuted.</strong> Not because the measurement was fabricated &mdash; it was not &mdash; but because the inference fails twice over. Even at full strength the observable is an axis, and an axis fixes a direction that every observer in the universe shares; the source&rsquo;s own citation says this in a figure caption and the source prints and dismisses the same point from a science journalist two pages earlier. And the measurement is not at full strength: the significance drops from the 5.15&sigma; of the pre-chosen sectors to about 3.2&sigma; once the axis is not assumed, the opposite-hemisphere half is consistent with zero in the originating dataset, the axis sits nearer the survey&rsquo;s own footprint than to any cosmic landmark, and every re-analysis listed above has gone one way &mdash; with the exchange described in section seven still open.</p>""",

    advocate=dict(
        best_defense=(
            "You have picked the weakest version of our argument and beaten it. We do not "
            "claim that a single axis proves a centre — of course a vector looks the same "
            "from everywhere, and we printed Ananthaswamy saying so, which you might have "
            "read as candour rather than as a slip. The claim is the concurrence. The "
            "microwave quadrupole and octopole align with each other, with the dipole and "
            "with the equinoxes; the quasar polarizations pick out an axis; the galaxy spins "
            "pick out an axis; Longo says in print that his result is 'a unique and completely "
            "independent confirmation that the AE is not an artifact in the WMAP data.' You "
            "answer that with an arithmetic exercise on one axis and a stated uncertainty of "
            "35 degrees — an uncertainty large enough that your 46 degrees to the ecliptic "
            "pole is barely more than one standard deviation, so you have shown nothing "
            "except that this measurement cannot locate an axis precisely, which we already "
            "knew. Second: your replication paragraph is a list of papers that assumed "
            "isotropy and found it. Iye deleted duplicates from someone else's catalogue, not "
            "Longo's. Patel and Desmond invented a statistic for the occasion, and Shamir has "
            "published a response showing it does not detect a dipole even when one is "
            "injected — you cite the response and then decline to weigh it. Third, and this "
            "is the one that should worry you: you concede that the leading proponent now "
            "traces the effect to a preferred direction fixed by the Milky Way's rotation and "
            "peaking at the Galactic pole. A cosmological-scale observable whose axis is set "
            "by the observer's own galaxy is precisely the kind of thing our tradition has "
            "been pointing at for fifty years. You have relabelled it and called it a "
            "refutation."),
        survives=4,
        preemptive=(
            "Four, and the number is driven by the first and third moves, not the second. "
            "Three concrete changes, in order. (a) The concurrence argument must be answered "
            "in the body rather than deferred to E01, and the answer has to be the specific "
            "one: this axis is not in the ecliptic frame at all. Section four already carries "
            "the numbers; what it must also carry — and now does — is the comparison that "
            "makes them mean something, namely that the axis is nearer the Galactic pole "
            "(21.5 degrees) and the SDSS footprint centre (22.3 degrees) than the ecliptic "
            "pole (46.4) or the microwave axis (49.8). With a 35-degree uncertainty the "
            "honest statement is that this measurement cannot place an axis, which is fatal "
            "to a claim that it lands on the equinoxes, and that is how section four is "
            "written. Do not let an editor compress it into 'the axis is 46 degrees off', "
            "which invites exactly the one-sigma reply. (b) On replication, drop any "
            "temptation to present the literature as unanimous. The Iye result is about "
            "Shamir's catalogue and the text must say so — it does — and the load-bearing "
            "result against Longo specifically is Patel & Desmond's joint monopole-dipole "
            "inference, which is Land et al.'s 2008 point applied to Longo's own galaxies. "
            "State that pairing explicitly; it is the only place in the section where "
            "Longo's data are the subject. (c) On the Milky Way point, resist the trade the "
            "defender is offering. Say plainly what section seven says: an axis set by our "
            "own Galaxy's rotation is a claim about a moving observer inside a rotating disc, "
            "and it is the opposite of a stationary Earth at a centre. If that explanation is "
            "right the list loses; if it is wrong the asymmetry is unexplained and still "
            "carries no location. Finally, on tone: 'we printed Ananthaswamy saying so' is a "
            "fair hit and should be conceded as one. The gloss credits the book with "
            "reproducing the objection at length; the criticism is not that it hid the answer "
            "but that it answered 'the spin axis is universal, not local' and did not notice "
            "that this is the objection."),
    ),

    straw_man=dict(
        identified=True,
        detail=("Two moves. The book explains the New Scientist rebuttal by motive rather than "
                "by argument — that Ananthaswamy 'feels he must make such a preemptive argument "
                "shows that he and his colleagues are very concerned about the geocentric "
                "interpretation', and that he is 'quick to stifle the geocentric implications'. "
                "The article's actual content is a two-sentence statement of how a global vector "
                "projects onto any observer's sky, which is standard geometry and was not written "
                "with geocentrism in view. Second, it presents Longo and the science press as "
                "having missed the meaning of their own data — 'both Longo and New Scientist miss "
                "the meaning of this asymmetry' — where Longo's paper had already drawn the "
                "hemispheric flip as a figure and captioned it as the expected appearance of a "
                "single global handedness. Nobody in the literature holds that a preferred "
                "cosmic axis would be evidence against a preferred cosmic axis; the position "
                "being answered is that a preferred axis does not pick out a preferred place, "
                "and that position is not addressed."),
    ),

    compression=dict(
        assessed=True, drifted=True,
        list_phrasing=("Three items: “Galaxy spin bias.” · “Radio galaxy handedness asymmetry.” · "
                       "“Galaxy spin hemisphere bias.”"),
        source_wording=("&ldquo;galaxies have a preferred left-handed spin to an excess of 7%, which "
                        "then translates into a preferred axis and a residual angular momentum for "
                        "the whole universe&rdquo; (Vol. I, p. 448 n.) &middot; &ldquo;The fact that "
                        "the northern hemisphere of the whole universe has most of its galaxies "
                        "spinning left, and the southern hemisphere of the whole universe has most of "
                        "its galaxies spinning right, is the same phenomena we experience with "
                        "hurricanes&hellip; It is a universal Coriolis force caused by the rotation "
                        "and oscillation of the universe around the Earth&rdquo; (Vol. I, p. 386) "
                        "&middot; the underlying paper: &ldquo;<em>A preference for spiral galaxies "
                        "in one sector of the sky to be left-handed or right-handed spirals "
                        "would indicate a parity violating asymmetry</em>&rdquo; (Longo, PLB 699:224)"),
        drift_type="hedge_dropped",
        note="""<p><strong>The chain has three links here, not two, and the enum has one slot.</strong> Take them in order, because the drift is a different size at each.</p>

<p><strong>Link one, Longo to the book: qualifiers removed at the sentence level.</strong> This is what <code>drift_type</code> records, and it is documented to the line. The book&rsquo;s footnote at Vol. I p.&nbsp;384 quotes Longo on the Iye &amp; Sugai southern catalogue and closes with the arXiv URL directly after &ldquo;with a preponderance of left-handed spirals&rdquo;; Longo&rsquo;s next sentence in that preprint reads &ldquo;This provides an independent confirmation of a spin asymmetry at the <strong>1.6&sigma;</strong> level.&rdquo; (The &ldquo;signal exceeding 5&sigma;&rdquo; that the same footnote quotes is <em>not</em> part of this: that is the number from the sector analysis over pre-chosen right-ascension ranges, and it appears in the peer-reviewed paper too, at 5.15&sigma;. The book dropped no qualifier there, and the drift finding does not rest on it.) And Longo&rsquo;s abstract states the finding as a conditional &mdash; a preference &ldquo;<em>would indicate</em>&rdquo; a parity-violating asymmetry &mdash; where the book reports it as a discovery about the Earth&rsquo;s position. <code>scope_widened</code> has an equal claim on this link: Longo&rsquo;s result is about SDSS DR6 spirals below <em>z</em>&nbsp;=&nbsp;0.085 in one sector of one Galactic cap, with an axis good to about 35&deg;, and it arrives as a fact about the two hemispheres of the universe.</p>

<p><strong>Link two, the popular press to the book.</strong> Between the paper and the book sits <em>New Scientist</em>, and the amplification is visible in the book&rsquo;s own quotation marks: the southern result Longo scores at 1.6&sigma; appears as &ldquo;a clear excess this time of right-handed spirals&hellip; the same effect, only in reverse.&rdquo; The book is quoting accurately; it is the intermediary that hardened the claim. This is the ordinary mechanism the project keeps finding, and it is worth naming as such rather than charging it to the book.</p>

<p><strong>Link three, the book to the list: not a hardening.</strong> &ldquo;Galaxy spin bias.&rdquo; and &ldquo;Galaxy spin hemisphere bias.&rdquo; claim considerably <em>less</em> than the pages they descend from, which assert a universal Coriolis force generated by a universe rotating about the Earth. The two lines are bare labels. What changes is the speech act, not the content: a label sits under a numbered heading in a document offered as evidence that the Earth is not a spinning ball, and it arrives with the geocentric machinery stripped off and therefore with nothing for a reader to check. Compare <a href="#ARG-E03">ARG-E03</a>, where the same understating happens on the same shelf and is recorded as <code>drifted=False</code>; here the upstream drop is large enough that the entry is scored on link one.</p>

<p><strong>Item 323 is a fourth thing and the enum has no word for it either.</strong> &ldquo;Radio galaxy handedness asymmetry.&rdquo; was searched for as a published result and none was identified: arXiv title-and-abstract queries pairing radio galaxies with parity, handedness and spin-direction terms; the complete arXiv author listing for Lior Shamir, who wrote most of this literature; and a full-text search of the seventh-edition scan for &ldquo;radio galax&rdquo;, which returns Singal&rsquo;s radio source counts (Vol. I, p.&nbsp;388) and the Nodland&ndash;Ralston polarization-rotation discussion (Vol. II, pp.&nbsp;380&ndash;381) &mdash; the second of which belongs to <a href="#ARG-E13">ARG-E13</a> and neither of which is a handedness claim. On the searches run, that item names no result. It is recorded as unlocated rather than assigned to the nearest paper that would fit, which is the move this project exists to document.</p>

<p><strong>And the finding that outranks the drift.</strong> Our cluster record carries no originator, no work and no year for E05. Two of its three items have a documented ancestor: <em>Galileo Was Wrong</em>, seventh edition, Vol. I, pp.&nbsp;383&ndash;387, in the same chapter that <a href="#ARG-E04">ARG-E04</a> and <a href="#ARG-E13">ARG-E13</a> were traced into. Three of the thirty clusters recorded as untraced have now been audited and all three came back with a source, so the untraced count should still be read as an upper bound in one direction only.</p>""",
    ),

    verdict_challenge=dict(challenged=False, proposed_verdict=None, reasoning=None),

    people=["PER-SUNGENIS"],
    related=["E01", "E02", "E03", "E04", "E06", "E13", "E17", "R01", "R06"],

    sources=[
        dict(label="Longo, “Detection of a dipole in the handedness of spiral galaxies with "
                   "redshifts z ~ 0.04”, Phys. Lett. B 699 (2011) 224–229 — the dipole "
                   "−0.0408 ± 0.011 at P = 7.9 × 10⁻⁴, the axis at (217°, 32°), the ~35° axis "
                   "uncertainty, the Fig. 1(a) caption, and Table I's 0.005 ± 0.032 for the "
                   "opposite sector",
             url="https://arxiv.org/abs/1104.2815"),
        dict(label="Longo, “Evidence for a Preferred Handedness of Spiral Galaxies” "
                   "(arXiv:0904.2529, 2009) — the version the book quotes; “independent "
                   "confirmation of a spin asymmetry at the 1.6σ level” is the sentence "
                   "immediately after the quotation ends",
             url="https://arxiv.org/abs/0904.2529"),
        dict(label="Longo, “Evidence for a Preferred Handedness of Spiral Galaxies” "
                   "(arXiv:0707.3793, 2007) — the first study, 2,616 galaxies, axis near "
                   "(202°, 25°)",
             url="https://arxiv.org/abs/0707.3793"),
        dict(label="Sungenis & Bennett, Galileo Was Wrong, 7th ed. (2013), Vol. I, ch. 3, "
                   "pp. 383–387 — the “universal Coriolis force” passage at p. 386, the "
                   "New Scientist rebuttal reproduced and declined at p. 385, Villard's "
                   "“statistical fluke” caveat at p. 387",
             url="https://archive.org/details/galileo-was-wrong-the-church-was-right-sungenis-vol-1-3-complete"),
        dict(label="Land et al. (Galaxy Zoo), “The large-scale spin statistics of spiral "
                   "galaxies in the SDSS”, MNRAS 388:1686 (2008) — ~37,000 spirals; after "
                   "correcting a measured classification bias, “consistent with statistical "
                   "isotropy… no significant dipole signal”",
             url="https://arxiv.org/abs/0803.3247"),
        dict(label="Hayes, Davis & Silva, “On the nature and correction of the spurious S-wise "
                   "spiral galaxy winding bias in Galaxy Zoo 1”, MNRAS 466:3928 (2017) — the "
                   "bias is a selection effect, not a chirality-labelling effect",
             url="https://arxiv.org/abs/1610.07060"),
        dict(label="Iye, Yagi & Fukumoto, “Spin Parity of Spiral Galaxies III”, ApJ 907:123 "
                   "(2021) — σ_D = 4.00 in Shamir's 2017 SDSS catalogue falls to σ_D = 0.29 "
                   "once duplicated entries are removed",
             url="https://arxiv.org/abs/2011.00662"),
        dict(label="Patel & Desmond, “No evidence for anisotropy in galaxy spin directions”, "
                   "MNRAS 534:1553 (2024) — pools all public spin catalogues including Longo's "
                   "15,158 galaxies; “when inferring both M and D, both Longo anomalies "
                   "disappear”; code public",
             url="https://arxiv.org/abs/2404.06617"),
        dict(label="Patel & Desmond, “Symmetry in Hyper Suprime-Cam Galaxy Spin Directions”, "
                   "RNAAS 8:281 (2024) — Bayes factor gives decisive evidence for the isotropic "
                   "model",
             url="https://arxiv.org/abs/2410.18884"),
        dict(label="Shamir, “Reproducible empirical evidence of cosmological-scale asymmetry in "
                   "galaxy spin directions” (arXiv:2404.13864, 2024) — the reply to Patel & "
                   "Desmond; the exchange is unresolved and is cited here as such",
             url="https://arxiv.org/abs/2404.13864"),
        dict(label="Shamir, “The distribution of galaxy rotation in JWST Advanced Deep "
                   "Extragalactic Survey” (arXiv:2502.18781) — the Doppler-brightening "
                   "explanation, which “should peak at around the Galactic pole”, together "
                   "with the author's own objection that the effect is too small",
             url="https://arxiv.org/abs/2502.18781"),
        dict(label="Iye et al., “Spin Parity of Spiral Galaxies VI” (arXiv:2605.05570, 2026) — "
                   "49,494 HSC spirals over 46,247 search volumes, consistent with statistical "
                   "randomness",
             url="https://arxiv.org/abs/2605.05570"),
    ]),
}
