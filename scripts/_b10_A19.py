# -*- coding: utf-8 -*-
"""Batch 10 — A19. "Gyrocompasses are sky-locked, not Earth-locked."

Verdict SELF-CONTRADICTED, kept. Research notes for whoever picks this up next.

0. ITEM COUNT. The brief that commissioned this entry said "3 items". `assign.py` maps
   exactly ONE item to A19: 229, "Gyrocompass sky-locked." Reported up; nothing in this
   entry assumes more than the one item, and the prose says "the item", never "the items".
   The other four gyroscope items on the list (12, 19, 112, 225) sit in A07, which has its
   own treatment; this entry uses two of them as evidence and does not re-litigate them.

1. THE SOURCE EXISTS AND IT IS REACHABLE. Sungenis & Bennett, Galileo Was Wrong Vol. I,
   ch. 12 "Technical and Summary Analysis of Geocentrism", printed pp. 709-711 of the
   Internet Archive scan (item GallileoWasWrong, the CD-ROM issue our WRK-SUNGENIS-2006
   record describes). The book lists three "geokinetic claims" for the Earth's spin, and
   the third of them is, verbatim: "The Sagnac effect used in laser gyroscopes and the
   precession of mechanical gyrocompasses indicate the Earth is spinning." It is stating
   the OTHER SIDE'S case, and then answering it with Mach's principle across pp. 710-713.
   THE SAME TEXT IS IN VOL. II of the 2013 seventh edition at ch. 10, printed pp. 157-158
   (archive.org item GalileoWasWrongTheChurchSungenisRobertA.Bennett4276). Both were
   downloaded and grepped for this entry. Do not treat the two page ranges as a conflict:
   it is one passage, printed twice, in the 2006 Vol. I and again after the 2013
   three-volume rearrangement. This is a rare case where the volume/edition trap resolves
   cleanly, so it is written into the locator.

2. THE HEDGE. The source does NOT assert that gyrocompasses are sky-locked. It asserts
   that you cannot tell: "No measurement of absolute or preferred rotation has been made
   to test whether the Earth is rotating or its surroundings. Until such a test is
   performed, Mach's principle is a valid statement; it has not been disproven
   experimentally" (p. 711). In the Sagnac chapter, numbered point 16 at p. 741: "By
   Mach's principle the Sagnac effect cannot distinguish between whether the Earth
   actually rotates and the ether is at rest, or the Earth is at rest and the ether whirls
   around it." A not-disproven, re-used by the list as an affirmative instrument result.
   drift_type = force_upgraded, the R01 pattern.

3. AND DO NOT STOP AT THE DISJUNCTION — that is the hedge rule violated on our side. The
   book states its conclusion flatly a few pages later. Michelson-Gale, Claims and
   Responses, p. 745, response point 3: "Just as the free mechanical motion of the
   Foucault pendulum defined a plane of motion relative to the rotating heavens, the free
   motion of the Michelson-Gale light ring defined a plane of radiation relative to the
   same heavens." No hedge in that sentence at all. So the entry must not present the
   source as merely agnostic; it holds the heavens turn, and says so.

4. THE ARGUMENT THAT ACTUALLY WORKS, AND IT IS NOT THE ONE IN clusters.py. Grant Mach
   entirely. A gyrocompass senses rotation relative to the LOCAL INERTIAL FRAME; if the
   cosmos turns and the Earth stands still, the frame is dragged and the instrument reads
   the same. The Machian model reproduces gyrocompass behaviour exactly, by construction,
   and the book says so. What Mach buys is an equivalence between ROTATIONS. It buys
   nothing about SHAPE. That is where this argument lands:
     - free-gyro azimuth drift  = 15.04 sin(latitude) deg/hr
     - free-gyro tilt rate      = 15.04 cos(latitude) sin(azimuth) deg/hr
     - gyrocompass directive force is proportional to cos(latitude): maximum at the
       equator, zero at the poles
   Two components of ONE vector of fixed magnitude, resolved in the local horizontal and
   local vertical. Their squares sum to a constant. That decomposition varies with
   position only because the local vertical swings through 90 degrees between equator and
   pole. On a PLANE the local vertical is one direction everywhere, so the angle it makes
   with any fixed rotation axis is the same at every point — whatever is turning, whichever
   way the axis points. No latitude dependence of any gyroscopic quantity is available on a
   flat Earth. The gyrocompass is therefore a curvature measurement made inside a closed
   box on a ship's bridge.

5. THE PAPER TRAIL, ALL OF IT CHECKED 2026-08-10.
   (a) IMO Resolution A.424(XI), Performance standards for gyro-compasses, as transcribed
       by the Netherlands Regulatory Framework: settle "within six hours in latitudes of up
       to 60 degrees"; settle point error "not exceed +/- 0.75 x secant latitude" (5.1.2);
       residual steady state error "+/- 0.25 x secant latitude" at twenty knots (5.2.3.a);
       "Means should be provided for correcting the errors induced by speed and latitude"
       (9.2). Secant latitude is 1/cos(latitude) — the reciprocal of the directive force.
   (b) Sperry Marine NAVIGAT X MK 2 datasheet (spinning mass, twin rotors 19,000 rpm):
       "Static < 0.1 deg secant latitude", "Settle point error < 0.1 deg secant latitude",
       "Dynamic < 0.4 deg secant latitude". A product you can buy, spec'd in sec(lat).
   (c) Speed error, Szczecin Maritime University gyro notes: tan(delta) = -(V cos KR) /
       (900 cos(phi) + V sin KR), and "At any latitude other than the equator, this
       velocity becomes 900 times the cosine of the latitude." 900 knots = 21,600 nautical
       miles / 24 h, and 21,600 is 360 x 60 arcminutes of a GREAT CIRCLE. The correction
       table is written in units of the Earth's own curvature. (Sidereal: 21,600/23.9345 =
       902.5 kn. The 0.3% gap is far inside the error budget; do not make it load-bearing.)
   (d) Tilt and drift rates: thenauticalsite.in gyro notes ("Rate of tilting in degrees per
       hour = 15 sine Azimuth * cosine Latitude"; "Rate of Drift in degrees per hour = 15
       sine Latitude") and knowledgeofsea.com, independently. Both were re-derived here
       from the vector decomposition and they are right.
   (e) Directive force: cultofsea.com — "the directive force is maximum at the equator and
       decreases to zero at the poles."
   (f) Foucault: precession proportional to sin(latitude), clockwise at the north pole,
       counterclockwise at the south, and at the equator "the plane of oscillation remains
       fixed relative to Earth."

6. THE SELF-CONTRADICTION, WHICH IS ON THE LIST ITSELF AND IS THE VERDICT'S BEST LEG.
   Item 229 says the gyrocompass follows the sky. Item 19 says "Gyroscopes stable absent
   recalibration" — follows the ground. Item 12 says "Gyroscope anomalies indicating no
   rotation." Under EVERY model on offer here the ground and the sky turn relative to each
   other once a day, or there is no day; so an instrument cannot hold still against both.
   Item 225, "Ring laser gyro corrections", concedes the correction exists, which is item
   19's denial reversed. Four items, one list, two incompatible readings of the same
   hardware. That is exactly what the SELF-CONTRADICTED chip is defined to mean.

7. ORIGIN STAYS UNTRACED, DELIBERATELY. Sungenis & Bennett Vol. I is an ANCESTOR — the
   earliest text located that carries this content — and that is not evidence of
   origination. The compressed phrase "sky-locked" is not located in either Sungenis
   volume's OCR, and the word "gyro" is not located anywhere in the archive.org OCR of
   Marshall Hall, The Earth Is Not Moving (1991), whose mechanical argument is the Foucault
   pendulum instead (26 hits for "Foucault", 48 for "pendulum", 0 for "gyro"). The fact the
   item leans on — that a free gyro holds its axis against the stars — is textbook and
   older than the movement; Foucault built the gyroscope in 1852 to show it. Nobody
   modern is credited. Do not substitute a guess.

8. WHAT WE COULD NOT REACH. No print copy of either Sungenis volume was consulted; both
   page ranges come from archive.org OCR. The Britannica and Bowditch treatments of the
   gyrocompass were not obtained at sentence level — the latitude law here rests on two
   maritime training sources plus the IMO standard and the Sperry datasheet, which is why
   all four are cited rather than one. No raw settling-time data from any vessel was
   obtained, and the advocate section says so in the defender's voice rather than ours.

9. DEFECTS IN OUR OWN RECORD, reported up, NOT edited here (this agent owns one file).
   clusters.py A19 note reads "A gyrocompass finds true north by sensing Earth's rotation.
   It cannot function on a non-rotating Earth." That note renders as `basis`, immediately
   above the refutation, and its second sentence is answered in one line by the source:
   on a stationary Earth inside a rotating cosmos the local inertial frame is dragged and
   the instrument works normally. Per the past-tense rule nothing about this appears in the
   published prose below; the refutation instead states the correct form in its own voice,
   as a warning about the popular version of the debunk. See record_problems.
"""

ENTRY = {

"A19": dict(

    tldr=("A free gyroscope really does hold its axis against the stars rather than the "
          "ground — that much is textbook, and it is why an aircraft's heading indicator "
          "has to be realigned every ten or fifteen minutes. A gyrocompass is the "
          "instrument built to break exactly that: weighted so the daily rotation tips "
          "it, it swings into "
          "the meridian instead, and its north-seeking force is strongest at the equator "
          "and falls to zero at the poles. That falling-off measures the angle between the "
          "local vertical and the rotation axis — and on a flat plane that angle is the "
          "same at every point, whatever is turning."),

    passage=dict(
        work="WRK-SUNGENIS-2006",
        pd=False,
        locator=("Vol. I, ch. 12 “Technical and Summary Analysis of Geocentrism”: the third "
                 "numbered geokinetic claim at printed p. 709, and the response to Claim #1 at "
                 "printed p. 710, of the Internet Archive OCR (item GallileoWasWrong). The same "
                 "passage is reprinted in the 2013 seventh edition at Vol. II, ch. 10, printed "
                 "pp. 157–158 (item GalileoWasWrongTheChurchSungenisRobertA.Bennett4276); both "
                 "scans were read for this entry. No print copy was consulted."),
        quote=("The Sagnac effect used in laser gyroscopes and the precession of mechanical "
               "gyrocompasses indicate the Earth is spinning. … Implicitly denied is the "
               "equally valid premise that the rotation of the external world, the universe, "
               "can cause the very same inertial forces — centripetal and Coriolis. That "
               "premise is known as Mach's Principle."),
        gloss="""<p><strong>Read who is speaking.</strong> The first sentence is not the book&rsquo;s claim. It is the book <em>stating the case against itself</em> &mdash; the third of three &ldquo;geokinetic claims&rdquo; it lists at p. 709 before answering them &mdash; and it states that case accurately and without sneering. The second sentence is the answer, from the response to Claim #1 on the facing page. Between them they contain the whole of what the source holds about gyroscopic instruments, and it is not what item 229 holds.</p>
<p><strong>What the source actually claims: a not-disproven, not a result.</strong> Two pages on, at p. 711: <em>&ldquo;No measurement of absolute or preferred rotation has been made to test whether the Earth is rotating or its surroundings. Until such a test is performed, Mach&rsquo;s principle is a valid statement; it has not been disproven experimentally.&rdquo;</em> And in the Sagnac chapter, numbered point 16 at p. 741: <em>&ldquo;By Mach&rsquo;s principle the Sagnac effect cannot distinguish between whether the Earth actually rotates and the ether is at rest, or the Earth is at rest and the ether whirls around it.&rdquo;</em> That is an indistinguishability claim, and on its own terms it is correct. Point 15, immediately above it, is even-handed in the same way: <em>&ldquo;A free gyroscope can be used to measure the rotation of the gimbal mounting; a Sagnac interferometer measures its angular velocity with respect to the local inertial (Geocentric) frame.&rdquo;</em></p>
<p><strong>But it does not stop at the disjunction, and neither should we.</strong> It would be the same trick in reverse to quote the book up to <em>&ldquo;cannot distinguish&rdquo;</em> and present it as neutral. A few pages later, answering the claim that Michelson&ndash;Gale shows the Earth rotating with respect to the heavens, the third numbered response at p. 745 drops the hedge entirely: <em>&ldquo;Just as the free mechanical motion of the Foucault pendulum defined a plane of motion relative to the rotating heavens, the free motion of the Michelson-Gale light ring defined a plane of radiation relative to the same heavens.&rdquo;</em> The heavens rotate; that is the book&rsquo;s position, stated flat. The refutation below answers that, at that strength.</p>
<p><strong>The detail on the same page that the list could not carry.</strong> Immediately before those responses, at p. 745, the book derives the Michelson&ndash;Gale time difference as &Delta;<em>t</em> = 4<em>A&omega;</em>&nbsp;sin&nbsp;&phi;/<em>c</em>&sup2; and explains the latitude factor geometrically: the Earth&rsquo;s axis of rotation projects onto the apparatus at an angle corresponding to the latitude; at the equator the polar axis lies parallel to the loop and there is no effect; at either pole it is perpendicular and the effect is maximal. That explanation is available only if the plane of the apparatus tips as you carry it over the surface &mdash; which is to say only on a globe. <strong>Sungenis and Bennett are geocentrists, not flat-earthers</strong>, and their spherical Earth is load-bearing in their own arithmetic.</p>
<p><strong>The objection the book prints against itself.</strong> At p. 310, footnote 615, the book reproduces &mdash; in its own words, &ldquo;Sciama quotes Eddington&rsquo;s objection to Mach&rdquo; &mdash; the sentence <em>&ldquo;We do not believe that if the heavenly bodies were all annihilated it would upset the gyrocompass.&rdquo;</em> That footnote hangs off a passage about relativity wanting things both ways, and this entry takes no view on what the book concludes from it. It is quoted for one thing only: a century ago, both sides of the Mach argument already understood the gyrocompass to be where the question sits.</p>
<p><strong>What this passage is being cited as.</strong> The earliest text located that carries this content in the form the item uses. It is an ancestor and not evidence of origination. The compressed word <em>sky-locked</em> is not located in the OCR of either Sungenis volume; the word <em>gyro</em> is not located anywhere in the archive.org OCR of Marshall Hall&rsquo;s <em>The Earth Is Not Moving</em> (1991), where the corresponding mechanical argument is about the Foucault pendulum. And the fact the item leans on &mdash; that a free gyroscope holds its axis against the stars rather than the ground &mdash; is ordinary navigation physics that predates the movement: L&eacute;on Foucault built the gyroscope in 1852 to demonstrate it. Our record credits nobody with this argument, and this entry does not change that.</p>"""),

    steelman=dict(
        description="""<p><strong>SURFACE (weak &mdash; do not use).</strong> &ldquo;The gyrocompass finds north by sensing the Earth&rsquo;s rotation, so it proves the Earth rotates.&rdquo; This loses, and it loses to the source&rsquo;s own page. A gyrocompass senses rotation with respect to the <em>local inertial frame</em>. Nothing in the instrument tells you whether that frame is fixed and the Earth turning, or the Earth fixed and the frame dragged round by a turning cosmos. Anyone opening with the surface version will be shown Mach&rsquo;s principle and will have nothing to say.</p>
<p><strong>DEEPER.</strong> The item&rsquo;s premise is literally true of a free gyroscope, and it is the mainstream reference works that say so. Wikipedia&rsquo;s own article on the gyrocompass puts it this way: a spun-up wheel &ldquo;will normally maintain its original orientation to a fixed point in outer space (not to a fixed point on Earth).&rdquo; That is <em>sky-locked</em>, in three words, from a source nobody in this argument would call partisan. It is why an aircraft&rsquo;s directional gyro wanders against the compass card and gets realigned every ten to fifteen minutes, and why a mechanical heading indicator carries a latitude nut &mdash; see <a href="#ARG-A07">ARG-A07</a>. An instrument that has to be dragged back into line with the ground several times an hour is not obviously an instrument that is referenced to the ground.</p>
<p><strong>KERNEL.</strong> The strongest form is the source&rsquo;s, and it is real physics rather than rhetoric. Mach&rsquo;s principle says the inertial field is set by the mass distribution of the universe; a rotating shell of distant matter therefore produces, inside itself, the same Coriolis and centrifugal terms as a rotating observer inside a still one. This is not a fringe conjecture. It is a general-relativistic calculation with a hundred years of literature behind it &mdash; Hans Thirring did the rotating-shell interior in 1918, Brill and Cohen sharpened it in <em>Physical Review</em> 143:1011 (1966), and Gravity Probe B measured frame dragging around the actual Earth in 2011 to about 19 per cent. So the kernel is: <em>every gyroscopic instrument on the planet measures relative rotation between the Earth and the cosmos, the physics of dragged inertial frames is mainstream and measured, and a gyroscopic reading cannot apportion that relative rotation between the two bodies.</em> All of that is correct, and it is why this page does not argue that a gyrocompass proves the Earth spins.</p>""",
        why_it_doesnt_save_claim="""<p>Because what Mach&rsquo;s principle buys is an equivalence between <strong>rotations</strong>. It buys nothing whatever about <strong>shape</strong> &mdash; and the list this item appears on is a flat-earth list.</p>
<p>Grant the whole Machian package. The inertial field inside the shell is then the same field an observer would see if the shell stood still and everything inside it turned; that is the point of the calculation. Now ask what a gyroscopic instrument standing on a surface inside that field actually reads. The answer depends on one thing only: the angle between the <em>local vertical at the instrument</em> and the rotation axis. On a sphere that angle is the co-latitude, and it sweeps through a right angle between equator and pole, which is why the free-gyro azimuth drift goes as sin&nbsp;&phi; and the tilt rate &mdash; and with it the gyrocompass&rsquo;s whole north-seeking torque &mdash; goes as cos&nbsp;&phi;. On a plane the local vertical is a single direction shared by every point on it, so that angle is the same everywhere, and no gyroscopic quantity can vary from place to place at all.</p>
<p>That conclusion does not care which body is turning, and it does not care which way the axis points. It is a fact about the surface. So the source&rsquo;s best argument, taken at full strength and conceded in full, delivers a <em>spherical</em> stationary Earth &mdash; which is what Sungenis and Bennett actually hold, and what their own Michelson&ndash;Gale derivation on p. 745 requires. Transplanted onto a flat Earth it stops working, and it stops working on the one quantity every ship&rsquo;s bridge in the world measures daily.</p>"""),

    refutation="""<p><strong>Start with the concession, because it is large and it is permanent.</strong> A free gyroscope is sky-locked. That is not a flat-earth talking point, it is how the instrument works, and the mainstream reference on the gyrocompass says so in one sentence: a spun-up wheel &ldquo;will normally maintain its original orientation to a fixed point in outer space (not to a fixed point on Earth).&rdquo; Second concession, bigger: <strong>no gyroscopic instrument can tell you whether the Earth turns or the cosmos turns around it.</strong> It measures rotation relative to the local inertial frame, and on a Machian model the frame is dragged by the turning cosmos and every reading comes out identical. The source makes that argument, it is right, and this page grants it whole. Anyone answering this item with &ldquo;a gyrocompass cannot work unless the Earth spins&rdquo; has skipped the step the source will not let them skip, and will lose the exchange on it.</p>

<h4>1. What the instrument is, since the item names it and the name matters</h4>

<p>A gyrocompass is not a free gyroscope. It is a free gyroscope that has been deliberately <em>broken</em> as a free gyroscope, and the breaking is the entire mechanism. The rotor is constrained so its spin axis stays roughly in the horizontal plane and is made bottom-heavy &mdash; gravity control, by pendulous mass or by a mercury ballistic. Now the Earth&rsquo;s rotation carries the local horizontal round underneath a spin axis that is trying to hold still against the stars; one end of the axis rises; the weight applies a torque; and a gyroscope answers a torque by precessing at right angles to it, so the axis swings in azimuth. The swing is towards the meridian, it overshoots, and damping brings it to rest pointing true north, typically over some hours. The oscillation period is tuned to the Schuler period of 84.4 minutes so that the ship&rsquo;s own accelerations do not throw it off.</p>

<p>So the item has named the one gyroscopic instrument in the world that is engineered <em>not</em> to be sky-locked. Its whole design is the conversion of a sky-locked axis into an Earth-locked one, and the conversion is powered by the relative rotation of the two. <a href="#ARG-A07">ARG-A07</a> handles the free-gyro and ring-laser items; this one is about the machine that eats the drift.</p>

<h4>2. Two numbers, and they are the argument</h4>

<p>Resolve the rotation vector <strong>&Omega;</strong> &mdash; magnitude 7.292115 &times; 10<sup>&minus;5</sup> rad s<sup>&minus;1</sup>, or 15.041&deg; per hour &mdash; into the local vertical and the local horizontal at the instrument. Two rates follow, and both are in the training material a watchkeeping officer sits an exam on:</p>

<p style="margin-left:1.5em">azimuth drift of a free gyro = 15&deg;&nbsp;&times;&nbsp;sin&nbsp;&phi; per hour<br>
tilt rate of a horizontal axis = 15&deg;&nbsp;&times;&nbsp;cos&nbsp;&phi;&nbsp;&times;&nbsp;sin&nbsp;(azimuth) per hour</p>

<p>(The training tables round the constant to 15&deg;; the rate the instrument actually senses is the sidereal one, 15.041&deg; per hour, a difference of 0.27 per cent that matters for the large ring lasers at <a href="#ARG-A02">ARG-A02</a> and not for a ship&rsquo;s compass.)</p>

<p>The second of those is the gyrocompass&rsquo;s power supply: no tilt, no torque, no north-seeking. Hence the standard statement of the directive force &mdash; it &ldquo;is maximum at the equator and decreases to zero at the poles.&rdquo; A gyrocompass is at its best on the equator and gives up entirely at the pole, which is the reverse of the intuition most people arrive with, and it is checkable by anyone who has stood a watch.</p>

<p>Notice what the two rates are. They are not two independent empirical curves. They are the two components of a single vector of fixed length, so sin&sup2;&nbsp;&phi;&nbsp;+&nbsp;cos&sup2;&nbsp;&phi;&nbsp;=&nbsp;1 and their quadrature sum is the same 15.041&deg; per hour at every latitude on Earth. The only thing that changes from place to place is <em>how that fixed vector is split between vertical and horizontal</em> &mdash; and that split is nothing but the angle between the local vertical and the rotation axis. The equator is the degenerate case worth checking by hand: there &Omega; lies in the horizontal plane pointing due north, so a free gyro aimed north is aligned with it and holds still against both the sky and the ground at once, while a gyro aimed east tilts at the maximum rate. Both facts fall out of the same decomposition.</p>

<h4>3. The step that flat and round part company on</h4>

<p>On a sphere, the local vertical is the radius, so the angle between it and the polar axis is the co-latitude and sweeps through 90&deg; from equator to pole. That is where sin&nbsp;&phi; and cos&nbsp;&phi; come from, and there are no free parameters in it.</p>

<p><strong>On a plane, the local vertical is one and the same direction at every point of the surface.</strong> The angle it makes with a fixed rotation axis is therefore identical everywhere, whatever that axis is and whichever body is doing the rotating. A rotating dome, a rotating disc, an ether whirl about the pole star &mdash; it makes no difference to this, because nothing in the reasoning depends on what is producing the rotation. It follows that on a flat Earth <em>no gyroscopic quantity can depend on where you are standing</em>. Free-gyro drift would be the same at Singapore and Reykjavik; the tilt rate would be the same; the gyrocompass&rsquo;s directive force would be the same. If the dome turns about an axis perpendicular to the plane, that common tilt rate is zero, and no gyrocompass would settle anywhere on Earth.</p>

<p>Turn that around and it is a positive result rather than a refutation: <strong>a gyrocompass measures the angle between the local vertical and the Earth&rsquo;s rotation axis, from inside a closed steel box, with no horizon in view and no photograph involved.</strong> Watching that angle change as you sail is watching the surface curve.</p>

<h4>4. The paper trail, which is in the regulations and the sales literature</h4>

<p>None of the above is a theoretical nicety maintained by cosmologists. It is written into the documents that govern commercial shipping.</p>

<p><em>The international standard.</em> IMO Resolution A.424(XI), <em>Performance standards for gyro-compasses</em>, requires that the compass &ldquo;settle within six hours in latitudes of up to 60&deg;&rdquo;, and specifies the tolerances as trigonometric functions of where the ship is: the settle point error shall &ldquo;not exceed &plusmn; 0.75 x secant latitude&rdquo;, and the residual steady state error after speed and course correction at twenty knots &plusmn; 0.25 &times; secant latitude. Secant latitude is 1/cos&nbsp;&phi; &mdash; precisely the reciprocal of the directive force. The standard also requires that &ldquo;means should be provided for correcting the errors induced by speed and latitude.&rdquo; A regulator writing rules for a flat Earth has no reason to reach for a trigonometric function of position, and no reason to stop the standard at 60&deg;.</p>

<p><em>The datasheet.</em> Sperry Marine&rsquo;s NAVIGAT X MK 2, a spinning-mass gyrocompass sold with twin rotors at 19,000 rpm, publishes its accuracy the same way: static error &ldquo;&lt; 0.1&deg; secant latitude&rdquo;, dynamic &ldquo;&lt; 0.4&deg; secant latitude&rdquo;. The globe&rsquo;s trigonometry is in the specification a buyer holds the manufacturer to.</p>

<p><em>The correction table.</em> A gyrocompass on a moving ship settles off true north, because the vessel&rsquo;s own northward motion adds to the Earth-rate the instrument is chasing. The correction, in the standard maritime form, is tan&nbsp;&delta; = &minus;<em>V</em>&nbsp;cos&nbsp;<em>C</em>&nbsp;/&nbsp;(900&nbsp;cos&nbsp;&phi;&nbsp;+&nbsp;<em>V</em>&nbsp;sin&nbsp;<em>C</em>), with <em>V</em> in knots and <em>C</em> the course. The 900 is the eastward speed of the ground at the equator, and the cos&nbsp;&phi; scales it to your latitude. Look at where that number comes from: the equator is 21,600 nautical miles round, because a nautical mile <em>is</em> one minute of arc of a great circle and there are 360 &times; 60 of them; 21,600 divided by 24 hours is 900 knots exactly. The constant in every ship&rsquo;s speed-error table is the Earth&rsquo;s rotation expressed in units of the Earth&rsquo;s own curvature. (Against the stars the figure is 902.5 knots; the 0.3% difference sits far inside the instrument&rsquo;s error budget and nothing here rests on it.)</p>

<h4>5. Its twin, which points the other way and settles the sign</h4>

<p>The Foucault pendulum is the same vector read on its other component: its precession goes as sin&nbsp;&phi;, it turns clockwise in the northern hemisphere and counterclockwise in the southern, and at the equator &ldquo;the plane of oscillation remains fixed relative to Earth.&rdquo; Gyrocompass directive force peaks exactly where the pendulum stops, and stops exactly where the pendulum is fastest. Two instruments of different physics, complementary across the whole range of latitude, summing to one constant vector. The hemispheric reversal is the part no single dome rotation can produce: one rotation about one axis over one plane has one sense, everywhere on the plane. See <a href="#ARG-A06">ARG-A06</a>.</p>

<h4>6. What the list says about this two hundred items earlier</h4>

<p>Take the item at its word. <em>Sky-locked</em> means the axis holds against the heavens and therefore turns, once a day, with respect to the deck it is bolted to. Item 229 is thus a concession that a gyroscopic instrument registers a daily rotation between ground and sky &mdash; and item 225, <em>&ldquo;Ring laser gyro corrections&rdquo;</em>, concedes the same thing from the engineering side, since a correction is only needed if there is something to correct for. Now item 12, on the same list: <em>&ldquo;Gyroscope anomalies indicating no rotation.&rdquo;</em> And item 224, five lines above item 229 in the same run of instrument fragments: <em>&ldquo;No rotation proof mechanical.&rdquo;</em> Those deny exactly what 229 and 225 assume. Under every model anyone in this argument holds, the ground and the heavens turn relative to one another once a day &mdash; otherwise there is no day &mdash; so an instrument cannot be holding still against both, and a list cannot have it both ways either.</p>

<p><strong>One item of the four has a defence, and it should be stated.</strong> Item 19, <em>&ldquo;Gyroscopes stable absent recalibration&rdquo;</em>, is a fair report about cheap mechanical gyroscopes, whose bearing friction really does swamp a rate of four thousandths of a degree per second &mdash; that is worked through at <a href="#ARG-A07">ARG-A07</a> and it is not counted here. The contradiction that survives is between items 12 and 224 on one side and items 225 and 229 on the other, and it does not turn on instrument grade: it is a straight disagreement about whether there is a daily relative rotation for a gyroscope to register at all. <strong>The list carries both halves and offers each as a proof.</strong> That is what the verdict chip on this entry names, and it is checkable in a minute against the specimen itself.</p>

<h4>7. What the verdict does and does not range over</h4>

<p>It does <em>not</em> claim that the gyrocompass settles whether the Earth turns or the heavens do. It does not, the source says it does not, and the source is right; that question is argued at <a href="#ARG-R01">ARG-R01</a> and <a href="#ARG-A22">ARG-A22</a>, on different ground. What is claimed here is narrower and harder: the item asserts, of a specific instrument, a behaviour that instrument is built to prevent; the latitude signature of the thing it actually does is a measurement of the surface&rsquo;s shape and is unavailable on a plane whatever rotates; and the list carries, elsewhere in its own numbering, items that flatly contradict it. The argument arrives on a flat-earth list out of a <em>geocentric</em> book whose own Michelson&ndash;Gale derivation, four pages later, needs the globe to produce its sin&nbsp;&phi;. It is the lineage problem this review exists to document, in a single four-word item.</p>""",

    advocate=dict(
        best_defense=(
            "Four moves, and the third is the one you should worry about. "
            "First: you conceded Mach and then changed the subject. Item 229 is a claim "
            "about what the instrument is referenced to, and on that you have now agreed "
            "with us twice in your own opening paragraph — a free gyro holds against the "
            "stars, and no gyroscope can say which body turns. Everything after that is "
            "you arguing about the shape of the Earth with a man who came to talk about "
            "its motion. "
            "Second: your cos-phi theorem assumes the only thing that can generate these "
            "effects is a rigid rotation about a single fixed axis. We do not hold that. "
            "The firmament is not a flywheel; it is an ether, and an ether over a plane "
            "moves as a vortex whose circulation varies with radius. Give me a radial "
            "profile and I will give you any latitude dependence you like, including "
            "yours. You have refuted a model nobody defends. "
            "Third: 'latitude' on our map is distance from the centre. So when you "
            "announce that gyroscopic behaviour varies with latitude, you have discovered "
            "that it varies with where you are standing, which we already knew, and then "
            "relabelled that discovery 'curvature'. The trigonometry is your "
            "parametrisation, not a finding. "
            "Fourth: look at what your best evidence turned out to be. A shipping "
            "regulation and a manufacturer's brochure. Both were written by people who "
            "assumed the globe before they started, and 'secant latitude' is in the "
            "firmware because the firmware was coded from the model. You have not shown "
            "me one settling curve from one vessel. You have shown me the paperwork of an "
            "industry and called it a measurement."),
        survives=4,
        preemptive=(
            "Rated 4: no physics error in it, and moves two and three are serious. Five "
            "things must stay in the published text and a reviewer should check each. "
            "(1) The concessions stay in the FIRST paragraph and stay in bold. If they "
            "migrate down the page, move one lands and the entry looks like it was "
            "caught rather than volunteering. The seventh section must also stay, because "
            "it states in our own voice that the verdict does not range over "
            "Earth-versus-cosmos rotation — which is what makes move one a restatement of "
            "our position rather than a hit on it. "
            "(2) Against move two, the load must rest on the QUADRATURE CONSTRAINT, which "
            "is already in section 2 and must not be cut as arithmetic decoration: the two "
            "rates are not two free curves to be fitted by a radial profile, they are the "
            "two components of one vector whose magnitude is 15.041 deg/hr at every "
            "latitude and is independently known. A vortex profile has to reproduce a "
            "two-component field of constant magnitude whose direction rotates through "
            "exactly 90 degrees between centre and rim, while the surface it sits over "
            "stays flat. "
            "(3) Against move three, the answer is in the same place and must be stated as "
            "the theorem it is: the objection is not that things vary with position, it is "
            "that the local vertical must make a DIFFERENT angle with the rotation axis at "
            "different places. A surface whose normal turns through a right angle across "
            "it is not a plane — that is what 'curved' means. The escape reintroduces "
            "curvature under the word 'ether'. Keep the sentence 'That conclusion does not "
            "care which body is turning, and it does not care which way the axis points.' "
            "(4) Against move four, do not let the IMO resolution and the Sperry datasheet "
            "be described anywhere as the evidence. They are corroboration, and section 4 "
            "should read that way. The load-bearing observations are that a gyrocompass "
            "settles at all at low latitude and stops settling at high latitude, and that "
            "the Foucault sense reverses between hemispheres — both observable in public "
            "installations by someone who trusts no manufacturer. Section 5 carries the "
            "second one and must not be trimmed. "
            "(5) The honest limit gets published rather than hidden: no raw settling data "
            "from any vessel was obtained for this entry, and the research notes say so. "
            "If a future editor wants to close move four properly, that is the datum to "
            "go and get."),
    ),

    straw_man=dict(
        identified=True,
        detail=("The response at printed p. 710 characterises the geokinetic case as "
                "depending on &ldquo;the assumption that the inertial effects can only be "
                "caused by the Earth&rsquo;s rotation&rdquo;, with the Machian alternative "
                "&ldquo;implicitly denied&rdquo;. That misdescribes the state of the "
                "physics. The alternative is not denied in the literature; it is computed "
                "in it. The interior of a rotating mass shell is a standard "
                "general-relativistic problem &mdash; Thirring published it in 1918, Brill "
                "and Cohen sharpened it in <em>Physical Review</em> 143:1011 (1966) &mdash; "
                "and the dragging of inertial frames by a rotating body was measured around "
                "the Earth itself by Gravity Probe B in 2011, to about 19 per cent. What a "
                "stationary-Earth cosmology owes is not an acknowledgement that the "
                "equivalence exists but a dynamics for the rotating cosmos, which is the "
                "argument at <a href=\"#ARG-R01\">ARG-R01</a>. Two things this entry does "
                "<em>not</em> call straw men, because they are not: the book&rsquo;s "
                "statement of the geokinetic claim at p. 709 is a fair statement of the "
                "popular case, and its indistinguishability claim at p. 741 is correct. The "
                "straw man to watch on our own side is the reflex reply that a gyrocompass "
                "proves the Earth spins, which this page does not run.")),

    compression=dict(
        assessed=True, drifted=True,
        list_phrasing="Gyrocompass sky-locked.",
        source_wording=("“The Sagnac effect used in laser gyroscopes and the precession of "
                        "mechanical gyrocompasses indicate the Earth is spinning.” … "
                        "“No measurement of absolute or preferred rotation has been made to test "
                        "whether the Earth is rotating or its surroundings. Until such a test is "
                        "performed, Mach's principle is a valid statement; it has not been "
                        "disproven experimentally.”"),
        drift_type="force_upgraded",
        note=("<p><strong>The wording barely moves and the speech act changes completely.</strong> "
              "In the source, the first sentence is <em>the opposing side&rsquo;s claim</em>, set "
              "out at p. 709 so that it can be answered; the answer, running from p. 710, is that "
              "nobody can tell which body is turning and that Mach&rsquo;s principle &ldquo;has "
              "not been disproven experimentally&rdquo;. A not-disproven is not a result. The "
              "list keeps one horn of an explicit indistinguishability and publishes it as an "
              "affirmative fact about an instrument &mdash; the <code>force_upgraded</code> "
              "pattern already worked at <a href=\"#ARG-R01\">ARG-R01</a>, where a concession its "
              "own author called &ldquo;forcing an open door&rdquo; arrives on a list as a "
              "proof.</p>"
              "<p><strong>A second drift travels with it that the seven values have no word "
              "for.</strong> Sungenis and Bennett are geocentrists: their Earth is a globe, it "
              "simply does not move. Four pages after the passage above, at p. 745, their own "
              "derivation of the Michelson&ndash;Gale effect is &Delta;<em>t</em> = "
              "4<em>A&omega;</em>&nbsp;sin&nbsp;&phi;/<em>c</em>&sup2;, and they explain the "
              "sin&nbsp;&phi; by the apparatus tipping relative to the polar axis as it is "
              "carried over the surface &mdash; zero at the equator, maximum at the poles. That "
              "reasoning needs the sphere. The item removes the sphere and keeps the conclusion. "
              "It is not a hedge dropped, not a scope widened and not a category shifted: it is a "
              "conclusion lifted out of the model that made it true. <code>force_upgraded</code> "
              "is recorded because it is the plainest and most checkable of the two, and both "
              "texts are printed above for the reader to judge.</p>"
              "<p><strong>The gap is the finding, and here it costs the list its own coherence.</strong> "
              "The source&rsquo;s claim &mdash; gyroscopic instruments measure relative rotation "
              "and cannot apportion it &mdash; is true, careful, and survives this page intact. "
              "The compressed version is the one that circulates, and it asserts something about "
              "a gyrocompass that is false of a gyrocompass, on a list that elsewhere asserts the "
              "opposite of it in items 12 and 19. The refutation above answers the source at the "
              "source&rsquo;s strength, by conceding the Machian point entirely and moving to the "
              "one thing Mach does not cover; the drift is published here because the reader "
              "meets the four words, not the chapter.</p>")),

    verdict_challenge=dict(challenged=False, proposed_verdict=None, reasoning=None),

    people=["PER-SUNGENIS"],
    related=["A02", "A06", "A07", "A22", "A26", "R01", "R08"],

    sources=[
        dict(label="Sungenis & Bennett, Galileo Was Wrong Vol. I — Internet Archive OCR (item "
                   "GallileoWasWrong); ch. 12, the three geokinetic claims at printed p. 709, "
                   "the Mach response at pp. 710–711, the Sagnac points 15–16 at p. 741, the "
                   "Michelson–Gale response and Δt = 4Aω sinφ/c² at p. 745, the Eddington-via-"
                   "Sciama gyrocompass footnote at p. 310 n. 615",
             url="https://ia801806.us.archive.org/5/items/GallileoWasWrong/Gallileo%20was%20wrong.pdf"),
        dict(label="Sungenis & Bennett, Galileo Was Wrong Vol. II (7th ed., 2013) — the same "
                   "passage reprinted at ch. 10 “Technical and Summary Analysis of Geocentrism”, "
                   "printed pp. 157–158",
             url="https://archive.org/stream/GalileoWasWrongTheChurchSungenisRobertA.Bennett4276/Galileo%20Was%20Wrong_%20The%20Church%20%20-%20Sungenis,%20Robert%20A.%20&%20Bennett,_4276_djvu.txt"),
        dict(label="Wikipedia — Gyrocompass: a spun-up wheel “will normally maintain its original "
                   "orientation to a fixed point in outer space (not to a fixed point on Earth)”; "
                   "van den Bos 1885, Anschütz-Kaempfe 1906/1908, Sperry 1908 (US patent "
                   "1,242,065), C. Plath 1913",
             url="https://en.wikipedia.org/wiki/Gyrocompass"),
        dict(label="IMO Resolution A.424(XI), Performance standards for gyro-compasses — settle "
                   "“within six hours in latitudes of up to 60°”; settle point error “± 0.75 x "
                   "secant latitude” (5.1.2); residual steady state error ± 0.25 × secant latitude "
                   "at twenty knots (5.2.3.a); correction for speed and latitude (9.2). Transcribed "
                   "by the Netherlands Regulatory Framework — Maritime",
             url="https://puc.overheid.nl/nsi/doc/PUC_2467_14/1/"),
        dict(label="Sperry Marine NAVIGAT X MK 2 digital gyrocompass datasheet — twin rotors at "
                   "19,000 rpm; static accuracy “< 0.1° secant latitude”, dynamic “< 0.4° secant "
                   "latitude”",
             url="https://www.bodc.ac.uk/data/documents/nodb/pdf/Sperry_Marine_gyro.pdf"),
        dict(label="Maritime University of Szczecin, gyrocompass laboratory notes — the speed "
                   "error tan δ = −(V cos KR)/(900 cos φ + V sin KR), “at any latitude other than "
                   "the equator, this velocity becomes 900 times the cosine of the latitude”, and "
                   "the 84.4-minute Schuler tuning",
             url="http://irm.am.szczecin.pl/images/instrukcje/PUN/gyro1.pdf"),
        dict(label="The Nautical Site, gyro compass notes — “Rate of tilting in degrees per hour = "
                   "15˚ sine Azimuth * cosine Latitude”; “Rate of Drift in degrees per hour = 15˚ "
                   "sine Latitude”",
             url="http://thenauticalsite.in/NauticalNotes/MagCompass/MyMagCompass-Lesson03-GyroCompass.htm"),
        dict(label="Cult of Sea, Gyro Compass — “the directive force is maximum at the equator and "
                   "decreases to zero at the poles”, and the hours needed to settle after a power "
                   "loss",
             url="https://www.cultofsea.com/bridge-equipment/gyro-compass-basic-principle-operation-and-usage-on-ships/"),
        dict(label="Knowledge of Sea, Gyro Compass — an independent statement of the same two "
                   "rates, 15 cos Latitude × sine Azimuth and 15 sine Latitude",
             url="https://knowledgeofsea.com/gyro-compass-2/"),
        dict(label="Wikipedia — Foucault pendulum: precession proportional to the sine of the "
                   "latitude, clockwise at the north pole and counterclockwise at the south, and "
                   "at the equator “the plane of oscillation remains fixed relative to Earth”",
             url="https://en.wikipedia.org/wiki/Foucault_pendulum"),
        dict(label="Brill & Cohen, “Rotating Masses and Their Effect on Inertial Frames”, Phys. "
                   "Rev. 143:1011 (1966) — the rotating-shell interior result Thirring began in "
                   "1918, i.e. the Machian equivalence the source invokes, computed inside general "
                   "relativity",
             url="https://journals.aps.org/pr/abstract/10.1103/PhysRev.143.1011"),
        dict(label="Pfister, “Mach's Principle, Dragging Phenomena, and Gravitomagnetism” — review "
                   "of the rotating-shell and frame-dragging literature",
             url="https://link.springer.com/chapter/10.1007/978-3-319-15036-9_4"),
        dict(label="Wikipedia — Frame-dragging: Gravity Probe B “demonstrated the frame-dragging "
                   "effect with an error of about 19 percent”, announced 4 May 2011",
             url="https://en.wikipedia.org/wiki/Frame-dragging"),
        dict(label="Marshall Hall, The Earth Is Not Moving (1991) — searched for this entry; the "
                   "mechanical argument in the archive.org OCR is the Foucault pendulum",
             url="https://archive.org/details/the-earth-is-not-moving"),
    ]),
}
