# -*- coding: utf-8 -*-
"""Batch 10 — B09. "Plumb lines are perpendicular everywhere."

Three items: 48 "Plumb lines perpendicular worldwide.", 396 "Architecture
plumb/level universal.", 397 "Skyscraper vertical stable." Verdict REFUTED, kept.

Research notes for whoever picks this up next.

1. THE CLUSTER HAS TWO DOCUMENTED ANCESTORS, ONE PER HALF, AND OUR RECORD'S YEAR
   IS WRONG FOR BOTH. Item 48 (plumb lines) descends from Rowbotham; items 396 and
   397 (architecture, skyscrapers) match Carpenter. Neither text is the 1865 book
   edition our cluster record cites.

   (a) ROWBOTHAM, 3rd ed. 1881, ch. XIV "Examination of the So-Called 'Proofs' of
       the Earth's Rotundity", section ARCS OF THE MERIDIAN, printed pp. 245-246
       (sacred-texts za40.htm): "If, however, the celestial surface is not concave,
       but horizontal, two plumb-lines suspended north and south of each other would
       be parallel, and would indicate equal length in all the degrees of latitude
       ... The differences required by a globe are not found in practice, but such
       as a plane would produce are invariably found."
       NOT LOCATED in the 1865 first book edition: Gutenberg #69892 was searched for
       plumb, perpendicular, wall, building, spire and tower. "plumb" occurs three
       times in that text and all three are instrumental (the Encyclopaedia
       Britannica "Levelling" extract defining level as crossing the plumb-line at
       right angles; the air-gun "carefully adjusted by a plumb-line"; the Plymouth
       Hoe mirror "fixed, by the aid of a plumb-line, in a true vertical position").
       The 1865 text DOES carry the arcs-of-the-meridian material and the "oblong
       instead of an oblate spheroid" quotation from Hugh Murray's Encyclopaedia of
       Geography; what the third edition ADDS is the von Gumpach extract and the
       plumb-lines-are-parallel inference. So this is the same edition trap logged
       for A05, B01, B04 and B06 — and A10 already carries year="1881" for
       Rowbotham in the same file, so the value is internally inconsistent too.
       Reported in record_problems; NOT edited here, this agent owns one file.

   (b) CARPENTER 1885, One Hundred Proofs, proof 72, indexed "Walls not parallel!":
       "Astronomers tell us that, in consequence of the Earth's 'rotundity,' the
       perpendicular walls of buildings are, nowhere, parallel, and that even the
       walls of houses on opposite sides of a street are not strictly so! But, since
       all observation fails to find any evidence of this want of parallelism which
       theory demands, the idea must be renounced as being absurd and in opposition
       to all well-known facts."
       This is the buildings half, verbatim, and it is the only located ancestor for
       items 396 and 397. PER-CARPENTER therefore belongs in this entry's people[].

   Origination is NOT established for either. Both are the earliest texts located
   carrying the respective forms; the gloss claims ancestry and nothing more.

2. NOBODY IN THE SOURCES OBSERVED A PLUMB LINE. This is the single most important
   fact about the cluster and it is easy to miss. Rowbotham's claim is an INFERENCE
   from a printed table of British meridian-arc degree lengths (Beachy Head, Dunnose,
   Clifton, Blenheim, Greenwich, Arbury Hill), quoted from Hugh Murray. Carpenter's
   claim is that no observation shows the non-parallelism. Neither hangs a wire.
   Answer the inference, not a measurement they never made.

3. DO NOT STOP AT THE CONDITIONAL. Rowbotham's sentence opens "If, however, the
   celestial surface is not concave, but horizontal ..." and it is tempting to
   present the argument as merely hypothetical. The NEXT sentence states the
   conclusion flat: "The differences required by a globe are not found in practice,
   but such as a plane would produce are invariably found. Hence the failure of
   geodesy becomes evidence against rotundity ... and therefore of mathematical and
   logical necessity A plane." Quote through to there. He is not hedging.

4. THE ARITHMETIC, ALL OF IT RECOMPUTED HERE 2026-08-10, R = 6,371 km.
   Two plumb lines a distance d apart converge by d/R radians:
     d = 20 m (a street)          -> 3.14e-6 rad = 0.65 arcsec
     d = 100 m (a city block)     -> 1.57e-5 rad = 3.24 arcsec
     d = 1,298 m (Verrazzano)     -> 2.04e-4 rad = 42.0 arcsec
     d = 1,410 m (Humber)         -> 2.21e-4 rad = 45.7 arcsec
   Tower-top spread = d*h/R:
     Verrazzano 1,298 m x 211 m / R = 43.0 mm. PUBLISHED FIGURE 41.275 mm
       (1 5/8 in). Agreement ~4%; do not claim an exact reproduction — the residual
       is the choice of local radius and of where the tower base is reckoned from.
     Humber 1,410 m x 155.5 m / R = 34.4 mm. Published 36 mm. ~5%.
   LIGO: sagitta of a 4 km chord = 4000^2/(2R) = 1.26 m. LIGO's own public page
     rounds it to "nearly a meter" — quote theirs, give ours as the sagitta, and do
     not manufacture a discrepancy out of a rounding.
   Latitude: 1 degree = 111.19 km, 1 arcminute = 1,853 m. The nautical mile is
     DEFINED as one minute of latitude, i.e. as the distance over which the plumb
     line turns by one arcminute against the stars.

5. THE TWO-HORN ARGUMENT AGAINST ROWBOTHAM'S OWN MODEL — the strongest thing in the
   entry, and it is derived, so check it before reusing it.
   His premise is that the "celestial surface" is horizontal, i.e. the plane of the
   sky is parallel to the plane of the earth.
   HORN 1: if the sky is far enough that its rays arrive parallel, then a plumb line
   and a star subtend the same angle everywhere, latitude does not vary, and the
   table of degree lengths he is arguing from cannot exist as a quantity.
   HORN 2: if the sky is at finite height h — which is his position, stated six pages
   earlier in the same chapter under DECLINATION OF THE POLE STAR, where Polaris
   sinking towards the equator is "an ordinary effect of perspective" — then
   d = h*cot(alpha) and the ground length of one degree is h/sin^2(alpha) per radian.
   At alpha = 51 deg that is 0.0289h per degree; at alpha = 10 deg it is 0.5789h.
   TWENTY TIMES LONGER near the equator, and in the direction of lengthening. The
   measured degree runs 110.574 km at the equator to 111.694 km at the pole: about
   1%, and the other way. So "equal degrees on a plane" fails on his own optics.

6. HIS ANOMALY IS REAL AND ITS CAUSE CONVICTS HIM. The British arcs really did come
   out with degrees decreasing northward — "as if the Earth were an oblong instead
   of an oblate spheroid" — and Murray's own text says "It has been found impossible
   to explain the want of agreement in a satisfactory way." The standard answer is
   station error: the plumb line at each astronomical station is pulled sideways by
   the local mass, corrupting the observed latitude. 1911 Encyclopaedia Britannica,
   "Earth, Figure of the": "At sixteen astronomical stations in the English survey
   the disturbance of latitude due to the form of the ground has been computed ...
   At six stations the deflection is under 2", at six others it is between 2" and 4",
   and at four stations it exceeds 4"," and "The non-recognition of this circumstance
   often led to much perplexity in the early history of geodesy."
   MAGNITUDE CHECK (ours): his table spans 60,766-60,890 fathoms, a spread of 124 in
   60,800 = 0.20%. The shortest arc in it, Dunnose-Greenwich, is about 0.86 deg =
   3,096 arcsec; 0.20% of that is 6.2 arcsec of latitude error. That is the ordinary
   size of a vertical deflection. State this as a magnitude argument, NOT as a
   published reanalysis of that table — we did not find one.

7. WHY DEFLECTION OF THE VERTICAL IS NOT AN AD HOC RESCUE. This is the defence to
   beat, and it is von Gumpach's, quoted by Rowbotham at pp. 243-244: astronomy
   "gives to the plumb-lines such imaginary directions as are needed in order to
   adapt the empirical results of geodetic measurements to the earth's imagined
   form." Three answers, in ascending order:
   (a) It made a prediction and the prediction FAILED. Everest's Great Trigonometrical
       Survey found the Kaliana-Kalianpur latitude difference 5.24 arcsec smaller
       geodetically than astronomically. Pratt (read 7 Dec 1854, published 1855)
       forward-computed the Himalaya's attraction and got 15.885 arcsec — more than
       three times the observed. A fudge factor does not overshoot by 3x. Airy's
       three-page 1855 reply proposed compensating mass at depth: that is the origin
       of isostasy, now independently confirmed by seismic crustal roots.
       Source: Watts, "Isostasy and Flexure of the Lithosphere", ch. 1 (history).
       Note the cross-link: this is the same G. B. Airy as ARG-A03.
   (b) It is now MEASURED, not inferred. NGS deflection-of-the-vertical surveys point
       a camera along the local plumb line and compare the star field against a
       GNSS-derived position and time: accuracy 0.1 arcsec, values reaching "many 10s
       of arc-seconds". The slope "is determined solely by the camera system".
   (c) Three independent instruments agree. Sensors 16(4):565 (2016) compares a
       QDaedalus astro-geodetic camera, GNSS-plus-geometric-levelling, and the
       ITALGEO2005 gravimetric geoid: the first two agree "well within the 1 arcsec
       level", the gravimetric model at about 2.5 arcsec standard deviation and
       "statistically consistent with the others".

8. THE TAMARACK MINE, because a well-read defender will raise it and it is the only
   real plumb-line anomaly on offer. Calumet, Michigan, 1901-02: J. B. Watson hung
   4,250 ft wires 15-16 ft apart down mine shafts and found them FARTHER APART at the
   bottom. F. W. McNair repeated it across three shafts (Science XV, 20 June 1902);
   results ran -0.028 to +0.141 ft with measurement error under 0.003 ft; he
   attributed the divergence to convection currents in the shafts. Our arithmetic:
   the geometric convergence expected for 15 ft of separation over 4,250 ft of depth
   is 4250 x 15/20,902,231 = 0.0031 ft, about 0.9 mm — one tenth of the smallest
   number in McNair's range and a fortieth of the largest. The experiment could not
   have detected the effect either way. Say that; do not say the anomaly is a fake.

9. VERDICT. REFUTED kept. SELF-CONTRADICTED was seriously considered, on the ground
   that Rowbotham's evidence (a table of degree lengths measured against the plumb
   line at each station) presupposes the plumb-line variation he concludes against.
   Not taken, for two reasons. First, that contradiction is DERIVED BY US, not
   conceded by him — unlike B05, where he reprints the correction he then denies,
   or B06. Second, the plain situation is that a testable claim was made and direct
   measurement came back against it: bridge towers built non-parallel by design, and
   the plumb direction measured against the stars to a tenth of an arcsecond.
   MISLEADING was also weighed for items 396/397, which taken narrowly are the
   convenience-frame move of R08 rather than a false claim. One verdict covers three
   items; the false one dominates. No verdict_challenge filed. The record problems
   are about `year`, `real_source` and the cluster `note`, not the verdict.

10. WHAT CARPENTER GETS RIGHT, AND IT MATTERS FOR THE STRAW-MAN FIELD. His statement
    of the globe's prediction is ACCURATE — vertical walls are nowhere exactly
    parallel, and houses across a street are not strictly so. He does not caricature
    the position; he states it correctly and then denies that it is observable. At
    his scale, in 1885, he was right that it was not observable: 0.65 arcsec across a
    street. Credit that in the steelman rather than reaching for the easy bust. The
    straw man in this cluster is in the Rowbotham/von Gumpach half only.

11. NOT LOCATED ELSEWHERE, each search scoped: the argument is not in the archive.org
    text of Dubay's 200 Proofs (item 200ProofsEarthIsNotASpinningBall, searched for
    plumb, perpendicular, architect, skyscraper, vertical — proof 7 is the surveyors/
    engineers/architects "no allowance" claim, which is B05/B06 territory, not this
    one); not in the archive.org text of Winship's Zetetic Cosmogony (item
    zeteticcosmogony00wins, one hit on "perpendicular", a radio-transmission aside);
    and in Scott's Terra Firma (item cu31924031764594) "plumb line" occurs once, as
    part of a triangulation instrument for measuring the Sun's height. Those are
    reports on the texts searched.

12. QUOTE PROVENANCE. Rowbotham 1881 was read in two transcriptions: sacred-texts
    za40.htm (printed pp. 245-246) and the archive.org scan at item
    zeteticastronomy-earthnotaglobe, file ZeteticAstronomy-EarthNotaGlobe-3e-format2,
    which is a REFORMATTED PDF and paginates the same passage at about pp. 186-189.
    Do not merge the two page ranges; the printed-page citation follows sacred-texts.
    Both transcriptions read "spewing" where the word is plainly "shewing"; the quote
    below prints "shewing" and the gloss records the OCR slip. Neither was checked
    against a print copy. Carpenter is quoted from Gutenberg #55387, which reproduces
    the Baltimore 1885 first printing (title page and Chew Street imprint present).
"""

ENTRY = {

"B09": dict(

    tldr=("Rowbotham's plumb-line sentence is in the 1881 third edition, not the 1865 book, and "
          "neither it nor Carpenter's version reports an observation of a plumb line — one "
          "argues from a table of survey arcs, the other from what the instruments of his day "
          "could not detect. Two plumb lines do converge — by 0.65 of an arcsecond across a "
          "twenty-metre street, which is why a Victorian bricklayer saw nothing, and by 42 "
          "arcseconds across the Verrazzano-Narrows, whose operator says its towers were built "
          "1 5/8 inches farther apart at the top to compensate for the curvature. And the "
          "survey discrepancy Rowbotham reads as the failure of geodesy traces to the plumb "
          "line being pulled sideways by the ground beneath each station — the effect whose "
          "measurement produced the theory of isostasy in 1855."),

    passage=dict(
        work="WRK-ROWBOTHAM-1865",
        pd=True,
        locator=("3rd ed., rev. and enl. (London: Day, 1881), ch. XIV “Examination of the "
                 "So-Called ‘Proofs’ of the Earth's Rotundity”, section “Arcs of the Meridian”, "
                 "printed pp. 245–246 as paginated at sacred-texts za40.htm. Not the 1865 first "
                 "book edition — see the gloss. A reformatted archive.org scan of the third "
                 "edition paginates the same passage at about pp. 186–189; the two page ranges "
                 "are not interchangeable, and neither transcription was checked against print"),
        quote=("The fallacy involved in all the attempts to prove the oblate spheroidal form of "
               "the earth, is, that the earth is first assumed to be a globe, the celestial "
               "surface above it to be concave, and the plumb-lines to be radii. If this were "
               "the true condition of things, then all the degrees of latitude would be the same "
               "in length; and if the earth were really “flattened at the poles,” the degrees "
               "would certainly shorten in going from the equator towards the north. If, "
               "however, the celestial surface is not concave, but horizontal, two plumb-lines "
               "suspended north and south of each other would be parallel, and would indicate "
               "equal length in all the degrees of latitude, thereby shewing the earth to be "
               "parallel with the celestial surface, and therefore a plane. The differences "
               "required by a globe are not found in practice, but such as a plane would produce "
               "are invariably found. Hence the failure of geodesy becomes evidence against "
               "rotundity, but demonstrating that the earth is parallel to the horizontal "
               "heavens, and therefore of mathematical and logical necessity A plane."),
        gloss="""<p><strong>Read the last three sentences before deciding this is a hypothetical.</strong> The argument opens on a condition &mdash; <em>if</em> the celestial surface is horizontal &mdash; and it would be convenient for us to stop there and say the source never asserted anything. It does. The condition is followed immediately by a flat empirical claim (&ldquo;The differences required by a globe are not found in practice&rdquo;) and a flat conclusion (&ldquo;of mathematical and logical necessity A plane&rdquo;). Rowbotham is not hedging and this page does not pretend he is.</p>
<p><strong>What he is arguing from is a table, not a plumb line.</strong> The section is about arcs of the meridian. Six pages of it reproduce the British Ordnance Survey&rsquo;s degree lengths &mdash; Beachy Head, Dunnose, Clifton, Blenheim, Greenwich, Arbury Hill &mdash; quoted from Hugh Murray&rsquo;s <em>Encyclopaedia of Geography</em>, together with Murray&rsquo;s observation that the degrees &ldquo;appear to <em>decrease</em>, as if the Earth were an <em>oblong</em> instead of an <em>oblate</em> spheroid&rdquo; and his admission that &ldquo;It has been found impossible to explain the want of agreement in a satisfactory way.&rdquo; The parallel plumb lines are an <em>inference</em> from that discrepancy. Neither this passage nor Carpenter&rsquo;s reports hanging a wire and measuring one, and the refutation below is aimed at the inference rather than at a measurement they did not make.</p>
<p><strong>The edition matters.</strong> This passage is in the third edition of 1881. It is not located in the 1865 first book edition: the Project Gutenberg text of that edition (#69892) was searched for <em>plumb</em>, <em>perpendicular</em>, <em>wall</em>, <em>building</em>, <em>spire</em> and <em>tower</em>, and its three occurrences of &ldquo;plumb&rdquo; are all instrumental &mdash; the <em>Encyclop&aelig;dia Britannica</em> &ldquo;Levelling&rdquo; extract that defines the level as a line crossing the plumb-line at right angles, an air-gun &ldquo;carefully adjusted by a plumb-line&rdquo;, and a mirror at Plymouth Hoe &ldquo;fixed, by the aid of a plumb-line, in a true vertical position&rdquo;. The 1865 text carries the arcs material and the &ldquo;oblong&rdquo; quotation; what 1881 adds is the von Gumpach extract and the plumb-lines-are-parallel inference drawn from them. Both online transcriptions of the third edition read &ldquo;spewing&rdquo; in the sentence above, an OCR slip for &ldquo;shewing&rdquo;.</p>
<p><strong>The other half of the cluster is Carpenter&rsquo;s, and it is a different claim.</strong> Items 396 and 397 &mdash; architecture and skyscrapers &mdash; match <em>One Hundred Proofs that the Earth Is Not a Globe</em> (Baltimore, 1885), proof 72, indexed by its author as &ldquo;Walls not parallel!&rdquo;: <em>&ldquo;Astronomers tell us that, in consequence of the Earth&rsquo;s &lsquo;rotundity,&rsquo; the perpendicular walls of buildings are, nowhere, parallel, and that even the walls of houses on opposite sides of a street are not strictly so! But, since all observation fails to find any evidence of this want of parallelism which theory demands, the idea must be renounced as being absurd and in opposition to all well-known facts.&rdquo;</em> Note what that is: an accurate statement of the globe&rsquo;s prediction, followed by a claim that the prediction is not observable. At his scale it was not. Across a twenty-metre street the two walls lean apart by 0.65 of an arcsecond.</p>
<p><strong>What these passages are being cited as.</strong> The earliest texts located carrying the two halves of this cluster in the form the list uses. They are ancestors and that is all &mdash; no earlier flat-earth or geocentric text was traced that puts either claim first, and neither man is credited here with originating it.</p>"""),

    steelman=dict(
        description="""<p><strong>SURFACE (weak &mdash; do not use).</strong> &ldquo;Plumb lines obviously converge on the centre; this is trivially false.&rdquo; It walks straight into Carpenter&rsquo;s actual point. He never denied what the theory predicts; he denied that anybody had <em>seen</em> it. Across the width of a street the predicted lean is 0.65 arcsec, far below what a mason&rsquo;s plumb bob, a builder&rsquo;s square or a spirit level resolves. Answering &ldquo;but the theory says so&rdquo; to a man complaining that the theory&rsquo;s prediction has never been observed is answering nothing.</p>
<p><strong>DEEPER.</strong> The argument is non-discriminating: &ldquo;plumb&rdquo; means <em>along local gravity</em> and &ldquo;level&rdquo; means <em>perpendicular to it</em>, so a builder who works plumb and level has measured the direction of gravity at one site and nothing else. True, and it disposes of items 396 and 397 &mdash; but it does not touch Rowbotham, whose claim is not about definitions at all. His is an inference from published survey data, and the data really were discordant.</p>
<p><strong>KERNEL.</strong> Two genuinely true things sit underneath this cluster. The first: <em>the British arc measurements came out wrong, and a standard reference work of the day said so.</em> The degrees decreased going north, which is the signature of a prolate Earth and the opposite of what flattening at the poles requires, and Murray&rsquo;s own text concedes that the want of agreement could not be satisfactorily explained. Rowbotham did not invent that; he found it in print and quoted it accurately. The second, which is sharper: <em>the plumb line genuinely does not point at the centre of the Earth,</em> and geodesy genuinely does substitute a computed ellipsoid normal for the observed vertical. Rowbotham prints von Gumpach making exactly that charge &mdash; that astronomy &ldquo;gives to the plumb-lines such imaginary directions as are needed in order to adapt the empirical results of geodetic measurements to the earth&rsquo;s imagined form.&rdquo; The distinction between the direction a plumb bob actually hangs and the direction the reference figure says it should is real, has a name, and is the subject of a whole sub-discipline.</p>""",
        why_it_doesnt_save_claim="""<p>Because both true things have <em>the same single cause</em>, and that cause is the plumb line moving.</p>
<p>The arcs disagreed because the astronomical latitude of each station is read against a plumb line that the surrounding rock pulls sideways. The 1911 <em>Encyclop&aelig;dia Britannica</em>&rsquo;s article on the figure of the Earth reports the computation for the English survey itself: at sixteen astronomical stations, six deflections under 2&Prime;, six between 2&Prime; and 4&Prime;, four above 4&Prime; &mdash; and adds that &ldquo;The non-recognition of this circumstance often led to much perplexity in the early history of geodesy.&rdquo; Rowbotham was reading the perplexity. The scatter in his own table is 124 fathoms in 60,800, or 0.20%; on its shortest arc, Dunnose to Greenwich at about 0.86&deg;, that is 6.2 arcseconds of latitude error. Which is precisely the size of the deflections the Britannica lists.</p>
<p>So the argument runs on a quantity that exists only because plumb lines are <em>not</em> parallel. Take the non-parallelism away and there is no station error, no discordance between arcs, and nothing for the passage to be about. The strongest thing in the cluster &mdash; von Gumpach&rsquo;s complaint that the plumb line does not point where the ellipsoid says &mdash; is a complaint that the local vertical wanders from place to place. That is the claim being denied.</p>"""),

    refutation="""<p><strong>The concession first, because it is real and because the easy version of this rebuttal loses to it.</strong> At the scale Carpenter names, he was right that nothing was observable. Two plumb lines a distance <em>d</em> apart converge by <em>d</em>/<em>R</em> radians. Across a twenty-metre street that is 3.1 &times; 10<sup>&minus;6</sup> rad, or <strong>0.65 arcseconds</strong>; across a hundred-metre city block, 3.2 arcseconds. No mason, spirit level or Victorian theodolite was going to find that in a party wall, and saying &ldquo;the theory predicts it&rdquo; to a man whose objection is that the prediction has never been seen concedes his point rather than answering it. (Recomputed here 2026-08-10 with <em>R</em> = 6,371 km.)</p>

<p><strong>What the verdict ranges over.</strong> Not &ldquo;a plumb line hangs perpendicular to the local level surface&rdquo; &mdash; that is true, on a globe as much as on a plane, and it is what a builder means by plumb. The cluster&rsquo;s claim is that plumb lines are parallel <em>to each other</em>, everywhere, and that this is evidence for a plane. Both halves fail, and they fail differently: the parallelism is contradicted by direct measurement at scales where it is big enough to matter, and the inference Rowbotham draws it from is self-defeating on his own optics.</p>

<h4>1. Where the effect is large enough to matter, it is measured and built for</h4>

<p>Go from a street to a strait. The Verrazzano-Narrows Bridge carries its towers 4,260 ft (1,298 m) apart and 693 ft (211 m) high. The two verticals at those foundations differ by 42 arcseconds, which over the tower height is 43 mm. The Metropolitan Transportation Authority, which owns and operates the bridge, puts it in its own public description: the towers are <em>&ldquo;1 5/8 inches farther apart at their tops than at their bases because the 4,260 foot distance between them made it necessary to compensate for the earth&rsquo;s curvature&rdquo;</em>. The standard description of the structure states the conclusion in Carpenter&rsquo;s own words and the opposite sense: <strong>&ldquo;The towers are not parallel to each other.&rdquo;</strong> The Humber Bridge, 1,410 m between towers and 155.5 m high, is described the same way &mdash; &ldquo;although vertical, [the towers] are 1.4 inches (36 mm) farther apart at the top than the bottom due to the curvature of the Earth.&rdquo; Our arithmetic gives 43.0 mm and 34.4 mm against the published 41.3 mm and 36 mm: agreement to within about 5%, the residue being the local radius of curvature and where the base is reckoned from. This is not a debating point produced for a website. It is a dimension on a drawing, and the two structures were built to it.</p>

<p>The same correction turns up wherever a straight line is long. LIGO&rsquo;s public description of its own construction: <em>&ldquo;Over the 4km length of each arm, the Earth curves away by nearly a meter!&rdquo;</em> &mdash; and the concrete slab under the beam tube had to be precision-levelled so that a laser leaving the corner station in a straight line &ldquo;strikes the test mass/mirror at the end of each arm, and not a meter above it.&rdquo; The sagitta of a 4 km chord is 1.26 m. An instrument built to detect a strain of one part in 10<sup>21</sup> is aligned around the fact that the local vertical rotates by two arcminutes over 4 km.</p>

<h4>2. The direction of a plumb line against the stars is what latitude <em>is</em></h4>

<p>Hang a plumb bob, or level a bubble, which is the same measurement made flat: you have fixed the local vertical. Now measure the angle from it to a star. Measured against the celestial pole, that angle is your astronomical latitude. Travel and it changes: the local vertical swings by one degree for every 111 km of ground you cross, in any direction on the surface, and by one degree of latitude for every 111 km of northing. The unit sailors use encodes it &mdash; the nautical mile <em>is</em> one minute of latitude, 1,853 m, the distance over which the plumb line turns by one arcminute relative to the sky. If plumb lines were parallel worldwide and the sky were far off, that angle would be the same everywhere, latitude would not exist as a measurable quantity, and there would be no degrees of the meridian to tabulate.</p>

<p><strong>Which is Rowbotham&rsquo;s problem, because the tabulated degrees are his evidence.</strong> His premise is that the celestial surface is &ldquo;not concave, but horizontal&rdquo; &mdash; a sky parallel to the plane. Take that premise seriously in either of its two available forms:</p>

<ul>
<li><strong>If the sky is far enough away that its rays arrive parallel</strong>, the angle between a plumb line and a star is identical at every station. Polaris stands at the same altitude in London and in Ceylon. There is no latitude, no arc, and no table &mdash; and the quantity Rowbotham spends six pages arguing about cannot be measured at all.</li>
<li><strong>If the sky is at a finite height <em>h</em></strong> &mdash; which is his actual position, set out six pages earlier in the same chapter, where Polaris sinking towards the equator is &ldquo;an ordinary effect of perspective&rdquo; like a receding row of lamp-posts &mdash; then a station seeing Polaris at altitude &alpha; stands at ground distance <em>h</em>&thinsp;cot&thinsp;&alpha; from beneath it, and one degree of &ldquo;latitude&rdquo; occupies a ground length proportional to 1/sin<sup>2</sup>&alpha;. At &alpha; = 51&deg; that is 0.029<em>h</em>; at &alpha; = 10&deg; it is 0.579<em>h</em>. <strong>A degree near the equator would be twenty times longer than a degree in England</strong>, and lengthening fast as you go south. The measured degree runs from 110.574 km at the equator to 111.694 km at the pole &mdash; about one per cent, and in the other direction.</li>
</ul>

<p>So the sentence &ldquo;two plumb-lines suspended north and south of each other would be parallel, and would indicate equal length in all the degrees of latitude&rdquo; does not follow from either version of his own sky. On the first there are no degrees; on the second they are grossly unequal. The globe predicts a one-per-cent lengthening polewards and that is what the surveys find, to the point where the residual disagreements are small enough to be diagnostic of something else.</p>

<h4>3. That something else is the plumb line, moving &mdash; and it was not invented to save the ellipsoid</h4>

<p>Rowbotham&rsquo;s anomaly is genuine. British degrees came out shortening northwards, an oblong figure, and his source concedes it could not be satisfactorily explained. The explanation, when it came, was that the astronomical latitude of a station is read against a plumb line deflected by the mass around it. The 1911 <em>Encyclop&aelig;dia Britannica</em> gives the numbers for the English survey specifically &mdash; sixteen stations computed, four of them deflected by more than 4 arcseconds by the form of the ground &mdash; and remarks that failing to recognise this &ldquo;often led to much perplexity in the early history of geodesy.&rdquo; Six arcseconds of latitude error at the ends of the shortest arc in Rowbotham&rsquo;s own table would produce the whole 0.20% spread in it.</p>

<p>Von Gumpach&rsquo;s reply, which Rowbotham prints, is that this is circular: astronomers assign the plumb lines &ldquo;such imaginary directions as are needed&rdquo; to fit the shape they have assumed. It is the best objection in the cluster and it has three answers.</p>

<p><strong>First, the theory made a prediction and the prediction failed.</strong> Everest&rsquo;s Great Trigonometrical Survey found the latitude difference between Kaliana and Kalianpur 5.24 arcseconds smaller by triangulation than by astronomy. J. H. Pratt, in a paper read on 7 December 1854 and published in 1855, computed forward from the visible mass of the Himalaya what deflection it ought to produce, and got 15.885 arcseconds &mdash; <em>more than three times</em> the observed value. A quantity invented to absorb discrepancies does not overshoot by a factor of three. What followed was Airy&rsquo;s three-page reply of 1855 proposing compensating light material at depth, which is the origin of isostasy, and whose crustal roots were later seen independently by seismology. (The same G. B. Airy as <a href="#ARG-A03">ARG-A03</a>, and the same year.)</p>

<p><strong>Second, the direction of the plumb line is now measured, not assigned.</strong> The US National Geodetic Survey&rsquo;s deflection-of-the-vertical surveys set a camera on a benchmark, align it precisely to the local plumb line, and compare the observed star field with the positions expected from a GNSS-derived location and time. Accuracy: 0.1 arcsecond. Observed deflections: &ldquo;many 10s of arc-seconds&rdquo;. The agency&rsquo;s own description of the method notes that while GNSS supplies position and time, &ldquo;the slope is determined solely by the camera system&rdquo;. That is the plumb bob and the sky, and nothing else.</p>

<p><strong>Third, independent instruments agree.</strong> A 2016 comparison in <em>Sensors</em> ran three unrelated methods at the same sites &mdash; an astro-geodetic zenith camera, GNSS heights differenced against spirit levelling, and a gravimetric geoid computed from measured gravity. The first two agree &ldquo;well within the 1 arcsec level&rdquo;; the gravity-derived values sit about 2.5 arcseconds out and remain &ldquo;statistically consistent with the others&rdquo;. A star camera, a levelling staff and a gravimeter are three different physical measurements &mdash; starlight, height differences, and the pull of gravity itself. They return the same tilt.</p>

<h4>4. Architecture and skyscrapers: a measurement of one point</h4>

<p>Items 396 and 397 need less. A builder&rsquo;s <em>plumb</em> is defined as the direction a weight hangs at that site and <em>level</em> as the surface perpendicular to it; a skyscraper is erected to a single vertical established at a single foundation. Nothing about that procedure compares the vertical at one site with the vertical at another, so nothing about it can show they are parallel &mdash; it is the convenience-frame move of <a href="#ARG-R08">ARG-R08</a> in mortar rather than in software. The place where two verticals <em>do</em> have to be reconciled is a structure long enough to stand on both, and there, as section 1 shows, the answer is on the drawings. And the stability of a tall building follows from each floor being level with respect to gravity where it is, which is a curved family of surfaces, not a stack of parallel planes &mdash; the same point <a href="#ARG-B06">ARG-B06</a> makes about the surveyor&rsquo;s word <em>level</em>, which the <em>Encyclop&aelig;dia Britannica</em> article Rowbotham himself reprints defines as <em>&ldquo;the curve of the Earth being the true level, and the tangent to it the apparent level.&rdquo;</em></p>

<h4>5. What is left</h4>

<p>Carpenter&rsquo;s observation was correct for his instruments and is now false for ours: the non-parallelism he could not find is 41 millimetres of designed spread between two bridge towers, and a tenth of an arcsecond is the routine precision with which the local vertical is now measured against the stars. Rowbotham&rsquo;s anomaly was real and its cause is the thing he was arguing against. Neither text observed a plumb line; both argued from what could not be detected in 1881 and 1885. The claim is not merely unsupported by the modern measurement &mdash; it is the quantity the modern measurement reports, with a value, at every benchmark.</p>""",

    advocate=dict(
        best_defense=(
            "Four moves. First, you changed the subject and then took a bow. Carpenter's "
            "claim was about walls of buildings and houses across a street; you have "
            "answered it with a 1,298-metre suspension bridge. You even concede in your "
            "opening paragraph that at his scale he was right. So on the actual claim, "
            "as its author stated it, you agree with him and have padded the disagreement "
            "out with structures nobody in 1885 could have pointed at. "
            "Second, and this is von Gumpach's point which you have restated for him "
            "rather than answered: you admit the British arcs came out prolate. Your "
            "rescue was to say the plumb lines are pulled sideways by mountains. When "
            "that rescue was computed it came out three times too big, so a second rescue "
            "was invented - invisible light material buried under the mountains, "
            "conveniently of exactly the amount required. You present a failed prediction "
            "followed by an unfalsifiable patch as though it were a triumph. In any other "
            "section of this website you would call that saving the appearances. "
            "Third, your latitude argument assumes the stars are effectively at infinity, "
            "which is the thing in dispute, and then you helpfully construct our model for "
            "us and refute the version you built. A near sky whose light is refracted "
            "through a dense atmosphere does not obey your clean cotangent. "
            "Fourth: plumb lines have in fact been hung, side by side, down 4,250 feet of "
            "mine shaft at Tamarack, and they came out farther apart at the bottom. Not "
            "converging. Diverging. The one time anybody actually performed the "
            "experiment your entire argument is about, it went the other way, and the "
            "profession's answer was a draught."),
        survives=4,
        preemptive=(
            "Four, and it is driven by the second and fourth moves. The first move is "
            "already answered in the body and the answer must not be softened into a "
            "boast: the concession that Carpenter was right at his scale stays in the "
            "first paragraph, in our voice, because the entry's whole argument is about "
            "scale and an editor who deletes it as throat-clearing turns the strongest "
            "section into the weakest. But add nothing to it either - the item on the "
            "list is 'plumb lines perpendicular WORLDWIDE', and worldwide is where the "
            "bridges live. That is the compression finding, and it is why answering at "
            "bridge scale is answering the claim in circulation. "
            "On the second move, the Pratt paragraph is load-bearing and must keep its "
            "exact shape: a forward computation from visible mass, published before the "
            "comparison, overshooting the observation by 3x. That is a failed prediction, "
            "and isostasy is not unfalsifiable - it predicts low-density crustal roots "
            "under mountains, which seismology later imaged independently. Keep the "
            "sentence saying so. Then let the load rest where it does not depend on any "
            "of this history at all: the NGS camera measuring the plumb direction against "
            "the star field to 0.1 arcsecond, and three unrelated instruments agreeing. "
            "On the third move, concede the premise and note that the entry does not need "
            "it: horn 1 and horn 2 between them exhaust the options, and horn 2 is built "
            "from Rowbotham's own perspective account of Polaris six pages earlier in the "
            "same chapter, not from a model we invented for him. Cite the section by name "
            "so a reader can check. Do not add a refraction rebuttal here; that belongs "
            "to ARG-B07 and importing it weakens both. "
            "On the fourth move, answer with arithmetic and without sneering, because the "
            "Tamarack measurements were careful and honestly reported. Fifteen feet of "
            "separation over 4,250 feet of depth predicts a convergence of 0.0031 ft, "
            "about 0.9 mm. McNair's results across three shafts ran from -0.028 to +0.141 "
            "ft with a measurement error under 0.003 ft. The expected signal is a tenth "
            "of his smallest number and a fortieth of his largest: the experiment could "
            "not have detected it in either direction, which is a statement about the "
            "apparatus and not about the men. That paragraph should be added to the body "
            "if this argument is ever attacked in public, and it is written out in the "
            "docstring above so nobody has to re-derive it."),
    ),

    straw_man=dict(
        identified=True,
        detail=("The von Gumpach extract Rowbotham prints at pp. 243-244 of the third edition "
                "says that astronomy assumes the plumb line is normal to the local horizon "
                "“without any proof or reason whatever” and that the assumption is "
                "“unsupported by even the shadow of a reason”. That misdescribes what "
                "geodesy does with the two directions. The direction a plumb bob actually hangs "
                "is observed, not assumed - it is what an astronomical latitude and longitude "
                "are - and the ellipsoid normal is a computed reference. The difference between "
                "them is not a fudge inserted to reconcile the two; it is a published, mapped, "
                "separately measured quantity called the deflection of the vertical, and the "
                "1911 Encyclopaedia Britannica prints station-by-station values for the very "
                "English survey Rowbotham is arguing from. "
                "The straw man is confined to that half. Carpenter's proof 72 does the opposite: "
                "his statement of the globe's prediction - that vertical walls are nowhere "
                "parallel, and that houses on opposite sides of a street are not strictly so - "
                "is accurate, and he neither exaggerates it nor invents a claim to knock down. "
                "He states it correctly and then denies it is observable. At his scale, with his "
                "instruments, that denial was true.")),

    compression=dict(
        assessed=True, drifted=True,
        list_phrasing="Plumb lines perpendicular worldwide.",
        source_wording=("“If, however, the celestial surface is not concave, but horizontal, two "
                        "plumb-lines suspended north and south of each other would be parallel, "
                        "and would indicate equal length in all the degrees of latitude … The "
                        "differences required by a globe are not found in practice, but such as "
                        "a plane would produce are invariably found.”"),
        drift_type="scope_widened",
        note=("The source&rsquo;s claim is about <em>two</em> plumb lines, <em>north and south of "
              "each other</em>, inferred from one printed table of British meridian arcs running "
              "between Dunnose on the Isle of Wight and Clifton in Yorkshire. The item says "
              "<em>worldwide</em>. That is the drift, and it is not cosmetic: within a single "
              "British survey the predicted lean between stations is a matter of arcseconds and "
              "is swamped by exactly the local effects that produced Rowbotham&rsquo;s anomaly in "
              "the first place, whereas &ldquo;worldwide&rdquo; is the scale at which two verticals "
              "differ by up to 180&deg; and at which bridge towers are built non-parallel on "
              "purpose. The list restates the claim at the one scale where it is most easily "
              "checked, and it fails there.<br><br>"
              "<strong>Two more things travel with the argument and neither survives into the "
              "items.</strong> <em>The condition:</em> the sentence is the consequent of &ldquo;if "
              "the celestial surface is not concave, but horizontal&rdquo; &mdash; a premise about "
              "the sky, which the item does not carry and which, taken either way, defeats the "
              "conclusion it was introduced to support. <em>The evidence:</em> Rowbotham is not "
              "reporting an observation of plumb lines but an inference from degree lengths he "
              "quotes from Hugh Murray&rsquo;s <em>Encyclopaedia of Geography</em>, including "
              "Murray&rsquo;s own admission that the disagreement between arcs could not be "
              "satisfactorily explained. The item presents as a fact about plumb lines what the "
              "source presents as a deduction from a surveying discrepancy. That second gap is a "
              "kind the seven-value list has no exact slot for &mdash; an inference republished as "
              "an observation &mdash; and <code>scope_widened</code> is recorded because it is the "
              "plainest and most checkable of the three, with both texts side by side above.<br><br>"
              "<strong>Items 396 and 397 drift the same way from a different author.</strong> "
              "Carpenter&rsquo;s proof 72 is scoped to walls of buildings and to houses across a "
              "street, where the effect is 0.65 arcseconds and his claim that it was not to be "
              "found by observation held for the instruments and the building practice of 1885. &ldquo;Architecture plumb/level universal&rdquo; and "
              "&ldquo;Skyscraper vertical stable&rdquo; keep his conclusion and drop the scale it "
              "depended on. There is a second, quieter slippage in the item wording itself: "
              "Carpenter&rsquo;s &ldquo;perpendicular walls&rdquo; means walls that are each plumb "
              "at their own site, which is true on a globe; the item&rsquo;s "
              "&ldquo;perpendicular&hellip;worldwide&rdquo; is read as all of them being parallel "
              "to one another, which is not. The one word carries both claims and only the second "
              "is at issue.<br><br>"
              "<strong>The refutation answers the sources, not the fragments:</strong> it concedes "
              "Carpenter&rsquo;s observation at Carpenter&rsquo;s scale in its own voice, quotes "
              "Rowbotham through to his flat conclusion rather than stopping at his conditional, "
              "and puts the weight on his own inference &mdash; that a table of latitude "
              "differences cannot exist if the local vertical does not vary, and that the "
              "discrepancy in the table is the size a few arcseconds of plumb-line deflection "
              "produces.")),

    verdict_challenge=dict(challenged=False, proposed_verdict=None, reasoning=None),

    people=["PER-ROWBOTHAM", "PER-CARPENTER"],
    related=["B02", "B04", "B05", "B06", "B08", "A03", "A10", "R08"],

    sources=[
        dict(label="Rowbotham (as “Parallax”), Zetetic Astronomy: Earth Not a Globe, 3rd ed. 1881, "
                   "ch. XIV, “Arcs of the Meridian”, printed pp. 245–246 — the plumb-lines passage, "
                   "the von Gumpach extract, and the Ordnance Survey degree table quoted from Hugh "
                   "Murray’s Encyclopaedia of Geography",
             url="https://sacred-texts.com/earth/za/za40.htm"),
        dict(label="Rowbotham, Zetetic Astronomy: Earth Not a Globe! (1865 first book edition), "
                   "Project Gutenberg #69892 — searched for plumb, perpendicular, wall, building, "
                   "spire, tower: the three occurrences of “plumb” are the Encyclopædia Britannica "
                   "“Levelling” extract, the air-gun and the Plymouth Hoe mirror, all instrumental",
             url="https://www.gutenberg.org/ebooks/69892"),
        dict(label="Rowbotham 1881, 3rd edition — archive.org scan (item "
                   "zeteticastronomy-earthnotaglobe, file ZeteticAstronomy-EarthNotaGlobe-3e-format2), "
                   "a reformatted PDF that paginates the same section at about pp. 186–189 and "
                   "carries the “Declination of the Pole Star” perspective argument",
             url="https://archive.org/download/zeteticastronomy-earthnotaglobe/ZeteticAstronomy-EarthNotaGlobe-3e-format2_djvu.txt"),
        dict(label="Carpenter, One Hundred Proofs that the Earth Is Not a Globe (Baltimore, 1885), "
                   "proof 72, indexed “Walls not parallel!” — the buildings-and-streets form of the "
                   "argument, and the only located ancestor of items 396 and 397",
             url="https://www.gutenberg.org/ebooks/55387"),
        dict(label="Metropolitan Transportation Authority, Verrazzano-Narrows Bridge — the operator’s "
                   "own description: towers “1 5/8 inches farther apart at their tops than at their "
                   "bases because the 4,260 foot distance between them made it necessary to "
                   "compensate for the earth’s curvature”",
             url="https://www.mta.info/agency/bridges-and-tunnels/verrazzano-narrows-bridge"),
        dict(label="Verrazzano–Narrows Bridge — “The towers are not parallel to each other, but are "
                   "1+5⁄8 in (41.275 mm) farther apart at their tops than at their bases”; towers "
                   "693 ft (211 m), main span 4,260 ft (1,298 m)",
             url="https://en.wikipedia.org/wiki/Verrazzano%E2%80%93Narrows_Bridge"),
        dict(label="Humber Bridge — “The towers, although vertical, are 1.4 inches (36 mm) farther "
                   "apart at the top than the bottom due to the curvature of the Earth”; towers "
                   "155.5 m, main span 1,410 m",
             url="https://en.wikipedia.org/wiki/Humber_Bridge"),
        dict(label="LIGO Caltech, “Facts” — “Over the 4km length of each arm, the Earth curves away "
                   "by nearly a meter!”, and the precision levelling of the beam-tube slab so the "
                   "beam “strikes the test mass/mirror at the end of each arm, and not a meter above it”",
             url="https://www.ligo.caltech.edu/page/facts"),
        dict(label="NOAA National Geodetic Survey, Deflection of the Vertical Survey — a camera "
                   "aligned to the local plumb line compared against the star field, “an accuracy of "
                   "0.1 arc-seconds”, deflections reaching “many 10s of arc-seconds”, and “the slope "
                   "is determined solely by the camera system”",
             url="https://geodesy.noaa.gov/GEOID/GSVS/deflection-vertical.shtml"),
        dict(label="1911 Encyclopædia Britannica, “Earth, Figure of the” — the English survey’s own "
                   "station deflections (sixteen stations; four exceed 4″) and “The non-recognition "
                   "of this circumstance often led to much perplexity in the early history of geodesy”",
             url="https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Earth,_Figure_of_the"),
        dict(label="Watts, Isostasy and Flexure of the Lithosphere, ch. 1 (history) — Everest’s "
                   "Kaliana–Kalianpur discrepancy of 5.24″, Pratt’s forward computation of 15.885″ "
                   "from the Himalaya (read 7 Dec 1854, published 1855), and Airy’s three-page 1855 "
                   "reply proposing compensation at depth",
             url="https://geofaculty.uwyo.edu/dueker/GeophysicsClass/watt%20isostasy%20flexure%20chap-1%20HISTORY.pdf"),
        dict(label="Barzaghi et al., “A Comparative Study of the Applied Methods for Estimating "
                   "Deflection of the Vertical in Terrestrial Geodetic Measurements”, Sensors 16(4):565 "
                   "(2016) — astro-geodetic camera, GNSS-plus-levelling and a gravimetric geoid "
                   "compared at the same sites",
             url="https://www.mdpi.com/1424-8220/16/4/565"),
        dict(label="Vertical deflection — magnitudes (“less than 10 arc-seconds in flat areas or up "
                   "to 1 arc-minute in mountainous terrain”, up to 100″ in the Himalaya) and "
                   "observational accuracies of ±0.2″",
             url="https://en.wikipedia.org/wiki/Vertical_deflection"),
        dict(label="Simanek, “The Tamarack Mines Mystery” — the 1901–02 Calumet plumb-line "
                   "measurements, McNair’s repeat across three shafts (Science XV, 20 June 1902), "
                   "results from −0.028 to +0.141 ft with error under 0.003 ft, and the convection "
                   "explanation",
             url="https://dsimanek.vialattea.net/hollow/tamarack.htm"),
    ]),
}
