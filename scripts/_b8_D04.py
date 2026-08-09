# -*- coding: utf-8 -*-
"""Batch 8 — D04, axis mundi / world tree / omphalos symbolism.

Sibling of D06 in the esoteric lane and the same category error one step further out:
D06 found a Hermetic maxim about planes of Being entered as a claim about the sky;
D04 finds a comparative historian's description of how myths organise sacred space
entered as evidence about the shape of the Earth. Three house constraints held:
the page adjudicates nothing about whether any tradition is true; unfalsifiable
claims are named, not ridiculed; and Eliade is answered at his own strength, which
is higher than "it's only symbolism" allows.

FOUR THINGS FOUND, all of them checkable:

  * ELIADE'S OWN TEXT RULES OUT THE GEOGRAPHICAL READING. The 1949 section reports
    rather than asserts — "According to Indian beliefs, Mount Meru rises at the center
    of the world" — and in the 1957 book the rule is explicit: the multiplicity of
    centres raises no difficulty, because what is at issue is not geometrical space.
    The list's use of the material needs precisely the reading he excludes.

  * THIRTEEN NAVELS, FIVE CONTINENTS. Delphi, the Foundation Stone, Calvary, Israel,
    Bodh Gaya, Hagia Sophia, Babylon, Paphos, Mount Song, Cusco, Baboquivari Peak,
    Rapa Nui, Mir Mine. On the geographical reading at most one can be right; on
    Eliade's reading all thirteen are consistent and nothing needs adjudicating.

  * THE NAMED TRADITIONS' OWN ASTRONOMY ANSWERS THE OTHER WAY, and only against the
    flat half of the list. The Sūrya Siddhānta puts Meru at the north pole of a
    spherical Earth and places a polar star at the zenith of EACH pole — two poles,
    which is the globe's geometry. It is also geocentric, and the entry says so.

  * THE SPECIMEN NAMES NOBODY. Fetching withthesun33.com/about-1 on 2026-08-09 and
    searching the full retrieved text turned up no author or work beside any of the
    six items. Eliade and Guénon are OUR reconstruction of the ancestry, not a
    citation the compiler made.

FOR THE PARENT — a record-level issue I could not fix, because clusters.py is not my
file and eleven other agents are writing right now:

  clusters.py D04 (and D05) set originator="Mircea Eliade (misapplied)". The field is
  documented as "the person who introduced this argument into the flat-earth or
  geocentric canon (NOT the person who repeated it)". Eliade introduced nothing into
  that canon; the "(misapplied)" parenthesis flags the problem without resolving it,
  and PER-ELIADE consequently appears on the People tab as an originator of a
  flat-earth argument. This is the shape of the C02 case: two corrections to one field
  would both be wrong because the FIELD is wrong. The candidate states are
  originator=None, or pre_modern with the centre-symbolism recorded as older than the
  movement and its repopularisers named. One documented modern repopulariser exists
  and is in the sources below: Eric Dubay, Flatlantis (2020), advertised as an inquiry
  into "Mount Meru, the alleged magnetic mountain ancient cultures worldwide believed
  existed at the North Pole" — a physical claim Eliade does not make. Whether the
  specimen drew on Dubay is NOT established and must not be asserted. Nothing about
  this appears in the published prose of this entry; it is here and in advocate mode
  only, per the past-tense rule.

Also for the parent: there is no PER-* id for René Guénon, though he is half of D04's
real_source line and is the strongest form of this argument. `people` therefore lists
PER-ELIADE alone.
"""

ENTRY = {

"D04": dict(

    verdict_challenge=dict(
        challenged=False, proposed_verdict=None,
        reasoning=("Considered SELF-CONTRADICTED and rejected it, the same trade D07 made. "
                   "The case is real and is published in the body: the Sūrya Siddhānta, which "
                   "is where item 173's Meru comes from, puts Meru at the north pole of a "
                   "sphere and a polar star at the zenith of each of two poles; Gylfaginning "
                   "sends Yggdrasil's three roots in three directions, one of them up into "
                   "heaven; Pausanias reports the Delphi navel as what the Delphians say; and "
                   "the Jerusalem-centred world maps were drawn by people who knew from "
                   "Aristotle that the world is spherical. Four of the six items therefore "
                   "point away from their own use. But UNFALSIFIABLE is still the better "
                   "description, for the reason the verdict exists: the items as written "
                   "assert only that these symbols exist, and they do exist. Nothing "
                   "measurable is put at risk by the assertion, so nothing measurable can "
                   "contradict it — including the four contradictions above, which land on "
                   "the geographical reading the items never quite state. Better to publish "
                   "the contradictions inside the entry than to make them carry a verdict "
                   "they only reach once a premise has been supplied on the claimant's "
                   "behalf. A second reading was also weighed and rejected: that the "
                   "empirical sub-claim — that this pattern is universal — is falsifiable, "
                   "was tested by Jonathan Z. Smith, and did not survive, so the cluster is "
                   "part-falsifiable. True of Eliade's scholarship, but the list does not "
                   "make the universality claim load-bearing; item 451's 'worldwide' is "
                   "decoration on a claim that would be equally unfalsifiable with one "
                   "example.")),

    tldr=("At least thirteen places on five continents have been called the navel of the world, "
          "and on any geographical reading at most one of them can be right. Eliade's account survives "
          "that only because it was never geographical: the multiplicity of centres, he wrote, "
          "raises no difficulty for religious thought, because what is at issue is not "
          "geometrical space. The list takes a comparative category built to describe how myths "
          "organise sacred space and enters it six times as evidence about the shape of the "
          "Earth — and where the traditions it names did astronomy, they answered the other "
          "way, the Sūrya Siddhānta putting Meru at the north pole of a sphere with a polar "
          "star at the zenith of each of two poles."),

    passage=dict(
        work="WRK-ELIADE-1949", pd=False,
        locator=("The Myth of the Eternal Return (Le Mythe de l'éternel retour, 1949), ch. I "
                 "“Archetypes and Repetition”, section “The Symbolism of the Center”; Willard R. "
                 "Trask's English translation, read in the online transcription at The Ted K "
                 "Archive. Printed page numbers not checked against a print copy — the section "
                 "sits early in ch. I in the Princeton/Bollingen pagination"),
        quote=("The Sacred Mountain—where heaven and earth meet—is situated at the center of the "
               "world. … Being an axis mundi, the sacred city or temple is regarded as the "
               "meeting point of heaven, earth, and hell. … According to Indian beliefs, Mount "
               "Meru rises at the center of the world, and above it shines the polestar."),
        gloss=(
            "<p>Read the grammar before the content. The first two sentences are a "
            "<em>schema</em>: Eliade is setting out, in numbered points, the structure he says "
            "the material shares. The third sentence is the schema being applied, and it "
            "carries a reporting frame &mdash; <em>according to Indian beliefs</em>. That frame "
            "is the whole finding in miniature. A historian of religion writing that Meru "
            "rises at the centre of the world according to Indian beliefs has said something "
            "about Indian beliefs. He has said nothing whatever about where any mountain is.</p>"

            "<p>The frame is not an isolated politeness. Eight years later, in "
            "<em>The Sacred and the Profane</em> (ch. 1), Eliade states the governing rule "
            "outright: &ldquo;The multiplicity, or even the infinity, of centers of the world "
            "raises no difficulty for religious thought&rdquo;, because this is &ldquo;not a "
            "matter of geometrical space, but of an existential and sacred space that has an "
            "entirely different structure, that admits of an infinite number of breaks.&rdquo; "
            "A geographer who found a hundred rival centres would have a contradiction on his "
            "hands and would have to adjudicate. Eliade has no contradiction, and says so, "
            "because his subject is how sacred space is organised in myth and rite rather than "
            "where anything sits on a survey. <strong>The list's use of this material requires "
            "exactly the reading its own authority excludes.</strong></p>"

            "<p>Now the honest complication, because a defender will reach for it and should "
            "find it conceded rather than hidden. Eliade is not a deflationary writer. In the "
            "same chapter he calls the Centre &ldquo;pre-eminently the zone of the sacred, the "
            "zone of absolute reality&rdquo;, and he was criticised for decades &mdash; by "
            "Jonathan Z. Smith among others &mdash; for a method that reads as theology with "
            "footnotes. Take that at full strength. It still does not convert into geography, "
            "because what Eliade means by reality here is participation in an archetype, an "
            "ontology he attributes to archaic thought and describes from the outside. The "
            "Centre is real in his sense whether the Earth is a disc, a sphere or a "
            "dodecahedron, which is why he can put thirteen of them on five continents without "
            "embarrassment.</p>"

            "<p>The second name on this cluster's source line is René Guénon, and he is a "
            "different case that deserves stating plainly, because he is the stronger witness. "
            "Guénon was not describing other people's beliefs; he held that traditional symbols "
            "express a real supra-sensible order, and he had no patience for readings that make "
            "a symbol &ldquo;merely&rdquo; a symbol. Even so, the sentence in "
            "<em>Le Roi du Monde</em> (1927) that states his axis doctrine keeps the adverb: "
            "the centre, he writes in ch. 2, &ldquo;constitutes the fixed point known "
            "<em>symbolically</em> to all traditions as the &lsquo;pole&rsquo; or axis around "
            "which the world rotates.&rdquo; A world that rotates about a pole is the geometry "
            "the list is trying to argue against. Guénon's ch. 9, &ldquo;The Omphalos and "
            "Sacred Stones&rdquo;, is the chapter that bears directly on items 453 and 454; the "
            "archive.org transcription we fetched terminated in ch. 6, so that chapter is "
            "recorded here as unread rather than characterised.</p>")),

    steelman=dict(
        description=(
            "<p><strong>SURFACE (weak &mdash; do not use).</strong> &ldquo;These are myths, and "
            "myths are not evidence.&rdquo; It loses on contact. Nobody involved claims the "
            "Prose Edda is a survey report, so the sentence answers a position no one holds; "
            "and it walks straight into Eliade's own vocabulary, where the Centre is &ldquo;the "
            "zone of absolute reality&rdquo;. Say &ldquo;only symbolism&rdquo; to a "
            "traditionalist and you have started a metaphysical argument you did not need to "
            "have and cannot win by measurement.</p>"

            "<p><strong>DEEPER.</strong> The convergence is real data. Peoples with no contact "
            "produced the same figure &mdash; a vertical connector at a centre, joining an "
            "upper, a middle and a lower region &mdash; and independent convergence is the sort "
            "of thing that normally demands an explanation rather than a shrug. True, and "
            "it is where the honest version of this argument starts. But on its own it is "
            "incomplete, because it establishes that something needs explaining without "
            "establishing what.</p>"

            "<p><strong>KERNEL.</strong> The strongest form of the argument is not Eliade's and "
            "does not need him. It is Guénon's, and it is a refusal of the question. On the "
            "traditionalist account, sacred geography is not a poetic dressing laid over "
            "profane geography; it is prior to it, and the demand that the world axis show up "
            "on a theodolite is a category error committed by the <em>critic</em>, who has "
            "silently assumed that measurable space is the only space there is. That is a "
            "coherent position with a long pedigree, it is held by serious people, and "
            "answering it with &ldquo;go and look, there is no pole&rdquo; concedes its "
            "central charge. Grant the whole of it.</p>"),
        why_it_doesnt_save_claim=(
            "<p>Because granting the whole of it grants nothing to <em>this list</em>. An order "
            "defined as not reachable by measurement is not reachable by measurement in the "
            "claimant's favour either. Guénon's axis is exactly as available to a rotating "
            "globe as to a stationary disc &mdash; his own sentence has the world rotating "
            "about it &mdash; which is why the identical symbolism has been recited with "
            "conviction by people holding mutually incompatible pictures of the sky. "
            "<strong>A premise compatible with every geometry distinguishes none of them.</strong> "
            "The kernel buys immunity from refutation at the price of any power to support, and "
            "the list needs support.</p>"

            "<p>The convergence argument fails for a different and more interesting reason: it "
            "proves too much, and the surplus is checkable. Thirteen navels of the world are "
            "documented across five continents. If the convergence is testimony to a fact of "
            "geography, twelve witnesses are lying and there is no principled way to pick the "
            "twelfth. If it is testimony to something about how human communities organise "
            "meaning around wherever they happen to be standing, all thirteen are consistent, "
            "nothing needs adjudicating, and the pattern is fully explained &mdash; which is "
            "the reading Eliade gives and the reason he can list them without discomfort.</p>"

            "<p>And the empirical half of the kernel, the universality that makes convergence "
            "look like data, is the one part of this that was ever put at risk &mdash; by a "
            "historian of religion, not by a physicist. Jonathan Z. Smith went to Eliade's "
            "showpiece case and found the exhibit assembled rather than observed. The scope of "
            "that result is stated carefully in the body below, because Smith himself scoped "
            "it carefully.</p>")),

    refutation=(
        "<p><strong>1. What is being claimed, at its own strength.</strong> Eliade's claim is "
        "that a great many traditions organise space around a centre where the cosmic regions "
        "meet, that temples and cities reproduce that centre, and that this structure is close "
        "to universal. He states it firmly; he was criticised for stating it too firmly. Every "
        "word of it can be granted here, because it is a claim about <em>myth and rite</em> and "
        "he says so in the sentence that introduces the material: Meru rises at the centre of "
        "the world <em>according to Indian beliefs</em>. The rule governing the whole "
        "construction is set out explicitly in his 1957 book: the multiplicity, even the "
        "infinity, of centres of the world raises no difficulty, because the space at issue is "
        "not geometrical space. That is a scholar telling you, in advance, that his centres are "
        "not locations. Six items of this list use them as locations.</p>"

        "<p><strong>2. Thirteen navels, five continents.</strong> The places for which a "
        "&ldquo;navel of the world&rdquo; claim is documented include Delphi; the Foundation "
        "Stone in Jerusalem; Calvary, also in Jerusalem; the land of Israel itself, on the "
        "strength of <em>tabbûr ha-'areṣ</em> at Ezekiel 38:12; the Bodhi Tree at Bodh Gaya; "
        "Hagia Sophia; Babylon; the altar at Paphos; Mount Song and nearby Luoyang in central "
        "China; Cusco, in Inca tradition; Baboquivari Peak in Arizona, for the O'odham; a site "
        "near Ahu Te Pito Kura on Rapa Nui; and, in a modern Soviet-era instance, the Mir mine "
        "in Sakha. Two of them are under a kilometre apart and still counted separately. "
        "Read as geography this is not a convergence at all, it is a dispute, and it has no "
        "resolution procedure. Read as Eliade reads it, there is nothing to resolve. "
        "<strong>The list needs the first reading; the evidence supports the second.</strong> "
        "The Delphic case even carries its own attribution: Pausanias, walking round the "
        "sanctuary in the second century, writes that the stone &ldquo;is made of white marble, "
        "and is said by the Delphians to be the centre of all the earth&rdquo; "
        "(<em>Description of Greece</em> 10.16.3). <em>Said by the Delphians.</em> The founding "
        "myth is equally frank about the method: Zeus released two eagles from the ends of the "
        "world and marked the point where they crossed. That is an etiology for a stone, and it "
        "is the kind of thing a community says about its own sanctuary.</p>"

        "<p><strong>3. Where these traditions did astronomy, they answered the other way &mdash; "
        "and only against half the list.</strong> This section is scoped deliberately, because "
        "the material cuts unevenly and pretending otherwise would be the error this review "
        "exists to catch.</p>"

        "<p><em>Meru</em> (item 173). The Sanskrit astronomical tradition did not treat Meru as "
        "a mountain at the middle of a plane. The <em>Sūrya Siddhānta</em> holds that the Earth "
        "is a sphere &mdash; <em>bhūgola</em>, literally earth-ball &mdash; and gives it a "
        "diameter of 1,600 yojanas; its twelfth chapter, on cosmography, places Meru at the "
        "Earth's north pole and states that on both sides of Meru, at the north and south poles "
        "of the Earth, a polar star stands at the zenith. <strong>Two poles.</strong> That is "
        "the geometry of a globe, written into the very text that supplies the item's "
        "vocabulary. Now the concession that has to go with it: the <em>Sūrya Siddhānta</em> is "
        "geocentric. It has a stationary globe with the Sun and planets going round it. So item "
        "173's own source contradicts the flat half of this list and supports the "
        "Earth-at-rest half. Saying so costs nothing and is the difference between an argument "
        "and a talking point.</p>"

        "<p><em>Yggdrasil</em> (item 174). <em>Gylfaginning</em> 15 gives the tree three roots "
        "running to three different places: one among the Æsir, with the holy well Urðarbrunnr "
        "beneath it, and that root extends to heaven; one among the frost jötnar, over "
        "Mímisbrunnr; one over Niflheim, where Níðhǫggr gnaws and Hvergelmir lies. A single "
        "vertical pole driven through a flat plane is a diagram somebody drew later. The Edda "
        "gives a branching structure whose roots run in three directions, one of them upward, "
        "and it will not flatten into an axis without help.</p>"

        "<p><em>Jerusalem</em> (item 454). The Jerusalem-at-the-centre world maps of the Latin "
        "Middle Ages are the strongest-looking case and the weakest on inspection. They are "
        "products of a culture that knew the Earth was a sphere: it was &ldquo;known from "
        "Aristotle that the world was spherical&rdquo;, and the maps themselves are &ldquo;"
        "primarily symbolic &hellip; of little use for accurate navigation, but designed as "
        "historical and educational tools&rdquo;. Jerusalem sits at the middle because of the "
        "crucifixion, not because of a survey. A centred map is a statement about "
        "<em>significance</em>. Every underground railway diagram in the world makes the same "
        "move and nobody reads them as claims about topology.</p>"

        "<p><strong>4. The one place this was ever tested, and by whom.</strong> Not by physics. "
        "The universality claim is a claim in the history of religions, and it was attacked "
        "there, in Jonathan Z. Smith's <em>To Take Place</em> (1987), whose opening chapter "
        "takes Eliade's showpiece &mdash; the Achilpa or Tjilpa sacred pole of central Australia "
        "&mdash; and goes back to the ethnography. Three findings. The single creator figure "
        "&ldquo;Numbakulla&rdquo; is an artefact of the 1927 Spencer and Gillen recension "
        "Eliade used rather than of the earlier reports: &ldquo;A common corporate name for "
        "ancestors has been reinterpreted as the proper name of a single figure&rdquo; (p. 5). "
        "The two incidents Eliade fuses &mdash; the ascent and the breaking of the pole &mdash; "
        "sit thirty pages apart in the source, among other tales, and are &ldquo;typical "
        "narrative units &hellip; not extraordinary, highly dramatic events to be lifted out "
        "and focused upon&rdquo; (p. 8). And the emphasis of the myth cycle runs the wrong way "
        "for a cosmic axis: its horizon &ldquo;is not celestial, it is relentlessly terrestrial "
        "and chthonic&rdquo;. Smith's positive proposal is worth more than the demolition: "
        "&ldquo;The language of &lsquo;center&rsquo; is preeminently political and only "
        "secondarily cosmological&rdquo; &mdash; centres are declared by people with the "
        "standing to declare them, which is a hypothesis that predicts thirteen navels rather "
        "than being embarrassed by them.</p>"

        "<p>Scope this honestly, because Smith did. He is not claiming that centre-symbolism is "
        "a fiction everywhere; he writes that &ldquo;such understandings of place &hellip; can "
        "be found within the history of religions &hellip; but they are not present in the "
        "Tjilpa myth&rdquo; (p. 10). What fell was the universality of the pattern and the "
        "standing of its most famous exhibit. That is a serious loss for a comparative argument "
        "that runs on ubiquity, and it happened inside Eliade's own discipline, on his own "
        "evidence.</p>"

        "<p><strong>5. What kind of claim the six items are, which is the verdict.</strong> Item "
        "451 says axis mundi symbols occur worldwide. They do. Item 453 says omphalos stones "
        "mark a world navel. They do. Item 174 says the Norse had Yggdrasil. They did. Every "
        "one of the six is true as written, and Eliade would dispute none of the nouns. What "
        "makes them items on a document headed <em>435 Pieces of Evidence The Earth is Not A "
        "Spinning Ball</em> is an inference that is nowhere written down: that because many "
        "peoples pictured a centre and an axis, there is one. The inference is not defended, "
        "and it cannot be checked, because no observation can show that a symbol has been read "
        "wrongly. Point a theodolite where you like; the reply that the axis is not that kind "
        "of axis is always available and is, on Eliade's and Guénon's own accounts, correct. "
        "<strong>That is what UNFALSIFIABLE names here, and it is a description of the claim's "
        "form, not a verdict on anybody's religion.</strong> This entry takes no position on "
        "whether any of these traditions is true, and none is needed: the question asked "
        "throughout is only what kind of claim is being made and whether the list represents "
        "the source it descends from.</p>"

        "<p><strong>6. The one point of contact with measurement, and it goes the other way.</strong> "
        "There is a real world axis. The sky turns about it once a sidereal day, and Eliade's "
        "own sentence notices it: above Meru &ldquo;shines the polestar.&rdquo; So take the "
        "symbolism at its most literal for one paragraph and see what it predicts. A rotation "
        "axis through a globe gives two celestial poles and two circumpolar skies, and that is "
        "what observers find: a northern sky wheeling anticlockwise about Polaris and a "
        "southern sky wheeling clockwise about a point in Octans that has no bright star near "
        "it at all, the nearest naked-eye candidate being σ Octantis at about magnitude 5.5. "
        "The axis also drifts. Precession carries the north celestial pole around a circle in "
        "roughly 25,800 years: Thuban held the position around 2700 BCE, Polaris holds it now "
        "and is closest around 2100 CE, and Vega will hold it in about twelve thousand years. "
        "None of that follows from a pole erected at the middle of a plane, and all of it "
        "follows from a spinning ball. The <em>Sūrya Siddhānta</em>, again, already has the "
        "two-pole version &mdash; a polar star at the zenith of each pole &mdash; which means "
        "the tradition item 173 invokes had worked this out and written it down.</p>"

        "<p><strong>Verdict: unfalsifiable, and misattributed in transit.</strong> The six items "
        "report a symbolism accurately and then do nothing with it that can be checked. The "
        "scholar whose category they borrow set out, in the section they borrow it from, the "
        "rule that forbids the use they make of it. And where the traditions named kept their "
        "own astronomical records, those records describe a sphere with two poles.</p>"),

    advocate=dict(
        best_defense=(
            "You have written a careful essay against a claim nobody made. The six items say "
            "these symbols exist; you agree they exist; so what has been refuted? Meanwhile "
            "you have conceded the interesting half. Eliade did claim near-universality and "
            "you have not shown it false — your own witness scopes his result to one Australian "
            "myth and says in terms that such understandings of place are found elsewhere in "
            "the history of religions. Thirteen navels is not a contradiction, it is a pattern, "
            "and patterns want explaining; 'people put the centre where they stand' is a "
            "hypothesis, not a measurement, and you have not tested it either. Worst of all, "
            "your best factual hit cuts your own way. The Sūrya Siddhānta you march out against "
            "Meru puts a stationary Earth at the centre of the cosmos. You have used a "
            "geocentric text to attack geocentrism's ancestors, and if I may cite it for the "
            "part you like, I may cite it for the part you do not."),
        survives=4,
        preemptive=(
            "Rate this 4. The last barb is a genuine hit and the 'what have you refuted' line "
            "is the one a reader will feel. Four concrete changes, all made in the text above; "
            "do not soften them in edit. (a) §3 now concedes the Sūrya Siddhānta's geocentrism "
            "IN THE SAME PARAGRAPH as the Meru point and scopes the argument explicitly to the "
            "flat half of the list — the concession is made before the defender can make it, "
            "and the sentence 'saying so costs nothing and is the difference between an "
            "argument and a talking point' stays. (b) §4 quotes Smith's own limiting sentence "
            "(p. 10) and adds a scope paragraph saying what did and did not fall, so the "
            "over-reading is closed off from inside. (c) §5 answers 'what have you refuted' "
            "head-on: the items are true as written, the inference is unwritten, and "
            "UNFALSIFIABLE is a description of claim-form rather than a dismissal of anyone's "
            "religion. (d) The navels material was moved out of the refutation's "
            "opening and into a position where it supports Smith's political hypothesis rather "
            "than standing as a bare tally, which is what makes it an explanation and not just "
            "a list. Two further notes for whoever edits this. FIRST, do not let anyone "
            "recast the entry as 'Eliade debunked'. Eliade is not the opponent here; he is the "
            "witness for the defence of the symbolic reading, and the entry is weaker every "
            "time it sounds otherwise. SECOND, and this is the one thing I could not do: "
            "clusters.py D04 and D05 record originator='Mircea Eliade (misapplied)' in a field "
            "documented as naming the person who introduced the argument into the flat-earth "
            "canon. He did not. The specimen names no author for any of these six items — "
            "searched in the full text retrieved from withthesun33.com/about-1 on 2026-08-09 — "
            "so the ancestry is our reconstruction, and the field's honest values are "
            "originator=None or the pre_modern state with repopularisers named. That file is "
            "not mine to edit and the parent has been told. Nothing about it appears in the "
            "published prose, per the past-tense rule.")),

    straw_man=dict(
        identified=True,
        detail=("Two, and the larger one does not point at us. The list's implied opponent is "
                "someone who says these symbols are trivial, or that the cultures that made "
                "them were foolish. Nobody holds that; the symbolism is a real and serious "
                "object of study, which is why a professor at Chicago spent a career on it. "
                "The misrepresentation that does occur runs towards the traditions themselves: "
                "item 160 calls it a “doctrine”, which promotes a twentieth-century "
                "comparative category into something the Achilpa, the Norse, the Delphians and "
                "the compilers of the Sūrya Siddhānta are made to have taught in "
                "common. They did not share a doctrine; sharing one is what the word smuggles "
                "in. The trap on our side is the mirror image and is worth naming so we do not "
                "fall into it: characterising Eliade as a neutral cataloguer of quaint beliefs "
                "would be its own straw man, since he calls the Centre the zone of absolute "
                "reality and meant it. The entry concedes that where it belongs, in the gloss, "
                "and answers it rather than pretending it away.")),

    compression=dict(
        assessed=True, drifted=True,
        list_phrasing=("Axis mundi doctrine. / Hindu Mount Meru axis. / Norse Yggdrasil. / Axis "
                       "mundi symbols (world tree, mountain) worldwide. / Omphalos stones "
                       "marking the world's navel/center. / Jerusalem/Delphi as “navel of the "
                       "world” motifs. (items 160, 173, 174, 451, 453, 454, entered as numbered "
                       "evidence that the Earth is not a spinning ball)"),
        source_wording=("“Being an axis mundi, the sacred city or temple is regarded as the "
                        "meeting point of heaven, earth, and hell. … According to Indian "
                        "beliefs, Mount Meru rises at the center of the world, and above it "
                        "shines the polestar.” — and the governing rule, from the same author: "
                        "“The multiplicity, or even the infinity, of centers of the world "
                        "raises no difficulty for religious thought”, since it is “not a matter "
                        "of geometrical space”."),
        drift_type="category_shifted",
        note=("<p>The words barely move, and item 451's are honest: it says <em>symbols</em>, "
              "which is what they are, and Eliade would dispute not one of the six nouns. What "
              "moves is the category. A comparative historian's description of how myths "
              "organise sacred space, hedged with reporting frames and governed by an explicit "
              "rule that the space in question is not geometrical, is entered six times as "
              "numbered evidence in a document headed <em>435 Pieces of Evidence The Earth is "
              "Not A Spinning Ball</em>. Nothing is misquoted. The claim has changed kind.</p>"

              "<p>One place the wording does shift, and it is the tell. Item 160 says "
              "&ldquo;axis mundi <strong>doctrine</strong>&rdquo;. A symbolism is a way of "
              "using images; a doctrine is a proposition that is taught, believed and — this is "
              "the point — <em>asserted about the world</em>. The single word converts an "
              "observed family resemblance among unrelated traditions into a shared teaching "
              "they can be quoted as holding. Item 451's &ldquo;worldwide&rdquo; does the "
              "complementary work, supplying the ubiquity that makes the resemblance look like "
              "convergent testimony. Together they are the whole argument, and neither is "
              "argued.</p>"

              "<p><strong>What we could and could not establish about the chain.</strong> No "
              "author or work stands beside any of the six items: the full text retrieved from "
              "the specimen page on 2026-08-09 was searched and carries no attribution for "
              "them, nor for the neighbouring esoteric items. Eliade and Guénon are this "
              "review's reconstruction of where the vocabulary comes from, not a citation the "
              "compiler made, and no intermediate text between the scholarship and the list has "
              "been identified. The geographical reading does exist in the modern flat-earth "
              "literature in a form Eliade's work does not support: Eric Dubay's "
              "<em>Flatlantis</em> (2020) is published as an inquiry into &ldquo;Mount Meru, the "
              "alleged magnetic mountain ancient cultures worldwide believed existed at the "
              "North Pole&rdquo; — an assertion about a physical object at a physical place, "
              "which is precisely the step from symbol to geography this cluster turns on. "
              "Whether the specimen drew on that book is not established here and should not be "
              "asserted; it is recorded as a documented instance of the drift, not as a "
              "channel.</p>")),

    people=["PER-ELIADE"],
    related=["D01", "D02", "D05", "D06", "D07", "D08", "D16", "A22"],

    sources=[
        dict(label="Eliade, The Myth of the Eternal Return, ch. I — “The Symbolism of the "
                   "Center”; the schema and the Meru sentence (online transcription)",
             url="https://www.thetedkarchive.com/library/mircea-eliade-the-myth-of-the-eternal-return"),
        dict(label="Eliade, The Sacred and the Profane, ch. 1 — “the multiplicity … of centers "
                   "of the world raises no difficulty”; “not a matter of geometrical space”",
             url="https://hermetics.net/media-library/rosicrucianism/mircaeda-eliade-sacred-profane/01-chapter-01-sacred-space-making-world-sacred/"),
        dict(label="Jonathan Z. Smith, To Take Place: Toward Theory in Ritual (Chicago, 1987) — "
                   "publisher's record",
             url="https://press.uchicago.edu/ucp/books/book/chicago/T/bo5951548.html"),
        dict(label="Engstrom, critical analysis of Eliade (Univ. of Florida) — quotes Smith at "
                   "pp. 5, 8 and 10 on the Numbakulla hybrid and the Tjilpa myth",
             url="https://ufdcimages.uflib.ufl.edu/NC/F0/00/32/58/00001/Engstrom_J.pdf"),
        dict(label="“Eliade's Aboriginal cosmic axis” — the two incidents thirty pages apart; "
                   "Smith on the terrestrial and chthonic horizon and on “center” as political",
             url="https://dreamflesh.com/essay/eliade-aboriginal-cosmic-axis/"),
        dict(label="Guénon, The King of the World (Le Roi du Monde, 1927), ch. 2 — the pole "
                   "“known symbolically to all traditions”. Transcription ends in ch. 6; the "
                   "omphalos chapter was not reached",
             url="https://archive.org/stream/reneguenon/1927%20-%20The%20King%20of%20the%20World_djvu.txt"),
        dict(label="Pausanias, Description of Greece 10.16.3 — “said by the Delphians to be the "
                   "centre of all the earth”",
             url="https://dmdhist.sitehost.iu.edu/Pausaniasdelphi.htm"),
        dict(label="Omphalos — the Delphi stone and the two eagles of Zeus",
             url="https://en.wikipedia.org/wiki/Omphalos"),
        dict(label="Navel of the World — the documented claimants, thirteen sites across five continents",
             url="https://en.wikipedia.org/wiki/Navel_of_the_World_(disambiguation)"),
        dict(label="Sūrya Siddhānta — spherical Earth, ch. 12 cosmography, a polar star at the "
                   "zenith of each pole, Meru at the north pole",
             url="https://en.wikipedia.org/wiki/Surya_Siddhanta"),
        dict(label="Yggdrasil — Gylfaginning 15, the three roots and the three wells",
             url="https://en.wikipedia.org/wiki/Yggdrasil"),
        dict(label="Mappae mundi (Magdalen College, Oxford) — Jerusalem centred for theological "
                   "reasons; sphericity known from Aristotle; maps “primarily symbolic”",
             url="https://www.magd.ox.ac.uk/blog/mappae-mundi-medieval-world-maps/"),
        dict(label="Axis mundi — the comparative category and its range of examples",
             url="https://en.wikipedia.org/wiki/Axis_mundi"),
        dict(label="Eric Dubay, Flatlantis (2020) — the modern geographic reading: Meru as an "
                   "“alleged magnetic mountain … at the North Pole”",
             url="https://www.goodreads.com/en/book/show/54822633"),
        dict(label="The specimen list — withthesun33.com/about-1, retrieved 2026-08-09; items "
                   "160, 173, 174, 451, 453, 454 carry no author attribution",
             url="https://withthesun33.com/about-1"),
    ]),
}
