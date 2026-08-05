# -*- coding: utf-8 -*-
"""Hedge-rule audit, batch A — A02, A10, A22.

Written 2026-08-05 against THE HEDGE RULE in scripts/deep.py. Each entry is a
`compression` block ready to be dropped into the argument's batch file (A02 in
deep_batch1.py, A10 in deep_batch3.py, A22 in deep_batch2.py — note A22 lives in
batch 2, not batch 1) and removed from the `_PRE_RULE` set in deep.py.

Primary-source reach:
  A10  Rowbotham, Zetetic Astronomy — REACHED. 1865 ed. (Gutenberg 69892) and the
       enlarged 3rd ed. of 1881, ch. III (sacred-texts za21.htm). All four quoted
       sentences confirmed verbatim except one ("must of necessity partake of its
       eastward motion"), for which the retrieved text gives a near-neighbour
       sentence of identical force.
  A22  Ptolemy, Almagest I.4 and I.7 (Taliaferro trans.) — REACHED. Both quoted
       sentences confirmed verbatim.
  A02  Sungenis & Bennett, Galileo Was Wrong — NOT REACHED at the sentence level.
       Three archive.org copies were tried; all returned front matter and tables
       of contents only, never the body of the Michelson-Gale section. The
       assessment below therefore rests on what our own record already quotes,
       plus two corroborating TOC-level facts from two different editions: the
       section is headed "The Michelson-Gale Exp: Sidereal Relative Rotation"
       (4275.o, p. 637) and the Sagnac section is headed "Georges Sagnac:
       Rediscovery of Absolute Motion" (GallileoWasWrong, p. 361). Both headings
       are consistent with the disjunctive reading recorded in our passage; the
       verbatim wording of the summary sentence remains unverified by us.
"""

HEDGE_A = {

"A02": dict(
    assessed=True, drifted=True,
    list_phrasing=(
        "Michelson–Gale ether drift detection. / "
        "Sagnac effect consistent with stationary Earth. / "
        "Sagnac proves apparatus rotation."),
    source_wording=(
        "&ldquo;Michelson-Gale detected the ether moving past the Earth&rsquo;s surface at 2% "
        "of the rotation speed. &hellip; the Michelson-Gale experiment measured <em>either</em> "
        "the effect of the Earth&rsquo;s rotation <em>or</em> the ether&rsquo;s rotation around "
        "the Earth.&rdquo;"),
    drift_type="force_upgraded",
    note=(
        "Sungenis and Bennett do not misreport the experiment. They say on the same pages that "
        "Michelson&ndash;Gale &ldquo;did not produce null results&rdquo; and that the displacement "
        "was closely related to the Earth&rsquo;s rotational velocity, and their summary sentence "
        "is a <em>disjunction</em>: the apparatus measured <em>either</em> the Earth&rsquo;s "
        "rotation <em>or</em> the ether&rsquo;s rotation around it. That is a statement about what "
        "an interferometer cannot decide. It is not a claim that the Earth is at rest, and the "
        "section heading in their own text &mdash; <em>Sidereal Relative Rotation</em> &mdash; "
        "says as much.</p>"
        "<p>The list keeps the caution and changes the job. &ldquo;Sagnac effect consistent with "
        "stationary Earth&rdquo; is a fair rendering of one branch of that disjunction, but it is "
        "entered as one of 461 numbered proofs, where <em>consistent with</em> is counted as "
        "evidence <em>for</em>. A live option has been promoted to a demonstration without a word "
        "being strengthened. Item 281, &ldquo;Sagnac proves apparatus rotation,&rdquo; is correct "
        "physics pointing the other way, and it sits in the same list unremarked.</p>"
        "<p><strong>The refutation above answers the disjunction, not the fragment.</strong> It "
        "concedes outright that Michelson&ndash;Gale alone cannot assign the rotation to one body, "
        "and puts the weight on the instruments a rotating optical medium cannot reach: the "
        "pendulum, the gyrocompass, and Coriolis circulation.")),

"A10": dict(
    assessed=True, drifted=True,
    list_phrasing=(
        "Atmospheric coupling unexplained. / "
        "No wind drag from 67,000 mph orbit. / "
        "No visible rotation of atmosphere or clouds."),
    source_wording=(
        "&ldquo;it is exceedingly difficult if not altogether impossible to conceive of such a "
        "mass moving at such a rate, and yet not taking the atmosphere along with it. &hellip; "
        "Hence we are compelled to conclude that if the earth revolves, the atmosphere revolves "
        "also, and in the same direction.&rdquo; &mdash; and, at the end of the argument, "
        "&ldquo;Such a state of the atmosphere is compatible <em>only</em> with the fact which "
        "other evidence has demonstrated, that the earth is at rest.&rdquo;"),
    drift_type="reversed",
    note=(
        "Rowbotham is blunter than the list, not more careful: his conclusion is that the observed "
        "sky is compatible <em>only</em> with a stationary Earth. So the drift is not in the "
        "strength. It is in the premise. Rowbotham <em>grants</em> co-rotation and spends a page "
        "establishing it &mdash; the grinding-stone experiment exists to show that a rugged "
        "spinning globe must carry its air &mdash; and his objection begins only afterwards: if "
        "the whole envelope streams east at 1,042 miles an hour, everything floating in it should "
        "stream east too, and clouds visibly do not. The list inverts that into &ldquo;atmospheric "
        "coupling unexplained&rdquo; and a drag from the 67,000 mph <em>orbit</em>, a figure and a "
        "mechanism absent from his atmospheric argument, which concerns axial rotation only.</p>"
        "<p><strong>This bears on our own text.</strong> The refutation opens by answering the "
        "fragment &mdash; Galileo&rsquo;s sealed cabin, the air is inside the cabin, the atmosphere "
        "co-rotates &mdash; and Rowbotham agrees with every word of it. The part that answers "
        "<em>him</em> is the arithmetic, a 10 m/s stratum riding a 465 m/s carrier, and the "
        "hemispheric reversal of the Coriolis deflection that his own citation of Ross&rsquo;s "
        "north-east and south-east trades hands us.")),

"A22": dict(
    assessed=True, drifted=True,
    list_phrasing=(
        "Celestial sphere rotation about observer. / "
        "Day–night cycle from firmament rotation. / "
        "Precession from dome rotation. / "
        "Seasonal stars via dome."),
    source_wording=(
        "<em>Almagest</em> I.7: &ldquo;as far as the appearances of the stars are concerned, "
        "nothing would perhaps keep things from being in accordance with this simpler "
        "conjecture&rdquo; &mdash; the conjecture being that the earth turns. And I.4: &ldquo;if "
        "it were flat, the stars would rise and set for all people together and at the same "
        "time.&rdquo;"),
    drift_type="force_upgraded",
    note=(
        "Ptolemy&rsquo;s chapter I.7 says close to the opposite of what twenty proof-items need it "
        "to say. He states the rotating-Earth hypothesis and concedes it: as far as the stars go, "
        "nothing would keep things from being in accordance with the simpler conjecture. On his "
        "own account the sky cannot decide. He rejects rotation on other grounds &mdash; clouds "
        "and thrown objects would be left behind &mdash; and that is the one part of the chapter "
        "that is wrong. The list takes the very appearances he declared non-discriminating and "
        "enters them as evidence, twenty times over.</p>"
        "<p>A second drift rides along, and the enum has no clean word for it. Items 34, 39 and "
        "210 credit him with a &ldquo;firmament&rdquo; and a &ldquo;dome.&rdquo; Ptolemy has "
        "neither. Three chapters earlier he proves the Earth spherical and disposes of the flat "
        "option in a single clause. <em>unsourced_addition</em> understates that: he does not "
        "merely omit the dome, he refutes the cosmology it belongs to.</p>"
        "<p><strong>Our refutation answers Ptolemy</strong>, agreeing with him that these "
        "observations were the shared premises of the dispute, and dating the four measurements "
        "that ended the equivalence he was right to assert.")),
}
