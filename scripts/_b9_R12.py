# -*- coding: utf-8 -*-
"""
Batch 9 — ARG-R12, "The Copernican principle is an unproven assumption".
1 item (354, "Copernican principle assumption."), lane A-REL, verdict REFUTED.

Research notes for whoever picks this up next, ordered by how much they change the entry.

0. THE BRIEF ASKED WHETHER THE CLASSIFICATION IS WRONG. IT IS NOT, AND THE FRONT PAGE
   DOES NOT MOVE. R12 is the one post-1950 argument outside lane E, and the two-clocks
   paragraph subtracts it to reach "nine are misappropriated astronomy". Three separate
   checks, all of which came back the same way:
     (a) Is it really post-1950? Yes, under any defensible choice of `real_source`. The
         work this argument actually points at is Bondi's Cosmology (1952/1960), Hawking
         & Ellis 1973, Gale in Scientific American 1981, Clifton/Ferreira/Land 2008 and
         Ellis's CQG review of 2011. The earliest of those is 1952. `_YR` takes the first
         four-digit year in the string, so every candidate rewrite still lands >= 1950 and
         `post1950_cited_clusters` keeps its ten members.
     (b) Is it really outside lane E? Yes, on the substance and not only on the label.
         Lane E is "data gathered by other people for other purposes and reinterpreted" —
         CMB maps, quasar catalogues, the Pioneer residual. R12 reinterprets other
         people's *methodological statements*: Ellis conceding that homogeneity is assumed
         rather than observed. That is a different move from misreading a survey, and the
         page's carve-out is correct.
     (c) Is A-REL the right home? Loosely. The lane comment in clusters.py reads
         "relativity/coordinates", and the Copernican principle is neither. But A-REL is
         already the underdetermination lane in practice — R09 is the conventionality of
         simultaneity, R11 is "no falsifier distinguishes the frames" — and R12 belongs
         with R11 more than with anything in E. Recommend leaving it and widening the lane
         comment; recorded in record_problems, clusters.py NOT touched.
   Net: the front page stands. The weakness is that the sentence subtracts the exception
   without naming it, so a reader is told "nine of ten" and never learns what the tenth
   is — and the tenth is the interesting one. That is a render.py note, not an R12 one.

1. THE ITEM ASSIGNMENT IS CORRECT AND I NEARLY FILED A FALSE DEFECT ABOUT IT. corpus.ITEMS
   is a LIST and item N sits at index N-1 (tests/test_provenance.py:47 pins this with
   ITEMS[460] for item 461). Read it as a dict-alike and 354 comes back "Redshift
   quantization concentric.", which is E12's subject, and the whole 351-355 block looks
   shifted by one. It is not. Item 354 is "Copernican principle assumption.", E12 holds
   items 60 and 355 and both are redshift-quantization items, D14 holds the dark-matter
   and MOND items. Verified against data/flat-earth-origins-provenance.json, which is
   built from the same tables and prints item_no explicitly. Do not re-raise this.

2. THE SOURCE PREDATES THE WORK WE CREDIT. clusters.py records originator_work "The
   Principle (film)", year 2014. The argument is in the earlier CD edition of Galileo Was
   Wrong Vol. I (ISBN 0-9779640-0-0, Catholic Apologetics International; galley submitted
   to Cardinal Levada, who was CDF Prefect from 2005), chapter 3, printed p. 145, in the
   same words as the seventh edition of 2013 at printed p. 309 — "Downright fearful of
   geocentrism ... Hence, the 'Copernican principle,' nowadays camouflaged by the term
   'cosmological principle' ... It is taken as an a-priori truth to which the rest of
   cosmology must conform." So the byline "Robert Sungenis & Robert Bennett" is right and
   the work/year pinned to it is not: Bennett is the book's co-author, while the film was
   produced by DeLano and Sungenis (works.py says so itself in WRK-PRINCIPLE-2014, and
   E11 records the film as "Robert Sungenis & Rick DeLano"). This entry quotes and cites
   the book only. Reported in record_problems; clusters.py NOT touched.

3. THE HEDGE RUNS THE OTHER WAY FROM THE USUAL, AND IT MATTERS FOR THE DRIFT TYPE. Most
   list items overstate a cautious source. Here the source is not cautious — but its claim
   is a NEGATIVE one about the other side's foundation ("you assumed this; you did not
   show it"), which is a ground-clearing move, not a proof of anything. The list files it
   as proof item 354 in a numbered list of proofs. Wording preserved, speech act changed:
   that is `force_upgraded`, the R01 pattern. `category_shifted` was the other candidate
   and was rejected because the four-word item asserts nothing physical on its face; the
   upgrade is in what a numbered proof list does to a parity claim, not in the words.
   Note also that DeLano's blog runs the argument far harder than the book does
   ("Copernican Principle, 1532-2013, RIP"), so if a future pass moves the originator_work
   to the film, the drift assessment has to be redone against DeLano, not against Bennett.

4. THE REFUTATION'S SPINE IS THAT THE SOURCE'S OWN FOOTNOTE ANSWERS IT. Sungenis quotes
   Ellis, arXiv:1103.2335 (CQG 28:164001, submitted 11 March 2011), at his footnote 427,
   citing "pp. 19, 5" — accurately, including the ellipsis that joins the conclusion back
   to p. 5. The sentence he takes is on p. 19: "standard CMB anisotropy studies do not
   prove the Copernican principle: they assume it at the start." Five pages earlier the
   same paper says the assumption "is indeed at least partly testable via measurements of
   CMB spectrum distortions", opens a section headed "Observational tests of spatial
   homogeneity", and lists four kinds of test. Its reference [128] is Zhang & Stebbins.
   Same for the Caldwell line the book quotes as a wish — "It would be great if there were
   someone out there who could look back at us and tell us if we're in a void", Marcus
   Chown, New Scientist, 12 Nov 2008, p. 33. Caldwell & Stebbins had published the paper
   doing exactly that six months earlier (PRL 100:191302, May 2008; the reionized universe
   as a mirror). Both quotations are real, both are in context, and both describe work
   that had already been done or was being called for by the man quoted.

5. NUMBERS, ALL FROM THE PAPERS AND CHECKABLE — AND MIND THE arXiv VERSION. Zhang &
   Stebbins is quoted here from the PUBLISHED text, arXiv v3, which is what the abs URL in
   the sources list serves. v3: SPT 95% upper limit dT^2 < 6.5 uK^2 at l = 3000, ACT
   dT^2 < 8 uK^2 at the same scale, i.e. SPT is the TIGHTER bound and the one the headline
   comparison is made against; Hubble-bubble models within the 3 sigma UNION2 supernova
   contour predict dT_H^2 > 10^3 uK^2 at the same multipole, "two orders of magnitude
   larger than the SPT upper limit"; models retuned to be consistent with the SPT result
   then fail the supernovae with delta-chi^2 > 209 (chi^2 > 814); only voids with
   Omega_0 -> 1 (>~ 0.8) or z_edge -> 0 (<~ 0.2, radius <~ 0.6 h^-1 Gpc) survive the kSZ
   test. THE SUPERSEDED v2 GIVES SPT < 13 uK^2 AND delta-chi^2 > 195 (against ACT); an
   earlier draft of this entry carried those two v2 figures and they have been corrected.
   Do not re-import them. The model-independent bound in v3 is |dH(z)/H(z)| < ~1% per mass
   shell of radial width ~1 h^-1 Gpc. Ellis's own "typical observationally viable model"
   has the observer "within 10% of the central position" of a void of size 160-250 h^-1
   Mpc, underdensity stretching to z ~ 0.08, "and no dark energy or quintessence field" —
   which sits INSIDE the window that survives the kSZ bound, and is therefore a specimen
   the supernova leg of the test excludes, not the kSZ leg. Section four now says so.

6. THE LIVE PART IS REAL AND THE PAGE SAYS SO — E01 PRECEDENT. Ellis in 2011 registered
   the kSZ claims as contested (Clarkson & Regis, JCAP 02:013, argued the LTB models were
   only weakly constrained because the analyses fixed the bang-time function and used
   FLRW perturbation theory). Bull, Clifton & Ferreira 2012 (PRD 85:024002) answered that
   specific objection by relaxing the bang time and still ruled the models out; note that
   Clifton and Ferreira are the "Living in a Void" authors, i.e. the proposal's own
   proponents closed it. Separately and still open: the number-count dipole. Secrest et
   al. 2021 (ApJL 908:L51) reported 4.9 sigma against the kinematic reading; 2022 (ApJL
   937:L31) a 5.1 sigma joint significance; Bashir, Chingangbam & Appleby (arXiv, 2 Nov
   2025) redid CatWISE2020 with clustering and mask systematics and got 3.27-3.63 sigma,
   "although the anomaly is reduced, it cannot be explained solely by the clustering
   dipole or mode coupling from the survey mask." Anyone writing that the cosmological
   principle is settled in 2026 will lose the exchange. The entry concedes it and then
   shows the anomaly is an AMPLITUDE anomaly in roughly the CMB dipole's own direction,
   which is a problem for LambdaCDM and not a centre for the Earth.

7. VERDICT KEPT AT REFUTED, AND MISLEADING WAS SERIOUSLY CONSIDERED. The bare proposition
   "it is an assumption" is true and REFUTED would be wrong for it. The source's claim is
   larger — that the principle is philosophical rather than scientific and overrides
   evidence — and that larger claim is contradicted by specific measurements, which is the
   rubric's definition. The basis line in clusters.py is looser than the paper supports,
   though: "rules out Gpc-scale off-centre void models" should be "rules out the void
   models deep enough to mimic dark energy", since the kSZ signal comes from distant
   observers being off-centre while the constrained quantity is radial inhomogeneity, and
   voids below ~0.6 h^-1 Gpc survive. THIS IS STILL NOT APPLIED. The R12 `note` in
   clusters.py is outside this file's ownership and no record_problems file exists in the
   repository, so the wrong line is live under the REFUTED chip on docs/index.html. The
   exact replacement wanted, anchored on the "R12" key and never on the originator= line:
     "It is not merely assumed — it is tested. The kSZ power spectrum rules out the LTB
      void models deep enough to mimic dark energy."
   Re-reported to the integrator rather than actioned here.
"""

ENTRY = {

"R12": dict(

    tldr=("This is true, and the field says so in its own journals: the Copernican principle "
          "was an assumption, and the very paper cited against it on this page opens by "
          "granting that it “remains largely unproven at Gpc radial scale and above.” What "
          "happened next is the answer. Because it was an assumption, cosmologists built "
          "tests for it — using distant electrons as mirrors to see the microwave background "
          "from somebody else's vantage point — and the radial inhomogeneity deep enough to "
          "fake dark energy overshoots the measured limit by two orders of magnitude. And a "
          "clean win would buy nothing here: the models at stake put us near the middle of a "
          "void hundreds of millions of light-years across, still expanding, with the Earth "
          "still in orbit around the Sun."),

    passage=dict(
        work="WRK-SUNGENIS-2006",
        pd=False,
        locator=("Vol. I, chapter 1, “The New Galileo and the Truth about Copernicanism”, "
                 "printed p. 92 of the seventh edition (2013); read in the Internet Archive "
                 "three-volume scan (item galileo-was-wrong-the-church-was-right-sungenis-"
                 "vol-1-3-complete), djvu text line 5,917. Not checked against a print copy."),
        quote=("This clearly shows that the Copernican Principle from which modern science "
               "creates its interpretations of the cosmological data is not scientific but "
               "philosophical. In other words, even if the empirical evidence shows Earth is "
               "not moving, the ever-present Copernican Principle requires that every piece "
               "of scientific data must be interpreted by assuming the earth is moving…"),
        gloss="""<p><strong>Read what is being claimed, because it is bigger than the item.</strong> The four-word list entry says only that the Copernican principle is an assumption. The book says that it is a <em>philosophical</em> assumption which <em>overrides evidence</em> &mdash; that a datum showing a stationary Earth would still be read the other way, because the principle decides in advance how every datum is read. That is a checkable charge about scientific practice, and it is the one answered below. The bare version is not worth answering: it is true, and it is stated in the same words by the paper this page cites against it.</p>
<p><strong>The dedicated treatment is in chapter 3</strong>, &ldquo;Evidence Earth is in the Center of the Universe&rdquo;, at printed pp. 308&ndash;311 of the seventh edition, where the principle is called something &ldquo;taken as an a-priori truth to which the rest of cosmology must conform.&rdquo; The same paragraph, word for word, is in the earlier CD edition of Volume I (ISBN 0-9779640-0-0) at printed p. 145, so the argument is the book&rsquo;s and predates the 2014 film by the better part of a decade. This treatment therefore quotes and cites the book, whose byline &mdash; Sungenis and Bennett &mdash; is the one our record carries.</p>
<p><strong>The chapter is built almost entirely out of working cosmologists&rsquo; own words</strong>, and quoted accurately: Bondi&rsquo;s <em>Cosmology</em>, Hawking and Ellis&rsquo;s <em>The Large Scale Structure of Space-Time</em>, George Gale in <em>Scientific American</em> (1981), Ellis&rsquo;s 1995 <em>Scientific American</em> profile, Clifton, Ferreira and Land&rsquo;s 2008 supernova paper, and Ellis&rsquo;s 2011 review of inhomogeneity effects. Nothing here turns on a misquotation. It turns on where each quotation is cut &mdash; which is a harder problem, and the subject of section 3 below.</p>"""),

    steelman=dict(
        description="""<p><strong>SURFACE (weak &mdash; do not use).</strong> &ldquo;The Copernican principle is not an assumption, it is proven.&rdquo; This loses immediately. The paper that closed the loophole opens: <em>&ldquo;The Copernican principle, a cornerstone of modern cosmology, remains largely unproven at Gpc radial scale and above&rdquo;</em> (Zhang &amp; Stebbins, PRL 107:041301). Anyone who denies the premise is contradicted by the citation they are about to make.</p>
<p><strong>DEEPER.</strong> &ldquo;It is an assumption, but a testable one, and it has been tested.&rdquo; True, and still incomplete, because it invites the obvious reply: the tests were run inside a framework that already assumes what they check, using structure-growth and foreground models built on &Lambda;CDM.</p>
<p><strong>KERNEL.</strong> The strongest form is a theorem, not a grievance, and it is George Ellis&rsquo;s. We observe the universe from essentially one point on one worldline, and the finite speed of light mixes distance with time, so <em>isotropy is directly observable and homogeneity is not</em>. The standard argument bridges the gap with the Ehlers&ndash;Geren&ndash;Sachs theorem &mdash; if every observer sees an isotropic background, the geometry is Friedmann&ndash;Lema&icirc;tre&ndash;Robertson&ndash;Walker &mdash; and the phrase &ldquo;every observer&rdquo; is doing work no telescope can do for us. Worse for the standard picture, and this is a published theorem rather than a worry: Mustapha, Hellaby and Ellis (<em>MNRAS</em> 292:817, 1997) proved that <em>&ldquo;homogeneity cannot be proven without either a fully determinate theory of source evolution, or availability of distance measures that are independent of source evolution&rdquo;</em> &mdash; a spherically symmetric Lema&icirc;tre&ndash;Tolman&ndash;Bondi model carries two free radial functions, and the freedom is enough to fit isotropic observations. So the underdetermination is exact, it is proved, and its author says out loud that cosmology chooses among the survivors on philosophical criteria: <em>&ldquo;I can construct you a spherically symmetrical universe with Earth at its center, and you cannot disprove it based on observations. You can only exclude it on philosophical grounds &hellip; A lot of cosmology tries to hide that.&rdquo;</em> That is Ellis in <em>Scientific American</em>, October 1995, read here as quoted at printed p. 310 of the seventh edition of <em>Galileo Was Wrong</em>; the magazine text itself was reachable only behind a paywall from here, so the wording is reported at one remove. Concede every word of it.</p>""",
        why_it_doesnt_save_claim="""<p>Because the man who proved the underdetermination also spent thirty years building the instruments that break it, and the book quotes the complaint without the programme. Ellis&rsquo;s point was never &ldquo;therefore we cannot know&rdquo;; it was <em>&ldquo;precisely because of the foundational nature of the Copernican Principle for standard cosmology, we need to fully check this foundation.&rdquo;</em> That is a work order. It was filled.</p>
<p>Goodman proposed using scattered CMB photons to look at the sky from somewhere else in 1995. Caldwell and Stebbins turned it into a bound in 2008, treating the reionized universe as a mirror. Clarkson, Bassett and Lu produced a consistency test the same year that depends only on the geometry being Robertson&ndash;Walker &mdash; independent of curvature, of dark energy, of what the matter is and of the theory of gravity &mdash; which is exactly the model-independence the circularity objection demands. Clifton, Ferreira and Land showed the void and dark-energy readings separate in the redshift dependence of luminosity distance around <em>z</em> ~ 0.1&ndash;0.4. Uzan, Clarkson and Ellis proposed watching redshifts drift. Zhang and Stebbins then closed the largest gap with the kinetic Sunyaev&ndash;Zel&rsquo;dovich power spectrum.</p>
<p>So the kernel points the other way at the exact step it was supposed to defend. An unexamined assumption that gets examined stops being an unexamined assumption; that is what happened here, in refereed journals, mostly before the seventh edition went to press. And the theorem never had the reach the argument needs anyway: the freedom Mustapha, Hellaby and Ellis established is the freedom to fit <em>isotropic</em> observations with a radially inhomogeneous model. It says nothing whatever about whether the Earth goes round the Sun.</p>"""),

    refutation="""<p><strong>First, the concession, and it is not grudging.</strong> The Copernican principle is an assumption. It was named after Copernicus rather than by him, its modern cosmological form dates to Bondi around 1948&ndash;1952, and it is a postulate about the large-scale distribution of matter that was adopted because it makes the equations tractable and the models predictive. The source&rsquo;s own quoted authority says so plainly &mdash; George Gale in <em>Scientific American</em>, quoted at printed p. 309 of the seventh edition, dates the extended form to Bondi in 1948. And the paper this page cites in answer says so in its first sentence: <em>&ldquo;The Copernican principle, a cornerstone of modern cosmology, remains largely unproven at Gpc radial scale and above.&rdquo;</em> A rebuttal that begins by denying the premise has already lost.</p>

<p><strong>Second, why it was an assumption, which is a better story than either side usually tells.</strong> We observe from what is effectively a single point, and every cosmological observation looks down a light cone that mixes how far away a thing is with how long ago it was. Isotropy &mdash; the sky looking the same in all directions &mdash; we can measure directly. Homogeneity &mdash; the universe looking the same <em>from other places</em> &mdash; we cannot, not by looking. The classical bridge is the Ehlers&ndash;Geren&ndash;Sachs theorem: if the background radiation is isotropic for <em>every</em> observer in an expanding universe, the geometry has to be Friedmann&ndash;Lema&icirc;tre&ndash;Robertson&ndash;Walker. The words &ldquo;every observer&rdquo; are the assumption, and they carry the whole standard model. Sungenis and Bennett have located a real load-bearing beam.</p>

<p><strong>Third, the sentence they quote, and the five pages in front of it.</strong> The book&rsquo;s strongest single citation is Ellis&rsquo;s 2011 review <em>Inhomogeneity effects in Cosmology</em> (arXiv:1103.2335; <em>Class. Quantum Grav.</em> 28:164001), footnote 427, cited to &ldquo;pp. 19, 5&rdquo;. The quoted line is real and is on p. 19: <em>&ldquo;Precisely because of the foundational nature of the Copernican Principle for standard cosmology, we need to fully check this foundation. And one must emphasize here that standard CMB anisotropy studies do not prove the Copernican principle: they assume it at the start.&rdquo;</em> What the same paper carries on p. 14, under the heading <em>The argument for homogeneity</em>, is this: <em>&ldquo;However it is now known that this assumption is indeed at least partly testable via measurements of CMB spectrum distortions, as will be discussed below. There are a number of other observational tests of the Copernican principle that are now possible, because of observational improvements in the past decade.&rdquo;</em> Section 4.4 is headed <em>Observational tests of spatial homogeneity</em> and sets out four kinds. Reference [128] of that paper is Zhang and Stebbins. The demand and its answer are in the same document, five pages apart, and the book carries the demand.</p>

<p>The pattern repeats with the other quotation the chapter leans on. At printed p. 320 it quotes Robert Caldwell wishing for an outside view &mdash; <em>&ldquo;It would be great if there were someone out there who could look back at us and tell us if we&rsquo;re in a void&rdquo;</em> (Marcus Chown, <em>New Scientist</em>, 12 November 2008, p. 33). Caldwell had published that experiment with Stebbins six months earlier, in May 2008: use the reionized universe as a mirror, let it scatter background photons back to us, and read off what the sky looks like from out there. The wish in the quotation had already been granted by the man being quoted.</p>

<p><strong>Fourth, the measurement, with the numbers.</strong> A universe that violates the Copernican principle radially &mdash; a deep void with us near the middle, big enough to fake cosmic acceleration &mdash; makes distant matter move relative to the background radiation, and that relative motion prints a kinetic Sunyaev&ndash;Zel&rsquo;dovich signal on the small-angle microwave sky. Zhang and Stebbins computed it. The observed ceiling comes from two experiments at multipole &#8467; = 3000: the South Pole Telescope&rsquo;s 95% upper limit of &Delta;<em>T</em>&sup2; &lt; 6.5 &micro;K&sup2;, the tighter of the two, and the Atacama Cosmology Telescope&rsquo;s &Delta;<em>T</em>&sup2; &lt; 8 &micro;K&sup2; at the same angular scale. Void models within the 3&sigma; contour of the UNION2 supernova fit predict &Delta;<em>T</em>&sup2; above 10&sup3; &micro;K&sup2; &mdash; in the paper&rsquo;s words, <em>&ldquo;two orders of magnitude larger than the SPT upper limit&rdquo;</em> &mdash; and the models retuned to slip under that limit then miss the supernovae by &Delta;&chi;&sup2; &gt; 209. Stated model-independently, the deviation of any ~1 <em>h</em>&#8315;&sup1; Gpc shell from the overall expansion is held to about 1%. The paper is equally explicit about where the kSZ leg of the test stops, and so is this page: voids shallow enough (&Omega;<sub>0</sub> above about 0.8) or small enough that the underdensity ends below <em>z</em> &asymp; 0.2 &mdash; radius under about 0.6 <em>h</em>&#8315;&sup1; Gpc &mdash; survive the kSZ bound, and are caught instead by the supernovae. That is why the two tests are always quoted together, and it is worth holding on to for section six. What the pair of them did is turn the principle from a postulate into a number with an error bar, and that is the specific measurement the verdict rests on.</p>

<p><strong>Fifth, be honest about what is still open, because two things are.</strong> Ellis in 2011 recorded the kSZ claims as contested: Clarkson and Regis had argued the void models were only weakly constrained because the analyses fixed the Lema&icirc;tre&ndash;Tolman&ndash;Bondi &ldquo;bang time&rdquo; function and studied structure formation with the wrong perturbation theory. That objection was answered on its own terms in 2012 by Bull, Clifton and Ferreira (<em>Phys. Rev. D</em> 85:024002), who let the bang time vary and found the extra freedom sufficient for individual observables but not for the supernovae, the small-angle CMB, the local Hubble rate and the kSZ effect together &mdash; and Clifton and Ferreira are the authors of &ldquo;Living in a Void&rdquo;, so the proposal was closed by its own proponents.</p>

<p>The second is not closed at all. The number-count dipole in radio and infrared source catalogues points roughly where the microwave-background dipole points but is about twice as large, which conflicts with reading the CMB dipole as pure motion. Secrest and colleagues put it at 4.9&sigma; with 1.36 million CatWISE quasars in 2021 and at a 5.1&sigma; joint significance across radio galaxies and quasars in 2022. A November 2025 reassessment of the same catalogue, with lognormal simulations of clustering, bias, selection and the survey mask, brings it down to 3.3&ndash;3.6&sigma; and concludes that the anomaly is reduced but not accounted for by clustering or mask coupling. <strong>So the cosmological principle is under live empirical strain right now, and this page says so.</strong> But look at what the strain is: the dipole is in roughly the right <em>direction</em> and the wrong <em>amplitude</em>. It is evidence that our inferred velocity is not the whole story. It is not a compass pointing at the Earth, and it is worth noting that the same list treats the CMB dipole as fictitious elsewhere while this anomaly is defined by comparison with it.</p>

<p><strong>Sixth, and decisively: suppose the principle failed tomorrow.</strong> What has actually been built and fitted is a Lema&icirc;tre&ndash;Tolman&ndash;Bondi void. Ellis&rsquo;s own specimen of an observationally viable one has the observer &ldquo;within 10% of the central position&rdquo; of an underdense region 160&ndash;250 <em>h</em>&#8315;&sup1; Mpc across &mdash; which puts it inside the window flagged in section four: small enough to slip under the kSZ bound, and left to the supernovae to exclude. And the LTB family is not the whole of the inhomogeneous literature, as the same review says in the next breath: <em>&ldquo;Actually you don&rsquo;t need a void to explain the observations; more general models can do the job&rdquo;</em>, and the same section reports Bolejko and Sussman arguing that our improbable position is less improbable in a Szekeres solution than in an LTB one. That is a real caveat and it is conceded. But the extra freedom is freedom in the <em>shape</em> of the inhomogeneity, not a different prize at the end of it, and the tolerance below is what the prize looks like. The centring tolerance is set by the microwave dipole an off-centre observer would see, and it works out at tens of megaparsecs &mdash; the arithmetic is done at <a href="#ARG-E09">ARG-E09</a>, where the same models are worked in the Hubble-tension vocabulary. Tens of megaparsecs is tens of millions of light-years. It contains the Local Group, the Virgo cluster&rsquo;s outskirts and millions of galaxies, and it cannot tell the Earth apart from the Sun, from Alpha Centauri or from Andromeda. Inside that void the spacetime is still expanding, the age is still billions of years, and the Earth still orbits the Sun once a year. The maximum available prize is &ldquo;our galaxy sits near the middle of a large hole&rdquo;, and it is not the claim on the list.</p>

<p><strong>Seventh, the two Copernican principles are not the same principle.</strong> The one Copernicus argued for is that the Earth orbits the Sun. The one Bondi named is that no place in the universe is privileged for the purpose of cosmological modelling. The second was retro-named after the first and the argument trades on the overlap. Heliocentrism is settled by things that have nothing to do with cosmological homogeneity: stellar parallax measured for about 1.47 billion sources by Gaia, annual aberration, radar ranging to Venus, and half a century of spacecraft navigating to targets on solutions that assume the Earth moves. Delete the cosmological principle in full &mdash; hand the geocentrist every void model in the literature &mdash; and every one of those measurements returns the same answer it returns today. The argument is aimed at a postulate whose failure the target does not depend on.</p>

<p><strong>Eighth, the charge in the passage, answered on its own terms.</strong> The book&rsquo;s claim is not merely that the principle is assumed; it is that the principle <em>overrides evidence</em> &mdash; that even a datum showing a stationary Earth would be re-read to preserve it. Test that against what the field did with the strongest anti-Copernican proposal ever seriously floated. When it turned out that a big enough local void could remove dark energy entirely, cosmologists did not suppress it: they wrote it up in <em>Physical Review Letters</em>, gave it the title <em>&ldquo;Living in a Void: Testing the Copernican Principle with Distant Supernovae&rdquo;</em>, specified the redshift range where it separates from &Lambda;CDM, and then spent four years measuring it. Clarkson&rsquo;s consistency test was built to be independent of curvature, dark energy, matter content and the theory of gravity precisely so that the answer could not be smuggled in through the assumptions. The evidence closed the option. The philosophy did not.</p>

<p><strong>Verdict: refuted, on the source&rsquo;s claim rather than the item&rsquo;s.</strong> &ldquo;It is an assumption&rdquo; was true when written and is conceded here without reservation. &ldquo;It is philosophy dressed as science, and it decides the data in advance&rdquo; is the claim the book actually makes, and it is contradicted by a specific measurement: the microwave background&rsquo;s small-angle power spectrum, which bounds radial inhomogeneity at the percent level per gigaparsec and excludes by two orders of magnitude the spherically symmetric Lema&icirc;tre&ndash;Tolman&ndash;Bondi voids deep and wide enough to replace dark energy &mdash; the class the kSZ test was aimed at, and the class the argument&rsquo;s own sources put forward. The foundation was checked, as the author they quote asked. It held.</p>""",

    advocate=dict(
        best_defense=(
            "You have refuted the void model. You have not touched my claim, and your own "
            "citation says so: Zhang and Stebbins open by conceding that the principle "
            "'remains largely unproven at Gpc radial scale and above.' That is my item, "
            "verbatim, from your witness. Second, your tests are not independent of the thing "
            "they test. The ACT limit is extracted with LambdaCDM foreground and point-source "
            "models; the kSZ prediction uses LambdaCDM structure growth; and Ellis says in the "
            "very paper you are quoting against me that these are 'not self consistent "
            "studies, as they use FLRW perturbation theory to study structure formation in LTB "
            "models.' You quote his call for tests and skip his objection to the tests. Third, "
            "and you conceded it yourself: the number-count dipole is a five-sigma conflict "
            "with the kinematic reading of the CMB dipole and it is not resolved in 2026. You "
            "are telling me the foundation held while the field publishes papers titled 'A "
            "Challenge to the Standard Cosmological Model.' Fourth, on Ellis disavowing the "
            "film: he disavowed an agenda, not a theorem. Nothing he wrote about "
            "underdetermination was retracted, and you have quoted it approvingly yourself. "
            "Fifth, your 'even if it failed you get nothing' move gives the game away. If the "
            "principle is doing no work, why did Wolfson invoke it to rule out a motionless "
            "Earth? Somebody is spending it. You cannot have it be both indispensable to "
            "cosmology and irrelevant to the question of what is at the centre."),
        survives=4,
        preemptive=(
            "Four, and the number is driven by the second and fifth moves, not the first. Four "
            "concrete requirements, all of which the text above already meets and which must "
            "not be edited out. (a) The circularity objection has to be met with a "
            "MODEL-INDEPENDENT test, named, or the section is worthless. That is why "
            "Clarkson, Bassett & Lu appear twice with their actual property spelled out - the "
            "C(z) consistency relation depends only on the geometry being Robertson-Walker, "
            "and is independent of curvature, dark energy, matter content and the theory of "
            "gravity. Do not compress that to 'model-independent'; the adjective is what is "
            "in dispute. (b) The Ellis 'not self consistent studies' quotation is the "
            "defender's best card and the answer must be by NAME: Bull, Clifton & Ferreira "
            "2012 relaxed the fixed bang-time function, which is the specific freedom Ellis "
            "said had been removed, and still ruled the models out - and two of those three "
            "authors proposed the void reading in the first place. Section five carries this; "
            "if an editor trims it to a cross-link the paragraph collapses. (c) On the "
            "number-count dipole, resist both temptations. Do not call it settled, because it "
            "is not, and do not let it stand unqualified, because a reader will take a "
            "five-sigma headline as a five-sigma vindication. The load-bearing sentence is "
            "that the dipole points roughly WHERE the CMB dipole points and disagrees about "
            "HOW BIG it is - an amplitude problem for LambdaCDM, not a direction pointing at "
            "the Earth - together with the 2025 reassessment's 3.3-3.6 sigma. Keep both. "
            "(d) The fifth move needs the answer it now has in section seven, stated as a "
            "distinction rather than a dodge: the principle IS indispensable to cosmology and "
            "IS irrelevant to heliocentrism, because it is a postulate about the large-scale "
            "distribution of matter and the Earth's orbit is established by parallax, "
            "aberration, radar ranging and spacecraft navigation. On Wolfson: the page should "
            "not defend that sentence. If a physicist really did wave away a stationary Earth "
            "on 'philosophical ground' in a lecture, the honest reply is that he had better "
            "arguments available and chose a worse one, and that the good ones are at "
            "ARG-A02 and ARG-A05. Conceding a bad argument by one's own side is cheap and it "
            "buys the credibility this whole page runs on."),
    ),

    straw_man=dict(
        identified=True,
        detail=("The chapter assigns motives to the scientists it quotes, and the motives are its "
                "own contribution. Ellis's 1979 remark that weakening homogeneity implies a "
                "preferred position - a statement of what the principle was designed to do - is "
                "introduced with \"Downright fearful of geocentrism and desiring to keep the "
                "status quo\". Hawking's position is glossed as \"using the cosmos as a mirror to "
                "reflect his own agnosticism\". Ellis is said to withhold the Earth as a rest "
                "frame \"for reasons he does not reveal\", in a passage where the reason he gives "
                "is quoted two paragraphs earlier: the background radiation picks out the frame. "
                "None of these people held the position being attacked. Ellis's actual position "
                "is that cosmology uses philosophical criteria and should say so, which is why "
                "he wrote the tests; asked about the 2014 film that carries this argument, he "
                "said he had not been told its purpose and added \"I totally disavow that silly "
                "agenda\". Kaku, Krauss, Tegmark, Barbour and the narrator Kate Mulgrew objected "
                "to their appearances in similar terms."),
    ),

    compression=dict(
        assessed=True, drifted=True,
        list_phrasing="Copernican principle assumption.",
        source_wording=("&ldquo;This clearly shows that the Copernican Principle from which modern "
                        "science creates its interpretations of the cosmological data is not "
                        "scientific but philosophical. In other words, <em>even if the empirical "
                        "evidence shows Earth is not moving</em>, the ever-present Copernican "
                        "Principle requires that every piece of scientific data must be "
                        "interpreted by assuming the earth is moving&hellip;&rdquo;"),
        drift_type="force_upgraded",
        note=("This drift runs the opposite way to the usual one, and it is the <a href=\"#ARG-R01\">"
              "ARG-R01</a> pattern rather than the <a href=\"#ARG-A03\">ARG-A03</a> one: almost no "
              "wording moves, and the <strong>speech act</strong> does. In <em>Galileo Was Wrong</em> "
              "the proposition is a <em>negative</em> claim about somebody else&rsquo;s foundation "
              "&mdash; you assumed this, you did not establish it, and you are using it to pre-read "
              "the data. That is ground-clearing. It is offered to remove an objection, and the "
              "chapter goes on to argue for a central Earth from other things entirely: microwave "
              "background alignments, quasar anisotropies, redshift structure. On the list the same "
              "four words stand alone as numbered proof 354, in a document whose organising claim is "
              "that each numbered line is a reason to believe the Earth does not move. A parity claim "
              "has become a proof, which is a promotion nothing in the source authorises.<br><br>"
              "<strong>The refutation above answers the source, not the item.</strong> The item&rsquo;s "
              "bare proposition is <em>true</em> &mdash; the Copernican principle was an assumption, "
              "and the paper cited against it here opens by saying so &mdash; and beating it would beat "
              "nobody. What the book claims, and what gets answered, is the stronger thing: that the "
              "principle is philosophical rather than scientific and overrides evidence. "
              "One further note for anyone auditing this later. Rick DeLano, who produced the 2014 "
              "film with Sungenis, states the argument on his blog at a strength neither the book nor "
              "the list reaches &mdash; &ldquo;Copernican Principle, 1532-2013, RIP&rdquo; and "
              "&ldquo;it has been scientifically falsified&rdquo;. So the chain does not degrade "
              "monotonically. It hardens from book to film and then softens again into the "
              "four-word list entry, which is a useful corrective to any picture of compression as a "
              "one-way ratchet."),
    ),

    verdict_challenge=dict(challenged=False, proposed_verdict=None, reasoning=None),

    people=["PER-SUNGENIS"],
    related=["R01", "R03", "R11", "E01", "E02", "E04", "E09", "E11", "E12", "E17", "D14"],

    sources=[
        dict(label="Sungenis & Bennett, Galileo Was Wrong, Vol. I — the Copernican-principle "
                   "passages at printed pp. 92 and 308–311 of the seventh edition (2013); "
                   "Internet Archive three-volume scan, djvu text searched 2026-08-09. The same "
                   "chapter-3 paragraph is in the earlier CD edition, ISBN 0-9779640-0-0, p. 145",
             url="https://archive.org/details/galileo-was-wrong-the-church-was-right-sungenis-vol-1-3-complete"),
        dict(label="Ellis, “Inhomogeneity effects in Cosmology”, arXiv:1103.2335, Class. Quantum "
                   "Grav. 28:164001 (2011) — the source of the sentence the book quotes, and, "
                   "five pages earlier, of “it is now known that this assumption is indeed at "
                   "least partly testable”; §4.4 lists four observational tests",
             url="https://arxiv.org/abs/1103.2335"),
        dict(label="Zhang & Stebbins, “Confirmation of the Copernican principle at Gpc radial "
                   "scale and above from the kinetic Sunyaev-Zel'dovich effect power spectrum”, "
                   "PRL 107:041301 (2011); quoted here from the published version, arXiv v3, "
                   "which is what the abs URL below serves — SPT limit ΔT² < 6.5 µK² and ACT "
                   "ΔT² < 8 µK² at ℓ = 3000; void models overshoot the SPT limit by two orders "
                   "of magnitude; Δχ² > 209 on the supernovae; |ΔH/H| ≲ 1% per ~1 h⁻¹ Gpc "
                   "shell. The superseded v2 reads SPT < 13 µK² and Δχ² > 195 — do not import "
                   "those figures against this citation",
             url="https://arxiv.org/abs/1009.3967"),
        dict(label="Caldwell & Stebbins, “A Test of the Copernican Principle”, PRL 100:191302 "
                   "(2008) — the reionized universe as a mirror; published six months before "
                   "the New Scientist piece in which the book quotes Caldwell wishing for one",
             url="https://arxiv.org/abs/0711.3459"),
        dict(label="Clarkson, Bassett & Lu, “A general test of the Copernican Principle”, PRL "
                   "101:011301 (2008) — the C(z) consistency relation, independent of curvature, "
                   "dark energy, matter content and the theory of gravity",
             url="https://arxiv.org/abs/0712.3457"),
        dict(label="Clifton, Ferreira & Land, “Living in a Void: Testing the Copernican Principle "
                   "with Distant Supernovae”, PRL 101:131302 (2008) — quoted at length and "
                   "accurately in Galileo Was Wrong ch. 3",
             url="https://arxiv.org/abs/0807.1443"),
        dict(label="Bull, Clifton & Ferreira, “The kSZ effect as a test of general radial "
                   "inhomogeneity in LTB cosmology”, Phys. Rev. D 85:024002 (2012) — relaxes the "
                   "fixed bang-time function and still “effectively rules out simple LTB models "
                   "as an explanation of dark energy”",
             url="https://arxiv.org/abs/1108.2222"),
        dict(label="Mustapha, Hellaby & Ellis, “Large Scale Inhomogeneity Versus Source "
                   "Evolution — Can We Distinguish Them Observationally?”, MNRAS 292:817 "
                   "(1997) — the underdetermination theorem the steelman rests on, by the "
                   "author the book quotes",
             url="https://arxiv.org/abs/gr-qc/9808079"),
        dict(label="Secrest et al., “A Test of the Cosmological Principle with Quasars”, ApJL "
                   "908:L51 (2021), 4.9σ; and “A Challenge to the Standard Cosmological Model”, "
                   "ApJL 937:L31 (2022), 5.1σ joint — the live anomaly, conceded above",
             url="https://arxiv.org/abs/2009.14826"),
        dict(label="Bashir, Chingangbam & Appleby, “The CatWISE2020 Quasar dipole: A Reassessment "
                   "of the Cosmic Dipole Anomaly” (arXiv, 2 November 2025) — 3.27–3.63σ after "
                   "clustering and mask systematics; “the anomaly is reduced [but] cannot be "
                   "explained solely by the clustering dipole or mode coupling”",
             url="https://arxiv.org/abs/2511.00822"),
        dict(label="Gibbs, “Profile: George F. R. Ellis — Thinking Globally, Acting Universally”, "
                   "Scientific American 273(4):55 (October 1995), publisher record of the “you "
                   "can only exclude it on philosophical grounds” passage the book quotes "
                   "correctly. Read here as quoted at printed p. 310 of Galileo Was Wrong 7th "
                   "ed.; the magazine text itself was reachable only behind a paywall",
             url="https://www.nature.com/articles/scientificamerican1095-55"),
        dict(label="The Principle (2014) — produced by Rick DeLano and Robert Sungenis; Ellis, "
                   "Kaku, Krauss, Tegmark, Barbour and narrator Kate Mulgrew all objected to "
                   "their appearances, Ellis saying “I totally disavow that silly agenda”",
             url="https://en.wikipedia.org/wiki/The_Principle"),
    ]),
}
