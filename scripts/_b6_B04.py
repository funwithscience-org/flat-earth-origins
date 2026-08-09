# -*- coding: utf-8 -*-
"""Batch 6 — B04. Long-range visibility of ships, lighthouses and towers.

Written 2026-08-07. The OPTICAL cluster: things seen at distances a naive
curvature calculation says should be hidden. B01 owns the hydrostatic premise,
B03 owns the Bedford Level trials, B05 owns the engineering "no allowance"
form. This one is about light paths.

Six findings a future session should not have to re-derive.

1. OUR ATTRIBUTION IS WRONG TWICE.
   (a) The cluster credits Rowbotham, Zetetic Astronomy, 1849. The lighthouse
       passage that is the actual ancestor lists "The Port Nicholson Light, in
       New Zealand (erected in 1859)". A text naming an 1859 lighthouse cannot
       be in an 1849 pamphlet. It is also absent from the searchable portion of
       the 1865 first book edition (Gutenberg #69892; Egerö, Dunkerque,
       Cordonan, Madras, Port Nicholson, Bonavista, Poolbeg all return nothing
       through p. 83, which is well past the point where the corresponding
       material sits in the later edition). Earliest text we can document is the
       3rd edition, London: Day, 1881, ch. II, pp. 28-30 — i.e.
       WRK-ROWBOTHAM-1865, whose own record covers the 3rd ed. in its imprint.
   (b) Our basis line says "Carpenter's proofs 5 and 36 (Cape Hatteras,
       Chesapeake Bay) reappear as Dubay's 89 and 96." Half right. Proof 36 IS
       Dubay's 96. Dubay's 89 is the Cape L'Agulhas light, which is nowhere in
       Carpenter. "Cape Hatteras" does not occur in 200 Proofs at all. It
       survives instead in Dubay's 2018 blog post "Enlightenment from
       Lighthouses", quoted verbatim and credited to Carpenter by name.

2. ROWBOTHAM PRINTED THE ANSWER IN HIS OWN BOOK. He reproduces the
   Encyclopaedia Britannica article "Levelling", which tells him (i) that rays
   are "incurvated by refraction" because of "the unequal densities of the air
   at different distances from the earth" — the exact mechanism he denies
   elsewhere; (ii) that refraction "may at a mean compensate for about
   one-seventh of the curvature of the earth" — k ≈ 1/7, which is the modern
   7/6 effective-radius rule; and (iii) that it "sometimes exceeds one-fifth,
   and at other times does not amount to one-fifteenth", which is our
   discriminator, in his own book, in 1865 and again in 1881.

2a. HOW HIS TABLE IS BUILT (get this right; we had it wrong until 2026-08-09).
   Each printed figure is [8 in x (visible distance - observer horizon)^2] MINUS
   the light's own altitude. Table cases use the 10-ft standard eye, i.e. a
   4-mile deduction; the Spurn Point example uses 16 ft and 5 miles; the Poolbeg
   /St George's Channel case uses 24 ft and 6 miles. So Egero: (28-4)^2 x 8 in =
   384 ft, less 154 = 230, which is the figure Dubay's proof 83 reprints.
   Bonavista: (35-4)^2 x 8 in = 641 ft, less 150 = the 491 he prints. The
   curvature term on Bonavista is therefore 641, not 491; a seventh of it is
   ~90 ft and a fifth ~130 ft, against his 13 ft — about sevenfold, not fivefold.

3. HALF THE CLUSTER FAILS BEFORE REFRACTION IS REACHED. The "visible N miles"
   figures in the lighthouse tables are LUMINOUS/NOMINAL ranges out of light
   lists — how far the lamp is bright enough to be seen — not horizon
   distances. Bowditch tells the mariner to compute both and take the lesser.
   Cape Agulhas: real focal plane 102 ft (Dubay says 238), real tower 89 ft
   (Dubay says 33), charted 30 nm nominal against a geographic range of about
   16 nm from a 15 ft eye. Nobody ever observed those lights at those ranges.

4. ROWBOTHAM'S OWN OBSERVATIONS ARE OF VARIABLE VISIBILITY. The Nab light-ship
   from Victoria Pier: from 32 inches above the water, "when it was very calm,
   the greater part of the hull ... was, through a good telescope, plainly
   visible. But on other occasions, when the water was much disturbed, no
   portion of the hull could be seen." And the Eddystone, visible from a 5 ft
   elevation in calm weather while in rough weather even the vane 100 ft up was
   "entirely out of sight." He needs visibility to be invariant. He reports it
   varying, and by 100 feet.

5. THE TELESCOPE CLAIM IS TESTABLE AND FALSE, AND IT IS STILL LIVE. Carpenter's
   proof 63 says a good telescope restores a hull lost to the naked eye. It is
   NOT Carpenter's own: Rowbotham 1881 ch. XIV (za33.htm) has it already, but
   conditioned on a calm sea and a vessel "just" hull down, and says outright
   that on a running sea "a telescope fails to restore it, however powerful it
   may be" because the waves are "magnified and rendered more obstructive by the
   very instrument". Proof 63 drops the condition; that is the hedge_dropped step
   and it is what makes the modern claim checkable. Corrected 2026-08-09; the
   gloss previously said none of Carpenter's four proofs was in Rowbotham. The
   Flat Earth Society wiki still says "a good telescope with sufficient zoom
   will change the observer's perspective and bring the ship's hull back in
   full view." Zoom is a crop; it cannot un-occlude. Raising the eye can, and
   that eye-height dependence is the fingerprint of a sphere.

6. ITEM 381 CANNOT DESCEND FROM ANYONE IN THIS LINEAGE. Rowbotham died in 1884,
   Carpenter published in 1885. The first offshore platform out of sight of
   land was Kerr-McGee's Kermac Rig No. 16, 10 miles off Louisiana, producing
   from 14 November 1947. "Oil rig sightlines" is a modern example fitted to a
   Victorian frame.

Could not reach: an 1880s US Light List entry for Cape Hatteras (to establish
where Carpenter's "40 miles" came from); focal-plane height and charted range
for the Sharps Island screwpile light; Hirt et al. 2010 JGR on measured
refraction-coefficient variability (paywalled, 403).
"""

ENTRY = {

"B04": dict(
    tldr=("Most of these sightings are real, correctly reported, and further than the popular "
          "arithmetic allows — concede all of that, because the arithmetic is wrong twice over. "
          "“8 inches per mile squared” gives the drop from a tangent plane, not what a curve "
          "hides, and it assumes an atmosphere that does not bend light; refraction is a "
          "standing, quantified correction, and the encyclopaedia article Rowbotham reprinted "
          "in his own book gives its mean value as one-seventh of the curvature — the same 7/6 "
          "effective-radius rule surveyors and radio engineers use today. The turn is that the "
          "same article says why no fixed allowance is safe: refraction varies, "
          "“sometimes exceeds one-fifth, and at other times does not amount to one-fifteenth.” "
          "A plane predicts visibility that never changes. Reality gives you a target lifted "
          "one morning and gone the next, and Rowbotham's own light-ship observation is one of "
          "the reports."),

    passage=dict(
        work="WRK-ROWBOTHAM-1865", pd=True,
        locator=("3rd ed., rev. and enl. (London: Day, 1881), ch. II, pp. 28–35 — the lighthouse "
                 "table, the refraction allowance, and the Encyclopædia Britannica “Levelling” "
                 "extract. Not the 1849 pamphlet: see the gloss"),
        quote="""The square of 24, multiplied by 8 inches, shows a declination of 384 feet. The altitude of the lights in Poolbeg Lighthouse is 68 feet; and of the red light on Holyhead Pier, 44 feet. Hence, if the earth were a globe, the former would always be 316 feet and the latter 340 feet below the horizon … The line of sight H, S, would be a tangent touching the horizon at H, and passing more than 300 feet over the top of each lighthouse.

[the table] The Egerö Light, on west point of Island, south coast of Norway, is fitted up with the first order of the dioptric lights, is visible 28 statute miles, and the altitude above high water is 154 feet. The Dunkerque Light, on the south coast of France, is 194 feet high, and is visible 28 statute miles. The Cordonan Light, on the River Gironde, west coast of France, is visible 31 statute miles, and its altitude is 207 feet. The Light at Madras, on the Esplanade, is 132 feet high, and is visible 28 statute miles. The Port Nicholson Light, in New Zealand (erected in 1859), is visible 35 statute miles, the altitude being 420 feet above high water. The Light on Cape Bonavista, Newfoundland, is 150 feet above high water, and is visible 35 statute miles.

Many instances could be given of lights being visible at sea for distances which would be utterly impossible upon a globular surface of 25,000 miles in circumference … The only modification which can be made in the above calculations is the allowance for refraction, which is generally considered by surveyors to amount to one-twelfth the altitude of the object observed. If we make this allowance, it will reduce the various quotients so little that the whole will be substantially the same.

[and, quoted by Rowbotham himself, from the Encyclopædia Britannica, article “Levelling”] We suppose the visual ray to be a straight line, whereas on account of the unequal densities of the air at different distances from the earth, the rays of light are incurvated by refraction. The effect of this is to lessen the difference between the true and apparent levels, but in such an extremely variable and uncertain manner that if any constant or fixed allowance is made for it in formula or tables, it will often lead to a greater error than what it was intended to obviate. For though the refraction may at a mean compensate for about one-seventh of the curvature of the earth, it sometimes exceeds one-fifth, and at other times does not amount to one-fifteenth. We have, therefore, made no allowance for refraction in the foregone formulæ.""",
        gloss="""<p><strong>Our own attribution is wrong, and the text dates itself.</strong> This cluster is credited to Rowbotham's 1849 <em>Zetetic Astronomy</em> &mdash; a sixteen-page pamphlet. The passage above names &ldquo;<em>The Port Nicholson Light, in New Zealand (erected in 1859)</em>.&rdquo; A text that cites an 1859 lighthouse cannot appear in an 1849 publication. Nor is it in the 1865 first book edition so far as we can search it: none of <em>Eger&ouml;</em>, <em>Dunkerque</em>, <em>Cordonan</em>, <em>Madras</em>, <em>Port Nicholson</em>, <em>Bonavista</em> or <em>Poolbeg</em> occurs in the Gutenberg text of 1865 through p. 83, which is past the point where the equivalent material sits in the later edition. The earliest text we can document is the <strong>third edition of 1881</strong>. The lighthouse argument is therefore a mature-Rowbotham addition of the 1860s&ndash;70s, not a founding claim, and our record has it about thirty years early. <em>This is a correction to us, not only to them.</em></p>

<p><strong>What Rowbotham actually does, which is more careful than the item that descends from it.</strong> He does not simply multiply eight inches by the square of the whole distance. He allows for the observer's own height and subtracts the resulting horizon distance first &mdash; &ldquo;<em>Allowing 16 feet for the altitude of the observer &hellip; 5 miles must be taken from the 30 miles, as the distance of the horizon</em>&rdquo; &mdash; and only then squares the remainder. That is the correct geometric procedure, and 16 ft does give a horizon at about 4.9 statute miles. That worked example is the Spurn Point light; in the lighthouse table itself he uses the ten-foot eye he calls the standard and takes off four miles. He converts the light lists' nautical miles into statute miles and says so each time. And he concedes refraction outright, quantifies it, applies it, and shows his working on Cape Bonavista: 150 ft divided by 12 gives &ldquo;<em>13 feet as the amount to be deducted from 491 feet, making instead 478 feet.</em>&rdquo; <strong>Every one of those qualifications is gone from the list item, which reads in full: &ldquo;Lighthouse visibility.&rdquo;</strong></p>

<p><strong>The Britannica extract is the most important thing on the page, and it is his.</strong> Rowbotham reprints it, in both editions, immediately around this material. It tells him the mechanism (&ldquo;the unequal densities of the air at different distances from the earth&rdquo;), the coefficient (&ldquo;at a mean &hellip; about one-seventh of the curvature&rdquo;, which is <em>k</em>&nbsp;&asymp;&nbsp;0.14, the 7/6 effective-Earth-radius rule still in the surveying textbooks), and the variability (&ldquo;sometimes exceeds one-fifth, and at other times does not amount to one-fifteenth&rdquo;). It also explains why the encyclopaedia's own tables omit refraction &mdash; not because it is absent but because a <em>fixed</em> allowance would mislead. Rowbotham reads that as licence to set refraction aside; the passage says the opposite. Elsewhere he goes further and denies the mechanism outright: &ldquo;<em>Refraction can only exist when the line of sight passes from one medium into another of different density.</em>&rdquo; The article he had just typeset says the line of sight <em>does</em> pass continuously through air of different densities. Compare <a href="#ARG-B06">ARG-B06</a>, where the same book supplies the &ldquo;8 inches per mile&rdquo; figure out of the same encyclopaedia entry.</p>

<p><strong>Carpenter's contribution is American and it is first-person.</strong> William Carpenter emigrated to Baltimore and localised the argument. Four of his hundred proofs are in this cluster, and three of the four are his own: the Cape Hatteras figure and the two Chesapeake cases are not located in the third edition of 1881. The fourth he had from Rowbotham. <strong>Proof 5:</strong> &ldquo;<em>The lights which are exhibited in lighthouses are seen by navigators at distances at which, according to the scale of the supposed &lsquo;curvature&rsquo; given by astronomers, they ought to be many hundreds of feet, in some cases, down below the line of sight! For instance: the light at Cape Hatteras is seen at such a distance (40 miles) that, according to theory, it ought to be nine-hundred feet higher above the level of the sea than it absolutely is, in order to be visible!</em>&rdquo; <strong>Proof 36:</strong> &ldquo;<em>If we take a journey down the Chesapeake Bay, by night, we shall see the &lsquo;light&rsquo; exhibited at Sharpe's Island for an hour before the steamer gets to it. We may take up a position on the deck so that the rail of the vessel's side will be in a line with the &lsquo;light&rsquo; &hellip; and we shall find that in the whole journey the light will not vary in the slightest degree in its apparent elevation. But, say that a distance of thirteen miles has been traversed, the astronomers' theory of &lsquo;curvature&rsquo; demands a difference (one way or the other!) &hellip; of 112 feet 8 inches!</em>&rdquo; <strong>Proof 7</strong> is the daytime version, with the far shore's &ldquo;<em>tall trees, towering up, in perspective, over the heads of the &lsquo;hull-down&rsquo; ships</em>&rdquo;. <strong>Proof 63</strong> is the telescope claim: &ldquo;<em>a good telescope will restore to our view this portion of the vessel. Now, since telescopes are not made to enable people to see through a &lsquo;hill of water&rsquo; &hellip;</em>&rdquo; That one is not Carpenter's invention, and the difference between the two versions is the whole of it. Rowbotham had written it in ch. XIV with a condition attached &mdash; &ldquo;<em>even on the sea, when the water is very calm, if a vessel is observed until it is just &lsquo;hull down,&rsquo; a powerful telescope turned upon it will restore the hull to sight</em>&rdquo; &mdash; and he states the contrary case just as plainly, because on a moving sea the waves are &ldquo;<em>magnified and rendered more obstructive by the very instrument</em>&rdquo; and &ldquo;<em>a telescope fails to restore it, however powerful it may be</em>.&rdquo; Carpenter's proof 63 asserts the effect with the condition struck out, and the Flat Earth Society wiki still repeats it in that form. <strong>The hedge dropped at that step is the one that had made the claim survivable</strong>: Rowbotham's version is hard to test, because it holds only on a glassy sea and only at the moment the hull is <em>just</em> lost; Carpenter's is testable on any afternoon, and is tested in section 8 below.</p>

<p><strong>The descent, corrected.</strong> Eric Dubay's <em>200 Proofs</em> (2015) reprints Rowbotham's table almost intact as proofs <strong>82&ndash;86</strong> (Port Nicholson, Eger&ouml;, Madras, Cordonan, Cape Bonavista) and the Poolbeg/Holyhead case as proof <strong>93</strong>; Carpenter's Chesapeake night journey is proof <strong>96</strong>, quoted with attribution. But <strong>Cape Hatteras is not in <em>200 Proofs</em> at all</strong>, and proof <strong>89</strong> &mdash; which our basis line identifies with it &mdash; is the Cape L'Agulhas light, a case with no Victorian ancestor. Carpenter's proof 5 survives instead in Dubay's 2018 post &ldquo;Enlightenment from Lighthouses&rdquo;, quoted verbatim and credited to Carpenter. <strong>So the lighthouse spine of this cluster is Rowbotham's, not Carpenter's; the two Chesapeake cases are Carpenter's, not Rowbotham's; and one of the two links our own record asserts does not exist.</strong></p>""" ),

    steelman=dict(
        description="""<p><strong>SURFACE (weak &mdash; and a knowledgeable defender will punish it).</strong> &ldquo;Refraction explains it, next.&rdquo; Said bare, this is the single worst move available, for three reasons. It sounds like a parameter tuned after the fact to whatever the observation needs; it is not even the right answer for most of the lighthouse items, which fail for a different reason entirely; and it concedes by implication that the naive calculation was sound and only needed a nudge. It was not sound. Anyone who opens with &ldquo;refraction&rdquo; has agreed to defend the weakest version of their own case.</p>

<p><strong>DEEPER (true, incomplete).</strong> &ldquo;The observations are real; your calculator is wrong.&rdquo; Correct, and it has to be said out loud: <strong>the &ldquo;8 inches per mile squared&rdquo; figure that dominates this debate is wrong as it is almost always used.</strong> It computes the drop of the sphere below the plane tangent at the observer &mdash; <em>&ldquo;the drop x is not what is hidden by the curvature of the earth!&rdquo;</em> &mdash; and it is only a hidden-height figure when the observer's eye is exactly at the surface. Raise the eye and the correct quantity is the drop over the distance <em>beyond your own horizon</em>, which is much smaller. Popular online curvature calculators routinely report the first number, default to zero refraction, and consequently predict that targets are hidden which are in fact seen every clear day. Flat-earthers who run those calculators are getting an honest answer to the wrong sum. But this stated alone still invites the reply that we are just moving the goalposts to wherever the target happens to be.</p>

<p><strong>KERNEL &mdash; refraction is not a rescue, it is a standing correction with a published coefficient, and the source printed the coefficient himself.</strong> The mean value of terrestrial refraction is not a free parameter. Andrew Young states the standard case flatly: the radius of curvature of a near-horizontal ray is about seven times the Earth's, so the geometry is handled by an effective radius <em>R&prime;&nbsp;=&nbsp;R&nbsp;&times;&nbsp;7/6</em>. Surveyors use <em>k</em>&nbsp;&asymp;&nbsp;0.13&ndash;0.14 and radio-path engineering uses <em>k</em>&nbsp;=&nbsp;4/3 for the same reason and by the same construction. It is written into navigation: Bowditch's geographic-range figures are 1.17&radic;<em>h</em> nautical miles rather than the geometric 1.06&radic;<em>h</em>, so about ten per cent of refraction is inside the table before a mariner touches it, and a 150-foot light is tabulated at 14.3 nm rather than 13.0. <strong>And the <em>Encyclop&aelig;dia Britannica</em> article Rowbotham reprints in his own chapter gives the same number in 1860s language</strong> &mdash; refraction &ldquo;at a mean compensate[s] for about one-seventh of the curvature of the earth.&rdquo; One-seventh <em>is</em> the 7/6 rule. The movement's founding text contains, verbatim, the correction its own argument omits, together with the mechanism (&ldquo;the unequal densities of the air at different distances from the earth&rdquo;). So the honest position, which we should state before we say anything else: <strong>many of these sightings are real, are correctly reported, and are exactly what a globe with an atmosphere predicts.</strong> That is why the verdict is MISLEADING and not REFUTED. The observations are usually sound. It is the inference that fails.</p>

<p><strong>And one more piece of ground that belongs to them.</strong> Rowbotham's account of the ship's hull is not &ldquo;perspective&rdquo; hand-waving; he proposes a physical mechanism &mdash; &ldquo;<em>the natural result of the law of perspective operating on a plane surface, but modified by the mobility of the water</em>&rdquo; &mdash; and at the eye heights he used, two or three feet above a choppy surface, <em>waves really do occlude low targets</em>. He is right that a rough sea hides things a calm sea shows. He simply never asks what happens to that mechanism when the eye is 30 metres up and the sea is glass.</p>""",

        why_it_doesnt_save_claim="""<p><strong>Because the same article that supplies the coefficient supplies the discriminator, in the same sentence.</strong> Refraction &ldquo;sometimes exceeds one-fifth, and at other times does not amount to one-fifteenth&rdquo; &mdash; a factor of three either side of the mean, stated in the 1860s, and confirmed by modern measurement: over Rainy Lake the refraction coefficient was measured running from about <em>k</em>&nbsp;=&nbsp;0.19 to <em>k</em>&nbsp;=&nbsp;0.41 across observing sessions, lifting a target 5.4 km away by about half a metre and one 9.5 km away by about a metre. A flat plane predicts visibility limited only by luminous intensity and atmospheric extinction: monotonic, and independent of the temperature profile. What is actually observed is a target lifted into view one morning and hidden the next, over the same water, at the same distance, from the same eye. <strong>Variability is not a defect in the globe answer. It is the observable the flat model cannot generate at all.</strong></p>

<p><strong>Because half these numbers were never horizon distances.</strong> The lighthouse tables are catalogue figures, not sightings. A light list's stated range is a <em>nominal</em> or <em>luminous</em> range &mdash; how far the lamp is bright enough to be seen in stated visibility &mdash; and the mariner is instructed to compute the geographic range separately and take the lesser. Cape Agulhas, Dubay's proof 89: the tower is 27 m (89 ft) and the focal plane 31 m (102 ft) above high water, not the &ldquo;33 feet high, 238 feet above sea level&rdquo; the proof asserts, and its charted 30 nautical miles is a luminous range against a geographic range of about 16 nm from a fifteen-foot eye. Nobody has ever stood on a deck and seen that light at fifty miles. The argument is not fighting refraction here; it is comparing a candela figure with a geometry figure and reporting the difference as curvature.</p>

<p><strong>Because the tables are height-dependent in exactly the way a sphere requires and a plane forbids.</strong> Every geographic-range table in every light list is a function of two heights &mdash; the light's and the observer's eye &mdash; added together as square roots. On a plane the observer's eye height would have no bearing whatever on whether a distant light is visible; only its brightness and the air's clarity would. Eye-height dependence is the fingerprint, it is tabulated, and mariners use it every night.</p>

<p><strong>Because waves do not explain the observation Rowbotham himself reported.</strong> He records the Eddystone light seen from five feet above the water in calm weather, while in rough weather at the same place the vane <em>one hundred feet</em> above the foundation was &ldquo;entirely out of sight.&rdquo; No sea state occludes a hundred feet. And the Nab light-ship from Victoria Pier: from 32 inches up, &ldquo;when it was very calm, the greater part of the hull &hellip; was, through a good telescope, plainly visible. But on other occasions, when the water was much disturbed, no portion of the hull could be seen.&rdquo; He needs long-range visibility to be a stable property of a flat surface. His own field notes record it changing with the day.</p>"""),

    refutation="""<p><strong>1. Concede the arithmetic first, because the arithmetic really is wrong.</strong> The figure that runs this whole debate &mdash; 8 inches per mile squared &mdash; is a correct number for the wrong quantity. Taking <em>R</em>&nbsp;=&nbsp;6,371&nbsp;km, one statute mile of horizontal run puts the surface 0.203&nbsp;m, or 8.00&nbsp;inches, below the plane tangent at the observer. That is <em>drop from a tangent plane</em>. It is not how much of a distant object is hidden, and it becomes that only if the observer's eye is on the surface. Lift the eye and the hidden height is the drop measured over the distance <em>past your own horizon</em>: with the eye at height <em>h</em> feet the horizon lies about 1.22&radic;<em>h</em> statute miles away, and only the excess beyond that is squared. Rowbotham knew this and did it correctly &mdash; four miles off each distance in the lighthouse table, five in the Spurn Point example where he allows sixteen feet of eye height, and only then square. The modern meme usually does not, and neither do most of the calculators circulating with it. <strong>Before refraction is mentioned at all, the popular version of the globe prediction is an overstatement, and the people running it against real sightings are getting a true answer to a false sum.</strong></p>

<p><strong>2. Then add the correction that is not optional and not ad hoc.</strong> Air is denser near the ground, so a near-horizontal ray bends downward continuously; its radius of curvature is roughly seven times the Earth's, and the standard device is to keep the ray straight and inflate the planet: an <em>effective</em> radius <em>R&prime;</em>&nbsp;=&nbsp;<em>R</em>/(1&nbsp;&minus;&nbsp;<em>k</em>), with the geodetic standard <em>k</em>&nbsp;&asymp;&nbsp;0.13&ndash;0.14 giving the familiar <strong>7/6 rule</strong>. Radio-path engineering uses the same construction with <em>k</em>&nbsp;=&nbsp;4/3, which is why ITU-R P.530 has designers draw straight lines over a 4/3-radius Earth. Under mean refraction the 8-inch figure becomes about <strong>6.9 inches per mile squared</strong>. This is not a correction invented for flat-earthers; it predates the dispute, it is used by people with no stake in it, and it is derived from a measurable temperature profile rather than fitted to the observation it is meant to save. See <a href="#ARG-B07">ARG-B07</a>, which is the cluster asserting that refraction is invoked ad hoc.</p>

<p><strong>3. The source contains the correction. This is the finding.</strong> Rowbotham reprints the <em>Encyclop&aelig;dia Britannica</em> article &ldquo;Levelling&rdquo; in the same chapter as his lighthouse table. It states the mechanism &mdash; &ldquo;<em>on account of the unequal densities of the air at different distances from the earth, the rays of light are incurvated by refraction</em>&rdquo; &mdash; and then the number: &ldquo;<em>the refraction may at a mean compensate for about one-seventh of the curvature of the earth.</em>&rdquo; One-seventh is <em>k</em>&nbsp;=&nbsp;0.143, which is the 7/6 rule to three digits. The Victorian encyclopaedia and the modern surveying textbook agree, and the agreement is printed inside the book being cited against them. Rowbotham's own substitute &mdash; &ldquo;<em>one-twelfth the altitude of the object observed</em>&rdquo; &mdash; is the wrong quantity in the wrong place: refraction scales with the square of the <em>distance</em>, not with the height of the target, so on Cape Bonavista he deducts 13 feet from a curvature term of about <strong>641 feet</strong>. The 491 he prints there is not the curvature term itself; it is that term less the light's own 150 feet, which is how every row of his table is built. The Poolbeg case quoted above shows the construction in his own words: a declination of 384 feet, less lights of 68 and 44 feet, gives the 316 and 340 he reports. Eger&ouml; is the check on the table proper &mdash; 28 statute miles less the four-mile horizon of the ten-foot eye he calls the standard is 24; 24&sup2; &times; 8 inches is 384 feet; 384 less the light's 154 feet is the 230 feet of depression that comes down intact to Dubay's proof 83. Bonavista runs the same way: 35 miles less four is 31, and 31&sup2; &times; 8 inches is 641 feet. So the encyclopaedia's own mean would take about a seventh of 641, some 90 feet, and a strong-refraction day nearer 130. That correction does not rescue the sighting either &mdash; we will come to why &mdash; but the allowance he made was about seven times too small and applied to the wrong variable.</p>

<p><strong>4. Navigation has all of this built in, and has for two centuries.</strong> Bowditch tabulates a light's <em>geographic</em> range as the sum of two horizon distances, the observer's and the light's, at 1.17&radic;<em>h</em> nautical miles for <em>h</em> in feet: 150 ft of light gives 14.3&nbsp;nm, a 5-foot eye adds 2.6, a 30-foot eye 6.4, a 70-foot eye 9.8. The purely geometric coefficient is 1.06, so roughly a tenth of the tabulated distance <em>is</em> refraction, standing, unremarked, in a table printed for people who need to make landfall. Bowditch also states the limit of the method in the same breath: &ldquo;<em>Abnormal refraction patterns might change this range; therefore, one cannot exactly predict the range at which a light will be seen.</em>&rdquo; That is a sphere-plus-atmosphere model telling you honestly which part of its prediction is soft.</p>

<p><strong>5. But most of the lighthouse items never reach the refraction question, because the numbers are not sightings.</strong> This is the part of the cluster that fails first, and it fails on definitions. A light list quotes a <strong>nominal range</strong> &mdash; the distance at which the lamp would be seen if meteorological visibility were 10 nautical miles &mdash; or a <strong>luminous range</strong>, its equivalent in the actual weather. Both are functions of candela and air clarity and have nothing to do with the horizon. The <strong>geographic range</strong> is the horizon-limited figure. The mariner computes both and uses the smaller, and the US Coast Guard <em>Light List</em> adds the loose end explicitly: &ldquo;<em>The &lsquo;loom&rsquo; (glow) of a powerful light is often seen beyond the limit of visibility of the actual rays of the light.</em>&rdquo; Now take the two named cases.</p>
<ul>
<li><strong>Cape Agulhas</strong> &mdash; Dubay's proof 89, &ldquo;33 feet high, 238 feet above sea level, and can be seen for over 50 miles.&rdquo; The tower is 27&nbsp;m (89&nbsp;ft); the focal plane is 31&nbsp;m (102&nbsp;ft) above high water; the charted range is 30 nautical miles, which is 56&nbsp;km, which is 35 statute miles. All three of the proof's numbers are wrong, and the geographic range from a fifteen-foot eye is about <strong>16&nbsp;nm</strong>, so the charted 30 is plainly a luminous figure. It is worth noting how the error may have arisen: &ldquo;56&nbsp;km&rdquo; read as miles is &ldquo;over 50 miles.&rdquo; We cannot prove that is what happened, but the claim is fifty per cent adrift from any published figure.</li>
<li><strong>Cape Hatteras</strong> &mdash; Carpenter's proof 5, &ldquo;seen at such a distance (40 miles).&rdquo; The National Park Service gives the focal height as 192.2&nbsp;ft, an official range of <strong>24 nautical miles</strong>, and a practical figure of &ldquo;up to 20 nautical miles at sea&rdquo; for most vessels in clear weather. Twenty nautical miles is 23 statute miles, and the geographic range for a 192-foot light and a fifteen-foot eye works out at <strong>20.7&nbsp;nm</strong>. In other words the range mariners actually get from that light is the range a sphere with a refracting atmosphere predicts, to within a few per cent. Carpenter's 40 miles is not a published figure then or now; we could not locate an 1880s Light List to trace where he got it.</li>
</ul>
<p>His &ldquo;nine-hundred feet&rdquo; then follows mechanically: 8&nbsp;in&nbsp;&times;&nbsp;40&sup2; is 1,067 feet, less the 191-foot light, gives 876. It is the naive drop-from-tangent sum, computed from a zero-height eye, on a distance twice the real one.</p>

<p><strong>6. What the light lists prove, if you read them the other way.</strong> Every geographic-range table is indexed by two heights and adds their square roots. On a plane, the height of the observer's eye could not matter: a light would be visible until it was too dim or the air too thick, and standing on a box would do nothing. The tables are built the way they are because raising the eye moves the horizon, and moving the horizon uncovers the target. That is the fingerprint, and it is not subtle &mdash; it is the difference between a 2.6&nbsp;nm and a 9.8&nbsp;nm contribution for the same light seen from a dinghy and a bridge wing.</p>

<p><strong>7. Refraction's variability is the discriminating observation, and it is enormous.</strong> The atmosphere does not merely add a fixed 15 per cent to the horizon. Depending on the vertical temperature gradient it produces a whole taxonomy, all of it standard optics and none of it available to a plane:</p>
<ul>
<li><strong>Looming</strong> &mdash; a thermal inversion steepens the density gradient, the ray bends harder, and objects normally below the horizon are lifted into view. This is the flat-earther's favourite photograph, and it is a named, modelled, predicted phenomenon.</li>
<li><strong>Sinking</strong> &mdash; a steep lapse rate does the reverse: targets ordinarily visible drop out of sight. <em>A plane has no mechanism for this at all.</em> If the surface were flat and visibility were limited by extinction, nothing that was visible yesterday could be hidden today in clearer air.</li>
<li><strong>Towering and stooping</strong> &mdash; vertical stretching and compression of the image, from curvature in the temperature profile. The Chicago skyline photographed across Lake Michigan shows both: the narrow section of the Willis Tower below the spires is visibly stretched, which is why the picture looks wrong rather than merely distant.</li>
<li><strong>Ducting</strong> &mdash; when the gradient reaches <em>k</em>&nbsp;=&nbsp;1 the ray curves with the Earth and the surface behaves optically as though it were flat; stronger still and rays are trapped and guided round the curve. This is the regime in which the record-breaking sightings occur, and it is transient, local and measurable.</li>
<li><strong>Inferior mirage and the Fata Morgana</strong> &mdash; inverted images below or above the erect one, and the multiple alternately erect and inverted strips of the Fata Morgana. Under inferior-mirage conditions the apparent horizon can pull in to about <strong>4&nbsp;km</strong> against a standard 13&ndash;14&nbsp;km. The horizon itself moves.</li>
</ul>
<p>The numbers are real and they are measured, not assumed. Across Rainy Lake, targets 0.37&ndash;1.6&nbsp;m above the water at 1.1&ndash;9.5&nbsp;km were surveyed against GNSS-fixed positions and returned refraction coefficients from about 0.19 to 0.41 between sessions, with apparent lifts of roughly 0.5&nbsp;m at 5.4&nbsp;km and 1&nbsp;m at 9.5&nbsp;km. And even generous refraction does not flatten the world: from Grand Mere State Park, 56.5 statute miles from the Willis Tower, the hidden height is 453&nbsp;m with no refraction, 404&nbsp;m at 10 per cent and 364&nbsp;m at 20 per cent &mdash; so on the best day most of a 442-metre building is still gone, which is precisely what the photographs show. <strong>The claim needs the sightings to be routine and stable. They are episodic and correlated with the weather, and the correlation is the thing being explained.</strong></p>

<p><strong>8. Hull-down is the discriminator on ships, and Carpenter made it testable.</strong> A ship going away does not shrink uniformly to a point: it is occluded from the waterline upward, the hull first, then the deck, then the funnel, with a hard edge at the horizon and full angular size retained in what remains. That is occlusion, not resolution. Carpenter's proof 63 makes the opposing prediction explicit &mdash; &ldquo;<em>a good telescope will restore to our view this portion of the vessel</em>&rdquo; &mdash; and the Flat Earth Society wiki still asserts it today: &ldquo;a good telescope with sufficient zoom will change the observer's perspective and bring the ship's hull back in full view.&rdquo; <strong>It is a falsifiable claim and it is false.</strong> Zooming is cropping and magnifying; it cannot recover an object that is geometrically behind the surface. The controlled version of the test is trivial: photograph a distant vessel, zoom by a factor of two, photograph again, then enlarge the first frame by two and compare the gap between the waterline and the horizon. The gap is unchanged. What <em>does</em> restore the hull is raising the camera, and the amount restored is the amount the horizon-shift predicts. Rowbotham's own alternative &mdash; that a rough sea occludes the hull &mdash; is a real effect at his 32-inch eye height and useless at 30 metres, where the hulls still vanish on a glassy sea.</p>

<p><strong>9. The two Chesapeake proofs, on their own terms.</strong> Proof 7's daytime observation &mdash; tall trees on the far shore visible over the heads of hull-down ships &mdash; is real and is exactly what a sphere gives you, because hidden height depends on the target's distance and the observer's eye, and tall things far away can clear what short things nearer cannot. Numerically: from a 2-metre deck the horizon is about 5.5&nbsp;km; a ship at 12&nbsp;km loses about 2.9&nbsp;m at the waterline, enough for a laden hull, while a treeline at 20&nbsp;km loses about 14&nbsp;m, so a 30-metre tree still shows fifteen metres of itself. The observation discriminates nothing; it merely feels paradoxical. Proof 36 is weaker still. Carpenter sights the light along &ldquo;the rail of the vessel's side&rdquo; &mdash; a bulwark on a hull that pitches, rolls, trims and settles as the coal burns off, which is not a levelling instrument by any definition &mdash; and demands a change in apparent elevation &ldquo;<em>one way or the other!</em>&rdquo;, which concedes that he does not know what the theory he is refuting predicts. It predicts one direction: approaching a light, it rises relative to the horizon. And his opening sentence gives the case away. &ldquo;<em>We shall see the light &hellip; for an hour before the steamer gets to it</em>&rdquo; describes a light that <em>comes into view at a finite range</em>. On a plane, why would it ever not have been in view?</p>

<p><strong>10. Why this is MISLEADING and not REFUTED, which matters.</strong> Most of the sightings in this cluster happened. Oil platforms are seen from beaches that a bad calculator says should hide them; skylines do appear across lakes; ships are visible past the naive horizon. We are not disputing the reports, and a page that did would deserve to lose. What fails is the step from the report to the conclusion, and it fails at three separate joints: the arithmetic computes the wrong quantity, the atmosphere is omitted from a calculation that navigation and surveying have included since before the dispute began, and half the numbers cited are luminous ranges out of a catalogue rather than observations of anything. <strong>A true observation, correctly reported, married to an inference the observation does not license &mdash; that is what MISLEADING names, and it is the right verdict here.</strong></p>

<p><strong>11. Scope.</strong> This cluster is the optical claim. The hydrostatic premise &mdash; what &ldquo;level&rdquo; means and what shape a free water surface takes &mdash; is <a href="#ARG-B01">ARG-B01</a>, and it deliberately rests on gravimetry and tide gauges rather than sight lines for exactly this reason. The Old Bedford Level trials, including Lady Blount's 1904 repeat, belong to <a href="#ARG-B03">ARG-B03</a>; we note only that Blount's own photographer, Edgar Clifton of Dallmeyer's, working from two feet above the water, recorded &ldquo;an aqueous shimmering vapour&rdquo; floating &ldquo;unevenly on the surface of the canal and adjoining fields&rdquo;, and that he and Blount reported seeing the target <em>and its reflection</em> &mdash; two images, which is the signature of a mirage and not of a plane. The engineering &ldquo;no curvature allowance&rdquo; form is <a href="#ARG-B05">ARG-B05</a>; the horizon's flatness and dip is <a href="#ARG-B02">ARG-B02</a>; the charge that refraction is an ad hoc rescue is <a href="#ARG-B07">ARG-B07</a>. And <a href="#ARG-B13">ARG-B13</a> is where the list contradicts itself: it carries &ldquo;Harbor mirage charts.&rdquo; as its own item while carrying &ldquo;Harbor lights flat lines.&rdquo; here. Conceding an atmospheric optical mechanism in one item and denying it in the next is not two arguments. It is one argument and its refutation, filed under different numbers.</p>""",

    advocate=dict(
        survives=4,
        best_defense=(
            "Notice how much you just gave away. You concede the observations are real, you "
            "concede the standard formula is wrong, you concede the calculators mispredict, and "
            "then you produce a coefficient — k, 7/6, 4/3, take your pick — that you are free to "
            "tune between 0.13 and 1 and beyond, and announce the discrepancy closed. That is not "
            "a prediction, it is a spare parameter, and you have admitted its range spans the "
            "entire distance between 'the Earth curves' and 'the Earth is optically flat.' At "
            "k = 1, by your own account, light follows the surface and the world behaves exactly "
            "as I say it is. You have a model with a knob on it that can be set to reproduce "
            "flatness, and you call the knob a confirmation. Second, you lean on 'variability' as "
            "your discriminator, but variability is what an honest observer calls not knowing. "
            "Rowbotham reported the Nab light-ship coming and going and gave a mechanism — the "
            "state of the water surface. You have relabelled his mechanism 'refraction' and "
            "claimed the relabelling as a victory. Third, and worst for you: your own light lists "
            "publish ranges that exceed your geographic limit, and you resolve that by declaring "
            "the numbers to be about candela rather than geometry. Convenient. When my figure "
            "exceeds your prediction it is 'nominal'; when it falls short it is 'geographic'; "
            "when it does neither it is 'abnormal refraction.' Name in advance one observation "
            "of a light or a ship that your model forbids, and that I could go and make."),
        preemptive=(
            "Rated 4. The 'spare parameter' charge is the reply this page will actually receive "
            "and it must be answered in the body, not left to the reader. Three concrete changes, "
            "and the first two are already drafted above and must not be cut. (a) Section 7 has "
            "to keep the *measured* refraction numbers rather than the textbook ones — the Rainy "
            "Lake k = 0.19-0.41 range, and the Chicago hidden-height figures at 0%, 10% and 20% "
            "showing that even generous refraction leaves most of a 442 m building hidden. k is "
            "measured against surveyed GNSS positions, not fitted to save an appearance, and the "
            "honest statement is that no value of k in the observed range flattens the Earth for "
            "these targets. (b) Section 5 has to carry the *definitions* of nominal, luminous and "
            "geographic range with the citation, because otherwise 'that number is nominal' does "
            "read as special pleading — the distinction is printed in Bowditch and in the Coast "
            "Guard Light List, it predates the argument, and it is used by people making landfall "
            "in the dark. (c) ADD, because it is the one thing that answers the closing demand "
            "and the page does not yet do it as a numbered item: a falsification list. Our model "
            "forbids, and a flat plane permits: a ship's hull recovered by magnification at fixed "
            "eye height (test it in an afternoon, and Carpenter's proof 63 asserts it); a light "
            "whose visible range is independent of the observer's eye height; a target that "
            "sinks, or stretches, or doubles into an inverted image without any temperature "
            "structure to produce it; and a distant object occluded from the top down rather than "
            "the bottom up. Every one is cheap to attempt and none has ever come in. Do not "
            "answer 'name a forbidden observation' with a paragraph of theory. Answer it with "
            "four experiments. Finally, on the relabelling charge: concede in the text that "
            "Rowbotham's wave mechanism is real at 32 inches of eye height, and then hold him to "
            "his own Eddystone datum, where the vane 100 feet up went out of sight. No sea state "
            "occludes a hundred feet; his mechanism is under-powered by his own observation, and "
            "that is why the relabelling is not a relabelling.")),

    straw_man=dict(
        identified=True,
        detail=("The cluster's central misrepresentation is that astronomers predict a light's "
                "charted range from curvature alone. Nobody does. The mainstream position is that "
                "a light's visible range is the LESSER of its luminous range, fixed by candela and "
                "meteorological visibility, and its geographic range, fixed by two heights of eye "
                "and standard refraction — a position printed in the light lists Rowbotham was "
                "reading the numbers out of. Carpenter's proof 5 takes catalogue ranges, treats "
                "every one of them as a horizon distance, and reports the mismatch as a scandal. "
                "The second misrepresentation is Carpenter's proof 63, which attributes to the "
                "other side the claim that a hull is hidden behind a 'hill of water' one might see "
                "through with better glass. Nobody claims refraction or magnification defeats "
                "occlusion; the mainstream claim is that the hull is geometrically behind the "
                "surface, which is why raising the eye recovers it and zoom does not. Attacking "
                "the 'hill of water' is attacking a phrase Carpenter supplied himself. Third, and "
                "smaller: proof 36's demand for a change in apparent elevation 'one way or the "
                "other!' imputes to the theory an indeterminate prediction. The prediction is "
                "determinate — a light rises relative to the horizon as you close on it — and the "
                "reference used to test it, a ship's rail, is not a level.")),

    compression=dict(
        assessed=True, drifted=True,
        list_phrasing=("Repeated long-range visibility. (222)  /  Tower sight lines beyond curve. (260)  /  "
                       "Harbor lights flat lines. (378)  /  Lighthouse visibility. (379)  /  "
                       "Oil rig sightlines. (381)  /  Ship optical range. (401)"),
        source_wording=("&ldquo;<em>Allowing 16 feet for the altitude of the observer &hellip; 5 miles must be taken "
                        "from the 30 miles, as the distance of the horizon</em>&rdquo; &hellip; &ldquo;<em>The only "
                        "modification which can be made in the above calculations is the allowance for refraction, "
                        "which is generally considered by surveyors to amount to one-twelfth the altitude of the "
                        "object observed</em>&rdquo; &hellip; and, quoted by Rowbotham himself from the "
                        "<em>Encyclop&aelig;dia Britannica</em>: &ldquo;<em>the rays of light are incurvated by "
                        "refraction &hellip; though the refraction may at a mean compensate for about one-seventh of "
                        "the curvature of the earth, it sometimes exceeds one-fifth, and at other times does not "
                        "amount to one-fifteenth</em>.&rdquo;"),
        drift_type="hedge_dropped",
        note=("<p><strong>The dominant drift is hedge_dropped, and this is one of the starkest cases on the page: "
              "the source shows its working and the list keeps two words of it.</strong> Item 379 reads, in full, "
              "&ldquo;Lighthouse visibility.&rdquo; The passage it descends from allows for the observer's own "
              "height and subtracts the resulting horizon before squaring &mdash; four miles in the table, five in "
              "the Spurn Point example where he allows sixteen feet of eye &mdash; converts the light "
              "lists' nautical miles into statute miles and says so each time, concedes an allowance for refraction, "
              "quantifies it, applies it, and prints the worked deduction on Cape Bonavista. Every qualification "
              "Rowbotham made survives into none of the six items. This matters more than usual because the "
              "qualifications are where he can be answered: his refraction allowance is the wrong quantity applied "
              "to the wrong variable &mdash; a twelfth of the <em>target's height</em> rather than about a seventh "
              "of the <em>curvature term</em> &mdash; and you cannot show that against a fragment reading "
              "&ldquo;Lighthouse visibility.&rdquo; The refutation above is therefore aimed at his arithmetic, not "
              "at the fragment.</p>"
              "<p><strong>The hedge that was dropped is the one that answers the argument.</strong> The strongest "
              "sentence in this whole cluster is not ours; it is the <em>Encyclop&aelig;dia Britannica</em> extract "
              "Rowbotham typeset into his own chapter, which supplies the mechanism, the mean coefficient (one "
              "seventh of the curvature, i.e. the modern 7/6 rule) and the variability (&ldquo;sometimes exceeds "
              "one-fifth &hellip; at other times does not amount to one-fifteenth&rdquo;). The list carries none of "
              "it, and neither does any modern restatement we found. The tradition dropped a hedge that was already "
              "printed on its own founding page.</p>"
              "<p><strong>A second hedge went the same way, and it is the cleanest specimen in the cluster.</strong> "
              "Rowbotham's telescope claim is conditional: a powerful glass restores the hull &ldquo;<em>when the "
              "water is very calm</em>&rdquo; and the vessel is <em>just</em> hull down, while on a running sea "
              "&ldquo;<em>a telescope fails to restore it, however powerful it may be</em>&rdquo;. Carpenter's "
              "proof 63 states the effect with no condition at all, and the Flat Earth Society wiki carries it "
              "forward in that unconditional form. The condition was the part that made the claim hard to check; "
              "removing it is what turned a hedged observation into a falsifiable one, and it is now false.</p>"
              "<p><strong>Item 381 is a different drift and a harder finding: unsourced_addition, and specifically an "
              "anachronism.</strong> &ldquo;Oil rig sightlines.&rdquo; cannot descend from the credited source. "
              "Rowbotham died in 1884; Carpenter published in 1885; the first offshore platform standing out of "
              "sight of land was Kerr-McGee's Kermac Rig No. 16, ten miles off Louisiana, in production from "
              "14 November 1947. It is a twentieth-century example fitted to a Victorian frame, exactly as the "
              "microwave and wind-farm items are in <a href=\"#ARG-B05\">ARG-B05</a>. Items 222, 260, 378 and 401 "
              "sit between the two cases: they are bare generalisations (&ldquo;Repeated long-range "
              "visibility.&rdquo;) of arguments the sources make about named, dated, checkable instances, which is "
              "scope_widened in effect &mdash; a claim about the Eger&ouml; light and the Chesapeake steamer "
              "restated as a claim about long-range visibility in general, with the instances that could be "
              "falsified removed.</p>"
              "<p><strong>And our own record drifted too.</strong> The cluster credits the whole cluster to "
              "Rowbotham's 1849 pamphlet; the ancestral passage names a lighthouse built in 1859. Our basis line "
              "says Carpenter's Cape Hatteras proof reappears as Dubay's proof 89; Dubay's 89 is the Cape L'Agulhas "
              "light and &ldquo;Cape Hatteras&rdquo; does not occur in <em>200 Proofs</em> at all. Both corrections "
              "are set out in the gloss. On a page about provenance, an error in our own genealogy is the same "
              "class of failure we are documenting, and it is published rather than quietly fixed.</p>")),

    verdict_challenge=dict(challenged=False, proposed_verdict=None, reasoning=None),

    people=["PER-ROWBOTHAM", "PER-CARPENTER", "PER-DUBAY", "PER-VOLIVA"],
    related=["B01", "B02", "B03", "B05", "B06", "B07", "B13", "B14"],

    sources=[
        dict(label="Rowbotham (as “Parallax”), Zetetic Astronomy: Earth Not a Globe, 3rd ed. 1881 — ch. II: the lighthouse table (Egerö, Dunkerque, Cordonan, Madras, Port Nicholson “erected in 1859”, Cape Bonavista), the “one-twelfth” refraction allowance, and the Encyclopædia Britannica “Levelling” extract",
             url="https://sacred-texts.com/earth/za/za14.htm"),
        dict(label="Rowbotham 1881, ch. XIV — hull disappearance as “perspective … modified by the mobility of the water”; the Eddystone light from five feet; the Nab light-ship seen from 32 inches at Victoria Pier, Portsmouth",
             url="https://sacred-texts.com/earth/za/za33.htm"),
        dict(label="Rowbotham 1881, General Index — “Eddystone light visible for 14 miles”, “Cause of ship's hull disappearing before the masthead”, “Refraction can only exist where the line of sight passes from one medium into another”",
             url="https://sacred-texts.com/earth/za/za68.htm"),
        dict(label="Rowbotham, Zetetic Astronomy: Earth Not a Globe! (1865), Gutenberg #69892 — searched for the lighthouse names: Egerö, Dunkerque, Cordonan, Madras, Port Nicholson, Bonavista, Poolbeg all absent through p. 83; “incurvated by refraction” present",
             url="https://www.gutenberg.org/ebooks/69892"),
        dict(label="Carpenter, One Hundred Proofs that the Earth Is Not a Globe (Baltimore, 1885) — proof 5 (Cape Hatteras), proof 7 (Chesapeake by day, “hull down”), proof 36 (Chesapeake by night, Sharpe's Island), proof 63 (the telescope)",
             url="https://www.gutenberg.org/ebooks/55387"),
        dict(label="Rebuttals to Dubay, 200 Proofs — proofs 82–86 and 93 are Rowbotham's lighthouse table; proof 89 is Cape L'Agulhas; proof 96 is Carpenter's proof 36. “Cape Hatteras” does not appear",
             url="https://flatearth.ws/eric-dubay"),
        dict(label="Dubay, “Enlightenment from Lighthouses” (2018) — where Carpenter's Cape Hatteras sentence actually survives, quoted verbatim and credited to Carpenter",
             url="https://ericdubay.wordpress.com/2018/07/11/enlightenment-from-lighthouses/"),
        dict(label="Bowditch, American Practical Navigator, ch. 4 §§406–407 — nominal, luminous and geographic range; geographic range as the sum of two horizon distances (150 ft → 14.3 nm; 5 ft → 2.6; 30 ft → 6.4; 70 ft → 9.8); “abnormal refraction patterns might change this range”",
             url="https://en.wikisource.org/wiki/The_American_Practical_Navigator/Chapter_4"),
        dict(label="US Coast Guard Light List — geographic range table for an observer at sea level, with the observer's own height added; “Atmospheric refraction may cause a light to be seen farther than under ordinary circumstances”; “The ‘loom’ (glow) of a powerful light is often seen beyond the limit of visibility of the actual rays”",
             url="https://www.navcen.uscg.gov/sites/default/files/pdf/msi/LightList_V3_2024.pdf"),
        dict(label="Andrew T. Young (SDSU), “The Horizon” — the ray's radius of curvature is about 7× the Earth's; effective radius R′ = R × 7/6; horizon 3.86√h km against 3.57 geometric; refraction “is particularly variable over water”",
             url="https://aty.sdsu.edu/explain/atmos_refr/horizon.html"),
        dict(label="Andrew T. Young (SDSU), “Looming, Towering, Stooping, and Sinking” — definitions and the temperature profiles that produce each",
             url="https://aty.sdsu.edu/mirages/mirsims/loom/loom.html"),
        dict(label="Andrew T. Young (SDSU), “An Introduction to Mirages” — ducts guiding rays around the curve; Fata Morgana; the apparent horizon pulling in to ~4 km under inferior-mirage conditions against 13–14 km standard",
             url="https://aty.sdsu.edu/mirages/mirintro.html"),
        dict(label="Bislin, “Eight Inches per Miles squared Formula Derivation” — “the drop x is not what is hidden by the curvature of the earth!”; the correct hidden-height formula with observer height",
             url="https://walter.bislins.ch/bloge/index.asp?page=Eight+Inches+per+Miles+squared+Formula+Derivation"),
        dict(label="Bislin, “Deriving Equations for Atmospheric Refraction” — k = 0.143 (a = 7/6) as the geodetic standard, k = 0.17 (a = 6/5) at sea level, and k = 1 as the ducting case where “the earth appears flat”",
             url="https://walter.bislins.ch/bloge/index.asp?page=Deriving+Equations+for+Atmospheric+Refraction"),
        dict(label="Bislin, “Rainy Lake Experiment: Refraction Measurements” — targets 0.37–1.6 m high at 1.1–9.5 km against survey-grade GNSS; measured k from ~0.19 to 0.41; apparent lift ~0.5 m at 5.4 km and ~1 m at 9.5 km",
             url="https://walter.bislins.ch/bloge/index.asp?page=Rainy+Lake+Experiment%3A+Refraction+Measurements"),
        dict(label="Metabunk, “Does Zooming in Change How Much of Something is Hidden by the Horizon [No]” — the controlled zoom-versus-digital-enlargement test",
             url="https://www.metabunk.org/threads/does-zooming-in-change-how-much-of-something-is-hidden-by-the-horizon-no.8840/"),
        dict(label="The Flat Earth Society wiki, “Sinking Ship Effect Caused by Limits to Optical Resolution” — the modern form of Carpenter's proof 63: “a good telescope with sufficient zoom … will bring the ship's hull back in full view”",
             url="https://wiki.tfes.org/Sinking_Ship_Effect_Caused_by_Limits_to_Optical_Resolution"),
        dict(label="Flat Earth Insanity, “Chicago skyline ‘looming’ from MI” — 56.5 miles from Grand Mere State Park; hidden height 453 m at 0% refraction, 404 m at 10%, 364 m at 20%; the stretched section below the spires",
             url="https://flatearthinsanity.blogspot.com/2016/07/chicago-skyline-looming-from-mi.html"),
        dict(label="FlatEarth.ws, “Distance to the Horizon & the Black Swan Observation” — the oil-rig case, and the same rigs photographed with the horizon clearly in front of them on another occasion",
             url="https://flatearth.ws/horizon-distance"),
        dict(label="National Park Service, Cape Hatteras Light Station — focal height 192.2 ft; official range 24 nautical miles; “most vessels in clear weather can see the lighthouse from up to 20 nautical miles at sea”",
             url="https://nps.gov/caha/planyourvisit/chls.htm"),
        dict(label="Cape Agulhas Lighthouse — tower 27 m (89 ft), focal plane 31 m (102 ft) above high water, range 30 nautical miles, against Dubay's “33 feet high, 238 feet above sea level … over 50 miles”",
             url="https://en.wikipedia.org/wiki/Cape_Agulhas_Lighthouse"),
        dict(label="Schadewald, The Plane Truth, ch. 7 — Lady Blount's 11 May 1904 repeat; photographer E. Clifton with a 5000 mm Dallmeyer telephoto lens two feet above the water; “an aqueous shimmering vapour [floated] unevenly on the surface of the canal and adjoining fields”",
             url="https://www.cantab.net/users/michael.behrend/ebooks/PlaneTruth/pages/Chapter_07.html"),
        dict(label="American Oil & Gas Historical Society — Kermac Rig No. 16, “the first offshore rig in the Gulf of Mexico that was out of sight of land”, 10 miles at sea, producing 14 November 1947",
             url="https://aoghs.org/offshore-history/offshore-oil-history/")]),
}
