# -*- coding: utf-8 -*-
"""Batch 11 — B12. "Polar navigation and dead reckoning imply a dome/disc."

Three items, all three re-verified against the live specimen page 2026-08-10:
128 "Navigation charts fixed pole.", 408 "Polar navigation star dome.",
409 "Dead reckoning dome compass." Verdict REFUTED, kept.

Research notes for whoever picks this up next.

1. OUR RECORD'S ORIGINATOR IS A GUESS AND A BETTER-EVIDENCED ANCESTOR EXISTS.
   `clusters.py` credits Charles K. Johnson, *Flat Earth News*, 1972. No text of
   Johnson's carrying a navigation argument was reached for this entry, and there is
   a fully documented Victorian chain that carries all three items:

     Rowbotham, *Earth Not a Globe* (1865), the circumnavigation section — meridians
     "converge to the northern centre of the Earth"; a mariner steering due west
     "practically circumnavigates a plane surface"; the southern degree-of-longitude
     claim with a numeric prediction; the Milner shipwreck quotation.
     -> Carpenter, *One Hundred Proofs* (1885), proofs 8-16 — the same material cut
     into numbered one-line proofs, which is the FORM this specimen is written in.
     -> Dubay, *200 Proofs* (2015), proofs 34-39 and 108-111 — including the Milner
     quotation reproduced from Rowbotham, footnote and all.

   The Milner quotation is the smoking gun for the chain: Rowbotham 1865 prints it
   with footnote [7] "'Tour through Creation,' by the Rev. Thomas Milner, M.A.", and
   Dubay prints the same passage 150 years later ("navigators to India have often
   fancied themselves east of the Cape when still west..."). Reported up in
   `record_problems`, NOT edited here — this agent owns one file. The gloss below
   therefore claims an ANCESTOR and nothing more, in the E08 pattern, and says nothing
   about the originator field either way.

2. THE PASSAGE CHOSEN, AND WHY. Carpenter proof 14, not Rowbotham. Two reasons: the
   specimen is a numbered proof-list and Carpenter is where that form starts, and
   proof 14 is the one place in the whole lineage where the argument states a
   MEASURABLE PREDICTION - parallels of latitude "INCREASE ... beyond the equator
   (going southwards)" - and ties it to dead reckoning in the same sentence ("causing
   the sailor to be continually getting out of his reckoning"). Both PD, so quote at
   length. Rowbotham and Dubay are quoted in the gloss.

3. THE HEDGE RULE RUNS BACKWARDS ON THIS ONE, AND THAT IS THE FINDING. Nearly every
   argument audited so far is FIRMER in the list than in the source. Here the sources
   are firmer than the list. Carpenter states his as a flat proof; Rowbotham stakes a
   number on it; Dubay repeats both. The three list items keep only "charts have a
   fixed pole", "polar navigation uses a star dome", "dead reckoning uses a compass" -
   all of which are true on the globe too and assert nothing. So do NOT write this up
   as "the list overstates its source"; it does the opposite, and the honest finding
   is that the compression dropped the falsifiable half. Recorded drift_type is
   `unsourced_addition` because the plainest checkable change is the word "dome" (see
   6); the note carries the structural one and says the enum has no value for it.

4. THE LOAD-BEARING ARGUMENT IS SCALE-FREE, AND CARPENTER SUPPLIES ITS PREMISE.
   Proof 14: parallels of latitude "are circles, which increase, progressively, from
   the northern centre to the southern circumference." Grant exactly that geometry -
   pole at the centre, meridians as radii, south radially outward - and the east-west
   length of a parallel is r x delta-lambda with r increasing monotonically southward.
   So on EVERY north-centred disc, whatever its radial scale function, a degree of
   longitude must get LONGER going south, without limit, past the equator. Measured
   (GRS80, recomputed here 2026-08-10): 111.32 km at the equator, 78.85 km at 45S,
   71.70 km at 50N. It shrinks. That result does not depend on the azimuthal-
   equidistant map, so the "you have refuted Gleason, not us" escape is closed before
   it is opened. Keep it that way — the AE numbers below are illustration, not load.

5. THE ARITHMETIC, ALL OF IT REPRODUCED HERE 2026-08-10 (GRS80: a = 6378137 m,
   e^2 = 0.00669438; great circles on R = 6371.0088 km).
   (a) Degree of longitude = (pi/180) a cos(phi) / sqrt(1 - e^2 sin^2 phi):
       equator 111.32 km; 45 deg 78.85 km (42.57 nmi, 48.99 statute mi); 50 deg
       71.70 km (38.71 nmi, 44.55 statute mi). Rowbotham's Mercator-chart table gives
       42.45 and 38.57 nmi - right to within 0.3%. His PLANE prediction for 45 deg S
       was 69.44 statute miles; measured 48.99; he is 42% high. His northern figure
       (45 statute miles at 50 deg N) is right to within 1%.
   (b) Rowbotham's three southern legs, great-circle: Cape Town-Sydney 5,946 nmi,
       Sydney-Cape Horn 5,065, Cape Horn-Cape Town 3,612. Sum 14,623 nmi, against the
       22,000 nmi he takes from "practical navigators" and against the 15,282 nmi his
       own table gives for the 45 deg parallel. NOTE the slip: 360 x 42.45 = 15,282,
       but the Gutenberg text of 1865 prints 14,282, which inflates his claimed error
       by a thousand miles. Low-stakes and possibly a typesetting fault; scoped as
       "as printed in" wherever it is mentioned.
   (c) The same 22,000 nmi figure exceeds the AZIMUTHAL-EQUIDISTANT flat map's own
       prediction for that parallel (2 pi R theta = 31,440 km = 16,975 nmi) by 30%.
       The Victorian data fit neither model, which is what you expect of sailing-route
       distances being compared with arcs of a parallel.
   (d) AE-disc chord vs great circle, same endpoints: Sydney-Perth 8,301 vs 3,290 km
       (2.52x); Sydney-Santiago 25,684 vs 11,347 (2.26x); Johannesburg-Sydney 23,481
       vs 11,041 (2.13x). London-New York is 1.07x, which is why the discrepancy is
       invisible on northern routes and why the southern ones are the test.
   (e) Schuler period 2 pi sqrt(R/g) = 84.4 min for R = 6371 km, g = 9.80665. Bowditch
       art. 618 gives the gyrocompass precession ellipse as "about 84 minutes" and
       says in its own parenthesis that this is "the period of oscillation of a
       pendulum with an arm equal to the radius of the earth."

6. THE WORD "DOME". Two of the three items carry it. Searches run 2026-08-10: the
   Project Gutenberg text of Carpenter #55387 returns no hit for "dome"; the Project
   Gutenberg text of Rowbotham 1865 (#69892) returns one, "the dome of the Pantheon",
   in the Foucault-pendulum section; the archive.org OCR of Dubay's 200 Proofs
   (item 200ProofsEarthIsNotASpinningBall_201903) returns none. All three argue for a
   PLANE with a northern centre and a southern circumference, and Carpenter proof 11
   denies a southern pole outright. The dome is Sargent-era (2015) enclosed-world
   furniture bolted onto a Victorian navigation argument. Hence `unsourced_addition`.
   CAUTION on over-reading "star dome": the fragment is four words and admits at least
   two innocent readings - the celestial sphere used in sight reduction, and the
   aircraft ASTRODOME through which a bubble sextant was shot on polar routes. The
   entry answers both and says the fragment supports either.

7. BOWDITCH IS THE REAL SOURCE THE CLUSTER LACKS, AND IT CONCEDES THE PREMISE ON ITS
   OWN PAGE. *The American Practical Navigator* (NGA Pub. 9, 2002 ed.) is US
   government work, public domain, and available as wikitext on Wikisource. Do not
   flinch from these:
     ch. 24 art. 2400: dead reckoning "involves the determination of one's present or
       future position by projecting the ship's course and distance run from a known
       position";
     ch. 24, list of sailings: plane sailing solves for course, distance, difference
       of latitude and departure "in which the Earth is regarded as a plane surface".
   Both true, and both scoped in the same breath: "To calculate the longitude, the
   spherical sailings are necessary. Plane sailing is not intended for distances of
   more than a few hundred miles." And the mid-latitude formula printed a few articles
   later is p = DLo cos L_m - the cosine of the latitude, i.e. the convergence of
   meridians on a sphere, inside the "flat" method itself.
   Other Bowditch anchors used below: art. 602 (magnetic dip 0 deg at the magnetic
   equator to 90 deg at the magnetic poles; magnetic poles "near, but not coincidental
   with" the geographic ones); art. 620 (gyrocompass directive force "is maximum at
   the equator and decreases to zero at the poles"); art. 1524 (celestial sphere "an
   imaginary sphere of infinite radius with the Earth at its center"); art. 1529 (the
   navigational triangle is a SPHERICAL triangle, and "the terrestrial counterpart is
   also called a navigational triangle"); ch. 15 on the degree of latitude increasing
   "from about 59.7 nautical miles at the equator to about 60.3 nautical miles at the
   poles", with 60 "correct at about latitude 45 deg".

8. DEAD RECKONING IN THE SOUTHERN OCEAN - GET THE SIGN RIGHT. The lineage's own
   examples run in OPPOSITE directions, which a uniform expansion of southern
   parallels cannot produce. Dubay 37 has Wilkes "consistently east of his reckoning,
   sometimes over 20 miles in less than 18 hours" (~1.1 kn of unaccounted set, which
   is the Antarctic Circumpolar Current's order of magnitude; Donohue et al., GRL
   43:11760, 2016, measure its Drake Passage transport at 173.3 Sv). Milner's Cape
   example is the reverse - vessels "fancied themselves east of the Cape when still
   west", i.e. LESS easting than reckoned. Do not assign a named current to the Cape
   case; the mechanism there was not established for this entry and the argument does
   not need it. What the entry says is only that the errors are directional and
   locally opposite, and that a log measures speed through the water, not over ground.
9. THE TWO NAMED WRECKS IN THE LINEAGE'S OWN QUOTATION. Checked because they travel
   unchanged from 1865 to 2015. "A fine frigate, the 'Challenger,' in 1845" driven
   ashore on the African coast: the Royal Navy ship of that name whose loss is
   documented in the period is HMS Challenger (1826), a 28-gun sixth rate, wrecked off
   Mocha Island, CHILE, on 19 May 1835 - and Wikipedia's account notes that "overcast
   skies had prevented her from taking sightings since 17 May", i.e. a longitude
   carried on dead reckoning without a celestial fix, which is the mundane reading.
   Dubay prints a longer version of the Milner passage than the 1865 Earth Not a Globe
   carries, adding "How came Her Majesty's Ship 'Conqueror' to be lost?" - HMS
   Conqueror, 100 guns, was lost on Rum Cay, BAHAMAS, on 29 December 1861 (Royal
   Museums Greenwich), at 23 deg N. Say what is documented; do NOT write that Milner
   invented his example, because a merchant Challenger in 1845 was not run down and
   the 1881 third edition was not consulted.

10. VERDICT. REFUTED considered against MISLEADING, which is what the adjacent
    convenience-frame clusters carry (B11 radar/LiDAR, R08 Earth-fixed coordinates).
    Kept REFUTED, because the source version is not a framing complaint: Carpenter
    proof 14 and proof 16 make a quantitative claim about the southern hemisphere
    ("twice the distance"), Rowbotham stakes a number on it and asks for the geodetic
    measurement, and the measurement went the other way. An argument that named its
    own test and failed it is refuted rather than misleading. No verdict_challenge
    filed. If a future pass moves the originator to Rowbotham or Carpenter the verdict
    gets STRONGER, not weaker, which is the right direction for a record correction.

11. EDITION TRAPS. Rowbotham is quoted from the 1865 first book edition via Project
    Gutenberg #69892; the enlarged 1881 third edition was not reached (sacred-texts is
    behind a Cloudflare interstitial from this container) and every Rowbotham locator
    below says 1865 explicitly. This is the project's standing blind spot - see the
    A05/B04/B06/B08 corrections. Carpenter is Gutenberg #55387, which is the 5th
    edition, Baltimore 1885. Bowditch is the 2002 edition as transcribed on Wikisource;
    article numbers are that edition's and are given rather than page numbers.

12. DEFECTS IN OUR OWN RECORD, reported up, NOT edited here — see `record_problems`.
"""

ENTRY = {

"B12": dict(

    tldr=("Navigation really is built around a fixed pole, and the navigator's manual really "
          "does say that plane sailing treats the sea as a plane surface — for runs of a few "
          "hundred miles, after which the same page sends you to the spherical sailings. Where "
          "the Victorians took a risk was the next step: Carpenter and Rowbotham both held that "
          "parallels of latitude grow as you go south. They shrink. A degree of longitude "
          "measures 111.3 km at the "
          "equator and 78.8 km at 45°S, and no map with the pole at its centre and south "
          "running outward can produce that, whatever radial scale it uses."),

    passage=dict(
        work="WRK-CARPENTER-1885",
        pd=True,
        locator=("Proof 14 of One Hundred Proofs that the Earth Is Not a Globe, Baltimore 1885, "
                 "as printed in the Project Gutenberg text #55387 (5th edition). Proofs 8–16 are "
                 "the pamphlet's navigation run; 14 is the one that states a measurable claim. "
                 "Not checked against a print copy."),
        quote=("“Parallels of latitude” only--of all imaginary lines on the surface of the "
               "Earth--are circles, which increase, progressively, from the northern centre to "
               "the southern circumference. The mariner's course in the direction of any one of "
               "these concentric circles is his longitude, the degrees of which INCREASE to such "
               "an extent beyond the equator (going southwards) that hundreds of vessels have "
               "been wrecked because of the false idea created by the untruthfulness of the "
               "charts and the globular theory together, causing the sailor to be continually "
               "getting out of his reckoning. With a map of the Earth in its true form all "
               "difficulty is done away with, and ships may be conducted anywhere with perfect "
               "safety. This, then, is a very important practical proof that the Earth is not a "
               "globe."),
        gloss="""<p><strong>Read what this proof is willing to be wrong about.</strong> The risk it takes is not the observation that navigators use pole-centred charts, which is true and settles nothing. It is the assertion that parallels of latitude <em>increase</em> southward past the equator, that the increase is large enough to wreck ships, and that a map drawn the other way would end the wrecks. That is a quantity, a consequence and a remedy &mdash; a testable claim, offered as such, in 1885. The refutation below answers that claim and not the four-word items.</p>
<p><strong>Where it comes from.</strong> Twenty years earlier Rowbotham had set out the same geometry at length in <em>Earth Not a Globe</em> (1865). Sailing due west, he writes, is steering at right angles to a north&ndash;south line fixed &ldquo;more accurately by the meridian lines which converge to the northern centre of the Earth&rdquo;, so that a mariner &ldquo;practically circumnavigates a plane surface &hellip; <em>because</em> the earth is a plane, having a central region, towards which the compass and the meridian lines which guide him, converge.&rdquo; Read him carefully: he is not confined to the modest point that a plane <em>could</em> be circumnavigated, though he makes that point too and builds a syllogism out of it; in the same sentence he states the plane as the cause. Carpenter then cut the material into numbered one-line proofs &mdash; 8 through 16 &mdash; which is the form the specimen list is written in, and proof 11 draws the conclusion that matters for item 128: &ldquo;there is no south &lsquo;point&rsquo; or &lsquo;pole&rsquo; but that, while the centre is North, a vast circumference must be South in its whole extent.&rdquo;</p>
<p><strong>And it is still in circulation, quotation marks and all.</strong> Dubay&rsquo;s <em>200 Proofs</em> (2015) carries the run at numbers 34&ndash;39 and 108&ndash;111: &ldquo;The North central Pole is the only proven fixed point on our flat Earth&rdquo;; &ldquo;every line of latitude south of the equator should measure a gradually larger and larger circumference the farther South travelled&rdquo;. Proof 38 reproduces the Reverend Thomas Milner shipwreck passage that Rowbotham had printed in 1865 with a footnote naming Milner&rsquo;s <em>Tour through Creation</em> &mdash; the same sentences, a century and a half later, about navigators to India who &ldquo;fancied themselves east of the Cape when still west&rdquo;. Very little in this cluster has moved since Palmerston was prime minister.</p>
<p><strong>What this passage is being cited as.</strong> The earliest text located that states this cluster&rsquo;s argument in numbered-proof form, with Rowbotham 1865 as the earlier prose statement of the same geometry and Dubay 2015 as the modern carrier. That is an ancestry claim and not a claim about who originated it: a search for an earlier numbered navigation proof was not run beyond these, and Rowbotham&rsquo;s own 1849 pamphlet is not digitised anywhere this review could reach.</p>"""),

    steelman=dict(
        description="""<p><strong>SURFACE (weak &mdash; do not use).</strong> &ldquo;Navigators know the Earth is round, so the argument is silly.&rdquo; This loses to a page of the navigator&rsquo;s own manual. Bowditch, ch. 24, defines plane sailing as solving for course, distance, difference of latitude and departure &ldquo;in which the Earth is regarded as a plane surface&rdquo;, and defines dead reckoning as projecting course and distance run from a known position &mdash; a plane construction with a straightedge. Anyone who opens by denying that navigation treats the sea as flat is contradicted by the standard reference in one sentence.</p>
<p><strong>DEEPER.</strong> The pole really is privileged, and not by convention alone. It is the one direction a magnetic needle finds unaided, the one point a chart can be built around without choosing an arbitrary origin, and the one place a star sits nearly still all night. Charts, compass roses, gyro repeaters and grid overlays are all organised around it. A defender who says this has said something true that no navigator would dispute.</p>
<p><strong>KERNEL.</strong> The strongest form is historical and it is uncomfortable, because for about forty years the data really did misbehave. Ships working the Southern Ocean in the 1830s and 1840s came out of their reckoning by tens of miles a day, reported it in their journals, and could not account for it: Wilkes recorded being &ldquo;consistently east of his reckoning, sometimes over 20 miles in less than 18 hours&rdquo;. No degree of longitude had then been measured on the ground south of the equator, and Rowbotham says so and asks for the measurement. So the honest 1865 position is: the southern hemisphere is charted from computation rather than from survey, the ships that sail it keep coming out wrong, and the people insisting the charts are right have not been there with a chain. <em>That is a legitimate demand for evidence, and it was made before the evidence existed.</em></p>""",
        why_it_doesnt_save_claim="""<p>Because the demand was met, and because the instruments the argument points at have the Earth&rsquo;s size and spin written into them.</p>
<p>Rowbotham named his own test: measure a degree of longitude in the far south. He predicted 69.44 statute miles at the parallel of Port Jackson against 45 statute miles at 50&deg;N, and wrote that the question &ldquo;has yet to be settled&rdquo;. It was settled. The measured figure at 45&deg; is 48.99 statute miles &mdash; 8.9% above his northern value, not 54% above it. His northern number was right to within one per cent, which shows he was reading the tables correctly; his southern number is the prediction, and the prediction failed.</p>
<p>And the equipment convicts him twice over. The mariner&rsquo;s compass he calls a proof of a central north dips into the ground at an angle that runs from 0&deg; at the magnetic equator to 90&deg; at the magnetic poles, which is why compass cards are balanced for magnetic zones. The gyrocompass that replaced it finds north by sensing the Earth&rsquo;s rotation, so its directive force &ldquo;is maximum at the equator and decreases to zero at the poles&rdquo; &mdash; and its natural period is about 84 minutes, which Bowditch stops to explain is &ldquo;the period of oscillation of a pendulum with an arm equal to the radius of the earth&rdquo;. The instrument that finds the pole for him has the planet&rsquo;s radius in its equation of motion.</p>"""),

    refutation="""<p><strong>Concede the description first, because it is accurate and it is in the standard reference.</strong> Charts really are built around a fixed pole. Dead reckoning really is a plane construction: Bowditch, <em>The American Practical Navigator</em>, art. 2400, defines it as &ldquo;the determination of one&rsquo;s present or future position by projecting the ship&rsquo;s course and distance run from a known position&rdquo;. Plane sailing really does treat the sea as flat &mdash; the same chapter says so in those words, solving for course, distance, difference of latitude and departure &ldquo;in which the Earth is regarded as a plane surface&rdquo;. Polar navigation really is a special case with its own apparatus. And celestial navigation really is done on a dome: art. 1524 has the navigator imagining the stars on the inside of a sphere. None of that is in dispute here, and an answer that starts by denying it deserves to lose.</p>

<p><strong>What the verdict ranges over.</strong> Not whether navigation uses pole-centred, locally flat methods. It does. The claim is that those methods <em>imply</em> a disc with a fixed northern centre &mdash; and that claim, in the form its own authors gave it, names a measurement and gets it wrong.</p>

<h4>1. The test Carpenter set, and it does not depend on which flat map you like</h4>

<p>Proof 14 grants the whole geometry the items assert: the pole is the centre, meridians run outward from it, and parallels of latitude are &ldquo;circles, which increase, progressively, from the northern centre to the southern circumference&rdquo;. Take that at face value. On any such figure the east&ndash;west length of a parallel is its radius times the longitude interval, and the radius grows as you go south, without exception, because south <em>is</em> outward. So on every north-centred disc &mdash; Gleason&rsquo;s, Rowbotham&rsquo;s, or one not yet drawn &mdash; a degree of longitude must be longer at 45&deg;S than at the equator, and longer still at 60&deg;S.</p>

<p>It is shorter. Computed here on the GRS80 ellipsoid, 2026-08-10: a degree of longitude is <strong>111.32 km at the equator, 78.85 km at 45&deg;S and 71.70 km at 50&deg;N</strong> &mdash; and the 45&deg;S figure is identical to the one at 45&deg;N, because an ellipsoid of revolution is symmetric about its equator. The southern value is 71% of the equatorial value where the disc requires it to be larger. That is the sphere&rsquo;s answer, cos&nbsp;&phi;, and it is fatal to the class of models rather than to one member of it. Nothing in the paragraph rests on the azimuthal-equidistant chart, so the reply &ldquo;that is not our map&rdquo; does not reach it.</p>

<h4>2. Rowbotham asked for the measurement in writing, and named the number</h4>

<p>He is more specific than Carpenter and more honest about the state of the evidence. In 1865 he sets the problem out as a challenge: a degree of longitude at 50&deg;N is 45 statute miles, and &ldquo;if the Earth is a plane, and the distances above referred to as given by nautical men are correct, a degree of longitude on the parallel of Port Jackson will be 69&middot;44 statute miles &hellip; This is the point which has yet to be settled.&rdquo; He wanted geodetic operations in the south, and he was entitled to want them.</p>

<p>The answer at that parallel is <strong>48.99 statute miles</strong>. His northern figure is right to within about one per cent; his southern prediction is 42% too high. Carpenter&rsquo;s harder version of the same claim &mdash; proof 16, that the circuit at 45&deg;S is &ldquo;found by navigators to be twice the distance&rdquo; of the circuit at 45&deg;N &mdash; asks for a ratio of 2. The measured ratio is 1.00.</p>

<h4>3. Where the Victorian numbers came from, and why they fit no map at all</h4>

<p>Rowbotham&rsquo;s southern circuit is assembled from sailing distances: Cape of Good Hope to Port Jackson 8,000 miles, Port Jackson to Cape Horn 8,000, Cape Horn to the Cape 6,000, total 22,000, which he compares with the parallel of 45&deg;. The three great-circle distances between those places are 5,946, 5,065 and 3,612 nautical miles &mdash; <strong>14,623 in total</strong>, comfortably inside the 15,282 nmi his own table gives for the 45&deg; parallel. (His page prints 14,282 for that circuit; 360 &times; 42&middot;45 is 15,282, and the slip inflates his claimed discrepancy by a thousand miles.)</p>

<p>The gap is not curvature. A sailing distance is what a ship covered, and square-riggers running the Southern Ocean did not follow parallels; they ran composite great-circle tracks far south of the rhumb line to hold the westerlies, and beat where they had to. Here is the check that settles it: <strong>22,000 nautical miles is 30% more than the flat azimuthal-equidistant map predicts for that same parallel</strong>, which is 16,975 nmi. The data Rowbotham rests his case on are too big for the globe <em>and</em> too big for the disc, which is the signature of a category error rather than of a discovery.</p>

<h4>4. The modern version of his experiment, which anybody can run this week</h4>

<p>Sydney to Perth is 35&deg; of longitude at about 33&deg;S, flown nonstop about eleven times a day, published at 3,294 km and scheduled at roughly 5 hours 15 minutes. On the north-polar azimuthal-equidistant chart those two airports are <strong>8,301 km</strong> apart in a straight line, so the flight would have to average about 1,580 km/h &mdash; supersonic at cruising altitude, in a subsonic airliner. Sydney to Santiago, Qantas QF27, is published at 11,333 km and scheduled at about 12&nbsp;h&nbsp;30; the same chart puts those cities 25,684 km apart, beyond the range of any airliner ever built. The identical calculation for London&ndash;New York gives a discrepancy of 7%, which is why northern routes never expose the problem and southern ones always do.</p>

<h4>5. Dead reckoning: what it is, and what it was doing wrong in 1840</h4>

<p>Dead reckoning is not a claim about the shape of the Earth. It is an estimate carried forward from the last fix by course and distance run, and it is wrong the moment anything moves the ship that the log cannot see &mdash; because a log measures speed through the water, not over the ground. The Southern Ocean is where that error is largest, and it took until the twentieth century to chart why: the Antarctic Circumpolar Current, whose transport through the Drake Passage was measured at 173.3 Sv by Donohue and colleagues in 2016, is the largest current on the planet. Wilkes&rsquo;s reported 20 miles of unaccounted easting in under 18 hours is a set of about 1.1 knots, which is the order of magnitude of that current.</p>

<p>Now look at the direction, because it is the discriminating detail and the lineage supplies it against itself. Wilkes runs <em>east</em> of his reckoning. Milner&rsquo;s Cape example, quoted by Rowbotham in 1865 and by Dubay in 2015, runs the other way: navigators &ldquo;fancied themselves east of the Cape when still west&rdquo;, that is, short of their reckoned easting. A southern hemisphere with parallels stretched by a uniform factor produces one signed error &mdash; every east&ndash;west passage takes longer than the chart says, everywhere, always. Errors that reverse sign between the Drake Passage and the Cape of Good Hope are what local currents look like, not what a rescaled globe looks like.</p>

<p>The two wrecks named in that quotation are worth following, since they have travelled unedited for a hundred and sixty years. The Royal Navy <em>Challenger</em> whose loss is documented in the period is HMS <em>Challenger</em> (1826), wrecked off Mocha Island, <strong>Chile</strong>, on 19 May 1835 &mdash; and the account notes that overcast skies had prevented sightings since 17 May, so her longitude was being carried on dead reckoning with no celestial fix, which is the ordinary explanation for running onto a coast. Dubay prints a longer form of the passage than the 1865 text carries, adding &ldquo;How came Her Majesty&rsquo;s Ship &lsquo;Conqueror&rsquo; to be lost?&rdquo; HMS <em>Conqueror</em>, 100 guns, was lost on Rum Cay in the <strong>Bahamas</strong> on 29 December 1861, at 23&deg;N.</p>

<h4>6. The compass, taken seriously</h4>

<p>The Victorian version of item 409 is Carpenter&rsquo;s proofs 10&ndash;13: a needle points north and south at once, which he says is impossible on a globe, so meridians must be straight lines to a central north. Dubay modernises it &mdash; on a ball &ldquo;the opposing &lsquo;South&rsquo; needle would actually be pointing up and off into outer-space&rdquo;.</p>

<p>It points into the <em>ground</em>, and by a measured amount. Bowditch art. 602: the angle of magnetic dip &ldquo;increases from 0&deg; at the magnetic equator to 90&deg; at the magnetic poles&rdquo;, with the horizontal component greatest at the magnetic equator and the vertical component greatest toward either pole. This is not a modern discovery invoked to save a theory; Robert Norman measured dip in London in 1581. Its practical consequence sits in every chandlery: compass cards are counterweighted for magnetic balancing zones, so a card balanced for northern service sits askew in southern latitudes. The same article records that the magnetic poles are &ldquo;near, but not coincidental with, the Earth&rsquo;s geographic poles&rdquo;, which is why every chart carries a variation figure and why the World Magnetic Model is reissued on a five-year cycle. A needle that pointed at a fixed central north would need neither.</p>

<h4>7. Polar navigation, and the dome</h4>

<p>Polar navigation is genuinely a special case, and the reason is the one the argument cannot afford. A gyrocompass seeks the meridian by sensing the Earth&rsquo;s rotation; Bowditch art. 620 states the consequence flatly &mdash; the directive force &ldquo;is maximum at the equator and decreases to zero at the poles&rdquo;, so &ldquo;vessels operating in high latitudes must construct error curves&rdquo;. That is a cos&nbsp;&phi; law, the horizontal component of a rotation vector tilting out of the local horizontal as you move over a sphere. On a stationary plane a gyrocompass would find nothing anywhere; on a spinning disc the rotation vector stands perpendicular to the surface at every point, so the horizontal component is zero everywhere and the instrument would never settle at any latitude. It settles everywhere except near the poles, exactly as the sphere requires.</p>

<p>Hence grid navigation, where meridians converge too fast to steer by &mdash; and here is the detail that decides item 408. Grid navigation is used at <strong>both</strong> ends. At the South Pole the local grid is defined so that &ldquo;Local Grid North aligns with the Greenwich meridian&rdquo;. Carpenter&rsquo;s proof 11 says there is no south point at all, only a circumference; a circumference has no convergence, and no grid would be needed to cope with one. The southern practice exists because the southern pole does.</p>

<p>As for the dome: the celestial sphere is defined in the navigator&rsquo;s own manual, art. 1524, as &ldquo;an imaginary sphere of infinite radius with the Earth at its center&rdquo;, and art. 1501 introduces it with the word <em>imagine</em>. It is a coordinate device, in the same way the Earth-fixed frame at <a href="#ARG-R08">ARG-R08</a> is a coordinate device. What is not imaginary is the geometry underneath it. The navigational triangle solved in every sight reduction is a <em>spherical</em> triangle, and art. 1529 notes that its terrestrial counterpart is one too: vertices at the elevated pole, the observer and the body&rsquo;s geographic position, with sides that are co-latitude, polar distance and zenith distance. The intercept a navigator plots is the difference between two arcs of a great circle on the Earth&rsquo;s surface, converted at sixty nautical miles to the degree &mdash; and the same chapter records that a degree of latitude runs &ldquo;from about 59.7 nautical miles at the equator to about 60.3 nautical miles at the poles&rdquo;, with the round 60 &ldquo;correct at about latitude 45&deg;&rdquo;. That variation is the Earth&rsquo;s oblateness, printed in the manual, in the unit the whole trade measures distance in. If the second reading of &ldquo;star dome&rdquo; is meant &mdash; the aircraft astrodome, the perspex blister through which a bubble sextant was shot on polar routes &mdash; the answer is the same one: what was done through it was spherical trigonometry with the pole as a vertex.</p>

<h4>8. What is left</h4>

<p>Every device in this cluster is pole-centred, and every one of them carries the globe inside it: the plane-sailing method that hands off to the spherical sailings after a few hundred miles and whose own mid-latitude formula is <em>p</em>&nbsp;=&nbsp;DLo&nbsp;cos&nbsp;<em>L</em>; the magnetic needle that dips to vertical over the poles; the gyrocompass that loses its north-seeking force as the cosine of the latitude and swings with the period of a pendulum as long as the Earth&rsquo;s radius; the imaginary star dome resolved by spherical triangles in units of one minute of arc. The argument found something real &mdash; navigation is organised around the pole &mdash; and read it as a claim about shape. Read as a claim about shape it makes a prediction, in Carpenter&rsquo;s own words, about how parallels behave south of the equator. They behave the other way.</p>""",

    advocate=dict(
        best_defense=(
            "Four moves. First, look at what you have actually done: you spent eight paragraphs "
            "quoting a US Navy manual back at us and every quote is on our side. 'The Earth is "
            "regarded as a plane surface.' 'Imagine that celestial bodies are located on the "
            "inner surface of a vast sphere.' We said navigation is done on a flat, pole-centred "
            "model with an imaginary dome overhead, and your own source says so in those words. "
            "Second, your headline argument refutes the azimuthal-equidistant map. Nobody signed "
            "for that map. It is a projection borrowed from the UN emblem and used as a sketch; "
            "the southern distances are the open problem in flat-earth cartography and we say so "
            "openly. You have refuted Gleason 1892 and called it a refutation of us. Third, your "
            "current is a rescue. When the data went against the charts you produced an ocean "
            "current, discovered later, sized after the fact to absorb exactly the discrepancy "
            "reported. If we did that you would call it curve-fitting, and you would be right. "
            "Fourth, and most telling: your entire southern case rests on distances published by "
            "the same institutions whose figures are in question, and on flight times you have "
            "not measured. You have not been to 45 degrees south with a chain either. Rowbotham "
            "asked for a survey. You have given him a table."),
        survives=4,
        preemptive=(
            "Four, and the number is driven by the second move. The answer to it is already the "
            "spine of section 1 and must not be allowed to migrate: the parallel argument is "
            "SCALE-FREE and Carpenter supplies its premise himself. Pole at the centre, south "
            "radially outward, parallels as concentric circles - that is proof 14's own wording - "
            "and it forces east-west distance per degree of longitude to increase monotonically "
            "southward on EVERY such map, drawn or undrawn. The measured sequence 111.32 / 78.85 "
            "km closes the class, not one member of it. If an editor ever trims that paragraph to "
            "the punchy azimuthal-equidistant numbers in section 4, the strongest passage on the "
            "page becomes the most answerable one, because those numbers do depend on the map. "
            "Keep section 4 labelled as illustration. On the first move, agree in public and "
            "loudly: the compression block already records that the source is the careful party "
            "here, and the Bowditch concessions are quoted in our own voice in the first "
            "paragraph rather than conceded under pressure - but keep the scope sentences "
            "ADJACENT to them ('to calculate the longitude, the spherical sailings are "
            "necessary'; 'not intended for distances of more than a few hundred miles'), because "
            "the concession without its scope is the defender's best quotation. On the third "
            "move the defender has a point about method and the text must not overreach: the "
            "Antarctic Circumpolar Current is offered as the order of magnitude for one reported "
            "error and no mechanism is assigned to the Cape case at all. The load there is "
            "carried by the SIGN of the errors reversing between two places, which no uniform "
            "rescaling of southern parallels can produce, and by the fact that the Victorian "
            "sailing distances overshoot the flat map by 30% as well. Do not upgrade that "
            "paragraph into a claim that the current explains every historical discrepancy. On "
            "the fourth, the flight figures are published schedules and are labelled as such; "
            "the reproducible core is the geodetic arithmetic, which is stated with its "
            "ellipsoid and its formula so a reader can rerun it."),
    ),

    straw_man=dict(
        identified=True,
        detail=("Two, and both are about what the globe model is supposed to require. Carpenter's "
                "proof 8 argues that if the Earth were a globe then a small model globe would be "
                "“the very best--because the truest--thing for the navigator to take to sea "
                "with him”, and that with such a toy “the mariner would wreck his ship, "
                "of a certainty!” Nothing in spherical navigation calls for a globe at the "
                "chart table; the sphere enters as trigonometry and as the projection the chart "
                "is drawn on, which is why Mercator's chart exists. Dubay's proof 34 does the "
                "same to method: it states that “Both Plane Sailing and Great Circle "
                "Sailing, the most popular navigation methods, use plane, not spherical "
                "trigonometry”. Great-circle sailing is the spherical-trigonometry case by "
                "definition, and Bowditch's chapter on the sailings classes it among the "
                "spherical sailings and defines a great circle as the intersection of a sphere "
                "with a plane through its centre. The claim attributes to working navigators a "
                "method they are not using, and the correction is available in the same "
                "reference the argument otherwise relies on.")),

    compression=dict(
        assessed=True, drifted=True,
        list_phrasing=("Navigation charts fixed pole. / Polar navigation star dome. / "
                       "Dead reckoning dome compass."),
        source_wording=("“‘Parallels of latitude’ only … are circles, which increase, "
                        "progressively, from the northern centre to the southern circumference. "
                        "… the degrees of which INCREASE to such an extent beyond the equator "
                        "(going southwards) that hundreds of vessels have been wrecked … causing "
                        "the sailor to be continually getting out of his reckoning.”"),
        drift_type="unsourced_addition",
        note=("<strong>The recorded drift is the word &ldquo;dome&rdquo;, which two of the three "
              "items carry and the navigation argument's own texts do not.</strong> Searches run "
              "2026-08-10: the Project Gutenberg text of Carpenter's <em>One Hundred Proofs</em> "
              "(#55387) returns no hit for it; the Project Gutenberg text of the 1865 <em>Earth "
              "Not a Globe</em> (#69892) returns one, &ldquo;the dome of the Pantheon&rdquo;, in "
              "the section on Foucault's pendulum; the archive.org OCR of Dubay's <em>200 "
              "Proofs</em> that was searched returns none. All three argue for a <em>plane</em> "
              "with a northern centre and a southern circumference, and Carpenter's proof 11 "
              "denies a southern pole outright &mdash; &ldquo;while the centre is North, a vast "
              "circumference must be South in its whole extent.&rdquo; The enclosing dome is "
              "later furniture, from the 2015 enclosed-world material, fitted to a Victorian "
              "navigation proof that neither needs nor mentions it.<br><br>"
              "<strong>The larger change runs the other way from this project's usual finding, "
              "and the enum has no value for it.</strong> Almost every argument audited here is "
              "firmer in the list than in the book. This one is weaker. Carpenter's proof 14 "
              "commits to a quantity &mdash; parallels of latitude increase going south, enough "
              "to wreck ships &mdash; and proof 16 puts a number on it, the circuit at 45&deg;S "
              "being &ldquo;twice the distance&rdquo; of the circuit at 45&deg;N. Rowbotham in "
              "1865 goes further and names the experiment that would settle it, predicting 69.44 "
              "statute miles to the degree of longitude at the parallel of Port Jackson and "
              "writing that the point &ldquo;has yet to be settled&rdquo;. What survives into the "
              "list is &ldquo;Navigation charts fixed pole&rdquo; &mdash; true of the globe as "
              "well, and committed to nothing. <em>The compression dropped the falsifiable "
              "half.</em> That is a drift toward unfalsifiability rather than toward overstatement, "
              "and it is worth naming because the usual diagnosis does not fit: on this argument "
              "the source is the party that took a risk, and the list is the party that stopped "
              "taking it. <code>unsourced_addition</code> is recorded because it is the plainest "
              "and most checkable of the two changes, following the precedent set at "
              "<a href=\"#ARG-E08\">ARG-E08</a>, and both texts are above so a reader can judge.<br><br>"
              "<strong>The refutation answers the source, not the fragment.</strong> It grants "
              "the description at full strength in its first paragraph, in the navigator's own "
              "manual's words, and then answers Carpenter's stated prediction about southern "
              "parallels and Rowbotham's stated number &mdash; not the four-word items, which "
              "assert too little to be wrong.")),

    verdict_challenge=dict(challenged=False, proposed_verdict=None, reasoning=None),

    people=["PER-ROWBOTHAM", "PER-CARPENTER", "PER-DUBAY"],
    related=["B05", "B06", "B08", "B11", "B13", "R08", "A07"],

    sources=[
        dict(label="Carpenter, One Hundred Proofs that the Earth Is Not a Globe (Baltimore, 1885) "
                   "— proofs 8–16 are the navigation run; proof 14 (parallels increase southward, "
                   "sailors “out of reckoning”), proof 11 (no south pole), proof 16 (45°S circuit "
                   "“twice the distance”)",
             url="https://www.gutenberg.org/ebooks/55387"),
        dict(label="Rowbotham, Zetetic Astronomy: Earth Not a Globe (1865 book edition) — meridians "
                   "“converge to the northern centre”, circumnavigation of a plane, the southern "
                   "degree-of-longitude challenge (“69·44 statute miles … has yet to be settled”) "
                   "and the Milner shipwreck quotation with its footnote",
             url="https://www.gutenberg.org/ebooks/69892"),
        dict(label="Dubay, 200 Proofs Earth Is Not a Spinning Ball (2015) — proofs 34–39 and "
                   "108–111 carry this cluster forward, including the Milner passage reproduced "
                   "from Rowbotham",
             url="https://archive.org/details/200ProofsEarthIsNotASpinningBall_201903"),
        dict(label="Bowditch, The American Practical Navigator (NGA Pub. 9, 2002 ed.), ch. 24 "
                   "“The Sailings” — art. 2400 on dead reckoning; plane sailing “in which the "
                   "Earth is regarded as a plane surface”, “not intended for distances of more "
                   "than a few hundred miles”, “to calculate the longitude, the spherical "
                   "sailings are necessary”; the mid-latitude formula p = DLo cos Lm",
             url="https://en.wikisource.org/wiki/The_American_Practical_Navigator/Chapter_24"),
        dict(label="Bowditch ch. 15 “Navigational Astronomy” — art. 1524, the celestial sphere as "
                   "“an imaginary sphere of infinite radius with the Earth at its center”; art. "
                   "1529, the navigational triangle as a spherical triangle with a terrestrial "
                   "counterpart; the degree of latitude running 59.7 to 60.3 nautical miles from "
                   "equator to pole",
             url="https://en.wikisource.org/wiki/The_American_Practical_Navigator/Chapter_15"),
        dict(label="Bowditch ch. 6 “Compasses” — art. 602, magnetic dip “increases from 0° at the "
                   "magnetic equator to 90° at the magnetic poles” and the magnetic poles are "
                   "“near, but not coincidental with” the geographic ones; art. 618, the "
                   "gyrocompass ellipse of “about 84 minutes … a pendulum with an arm equal to "
                   "the radius of the earth”; art. 620, directive force “maximum at the equator "
                   "and decreases to zero at the poles”",
             url="https://en.wikisource.org/wiki/The_American_Practical_Navigator/Chapter_6"),
        dict(label="South Pole Antarctic Specially Managed Area — “Local Grid North aligns with "
                   "the Greenwich meridian (0º)”, i.e. grid navigation is used at the southern "
                   "pole as well as the northern",
             url="https://www.southpole.aq/maps/"),
        dict(label="Donohue et al., “Mean Antarctic Circumpolar Current transport measured in "
                   "Drake Passage”, Geophys. Res. Lett. 43:11760 (2016) — 173.3 Sv, the scale of "
                   "the current that dead reckoning in the Southern Ocean cannot see",
             url="https://doi.org/10.1002/2016GL070319"),
        dict(label="HMS Challenger (1826) — the Royal Navy ship of that name whose loss is "
                   "documented in the period: wrecked off Mocha Island, Chile, 19 May 1835, "
                   "having had no sightings since 17 May",
             url="https://en.wikipedia.org/wiki/HMS_Challenger_(1826)"),
        dict(label="Royal Museums Greenwich — “The loss of HMS ‘Conqueror’, 100 guns, on Rum Cay, "
                   "Bahamas, 29 December 1861”, the second wreck named in the passage Dubay "
                   "reprints",
             url="https://collections.rmg.co.uk/collections/objects/113560.html"),
        dict(label="Sydney–Perth nonstop: 3,294 km, about 5 h 15 m, roughly eleven services a day "
                   "— the published schedule against which the flat-map figure of 8,301 km is "
                   "compared",
             url="https://www.flightsfrom.com/SYD-PER"),
        dict(label="Qantas QF27 Sydney–Santiago nonstop, Boeing 787-9, published 11,333 km and "
                   "about 12 h 30 m",
             url="https://info.flightmapper.net/route/Qantas_QF_SYD_SCL"),
        dict(label="Astrodome (aeronautics) — the transparent blister through which a bubble "
                   "sextant was used on long-range and polar air routes, the likeliest referent "
                   "of the item’s “star dome” if the celestial sphere is not meant",
             url="https://en.wikipedia.org/wiki/Astrodome_(aeronautics)"),
        dict(label="The Final Experiment, Union Glacier, Antarctica, 14–17 December 2024 — the "
                   "24-hour midnight sun observed at about 79°S; Jeran Campanella conceded",
             url="https://en.wikipedia.org/wiki/The_Final_Experiment_(expedition)"),
    ]),
}
