# -*- coding: utf-8 -*-
"""
PER-* — the people the claims descend from.

Every field is a claim about a real person, so the bar is higher than for
arguments. Rules enforced in tests/:
  * every biographical assertion carries a source
  * `formation` and `ignored` distinguish what they SAID from what we INFER
  * `kernel` is mandatory — find what they got right before showing why it fails
  * `bio_status: "stub"` means verified facts only, no interpretation yet

Schema per record:
  name, dates, lineage, role     identity
  works[]                        WRK-* ids
  bio_status                     "worked" | "stub"
  formation                      where the position came from, and why
  had                            the data genuinely available to them, honestly used
  ignored                        the data available and not engaged
  kernel                         {description, why_it_doesnt_save_claim}
  legacy                         what descends from them
  sources[]                      {label, url}
"""

def _p(**kw):
    kw.setdefault("bio_status", "stub")
    for f in ("formation", "had", "ignored", "legacy"):
        kw.setdefault(f, None)
    kw.setdefault("kernel", None)
    kw.setdefault("sources", [])
    kw.setdefault("works", [])
    return kw


PEOPLE = {

# ─────────────────────────────────────────────── worked example (zetetic)
"PER-ROWBOTHAM": _p(
    name="Samuel Birley Rowbotham", dates="1816 – 23 December 1884",
    lineage="Zetetic", role="Founder of the zetetic tradition. Wrote as “Parallax”.",
    works=["WRK-ROWBOTHAM-1849", "WRK-ROWBOTHAM-1865"],
    bio_status="worked",
    formation=(
        "Rowbotham began at Manea Fen, a short-lived Owenite socialist commune in the "
        "Cambridgeshire Fens, in the late 1830s. The setting matters more than it looks: "
        "the Old Bedford Canal runs arrow-straight for six miles there, and it was the "
        "one piece of apparatus he had. His method came out of the same milieu — a "
        "self-taught radical's distrust of credentialed authority, formalised as the "
        "<em>zetetic</em> method: from Greek <em>zeteo</em>, to search. In his own words, "
        "it proceeds “only by inquiry; to take nothing for granted” and stands "
        "“in contradistinction from the word ‘theoretic,’ the meaning of which is, "
        "speculative—imaginary—not tangible.” That sentence is the load-bearing move of "
        "the entire tradition, and everything downstream inherits it: observation is real, "
        "theory is imaginary. He wrote as “Parallax” from the end of 1849 — in the ordinary "
        "optical sense of an apparent shift with viewpoint, which is the engine of his own "
        "perspective theory. (An earlier version of this page said he named himself after "
        "the measurement he spent his life denying. That was false and was withdrawn on "
        "2026-08-07: he adopted the name 32 years before he wrote about stellar parallax, "
        "and he relied on the phenomenon rather than denying it.)"),
    had=(
        "More than he is usually credited with. The “8 inches per mile, multiplied by the "
        "square of the distance” figure is not invented — he lifted it from the "
        "<em>Encyclopaedia Britannica</em> article on Levelling, and it is genuine "
        "surveying arithmetic for the difference between true and apparent level. He read "
        "the astronomy of his day and engaged its numbers. His observations at the canal "
        "were real observations, repeated over years, and he reported what he actually saw."),
    ignored=(
        "Two things, and the second is the fatal one. First, atmospheric refraction over "
        "water — described in the surveying literature he was quoting <em>from</em>, and "
        "the reason a near-water sightline over a canal is the single worst configuration "
        "in which to test for curvature. Second, and unanswerable: the southern sky. "
        "Circumpolar star trails rotating about a <em>southern</em> pole had been logged by "
        "European navigators for three centuries and were in every nautical almanac he "
        "could have opened. No single-plane model produces two opposite centres of "
        "rotation. He did not engage it."),
    kernel=dict(
        description=(
            "The zetetic complaint had a real target. Mid-Victorian popular astronomy did "
            "ask readers to accept a great deal on authority, often with textbook diagrams "
            "that were schematic rather than measured, and Rowbotham was right that "
            "“because the astronomers say so” is not evidence. His insistence on going and "
            "looking is, in the abstract, the correct instinct — and his 8-inches-per-mile "
            "formula is correct arithmetic, honestly sourced."),
        why_it_doesnt_save_claim=(
            "Because the instinct was applied with a stopping rule. Going and looking is "
            "only zetetic if you keep looking after the first result agrees with you. "
            "Rowbotham quoted the surveyors' curvature correction and then denied the thing "
            "it corrects for; he ran the canal experiment in the one geometry where "
            "refraction guarantees a false null and never varied it. When Wallace varied it "
            "in 1870 — sightline raised to 13 feet, a third marker at the midpoint — the "
            "curvature appeared, and Oldham reproduced it in 1901. The method was not "
            "wrong. It was stopped early.")),
    legacy=(
        "65 of the 461 items on the specimen list descend from him — the single largest "
        "share by any one author. Bedford Level, water-finds-its-level, horizon-at-eye-"
        "level, the perspective account of sunset, surveyors-make-no-allowance, and the "
        "vertical-projectile argument against rotation are all his. Carpenter condensed "
        "him into 100 numbered proofs in 1885; Voliva reprinted Carpenter at Zion in 1929; "
        "Dubay quotes him by name in nine of 200 proofs and closes the list with him."),
    sources=[
        dict(label="Zetetic Astronomy, 3rd ed. 1881 — full text",
             url="https://sacred-texts.com/earth/za/index.htm"),
        dict(label="Schadewald, The Plane Truth, ch. 1",
             url="https://www.cantab.net/users/michael.behrend/ebooks/PlaneTruth/pages/Chapter_01.html"),
        dict(label="Library of Congress — The Flat Earth and its Advocates",
             url="https://guides.loc.gov/flat-earth/books"),
        dict(label="Bedford Level experiment — Wallace 1870, Oldham 1901",
             url="https://en.wikipedia.org/wiki/Bedford_Level_experiment")]),

# ─────────────────────────────────────────────── worked example (tychonian)
"PER-VANDERKAMP": _p(
    name="Walter van der Kamp", dates="5 March 1913 – 26 January 1998",
    lineage="Tychonian", role="Founder of modern geocentrism. Coined “Airy's failure”.",
    works=["WRK-VDK-1988"],
    bio_status="worked",
    formation=(
        "A Dutch-Canadian schoolteacher, not a scientist, working from Pitt Meadows, "
        "British Columbia. He came to geocentrism through Reformed theology rather than "
        "through physics, and circulated his first brochure — <em>The Heart of the "
        "Matter</em>, 32 pages — to about fifty people in 1967. By his own account it "
        "“went nowhere fast.” He founded the Tychonian Society in 1971 and edited its "
        "<em>Bulletin</em> through 1984, the early issues handwritten and photocopied. His "
        "argument was structural, not observational: he held that heliocentrism rests on "
        "affirming the consequent — the theory predicts what we see, therefore the theory "
        "is true — and he read Popper and Dingle to sharpen the point."),
    had=(
        "The actual experimental record, and he read it more carefully than most of his "
        "successors. He identified correctly that Michelson–Morley returned a null, that "
        "Airy's 1871 water-telescope experiment returned a null, and that both nulls were "
        "genuinely awkward for the aether physics of their own moment. His logical "
        "objection — that a theory fitting the data does not make the theory unique — is a "
        "real point in philosophy of science, and it is the same point Duhem and Quine "
        "were making in more respectable company."),
    ignored=(
        "That both nulls had been <em>predicted in advance</em>, by two different theories, "
        "for reasons having nothing to do with a stationary Earth. Fresnel's dragging "
        "coefficient predicted Airy's null before Airy ran it; special relativity predicts "
        "it again from the transformation of ray direction between frames. He also passed "
        "over Michelson–Gale–Pearson (1925), a positive detection of Earth's rotation "
        "published in the <em>Astrophysical Journal</em>, which measures the very motion he "
        "denied — and over stellar aberration, which exists at all only because the Earth "
        "moves, and which his own successor Bouw rebuilt the model to accommodate."),
    kernel=dict(
        description=(
            "The underdetermination argument is not crankery. Van der Kamp was right that "
            "a null result cannot by itself select between “no motion” and “motion plus a "
            "compensating effect,” and right that general relativity permits physics to be "
            "written in Earth-centred coordinates. Bouw, his successor and the movement's "
            "only credentialed astronomer, took the argument to its honest conclusion and "
            "conceded in print that the model is <em>observationally equivalent</em> to "
            "heliocentrism and must therefore be chosen on theological grounds."),
        why_it_doesnt_save_claim=(
            "Because that concession is the end of the argument, not the start of one. If "
            "the two descriptions are observationally equivalent, then no experiment — "
            "including Airy's, including Michelson–Morley — is <em>evidence</em> for either. "
            "The movement cannot simultaneously claim that the frames are indistinguishable "
            "and that specific experiments distinguish them in its favour. Every item on "
            "the specimen list that cites an experiment is spending the concession it "
            "elsewhere relies on.")),
    legacy=(
        "24 items on the list, six distinct arguments, and one phrase that has outlived "
        "him. “Airy's failure” exists nowhere in the physics literature — every occurrence "
        "traces to this movement, and Bouw's obituary of him credits the coinage by name, "
        "calling him “the father of modern geocentricity.” Sungenis inherits the term "
        "without attribution, writing that the experiment “was called” that, and adding "
        "the false gloss that it reflects “the thoughts of the experimenters during this "
        "era.” Airy's own paper is titled neutrally and does not contain the word."),
    sources=[
        dict(label="De Labore Solis: Airy's Failure Reconsidered (1988)",
             url="https://geocentricity.com/bibastron/ts_history/de_labore.pdf"),
        dict(label="Bouw's obituary of van der Kamp, The Biblical Astronomer no. 84",
             url="https://www.geocentricity.com/ba1/no084/obits.pdf"),
        dict(label="Association for Biblical Astronomy — society history",
             url="https://www.geocentricity.com/bibastron/index.html"),
        dict(label="Michelson, Gale & Pearson 1925, ApJ 61:140 — original paper",
             url="https://paulba.no/paper/Michelson_Gale_II.pdf")]),

# ─────────────────────────────────────────────── stubs (verified facts only)
"PER-CARPENTER": _p(
    name="William Carpenter", dates="25 February 1830 – 1 September 1896",
    lineage="Zetetic", role="Originated the numbered-proof-list format.",
    works=["WRK-CARPENTER-1885"],
    sources=[dict(label="One Hundred Proofs (1885) — full text",
                  url="https://www.gutenberg.org/ebooks/55387")]),

"PER-WINSHIP": _p(
    name="Thomas Winship", dates="fl. 1899", lineage="Zetetic",
    role="Wrote as “Rectangle”; first significant zetetic text outside Britain/USA.",
    works=["WRK-WINSHIP-1899"],
    sources=[dict(label="LoC — The Flat Earth and its Advocates",
                  url="https://guides.loc.gov/flat-earth/books")]),

"PER-VOLIVA": _p(
    name="Wilbur Glenn Voliva", dates="10 March 1870 – 11 October 1942",
    lineage="Zetetic", role="Institutional capture: schools, radio, and the 1929 reprint.",
    works=["WRK-VOLIVA-ZION"],
    sources=[dict(label="Schadewald, The Plane Truth, ch. 8",
                  url="https://www.cantab.net/users/michael.behrend/ebooks/PlaneTruth/pages/Chapter_08.html")]),

"PER-SHENTON": _p(
    name="Samuel Shenton", dates="d. 1971", lineage="Zetetic",
    role="Founded the International Flat Earth Research Society, 20 December 1956.",
    sources=[dict(label="Schadewald, The Plane Truth, ch. 9",
                  url="https://www.cantab.net/users/michael.behrend/ebooks/PlaneTruth/pages/Chapter_09.html")]),

"PER-JOHNSON": _p(
    name="Charles Kenneth Johnson", dates="24 July 1924 – 19 March 2001",
    lineage="Zetetic", role="Added the conspiracy frame: astronomers are lying, not mistaken.",
    works=["WRK-JOHNSON-FEN"],
    sources=[dict(label="Wikipedia — Charles K. Johnson",
                  url="https://en.wikipedia.org/wiki/Charles_K._Johnson")]),

"PER-DUBAY": _p(
    name="Eric Dubay", dates="active 2015–", lineage="Zetetic",
    role="Compiler of 200 Proofs. Names his Victorian sources in 17 of 200 items.",
    works=["WRK-DUBAY-2015"],
    sources=[dict(label="flatearth.ws — rebuttals to Dubay's 200 Proofs",
                  url="https://flatearth.ws/eric-dubay")]),

"PER-SARGENT": _p(
    name="Mark Sargent", dates="active 2015–", lineage="Zetetic",
    role="The enclosed-world model: disc, ice wall, dome.",
    works=["WRK-SARGENT-2015"],
    sources=[dict(label="Wikipedia — Mark Sargent",
                  url="https://en.wikipedia.org/wiki/Mark_Sargent_(flat_Earth_proponent)")]),

"PER-SKIBA": _p(
    name="Rob Skiba", dates="active c. 2015–2021", lineage="Zetetic",
    role="Biblical-firmament cosmology; reissued Rowbotham and Carpenter under joint byline.",
    works=["WRK-SKIBA-2018"],
    sources=[dict(label="Testing the Globe — catalogue record",
                  url="https://books.google.com/books/about/Testing_the_Globe.html?id=7JU6vQEACAAJ")]),

"PER-KNODEL": _p(
    name="Bob Knodel", dates="active 2015–", lineage="Zetetic",
    role="Ring-laser gyroscope test; measured 15°/hour on camera.",
    works=["WRK-BTC-2018"],
    sources=[dict(label="Newsweek on Behind the Curve",
                  url="https://www.newsweek.com/behind-curve-netflix-ending-light-experiment-mark-sargent-documentary-movie-1343362")]),

"PER-BOUW": _p(
    name="Gerardus D. Bouw", dates="15 March 1945 – 4 November 2023",
    lineage="Tychonian",
    role="PhD astronomy, Case Western Reserve. Conceded observational equivalence.",
    works=["WRK-BOUW-1992"],
    sources=[dict(label="Wikipedia — Gerardus D. Bouw",
                  url="https://en.wikipedia.org/wiki/Gerardus_D._Bouw"),
             dict(label="Faulkner review, Journal of Creation",
                  url="https://creation.com/geocentric-gobbledegook")]),

"PER-SUNGENIS": _p(
    name="Robert Sungenis", dates="active 2006–", lineage="Tychonian",
    role="Galileo Was Wrong (with Robert Bennett); The Principle (with Rick DeLano).",
    works=["WRK-SUNGENIS-2006", "WRK-PRINCIPLE-2014"],
    sources=[dict(label="Galileo Was Wrong — full text, 2013 ed.",
                  url="https://archive.org/stream/GalileoWasWrongTheChurchSungenisRobertA.Bennett4276/Galileo%20Was%20Wrong_%20The%20Church%20%20-%20Sungenis,%20Robert%20A.%20&%20Bennett,_4276_djvu.txt"),
             dict(label="Krauss on The Principle, Slate, 8 April 2014",
                  url="https://slate.com/technology/2014/04/lawrence-krauss-on-ending-up-in-the-geocentrism-documentary-the-principle.html")]),

"PER-MARSHALLHALL": _p(
    name="Marshall Hall", dates="active 1991–", lineage="Tychonian",
    role="The Earth is not Moving (1991) — the populist/conspiracist wing.",
    sources=[dict(label="Faulkner, “Geocentric Gobbledegook”",
                  url="https://creation.com/geocentric-gobbledegook")]),

"PER-BLAVATSKY": _p(
    name="Helena Petrovna Blavatsky", dates="1831 – 1891", lineage="Esoteric",
    role="Theosophy. Popularised “as above, so below” alongside the Kybalion.",
    works=["WRK-BLAVATSKY-1877"],
    sources=[dict(label="Wikipedia — Helena Blavatsky",
                  url="https://en.wikipedia.org/wiki/Helena_Blavatsky")]),

"PER-HALL": _p(
    name="Manly P. Hall", dates="1901 – 1990", lineage="Esoteric",
    role="The Secret Teachings of All Ages (1928). Esoteric popularizer, self-described.",
    works=["WRK-HALL-1928"],
    sources=[dict(label="Wikipedia — Manly P. Hall",
                  url="https://en.wikipedia.org/wiki/Manly_P._Hall")]),

"PER-ATKINSON": _p(
    name="William Walker Atkinson", dates="1862 – 1932", lineage="Esoteric",
    role="Wrote The Kybalion as “Three Initiates”. New Thought, not Hermeticism.",
    works=["WRK-KYBALION-1908"],
    sources=[dict(label="Wikipedia — The Kybalion",
                  url="https://en.wikipedia.org/wiki/The_Kybalion")]),

"PER-ELIADE": _p(
    name="Mircea Eliade", dates="1907 – 1986", lineage="Esoteric",
    role="Historian of religion. Cited as cosmography; wrote about symbolism.",
    works=["WRK-ELIADE-1949"],
    sources=[dict(label="Britannica — Mircea Eliade",
                  url="https://www.britannica.com/biography/Mircea-Eliade"),
             dict(label="J. Z. Smith, To Take Place (1987)",
                  url="https://press.uchicago.edu/ucp/books/book/chicago/T/bo5951548.html")]),

"PER-PTOLEMY": _p(
    name="Claudius Ptolemy", dates="c. 100 – c. 170 CE", lineage="Pre-modern",
    role="Geocentric AND spherical. Cited by the list against its own flat half.",
    works=["WRK-PTOLEMY-ALMAGEST"],
    sources=[dict(label="Wikipedia — Almagest",
                  url="https://en.wikipedia.org/wiki/Almagest")]),
}
