# -*- coding: utf-8 -*-
"""
ARG-A07 — "Gyroscopes / ring-laser gyros show no Earth rotation" (verdict SELF-CONTRADICTED).
Batch 8. Work record WRK-BTC-2018 (pd=False), items 12, 19, 112, 225, 374.

Written under THE HEDGE RULE. The list fragment ("Gyroscope anomalies indicating no
rotation.") states the reverse of the only source text we can hold it against — the
originator's own filmed report of what his instrument read — so the drift verdict is
`reversed`. But the fragment is not the strongest form of the argument, and refuting it
would be refuting nobody. Items 225 and 374 ("Ring laser gyro corrections", "INS Earth
updates") carry a real and correct engineering objection, and the refutation is built to
answer THAT, not item 12.

SCRUPULOUS-FAIRNESS CONSTRAINTS OBSERVED (Bob Knodel is living):
  * No claim about motive, belief, finances or state of mind anywhere in the published
    fields. The widely-circulated "$20,000 in this freaking gyro" line is deliberately
    NOT quoted; the gloss says so and says why.
  * The filmed words are treated as reported speech about an instrument reading, not as
    data and not as evidence for the Earth's rotation. The evidence is cited separately
    (Foucault 1852, Michelson-Gale 1925, Christchurch 1992, Wettzell G, Di Virgilio 2022).
  * The experimental design is credited as sound, and the systematics hunt is credited as
    correct practice. The finding is located in the protocol's missing acceptance
    criterion, which is a statement about a method, not about a person.

THINGS THIS AGENT COULD NOT REACH, recorded as unchecked and never as absent:
  * The film itself. Both transcriptions of the quote are from press write-ups; no
    timecoded viewing was made, and the surrounding edit was not verified.
  * The GlobeBusters broadcast archive. No Knodel-authored write-up of the gyroscope data
    was located, and that archive was not searched for this entry.
  * Whether an acceptance criterion was stated elsewhere in the film.

REPORTED TO PARENT, NOT FIXED HERE (no other file was touched):
  1. works.py WRK-BTC-2018 carries author="PER-KNODEL" for a film whose title field
     correctly names its director, Daniel J. Clark. Knodel is a participant in someone
     else's documentary, not its author — a different provenance relation from every
     other WRK-* record.
  2. clusters.py A07 originator_work is "GlobeBusters / Behind the Curve"; only the
     second has a WRK record, and GlobeBusters was not searched.
  3. clusters.py A07 year="2018" dates the filmed test, not the argument: a video making
     the gyroscope case was already in circulation and under discussion on Metabunk in
     March 2016.
  4. Also unmentioned in the WRK-BTC-2018 imprint: the Hot Docs festival premiere,
     30 April 2018.
None of these is asserted as a defect in published prose, per the past-tense rule.
"""

ENTRY = {

"A07": dict(

    tldr=("A ring laser gyroscope bought to test whether the Earth turns read a "
          "15-degree-per-hour drift on camera, which is the rate a rotating Earth "
          "predicts and the rate a stationary one puts at zero. The design was sound — "
          "the right instrument, the right quantity, an unambiguous prediction — and it "
          "was the right answer to the strongest form of the argument, which is that a "
          "working navigation system has Earth rotation fed into it rather than measured "
          "out of it. What the film records next is a search for something to shield the "
          "apparatus from."),

    passage=dict(
        work="WRK-BTC-2018",
        pd=False,
        locator=("Bob Knodel speaking on camera in the ring laser gyroscope sequence. "
                 "Transcribed here from two press accounts of the film — Newsweek, "
                 "15 February 2019, for the first sentence, and JOE.co.uk for the second — "
                 "which differ in small ways. No timecoded viewing of the film was made "
                 "for this entry and the surrounding edit was not verified."),
        quote=("What we found is, is when we turned on that gyroscope we found that we "
               "were picking up a drift. A 15 degree per hour drift. … We obviously were "
               "not willing to accept that, and so we started looking for ways to "
               "disprove it was actually registering the motion of the Earth."),
        gloss=(
            "<p>The provenance of this passage is unusual and worth stating before anything "
            "else is built on it. It is not a publication. It is a man speaking in a "
            "documentary someone else made &mdash; <em>Behind the Curve</em>, directed by "
            "Daniel J. Clark, festival premiere 30 April 2018, US release 15 November 2018, "
            "Netflix February 2019 &mdash; and the only reason the sentence exists at all is "
            "that a camera crew was present. Bob Knodel is living, and everything below "
            "treats these words as an honest description of what an apparatus displayed and "
            "what was done next. This page makes no claim about why.</p>"
            "<p><strong>One line is deliberately left out.</strong> The most quoted sentence "
            "from this sequence is about what the instrument cost. It is easy to find and it "
            "is not reproduced here, because the only use for it is to invite a reader to "
            "infer a motive, and inferring motive from a filmed remark is the move this "
            "review exists to object to when it is done to us.</p>"
            "<p><strong>The number.</strong> 360&deg; &divide; 24 h is 15.000&deg; per hour "
            "exactly; the sidereal rate &mdash; the one a gyroscope actually senses, because "
            "it measures rotation with respect to the local inertial frame rather than with "
            "respect to the Sun &mdash; is &Omega; = 7.292115 &times; 10<sup>&minus;5</sup> "
            "rad s<sup>&minus;1</sup>, or 15.041&deg; per hour. The two differ by 0.27 per "
            "cent. The figure as spoken carries two significant figures and cannot separate "
            "them, so nothing here claims that this apparatus resolved sidereal from solar. "
            "Large ring lasers do resolve it, routinely, and that matters for a separate "
            "reason set out under <a href=\"#ARG-A02\">ARG-A02</a>.</p>"
            "<p><strong>Why the reading is not nothing.</strong> A ring laser gyroscope has "
            "no spinning rotor and no bearings to bind. Two laser beams counter-propagate "
            "around a closed optical cavity, and rotation of the cavity with respect to the "
            "local inertial frame separates their frequencies by "
            "&Delta;<em>f</em> = 4<strong>A</strong>&middot;<strong>&Omega;</strong> / "
            "&lambda;<em>L</em>, with <em>A</em> the enclosed area, <em>L</em> the perimeter "
            "and &lambda; the vacuum wavelength. Navigation-grade units of this class are "
            "specified at bias uncertainties better than 0.01&deg; per hour &mdash; some "
            "fifteen hundred times smaller than the figure reported here. No make, model, "
            "input-axis orientation or uncertainty is given in the sequences the press "
            "transcriptions cover, so the reading is treated throughout as reported speech "
            "and never as a measurement this page relies on.</p>"
            "<p><strong>What happened next, from a secondary account.</strong> Jay L. Wile's "
            "contemporaneous review of the film describes the follow-up: the instrument was "
            "enclosed in a container excluding magnetic fields, on the hypothesis that the "
            "dome of stars was influencing it in some way; the same result came back; and a "
            "chamber made of bismuth was being sought next. That is a secondary account of a "
            "film sequence, not a laboratory record, and it is used below only for the shape "
            "of the follow-up, never for a number.</p>"
            "<p><strong>What we could not reach.</strong> No write-up of this gyroscope data "
            "authored by Knodel himself was located. The GlobeBusters broadcast archive was "
            "not searched for this entry. Unreached is not the same as non-existent, and "
            "nothing in this treatment turns on the assumption that no such record exists.</p>"
        )),

    steelman=dict(
        description=(
            "<p><strong>SURFACE (weak &mdash; do not use).</strong> &ldquo;They do not "
            "understand gyroscopes.&rdquo; This is the easy bust and it is false here, "
            "conspicuously so. The argument identifies the correct instrument, the correct "
            "physical quantity and a prediction the two models disagree about by the whole "
            "of it: a gyroscope bolted to a stationary Earth senses zero rotation with "
            "respect to inertial space, and one bolted to a turning Earth senses "
            "15.041&deg; per hour. Somebody then went and bought one. Anyone who opens with "
            "the surface reading has conceded the more interesting ground before the "
            "exchange starts.</p>"
            "<p><strong>DEEPER.</strong> The mechanical version of the claim rests on "
            "something true. A toy gyroscope, or a cheap mechanical one on jewelled "
            "bearings, genuinely cannot resolve 15&deg; per hour: static friction in the "
            "bearings and imperfect balancing swamp a rate of four thousandths of a degree "
            "per second, and the resulting real wander is larger and less predictable than "
            "the signal being looked for. Videos making exactly this demonstration were "
            "circulating and being picked apart on Metabunk in March 2016, two years before "
            "the film. Item 19 &mdash; <em>&ldquo;Gyroscopes stable absent "
            "recalibration&rdquo;</em> &mdash; is therefore a true report about a class of "
            "instrument. It is incomplete rather than wrong: it is a fact about sensitivity, "
            "not a fact about the Earth.</p>"
            "<p><strong>KERNEL.</strong> The strongest form of this argument is not about "
            "gyroscopes failing. It is items 225 and 374 &mdash; <em>&ldquo;Ring laser gyro "
            "corrections&rdquo;</em>, <em>&ldquo;INS Earth updates&rdquo;</em> &mdash; and "
            "they are correct about deployed hardware. A strapdown inertial navigation "
            "system does not present the Earth's rotation to its user as a measurement. It "
            "<em>supplies</em> an Earth-rate term, computed from a stored latitude and a "
            "fixed constant, and subtracts it from the sensed body rates before the "
            "navigation solution is formed; the solution then accumulates integration drift "
            "and has its position periodically corrected by an external system, in practice "
            "GPS. Which means the popular debunk &mdash; <em>&ldquo;the inertial platform in "
            "your airliner proves the Earth spins&rdquo;</em> &mdash; is, on that framing, "
            "circular: the rotation was an input. The argument has found a real hole in a "
            "commonly offered proof. And the right way to close a hole like that is exactly "
            "what was done here: obtain the sensor, bypass the navigation solution, and read "
            "the raw sensed rate. That is a better experiment than most of this list "
            "contains, and better than the objection's usual critics propose.</p>"),
        why_it_doesnt_save_claim=(
            "<p>Because a correction is derivable only from a quantity that is measurable, "
            "and this particular correction wears its measurement on its face.</p>"
            "<p><strong>It has a latitude signature.</strong> The Earth-rate term applied to "
            "a directional gyro is not a constant fudge; it is 15 &times; sin(latitude) "
            "degrees per hour, sign flipping between hemispheres. Mechanical heading "
            "indicators carry a <em>latitude nut</em>, set on the ground, whose entire "
            "purpose is to induce an equal and opposite real wander in the rotor. A screw "
            "calibrated to a trigonometric function of where you are standing is not a "
            "patch applied to save a theory; it is a fit to a rotation vector with a "
            "direction in space. A stationary Earth supplies no reason for that term to "
            "exist, and no reason at all for it to vary as the sine of latitude.</p>"
            "<p><strong>The same physics finds north from scratch, with nothing fed in.</strong> "
            "A gyrotheodolite is given no heading, no almanac and no satellite: it senses the "
            "horizontal component of the Earth's rotation vector and precesses into the "
            "meridian, to within about ten arc seconds. It is standard equipment in mine "
            "surveying and tunnel engineering precisely where star sights and GPS do not "
            "reach, and it was used to align the Channel Tunnel bores. Its documented failure "
            "mode is the tell: it is not used within roughly 15&deg; of either pole, because "
            "there the angle between the Earth's rotation axis and the local vertical becomes "
            "too small for the horizontal component to be recovered. An instrument that "
            "extracts a direction out of nothing, and that fails exactly where the vector it "
            "is extracting goes flat, is not running on an assumption.</p>"
            "<p><strong>And in this cluster's own case the experiment was performed.</strong> "
            "The kernel says a deployed system presupposes the rotation rather than measuring "
            "it. The correct response is to strip the presupposition out and read the sensor "
            "directly. That was done, on camera, and the film's own record of the reading is "
            "the rate the rotating model predicts. The kernel is a genuine objection to a "
            "sloppy proof; it is not an objection to the Earth turning, and the one test it "
            "licenses has been run.</p>")),

    refutation=(
        "<p><strong>First, the concession, because it is the honest place to start.</strong> "
        "An inertial navigation system in an aircraft is not an independent demonstration of "
        "the Earth's rotation. Its mechanisation subtracts an Earth-rate term derived from a "
        "stored latitude before it forms a navigation solution; the solution suffers "
        "integration drift, because small errors in sensed acceleration and angular rate are "
        "integrated into progressively larger errors in velocity and position; and it is "
        "therefore periodically corrected from an external source, normally GPS. Anyone who "
        "answers this cluster by pointing at an airliner has argued in a circle, and items "
        "225 and 374 have caught them at it. This page does not make that argument.</p>"

        "<p><strong>Second, what a ring laser gyroscope measures.</strong> Not motion relative "
        "to the ground, not motion relative to a medium, and not motion relative to the "
        "instrument's own past: rotation with respect to the <em>local inertial frame</em>. "
        "Two beams counter-propagate around a closed cavity; rotating the cavity separates "
        "their frequencies by &Delta;<em>f</em> = 4<strong>A</strong>&middot;"
        "<strong>&Omega;</strong> / &lambda;<em>L</em>. There is no free rotor, so the "
        "bearing-friction objection that defeats a mechanical gyroscope &mdash; the true "
        "objection behind item 19 &mdash; has nothing to act on. The underlying effect is the "
        "Sagnac effect, and the fact that it contains no medium in its statement is worked "
        "through at <a href=\"#ARG-A02\">ARG-A02</a> rather than repeated here.</p>"

        "<p><strong>Third, the filmed reading, with its limits stated plainly.</strong> The "
        "figure spoken in <em>Behind the Curve</em> is 15 degrees per hour. In the sequences "
        "the press transcriptions cover it arrives with no make, no model, no input-axis "
        "orientation, no uncertainty, no duration and no repeat, and it is not evidence this "
        "page leans on. "
        "Note in particular that the axis geometry is unresolved: a three-axis unit reports "
        "the magnitude of the rotation vector, the full 15.041&deg; per hour at any latitude, "
        "whereas a single-axis unit with its input axis vertical reads only "
        "&Omega;&nbsp;sin&nbsp;&phi;. Nothing in this treatment depends on which it was. "
        "<strong>The reading is evidence about the argument, not about the Earth.</strong> "
        "The Earth's rotation is established by the instruments in the next paragraph.</p>"

        "<p><strong>Fourth, where the evidence actually is.</strong> L&eacute;on Foucault "
        "built the first gyroscope in 1852 as a follow-up to his pendulum, for the express "
        "purpose of demonstrating the Earth's rotation, and coined the word for it &mdash; "
        "<em>gyros</em> and <em>skopein</em>, to view the rotation. Michelson, Gale and "
        "Pearson closed a light path around a rectangle at Clearing, Illinois in 1925, "
        "predicted a fringe displacement of 0.236 &plusmn; 0.002 for a rotating Earth and "
        "measured 0.230 &plusmn; 0.005 (<a href=\"#ARG-A02\">ARG-A02</a>). A 1 m &times; 1 m "
        "ring laser in Christchurch resolved the Earth's rotation in 1992, and because "
        "sensitivity grows as the square of the ring size, the 4 m &times; 4 m G ring laser "
        "at the Geodetic Observatory Wettzell does far better: at latitude 49.145&deg; with a "
        "632.8 nm helium&ndash;neon laser, the formula above returns a Sagnac beat of about "
        "348 Hz for the Earth's rotation alone &mdash; that figure is our arithmetic from the "
        "published expression and the instrument's stated geometry, not a quoted measurement. "
        "Di Virgilio and colleagues report that G's Allan deviation drops below one part in "
        "10<sup>9</sup> of the Earth's angular rate after about 10<sup>4</sup> s of "
        "integration. Nine digits. That instrument tracks length-of-day variation and polar "
        "motion, and agrees with VLBI determinations of the same wobbles made by an entirely "
        "different technique.</p>"

        "<p><strong>Fifth &mdash; and this is the crux &mdash; the reading was tested against "
        "the wrong hypothesis.</strong> &ldquo;Drift&rdquo; is the correct term of art: in "
        "gyro engineering it names the instrument's own bias. So the first objection to a "
        "15&deg;-per-hour reading is the right one, and it is <em>this is my bias, not the "
        "Earth</em>. What separates the two is geometry, and it is free. A bias is fixed in "
        "the instrument's body frame; the Earth's rotation is fixed in inertial space, along "
        "the celestial pole. Three consequences follow, and each is a test that costs "
        "nothing.</p>"
        "<p>(a) <em>Reverse the azimuth.</em> Turn the unit 180&deg; about the local vertical "
        "and re-run. The sensed Earth-rate component reverses sign; the bias does not. This "
        "two-position comparison is standard practice, and it separates the two terms "
        "outright.</p>"
        "<p>(b) <em>Tilt the input axis.</em> With the axis vertical the sensed component is "
        "&Omega;&nbsp;sin&nbsp;&phi;; swing it to horizontal-east and the component goes to "
        "zero, because the input axis is then perpendicular to the Earth's rotation vector. A "
        "bias is indifferent to which way the box is pointed.</p>"
        "<p>(c) <em>Change latitude.</em> Carry the same unit north or south and the "
        "vertical-axis reading scales as sin&nbsp;&phi;. A bias travels unchanged.</p>"
        "<p><strong>Magnetic shielding is not on that list, and could not have been.</strong> "
        "The Sagnac output depends on the enclosed area, the wavelength and the rotation rate; "
        "an external field is not a term in it. But the shielding run deserves credit rather "
        "than ridicule, because it was a control and it did its job: it tested a specific "
        "hypothesis &mdash; an outside influence coupling into the apparatus &mdash; and, on "
        "the secondary account we have, returned the same number, which excluded exactly what "
        "it was built to exclude. That is a result. Hunting systematics after an unwelcome "
        "reading is what every laboratory does and it is not a criticism.</p>"

        "<p><strong>Sixth, the four remaining items, answered from the hardware.</strong></p>"
        "<p><em>Item 19, &ldquo;Gyroscopes stable absent recalibration.&rdquo;</em> The "
        "opposite is in every pilot's training material. A mechanical heading indicator wanders "
        "at an Earth-rate of 15 &times; sin(latitude) degrees per hour, is trimmed on the "
        "ground with a latitude nut, and is manually realigned against the magnetic compass "
        "every ten to fifteen minutes in routine in-flight checks; neglecting it is a "
        "recognised source of navigation error. An attitude indicator carries an erection "
        "mechanism that continuously applies force to return the gyro to the vertical, because "
        "the local vertical is not a fixed direction in space. Aircraft gyroscopes are not "
        "stable absent recalibration; recalibrating them is a checklist item.</p>"
        "<p><em>Item 225, &ldquo;Ring laser gyro corrections.&rdquo;</em> True, and the "
        "correction is the Earth's rotation. Its magnitude is not a free parameter chosen to "
        "make the numbers work: it is fixed by a rate measured independently, to nine digits, "
        "by the large ring lasers above, and its dependence on latitude is a signature no "
        "stationary model supplies a reason for.</p>"
        "<p><em>Item 374, &ldquo;INS Earth updates.&rdquo;</em> Conceded in the first "
        "paragraph, and it does not reach the claim. Position is externally updated; heading "
        "is not. An inertial platform obtains true north during alignment by sensing the "
        "horizontal component of the Earth's rotation vector, which is the same operation a "
        "gyrotheodolite performs underground with no satellite and no star in view.</p>"
        "<p><em>Item 112, &ldquo;Non-rotation gyroscope studies.&rdquo;</em> This names a "
        "genre rather than a result, and no study answering to the description was located in "
        "the searches run for this entry, which are the ones listed in the sources below. The "
        "nearest artefact located is a video of a mechanical-gyroscope demonstration in "
        "circulation by March 2016; the failure mode of that demonstration is set out in the "
        "steelman above and it is a real one.</p>"

        "<p><strong>Seventh, what the verdict claims, and what it withholds.</strong> "
        "<em>Self-contradicted</em> here is a claim about an argument, not about a person. It "
        "means this: the argument nominates a test, the test is the correct one, it was "
        "designed and run by the person our records name as the argument's originator, and "
        "the instrument returned the value the argument requires to be zero. No inference is "
        "drawn from that about anyone's sincerity, competence or state of mind &mdash; and "
        "the competence point runs the other way, since buying a navigation-grade instrument "
        "and running the measurement is more than the argument's distributors did, and more "
        "than most items on this list have behind them.</p>"

        "<p><strong>Eighth, the one thing the design was missing, stated as a method "
        "problem.</strong> The apparatus was right, the quantity was right, the prediction "
        "was unambiguous and the follow-up control was reasonable. What is missing from the "
        "sequences the press transcriptions cover is an acceptance criterion &mdash; a "
        "statement, made before the run, of which reading would count as confirmation and "
        "which as refutation. We have not viewed the full film and cannot say whether one was "
        "given elsewhere in it. Without one, no reading can be decisive in either direction, "
        "and the experiment's own result has nowhere to go. That is the whole of the finding: "
        "the instrument reported, the protocol had no place to put it. The repair is cheap and "
        "is written above &mdash; reverse the azimuth, tilt the input axis, move the box a few "
        "degrees of latitude, and say in advance what each outcome will mean.</p>"),

    compression=dict(
        assessed=True, drifted=True,
        list_phrasing="Gyroscope anomalies indicating no rotation.",
        source_wording=("&ldquo;when we turned on that gyroscope we found that we were "
                        "picking up a drift. <em>A 15 degree per hour drift.</em>&rdquo;"),
        drift_type="reversed",
        note=(
            "<p>This is the flattest reversal on the board, and it is worth being precise "
            "about what is being compared. The item asserts a gyroscope anomaly indicating "
            "<em>no</em> rotation. The only source text available to hold it against is the "
            "filmed statement of the person our records name as the argument's originator, "
            "and that statement reports a gyroscope indicating rotation, at the rate the "
            "rotating model predicts. Same instrument, same experiment, opposite sign.</p>"
            "<p><strong>The reversal is carried by item 12 alone, and the cluster is named "
            "after it.</strong> That matters, because the other four do not all drift the "
            "same way and it would be dishonest to score them as though they did. Item 19 is "
            "a faithful compression of a true claim about cheap mechanical gyroscopes, whose "
            "bearing friction really does swamp a 15&deg;-per-hour signal. Items 225 and 374 "
            "are faithful compressions of a correct engineering objection about how deployed "
            "inertial systems obtain their Earth-rate term, and they are the ones the "
            "refutation above spends most of its length on, for exactly the reason the hedge "
            "rule exists: they are the version worth beating. Item 112 names a genre rather "
            "than stating a result, so there is nothing in it to be faithful or unfaithful "
            "to.</p>"
            "<p><strong>The gap is the finding, and it runs the usual direction.</strong> A "
            "cluster whose best items are a careful objection to a circular proof arrives on "
            "the list under a headline asserting a result nobody in its own lineage is on "
            "record obtaining. What circulates is item 12. What was actually said is the "
            "quotation above.</p>")),

    verdict_challenge=dict(challenged=False, proposed_verdict=None, reasoning=None),

    straw_man=dict(
        identified=True,
        detail=("Items 225 and 374 aim at a claim careful people should not be making. "
                "“The inertial platform in your airliner proves the Earth spins” is "
                "circular, because a deployed system has an Earth-rate term supplied to it "
                "from a stored latitude and has its position reset from GPS. That is a fair "
                "hit on a common popular debunk, and this page does not run it. The straw man "
                "to watch on our own side is the reflex that they do not understand "
                "gyroscopes: the argument named the correct instrument, the correct quantity "
                "and a prediction of zero, and someone went and bought one."),

    ),

    advocate=dict(
        best_defense=(
            "You have built a verdict, and the loudest verdict on your whole board, out of "
            "about ten seconds of somebody else's film. Look at what you are treating as "
            "decisive: no data set, no calibration record, no stated input-axis orientation, "
            "no error bars, no duration, no repeat, no published protocol, and a transcript "
            "you admit you took from press write-ups rather than from the film. You would not "
            "accept that standard from us for one second — you rejected an entire cluster of "
            "our item titles because you could only find them in one OCR'd scan. A man said a "
            "number on camera and you have promoted it to an experimental result because it is "
            "the number you wanted. "
            "Second, you have the epistemics exactly backwards. An experimenter who gets an "
            "anomalous reading and immediately starts hunting for systematic error is doing "
            "what every laboratory on Earth does, and you have written it up as refusing to "
            "accept data. A magnetic enclosure is a control. If a physicist had run it you "
            "would have called it due diligence. "
            "Third, and this is the one you cannot get around: items 225 and 374 stand "
            "untouched by the film. You concede in your own first paragraph that deployed "
            "inertial systems have the rotation fed into them and are reset from GPS. So the "
            "artefacts that surround every one of us daily are not evidence, by your own "
            "admission — and what is left is a handful of specialist installations at Wettzell "
            "and Christchurch whose raw output nobody outside those collaborations has ever "
            "seen, reduced through models that assume the answer. You have replaced a circular "
            "proof with an appeal to instruments that are, to a reader, a photograph and a "
            "citation. "
            "Fourth, your scoring is asymmetric and you should say so out loud. One "
            "uncontrolled reading in our favour would be dismissed by you in a line; one "
            "uncontrolled reading against us is a headline verdict called SELF-CONTRADICTED."),
        survives=4,
        preemptive=(
            "Rated 4: nothing in it is a physics error, the third strand is correct, and left "
            "unanswered it takes the entry apart. Four concrete things were written into the "
            "published text to meet it, and a reviewer should check they are still there. "
            "(1) The separation is made explicit and early rather than left implicit: the "
            "third paragraph of the refutation states in bold that the filmed reading is "
            "evidence about the ARGUMENT and not about the Earth, and lists what the film does "
            "not supply — make, model, axis, uncertainty, duration, repeat — before the "
            "advocate can. The passage locator concedes the transcription route and the absence "
            "of a timecoded viewing in its own first sentence. This removes the 'ten seconds of "
            "film' hit entirely, because we are not standing on it. "
            "(2) The evidence for the Earth's rotation is relocated into its own paragraph "
            "(Foucault 1852, Michelson–Gale 1925 with the 0.236 vs 0.230 fringes, Christchurch "
            "1992, Wettzell G, Di Virgilio's one part in 10^9) so the verdict does not rest on "
            "Knodel at all. Against 'nobody has seen the raw output', note that the paragraph "
            "cites the cross-check the advocate omits: G agrees with VLBI on polar motion and "
            "length of day, and VLBI is a different technique run by different people. "
            "(3) The systematics point is conceded in the source's favour, in bold — the "
            "shielding run 'deserves credit rather than ridicule', 'was a control and it did "
            "its job', 'that is a result'. The finding is then relocated to where it survives: "
            "not the checking, but the missing acceptance criterion, plus the observation that "
            "the three tests which would actually separate bias from rotation (azimuth "
            "reversal, axis tilt, latitude transport) are geometric and free, and shielding is "
            "not among them. That is a methodological finding, and it cannot be answered by "
            "'checking is normal'. "
            "(4) Items 225 and 374 are answered without the film, in the steelman's second "
            "half and again in section six: the latitude nut (15 x sin(latitude) degrees per "
            "hour, set on the ground) and the gyrotheodolite (finds true north from nothing, "
            "used for the Channel Tunnel, unusable within ~15 degrees of the poles). Both are "
            "cheap, both are checkable by a reader without trusting a collaboration, and both "
            "have a latitude dependence no stationary model supplies a reason for. "
            "On the asymmetry charge: it is answered by the seventh section defining "
            "SELF-CONTRADICTED as a claim about an argument's internal structure rather than "
            "about a measurement's quality — the verdict does not require the filmed reading "
            "to be good data, only to be the argument's own nominated test returning the "
            "argument's own excluded value. If a reviewer thinks that definition is doing too "
            "much work, that is the place to press, not the physics.")),

    people=["PER-KNODEL"],
    related=["A02", "A06", "A08", "A19", "A26", "R01"],

    sources=[
        dict(label="Newsweek, “Flat Earthers Disprove Themselves in Behind the Curve”, "
                   "15 February 2019 — transcription of the gyroscope quote and the "
                   "closing light-through-holes experiment",
             url="https://www.newsweek.com/behind-curve-netflix-ending-light-experiment-"
                 "mark-sargent-documentary-movie-1343362"),
        dict(label="JOE.co.uk on Behind the Curve — a second transcription of the same "
                   "sequence, differing in small ways from Newsweek's",
             url="https://www.joe.co.uk/news/flat-earther-accidentally-proves-earth-is-"
                 "round-after-spending-20k-on-experiment-3-456989"),
        dict(label="Wikipedia — Behind the Curve: dir. Daniel J. Clark, Delta-v Productions; "
                   "Hot Docs premiere 30 April 2018, US release 15 November 2018, Netflix "
                   "February 2019",
             url="https://en.wikipedia.org/wiki/Behind_the_Curve"),
        dict(label="Jay L. Wile, “A Really Good Flat Earth Documentary” (2019) — secondary "
                   "account of the magnetic enclosure, the dome-of-stars hypothesis and the "
                   "proposed bismuth chamber",
             url="https://blog.drwile.com/a-really-good-flat-earth-documentary/"),
        dict(label="Wikipedia — Foucault's gyroscope: built 1852 to demonstrate the Earth's "
                   "rotation; Foucault coined the name, “to view the rotation”",
             url="https://en.wikipedia.org/wiki/Foucault%27s_gyroscope"),
        dict(label="Wikipedia — Ring laser: the Sagnac beat frequency 4AΩ/λL, the 1 m × 1 m "
                   "Christchurch ring of 1992, the 4 m × 4 m Wettzell ring, and sensitivity "
                   "growing as the square of ring size",
             url="https://en.wikipedia.org/wiki/Ring_laser"),
        dict(label="Wikipedia — Ring laser gyroscope: no moving parts beyond the dither "
                   "assembly; navigation-grade bias uncertainty better than 0.01°/hour",
             url="https://en.wikipedia.org/wiki/Ring_laser_gyroscope"),
        dict(label="Di Virgilio et al., “Overcoming 1 part in 10⁹ of Earth angular rotation "
                   "rate measurement with the G Wettzell data”, EPJ C 82:824 (2022) — Allan "
                   "deviation below 1 part in 10⁹ after ~10⁴ s",
             url="https://ar5iv.labs.arxiv.org/html/2208.09134"),
        dict(label="Wikipedia — Heading indicator: Earth-rate apparent drift of "
                   "15·sin(latitude) °/hr, the ground-set latitude nut, and realignment "
                   "against the magnetic compass every ten to fifteen minutes",
             url="https://en.wikipedia.org/wiki/Heading_indicator"),
        dict(label="CFI Notebook — Attitude Indicator: the erection mechanism that "
                   "continuously returns the gyro to the local vertical",
             url="https://www.cfinotebook.net/notebook/avionics-and-instruments/"
                 "attitude-indicator"),
        dict(label="Wikipedia — Gyrotheodolite: finds true north by sensing the Earth's "
                   "rotation, ~10 arc seconds, used for the Channel Tunnel, not used within "
                   "about 15° of the poles",
             url="https://en.wikipedia.org/wiki/Gyrotheodolite"),
        dict(label="Metabunk, “Debunked: Gyro Experiment — Proves Motionless Earth?”, thread "
                   "opened 20 March 2016 — the mechanical-gyroscope version of the argument "
                   "in circulation two years before the film",
             url="https://www.metabunk.org/threads/debunked-gyro-experiment-proves-"
                 "motionless-earth.7413/"),
        dict(label="Wikipedia — Inertial navigation system: integration drift and periodic "
                   "correction from an external navigation system",
             url="https://en.wikipedia.org/wiki/Inertial_navigation_system"),
    ]),
}
