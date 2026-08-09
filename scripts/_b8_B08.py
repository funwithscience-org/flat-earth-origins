# -*- coding: utf-8 -*-
"""Batch 8 — B08. Star trails, Polaris fixed, southern circumpolar geometry.

Four things found while writing this one, flagged for the parent because they touch
files this agent was told not to edit:

1. THE SOURCE DOES NOT DUCK THE SOUTHERN SKY. Dubay's proof 101 is about Sigma
   Octantis by name, and makes four specific claims about it. A refutation that
   simply asserts "no flat model can produce a southern pole" would be aimed at the
   list's fragments, which mention nothing south of the equator. The refutation below
   answers proof 101 clause by clause first, then runs the geometry.

2. PARTIAL MIS-ATTRIBUTION IN OUR RECORD (clusters.py, ARG-B08, not edited here).
   The cluster is credited to Dubay, 200 Proofs, 2015. That is right for the Sigma
   Octantis strand. It is not the earliest documented text for the Polaris strand:
   Carpenter's One Hundred Proofs (5th ed., 1885) already carries proof 71 ("to see
   the North Star is an impossibility ... yet it is well known this star has been
   seen by navigators when they have been more than 20 degrees south of the equator"),
   which is Dubay's proof 99 almost word for word, and proof 80, the North Star seen
   through the same pane of glass all year round, which is the Polaris-fixed strand.
   Reported, not applied.

   CORRECTED 2026-08-09, and it runs further back than this note first had it.
   Rowbotham is the originator of BOTH strands, not Carpenter and not Dubay.
   (a) Southern strand: Zetetic Astronomy 3rd ed., 1881, section "Motion of Stars
   North and South" (sacred-texts za48.htm) carries the south-pole denial, the
   Southern Cross / Great Bear simultaneity objection in Dubay's own comparative
   form, and the Arthur's Seat perspective reply. That section is not located in
   the 1865 first book edition (Gutenberg #69892, searched for circumpolar, pole
   star, south polar, Southern Cross), so 1881 is the earliest edition we can
   document it in. (b) Polaris-below-the-equator strand: present already in the
   1865 first book edition, on Captain Wilkins in the Times of 13 May 1862 — two
   decades before Carpenter's proof 71. The gloss now says so and cites both.
   For the parent: clusters.py ARG-B08 still reads originator="Eric Dubay",
   year="2015", real_source=None. PER-ROWBOTHAM has been added to this entry's
   people[]; the originator and real_source fields are the parent's call.

3. THE DRIFT RUNS BACKWARDS HERE. Every drift recorded on this page so far moves
   towards more certainty than the author stated. B08 moves the other way: the seven
   list items keep only the northern half, which nobody disputes, and drop the
   southern claims, which are false and checkable. Recorded in the compression note;
   the seven-value enum has no name for a weakening.

4. THE THREE-CONTINENT SIMULTANEITY CLAIM NEEDED TRIMMING. Santiago, Cape Town and
   Sydney span 222 degrees of longitude, so they cannot all be in darkness at the
   same instant. Sigma Octantis is above the horizon at every longitude of a southern
   parallel simultaneously, which is the geometric fact that matters, and any two of
   the three that are dark together see it in the same place. The text says so.
"""

ENTRY = {

"B08": dict(
    tldr=("Go south of the equator and the whole sky turns about a second pole, in the "
          "opposite sense, with Sigma Octantis about one degree from its centre. That is the "
          "observation a disc with Polaris over its middle cannot produce, because a single "
          "rotation axis gives every observer exactly one centre of rotation — and 200 Proofs "
          "does not step around the problem: proof 101 denies that the southern pole star can "
          "be seen at all through publicly available telescopes. Of its four claims about Sigma "
          "Octantis, the two that hold — that it sits about a degree off centre and that it "
          "moves — hold for Polaris in the same way, and Polaris is the fixed benchmark the "
          "same book builds on."),

    passage=dict(
        work="WRK-DUBAY-2015",
        pd=False,
        locator=("proof 101 of 200. The 2015 free PDF is numbered by proof, not by page; read "
                 "in the full-text reproduction posted 31 July 2018 at rexynotes.wordpress.com "
                 "and cross-checked against the SlideShare scan of the PDF. Not checked against "
                 "the 2018 print edition."),
        quote=("Sigma Octantis is claimed to be a Southern central pole star similar to Polaris, "
               "around which the Southern hemisphere stars all rotate … Unlike Polaris, however, "
               "Sigma Octantis can NOT be seen simultaneously from every point along the same "
               "latitude, it is NOT central but allegedly 1 degree off-center, it is NOT "
               "motionless."),
        gloss=("<p>The sentence is trimmed for length; the clause that follows in the original "
               "adds that the star cannot be seen at all using publicly available telescopes. "
               "So there are four claims here, not one, and they are of two kinds. Two are "
               "checkable statements about a star&rsquo;s geometry &mdash; it is not central, it "
               "is not motionless &mdash; and both are correct. Two are claims about what can be "
               "observed and by whom, and those are the ones this treatment tests.</p>"
               "<p>Proof 101 matters more than its neighbours because of what proof 107 commits "
               "the model to. There Dubay reaches for the ring magnet found in loudspeakers, "
               "with a central north pole and the opposite south pole being all points along the "
               "outer circumference. On that model &ldquo;south&rdquo; is not a place; it is a "
               "direction that fans outward from the rim in every azimuth at once. A single "
               "southern point with the sky wheeling around it is therefore not an awkward "
               "detail for the model to absorb, it is the thing the model forbids &mdash; which "
               "is why proof 101 goes after whether the star can be observed at all rather than "
               "trying to fit it in.</p>"
               "<p>Two of the neighbouring proofs are older than 2015. Proof 99, that Polaris is "
               "visible more than 20 degrees south of the equator, restates William "
               "Carpenter&rsquo;s <em>One Hundred Proofs that the Earth is Not a Globe</em> "
               "(5th ed., 1885), proof 71: &ldquo;The astronomers&rsquo; theory of a globular "
               "Earth necessitates the conclusion that, if we travel south of the equator, to "
               "see the North Star is an impossibility. Yet it is well known this star has been "
               "seen by navigators when they have been more than 20 degrees south of the "
               "equator.&rdquo; The Polaris-is-fixed strand has an 1885 ancestor too, in "
               "Carpenter&rsquo;s proof 80, which reasons from seeing the North Star through the "
               "very same corner of the very same pane of glass all the year round. What is new "
               "in 2015 is the naming of Sigma Octantis. The argument around it is not. "
               "Rowbotham&rsquo;s <em>Zetetic Astronomy: Earth Not a Globe</em> (3rd ed., 1881) "
               "gives the southern sky a section of its own, &ldquo;Motion of Stars North and "
               "South&rdquo;, which opens on this exact claim &mdash; &ldquo;IT has often been "
               "urged that the earth must be a globe, because the stars in the southern "
               "&lsquo;hemisphere&rsquo; move round a south polar star&rdquo; &mdash; and "
               "answers it with a denial: the southern region &ldquo;is not central, but "
               "circumferential; and therefore there is no southern pole, no south pole star, "
               "and no southern circumpolar constellations.&rdquo; Proof 101&rsquo;s "
               "simultaneity objection is there in the same comparative form &mdash; &ldquo;The "
               "Southern Cross is not at all times visible from every point of the southern "
               "hemisphere, as the &lsquo;Great Bear&rsquo; is from every point in the "
               "northern&rdquo; &mdash; and so is the perspective reply, which Rowbotham stages "
               "by asking the reader to stand with his back to the north on Arthur&rsquo;s Seat, "
               "near Edinburgh, and watch the stars in his zenith. Quoted from the 1881 third "
               "edition; that section is not located in the 1865 first book edition as posted at "
               "Project Gutenberg (#69892), which we searched for <em>circumpolar</em>, "
               "<em>pole star</em>, <em>south polar</em> and <em>Southern Cross</em>. The 1865 "
               "text does carry the other strand, though &mdash; the north polar star seen "
               "&ldquo;as far even as the tropic of Capricorn&rdquo;, on a report of Captain "
               "Wilkins in the <em>Times</em> of 13 May 1862 &mdash; twenty years before "
               "Carpenter&rsquo;s proof 71. Both halves of this cluster are inherited, and of "
               "the texts traced here the southern half is the earlier: 1881 against "
               "Carpenter&rsquo;s fifth edition of 1885, whose own earlier editions we could not "
               "obtain.</p>"
               "<p>The positive claim is stated most plainly outside the book. Dubay&rsquo;s "
               "video <em>Flat Earth Star Trails Explained</em>, published 30 November 2018 and "
               "archived at the Internet Archive, holds that star trails in both hemispheres "
               "turn about Polaris in the same direction, east to west, rather than in opposite "
               "directions. That is a falsifiable statement, it is the one the geometry below "
               "answers, and none of it survives into the seven items the list carries.</p>")),

    steelman=dict(
        description=(
            "<p><strong>SURFACE (weak &mdash; do not use).</strong> &ldquo;You cannot see "
            "northern constellations from the southern hemisphere, so his numbers are "
            "nonsense.&rdquo; Wrong, and it loses the exchange in one move. Proofs 103 to 105 "
            "list constellations with the latitude bands they can be seen from &mdash; Vulpecula "
            "from 90 degrees north to 55 degrees south, Virgo from 80 north to 80 south, Orion "
            "from about 85 north to about 75 south &mdash; and those bands are arithmetically "
            "right. They are also astronomy&rsquo;s own numbers, printed in ordinary "
            "constellation guides, and they follow from one rule: a star of declination "
            "<em>&delta;</em> stays below the horizon for a northern observer at latitude "
            "<em>&phi;</em> only when <em>&delta;</em> &lt; <em>&phi;</em> &minus; 90&deg;. A "
            "constellation straddling the celestial equator is therefore visible from almost "
            "pole to pole, on a globe, exactly as he says.</p>"
            "<p><strong>DEEPER.</strong> The northern observation at the heart of the cluster is "
            "correct and it is a real constraint. From any site in the northern hemisphere the "
            "stars trace concentric circles about one point, the circles close, and the "
            "constellations show no measurable distortion from one site to the next. That tells "
            "you two things before any model is chosen: the sky&rsquo;s daily motion is a single "
            "rigid rotation about one axis, and the stars are so far away that no baseline on "
            "the ground changes their arrangement. Proof 102 adds a fair point of its own &mdash; "
            "that an object sinking towards the horizon as you walk away from it is generic, and "
            "not by itself a demonstration of curvature.</p>"
            "<p><strong>KERNEL.</strong> Proof 101 is the best thing in the cluster, because it "
            "identifies the decisive datum instead of walking past it. Of 200 proofs it is the "
            "one that names the observation the model has to defeat, and it goes at it head-on. "
            "And two of its four objections are simply true. Sigma Octantis is not on the pole: "
            "it sits slightly more than one degree from it, and precession is carrying the pole "
            "away from it. It is not motionless: it circles the pole once a sidereal day, and it "
            "is a Delta Scuti variable whose brightness shifts by about 0.03 magnitudes every "
            "2.33 hours. Anyone who answers proof 101 by calling Sigma Octantis a fixed southern "
            "Polaris has conceded the point to him. Concede both facts first.</p>"),
        why_it_doesnt_save_claim=(
            "<p>Because both true facts are true of Polaris, in the same way and to within a "
            "factor of two. Polaris was 0.66 degrees (39.6 arcminutes) from the north celestial "
            "pole in 2018, so it traces a circle about 1.3 degrees across every day; Sigma "
            "Octantis is about 1.06 degrees out and traces a circle about 2.1 degrees across. "
            "Polaris is a classical Cepheid and varies in brightness too. Precession is moving "
            "the north pole as well &mdash; towards Polaris until soon after 2100, when it comes "
            "within about 0.45 degrees, and away from it afterwards. So the test proof 101 "
            "applies to the southern pole star &mdash; off centre, and moving &mdash; retires "
            "the northern one on which proof 98 rests. A criterion that deletes your own "
            "benchmark is not a criterion.</p>"
            "<p>And the southern rotation centre is not located by Sigma Octantis in the first "
            "place. It is fixed by the trails of every star in the southern cap, thousands of "
            "them, whose common centre can be measured on a photograph in which no star sits at "
            "the centre at all. Sigma Octantis is a convenience for a navigator, not the "
            "evidence. Removing it would leave the second pole exactly where it is.</p>"),),

    refutation=(
        "<p><strong>Start by giving away the part that is right.</strong> The latitude bands in "
        "proofs 103 to 105 are correct, and the rule that generates them is the globe&rsquo;s. "
        "Circumpolarity and invisibility are set by declination against latitude: a star never "
        "sets when <em>&phi;</em> + <em>&delta;</em> &gt; +90&deg; in the north or "
        "<em>&phi;</em> + <em>&delta;</em> &lt; &minus;90&deg; in the south, and never rises "
        "when the same sums run the other way. Anyone who answers this cluster by insisting that "
        "each hemisphere has its own private sky is wrong, and will be shown to be wrong with "
        "the objector&rsquo;s own star charts.</p>"

        "<p><strong>1. What the southern sky does.</strong> The measurements are these. The "
        "whole sky turns once per sidereal day, 23 h 56 m 04 s, at 15.04 degrees per hour, in "
        "both hemispheres. From a northern site the turn is anticlockwise about a point due "
        "north at an altitude equal to the observer&rsquo;s latitude. From a southern site it is "
        "clockwise about a point due <em>south</em>, again at an altitude equal to the "
        "observer&rsquo;s latitude. At Cape Town, Santiago and Sydney &mdash; all near 34 "
        "degrees south &mdash; that centre stands about 34 degrees above the southern horizon, "
        "and a cap of sky 34 degrees in radius around it never sets: 8.6 per cent of the "
        "celestial sphere, permanently up, with an equal 8.6 per cent around the north celestial "
        "pole permanently out of reach. The Southern Cross lies inside that cap; it is "
        "circumpolar south of 34 degrees south, and its brightest star, Acrux, sits at "
        "declination about &minus;63 degrees. Sigma Octantis, about 1.06 degrees from the "
        "southern pole, is circumpolar for any observer more than about 1.1 degrees south of the "
        "equator &mdash; that is, for essentially the whole southern hemisphere.</p>"

        "<p><strong>2. Proof 101, clause by clause.</strong></p>"
        "<p>(a) <em>&ldquo;can NOT be seen simultaneously from every point along the same "
        "latitude.&rdquo;</em> Being circumpolar from about 1.1 degrees south onward, Sigma "
        "Octantis is above the horizon at <em>every</em> longitude of a southern parallel at the "
        "same instant. One honest qualification, which the list&rsquo;s defenders are entitled "
        "to press: half those longitudes are in daylight at any given moment. Santiago (70.7&deg;W), "
        "Cape Town (18.4&deg;E) and Sydney (151.2&deg;E) span 222 degrees of longitude and cannot "
        "all be dark together. But any two of them that are dark together find the star in the "
        "same place, due south, at an altitude matching their latitude, with the same stars "
        "wheeling around it &mdash; and the daylight limit applies identically to Polaris on the "
        "northern parallel, which proof 101 treats as the standard. Sunlight is not a fact about "
        "geometry.</p>"
        "<p>(b) <em>&ldquo;NOT central but allegedly 1 degree off-center.&rdquo;</em> Correct, "
        "and conceded: slightly more than one degree. Polaris was 0.66 degrees off in 2018. "
        "Nobody has claimed either star sits on its pole; the claim is that each is the nearest "
        "star of its kind to one.</p>"
        "<p>(c) <em>&ldquo;NOT motionless.&rdquo;</em> Correct, and conceded: it circles the pole "
        "once a sidereal day, in a circle about 2.1 degrees across, and its brightness varies by "
        "0.03 magnitudes every 2.33 hours. Polaris circles in 1.3 degrees and varies too.</p>"
        "<p>(d) <em>cannot be seen at all using publicly available telescopes.</em> This is the "
        "one that decides the exchange, and it is checkable by the reader. Sigma Octantis has "
        "apparent magnitude 5.42, about 294 light years away, spectral class F0 IV. The "
        "naked-eye limit under a dark sky is around magnitude 6.5, so the star is a naked-eye "
        "object for a southern observer away from town, and an easy one in any binocular. It is "
        "also on the flag of Brazil, adopted 19 November 1889, where it stands for the Federal "
        "District &mdash; and the official rationale for putting it there is that it is small, "
        "but all the other stars turn around it. That is a documented southern-hemisphere "
        "statement of the second pole, published 126 years before the 2015 PDF, by a government "
        "with no stake in this dispute.</p>"

        "<p><strong>3. What a single-plane model predicts instead.</strong> Take the standard "
        "flat map: the azimuthal-equidistant projection centred on the north pole, on which "
        "ground distance from the centre runs about 111 km per degree of colatitude, with "
        "Polaris hanging at some height <em>h</em> over the centre and the stars carried round "
        "on a dome that turns about the vertical axis through it. Five consequences follow, and "
        "each one is measured to be false.</p>"
        "<p>(i) <em>One centre of rotation, for everybody.</em> A single axis produces exactly "
        "one apparent centre per observer, and it lies in the direction of that axis &mdash; "
        "northward, everywhere on the disc. Southern observers measure a second centre, in the "
        "opposite direction, with its own circumpolar cap.</p>"
        "<p>(ii) <em>One sense of rotation.</em> Every observer on the disc sees the sky turn "
        "the same way about that one centre. Southern trails close in the opposite handedness "
        "from northern ones, at the same rate, on the same nights.</p>"
        "<p>(iii) <em>Polaris at the wrong altitude nearly everywhere.</em> On the disc the "
        "altitude of Polaris is arctan(<em>h</em>/<em>r</em>), with <em>r</em> the ground "
        "distance from the centre. Fit <em>h</em> so that the altitude comes out right at 45 "
        "degrees north and you need <em>h</em> = 5,000 km. That same height then puts Polaris "
        "36.9 degrees up at 30 degrees north, where it is measured at 30; 29.4 degrees up at 10 "
        "degrees north, where it is measured at 10; and 26.6 degrees up at the equator, where it "
        "is on the horizon. The 10-degree error is 19.4 degrees, about thirty-nine full-moon "
        "widths, against a sextant that reads to an arcminute. Fitting each latitude separately "
        "gives a different height every time &mdash; about 5,800 km at 60 north, 3,850 km at 30 "
        "north, 1,570 km at 10 north, and zero at the equator. There is no single height, which "
        "is the arithmetic statement of the fact that altitude equals latitude on a sphere and "
        "cannot on a plane.</p>"
        "<p>(iv) <em>The southern pole would have to be in three directions at once.</em> On "
        "that map Santiago, Cape Town and Sydney all sit about 13,800 km from the centre, on "
        "bearings 89, 133 and 138 degrees apart. Each observer&rsquo;s due south is the "
        "direction straight away from the centre, so their three southern horizons face outward "
        "along three widely divergent lines. Sigma Octantis is 294 light years away; the three "
        "sight-lines to it are parallel to about a millionth of an arcsecond. On the disc they "
        "diverge by up to 138 degrees. One object cannot occupy three directions at once, which "
        "is the whole of the argument, stated without any appeal to authority.</p>"
        "<p>(v) <em>The rim is not a point.</em> Dubay&rsquo;s own proof 107 makes the south the "
        "entire outer circumference. On that map the rim is a circle roughly 126,000 km around. "
        "The southern sky says the southern axis is a point: from every southern longitude the "
        "trails share one centre, and its altitude tracks the observer&rsquo;s latitude one for "
        "one from the tropics to the Antarctic coast.</p>"

        "<p><strong>4. The vanishing-point reply, answered before it is made.</strong> The "
        "standard response at this stage is proof 102&rsquo;s: perspective on a plane. Distant "
        "things converge; a southern observer looking outward across the disc is seeing the far "
        "stars foreshortened into an apparent centre, the way rails appear to meet. Three "
        "measurements close this off. First, a vanishing point on a plane lies on the horizon, "
        "at altitude zero, by construction; the southern centre stands at an altitude equal to "
        "the observer&rsquo;s latitude &mdash; about 12 degrees at Darwin, 34 at Cape Town, 53 "
        "at Punta Arenas &mdash; and moves up as you travel south. Second, a vanishing point is "
        "fixed with respect to the observer and does not turn; the southern centre has stars "
        "circling it at 15.04 degrees per hour, closing into complete circles in one sidereal "
        "day, which is a rotation and not a projection. Third, perspective foreshortens: an "
        "off-centre observer under a dome of finite height would see the constellations near the "
        "far rim compressed, and their angular sizes would change with his distance from the "
        "centre. The Southern Cross subtends the same angle from Chile as from Australia.</p>"

        "<p><strong>5. The two items that make a claim about time.</strong> &ldquo;Polaris "
        "constant alignment over millennia&rdquo; and &ldquo;Zodiacal alignment constant&rdquo; "
        "are the only items in the cluster that assert something about history, and precession "
        "settles both. The axis completes a circuit in roughly 25,800 years, moving the pole "
        "about one degree every 72 years. In classical antiquity the north celestial pole stood "
        "about 10 degrees from Polaris and about as far from Kochab; Pytheas, around 320 BC, "
        "described the pole as devoid of stars. Polaris will be closest to it soon after 2100, "
        "at about 0.45 degrees, and will then recede for the next thirteen millennia. The "
        "equinox has slid about a full zodiacal sign since Hipparchus measured the drift in the "
        "second century BC. These are not fine corrections rescuing a model; the measurement of "
        "this drift is where the study of the sky&rsquo;s long-term motion began.</p>"

        "<p><strong>What is actually in dispute.</strong> Three of the seven items &mdash; "
        "perfect circular star trails around Polaris, perfect star circles, Polaris fixed "
        "&mdash; report things that are true and that nobody contests. Northern trails do close "
        "into near-perfect circles about a point 0.66 degrees from Polaris. Refuting an "
        "observation is not on offer and is not needed. What fails is the inference, and it "
        "fails on a second observation the same instrument makes from the other half of the "
        "world: point the camera south from Paranal and the trails close about a different "
        "centre, turning the other way. Two poles, one sky, one rotation. A disc with Polaris "
        "over its middle has one axis and can deliver one centre, which is why the argument "
        "arrives at the southern pole star with a denial rather than an explanation. "
        "<strong>Verdict: refuted</strong> &mdash; and refuted by an observation any reader with "
        "a camera, a tripod and a flight to the southern hemisphere can make without trusting "
        "anyone.</p>"),

    advocate=dict(
        best_defense=(
            "Notice what you have actually done. Every load-bearing number in that answer comes "
            "from the institutions whose honesty is the thing in dispute: a Wikipedia infobox "
            "for the magnitude, a European observatory&rsquo;s press image for the trails, a "
            "government flag committee for the 1889 rationale. I say the southern pole star is "
            "not observable by ordinary people with ordinary equipment, and your reply is a "
            "photograph. Long exposures are the easiest images in the world to composite, and "
            "you have offered no observation I can make from where I am standing &mdash; which "
            "is the definition of an argument from authority. On the geometry: you have assumed "
            "my model rather than read it. Perspective on a plane does not merely shrink things, "
            "it converges them; over thousands of miles the convergence is severe, and the "
            "centre of that convergence rises above the horizon exactly as the observer moves "
            "outward from the centre of the disc, which is the correlation you are calling a "
            "signature of a sphere. Your best point is the arctangent table, and even there you "
            "have chosen a projection for me and then refuted your own choice: nothing obliges a "
            "flat map to be azimuthal-equidistant with a fixed Polaris height, and until you can "
            "show me every possible flat cosmology fails, you have refuted one drawing."),
        survives=4,
        preemptive=(
            "Rated 4 because two of the three moves are good and one of them is the movement's "
            "actual position rather than a caricature. Three changes, all now in the body rather "
            "than left to the reader. (1) The perspective reply gets a dedicated section 4 with "
            "three independent measurements against it &mdash; a vanishing point sits at "
            "altitude zero while the southern centre sits at altitude equal to latitude; a "
            "vanishing point does not turn while the southern centre carries stars round it at "
            "15.04 degrees per hour, closing in one sidereal day; and a finite dome foreshortens "
            "while the Southern Cross subtends the same angle from Chile and from Australia. "
            "Write it before he does, because 'perspective' is the reply that lands with "
            "readers. (2) The authority objection is answered by choosing evidence he can reach: "
            "the closing paragraph puts the test in the reader's hands (camera, tripod, "
            "southbound flight), and the Brazilian flag is used precisely because it is a "
            "documented 1889 statement of the second pole from the southern hemisphere itself, "
            "not a modern institutional claim. Do not answer 'you can go and look' with more "
            "photographs. (3) The 'you chose my projection' move is real and is not fully "
            "closed, and the body is written so it does not need to be: section 3(iv) does not "
            "depend on the azimuthal-equidistant map at all beyond the bearings, and section "
            "3(i) and (ii) depend only on there being a single rotation axis, which is what "
            "'the stars go round over a plane' means. Keep the arctangent table as an "
            "illustration, never as the load-bearing step, and say out loud that the general "
            "claim is against any single-axis model, not against one drawing. Finally: the "
            "'unobservable by ordinary people' claim, pressed hard enough, becomes unfalsifiable "
            "for a reader who will not travel. Name that plainly &mdash; it is a limit on what "
            "can be settled from an armchair, not a defect in the observation &mdash; and do not "
            "mock it."),),

    straw_man=dict(
        identified=True,
        detail=("Three, and the first two are in one sentence. (1) Proof 101's fourth clause "
                "sets a test nobody proposed &mdash; whether the star can be seen 'using "
                "publicly available telescopes' &mdash; and treats failing it as decisive. No "
                "astronomical claim about the south celestial pole depends on telescope access; "
                "a magnitude 5.42 star is a naked-eye object under a dark sky. (2) The second "
                "and third clauses attack a position nobody holds: that Sigma Octantis sits "
                "exactly on the pole and does not move. The standard statement is that it is the "
                "nearest naked-eye star to the southern pole, roughly a degree out and circling "
                "&mdash; which is exactly the relationship Polaris has to the northern pole, and "
                "proof 98 accepts Polaris without demur. (3) Proof 99, and its ancestor at "
                "Carpenter proof 71 in the 1885 fifth edition, state the globe's prediction as "
                "'to see the North Star is an impossibility' south of the equator, and then "
                "offer sightings 20 degrees south as a refutation. The prediction is a specific "
                "number, not an absolute: a star 0.66 degrees from the pole is above the horizon "
                "until about 0.7 degrees past the equator, extended by roughly another degree by "
                "horizon refraction. Carpenter's own supporting sightings are introduced in that "
                "1885 edition as 'well known', with no observer, date, vessel or instrument "
                "attached to them, and Dubay's proof 99 inherits the claim in the same form."),),

    compression=dict(
        assessed=True, drifted=True,
        list_phrasing="Constant constellations. / Constellation stability.",
        source_wording=("&ldquo;There are several constellations which can be seen from far "
                        "greater distances over the face of the Earth than should be possible if "
                        "the world were a rotating, revolving, wobbling ball.&rdquo; &hellip; "
                        "&ldquo;The constellation Vulpecula can be seen from 90 degrees North "
                        "latitude, all the way to 55 degrees South latitude.&rdquo; "
                        "(proofs 103&ndash;104)"),
        drift_type="scope_widened",
        note=("Dubay&rsquo;s claim is <em>spatial and specific</em>: named constellations, each "
              "with the band of latitudes it can be seen from, offered as bands too wide for a "
              "globe. The list renders this as &ldquo;Constant constellations&rdquo; and "
              "&ldquo;Constellation stability&rdquo; &mdash; two-word fragments that a reader "
              "will take as a claim about <em>time</em>, that the constellations do not change. "
              "Read that way they are false for reasons Dubay never argued (precession, proper "
              "motion); read the source&rsquo;s way they are a claim about visibility geometry "
              "with checkable numbers, and the numbers are right. The refutation above answers "
              "the source&rsquo;s version &mdash; which is why it opens by conceding the "
              "latitude bands rather than disputing them. Item 145, &ldquo;Zodiacal alignment "
              "constant&rdquo;, is the one this pass could place least confidently against any "
              "proof in the text read.<br><br>"
              "<strong>A second movement, and it runs the other way from every drift on this "
              "page.</strong> The seven items report only the northern sky: perfect circular "
              "star trails, Polaris fixed, constellations constant. Nothing south of the equator "
              "survives into them. But the southern sky is where the source stakes its case "
              "&mdash; proofs 99 to 102 on Polaris below the equator, the Southern Cross, and "
              "Sigma Octantis, and the 2018 video <em>Flat Earth Star Trails Explained</em>, "
              "which holds that trails in both hemispheres turn about Polaris in the same "
              "direction. Those claims are bold and checkable. The list kept the half that is "
              "uncontested &mdash; northern trails really do close into circles about Polaris "
              "&mdash; and dropped the half that fails. So the fragment is not overstated here; "
              "it is <em>disarmed</em>, and a reader meeting item 16 as a proof meets something "
              "no astronomer disputes. The seven drift types have no value for a weakening, so "
              "it is recorded in words: on this cluster the chain degraded towards safety rather "
              "than towards certainty, which is a counter-example to the pattern the rest of "
              "this page has found, and worth more than the label.")),

    verdict_challenge=dict(challenged=False, proposed_verdict=None, reasoning=None),

    people=["PER-DUBAY", "PER-CARPENTER", "PER-ROWBOTHAM"],
    related=["A22", "A05", "B12", "B02", "D11"],

    sources=[
        dict(label="Dubay, 200 Proofs Earth Is Not a Spinning Ball (2015) — full-text "
                   "reproduction, 31 July 2018; proofs 98–108 read here",
             url="https://rexynotes.wordpress.com/2018/07/31/200-proofs-earth-is-not-a-spinning-ball-english/"),
        dict(label="Dubay, 200 Proofs — SlideShare scan of the PDF, used to cross-check the "
                   "wording of proof 101",
             url="https://www.slideshare.net/slideshow/dubay-eric-200-proofs-earth-is-not-a-spinning-ball/72521066"),
        dict(label="Dubay, “Flat Earth Star Trails Explained” (30 November 2018) — Internet "
                   "Archive mirror; the both-hemispheres-turn-about-Polaris claim",
             url="https://archive.org/details/youtube-X-w8acuxF6w"),
        dict(label="Carpenter, One Hundred Proofs that the Earth is Not a Globe (5th ed., 1885) "
                   "— Project Gutenberg full text; proofs 71 and 80, the 1885 ancestors",
             url="https://www.gutenberg.org/files/55387/55387-h/55387-h.htm"),
        dict(label="Rowbotham (as “Parallax”), Zetetic Astronomy: Earth Not a Globe, 3rd ed. "
                   "1881 — “Motion of Stars North and South”: the south-pole denial, the "
                   "Southern Cross / Great Bear simultaneity objection, and the Arthur’s Seat "
                   "perspective reply, all quoted above",
             url="https://sacred-texts.com/earth/za/za48.htm"),
        dict(label="Rowbotham, Zetetic Astronomy: Earth Not a Globe! (1865 first book edition), "
                   "Project Gutenberg #69892 — searched for circumpolar, pole star, south "
                   "polar, Southern Cross; carries the north polar star “as far even as the "
                   "tropic of Capricorn” (Captain Wilkins, the Times, 13 May 1862)",
             url="https://www.gutenberg.org/ebooks/69892"),
        dict(label="Sigma Octantis — magnitude 5.42, ~294 ly, F0 IV, Delta Scuti, just over 1° "
                   "from the south celestial pole",
             url="https://en.wikipedia.org/wiki/Sigma_Octantis"),
        dict(label="Polaris — 0.66° (39.6′) from the north celestial pole in 2018, closest "
                   "approach ~0.45° soon after 2100, ~10° away in classical antiquity",
             url="https://en.wikipedia.org/wiki/Polaris"),
        dict(label="Circumpolar star — the φ + δ conditions for never setting and never rising",
             url="https://en.wikipedia.org/wiki/Circumpolar_star"),
        dict(label="Crux — constellation declination range −55.68° to −64.70°; circumpolar south "
                   "of the 34th parallel south",
             url="https://en.wikipedia.org/wiki/Crux"),
        dict(label="Crux (Constellation Guide) — second source for “circumpolar south of 34°S”; "
                   "Acrux at about −63° declination",
             url="https://www.constellation-guide.com/constellation-list/crux-constellation/"),
        dict(label="Flag of Brazil — adopted 19 November 1889; Sigma Octantis stands for the "
                   "Federal District because “all the other stars turn around it”",
             url="https://en.wikipedia.org/wiki/Flag_of_Brazil"),
        dict(label="ESO / A. Santerne, “Southern Hemisphere circumpolar star trails”, Paranal "
                   "Observatory, Chile",
             url="https://www.eso.org/public/images/171109-cc/"),
        dict(label="FlatEarth.ws — rebuttal index to the 200 Proofs, used to locate the proof "
                   "numbers before reading them in the source",
             url="https://flatearth.ws/eric-dubay")]),
}
