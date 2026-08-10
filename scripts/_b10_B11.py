# -*- coding: utf-8 -*-
"""
ARG-B11 — "Radar, LiDAR, photogrammetry and sonar assume a plane".  Batch 10, 2026-08-10.

Four items.  Verbatim text, re-fetched from the specimen 2026-08-10:
  217  "Flat radar horizon."
  390  "Photogrammetry planar."
  392  "SAR interferometry."
  400  "Bathymetry sonar straight."

Cluster record on entry: originator=None, year=None, real_source=None, verdict=MISLEADING,
basis "All of these run on ellipsoidal datums. Same convenience-frame error as R08."
The verdict is CHALLENGED here — see `verdict_challenge` and note 7.

Research notes for whoever picks this up next.

1. PROVENANCE: THE SEARCH RAN AND TERMINATED IN A RESULT.  B11 is one of the clusters
   still filed untraced, and it stayed there.  No named author, no cited publication, no
   earlier list carrying these four lines.  Route, so a later reader can correct us:

     * The specimen (withthesun33.com/about-1, re-fetched 2026-08-10).  Heading "435
       Pieces of Evidence The Earth is Not A Spinning Ball" over 461 numbered lines.  No
       citation is attached to these four items or to any other.  Items 217, 390, 392 and
       400 verified character-for-character against the live page on that date, together
       with the whole run 385-402, which is reproduced in the entry.
     * Sungenis & Bennett, GALILEO WAS WRONG Vol. I — Internet Archive item
       `GallileoWasWrong`, full text `Gallileo was wrong_djvu.txt` (462,032 words), and
       Vol. II — item `GalileoWasWrongTheChurchSungenisRobertA.Bennett4276` (284,044
       words, 7th ed. 2013, chs 7-13).  Both downloaded and searched offline 2026-08-10.
       photogrammetr* 0, sonar 0, bathymetr* 0, lidar 0, "synthetic aperture" 0,
       "echo sound"/"echosound" 0, "remote sensing" 0, "aerial photo" 0, "point cloud" 0,
       in BOTH volumes.  radar: 24 hits in Vol. I, 22 in Vol. II — EVERY hit read, and
       every one is either the Shapiro/Wallace Venus time-delay material (ch. 12 in
       Vol. I, ch. 10 in Vol. II), Van Flandern's planetary radar-ranging item, or the
       one sentence about the Department of Defense using radar to map GPS satellites to
       ground reference points.  Not one is about a terrestrial radar horizon.
       interferometr*: 23 and 9 hits, all Michelson-Morley / Miller / Allais / Sagnac /
       VLBI.  None is synthetic-aperture.
     * Dubay, 200 PROOFS EARTH IS NOT A SPINNING BALL — item
       `200ProofsEarthIsNotASpinningBall`, full text searched 2026-08-10.  ZERO hits for
       every one of radar, sonar, lidar, photogrammetr*, bathymetr*, interferometr*,
       "synthetic aperture", "remote sensing".  The largest modern flat-earth proof list
       does not reach this material at all.
     * The Flat Earth Society wiki FAQ (wiki.tfes.org/Flat_Earth_-_Frequently_Asked_
       Questions), read end to end 2026-08-10: none of these terms located in it.
     * FlatEarth.ws, the debunking site that catalogues circulating claims, has a radar
       topic index with three articles.  Exactly one flat-earth radar claim is described
       there, and IT IS A DIFFERENT CLAIM: that marine radars are marketed with maximum
       ranges exceeding the distance to the horizon ("Marine Radar", 9 April 2020).  No
       originator is named in it.  Useful anyway — see note 3.
   Rowbotham and Carpenter were NOT searched and should not be: radar is 1935+, sonar
   1912+, photogrammetric aerotriangulation 1920s+, SAR 1951+, InSAR 1974+.  A Victorian
   ancestor is not a live hypothesis for these four items and looking for one would be
   theatre.  What IS worth recording is the SHAPE of the run they sit in: 385-402 walks
   through applied geoscience by discipline — pipelines, rail, highways, wind farms,
   drone RTK, photogrammetry, LiDAR, SAR, seismology, infrasound, mining, architecture,
   skyscrapers, pendulum clocks, GNSS, bathymetry — one line each, no predicates, no
   citations.  That is a list grown by enumerating professions, not by citing anybody.

2. `pre_modern` WAS CONSIDERED AND REJECTED, for the obvious reason: the instruments
   postdate the movement rather than predating it.  Origin stays UNTRACED.  Nothing in
   this entry credits an originator, and the untraceable block says in terms that no
   author found means we did not find one.

3. ITEM 217 HAS TWO READINGS AND THE ENTRY ANSWERS BOTH.  "Flat radar horizon." is three
   words.  Reading (a): the radar horizon is a flat-plane phenomenon / radar sees a
   plane.  Reading (b), the one FlatEarth.ws documents as actually circulating: radar
   detects targets further away than a curved Earth should allow.  Do NOT quietly pick
   one.  (a) is answered by the horizon formula containing R; (b) by the difference
   between an advertised signal range and a horizon-limited detection range.  Both are in
   section 1 of the refutation.

4. THE KERNEL, AND IT IS THE BEST ONE AVAILABLE.  Every one of these four disciplines
   really does contain a named, documented, daily-used flat-Earth approximation, and a
   defender who knows the fields can name all four:
     * radio propagation: the PLANE EARTH LOSS model (two-ray ground reflection), in
       every RF textbook;
     * photogrammetry: the collinearity equations are written in a 3-D Cartesian frame,
       with earth curvature entering afterwards as a CORRECTION to a planar model;
     * InSAR: a processing step called FLAT EARTH PHASE REMOVAL, sometimes "flattening";
     * shallow-water acoustics: the isovelocity / straight-ray assumption.
   So the surface bust — "obviously they account for curvature, this is silly" — loses to
   a citation, and must not be used.  The KERNEL answer is that each discipline also
   publishes the LIMIT of its own flat approximation, and the limit is computed from R.
   The single cleanest statement of this in the literature is Yang, Molisch, Ekman, Røste
   & Berbineau, "A Round Earth Loss Model and Small-scale Channel Properties for Open-Sea
   Radio Propagation", IEEE Trans. Veh. Technol. (2019): "the PEL assumption of a plane
   earth surface inherent in this model is not fulfilled for maritime radio links at
   larger distances ... This is due to the fact that the diffraction loss caused by the
   earth curvature and sea roughness can not be ignored."  The RF literature has a plane
   earth model AND a round earth model, and published the second because the first fails
   at range.  That is the whole argument in one citation.

5. THE SINGLE BEST FACT ON THIS CLUSTER, AND IT IS ITEM 392's OWN VOCABULARY.  In SAR
   interferometry the phrase "flat earth" names a thing you SUBTRACT.  ESA's own
   processing documentation for the SNAP/jLinda Interferogram operator defines it: the
   flat-earth phase is "the phase present in the interferometric signal due to the
   curvature of the reference surface"; the reference system is "for now only WGS84
   supported, which the reference system used by all space-borne SAR systems"; and
   without the subtraction "the formed interferogram will still have the fringes caused
   by the earth curvature".  Wikipedia's InSAR article summarises the same step as "the
   interferometric phase due to the curvature of the Earth is removed, a process referred
   to as flattening."  DO NOT REST THE ARGUMENT ON THE NAME — a defender will correctly
   call that a pun.  Rest it on the DEFINITION, which is an ellipsoid, and on the fact
   that the fringes are observed and then modelled away.
   Two further SAR facts, both checked:
     * The Range-Doppler geolocation model is THREE equations — slant range, Doppler,
       and the Earth ellipsoid (x²/R_e² + y²/R_e² + z²/R_p² = 1).  Wang, Huang, Dong et
       al., Chinese Science Bulletin 57(2-3), 2012, print it as their Eq. (3).  You
       cannot solve for a SAR pixel's ground position without an ellipsoid in the system.
     * Spaceborne SAR steers its own attitude to cancel the Doppler the Earth's rotation
       puts into the return.  Zhao & Wei, Progress In Electromagnetics Research Letters
       63 (2016): "the Doppler centroid is not zero in the conventional broadside mode
       ... due to the earth rotation and eccentricity of the orbit."  The technique is
       total zero-Doppler steering (Fiedler, Börner, Mittermayer & Krieger, IEEE GRSL,
       2005; developed for TerraSAR-X).  Do not assert a specific Sentinel-1 steering law
       — that was not verified here.

6. ARITHMETIC, ALL RECOMPUTED 2026-08-10, R = 6371 km unless stated.
   (a) Radar horizon.  d = sqrt(2kRh); k = 4/3 gives 4.122 km per sqrt(metre), i.e. the
       textbook d(km) = 4.12 sqrt(h(m)); k = 1 gives 3.57.  Cross-checked against the two
       worked examples in the Radar horizon article: 1 mile (1609 m) -> 165 km against
       its "102 miles", 75 ft (23 m) -> 19.8 km against its "12 miles".  Both match.
   (b) Weather-radar beam centre, 4/3-earth model,
       h = sqrt(r² + (ka)² + 2 r ka sin θ) − ka, ka = 8494.7 km, θ = 0.5°:
       0.58 km at 50 km, 1.46 km at 100 km, 2.63 km at 150 km, 5.12 km at 230 km
       (= 124 nmi, the WSR-88D's quantitative precipitation range).  Quote 5.1 km, not
       5.5 — 5.5 is what you get including tower height and beam half-width, and this
       entry only derived the centreline.
   (c) Photogrammetric earth-curvature displacement, d = r³(H − Z_P)/(2c²R) with
       R = 6372.2 km (the sphere approximation used in the analytical-photogrammetry
       notes this formula is taken from).  H − Z = 1500 m, c = 100 mm, r = 150 mm:
       39.7 µm in the image, 0.60 m on the ground at 1:15,000, about 8 pixels at a 5 µm
       pitch.  DERIVED A SECOND WAY as a check: ground radial 2250 m, curvature drop
       2250²/2R = 0.397 m, relief displacement r·h/H = 39.7 µm.  Identical.  At the true
       corner of a 230 mm frame (r = 162.6 mm) it is 50.6 µm and 0.76 m.
   (d) Spherical excess of one arcsecond = a triangle of 197 km² (ε = A/R²).  Arc minus
       chord ≈ s³/24R²: 6.2 mm at 18.2 km, 8.2 mm at 20 km, 9.9 mm at 21.3 km.  These
       are the numbers that define where plane surveying stops.
   (e) Bathymetry, and this one goes AGAINST us, which is why it is in the entry.
       Curvature drop across a multibeam swath: 0.0003 m at 60 m half-swath (a 30 m-deep
       coastal survey), 0.02 m at 500 m, 7.8 m at 10 km.  IHO S-44 6.1.0 TVU =
       sqrt(a² + (b·d)²): Order 1a (a = 0.5, b = 0.013) allows 1.39 m at 100 m depth;
       Order 2 (a = 1.0, b = 0.023) allows 115 m at 5000 m.  So earth curvature is
       genuinely negligible inside one swath, at every order, and the entry says so.
       The bathymetry answer is refraction and the vertical datum, NOT curvature.
   (f) Refraction, to show the size of the term that ISN'T negligible.  Snell in the
       water column, sin θ / c constant.  A 1% error in the sound-speed profile (15 m/s;
       about 3 °C of temperature error, since the Mackenzie equation's linear term is
       4.591 T) turns a 60° outer beam into 61.0°, moves the sounding 7.3 m across-track
       at 100 m depth, and puts 1.0 m of error into a budget that allows 1.39 m.  One
       systematic eats 72% of an Order 1a allowance.

7. THE VERDICT.  MISLEADING is challenged, not written around.  Proposed:
   SELF-CONTRADICTED, on the C05/C09/C10 precedent — the list runs two proofs that
   cancel.  Here they are ADJACENT: item 390 "Photogrammetry planar." and item 391
   "LiDAR ECEF." are consecutive lines, and ECEF/WGS84 is an ellipsoidal, rotating frame.
   Better still, the cancellation is available INSIDE ONE ITEM: item 392's own technique
   contains a planar term that exists only as something computed from the WGS84 ellipsoid
   and subtracted.  That form does not depend on cross-item adjacency and survives the
   obvious objection ("different instruments").  Fallback if a reviewer reads
   SELF-CONTRADICTED as reserved for the fact-denial tier: REFUTED, because two of the
   four items — 217 and 400 — are false as descriptions of the instruments they name,
   and are contradicted by specific measurements (the radar horizon relation; measured
   sound-speed profiles).  MISLEADING is defensible for 390 and 392 and is not defensible
   for 217 and 400, and the challenge says exactly that rather than overclaiming.
   clusters.py NOT touched.

8. DEFECTS IN OUR OWN RECORD, reported up in `record_problems`, NOT edited here (this
   agent owns one file), and deliberately NOT written into the published prose — rule 4
   of the curmudgeon sweep: never ship a to-do as a finding.
     * The cluster NAME says "Radar, LiDAR, photogrammetry and sonar".  No LiDAR item is
       assigned to B11; item 391 "LiDAR ECEF." is assigned to R08, correctly.  The name
       promises an instrument the cluster does not contain.
     * The basis line "All of these run on ellipsoidal datums" is true of 390 and 392 and
       is not the answer to 217 or 400.  A radar horizon is not a datum question and a
       sonar ray path is not a datum question.  The refutation therefore opens by saying
       which two items the datum answer covers, without characterising our own record.
     * originator/originator_work/year/real_source are all None, which is correct on this
       pass and should stay None.  Do not fill real_source with "WGS84, ITRF" by analogy
       with R08; that would smuggle a source into a cluster that has none.

9. TRAPS AVOIDED, recorded because each nearly reached the page.
   * "Radar proves the Earth is round because radar horizons exist."  Too fast: ducting
     and anomalous propagation really do produce over-horizon detections, routinely.  The
     defensible form, used in the text, is that ducting is itself an atmospheric-
     refraction effect whose standard engineering model is a MODIFICATION OF THE
     EFFECTIVE EARTH RADIUS — the 4/3 factor, and larger k for a duct — so it is
     parameterised by R rather than a rival to it.
   * Do not write that the flat-earth phase is "the biggest term in the interferogram" or
     put a fringe count on it.  The fringe count depends on baseline, wavelength and
     look-angle span, none of which is fixed for these items, and nothing here needs it.
   * Do not lean on the SNAP note that a degree-5 polynomial suffices for a 100x100 km
     scene "and higher degree for long-swath scenes" as if it proved curvature.  It is
     consistent with curvature and it is not a demonstration; the definition already
     names the reference surface, so nothing rests on the polynomial degree.
   * Do NOT say the discipline of plane surveying is a mistake.  It is not, it is correct
     within a published tolerance, and B06 already owns that ground.  Cross-linked.
   * The "afternoon effect" is often told as a WWII story with no citation.  There is a
     real one: Iselin & Woodcock, "Preliminary report on the prediction of 'afternoon
     effect'", Woods Hole Oceanographic Institution, 1942, whose abstract reads "With
     moderate or light winds and a clear sky the diurnal heating which occurs near the
     sea surface can cause a serious reduction in the range of submarine detection."
     Use that, not the folklore.
"""

ENTRY = {

"B11": dict(

    tldr=("Radar horizons are not flat: the standard range formula, d ≈ 4.12√h kilometres, is "
          "the horizon of a curved Earth with refraction already folded in, and airborne early "
          "warning and over-the-horizon radar are two equipment categories built to defeat it. "
          "Sonar rays are not straight either — they bend by Snell's law through the "
          "sound-speed profile, which is why survey ships stop to lower a probe. Aerial "
          "photogrammetry really does work in a plane, and ships with a curvature correction "
          "worth more than half a metre on the ground at the edge of an ordinary frame. And in "
          "SAR interferometry the “flat-earth phase” is defined as the signal produced by the "
          "curvature of the reference surface, computed on the WGS 84 ellipsoid and then "
          "subtracted."),

    passage=None,

    untraceable="""<p>There is no original to quote, and as at <a href="#ARG-C08">ARG-C08</a> and <a href="#ARG-C09">ARG-C09</a> that is a conclusion rather than a shrug. The specimen carries no citation for these four items &mdash; it carries none for any of the 461 &mdash; so the search ran outward through the literature the rest of the list demonstrably draws on. Here is the route, and where it stopped.</p>

<p><strong>The movement&rsquo;s largest work reaches none of these four instruments.</strong> The full text of <em>Galileo Was Wrong</em> Vol.&nbsp;I (Internet Archive item <code>GallileoWasWrong</code>, 462,032 words) and Vol.&nbsp;II (item <code>&hellip;Bennett4276</code>, seventh edition, 2013, chapters&nbsp;7&ndash;13, 284,044 words) were downloaded and searched offline on 2026-08-10. &ldquo;Photogrammetry&rdquo;, &ldquo;sonar&rdquo;, &ldquo;bathymetry&rdquo;, &ldquo;LiDAR&rdquo;, &ldquo;synthetic aperture&rdquo;, &ldquo;echo sounding&rdquo; and &ldquo;remote sensing&rdquo; are not located in the text of either volume as searched. &ldquo;Radar&rdquo; is there &mdash; 24 occurrences in Vol.&nbsp;I and 22 in Vol.&nbsp;II &mdash; and every one was read. They fall into four groups. Most are the Shapiro Venus time-delay experiment and Bryan Wallace&rsquo;s challenge to it. Then Van Flandern&rsquo;s planetary radar-ranging item; a single sentence about the Department of Defense using radar to map GPS satellites to ground reference points; and contents-page and bibliography lines pointing back at the first group. One occurrence in Vol.&nbsp;I is neither: it is the figure of speech &ldquo;not merely a blip on the radar screen&rdquo;. So: planetary radar, satellite tracking, and a metaphor. A terrestrial radar horizon is not among them. &ldquo;Interferometry&rdquo; is there too, 23 and 9 times, and every occurrence located is Michelson&ndash;Morley, Miller, Allais, Sagnac or very-long-baseline &mdash; none of it synthetic-aperture.</p>

<p><strong>The largest modern flat-earth proof list reaches them even less.</strong> The full text of Dubay&rsquo;s <em>200 Proofs Earth Is Not a Spinning Ball</em> was searched the same way on the same day, for radar, sonar, LiDAR, photogrammetry, bathymetry, interferometry, synthetic aperture and remote sensing. The count for every one of those terms in that text is zero.</p>

<p><strong>Two more places a claim of this shape would live.</strong> The Flat Earth Society wiki&rsquo;s <em>Frequently Asked Questions</em> was read end to end on 2026-08-10; none of these terms is located in it. And FlatEarth.ws &mdash; a debunking site, but a useful census of what actually circulates, because it writes up claims in order to answer them &mdash; carries a radar topic index of three articles. Exactly one flat-earth radar claim is described there, and <em>it is a different claim from ours</em>: that marine radar sets are marketed with maximum ranges far exceeding the distance to the horizon (&ldquo;Marine Radar&rdquo;, 9&nbsp;April 2020). No originator is named for it. It is answered in section&nbsp;1 below anyway, because it is the most plausible thing item&nbsp;217 could mean.</p>

<p><strong>Why nothing older was searched.</strong> Rowbotham and Carpenter are the ancestors for most of lane&nbsp;B, and they are not candidates here: radar dates from the 1930s, sonar from 1912, photogrammetric aerotriangulation from the 1920s, synthetic-aperture radar from 1951 and interferometric SAR from 1974. Hunting a Victorian ancestor for these four lines would be theatre. What is worth recording instead is the shape of the passage they sit in. Items&nbsp;385 to&nbsp;402 run: pipelines, railroads, highways, wind farms, drone RTK, photogrammetry, LiDAR, SAR, seismology, volcano infrasound, mining surveys, architecture, skyscrapers, pendulum clocks, GNSS pseudorange, bathymetry, ship optical range, harbour mirage charts. Eighteen consecutive lines, one per profession, most of them without a verb. That is a list grown by enumerating disciplines rather than by citing anyone, and it is the clearest specimen of the mechanism on the whole page.</p>

<p><strong>An honest note on our limits.</strong> <em>No author found</em> means we did not find one, not that none exists. Four noun phrases can enter circulation through a livestream, a comment thread, a slide or an image caption that leaves nothing searchable. A reader who can point us at someone who actually argued from radar, photogrammetry, SAR or sonar to a flat Earth &mdash; in print, on air, anywhere datable &mdash; will improve this entry, and we will publish the correction.</p>""",

    steelman=dict(
        description="""<p><strong>SURFACE (weak &mdash; do not use).</strong> &ldquo;Obviously these instruments account for curvature; the claim is silly.&rdquo; This loses, and it loses to citations, because a flat Earth is a named, documented, daily-used object in all four of these fields. Anyone who opens with the easy bust will be handed four references and will deserve it.</p>

<p><strong>DEEPER.</strong> Working in a local tangent plane is not a shortcut, it is the professional standard over short baselines, and it has a name: <em>plane surveying</em>, as distinct from geodetic surveying. Over the extent of one job the plane is not merely convenient, it is accurate. A defender who says this has said something every practitioner agrees with.</p>

<p><strong>KERNEL.</strong> The strongest form names the four objects individually, and every one of them is real. In radio propagation there is a standard model called <strong>plane earth loss</strong> &mdash; the two-ray ground-reflection model, in every RF textbook, which treats the ground as an infinite plane. In photogrammetry the collinearity equations that underpin every bundle adjustment are written for a three-dimensional Cartesian space, with the Earth&rsquo;s curvature entering <em>afterwards</em>, as a correction applied to a model that did not contain it. In SAR interferometry there is a processing step whose name is <strong>flat-earth phase removal</strong>. In shallow-water acoustics there is the isovelocity assumption, under which sound is taken to travel in straight lines. So the honest version of this cluster is not &ldquo;these instruments secretly know the Earth is round&rdquo; versus &ldquo;they assume a plane&rdquo;. It is: <em>the flat Earth is a working object in all four disciplines, it is in the textbooks under that description, and the list did not invent it.</em></p>""",
        why_it_doesnt_save_claim="""<p>Because each discipline publishes the <strong>limit</strong> of its own flat approximation, and the limit is computed from the Earth&rsquo;s radius. A truncated series is not a rival to the function it was truncated from.</p>

<p>The cleanest statement of this is in the radio literature, where both models exist side by side and the second was published because the first fails. Yang, Molisch, Ekman, R&oslash;ste and Berbineau, proposing a <em>Round Earth Loss</em> model for open-sea propagation, state the reason directly: &ldquo;the PEL assumption of a plane earth surface inherent in this model is not fulfilled for maritime radio links at larger distances &hellip; This is due to the fact that the diffraction loss caused by the earth curvature and sea roughness can not be ignored.&rdquo; Plane earth loss is real, taught, and bounded &mdash; and what bounds it is the curvature.</p>

<p>The same shape holds in each of the other three, and section by section the refutation gives the numbers: the photogrammetric planar model is corrected by a term of the form <em>r</em>&sup3;(<em>H</em>&nbsp;&minus;&nbsp;<em>Z</em>)/2<em>c</em>&sup2;<em>R</em>, which has the Earth&rsquo;s radius in the denominator and is worth about 40&nbsp;micrometres at the corner of an ordinary aerial frame; the flat-earth phase in InSAR is <em>defined</em> as the phase due to the curvature of the reference surface and is computed on WGS&nbsp;84; and the straight-ray assumption in sonar is what produces the artefacts hydrographers call smiles and frowns, which is why they measure the profile instead. In every case the flat model is derived from the round one, carries an error term proportional to 1/<em>R</em>, and is used inside the range where that term is smaller than the tolerance. You cannot know where a plane stops working without knowing the radius of the thing it is approximating.</p>"""),

    refutation="""<p><strong>What this cluster covers, stated first, because two of its four items are not the same kind of claim as the other two.</strong> The four are item&nbsp;217 &ldquo;Flat radar horizon.&rdquo;, item&nbsp;390 &ldquo;Photogrammetry planar.&rdquo;, item&nbsp;392 &ldquo;SAR interferometry.&rdquo; and item&nbsp;400 &ldquo;Bathymetry sonar straight.&rdquo; The datum answer &mdash; that these systems run on an ellipsoidal reference &mdash; is the right answer to 390 and 392, and it is scored in its general form at <a href="#ARG-R08">ARG-R08</a>. It is <em>not</em> the answer to 217 or 400, because a radar horizon is not a datum question and a sonar ray path is not a datum question. Those two need different answers and get them below.</p>

<p><strong>And one concession before anything else, because it governs how the rest should be read.</strong> Items&nbsp;390 and&nbsp;392 are noun phrases with no predicate. &ldquo;SAR interferometry.&rdquo; asserts nothing at all on its own; the claim is supplied by the page heading these lines sit under, <em>&ldquo;435 Pieces of Evidence The Earth is Not A Spinning Ball&rdquo;</em>. So what follows answers the strongest reading available &mdash; that these techniques model the ground as a plane and thereby show it is one &mdash; and says so out loud rather than pretending the items argued it.</p>

<h4>1. The radar horizon has a formula, and the Earth&rsquo;s radius is in it</h4>

<p>Take reading (a) first: that radar sees a plane. The distance at which a radar loses a low target is standard engineering, not a controversy. With the Earth&rsquo;s radius <em>R</em> and antenna height <em>h</em>, the geometric horizon is <em>d</em>&nbsp;=&nbsp;&radic;(2<em>Rh</em>); the working version folds in atmospheric refraction by replacing <em>R</em> with an effective <sup>4</sup>&frasl;<sub>3</sub><em>R</em>&nbsp;=&nbsp;8,495&nbsp;km, giving the number every radar text carries: <em>d</em>(km)&nbsp;&asymp;&nbsp;4.12&nbsp;&radic;<em>h</em>(m). Recomputed here 2026-08-10: &radic;(2&nbsp;&times;&nbsp;<sup>4</sup>&frasl;<sub>3</sub>&nbsp;&times;&nbsp;6.371&nbsp;&times;&nbsp;10<sup>6</sup>)&nbsp;=&nbsp;4,122, so 4.12 with <em>h</em> in metres and <em>d</em> in kilometres; the unrefracted constant is 3.57. A 10&nbsp;m mast reaches 13&nbsp;km, a 23&nbsp;m one 19.8&nbsp;km, an aircraft at 10&nbsp;km reaches 412&nbsp;km. The whole quantity is a curvature; set the curvature to zero and the formula returns an infinite horizon, which is not what anybody measures.</p>

<p>This is not a textbook curiosity, it is a daily operational constraint. The United States weather-radar network is limited by it every hour: as the National Weather Service puts it, &ldquo;Earth curvature and standard refraction dictate that the beam becomes more elevated above the surface with increasing range&rdquo;, so the radar <em>overshoots</em> shallow precipitation at distance, and &ldquo;overshooting of precipitation by the radar beam often produces the largest errors, usually causing precipitation underestimation.&rdquo; The 4/3-earth beam-height relation puts a 0.5&deg; beam at 0.58&nbsp;km above ground at 50&nbsp;km, 1.46&nbsp;km at 100&nbsp;km and <strong>5.1&nbsp;km at 230&nbsp;km</strong> &mdash; recomputed here. The forecaster in the next county cannot see the rain falling under that beam, and the reason has a radius in it.</p>

<p>Two entire equipment categories exist because of this limit. Airborne early warning aircraft carry a radar up a tower fifty times higher than any mast can be built, for no other reason. And over-the-horizon radar &mdash; the Australian Jindalee network, with an official range of 3,000&nbsp;km &mdash; abandons microwaves altogether and bounces high frequencies off the ionosphere, because, in the reference literature&rsquo;s own words, microwave radar propagation &ldquo;generally limits the detection range of radar systems to objects on their horizon &hellip; due to the curvature of the Earth.&rdquo; Nations do not fund a second physics for a limit that does not exist.</p>

<p>Now reading (b), which is the version documented as actually circulating: that marine radars are advertised with ranges far beyond the horizon, so the horizon cannot be real. The advertised figure is a <em>signal</em> range &mdash; how far the transmitter can put usable power and still resolve a return &mdash; not a detection range for a surface target. Recomputed: a set with its scanner 20&nbsp;m up, looking at a ship whose superstructure reaches 30&nbsp;m, has a radar horizon of 4.12(&radic;20&nbsp;+&nbsp;&radic;30)&nbsp;=&nbsp;41&nbsp;km, about 22&nbsp;nautical miles. That set may be sold as a 96-mile radar, and it will indeed paint a mountain or a rain cell at 96 miles, because those are tall. It will not paint a hull. Every navigation course teaches the distinction, and the ranges at which it fails are the ranges the formula predicts.</p>

<p><strong>The honest qualification, which a defender will otherwise supply.</strong> Radar does routinely detect targets beyond the 4/3 horizon, through ducting and other anomalous propagation, and sometimes by hundreds of kilometres. That is real. It also does not help, because ducting is an atmospheric-refraction phenomenon whose standard engineering treatment is <em>a further modification of the effective Earth radius</em> &mdash; the 4/3 factor is the standard-atmosphere case, a duct is a larger <em>k</em>, and a sub-refractive layer is a smaller one. Anomalous propagation is parameterised by the curvature it bends around, not offered as an alternative to it.</p>

<h4>2. Photogrammetry: the planar model is real, and it ships with a curvature term</h4>

<p>Item&nbsp;390 is true as far as it goes, and that is the interesting part. Analytical photogrammetry does work in Cartesian space: the collinearity condition that ties an image point to a ground point is written for a three-dimensional Cartesian frame at both ends, and over one frame that frame is effectively flat. The discipline then applies a correction, and the correction is published in the same chapter as the model. The radial displacement of an image point caused by the Earth&rsquo;s curvature is</p>

<p style="margin-left:1.5em"><em>d</em><sub>earth</sub> = <em>r</em>&sup3;(<em>H</em> &minus; <em>Z</em><sub>P</sub>) / (2<em>c</em>&sup2;<em>R</em>)</p>

<p>with <em>r</em> the radial distance in the image, <em>c</em> the principal distance, <em>H</em>&nbsp;&minus;&nbsp;<em>Z</em><sub>P</sub> the height above the ground point, and <em>R</em> the Earth&rsquo;s radius, taken in the standard treatment as a sphere of 6,372.2&nbsp;km. Note where <em>R</em> sits: in the denominator, so the correction vanishes only as the radius goes to infinity.</p>

<p>Put ordinary numbers in it. A survey flown 1,500&nbsp;m above the ground with a 100&nbsp;mm lens, at a point 150&nbsp;mm out from the principal point: <em>d</em>&nbsp;=&nbsp;39.7&nbsp;micrometres in the image &mdash; about eight pixels on a 5&nbsp;&micro;m sensor &mdash; which at 1:15,000 is <strong>0.60&nbsp;m on the ground</strong>. At the true corner of a 230&nbsp;mm frame it is 50.6&nbsp;&micro;m and 0.76&nbsp;m. That was derived here a second way as a check, and the two agree exactly: the ground radius is 2,250&nbsp;m, the curvature drop over 2,250&nbsp;m is 2250&sup2;/2<em>R</em>&nbsp;=&nbsp;0.397&nbsp;m, and the relief displacement of a 0.397&nbsp;m height change at that position is 39.7&nbsp;&micro;m. The curvature is not a rounding error hidden in the software; it is a systematic tilt of the whole frame outward, larger &mdash; as the standard treatment notes in as many words &mdash; than the atmospheric-refraction correction sitting next to it. A photogrammetrist who left it out would deliver a block that fails its own check points.</p>

<h4>3. SAR interferometry: &ldquo;flat earth&rdquo; is the name of the thing you subtract</h4>

<p>Item&nbsp;392 names a technique in which the phrase &ldquo;flat earth&rdquo; is genuinely standard vocabulary &mdash; and it is the name of an artefact, computed from an ellipsoid, and removed. The argument here is not the pun; it is the definition. ESA&rsquo;s own processing documentation for the interferogram operator states it: the flat-earth phase is <em>&ldquo;the phase present in the interferometric signal due to the curvature of the reference surface&rdquo;</em>; the reference system is <em>&ldquo;for now only WGS84 supported, which the reference system used by all space-borne SAR systems&rdquo;</em>; and if you skip the step, <em>&ldquo;the formed interferogram will still have the fringes caused by the earth curvature, and could hamper further interferometric processing and analysis.&rdquo;</em> The reference summary of InSAR says the same in one line: &ldquo;the interferometric phase due to the curvature of the Earth is removed, a process referred to as flattening.&rdquo; Those fringes are observed. They are counted. They are then modelled away using a rotational ellipsoid with a specified flattening, and what is left over is the topography and the ground motion the mission was flown to measure.</p>

<p>Two further things are true of every spaceborne SAR image, and neither is optional.</p>

<p><strong>The ellipsoid is one of the three equations.</strong> Locating a SAR pixel on the ground is a simultaneous solution of a slant-range equation, a Doppler equation, and an Earth-model equation &mdash; and the third one is the ellipsoid, printed in the geolocation literature as <em>x</em>&sup2;/<em>R</em><sub>e</sub>&sup2;&nbsp;+&nbsp;<em>y</em>&sup2;/<em>R</em><sub>e</sub>&sup2;&nbsp;+&nbsp;<em>z</em>&sup2;/<em>R</em><sub>p</sub>&sup2;&nbsp;=&nbsp;1 with an equatorial radius and a distinct polar radius. Remove the third equation and the system is underdetermined: the range and Doppler conditions alone place the target on a circle, and it is the Earth model that picks the point. There is no SAR image whose pixels have ground coordinates without an oblate spheroid in the solver.</p>

<p><strong>And the spacecraft physically turns to cancel the Earth&rsquo;s rotation.</strong> A side-looking radar in a polar orbit sees a Doppler shift from the ground it is illuminating, and part of that shift is the ground moving underneath: as the SAR attitude-control literature puts it, &ldquo;the Doppler centroid is not zero in the conventional broadside mode &hellip; due to the earth rotation and eccentricity of the orbit.&rdquo; The standard fix, developed for TerraSAR-X and known as total zero-Doppler steering, is a yaw manoeuvre computed to null it. The satellite is aimed slightly off square, continuously, at an angle derived from &omega;<sub>&oplus;</sub>. Set the Earth&rsquo;s rotation to zero and the steering law has nothing to correct.</p>

<h4>4. Bathymetry: the rays are the problem, and the curvature is not</h4>

<p><strong>Start with the part that goes against us, because it does.</strong> Over the width of one multibeam swath the Earth&rsquo;s curvature is negligible, and no amount of rhetoric changes that. Recomputed here: the curvature drop across a 60&nbsp;m half-swath &mdash; a typical coastal survey in 30&nbsp;m of water &mdash; is three tenths of a millimetre; at 500&nbsp;m it is 2&nbsp;cm; it only reaches 7.8&nbsp;m at a 10&nbsp;km half-swath in the deep ocean, where the IHO&rsquo;s Order&nbsp;2 vertical allowance at 5,000&nbsp;m depth is 115&nbsp;m. So anyone answering item&nbsp;400 by saying &ldquo;but the sea floor curves&rdquo; is answering with a term far below the noise. That is not the answer.</p>

<p><strong>The answer is that the word in the item is &ldquo;straight&rdquo;, and sonar rays are not.</strong> Sound speed in the sea is not a constant: the Mackenzie equation&rsquo;s linear term is 4.591<em>T</em>, so roughly 4.6&nbsp;m/s per degree Celsius, with further dependence on salinity and pressure. A ray crossing a layered water column therefore refracts, by Snell&rsquo;s law, exactly as light does entering glass. This is not a subtlety at the edge of the error budget; it is the discipline&rsquo;s principal systematic, and it has names. Get the profile wrong and the swath develops what hydrographers call <em>smiles</em> and <em>frowns</em> &mdash; &ldquo;two classic error patterns in multibeam data, where the seafloor appears to curve up or down at the edges of the swath&rdquo;. Note what that means: assuming straight rays does not flatten the sea floor, it <strong>bends</strong> it, into a curvature that is not there.</p>

<p>The size of it, recomputed here. A 1% error in the sound-speed profile is about 15&nbsp;m/s, which is roughly three degrees of temperature. By Snell&rsquo;s law that turns a beam launched at 60&deg; into one travelling at 61.0&deg;, displaces the sounding 7.3&nbsp;m across-track in 100&nbsp;m of water, and puts about 1.0&nbsp;m of vertical error into a budget that allows 1.39&nbsp;m at that depth for an IHO Order&nbsp;1a survey. One systematic, from one un-measured profile, eats 72% of the entire allowance. This is why survey vessels stop, lower a sound-velocity probe, and repeat it as conditions change, and why permanent sensors are fitted at the transducer head.</p>

<p>It has a documented history, too. The refraction of sound by a warm surface layer was identified during the Second World War as the <em>afternoon effect</em>, in which sonar detection ranges collapsed on calm sunny days: Iselin and Woodcock reported for Woods Hole in 1942 that &ldquo;with moderate or light winds and a clear sky the diurnal heating which occurs near the sea surface can cause a serious reduction in the range of submarine detection.&rdquo; The response was the bathythermograph &mdash; an instrument invented for no other purpose than to measure the profile that bends the rays. Straight-line sonar is not the assumption of the field. It is the failure mode the field was built around.</p>

<p>And the vertical reference is not a plane either. Modern hydrography is positioned by GNSS in a three-dimensional geodetic frame and reduced through a separation model: NOAA&rsquo;s ellipsoidally referenced surveys describe geoid undulation as &ldquo;the outward-normal distance from the reference ellipsoid&rdquo;, and the chart datum a sounding is finally referred to is derived from tidal and gravimetric surfaces, not from a level plane. That half of the answer <em>is</em> the datum argument, and it belongs with 390 and 392.</p>

<h4>5. Why the plane is allowed, and what allowing it costs the argument</h4>

<p>Nothing above says a practitioner is wrong to work in a plane. The opposite: the plane is correct, within a tolerance, and the discipline states the tolerance. Two numbers define it, both recomputed here. The spherical excess of a triangle &mdash; the amount by which its angles exceed 180&deg; &mdash; is its area divided by <em>R</em>&sup2;, so a triangle of 197&nbsp;km&sup2; has an excess of one arcsecond. And a line on the Earth&rsquo;s surface exceeds its own chord by roughly <em>s</em>&sup3;/24<em>R</em>&sup2;, which is 8&nbsp;mm at 20&nbsp;km and 6&nbsp;mm at 18&nbsp;km. Those are the numbers that separate plane surveying from geodetic surveying, and both of them have <em>R</em> in them.</p>

<p>That is the whole structure of the answer. A flat-Earth approximation is a truncated series. It is the first term of an expansion whose next term is proportional to 1/<em>R</em>, and you use it precisely where that next term is smaller than what you are trying to measure. Every one of the four disciplines named here does that, and every one of them publishes the crossover. The claim needs the plane to be the <em>model</em>. What the textbooks contain is the plane as an <em>approximation with a stated radius of validity</em> &mdash; and you cannot state the radius of validity without the radius. The surveying form of this argument is scored at <a href="#ARG-B06">ARG-B06</a>, and the engineering form &mdash; canals, rail, pipelines &mdash; at <a href="#ARG-B05">ARG-B05</a>.</p>

<h4>6. The list cancels itself, two lines apart</h4>

<p>Read the specimen&rsquo;s own sequence. Item&nbsp;390 is &ldquo;Photogrammetry planar.&rdquo; Item&nbsp;391, the next line, is &ldquo;LiDAR ECEF.&rdquo; Item&nbsp;389, the line before, is &ldquo;Drone RTK Earth grid.&rdquo; ECEF is Earth-Centred, Earth-Fixed: a frame whose datum is the WGS&nbsp;84 ellipsoid and whose transformation to an inertial frame contains the Earth&rsquo;s rotation rate as an explicit term &mdash; the point scored at <a href="#ARG-R08">ARG-R08</a>. Airborne LiDAR and aerial photogrammetry are commonly flown on the same aircraft, on the same GNSS/inertial trajectory, adjusted against the same control and delivered in the same coordinate reference system. The list offers the planar character of one and the ellipsoidal frame of the other as two separate proofs of the same conclusion, on consecutive lines.</p>

<p>And the cancellation does not need two items. It is available inside item&nbsp;392 alone: the technique it names contains a planar term that exists only as something computed from the WGS&nbsp;84 ellipsoid and then subtracted, so &ldquo;SAR interferometry&rdquo; is simultaneously the list&rsquo;s evidence for a plane and the clearest instrument on the list for measuring the curvature it removes. Which is the point of counting arguments rather than items. Four lines here, and the two halves of the same processing chain are being spent on both sides of the same ledger.</p>""",

    advocate=dict(
        best_defense=(
            "Your own hedge rule convicts you, and I will start there. Item 392 is the two "
            "words 'SAR interferometry.' It has no verb. You have written three thousand "
            "words against a claim you constructed and then labelled 'the strongest reading "
            "available' — which is precisely the manoeuvre this website exists to complain "
            "about, performed on a fragment you admit has no source, no author and no "
            "predicate. By your own standard that is a critical failure, not a treatment. "
            "Second: on the substance you keep conceding my case and calling it a refutation. "
            "'Photogrammetry planar' is TRUE — your own section 2 says the collinearity "
            "equations are Cartesian and the curvature arrives afterwards as a bolt-on "
            "correction. A model plus a fudge factor is a planar model with a fudge factor. "
            "'Bathymetry sonar straight' survives too, by your own arithmetic: you compute "
            "that curvature across a swath is three tenths of a millimetre and then change "
            "the subject to refraction, which nobody raised. Refraction is not curvature. "
            "You have answered a different item. Third, your flat-earth-phase paragraph is a "
            "pun dressed as evidence, and you know it, because you say so — you tell your own "
            "readers not to rest on the name and then build a whole section around it. Fourth, "
            "the radar horizon: you concede in your own text that ducting produces detections "
            "hundreds of kilometres beyond your formula, routinely, and then rescue yourself "
            "with a free parameter, k, which you are allowed to enlarge whenever the data "
            "embarrass you. A model with an adjustable radius is unfalsifiable — your word, "
            "your rubric. And finally: you looked for a source and found nothing. Nobody wrote "
            "this. So who exactly are you refuting?"),
        survives=4,
        preemptive=(
            "Four, driven by the first and second moves; the third and fourth are already "
            "answered in the body and must not be softened. Five concrete requirements, all "
            "now in the text. (a) THE NO-PREDICATE HIT IS CONCEDED IN OUR OWN VOICE, in the "
            "second paragraph of the refutation, before any argument: items 390 and 392 are "
            "noun phrases, the predicate comes from the page heading '435 Pieces of Evidence "
            "The Earth is Not A Spinning Ball', and we say we are answering the strongest "
            "available reading rather than pretending the item argued it. That paragraph is "
            "load-bearing and an editor who deletes it as throat-clearing hands the defender "
            "the strongest objection on the page. (b) THE BATHYMETRY CONCESSION STAYS FIRST "
            "AND STAYS QUANTITATIVE. Section 4 opens by conceding curvature is negligible "
            "across a swath and gives the numbers against ourselves. The answer to item 400 "
            "is the word 'straight', not the word 'flat', and the text says so — the item "
            "makes a claim about ray paths, and ray paths are the one thing in hydrography "
            "that demonstrably are not straight. Do not let a later edit reorder this so the "
            "curvature number comes second; conceding late reads as being caught. (c) THE "
            "SAR SECTION RESTS ON THE DEFINITION, NOT THE NAME. The quoted definition is 'the "
            "phase present in the interferometric signal due to the curvature of the reference "
            "surface', on WGS 84, and the section carries two independent legs that survive "
            "without the phrase at all — the ellipsoid as the third equation of range-Doppler "
            "geolocation, and yaw steering against the Earth's rotation. If the pun is struck "
            "out entirely the section still stands. (d) ON DUCTING, the concession is made in "
            "our own voice and the reply is specific rather than hand-waving: anomalous "
            "propagation is modelled as a modification of the EFFECTIVE EARTH RADIUS, so k is "
            "a refraction parameter multiplying a curvature, not a free knob that survives "
            "R going to infinity — at infinite R the formula returns an infinite horizon for "
            "every k, which is not what is measured. (e) ON 'WHO ARE YOU REFUTING', agree in "
            "public and make it the finding. The provenance search returned a result: four "
            "noun phrases in an eighteen-line sweep through professions, with no author "
            "anywhere. Say plainly that where there is no upstream sentence there is no hedge "
            "to protect, that this is the part of the list which grew by enumeration rather "
            "than by citation, and that the technical vocabulary the items borrow can still be "
            "checked against the disciplines they name — which is what sections 1 to 4 do."),
    ),

    straw_man=dict(
        identified=True,
        detail=("These four items are addressed to an opponent who denies that practitioners "
                "ever work in a plane. No such opponent exists. Plane surveying is a named "
                "discipline, plane earth loss is a standard propagation model, the "
                "collinearity equations are Cartesian, and flat-earth phase removal is a step "
                "in ESA's own SAR processor — all conceded in the steelman above, at full "
                "strength, before anything is answered. The imported opponent is a "
                "geodesist, photogrammetrist, radar engineer or hydrographer who does not "
                "know which reference surface their own standards specify. What the "
                "professions publish is the opposite: the flat approximation together with "
                "the radius of validity that bounds it, and the correction term to apply "
                "outside it."),),

    compression=dict(
        assessed="no_source", drifted=None, list_phrasing=None, source_wording=None,
        drift_type=None,
        note=("There is no original to hold these four lines against, and the search that "
              "established it is set out in full under &ldquo;No original to quote&rdquo; "
              "above: the specimen cites nothing; the full texts of <em>Galileo Was Wrong</em> "
              "Vol.&nbsp;I and Vol.&nbsp;II were searched offline and photogrammetry, sonar, "
              "bathymetry, LiDAR and synthetic aperture are not located in either as searched, "
              "while every one of the 46 occurrences of &ldquo;radar&rdquo; across the two "
              "volumes is planetary radar, satellite tracking, a contents or bibliography line, "
              "or &mdash; once &mdash; a figure of speech; Dubay&rsquo;s <em>200 Proofs</em> returns zero "
              "for every one of those terms; and the one flat-earth radar claim the "
              "claim-cataloguing literature does record is a different claim about marine "
              "radar advertising, with no originator named. "
              "<strong>The hedge rule has nothing to bite on here, and that is the "
              "result.</strong> Where an argument has an author we can show the list hardening "
              "a hedge; here there is no hedge, because there is no sentence upstream of the "
              "fragment.<br><br>"
              "<strong>Two things are worth publishing anyway, and neither is a drift.</strong> "
              "The first is that <em>the items have no predicates</em>. &ldquo;Photogrammetry "
              "planar.&rdquo; and &ldquo;SAR interferometry.&rdquo; assert nothing on their own; "
              "the argument is supplied entirely by the heading the lines sit under, "
              "&ldquo;435 Pieces of Evidence The Earth is Not A Spinning Ball&rdquo;. A reader "
              "meets them already told what they are for. That is compression with the source "
              "removed rather than compression of a source, and the seven drift types have no "
              "word for it because all seven presuppose an upstream sentence.<br><br>"
              "The second is that the items borrow technical vocabulary, and vocabulary can be "
              "checked even when authorship cannot. Item&nbsp;392 is the clean case: "
              "&ldquo;flat earth&rdquo; <em>is</em> standard terminology in SAR interferometry, "
              "and in ESA&rsquo;s own processing documentation it denotes &ldquo;the phase "
              "present in the interferometric signal due to the curvature of the reference "
              "surface&rdquo;, computed on WGS&nbsp;84 and subtracted. The list has picked up a "
              "phrase whose published definition is the curvature of the Earth. Nothing was "
              "misquoted, because nothing was quoted; the reversal happened between a "
              "discipline and a noun phrase, with no author in between.<br><br>"
              "<strong>Recorded as no-source rather than unassessed.</strong> The comparison "
              "was attempted and it terminated in an answer, which is a finding about how this "
              "part of the list was assembled &mdash; eighteen consecutive lines, one per "
              "profession, none of them citing anyone &mdash; and not a backlog item."),),

    verdict_challenge=dict(
        challenged=True,
        proposed_verdict="SELF-CONTRADICTED",
        reasoning=(
            "MISLEADING is defined on this page as real data with a wrong conclusion made to "
            "look supported. That fits items 390 and 392, where the underlying practice is "
            "real: photogrammetry's collinearity model genuinely is Cartesian, and SAR "
            "interferometry genuinely does contain a step called flat-earth phase removal. It "
            "does not fit items 217 and 400, which are not real data with a wrong conclusion "
            "attached but false descriptions of the instruments they name. Radar horizons are "
            "not flat — the range relation d = 4.12 sqrt(h) is a curvature, the National "
            "Weather Service states that Earth curvature and standard refraction raise the "
            "beam above the surface with increasing range (the 5.1 km figure at 230 km given "
            "in the refutation is our own computation from the 4/3-earth relation, not the "
            "Weather Service's number), and airborne early warning and over-the-horizon radar "
            "are two equipment categories built to defeat the limit. "
            "Sonar rays are not straight — sound speed varies about 4.6 m/s per degree "
            "Celsius, rays refract by Snell's law, and the straight-ray assumption is what "
            "produces the artefacts hydrographers call smiles and frowns. "
            "SELF-CONTRADICTED is proposed on the precedent set at C05, C09 and C10, where "
            "the verdict marks a list running two proofs that cancel. It cancels twice here, "
            "and one of the two does not depend on cluster boundaries at all. Across items: "
            "item 390 'Photogrammetry planar.' and item 391 'LiDAR ECEF.' are consecutive "
            "lines in the specimen, and ECEF is the WGS 84 ellipsoid in a rotating frame — "
            "the two instruments are routinely flown on the same aircraft, adjusted in the "
            "same block and delivered in the same reference system. Within a single item: "
            "the flat-earth phase item 392 invokes is defined in ESA's own processing "
            "documentation as the phase due to the curvature of the reference surface, "
            "computed on WGS 84 and subtracted, so item 392 offers as evidence for a plane a "
            "technique whose planar term exists only as a measured consequence of curvature. "
            "The fallback, if a reviewer reads SELF-CONTRADICTED as reserved for the "
            "fact-denial tier rather than for cancelling proofs, is REFUTED, on the strength "
            "of the two items that are contradicted by specific measurements. What should "
            "not survive either way is treating all four items as one kind of claim: the "
            "datum answer covers two of them and is not the answer to the other two, and the "
            "refutation above says which is which in its opening paragraph."),),

    people=[],
    related=["B04", "B05", "B06", "B07", "B13", "B14", "R08"],

    sources=[
        dict(label="The specimen — withthesun33.com/about-1, items 217, 390, 392 and 400, and "
                   "the run 385–402; re-fetched 2026-08-10. Heading “435 Pieces of Evidence "
                   "The Earth is Not A Spinning Ball” over 461 numbered lines, with no "
                   "citation attached to any item",
             url="https://withthesun33.com/about-1"),
        dict(label="Sungenis & Bennett, Galileo Was Wrong Vol. I — Internet Archive item "
                   "GallileoWasWrong. Full text (462,032 words) downloaded and searched "
                   "2026-08-10: zero hits for photogrammetry, sonar, bathymetry, LiDAR, "
                   "synthetic aperture, echo sounding; 24 for “radar”, all planetary radar "
                   "or GPS tracking; 23 for “interferometry”, none synthetic-aperture",
             url="https://archive.org/details/GallileoWasWrong"),
        dict(label="Sungenis & Bennett, Galileo Was Wrong Vol. II, seventh edition 2013, "
                   "chs 7–13 — Internet Archive item "
                   "GalileoWasWrongTheChurchSungenisRobertA.Bennett4276. Full text (284,044 "
                   "words) searched 2026-08-10, same term list, same result; 22 “radar” hits, "
                   "all Shapiro/Wallace Venus material or the GPS sentence",
             url="https://archive.org/details/GalileoWasWrongTheChurchSungenisRobertA.Bennett4276"),
        dict(label="Dubay, 200 Proofs Earth Is Not a Spinning Ball — Internet Archive item "
                   "200ProofsEarthIsNotASpinningBall, full text searched 2026-08-10: zero "
                   "occurrences of radar, sonar, LiDAR, photogrammetry, bathymetry, "
                   "interferometry, synthetic aperture and remote sensing",
             url="https://archive.org/details/200ProofsEarthIsNotASpinningBall"),
        dict(label="The Flat Earth Society wiki, “Flat Earth – Frequently Asked Questions” — "
                   "read end to end 2026-08-10; none of these instrument terms located in it",
             url="https://wiki.tfes.org/Flat_Earth_-_Frequently_Asked_Questions"),
        dict(label="FlatEarth.ws, “Marine Radar” (9 April 2020) — the one flat-earth radar "
                   "claim this claim-catalogue records, and a different one: advertised "
                   "maximum ranges exceeding the distance to the horizon. No originator named",
             url="https://flatearth.ws/marine-radar"),
        dict(label="Wikipedia, “Radar horizon” — the 4/3 effective Earth radius of 8.5×10³ km "
                   "and the worked examples (1 mile altitude → 102 miles; 75 ft → 12 miles), "
                   "both of which reproduce d(km) = 4.12√h(m)",
             url="https://en.wikipedia.org/wiki/Radar_horizon"),
        dict(label="National Weather Service, “WSR-88D Radar Rainfall Estimation: "
                   "Capabilities, Limitations and Potential Improvements” — “Earth curvature "
                   "and standard refraction dictate that the beam becomes more elevated above "
                   "the surface with increasing range”, and overshooting as the largest source "
                   "of precipitation underestimation beyond 60 nm",
             url="https://www.weather.gov/mrx/radarrainfallestimates"),
        dict(label="Wikipedia, “Over-the-horizon radar” — microwave radar “generally limits "
                   "the detection range of radar systems to objects on their horizon … due to "
                   "the curvature of the Earth”; the Jindalee network's official 3,000 km range",
             url="https://en.wikipedia.org/wiki/Over-the-horizon_radar"),
        dict(label="Yang, Molisch, Ekman, Røste & Berbineau, “A Round Earth Loss Model and "
                   "Small-scale Channel Properties for Open-Sea Radio Propagation”, IEEE "
                   "Trans. Veh. Technol. (2019) — “the PEL assumption of a plane earth surface "
                   "inherent in this model is not fulfilled for maritime radio links at larger "
                   "distances … the diffraction loss caused by the earth curvature and sea "
                   "roughness can not be ignored”",
             url="https://wides.usc.edu/Updated_pdf/yang2019round.pdf"),
        dict(label="Elements of Analytical Photogrammetry (course text, Univ. of Arizona LPL "
                   "copy), §5 — the earth-curvature displacement d = r³(H − Z_P)/(2c²R) with "
                   "R = 6372.2 km, and the note that “the correction due to earth curvature is "
                   "larger than the correction for refraction”",
             url="https://lpl.arizona.edu/hamilton/sites/lpl.arizona.edu.hamilton/files/courses/ptys551/Elements_of_Analytical_Photogrammetry.pdf"),
        dict(label="ESA SNAP / jLinda Interferogram operator documentation — the flat-earth "
                   "phase is “the phase present in the interferometric signal due to the "
                   "curvature of the reference surface”; reference system “for now only WGS84 "
                   "supported, which the reference system used by all space-borne SAR "
                   "systems”; without subtraction the interferogram keeps “the fringes caused "
                   "by the earth curvature”",
             url="https://step.esa.int/main/wp-content/help/versions/10.0.0/snap-toolboxes/org.jlinda.jlinda.nest.ui/operators/InterferogramOp.html"),
        dict(label="Wikipedia, “Interferometric synthetic-aperture radar” — “the "
                   "interferometric phase due to the curvature of the Earth is removed, a "
                   "process referred to as flattening”",
             url="https://en.wikipedia.org/wiki/Interferometric_synthetic-aperture_radar"),
        dict(label="Wang, Huang, Dong et al., “High-precision, fast geolocation method for "
                   "spaceborne synthetic aperture radar”, Chinese Science Bulletin 57(2–3), "
                   "2012 — the Range-Doppler model as three equations, the third being the "
                   "Earth ellipsoid x²/R_e² + y²/R_e² + z²/R_p² = 1",
             url="https://link.springer.com/content/pdf/10.1007/s11434-011-4779-2.pdf"),
        dict(label="Zhao & Wei, “Study on Attitude Control Method for Zero-Doppler Steering in "
                   "Space Borne SAR System”, Progress In Electromagnetics Research Letters 63 "
                   "(2016) — “the Doppler centroid is not zero in the conventional broadside "
                   "mode … due to the earth rotation and eccentricity of the orbit”",
             url="https://www.jpier.org/ac_api/download.php?id=16062102"),
        dict(label="Fiedler, Börner, Mittermayer & Krieger, “Total Zero Doppler Steering — a "
                   "new method for minimizing the Doppler centroid”, IEEE Geoscience and "
                   "Remote Sensing Letters (2005) — the yaw-steering law developed for "
                   "TerraSAR-X",
             url="https://ieeexplore.ieee.org/document/1420292/"),
        dict(label="NPL, “Technical Guides — Speed of sound in sea water: underlying physics” "
                   "— the Mackenzie (1981) equation, whose linear temperature term is 4.591T, "
                   "i.e. about 4.6 m/s per °C",
             url="https://resource.npl.co.uk/acoustics/techguides/soundseawater/underlying-phys.html"),
        dict(label="Beaudoin, “Smiles, Frowns & Misplaced Seafloors: The Case for Accurate "
                   "Sound Velocity Data” (AML Oceanographic, 23 October 2025) — “Sound doesn't "
                   "travel in a straight line underwater — it bends, or refracts”; smiles and "
                   "frowns as “two classic error patterns in multibeam data, where the seafloor "
                   "appears to curve up or down at the edges of the swath”",
             url="https://amloceanographic.com/blogs/smiles-frowns-misplaced-seafloors-the-case-for-accurate-sound-velocity-data"),
        dict(label="IHO S-44 Edition 6.1.0, Table 1 — TVU_max(d) = √(a² + (b×d)²); Order 1a "
                   "a = 0.5 m, b = 0.013; Order 2 a = 1.0 m, b = 0.023. The allowances the "
                   "refraction arithmetic above is measured against",
             url="https://iho.int/uploads/user/pubs/standards/s-44/S-44_Edition_6.1.0.pdf"),
        dict(label="Iselin & Woodcock, “Preliminary report on the prediction of ‘afternoon "
                   "effect’”, Woods Hole Oceanographic Institution, 1942 — “With moderate or "
                   "light winds and a clear sky the diurnal heating which occurs near the sea "
                   "surface can cause a serious reduction in the range of submarine detection”",
             url="https://darchive.mblwhoilibrary.org/handle/1912/2044"),
        dict(label="NOAA Office of Coast Survey, “Ellipsoidally Referenced Surveys (ERS)” — "
                   "positioning “within a geometric, three-dimensional coordinate reference "
                   "frame … using Global Navigation Satellite System (GNSS) technology”, with "
                   "geoid undulation as “the outward-normal distance from the reference "
                   "ellipsoid”",
             url="https://nauticalcharts.noaa.gov/learn/ellipsoidally-referenced-surveys.html"),
    ]),
}
