# -*- coding: utf-8 -*-
"""Batch 9 — E14. "Solar anomalies (oblateness, neutrinos, apex, barycentre wobble)."

Research notes for whoever picks this up next.

0. THE FIVE ITEMS. assign.py puts items 104, 138, 192, 195 and 361 in E14:

     104  "Solar inertial wobble about Earth."
     138  "Solar apex inconsistency."
     192  "Solar neutrino problem."
     195  "Solar oblateness constancy."
     361  "Sun barycenter wobble epicyclic."

   Five topics, four of them unrelated to each other. Treat it as a bundle, because
   the list treats it as a bundle; do not let the bundling hide that only one of the
   five is a live question in 2026.

1. THE RECORD SAYS UNTRACED. IT SURVIVES ONLY PARTLY. clusters.py has
   originator=None, originator_work=None, year=None, real_source=None. I pulled the
   full OCR text of Galileo Was Wrong Vol. I (Internet Archive item GallileoWasWrong,
   file "Gallileo was wrong_djvu.txt", ~3.3 MB, the CD edition of the 2006 Vol. I) and
   word-searched it. Four of the five items have a matching argument in that volume,
   at these printed page numbers as they appear in the OCR:

     195 oblateness  -> Appendix 5, printed pp. 1003-1004 (Dicke & Goldenberg, the
                       "39.6 not 43.0" residual, Roxburgh's fast core, Hill, Dicke's
                       own 1985 revision to 12 ppm, Clifford Will's "open question")
     138 apex        -> Chapter 12 Conclusion, printed p. 959 ("The sun is actually
                       traveling in a direction toward Hercules ... This is about 32
                       degrees away from an orbital path in the Milky Way!")
     104/361 wobble  -> Chapter 4, printed pp. 198-199 (Hoyle's centre-of-mass passage
                       and Sungenis's inference), extended at Chapter 10, pp. 598-603
                       ("the immovable barycenter of the universe")

   192 (neutrinos) did NOT come back that way. "neutrino" occurs eight times in the
   Vol. I full text and every occurrence is in a list of particle species or in the
   "neutrino sea" cosmology discussion, not in a treatment of the Homestake deficit.
   The documented home of that argument is young-earth creationist, not geocentrist —
   TalkOrigins' Solar FAQ names Brown 1995, Oard 1995, Davies 1996 and Snelling 1997;
   CRSQ's own retrospective names Hinderliter 1980 and Steidl 1981. I did not find a
   link from any of them to this list, so item 192 stays untraced on the evidence I
   have, and this entry says so rather than picking the nearest plausible author.

   IMPORTANT: what I established is that the same four arguments are in print in that
   volume, in a form the fragments match. That is a content match. It is not a
   demonstrated transmission chain — the list carries no citations at all. Reported up
   in record_problems; clusters.py was NOT touched.

2. THE COMPRESSION FINDING IS THE OBLATENESS ITEM AND IT IS A REVERSAL. Everything
   the located source says about solar oblateness is about its VARIABILITY and its
   irreproducibility. Sungenis's own footnote 1507 cites, by title, "The variable
   oblateness of the Sun: measurements of 1984", "Is the solar oblateness variable?
   Measurements of 1985", and "Oblateness of the Sun in 1983 and Relativity"; his text
   reports Dicke coming back in 1985 with 12 ppm instead of 40, and concludes "These
   results show the extreme difficulty in obtaining accurate and reliable results."
   The list item says "Solar oblateness constancy." If it descends from there, the
   list asserts the negation of its source's point. That is `reversed`.

   The honest caveat is carried in the compression note: there IS a real result the
   word "constancy" fits — Kuhn et al., Science 337:1638 (2012), whose headline was
   that the solar shape is remarkably constant across the activity cycle and too small
   to match the surface rotation. That result postdates the geocentric literature by
   six years and cuts the other way, because a small stable oblateness is exactly what
   leaves general relativity's 42.98"/century intact.

3. WHERE THE LITERATURE IS GENUINELY LIVE — SAY SO, E01 PRECEDENT.
   (a) The fine structure of the solar shape is unsettled RIGHT NOW. Meftah & Mecheri,
       A&A (2025), get 9.02 +/- 0.72 x 10^-6 from the limb and 8.40 +/- 0.02 x 10^-6
       from helioseismic inference, note the two methods disagree on the PHASE of any
       cycle variation, and call that "troubling". Kuhn 2012 had 7.50 +/- 0.51 x 10^-6.
       Surface rotation alone predicts about 8.1 x 10^-6. Nobody should pretend this
       is closed.
   (b) The solar apex has a real internal disagreement, and it is not the one the list
       means. Dehnen & Binney 1998 gave V(sun) = 5.25 +/- 0.62 km/s; Schonrich, Binney
       & Dehnen 2010 revised it to 12.24 km/s, "7 km/s larger than previously
       estimated", and the value is still argued over.
   (c) The solar MODEL problem (composition vs helioseismology) is open — Gustafsson's
       2025 A&ARv review declines to call it solved. That is adjacent to item 192 and
       must not be confused with the neutrino deficit, which is closed.
   (d) The innermost solar core's rotation rate is contested: Fossat et al. 2017 (A&A
       604:A40) claimed 3.8x the radiative envelope from asymptotic g modes; Schunker
       et al. called the detection fragile. This matters because Dicke's mechanism was
       a fast core — but even Fossat's 3.8x is nowhere near Dicke's postulated 20x,
       and J2 is now measured directly from an orbit anyway.

4. ARITHMETIC, ALL REPRODUCIBLE, ALL RUN FOR THIS ENTRY.
   Perihelion: d(omega) = 3*pi*J2*(R/a)^2/(1-e^2)^2 per orbit. With R = 6.957e5 km,
   a = 5.79091e7 km, e = 0.205630, 415.2 orbits per Julian century, the coefficient is
   1.2701e5 arcsec/century per unit J2. Then:
     J2 = 2.25e-7 (Park et al. 2017, MESSENGER)  ->  0.0286"/cy = 0.067% of GR's 42.98
     J2 = 2.5e-5  (Dicke's inference)            ->  3.18"/cy, i.e. his claimed 3.4"
     J2 required for 3.4"                        ->  2.68e-5 = 119x the measured value
   Barycentre: Sun-Earth offset = 1.496e8 * (5.9722e24/1.98892e30) = 449 km = 0.065% of
   a solar radius; Sun's reflex speed from Earth 8.9 cm/s. Sun-Jupiter offset 742,900 km
   = 1.068 R(sun); reflex speed 12.5 m/s. Jupiter's displacement is 1654x Earth's.
   Apex: with (U,V,W) = (11.1, 12.24, 7.25) and a circular speed of 233 km/s, the Sun's
   galactocentric velocity is 245.6 km/s at 3.1 degrees from the tangential direction.
   Sungenis's 32 degrees is 90 minus the 58-degree apex-to-Galactic-centre angle; the
   angle from the apex to the actual l=90 direction is 41 degrees. Either way it is a
   residual, not a total.

5. THE ONE MEASUREMENT THAT ENDS THE APEX ITEM WAS PUBLISHED BEFORE THE BOOK. Reid &
   Brunthaler, ApJ 616:872 (2004): Sgr A* has an apparent proper motion of 6.379 +/-
   0.024 mas/yr "almost entirely in the plane of the Galaxy", and "the effects of the
   orbit of the Sun around the Galactic center can account for this motion". The 2020
   sequel (ApJ 892:39) gives -6.411 +/- 0.008 mas/yr along the plane against -0.219
   +/- 0.007 toward the north Galactic pole — 1.96 degrees out of plane. Vol. I is
   dated 2006. Do not describe this as hindsight.

6. VERDICT. I filed a challenge. REFUTED is right for three items and wrong for two,
   and it is most wrong on the item the cluster NAME leads with. See verdict_challenge.

7. QUOTE PROVENANCE. Every Galileo Was Wrong quotation here is from the OCR of the
   Internet Archive scan, read directly (not via a summarising fetch). Printed page
   numbers are the ones embedded in the OCR text as page footers; they have not been
   checked against a print copy and the locator says so. The book is in copyright, so
   the passage quote is a short excerpt; A03 and R03 set the same practice.
"""

ENTRY = {

"E14": dict(

    tldr=("Four solar topics bundled as five exhibits. The neutrino deficit was closed in "
          "2001 when SNO found the missing two-thirds had changed flavour, and the creationist "
          "ministry that had promoted the argument put it on a public list of claims to stop "
          "using. The Sun's wobble about the barycentre is real, is 1,654 times more Jupiter "
          "than Earth, and is the same effect used to find exoplanets. The solar apex points "
          "where it does because the Galaxy's rotation has already been subtracted out of it. "
          "Real open questions remain here - the Sun's exact shape, one component of the apex, "
          "the solar composition problem - but they are questions about the Sun, which is the "
          "same Sun in both cosmologies."),

    passage=dict(
        work="WRK-SUNGENIS-2006",
        pd=False,
        locator=("Vol. I, Appendix 5, printed p. 1003 of the Internet Archive scan (item "
                 "GallileoWasWrong, file 'Gallileo was wrong_djvu.txt'); page number taken from "
                 "the OCR page footer, not checked against a print copy"),
        quote=("Dicke and his partner Goldenberg found that the sun's polar axis is shorter "
               "than its equatorial axis by approximately 40 parts per million, thus making "
               "the sun oblate, and accounting for at least 3.4″ of the residual perihelion "
               "of Mercury. This new evidence brought the residual down from 43.0 to 39.6."),
        gloss="""<p><strong>What the argument actually is.</strong> Not &ldquo;the Sun is oblate&rdquo; &mdash; everybody agrees it is. The argument is that if the Sun&rsquo;s equatorial bulge is big enough, it explains part of Mercury&rsquo;s anomalous perihelion advance by ordinary Newtonian gravity, leaving general relativity to account for less than the 43&Prime; per century it is famous for predicting. Robert Dicke made that case in earnest from 1967, and he had a theory ready to occupy the space: Brans&ndash;Dicke scalar&ndash;tensor gravity, which predicts slightly less perihelion advance than Einstein. This is a real episode in the history of gravitation, and Sungenis and Bennett report it substantially accurately.</p>
<p><strong>Read what the same appendix concedes.</strong> The passage above is the high-water mark of the section; the pages around it hedge hard. Dicke, we are told, &ldquo;came back in 1985 with further experiments and stated that the results yielded 12 parts per million rather than the original 40 parts per million&rdquo; &mdash; that is the source reporting its own headline number falling by a factor of three &mdash; and the paragraph closes: &ldquo;These results show the extreme difficulty in obtaining accurate and reliable results&rdquo; (printed p. 1004). The supporting footnote 1507 cites its own authorities by title: <em>The variable oblateness of the Sun</em>, <em>Is the solar oblateness variable?</em> The section&rsquo;s conclusion is borrowed from a relativist &mdash; Clifford Will&rsquo;s &ldquo;It is ironic that after seventy years, Einstein&rsquo;s first great success remains an open question, a source of controversy and debate&rdquo; &mdash; and that is a 1986 sentence being asked to describe 2026.</p>
<p><strong>The other three arguments in this cluster, and where they are in print.</strong> The solar apex claim is in the Conclusion to Chapter 12, printed p. 959: <em>&ldquo;The sun is actually traveling in a direction toward Hercules [R.A.18h Dec. +29&deg;] at 20 km/sec (Wilson, 1911). This is about 32&deg; away from an orbital path in the Milky Way!&rdquo;</em> The barycentre claim is in Chapter 4, printed pp. 198&ndash;199, where Fred Hoyle is quoted saying that to calculate correctly &ldquo;the center of the solar system must be placed at an abstract point known as the &lsquo;center of mass,&rsquo; which is displaced quite appreciably from the center of the Sun&rdquo;, and that which centre you use &ldquo;depends on the way in which the local system is considered to be isolated from the universe as a whole&rdquo; &mdash; from which the authors conclude: <em>&ldquo;Certainly no one can object, then, if God had decided long ago to put the Earth in that very barycenter.&rdquo;</em> It is developed at Chapter 10, pp. 598&ndash;603, as &ldquo;the immovable barycenter of the universe&rdquo;.</p>
<p><strong>The neutrino item has a different family.</strong> A word search of the Vol. I full text returns eight occurrences of &ldquo;neutrino&rdquo;, all of them in lists of particle species or in the discussion of a cosmological neutrino sea, and none in a treatment of the Homestake deficit. The argument that the missing solar neutrinos mean the Sun is not fusion-powered is documented in young-earth creationist writing rather than geocentric writing, and it is documented there being withdrawn: Creation Ministries International lists <em>&ldquo;Missing solar neutrinos prove that the sun shines by gravitational collapse, and is proof of a young sun&rdquo;</em> among arguments creationists should not use, and instructs that they should &ldquo;<em>no longer</em> invoke the missing neutrino problem to deny that fusion is the primary source of energy for the sun.&rdquo; Whether this list took the item from that tradition is not shown; it carries no citation.</p>"""),

    steelman=dict(
        description="""<p><strong>SURFACE (weak &mdash; do not use).</strong> &ldquo;These are just gaps, and gaps get filled.&rdquo; That is a promissory note, not an argument, and it is exactly the move this project objects to when a proof list makes it. Equally weak: &ldquo;the solar neutrino problem was never a real problem.&rdquo; It was a real problem for thirty-three years, and two Nobel Prizes were awarded over it.</p>
<p><strong>DEEPER.</strong> Every one of the five facts is real. The Sun really does wobble about the system&rsquo;s centre of mass rather than sitting still at a focus. The solar apex really does point at Hercules at about 20 km/s, nowhere near the direction of the Galactic centre. Homestake really did see about a third of the predicted neutrinos, for decades, and the standard solar model really was under suspicion. The Sun really is oblate and its exact shape is <em>still</em> disputed in the 2025 literature. A defender who says only &ldquo;none of your five is fabricated&rdquo; is correct.</p>
<p><strong>KERNEL.</strong> The strongest form is Dicke&rsquo;s, and it is not about the Sun at all. It is that <em>the single most celebrated confirmation of general relativity is a residual</em> &mdash; what is left of Mercury&rsquo;s 575&Prime;/century after subtracting the planetary perturbations and the precession of the equinoxes &mdash; and a residual inherits every uncertainty in everything you subtracted. Dicke saw that a Newtonian source nobody had measured properly, a solar quadrupole, sat inside the error budget of the crown-jewel test, and he went and measured it rather than arguing about it. He was right that the test was model-dependent, right that an alternative theory could occupy the gap, and right that the community&rsquo;s confidence had outrun its data. Sungenis and Bennett found a genuine episode in which the establishment&rsquo;s certainty was ahead of its evidence, and they quote a relativist saying so. Concede all of that.</p>""",
        why_it_doesnt_save_claim="""<p>Because the thing Dicke said had not been measured has since been measured, twice, by methods that do not use Mercury. Helioseismology reads the Sun&rsquo;s internal rotation profile directly from its oscillation modes and finds the radiative interior turning close to rigidly rather than twenty times faster than the surface, which was Dicke&rsquo;s postulated mechanism. And ranging to the MESSENGER spacecraft in orbit at Mercury fixed the solar quadrupole moment at J<sub>2</sub> = (2.25 &plusmn; 0.09) &times; 10<sup>&minus;7</sup> (Park et al., <em>AJ</em> 153:121, 2017). Put that number in the standard expression &mdash; &Delta;&omega; = 3&pi;J<sub>2</sub>(R<sub>&#9737;</sub>/a)<sup>2</sup>/(1&minus;e<sup>2</sup>)<sup>2</sup> per orbit, 415.2 orbits per Julian century &mdash; and the quadrupole contributes <strong>0.029&Prime; per century</strong>, seven hundredths of one per cent of the 42.98&Prime; general relativity predicts. Dicke&rsquo;s 3.4&Prime; needed J<sub>2</sub> = 2.7 &times; 10<sup>&minus;5</sup>: <strong>119 times</strong> the measured value.</p>
<p>The rest of the kernel closed the same way. Brans&ndash;Dicke theory was not refuted so much as squeezed: the Cassini radio-link test put the PPN parameter &gamma; within (2.1 &plusmn; 2.3) &times; 10<sup>&minus;5</sup> of the Einstein value (Bertotti, Iess &amp; Tortora, <em>Nature</em> 425:374, 2003), forcing &omega; above roughly 40,000, at which point the theory Dicke built to exploit the oblateness makes predictions no experiment can tell from general relativity&rsquo;s. And Will&rsquo;s &ldquo;open question&rdquo; sentence, which the source uses as its closer, was written in 1986 &mdash; before helioseismic rotation inversions, before Cassini, before MESSENGER. Quoting it in 2006 was already stale; carrying it forward to a list published later is quoting a scientist&rsquo;s honest uncertainty about data he did not yet have as though it were a verdict on data he now does.</p>""",
    ),

    refutation="""<p>Five items, five different situations. They are answered separately because bundling them is the only thing that makes them look like a pattern.</p>

<p><strong>1. The neutrino deficit (item 192) &mdash; closed, and closed by the people who would have loved it to stay open.</strong> Ray Davis&rsquo;s Homestake detector, running from the late 1960s, saw roughly a third of the electron neutrinos the standard solar model predicted. That is a genuine three-decade anomaly and it was taken seriously: either the Sun&rsquo;s core was cooler than modelled, or something happened to neutrinos in flight. The Sudbury Neutrino Observatory settled it by measuring both quantities at once &mdash; the electron-neutrino flux and the flux of <em>all three</em> flavours, via a neutral-current channel that does not care which flavour arrives. The electron fraction came out about a third, matching Homestake; the total came out at the standard solar model&rsquo;s prediction. The missing neutrinos were not missing, they had changed flavour, which means they have mass. Kajita and McDonald took the 2015 Nobel Prize for it. There is no residue of this problem left to point at. What makes the item worth publishing is not that it is out of date but <em>who says so</em>: Creation Ministries International carries &ldquo;Missing solar neutrinos prove that the sun shines by gravitational collapse&rdquo; on its standing list of arguments creationists should not use, with the instruction that they should &ldquo;<em>no longer</em> invoke&rdquo; it. A movement that maintains a public retraction list retracted this one, and it has turned up here anyway, three words wide and with no date attached.</p>

<p>One neighbouring question is still open and should not be conflated with this one. The <em>solar composition</em> problem &mdash; the downward revision of the Sun&rsquo;s metal abundances, which broke the agreement between the standard solar model and helioseismic soundings of the convection-zone depth and helium content &mdash; remains unsettled; Gustafsson&rsquo;s 2025 review in <em>The Astronomy and Astrophysics Review</em> declines to pronounce the &ldquo;solar model problem&rdquo; definitively solved. That is a live disagreement about the Sun&rsquo;s ingredients. It is not the neutrino deficit, which was a disagreement about the Sun&rsquo;s energy source and is finished, and item 192 names the finished one.</p>

<p><strong>2. The barycentre wobble (items 104 and 361) &mdash; a prediction, reported as an embarrassment.</strong> Both items are true descriptions of the solar system and neither is a problem for anything. The Sun does not sit still: it orbits the system&rsquo;s centre of mass, and because Jupiter and Saturn are where the mass is, that centre wanders up to a couple of solar radii from the Sun&rsquo;s own centre. This is not a patch. It falls straight out of Newton&rsquo;s third law &mdash; if the Sun pulls Jupiter, Jupiter pulls the Sun &mdash; and it is quantitatively fixed with no freedom at all. Item 104 says the wobble is about the Earth. Run the numbers: the Sun&ndash;Earth centre of mass lies 449 km from the Sun&rsquo;s centre, which is 0.065% of a solar radius, and the Earth swings the Sun at 8.9 cm/s. The Sun&ndash;Jupiter centre of mass lies 742,900 km out, 1.068 solar radii, and Jupiter swings the Sun at 12.5 m/s. Jupiter&rsquo;s displacement of the Sun is <strong>1,654 times</strong> the Earth&rsquo;s. A model in which the Sun&rsquo;s inertial wobble tracks the Earth is not a rival interpretation of the same data; it is off by three orders of magnitude in the one quantity it names.</p>

<p>Item 361 calls the wobble &ldquo;epicyclic&rdquo;, and the charge deserves a straight answer rather than a sneer, because the historical half of it is correct. Copernicus really did need more circles than the schoolbook story admits &mdash; historians of astronomy have been saying so since Koestler, and Owen Gingerich, whom this cluster&rsquo;s source quotes accurately on the point, has spent a career correcting the &ldquo;thirty-four circles&rdquo; legend. A heliocentric model is not automatically simpler. But an epicycle in the Ptolemaic sense is a <em>free parameter</em>: a circle whose radius and period you choose, after the fact, to fit a planet that was not behaving. The Sun&rsquo;s barycentric path has no free parameters. Its amplitude, period and phase are forced by the planetary masses and orbits, and it is checked to the centimetre per second every night: precision Doppler spectroscopy subtracts the observer&rsquo;s velocity about the solar-system barycentre to 1 cm/s (Wright &amp; Eastman, <em>PASP</em> 126:838, 2014), and if that motion were fictional the subtraction would spoil the data rather than clean it. The same reflex wobble seen from outside is how planets are found around other stars: 51 Pegasi swings at 59 m/s, and the Sun would show 12.5 m/s to a distant observer with our instruments. Ptolemy&rsquo;s epicycles predicted nothing new. This wobble predicted a planetary population nobody had seen.</p>

<p><strong>3. The solar apex (item 138) &mdash; a residual mistaken for a total.</strong> The source&rsquo;s version is specific enough to check: the Sun moves toward Hercules at about 20 km/s, which is roughly 32&deg; away from where it would have to point to be orbiting the Galaxy, so &ldquo;present popular theories regarding the rotation of the Milky Way Galaxy cannot be correct.&rdquo; The arithmetic behind the 32&deg; is sound &mdash; the apex sits about 58&deg; from the Galactic centre, and 90 &minus; 58 = 32 &mdash; and the conclusion still does not follow, because of what the apex <em>is</em>. The solar apex is the Sun&rsquo;s motion relative to the local standard of rest: the mean motion of the stars in our neighbourhood, which are themselves all sweeping around the Galaxy together. Galactic rotation is common to the Sun and to the comparison sample, so it cancels in the subtraction <em>by construction</em>. The apex is the leftover after removing exactly the motion the argument then complains is absent. Restore it: with a solar peculiar velocity of (11.1, 12.24, 7.25) km/s and a circular speed of 233 km/s, the Sun&rsquo;s velocity about the Galactic centre is 245.6 km/s, and it lies <strong>3.1&deg;</strong> from the tangential direction. The 20 km/s residual is under 8% of the total.</p>

<p>That is a calculation, so here is a measurement. Very Long Baseline Array astrometry of Sagittarius A* against background quasars sees the Galactic centre drifting across the sky at 6.379 &plusmn; 0.024 mas/yr, &ldquo;almost entirely in the plane of the Galaxy&rdquo;, and the authors state that &ldquo;the effects of the orbit of the Sun around the Galactic center can account for this motion&rdquo; (Reid &amp; Brunthaler, <em>ApJ</em> 616:872, 2004). The eighteen-year sequel gives &minus;6.411 &plusmn; 0.008 mas/yr along the plane against &minus;0.219 &plusmn; 0.007 toward the north Galactic pole (<em>ApJ</em> 892:39, 2020) &mdash; the Sun&rsquo;s motion relative to the Galactic centre is <strong>1.96&deg;</strong> out of the plane, not 32&deg;. The first of those papers was published two years before <em>Galileo Was Wrong</em> Vol. I.</p>

<p>There <em>is</em> a real inconsistency in the solar-apex literature, and it is worth naming because it is not the one being claimed. The Sun&rsquo;s velocity component in the direction of Galactic rotation has moved: Dehnen &amp; Binney put V<sub>&#9737;</sub> at 5.25 &plusmn; 0.62 km/s in 1998; Sch&ouml;nrich, Binney &amp; Dehnen revised it to 12.24 km/s in 2010, &ldquo;7 km s<sup>&minus;1</sup> larger than previously estimated&rdquo;, after finding a metallicity bias in the asymmetric-drift extrapolation everyone had been using; and it is still argued over. That is a genuine 7 km/s disagreement about one component of a 20 km/s residual inside a 246 km/s motion. It tells you the local disc is complicated. It does not move the Sun off its orbit.</p>

<p><strong>4. Solar oblateness (item 195) &mdash; the one live question here, and it points the wrong way for the list.</strong> Take this seriously, because it has not been settled. The current numbers: Meftah &amp; Mecheri (<em>A&amp;A</em>, 2025) measure a fractional oblateness of 9.02 &plusmn; 0.72 &times; 10<sup>&minus;6</sup> from limb observations and 8.40 &plusmn; 0.02 &times; 10<sup>&minus;6</sup> from helioseismic inference; Kuhn et al. (<em>Science</em> 337:1638, 2012) had 7.50 &plusmn; 0.51 &times; 10<sup>&minus;6</sup> and reported the shape as remarkably constant across the activity cycle and slightly too small for the surface rotation. The two modern methods disagree about whether the oblateness varies in phase or in anti-phase with solar activity, and the 2025 authors call that &ldquo;troubling&rdquo;. Anyone claiming the shape of the Sun is fully understood is overstating.</p>

<p>Now put a ruler on it. All of those values cluster around 8 &times; 10<sup>&minus;6</sup>. Dicke and Goldenberg&rsquo;s was (5.0 &plusmn; 0.7) &times; 10<sup>&minus;5</sup> &mdash; six times larger &mdash; and the quantity that actually acts on Mercury is not the surface flattening but the mass quadrupole J<sub>2</sub>, which is smaller still because the Sun is centrally condensed and the shape of a thin bright edge says little about how the mass inside is distributed. Dicke&rsquo;s inference from surface shape to a large J<sub>2</sub> required a core spinning about twenty times faster than the surface; helioseismic inversions later read the interior rotation directly and found the radiative zone turning close to rigidly. MESSENGER then measured J<sub>2</sub> = (2.25 &plusmn; 0.09) &times; 10<sup>&minus;7</sup> from Mercury&rsquo;s own orbit, giving a quadrupole contribution of <strong>0.029&Prime; per century</strong> against general relativity&rsquo;s 42.98&Prime;. So the whole live dispute &mdash; every part-per-million of it &mdash; is happening two orders of magnitude below the level at which it could touch the test it was recruited to unsettle. The Sun&rsquo;s shape is an open problem in solar physics and a closed one in celestial mechanics, and the item does not distinguish the two.</p>

<p><strong>5. The step that is left to the reader.</strong> Only one of the five items names the Earth &mdash; item 104, and it names it as the body the Sun supposedly wobbles around, which is still a claim about the Sun. In all five the move from a solar fact to a conclusion about the Earth&rsquo;s motion or shape is unstated. Suppose every one were true at maximum strength: the Sun&rsquo;s core spins fast, its shape is unexplained, its apex is odd, its neutrinos are short, and it wobbles. Every one of those is a fact about the Sun, and the Sun&rsquo;s internal physics is the same object of study in both cosmologies. A geocentric or flat-Earth model inherits these questions rather than dissolving them: it needs the Sun&rsquo;s neutrino flux accounted for and its oblateness measured exactly as much as anyone else does. What such a model offers on either count is not located in the Vol. I text searched for this entry, whose solar-physics content is the Appendix 5 perihelion argument quoted above. The bundle&rsquo;s working function is volume: five items, five independent-looking witnesses, one inference nobody writes down.</p>

<p><strong>Verdict.</strong> Three of the five are contradicted by specific measurements &mdash; the neutrino deficit by SNO, the Earth-centred wobble by the mass ratio, the apex claim by VLBI astrometry of Sgr A*. One is a prediction reported as a defect. One is a real open question in solar physics with no stated bearing on the Earth. Refuted &mdash; with the dissent recorded below, because the oblateness item has not earned that word.</p>""",

    advocate=dict(
        best_defense=(
            "Look at what you actually did. You chose the oblateness item for your compression "
            "block, called it 'reversed', and then admitted in the same breath that you cannot "
            "show our list ever read that book. So the finding is: if the item came from a "
            "source you have not connected it to, then it contradicts that source. That is a "
            "conditional dressed as a catch. Second, your own text concedes more than it "
            "refutes. You concede the solar shape is unresolved in 2025 and that two modern "
            "methods disagree about its sign; you concede the apex has a live 7 km/s dispute; "
            "you concede the solar model problem is open; you concede the innermost core's "
            "rotation is contested; you concede the Sun does wobble and that Copernicus needed "
            "more circles than the textbooks say. Five concessions is not a debunk, it is our "
            "list with footnotes. Third, and this is the one that should worry you: your "
            "answer to Dicke is MESSENGER, and Park et al. estimate J2 and the PPN parameters "
            "beta and gamma from the same ranging data in the same fit. You have told a man "
            "who said the perihelion test cannot separate a Newtonian source from a "
            "relativistic one that the question was settled by a fit which estimates both at "
            "once. That is his objection, not its answer. And notice how much machinery you "
            "needed - helioseismic inversions, a Cassini radio link, a spacecraft in orbit at "
            "Mercury - to dispose of five sentences. Arguments that are obviously wrong do not "
            "cost that much."),
        survives=3,
        preemptive=(
            "Three is right and the third move is what earns it. Three changes, in order. "
            "(a) The MESSENGER circularity charge must be answered in the body and is, in the "
            "steelman's second half: J2 is fixed independently of any orbit fit by helioseismic "
            "rotation inversions, and gamma is fixed independently of Mercury by Cassini, so "
            "the degeneracy Dicke identified is broken by data from outside the fit rather than "
            "inside it. If an editor ever trims that paragraph, the strongest objection on this "
            "page loses its answer. (b) On the conditional: do not defend it, state it. The "
            "compression note already says the drift holds only if the item descends from that "
            "appendix, and names the alternative reading; keep that sentence and resist any "
            "edit that firms it up. A compression finding that has to be true regardless of "
            "provenance is not a provenance finding. (c) On the concessions, invert the frame "
            "rather than reducing their number. Every one of them is a live question about the "
            "SUN, and the Sun is identical in both cosmologies - so a defender who banks all "
            "five has banked nothing about the Earth. Say that where the concessions are made, "
            "not only in the closing section, because a reader who stops early meets the "
            "concessions first. On tone: 'arguments that are obviously wrong do not cost that "
            "much' is fair and should not be brushed off. The reply is that the cost was paid "
            "once, by solar physics, for its own reasons, and this page is spending it rather "
            "than earning it.")),

    straw_man=dict(
        identified=True,
        detail=("The oblateness section is aimed at a confidence nobody defends. It quotes "
                "Clifford Will's 1986 line about Einstein's first great success remaining "
                "'an open question, a source of controversy and debate' as though relativists "
                "claimed the Mercury test was airtight and were caught out - when the sentence "
                "is a relativist volunteering the uncertainty, in a popular book, decades "
                "before the measurements that closed it. Reporting a field's own published "
                "self-criticism as though it had been extracted under pressure is the "
                "misrepresentation. The same shape appears in the neutrino item: the deficit "
                "was announced, publicised and pursued by the physicists whose model it "
                "threatened, and Davis spent thirty years on it and was given a Nobel Prize "
                "for the anomaly itself."),
    ),

    compression=dict(
        assessed=True, drifted=True,
        list_phrasing="Solar oblateness constancy.",
        source_wording=("&ldquo;Dicke came back in 1985 with further experiments and stated that the "
                        "results yielded 12 parts per million rather than the original 40 parts per "
                        "million. These results show the extreme difficulty in obtaining accurate and "
                        "reliable results.&rdquo; &mdash; with the supporting footnote citing, by "
                        "title, <em>The variable oblateness of the Sun: measurements of 1984</em> and "
                        "<em>Is the solar oblateness variable? Measurements of 1985</em>."),
        drift_type="reversed",
        note=("<strong>The located source argues that the solar oblateness is large, variable and "
              "hard to pin down. The item asserts that it is constant.</strong> Everything the "
              "appendix at printed pp. 1003&ndash;1004 does with this topic depends on the "
              "measurements disagreeing with each other &mdash; that is how the residual perihelion "
              "is made to look negotiable, and the section&rsquo;s own footnote 1507 recruits papers "
              "whose titles ask whether the oblateness varies. A one-word compression to "
              "&ldquo;constancy&rdquo; states the negation of the point the pages are making. "
              "<strong>The condition matters and is not hidden:</strong> this holds if item 195 "
              "descends from that appendix, and the list carries no citations, so the descent is a "
              "content match rather than a demonstrated chain. "
              "<strong>The charitable alternative reading does not rescue it either.</strong> There "
              "is a real result the word fits &mdash; Kuhn et al., <em>Science</em> 337:1638 (2012), "
              "whose finding was that the solar shape stays remarkably constant across the activity "
              "cycle and comes out slightly too small for the surface rotation, a puzzle still open "
              "in the 2025 measurements. But that result is six years later than the book and runs "
              "the opposite way for the argument: a small, stable oblateness is precisely what "
              "leaves Einstein&rsquo;s 42.98&Prime; per century untouched. On either reading the "
              "three-word item claims something its ancestry will not support &mdash; on the first "
              "by contradicting it, on the second by borrowing a result that refutes the case it is "
              "filed under. Compare <a href=\"#ARG-E13\">ARG-E13</a>, where real anomalies are "
              "bundled the same way, and <a href=\"#ARG-E01\">ARG-E01</a>, the standing example of "
              "an anomaly this project declines to overclaim about."),
    ),

    verdict_challenge=dict(
        challenged=True,
        proposed_verdict=("REFUTED for items 104, 138 and 192; MISLEADING for item 361; "
                          "NOT DEMONSTRATED for item 195"),
        reasoning=("One verdict is doing work here that it cannot do, and it fails hardest on the "
                   "topic the cluster is named after. REFUTED means 'contradicted by a specific "
                   "measurement'. That is exactly right for the neutrino deficit, which SNO "
                   "measured out of existence, for the claim that the Sun's inertial wobble is "
                   "about the Earth, which is wrong by a factor of 1,654, and for the apex claim, "
                   "which VLBI astrometry of Sgr A* contradicts directly. It is the wrong label "
                   "for item 361: the Sun's barycentric wobble is real, predicted and used, so "
                   "what is wrong is the inference, which is what MISLEADING is for - real data, "
                   "wrong conclusion made to look supported. And it is the wrong label for item "
                   "195, where no measurement contradicts anything: the solar oblateness and its "
                   "cycle variation are genuinely unresolved in the 2025 literature, and what is "
                   "missing is any argument from the Sun's shape to the Earth's motion, which is "
                   "what NOT DEMONSTRATED is for. Calling a live solar-physics question REFUTED "
                   "is the single most attackable sentence this cluster could publish, because a "
                   "defender who has read Meftah and Mecheri can show that we called an open "
                   "measurement closed - and would be right. The cluster note is a second-order "
                   "instance of the same gap: it addresses neutrinos and the barycentre and is "
                   "silent on the two topics named in the cluster title. If the schema will not "
                   "carry per-item verdicts, the defensible single verdict for the bundle is "
                   "MISLEADING rather than REFUTED, since the bundle's characteristic move is "
                   "assembling true or arguable solar facts behind an inference nobody states."),
    ),

    people=["PER-SUNGENIS"],
    related=["E01", "E03", "E13", "E15", "E16", "E17", "E18", "R01", "R03", "A03", "A05"],

    sources=[
        dict(label="Sungenis & Bennett, Galileo Was Wrong Vol. I — Internet Archive scan (item "
                   "GallileoWasWrong): solar oblateness at printed pp. 1003–1004, the solar-apex "
                   "claim at p. 959, the Hoyle barycentre passage at pp. 198–199",
             url="https://archive.org/details/GallileoWasWrong"),
        dict(label="Dicke & Goldenberg, “Solar Oblateness and General Relativity”, Phys. Rev. "
                   "Lett. 18:313 (1967) — the (5.0 ± 0.7) × 10⁻⁵ figure the source quotes",
             url="https://link.aps.org/doi/10.1103/PhysRevLett.18.313"),
        dict(label="Park et al., “Precession of Mercury's Perihelion from Ranging to the "
                   "MESSENGER Spacecraft”, AJ 153:121 (2017) — J₂ = (2.25 ± 0.09) × 10⁻⁷, total "
                   "precession 575.3100 ± 0.0015″/century",
             url="https://dspace.mit.edu/handle/1721.1/109312"),
        dict(label="Bertotti, Iess & Tortora, “A test of general relativity using radio links "
                   "with the Cassini spacecraft”, Nature 425:374 (2003) — γ to 2.3 × 10⁻⁵, which "
                   "is what squeezed Brans–Dicke",
             url="https://www.nature.com/articles/nature01997"),
        dict(label="Kuhn, Bush, Emilio & Scholl, “The Precise Solar Shape and Its Variability”, "
                   "Science 337:1638 (2012) — the shape is constant across the activity cycle "
                   "and too small for the surface rotation",
             url="https://www.science.org/doi/10.1126/science.1223231"),
        dict(label="Meftah & Mecheri, “Solar shape variations across cycles 24 and 25: "
                   "observations from 2010 to 2023”, A&A (2025) — 9.02 ± 0.72 × 10⁻⁶ from the "
                   "limb, 8.40 ± 0.02 × 10⁻⁶ helioseismic, the two methods in disagreement over "
                   "the phase of the cycle variation",
             url="https://www.aanda.org/articles/aa/full_html/2025/01/aa51130-24/aa51130-24.html"),
        dict(label="Reid & Brunthaler, “The Proper Motion of Sagittarius A*. II”, ApJ 616:872 "
                   "(2004) — 6.379 ± 0.024 mas/yr, “almost entirely in the plane of the Galaxy”; "
                   "published two years before Galileo Was Wrong Vol. I",
             url="https://arxiv.org/abs/astro-ph/0408107"),
        dict(label="Reid & Brunthaler, “The Proper Motion of Sagittarius A*. III”, ApJ 892:39 "
                   "(2020) — −6.411 ± 0.008 mas/yr along the plane, −0.219 ± 0.007 toward the "
                   "north Galactic pole",
             url="https://arxiv.org/abs/2001.04386"),
        dict(label="Schönrich, Binney & Dehnen, “Local kinematics and the local standard of "
                   "rest”, MNRAS 403:1829 (2010) — (U,V,W)⊙ = (11.1, 12.24, 7.25) km/s, V⊙ "
                   "“7 km s⁻¹ larger than previously estimated”",
             url="https://academic.oup.com/mnras/article/403/4/1829/1054839"),
        dict(label="Creation Ministries International, “Arguments we think creationists should "
                   "NOT use” — retires “Missing solar neutrinos prove that the sun shines by "
                   "gravitational collapse”",
             url="https://creation.com/en/articles/arguments-we-think-creationists-should-not-use"),
        dict(label="TalkOrigins Solar FAQ — documents the creationist use of the neutrino deficit "
                   "(Brown 1995, Oard 1995, Davies 1996, Snelling 1997) and its resolution by "
                   "neutrino oscillation",
             url="http://talkorigins.org/faqs/faq-solar.html"),
        dict(label="Solar neutrino problem — Homestake's one-third deficit, the SNO neutral-current "
                   "result, and the 2015 Nobel Prize to Kajita and McDonald",
             url="https://en.wikipedia.org/wiki/Solar_neutrino_problem"),
        dict(label="Gustafsson, “Is the composition of the solar atmosphere unusual, and if so, "
                   "why?”, The Astronomy and Astrophysics Review (2025) — the solar composition "
                   "problem is not yet “definitively solved”; distinct from the neutrino deficit",
             url="https://link.springer.com/article/10.1007/s00159-025-00160-9"),
        dict(label="Fossat et al., “Asymptotic g modes: evidence for a rapid rotation of the "
                   "solar core”, A&A 604:A40 (2017) — the contested 3.8× core rotation claim",
             url="https://www.aanda.org/articles/aa/full_html/2017/08/aa30460-17/aa30460-17.html"),
        dict(label="Wright & Eastman, “Barycentric corrections at 1 cm/s for precise Doppler "
                   "velocities”, PASP 126:838 (2014) — the Sun's barycentric motion as working "
                   "metrology",
             url="https://arxiv.org/abs/1409.4774"),
    ]),
}
