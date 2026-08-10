# -*- coding: utf-8 -*-
"""Batch 9 — D01. "All ancient cultures were geocentric."
4 items (21, 25, 119, 367), lane D, cluster verdict NOT DEMONSTRATED,
originator recorded as Robert Sungenis, Galileo Was Wrong Vol. II, 2006.

Research notes for whoever picks this up next.

1. THE HEADLINE: THE SOURCE STATES THE OPPOSITE, IN A SENTENCE, ON ITS OWN PAGE 62.
   This is the A05 shape a second time — the work our record credits as the origin
   carries the counter-evidence in its own text. Volume I of Galileo Was Wrong opens
   its historical survey by saying the question has "divided right down the middle"
   a debate "that stretches as far back as written records take us", and then names
   a roster of ancient heliocentrists: "Plato, Philolaus, Pliny, Aristarchus, and
   Seleucus versus the geocentric school of Aristotle, Hipparchus, Theon of Smyrna,
   Appolonius and Ptolemy", plus "the Indian astronomer Aryabhata". Footnote 133 on
   the same spread adds "Hiketas (450) Heraklides (350) and Ekphantus (450) held that
   the Earth rotates in a non-moving heavens." Appendix 9, footnote 1565, quotes
   Dreyer's translation of Archimedes on Aristarchus at length. Four list items assert
   a universal that their own cited authority spends pages denying. drift_type is
   `reversed`, and this is the cleanest instance of it on the board.

2. BE FAIR ABOUT THE ROSTER — IT IS LOOSE, AND SAYING SO PROTECTS US. Plato's Timaeus
   puts the Earth at the centre; Pliny is a geocentrist; the "Babylonians ... the sun
   occupied the center of the universe" claim rests on footnote 132's inference from
   a sun god, which does not follow; and Aryabhata argued for the Earth's ROTATION,
   not for a Sun-centred system. But the roster is not invented. Aristotle himself,
   De caelo II.13, reports the disputed reading of the Timaeus — "Others, again, say
   that the earth, which lies at the centre, is 'rolled', and thus in motion, about
   the axis of the whole heaven. So it stands written in the Timaeus." Strike the
   loose names and Philolaus, Aristarchus, Seleucus, Hicetas, Heraclides and Ecphantus
   are still standing, and three items assert a universal quantifier. Do NOT publish
   the source's roster unaudited; a defender who checks Pliny will use it on us.

3. THE INTERNAL COLLISION WITH D02. The list's item 120 is "Plato's Timaeus central
   Earth", cited as a geocentric authority. The source's p. 62 files Plato among the
   heliocentrists. Both cannot be right. D02 owns Plato and the four named authorities;
   this entry points at the collision and does not re-argue the Timaeus.

4. WHERE THE APPEAL TO ANTIQUITY ACTUALLY LIVES IN THE BOOK, AND ITS FORM. The only
   appeal-to-antiquity located in the two scans searched is at Vol. I p. 130, and it
   is a quotation from Wolfgang Smith's The Wisdom of Ancient Cosmology (2003),
   pp. 180-181 — geocentrism is "not only an ancient, but indeed a traditional
   doctrine; should we not presume that as such it enshrines a perennial truth?" A
   rhetorical question offered as grounds to REOPEN the file, followed immediately by
   "It will not be without interest, therefore, to investigate whether the geocentrist
   claim ... had indeed been ruled out of court." That is a presumption, explicitly
   not a proof. The list converts it into a flat historical universal.

5. ITEM 367 IS A DIFFERENT ARGUMENT WEARING THE CLUSTER'S NAME. "Ancient stone
   calendars geocentric" is archaeoastronomy, not doxography. "Stonehenge",
   "megalith", "Newgrange" and "Nabta" are not located in either the Volume I scan
   (archive.org item GallileoWasWrong) or the Volume II scan (item ...Bennett4276)
   that were searched; the route is named in the gloss. It is answered here on the
   merits anyway, because it is on the list. Flagged upward as a possible cluster
   boundary problem — its neighbours 363-366 are D19.

6. WORK RECORD. clusters.py was NOT touched. The originator_work/year pair says
   "Galileo Was Wrong, Vol. II" / "2006", i.e. the historical volume of the
   two-volume 2005-2010 set; no scan of that volume was reachable this pass, and the
   passage that actually addresses ancient cosmology is in Volume I, p. 62. Reported
   up rather than written around. C07 has already been moved to "Vol. III
   (three-volume edition) 2013"; D01, D02 and D03 still carry the old pair.

7. QUOTE PROVENANCE. Every quotation from Galileo Was Wrong below was taken from the
   plain-text OCR of Internet Archive item GallileoWasWrong (file "Gallileo was
   wrong_djvu.txt"), downloaded whole and searched locally rather than through a
   truncating fetch, so the searches in this entry cover the entire file. Printed
   pages were located from the running heads ("62 Chapter 1 Galileo Was Wrong").
   OCR spellings are preserved verbatim, including "Appolonius" and "Hiketas".
   Nothing was checked against a print copy and the locator says so.

Living-person constraint honoured: Sungenis is treated as an author of arguments only.
No motive, finances or good faith. The page adjudicates no religious claim.
"""

ENTRY = {

"D01": dict(

    tldr=("Antiquity was not unanimous, and the book our record credits for this says so: "
          "Volume I of Galileo Was Wrong describes “a debate that stretches as far back as "
          "written records take us” and files Philolaus, Aristarchus and Seleucus on the other "
          "side of it. Take the weaker version that is true — geocentrism was the ancient "
          "default — and it still does no work, because a consensus produced by an appearance "
          "everyone shares is one observation repeated, not many witnesses agreeing. And the "
          "ancient authorities the list names elsewhere for geocentrism — Aristotle and Ptolemy "
          "among them — held the Earth to be a globe."),

    passage=dict(
        work="WRK-SUNGENIS-2006",
        pd=False,
        locator=("Volume I, The Scientific Evidence (Catholic Apologetics International "
                 "Publishing, ISBN 0-9779640-0-0), chapter 1, printed p. 62, with footnote 133 "
                 "running to p. 63; from the plain-text OCR of Internet Archive item "
                 "GallileoWasWrong, downloaded whole and searched locally, with the printed "
                 "page located from the running head “62 Chapter 1 Galileo Was Wrong”. Not "
                 "checked against a print copy. Our cluster record names Volume II (2006), the "
                 "historical volume of the two-volume set; no scan of that volume was reachable "
                 "this pass."),
        quote=("[History] has been divided right down the middle … by the on-going debate as to "
               "what revolves around what; a debate that stretches as far back as written "
               "records take us. … it was the Pythagorean school of heliocentrists: Plato, "
               "Philolaus, Pliny, Aristarchus, and Seleucus versus the geocentric school of "
               "Aristotle, Hipparchus, Theon of Smyrna, Appolonius and Ptolemy."),
        gloss="""<p><strong>Read the first clause before the roster.</strong> The source&rsquo;s account of ancient cosmology is not &ldquo;everyone agreed&rdquo;; it is a <em>controversy</em>, running as far back as there are written records, with two named sides. Four items on this list assert the exact negation of that sentence. This is not a case where the source hedged and the list firmed the hedge up. The source took a position and the list took the opposite one, while citing the source.</p>

<p><strong>1. The footnote goes further than the paragraph.</strong> Footnote 133, attached to the roster and running onto p.&nbsp;63, surveys the pre-Socratics and closes: &ldquo;whereas Hiketas (450) Heraklides (350) and Ekphantus (450) held that the Earth rotates in a non-moving heavens.&rdquo; (The OCR spellings are the book&rsquo;s.) It cites Dreyer, Pederson and Duhem for it. So the work names three more ancients who denied a motionless Earth, in a footnote written to support the paragraph the list reverses. Further in, Appendix&nbsp;9 &mdash; footnote 1565, at scan pp.&nbsp;1041&ndash;42 &mdash; quotes Dreyer&rsquo;s translation of Archimedes at length: Aristarchus &ldquo;supposes that the fixed stars and the sun are immovable, but that the earth is carried round the sun in a circle.&rdquo; The book is not merely aware of ancient heliocentrism; it reproduces the primary attestation of it.</p>

<p><strong>2. The roster is loose, and we say so before a defender does.</strong> Three of the five names on the heliocentric side will not bear weight. Plato&rsquo;s <em>Timaeus</em> places the Earth at the centre. Pliny&rsquo;s <em>Natural History</em> is geocentric. And the Babylonian claim rests on footnote 132&rsquo;s reasoning that they &ldquo;believed that the sun god controlled the world, and naturally the sun occupied the center of the universe&rdquo; &mdash; which does not follow. A fourth, Aryabhata, argued for the Earth&rsquo;s <em>rotation</em> rather than for a Sun-centred system. But the roster is not invented out of nothing: Aristotle himself, <em>De caelo</em> II.13, records the disputed reading &mdash; &ldquo;Others, again, say that the earth, which lies at the centre, is &lsquo;rolled&rsquo;, and thus in motion, about the axis of the whole heaven. So it stands written in the Timaeus&rdquo; &mdash; and Plutarch preserves Theophrastus&rsquo;s report that Plato late in life regretted giving the Earth the middle place. Strike the three that fail and Philolaus, Aristarchus and Seleucus remain, with Hicetas, Heraclides and Ecphantus behind them in the footnote. Six ancients are six too many for the word <em>uniformly</em>.</p>

<p><strong>3. It collides with the list&rsquo;s own item 120.</strong> Item 120 is &ldquo;Plato&rsquo;s Timaeus central Earth&rdquo;, offered as a geocentric authority; p.&nbsp;62 of the source files Plato among the heliocentrists. One of the two is wrong, and the list runs both. Plato and the other named authorities belong to <a href="#ARG-D02">ARG-D02</a>, which reads them in their own texts; nothing about the <em>Timaeus</em> is re-argued here.</p>

<p><strong>4. Where the appeal to antiquity actually lives in this book, and what shape it has.</strong> The one appeal-to-antiquity located in the two scans searched is at Vol.&nbsp;I p.&nbsp;130, and it is a quotation from another author &mdash; Wolfgang Smith, <em>The Wisdom of Ancient Cosmology</em> (2003), pp.&nbsp;180&ndash;181, cited in the book&rsquo;s footnote 294. Smith writes that geocentrist cosmology is &ldquo;not only an ancient, but indeed a traditional doctrine; should we not presume that as such it enshrines a perennial truth?&rdquo; &mdash; and then, in the next breath, &ldquo;It will not be without interest, therefore, to investigate whether the geocentrist claim &hellip; had indeed been ruled out of court.&rdquo; That is a presumption offered as a reason to reopen an inquiry, phrased as a question, by a writer who then promises to argue the case on other grounds. It is not a claim that every ancient culture was geocentric, and it is not offered as a proof of anything.</p>

<p><strong>5. Item 367 and the route by which it was searched.</strong> &ldquo;Ancient stone calendars geocentric&rdquo; is a claim about megalithic archaeoastronomy. The strings &ldquo;Stonehenge&rdquo;, &ldquo;megalith&rdquo;, &ldquo;Newgrange&rdquo;, &ldquo;Nabta&rdquo;, &ldquo;pyramid&rdquo; and &ldquo;archaeoastronomy&rdquo; are not located in either of the two texts searched: the Volume&nbsp;I plain-text scan (item GallileoWasWrong, the whole file, 462,000 words) or the Volume&nbsp;II plain-text scan (item &hellip;Bennett4276, seventh edition 2013, chapters 7&ndash;13, the whole file). The historical Volume&nbsp;II of the 2006 two-volume set was not reachable this pass, so nothing here is a statement about what that volume holds. Item 367 is answered on its merits in the refutation regardless of where it came from, because it is on the list and readers meet it.</p>"""),

    steelman=dict(
        description="""<p><strong>SURFACE (weak &mdash; do not use).</strong> &ldquo;Appeal to antiquity, that&rsquo;s a fallacy, next.&rdquo; Naming the fallacy is not answering it, and the sneering version &mdash; the ancients were primitive people guessing &mdash; is false and will lose the exchange to anyone who has opened the <em>Almagest</em>. Greek mathematical astronomy was quantitative, predictive and self-correcting; Ptolemy&rsquo;s model predicted planetary positions well enough to remain the working tool of practising astronomers for fourteen centuries. The people this argument invokes were not credulous, and the source knows it: it quotes Fred Hoyle to the effect that Hipparchus and Ptolemy rejected the heliocentric theory of Aristarchus because &ldquo;the Hipparchus theory grapples with the facts whereas the circular picture of Aristarchus fails to do so&rdquo; &mdash; &ldquo;this, rather than prejudice&rdquo;.</p>

<p><strong>DEEPER.</strong> The weak reading of the claim is simply true, and conceding it costs nothing. From Babylonian celestial omen texts through Aristotle, Ptolemy, the Islamic commentators and the Latin schoolmen, the standing view of educated people for something like two thousand years is a stationary Earth. Dissent existed and was a minority. Anybody who answers this cluster by pretending antiquity was evenly split is overcorrecting, and the source&rsquo;s own p.&nbsp;62 roster does not support an even split either.</p>

<p><strong>KERNEL.</strong> The strongest thing here is not the head-count. It is that <strong>the ancient consensus was evidence-driven, and its authorities named the observation that would overturn it.</strong> Aristotle argues for a central Earth in <em>De caelo</em> and gives reasons; the decisive one, restated by every later geocentrist down to Tycho, is that a moving Earth requires the nearer stars to shift annually against the further ones, and no such shift could be seen. That is a genuine prediction, correctly derived, and it failed for the other side for two thousand years. The consensus was therefore not inertia. It was a large number of careful people reasoning correctly from the best measurements available, and reaching a conclusion the measurements at the time supported. A defender who puts the argument that way &mdash; <em>the ancients agreed because the evidence then agreed</em> &mdash; has said something true, something the history of astronomy backs, and something that no honest account of the period can wave away.</p>""",

        why_it_doesnt_save_claim="""<p>Because a conclusion held for a stated reason is <strong>hostage to that reason</strong>, and the reason was checked. The falsifier the ancients themselves nominated is stellar parallax, and it was found: Bessel published an annual shift of 0.314&Prime; for 61 Cygni in 1838, Henderson and Struve followed within two years, and Gaia DR3 now publishes parallaxes for about 1.47 billion sources. The consensus ended exactly where its own authorities said it would end. Honouring their method means accepting the answer their method returned; keeping the conclusion while discarding the test is not fidelity to Aristotle, it is the opposite of it. The parallax cluster is <a href="#ARG-A05">ARG-A05</a>.</p>

<p>And the kernel cuts against the item in a second way. If the ancients were geocentric <em>on evidence</em>, then their agreement is not independent testimony from many cultures &mdash; it is the same inference, from the same two observations available to everyone with eyes (no felt motion, no visible parallax), reached over and over. Universal agreement among people looking at one appearance is worth exactly what that appearance is worth. It is one datum with a large number of witnesses attached, and the list is counting the witnesses.</p>"""),

    refutation="""<p><strong>First, the concession, and it should be made without grudging.</strong> Geocentrism was the default of the ancient world. Babylonian, Egyptian, Greek, Roman, Indian, Chinese, Mesoamerican and Norse cosmologies all describe a sky that moves over a world that does not, and the learned tradition that ran from Aristotle through Ptolemy to the Latin Middle Ages made a stationary central Earth its first premise. Anybody answering this cluster by suggesting antiquity was divided down the middle has overstated the case &mdash; and would, incidentally, be overstating it in the same direction the source does.</p>

<p><strong>Second, the universal is false, and the counter-witnesses are ancient and primary.</strong> Three of the four items carry an explicit universal quantifier: <em>uniformly</em>, <em>universal</em>, <em>all</em>. One counterexample is enough. The list below carries seven names, six of them Greek, and the testimony for them is ancient rather than modern reconstruction.</p>

<ul>
<li><strong>Philolaus</strong> (5th century BCE) put fire, not Earth, at the centre. The witness is Aristotle, the list&rsquo;s own geocentric authority, in <em>De caelo</em> II.13: &ldquo;At the centre, they say, is fire, and the earth is one of the stars, creating night and day by its circular motion about the centre.&rdquo;</li>
<li><strong>Hicetas, Heraclides and Ecphantus</strong> held that the Earth turns on its axis in a motionless heaven. The witness here is the source itself, footnote 133, quoted above.</li>
<li><strong>Aristarchus of Samos</strong> (c. 310&ndash;230 BCE) put the Sun at the centre and the Earth in orbit. The witness is Archimedes, a contemporary, in the <em>Sand-Reckoner</em> &mdash; a primary document, not a later report &mdash; and the passage is reproduced in this book&rsquo;s own Appendix&nbsp;9.</li>
<li><strong>Seleucus of Seleucia</strong> (fl. c. 150 BCE) defended the same system; Plutarch records that he was the first to <em>demonstrate</em> it by reasoning, though what those arguments were is now lost.</li>
<li><strong>Āryabhaṭa</strong> (<em>Āryabhaṭīya</em>, 499 CE) argued that the Earth turns, in the analogy every history of Indian astronomy quotes: a man in a moving boat sees the stationary objects on the bank go backwards, and so the stationary stars are seen to move west.</li>
</ul>

<p>Item 25 restricts itself to &ldquo;pre-Copernican&rdquo;, which does not help it. Nicholas of Cusa&rsquo;s <em>De docta ignorantia</em> (1440), a century before <em>De revolutionibus</em>, holds that the Earth is not fixed at any given point, cannot be the exact physical centre of the universe, and that the universe has no boundary &mdash; a position from which &ldquo;centre&rdquo; is a matter of where you stand. One case that should be reported accurately rather than recruited: Nicole Oresme, in the <em>Livre du ciel et du monde</em> (1377), answered the standard arguments against the Earth&rsquo;s daily rotation one by one &mdash; including the scriptural ones &mdash; and then declared for a stationary Earth anyway. He is not a counterexample to geocentrism. He is something more awkward for this cluster: a pre-Copernican who concluded that the appearances could not settle the question, which is precisely what items 21, 25 and 119 are being used to deny.</p>

<p><strong>Third, take the weak reading &mdash; and it still does no work.</strong> Suppose we read the items charitably as &ldquo;geocentrism was the near-universal default&rdquo;, which is true. Two things follow, and both go the wrong way for the list.</p>

<p>(a) <strong>The agreement is not corroboration.</strong> Independent witnesses agreeing is evidence; witnesses who all consulted the same source are one witness. Every ancient culture had access to exactly the same two facts &mdash; the ground does not feel like it is moving, and the sky goes round once a day &mdash; and every one of them drew the inference those two facts support. That is not a thousand confirmations. It is one appearance, correctly described, a thousand times; and the appearance is identical on a rotating Earth, which is the whole content of <a href="#ARG-A22">ARG-A22</a>. Universality of this kind is what you predict when a belief is generated by a shared perceptual situation rather than by inquiry, and its presence is therefore not evidence about which model is true. The list treats 461 items as 461 witnesses; this cluster does the same thing to the ancient world.</p>

<p>(b) <strong>The same consensus goes the other way on the list&rsquo;s other half.</strong> From roughly the fourth century BCE, the literate Mediterranean world is as unanimous about the Earth&rsquo;s <em>sphericity</em> as it is about its rest &mdash; Aristotle argued it from the curved shadow in lunar eclipses, Eratosthenes measured the circumference around 240 BCE, Ptolemy ruled out a flat Earth from eclipse timings at different longitudes, and the Islamic and Latin astronomical traditions that inherited all of this treated sphericity as settled. A list that is half flat-earth cannot spend ancient consensus without buying that. The point is developed at <a href="#ARG-C07">ARG-C07</a> and <a href="#ARG-D02">ARG-D02</a> and is not re-run here; what belongs to D01 is the arithmetic of it. Consensus is not a resource you can draw on selectively. If it is evidence, it is evidence for the sphere too.</p>

<p><strong>Fourth, the word &ldquo;cultures&rdquo; is doing work it cannot do.</strong> Note what was conceded in the first section and what was not. Those cosmologies assert <em>geostasis</em> &mdash; a world that does not move &mdash; and that concession stands. <em>Geocentrism</em> is a further and different claim, and it is the one the items make. &ldquo;Geocentric&rdquo; is a term of art out of Greek mathematical astronomy. It means something specific: the Earth occupies the centre of a system of circles or spheres that carry the Sun, Moon and planets, and the model is used to compute positions. A culture with no concept of a cosmic centre and no notion of planetary orbits cannot be geocentric, any more than it can be heliocentric. The Egyptian cosmos is the sky-goddess Nut arched over the earth-god Geb with the Sun sailing a barque; the <em>Enūma Eliš</em> builds heaven and earth from the halves of a body; the Norse world is a tree. These are accounts of order and origin, and they are not answers to the question &ldquo;what goes round what&rdquo;, because that question is not being asked in them. Counting them as geocentric votes recruits as witnesses people who left no testimony on the point &mdash; which is the exact failure this review documents twice elsewhere in family D, where descriptive scholarship about religious symbolism is read as testimony about geography (<a href="#ARG-D04">ARG-D04</a>, <a href="#ARG-D06">ARG-D06</a>).</p>

<p><strong>Fifth, and this one is specific to a list that wants both halves.</strong> Sort the ancient world by what it actually held and the two properties come apart cleanly. The cosmologies that are flat &mdash; Babylonian, early Egyptian, Vedic, Norse &mdash; are not geocentric in the technical sense at all; they have no centre and no orbits to put a centre in. The cosmologies that are unambiguously geocentric &mdash; Aristotle, Ptolemy, and every commentator downstream of them &mdash; are spherical-Earth to a man. <strong>There is no ancient culture that supplies both halves of this list.</strong> The item is written as though antiquity were a single witness who could be called for the whole case; it is two witnesses, and each of them contradicts one half of it.</p>

<p><strong>Sixth, the stone calendars (item 367).</strong> The alignments are real and the good ones are well attested: Historic England&rsquo;s own account has it that &ldquo;Stonehenge&rsquo;s architecture was designed to allow views of the exact points where the summer and winter solstice suns appear or disappear on the horizon&rdquo;, and Newgrange, whose roof-box admits the midwinter sunrise into the passage, is as securely attested. Claims made for other sites vary a good deal in strength, and the honest thing is to take the well-evidenced cases at full value. Three things follow, none of them favourable to the item.</p>

<p>(a) <strong>What an alignment records is a topocentric appearance.</strong> A sightline says: <em>from this spot, at midsummer, the Sun comes up over there</em>. That statement is about the relation of a horizon to a rising point, and it is predicted identically by a turning Earth and a turning sky. It is the same non-discriminating observation as <a href="#ARG-A22">ARG-A22</a>, cut in stone. A monument cannot testify for a cosmology when both cosmologies build it in the same place.</p>

<p>(b) <strong>The builders left no cosmology.</strong> The people who raised Stonehenge, Nabta Playa and Newgrange were preliterate: what survives from them is earthworks, timber and stone, and no statement of their cosmology survives at all. Calling their monuments &ldquo;geocentric&rdquo; is an inference from a sightline to a metaphysics, across a gap the evidence does not span &mdash; and the field itself is careful about exactly this, Historic England noting that &ldquo;archaeoastronomy is an interdisciplinary field prone to misinterpretation and speculation&rdquo; and that the monument&rsquo;s relationship to the Moon &ldquo;is much more difficult to prove&rdquo;. The cautionary case is Gerald Hawkins&rsquo;s <em>Stonehenge Decoded</em>, whose eclipse-computer reading R. J. C. Atkinson took apart in <em>Antiquity</em> 40 (1966), pp.&nbsp;212&ndash;216, concluding that the alignment counts claimed were &ldquo;wholly consistent with the hypothesis that the alignments claimed are accidental&rdquo;. The solstitial axis survived that scrutiny. The cosmological readings did not.</p>

<p>(c) <strong>The stones no longer point quite where they pointed, and the correction is dynamical.</strong> The obliquity of the ecliptic is not fixed: on the standard polynomial it was 23.97&deg; around 2500 BCE against 23.44&deg; today. At Stonehenge&rsquo;s latitude of 51.18&deg;N that moves the azimuth of midsummer sunrise from about 49.6&deg; to about 50.6&deg; &mdash; a shift of roughly one degree, about two solar diameters, over the monument&rsquo;s lifetime. (Reproducible: cos&nbsp;<em>A</em>&nbsp;=&nbsp;sin&nbsp;&delta;&nbsp;/&nbsp;cos&nbsp;&phi;, flat horizon, centre of the disc, refraction ignored.) Archaeoastronomers apply that correction as a matter of course, and it is what lets an alignment be used to date a structure. In standard theory the drift is a consequence of planetary perturbation of a spinning, orbiting Earth&rsquo;s axis. A geocentrist can of course redescribe it as a slow tilt of the sky, and that redescription costs nothing kinematically &mdash; which is the honest point to make here. What cannot be said is that the monument confirms anything. The stones record where the Sun rose; they are silent on why.</p>

<p><strong>Seventh, the argument form, and the tradition&rsquo;s own answer to it.</strong> &ldquo;Everyone used to believe X&rdquo; is a premise about the history of opinion, and the conclusion the list wants is about the Earth. The bridge between them &mdash; that long agreement is truth-tracking &mdash; is the only part that would need defending, and the four items state the premise and stop, leaving the reader to supply it. Nor is it a bridge this tradition can afford, because its own patron crossed the other way: Tycho Brahe&rsquo;s observations of the comet of 1577 put the object beyond the Moon and helped dissolve the crystalline spheres that ancient consensus had held for two thousand years, and Eratosthenes settled the size of the Earth around 240 BCE by measuring it rather than by counting authorities. The ancient world&rsquo;s best moments are the ones where somebody stopped polling and took a reading. That is the part of antiquity worth appealing to, and it is the part this item leaves out.</p>

<p><strong>Verdict.</strong> The universal is false and its falsification sits in the work our record credits as its origin: p.&nbsp;62 of Volume&nbsp;I calls the ancient position a debate rather than a consensus and names the other side. The true weaker version &mdash; geocentrism was the default &mdash; is conceded in full and discriminates between nothing, because the appearance that produced it is identical on both models, and because the same consensus is just as firm about a spherical Earth. Four items, three of them the same sentence with different words, and none of them a measurement.</p>""",

    advocate=dict(
        best_defense=(
            "You have spent a page refuting the word “all”, which nobody means literally, and "
            "you know it. The claim is that geocentrism was the settled framework of every "
            "civilisation that left us a cosmology, and you conceded that in your first "
            "sentence. Aristarchus is famous precisely because he stood alone: antiquity heard "
            "him and rejected him, and — as your own steelman admits — rejected him on "
            "evidence, not prejudice. A handful of dissenters no more breaks the consensus than "
            "a handful of modern dissenters breaks yours. Second, your “shared appearance” move "
            "proves far too much. Universal agreement that fire is hot is also produced by a "
            "shared perceptual situation; by your rule it is worthless as evidence. What you "
            "have actually said is that agreement never counts unless you like the conclusion. "
            "Third, and this is the one you should worry about: your best material is our book. "
            "You quote page 62 to show the list is wrong, which means you agree that the "
            "authors are careful, honest with the record, and not the people who wrote the list "
            "you are reviewing. So which is it? Either Galileo Was Wrong is a reliable account "
            "of the history — in which case stop citing a 461-item internet list as though it "
            "were our position — or it is not, in which case you cannot use it as your star "
            "witness. You have built your headline finding out of our scholarship and then "
            "billed us for a webpage we did not write."),
        survives=4,
        preemptive=(
            "Four, and the number is driven by the third move, not the first two. Three "
            "concrete changes, all of which are in the text above and must stay there. "
            "(a) The 'nobody means all literally' hit is disarmed BEFORE it lands: section "
            "Third grants the weak reading explicitly and then defeats it twice, and section "
            "First concedes the default in the opening sentence. If an editor ever cuts the "
            "concession to save space, the entry becomes exactly the pedantic quantifier-"
            "hunting the defender accuses it of. Do not cut it. "
            "(b) The 'fire is hot' analogy is the strongest thing in this defence and the text "
            "must answer it rather than leave it implied. The answer is a distinction the "
            "refutation already turns on and should state in one sentence: shared perception is "
            "excellent evidence about the appearance and no evidence about the mechanism behind "
            "it. Everyone agreeing that fire feels hot settles what fire feels like; it does "
            "not settle phlogiston versus oxidation. Everyone agreeing that the sky turns "
            "settles that the sky appears to turn — which both models predict, which is why "
            "ARG-A22 is scored STANDARD PHYSICS and not REFUTED. "
            "(c) The 'you are citing us against a list we did not write' move is the hedge "
            "rule's own bite turned around, and it deserves a straight answer rather than a "
            "flinch: yes, and that is the finding. The compression block says so in terms — the "
            "source is better than the list, the list is what circulates, and both facts get "
            "published. The one thing the entry must not do is soften the drift finding to "
            "avoid the charge. Cross-link the compression block from the refutation's closing "
            "paragraph if a reader could otherwise reach the verdict without meeting it.")),

    straw_man=dict(
        identified=True,
        detail=("The items are aimed at a position nobody holds. No historian of astronomy "
                "denies that geocentrism was antiquity's default, and the standard accounts - "
                "Dreyer, Duhem, Kuhn, all of whom this source cites approvingly - treat "
                "Ptolemaic astronomy as competent quantitative science rather than as "
                "superstition. Stating the consensus as though it were contested lets the item "
                "read as a refutation of somebody, while the inference that would make it an "
                "argument - that long agreement tracks truth - is never written down and so "
                "never has to be defended. There is a second, quieter misdescription in the "
                "framing: it presents the moving Earth as a modern intrusion on an undisturbed "
                "tradition, when Aristarchus put the Sun at the centre roughly four centuries "
                "before Ptolemy wrote the Almagest. Within the ancient tradition itself, the "
                "fully worked geocentric system is the later arrival.")),

    compression=dict(
        assessed=True, drifted=True,
        list_phrasing=("Ancient cosmologies uniformly geocentric. / Pre-Copernican universal "
                       "geocentrism. / All ancient cultures geocentric. / Ancient stone "
                       "calendars geocentric."),
        source_wording=("“[History] has been divided right down the middle … by the on-going debate "
                        "as to what revolves around what; <em>a debate that stretches as far back "
                        "as written records take us</em>. … it was the Pythagorean school of "
                        "heliocentrists: Plato, Philolaus, Pliny, Aristarchus, and Seleucus versus "
                        "the geocentric school of Aristotle, Hipparchus, Theon of Smyrna, "
                        "Appolonius and Ptolemy.” (Vol. I, p. 62)"),
        drift_type="reversed",
        note=("This is not a hedge that got firmed up. It is a <strong>negation</strong>. The work our "
              "record credits with these four items opens its historical survey by describing ancient "
              "cosmology as a controversy running as far back as written records go, names a roster of "
              "ancient heliocentrists, adds three more ancients who held the Earth to rotate in a "
              "footnote on the same spread, and reproduces Archimedes on Aristarchus in its Appendix 9. "
              "The list turns that into &ldquo;uniformly&rdquo;, &ldquo;universal&rdquo; and "
              "&ldquo;all&rdquo;. Compare <a href=\"#ARG-A05\">ARG-A05</a>, where Rowbotham&rsquo;s own "
              "third edition prints the parallax measurements the cluster is titled against: same shape, "
              "different lineage, and it is becoming the review&rsquo;s most common single finding."
              "<br><br>"
              "<strong>What the source&rsquo;s actual appeal to antiquity looks like.</strong> The one "
              "located in the two scans searched is at Vol. I p. 130 and is a quotation from Wolfgang "
              "Smith&rsquo;s <em>The Wisdom of Ancient Cosmology</em> (2003), pp. 180&ndash;181: "
              "geocentrism is &ldquo;not only an ancient, but indeed a traditional doctrine; should we "
              "not presume that as such it enshrines a perennial truth?&rdquo; A question, about a "
              "doctrinal tradition rather than about world cultures, offered as grounds to reopen an "
              "inquiry &mdash; &ldquo;It will not be without interest, therefore, to investigate whether "
              "the geocentrist claim &hellip; had indeed been ruled out of court.&rdquo; The list "
              "publishes the presumption as a finding and drops the investigation it was raised to "
              "justify."
              "<br><br>"
              "<strong>And the refutation above answers the source, not the fragment.</strong> The "
              "source&rsquo;s real position &mdash; antiquity was divided, and the geocentric majority "
              "held its view on evidence &mdash; is the position the steelman is built on and the "
              "refutation engages: the majority is conceded in the first sentence, the evidence-driven "
              "reading is credited as the kernel, and the weight falls on what a consensus generated by "
              "a shared appearance can be worth. Item 367 is a separate matter: &ldquo;Stonehenge&rdquo;, "
              "&ldquo;megalith&rdquo;, &ldquo;Newgrange&rdquo; and &ldquo;Nabta&rdquo; are not located "
              "in either the Volume I or the Volume II scan searched, so on the evidence reachable this "
              "pass it is an <em>unsourced_addition</em> riding along with three items that are "
              "<em>reversed</em>; the single enum value records the dominant drift, and this sentence "
              "records the rest."),
    ),

    verdict_challenge=dict(
        challenged=True,
        proposed_verdict="REFUTED",
        reasoning=(
            "The cluster is scored NOT DEMONSTRATED, and its own `note` already says the claim is "
            "\"false in detail\". Those two do not sit together. NOT DEMONSTRATED is the right "
            "verdict for an argument whose premises are true but which does not reach its "
            "conclusion - which is why it fits D02, where the named authorities are real and simply "
            "support the wrong thing. Here the premise itself fails: three of the four items carry "
            "an explicit universal quantifier (\"uniformly\", \"universal\", \"all\"), and a "
            "universal falls to one counterexample. There are six, all attested by ancient primary "
            "witnesses rather than modern reconstruction - Philolaus via Aristotle's De caelo II.13, "
            "Hicetas, Heraclides and Ecphantus via the source's own footnote 133, Aristarchus via "
            "Archimedes' Sand-Reckoner, Seleucus via Plutarch - plus Aryabhata in 499 CE and, for "
            "item 25's narrower \"pre-Copernican\", Nicholas of Cusa in 1440. That is the same "
            "evidential situation as A08, A10 and A14, all of which are REFUTED. "
            "SELF-CONTRADICTED was considered and is defensible, on the B06/R11 pattern where the "
            "movement's own cited authority states the opposite: p. 62 of Volume I calls ancient "
            "cosmology a debate \"that stretches as far back as written records take us\" and names "
            "the heliocentric side. It was not proposed because the proposition is false "
            "independently of who cited it - the ancient counter-witnesses would sink it if Galileo "
            "Was Wrong had never been written - and because the self-contradiction is already "
            "published, in its proper place, as a `reversed` drift in the compression block. Using "
            "it twice would double-count one finding. "
            "The honest case for leaving NOT DEMONSTRATED alone: if the cluster is read as scoring "
            "the *inference* (ancient consensus therefore stationary Earth) rather than the "
            "*proposition*, then NOT DEMONSTRATED is correct and the falsity of the premise is a "
            "bonus. The refutation covers that reading too, in its third section, so no argument is "
            "lost either way. The operator decides. If the change is made, the cluster `note` should "
            "lose its Eratosthenes clause, which is about the Earth's shape rather than its place "
            "and belongs with C07."),
    ),

    people=["PER-SUNGENIS"],
    related=["D02", "D03", "D19", "D04", "D06", "C07", "A22", "A05", "R11"],

    sources=[
        dict(label="Sungenis & Bennett, Galileo Was Wrong Vol. I, The Scientific Evidence — "
                   "the “debate that stretches as far back as written records take us” and the "
                   "heliocentrist roster at printed p. 62; footnote 133 on Hicetas, Heraclides "
                   "and Ecphantus; Wolfgang Smith quoted at p. 130; Archimedes on Aristarchus in "
                   "Appendix 9, footnote 1565 (scan pp. 1041–42). Internet Archive item "
                   "GallileoWasWrong, plain-text OCR searched in full",
             url="https://archive.org/details/GallileoWasWrong"),
        dict(label="Sungenis & Bennett, Galileo Was Wrong Vol. II (7th ed., 2013, chs 7–13) — "
                   "the second scan searched for the stone-calendar material",
             url="https://archive.org/stream/GalileoWasWrongTheChurchSungenisRobertA.Bennett4276/Galileo%20Was%20Wrong_%20The%20Church%20%20-%20Sungenis,%20Robert%20A.%20&%20Bennett,_4276_djvu.txt"),
        dict(label="Aristotle, De caelo II.13 (Stocks translation) — the Pythagorean central "
                   "fire, “the earth is one of the stars”, and the disputed rotating-Earth "
                   "reading of the Timaeus",
             url="http://classics.mit.edu/Aristotle/heavens.2.ii.html"),
        dict(label="Heath, Aristarchus of Samos: The Ancient Copernicus (Clarendon Press, 1913) — "
                   "the standard collection of the ancient testimony, and the volume Sungenis "
                   "cites for it",
             url="https://archive.org/details/aristarchusofsam00heat"),
        dict(label="Dreyer, History of the Planetary Systems from Thales to Kepler (1906) — the "
                   "translation of Archimedes' Sand-Reckoner quoted inside Galileo Was Wrong",
             url="https://archive.org/details/historyofplaneta00dreyuoft"),
        dict(label="Seleucus of Seleucia — Plutarch's report that he was the first to demonstrate "
                   "the heliocentric system by reasoning; the arguments themselves are lost",
             url="https://en.wikipedia.org/wiki/Seleucus_of_Seleucia"),
        dict(label="Parakh, “A Note on Āryabhaṭa's Principle of Relativity” (arXiv) — the boat "
                   "analogy at Gola 9 of the Āryabhaṭīya, on the Earth's rotation",
             url="https://arxiv.org/pdf/physics/0610095"),
        dict(label="Stanford Encyclopedia of Philosophy, “Nicholas of Cusa” — De docta ignorantia "
                   "(1440): the Earth is not fixed in place and cannot be the exact physical "
                   "centre of the universe",
             url="https://plato.stanford.edu/entries/cusanus/"),
        dict(label="Historic England, “Astronomical Research at Stonehenge” — the solstitial axis, "
                   "the difficulty of the lunar case, and the field's own warning that "
                   "archaeoastronomy is “prone to misinterpretation and speculation”",
             url="https://historicengland.org.uk/whats-new/research/back-issues/astronomical-research-at-stonehenge/"),
        dict(label="R. J. C. Atkinson, “Moonshine on Stonehenge”, Antiquity 40 (159), September "
                   "1966, pp. 212–216 — the statistical demolition of the Stonehenge Decoded "
                   "eclipse-computer reading",
             url="https://www.cambridge.org/core/services/aop-cambridge-core/content/view/8BA0BBA8A51E43C1EC551869154710FA/S0003598X0003252Xa.pdf/moonshine-on-stonehenge.pdf"),
    ]),
}
