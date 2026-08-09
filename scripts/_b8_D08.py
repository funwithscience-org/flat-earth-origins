# -*- coding: utf-8 -*-
"""Batch 8 — D08, the architecture cluster of family D (Hall, 1928).

Sibling of _b6_D07.py and deliberately disjoint from it. D07 owns Hall's Qabbalah
chapter (the sephirothic Ptolemaic table), his Rosicrucian plates ("a Ptolemaic
chart", "the surface of the earth and sea", "the region of the central fire"), the
Masonic monitors, the Fama, the Gnostic hebdomad, the Mithraic tauroctony and
Blavatsky's Isis Unveiled ch. I. This entry owns Hall's ch. VI (the pyramid),
ch. IX (the zodiac, where the Dendera stone appears), ch. XI (Wonders of Antiquity,
the Ephesus line) and ch. XXIX (the Tabernacle, where the temple-as-universe
sentence and the Josephus key sit), plus the Dendera object itself, the 1820s
dating fight, and the Sacrobosco / Dante material behind item 127. Where the two
touch — the nested-spheres finding — this one cites D07 rather than re-arguing it.

Three things worth flagging forward to whoever takes D01, D04, D09, D16:

  * THE D07 TEST KEEPS WORKING. "Open the named originator's named book and read
    what it says about the shape of the earth" is now three for three in this lane
    (D06 Kybalion, D07 Isis Unveiled p. 9, D08 here). In Hall's own zodiac chapter
    the zodiac is a band "apparently encircling the earth" whose plane "intersects
    the celestial equator at an angle of approximately 23° 28'". Encircling, and a
    celestial equator. Run it first on every remaining D cluster.

  * THE ITEM-LEVEL ATTRIBUTION IS NOT UNIFORM AND I COULD NOT MAKE IT SO. Items
    74, 430, 440 and 456 have located homes in Hall's chapters (XXIX, XI, IX). Item
    126's vocabulary ("world-centers") is Mircea Eliade's, and PER-ELIADE /
    WRK-ELIADE-1949 already exist in our records; item 127 points at Latin-European
    material. Neither was located in the four Hall chapters I read. This is the R06
    failure mode — a cluster-level attribution applied to every item in the cluster
    — and the honest scope is "not located in the chapters read", not "not in the
    book". Recorded in the compression note as a scoped search result. NOT fixed
    here: clusters.py is another agent's file this pass. Reported to the parent.

  * THE OBJECT HAS BEEN RECRUITED TWICE, IN OPPOSITE DIRECTIONS. In the 1820s the
    Dendera ceiling was the exhibit for a world far older than Mosaic chronology;
    it is now an exhibit for a Mosaic cosmology. Champollion settled the first fight
    by reading the cartouche; Cauville and Aubourg settled the date by running the
    planets and two eclipses backwards. Both settlements are spherical-astronomy
    operations, which is the whole entry in one sentence.

Sources read at the transcription level, not from page images: Hall is quoted from
the sacred-texts.com transcription (sta09, sta12, sta14, sta32). The 1928 folio
pagination has not been checked against page images and no page numbers are
claimed. sacred-texts served sta09 only from the www host; the bare host returned
403 on that file.
"""

ENTRY = {

"D08": dict(

    verdict_challenge=dict(
        challenged=False, proposed_verdict=None,
        reasoning=("Considered UNFALSIFIABLE, which is the verdict its sibling D07 "
                   "carries, and rejected it here. The two "
                   "clusters are cut from the same book and the same method statement, so the "
                   "case is real: Hall's introduction says the doctrine is not upon the open "
                   "pages, and under that rule no surface reading of a ceiling can count "
                   "against an esoteric reading of it. But D08 differs in a way that decides "
                   "the verdict. Its central exhibit is not an interpretation, it is an object "
                   "with an inventory number, a quarry, a findspot, a datable planetary "
                   "configuration and two datable eclipses; and the proof set contains, "
                   "alongside it, an item asserting concentric heavens, which in the "
                   "Latin-European art it names are drawn about a globe, while the cosmos its "
                   "own temple items model is an inventory of seven planetary courses inside a "
                   "zodiac circle. The contradiction is therefore inside "
                   "the set rather than imposed on it: the same seven items ask a reader to "
                   "accept nested spheres and a flat earth under a dome at once. "
                   "SELF-CONTRADICTED describes that exactly, and it is the more modest "
                   "verdict, because it convicts the argument out of its own materials rather "
                   "than out of a general claim about esoteric method.")),

    tldr=("The Dendera ceiling is a real Egyptian relief and its astronomy is real — which is "
          "the problem. It is a planisphere, a flat projection of the sky, carved around 50 BCE "
          "in a Ptolemaic temple, using zodiac signs that reached Egypt from Mesopotamia through "
          "the Greek world, and what it maps is the sky: constellations, decans and planets, "
          "held up by four goddesses and four pairs of falcon-headed spirits. In the same book "
          "these items are drawn from, Manly P. Hall defines the zodiac as a band “apparently "
          "encircling the earth” whose plane “intersects the celestial equator at an angle of "
          "approximately 23° 28′”, and prints a description of the Dendera stone in which the "
          "constellations run in a spiral inside a square. Several of these buildings really were "
          "built as models of a cosmos, on the testimony of their own describers — and the cosmos "
          "they model is the seven planetary courses and the zodiac circle, which is a globe "
          "inside nested spheres."),

    passage=dict(
        work="WRK-HALL-1928", pd=True,
        locator=("ch. IX, “The Zodiac and Its Signs” (Dendera/Tentyra); with ch. XXIX, “The "
                 "Tabernacle in the Wilderness”, ch. XI, “Wonders of Antiquity”, and ch. VI, "
                 "“The Initiation of the Pyramid”. Read in the sacred-texts.com transcription "
                 "(sta12, sta32, sta14, sta09); 1928 folio pagination not checked against page "
                 "images, so no page numbers are claimed"),
        quote=("… a band of fixed stars about sixteen degrees wide, apparently encircling the "
               "earth.\n\n"
               "The plane of the zodiac intersects the celestial equator at an angle of "
               "approximately 23° 28′. The two points of intersection (A and B) are called the "
               "equinoxes.\n\n"
               "Each sign of the zodiac consists of thirty degrees, and as the sun loses about "
               "one degree every seventy-two years, it regresses through one entire "
               "constellation (or sign) in approximately 2,160 years, and through the entire "
               "zodiac in about 25,920 years. This retrograde motion is called the precession "
               "of the equinoxes.\n\n"
               "The oldest circular zodiac known is the one found at Tentyra, in Egypt, and now "
               "in the possession of the French government.\n\n"
               "[quoting John Cole] The diameter of the medallion in which the constellations "
               "are sculptured, is four feet nine inches, French measure. It is surrounded by "
               "another circle of much larger circumference, containing hieroglyphic characters; "
               "this second circle is enclosed in a square, whose sides are seven feet nine "
               "inches long. * * * The asterisms, constituting the Zodiacal constellations "
               "mixed with others, are represented in a spiral."),
        gloss=(
            "<p>This is the chapter the Dendera item comes from, and it is worth reading before "
            "anything is argued about it, because Hall does the list&rsquo;s work for it and "
            "then undoes it in the same paragraph.</p>"
            "<p><strong>Encircling, not doming.</strong> Hall&rsquo;s working definition of the "
            "zodiac in this chapter is a band of fixed stars about sixteen degrees wide "
            "<em>apparently encircling the earth</em>. A band that encircles a body goes all the "
            "way round it; a dome sits over one side of it. Those are different shapes, and the "
            "one in the chapter is not the one on the list.</p>"
            "<p><strong>A celestial equator, and equinoxes where two great circles cross.</strong> "
            "Hall then gives the geometry: the plane of the zodiac cuts the celestial equator at "
            "about 23&deg;&nbsp;28&prime;, and the two intersections are the equinoxes. The "
            "celestial equator is the projection of the earth&rsquo;s equator onto the sky; the "
            "zodiac band is the ecliptic; the angle between them is the obliquity; two great "
            "circles inclined to each other on a sphere cross in exactly two places, which is why "
            "there are two equinoxes and not one or three. None of those quantities is defined on "
            "a plane. Hall also supplies the precession numbers &mdash; one degree in about "
            "seventy-two years, 2,160 years to a sign, 25,920 years for the circuit &mdash; and "
            "precession is a slow wobble of that spherical frame, discovered by comparing star "
            "catalogues. <a href=\"#ARG-D07\">D07</a> uses the same obliquity figure for the "
            "Mithraic item; it is cited here for the different reason that it appears in the "
            "chapter where Dendera is presented.</p>"
            "<p><strong>And the description he prints of the stone itself has no dome in it.</strong> "
            "Hall introduces the Tentyra zodiac as the oldest circular zodiac known and hands the "
            "description to John Cole: a sculptured medallion four feet nine inches across, "
            "wrapped in a larger inscribed circle, set inside a square seven feet nine inches on "
            "a side, with the constellations laid out <em>in a spiral</em>. A spiral on a flat "
            "medallion in a square frame is a draughtsman&rsquo;s solution to fitting a sky onto "
            "a slab. It is the description of a map.</p>"
            "<p><strong>The architecture chapters say what the buildings model, and then say what "
            "the model contains.</strong> In <em>The Tabernacle in the Wilderness</em> Hall writes "
            "that &ldquo;[t]he temples of Egyptian mysticism (from which the Tabernacle was "
            "copied) were&mdash;according to their own priests&mdash;miniature representations of "
            "the universe&rdquo;, and in <em>Wonders of Antiquity</em> that the temple of Diana at "
            "Ephesus was &ldquo;designed as a miniature of the universe&rdquo;. Concede both "
            "without argument &mdash; they are the cluster&rsquo;s own thesis, stated by its own "
            "authority, and they are also the mainstream reading. Then read the inventory Hall "
            "gives of what is being modelled, quoting Josephus: the tabernacle&rsquo;s three parts "
            "denote &ldquo;the land and the sea &hellip; [and] the third division for God, because "
            "heaven is inaccessible to men&rdquo;; the seven lamps &ldquo;referred to the course "
            "of the planets, of which that is the number&rdquo;; the twelve stones are &ldquo;the "
            "like number of the signs of that circle which the Greeks call the Zodiac&rdquo;; the "
            "high priest&rsquo;s girdle &ldquo;signified the ocean, for that goes round about and "
            "includes the universe&rdquo;. Seven planetary courses and a zodiac circle the Greeks "
            "named is the Hellenistic nest of spheres, and Josephus says whose vocabulary it is in "
            "the sentence itself.</p>"
            "<p>One more, from the pyramid chapter, because item 163 leans on orientation. Hall "
            "records that &ldquo;[t]he sides of the Great Pyramid face the four cardinal "
            "angles&rdquo; and then glosses them, via Eliphas Levi, as &ldquo;the extremities of "
            "heat and cold (south and north) and the extremities of light and darkness (east and "
            "west)&rdquo;, calling the building &ldquo;the perfect emblem of the microcosm and the "
            "macrocosm&rdquo;. The gloss he chooses for the alignment is elemental and moral. It "
            "is not a survey result, and he does not offer it as one.</p>")),

    steelman=dict(
        description=(
            "<p><strong>SURFACE (weak &mdash; do not use).</strong> &ldquo;Buildings are not "
            "evidence; a temple ceiling is decoration.&rdquo; This is false and it will be "
            "corrected in public by the first Egyptologist who reads it. Sacred architecture is "
            "read as cosmology across the whole field &mdash; and note who is on that side of the "
            "argument here. It is not the list against the academy: the temple-as-microcosm "
            "reading is the academy&rsquo;s, and Hall is quoting Josephus, a first-century "
            "witness, not inventing a modern conceit.</p>"
            "<p><strong>DEEPER.</strong> &ldquo;Dendera is late &mdash; Ptolemaic, about 50 BCE "
            "&mdash; so it is not evidence about ancient Egypt.&rdquo; True, and incomplete, and "
            "it walks into the standing reply: a late monument can copy an old programme, and "
            "Egyptian temple decoration is famously conservative. That reply is not silly. It is "
            "the same move Dupuis made in the 1790s, and answering the date alone leaves it "
            "standing.</p>"
            "<p><strong>KERNEL.</strong> Name the specific true thing, and it is large and it is "
            "conceded in full: <em>the native Egyptian picture of the world really is a sky "
            "stretched over a flat earth, and the Dendera temple is an Egyptian temple.</em> Nut "
            "is the sky and Geb is the earth; she is &ldquo;pictured as a woman arched on her toes "
            "and fingertips over the Earth; her body portrayed as a star-filled sky&rdquo;, and "
            "she is &ldquo;sometimes depicted in the form of a cow whose great body formed the sky "
            "and heavens&rdquo;. No globe appears in that image, and it is not read as one in the "
            "reference accounts we consulted. So an item that says Egyptian sacred architecture encodes a covering sky over "
            "a flat earth is, <em>for the native tradition</em>, telling the truth &mdash; and it "
            "is telling a truth the field publishes in its own textbooks. Any rebuttal that "
            "pretends otherwise is beaten before it starts.</p>"),
        why_it_doesnt_save_claim=(
            "<p><strong>Because the one ceiling on that roof the list picked is the one piece of "
            "it that is not native.</strong> The zodiac &ldquo;was imported during Ptolemaic or "
            "Roman Period to Egypt&rdquo; (UCL, <em>Digital Egypt</em>); on the Dendera stone "
            "several signs appear &ldquo;in the same Greco-Roman iconographic forms as their "
            "familiar counterparts (e.g. the Ram, Taurus, Scorpio, and Capricorn)&rdquo;, while "
            "others are Egyptianised &mdash; Aquarius is Hapi with his two vases. The object is a "
            "hybrid, and the half the list needs to be primordial is the half that arrived from "
            "Mesopotamia by way of the Greek world. The conservatism reply is answered by the same "
            "fact rather than by the date: nobody has to deny that Ptolemaic temples reproduce "
            "older programmes, because the zodiac is precisely the element the Egyptological "
            "literature does <em>not</em> assign to the older programme.</p>"
            "<p><strong>And the native picture, taken as the list needs to take it, proves too "
            "much.</strong> If Nut arched over Geb is a report about the world&rsquo;s shape, then "
            "so is Nut as a cow, and so is the sky held up at four points by falcon-headed "
            "spirits. A tradition that renders the sky as a woman, a cow and a disc on eight "
            "shoulders is not filing survey returns; it is doing what iconography does. The list "
            "wants to read one of those images literally and the others figuratively, and it has "
            "supplied no rule for choosing.</p>"
            "<p><strong>Then there is what the list actually wants, which the kernel cannot "
            "deliver.</strong> The argument needs testimony that is at once authoritative, "
            "ancient and suppressed. The Nut cosmology is ancient and entirely unsuppressed &mdash; "
            "it is in every introductory book on Egyptian religion &mdash; and it is not "
            "testimony, because the people who held it had not measured the thing they were "
            "picturing. The Dendera zodiac is a measurement, precise enough to be dated to a "
            "particular year from the planets it shows plus a lunar eclipse of 25 September 52 BCE "
            "and a solar eclipse of 7 March 51 BCE &mdash; and it is neither native nor early. You "
            "may have the authority or the antiquity. Not both, and not from the same ceiling.</p>"
            "<p>The kernel also reaches only two of the seven items, and the second of those it "
            "reaches to no effect: 456, the Dendera item, and 440, whose <em>revolving</em> "
            "heavens a firmament turning over a plane supplies as readily as a turning sphere, so "
            "that item settles nothing about shape in either direction. It does nothing for 127, "
            "whose concentric heavens are Latin-European and drawn around a sphere; nothing for "
            "74 and 430, where the model&rsquo;s own inventory is seven planets and a zodiac "
            "circle; nothing for 126, whose world-centre vocabulary is Eliade&rsquo;s and is "
            "treated at <a href=\"#ARG-D04\">D04</a>; and nothing for 163, where orientation is "
            "compatible with any ground whatever.</p>")),

    refutation=(
        "<p><strong>1. What the object is.</strong> The Dendera zodiac is a sandstone bas-relief "
        "from the ceiling of the pronaos of a chapel dedicated to Osiris, on the roof of the "
        "temple of Hathor at Dendera. The existing temple was begun in 54 BCE under Ptolemy XII; "
        "the relief is dated to about 50 BCE; the hypostyle hall was added under Tiberius. It is "
        "in the Louvre, catalogued D 38 / E 13482 / CM 464, and what is on the ceiling at Dendera "
        "today is a copy &mdash; the original was cut out in 1820&ndash;21 by Jean Lelorrain, who "
        "used explosives to unseat it, reached Paris in the summer of 1822, and was bought by "
        "Louis XVIII for 150,000 francs. Its form is &ldquo;a planisphere or map of the stars on a "
        "plane projection&rdquo;, showing the zodiacal constellations and the decans; &ldquo;[f]our "
        "women and four pairs of falcon-headed figures, arranged 45&deg; from one another, hold up "
        "the sky disc.&rdquo; None of that is contested in the sources we consulted, on either "
        "side of the argument.</p>"

        "<p><strong>2. It is a map of the sky, and a dome over the earth is a reading laid on top "
        "of it.</strong> The relief is round, and it was fixed above a viewer&rsquo;s head, so a "
        "person standing under it stood under a disc. That is a fact about ceilings. What is "
        "carved on it is the contents of the sky &mdash; constellations, decans, planets in their "
        "positions &mdash; and in the descriptions we consulted (the Louvre&rsquo;s catalogue "
        "numbers and object description, the standard encyclopaedia account, and John Cole&rsquo;s "
        "inventory as Hall prints it) the earth is not among the things identified on the stone. "
        "We did not read Cauville&rsquo;s 1997 monograph on the ceiling, which is the specialist "
        "publication and would settle the identification of every figure; that is stated as a gap, "
        "not as a result. The four goddesses and four falcon-headed pairs are sky-supports, which "
        "is a native motif &mdash; and note what they are supporting. Not a firmament above a "
        "world. A <em>disc of stars</em>, which is to say the map itself. The list has read the "
        "physical slab as though it were the thing depicted, which is the error of taking a "
        "photograph of the sky for the sky.</p>"

        "<p><strong>3. The astronomy on it is the astronomy of a sphere, and that is how its age "
        "was settled.</strong> A planisphere is a projection: a spherical sky flattened onto a "
        "plane by a stated rule, the way a world map flattens a globe. The word is a modern "
        "description of the object&rsquo;s geometry and no ancient label on the stone says it "
        "&mdash; the concession costs nothing, because the geometry is visible whether or not it "
        "was named. Sylvie Cauville and &Eacute;ric Aubourg dated the relief to 50 BCE from the "
        "configuration of the planets it depicts, together with two eclipses it records: a lunar "
        "eclipse on 25 September 52 BCE, shown as an Eye of Horus locked in a circle, and a solar "
        "eclipse on 7 March 51 BCE, shown as Isis holding a baboon by the tail. Read that "
        "procedure slowly. The stone was dated by running the solar system backwards two thousand "
        "years and finding that the sky it shows occurred. Eclipse prediction and retrodiction are "
        "the oldest working products of spherical astronomy; you cannot compute the circumstances "
        "of a solar eclipse without the geometry of a lit sphere, an orbiting moon and a place on "
        "the surface. The exhibit is dated by the model it is offered against.</p>"

        "<p><strong>4. The dating fight is the claim&rsquo;s own ancestor, and it was lost on the "
        "evidence.</strong> This is not a new argument, and the movement is on the second lap of "
        "it. When the ceiling reached Paris it was the centrepiece of a dispute about the age of "
        "the world: various astronomical and mathematical methods were canvassed for dating it, "
        "with extreme antiquity urged, and the matter was settled when Jean-Fran&ccedil;ois "
        "Champollion identified the Greek title <em>autokrator</em> in a cartouche and placed the "
        "ceiling in the period of Greco-Roman domination &mdash; so the ceiling &ldquo;was not "
        "especially old, and its existence posed no problems for Mosaic chronology.&rdquo; The "
        "same object has now been recruited by an argument pointing the other way, as evidence for "
        "an ancient cosmology of a covered flat earth. It cannot serve both, and it was retired "
        "from the first by the two methods that also retire it from the second: reading what is "
        "written on it, and computing the sky it shows.</p>"

        "<p><strong>5. Temple as cosmic model &mdash; conceded, and then read.</strong> Items 74, "
        "430 and 440 assert that temples were built as models of the cosmos. Grant it "
        "entirely; the sources say so themselves, and Hall quotes them saying so. (Item 126, "
        "&ldquo;Temples as world-centers&rdquo;, is a different claim in a different vocabulary "
        "&mdash; Eliade&rsquo;s centre-of-the-world language, which this page treats at "
        "<a href=\"#ARG-D04\">D04</a> &mdash; and it was not located in the Hall chapters read "
        "for this entry.) The question the "
        "list never asks is <em>which cosmos</em>. Josephus&rsquo;s key, as Hall prints it, is: "
        "three parts for land, sea and heaven; seven lamps for &ldquo;the course of the planets, "
        "of which that is the number&rdquo;; twelve stones for &ldquo;the signs of that circle "
        "which the Greeks call the Zodiac&rdquo;; four colours in the veil for the four elements. "
        "Seven planetary courses, a zodiac circle, four elements &mdash; that is the Hellenistic "
        "geocentric cosmos, whose central earth is a globe by construction and whose outermost "
        "shell carries the fixed stars. <a href=\"#ARG-D07\">D07</a> reached the identical result "
        "from the Gnostic hebdomad and from Hall&rsquo;s own sephirothic table, and from a "
        "Rosicrucian plate Hall captions &ldquo;a Ptolemaic chart&rdquo; and walks inward past "
        "&ldquo;the surface of the earth and sea&rdquo; to &ldquo;the region of the central "
        "fire&rdquo; &mdash; a body with a surface and an interior. That work is not repeated "
        "here; it is cited, because two chapters of one book reaching the same nested-sphere "
        "cosmos independently is the finding.</p>"

        "<p><strong>6. Item 127: the concentric heavens of medieval art are drawn around a "
        "ball.</strong> The diagrams the item points at belong to the tradition of Johannes de "
        "Sacrobosco&rsquo;s <em>Tractatus de sphaera</em>, written about 1230, copied in hundreds "
        "of manuscripts, first printed at Ferrara in 1472 and issued in at least eighty-four "
        "editions in the two centuries after &mdash; the standard university astronomy text of "
        "Latin Europe, and the source of the picture everyone recognises. Its title is <em>the "
        "sphere</em>. Its first chapter argues that the earth is one, from observations: stars "
        "rise and set earlier for those further east, a lunar eclipse is timed differently at "
        "different longitudes, more northern stars come into view as you travel north, more sea is "
        "visible from the masthead than from the deck, and water takes a round shape of itself. "
        "The concentric heavens in the illuminations are concentric <em>about that sphere</em>. "
        "The literary monument of the same scheme makes it unmissable: in the last canto of "
        "Dante&rsquo;s <em>Inferno</em>, the two poets climb down Satan&rsquo;s flank, pass through "
        "the centre of gravity, and continue &lsquo;upward&rsquo; to the surface at the antipodes, "
        "emerging in the Southern Hemisphere at the mountain of Purgatory. A cosmology whose plot "
        "requires walking through the earth and coming out the other side is not testimony for a "
        "flat one.</p>"

        "<p><strong>7. Item 440, and what revolving heavens do not settle.</strong> &ldquo;Temple "
        "architecture mirroring revolving heavens&rdquo; names the daily turning of the sky "
        "&mdash; the motion that makes stars circle the pole, that fixes what &lsquo;true "
        "north&rsquo; means, and that a temple axis can be aligned to. It is a real phenomenon "
        "and it is what the builders watched. On its own it does not decide the shape question, "
        "and we are not going to pretend it does: a firmament turning over a plane also carries "
        "stars round a pole, and the list says so itself &mdash; &ldquo;Precession from dome "
        "rotation&rdquo; and &ldquo;Day&ndash;night cycle from firmament rotation&rdquo; are "
        "items in this same corpus. What decides it is that the turn has two centres, one in "
        "each hemisphere, which no single axis through a disc delivers; that is argued at "
        "<a href=\"#ARG-B08\">B08</a> and not re-run here. What item 440 concedes is that the "
        "heavens revolve, which is a claim about motion; whether the sky or the observer turns "
        "is the geocentric question, belonging to lane A and to <a href=\"#ARG-D02\">D02</a>, "
        "not to this family.</p>"

        "<p><strong>8. Item 163, honestly: orientation is nearly content-free here.</strong> "
        "Aligning a building to the cardinal points, to a solstice sunrise, or to a star&rsquo;s "
        "rising tells you the builders watched the sky with care and could transfer a sightline to "
        "the ground. It does not tell you what they believed the ground&rsquo;s shape was, because "
        "the same sightlines are available under either model. We are not going to pretend "
        "otherwise in order to win an item. What the item does establish is the opposite of what "
        "it is filed for: it concedes that these builders were competent observational "
        "astronomers, and competent observational astronomy in the Mediterranean world of the "
        "Ptolemaic temples had already produced a measured spherical earth &mdash; the "
        "Eratosthenes strand, which is scored at <a href=\"#ARG-D06\">D06</a> rather than "
        "re-argued here. Hall&rsquo;s own gloss on the pyramid&rsquo;s cardinal faces, borrowed "
        "from Eliphas Levi, is heat and cold, light and darkness. Elemental, not geodetic.</p>"

        "<p><strong>9. What the cluster would need, and what it has.</strong> Architecture becomes "
        "evidence about the shape of the earth when it records a measurement of the earth. The "
        "Dendera ceiling does record measurements &mdash; of planets, on a date, with two eclipses "
        "&mdash; and those measurements are the ones that come out spherical. Everything else in "
        "the cluster is a claim about what a building meant to the people who built it, which is a "
        "real and answerable question, and one whose answer here is the nested spheres. A proof "
        "set that contains &lsquo;concentric heavens&rsquo; drawn about a globe and &lsquo;a dome "
        "above a flat earth&rsquo;, and whose own temple items model a cosmos of seven planetary "
        "courses inside a zodiac circle, is not being merely wrong; it is holding two "
        "geometries at once and drawing on whichever is convenient. That is the verdict.</p>"),

    advocate=dict(
        best_defense=(
            "You have conceded the load-bearing point and then walked past it. The Egyptians' own "
            "cosmology is a sky stretched over a flat earth — you say so yourself, in your "
            "steelman, citing the standard reference — and Dendera is an Egyptian temple built by "
            "Egyptian priests for Egyptian rites. The Greek signs are a veneer on a native "
            "ceiling: the sky-supports are Egyptian, the decans are Egyptian, Aquarius is Hapi "
            "with his vases. 'Planisphere' is your word, not theirs; nothing on the stone says "
            "'projection', and calling a round carving a projection because it is round is the "
            "same inference you accuse us of making about domes. Dating the slab dates the slab: "
            "Egyptian temple programmes are conservative by design, and a Ptolemaic mason copying "
            "an older ceiling gives you a Ptolemaic date for an older idea. Worst of all, your "
            "star witness against us is Manly Hall's editorial prose. Hall writes in 1928, in the "
            "ordinary astronomical vocabulary of 1928, when he introduces a subject to his "
            "readers; that vocabulary is his, not the tradition's. Quoting his framing sentence "
            "as though it were the ancient testimony is compression — exactly the offence your "
            "own hedge rule exists to catch — and you have committed it while accusing us of it."),
        survives=4,
        preemptive=(
            "This defence is strong and three of its four moves are answered in the body above "
            "rather than left to the reader; the fourth is the one to watch. (a) The conservatism "
            "move is answered in why_it_doesnt_save_claim, and the answer deliberately does NOT "
            "rest on the date: it concedes that Ptolemaic temples reproduce older programmes and "
            "then observes that the zodiac is the specific element the Egyptological literature "
            "does not assign to the older programme, citing UCL's Digital Egypt — 'the zodiac was "
            "imported during Ptolemaic or Roman Period to Egypt'. (b) The 'planisphere is your "
            "word' move is conceded in §3 in a sentence written for this purpose: the term is a "
            "modern description of the object's geometry, no ancient label on the stone says it, "
            "and the concession costs nothing because the geometry is visible whether or not it "
            "was named. (c) The 'read a ceiling as a dome' symmetry is answered in §2, which "
            "grants that the slab is round and overhead and then distinguishes the slab from what "
            "is carved on it. (d) The one that must not be fudged is the Hall-in-1928 charge, and "
            "it is half right. Hall's phrases 'celestial equator' and '23° 28′' ARE his own "
            "vocabulary and are not ancient testimony, and this entry must never claim they are. "
            "The claim made in the gloss is narrower and survives: the list offers HALL's chapters "
            "as its source, so what Hall's chapters say about the shape of the thing is a fact "
            "about the proof set, not about ancient Egypt. That is why the verdict is "
            "SELF-CONTRADICTED and not FALSE — the contradiction is between the list and its own "
            "cited authority. Keep the gloss's framing sentence ('Hall does the list's work for it "
            "and then undoes it in the same paragraph') and never upgrade it to a claim about "
            "Egyptian belief. The independent, non-Hall legs — the import date, the eclipse "
            "dating, Sacrobosco, Dante — are what carry the argument if a defender refuses Hall "
            "entirely, and they are placed in separate numbered sections so they can be read "
            "without him.")),

    straw_man=dict(
        identified=True,
        detail=("Two, and the first is ours to avoid. Do not answer this cluster with 'it is only "
                "symbolic'. The temple-as-microcosm reading is not a concession wrung out of "
                "scholarship, it IS scholarship, and Hall reaches it by quoting Josephus rather "
                "than by asserting it; anyone who says these buildings were not built as cosmic "
                "models will be corrected from the standard literature. Theirs is the framing that "
                "puts the academy on the other side of the temple question, when the academy is "
                "the source of the reading. Separately, and noted at D07 as a cross-cluster "
                "problem rather than a straw man: this list offers esoteric architecture as "
                "testimony FOR a fixed flat earth at D07 and D08, while D10 offers the same "
                "traditions as the occult SOURCE of heliocentrism. Both cannot be evidence.")),

    compression=dict(
        assessed=True, drifted=True,
        list_phrasing="Dendera zodiac as dome above Earth.",
        source_wording=("&ldquo;&hellip; a band of fixed stars about sixteen degrees wide, "
                        "<em>apparently encircling the earth</em>.&rdquo; &mdash; and, of the "
                        "object: &ldquo;The oldest circular zodiac known is the one found at "
                        "Tentyra&rdquo;, described via John Cole as a sculptured medallion "
                        "&ldquo;four feet nine inches&rdquo; across, inside a larger inscribed "
                        "circle, inside &ldquo;a square, whose sides are seven feet nine inches "
                        "long&rdquo;, with the constellations &ldquo;represented in a spiral&rdquo;."),
        drift_type="unsourced_addition",
        note=("<p>The comparison was run against the two chapters that carry this cluster&rsquo;s "
              "material: Hall&rsquo;s ch. IX, <em>The Zodiac and Its Signs</em>, which is where "
              "the Dendera (Tentyra) stone appears, and ch. XXIX, <em>The Tabernacle in the "
              "Wilderness</em>, which is where the temple-as-universe sentence sits; with ch. XI "
              "and ch. VI read for the Ephesus and pyramid items. All four were read in the "
              "sacred-texts.com transcription (sta12, sta32, sta14, sta09). The 1928 folio was not "
              "consulted and no page numbers are claimed.</p>"
              "<p><strong>The dome is the list&rsquo;s.</strong> In the chapter searched, the "
              "zodiac is a band <em>encircling</em> the earth, its plane crosses the celestial "
              "equator at 23&deg;&nbsp;28&prime;, and the stone itself is described &mdash; in the "
              "words Hall chose to print &mdash; as a flat medallion in a square with the "
              "constellations running in a spiral. A dome above the Earth is not located in the "
              "text of that chapter as transcribed at sta12, which is the text we searched; a "
              "reader with the folio may find otherwise and we would want to know. Encircling and "
              "doming are different geometries, and only one of them is in the source. This is the "
              "<em>unsourced_addition</em> pattern: the item&rsquo;s content word is not the "
              "source&rsquo;s.</p>"
              "<p><strong>And the second clause of the hedge rule applies, so the refutation "
              "answers both.</strong> The dome reading is what circulates &mdash; the Dendera image "
              "travels widely with a firmament caption attached &mdash; and beating only the "
              "source&rsquo;s version would leave the version readers actually meet untouched. So "
              "&sect;2 and &sect;3 above answer the dome reading on the object&rsquo;s own merits "
              "(what is carved on the slab, and how the slab was dated), while &sect;5 answers "
              "Hall&rsquo;s version, which is the nested-sphere cosmos of Josephus&rsquo;s "
              "key.</p>"
              "<p><strong>Coverage, stated as a scope and not as a verdict.</strong> Items 74, "
              "430, 440 and 456 were located in the Hall chapters read, and 163 has its nearest "
              "home in the pyramid chapter&rsquo;s cardinal-faces passage. Items 126 (&ldquo;Temples "
              "as world-centers&rdquo;) and 127 (&ldquo;Medieval art concentric heavens&rdquo;) "
              "were not located in those four chapters. The vocabulary of 126 is Mircea "
              "Eliade&rsquo;s centre-of-the-world language, which this page treats at "
              "<a href=\"#ARG-D04\">D04</a>; 127 points at Latin-European material of the "
              "Sacrobosco and Dante tradition, handled at &sect;6 above. Neither observation is a "
              "claim about what Hall&rsquo;s book contains &mdash; forty-one other chapters were "
              "not read &mdash; only a record of where the search reached.</p>")),

    people=["PER-HALL", "PER-ELIADE", "PER-PTOLEMY"],
    related=["D07", "D06", "D04", "D02", "D01", "D09", "D16", "A22", "B08"],

    sources=[
        dict(label="Hall, The Secret Teachings of All Ages (1928), ch. IX “The Zodiac and Its "
                   "Signs” — the band “apparently encircling the earth”, the celestial equator at "
                   "23° 28′, the Tentyra zodiac and John Cole's description",
             url="https://sacred-texts.com/eso/sta/sta12.htm"),
        dict(label="Hall, ch. XXIX “The Tabernacle in the Wilderness” — Egyptian temples as "
                   "“miniature representations of the universe”; the Josephus key (land and sea, "
                   "seven lamps for the planets, twelve stones for the Greeks' Zodiac circle)",
             url="https://sacred-texts.com/eso/sta/sta32.htm"),
        dict(label="Hall, ch. XI “Wonders of Antiquity” — the temple of Diana at Ephesus "
                   "“designed as a miniature of the universe”",
             url="https://sacred-texts.com/eso/sta/sta14.htm"),
        dict(label="Hall, ch. VI “The Initiation of the Pyramid” — the four cardinal angles, "
                   "Eliphas Levi's elemental gloss, “the perfect emblem of the microcosm and the "
                   "macrocosm” (served only from the www host; the bare host returned 403)",
             url="https://www.sacred-texts.com/eso/sta/sta09.htm"),
        dict(label="Dendera zodiac — planisphere on a plane projection; the Osiris-chapel pronaos "
                   "ceiling; Cauville and Aubourg's 50 BCE dating from the planetary "
                   "configuration; the 52 and 51 BCE eclipses; the four women and four "
                   "falcon-headed pairs at 45°; Greco-Roman sign forms and Hapi as Aquarius",
             url="https://en.wikipedia.org/wiki/Dendera_zodiac"),
        dict(label="Dendera Zodiac — Louvre inventory D 38 / E 13482 / CM 464; sandstone "
                   "bas-relief; late Ptolemaic, c. 50 BCE; pronaos built under Tiberius",
             url="https://egypt-museum.com/the-dendera-zodiac/"),
        dict(label="Dendera Temple complex — Hathor temple begun 54 BCE under Ptolemy XII; "
                   "hypostyle hall under Tiberius; the ceiling relief removed in 1820 and "
                   "replaced with a copy",
             url="https://en.wikipedia.org/wiki/Dendera_Temple_complex"),
        dict(label="UCL, Digital Egypt — “The zodiac was imported during Ptolemaic or Roman "
                   "Period to Egypt”",
             url="https://www.ucl.ac.uk/museums-static/digitalegypt/astro/zodiac.html"),
        dict(label="The Zodiac at Dendera and the debate over the age of the earth (Victorian Web) "
                   "— Lelorrain's 1821 extraction with explosives, Paris 1822, 150,000 francs; "
                   "Champollion's reading of autokrator and the Greco-Roman dating",
             url="https://victorianweb.org/science/denderazodiac.html"),
        dict(label="Nut (goddess) — the sky arched over the Earth, her body a star-filled sky, "
                   "sometimes a cow; Geb as the Earth",
             url="https://en.wikipedia.org/wiki/Nut_(goddess)"),
        dict(label="Sacrobosco, De sphaera mundi (c. 1230) — the standard university text; "
                   "hundreds of manuscripts, printed 1472, at least 84 editions in two centuries; "
                   "chapter one's observational arguments for a spherical earth",
             url="https://en.wikipedia.org/wiki/De_sphaera_mundi"),
        dict(label="Dante, Inferno canto XXXIV — passing the centre of gravity and climbing to the "
                   "antipodal surface, emerging in the Southern Hemisphere at Mount Purgatory",
             url="https://en.wikipedia.org/wiki/Inferno_(Dante)")]),
}
