# -*- coding: utf-8 -*-
"""Batch 6 — B01. "Water finds its level, therefore the surface is a plane."

Written 2026-08-07, promoted ahead of larger clusters because it is the item
actively circulating: a flat-earth account posting "we have SEA LEVEL! It isn't
SEA CURVE!" over a link to Gutenberg #55387 — Carpenter's One Hundred Proofs
(1885), not Dubay.

Four findings a future session should not have to re-derive.

1. OUR ATTRIBUTION IS HALF WRONG. The cluster credits both items to Rowbotham,
   Zetetic Astronomy, 1849. Item 42 ("Water finds level.") is fairly his — the
   1849 pamphlet's own title asserts "the surface of the sea is a perfect plane."
   Item 384 ("River grades.") is NOT. There is no river-gradient argument in the
   1849 pamphlet as quoted by Schadewald, none in the 1865 Earth Not a Globe
   full text (searched: "Nile" not present), and no "Nile" or "Rivers" entry in
   the 1881 third edition's own General Index. The earliest text we can document
   is Carpenter 1885, proof 4, which passes verbatim into Dubay's proof 5.

2. THE BRIEF'S PREMISE ABOUT CARPENTER IS WRONG, AND USEFULLY SO. It was put to
   this session that Carpenter never argues from the word "level" — only from
   observation. He does. Proof 18: "Every man in full command of his senses
   knows that a level surface is a flat or horizontal one; but astronomers tell
   us that the true level is the curved surface of a globe! ... so they give him
   one in name which is not one in fact!" That IS the "sea level, not sea curve"
   move, in 1885. The meme is not a modern degradation; it is Carpenter's
   proof 18. What the meme gets wrong is which proof it cites — it links a book
   whose proof 2 is empirical while running the argument of proof 18.

3. THE KERNEL IS NEWTON. "A free water surface is an equilibrium surface" is the
   premise of Principia III's principle of canals, from which Newton derived a
   flattening of ~1/230 with no astronomy at all. Rowbotham had the right
   premise and never solved it. Do not argue that water fails to find its level.

4. THE 1849 PAMPHLET IS NOT ONLINE. Searched: Gutenberg, archive.org,
   sacred-texts, the LoC flat-earth guide, Google Books. Only the title and
   Schadewald's verbatim extract are reachable. Recorded in the gloss.
"""

ENTRY = {

"B01": dict(
    tldr=("Water does find its level — concede it immediately, because it is true and it is "
          "the founding premise of geodesy, not a flat-earth discovery. A level surface is one "
          "of constant gravitational potential, perpendicular to gravity everywhere, and on a "
          "rotating Earth that surface is curved: Newton derived the planet's oblateness from "
          "this premise alone in 1687, and the sea obliges by standing 21.4 km further from the "
          "centre at the equator than at the poles. The argument needs “level” to mean “planar”, "
          "and that sense is a later offshoot of a word that began as the name of a gravity "
          "instrument."),

    passage=dict(
        work="WRK-ROWBOTHAM-1849", pd=True,
        locator=("title page, and the sixth experiment (fig. 9). No transcription or scan of the "
                 "16-page pamphlet could be reached; the body sentence is quoted from Schadewald, "
                 "The Plane Truth, ch. 1, which reproduces it verbatim"),
        quote="""ZETETIC ASTRONOMY. A description of several experiments which prove that the surface of the sea is a perfect plane, and that the earth is not a globe!

[title page, continued] Being the substance of a paper read before the Royal Astronomical Society on the evening of Dec. 8, 1848.

[the sixth experiment] A small boat was sent out 6 miles from the Theodolite—as represented in fig. 9, but no convexity whatever could be detected! the surface of the water was perfectly level!!""",
        gloss="""<p><strong>The claim is in the title.</strong> Rowbotham's first publication &mdash; sixteen pages, Birmingham, 1849, under the pseudonym &ldquo;Parallax&rdquo; &mdash; does not argue from hydrostatic principle at all. It asserts a result: <em>the surface of the sea is a perfect plane</em>, established by six experiments with a surveyor's theodolite. The logical form is a modus tollens, and it is the same form in the mature book. <em>Earth Not a Globe</em> opens its water chapter: &ldquo;If the earth is a globe, and is 25,000 English statute miles in circumference, the surface of all standing water must have a certain degree of convexity&mdash;every part must be an <em>arc of a circle</em>.&rdquo; Then the observation, then the denial of the consequent. Rowbotham is not saying &ldquo;water is level by nature, therefore the Earth is flat.&rdquo; He is saying &ldquo;a globe predicts convex standing water; I went and looked; it was not convex.&rdquo;</p>
<p><strong>We could not reach the 1849 text.</strong> Searched: Project Gutenberg, archive.org, sacred-texts, the Library of Congress flat-earth research guide, and Google Books. The pamphlet is catalogued but not digitised anywhere we can read. The quotation above is therefore the title, which is the claim, plus the one body sentence Robert Schadewald reproduces verbatim. <em>WRK-ROWBOTHAM-1849 is public domain and we would quote it at length if we could.</em> This is a coverage gap in the primary record, not a stylistic choice.</p>
<p><strong>The title page contains a documented misrepresentation.</strong> &ldquo;Being the substance of a paper read before the Royal Astronomical Society on the evening of Dec. 8, 1848&rdquo; is not what happened. Augustus De Morgan, who was the Society's Secretary at the time and is therefore the best possible witness, recorded in <em>A Budget of Paradoxes</em>: &ldquo;No account of such a paper appears in the Notice for that month &hellip; Dec. 8, 1848, the Secretary of the Astronomical Society (De Morgan by name) said, at the close of the proceedings,&mdash;&lsquo;Now, gentlemen, if you will promise not to tell the Council, I will read something for your amusement:&rsquo; and he then read a few of the arguments that had been transmitted by the lecturer.&rdquo; The founding document of the tradition claims an institutional hearing it did not get, on its title page, in its first year.</p>
<p><strong>What the circulating meme actually cites.</strong> The post that prompted this treatment &mdash; &ldquo;we have SEA LEVEL! It isn't SEA CURVE!&rdquo; &mdash; links Gutenberg #55387, William Carpenter's <em>One Hundred Proofs that the Earth Is Not a Globe</em> (Baltimore, 1885), not Rowbotham and not Dubay. Carpenter restates the claim as <strong>proof 2</strong>: &ldquo;Whenever experiments have been tried on the surface of standing water, this surface has always been found to be level. If the Earth were a globe, the surface of all standing water would be convex. This is an experimental proof that Earth is not a globe.&rdquo; Carpenter is explicit that he is a follower, not an author: his introduction opens &ldquo;&lsquo;Parallax,&rsquo; the Founder of the Zetetic Philosophy, is dead,&rdquo; calls Rowbotham &ldquo;certainly, one of the most gifted of men,&rdquo; and says he is &ldquo;proud of having spent many a pleasant hour in the company of Samuel Birley Rowbotham.&rdquo; <strong>So the meme cites the distributor as the authority, thirty-six years downstream of the claim, in a book that says on its first page whose claim it is.</strong></p>
<p><strong>And it cites the wrong proof inside the right book.</strong> Proof 2 is empirical &mdash; a claim about what canal experiments found. The meme argues from the <em>word</em>: we say &ldquo;sea level,&rdquo; not &ldquo;sea curve,&rdquo; therefore the sea is flat. That is a different argument, and it is not proof 2 &mdash; but it is not new either, and it is not the meme's invention. It is Carpenter's <strong>proof 18</strong>: &ldquo;Every man in full command of his senses knows that a level surface is a flat or horizontal one; but astronomers tell us that the true level is the curved surface of a globe! They know that man requires a level surface on which to live, so they give him one in name which is not one in fact!&rdquo; The argument from terminology has been in the tradition since 1885. It is simply filed under a different number than the one the meme links.</p>
<p><strong>The second item in this cluster has a different father.</strong> Item 384, &ldquo;River grades.&rdquo;, is Carpenter's <strong>proof 4</strong>: &ldquo;There are rivers that flow for hundreds of miles towards the level of the sea without falling more than a few feet&mdash;notably, the Nile, which, in a thousand miles, falls but a foot. A level expanse of this extent is quite incompatible with the idea of the Earth's &lsquo;convexity.&rsquo;&rdquo; We looked for an earlier source and did not find one: the argument is absent from the 1849 pamphlet as quoted, the word &ldquo;Nile&rdquo; does not occur in the full text of the 1865 <em>Earth Not a Globe</em>, and the 1881 third edition's own General Index has no entry for &ldquo;Nile&rdquo; or &ldquo;Rivers&rdquo; (it has one for &ldquo;Standing water, experiments demonstrating the true form of, 9&ndash;62&rdquo;). Carpenter's sentence then passes into Eric Dubay's <em>200 Proofs</em> (2015) almost unaltered as proof 5 &mdash; &ldquo;One portion of the Nile River flows for a thousand miles with a fall of only one foot&rdquo; &mdash; alongside proof 3, &ldquo;The natural physics of water is to find and maintain its level,&rdquo; which is proof 2 modernised. <strong>Our own cluster record attributes both items to Rowbotham 1849; on the river item that is an error, and it is recorded below.</strong></p>"""),

    steelman=dict(
        description="""<p><strong>SURFACE (weak &mdash; and it loses the argument on contact).</strong> &ldquo;Water doesn't find its level.&rdquo; Anyone who says this has conceded the exchange. Water in a connected vessel absolutely does come to rest on a single, reproducible, well-defined surface, it does so quickly, and it does so identically in a bathtub, a canal, a spirit level and an ocean. It is one of the most robust everyday facts there is. Do not attack it. A close cousin, equally bad: &ldquo;the curvature is too small to see.&rdquo; True over a bathtub and irrelevant over the Atlantic, and it silently concedes that the surface really is a plane to within measurement, which is not what we mean.</p>
<p><strong>DEEPER (true but incomplete).</strong> &ldquo;&lsquo;Level&rsquo; is a technical term meaning equipotential, and an equipotential on a rotating spheroid is curved.&rdquo; This is correct, it is the operative definition in geodesy, and it is the answer. But stated bare it sounds exactly like what a defender says it is &mdash; a redefinition produced on demand to rescue a theory &mdash; and it invites the reply &ldquo;then no observation of a water surface could ever count against you.&rdquo; That reply has to be answered, not asserted past.</p>
<p><strong>KERNEL &mdash; the premise is not merely defensible, it is the founding premise of the science being attacked.</strong> &ldquo;A free water surface is an equilibrium surface&rdquo; is precisely the assumption Isaac Newton used to derive the shape of the Earth in the <em>Principia</em>, by what became known as the <em>principle of canals</em>: imagine two water-filled channels bored from the surface to the centre, one from the equator and one from the pole, meeting there. If the water is in equilibrium the two columns must balance. The equatorial column is lightened by the rotation, so it has to be longer. Newton solved it and got a polar-to-equatorial axis ratio of 689 to 692 &mdash; a flattening of about 1 in 230 &mdash; from hydrostatics alone, with no telescope, no voyage and no survey. That is &ldquo;water finds its level&rdquo; carried through to a number. Rowbotham had the right premise. He simply stopped at the premise.</p>
<p><strong>And the terminology really is misleading &mdash; this part of the complaint is fair.</strong> A spirit level does define a tangent plane. A surveyor setting out a slab does treat &ldquo;level&rdquo; as &ldquo;flat.&rdquo; In ordinary English a level line <em>is</em> a straight horizontal one, and the two senses are not distinguishable by the instrument at the scale the instrument is used: over a 30 m run the geoid departs from the tangent plane by <strong>0.07 mm</strong>, and the angle between them is <strong>about 1 arcsecond</strong> &mdash; roughly a quarter of one division on the most sensitive machinist's bubble level made. Rowbotham was not being stupid and was not playing dumb. He was using the word the way his readers used it, in the one regime where the two meanings genuinely coincide.</p>""",

        why_it_doesnt_save_claim="""<p><strong>Because the premise, solved rather than merely stated, returns a curved surface &mdash; and the number is right.</strong> Newton's hydrostatic argument predicted a flattening near 1/230; the measured value is <strong>1/298.257223563</strong>, and the WGS 84 figure of the Earth stands 6,378,137.0 m from centre to equator against 6,356,752.3 m to the poles. The ocean's own surface is <strong>21.4 km</strong> further from the centre at the equator than at the poles, and it is there because the planet turns. Newton was wrong in the third digit and right in the physics, which is the ordinary condition of a first-principles prediction. &ldquo;Water finds its level&rdquo; is not a fact the flat model owns and the round model must explain away. It is a fact the round model <em>used</em>, two centuries before Rowbotham, to compute its own shape.</p>
<p><strong>Because the scale at which the two senses of &ldquo;level&rdquo; coincide is exactly the scale at which the claim carries no information.</strong> The convergence is real and it is quantitative: 1 arcsecond over 30 m, undetectable; <strong>32 arcseconds over 1 km</strong>, about eight divisions on the same instrument, and unmissable. That is not a boundary anyone drew to be convenient. It is the reason precise levelling procedure balances backsights against foresights and tolerances the imbalance &mdash; see <a href="#ARG-B05">ARG-B05</a>. The observation &ldquo;my level says the water is flat&rdquo; is true and empty; the observation &ldquo;the water surface is planar over a kilometre&rdquo; is a measurement, and it comes out the other way.</p>
<p><strong>Because a level surface exists on both models, so its existence discriminates nothing.</strong> This is the question the argument never asks. On a flat Earth there is a level water surface. On a spheroidal Earth there is a level water surface. Every hydrostatic fact in the cluster &mdash; water settles, canals hold water, a bubble centres, a river runs downhill &mdash; is predicted by both. The discriminating content is not <em>whether</em> there is a level surface but <em>what shape</em> it has, and that has been surveyed, sounded, gravimetrically modelled and mapped from orbit. It is not a plane, it is not even an ellipsoid, and its departures from the ellipsoid reach 100 m in either direction and track the mass anomalies that produce them.</p>"""),

    refutation="""<p><strong>1. Grant the premise completely, because it is true.</strong> A fluid at rest, free to move under gravity alone, comes to rest with its surface everywhere perpendicular to the local gravity vector. That is hydrostatic equilibrium: were any part of the surface not perpendicular, there would be an unbalanced component along it and the water would still be moving. This is not disputed physics, it is not a recent formulation, and it is not something anyone answering this argument should want to weaken. Water finds its level. The entire content of the dispute is in the next sentence.</p>

<p><strong>2. What &ldquo;level&rdquo; means, in the trade that owns the word.</strong> A level surface is an <em>equipotential</em> surface of the gravity field: a surface along which you can move a mass without doing work on it or extracting work from it. NOAA's National Geodetic Survey puts it in exactly those terms &mdash; &ldquo;<em>We define horizontal motion, when there is no change in potential energy</em>&rdquo;, as against &ldquo;<em>motions along the vertical that are associated with a gain or loss of energy</em>&rdquo; &mdash; and states the consequence for fluids directly: &ldquo;<em>Water will flow as a function of height difference and/or changes in the gravity field. This combination is defined as geopotential.</em>&rdquo; The particular equipotential that best fits global mean sea level is the <strong>geoid</strong>. It is closed, it wraps the planet, it is the reference for every orthometric height ever published, and it is curved. A plumb line hangs along its normal; a bubble level sits in its tangent plane; still water lies in it.</p>

<p>The word's own history says the same thing. &ldquo;Level&rdquo; comes into English in the mid fourteenth century as the name of a <em>tool</em> &mdash; Old French <em>livel</em>, from Latin <em>libella</em>, &ldquo;a balance,&rdquo; the diminutive of <em>libra</em>, the scales. It is named after the instrument that finds the direction of gravity, and the geometric senses are later growths from that root: the Online Etymology Dictionary dates the adjective &ldquo;having an even surface&rdquo; to the early fifteenth century, and &ldquo;lying in the same horizontal plane&rdquo; to the 1550s &mdash; two centuries after the tool. Both are genuine senses of the word, as the steelman above concedes, but neither is the primitive one; and &ldquo;sea level&rdquo; itself descends from the noun sense &ldquo;position as marked by a horizontal line&rdquo; (1530s), which is a height, not a shape. An argument that runs &ldquo;we say sea <em>level</em>, not sea <em>curve</em>&rdquo; leans on the derived sense while presenting it as the original one, and the original one is the name of a gravity instrument.</p>

<p><strong>3. Where the equivocation happens, in numbers.</strong> The argument needs one word to carry two meanings: (a) <em>level</em> = perpendicular to gravity everywhere, and (b) <em>level</em> = lying in a Euclidean plane. Over short runs these are indistinguishable, and the honest thing is to say by how much. Taking R = 6,371 km, a tangent plane departs from the equipotential by d&sup2;/2R:</p>
<ul>
<li>over <strong>30 m</strong> (a builder's straightedge): <strong>0.07 mm</strong>; angle between the two surfaces, <strong>0.97&Prime;</strong>. The most sensitive machinist's level in normal use reads about 0.02 mm/m, or 4.1&Prime; per division. The curvature is a quarter of one division. <em>The instrument physically cannot see it.</em></li>
<li>over <strong>1 km</strong>: <strong>78 mm</strong>; angle <strong>32&Prime;</strong>, close to eight divisions. Now it is the dominant error, which is why levelling procedure is built to cancel it.</li>
<li>over <strong>800 km</strong> (Aswan to Cairo): <strong>about 50 km</strong>.</li>
</ul>
<p>Sense (a) is the one every instrument implements, because bubbles and plumb bobs respond to gravity and to nothing else. Sense (b) is an approximation to it that is superb below a hundred metres and worthless above a hundred kilometres. The argument takes an observation valid in the first regime and asserts a conclusion about the second.</p>

<p><strong>4. So does anything here distinguish a flat Earth from a globe?</strong> Not the existence of a level surface, which both models have. The discriminating question is what shape the level surface has, and it has been measured four independent ways, none of them optical and none of them dependent on a photograph.</p>
<p><em>(i) The sea stands 21.4 km higher at the equator.</em> The equatorial radius of the reference figure is 6,378,137.0 m and the polar radius 6,356,752.3 m &mdash; a flattening of 1/298.257223563. That bulge is not a land feature; the ocean surface participates in it, because the ocean surface <em>is</em> the equipotential. And its cause is rotation: a self-gravitating fluid that turns must be oblate, which is the whole content of Newton's canal calculation and of Clairaut's theorem after him. The observed value sits within a few tenths of Newton's 1687 estimate. Water found its level, and the level it found is the signature of a spinning planet.</p>
<p><em>(ii) The level surface is not even an ellipsoid, and the lumps are where the mass is.</em> The geoid departs from the best-fitting ellipsoid by up to 100 m in either direction, and those departures correlate with density structure &mdash; which is what makes the geoid a working geophysical tool rather than a fitted curve. Satellite gravimetry maps it globally and repeatedly, and terrestrial levelling against tide gauges agrees with it. A model in which &ldquo;level&rdquo; means &ldquo;planar&rdquo; has nothing to say about any of this, and predicts none of it.</p>
<p><em>(iii) Two connected seas are not at the same height.</em> Mean sea level at the Pacific end of the Panama Canal stands about <strong>20 cm</strong> above mean sea level at the Atlantic end, from density and wind differences. The Permanent Service for Mean Sea Level states the general case flatly: <em>mean sea level is not a &ldquo;level surface&rdquo;</em>. This is worth dwelling on, because it cuts against the flat model in an unexpected direction: the sea is not even <em>exactly</em> equipotential, let alone planar. The argument's own premise, taken at the precision now available, is an approximation &mdash; and the departures from it are measured, explained and modelled.</p>
<p><em>(iv) The level surface moves, twice a day.</em> Tides are the equipotential itself being deformed by the Moon and the Sun, and the water following it. A surface whose defining property is that it is perpendicular to the total gravity field must move when the field changes, and it does, by metres, on schedule, everywhere, in step with an astronomical calculation. On the &ldquo;level means planar&rdquo; reading there is no reason for any of this to happen.</p>

<p><strong>5. River grades &mdash; item 384, and Carpenter's proof 4.</strong> The sub-argument is that rivers fall almost nothing over enormous distances, so the land they cross must be a plane; in its stronger form, that on a globe some rivers would have to flow uphill. Three answers, in order of increasing force.</p>
<p><em>First, the headline number is simply wrong.</em> Carpenter wrote that the Nile &ldquo;in a thousand miles, falls but a foot,&rdquo; and Dubay reprints it. The Nile falls from 378 m above sea level at Khartoum to 91 m at Aswan &mdash; <strong>over 280 m in some 1,847 km</strong>, a gradient of about 15 cm/km. From Aswan to Cairo, roughly 500 miles, the modern river falls <strong>about 70 m</strong>, some 460 feet per thousand miles. Even the flattest reach in the whole system, the White Nile between Malakal and Khartoum through the Sudd, runs at about <strong>1:101,000</strong>, under 1 cm/km &mdash; which is still 52 feet per thousand miles, fifty-two times Carpenter's figure. There is no reach of the Nile that falls a foot in a thousand miles, and the flattest large-river reach on Earth is not within an order of magnitude of it.</p>
<p><em>Second, gradient is measured against the geoid, not against a plane.</em> A river's slope is a loss of <em>potential</em>, which is what makes water move; NGS again, &ldquo;<em>water will flow as a function of height difference and/or changes in the gravity field.</em>&rdquo; The heights in every river-gradient figure ever quoted &mdash; gauge datums, SRTM and satellite altimetry products, national levelling networks &mdash; are orthometric heights, referred to the geoid. So a river falling 70 m over 800 km is losing 70 m of height <em>above the equipotential</em>. Over that same 800 km the equipotential departs from a tangent plane by about 50 km. The two quantities are not competing; they are not even the same kind of quantity. The intuition that the river must &ldquo;climb the curve&rdquo; treats a 50 km geometric departure as though it were a hydraulic slope, and it is not one: the equipotential has, by construction, zero slope. Water is not being asked to run uphill, because the curve is not uphill. The curve is the definition of horizontal.</p>
<p><em>Third, this is not a second argument.</em> It is the same equivocation applied to a moving fluid instead of a standing one. Grant &ldquo;level&rdquo; its technical sense and both items dissolve together; insist on the planar sense and both items still fail, because the numbers are wrong.</p>
<p>The companion claim, Dubay's proof 4, that rivers flow &ldquo;North, South, East, West and all other intermediary directions&rdquo; and that on a globe many would be flowing uphill, is answered by the same sentence. Compass direction has nothing to do with potential. The Nile flows north and downhill; the Amazon flows east and downhill; every river on the planet flows in whatever compass direction its terrain runs and in exactly one direction with respect to the geopotential, which is down.</p>

<p><strong>6. Is this just a definition rigged to be unfalsifiable?</strong> The most serious objection to everything above is that &ldquo;level&rdquo; has been redefined so that no observation of water could ever contradict the round Earth. It has not, and the test is whether the definition generates numbers that could have come out otherwise. Three did.</p>
<p>(a) <strong>Newton's flattening was a prediction, and it was wrong &mdash; in the direction that could have killed it.</strong> He got 1/230 from hydrostatics; his contemporary rivals, the Cassinis, held from French meridian arcs that the Earth was <em>prolate</em>, lengthened at the poles, which is the opposite sign. That dispute was settled by going and measuring, on the Lapland and Peru expeditions of the 1730s, and it could have gone the other way. It went Newton's, and the modern value is 1/298.257 &mdash; a real disagreement with 1/230 that later theory (Clairaut, and the Earth's non-uniform density) had to earn its way out of.</p>
<p>(b) <strong>The geoid is measured before it is used, and it has a residual.</strong> If &ldquo;level&rdquo; simply meant &ldquo;whatever the water does,&rdquo; the Panama result &mdash; 20 cm of head between two connected oceans &mdash; could not be stated at all, because there would be nothing for it to be a departure <em>from</em>. It is stated, and quantified, precisely because the equipotential is defined independently of the sea surface. That is the mark of a real reference, not a rigged one.</p>
<p>(c) <strong>The 8-inches-per-mile-squared figure is the flat model's own arithmetic, and it is a prediction with a threshold.</strong> Below about a hundred metres it says curvature is unmeasurable with a bubble; above a kilometre it says curvature dominates. Both halves are checkable, and the second half is checked every working day by levelling crews who balance their sights for exactly this reason and tabulate the correction when they cannot. Rowbotham took that figure from the <em>Encyclop&aelig;dia Britannica</em> article on Levelling &mdash; the same article that told him &ldquo;<em>the curve of the Earth being the true level, and the tangent to it the apparent level</em>&rdquo; &mdash; and reprinted the definition that answers him. See <a href="#ARG-B06">ARG-B06</a>.</p>

<p><strong>7. Scope, and where the neighbouring arguments live.</strong> This cluster is the <em>hydrostatic</em> claim: what a water surface is, and what &ldquo;level&rdquo; means. It is not the optical one. Whether ships, lighthouses and towers stay visible further than a spherical Earth allows is <a href="#ARG-B04">ARG-B04</a>, and turns on atmospheric refraction. Rowbotham's Old Bedford Canal trials, which are where his 1849 water sentence comes from, are <a href="#ARG-B03">ARG-B03</a>: that cluster covers the two-point near-water sightline that produces a false null, Wallace's three-point 1870 repeat and Oldham's 1901 replication. The engineering form &mdash; canals and railways built without a curvature allowance &mdash; is <a href="#ARG-B05">ARG-B05</a>. Plumb-line convergence, which is the same equipotential fact stated as a direction rather than a surface, is <a href="#ARG-B09">ARG-B09</a>. B01 answers the premise those four all borrow.</p>

<p><strong>Verdict: refuted, and refuted by conceding the premise.</strong> Water finds its level; a level surface is an equipotential surface; an equipotential surface on a rotating, self-gravitating body is curved and specifically oblate; the oblateness was computed from this premise in 1687 and measured to nine significant figures since. The argument survives only on an equivocation between two senses of one word, in the regime where they happen to agree to within a fraction of an arcsecond &mdash; and it is stated in a vocabulary borrowed wholesale from the surveyors who use the technical sense.</p>""",

    advocate=dict(
        survives=3,
        best_defense=(
            "You have not refuted anything; you have relabelled. Notice what you did. I said water "
            "is level. You agreed. Then you announced that \"level\" secretly means \"curved\", "
            "cited the people who profit from saying so, and declared the matter closed. That is "
            "not physics, it is lexicography, and it is unfalsifiable by construction: on your "
            "definition there is no possible observation of a water surface that could count "
            "against a globe, because any surface water rests on is by definition the level one. "
            "Second, you keep handing me my own case. You concede the two senses of \"level\" are "
            "indistinguishable to the instrument at every scale a human being ever actually uses "
            "one. Every direct measurement anyone has ever made of a water surface with an "
            "instrument in their hands returns a plane. The curvature only appears when you switch "
            "from the instrument to a model — WGS 84, a geoid grid, a satellite product — every "
            "one of which has the radius built into it before the first datum is processed. Third, "
            "the 21 km bulge and the 100 m geoid undulations are not observations of water; they "
            "are outputs of gravity models fitted to satellite tracking, which assume the shape "
            "they report. Show me a photograph of a curved lake."),
        preemptive=(
            "Rated 3: this is the reply the page will actually receive, and section 6 of the "
            "refutation was written specifically to answer it — it did not exist in the first "
            "draft and must not be cut. The concrete change: a numbered subsection headed \"Is "
            "this just a definition rigged to be unfalsifiable?\" giving three cases where the "
            "definition produced a number that could have come out otherwise — (a) Newton's 1/230 "
            "against the Cassinis' prolate Earth, settled by the Lapland and Peru expeditions, "
            "with the honest admission that 1/230 disagrees with the modern 1/298.257; (b) the "
            "20 cm Panama head, which is only *statable* because the equipotential is defined "
            "independently of the sea surface; (c) 8-inches-per-mile-squared as a two-sided "
            "prediction with a threshold, both halves checkable. Two further hardening moves if "
            "this argument recurs. First, meet the \"it's all models with the radius baked in\" "
            "charge with pre-satellite, pre-model measurements: the Lapland and Peru arcs "
            "(1735–40) measured a degree of latitude with theodolites and zenith sectors and "
            "found the degree *longer* near the pole, which is oblateness measured directly, a "
            "century and a half before anyone had a datum to assume. Second, decline the "
            "photograph demand explicitly rather than by omission — a photograph of a lake is an "
            "optical measurement and belongs to ARG-B04, where refraction is the controlling "
            "term; B01 rests on gravimetry, levelling and tide-gauge data precisely because those "
            "do not depend on light paths at all. Do not answer a hydrostatic argument with a "
            "picture.")),

    straw_man=dict(
        identified=True,
        detail=("Carpenter's proof 18 is a misrepresentation of the mainstream position and it is "
                "the one the modern meme inherits: astronomers, it says, know people need a level "
                "surface \"so they give him one in name which is not one in fact\" — a deliberate "
                "bait-and-switch, a word issued in bad faith. Nobody did that. \"Level\" named a "
                "gravity instrument, the Latin libella or balance, four centuries before anyone "
                "had a theory of the geoid; the technical sense is the original sense and the "
                "planar sense is the loose one. Proof 90 does the same work by inventing a "
                "spokesman: \"Is water level, or is it not?\" was a question once asked of an "
                "astronomer. \"Practically, yes; theoretically, no,\" was the reply — an "
                "unnamed astronomer, an unsourced exchange, and a concession no geodesist would "
                "phrase that way, since on the technical definition the answer is simply yes. A "
                "third misrepresentation is institutional rather than scientific and sits on the "
                "founding document itself: the 1849 pamphlet's title page claims its contents "
                "were \"read before the Royal Astronomical Society\" on 8 December 1848. De "
                "Morgan, the Society's own Secretary, recorded that he read out a few of the "
                "transmitted arguments for the members' amusement after the close of proceedings, "
                "having asked them not to tell the Council.")),

    compression=dict(
        assessed=True, drifted=True,
        list_phrasing=("Water finds level. (item 42)  /  River grades. (item 384)"),
        source_wording=("&ldquo;A description of several experiments which prove that <em>the surface of the "
                        "sea is a perfect plane</em>, and that the earth is not a globe!&rdquo; &mdash; and, in the "
                        "mature statement, &ldquo;<em>If the earth is a globe &hellip; the surface of all standing "
                        "water must have a certain degree of convexity&mdash;every part must be an arc of a "
                        "circle.</em>&rdquo; On rivers, Rowbotham says nothing at all."),
        drift_type="unsourced_addition",
        note=("<p><strong>The two items in this cluster drift differently, and one of them does not drift.</strong> "
              "The enum forces a single value, so it is set to the finding that actually changes the record; "
              "both are set out here.</p>"
              "<p><strong>Item 42 &mdash; no drift.</strong> &ldquo;Water finds level.&rdquo; is a fair label for "
              "Rowbotham's claim at Rowbotham's strength. If anything the list is <em>weaker</em> than its source: "
              "the item states a hydrostatic principle that mainstream physics also asserts, while the 1849 title "
              "asserts the far bolder and quite false proposition that the sea's surface is <em>a perfect plane</em>. "
              "There is no hedge to have dropped &mdash; Rowbotham does not hedge, in 1849 or in 1881 &mdash; and no "
              "scope to have widened. We looked for a drift here and did not find one, and say so rather than "
              "manufacture one.</p>"
              "<p><strong>Item 384 &mdash; unsourced addition.</strong> &ldquo;River grades.&rdquo; is credited by our "
              "own cluster record, and by the movement's own genealogy, to Rowbotham's 1849 <em>Zetetic Astronomy</em>. "
              "It is not there. The argument does not appear in the 1849 pamphlet as Schadewald quotes it; the word "
              "&ldquo;Nile&rdquo; does not occur in the full text of the 1865 <em>Earth Not a Globe</em>; and the 1881 "
              "third edition's own General Index carries no entry for &ldquo;Nile&rdquo;, &ldquo;Rivers&rdquo;, "
              "&ldquo;Amazon&rdquo; or &ldquo;Mississippi&rdquo;. The earliest text we can document is <strong>Carpenter, "
              "1885, proof 4</strong> &mdash; &ldquo;the Nile, which, in a thousand miles, falls but a foot&rdquo; &mdash; "
              "which passes near-verbatim into Dubay's proof 5 in 2015. So a claim invented by the distributor is "
              "attributed to the originator, and the modern list inherits the misattribution intact. "
              "<strong>We inherited it too: the correction is to our own record, not only to theirs.</strong></p>"
              "<p><strong>The circulating meme drifts a third way, and it is the interesting one.</strong> "
              "&ldquo;Why do people think the Earth is a globe when we have SEA LEVEL! It isn't SEA CURVE!&rdquo; is an "
              "argument from terminology, and it is posted over a link to Carpenter's proof 2, which is an argument "
              "from experiment. Taken as a gloss on proof 2 that is a clean category shift &mdash; an empirical claim "
              "about canal trials restated as a claim about what a word implies. But the shift is not the meme's, and "
              "it is not modern. Carpenter's <strong>proof 18</strong> makes exactly the terminological argument, in "
              "1885, in the same book: &ldquo;<em>Every man in full command of his senses knows that a level surface is "
              "a flat or horizontal one; but astronomers tell us that the true level is the curved surface of a globe!"
              "</em>&rdquo; The meme is a faithful descendant of proof 18 that has lost track of its own citation and "
              "attached itself to proof 2. That is the characteristic failure mode of a tradition that circulates by "
              "restatement: the argument survives, the provenance does not, and the source it names is right about the "
              "book and wrong about the page. Both the refutation and the steelman above answer Rowbotham's and "
              "Carpenter's versions on the merits, not the fragments &mdash; which is why section 1 concedes the "
              "premise outright and section 6 answers the &ldquo;you have redefined the word&rdquo; reply directly.</p>")),

    verdict_challenge=dict(challenged=False, proposed_verdict=None, reasoning=None),

    people=["PER-ROWBOTHAM", "PER-CARPENTER", "PER-DUBAY", "PER-VOLIVA"],
    related=["B02", "B03", "B04", "B05", "B06", "B09"],

    sources=[
        dict(label="Carpenter, One Hundred Proofs that the Earth Is Not a Globe (1885) — full text; proof 2 (standing water), proof 4 (the Nile), proof 18 (the argument from the word “level”), proof 90",
             url="https://www.gutenberg.org/ebooks/55387"),
        dict(label="Rowbotham (as “Parallax”), Zetetic Astronomy, Earth Not a Globe, 3rd ed. 1881 — ch. II, “Experiments demonstrating the true form of standing water”",
             url="https://sacred-texts.com/earth/za/za05.htm"),
        dict(label="Rowbotham, Zetetic Astronomy / Earth Not a Globe (1865) — full text, searched for “Nile” and river-gradient arguments: not present",
             url="https://archive.org/stream/zeteticastronom00rowbgoog/zeteticastronom00rowbgoog_djvu.txt"),
        dict(label="Rowbotham 1881, General Index — no entry for “Nile” or “Rivers”; “Standing water … 9–62”",
             url="https://sacred-texts.com/earth/za/za68.htm"),
        dict(label="Schadewald, The Plane Truth, ch. 1 — the 1849 pamphlet quoted verbatim, and De Morgan on what happened at the Royal Astronomical Society on 8 December 1848",
             url="https://www.cantab.net/users/michael.behrend/ebooks/PlaneTruth/pages/Chapter_01.html"),
        dict(label="NOAA / National Geodetic Survey, “The Geopotential Surface” — “we define horizontal motion, when there is no change in potential energy”; “water will flow as a function of height difference and/or changes in the gravity field”",
             url="https://geodesy.noaa.gov/research/geopotential-datums/geopotential-surface.shtml"),
        dict(label="Permanent Service for Mean Sea Level, FAQ — “mean sea level is not a ‘level surface’”; geoid–ellipsoid separation up to 100 m; ~20 cm difference across the Panama Canal",
             url="https://psmsl.org/train_and_info/faqs/"),
        dict(label="American Physical Society, “How Newton Derived the Shape of the Earth” — the principle of canals, and the 689:692 / 1-in-230 flattening",
             url="https://www.aps.org/apsnews/2022/10/newton-earth-shape"),
        dict(label="Equatorial bulge — WGS 84 equatorial radius 6,378.137 km against polar 6,356.7523 km; flattening 1/298.257223563",
             url="https://en.wikipedia.org/wiki/Equatorial_bulge"),
        dict(label="Woodward et al., “The River Nile: Evolution and Environment” (Univ. of Manchester) — Khartoum 378 m asl, Aswan 91 m asl, 280 m fall over 1,847 km; ~70 m fall Aswan to Cairo; White Nile Malakal–Khartoum gradient 1:101,000",
             url="https://pure.manchester.ac.uk/ws/files/170946668/Chapter_14_THE_NILE_FINAL.pdf"),
        dict(label="Britannica, Nile — physiography and distances (first cataract to Cairo, about 500 miles)",
             url="https://www.britannica.com/place/Nile-River/Physiography"),
        dict(label="Etymology of “level” — Old French livel, Latin libella “a balance”, diminutive of libra “scales”; originally the name of the instrument",
             url="https://etymology.en-academic.com/21893/level"),
        dict(label="Online Etymology Dictionary, “level” — noun mid-14c. (the tool); “position as marked by a horizontal line” 1530s (as in sea-level); adjective “having an even surface” early 15c.; “lying in the same horizontal plane” 1550s",
             url="https://www.etymonline.com/word/level"),
        dict(label="Rebuttals to Dubay, 200 Proofs — proof 3 (“the natural physics of water is to find and maintain its level”) and proof 5 (the Nile, “a thousand miles with a fall of only one foot”)",
             url="https://flatearth.ws/eric-dubay")]),
}
