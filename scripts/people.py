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
        "Two things, and the second is the fatal one. Neither is a case of never having "
        "looked. Both are cases of looking, and then setting the result aside. "
        "First, atmospheric refraction over water — which he underrated rather than "
        "overlooked. He reprints the <em>Encyclopædia Britannica</em> article on Levelling, "
        "which hands him the mechanism (“the unequal densities of the air at different "
        "distances from the earth”) and the coefficient (“at a mean … about one-seventh of "
        "the curvature of the earth”), and then substitutes an allowance of his own — "
        "“one-twelfth the altitude of the object observed” — which is the wrong variable, "
        "since refraction scales with the square of the distance and not with the height "
        "of the target. On Cape Bonavista that substitution deducts 13 feet where the "
        "encyclopaedia's own mean would take about 90, roughly seven times more. His "
        "General Index carries both “Experiments showing that refraction does not account "
        "for the elevation of objects seen at a distance of several miles” and “Refraction "
        "can only exist where the line of sight passes from one medium into another of "
        "different density” — and the second is contradicted by the article he had just "
        "typeset. The consequence is that he tested for curvature in the one configuration, "
        "a sightline a few inches above still water, where the effect he had cut by a "
        "factor of seven is largest. "
        "Second, and unanswerable: the southern sky. Circumpolar star trails rotating about "
        "a <em>southern</em> pole had been logged by European navigators for three centuries "
        "and were in every nautical almanac he could have opened. No single-plane model "
        "produces two opposite centres of rotation. He engaged it, and disqualified it. The "
        "3rd edition's General Index lists “Stars, north and south, motion of [284]” and "
        "“Southern Cross [287]”; under the heading “Motion of Stars North and South” he has "
        "every southern constellation, “pole star included,” sweeping “over a great southern "
        "arc and across the meridian” about the one northern centre, and treats the Southern "
        "Cross as a constellation that has simply not yet risen for observers further north. "
        "He quotes Sir James Clark Ross, Humboldt, and von Spix and von Martius on the "
        "latitudes at which they first sighted it, and then sets their testimony aside on the "
        "ground that observers “educated to believe that the earth is a globe … do not examine "
        "such matters critically.” What he passed over was not the observation. It was the "
        "observers: when the reading could only come out one way, the people holding the "
        "instrument stopped counting as witnesses."),
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
    lineage="Tychonian",
    role="Founder of modern geocentrism. Earliest documented user of the phrase "
         "“Airy's failure”.",
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
        "over Michelson–Gale–Pearson (1925), a positive detection of the Earth's rotation "
        "published in the <em>Astrophysical Journal</em>, which measures the very motion he "
        "denied: we do not find it treated anywhere in <em>De Labore Solis</em> (1988), the "
        "one work of his we hold. Stellar aberration he did <em>not</em> pass over — "
        "<em>De Labore Solis</em> is a book about it, working through Bradley and Molyneux "
        "at the chimney stack and resting the whole argument on the aberration angle. What "
        "he passed over is what aberration is evidence <em>of</em>. He kept Bradley's "
        "phenomenon and moved the motion — “then the starry sphere swings” — and that book "
        "does not account for why the swing should imitate the Earth's orbit so exactly. "
        "His own successor declined to follow him there: Bouw rebuilt the model to keep "
        "aberration."),
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
        "him. “Airy's failure” is not a term of art in physics: no use of it as a name for "
        "the 1871 water-telescope experiment has been found outside this movement, and the "
        "earliest documented occurrence is the subtitle of his own 1988 book. Bouw's "
        "obituary does not credit him with the coinage — it uses the phrase as settled "
        "vocabulary, credits his “pioneering work in pointing out the geocentric nature of "
        "Airy's failure,” and calls him “the father of modern geocentricity.” Sungenis "
        "inherits the term without attribution, writing that the experiment “was called” "
        "that, and adding the false gloss that it reflects “the thoughts of the "
        "experimenters during this era.” Airy's own paper is titled neutrally — “On a "
        "supposed alteration in the amount of astronomical aberration of light, produced by "
        "the passage of the light through a considerable thickness of refracting medium,” "
        "<em>Proceedings of the Royal Society of London</em> 20 (1871), pp. 35–39 — and the "
        "word “failure” is not located anywhere in it."),
    sources=[
        dict(label="De Labore Solis: Airy's Failure Reconsidered (1988)",
             url="https://geocentricity.com/bibastron/ts_history/de_labore.pdf"),
        dict(label="Bouw's obituary of van der Kamp, The Biblical Astronomer no. 84",
             url="https://www.geocentricity.com/ba1/no084/obits.pdf"),
        dict(label="Association for Biblical Astronomy — society history",
             url="https://www.geocentricity.com/bibastron/index.html"),
        dict(label="Michelson, Gale & Pearson 1925, ApJ 61:140 — original paper",
             url="https://paulba.no/paper/Michelson_Gale_II.pdf")]),

# ─────────────────────────────────────────────── researched (2026-08-11)
"PER-CARPENTER": _p(
    name="William Carpenter", dates="25 February 1830 – 1 September 1896",
    lineage="Zetetic",
    role=(
        "Originator of the numbered-proof-list format — the earliest such list identified, not "
        "provably the first. Carrier, not originator, of the arguments inside it: they are "
        "Rowbotham's, condensed."),
    works=["WRK-CARPENTER-1885"],
    bio_status="worked",
    formation=(
        "A Greenwich printer by trade and a Pitman shorthand man by avocation — a member of the "
        "Phonetic Society from 1848, later running a shorthand school in his own house and editing a "
        "magazine called <em>Shorthand</em> in 1893–94. Astronomy was his third enthusiasm, not his "
        "first. In September 1858 he launched <em>The Spiritual Messenger: A Magazine Devoted to "
        "Spiritualism, Mesmerism, and Other Branches of Psychological Science</em>, held séances at "
        "his house in Greenwich, took down spirit discourses in shorthand, and folded the magazine in "
        "March 1859 after losing two children that winter. He was converted at a Rowbotham lecture in "
        "1861, and published an eight-page pamphlet mostly in verse, <em>Earth Not a Globe</em>, as "
        "“Common Sense” in 1864 — a year before Rowbotham's book of nearly that title. Eight "
        "sixteen-page installments of <em>Theoretical Astronomy Examined and Exposed</em> followed in "
        "1865–66, bound afterwards as a 128-page book dedicated to “Parallax.” In March 1870 he was "
        "John Hampden's appointed referee at the Old Bedford Canal against Alfred Russel Wallace. In "
        "1879, aged 49, he shipped his wife and six children to America, settled in Baltimore early "
        "in 1880, and set up as a printer; <em>One Hundred Proofs that the Earth Is Not a Globe</em> "
        "was printed and published by him at 71 Chew Street in 1885. He died on 1 September 1896 "
        "after a series of strokes; his wife Annie died nine weeks later. Two facts about the "
        "formation carry the whole biography. He was trained to set type and to take down speech "
        "exactly — and both trades are visible in what he made. The hundred proofs are a printer's "
        "object before they are an argument: one paragraph each, an index of one-line titles at the "
        "front, twenty-five cents, five copies postpaid for a dollar. And the best documentary record "
        "the movement produced of the 1870 canal week is his own shorthand of it. He was not, at any "
        "point, an observer with an instrument of his own. He was the man who wrote down what "
        "happened and then set it in type."),
    had=(
        "More than the format alone, and the fair account has to start with the week at the canal. He "
        "was there for all of it, which is more direct instrumental experience of the decisive "
        "experiment than almost anyone downstream of him has ever had. His procedural objections on "
        "the first attempt were <em>correct</em>: the distances had been paced rather than chained, "
        "at least one signal had been knocked down and reset at the wrong height, and Wallace's "
        "borrowed astronomical telescope could not be levelled and carried no cross-hairs. Carpenter "
        "said so, insisted that valid observations required a surveyor's level, and Wallace went to "
        "King's Lynn on the Thursday and borrowed a Troughton's level to satisfy him. The experiment "
        "that settled the wager was a better experiment because Carpenter objected to the first one. "
        "His shorthand is the other real asset. Schadewald, reconstructing the week more than a "
        "century later, works largely from Carpenter's own 1871 account of it, calling it “the first "
        "really detailed description of the Bedford Canal experiment.” The verbatim exchanges on the "
        "barge survive because a professional stenographer happened to be standing on it. Beyond the "
        "canal he had Rowbotham's corpus and Rowbotham himself — the introduction to the 1885 "
        "pamphlet is a memorial to a man he had spent “many a pleasant hour” with — and he worked "
        "from named, citable printed books rather than assertion, which is the reason his claims can "
        "be checked at all. (The quotations he takes from Proctor and Herschel were not independently "
        "collated against those authors in this pass.) One more thing belongs here, because the "
        "record is otherwise unfair to him. He printed his opponents. The appendices to the third, "
        "fourth and fifth editions carry Richard Proctor's polite reply of 12 December 1885 with its "
        "sting intact — that the pamphlet “might more precisely be called ‘One hundred difficulties "
        "for young students of astronomy’” — Spencer Baird's brush-off from the Smithsonian, and page "
        "after page of hostile press verbatim, including the <em>Florida Times Union</em> calling his "
        "motto “an upright lie, a downright invention,” and the <em>New York Herald</em>'s line that "
        "he “succeeds only in showing that he is himself one.” He advertised for a paid reviewer to "
        "demolish the book, on one condition: sign your name to it. That is not the behaviour of a "
        "man hiding from criticism, and the page should say so before it says anything else."),
    ignored=(
        "One thing, and he was holding it. On Saturday 5 March 1870, at Welney Bridge, three targets "
        "were set at the same height above the water — a banner on Old Bedford Bridge at 13 ft 4 in, "
        "a disc on the mid-point signal at 13 ft 4 in, and the optical axis of the levelled "
        "Troughton's level on the parapet. Carpenter fetched the level from the carriage himself, "
        "helped set it up, looked through it and, in Schadewald's phrase, “actually jumped for joy.” "
        "His written report to the umpire says what he saw: the stations appeared “equi-distant in "
        "the field of view, and also in a regular series: first, the distant bridge; secondly, the "
        "central signal; and, thirdly, the horizontal cross-hair” — from which he concluded that “a "
        "straight line from one point to the other passes through the central point in its course, "
        "and that a curved surface of water has not been demonstrated.” That is the measurement, and "
        "it is a measurement of the curvature. On a plane, three marks at the same height as a "
        "levelled sightline coincide with the cross-hair; they do not step away from it. On a sphere "
        "the drop below the horizontal grows as the square of the distance, so the <em>angle</em> "
        "below the sightline grows in simple proportion to it — about 6 ft at 3 miles and 24 ft at 6 "
        "miles by his own 8-inches-per-mile-squared arithmetic, which is 1.3 and 2.6 arcminutes, a "
        "regular series in exactly equal steps. Equal spacing is the signature of the sphere. "
        "Coincidence would have been the signature of the plane. He recorded the right numbers, drew "
        "them accurately enough that Coulcher countersigned, and read them backwards. Then he did "
        "something harder to defend than the misreading: his schedule of thirteen objections to Walsh "
        "argued that the markers' appearance below the cross-hair should be discounted because a "
        "surveyor's ordinary level cannot be expected to be truly level — after a week of insisting "
        "that nothing else would do. Walsh, publishing his decision in <em>The Field</em> of 26 March "
        "1870, added that Carpenter had told him the flat opinion rested on theory alone and had "
        "never been tried, while a treatise by “Parallax” bearing Carpenter's own name on the title "
        "page described the same experiment on the same water; he called him “a most improper person "
        "to be selected to act as referee.” Fifteen years later the pamphlet tells its readers that "
        "Wallace “took up six miles in his experiment, and was unable to prove that there is any "
        "‘curvature,’ though he claimed the money and got it.” Two smaller gaps, named as gaps rather "
        "than refusals. Refraction: the string “refract” does not occur anywhere in the "
        "143,011-character Project Gutenberg text of the fifth edition (#55387), searched in full — "
        "the mechanism Rowbotham had reprinted from the <em>Encyclopædia Britannica</em> upstream of "
        "him is simply not in the list. And the southern sky: six proofs concern the south (11, 14, "
        "16, 52, 53, 78) and all six are about distances, ice and the sun's speed; “circumpolar” "
        "occurs zero times, and no proof addresses the rotation of the southern sky about a southern "
        "pole. His two Polaris proofs (71, 84) show he was thinking hard about how the sky changes "
        "with latitude. He answered the northern half of that question. Scope note: these absences "
        "are stated of the fifth-edition text only. His <em>Water, Not Convex</em> (1871) and "
        "<em>Wallace's Wonderful Water</em> (1875) were not reached in this pass and may treat both "
        "subjects."),
    legacy=(
        "What descends from him is the container, not the contents. In this dataset he holds 17 of "
        "the 461 items and two arguments — B05, engineering makes no curvature allowance (12 items), "
        "and C01, proof-texts on an immovable Earth (5) — a deliberately small number, and the small "
        "number is the finding. Carried forward, documented: proofs 3, 40, 41 and 51 are the ancestor "
        "of the whole modern engineering-allowance cluster, whose twelve items are pipelines, "
        "wind-farm layouts, microwave Fresnel zones, undersea cables and aerial refuelling — new "
        "examples fitted to Victorian frames; proof 3 reappears as Dubay's 7 and proof 40 (Suez) as "
        "Dubay's 8; proof 4, the Nile which “in a thousand miles, falls but a foot,” is the earliest "
        "text located for the river-grades item and passes near-verbatim into Dubay's 5, an "
        "attribution this project corrected onto him in August 2026 after having credited Rowbotham "
        "for it. Dubay names him at proofs 96 and 129. The reprint chain is physical: Voliva reissued "
        "the hundred proofs under his own Zion, Illinois imprint in 1929, a St Petersburg, Florida "
        "reprint followed in 1955, and Skiba's <em>Testing the Globe</em> (2018) is catalogued with "
        "Rowbotham and Carpenter as co-authors — the movement reissuing a man 122 years dead under "
        "joint byline. What does <em>not</em> descend from him, and the record has had to say so "
        "twice: the sun-motion proof-texts were taken off him in August 2026 when the full text "
        "showed his pamphlet contains exactly one scriptural proof and never mentions Joshua, "
        "Habakkuk or Ecclesiastes, and that corpus traces instead to Bellarmine in 1615; C01 keeps "
        "him only for proof 50, and the four chapter-and-verse citations those items give are not in "
        "the text we hold. Merely resembling rather than descending: the numbered list of proofs is a "
        "form he cannot be shown to have invented. It is verified that no numbered proof-list stands "
        "in Rowbotham's 1865 or 1881 texts. It is not verified that none stands in Carpenter's own "
        "earlier works — <em>Theoretical Astronomy Examined and Exposed</em> (1865–66), <em>Water, "
        "Not Convex</em> (1871), <em>Wallace's Wonderful Water</em> (1875) — none of which is held by "
        "the Internet Archive under his name, all of which returned a Cloudflare block at HathiTrust "
        "and metadata only at Google Books during this pass. “Earliest numbered proof-list "
        "identified” is what the evidence supports, and the test suite is right to guard the stronger "
        "claim. One correction to our own genealogy. The clean line that the Victorians thought "
        "astronomers mistaken while Johnson later said they were lying does not hold for Carpenter "
        "without qualification. He calls Wallace's claim false and his acceptance of the money a "
        "thing he “dared” to do, calls the <em>New York Herald</em>'s quotations “fraudulent,” calls "
        "the mathematicians of the world “cowards” for not reviewing him, and Schadewald reads his "
        "1865–66 work as holding that a general understanding of a flat earth had been perverted "
        "through fraud. What Charles K. Johnson adds in 1972 is the institution — NASA, Hollywood, a "
        "script by Arthur C. Clarke — not the imputation of bad faith, which is already here."),
    kernel=dict(
        description=(
            "Two true things, one small and sharp, one structural. Proof 41 is the sharp one, and it "
            "is worth stating at full strength: astronomers and surveyors say that a curved surface "
            "is the <em>true level</em>, and they also say that canal engineers must make an "
            "<em>allowance for curvature</em>. Carpenter's objection is that these cannot both be "
            "operative in the same sense — if the level surface is already the curved one, then "
            "asking a builder to allow for curvature is asking him to depart from the surface he is "
            "building to. That is a real equivocation in the popular astronomy of the 1880s, caught "
            "in a single paragraph by a man with no training, and it is the same catch Rowbotham had "
            "half-made by reprinting the <em>Britannica</em> article that defines <em>level</em> as "
            "curved. The structural one is the format. Rowbotham's book is 50,000 words in fourteen "
            "wildly uneven sections; Carpenter turned it into a hundred one-paragraph claims with an "
            "index of one-line titles at the front, each traceable to a named book. Whatever else "
            "that is, it is more checkable than what it replaced — it is the reason a modern list can "
            "be traced back to him at all, and it is the reason this review exists in the form it "
            "does."),
        why_it_doesnt_save_claim=(
                "Where it points is the problem. The equivocation dissolves the moment “level” is "
                "read as what every levelling instrument physically implements — a surface of "
                "constant gravitational potential, which a bubble and a plumb line track because they "
                "respond to gravity and nothing else — and on a rotating spheroid that surface is "
                "curved. Free water settles onto it by itself, which is why the Suez Canal has no "
                "locks and why Carpenter's own observation about it is true and neutral. And the "
                "format defeats the list it founded. If each numbered item is an independent witness, "
                "then counting them measures something; but his hundred compress to roughly five of "
                "Rowbotham's arguments, exactly as the specimen's 461 compress to 98 and to nineteen "
                "people. Enumeration was never evidence, and Carpenter is the proof of it: the one "
                "occasion on which a single decisive measurement was placed in front of him, the "
                "virtue of his format — a hundred small independent claims — was no help at all. What "
                "was needed was the opposite skill, weighing one observation properly, and it is the "
                "skill his hundred proofs are designed not to require.")),
    sources=[
        dict(label=(
                "Carpenter, One Hundred Proofs that the Earth Is Not a Globe (Baltimore, title page "
                "1885; text held is the 5th edition, appendix closing 9 November 1886) — full text"),
             url="https://www.gutenberg.org/ebooks/55387"),
        dict(label=(
                "One hundred proofs that the earth is not a globe — Internet Archive scan, catalogued "
                "1886"),
             url="https://archive.org/details/onehundredproofs00carp"),
        dict(label=(
                "Schadewald, The Plane Truth, ch. 2 — 'Hampden and the Old Bedford Canal' (the March "
                "1870 week, and Carpenter's report to the umpire)"),
             url="https://www.cantab.net/users/michael.behrend/ebooks/PlaneTruth/pages/Chapter_02.html"),
        dict(label=(
                "Schadewald, The Plane Truth, ch. 1 — Carpenter's spiritualist period, the 1864 verse "
                "pamphlet, and Theoretical Astronomy Examined and Exposed"),
             url="https://www.cantab.net/users/michael.behrend/ebooks/PlaneTruth/pages/Chapter_01.html"),
        dict(label=(
                "Schadewald, The Plane Truth, ch. 5 — 'Carpenter and the American Flat-Earth "
                "Movement' (Baltimore, Johns Hopkins, the reprints, his death)"),
             url="https://www.cantab.net/users/michael.behrend/ebooks/PlaneTruth/pages/Chapter_05.html"),
        dict(label="Wikipedia — William Carpenter (flat-Earth theorist)",
             url="https://en.wikipedia.org/wiki/William_Carpenter_(flat-Earth_theorist)"),
        dict(label="Library of Congress — The Flat Earth and its Advocates",
             url="https://guides.loc.gov/flat-earth/books"),
        dict(label=(
                "Rowbotham, Earth Not a Globe (1865) — full text, checked for the absence of any "
                "numbered proof-list"),
             url="https://www.gutenberg.org/ebooks/69892")]),

"PER-WINSHIP": _p(
    name="Thomas Winship", dates="September 1860 – 30 July 1942",
    lineage="Zetetic",
    role=(
        "Wrote as “Rectangle” from Durban, Natal — the movement's only southern-hemisphere field "
        "investigator. Carrier of Rowbotham and Carpenter; originator, as far as located, of the "
        "sextant derivation behind item 31."),
    works=["WRK-WINSHIP-1899"],
    bio_status="worked",
    formation=(
        "An accountant in Durban, in the Colony of Natal — numerate by trade, not a scientist, and "
        "the only figure in this dataset who wrote from the southern hemisphere. Born at "
        "Newcastle-on-Tyne in September 1860, he emigrated to South Africa at 21, went first to Cape "
        "Town, and settled in Durban with his family in 1897; he was known in the town's yachting "
        "circles and was once wrecked in his own yacht off Port Shepstone, a Durban tug going out to "
        "fetch him. (These facts are Schadewald's, sourced by him to the obituary in the <em>Durban "
        "Daily News</em> of 31 July 1942 — a newspaper obituary we have not seen, reported in an "
        "unfinished manuscript published posthumously on a private website, not in peer-reviewed "
        "scholarship.) His method is second-hand and he does not hide it: the preface to the first "
        "edition states it in Rowbotham's own vocabulary — “The Zetetic process is to go upon enquiry "
        "only; to search out; to examine by testing the evidence,” against theory, which “accepts "
        "without proof” and “learns on credit and believes on trust.” What is his own is the setting. "
        "He did not have a canal; he had a working colonial port, a shipping press, and ships' "
        "officers who would hand him their logs. The first edition — a 46-page pamphlet, its preface "
        "signed “T.W.,” P.O. Box 347, Durban, Natal, December 1897 — came out in the year he settled "
        "there; the enlarged second edition of 192 pages, arranged alphabetically for reference and "
        "priced 2s. 6d., was written from 12 Castle Buildings, Durban, and its preface is dated "
        "November 1899."),
    had=(
        "More primary data than anyone else on this page, and he went and got it himself. He obtained "
        "the log of the S.S. <em>Withsdale</em> of Glasgow, Hamelin Bay to Port Natal, 8 January to 1 "
        "February 1898, 4,519 nautical miles, from her chief officer Mr Boyle, “also a passed "
        "Master,” and worked the arithmetic out of it. He took lighthouse visibility figures from the "
        "<em>Argus Annual</em> for 1894 and the <em>Natal Mercury</em>, and checked them against the "
        "Bluff light he could see from his own harbour. He made dated naked-eye observations of the "
        "Moon from Durban and printed the rise times against sunrise — 30 August 1898, moonrise 1.07 "
        "a.m., sunrise 6.35 — which is a real observing programme, however he read it. He interviewed "
        "the most famous solo navigator alive: “In December, 1897, I met Captain Slocum on board the "
        "<em>Spray</em>.” He challenged an opponent writing as “Ancient Mariner” to settle the matter "
        "by experiment on the water of Table Bay, and reported that he was still waiting for an "
        "acceptance. He argued it out in the Natal newspapers and wrote warmly about their "
        "willingness to print him. His figures are his own and, granted his premises, competently "
        "done: his three published “circumference” results reproduce to within a few per cent when "
        "recomputed from the data he prints. And his central navigational claim was true as stated in "
        "1899 — ships were in practice worked by plane sailing and dead reckoning, and the textbook "
        "he quotes says so in the sentence he quotes. He also had, as no other zetetic author did, "
        "the sky over Durban: the south celestial pole stands 29°53′ above his southern horizon."),
    ignored=(
        "Two things, and both were in his hands rather than out of reach. <strong>First, the southern "
        "sky — he printed the objection and answered half of it.</strong> He quotes S. Laing on da "
        "Gama's ships running south: the Pole Star's elevation fell away, and “other stars, some of "
        "them forming magnificent constellations, had come into view—the stars of the Southern "
        "hemisphere.” His reply is a row of street lamps down a flat mile, receding until the last is "
        "“apparently quite on the ground,” with the note that “the writer has tried the street lamp "
        "many times with the same result” (2nd ed., printed pp. 34–35). That answers the sinking of "
        "the Pole Star. It does not touch the second clause of the sentence he had just set in type — "
        "and that clause is the one he alone could have tested from where he stood, because every "
        "star within 29°53′ of the south celestial pole circles it above Durban without ever setting. "
        "In the 488,000-character OCR of the second edition (archive.org "
        "<em>zeteticcosmogony00unse</em>) we searched for “Southern Cross,” “circumpolar,” “Crux,” "
        "“Canopus,” “Centaur,” “celestial pole,” “Polaris” and “pole star”: the southern stars occur "
        "once, inside the quotation he is rebutting. Not located there — that is a claim about that "
        "scan and those strings, not about every page he ever wrote. Nor was the question dormant: "
        "<em>Earth Review</em>, which he quotes throughout the book, had been fighting about it since "
        "April 1893, when its New Zealand correspondents reported that the Southern Cross stands "
        "inverted between its lowest and highest positions and the editor filed the report as "
        "“hearsay evidence.” <strong>Second, and worse, the midnight sun — where he scopes his "
        "negative correctly and then over-draws it.</strong> He asks “how is it that the midnight sun "
        "is never seen in the south during the southern summer,” names Cook to 71°, Weddell to 74° "
        "and “Sir James C. Ross in 1841 and 1842” to the 78th parallel, and adds, properly, “I am not "
        "aware that any of these navigators have left it on record that the sun was seen at midnight "
        "in the south” — then concludes, from that, “that there is no midnight sun in the south” "
        "(printed pp. 63–64). The record was in a book he had open. He quotes Ross twice for currents "
        "and dead reckoning, and one of those quotations — “By our observations at noon we found "
        "ourselves fifty-eight miles to the eastward of our reckoning” — sits in vol. I of Ross's "
        "<em>Voyage of Discovery and Research in the Southern and Antarctic Regions</em> under 26 "
        "July. The same volume, at 22 January 1841 near 74° S: “At midnight, when the sun was "
        "skimming along the southern horizon at an altitude of about two degrees, the sky over head "
        "was remarked to be of a most intense indigo blue.” And at his furthest south Ross fixes the "
        "record latitude by “an observation of the sun at 28 minutes after midnight, which gave the "
        "latitude 77° 56′ S.” A sun sight taken after midnight, by the navigator Winship names, in "
        "the volume Winship mines, with the instrument Winship trusted above every other. His "
        "fallback is an argument from silence in a summary pamphlet: the Belgian Antarctic "
        "expedition's paper records the sun's disappearance from 17 May to 21 July, and since “there "
        "is not one word in the pamphlet about the matter” of a midnight sun, he concludes there was "
        "none. At the latitude he himself quotes, 71°36′ S, the sun stands about 5° above the horizon "
        "at local midnight at the December solstice (|φ| + δ − 90 = 71.6 + 23.44 − 90) and does not "
        "set at all from roughly 20 November to 22 January. A smaller instance of the same habit, and "
        "to his credit he seems to have dropped it: the first edition contrasts southern twilight "
        "with northern — “In northern latitudes the writer has read a book until ten o'clock at night "
        "by twilight alone. Let anyone try this in Natal, which is only 30 degrees south” (1897, "
        "printed p. 36) — which compares 30° in one hemisphere with about 53° in the other. Twilight "
        "length depends on latitude and solar declination and is symmetric between the hemispheres at "
        "equal latitude and opposite season; the control he needed was 30° North. We did not locate "
        "the claim in the 1899 text (searched “twilight”)."),
    legacy=(
        "Small, specific, and it is not the part of him worth reading. Two of his lines survive into "
        "the 461-item specimen. The sextant derivation is the load-bearing one: one minute of arc "
        "read on the instrument taken as one nautical mile, applied to the sky, giving “about 32 "
        "nautical miles in diameter” for the Moon on printed p. 71 and 32 for the Sun on p. 120 — "
        "which is where item 31, “Equal apparent size of Sun and Moon,” gets whatever teeth it has. "
        "That equality is not observed at the end of the procedure; it is fixed at the start, because "
        "the conversion places everything it touches at one Earth radius. It travels by a visible "
        "route and then an invisible one: David Wardlaw Scott quotes the sun passage in <em>Terra "
        "Firma</em> (1901), printed pp. 173–174, crediting “Zetetic Cosmogony” p. 120; Dubay's "
        "<em>200 Proofs</em> then carries the 32-mile figure at #123 and the “measured with sextants "
        "to be of equal size and equal distance” claim at #147, crediting neither to him. Batch-11 "
        "research on B10 did not locate the equal-size argument in Rowbotham's 1865 text, so on the "
        "searches run so far Winship — not Rowbotham, who currently holds the cluster record — is the "
        "located ancestor of item 31. His second survivor is a flat assertion in his own voice at "
        "printed p. 130: “At Port Natal the rise and fall is about six feet, while at Beira, about "
        "600 miles up the coast, the rise and fall is 26 feet. This effectually settles the matter "
        "that the moon has no influence on the tides.” That reaches Dubay's proof 118 and stands "
        "behind item 252. Dubay names him once in 200 proofs, at #31, for the Blue Hill Observatory "
        "kite clipping he took from the <em>American Exporter</em> of November 1897. And per "
        "Schadewald, British flat-earthism in its 1890s flowering “produced not a single book. "
        "Winship remedied that by producing two” — so the movement's book of that decade is a "
        "colonial one. What did <em>not</em> descend is the striking part. Searching the 461-item "
        "corpus for “circumnav,” “plane sailing,” “great circle,” “Slocum,” “midnight,” “twilight,” "
        "“Antarctic” and “southern” returns nothing of his: the <em>Withsdale</em>'s log, the "
        "<em>Challenger</em>'s distances, the Slocum interview, the Table Bay challenge, the whole "
        "circumference argument he built out of documents he collected himself, are absent from this "
        "list. The two things that travelled are the two one-line assertions. That is a finding about "
        "this specimen and how it was assembled, not a general law about the literature."),
    kernel=dict(
        description=(
            "Two true things, and the second is better than the movement usually manages. First, he "
            "actually did what the zetetic method says to do. Where Rowbotham had one canal and "
            "Carpenter had a printing press, Winship had a port, and he used it: ships' logs obtained "
            "from the officers who kept them, lighthouse tables from the local annual and the "
            "<em>Natal Mercury</em>, dated observations of his own, an interview with a "
            "circumnavigator, and a standing public offer to settle the question by experiment on "
            "Table Bay. He is the only person on this page who systematically collected primary "
            "documents from working professionals and did the arithmetic himself; recomputing his "
            "three “circumference” results from the data he prints reproduces his published answers "
            "to within a few per cent, so the sums are honest. Second, his navigational premise was "
            "true as stated in 1899: ships were in practice worked by plane sailing and dead "
            "reckoning, and the textbook he quotes concedes it in his favour — “although in practice "
            "scarcely any other rules are used but those derived from plane sailing.”"),
        why_it_doesnt_save_claim=(
                "Because the strongest form of his argument is a claim about how far an approximation "
                "can be pushed, and every source he quotes states the limit inside the sentence he "
                "quotes. Evers, in the passage he reprints: “It is not a strictly correct supposition "
                "to take any part whatever of the earth's surface as a plane; <em>yet</em> when the "
                "vessel goes on short voyages, the results obtained by plane sailing will be "
                "sufficiently correct to serve every useful purpose.” He reads a specification as a "
                "concession. And the circumference argument — his most original construction — fails "
                "at a step his own page admits. He converts a steaming distance into a circumference "
                "by treating the track as an arc of a parallel of latitude and scaling it by 360°/Δλ. "
                "Ships do not sail parallels. They sail near-geodesics when they can and detours when "
                "they must, and his method silently converts every excess mile into extra world. "
                "Recomputed here: the great-circle distances for his three cases are about 4,158, "
                "5,581 and 1,202 nautical miles, against the 4,519, 7,637 and 1,432 he uses. Of the "
                "first he notes himself that she “did not make quite a rhomb line track,” and then "
                "adds 100 miles to force her onto one. The second is the clearest: H.M.S. "
                "<em>Challenger</em>'s run from the Cape to Melbourne was a survey cruise that called "
                "at the Prince Edward Islands, the Crozets, Kerguelen and Heard Island and spent "
                "February 1874 working among pack ice near the Antarctic Circle. He treats it as a "
                "straight passage along the 35½° parallel and gets a world over 25,000 statute miles "
                "round at that latitude. The data were real and honestly obtained; the reasoning "
                "needed a ship that sailed in a straight line, and the logs he had collected were the "
                "evidence that none of them did.")),
    sources=[
        dict(label="Winship [“Rectangle”], Zetetic Cosmogony, 2nd ed. enl. (Durban",
             url="https://archive.org/details/zeteticcosmogony00unse",
             note="T. L. Cullingworth, 1899) — full OCR text of the book of record"),
        dict(label=(
                "Winship, Zetetic Cosmogony, 1st ed. [1897], 46 pp., Boston Public Library copy — "
                "preface signed “T.W.”, Durban, December 1897"),
             url="https://archive.org/details/zeteticcosmogony00wins"),
        dict(label=(
                "HathiTrust catalogue record for the 1899 second edition (NYPL copy), collated iv + "
                "192 pp."),
             url="https://catalog.hathitrust.org/Record/008629354"),
        dict(label=(
                "Schadewald, The Plane Truth, ch. 6 “Elsewhere Across the Plane” — Winship's "
                "biography, the Slocum encounters, and the Earth Review dispute over the southern "
                "stars"),
             url="https://www.cantab.net/users/michael.behrend/ebooks/PlaneTruth/pages/Chapter_06.html"),
        dict(label=(
                "Slocum, Sailing Alone Around the World (1900) — the Durban flat-earth visitors and "
                "Kruger"),
             url="https://www.gutenberg.org/ebooks/6317"),
        dict(label=(
                "Ross, A Voyage of Discovery and Research in the Southern and Antarctic Regions, vol. "
                "I (1847) — midnight sun at ~74°S on 22 January 1841, and the sun sight taken 28 "
                "minutes after midnight at 77°56′S"),
             url="https://archive.org/details/voyageofdiscover01ross"),
        dict(label="Challenger expedition route, Cape Town to Melbourne 1873–74",
             url="https://en.wikipedia.org/wiki/Challenger_expedition",
             note=(
                "Prince Edward Islands, Crozets, Kerguelen, Heard Island, and February 1874 near the "
                "Antarctic Circle")),
        dict(label="Library of Congress — The Flat Earth and its Advocates",
             url="https://guides.loc.gov/flat-earth/books",
             note="books list")]),

"PER-VOLIVA": _p(
    name="Wilbur Glenn Voliva", dates="10 March 1870 – 11 October 1942",
    lineage="Zetetic",
    role=(
        "Carrier, not originator. Built the movement's only institution — Zion's required curriculum, "
        "its pulpit and a 5,000-watt station — and wrote no flat-earth book of his own."),
    works=["WRK-VOLIVA-ZION"],
    bio_status="worked",
    formation=(
        "Born on a farm near Newtown, Fountain County, Indiana, on 10 March 1870, to James H. Voliva, "
        "a Methodist lawyer, and his wife Rebecca, a former Presbyterian. He joined the “New Light” "
        "Christian Church at fourteen and was ordained at nineteen; over the next decade he attended "
        "four Bible colleges or seminaries, pastored six churches, and moved to the Disciples of "
        "Christ. By 1898 he had concluded the ministry was hypocrisy and was considering law school. "
        "What redirected him was a magazine: he read an issue of <em>Leaves of Healing</em>, went to "
        "Chicago to hear John Alexander Dowie, and joined the Christian Catholic Apostolic Church on "
        "22 February 1899. Elder in April, Cincinnati within the year, Overseer on 4 August 1901, "
        "then four years running the Australian mission from Melbourne with branches in Sydney and "
        "Adelaide. Recalled by telegram at the end of 1905, he found Zion City bankrupt, displaced "
        "Dowie, bought the town back out of receivership piece by piece, and by 1910 held the titles "
        "in his own name. <strong>Nothing in that path is scientific, and nothing in it is "
        "zetetic.</strong> He arrived at Zion as an administrator of a church, and the cosmology "
        "followed the office rather than preceding it.<br><br>The flat Earth arrives late, and not "
        "from an experiment. His first public attack on astronomy was a sermon at Shiloh Tabernacle "
        "on 16 August 1914 — mostly the usual against doctors and druggists, with astronomy added, "
        "and it never says the Earth is flat. Its one cosmological argument is a question about the "
        "Ascension: if the world is “whirling around in space,” then “how is the Lord going to light "
        "on it?” The doctrine is in plain English by 26 December 1915 — “I believe this earth is a "
        "stationary plane; that it rests upon water,” and “Neither do I believe there is any such "
        "thing as the law of gravitation: I believe that that is a lot of rot, too.” On his own "
        "account the route was textual, not observational: <em>I get my astronomy from the "
        "Bible.</em> That is his stated reason and it is the only one this page asserts. Schadewald, "
        "who tried to date the conversion, writes that it is not clear how or when it happened, and "
        "allows that Voliva may have reached the position independently of the zetetic tradition — "
        "but by the sermon of 3 February 1916 the borrowing is visible. There Voliva tells his "
        "congregation that “the foremost writers” concede the stationary-plane position explains the "
        "phenomena as well as their own. That is a paraphrase of the Robert Woodhouse quotation "
        "printed in Lady Blount's <em>Earth Review</em> under the heading “Honest and Noble "
        "Confessions” — a passage Schadewald notes was given <em>without a source</em> and was then "
        "recycled through flat-earth literature for decades. Within eighteen months of his first "
        "sermon, Voliva had found the library. He spent the next twenty-six years distributing it."),
    had=(
        "More than a pulpit, and — the part usually left out — an actual attempt at measurement. The "
        "Zion cosmology carried numbers, and they were derived rather than announced. The Sun's "
        "diameter, 32 miles, was computed from the width of the zone in equatorial regions in which a "
        "vertical pole casts no shadow. Its height, about 3,000 miles, was computed from two noon "
        "observations at equinox: the Sun 45° above the horizon in Maine, directly overhead in "
        "southern Colombia, roughly 3,000 miles apart, so on a plane the lamp sits 3,000 miles up. "
        "<strong>That is Eratosthenes' instrument run on the other premise.</strong> It is arithmetic "
        "from field data, it is falsifiable, and it is a better class of thing than the bare "
        "assertions that make up most of the specimen list. He also had the whole existing zetetic "
        "corpus — Rowbotham, Blount's <em>Earth Review</em>, and Alexander Gleason's 1892 azimuthal "
        "map, which he held up for a newspaper photographer in 1922 and put on the cover of his 1930 "
        "special issue.<br><br>And he engaged the standard case rather than refusing to hear it. The "
        "10 May 1930 issue of <em>Leaves of Healing</em> runs 64 pages and about 75,000 words, and "
        "two of its six articles are Chester M. Shippey answering the ordinary proofs of sphericity "
        "one at a time: ships vanishing hull-first, where the edge is, how there can be night, how "
        "far the Sun is, how eclipses are predicted. The answers are stock zetetic answers, but they "
        "are answers to the actual objections, printed in full alongside them. Whatever else is wrong "
        "here, it is not incuriosity.<br><br>What he had above all was reach, and this is his real "
        "contribution. WCBD, 5,000 watts from 1923, was — on the National Center for Science "
        "Education's account — the first radio station owned by an evangelist, and its signal carried "
        "to Australia. A church magazine went to foreign missions. A school system taught the "
        "doctrine as curriculum. No previous flat-earther had anything remotely like it."),
    ignored=(
        "Begin with what he did <em>not</em> pass over, because it matters to the fairness of the "
        "rest: he printed the objections. The failing is not a refusal to hear the other side; it is "
        "what happened after hearing it.<br><br><strong>First, the third station.</strong> The "
        "3,000-mile Sun rests on exactly two observations, and two observations cannot decide this. A "
        "near lamp over a plane and a distant Sun over a globe fit any <em>pair</em> of noon "
        "altitudes identically — that is why Eratosthenes needed a premise as well as a measurement. "
        "A third latitude separates them: on the globe the implied geometry stays consistent, on the "
        "plane the implied lamp height comes out different for every pair you choose. Noon altitudes "
        "for any latitude on any date were in every almanac in Zion. And the movement's own "
        "arithmetic had already delivered the third station uninvited. Voliva's Zion put the Sun "
        "3,000 miles up; W. E. Goudey in Boston, working Gleason's own Ottawa-and-South-America "
        "example, got 2,700 nautical miles; Gleason himself published 1,725. Three computations of "
        "one quantity by one method, three answers, all in print in works Voliva knew. Not located in "
        "Schadewald's chapter 8, which is our record's cited source for Zion: any Zion publication "
        "reconciling them. The 10 May 1930 issue itself was not consulted.<br><br><strong>Second, the "
        "southern hemisphere, which he had personally administered.</strong> He lived in Melbourne "
        "for four years, with branches in Sydney and Adelaide and missions in New Zealand; the "
        "church's largest overseas mission was in South Africa. On the Gleason disc he posed with, "
        "everything south of the equator is smeared around an ever-widening rim, and Melbourne–Cape "
        "Town, Sydney–Santiago and the Antarctic circumnavigations come out far longer than the "
        "sailing schedules his own church booked passage against. Schadewald, writing of Goudey "
        "citing Gleason to prove southern distances work out: “Actually, they don't work out on the "
        "zetetic scale.” Voliva had spent four years standing under a sky whose stars turn about a "
        "southern pole, and had the correspondence of a southern-hemisphere church organisation on "
        "his desk. Not located in Schadewald's chapter 8: any Zion treatment of southern distances or "
        "of the southern circumpolar sky.<br><br><strong>Third, and this is the one that defines him: "
        "the $5,000.</strong> The standing offer was to anyone who could prove <em>to him</em> that "
        "the Earth is a globe, and “nobody ever collected.” A prize whose claimant-in-chief is also "
        "the judge is not a test, and Voliva's own report of it in 1930 is a report on the claimants "
        "rather than the claims — the letters, he wrote, betrayed “an appalling ignorance of the "
        "whole subject.” The comparison is inside the movement's own history and it is exact: when "
        "John Hampden's 1870 Bedford Level wager was put to a named referee, the referee found for "
        "Wallace. Voliva's version kept the money and removed the referee. Two of the specimen list's "
        "own conventions descend from that shape. (Our record notes that the offer is well attested "
        "but its start date is not established; that limitation stands.)<br><br><strong>Fourth, the "
        "institutional move.</strong> From 1916 the doctrine was curriculum: teachers in Zion's "
        "parochial schools were, in Schadewald's words, “required to teach students that the earth is "
        "flat,” and the Theocratic Party controlled the public school board as well. A claim taught "
        "to children under employment conditions is a claim removed from the class of things that can "
        "lose. That is the mechanism this project exists to name, and Zion is its clearest instance."),
    legacy=(
        "Distinguish four things, because they are not the same and only two of them are "
        "descent.<br><br><strong>Textually, nothing descends.</strong> Schadewald's verdict is blunt "
        "and we did not find grounds to soften it: “neither Voliva nor any of his disciples ever "
        "produced a flat-earth book, or even a pamphlet.” The name “Voliva” returns zero hits in the "
        "Internet Archive OCR of Dubay's <em>200 Proofs</em> (139,316 bytes, searched end to end "
        "2026-08-11; the one “Zion” hit is the <em>Protocols</em>, not Illinois). His distinctive "
        "content is not on the specimen list either: searching all 461 items for ice, Antarctic, the "
        "32-mile Sun, the 3,000-mile Sun and the silver-dollar circumnavigation returns one item — "
        "number 82, “Heliocentric gravity assumptions unproven” — and there is no ice-wall item at "
        "all. Seven items are credited to him across two clusters, and the arguments in both were in "
        "print before he was ordained (see <code>record_problems</code>).<br><br><strong>One image "
        "does descend.</strong> He did not make the flat-earth map — that is Gleason's “New Standard "
        "Map of the World,” Buffalo 1892, US Patent 497,917 — but he is why it was photographed. He "
        "posed with it for the newspapers in 1922 and put it on the cover of the 10 May 1930 "
        "<em>Leaves of Healing</em>. The azimuthal-equidistant disc that is now the movement's emblem "
        "passed through his hands into the American press.<br><br><strong>One letter descends, and it "
        "may outweigh everything else.</strong> In 1942, the last year of his life, an "
        "eighteen-year-old Texan wrote to Zion asking for more information about the flat Earth. "
        "Voliva sent a kind reply. The correspondent was Charles Kenneth Johnson, who would run the "
        "International Flat Earth Research Society for nearly thirty years and add the frame in which "
        "astronomers are lying rather than mistaken. Zion to Lancaster, California, in one envelope. "
        "<em>This rests on a single sentence in Schadewald and is not corroborated in Johnson's own "
        "published accounts as we have them; label it as reported, not "
        "established.</em><br><br><strong>What resembles him is not descended from him.</strong> Zion "
        "is the only flat-earth theocracy on record — required curriculum, a church press, a "
        "broadcast licence, a cash challenge with the proponent as judge. Modern flat-earth media "
        "reproduce that shape almost feature for feature, and no line of transmission has been traced "
        "here; the resemblance is best read as the same shape being reinvented, not inherited. Two "
        "closing facts cut against any triumphal reading in either direction. Zion became, in "
        "Schadewald's phrase, “a national laughingstock,” with pieces in <em>Collier's</em> (14 May "
        "1927) and <em>American Mercury</em> (April 1930) — which is why the movement's "
        "early-20th-century public face was authoritarian-religious rather than zetetic-empirical, an "
        "association it has been arguing against ever since. And in 1935 Voliva was deposed; the "
        "church dropped the word “Apostolic” and the flat Earth together. The institution he built "
        "discarded the doctrine seven years before he died."),
    kernel=dict(
        description=(
            "Voliva's opening to the 1930 special issue is the best sentence anyone in this movement "
            "has written, and it is <em>correct</em>: “The so-called Fundamentalists of the Churches, "
            "in opposition to Modernism, strain out the gnat of Evolution and swallow the camel of "
            "Modern Astronomy. All the leading Modernists declare that the Bible teaches that the "
            "earth is a stationary plane. In that declaration, they are right.” He is right about "
            "them, and he is right about the text. The hermeneutic that reads Genesis 1 as a literal "
            "six-day report, applied without exception, also yields a solid sky. His lieutenant Anton "
            "Darms argued that <em>chug</em> in Isaiah 40:22 and Job 22:14 should be rendered “vault” "
            "or “arch” rather than “circle” — which is what the New English Bible gives, and "
            "Schadewald, an opponent, breaks off mid-refutation to say modern scholars agree. Paul "
            "Seely's “The Firmament and the Water Above” (<em>Westminster Theological Journal</em> "
            "53, 1991) argues at length in a confessional journal that the <em>raqia</em> was "
            "conceived as literally solid. So Voliva caught his opponents in a real inconsistency: "
            "fundamentalists who fought evolution on the strength of a literal reading, and accepted "
            "an astronomy that reading forbids. He said so in public for twenty-six years and was not "
            "answered on the point."),
        why_it_doesnt_save_claim=(
                "Because it is an argument about what an ancient text describes, and it runs equally "
                "hard in the opposite direction. Schadewald built the same case in “The Flat-Earth "
                "Bible” and drew the opposite conclusion — the cosmology is there, so the text is "
                "reporting the sky as its authors understood it. Voliva's exegesis establishes that "
                "his opponents were inconsistent; it does not establish where the Sun is, and the two "
                "questions are settled by different instruments. He knew that himself, which is why "
                "the 1930 issue does not stop at scripture: it computes a Sun 32 miles wide and 3,000 "
                "miles up. The moment the claim becomes a distance it becomes checkable, and at that "
                "moment the exegesis stops helping. A third noon altitude decides it; the movement's "
                "own three incompatible answers for that one distance decided it before anyone "
                "outside had to.")),
    sources=[
        dict(label=(
                "Robert Schadewald, The Plane Truth, ch. 8 (\"Voliva and Zion\") — the primary "
                "narrative for everything above"),
             url="https://www.cantab.net/users/michael.behrend/ebooks/PlaneTruth/pages/Chapter_08.html",
             note=(
                "Fountain County birth, the Dowie years, Australia 1901-05, the sermons of 16 Aug "
                "1914 / 26 Dec 1915 / 3 Feb 1916, Darms's fifty reasons and 229 verses, the 1916 "
                "schools, WCBD, the $5,000 offer, the 10 May 1930 special issue, the 1935 deposition, "
                "death 11 Oct 1942, and the 1942 letter to Charles…")),
        dict(label=(
                "Preface to the 2015 web edition of The Plane Truth — Schadewald died in 2000 with "
                "the book unfinished; Lois Schadewald prepared this edition with Bob Forrest and "
                "Michael Behrend and states she \"could have never fact checked it\""),
             url="https://www.cantab.net/users/michael.behrend/ebooks/PlaneTruth/pages/Preface.html"),
        dict(label=(
                "Schadewald, The Plane Truth, ch. 4 — the Robert Woodhouse quotation as printed in "
                "Lady Blount's Earth Review under \"Honest and Noble Confessions\", with Schadewald's "
                "note that \"No source was given\" and that it \"was recycled endlessly in flat-earth "
                "literature\". This is what Voliva paraphrases on 3 Feb 1916"),
             url="https://www.cantab.net/users/michael.behrend/ebooks/PlaneTruth/pages/Chapter_04.html"),
        dict(label="Samuel Rowbotham (\"Parallax\"), Zetetic Astronomy",
             url="https://www.gutenberg.org/ebooks/69892",
             note=(
                "Earth Not a Globe! (1865) — Section 14, \"The doctrine of the universality of "
                "gravitation is an assumption\", at lines 3703-3704 of the plain text. The dated "
                "evidence that cluster A23's argument predates Voliva by fifty years")),
        dict(label=(
                "William Carpenter, One Hundred Proofs that the Earth Is Not a Globe (Baltimore, "
                "1885) — searched for gravitation/attraction; one hit, at line 762, and no numbered "
                "proof turns on gravity. The work Zion is said to have reprinted in 1929"),
             url="https://www.gutenberg.org/ebooks/55387"),
        dict(label=(
                "Eric Dubay, 200 Proofs Earth Is Not a Spinning Ball — Internet Archive OCR, 139,316 "
                "bytes, searched end to end 2026-08-11. \"Voliva\" returns 0 hits; \"Zion\" returns "
                "1, in a reference to the Protocols. Cited for a scoped negative: Voliva is not named "
                "in the modern compilation"),
             url="https://archive.org/details/200proofsearthisnotaspinningballericdubay"),
        dict(label="Paul H. Seely, \"The Firmament and the Water Above, Part I",
             url="https://thedivinecouncil.com/seelypt1.pdf",
             note=(
                "The Meaning of raqia' in Gen 1:6-8\", Westminster Theological Journal 53 (1991) — "
                "argues the raqia was conceived as literally solid. Supports the kernel: the "
                "exegetical claim Voliva and Darms made about the ancient text is substantially what "
                "critical scholarship holds")),
        dict(label=(
                "Robert Schadewald, \"The Flat-Earth Bible\", Bulletin of the Tychonian Society 44 "
                "(July 1987) — an opponent building the same exegetical case Voliva built and drawing "
                "the opposite conclusion. The reason the kernel does not save the claim"),
             url="https://www.theflatearthsociety.org/library/pamphlets/Bulletin%20of%20the%20Tychonian%20Society%20(Number%2044%20-%20July%201987).pdf"),
        dict(label=(
                "Glenn Branch (NCSE), \"Voliva!\", 5 August 2014 — the \"trinity of evils\" framing, "
                "and that globes were banned in Zion's schools; also that WCBD was powerful enough to "
                "be heard in Australia"),
             url="https://ncse.ngo/voliva"),
        dict(label=(
                "Wikipedia, \"Wilbur Glenn Voliva\" — the 1923 WCBD date (cited there to Kneitel), "
                "the 32-mile / 3,000-mile Sun and the \"lamp in Kenosha\" line (both cited there to "
                "Gardner, Fads and Fallacies, Dover 2nd ed. 1957), and the end-times prediction years"),
             url="https://en.wikipedia.org/wiki/Wilbur_Glenn_Voliva"),
        dict(label=(
                "Fountain County INGenWeb Project, Voliva biography file — birth 10 March 1870 on a "
                "farm near Newtown, Fountain County, Indiana; father James H., mother Rebecca F. "
                "Transcribed from the Pittsburg (Kansas) Sun, 12 Feb 1906; New Richmond Record, 12 "
                "Nov 1914; and Zion City's own The Theocrat, 4 May 1918. Independent corroboration of "
                "the birth data in our dates field"),
             url="http://ingenweb.org/infountain/bios%20N_Z/voliva,-wilbur.html"),
        dict(label=(
                "Library of Congress research guide, \"The Flat Earth and its Advocates\" — searched "
                "for Voliva and for a 1929 edition of Carpenter. Voliva appears only through popular "
                "anthologies of eccentrics (Gardner 1957; Wallace 1957; Bramhall 1982; Sifakis 1984; "
                "Time-Life 1992). No 1929 edition of One Hundred Proofs appears"),
             url="https://guides.loc.gov/flat-earth/books"),
        dict(label="Philip L. Cook, Zion City, Illinois",
             url="https://archive.org/details/zioncityillinois0000cook",
             note=(
                "Twentieth-Century Utopia (Syracuse University Press, 1996; LCCN 95033571) — the "
                "standing academic history of Zion City under Dowie and Voliva. LISTED, NOT "
                "CONSULTED: the Internet Archive copy is lending-restricted and no searchable text "
                "was available. Everything above rests on Schadewald, and…"))]),

"PER-SHENTON": _p(
    name="Samuel Shenton", dates="30 March 1903 – 2 March 1971",
    lineage="Zetetic",
    role=(
        "Institutional, not originating: founding officer of the flat-earth society of 1956 and the "
        "movement's first respondent to the space age. Carrier of Rowbotham; no argument on this list "
        "traces to him."),
    bio_status="worked",
    formation=(
        "A signwriter in Dover, Kent — born at Great Yarmouth, the son of an army sergeant major — "
        "who arrived at the flat Earth backwards, through an invention that assumed the opposite. By "
        "the 1920s he had worked out an airship that would rise, hold station, and let the Earth turn "
        "westward beneath it at some 1,000 km/h until the destination arrived at the same latitude. "
        "That scheme requires a <em>rotating</em> Earth. Unable to see why nobody had thought of it, "
        "he went to the reading room of the British Museum, found that Charles Isaac Stevens — an "
        "associate of Lady Blount of the Universal Zetetic Society — had proposed much the same "
        "craft, pulled the bibliographic thread that discovery opened, and came out of it holding "
        "Parallax's <em>Zetetic Astronomy</em>. He converted on the spot. (This account is Christine "
        "Garwood's, at pp. 220–222 of her 2007 history; we cite her at second hand through "
        "Wikipedia's footnotes — see <em>sources</em> for why.)<br><br>What he took from Rowbotham "
        "was the rule rather than any particular measurement. Garwood's summary is that he held to "
        "“zetetic enquiry” in which only personally acquired facts were permissible. Applied in 1849 "
        "that rule sends a man to a canal with a telescope. Applied in 1956 it says in advance that "
        "nothing produced by a space agency can ever count as evidence, because you did not produce "
        "it — and that is the position on which he helped found a society in the year before Sputnik. "
        "He then built out a cosmology of his own: a disc centred on the North Pole, an ice wall at "
        "the rim, seven literal heavens stacked above a dome, a Sun 32 miles across and 3,000 miles "
        "up, and a detailed account of how the alleged space capsules moved <em>above</em> the Earth "
        "rather than around it."),
    had=(
        "Less than his predecessors and a harder job than any of them. Rowbotham had a six-mile "
        "canal; Shenton had a terrace house, a signwriter's hand for flip charts, and eleven years in "
        "which the evidence against him arrived on television roughly annually.<br><br>He also had, "
        "from the first meeting, exactly the interlocutor this page usually complains is missing. "
        "Patrick Moore of <em>The Sky at Night</em> came to the 1956 inaugural meeting out of "
        "curiosity and later wrote it up; correspondents sent Shenton photographs of the Earth from "
        "space and diagrams “painstakingly constructed with compasses and set-squares”; he answered "
        "the letters, gave dozens of lectures for a fee of perhaps £5 and expenses, and by "
        "Schadewald's count roughly half his post came from schoolchildren. He did this through two "
        "strokes in 1963 and the collapse of his signwriting business, largely at his own "
        "expense.<br><br>And on the one point where the movement is usually at its weakest he had "
        "something real. Between 1956 and Christmas 1968, every whole-Earth image a man in Dover "
        "could be shown was, as a matter of engineering, <em>assembled</em>. ATS-1's spin-scan camera "
        "took a strip of the Earth per rotation and tilted its mirror for the next, so that, in "
        "NOAA's own description, “an image of Earth could be pieced together line by line in less "
        "than 30 minutes.” Lunar Orbiter developed its film in orbit, scanned it with a "
        "photomultiplier, radioed the signal home, and had ground crews lay the framelets “side by "
        "side on stable-base polyester film to reconstruct the original photograph.” Garwood dates "
        "the sharp fall in his membership to the Lunar Orbiter pictures. When Shenton said the "
        "pictures were put together, he was describing the process correctly.<br><br>Last, and rarest "
        "on this page: in December 1968, in a wire story, he said in public and in advance what would "
        "settle it. “If they show us a very clear picture of the earth from space and the picture "
        "does not show all the continents, and the edge of the picture is out of perspective, then "
        "that would prove that the earth is round.” Both halves of that test are the right two things "
        "to ask for — one hemisphere's worth of continents, and a foreshortened limb."),
    ignored=(
        "The answer to his own test, which arrived inside a fortnight. Apollo 8 was in lunar orbit on "
        "the day that criterion was printed; the crew were home on 27 December, and their Earth "
        "photographs were not scans or assemblies but 70 mm film exposed in a Hasselblad, carried "
        "back in the spacecraft and processed after the mission — a single frame showing one face of "
        "the planet with the limb curving away, which is what he had asked for. On 3 January 1969 he "
        "answered it: “That's where those Americans and Russians are so damned cunning… Some of the "
        "pictures have been blatantly doctored. Studio shots, probably.” After Apollo 11 the "
        "objection moved once more: “The astronauts are hypnotized into believing they go into "
        "space.”<br><br>Note where the objection travelled. It began at the image, where it was "
        "checkable and where he had a real point, and it ended at the people holding the camera, "
        "where nothing can reach it. That is Rowbotham's move on the Antarctic navigators, made again "
        "with better pictures: when the reading could only come out one way, the witnesses stopped "
        "counting as witnesses.<br><br>The second thing unused is the rule itself. “Only personally "
        "acquired facts” was applied to the photographs and not to his own cosmology: a Sun 32 miles "
        "wide and 3,000 miles up, seven stacked heavens, an ice wall — not one of which anybody in "
        "Dover could take with a ruler, and whose provenance we have not located in the sources read "
        "for this pass. A rule that admits inherited numbers and excludes inherited images is not a "
        "rule about how facts are acquired.<br><br>One failing he should not be charged with: he did "
        "not hide from critics. The astronomer was at the first meeting, the sceptics' letters were "
        "opened, the invitations to speak were accepted, and the falsification criterion was "
        "volunteered rather than extracted. What he did with the answer is the finding; the refusal "
        "to be in the room is not available as one."),
    legacy=(
        "<strong>Carried forward: the institution, not an argument.</strong> What descends from "
        "Shenton is continuity — a flat-earth society that survived the space age at all. He picked "
        "Ellis Hillman as successor with Patrick Moore's encouragement; Hillman, then working up a "
        "postgraduate course on the history of ideas about the Earth's shape, did little with it. "
        "After Shenton's death in March 1971 his widow Lillian kept the society going briefly, and in "
        "1972 the leadership and “a small but precious library of flat-earth books” went to Charles "
        "K. Johnson in California. Every later body trading under the name stands downstream of that "
        "transfer.<br><br><strong>Not carried forward: any item on this list.</strong> On the "
        "evidence located, none of the 461 items traces to him. `clusters.py` A21 (items 15, 96 and "
        "109) currently prints “Samuel Shenton, 1957”, and that attribution does not survive "
        "inspection on three counts: no satellite occupied a geostationary orbit until Syncom 3 in "
        "1964, so there was nothing in 1957 for the argument to be about; the date contradicts our "
        "own founding date elsewhere in the dataset; and the speech act is the wrong way round. A21 "
        "<em>affirms</em> the satellites and re-describes them in an Earth-fixed rotating-heavens "
        "frame — a Machian argument whose named modern author in the corpus is Martin Selbrede via "
        "Sungenis & Bennett. Shenton's move was the denial that they orbit anything. The two are not "
        "the same claim, and this record does not claim him as an originator of "
        "it.<br><br><strong>Resembling but not traced.</strong> Modern “the photographs are CGI” "
        "resembles “studio shots, probably”, but the documented line into modern lists runs through "
        "Johnson's <em>Flat Earth News</em> and its NASA-fakery layer, not through Dover — and it "
        "cannot be tested on this specimen in any case, because a search of all 461 items for "
        "photograph, image, composite, hoax, fake or NASA returns no photo-fakery item at all. This "
        "list is technical and scriptural; the lane Shenton opened is missing from "
        "it.<br><br><strong>One correction owed to our own genealogy.</strong> The project's summary "
        "line — Rowbotham and Carpenter said the astronomers were <em>wrong</em>, Johnson said they "
        "were <em>lying</em> — needs a hedge. The attribution of deliberate deception to the space "
        "agencies is in Shenton's mouth in a wire report of 3 January 1969, three years before "
        "Johnson inherited the society. Johnson systematised it; he did not start it."),
    kernel=dict(
        description=(
            "For the whole of his active career the "
            "sentence “that picture was put together” was true of the pictures. It is true of ATS-1's "
            "line-by-line spin scan and true of Lunar Orbiter's framelets pasted onto polyester, and "
            "it is documented by the agencies themselves, not by his side. And he did the thing this "
            "review keeps asking of the people it reviews — he named a falsifier in advance, in "
            "public, and named the right one: show the Earth with only some of its continents visible "
            "and its edge in perspective. Almost nobody else on the People tab left a dated statement "
            "of what would change their mind."),
        why_it_doesnt_save_claim=(
                "a criterion binds you on the day it is met. His was met in ten days, by images made "
                "a different way — chemical film exposed through a lens and physically carried home — "
                "and he did not pay. Instead the objection relocated from the photograph to the "
                "photographers: cunning, then doctored, then hypnotised. That relocation is "
                "unfalsifiable by construction, and it converts the good instinct into its opposite, "
                "because a test you will re-site when it fails was never a test. The value of his "
                "case to this page is precisely that he wrote the criterion down first: the failure "
                "is legible because he made it checkable, which is more than the arguments in the "
                "specimen list do.")),
    sources=[
        dict(label=(
                "Schadewald, The Plane Truth, ch. 9 — the Shenton passage and the 1972 transfer to "
                "Johnson"),
             url="https://www.cantab.net/users/michael.behrend/ebooks/PlaneTruth/pages/Chapter_09.html"),
        dict(label="Wikipedia — Samuel Shenton (article and raw wikitext, retrieved 2026-08-11)",
             url="https://en.wikipedia.org/wiki/Samuel_Shenton"),
        dict(label="Garwood, Flat Earth",
             url="https://archive.org/details/flatearthhistory0000garw",
             note="The History of an Infamous Idea (Macmillan, 2007), pp. 220–222 and 234–238"),
        dict(label=(
                "AP, “Flat Earth Proponents To Pause and Reconsider”, St Louis Post-Dispatch, 24 "
                "December 1968, p. 4A — the falsification criterion"),
             url="https://www.newspapers.com/clip/21503644/st_louis_postdispatch/"),
        dict(label=(
                "“Apollo Levels Flat Earth Chief”, Green Bay Press-Gazette, 3 January 1969, p. B12 — "
                "“blatantly doctored… studio shots, probably”"),
             url="https://www.newspapers.com/clip/21504109/green_bay_pressgazette/"),
        dict(label=(
                "Robert C. Toth (LA Times service), “Flat Earth Society Leader Scoffs At Apollo 11 "
                "Flight”, Anniston Star, 6 August 1969, p. 9A"),
             url="https://www.newspapers.com/clip/21504047/the_anniston_star/"),
        dict(label=(
                "NOAA NESDIS — the 50th anniversary of ATS-1, on how the spin-scan camera built a "
                "full disc line by line"),
             url="https://www.nesdis.noaa.gov/news/the-50th-anniversary-of-ats-1"),
        dict(label="LPI/USRA — Digital Lunar Orbiter Photographic Atlas of the Moon, Introduction",
             url="https://www.lpi.usra.edu/resources/lunar_orbiter/book/introduction.shtml",
             note="Bimat development in orbit, photomultiplier scan, framelets reassembled on polyester"),
        dict(label=(
                "NASA — Astronaut Still Photography During Apollo (Hasselblad EL first used on Apollo "
                "8; 70 mm magazines; ~1,100 photographs returned)"),
             url="https://www.nasa.gov/history/astronaut-still-photography-during-apollo"),
        dict(label=(
                "Royal Astronomical Society — how to join (fellowship open to anyone over 18, by "
                "nomination or reference, elected by Council)"),
             url="https://ras.ac.uk/membership/join")]),

"PER-JOHNSON": _p(
    name="Charles Kenneth Johnson", dates="24 July 1924 – 19 March 2001",
    lineage="Zetetic",
    role=(
        "Institutional carrier rather than originator: he inherited Shenton's society and library in "
        "1972 and ran it until 2001. What is new in him is the scale and machinery of the deception "
        "charged, not the charge itself — Carpenter was already accusing astronomers of deceiving "
        "people in 1885."),
    works=["WRK-JOHNSON-FEN"],
    bio_status="worked",
    formation=(
        "Born 24 July 1924 on his father's ranch near San Angelo, Texas. By his own account, repeated "
        "for the rest of his life, he rejected the globe in the early 1930s at the age of seven or "
        "eight, when a grade-school teacher answered “why don't things fall off?” with the "
        "swinging-bucket demonstration; he went home, pumped a bucket of water at the well, swung it, "
        "and concluded that the demonstration had nothing whatever to do with the shape of the Earth. "
        "He was right about that much, and it is worth saying so — the bucket shows that a constraint "
        "force can exceed gravity, and it shows nothing about the figure of the Earth. He left the "
        "school system as a teenager, read widely on his own, worked in Texas and Colorado and then "
        "California, and spent some twenty-five years as an airplane mechanic in San Francisco. In "
        "1981 he went back to the John H. Reagan School in San Angelo, found the same room and what "
        "he took to be the same globe, and printed the photograph in his own newsletter. In the late "
        "1960s an American press item about Samuel Shenton reached him; he wrote to Dover and joined. "
        "Shenton died in 1971 having named Ellis Hillman his successor; Hillman would not take it and "
        "Shenton's widow Lillian could not hold it, so in 1972 the presidency and Shenton's small "
        "library of flat-earth books crossed to Johnson's five acres at Hi Vista, in the Mojave "
        "outside Lancaster, California, where he ran the body as the International Flat Earth "
        "Research Society of America and Covenant People's Church until his death. On his own telling "
        "the conviction was not reached by argument and was never revised: he formed it at seven and "
        "spent the next seven decades administering it."),
    had=(
        "Less than any other name on this page, and he was candid about it. He had Shenton's library "
        "— the movement's own primary literature, Rowbotham through Cook — and he had a tradition "
        "that told him its work was finished. He had his eyes and two lakes: he and Marjory checked "
        "the surfaces of Lake Tahoe and the Salton Sea for curvature and found none. That is the "
        "right instinct and the wrong instrument, and the reason is the same one that runs through "
        "the Rowbotham entry — an unaided sightline a few feet above water cannot resolve the effect "
        "without a target of known height or a marker at the midpoint, and the Salton Sea in "
        "particular is a shallow desert lake with exactly the thermal gradient that manufactures a "
        "false null. He also had something no other figure here had: the space programme in his back "
        "yard. The orbiters were assembled at Palmdale and flight-tested at Edwards, and he knew "
        "people who worked on them. That access produced at least one accurate report. His sneer that "
        "the tiles were “stuck on with epoxy, and half fell off” describes a real event: NASA's own "
        "history of the March 1979 ferry flight from Palmdale to Kennedy records that thousands of "
        "thermal-protection tiles came off in transit and that nine days were spent reapplying them. "
        "And he had the 1970s, which is not nothing. A man forming the view that governments lie "
        "systematically between 1971 and 1976 was reading the same front pages as everyone else: the "
        "Pentagon Papers, the stolen COINTELPRO files, Tuskegee, Watergate, the Church Committee. Two "
        "props he declined to use. He would not argue from scripture — “We don't quote Scriptures,” "
        "he said, “We concentrate on the evidence” — and he would not claim the authority of science, "
        "saying instead that what the society had was not flat-Earth science but flat-Earth facts."),
    ignored=(
        "One thing, and it landed twenty-odd miles from his front door. He held that the Space "
        "Shuttle was never intended to fly. On 14 April 1981 <em>Columbia</em> came down on Rogers "
        "Dry Lakebed at Edwards Air Force Base in front of an estimated 400,000 spectators, its "
        "double sonic boom audible across the Antelope Valley, and Edwards went on hosting shuttle "
        "landings for three decades. No answer to that is located in the material reached for this "
        "entry — Schadewald's chapter, the <em>Science Digest</em> interview of July 1980, and the "
        "three obituaries — and the scope matters, because his own quarterly is where an answer would "
        "be: no issue of <em>Flat Earth News</em> was reachable from this container on 2026-08-11 "
        "(the society's own library returned HTTP 403 to a direct fetch and a TLS hostname mismatch "
        "to the fetch tool, while its wiki says nineteen issues are online). So this is an objection "
        "not answered in what we could read, not an objection provably never answered. The second is "
        "the tradition's own instruction. Schadewald, who held a membership card and visited the "
        "house, records that Johnson “didn't contribute much to flat-earth theory” because he "
        "regarded the zetetic system as essentially complete. <em>Zetetic</em> means <em>to "
        "search</em>. Declaring the search finished is the one move the method forbids, and it is the "
        "difference between Rowbotham, who stopped early, and Johnson, who did not start. What he did "
        "not do deserves recording too, because the list of failings here is short and could easily "
        "be padded. He did go and look at water rather than only reading about it. He did not retreat "
        "into scripture when the evidence thinned. And when a <em>Balanced Treatment of Flat-Earth "
        "Science and Spherical-Earth Science Act</em> was floated, he refused to support it — he did "
        "not want equal time, on the ground that accepting the frame of science was the kiss of "
        "death. That is a more honest position than the one his successors took."),
    legacy=(
        "Start with the measurement, because it is embarrassing. This dataset credits him with 2 "
        "arguments and 4 of the 461 items — B12, polar navigation and dead reckoning (items 128, 408, "
        "409), and B14, rocket and balloon footage (item 228) — and neither attribution is evidenced. "
        "The B12 treatment says so in terms: no text of Johnson's carrying a navigation argument was "
        "reached, while a fully documented Victorian chain carries all three items, from Rowbotham's "
        "1865 circumnavigation section through Carpenter's proofs 8–16 to Dubay's proofs 34–39 and "
        "108–111, the Milner quotation reproduced footnote and all. B14 rests on the same unread "
        "source. If both were withdrawn his item count would be zero, and his importance would be "
        "unchanged — which is the finding, not an objection to it. What does not descend from him is "
        "easy to check and worth checking. The string “Johnson” returns no hit in the OCR of Dubay's "
        "<em>200 Proofs</em> (archive.org item 200ProofsEarthIsNotASpinningBall_201903, 139,316-byte "
        "text, searched 2026-08-11), and this project's map of Dubay's named sources lists Rowbotham, "
        "Carpenter, Winship, Scott and Blount's <em>Earth Review</em>. Nor is there organisational "
        "descent: the society went dormant when he died in March 2001, the name was taken up in 2004 "
        "by Daniel Shenton — no relation to Samuel — as a web forum relaunched in October 2009, and "
        "the 2014–15 YouTube wave that produced the specimen list was unaffiliated with any of it. "
        "One suggestive thread runs through and will not bear weight. Johnson named Arthur C. Clarke "
        "as the man who wrote the scripts for the faked Moon landings; Dubay's proof 166 names "
        "“Freemason science-fiction writer Arthur C. Clarke” as the inventor of the geostationary "
        "satellite. Same man, different charge, thirty-five years apart — and Clarke's 1945 paper on "
        "stationary orbits is a real and obvious thing to arrive at independently, so this is "
        "resemblance, not a demonstrated chain. What does plausibly carry is the frame itself, and "
        "one dated claim. He is not the originator of the Moon-hoax argument — the earliest "
        "documented flat-earth statement of it located here is his, in 1980, four years after Bill "
        "Kaysing's self-published book of 1976 — but his 1980 interview is also the earliest "
        "documented use this pass has located of the claim that the United Nations took the "
        "flat-earth map as its emblem, an argument the project has until now recorded as having no "
        "traceable origin. That is an earliest documented use, not an origin."),
    kernel=dict(
        description=(
            "Three true things, and the third is to his credit rather than his argument's. First, he "
            "was right that almost nobody who says the Earth is a globe has checked. What most people "
            "hold is testimony, and testimony is a social relation rather than evidence in hand — a "
            "point that survives being made by someone who then draws the wrong conclusion from it. "
            "Second, he was right that large institutions lie, and he was making the claim in the "
            "decade that proved it: the Pentagon Papers, COINTELPRO, Tuskegee, Watergate and the "
            "Church Committee all landed between 1971 and 1976. He was even right about the tiles. "
            "Third, and this is the strongest form of Charles Johnson: he refused the credibility "
            "costume. He would not argue from scripture and would not call his position science, and "
            "when an equal-time bill for “flat-Earth science” was proposed he declined it, saying "
            "that taking the frame of science was the kiss of death — the precise mistake he thought "
            "the creationists had made. Very few people in this review turned down borrowed authority "
            "when it was offered."),
        why_it_doesnt_save_claim=(
                "An institution that has lied about some things is not thereby lying about "
                "everything, and the useful question is which particular claim is checkable and by "
                "whom. Johnson's frame supplies no handle for that: it accommodates any observation "
                "whatever, which is exactly why the two lakes could never have come out the other "
                "way, and why the Shuttle landing over the hill required no answer. When his heirs "
                "did finally build the checkable version, it answered — Bob Knodel's ring-laser "
                "gyroscope read 15°/hour on camera in 2018, and the Antarctic midnight sun was "
                "observed and conceded in December 2024. And the one thing he got right about method "
                "is the one thing the movement did not carry forward. It took the lab coat he "
                "refused, and kept the frame that makes the coat unnecessary.")),
    sources=[
        dict(label="Schadewald, The Plane Truth, ch. 9 — “Johnson and Johnson",
             url="https://www.cantab.net/users/michael.behrend/ebooks/PlaneTruth/pages/Chapter_09.html",
             note="Two Witnesses”"),
        dict(label="Schadewald, “The flat-out truth",
             url="https://www.zunick.com/earth-science/ewExternalFiles/ES%20The%20Flat%20Out%20Truth.pdf",
             note=(
                "earth orbits? Moon landings? A fraud! says this prophet,” Science Digest v. 88 (July "
                "1980), 58–63")),
        dict(label="Library of Congress — The Flat Earth and its Advocates",
             url="https://guides.loc.gov/flat-earth/articles",
             note="journal articles"),
        dict(label="Tim Bullamore, obituary of Charles Johnson, The Independent, 30 March 2001",
             url="http://library.tfes.org/library/2001_03_30_-_the_independent_obituary.html"),
        dict(label="Obituary, NY Press, 4 April 2001 (page now dated 2014 after a site migration)",
             url="https://www.nypress.com/news/charles-k-johnson-president-of-the-international-flat-earth-research-society-icnp1020010404304049996"),
        dict(label="Wikipedia — Charles K. Johnson; Modern flat Earth beliefs",
             url="https://en.wikipedia.org/wiki/Charles_K._Johnson"),
        dict(label=(
                "Carpenter, One Hundred Proofs that the Earth Is Not a Globe (5th ed., Baltimore "
                "1885) — Project Gutenberg #55387"),
             url="https://www.gutenberg.org/ebooks/55387"),
        dict(label="Edwards AFB public affairs — anniversary of Columbia's first landing, 14 April 1981",
             url="https://www.edwards.af.mil/News/Article/829237/april-14-marks-anniversary-of-space-shuttle-columbias-first-landing/"),
        dict(label="NASA history — 45 years ago",
             url="https://www.nasa.gov/history/45-years-ago-space-shuttle-columbia-arrives-at-nasas-kennedy-space-center/",
             note="Space Shuttle Columbia arrives at Kennedy Space Center"),
        dict(label="Dubay, 200 Proofs Earth Is Not a Spinning Ball — OCR text at archive.org",
             url="https://archive.org/details/200ProofsEarthIsNotASpinningBall_201903"),
        dict(label="The Flat Earth Wiki — Flat Earth News",
             url="https://wiki.tfes.org/Flat_Earth_News")]),

"PER-DUBAY": _p(
    name="Eric Dubay", dates="active 2008–; flat-earth work from 2014",
    lineage="Zetetic",
    role=(
        "Carrier, not originator. Compiler of 200 Proofs (2015) and president of the revived IFERS; "
        "his single origination credit in this dataset is contested by our own B08 research."),
    works=["WRK-DUBAY-2015"],
    bio_status="worked",
    formation=(
        "Dubay did not arrive at the flat Earth through an experiment, and has never said he did. He "
        "describes himself on his publisher&rsquo;s author page as “a 43 year old American living in "
        "Thailand where he teaches Yoga and Wing Chun part time while exposing the New World Order "
        "full time” — a self-description, reproduced as such; a near-identical bio on his PeakD "
        "profile gives his age as 36, and neither page is dated. The publishing sequence tells more "
        "than the biography does. A novel, <em>Asbestos Head</em>, in 2008; <em>The Atlantean "
        "Conspiracy</em>, subtitled <em>Exposing the Global Conspiracy from Atlantis to Zion</em>, "
        "whose editions Open Library dates 2011 and 2013; <em>Spiritual Science</em> in 2012; then "
        "<em>The Flat-Earth Conspiracy</em> in 2014 and <em>200 Proofs Earth Is Not a Spinning "
        "Ball</em> as a free PDF and narrated videobook in 2015. (Those dates come from Open Library, "
        "a crowd-edited catalogue, not from a bibliography.) The flat Earth is therefore the fourth "
        "item in a conspiracy programme he already had, rather than the thing that started one — and "
        "the giveaway is that the subtitle of the pre-flat-earth book is, word for word, the "
        "strapline of the flat-earth forum he now administers. He also claims a specific line of "
        "descent. Arguing that Leo Ferrari&rsquo;s Flat Earth Society is “controlled opposition,” he "
        "writes: “To combat Ferrari&rsquo;s Flat Earth Society controlled opposition forum, and in "
        "memory of Samuel Shenton, Charles Johnson, and other true flat Earth researchers of the past "
        "I have now (re)started IFERS, The International Flat Earth Research Society forum!” That is "
        "a movement-internal statement on his own blog — evidence of where he places himself, not "
        "evidence of what happened — and it places him precisely where the item counts on this page "
        "already put him: downstream."),
    had=(
        "More than the genre norm, and the difference is documentable. The Victorian zetetic corpus "
        "is out of copyright and was fully online by 2015, and he used it openly rather than quietly. "
        "In the Internet Archive scan of <em>200 Proofs</em>, fifteen of the two hundred items carry "
        "a named source with a block quotation: Rowbotham at 62–66, 130, 148 and the closing item "
        "200; Carpenter at 96 and 129; Winship at 31; David Wardlaw Scott at 192 and 194; Lady "
        "Blount&rsquo;s <em>Earth Review</em> at 9 and 12. Beyond his own tradition he quotes "
        "Gabrielle Henriet, the Rev. Thomas Milner, Sir James Clark Ross, Lactantius, E. Eschini, the "
        "historian of mathematics Morris Kline — and, at 196, Marshall Hall, who belongs to the "
        "<em>other</em> lineage on this page. The geocentric and flat wings were never reconciled "
        "with each other; item 196 is one documented place where material crossed between them, taken "
        "from a man who holds the Earth to be a globe. He also states the hard case instead of "
        "ducking it: item 101 goes at Sigma Octantis by name and makes four specific, checkable "
        "claims about it, where the compressed list downstream keeps only the northern sky and "
        "mentions nothing south of the equator. And the delivery was genuinely his: free PDF, "
        "narrated videobook, then print, audiobook and translation, a German edition catalogued for "
        "2022. Nothing in the argument is new. The distribution is."),
    ignored=(
        "Four things, and the first two are checks he had every means to run. <em>First</em>, his own "
        "headline southern claim. Item 101 says Sigma Octantis “cannot be seen at all using publicly "
        "available telescopes,” and that “there is legitimate speculation regarding whether Sigma "
        "Octantis even exists.” It is magnitude +5.42 at about 294 light years, roughly a degree from "
        "the south celestial pole, formally named Polaris Australis, and it served as the comparison "
        "standard for southern-hemisphere magnitudes in the 1908 <em>Revised Harvard Photometry</em>. "
        "It is naked-eye at a dark site and has been in professional catalogues for over a century. "
        "<em>Second</em>, the document answers itself. The same item disqualifies the star for being "
        "“NOT central but allegedly 1 degree off-center” — but Polaris, on which his items 98 and 99 "
        "rest, stood 0.66° from the north celestial pole in 2018 and is still moving. The standard "
        "applied to the southern pole star removes the northern one. <em>Third</em>, a provenance "
        "failure of exactly the kind this review exists to catch. Item 198 offers the <em>Protocols "
        "of the Learned Elders of Zion</em> as a plan “completely disclosed.” Philip Graves "
        "demonstrated in <em>The Times</em> in 1921 that the text is plagiarised from Maurice "
        "Joly&rsquo;s <em>Dialogue aux enfers</em> of 1864 — some 160 passages — and a Bern court "
        "called it forgery in 1935. The tracing had been public for 94 years when he cited it. That "
        "is a statement about a source, not about the man who cited it: this page reviews claims, and "
        "a claim is neither better nor worse for whose name is on it. But a text whose provenance was "
        "demonstrated fraudulent in 1921 cannot be evidence in 2015, and a compiler who quotes his "
        "sources this carefully had the apparatus to check that one. (Danny Faulkner made a related "
        "criticism of the book in 2019 for Answers in Genesis — an apologetics organisation, not a "
        "scholarly body.) <em>Fourth</em>, and open rather than closed: in December 2024 members of "
        "his own movement observed the twenty-four-hour Antarctic sun on <em>The Final "
        "Experiment</em>, and Jeran Campanella conceded in full. That observation bears directly on "
        "his items 100–110. The expedition&rsquo;s own account states he was not among those who "
        "went; no reason from him has been located and none is inferred here. No published response "
        "by him to the observation was located in the searches run for this entry — his YouTube "
        "channel page, ericdubay.wordpress.com, and general web search, August 2026. That is a scoped "
        "absence, not a finding."),
    legacy=(
        "Small on this page, and the shape of the smallness is the finding. Seven of the 461 items "
        "and one argument — ARG-B08, the star-trail and Polaris cluster — and even that single "
        "origination credit is contested inside this repository. The agent who worked B08 traced both "
        "of its strands back to Rowbotham: the south-pole denial to the 1881 third edition, and the "
        "Polaris-seen-south-of-the-equator claim to the 1865 first book edition, on Captain Wilkins "
        "in <em>The Times</em> of 13 May 1862, two decades before Carpenter&rsquo;s proof 71 and 150 "
        "years before Dubay. <code>clusters.py</code> still reads originator “Eric Dubay”, year 2015. "
        "If that correction is applied he originates nothing on this page at all, which would make "
        "him the clearest carrier in the dataset rather than a marginal originator.<br><br>What did "
        "<em>not</em> travel is as informative. Roughly items 160 to 198 of <em>200 Proofs</em> are "
        "NASA, CGI, Freemasonry and motive — the layer with no Victorian ancestor, descending from "
        "Charles K. Johnson&rsquo;s conspiracy frame. A keyword search of all 461 corpus items for "
        "NASA, Apollo, satellite hoax, CGI, Freemason, Zion, Protocols, ice wall and Antarctica "
        "returns exactly one hit: item 459, “Masonic tracing boards beneath starry canopy,” which "
        "sits in the esoteric lane and is credited to Manly P. Hall and Blavatsky, not to him. The "
        "compiler downstream took the technical half of his list and dropped the half that was "
        "distinctively his.<br><br>Carried-forward against merely-resembling: 200 is "
        "Carpenter&rsquo;s 100 doubled, and Dubay says so. 461 is not 200 doubled again by anyone — "
        "the specimen is a different list with a different centre of gravity, roughly two-thirds "
        "Tychonian, and it touches his territory only in the Polaris items. What does descend from "
        "him is institutional rather than argumentative: he administers the revived IFERS forum, "
        "which displayed 8,550 registered users and 19,581 posts on 11 August 2026, on an explicit "
        "claim to Shenton&rsquo;s and Johnson&rsquo;s succession and against a rival flat-earth "
        "organisation he calls controlled opposition. Pannofino&rsquo;s 2024 study in "
        "<em>Genealogy</em> — the one piece of peer-reviewed scholarship located that names him — "
        "describes him in exactly those terms and records his book circulating in the Italian "
        "flat-earth scene, citing the 2018 CreateSpace edition."),
    kernel=dict(
        description=(
            "He shows his working, and in this genre that is rare enough to count as a virtue. The "
            "document this review actually examines — 461 numbered assertions — carries not one "
            "citation on any item. Dubay's 200 carry fifteen, with named authors, titles and block "
            "quotations, and the list closes by handing the reader back to Rowbotham and telling him "
            "where to read more. That is why a provenance review of this material is possible at all: "
            "the trail exists because he left it, and the compression finding this whole page rests "
            "on is measurable only against a source that named its own sources. He also states "
            "falsifiable claims where a vaguer writer would hedge. Item 101 names Sigma Octantis and "
            "makes four specific assertions about it, any one of which could have sunk him. "
            "Preferring the checkable claim to the safe one is closer to the zetetic ideal than most "
            "of what descends from Rowbotham."),
        why_it_doesnt_save_claim=(
                "Because citing a source is the first move and he stops after it. All four Sigma "
                "Octantis assertions are false and were checkable in 2015 against a star catalogue; "
                "the Protocols had been traced to Joly's 1864 satire in 1921. Naming where a claim "
                "came from is only worth something if somebody then goes and asks whether the place "
                "it came from was right — which is exactly the check this review is running on him, "
                "using the trail he supplied. And the virtue did not survive transmission. The "
                "specimen carries his subject matter with his attributions stripped: 461 items, no "
                "sources, no authors, no dates. The one thing that was genuinely his contribution to "
                "the form was gone within a single generation of copying, and his own list minus its "
                "sources is the object we are reviewing.")),
    sources=[
        dict(label=(
                "Dubay, 200 Proofs Earth Is Not a Spinning Ball — Internet Archive scan, OCR text "
                "read in full for this entry (items 9, 12, 31, 62–66, 96, 101, 129, 130, 148, 192, "
                "194, 196–200 quoted or counted)"),
             url="https://archive.org/details/200proofsearthisnotaspinningballericdubay"),
        dict(label=(
                "Eric Dubay, “The Flat Earth Society is Controlled Opposition” — the "
                "(re)started-IFERS statement and the claimed descent from Shenton and Johnson"),
             url="https://ericdubay.wordpress.com/2018/07/11/the-flat-earth-society-is-controlled-opposition/"),
        dict(label=(
                "IFERS — “Administrated by President Eric Dubay”; 8,550 registered users, 19,581 "
                "posts as displayed 11 August 2026"),
             url="https://ifers.forumotion.com/"),
        dict(label=(
                "Lulu author spotlight — Dubay's own author biography (“a 43 year old American living "
                "in Thailand…”)"),
             url="https://www.lulu.com/spotlight/ericdubay"),
        dict(label="PeakD profile — near-identical self-description giving his age as 36",
             url="https://peakd.com/@ericdubay"),
        dict(label=(
                "Open Library — Asbestos Head 2008, Atlantean Conspiracy 2011/2013, Spiritual Science "
                "2012, Flat-Earth Conspiracy 2014, 200 Proofs print 2018, Flatlantis 2020, German "
                "edition 2022"),
             url="https://openlibrary.org/search?q=Eric+Dubay"),
        dict(label="Pannofino, N. L. (2024), “The ‘Global’ Deception",
             url="https://www.mdpi.com/2313-5778/8/2/32",
             note=(
                "Flat-Earth Conspiracy Theory between Science and Religion”, Genealogy 8(2):32 — "
                "names Dubay as “a conspiracy theorist who points to previous flat-earth "
                "organizations as ‘controlled opposition’”, cites the 2018 CreateSpace edition")),
        dict(label=(
                "Sigma Octantis — magnitude +5.42, c. 294 ly, c. 1° from the south celestial pole, "
                "named Polaris Australis, comparison standard in the 1908 Revised Harvard Photometry"),
             url="https://en.wikipedia.org/wiki/Sigma_Octantis"),
        dict(label=(
                "Polaris — 0.66° (39.6′) from the north celestial pole in 2018, closest c. 0.45° "
                "after 2100"),
             url="https://en.wikipedia.org/wiki/Polaris"),
        dict(label=(
                "The Protocols — Philip Graves in The Times, 1921, showing c. 160 passages "
                "plagiarised from Joly's Dialogue aux enfers (1864); Bern verdict 19 May 1935"),
             url="https://en.wikipedia.org/wiki/The_Protocols_of_the_Elders_of_Zion"),
        dict(label=(
                "Danny Faulkner, “The Modern Flat-Earth Movement and Anti-Semitism”, 9 August 2019 — "
                "related criticism of 200 Proofs"),
             url="https://answersingenesis.org/blogs/danny-faulkner/2019/08/09/modern-flat-earth-movement-anti-semitism/"),
        dict(label=(
                "The Final Experiment, Antarctica, December 2024 — 24-hour sun observed, Campanella "
                "conceded; the article does not mention Dubay"),
             url="https://en.wikipedia.org/wiki/The_Final_Experiment_(expedition)"),
        dict(label="The Final Experiment (organisers), 2 October 2024",
             url="https://x.com/TFEAntarctica/status/1841574525508698439",
             note="“Eric Dubay will not be going to Antarctica with us.” No reason stated"),
        dict(label=(
                "Carpenter, One Hundred Proofs (1885) — searched for “Octantis”, “Southern Cross”, "
                "“circumpolar”, “south polar”"),
             url="https://www.gutenberg.org/ebooks/55387",
             note="zero hits"),
        dict(label=(
                "Rowbotham, Earth Not a Globe (1865 first book edition) — “Octantis” zero hits, "
                "“Southern Cross” one"),
             url="https://www.gutenberg.org/ebooks/69892"),
        dict(label=(
                "flatearth.ws — item-by-item rebuttals to the 200 Proofs; carries no biographical "
                "material on Dubay"),
             url="https://flatearth.ws/eric-dubay")]),

"PER-SARGENT": _p(
    name="Mark Sargent", dates="born c. 1968; active 2015–",
    lineage="Zetetic",
    role=(
        "Carrier and distributor, on his own account: the enclosed-world model packaged as a free "
        "video series from 10 February 2015. He denies originating anything — “I did not invent flat "
        "Earth” — and the dataset agrees with him."),
    works=["WRK-SARGENT-2015"],
    bio_status="worked",
    formation=(
        "Whidbey Island, Washington, born about 1968, and back living there now. Three years at "
        "Western Washington University without a degree, then roughly two decades in Colorado in and "
        "around the games and software trades: a win at a digital pinball competition in 1994 led to "
        "games-testing work for StarPlay Productions, and after that to training people in "
        "proprietary software until 2014. No training in any physical science, and — this matters, "
        "and it is to his credit — he has never claimed any. The conversion account is his own, given "
        "at the Flat Earth International Conference in Edmonton in August 2018 and reported from it: "
        "he came across a flat-earth video in the summer of 2014, set out to debunk it, and did not. "
        "He attributes his own susceptibility to spare time rather than to insight — “Most people get "
        "married and have kids. But if you don't, you have a huge amount of free time on your hands.” "
        "<em>That is a self-report, told to a friendly room, and it is recorded here as what he says "
        "about himself rather than as documentation of what happened.</em> On 10 February 2015 he "
        "uploaded “Flat Earth Clues Introduction” to YouTube. Note what is missing from that "
        "formation compared with everyone above him on this page: no canal, no theodolite, no "
        "telescope, no experiment. Rowbotham had six miles of still water; Bouw had a doctorate; "
        "Sargent had an editing suite. He entered a tradition that was already 166 years old, as a "
        "viewer, and left it as a broadcaster."),
    had=(
        "Less apparatus than anyone else on this page, and a clearer view than most of them of what "
        "the movement actually lacked. Rowbotham's <em>Earth Not a Globe</em> and Carpenter's hundred "
        "proofs had been free online for years by 2015; what did not exist was a version anybody "
        "would sit through. He supplied one — short, serialised, narratively framed, no arithmetic, "
        "no fee — and the audience arrived. That is a real observation about how this material "
        "propagates, and this review's own provenance data supports it rather than contradicting it. "
        "He also had one rhetorical instrument and used it consistently: the planetarium. In the Flat "
        "Earth Society's interview with him the dome is argued from Genesis 1:6 and from the analogy "
        "— “You're in a planetarium and you see Mars and Jupiter … then you walk outside the "
        "planetarium — How do you not know you are just not inside a bigger planetarium?” — and on "
        "ITV he puts the same thing as a sound stage and cites <em>The Truman Show</em>. He is also, "
        "in his own voice, more careful than his summarisers. Encyclopaedic accounts of his position "
        "give a “giant ice wall”; asked directly he hedges it — “It's not necessarily an ice wall, "
        "it's just Antarctica, this really, really, really high continent”. Asked what is beyond the "
        "enclosure he declines to answer: “That's a tough one, isn't it. If you can't get outside "
        "you're not going to know for sure.” <strong>The hedge rule applies to him as to everyone: we "
        "answer that version, not the compressed one.</strong> And what he did not have, he did not "
        "pretend to have. No experiment of his own is described in any source reached here — the "
        "Wikipedia article, the Flat Earth Society interview, the <em>Canadian Geographic</em>, "
        "<em>Everett Herald</em> and ABC News profiles, or the coverage of <em>Behind the Curve</em>. "
        "In the film he is the principal subject of, the two experiments it closes on belong to other "
        "people."),
    ignored=(
        "The objection he raises himself, and does not close. The engine of the enclosed-world model "
        "is that the sky can be <em>displayed</em> rather than inhabited: a ceiling good enough to be "
        "mistaken for a cosmos. Grant that, and no observation of the sky is evidence for any "
        "geometry — not for a globe, and not for a disc. It disposes of the 461 items on the specimen "
        "list, which are almost entirely sky observations, along with everything else. He states the "
        "premise in one interview (“if you can't get outside you're not going to know for sure”) and "
        "the conclusion from a conference stage in the same period (“Everybody here can agree on "
        "absolutely one thing, which is [Earth] is not a globe”), and nothing located here reconciles "
        "the two. This is the same shape as the Tychonian problem two lineages over: Bouw conceded "
        "observational equivalence and then his successors went on citing experiments as proof. A "
        "model that explains any appearance buys immunity by spending its evidence. Second, and "
        "available for the asking: the measurements that do not route through the appearance of the "
        "sky. A ring-laser gyroscope reading 15°/hour — which is 360° ÷ 24 h, and which was filmed "
        "inside his own documentary. The 207.4 ns that a synchronisation accumulates carried eastward "
        "around the equator, a number that is exactly zero on a stationary Earth (Ashby, <em>Living "
        "Reviews in Relativity</em> 6:1, 2003). Southern great-circle distances: Sydney–Santiago is "
        "11,347 km on the globe against 25,684 km across the azimuthal-equidistant disc, a factor of "
        "2.26, and the aircraft flies it nonstop. A ceiling can imitate a picture. It cannot imitate "
        "a flight time, a clock offset or a beat frequency. Nothing engaging any of these was located "
        "in the sources listed above. <strong>Two limits on that, stated rather than buried.</strong> "
        "The video series itself was not reached — no transcript of <em>Flat Earth Clues</em> was "
        "obtained — so it stands unchecked, not clear, and nothing here is a statement about its "
        "contents. And this is a record of what is not in the texts we read, not a claim that he has "
        "never addressed these things; he is living and still publishing, and the only account we "
        "found of his response to the December 2024 Antarctic observations is a partisan wiki whose "
        "wording we decline to repeat or rely on."),
    legacy=(
        "What descends from him is a delivery mechanism and an audience, and that is not a small "
        "thing. <em>Canadian Geographic</em>, covering the Edmonton conference, calls him “arguably "
        "the reason we are here” and dates the modern revival to the February 2015 upload; his "
        "channel stood at roughly 65,000–70,000 subscribers by early 2019, with view counts reported "
        "in the millions. <em>Behind the Curve</em> (2018, Netflix from February 2019) put him in "
        "front of an audience no zetetic text had ever reached, and both he and Patricia Steere "
        "reported their followings growing after it. He is the movement's onboarding artefact in "
        "person, which is what “recruiter” — his word, in preference to “father” — actually "
        "describes. What does <em>not</em> descend from him is arguments. Three of the 461 items "
        "(201–203: an electromagnetic firmament, a toroidal field, the Schumann resonance) were "
        "attributed to him in this dataset. That attribution was our hypothesis and it was tested on "
        "2026-08-10 against Sungenis & Bennett Vols I–II, Dubay's <em>200 Proofs</em>, and the two "
        "Sargent texts reachable without the video; it did not verify, and the recorded "
        "recommendation is to withdraw it to <em>untraced</em> rather than to substitute a guess. The "
        "nearest lead is that the Flat Earth Society interview does contain “I think its "
        "electromagnetic” — of gravity, not of the dome, three paragraphs after the dome answer. A "
        "fusion someone downstream may have performed is not a claim he made. His furniture does "
        "travel, but as vocabulary rather than as argument: eight items carry the word “dome” across "
        "six clusters, and items 408 and 409 bolt a dome onto a Victorian navigation claim whose own "
        "authors denied a southern pole outright — Carpenter's proof 11 — which this review records "
        "as an unsourced addition of 2015 vintage onto an 1885 argument. Beyond that, the specimen "
        "contains no ice wall, no Antarctica item and no enclosure item at all. The most visible face "
        "of the modern movement contributes, to the largest proof list we hold, not one distinct "
        "argument — and by his own account that was never the job he took."),
    kernel=dict(
        description=(
            "Two true things, and the first is the one people miss. He is right about propagation. "
            "Four hundred numbered assertions do not recruit anybody; a watchable serial narrative "
            "does, and he identified that in 2015 when the movement's own back catalogue had been "
            "sitting free and unread for a decade. This review's provenance data is evidence for his "
            "thesis, not against it — the list works by volume and vibe, and he understood that "
            "before we did. The second is the planetarium, and at full strength it is not crankery: "
            "you cannot, from inside a sufficiently good projection, distinguish it from the thing "
            "projected. That is the underdetermination problem, it is old and respectable, and it is "
            "the same structural move van der Kamp made on the Tychonian side without the cinema. He "
            "also states it with a candour that his own downstream does not inherit. “I did not "
            "invent flat Earth.” “If you can't get outside you're not going to know for sure.” Both "
            "are accurate, and both are more honest than the 461-item list built on top of him."),
        why_it_doesnt_save_claim=(
                "Because the planetarium argument is symmetric, and it reaches his side first. If a "
                "ceiling can produce any appearance, then sunsets, hulls vanishing bottom-first, star "
                "trails, the Bedford Level sightline and every celestial item on the specimen list "
                "are equally accounted for by it — and none of them is evidence for a disc. He has "
                "correctly identified that his model is undecidable from the inside, and then joined "
                "a movement whose entire output is inside evidence. The immunity is not even "
                "complete. Undecidability holds only for what a ceiling can display, and the ceiling "
                "is a display: it can render a picture, and it cannot render a dynamical quantity. "
                "The gyroscope beat, the eastward clock offset, the southern flight time are not "
                "pictures of the sky; they are measurements of the floor, taken from inside the room. "
                "One of them was taken inside his own documentary, by his own community, on camera, "
                "and it returned the globe's number to the degree. That is the thing his strongest "
                "argument cannot cover, and it is why the enclosure buys silence rather than support.")),
    sources=[
        dict(label="Wikipedia — Mark Sargent (flat Earth proponent)",
             url="https://en.wikipedia.org/wiki/Mark_Sargent_(flat_Earth_proponent)",
             note=(
                "birth c. 1968, Whidbey Island, three years at Western Washington University, "
                "StarPlay Productions, software training to 2014, the summer-2014 debunking attempt, "
                "the \"recruiter\" self-description, Strange World from 2015")),
        dict(label=(
                "Omar Mouallem, “Welcome to Flat Earth 101”, Canadian Geographic — dates the first "
                "upload to 10 February 2015, calls him “arguably the reason we are here”, describes "
                "him as a former software consultant and as the opening speaker at the Edmonton "
                "conference of August 2018"),
             url="https://canadiangeographic.ca/articles/welcome-to-flat-earth-101/"),
        dict(label=(
                "ABC News, 25 January 2018, from the Flat Earth International Conference, Raleigh NC, "
                "November 2017 — “I did not invent flat Earth …”; he declines “father” of the "
                "movement in favour of “recruiter”; “Everybody here can agree on absolutely one "
                "thing, which is [Earth] is not a globe”"),
             url="https://abcnews.com/US/inside-flat-earth-international-conference-believes-earth-round/story?id=52580041"),
        dict(label=(
                "ITV, This Morning — “We're living in a big sound stage with walls, and a floor”; the "
                "Truman Show comparison; “It's not necessarily an ice wall, it's just Antarctica, "
                "this really, really, really high continent”; “If you can't get outside you're not "
                "going to know for sure”"),
             url="https://www.itv.com/thismorning/articles/mark-sargent-the-man-who-says-the-earth-is-flat"),
        dict(label=(
                "Andrea Brown, “He's semi-famous for being flat-out wrong about Earth”, Everett "
                "Herald, 15 January 2019 — age 50, Whidbey Island, ~20 years in Colorado in games and "
                "tech support, ~70,000 subscribers, “The entire Apollo program is a fabrication”"),
             url="https://www.heraldnet.com/2019/01/15/hes-semi-famous-for-being-flat-out-wrong-about-earth/"),
        dict(label="“Flat Earth Clues",
             url="https://theflatearthsociety.org/home/index.php/blog/flat-earth-clues-mark-sargent",
             note=(
                "Exclusive Interview with Mark Sargent”, The Flat Earth Society — the dome via "
                "Genesis 1:6 and the planetarium analogy; enclosedworld.com; “I think its "
                "electromagnetic. I think its a molecular magnet that pulls things down”, said of "
                "gravity and not of the dome")),
        dict(label="Wikipedia — Behind the Curve (dir. Daniel J. Clark)",
             url="https://en.wikipedia.org/wiki/Behind_the_Curve",
             note=(
                "Hot Docs premiere 30 April 2018, US release 15 November 2018, Netflix February 2019; "
                "Sargent as principal subject; the film's experiments returning the globe's answer; "
                "both he and Steere reporting larger followings afterwards")),
        dict(label=(
                "Newsweek, 15 February 2019 — transcription of the ring-laser gyroscope sequence (a "
                "“15 degree per hour drift”) and the closing light-through-holes experiment"),
             url="https://www.newsweek.com/behind-curve-netflix-ending-light-experiment-mark-sargent-documentary-movie-1343362"),
        dict(label="Wikipedia — The Final Experiment",
             url="https://en.wikipedia.org/wiki/The_Final_Experiment_(expedition)",
             note=(
                "Union Glacier Camp, ~79°S, 14–17 December 2024, three days of continuous "
                "midnight-sun livestream, Campanella's concession, and the wider community's "
                "rejection of the footage. The article does not mention Sargent")),
        dict(label=(
                "Neil Ashby, “Relativity in the Global Positioning System”, Living Reviews in "
                "Relativity 6:1 (2003) — ECI synchronisation, and the 207.4 ns discrepancy "
                "accumulated by an eastward equatorial circumnavigation"),
             url="https://link.springer.com/article/10.12942/lrr-2003-1")]),

"PER-SKIBA": _p(
    name="Rob Skiba", dates="26 May 1969 – 13 October 2021",
    lineage="Zetetic",
    role=(
        "Carrier, not originator: the proximate route the scriptural proof-texts travelled into the "
        "modern lists, and the movement's most recent documented republisher of its own Victorians."),
    works=["WRK-SKIBA-2018"],
    bio_status="worked",
    formation=(
        "He did not come from science, and he did not come from the canal. A graduate of the "
        "Hollywood Film Institute, Skiba worked as a documentary filmmaker and self-published author, "
        "and was known for a decade before flat earth for something else entirely: <em>Archon "
        "Invasion: The Rise, Fall and Return of the Nephilim</em>, the <em>Babylon Rising</em> books, "
        "and the in-development <em>SEED</em> series. His conference biography describes him as an "
        "“ancient Nephilim theorist” bringing a perspective to the UFO question; he broadcast through "
        "Virtual House Church and Revolutionary Radio and wrote from a Torah-observant, "
        "King-James-reading position. Genesis 6 was the apparatus he already had, and Genesis 1 is "
        "next door. He gives the starting date himself: challenged on 13 April 2015 to prove the "
        "globe, he says he first tried to build a biblical case <em>for</em> a sphere — Isaiah 40:22, "
        "the standard apologetic verse — decided the text would not carry it, and worked outward from "
        "there. On his own account the shift was gradual rather than sudden: unconvinced, then "
        "roughly eighty per cent persuaded, then committed. He borrowed Rowbotham's word for the "
        "result and called the enterprise a <em>zetetic investigation</em>. The word is the whole "
        "inheritance, and it is worth noticing what changed in transit: Rowbotham's investigation "
        "began with an instrument at a six-mile canal and reached scripture late; Skiba's began with "
        "a concordance and reached the horizon afterwards. Both called it the same method. (On the "
        "record itself: this project's genealogy doc still lists Skiba's death under “NOT VERIFIED — "
        "do not publish as fact,” on the ground that only content-farm obituaries could be found. "
        "That was true when written and is no longer. Two dated, named sources were located on this "
        "pass — Danny Faulkner's memorial notice at Answers in Genesis, 14 October 2021, which "
        "supplies both dates, and contemporary reporting in <em>The Daily Beast</em>. Both give the "
        "cause as COVID-19 after weeks in hospital; Faulkner, who argued against him publicly, "
        "records only that “Rob always treated me kindly. He was a gentleman.” The stub's "
        "<code>active c. 2015–2021</code> should be replaced with the full dates.)"),
    had=(
        "More than a hostile reading would allow, and one thing almost nobody else in this dataset "
        "has. He had the Victorian corpus in the public domain and fully digitised, and rather than "
        "paraphrase it he <em>reprinted</em> it — <em>Testing the Globe</em> (Independently "
        "Published, 30 September 2018, 424 pp.) carries Rowbotham's <em>Zetetic Astronomy</em> and "
        "Carpenter's <em>100 Proofs</em> between covers with his own commentary, under a joint "
        "byline. He had real philology and used it correctly: <em>rāqîaʿ</em> as a beaten-out solid "
        "vault, <em>ḥûg</em> at Isaiah 40:22 as circle or vault rather than sphere, <em>bəlî-mâ</em> "
        "at Job 26:7 as a hapax. Those readings are not inventions; they track mainstream biblical "
        "scholarship — Seely in the <em>Westminster Theological Journal</em> reconstructs both the "
        "solid sky and the flat disc — and this review's own C04 treatment grants the case at full "
        "strength. He had Robert Schadewald's 1987 compilation, and here is the part that has to be "
        "said in a genre defined by unattributed recopying: <strong>he cited it</strong>. He named "
        "the essay and its author, printed the copyright line and the URL of the page hosting it, "
        "block-quoted several paragraphs and told readers to go and read the whole thing. He hedged "
        "in his own voice — <em>“I don't make any claims to having the definitive answer to this "
        "controversy”</em> — while stating the conclusion at full strength where he meant it: of Job "
        "38, <em>“If ever there was a Flat Earther, anti-globalist Scripture, this one is it.”</em> "
        "He built a three-dimensional rendering of his model rather than only asserting it, he "
        "answered the obvious objection to it, and he stood on a stage at the 2017 Flat Earth "
        "International Conference where his critics could reach him."),
    ignored=(
        "Not concealment — the opposite of it — and not the circle-versus-corners problem either, "
        "which he met head-on and answered with a circle inscribed into a square container, an answer "
        "he labelled speculation in his own text. Three things, all of them narrower and all of them "
        "inside documents he had open. <strong>First, the caveats in the essay he recommended "
        "whole.</strong> Schadewald files the foundations-and-pillars texts under a heading he calls "
        "<em>“Weaker Arguments”</em> and writes that <em>“No one would argue for a flat-earth solely "
        "on the basis of ‘foundations’ quotes”</em>; in the same essay he reports that Gerardus Bouw "
        "— the geocentrists' own credentialed astronomer — runs those very verses as evidence for "
        "<em>sphericity</em>. That is a non-discrimination result, published inside the movement, "
        "sitting in the document Skiba handed his readers. <strong>Second, the methodological rule "
        "stated in the same essay:</strong> that <em>“it is a grave error to reinterpret ancient "
        "documents to force their authors to speak with modern voices.”</em> That sentence is the "
        "precise objection to the step his argument needs, written by the man who assembled the "
        "proof-text set he was using. <strong>Third, a criterion of his own, unapplied "
        "evenly.</strong> He is right that <em>bəlî-mâ</em> is a hapax, and he builds a "
        "two-or-three-witnesses rule on it (2 Cor 13:1) to keep Job 26:7 from carrying weight alone. "
        "Run that rule on his own lead pillars text and it goes badly: 1 Samuel 2:8's <em>məṣuqê</em> "
        "occurs twice in the Hebrew Bible, and the other occurrence is a rock crag. <strong>Scope, "
        "and it matters here more than usual.</strong> These are absences in the 2015–16 teaching PDF "
        "<em>The Bible and the Still Flat Earth</em>, in Schadewald 1987, and on testingtheglobe.com "
        "— the documents this review could search. The 424-page 2018 book is in copyright and its "
        "full text was not searchable. So the claim is <em>not located in what we could read</em>, "
        "never <em>he never answered it</em>."),
    legacy=(
        "Thirty-eight of the 461 items touch him, more than any zetetic-lineage figure except "
        "Rowbotham — but the two halves of that number mean different things, and the distinction is "
        "this record's whole point. Twenty-two items are credited to him as <em>originator</em>: C03 "
        "foundations and pillars (6), C04 firmament and dome (9), C05 circle and four corners (7). "
        "Sixteen more are C02, the sun-motion proof-texts, where the dataset records him not as an "
        "author but as a repopulariser — “the proximate route these sixteen items travelled into the "
        "modern flat-earth compilations.” <strong>What actually descends from him is distribution, "
        "not authorship.</strong> The firmament and foundations sets were assembled in print in July "
        "1987 by Robert Schadewald, a debunker and later president of the National Center for Science "
        "Education, writing in the <em>Bulletin of the Tychonian Society</em> to tell geocentrists "
        "their proof-texts proved more than they wanted; Schadewald in turn reports earlier compilers "
        "— Rowbotham's seventy-six scriptures in the second edition of <em>Earth Not a Globe</em>, "
        "and Anton Darms, Voliva's assistant, in 1930. Skiba carried that corpus forward with the "
        "credit attached; the compilers downstream of him carried it forward without. What is "
        "genuinely his is the republishing act: putting Rowbotham and Carpenter back into print under "
        "a shared cover in 2018 is structurally the same move as Voliva's 1929 Zion reprint of "
        "Carpenter, and it is the mechanism this whole review documents — the canon travels by "
        "republication, not by new observation. <strong>What merely resembles him is being read as "
        "its author, and this project has made that mistake itself.</strong> C02's originator was "
        "moved from Carpenter to Skiba on 2026-08-02 and withdrawn entirely on 2026-08-09, once "
        "Bellarmine's letter of 12 April 1615 turned up deploying Ecclesiastes 1:5 against "
        "Copernicus. The identical correction is still outstanding on C03, C04 and C05, where "
        "<code>clusters.py</code> continues to credit him with a corpus the review's own treatments "
        "trace to 1987 and earlier. <strong>And one thing of his did not descend at all.</strong> The "
        "square container that reconciles the circle with the four corners — his construction, "
        "offered as speculation — appears in none of the seven C05 items. The list kept the verses "
        "and dropped the container, which is the clearest case on the site of a qualifier stripped in "
        "transit."),
    kernel=dict(
        description=(
            "The philology is right, and it is mainstream. The <em>rāqîaʿ</em> of Genesis 1 was a "
            "solid vault to the people who wrote it; <em>ḥûg</em> at Isaiah 40:22 means circle, vault "
            "or horizon, not sphere, and Hebrew had a word for a ball — <em>kaddûr</em> — which "
            "Isaiah used fourteen chapters earlier and did not use here. That reconstruction belongs "
            "to Paul Seely in the <em>Westminster Theological Journal</em>, not to a flat-earth "
            "pamphlet, and the sharpest published attack on the opposing “circle must mean sphere” "
            "apologetic came from Schadewald, a career critic of flat-earthism, who called Henry "
            "Morris's version poor scholarship. On this specific point the person telling Skiba he is "
            "inventing his Hebrew is the one out of step with the journals. The second true thing is "
            "rarer and is worth as much: <strong>he cited his source, named it, dated it, printed its "
            "URL and sent his readers to the original</strong> — in a genre that recopies without "
            "attribution, and by a compiler who had every incentive not to reveal that his proof-text "
            "set came from a debunker."),
        why_it_doesnt_save_claim=(
                "Where it points is the problem. What the philology establishes is what ancient "
                "writers <em>pictured</em>, not what a drill or a seismograph will <em>find</em>; the "
                "step between is supplied by the modern reader, and it is the exact step his own "
                "cited source calls a grave error. Foundations and firmaments are in any case claims "
                "about the sky and the underworld rather than about the shape of the ground — Bouw "
                "ran the same verses for a <em>sphere</em>. And the closing argument is Skiba's own. "
                "His conclusions page says he has far more questions than answers, that he cannot "
                "demonstrate the conspiracy he suspects, and that <em>“even if all I've said here is "
                "totally debunked, I'm still going to have to put my faith on the side of "
                "Scripture.”</em> Whether that is the right commitment to hold is outside this "
                "review's domain and stays there — the page has nothing to say about it in either "
                "direction. What it settles is narrower and decisive: the man these thirty-eight "
                "items descend from had already said, in print, that his position does not rest on "
                "them. That is the same admission Bouw made from the Tychonian side, reached "
                "independently. <strong>Both engines of this movement concede that the case is not "
                "evidential, and the lists built from them are circulated as evidence.</strong>")),
    sources=[
        dict(label="Danny Faulkner, “Rob Skiba",
             url="https://answersingenesis.org/blogs/danny-faulkner/2021/10/14/rob-skiba/",
             note=(
                "May 26, 1969 – October 13, 2021”, Answers in Genesis, 14 October 2021 — the source "
                "of both dates and of the cause of death")),
        dict(label="“Flat Earth Preacher Rob Skiba Dies of COVID-19”, The Daily Beast, October 2021",
             url="https://www.thedailybeast.com/flat-earth-preacher-rob-skiba-dies-of-covid-19/"),
        dict(label=(
                "Rob Skiba, “The Bible and the Still Flat Earth” (© 2015–2016) — the teaching "
                "document actually quoted in ARG-C03, C04 and C05; contains the Schadewald block "
                "quotation with copyright line and URL, the “Pillars of the Earth” section, the "
                "beli-mah / two-witnesses argument, and the circle-inscribed-in-a-square model"),
             url="https://s3.amazonaws.com/mychurchwebsite/c4890/the_bible_and_the_still_flat_earth_rob_skiba.pdf"),
        dict(label="testingtheglobe.com — Skiba's own site (King's Gate Media LLC)",
             url="https://www.testingtheglobe.com/",
             note=(
                "the 13 April 2015 challenge, the “not convinced → about 80% → committed” "
                "progression, and the site's self-description as a work in progress")),
        dict(label=(
                "testingtheglobe.com, “Conclusions” — “If anything, I have far more questions than I "
                "do answers”; “even if all I've said here is totally debunked, I'm still going to "
                "have to put my faith on the side of Scripture”"),
             url="http://testingtheglobe.com/conclusions.html"),
        dict(label=(
                "Robert Schadewald, “The Flat-Earth Bible”, Bulletin of the Tychonian Society 44 "
                "(July 1987) — the page Skiba cites by URL"),
             url="https://dsimanek.vialattea.net/febible.htm",
             note=(
                "the “Weaker Arguments” heading, “No one would argue for a flat-earth solely on the "
                "basis of ‘foundations’ quotes”, the report of Bouw citing the same verses for "
                "sphericity, and “a grave error to reinterpret ancient documents…”")),
        dict(label=(
                "Schadewald, “The Flat-Earth Bible” — second full text, used to cross-check every "
                "quotation above"),
             url="https://www.cantab.net/users/michael.behrend/ebooks/PlaneTruth/pages/Appendix_A.html"),
        dict(label="Testing the Globe",
             url="https://books.google.com/books/about/Testing_the_Globe.html?id=7JU6vQEACAAJ",
             note=(
                "A Zetetic Investigation — catalogue record: Rowbotham, Carpenter and Skiba as "
                "authors; Independently Published, 30 September 2018; 424 pp.; ISBN 9781724119049; "
                "described as combining Zetetic Astronomy and 100 Proofs with Skiba's commentary")),
        dict(label=(
                "Flat Earth International Conference speaker page — Hollywood Film Institute, "
                "documentary filmmaker, Archon Invasion, Babylon Rising, SEED the series, “ancient "
                "Nephilim theorist”"),
             url="https://flatearthconference.com/speakers/rob-skiba/"),
        dict(label="Paul H. Seely, “The Firmament and the Water Above, Part I",
             url="https://thedivinecouncil.com/seelypt1.pdf",
             note=(
                "The Meaning of rāqîaʿ in Gen 1:6–8”, Westminster Theological Journal 53 (1991) — the "
                "scholarship the kernel's philological concession rests on")),
        dict(label=(
                "Robert Schadewald — later president of the National Center for Science Education; a "
                "critic of flat-earthism, not an advocate"),
             url="https://en.wikipedia.org/wiki/Robert_Schadewald")]),

"PER-KNODEL": _p(
    name="Robert “Bob” Lawrence Knodel", dates="6 November 1960 – 6 April 2023",
    lineage="Zetetic",
    role=(
        "Carrier, not originator — the gyroscope argument was already being debunked in public two "
        "years before he filmed it. What is his is the test: the movement's one instrumented "
        "measurement of the Earth's rotation, bought and run at his own expense."),
    works=["WRK-BTC-2018"],
    bio_status="worked",
    formation=(
        "He came at this from the opposite direction to Rowbotham, and the order matters. Rowbotham "
        "began with an apparatus — six straight miles of Fenland canal — and built a cosmology out of "
        "what he saw in it. Knodel began with a settled position about institutions and acquired the "
        "apparatus thirteen years later. The only account of his route in that we have from him is "
        "his own conference biography, a self-description hosted by the Flat Earth International "
        "Conference organisers and therefore evidence of what the movement says about itself rather "
        "than documentation of what happened: it describes him as an active member of the truther "
        "community since 9/11, says he had researched “conspiracy theories” for over twenty years, "
        "and that he concluded most of them “go far into the realm of conspiracy fact.” Flat Earth "
        "arrives downstream of that conclusion, not upstream of it — which places him in Charles K. "
        "Johnson's line of descent (the astronomers are lying, not mistaken) rather than in "
        "Rowbotham's, whatever the instrument on the bench. On 25 July 2015 he and Jeran Campanella "
        "launched the YouTube channel GlobeBusters, and his standing role there, by that same bio, "
        "was to present “the more technical aspects” — the engineering seat. He was born in Denver, "
        "Colorado and died at Spartanburg Regional Medical Center, South Carolina; a funeral-home "
        "notice gives both dates, names him a United States Air Force veteran, a Microsoft and Novell "
        "certified engineer with an associate's degree who “enjoyed research and physics,” and "
        "directs mourners to <em>flatearthfestivals.com</em> for the memorial arrangements, which is "
        "what identifies it as the same man. <strong>This page's own record had him as “active "
        "2015–”. That was wrong and is corrected here.</strong> He stated the significance motive "
        "himself, to a newspaper in 2022 — “The bottom line is that there is a creator. This place "
        "was made for us. We are special” — and it is quoted because he said it. Nothing about motive "
        "is inferred for him or for anyone else on this page."),
    had=(
        "More than anyone else in this dataset, and it should be said plainly. Every other modern "
        "name on the People tab argues from books, videos and other people's data; Knodel bought an "
        "instrument. It was an optical gyroscope of navigation class — the film has him call it a "
        "laser ring gyroscope, a 2022 newspaper profile calls it a fiber optic gyroscope, and no make "
        "or model has been located, but either is a Sagnac-effect device with no rotor and no "
        "bearings, which is exactly the right class for the job. It cost about $20,000, and the "
        "figure is mentioned here only because the money is the measure of the seriousness. He also "
        "had the correct quantity and an unambiguous two-way prediction: a gyroscope bolted to a "
        "stationary Earth senses zero rotation with respect to inertial space, one bolted to a "
        "turning Earth senses 15.041° per hour, and no interpretation stands between the two. And he "
        "had a real engineering objection to run it against — the one carried by items 225 and 374 on "
        "the specimen list, that a deployed inertial navigation system does not <em>measure</em> the "
        "Earth's rotation but is <em>given</em> an Earth-rate term computed from a stored latitude, "
        "and has its position reset from GPS. That objection is correct about the hardware, and the "
        "popular reply that the platform in your airliner proves the Earth spins is circular. The "
        "right way to close a hole like that is to obtain the sensor, bypass the navigation solution "
        "and read the raw sensed rate. That is what he did. When the reading came back at the value "
        "his model excluded, he ran a control — enclosing the apparatus against magnetic fields, on "
        "the hypothesis of an outside influence — which is what any laboratory does with an unwelcome "
        "number and is not a criticism. Then he said the number out loud, on film, to an audience "
        "that did not want it. Against the standard of this list, where the median cited experiment "
        "dates from 1933, that is the whole of the modern evidential effort."),
    ignored=(
        "Not the result — he engaged it twice, and the honest finding is narrower and more useful "
        "than “he looked away.” What is missing is a decision rule and a discriminating test. First, "
        "no acceptance criterion has been located: a statement, made before the run, of which reading "
        "would count as confirmation and which as refutation. We have not viewed the full film and "
        "cannot say whether one was given elsewhere in it; what the press transcriptions cover does "
        "not contain one, and without it a reading has nowhere to go in either direction. Second, and "
        "this is the concrete gap, three tests separate an instrument's own bias from the Earth's "
        "rotation and all three are geometric and free: reverse the azimuth 180° and the sensed "
        "Earth-rate component changes sign while a bias does not; tilt the input axis from vertical "
        "to horizontal-east and the component goes to zero; carry the box a few degrees of latitude "
        "and a vertical-axis reading scales as sin φ. None of the three is described in any account "
        "of the sequence located for this entry. Magnetic shielding, which was tried, is not among "
        "them and could not have been: the Sagnac output depends on enclosed area, wavelength and "
        "rotation rate, and an external field is not a term in it — so the control that was run was a "
        "good control of the wrong hypothesis. Third, his settled later answer, given to a reporter "
        "in 2022, is that the rotation is real but belongs to the luminiferous aether rather than to "
        "the Earth. That is a reinterpretation, not a measurement, and it leaves an objection "
        "standing that has not been answered anywhere we have located: an aether whose circulation "
        "happens to match the sidereal day would have to match it to the nine digits the large ring "
        "lasers at Wettzell reach, and to track length-of-day variation and polar motion in agreement "
        "with VLBI, a wholly different technique — and the Sagnac expression he is relying on "
        "contains no medium in its statement at all. Fourth, and separately from the gyroscope: the "
        "astronomer Danny Faulkner, a critic writing from a young-earth creationist ministry, "
        "attended the November 2018 Denver conference and published arithmetic against two of "
        "Knodel's other arguments there — that a Sun moved to one light-day away would be invisible, "
        "and that the Moon should blind an approaching astronaut. Faulkner ran the inverse-square and "
        "angular-size numbers and got the opposite answer both times. No reply to Faulkner by Knodel "
        "was located in the searches run for this entry, which are the ones listed below; that is a "
        "statement about our searches, not about the record."),
    legacy=(
        "Almost nothing descends from him as argument, and that is the point of the entry. Five of "
        "the 461 items — 12, 19, 112, 225 and 374 — sit in the one cluster our dataset attributes to "
        "him, and the argument itself was not his: a gyroscope video making the same case was already "
        "being taken apart on the Metabunk forum on 20 March 2016, two years before the film, with no "
        "flat-Earth personality named in the thread. He inherited a claim and did the thing nobody in "
        "the tradition had done with it. What actually travels from him is the <em>number</em>, and "
        "it travels to the other side. “A 15 degree per hour drift” is now standard material in "
        "debunking write-ups; a Metabunk member reported in January 2020 that he had repeated it with "
        "three aeroplane gyroscopes and got the same figure every time (a forum post, not a paper); "
        "and the movement-internal Flerf Wiki — community-edited, not scholarship — records the "
        "phrase “Thanks Bob” circulating as a result. Meanwhile item 12 of the specimen list, "
        "“Gyroscope anomalies indicating no rotation,” asserts the reverse of what his instrument "
        "read: the list kept the argument and discarded the experiment. Inside the movement, what "
        "descends is the aether reading. That move — keep the measured rotation, reassign it to a "
        "medium turning around a stationary Earth — is the same move Sungenis and Bennett make with "
        "Michelson–Gale, whose own text offers the disjunction “the effect of the Earth's rotation "
        "<em>or</em> the ether's rotation around the Earth.” We have not found that Knodel took it "
        "from them and do not claim he did; he cited Michelson directly, which is the shared "
        "ancestor. Call it convergence, not descent. One more thing that is a fact about people "
        "rather than about arguments: Jeran Campanella, who co-founded GlobeBusters with him on the "
        "same day in 2015, went to Union Glacier in December 2024, watched the Sun fail to set for "
        "three days, and conceded on camera that his model was no longer valid — while part of the "
        "community called the footage faked. Same channel, same class of failed prediction, opposite "
        "response. Finally, and this belongs on the record: Knodel told a reporter in 2022 that after "
        "the film he received death threats and lost job contracts. That is his account, and it is "
        "the reason the disclaimer at the top of this page has to mean something. This review is "
        "about five list items and one instrument reading. It is not about him."),
    kernel=dict(
        description=(
            "He is the only person in this dataset who turned a claim into an instrumented "
            "measurement at his own expense and then published the number. The objection he was "
            "testing is genuinely correct: a deployed inertial navigation system has the Earth-rate "
            "term supplied to it from a stored latitude and is reset from GPS, so anyone who answers "
            "this cluster by pointing at an airliner has argued in a circle. The correct repair is to "
            "strip the presupposition out and read the raw sensor — obtain a Sagnac-effect gyroscope, "
            "bypass the navigation solution, look at the rate. That is better method than the list "
            "contains anywhere else, and better than the debunk it was aimed at. He then ran a "
            "systematics check when the answer displeased him, which is what laboratories do, and "
            "reported the reading anyway to people who did not want it. Take the zetetic instruction "
            "seriously — go and look, take nothing on authority — and this is what following it looks "
            "like in 2018."),
        why_it_doesnt_save_claim=(
                "Because the argument nominated the test, the test was the right one, and it returned "
                "the value the argument requires to be zero. Everything after that is a matter of "
                "what you do with a result, and the two things that were done — shield the box, then "
                "reassign the rotation to an aether — are respectively a control on a hypothesis the "
                "physics excludes (an external field is not a term in Δf = 4A·Ω/λL) and a "
                "reinterpretation that makes the apparatus stop being a test of anything. A reading "
                "you keep but re-label cannot discriminate, and the same instrument class scaled up "
                "at Wettzell resolves the Earth's rate to one part in 10⁹ and agrees with VLBI on "
                "polar motion. What is missing is not equipment, effort or nerve; it is the sentence "
                "stating in advance which outcome would count as refutation. The most accurate line "
                "in the whole cluster is his own, said to a reporter three years later with the irony "
                "fully intended: he has “the dubious distinction of being the only person in the "
                "world that proved the Earth's rotation.”")),
    sources=[
        dict(label=(
                "Roberts Funeral Home, Spartanburg SC — obituary of Robert “Bob” Lawrence Knodel, b. "
                "6 Nov 1960, d. 6 Apr 2023; USAF veteran; Microsoft and Novell certified engineer; "
                "memorial 15–16 April 2023"),
             url="https://www.robertsfhsc.com/obituary/RobertBob-Knodel"),
        dict(label=(
                "Tribute Archive mirror of the same obituary — adds birth in Denver, Colorado and the "
                "memorial link to flatearthfestivals.com"),
             url="https://www.tributearchive.com/obituaries/32040258/robert-%22bob%22-lawrence-knodel"),
        dict(label=(
                "Flat Earth International Conference 2018 (Denver, 15–16 November) — Knodel speaker "
                "biography"),
             url="https://fe2018.com/speakers/bob-knodel/",
             note=(
                "engineering claims, “truther” route in, GlobeBusters founded 25 July 2015 with Jeran "
                "Campanella")),
        dict(label="FEIC speaker page (2019 sessions",
             url="https://flatearthconference.com/speakers/bob-knodel/",
             note=(
                "“Globebusters LIVE”, 14 Nov; “Scientific Breakdown”, 15 Nov) — a slightly different "
                "version of the same self-description")),
        dict(label=(
                "Loren Bienvenu, “Flatter Day Saints”, Santa Fe Reporter, 24 January 2022 — “IT "
                "contractor with an engineering background”; “$20,000 fiber optic gyroscope”; the "
                "luminiferous-aether reinterpretation citing Michelson; the “dubious distinction” "
                "line; his stated creator/significance motive; his account of death threats and lost "
                "contracts"),
             url="https://sfreporter.com/coverstories/flatter-day-saints/"),
        dict(label=(
                "Andrew Whalen, Newsweek, February 2019 — transcription of the “15 degree per hour "
                "drift” line and the closing light-through-holes experiment"),
             url="https://www.newsweek.com/behind-curve-netflix-ending-light-experiment-mark-sargent-documentary-movie-1343362"),
        dict(label="Metabunk, “Debunked",
             url="https://www.metabunk.org/threads/debunked-gyro-experiment-proves-motionless-earth.7413/",
             note=(
                "Gyro Experiment — Proves Motionless Earth?”, opened by Z.W. Wolf, 20 March 2016 — "
                "the gyroscope argument in circulation and under rebuttal two years before the film; "
                "no flat-earth creator named in the thread")),
        dict(label=(
                "Same thread, page 2 — Z.W. Wolf posts the Knodel quote (1 Dec 2018) with the "
                "zero-gauss and bismuth follow-ups; member “Jesse3959” reports (30 Jan 2020) "
                "repeating the measurement with three aircraft gyroscopes and getting 15°/hour each "
                "time"),
             url="https://www.metabunk.org/debunked-gyro-experiment-proves-motionless-earth.t7413/page-2"),
        dict(label=(
                "Danny Faulkner, report on the Second Flat Earth International Conference (Denver, "
                "15–16 November 2018), 14 December 2018 — arithmetic against Knodel's "
                "Sun-at-one-light-day and lunar-brightness arguments"),
             url="https://answersingenesis.org/blogs/danny-faulkner/2018/12/14/second-flat-earth-international-conference/"),
        dict(label=(
                "Behind the Curve — dir. Daniel J. Clark; Hot Docs premiere 30 April 2018, US release "
                "15 November 2018, Netflix February 2019"),
             url="https://en.wikipedia.org/wiki/Behind_the_Curve"),
        dict(label=(
                "The Final Experiment, Union Glacier, Antarctica, 14–17 December 2024 — Jeran "
                "Campanella's on-camera concession and the community's rejection of the footage"),
             url="https://en.wikipedia.org/wiki/The_Final_Experiment_(expedition)"),
        dict(label=(
                "Flerf Wiki — “fiber optic gyroscope”, death 6 April 2023 aged 62, memorial "
                "livestream 16 April 2023, the “Thanks Bob” phrase, FE Core"),
             url="https://www.flerf.info/index.php/Bob_Knodel"),
        dict(label="Flat Earth Society forum thread, “Globebusters' Bob Knodel Passed Away”",
             url="https://forum.tfes.org/index.php?topic=19973.0")]),

"PER-BOUW": _p(
    name="Gerardus Dingeman Bouw", dates="15 March 1945 – 4 November 2023",
    lineage="Tychonian",
    role=(
        "Van der Kamp's successor: edited the movement's journal from 1984, renamed the society 1991. "
        "Carrier and cited authority rather than originator — credited here with 2 of 98 arguments, "
        "both provisionally."),
    works=["WRK-BOUW-1992"],
    bio_status="worked",
    formation=(
        "Born at Sliedrecht in South Holland on 15 March 1945, during the famine at the end of the "
        "German occupation; the family emigrated to Canada in 1952, landing at Halifax, and then to "
        "the United States — Torrance, California, and two years later Rochester, New York. He "
        "entered the University of Rochester at eighteen and took a B.S. in astrophysics in 1967, "
        "becoming an atheist during the degree; a Ph.D. in astronomy followed from Case Western "
        "Reserve University in 1973, into a post-Apollo job market that left him, in his own phrase, "
        "“massively unemployable.” <strong>The order of events is the thing most short accounts get "
        "backwards, and it matters.</strong> The underdetermination premise came first, and it came "
        "out of the physics rather than the theology: writing of his undergraduate years he says he "
        "had “taken enough relativity theory to know that neither heliocentrism nor geocentricity "
        "could be proven or disproven.” That is the proposition he would spend the next forty years "
        "defending, and he reached it before he was a believer of any kind. The rest followed in a "
        "documented sequence — conversion at Rochester on 26 January 1975; young-earth creationism by "
        "way of a Duane Gish tract; membership of the Creation Research Society; and in early 1976 a "
        "note by Harold Armstrong in the <em>Creation Research Society Quarterly</em> naming Walter "
        "van der Kamp as an extreme case. Bouw wrote to van der Kamp asking, in effect, <em>which "
        "Scriptures?</em>, judged the answer weak, ran a three-week study of his own and printed the "
        "result in the <em>Bulletin of the Tychonian Society</em> no. 13 in 1976. Nearly all of this "
        "comes from one document — his signed <em>Testimony</em> on his own organisation's website, "
        "which is a self-published autobiographical account by the subject and is movement-internal. "
        "It is evidence of what he said about himself. Where it is checkable from outside (the Ph.D., "
        "the dates, the Rochester and Cleveland moves) it checks out; his motives are reported here "
        "only because he stated them."),
    had=(
        "More than anyone else in this dataset, and he used it. An earned doctorate in astronomy from "
        "a research university, a teaching post at Cleveland State from 1977 and a professorship at "
        "Baldwin-Wallace College from 1980. He turned the training on his own side first: against van "
        "der Kamp's 60-light-day universe he pointed out that stellar diameters are measurable by "
        "interferometry, so that at forty light-days “many of the stars would be earth-sized or "
        "larger” — and he refused the small cosmos, rebuilding the Tychonic model instead so that the "
        "stars accompany the Sun in its yearly motion, which keeps both aberration and parallax. He "
        "printed his critics at length: George Mulfinger's letter to the Creation Research Society "
        "board, arguing that a geostationary satellite over a motionless Earth would have to fall, is "
        "reproduced in his own book — and Bouw's reply is correct textbook physics, that a body "
        "holding a constant distance from the axis of rotation feels no Coriolis term. He knew the "
        "technical Machian literature by name and cited it: Thirring, Birkhoff, Moon and Spencer, "
        "Rosser, Assis, and Barbour and Bertotti's <em>Gravity and Inertia in a Machian "
        "Framework</em> (<em>Il Nuovo Cimento B</em> 38:1, 1977). Robert Schadewald, a hostile "
        "witness who spent decades documenting this movement, called Bouw's books “the most "
        "sophisticated defenses of geocentricity ever published, and the only ones written by an "
        "astronomer with a Ph.D. from a first-class university.”"),
    ignored=(
        "Very little that he never looked at. The gap is at the point where looking further would "
        "have cost him something, and there are two of them. <strong>First, the apparatus he had and "
        "did not run.</strong> His claim is not that the Earth-fixed frame is a legal relabelling; it "
        "is that a physical medium does the work. The firmament, he writes, is “a superdense medium "
        "that pervades all of space,” and “it is the firmament that physically controls all motion” "
        "(2013 ed., p. 5); at p. 523 he says geocentricity <em>predicts</em>. A medium that controls "
        "motion has field equations, and he was trained to write them. Appendix E — checked against "
        "page images for this project in August 2026 — derives the rotating-frame accelerations, "
        "multiplies through by the mass to get F = ma, applies that to sun, moon, planets, artificial "
        "satellites, stars and the propagation of light, and stops. No metric, no stress-energy "
        "tensor, no cosmological solution: nothing to fit, and so nothing that could come back wrong. "
        "The Machian papers he names do not close the gap either — Barbour and Bertotti's relational "
        "dynamics, which he calls the most successful of them, abolishes absolute space rather than "
        "awarding the centre to anybody. He concedes the residual himself at p. 556, and the "
        "concession is honest: the Milky Way “could just as well be viewed as located at the center "
        "of the cosmic shells we examined in this chapter; and the earth is not exactly at the center "
        "of the F-stars and G-stars, either. But that is where Scripture comes into play.” That is an "
        "answer rather than an evasion, and by his own placement of it, it sits outside the testable "
        "domain. His stopping rule is stated in his own voice at chapter 31: “our defense of "
        "geocentricity does not require us to understand all there is about aberration. We only need "
        "to show that geocentricity is consistent with what we do know about aberration.” Consistency "
        "is a lower bar than discrimination, and he never pretends otherwise. <strong>Second, and "
        "narrowly scoped:</strong> two measurement programmes bearing directly on the mechanism he "
        "invokes are not present in his last edition. A full-text search of the Internet Archive OCR "
        "of <em>Geocentricity: Christianity in the Woodshed</em> (2013, ISBN 9781890120900) returns "
        "no occurrence of “Gravity Probe”, “frame drag”, “ring laser”, “GPS” or “Global Positioning”, "
        "against 36 occurrences of “Sagnac” and six of “Michelson-Gale”. Gravity Probe B's final "
        "result — frame dragging by a rotating Earth, −37.2 ± 7.2 mas/yr, <em>PRL</em> 106:221101 — "
        "was published in 2011, two years before that edition, and it is a measurement of the "
        "gravitomagnetic effect on which his answers to Foucault and to Coriolis depend; the large "
        "ring-laser gyroscopes now run the Sagnac experiment some nine orders of magnitude better "
        "than the 1925 apparatus he does discuss. This is an absence in one edition of one book as "
        "searched here, not a claim about what he knew: he cites Thirring by name, so he plainly knew "
        "the effect existed."),
    legacy=(
        "Carried forward, and traceable. The modified Tychonic model — stars moved onto the Sun's "
        "annual motion so that aberration survives — is Bouw's correction of van der Kamp, made over "
        "van der Kamp's objection, and it is the version modern geocentrists actually use. The word "
        "<em>geocentricity</em> is his term of art and it does not mean what most people who repeat "
        "it think: “In geocentricity, the earth is static, but not necessarily at the center of the "
        "universe,” he writes; it is a claim about immobility, not centrality. Institutionally he is "
        "the whole apparatus — editor of the <em>Bulletin</em> from 1984, then the Association for "
        "Biblical Astronomy and <em>The Biblical Astronomer</em> (his own society's history says "
        "January 1991; Schadewald says 1990, and the conflict is unresolved). He wrote van der Kamp's "
        "obituary, which is where “Airy's failure” appears as settled vocabulary and where “the "
        "father of modern geocentricity” comes from. Sungenis and Bennett quote his "
        "Venus-and-epicycles answer verbatim from <em>Geocentricity</em> (1992), pp. 309–310 — "
        "fourteen years before the year this project records for that cluster — and thank him in a "
        "footnote at Vol. I p. 365; Malcolm Bowden's account, printed in Bouw's own book, credits "
        "Bouw's books with convincing him. <strong>What does not descend from him is the flat "
        "Earth.</strong> Five of the 461 items are credited to him — three in R11, two in E12 — and "
        "both credits are marked provisional in this project's own files: R11's doctrine is his in "
        "print but he attributes the proposition to “the more subtle physicists”, and E12's "
        "vocabulary is Sungenis and Bennett's, with the only documented Bouw instance later than "
        "1992. He is named in the rosters of 14 of the 98 arguments and originates at most two of "
        "them, which is the shape of a cited authority rather than a source. And the authority being "
        "cited held the Earth to be a globe: his chapter 3 is titled “The Bible and the Flat Earth”, "
        "argues that Scripture was “already referring to the sphericity of the earth some 500 years "
        "before the Greeks first thought to question the flatness of the earth”, and answers Robert "
        "Schadewald by name on the flat-earth reading of Luke 17. A flat-earth list quoting Bouw is "
        "quoting a book with a chapter against it."),
    kernel=dict(
        description=(
            "The strongest form of Bouw's position is neither the Bible nor the interferometers. It "
            "is this: a coordinate change to an Earth-fixed frame is exact and legal, and the step by "
            "which textbook physics moves from a kinematic description to a dynamical one — his "
            "complaint at p. 4 that all one does is multiply through by m/m — genuinely does not, by "
            "itself, confer physical content. What picks out the inertial frames is a fact about the "
            "whole matter distribution, and that is Mach's question rather than a settled result. He "
            "is on real ground when he says the Machian programme is real physics: Einstein named the "
            "principle and took it seriously, Lense and Thirring computed the interior field of a "
            "rotating shell in 1918, Barbour and Bertotti published a relational dynamics in 1977, "
            "and frame dragging has since been measured. His hedge at p. 5 is the honest form of the "
            "whole book — Mach's principle, he says there, “makes geocentricity as plausible as any "
            "other center.” Anyone answering him by denying that a null result underdetermines the "
            "model will lose, because that principle is ours too."),
        why_it_doesnt_save_claim=(
                "A Machian cosmos is quantitative: the shell's mass and rotation rate fix the size of "
                "the dragging, and Pfister and Braun (<em>Class. Quantum Grav.</em> 2:909, 1985) had "
                "to add the shell's own stresses before a rotating shell reproduced the centrifugal "
                "force exactly. Numbers of that kind can fail, which is precisely what makes them "
                "evidence — and Appendix E ends before any of them. The tension is inside his own "
                "book rather than only inside the list: the same volume says that every fundamental "
                "experiment measures a speed of zero and that the geocentric evidence is "
                "overwhelming, and then that dynamical proofs “are not proofs of anything; nor are "
                "they proofs against the geocentric universe.” The specimen list banks the second "
                "sentence as proof number 293 while spending the first everywhere else. Taken "
                "symmetrically — the way he states it at p. 747 — the claim is fatal to the list that "
                "quotes him, because if no experiment discriminates then Airy, Michelson–Morley, "
                "Michelson–Gale and the microwave-background items are not evidence for anybody. And "
                "where the astronomy runs out, at the gap between the Earth and the Milky Way, he "
                "says in plain words what closes it, and it is not an instrument.")),
    sources=[
        dict(label=(
                "Bouw, “Testimony of Gerardus Dingeman Bouw”, Association for Biblical Astronomy — "
                "the source for birth, emigration, degrees, conversion and the 1976 approach to van "
                "der Kamp"),
             url="https://www.geocentricity.com/bibastron/bouw_bio.html"),
        dict(label="Bouw, GEOCENTRICITY",
             url="https://archive.org/details/geocentricity-christianity-in-the-woodshed",
             note=(
                "CHRISTIANITY IN THE WOODSHED (Association for Biblical Astronomy, 2013, ISBN "
                "9781890120900) — the 2013 retitling of Geocentricity (1992); all page locators here "
                "are to its Internet Archive OCR, not to a print copy")),
        dict(label="Bouw, “GEOCENTRICITY",
             url="https://www.geocentricity.com/~geocent1/ba1/fresp/index.html",
             note=(
                "A Fable for Educated Man?” — his reply to Faulkner; source of “can both account for "
                "the observed motions”, of the geocentricity-vs-geocentrism distinction, and of “The "
                "issue is final authority”")),
        dict(label="Association for Biblical Astronomy — society history",
             url="https://www.geocentricity.com/bibastron/index.html",
             note="van der Kamp hands over the Bulletin in 1984; renamed “In January of 1991”"),
        dict(label=(
                "Gerardus “Gerry” Dingeman Bouw, obituary, 4 November 2023 — Sliedrecht birth, death "
                "at Conneaut, Ohio, retired Professor of Computer Science at Baldwin-Wallace"),
             url="https://www.lakeeriecremationandfuneralservices.com/obituaries/gerardus-dingeman-bouw"),
        dict(label=(
                "Faulkner, “Geocentrism and Creation”, Journal of Creation 15(2):110–121 (2001) — "
                "“the essential difference between the heliocentric and Tychonian models is a "
                "co-ordinate change from the Sun to the Earth”. THIS is the correct Faulkner "
                "citation; creation.com/geocentric-gobbledegook is a different review, of Marshall "
                "Hall"),
             url="https://creation.com/geocentrism-and-creation"),
        dict(label=(
                "Faulkner, “The Rise of the Modern Geocentric Theory Movement”, Answers in Genesis, 4 "
                "September 2020 — dates Bouw's 1976 entry and reports “geocentricity” as his "
                "rebranding"),
             url="https://answersingenesis.org/astronomy/rise-of-modern-geocentric-theory-movement/"),
        dict(label=(
                "Schadewald, The Plane Truth, Appendix D — 1978 conference, 1984 succession, the 1990 "
                "reorganisation, and “the most sophisticated defenses of geocentricity ever "
                "published”"),
             url="https://www.cantab.net/users/michael.behrend/ebooks/PlaneTruth/pages/Appendix_D.html"),
        dict(label=(
                "Branch, “In the Orbit of McLean”, NCSE, 1 July 2014 — Bouw on the Defendants' Second "
                "List of Witnesses in McLean v. Arkansas; “Dr. Bouw will testify that neither "
                "creation-science nor evolution-science can be proved absolutely”; he did not testify"),
             url="https://ncse.ngo/orbit-mclean"),
        dict(label=(
                "Barbour & Bertotti, “Gravity and inertia in a Machian framework”, Il Nuovo Cimento B "
                "38:1–27 (1977) — named by Bouw as the most successful Machian model; verified to "
                "exist and to be correctly cited by him"),
             url="https://doi.org/10.1007/BF02726670"),
        dict(label=(
                "Pfister & Braun, “Induction of correct centrifugal force in a rotating mass shell”, "
                "Class. Quantum Grav. 2:909–918 (1985) — the quantitative form of the rotating-shell "
                "result"),
             url="https://doi.org/10.1088/0264-9381/2/6/015"),
        dict(label="Everitt et al., “Gravity Probe B",
             url="https://doi.org/10.1103/PhysRevLett.106.221101",
             note=(
                "Final Results of a Space Experiment to Test General Relativity”, Phys. Rev. Lett. "
                "106:221101 (2011) — frame dragging −37.2 ± 7.2 mas/yr; not located anywhere in the "
                "2013 edition")),
        dict(label=(
                "Wikipedia — Gerardus D. Bouw. Retained only as a finding aid; its Edwards v. "
                "Aguillard sentence is not supported by the NCSE source it cites, and its “instructor "
                "for astronomy at Baldwin Wallace” is unsupported by the obituary or by his own "
                "account"),
             url="https://en.wikipedia.org/wiki/Gerardus_D._Bouw"),
        dict(label="Mandelbrote & van der Meer (eds), Nature and Scripture in the Abrahamic Religions",
             url="https://brill.com/edcollbook/title/17821",
             note=(
                "1700–Present (Brill, 2008), pp. 449–454 — cited by Wikipedia as the scholarly source "
                "for Bouw's KJV-only route and for the equivalence-plus-theological-reasoning "
                "reading. NOT VERIFIED: paywalled, and the chapter author and wording were not "
                "established from here. Do not publish anything on its…")),
        dict(label="Faulkner review, Journal of Creation",
             url="https://creation.com/geocentric-gobbledegook")]),

"PER-SUNGENIS": _p(
    name="Robert A. Sungenis, Sr.", dates="b. c. 1955 – living · geocentric work from c. 2002",
    lineage="Tychonian",
    role=(
        "Carrier and systematiser of the Tychonian lane — van der Kamp's and Bouw's arguments "
        "assembled into a “Claims and Responses” apparatus — and, with Bennett and DeLano, the "
        "probable point of entry for the CMB-anomaly argument. 134 items across three bylines, the "
        "largest share after Rowbotham. He is not the originator of the experiments the list credits "
        "to him, and he does not hold the list's headline claim."),
    works=["WRK-SUNGENIS-2006", "WRK-PRINCIPLE-2014"],
    bio_status="worked",
    formation=(
        "<strong>The bibliography, since the dateline cannot hold it.</strong> <em>Galileo Was "
        "Wrong</em> ran to five editions in two volumes by 2010, a sixth in three volumes in January "
        "2013 and a seventh later the same year; <em>The Principle</em> is 2014; <em>Flat Earth, Flat "
        "Wrong</em> is 2018.<br><br>He arrives from theology, not from physics, and the route "
        "matters. Raised Roman Catholic, he converted to Protestantism as a young man, took a BA in "
        "religion from George Washington University and an MA in theology from Westminster "
        "Theological Seminary, and returned to Catholicism in the early 1990s — the reversion date is "
        "given as 1992 by the Wikipedia article, which is a wiki and not scholarship, and we did not "
        "confirm it against a document. He founded Catholic Apologetics International and spent a "
        "decade arguing Catholic-Protestant controversy before cosmology entered the picture at all. "
        "On the same wiki's account he came to geocentrism around 2002 by reading Gerardus Bouw's "
        "<em>Geocentricity</em> (1992); his own book supports the route, thanking Bouw for “expertise "
        "and consultations” in the acknowledgements and citing van der Kamp's <em>De Labore "
        "Solis</em> by page. That is the whole lineage in one line: van der Kamp to Bouw to Sungenis, "
        "and the arguments were already made when he found them. What he brought was an apologist's "
        "instinct for the objection-and-reply. The epigraphs to Volume II are Twain, Arthur C. Clarke "
        "and Karl Popper twice, one of them the line that a scientific theory “neither explains nor "
        "describes the world; it is nothing but an instrument” — the same instrumentalist furniture "
        "van der Kamp assembled from Popper and Dingle, inherited rather than rebuilt. The doctorate "
        "came last and out of the same project: by his own published account the degree was awarded "
        "by Calamus International University on 5 April 2006 for a dissertation defending "
        "geocentrism, and the CD-ROM edition of <em>Galileo Was Wrong</em> carries an introduction "
        "signed twenty days later. He states in that account that “CIU is not accredited by a "
        "governmental body, only by private bodies,” and that the first reading of the dissertation "
        "was performed by Robert Bennett — the physicist who would co-sign the book."),
    had=(
        "More than anyone else on this page, and the review should say so plainly. He had a co-author "
        "with a real physics doctorate: the book's own <em>About the Authors</em> records that Robert "
        "J. Bennett “holds a doctorate in Physics from Stevens Institute of Technology with a thesis "
        "on General Relativity titled ‘Relativistic Rigid Body Motion,’” taught physics at Manhattan "
        "College and Bergen Community College from 1967 to 1983, and “has written Chapter 10” — the "
        "technical chapter — while Sungenis wrote every other chapter and appendix of the volume. He "
        "had the primary literature and used it: Lynden-Bell, Katz and Bičák in <em>MNRAS</em> 272 "
        "(1995), Thirring, Brill and Cohen, Barbour and Bertotti, Gödel, Hoyle, Bondi, the Michelson "
        "papers, Bilger's ring-laser precision figure, Hipparcos. He quotes them with page-numbered "
        "footnotes, which is more than the list built on him ever does. And he had a method: Volume "
        "II's chapter 10 is organised as “Claims and Responses” against Sagnac, Michelson–Gale, "
        "Hafele–Keating, GPS, Ives–Stilwell, parallax versus aberration, binary stars, redshift "
        "surveys, the Pioneer anomaly and the CMB dipole. That is a man who went looking for the "
        "strongest objections and answered them in print, which is the method this review uses and is "
        "entitled to respect for. The usual accusations do not survive contact with the text. In the "
        "1.76-million-character OCR of Volume II (7th ed., 2013) read for this entry, “aberration” "
        "occurs 258 times, “Bradley” 59, “Sagnac” 263, “stellar parallax” 11, “Hipparcos” 7 and “ring "
        "laser” 13 — including a correct textbook account of the modern instrument, ending with the "
        "sentence that the beat frequency varies with the rotation of the ring “with respect to the "
        "local inertial frame of reference” and the flat statement that “ω is the angular rotation of "
        "the Earth,” followed by the observation that global clock synchronisation “must take the "
        "rotation of Earth into account.” He printed the measurement, and printed what it measures."),
    ignored=(
        "Not the evidence — he read it. Three things, all of them arguments rather than data, and the "
        "first is the load-bearing one. <em>First, nothing in the model sets the number.</em> "
        "Bennett's formal proof states its two premises openly: an Earth rotating at angular velocity "
        "ω against a stationary star shell produces the Coriolis and centrifugal terms, and a star "
        "shell rotating at ω against a stationary Earth produces a gravitomagnetic field with vector "
        "potential <em>A</em> = (<strong>B</strong>×<strong>r</strong>)/2 — and the equations of "
        "motion coincide. That is an identification, not a derivation. On the rotating-Earth account "
        "ω follows from the planet's angular momentum and shows up independently in its oblateness; "
        "on the shell account ω is inserted, and the value inserted is the one the other account "
        "already predicted. No page in the Volume II text searched for this entry derives "
        "<strong>B</strong> from the mass distribution of the shell, and the fitted parameter is "
        "therefore on the geocentric side of a comparison the chapter presents as even. <em>Second, "
        "the theorem he quotes rules out the arrangement he wants, and the objection is not taken "
        "up.</em> At pp. 146–147 he reports the Lynden-Bell team's “general proof that the angular "
        "momentum of any closed universe is zero,” and reads it as providing “the fixed and "
        "undisturbed cradle for the barycenter, the Earth.” A cosmos rigidly circulating once a day "
        "carries an immense total angular momentum, and that is precisely the quantity the proof sets "
        "to zero. On the same page he prints the paper's own condition — Mach's principle follows “if "
        "the universe is closed” — and the sentence that travels downstream carries no trace of it. "
        "<em>Third, and structurally, the book runs both halves of an argument that cancels.</em> "
        "Chapters 9 and 10 argue that the frames are indistinguishable: Mach, general covariance, and "
        "the Michelson–Gale summary offered as an explicit disjunction — the apparatus measured "
        "either the Earth's rotation <em>or</em> the ether's rotation about it. Then the same "
        "chapters conclude that “geocentrism has been established by the very physics that sought to "
        "dethrone it in 1905.” If the descriptions are equivalent, no experiment is evidence for "
        "either, and every experiment cited as a proof is spending the concession the rest of the "
        "case rests on. That is van der Kamp's problem returning one generation later, and Bouw — the "
        "man who brought Sungenis into this, thanked by name in the front matter — went the other way "
        "and conceded it. No page located in the volume read reconciles the two."),
    legacy=(
        "134 of the 461 items, across 24 clusters and three bylines — with Bennett, with DeLano, and "
        "alone. The two largest clusters on the entire specimen carry his byline: 28 items on "
        "Earth-fixed coordinate systems and 15 restating coordinate freedom in different technical "
        "vocabularies. But those two are also where this review's compression audit found the drift "
        "running away from him, and the distinction is the point of this field. <strong>Carried "
        "forward substantially intact:</strong> the Michelson–Gale and Sagnac framing, Dayton Miller, "
        "Michelson–Pease–Pearson, the Machian relational argument, the “Ptolemaic models predicted "
        "accurately” line, the patristic and church-tradition appeal, and the CMB anomalies. "
        "<strong>Merely resembling him:</strong> the 28 navigation, geodesy, seismology and metrology "
        "items, which the source nowhere offers as evidence that the Earth does not move — the "
        "premise that converts them into an argument was supplied by the page they sit on — and six "
        "of the fifteen formalism vocabularies, whose keywords (Noether, Fermat, light cone, "
        "renormalization) were not located in the scanned volume at all. What descends is firmer than "
        "what he wrote, consistently in the direction of more certainty; his Michelson–Gale "
        "disjunction arrives as “Sagnac effect consistent with stationary Earth,” filed as one of 461 "
        "proofs. <strong>And the largest fact about his legacy on a flat-earth list is that he is not "
        "a flat-earther and has published at length against them.</strong> The volume read here uses "
        "“sphere” 148 times; it records that “Lactantius was the only Father of the Church … who held "
        "to the idea of a non-spherical Earth”; and it reaches for the flat-earther as its own image "
        "of the fringe it fears being filed with — a man “who still believes in a flat Earth and "
        "spends his day donning an aluminum foil hat waiting for messages from outer space.” In 2018 "
        "he published a 732-page book, <em>Flat Earth, Flat Wrong</em>, against the position. The "
        "list's single largest tranche of technical material is quarried from an author whose stated "
        "view is a spherical Earth at rest, and who wrote a book to refute the claim the list exists "
        "to defend. Where the two lineages meet, they meet as strangers."),
    kernel=dict(
        description=(
            "Bennett's formal proof is correct, and it is not a fringe result. Write the equation of "
            "motion for a test body in a frame rotating at ω and you get the Coriolis and centrifugal "
            "terms; write it for a stationary body inside a shell generating a constant homogeneous "
            "gravitomagnetic field and you get the same equation when ω = <em>B</em>/2. Thirring "
            "showed a version of this in 1918, Brill and Cohen extended it, and Lynden-Bell, Katz and "
            "Bičák put Mach's principle on the relativistic constraint equations in a refereed "
            "journal in 1995 — all of it cited accurately in the book, with page numbers. Sungenis's "
            "second true thing is methodological and this review is in no position to sneer at it: he "
            "sought out the objections and answered them one at a time in print, including the ones "
            "that hurt, and where the physics community's own view is contested he sometimes says so "
            "— the chapter on the CMB alignments notes that the significance is “now contested by "
            "mainstream scientists,” which is more caution than his own downstream lists allow. He "
            "is, on the evidence of the text, the most careful author on this page."),
        why_it_doesnt_save_claim=(
                "An equivalence has two ends. If a rotating shell reproduces the rotating-Earth "
                "account exactly, then Michelson–Gale, Sagnac, Foucault, Miller and the gyrocompass "
                "are evidence for neither description, and cannot be counted as proofs of one — which "
                "is what the 134 items do with them. Where the two accounts are not equivalent, the "
                "asymmetry runs against him: the Earth's ω is determined by its angular momentum and "
                "independently visible in its oblateness, while the shell's <em>B</em> has to be set "
                "by hand to the value already measured, and the zero-total-angular-momentum theorem "
                "he quotes is the result that most directly excludes a cosmos circulating once a day. "
                "And the honest terminus of his own argument is a globe — round, at rest, in a "
                "Machian universe — which is Bouw's position, and Bouw drew the conclusion Sungenis "
                "has not: that a model observationally equivalent to the standard one is chosen on "
                "other grounds than observation. A flat-earth proof list cannot inherit the argument "
                "without inheriting that, and it does not.")),
    sources=[
        dict(label="Galileo Was Wrong",
             url="https://archive.org/stream/GalileoWasWrongTheChurchSungenisRobertA.Bennett4276/Galileo%20Was%20Wrong_%20The%20Church%20%20-%20Sungenis,%20Robert%20A.%20&%20Bennett,_4276_djvu.txt",
             note=(
                "The Church Was Right, Vol. II (7th ed., 2013), chs 7–13 — full OCR text, retrieved "
                "and searched 2026-08-11")),
        dict(label="Sungenis, “My Ph.D. from Calamus International University”",
             url="https://isidore.co/misc/Physics%20papers%20and%20books/Cosmology/Copernican%20principle/Sungenis%20&%20De%20Lano/about%20Sungenis's%20%22Diploma%20Mill%22%20PhD.pdf"),
        dict(label=(
                "“Authors” page, galileowaswrong.blogspot.com — claimed credentials for Sungenis and "
                "Bennett"),
             url="http://galileowaswrong.blogspot.com/p/authors.html"),
        dict(label="Flat Earth Flat Wrong",
             url="https://www.goodreads.com/book/show/46194734-flat-earth-flat-wrong",
             note="An Historical, Biblical & Scientific Analysis (2018, 732 pp) — catalogue record"),
        dict(label=(
                "“Some Catholics maintain Galileo was wrong and Earth is at universe's center”, 7 "
                "July 2011 — on the November 2010 geocentrism conference near Notre Dame"),
             url="https://www.bangordailynews.com/2011/07/07/news/some-catholics-maintain-galileo-was-wrong-and-earth-is-at-universe%E2%80%99s-center/"),
        dict(label="Wikipedia — Robert Sungenis",
             url="https://en.wikipedia.org/wiki/Robert_Sungenis"),
        dict(label=(
                "Lynden-Bell, Katz & Bičák, “Mach's principle from the relativistic constraint "
                "equations”, MNRAS 272 (1995) 150"),
             url="https://ui.adsabs.harvard.edu/abs/1995MNRAS.272..150L/abstract"),
        dict(label="Michelson, Gale & Pearson 1925, ApJ 61:140 — original paper",
             url="https://paulba.no/paper/Michelson_Gale_II.pdf"),
        dict(label="Krauss on The Principle, Slate, 8 April 2014",
             url="https://slate.com/technology/2014/04/lawrence-krauss-on-ending-up-in-the-geocentrism-documentary-the-principle.html")]),

"PER-MARSHALLHALL": _p(
    name="Marshall Hall", dates="dates not established · active 1973 – 2013",
    lineage="Tychonian",
    role=(
        "Populist wing of the Tychonian lane. Carrier of van der Kamp's and Bouw's arguments; "
        "originator, as located, of exactly one — the occult roots of heliocentrism (D10, item 76)."),
    bio_status="worked",
    formation=(
        "<strong>His dates are not established.</strong> Wikipedia’s Benjamin Bridges article gives "
        "“1931–2013”, cited only to the fixedearth.com home page as retrieved in 2013 — a live "
        "website, not a death notice; no obituary was located. What is documented is activity: "
        "president of the Fair Education Foundation, Inc. from 1973 (the Foundation’s own signature "
        "line); researching geocentrism from 1980 and fixedearth.com online from 1997 (Religion News "
        "Service, 29 March 2006); <em>The Earth Is Not Moving</em> 1991, third printing April 2005; "
        "site content ends mid-2013.<br><br>Marshall Hall came to a stationary Earth from "
        "anti-evolution campaigning, and the order is the shape of the whole position. He ran the "
        "Fair Education Foundation, Inc., a small nonprofit at Box 866, Cornelia, Georgia, whose own "
        "signature line dates his presidency from 1973, and he was writing against evolution in "
        "public schooling before he wrote about the Earth's motion. His account of the route is in "
        "the book, in the first person: around 1975 he encountered the anti-evolution work of Richard "
        "Elmendorf, a mechanical engineer near Pittsburgh, who introduced him to the <em>Bulletin of "
        "the Tychonian Society</em> under Walter van der Kamp's editorship; by the early 1980s he had "
        "found the mathematician James Hanson and the astronomer Gerardus Bouw; in 1984 he circulated "
        "an unpublished anti-Copernican manuscript at a meeting in Cleveland. Religion News Service, "
        "reporting in 2006, has him researching geocentrism since 1980 and putting fixedearth.com "
        "online in 1997. The lineage is documentary and short: he is downstream of van der Kamp by "
        "way of the American creationist network, and he says so. What he adds is the frame. Where "
        "van der Kamp argued that heliocentrism is <em>unproven</em>, Hall argues that it is the "
        "keystone — pull it and evolution, deep time and the rest come down with it — and that it was "
        "put there deliberately. The book is a dialogue between two characters, Bo Bo and Vern, with "
        "Hall speaking as Bo Bo; the cover promises the exposure of over four hundred years of "
        "deception. His stated reason throughout is Biblical inerrancy, which satisfies this page's "
        "self-report rule: it is what he says, not what we infer."),
    had=(
        "More than the finished product suggests. He had the Tychonian literature and had read it, "
        "citing van der Kamp, Bouw, Hanson and N. M. Gwynne by name and by <em>Bulletin</em> issue "
        "number. For the historical argument — the one this list actually takes from him — his source "
        "is real scholarship, correctly cited: Edward Rosen, “Kepler and Witchcraft Trials,” <em>The "
        "Historian</em> 28 (1966), p. 447, by the leading Copernicus scholar of his generation, then "
        "at City College of New York. The facts he lifts from it are true. Katharina Kepler was tried "
        "as a witch on forty-nine counts, was imprisoned at Güglingen, and her son travelled there "
        "and submitted a defence brief in May 1621. Hall prints her acquittal himself, in Rosen's own "
        "words. He also had the apparatus, and he went and looked at it: he inspected the Foucault "
        "pendulums at the Franklin Institute in Philadelphia and at the Smithsonian, and the book "
        "carries a photograph of him at the top of the Philadelphia exhibit with the bob eighty-five "
        "feet below. That is not armchair work, and it is the same instinct the zetetic lane claims "
        "for itself. And he corrected himself in print — the third printing opens with an author's "
        "note conceding that the chapter on eclipses (pp. 207–214) will have to be amended, because "
        "the direction of the eclipse shadow turns out to be the same in both models. An argument of "
        "his own, withdrawn in his own book, with the chapter still in it."),
    ignored=(
        "Two things, and only the second is his own making. <br><br><strong>First, "
        "inherited.</strong> Michelson–Gale–Pearson. The book's thesis is that nothing has ever been "
        "measured showing the Earth turning; the 1925 <em>Astrophysical Journal</em> paper is a "
        "fringe measurement of exactly that — 0.236 ± 0.002 predicted, 0.230 ± 0.005 observed — "
        "published sixty-six years before he wrote. It is not located in the ABBYY OCR of the third "
        "printing (April 2005) scanned at archive.org: no occurrence of “Gale”, “Sagnac”, “ring "
        "laser” or “1925”, and the book's own printed index steps from “Michelson” straight to "
        "“Michelson-Morley” with nothing between. Scope that: no print copy was consulted, and the "
        "1991 first printing was not reached. It is also not a hole he dug. <em>De Labore Solis</em> "
        "has the same one, and Hall is reading van der Kamp.<br><br><strong>Second, and internal: he "
        "raised the objection to his own argument and printed it beside the argument.</strong> On the "
        "Foucault pendulum he says two incompatible things within a dozen pages. The instrument is “a "
        "counterfeit of a true pendulum”, a rigged contrivance, and he backs that with a figure — the "
        "speed at Philadelphia is “1100 feet or more per second, not three or four inches every "
        "quarter hour”. The number is right and it is the wrong quantity. 1,674 km/h × cos 40° is 356 "
        "m/s, or 1,168 ft/s, and that is how fast Philadelphia travels round the Earth's axis — a "
        "motion the cable, the floor and the building all share, so it cancels. What is left is the "
        "differential: the swing plane turns at Ω sin φ, which at the Franklin Institute's latitude "
        "is 15.041°/hr × sin 39.96° = 9.66° per hour, about 2.4° per quarter hour, and at a pin ring "
        "a couple of metres across that is precisely the three or four inches he is objecting to. "
        "Then, on the same subject, he quotes Bouw reporting Garber's 1898 result that a rotating "
        "universe would drag the bob identically, so the instrument “can neither prove nor disprove "
        "the rotation of the earth”. He never reconciles them, and they cannot both stand: if the "
        "pendulum cannot decide the question then it is not a fraud, the Smithsonian is deceiving "
        "nobody, and there is nothing to expose. He keeps the strong claim and the honest one side by "
        "side."),
    legacy=(
        "Small, specific, and not where the name would lead you to look. One item of the 461 descends "
        "from him: item 76, “Occult roots of heliocentrism,” cluster D10. Against Rowbotham's "
        "sixty-five and Sungenis's hundred and thirty-four that is nearly nothing, and the shape of "
        "the nothing is the finding — the author of a full-length geocentric book contributes a "
        "single line to this list, and it is not one of his physics arguments. Those are carried, not "
        "made: Michelson–Morley reframed as a positive result, the shrunken star-sphere that lets a "
        "close universe turn daily, the Foucault material — all reach him from van der Kamp and Bouw, "
        "and are attributed to them elsewhere on this page.<br><br>Where he is the earliest instance "
        "<em>located</em> in this lineage is the occult-origins argument, and it is worth saying how "
        "far the search went. It is not in <em>De Labore Solis</em> (1988): searched, zero "
        "occurrences of <em>occult</em>, <em>Kabbal</em>, <em>Mason</em> or <em>Satan</em>, one "
        "incidental each of <em>witch</em> and <em>astrolog</em>. The <em>Bulletin</em> runs of "
        "1971–84 and Bouw's <em>Geocentricity</em> (1992) were not searched. Earliest located, "
        "therefore, not first.<br><br>The developed version left under somebody else's name. In "
        "February 2007 a memo circulating in the Georgia legislature under Rep. Ben Bridges' name, "
        "and then distributed in the Texas legislature by Rep. Warren Chisum, directed readers to "
        "fixedearth.com and argued that the Big Bang and evolution are the creation scenario of the "
        "“Pharisee Religion”, taken concept for concept from the Kabbala. The Anti-Defamation League "
        "and the Texas Freedom Network condemned the material; Bridges said he had nothing to do with "
        "the memo, and Hall said he had Bridges' approval. That is the one occasion on which this "
        "argument reached a legislature, and it also shows the shape of the developed claim: on the "
        "website the occult-roots thesis is Kabbalist and Pharisaic rather than Masonic — 1,208 "
        "occurrences of <em>Kabbal</em> against 17 of <em>Mason</em> in the site transcription "
        "uploaded to archive.org, and none of those words at all in the 1991 book. The site also "
        "carries Holocaust-revisionist and September-11 material in the author's own voice; that is "
        "not part of D10, but it is what the argument's home text is, and this page's standard is to "
        "say what a source is.<br><br>And what does <em>not</em> descend, which matters most on a "
        "flat-earth list. Hall was not a flat-earther and said the opposite in print: the book states "
        "that “the Bible taught that the Earth was a sphere”, treats Columbus and Magellan as having "
        "disposed of the flat-Earth idea, and uses that idea as its worked example of a belief "
        "properly killed by evidence; the site treats the equation of geocentrists with flat-earthers "
        "as a taunt used against them. His single contribution sits on a list whose headline claim "
        "his own book calls a settled error.<br><br>Everything here is drawn from published material "
        "under his own name or from contemporaneous reporting. No death notice was located, so he is "
        "treated as possibly living; nothing is asserted about his motives, and the page scores the "
        "argument, not the man."),
    kernel=dict(
        description=(
            "The premise is true, and it is not fringe history. Modern astronomy did not step into a "
            "disenchanted world. Copernicus, arguing in <em>De revolutionibus</em> I.10 for the Sun "
            "at the centre, reaches for Hermes Trismegistus, who “labels it a visible god”. Kepler "
            "cast horoscopes for a living, wrote a lunar dream-voyage narrated by a daemon, and his "
            "mother really was tried as a witch — and Hall's authority for that trial is Rosen's "
            "peer-reviewed article, cited by volume, year and page. Anyone handed a clean story in "
            "which secular science simply replaces superstition on a datable morning has been handed "
            "something historians of science do not sell either. Hall read real history, read it "
            "correctly, and noticed that the tidy version is tidy."),
        why_it_doesnt_save_claim=(
                "Because of what is done with it next — and he says so himself before doing it. "
                "Having set the Kepler material out, he asks the question and answers it: “What does "
                "all this prove? Nothing. But where there is smoke, there's usually fire.” The "
                "concession is printed and overridden in the same breath, and what overrides it is "
                "the genetic fallacy: where an idea came from is not evidence about whether it is "
                "true, which is why D10 is scored NOT DEMONSTRATED rather than false. Item 76 does "
                "not carry the concession — his text says the evidence proves nothing, the item "
                "states the conclusion flat, and that gap is the compression this page exists to "
                "show.<br><br>And the test does not survive being applied evenly. If occult company "
                "disqualifies a cosmology, geocentrism goes first and by a wide margin. The Ptolemaic "
                "spheres were the working machinery of astrology for fourteen centuries. Tycho Brahe, "
                "whose system Hall adopts, cast the nativity of Christian IV weeks after the birth in "
                "1577, supplied Frederick II and Rudolph II with predictions, read the 1572 supernova "
                "and the 1577 comet astrologically, and built Uraniborg as observatory and alchemical "
                "laboratory together — defending astrology by exactly the macrocosm–microcosm "
                "correspondence, as above so below, that this same list leans on in lane D. "
                "Historians have argued that the commitment shaped his rejection of Copernicus and "
                "the world-system that carries his name. Run consistently, the argument destroys the "
                "model it was built to defend before it reaches the one it was aimed at.")),
    sources=[
        dict(label=(
                "Marshall Hall, The Earth Is Not Moving (copyright 1991; scan is the third printing, "
                "April 2005) — full scan and OCR"),
             url="https://archive.org/details/the-earth-is-not-moving"),
        dict(label=(
                "Danny Faulkner, “Geocentric Gobbledegook”, Journal of Creation 15(2), 2001 — review "
                "of Hall's book"),
             url="https://creation.com/geocentric-gobbledegook"),
        dict(label=(
                "Edward Rosen, “Kepler and Witchcraft Trials”, The Historian 28 (1966), p. 447 — "
                "Hall's own cited authority for the Kepler material"),
             url="https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1540-6563.1966.tb01751.x"),
        dict(label=(
                "Religion News Service, 29 March 2006 — “researching geocentrism since 1980”, "
                "fixedearth.com posted 1997, resident of Cornelia, Georgia"),
             url="https://religionnews.com/2006/03/29/in-this-world-view-the-sun-revolves-around-the-earth/"),
        dict(label=(
                "Fair Education Foundation, Inc. — fixedearth.com home page (copyright line "
                "1997–2013)"),
             url="http://www.fixedearth.com/"),
        dict(label=(
                "“FIXEDEARTH. Marshall Hall” — full-text transcription of the website (word counts "
                "for Kabbal / Pharis / Talmud / Mason taken from this)"),
             url="https://archive.org/details/fixedearth.marshallhall"),
        dict(label="Texas Freedom Network on the Chisum–Bridges memo, February 2007",
             url="https://tfn.org/chisum-launches-attack-on-evolution/"),
        dict(label=(
                "Wikipedia — Benjamin Bridges, §2007 anti-evolution/heliocentrism controversy; source "
                "of the disputed “1931–2013” and of the AJC and Texas Citizens for Science citations"),
             url="https://en.wikipedia.org/wiki/Benjamin_Bridges"),
        dict(label=(
                "Walter van der Kamp, De Labore Solis (1988) — searched for this entry; the "
                "occult-origins argument is not located in it"),
             url="https://geocentricity.com/bibastron/ts_history/de_labore.pdf"),
        dict(label=(
                "Michelson, Gale & Pearson 1925, ApJ 61:140 — the positive rotation measurement not "
                "located in Hall's text"),
             url="https://paulba.no/paper/Michelson_Gale_II.pdf"),
        dict(label="“Starry Messenger",
             url="http://www.sites.hps.cam.ac.uk/starry/tychoastrol.html",
             note=(
                "Tycho Brahe and Astrology”, Cambridge Dept. of History and Philosophy of Science — "
                "nativities, prognostications, Uraniborg as observatory and alchemical laboratory")),
        dict(label=(
                "Rosen 1966 — DOI landing page (10.1111/j.1540-6563.1966.tb01751.x); Hall's footnote "
                "cites p. 447"),
             url="https://onlinelibrary.wiley.com/doi/10.1111/j.1540-6563.1966.tb01751.x")]),

"PER-BLAVATSKY": _p(
    name="Helena Petrovna Blavatsky", dates="12 August 1831 (31 July, Old Style) – 8 May 1891",
    lineage="Esoteric",
    role=(
        "Carrier and subject-of-appropriation, not an originator: no argument on the specimen list "
        "starts with her, and the book cited against the globe affirms the globe on its ninth page."),
    works=["WRK-BLAVATSKY-1877"],
    bio_status="worked",
    formation=(
        "Born Helena Petrovna von Hahn at Yekaterinoslav on 12 August 1831 — 31 July by the Julian "
        "calendar then in use in Russia — into German-descended Russian service nobility. Her mother "
        "was a novelist who published as “Zenaida R-va” and died at twenty-eight; her grandmother was "
        "a self-taught naturalist. Married at seventeen, on 7 July 1849, to Nikifor Blavatsky, "
        "vice-governor of Erivan, and gone within months. The twenty-four years between that and New "
        "York in 1873 are the part of the record that cannot be checked: the studies in India and "
        "Tibet rest on her own later testimony, and Britannica reports them in exactly that register "
        "— she is described as “claiming to have studied under Hindu gurus in India and Tibet.” No "
        "independent corroboration was located in the sources read for this entry. What is datable is "
        "everything after: the Theosophical Society founded in New York with Henry Steel Olcott and "
        "William Quan Judge on 7 September 1875; <em>Isis Unveiled</em> published in two volumes by "
        "J. W. Bouton in 1877, edited by Alexander Wilder; Bombay in 1879 and Adyar from 1882; the "
        "Society for Psychical Research's report of December 1885; <em>The Secret Doctrine</em> in "
        "1888–89; death in London on 8 May 1891.<br><br>The position itself came out of a two-front "
        "quarrel, and she states it on her second page: “Our work, then, is a plea for the "
        "recognition of the Hermetic philosophy, the anciently universal Wisdom-Religion, as the only "
        "possible key to the Absolute in science and theology.” She then names the classes she "
        "expects to array against her, and there are two: “The Christians, who will see that we "
        "question the evidences of the genuineness of their faith” and “The Scientists, who will find "
        "their pretensions placed in the same” category. That is the whole formation, and it matters "
        "here because it is neither a flat-earth formation nor a geocentric one. Her opponent is "
        "authority in both its Victorian costumes; her alternative is a claimed knowledge older than "
        "either. Nothing in that requires a stationary Earth, and nothing in it produced one."),
    had=(
        "The orientalist library of the 1870s, and she used it rather than gesturing at it. On the "
        "pages this project keeps citing she is working from Martin Haug's translation of the "
        "<em>Aitareya Brahmana</em>, quoting it, and arguing from the wording — and the comparative "
        "method she is running was the mainstream method of her decade, the one Max Müller was "
        "practising in a chair at Oxford. She had no chair, no university, no learned society and no "
        "training; the universities were shut to her by sex and the societies by everything else. "
        "English was not her first language and the 1877 manuscript was heavily edited by Alexander "
        "Wilder before it was printable.<br><br>What her apparatus actually consisted of is now "
        "better known than she would have liked, because a hostile spiritualist went and checked. "
        "William Emmette Coleman traced <em>Isis Unveiled</em> to roughly a hundred "
        "nineteenth-century books, quoted largely without acknowledgement and often at second hand "
        "out of compilations, chiefly Samuel Fales Dunlap's. Coleman is not a neutral witness — a "
        "spiritualist opponent of Theosophy, whose promised fuller book never appeared and whose "
        "notes are reported lost in the 1906 San Francisco earthquake — but the finding outlived him. "
        "Wouter Hanegraaff, writing in <em>Correspondences</em> in 2017 and no enemy of this "
        "literature, records that “while Coleman's polemical intentions are obvious, there can be no "
        "doubt that his analysis was essentially correct,” and argues the useful next move is textual "
        "rather than moral. Read as a fact about apparatus instead of about character, that is a "
        "description of a working library: a self-taught writer with about a hundred books, no access "
        "to the manuscripts behind them, and no colleague to check her against.<br><br>And with that "
        "apparatus she got right the one question this page exists to review. <em>Isis Unveiled</em> "
        "vol. I, pp. 9–10, argues that the Vedic authors “must have been acquainted with the "
        "rotundity of our globe and the Heliocentric system,” reads their description of the earth as "
        "a “<em>round</em> and <em>bald</em> head” as evidence “that the authors of the sacred Vedic "
        "books knew the earth to be <em>round</em> or spherical,” and takes the Brahmana's sun that "
        "“<em>never sets nor rises</em>” for an ancient statement that the earth turns. Volume II, p. "
        "477, goes further and names the deniers: Augustine, “the giant of learning and erudition,” "
        "who “scouted the sphericity of the earth”; Lactantius, who rejected Pliny's sphere “on the "
        "remarkable ground that it would make the trees at the other side of the earth grow and the "
        "men walk with their heads downward”; Cosmas Indicopleustes, whose “orthodox system of "
        "geography is embalmed in his ‘Christian topography'”; and Bede. Eleven years later <em>The "
        "Secret Doctrine</em> is more specific still: “Hicetas, Heraclides, Ecphantus, Pythagoras, "
        "and all his pupils, taught the rotation of the earth; and Âryabhata of India, Aristarchus, "
        "Seleucus, and Archimedes calculated its revolution as scientifically as the Astronomers do "
        "now.” The esoteric author on this tab is, on the shape and motion of the Earth, on the other "
        "side from the list that cites her."),
    ignored=(
        "Three things, and one common charge that should <em>not</em> be laid at her door. Take that "
        "one first, because fairness costs nothing: she did not ignore the Hodgson report. She wanted "
        "to sue over it and was dissuaded; whatever else that is, it is not silence, and this entry "
        "does not count it against her.<br><br>First, Casaubon. She stakes a great deal on the "
        "antiquity of the Hermetic books — Iamblichus's 1,100 titles, Seleucus's 20,000 “before the "
        "period of Menes,” the surviving texts explained away as “Latin retranslations of Greek "
        "translations” of originals “preserved by some adepts.” Isaac Casaubon had shown in 1614, on "
        "internal linguistic evidence, that the Greek Hermetica are late Hellenistic compositions; "
        "that was standard philology 263 years before <em>Isis Unveiled</em>, and its consequence is "
        "not exotic — a resemblance between “Egyptian” doctrine and Greek philosophy is explained by "
        "the text being Greek. The name does not occur in the Project Gutenberg full texts of either "
        "volume (#68705, #75871), searched for this entry; we did not search her later works. This is "
        "not a writer who had never heard of transmission: she has Pythagoras fetching his astronomy "
        "from India and says so repeatedly. Transmission is accepted where it lengthens the pedigree "
        "and left unexamined where it would shorten it.<br><br>Second, the source, stated as what it "
        "is. The <em>Book of Dzyan</em> and its Senzar have not been located by anyone, and she never "
        "put a manuscript in front of a reader, a scholar or a critic. That is a search that has not "
        "found its object, and it should be said in that form rather than as a charge: the one "
        "long-term Sanskrit and Tibetan Buddhist specialist to work the question, David Reigle, "
        "identifies her “Books of Kiu-te” with the Tibetan <em>rgyud-sde</em> and argues for "
        "authenticity while conceding the text remains unidentified. Our own record carried the "
        "harsher sentence — that Buddhist-studies scholars regard it as her invention — until 7 "
        "August 2026, when it was withdrawn as wrong about the book, wrong about the field and "
        "irrelevant to the items anyway. It is still standing in two places we do not control from "
        "this entry (see record problems).<br><br>Third, the structural objection, which nothing in "
        "the corpus answers. Her method has a rule that the exoteric surface of a tradition is a "
        "blind laid over the doctrine for the crowd. Grant that rule and no arrangement of surface "
        "evidence can count against any proposed reading, including a wrong one, and she nowhere sets "
        "out the reading her own doctrine would forbid. This is not a slur and it is not aimed only "
        "at her: it is precisely what our verdict of UNFALSIFIABLE on ARG-D07 records, and it cuts at "
        "her conclusions exactly as it cuts at the list's. Her page-9 reading of the <em>Aitareya "
        "Brahmana</em> as ancient heliocentrism is protected by the same rule that protects item "
        "165's reading of Malkuth as a fixed Earth. Neither can be checked, and she supplied the "
        "rule."),
    legacy=(
        "Start with the number, because it is zero. No argument in the 461-item specimen originates "
        "with her. Her name appears in one cluster's originator string — D07, twelve items — and it "
        "appears second; since the 7 August 2026 correction that string resolves to Manly P. Hall, so "
        "the items credited to her as a named originator in the current dataset number none. She is "
        "on this tab because she is cited, not because anything descends from her as a "
        "claim.<br><br>What does descend is a method, and it is worth quoting because it is the "
        "engine the whole D-family runs on. <em>Isis Unveiled</em> vol. I, p. 560: “There never was, "
        "nor can there be more than one universal religion… On this divine chain was strung the "
        "exoteric symbology of every people. Their variety of form is powerless to affect their "
        "substance.” Twelve pages later she runs it on buildings — identical “parts, courses, and "
        "measurements” in temples of every country make it “a warrantable inference that like "
        "religious rites were celebrated in all” — which is the move ARG-D08's seven items make, "
        "fifty-one years before the Hall chapter D08 is actually built on. Whether Hall took it from "
        "her is <em>not</em> established here: his Introduction (sacred-texts <code>sta03</code>) "
        "does not name her, and no full-text search of his book was run for this entry. A shared "
        "method is documented; a line of descent is not, and the difference is the whole point of "
        "this tab. Also carried forward: the free-standing English maxim, at vol. I p. 35 (“As above, "
        "so it is below…”) and p. 294 (“Remember the Hermetic axiom:—‘As above, so below; as in "
        "heaven, so on earth.'”). The 1908 <em>Kybalion</em> numbered it as a Principle and Hall 1928 "
        "carried the package on; our D06 note was corrected in her favour on this point, because the "
        "compact English form is in circulation before the pamphlet that gets the credit.<br><br>What "
        "merely resembles her, and should not be attributed to her: gravity. <em>The Secret "
        "Doctrine</em> vol. I carries a section headed “Is Gravitation a Law?”, and a reader who "
        "knows the modern movement will recognise the tune — “They call Gravity a law, a cause in "
        "itself. We call the forces acting under that name effects, and very secondary effects, too.” "
        "It is a different argument. Her complaint is that a description has been promoted to a "
        "cause, and she makes it in a cosmos whose planets are in orbit and whose Earth, at p. 294 of "
        "the earlier book, has “day and night on the planet, as it turns about its axis.” The list's "
        "gravity cluster, A23, traces to Voliva's “gravity is a lot of rot” by way of the zetetic "
        "line, not to her.<br><br>One find is worth publishing on its own. The roll of ancient "
        "Earth-movers in <em>The Secret Doctrine</em> — Hicetas, Heraclides, Ecphantus, Pythagoras, "
        "Âryabhata, Aristarchus, Seleucus, Archimedes — is very nearly the list our cluster D01 uses "
        "to refute the Tychonian claim that antiquity was unanimously geocentric. The esoteric "
        "lineage's own authority published the refutation of the geocentric lineage's argument in "
        "1888. The two lineages were never reconciled; this is one of the seams, and it is in print."),
    kernel=dict(
        description=(
            "Two true things, at their strongest. The first is the complaint. Victorian scientific "
            "materialism did claim more finality than it had earned, and mid-century popular science "
            "did ask to be believed on authority; she made that complaint from outside every "
            "institution that would have let her make it properly, in a decade when no university in "
            "Europe would have enrolled her. Her insistence that Sanskrit and Buddhist material be "
            "read as intellectual systems rather than as heathenism was, in 1877, ahead of most of "
            "the drawing rooms she was arguing with. The second is narrower and belongs to this page: "
            "on the question of the shape of the Earth she was right, and the people citing her are "
            "wrong. She held that the ancients knew the globe, said so in 1877 and again in 1888, and "
            "put the flat-Earth party — Lactantius, Cosmas Indicopleustes — on the list of the "
            "ignorant. The history of science has since come round to her side of that: Jeffrey "
            "Burton Russell showed the “medieval flat Earth” to be a nineteenth-century invention "
            "propagated by Draper and White, counting at most five patristic deniers in all. Her own "
            "roll of four is a piece of the Draper–White caricature and is too long — but she is "
            "facing the right way, and she is facing it in the two volumes the specimen list cites "
            "against the globe."),
        why_it_doesnt_save_claim=(
                "Because the premise is separable from the method, and only the method travels. "
                "“Their variety of form is powerless to affect their substance” converts resemblance "
                "into testimony; the exoteric-blind rule then guarantees that no surface reading can "
                "disconfirm whatever the conversion produces. Feed that apparatus a Kabbalistic tree, "
                "a Masonic tracing board and a Mithraic relief and it returns a single doctrine about "
                "the sky — and it returns whichever doctrine the operator brought to it. The "
                "demonstration is already in the record: she ran it and got the rotundity of our "
                "globe and the heliocentric system; the specimen list runs it on the same images and "
                "gets a fixed flat Earth; the same rule protects both results against the same "
                "evidence. A procedure that yields a claim and its negation from identical inputs is "
                "not evidence for either. That is why the twelve items filed under D07 do not become "
                "measurements by being old, and why nothing on this list is entitled to lean on her — "
                "least of all the half of it that says the Earth does not move.")),
    sources=[
        dict(label=(
                "Isis Unveiled, vol. I (1877) — full text, Project Gutenberg #68705 (pp. 9–10 "
                "rotundity/heliocentric; p. 35 and p. 294 the maxim; p. 560 one universal religion; "
                "p. 572 temple proportions)"),
             url="https://www.gutenberg.org/ebooks/68705"),
        dict(label="Isis Unveiled, vol. II (1877) — full text, Project Gutenberg #75871 (p. 477",
             url="https://www.gutenberg.org/ebooks/75871",
             note="Augustine, Lactantius, Cosmas Indicopleustes and Bede as the deniers of sphericity)"),
        dict(label=(
                "The Secret Doctrine, vol. I (3rd ed. 1893) — Project Gutenberg #54824; the ancient "
                "Earth-movers passage, and Part III §III “Is Gravitation a Law?”"),
             url="https://www.gutenberg.org/ebooks/54824"),
        dict(label=(
                "Isis Unveiled vol. I ch. I — “the rotundity of our globe and the Heliocentric "
                "system”"),
             url="https://www.theosociety.org/pasadena/isis/iu1-01.htm"),
        dict(label=(
                "Wouter J. Hanegraaff, “The Theosophical Imagination”, Correspondences 6 (2017), pp. "
                "1–37 — on Coleman's analysis and on Blavatsky's working sources"),
             url="http://correspondencesjournal.com/wp-content/uploads/2017/12/16401_20537158_hanegraaff.pdf"),
        dict(label=(
                "Jeffrey Burton Russell, “The Myth of the Flat Earth” (1997) — the medieval flat "
                "Earth as a 19th-c. invention; Draper and White"),
             url="https://www.asa3.org/ASA/topics/history/1997Russell.html"),
        dict(label="William Emmette Coleman, “The Sources of Madame Blavatsky's Writings” (1895)",
             url="https://www.blavatskyarchives.com/colemansources1895.htm"),
        dict(label="David Reigle, “The Book of Dzyan",
             url="http://www.easterntradition.org/article/Book%20of%20Dzyan%20-%20The%20Current%20State%20of%20the%20Evidence,%20pre-publication.pdf",
             note=(
                "The Current State of the Evidence” — the Kiu-te / rgyud-sde identification (host "
                "refused our fetch; see record problems)")),
        dict(label=(
                "Psi Encyclopedia, “The Hodgson Report (Theosophy)” — Harrison's handwriting "
                "critique; no corporate retraction described"),
             url="https://psi-encyclopedia.spr.ac.uk/articles/hodgson-report-theosophy"),
        dict(label=(
                "Britannica — Helena Blavatsky (dates; “claiming to have studied under Hindu gurus”; "
                "“unjustly condemned”)"),
             url="https://www.britannica.com/biography/Helena-Blavatsky"),
        dict(label=(
                "Wikipedia — Helena Blavatsky (dates, marriage, Society founding, Adyar, Coulomb "
                "affair, Dzyan)"),
             url="https://en.wikipedia.org/wiki/Helena_Blavatsky"),
        dict(label="Wikipedia — Hodgson Report (the 1986 SPR press-release title)",
             url="https://en.wikipedia.org/wiki/Hodgson_Report")]),

"PER-HALL": _p(
    name="Manly Palmer Hall", dates="18 March 1901 – 29 August 1990",
    lineage="Esoteric",
    role=(
        "Subject of appropriation, not an originator: a 1928 esoteric compendium mined for imagery by "
        "a list that never names him, and whose own chapters give a Ptolemaic nest of spheres and the "
        "sentence “Astronomically, the geocentric system is incorrect.”"),
    works=["WRK-HALL-1928"],
    bio_status="worked",
    formation=(
        "Born at Peterborough, Ontario, in 1901; in Los Angeles from 1919 and there for the rest of "
        "his life. He had almost no formal education &mdash; the accounts available to us differ on "
        "the household but agree on the schooling. Wikipedia, citing Louis Sahagun&rsquo;s biography, "
        "has him moving to Los Angeles in 1919 &ldquo;to reunite with his birth mother&rdquo;, Louise "
        "Antist Palmer Hall, a chiropractor and a member of Max Heindel&rsquo;s Rosicrucian "
        "Fellowship; the Theosophy Wiki &mdash; a movement-adjacent wiki, not scholarship &mdash; "
        "says he was raised by his maternal grandmother Florence Palmer, was &ldquo;a sickly child, "
        "got little schooling but read voraciously on his own&rdquo;, and lived for a time at the "
        "Rosicrucian Fellowship before growing suspicious of its claims. Sahagun&rsquo;s book was not "
        "read for this pass; the two accounts are reconcilable but they are not the same story, and "
        "neither is a page-cited scholarly source.</p><p>What is not in doubt is the trajectory. He "
        "was preaching at the Church of the People in the Trinity Auditorium within months of "
        "arriving, aged eighteen, and was ordained on 17 May 1923. <em>The Secret Teachings of All "
        "Ages</em> was written by a twenty-seven-year-old lecturer with no university behind him, "
        "financed by public subscription and wealthy patrons, illustrated by J. Augustus Knapp, "
        "designed by John Henry Nash and printed by H. S. Crocker of San Francisco in 1928. He "
        "founded the Philosophical Research Society in 1934 and presided over it until his "
        "death.</p><p>The formative point for this page is what kind of book he set out to write, "
        "because he says so on the first page of it. It is a hermeneutic, not a cosmography: "
        "&ldquo;Symbolism is the language of the Mysteries&rdquo;, and &ldquo;he who seeks to unveil "
        "the secret doctrine of antiquity must search for that doctrine not upon the open pages of "
        "books which might fall into the hands of the unworthy but in the place where it was "
        "originally concealed.&rdquo; That second sentence is the load-bearing rule of everything "
        "downstream of him &mdash; it is why the clusters cut from his chapters are verdicted "
        "unfalsifiable &mdash; and it is his. The use made of it is not."),
    had=(
        "A very large body of esoteric literature, a compiler&rsquo;s temperament, and an unusually "
        "honest statement of what he was doing with both. The preface disclaims exactly the authority "
        "the list later borrows: &ldquo;I make no claim for either the infallibility or the "
        "originality of any statement herein contained&rdquo;, and &ldquo;Having no particular "
        "<em>ism</em> of my own to promulgate, I have not attempted to twist the original writings to "
        "substantiate preconceived notions.&rdquo; He indexed the book, appended a bibliography to "
        "send readers to the originals, and named his intermediaries in the text &mdash; John Cole "
        "for the Dendera description, Albert Churchward for the twelve gates, Eliphas Levi on the "
        "pyramid&rsquo;s cardinal faces, Josephus on the Tabernacle, Georgius von Welling&rsquo;s "
        "<em>Writings</em> of 1735 for the Rosicrucian plates.</p><p>And he transcribed the period "
        "cosmology accurately, which matters more than it sounds. His sephirothic table runs "
        "<em>Primum Mobile</em> &rarr; Zodiac &rarr; Saturn &rarr; Jupiter &rarr; Mars &rarr; Sun "
        "&rarr; Venus &rarr; Mercury &rarr; Moon &rarr; Elements: the Aristotelian&ndash;Ptolemaic "
        "nest, unmangled. His zodiac is &ldquo;a band of fixed stars about sixteen degrees wide, "
        "apparently encircling the earth&rdquo;, whose plane &ldquo;intersects the celestial equator "
        "at an angle of approximately 23&deg; 28&prime;&rdquo;. He gives precession at a degree in "
        "about seventy-two years, 2,160 years to a sign, 25,920 to the circuit &mdash; and hedges it "
        "himself: &ldquo;(Authorities disagree concerning these figures.)&rdquo; He captions his own "
        "Rosicrucian plate &ldquo;a Ptolemaic chart&rdquo; and walks its rings inward past &ldquo;the "
        "surface of the earth and sea&rdquo; to &ldquo;the region of the central fire&rdquo;. The "
        "temple-as-microcosm reading he prints is Josephus&rsquo;s and the Egyptian priests&rsquo;, "
        "and it is also the mainstream reading in Egyptology and classics &mdash; not a private "
        "conceit.</p><p>He also relayed material that cuts against a central Earth rather than "
        "quietly dropping it: the Pythagorean scheme he sets out has ten spheres turning about a "
        "central fire, with the Earth one of the ten and not at the middle. And on the physical "
        "question he did not hide behind symbolism. In the same chapter the list&rsquo;s zodiac items "
        "come from, he writes: &ldquo;Astronomically, the geocentric system is incorrect&rdquo; "
        "&mdash; and describes the heliocentric system as placing the sun at the centre &ldquo;where "
        "it naturally belongs&rdquo;. He was not making a claim about the shape of the Earth. There "
        "is no flat-earth argument in him to be fair or unfair about."),
    ignored=(
        "He cannot be charged with failing to write a book he never set out to write, and this entry "
        "does not do that. Two real gaps remain, and one of them he made worse in his own "
        "voice.</p><p><strong>First, the shelf.</strong> Where a critical literature existed he "
        "frequently took the antiquarian one. The Dendera description he prints is John Cole&rsquo;s, "
        "from the 1820s &mdash; measurements of a medallion four feet nine inches across, set in a "
        "square seven feet nine inches on a side &mdash; and the dating question that object had "
        "already provoked was settled in 1822, when Champollion read <em>autokrator</em> in a "
        "cartouche and placed the ceiling in the Greco-Roman period. No engagement with that reading "
        "is located in the chapters this review has read (the pyramid chapter, the zodiac chapter, "
        "<em>Wonders of Antiquity</em>, <em>The Tabernacle in the Wilderness</em>, the Qabbalah "
        "chapter, the fifteen Rosicrucian diagrams and the alchemy chapter). Calling the Tentyra "
        "stone &ldquo;the oldest circular zodiac known&rdquo; is defensible; leaving a century of "
        "decipherment out of a chapter that turns on the object&rsquo;s antiquity is "
        "not.</p><p><strong>Second, and sharper: he hedged the arithmetic and not the fable.</strong> "
        "The same chapter that states the obliquity to the minute and stops to warn that authorities "
        "disagree about the precession figures also relays, without demur, that &ldquo;One author, "
        "after many years of deep study on the subject, believed man&rsquo;s concept of the zodiac to "
        "be at least five million years old&rdquo;, and asserts in Hall&rsquo;s own voice: &ldquo;In "
        "all probability it is one of the many things for which the modern world is indebted to the "
        "Atlantean or the Lemurian civilizations.&rdquo; Precession is precisely the measurement by "
        "which a zodiac can be dated, and he had just printed its rate. The caution went to the "
        "number he could check and not to the claim he could not.</p><p><strong>Third, the objection "
        "he never answered &mdash; and could not have, because it is structural.</strong> If the "
        "doctrine is &ldquo;not upon the open pages&rdquo;, then nothing on the open pages can count "
        "against a reading, including his own Ptolemaic caption and his own sentence about the "
        "geocentric system. He states the rule and never states what would falsify a reading made "
        "under it. That is not fraud and it is not stupidity &mdash; esoteric hermeneutics is an old "
        "practice with its own standards, and he declares his openly, which is more than many do. It "
        "is an unpriced cost, and every argument descending from his chapters inherits it."),
    legacy=(
        "<strong>Carried forward, documented.</strong> The Philosophical Research Society, founded "
        "1934, outlived him and still operates; by its own account &mdash; institutional "
        "self-description, self-reported &mdash; he wrote &ldquo;over 150 books and essays&rdquo; and "
        "gave &ldquo;over 8000 lectures&rdquo;. <em>The Secret Teachings of All Ages</em> has never "
        "been out of print and is the standard one-volume anthology of Western esoteric imagery in "
        "English. That is a real inheritance and it has nothing to do with the shape of the "
        "Earth.</p><p><strong>On this list: 19 of the 461 items, two arguments &mdash; and be exact "
        "about what kind of descent that is.</strong> He carries D07 (Kabbalistic, alchemical, "
        "Gnostic, Rosicrucian and Masonic iconography, 12 items) and D08 (temple, cathedral and "
        "Dendera-zodiac architecture, 7 items), and he is also the located ancestor behind "
        "D09&rsquo;s three astrology items, where our record deliberately leaves the originator field "
        "empty. But the specimen list names no esoteric author anywhere in its 461 items, and no "
        "citation from any flat-earth author to Hall was located in the searches run for this review. "
        "The attribution is a proximate-source identification, not a citation chain: the D07 cluster "
        "name is very nearly his subtitle &mdash; <em>An Encyclopedic Outline of Masonic, Hermetic, "
        "Qabbalistic and Rosicrucian Symbolical Philosophy</em> &mdash; and its twelve items track "
        "his chapter list close to one for one. That is a resemblance strong enough to name the "
        "nearest text and not strong enough to call transmission, and it is recorded that way. The "
        "scope is not uniform even inside the clusters: items 126 and 127 were not located in the "
        "Hall chapters read, item 126&rsquo;s vocabulary being Eliade&rsquo;s.</p><p><strong>What "
        "does not descend from him: the claim.</strong> Every cosmology his pages preserve is the "
        "geocentric nest of spheres of its own century, and that cosmos has a round Earth in it by "
        "construction &mdash; a <em>primum mobile</em>, a sphere of fixed stars, seven planetary "
        "shells, four elements at the centre, a celestial equator, an obliquity, a precession. His "
        "book was searched in full in an earlier pass of this review for the Christian-devotional "
        "items in lane C, and no conclusion about the shape of the Earth is drawn from that imagery "
        "anywhere in the text searched. What travels intact from Hall to the list is the reading "
        "method and the pictures. The conclusion the pictures are filed under is the list&rsquo;s, "
        "and his own chapter answers it: astronomically, the geocentric system is incorrect."),
    kernel=dict(
        description=(
            "Hall was right that this material is "
            "a coherent body of cosmological thought rather than decoration, and right that reading "
            "it requires a grammar. He was right, specifically and checkably, about the content: "
            "these traditions really do put the Earth at the centre with the heavens turning round "
            "it, and he transcribed that scheme faithfully &mdash; down to the obliquity, the "
            "precession rate and the caption &ldquo;a Ptolemaic chart&rdquo;. He was honest about his "
            "standing, disclaiming infallibility and originality in his preface and appending a "
            "bibliography to send readers past him to the originals. And the reflex objection fails "
            "against him: &ldquo;it is only mysticism&rdquo; loses in public, because the academy "
            "reads this literature seriously &mdash; Frances Yates on the Rosicrucians, Newman and "
            "Principe on alchemy &mdash; and the temple-as-microcosm reading he prints is the "
            "mainstream one, quoted from a first-century witness. A critic who dismisses the whole "
            "shelf is wrong about the shelf and will be corrected by the first specialist who reads "
            "him."),
        why_it_doesnt_save_claim=(
                "At a ball. The nested spheres he preserved require a spherical Earth to be defined "
                "at all; a celestial equator is the projection of a terrestrial one; two great "
                "circles inclined on a sphere cross in exactly two places, which is why there are two "
                "equinoxes and not one or three; precession is a slow wobble of that same frame, and "
                "he gives its period. So the strongest form of the material he assembled is evidence "
                "for a geocentric <em>globe</em> &mdash; a claim about motion, scored on its merits "
                "elsewhere on this page &mdash; and evidence against the lane that files it. His own "
                "sentence closes the question he is being cited to reopen. The one thing that "
                "transmits without loss is the method rule, and it transmits as a liability: a "
                "doctrine that is &ldquo;not upon the open pages&rdquo; cannot be checked against "
                "them, by anyone, in either direction. That is why the two clusters descending from "
                "his chapters are unfalsifiable and self-contradicted rather than simply false "
                "&mdash; and it is a cost the list pays without noticing it has been charged.")),
    sources=[
        dict(label=(
                "Hall, The Secret Teachings of All Ages (1928), Preface — \"I make no claim for "
                "either the infallibility or the originality of any statement herein contained\"; "
                "\"Having no particular ism of my own to promulgate\""),
             url="https://sacred-texts.com/eso/sta/sta01.htm"),
        dict(label=(
                "Hall, Introduction — \"Symbolism is the language of the Mysteries\"; the doctrine "
                "sought \"not upon the open pages of books\""),
             url="https://sacred-texts.com/eso/sta/sta03.htm"),
        dict(label=(
                "Hall, ch. IX \"The Zodiac and Its Signs\" — \"Astronomically, the geocentric system "
                "is incorrect\"; the sun \"where it naturally belongs\"; the zodiac \"apparently "
                "encircling the earth\" at 23° 28′; John Cole on the Tentyra stone; \"the Atlantean "
                "or the Lemurian civilizations\""),
             url="https://sacred-texts.com/eso/sta/sta12.htm"),
        dict(label=(
                "Hall, \"Fifteen Rosicrucian and Qabbalistic Diagrams\" — \"a Ptolemaic chart\", "
                "\"the surface of the earth and sea\", \"the region of the central fire\"; plates "
                "after Georgius von Welling's Writings, Frankfort and Leipzig 1735 and 1760"),
             url="https://sacred-texts.com/eso/sta/sta35.htm"),
        dict(label=(
                "Hall, \"The Tree of the Sephiroth\" — Kether/Primum Mobile through "
                "Malchuth/Elements; the sephiroth as \"ten globes of luminous splendor\""),
             url="https://sacred-texts.com/eso/sta/sta29.htm"),
        dict(label=(
                "Wikipedia — Manly P. Hall (18 March 1901 – 29 August 1990; ordained 17 May 1923; "
                "Jewel Lodge No. 374, 1954; 33° 1973; H. S. Crocker, Knapp, Nash)"),
             url="https://en.wikipedia.org/wiki/Manly_P._Hall"),
        dict(label=(
                "Wikipedia — The Secret Teachings of All Ages (written at 27; funded by solicited "
                "public subscription; Knapp's illustrations; Nash's design)"),
             url="https://en.wikipedia.org/wiki/The_Secret_Teachings_of_All_Ages"),
        dict(label=(
                "Philosophical Research Society — \"founded the Philosophical Research Society (PRS) "
                "in 1934\"; \"over 150 books and essays\"; \"over 8000 lectures\""),
             url="https://www.prs.org/manly-p-hall/"),
        dict(label=(
                "Theosophy Wiki — Manly Palmer Hall (grandmother Florence Palmer; \"a sickly child, "
                "got little schooling but read voraciously on his own\"; residence at Max Heindel's "
                "Rosicrucian Fellowship; the 50,000-volume PRS library)"),
             url="https://www.theosophy.wiki/en/Manly_Palmer_Hall"),
        dict(label="Louis Sahagun, Master of the Mysteries",
             url="https://processmediainc.com/master-of-the-mysteries/",
             note="The Life of Manly Palmer Hall (Process Media, 2008)")]),

"PER-ATKINSON": _p(
    name="William Walker Atkinson", dates="5 December 1862 – 22 November 1932",
    lineage="Esoteric",
    role=(
        "Carrier, not originator: the Chicago New Thought editor who fixed “as above, so below” as a "
        "numbered Hermetic Principle in 1908. He introduced no claim about the Earth — his own book "
        "calls it one world among millions."),
    works=["WRK-KYBALION-1908"],
    bio_status="worked",
    formation=(
        "Atkinson was born in Baltimore on 5 December 1862, son of William C. and Emma L. (Mittnacht) "
        "Atkinson, and his own entry in <em>Who's Who in America</em> gives his education in four "
        "words: “ed. pub. sch.” He was in commercial life from 1882, read law, and was admitted to "
        "the Pennsylvania bar in 1894 and the Illinois bar in 1903. Then it came apart. The reference "
        "literature describes overwork producing “a complete physical and mental breakdown, and "
        "financial disaster”; in the spring of 1900 he left Philadelphia without telling family or "
        "colleagues and surfaced at Dr Herbert A. Parkyn's clinic in Chicago with nervous "
        "prostration, staying six weeks. He recovered under Parkyn's suggestive therapeutics and "
        "never returned to law. From 1901 he was associate editor of <em>Suggestion</em>, then editor "
        "of <em>New Thought</em> (1901–05) and later <em>Advanced Thought</em> (1916–19); he founded "
        "the Yogi Publication Society and Advanced Thought Publishing, both run out of the Masonic "
        "Temple in Chicago, and was a past and then honorary president of the International New "
        "Thought Alliance. He wrote something near a hundred books in thirty years, under his own "
        "name and under at least five personas — Yogi Ramacharaka, Swami Bhakta Vishita, Swami "
        "Panchadasi, Theron Q. Dumont, Magus Incognito. The direction of travel is the thing to hold "
        "on to: he arrived at Hermes Trismegistus from American self-help psychology, not from "
        "Hermeticism, and everything he published about ancient wisdom was produced by a working "
        "magazine editor for a mass market."),
    had=(
        "More than “occultist” suggests, and he used it in the direction the list would least like. "
        "The <em>Kybalion</em> is the work of a man tracking the popular science of 1908 and "
        "flattering it. Its chapter on vibration reaches for “Corpuscles, sometimes called "
        "‘electrons,' ‘ions,'” — J. J. Thomson's vocabulary, then about a decade old. Its model of "
        "sound reasoning is an astronomer who, “seated in his observatory”, uses geometry to “measure "
        "distant suns and their movements”. And its cosmology is stated without hedge or allegory: "
        "the Earth is “a mere grain of dust in the Universe”, there are “millions upon millions of "
        "such worlds, and greater”, and we live in “our own little solar system”. All three passages "
        "are verifiable in the public-domain text at Project Gutenberg (#14209), lines 458, 481 and "
        "1150. He had craft, too. The seven Principles are a clean, teachable synthesis that has "
        "stayed in print for well over a century, and he told the reader exactly which planes he "
        "meant — Physical, Mental, Spiritual — rather than leaving it to be guessed at. The pseudonym "
        "deserves the same fairness: anonymous and Orientalised bylines were ordinary trade practice "
        "in the Chicago metaphysical publishing world, and this was not a permanent concealment. "
        "Within four years he had listed the anonymous titles under his own name in a standard "
        "biographical directory."),
    ignored=(
        "The Hermetic scholarship of his own moment, and it was sitting in his own shop window. Isaac "
        "Casaubon had demonstrated in 1614 that the Greek <em>Hermetica</em> are late-antique rather "
        "than pre-Mosaic Egyptian; and in 1906 — two years before the <em>Kybalion</em>, from the "
        "Theosophical Publishing Society, the press of the milieu he wrote for — G. R. S. Mead "
        "published <em>Thrice-Greatest Hermes</em> in three volumes, subtitled <em>Studies in "
        "Hellenistic Theosophy and Gnosis</em>. Searching the Gutenberg text for <em>Pymander</em>, "
        "<em>Asclepius</em>, <em>Corpus Hermeticum</em>, <em>Emerald Tablet</em> and <em>Mead</em> "
        "returns nothing, and the book carries no bibliography; what stands in their place is chapter "
        "I, where the teachings come “From old Egypt”, Hermes dwells there “in the earliest days” and "
        "“long before the days of Moses”, and the doctrine descends “from lip to ear”. Then the "
        "objection nobody has answered, which is about the title itself. The book quotes a work "
        "called THE KYBALION in italics throughout and describes “the original text” as “purposely "
        "veiled in obscure terms” — having stated four paragraphs earlier that “Its precepts have "
        "never been written down, or printed, so far as we know.” Take the hedge seriously, because "
        "the hedge is fair: “so far as we know” is a proper thing to write about an oral tradition. "
        "It is not a proper thing to write immediately before quoting that tradition as a book with "
        "an original text and italicised extracts. No pre-1908 work of that title is identified in "
        "Deslippe (2011) as reported by Chapel, in Chapel (2013), or in the searches run for this "
        "entry, and Chapel notes the word looks Greek but carries no known meaning in Greek. Beyond "
        "the directory listing, no statement by Atkinson about the book was located in the sources "
        "consulted here."),
    legacy=(
        "Distinguish carefully, because most of what sits under his name in this dataset is not his. "
        "Twelve of the 461 items fall in the one cluster that names him, and two carry his wording: "
        "item 161, “Hermetic as above so below.”, and item 460, “Hermetic altar at the world center "
        "(‘as above, so below')”. What descends from him is a slogan's modern packaging — the doubled "
        "form fixed as one of seven numbered “Hermetic Principles”, which is how most "
        "twenty-first-century readers meet it. What does <em>not</em> descend from him: the maxim "
        "itself (Arabic <em>Kitāb sirr al-ḫalīqa</em>, c. 750–830; Latin vulgate, twelfth century), "
        "its free-standing English form (already in Blavatsky's <em>Isis Unveiled</em>, 1877, as this "
        "review corrected on 2026-08-07), the Platonic-solid cosmos (Plato, or Kepler's avowedly "
        "Copernican <em>Mysterium Cosmographicum</em> of 1596), planet-spacing harmonics (Kepler 1619 "
        "or Titius–Bode), the Earth heart chakra (Coon 1971, Grant 1972) and the toroid. His real "
        "posterity is elsewhere and it is large: the <em>Kybalion</em> has stayed in print from its "
        "original publisher, has trade reissues from Tarcher/Penguin in 2011 and 2018, and its lineal "
        "descendants are law-of-attraction self-help, not cosmology. On the flat-earth side the link "
        "is inference rather than citation. The specimen list carries no citations, footnotes or "
        "named sources of any kind — re-verified against the live page by earlier passes of this "
        "review — so his name is attached to this cluster by wording-match. No flat-earth text naming "
        "the <em>Kybalion</em> was found in the searches run for this entry. If the list's compiler "
        "does not mean Atkinson, item 161 can be withdrawn; what cannot be done is to keep the phrase "
        "and decline to say whose wording it is."),
    kernel=dict(
        description=(
            "Take the strong version first, because it is not the one usually offered. The weak move "
            "is “the <em>Kybalion</em> is a 1908 fake, so the cluster collapses”, and it loses twice: "
            "pseudepigraphic attribution is the normal condition of this literature rather than a "
            "scandal within it, the Greek <em>Hermetica</em> really are ancient, and the "
            "correspondence intuition is old, near-universal and has been scientifically productive — "
            "Kepler built the nested-solid cosmos and, two decades later, the third law out of "
            "exactly that conviction. The strong version is about Atkinson himself, and it runs in "
            "his favour. He is the rare figure on this page whose source does not merely hedge what "
            "the list makes of it but says the opposite: he named his three planes, he told the "
            "reader the teaching was unwritten, and he described a small world among millions in a "
            "solar system measured from an observatory. Read him as he asked to be read and no flat "
            "or stationary Earth is obtainable from him. There is a second true thing, and it is the "
            "mechanism this whole review exists to document: an idea borrows authority by being dated "
            "backwards. Chapel finds the same habit in books published under Atkinson's own name, "
            "where New Thought propositions are credited to “the ancient philosophers of India, five "
            "thousand years ago”. Nothing here turns on what he intended by it, and this page does "
            "not speculate about that."),
        why_it_doesnt_save_claim=(
                "Because it is the frontispiece, not the philosophy, that the list is using. "
                "Everything the specimen takes from this cluster is the Egyptian frame Atkinson "
                "supplied; everything underneath the frame runs the other way. A list that reaches "
                "for “Hermetic” authority through the <em>Kybalion</em> is citing, for antiquity, the "
                "newest link in the chain — and citing a book that answers the list's headline "
                "question against it. That is not a finding about Hermeticism, and this review takes "
                "no position on whether any tradition named here is true. It is a classification "
                "error, and it is the list's, not Atkinson's.")),
    sources=[
        dict(label=(
                "Who's Who in America, Vol. VII (1912–1913), ed. A. N. Marquis, s.v. “Atkinson, "
                "William Walker” — his own entry, listing under “Also, anonymously”: “The Kybalion, "
                "1908”"),
             url="https://archive.org/details/whoswhoinamerica0000albe"),
        dict(label=(
                "Who's Who in America, Vol. VI (1910–1911), same entry — Ramacharaka titles listed, "
                "no “Also, anonymously” block, no occurrence of “Kybalion” in the volume"),
             url="https://archive.org/details/whos-who-in-america_1910-1911_6"),
        dict(label=(
                "The Kybalion (1908), full text — Project Gutenberg #14209. “a mere grain of dust in "
                "the Universe”; “our own little solar system”; “measure distant suns … seated in his "
                "observatory”; “never been written down, or printed, so far as we know”"),
             url="https://www.gutenberg.org/ebooks/14209"),
        dict(label="Nicholas E. Chapel, “The Kybalion's New Clothes",
             url="http://www.jwmt.org/v3n24/chapel.html",
             note=(
                "An Early 20th Century Text's Dubious Association with Hermeticism”, Journal of the "
                "Western Mystery Tradition 3:24 (2013)")),
        dict(label="Philip Deslippe (ed.), The Kybalion",
             url="https://www.penguinrandomhouse.com/books/530627/the-kybalion-by-william-walker-atkinson/",
             note="The Definitive Edition (Tarcher/Penguin, 2011) — the attribution argument"),
        dict(label="Mitch Horowitz, “The New Age and Gnosticism",
             url="https://doi.org/10.1163/2451859X-12340073",
             note=(
                "Terms of Commonality”, Gnosis: Journal of Gnostic Studies 4:2 (2019), pp. 191–215 — "
                "the book's New Age influence")),
        dict(label="G. R. S. Mead, Thrice-Greatest Hermes",
             url="https://archive.org/details/thricegreatesthe01hermuoft",
             note=(
                "Studies in Hellenistic Theosophy and Gnosis, 3 vols, London: Theosophical Publishing "
                "Society, 1906 — the scholarship available in his own milieu two years before")),
        dict(label=(
                "Wikipedia — William Walker Atkinson (breakdown, Parkyn clinic, magazines, "
                "pseudonyms, INTA, 1919 Post Office inquiry)"),
             url="https://en.wikipedia.org/wiki/William_Walker_Atkinson"),
        dict(label=(
                "Gale, Encyclopedia of Occultism and Parapsychology, s.v. Atkinson (via "
                "encyclopedia.com) — death 22 November 1932, Los Angeles"),
             url="https://www.encyclopedia.com/people/philosophy-and-religion/other-religious-beliefs-biographies/william-walker-atkinson"),
        dict(label=(
                "“Three Initiates Unveiled” — survey of 12 proposed authorship candidates, including "
                "the Paul Foster Case report"),
             url="https://philosophadam.wordpress.com/2024/03/16/three-initiates-unveiled-a-critical-historical-analysis-of-12-proposed-candidates-for-authorship-of-the-kybalion-1908/"),
        dict(label="Wikipedia — The Kybalion",
             url="https://en.wikipedia.org/wiki/The_Kybalion")]),

"PER-ELIADE": _p(
    name="Mircea Eliade", dates="1907 – 22 April 1986",
    lineage="Esoteric",
    role=(
        "Not an originator: a historian of religions whose descriptive category was mined by the list "
        "— subject of appropriation, withdrawn from the originator field on 2026-08-09."),
    works=["WRK-ELIADE-1949"],
    bio_status="worked",
    formation=(
        "He is on this page because his vocabulary was quoted, not because he wrote anything about "
        "the shape of the Earth, and the biography has to start by saying so. Born in Bucharest in "
        "1907, he read philosophy at the University of Bucharest, then spent 1928–1930 in India — "
        "Sanskrit and Indian philosophy with Surendranath Dasgupta at Calcutta, then a period at "
        "Swami Shivananda&rsquo;s ashram at Rishikesh — and took a doctorate on Yoga in 1933. He "
        "belonged to the interwar Bucharest generation around Nae Ionescu, and that milieu has a "
        "documented political half which is recorded here as fact rather than as argument: in 1937 he "
        "published in the press aligned with the Legionary movement (<em>Sfarmă-Piatră</em>, <em>Buna "
        "Vestire</em>), enrolled in its Totul pentru Țară party, and was arrested on 14 July 1938 in "
        "Carol II&rsquo;s crackdown, declining to sign a declaration of dissociation. He passed the "
        "war as a Romanian cultural attaché in London and then Lisbon, moved to Paris and the École "
        "Pratique des Hautes Études in 1945, and from 1956 — Haskell Lecturer, then professor in the "
        "Divinity School from 1957 — was at the University of Chicago until his death, where he "
        "co-founded the journal <em>History of Religions</em> and held the Sewell L. Avery chair. Two "
        "reasons the political record appears at all: it is the anti-modernist milieu he shares with "
        "René Guénon, the other name on ARG-D04&rsquo;s source line, and a reader who goes looking "
        "will find it anyway. How far it reaches into the postwar scholarship is genuinely disputed "
        "among specialists and <strong>this review does not adjudicate it</strong>. It has no bearing "
        "on the six items, which stand or fall on what the texts say."),
    had=(
        "The apparatus of a comparativist of his generation, used in the way this section exists to "
        "credit. He read Sanskrit and had first-hand exposure to Indian practice; the rest came from "
        "texts and from other people&rsquo;s ethnographic reports, which in 1949 was not a shortcut "
        "but the state of the art — the central Australian material he leaned on existed as Spencer "
        "and Gillen or not at all. What matters is what he did with it: <strong>he marked his "
        "frames.</strong> The sentence the list&rsquo;s Meru items descend from is a report about a "
        "belief — Meru rises at the centre of the world &ldquo;according to Indian beliefs&rdquo; — "
        "and the reporting verb is not decoration. Where a geographer collecting rival centres would "
        "have had a contradiction on his hands, Eliade wrote the governing rule out in full eight "
        "years later: the multiplicity, even the infinity, of centres of the world &ldquo;raises no "
        "difficulty for religious thought&rdquo;, because this is &ldquo;not a matter of geometrical "
        "space&rdquo; (<em>The Sacred and the Profane</em>, ch. 1, German original 1957). He was also "
        "arguing against something real. The comparative religion he trained into explained religion "
        "away — as bad physics, mistaken biology, or neurosis — and insisting that a religious "
        "structure first be described in its own terms is a defensible methodological choice rather "
        "than an evasion. On the one question this review asks: no assertion about the physical shape "
        "or motion of the Earth was located in the passages read for ARG-D04 and ARG-D05 (<em>The "
        "Myth of the Eternal Return</em>, ch. I &ldquo;The Symbolism of the Center&rdquo;; <em>The "
        "Sacred and the Profane</em>, ch. 1), and both passages point the other way. That is a scoped "
        "result from two chapters, not a survey of a fifty-year bibliography."),
    ignored=(
        "Two things have to be kept apart, and the first is that <strong>on the use this page is "
        "reviewing there is no failing to record</strong>. He died in April 1986; the specimen list "
        "dates from 2026, names no author for any of the eight items that speak his vocabulary, and "
        "postdates him by decades. Inventing a fault to fill this field would be exactly the error "
        "the field exists to catch. The objection he did have in front of him, and did not answer, "
        "belongs to his own discipline: whether his sources bore the weight of his generalisations. "
        "Edmund Leach put it in the <em>New York Review of Books</em> on 20 October 1966 — &ldquo;A "
        "writer who is prepared to generalize in this grandiose way is not going to be put out by a "
        "mere discordance of evidence&rdquo; — with the sharper charge alongside it that authorities "
        "were cited rather than checked. Jonathan Z. Smith pressed the same line from inside Chicago "
        "in &ldquo;The Wobbling Pivot&rdquo; (<em>Journal of Religion</em> 52:2, April 1972). The "
        "demonstration came later still: <em>To Take Place</em> (1987) went back to the ethnography "
        "behind his showpiece Achilpa sacred pole and found the single creator figure to be an "
        "artefact of the 1927 Spencer and Gillen recension, and the two dramatic incidents fused from "
        "passages thirty pages apart. That one appeared a year after his death and is not something "
        "he declined to answer. Leach&rsquo;s, twenty years earlier, is — with a scope on the claim: "
        "<strong>no published reply by Eliade to Leach was located in the searches run for this "
        "entry</strong> (the NYRB article page and general web search); his journals, the "
        "Romanian-language material and the <em>History of Religions</em> back run were not "
        "consulted. Read that as not-found, not as not-existing. The consequence for this dataset is "
        "structural rather than moral, and it is the closest thing to a criticism this record can "
        "honestly carry: a description built to be indifferent to which cosmology is true will fit "
        "any cosmology, and can therefore be quoted in support of any. He stated the rule that blocks "
        "the geographical reading — once, in a different book from the one the vocabulary travels in."),
    legacy=(
        "What descends from him is a category, and the category is genuinely his: the grouping of "
        "world tree, sacred mountain, omphalos and centred temple under one comparative head, which "
        "is what the eight items are speaking when they say &ldquo;axis mundi&rdquo;. The Latin "
        "phrase is older than that use — in Greco-Roman and early-modern astronomy it names the axis "
        "of the celestial sphere, the rotation axis of a spherical cosmos, which is the geometry the "
        "list is arguing against; that point comes from the English Wikipedia article, a wiki and not "
        "scholarship, and has not been checked against a printed edition of Geminus. Institutionally "
        "what descends is the machinery: the journal <em>History of Religions</em>, a chair at "
        "Chicago, and the sixteen-volume <em>Encyclopedia of Religion</em> (Macmillan, 1987) he "
        "edited, through which &ldquo;axis mundi&rdquo;, &ldquo;hierophany&rdquo; and &ldquo;sacred "
        "space&rdquo; reached general reference shelves. <strong>What does not descend is any claim "
        "about the Earth.</strong> Eight of the 461 items use his vocabulary — the six of ARG-D04 and "
        "the two of ARG-D05 — and not one carries an author or a work: the full text retrieved from "
        "withthesun33.com/about-1 on 2026-08-09 was searched. Eliade is this review&rsquo;s "
        "reconstruction of where the words come from, not a citation the compiler made, and no "
        "intermediate text between the scholarship and the list has been identified. Until 2026-08-09 "
        "this dataset recorded him as the <em>originator</em> of both clusters, with a "
        "&ldquo;(misapplied)&rdquo; parenthesis that flagged the trouble without fixing it; the "
        "attribution was withdrawn because the field was wrong, not because a better name was found. "
        "He now carries zero arguments and zero items, and <strong>the zero is the finding</strong>. "
        "Resembling rather than descending: the geographical reading does exist downstream, in a form "
        "his work does not support. Eric Dubay&rsquo;s <em>Flatlantis</em> is advertised on his own "
        "site as an inquiry into &ldquo;Mount Meru, the alleged magnetic mountain ancient cultures "
        "worldwide believed existed at the North Pole&rdquo; — a magnetic object at a surveyable "
        "place, which is precisely the step from symbol to geography Eliade declines. That is a "
        "documented instance of the drift and <em>not</em> an established channel to the specimen. "
        "Nor is any of this new for him: Mark Weitzman, <em>Religions</em> 11(5) (2020), documents "
        "over a hundred citations of Eliade across far-right sites and publishers, and states the "
        "caution this page needs — &ldquo;no author can be held totally responsible for how their "
        "words are understood or used after publication.&rdquo;"),
    kernel=dict(
        description=(
            "The convergence he described is real data and the category is a real achievement. "
            "Peoples with no contact did produce the same figure — a vertical connector at a centre "
            "joining an upper, a middle and a lower region — and independent convergence normally "
            "demands an explanation rather than a shrug. Eliade&rsquo;s move was to describe that "
            "pattern in its own terms instead of explaining it away as bad physics or neurosis, which "
            "is why the material is still usable at all. Stated at its strongest, the kernel is not "
            "that he is merely innocent of the list&rsquo;s use of him: <strong>he is a witness "
            "against it, in the very section the list borrows from</strong>, having written that a "
            "multiplicity of centres raises no difficulty because the space in question is not "
            "geometrical. And the honest complication stays in, because a defender will reach for it: "
            "he is not a deflationary writer. He calls the Centre the zone of absolute reality and he "
            "meant it. Grant that whole."),
        why_it_doesnt_save_claim=(
                "Because the reality he claims is one he defines as not geometrical, and an order "
                "defined as unreachable by measurement is unreachable by measurement in the "
                "claimant&rsquo;s favour too. A premise compatible with every geometry distinguishes "
                "none of them; the identical symbolism has been recited with conviction by people "
                "holding incompatible pictures of the sky. Where the traditions he reports kept "
                "astronomical records, they answer the other way and only against the flat half of "
                "the list — the <em>Sūrya Siddhānta</em> puts Meru at the north pole of a sphere and "
                "a polar star at the zenith of each of two poles, and it is geocentric, so it cuts "
                "for the Tychonian half and against the zetetic one. There is also a plainer point "
                "specific to him: naming a source is not the same as having one. The specimen cites "
                "nobody for these eight items, so what the list actually possesses is a vocabulary "
                "with the scholar detached from it — and the scholar, when reattached, testifies for "
                "the other side.")),
    sources=[
        dict(label=(
                "Guide to the Mircea Eliade Papers 1926–1998, University of Chicago Library — "
                "biographical note"),
             url="https://www.lib.uchicago.edu/e/scrc/findingaids/view.php?eadid=ICU.SPCL.ELIADEM",
             note=(
                "b. 13 March 1907; India 1928–1930 with Dasgupta and at Rishikesh; doctorate 1933; "
                "Haskell Lecturer 1956; Divinity School professor 1957–1986; Sewell L. Avery chair; "
                "d. 22 April 1986")),
        dict(label=(
                "Britannica summary — “born March 9, 1907, Bucharest, Rom.—died April 22, 1986, "
                "Chicago, Ill.” (the dissenting birth date)"),
             url="https://www.britannica.com/summary/Mircea-Eliade"),
        dict(label="Wikipedia — Mircea Eliade",
             url="https://en.wikipedia.org/wiki/Mircea_Eliade",
             note=(
                "13 March 1907 (O.S. 28 Feb); Campanella thesis; 1937 articles in Sfarmă-Piatră and "
                "Buna Vestire; Totul pentru Țară; arrest 14 July 1938; London and Lisbon posts; EPHE "
                "from 1945")),
        dict(label=(
                "Edmund R. Leach, “Sermons by a Man on a Ladder”, New York Review of Books, 20 "
                "October 1966 — the source-criticism objection made in Eliade's lifetime"),
             url="https://www.nybooks.com/articles/1966/10/20/sermons-by-a-man-on-a-ladder/"),
        dict(label=(
                "Jonathan Z. Smith, “The Wobbling Pivot”, The Journal of Religion 52:2 (April 1972) — "
                "the same objection pressed from inside Eliade's own department"),
             url="https://www.journals.uchicago.edu/doi/10.1086/486294"),
        dict(label="Jonathan Z. Smith, To Take Place",
             url="https://press.uchicago.edu/ucp/books/book/chicago/T/bo5951548.html",
             note=(
                "Toward Theory in Ritual (Chicago, 1987) — the Achilpa demonstration; published a "
                "year after Eliade's death")),
        dict(label=(
                "Eliade, The Myth of the Eternal Return, ch. I “The Symbolism of the Center” — the "
                "schema and the “according to Indian beliefs” Meru sentence"),
             url="https://www.thetedkarchive.com/library/mircea-eliade-the-myth-of-the-eternal-return"),
        dict(label="Eliade, The Sacred and the Profane, ch. 1 — the governing rule",
             url="https://hermetics.net/media-library/rosicrucianism/mircaeda-eliade-sacred-profane/01-chapter-01-sacred-space-making-world-sacred/",
             note="multiplicity of centres “raises no difficulty”, “not a matter of geometrical space”"),
        dict(label="Mark Weitzman, “‘One Knows the Tree by the Fruit That It Bears’",
             url="https://www.mdpi.com/2077-1444/11/5/250",
             note=(
                "Mircea Eliade's Influence on Current Far-Right Ideology”, Religions 11(5) (2020) — "
                "documents 100+ citations of Eliade on far-right sites and states that no author is "
                "wholly responsible for later use")),
        dict(label="“Mircea Eliade and Antisemitism",
             url="https://lareviewofbooks.org/article/mircea-eliade-and-antisemitism-an-exchange/",
             note=(
                "An Exchange”, Los Angeles Review of Books — evidence that the interpretation of the "
                "political record is contested among specialists")),
        dict(label="Wikipedia — Axis mundi",
             url="https://en.wikipedia.org/wiki/Axis_mundi",
             note=(
                "credits Eliade with introducing the concept to comparative mythology, and records "
                "the older astronomical sense of the Latin phrase (the axis of the celestial sphere, "
                "via Geminus)")),
        dict(label=(
                "The Encyclopedia of Religion, 16 vols, Macmillan 1987, Mircea Eliade editor-in-chief "
                "— the reference machinery through which the vocabulary spread"),
             url="https://search.worldcat.org/title/encyclopedia-of-religion/oclc/442857928"),
        dict(label="Eric Dubay, Flatlantis — the author's own page",
             url="https://ericdubay.wordpress.com/2022/02/21/flatlantis/",
             note=(
                "an inquiry into “Mount Meru, the alleged magnetic mountain ancient cultures "
                "worldwide believed existed at the North Pole”. Year 2020 per catalogue records, "
                "undated here")),
        dict(label=(
                "The specimen list — items 160, 173, 174, 451, 453, 454 (ARG-D04) and 175, 455 "
                "(ARG-D05) carry no author or work; full text retrieved 2026-08-09 and searched"),
             url="https://withthesun33.com/about-1"),
        dict(label="Britannica — Mircea Eliade",
             url="https://www.britannica.com/biography/Mircea-Eliade")]),

"PER-PTOLEMY": _p(
    name="Claudius Ptolemy", dates="c. 100 – c. 170 CE · observations dated 127–141",
    lineage="Pre-modern",
    role=(
        "Subject of appropriation, not an originator: a geocentric AND spherical-Earth astronomer "
        "whose Almagest is quoted by the list against the list's own headline claim."),
    works=["WRK-PTOLEMY-ALMAGEST"],
    bio_status="worked",
    formation=(
        "Ptolemy worked at Alexandria in Roman Egypt, and that is very nearly the whole of what is "
        "documented about his life. His name is the best biographical evidence there is: "
        "Greek-Egyptian <em>Ptolemaios</em> with the Roman <em>Claudius</em> in front of it — a "
        "Greek-speaking Egyptian family holding Roman citizenship, and no relation to the Ptolemaic "
        "kings. The claim that he was born at Ptolemais Hermiou first surfaces more than a thousand "
        "years after his death and is uncorroborated. The hard anchors are his own: the observations "
        "recorded in the <em>Almagest</em> run from 26 March 127 to 2 February 141, and the Canobic "
        "Inscription is dated 146/147.</p><p>He did not arrive at geocentrism. He inherited it, along "
        "with an archive — Babylonian eclipse records reaching back to 747 BCE, Hipparchus's "
        "observations and his discovery of precession, Apollonius's epicycle geometry — and then "
        "argued the position rather than assuming it. He also inherited a method that runs the "
        "opposite way round from Aristotle's: physics deals in matter that is “unstable and obscure,” "
        "whereas “only the mathematical, if approached enquiringly, would give its practitioners "
        "certain and trustworthy knowledge” (<em>Almagest</em> I.1, Taliaferro). Geometry first, "
        "physical causes afterwards.</p><p>The consequence for this page arrives before any of the "
        "geocentric argument does. Book I chapter 4 establishes that the Earth is a <em>sphere</em>, "
        "and does it observationally — eclipses recorded at different local hours as you move east or "
        "west, the offset scaling with distance, mountains rising out of the sea as you sail towards "
        "them. The flat alternative is disposed of in a single clause: “if it were flat, the stars "
        "would rise and set for all people together and at the same time.” Everything else said about "
        "him here sits downstream of that sentence."),
    had=(
        "An eight-hundred-year observational baseline and no instrument capable of settling the "
        "question. The Babylonian eclipse records he worked from go back to 747 BCE. His own "
        "apparatus was the armillary astrolabe, the meridian quadrant, the plinth and the dioptra — "
        "all naked-eye, all limited to a few arc minutes at best. There would be no telescope for "
        "another fourteen centuries and no clock better than water.</p><p>What he built with that is "
        "not a placeholder. Reconstructed with modern figures, his Mars scheme places the planet "
        "against the fixed stars to about 14 arc minutes — half the width of the Moon — and his solar "
        "model to roughly one; the machinery underwrote calendars and navigation in Greek, Arabic and "
        "Latin for something like fourteen hundred years. He also went beyond geometry into physical "
        "cosmology: the <em>Planetary Hypotheses</em> assigns actual distances, the Sun's sphere at "
        "1,210 Earth radii and the fixed stars at about 20,000.</p><p>Every measurement that "
        "eventually decided the question lies beyond his reach by one to three orders of magnitude. "
        "The phases of Venus need a telescope (1610); stellar aberration is 20.5″ (1729); the "
        "parallax of 61 Cygni is 0.31″ (1838); Foucault's demonstration needs a long free suspension "
        "and a means of recording a slow precession (1851). He did not decline to make those "
        "measurements. They did not exist.</p><p>And within his limits he did not duck the awkward "
        "reply. In I.7 he raises, in the proponents' own voice, the obvious objection to his "
        "objection — that the air might be carried round together with the Earth — and answers it: "
        "“If they should say that the air is also carried around with the earth in the same direction "
        "and at the same speed, none the less the bodies contained in it would always seem to be "
        "outstripped by the movement of both.” The answer is wrong. It is still an answer, offered "
        "where silence would have been easier."),
    ignored=(
        "Two things, and the second one is his own book.</p><p><strong>First, Aristarchus — and the "
        "charge has to be scoped, because he is not silent about the man.</strong> The "
        "<em>Almagest</em> preserves Aristarchus's summer-solstice observation of 280 BCE among the "
        "older records it works from, so Ptolemy knew him as an observer and used him as one. What is "
        "absent is the hypothesis. In the Taliaferro text of Book I chapters 1–7 that this page cites "
        "— 4,832 words, searched — the string “Aristarchus” does not occur; the rotating-Earth "
        "conjecture is taken up in chapter 7 in the anonymous voice of “some people,” and it is "
        "rejected on terrestrial mechanics, clouds and thrown objects being left behind, rather than "
        "on any test capable of separating the two accounts. Archimedes' <em>Sand-Reckoner</em>, "
        "which preserves both Aristarchus's proposal and his answer to the no-parallax objection — "
        "that the sphere of the fixed stars is so vast that no shift could show — was three centuries "
        "old and Alexandrian. One further irony is our reading rather than his statement, and is "
        "offered as such: chapter 6 grants that the Earth “has sensibly the ratio of a point to its "
        "distance from the sphere of the so-called fixed stars.” That is exactly the concession "
        "Aristarchus needed. Ptolemy grants it for the Earth's own bulk and never puts the question "
        "of whether it could be granted for an orbit.</p><p><strong>Second, the one his own "
        "instruments could have caught.</strong> His lunar model is fitted to the Moon's motion in "
        "longitude, and there it works. Driven, it swings the Moon's distance from about 33 to about "
        "64 Earth radii, which requires the lunar disc to grow by nearly a factor of two between "
        "apogee and perigee. The observed variation is about fourteen per cent — and he owned a "
        "dioptra and used it on apparent diameters. This is not a modern objection dressed up; it is "
        "arithmetic on his own published parameters, and it was pressed afterwards by Ibn al-Shāṭir "
        "and then by Copernicus, both of whom rebuilt the lunar model because of it. We do not find "
        "it confronted in the <em>Almagest</em> as the standard reconstructions summarise Book V; we "
        "have not read Book V entire, and the absence is scoped to that.</p><p><strong>What is not a "
        "failing, and should not be listed as one.</strong> The phases of Venus, aberration, "
        "parallax, the pendulum. There was nothing there to ignore."),
    legacy=(
        "Two lines descend from him and only one of them is actually his.</p><p><strong>The real one "
        "is the mathematics.</strong> His epicycle-to-deferent ratios return the planets' distances "
        "<em>from the Sun</em> — 0.72, 1.52 and 5.22 for Venus, Mars and Jupiter — so the "
        "heliocentric orbit radii were sitting, to within half a per cent, inside a book that put the "
        "Earth at rest in the middle. The equant, his device for non-uniform motion on a circle, was "
        "still doing work in Kepler's trial models before the ellipse. The catalogue of more than a "
        "thousand stars in 48 constellations is the skeleton of the constellation list still in use. "
        "And the book reached Europe through Arabic, which is why it is called the <em>Almagest</em> "
        "and not the <em>Syntaxis</em>. His <em>Geography</em> carries a substantial error of his "
        "own: 180,000 stades for the Earth's circumference, 500 to the degree, against Eratosthenes' "
        "252,000 — low by roughly thirty per cent. Note the shape of that mistake. You can only get a "
        "circumference wrong if there is one.</p><p><strong>What descends into this list is not his "
        "astronomy but a claim about it, and the flat Earth was fitted downstream.</strong> "
        "Rowbotham's <em>Zetetic Astronomy</em> (1865, §9, on eclipses) already uses Ptolemy's "
        "eclipse predictions to argue that predictive accuracy is independent of theory — and sources "
        "it entirely from Victorian popular astronomy (Smith's <em>Rise and Progress of "
        "Astronomy</em>, Partington, Phillips, Somerville), never from the <em>Almagest</em>. As "
        "Rowbotham states it the argument is careful and largely right: eclipse tables can be "
        "computed from observed cycles without commitment to a model. Carpenter's <em>One Hundred "
        "Proofs</em> (1885), proof 66, states the same fact and adds five words that are in neither "
        "Rowbotham nor Ptolemy — Ptolemy predicted eclipses “<em>on the basis of a plane Earth</em>.” "
        "That is the point at which a flat Earth enters the Ptolemy material, and it is precisely the "
        "compression this project's hedge rule exists to catch, occurring inside the movement's own "
        "transmission rather than at its edge. (Whether Carpenter took it from Rowbotham or from the "
        "same secondary shelf is not established here.)</p><p><strong>The rest merely "
        "resembles.</strong> Twenty specimen items restate his non-discriminating appearances as "
        "proofs, and three of them — day–night “from firmament rotation,” “precession from dome "
        "rotation,” “seasonal stars via dome” — hand him a dome he does not have. His cosmos is "
        "nested spheres with a spherical Earth at the centre and the fixed stars some 20,000 Earth "
        "radii out. A dome over a plane is not a smaller version of that; it is a different object, "
        "and he refutes the cosmology it belongs to three chapters before the geocentric argument "
        "begins."),
    kernel=dict(
        description=(
            "Book I chapter 7 contains a concession made by the man the list is citing, against the "
            "use the list makes of him. He sets out the rotating-Earth conjecture in full, grants "
            "that <em>&ldquo;as far as the appearances of the stars are concerned, nothing would "
            "perhaps keep things from being in accordance with this simpler conjecture,&rdquo;</em> "
            "and only then rejects it &mdash; on grounds drawn from the behaviour of clouds and "
            "thrown objects rather than from anything in the sky. That is an early, clean and correct "
            "statement of observational underdetermination, made by someone with every professional "
            "reason not to make it. Van der Kamp and Bouw would spend the twentieth century "
            "rediscovering it.</p><p>And the programme it belongs to was real quantitative science. "
            "It made forward predictions to stated accuracy, it was corrected against observation "
            "across generations, and it was good enough to keep calendars and steer ships for "
            "fourteen centuries. Any answer to this material that begins by calling Ptolemy credulous "
            "is wrong about the history and will lose the exchange to a reader who has opened the "
            "book."),
        why_it_doesnt_save_claim=(
                "Because the concession is symmetric, and because the authority is being run "
                "backwards.</p><p><strong>Symmetric.</strong> If the daily turning of the sky is "
                "consistent with a turning sky, it is equally consistent with a turning Earth &mdash; "
                "so it is evidence for neither, and twenty restatements of it in eight vocabularies "
                "do not accumulate into one that is. Ptolemy says this himself, which is why this "
                "page agrees with him rather than answering him.</p><p><strong>Backwards, and this is "
                "the harder half.</strong> The same seven chapters do two separate things. Chapter 7 "
                "says the appearances cannot decide between a moving sky and a moving Earth. Chapter "
                "4 says the eclipse timings <em>do</em> decide between a sphere and a plane. The list "
                "enters his non-discriminating half as proof and passes over his decisive half in "
                "silence &mdash; and the decisive half goes against its headline claim. A source "
                "quoted only where he is agnostic, and muted where he measured, is not being called "
                "as a witness; it is being used as a name.</p><p><strong>And the equivalence was "
                "never permanent.</strong> It held because the instruments were not yet good enough, "
                "and it ended when they became good enough: 1610, 1729, 1838, 1851. It closed by "
                "measurement rather than by argument &mdash; which is the one route his "
                "second-century apparatus could not take, and the one the list declines to take now.")),
    sources=[
        dict(label=(
                "Ptolemy, Almagest Book I chs. 1–7, trans. R. Catesby Taliaferro (1952) — the text "
                "used for every Ptolemy quotation here, and searched (4,832 words) for the "
                "'Aristarchus' absence"),
             url="https://bertie.ccsu.edu/naturesci/cosmology/ptolemy.html"),
        dict(label="MacTutor History of Mathematics — Ptolemy",
             url="https://mathshistory.st-andrews.ac.uk/Biographies/Ptolemy/",
             note=(
                "observation dates 127–141, the Hermiou birthplace claim, the equant, Newton's "
                "fabrication charge and Graßhoff's reply")),
        dict(label="Wikipedia — Ptolemy",
             url="https://en.wikipedia.org/wiki/Ptolemy",
             note=(
                "dates, Alexandria, the 48-constellation catalogue, the Newton controversy and "
                "Gingerich's rejection of 'fraud'")),
        dict(label="Wikipedia — Geography",
             url="https://en.wikipedia.org/wiki/Geography_(Ptolemy)",
             note="180,000 stades and 500 stades to the degree, against Eratosthenes' 252,000"),
        dict(label=(
                "Richard Fitzpatrick (UT Austin), 'Ptolemy's Model of the Solar System' — the equant, "
                "the ~14′ Mars accuracy, and the lunar model's factor-of-two distance defect"),
             url="https://farside.ph.utexas.edu/books/Syntaxis/Almagest/node3.html"),
        dict(label="Oxford Philosophy of Cosmology — Ptolemy",
             url="https://philosophy-of-cosmology.ox.ac.uk/ptolemy.html",
             note=(
                "nested spheres, Sun at 1,210 Earth radii, fixed stars at 20,000 (Planetary "
                "Hypotheses)")),
        dict(label="Rowbotham (as 'Parallax'), Zetetic Astronomy",
             url="https://www.gutenberg.org/ebooks/69892",
             note=(
                "Earth Not a Globe!, Simpkin Marshall, 1865 — §9, the Ptolemy eclipse-prediction "
                "argument, sourced to Smith, Partington, Phillips and Somerville")),
        dict(label=(
                "Carpenter, One Hundred Proofs that the Earth is Not a Globe (1885) — proof 66, where "
                "'on the basis of a plane Earth' is added to the same argument"),
             url="https://www.gutenberg.org/ebooks/55387"),
        dict(label=(
                "Gysembergh, Williams & Zingg, 'New evidence for Hipparchus' Star Catalogue revealed "
                "by multispectral imaging', Journal for the History of Astronomy 53:4 (2022) — bears "
                "on the copying charge"),
             url="https://journals.sagepub.com/doi/10.1177/00218286221128289"),
        dict(label=(
                "Murschel, 'The Structure and Function of Ptolemy's Physical Hypotheses of Planetary "
                "Motion', Journal for the History of Astronomy 26 (1995), 33 — the realist reading of "
                "the Planetary Hypotheses"),
             url="https://ui.adsabs.harvard.edu/abs/1995JHA....26...33M"),
        dict(label=(
                "Aristotle, De caelo II.14 (Stocks trans.) — the thrown-body argument and the "
                "eclipse-shadow argument that precede Ptolemy's"),
             url="http://classics.mit.edu/Aristotle/heavens.2.ii.html"),
        dict(label="Wikipedia — Almagest",
             url="https://en.wikipedia.org/wiki/Almagest")]),
}
