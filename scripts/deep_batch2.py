# -*- coding: utf-8 -*-
"""Batch 2 — written 2026-08-02, one agent per argument, five largest clusters.

Shipped in this file: R08 (28 items), A22 (20), C02 (16).
R06 (15) and A10 (13) were scoped into this batch but not dispatched; they
remain at cluster depth. See review/triage.json.

New in batch 2: `verdict_challenge`. An agent that thinks the triage verdict is
wrong records it here instead of writing a refutation it does not believe.
All three came back challenged=false.

⚠️ C02 also produced a PROVENANCE correction that changed the corpus — see
review/corrections.json entry 3. Carpenter's One Hundred Proofs contains exactly
one scriptural proof (#50, on immovability), and the words Joshua, Habakkuk and
Ecclesiastes appear ZERO times in the book. The sun-motion proof-text corpus is
a later accretion, so C02's originator was reassigned from Carpenter to Skiba.
"""

BATCH2 = {

# ═══════════════════════════════════════════════ R08 — largest cluster, 28 items
"R08": dict(
    tldr=("WGS 84 — the coordinate system cited most often here as evidence for a fixed "
          "Earth — has the Earth's angular velocity, ω = 7292115 × 10⁻¹¹ rad/s, as one of "
          "its four defining parameters, sitting beside a flattening that exists because "
          "the Earth rotates. Twenty-eight items restate one true and unremarkable fact — "
          "that engineers work in the frame they stand in — in twenty-eight technical "
          "vocabularies. The choice of origin is genuinely conventional; the fictitious-force "
          "terms you must add to make Newton's laws work in the Earth-fixed frame are not."),
    passage=dict(
        work="WRK-SUNGENIS-2006", pd=False,
        locator="Vol. I, Introduction, p. 9 (with n. 22)",
        quote=("Either coordinate system could be used with equal justification. The two "
               "sentences: “the sun is at rest and the Earth moves,” or “the sun moves and "
               "the Earth is at rest,” would simply mean two different conventions "
               "concerning two different coordinate systems."),
        gloss="""<p>This is the load-bearing sentence for the whole cluster, and the first thing to say about it is that <strong>Sungenis and Bennett did not write it</strong>. It appears in their Introduction as a quotation, footnoted (n. 22) to Albert Einstein and Leopold Infeld, <em>The Evolution of Physics</em> (1938/1966), p. 212. On the same page they also quote Poincar&eacute; on the undetectability of uniform translation, and Bellarmine on saving the appearances. The Introduction assembles a conventionalist case: that the Ptolemy&ndash;Copernicus dispute is about description rather than fact.</p>
<p><strong>The list items are considerably firmer than the source.</strong> Sungenis and Bennett are making a philosophical argument about the covariance of physical law. They do not argue anywhere that GPS's use of ECEF coordinates, or a nautical almanac's geocentric columns, constitute <em>evidence</em> that the Earth does not move. That inference &mdash; from engineering practice to cosmological fact &mdash; is a downstream compression, and it is weaker than what the book says. Einstein's claim in context concerns the form of physical laws under coordinate transformation; it is not a claim that a rotating and a non-rotating frame are dynamically indistinguishable, and Einstein plainly did not think that.</p>"""),
    steelman=dict(
        description="""<p><strong>SURFACE (weak).</strong> &ldquo;They mistake a coordinate choice for a claim about reality.&rdquo; True but nearly empty. It answers a slogan, not a position.</p>
<p><strong>DEEPER.</strong> The frames really are conventional. General relativity is generally covariant; the laws can be written in any coordinate system, including one rigidly attached to a point on the Earth's surface. No experiment returns the value &ldquo;origin.&rdquo; Choosing the solar-system barycentre over the Earth's centre of mass is a choice made for tractability, and tractability is not truth.</p>
<p><strong>KERNEL &mdash; the operationalist argument, which deserves to be met head-on.</strong> Every measurement humans have ever made was made from the Earth. The ICRF is defined by quasar positions determined by Earth-based VLBI. The barycentric ephemerides are fitted to observations taken from Earth's surface, or from spacecraft tracked from it. The barycentric frame is therefore not something we <em>found</em>; it is something we <em>constructed</em> from topocentric data by applying a transformation we chose. If the epistemic root of every frame is an Earth-bound observation, in what sense is a frame whose origin lies somewhere nobody has ever stood <em>more real</em> than the one where the observations were actually taken? This is Poincar&eacute;'s conventionalism, and it is a serious position seriously held. The 28 items can be read as an empirical demonstration of it: when people need to <em>do</em> something rather than philosophise, they revert to the frame the measurements were made in &mdash; in geodesy, seismology, aviation and volcanology alike. That convergence is a real fact and it wants an explanation.</p>
<p>We concede all of this without reservation.</p>""",
        why_it_doesnt_save_claim="""<p><strong>The conventionality of the origin is not the conventionality of the dynamics.</strong> This is the hinge. You may put the origin anywhere, and nothing physical changes. What you may not do is thereby make the fictitious-force terms disappear. Write Newton's laws in a frame rigidly attached to the Earth's surface and they are false as stated: you must add a centrifugal term and a Coriolis term to recover agreement with observation. Write them in a frame that does not rotate with respect to the distant matter of the universe and you need add nothing. That asymmetry does not depend on where the origin is. It divides all frames into two classes, and the division is measurable, not stipulated.</p>
<p>The coefficient of those extra terms is a number, &omega;, and it is the same &omega; that appears as a defining constant of WGS 84, as the rate parameter in the IERS Earth Rotation Angle, as the Sagnac term in GNSS pseudorange processing, and as the reading of a ring laser gyroscope in a sealed room with no view of the sky. Conventionalism is a thesis about description. It cannot make a measured number go away.</p>
<p>There is a second reason the kernel does not deliver, and it decides this cluster. Even granting operationalism in full, the argument fails <em>on its own evidence</em>. If the practical primacy of Earth-fixed coordinates were evidence of a fixed Earth, we would expect those coordinate systems to require no rotation parameter. Instead every one of them has Earth's rotation rate written into its definition, and several break by tens of metres if that rate is set to zero. The items point at the artefacts; the artefacts contain the answer.</p>"""),
    refutation="""<p><strong>First, what the book actually argues &mdash; because it is not what the list says.</strong> Sungenis and Bennett argue <em>conventionalism</em>: that the Ptolemy&ndash;Copernicus dispute is a dispute about description rather than about fact, and that the geocentric description is therefore admissible. They argue it by quoting Einstein and Infeld, Poincar&eacute; and Bellarmine. They do not cite GPS. They do not cite WGS&nbsp;84, ITRF, seismic hypocentres or a nautical almanac. In the whole of the passage this cluster rests on, <strong>no instrument is named at all</strong>, and Sungenis&rsquo;s own later restatements of the case reach for the same Einstein sentence without naming one. So the argument has to be met where it is made.</p><p><strong>The Einstein sentence, with its condition restored.</strong> The quotation is real and it is quoted accurately, but it arrives on the list stripped of the clause that governs it. Einstein and Infeld are making a conditional: <em>if</em> the laws of physics can be formulated for arbitrary frames of reference, <em>then</em> the old struggle between the two systems would be meaningless, and either coordinate system could be used with equal justification. That is a claim about what follows from general covariance. It is not a claim that the Earth is at rest, and Einstein plainly did not hold that it is.</p><p><strong>Now the answer: a conventional origin is not a conventional dynamics.</strong> This is the hinge, and it survives granting the conventionalist everything they ask for. Put the origin wherever you like &mdash; nothing physical changes. What you cannot do is thereby make the fictitious-force terms disappear. Write Newton&rsquo;s laws in a frame rigidly attached to the Earth&rsquo;s surface and they are false as stated: you must add a centrifugal term and a Coriolis term to recover agreement with observation. Write them in a frame that does not rotate with respect to the distant matter of the universe and you need add nothing. That asymmetry has nothing to do with where the origin sits. It sorts all frames into two classes, and the sorting is <em>measured</em>, not stipulated.</p><p>The coefficient of those extra terms is a number, &omega;. It is the same &omega; that appears as a defining constant of WGS&nbsp;84, as the rate parameter in the IERS Earth Rotation Angle, as the Sagnac term in GNSS pseudorange processing, and as the reading of a ring laser gyroscope in a sealed room with no view of the sky. Conventionalism is a thesis about description. It cannot make a measured number go away.</p><p><strong>And the conventionalist reading costs its holder the rest of the list.</strong> If the choice really is a convention with nothing to decide between the options, then no experiment can decide it either &mdash; which retires Michelson&ndash;Gale, Sagnac, &ldquo;Airy&rsquo;s failure&rdquo;, Michelson&ndash;Morley and the microwave-background alignments in a single stroke, since each of those asserts that a measurement came out the geocentrist&rsquo;s way. The same trade is set out at <a href="#ARG-R01">R01</a>. It is available, it is honest, and the list cannot afford it.</p><hr style="border:none;border-top:1px solid var(--rule);margin:1.4rem 0"><p><strong>The twenty-eight items are the list&rsquo;s addition, not the authors&rsquo;.</strong> Everything above answers the book. What follows answers the items, which are a different thing and need saying so. Each is a bare noun phrase &mdash; &ldquo;WGS84 ECEF.&rdquo;, &ldquo;LiDAR ECEF.&rdquo; &mdash; and none of them contains an argument. The premise that turns them into one is supplied by the page they sit on, headed &ldquo;435 Pieces of Evidence The Earth is Not A Spinning Ball&rdquo;. Twenty-eight technical artefacts have been added to the source&rsquo;s account by later hands, and the inference attached to them &mdash; <em>a practical system uses Earth-fixed coordinates, therefore the Earth is fixed</em> &mdash; is strictly weaker than the conventionalism it replaced.</p><p>We answer them anyway, because they are what circulates and what a reader arrives with. The technical range creates an impression of independent lines converging; in fact every item has the identical logical form, so twenty-eight restatements of one invalid inference are not twenty-eight pieces of evidence. They sort into seven kinds &mdash; and the striking thing, which the compilers cannot have intended, is how many of them carry the Earth&rsquo;s rotation inside their own definitions.</p>
<p><strong>Kind 1 &mdash; the standard names its own rotation rate.</strong> WGS84 ECEF, geodesy Earth-centered, GPS Earth-centered, radar ECEF, LiDAR ECEF, drone RTK, GNSS pseudorange. WGS 84 has exactly four defining parameters, and NGA lists them as: semi-major axis <em>a</em> = 6378137.0 m; reciprocal flattening 1/<em>f</em> = 298.257223563; geocentric gravitational constant GM = 3986004.418 &times; 10<sup>8</sup> m&sup3;/s&sup2;; and <strong>the angular velocity of the Earth, &omega; = 7292115 &times; 10<sup>&minus;11</sup> rad/s</strong>. Two of the four bear directly on the question. The flattening is there because an oblate spheroid &mdash; TR8350.2 calls the reference figure &ldquo;a geocentric ellipsoid of revolution&rdquo; &mdash; is the equilibrium shape of a self-gravitating body that <em>spins</em>; a non-rotating fluid Earth would be round. And &omega; is not derived, inferred or optional: it is one of the four constants from which the rest of the datum is computed. TR8350.2 &sect;3.2.4 defines it as the rate of &ldquo;a standard Earth rotating with a constant angular velocity,&rdquo; and adds that &ldquo;the actual angular velocity of the Earth fluctuates with time.&rdquo; The coordinate system offered as proof that the Earth does not turn is defined by how fast it turns, and carries a footnote about the irregularities in that turning.</p>
<p><strong>Kind 2 &mdash; the item is about a transformation that exists only because of rotation.</strong> ECI-ECEF transforms, navigation inertial Earth base, airliner FMS Earth grid, ephemeris time. IERS Conventions (2010) ch. 5 gives the terrestrial-to-celestial transformation as [GCRS] = Q(t) R(t) W(t) [ITRS], where W(t) handles polar motion, Q(t) precession-nutation, and R(t) is a rotation through the Earth Rotation Angle, ERA(T<sub>u</sub>) = 2&pi;(0.7790572732640 + 1.00273781191135448 T<sub>u</sub>). On a non-rotating Earth, R(t) would be the identity matrix, Q(t) and W(t) unnecessary, and ECI and ECEF the same frame &mdash; there would be no transformation to name. The rate constant repays reading: 1.00273781191135448 revolutions per UT1 day is the sidereal-to-solar ratio, and the excess 0.00273781 is precisely the one extra rotation per year that an <em>orbiting</em> body accumulates. An item citing &ldquo;ECI-ECEF transforms&rdquo; as evidence for a fixed Earth is citing a matrix whose entire content is the Earth's rotation and orbit.</p>
<p><strong>Kind 3 &mdash; clocks, where rotation is a first-order effect.</strong> Ashby's <em>Living Reviews in Relativity</em> survey is explicit that GPS synchronisation is carried out in the Earth-Centred Inertial frame precisely <em>because</em> synchronisation in the rotating frame is not self-consistent: &ldquo;Path-dependent discrepancies in the rotating frame are thus inescapable &hellip; while synchronization in the underlying inertial frame &hellip; is self-consistent.&rdquo; For an eastward equatorial circumnavigation the discrepancy is 207.4 ns. In receiver processing the same physics appears as the Sagnac correction: Farrell and Hu (<em>J. Geodesy</em> 98:102, 2024) note the ECEF frame rotates during signal propagation, and that neglecting it puts the computed satellite position in error by over 30 metres, with roughly 20 metres of user-position shift at mid-latitudes. Every one of these numbers is exactly zero on a stationary Earth.</p>
<p><strong>Kind 4 &mdash; the frame requires a continuously measured rotation series.</strong> The ITRF is not usable alone; the transformation to the celestial frame requires the Earth Orientation Parameters &mdash; polar motion, UT1&minus;UTC, length of day, celestial pole offsets. These are not computed from theory. They are measured continuously by VLBI on quasars, satellite and lunar laser ranging, and GNSS, because, as the US Naval Observatory puts it, &ldquo;the rotational speed of the Earth remains essentially unpredictable in nature due to incompletely understood variations,&rdquo; with length-of-day departures of 0.001 to 0.002 seconds. The Earth-fixed frame presented as evidence of fixity is maintained by an international service whose full-time job is publishing bulletins of how the Earth's rotation changed last week.</p>
<p><strong>Kind 5 &mdash; the pipeline runs the other way.</strong> JPL's DE440/DE441 equations of motion are integrated in a <em>barycentric</em> frame tied to the ICRS, in barycentric dynamical time. The Horizons documentation states that all underlying calculations are done in the reference frame of the planetary ephemeris, taken as indistinguishable from the ICRF, and results are <em>then</em> transformed to whatever geocentric or topocentric output the user requests. The geocentric columns in a nautical almanac are the <em>product</em> of a barycentric integration, not an alternative to one. The item worded &ldquo;barycentric transforms yield observer ephemerides&rdquo; describes this sequence correctly and draws the reverse conclusion from it. The parallax item inverts itself more sharply still: the parallax equation begins from the Earth because the Earth <em>moves</em>, the baseline being the diameter of its orbit. No motion, no baseline, no equation.</p>
<p><strong>Kind 6 &mdash; self-refuting on its own geometry.</strong> A great circle is by definition the intersection of a sphere with a plane through the sphere's centre; great-circle distance is a quantity that exists only on a sphere. Airline and marine route planning uses it because the Earth is a globe, and the modern refinement goes further in the same direction: Karney's geodesic algorithms (<em>J. Geodesy</em> 87:43&ndash;55, 2013) compute shortest paths on an ellipsoid of revolution &mdash; the sphere corrected for the very flattening that rotation produces. There is no reading of &ldquo;great-circle math&rdquo; that supports a flat or non-rotating Earth; the item names the sphere in its own title.</p>
<p><strong>Kind 7 &mdash; seismology and infrasound.</strong> Hypocentres are reported in Earth-fixed latitude, longitude and depth, but the location is obtained by inverting travel times against a velocity model &mdash; and the standard models, PREM and ak135, are spherically symmetric, radially stratified models of a layered globe. Dziewonski and Anderson's PREM specifies an Earth radius of 6371 km and divides the interior into ocean, crust, lithosphere, low-velocity zone, transition zone, lower mantle, outer core and inner core. You cannot locate an earthquake in Earth-fixed coordinates without assuming a spherical Earth with a liquid outer core.</p>
<p><strong>And the honest remainder.</strong> Several items are simply true statements about engineering convenience and should be granted without qualification: marine sextant work is done in a geocentric-topocentric framework; naked-eye positional astronomy is topocentric; VOR bearings are referenced to the ground; &ldquo;centre equals measurement origin&rdquo; is a fair description of how origins get picked. You do navigate in the frame you stand in, and nobody disputes it. These items are accurate. What they are not is evidence about the Earth's motion &mdash; any more than a ship's captain plotting positions relative to his own vessel is evidence that the vessel is at rest.</p>""",
    straw_man=dict(
        identified=True,
        detail=("Yes, and it runs in the direction that should worry us rather than the "
                "movement. The 28 items attribute to the source an argument the source does "
                "not make. Sungenis and Bennett argue conventionalism — that frames are "
                "descriptive choices and the geocentric one is admissible — by quoting "
                "Einstein, Poincaré and Bellarmine. They nowhere argue that GPS's use of "
                "ECEF is evidence the Earth does not move. That inference is a downstream "
                "compression by list compilers and is strictly weaker than the book. If we "
                "refute only the compressed form we knock down something the named source "
                "did not write. A milder distortion runs the other way: a handful of items "
                "(sextant, topocentric naked-eye astronomy, VOR bearings) are true remarks "
                "about convenience, and treating them as fallacies would misrepresent them.")),
    verdict_challenge=dict(challenged=False, proposed_verdict=None, reasoning=None),
    people=["PER-SUNGENIS", "PER-BOUW", "PER-PTOLEMY"],
    related=["R01", "R02", "R03", "R06", "R09", "R11", "A02", "A07", "A18", "A19", "A22", "B06", "B11", "E15"],
    advocate=dict(
        survives=3,
        best_defense=("You have shown that our coordinate standards contain a parameter "
                      "labelled 'Earth's rotation rate.' We do not dispute the parameter. What "
                      "ω measures is the relative angular rate between the ground and the sky, "
                      "and that number is numerically identical whether the ground turns "
                      "beneath a fixed heaven or the heaven wheels about fixed ground. Tycho "
                      "granted the relative rotation too. You have measured a relative motion "
                      "with great care and then described it as though you had measured an "
                      "absolute one. Nor does the Coriolis argument reach us: in a cosmos whose "
                      "total mass-energy rotates about the Earth, Mach's principle and the "
                      "rotating-mass solutions in general relativity deliver those centrifugal "
                      "and Coriolis terms as genuine gravitational effects of the surrounding "
                      "matter, not as fictions added by hand."),
        preemptive=("First, note what this defence gives up. The moment it says ω is a real "
                    "relative rotation rate and the Coriolis terms are real gravitational "
                    "effects, it has conceded that the Earth-fixed frame is dynamically "
                    "distinguished — which is our whole reply. It has also abandoned the "
                    "argument the 28 items actually make. Those items claim engineering "
                    "practice is EVIDENCE; this defence claims the evidence is neutral between "
                    "two equivalent descriptions. Those are different positions, and the second "
                    "leaves R08 with nothing to do. Second, the relative-rotation premise is "
                    "answerable locally: a ring laser gyroscope in a sealed windowless room "
                    "returns Earth's rotation rate, and the G ring laser at Wettzell resolves "
                    "it to better than one part in 10⁹, independently recovering length-of-day "
                    "variation and polar motion in agreement with VLBI. No sky is involved, so "
                    "the symmetry the defence needs does not obtain. Third, the rotating-cosmos "
                    "route must track ω's IRREGULARITIES — the distant galaxies would have to "
                    "speed up and slow down in phase with El Niño and with the Earth's core. "
                    "That is where the position becomes unfalsifiable rather than unorthodox.")),
    sources=[
        dict(label="NGA Office of Geomatics — WGS 84: the four defining parameters, including ω = 7292115 × 10⁻¹¹ rad/s",
             url="https://earth-info.nga.mil/index.php?dir=wgs84&action=wgs84"),
        dict(label="NIMA TR8350.2, DoD World Geodetic System 1984 (3rd ed.) — §3.2, Table 3.1, §3.2.4 on ω",
             url="https://gis-lab.info/docs/nima-tr8350.2-wgs84fin.pdf"),
        dict(label="IERS Conventions (2010), TN 36 ch. 5 — [GCRS] = Q(t)R(t)W(t)[ITRS] and the Earth Rotation Angle",
             url="https://iers-conventions.obspm.fr/content/chapter5/icc5.pdf"),
        dict(label="Ashby, “Relativity in the Global Positioning System”, Living Reviews in Relativity 6:1 (2003)",
             url="https://link.springer.com/article/10.12942/lrr-2003-1"),
        dict(label="IERS — Earth Orientation Parameters: the rotation of ITRS to ICRS as a function of time",
             url="https://www.iers.org/IERS/EN/Science/EarthRotation/EOP.html"),
        dict(label="US Naval Observatory — Earth's rotation “essentially unpredictable … due to incompletely understood variations”",
             url="https://maia.usno.navy.mil/information/what-is-eop"),
        dict(label="Park et al., “The JPL Planetary and Lunar Ephemerides DE440 and DE441”, AJ 161:105 (2021)",
             url="https://ssd.jpl.nasa.gov/doc/Park.2021.AJ.DE440.pdf"),
        dict(label="JPL Horizons User Manual — calculations done in the DE440/441 frame, then transformed to observer frames",
             url="https://ssd.jpl.nasa.gov/horizons/manual.html"),
        dict(label="Dziewonski & Anderson, “Preliminary reference Earth model”, PEPI 25:297–356 (1981)",
             url="https://lweb.cfa.harvard.edu/~lzeng/papers/PREM.pdf"),
        dict(label="Farrell & Hu, “Derivation of the Sagnac (Earth-rotation) correction …”, J. Geodesy 98:102 (2024) — >30 m error if uncorrected",
             url="https://link.springer.com/article/10.1007/s00190-024-01914-6"),
        dict(label="Karney, “Algorithms for geodesics”, J. Geodesy 87:43–55 (2013) — shortest paths on an ellipsoid of revolution",
             url="https://link.springer.com/article/10.1007/s00190-012-0578-z")]),

# ═══════════════════════════════════════════════ A22 — 20 items
"A22": dict(
    tldr=("Twenty items in this cluster observe that the sky appears to turn, and every one "
          "of them is true. They are also non-discriminating: a rotating sky and a rotating "
          "Earth predict the identical appearance, which is precisely what Ptolemy meant by "
          "saving the appearances — and he says so himself in Almagest I.7. The equivalence "
          "was real until it was broken by measurement, not argument: the phases of Venus "
          "(1610), stellar aberration (1729), stellar parallax (1838) and Foucault's "
          "pendulum (1851)."),
    passage=dict(
        work="WRK-PTOLEMY-ALMAGEST", pd=True,
        locator="Book I, chs. 4 and 7 (trans. R. Catesby Taliaferro)",
        quote="""[Book I, ch. 4 — “That Also the Earth, Taken as A Whole, is Sensibly Spherical”]

Now, that also the earth taken as a whole is sensibly spherical, we could most likely think out in this way. For again it is possible to see that the sun and moon and the other stars do not rise and set at the same time for every observer on the earth, but always earlier for those living towards the orient and later for those living towards the occident. For we find that the phenomena of eclipses taking place at the same time, especially those of the moon, are not recorded at the same hours for everyone … And since the differences in the hours is found to be proportional to the distances between the places, one would reasonably suppose the surface of the earth spherical …

For, if it were concave, the rising stars would appear first to people towards the occident; and if it were flat, the stars would rise and set for all people together and at the same time; and if it were a pyramid, a cube, or any other polygonal figure, they would again appear at the same time for all observers on the same straight line. But none of these things appears to happen. … Again, whenever we sail towards mountains or any high places from whatever angle and in whatever direction, we see their bulk little by little increasing as if they were arising from the sea, whereas before they seemed submerged because of the curvature of the water's surface.

[Book I, ch. 7 — “That the Earth Does Not in any Way Move Locally”]

Now some people, although they have nothing to oppose to these arguments, agree on something, as they think, more plausible. And it seems to them there is nothing against their supposing, for instance, the heavens immobile and the earth as turning on the same axis from west to east very nearly one revolution a day …

But it has escaped their notice that, indeed, as far as the appearances of the stars are concerned, nothing would perhaps keep things from being in accordance with this simpler conjecture, but that in the light of what happens around us in the air such a notion would seem altogether absurd. … never would a cloud be seen to move toward the east nor anything else that flew or was thrown into the air.""",
        gloss="""<p>Claudius Ptolemy worked at Alexandria around 150 CE. The <em>Almagest</em> is the most successful scientific book ever written by duration of service: its planetary tables were the working standard in Greek, Arabic and Latin for roughly fourteen centuries. It is not folklore. It is a quantitative, geometrical, tested model.</p>
<p><strong>First, the irony.</strong> Book I ch. 4 is one of antiquity's cleanest arguments that <em>the Earth is a sphere</em>, argued exactly the way the modern globe is argued: eclipses timed at different longitudes give different local hours, and the offset scales with distance; a mountain rises out of the sea as you approach it. Ptolemy rules out the alternatives by name, and the flat option is dispatched in a single clause &mdash; <em>&ldquo;if it were flat, the stars would rise and set for all people together and at the same time.&rdquo;</em> The list's largest pre-modern authority refutes the list's headline claim on his fourth page.</p>
<p><strong>Second, the concession.</strong> In ch. 7 Ptolemy considers a rotating Earth and grants &mdash; in his own words &mdash; that <em>&ldquo;as far as the appearances of the stars are concerned, nothing would perhaps keep things from being in accordance with this simpler conjecture.&rdquo;</em> He states the non-discrimination point himself. He rejects rotation not from the sky but from terrestrial mechanics: a thrown object or a cloud would be left behind. That argument is the direct ancestor of <a href="#ARG-A10">ARG-A10</a> and <a href="#ARG-A17">ARG-A17</a>, and it is the one part of the chapter that is wrong.</p>"""),
    steelman=dict(
        description="""<p><strong>SURFACE (weak).</strong> &ldquo;These items only describe how things look.&rdquo; True but empty; every observation describes how things look. Stated this way the objection would equally dismiss the observations that <em>did</em> settle the question.</p>
<p><strong>DEEPER.</strong> Ptolemaic astronomy was real science, not a placeholder. It was quantitative, it made forward predictions of eclipses and planetary positions to stated accuracy, it was corrected against observation across generations, and it worked well enough to navigate and keep calendars for fourteen hundred years. Dismissing it as superstition misrepresents the history and makes the eventual correction look like a change of fashion.</p>
<p><strong>KERNEL.</strong> The strongest form is epistemic, and it is correct. &ldquo;Saving the appearances&rdquo; was a serious methodological programme: build the geometry that reproduces the data and remain agnostic about what is physically moving. For the daily rotation of the sky, the geocentric and heliocentric accounts are <em>observationally equivalent</em> &mdash; they predict the same appearance to arbitrary precision, so no amount of watching the sky turn can decide between them. It follows that anyone asserting Earth's motion as established fact before the first genuinely discriminating measurement was going beyond the evidence available to them. Ptolemy says as much in ch. 7. That is a real concession and this page grants it in full.</p>""",
        why_it_doesnt_save_claim="""<p>The kernel is granted and it still leaves the argument where it started, because it is an argument about <em>a set of observations</em>, not about <em>the world</em>. Equivalence is two-edged: if the daily turning of the sky is consistent with a rotating sky, it is equally consistent with a rotating Earth. An observation compatible with both models is evidence for neither. Twenty items of it is still evidence for neither &mdash; restating a non-discriminating observation twenty times in different vocabulary does not accumulate into a discriminating one.</p>
<p>So these items cannot do the work the list needs. They are offered as proofs; they are shared premises. Both sides of the dispute predicted every one of them before the dispute began.</p>
<p>And the equivalence was never permanent. It held because instruments were not yet good enough, and it ended when they became good enough &mdash; by measurement, on dated occasions, not by anyone deciding the matter.</p>"""),
    refutation="""<p>Take the items at face value first, because most are simply correct. The celestial sphere does appear to rotate about the observer. Sidereal rotation is constant to high precision at 23h 56m 04s. Solar declination repeats annually, the ecliptic tilt is stable on human timescales, precession is real, solar noon is symmetric, and the Ptolemaic apparatus did reproduce retrograde motion. Nothing here needs correcting.</p>
<p>Three items deserve specific credit rather than rebuttal. <strong>Libration</strong> is a genuine perspective and orbital effect, reaching 7&deg;54&prime; in longitude from orbital eccentricity and 6&deg;50&prime; in latitude from the Moon's axial tilt, which together let us see about 59% of the lunar surface &mdash; as stated, that item is right. The <strong>analemma</strong> is a real figure-eight with an exact and unmysterious cause: the north&ndash;south extent is the Sun's changing declination from the 23.44&deg; axial tilt, and the east&ndash;west width is the equation of time, an eccentricity term of amplitude 7.66 minutes plus an obliquity term of amplitude 9.87 minutes, running from +16m 25s around 3 November to &minus;14m 15s around 11 February. And <strong>birds do navigate by the sky</strong>: Emlen's planetarium work with indigo buntings established a stellar compass calibrated on the rotational centre of the night sky rather than on individual stars. Real biology with no cosmological content &mdash; a bird orienting on the pole would orient identically under either model.</p>
<p>The relevant question is not whether these observations are true. It is whether any distinguishes a turning sky from a turning Earth. None does, and that is not a criticism of them. It is what Ptolemy himself says in Book I ch. 7. On this point the page agrees with Ptolemy.</p>
<p>What broke the equivalence was measurement, and each break has a date. <strong>1610:</strong> Galileo observed Venus through its full cycle of phases, including gibbous and near-full. In the Ptolemaic ordering Venus rides an epicycle between Earth and Sun and can never present a fully lit face; the full sequence is impossible in that model. (Precision matters: this refutes Ptolemy, not Tycho, whose arrangement predicts the same phases &mdash; and the list's geocentric bulk is Tychonian, so it survives this particular test.) <strong>1729:</strong> Bradley, observing &gamma; Draconis, announced stellar aberration &mdash; an annual displacement of every star by up to 20.4955&Prime;, in phase with Earth's <em>velocity</em> rather than its position. That is a direct signature of the observer's motion, and it is the first observation a stationary Earth cannot accommodate. <strong>1838:</strong> Bessel measured the parallax of 61 Cygni at 0.3136&Prime; &plusmn; 0.0136&Prime;; the modern value is 0.28718&Prime;. <strong>1851:</strong> Foucault hung a 28 kg bob on a 67 m wire in the Panth&eacute;on and the swing plane precessed at about 11.3&deg; per hour, matching 2&Omega;sin&phi; at the latitude of Paris &mdash; Earth's rotation made visible in a room, with no sky involved at all.</p>
<p>Retrograde motion deserves separate treatment, because it is where the difference between <em>fitting</em> and <em>explaining</em> is sharpest. Ptolemy's epicycles reproduce retrograde loops accurately. But to make them come out at the right times he had to impose a condition by hand: for each superior planet, the epicycle's period is locked to one year and its radius stays parallel to the Earth&ndash;Sun line. Nothing in the model says why the Sun should be written into the motion of Mars, Jupiter and Saturn at all &mdash; it is a parameter fixed to match the data. In the heliocentric account the same fact is not a parameter but a consequence: retrograde is what overtaking looks like from the inside lane, so it must occur when Earth passes the planet &mdash; exactly opposition &mdash; and the planet must be nearest and brightest precisely then. One model absorbs the correlation; the other predicts it without being asked. Both save the appearances; only one accounts for them.</p>
<p>So the verdict on this cluster is not that its members are false. It is that they are <em>shared</em>. They were the common ground of the dispute, and the dispute was settled elsewhere. Roughly ninety items across this list have this same shape. They are best read not as claims to be refuted but as a description of the sky that both parties already agreed on.</p>""",
    straw_man=dict(
        identified=True,
        detail=("Several items — 'Retrograde motion math valid', 'Planetary retrograde motion "
                "fit geocentric math', 'Celestial equator precision' — are framed as though "
                "modern astronomy denies that Ptolemaic mathematics worked. Nobody holds that "
                "position. The historical claim is that the model fitted the data by imposing "
                "correlations as free parameters, chiefly the one-year lock of each superior "
                "planet's epicycle to the Earth–Sun line, which the heliocentric model derives. "
                "Demonstrating that epicycle arithmetic reproduces retrograde motion rebuts a "
                "claim nobody makes. 'Analemma lamp artifact' works similarly, treating a fully "
                "explained consequence of axial tilt plus orbital eccentricity as an anomaly.")),
    verdict_challenge=dict(challenged=False, proposed_verdict=None, reasoning=None),
    people=["PER-PTOLEMY"],
    related=["A10", "A17", "A05", "A04", "R01"],
    advocate=dict(
        survives=4,
        best_defense=("For the daily appearance of the sky, the geocentric and heliocentric "
                      "models are observationally equivalent — they predict the same thing to "
                      "arbitrary precision. Ptolemaic astronomy was accurate, predictive and "
                      "self-correcting, and it served for fourteen centuries. Anyone who "
                      "asserted that the Earth moves before there was a measurement capable of "
                      "detecting that motion was asserting more than the evidence supported, "
                      "and it is fair to say so."),
        preemptive=("The strongest anticipated reply is that aberration and parallax are "
                    "themselves model-dependent — that a Tychonic arrangement with the stars "
                    "carried around annually could reproduce both. It can be made to, and van "
                    "der Kamp attempted exactly this by reinterpreting aberration as parallax; "
                    "Bouw later rejected that move and modified the model instead. But the cost "
                    "is the point: each new measurement has to be absorbed by adding a fresh "
                    "stipulation, applied to every star in the sky simultaneously, with no "
                    "independent reason for it. Bouw conceded in print that the resulting model "
                    "is observationally equivalent to heliocentrism and must therefore be chosen "
                    "on theological grounds. That concession is the honest end state of the "
                    "'saving the appearances' programme, and it is not a claim about evidence.")),
    sources=[
        dict(label="Ptolemy, Almagest Book I (Taliaferro trans.), full text of chs. 1–7",
             url="https://bertie.ccsu.edu/naturesci/cosmology/ptolemy.html"),
        dict(label="Phases of Venus incompatible with the Ptolemaic model — Royal Belgian Institute for Space Aeronomy",
             url="https://www.aeronomie.be/en/encyclopedia/venus-phases-not-line-geocentric-model"),
        dict(label="Aberration of light: constant 20.49552″ (J2000); Bradley on γ Draconis, announced January 1729",
             url="https://en.wikipedia.org/wiki/Aberration_(astronomy)"),
        dict(label="Reid & Menten, “The First Stellar Parallaxes Revisited” (arXiv:2009.11913) — Bessel's 1838 value re-analysed",
             url="https://arxiv.org/abs/2009.11913"),
        dict(label="Foucault pendulum: Panthéon, 28 kg bob on 67 m wire, ~11.3°/hr at Paris latitude",
             url="https://en.wikipedia.org/wiki/Foucault_pendulum"),
        dict(label="Retrograde motion as a perspective effect occurring at opposition — Penn State ASTRO 801",
             url="https://courses.ems.psu.edu/astro801/content/l2_p4.html"),
        dict(label="Lunar libration: 7°54′ longitude, 6°50′ latitude, ~59% of the surface visible",
             url="https://en.wikipedia.org/wiki/Libration"),
        dict(label="Equation of time: eccentricity term 7.66 min, obliquity term 9.87 min",
             url="https://en.wikipedia.org/wiki/Equation_of_time"),
        dict(label="Emlen, “Celestial Rotation: Its Importance in the Development of Migratory Orientation”, Science 170:1198 (1970)",
             url="https://www.science.org/doi/10.1126/science.170.3963.1198")]),

# ═══════════════════════════════════════════════ C02 — 16 items
"C02": dict(
    tldr=("The list treats scriptural passages about a moving sun as evidence in a physical "
          "dispute. A theological reading of a text is not a measurement, so it cannot be "
          "confirmed or refuted by one — which places the claim outside what this review can "
          "adjudicate, and we decline to arbitrate the interpretive question, which is "
          "genuinely contested and not ours to settle. What we can say is narrower and "
          "internal: the proof-text method generates conflicting results within the list's "
          "own pages, and the provenance is not what it is usually said to be."),
    passage=dict(
        work="WRK-CARPENTER-1885", pd=True,
        locator="Proofs 39 and 50",
        quote="""39. We have abundance of evidence that the Sun moves daily round and over the Earth in circles concentric with the northern region over which hangs the North Star; but, since the theory of the Earth being a globe is necessarily connected with the theory of its motion round the Sun in a yearly orbit, it falls to the ground when we bring forward the evidence of which we speak, and, in so doing, forms a proof that the Earth is not a globe.

50. We read in the inspired book, or collection of books, called The Bible, nothing at all about the Earth being a globe or a planet, from beginning to end, but hundreds of allusions there are in its pages which could not be made if the Earth were a globe … we have a store from which to take all the proofs we need, but we will just put down one proof—the Scriptural proof—that Earth is not a globe.""",
        gloss="""<p>The numbered-proof format these sixteen items inherit begins with Carpenter. But the genealogy runs differently than the modern list assumes, and the primary text settles it.</p>
<p>Carpenter's book contains one hundred numbered proofs. <strong>Exactly one is scriptural: Proof 50.</strong> Carpenter says so himself, inside the proof &mdash; <em>&ldquo;we will just put down one proof&mdash;the Scriptural proof.&rdquo;</em> He treats his scriptural material as a single entry in a list of a hundred, not as a foundation. And the passages he gestures at there are the immovability and stretched-out-earth texts, not sun-motion texts at all.</p>
<p><strong>The words <em>Joshua</em>, <em>Habakkuk</em> and <em>Ecclesiastes</em> do not appear anywhere in the book.</strong> Not once in 143,000 characters. Carpenter's actual sun-motion proofs &mdash; 38 and 39 &mdash; argue from what an observer sees: the midnight sun skimming the horizon, the sun's daily circuit. Whatever one makes of that reasoning, it is an appeal to appearance, not to a proof-text.</p>
<p>So the sixteen items here are a later accretion. The numbered-proof <em>form</em> is Carpenter's; the scriptural sun-motion <em>content</em> was assembled afterwards, and reaches its present shape in twentieth- and twenty-first-century compilations sorted under headings like &ldquo;Sun Moves, not the Earth.&rdquo; Attributing that corpus to Carpenter overstates his role and misdescribes what he thought he was doing.</p>"""),
    steelman=dict(
        description="""<p>The strongest version of this argument is not about astronomy at all. It is about hermeneutic consistency, and it deserves to be stated at full strength.</p>
<p>Suppose you hold a text to be authoritative and to speak plainly about the world. You did not adopt that position casually; it is load-bearing for a great deal else you believe, and it has a long and serious intellectual pedigree. Now you notice that the same text describes the sun as running a circuit, as being halted, as reversing on a sundial. You have two options. You can read those passages plainly, the way you read the passages you build your life on. Or you can read them non-literally &mdash; but then you owe an account of <em>why these and not others</em>, and if the honest answer is &ldquo;because modern astronomy says so,&rdquo; you have made astronomy the arbiter of your text.</p>
<p>Someone who declines to do that is not being naive. They are refusing a move they regard as special pleading. Consistency is a real intellectual virtue, and applying one's hermeneutic without exception when it is inconvenient is a harder discipline than applying it only when it is comfortable. That is a defensible position, and treating it as ignorance is both wrong and rude.</p>""",
        why_it_doesnt_save_claim="""<p>The kernel is defensible right up to a specific point, and it is worth naming that point precisely.</p>
<p>A commitment about how to read a text is a commitment about reading. It stays entirely inside its own domain, and nothing this review does can touch it. But the argument here does not stop there. It continues: <em>therefore</em> the sun physically moves over a stationary Earth. That &ldquo;therefore&rdquo; carries the claim across a boundary. The moment a reading is asserted to entail that a gyroscope will precess a certain way, that a pendulum will rotate at a certain rate, that a ring interferometer will show a certain fringe shift &mdash; the claim has become a claim about instrument readings.</p>
<p>And instrument readings are answerable to instruments. Not to argument, not to authority, and not to the interpretive question, which remains exactly as open as it was. The dilemma the steelman poses is real, but its second horn was never &ldquo;let astronomy arbitrate your text.&rdquo; It is that a reading which generates a physical prediction has stepped into a domain with its own arbiter, and the prediction is now separable from the reading that produced it. The prediction can fail without the reading being adjudicated at all &mdash; which is precisely why this treatment can reach a verdict without touching the theology.</p>"""),
    refutation="""<p><strong>This section is about domain, not about the text.</strong> Nothing here argues that a scriptural passage is false, and nothing here takes a position on whether God exists. Those are not questions a review of measurements can answer, in either direction, and this review does not attempt them. What follows concerns only what kind of claim is being made and what can settle it.</p>
<p><strong>1. Describing appearance is not asserting mechanism.</strong> This is an observation about language, not a claim about what any text means. &ldquo;The sun rises&rdquo; is how observers in every language and every era have described what they see from where they stand. It is also how working astronomy describes it today: the US Naval Observatory and HM Nautical Almanac Office both publish sunrise and sunset tables, every marine almanac and aviation chart uses the same vocabulary, and celestial navigation is computed in a frame where the observer is fixed and the bodies move. Nobody drawing a sight reduction from an almanac believes they have thereby asserted geocentrism. Noting this does not tell us what any given text intends by it &mdash; that is the interpretive question, addressed next.</p>
<p><strong>2. The interpretive question is contested, and it is not ours.</strong> Many religious traditions, commentators and scholars have read these passages non-literally for a very long time. Others read them literally. Both are theological positions, held by serious people, argued on textual and traditional grounds. This review takes no side, and readers should not infer one from anything above. The dispute is internal to interpretation, and &mdash; this is the operative point &mdash; <strong>no instrument resolves it.</strong> There is no measurement whose outcome makes one reading correct. That is not a criticism of either reading. It is a statement about what measurement is for, and about the limits of this review's remit.</p>
<p><strong>3. What <em>is</em> in our domain: the proof-text method conflicts with itself.</strong> The lists these sixteen items come from are not offered as devotional reading. They are offered as <em>evidence</em>, sorted into evidentiary categories, in a dispute about the shape of the Earth. Assessing whether a stated method delivers consistent results is fair comment on the argument being made, and it requires no theology.</p>
<p>It does not deliver consistent results, and the list under review demonstrates that without any help from us. Item&nbsp;414 enters Isaiah 40:22, the <em>circle</em> of the Earth. Item&nbsp;420 enters Revelation 7:1, the <em>four corners</em>. Items&nbsp;410 and 415 enter the <em>pillars</em> of Psalm 75:3 and 1 Samuel 2:8. Item&nbsp;412 enters Job 26:7, the Earth <em>hung upon nothing</em>. That is four different shapes and two incompatible supports, entered as five separate confirmations of a single physical model. A disc has no corners; a thing resting on pillars is not hanging upon nothing. A method returning all five as independent evidence is not filtering anything &mdash; it is counting. Every number above is checkable in the item table on this page, which is the point: the internal conflict is a property of the list, not of our reading of it.</p>
<p>Note carefully what this is and is not. It is <em>not</em> a claim that the texts contradict each other &mdash; every one of those passages has been read coherently within the tradition for centuries, and how they fit together is again the interpretive question we are not touching. It is a claim about the <em>method</em>: read this way, as a shape-extraction procedure, it yields mutually exclusive shapes.</p>
<p><strong>4. The domain distinction comes from inside the tradition.</strong> The fairest available framing of this boundary was not written by a critic of religion. It was written in 1615 by Galileo, a believer, in his <em>Letter to the Grand Duchess Christina</em>, making a theological argument to a devout audience. Quoting Cardinal Baronius, he wrote: <em>&ldquo;That the intention of the Holy Ghost is to teach us how one goes to heaven, not how heaven goes.&rdquo;</em> He develops the point at length, observing that scripture speaks of physical things &ldquo;but casually,&rdquo; and concluding that &ldquo;in discussions of physical problems we ought to begin not from the authority of scriptural passages but from sense-experiences and necessary demonstrations.&rdquo;</p>
<p>Galileo's own view was that scripture and nature &ldquo;proceed alike from the divine Word.&rdquo; We cite him not as an authority on what the texts mean &mdash; he was making a contested theological argument and knew it &mdash; but because the domain distinction drawn here is not an outsider's imposition. It has been argued from within, by believers, for four hundred years.</p>
<p><strong>5. Joshua 10, specifically.</strong> This passage has been read in several ways within the tradition, over a long period, by people who took it entirely seriously. We are not going to tell readers which reading is right; that is exactly the line this treatment does not cross. The only thing within our remit is this: astronomy does not settle it. There is no observation that arbitrates between the readings, and anyone claiming a telescope has decided the question has made the same category error the proof-texts are being asked to make. The passage is not evidence in a physics dispute &mdash; in either direction.</p>
<p><strong>Verdict.</strong> UNFALSIFIABLE, in a precise and non-pejorative sense: the claim as stated cannot be confirmed or refuted by measurement, because a reading of a text is not the kind of thing measurement addresses. This is a statement about our remit and about the structure of the claim. It is not a statement about the value of the text, and it should not be read as one.</p>""",
    straw_man=dict(
        identified=True,
        detail=("Two straw men run in opposite directions and both should be named. The one "
                "this treatment must avoid: characterising the argument as 'religious people "
                "believe the Bible instead of science.' That misdescribes the position, insults "
                "a large share of this site's own audience, and is empirically wrong — many of "
                "the most rigorous rebuttals of flat-earth claims come from believers, which is "
                "itself evidence that the fault line is not religion versus science. The one the "
                "argument itself deploys: Carpenter's Proof 50 frames the astronomer's position "
                "as 'the groundwork of modern infidelity', converting a dispute about "
                "measurement into a loyalty test. That framing is inherited by the modern lists "
                "and does real work — it makes any evidentiary objection look like an attack on "
                "the reader's faith, which forecloses the conversation the evidence would "
                "otherwise have. Both moves substitute a fight about identity for a question "
                "about domain.")),
    verdict_challenge=dict(challenged=False, proposed_verdict=None, reasoning=None),
    people=["PER-CARPENTER", "PER-SKIBA"],
    related=["C01", "C03", "C04", "C05", "C10", "C07"],
    advocate=dict(
        survives=3,
        best_defense=("You have conceded the strongest thing I need: you cannot refute me. You "
                      "say so yourself in the verdict. Your entire case rests on the assumption "
                      "that instruments are the final arbiter of physical questions, and that is "
                      "not a measured result — it is a philosophical commitment, exactly as much "
                      "a prior as mine, which you have declared rather than defended. Second, "
                      "your internal-tension argument attacks a list I did not write. If some "
                      "compiler files 'circle' and 'four corners' carelessly, that is a fact "
                      "about that compiler's care, not about whether Ecclesiastes 1:5 describes "
                      "a moving sun. Third, you quote Galileo — a man the Church condemned — as "
                      "though his hermeneutic were the tradition's settled position. You cannot "
                      "claim neutrality on interpretation and then adopt one side's framing as "
                      "your organising principle."),
        preemptive=("The strongest of these is the second, and it should be answered rather than "
                    "deflected. The internal-tension point is deliberately scoped: it is not "
                    "evidence about what any passage means, and the treatment says so. It is "
                    "evidence about a specific method — proof-text extraction of physical shape "
                    "— aimed at the compilations these sixteen items were actually drawn from. "
                    "An advocate who disclaims the compilations is welcome to; the cost is that "
                    "the sixteen items lose their evidentiary framing and become sixteen "
                    "readings, which is a weaker position than the one they were entered under. "
                    "On the first: the review does not claim instrumentation arbitrates all "
                    "questions — it claims the narrower thing, that once a claim asserts what a "
                    "gyroscope will read, that assertion is answerable to the gyroscope. Claims "
                    "that decline to enter that scope are recorded as UNFALSIFIABLE rather than "
                    "refuted, which is what happened here. On the third: fair — the treatment "
                    "makes no claim that Galileo's hermeneutic is correct or authoritative, and "
                    "cites him only to establish that the domain distinction has been argued "
                    "from inside the tradition by believers. That is a point about provenance, "
                    "not about who is right.")),
    sources=[
        dict(label="William Carpenter, One Hundred Proofs That the Earth Is Not a Globe (1885) — full text",
             url="https://www.gutenberg.org/ebooks/55387"),
        dict(label="Carpenter, One Hundred Proofs — plain text used for verification (Proofs 38, 39, 50; zero occurrences of Joshua/Habakkuk/Ecclesiastes)",
             url="https://www.gutenberg.org/cache/epub/55387/pg55387.txt"),
        dict(label="Galileo, Letter to the Grand Duchess Christina (1615) — English translation, Ohio State",
             url="https://hti.osu.edu/sites/default/files/galileo_galilei.pdf"),
        dict(label="Letter to the Grand Duchess Christina — publication history and context",
             url="https://en.wikipedia.org/wiki/Letter_to_the_Grand_Duchess_Christina"),
        dict(label="US Naval Observatory — sunrise/sunset tables published in observer-frame language",
             url="https://aa.usno.navy.mil/data/RS_OneDay"),
        dict(label="HM Nautical Almanac Office — rise/set and twilight data service",
             url="https://astro.ukho.gov.uk/nao/websurf/")]),
}
