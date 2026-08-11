# -*- coding: utf-8 -*-
"""Batch 11 — A21. "Satellites and geostationary orbits reinterpreted in an Earth-fixed frame."

Three items: 15 "Geostationary satellites fit rotating sky model.", 96 "Satellite
stability Earth-frame.", 109 "Geostationary satellites reinterpretation."
Verdict STANDARD PHYSICS, kept. No verdict_challenge; the attribution is challenged
instead, in `record_problems` — see 8 below.

Research notes for whoever picks this up next.

1. THE RECORD'S ATTRIBUTION DOES NOT SURVIVE CONTACT, AND IT IS THE MAIN FINDING OF
   THIS PASS. clusters.py A21 carries originator="Samuel Shenton",
   originator_work="International Flat Earth Research Society", year="1957", and a note
   quoting Shenton's Sputnik line about sailing round the Isle of Wight. Four separate
   problems, each checkable:
     (a) ANACHRONISM. Two of the three items are about GEOSTATIONARY orbits. The first
         successful geosynchronous satellite was Syncom 2, 26 July 1963; the first
         geostationary one Syncom 3, 19 August 1964 (Wikipedia, "Syncom"). A claim dated
         1957 cannot be about a class of orbit that did not have an occupant for six more
         years. Shenton died in 1971, so a later remark of his is not impossible — but
         our record does not cite one.
     (b) OUR OWN DATE IS INTERNALLY INCONSISTENT. Schadewald, The Plane Truth ch. 9,
         which is the source people.py cites for PER-SHENTON, gives the founding as
         "Shenton and William Mills founded the International Flat Earth Society on
         December 20, 1956." people.py already says 20 December 1956. The cluster says
         1957. (The only 1957 in that chapter is Sputnik, and Mills's son's death.)
     (c) THE QUOTED LINE IS NOT LOCATED IN THE CHAPTER WE CITE FOR IT. "Isle of Wight"
         does not appear anywhere in Schadewald ch. 9 as retrieved 2026-08-11; a
         string search of the full chapter text returns zero hits for "Wight". What
         that chapter does say about satellites is one clause: with the space
         programme "he attracted a lot of reporters eager to hear him explain the
         satellites allegedly orbiting the earth". The Isle of Wight remark is widely
         attributed to Shenton in the popular literature; this pass did not verify it,
         and it is not in the source our own note leans on. Do not repeat it as sourced.
     (d) WRONG ARGUMENT, WRONG LINEAGE. Shenton's move — circumnavigation of a body
         proves nothing about its shape — is a DENIAL that satellites are evidence for a
         globe. Items 15/96/109 are the opposite speech act: a positive claim that
         satellite behaviour is what an Earth-fixed, rotating-heavens model predicts.
         That is Tychonian material, requiring an equator and Newtonian gravity, and it
         has a documented textual home (2 below). The two claims are not the same claim.
   RECOMMENDATION, filed and NOT applied here (this agent owns one file): withdraw
   A21's originator to None and record the ancestor in the note, the E13/E08 shape.
   Do NOT substitute Selbrede as originator — see 3.

2. WHERE THE ARGUMENT ACTUALLY LIVES. Galileo Was Wrong carries it in at least five
   places, and they are not all the same argument:
     - Vol. I scan (archive item GallileoWasWrong), ch. 1, printed p. 37: geosynchronous
       satellites listed among phenomena which "do not prove, in the least, the
       heliocentric system". A DENIAL of evidential force.
     - Vol. I ch. 7, printed p. 468: a long block quotation from Dennis Sciama, The Unity
       of the Universe (1959), pp. 85–89 per the book's footnote 907 — the 24-hour
       satellite that "would always be above the same point of the earth's surface",
       an observer seeing "a body at rest above his head, hovering with no visible means
       of support!" That is a mainstream Machian physicist illustrating why Newton's
       second law needs an inertial frame, quoted accurately.
     - Vol. I ch. 10, printed pp. 607–612: the Machian machinery. Einstein's 1913 letter
       to Mach, Thirring 1918, Orwig 1978, Grøn & Eriksen 1989, all in the footnotes,
       with an acknowledgement "My thanks to Martin Selbrede for these sources and
       analysis". Also Thirring's axial component (5 below).
     - Vol. I ch. 11, printed p. 662: Helmut Posch on Hildegard of Bingen — "Therefore,
       geostationary satellites travel against the rotation of space in order to appear
       stationary [to us]." This is the sentence item 15 most nearly paraphrases, and it
       is a translator's gloss on a twelfth-century vision, not a physics claim.
     - Vol. II scan, Appendix 1, printed pp. 630–648: the Selbrede essay. This is the
       strongest and most technical form and it is what the entry answers.

3. THE ESSAY, AND WHY IT IS AN ANCESTOR AND NOT AN ORIGIN. Appendix 1 of the Vol. II
   scan reprints "Geocentricity's Critics Refuse to Do Their Homework" by Martin
   Selbrede. The book's own footnotes 1155 and 1158 and its bibliography give the
   original venue: Martin G. Selbrede, "Geocentricity's Critics Refuse to Do Their
   Homework," The Chalcedon Report, 1994, pp. 11–12, described there as a 12-page
   rebuttal of Michael Martin Nieto of Los Alamos, "hired by Gary North … to attempt to
   refute geocentrism". The Chalcedon Report issue was not consulted for this pass; the
   1994 date is the book's, and the essay's own citations (Bussey, Phys. Lett. A 176,
   1993; Novello et al., GRG 25:137, 1993) put the writing no earlier than 1993, which
   is consistent. BUT Selbrede disclaims origination in the essay itself: the equatorial
   restriction "has been asserted in books, in journals, on audiotapes, and videotapes",
   and the argument was already on a videotape sent to North in 1992. So: documented
   ancestor, 1994, named. Origination NOT established. Record it that way.

4. THE HEDGE RULE, BOTH DIRECTIONS, AND THIS ONE IS DELICATE.
   The trap on OUR side is real here. The easy, self-serving move is to quote the ch. 1
   line — satellites "do not prove, in the least, the heliocentric system" — and say the
   source only ever claimed a negative. That would be quoting up to the disjunction and
   stopping. Six hundred pages later the same book prints, in Selbrede's voice: "This
   motion of the firmament is evidenced in the Sagnac effect, the well-known Coriolis
   forces, and by geosynchronous satellites." That is a flat evidential claim, and it is
   the sentence the entry quotes and answers. Do not soften it.
   The trap on THEIR side is not in the wording at all — item 109 literally says
   "reinterpretation", which is more honest than most of the list. The drift is in the
   speech act (a permission published as proof item 15 of 461) and in three restrictions
   the source states and the items drop: equator only, Newton's own height, and
   satellites fall if the heavens stop. drift_type = force_upgraded, on the R01
   calibration; the compression note says out loud that the enum choice is contestable
   and why we still record a drift.
   AND THE TRAP ON OUR SIDE AGAIN, CAUGHT AND FIXED 2026-08-11. `passage.quote` stopped
   at "the satellites would fall to the earth", and the sentence immediately after it in
   the scan is Selbrede's answer to the reading the gloss was building: "But when the
   heavens are postulated to be in motion, it is Dr. Nieto's equations that are
   deficient, not ours." Trimming there is the exact move this project convicts its
   subject of. The quote plus that sentence runs 67 words, over the 60-word fair-use
   ceiling for an in-copyright book, so the D03 remedy is used instead: the excerpt is
   left as it is and the reversing sentence is quoted IN FULL in the gloss, granted on
   its merits, and answered on the point that actually carries the entry (the rotation
   rate is an input — section 6 here, section 1 of the refutation). The gloss's old
   "gives the whole game away" also went; it claimed more than the paragraph supports.
   The compression block had a related defect: render.py prints list_phrasing above
   source_wording and then the drift label, and the visible pairing showed a source
   ASSERTING evidential force above a list item that only says "fit" — which reads as
   the opposite of `force_upgraded`. The permission that licenses the label, the p. 637
   "by definition" thesis, was only in the note. It is now in source_wording, where the
   reader can see the label's own evidence.

5. THE TECHNICAL CHAIN, ALL VERIFIED 2026-08-11 BY BIBLIOGRAPHIC LOOKUP (Crossref):
     - Thirring, Phys. Zeit. 19:33 (1918) + correction 22:29 (1921) — a rotating mass
       shell induces Coriolis-like and centrifugal-like forces inside. As cited.
     - Brill & Cohen, Phys. Rev. 143:1011–1015 (1966). Real, as cited.
     - Orwig, "Machian effects in compact, rapidly spinning shells", Phys. Rev. D
       18:1757–1763 (1978). Real; the book quotes its abstract correctly.
     - Grøn & Eriksen, "Translational inertial dragging", Gen. Rel. Grav. 21:105–124
       (Feb 1989), doi 10.1007/BF00761081. Real; journal, volume, issue and page range
       exactly as the REPRINTED ESSAY gives them (Vol. II, printed p. 633: "General
       Relativity and Gravitation, Volume 21, No. 2, 1989, pgs. 105-124"). Vol. I
       footnote 1168 gives the same paper as "Vol. 21, No. 2, 1989, pp. 109-110" —
       the pages of the quotation, not of the article.
   HOW PRECISE THE BOOK'S CITATIONS ACTUALLY ARE, checked 2026-08-11 against both
   scans, because the first draft of this entry credited them with more than they
   carry and the correction is now applied to tldr, gloss and refutation:
     - Orwig: NO volume number in the three places the book cites him. Vol. I fn 1168
       and the Vol. I bibliography both read "Physical Review D, 1757-1763, 1978";
       the reprinted essay names him with a year only ("Orwig (1978)"). Page range
       right, volume absent. (True citation: Phys. Rev. D 18, issue 6, 1757–1763.)
     - Brill & Cohen: Vol. I fn 1188 reads "Physical Review, 143, Issue 4, March 25,
       1966, pp. 1012, 1014" — volume, issue and date right; the pages are quote
       locations inside an article running 1011–1015.
     - Thirring: "Physikalische Zeitschrift 19, 33, 1918" — volume and opening page,
       not a range.
   So the defensible claim is: everything the book PRINTS checks out, and the two
   article ranges it gives are right. Not "cited at the right journal, volume and
   page range", which is what the entry said before 2026-08-11.
     - Obukhov, "Rotation in cosmology", GRG 24:121–128 (1992). Real, as cited.
   WHAT WAS AND WAS NOT CHECKED. Bibliographic existence and location: all five, via
   Crossref, 2026-08-11. The papers themselves were NOT opened; the internal page
   attributions the book gives (G&E at pp. 109-110 and 117-118) are its own. What can
   be said about quotation fidelity is this and only this: the G&E passages appear
   word for word in two different editions of the book, Vol. I ch. 10 footnotes and
   Vol. II Appendix 1, which is as much of a cross-check as two scans allow.
   THE CITATIONS ARE GOOD. Say so, at that strength and no higher. An agent who tries
   to win this on "they made the papers up" will lose, publicly, to a five-minute check.
   THE ONE THE BOOK GETS BACKWARDS: Thirring's 1918 interior field carries, besides the
   Coriolis and centrifugal terms, an extra axial term — in modern notation the
   2(ω·r)ω piece of a = −2d1(ω×v) − d2[ω×(ω×r) + 2(ω·r)ω] (Wikipedia, "Frame-dragging",
   which cites Pfister & Braun for the resolution). Vol. I pp. 611–612 treats that term
   as a discovery and builds the 23.5° obliquity on it. Pfister & Braun, CQG 2:909–918
   (1985), showed the correct centrifugal force is induced once the shell is allowed to
   deform instead of being held rigid — i.e. the extra term is an artefact of the
   idealisation. Give them Thirring's main result; take the mechanism built on his
   error.

6. THE ARITHMETIC, REPRODUCED HERE 2026-08-11.
   (a) r_GEO = (GM/ω²)^(1/3) with GM = 3.986004418×10^14 m³/s² and ω = 7.2921150×10^−5
       rad/s: 4.216417×10^7 m = 42,164 km, altitude 35,786 km, orbital speed ωr =
       3.075 km/s. Matches the published figures (Wikipedia, "Geostationary orbit":
       42,164 km, 35,786 km, 3.07 km/s, period 1,436 min = one sidereal day).
   (b) SIDEREAL, NOT SOLAR. Redo (a) with ω = 2π/86,400 s and you get 42,241 km — 77 km
       higher, and a satellite there falls behind the ground by 0.985°/day, i.e. 360° in
       a year. The station-keeping altitude is set by the rotation relative to the STARS.
       This does not discriminate geocentric from heliocentric (the Tychonic firmament
       turns on the sidereal period too) and the entry must not pretend it does.
   (c) THE MACHIAN COINCIDENCE, and it is the best thing in the steelman. For the shell
       formula d1 = 4α(2−α)/((1+α)(3−α)) with α = GM/2Rc², "perfect dragging" (d1 = 1)
       needs α = 1, the shell at its gravitational radius. Put in a Hubble sphere at
       critical density: α = GM/2Rc² = 1/4 exactly (the H² cancels), giving d1 ≈ 0.51.
       Order unity, off by a factor of two. That is a back-of-envelope static-shell
       estimate and NOT a cosmological calculation — say so in the text, because a
       defender who knows FRW will otherwise take the paragraph apart.
   (d) Light cylinder c/ω = 4.111×10^12 m = 27.5 AU. Included only to be honest about
       where the superluminal objection lives, and then to concede it (7 below).

7. THREE ARGUMENTS THAT LOOK GOOD AND MUST NOT BE USED. Written down because each of
   them is the kind of thing that gets a section discredited on the one point where the
   defender is right.
   (a) COSMIC-VORTICITY BOUNDS (Collins & Hawking, Saadeh et al.). They constrain
       rotation of the matter relative to the LOCAL INERTIAL FRAMES. A rigid change of
       chart does not touch that quantity — both descriptions agree the relative
       rotation of distant matter and the local compass of inertia is nil. Deploying
       those limits here would be a category error and a bad one.
   (b) "THE STARS WOULD MOVE FASTER THAN LIGHT." Coordinate speeds exceeding c are not
       forbidden in general relativity, no local observer measures a superluminal
       passage, and the book anticipates the objection explicitly (Vol. II App. 1,
       printed p. 647 — corrected 2026-08-11 from 646; the marker "646" sits at the foot
       of the preceding page: if space can stretch faster than light, why can it not
       rotate faster than light). The analogy is imperfect but the objection as usually stated
       is worse. Leave it.
   (c) "THE MODEL HAS NO FORCE TO HOLD THE SATELLITE UP." That is precisely North and
       Nieto's move as Selbrede reports it, and it is answered by Einstein's own letter
       to Mach and by Thirring. It is the SURFACE bust and it loses.
   (d) AND THE ONE THAT HAD LEAKED IN, FIXED 2026-08-11. `straw_man.detail` answered
       "proof of a moving earth is proof general relativity is a myth" by saying the
       Earth's rotation relative to the local inertial frames "is measurable,
       frame-independent, and measured, by ring-laser gyroscopes and by the Foucault
       pendulum" — and stopped there. Strictly true, and it reads as an evidential
       claim, which is (a) in a new suit: under perfect dragging the compass of inertia
       turns with the heavens, so the essay predicts that measurement too, and says so
       at printed p. 650 ("the rotating heavens were dragging Foucault pendula and
       weather systems around"). The box now grants that in its own voice before making
       its narrow point, which is the only point it needs: establishing the relative
       rotation would leave general relativity where it was, so the threat in the
       second sentence is empty.

8. VERDICT. STANDARD PHYSICS, kept, and the reasoning is worth recording because the
   neighbouring cluster carries a different verdict on adjacent material. R08 ("practical
   systems use Earth-fixed coordinates, therefore Earth is fixed", item 244) is
   MISLEADING because its item states the inference. A21's three items state a fit, a
   frame and a reinterpretation, and every one of those is true: in the Earth-fixed
   rotating frame a geostationary satellite is at rest, and general covariance licenses
   the chart. What fails is the use of a true, non-discriminating statement as proof item
   15 of 461, which is what STANDARD PHYSICS is for on this page. Boundary noted rather
   than hidden: a reviewer who wants A21 at MISLEADING has a case, and it should be made
   against the rubric, not by rewriting this entry.

9. DEFECTS IN OUR OWN RECORD, reported up, NOT edited here. Full list in
   record_problems: the Shenton attribution and its four sub-faults (1 above); the
   cluster note's unsourced Isle of Wight quotation; real_source=None though the book's
   own treatment rests on Sciama 1959, Thirring 1918 and Grøn & Eriksen 1989; and the
   absence of a PER-SELBREDE record, which is why `people` here carries PER-SUNGENIS
   only. Until the cluster edit lands, the card will render "Samuel Shenton, 1957" above
   a gloss about a 1994 essay; the published prose below therefore names no originator
   at all, and claims only what it can show about the text.

10. SCAN PROVENANCE — READ THIS BEFORE CITING A PAGE. Two archive.org items were used
   and they are different editions with different chapter numbering and pagination for
   OVERLAPPING content:
     - item GallileoWasWrong (the CD-ROM issue works.py records as Vol. I): ch. 10
       Machian material at pp. 607–612, ch. 11 "Hildegardian Geocentrism" at p. 662,
       ch. 12 technical/summary chapter at pp. 719–720, appendices past p. 1024.
     - item GalileoWasWrongTheChurchSungenisRobertA.Bennett4276 (Vol. II, 7th ed. 2013,
       chs 7–13): the same technical/summary material is "Chapter 10: Technical and
       Summary Analysis of Geocentrism" at p. 167, Hildegard is ch. 12, and Appendix 1
       runs from p. 623. The etherometry paragraph about a satellite's translational
       speed being zero "at the geostationary distance of 22,000 miles" appears in BOTH,
       at p. 167 of one and pp. 719–720 of the other. Do not merge the page ranges, and
       do not assume a chapter number transfers between the two.
   Neither was checked against a print copy and the locator says so. OCR notes: the
   quoted sentence prints "geostationarv" for "geostationary" and the running head
   mangles Selbrede's name ("Sclbrcdi", "Sell) rede"); both are silently corrected in
   the quotation and flagged here.
"""

ENTRY = {

"A21": dict(

    tldr=("In an Earth-fixed frame a geostationary satellite really does sit still — that is "
          "ordinary orbital mechanics, and the relativity papers the source leans on for it are "
          "real, with every journal, volume and year the book gives for them checking out. The "
          "price is stated in the same "
          "appendix: the satellite has to be over the equator, at the height Newton's arithmetic "
          "already gives, and it would fall if the heavens stopped turning. Those are three "
          "properties of a spinning globe rewritten in rotating coordinates — and the same list "
          "elsewhere insists the surface is flat."),

    passage=dict(
        work="WRK-SUNGENIS-2006",
        pd=False,
        locator=("Vol. II, Appendix 1, in the reprinted essay “Geocentricity's Critics Refuse to "
                 "Do Their Homework” by Martin Selbrede, at printed p. 648 of the archive.org OCR "
                 "text (item GalileoWasWrongTheChurchSungenisRobertA.Bennett4276; the project "
                 "records this scan as Vol. II, 7th ed., 2013). The OCR prints “geostationarv” for "
                 "“geostationary”, corrected here. Not checked against a print copy; a second "
                 "archive scan (item GallileoWasWrong) paginates overlapping material differently"),
        quote=("This motion of the firmament is evidenced in the Sagnac effect, the well-known "
               "Coriolis forces, and by geosynchronous satellites (or, in a more Tychonian vein, "
               "geostationary satellites). In the geocentric model, we agree that if the heavens "
               "ceased their rotation, the satellites would fall to the earth."),
        gloss="""<p><strong>Read the second sentence with the first.</strong> The claim is evidential &mdash; satellites <em>evidence</em> the firmament&rsquo;s daily rotation &mdash; and it is stated flatly, so nobody should pretend the source only ever denied that satellites prove anything. But it arrives attached to a conditional that names what the model is resting on: the satellite stays up <em>because</em> the heavens turn, and would fall if they stopped.</p>

<p>The essay does not leave the concession there, and neither should we. The excerpt above stops one sentence short, because carrying on would take it past the 60-word ceiling this project keeps for quoting an in-copyright book; the sentence it stops short of is Selbrede turning the concession round: <em>&ldquo;But when the heavens are postulated to be in motion, it is Dr. Nieto&rsquo;s equations that are deficient, not ours.&rdquo;</em> That is fair as far as it goes. The conditional is counterfactual in his model, and he is answering a critic who, on his account of him, had argued that a satellite could not stay up over a fixed Earth at all. The objection here is not that the conditional is false. It is that the one quantity the whole arrangement then hangs on &mdash; the rate at which the heavens turn relative to the ground &mdash; is an input: read off the rotating-globe solution and put in by hand, together with the equator and the height that go with it. That is section 1 of the refutation below, and it is where this entry puts its weight.</p>

<p><strong>Whose argument this is, and where it came from.</strong> The essay is Martin Selbrede&rsquo;s, written against a critique that Gary North commissioned from Michael Martin Nieto of Los Alamos; Sungenis and Bennett reprint it as Appendix 1 and, in their own footnotes and bibliography, give the original as <em>The Chalcedon Report</em>, 1994, pp. 11&ndash;12. Its physics is not homemade. It runs on Einstein&rsquo;s 1913 letter to Mach, on Thirring&rsquo;s 1918 rotating-shell paper, on Orwig&rsquo;s <em>Phys. Rev. D</em> 18:1757 (1978) and on &Oslash;. Gr&oslash;n and E. Eriksen, <em>&ldquo;Translational inertial dragging&rdquo;</em>, <em>General Relativity and Gravitation</em> 21:105&ndash;124 (1989). Every one of those exists, and every bibliographic detail the book prints for them checks out &mdash; checked here against Crossref. Said at its true strength and no higher: where the book gives an article page range it is right (Gr&oslash;n and Eriksen at 105&ndash;124), but it gives no volume number for Orwig at all &mdash; <em>Physical Review D</em>, 1757&ndash;1763, 1978, in the Vol. I footnote and again in the Vol. I bibliography &mdash; Thirring it gives by volume and opening page rather than by range, and the page numbers it prints inside Brill and Cohen and, in Vol. I, inside Gr&oslash;n and Eriksen are quote locations, not article ranges. The papers themselves were not opened for this entry, so those internal locations are the book&rsquo;s; what can be said for them is that the Gr&oslash;n and Eriksen quotations appear word for word in two different editions of the book, Vol. I&rsquo;s chapter 10 footnotes and this appendix. The footnote at Vol. I p. 607 credits Selbrede with supplying the references.</p>

<p><strong>Three restrictions the source states and the list does not inherit.</strong> At printed p. 635 of the same essay: geostationary satellites can sit &ldquo;only over the equator, and at the same prescribed height as that indicated by the Newtonian methods Dr. North favors&rdquo; &mdash; the equator, and Newton&rsquo;s own number. At p. 637 the essay states its thesis outright: &ldquo;it is impossible to launch an attack on geocentricity on the basis of general relativity, by definition.&rdquo; And at p. 648, the conditional quoted above. A result that holds <em>by definition</em>, at a height somebody else&rsquo;s theory already fixed, over an equator, is a demonstration that the two descriptions agree. That is what the essay set out to show, and it shows it.</p>

<p><strong>The book&rsquo;s other satellite passages, for anyone following the chain.</strong> Its opening chapter (Vol. I scan, ch. 1, printed p. 37) lists geosynchronous satellites among phenomena which &ldquo;do not prove, in the least, the heliocentric system&rdquo; &mdash; the negative form. Vol. I ch. 7, printed p. 468, quotes the geosynchronous satellite &ldquo;hovering with no visible means of support!&rdquo; from Dennis Sciama&rsquo;s <em>The Unity of the Universe</em> (1959), where it is an illustration of why Newton&rsquo;s second law needs an inertial frame. Vol. I ch. 11, printed p. 662, has Helmut Posch glossing a vision of Hildegard of Bingen: &ldquo;Therefore, geostationary satellites travel against the rotation of space in order to appear stationary [to us].&rdquo; The sentence quoted above is the technical version of the same move, and it is the one worth answering.</p>

<p><strong>What this passage is being cited as.</strong> The earliest text located in this review that states the argument in the form the three items take, with a date and a named author. It is an ancestor, and the essay itself declines to be an origin: the equatorial restriction, Selbrede writes, &ldquo;has been asserted in books, in journals, on audiotapes, and videotapes&rdquo;, and the material was already on a videotape sent to his critic in 1992. Origination is not established here and is not claimed.</p>"""),

    steelman=dict(
        description="""<p><strong>SURFACE (weak &mdash; do not use).</strong> &ldquo;If the Earth were not turning, a geostationary satellite would have nothing holding it up, so it would fall.&rdquo; This is exactly the objection the source was written to answer, and it loses to Einstein&rsquo;s own words. Einstein to Mach, 25 June 1913: rotate a heavy shell of matter about an axis through its centre and &ldquo;a Coriolis force arises in the interior of the shell, that is, the plane of a Foucault pendulum is dragged around.&rdquo; There is no free win here.</p>

<p><strong>DEEPER.</strong> &ldquo;It is only a change of coordinates.&rdquo; True, and incomplete, because it concedes the point in the form the defender wants: yes, the Earth-fixed rotating frame is a legitimate chart, satellite operations use one (ITRF/ECEF) every day, and general covariance guarantees the field equations hold in it. Stopping there invites the reply <em>then you agree with us</em>.</p>

<p><strong>KERNEL.</strong> The specific true thing this tradition found is a real and respectable result, and it is stronger than the version in the book. A rotating mass shell does induce centrifugal- and Coriolis-like fields in its interior (Thirring 1918); in the limit where the shell approaches its gravitational radius the interior inertial frames are dragged round <em>rigidly</em> with it (Brill &amp; Cohen 1966; Orwig 1978; quoted by Gr&oslash;n and Eriksen as &ldquo;perfect dragging&rdquo;). And the numbers are not absurd. For an interior dragging coefficient <em>d</em><sub>1</sub> = 4&alpha;(2&minus;&alpha;)/((1+&alpha;)(3&minus;&alpha;)) with &alpha; = <em>GM</em>/2<em>Rc</em>&sup2;, perfect dragging needs &alpha; = 1; a Hubble sphere at critical density gives &alpha; = 1/4 exactly (the <em>H</em>&sup2; cancels) and <em>d</em><sub>1</sub> &asymp; 0.51 &mdash; the right order, off by a factor of two. That is a static-shell estimate and not a cosmological calculation, and it is offered as nothing more; but it is why Einstein, Sciama and a good deal of subsequent literature took cosmological inertial dragging seriously, and it is why the satellite question has a real answer inside a geocentric chart.</p>""",
        why_it_doesnt_save_claim="""<p>Because perfect dragging is <em>the statement that the two descriptions cannot be told apart</em>. It is not a rival account that happens to fit; it is the condition under which no observation distinguishes &ldquo;Earth turns in a fixed cosmos&rdquo; from &ldquo;cosmos turns about a fixed Earth&rdquo;. The better the dragging works, the less there is to detect &mdash; which is why the essay can say its conclusion follows &ldquo;by definition&rdquo;. A conclusion that follows by definition is not evidence for anything, and cannot be item 15 in a list of proofs.</p>

<p>And notice what has to be imported before the dragging account can start. The shell has to rotate at one particular rate, once per sidereal day. The satellite has to sit over the equator &mdash; a plane defined by that rotation. Its radius has to be 42,164 km from the Earth&rsquo;s centre, which is <em>(GM/&omega;&sup2;)</em><sup>1/3</sup>, the Newtonian answer, as the essay concedes in as many words. Nothing in the Machian picture supplies any of those three; they are read off the rotating-globe solution first and then re-described. The geocentric frame is a translation, and it is a translation that arrives after the original.</p>"""),

    refutation="""<p><strong>The concession comes first, because it is large and it is permanent.</strong> A geostationary satellite is at rest in the Earth-fixed rotating frame. That frame is a legitimate coordinate system; general relativity places no bar on writing the field equations in it; a rotating shell of matter really does induce Coriolis-like and centrifugal-like fields inside itself, as Thirring showed in 1918 and as Brill and Cohen, Orwig, and Gr&oslash;n and Eriksen developed afterwards. Every paper the source cites for this exists &mdash; Thirring 1918, Brill and Cohen 1966, Orwig 1978, Gr&oslash;n and Eriksen 1989 &mdash; and every bibliographic detail the book prints for them checks out against Crossref: the journals, the years, Thirring&rsquo;s volume and opening page, Brill and Cohen&rsquo;s volume and issue, and the two article page ranges it gives, Gr&oslash;n and Eriksen at 105&ndash;124 and Orwig at 1757&ndash;1763. Two things it does not give, said here so that the compliment is the right size: no volume number for Orwig in the Vol. I footnote, the Vol. I bibliography or the reprinted essay, the three places it cites him; and, inside Brill and Cohen and inside Gr&oslash;n and Eriksen, page numbers that locate the quotations rather than the articles. Those we did not confirm, because the papers themselves were not opened for this entry. Nothing the book prints is wrong. Anyone answering this argument by claiming the citations are invented, or that a stationary-Earth chart is forbidden, is going to lose the exchange in five minutes.</p>

<p><strong>What the verdict ranges over.</strong> Not &ldquo;the satellite would fall.&rdquo; The claim under review is that satellite behaviour is <em>evidence</em> for a rotating firmament about a fixed Earth. It is not, and the reason is visible in the source&rsquo;s own sentence: the satellite stays up <em>because the heavens turn</em>, at a rate that has to be put in by hand, over an equator that rotation defines, at a height Newton&rsquo;s arithmetic already fixed.</p>

<h4>1. The whole argument is one number, and both models share it</h4>

<p>A body in a circular orbit at radius <em>r</em> keeps station over a point on the ground when <em>GM</em>/<em>r</em>&sup2; = &omega;&sup2;<em>r</em>, so <em>r</em> = (<em>GM</em>/&omega;&sup2;)<sup>1/3</sup>. With <em>GM</em> = 3.986004418 &times; 10<sup>14</sup> m&sup3;/s&sup2; and &omega; = 7.2921150 &times; 10<sup>&minus;5</sup> rad/s this returns <strong>42,164 km</strong> from the Earth&rsquo;s centre &mdash; 35,786 km of altitude, orbital speed 3.075 km/s, period 1,436 minutes. (Recomputed here 2026-08-11; the published figures are 42,164 km, 35,786 km and 3.07 km/s.) Rewrite the same physics in coordinates rotating with the ground and the orbital term becomes a centrifugal term; the satellite is then at rest, held by gravity against that term. In the geocentric telling the centrifugal term is supplied by the turning cosmos instead of by the choice of frame. <strong>The three tellings differ in what they say &omega; belongs to. The number is the same in all three, and so is the orbit.</strong></p>

<p>Which is why the source concedes the number. Selbrede, on the same essay&rsquo;s printed p. 635: stable geostationary satellites sit &ldquo;only over the equator, and at the same prescribed height as that indicated by the Newtonian methods Dr. North favors.&rdquo; A model that reproduces its rival&rsquo;s number, at its rival&rsquo;s location, has demonstrated agreement. It has not produced a measurement of its own.</p>

<p>One detail worth having, since the list trades on the word <em>stationary</em>. The station-keeping radius is set by the <em>sidereal</em> day, 86,164.1 s, not the solar day. Redo the arithmetic with a 24-hour period and you get 42,241 km &mdash; 77 km too high, and a satellite parked there drifts west of its slot by 0.985&deg; a day, a full circuit of the Earth in a year. So what a geostationary satellite keeps station with is the sky, not the Sun. That does not discriminate between a turning Earth and a turning firmament, since the Tychonic firmament turns on the sidereal period too, and this page is not going to pretend it does. It does show what the number encodes: a rotation rate measured against the stars, which is the one quantity everybody in this argument agrees about.</p>

<h4>2. Where the argument&rsquo;s own machinery comes from</h4>

<p>The image of the satellite &ldquo;hovering with no visible means of support&rdquo; is not a geocentrist&rsquo;s invention and the book does not pretend otherwise: at printed p. 468 of the Vol. I scan it is a block quotation from Dennis Sciama&rsquo;s <em>The Unity of the Universe</em> (1959), where the point is that Newton&rsquo;s second law only holds if accelerations are measured in an inertial frame, and the satellite is the vivid case. Sciama&rsquo;s conclusion is that inertial frames are what need explaining &mdash; the argument that leads to Machian cosmology, not away from a moving Earth. The same chain runs through Einstein&rsquo;s 1913 letter to Mach and Thirring&rsquo;s 1918 paper. This tradition is quoting the mainstream Machian literature, accurately, and then reporting the equivalence it establishes as a win for one side of it.</p>

<p><strong>One link in that chain the book gets backwards, and it matters because a mechanism is built on it.</strong> Thirring&rsquo;s 1918 interior field contains, besides the Coriolis and centrifugal terms, an extra axial term &mdash; the 2(<strong>&omega;</strong>&middot;<strong>r</strong>)<strong>&omega;</strong> piece &mdash; with no Newtonian counterpart. Vol. I, printed pp. 611&ndash;612, treats that term as a discovery, and proposes it as the cause of the 23.5&deg; obliquity: the axial force &ldquo;keeps bringing the universe back to the equatorial&rdquo; plane. But the extra term is an artefact of holding the shell rigid, and the title of the paper that removed it says as much: Pfister and Braun, <em>&ldquo;Induction of correct centrifugal force in a rotating mass shell&rdquo;</em>, <em>Classical and Quantum Gravity</em> 2:909&ndash;918 (1985). Let the shell deviate from a precisely spherical shape and let its mass density vary &mdash; that is, let it take the shape its own rotation gives it &mdash; and the interior can be made flat, with the correct centrifugal force induced and no axial residue to build a mechanism on. Thirring&rsquo;s main result survives, and the geocentric use of it survives with it. The obliquity mechanism does not: it is built on the part of the 1918 calculation that a later paper removed.</p>

<h4>3. The satellite is not hovering; it is being flown</h4>

<p>&ldquo;Stationary&rdquo; is doing rhetorical work the orbit cannot support. A geostationary satellite left alone does not stay put. Lunar and solar gravity tilt its orbital plane, and an uncorrected satellite reaches an inclination of about 15&deg; in 26.5 years; holding inclination near zero costs roughly <strong>50 m/s of delta-v every year</strong>. The Earth&rsquo;s equator is slightly elliptical, so the satellite also drifts in longitude towards one of two stable points at <strong>75.3&deg;E and 108&deg;W</strong> (with unstable points at 165.3&deg;E and 14.7&deg;W); correcting that costs up to about 2 m/s a year. Solar radiation pressure adds more. Every one of those terms is Newtonian celestial mechanics of an oblate, rotating globe perturbed by the Moon and the Sun; each is computed and budgeted before launch, and burned as propellant across the satellite&rsquo;s working life. The Earth-fixed description inherits all of it unchanged and contributes none of it. That is the shape of the whole argument in one example: it can re-express the answer, and in the geocentric material read for this review it does not derive one.</p>

<p>The same holds for the frame itself. Satellite operations do run in Earth-fixed coordinates, and converting between them and the inertial frame requires Earth-orientation parameters that have to be <em>measured</em>, continuously, because the rotation is not uniform: the excess length of the mean solar day over 86,400 SI seconds ran between about 0.25 and 1 ms across 1999&ndash;2010, and on 29 June 2022 the day came in 1.59 ms short. The IERS publishes UT1&minus;UTC and polar motion for exactly this reason. Read geocentrically, the entire firmament speeds up and slows down by parts in 10<sup>8</sup>, in step with terrestrial weather and the Earth&rsquo;s core, and the rate has to be re-measured and re-broadcast every day so that spacecraft can be flown. That is not a contradiction &mdash; the chart absorbs it, as charts do. It is a statement about which end of the arrangement the explanations are coming from.</p>

<h4>4. What the argument costs its own list</h4>

<p>Follow the concession at p. 635 to where it lands. Geostationary orbit exists <em>only</em> over the equator, and <em>only</em> at 42,164 km from the Earth&rsquo;s centre. An equator is the great circle a rotation axis defines on a sphere; a radius from the centre is a distance from the middle of a solid body. Item 15 is proof number fifteen in a list which elsewhere asserts that long-distance views show a flat horizon (item 43), that radar horizons are flat (217), that mining surveys assume a plane (395) and that railways make no allowance for curvature (386). <strong>The argument at item 15 is a spherical-Earth argument, and it is being used to support the claim that the Earth is not a sphere.</strong> Its authors would say so themselves: the Tychonian tradition holds the Earth to be a globe that does not move, and the satellite reasoning here is unusable without one.</p>

<h4>5. What is left, stated without decoration</h4>

<p>The Earth-fixed frame is legitimate, the dragging literature is real, and the source&rsquo;s use of it is careful enough that its strongest sentence is a claim of exact equivalence: no attack on geocentricity can be launched from general relativity &ldquo;by definition&rdquo;. Agreed &mdash; and the trade runs both ways, which is the part that does not travel. You can have the coordinate freedom or you can have the evidence; the freedom is granted precisely because nothing follows from it. Every quantity the satellite argument uses &mdash; the rotation rate, the equator, the 42,164 km &mdash; is imported from the description it means to displace, and the satellite that is supposed to be hovering unsupported is in fact being held in a slot, against the Moon and the Sun and the Earth&rsquo;s own lumpy equator, at a cost of about fifty metres per second a year.</p>""",

    advocate=dict(
        best_defense=(
            "Four moves, and the first three are yours, not mine. One: you concede the "
            "frame is legitimate. Two: you concede the citations are sound — Thirring, "
            "Orwig, Grøn and Eriksen, checked and correct. Three: you concede that "
            "perfect dragging makes the two descriptions indistinguishable. Item 15 says "
            "geostationary satellites FIT the rotating sky model. You have just spent "
            "two thousand words agreeing that they do. Where is the refutation? "
            "Four, and this is the real complaint: you have taken a defensive essay — "
            "written because two critics claimed our satellites would fall out of the "
            "sky — and you are marking us down for winning it. Selbrede stated the "
            "equatorial restriction and the Newtonian height himself, in print, in 1994; "
            "now you produce our own doctrine as though you had caught us in something. "
            "That is not provenance work, it is theatre. Nor is the Sciama point better: "
            "the quotation is accurate, in context, and used for exactly what Sciama "
            "used it for. Telling your readers where a true premise came from is a "
            "genetic fallacy with footnotes. And your closing flourish is a straw man of "
            "the whole tradition: your quarrel about whether the Earth is flat is with "
            "whoever compiled somebody's webpage. We say the Earth is a sphere. We have "
            "said so for four hundred years. Take it up with them."),
        survives=4,
        preemptive=(
            "Four, and the number is driven by moves three and four, not by the physics. "
            "Five specific things must stay in the body and one must stay out. "
            "(a) The equivalence answer must be stated in our own voice and stay adjacent "
            "to the concession — 'perfect dragging is the statement that the two "
            "descriptions cannot be told apart', and 'a conclusion that follows by "
            "definition is not evidence'. If an editor moves that sentence away from the "
            "concession, the section reads as agreement. "
            "(b) The equatorial restriction must be attributed to Selbrede EVERY time it "
            "appears, with the page, and never phrased as a discovery of ours. The text "
            "does this; keep it. Its force is not that we caught them, it is that the "
            "restriction is incompatible with the list carrying the item. "
            "(c) The lineage point must stay pinned to the LIST and not to the "
            "Tychonians, because on this the defender is right: they hold the Earth is a "
            "globe, and saying otherwise would be the misrepresentation we exist to "
            "object to. The section already names items 43, 217, 386 and 395 as the "
            "counterparties. Never write 'flat-earthers claim geostationary satellites'. "
            "(d) The Sciama paragraph must argue that the equivalence Sciama establishes "
            "is the thing being misused, not that the source misquoted him — it did not. "
            "If it ever shortens into 'they took it from a mainstream physicist', delete "
            "it; at that length it IS a genetic fallacy. "
            "(e) Pfister and Braun must be presented as removing the obliquity mechanism "
            "only, with Thirring's main result explicitly granted in the same sentence. "
            "And the thing that must stay OUT: do not deploy cosmological vorticity "
            "bounds (Collins and Hawking; Saadeh et al.) or the superluminal-firmament "
            "objection. Both are category errors against a chart change, the book "
            "anticipates the second, and a defender who knows either one gets to "
            "discredit the section on the one point where he is right."),
    ),

    straw_man=dict(
        identified=True,
        detail=("At printed p. 637 the essay concludes: “it is impossible to launch an attack on "
                "geocentricity on the basis of general relativity, by definition. Proof of a moving "
                "earth is simultaneously proof that general relativity is a myth.” The second "
                "sentence misdescribes the position it is answering. No physicist claims the Earth "
                "rotates in the pre-relativistic absolute sense the sentence assumes; the claim is "
                "that the Earth rotates relative to the local inertial frames — the compass of "
                "inertia — and that quantity is measurable, frame-independent, and measured, by "
                "ring-laser gyroscopes and by the Foucault pendulum the essay itself discusses. "
                "That measurement is not itself a point against the essay and is not offered as "
                "one: what it returns is the relative rotation of the ground and the local "
                "compass of inertia, both accounts predict it, and they differ only over which "
                "of the two to call at rest — this essay's own answer, at printed p. 650, is that "
                "the rotating heavens drag the pendulum round. The point here is narrower. "
                "Establishing that relative rotation would leave general relativity exactly where "
                "it was, so the second sentence's threat is empty. The "
                "characterisation of the critics is a separate matter and is not scored here: "
                "Michael Martin Nieto's essay and Gary North's publication were not obtained for "
                "this pass, so what they argued is known only from the reply, and the reply's "
                "account of them is not treated as established. Two things the essay is NOT doing "
                "wrong, for the avoidance of doubt: its Grøn and Eriksen quotations appear word "
                "for word in both scanned editions of the book, the paper itself not having been "
                "opened here, and its use of Sciama's hovering-satellite illustration "
                "is accurate and in context.")),

    compression=dict(
        assessed=True, drifted=True,
        list_phrasing="Geostationary satellites fit rotating sky model.",
        source_wording=("“This motion of the firmament is evidenced in the Sagnac effect, the "
                        "well-known Coriolis forces, and by geosynchronous satellites … In the "
                        "geocentric model, we agree that if the heavens ceased their rotation, "
                        "the satellites would fall to the earth.” (p. 648) &mdash; and, as the "
                        "essay&rsquo;s own thesis about what any of this can be used for: "
                        "“it is impossible to launch an attack on geocentricity on the basis of "
                        "general relativity, by definition.” (p. 637)"),
        drift_type="force_upgraded",
        note=("<strong>On wording, this compression is unusually faithful, and the entry says so "
              "rather than manufacturing a gap.</strong> The source asserts the evidential claim "
              "flatly &mdash; satellites <em>evidence</em> the firmament&rsquo;s rotation &mdash; "
              "so it will not do to answer only the book&rsquo;s milder opening chapter, where "
              "geosynchronous satellites are listed among phenomena that &ldquo;do not prove, in "
              "the least, the heliocentric system&rdquo; (Vol. I scan, ch. 1, printed p. 37). And "
              "item 109 goes further in the source&rsquo;s favour than the source needed: "
              "&ldquo;Geostationary satellites reinterpretation&rdquo; concedes in one word that "
              "this is a re-description. A reader could reasonably score that as no drift at all."
              "<br><br>"
              "<strong>The drift is in the speech act and in three dropped restrictions.</strong> "
              "The essay is a defence &mdash; it exists to answer two critics who argued that "
              "geosynchronous satellites are impossible on a fixed Earth &mdash; and its thesis "
              "is equivalence: &ldquo;it is impossible to launch an attack on geocentricity on "
              "the basis of general relativity, by definition&rdquo; (printed p. 637). A "
              "permission that holds by definition arrives on the list as proof item 15 of 461. "
              "That is the R01 move exactly: the wording barely shifts and the speech act does. "
              "Travelling with it, and lost: <em>the equator</em> &mdash; geostationary satellites "
              "sit &ldquo;only over the equator, and at the same prescribed height as that "
              "indicated by the Newtonian methods Dr. North favors&rdquo; (p. 635); "
              "<em>the height</em> &mdash; conceded in that same clause to be Newton&rsquo;s own "
              "number, 42,164 km from the Earth&rsquo;s centre; and <em>the conditional</em> "
              "&mdash; the satellites would fall if the heavens stopped, so the entire support is "
              "the assumed cosmic rotation rate."
              "<br><br>"
              "<strong>The restriction that does not survive the journey at all.</strong> An "
              "equator and a radius from a centre are properties of a globe, and the tradition "
              "the passage belongs to says so openly. Items 43, 217, 386 and 395 of the same list "
              "assert that the surface is flat. The compression therefore does something the "
              "seven-value enum has no word for: it moves a claim into a document whose headline "
              "its own premises deny. <code>force_upgraded</code> is recorded because it is the "
              "plainest and most checkable of the three, and the reader has both texts above."
              "<br><br>"
              "<strong>The refutation answers the source, not the fragment:</strong> it grants "
              "the Earth-fixed frame, grants that the cited relativity papers are real and that "
              "the book&rsquo;s bibliographic details for them check out, grants that a rotating "
              "shell induces the right forces, and puts "
              "the weight on what the source itself concedes &mdash; the equator, the Newtonian "
              "radius, and a conclusion that holds by definition.")),

    verdict_challenge=dict(challenged=False, proposed_verdict=None, reasoning=None),

    people=["PER-SUNGENIS"],
    related=["A06", "A09", "A13", "A18", "A20", "A22", "R01", "R06", "R08"],

    sources=[
        dict(label="Sungenis & Bennett, Galileo Was Wrong Vol. II — archive.org OCR text (item "
                   "GalileoWasWrongTheChurchSungenisRobertA.Bennett4276). Appendix 1 reprints "
                   "Selbrede's essay from printed p. 630; the equatorial and Newtonian-height "
                   "concession at p. 635, “by definition” at p. 637, the quoted sentence at p. 648",
             url="https://archive.org/stream/GalileoWasWrongTheChurchSungenisRobertA.Bennett4276/Galileo%20Was%20Wrong_%20The%20Church%20%20-%20Sungenis,%20Robert%20A.%20&%20Bennett,_4276_djvu.txt"),
        dict(label="Galileo Was Wrong — the second archive scan (item GallileoWasWrong), used here "
                   "for ch. 1 p. 37, the Sciama quotation at ch. 7 p. 468, the Machian footnotes at "
                   "ch. 10 pp. 607–612, and Posch on Hildegard at ch. 11 p. 662. Different edition, "
                   "different pagination",
             url="https://archive.org/details/GallileoWasWrong"),
        dict(label="Ø. Grøn & E. Eriksen, “Translational inertial dragging”, Gen. Rel. Grav. "
                   "21:105–124 (1989) — the “perfect dragging” passage and the Moon example, which "
                   "the source quotes and places at pp. 109–110 and pp. 117–118; those internal "
                   "page attributions are the book's and the paper was not opened for this entry",
             url="https://doi.org/10.1007/BF00761081"),
        dict(label="H. Pfister & K. Braun, “Induction of correct centrifugal force in a rotating "
                   "mass shell”, Class. Quantum Grav. 2:909–918 (1985) — the correct centrifugal "
                   "force is induced once the shell is allowed to deform",
             url="https://doi.org/10.1088/0264-9381/2/6/015"),
        dict(label="D. R. Brill & J. M. Cohen, “Rotating Masses and Their Effect on Inertial "
                   "Frames”, Phys. Rev. 143:1011–1015 (1966)",
             url="https://doi.org/10.1103/PhysRev.143.1011"),
        dict(label="L. P. Orwig, “Machian effects in compact, rapidly spinning shells”, Phys. Rev. "
                   "D 18:1757–1763 (1978) — the abstract the source quotes",
             url="https://doi.org/10.1103/PhysRevD.18.1757"),
        dict(label="H. Pfister, “On the history of the so-called Lense–Thirring effect”, Gen. Rel. "
                   "Grav. 39:1735–1748 (2007)",
             url="https://doi.org/10.1007/s10714-007-0521-4"),
        dict(label="Frame-dragging — the interior acceleration of a rotating shell, including the "
                   "extra axial term 2(ω·r)ω and the coefficients d₁, d₂, with Pfister & Braun "
                   "cited for the deformable-shell resolution",
             url="https://en.wikipedia.org/wiki/Frame-dragging"),
        dict(label="Geostationary orbit — 42,164 km radius, 35,786 km altitude, 3.07 km/s, period "
                   "one sidereal day; ~50 m/s per year of north–south station-keeping; stable "
                   "longitudes at 75.3°E and 108°W at ~2 m/s per year",
             url="https://en.wikipedia.org/wiki/Geostationary_orbit"),
        dict(label="Earth's rotation — ω = (7.2921150 ± 0.0000001)×10⁻⁵ rad/s, stellar day "
                   "86,164.0989 s, excess length of day 0.25–1 ms over 1999–2010 and −1.59 ms on "
                   "29 June 2022; IERS Earth-orientation parameters",
             url="https://en.wikipedia.org/wiki/Earth%27s_rotation"),
        dict(label="Syncom — first geosynchronous satellite Syncom 2, 26 July 1963; first "
                   "geostationary satellite Syncom 3, 19 August 1964",
             url="https://en.wikipedia.org/wiki/Syncom"),
        dict(label="D. W. Sciama, The Unity of the Universe (1959) — the hovering-satellite "
                   "illustration quoted at Vol. I p. 468 from pp. 85–89 per the book's footnote 907",
             url="https://openlibrary.org/search?q=The+Unity+of+the+Universe+Sciama"),
        dict(label="Yu. N. Obukhov, “Rotation in cosmology”, Gen. Rel. Grav. 24:121–128 (1992) — "
                   "cited by the source on the viability of rotating cosmological models",
             url="https://doi.org/10.1007/BF00756780"),
        dict(label="Schadewald, The Plane Truth, ch. 9 — the International Flat Earth Society "
                   "founded by Shenton and William Mills on 20 December 1956; the chapter's only "
                   "satellite sentence is that reporters came to hear Shenton explain them",
             url="https://www.cantab.net/users/michael.behrend/ebooks/PlaneTruth/pages/Chapter_09.html"),
    ]),
}
