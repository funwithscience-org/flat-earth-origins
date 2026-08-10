# -*- coding: utf-8 -*-
"""
Distinct-argument clusters, with named provenance.

Each cluster records:
  originator      - the person who introduced this argument into the flat-earth
                    or geocentric canon (NOT the person who repeated it)
  originator_work - the specific publication/broadcast it first appears in
  year            - date of that work
  real_source     - where a genuine scientist's real work is being cited, who
                    actually did it (so the reader can go check the original)
  verdict         - six-verdict rubric; "PENDING" where the writeup is not done
  pre_modern      - OPTIONAL. Set when the argument demonstrably PREDATES the modern
                    movement and no modern author originated it. This is a THIRD state,
                    not a flavour of untraced, and the distinction is the same one
                    `compression.assessed` draws with "no_source":

                      originator="Name"   a modern author put this into the canon
                      originator=None     we looked for an origin and did not find one
                      pre_modern={...}    we looked, and found the origin is older than
                                          the movement - a finding, not a gap

                    Shape: {earliest_documented_use, note, repopularised[]}.
                    `earliest_documented_use` must be a citable instance we have actually
                    read, phrased as EARLIEST DOCUMENTED, never "first" - we cannot show
                    anything is first. A cluster with pre_modern set MUST have
                    originator=None, so nobody is credited with founding what they inherited.

                    `repopularised` is the point of the field, not a footnote to it. An
                    argument older than the movement still had to be CARRIED into it, wave
                    by wave, and each wave is nameable: [{who, work, year}] in date order.
                    That is the distribution chain this whole review exists to expose - few
                    people make these arguments, many carry them - and it is exactly the
                    information a bare originator=None would throw away. Skiba did not
                    originate the sun-motion proof-texts; he is the reason sixteen items of
                    this particular list carry them, and that is worth recording as what it
                    is rather than mislabelling as authorship.
"""

# lane codes: A-EXP geocentric experiment | A-REL relativity, coordinates and
#                                                  underdetermination
#             B flat-earth observation | C scriptural | D historical-esoteric
#             E misappropriated astronomy
#
# The A-REL label was widened 2026-08-10. "relativity/coordinates" did not cover R12
# (the Copernican principle), and arguably not R09 (conventionality of simultaneity) or
# R11 either; in practice this is the underdetermination lane. Lane MEMBERSHIP is
# unchanged - moving R12 would disturb post1950_cited_clusters, and it is filed
# correctly. Only the description was wrong.

CLUSTERS = {

# ---------------------------------------------------------------- A-EXP
"A01": dict(lane="A-EXP", name="Michelson–Morley null proves Earth is not moving",
    originator="Walter van der Kamp", originator_work="The Heart of the Matter", year="1968",
    real_source="Michelson & Morley 1887, Am. J. Sci. 34:333",
    verdict="STANDARD PHYSICS",
    note="A null ether-drift result is exactly what special relativity predicts for a moving Earth. Non-discriminating."),

"A02": dict(lane="A-EXP", name="Michelson–Gale / Sagnac interferometry shows a stationary Earth",
    originator="Robert Sungenis & Robert Bennett", originator_work="Galileo Was Wrong, Vol. I", year="2006",
    real_source="Michelson, Gale & Pearson 1925, ApJ 61:140",
    verdict="REFUTED",
    note="MGP predicted a 0.236 fringe shift for a rotating Earth and measured 0.230 ± 0.005. It detected the rotation and returned the rate to ~2%. Cited backwards. Geocentrist Malcolm Bowden concedes the measurement in Journal of Creation 16(2), 2002."),

"A03": dict(lane="A-EXP", name="“Airy's failure” — water-filled telescope shows no Earth motion",
    originator="Walter van der Kamp", originator_work="De Labore Solis: Airy's Failure Reconsidered", year="1988",
    real_source="G. B. Airy 1871, Proc. Roy. Soc. London, pp. 35–39",
    verdict="REFUTED",
    note="CAREFUL CASE. The null is the predicted result — first via Fresnel's dragging coefficient, then via special relativity: aberration depends on relative source-observer velocity, not on a medium downstream of it. The phrase 'Airy's failure' is internal to the movement; Bouw credits van der Kamp with it. Aberration existing at all is itself evidence Earth moves."),

"A04": dict(lane="A-EXP", name="Stellar aberration is optical/parallax, not Earth's motion",
    originator="Walter van der Kamp", originator_work="Bulletin of the Tychonian Society", year="1970s",
    real_source="James Bradley 1729",
    verdict="REFUTED",
    note="Bouw rejected van der Kamp's version and rebuilt the model to keep aberration — an internal contradiction within the movement."),

"A05": dict(lane="A-EXP", name="No measurable stellar parallax",
    # Corrected 2026-08-07. (1) Not in the 1865 edition — "parallax" occurs there twice, both
    # in the byline. The argument is an 1881 3rd-ed. addition, ch. III pp. 82-87. (2) "Took his
    # pseudonym from the thing he denied" was FALSE and is withdrawn: he was using "Parallax"
    # by the end of 1849, 32 years before writing on stellar parallax, in the generic optical
    # sense his own perspective theory RELIES on. A rhetorically attractive line that did not
    # survive checking.
    originator="Samuel Rowbotham", originator_work="Zetetic Astronomy, 3rd ed. enl. (1881), ch. III (as “Parallax”)", year="1881",
    real_source="Bessel 1838 (61 Cygni, 0.314″); ESA Gaia DR3",
    verdict="REFUTED",
    note="Gaia DR3 publishes parallaxes for ~1.468 billion sources at 0.02–0.03 mas for G<15. Rowbotham's own third edition prints the measurements it is cited against."),

"A06": dict(lane="A-EXP", name="Foucault pendulum explained by a rotating firmament",
    originator="Robert Sungenis & Robert Bennett", originator_work="Galileo Was Wrong, Vol. I", year="2006",
    real_source="Léon Foucault 1851",
    verdict="STANDARD PHYSICS",
    note="Restates the observation in a rotating-universe frame. Non-discriminating on its own; ruled out in combination with ring-laser gyros and Michelson–Gale."),

"A07": dict(lane="A-EXP", name="Gyroscopes / ring-laser gyros show no Earth rotation",
    # Corrected 2026-08-09. The basis line published the instrument's price, which the
    # treatment's gloss says it is deliberately withholding because its only use is to
    # invite an inference about a living man's motive; struck. It also framed the
    # shielding run as a refusal to accept the reading, where the refutation credits it
    # as a control that did its job. The outcome stays hedged to the secondary account
    # (Wile's review), which is the only account we have of that sequence.
    originator="Bob Knodel", originator_work="GlobeBusters / Behind the Curve", year="2018",
    real_source="Sagnac 1913; standard ring-laser INS engineering",
    verdict="SELF-CONTRADICTED",
    note="Knodel's own ring-laser gyro measured a 15°/hour drift on camera — exactly 360°÷24h. The magnetic-shielding run that followed was a reasonable control, and on the secondary account available it returned the same reading."),

"A08": dict(lane="A-EXP", name="Aircraft don't compensate for spin; east/west flight times symmetric",
    originator="Samuel Rowbotham", originator_work="Earth Not a Globe", year="1865",
    real_source="Inertial navigation systems measure Earth rate on every flight",
    verdict="REFUTED",
    note="Descends from Rowbotham's vertical-projectile argument. The atmosphere co-moves; INS platforms explicitly correct for a ~15°/hr Earth rate."),

"A09": dict(lane="A-EXP", name="Coriolis effects reassigned to a rotating sky or to electromagnetism",
    originator="Robert Sungenis & Robert Bennett", originator_work="Galileo Was Wrong, Vol. I", year="2006",
    real_source="Gaspard-Gustave de Coriolis 1835",
    verdict="STANDARD PHYSICS", note="Frame restatement; adds no prediction the rotating model does not already make."),

"A10": dict(lane="A-EXP", name="No wind or drag is felt from the Earth's motion",
    originator="Samuel Rowbotham", originator_work="Earth Not a Globe (3rd ed., enl.)",
    year="1881",
    real_source=None, verdict="REFUTED",
    # Renamed and rewritten 2026-08-05 under the hedge rule. The old name — "atmosphere
    # can't co-rotate" — and the old basis — "assumes the atmosphere is not
    # gravitationally bound to the Earth" — both stated the REVERSE of the source.
    # Rowbotham grants co-rotation explicitly ("we are compelled to conclude that if the
    # earth revolves, the atmosphere revolves also, and in the same direction") and builds
    # his argument from inside that concession. Refuting the fragment was refuting nobody.
    note="Rowbotham grants that the air turns with the Earth, then argues no residual "
         "effect is felt. It is: Coriolis deflection, measured daily."),

"A11": dict(lane="A-EXP", name="Michelson–Pease–Pearson null result",
    originator="Robert Sungenis & Robert Bennett", originator_work="Galileo Was Wrong, Vol. I", year="2006",
    real_source="Michelson, Pease & Pearson 1929, JOSA 18(3):181",
    verdict="STANDARD PHYSICS",
    note="A high-precision repeat of Michelson–Morley (expected 0.9 fringe, measured 0.01), run by Michelson at Mount Wilson specifically to test Miller. Same non-discriminating status as A01."),

"A12": dict(lane="A-EXP", name="Dayton Miller detected a real aether drift that was suppressed",
    originator="Robert Sungenis & Robert Bennett", originator_work="Galileo Was Wrong, Vol. I", year="2006",
    real_source="Miller 1933, Rev. Mod. Phys. 5:203; Shankland et al. 1955, Rev. Mod. Phys. 27:167",
    verdict="REFUTED",
    note="Shankland et al. re-examined Miller's original data sheets and traced the periodic shifts to reading statistics and local temperature variation. Shankland had been Miller's own student and colleague — which undercuts the cover-up framing."),

"A13": dict(lane="A-EXP", name="No centrifugal effects felt; equatorial bulge has another cause",
    originator="Samuel Rowbotham", originator_work="Earth Not a Globe", year="1865",
    real_source=None, verdict="REFUTED",
    note="Centrifugal acceleration at the equator is ~0.034 m/s², about 0.3% of g — below unaided perception but routinely measured by gravimeters."),

"A14": dict(lane="A-EXP", name="Ballistics and artillery ignore Earth's rotation",
    originator="Samuel Rowbotham", originator_work="Earth Not a Globe", year="1865",
    real_source="Standard long-range fire-control tables",
    verdict="REFUTED",
    note="Long-range gunnery has corrected for Coriolis drift since WWI; naval fire-control computers did it mechanically."),

"A15": dict(lane="A-EXP", name="Torsion balances, gravimeters and pendulum clocks show no variation",
    originator=None, originator_work=None, year=None, real_source=None,
    verdict="NOT DEMONSTRATED", note="No specific published measurement is cited by the list."),

"A16": dict(lane="A-EXP", name="High-altitude balloon drift and sun-angle anomalies",
    originator=None, originator_work=None, year=None, real_source=None,
    verdict="NOT DEMONSTRATED", note="No dataset cited."),

"A17": dict(lane="A-EXP", name="Conservation-of-momentum paradox for a moving Earth",
    originator="Samuel Rowbotham", originator_work="Earth Not a Globe", year="1865",
    real_source=None, verdict="REFUTED", note="Galilean relativity, established 1632."),

"A18": dict(lane="A-EXP", name="GPS/time-dilation corrections work in an Earth frame",
    originator="Robert Sungenis & Robert Bennett", originator_work="Galileo Was Wrong, Vol. I", year="2006",
    real_source="GPS relativistic clock corrections",
    verdict="STANDARD PHYSICS", note="GPS corrections are computed in an Earth-centred inertial frame precisely because the Earth rotates within it."),

"A19": dict(lane="A-EXP", name="Gyrocompasses are sky-locked, not Earth-locked",
    originator=None, originator_work=None, year=None,
    real_source="Gyrocompass operating principle",
    verdict="SELF-CONTRADICTED", note="A gyrocompass finds true north by sensing Earth's rotation. It cannot function on a non-rotating Earth."),

"A20": dict(lane="A-EXP", name="Lunar laser ranging shows a fixed baseline",
    originator=None, originator_work=None, year=None,
    real_source="Apollo/Lunokhod retroreflector ranging",
    verdict="NOT DEMONSTRATED", note="No measurement cited; LLR data in fact resolve Earth rotation and lunar recession."),

"A21": dict(lane="A-EXP", name="Satellites and geostationary orbits reinterpreted in an Earth-fixed frame",
    originator="Samuel Shenton", originator_work="International Flat Earth Research Society", year="1957",
    real_source=None, verdict="STANDARD PHYSICS",
    note="Shenton's Sputnik line — 'would sailing round the Isle of Wight prove it spherical?' — is the template."),

"A22": dict(lane="A-EXP", name="The sky's daily appearance is equally described by a moving sky",
    originator="Claudius Ptolemy (via the modern movement)", originator_work="Almagest", year="c. 150 CE",
    real_source=None, verdict="STANDARD PHYSICS",
    note="The observation is true and ancient. It is the definition of a non-discriminating claim: both models predict it identically."),

"A23": dict(lane="A-EXP", name="Gravity / the heliocentric mechanism is unproven",
    originator="Wilbur Glenn Voliva", originator_work="Zion sermons & Leaves of Healing", year="1915",
    real_source=None, verdict="REFUTED",
    note="Voliva's 'gravity is a lot of rot.' Cavendish 1798 onward; g measured to nine significant figures."),

"A25": dict(lane="A-EXP", name="Orbital / lunar / ring stability objections",
    originator=None, originator_work=None, year=None, real_source=None,
    verdict="NOT DEMONSTRATED", note="Asserted without a stated calculation."),

"A26": dict(lane="A-EXP", name="No orbital acceleration or rotation has ever been directly detected",
    originator="Walter van der Kamp", originator_work="De Labore Solis", year="1988",
    real_source=None, verdict="SELF-CONTRADICTED",
    note="Contradicted by items the list itself includes: Michelson–Gale, Sagnac, ring-laser gyros, stellar aberration, parallax."),

"A27": dict(lane="A-EXP", name="Tides explained by sky/firmament torque",
    originator=None, originator_work=None, year=None, real_source=None,
    verdict="NOT DEMONSTRATED", note="No mechanism specified."),

# ---------------------------------------------------------------- A-REL
"R01": dict(lane="A-REL", name="General covariance permits a stationary-Earth frame",
    # Corrected 2026-08-09. Credited to The Heart of the Matter (1968), but every scrap of
    # evidence in the treatment - passage, gloss, compression comparison - comes from
    # De Labore Solis (1988). We have not read the 1968 text. Cite the earliest text we can
    # actually quote, per the standing rule against asserting what a source we have not read
    # contains. (That string occurs three times in this file; this edit is anchored on the
    # R01 key, after a batch-7 edit anchored on a shared field line landed on the wrong cluster.)
    originator="Walter van der Kamp",
    originator_work="De Labore Solis: Airy's Failure Reconsidered", year="1988",
    real_source="Einstein, general relativity (1915)",
    verdict="STANDARD PHYSICS",
    note="CAREFUL CASE. The true part must be conceded: you may write physics in any coordinates. But coordinate freedom is not physical rest — in Earth-centred coordinates the rest of the universe acquires enormous fictitious forces, which is the observable difference."),

"R02": dict(lane="A-REL", name="Mach's principle / relational mechanics allows a fixed Earth",
    originator="Robert Sungenis & Robert Bennett", originator_work="Galileo Was Wrong, Vol. I", year="2006",
    real_source="Ernst Mach, The Science of Mechanics (1883)",
    verdict="STANDARD PHYSICS", note="Mach's principle is not a settled part of GR and does not privilege Earth in any case."),

"R03": dict(lane="A-REL", name="No experiment detects absolute motion; only relative motion is observable",
    # real_source added 2026-08-09. It was null although the proposition is Poincaré's
    # principle of relativity almost verbatim, and van der Kamp quotes that sentence at
    # p. 45 of the De Labore Solis scan - so the genuine work being cited is nameable and
    # the reader can go and read the scope Poincaré wrote into it ("a uniform motion of
    # translation"), which is the hinge of the treatment below.
    # Filling the field has a downstream consequence, recorded here because it is not
    # obvious from this line: build.py dates every argument from `real_source`, so R03's
    # 8 items now count in the two-clocks totals (dated arguments 27 -> 28, items on
    # pre-1930 work 53/107 -> 61/115, which crosses half; median stays 1933).
    originator="Walter van der Kamp", originator_work="The Heart of the Matter", year="1968",
    real_source="Henri Poincaré 1904, “The Present and the Future of Mathematical Physics” (St Louis)",
    verdict="STANDARD PHYSICS",
    note="Correct, and it cuts both ways: it equally forbids establishing that the Earth is absolutely at rest."),

"R04": dict(lane="A-REL", name="The equivalence principle validates a local rest frame",
    originator="Robert Sungenis & Robert Bennett", originator_work="Galileo Was Wrong, Vol. I", year="2006",
    real_source="Einstein equivalence principle",
    verdict="STANDARD PHYSICS", note="Local, not global. It says nothing about the Earth's state of motion relative to distant matter."),

"R05": dict(lane="A-REL", name="GR admits rotating-universe solutions / frame dragging",
    originator="Robert Sungenis & Robert Bennett", originator_work="Galileo Was Wrong, Vol. I", year="2006",
    real_source="Gödel 1949; Lense–Thirring 1918; Gravity Probe B",
    verdict="MISLEADING", note="Gödel's universe is a mathematical solution incompatible with the observed cosmos. Frame dragging is real and measured — and is far too small to hold the stars in a daily circuit."),

"R06": dict(lane="A-REL", name="Tensor/gauge/coordinate formalism can be written Earth-centred",
    originator="Robert Sungenis & Robert Bennett", originator_work="Galileo Was Wrong, Vol. I", year="2006",
    real_source=None, verdict="STANDARD PHYSICS",
    note="The largest single cluster in the list. Restates coordinate freedom in ~15 different technical vocabularies. All one argument, already answered at R01."),

"R07": dict(lane="A-REL", name="Alternative gravity theories admit geocentric variants",
    originator=None, originator_work=None, year=None, real_source=None,
    verdict="NOT DEMONSTRATED", note="No specific variant, paper, or prediction is cited."),

"R08": dict(lane="A-REL", name="Practical systems use Earth-fixed coordinates, therefore Earth is fixed",
    originator="Robert Sungenis & Robert Bennett", originator_work="Galileo Was Wrong, Vol. I", year="2006",
    real_source="WGS84, ITRF, ECEF/ECI, nautical almanacs",
    verdict="MISLEADING",
    note="The second-largest cluster. A reference frame is chosen for convenience — you navigate in the frame you stand in. WGS84 is an Earth-centred model *of an oblate rotating spheroid*; ECI-to-ECEF conversion contains Earth's rotation rate as an explicit term."),

"R09": dict(lane="A-REL", name="Clock synchronisation / one-way light speed is conventional",
    originator=None, originator_work=None, year=None,
    real_source="Reichenbach–Grünbaum conventionality thesis",
    verdict="STANDARD PHYSICS", note="A real and respectable philosophy-of-physics point that has no geocentric consequence."),

"R10": dict(lane="A-REL", name="Quantum observer-defined frames put the observer at the centre",
    originator=None, originator_work=None, year=None, real_source=None,
    verdict="MISLEADING", note="Equivocates on 'observer'. Quantum measurement is not about spatial centrality."),

"R11": dict(lane="A-REL", name="No falsifier distinguishes the frames; multiple cosmologies fit the data",
    originator="Gerardus Bouw", originator_work="Geocentricity", year="1992",
    real_source=None, verdict="SELF-CONTRADICTED",
    note="Bouw — the movement's only credentialed astronomer — conceded his model is observationally equivalent to heliocentrism and must therefore be chosen on theological grounds. That concession removes the list's own claim to be scientific evidence."),

"R12": dict(lane="A-REL", name="The Copernican principle is an unproven assumption",
    # Corrected 2026-08-10, work/year and note.
    # (1) The byline is the BOOK's pair, but the work recorded against it was the film,
    #     which Bennett had no part in - works.py has the film as DeLano and Sungenis, and
    #     E11 records it that way. The treatment quotes and cites the book only, and the
    #     paragraph is already in the 2006 first edition at printed p. 145 (matching the
    #     7th ed. at p. 309), the better part of a decade before the film. The byline was
    #     right; the work pinned to it was not. Repointing to the film instead would have
    #     required redoing the compression drift against DeLano, whose blog runs the
    #     argument far harder than the book does; the force_upgraded finding is calibrated
    #     to the book.
    # (2) The note said the kSZ spectrum "rules out Gpc-scale off-centre void models".
    #     "Off-centre" inverted the geometry - these models put US near the centre, and it
    #     is the distant observers who are off-centre - and "Gpc-scale" now contradicts
    #     the treatment's section four, which publishes Zhang & Stebbins's survival
    #     window: voids with radius ≲0.6 h⁻¹ Gpc survive the kSZ bound and are excluded by
    #     the supernovae instead.
    originator="Robert Sungenis & Robert Bennett", originator_work="Galileo Was Wrong, Vol. I", year="2006",
    real_source="Zhang & Stebbins 2011, PRL 107:041301",
    verdict="REFUTED",
    note="It is not merely assumed — it is tested. The kSZ power spectrum rules out the "
         "LTB void models deep enough to mimic dark energy."),

# ---------------------------------------------------------------- B
"B01": dict(lane="B", name="Water finds its level, therefore the surface is a plane",
    # Corrected 2026-08-07: item 42 is Rowbotham 1849, but item 384 (river grades) is NOT —
    # "Nile" does not occur in the 1865 text and the 1881 index has no Nile/Rivers entry.
    # Earliest documented text is Carpenter 1885 proof 4, passing near-verbatim into Dubay 5.
    originator="Samuel Rowbotham", originator_work="Zetetic Astronomy (item 384: Carpenter 1885, proof 4)", year="1849",
    real_source=None, verdict="REFUTED",
    note="Equivocates on 'level': a level surface is an equipotential surface, which on a rotating spheroid is curved. Newton derived the Earth's oblateness from that same premise in the Principia."),

"B02": dict(lane="B", name="The horizon is flat and rises to eye level",
    originator="Samuel Rowbotham", originator_work="Zetetic Astronomy", year="1849",
    real_source=None, verdict="REFUTED", note="Dip of horizon is measurable with a theodolite and grows with altitude."),

"B03": dict(lane="B", name="Bedford Level / laser canal tests show no curvature",
    originator="Samuel Rowbotham", originator_work="Old Bedford Canal trials", year="1838",
    real_source="Wallace 1870; Oldham 1901",
    verdict="REFUTED",
    note="Rowbotham's two-point setup with a near-water sightline is the exact configuration in which refraction produces a false null. Wallace's three-point 1870 repeat and Oldham's 1901 replication both found the curvature. Flat-earthers cite the court voiding the *wager* as if it reversed the *measurement*."),

"B04": dict(lane="B", name="Long-range visibility of ships, lighthouses and towers",
    # Corrected 2026-08-07. (1) 1849 is impossible: the ancestral passage cites the Port
    # Nicholson light, erected 1859, and the lighthouse table is absent from the 1865 edition.
    # It is an 1881 3rd-ed. addition, ch. II pp. 28-35. (2) Dubay 89 is Cape Agulhas, not Cape
    # Hatteras — "Cape Hatteras" does not occur in 200 Proofs at all. (3) The lighthouse spine
    # of the cluster is Rowbotham's table, not Carpenter's.
    originator="Samuel Rowbotham", originator_work="Zetetic Astronomy, 3rd ed. enl. (1881), ch. II", year="1881",
    real_source=None, verdict="MISLEADING",
    note="Rowbotham reprints the Britannica “Levelling” article in the same chapter as his lighthouse table — it gives him the refraction mechanism, the one-seventh coefficient, and the variability that a flat plane cannot produce. Lady Blount's own 1904 photographer recorded the shimmering vapour layer that explains her result."),

"B05": dict(lane="B", name="Engineering makes no curvature allowance (canals, rail, pipelines, bridges)",
    originator="William Carpenter", originator_work="One Hundred Proofs that the Earth Is Not a Globe", year="1885",
    real_source=None, verdict="REFUTED",
    note="Carpenter's proofs 3 and 40 (Suez Canal) reappear as Dubay's 7 and 8. Local works are built to the local equipotential — which *is* the curved surface. Long-baseline works (tunnels, geodetic survey, GNSS) explicitly model the ellipsoid."),

"B06": dict(lane="B", name="Surveyors assume a plane and make no 'allowance'",
    # Corrected 2026-08-09. The record dated this to the 1849 pamphlet while the treatment
    # rendered below it dates the text twice: the argument turns on a Standing Order of the
    # Houses of Lords and Commons which the 1881 third edition introduces as "for the Session
    # of 1862", and a text quoting an 1862 order cannot stand in an 1849 pamphlet. The
    # earliest text located is the 1865 first book edition, pp. 54-56 (Gutenberg #69892,
    # checked on two mirrors) - WRK-ROWBOTHAM-1865, which is also what passage.work cites.
    # Title moved to the house form for that work at the same time.
    originator="Samuel Rowbotham", originator_work="Earth Not a Globe", year="1865",
    real_source="Encyclopaedia Britannica article 'Levelling'",
    verdict="SELF-CONTRADICTED",
    note="Rowbotham's own '8 inches per mile squared' is lifted from a surveying text — real arithmetic for the difference between true and apparent level. He quoted the correction and then denied the thing it corrects for."),

"B07": dict(lane="B", name="Refraction is invoked ad hoc to rescue curvature",
    originator="Samuel Rowbotham", originator_work="Zetetic Astronomy", year="1849",
    real_source=None, verdict="MISLEADING",
    note="Refraction is independently measurable, was described before the dispute, and is used in the same form by surveyors who are not arguing about Earth's shape."),

"B08": dict(lane="B", name="Star trails / Polaris fixed / southern circumpolar geometry",
    originator="Eric Dubay", originator_work="200 Proofs Earth Is Not a Spinning Ball", year="2015",
    real_source=None, verdict="REFUTED",
    note="Southern-hemisphere circumpolar star trails around a *southern* pole are impossible on any single-plane model. This is the item the flat model most clearly gets wrong."),

"B09": dict(lane="B", name="Plumb lines are perpendicular everywhere",
    originator="Samuel Rowbotham", originator_work="Earth Not a Globe", year="1865",
    real_source=None, verdict="REFUTED", note="Plumb lines point to the local gravity vector, which converges toward the centre. Measured by deflection-of-the-vertical surveys."),

"B10": dict(lane="B", name="Sun and Moon appear the same size; solar diameter constant",
    originator="Samuel Rowbotham", originator_work="Earth Not a Globe", year="1865",
    real_source=None, verdict="MISLEADING",
    note="Coincidence of angular size is real and well known. Solar angular diameter in fact varies ~3.4% annually — the reason we have both total and annular eclipses."),

"B11": dict(lane="B", name="Radar, LiDAR, photogrammetry and sonar assume a plane",
    originator=None, originator_work=None, year=None, real_source=None,
    verdict="MISLEADING", note="All of these run on ellipsoidal datums. Same convenience-frame error as R08."),

"B12": dict(lane="B", name="Polar navigation and dead reckoning imply a dome/disc",
    originator="Charles K. Johnson", originator_work="Flat Earth News", year="1972",
    real_source=None, verdict="REFUTED",
    note="Antarctic circumnavigation and the 24-hour midnight sun are incompatible with any disc model — as Jeran Campanella conceded on the December 2024 'Final Experiment' expedition."),

"B13": dict(lane="B", name="Mirage and optical ducting explain far sightings",
    originator=None, originator_work=None, year=None, real_source=None,
    verdict="SELF-CONTRADICTED", note="Conceding an atmospheric optical mechanism concedes the refraction answer the list elsewhere rejects (B07)."),

"B14": dict(lane="B", name="Rocket and balloon footage shows a flat horizon",
    originator="Charles K. Johnson", originator_work="Flat Earth News", year="1972",
    real_source=None, verdict="MISLEADING",
    note="Curvature is below the noise of a wide-angle lens at balloon altitude; the same footage at altitude with a rectilinear lens shows it."),

# ---------------------------------------------------------------- C
"C01": dict(lane="C", name="Proof-texts on an immovable, established Earth",
    # Work label narrowed 2026-08-10. "(proof 50 onward)" was wrong and the meta line
    # renders as "first published by William Carpenter", so the skim path read a
    # first-publication attribution for four chapter-and-verse citations the pamphlet
    # does not contain. Checked against Project Gutenberg #55387 (5th ed., Baltimore
    # 1885): there are exactly 100 proofs, nothing runs "onward" from 50, and proof 50
    # is the only one that touches scripture - Carpenter says so inside it ("we will
    # just put down one proof--the Scriptural proof"). The credit is kept because that
    # proof does argue this cluster's claim; what is withdrawn is the implication that
    # the citations came through him. Withdrawing the credit outright, the route C02
    # took, remains open to the operator - it moves the traced/untraced totals, so it
    # is not this pass's to make.
    originator="William Carpenter", originator_work="One Hundred Proofs, proof 50", year="1885",
    real_source=None, verdict="UNFALSIFIABLE",
    note="Outside the testable domain. Carpenter's proof 50 is the pamphlet's only "
         "scriptural proof and carries the shared clause “established that it cannot be "
         "moved” unattributed; the four chapter-and-verse citations these items give — "
         "Psalm 93:1, Psalm 104:5, 1 Chronicles 16:30 and Psalm 96:10 — are not located "
         "in the Project Gutenberg text of the fifth edition (#55387)."),
"C02": dict(lane="C", name="Proof-texts on a moving Sun",
    # Attribution corrected TWICE and now withdrawn entirely, 2026-08-09.
    # Carpenter (original) was wrong: his 1885 pamphlet has exactly ONE scriptural proof
    # and never mentions Joshua, Habakkuk or Ecclesiastes. Skiba (2026-08-02) was wrong in
    # the other direction: Bellarmine deploys Ecclesiastes 1:5 against Copernicus in 1615,
    # Galileo's Letter to Christina - which this treatment quotes - replies to that genre,
    # and Bouw runs the same bloc in 1999. Substituting Bouw was rejected on verification
    # as repeating the error one step upstream. There is no modern first author to name,
    # so we name none, and record instead that the origin is older than the movement.
    originator=None, originator_work=None, year=None,
    pre_modern=dict(
        earliest_documented_use="Cardinal Bellarmine to Foscarini, 12 April 1615",
        repopularised=[
            dict(who="Robert Schadewald", work="“The Flat-Earth Bible,” Bulletin of the "
                     "Tychonian Society 44", year="1987",
                 role="surveyed and catalogued the corpus — from the debunking side, "
                      "writing for geocentrist readers"),
            dict(who="Gerardus Bouw", work="Geocentricity; A Geocentricity Primer",
                 year="1992/1999",
                 role="runs Joshua 10:12–13, Isaiah 38:8 and Psalm 19:4–6 as evidence the "
                      "Sun's motion is real rather than apparent"),
            dict(who="Rob Skiba", work="biblical-cosmology teaching", year="2015",
                 role="the proximate route these sixteen items travelled into the modern "
                      "flat-earth compilations; quotes Schadewald by name"),
        ],
        note="Bellarmine cites Ecclesiastes 1:5 &mdash; <em>&ldquo;The sun also riseth, and "
             "the sun goeth down, and hasteth to his place where he arose&rdquo;</em> &mdash; "
             "as evidence that the sun really moves and the Earth stands still, and argues "
             "that unlike a passenger who sees the shore recede, here <em>&ldquo;no wise man "
             "has any need to correct the error.&rdquo;</em> That is this cluster's argument, "
             "in 1615, four centuries before the list. The modern compilers are distributing "
             "it, not inventing it &mdash; which is what this review exists to show."),
    real_source=None, verdict="UNFALSIFIABLE",
    note="Outside the testable domain. Reattributed 2026-08-02: Carpenter's 1885 pamphlet "
         "contains exactly ONE scriptural proof (#50, on immovability) and never mentions "
         "Joshua, Habakkuk or Ecclesiastes. The sun-motion proof-text corpus is a later "
         "accretion reaching its present shape in modern thematic compilations."),
"C03": dict(lane="C", name="Proof-texts on foundations and pillars",
    originator="Rob Skiba", originator_work="biblical-cosmology teaching", year="2015",
    real_source=None, verdict="UNFALSIFIABLE", note="Outside the testable domain."),
"C04": dict(lane="C", name="Proof-texts on the firmament / dome",
    originator="Rob Skiba", originator_work="biblical-cosmology teaching", year="2015",
    real_source=None, verdict="UNFALSIFIABLE", note="Outside the testable domain."),
"C05": dict(lane="C", name="Circle, four corners and ends of the Earth",
    originator="Rob Skiba", originator_work="biblical-cosmology teaching", year="2015",
    real_source=None, verdict="SELF-CONTRADICTED",
    note="The list cites both 'four corners' and 'the circle of the Earth' as proofs. They describe different shapes."),
"C06": dict(lane="C", name="Anthropocentric creation / Earth as footstool",
    originator="Wilbur Glenn Voliva", originator_work="Zion sermons", year="1915",
    real_source=None, verdict="UNFALSIFIABLE", note="A theological claim about purpose, not geometry."),
"C07": dict(lane="C", name="Patristic, scholastic and church-tradition affirmation",
    # Corrected 2026-08-09. "Vol. III (2006)" cannot exist: the copyright page of the volume
    # we hold records five previous editions in TWO volumes, 2005-2010, and a sixth edition in
    # three volumes from January 2013. Our own gloss already said this was "not a citation that
    # can exist" while the record went on asserting it - the sweep's pattern 4, self-criticism
    # shipped as prose instead of applied as a fix. real_source added: Bellarmine is the
    # argument's documented earlier hand, quoted and credited by Sungenis himself.
    originator="Robert Sungenis",
    originator_work="Galileo Was Wrong, Vol. III (three-volume edition)", year="2013",
    real_source="Robert Bellarmine to Paolo Antonio Foscarini, 12 April 1615",
    verdict="NOT DEMONSTRATED", note="Appeal to authority; also historically contested. The "
    "tradition invoked is geocentric AND spherical-Earth - Sungenis himself records that "
    "Lactantius was the only Father who held the Earth non-spherical."),
"C08": dict(lane="C", name="Liturgy, calendar and eastward orientation as cosmology",
    originator=None, originator_work=None, year=None, real_source=None,
    verdict="NOT DEMONSTRATED", note="Ritual practice keyed to apparent sky motion is not a measurement of the sky."),
"C09": dict(lane="C", name="Church art and iconography as cosmology",
    originator=None, originator_work=None, year=None, real_source=None,
    verdict="UNFALSIFIABLE", note="Devotional imagery is not survey data."),
"C10": dict(lane="C", name="Job 26:7 — 'he hangs the earth on nothing'",
    originator=None, originator_work=None, year=None, real_source=None,
    verdict="SELF-CONTRADICTED",
    note="Cited alongside the pillars-and-foundations texts (C03), which say the opposite. The list uses both as proofs."),

# ---------------------------------------------------------------- D
"D01": dict(lane="D", name="All ancient cultures were geocentric",
    originator="Robert Sungenis", originator_work="Galileo Was Wrong, Vol. II", year="2006",
    real_source=None, verdict="NOT DEMONSTRATED",
    note="Appeal to antiquity. Also false in detail: Aristarchus proposed heliocentrism in the 3rd c. BCE, and Eratosthenes measured the Earth's circumference c. 240 BCE."),
"D02": dict(lane="D", name="Named ancient authorities (Plato, Aristotle, Ptolemy, Tycho)",
    originator="Robert Sungenis", originator_work="Galileo Was Wrong, Vol. II", year="2006",
    real_source=None, verdict="NOT DEMONSTRATED",
    note="Every one of them held the Earth to be a *sphere*. Citing them supports geocentrism at best, and actively refutes the flat half of the list."),
"D03": dict(lane="D", name="Geocentric/Ptolemaic models made accurate predictions",
    originator="Robert Sungenis", originator_work="Galileo Was Wrong, Vol. II", year="2006",
    real_source=None, verdict="STANDARD PHYSICS",
    note="True, and the point: they were superseded *by measurement*, not by decree."),
"D04": dict(lane="D", name="Axis mundi / world tree / omphalos symbolism",
    # Corrected 2026-08-09, the C02 shape again: the FIELD was wrong, so no substituted name
    # would have been right. `originator` is documented as "the person who introduced this
    # argument into the flat-earth or geocentric canon". Eliade introduced nothing into that
    # canon - he was a historian of religion REPORTING how myths structure sacred space, and
    # says so: "the multiplicity, or even the infinity, of centers of the world raises no
    # difficulty for religious thought" (The Sacred and the Profane, ch. 1). Naming him
    # originator put a real scholar on the People tab as the author of a flat-earth argument.
    # He belongs in `real_source` - the field for whose genuine work is being cited - and
    # that is where he now is, alone.
    originator=None, originator_work=None, year=None,
    real_source="Eliade 1949; Guénon, Le Roi du Monde 1927",
    verdict="UNFALSIFIABLE",
    note="Eliade described religious *symbolism*, not geography — and Jonathan Z. Smith showed even the universality claim is a scholarly construct built on a misread of Spencer and Gillen."),
"D05": dict(lane="D", name="Mandala / still-centre symbolism",
    # Same correction as D04, 2026-08-09.
    originator=None, originator_work=None, year=None,
    real_source="Mircea Eliade, Patterns in Comparative Religion (1949) - reported, not asserted",
    verdict="UNFALSIFIABLE", note="Symbol resemblance is not measurement."),
"D06": dict(lane="D", name="Hermetic 'as above, so below' / sacred geometry / microcosm",
    originator="William Walker Atkinson (as 'Three Initiates')", originator_work="The Kybalion", year="1908",
    real_source="Emerald Tablet, Arabic recensions c. 750–830 CE",
    verdict="UNFALSIFIABLE",
    # Corrected 2026-08-07: the Kybalion CODIFIED the axiom as a numbered Principle;
    # the compact English form was already free-standing in Blavatsky 1877. "Popularised" overcredited it.
    note="The maxim is a 12th-c. Latin rendering of an 8th–9th-c. Arabic alchemical text about transmutation — current in English occultism from Blavatsky (1877) and codified as a numbered Hermetic Principle by a 1908 Chicago New Thought pamphlet. It is not an Egyptian statement about the shape of the Earth."),
"D07": dict(lane="D", name="Kabbalistic / alchemical / Gnostic / Rosicrucian / Masonic iconography",
    # Corrected 2026-08-07. Three faults, one MAJOR. (1) The Book of Dzyan sentence is
    # withdrawn: it frames The Secret Doctrine (1888), not Isis Unveiled (1877); the people on
    # record calling it fabricated are historians and critics, not Buddhist-studies scholars —
    # the one long-term Sanskrit/Tibetan specialist on the question, David Reigle, reports
    # circumstantial evidence FOR authenticity. And no item here descends from Dzyan anyway.
    # (2) The items track Hall 1928 almost one-for-one, so Hall is primary. (3) Year follows.
    originator="Manly P. Hall; Helena Blavatsky", originator_work="The Secret Teachings of All Ages (1928); Isis Unveiled (1877)", year="1928",
    real_source=None, verdict="UNFALSIFIABLE",
    note="Esoteric interpretive literature. Where these traditions do carry cosmology it is the geocentric nested spheres of their own century — which contain a spherical Earth. Hall captions the Rosicrucian plate a “Ptolemaic chart”."),
"D08": dict(lane="D", name="Temple, cathedral and Dendera-zodiac architecture as cosmology",
    originator="Manly P. Hall", originator_work="The Secret Teachings of All Ages", year="1928",
    real_source="Dendera zodiac, Louvre E 13482, dated c. 50 BCE",
    verdict="SELF-CONTRADICTED",
    note="The Dendera ceiling is a late-Ptolemaic *planisphere* incorporating the Babylonian/Greek zodiac — a projection of a spherical sky, and evidence of Hellenistic transmission rather than primordial hidden knowledge."),
"D09": dict(lane="D", name="Geocentric astrology and zodiacal symbolism as evidence",
    originator=None, originator_work=None, year=None, real_source=None,
    verdict="UNFALSIFIABLE", note="Astrology is geocentric because it is observational and topocentric, not because the Earth is fixed."),
"D10": dict(lane="D", name="Heliocentrism has occult/masonic roots",
    originator="Marshall Hall", originator_work="The Earth is not Moving", year="1991",
    real_source=None, verdict="NOT DEMONSTRATED",
    note="Genetic fallacy. Where an idea came from is not evidence about whether it is true."),
"D11": dict(lane="D", name="Perception is reliable; the observer defines the centre",
    originator="Samuel Rowbotham", originator_work="Zetetic Astronomy (the zetetic method)", year="1849",
    real_source=None, verdict="NOT DEMONSTRATED",
    note="Rowbotham's founding move — 'observation is real, theory is imaginary'. It is the epistemology the whole genre rests on, and it is the thing actually being defended."),
"D12": dict(lane="D", name="Simplicity / common sense favours a fixed Earth",
    originator="Samuel Rowbotham", originator_work="Zetetic Astronomy", year="1849",
    real_source=None, verdict="NOT DEMONSTRATED", note="Parsimony is not a measurement, and the flat/fixed model is not in fact simpler once it must account for the southern sky."),
"D13": dict(lane="D", name="Meaning, teleology and fine-tuning imply centrality",
    originator="Robert Sungenis", originator_work="The Principle (film)", year="2014",
    real_source=None, verdict="UNFALSIFIABLE", note="A claim about significance, not position."),
"D14": dict(lane="D", name="Dark matter / dark energy / MOND are modern epicycles",
    originator="Robert Sungenis", originator_work="Galileo Was Wrong, Vol. I", year="2006",
    real_source=None, verdict="MISLEADING",
    note="Rhetorically effective and substantively empty: an unexplained residual in a theory is not evidence for a specific alternative, least of all one with no quantitative model."),
"D15": dict(lane="D", name="The Galileo affair was scientific, not religious",
    # Corrected 2026-08-09, same impossible pairing as C07: no Vol. III existed in 2006.
    originator="Robert Sungenis",
    originator_work="Galileo Was Wrong, Vol. III (three-volume edition)", year="2013",
    real_source=None, verdict="NOT DEMONSTRATED", note="A history-of-science claim with no bearing on the Earth's motion either way."),
"D16": dict(lane="D", name="World mythologies depict a circling sun or a covering sky",
    originator=None, originator_work=None, year=None, real_source=None,
    verdict="UNFALSIFIABLE", note="Myth records how the sky looks, which is not in dispute."),
"D17": dict(lane="D", name="An electromagnetic/toroidal dome centred on Earth",
    originator="Mark Sargent", originator_work="Flat Earth Clues", year="2015",
    real_source="Schumann resonance (real, and a consequence of a spherical cavity)",
    verdict="NOT DEMONSTRATED",
    note="Sargent's enclosed-world model. The Schumann resonance frequency is derived from the Earth-ionosphere cavity treated as a *sphere* of radius 6371 km — the number only comes out right on a globe."),
"D19": dict(lane="D", name="Eclipse and lunar cycles are tuned to human timekeeping",
    originator=None, originator_work=None, year=None, real_source=None,
    verdict="UNFALSIFIABLE", note="Saros and Metonic cycles are consequences of orbital periods; the calendars were built to fit them, not the reverse."),

# ---------------------------------------------------------------- E
"E01": dict(lane="E", name="CMB 'Axis of Evil' aligns with Earth / the ecliptic",
    # RESTORED 2026-08-09. A batch-7 edit intended for E03 landed here instead: E01 and E03
    # carried an identical originator/work/year line, and the edit used replace(old, new, 1),
    # which took the FIRST match. E01 silently gained E03's comment and E03's work/year, and
    # ten E01 dataset rows were republished with them. E03 never got its correction at all.
    # Caught by the curmudgeon sweep 2026-08-09 and logged in corrections.json.
    originator="Robert Sungenis & Rick DeLano", originator_work="The Principle (film)", year="2014",
    real_source="Land & Magueijo 2005, PRL 95:071301; de Oliveira-Costa et al. 2004; Schwarz et al. 2004",
    verdict="MISLEADING",
    note="CAREFUL CASE — represent honestly. The alignment is a real, reproducible feature of the data and the significance debate is genuinely open. But Land & Magueijo themselves walked the significance back in 2007 ('no evidence' under Bayesian model comparison for the general model); Planck 2018 VII notes the look-elsewhere effect and finds no corresponding anomaly in polarization. Decisively: the axis aligns with the *ecliptic and the dipole*, which points to a local/systematic origin — i.e. the alignment is evidence the signal may be partly non-cosmological, which is the opposite of what is claimed."),
"E02": dict(lane="E", name="CMB hemispheric asymmetry, Cold Spot, parity and variance anomalies",
    originator="Robert Sungenis & Rick DeLano", originator_work="The Principle (film)", year="2014",
    real_source="Planck 2018 VII, A&A 641:A7; Schwarz et al. 2016, CQG 33:184001",
    verdict="MISLEADING", note="Same status as E01: real features, contested significance, no geocentric implication."),
"E03": dict(lane="E", name="CMB dipole, dark flow and bulk-flow directionality",
    # Corrected 2026-08-08, actually applied 2026-08-09 (the first attempt landed on E01).
    # The dipole argument is TEXTUAL, not filmic: thirteen numbered "Claims and Responses"
    # across Galileo Was Wrong Vol. I ch. 3 and Vol. II ch. 10; the film contains the least
    # of it. Separately, "dark flow" and "bulk flow" occur ZERO times in all three volumes —
    # item 327 traces to DeLano's blog, 18 May 2013, not to the book or the film.
    originator="Robert Sungenis & Rick DeLano",
    originator_work="Galileo Was Wrong (7th ed., 2013), Vol. I ch. 3 and Vol. II ch. 10", year="2013",
    real_source="Kashlinsky et al. 2008; Planck Int. XIII 2014, A&A 561:A97",
    verdict="REFUTED",
    note="The dipole *is* our motion — 369.82 ± 0.11 km/s, measured. Dark flow was not confirmed: Planck found no detection of bulk flow in any comoving sphere."),
"E04": dict(lane="E", name="Quasar polarization alignment and large quasar groups",
    # real_source gained Varshni 2026-08-10: it named Hutsemékers and Clowes but not the
    # ancestor of item 90, which is the subject of two of the treatment's eight sections.
    originator=None, originator_work=None, year=None,
    real_source="Varshni 1976, Ap&SS 43:3–8; Hutsemékers et al. 2005, A&A 441:915; Clowes et al. 2013, MNRAS 429:2910",
    verdict="MISLEADING",
    note="Real, replicated signals with an accepted astrophysical mechanism — black-hole spins align with the filaments they sit in. Preferred directions differ by redshift slice and hemisphere, so there is no single axis through Earth. Nadathur 2013 showed Clowes's algorithm finds Gpc 'structures' in explicitly homogeneous random simulations."),
"E05": dict(lane="E", name="Galaxy spin handedness / hemispheric bias",
    # real_source completed 2026-08-10. It named Longo and Patel & Desmond only, while
    # the three checks doing the load-bearing work in the treatment - and now named in
    # its tldr - went uncredited.
    originator=None, originator_work=None, year=None,
    real_source="Land et al. 2008, MNRAS 388:1686; Longo 2011, PLB 699:224; "
                "Hayes, Davis & Silva 2017, MNRAS 466:3928; "
                "Iye, Yagi & Fukumoto 2021, ApJ 907:123; "
                "Patel & Desmond 2024, MNRAS 534:1553",
    verdict="REFUTED",
    note="The nearest thing to settled on this list. Galaxy Zoo found classifier bias; Iye et al. 2021 found a headline 4.0σ result collapsed to 0.29σ once duplicate entries were removed; Patel & Desmond 2024 pooled all public datasets and found consistency with isotropy."),
"E06": dict(lane="E", name="Dwarf-galaxy planes and satellite alignments",
    # Corrected 2026-08-10, both fields.
    # (1) real_source named ONLY the rebuttal - the paper that argues the anomaly away
    #     was recorded as the source of items that assert it. The papers items 337/338
    #     actually compress are the ones now listed first; Sawala is kept last, as the
    #     work that answers them. Kanehisa et al. 2025 is NOT added: it postdates the
    #     list and so cannot be what these items point at, though it is in the treatment.
    # (2) The note said the tension "has substantially deflated". That was stronger than
    #     the literature supports and it contradicted the treatment's own section 1.
    originator=None, originator_work=None, year=None,
    real_source="Kroupa, Theis & Boily 2005, A&A 431:517; "
                "Pawlowski, Pflamm-Altenburg & Kroupa 2012, MNRAS 423:1109; "
                "Ibata et al. 2013, Nature 493:62; Müller et al. 2018, Science 359:534; "
                "Sawala et al. 2023, Nature Astronomy 7:481",
    verdict="MISLEADING", note="A real and still-unresolved ΛCDM tension. Sawala et al. 2023 answered the Milky Way case and said so; Seo et al. 2024 rebuilt the rarity test and still get 0.00–3.40%, and the Centaurus A result of 2021 is titled “remains a challenge”. No geocentric content either way."),
"E07": dict(lane="E", name="Gamma-ray-burst anisotropy",
    originator=None, originator_work=None, year=None, real_source=None,
    verdict="NOT DEMONSTRATED", note="No specific result cited."),
"E08": dict(lane="E", name="Pioneer and flyby anomalies are Earth-directed",
    # Corrected 2026-08-10. The note called the flyby anomaly "an unreplicated 1990s
    # Doppler-tracking puzzle ... a navigation problem". Both halves were wrong: Rosetta I
    # is a March 2005 detection at 1.82 ± 0.05 mm/s, and "a navigation problem" asserted a
    # resolution nobody has published. Two of the three items here are flyby items, so
    # real_source also gained the flyby paper it had been missing.
    originator=None, originator_work=None, year=None,
    real_source="Anderson et al. 1998, PRL 81:2858; Anderson et al. 2008, PRL 100:091102; "
                "Turyshev et al. 2012, PRL 108:241101",
    verdict="REFUTED",
    note="The Pioneer anomaly was resolved in 2012 — anisotropic thermal recoil, of which "
         "Earth-pointing was the prediction, not the puzzle. The flyby anomaly is not "
         "resolved: Galileo 1990, NEAR 1998 and Rosetta in March 2005 are unexplained, and "
         "the nulls since have shrunk its footprint rather than accounted for it. Neither "
         "anomaly is evidence of anything cosmological, and nobody in the field has "
         "proposed that either is."),
"E09": dict(lane="E", name="Hubble tension shows we are at a special location",
    # Corrected 2026-08-10. The note said the local-void reading "was tested directly on
    # 1295 supernovae and excluded at 4–5σ". Kenworthy, Scolnic & Riess 2019 exclude
    # SHARP-EDGED LTB underdensities deeper than 20%; they do not close the local-void
    # reading, which is still argued in MNRAS and which the treatment's §5, §6 and tldr
    # deliberately leave open. The note renders as the basis line beside the verdict chip,
    # so skim readers were meeting the one claim the body refuses to make.
    originator=None, originator_work=None, year=None,
    real_source="Riess et al. 2022, ApJL 934:L7; Kenworthy et al. 2019, ApJ 875:145",
    verdict="MISLEADING",
    note="Two rival explanations of one number, counted as two proofs. Kenworthy et al. "
         "2019 exclude sharp-edged voids deeper than 20% at 4–5σ on 1295 supernovae; a "
         "shallower local void is still argued in MNRAS. Either way the region is tens to "
         "hundreds of megaparsecs across and does not single out the Earth."),
"E10": dict(lane="E", name="Zodiacal dust and Kuiper structure show ecliptic symmetry",
    # Corrected 2026-08-10. The note read "Solar-system material lies in the solar-system
    # plane. That is what a solar system is." — loose in exactly the way this argument
    # turns on, since there is no single solar-system plane and the treatment's section 1
    # is the demonstration that the ecliptic is the worst of the three fits to the dust.
    originator=None, originator_work=None, year=None, real_source=None,
    verdict="STANDARD PHYSICS",
    note="Solar-system material lies near a family of planes set by the planets' secular "
         "perturbations, and there is no single solar-system plane: the ecliptic, the "
         "invariable plane and the zodiacal cloud's fitted symmetry surface are mutually "
         "inclined by one to two degrees. On both published fits of the dust, the Earth's "
         "is the worst of the three."),
"E11": dict(lane="E", name="The solar-system plane coincides with the CMB axis",
    originator="Robert Sungenis & Rick DeLano", originator_work="The Principle (film)", year="2014",
    real_source=None, verdict="MISLEADING", note="This is the E01 coincidence restated — and it is the strongest available hint that the CMB alignment is a local systematic."),
"E12": dict(lane="E", name="Redshift quantization in concentric shells around Earth",
    # Corrected 2026-08-10, real_source and note.
    # real_source read "Tifft 1976; refuted by 2dF/SDSS surveys" and was wrong twice: the
    # 2dF paper (Hawkins et al. 2002) tested the Burbidge–Karlsson log(1+z) QUASAR
    # periodicity on 1647 galaxy-quasar pairs, not Tifft's galaxy comb, and the two
    # carriers the items actually run through were unrecorded.
    # The note claimed the effect "disappeared" and was "an artefact of small, sparse
    # samples". Section IV of the treatment refuses both halves: large-sample tests put it
    # at ~2σ rather than at zero, and the frame dependence is the thing that kills it.
    # originator="Gerardus Bouw", 1992 is NOT confirmed - the vocabulary is Sungenis &
    # Bennett's and the only documented Bouw instance is later. Withdrawing it moves the
    # traced-item and per-person totals, so it is left for the operator.
    originator="Gerardus Bouw", originator_work="Geocentricity", year="1992",
    real_source="Tifft 1976, ApJ 206:38; Tifft & Cocke 1984, ApJ 287:492; "
                "Napier & Guthrie 1997, J. Astrophys. Astr. 18:455; Humphreys, TJ 16(2), 2002",
    verdict="REFUTED",
    note="The periodicity survives only in frames defined by the Earth's motion, and the "
         "shell reading fails its own author's blurring criterion by a factor of eight; "
         "large-sample tests reduce it to ~2σ rather than eliminating it."),
"E13": dict(lane="E", name="Supernova dimming, BAO, birefringence and Lyman-alpha anisotropy",
    # Corrected 2026-08-08. This cluster was one of THIRTY carrying `originator: None`,
    # and only one of the thirty had ever been audited. E13 was the second test and it
    # came back the other way: three of six items have a documented ancestor in
    # Sungenis & Bennett. The birefringence item is the firmest — Vol. II gives Nodland
    # and Ralston three pages under a subheading reading simply "Birefringence:" and
    # closes by placing the axis "in the ecliptic plane along the equinox", which is
    # where the item's two content words come from. "Untraced" was our claim, not a
    # fact about the list, and it did not survive contact.
    originator="Robert Sungenis & Robert Bennett",
    originator_work="Galileo Was Wrong, Vol. II (7th ed., 2013), ch. 10; Vol. I, chs 2-3",
    year="2013", real_source=None,
    verdict="NOT DEMONSTRATED",
    note="Real anomalies, none of which discriminate. Three of six items trace to Sungenis "
         "& Bennett; the cluster was recorded as untraced until audited 2026-08-08."),
"E14": dict(lane="E", name="Solar anomalies (oblateness, neutrinos, apex, barycentre wobble)",
    # Note extended 2026-08-10: it answered only two of the four topics in the cluster's
    # own title, and the oblateness silence was the costly one, because the treatment's
    # verdict_challenge argues item 195 is a live 2025 question. Origin fields stay None:
    # four of the five items have a page-located counterpart in Galileo Was Wrong Vol. I
    # (oblateness pp. 1003-1004, apex p. 959, barycentre pp. 198-199 and 598-603) and
    # item 192 has none in the volume searched, but a content match is not a transmission
    # chain and the list carries no citations. That parallel was NOT written into
    # real_source: that field records whose genuine work is being cited, and build.py
    # dates the two-clocks section off it, so a geocentric book there would be counted as
    # a piece of dated science.
    originator=None, originator_work=None, year=None, real_source=None,
    verdict="REFUTED",
    note="The solar neutrino problem was solved by neutrino oscillation (SNO 2001; Nobel "
         "2015). The barycentre wobble is a prediction of the Sun being orbited by "
         "planets, and Jupiter displaces the Sun 1,654 times as far as the Earth does. "
         "The solar apex is what is left after Galactic rotation has been subtracted out "
         "by construction. The Sun's exact oblateness is still argued over in the 2025 "
         "literature, but a small stable flattening is what the standard picture expects, "
         "and MESSENGER broke its degeneracy with Mercury's perihelion."),
"E15": dict(lane="E", name="VLBI, interferometry and Gaia reductions assume an Earth frame",
    originator=None, originator_work=None, year=None, real_source=None,
    verdict="MISLEADING",
    note="Same convenience-frame error as R08. VLBI is in fact one of the instruments that *measures* Earth orientation and rotation to microsecond precision."),
"E16": dict(lane="E", name="Meteor, bolide and micrometeor distributions",
    originator=None, originator_work=None, year=None, real_source=None,
    verdict="STANDARD PHYSICS", note="Meteor-shower radiants and calendar fixity are consequences of Earth's orbit crossing debris streams — a heliocentric prediction."),
"E17": dict(lane="E", name="Observed isotropy / Earth-centred fields imply we are the centre",
    originator=None, originator_work=None, year=None, real_source=None,
    verdict="MISLEADING",
    note="Isotropy is observed from every vantage point in a homogeneous universe — that is the standard result, not an anomaly. The Earth's magnetosphere is Earth-centred because it is the Earth's field."),
"E18": dict(lane="E", name="Solar-system angular-momentum distribution problem",
    originator=None, originator_work=None, year=None, real_source=None,
    verdict="STANDARD PHYSICS", note="A question in planetary-formation theory (magnetic braking, disc transport), not evidence about Earth's motion."),
}
