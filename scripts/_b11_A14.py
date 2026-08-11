# -*- coding: utf-8 -*-
"""Batch 11 — A14. "Ballistics and artillery ignore Earth's rotation."

Three items: 114 "Artillery stationary calculations.", 258 "Ballistics ignore
rotation.", 407 "Artillery geocentric mils." Verdict REFUTED, kept, no challenge filed.

Research notes for whoever picks this up next.

1. THE CORPUS TEXT IS GOOD, AND THE SPECIMEN WAS RE-READ. The live page at
   withthesun33.com/about-1 was fetched again on 2026-08-11 and all three item strings
   appear on it verbatim and in the corpus order. While there, 460 of our 461 corpus
   items were matched against the page after normalising curly quotes; the one that does
   not match is item 461, which our corpus already flags as truncated in source. So the
   corpus is sound. TWO OBSERVATIONS ABOUT THE SPECIMEN, REPORTED UP, NOT ACTED ON HERE:
   the page's own heading reads "435 Pieces of Evidence The Earth is Not A Spinning Ball"
   above a list our count puts at 461, and the site is bylined Andy J Consoli.

2. THE ATTRIBUTION IN clusters.py DOES NOT SURVIVE CONTACT. The record has
   originator="Samuel Rowbotham", originator_work="Earth Not a Globe", year="1865".
   Searching the Project Gutenberg text of the 1865 first edition (ebook #69892) for
   artillery, gunnery, gunner, cannon, ballistic, projectile, mortar, shell and firing
   returns exactly one relevant passage, and it is the vertical AIR-GUN experiment — the
   ball fired straight up that falls back into the muzzle. That is the vertical-projectile
   argument the project already credits to Rowbotham in the genealogy doc, and it is not
   this cluster. The same search over the Google/archive scan of the 1865 edition
   (item samuel_rowbotham_-_earth_not_a_globe, title page dated 1865) returns the same
   air-gun passage and nothing else. Rowbotham is not the source of an artillery claim.

3. WHAT THE SOURCE ACTUALLY IS. Two modern texts, in the transmission order the project
   already documents (Dubay compiles; this list pads Dubay):
     (a) Eric Dubay, 200 Proofs Earth Is Not a Spinning Ball (2015), proof 24 — east- and
         west-firing cannon should differ in range, north/south "should establish a
         control", and "regardless of which direction cannons are fired, the distance
         covered is always the same." This is the ROTATION-specific ballistics claim and
         it is the passage used in the entry below. Proof 20 next to it is the vertical
         cannonball (Rowbotham's air gun, modernised) and belongs to a different cluster.
     (b) Edward Hendrie, The Greatest Lie on Earth (2016), CHAPTER 9, "No Coriolis Effect
         Proves a Stationary Earth", printed pp. 105-114, with the artillery and sniper
         material at pp. 113-114. PAGE CONVENTION, ESTABLISHED FROM FOUR ANCHORS BEFORE
         BEING USED: in this OCR the printed page marker sits at the FOOT of its page, so
         text between markers N and N+1 is page N+1. The chapter 9 heading follows marker
         104 and the table of contents gives chapter 9 as p. 105; the chapter 10 heading
         follows marker 114 against a TOC page 115; chapter 7 follows marker 83 against TOC
         84; chapter 11 follows marker 119 against TOC 120. The artillery/sniper paragraph
         sits between markers 112 and 113 and is therefore on p. 113; the "former federal
         firearms instructor" warrant sits between 113 and 114, on p. 114. Earlier drafts of
         this entry cited pp. 112-113 and were off by one; corrected 2026-08-11.
         This is where the list's word "artillery" comes from.
         Hendrie: "you will look in vain for any mention of Coriolis effect in any
         military artillery or sniper instruction manual", and "no soldier has ever been
         instructed to consider the Coriolis effect of a spinning Earth when [sighting] in
         a target with his artillery piece or other weapon."
   Checked and negative, so nobody re-derives it: searching the archive.org OCR text of
   Galileo Was Wrong Vol. II returns no occurrence of artiller-, gunner- or mils, though
   it uses Coriolis 45 times in the Machian rotating-universe sense that belongs to A09
   and R02. This is not a Sungenis argument.

4. THE ANCESTOR IS PRE-MODERN AND IT IS DOCUMENTED. Giovanni Battista Riccioli,
   Almagestum Novum (Bologna, 1651), Part II, Book 9, Sec. 4, ch. 21, pp. 425, 426-7 —
   arguments 17 and 19 of his 77 against the motion of the Earth. Both are cannon
   arguments: a ball fired toward the pole should be deflected because the ground moves
   more slowly at higher latitudes, and a ball fired north should strike more weakly than
   one fired east. Riccioli credits the cannon experiment to Tycho and argument 19 to
   Grimaldi. Claude Francois Milliet Dechales repeats it in Cursus seu Mundus
   Mathematicus (1674). English renditions and analysis by Christopher M. Graney:
   arXiv:1012.3642 (the translation used here), arXiv:1103.2057 = JHA 43 (2012) 215-226,
   arXiv:1611.07912 = Physics Today 70(7):12 (2017). Graney's own claim is hedged — the
   argument "appears to be an early description of the Coriolis effect" — and this entry
   keeps that hedge. So the origin state for A14 is the PRE-MODERN one (Tycho ->
   Riccioli/Grimaldi 1651 -> Dechales 1674), which forces originator=None and forbids the
   word "first". See §10.

5. RICCIOLI'S OWN TEXT CONTAINS THE ANSWER AND REJECTS IT, WHICH IS THE KERNEL.
   Graney's rendition: "The Copernican response to this argument is to deny it, or to
   concede it but claim that the differences in trajectory fall below our ability to
   measure. But in fact the argument is strong, and this response is not." The Copernicans
   were right and Riccioli was wrong, on a question of magnitude, and the magnitude is
   computable. Riccioli's own case is a 60-80 lb ball crossing 250 paces in 2 seconds.

6. THE ARITHMETIC, COMPUTED HERE 2026-08-11. Flat-trajectory approximation, lateral
   deflection D = OMEGA sin(lat) * R * T with OMEGA = 7.292115e-5 rad/s:
     Riccioli's shot, 250 paces (~310-370 m) in 2 s at Bologna 44.5N ... 3-4 cm
     rifle, 300 m, TOF 0.40 s, 45N ............................... 6 mm
     rifle, 1000 yd, TOF 1.7 s, 38.6N ............................ 7.1 cm (2.8 in)
     155 mm, 22 km, TOF 65 s, 45N ................................ 74 m (= 3.4 mils)
     155 mm, 30 km, TOF 90 s, 45N ................................ 139 m
     Paris Gun, 120 km, TOF 176 s, 49.5N ......................... 1.2 km
   THE FORMULA IS CROSS-CHECKED, not asserted: it reproduces the independently published
   figure of about 2.8 in for a 1,000-yard northward shot at Sacramento's latitude when
   given a 1.7 s time of flight. Do not claim it reproduces any printed firing-table
   value — Table H and Table I appear in TC 3-09.81 as figure images and were NOT read.
   Vertical (Eotvos) component, a_z = 2 OMEGA v cos(lat), range effect ~ (a_z/g) R:
     155 mm, 22 km, 45N ... a_z = 0.035 m/s^2, dR ~ 78 m, 0.36% of range
     Paris Gun ............ dR ~ 790 m, 0.66% of range
   Dubay's naive version, by contrast, has the 1,000 mph (447 m/s) adding to and
   subtracting from muzzle velocity; at a 684 m/s muzzle velocity and range going as v^2
   that is an east/west range ratio of about 23:1. Observed: nothing of the sort. Correct,
   and Galilean, and not the effect the firing tables tabulate.

7. THE DOCUMENTS THAT DECIDE IT. Two, seventy-one years apart, both public:
     TC 3-09.81, Field Artillery Manual Cannon Gunnery, HQ Dept of the Army, 13 April
       2016 — the same year as Hendrie's book. Para 3-63 lists "Rotation of the earth"
       among the deviations from standard conditions affecting BOTH range and deflection.
       Chapter 7 paras 7-20 to 7-24: Table H gives "the correction to range in meters for
       the rotation of the earth at 0 degrees latitude" with a latitude multiplier; Table
       I gives "the correction to deflection in mils, for the rotation of the earth", with
       "tables for every 10 degrees latitude starting from 0 degrees north or south
       latitude to 70 degrees north or south latitude", entered along the top for northern
       latitudes and "from the bottom" for southern. Para 7-22 works the theory: a point
       on the equator has an eastward linear velocity of "approximately 457 meters per
       second" (that is 1,500 ft/s, about 1.7% under the sidereal 465.1 m/s), a gun firing
       east impacts over the target and one firing west impacts short. That paragraph is
       Dubay's proof 24, worked and tabulated. The training example at para 11-x step 17
       reads "Select the appropriate Table I on the basis of latitude (30 degrees N)".
     FM 6-40, War Department Field Manual, Field Artillery, Gunnery, 1945 — para 10 lists
       "rotation of the earth tables for direction and range" among the firing-table
       corrections; para 323 instructs the computer to list "altitude (and latitude) of
       battery, direction of fire" and to take "range and deflection effects due to
       rotation of the earth for the latitude of the battery (long range weapons only)".
     FM 4-10 (Coast Artillery, Gunnery, 1944) carries the same tables — corroboration
       only; nothing below rests on it.

8. THE HONEST CONCESSIONS, AND THEY ARE THREE. Do not soften them; the entry is stronger
   for carrying them and a defender who finds them missing gets the section.
   (a) The word "Coriolis" is not located in the text layer of the April 2016 TC 3-09.81
       PDF searched here. That manual, and FM 6-40 (1945), call the thing "rotation of the
       earth" — the word "Coriolis" is not located in either. What the wider doctrinal
       corpus calls it was NOT checked, and the published concession no longer says it was.
       Hendrie's sentence, read as a claim about the WORD, survives; read as a claim about
       the THING, it is refuted by two tables in the document.
   (b) The word "Coriolis" is likewise not located in the archive.org OCR text of FM 23-10
       Sniper Training (17 August 1994) searched here — which is the manual Hendrie's own
       footnote cites. His small-arms testimony is TRUE and the entry says so.
   (c) The National Geographic passage Hendrie attacks is genuinely bad: the claim that a
       pilot flying "in a straight line" from Portland, Oregon would end up near New York
       confuses a great circle drawn on a Mercator projection with a Coriolis deflection.
       Wikipedia's own Coriolis article warns against exactly that conflation. He is right
       about his target and wrong about the conclusion he draws from it.
9. HENDRIE'S FOOTNOTES ARE THE SHORTEST ROUTE TO THE ANSWER. The passage at p. 113
   carries two notes. One cites FM 23-10 (1994) and a Navy SEAL sniper program. The other,
   supporting a claim about "all of the wars fought throughout history", cites four
   artillery manuals: Bethel, Modern Artillery in the Field (1911); Instruction for Field
   Artillery Prepared by a Board of Artillery Officers (1860); Artillerist's Manual (1863);
   Roberts, The Hand-Book of Artillery (1863). Three of the four predate the First World
   War and the newest is from 1911. The in-line OCR markers are garbled, so the entry does
   NOT assert which sentence takes which note — it describes what the two notes cite, which
   is all the argument needs. (The endnote list itself is legible and numbers them 115
   — FM 23-10 plus the Navy SEAL program — and 116 — Bethel 1911, Instruction for Field
   Artillery 1860, Artillerist's Manual 1863, Roberts 1863; the two markers appear in that
   order in the paragraph, but the published prose does not lean on that.)

10. DEFECTS IN OUR OWN RECORD, reported up, NOT edited here (this agent owns one file):
    (a) clusters.py A14 originator/originator_work/year credit Rowbotham 1865 for a claim
        not located in that book. Proposal: withdraw to the PRE-MODERN state with
        earliest_documented_use = Riccioli, Almagestum Novum, 1651, arguments 17 and 19,
        and Dubay 2015 / Hendrie 2016 recorded as repopularisers. This is the C02 shape.
    (b) clusters.py A14 real_source="Standard long-range fire-control tables" is vague for
        a project whose product is provenance. Proposal: TC 3-09.81 (2016) Tables H and I;
        FM 6-40 (1945) firing-table tables D and E. Both halves re-verified 2026-08-11 —
        FM 6-40 para 323: "From tables D and E, part 2, of the firing tables, obtain range
        and deflection effects due to rotation of the earth for the latitude of the
        battery (long range weapons only)."
    (c) clusters.py A14 note asserts "Long-range gunnery has corrected for Coriolis drift
        since WWI; naval fire-control computers did it mechanically." NEITHER HALF WAS
        VERIFIED HERE AND THE FIRST FAILED A CHECK: the phrase "rotation of the earth" is
        not located in the archive.org OCR text of Alger, The Groundwork of Practical Naval
        Gunnery (1917), which is a WWI-era naval exterior-ballistics textbook and treats
        drift in the spin sense only. The earliest gunnery document reached here that
        carries the correction is FM 6-40 (1945). The mechanical-computer half was not
        tested at all. Proposal: replace with the 1945/2016 pair, which is checkable.
    (d) works.py has no record for Hendrie 2016 and people.py has none for Hendrie, so the
        passage below uses WRK-DUBAY-2015 — the other of the two modern sources, in
        WORKS, and the one this list descends from — and carries Hendrie in the gloss and
        the sources list. If a WRK-HENDRIE-2016 is ever added, the passage should move.
    STILL UNAPPLIED as of 2026-08-11 — recorded here across two passes and not yet carried
    into clusters.py, which is the E01/E03 "recorded, not actually applied" pattern. Until
    it is, the rendered header prints "first published by Samuel Rowbotham" directly above a
    gloss that says no single author is credited, and the basis line under the Refutation
    summary prints an unverified WWI/naval-computer claim directly above our own concession
    about the 2016 manual. Whoever applies it: anchor the edit on the cluster key "A14",
    never on the byte-identical originator= line (that exact line occurs seven times in
    clusters.py — A08, A13, A14, A17, B06, B09, B10, checked 2026-08-11), and keep
    the word "first" out of the replacement — the attribution guards test for it.
    None of this is written into the published prose as a recommendation. The prose states
    what the texts show and nothing about what our records ought to say.

11. RE-VERIFICATION PASS, 2026-08-11 (adversarial review applied). Every source claim in
    this entry was re-checked against the source text, not against the review note:
    (a) TC 3-09.81, 13 April 2016 PDF pulled from armypubs and converted with pdftotext.
        "coriolis" 0 occurrences in the text layer. Para 3-63 verbatim: "Actual firing
        conditions, however, will never equate to standard conditions", with "Rotation of
        the earth" in BOTH the range-effects and the deflection-effects lists. Figure 7-1
        (and the duplicate figure 11-1) list NO ROTATION OF THE EARTH under POSITION and
        NO WIND under WEATHER — so they are in the same standard-conditions list but NOT
        adjacent; the note used to say "directly beneath NO WIND" and now does not.
        Paras 7-20/7-21 (Table H), 7-23/7-24 (Table I), 7-22 ("approximately 457 meters per
        second", "impact east of the target (over the target in this case)", west "short of
        the target") and step 17a ("Select the appropriate Table I on the basis of latitude
        (30 degrees N)") all confirmed verbatim.
    (b) FM 6-40 (1945), archive.org OCR: "coriolis" 0; "rotation of the earth tables for
        direction and range" and "from tables D and E, part 2, of the firing tables, obtain
        range and deflection effects due to rotation of the earth for the latitude of the
        battery (long range weapons only)" both confirmed verbatim.
    (c) Dubay proof 24 confirmed verbatim, including "lOOOmph"; proof 25 is the eastbound
        airliner, as stated. "artiller" and "mils" each 0 occurrences in that OCR.
    (d) Hendrie: the artillery/sniper passage confirmed verbatim; "mils" 0 occurrences in
        that OCR. Page numbering corrected 112-113 -> 113-114, see §3(b).
    (e) Graney arXiv:1012.3642 confirmed verbatim for all three quoted strings, including
        the full Copernican-response sentence quoted through its reversal ("...or to concede
        it but claim that the differences in trajectory fall below our ability to measure.
        But in fact the argument is strong, and this response is not."), and for the
        60-or-80-pound ball crossing 250 paces in 2 human pulsebeats.
    (f) The "four orders below" figure in section 2 was WRONG and is gone. Like for like at
        22 km: the naive v^2 model gives ~60 km east against ~2.6 km west, a difference of
        ~57 km, against a real ~156 m — a factor of ~370, i.e. 2.6 orders. Four came from
        comparing the dimensionless 23:1 ratio with the 0.36% fractional shift.

12. VERDICT. REFUTED, kept. The cluster asserts that gunnery ignores the Earth's rotation.
    Two field manuals seventy-one years apart tabulate the correction, index it by the
    battery's latitude, express half of it in mils and reverse the table entry across the
    equator. There is no live scientific question here — this is settled exterior
    ballistics, not an open literature, so the E01 caution does not apply. What IS
    conceded is the small-arms half, in the entry's own voice, because it is true.
"""

ENTRY = {

"A14": dict(

    tldr=("US Army cannon firing tables carry a correction for the rotation of the earth — "
          "in the 1945 manual and in the 2016 one. It is indexed by the battery's latitude, "
          "it is entered from opposite edges of the table in the northern and southern "
          "hemispheres, and the deflection half of it is published in mils, the unit the "
          "list's own item names. The argument is right that a rifleman can ignore the "
          "effect and wrong that a long-range gunner does, and one piece of arithmetic "
          "explains both halves: the deflection grows with range and time of flight, so it "
          "is a few centimetres at a thousand yards and over a hundred metres at thirty "
          "kilometres."),

    passage=dict(
        work="WRK-DUBAY-2015",
        pd=False,
        locator=("Proof 24 of 200 Proofs Earth Is Not a Spinning Ball, transcribed from the "
                 "archive.org OCR text of the PDF (item 200ProofsEarthIsNotASpinningBall), "
                 "where the numeral is rendered “lOOOmph”. Identified by its neighbours: "
                 "proof 23 is the atmosphere-dragging item and proof 25 is the eastbound "
                 "airliner. Not checked against the 2018 print edition, which may renumber"),
        quote=("If Earth and its atmosphere were constantly spinning eastwards over 1000mph "
               "then North/South facing cannons should establish a control while East-firing "
               "cannonballs should fall significantly farther than all others while "
               "West-firing cannonballs should fall significantly closer. In actual fact, "
               "however, regardless of which direction cannons are fired, the distance "
               "covered is always the same."),
        gloss="""<p><strong>Read what the claim commits to.</strong> It is not vague. It names a control (north/south fire), a signal (an east&ndash;west range difference), and a result (there is none). That is a testable proposition about gunnery, and it is the only member of this cluster&rsquo;s ancestry that specifies the <em>rotation</em> rather than the Earth&rsquo;s motion in general. Everything below answers it at that strength.</p>
<p><strong>Where the word &ldquo;artillery&rdquo; comes from, because it is not from here.</strong> Dubay writes &ldquo;cannons&rdquo;. The list writes &ldquo;artillery&rdquo;, twice, and the vocabulary tracks a second and later book: Edward Hendrie, <em>The Greatest Lie on Earth</em> (2016), chapter 9, &ldquo;No Coriolis Effect Proves a Stationary Earth&rdquo;, at printed pp. 105&ndash;114, with the passage the items compress at pp. 113&ndash;114. Hendrie states it without a hedge anywhere in it: <em>&ldquo;you will look in vain for any mention of Coriolis effect in any military artillery or sniper instruction manual&rdquo;</em>, and that in all the wars of history <em>&ldquo;no soldier has ever been instructed to consider the Coriolis effect of a spinning Earth&rdquo;</em> when laying a gun. He adds a personal warrant &mdash; he is a former federal firearms instructor and has never seen a round affected by it, nor read of it in a firearms manual.</p>
<p><strong>The footnotes are the shortest route to the answer.</strong> That passage carries two notes. One cites FM 23-10, <em>Sniper Training</em> (17 August 1994) and a Navy SEAL sniper program. The other, attached to a claim about every war ever fought, cites four artillery manuals: Bethel&rsquo;s <em>Modern Artillery in the Field</em> (1911), <em>Instruction for Field Artillery</em> (1860), the <em>Artillerist&rsquo;s Manual</em> (1863) and Roberts&rsquo;s <em>Hand-Book of Artillery</em> (1863). Three of the four are American Civil War-era and the newest is from 1911 &mdash; that is, the evidence offered for the state of gunnery is a shelf assembled entirely before the ranges at which the effect matters were reached.</p>
<p><strong>The argument is far older than either book, and its ancestor is better made.</strong> In the <em>Almagestum Novum</em> (Bologna, 1651), the Jesuit astronomer Giovanni Battista Riccioli set out 77 arguments against the motion of the Earth; numbers 17 and 19 are cannon arguments. If the Earth turned, he reasoned, a ball fired toward the pole would be carried off, because &ldquo;on parallels nearer the poles, the ground moves more slowly, whereas on parallels nearer the equator, the ground moves more rapidly&rdquo;, and a ball fired north would strike its target more weakly than one fired east. He credits the cannon experiment to Tycho and argument 19 to his colleague Grimaldi; Dechales repeated it in 1674. Riccioli derived his effect from theory rather than asserting it from a shelf of manuals, and Christopher Graney, whose English rendition is used here, puts the identification carefully: the argument <em>appears</em> to be an early description of what is now called the Coriolis effect. Two centuries before Coriolis, a geocentrist had the physics of this cluster essentially right.</p>
<p><strong>What this passage is being cited as.</strong> The reachable modern statement of the rotation-specific ballistics claim, in the compilation this 461-item list is padded out of. It is not evidence of origination: the argument is older than anyone on the People tab, and no single author is credited for it here.</p>"""),

    steelman=dict(
        description="""<p><strong>SURFACE (weak &mdash; do not use).</strong> &ldquo;Snipers correct for Coriolis, so the claim is simply false.&rdquo; This loses on the defender&rsquo;s home ground. Searching the archive.org OCR text of FM 23-10, <em>Sniper Training</em> (1994) &mdash; the manual Hendrie&rsquo;s own footnote cites &mdash; returns no occurrence of the word Coriolis, and none of the word rotation in any relevant sense. Anyone who opens with this is contradicted by the document the other side supplied.</p>
<p><strong>DEEPER.</strong> &ldquo;Long-range artillery corrects for it.&rdquo; True, and still incomplete, because it invites the obvious reply: <em>your effect is conveniently absent everywhere an ordinary person could check it, and present only in tables produced by the same institutions you are asking me to trust about everything else.</em> A defender who is quick will get there in one move.</p>
<p><strong>KERNEL.</strong> The strongest form is Riccioli&rsquo;s, not Hendrie&rsquo;s, and it is a real argument. It runs: <em>a rotating Earth makes a specific, derivable prediction about where a cannon ball lands &mdash; I can derive it myself, without instruments, from the fact that the ground moves faster near the equator than near the pole. Gunners are extraordinarily good at their trade; skilled artillerymen can put a shot down the mouth of an enemy cannon. If the prediction were real they would have had to notice. They have not. The Copernican reply is that the difference falls below what we can measure &mdash; but that reply can be made about any prediction whatever, and a theory rescued that way is not being tested.</em> Every step of that is honest, and the last sentence is a serious point about falsifiability that the seventeenth century had no way to settle.</p>""",
        why_it_doesnt_save_claim="""<p>Because the &ldquo;too small to measure&rdquo; reply was not a rescue &mdash; it was a <strong>quantitative prediction with a date on it</strong>, and the date arrived.</p>
<p>The deflection is not a free parameter. On a flat trajectory it is <em>D</em> = &Omega; sin&thinsp;&phi; &times; <em>R</em> &times; <em>T</em>: the Earth&rsquo;s rotation rate, the sine of the latitude, the range and the time of flight, and nothing else. That formula says the effect must be invisible at Riccioli&rsquo;s ranges and unavoidable at long ones, and it says by how much. Riccioli&rsquo;s own case is a ball crossing 250 paces in two seconds; at Bologna&rsquo;s latitude that is a deflection of <strong>three to four centimetres</strong>, on a shot from a smoothbore whose round-to-round scatter was measured in metres. He was not wrong to see the effect. He was wrong about one number, and the Copernicans he dismissed had that number right.</p>
<p>So the argument carries its own falsification schedule. As soon as ranges and times of flight grew, the term crossed the dispersion of the weapon &mdash; and at that point gunners started correcting for it, which is exactly what the theory Riccioli was attacking predicts and what his own theory forbids. By 1918 the Paris Gun was throwing shells 120 km in about three minutes, where the same formula gives well over a kilometre of drift. The tables followed the arithmetic, not the other way round.</p>"""),

    refutation="""<p><strong>Start with what is conceded, because two of the three concessions are permanent.</strong></p>

<p><strong>One.</strong> The word &ldquo;Coriolis&rdquo; does not occur anywhere in the text layer of the April 2016 edition of the US Army&rsquo;s cannon gunnery manual searched here. That manual calls the thing <em>rotation of the earth</em> throughout, as does FM 6-40 in 1945. What the rest of Army doctrine calls it was not checked for this entry.</p>

<p><strong>Two.</strong> The small-arms half of the claim is true. Searching the archive.org OCR text of FM 23-10, <em>Sniper Training</em> (17 August 1994) &mdash; the manual the source&rsquo;s own footnote cites &mdash; returns no occurrence of the word Coriolis. A firearms instructor who says he has never seen a round visibly affected by the Earth&rsquo;s rotation, and never heard it discussed on a range, is reporting something accurate.</p>

<p><strong>Three.</strong> The popular-science passage the source attacks deserves it. The <em>National Geographic</em> explanation quoted in that chapter says that a pilot flying &ldquo;in a straight line&rdquo; from Portland, Oregon would end up near New York or Pennsylvania. That is a great circle drawn on a Mercator projection being reported as a Coriolis deflection &mdash; a conflation the Coriolis-force reference article cited below warns against explicitly. Attacking it is fair.</p>

<p><strong>What the verdict ranges over.</strong> Not &ldquo;the effect is large&rdquo;, and not &ldquo;everyone who points a weapon corrects for it.&rdquo; The cluster&rsquo;s claim is that <em>gunnery ignores the Earth&rsquo;s rotation</em>, and that this is evidence the Earth does not turn. Both halves fail, and they fail for the same reason: the size of the correction is fixed by the rotation rate, and gunners apply it exactly where that size exceeds the accuracy of the weapon.</p>

<h4>1. The table exists, and it is indexed by latitude</h4>

<p>Open <em>TC 3-09.81, Field Artillery Manual Cannon Gunnery</em>, Headquarters, Department of the Army, dated 13 April 2016 &mdash; the same year the source&rsquo;s book was published. Paragraph 3-63 lists the deviations from standard conditions that firing data must be corrected for. Under range effects: muzzle velocity, projectile weight, range wind, air temperature, air density, <strong>rotation of the earth</strong>, propellant temperature. Under deflection effects: drift, crosswind, <strong>rotation of the earth</strong>.</p>

<p>Chapter 7 says how. <strong>Table H</strong> gives &ldquo;the correction to range in meters for the rotation of the earth at 0&deg; latitude&rdquo;, entered with the range and with &ldquo;the exact azimuth (to the nearest mil) to the target&rdquo;, and multiplied by a factor taken from a latitude table beneath it. <strong>Table I</strong> gives &ldquo;the correction to deflection in mils, for the rotation of the earth&rdquo;, and there are &ldquo;tables for every 10&deg; latitude starting from 0&deg; north or south latitude to 70&deg; north or south latitude&rdquo;. Northern latitudes are entered along the top of the table; for southern latitudes &ldquo;you enter from the bottom&rdquo;. The manual&rsquo;s own worked example instructs the student to &ldquo;Determine corrections for azimuth to compensate for rotation of the earth from Table I&rdquo; and then to &ldquo;Select the appropriate Table I on the basis of latitude (30&deg;N).&rdquo;</p>

<p>Read that structure rather than just the fact of it. The correction depends on <strong>where on the Earth the gun is standing</strong>, on <strong>which way it is pointing</strong>, and it is entered from <strong>opposite edges of the table in the two hemispheres</strong>. Those are three dependencies that a rotating sphere predicts and that nothing else in the gunnery problem &mdash; not wind, not air density, not propellant temperature, not the rifling &mdash; produces.</p>

<p>And this is not new doctrine. <em>FM 6-40, Field Artillery, Gunnery</em>, War Department, 1945, already tells the computer that firing-table factors correct for, among other things, &ldquo;rotation of the earth tables for direction and range&rdquo;, and instructs him to list the &ldquo;altitude (and latitude) of battery, direction of fire&rdquo; and to take &ldquo;range and deflection effects due to rotation of the earth for the latitude of the battery (long range weapons only).&rdquo; That parenthesis is not a hedge in our favour; it is the whole physics of the case, printed in 1945, and section 3 below is about it.</p>

<h4>2. The passage above is the manual&rsquo;s own worked example</h4>

<p>The claim in the passage is that east-firing and west-firing cannon show no range difference. Paragraph 7-22 of the 2016 manual sets out the theory behind Table H in precisely those terms: because of the rotation of the earth &ldquo;a point on the equator has an eastward linear velocity of approximately 457 meters per second&rdquo;, decreasing to zero at either pole; a gun on the equator firing east will have its projectile &ldquo;impact east of the target (over the target in this case)&rdquo;, and one firing west will impact &ldquo;short of the target&rdquo;. Firing east goes long, firing west goes short, and the manual tabulates by how much. <em>That is the passage&rsquo;s experiment, performed, quantified and issued as doctrine.</em></p>

<p>The size is the point. Two different things are being run together in the claim, and separating them settles it:</p>

<ul>
<li><strong>The version the passage argues against.</strong> If the ground&rsquo;s 1,000&nbsp;mph (447&nbsp;m/s) were added to an eastward shot and subtracted from a westward one, then at a howitzer&rsquo;s muzzle velocity of roughly 684&nbsp;m/s, with range going as the square of velocity, the east/west range ratio would be about <strong>23 to 1</strong>. Nothing of the sort is observed. The passage is right, and the reason is Galilean: gun, ball, target and air all share the rotation, so it cancels out of the leading term. That has been the answer since 1632 and this review carries it at <a href="#ARG-A17">ARG-A17</a>.</li>
<li><strong>The version that survives.</strong> What does <em>not</em> cancel is the small residual from the rotation of the frame itself. For a 155&nbsp;mm shell out to 22&nbsp;km with a 65-second time of flight at 45&deg; latitude, the vertical component works out to an acceleration of about 0.035&nbsp;m/s&sup2;, which shifts the range by roughly <strong>78&nbsp;m &mdash; about 0.36% of it</strong>, in opposite directions for eastward and westward fire. That is Table H. Put the two side by side at the same range: the naive version predicts an eastward shot going about 60&nbsp;km against a westward 2.6&nbsp;km, an east/west difference of tens of kilometres, where the real difference is the 78&nbsp;m taken twice &mdash; about 150&nbsp;m, smaller by a factor of several hundred. And still far above what a battery can afford to leave out.</li>
</ul>

<p>(Both figures recomputed here on 2026-08-11 from the standard expressions; the lateral formula used throughout is cross-checked below.)</p>

<p>One limit on all of this, stated rather than buried: <strong>Table H and Table I are reproduced in the manual as figure images and were not read here.</strong> The numbers above are computed from the standard expressions and cross-checked in section 3 against an independently published rifle figure &mdash; not against the printed tables. If someone reads those tables and the values disagree with the arithmetic, this section is wrong and should be corrected against them.</p>

<h4>3. Why the rifleman is right and the gunner is not</h4>

<p>One expression explains the entire pattern of who corrects and who does not. For a flat trajectory the lateral deflection is</p>

<p style="margin-left:1.5em"><em>D</em> = &Omega; sin&thinsp;&phi; &times; <em>R</em> &times; <em>T</em>, &nbsp;&nbsp;&Omega; = 7.292115 &times; 10<sup>&minus;5</sup> rad/s</p>

<p>&mdash; the rotation rate, the latitude, the range and the time of flight. It is checked here against an independently published figure rather than asserted: for a 1,000-yard northward shot at Sacramento&rsquo;s latitude the standard number is about 2.8 inches, and the expression returns 7.1&nbsp;cm for a 1.7-second time of flight. Now run it across the cases:</p>

<table style="margin-left:1.5em">
<tr><td>rifle, 300&nbsp;m, 0.40&nbsp;s, 45&deg;</td><td style="padding-left:1.5em"><strong>6&nbsp;mm</strong></td></tr>
<tr><td>rifle, 1,000&nbsp;yd, 1.7&nbsp;s, 38.6&deg;</td><td style="padding-left:1.5em"><strong>7&nbsp;cm</strong></td></tr>
<tr><td>155&nbsp;mm, 22&nbsp;km, 65&nbsp;s, 45&deg;</td><td style="padding-left:1.5em"><strong>74&nbsp;m</strong> (3.4&nbsp;mils)</td></tr>
<tr><td>155&nbsp;mm, 30&nbsp;km, 90&nbsp;s, 45&deg;</td><td style="padding-left:1.5em"><strong>139&nbsp;m</strong></td></tr>
<tr><td>Paris Gun, 120&nbsp;km, 176&nbsp;s, 49.5&deg;</td><td style="padding-left:1.5em"><strong>1.2&nbsp;km</strong></td></tr>
</table>

<p>Six millimetres at 300&nbsp;m is inside the group of any rifle and any shooter; it is not that instructors suppress it, it is that it is smaller than the thing they are trying to teach. Seven centimetres at 1,000 yards is at the edge &mdash; comparable to a very good rifle&rsquo;s dispersion, which is why it is long-range shooters and not riflemen generally who bother with it. A hundred and thirty-nine metres at 30&nbsp;km is larger than the target, the battery and the safety fan.</p>

<p><strong>So the claim is a description of the low-range end of that table, presented as a fact about the world.</strong> And the 1945 manual states the cut-off in its own words &mdash; the earth-rotation tables are for &ldquo;long range weapons only.&rdquo; The correction appears exactly where &Omega; sin&thinsp;&phi; <em>R T</em> crosses the accuracy of the weapon. No conspiracy, no fudge factor, and no discretion: a gunner who omitted it at 30&nbsp;km would miss, and one who applied it at 300&nbsp;m would be adjusting by less than the width of the bullet.</p>

<h4>4. Answering the strongest form &mdash; Riccioli&rsquo;s, not the list&rsquo;s</h4>

<p>Riccioli put the argument better in 1651 than the modern texts do, and he anticipated the reply. His rendition records it: the Copernicans either deny the effect &ldquo;or concede it but claim that the differences in trajectory fall below our ability to measure&rdquo;, and he judged that &ldquo;the argument is strong, and this response is not.&rdquo; He also gave the case its parameters &mdash; a ball of sixty or eighty pounds crossing 250 paces in two human pulsebeats.</p>

<p>Put his own numbers into the expression above. Two hundred and fifty paces is somewhere around 310&ndash;370&nbsp;m; two seconds of flight; Bologna is at 44.5&deg; north. The deflection is <strong>three to four centimetres</strong>. Riccioli&rsquo;s guns scattered by metres. The Copernicans were not evading him; they were right, and they were right by a factor of about a hundred, and the only way to have known that in 1651 was to do an arithmetic nobody could yet do &mdash; the mathematics that puts a number on the deflection was published by Coriolis in 1835, and Riccioli died in 1671.</p>

<p>That is the whole history of this argument in one sentence: <strong>it was a good argument that was refuted by the growth of gun ranges.</strong> Reviving it in 2016 requires the ranges to have stopped growing, and they did not.</p>

<h4>5. What the claim would have to explain</h4>

<p><strong>First, the strongest version of the reply: that the tables are decoration on a stationary-Earth solution.</strong> The point is a real one and the manual concedes half of it in print &mdash; the list of standard conditions the firing tables are built on includes <code>NO ROTATION OF THE EARTH</code>. The ballistic solution genuinely is computed on a motionless Earth and corrected afterwards. But the same list includes <code>NO WIND</code> and a propellant temperature of 70&deg;F, and nobody reads it as a claim that wind does not exist or that powder is always at seventy degrees. The paragraph that introduces the deviations says so in terms: actual firing conditions &ldquo;will never equate to standard conditions.&rdquo; A baseline is not a denial. So the question is not whether the baseline is stationary &mdash; it is &mdash; but what the corrections applied to it depend on.</p>

<p>Suppose gunnery really did work on a stationary Earth and the tables were institutional decoration. Then a defender owes an account of four things at once: why the correction is a function of the <em>battery&rsquo;s latitude</em>; why it is a function of the <em>azimuth of fire</em>; why the deflection table is entered from the opposite edge in the southern hemisphere; and why its magnitude agrees with a number computed from nothing but the length of the day. Wind depends on none of those. Air density depends on none of them. Rifling drift is a constant handed sideways, the same at every latitude. There is no second candidate that produces a latitude-and-azimuth-dependent, hemisphere-reversing correction of exactly the computed size, and none of the sources traced for this entry proposes one.</p>

<h4>6. What is left, stated without decoration</h4>

<p>The rotation of the earth is a named, tabulated correction in US Army cannon gunnery in 1945 and in 2016. It is indexed by latitude and azimuth, reverses across the equator, and is published in mils &mdash; the artillery angular unit that one of these three list items names. The claim that it is absent is true only of small arms, where the arithmetic says it should be, and is stated in the sources as a claim about everything. This argument was better made in 1651, and it lost to nothing more exotic than longer guns.</p>""",

    advocate=dict(
        best_defense=(
            "Look at what you have actually conceded. The word Coriolis is not in the "
            "sniper manual. It is not in your own 2016 artillery manual either — you had "
            "to go looking for a different phrase. The effect is below the dispersion of "
            "the weapon at every range where a private citizen could test it for himself "
            "with equipment he owns. So the entire empirical content of your reply is a "
            "table inside a document issued by the same institution whose satellite "
            "photographs and moon landings you are also asking me to accept. That is not "
            "independent evidence; that is the same witness testifying twice. "
            "Second — and this is the part you have walked straight past — your own "
            "manual lists NO ROTATION OF THE EARTH under STANDARD CONDITIONS. The "
            "baseline the whole ballistic solution is computed on is a stationary Earth. "
            "Everything after that is a correction table, and correction tables are "
            "fitted to observed fall of shot: gunners fire, they see where the rounds "
            "land, and they write the difference into a table. You have no way to show me "
            "that the numbers in Table I were derived from omega rather than measured and "
            "then labelled with omega afterwards, because you did not read Table I — you "
            "said so. You computed what you think it ought to say and called that a "
            "check. Third, your best number is a centimetre. You are asking me to "
            "overturn what I can see with my own eyes on the strength of a residual a few "
            "hundred times smaller than the effect the theory started out predicting, "
            "every time it fails to show up."),
        survives=4,
        preemptive=(
            "Four, driven by the second and third moves. The FIRST move is answered by "
            "not overclaiming in the first place, and the body already concedes the two "
            "absences in its own voice — those concessions must stay where they are, at "
            "the top, and must not be moved below the tables. "
            "The SECOND move is the serious one and it is now answered in the body "
            "explicitly rather than by implication: section 5 opens on it. Three "
            "responses. (a) The standard-conditions list that contains NO ROTATION OF THE "
            "EARTH also contains NO WIND and a propellant temperature of 70°F — nobody "
            "reads that list as a claim that wind does not exist, and the paragraph that "
            "introduces the deviations (3-63) says in terms that actual firing conditions "
            "'will never equate to standard conditions'. That is the new section 5 "
            "lead-in. (b) The correction was DERIVED BEFORE IT WAS MEASURED — Riccioli got "
            "the sign and the geometry of it in 1651 from the rotation alone, with no "
            "fall-of-shot data of any kind, which is exactly what a fitted fudge factor "
            "cannot be; section 4 carries it, and it is the one answer that does not "
            "require trusting any military document at all. (c) A fitted correction has no "
            "reason to be indexed by the battery's latitude or to reverse across the "
            "equator — the body of section 5. "
            "On the admission that Table I itself was not read: it is no longer only in "
            "these notes. The last paragraph of section 2 now states in the entry's own "
            "published voice that Table H and Table I are figure images, that they were "
            "not read here, that the arithmetic is cross-checked instead against an "
            "independently published rifle figure, and that the section is wrong if the "
            "printed values disagree. A defender who discovers a gap the page has already "
            "declared cannot call it bluffing. If anyone later reads the printed tables "
            "and the numbers agree, that is a genuine upgrade to make. "
            "The THIRD move is answered by the falsification schedule, not by the "
            "centimetre: the same expression that gives a centimetre at rifle range gives "
            "1.2 km for the Paris Gun, and a claim that has to be true only below a "
            "threshold it cannot name is the one making the special plea. Do not let the "
            "small-arms concession migrate to a footnote — it is the most credible "
            "sentence on the page, and it is what earns the rest."),
    ),

    straw_man=dict(
        identified=True,
        detail=("The chapter treats the absence of the word from a shelf of manuals as "
                "proof of bad faith rather than of a small number: the mainstream position "
                "is characterised as a deception that scientists must 'sell', and the "
                "National Geographic passage as 'simply making things up to fool the "
                "gullible public', on the stated ground that no supporting authority "
                "exists. Two authorities are cited above, dated 1945 and 2016, and both "
                "are public. The imputation of motive is doing the work that the missing "
                "citation search would have done. Note what is NOT a straw man here, "
                "because the distinction matters: the attack on the National Geographic "
                "explanation itself is fair. That passage tells the reader a pilot flying "
                "straight from Portland, Oregon would end up near New York, which is a "
                "great circle on a Mercator projection misreported as a Coriolis "
                "deflection, which the Coriolis-force reference article "
                "cited in the sources warns against explicitly. A bad popular explanation was correctly identified; the "
                "conclusion drawn from it does not follow.")),

    compression=dict(
        assessed=True, drifted=True,
        list_phrasing="Ballistics ignore rotation. / Artillery stationary calculations. / Artillery geocentric mils.",
        source_wording=("“In actual fact, however, regardless of which direction cannons are "
                        "fired, the distance covered is always the same.” (Dubay, proof 24) — "
                        "and “you will look in vain for any mention of Coriolis effect in any "
                        "military artillery or sniper instruction manual … no soldier has ever "
                        "been instructed to consider the Coriolis effect of a spinning Earth” "
                        "(Hendrie 2016, ch. 9, p. 113)."),
        drift_type="unsourced_addition",
        note=("<strong>Take the middle item first, because it is the unusual result.</strong> "
              "&ldquo;Ballistics ignore rotation&rdquo; does <em>not</em> overstate its sources. "
              "If anything the traffic runs the other way: Dubay asserts the range is "
              "&ldquo;always the same&rdquo; whatever the direction of fire, and Hendrie asserts "
              "it of <em>any</em> military manual and of <em>every</em> war ever fought, with a "
              "personal warrant attached. There is no hedge here to drop. This review has found "
              "the compressed version firmer than the original in almost every argument it has "
              "checked; on this one the compression is the mildest statement in the chain, and "
              "the honest finding is that the source is where the overreach lives.<br><br>"
              "<strong>Of the other two items, one is an addition and one is not.</strong> "
              "&ldquo;Artillery geocentric mils&rdquo; is the list&rsquo;s own vocabulary: the "
              "word <em>mils</em> is not located anywhere in the archive.org OCR text of either "
              "book searched for this entry, and whatever the phrase was meant to convey &mdash; "
              "the wording does not settle it &mdash; it did not come from these sources. "
              "&ldquo;Artillery stationary calculations&rdquo; is <em>not</em> an addition. It is "
              "not in proof 24 of <em>200 Proofs</em>, which is where a check against Dubay alone "
              "would stop; it is in Hendrie, at p. 113, where the artillery officers who on a "
              "spinning Earth would be &ldquo;trained to consider the spin of the earth in making "
              "their calculations for accurate firing&rdquo; are said not to be. Four words for "
              "one sentence, and nothing added.<br><br>"
              "<strong>And this is the part worth the reader&rsquo;s time.</strong> Both "
              "statements are <em>true</em>, and both convict the cluster they sit in. Firing "
              "tables really are computed on a stationary Earth: <code>NO ROTATION OF THE "
              "EARTH</code> is one of the standard conditions listed in figure 7-1 of TC 3-09.81 "
              "(2016), in the same list as <code>NO WIND</code>, which nobody reads as a denial "
              "that wind exists. And "
              "the artillery angular unit really is the mil: it is the unit in which Table I "
              "publishes <em>the correction to deflection for the rotation of the earth</em>, "
              "tabulated for every 10&deg; of latitude from 0&deg; to 70&deg; north or south. The two "
              "details that make the claim sound technical are the two details that answer "
              "it.<br><br>"
              "<strong>The refutation answers the sources, not the fragments:</strong> it grants "
              "Dubay&rsquo;s east&ndash;west null at full strength and explains it (Galilean: the "
              "naive version predicts an east/west range ratio near 23:1, where the real "
              "residual shifts the range by about 0.36%), grants Hendrie&rsquo;s sniper "
              "manual and his firearms testimony outright, grants that the word <em>Coriolis</em> "
              "is not located in the 2016 artillery manual searched for this entry, and then answers the strongest version of the argument "
              "&mdash; Riccioli&rsquo;s 1651 one &mdash; on its own ground.")),

    verdict_challenge=dict(challenged=False, proposed_verdict=None, reasoning=None),

    people=["PER-DUBAY"],
    related=["A06", "A08", "A09", "A10", "A13", "A17", "R08"],

    sources=[
        dict(label="TC 3-09.81, Field Artillery Manual Cannon Gunnery, HQ Dept of the Army, "
                   "13 April 2016 — para 3-63 lists “Rotation of the earth” among deviations "
                   "from standard conditions affecting range and deflection; paras 7-20 to 7-24 "
                   "describe Table H (range correction, by azimuth and latitude) and Table I "
                   "(“the correction to deflection in mils, for the rotation of the earth”, "
                   "tabulated every 10° of latitude, 0°–70° N or S)",
             url="https://armypubs.army.mil/epubs/DR_pubs/DR_a/pdf/web/tc3_09x81.pdf"),
        dict(label="FM 6-40, War Department Field Manual, Field Artillery, Gunnery (1945) — "
                   "“rotation of the earth tables for direction and range”, taken “for the "
                   "latitude of the battery (long range weapons only)”",
             url="https://archive.org/details/Fm6-401945"),
        dict(label="FM 4-10, Coast Artillery, Gunnery (1944) — the same rotation-of-the-earth "
                   "tables in the coast-artillery firing tables; corroboration only",
             url="https://archive.org/details/FM_4_10_W_D_C_1944"),
        dict(label="Eric Dubay, 200 Proofs Earth Is Not a Spinning Ball (2015) — proof 24, the "
                   "east/west cannon claim quoted above; proof 20 is the neighbouring vertical "
                   "cannonball item",
             url="https://archive.org/details/200ProofsEarthIsNotASpinningBall"),
        dict(label="Edward Hendrie, The Greatest Lie on Earth (2016), ch. 9 “No Coriolis Effect "
                   "Proves a Stationary Earth”, printed pp. 105–114; the artillery and sniper "
                   "passage at p. 113, with its four pre-1912 artillery-manual citations at "
                   "endnote 116, and the firearms-instructor testimony at p. 114",
             url="https://archive.org/details/the-greatest-lie-on-earth-proof-that-our-world-is-not-a-moving-globe"),
        dict(label="FM 23-10, Sniper Training, HQ Dept of the Army, 17 August 1994 — the manual "
                   "Hendrie's footnote cites; searching its OCR text returns no occurrence of "
                   "the word Coriolis, which is why the small-arms concession is made in our "
                   "own voice",
             url="https://archive.org/details/fm-23-10-sniper-training-1994"),
        dict(label="C. M. Graney, “The Coriolis Effect Apparently Described in Giovanni Battista "
                   "Riccioli's Arguments Against the Motion of the Earth” (arXiv:1012.3642) — "
                   "English rendition of Almagestum Novum II, bk 9, sec. 4, ch. 21, pp. 425, "
                   "426–7, arguments 17 and 19 of Riccioli's 77",
             url="https://arxiv.org/abs/1012.3642"),
        dict(label="C. M. Graney, “126 Arguments Concerning the Motion of the Earth, as presented "
                   "by Giovanni Battista Riccioli in his 1651 Almagestum Novum”, Journal for the "
                   "History of Astronomy 43 (2012) 215–226 (arXiv:1103.2057)",
             url="https://arxiv.org/abs/1103.2057"),
        dict(label="C. M. Graney, “The Coriolis Effect Further Described in the Seventeenth "
                   "Century”, Physics Today 70(7):12 (2017) — Dechales, Cursus seu Mundus "
                   "Mathematicus (1674), making the same argument against Earth's rotation",
             url="https://arxiv.org/abs/1611.07912"),
        dict(label="Riccioli, Almagestum Novum (Bologna, 1651) — e-rara scan",
             url="https://www.e-rara.ch/zut/content/pageview/140188"),
        dict(label="Paris Gun — the 120 km bombardment of 1918, for which “the Coriolis "
                   "effect—the rotation of the Earth—was substantial enough to affect trajectory "
                   "calculations”",
             url="https://en.wikipedia.org/wiki/Paris_Gun"),
        dict(label="Coriolis force — the ~2.8 in figure for a 1,000-yard northward shot at "
                   "Sacramento's latitude used to cross-check the arithmetic here, and the "
                   "standing warning against confusing Coriolis deflection with the curvature "
                   "of a great circle drawn on a Mercator projection",
             url="https://en.wikipedia.org/wiki/Coriolis_force"),
        dict(label="Rowbotham (“Parallax”), Zetetic Astronomy: Earth Not a Globe (1865), Project "
                   "Gutenberg #69892 — searched for this entry; the gunnery vocabulary is not "
                   "located in it and the only projectile passage is the vertical air-gun",
             url="https://www.gutenberg.org/ebooks/69892"),
        dict(label="Carpenter, One Hundred Proofs That the Earth Is Not a Globe (1885), Project "
                   "Gutenberg #55387 — proofs 42–44, the Victorian projectile items, which "
                   "argue from the Earth's translational motion rather than its rotation",
             url="https://www.gutenberg.org/ebooks/55387"),
        dict(label="The specimen: “435 Pieces of Evidence The Earth is Not A Spinning Ball”, "
                   "withthesun33.com/about-1 (Andy J Consoli) — re-fetched 2026-08-11; items "
                   "114, 258 and 407 confirmed verbatim",
             url="https://withthesun33.com/about-1"),
    ]),
}
