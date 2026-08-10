# -*- coding: utf-8 -*-
"""
Batch 9 — ARG-E06, "Dwarf-galaxy planes and satellite alignments".
3 items (330, 337, 338), lane E, verdict MISLEADING, originator recorded null.

Research notes for whoever picks this up next. Six things, in order of how much they
change the entry.

1. THE THREE ITEMS ARE NOT ONE CLAIM. Items 337 ("Dwarf galaxy planes coherence.") and
   338 ("Satellite alignments.") compress the plane-of-satellites literature. Item 330
   ("Cluster axes ecliptic.") is a different assertion in a different vocabulary: it is
   an ECLIPTIC-alignment claim, and the ecliptic appears nowhere in the satellite-plane
   papers read for this entry. It sits with E01/E11's vocabulary, not with this
   cluster's. Reported up, not moved: `assign.py` was NOT touched, and neither was
   `clusters.py`. The cluster NAME does not cover item 330 either.

2. THE ANOMALY IS LIVE AND THE PAGE MUST KEEP SAYING SO — the E01 precedent exactly.
   The record's note calls it "a real LambdaCDM tension that has substantially
   deflated". That is stronger than the literature supports as of this pass: Sawala et
   al. 2023 (Nature Astronomy 7:481) is one side of an argument, not its close. Against
   it: Mueller et al. 2021 (A&A 645:L5), whose title is "The coherent motion of Cen A
   dwarf satellite galaxies REMAINS A CHALLENGE for LambdaCDM cosmology"; Seo et al.
   2024 (ApJ 976:253), which rebuilds the rarity test and still gets 0.00-3.40% for the
   Milky Way disc of satellites; Pawlowski et al. 2024 (A&A, NGC 4490). Sawala's own
   follow-up (arXiv:2510.01318, v2 dated 19 March 2026) reconciles "transient" and
   "persistent" rather than declaring a win. Recorded in `record_problems`; the
   published prose below states the state of the dispute directly and does not comment
   on our own record.

3. `real_source` NAMES ONLY THE REBUTTAL. The field carries Sawala 2023 and nothing
   else, so the record cites the paper that argues the anomaly away as the source of an
   item that asserts the anomaly. The papers the items actually compress are Kroupa,
   Theis & Boily 2005 (A&A 431:517), Kroupa et al. 2010 (A&A 523:A32), Pawlowski,
   Pflamm-Altenburg & Kroupa 2012 (MNRAS 423:1109), Ibata et al. 2013 (Nature 493:62)
   and Mueller et al. 2018 (Science 359:534). Also reported up.

4. NO MOVEMENT TEXT WAS LOCATED, AND THE SEARCH IS WRITTEN OUT IN `untraceable`. The
   djvu text of the three-volume Internet Archive scan
   'galileo-was-wrong-the-church-was-right-sungenis-vol-1-3-complete' was downloaded
   whole (5.5 MB, 134,983 lines) and searched: "Kroupa", "Ibata", "M31", "Tully",
   "plane of satellites", "disk of satellites" return zero; "dwarf" returns twelve, of
   which the only astronomical run is the dwarf-irregular REDSHIFT-QUANTIZATION passage
   that belongs to ARG-E12; "Andromeda" returns two, both Italian publisher addresses in
   the bibliography. So the geocentric compendium this list demonstrably uses elsewhere
   does not appear to be where these three came from, and the claim's only identifiable
   ancestors are the astronomy papers themselves. originator=None stands.

5. THE NUMBERS IN THE REFUTATION WERE COMPUTED IN-SESSION (2026-08-09) FROM PUBLISHED
   NORMALS, and the computation is self-checked. Inputs: VPOSall normal (l,b) =
   (156.4 deg, -2.2 deg) (Kroupa et al. 2010, as tabulated by Pawlowski et al. 2012
   Table 1); GPoA normal (l,b) = (206 deg, 8 deg) (Pawlowski, Kroupa & Jerjen 2013);
   north ecliptic pole in galactic coordinates (96.38 deg, +29.81 deg), derived from
   RA 18h00m, Dec +66.5607 deg with the J2000 galactic pole. Outputs: VPOSall inclined
   65.5 deg to the ecliptic, GPoA 77.3 deg, and VPOSall-to-GPoA 50.5 deg. That last
   number is the CHECK: Pawlowski, Kroupa & Jerjen publish 51 deg for the same pair, so
   the coordinate handling is verified against their result before any of it is used.
   For a randomly oriented plane, P(inclination to the ecliptic < a) = 1 - cos a, which
   puts a random plane closer to the ecliptic than the VPOS 59% of the time and closer
   than the GPoA 78% of the time.

6. THE ITEM-330 ANSWER IS THE BEST PART AND IT IS INSTRUMENTAL. Deep extragalactic
   catalogues really do pile up at the ecliptic poles, for a reason that has nothing to
   do with clusters: ROSAT scanned great circles perpendicular to the ecliptic plane and
   all such circles meet at the ecliptic poles (hence a "ROSAT North Ecliptic Pole
   survey" exists at all); JWST's NEP Time-Domain Field is in the northern Continuous
   Viewing Zone; Euclid Deep Field North sits at 17:58:55.9 +66:01:03.7, and ESA's own
   survey page gives the reason as "The proximity to the ecliptic pole ensures maximum
   coverage throughout the year". An ecliptic dependence in such a catalogue is the
   spacecraft's, and that is the same lesson E01 draws about the CMB alignments.

TRAP AVOIDED. The tempting line "the plane-of-satellites problem was solved in 2022" is
false and would hand a defender the entry. Sawala et al. answered the Milky Way case and
said so; they explicitly did not address the other hosts ("This work only directly
addresses the archetypal 'plane of satellites' around the MW").
"""

ENTRY = {

"E06": dict(

    tldr=("The plane-of-satellites problem is real, still unsettled, and argued out in "
          "Nature and Science by people with no stake in this list — and every structure "
          "in it is referenced to other galaxies rather than to us. The Milky Way's "
          "satellite plane is inclined about 65° to the ecliptic and Andromeda's about "
          "77°, and the two are inclined about 51° to each other, so there is no shared "
          "axis on offer to point anywhere. The one genuinely Earth-facing fact is that "
          "Andromeda's plane is seen edge-on from here, which is the condition for "
          "detecting its rotation at all: its discoverers call that orientation "
          "fortunate, and their own 2026 mock-observation study finds that orientation is "
          "one of the two a survey can detect at all. The third item, cluster axes on the "
          "ecliptic, matched "
          "nothing in the cluster-alignment literature searched — where the ecliptic does "
          "show up in deep extragalactic catalogues, it is because that is where a "
          "spacecraft tied to the Earth's orbit can stare longest."),

    passage=None,

    untraceable="""<p>There is no movement text to quote here, and the search that established it is worth writing out, because this cluster sits in the part of the list where the flat-earth material stops and other people&rsquo;s astronomy starts.</p>

<p><strong>The specimen carries no citation.</strong> Re-fetched 2026-08-09: the heading reads &ldquo;435 Pieces of Evidence The Earth is Not A Spinning Ball&rdquo; over 461 numbered lines, and items 330, 337 and 338 are three bare noun phrases &mdash; <em>Cluster axes ecliptic.</em> &middot; <em>Dwarf galaxy planes coherence.</em> &middot; <em>Satellite alignments.</em> &mdash; with no author, paper, date or number attached to any of them.</p>

<p><strong>The geocentric compendium the rest of the list uses was searched in full and did not yield them.</strong> The djvu text of the three-volume Internet Archive scan <code>galileo-was-wrong-the-church-was-right-sungenis-vol-1-3-complete</code> (5.5&nbsp;MB, 134,983 lines) was downloaded whole and searched term by term. &ldquo;Kroupa&rdquo;, &ldquo;Ibata&rdquo;, &ldquo;M31&rdquo;, &ldquo;Tully&rdquo;, &ldquo;plane of satellites&rdquo; and &ldquo;disk of satellites&rdquo; each return zero hits in that text. &ldquo;Dwarf&rdquo; returns twelve, of which one run is astronomical &mdash; the dwarf-irregular <em>redshift-quantization</em> passage, which is <a href="#ARG-E12">ARG-E12</a>&rsquo;s material and a different argument &mdash; and the rest are Gulliver, a simile about Hubble, and the phrase &ldquo;dwarfs any other&rdquo;. &ldquo;Andromeda&rdquo; returns two, both of them an Italian publisher&rsquo;s address in the bibliography.</p>

<p><strong>Where the vocabulary of item 330 does live.</strong> &ldquo;Ecliptic&rdquo; is dense in that same scan &mdash; scores of occurrences &mdash; but all of the ones read here are in the microwave-background chapter, arguing that the CMB multipoles line up with the Earth&rsquo;s orbital plane. That is <a href="#ARG-E01">ARG-E01</a>&rsquo;s claim, in <a href="#ARG-E01">ARG-E01</a>&rsquo;s words. Item 330 applies the same word to galaxy-cluster axes, and the sentence that would license it was not located in the text searched. We record the resemblance as a resemblance and stop: a shared word is not a derivation, and inventing an author to fill the blank is the error this review exists to document.</p>

<p><strong>An honest note on our limits.</strong> <em>No movement source found</em> means we did not find one, not that none exists. Three noun phrases can enter a list from a broadcast, a forum, a slide or a caption that leaves nothing searchable, and the astronomy they compress has been in the popular press since 2013. A reader who can point us at someone who actually argued from satellite planes to a central Earth &mdash; in print, on air, anywhere datable &mdash; will improve this entry, and we will publish the correction.</p>

<p>What follows therefore answers the <em>science</em> at its own strength rather than a summary of it: the planes are real, the tension with the standard cosmological model is real, and the argument about it is still running.</p>""",

    steelman=dict(
        description="""<p><strong>SURFACE (weak &mdash; do not use).</strong> &ldquo;The plane-of-satellites problem was solved in 2022.&rdquo; Anyone who says this loses the exchange to a reader with a search engine. Sawala et al. answered the <em>Milky Way</em> case and were explicit about the scope: their paper says it &ldquo;only directly addresses the archetypal &lsquo;plane of satellites&rsquo; around the MW&rdquo;. Two years later Seo et al. rebuilt the rarity test from the satellites&rsquo; orbital poles and distances and still got 0.00&ndash;3.40% for the Milky Way system, and the Centaurus&nbsp;A paper of 2021 has the word &ldquo;remains&rdquo; in its title.</p>

<p><strong>DEEPER.</strong> The observations are solid and they were made by people with no interest in this list. Around the Milky Way, satellites, young halo globular clusters and stellar streams share one highly inclined plane from 10 to 250&nbsp;kpc out, with an RMS height of about 29&nbsp;kpc (Pawlowski, Pflamm-Altenburg &amp; Kroupa 2012). Around Andromeda, Ibata et al. found a planar subgroup containing about half the satellites at 99.998% significance: at least 400&nbsp;kpc across, less than 14.1&nbsp;kpc thick, with the line-of-sight velocities showing a common sense of rotation (<em>Nature</em>, 2013). Around Centaurus&nbsp;A, 14 of the 16 satellites with measured velocities follow a coherent pattern along the long axis of their distribution, a configuration found in fewer than 0.5% of simulated analogues (<em>Science</em>, 2018). Anyone answering this by denying that the planes are there is simply wrong.</p>

<p><strong>KERNEL.</strong> The strongest form is not &ldquo;an anomaly exists&rdquo;. It is that <em>the geometry demonstrably involves our own position</em>, and the discoverers say so in print. Ibata et al.&rsquo;s abstract calls it intriguing: the Andromeda plane is &ldquo;approximately aligned with the pole of the Milky Way&rsquo;s disk and is co-planar with the Milky Way to Andromeda position vector.&rdquo; Pawlowski, Kroupa &amp; Jerjen put a number on it &mdash; the plane&rsquo;s normal is almost perpendicular to the Milky Way&ndash;Andromeda line, so the structure &ldquo;is seen edge-on from the MW (inclined by only 3&deg;)&rdquo; &mdash; and they find the two Local Group dwarf planes &ldquo;surprisingly symmetric&rdquo;, similarly thin, with &ldquo;near-to-identical offsets from the MW and M31&rdquo;. A defender who builds the argument out of those three sentences is quoting the literature accurately and is not inventing anything.</p>""",
        why_it_doesnt_save_claim="""<p>Because the body all three sentences are referenced to is a <em>galaxy</em>, and the step from there to the Earth is the one step nobody in that literature takes or needs. &ldquo;Aligned with the pole of the Milky Way&rsquo;s disk&rdquo; is a statement about the rotation axis of a 30-kpc stellar disc. &ldquo;Co-planar with the Milky Way to Andromeda position vector&rdquo; is a statement about a 780-kpc line joining two galaxies. Both are exactly what the proposed explanations predict &mdash; accretion along the local filament, or tidal debris flung out in a past encounter between the two big galaxies &mdash; and both would read identically if the Sun sat anywhere else in the disc. The ecliptic, by contrast, is the plane of a 1-astronomical-unit orbit, and one AU is about ten billion times smaller than the distance to the nearest satellite galaxy in the structure. A plane fitted to objects 10 to 250&nbsp;kpc out cannot resolve where in the Solar System you stood when you fitted it.</p>

<p>And the edge-on geometry is the <strong>condition of the measurement</strong>, not a result of it. Corotation in the Andromeda system is inferred from line-of-sight velocities alone, which carry the signal only when the plane is presented near edge-on &mdash; which is why Pawlowski, Kroupa &amp; Jerjen call that orientation <em>fortunate</em> in the same paragraph where they use it. In 2026 the same group quantified the effect in mock observations of simulated hosts and reported that planes &ldquo;viewed nearly edge-on or face-on, are the most readily detected&rdquo;, with intermediate orientations largely missed. So the discovered cases are drawn from the orientations in which discovery is possible. A plane through Andromeda lies within 3&deg; of containing the Milky Way direction for about 5% of random orientations; that is a modest coincidence, and it is precisely the 5% in which the corotation can be seen at all.</p>""",),

    refutation="""<p><strong>1. First the concession, and it is not grudging.</strong> The planes are real, the tension with the standard cosmological model is real, and it is not closed. The history is public: Lynden-Bell noticed the alignment of several Milky Way companions with the Magellanic Stream in 1976; Kroupa, Theis &amp; Boily made it a cosmological problem in 2005; the Milky Way structure was extended to globular clusters and streams in 2012; <em>Nature</em> published the Andromeda plane in 2013 and <em>Science</em> the Centaurus&nbsp;A plane in 2018. The pushback is just as real &mdash; Cautun et al. showed in 2015 that flattened subsets are common in simulations and that the look-elsewhere effect inflates the reported significance by factors of 30 and 100 for the Milky Way and Andromeda respectively, and Sawala et al. traced most of the Milky Way&rsquo;s anisotropy to a lopsided radial distribution plus the fleeting present-day conjunction of Leo&nbsp;I and Leo&nbsp;II, finding the orbital-pole clustering in about 2% of simulated systems where an earlier estimate had said 0.04%. And the pushback has been pushed back: Seo et al. (2024) rebuilt the rarity test around the satellites&rsquo; orbital poles and distances and still found the Milky Way disc of satellites at 0.00&ndash;3.40%; the Centaurus&nbsp;A follow-up of 2021 is titled &ldquo;remains a challenge&rdquo;. This page takes no side in that dispute. It is a live question in galaxy formation, and a reader should be suspicious of anyone &mdash; on either side of the flat-Earth argument &mdash; who tells them it is settled.</p>

<p><strong>2. What the dispute is about, which is not the Earth.</strong> Every participant is arguing about the same thing: whether dark-matter subhaloes, falling into a galaxy along filaments and in groups, can produce satellite systems as flattened and as kinematically coherent as the ones observed. The competing answers are (a) yes, given lopsided radial distributions and short-lived alignments, or (b) no, so the satellites are not dark-matter subhaloes at all but tidal dwarf galaxies formed from material torn out in a past encounter. Both answers are about the formation of galaxies. Neither is about the shape of the Earth, the motion of the Earth, or the position of the Earth, and the arithmetic of the papers would be unchanged if the Solar System were deleted from them.</p>

<p><strong>3. The planes do not share an axis, and the ecliptic is not it.</strong> Items 337 and 338 name no direction, so the test has to be supplied &mdash; and the only Earth-referenced axis the neighbouring items offer is the ecliptic, which item 330 names outright. Run it. Taking the published normals &mdash; the Milky Way disc of satellites at galactic (156.4&deg;, &minus;2.2&deg;) and the Great Plane of Andromeda at (206&deg;, +8&deg;) &mdash; and the north ecliptic pole at galactic (96.4&deg;, +29.8&deg;), the Milky Way&rsquo;s plane is inclined <strong>65.5&deg;</strong> to the ecliptic and Andromeda&rsquo;s <strong>77.3&deg;</strong>. The same computation returns 50.5&deg; for the angle between the two satellite planes, against the 51&deg; Pawlowski, Kroupa &amp; Jerjen publish for that pair, which is how we know the coordinates were handled correctly before any of this was used. For a randomly oriented plane the probability of lying closer to the ecliptic than a given inclination <em>a</em> is 1 &minus; cos&nbsp;<em>a</em>: a random plane beats the Milky Way&rsquo;s for ecliptic alignment 59% of the time and Andromeda&rsquo;s 78% of the time. These structures are not merely unaligned with the Earth&rsquo;s orbital plane; they are further from it than chance usually manages. And they are 51&deg; apart from each other, so there is no common axis in the data for anything to be centred on.</p>

<p><strong>4. Whose centre these are fitted about.</strong> A plane has an orientation and an offset, and the offsets are published too. The Milky Way structure is fitted in galactocentric coordinates, spans 10 to 250&nbsp;kpc, and the globular-cluster plane inside it sits 2.6&nbsp;kpc off the <em>Galactic</em> centre. The Sun is about 8&nbsp;kpc from that centre, so if these were Earth-referenced structures the fits would be displaced by the Sun&rsquo;s offset, and they are not; nobody has needed to try. Centaurus&nbsp;A settles it without any arithmetic: its satellite plane is centred on a galaxy 3.8&nbsp;Mpc away. A thin, rotating structure around another galaxy cannot be evidence that this one is the centre of anything, whichever way it is tilted.</p>

<p><strong>5. The one fact that does involve us, stated at full strength and then answered.</strong> The Andromeda plane is oriented so that it nearly contains the line from here to Andromeda: its normal is almost perpendicular to that line, and the plane is presented to us within about 3&deg; of edge-on. That is real and it is in the discovery papers. But it is also the reason the discovery exists. The rotation of the Andromeda system was established from line-of-sight velocities &mdash; northern members receding from us in the Andromeda rest frame, southern ones approaching &mdash; and a plane tilted face-on projects that motion out of the line of sight entirely. Pawlowski, Kroupa &amp; Jerjen say as much when they describe the orientation as fortunate; in 2026 Crosby, Pawlowski, Mueller and Jerjen built mock observations of simulated hosts to work out which planes surveys actually find, and reported that planes viewed nearly edge-on or face-on are the most readily detected while intermediate orientations are missed. That is a selection effect measured by the people who believe the planes are a problem, and it is the least contested thing in this section. What it means is plain: the case that looks addressed to us is the case in which an observation addressed to us was possible.</p>

<p><strong>6. Item 330, and the ecliptic that really is in the catalogues.</strong> Galaxy-cluster axes do align &mdash; with each other. West et al. (2025) used the largest available cluster catalogue and found orientations correlated out to 200&ndash;300 comoving Mpc and detectable to redshift 1 or beyond, with the comparison to simulations suggesting that coherent structures on such scales &ldquo;may be expected in LCDM models&rdquo;. That is clusters growing along the filaments of the cosmic web and remembering the direction they grew from, at distances where the light left before the Solar System existed. What could not be located, in the cluster-alignment literature searched for this entry or in the geocentric volume searched for it, is any measurement tying cluster axes to the ecliptic. What <em>is</em> tied to the ecliptic is the observing. ROSAT surveyed the sky on great circles perpendicular to the ecliptic plane, and every such circle passes through the ecliptic poles, which is why the deepest X-ray exposure of that survey &mdash; and a literature of cluster papers with &ldquo;North Ecliptic Pole&rdquo; in the title &mdash; is there. JWST&rsquo;s North Ecliptic Pole Time-Domain Field was sited where it is because it is the one clean extragalactic deep field inside the telescope&rsquo;s northern Continuous Viewing Zone. Euclid&rsquo;s northern deep field is at 17h58m56s +66&deg;01&prime;, and ESA&rsquo;s stated reason is that &ldquo;the proximity to the ecliptic pole ensures maximum coverage throughout the year&rdquo;. So deep extragalactic samples really do accumulate towards the ecliptic poles, for the same reason a north-facing window sees more of the northern sky. An ecliptic signature in such a catalogue is the spacecraft&rsquo;s orbit showing through the data &mdash; which is the identical lesson <a href="#ARG-E01">ARG-E01</a> draws about the microwave background, and it points at a local systematic rather than a cosmic centre.</p>

<p><strong>7. What the anomaly buys at maximum strength, and who has to pay for it.</strong> Suppose the planes stand and the standard model cannot make them. The reading the literature offers is the one Sawala et al. set out in their own introduction before disputing it: the plane of satellites &ldquo;might constitute evidence for MOND&rdquo;, in which the Milky Way&rsquo;s satellites are dark-matter-free tidal dwarf galaxies formed in a hypothetical past close encounter between the Milky Way and Andromeda. Follow that and the prize is modified gravity plus two galaxies that swung past each other &mdash; a cosmology in which the Milky Way moves, Andromeda moves, and the Earth plays no part in the argument at all. It is also a cosmology the rest of this list has already rejected: items 86, 352 and 353 file dark matter, dark energy and MOND together as modern epicycles (<a href="#ARG-D14">ARG-D14</a>). The list is spending the significance of an anomaly that only has significance inside a debate it dismisses, and cashing it for a conclusion neither side of that debate holds.</p>

<p><strong>8. The instrument problem, which cuts the same way.</strong> The kinematics that make these items sound impressive are proper motions from Gaia and radial velocities reduced to the Solar-System barycentre. Both reductions subtract the Earth&rsquo;s rotation and orbital motion before anything is fitted. Ten items later the same list calls Gaia&rsquo;s reduction &ldquo;flexible&rdquo; and complains that interferometry assumes a ground frame (<a href="#ARG-E15">ARG-E15</a>). A claim cannot draw its evidential weight from a catalogue whose reduction it elsewhere refuses, and if the reduction is wrong the satellite velocities go with it.</p>

<p><strong>Verdict: misleading, and the misleading part is the framing rather than the facts.</strong> Two of the three items point at genuine, unresolved research; the third points at nothing we could locate. What none of them does is discriminate. Every measurement in this cluster is an angle on the sky and a velocity along the line of sight for dwarf galaxies orbiting other galaxies, and the two models the list is trying to choose between predict identical values for all of them.</p>""",

    advocate=dict(
        best_defense=(
            "Read what you have just written. You conceded that the anomaly is live, that "
            "the planes are real, that the significance is disputed, and that Andromeda's "
            "plane is oriented within three degrees of edge-on to us. Then you explained "
            "the one fact that involves our position by calling it a selection effect — "
            "which is what a defender of any theory says about the observation that "
            "embarrasses it. Note the shape of your argument: where the data point at us, "
            "the data are a bias; where they do not, they are evidence. Second, your "
            "ecliptic arithmetic refutes a claim we did not make. Items 337 and 338 say "
            "nothing about the ecliptic; you supplied the axis yourself and then knocked "
            "it down. Third, the symmetry you skipped past is the real one. Pawlowski, "
            "Kroupa and Jerjen found two Local Group planes that are surprisingly "
            "symmetric, similarly thin, and at near-identical offsets from the Milky Way "
            "and Andromeda — an arrangement they say no detailed model explains. You "
            "answer with 'that is about galaxies, not the Earth', as though we could be "
            "somewhere else while our Galaxy sits at the axis of the local universe. And "
            "you close by demanding we choose between dark matter and MOND. We decline "
            "both, which is the whole point: the standard model's own best data keep "
            "producing structures its own simulations cannot make."),
        survives=3,
        preemptive=(
            "Three is right and the number is set by the second move, not the first. The "
            "'you supplied the axis' hit is fair and must be disarmed BEFORE the "
            "arithmetic rather than after, which is why section 3 now opens by saying that "
            "items 337 and 338 name no direction and that the ecliptic is being tested "
            "because it is the only Earth-referenced axis the neighbouring items offer. "
            "Keep that sentence attached to the numbers; split them and the strongest "
            "paragraph becomes the most vulnerable one. The dilemma it sets up has to stay "
            "visible too: either the satellite planes are supposed to be Earth-referenced, "
            "in which case they fail the only test available at 65 and 77 degrees, or they "
            "are not, in which case they carry no Earth content and belong on a different "
            "list. Second, the selection-effect answer must never be asserted in our own "
            "voice alone — section 5 as written attributes it to Pawlowski, Kroupa and "
            "Jerjen's word 'fortunate' and to the 2026 mock-observation paper by "
            "Pawlowski's own group, and it stays that way, because an unattributed appeal "
            "to selection is exactly the move the defender has correctly identified as "
            "cheap. Third, on the Local Group symmetry: do not answer it by minimising it, "
            "because it is real and its authors say no detailed model explains it. Answer "
            "by naming what the symmetry is symmetric about — the Milky Way and Andromeda, "
            "two galaxies whose mutual orbit is the proposed cause — and note that the "
            "arrangement is unchanged under moving the Sun anywhere in the Galactic disc, "
            "which is the operation that would matter if the Earth were the referent."),
    ),

    straw_man=dict(
        identified=True,
        detail=("The items are presented as facts a standard cosmology cannot have, and "
                "the standard cosmology does not predict what they are being scored "
                "against. Nobody in the field expects satellite galaxies to be "
                "isotropically distributed: accretion along filaments, infall in groups, "
                "and the Magellanic system arriving as a pair all produce anisotropy in "
                "ordinary simulations, and the papers on both sides say so. The dispute is "
                "over degree - whether the observed systems are thinner and more coherent "
                "than the simulations manage - which is a quantitative question with "
                "published numbers on both sides. There is also an implied suppression the "
                "record does not support: the anomaly was published in Nature in 2013 and "
                "Science in 2018, its principal critique in Nature Astronomy in 2022, and "
                "the argument has run in the open journals continuously since."),
    ),

    compression=dict(
        assessed=True, drifted=True,
        list_phrasing=("Cluster axes ecliptic. / Dwarf galaxy planes coherence. / "
                       "Satellite alignments."),
        source_wording=("Ibata et al., <em>Nature</em> 493:62 (2013), on the Andromeda plane: "
                        "&ldquo;it has been claimed that the apparently planar distribution of "
                        "satellites is not predicted within standard cosmology &hellip; However, "
                        "other studies dispute this conclusion.&rdquo; And on the alignment "
                        "itself: &ldquo;Intriguingly, the plane we identify is approximately "
                        "aligned with the pole of the Milky Way&rsquo;s disk and is co-planar "
                        "with the Milky Way to Andromeda position vector.&rdquo;"),
        drift_type="scope_widened",
        note=("The comparison here is against the astronomy, because that is where the claim "
              "comes from: no movement text carrying these three items was located, and the "
              "search is written out in the passage block above. Three things change in "
              "transit. <strong>The scope.</strong> The papers make claims about the satellite "
              "systems of named hosts &mdash; the Milky Way, Andromeda, Centaurus&nbsp;A, "
              "NGC&nbsp;4490 &mdash; and about how often systems that flat and that coherent "
              "turn up in simulated analogues. The list states &ldquo;Satellite alignments&rdquo; "
              "as a general property of the universe. <strong>The hedge.</strong> Ibata et al. "
              "print the dispute inside their own abstract, in the sentence quoted; Sawala et "
              "al. restrict their result to the Milky Way in as many words; Seo et al. give a "
              "range rather than a number. Every one of those qualifications is gone by the time "
              "the claim is three words long. <strong>The subject.</strong> This is the deepest "
              "change and the enum has no slot for it: a statistical tension in galaxy formation "
              "becomes an item on a list about the shape and motion of the Earth. We recorded "
              "<em>scope_widened</em> rather than force it into <em>category_shifted</em>, whose "
              "definition is a historical or philosophical claim turned physical; this is a "
              "physical claim about other galaxies turned into a physical claim about this one. "
              "Item 330 is a fourth kind again: &ldquo;Cluster axes ecliptic&rdquo; adds a word "
              "the satellite-plane literature does not use, and no measurement tying cluster "
              "axes to the ecliptic was located in the papers searched for this entry. "
              "<strong>The refutation above answers the source, not the fragment:</strong> it "
              "concedes the anomaly at full strength, quotes the discovery papers on the one "
              "alignment that does involve our position, and puts the weight on what those "
              "structures are referenced to and on why the edge-on case is the case that gets "
              "found. Compare <a href=\"#ARG-E01\">ARG-E01</a>, where the same lane&rsquo;s "
              "ecliptic alignment is also real and also points at the observing system."),
    ),

    verdict_challenge=dict(challenged=False, proposed_verdict=None, reasoning=None),

    people=[],
    related=["E01", "E02", "E04", "E05", "E09", "E12", "E13", "E15", "E17", "D14"],

    sources=[
        dict(label="Ibata et al., “A vast, thin plane of corotating dwarf galaxies orbiting "
                   "the Andromeda galaxy”, Nature 493:62–65 (2013) — 99.998% significance, "
                   ">400 kpc across, <14.1 kpc thick, and the alignment with the Milky Way "
                   "disc pole and the MW–M31 vector",
             url="https://arxiv.org/abs/1301.0446"),
        dict(label="Pawlowski, Pflamm-Altenburg & Kroupa, “The VPOS: a vast polar structure "
                   "of satellite galaxies, globular clusters and streams around the Milky "
                   "Way”, MNRAS 423:1109 (2012) — the DoS normal at (156.4°, −2.2°), RMS "
                   "height 28.9 kpc, extent 10–250 kpc",
             url="https://arxiv.org/abs/1204.5176"),
        dict(label="Pawlowski, Kroupa & Jerjen, “Dwarf galaxy planes: the discovery of "
                   "symmetric structures in the Local Group”, MNRAS 435:1928 (2013) — the "
                   "GPoA normal, the 51° VPOS–GPoA inclination, and the “fortunate” edge-on "
                   "orientation seen from the Milky Way",
             url="https://arxiv.org/abs/1307.6210"),
        dict(label="Kroupa, Theis & Boily, “The great disk of Milky-Way satellites and "
                   "cosmological sub-structures”, A&A 431:517 (2005) — where the "
                   "configuration became a cosmological problem",
             url="https://arxiv.org/abs/astro-ph/0410421"),
        dict(label="Kroupa et al., “Local-Group tests of dark-matter concordance cosmology”, "
                   "A&A 523:A32 (2010) — the disc-of-satellites fit the 2012 normal is taken "
                   "from",
             url="https://arxiv.org/abs/1006.1647"),
        dict(label="Müller, Pawlowski, Jerjen & Lelli, “A whirling plane of satellite "
                   "galaxies around Centaurus A challenges cold dark matter cosmology”, "
                   "Science 359:534 (2018) — 14 of 16 satellites coherent, <0.5% of "
                   "simulated analogues",
             url="https://arxiv.org/abs/1802.00081"),
        dict(label="Müller et al., “The coherent motion of Cen A dwarf satellite galaxies "
                   "remains a challenge for ΛCDM cosmology”, A&A 645:L5 (2021)",
             url="https://www.aanda.org/articles/aa/full_html/2021/01/aa39973-20/aa39973-20.html"),
        dict(label="Cautun et al., “Planes of satellite galaxies: when exceptions are the "
                   "rule”, MNRAS 452:3838 (2015) — flattened subsets are common, and the "
                   "look-elsewhere effect inflates the significance by factors of 30 and 100",
             url="https://arxiv.org/abs/1506.04151"),
        dict(label="Sawala et al., “The Milky Way's plane of satellites is consistent with "
                   "ΛCDM”, Nature Astronomy 7:481–491 (2023) — Leo I/Leo II conjunction, "
                   "0.04% → ~2%, and the scope limit to the Milky Way",
             url="https://arxiv.org/abs/2205.02860"),
        dict(label="Seo, Yoon, Paudel, An & Moon, “A new rarity assessment of the ‘disk of "
                   "satellites’: the Milky Way system is the exception rather than the rule "
                   "in the ΛCDM cosmology”, ApJ 976:253 (2024) — 0.00–3.40%",
             url="https://arxiv.org/abs/2411.18040"),
        dict(label="Sawala, “Planes of satellites, at once transient and persistent” "
                   "(arXiv:2510.01318, v2 19 March 2026) — reconciling the two lifetimes "
                   "rather than closing the question",
             url="https://arxiv.org/abs/2510.01318"),
        dict(label="Crosby, Pawlowski, Müller & Jerjen, “Detectability of satellite planes in "
                   "mock observations of isolated L* galaxies” (arXiv:2602.20447, February "
                   "2026) — detection depends strongly on orientation to the observer; "
                   "edge-on and face-on planes are the ones found",
             url="https://arxiv.org/abs/2602.20447"),
        dict(label="West, De Propris, Einasto, Wen & Han, “Evolution of cluster alignments as "
                   "evidence of large-scale structure formation in the universe”, ApJL (2025) "
                   "— cluster orientations correlated to 200–300 comoving Mpc and to z ≥ 1",
             url="https://arxiv.org/abs/2506.19826"),
        dict(label="Lynden-Bell, “Dwarf galaxies and globular clusters in high velocity "
                   "hydrogen streams”, MNRAS 174:695 (1976) — the earliest note of the "
                   "alignment, half a century before this list",
             url="https://ui.adsabs.harvard.edu/abs/1976MNRAS.174..695L/abstract"),
        dict(label="Jansen et al., “The JWST North Ecliptic Pole Time-Domain Field: field "
                   "selection” (arXiv:1807.05278) — the field is where it is because it is in "
                   "JWST's northern Continuous Viewing Zone",
             url="https://arxiv.org/abs/1807.05278"),
        dict(label="ESA, Euclid survey pages — Euclid Deep Field North at 17:58:55.9 "
                   "+66:01:03.7: “The proximity to the ecliptic pole ensures maximum coverage "
                   "throughout the year”",
             url="https://www.cosmos.esa.int/web/euclid/euclid-survey"),
        dict(label="ROSAT all-sky survey — scanning on great circles perpendicular to the "
                   "ecliptic plane, which is why the deepest exposure and a run of cluster "
                   "papers sit at the North Ecliptic Pole",
             url="https://en.wikipedia.org/wiki/ROSAT_All-Sky_Survey"),
        dict(label="Sungenis & Bennett, Galileo Was Wrong — Internet Archive three-volume "
                   "scan (item galileo-was-wrong-the-church-was-right-sungenis-vol-1-3-"
                   "complete); djvu text searched in full for the satellite-plane literature",
             url="https://archive.org/details/galileo-was-wrong-the-church-was-right-sungenis-vol-1-3-complete"),
    ]),
}
