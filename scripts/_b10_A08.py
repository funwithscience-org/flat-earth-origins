# -*- coding: utf-8 -*-
"""Batch 10 — A08. "Aircraft don't compensate for spin; east/west flight times symmetric."

Four items: 13 "Aircraft navigation not compensating for spin.", 45 "Plane flight
times consistent with rest Earth.", 110 "Flight symmetry east/west.", 236 "Flight
times symmetric." Verdict REFUTED, kept.

Research notes for whoever picks this up next.

1. THE ORIGINATOR IN OUR RECORD CANNOT BE RIGHT, AND THE REAL ONE IS FINDABLE.
   clusters.py credits this cluster to Samuel Rowbotham, *Earth Not a Globe*, 1865.
   Rowbotham died 23 December 1884; powered flight is 17 December 1903. No edition
   published in his lifetime can contain an argument about aeroplanes. What the 1865
   text does contain (Project Gutenberg #69892, the Simpkin, Marshall printing,
   Section II "The Earth no Axial or Orbital Motion") is the AIR-GUN passage — a ball
   fired vertically that should land "5,600 feet, or considerably more than one statute
   mile to the west of the air-gun" and does not. That is the seed, and ARG-A10 already
   owns it. Searching that 1865 text for balloon, aeronaut, fly, flight, east and west
   returns the concavity-from-a-balloon quotations (Wise, Mayhew, Elliott, Glaisher),
   the Bishop Wilkins balloon joke inside a REPRINTED newspaper article about Foucault,
   and — the only east/west travel-time material in it — the date-line passage, where
   Rowbotham considers the day gained or lost on an east or west circumnavigation and
   concludes it is "no more favourable to the idea of rotundity than it is to the
   opposite fact that the earth is a plane; as both forms will permit of the same
   effect." I.e. on the nearest topic he has, he calls east/west travel asymmetry
   NON-DISCRIMINATING. That is the opposite of what this cluster asserts in his name.

2. THE VICTORIAN ANCESTOR IS CARPENTER, NOT ROWBOTHAM, AND HE IS EXPLICIT.
   *One Hundred Proofs* (1885, Gutenberg #55387) carries the argument form twice, in
   its own index: proof 42/44 "Projectiles — firing east or west" and proof 54
   "Balloons not left behind". Proof 44 verbatim: "since the Earth is said to move at
   the rate of nineteen miles in a second of time, 'from west to east,' it would make
   all the difference imaginable if the gun were fired in an opposite direction. But,
   as, in practice, there is not the slightest difference, whichever way the thing may
   be done…". Proof 54 verbatim: "The aeronaut is able to start in his balloon and
   remain for hours in the air … and come down again in the same county or parish from
   which he ascended." East/west symmetry as a proof is Carpenter's move; the vehicle
   is a cannon and a balloon because those were the vehicles.

3. THE AEROPLANE VERSION: GABRIELLE HENRIET. Dubay's *200 Proofs* proof 26 is a block
   quotation from "Heaven and Earth" by Gabrielle Henriet, and it is the earliest text
   located that argues from AIRCRAFT speeds. Henriet, ch. II "On the fact that the
   earth does not rotate", pp. 11–12: an aircraft's distance covered "would be reduced
   or increased by the speed of the rotation"; at 1,000 km/h rotation and 500 km/h
   airspeed the eastbound destination "will be farther removed every minute"; westbound
   covers 1,500 km/h; an aircraft matching the rotation eastbound "could not cover any
   ground at all"; and an airfield is "slipping away at the rate of 1,000 kilometers an
   hour". He closes: "It might certainly be useful to know what people who fly think of
   the rotation of the earth." Dating: Kook Science gives 1956, Holborn Publishing Co.,
   London; LibraryThing gives 1958; the archive.org scan's title page carries only
   "Translated from the French", the price 16/-, and the printer (Mitchell & Co.,
   Arundel, Sussex). Regency Press 1963 is a DIFFERENT Henriet title, *The Solid Vault
   of Heaven* — do not merge them. Say "mid-1950s" and footnote the disagreement.

4. THE UNIT SUBSTITUTION — the sharpest single finding in this entry, and it is inside
   quotation marks. Henriet says KILOMETERS three times. Dubay's proof 26 prints MILES
   three times. Verified in two independent copies of each: Henriet at archive.org
   (item HeavenAndEarthGabrielleHenriet, OCR) and at theflatearthsociety.org's PDF
   (text layer) both read "1,000 kilometers"; Dubay at archive.org both in the djvu OCR
   and in the PDF text layer reads "1,000 miles". Dubay also drops one sentence from
   the middle without an ellipsis and silently changes "Thus, if the earth rotates" to
   "If the earth rotates". Why it matters and why nobody noticed: 1,000 km/h is the
   Earth's surface speed at about 51.5°N — Britain — to within 4% (computed: 1,041
   km/h), and 1,000 mph is the equatorial figure to within 4% (1,040 mph). Both numbers
   "work", at different latitudes, so the substitution rescales the physical claim by
   1.61 while leaving the rhetoric intact and the arithmetic self-consistent.

5. THE SIGN IS THE REFUTATION, AND IT IS BETTER THAN THE MAGNITUDE. Henriet predicts
   eastbound flights disadvantaged and westbound favoured; Dubay's proof 25 predicts
   westward "arrived at thrice the speed". Observed on the mid-latitude routes this
   argument is made about: eastbound is the FAST direction. BA112, a 747-400, JFK to
   Heathrow on 9 February 2020, 4 h 56 min for 5,554 km — average ground speed 1,126
   km/h, peak 1,327 km/h, against a cruise airspeed of about 933 km/h (Guinness World
   Records; Flightradar24 blog). The same day, westbound traffic routed north of
   Greenland to dodge the headwind and ran over an hour late. So do not argue only that
   the asymmetry is smaller than claimed. Argue that it has the wrong sign.

6. AND THE ASYMMETRY REVERSES WITH LATITUDE, WHICH NO SLIPPAGE MODEL CAN DO. Trades
   easterly below ~30°, westerlies above: both are Coriolis products of the Hadley/
   Ferrel circulation (LibreTexts 16.7; Wikipedia "Trade winds": surface air flowing
   equatorward "is deflected toward the west in both hemispheres by the Coriolis
   effect"). Urdaneta's 1565 *tornaviaje* is the historical anchor — sail west in the
   trades, come home east in the westerlies, three centuries before Rowbotham. A
   ground-slip term has one sign everywhere; the observed asymmetry flips at a latitude
   the rotating model predicts.

7. THE COMPENSATION IS REAL AND HAS A PROCEDURE. Item 13 is answered by the alignment
   page of an airliner IRS manual, not by argument. Earth rate = 15.041°/hr (computed
   from Ω = 7.2921150e-5 rad/s; sidereal day 23 h 56 m 4 s). At 51.5°N the horizontal
   component is 9.36°/hr and the vertical 11.77°/hr. Honeywell's GG1320AN — the
   industry-standard navigation-grade ring laser gyro — has typical bias stability
   0.0035°/hr, so Earth rate is roughly 4,300 times the instrument's noise floor. The
   IRS text used here (an operator's IRS description mirrored at
   digilander.libero.it/andreatheone/irs.htm — an unofficial copy, and the entry says
   so) states: "The alignment computations use the basic premise that the only
   accelerations during alignment are due to the earth's gravity; the only motion
   during alignment is due to the earth's rotation"; "the laser gyro sensed earth rate
   components are used to establish the heading of the airplane"; "Earth rate sensing
   by the laser gyros allows the IRU to determine initial latitude"; that gyro latitude
   "is compared to the crew entered latitude" and the comparison "must be favorable to
   complete the alignment period"; minimum align time 10 minutes. Corroboration for the
   general statement, from a professional publication rather than a mirror: Inside GNSS,
   "The Inertialist: Fundamentals of Inertial Navigation" — Earth rate, transport rate
   and Coriolis acceleration are the non-inertial effects navigation-grade systems
   compensate, alignment uses the gravity and Earth-rate vectors, and "For lower-grade
   IMUs, Earth rate (15 deg/hr) stays below gyro errors and cannot be measured reliably."

8. TWO MORE MEASURED RESIDUES, BOTH REPRODUCED HERE 2026-08-10.
   (a) Coriolis/Eötvös at cruise. At 45° and 250 m/s: horizontal Coriolis 2Ωv sin φ =
       0.0258 m/s² (a dropped term integrates to order ½at² ≈ 170 km in an hour — quote
       it as an order of magnitude, since real INS error dynamics are Schuler-bounded);
       vertical Eötvös 2Ωv cos φ = 0.0258 m/s² = 2,578 mGal = 0.26% of g, so the
       east-minus-west swing is about 5,150 mGal. This is not theoretical: Eötvös found
       it in shipboard gravimetry and it was confirmed by the two-ship Black Sea trial
       of 1908; Harlan, "Eötvös corrections for airborne gravimetry", JGR 73:4675
       (1968), is the aviation version.
   (b) Hafele–Keating. Cesium clocks on scheduled commercial flights, October 1971,
       once east and once west: observed −59 ± 10 ns eastward, +273 ± 7 ns westward
       (predicted −40 ± 23 and +275 ± 21). The abstract's own phrase is "directionally
       dependent time differences". A 332 ns east-west split on ordinary airline
       flights, which on a non-rotating Earth would be zero. NPL repeated it in 1996
       (39 ± 2 ns against 39.8 predicted) and in 2010 (230 ± 20 against 246 ± 3).

9. DO NOT USE THE SURFACE ANSWER. "The atmosphere rotates with the Earth and carries
   the plane" loses, and it deserves to: the air visibly does not move with the ground
   (that is what wind is), and Dubay's proof 23 pre-emptively caricatures that reply
   ("gravity magically and inexplicably drags the entire lower-atmosphere … in perfect
   synchronization"). The answer is the frame, not the fluid — and then the residues in
   note 8, which is where the argument actually dies. ARG-A10 owns the atmosphere
   question and states Rowbotham's own position (he GRANTS co-rotation); do not
   re-litigate it here, cross-link it.

10. DEFECTS IN OUR OWN RECORD, reported up, NOT edited here (this agent owns one file):
    clusters.py A08 gives originator Rowbotham / *Earth Not a Globe* / 1865 for an
    argument about aeroplanes; its note leads with the weak atmospheric answer; and
    works.py/people.py have no Henriet records, which is why the passage below cites
    WRK-DUBAY-2015 (which does exist) and puts Henriet in the gloss. Note the knock-on:
    moving four items off Rowbotham takes his total from 65 to 61 and adds a twentieth
    named originator, both of which are asserted in tests/test_provenance.py. Priority
    is NOT established — Henriet is the earliest text LOCATED, not demonstrably the
    first — so if it will not verify, the honest move is untraced, not a different guess.
"""

ENTRY = {

"A08": dict(

    tldr=("Airliners do compensate for the Earth's spin — not in the cockpit, but in the "
          "avionics bay. An inertial reference unit spends its pre-flight alignment — ten "
          "minutes, minimum — measuring the Earth's rotation, and derives the aircraft's "
          "latitude from it to check the crew's entry. East–west flight times are not symmetric "
          "either: on 9 February 2020 a 747 crossed New York to London eastbound in 4 h 56 min, "
          "at a ground speed of 1,327 km/h against an airspeed of 933. The asymmetry is real, "
          "and it runs the opposite way from the prediction in the oldest source located for "
          "the aeroplane version of this argument."),

    passage=dict(
        work="WRK-DUBAY-2015",
        pd=False,
        locator=("200 Proofs Earth Is Not a Spinning Ball, numbered proofs 25–27, quoted from the "
                 "Internet Archive copy of the print edition (item "
                 "200-proofs-the-earth-is-not-a-spinning-ball; PDF text layer, sixth and seventh "
                 "pages of the list). That edition carries no printed page numbers in its text "
                 "layer, so the proof numbers are the locator. Proof 26 is a block quotation from "
                 "Gabrielle Henriet, Heaven and Earth — see the gloss"),
        quote=("If Earth and its atmosphere were constantly spinning eastwards over 1000mph, then "
               "the average commercial airliner traveling 500mph should never be able to reach its "
               "Eastward destinations before they come speeding up from behind! Likewise Westward "
               "destinations should be arrived at thrice the speed, but this is not the case."),
        gloss="""<p><strong>Read the last clause before anything else.</strong> Dubay&rsquo;s empirical claim is narrow and, as far as it goes, true: westward flights are not arrived at three times the speed of eastward ones. Across proofs 25 to 27 that is the whole of the observation offered. The list&rsquo;s items 110 and 236 &mdash; <em>&ldquo;Flight symmetry east/west&rdquo;</em>, <em>&ldquo;Flight times symmetric&rdquo;</em> &mdash; assert something else, and something checkable: that the two directions take the same time. They do not, and the compression block below carries that as a finding.</p>
<p><strong>Where the aeroplane version comes from.</strong> The next proof in the same run, number 26, is a block quotation from <em>Heaven and Earth</em> by Gabrielle Henriet, and that book is the earliest text located that argues from aircraft speeds at all. Henriet&rsquo;s chapter II, &ldquo;On the fact that the earth does not rotate&rdquo;, at pp. 11&ndash;12: <em>&ldquo;Thus, if the earth rotates, as it is said, at 1,000 kilometers an hour, and a plane flies in the same direction at only 500 kilometers, it is obvious that its place of destination will be farther removed every minute.&rdquo;</em> An aircraft matching the rotation eastward would <em>&ldquo;remain suspended in mid-air over the spot from which it took off&rdquo;</em>; landing is difficult to picture on an airfield <em>&ldquo;slipping away at the rate of 1,000 kilometers an hour&rdquo;</em>. The chapter ends with a challenge that this page takes seriously enough to answer literally: it would be useful, Henriet writes, to know what people who fly think of the rotation of the earth. Dating is unsettled &mdash; one reference work gives 1956 (Holborn Publishing Co., London), another 1958; the scan used here has no date on its title page, only &ldquo;Translated from the French&rdquo;, the price, and the printer&rsquo;s imprint at Arundel, Sussex. Mid-1950s is as tight as this pass could make it.</p>
<p><strong>A word that changed on the way through.</strong> Henriet writes <em>kilometers</em> &mdash; three times, in both copies checked. Dubay&rsquo;s proof 26 prints <em>miles</em>, three times, inside the quotation marks. The substitution is not visible to a reader, and it is not obviously careless either, because both versions happen to be roughly right: 1,000 km/h is the Earth&rsquo;s surface speed at about 51.5&deg;N, the latitude of London, to within four per cent; 1,000 mph is the equatorial figure to within four per cent. The claim is rescaled by a factor of 1.61 and its arithmetic still closes. Proof 26 also drops a sentence from the middle of the passage without an ellipsis.</p>
<p><strong>The Victorian ancestry, which is Carpenter&rsquo;s and not the vehicle you would expect.</strong> East/west symmetry as a numbered proof is in <em>One Hundred Proofs</em> (1885) twice over. Proof 44: <em>&ldquo;since the Earth is said to move at the rate of nineteen miles in a second of time, &lsquo;from west to east,&rsquo; it would make all the difference imaginable if the gun were fired in an opposite direction. But, as, in practice, there is not the slightest difference, whichever way the thing may be done…&rdquo;</em> Proof 54: <em>&ldquo;The aeronaut is able to start in his balloon and remain for hours in the air, at an elevation of several miles, and come down again in the same county or parish from which he ascended.&rdquo;</em> Behind Carpenter stands the air-gun of <em>Earth Not a Globe</em>, Section II &mdash; the ball that should fall <em>&ldquo;considerably more than one statute mile to the west&rdquo;</em> and lands at the muzzle. That argument is <a href="#ARG-A10">ARG-A10</a>&rsquo;s, and it is genuinely Rowbotham&rsquo;s; the aeroplane is a later vehicle bolted onto it, and the man who built the chassis died nineteen years before the Wright brothers flew.</p>
<p><strong>One thing the 1865 text does say about travelling east and west.</strong> Considering the day gained or lost on a circumnavigation, Rowbotham concludes that it is <em>&ldquo;no more favourable to the idea of rotundity than it is to the opposite fact that the earth is a plane; as both forms will permit of the same effect.&rdquo;</em> On the nearest question he addresses, the founder of the zetetic lane calls east/west travel asymmetry non-discriminating &mdash; which is the opposite of the use four items on this list make of it. (Searched: the Project Gutenberg #69892 text of the 1865 Simpkin, Marshall printing, for <em>balloon</em>, <em>aeronaut</em>, <em>fly</em>, <em>flight</em>, <em>east</em> and <em>west</em>. An aeroplane argument is not located in that text; later editions were not reached in this pass.)</p>"""),

    steelman=dict(
        description="""<p><strong>SURFACE (weak &mdash; do not use).</strong> &ldquo;The atmosphere rotates with the Earth, so it carries the aircraft along.&rdquo; This loses, and it loses to a five-year-old&rsquo;s objection: the air demonstrably does <em>not</em> move with the ground, which is what wind is, and an aircraft carried by an air mass is carried at the air mass&rsquo;s speed, not the ground&rsquo;s. Dubay has the caricature pre-loaded at proof 23 &mdash; gravity &ldquo;magically and inexplicably&rdquo; dragging the lower atmosphere &ldquo;in perfect synchronization&rdquo; up to some undetermined height &mdash; and anyone who opens with the fluid instead of the frame walks into it.</p>
<p><strong>DEEPER.</strong> Galilean invariance: the aircraft, the runway and the air all share the Earth&rsquo;s rotational velocity before the wheels leave the ground, and nothing in the flight removes it, so ground speed is a relation between aircraft and ground and the shared term cancels. True, and answered in 1632 in the Second Day of Galileo&rsquo;s <em>Dialogo</em>. Incomplete, because it invites the obvious reply: if the shared motion cancels out of everything, you have not shown that it exists &mdash; which is <a href="#ARG-R03">ARG-R03</a>&rsquo;s move, and a good one.</p>
<p><strong>KERNEL.</strong> Henriet has asked for the right thing. His argument is not really about aerodynamics; it is a demand for an observable that would distinguish the frames &mdash; the discrepancy between an aircraft&rsquo;s motion through the air and its motion over the ground &mdash; and he is right that on a rotating Earth with a stationary atmosphere that discrepancy would be enormous and permanent and easterly. He is also right that flight is the place to look, because an aircraft is the one everyday vehicle that is mechanically decoupled from the surface for hours at a time. And his closing line is a fair challenge rather than a taunt: ask the people who fly. His number is not sloppy either &mdash; 1,000 km/h is the surface speed at British latitudes to four per cent. The strongest form of this cluster is therefore: <em>an aeroplane is the natural apparatus for detecting the Earth&rsquo;s rotation, aviation has run that apparatus continuously for a century, and if the rotation were real the industry would have had to build something to cope with it.</em></p>""",
        why_it_doesnt_save_claim="""<p>Because the industry did, and the answer to Henriet&rsquo;s challenge is a printed procedure rather than an argument.</p>
<p>The discrepancy he asks about is computed on every flight. An inertial reference unit outputs, among other things, <em>wind speed and direction</em>, and it gets them by differencing two independent sensor chains: inertial ground velocity against true airspeed from the air data computers. That readout is Henriet&rsquo;s quantity. If the ground were sliding eastward under a still atmosphere at 1,000 km/h, every airliner in the world would display a permanent 1,000 km/h easterly. They display tens to a few hundred kilometres per hour, in a direction that changes with the weather.</p>
<p>And the residual rotation terms he is implicitly betting against are not zero. They are in the navigation equations by name &mdash; Earth rate, transport rate, Coriolis &mdash; they are the reason a navigation-grade gyro is required at all, and one of them is measured before pushback: the alignment derives the aircraft&rsquo;s latitude from the sensed rotation and refuses to complete if it disagrees with what the crew typed in. The kernel is exact and it points the other way: aviation is the best-instrumented place to look for the Earth&rsquo;s rotation, which is why aviation found it.</p>"""),

    refutation="""<p><strong>Start with what is conceded, because two things in this cluster are true.</strong> A pilot makes no correction for the Earth&rsquo;s rotation in the sense the argument means &mdash; there is no rotation knob, no westward drift allowance in the flight plan, nothing in the cockpit that answers to &ldquo;spin&rdquo;. And westward flights are not three times faster than eastward ones, which is the only empirical claim the source text actually makes. Both are granted at full strength. The cluster fails anyway, on the two things it adds to them: that flight times are <em>symmetric</em>, and that nothing in aviation compensates for the rotation.</p>

<h4>1. The prediction has the wrong sign</h4>

<p>Take the source at its own strength. Henriet&rsquo;s aircraft flies east into a receding destination and west with 1,000 km/h added; Dubay&rsquo;s version has westward destinations reached at thrice the speed. Both make eastbound the disadvantaged direction. On the mid-latitude routes this argument is always made about, eastbound is the <em>fast</em> direction, and has been since the routes existed.</p>

<p>The clean instance: British Airways flight BA112, a Boeing 747-400, New York JFK to London Heathrow on 9 February 2020, <strong>4 hours 56 minutes</strong> for 5,554 km &mdash; an average ground speed of 1,126 km/h and a peak of 1,327 km/h, against a cruise airspeed of about 933 km/h. The aircraft covered ground faster than it moved through the air, going <em>east</em>, in the direction Henriet says an aircraft cannot make progress at all. On the same day westbound traffic detoured north of Greenland to escape the headwind and lost more than an hour. The routine version of the same fact, without the storm: eastbound long-haul flights run shorter than their westbound returns by an hour or more.</p>

<p>So the answer to items 110 and 236 is not that the asymmetry is smaller than claimed. It is that the asymmetry is <strong>real, published in every timetable, and pointed the other way</strong>.</p>

<h4>2. The asymmetry reverses with latitude, which is the discriminating part</h4>

<p>A ground-slip term has one sign everywhere: whatever the Earth is doing, it is doing it in the same direction at every latitude. The observed asymmetry does not behave like that. Below about 30&deg; the prevailing surface winds are the easterly trades; above it they are the westerlies, and the mid-latitude jet stream sits in that belt. Both are products of the same rotation: air moving equatorward in the Hadley circulation is &ldquo;deflected toward the west in both hemispheres by the Coriolis effect&rdquo;, and air moving poleward is deflected the other way, which is why the mid-latitude belt blows from the southwest.</p>

<p>Sailors were exploiting the reversal four centuries ago. Urdaneta&rsquo;s <em>tornaviaje</em> of 1565 established the Pacific round trip that the Manila galleons then ran for 250 years: west in the tropical trades, home eastward at high latitude in the westerlies. The east/west travel asymmetry this cluster denies is not merely real, it is old enough to have organised the world&rsquo;s shipping three centuries before Rowbotham, and its <em>latitude structure</em> is a rotation signature that no slippage between ground and air can imitate.</p>

<h4>3. The compensation exists, and it has a procedure and a duration</h4>

<p>Item 13 is the interesting one, because it is answerable from a manual. An airliner&rsquo;s inertial reference system aligns on the ramp before every flight, and here is what the alignment is: <em>&ldquo;The alignment computations use the basic premise that the only accelerations during alignment are due to the earth&rsquo;s gravity; the only motion during alignment is due to the earth&rsquo;s rotation.&rdquo;</em> The accelerometers find local vertical from gravity; then <em>&ldquo;the laser gyro sensed earth rate components are used to establish the heading of the airplane&rdquo;</em>, and <em>&ldquo;Earth rate sensing by the laser gyros allows the IRU to determine initial latitude&rdquo;</em>, which <em>&ldquo;is compared to the crew entered latitude&rdquo;</em> &mdash; a comparison that <em>&ldquo;must be favorable to complete the alignment period&rdquo;</em>. Minimum align time: ten minutes.</p>

<p>Read that again as a measurement rather than as avionics. Before the aircraft moves, its instruments determine which way is north and what latitude it is at, using nothing but gravity and the rotation of the Earth &mdash; and then check the answer against the crew. On a stationary Earth the gyros would see nothing to work with and the procedure would have no content. The signal is not marginal, either: Earth rate is 15.041&deg;/hr (the sidereal day is 23 h 56 m 4 s), of which 9.36&deg;/hr is horizontal at the latitude of London, while Honeywell&rsquo;s GG1320AN &mdash; the industry-standard navigation-grade ring laser gyro &mdash; has a typical bias stability of 0.0035&deg;/hr. The thing being measured is about four thousand times the instrument&rsquo;s noise floor. This is the same instrument, and the same 15&deg;/hr, that <a href="#ARG-A07">ARG-A07</a> records a flat-earth researcher measuring on camera and declining to accept.</p>

<p>The rotation then stays in the equations for the rest of the flight. The non-inertial terms a navigation-grade system must compensate are named in the professional literature as Earth rate, transport rate and Coriolis acceleration &mdash; and the same source notes the converse, that in cheap sensors &ldquo;Earth rate (15 deg/hr) stays below gyro errors and cannot be measured reliably&rdquo;, which is precisely why cheap sensors cannot navigate. The size of the Coriolis term at cruise: 2&Omega;<em>v</em> sin&nbsp;&phi; = 0.026 m/s&sup2; at 45&deg; and 250 m/s. Dropped from the mechanisation, an acceleration that size integrates to a position error of order &frac12;<em>at</em>&sup2; &mdash; something like 170 km after an hour, before any of the error-bounding behaviour of a real navigator is considered. It is not dropped.</p>

<h4>4. Two more residues that were measured, one of them from an aircraft</h4>

<p><strong>Weight.</strong> The vertical companion of the Coriolis term is the E&ouml;tv&ouml;s effect: 2&Omega;<em>v</em> cos&nbsp;&phi;, which at 45&deg; and 250 m/s is 0.026 m/s&sup2; &mdash; 2,578 mGal, about 0.26% of <em>g</em>, and reversing sign between east and west for a swing of some 5,150 mGal. Baron Roland von E&ouml;tv&ouml;s noticed the discrepancy in shipboard gravimetry and it was confirmed in 1908 by sending two ships across the Black Sea in opposite directions. Airborne gravity surveying inherited the problem wholesale &mdash; Harlan&rsquo;s 1968 paper in the <em>Journal of Geophysical Research</em> is titled, flatly, &ldquo;E&ouml;tv&ouml;s corrections for airborne gravimetry&rdquo;. An aircraft flying east weighs measurably less than the same aircraft flying west, and the survey industry has spent sixty years subtracting the difference.</p>

<p><strong>Time.</strong> In October 1971 Hafele and Keating put four caesium clocks on <em>scheduled commercial flights</em> and flew them round the world twice, once east and once west. Their abstract reports &ldquo;directionally dependent time differences&rdquo;: the flying clocks &ldquo;lost 59 &plusmn; 10 nanoseconds during the eastward trip and gained 273 &plusmn; 7 nanoseconds during the westward trip&rdquo;, against predictions of &minus;40 &plusmn; 23 and +275 &plusmn; 21. That 332-nanosecond split between the two directions is the east/west asymmetry of air travel, measured to the nanosecond, on ordinary airline tickets &mdash; and it exists <em>only</em> because the ground the aircraft take off from is itself moving. On a stationary Earth the two trips are mirror images and the split is zero. The experiment has been repeated by the National Physical Laboratory twice, London&ndash;Washington in 1996 (39 &plusmn; 2 ns against 39.8 predicted) and round the world in 2010 (230 &plusmn; 20 against 246 &plusmn; 3).</p>

<h4>5. What the frame argument does and does not have to do</h4>

<p>The reason an aircraft does not need to chase its destination is not that the atmosphere drags it. It is that ground speed is a relation between the aircraft and the ground, and both carry the same rotational velocity into the flight &mdash; the point Galileo made with a ship&rsquo;s sealed cabin in 1632 and which <a href="#ARG-A10">ARG-A10</a> works through in Rowbotham&rsquo;s own words, since Rowbotham granted that the atmosphere turns with the Earth and built an experiment to show it. That is the whole of the frame answer, and on its own it would leave <a href="#ARG-R03">ARG-R03</a>&rsquo;s reply standing: cancelling terms prove nothing either way.</p>

<p>Which is why the load in this entry is carried by the terms that do <em>not</em> cancel. Coriolis, E&ouml;tv&ouml;s, the sensed Earth rate in the alignment, the directional split in the clocks: four quantities that are zero on a stationary Earth, are not zero, and are each the size a rotating Earth predicts. The list asks whether aviation compensates for the spin. It does &mdash; in the alignment procedure, in the mechanisation equations, in the gravimeter&rsquo;s correction table and in the timing budget &mdash; and the compensations are the measurement.</p>""",

    advocate=dict(
        best_defense=(
            "Four moves. First, your inertial-navigation argument is circular and you should "
            "know it: the box is PROGRAMMED with 15 degrees per hour because its designers "
            "assumed rotation. A model that subtracts an assumed term and then reports that "
            "the residual is small has not measured anything. Second, the sign argument is "
            "weather, and weather is a free parameter. Eastbound is faster today because you "
            "call the wind a jet stream; if eastbound were slower you would call it a "
            "headwind. Any observation whatever is absorbed. Third — and this is the one you "
            "cannot wriggle out of — every instrument you cite measures rotation RELATIVE TO "
            "THE LOCAL INERTIAL FRAME. Ring lasers, Foucault pendulums, Coriolis, your "
            "clock experiment: all of them are silent on whether the Earth turns beneath a "
            "fixed heaven or the heavens turn about a fixed Earth, because in the second "
            "case the rotating cosmos defines the inertial frame. Your own site concedes "
            "this at ARG-R01 and ARG-R03. You have proved relative rotation, which nobody "
            "disputed, and then billed it as absolute. Fourth, look at what you have "
            "actually done here: you found a mid-1950s translated pamphlet, decided it is "
            "the origin of a claim four lines long on somebody else's website, and spent "
            "your best paragraph on a units discrepancy in a quotation. That is bookkeeping, "
            "not physics."),
        survives=4,
        preemptive=(
            "Four, and it is the third move that earns it — the frame-dragging escape is "
            "the strongest reply available to this cluster and the body must not be left "
            "looking as though it had not noticed. Three text commitments follow. (a) The "
            "circularity charge is answered inside section 3 and the answer must stay "
            "there, adjacent to the claim: the alignment does not subtract an assumed rate, "
            "it DERIVES LATITUDE from the sensed rate and refuses to complete when that "
            "disagrees with the crew's entry — an independent determination with a "
            "documented failure mode, on an open-loop rate sensor whose output is a fringe "
            "count. If an editor ever compresses that paragraph to 'the INS corrects for "
            "Earth rate', the section becomes exactly the circle the defender describes. "
            "(b) On the weather move, keep the LATITUDE REVERSAL in section 2 rather than "
            "the single record flight. One fast eastbound crossing is anecdote and a "
            "defender can call it wind; a wind system whose sign flips at 30 degrees, in "
            "the place rotating-fluid dynamics puts the flip, and which organised the "
            "Manila galleon route from 1565, is a structure. The record flight is the "
            "illustration, not the argument. (c) On the frame move, concede in public and "
            "narrow. The gyro half of this cluster IS observationally equivalent under a "
            "rotating-cosmos model, and that concession belongs in the body with a "
            "cross-link to ARG-R01 and ARG-R03 — but it does not touch the two claims "
            "actually on the list. 'Flight times symmetric' is false in the timetables "
            "whatever defines the inertial frame, and 'aircraft navigation not compensating "
            "for spin' is false in the alignment procedure whatever is rotating relative to "
            "what. A defender who reaches for general covariance to defend those two "
            "sentences has abandoned them. Finally, on the fourth move: do not defend the "
            "provenance work as physics. Say what it is — this is a page about where claims "
            "come from, the compression block is the product, and a substitution inside "
            "quotation marks is the cleanest specimen of the process it exists to document."),
    ),

    straw_man=dict(
        identified=True,
        detail=("Proof 23 of the same run, two items before the passage quoted above, states the "
                "position it is attacking as: gravity &ldquo;magically and inexplicably drags the "
                "entire lower-atmosphere of the Earth in perfect synchronization up to some "
                "undetermined height where this progressively faster spinning atmosphere gives way "
                "to the non-spinning, non-gravitized, non-atmosphere of infinite vacuum space.&rdquo; "
                "Three things there are nobody's account but the author's. The atmosphere is not "
                "dragged; it retains the rotational velocity it has always had, and gravity binds "
                "it rather than towing it. It does not spin progressively faster with height &mdash; "
                "tangential speed rises with radius by a fraction of a per cent over the whole "
                "depth of the troposphere, which is dwarfed by ordinary winds. And there is no "
                "boundary at which co-rotation stops: density falls off smoothly and the degree of "
                "co-rotation weakens gradually through the thermosphere and beyond. The caricature "
                "matters because it is aimed at the answer this page declines to give &mdash; see "
                "the SURFACE tier of the steelman &mdash; and a defender who has only ever met the "
                "'gravity drags the air' reply is entitled to think the argument works. Henriet's "
                "own closing line, by contrast, is not a straw man at all but a fair challenge: he "
                "asks what people who fly think of the rotation of the earth, and section 3 answers "
                "it with their alignment procedure.")),

    compression=dict(
        assessed=True, drifted=True,
        list_phrasing=("Aircraft navigation not compensating for spin. / Plane flight times "
                       "consistent with rest Earth. / Flight symmetry east/west. / "
                       "Flight times symmetric."),
        source_wording=("“…the average commercial airliner traveling 500mph should never be able to "
                        "reach its Eastward destinations before they come speeding up from behind! "
                        "Likewise Westward destinations should be arrived at thrice the speed, but "
                        "this is not the case.”"),
        drift_type="unsourced_addition",
        note=("<strong>The source&rsquo;s empirical claim is true; the list&rsquo;s is false.</strong> "
              "That is the finding, and it is the reverse of this project&rsquo;s usual one. Dubay "
              "denies a threefold westward advantage, which is correct &mdash; no such thing exists. "
              "Henriet, quoted in the next proof, offers no empirical observation in the passage "
              "Dubay reproduces: it is an <em>a priori</em> argument about what would follow if the "
              "ground moved, and what flight times actually do is not stated anywhere in it. Items 110 and 236 supply the "
              "missing premise on the sources&rsquo; behalf &mdash; &ldquo;Flight symmetry "
              "east/west&rdquo;, &ldquo;Flight times symmetric&rdquo; &mdash; and it is refutable "
              "from a timetable. Item 13&rsquo;s nearest source text is proof 27 (landing on a "
              "moving runway) and Henriet&rsquo;s airfield &ldquo;slipping away&rdquo;; the phrase "
              "&ldquo;navigation not compensating&rdquo; is the list&rsquo;s own.<br><br>"
              "<code>unsourced_addition</code> is recorded because the symmetry claim is attributed "
              "to a literature in which this pass could not locate it. <code>scope_widened</code> was the "
              "alternative &mdash; &ldquo;not thrice as fast&rdquo; widened into &ldquo;the "
              "same&rdquo; &mdash; and a reader who prefers it has both texts above to judge from.<br><br>"
              "<strong>The sharper drift happened one link earlier, and the enum has no word for it.</strong> "
              "Dubay&rsquo;s proof 26 quotes Henriet inside quotation marks and prints "
              "<em>miles</em> three times where Henriet wrote <em>kilometers</em> &mdash; verified in "
              "two independent copies of each book &mdash; while dropping a sentence from the middle "
              "without an ellipsis. The claim is rescaled by 1.61 in transit. It is invisible "
              "because both numbers survive the change: 1,000 km/h is the Earth&rsquo;s surface "
              "speed at the latitude of London to within four per cent, and 1,000 mph is the "
              "equatorial figure to within four per cent. This is not the list compressing a "
              "source; it is one source restating another and the number moving, which is the same "
              "process one link upstream.<br><br>"
              "<strong>The refutation answers the source, not the fragment.</strong> It takes "
              "Henriet&rsquo;s claim at his own strength &mdash; that an eastbound aircraft could "
              "not cover ground &mdash; and answers it with an eastbound aircraft covering ground "
              "at 1,327 km/h; it takes his challenge to ask people who fly and answers it with "
              "their alignment procedure. What the fragment adds, the symmetry of the timetables, "
              "is refuted separately, because the fragment is what circulates.")),

    verdict_challenge=dict(challenged=False, proposed_verdict=None, reasoning=None),

    people=["PER-DUBAY", "PER-CARPENTER"],
    related=["A07", "A09", "A10", "A16", "R01", "R03", "R08"],

    sources=[
        dict(label="Gabrielle Henriet, Heaven and Earth (translated from the French; mid-1950s) — "
                   "ch. II “On the fact that the earth does not rotate”, pp. 11–12, the aircraft "
                   "passage, reading “1,000 kilometers an hour”",
             url="https://archive.org/details/HeavenAndEarthGabrielleHenriet"),
        dict(label="Heaven and Earth — second copy consulted, PDF text layer, confirming "
                   "“kilometers” in the same three sentences",
             url="https://www.theflatearthsociety.org/library/books/Heaven%20and%20Earth%20(Gabrielle%20Henriet).pdf"),
        dict(label="Kook Science on Gabrielle Henriet — “a French-born proponent of a flat earth "
                   "theory”; Heaven and Earth catalogued 1956, Holborn Publishing Co., London; "
                   "The Solid Vault of Heaven, Regency Press, 1963, is a separate title",
             url="https://hatch.kookscience.com/wiki/Gabrielle_Henriet"),
        dict(label="Eric Dubay, 200 Proofs Earth Is Not a Spinning Ball — proofs 23, 25, 26, 27; "
                   "proof 26 prints Henriet with “miles” for “kilometers”",
             url="https://archive.org/details/200-proofs-the-earth-is-not-a-spinning-ball"),
        dict(label="William Carpenter, One Hundred Proofs that the Earth Is Not a Globe (1885) — "
                   "proof 44 “Firing in opposite direction” and proof 54 “Balloons not left "
                   "behind”: the east/west symmetry argument before aircraft existed",
             url="https://www.gutenberg.org/ebooks/55387"),
        dict(label="“Parallax” [Samuel Rowbotham], Zetetic Astronomy: Earth Not a Globe! (1865, "
                   "Simpkin, Marshall) — Section II, the air-gun experiment; and the date-line "
                   "passage calling east/west circumnavigation “no more favourable to the idea of "
                   "rotundity than … that the earth is a plane”",
             url="https://www.gutenberg.org/ebooks/69892"),
        dict(label="Operator IRS description (unofficial mirror) — “the only motion during "
                   "alignment is due to the earth’s rotation”; earth rate sensing establishes "
                   "heading and initial latitude, compared against the crew entry; 10-minute "
                   "minimum alignment",
             url="https://digilander.libero.it/andreatheone/irs.htm"),
        dict(label="Inside GNSS, “The Inertialist: Fundamentals of Inertial Navigation” — Earth "
                   "rate, transport rate and Coriolis acceleration as the compensated non-inertial "
                   "effects; “For lower-grade IMUs, Earth rate (15 deg/hr) stays below gyro errors "
                   "and cannot be measured reliably”",
             url="https://insidegnss.com/the-inertialist-fundamentals-of-inertial-navigation/"),
        dict(label="Honeywell GG1320AN digital ring laser gyro — “industry standard navigation "
                   "grade gyro”, bias stability 0.0035 deg/hr typical",
             url="https://www.redimec.com.ar/contenido/productos/pdf/1425567476_1.pdf"),
        dict(label="Hafele & Keating, “Around-the-World Atomic Clocks: Observed Relativistic Time "
                   "Gains”, Science 177:168–170 (1972) — “directionally dependent time "
                   "differences”; −59 ± 10 ns eastward, +273 ± 7 ns westward",
             url="http://faculty.bard.edu/hhaggard/teaching/phys125Sp19/homework/HafeleKeatingFlyingClocks.pdf"),
        dict(label="Hafele–Keating experiment — the prediction table (−40 ± 23 eastward, +275 ± 21 "
                   "westward) and the NPL repeats of 1996 and 2010",
             url="https://en.wikipedia.org/wiki/Hafele%E2%80%93Keating_experiment"),
        dict(label="Guinness World Records — fastest subsonic transatlantic commercial flight: "
                   "BA112, Boeing 747-400, JFK–Heathrow, 9 February 2020, 4 hr 56 min for 5,554 km, "
                   "1,327 km/h over the ground against a ~933 km/h cruise",
             url="https://www.guinnessworldrecords.com/world-records/601621-fastest-subsonic-transatlantic-commercial-flight"),
        dict(label="CNN, “Strong jet stream sees transatlantic aircraft fly at the ‘speed of sound’” "
                   "— “the jet stream is the reason why eastbound flights tend to be shorter than "
                   "westbound ones … time differences of an hour or more”",
             url="https://www.cnn.com/travel/article/jet-stream-flights-speed-of-sound/index.html"),
        dict(label="Eötvös effect — the 2Ωu cos φ correction, the Potsdam shipboard measurements "
                   "and the two-ship Black Sea confirmation of 1908",
             url="https://en.wikipedia.org/wiki/E%C3%B6tv%C3%B6s_effect"),
        dict(label="Harlan, “Eötvös corrections for airborne gravimetry”, J. Geophys. Res. "
                   "73:4675 (1968) — the correction as routine survey practice",
             url="https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/JB073i014p04675"),
        dict(label="Global atmospheric circulation — Coriolis deflection of the Hadley and Ferrel "
                   "cells produces easterly trades and mid-latitude westerlies",
             url="https://geo.libretexts.org/Courses/Fullerton_College/Introduction_to_Earth_Science_(Ikeda)/16:_The_Atmosphere/16.07:_Global_Atmospheric_Circulations"),
        dict(label="Trade winds — equatorward surface air “deflected toward the west in both "
                   "hemispheres by the Coriolis effect”; Urdaneta’s 1565 return route using the "
                   "westerlies",
             url="https://en.wikipedia.org/wiki/Trade_winds"),
    ]),
}
