# -*- coding: utf-8 -*-
"""Batch 10 — A15. "Torsion balances, gravimeters and pendulum clocks show no variation."

Four items: 232 "Gravimeter constancy.", 249 "Pendulum building sensitivity.",
250 "Torsion balance null variation.", 398 "Pendulum clocks stable."
Verdict NOT DEMONSTRATED, kept. originator=None, kept.

Research notes for whoever picks this up next.

1. PROVENANCE FIRST, BECAUSE THIS IS ONE OF THE UNTRACED 28 AND THE RECORD IS A
   HYPOTHESIS. The search was run and it TERMINATED IN A RESULT: no author was found
   who argues from gravimeters, pendulum clocks or torsion balances to a stationary
   Earth, and `pre_modern` was considered and rejected (there is no old text to inherit
   from either). What was searched, with the counts, so a future pass can re-run it:

     * The specimen (withthesun33.com/about-1, re-fetched 2026-08-10). Heading "THE EARTH
       IS FLAT AND NON ROTATING"; 461 numbered lines; no citation attached to any item.
       Items 232/249/250/398 confirmed verbatim as recorded in corpus.py.
     * Rowbotham, ZETETIC ASTRONOMY: EARTH NOT A GLOBE (1865 first book edition, Project
       Gutenberg #69892, full text). "pendulum" 78 hits; "Foucault" 14; "gravimet-",
       "torsion" and "Cavendish" 0 each. THE 78 MATTER — see §2.
     * Carpenter, ONE HUNDRED PROOFS (1885, Gutenberg #55387, full text). "pendulum" 7
       hits, all proof 73 plus the index line. "gravimet-", "torsion", "Cavendish",
       "Foucault", "clock": 0 each. Proof 73 is a Foucault-precession claim, i.e. A06.
     * Dubay, 200 PROOFS (archive item 200proofsearthisnotaspinningballericdubay, djvu
       text). "pendulum" 9 hits, all proof 140; "Foucault" 3; "gravimet-", "torsion",
       "Cavendish" 0 each. Proof 140 is again Foucault. Its "clock" hits are about
       circumnavigation and time zones.
     * Sungenis & Bennett, GALILEO WAS WRONG, both archive scans, full OCR text.
       Vol. I (item GallileoWasWrong) and Vol. II (item ...Bennett4276): "gravimeter" and
       "gravimetr-" 0 hits in either; "torsion" 14 in each; "Eotvos" 2 in each; "Richer"
       and "Cayenne" 0 in either. The torsion hits are the two things in §3.
     * Edward Hendrie, THE GREATEST LIE ON EARTH (2016), archive OCR text of item
       the-greatest-lie-on-earth-proof-that-our-world-is-not-a-moving-globe: "pendulum",
       "Foucault", "gravimeter", "torsion" and "Cavendish" all 0 hits. Included because
       it is the largest post-2015 flat-earth compendium with a physics apparatus.
     * The Flat Earth Society wiki, pages "Gravimetry" and "Variations in Gravity", read
       end to end. Their argument is NOT constancy. It is that gravimeters are long-period
       seismometers and that the published numbers are reached through latitude, free-air
       and terrain corrections — "Gravimeters do not give direct measurements of gravity."
       That is a different claim from item 232, and it is the strongest one in the field.

2. THE NEAREST TEXT ON THE PENDULUM HALF SAYS THE REVERSE, AND IT IS ROWBOTHAM. In the
   1865 edition, in the run of anti-rotundity arguments after the Polaris passage in
   Section I, Rowbotham takes up the latitude variation of the seconds pendulum, CONCEDES
   IT, PRINTS THE NUMBERS (39.027 in. at the equator, 39.197 in. at the pole) and
   reattributes it to (a) thermal expansion of the rod and (b) air density. This is A13's
   material, not A15's — but it is the nearest thing in the tradition to item 398, and it
   is its negation. DO NOT file it as A15's source and DO NOT let a future pass move item
   398 into A13: 398 asserts the stability Rowbotham denies.

3. THE ARITHMETIC THAT KILLS ROWBOTHAM'S REATTRIBUTION, USING ONLY HIS OWN TWO
   FOOTNOTES. Recomputed here 2026-08-10.
   (a) What he must explain. (39.197 - 39.027)/39.027 = 4.356e-3. Since T is proportional
       to sqrt(L), a rate difference of 0.5 x 4.356e-3 x 86400 = 188 s/day.
   (b) What his mechanism supplies. His footnote 6 quotes Noad: 30 degF alters the length
       by 1/5000 and costs "8 seconds per day" — internally consistent, since
       0.5 x (1/5000) x 86400 = 8.64 s/day. His footnote 5 table gives his own
       equator-to-pole mean temperature span: 84.2 degF to 0.0 degF. So
       (84.2/30)/5000 = 5.613e-4, i.e. 24 s/day.
   (c) 188/24 = 7.8. His cause is short by a factor of about eight, on his numbers.
   (d) Buoyancy is worse. ALL the air is worth 0.5 x (1.2/8500) x 86400 = 6 s/day for a
       brass bob; the equator-to-pole air-density difference is a fraction of that.
   (e) AND THE DECISIVE ONE, which is not arithmetic at all. The London figure Rowbotham
       quotes from Noad — 39.13929 in. — is given "in vacuo ... at the temperature of
       62 deg". That is Kater's 1818 reduction (Kater's published value is 39.1386 in.
       at London, sea level, 62 degF, in vacuum; the two agree to about 1 part in 50,000).
       Temperature and air were held fixed BY DEFINITION in the datum he is explaining.
       Do not soften this into "he was unaware of the corrections" — he prints them.

4. THE MOVEMENT WANTS BOTH ANSWERS AT ONCE, AND BOTH HALVES ARE DOCUMENTED IN ONE BOOK.
   Vol. II ch. 7 ("The Cause of Gravity in the Geocentric Universe", printed p. 27 with
   its footnote 70) and Appendix 1 (printed p. 640) cite torsion-balance and pendulum
   ANOMALIES as evidence for a LeSagean geocentric dynamics — Long, Nature 260:417 (1976)
   and its "systematic discrepancies of 0.37%"; the eclipse pendulum work at Phys. Rev.
   D3, 823 (that is Saxl & Allen 1971) and Kuusela 1990/91; the Holding & Tuck mineshaft
   G determination. So the same tradition's flagship volume argues that these instruments
   show anomalous VARIATION, while item 250 argues they show a null. Report both.

5. THE ONE TORSION-BALANCE NULL ON POINT IN THE GEOCENTRIC LITERATURE IS DISCLAIMED BY
   THE BOOK THAT PRINTS IT. Vol. I ch. 12 is a catalogue of ether-drift experiments, each
   followed by a "Geocentrism's Response". Trouton-Noble 1903 — a charged capacitor on a
   torsion fibre, null for the Earth's motion — begins on printed p. 855, and on p. 856
   the response reads: "Only light and gases show ether effects; the experiment was
   incapable of achieving ether detection unless a charged gas is used between the
   plates." The book also records the null "was repeated in experiments by Chase in 1927
   and Hayden in 1994" and that such results "are now thought to be consistent with
   Special Relativity". A defender cannot bank that null; his own source spent it.

6. THE KERNEL, AND IT IS THE BEST THING IN THIS ENTRY. Eotvos's torsion balance returns a
   null, and the null is genuine and famous. But the balance detects a difference in
   inertial-to-gravitational mass ratio only through the HORIZONTAL COMPONENT OF THE
   CENTRIFUGAL ACCELERATION, which at his latitude is omega^2 R cos(phi) sin(phi) =
   0.0339 x cos(47.5) x sin(47.5) = 0.0169 m/s^2, about 1.7e-3 g. Set omega = 0 and the
   term is identically zero: the instrument has no signal channel, and what you have is
   not a null result but no experiment. Same shape as E08's flyby constant K = 2*omega*R/c,
   and stronger, because the balance is the movement's own favourite instrument.

7. NUMBERS USED, ALL RECOMPUTED HERE 2026-08-10.
   omega^2 a = (7.292115e-5)^2 x 6378137 = 0.033916 m/s^2 = 0.347% of g.
   IGF: 9.7803253359 (equator) to 9.8321849378 (pole) m/s^2 = 0.530%.
   Seconds pendulum from L = g/pi^2: 39.014 in. (equator), 39.221 in. (pole). Rowbotham's
   39.027/39.197 are Sir Richard Phillips's, and span less than the modern values; quote
   them as HIS and do the arithmetic in his numbers, not ours.
   Eotvos correction 2*omega*v*cos(phi) at 45 deg: 10-knot ship (5.144 m/s) eastward =
   5.30e-4 m/s^2 = 53 mGal; aircraft at 200 m/s = 2.06e-2 m/s^2 = 2063 mGal.
   Solar tidal gradient 2*G*M_sun*R_E/d^3 = 5.05e-7 m/s^2 (about 50 uGal) against the
   Sun's direct pull at Earth of 5.93e-3 m/s^2, which free fall cancels.

8. WHAT IS OPEN, AND THE PAGE MUST KEEP SAYING IT. A gravimeter really does show nothing
   attributable to a 30 km/s orbital velocity, and it should not — that is the equivalence
   principle, and it is the same structure as A03's null. Do not claim gravimetry detects
   the orbit. It detects the tidal residual, which is a gradient, not a velocity.
   Separately: the most interesting real claim linking torsion balances to the Earth's
   rotation runs the OTHER way — Anderson et al., EPL 110:10002 (2015) reported a 5.9-year
   periodicity in measured G in phase with length-of-day variation. It did not hold:
   Schlamminger, Gundlach & Newman (arXiv:1505.01774) showed corrections to the G data
   significantly weaken the correlation, and Pitkin (EPL 111:30002) found an extra-noise
   model favoured over a sinusoid by factors of order e^30. Say all of that plainly; it is
   the honest way to hold the "torsion balances see nothing anomalous" ground.

9. VERDICT. NOT DEMONSTRATED kept, and REFUTED was seriously weighed. The reason it was
   rejected is worth keeping: two of the four items state TRUE things. Torsion balances do
   return nulls, and pendulum apparatus really is sensitive to its mounting. REFUTED
   ("contradicted by a specific measurement") would be right for 232 and 398 and wrong for
   250 and 249. What fails across all four is the inference, which is never made — which
   is exactly what NOT DEMONSTRATED means. The refutation states this in its own voice so
   a defender cannot mine the chip. No verdict_challenge filed.

10. DEFECTS IN OUR OWN RECORD, reported up, NOT edited here (this agent owns one file).
    See record_problems in the handoff. Summary: the cluster NAME asserts a single claim
    the four items do not share and that is false of two of them; the cluster NOTE ("No
    specific published measurement is cited by the list") is true of all 461 items and so
    carries no A15-specific information, and it renders as the basis line under the
    verdict chip; A13's record would be improved by the ENaG locator found in §2; and item
    249 is grammatically ambiguous in a way the cluster name silently resolves.
"""

ENTRY = {

"A15": dict(

    tldr=("Gravimeters and pendulum clocks are not steady. Measured gravity is 0.53% stronger "
          "at the pole than at the equator; a pendulum clock taken to Cayenne in 1672 lost "
          "2m 28s a day; a 1929 pendulum clock registered the Moon's tidal pull on itself. The "
          "torsion-balance null is real, and it is the wrong kind of null: Eötvös's balance can "
          "detect anything at all only because the Earth turns, so on a stationary Earth it is "
          "not a null result but no experiment. We looked for whoever argued this first and did "
          "not find them — and Galileo Was Wrong, which prints the torsion-balance null a "
          "defender would want, calls that experiment incapable of detecting anything."),

    passage=None,

    untraceable="""<p>Four one-line items, three instruments, and no author. The search for one was run in full and it ended in an answer rather than a shrug, so here is exactly what was read and where it stopped &mdash; including the places a reader who knows better should push back.</p>

<p><strong>The specimen cites nothing.</strong> Re-fetched 2026-08-10: the page is headed &ldquo;THE EARTH IS FLAT AND NON ROTATING&rdquo; and carries 461 numbered lines with no footnote, link or attribution against any of them. Items 232, 249, 250 and 398 read in their entirety: <em>&ldquo;Gravimeter constancy.&rdquo; &ldquo;Pendulum building sensitivity.&rdquo; &ldquo;Torsion balance null variation.&rdquo; &ldquo;Pendulum clocks stable.&rdquo;</em> That is the whole of the argument as published.</p>

<p><strong>The Victorian trunk of the tradition.</strong> Rowbotham&rsquo;s <em>Zetetic Astronomy: Earth Not a Globe!</em> (1865 first book edition, Project Gutenberg transcription #69892) returns 78 hits for &ldquo;pendulum&rdquo; and none at all for &ldquo;gravimet-&rdquo;, &ldquo;torsion&rdquo; or &ldquo;Cavendish&rdquo;. Carpenter&rsquo;s <em>One Hundred Proofs</em> (1885, Gutenberg #55387) returns seven for &ldquo;pendulum&rdquo;, all of them proof 73 and the index line, and zero for the other three words. Both pendulum discussions are about Foucault precession, which this review scores at <a href="#ARG-A06">ARG-A06</a>.</p>

<p><strong>And the seventy-eight hits point the wrong way for the list.</strong> This is the finding worth the search. In the 1865 edition, in the sequence of anti-rotundity arguments that follows the Polaris passage in Section&nbsp;I, Rowbotham takes up precisely the phenomenon item&nbsp;398 denies &mdash; and concedes it. He writes that &ldquo;a pendulum vibrates more rapidly in the northern region than at the equator&rdquo;, and prints the figures: &ldquo;the length of a seconds pendulum at the equator is 39,027 inches, and 39,197 inches at the north pole&rdquo; (the commas are the printer&rsquo;s; read 39.027 and 39.197). His objection is not that the variation is absent. It is that the inference to a spheroid &ldquo;proceeds upon the <em>assumption</em> that the Earth <em>is</em> a globe having a &lsquo;centre of attraction of gravitation&rsquo;&rdquo;, and that &ldquo;it should also be first proved that <em>no other</em> cause could operate&rdquo;. He then supplies two other causes: thermal expansion of the rod, and the density of the air. <strong>The founding text of the flat-earth tradition agrees that pendulum clocks are not stable, and argues about why.</strong> The refutation above answers that argument, at its own strength, in his own numbers. It is the nearest thing to a source this cluster has, and it is its negation &mdash; which is why nobody is credited here, and why item&nbsp;398 has not been moved into <a href="#ARG-A13">ARG-A13</a>, where Rowbotham&rsquo;s real argument lives.</p>

<p><strong>The modern compilers.</strong> Dubay&rsquo;s <em>200 Proofs Earth Is Not a Spinning Ball</em> (archive.org item <code>200proofsearthisnotaspinningballericdubay</code>, djvu text) gives nine hits for &ldquo;pendulum&rdquo;, all inside proof 140, and none for &ldquo;gravimet-&rdquo;, &ldquo;torsion&rdquo; or &ldquo;Cavendish&rdquo;. Proof 140 is a Foucault claim &mdash; the swing &ldquo;depends on 1) the initial force beginning its swing and, 2) the ball-and-socket joint used&rdquo; &mdash; which is the honest ancestor of item&nbsp;249 on one reading of that item, and is answered in &sect;3 of the refutation. Edward Hendrie&rsquo;s <em>The Greatest Lie on Earth</em> (2016), the largest post-2015 compendium with a physics apparatus, returns zero hits for all five of &ldquo;pendulum&rdquo;, &ldquo;Foucault&rdquo;, &ldquo;gravimeter&rdquo;, &ldquo;torsion&rdquo; and &ldquo;Cavendish&rdquo; in the archive.org OCR text of that scan.</p>

<p><strong>The geocentric side, where the instruments actually appear.</strong> Sungenis and Bennett&rsquo;s <em>Galileo Was Wrong</em> is the one place in this literature where torsion balances are discussed at length, and it discusses them twice, in opposite directions from the list. In Vol.&nbsp;I, chapter&nbsp;12 &mdash; a catalogue of ether-drift experiments, each with a &ldquo;Geocentrism&rsquo;s Response&rdquo; appended &mdash; Trouton&ndash;Noble 1903 appears at printed p.&nbsp;855: a charged capacitor hung on a torsion fibre, which returned a null for the Earth&rsquo;s motion. That is the only torsion-balance null on point anywhere in the reachable geocentric corpus, and <strong>the book declines to bank it</strong>. Its response, on p.&nbsp;856, reads in full: &ldquo;Only light and gases show ether effects; the experiment was incapable of achieving ether detection unless a charged gas is used between the plates.&rdquo; The same section records that the null &ldquo;was repeated in experiments by Chase in 1927 and Hayden in 1994&rdquo; and that such results &ldquo;are now thought to be consistent with Special Relativity&rdquo;. Meanwhile Vol.&nbsp;II runs the opposite argument: at printed p.&nbsp;27 and again in Appendix&nbsp;1 at p.&nbsp;640 it cites torsion-balance and pendulum <em>anomalies</em> &mdash; Long&rsquo;s 1976 inverse-square discrepancy &ldquo;to the tune of 0.37%&rdquo;, the eclipse pendulum measurements at <em>Physical Review</em> D3, 823, the Holding and Tuck mineshaft determination of <em>G</em> &mdash; as positive evidence for a LeSagean geocentric dynamics. Searching the OCR text of both volumes for &ldquo;gravimeter&rdquo; and &ldquo;gravimetr-&rdquo; returns zero hits in either.</p>

<p><strong>The one live modern argument, which is not this one.</strong> The Flat Earth Society wiki does have pages on gravimetry, and their claim is worth stating accurately because it is better than item&nbsp;232. It is not that gravimeters read constant. It is that they are long-period seismometers whose published output is reached through a stack of modelled corrections &mdash; latitude, free-air, terrain &mdash; and the page quotes a training manual to the effect that &ldquo;Gravimeters do not give direct measurements of gravity; rather, a meter reading is taken which is then multiplied by an instrumental calibration factor.&rdquo; That is the circularity charge, it is the strongest version of the position, and it is answered in &sect;5 of the refutation rather than here.</p>

<p><strong>Why this is not filed as older than the movement.</strong> That state records where an <em>argument</em> came from, and it needs an old text that contains the argument. Instruments this sensitive did not exist before the movement did: the superconducting gravimeter dates from the 1960s, the Cavendish balance from 1798, the Eötvös torsion balance from the 1890s. There is nothing upstream to inherit from.</p>

<p><strong>An honest note on our limits.</strong> <em>No source found</em> means we did not find one, not that none exists. Four noun phrases with no verb between them can begin in a livestream, a comment thread or a caption, leaving nothing to search; and the corpora above were read as OCR transcriptions rather than print copies, so a hit could have been missed to a scanning error. A reader who can point us at someone who actually made this argument &mdash; in print, on air, anywhere datable &mdash; will improve this entry, and we will publish the correction.</p>""",

    steelman=dict(
        description="""<p><strong>SURFACE (weak &mdash; do not use).</strong> &ldquo;Gravimeters vary all the time, so the items are simply false.&rdquo; This wins a quarter of the argument and loses the rest in public. It is true of item&nbsp;232 and item&nbsp;398. It is <em>not</em> true of item&nbsp;250, because torsion-balance tests of the equivalence principle really do return nulls and are celebrated for it; and it is not true of item&nbsp;249 on its natural reading, because a Foucault pendulum really is sensitive to how it is hung and how it is started. Two of the four sentences in this cluster are correct as written. Anyone who opens by calling all four false has handed a defender two free recoveries.</p>

<p><strong>DEEPER.</strong> The nulls are extraordinary and they are real. A continuously rotating torsion balance at Washington compared the fall of beryllium and titanium and found the E&ouml;tv&ouml;s parameter to be &eta; = (0.3 &plusmn; 1.8) &times; 10<sup>&minus;13</sup>, with differential accelerations in <em>any</em> space-fixed direction bounded below 8.8 &times; 10<sup>&minus;15</sup> m/s&sup2;. That is one of the most precise mechanical measurements ever made, and it found nothing. A defender who says only this has said nothing a physicist would contest.</p>

<p><strong>KERNEL.</strong> The strongest form drops the false items and keeps the true one, and it is genuinely uncomfortable: <em>the most sensitive mechanical instruments ever built have been pointed at this question for a century and a quarter, and the headline result is a null. E&ouml;tv&ouml;s got a null in 1909. Trouton and Noble got a null in 1903 and Hayden got it again in 1994. The rotating balance gets a null today at one part in 10<sup>13</sup>. And a gravimeter sitting in a vault registers precisely nothing attributable to a planet supposedly travelling at 30 kilometres a second. You keep telling us the Earth is racing through space. The best instruments in the building cannot feel it.</em> Every factual component of that is correct, and the last sentence is correct in a way this page has to concede in its own voice rather than talk around.</p>""",
        why_it_doesnt_save_claim="""<p>Because the nulls are nulls <em>of the wrong quantity</em>, and one of them is a null that only exists because the Earth spins.</p>

<p><strong>Take the gravimeter first, and concede it fully.</strong> A gravimeter shows no signal from the Earth&rsquo;s orbital velocity, and it should not. The Earth is in free fall around the Sun: the Sun&rsquo;s pull at our distance is 5.9 &times; 10<sup>&minus;3</sup> m/s&sup2;, and the orbital acceleration cancels it to first order everywhere in the laboratory. What survives is the gradient across the Earth &mdash; the solar tide, about 5 &times; 10<sup>&minus;7</sup> m/s&sup2;, roughly 50 &micro;Gal &mdash; and gravimeters measure that, twice a day, on schedule. A steady velocity produces no force on anything; that has been the answer since Galileo put the sailor below decks, and <a href="#ARG-A17">ARG-A17</a> scores it separately. Insisting an instrument should register a velocity is asking it to violate the principle that makes it work.</p>

<p><strong>Now the torsion balance, which is where the true thing points the other way.</strong> E&ouml;tv&ouml;s&rsquo;s balance compares two bodies of different composition hanging on one beam. It can distinguish them <em>only</em> because gravity pulls toward the Earth&rsquo;s centre while the centrifugal effect of rotation pulls perpendicular to the spin axis, so the two do not act along the same line, and a difference in the ratio of inertial to gravitational mass would twist the beam. The size of that twist is set by the <em>horizontal</em> component of the centrifugal acceleration, &omega;&sup2;<em>R</em>&nbsp;cos&nbsp;&phi;&nbsp;sin&nbsp;&phi;, which at the latitude of Budapest is 0.0339 &times; cos&nbsp;47.5&deg; &times; sin&nbsp;47.5&deg; = 0.0169 m/s&sup2;, about 1.7 &times; 10<sup>&minus;3</sup> of <em>g</em> (recomputed here 2026-08-10). Set the Earth&rsquo;s rotation to zero and that term is identically zero. The beam has nothing to twist it, in either direction, whatever the test masses are made of. <strong>On a stationary Earth the E&ouml;tv&ouml;s experiment is not a null result. It is no experiment.</strong> The movement&rsquo;s favourite instrument is sensitive at all only on the hypothesis it is being cited against.</p>

<p>The modern version keeps the same dependence and adds a second one. The rotating balance quotes its bound on differential accelerations &ldquo;in any direction&rdquo; in a <em>space-fixed</em> frame &mdash; one defined by the stars &mdash; and the route from the laboratory to that frame is a rotation at the Earth&rsquo;s rate. The null is stated in coordinates that presuppose the turning the item denies.</p>""",),

    refutation="""<p><strong>What this verdict ranges over, stated before anything else.</strong> Not &ldquo;these instruments are useless&rdquo;, and not &ldquo;all four sentences are false&rdquo;. Two of the four are true as written: torsion-balance tests of the equivalence principle do return nulls, and pendulum apparatus is genuinely sensitive to how it is built and started. The two that are false &mdash; <em>gravimeter constancy</em> and <em>pendulum clocks stable</em> &mdash; are contradicted below by named measurements. What fails across all four is the step from an instrument reading to a conclusion about the Earth, and that step is never taken anywhere in the specimen. Four noun phrases are not an argument, which is why the verdict is <em>not demonstrated</em> rather than <em>refuted</em>: there is no inference here to be wrong. REFUTED was weighed and rejected for exactly the reason a defender would give &mdash; it would be right about half this cluster and wrong about the other half.</p>

<h4>1. Gravimeters are not constant, and the largest thing that moves them is the Earth&rsquo;s spin</h4>

<p>Start with the number every gravity survey begins from. The International Gravity Formula puts <em>g</em> at 9.7803253359 m/s&sup2; on the equator and 9.8321849378 m/s&sup2; at the pole &mdash; a spread of <strong>0.53%</strong>, which is thousands of times the resolution of a field instrument. Of that, the centrifugal term accounts for &omega;&sup2;<em>a</em> = (7.292115 &times; 10<sup>&minus;5</sup>)&sup2; &times; 6,378,137 = 0.0339 m/s&sup2;, or 0.347% of <em>g</em> (recomputed here 2026-08-10); the remainder comes from the equatorial bulge, which is itself a consequence of the rotation. <a href="#ARG-A13">ARG-A13</a> scores the bulge on its own.</p>

<p>On top of that sits a signal nobody can operate a gravimeter without modelling. The solid Earth tide swings local gravity by <strong>100 to 300 &micro;Gal depending on the phase of the Moon</strong>, twice a day, every day. It is not a delicate inference from a specialist instrument: a chip-scale MEMS gravimeter, a device etched in silicon, tracked nineteen days of it with a correlation of 0.975 against the theoretical tide. The theoretical tide is computed from the positions of the Moon and the Sun. A reading that agrees with an ephemeris to that tolerance is the opposite of a constant.</p>

<p>And then there is the signal that settles the matter, because it exists for one reason only. The Earth&rsquo;s rotation axis wanders within the planet &mdash; the Chandler wobble, about 435 days. As it wanders, the centrifugal pseudo-force at a fixed station changes, and the station&rsquo;s gravity changes with it. Superconducting gravimeters of the Global Geodynamics Project network see this, and the quantity they report is a measured admittance rather than an assumed one: stacking decade-long records gives a gravimetric factor at the Chandler frequency of <strong>1.118 &plusmn; 0.016</strong> in amplitude with a phase of &minus;0.45&deg; &plusmn; 0.66&deg;, which the authors note is &ldquo;smaller in amplitude than expected&rdquo;. Two things follow. The pole tide is a gravity signal generated by the variation of a centrifugal term, so it cannot exist at all on a non-rotating Earth. And the number came out <em>disagreeing</em> with the prediction, which is not what a fitted parameter does.</p>

<h4>2. Pendulum clocks: the instability is the founding datum of the whole subject</h4>

<p>In 1672 Jean Richer took a pendulum clock, regulated in Paris, to Cayenne at about five degrees north. Newton reported that it went &ldquo;slower than it ought in respect of the mean motion of the sun at the rate of 2<sup>m</sup> 28<sup>s</sup> a day&rdquo;, and that to beat seconds there the pendulum had to be made 1.25 lignes &mdash; 2.256 mm &mdash; shorter than at Paris. Huygens read it as the centrifugal effect of the Earth&rsquo;s rotation reducing apparent gravity near the equator; Newton read it as the equatorial bulge. Both readings are readings of a spinning planet, and the disagreement between them is the reason the eighteenth century sent expeditions to Lapland and Peru. Item 398 asserts the stability of an instrument whose <em>instability</em> is the single observation from which the figure of the Earth was first inferred.</p>

<p>By 1818 the effect was metrology. Kater&rsquo;s reversible pendulum gave the seconds pendulum at London, at sea level, at 62&nbsp;&deg;F, swinging in vacuum, as 39.1386 inches, with a scatter from the mean of 0.00028 inches &mdash; a precision in <em>g</em> of about 7 mGal. Pendulum parties then carried Kater instruments from the tropics to the Arctic for the express purpose of measuring how much the reading changed with latitude, and published the ellipticity they got out of it.</p>

<p><strong>And the finest pendulum clocks felt the Moon.</strong> In 1929, before spring gravimeters were measuring Earth tides at all, a Shortt&ndash;Synchronome free-pendulum clock was run against a timing system with a least count of a millisecond, and Brown and Brouwer&rsquo;s analysis of the record found a diurnal sinusoid of amplitude 0.097 &times; 10<sup>&minus;3</sup> s and a semidiurnal one of 0.161 &times; 10<sup>&minus;3</sup> s &mdash; against a predicted semidiurnal amplitude of 0.178 &times; 10<sup>&minus;3</sup> s, ten per cent larger and almost exactly in phase. Duncan Agnew&rsquo;s history of these measurements draws the conclusion plainly: clock-based systems, though noisier than spring gravimeters, &ldquo;were an early form of an absolute gravimeter that could indeed observe Earth tides&rdquo;. A pendulum clock detected the tidal pull of the Moon on its own bob, in 1929, at the level of a sixth of a millisecond. That is the instrument item&nbsp;398 calls stable.</p>

<h4>3. &ldquo;Pendulum building sensitivity&rdquo; is true, and it is the field&rsquo;s own point</h4>

<p>Item&nbsp;249 admits two readings &mdash; that pendulums are sensitive to the building they hang in, or that pendulums can be built to great sensitivity &mdash; and the first is the one with a tradition behind it. Dubay&rsquo;s proof 140 says the behaviour of a Foucault pendulum &ldquo;depends on 1) the initial force beginning its swing and, 2) the ball-and-socket joint used which most-readily facilitates circular motion over any other&rdquo;, and Carpenter&rsquo;s proof 73 makes the Victorian version. On the physics, they are right, and we are not going to pretend otherwise. A Foucault pendulum &ldquo;requires care to set up because imprecise construction can cause additional veering which masks the terrestrial effect&rdquo;; a geometrical imperfection or elasticity in the wire can beat two horizontal modes against each other; an elliptical swing precesses on its own. This is why the bob is released by burning a thread rather than by hand, and why a Charron ring is fitted to bleed off the ellipticity.</p>

<p>What follows is the opposite of what the item wants. A demonstration whose systematics you have to engineer away is a <em>demonstration</em>, and the movement is entitled to say so. The measurement is elsewhere, and it has no thread and no bearing: a ring-laser gyroscope has no moving parts, and the G instrument at Wettzell tracks the Earth&rsquo;s rotation rate to below one part in 10<sup>9</sup>, resolving length-of-day variation and polar motion in agreement with VLBI. <a href="#ARG-A07">ARG-A07</a> and <a href="#ARG-A19">ARG-A19</a> follow that through. Conceding that a museum pendulum is fiddly costs this page nothing, because the pendulum stopped being the evidence decades ago.</p>

<p>There is also an internal tension the list never resolves. Item&nbsp;11 of the same specimen &mdash; scored at <a href="#ARG-A06">ARG-A06</a> &mdash; treats the Foucault precession as a real, regular phenomenon requiring an explanation, and explains it by a rotating firmament. Item&nbsp;249, read the first way, treats the same precession as an artefact of the mounting. The list needs the precession to be real when it is being reassigned to the sky and unreal when it is being dismissed.</p>

<h4>4. The torsion-balance null is real. It is also the wrong null, and it is one the geocentric literature has already spent</h4>

<p>Torsion balances return nulls, and the best ones are magnificent. A continuously rotating balance comparing beryllium and titanium reports &eta; = (0.3 &plusmn; 1.8) &times; 10<sup>&minus;13</sup> and bounds differential accelerations in any space-fixed direction below 8.8 &times; 10<sup>&minus;15</sup> m/s&sup2;. Nobody disputes the null; the question is what it is a null <em>of</em>. It is a null of a <em>difference</em> between two materials, and the channel through which that difference could show up is the horizontal component of the centrifugal acceleration &mdash; 1.7 &times; 10<sup>&minus;3</sup> of <em>g</em> at E&ouml;tv&ouml;s&rsquo;s latitude, and exactly zero if the Earth does not turn. Cite the null and you have cited an instrument whose sensitivity is a function of &omega;.</p>

<p>Meanwhile the one torsion-balance experiment in this literature that <em>was</em> aimed at the Earth&rsquo;s motion has been disclaimed by the people citing it. Trouton and Noble hung a charged capacitor on a torsion fibre in 1903 to look for a turning couple from motion through the ether, and found none. <em>Galileo Was Wrong</em> Vol.&nbsp;I sets the experiment out at printed p.&nbsp;855 and answers it on p.&nbsp;856 in its own voice: &ldquo;Only light and gases show ether effects; the experiment was incapable of achieving ether detection unless a charged gas is used between the plates.&rdquo; A null from an apparatus your own source calls incapable is not evidence, and the book is right to say so; the same section notes the result &ldquo;was repeated in experiments by Chase in 1927 and Hayden in 1994&rdquo; and is &ldquo;now thought to be consistent with Special Relativity&rdquo;.</p>

<p><strong>Worse for the item, the same authors argue the reverse elsewhere in the same work.</strong> Vol.&nbsp;II&rsquo;s chapter on the cause of gravity, at printed p.&nbsp;27, and its Appendix&nbsp;1, at p.&nbsp;640, recruit torsion-balance and pendulum <em>anomalies</em> as positive evidence for a LeSagean geocentric dynamics: Long&rsquo;s 1976 report of a discrepancy in the inverse-square law &ldquo;to the tune of 0.37%&rdquo;, the eclipse pendulum measurements at <em>Physical Review</em> D3, 823, the Holding and Tuck mineshaft determination of <em>G</em>. A tradition cannot run &ldquo;the sensitive instruments show nothing, which proves us right&rdquo; and &ldquo;the sensitive instruments show anomalies, which proves us right&rdquo; on the same page of the same shelf.</p>

<p>For completeness, and because it is the honest way to hold this ground: the most interesting claim ever made linking torsion balances to the Earth&rsquo;s rotation ran in the geocentrists&rsquo; favour and did not survive. Anderson and colleagues reported in 2015 that published measurements of <em>G</em> oscillate with a 5.9-year period in phase with length-of-day variations. Schlamminger, Gundlach and Newman showed that corrections and additions to the <em>G</em> data &ldquo;significantly weaken the correlation&rdquo;, and Pitkin&rsquo;s Bayesian reanalysis found a model with an extra unknown noise component favoured over any sinusoid by factors of order e<sup>30</sup>. We would have had to publish that had it held. It did not.</p>

<h4>5. The circularity charge, which is the best objection here and is answerable</h4>

<p>The strongest version of item&nbsp;232 is not in the specimen at all; it is on the Flat Earth Society&rsquo;s own wiki, and it runs: a raw gravimeter reading means nothing until you have applied a latitude correction, a free-air correction, a terrain correction and a drift correction, every one of them derived from the model whose truth is in question. You are reading the globe back out of numbers you put the globe into.</p>

<p>That deserves a direct answer, and there is one. <strong>Take the E&ouml;tv&ouml;s correction, which is the rotation term applied to every gravity measurement made from a moving platform.</strong> Its size is 2&omega;<em>v</em>&nbsp;cos&nbsp;&phi;: at 45&deg; latitude, a ship steaming east at ten knots reads 53 mGal light, and an aircraft at 200 m/s reads about 2,060 mGal light (recomputed here 2026-08-10). Marine and airborne surveys work at the milligal level, so this term is tens to thousands of times the signal being mapped. Set &omega; to zero and it vanishes identically, and every marine gravity survey ever flown or sailed would need no such term at all.</p>

<p>Now the part that answers the circularity. <strong>The E&ouml;tv&ouml;s effect was not imposed as a correction. It was found as an unexplained discrepancy.</strong> A German team from the Geodetic Institute of Potsdam took gravity measurements aboard ships in the Atlantic, Indian and Pacific in the early 1900s, and the readings came out lower when the vessel was moving east and higher when it was moving west. E&ouml;tv&ouml;s identified the cause, and in 1908 two ships were run in opposite directions on the Black Sea to test it. The prediction held. That is the shape of a discovery, not of a fitted parameter: the data arrived first, from people who were not looking for it, and the term that explains it is proportional to the rate at which the Earth turns.</p>

<h4>6. What is conceded, without decoration</h4>

<p>A gravimeter shows nothing attributable to the Earth&rsquo;s 30 km/s orbital velocity. That is true, it will stay true however good the instruments get, and it is a prediction of the moving-Earth account rather than a difficulty for it &mdash; the laboratory is in free fall, the Sun&rsquo;s 5.9 &times; 10<sup>&minus;3</sup> m/s&sup2; pull is cancelled by the orbital acceleration, and only the gradient survives. The same non-discrimination applies to a uniform velocity of any kind, which is <a href="#ARG-A17">ARG-A17</a>&rsquo;s subject and was Galileo&rsquo;s in 1632. What the instruments <em>do</em> see is rotation, and they see it four separate ways: in the 0.53% latitude gradient of <em>g</em>, in the pole tide as the spin axis wanders, in the E&ouml;tv&ouml;s term on every moving platform, and in the very existence of a signal channel in the E&ouml;tv&ouml;s balance. Three sentences of this cluster describe instruments that register the Earth&rsquo;s rotation, and one describes an instrument that cannot register a velocity because nothing can.</p>""",

    advocate=dict(
        best_defense=(
            "Four moves, and the first one is fatal to your own method. (1) You have just "
            "spent several thousand words refuting a phrase that, by your own admission, "
            "nobody wrote. Your standing rule is that a refutation aimed at the list's "
            "compression rather than a source's own wording is a critical failure — the "
            "same error we are accused of. You could not find a source. By your rule you "
            "should have stopped. (2) Your Rowbotham demolition is a bait and switch. You "
            "concede in your own untraceable block that the passage is A13's material, then "
            "spend the best arithmetic on this page attacking it here, so that a reader who "
            "skims sees Rowbotham crushed under a heading he has nothing to do with. "
            "(3) The Eötvös point is circular and you have dressed it as a kernel. You "
            "compute a centrifugal term by assuming the rotation, then announce that the "
            "term proves the rotation. On our cosmology the same relative motion exists "
            "between the balance and the heavens, and whatever produces the diurnal "
            "asymmetry produces it in our frame too — you have redescribed the geometry, "
            "not tested it. (4) And you have conceded the load-bearing point yourself, in "
            "bold: the finest gravimetric instruments ever built detect nothing whatever of "
            "a 30 km/s orbit. Your answer is that free fall hides it. Convenient. Every "
            "positive effect you list — tides, latitude gradient, pole tide — is equally "
            "available to a stationary Earth beneath a moving heaven, since a tide only "
            "needs relative motion between Earth and Moon. So your four ways of seeing "
            "rotation reduce to one contested definition of what is turning, and your "
            "verdict admits that half our items are true."),
        survives=4,
        preemptive=(
            "Four, driven by moves (1) and (3); (2) is fair and has already been fixed in "
            "the text, and (4) is answered but must never be softened. Taking them in order. "
            "MOVE 1 is the serious one and the body must meet it head-on rather than in a "
            "footnote: the hedge rule's second clause exists precisely for this case — the "
            "compressed version is what circulates, so the obligation is to answer the "
            "argument AND publish the gap, and where there is no upstream sentence the gap "
            "IS the finding. The entry discharges this by (a) answering the strongest real "
            "argument in the tradition at full strength — Rowbotham's reattribution, in "
            "Rowbotham's own numbers — and (b) publishing, in the untraceable block, that "
            "the nearest texts argue for anomalies rather than nulls and that the one "
            "on-point torsion-balance null is disclaimed by the book that prints it. If an "
            "editor ever trims the untraceable block to a sentence, this defence becomes "
            "unanswerable. MOVE 2 is why the untraceable block says in terms that the "
            "Rowbotham passage is A13's material and is the item's NEGATION, and why item "
            "398 has explicitly not been moved into A13. Keep both sentences. MOVE 3 needs "
            "the answer stated in our voice and it is not in the body strongly enough: the "
            "Eötvös point is not 'centrifugal force exists, therefore rotation'. It is "
            "conditional and it is about instrument design — IF the Earth does not rotate, "
            "the balance has no channel through which a composition-dependent effect could "
            "produce a torque, so the geocentrist is quoting a null from an apparatus that, "
            "on his own cosmology, was never able to return anything else. A defender who "
            "answers 'the heavens turn instead, and that produces the same horizontal term' "
            "has conceded that the term is real and non-zero, which is all this argument "
            "needs; that trade is ARG-R01's and is scored there. MOVE 4: do not retreat one "
            "inch. The concession that gravimetry cannot see orbital velocity stays in bold "
            "in §6, in our own voice, because a defender who extracts it from us later gets "
            "to run the whole section as a reluctant admission. And do not answer the "
            "'tides work either way' line by disputing it — it is correct, and the four "
            "rotation signals in §6 were chosen precisely because the tide is not among "
            "them: the latitude gradient, the pole tide, the Eötvös term and the balance's "
            "sensitivity all carry ω explicitly and all go to zero with it."),
    ),

    straw_man=dict(
        identified=True,
        detail=("Two of the four items are framed as difficulties for a moving Earth by "
                "presupposing predictions that nobody has made. “Torsion balance null "
                "variation” is offered as though the moving-Earth account predicted that a "
                "torsion balance would swing in step with the Earth's motion; it predicts the "
                "opposite, and has since 1905 — a uniform velocity produces no force on "
                "anything, which is why the null is quoted in the physics literature as a "
                "confirmation rather than a puzzle. “Gravimeter constancy” carries the same "
                "implication in reverse, that the globe model expects wild gravimeter "
                "excursions from the planet's motion. What the model expects is a 0.53% "
                "latitude gradient, a tide of 100–300 microgal, and a pole tide — all of "
                "which are what the instruments show. The imagined opponent who thinks a "
                "gravimeter should register 30 km/s does not exist.")),

    compression=dict(
        assessed="no_source", drifted=None, list_phrasing=None, source_wording=None,
        drift_type=None,
        note=("There is no original to hold these four lines against, and the search that "
              "established it is set out in full under &ldquo;No original to quote&rdquo; above: "
              "the specimen carries no citation for any of its 461 items; Rowbotham 1865 and "
              "Carpenter 1885 discuss pendulums only as Foucault precession, and neither "
              "&ldquo;gravimet-&rdquo; nor &ldquo;torsion&rdquo; nor &ldquo;Cavendish&rdquo; is "
              "located in the full text of either; Dubay&rsquo;s <em>200 Proofs</em> is the same "
              "picture; Hendrie&rsquo;s 2016 compendium returns zero hits for all five terms in "
              "the OCR text of that scan; and both volumes of <em>Galileo Was Wrong</em> return "
              "zero hits for &ldquo;gravimeter&rdquo;. <strong>The hedge rule has nothing to bite "
              "on, and that is itself the result</strong> &mdash; where an argument has an author "
              "we can show the list hardening a hedge, and here there is no hedge because there "
              "is no sentence upstream of the fragment.<br><br>"
              "<strong>But the search returned something sharper than a blank, and it runs in "
              "three directions at once.</strong> <em>On the pendulum:</em> the founding text of "
              "the tradition states the reverse of item&nbsp;398. Rowbotham concedes that the "
              "seconds pendulum is longer at the pole than at the equator, prints both figures, "
              "and argues about the <em>cause</em> rather than the fact. <em>On the torsion "
              "balance:</em> the only null on point in the reachable geocentric corpus &mdash; "
              "Trouton&ndash;Noble 1903, at <em>Galileo Was Wrong</em> Vol.&nbsp;I printed "
              "p.&nbsp;855 &mdash; is disclaimed on the next page by the book that reports it, as "
              "an experiment &ldquo;incapable of achieving ether detection&rdquo;. <em>And on the "
              "instruments generally:</em> the same authors&rsquo; Vol.&nbsp;II argues at printed "
              "pp.&nbsp;27 and 640 that torsion balances and pendulums show anomalous "
              "<em>variation</em>, and treats that as evidence for geocentrism. So the compressed "
              "items are not firmer versions of something upstream; on three of four they point "
              "where the upstream literature declines to go.<br><br>"
              "One further gap belongs here rather than in the refutation, because it is a "
              "property of the compression itself: <em>&ldquo;Pendulum building "
              "sensitivity&rdquo;</em> is four words that will not resolve. It reads either as "
              "&ldquo;pendulums are sensitive to the building&rdquo; &mdash; the Dubay and "
              "Carpenter claim, which is true and which the refutation grants at &sect;3 &mdash; "
              "or as &ldquo;pendulums can be built to great sensitivity&rdquo;, which is the "
              "reading our own cluster name silently adopts. An item that cannot be pinned to one "
              "assertion cannot have drifted from a source, and cannot be answered without "
              "answering both. &sect;3 answers both.")),

    verdict_challenge=dict(challenged=False, proposed_verdict=None, reasoning=None),

    people=[],
    related=["A06", "A07", "A13", "A17", "A19", "A23", "B09", "R08"],

    sources=[
        dict(label="The specimen list — withthesun33.com/about-1, items 232, 249, 250, 398; "
                   "re-fetched 2026-08-10, no citation attached to any of the 461 items",
             url="https://withthesun33.com/about-1"),
        dict(label="Rowbotham (“Parallax”), Zetetic Astronomy: Earth Not a Globe! (Simpkin, "
                   "Marshall & Co., 1865) — Project Gutenberg #69892. Section I: the seconds "
                   "pendulum “39,027 inches” at the equator and “39,197 inches” at the pole, the "
                   "temperature table (84.2 °F to 0 °F) from Phillips's Million of Facts, and "
                   "the Noad figure 39.13929 in. “in vacuo … at the temperature of 62°”",
             url="https://www.gutenberg.org/cache/epub/69892/pg69892.txt"),
        dict(label="Carpenter, One Hundred Proofs That the Earth Is Not a Globe (1885) — Project "
                   "Gutenberg #55387; proof 73 is the Foucault-pendulum claim",
             url="https://www.gutenberg.org/ebooks/55387"),
        dict(label="Dubay, 200 Proofs Earth Is Not a Spinning Ball — archive.org item "
                   "200proofsearthisnotaspinningballericdubay; proof 140 on the Foucault "
                   "pendulum's dependence on “the initial force beginning its swing” and “the "
                   "ball-and-socket joint used”",
             url="https://archive.org/details/200proofsearthisnotaspinningballericdubay"),
        dict(label="Sungenis & Bennett, Galileo Was Wrong Vol. I — archive.org item "
                   "GallileoWasWrong. Ch. 12, Trouton–Noble 1903 at printed p. 855; the "
                   "“Geocentrism's Response” calling the experiment “incapable of achieving "
                   "ether detection” at p. 856",
             url="https://archive.org/stream/GallileoWasWrong/Gallileo%20was%20wrong_djvu.txt"),
        dict(label="Sungenis & Bennett, Galileo Was Wrong Vol. II — archive.org item "
                   "GalileoWasWrongTheChurchSungenisRobertA.Bennett4276. Ch. 7 at printed p. 27 "
                   "(Cavendish torsion balance, Long 1976, the eclipse pendulums at Phys. Rev. "
                   "D3 823) and Appendix 1 at p. 640 (“systematic discrepancies of 0.37%”)",
             url="https://archive.org/stream/GalileoWasWrongTheChurchSungenisRobertA.Bennett4276/Galileo%20Was%20Wrong_%20The%20Church%20%20-%20Sungenis,%20Robert%20A.%20&%20Bennett,_4276_djvu.txt"),
        dict(label="Edward Hendrie, The Greatest Lie on Earth (2016) — archive.org OCR text "
                   "searched 2026-08-10 for pendulum, Foucault, gravimeter, torsion and "
                   "Cavendish; zero hits for each",
             url="https://archive.org/details/the-greatest-lie-on-earth-proof-that-our-world-is-not-a-moving-globe"),
        dict(label="The Flat Earth Wiki, “Gravimetry” — the strongest version of the gravimeter "
                   "objection: gravimeters as long-period seismometers, and “Gravimeters do not "
                   "give direct measurements of gravity”",
             url="https://wiki.tfes.org/Gravimetry"),
        dict(label="The Flat Earth Wiki, “Variations in Gravity” — the companion page",
             url="https://wiki.tfes.org/Variations_in_Gravity"),
        dict(label="Jean Richer's 1672 Cayenne observation — Newton's report that the clock ran "
                   "“slower than it ought … at the rate of 2m 28s a day”, the 1.25-ligne "
                   "(2.256 mm) shortening, and the Huygens/Newton disagreement over the cause",
             url="https://en.wikipedia.org/wiki/Jean_Richer"),
        dict(label="Kater's pendulum — the 1818 London determination, 39.1386 in. at sea level, "
                   "62 °F, in vacuum, scatter 0.00028 in. (about 7 mGal), and the corrections "
                   "applied for arc, temperature, buoyancy and altitude",
             url="https://en.wikipedia.org/wiki/Kater%27s_pendulum"),
        dict(label="Duncan C. Agnew, “Time and tide: pendulum clocks and gravity tides”, Hist. "
                   "Geo Space Sci. 11:215–224 (2020) — the 1929 Shortt clock, Brown & Brouwer "
                   "(1931) diurnal 0.097×10⁻³ s and semidiurnal 0.161×10⁻³ s against a predicted "
                   "0.178×10⁻³ s, and clocks as “an early form of an absolute gravimeter”",
             url="https://hgss.copernicus.org/articles/11/215/2020/"),
        dict(label="A 19-day Earth tide measurement with a MEMS gravimeter, Sci. Rep. 12 (2022) — "
                   "tidal amplitude “between around 100 μGal and 300 μGal, depending on the "
                   "monthly phase of the Moon”; correlation 0.975 with the theoretical tide",
             url="https://www.nature.com/articles/s41598-022-16881-1"),
        dict(label="Estimation of the gravimetric pole tide by stacking long time-series of GGP "
                   "superconducting gravimeters, Geophys. J. Int. 205:77 (2016) — gravimetric "
                   "factor 1.118 ± 0.016 at the Chandler frequency, driven by “the variation of "
                   "the centrifugal pseudo-force”",
             url="https://academic.oup.com/gji/article/205/1/77/2594825"),
        dict(label="Eötvös experiment — the torsion balance's sensitivity to a difference of "
                   "inertial and gravitational mass via the Earth's centrifugal force, and the "
                   "1909/1922 accuracy of 1 part in 10⁸",
             url="https://en.wikipedia.org/wiki/E%C3%B6tv%C3%B6s_experiment"),
        dict(label="Eötvös effect — the Potsdam Atlantic/Indian/Pacific shipboard readings that "
                   "were “lower when the boat moved eastwards, higher when it moved westward”, "
                   "the 1908 Black Sea confirmation, and the 2Ωu cos φ correction",
             url="https://en.wikipedia.org/wiki/E%C3%B6tv%C3%B6s_effect"),
        dict(label="Schlamminger et al., “Test of the Equivalence Principle Using a Rotating "
                   "Torsion Balance”, Phys. Rev. Lett. 100:041101 (2008) — η = (0.3 ± 1.8)×10⁻¹³ "
                   "for Be–Ti; “space-fixed differential accelerations in any direction are "
                   "limited to less than 8.8×10⁻¹⁵ m/s²”",
             url="https://arxiv.org/abs/0712.0607"),
        dict(label="Anderson et al., “Measurements of Newton's gravitational constant and the "
                   "length of day”, EPL 110:10002 (2015) — the claimed 5.9-year periodicity in G "
                   "in phase with length-of-day variation",
             url="https://arxiv.org/abs/1504.06604"),
        dict(label="Schlamminger, Gundlach & Newman, “Recent measurements of the gravitational "
                   "constant as a function of time” (arXiv:1505.01774) — corrections and "
                   "additions to the G data “significantly weaken the correlation”",
             url="https://arxiv.org/abs/1505.01774"),
        dict(label="Pitkin, Comment on Anderson et al., EPL 111:30002 (2015) — an extra unknown "
                   "Gaussian noise component is favoured “by factors of ≳ e³⁰” over models with "
                   "a sinusoidal component",
             url="https://arxiv.org/abs/1505.06725"),
        dict(label="Foucault pendulum — precession proportional to sin(latitude); “requires care "
                   "to set up because imprecise construction can cause additional veering which "
                   "masks the terrestrial effect”; the burnt thread and the Charron ring",
             url="https://en.wikipedia.org/wiki/Foucault_pendulum"),
        dict(label="The G ring laser at Wettzell — Earth rotation tracked below 1 part in 10⁹, "
                   "resolving length-of-day variation and polar motion in agreement with VLBI; "
                   "Eur. Phys. J. C 82 (2022)",
             url="https://link.springer.com/article/10.1140/epjc/s10052-022-10798-9"),
    ]),
}
