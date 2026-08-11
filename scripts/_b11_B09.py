# -*- coding: utf-8 -*-
"""Batch 11 — B09. "Plumb lines are perpendicular everywhere."

Three items: 48 "Plumb lines perpendicular worldwide.", 396 "Architecture
plumb/level universal.", 397 "Skyscraper vertical stable." Lane B, verdict
REFUTED, kept. Research notes for whoever picks this up next, ordered by how much
they change the entry.

0. THERE IS ALREADY AN UNWIRED TREATMENT OF B09 ON DISK. `scripts/_b10_B09.py`
   exists, is untracked, and is not imported by `deep.py` (which stops at batch 9).
   This file was written independently and every quotation, page reference and
   number below was re-derived from the primary texts here on 2026-08-10/11 rather
   than carried over. Where the two agree they agree because the sources say so.
   IMPORTANT FOR WHOEVER WIRES BATCH 11: `deep.py` asserts `_k not in DEEP` on every
   batch import, so importing both files raises "collision: B09". One of them has to
   be dropped or merged. Reported in record_problems; not resolved here, this agent
   owns one file.

1. THE RECORD'S ORIGINATOR/YEAR IS A HYPOTHESIS AND HALF OF IT DID NOT SURVIVE.
   `clusters.py` B09 reads originator="Samuel Rowbotham", originator_work="Earth Not
   a Globe", year="1865". Two problems, both checked here.

   (a) THE EDITION. The plumb-lines sentence is in the THIRD edition (1881). It is
       not located in the 1865 first book edition: Project Gutenberg #69892 (the
       Simpkin, Marshall & Co. 1865 text) was searched here for plumb, perpendicular,
       wall, building, spire, tower and parallel. "plumb" occurs exactly three times
       and all three are instrumental — the Encyclopaedia Britannica "Levelling"
       extract defining the level as a line crossing the plumb-line at right angles
       (line 237 of that transcription); an air-gun "carefully adjusted by a
       plumb-line" (1461); a mirror at Plymouth Hoe "fixed, by the aid of a
       plumb-line, in a true vertical position" (3487).
       WHAT MAKES THIS SHARPER THAN THE USUAL EDITION TRAP: the 1865 text DOES carry
       the whole arcs-of-the-meridian apparatus — the Ordnance Survey narrative, the
       Hugh Murray degree table with all eight rows identical to 1881, and the
       "oblong instead of an oblate spheroid" quotation. What 1865 concludes from it
       is only that the measurements are unsatisfactory and that "whether oblate or
       oblong, or truly spherical, are questions logically misplaced." The von
       Gumpach extract and the plumb-lines-are-parallel INFERENCE are 1881 additions.
       So the cluster's year is not merely off by an edition; it is dated to a text in
       which the argument has not yet been made. Same trap logged for A05, B01, B04,
       B06; A10 already carries year="1881" for Rowbotham in the same file, so the
       field is internally inconsistent too.

   (b) THE OTHER TWO ITEMS ARE NOT ROWBOTHAM'S AT ALL. Items 396 and 397 are the
       buildings form, and that is Carpenter 1885, One Hundred Proofs, proof 72,
       indexed by its author as "Walls not parallel!" (index line 144, text lines
       1167-1173 of Gutenberg #55387). Neither Rowbotham edition carries it: both
       were searched here for walls, houses, spire, building and skyscraper, and the
       hits are an amphitheatre simile, the Antarctic ice walls, sea walls in a
       visibility passage, and the church spire in the perspective argument. So
       PER-CARPENTER belongs in people[] and the cluster credits one author for a
       two-author cluster.

   Origination is NOT established for either half. Both are the earliest texts
   located that carry the respective forms; the gloss claims ancestry and nothing
   more, and no originator is invented. Reported in record_problems.

2. NEITHER SOURCE HUNG A PLUMB LINE. This is the single most important fact about
   the cluster. Rowbotham's claim is an INFERENCE from a printed table of British
   meridian-arc degree lengths quoted from Hugh Murray's Encyclopaedia of Geography.
   Carpenter's claim is that no observation had found the predicted non-parallelism.
   Answer the inference and the evidential claim; do not answer a measurement they
   never made.

3. DO NOT STOP AT THE CONDITIONAL — this is the hedge rule applied against us.
   Rowbotham's sentence opens "If, however, the celestial surface is not concave, but
   horizontal ...", and it would be convenient to present the argument as a
   hypothetical nobody asserted. The next two sentences state the conclusion flat:
   "The differences required by a globe are not found in practice, but such as a
   plane would produce are invariably found. Hence the failure of geodesy becomes
   evidence against rotundity ... and therefore of mathematical and logical necessity
   A plane." Quote through to there. He is not hedging.

4. THE CENTREPIECE, AND IT IS INTERNAL TO THE SOURCE. A plane with a parallel sky
   predicts degrees of latitude EXACTLY EQUAL. The table Rowbotham prints two
   paragraphs earlier runs 60,766 to 60,890 fathoms. Recomputed here 2026-08-11
   (1 fathom = 1.8288 m):
     spread 124 fathoms = 226.8 m = 0.204% — not zero, and systematically ordered.
     the eight rows convert to 111.129-111.356 km.
     modern ellipsoid (WGS84) over the printed midpoint latitudes 51.048-52.842:
       111.249-111.283 km, i.e. the flattening signal across that band is 34 m.
   So: the plane predicts 0 m of variation, the ellipsoid predicts 34 m, the table
   shows 227 m in the wrong direction. BOTH predictions are swamped, which is exactly
   why the British arcs could not settle the figure of the Earth, and it is why the
   sentence "such as a plane would produce are invariably found" is false against the
   page it stands on.
   MAGNITUDE OF THE STATION ERROR NEEDED, and say plainly that this is a magnitude
   argument and not a published reanalysis of that table:
     Dunnose & Greenwich, 60,884 fathoms = 111.345 km vs 111.249 modern = +0.086%.
     The printed midpoint 51 deg 02' 54.2" is the exact mean of Dunnose (50 deg 37')
     and Greenwich (51 deg 28' 40"), which confirms the row is what it says it is, and
     makes the arc 0.86 deg = 3,107". 0.086% of that is 2.7 arcsec.
     The extreme row (Arbury Hill & Clifton, -154 m against the modern value) needs
     of order 4-5 arcsec.
   1911 Encyclopaedia Britannica, "Earth, Figure of the", on the English survey
   itself: "At sixteen astronomical stations in the English survey the disturbance of
   latitude due to the form of the ground has been computed ... At six stations the
   deflection is under 2", at six others it is between 2" and 4", and at four stations
   it exceeds 4"," plus "The non-recognition of this circumstance often led to much
   perplexity in the early history of geodesy." Verified here against wikisource.
   CAUTION: do not derive station latitudes from the table's midpoints wholesale. Two
   rows imply Arbury Hill at 52.56 deg and two imply 52.22 deg; the table is
   internally inconsistent by about a third of a degree on that one station. Nothing
   here rests on it, and the entry uses only the Dunnose/Greenwich row, which checks.

5. THE TWO-HORN ARGUMENT AGAINST ROWBOTHAM'S OWN SKY. Derived, so check before
   reusing. His premise is that the celestial surface is horizontal, i.e. parallel to
   the plane of the earth.
   HORN 1: if the sky is far enough that its rays arrive parallel, a plumb line and a
   star subtend the same angle everywhere, latitude is not a measurable quantity, and
   the table he is arguing from cannot exist.
   HORN 2: if the sky is at finite height h — his actual position, stated earlier in
   the same edition under DECLINATION OF THE POLE STAR (printed p. 180 of the
   archive.org transcription, against pp. 186-189 for the arcs section), where Polaris
   sinking towards the equator is "an ordinary effect of perspective" like a row of
   lamp-posts — then a station seeing Polaris at altitude alpha stands at ground
   distance h*cot(alpha), and one degree of "latitude" occupies h/sin^2(alpha) per
   radian: 0.0289h per degree at alpha = 51 deg, 0.5789h at alpha = 10 deg. TWENTY
   TIMES LONGER near the equator and lengthening the wrong way. Measured: 110.574 km
   at the equator to 111.694 km at the pole, about 1%, in the other direction.

6. THE DEFENCE TO BEAT IS VON GUMPACH'S CIRCULARITY CHARGE, printed by Rowbotham at
   pp. 187-188 of that transcription: astronomy "gives to the plumb-lines such
   imaginary directions as are needed in order to adopt the empirical results of
   geodetic measurements to the earth's imagined form", and the claim that the plumb
   line is normal to the horizon is "a mere assumption, unsupported by even the shadow
   of a reason." Three answers, in ascending order of force:
   (a) The mass-attraction explanation made a forward prediction and OVERSHOT.
       Everest's Great Trigonometrical Survey: Kaliana-Kalianpur latitude difference
       5.24" smaller geodetically than astronomically. Pratt computed the Himalaya's
       attraction (read 7 Dec 1854, published 1855) and got 15.885" — more than three
       times the observation. A quantity invented to absorb discrepancies does not
       overshoot by 3x. Airy's 1855 reply proposed light crust substituted for heavy
       material at depth: the origin of isostasy. Source: Watts, "Isostasy and Flexure
       of the Lithosphere", ch. 1, verified here.
   (b) The deflection is now MEASURED with no ellipsoid in the loop. NOAA NGS
       deflection-of-the-vertical survey: "a camera is placed on each GSVS bench mark
       and very precisely leveled to the local plumb line", star field compared
       against GNSS-derived position and time, "an accuracy of 0.1 arc-seconds",
       values "can approach many 10s of arc-seconds", and "the slope is determined
       solely by the camera system". Verified here.
   (c) Three unrelated instruments agree. Barzaghi et al., Sensors 16(4):565 (2016):
       astro-geodetic (QDaedalus) vs GNSS-plus-levelling "well within the 1 arcsec
       level", gravimetric geoid (ITALGEO2005) at 2.5 arcsec. Verified here.

7. THE ANSWER TO 396/397 THAT LANDS IN THEIR OWN IDIOM, and it is better than jumping
   straight to bridges. The professions the items invoke publish a national grid of
   the exact quantity the items say is not there. NGS DEFLEC18 "represents the
   deflections of the vertical (DOV's) at the surface of the Earth", in Xi (meridian)
   and Eta (prime vertical) components, "typically a few arc seconds, but can reach an
   arc minute of departure", and it exists for "the conversion between astronomic and
   ellipsoidal azimuths (the Laplace correction)". Verified here. A surveyor
   converting an astronomic azimuth to a geodetic one is applying the non-parallelism
   of plumb lines as a named, tabulated correction.

8. THE ARITHMETIC, ALL RECOMPUTED HERE 2026-08-11, R = 6,371 km.
   Convergence of two plumb lines d apart = d/R radians:
     20 m (a street)        3.14e-6 rad = 0.65"
     100 m (a city block)   1.57e-5 rad = 3.24"
     1,298 m (Verrazzano)   2.04e-4 rad = 42.0"
     1,410 m (Humber)       2.21e-4 rad = 45.7"
   Tower-top spread = d*h/R:
     Verrazzano 1,298 x 211 / R = 43.0 mm. Published 1 5/8 in = 41.275 mm. ~4%.
     Humber 1,410 x 155.5 / R = 34.4 mm. Published 36 mm. ~5%.
   Do NOT claim an exact reproduction; the residue is the local radius of curvature
   and where the tower base is reckoned from.
   LIGO: sagitta of a 4 km chord = 4000^2/(2R) = 1.256 m; LIGO's own page says "nearly
   a meter". Quote theirs, give ours as the sagitta, do not manufacture a discrepancy
   out of a rounding. The 4 km arm subtends 129.5" = 2.16 arcmin of vertical rotation.
   Ellipsoid normal vs geocentric radius: (1-e^2)tan(phi_gc) relation gives a maximum
   separation of 11.55 arcmin (693") at latitude 45. Useful twice: it is 1,000x
   anything Carpenter could see, and it is the precise sense in which von Gumpach is
   right that the plumb line is not a radius.
   Latitude: 1 degree = 111.19 km mean; the international nautical mile is 1,852 m
   EXACTLY by definition (1929) and was adopted because that is about one minute of
   latitude — do not write that it "is" one minute, the modern definition is a fixed
   metric value.

9. TAMARACK, because a well-read defender will raise it and it is the only real
   plumb-line experiment on offer. Calumet, Michigan: J. B. Watson, chief engineer at
   the Tamarack mine, hung 4,250 ft wires 15-16 ft apart down the shafts in 1901 and
   found them FARTHER APART at the bottom. F. W. McNair (Michigan College of Mines)
   repeated it in January-February 1902 across several shafts with different wire and
   bob materials; results ran from 0.028 ft convergence to 0.141 ft divergence, with
   "an error not greater than 0.003 feet", and he attributed the spread to up-and-down
   air currents in the shafts, testing that by blocking the currents and moving the
   wires. Our arithmetic: expected geometric convergence = 15 x 4250 / 20,902,231 ft =
   0.0031 ft, about 0.9 mm — a tenth of the smallest number in his range and a
   fortieth of the largest. The experiment could not have detected the effect either
   way. Say that; do not say the anomaly was faked. Source: Simanek, verified here.

10. VERDICT. REFUTED kept, and the alternatives were weighed rather than waved at.
    SELF-CONTRADICTED has a real case here — stronger than the batch-10 file allows,
    because the contradiction is not derived by us: Rowbotham prints a table of
    UNEQUAL degrees and, on the same page, says the equality a plane would produce is
    "invariably found". That is the B05 shape (he reprints the correction he then
    denies). It was not taken for two reasons. First, the verdict covers three items
    and two of them are Carpenter's, whose text contains no such contradiction —
    SELF-CONTRADICTED would be published against a cluster two thirds of which does
    not carry the self-contradiction. Second, the plain situation is that a testable
    claim was made and direct measurement came back against it: bridge towers built
    non-parallel by design, and the local vertical now measured against the star field
    to 0.1 arcsecond. REFUTED says that; SELF-CONTRADICTED would say less. The
    internal contradiction is therefore published inside the refutation, where it
    belongs, and no verdict_challenge is filed. MISLEADING was also weighed for 396/397
    alone, which taken narrowly are the convenience-frame move of R08 rather than a
    false claim; one verdict covers three items and the false one dominates.

11. WHAT CARPENTER GETS RIGHT, AND IT DECIDES THE STRAW-MAN FIELD. His statement of
    the globe's prediction is ACCURATE — vertical walls are nowhere exactly parallel,
    and houses across a street are not strictly so. He does not caricature the
    position; he states it correctly and then denies that it is observable, and at his
    scale, in 1885, he was right: 0.65 arcsec across a street. Credit that. The straw
    man in this cluster is in the Rowbotham/von Gumpach half only.

12. NOT LOCATED ELSEWHERE, each search scoped, all run here:
    - Dubay, 200 Proofs (archive.org item 200ProofsEarthIsNotASpinningBall_201710,
      djvu text) searched for plumb, architect, skyscraper, building: proof 7 is the
      "surveyors, engineers and architects are never required to factor the supposed
      curvature" claim, which is B05/B06 territory, and the Chicago-skyline passage
      uses the non-parallelism the OTHER way round ("the buildings would be leaning
      away from our view point"), which is B04/B07 territory. The plumb/level claim is
      not located in that text.
    - Winship, Zetetic Cosmogony (item zeteticcosmogony00wins): one hit on
      "perpendicular", in a radio-transmission aside.
    - Scott, Terra Firma (item cu31924031764594): "plumb line" occurs once, inside a
      quotation of Rowbotham on measuring the Sun's height by plane trigonometry.
    Those are reports on the texts searched, not claims about the corpora.

13. THE SPECIMEN'S OWN NEIGHBOURHOOD, checked against the live page 2026-08-10.
    Items 396-397 do not sit among Victorian material. They sit inside a run of
    modern engineering-vocabulary one-liners — "Leveling equipotential planes.",
    "Hydrology planar.", "Photogrammetry planar.", "Mining surveys flat.",
    "Architecture plumb/level universal.", "Skyscraper vertical stable.", "Pendulum
    clocks stable.", "GNSS pseudorange Earth clocks." — none of which carries a
    citation, and several of which use a technical term against itself ("equipotential"
    names a curved surface). That is context for the compression finding: the
    Carpenter claim has been restated in a vocabulary Carpenter did not have, in a
    block that reads as generated rather than quoted.

14. QUOTE PROVENANCE. Rowbotham 1881 is quoted from the archive.org OCR at item
    zeteticastronomy-earthnotaglobe, file ZeteticAstronomy-EarthNotaGlobe-3e-format2,
    a REFORMATTED PDF whose own page numbers put the arcs section at 186-189. That is
    the pagination the locator cites and it is not the printed pagination of the 1881
    Day edition; sacred-texts (za40.htm) was unreachable from here on 2026-08-10 (a
    Cloudflare interstitial, not a 404), so its page numbers are not asserted. Do not
    merge two page ranges. That OCR reads "spewing" where the word is plainly
    "shewing"; the quote below prints "shewing" and the gloss records the slip. No
    print copy was consulted. Carpenter is quoted from Gutenberg #55387, which
    reproduces the Baltimore 1885 printing.
"""

ENTRY = {

"B09": dict(

    tldr=("Rowbotham's plumb-line sentence is an 1881 addition — the 1865 book prints the same "
          "survey table without it — and neither passage reports hanging a plumb line: one argues "
          "from a table of survey arcs, the other from what the instruments of 1885 could not find. "
          "Two verticals do converge — by 0.65 of an arcsecond across a twenty-metre street, "
          "which is why a Victorian bricklayer saw nothing, and by 42 arcseconds across the "
          "Verrazzano-Narrows, whose operator says its towers were built 1 5/8 inches farther "
          "apart at the top to compensate for the curvature. The table Rowbotham prints does not "
          "show the equal degrees his own conclusion requires, and the surveying profession the "
          "other two items appeal to publishes a national grid of the non-parallelism and applies "
          "it under the name of the Laplace correction."),

    passage=dict(
        work="WRK-ROWBOTHAM-1865",
        pd=True,
        locator=("3rd ed., rev. and enl. (London: Day, 1881), ch. XIV, section “Arcs of the "
                 "Meridian”, at printed pp. 188–189 of the archive.org transcription (item "
                 "zeteticastronomy-earthnotaglobe, file ZeteticAstronomy-EarthNotaGlobe-3e-format2), "
                 "a reformatted PDF whose pagination is its own. NOT the 1865 first book edition — "
                 "see the gloss. No print copy was consulted, and the printed pagination of the "
                 "1881 Day edition is not asserted here"),
        quote=("The fallacy involved in all the attempts to prove the oblate spheroidal form of "
               "the earth, is, that the earth is first assumed to be a globe, the celestial "
               "surface above it to be concave, and the plumb-lines to be radii. If this were the "
               "true condition of things, then all the degrees of latitude would be the same in "
               "length; and if the earth were really “flattened at the poles,” the degrees would "
               "certainly shorten in going from the equator towards the north. If, however, the "
               "celestial surface is not concave, but horizontal, two plumb-lines suspended north "
               "and south of each other would be parallel, and would indicate equal length in all "
               "the degrees of latitude, thereby shewing the earth to be parallel with the "
               "celestial surface, and therefore a plane. The differences required by a globe are "
               "not found in practice, but such as a plane would produce are invariably found. "
               "Hence the failure of geodesy becomes evidence against rotundity, but demonstrating "
               "that the earth is parallel to the horizontal heavens, and therefore of "
               "mathematical and logical necessity A plane."),
        gloss="""<p><strong>Read to the end before deciding this is a hypothetical.</strong> The argument opens on a condition &mdash; <em>if</em> the celestial surface is horizontal &mdash; and it would suit this page to stop there and say the source asserted nothing. It does assert. The condition is followed immediately by a flat empirical claim (&ldquo;The differences required by a globe are not found in practice&rdquo;) and a flat conclusion (&ldquo;of mathematical and logical necessity A plane&rdquo;). Quoting up to the disjunction and stopping would be the same trimming this review objects to when it is done to us, so the passage is printed through to the conclusion.</p>
<p><strong>What he is arguing from is a table, not a plumb line.</strong> The section is about arcs of the meridian. It reproduces the British Ordnance Survey&rsquo;s degree lengths &mdash; Arbury Hill, Blenheim, Greenwich, Clifton, Dunnose &mdash; quoted from Hugh Murray&rsquo;s <em>Encyclopaedia of Geography</em>, with Murray&rsquo;s remark that the degrees &ldquo;appear to decrease, as if the earth were an oblong instead of an oblate spheroid&rdquo; and the survey&rsquo;s own admission that &ldquo;It has been found impossible to explain the want of agreement in a satisfactory way.&rdquo; The parallel plumb lines are an <em>inference</em> from that discrepancy. Neither this passage nor Carpenter&rsquo;s reports suspending a wire and measuring one, and the refutation is aimed at the inference and at the evidential claim, not at an observation they did not make.</p>
<p><strong>The edition matters, and it matters more than usual here.</strong> This passage is in the third edition of 1881. It is not located in the 1865 first book edition: the Project Gutenberg text of that edition (#69892) was searched for <em>plumb</em>, <em>perpendicular</em>, <em>wall</em>, <em>building</em>, <em>spire</em>, <em>tower</em> and <em>parallel</em>, and its three occurrences of &ldquo;plumb&rdquo; are all instrumental &mdash; the <em>Encyclop&aelig;dia Britannica</em> &ldquo;Levelling&rdquo; extract defining the level as a line crossing the plumb-line at right angles, an air-gun &ldquo;carefully adjusted by a plumb-line&rdquo;, and a mirror at Plymouth Hoe &ldquo;fixed, by the aid of a plumb-line, in a <em>true vertical position</em>&rdquo;. The 1865 book already carries the entire arcs apparatus, the same eight-row table and the &ldquo;oblong&rdquo; quotation; what it draws from them is only that the measurements are unsatisfactory and that &ldquo;whether oblate or oblong, or truly spherical, are questions logically misplaced.&rdquo; The von Gumpach extract and the plumb-lines-are-parallel inference arrive with the third edition. The claim is sixteen years younger than the first book edition of the work it appears in, and the difference is not a rewording: in 1865 the same evidence supports no conclusion at all.</p>
<p><strong>The other half of the cluster belongs to a different author and is a different claim.</strong> Items 396 and 397 &mdash; architecture and skyscrapers &mdash; match <em>One Hundred Proofs that the Earth Is Not a Globe</em> (Baltimore, 1885), proof 72, indexed by Carpenter himself as &ldquo;Walls not parallel!&rdquo;: <em>&ldquo;Astronomers tell us that, in consequence of the Earth&rsquo;s &lsquo;rotundity,&rsquo; the perpendicular walls of buildings are, nowhere, parallel, and that even the walls of houses on opposite sides of a street are not strictly so! But, since all observation fails to find any evidence of this want of parallelism which theory demands, the idea must be renounced as being absurd and in opposition to all well-known facts.&rdquo;</em> Note what that is: an accurate statement of the globe&rsquo;s prediction, followed by a claim about the state of the evidence in 1885. At his scale the evidence really was silent &mdash; across a twenty-metre street the two walls lean apart by 0.65 of an arcsecond. Neither Rowbotham edition carries this form; both were searched here for <em>walls</em>, <em>houses</em>, <em>building</em>, <em>spire</em> and <em>skyscraper</em>.</p>
<p><strong>What these passages are being cited as.</strong> The earliest texts located that carry the two halves of this cluster in the form the list uses. They are ancestors and that is the whole claim &mdash; no earlier flat-earth or geocentric text was traced that puts either argument first, and neither man is credited here with originating it.</p>"""),

    steelman=dict(
        description="""<p><strong>SURFACE (weak &mdash; do not use).</strong> &ldquo;Plumb lines obviously converge towards the centre, so this is trivially false.&rdquo; That walks straight into Carpenter&rsquo;s actual point. He never denied what the theory predicts; he wrote the prediction out correctly and then said nobody had <em>found</em> it. Across the width of a street the predicted lean is 0.65 arcsec &mdash; far below a mason&rsquo;s plumb bob, a builder&rsquo;s square or a Victorian spirit level. Replying &ldquo;but the theory says so&rdquo; to a man whose complaint is that the theory&rsquo;s prediction has never been seen is not an answer.</p>
<p><strong>DEEPER.</strong> The claim is non-discriminating as stated: <em>plumb</em> means along local gravity and <em>level</em> means perpendicular to it, so a builder working plumb and level has measured the direction of gravity at one site and nothing else. True, and it disposes of items 396 and 397 as <em>evidence</em> &mdash; but it does not touch Rowbotham, whose argument is not about definitions. His is an inference from published survey data, and the data really were discordant.</p>
<p><strong>KERNEL.</strong> Two genuinely true things sit under this cluster and both are worth stating at full strength. The first: <em>the British arc measurements came out wrong, and the standard reference work of the day said so in print.</em> The degrees decreased going north &mdash; the signature of a prolate figure, the opposite of polar flattening &mdash; and the survey account Rowbotham quotes concedes that the want of agreement could not be explained satisfactorily. He did not invent that; he found it in a geography encyclopaedia and quoted it accurately. The second is sharper: <em>the plumb line does not point at the centre of the Earth.</em> Even on a smooth rotating ellipsoid with no local mass anomalies at all, the local vertical misses the geocentre by up to 11.5 arcminutes &mdash; 693 arcseconds, a thousand times larger than anything Carpenter could have detected in a party wall. Rowbotham prints von Gumpach making the charge that follows from it: that astronomy &ldquo;gives to the plumb-lines such imaginary directions as are needed in order to adopt the empirical results of geodetic measurements to the earth&rsquo;s imagined form.&rdquo; The gap between the direction a plumb bob actually hangs and the direction a reference figure says it should is real, is not small, and has a whole sub-discipline attached to it.</p>""",
        why_it_doesnt_save_claim="""<p>Because both true things are the <em>same</em> thing, and that thing is the local vertical varying from place to place.</p>
<p>The arcs disagreed because the astronomical latitude of each station is read off a plumb line that the surrounding rock pulls sideways. The 1911 <em>Encyclop&aelig;dia Britannica</em> publishes the computation for the English survey Rowbotham is arguing from: sixteen stations, six deflections under 2&Prime;, six between 2&Prime; and 4&Prime;, four above 4&Prime;, and the remark that &ldquo;The non-recognition of this circumstance often led to much perplexity in the early history of geodesy.&rdquo; Rowbotham was reading the perplexity, in a book that told him it was unexplained.</p>
<p>So the quantity his argument runs on &mdash; a discrepancy between arcs &mdash; exists only because plumb lines are <em>not</em> parallel. Take the non-parallelism away and there is no station error, no disagreement between arcs, and nothing for the passage to be about. And von Gumpach&rsquo;s charge is a complaint that the vertical wanders from site to site, which is the proposition being denied. The strongest material in the cluster is a description of the effect its conclusion says does not occur.</p>"""),

    refutation="""<p><strong>The concession first, because the easy version of this rebuttal loses to it.</strong> At the scale Carpenter names, he was right that nothing was observable. Two plumb lines a distance <em>d</em> apart converge by <em>d</em>/<em>R</em> radians: across a twenty-metre street that is 3.1 &times; 10<sup>&minus;6</sup> rad, or <strong>0.65 arcseconds</strong>; across a hundred-metre city block, 3.2 arcseconds. No mason, spirit level or Victorian theodolite was going to find that in a party wall, and answering &ldquo;the theory predicts it&rdquo; to a man whose objection is that the prediction has never been seen concedes his point instead of meeting it. (Recomputed here 2026-08-11 with <em>R</em> = 6,371 km.)</p>

<p><strong>What the verdict ranges over.</strong> Not &ldquo;a plumb line hangs perpendicular to the local level surface&rdquo; &mdash; that is true, on a globe exactly as on a plane, and it is what a builder means by plumb. The cluster&rsquo;s claim is that the verticals at different places are parallel <em>to one another</em>, everywhere, and that this indicates a plane. That fails three ways: it fails against the table the source prints, it fails on the source&rsquo;s own account of the sky, and it fails against direct measurement of the quantity itself.</p>

<h4>1. The table on the page does not show what the sentence claims</h4>

<p>A plane under a parallel sky predicts something exact: every degree of latitude the same length. Rowbotham writes that &ldquo;the differences required by a globe are not found in practice, but such as a plane would produce are invariably found.&rdquo; Two paragraphs above it stands the table he is describing, eight British arcs from Murray&rsquo;s <em>Encyclopaedia of Geography</em>, running from <strong>60,766 to 60,890 fathoms</strong> &mdash; 111.129 to 111.356 km, a spread of 124 fathoms or <strong>227 metres</strong>. The prediction of a plane is zero. The figure on the page is 0.20%.</p>

<p>Nor does the globe fit those numbers, and saying so is the honest way to take the point. Over the band of midpoint latitudes the table covers, 51.05&deg; to 52.84&deg;, the modern ellipsoid predicts a variation of just <strong>34 metres</strong> &mdash; 54 m across the full spread of the stations themselves &mdash; and in the opposite direction to the trend Murray noticed. Row by row against modern values the table&rsquo;s errors run from &minus;154 m to +103 m, so the ellipsoid&rsquo;s residuals span 257 m where the plane&rsquo;s span 227 m: <strong>neither figure of the Earth fits, and the plane fits no better.</strong> That is the real state of the evidence Rowbotham had, and it has an unglamorous meaning: <em>a survey confined to under three degrees of British latitude could not resolve the flattening of the Earth at all,</em> because the signal it was looking for was several times smaller than its own station errors. Reading a plane out of that table is reading a result out of noise &mdash; and reading the specific result of <em>equal degrees</em> out of a table of unequal ones.</p>

<p>How large are the errors required? Take the row this page can check independently: Dunnose and Greenwich, 60,884 fathoms, 111.345 km against 111.249 km for that latitude today, an excess of 0.086%. The printed midpoint latitude, 51&deg;&nbsp;02&prime;&nbsp;54.2&Prime;, is the exact mean of Dunnose on the Isle of Wight and Greenwich, which confirms the row is the pair it says it is and makes the arc 0.86&deg;, or about 3,100 arcseconds. An 0.086% error over that arc is <strong>2.7 arcseconds of latitude</strong>. The extreme row of the table needs of order 4 to 5. Set that against the <em>Encyclop&aelig;dia Britannica</em>&rsquo;s computed deflections for those very stations &mdash; four of sixteen above 4&Prime;, six between 2&Prime; and 4&Prime; &mdash; and the anomaly is accounted for at the right size. This is a magnitude argument, offered as one: it is not a published reanalysis of Murray&rsquo;s table, and no such reanalysis was located in the searches run for this entry.</p>

<h4>2. The premise defeats the conclusion, on the source&rsquo;s own optics</h4>

<p>The sentence is conditional on a sky that is &ldquo;not concave, but horizontal&rdquo; &mdash; a celestial surface parallel to the plane. Take that seriously in either of the two forms available to it.</p>

<ul>
<li><strong>If the sky is far enough away that its rays arrive parallel</strong>, the angle between a plumb line and a star is the same at every station. Polaris stands at one altitude in London and the same in Ceylon, latitude is not a measurable quantity, there are no degrees of the meridian, and the table the argument is built on cannot exist.</li>
<li><strong>If the sky is at a finite height <em>h</em></strong> &mdash; which is Rowbotham&rsquo;s stated position, set out earlier in the same edition under &ldquo;Declination of the Pole Star&rdquo;, where Polaris sinking towards the equator is &ldquo;an ordinary effect of perspective&rdquo; like a receding row of lamp-posts &mdash; then a station seeing Polaris at altitude &alpha; stands at ground distance <em>h</em>&thinsp;cot&thinsp;&alpha;, and one degree of &ldquo;latitude&rdquo; occupies a ground length proportional to 1/sin<sup>2</sup>&alpha;: 0.029<em>h</em> at &alpha; = 51&deg;, 0.579<em>h</em> at &alpha; = 10&deg;. <strong>A degree near the equator would be twenty times longer than a degree in England.</strong> The measured degree runs from 110.574 km at the equator to 111.694 km at the pole &mdash; a variation of one per cent, and the other way about.</li>
</ul>

<p>So &ldquo;two plumb-lines suspended north and south of each other would be parallel, and would indicate equal length in all the degrees of latitude&rdquo; does not follow from either version of his own sky. On the first there are no degrees to compare; on the second they are grossly unequal in the direction his data most conspicuously does not show.</p>

<h4>3. The explanation of the scatter was not invented to save the ellipsoid</h4>

<p>Von Gumpach&rsquo;s objection, which Rowbotham prints at length, is the best thing in the cluster: astronomy assigns the plumb lines &ldquo;such imaginary directions as are needed in order to adopt the empirical results of geodetic measurements to the earth&rsquo;s imagined form.&rdquo; If deflection of the vertical were a free parameter fitted after the fact, he would be right and this section would be circular. It is not, and the history is specific.</p>

<p><strong>It was computed forward, and it failed.</strong> Everest&rsquo;s Great Trigonometrical Survey found the latitude difference between Kaliana and Kalianpur 5.24&Prime; smaller by triangulation than by astronomy. J. H. Pratt, in a paper read to the Royal Society on 7 December 1854 and published in 1855, calculated from the visible mass of the Himalaya what deflection it ought to produce and got <strong>15.885&Prime;</strong> &mdash; more than three times the observed value. A quantity invented to absorb a discrepancy does not overshoot it by a factor of three. What the overshoot forced was Airy&rsquo;s 1855 proposal that a mountain range is underlain by light crust substituted for heavy material, so that most of its attraction is cancelled from below: the origin of isostasy, which is now ordinary geophysics. (The same G. B. Airy as <a href="#ARG-A03">ARG-A03</a>, in the same year.)</p>

<h4>4. The vertical is now measured, and the professions in items 396 and 397 correct for it by name</h4>

<p>This is where the argument stops being historical. A deflection-of-the-vertical survey at the US National Geodetic Survey works like this: at night <em>&ldquo;a camera is placed on each GSVS bench mark and very precisely leveled to the local plumb line&rdquo;</em>, and the star field it records is compared with the star field expected at a position and time supplied by GNSS. Accuracy: <em>&ldquo;an accuracy of 0.1 arc-seconds&rdquo;</em>. Observed values: they <em>&ldquo;can approach many 10s of arc-seconds&rdquo;</em>. And the agency is explicit about which instrument does the work &mdash; the satellite fix gives position and time, but <em>&ldquo;the slope is determined solely by the camera system&rdquo;</em>. A plumb bob and the sky, twice, in two places.</p>

<p><strong>Now the part aimed directly at architecture and surveying.</strong> Items 396 and 397 appeal to what builders and surveyors do. What they do is apply this correction under its own name. NGS publishes DEFLEC18, which <em>&ldquo;represents the deflections of the vertical (DOV&rsquo;s) at the surface of the Earth&rdquo;</em> in north&ndash;south and east&ndash;west components, states that they are <em>&ldquo;typically a few arc seconds, but can reach an arc minute of departure&rdquo;</em>, and gives its purpose as <em>&ldquo;the conversion between astronomic and ellipsoidal azimuths (the Laplace correction)&rdquo;</em>. A surveyor turning an observed astronomic azimuth into a geodetic one is subtracting the non-parallelism of plumb lines from his own observation, off a national grid of it. The claim that the professions treat the vertical as universal is refuted by their tooling, not by anybody&rsquo;s cosmology.</p>

<p>And three unrelated instruments agree on the numbers. A 2016 comparison in <em>Sensors</em> ran an astro-geodetic zenith camera, GNSS heights differenced against spirit levelling, and a gravimetric geoid computed from measured gravity, at the same sites: the first two agree well within 1 arcsecond, the gravity-derived values sit about 2.5 arcseconds out. Starlight, a levelling staff and a gravimeter are three different physical measurements returning one tilt.</p>

<p>It is worth being precise about what needs no ellipsoid at all, because a defender will press the circularity charge here. The proposition under test is only that two verticals point in different directions. Two star cameras at two benchmarks settle that between them: each measures its own plumb line against the same sky, and the directions differ. Every reference figure, geoid model and ellipsoid normal in the paragraphs above is machinery for saying <em>how much</em> and <em>why</em> &mdash; none of it is required to establish <em>whether</em>.</p>

<h4>5. Where the effect is large enough to build for, it is on the drawings</h4>

<p>Go from a street to a strait. The Verrazzano-Narrows Bridge carries its towers 4,260 ft (1,298 m) apart and 693 ft (211 m) high; the two verticals there differ by 42 arcseconds, which over the tower height is 43 mm. The Metropolitan Transportation Authority, the bridge&rsquo;s owner and operator, says so on its own page: the towers are <em>&ldquo;1 5/8 inches farther apart at their tops than at their bases because the 4,260 foot distance between them made it necessary to compensate for the earth&rsquo;s curvature.&rdquo;</em> The Humber Bridge, 1,410 m between towers and 155.5 m high, is described the same way: <em>&ldquo;The towers, although vertical, are 1.4 inches (36 mm) farther apart at the top than the bottom due to the curvature of the Earth.&rdquo;</em> Our arithmetic gives 43.0 mm and 34.4 mm against the published 41.275 mm and 36 mm &mdash; agreement to within about five per cent, the residue being the local radius of curvature and where the tower base is reckoned from. These are dimensions on drawings, and two structures were built to them.</p>

<p>The same correction appears wherever a straight line is long. LIGO&rsquo;s own description of its construction: <em>&ldquo;Over the 4km length of each arm, the Earth curves away by nearly a meter!&rdquo;</em>, and the slab under the beam tube had to be precision-levelled so that the beam leaving the corner station in a straight line <em>&ldquo;strikes the test mass/mirror at the end of each arm, and not a meter above it.&rdquo;</em> The sagitta of a 4 km chord is 1.256 m, and the vertical rotates by 2.2 arcminutes along it.</p>

<h4>6. The one time the wires were actually hung</h4>

<p>They were, once, and honesty requires reporting it. At the Tamarack mine in Calumet, Michigan, in 1901, chief engineer J. B. Watson suspended 4,250-foot plumb lines 15 to 16 feet apart down the shafts and found them farther apart at the bottom &mdash; diverging, not converging. F. W. McNair of the Michigan College of Mines repeated the work in January and February 1902 across several shafts with different wires and bobs; his results ran from 0.028 ft of convergence to 0.141 ft of divergence, with an error he put at not more than 0.003 ft, and he attributed the spread to air currents in the shafts, testing that by blocking the currents and moving the wires.</p>

<p>The arithmetic settles what the experiment could show. Fifteen feet of separation over 4,250 feet of depth predicts a convergence of 15 &times; 4,250 / 20,902,231 ft = <strong>0.0031 ft</strong>, about 0.9 mm &mdash; one tenth of the smallest number in McNair&rsquo;s range and one fortieth of the largest. The apparatus could not have detected the predicted effect in either direction. That is a statement about the apparatus and not about the men, who reported their numbers and their doubts in <em>Science</em>; and it is why a mine shaft is not where this question gets settled, while a camera reading the star field to a tenth of an arcsecond is.</p>

<h4>7. What is left</h4>

<p>Carpenter&rsquo;s observation was true for his instruments and is false for ours: the non-parallelism he could not find is 41 millimetres of designed spread between two bridge towers and a tabulated correction in a surveyor&rsquo;s software. Rowbotham&rsquo;s anomaly was real, was flagged as unexplained by the book he took it from, and was caused by the very effect his conclusion denies &mdash; and the equal degrees his conclusion requires are not in the table he printed to prove them. Neither man measured a plumb line. The claim is not merely unsupported today; the quantity it says is not there is published as a grid in two components by a national geodetic agency, and measured directly, to a tenth of an arcsecond, by a camera aimed at the stars.</p>""",

    advocate=dict(
        best_defense=(
            "Four moves, in order of how much they should worry you. "
            "First, you have answered a claim about walls of houses with a suspension "
            "bridge, and you conceded in your own opening paragraph that at Carpenter's "
            "scale Carpenter was right. So on the proposition as its author stated it "
            "you agree with him, and the disagreement is padding made of structures "
            "nobody in 1885 could point at. "
            "Second, your section 4 is circular and the circularity is in the word "
            "'deflection'. A deflection is a departure FROM something, and the something "
            "is a reference ellipsoid — a shape assumed before the first measurement is "
            "taken. Your DEFLEC18 grid is derived from a geoid model which is itself fitted "
            "to an assumed figure of the Earth. You have found that when astronomers "
            "assume a globe, they need a correction table to make their observations fit "
            "it, and you have published the table as proof of the globe. That is von "
            "Gumpach's point, verbatim, and quoting the table back at him does not answer it. "
            "Third, your two horns are a model you built for us. A finite sky whose light "
            "crosses a dense and stratified atmosphere does not obey your clean cotangent, "
            "and you know it, because elsewhere on this site you spend paragraphs on how "
            "much refraction bends a sightline near the horizon — which is exactly where "
            "your twenty-times-longer degree is supposed to appear. "
            "Fourth, and this is the one you should not have raised yourself: the only "
            "time anyone actually hung the wires, at Tamarack, they came out diverging, "
            "and the profession's answer was a draught in the shaft. You have written the "
            "arithmetic showing the experiment was useless — fine. Then say plainly what "
            "follows: the direct experiment has never been done successfully, and every "
            "measurement you rely on is an inference from starlight, satellites and "
            "gravity models. You are not measuring plumb lines. You are computing them."),
        survives=4,
        preemptive=(
            "Four, driven by the second and fourth moves; the first and third are already "
            "answered in the body and the answers must not be softened. "
            "MOVE ONE. The concession that Carpenter was right at his scale stays in the "
            "first paragraph, in our voice — the entry's whole argument is about scale, and "
            "an editor who deletes it as throat-clearing turns the strongest section into "
            "the weakest. But add nothing to it either: the item in circulation says "
            "WORLDWIDE, and worldwide is where the bridges are. That is the compression "
            "finding and it is why answering at bridge scale answers the claim readers meet. "
            "MOVE TWO is the serious one and the body must keep its last paragraph of "
            "section 4 exactly where it is, adjacent to the DEFLEC18 material rather than "
            "in a footnote: the proposition under test is only that two verticals differ, "
            "two star cameras at two benchmarks settle it against the same sky, and every "
            "ellipsoid in the section is machinery for HOW MUCH, not WHETHER. If that "
            "paragraph ever migrates or is cut, this argument becomes genuinely circular "
            "and a well-read defender will say so first. Do not respond by removing the "
            "ellipsoid material — the Laplace-correction point is what lands items 396 "
            "and 397 — respond by keeping the non-circular claim next to it. "
            "MOVE THREE. Concede the premise and note that the entry does not need it: "
            "horn 1 and horn 2 exhaust the options, horn 2 is built from Rowbotham's own "
            "perspective account of Polaris in the same edition rather than from a model "
            "invented for him, and refraction of a few arcminutes near the horizon does not "
            "convert a factor of twenty into a factor of one. Do not import the refraction "
            "argument itself; that belongs to ARG-B07 and importing it weakens both. "
            "MOVE FOUR. Answer with arithmetic and without sneering — the Tamarack "
            "measurements were careful and honestly reported, and the entry already says "
            "so. Then refuse the last step, in the body if this is ever attacked in public: "
            "'inference from starlight' is what an astronomical latitude has always been, "
            "including every latitude in Rowbotham's own table, so a defender who "
            "disqualifies it disqualifies the evidence his own argument is made of. The "
            "star-camera measurement is a plumb bob and a photograph of the sky; calling "
            "that 'computing' a plumb line and a mine shaft with a draught in it "
            "'measuring' one inverts the two."),
    ),

    straw_man=dict(
        identified=True,
        detail=("The von Gumpach extract Rowbotham prints immediately before the plumb-lines "
                "sentence says that astronomy assumes the plumb line's direction “not only "
                "without any proof or reason whatever” and that the claim it is normal to the "
                "horizon is “a mere assumption, unsupported by even the shadow of a reason.” "
                "That misdescribes what geodesy does with the two directions. The direction a "
                "plumb bob hangs is observed, not assumed — it is what an astronomical latitude "
                "and longitude ARE, and it is what the star camera in section 4 records — while "
                "the ellipsoid normal is an admitted construction. The difference between them is "
                "not a fudge inserted to reconcile the two: it is separately measured, published "
                "as a grid, and applied under a name, and the 1911 Encyclopaedia Britannica "
                "prints station-by-station values for the very English survey Rowbotham is "
                "arguing from. "
                "The straw man is confined to that half of the cluster. Carpenter's proof 72 does "
                "the opposite: his statement of the globe's prediction — that vertical walls are "
                "nowhere parallel, and that houses on opposite sides of a street are not strictly "
                "so — is accurate, and he neither exaggerates it nor invents a position to "
                "knock down. He states it correctly and then denies it is observable, and at his "
                "scale, with his instruments, that denial was true.")),

    compression=dict(
        assessed=True, drifted=True,
        list_phrasing="Plumb lines perpendicular worldwide.",
        source_wording=("“If, however, the celestial surface is not concave, but horizontal, two "
                        "plumb-lines suspended north and south of each other would be parallel, and "
                        "would indicate equal length in all the degrees of latitude … The "
                        "differences required by a globe are not found in practice, but such as a "
                        "plane would produce are invariably found.”"),
        drift_type="scope_widened",
        note=("The source&rsquo;s claim is about <em>two</em> plumb lines, <em>north and south of "
              "each other</em>, inferred from one printed table of British meridian arcs whose "
              "midpoint latitudes span 51.05&deg; to 52.84&deg; and whose stations run from the "
              "Isle of Wight to Yorkshire &mdash; some 300 km of one country. The item says "
              "<em>worldwide</em>. The widening is not cosmetic: inside a "
              "single British survey the predicted lean between stations is a few arcseconds and "
              "is swamped by the local deflections that produced Rowbotham&rsquo;s anomaly in the "
              "first place, whereas &ldquo;worldwide&rdquo; is the scale at which two verticals "
              "differ by up to 180&deg; and at which bridge towers are built non-parallel on "
              "purpose. The list restates the claim at the one scale where it is easiest to check, "
              "and it fails there.<br><br>"
              "<strong>Two further things travel with the argument and neither survives into the "
              "item.</strong> <em>The condition:</em> the sentence is the consequent of &ldquo;if "
              "the celestial surface is not concave, but horizontal&rdquo;, a premise about the sky "
              "which the item does not carry and which, taken either way, defeats the conclusion it "
              "was introduced to support. <em>The evidence:</em> Rowbotham is not reporting an "
              "observation of plumb lines but drawing an inference from degree lengths he quotes "
              "from Hugh Murray&rsquo;s <em>Encyclopaedia of Geography</em> &mdash; including "
              "Murray&rsquo;s own report that the disagreement between arcs could not be explained "
              "satisfactorily. The item presents as a fact about plumb lines what the source "
              "presents as a deduction from a surveying discrepancy. That second gap has no exact "
              "slot in the seven-value list &mdash; an inference republished as an observation "
              "&mdash; and <code>scope_widened</code> is recorded because it is the plainest and "
              "most checkable of the three, with both texts printed above.<br><br>"
              "<strong>Items 396 and 397 drift the same way from a different author, and add a "
              "drift in time.</strong> Carpenter&rsquo;s proof 72 is scoped to walls of buildings "
              "and houses across a street, where the lean is 0.65 arcseconds, and his assertion is "
              "about the state of the evidence in 1885: that <em>all observation fails to find</em> "
              "the non-parallelism. &ldquo;Architecture plumb/level universal&rdquo; and "
              "&ldquo;Skyscraper vertical stable&rdquo; keep the conclusion, drop the scale it "
              "depended on, and restate a 141-year-old claim about what had then been detected as a "
              "standing fact about what is detectable now &mdash; in a decade when the quantity is "
              "published as a national grid to a tenth of an arcsecond. There is a quieter "
              "slippage in the wording too: Carpenter&rsquo;s &ldquo;perpendicular walls&rdquo; "
              "means walls each plumb at its own site, which is true on a globe, while the "
              "item&rsquo;s &ldquo;perpendicular &hellip; worldwide&rdquo; is read as all of them "
              "being parallel to one another, which is not. One word carries both claims and only "
              "the second is at issue.<br><br>"
              "<strong>Where the items sit is itself evidence.</strong> In the specimen, 396 and "
              "397 are not among Victorian material: they fall inside a run of modern "
              "engineering-vocabulary one-liners &mdash; &ldquo;Leveling equipotential planes.&rdquo;, "
              "&ldquo;Photogrammetry planar.&rdquo;, &ldquo;Mining surveys flat.&rdquo;, "
              "&ldquo;Pendulum clocks stable.&rdquo; &mdash; none of which carries a citation, and "
              "one of which uses a term for a curved surface as a synonym for a plane. The "
              "Victorian claim has been re-dressed in a professional vocabulary its author did not "
              "have.<br><br>"
              "<strong>The refutation answers the sources, not the fragments:</strong> it concedes "
              "Carpenter&rsquo;s observation at Carpenter&rsquo;s scale in its own voice, quotes "
              "Rowbotham through to his flat conclusion rather than stopping at his conditional, "
              "and puts the weight on his own materials &mdash; the table that shows unequal "
              "degrees where his conclusion requires equal ones, and the perspective sky that "
              "cannot produce equal ones either.")),

    verdict_challenge=dict(challenged=False, proposed_verdict=None, reasoning=None),

    people=["PER-ROWBOTHAM", "PER-CARPENTER"],
    related=["B01", "B02", "B04", "B05", "B06", "B11", "R08", "A03"],

    sources=[
        dict(label="Rowbotham (as “Parallax”), Zetetic Astronomy: Earth Not a Globe, 3rd ed. 1881 — "
                   "archive.org transcription (item zeteticastronomy-earthnotaglobe, file "
                   "ZeteticAstronomy-EarthNotaGlobe-3e-format2); “Arcs of the Meridian” at that "
                   "file’s pp. 186–189, carrying the von Gumpach extract, the Ordnance Survey "
                   "degree table from Hugh Murray, and the plumb-lines passage; “Declination of the "
                   "Pole Star” at p. 180",
             url="https://archive.org/download/zeteticastronomy-earthnotaglobe/ZeteticAstronomy-EarthNotaGlobe-3e-format2_djvu.txt"),
        dict(label="Rowbotham, Zetetic Astronomy: Earth Not a Globe! (1865 first book edition), "
                   "Project Gutenberg #69892 — searched for plumb, perpendicular, wall, building, "
                   "spire, tower, parallel: the three occurrences of “plumb” are the Encyclopædia "
                   "Britannica “Levelling” extract, the air-gun and the Plymouth Hoe mirror, all "
                   "instrumental; the arcs table and the “oblong” quotation are present, the "
                   "plumb-line inference is not",
             url="https://www.gutenberg.org/ebooks/69892"),
        dict(label="Carpenter, One Hundred Proofs that the Earth Is Not a Globe (Baltimore, 1885), "
                   "proof 72, indexed “Walls not parallel!” — the buildings-and-streets form, and "
                   "the only located ancestor of items 396 and 397",
             url="https://www.gutenberg.org/ebooks/55387"),
        dict(label="NOAA National Geodetic Survey, Deflection of the Vertical Survey — a camera "
                   "levelled to the local plumb line and compared against the star field, “an "
                   "accuracy of 0.1 arc-seconds”, values that “can approach many 10s of "
                   "arc-seconds”, and “the slope is determined solely by the camera system”",
             url="https://geodesy.noaa.gov/GEOID/GSVS/deflection-vertical.shtml"),
        dict(label="NOAA National Geodetic Survey, DEFLEC18 — a published grid of the deflection of "
                   "the vertical in Xi and Eta components, “typically a few arc seconds, but can "
                   "reach an arc minute of departure”, used for “the conversion between astronomic "
                   "and ellipsoidal azimuths (the Laplace correction)”",
             url="https://geodesy.noaa.gov/GEOID/DEFLEC18/"),
        dict(label="1911 Encyclopædia Britannica, “Earth, Figure of the” — the English survey’s own "
                   "station deflections (sixteen stations: six under 2″, six between 2″ and 4″, "
                   "four above 4″) and “The non-recognition of this circumstance often led to much "
                   "perplexity in the early history of geodesy”",
             url="https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Earth,_Figure_of_the"),
        dict(label="Watts, Isostasy and Flexure of the Lithosphere, ch. 1 (history) — Everest’s "
                   "Kaliana–Kalianpur discrepancy of 5.24″, Pratt’s forward computation of 15.885″ "
                   "from the Himalaya (read 7 December 1854, published 1855), and Airy’s 1855 reply "
                   "proposing light crust at depth",
             url="https://geofaculty.uwyo.edu/dueker/GeophysicsClass/watt%20isostasy%20flexure%20chap-1%20HISTORY.pdf"),
        dict(label="Barzaghi et al., “A Comparative Study of the Applied Methods for Estimating "
                   "Deflection of the Vertical in Terrestrial Geodetic Measurements”, Sensors "
                   "16(4):565 (2016) — astro-geodetic camera, GNSS-plus-levelling and a gravimetric "
                   "geoid compared at the same sites",
             url="https://www.mdpi.com/1424-8220/16/4/565"),
        dict(label="Metropolitan Transportation Authority, Verrazzano-Narrows Bridge — the "
                   "operator’s own description: towers “1 5/8 inches farther apart at their tops "
                   "than at their bases because the 4,260 foot distance between them made it "
                   "necessary to compensate for the earth’s curvature”; towers 693 ft, main span "
                   "4,260 ft",
             url="https://www.mta.info/agency/bridges-and-tunnels/verrazzano-narrows-bridge"),
        dict(label="Humber Bridge — “The towers, although vertical, are 1.4 inches (36 mm) farther "
                   "apart at the top than the bottom due to the curvature of the Earth”; towers "
                   "155.5 m, main span 1,410 m",
             url="https://en.wikipedia.org/wiki/Humber_Bridge"),
        dict(label="LIGO Caltech, “Facts” — “Over the 4km length of each arm, the Earth curves away "
                   "by nearly a meter!”, and the precision levelling of the beam-tube slab so the "
                   "beam “strikes the test mass/mirror at the end of each arm, and not a meter "
                   "above it”",
             url="https://www.ligo.caltech.edu/page/facts"),
        dict(label="Simanek, “The Tamarack Mines Mystery” — the 1901–02 Calumet plumb-line "
                   "measurements, McNair’s repeat across several shafts (January–February 1902), "
                   "results from 0.028 ft convergence to 0.141 ft divergence with “an error not "
                   "greater than 0.003 feet”, and the air-current explanation",
             url="https://dsimanek.vialattea.net/hollow/tamarack.htm"),
    ]),
}
