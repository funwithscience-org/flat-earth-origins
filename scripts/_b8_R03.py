# -*- coding: utf-8 -*-
"""Batch 8 — R03. "No experiment detects absolute motion; only relative motion is observable."

Research notes for whoever picks this up next.

1. THE WORK RECORD. clusters.py credits R03 to van der Kamp's "The Heart of the Matter"
   (1968). That booklet is real — Bouw's obituary records a rough draft privately
   circulated in 1967, printed January 1968, and says it "went nowhere fast" — but no
   copy of it was reachable from here, and nothing in this entry rests on it. Every
   quotation below is from De Labore Solis (1988), which is the published book and the
   one downstream writers cite. clusters.py was NOT touched; reported up. Two things
   worth the parent's attention there: the originator_work/year pair, and `real_source`,
   which is null although the proposition is Poincaré's 1904 principle of relativity
   almost verbatim — van der Kamp quotes it at p. 45 of the scan.

2. THE SOURCE IS NOT ASSERTING THE LIST'S PROPOSITION; HE IS DISMANTLING IT. The
   paragraph quoted in `passage` (p. 62 of the scan) names Bertrand Russell and Fred
   Hoyle as the people who hold the equivalence and says their claims "are only tenable
   if certain presuppositions are assumed to be self-evident. Which they are not!" His
   own use of relativity is under an explicit antecedent — "If Einstein is right ..."
   (p. 67, worked at R01) — and his book opens by demanding a control experiment on a
   fast platform (pp. 6–7) with a warning against generalising null results ("if in the
   Sahara no icefields can be found, this observation does not thereby prove that
   icefields exist nowhere", p. 6). So the drift here is hedge_dropped and it is a
   different drift from R01's force_upgraded on the same book: R01 catches a concession
   promoted to a proof, R03 catches a conditional, other-attributed proposition restated
   flat and in the source's own name.

3. THE PHYSICS HINGE IS ONE WORD IN POINCARÉ'S SENTENCE: "translation". The principle
   is scoped to uniform motion of translation and rotation was never inside it. That is
   what separates R03 from R01: R01 is about covariance and coordinates, R03 is about
   the scope of a symmetry. Keep them apart or the two entries collapse into one.

4. QUOTE PROVENANCE. The p. 62 paragraph was retrieved twice, on differently worded
   passes over the same PDF, and came back with the same sentence order and the same
   "Russel's" misspelling. It has not been checked against a print copy; the locator
   says so. Do not upgrade that locator without page images.
"""

ENTRY = {

"R03": dict(

    tldr=("This one is true, and it is the strongest thing the geocentric case has: no "
          "experiment detects motion through absolute space, and the most precise versions "
          "run so far agree. But Poincaré wrote the limit into his own sentence — the principle "
          "covers uniform motion of translation, and rotation was never inside it, which is "
          "why a ring laser bolted to the ground reads the Earth's spin without looking at the "
          "sky. And van der Kamp did not hold the flat version the list credits him with: his "
          "book demands a decisive experiment rather than declaring the question closed."),

    passage=dict(
        work="WRK-VDK-1988",
        pd=False,
        locator=("p. 62 of the PDF scan at geocentricity.com, in the discussion of Russell and "
                 "Hoyle; retrieved twice on separately worded passes over the same scan, not "
                 "checked against a print copy"),
        quote=("Bertrand Russel's contention that the observable phenomena will be the same "
               "whether the Earth rotates or the Heavens revolve, as well as Fred Hoyle's "
               "declaration that the geocentric view is as good as anybody else's, but not "
               "better, they are only tenable if certain presuppositions are assumed to be "
               "self-evident. Which they are not!"),
        gloss="""<p><strong>Read who is speaking.</strong> The proposition the list credits to van der Kamp is, in his own book, <em>other people&rsquo;s</em> &mdash; Russell&rsquo;s and Hoyle&rsquo;s &mdash; and he names them in order to say their claims will not stand on their own. (&ldquo;Russel&rsquo;s&rdquo; is the spelling in the scan.) He quotes Russell earlier, at pp. 12&ndash;13, in the famous form: whether the Earth rotates west to east or the heavens revolve east to west, <em>&ldquo;the observable phenomena will be exactly the same&rdquo;</em>, which Russell calls a defect in Newtonian dynamics because &ldquo;an empirical science ought not to contain a metaphysical assumption, which can never be proved or disproved by observation.&rdquo; Russell is a hostile witness and that is exactly why van der Kamp wants him. But wanting a hostile witness is not the same as owning his conclusion, and by p. 62 van der Kamp is refusing to own it.</p>
<p><strong>What he wanted instead.</strong> The book opens with a demand for a test, not a stalemate. He asks for &ldquo;at least one control experiment&rdquo; (p. 6), sets it out as a <em>modus tollens</em> &mdash; if the speed of light measured from a fast-moving platform comes out at the earthly <em>c</em>, &ldquo;he stands vindicated&rdquo;, and if it changes with the platform&rsquo;s speed, &ldquo;then he will be discredited&rdquo; (p. 7) &mdash; and warns against reading too much into any null: &ldquo;if in the Sahara no icefields can be found, this observation does not thereby prove that icefields exist nowhere&rdquo; (p. 6). His relativistic argument runs under an antecedent he rejects, <em>&ldquo;If Einstein is right &hellip;&rdquo;</em>, and that sentence and its cost are worked in full at <a href="#ARG-R01">ARG-R01</a>.</p>
<p><strong>On the work cited.</strong> Our cluster record for R03 credits van der Kamp&rsquo;s earlier booklet <em>The Heart of the Matter</em> (1968). No copy of that booklet was reachable from here, so this treatment quotes and cites only <em>De Labore Solis</em> (1988) &mdash; the published book, and the text later geocentrist writers work from. What is documented about the 1968 item is Bouw&rsquo;s obituary account: a rough draft privately circulated in 1967, printed in January 1968, which in Bouw&rsquo;s words &ldquo;went nowhere fast.&rdquo;</p>"""),

    steelman=dict(
        description="""<p><strong>SURFACE (weak &mdash; do not use).</strong> &ldquo;Of course absolute motion is detectable &mdash; look at a Foucault pendulum.&rdquo; This loses the exchange in one move, because a pendulum detects <em>rotation</em>, not velocity through space, and anyone who conflates the two has conceded that they do not know what the relativity principle says. Equally weak: &ldquo;Michelson&ndash;Morley was a failed experiment.&rdquo; It was a successful one, and its result is the claim under discussion.</p>
<p><strong>DEEPER.</strong> The proposition is simply true, and it is not a hedge or a shrug. No experiment has detected uniform motion relative to a substrate, and the modern versions are brutal about it: rotating optical cavities bound a direction-dependence of the speed of light at the 10<sup>&minus;17</sup> level (Herrmann et al., <em>Phys. Rev. D</em> 80:105011, 2009) and at 10<sup>&minus;18</sup> (Nagel et al., <em>Nature Communications</em> 6:8174, 2015). A defender of the list who says only this has said something correct that no physicist will dispute.</p>
<p><strong>KERNEL.</strong> The strongest form is not the list&rsquo;s and it is not a physics claim at all. It is van der Kamp&rsquo;s, and it is a claim about what a null result is worth. He accepted that the observations tie; he refused to accept that a tie in the observations settles what is the case; and he asked for the experiment that would break the tie rather than treating the tie as a resting place. His Sahara line is a compact statement of a real point in philosophy of science &mdash; the underdetermination of theory by evidence &mdash; and his framing of the test as a <em>modus tollens</em> rather than a confirmation is Popper&rsquo;s point, correctly applied. Add Russell as the hostile witness: an empirical science ought not to carry an assumption that observation can neither prove nor disprove. That is a serious complaint, seriously made, by people with no interest in geocentrism. Concede all of it.</p>""",
        why_it_doesnt_save_claim="""<p>Because Russell&rsquo;s complaint was answered, and the answer was to <strong>delete absolute space</strong>, not to put the Earth in the middle of it. The metaphysical assumption Russell objected to in Newtonian dynamics is the one relativity removed: after 1905 there is no quantity &ldquo;the Earth&rsquo;s absolute velocity&rdquo; that is hidden from us, because there is no such quantity to have a value. That is why the principle cannot be turned into a positive result for anybody. &ldquo;The Earth is at absolute rest&rdquo; is not an unproven-but-live possibility on this theory; it is a sentence with nothing to be true of, and it is exactly as available to Jupiter.</p>
<p>And the principle is <em>scoped</em>, in the wording of the man who named it. Poincaré&rsquo;s 1904 St Louis lecture states it as the laws being the same for a stationary observer and for one &ldquo;carried along in a <strong>uniform motion of translation</strong>, so that we have no means, and can have none, of determining whether or not we are being carried along in such a motion.&rdquo; <em>Such a</em> motion. Rotation is not a uniform translation, acceleration is not a uniform translation, and neither was ever inside the shield. The one claim geocentrism has to make about the Earth &mdash; that it does not turn &mdash; falls in the part of kinematics the principle leaves exposed.</p>
<p>Finally, van der Kamp&rsquo;s own standard convicts the list rather than the critics. He said a null result does not license a universal negative. The list&rsquo;s items 29, 88 and 317 are universal negatives built from null results.</p>"""),

    refutation="""<p><strong>First, the concession, and it is total.</strong> There is no experiment that reveals motion relative to absolute space, and the attempts to find one are among the most refined measurements physics has. Michelson and Morley set the pattern in 1887; Kennedy and Thorndike added the velocity-dependent version in 1932; the modern descendants use rotating cryogenic optical cavities and bound a direction-dependence of the speed of light at the 10<sup>&minus;17</sup> level (Herrmann et al. 2009) and a Lorentz-violating anisotropy at 10<sup>&minus;18</sup> (Nagel et al. 2015). Nothing has turned up. This is not an embarrassment being managed &mdash; it is among the most stringently confirmed symmetries in physics, and it is the reason the theory has the shape it has. Anyone answering this argument by claiming that absolute motion has been measured is wrong, and will deserve to lose the exchange.</p>

<p><strong>Second, the word the principle turns on.</strong> Poincaré, naming it in 1904: the laws are the same for a stationary observer as for one &ldquo;carried along in a uniform motion of <em>translation</em>, so that we have no means, and can have none, of determining whether or not we are being carried along in such a motion.&rdquo; Einstein&rsquo;s 1905 postulate is scoped the same way, to frames in which the equations of mechanics hold &mdash; inertial frames. A rotating frame is not one. This is not a loophole discovered by critics; it is the load-bearing distinction of the whole subject, the one Newton built the bucket to illustrate, and it is why the theory that abolished absolute velocity left absolute <em>rotation</em> standing as a local, coordinate-free fact about a body.</p>

<p>So the quantity to look at is the Earth&rsquo;s rotation relative to the local compass of inertia &mdash; what gyroscopes point at &mdash; and it is measurable in a closed room with the blinds down. Foucault did it in 1851 with a wire. Michelson, Gale and Pearson did it optically in 1925, predicting a 0.236 fringe shift and measuring 0.230 &plusmn; 0.005 (that experiment is <a href="#ARG-A02">ARG-A02</a>, where the list cites it backwards). The G ring laser at Wettzell now resolves the Earth&rsquo;s rate to better than one part in 10<sup>9</sup>, tracking the Chandler wobble and solid-Earth tides as they move it. Every one of these instruments answers the question without reference to the sky. The relativity principle has nothing to say about them, by its own terms.</p>

<p><strong>Be fair about the one reply that engages.</strong> A defender can say that the compass of inertia is itself set by the matter of the universe, so a cosmos turning once a day would drag the gyroscopes with it and the ring laser would read 15.04&deg;/h either way. That is Mach&rsquo;s principle, it is a real research question, Thirring proved a version of it for a rotating shell in 1918, and it converts R03 from a claim about what experiments can decide into a claim about dynamics &mdash; a stress-energy tensor, a solution, a fit. The dynamical version is argued in full at <a href="#ARG-R01">ARG-R01</a> and is not re-run here. The point that belongs to R03 is narrower and harder: <strong>the moment the defence becomes dynamical it is outside the relativity principle&rsquo;s protection.</strong> A theory that says the sky physically drags the local inertial frame is a theory with consequences, and consequences are the thing R03 was invoked to say we could never have.</p>

<p><strong>Third, the revolution, which is the one item here that makes a checkable claim.</strong> Item 88 says there is no proof of revolution. The Earth&rsquo;s orbital motion is not merely detected; it is used as a working instrument. Every precision Doppler spectrum taken anywhere in the world has the observer&rsquo;s velocity about the Solar-System barycentre subtracted before the data are used, and the standard for that correction is accurate to 1 cm/s (Wright &amp; Eastman, <em>PASP</em> 126:838, 2014). If the Earth held still, that subtraction would be a fiction, and the fiction would have to be the reason exoplanet signals stay coherent across years of observation. In the microwave background the same 30 km/s shows up as the <em>orbital dipole</em>, and Planck used it as the absolute photometric calibrator for its channels from 30 to 353 GHz. The Earth&rsquo;s revolution is a metrological standard. The classical versions of this point &mdash; aberration and stellar parallax &mdash; are at <a href="#ARG-A03">ARG-A03</a> and <a href="#ARG-A05">ARG-A05</a>.</p>

<p>State plainly what these are and are not. They are measurements of motion <em>relative to matter</em>: relative to the Solar-System barycentre, relative to the frame in which the microwave background looks isotropic. None of them is a detection of absolute motion, and nothing here claims otherwise. That is the whole point. Relative motion is the observable kind &mdash; the list says so itself, in item 276 &mdash; and the Earth&rsquo;s relative motion is observed, tabulated and used.</p>

<p><strong>Fourth, the shield excludes the thing it was raised to protect.</strong> The geocentric thesis is not &ldquo;the Earth is at absolute rest.&rdquo; It is that the Sun, planets and stars physically circle the Earth once a sidereal day. That is a claim about the <em>relative</em> motion of matter, which is the category the principle declares observable. What is actually observed is a relative rotation of Earth and sky at about 15.04&deg;/h, on which both models agree and which therefore discriminates between nothing; and a rotation of the Earth relative to local gyroscopes, on which they disagree, and which has been measured to nine digits. A principle whose content is &ldquo;only relative motion is observable&rdquo; cannot be used to protect a claim about relative motion from observation.</p>

<p><strong>Fifth, the symmetry, which is the cluster&rsquo;s basis and worth stating without decoration.</strong> If no experiment can establish that the Earth moves absolutely, none can establish that it is absolutely at rest. The principle is not evidence for one of the two options; it dissolves the question both options were answers to. Item 131 (&ldquo;No absolute frame&rdquo;) is true and equally forbids a geocentric absolute frame. Item 317 (&ldquo;No global inertial frame proven&rdquo;) is true in a stronger way than the list appears to intend: in a curved spacetime inertial frames are local, there is no global one, and so there is no global &ldquo;at rest&rdquo; for a body to occupy. That item is a true statement whose truth erases the sentence it is being marshalled to support. R01 records the movement&rsquo;s own retreat from this position &mdash; Sungenis and Bennett naming the Earth-Centred Inertial frame as &ldquo;one universal absolute preferred frame in which <em>c</em> is isotropic&rdquo;, which is a preferred-frame theory and the negation of R03 rather than an extension of it.</p>

<p><strong>Sixth, the cost across the rest of the list.</strong> R03 is the deepest thing in the collection and it is also the most expensive, because it is a universal solvent. If experiments cannot discriminate between the frames, then Michelson&ndash;Gale is not evidence, &ldquo;Airy&rsquo;s failure&rdquo; is not evidence, Miller&rsquo;s drift is not evidence and the microwave alignments are not evidence &mdash; and each of those is asserted elsewhere on the same list as an experiment that came out the geocentrist&rsquo;s way. Bouw, the movement&rsquo;s only credentialed astronomer, took the consistent route and referred the decision to Scripture (<a href="#ARG-R11">ARG-R11</a>). The list takes neither route: it runs R03 and the experimental items side by side and asks the reader to accept both.</p>

<p><strong>Seventh, the test he asked for.</strong> Van der Kamp wanted the speed of light measured from a fast platform &mdash; &ldquo;e.g. a Concorde or Space shuttle&rdquo; &mdash; before he would grant relativity viability. That class of experiment has a name he did not use for it: it is the Kennedy&ndash;Thorndike experiment, which tests whether the speed of light depends on the velocity of the apparatus, and its modern versions get the varying platform velocity for free from the Earth&rsquo;s own rotation and orbit rather than from an aircraft. Those versions are the same cryogenic-cavity experiments quoted above. Clocks on fast platforms had already been flown in 1971, when Hafele and Keating carried caesium standards east and west around the world and found the gains and losses in agreement with the relativistic predictions to within the roughly 10% precision of the experiment &mdash; seventeen years before <em>De Labore Solis</em> went to press. His demand was reasonable when he framed it and had in substance been met by the time he published it.</p>

<p><strong>Verdict: standard physics.</strong> The proposition is correct, it is taught, and it belongs to relativity rather than to geocentrism. It says that one particular quantity &mdash; velocity through a substrate &mdash; is not a physical quantity at all. It carries no implication that the Earth&rsquo;s motion is unknowable, because rotation and acceleration were never covered by it; it does not favour the Earth, because it favours nothing; and it cannot be spent, because spending it retires most of the list that carries it.</p>""",

    advocate=dict(
        best_defense=(
            "You conceded the principle and then walked rotation in through the back door. "
            "“Rotation relative to the local inertial structure” is only a discriminator if "
            "the local inertial structure is fixed independently of the matter of the "
            "universe — and Mach, whom Einstein credited by name, says it is not. On a "
            "cosmos that turns, the compass of inertia turns with it, your ring laser reads "
            "15.04°/h exactly as observed, and your “coordinate-free invariant” is a "
            "definition wearing the costume of a measurement. Second: every number you "
            "produced — the barycentric correction, the orbital dipole, Michelson–Gale — "
            "measures motion relative to matter, and you say so yourself. We have never "
            "denied relative motion. You have confirmed our thesis and called it a "
            "refutation. Third, and worst for you: you have found that van der Kamp wanted a "
            "control experiment and you present this as though it embarrasses him. It "
            "vindicates him. He said the question was open and asked for the test that would "
            "close it. Your answer is that the test was done by other means, in other "
            "decades, by people who already assumed the answer. That is not a control "
            "experiment; that is a research programme measuring its own premises. And note "
            "what your own seventh section concedes: you had to reach for Kennedy–Thorndike "
            "and Hafele–Keating to answer a man who asked, politely, in print, for one clean "
            "experiment. He would have taken it."),
        survives=4,
        preemptive=(
            "Four is right and the number is driven by the third move, not the first. Three "
            "concrete changes, in order of urgency. (a) The 'you measure only relative "
            "motion' hit must be disarmed BEFORE it lands, not after: the paragraph "
            "beginning 'State plainly what these are and are not' does that work and must "
            "stay adjacent to the barycentric/Planck paragraph — if an editor ever splits "
            "them, the strongest paragraph on the page becomes the most vulnerable one. "
            "(b) The Machian reply currently ends in a cross-link to R01. A bare cross-link "
            "reads as evasion at exactly the point the defender is strongest. Add one "
            "sentence naming R01's actual answer rather than pointing at it — that Thirring's "
            "1918 result is a linearised interior solution for a slowly rotating shell in an "
            "asymptotically flat spacetime, and that nobody has scaled it into a "
            "self-consistent cosmological solution with a stress-energy tensor and a fit to "
            "the data. (c) On the control experiment, resist the temptation to say the "
            "one-way speed of light has been measured isotropic; it has not and cannot be, "
            "because one-way simultaneity is conventional, and a defender who knows this will "
            "use an overclaim to discredit the section. The seventh section as written stays "
            "on two-way and velocity-dependence tests, which is the defensible ground; keep "
            "it there. Finally, on tone: 'he would have taken it' is the defender's best "
            "line and it is fair. The answer is not that van der Kamp was foolish to ask but "
            "that the movement stopped asking — the list publishes as a settled proof the "
            "proposition he wanted put to trial."),
    ),

    straw_man=dict(
        identified=True,
        detail=("The argument is aimed at a position modern physics gave up in 1905. Nobody in "
                "the field holds that the Earth is in absolute motion, or that any experiment "
                "shows it; the claims actually made are that the Earth rotates relative to the "
                "local inertial structure and revolves about the Solar-System barycentre, both "
                "of which are relative and both of which are measured. Demanding proof of "
                "absolute motion, and reporting the failure to supply it, is a demand made of "
                "Newton rather than of anyone now living. Russell, whom van der Kamp quotes for "
                "the complaint, was making it against Newtonian dynamics for exactly that "
                "reason - and the resolution he was pointing towards was to abandon absolute "
                "space, not to re-centre it."),
    ),

    compression=dict(
        assessed=True, drifted=True,
        list_phrasing="Kinematical equivalence.",
        source_wording=("“Bertrand Russel's contention that the observable phenomena will be the "
                        "same whether the Earth rotates or the Heavens revolve, as well as Fred "
                        "Hoyle's declaration that the geocentric view is as good as anybody "
                        "else's, but not better, they are only tenable <em>if certain "
                        "presuppositions are assumed to be self-evident. Which they are not!</em>”"),
        drift_type="hedge_dropped",
        note=("Three qualifications travel with this proposition in <em>De Labore Solis</em> and "
              "none of them survives into the eight list items. <strong>Whose claim it is:</strong> "
              "in the book the equivalence belongs to Russell and Hoyle, who are named, and van der "
              "Kamp&rsquo;s sentence about them is a refusal &mdash; their claims hold only on "
              "presuppositions he rejects in the next three words. On the list the same proposition "
              "appears in his own name. <strong>The antecedent:</strong> his relativistic argument "
              "runs under &ldquo;If Einstein is right &hellip;&rdquo; (p. 67), and he held general "
              "relativity untenable in its present form; the list asserts the consequent with the "
              "antecedent removed. <strong>The demand:</strong> the book opens by asking for a "
              "control experiment to settle the question (pp. 6&ndash;7) and warns that a null "
              "result licenses no universal negative &mdash; &ldquo;if in the Sahara no icefields "
              "can be found, this observation does not thereby prove that icefields exist "
              "nowhere&rdquo; (p. 6). Items 29, 88 and 317 are universal negatives built from null "
              "results, which is the move his own line was written to block. "
              "<strong>The refutation above answers the source, not the fragment:</strong> it "
              "concedes the relativity principle outright, at the strength the modern experiments "
              "give it, and puts the weight on the scope Poincaré wrote into the sentence and on "
              "what a dynamical rotating-cosmos defence costs once it leaves that scope. "
              "This is a rare case in which compression makes the argument look <em>stronger</em> "
              "than its author left it: he published a request for a trial, and the list publishes "
              "a verdict. Compare <a href=\"#ARG-R01\">ARG-R01</a>, where the same book is "
              "compressed the other way &mdash; a concession promoted to a proof with its wording "
              "intact."),
    ),

    verdict_challenge=dict(challenged=False, proposed_verdict=None, reasoning=None),

    people=["PER-VANDERKAMP", "PER-BOUW", "PER-SUNGENIS"],
    related=["R01", "R02", "R05", "R06", "R08", "R11", "A02", "A03", "A05", "E01"],

    sources=[
        dict(label="van der Kamp, De Labore Solis: Airy's Failure Reconsidered (1988) — the "
                   "Russell/Hoyle paragraph at scan p. 62, the Poincaré principle quoted at "
                   "p. 45, the control-experiment demand and the Sahara line at pp. 6–7",
             url="https://geocentricity.com/bibastron/ts_history/de_labore.pdf"),
        dict(label="Poincaré, “The Present and the Future of Mathematical Physics”, St Louis, "
                   "1904 — the principle of relativity stated for “a uniform motion of "
                   "translation”",
             url="https://maricourt.press/keohane_foy/contents/henri-poincares-1904-lecture/"),
        dict(label="Herrmann et al., “Rotating optical cavity experiment testing Lorentz "
                   "invariance at the 10⁻¹⁷ level”, Phys. Rev. D 80:105011 (2009)",
             url="https://arxiv.org/abs/1002.1284"),
        dict(label="Nagel et al., “Direct terrestrial test of Lorentz symmetry in "
                   "electrodynamics to 10⁻¹⁸”, Nature Communications 6:8174 (2015)",
             url="https://research-repository.uwa.edu.au/en/publications/direct-terrestrial-test-of-lorentz-symmetry-in-electrodynamics-to/"),
        dict(label="Kennedy–Thorndike experiment — the velocity-dependence test van der Kamp "
                   "asked for, and its modern versions using the Earth's own rotation and orbit "
                   "as the varying platform velocity",
             url="https://en.wikipedia.org/wiki/Kennedy%E2%80%93Thorndike_experiment"),
        dict(label="Wright & Eastman, “Barycentric corrections at 1 cm/s for precise Doppler "
                   "velocities”, PASP 126:838 (2014)",
             url="https://arxiv.org/abs/1409.4774"),
        dict(label="Planck 2018 results I (A&A 641:A1) — Solar System velocity 369.82 ± 0.11 km/s "
                   "from the CMB dipole, and the “orbital dipole” used as the absolute "
                   "photometric calibrator from 30 to 353 GHz",
             url="https://www.aanda.org/articles/aa/full_html/2020/09/aa33880-18/aa33880-18.html"),
        dict(label="Di Virgilio et al., EPJ C 82:824 (2022) — Earth rotation rate to better than "
                   "1 part in 10⁹ at the Wettzell ring laser",
             url="https://link.springer.com/article/10.1140/epjc/s10052-022-10798-9"),
        dict(label="Hafele–Keating experiment (flights 1971, Science, July 1972) — clocks on fast "
                   "platforms, results agreeing with relativity to the ~10% precision of the "
                   "experiment",
             url="https://en.wikipedia.org/wiki/Hafele%E2%80%93Keating_experiment"),
        dict(label="Bouw, obituary of Walter van der Kamp, Biblical Astronomy no. 84 — The Heart "
                   "of the Matter drafted 1967, printed January 1968, and “went nowhere fast”",
             url="https://www.geocentricity.com/ba1/no084/obits.pdf"),
        dict(label="Faulkner, “The Rise of the Modern Geocentric Theory Movement” (Answers in "
                   "Genesis) — names The Heart of the Matter (1968) and Airy Reconsidered (1970)",
             url="https://answersingenesis.org/astronomy/rise-of-modern-geocentric-theory-movement/"),
    ]),
}
