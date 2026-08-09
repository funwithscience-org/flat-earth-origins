# -*- coding: utf-8 -*-
"""Batch 8 — D13: meaning, teleology and fine-tuning imply centrality.

HANDLE WITH CARE was the brief and it is the right brief. Fine-tuning is a live,
respectable discussion in cosmology and philosophy of physics; the leading review
of it (Barnes 2012, PASA 29:529) explicitly declines to draw any conclusion from
it, and this page is in no position to do better. Nothing here adjudicates whether
the universe has a purpose. The discriminating question is narrower and it is
answerable: does any of this locate the Earth at a physical centre?

Three things this treatment leans on, all checked in this pass:

1. THE FILM'S OWN SYNOPSIS IS INTERROGATIVE AND TELEOLOGICAL, NOT POSITIONAL.
   "are we significant within the structure of the Universe? If we were created
   with a purpose, if we aren't an accident, what does this mean for the future of
   mankind?" — distributor synopsis, PRWeb/FrontGate, 8 December 2015; the same
   wording runs through the film's promotional material. E01 quotes a different
   clause of the same body of copy (the "preferred direction … aligned with our
   supposedly insignificant Earth" line). The two entries do not overlap.

2. A PHYSICIST WHO APPEARS IN THE FILM DRAWS THE DISTINCTION FOR US. John
   Hartnett's own review (biblescienceforum.com, 3 November 2014) holds that we
   are near the centre of the visible universe and rejects the film's absolute
   geocentric reading, noting the CMB axis defines an anisotropy direction rather
   than a unique centre. That is the discriminating question answered from inside
   the film's own tent, which is worth far more than answering it from outside.

3. THE PREMISE THE ARGUMENT NEVER STATES IS HISTORICALLY BACKWARDS. "Centre =
   place of honour" is post-Copernican. Danielson, AJP 69:1029 (2001), and Myth 6
   in Numbers ed., Galileo Goes to Jail (Harvard, 2009).

ATTRIBUTION. The work record (WRK-PRINCIPLE-2014) survives this pass on substance: the
film carries the teleological framing and reviewers place fine-tuning material in it. Its
authorship line did not. An earlier version of this docstring and of the gloss said
Sungenis co-wrote and co-produced the film; both credit blocks located in this pass say
otherwise, and one of them is a source this entry already cited. Variety's review lists
Director: Katheryne Thomas / Producer and Screenplay: Rick DeLano / Executive producer:
Robert Sungenis, and describes Sungenis as interviewed on screen throughout; the
distributor release of 25 March 2015 (PR Newswire, In Ohm Entertainment) lists
"Producer/Writer: Rick DeLano" and "Executive Producer: Robert Sungenis". The gloss now
follows the credit blocks. Two consequences are reported, not applied here: works.py's
WRK-PRINCIPLE-2014 imprint still reads "Produced by Rick DeLano and Robert Sungenis",
which is loose about the executive-producer credit; and `originator` is deliberately NOT
changed — a screenplay credit does not settle who introduced the argument, and Sungenis
is the film's on-screen geocentric proponent and, with Bennett, the author of the
Galileo Was Wrong material this cluster descends from. works.py and clusters.py NOT
edited.

Items 185 (teleological seasons) and 288 (cosmological constant "Earthward") were not
verified against the film in this pass — we could not view it, and neither phrase turned
up in the synopsis copy or in the six published reviews read here. Recorded as unchecked,
not as absent. Flagged to the parent.
"""

ENTRY = {

"D13": dict(
    tldr=("Fine-tuning is a real and unsettled discussion, and the film's question — are we "
          "significant? — is a real question. But the quantities that carry the cosmological "
          "version of the argument are constants: the cosmological constant has one value "
          "everywhere and no "
          "direction at all, so “fine-tuned Earthward” has nothing to point with. Significance "
          "is not a coordinate, which is why the film argues centrality from galaxy shells and "
          "the CMB axis instead — and why John Hartnett, who appears in it, accepts that we sit "
          "in a special place and still rejects the geocentric reading."),

    passage=dict(
        work="WRK-PRINCIPLE-2014",
        pd=False,
        locator=("Official distributor synopsis, issued with the home-video release (FrontGate "
                 "Media / PRWeb, 8 December 2015); the same wording runs through the film's "
                 "promotional copy. Quoted from the press text, not from the film's soundtrack, "
                 "which we were not able to view in this pass."),
        quote=("The Principle explores the significance of the Earth's place within the Cosmos. "
               "… leads us face-to-face with the question, and the challenge — are we "
               "significant within the structure of the Universe? If we were created with a "
               "purpose, if we aren't an accident, what does this mean for the future of "
               "mankind?"),
        gloss="""<p>Read what the sentence actually does. It is a <em>question</em>, and the question is about <strong>significance</strong> and <strong>purpose</strong> &mdash; not about position, not about coordinates, and not about the Earth being in the middle of anything. The film is entitled to ask it. Physics does not answer it, and this page does not answer it either.</p>
<p>The second thing to notice is which word is missing from this sentence: <em>centre</em>. The film's positional claim is carried elsewhere and by different material. John Hartnett, the University of Adelaide physicist who appears in the film, reviewed it on 3 November 2014 and separates the two loads explicitly: the concentric-shell structure in redshift space is his own work and he reads it as placing us near the centre of the <em>visible</em> universe, while the &ldquo;axis of evil&rdquo; defines an anisotropy direction rather than a unique centre. He states that the film aims at an absolute geocentric view and that he does not hold it. So a scientist inside the film draws precisely the distinction this cluster's five items collapse.</p>
<p>The teleological register is real and is not a caricature of the film. Variety's reviewer reports it reaching for &ldquo;a baby's smile&rdquo; and &ldquo;the crescendo of a symphony&rdquo; as evidence of the planet's specialness. Those are appeals to meaning. They are offered as meaning, not as measurement, and the honest reply is not ridicule but the observation that they carry no coordinate. Rick DeLano wrote and produced the film &mdash; Variety credits the screenplay to him &mdash; and Robert Sungenis is its executive producer, interviewed on screen throughout; Sungenis and Bennett's <em>Galileo Was Wrong</em> supplies the CMB material that the film's positional half rests on, which is treated at <a href="#ARG-E01">ARG-E01</a>.</p>""",
    ),

    steelman=dict(
        description="""<p><strong>SURFACE (weak &mdash; do not use).</strong> &ldquo;Fine-tuning is not a real problem.&rdquo; That is a position in a live dispute, not a fact, and anyone who asserts it flatly will be handed a reading list. The cosmological-constant problem is one of the sharpest open questions in theoretical physics &mdash; Weinberg's 1989 review (<em>Rev. Mod. Phys.</em> 61:1) treats it as a crisis, and the observed value sits near 10<sup>&minus;122</sup> in Planck units against naive estimates that are 120 orders of magnitude larger. Luke Barnes's 77-page review (<em>PASA</em> 29:529, 2012) surveys the cases seriously and is scrupulous about what follows from them: &ldquo;I do not attempt to defend any conclusion based on the fine-tuning of the universe for intelligent life.&rdquo; If the leading review declines to draw a conclusion, a debunk page has no business drawing the opposite one.</p>
<p><strong>DEEPER.</strong> Fine-tuning is about parameter <em>values</em>, and centrality is about <em>position</em>; the argument slides between them. True, and it is most of the answer &mdash; but on its own it invites the obvious reply that a universe built to be inhabited makes its inhabitants central in the only sense anyone cares about. That reply is not stupid, and a rebuttal that stops here has not met it.</p>
<p><strong>KERNEL.</strong> The specific true thing this tradition found is that the Copernican principle is a <em>posit</em>, and that a metaphysical rider travelled with it unearned. Two halves, both defensible. First, the geometry: homogeneity was written into the FLRW metric as an assumption long before anyone tried to measure it, which is exactly why cosmologists have had to invent tests for it since &mdash; Clifton, Ferreira and Land, <em>PRL</em> 101:131302 (2008), testing it with distant supernovae; Caldwell and Stebbins, <em>PRL</em> 100:191302 (2008), via CMB spectral distortions; Zhang and Stebbins, <em>PRL</em> 107:041301 (2011), confirming it at Gpc radial scale from the kinetic Sunyaev&ndash;Zel'dovich power spectrum. You do not build a test for something you already measured. Second, the rider: &ldquo;the Earth is not at the geometric centre&rdquo; became, in a great deal of popular scientific writing, &ldquo;the Earth and its inhabitants are of no particular significance&rdquo; &mdash; and that step is a philosophical addition which the geometry never licensed. The film's complaint is against that step, and against that step the complaint is <strong>correct</strong>.</p>""",
        why_it_doesnt_save_claim="""<p>Because the remedy for an illegitimate inference is not the same inference run backwards.</p>
<p>Grant the kernel entirely: &ldquo;not central, therefore insignificant&rdquo; is a non sequitur, because no coordinate entails a value. Then notice that &ldquo;significant, therefore central&rdquo; is the identical non sequitur pointed the other way, and it is the one this cluster needs. Both directions require a bridge between a position and a worth, and the argument's own best insight is that there is no such bridge. Having established that geometry cannot settle significance, it cannot then have significance settle geometry.</p>
<p>The bridge it borrows without stating it is <em>centre = place of honour</em>, and that premise is historically backwards. Dennis Danielson's work &mdash; &ldquo;The great Copernican clich&eacute;&rdquo;, <em>Am. J. Phys.</em> 69:1029 (2001), and Myth 6 of Numbers ed., <em>Galileo Goes to Jail</em> (Harvard, 2009) &mdash; documents that in the cosmology Copernicus displaced, the centre was the <em>low</em> point: where heavy matter falls, where Dante put the pit of hell at the midpoint of the Earth at the dead centre of the cosmos, and which Galileo in the <em>Dialogue</em> called the sump where the universe's filth and ephemera collect. Galileo argued that moving the Earth <em>ennobled</em> it. So the demotion narrative the film is protesting and the honour-of-the-centre premise the film relies on are the same modern invention, and it has adopted one while objecting to the other.</p>
<p>And the &ldquo;it is only an assumption&rdquo; half has been shrinking since 2008, on the record, by people who went and tested it.</p>"""),

    refutation="""<p>Start with the concessions, because they are large and because overstating this one would be the worse error. The fine-tuning problem is real and open. The cosmological constant's smallness is a genuine puzzle that Weinberg framed as such in 1989 and that remains unsolved. The Copernican principle really was assumed before it was tested. Whether the universe has a purpose is not a question physics is equipped to answer, and this page does not attempt to answer it in either direction. What follows is about one narrow step, and only that step: whether any of this places the Earth at a physical centre.</p>

<p><strong>1. What the source claims, at its own strength.</strong> The film's synopsis asks whether we are significant within the structure of the universe and what it would mean if we were created with a purpose rather than being an accident. That is a question about meaning, put as a question. Variety's reviewer reports the film illustrating the point with a baby's smile and the crescendo of a symphony. Nobody is pretending those are data, and treating them as though they were a failed measurement would be a straw man. The claim on the table is: <em>a cosmos with these constants, and these alignments, looks like a place we were meant to be.</em> That is a claim about intention. Answer it on its own ground: intention has no coordinates. A universe intended for its inhabitants would be intended for them wherever they stood in it.</p>

<p><strong>2. Inside the film, centrality is carried by other material entirely.</strong> This matters for provenance, which is what this review is for. Hartnett's review, written by a physicist who appears in the film and who does think we occupy a special place, identifies the positional argument as the concentric shells in redshift space and the CMB axis. He then declines the film's conclusion, observing that the axis defines a direction of anisotropy rather than a unique centre, and stating plainly that he does not hold the absolute geocentric view the film is aiming at. The fine-tuning and purpose material is doing a different job in the film: it establishes significance. The list item <em>&ldquo;Fine-tuning favors centrality&rdquo;</em> welds the two together and supplies a connective &mdash; <em>favors</em> &mdash; that is the list's own: it is not in the distributor synopsis quoted above, which is the film's own statement of its thesis and the text we were able to check. On the axis half, see <a href="#ARG-E01">ARG-E01</a>: the alignments are real and unexplained, and they correlate with the ecliptic, the Galactic plane and our own motion, which is evidence about where the signal comes from and points local rather than cosmic.</p>

<p><strong>3. The tuned quantities have no address.</strong> This is the decisive point for items 184 and 288 and it is a point about grammar, not about magnitude. Rees's six numbers &mdash; N, &epsilon;, &Omega;, &Lambda;, Q, D &mdash; and the rest of the standard list are <em>constants</em>: single values holding at every point of spacetime. A constant is a scalar; a scalar has no gradient and no preferred direction. So &ldquo;cosmological constant fine-tuned Earthward&rdquo; has no referent for the word <em>Earthward</em>. If &Lambda; is tuned for life, it is tuned identically at the centre of the Boötes void, in the Hercules&ndash;Corona Borealis Great Wall, and at every location where nothing lives and nothing ever will. Concede the tuning at full strength &mdash; concede a designer, for the sake of the argument &mdash; and you still have not been handed a position, because the quantity in question is the same everywhere by construction. Nothing that is uniform can single out a place.</p>

<p><strong>4. The other fine-tuning literature, and the seasons.</strong> There is a second and quite different body of work about local habitability &mdash; the Earth&ndash;Moon&ndash;Sun arrangement rather than the constants of nature &mdash; and item 185 belongs to it. Take it at full strength. Seasons are produced by axial obliquity, currently about 23.4&deg;, and not by distance or by cosmic position: the Earth is nearest the Sun in the first week of January, during northern winter. Obliquity is not a fixed dial, either. It oscillates by about &plusmn;1.3&deg; around 23.3&deg; on a roughly 41,000-year Milankovitch cycle, and Laskar, Joutel and Robutel (<em>Nature</em> 361:615, 1993) showed that this stability is the Moon's doing: without it, the chaotic zone in obliquity would run from near 0&deg; up to about 85&deg;, and Earth's tilt would wander through it. Mars, with an obliquity near 25&deg;, has seasons too. So the seasons are a drifting property of one planet's spin axis, maintained by its satellite. Grant every teleological reading of that arrangement you like: the conclusion reached is about an axis of rotation, and an axis of rotation is not a location in the cosmos.</p>

<p><strong>5. The centre that was removed, and who removed it.</strong> Item 187 &mdash; &ldquo;infinite universe removes meaning of center&rdquo; &mdash; is the cluster's own tell, because it is <em>true</em>, and it is true as geometry rather than as ideology. A homogeneous unbounded space has no centre, not because cosmologists preferred it that way but because there is no such point to have. And the observation is far older than the grievance, and came from the opposite direction. Nicholas of Cusa, cardinal and papal legate, wrote in <em>De docta ignorantia</em> II.12 in 1440 &mdash; a century before Copernicus &mdash; that &ldquo;the world-machine will have its center everywhere and its circumference nowhere, so to speak; for God, who is everywhere and nowhere, is its circumference and center&rdquo; (Hopkins translation, &sect;162). In the same chapter he anticipates item 85 exactly: an observer on the Sun, on the Earth, on the Moon or on Mars would in each case fix the poles about himself and take himself to be at the immovable centre. Cusa offered this as an enlargement of God's immensity, not as a demotion of humanity. The item records a real fact about the geometry and then registers it as a loss of meaning &mdash; which is a perfectly intelligible thing to feel and is not a measurement of anything. A grievance about a geometry is not evidence for a different geometry.</p>

<p><strong>6. The premise doing the silent work.</strong> Every item here needs <em>centre = importance</em>, and nowhere states it, because stating it invites the check. The check does not go well. In the cosmology Copernicus displaced, the centre was the basest place in creation: the sink toward which heavy matter falls, with Dante's hell at the midpoint of the Earth at the dead centre of the universe, and the Earth itself described in the Maimonides&ndash;Aquinas line Danielson quotes as the coarsest and most material (<em>ignobilissima</em>) of bodies. Galileo, in the <em>Dialogue</em>, calls the immobile Earth of that picture the sump where the universe's filth and ephemera collect, and argues that setting it in motion among the planets <em>raises</em> its dignity. Danielson's conclusion, in the <em>American Journal of Physics</em> and in the Harvard myths volume, is that the story of Copernicus demoting humanity is a later construction. If so, the equation this cluster runs on was manufactured by the same narrative it is protesting against.</p>

<p><strong>7. The cumulative case, taken at full strength.</strong> The strongest form of the argument is not item-by-item but Bayesian: the constants are hospitable <em>and</em> the largest-scale structures line up with us, and the conjunction is what you would expect if the place were prepared. Take it seriously and it still fails, for two separate reasons. First, a likelihood ratio needs the alternative hypothesis to make a prediction, and geocentrism makes none here: it does not predict a value of &Lambda;, a multipole, an amplitude, or a scale at which the effect cuts off. A hypothesis that would have been equally comfortable with any observation gains nothing when a striking one arrives. Second, and independently: suppose the conjunction really is strong evidence for purpose. Purpose is still not a position. You can drive the likelihood ratio as high as you please and arrive with no coordinates, because none of the evidence in the conjunction is positional except the axis, and the axis is a direction that every observer in the universe would see, as <a href="#ARG-E01">ARG-E01</a> sets out and as Hartnett says in his own review.</p>

<p><strong>8. What the verdict means, and what it does not.</strong> UNFALSIFIABLE is not a synonym for foolish and is not a dismissal of fine-tuning, which is a serious and unresolved question that serious people work on. It records something specific: four of these five items make claims about significance, purpose and meaning, and no observation settles those either way &mdash; not ours, and not theirs. The fifth, &ldquo;cosmological constant fine-tuned Earthward&rdquo;, does make a physical claim, and it fails not because the constant is unremarkable but because a constant is the wrong kind of object to point anywhere. A reader who accepts every word the film says about purpose still leaves without an address for the Earth. That is the whole finding, and the page claims nothing beyond it.</p>""",

    advocate=dict(
        best_defense=(
            "You have conceded the load-bearing points and then answered a compression rather "
            "than us. Nobody in the film claims to have measured purpose, and nobody claims "
            "the cosmological constant has a direction — that phrasing is your list's, not "
            "ours, and you know it, because your own compression block says so. Our argument "
            "is a conjunction: a universe whose constants sit in a vanishingly narrow "
            "life-permitting window, and whose largest observable structures orient on the "
            "plane of our own orbit. Each is startling; together they are what you would "
            "expect if this place was prepared. You reply that geocentrism makes no "
            "quantitative prediction — but neither does the multiverse, and cosmologists take "
            "that seriously as an explanation of exactly the same fine-tuning. You reply that "
            "the Copernican principle has been tested since 2008 — and every one of those "
            "papers exists because your own field noticed it had been assuming what it had "
            "not measured, which is our point, made by you. And on history: showing that the "
            "medieval centre was the low place does not help you. It shows that 'central' and "
            "'significant' have been welded and unwelded to suit whatever the age wanted to "
            "believe, which is an argument about the sociology of your position as much as "
            "ours."),
        survives=4,
        preemptive=(
            "Rated 4: strong, and largely right about our weakest habit. Three concrete "
            "changes, two of which are now in the published text. (a) Section 7 was written "
            "to answer the cumulative Bayesian form directly rather than only the items — if "
            "a later edit trims it, the multiverse parity point must survive, because it is "
            "the sharpest thing in the defence: the honest reply is that the multiverse is "
            "criticised on exactly that ground by Barnes and others, and that a hypothesis "
            "with no likelihood function cannot be confirmed by a surprise, whoever holds it. "
            "(b) Section 3 was written to concede explicitly that 'Earthward' is the list's "
            "word before answering it, so that the answer is not mistaken for a rebuttal of "
            "the film — the compression block carries the same concession. (c) Still owed and "
            "NOT yet in the text: a sentence acknowledging that the 2008–2011 Copernican "
            "tests were motivated by precisely the gap the movement identified, so that the "
            "steelman's credit is not quietly withdrawn in the refutation. Finally, avoid the "
            "trap the defence sets in its last move: the historical point is not that "
            "'central' means whatever an age wants, it is that this argument imports a "
            "specific modern equation while attacking the narrative that produced it. Say "
            "that, and do not overclaim Danielson into a general thesis about the sociology "
            "of cosmology.")),

    straw_man=dict(
        identified=True,
        detail=("Yes, and it is worth being fair about how it arose. The film's copy puts into "
                "the mouth of cosmology a proposition cosmology does not contain: that we are "
                "'a cosmic accident', of 'utter insignificance', an Earth described in its own "
                "publicity as 'supposedly insignificant'. The Copernican principle as it is "
                "actually used is a statement about spatial homogeneity — that our location is "
                "not dynamically special — and it carries no proposition about human worth "
                "either way. But the movement did not invent the target. A large volume of "
                "popular scientific writing has drawn exactly that rider, under the name "
                "'principle of mediocrity', and readers have met it there. So this is a straw "
                "man of the physics assembled from real quotations of its popularisers, which "
                "is a more interesting failure than fabrication and should be described that "
                "way. Our own straw man to avoid is the mirror image: treating a stated appeal "
                "to meaning as though it were a botched measurement. It is not offered as a "
                "measurement, and answering it as one would be the same move we object to.")),

    compression=dict(
        assessed=True, drifted=True,
        list_phrasing="Fine-tuning favors centrality.",
        source_wording=("&ldquo;<em>are we significant within the structure of the Universe?</em> "
                        "If we were created with a purpose, if we aren't an accident, what does "
                        "this mean for the future of mankind?&rdquo;"),
        drift_type="category_shifted",
        note=("Two moves, in one five-word item. The source's statement of its own thesis is "
              "<strong>interrogative</strong> and <strong>teleological</strong>: it asks whether we "
              "are <em>significant</em>, and what it would mean to have been created with a "
              "<em>purpose</em>. The list item is <strong>declarative</strong> and "
              "<strong>positional</strong>: fine-tuning <em>favors centrality</em>. A question about "
              "worth has become an assertion about place, and the connective doing the work &mdash; "
              "<em>favors</em> &mdash; is the list's contribution. This is the same category shift "
              "recorded at <a href=\"#ARG-A03\">ARG-A03</a>, running from philosophy to physics "
              "rather than from history to physics.<br><br>"
              "The pattern repeats across the cluster. Item 288, &ldquo;cosmological constant "
              "fine-tuned Earthward&rdquo;, attaches a direction to a scalar; the fine-tuning "
              "literature the claim descends from &mdash; Weinberg 1989, Rees's six numbers, Barnes "
              "2012 &mdash; states the puzzle as a value, never as a bearing. Item 187, "
              "&ldquo;infinite universe removes meaning of center&rdquo;, compresses a complaint about "
              "meaning into what reads on a numbered proof list as a cosmological finding. "
              "<strong>The refutation above answers the film's version first</strong> &mdash; the "
              "teleological question, and the cumulative Bayesian form of it, which is the strongest "
              "shape the argument takes &mdash; and answers the fragments separately and second, "
              "because the fragments are what circulate. Also relevant to provenance: on the account "
              "of John Hartnett, a physicist who appears in the film, the film's positional argument "
              "is carried by the redshift shells and the CMB axis, with the fine-tuning material "
              "establishing significance instead. The welding of the two is the list's."))
,
    verdict_challenge=dict(challenged=False, proposed_verdict=None, reasoning=None),

    people=["PER-SUNGENIS"],
    related=["E01", "E17", "D11", "D12", "D14", "D19"],

    sources=[
        dict(label="The Principle — official distributor synopsis (FrontGate Media / PRWeb, "
                   "8 December 2015): the “are we significant within the structure of the "
                   "Universe?” passage quoted above",
             url="https://www.prweb.com/releases/the_controversial_documentary_that_big_science_tried_to_stop_the_principle_available_on_dvd_blu_ray_and_streaming_today/prweb13118958.htm"),
        dict(label="The Principle — earlier distributor release carrying the same synopsis "
                   "(In Ohm Entertainment, PR Newswire, 25 March 2015)",
             url="https://www.prnewswire.com/news-releases/controversial-new-film-the-principle-addresses-one-of-the-most-heated-debates-of-our-timeour-place-in-the-cosmos-300055351.html"),
        dict(label="John Hartnett, “Review of The Principle”, 3 November 2014 — a physicist who "
                   "appears in the film, separating the shells and the axis from the geocentric "
                   "conclusion and declining the latter",
             url="https://biblescienceforum.com/2014/11/03/review-of-the-principle/"),
        dict(label="Variety review of The Principle (2015) — reports the film's appeal to “a "
                   "baby's smile” and “the crescendo of a symphony”",
             url="https://variety.com/2015/film/reviews/film-review-the-principle-1201409088/"),
        dict(label="Weinberg, “The cosmological constant problem”, Rev. Mod. Phys. 61:1 (1989)",
             url="https://ui.adsabs.harvard.edu/abs/1989RvMP...61....1W/abstract"),
        dict(label="Barnes, “The Fine-Tuning of the Universe for Intelligent Life”, PASA 29:529 "
                   "(2012) — the standard review, and explicit that it defends no conclusion "
                   "drawn from fine-tuning",
             url="https://arxiv.org/abs/1112.4647"),
        dict(label="Clifton, Ferreira & Land, “Living in a Void: Testing the Copernican Principle "
                   "with Distant Supernovae”, PRL 101:131302 (2008)",
             url="https://arxiv.org/abs/0807.1443"),
        dict(label="Caldwell & Stebbins, “A Test of the Copernican Principle”, PRL 100:191302 (2008)",
             url="https://link.aps.org/doi/10.1103/PhysRevLett.100.191302"),
        dict(label="Zhang & Stebbins, “Confirmation of the Copernican Principle at Gpc Radial "
                   "Scale and above from the Kinetic Sunyaev-Zel'dovich Effect Power Spectrum”, "
                   "PRL 107:041301 (2011)",
             url="https://www.osti.gov/pages/biblio/1100362-confirmation-copernican-principle-gpc-radial-scale-above-from-kinetic-sunyaev-zel-dovich-effect-power-spectrum"),
        dict(label="Laskar, Joutel & Robutel, “Stabilization of the Earth's obliquity by the "
                   "Moon”, Nature 361:615 (1993) — ±1.3° about 23.3° with the Moon; a chaotic "
                   "zone from near 0° to about 85° without it",
             url="https://www.nature.com/articles/361615a0"),
        dict(label="Danielson, “The great Copernican cliché”, Am. J. Phys. 69:1029 (2001)",
             url="https://pubs.aip.org/aapt/ajp/article-abstract/69/10/1029/1042331/The-great-Copernican-cliche"),
        dict(label="Danielson, “Did Copernicus Dethrone the Earth?” (CSCA pamphlet) — the centre "
                   "as the cosmic low point, and Galileo on the Earth as “the sump where the "
                   "universe's filth and ephemera collect”",
             url="https://www.csca.ca/uploads/resources/pamphlets/danielson-bw.pdf"),
        dict(label="Nicholas of Cusa, De docta ignorantia II.12 §162 (1440), Hopkins translation "
                   "— “its center everywhere and its circumference nowhere”, and the observer on "
                   "the Sun, Earth, Moon or Mars who takes himself to be at the centre",
             url="https://johnplaice.substack.com/p/an-infinite-sphere-whose-centre-is"),
        dict(label="Fine-tuned universe — overview of the parameters usually cited, including "
                   "Rees's six numbers and Λ ≈ 10⁻¹²² in Planck units",
             url="https://en.wikipedia.org/wiki/Fine-tuned_universe")]),
}
