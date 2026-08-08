# -*- coding: utf-8 -*-
"""
Batch 7 — ARG-C07, "Patristic, scholastic and church-tradition affirmation".
9 items, lane C, verdict NOT DEMONSTRATED, originator recorded as Robert Sungenis,
Galileo Was Wrong Vol. III (2006).

Operator constraint, honoured throughout: this page never adjudicates whether God
exists, whether scripture is true, or whether any church is right — in either
direction. Three questions only: what kind of claim is being made, whether
measurement can settle it, and whether the list represents its own source.
Sungenis is a living Catholic apologist; nothing here touches motive, finances or
good faith, and the scholastic tradition is treated as what it is — a serious
intellectual enterprise that got the shape of the Earth right.

Siblings, deliberately non-overlapping. C02 owns the domain boundary
(Galileo/Baronius), the Carpenter genealogy and the proof-text-method finding.
C04 owns the raqia philology, the reception history and the Schadewald ancestry.
C05 owns the chug/kanphot philology and the documented Schadewald→Skiba chain.
C04 and C05 have already used Basil, Aquinas and Calvin on the shape of the
HEAVENS. C07 owns different ground: the shape of the EARTH in the same
authorities, the flat-earth-myth historiography (Irving → Letronne → Draper →
White → Russell), the source's own anti-flat-earth book, and the volume identity
of the Galileo Was Wrong scan — which this pass settles.

Known defect in C02 NOT repeated: every quotation below traces to an entry in
`sources`.
"""

ENTRY = {

"C07": dict(

    tldr=("The tradition this cluster summons is geocentric, and geocentrism is a "
          "spherical-Earth position — a round Earth at the centre of round heavens. That is "
          "not our reading imposed on it: the man our own record names as originator says so "
          "in the book the cluster is credited to, and later wrote a 736-page book arguing the "
          "Earth is a globe. Nine items reporting that the Church taught the Earth does not "
          "move are not evidence that it is flat, they are three claims rather than nine, and "
          "a commentary on a proof-text is not a second witness to it."),

    passage=dict(
        work="WRK-SUNGENIS-2006",
        locator=("Vol. II, ch. 13 “Modern Science and its Persistent Problems”, p. 584 of the "
                 "archive.org full-text scan (seventh edition, 2013), with the supporting "
                 "patristic dossier at footnote 574 on the same page."),
        pd=False,
        quote=("The reality is that Lactantius was the only Father of the Church (and he was "
               "not a highly esteemed patristic witness) who held to the idea of a "
               "non-spherical Earth. Every other Father who wrote at length on cosmological "
               "issues stated his belief, based on Scripture and science, that the Earth was "
               "a sphere."),
        gloss="""<p>That sentence is the whole of this cluster in one line, and it was written by the man our record credits with the cluster. Everything below is bookkeeping around it &mdash; including three corrections to our own records.</p>

<p><strong>1. The archive scan is Volume II, and we have been calling it Volume I.</strong> <a href="#ARG-R06">ARG-R06</a> records, in <code>review/corrections.json</code>, an unresolved question: the archive item our source list points at is labelled <em>Galileo Was Wrong (2)</em> rather than volume&nbsp;I. It is now resolved, from the scan's own front matter. The title page reads <em>Vol II, Chapters 7 to 13, Seventh edition</em>, and the copyright page names the work <em>&hellip; Volume II</em>, published 2013 by Catholic Apologetics International Publishing. The two page citations R06 draws from it both land inside it: the rotating-frame Lagrangian is on p.&nbsp;161 and the &ldquo;General covariance&rdquo; section closes on p.&nbsp;171, exactly as R06 says &mdash; but in Volume II, not Volume I. R06's finding is unaffected in substance; its volume label is wrong and so is the label on our sources entry, and the standing caveat &ldquo;we have not yet resolved which volume this is&rdquo; can be retired.</p>

<p><strong>2. &ldquo;Vol. III, 2006&rdquo; is not a citation that can exist.</strong> The same copyright page states that the <em>previous five editions, in two volumes,</em> were published between 2005 and 2010, and that the <em>sixth edition, in three volumes,</em> appeared in January 2013. A third volume therefore first exists in 2013, six and a half years after the date on our record. Our cluster line for C07 &mdash; and for <a href="#ARG-D15">ARG-D15</a>, which carries the same pairing &mdash; should read either the 2006 two-volume edition (whose second volume is the historical one) or Vol.&nbsp;III of 2013, not a volume III dated 2006. Two smaller discrepancies in the work record travel with it: it describes Vol.&nbsp;II as the historical volume, whereas the 2013 Vol.&nbsp;II we can read is chapters 7&ndash;13 of the scientific argument; and it gives a tenth edition in 2013, which cannot be right if the sixth edition appeared in January of that year and the copy we hold is the seventh.</p>

<p><strong>3. The argument has a documented earlier hand, and the source credits it.</strong> Two pages before the sentence quoted above, Sungenis quotes Robert Bellarmine writing to Paolo Antonio Foscarini on 12 April 1615: the Council of Trent <em>&ldquo;prohibits interpreting Scripture against the common consensus of the Holy Fathers&rdquo;</em>, and the commentators &ldquo;all agree&rdquo; that the sun turns around a motionless Earth. That is items 24, 77, 124 and 427 in their original form, 391 years before the work our record names. Sungenis is transmitting an argument, names its author, and quotes him at length &mdash; which is more than the list does. Our <code>real_source</code> field for this cluster is null and should carry Bellarmine's letter, the way <a href="#ARG-A02">ARG-A02</a> carries Michelson&ndash;Gale.</p>

<p><strong>4. The nine items name nobody at all.</strong> Checked against the specimen: the list gives no father, no scholastic, no catechism, no sermon and no commentary. &ldquo;Early Church fathers.&rdquo; is the entire text of item 124. Nine numbered pieces of evidence carry zero citations between them, which is what the verdict NOT DEMONSTRATED is recording &mdash; not that the tradition said something else, but that no argument was made.</p>

<p><strong>5. Nine items are three claims, and one of them is not a claim about the world.</strong> Items 77 (&ldquo;Early theologians affirmed geocentrism&rdquo;), 124 (&ldquo;Early Church fathers&rdquo;) and 427 (&ldquo;Church Fathers affirm rest&rdquo;) are one assertion entered three times; 78 (&ldquo;Medieval hierarchy centered on Earth&rdquo;), 428 (&ldquo;Scholastics harmonize Aristotle&rdquo;) and 444 (&ldquo;Medieval sermons describing concentric heavens&rdquo;) are a second entered three times, and 444 is additionally a near-twin of item 127, &ldquo;Medieval art concentric heavens&rdquo;, which sits in another cluster. Item 443 (catechisms) is a third. That leaves items 24 and 445, which are of a different kind altogether and are dealt with in section 4 of the refutation: they assert that the tradition <em>agrees with the texts already on the list</em>, which is not a further witness.</p>

<p><strong>6. This material did not come down the flat-earth line.</strong> Worth stating because the cluster sits in a scriptural lane full of Victorian ancestry. William Carpenter's <em>One Hundred Proofs</em> (1885), the source of the numbered-proof form, contains zero occurrences of <em>father</em>, <em>Augustine</em>, <em>Aquinas</em>, <em>patristic</em>, <em>scholastic</em>, <em>catechism</em>, <em>council</em> or <em>tradition</em> &mdash; full text searched. The vocabulary of this cluster is Catholic and it arrives from the geocentric lineage, not the zetetic one. That is the whole difficulty with it, and it is the subject of the refutation.</p>

<p><strong>Scope.</strong> The volume we could read in full is Vol.&nbsp;II of the seventh edition. Volume&nbsp;III &mdash; the church-history volume, and the one our record names &mdash; is in copyright and we could not search it. Where an item cannot be found, the claim below is always <em>not located in the volume we could read</em>, never <em>the author never wrote it</em>. Same discipline as <a href="#ARG-R06">ARG-R06</a>.</p>"""),

    steelman=dict(
        description="""<p>Two things here are true, and the second is more interesting than the first.</p>

<p><strong>The tradition really was geocentric, and the dossier is real.</strong> Basil of Caesarea, preaching in the 370s, says the Earth <em>&ldquo;occupies the centre of the universe, its natural place&rdquo;</em> and that <em>&ldquo;by necessity it is obliged to remain in its place, unless a movement contrary to nature should displace it&rdquo;</em>. John Chrysostom says the Earth <em>&ldquo;turns not, but stands firm&rdquo;</em>. The Roman Catechism of 1566 says God commanded the earth <em>&ldquo;to stand in the midst of the world, rooted in its own foundation&rdquo;</em> &mdash; so item 443 is not invented either. And Bellarmine, writing to Foscarini in 1615, states the position in its strongest form: the commentators <em>&ldquo;all agree&rdquo;</em>, and he asks whether the Church <em>&ldquo;can tolerate giving Scripture a meaning contrary to the Holy Fathers and to all the Greek and Latin commentators&rdquo;</em>. Anybody who tells this cluster that the Fathers were quietly heliocentric is simply wrong, and would deserve the correction.</p>

<p><strong>And the underlying demand is not a fallacy, it is a rule of the tradition being cited.</strong> The weak form of this argument is &ldquo;lots of holy men agreed with me&rdquo;, which is an appeal to authority and can be dismissed as one. The strong form is different: Trent laid down that Scripture is not to be interpreted against the unanimous consent of the Fathers, and Bellarmine is applying that rule, not inventing it. On that reading the claim is not &ldquo;the Fathers were good physicists&rdquo; but &ldquo;a communion that binds itself to a rule of interpretation owes an account of what happened to the rule&rdquo;. That is a serious question, it is internal to a tradition entitled to ask it, and the modern geocentrist presses it hard: when the Master of the Sacred Palace was overruled in 1820 and the books came off the Index in 1835, was that a doctrinal reversal or a disciplinary accommodation? Writers in Sungenis's own circle argue the latter in detail, and the argument is not stupid.</p>""",

        why_it_doesnt_save_claim="""<p>It does not save the claim because <strong>every authority in the dossier held that the Earth is a sphere</strong>, and the source says so himself, in the same chapter, two paragraphs after he assembles them.</p>

<p>His footnote 574 &mdash; the one supporting the sentence quoted above &mdash; is a patristic sphericity dossier: Athanasius on the ocean flowing <em>&ldquo;outside round the whole Earth&rdquo;</em>; Gregory of Nyssa on the sun's shadow, <em>&ldquo;because its spherical shape makes it impossible for it to be clasped all round at one and the same time by the rays&rdquo;</em>, and on <em>&ldquo;some particular point of the globe&rdquo;</em> &mdash; verifiable verbatim in <em>On the Soul and the Resurrection</em>; Augustine on <em>&ldquo;the circles of the round world&rdquo;</em>; Jerome on spheres. Augustine elsewhere concedes the geometry outright while doubting only the inhabitants: <em>&ldquo;although it be supposed or scientifically demonstrated that the world is of a round and spherical form&rdquo;</em>. Move forward to the schoolmen of items 78, 428 and 444 and it becomes structural rather than incidental: Aquinas's textbook example, in the first article of the first question of the <em>Summa</em>, of one conclusion proved by two sciences, is <em>&ldquo;that the earth, for instance, is round&rdquo;</em>. Sacrobosco's <em>De sphaera mundi</em> (c.&nbsp;1230) &mdash; the standard university astronomy text for four centuries, 84 printed editions in two hundred years &mdash; opens by proving it, from lunar eclipse timings, from stars near the pole, from seeing further up the mast, from water taking a round shape. David Lindberg's summary of the field is that there was <em>&ldquo;scarcely a Christian scholar of the Middle Ages who did not acknowledge Earth's sphericity&rdquo;</em>.</p>

<p>So the cluster's own witnesses testify against the list they have been entered into. And this is not a debating point about half a sentence: the geometry is load-bearing. <strong>Concentric heavens require a round Earth at the centre of them</strong> &mdash; that is what makes them concentric &mdash; so item 444 is a spherical-Earth cosmology entered as evidence for a flat one. Item 428, the harmonisation of Aristotle, imports sphericity as part of the package being harmonised; that is why the scholastic astronomy textbook is called <em>On the Sphere</em>.</p>

<p>The second half of the steelman fails differently, and more quietly. If the argument is really about a tradition's fidelity to its own interpretive rule, then it is an argument inside that tradition about that tradition, and no measurement bears on it in either direction &mdash; which is precisely what this review says at <a href="#ARG-C02">ARG-C02</a> and does not adjudicate. The moment it is entered on a list of <em>pieces of evidence about the Earth</em>, it has changed what it is claiming, and it must then answer to instruments rather than to Trent. The two versions cannot both be run: the strong one is out of our remit and out of the list's, and the weak one is authority-counting, which does not survive the next paragraph.</p>"""),

    refutation="""<p><strong>The boundary, once, and then not again.</strong> Nothing below argues that any passage is false, that any council erred in what it was for, or that anyone's faith is misplaced &mdash; and nothing below argues the reverse either. The boundary is set out in full at <a href="#ARG-C02">ARG-C02</a>. Three questions are inside the remit: what kind of claim is being made, whether measurement can settle it, and whether the list represents its source. The scholastic tradition is treated here as what it was, a rigorous intellectual enterprise that happened to be right about the shape of the Earth and wrong about its motion; a review that sneered at it would be both mistaken and, given what follows, self-defeating.</p>

<p><strong>1. Read the nine items and notice what none of them says.</strong> Church consistency with Scripture. Early theologians affirmed geocentrism. Medieval hierarchy centered on Earth. Early Church fathers. Church Fathers affirm rest. Scholastics harmonize Aristotle. Early catechisms reflecting immovable Earth language. Medieval sermons describing concentric heavens. Patristic commentaries on the sun's &ldquo;course.&rdquo; Every one is about <em>rest</em> or <em>centrality</em>. Not one is about <em>shape</em>. They are geocentric claims, and they are accurate ones: the tradition did hold that the Earth stands still at the centre. The list they appear on is titled <em>435 Pieces of Evidence The Earth is Not A Spinning Ball</em>, and its neighbouring clusters require a flat Earth &mdash; a dome overhead at <a href="#ARG-C04">ARG-C04</a>, four literal corners at <a href="#ARG-C05">ARG-C05</a>. Those two things cannot both be supported by this material, because the material supports a globe.</p>

<p><strong>2. Geocentrism is a spherical-Earth position, and this cluster is the cleanest place on the site to see it.</strong> The evidence is set out in the steelman above and is not repeated; the short form is that the Fathers, the schoolmen and the standard medieval astronomy textbook all put a round Earth at the centre, and that the source of this cluster says so in print. He is not a reluctant witness. Robert Sungenis published <em>Flat Earth | Flat Wrong: An Historical, Biblical and Scientific Analysis</em> (Catholic Apologetics International Publishing, 2018), 736 pages, of which roughly eighty are given to the Fathers' views on a spherical Earth, and its stated purpose is to show <em>&ldquo;why, historically, biblically and scientifically, the globe Earth is the true reality&rdquo;</em>. A reviewer of it describes the exact manoeuvre this cluster performs: <em>&ldquo;Many flat earthers take statements Early Church Fathers made supporting geocentrism and then claim those statements show the early church believed in a flat earth.&rdquo;</em> The 2013 volume behind the cluster is the same: it works in WGS84 ellipsoid parameters, an Earth radius of some 4,000 miles, polar flattening and an equatorial bulge. <strong>The person our record names as this cluster's originator has written a book against the conclusion the cluster is being used to support.</strong> That is not an ambush and it is not a gotcha; it is the plainest available statement of the structural finding this whole review keeps arriving at &mdash; that two lineages have been merged in this list which were never reconciled, and that the geocentric one brought a globe with it.</p>

<p><strong>3. The one Father who did hold a flat Earth, and what happened to him.</strong> Lactantius, and the source names him first, unprompted. The other standard name, Cosmas Indicopleustes, was a sixth-century Alexandrian merchant turned monk whose <em>Christian Topography</em> modelled the cosmos on the tabernacle; David Lindberg calls him <em>&ldquo;the only medieval European known to have defended a flat earth cosmology&rdquo;</em>, three or four manuscripts survive, and John Philoponus wrote against him inside his own century. Two men, both marginal, both answered by their contemporaries. That is the flat-earth tradition available for recruitment here, and the list does not recruit it &mdash; it recruits the other one.</p>

<p><strong>4. Two of the nine are not independent witnesses at all.</strong> Item 24, &ldquo;Church consistency with Scripture&rdquo;, does not assert anything about the Earth. It asserts that one authority agrees with another authority whose testimony is already on the list at <a href="#ARG-C01">ARG-C01</a> and <a href="#ARG-C02">ARG-C02</a>. Item 445, &ldquo;Patristic commentaries on the sun's &lsquo;course&rsquo;&rdquo;, is the same shape: a commentary on a verse is not evidence in addition to the verse. A body of commentary on a text will agree with the text; that is what commentary is for, and it adds no information about the world. This matters because the list's whole method is accumulation &mdash; 461 items feels like 461 witnesses. Counting a text, then counting the commentary on the text, then counting the catechism that summarises the commentary, produces three numbers from one source.</p>

<p><strong>5. What NOT DEMONSTRATED means here, precisely.</strong> It does not mean the Fathers were wrong, and the distinction matters: REFUTED would require showing the tradition mistaken, and this review neither shows that nor needs to. It means the argument was never made. Between &ldquo;the Church taught that the Earth is at rest&rdquo; and &ldquo;the Earth is at rest&rdquo; there is a missing step, and no item supplies it. An authority's testimony is evidence about what the authority held. To convert it into evidence about the world you need the further premise that this authority is reliable on this question, and that premise cannot be established by more testimony without circularity &mdash; it has to come from somewhere else, and on the motion of the Earth the somewhere else is instruments. This is not a modern imposition on the tradition. It is close to what Aquinas is doing in the very passage cited above: distinguishing the ways two sciences prove the same conclusion, and taking the roundness of the Earth as the example of a thing so proved.</p>

<p><strong>6. The authority's own later acts, offered as dates rather than as a verdict.</strong> The general prohibition of books teaching heliocentrism was dropped from the Index in 1758. In 1820 the Master of the Sacred Palace, Filippo Anfossi, refused a licence to Canon Giuseppe Settele's astronomy textbook for treating heliocentrism as physical fact; Settele appealed, and after review the refusal was overturned, the decree recording that <em>no obstacles exist for those who sustain Copernicus' affirmation regarding the earth's movement</em> as modern astronomers understand it. Copernicus's <em>De revolutionibus</em> and Galileo's <em>Dialogo</em> were omitted from the next edition of the Index, in 1835. Those are checkable facts and they are all that is asserted here. <strong>The geocentrist reply is fair and should be stated:</strong> a licence to print is a disciplinary act, not a doctrinal definition, and writers in Sungenis's own circle argue exactly that &mdash; that the 1822 imprimatur <em>&ldquo;did not refer to Galileo or to the sentence of 1633&rdquo;</em> and that the books stayed on the Index another thirteen years. Grant it entirely. Notice what granting it costs: the argument is then no longer that the tradition's witness settles the question, but that <em>some</em> acts of the tradition count and others do not &mdash; and the criterion sorting them is supplied from outside the counting. Which is the case for every appeal to authority, and is why this one cannot do the work asked of it. The same reflexivity runs the other way and is worth admitting: when this page cites Aquinas or Sacrobosco on sphericity it is not treating them as authorities on the Earth either. They are being cited as witnesses to <em>what the tradition held</em> &mdash; which is the only thing an item of the form &ldquo;the Fathers affirmed X&rdquo; can be about, and on that narrow question they are the best witnesses there are.</p>

<p><strong>7. The myth in the background, which both sides of this argument have inherited.</strong> The idea that medieval Christians thought the Earth flat is itself a nineteenth-century construction. Washington Irving's <em>A History of the Life and Voyages of Christopher Columbus</em> (1828) supplied a largely fictional Salamanca commission raising religious objections to sphericity, when the real dispute was about the Earth's <em>size</em>; Jean Antoine Letronne misrepresented the Fathers and their successors as flat-earthers in 1834; John William Draper (1874) and Andrew Dickson White (1896) made it a weapon of the conflict thesis. Jeffrey Burton Russell's <em>Inventing the Flat Earth</em> (1991) is the standard correction, and its finding is that with extraordinarily few exceptions no educated person in the West believed the Earth flat from the third century BC onward. That myth is doing work on both sides of the present dispute. A polemicist who says the Church taught a flat Earth and was ignorant, and a compiler who says the Church taught a flat Earth and was right, have made the same historical error and only disagree about the scoring. This review declines both.</p>

<p><strong>8. The question every argument on this site is finally asked.</strong> Does any of it distinguish a flat, stationary Earth from an ordinary spinning globe? These nine items cannot, because they contain no measurement &mdash; but the failure here is sharper than usual and runs one way. On the flat/round axis the cluster's own authorities discriminate <em>against</em> the list: they held a globe, and said why. On the moving/stationary axis the items report a genuine historical consensus and no more, and the discriminating evidence lies elsewhere on this page &mdash; the Michelson&ndash;Gale fringe shift at <a href="#ARG-A02">ARG-A02</a>, ring-laser gyroscopy at <a href="#ARG-A07">ARG-A07</a>, the southern pole of rotation at <a href="#ARG-B08">ARG-B08</a>.</p>

<p><strong>Verdict.</strong> NOT DEMONSTRATED, in the register the legend gives it: asserted, argument never made. Three things it is not. It is not a finding that the Fathers or the schoolmen were fools &mdash; they were right about the shape of the Earth by observation and argument, centuries before anyone could photograph it, and they are cited above for exactly that. It is not a verdict on any church, any council or any text; that is outside the remit in both directions. And it is not REFUTED, which would require showing the tradition mistaken about what it taught. What is shown is narrower and sufficient: nine unattributed items, collapsing to three claims, none of which is about the shape of the Earth, drawn from a body of authorities who held it to be a sphere, assembled by an author who has written 736 pages saying so.</p>""",

    advocate=dict(
        best_defense=(
            "You have written a long page proving something I said first, quoted me saying it, "
            "and then filed it under a verdict against me. Of course the Fathers held a "
            "spherical Earth. I am the one who documented it — at book length, against the "
            "flat-earthers, at my own expense. So whatever you have refuted, it is not me; it "
            "is a compiler who lifted my paragraphs, and you say so yourself. Second, and this "
            "is the real complaint: you changed the subject. My claim is that the patristic and "
            "magisterial consensus is geocentric. You agree. You have conceded the entire "
            "content of items 24, 77, 78, 124, 427, 428, 443, 444 and 445 and then marked them "
            "NOT DEMONSTRATED because a third party misused them. Third, your dates. An "
            "imprimatur is a licence to print, granted by a congregation, and you know the "
            "difference between that and a doctrinal definition — 1616 and 1633 were never "
            "rescinded, and you have quoted the man who explains why. Fourth, your reflexivity "
            "paragraph is an admission. You cite Aquinas when he suits you and dismiss the "
            "tradition as authority-counting when it does not. Either the witness of the "
            "tradition is evidence or it is not; you cannot have it as evidence of sphericity "
            "and as noise on motion. Fifth, and last: you say the question is settled by "
            "instruments. Which instrument reading, exactly, is inconsistent with a stationary "
            "Earth in the frame in which it is stationary? You have spent this page on history "
            "because the physics is at R01 and R06, and there you concede that the formalism "
            "does not decide it."),
        survives=4,
        preemptive=(
            "Strong — the second and fourth points in particular — and four changes were made "
            "in the body rather than left to the reader. (a) The concession is now made in the "
            "body and not smuggled into the steelman: section 1 states outright that the items "
            "are accurate geocentric claims and that the tradition did hold the Earth at rest. "
            "A defender who springs that on us wins the exchange; conceding it first costs "
            "nothing and is true. The verdict is then scoped to what it actually attaches to — "
            "the missing step in section 5, and the shape/motion equivocation in sections 1 and "
            "2 — not to the historical claim. (b) The 'you changed the subject' charge is "
            "pre-answered by the list's own title, quoted in section 1: the items were entered "
            "as evidence that the Earth is not a spinning ball, in a corpus whose sibling "
            "clusters require a flat one. Shape is not our subject-change, it is the "
            "compilation's, and section 2 attributes the fault to the compiler explicitly and "
            "by name-free description. (c) The fourth point — that we cite Aquinas selectively "
            "— is answered inside section 6 rather than left implicit, and it is the single "
            "most important addition this pass made: Aquinas and Sacrobosco are cited as "
            "witnesses to what the tradition held, which is the only question an item of the "
            "form 'the Fathers affirmed X' can be about, and not as authorities on the Earth. "
            "That distinction is stated in the text so a reader meets it before the objection "
            "does. (d) The 1758/1820/1835 material is presented as dates only, with the "
            "disciplinary reading granted in full and sourced to his own circle, and the reply "
            "narrowed to the one thing granting it establishes: that acts of the authority are "
            "being sorted by a criterion from outside. On the fifth point we do not need "
            "physics here and the text says where it lives; C07 is a provenance and category "
            "finding, and R01, R06 and R11 carry the frame argument — R11 with Bouw's own "
            "concession that the models are observationally equivalent and must be chosen on "
            "other grounds, which is the geocentrist camp conceding the fifth point to us in "
            "print.")),

    straw_man=dict(
        identified=True,
        detail=("The straw man this cluster needs is the Draper-White caricature: that anyone "
                "defending the globe must hold that the medieval Church was ignorant and "
                "hostile to knowledge, so that citing the tradition at all looks like a blow "
                "against modern arrogance. That caricature is false, and its falsity is a "
                "matter of record rather than of opinion - Irving's fictionalised Columbus in "
                "1828, Letronne in 1834, Draper in 1874, White in 1896, corrected by Russell in "
                "1991. It is also, precisely, the thing the tradition itself disproves: the "
                "schoolmen taught sphericity from a textbook called On the Sphere. The straw "
                "man this page had to avoid in return is the mirror image of it, and it is the "
                "easy one to reach for: treating patristic and scholastic cosmology as naive, "
                "or the appeal to it as simple credulity. It is neither. Bellarmine is applying "
                "a stated rule of interpretation, not counting heads, and a review that scored "
                "the cheap point against scholasticism would be arguing against its own best "
                "evidence, since the strongest witnesses to a spherical Earth on this page are "
                "Aquinas, Sacrobosco and the Fathers whose dossier the source assembled.")),

    compression=dict(
        assessed=True, drifted=True,
        list_phrasing=("Church Fathers affirm rest. / Early theologians affirmed geocentrism. / "
                       "Scholastics harmonize Aristotle. / Medieval sermons describing "
                       "concentric heavens. / Early catechisms reflecting immovable Earth "
                       "language. / Church consistency with Scripture."),
        source_wording=("&ldquo;&hellip; the geocentric foundation laid down in Scripture; which "
                        "foundation was promoted, without exception, by a consensus of the "
                        "Church Fathers; continued faithfully by Thomas Aquinas and the "
                        "medievals; and confirmed by papal and conciliar decrees&rdquo; "
                        "(Vol.&nbsp;II, ch.&nbsp;12, p.&nbsp;455) &mdash; and, at p.&nbsp;584: "
                        "&ldquo;Every other Father who wrote at length on cosmological issues "
                        "stated his belief, based on Scripture and science, that the Earth was "
                        "a sphere.&rdquo;"),
        drift_type="scope_widened",
        note="""<p><strong>Start with what did not drift, because it is the more usual finding in this family and it is absent.</strong> The strength is not inflated. The source says the Fathers held geocentrism <em>&ldquo;without exception&rdquo;</em> and that the medievals continued it <em>&ldquo;faithfully&rdquo;</em>; the list says &ldquo;Church Fathers affirm rest&rdquo;, which is weaker if anything. No hedge was dropped, because there is no hedge to drop. We looked specifically for <em>force_upgraded</em> &mdash; the pattern where a careful author argues only that a position is <em>permitted</em> or <em>traditional</em> and the list re-uses the permission as a proof &mdash; and did not find it in the volume we could read: on the patristic consensus this author asserts, he does not concede. <strong>We are not manufacturing a drift where the wording is faithful.</strong> The refutation above therefore answers the claim at full strength, as stated, and does not lean on the compression.</p>

<p><strong>What did move is the scope of what the material is offered as evidence for.</strong> In the source, the patristic and scholastic consensus is evidence for geocentrism &mdash; a still, central, and explicitly <em>spherical</em> Earth. The qualifying clause is not distant or inferred; it stands in the same chapter, in the sentence quoted in the second half of the box above, and its supporting footnote is a dossier of Fathers testifying to sphericity. That clause does not travel. The nine items reach the list stripped of it, in a compilation titled <em>435 Pieces of Evidence The Earth is Not A Spinning Ball</em> whose sibling clusters assert a solid dome (<a href="#ARG-C04">ARG-C04</a>) and four literal corners (<a href="#ARG-C05">ARG-C05</a>). A narrow claim &mdash; this tradition supports geocentrism &mdash; has been generalised into a broad one: this tradition supports this list. The author's own 736-page book against flat-earthism is the measure of how far that is from his position.</p>

<p><strong>A second drift is present and the enum takes one value, so it is recorded here.</strong> Items 24 (&ldquo;Church consistency with Scripture&rdquo;) and 445 (&ldquo;Patristic commentaries on the sun's &lsquo;course&rsquo;&rdquo;) undergo the <em>category_shifted</em> change instead. In the source, and in Bellarmine's 1615 letter behind it, the consensus of the Fathers functions as a <em>rule of interpretation</em> &mdash; Trent's prohibition on reading Scripture against their common consent. That is a claim about how a text may be read. On the list it is numbered evidence about the Earth. The same move A03 records for &ldquo;Airy's failure&rdquo;: a claim of one kind entering a proof list as a claim of another.</p>

<p><strong>Scope of the comparison.</strong> Vol.&nbsp;II of the seventh edition (2013) was searched in full. Volume&nbsp;III, the church-history volume our record names, is in copyright and could not be searched, so nothing above should be read as &ldquo;the author never wrote this&rdquo;. Two items in particular &mdash; 443 (early catechisms) and 444 (medieval sermons) &mdash; have no counterpart in the volume we could read; <em>catechism</em> does not occur in it at all. They are recorded as <em>not located in the volume available</em>, and item 443 in any case has an obvious real referent in the Roman Catechism of 1566, which is quoted in the steelman above and which says nothing whatever about the Earth's shape.</p>"""),

    verdict_challenge=dict(challenged=False, proposed_verdict=None, reasoning=None),

    people=["PER-SUNGENIS", "PER-CARPENTER"],

    related=["C01", "C02", "C04", "C05", "C08", "C09", "D01", "D15", "R06", "R11"],

    sources=[
        dict(label="Sungenis & Bennett, Galileo Was Wrong: The Church Was Right, Vol. II (7th ed., 2013) — archive.org full-text scan; title/copyright pages give the volume, edition and the two- vs three-volume history; ch. 13 p. 584 (Lactantius, the Fathers on sphericity, footnote 574); ch. 12 p. 455 (the consensus sentence); Bellarmine to Foscarini at footnote 571; ch. 10 pp. 161 and 171 (the passages ARG-R06 cites as “Vol. I”)",
             url="https://archive.org/stream/GalileoWasWrongTheChurchSungenisRobertA.Bennett4276/Galileo%20Was%20Wrong_%20The%20Church%20%20-%20Sungenis,%20Robert%20A.%20&%20Bennett,_4276_djvu.txt"),
        dict(label="Robert Sungenis, Flat Earth | Flat Wrong: An Historical, Biblical and Scientific Analysis — publisher's page: 736 pages, ~80 pages on the Church Fathers' views on a spherical Earth, “the globe Earth is the true reality”",
             url="https://flatearthflatwrong.com/"),
        dict(label="Review of Flat Earth Flat Wrong (2018, Catholic Apologetics International Publishing, 736 pp.) — “Many flat earthers take statements Early Church Fathers made supporting geocentrism and then claim those statements show the early church believed in a flat earth”",
             url="https://eclalibraries.org/2019/06/23/6274/"),
        dict(label="Basil of Caesarea, Hexaemeron, Homily 1 §10 — the Earth “occupies the centre of the universe, its natural place”; the geocentric passage the source quotes",
             url="https://www.newadvent.org/fathers/32011.htm"),
        dict(label="Basil of Caesarea, Hexaemeron, Homily 9 §1 — declines to settle the Earth's shape: “If it be spherical or cylindrical, if it resemble a disc … or if it has the form of a winnowing basket and is hollow in the middle”",
             url="https://www.newadvent.org/fathers/32019.htm"),
        dict(label="Gregory of Nyssa, On the Soul and the Resurrection — verified verbatim: “because its spherical shape makes it impossible for it to be clasped all round at one and the same time by the rays”, quoted in the source's own footnote 574",
             url="https://www.newadvent.org/fathers/2915.htm"),
        dict(label="Augustine, City of God XVI.9 — “although it be supposed or scientifically demonstrated that the world is of a round and spherical form”: the antipodes are doubted, the sphere is not",
             url="https://www.newadvent.org/fathers/120116.htm"),
        dict(label="Thomas Aquinas, Summa Theologiae I q.1 a.1 ad 2 — “The astronomer and the physicist both may prove the same conclusion: that the earth, for instance, is round”",
             url="https://www.newadvent.org/summa/1001.htm"),
        dict(label="Sacrobosco, De sphaera mundi (c. 1230) — the standard university astronomy textbook for four centuries, 84 printed editions in two hundred years; ch. 1 proves the Earth spherical from eclipse timings, polar stars, the view from the masthead and the shape of water",
             url="https://en.wikipedia.org/wiki/De_sphaera_mundi"),
        dict(label="Myth of the flat Earth — Irving 1828, Letronne 1834, Draper 1874, White 1896; Russell, Inventing the Flat Earth (1991); Lindberg: “scarcely a Christian scholar of the Middle Ages who did not acknowledge Earth's sphericity”",
             url="https://en.wikipedia.org/wiki/Myth_of_the_flat_Earth"),
        dict(label="Cosmas Indicopleustes — the sixth-century Christian Topography; Lindberg: “the only medieval European known to have defended a flat earth cosmology”; three or four surviving manuscripts; refuted by John Philoponus",
             url="https://en.wikipedia.org/wiki/Cosmas_Indicopleustes"),
        dict(label="Jonathan Sarfati, “The flat earth myth”, Creation Ministries International — a young-earth creationist source on Bede (“We call the earth a globe … like a ball” rather than “like a shield”), Aquinas, Lactantius and Cosmas, Irving, Draper, White and Russell",
             url="https://creation.com/en/articles/flat-earth-myth"),
        dict(label="Catechism of the Council of Trent (1566), Creed Article I — “The earth, also, God commanded to stand in the midst of the world, rooted in its own foundation”: the likeliest referent of item 443, and it says nothing about shape",
             url="https://en.wikisource.org/wiki/The_Catechism_of_the_Council_of_Trent/Part_1:_Article_1"),
        dict(label="David Palm, “Geocentric Exaggerations: The Catechism of Trent”, GeocentrismDebunked.org — a Catholic apologist arguing that the Catechism passage concerns land and water, not the Earth's place in the cosmos",
             url="https://www.geocentrismdebunked.org/geocentric-exaggerations-the-catechism-of-trent/"),
        dict(label="Decree of approval for Settele's Elements of Astronomy, 16 August 1820, Pius VII — “no obstacles exist for those who sustain Copernicus' affirmation regarding the earth's movement”",
             url="https://inters.org/approval-Settele-heliocentric"),
        dict(label="Galileo affair — the 1758 removal of the general prohibition; Anfossi's 1820 refusal and its reversal; De revolutionibus and the Dialogo omitted from the 1835 Index",
             url="https://en.wikipedia.org/wiki/Galileo_affair"),
        dict(label="Levi Pingleton, “Canon Giuseppe Settele's Imprimatur”, published on Robert Sungenis's Substack, 5 February 2025 — the geocentrist reading stated in its own words: the imprimatur “did not refer to Galileo or to the sentence of 1633”",
             url="https://robertsungenis.substack.com/p/canon-giuseppe-setteles-imprimatur"),
        dict(label="William Carpenter, One Hundred Proofs That the Earth Is Not a Globe (1885) — full text; verified: zero occurrences of father, Augustine, Aquinas, patristic, scholastic, catechism, council or tradition",
             url="https://www.gutenberg.org/cache/epub/55387/pg55387.txt"),
        dict(label="The specimen list, “435 Pieces of Evidence The Earth is Not A Spinning Ball” — the nine items as they stand, with no citation of any father, scholastic, catechism or sermon",
             url="https://withthesun33.com/about-1")]),
}
