# -*- coding: utf-8 -*-
"""Batch 4 — written 2026-08-02. E01, the CMB "axis of evil" careful case.

The designated hardest case on the list: overclaiming here would be this
review's own worst error. The treatment never says the anomaly is resolved.
It says the opposite, repeatedly, and quotes Planck 2018 VII calling the
features' existence "uncontested".

Two loads are carried by the argument instead:
  1. the axis correlates with the ECLIPTIC, the Galactic plane and our own
     motion — i.e. with local frames, which is evidence about provenance and
     points inward rather than outward
  2. an axis is a DIRECTION, not a CENTRE — and no quantity of anisotropy
     yields a location

D06 and R01 remain at cluster depth.
"""

BATCH4 = {

"E01": dict(
    tldr=("The large-angle CMB alignments are real, reproducible, and still unexplained: "
          "Planck's own isotropy paper calls the existence of these features “uncontested”, "
          "and serious cosmologists continue to argue in print that something needs "
          "explaining. What fails is the step from those features to geocentrism. The axis "
          "lines up with the ecliptic, the Galactic plane, and our own motion through the "
          "CMB — correlations pointing to something local rather than something cosmic — and "
          "in any case an axis is a direction, not a centre."),
    passage=dict(
        work="WRK-PRINCIPLE-2014", pd=False,
        locator=("Official synopsis, as issued in the distributor's press release "
                 "(In Ohm Entertainment, PR Newswire, 25 March 2015); the same wording was "
                 "carried across the film's promotional material."),
        quote=("astonishing results from recent large-scale surveys of our universe—surveys "
               "that disclose unexpected evidence of a preferred direction in the cosmos, "
               "aligned with our supposedly insignificant Earth"),
        gloss="""<p>Twenty-seven words carrying the whole argument in three moves. An appeal to real observational results &mdash; correct, and the film is entitled to it. Then the claim that those results &ldquo;disclose &hellip; a preferred direction in the cosmos&rdquo;. Then, doing the actual work, <em>aligned with our supposedly insignificant Earth</em>, converting a direction on the sky into a statement about Earth's standing in the universe.</p>
<p>Note what the film does <em>not</em> say. It does not claim the Sun orbits a stationary Earth, and offers no cosmological model with parameters. It claims the Copernican principle &mdash; that we occupy no specially favoured location &mdash; has been contradicted by data. That is narrower and more defensible-sounding than &ldquo;the Earth is the centre of the universe&rdquo;, and a rebuttal answering the wider slogan has answered the wrong claim. DeLano and Sungenis produced and wrote the film; Sungenis and Bennett's <em>Galileo Was Wrong</em> is the source of the CMB material and, as with their Michelson&ndash;Gale treatment, is more hedged than the claims descending from it.</p>
<p>The load-bearing word is <em>aligned</em>. Everything turns on what the low multipoles are aligned <em>with</em> &mdash; an answer that is on the record and disputed by nobody.</p>"""),
    steelman=dict(
        description="""<p>Concede this fully, because it is true. The standard model makes a sharp, falsifiable prediction: the CMB temperature field is a realisation of a statistically isotropic Gaussian random field, and no direction is special. A cluster of large-angle features sits uncomfortably against it, found by mainstream cosmologists on mainstream data, and found early. de Oliveira-Costa, Tegmark, Zaldarriaga and Hamilton (PRD 69:063516, 2004) reported the quadrupole low at roughly 1-in-20, the octopole anomalously planar at roughly 1-in-20, and the quadrupole&ndash;octopole alignment anomalous at about 1-in-60. Schwarz, Starkman, Huterer and Copi (PRL 93:221301, 2004) found the two &ldquo;far more correlated (99.97% C.L.) than previously thought&rdquo;. Land and Magueijo (PRL 95:071301, 2005) supplied the name, reporting alignment that &ldquo;extends up to &ell;=5 rejecting statistical isotropy with a probability in excess of 99.9%&rdquo;, and adding they were &ldquo;unable to blame these effects on foreground contamination or large-scale systematic errors&rdquo;.</p>
<p>Nor is it one lonely feature. Copi, Huterer, Schwarz and Starkman (MNRAS 399:295, 2009) report a near-absence of two-point correlation above about 60 degrees outside the Galaxy &ldquo;at a level that would occur in 0.025 per cent of realizations of the concordance model&rdquo;, concluding that absent an undiscovered error &ldquo;the data point towards a violation of statistical isotropy&rdquo;. Alongside sit the hemispherical power asymmetry, the odd-parity preference, and the Cold Spot. Revisiting the set after Planck (CQG 33:184001, 2016), the same four argue that because some pairs of features are demonstrably uncorrelated their combined significance increases, indicating &ldquo;a significant detection of CMB features at angular scales larger than a few degrees on top of the standard model&rdquo;.</p>
<p>The alignments are also durable, which is the part deserving most respect. They survived every WMAP release, a different instrument with a different scan pattern in Planck, and four independent component-separation pipelines. Schwarz et al. state that &ldquo;no systematics and no foregrounds have been identified to explain these apparent violations of statistic isotropy&rdquo;, and that they worsen when the kinematic quadrupole is correctly removed. Planck 2018 VII agrees &ldquo;the existence of these features is uncontested&rdquo;. Patel, Aluri and Ralston (MNRAS 539:542, 2025), across all eight full-sky releases, still find alignments among &ell; = 1, 2, 3 &ldquo;very consistent and robust&rdquo; and conclude &ldquo;it appears that the CMB is not as random as the cosmological principle predicts on large angular scales&rdquo;.</p>
<p>So the kernel is the strong version, not the weak one. &ldquo;The anomalies aren't significant&rdquo; is contested and should not be used. The strong version: <em>the standard model predicts statistical isotropy; several independent-looking large-angle features are in tension with it; the tension has persisted across instruments for two decades; no explanation has been established.</em> Someone pointing at that is pointing at something real, and the people pointing at it include the authors of the Planck analysis papers.</p>""",
        why_it_doesnt_save_claim="""<p><strong>(a) An unexplained feature is not evidence for a specific alternative.</strong> Geocentrism makes no quantitative CMB prediction &mdash; not which multipoles align, not the amplitude, not why the effect is confined to &ell; &lesssim; 5 and vanishes above it, not why the quadrupole is low. A model that would have accommodated any result equally well gains nothing when a surprising one arrives. The anomaly is a gap in one explanation, not confirmation of another.</p>
<p><strong>(b) The alignments are with local frames, not a cosmic one</strong> &mdash; the ecliptic, the Galactic plane, and our own motion. Developed below; it is the heart of the matter.</p>
<p><strong>(c) Polarization has not confirmed it.</strong> Planck 2018 VII reports that on intermediate and large scales &ldquo;no unambiguous detections of cosmological non-Gaussianity, or of anomalies corresponding to those seen in temperature, are claimed&rdquo; &mdash; while carefully adding that polarization data &ldquo;have not been able to refute or confirm the original signal found in temperature&rdquo;. An absence of corroboration, not a contradiction; but a cosmological origin predicted corroboration, and it has not arrived.</p>
<p><strong>(d) An axis is not a centre.</strong> Even granting the anomaly in full and granting it a cosmological origin, a preferred direction says nothing about where the middle of anything is. Decisive on its own.</p>"""),
    refutation="""<p>Begin with what is not in dispute, because overstatement is the biggest error available here. The CMB large-angle anomalies have not been resolved. They are not debunked, not a misreading, not an artefact anyone has identified. They are real, reproducible features that survived twenty years of scrutiny by people trying hard to make them go away, and whether they are a fluke, an unidentified systematic, or new physics is open and argued by capable people on both sides. Nothing below settles it.</p>
<p>The naming history is worth getting right. The anomaly was found by de Oliveira-Costa et al. (2004) and independently characterised by Schwarz et al. (2004); Land and Magueijo coined &ldquo;the axis of evil&rdquo; a year later. Two years after that they revisited their own result against WMAP's three-year data (MNRAS 378:153, 2007), reporting that &ldquo;previous statistics are not robust with respect to the data-sets available and different treatments of the galactic plane&rdquo;. Switching to model selection, they found features significant at &ldquo;the 94-98% level, depending on the particular AOE model&rdquo;, while &ldquo;the Bayesian evidence finds lower significance, ranging from &lsquo;substantial&rsquo; &hellip; to no evidence for the most general AOE model&rdquo;. Not a retraction &mdash; they still find features &mdash; but the authors who named the axis watched its significance fall under a more careful treatment, with mask choice mattering more than expected.</p>
<p><strong>Now the point that matters most, which the synopsis walks straight past.</strong> The question is not <em>whether</em> the low multipoles are aligned, but what they are aligned <em>with</em>. The answer, from the pro-anomaly camp's own papers, is: the ecliptic plane, the Galactic plane, and the CMB dipole &mdash; the plane of our planetary system, the plane of our galaxy, and the direction of our own motion at roughly 370 km/s. Schwarz et al. (2004) found three octopole planes orthogonal to the ecliptic &ldquo;at a level inconsistent with gaussian random statistically isotropic skies at 99.8% C.L.&rdquo;, with normals aligned &ldquo;at 99.9% C.L. with the direction of the cosmological dipole and with the equinoxes&rdquo;. Their 2016 review quantifies it again: perpendicular to the ecliptic at p-values of 2&ndash;4%, aligned with the Galactic pole at 0.8&ndash;1.6%, and strongest of all, aligned with the dipole direction at 0.09&ndash;0.37%. Their own abstract describes alignment of the lowest multipoles &ldquo;with one another and with the motion and geometry of the Solar System&rdquo;.</p>
<p>Sit with what that means. The CMB was emitted about 380,000 years ago from a surface some 45 billion light years away in comoving terms. The ecliptic is the plane in which a few rocks orbit one ordinary star, fixed by the angular momentum of a gas cloud that collapsed roughly nine billion years <em>after</em> that light departed. The two have no causal contact and no common cause. A primordial signal has no way of knowing the orientation of our planetary system and no reason to care. So when a signal claiming to be cosmological lines up with our orbital plane, our galaxy's plane, and our velocity vector, the conventional reading in observational astronomy is that part of it is <em>not coming from where it appears to come from</em> &mdash; zodiacal dust, foreground residuals, imperfect kinematic-quadrupole subtraction, or the satellite's own scan pattern, all of which live in ecliptic-referenced coordinates, because that is the frame the spacecraft flies in.</p>
<p>Be precise about how strong that claim is. No such contaminant has been identified; Schwarz et al. say so in as many words, and note the alignments are exacerbated, not relieved, by proper removal of the kinematic quadrupole. The argument is not &ldquo;it's dust, case closed&rdquo;. It is about the direction of inference. Correlation with local structure is evidence about <em>where the signal comes from</em>, and it points inward, toward the solar system, not outward toward cosmology &mdash; the precise opposite of what a geocentric reading needs. Geocentrism requires the axis to be cosmological in order to say anything about the cosmos at all, and the one property making the axis look special &mdash; its correlation with our local frame &mdash; is the very property arguing most against a cosmological origin. However this resolves, none of the three live options is geocentrism, and the option best explaining the solar-system correlation is the one where the signal is partly not cosmological at all.</p>
<p><strong>And now the point that survives even if every concern above were answered: an axis is not a centre.</strong> Suppose tomorrow the alignment were confirmed beyond doubt, seen in polarization, traced to primordial physics and given a mechanism. What would we have? A preferred <em>direction</em> &mdash; an axis, a line, an orientation. A direction has no midpoint. Every observer anywhere in a universe with a preferred axis sees that same axis, because an axis is a property of the field, not of a location in it. A galaxy ten billion light years away would see it too, and be no more and no less &ldquo;central&rdquo; for seeing it. Centrality is a claim about position, anisotropy a claim about orientation, and no quantity of the second yields the first. The synopsis performs the entire slide in one phrase &mdash; &ldquo;a preferred direction in the cosmos, aligned with our supposedly insignificant Earth&rdquo; &mdash; where the direction is the finding and Earth's significance is the conclusion, with nothing in between. Nothing <em>can</em> go in between.</p>
<p>Two further tests, at their real strength rather than inflated. Polarization is a partly independent observable, sourced at the same epoch by the same fluctuations but measured through a different systematic chain, and the natural place to seek a temperature anomaly's counterpart. Planck 2018 VII reports that for &ell; &lesssim; 400, &ldquo;no unambiguous detections of cosmological non-Gaussianity, or of anomalies corresponding to those seen in temperature, are claimed&rdquo;. The honest caveat, supplied by Planck itself: residual large-scale polarization systematics remain, and the polarization data &ldquo;have not been able to refute or confirm the original signal found in temperature&rdquo;. A test a cosmological interpretation needed to pass and has not yet passed, not one it failed. Then the a posteriori problem. Bennett et al. (ApJS 192:17, 2011), the WMAP team's own assessment, concluded &ldquo;in most cases we find that claimed anomalies depend on posterior selection of some aspect or subset of the data&rdquo;. Planck 2018 VII is more even-handed: the features' existence is uncontested, but &ldquo;given the modest significances at which they deviate from the standard &Lambda;CDM cosmological model, and the a posteriori nature of their detection, the extent to which they provide evidence for a violation of isotropy in the CMB remains unclear&rdquo;. Both sides know this argument; Schwarz et al. reply that the alignments were carried forward into new datasets rather than mined afresh, which is fair, and part of why the question is live.</p>
<p>On the film's standing, briefly. <em>The Principle</em> was released 24 October 2014. Its narrator, Kate Mulgrew, disavowed it on 8 April 2014: &ldquo;I am not a geocentrist, nor am I in any way a proponent of geocentrism&rdquo;, adding that she had been &ldquo;a voice for hire, and a misinformed one, at that&rdquo;. Lawrence Krauss, Michio Kaku, Max Tegmark, George Ellis and Julian Barbour all objected to the use of their interviews. This does not refute the argument &mdash; arguments stand or fall on their own &mdash; but the appearance of five prominent cosmologists is not endorsement of anything in it.</p>
<p>Where this leaves the entry. The anomaly is unresolved and should be described that way until it is not: as recently as 2025, Patel, Aluri and Ralston found the &ell; = 1, 2, 3 alignments &ldquo;very consistent and robust&rdquo; across all eight full-sky releases, while noting that broadening the search dilutes significance. That is the present state &mdash; a durable, unexplained, modestly significant tension in the largest-scale CMB modes, with reasonable cosmologists disagreeing about what it portends. The MISLEADING verdict attaches to none of that. It attaches to the passage from it to &ldquo;aligned with our supposedly insignificant Earth&rdquo;: a passage requiring the axis to be cosmological when its defining correlation is with our own solar system, requiring corroboration polarization has not supplied, and requiring a direction to specify a location, which no direction can do.</p>""",
    straw_man=dict(
        identified=True,
        detail=("Two straw men are live and both are easy to fall into. The first is OURS: "
                "presenting the CMB anomalies as resolved, refuted, or explained away. They are "
                "none of these. Planck 2018 VII calls their existence uncontested, Schwarz et "
                "al. (2016) state no systematic or foreground has been identified to explain "
                "them, and Patel et al. (2025) still find the low-multipole alignments robust "
                "across all eight public releases. Any rebuttal built on “the anomaly went away” "
                "is false and would be dismantled by anyone who has read the literature. The "
                "second is a straw man of the source: the film does not claim to have measured "
                "Earth at the centre of the universe. Its own synopsis claims evidence of “a "
                "preferred direction in the cosmos, aligned with our supposedly insignificant "
                "Earth” — a challenge to the Copernican principle, not a positive geocentric "
                "measurement. Sungenis and Bennett's book is likewise more hedged than the list "
                "items derived from it, the same pattern already documented for their "
                "Michelson–Gale material.")),
    verdict_challenge=dict(challenged=False, proposed_verdict=None, reasoning=None),
    people=["PER-SUNGENIS"],
    related=["E02", "E03", "E11", "E17", "R12"],
    advocate=dict(
        survives=3,
        best_defense=("The strongest defence does not assert geocentrism outright. It runs: the "
                      "Copernican principle is an assumption built into the FLRW metric at the "
                      "foundation of modern cosmology, not an observation; the standard model's "
                      "prediction of statistical isotropy is sharp; and several large-angle "
                      "features, some demonstrably uncorrelated with each other, have been in "
                      "tension with that prediction for two decades across two satellites and "
                      "multiple independent cleaning pipelines. No systematic and no foreground "
                      "has ever been identified to account for them, and the people saying so "
                      "are Schwarz, Copi, Huterer and Starkman in Classical and Quantum Gravity. "
                      "Against that, the a posteriori objection is a general-purpose solvent that "
                      "could be poured on any unexpected result, and Planck itself calls the "
                      "polarization test not yet decisive either way. So the honest state of play "
                      "is an unexplained tension with the cosmological principle's central "
                      "prediction, and it is at minimum reasonable to say the assumption that we "
                      "occupy no special place is under observational strain rather than "
                      "confirmed."),
        preemptive=("Three moves a well-read defender will make. (1) “You are invoking the "
                    "look-elsewhere effect to dismiss inconvenient data.” Then do not lean on it. "
                    "Concede it cuts both ways and note Planck itself calls the features' "
                    "existence uncontested; this argument does not need the anomaly to be a "
                    "fluke. (2) “The ecliptic correlation could itself be the new physics.” "
                    "Correct, and the response does not assume otherwise — no contaminant has "
                    "been identified, and Schwarz et al. say so. The claim is narrower: "
                    "correlation with our orbital plane, our galaxy's plane and our velocity "
                    "vector is evidence about provenance, and it points local. A defender "
                    "insisting the solar-system correlation is genuinely cosmological now owes a "
                    "mechanism by which primordial perturbations knew the orientation of a "
                    "planetary system formed nine billion years later — a far heavier debt than "
                    "the one they are trying to collect. (3) “Fine, but it shows the universe has "
                    "a preferred frame.” Grant it entirely and lose nothing. A frame or axis is "
                    "an orientation; it fixes no origin. Ask what observation would distinguish "
                    "Earth-at-the-centre from any other location in an axis-bearing universe — "
                    "the answer is none, because every observer sees the same axis.")),
    sources=[
        dict(label="Land & Magueijo, “The axis of evil”, PRL 95:071301 (2005) — coinage",
             url="https://arxiv.org/abs/astro-ph/0502237"),
        dict(label="Land & Magueijo, “The Axis of Evil revisited”, MNRAS 378:153 (2007) — the authors' own reassessment",
             url="https://arxiv.org/abs/astro-ph/0611518"),
        dict(label="de Oliveira-Costa, Tegmark, Zaldarriaga & Hamilton, PRD 69:063516 (2004) — original quadrupole/octopole anomalies",
             url="https://arxiv.org/abs/astro-ph/0307282"),
        dict(label="Schwarz, Starkman, Huterer & Copi, “Is the low-l microwave background cosmic?”, PRL 93:221301 (2004) — the ecliptic and dipole alignments",
             url="https://arxiv.org/abs/astro-ph/0403353"),
        dict(label="Bennett et al., “Are There Cosmic Microwave Background Anomalies?”, ApJS 192:17 (2011) — WMAP team assessment",
             url="https://arxiv.org/abs/1001.4758"),
        dict(label="Planck 2018 results VII, Isotropy and Statistics of the CMB, A&A 641:A7 (2020)",
             url="https://arxiv.org/abs/1906.02552"),
        dict(label="Planck 2018 VII — A&A full text (look-elsewhere and polarization passages)",
             url="https://www.aanda.org/articles/aa/full_html/2020/09/aa35201-19/aa35201-19.html"),
        dict(label="Schwarz, Copi, Huterer & Starkman, “CMB Anomalies after Planck”, CQG 33:184001 (2016) — the pro-anomaly case",
             url="https://arxiv.org/abs/1510.07929"),
        dict(label="Copi, Huterer, Schwarz & Starkman, “No large-angle correlations on the non-Galactic microwave sky”, MNRAS 399:295 (2009)",
             url="https://arxiv.org/abs/0808.3767"),
        dict(label="Patel, Aluri & Ralston, MNRAS 539:542 (2025) — PR4-era assessment, alignments still robust",
             url="https://academic.oup.com/mnras/article/539/1/542/8088428"),
        dict(label="Krauss on his appearance in The Principle, Slate, 8 April 2014",
             url="https://slate.com/technology/2014/04/lawrence-krauss-on-ending-up-in-the-geocentrism-documentary-the-principle.html"),
        dict(label="Kate Mulgrew's disavowal, 8 April 2014",
             url="https://blog.trekcore.com/2014/04/kate-mulgrew-speaks-out-against-geocentrism-film/"),
        dict(label="The Principle — distributor press release containing the official synopsis quoted above",
             url="https://www.prnewswire.com/news-releases/controversial-new-film-the-principle-addresses-one-of-the-most-heated-debates-of-our-timeour-place-in-the-cosmos-300055351.html")]),
}
