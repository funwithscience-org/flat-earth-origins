# -*- coding: utf-8 -*-
"""
WRK-* — the publications the claims descend from.

`pd` (public domain) governs how much original text we may reproduce:
  True  -> quote the passage in full, link the scan
  False -> short fair-use excerpt + citation only
This distinction is surfaced on the page so the uneven depth between lanes
reads as a legal constraint, not as uneven effort.
"""

WORKS = {
"WRK-ROWBOTHAM-1849": dict(
    author="PER-ROWBOTHAM", year="1849", pd=True,
    title="Zetetic Astronomy: A description of several experiments which prove that "
          "the surface of the sea is a perfect plane, and that the earth is not a globe",
    imprint="By “Parallax” [pseud.]. Birmingham: W. Cornish. 16 pp.",
    url="https://guides.loc.gov/flat-earth/books",
    note="The 16-page first pamphlet. Everything in the zetetic lane starts here."),

"WRK-ROWBOTHAM-1865": dict(
    author="PER-ROWBOTHAM", year="1865", pd=True,
    title="Earth Not a Globe",
    imprint="1st book edition, 221 pp. 2nd ed., rev. and enl., London: John B. Day, 1873. "
            "3rd ed., rev. and enl., London: Day, 1881, 430 pp.",
    url="https://sacred-texts.com/earth/za/index.htm",
    note="Discursive prose in numbered SECTIONS (I–XV). Verified: no numbered proof-list is "
         "located in the 1865 or 1881 texts — that format is Carpenter's. Note the three book "
         "editions before citing this record: Schadewald credits Rowbotham with 76 scriptures "
         "in the last chapter of the SECOND edition, which his own bibliography dates to 1873, "
         "and that edition was not reached for this review."),

"WRK-CARPENTER-1885": dict(
    author="PER-CARPENTER", year="1885", pd=True,
    title="One Hundred Proofs that the Earth Is Not a Globe",
    imprint="Baltimore: printed and published by the author, 71 Chew Street. "
            "Preface dated August 1885; LoC deposit 8 October 1885; 6 editions in ~18 months.",
    url="https://www.gutenberg.org/ebooks/55387",
    note="The origin of the numbered-proof-list format. Each item closes "
         "“…is a proof that the Earth is not a globe.”"),

"WRK-WINSHIP-1899": dict(
    author="PER-WINSHIP", year="1899", pd=True,
    title="Zetetic Cosmogony; or, Conclusive evidence that the world is not a "
          "rotating-revolving-globe, but a stationary plane circle",
    imprint="By “Rectangle” [pseud.]. 2nd ed., enl. Durban, Natal: T. L. Cullingworth. 192 pp.",
    url="https://guides.loc.gov/flat-earth/books",
    note="First edition date not established — the 1899 printing is explicitly the second."),

"WRK-VOLIVA-ZION": dict(
    author="PER-VOLIVA", year="1915", pd=True,
    title="Zion sermons and Leaves of Healing",
    imprint="Christian Catholic Apostolic Church, Zion, Illinois. Flat-earth doctrine "
            "adopted March 1916; taught in Zion's schools from 1916; radio station WCBD from 1922.",
    url="https://www.cantab.net/users/michael.behrend/ebooks/PlaneTruth/pages/Chapter_08.html",
    note="Reprinted Carpenter's 100 Proofs under his own Zion imprint in 1929 — the "
         "documented bridge carrying the Victorian list into the 20th century."),

"WRK-JOHNSON-FEN": dict(
    author="PER-JOHNSON", year="1972", pd=False,
    title="Flat Earth News",
    imprint="Quarterly, International Flat Earth Research Society, Lancaster, California. "
            "Society records destroyed by fire, 1997.",
    url="https://en.wikipedia.org/wiki/Charles_K._Johnson",
    note="Where the conspiracy frame enters: astronomers are not mistaken but lying."),

"WRK-VDK-1988": dict(
    author="PER-VANDERKAMP", year="1988", pd=False,
    title="De Labore Solis: Airy's Failure Reconsidered",
    imprint="Self-published, Pitt Meadows, B.C.",
    url="https://geocentricity.com/bibastron/ts_history/de_labore.pdf",
    note="Earliest DOCUMENTED use of the phrase “Airy's failure” — subtitle, chapter "
         "title (“The Unfailing Import of Airy's Failure”, p. 52), and throughout. "
         "The 1968/1970 precursor was titled Airy RECONSIDERED, without “failure”; "
         "whether the phrase appears inside it is unverified."),

"WRK-BOUW-1992": dict(
    author="PER-BOUW", year="1992", pd=False,
    title="Geocentricity",
    imprint="Association for Biblical Astronomy, Cleveland.",
    url="https://creation.com/geocentric-gobbledegook",
    note="By the movement's only credentialed astronomer (PhD, Case Western Reserve). "
         "Concedes the model is observationally equivalent to heliocentrism."),

"WRK-SUNGENIS-2006": dict(
    author="PER-SUNGENIS", year="2006", pd=False,
    title="Galileo Was Wrong: The Church Was Right",
    imprint="With Robert J. Bennett. The Vol. I read for this review is the CD-ROM issue, "
            "ISBN 0-9779640-0-0 (Internet Archive item GallileoWasWrong), whose title page reads "
            "“Galileo Was Wrong: The Scientific, Scriptural, Ecclesiastical and Patristic "
            "Evidence for Geocentrism / Volume I / The Scientific Evidence” and whose "
            "introduction is signed 25 April 2006. “Volume I, The Scientific Case for "
            "Geocentrism” is the hardcover's subtitle (ISBN 0-9779640-5-1, catalogued 2007) — a "
            "different printing, not the same title page. "
            "Five editions in two volumes, 2005–2010; three volumes from the sixth edition "
            "of January 2013, in which Vol. II is chapters 7–13 of the scientific argument "
            "and Vol. III, chapters 14–17, the church-history volume. 7th ed. 2013.",
    url="https://www.goodreads.com/series/55023-galileo-was-wrong",
    note="Direct source of the Michelson–Gale, Sagnac, Miller, Foucault and Airy material "
         "in modern lists. In copyright — short excerpts only."),

"WRK-PRINCIPLE-2014": dict(
    author="PER-SUNGENIS", year="2014", pd=False,
    title="The Principle (film)",
    imprint="Produced by Rick DeLano and Robert Sungenis; narrated by Kate Mulgrew. "
            "Released 24 October 2014.",
    url="https://en.wikipedia.org/wiki/The_Principle",
    note="Narrator Mulgrew publicly disavowed it 8 April 2014; Krauss, Kaku, Tegmark, "
         "Ellis and Barbour all objected to their appearances."),

"WRK-DUBAY-2015": dict(
    author="PER-DUBAY", year="2015", pd=False,
    title="200 Proofs Earth Is Not a Spinning Ball",
    imprint="Free PDF and YouTube videobook, 2015; print editions 2018.",
    url="https://flatearth.ws/eric-dubay",
    note="Names Rowbotham, Carpenter, Winship, Scott and Blount's Earth Review in 17 of "
         "its 200 items, and closes at #200 with a Rowbotham quotation."),

"WRK-SARGENT-2015": dict(
    author="PER-SARGENT", year="2015", pd=False,
    title="Flat Earth Clues",
    imprint="YouTube video series, February 2015.",
    url="https://en.wikipedia.org/wiki/Mark_Sargent_(flat_Earth_proponent)",
    note="The enclosed-world model: disc, ice wall, indestructible dome, stars as lights on it."),

"WRK-SKIBA-2018": dict(
    author="PER-SKIBA", year="2018", pd=False,
    title="Testing the Globe: A Zetetic Investigation",
    imprint="424 pp. Catalogued with Samuel Rowbotham and William Carpenter as CO-AUTHORS.",
    url="https://books.google.com/books/about/Testing_the_Globe.html?id=7JU6vQEACAAJ",
    note="The movement reissuing its own Victorians under joint byline."),

"WRK-BTC-2018": dict(
    author="PER-KNODEL", year="2018", pd=False,
    title="Behind the Curve (dir. Daniel J. Clark)",
    imprint="US release 15 November 2018; Netflix February 2019.",
    url="https://www.newsweek.com/behind-curve-netflix-ending-light-experiment-mark-sargent-documentary-movie-1343362",
    note="Knodel's ring-laser gyroscope measures a 15°/hour drift on camera."),

"WRK-KYBALION-1908": dict(
    author="PER-ATKINSON", year="1908", pd=True,
    title="The Kybalion",
    imprint="By “Three Initiates”. Chicago: Yogi Publication Society.",
    url="https://en.wikipedia.org/wiki/The_Kybalion",
    note="Where modern “as above, so below” actually comes from — a New Thought pamphlet, "
         "not Egyptian cosmology."),

"WRK-BLAVATSKY-1877": dict(
    author="PER-BLAVATSKY", year="1877", pd=True,
    title="Isis Unveiled; The Secret Doctrine (1888–89)",
    imprint="Theosophical Society, founded New York, 7 September 1875.",
    url="https://en.wikipedia.org/wiki/Helena_Blavatsky",
    note="Her claimed source, the “Book of Dzyan”, is regarded by Buddhist-studies "
         "scholars as her own invention."),

"WRK-HALL-1928": dict(
    author="PER-HALL", year="1928", pd=True,
    title="The Secret Teachings of All Ages",
    imprint="An Encyclopedic Outline of Masonic, Hermetic, Qabbalistic and Rosicrucian "
            "Symbolical Philosophy. Los Angeles.",
    url="https://en.wikipedia.org/wiki/Manly_P._Hall",
    note="Esoteric popularizer, self-described. Interpretive, not historical-critical."),

"WRK-ELIADE-1949": dict(
    author="PER-ELIADE", year="1949", pd=False,
    title="The Myth of the Eternal Return; Patterns in Comparative Religion",
    imprint="Originally Le Mythe de l'éternel retour and Traité d'histoire des religions.",
    url="https://www.britannica.com/biography/Mircea-Eliade",
    note="A historian of religion describing SYMBOLISM. Jonathan Z. Smith (To Take Place, "
         "1987) showed even the universality claim rests on a conflation of two incidents "
         "thirty pages and thirty years apart in Spencer and Gillen."),

"WRK-PTOLEMY-ALMAGEST": dict(
    author="PER-PTOLEMY", year="c. 150 CE", pd=True,
    title="Almagest",
    imprint="Alexandria.",
    url="https://en.wikipedia.org/wiki/Almagest",
    note="Geocentric AND spherical. Cited by the list against its own flat half."),
}
