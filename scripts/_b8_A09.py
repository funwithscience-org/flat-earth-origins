# -*- coding: utf-8 -*-
"""Batch 8 — A09. Coriolis reassigned to a rotating sky or to electromagnetism.

Research notes for whoever picks this up next.

1. THE SOURCE IS REACHABLE, THE BOOK PAGE IS NOT. Full-text search of Galileo Was
   Wrong was not achievable with the tools available here: both archive.org text
   renderings (item GallileoWasWrong, and the ...Bennett4276 scan) truncate for the
   fetcher — the Vol. I text stops inside chapter 1 at printed p. 22, the Vol. II
   stream at the chapter-10 contents. What IS reachable is Sungenis stating the
   argument in his own words in the Palm-Sungenis debate document of July 2018
   (archive item RobertSungenisVsDavidPalmDebateOnGeocentrism), where the ether
   version carries the footnote "GWWi, p. 168". Everything this entry attributes to
   the book is attributed at that strength and no further. Two anchors were
   confirmed from tables of contents and are worth recording: Vol. I ch. 4 carries a
   section "Doesn't the Foucault Pendulum Prove Earth is Rotating?" at p. 203, and
   the ...Bennett4276 scan (Vol. II, 7th ed., 2013) carries "The Foucault Pendulum"
   at p. 172 — one page after the general-covariance passage R01 cites at p. 171.

2. THE SOURCE HEDGES AND THE HEDGE WAS CORRECT IN 1918. Sungenis writes that on
   Thirring's rotating-universe result pendulums, satellites and winds "would behave
   very much like we see them behave, but not exactly." That "not exactly" is real
   physics history: Thirring's 1918 interior solution carries a spurious extra term
   and reduced coefficients. Pfister and Braun closed it in 1985 — the paper is
   titled "Induction of correct centrifugal force in a rotating mass shell", CQG
   2(6):909-918 — by putting the shell's interior stresses in properly. The list
   drops the hedge; the literature has since earned the right to drop it, but only
   by moving to a solution that costs more, not less. That is the compression
   finding and it is the most interesting thing on this target.

3. THE CLUSTER HOLDS TWO INCOMPATIBLE ARGUMENTS. Items 6, 106 and 292 say the
   Coriolis terms are real and are produced by the sky. Items 56 and 113 say they
   are electromagnetic; item 214 says they are not there at all. Sungenis's version
   refutes the other two, and item 214 (drones) is anachronistic for a 2006 book.
   verdict_challenge proposes a split. clusters.py was NOT touched — reported up.
"""

ENTRY = {

"A09": dict(
    tldr=("Set the sky spinning instead of the Earth and the Coriolis terms come back "
          "unchanged — so this is not a rival to Coriolis, it is Coriolis re-derived, "
          "which is why the verdict is standard physics rather than refuted. General "
          "relativity really does license it: a rotating mass shell drags the inertial "
          "frames inside it, and once the shell's own stresses are included the interior "
          "carries the correct centrifugal force. The bill arrives afterwards, and only "
          "for those who say the sky's rotation is physical rather than a change of "
          "coordinates: everything the deflection does, the rotating sky must now do too "
          "— reverse sign at the equator, scale as the sine of latitude, and wander in a "
          "433-day wobble driven by pressure on the Pacific sea floor. A disc under a "
          "rotating dome cannot "
          "produce the reversal at all, because its rotation axis points the same way "
          "everywhere on it."),

    passage=dict(
        work="WRK-SUNGENIS-2006", pd=False,
        locator=("Vol. I, p. 168 — as cited by Sungenis himself in the Palm–Sungenis debate "
                 "document of July 2018 (Internet Archive item "
                 "RobertSungenisVsDavidPalmDebateOnGeocentrism), where the sentence is "
                 "footnoted “GWWi, p. 168”. Not checked against page images of Vol. I; given "
                 "the 2013 rearrangement into three volumes, the volume label needs "
                 "confirmation independent of that footnote"),
        quote=("the same ether that caused the 1925 Michelson-Gale experiment to measure an "
               "ether-drift of a 24-hour period … is the same ether that causes a Foucault "
               "Pendulum at the North Pole to rotate 360 in a 24-hour period"),
        gloss="""<p>Two reassignments run side by side in this material, and it is worth separating them before answering either, because they are different physical claims and only one of them is defensible.</p>
<p><strong>The medium version</strong> is the sentence above: the pendulum turns because a rotating <em>ether</em> turns it, the same ether Michelson and Gale are said to have detected in 1925. This is the ancestor of the &ldquo;electromagnetic&rdquo; items in the cluster &mdash; a physical substance, circling the Earth once a day, pushing things about.</p>
<p><strong>The frame version</strong> is the one that carries the argument, and Sungenis states it plainly in the 2018 debate document: <em>&ldquo;in 1918, Hans Thirring was the first to show how this would work. He showed, by pure mathematics, how a rotating universe would affect pendulums on Earth, satellites above the Earth, winds on Earth&hellip;&rdquo;</em> &mdash; and then, in the sentence this page's compression block turns on, that on Thirring's result those things <em>&ldquo;would behave very much like we see them behave, but not exactly.&rdquo;</em> He goes on to say the resulting centrifugal and Coriolis terms are &ldquo;real forces and not fictitious&rdquo;, and are &ldquo;understood as gravitational forces in the geocentric system.&rdquo;</p>
<p>Note who is speaking and what he is not saying. Sungenis and Bennett argue for a <em>stationary spherical</em> Earth at the centre of a rotating cosmos, not for a disc; Sungenis published a book-length attack on flat-earth cosmology, <em>Flat Earth, Flat Wrong</em>, in 2018. The six list items borrow his answer to Coriolis into a model he wrote a book against &mdash; and, as the refutation below works out, the answer does not survive the transfer, because the whole reason a rotating frame can reverse the deflection at the equator is that the Earth is round.</p>"""),

    steelman=dict(
        description="""<p><strong>SURFACE (weak &mdash; do not use).</strong> &ldquo;Coriolis is a fictitious force, so there is nothing to reassign,&rdquo; or &ldquo;a rotating universe is not a thing.&rdquo; Both lose the exchange. &ldquo;Fictitious&rdquo; is a term of art meaning <em>frame-dependent</em>, not <em>unreal</em>: the deflection sinks ships, steers hurricanes and is coded into every operational weather model. And rotating cosmological solutions of the field equations exist; G&ouml;del wrote one down in 1949.</p>
<p><strong>DEEPER.</strong> Mach's principle is a genuine strand in the history of general relativity rather than a fringe borrowing, Einstein named it among the theory's motivations, and frame dragging is real and measured &mdash; Gravity Probe B returned a Lense&ndash;Thirring drift of &minus;37.2 &plusmn; 7.2 mas/yr against a predicted &minus;39.2. True, and incomplete, because it invites the reply that measured frame dragging is ten orders of magnitude too small to be the diurnal rotation.</p>
<p><strong>KERNEL, first form: the rotating-shell result is stronger than the geocentrist usually states it.</strong> Thirring showed in 1918 that inside a slowly rotating mass shell the inertial frames are dragged, and that the interior acquires terms of Coriolis and centrifugal form. His solution was not clean &mdash; it carried a spurious extra term, and Sungenis's own &ldquo;but not exactly&rdquo; is an accurate report of it. The literature then fixed it: Pfister and Braun showed in 1985, in a paper titled <em>Induction of correct centrifugal force in a rotating mass shell</em> (<em>Class. Quantum Grav.</em> 2:909&ndash;918), that with the shell's interior stresses treated properly the correct centrifugal force is induced inside. Brill and Cohen had shown in 1966 (<em>Phys. Rev.</em> 143:1011) that as a shell's radius approaches its own Schwarzschild radius the dragging becomes complete &mdash; the interior frames rotate <em>with</em> the shell. Our universe's mass and radius put it in the neighbourhood of that limit. So &ldquo;the turning sky turns the pendulum&rdquo; is not crankery. It is a licensed reading of a theory nobody in this dispute rejects at that point.</p>
<p><strong>KERNEL, second form &mdash; and this one is for the electromagnetic branch, which deserves better than the mockery it usually gets.</strong> Sibling argument <a href="#ARG-A10">A10</a> establishes the decisive fact: the deflection <em>reverses sign across the equator</em>, and a thermal driver such as solar heating has no handedness from which a reversal could come. Now ask what else in ordinary physics does. There is exactly one common candidate: the magnetic Lorentz force, <em>qv</em>&times;<em>B</em>, which is chiral by construction &mdash; and the vertical component of the geomagnetic field flips sign at the magnetic dip equator, close to the geographic one. Whoever first said &ldquo;ocean currents are electromagnetic&rdquo; had picked the only everyday force with the right qualitative signature: handed, and handed the other way south of a line near the equator. That is a better instinct than it looks.</p>""",
        why_it_doesnt_save_claim="""<p><strong>Against the frame version: reproducing a term by construction is not evidence for the model that reproduces it.</strong> This is the whole of it. If the rotating-universe description contains the same 2&Omega;&times;<em>v</em> with the same coefficient &mdash; and that is what its defenders are claiming, correctly &mdash; then every measurement of the Coriolis deflection comes out identically in both descriptions, and no such measurement can favour either. The six items in this cluster are offered as evidence against a spinning Earth. Their own best defence makes them evidence for nothing. That is a real cost and it is paid in this cluster's own currency: on the geocentrist's account, items 6, 106 and 292 stop being arguments and become bookkeeping.</p>
<p><strong>And the reproduction is exact only in a limit that has a price.</strong> The clean interior result needs a shell with the right internal stresses, and completeness of dragging needs the shell at its gravitational radius. A model in which dragging is anything less than complete gives a Coriolis parameter reduced by a factor below one &mdash; and the measured parameter matches complete dragging to the precision of ring-laser gyroscopy, better than one part in 10<sup>9</sup>. The rotating-Earth account predicts that number with nothing to adjust. The rotating-universe account has to be tuned to the limit in which it agrees.</p>
<p><strong>Against the electromagnetic version: right instinct, wrong line and wrong size by seven orders of magnitude.</strong> The line first. The magnetic dip equator is not the geographic equator, and it migrates &mdash; Yizengaw's survey records the dip equator moving north over Brazil at about 0.2&deg; of latitude per year, some 3.85&deg; in twenty years. The line where cyclonic organisation fails does not travel with it; NOAA's hurricane researchers state the exclusion zone as a distance from the equator, about 300 miles or five degrees, and it has stayed there. Then the size, with the inputs on the table so a reader can redo it: seawater conductivity 3.2 S/m, geomagnetic field 5&times;10<sup>&minus;5</sup> T, current speed 0.1 m/s give an induced current density <em>&sigma;vB</em> &asymp; 1.6&times;10<sup>&minus;5</sup> A/m&sup2; and a Lorentz force density <em>jB</em> &asymp; 8&times;10<sup>&minus;10</sup> N/m&sup3;, which on 1025 kg/m&sup3; of seawater is an acceleration near 8&times;10<sup>&minus;13</sup> m/s&sup2;. The Coriolis acceleration on the same water is 2&Omega;<em>v</em>&thinsp;sin&phi; &asymp; 1.0&times;10<sup>&minus;5</sup> m/s&sup2;. The proposed cause is about ten million times too weak.</p>
<p><strong>Against both, and fatally for this list in particular: the reassignment is a globe-shaped answer.</strong> The reversal exists because on a sphere only the component of the rotation vector along the local vertical enters the horizontal deflection, and that component changes sign at the equator. Put the rotation axis through the centre of a flat disc, as a rotating dome requires, and the axis is parallel to the local vertical at every point on the disc: the Coriolis parameter is 2&Omega; everywhere, one sign everywhere, no equatorial calm belt and no mirrored trade winds. Sungenis's answer works only in Sungenis's cosmos.</p>"""),

    refutation="""<p><strong>First, the concession, and it has to be complete.</strong> In a frame rotating with angular velocity <strong>&Omega;</strong> relative to the local inertial frames, the equation of motion acquires the terms &minus;2<strong>&Omega;</strong>&times;<strong>v</strong>, &minus;<strong>&Omega;</strong>&times;(<strong>&Omega;</strong>&times;<strong>r</strong>) and &minus;(d<strong>&Omega;</strong>/d<em>t</em>)&times;<strong>r</strong>. Nothing in that derivation says which body rotates. It is a statement about relative rotation, and it was so from the beginning: Coriolis's 1835 paper, <em>Sur les &eacute;quations du mouvement relatif des syst&egrave;mes de corps</em> (<em>Journal de l'&Eacute;cole Polytechnique</em> XV, pp. 142&ndash;154), was about the relative motion of systems of bodies, and the Earth was not his subject. Bibnum's study of the paper notes that meteorology &ldquo;is an area that was without a doubt even more foreign to the concerns of Coriolis&rdquo; than the celestial mechanics that Foucault later drew out of it; the application to winds and currents is William Ferrel's, from the late 1850s, in the form &mdash; already the crux of this page &mdash; that the deflection &ldquo;always deflects it to the right in the northern hemisphere.&rdquo;</p>

<p><strong>The two numbers, which this page got wrong once and now keeps apart.</strong> The Coriolis parameter is <em>f</em> = 2&Omega;&thinsp;sin&phi;. The precession rate of a Foucault pendulum is &Omega;&thinsp;sin&phi; &mdash; <em>half</em> of it &mdash; which is why the plane of swing takes a full sidereal day, 23 h 56 m, to come round at the pole and about 32 hours at the latitude of Paris. Earth's rotation rate &Omega; is 7.292&times;10<sup>&minus;5</sup> rad/s, or 15.04&deg; per hour. A treatment that runs the two together will be caught by anyone who checks, and the factor of two is not decorative: it is the difference between the deflection of a moving parcel and the rotation of a plane.</p>

<p><strong>Second, what general relativity actually grants, stated at full strength.</strong> Hans Thirring showed in 1918 that inside a rotating mass shell the inertial frames are dragged, and that the interior picks up terms with the form of the centrifugal and Coriolis forces. That result was imperfect &mdash; the interior also acquired a term with no Newtonian counterpart &mdash; and it was repaired, not by geocentrists and not by their critics, but by the relativity literature: Pfister and Braun, <em>Induction of correct centrifugal force in a rotating mass shell</em>, <em>Classical and Quantum Gravity</em> 2(6):909&ndash;918 (1985). Brill and Cohen, <em>Rotating masses and their effect on inertial frames</em>, <em>Physical Review</em> 143:1011 (1966), had already shown that dragging becomes complete for a shell near its own Schwarzschild radius. Put those together and the geocentrist's claim &mdash; that a universe rotating about a stationary Earth would produce the Coriolis and centrifugal effects we observe &mdash; is not a misunderstanding of physics. It is a reading physics supports. <strong>This is why the verdict on A09 is STANDARD PHYSICS and not REFUTED, and the page should not pretend otherwise.</strong></p>

<p><strong>Third, why that grant is worth nothing to the argument.</strong> Because it is symmetric, and the items are not. Item 106 is listed as a reason to think the Earth does not spin. But if the two descriptions contain the same term with the same coefficient, then the observation of that term discriminates between them exactly as well as a thermometer discriminates between Celsius and Fahrenheit. The strongest form of this argument is a proof that the Coriolis evidence is <em>neutral</em>. Neutral evidence is not evidence for the stationary side. Sungenis is careful here in a way the list is not: he does not present Thirring as a measurement, he presents him as a demonstration that the geocentric system is &ldquo;the more complete system&rdquo; because it needs no forces labelled fictitious. That is an argument about elegance and vocabulary. It is not an observation, and it was never offered as one.</p>

<p><strong>Fourth, the vocabulary itself, because a straw man is buried in it.</strong> Calling the Coriolis term &ldquo;fictitious&rdquo; has never meant that nothing happens. It means the term is frame-dependent: it appears in the equations written in a rotating frame and vanishes in the equations written in an inertial one, while the physical facts &mdash; where the shell lands, which way the storm turns, how many fringes the ring laser counts &mdash; are the same either way. Sungenis's version, that these are &ldquo;real forces and not fictitious&rdquo; in the geocentric system, is a claim about which chart to privilege, dressed as a claim about what exists. Nobody needs to contest it to answer the argument, and contesting it is how the mainstream side usually loses this exchange.</p>

<p><strong>Fifth, what the physical reading costs &mdash; and this is where the two readings part company.</strong> Following <a href="#ARG-R01">R01</a>: <em>(a)</em> writing the standard solar system in Earth-fixed rotating coordinates is a change of chart, free, and carries no commitment; <em>(b)</em> asserting that the cosmos physically turns about a stationary Earth is a different model that owes a dynamics. On reading (b) the rotating sky inherits every irregularity of the Earth's rotation, because the two are the same relative motion measured one way or the other. So:</p>
<ul>
<li><strong>The cosmos must wobble on a 433-day period.</strong> The Chandler wobble &mdash; period 433.0 &plusmn; 1.1 days &mdash; is the free nutation of a deformable spinning body, and Gross's analysis of 1985&ndash;1996 data attributes its excitation chiefly to <em>ocean-bottom pressure fluctuations</em> (3.45 mas&sup2; of power in the Chandler band, against 1.87 for atmospheric pressure). Under (b) the rotation axis of the universe is being nudged by pressure changes on the floor of the Pacific.</li>
<li><strong>The cosmos must speed up and slow down with the monsoon.</strong> Length of day varies by milliseconds, and EarthScope's summary puts about 90 per cent of the seasonal variation down to shifts in zonal wind patterns, with El Ni&ntilde;o years running long and La Ni&ntilde;a years short. A millisecond on 86,400 s is about one part in 10<sup>8</sup>; under (b) the whole rotating cosmos changes its rate by that fraction, twice a year, in step with the atmosphere's angular momentum, and secularly by the 2.3 ms per century that tidal friction adds.</li>
</ul>
<p>Be exact about what this does and does not show. It is not a contradiction on reading (a), where these are coordinate descriptions of the Earth's own wobbles and the arithmetic is the same arithmetic. It is a bill on reading (b), and reading (b) is the one Sungenis takes: in the same passage he credits Thirring's rotating universe with showing how &ldquo;its own nutation and precession would affect what we see on Earth.&rdquo; Once the sky's nutation is doing explanatory work, the sky owes an account of why its nutation is excited by seawater.</p>

<p><strong>Sixth, the electromagnetic branch, on its own terms.</strong> Items 56 and 113 replace the inertial deflection with an electromagnetic one. The instinct is sound &mdash; the Lorentz force is the one everyday force with a built-in handedness that flips near the equator &mdash; and the mechanism is real: moving seawater does generate electric currents in the geomagnetic field, and the resulting magnetic signals are measured, at roughly 1&ndash;2 nT at satellite altitude for the great current systems. What fails is the back-reaction. The force those currents exert on the water is around 8&times;10<sup>&minus;13</sup> m/s&sup2; on the numbers set out in the steelman, against 1.0&times;10<sup>&minus;5</sup> m/s&sup2; for Coriolis on the same parcel: seven orders of magnitude. And there is a cleaner test than arithmetic. An electromagnetic cause must scale with conductivity. Air at the surface conducts about 10<sup>&minus;14</sup> S/m, some fourteen orders of magnitude below seawater &mdash; yet the atmosphere is deflected with the same handedness, the same sign reversal and the same 2&Omega;<em>v</em>&thinsp;sin&phi; magnitude as the ocean. A Foucault bob of copper, brass or lead precesses at the same &Omega;&thinsp;sin&phi;. Material-independent and mass-proportional is the signature of an inertial term; conductivity-dependent is the signature of an electromagnetic one; the measurements say the first.</p>

<p><strong>Seventh, the drones.</strong> Item 214 says there is no Coriolis correction in drone flight software. Take the factual core as given &mdash; we have not read hobby flight-controller source and are not going to assert anything about what is in it &mdash; because the inference fails whatever the code contains. Start with the size: for a drone at 10 m/s at 45&deg; latitude the Coriolis acceleration is 2&Omega;<em>v</em>&thinsp;sin&phi; &asymp; 1.0&times;10<sup>&minus;3</sup> m/s&sup2;, about one ten-thousandth of gravity, which a quadcopter cancels with a tilt of six thousandths of a degree. Left entirely uncorrected it would move the aircraft about 5 m off track over a 100-second leg &mdash; smaller than the drift from a light breeze, and nulled by the same GPS-and-barometer feedback loop that nulls the breeze. A closed loop does not need a model of a disturbance it is already measuring. Now look at the systems that <em>cannot</em> close the loop, because they navigate with no external reference: strapdown inertial navigators carry Earth-rate and transport-rate terms explicitly in their mechanisation equations, and a gyrocompass finds true north by sensing Earth's rotation and nothing else &mdash; iMAR's engineering guide sets the threshold plainly, gyro drift below about 0.1&deg;/h against Earth rate of 15.05&deg;/h, and quotes the heading a 0.015&deg;/h gyro can reach from that ratio. Ships have been steering by that principle since the early twentieth century. So the honest version of item 214 is: <em>where the effect is below the noise and the loop is closed, nobody codes it; where it is above the noise or the loop is open, everybody does</em> &mdash; which is what a real 2&Omega;<em>v</em> term predicts, and what a non-existent one does not. Compare <a href="#ARG-A14">A14</a> on artillery and <a href="#ARG-A19">A19</a> on gyrocompasses, where the same trade appears.</p>

<p><strong>Eighth, the cluster contradicts itself, and the contradiction is not ours to resolve.</strong> Items 6, 106 and 292 say the Coriolis effects are real, are exactly as observed, and are produced by the turning heavens. Items 56 and 113 say they are produced by electromagnetism instead; item 214 says they are not produced at all. These cannot all be held. On the geocentric account the deflection is a genuine consequence of relative rotation and its magnitude is 2&Omega;<em>v</em>&thinsp;sin&phi; &mdash; so Sungenis's items refute the electromagnetic items, and both refute the drone item. This is the same structure <a href="#ARG-R01">R01</a> found on covariance: the list carries an argument and its own answer side by side, and a defender has to choose which one to keep.</p>

<p><strong>Verdict: standard physics.</strong> The frame version of this argument is a legitimate restatement inside a theory nobody here disputes, it produces the observed Coriolis terms because it was built to, and for exactly that reason it produces no observation the rotating-Earth model does not already produce. It is not evidence; on its own showing it cannot be. What it does have is a price list &mdash; a cosmos whose spin rate tracks the seasonal winds and whose axis is nudged by pressure on the sea floor &mdash; and a shape requirement its borrowers do not meet, since the equatorial reversal that makes the whole phenomenon interesting exists only because the local vertical changes its angle to the rotation axis, which is a thing that happens on a sphere and not on a disc.</p>""",

    advocate=dict(
        survives=4,
        best_defense=(
            "You have conceded the argument and then complained about the bill. Read your own "
            "third section: the two descriptions contain the same term with the same "
            "coefficient, so no Coriolis measurement discriminates. That is our claim. We never "
            "said the pendulum stands still; we said it does not tell you which of the two is "
            "turning, and you agree. Your price list is a coordinate artefact dressed as an "
            "objection: of course the sky's rotation carries the Chandler wobble and the "
            "seasonal length-of-day signal, because 'the sky's rotation relative to the Earth' "
            "and 'the Earth's rotation relative to the sky' are one quantity with two names — "
            "you have discovered that a mirror image is left-handed. As for tuning to complete "
            "dragging: Brill and Cohen showed complete dragging is what you get for a shell at "
            "its gravitational radius, and the observed universe sits near that value. We did "
            "not tune it; we found it, and it is the strongest Machian coincidence in cosmology. "
            "Finally, the flat-earth geometry point is not an argument against us. We are not "
            "flat-earthers. If a flat-earth list has borrowed our answer, take that up with "
            "them — it does not touch the geocentric case, and Sungenis wrote a book against "
            "them in 2018."),
        preemptive=(
            "This defence is strong and three of its four moves are already answered in the "
            "body; the fourth needed a change, which was made. (a) The 'you conceded it' move "
            "is anticipated in section three and turned into the finding — neutral evidence is "
            "not evidence for the stationary side, and the concession costs the list its own "
            "items. Keep that paragraph adjacent to the concession, never later. (b) The "
            "'coordinate artefact' move is why section five was rewritten to split readings (a) "
            "and (b) explicitly and to say in terms that the wobble bill is NOT a contradiction "
            "on the chart reading. If that sentence is ever cut for length the section becomes "
            "vulnerable, because on the chart reading the advocate is simply right. (c) The "
            "complete-dragging point is fair and the body concedes it as a kernel rather than "
            "disputing it; the reply that survives is the one in the steelman — the "
            "rotating-Earth account predicts the same number with nothing to adjust, so the "
            "geocentric version buys agreement at the cost of a coincidence it must import. (d) "
            "The last move — 'we are not flat-earthers' — is correct and was conceded in the "
            "passage gloss and again in the closing paragraph. That is the right handling for "
            "THIS page: A09's items sit in a flat-earth list, so the finding is not that "
            "Sungenis is wrong about his own model but that the borrowers have taken an answer "
            "that requires a sphere. Do not soften it into an accusation against him; the "
            "sentence to keep is the geometric one about the local vertical."),),

    straw_man=dict(
        identified=True,
        detail=("Two, one in each branch. The frame branch misdescribes the mainstream position "
                "as needing to 'add in fictitious forces', with the implication that mainstream "
                "physics treats the deflection as unreal and the geocentric system is therefore "
                "'the more complete system'. Nobody holds the position being improved on: "
                "'fictitious' is a term of art for 'frame-dependent', and the observable "
                "consequences — the fringe count, the storm's sense of rotation, the shell's "
                "landing point — are identical in both charts, which is precisely why the "
                "argument cannot be evidence. The drone branch attributes to us a claim we do "
                "not make: that every moving object needs an explicit Coriolis term in its "
                "software. The claim is that the term is there in the physics with magnitude "
                "2*Omega*v*sin(phi), which is why open-loop navigators code it and closed-loop "
                "ones absorb it. A third pattern is worth naming without calling it a straw "
                "man: item 214 asks for a correction in a system whose feedback removes the "
                "need for one, then reads the absence as the absence of the effect.")),

    compression=dict(
        assessed=True, drifted=True,
        list_phrasing="Coriolis equivalence with sky rotation.",
        source_wording=("“Thirring discovered that pendulums, satellites and winds would behave "
                        "very much like we see them behave, <em>but not exactly</em>.”"),
        drift_type="hedge_dropped",
        note=("The item asserts <em>equivalence</em>. The source, in Sungenis's own words in the "
              "July 2018 Palm&ndash;Sungenis debate document, asserts near-equivalence and says "
              "so twice in one sentence: <em>very much like</em>, and <em>but not exactly</em>. "
              "That qualification is not modesty, it is accurate physics history &mdash; "
              "Thirring's 1918 interior solution carries a term with no Newtonian counterpart, "
              "and the coefficients are not those of a rotating frame. What makes this case "
              "unusual is that the hedge <em>became</em> droppable after the fact: Pfister and "
              "Braun's 1985 paper, titled <em>Induction of correct centrifugal force in a "
              "rotating mass shell</em>, showed that a shell with its interior stresses handled "
              "properly induces the correct centrifugal force, and Brill and Cohen's 1966 result "
              "gives complete dragging in the limit of a shell at its gravitational radius. So "
              "the flat list item is closer to today's literature than the hedged source is "
              "&mdash; and it is still a worse argument, because the exactness is bought by "
              "moving to a solution that requires tuned interior stresses and a shell at its "
              "gravitational radius, which is a larger commitment, not a smaller one. The "
              "refutation above is aimed at the strong modern version, not at Thirring's 1918 "
              "approximation, which would be the easy target and the wrong one."
              "<p><strong>A second pattern, which the single-value enum cannot carry.</strong> "
              "Six items sit in this cluster and they do not share a lineage. Items 6, 106 and "
              "292 are the reassignment as Sungenis argues it. Items 56 and 113 "
              "(&ldquo;electromagnetic&rdquo;) and 214 (drones) assert something his argument "
              "needs to be false, and we could not locate them in the Sungenis text we were able "
              "to search &mdash; which was limited: both archive renderings truncate, the Vol. I "
              "text stopping inside chapter 1 at printed p. 22 and the Vol. II scan at the "
              "chapter-10 contents, so this is a statement about our search and not about the "
              "books. Item 214 also has a dating problem independent of any search: consumer "
              "camera drones postdate a 2006 publication. Recorded here rather than acted on; "
              "the cluster record was left untouched.</p>")),

    verdict_challenge=dict(
        challenged=True,
        proposed_verdict=("STANDARD PHYSICS for items 6, 106 and 292; REFUTED for items 56 and "
                          "113; MISLEADING for item 214"),
        reasoning=("The cluster name joins two reassignments with an 'or', and they do not share "
                   "a verdict. Reassigning the Coriolis terms to a rotating universe is standard "
                   "physics: general relativity supports it, it reproduces the observed terms by "
                   "construction, and the objection to it is that it is not evidence rather than "
                   "that it is wrong. Reassigning them to electromagnetism is a different claim "
                   "with a different fate — it is quantitatively dead, about seven orders of "
                   "magnitude short, and it predicts a sign-reversal line on the migrating "
                   "magnetic dip equator rather than on the geographic one. Item 214 is neither: "
                   "its factual core may well be true and its inference does not follow, which "
                   "is what MISLEADING is for on this page. Holding all six under STANDARD "
                   "PHYSICS reads as though the page had blessed the electromagnetic claim, and "
                   "it also hides the more interesting finding, which is that the two halves of "
                   "the cluster contradict each other. This is a proposal only: clusters.py was "
                   "not edited, and whether the answer is a verdict change or a cluster split is "
                   "an operator's call.")),

    people=["PER-SUNGENIS"],
    related=["A06", "A10", "A13", "A14", "A19", "R01", "R02", "R05", "D17"],

    sources=[
        dict(label="Palm–Sungenis debate document, July 2018 (Internet Archive) — Sungenis on "
                   "Thirring's rotating universe, “very much like we see them behave, but not "
                   "exactly”, and the ether/Foucault sentence footnoted “GWWi, p. 168”",
             url="https://archive.org/stream/RobertSungenisVsDavidPalmDebateOnGeocentrism/Robert%20Sungenis%20Vs%20David%20Palm%20Debate%20on%20Geocentrism_djvu.txt"),
        dict(label="Sungenis & Bennett, Galileo Was Wrong Vol. I — Internet Archive scan (item "
                   "GallileoWasWrong); the contents list a section “Doesn't the Foucault Pendulum "
                   "Prove Earth is Rotating?” at p. 203. The text rendering available to us "
                   "truncates inside chapter 1 at printed p. 22",
             url="https://archive.org/details/GallileoWasWrong"),
        dict(label="Pfister & Braun, “Induction of correct centrifugal force in a rotating mass "
                   "shell”, Class. Quantum Grav. 2(6):909–918 (1985) — bibliographic record",
             url="https://pascal-francis.inist.fr/vibad/index.php?action=getRecordDetail&idt=8729257"),
        dict(label="Brill & Cohen, “Rotating masses and their effect on inertial frames”, Phys. "
                   "Rev. 143:1011 (1966)",
             url="https://ntrs.nasa.gov/citations/19660060823"),
        dict(label="Moatti, “Coriolis: the Birth of a Force” (Bibnum) — the 1835 paper, and "
                   "Ferrel's application to winds: deflection “always to the right in the "
                   "northern hemisphere”",
             url="https://www.bibnum.education.fr/sites/default/files/analyse-coriolis-force-en.pdf"),
        dict(label="Coriolis 1835, Journal de l'École Royale Polytechnique, Cahier XXIV, Tome XV, "
                   "pp. 142–154 — bibliographic record",
             url="https://www.scirp.org/reference/referencespapers?referenceid=898138"),
        dict(label="Gross, “The excitation of the Chandler wobble”, Geophys. Res. Lett. "
                   "27(15):2329–2332 (2000) — 433.0 ± 1.1 days, excited chiefly by ocean-bottom "
                   "pressure fluctuations",
             url="https://svalgaard.leif.org/EOS/2000GL011450.pdf"),
        dict(label="EarthScope Consortium — length-of-day variation: ~90% of the seasonal signal "
                   "from zonal winds; 2.3 ms per century from tidal friction",
             url="https://www.earthscope.org/news/a-day-is-not-always-24-hours-how-earths-shifting-systems-cause-day-length-variation/"),
        dict(label="Yizengaw, “The Potential Impacts of the Erratic Motion of Dip Equator and "
                   "Magnetic Poles” (2020) — dip equator migrating ~0.2°/yr over Brazil",
             url="https://par.nsf.gov/servlets/purl/10248981"),
        dict(label="Modelling of electromagnetic signatures of global ocean circulation, Earth "
                   "Planets Space 71 (2019) — motional induction, seawater conductivity 3.2 S/m, "
                   "signals of order 1–2 nT at satellite altitude",
             url="https://link.springer.com/article/10.1186/s40623-019-1033-7"),
        dict(label="iMAR Navigation, engineering decision guide — gyrocompassing against Earth "
                   "rate of 15.05°/h; drift below ~0.1°/h needed to find north autonomously",
             url="https://www.imar-navigation.de/downloads/Decision_assistant-Dateien/Decision_assistant.pdf"),
        dict(label="NOAA AOML Hurricane Research Division FAQ — cyclones require roughly 300 "
                   "miles (about 5°) from the equator",
             url="https://www.aoml.noaa.gov/hrd-faq/"),
        dict(label="NOAA National Ocean Service — the Ekman spiral: surface water deflected to "
                   "the right of the wind in the Northern Hemisphere",
             url="https://oceanservice.noaa.gov/education/tutorial_currents/04currents4.html"),
        dict(label="Faulkner, “The Rise of the Modern Geocentric Theory Movement” (Answers in "
                   "Genesis) — geocentrists “often argue a version of Mach's principle”, with "
                   "Lense and Thirring",
             url="https://answersingenesis.org/astronomy/rise-of-modern-geocentric-theory-movement/"),
        dict(label="Sungenis, Flat Earth, Flat Wrong: An Historical, Biblical and Scientific "
                   "Analysis (2018) — the cluster's originator arguing against flat-earth "
                   "cosmology",
             url="https://www.goodreads.com/book/show/46194734-flat-earth-flat-wrong")]),
}
