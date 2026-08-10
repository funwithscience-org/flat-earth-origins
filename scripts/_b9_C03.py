# -*- coding: utf-8 -*-
"""
Batch 9 — ARG-C03, "Proof-texts on foundations and pillars". 6 items, lane C,
verdict UNFALSIFIABLE, cluster record credits Rob Skiba (biblical-cosmology
teaching, 2015).

Operator constraint, honoured throughout and inherited from C02/C04: this page
never adjudicates whether God exists, whether scripture is true, or whether any
religious reading is correct — in either direction. Three questions are inside
the remit: what kind of claim is being made, whether measurement can settle it,
and whether the list represents its own source accurately.

WHAT THE SIX ITEMS ACTUALLY ARE (checked against corpus.py/assign.py, not assumed)

    68   Job 38:4 Earth's foundation.
    155  Job 38 Earth foundation.                <- same verse as 68
    410  Psalm 75:3 pillars of Earth.
    411  Job 9:6 shaken Earth.
    415  1 Sam 2:8 pillars set world.
    449  Biblical metaphors of "pillars," "foundations," "footstool."

So six items are five claims, and 449 is a category label for the other four
rather than a fifth verse. Item 412 — "Job 26:7 hangs on nothing" — is the NEXT
ITEM ON THE LIST after 411 and is filed as its own cluster, C10, whose verdict
is already SELF-CONTRADICTED "cited alongside the pillars-and-foundations texts
(C03)". The two sides of that contradiction are adjacent list entries.

THE BRIEF SAID LANE E. It is lane C. The "two sources, real science plus the
text that repurposes it" framing in the assignment does not apply here; the
C02/C04 framing does, and this entry follows it.

1. THE SOURCE IS REAL AND CARRIES ALL FIVE VERSES. Skiba's 2015-2016 teaching
   document "The Bible and the Still Flat Earth" has a dedicated section headed
   "Pillars of the Earth" which runs Job 38:4-6, 1 Samuel 2:8, 2 Samuel 22:16,
   Psalm 18:15, Psalm 75:3, Psalm 102:25, Psalm 104:5 and Jonah 2:6, gives the
   Hebrew for 'ammud and yasad, and uses Samson pulling down the pillars of the
   Philistine house (Judges 16) as the picture. On Job 38 he is at full strength,
   with no hedge: "If ever there was a Flat Earther, anti-globalist Scripture,
   this one is it." The refutation answers him at that strength.

2. WHERE THE PROVENANCE ACTUALLY GOES. The record's "Rob Skiba / 2015" is the
   proximate carrier, not the origin, and Skiba does not present himself as the
   origin — his own ADDITIONAL READING list links Schadewald's "The Flat-Earth
   Bible" and he block-quotes it elsewhere in the document (established at C04).
   Schadewald's 1987 essay already catalogues the foundations texts, and reports
   two earlier hands: Rowbotham's 76-scripture chapter in the 1865 second edition
   of Earth Not a Globe, and Anton Darms (assistant to Voliva) in 1930. Reported
   up in record_problems; clusters.py NOT touched.

3. THE FINDING THAT MATTERS, AND IT IS THE HEDGE RULE'S SECOND CLAUSE. Schadewald
   files the foundations texts under a heading he calls "Weaker Arguments", says
   such arguments "can help support a cumulative picture but are insufficient on
   their own", and writes: "Foundations are, however, fairly well-covered by
   geocentricity. No one would argue for a flat-earth solely on the basis of
   'foundations' quotes." The list makes six independently numbered proofs of
   exactly the class he ruled out using that way. And in the same essay he
   reports that Gerardus Bouw — the movement's own credentialed astronomer —
   "cites a barrage of scriptures about the foundations of the earth or world as
   evidence FOR SPHERICITY". The same proof-text set is deployed by both sides of
   the movement's internal shape dispute, which is the cleanest demonstration of
   non-discrimination this lane will produce.

4. THE TWO ORIGINATORS PUT DIFFERENT THINGS UNDERNEATH. Rowbotham 1865 handles
   Job 26:7 by quoting Adam Clarke and a Chaldee version to get "He layeth the
   Earth upon the waters", and his earth stands on a fathomless deep. The strings
   "pillar" and "corner stone" return zero hits in the Internet Archive OCR of
   that 1865 scan (item zeteticastronom00rowbgoog). Skiba 2015 handles the same
   verse by reading beli-mah as "not hung on ANYTHING" and puts the earth on
   'ammud pillars with a cornerstone. Both defuse the same verse; they land on
   incompatible substrates.

5. LEXICAL SPADEWORK, VERIFIED ON BIBLEHUB INTERLINEARS. Job 38:6 "foundations"
   is 'adaneha, Strong's H134, the tabernacle-socket word (57 occurrences,
   concentrated in Exodus 26-27). Job 9:6 and Psalm 75:3 "pillars" is 'ammud,
   H5982, a common word — concede that. 1 Samuel 2:8 "pillars" is metsuqe, H4690,
   which occurs twice in the OT: here and 1 Samuel 14:5, where it is a rock crag.
   Job 26:7's beli-mah, H1099, is a hapax — Skiba is RIGHT about that, and builds
   a two-or-three-witnesses rule (2 Cor 13:1) on it. Applied evenly, that rule
   goes badly for his own lead pillars text.

6. INSIDE THE TRADITION, THE QUESTION WAS NEVER SETTLED BY THE VERSE. Chagigah
   12b runs Job 9:6 — item 411's verse — as the proof text for pillars, then puts
   the pillars on water, the water on mountains, the mountains on wind, the wind
   on a storm, and the storm on God's arm; then records twelve pillars, seven
   pillars, and one pillar named Righteous. The regress and the disagreement are
   in the tradition itself.

7. QUOTE PROVENANCE. Skiba quotations were taken from the PDF at the S3 URL in
   `sources`, converted with pdftotext, and located by string search; page
   numbers in the PDF are not reliable, so the locator names the section heading
   instead. Schadewald quotations were retrieved from the dsimanek.vialattea.net
   copy and cross-checked against the cantab.net reprint, which agreed on the
   "Weaker Arguments" sentences.
"""

ENTRY = {

"C03": dict(

    tldr=("The Bible really does picture an earth with sockets, foundations and pillars, "
          "and anyone who denies it loses on the philology — the Talmud reads item 411's "
          "verse exactly that way, and the scholar Skiba himself quotes grants the point. "
          "What the argument needs is the next step, from what an ancient poem pictures to "
          "what a drill or a seismograph will find, and that step is supplied by the modern "
          "reader rather than by any text. Foundations also do not tell flat from round: the "
          "1987 catalogue Skiba's own reading list points to files them under a heading of "
          "weaker arguments, and reports a geocentrist astronomer citing the same verses to "
          "argue the opposite shape."),

    passage=dict(
        work="WRK-SKIBA-2018",
        locator=("The Bible and the Still Flat Earth, the 2015-2016 teaching document issued "
                 "through testingtheglobe.com, in the discussion of Job 38 that precedes the "
                 "section headed \"Pillars of the Earth\". Retrieved as PDF from the S3 URL in "
                 "sources and converted with pdftotext; the PDF's page numbering is unreliable, "
                 "so the section heading is the locator. Our work record WRK-SKIBA-2018 "
                 "catalogues Testing the Globe, the later book; the cluster's date of 2015 "
                 "belongs to the document, and the document is what is quoted."),
        pd=False,
        quote=("If ever there was a Flat Earther, anti-globalist Scripture, this one is it. "
               "How do you twist and distort that Scripture to fit a rotating globe, freely "
               "floating in space? Where is the “fastened foundation” with a "
               "“corner stone” in that model?"),
        gloss="""<p><strong>No hedge, and the page should say so plainly.</strong> Elsewhere Skiba writes that he makes no claim to the definitive answer &mdash; the disclaimer quoted at <a href="#ARG-C04">ARG-C04</a> &mdash; but that modesty is about his own standing, not about this claim. On Job 38:4&ndash;6 he asserts flat out that the verse cannot be read any other way, and he tells the reader what he wants done with it: <em>&ldquo;what if we just accept what it says, literally at face value?&rdquo;</em> The refutation below answers the literal reading at full strength, because that is the reading he asks for.</p>

<p><strong>What the source actually contains, which is more than the six items show.</strong> The teaching document has a dedicated section headed &ldquo;Pillars of the Earth&rdquo;. It runs Job 38:4&ndash;6, 1 Samuel 2:8, 2 Samuel 22:16, Psalm 18:15, Psalm 75:3, Psalm 102:25, Psalm 104:5 and Jonah 2:6; it gives the Hebrew for <em>&#7703;ammud</em> and <em>yasad</em>; and it grounds the picture in Samson pulling down the two middle pillars of the Philistine house (Judges 16:29&ndash;30), which is a fair illustration of what the word does elsewhere in the same corpus. It also does something the list does not: it argues. Skiba does not simply stack verses, he takes the standard counter-text head on.</p>

<p><strong>The counter-text is the next item on the list.</strong> His section opens by naming Job 26:7, <em>&ldquo;hangeth the earth upon nothing&rdquo;</em>, as the verse his opponents use, notes correctly that the Hebrew <em>beli-mah</em> occurs exactly once in the Hebrew Bible (Strong's H1099), invokes the two-or-three-witnesses rule of 2 Corinthians 13:1 against it, and then re-reads it: on his account Job is saying the earth is <em>not hung on anything</em> &mdash; because it is set on pillars &mdash; and Job 26:11, four verses later, gives pillars to heaven as well. On our own list Job 26:7 is item 412, which sits immediately after item 411 in the same numbered sequence, and it is filed as a separate cluster, <a href="#ARG-C10">ARG-C10</a>, already carrying the verdict SELF-CONTRADICTED. The two halves of that contradiction are adjacent entries, and the source the list is drawing on had already noticed the problem and written a reply to it.</p>

<p><strong>On provenance.</strong> Our cluster record names Skiba as originator, dated 2015. He is a real and traceable carrier &mdash; all five verses are in his document, in a section built around them. He is not the first hand. Robert Schadewald catalogued the foundations texts in <em>&ldquo;The Flat-Earth Bible&rdquo;</em> in July 1987, and Skiba's own ADDITIONAL READING list links that essay directly. Schadewald in turn records two earlier compilers: Samuel Rowbotham, who ran 76 scriptures in the closing section of the 1865 second edition of <em>Earth Not a Globe</em>, and Anton Darms, assistant to Wilbur Glenn Voliva, writing in 1930. This treatment therefore describes Skiba as the route these six items travelled, and names the documented earlier hands rather than crediting him with the compilation.</p>"""),

    steelman=dict(
        description="""<p><strong>SURFACE (weak &mdash; do not use).</strong> &ldquo;It is poetry, obviously.&rdquo; Said on its own this is a dodge and a well-read opponent will treat it as one, because the same reader who waves away the pillars as poetry usually wants Job 26:7 read as astrophysics. Consistency is the whole of Skiba's complaint and he is entitled to press it.</p>

<p><strong>DEEPER.</strong> The picture is really in the text and mainstream scholarship says so. The earth of the Hebrew Bible has <em>&#702;adanim</em> &mdash; sockets, Job 38:6, Strong's H134, the same word used 57 times mostly in Exodus 26&ndash;27 for the pedestals the tabernacle frames stood in &mdash; and a cornerstone, and a measuring line stretched across it. It has <em>&#7703;ammudim</em>, pillars, that tremble when God shakes it (Job 9:6, Psalm 75:3). Paul Seely reconstructed the flat, disc-shaped, water-founded earth of Genesis 1:10 in the <em>Westminster Theological Journal</em>, from inside a conservative inerrantist tradition. A defender who says only this has said something no competent scholar of the ancient Near East will contest.</p>

<p><strong>KERNEL.</strong> The strongest thing here is not a proof text at all; it is a methodological catch, and it lands. Skiba's section begins by observing that the sphericity apologists reach for one verse, Job 26:7, whose key word occurs once in the entire Hebrew Bible, and convert it into a statement about a planet held in orbit &mdash; while treating every architectural image around it as ornament. He is right that this is selective. He is right about the philology of <em>beli-mah</em>: it is a hapax legomenon, and its sense is genuinely obscure. And the professional judgement agrees with him about the conclusion, in the very article he cites: Robert Schneider of Berea College, writing in <em>Perspectives on Science and Christian Faith</em>, tells his students that the one thing Job 26:7 <em>&ldquo;certainly does not convey &hellip; is that of a spherical earth held by the force of gravity in space&rdquo;</em>, and adds that <em>&ldquo;the earth that hangs on nothing is also the earth that rests on &lsquo;pillars&rsquo;&rdquo;</em>. Skiba caught a real piece of eisegesis, and he caught it in the work of people who were arguing on his opponents' side. Concede all of that before saying anything else.</p>""",

        why_it_doesnt_save_claim="""<p>Because the catch cuts both ways and he keeps only one edge of it. Schneider's next sentence is the one that settles the matter: <em>&ldquo;I see no value in trying to reconcile these many and varied metaphorical images with our own image of a spherical, rotating planet.&rdquo;</em> The remedy for reading modern astronomy into an ancient poem is to stop reading modern astronomy into an ancient poem &mdash; not to read a different modern cosmology into it. A flat earth resting on load-bearing columns is still a twenty-first-century engineering claim being extracted from a text that was answering a different question. Schadewald, whose compilation this proof-text set descends from, put the same rule in one line: <em>&ldquo;it is a grave error to reinterpret ancient documents to force their authors to speak with modern voices.&rdquo;</em></p>

<p>And then there is the part the argument cannot survive on its own terms. Even granting the entire ancient picture &mdash; sockets, cornerstone, pillars, the lot &mdash; foundations say nothing about whether the ground is a disc or a ball. That is not an outsider's objection. It is the verdict of the man who assembled the corpus. Schadewald filed the foundations verses under a heading he wrote as <em>Weaker Arguments</em>, said such arguments <em>&ldquo;can help support a cumulative picture but are insufficient on their own&rdquo;</em>, and concluded: <em>&ldquo;Foundations are, however, fairly well-covered by geocentricity. No one would argue for a flat-earth solely on the basis of &lsquo;foundations&rsquo; quotes.&rdquo;</em> He then reported the proof of it: Gerardus Bouw, the movement's own credentialed astronomer, <em>&ldquo;cites a barrage of scriptures about the foundations of the earth or world as evidence for sphericity&rdquo;</em>. One proof-text set, two incompatible conclusions, both drawn inside the same movement. A set of verses that can be run either way is not evidence for either.</p>"""),

    refutation="""<p><strong>What this page adjudicates, and what it will not.</strong> The boundary is the one set at <a href="#ARG-C02">ARG-C02</a> and <a href="#ARG-C04">ARG-C04</a> and is not re-argued here: no position is taken on whether God exists, whether scripture is true, or which reading of a passage is correct, in either direction. Three questions are in the remit &mdash; what kind of claim is being made, whether measurement can settle it, and whether the list represents its own source accurately &mdash; and every section below is one of those three.</p>

<p><strong>1. The concession, first and without qualification.</strong> The Hebrew Bible pictures an earth with a built substructure. Job 38:6 asks on what its <em>&#702;adanim</em> were sunk and who laid its cornerstone, and <em>&#702;eden</em> is the word for the sockets the tabernacle frames stood in. Job 9:6 and Psalm 75:3 give it <em>&#7703;ammudim</em>, pillars, and <em>&#7703;ammud</em> is an ordinary, common word for a structural column &mdash; the same one used of the two middle pillars Samson takes hold of in Judges 16:29. Skiba's reading of those verses is not eccentric and it is not ignorant. It is roughly what the Babylonian Talmud does with the same verse: <em>&ldquo;Upon what does the earth stand? Upon pillars, as it is stated: &lsquo;Who shakes the earth out of its place, and its pillars tremble&rsquo; (Job 9:6).&rdquo;</em> That is item 411's verse, read for pillars, in the tradition's own commentary. Nothing on this page depends on denying any of it.</p>

<p><strong>2. The verdict attaches to a step, not to the reading.</strong> A text picturing a supported earth is a fact about the text. The claim on the list is a different claim: that because the text pictures it, the ground is built that way and an instrument would find it so. That inference is in no verse and no verse could carry it, because the question &mdash; what would a seismograph record &mdash; was not being asked or answered. The move from description to prediction is supplied entirely by the modern reader. That is what UNFALSIFIABLE marks here: not a judgement on the passages, which this review is not competent to make, but the observation that the load-bearing step has no support from the authority it invokes. The verdict is not a concession that the argument survives; sections 3 to 6 are the reasons it does not.</p>

<p><strong>3. The discriminating question, answered by the movement's own compiler.</strong> Every argument on this site is finally asked whether it distinguishes a flat, stationary earth from an ordinary globe. Foundations do not, and the person who says so most clearly is Robert Schadewald, whose 1987 essay is where this proof-text corpus was assembled in print and which Skiba's own reading list links. Schadewald put the foundations verses in a section he headed <em>Weaker Arguments</em>, wrote that arguments in that section <em>&ldquo;can help support a cumulative picture but are insufficient on their own&rdquo;</em>, and stated the conclusion in terms: <em>&ldquo;Foundations are, however, fairly well-covered by geocentricity. No one would argue for a flat-earth solely on the basis of &lsquo;foundations&rsquo; quotes.&rdquo;</em> He is not conceding this reluctantly &mdash; he is the one arguing that the Bible is a flat-earth book, and he still will not spend these verses on it.</p>

<p>The demonstration follows two paragraphs later in the same essay, and it is worth stating slowly. Schadewald reports that Gerardus Bouw, in an undated paper called &ldquo;The Form of the Earth&rdquo;, <em>&ldquo;cites a barrage of scriptures about the foundations of the earth or world as evidence for sphericity&rdquo;</em>, and adds that all or nearly all of the same verses had traditionally been used by flat-earthers to prove the earth flat. Bouw is not an opponent of this tradition; he is the geocentrist movement's only credentialed astronomer and appears elsewhere on this site as an originator. So the identical verses are run for a flat earth by one wing and for a spherical one by the other. A proof text that both sides of an internal dispute can cite for opposite conclusions is not evidence about the shape of anything. (Bouw's paper itself was not reachable from here; the report of its contents is Schadewald's, quoted above, and is presented as his.)</p>

<p><strong>4. The regress, which the tradition ran to the end and left open.</strong> Ask what the pillars stand on and the argument has to answer, because a support that needs no support is not doing the work the image promises. Chagigah 12b in the Babylonian Talmud asks precisely that, and stacks it: the pillars stand on water (Psalm 136:6), the water on mountains (Psalm 104:6), the mountains on wind (Amos 4:13), the wind on a storm (Psalm 148:8), and the storm <em>&ldquo;hangs upon the arm of the Holy One, Blessed be He&rdquo;</em> (Deuteronomy 33:27). It then records the disagreement rather than resolving it: the Rabbis say twelve pillars, some say seven, and Rabbi Elazar ben Shammua says <em>&ldquo;the earth rests on one pillar and a righteous person is its name&rdquo;</em> (Proverbs 10:25). That is a tradition treating &ldquo;what is underneath&rdquo; as a question the verse does not close, using the same verse, and ending in a theological answer rather than a structural one. It is also the exact point at which the modern argument stops: the six items reach a pillar and go no further.</p>

<p><strong>5. The movement's two named originators put different things underneath.</strong> This is not a debating point; it is a fact about the sources our own record names. Samuel Rowbotham reached Job 26:7 in the closing section of the 1865 second edition of <em>Earth Not a Globe</em>, and defused it &mdash; quoting Adam Clarke's literal rendering, <em>&ldquo;on the hollow or empty waste&rdquo;</em>, and a Chaldee version giving <em>&ldquo;He layeth the Earth upon the waters nothing sustaining it&rdquo;</em>. His conclusion is that the earth stands in and upon the waters of the great deep, whose depth he argues is boundless. The strings &ldquo;pillar&rdquo; and &ldquo;corner stone&rdquo; are not located anywhere in the Internet Archive OCR of that 1865 edition (item zeteticastronom00rowbgoog). Skiba, 150 years later, defuses the same verse the other way &mdash; <em>beli-mah</em> read as &ldquo;not hung on <em>anything</em>&rdquo; &mdash; and lands on pillars with a cornerstone. Two flat-earth authorities, one shared obstacle, two incompatible substrates: bottomless water and load-bearing columns. Both cannot be what the text describes, and the list carries only one of them; a search of the 461 items for the deep, the waters beneath or a floating earth returns nothing of Rowbotham's reading at all.</p>

<p><strong>6. The philology, since the argument is a philological one.</strong> Three separate Hebrew words are doing the work, and the items present them as one thing. Job 38:6 has <em>&#702;adaneha</em> (H134), sockets or pedestals, 57 occurrences concentrated in the tabernacle specifications of Exodus 26&ndash;27 &mdash; a tent-shrine word, and the surrounding verses supply the rest of the building yard: a measuring line stretched across it, a cornerstone laid. Job 9:6 and Psalm 75:3 have <em>&#7703;ammudeha</em> (H5982), and that one is common; concede it without argument. But 1 Samuel 2:8, the verse Skiba introduces as the place where <em>&ldquo;we get more details concerning this foundation&rdquo;</em>, has neither: it has <em>me&#7779;uqe</em> (H4690), a word that occurs twice in the Hebrew Bible &mdash; here, and at 1 Samuel 14:5, where it is a rocky crag Jonathan climbs. Skiba's own evidential rule is the two-or-three-witnesses standard of 2 Corinthians 13:1, and he applies it to rule Job 26:7 out of court for resting on a word used once. Applied evenly, that rule gives his lead pillars text two witnesses, one of which is a cliff in a battle narrative. Note also that within Job 26 itself the pillars belong to <em>heaven</em>, not to the earth: verse 11 has &ldquo;the pillars of heaven tremble&rdquo;. The imagery is architectural throughout and it is not consistently pointed at the ground.</p>

<p><strong>7. Where the claim is made physical it stops being a reading, and then it is measured.</strong> This section is here only because the source asks for it. Skiba's instruction is to <em>&ldquo;just accept what it says, literally at face value&rdquo;</em>, and a literal supported earth makes a checkable claim about what is beneath the ground. It has been checked, continuously, since 1906, and not by anyone looking for pillars. Seismic waves from large earthquakes travel through the planet and are recorded on the far side; the shadow zone in shear waves established a liquid outer core, Inge Lehmann's 1936 analysis of anomalous P&prime; arrivals established an inner core inside it, and in 2023 Pham and Tkal&#269;i&#263; reported compressional waves reverberating back and forth through the Earth's centre up to five times before dying away (<em>Nature Communications</em> 14:754). Those paths run from one side of the planet to the other and back; they pass through the region a pillar would have to occupy. What they find, all the way down and out the other side, is rock and iron under increasing pressure &mdash; a density profile, not a substructure. <strong>This does not refute anybody's reading of a poem, and it is not offered as though it did.</strong> It refutes the only version of the claim an instrument can be pointed at, which is the version the list's phrasing invites.</p>

<p><strong>8. The people arguing the other way here are frequently believers, and one of them is answering this exact pair of verses.</strong> Answers in Genesis &mdash; an organisation whose reason for existing is a literal reading of Genesis &mdash; published Erik Lutz on the tension between Job 26:7 and the pillars texts, concluding that <em>&ldquo;the supposed contradiction quickly disappears when we examine the context of each passage and recognize it as figurative language&rdquo;</em>, and that <em>&ldquo;we know that the earth does not literally have foundations and a cornerstone like a building.&rdquo;</em> Robert Schneider, whom Skiba quotes approvingly on Job 26:7, reaches the opposite reading of the same verse from within the same commitment to the text, and says the response the passage calls for <em>&ldquo;is awe, not scientific analysis.&rdquo;</em> Paul Seely, who grants the ancient flat-earth reconstruction in full, published it in a conservative Reformed journal and drew no modern conclusion from it. The fault line does not run between faith and science. It runs between ways of reading, and the strongest scholarly support for the ancient picture comes from people who take the text with complete seriousness and stop where the text stops.</p>

<p><strong>9. Inside our domain and failing: the list's fidelity to its own source.</strong> Four findings, all checkable against the 461 items and the teaching document. <em>Six items are five claims:</em> 68 (&ldquo;Job 38:4 Earth's foundation&rdquo;) and 155 (&ldquo;Job 38 Earth foundation&rdquo;) are the same verse entered twice. <em>Item 449</em> &mdash; &ldquo;Biblical metaphors of &lsquo;pillars,&rsquo; &lsquo;foundations,&rsquo; &lsquo;footstool&rsquo;&rdquo; &mdash; is a label for the category the other items already fill, and its footstool element belongs to the Matthew 5:35 item at <a href="#ARG-C06">ARG-C06</a>. <em>Item 411 is titled by the wrong half of its verse:</em> &ldquo;Job 9:6 shaken Earth&rdquo; foregrounds the clause the source lists under &ldquo;What about seeming contradictions such as&rdquo; and drops &ldquo;and the pillars thereof tremble&rdquo;, the clause he actually argues from. <em>And the contradiction is on the list twice, four entries apart:</em> item 411's pillars and item 412's earth hanging on nothing, filed as separate proofs, with the source's own reconciliation of them left behind. These are claims about the compilation, not about the passages.</p>

<p><strong>Verdict.</strong> UNFALSIFIABLE, in the precise and non-pejorative sense this review uses: what the six items assert is a reading of texts, and no measurement confirms or refutes a reading. Two things that verdict is not. It is not a finding that the argument is undamaged &mdash; it fails on its own ground, because the verses do not distinguish a disc from a globe and the movement's own compiler and its own astronomer between them demonstrate as much. And it is not a verdict on the texts, on the tradition, or on anyone's faith. The internal contradiction these items stand on one side of is recorded separately, at <a href="#ARG-C10">ARG-C10</a>.</p>""",

    advocate=dict(
        best_defense=(
            "Three of your nine sections attack Schadewald's opinion of my evidence, and "
            "Schadewald is an atheist debunker who spent his career against people like me. "
            "Quoting him at me as though he were my authority is a trick. My source is the "
            "text, and you have conceded the text: sockets, cornerstone, pillars, all of it, "
            "in your own first section. Second, your Talmud passage is my argument, not "
            "yours. You produced a rabbinic tradition that reads Job 9:6 for literal pillars "
            "and then ask me to be embarrassed that they could not agree on the count. "
            "Nobody in that passage suggests the earth is a ball. Third, your seismology is "
            "the category error you spent a whole section warning yourself about. You cannot "
            "say that the verdict attaches to a step from text to prediction and then run "
            "the prediction. Either measurement is relevant here or it is not; you want it "
            "both ways because section 7 is the only paragraph in the piece where you have "
            "an instrument. Fourth, you scored a point on 1 Samuel 2:8 and it costs you "
            "nothing that matters — 'ammud in Job 9:6 and Psalm 75:3 is common and you "
            "conceded it, so the pillars stand on two clean witnesses by my own rule. And "
            "fifth, the honest reader will notice what your verdict says. UNFALSIFIABLE "
            "means you cannot show I am wrong."),
        survives=4,
        preemptive=(
            "Four, and the number is set by the third and fifth moves rather than the first. "
            "Five changes were made in the body rather than left to the reader. (a) Section 3 "
            "now states that Schadewald is arguing FOR the flat-earth reading of the Bible "
            "when he sets the foundations verses aside, so the 'hostile witness' reply has "
            "nothing to grip: this is a concession against interest, not a critic's dismissal. "
            "The Bouw paragraph carries the real weight anyway and Bouw is not hostile at all. "
            "(b) Section 7 is explicitly bounded, in bold, to say that it does not touch "
            "anyone's reading of the text and is answering only the literal version the source "
            "itself asks for; the category-error charge is pre-answered by naming the source's "
            "own 'literally at face value' instruction as the reason the section exists. If an "
            "editor ever deletes that sentence the section becomes indefensible. (c) The "
            "'ammud concession is now made in the body twice, unprompted, in sections 1 and 6, "
            "so that the 1 Samuel finding is presented as narrow rather than as a takedown. "
            "(d) The verdict paragraph states in terms that UNFALSIFIABLE is not a concession "
            "of survival and points at the sections that do the damage, because the fifth "
            "objection depends entirely on reading it as one. (e) The Talmud paragraph now "
            "leads with the concession that the tradition reads Job 9:6 for pillars, and takes "
            "its point from the regress and the unresolved count rather than from any claim "
            "that the rabbis were globe-earthers, which they were not and which nothing here "
            "asserts."),
    ),

    straw_man=dict(
        identified=True,
        detail=("The straw man set for opponents is that a defender of the globe must read "
                "'foundations' as empty poetry while reading 'hangs on nothing' as literal "
                "astrophysics - inconsistency dressed as scholarship. Some apologists really "
                "do this: Schneider names Henry Morris reading the hydrological cycle, the "
                "earth's rotation and an expanding universe out of Job, and calls it eisegesis. "
                "But that is not the position under review here and it is not where the field "
                "sits. The mainstream reading takes both images the same way, as an ancient "
                "picture of the world, and Schneider states it flatly: the earth that hangs on "
                "nothing is also the earth that rests on pillars. The straw man this page has "
                "to avoid in return is treating the pillars reading as naive. It is not. It is "
                "what Chagigah 12b does with Job 9:6, what the comparative material from "
                "Mesopotamia and Egypt supports, and what a conservative inerrantist scholar "
                "argued in the Westminster Theological Journal. Calling it ignorant would be "
                "false as well as unkind, and it would hand the argument back."),
    ),

    compression=dict(
        assessed=True, drifted=True,
        list_phrasing=("Job 38:4 Earth's foundation. / Job 38 Earth foundation. / Psalm 75:3 "
                       "pillars of Earth. / Job 9:6 shaken Earth. / 1 Sam 2:8 pillars set "
                       "world. / Biblical metaphors of “pillars,” “foundations,” "
                       "“footstool.”"),
        source_wording=("Schadewald 1987, under his heading <em>Weaker Arguments</em>: such arguments "
                        "&ldquo;can help support a cumulative picture but are insufficient on their "
                        "own&rdquo; &mdash; &ldquo;Foundations are, however, fairly well-covered by "
                        "geocentricity. No one would argue for a flat-earth solely on the basis of "
                        "&lsquo;foundations&rsquo; quotes.&rdquo; Skiba 2015&ndash;2016, introducing "
                        "Job 9:6: &ldquo;What about seeming contradictions such as&hellip;&rdquo;"),
        drift_type="force_upgraded",
        note="""<p>Two drifts, and the second is the sharper one.</p>

<p><strong>The class of texts was scoped by the man who compiled it.</strong> This proof-text set reaches the modern lists through Robert Schadewald's 1987 essay &mdash; the compilation Skiba links in his own reading list &mdash; and Schadewald put the foundations verses in a section he headed <em>Weaker Arguments</em>, wrote that arguments there are &ldquo;insufficient on their own&rdquo;, and said in terms that nobody would argue for a flat earth from foundations quotes alone. Six independently numbered proofs is exactly the use he ruled out. The wording is untouched &mdash; the same verses, cited the same way &mdash; and what changes is the speech act: a class of evidence its own compiler down-rated arrives on the list as six standalone witnesses, which is the <a href="#ARG-R01">ARG-R01</a> pattern applied to a citation set instead of a sentence.</p>

<p><strong>Item 411 is titled by the half of its verse the source treats as a problem.</strong> In the teaching document Job 9:6 appears twice. In the &ldquo;Pillars of the Earth&rdquo; section Skiba uses it affirmatively, for the pillars. Earlier, under the question &ldquo;What about seeming contradictions such as:&rdquo;, he lists it first among the texts he has to reconcile with an immovable earth, and answers that shaking is not the same as removal &mdash; the earth may be knocked about without leaving its foundation. The list keeps the difficulty and discards the reply: item 411 reads &ldquo;Job 9:6 shaken Earth&rdquo;, with &ldquo;and the pillars thereof tremble&rdquo; &mdash; the clause the source argues from &mdash; dropped. On a list whose thesis is a stationary earth, the surviving half describes the earth being shaken out of its place.</p>

<p><strong>What did not drift, stated because the hedge rule cuts both ways.</strong> On Job 38 the source is at full strength and the items do not overstate him: &ldquo;If ever there was a Flat Earther, anti-globalist Scripture, this one is it.&rdquo; His disclaimers elsewhere are about his own standing, not the claim's strength, and it would be a misreading to record a hedge that is not being made. The refutation above answers the literal reading at the strength he states it, and grants the philology and the ancient picture in full before doing so.</p>

<p><strong>Bookkeeping, for the record.</strong> Six items are five claims &mdash; 68 and 155 are the same verse. Item 449 is a category label rather than a distinct claim, and its &ldquo;footstool&rdquo; element belongs with the Matthew 5:35 item at <a href="#ARG-C06">ARG-C06</a>. And the reconciliation the source wrote for Job 26:7 is not carried across: that verse is item 412, one place after item 411, filed as its own proof at <a href="#ARG-C10">ARG-C10</a>. The enum value recorded here is <em>force_upgraded</em>, which fits the first drift well and the second only approximately; the second is better described as a source's self-raised objection being promoted into evidence, and is set out above in its own words rather than forced into the box.</p>""",
    ),

    verdict_challenge=dict(challenged=False, proposed_verdict=None, reasoning=None),

    people=["PER-SKIBA", "PER-ROWBOTHAM", "PER-BOUW"],

    related=["C01", "C02", "C04", "C05", "C06", "C09", "C10", "D07"],

    sources=[
        dict(label="Rob Skiba, “The Bible and the Still Flat Earth” (© 2015–2016) — the teaching "
                   "document quoted; the section headed “Pillars of the Earth”, the Job 38 passage, "
                   "the beli-mah / two-witnesses argument, and the “seeming contradictions” list",
             url="https://s3.amazonaws.com/mychurchwebsite/c4890/the_bible_and_the_still_flat_earth_rob_skiba.pdf"),
        dict(label="Robert Schadewald, “The Flat-Earth Bible” (Bulletin of the Tychonian Society 44, "
                   "July 1987) — the “Weaker Arguments” section on foundations, the report of Bouw’s "
                   "“The Form of the Earth” citing the same verses for sphericity, and the "
                   "“grave error to reinterpret ancient documents” rule",
             url="https://dsimanek.vialattea.net/febible.htm"),
        dict(label="Schadewald, “The Flat-Earth Bible” — second copy, cross-checked for the "
                   "foundations and Job 26:7 passages",
             url="https://www.cantab.net/users/michael.behrend/ebooks/PlaneTruth/pages/Appendix_A.html"),
        dict(label="Samuel Rowbotham, Zetetic Astronomy: Earth Not a Globe, 2nd ed. (1865), Section XI, "
                   "printed pp. 198–201 — Job 26:7 answered via Adam Clarke and a Chaldee version, "
                   "and the earth founded on a fathomless deep",
             url="https://archive.org/details/zeteticastronom00rowbgoog"),
        dict(label="Robert J. Schneider, “Does the Bible Teach a Spherical Earth?”, Perspectives on "
                   "Science and Christian Faith 53 (2001) — the article Skiba himself cites; "
                   "“the earth that hangs on nothing is also the earth that rests on ‘pillars’”",
             url="https://www.asa3.org/ASA/PSCF/2001/PSCF9-01Schneider.html"),
        dict(label="Babylonian Talmud, Chagigah 12b (Sefaria, William Davidson translation) — Job 9:6 "
                   "read for pillars, the regress to water, mountains, wind and storm, and the "
                   "twelve / seven / one disagreement",
             url="https://www.sefaria.org/Chagigah.12b"),
        dict(label="Erik Lutz, “Contradictions: Hanging on Pillars of Nothing?”, Answers in Genesis — "
                   "a young-earth creationist organisation answering this exact pair of verses as "
                   "figurative language",
             url="https://answersingenesis.org/astronomy/earth/contradictions-hanging-on-pillars-of-nothing/"),
        dict(label="Strong’s H134, ʾeden — “base, pedestal, socket”, 57 occurrences, concentrated in "
                   "the tabernacle specifications; the word behind “foundations” at Job 38:6",
             url="https://biblehub.com/hebrew/134.htm"),
        dict(label="Strong’s H4690, māṣûq — the word behind “pillars” at 1 Samuel 2:8; two "
                   "occurrences, the other being the crag at 1 Samuel 14:5",
             url="https://biblehub.com/hebrew/4690.htm"),
        dict(label="Strong’s H1099, belîmaʿ — hapax legomenon, Job 26:7 only; Skiba is correct about "
                   "this and builds his two-witnesses argument on it",
             url="https://biblehub.com/hebrew/1099.htm"),
        dict(label="Paul H. Seely, “The Geographical Meaning of ‘Earth’ and ‘Seas’ in Genesis 1:10”, "
                   "Westminster Theological Journal 59 (1997) — the flat, water-founded earth "
                   "reconstructed from inside a conservative inerrantist tradition",
             url="https://www.galaxie.com/article/wtj59-2-06"),
        dict(label="Pham & Tkalčić, “Up-to-fivefold reverberating waves through the Earth’s centre "
                   "and distinctly anisotropic innermost inner core”, Nature Communications 14:754 "
                   "(2023) — seismic paths straight through the region a pillar would occupy",
             url="https://www.nature.com/articles/s41467-023-36074-2"),
    ]),
}
