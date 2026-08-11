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
    # note rewritten 2026-08-11, anchored on the "A08" key. The old basis line led with
    # "The atmosphere co-moves", which is the reply the treatment's own steelman files as
    # SURFACE ("this loses, and it deserves to") and which the refutation explicitly
    # declines to make - so the summary line under the verdict chip was the one answer the
    # body refuses. It also asserted descent from Rowbotham's vertical-projectile argument,
    # which the treatment argues cannot hold. The originator/work/year fields still name
    # Rowbotham for an argument about aeroplanes; that is an operator decision because
    # withdrawing it moves the traced/untraced totals and the Rowbotham item count.
    originator="Samuel Rowbotham", originator_work="Earth Not a Globe", year="1865",
    real_source="Inertial navigation systems measure Earth rate on every flight",
    verdict="REFUTED",
    note="A pre-flight IRS alignment derives the aircraft's own latitude from the sensed Earth rate and refuses to complete if that disagrees with the crew entry; Earth rate, transport rate and Coriolis stay in the mechanisation for the rest of the flight."),

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
    # Corrected 2026-08-11, anchored on the "A11" key. Two of the note's three factual
    # claims were wrong on our own evidence and the note renders directly above a section
    # headed "The higher altitude did not happen": Pease and Pearson did the observing
    # under Michelson's direction (Swenson, The Ethereal Aether, p. 220), and the
    # apparatus was in the Mount Wilson Observatory's PASADENA laboratory (pp. 220-221),
    # not on the mountain - it went up the mountain in summer 1930, after publication.
    # real_source also gained the Nature printing: the sentence the downstream tradition
    # quotes ("no displacement as great as one-fifteenth") is Nature 19 Jan 1929, and the
    # two 1929 printings give different limits. Both citations are 1929, so no dated-work
    # figure moves.
    originator="Robert Sungenis & Robert Bennett", originator_work="Galileo Was Wrong, Vol. I", year="2006",
    real_source="Michelson, Pease & Pearson, Nature 123:88 (19 Jan 1929); J. Opt. Soc. Am. 18(3):181–182 (Mar 1929) — the two printings state different limits",
    verdict="STANDARD PHYSICS",
    note="A high-precision repeat of Michelson–Morley (expected 0.9 fringe, measured 0.01), run by Pease and Pearson under Michelson at the Mount Wilson Observatory's Pasadena laboratory, specifically to test Miller. Same non-discriminating status as A01."),

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
    # note replaced 2026-08-11, anchored on the "A14" key (the originator= line is
    # byte-identical in seven clusters). Neither half of the old note was verified and the
    # first failed a check: "rotation of the earth" is not located in the archive.org OCR
    # of Alger, The Groundwork of Practical Naval Gunnery (1917), and the mechanical
    # fire-control-computer claim was not tested at all. The earliest gunnery document
    # reached is FM 6-40 (1945). Two fields are NOT changed here because they move
    # published figures and are the operator's: the Rowbotham attribution (the gunnery
    # vocabulary is not located in the 1865 text), and real_source, where the proposed
    # "TC 3-09.81 (2016); FM 6-40 (1945)" would date this A-lane cluster post-1950 and
    # break the "R12 is the only post-1950 citation outside misappropriated astronomy"
    # test.
    originator="Samuel Rowbotham", originator_work="Earth Not a Globe", year="1865",
    real_source="Standard long-range fire-control tables",
    verdict="REFUTED",
    note="US Army firing tables have carried a rotation-of-the-earth correction, indexed by the latitude of the battery, since at least FM 6-40 of 1945; the 2016 cannon gunnery manual lists it under both range and deflection effects."),

"A15": dict(lane="A-EXP",
    # name and note replaced 2026-08-11, anchored on the "A15" key. The old name asserted
    # one claim the four items do not share and that is false of two of them - torsion
    # balances do return nulls and pendulum apparatus really is sensitive to its mounting
    # (the treatment's §9, which is why REFUTED was rejected). The old note, "No specific
    # published measurement is cited by the list", is true of all 461 items - the specimen
    # carries no citation anywhere - so it carried no A15-specific information while
    # rendering as the basis line under the verdict chip.
    name="Gravimeters, pendulum clocks and torsion balances register nothing of the Earth's motion",
    originator=None, originator_work=None, year=None, real_source=None,
    verdict="NOT DEMONSTRATED", note="Two of the four items state true things; what is not stated is the step from an instrument reading to a conclusion about the Earth. Measured gravity varies by 0.53% with latitude and by 100–300 microgal with the tide."),

"A16": dict(lane="A-EXP", name="High-altitude balloon drift and sun-angle anomalies",
    # note replaced 2026-08-11, anchored on the "A16" key. "No dataset cited." renders
    # next to the verdict chip and misstates the failure: the observation is real and
    # accurately reported (balloons do return near their launch point; Baumgartner landed
    # in eastern New Mexico), and what fails is the inference. The verdict is left alone -
    # a verdict_challenge proposing REFUTED is filed in the treatment and moving it would
    # move the published verdict distribution.
    originator=None, originator_work=None, year=None, real_source=None,
    verdict="NOT DEMONSTRATED", note="The observation is real and accurately reported — balloons do come down near where they went up — and the step from it to a stationary Earth is what is missing. A radiosonde drifts several hundred kilometres while the air moves east with the ground at 388 m/s."),

"A17": dict(lane="A-EXP", name="Conservation-of-momentum paradox for a moving Earth",
    originator="Samuel Rowbotham", originator_work="Earth Not a Globe", year="1865",
    real_source=None, verdict="REFUTED", note="Galilean relativity, established 1632."),

"A18": dict(lane="A-EXP", name="GPS/time-dilation corrections work in an Earth frame",
    originator="Robert Sungenis & Robert Bennett", originator_work="Galileo Was Wrong, Vol. I", year="2006",
    real_source="GPS relativistic clock corrections",
    verdict="STANDARD PHYSICS", note="GPS corrections are computed in an Earth-centred inertial frame precisely because the Earth rotates within it."),

"A19": dict(lane="A-EXP", name="Gyrocompasses are sky-locked, not Earth-locked",
    # note replaced 2026-08-11, anchored on the "A19" key. The old second sentence - "It
    # cannot function on a non-rotating Earth" - is answered in one line by the source and
    # is conceded in bold by the refutation printed directly beneath it: on a stationary
    # Earth inside a rotating cosmos the local inertial frame is dragged and the instrument
    # reads normally (Sungenis & Bennett, Vol. I pp. 710-713, and they are right). The
    # basis line was the popular version of the debunk this entry exists to warn against.
    # What survives is the latitude dependence, which no flat surface can supply.
    originator=None, originator_work=None, year=None,
    real_source="Gyrocompass operating principle",
    verdict="SELF-CONTRADICTED", note="A gyrocompass finds north from the horizontal component of the rotation vector, which goes as cos(latitude) — maximum at the equator, zero at the poles. That latitude dependence is unavailable on a flat surface whatever is rotating."),

"A20": dict(lane="A-EXP", name="Lunar laser ranging shows a fixed baseline",
    originator=None, originator_work=None, year=None,
    real_source="Apollo/Lunokhod retroreflector ranging",
    verdict="NOT DEMONSTRATED", note="No measurement cited; LLR data in fact resolve Earth rotation and lunar recession."),

"A21": dict(lane="A-EXP", name="Satellites and geostationary orbits reinterpreted in an Earth-fixed frame",
    # note replaced 2026-08-11, anchored on the "A21" key. The old note quoted Shenton's
    # "Isle of Wight" line as sourced. "Wight" returns zero hits in Schadewald, The Plane
    # Truth ch. 9 as retrieved 2026-08-11 - the text people.py cites for PER-SHENTON - so
    # the quotation is widely attributed but not verified from the source our own record
    # leans on, and it must not be repeated as sourced. (The same unsourced quotation is
    # in claude/source-genealogy.md, Lineage 1 table, Shenton row; not this file's to fix.)
    # The originator/work/year fields are NOT changed here: withdrawing them moves the
    # traced/untraced split, and the four faults in them are filed for the operator.
    originator="Samuel Shenton", originator_work="International Flat Earth Research Society", year="1957",
    real_source=None, verdict="STANDARD PHYSICS",
    note="A rotating-heavens model reproduces the geostationary result by taking the equator, the altitude and the rotation rate from the rotating-globe solution as inputs. Reproducing a rival's number at the rival's location is agreement, not a measurement of its own."),

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
    # note replaced 2026-08-11, anchored on the "A27" key. "No mechanism specified." is
    # contradicted by the treatment printed beneath it: Rowbotham 1865 §10 specifies one in
    # detail and derives four consequences from it (Winship 1899 p. 131 and Scott 1901
    # pp. 258-261 restate it), the Christian Flat Earth Ministry page of 2015 adds a polar
    # vortex, and Sungenis & Bennett p. 794 add a latitude-varying ether flow. Mutually
    # incompatible mechanisms are a different and worse problem than silence. The name is
    # left alone: "sky torque" is item 233's own wording, and cluster names state the
    # list's claim. Verdict untouched - a verdict_challenge proposing REFUTED is filed.
    originator=None, originator_work=None, year=None, real_source=None,
    verdict="NOT DEMONSTRATED", note="Mechanisms are specified — Rowbotham's atmosphere pressing on a floating plate, a polar vortex, a latitude-varying ether — and they are mutually incompatible. None of them ties to the 12 h 25 min lunar period the tide records carry."),

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
    # Verdict changed 2026-08-10, STANDARD PHYSICS -> MISLEADING. STANDARD PHYSICS means
    # "real, already explained, does not discriminate", and the note directly contradicted
    # the middle clause: Mach's principle is an unfinished programme, not settled physics
    # (Bondi and Samuel enumerate eleven inequivalent statements, some of which GR
    # violates). What the source does is quote real papers by Lynden-Bell, Katz and Bicak
    # and by Barbour and Bertotti under headings like "Lynden-Bell's Geocentrism" and
    # conclude that geocentrism "has been established" — real data, wrong conclusion made
    # to look supported, which is MISLEADING. Recorded counter-case: under Assis's
    # relational mechanics the equivalence does hold, so one branch of the cluster is
    # arguably true-but-non-discriminating. That branch is not the one carrying the weight.
    verdict="MISLEADING", note="Mach's principle is not a settled part of GR — Bondi and Samuel count eleven inequivalent versions — and no version privileges the Earth. The zero-angular-momentum theorem is quoted accurately and then read as support for the arrangement it excludes."),

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
    # note replaced 2026-08-11, anchored on the "R05" key. "Frame dragging … is far too
    # small to hold the stars in a daily circuit" compares the Earth-generated effect with
    # a cosmological one and bounds nothing; the treatment's steelman files that exact
    # formulation as "SURFACE (weak — do not use) … This loses, and it loses in one move"
    # (a defender with Brill & Cohen 1966 in hand wins it: dragging becomes complete as a
    # shell approaches its own gravitational radius, and the observable universe is within
    # a factor of about two of its own). It rendered both under the verdict chip and as the
    # summary line of section 3. NOT used: the previous pass's suggested replacement about
    # spatially homogeneous rotating solutions, which is now known to mischaracterise
    # ch. 10 - the chapter runs on rotating SHELLS. real_source is left alone: replacing
    # Gödel 1949 / Gravity Probe B with 1918/1992/2004 moves the two-clocks median and the
    # pre-1930 share, and that is an operator decision with a test to re-run.
    originator="Robert Sungenis & Robert Bennett", originator_work="Galileo Was Wrong, Vol. I", year="2006",
    real_source="Gödel 1949; Lense–Thirring 1918; Gravity Probe B",
    verdict="MISLEADING", note="The chapter's own citations give a rotating shell, and a shell distinguishes its own centre, not whatever body sits there. And the frame-dragging measurement offered as support is computed from the Earth's own angular momentum: set the Earth's spin to zero and the predicted LAGEOS precession is zero."),

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
    # note replaced 2026-08-11, anchored on the "R11" key. Two faults in one sentence, both
    # on the skim path. (1) It stated as Bouw's settled position one horn of the
    # contradiction this entry exists to expose, and §3 of the treatment says the opposite:
    # on the same book's p. 3 "every fundamental experiment ever devised to measure the
    # speed of the earth through space measures a speed of zero", p. 523 geocentricity
    # "predicts" what experiments detect, p. 539 the geocentric evidence has "forced" the
    # model. The theological move is real but narrow - the Earth-versus-Milky-Way residual
    # at p. 556 and the Bible-believer sufficiency claim at p. 15 - and the note generalised
    # it into his whole position. (2) "the movement's only credentialed astronomer" is an
    # unscoped superlative over an entire movement, untested by any pass, in the
    # highest-traffic field on the entry; withdrawn rather than rescoped. The same
    # overstatement is in claude/source-genealogy.md and claude/social-section-framing.md
    # §3 and should be qualified in all three places at once - not this file's to fix.
    # A parallel batch-11 pass reaches the opposite provenance conclusion (the contradiction
    # printed in Sungenis & Bennett rather than in Bouw); this wording follows the live
    # treatment, _b10_R11, which is the one deep.py loads. originator/year and real_source
    # (Ellis 1978) are unresolved and move published figures: operator.
    originator="Gerardus Bouw", originator_work="Geocentricity", year="1992",
    real_source=None, verdict="SELF-CONTRADICTED",
    note="Bouw states the symmetry himself — dynamical proofs “are not proofs of anything; nor are they proofs against the geocentric universe” — and elsewhere in the same book calls the geocentric evidence overwhelming and reports his model as making predictions that experiments confirm. The list files the first claim as a proof while spending the second. Where the astronomical evidence runs out, at the Earth-versus-Galaxy gap, he names Scripture as what closes it."),

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
    # note replaced 2026-08-11, anchored on the "B02" key (the originator= line is
    # byte-identical across B02/B06/B07/D12; a positional replace on it is how the batch-7
    # E03 correction landed on E01). render.py prints basis twice inside this entry, and
    # the old sentence was the exact objection the treatment shows Rowbotham anticipated,
    # reproduced with his own theodolite and answered with a lens-free instrument - our
    # case at its weakest, stated on the skim path. NOT used: the earlier suggestion that
    # "his own optics exempt the axis his own method uses", which he answers in the same
    # section of the enlarged edition (pp. 203-204). The square-root clause is what the
    # body rests on. year/originator_work are the operator's: the material is in the 1865
    # book and the enlarged editions, and the 1849 pamphlet was not reached for review.
    originator="Samuel Rowbotham", originator_work="Zetetic Astronomy", year="1849",
    real_source=None, verdict="REFUTED", note="Rowbotham measured the theodolite dip himself and blamed the lenses; but the dip grows as the square root of the height, which no lens does."),

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
    # note and real_source 2026-08-11, anchored on the "B07" key, never on the originator=
    # line (byte-identical across B02/B06/B07/D12). (1) The note asserted that refraction
    # "was described before the dispute" with nothing to check it against; the treatment
    # documents it (Lehn & van der Werf, Appl. Opt. 44:5624, 2005), so the basis line now
    # carries the two dates. (2) real_source was null although the source names and
    # reprints one - the same Britannica article already recorded under B06. It carries no
    # year, so no dated-work figure moves. NOT changed here: year=1849, where the two
    # reports disagree (1881 for the shilling-in-a-basin and the barometer control, 1865
    # for the fuller Britannica extract) - an operator call, and an edition correction
    # belongs in review/corrections.json, which this agent does not own.
    originator="Samuel Rowbotham", originator_work="Zetetic Astronomy", year="1849",
    real_source="Encyclopaedia Britannica article 'Levelling', as reprinted by Rowbotham — the Britannica edition it was taken from has not been identified",
    verdict="MISLEADING",
    note="Refraction is independently measurable and was described before the dispute — Tycho measured it and published in 1596, Gauss put the surveying coefficient near 0.13 from the Hannover triangulation of the 1820s — and it is used in the same form by surveyors who are not arguing about Earth's shape."),

"B08": dict(lane="B", name="Star trails / Polaris fixed / southern circumpolar geometry",
    originator="Eric Dubay", originator_work="200 Proofs Earth Is Not a Spinning Ball", year="2015",
    real_source=None, verdict="REFUTED",
    note="Southern-hemisphere circumpolar star trails around a *southern* pole are impossible on any single-plane model. This is the item the flat model most clearly gets wrong."),

"B09": dict(lane="B", name="Plumb lines are perpendicular everywhere",
    # note replaced 2026-08-11, anchored on the "B09" key. "converges toward the centre"
    # is not right and it rendered next to the verdict chip: the local vertical does not
    # pass through the geocentre - on a smooth WGS84 ellipsoid it misses by up to 11.55
    # arcminutes at latitude 45, and local deflections add tens of arcseconds on top. That
    # gap is the cluster's whole subject and von Gumpach's circularity charge, so conceding
    # it accurately is stronger than eliding it. The old wording also conflated deflection
    # of the vertical (departure from the ellipsoid normal) with the convergence of
    # neighbouring plumb lines. Left for the operator: year (the plumb-line passage is in
    # the 1881 third edition, not the 1865 text searched - an edition correction needs a
    # corrections.json entry), the Carpenter half of the attribution, and real_source.
    originator="Samuel Rowbotham", originator_work="Earth Not a Globe", year="1865",
    real_source=None, verdict="REFUTED", note="Plumb lines follow local gravity, whose direction varies from place to place and is measured rather than assumed: deflection-of-the-vertical surveys read it against the star field to 0.1 arcsecond, and the Verrazzano-Narrows towers were built 41.275 mm farther apart at the top than at the base."),

"B10": dict(lane="B", name="Sun and Moon appear the same size; solar diameter constant",
    # note replaced 2026-08-11, anchored on the '"B10"' key and NOT on the originator=
    # line (byte-identical across B02/B06/B07/D12 - the route by which the batch-7 E03
    # correction landed on E01). The old note credited the Sun's 3.4% swing with producing
    # both eclipse types. §1 of the treatment publishes the figures that contradict it:
    # the Moon runs 29'26" to 33'30" against the Sun's 31'36" to 32'42", and the Moon's
    # mean disc is the SMALLER of the two (31.07' against 31.97'), which is why a central
    # eclipse is sometimes annular. The page was disagreeing with itself. The percentage
    # figures the two reports proposed for the Moon's swing (~13.8% / ~14%) are not
    # computed in the treatment, so the ranges are given instead. Origin fields and
    # real_source, and the composite split (item 31 -> Winship 1899, 97/220 -> Carpenter
    # 1885), are the operator's: they move published counts.
    originator="Samuel Rowbotham", originator_work="Earth Not a Globe", year="1865",
    real_source=None, verdict="MISLEADING",
    note="Coincidence of angular size is real and well known. The Sun's disc does vary, 31′36″ to 32′42″; the Moon's varies over a wider range, 29′26″ to 33′30″, and its mean disc is the smaller of the two — which is why a central eclipse is sometimes annular."),

"B11": dict(lane="B",
    # name and note replaced 2026-08-11, anchored on the "B11" key. (1) The name promised
    # an instrument the cluster does not contain: item 391 "LiDAR ECEF." is assigned to
    # R08 (assign.py), correctly, and B11's four items are 217, 390, 392 and 400. The name
    # renders in the H3 heading. (2) The basis line "All of these run on ellipsoidal
    # datums" is true of 390 and 392 and is not the answer to 217 or 400 - a radar horizon
    # is not a datum question and a sonar ray path is not a datum question - and the
    # refutation printed beneath it opens by saying exactly that. The alternative wording
    # proposed by the earlier pass ("every one of these fields publishes the limit of its
    # own flat approximation") was not used: the treatment's own first paragraph splits the
    # cluster two-and-two, and that is what the summary line should carry.
    # originator/real_source stay None - the search confirmed untraced, and do NOT
    # populate real_source with "WGS84, ITRF" by analogy with R08.
    name="Radar, photogrammetry, SAR and sonar assume a plane",
    originator=None, originator_work=None, year=None, real_source=None,
    verdict="MISLEADING", note="Two of the four are datum questions and are answered at R08; a radar horizon and a sonar ray path are not, and are answered on the measurements."),

"B12": dict(lane="B", name="Polar navigation and dead reckoning imply a dome/disc",
    # note replaced 2026-08-11, anchored on the "B12" key. Two faults, both on the skim
    # path: (a) the old note answered none of the cluster's three items, which are about
    # charts, polar navigation practice and dead reckoning - the midnight-sun observation
    # is a different argument; (b) "any disc model" is an unscoped universal, where what
    # the December 2024 observation bears on is the north-centred disc of the
    # Gleason/Rowbotham type. The replacement is the scale-free result the treatment turns
    # on, which does reach all three items. The Campanella concession is unaffected and
    # stays in the body. The originator (no Johnson text carrying a navigation argument was
    # reached; a documented Rowbotham/Carpenter chain exists) moves items between people
    # and is the operator's.
    originator="Charles K. Johnson", originator_work="Flat Earth News", year="1972",
    real_source=None, verdict="REFUTED",
    note="A degree of longitude measures 111.32 km at the equator and 78.85 km at 45°S, where every north-centred disc requires it to be longer in the south."),

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
    # Verdict changed 2026-08-10, NOT DEMONSTRATED -> REFUTED. The note already said the
    # claim was "false in detail" while the verdict said the argument merely failed to
    # reach its conclusion; those do not sit together. Three of the four items carry an
    # explicit universal ("uniformly", "universal", "all"), and a universal falls to one
    # counterexample. There are six, all from ancient primary witnesses rather than modern
    # reconstruction. Eratosthenes was dropped from the note: he measured the Earth's
    # SHAPE, not its place, so he answers a claim this cluster does not make.
    originator="Robert Sungenis", originator_work="Galileo Was Wrong, Vol. II", year="2006",
    real_source=None, verdict="REFUTED",
    note="Appeal to antiquity, and false as stated. Philolaus (via Aristotle, De caelo II.13), Hicetas, Heraclides, Ecphantus, Aristarchus (via Archimedes, Sand-Reckoner) and Seleucus (via Plutarch) all placed the Earth in motion; Aryabhata did so in 499 CE."),
"D02": dict(lane="D", name="Named ancient authorities (Plato, Aristotle, Ptolemy, Tycho)",
    originator="Robert Sungenis", originator_work="Galileo Was Wrong, Vol. II", year="2006",
    real_source=None, verdict="NOT DEMONSTRATED",
    note="Every one of them held the Earth to be a *sphere*. Citing them supports geocentrism at best, and actively refutes the flat half of the list."),
"D03": dict(lane="D", name="Geocentric/Ptolemaic models made accurate predictions",
    # Volume corrected 2026-08-11, anchored on the "D03" key - the originator= line is
    # byte-identical across D01, D02 and D03. The material is in VOLUME I in both
    # arrangements: 2006 scan ch. 1 pp. 41-43 and ch. 4 pp. 210-212; seventh edition Vol. I
    # ch. 1 pp. 40-41 and 55-56 and Vol. I ch. 2 "Objection #16". Vol. II in this project's
    # settled reading is chs 7-13, the Michelson/Sagnac/Pioneer half, and none of this
    # cluster is there. Same shape as the D15 correction of 2026-08-09. The originator and
    # year do not survive checking either - three strands with three ancestries, the Venus
    # answer quoted from Bouw 1992, fourteen years before our recorded year - but
    # withdrawing them moves the traced/untraced totals, so that is filed for the operator.
    originator="Robert Sungenis", originator_work="Galileo Was Wrong, Vol. I", year="2006",
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
    # note replaced 2026-08-11, anchored on the "D09" key. The old wording ran two
    # different things together: astrological planetary positions are GEOCENTRIC apparent
    # places, referred to the Earth's centre, and only the house cusps (plus the optional
    # lunar-parallax correction) are TOPOCENTRIC, depending on the observer's latitude and
    # longitude. §4 of the refutation printed beneath it keeps them apart deliberately, so
    # the record was contradicting the entry it heads. originator/real_source are left
    # None: the located ancestor (Hall 1928, already WRK-HALL-1928 in works.py) is an
    # ancestor and not an origination, and filling either field moves published counts.
    originator=None, originator_work=None, year=None, real_source=None,
    verdict="UNFALSIFIABLE", note="Astrology is geocentric because it describes appearances: chart positions are apparent places referred to the Earth's centre, and only the house cusps and the optional lunar-parallax correction are topocentric. Neither requires the Earth to be fixed."),
"D10": dict(lane="D", name="Heliocentrism has occult/masonic roots",
    originator="Marshall Hall", originator_work="The Earth is not Moving", year="1991",
    real_source=None, verdict="NOT DEMONSTRATED",
    note="Genetic fallacy. Where an idea came from is not evidence about whether it is true."),
"D11": dict(lane="D", name="Perception is reliable; the observer defines the centre",
    originator="Samuel Rowbotham", originator_work="Zetetic Astronomy (the zetetic method)", year="1849",
    real_source=None, verdict="NOT DEMONSTRATED",
    note="Rowbotham's founding move — 'observation is real, theory is imaginary'. It is the epistemology the whole genre rests on, and it is the thing actually being defended."),
"D12": dict(lane="D", name="Simplicity / common sense favours a fixed Earth",
    # note replaced 2026-08-11, anchored on the "D12" key, never on the originator= line
    # (byte-identical across B02/B06/B07/D12). The old second clause reached only the flat
    # branch, while item 83 says "geocentrism", which in this list's other lineage is a
    # globe Earth with an ordinary southern sky - so the basis line under-described half
    # its own cluster. The replacement carries both branches, as the refutation does.
    # year/originator_work are NOT changed: the passage is in the 1865 book (Section XIV,
    # pp. 180-181) and again in the 1881 third edition, and the 16-page 1849 pamphlet was
    # not reachable - an edition correction that needs a corrections.json entry, which is
    # the operator's to make.
    originator="Samuel Rowbotham", originator_work="Zetetic Astronomy", year="1849",
    real_source=None, verdict="NOT DEMONSTRATED", note="Parsimony is not a measurement. The plane leaves the southern sky unpaid, and turning the whole sky daily instead has to buy a rotating universe or an aether — the purchase this list calls a 'modern epicycle' when cosmologists make it."),
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
    # note replaced 2026-08-11, anchored on the "D17" key. "the number only comes out right
    # on a globe" is false and it was live in docs/index.html in two places (render.py
    # prints basis under the verdict chip and again as the Refutation summary): Schumann's
    # ideal formula f_n = (c/2*pi*a)*sqrt(n(n+1)) with a = 6371 km gives 10.59 Hz against
    # an observed 7.83 Hz, a 26% miss explained by finite ionospheric conductivity. The
    # load is on the mode ratios, which contain no cavity size. The proposed opening
    # sentence - that Sargent's model is real but is not the source of these three items -
    # is NOT included here: it presumes the originator withdrawal, which moves published
    # counts and is the operator's, and printing it under a meta line still reading "first
    # published by Mark Sargent" would swap one self-contradiction for another. The
    # treatment's past-tense disclosure sentence is likewise held until that lands.
    originator="Mark Sargent", originator_work="Flat Earth Clues", year="2015",
    real_source="Schumann resonance (real, and a consequence of a spherical cavity)",
    verdict="NOT DEMONSTRATED",
    note="The Schumann resonance is derived from the Earth-ionosphere cavity treated as a *sphere* of radius 6371 km; the ideal formula misses the observed 7.83 Hz by 26%, and the load sits on the mode ratios, which contain no cavity size."),
"D19": dict(lane="D", name="Eclipse and lunar cycles are tuned to human timekeeping",
    # Verdict changed 2026-08-10, UNFALSIFIABLE -> MISLEADING, and the four origin fields
    # filled. UNFALSIFIABLE was chosen from the CLUSTER NAME: "tuned to human timekeeping"
    # reads as a design claim, and a design claim is indeed untestable. But no source
    # making the design claim could be located. The sourced argument is different and
    # checkable — Rowbotham's eclipse chapter, where the Saros, the node and the apogee
    # appear and the point built on them is that eclipse prediction is theory-independent.
    # That descends intact to Dubay 2018 and is carried without the cycle names by
    # Carpenter's proof 66 of 1885, so the route is overdetermined even where the
    # vocabulary is not. Its factual core about ancient practice is true and the inference
    # does not follow: MISLEADING. Recorded and not taken: SELF-CONTRADICTED, on the ground
    # that a node and a draconic month are defined only by an inclined orbit crossing the
    # ecliptic, so the items cite the globe model's own measurements against it. The
    # primary source argues about method rather than about the cycles, so MISLEADING fits
    # the source better — and the hedge rule says we answer the source.
    # ORIGIN FIELDS HELD, NOT FILLED, and this is an operator decision rather than a
    # research one. The treatment's evidence points at Rowbotham's eclipse chapter, and on
    # that evidence originator="Samuel Rowbotham", originator_work="Zetetic Astronomy:
    # Earth Not a Globe", year="1865" would be right. But crediting it moves three
    # published headlines at once: traced items 348 -> 352, untraced 97 -> 93, and
    # Rowbotham 65 -> 69, which tips the Rowbotham-plus-Sungenis share from 43% to 44%.
    # The operator approved a verdict change, not an attribution change. Held deliberately
    # — and note the direction: leaving it None publishes this cluster as untraced when we
    # have a candidate source, so the untraced figure is an upper bound here in the way the
    # README already says it is generally.
    originator=None, originator_work=None, year=None,
    real_source="Saros cycle, 6,585.32 days; Metonic cycle, 19 years",
    verdict="MISLEADING", note="Saros and Metonic cycles are consequences of orbital periods; the calendars were built to fit them, not the reverse. Nor are the cycles exact: the Saros drifts about half a degree off the node per repeat, and its series are catalogued as beginning and ending."),

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
    # Verdict changed 2026-08-10, REFUTED -> MISLEADING, and this was the urgent one.
    # REFUTED is defined on this page as "contradicted by a specific measurement". That is
    # exactly right for three of the five items, and WRONG for the topic the cluster is
    # named after: solar oblateness and its cycle variation are genuinely unresolved in the
    # current literature, so publishing REFUTED over item 195 called an open measurement
    # closed. A defender who has read Meftah or Mecheri could show that, and would be
    # right. It is also the opposite of the restraint this project insists on at ARG-E01,
    # where the page keeps saying the CMB axis debate is live.
    #
    # MISLEADING is the defensible verdict for the BUNDLE, because the bundle's move is
    # assembling true or arguable solar facts behind an inference nobody states. The
    # per-item reading the treatment argues for — REFUTED on 104, 138 and 192, MISLEADING
    # on 361, NOT DEMONSTRATED on 195 — is better still, and cannot be expressed: the
    # schema carries one verdict per cluster. That limitation is now a live design item.
    verdict="MISLEADING",
    note="The solar neutrino problem was solved by neutrino oscillation (SNO 2001; Nobel "
         "2015). The barycentre wobble is a prediction of the Sun being orbited by "
         "planets, and Jupiter displaces the Sun 1,654 times as far as the Earth does. "
         "The solar apex is what is left after Galactic rotation has been subtracted out "
         "by construction. The Sun's exact oblateness is still argued over in the 2025 "
         "literature, but a small stable flattening is what the standard picture expects, "
         "and MESSENGER broke its degeneracy with Mercury's perihelion."),
"E15": dict(lane="E",
    # name and note replaced 2026-08-11, anchored on the "E15" key, NEVER on the shared
    # `originator=None, originator_work=None, year=None, real_source=None,` line, which is
    # byte-identical across E14/E15/E16 and others. (1) "…assume an Earth frame" describes
    # the R08 convenience-frame argument, while the entry's gloss says in terms that the
    # claim is a circularity charge, not a frame-convention point, and the located source
    # argues the stronger thing. (2) The old note's "microsecond precision" was not
    # verified from anything read for the entry, and the note was silent on Gaia, one of
    # the cluster's three items. Two name proposals were on file; the one kept names all
    # three instruments, because a heading for a three-instrument cluster should not drop
    # two of them. real_source stays None: ICRF3 (2020) and Gaia EDR3 would date this
    # cluster and move the two-clocks figures, so it is the operator's.
    name="VLBI, interferometry and Gaia reductions presuppose the Earth's motion",
    originator=None, originator_work=None, year=None, real_source=None,
    verdict="MISLEADING",
    note="The reductions estimate the transformation between an Earth-fixed and a sky-fixed frame rather than assuming it; ICRF3 sessions observe tens to hundreds of sources each and measured the solar system's own galactic acceleration at 25 sigma, and Gaia's frame orientation and its 17-microarcsecond parallax bias are published corrections rather than hidden freedoms."),
"E16": dict(lane="E", name="Meteor, bolide and micrometeor distributions",
    # note replaced 2026-08-11, anchored on the "E16" key and NOT on the shared
    # `originator=None, …` line (byte-identical across E14/E15/E16 - the batch-7 E01/E03
    # misfire was manufactured exactly that way). The old note covered item 239 only, while
    # the cluster bundles 238, 239 and 242 and the entry's verdict_challenge turns on 242
    # being different in kind; a note that never mentions it misdescribes the chip it sits
    # beside. Same shape as the E08 defect. real_source stays None deliberately: it feeds
    # the "two clocks" median and the post-1950 lane-E tally, so adding the 2008-2020
    # meteor literature is a dataset change and the operator's call.
    originator=None, originator_work=None, year=None, real_source=None,
    verdict="STANDARD PHYSICS", note="Shower dates are positions in the Earth's orbit, catalogued by solar longitude rather than by calendar. Meteorite-dropping bolides cluster near 18h local time, and the small-particle influx has six standing sources in a frame centred on the apex of the Earth's way."),
"E17": dict(lane="E", name="Observed isotropy / Earth-centred fields imply we are the centre",
    originator=None, originator_work=None, year=None, real_source=None,
    verdict="MISLEADING",
    note="Isotropy is observed from every vantage point in a homogeneous universe — that is the standard result, not an anomaly. The Earth's magnetosphere is Earth-centred because it is the Earth's field."),
"E18": dict(lane="E", name="Solar-system angular-momentum distribution problem",
    originator=None, originator_work=None, year=None, real_source=None,
    verdict="STANDARD PHYSICS", note="A question in planetary-formation theory (magnetic braking, disc transport), not evidence about Earth's motion."),
}
