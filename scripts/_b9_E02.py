# -*- coding: utf-8 -*-
"""
Batch 9 — ARG-E02, "CMB hemispheric asymmetry, Cold Spot, parity and variance anomalies".
6 items (326, 331, 336, 339, 341, 342), lane E, verdict MISLEADING, cluster record
crediting Sungenis & DeLano's film The Principle (2014).

Siblings: E01 owns the low-multipole ALIGNMENTS (the "axis of evil"), E03 owns l = 1
(dipole, dark flow, bulk flows). E02 owns the rest of the standard anomaly list:
hemispherical/dipolar power asymmetry, the Cold Spot, point-parity, low variance, plus
two catch-alls (336 "Cosmic isotropy violations", 331 "ISW correlations ecliptic-linked").
E01's restraint rule is inherited in full and is not negotiable here: Planck 2018 VII
calls the existence of these features "uncontested", the significance question is open,
and nothing below may be written as though it were closed.

WHAT SEPARATES E02 FROM E01, AND WHY IT IS WORTH ITS OWN ENTRY
---------------------------------------------------------------
E01's answer is "an axis is a direction, not a centre." E02's answer is one step harder
and one step better, and it is available *from inside the source*:

  1. Two of the six items (parity, variance) are SCALARS. A single number computed over
     the whole sky has no direction at all, so it cannot point at anybody. Nothing in
     E01 makes that point because E01's items all carry directions.
  2. The items that DO carry directions carry DIFFERENT ones. Computed from the
     coordinates printed on the source's own figure (7th ed., Vol. I, p. 366): the
     maximum-asymmetry axis (57, 10) sits 72 deg from the "Axis of Evil" (260, 60) and
     48.6 deg out of the ecliptic plane; the Cold Spot (209, -57) sits 56 deg from the
     same axis and 37.1 deg out of the ecliptic. The caption under that figure says the
     axes form "an X and Y graph, with Earth at or very near the intersection point."
     Two of the six labels in the figure are nowhere near the X or the Y.

     Recomputed in-session 2026-08-09, spherical trigonometry only, from the six label
     coordinates as OCR'd from the scan. Anyone can redo it in four lines.

WHAT IS IN THE SOURCE AND WHAT IS NOT — SCOPE EVERY ABSENCE
------------------------------------------------------------
Two texts were searched in full, and only these two:

  (A) The 2006 "GWW_Final" PDF at Internet Archive item `GallileoWasWrong` (PDF metadata
      CreationDate June 2006; runs to printed p. 1147). 3.1 MB of extracted text.
  (B) The complete seventh edition (2013), Volumes 1-3, at Internet Archive item
      `galileo-was-wrong-the-church-was-right-sungenis-vol-1-3-complete` (djvu.txt, 5.5 MB),
      cross-checked against the separate Vol. II scan at item
      `GalileoWasWrongTheChurchSungenisRobertA.Bennett4276`.

  Located:
    * The hemispheric asymmetry, via a block quotation of Starkman & Schwarz's Scientific
      American piece (Aug 2005, p. 52) reporting Eriksen's 2003 result — 2006 ed., Vol. I
      ch. 3, pp. 164-165. The quoted paragraph ENDS with the words "a type of
      observational artifact", and Sungenis prints that sentence.
    * The same anomaly again as Bennett's item 23 in a 26-item list, Vol. II ch. 10,
      printed p. 386: "A deficit in large-scale multipole power exists between the north
      and south ecliptic hemispheres."
    * The WMAP nine-year paper's report that the map power asymmetry "has indeed been
      mitigated in the new beam-symmetrized maps" — quoted by Sungenis at 7th ed. Vol. I
      p. 371 and answered, in his own voice, "power asymmetries are not the cause of the
      Axis of Evil." That is the `passage` for this entry.
    * "Cold spot (209,-57)" and "Max asym axis (57,10)" — as LABELS inside the borrowed
      figure at 7th ed. Vol. I p. 366, and, in the searched text, nowhere else.
    * The lack of large-angle correlation, repeatedly (Starkman's lecture abstract quoted
      at p. 375; Bennett's list item 1 at Vol. II p. 386).

  NOT located in (A) or (B) — searched in full, both editions, whole text:
    * "Sachs" — zero occurrences. No ISW discussion of any kind is located there.
    * CMB point-parity. "parity" occurs six times in (B): five are "disparity"; the sixth
      is Anil Ananthaswamy on cosmic parity conservation in a discussion of GALAXY SPIN
      handedness (Longo, Shamir) at 7th ed. Vol. I p. ~384, which is ARG-E05's material,
      not the CMB point-parity statistic of item 341.
    * The low-variance statistic. "variance" in (B) resolves to covariance/invariance;
      the related anomaly the source does discuss is the vanishing two-point correlation,
      which is a different measurement.
    * The Cold Spot as anything the source argues from. Vielva, Cruz and Eridanus return
      zero occurrences in both texts.
  Unreachable is not absent: the film's audio could not be transcribed from here, and
  DeLano's blog was not exhaustively searched. This says what was searched, not what exists.

THE PROVENANCE FINDING, AND WHERE THE ITEMS PROBABLY COME FROM
---------------------------------------------------------------
The six list items use the vocabulary of the anomaly LITERATURE, not of the geocentric
text: "hemispheric power asymmetry", "parity asymmetry", "variance anomalies" are, near
verbatim, the section headings of Planck 2018 VII sect. 6 and the five-item enumeration in
Schwarz, Copi, Huterer & Starkman, CQG 33:184001 (2016). The most economical reading is
that this cluster was assembled by copying a review's list of anomalies, not by reading
Sungenis. That is a finding about how the list grew, and it is why `drift_type` is
`unsourced_addition` rather than the `reversed` that item 339 alone would earn.

ON THE WORK RECORD. `clusters.py` credits The Principle (2014). Every quotation below is
from the book, which is where this material is set out, and the entry cites
WRK-SUNGENIS-2006 accordingly; the film is named in the gloss. This is the same
observation E03 made about the dipole material and it is reported upward, not applied
here — `clusters.py` was not touched.

FOOTNOTE WORTH KEEPING. The p. 365 analysis carries an acknowledgement: "My thanks to
Gerry Bouw for his help in analyzing this data." The movement's only credentialed
astronomer worked on this chapter. PER-BOUW is in `people`.

QUOTE PROVENANCE. The p. 371 passage was read from the OCR of scan (B) and the same
sentences were checked against the independent Vol. II scan and against the 2006 PDF's
own text layer where they overlap. Page numbers are the PRINTED numbers in the running
text, not PDF page indices, and none has been checked against a print copy; the locator
says so.
"""

ENTRY = {

"E02": dict(

    tldr=("All six of these are real features of the microwave sky and Planck says so — its "
          "isotropy paper calls their existence “uncontested”. What they do not do is agree "
          "with each other. The source reproduces a figure whose own printed labels put the "
          "Cold Spot at galactic (209, -57) and the maximum-asymmetry axis at (57, 10), then "
          "captions it as an X and a Y with the Earth at the crossing point — and those two "
          "labels sit 56 and 72 degrees away from the axis the cross is drawn on. Two of the "
          "six items are single numbers with no direction at all, and a number cannot point "
          "at anyone."),

    passage=dict(
        work="WRK-SUNGENIS-2006",
        pd=False,
        locator=("Seventh edition (2013), Vol. I, ch. 3 (“Evidence Earth is in the Center of the "
                 "Universe”), printed p. 371, in a running critique of the WMAP nine-year "
                 "foreground paper. The indented block is Sungenis quoting the WMAP team; the "
                 "sentence after it is his own. Read from the complete three-volume scan at "
                 "Internet Archive item galileo-was-wrong-the-church-was-right-sungenis-vol-1-3-"
                 "complete; printed page number as it appears in the running text, not checked "
                 "against a print copy."),
        quote=("As a result of this new procedure, the previously reported map power asymmetry, "
               "which we speculated was due to the asymmetric beams and not cosmology … has "
               "indeed been mitigated in the new beam-symmetrized maps. … This is all well and "
               "good, but power asymmetries are not the cause of the Axis of Evil."),
        gloss=r"""<p><strong>Watch what he does with the concession, because it decides what this entry has to answer.</strong> The list carries &ldquo;CMB hemispheric power asymmetry&rdquo; as proof item 339. In the source, the hemispheric power asymmetry arrives as a <em>quotation of the WMAP team reporting that they had largely removed it</em> &mdash; they had traced it to asymmetric instrument beams rather than to the sky &mdash; and Sungenis&rsquo;s reply is not to dispute that. It is to set the whole anomaly aside as no part of his case: <em>power asymmetries are not the cause of the Axis of Evil</em>. His argument is about the alignment of the quadrupole and octopole with the ecliptic, which is <a href="#ARG-E01">ARG-E01</a>&rsquo;s material and not this cluster&rsquo;s. On the list, the item he disowned appears as an independent witness in its own right.</p>

<p><strong>The figure five pages earlier, which is the best evidence on this page and it is his.</strong> At p. 366 the book reproduces the anomaly-direction map from Copi, Huterer, Schwarz &amp; Starkman&rsquo;s review <em>Large-Angle Anomalies in the CMB</em> (Advances in Astronomy 2010:847541), which Sungenis cites by name three pages later. Six directions are printed on it in galactic coordinates: <em>Axis of Evil ~(260,60)</em>, <em>Dipole (264,48)</em>, <em>Virgo ~(260,70)</em>, <em>Ecliptic pole (96,30)</em>, <em>Max asym axis (57,10)</em>, and <em>Cold spot (209,-57)</em>. The caption underneath is his: <em>&ldquo;The Dipole axis intersects with the Quadrupole/Octupole axis, forming an X and Y graph, with Earth at or very near the intersection point.&rdquo;</em></p>

<p>Take the caption at its word and check the other four labels against it. The Axis of Evil sits 12&deg; from the dipole and 1.0&deg; out of the ecliptic plane &mdash; so the X and the Y are real, and E01 concedes them. The maximum-asymmetry axis, the direction belonging to item 339, sits <strong>72&deg; from the Axis of Evil</strong> and <strong>48.6&deg; out of the ecliptic plane</strong>. The Cold Spot, item 326, sits <strong>56&deg; from the Axis of Evil</strong>, 52&deg; from the maximum-asymmetry axis, and <strong>37.1&deg; out of the ecliptic</strong>. Two of the six labels on the figure are nowhere near the cross the figure is captioned as showing. (Angles recomputed here from the six printed label coordinates, spherical trigonometry only; axis separations are quoted modulo 180&deg;, which is the generous convention for headless directions.)</p>

<p><strong>Where each of the six items is, and is not, located.</strong> Two texts were searched in full and only these two: the 2006 <em>GWW_Final</em> PDF at Internet Archive item <code>GallileoWasWrong</code>, and the complete seventh edition (2013), Volumes 1&ndash;3, at item <code>galileo-was-wrong-the-church-was-right-sungenis-vol-1-3-complete</code>. In those two texts: the hemispheric asymmetry is present twice more &mdash; as a block quotation of Starkman and Schwarz in <em>Scientific American</em> (2006 ed., Vol. I, pp. 164&ndash;165) and as Bennett&rsquo;s item 23 in a 26-item anomaly list (Vol. II ch. 10, p. 386); the Cold Spot is present as the figure label above and, in the searched text, nowhere else; and the words &ldquo;Sachs&rdquo;, &ldquo;Vielva&rdquo; and &ldquo;Eridanus&rdquo; return zero occurrences, while every instance of &ldquo;parity&rdquo; is either &ldquo;disparity&rdquo; or a discussion of <em>galaxy-spin</em> handedness that belongs to <a href="#ARG-E05">ARG-E05</a>. That is a statement about two editions and the routes used to read them. The film&rsquo;s audio could not be transcribed from here and is not covered by it.</p>

<p><strong>One quoted sentence the source prints and then reverses.</strong> The <em>Scientific American</em> paragraph he reproduces at pp. 164&ndash;165 ends by saying the north&ndash;south asymmetry &ldquo;was the first sign that the CMB fluctuations, which were supposed to be cosmological in origin&hellip;have a solar system signal in them &ndash; that is, a type of observational artifact.&rdquo; He prints that clause and then glosses the finding as showing that &ldquo;all the radiation in the universe&hellip;is centered around the Earth&rdquo;. The authors&rsquo; conclusion &mdash; part of this signal is local contamination &mdash; and his conclusion are not the same conclusion, and the first one is on the page above the second.</p>

<p><strong>On the work cited.</strong> Our cluster record for E02 credits <em>The Principle</em> (2014), the Sungenis&ndash;DeLano film. This material is set out in the book, so this treatment quotes and cites the book; the film is the artefact that carries the least of it, exactly as <a href="#ARG-E03">ARG-E03</a> found for the dipole. Worth recording alongside it: the p. 365 analysis carries the footnote <em>&ldquo;My thanks to Gerry Bouw for his help in analyzing this data&rdquo;</em>, which puts the movement&rsquo;s only credentialed astronomer inside this chapter.</p>"""),

    steelman=dict(
        description=r"""<p>There are three tiers here and the top one is genuinely strong. Getting this wrong in the easy direction would be this entry&rsquo;s worst available error.</p>

<p><strong>SURFACE (weak &mdash; do not use).</strong> &ldquo;These anomalies were debunked / went away / were foregrounds all along.&rdquo; False, and a defender who has read Planck will end the exchange with one quotation. Planck 2018 VII, opening its anomalies section: <em>&ldquo;The existence of these features is uncontested.&rdquo;</em> Equally weak: &ldquo;the Cold Spot is just the Eridanus supervoid.&rdquo; That explanation has been tested and it failed, which is discussed below, and a critic who leans on it is quoting a 2015 press release against a 2017 redshift survey.</p>

<p><strong>DEEPER.</strong> Each of the four named features is real, published in refereed journals by mainstream cosmologists, and has survived a change of satellite. The hemispherical asymmetry was found by Eriksen and by Hansen and collaborators in the first-year WMAP data and is still in Planck as a dipolar power modulation; the Cold Spot was found by Vielva and colleagues with spherical Mexican-hat wavelets in 2004; the odd-parity preference goes back to Land and Magueijo in 2005 and to Kim and Naselsky in 2010; the low variance to Monteser&iacute;n and colleagues in 2008. None of them is a crank artefact and none was found by geocentrists.</p>

<p><strong>KERNEL.</strong> The strongest version is not that any one anomaly is significant &mdash; each is modest on its own &mdash; but that they may be <em>jointly</em> significant. Schwarz, Copi, Huterer and Starkman make exactly this argument in <em>CMB Anomalies after Planck</em> (CQG 33:184001, 2016), listing &ldquo;a lack of both variance and correlation on the largest angular scales&rdquo;, the low-multipole alignments, &ldquo;a hemispherical power asymmetry or dipolar power modulation&rdquo;, &ldquo;a preference for odd parity modes&rdquo; and &ldquo;an unexpectedly large cold spot in the Southern hemisphere&rdquo;, and observing that <em>&ldquo;some pairs of those features are demonstrably uncorrelated, increasing their combined statistical significance and indicating a significant detection of CMB features at angular scales larger than a few degrees on top of the standard model.&rdquo;</em> That is the honest strong form: not one 2&sigma; curiosity but a set of partly independent ones, in the regime where Planck is cosmic-variance limited so no future temperature map can settle it. Add that the review closest to the geocentric thesis in spirit &mdash; Aluri and twenty-odd co-authors, <em>Is the observable Universe consistent with the cosmological principle?</em>, CQG 40:094001 (2023) &mdash; treats these alongside the Hubble tension and the radio/quasar dipole excess as a live case that the FLRW paradigm may need modifying. Concede every word of that.</p>""",
        why_it_doesnt_save_claim=r"""<p><strong>Because &ldquo;jointly significant&rdquo; is the argument for a violation of statistical isotropy, and statistical isotropy is not geocentrism&rsquo;s claim.</strong> Schwarz et al. are arguing that the sky is not a realisation of an isotropic Gaussian random field. Suppose they win outright. What follows is that the universe has structure at the largest scales &mdash; a preferred direction, a modulation, a patch. Every one of those is a property of the <em>field</em>, seen identically by every observer in it. None of them is a property of a <em>place</em>.</p>

<p><strong>And the joint case cuts the other way on the one question this cluster needs answered.</strong> If several partly independent features all pointed at the same axis, that would be a coherent thing to argue from. They do not. Computed from the coordinates the source itself prints: the maximum-asymmetry axis is 72&deg; from the low-multipole axis and 62&deg; from the dipole; the Cold Spot is 56&deg; from the low-multipole axis and 52&deg; from the maximum-asymmetry axis. Mutual independence is precisely what makes the combined <em>significance</em> larger &mdash; and precisely what makes the combined <em>direction</em> non-existent. The source cannot have both.</p>

<p><strong>Two of the six items have no direction to disagree about.</strong> Point-parity is a comparison of summed even-<em>&ell;</em> against summed odd-<em>&ell;</em> power. Variance is one number over a masked sky. Neither has an axis, a location or a pointing. An anomaly that reduces to a scalar cannot single out an observer, and no amount of significance changes that; it is a category error, not a measurement problem.</p>

<p><strong>Finally, the source&rsquo;s own reading of the whole set is local, not cosmic.</strong> Bennett&rsquo;s technical chapter, summarising the low-multipole anomaly, gives as its seventh point: <em>&ldquo;becoming more likely that the large scale microwave sky has a local cause&rdquo;</em>, and offers as the reading of the correlations that &ldquo;we are seeing the influence of the solar system environment, not the global properties of space.&rdquo; A signal contaminated by the solar system is a signal that tells you less about the cosmos, not one that puts you in the middle of it.</p>"""),

    refutation=r"""<p><strong>Start where honesty requires and stay there for a paragraph.</strong> These are real features. Planck&rsquo;s own isotropy paper opens its anomalies section by saying so: <em>&ldquo;The existence of these features is uncontested, but, given the modest significances at which they deviate from the standard &Lambda;CDM cosmological model, and the a posteriori nature of their detection, the extent to which they provide evidence for a violation of isotropy in the CMB remains unclear. It is plausible that they are indeed simply statistical fluctuations. Nevertheless, if any one of them has a physical origin, it would be extremely important, and hence further investigation is certainly worthwhile.&rdquo;</em> That is the state of the field and this page does not improve on it. Nothing below claims the anomalies are resolved, and any rebuttal that does is wrong.</p>

<p><strong>The test this cluster fails is not significance. It is agreement.</strong> The list presents six findings as six witnesses to one fact. Witnesses to a single geometric fact should point somewhere in common. Take the six directions off the figure the source itself reproduces at Vol. I p. 366 and measure them against each other. Axis of Evil (260, 60); dipole (264, 48); Virgo (260, 70); north ecliptic pole (96, 30); maximum-asymmetry axis (57, 10); Cold Spot (209, &minus;57). The first three cluster within 22&deg; of one another and lie 1&ndash;11&deg; from the ecliptic <em>plane</em> &mdash; that is E01&rsquo;s coincidence, and it is granted. The other two do not join them. The maximum-asymmetry axis lies 72&deg; from the Axis of Evil, 63&deg; from the dipole, and 48.6&deg; out of the ecliptic plane. The Cold Spot lies 56&deg; from the Axis of Evil, 66&deg; from the dipole, 52&deg; from the maximum-asymmetry axis, and 37.1&deg; out of the ecliptic. On a page arguing that the microwave sky is organised about the Earth&rsquo;s orbital plane, the two features this cluster is built from are the two that are not.</p>

<p><strong>Item 339, the hemispheric power asymmetry.</strong> The effect is a dipolar modulation of small-scale power: one half of the sky is slightly hotter in fluctuation amplitude than the other, at about the 7% level on large angular scales. Planck 2018 VII adopts the direction (<em>l</em>, <em>b</em>) = (221&deg;, &minus;20&deg;) for the modulation, and its own local-variance analysis of the temperature maps returns (205&deg;, &minus;20&deg;) at full resolution and (209&deg;, &minus;15&deg;) degraded. The source&rsquo;s figure gives the same axis by its other end: (57, 10) has antipode (237, &minus;10), which sits 18&deg; from Planck&rsquo;s adopted direction and 28&ndash;32&deg; from the local-variance ones &mdash; the same line, measured a decade apart with different estimators. Three things then have to be said, and the third is the one that matters here. <em>First</em>, the significance is modest and a posteriori: the direction was not predicted, it was found by looking. <em>Second</em>, polarization has not corroborated it. Planck 2018 VII: <em>&ldquo;Neither investigations using a variance estimator nor via &ell; to &ell; &plusmn; 1 mode coupling find strong evidence of this asymmetry&rdquo;</em> in the E-mode data, and the paper is careful to add that the apparently suggestive alignment of the temperature and polarization preferred directions &ldquo;cannot be interpreted as evidence of power asymmetry in polarization&rdquo;. <em>Third</em> &mdash; and this is the fact that ought to travel with item 339 wherever it goes &mdash; <strong>at the point where he introduces it, the source declines to argue from it.</strong> He quotes the WMAP nine-year team reporting that the map power asymmetry &ldquo;has indeed been mitigated in the new beam-symmetrized maps&rdquo; after they traced it to asymmetric instrument beams, and answers: &ldquo;power asymmetries are not the cause of the Axis of Evil.&rdquo; The list is running as a proof the one item its own authority set down.</p>

<p><strong>Item 326, the Cold Spot.</strong> A region about 5&ndash;10&deg; across in Eridanus, at galactic (209&deg;, &minus;57&deg;), colder than a Gaussian sky comfortably predicts; found by Vielva and colleagues in 2004 with wavelet filtering. Begin by noticing what the item claims: a <em>preferred axis</em>. A cold patch is a position on the celestial sphere. It defines a direction from here to there in the same sense that any object in the sky does, and it defines nothing else &mdash; no orientation of the field, no symmetry axis, no plane. The Andromeda galaxy also defines a direction from here to there. Then the physics. The best-motivated explanation was that a supervoid along the line of sight cools the photons crossing it through the integrated Sachs&ndash;Wolfe effect; Szapudi and colleagues reported such a supervoid aligned with the spot in 2015 (MNRAS 450:288). It was tested and it failed. Mackenzie and colleagues surveyed the inner 5&deg; spectroscopically &mdash; the 2dF&ndash;VST ATLAS Cold Spot redshift survey, about 7000 galaxies at <em>z</em> &lt; 0.4 &mdash; and concluded that the voids they found were &ldquo;interspersed with small overdensities, and the scale of these voids is insufficient to explain the Cold Spot through the &Lambda;CDM ISW effect&rdquo; (MNRAS 470:2328, 2017), with a combined decrement of roughly &minus;9 &micro;K against the roughly &minus;150 &micro;K needed. A 2022 lensing analysis of the same region put the odds against a large void at about 1:13 to 1:20 relative to plain &Lambda;CDM. Their own summary is worth quoting because it is the least convenient sentence for both sides: the Cold Spot <em>&ldquo;may have a primordial origin rather than being due to line-of-sight effects&rdquo;</em> &mdash; or, in the same paper&rsquo;s framing, it may be a statistical fluctuation. Planck 2018 VII adds that it finds no polarization signature associated with the Cold Spot. So the honest position is that the Cold Spot is unexplained; and an unexplained cold patch 127&deg; from the north ecliptic pole is not evidence for a cosmos organised about the Earth&rsquo;s orbit.</p>

<p><strong>Item 341, parity asymmetry.</strong> Odd-<em>&ell;</em> multipoles carry slightly more power than even ones at large scales &mdash; Land and Magueijo asked &ldquo;Is the Universe odd?&rdquo; in 2005, Kim and Naselsky sharpened it on WMAP7. Planck 2018 VII confirms a preference and then does the arithmetic the list never does: counting how often the same excursion appears anywhere in a range of simulated skies, <em>&ldquo;even considering the look-elsewhere effect, an odd-parity preference is observed with a lower-tail probability of about 1.6%&rdquo;</em>, and it notes that the probability rises as the lowest multipoles are dropped, &ldquo;demonstrating that the anomaly is mostly driven by the largest scales&rdquo; &mdash; that is, by the same handful of modes that generate the alignment story, which is why this is not an independent seventh witness. In polarization, Planck reports no evidence of a violation of point-parity symmetry. And note the one result that gives parity a direction at all: Santos and Zhao find that the preferred axis of the parity asymmetry lies close to galactic (270&ndash;284&deg;, +50&deg;) &mdash; within a few degrees of the CMB dipole &mdash; and draw the conclusion that <em>&ldquo;the alignment of the CMB dipole (purely kinematic effect) and the other preferred axes strongly suggests a non-cosmological origin of the large scale anomalies.&rdquo;</em> The specialists who supplied item 341 with an axis read that axis as evidence the anomalies are contaminated, not cosmic.</p>

<p><strong>Item 342, variance anomalies.</strong> The sky has slightly less variance than &Lambda;CDM expects at low resolution. This is the same physical fact as the missing large-angle power that <a href="#ARG-E01">ARG-E01</a> treats, seen through a different statistic &mdash; not an independent finding. Planck 2018 VII quantifies it at roughly 1% with the 2018 common mask and 0.7&ndash;0.8% with the more aggressive 2016 mask, and states the dependence plainly: <em>&ldquo;the low variance anomaly becomes less significant with increasing sky coverage.&rdquo;</em> An anomaly whose significance is a function of how much of the Galaxy you cut is an anomaly with a foreground question inside it. In polarization: <em>&ldquo;no evidence is found for a low variance of the polarized sky signal.&rdquo;</em> And, again, variance is one number. It has no direction, so it can be evidence about the amplitude of primordial fluctuations and cannot be evidence about anybody&rsquo;s address.</p>

<p><strong>Item 331, ISW correlations, said to be ecliptic-linked.</strong> The integrated Sachs&ndash;Wolfe effect is real and detected: cross-correlating the CMB with radio, optical and infrared tracers plus the Planck lensing map yields, in Planck 2015 XXI, &ldquo;a detection at 4&sigma;&rdquo;, with the Planck data alone giving about 3&sigma; through the ISW-lensing bispectrum. It is a probe of dark energy, which is what makes it interesting. Two things then need saying. The genuinely live ISW question is the amplitude of the stacked imprint of supervoids and superclusters, repeatedly claimed to run above the &Lambda;CDM prediction since Granett, Neyrinck and Szapudi in 2008 &mdash; and the most recent large measurement, Hang and colleagues on four tomographic bins of the DESI Legacy Survey (MNRAS 507:510, 2021), returns a combined amplitude <em>A</em><sub>ISW</sub> = 0.68 &plusmn; 0.50, consistent with the standard prediction. That debate has cooled rather than closed. But the ecliptic clause is the load-bearing half of item 331, and the ISW literature bears on it in the opposite direction. Francis and Peacock reconstructed the <em>local</em> ISW signal from 2MASS photometric redshifts out to <em>z</em> = 0.3 and subtracted it, and reported that <em>&ldquo;removal of the foreground ISW signal from WMAP data reduces the significance of a number of reported large-scale anomalies in the CMB, including the low quadrupole power and the apparent alignment between the CMB quadrupole and octopole&rdquo;</em> (MNRAS 406:14, 2010) &mdash; the quadrupole&ndash;octopole alignment probability moving from a fraction of a percent to over 20%, and the ecliptic no longer tracking a node line in the residual map. The one place the ISW touches this cluster&rsquo;s central claim, it removes the coincidence rather than supplying one.</p>

<p><strong>Item 336, &ldquo;cosmic isotropy violations&rdquo;.</strong> This is the cluster&rsquo;s summary item and it deserves a straight answer rather than a dismissal. Is statistical isotropy violated? Unknown, and reasonable people are on both sides; the 2023 CQG review by Aluri and collaborators sets out the case that it might be, alongside the Hubble tension and the radio-source dipole excess, and concludes that new observations are needed rather than that the matter is settled. Grant the whole of it. Statistical isotropy is a claim about the <em>statistics of a field</em>: that its correlations depend only on angular separation and not on orientation. Its negation is that some direction or some patch is distinguished. The negation of &ldquo;there is no special direction&rdquo; is &ldquo;there is a special direction&rdquo; &mdash; it is not, and cannot be made into, &ldquo;there is a special <em>observer</em>&rdquo;. Homogeneity is the property that would bear on location, and none of these six items measures it. That is why <a href="#ARG-E09">ARG-E09</a> and <a href="#ARG-E17">ARG-E17</a>, which do engage the location question through voids and through isotropy-plus-Copernicanism, are separate arguments and are answered separately.</p>

<p><strong>What a set of unrelated marginal features looks like, and what this set looks like.</strong> If several 1&ndash;2% features in one dataset were the signature of a single structure, the expectation is that they would corroborate: same axis, and confirmation in an independent observable. What is actually on the record is the reverse on both counts. The axes disagree by 50&ndash;70&deg;. The one partly independent observable available &mdash; E-mode polarization, sourced at the same epoch by the same fluctuations but measured through a different systematic chain &mdash; has produced, in Planck&rsquo;s own summary of its 2018 analysis, no counterpart to any of them: <em>&ldquo;We find no evidence in the polarization data of a lack of large-scale angular correlations, a hemispherical asymmetry in the behaviour of N-point functions or peak distributions, a violation of point-parity symmetry, or a polarization signature associated with the Cold Spot.&rdquo;</em> Be exact about the strength of that: Planck also says polarization is partly correlated with temperature and so is not a fully independent probe, and elsewhere that the polarization data &ldquo;have not been able to refute or confirm&rdquo; the temperature signal. It is a test a cosmological interpretation needed to pass and has not yet passed, not one it has failed.</p>

<p><strong>Verdict: misleading, and precisely in the way the cluster name suggests.</strong> Six real entries from the anomaly literature are presented as six independent confirmations of one conclusion. Two of them are scalars and can confirm no directional conclusion at all. Two of them carry directions that disagree with the axis the argument runs on, by margins printed on the source&rsquo;s own figure. One of them is disowned by the source in the source&rsquo;s own words. And the sixth, the ISW clause, points at a body of work whose contact with this argument consists of a paper that removes the ecliptic coincidence by subtracting a local foreground. The anomalies are not the problem. The claim that they converge is.</p>""",

    advocate=dict(
        survives=4,
        best_defense=(
            "You have written a careful page and then done the one thing you tell others not "
            "to do: you have refuted an arrangement rather than an argument. Take your "
            "strongest move, the angles. You computed them from a figure in our book and "
            "announced that our own evidence disagrees with us. But that figure is a "
            "reproduction of Copi and Starkman's summary of the whole anomaly field — we put "
            "it in because it is the mainstream's own inventory, and your complaint is "
            "therefore with them, not with us. Nobody, including Schwarz and Starkman, has "
            "ever claimed the Cold Spot lies on the quadrupole-octopole axis. You have "
            "invented a convergence requirement, found it unmet, and billed us for it. "
            "Second: your scalar argument proves too much. You say variance and parity have "
            "no direction and therefore cannot bear on location. Fine — then they bear on "
            "whether the universe is the smooth Gaussian object the Copernican principle "
            "requires, which is the premise your whole cosmology rests on, and by your own "
            "account that premise is in trouble at 1% and nobody can say why. You are "
            "reduced to arguing that our evidence against your model is not evidence for "
            "ours. Granted. It is still evidence against yours, and you have spent twenty "
            "years failing to explain it. Third, and worst: you quote Planck saying these may "
            "be statistical fluctuations, and then you also quote Planck saying polarization "
            "cannot refute or confirm them. Those are not two arguments, they are one "
            "shrug repeated. And note the shape of your own answer. Every anomaly that "
            "correlates with the solar system, you attribute to the solar system — dust, "
            "beams, masks, scan patterns. That is not a theory, it is an exemption. When the "
            "sky is anomalous you call it a fluke; when it is anomalous in our direction you "
            "call it a systematic. There is no possible observation that your method would "
            "count as evidence, which is the definition of the thing you accuse us of."),
        preemptive=(
            "Four is right, and the number is driven by the first and last moves, not the "
            "middle. Four concrete changes, in order of urgency. (a) The 'you invented the "
            "convergence requirement' hit is the strongest thing on the board and it must be "
            "answered where it lands, not left to the reader. The answer is already implicit "
            "in the refutation and must be made explicit: the convergence requirement is not "
            "ours and it is not the anomaly literature's — it is the LIST'S, because the list "
            "presents six items as six witnesses to one conclusion about where the Earth is, "
            "and only a shared geometry could make them that. Schwarz and Starkman make no "
            "such claim and are not being held to one. Keep the sentence 'witnesses to a "
            "single geometric fact should point somewhere in common' adjacent to the "
            "computed angles; if an editor ever separates them the section becomes "
            "vulnerable. (b) The 'exemption, not a theory' charge is fair as stated and must "
            "be met on the merits rather than by repetition. The reply is that the local "
            "readings are not offered as established: Planck says the significance question "
            "is open, Schwarz et al. say in as many words that no systematic or foreground "
            "has been identified, and this page says both. What the page claims is narrower "
            "and testable — that correlation with the ecliptic is evidence about provenance "
            "and points inward. Say so in the body rather than assuming the reader carries it "
            "over from E01. (c) Do NOT reply to the scalar counter-argument by conceding that "
            "variance and parity 'bear on the Copernican principle'. They bear on statistical "
            "isotropy, which is a different proposition, and blurring them hands back the "
            "distinction the whole entry rests on. The concession to make instead is the true "
            "one: a violation of statistical isotropy would be a major result and nobody here "
            "is denying the possibility. (d) On item 339, resist any temptation to write that "
            "Sungenis 'admitted' the asymmetry away. He did not concede it; he declined to use "
            "it. The finding is about the LIST, which runs as proof an item its own source set "
            "aside — and it is weaker and truer stated that way than as a gotcha."),
    ),

    straw_man=dict(
        identified=True,
        detail=("Yes, and it is specific rather than general. The chapter these items come from "
                "presents the CMB analysis community as manufacturing isotropy on purpose — "
                "'NASA is telling us that they squeezed the data into their preferred (or "
                "“prior”) molds', 'NASA wants the CMB to be as isotropic as possible', "
                "'the obvious fudging of the data to fit its Big Bang model'. That characterisation "
                "cannot survive contact with the chapter's own sources. Every anomaly in this "
                "cluster was found, named, quantified and published by the people being "
                "described: the hemispheric asymmetry by Eriksen and by Hansen, the Cold Spot by "
                "Vielva and Cruz, the odd-parity preference by Land and Magueijo, the low "
                "variance by Monteserin, the whole inventory assembled and mapped by Copi, "
                "Huterer, Schwarz and Starkman — whose figure the chapter reproduces. A field "
                "suppressing anomalies does not spend two decades cataloguing them, and Planck's "
                "isotropy paper does not open by calling their existence uncontested. Related, "
                "and milder: the claim at p. 367 that the 'fluke' hypothesis 'has been ruled out "
                "by a 99% confidence level in the collected data' overstates what a 99% "
                "confidence level does — it is not a refutation of chance, and Planck's own "
                "position is that these features remaining statistical fluctuations is plausible."),
    ),

    compression=dict(
        assessed=True, drifted=True,
        list_phrasing=("Six items: “Cold Spot preferred axis.” · “ISW correlations ecliptic-linked.” · "
                       "“Cosmic isotropy violations.” · “CMB hemispheric power asymmetry.” · "
                       "“Parity asymmetry.” · “Variance anomalies.”"),
        source_wording=("Item 339&rsquo;s only counterpart in the searched text is a refusal to use it: "
                        "&ldquo;This is all well and good, but <em>power asymmetries are not the cause "
                        "of the Axis of Evil</em>&rdquo; (7th ed., Vol. I, p. 371). Item 326&rsquo;s is "
                        "a label inside a borrowed figure &mdash; &ldquo;Cold spot (209,-57)&rdquo; "
                        "(p. 366). The chapter&rsquo;s own conclusion is hedged and disjunctive: the "
                        "CMB&rsquo;s characteristics &ldquo;<em>suggest</em> that our local system "
                        "&hellip; is <em>either</em> a central source <em>or</em> the central depository "
                        "or &lsquo;sink&rsquo; for the CMB radiation&rdquo; (p. 365)."),
        drift_type="unsourced_addition",
        note=r"""<p><strong>The comparison was run against two full editions and it came back mixed, so both halves are published.</strong> Texts searched, in full and only these: the 2006 <em>GWW_Final</em> PDF at Internet Archive item <code>GallileoWasWrong</code>, and the complete seventh edition (2013), Volumes 1&ndash;3, at item <code>galileo-was-wrong-the-church-was-right-sungenis-vol-1-3-complete</code>, cross-checked against the separate Vol. II scan at item <code>GalileoWasWrongTheChurchSungenisRobertA.Bennett4276</code>. The film&rsquo;s audio could not be transcribed from here and DeLano&rsquo;s blog was not exhaustively searched, so nothing below is a claim about those.</p>

<p><strong>Four of the six items have no counterpart to compare against in the texts searched, which is why the drift is recorded as <code>unsourced_addition</code>.</strong> &ldquo;Sachs&rdquo; returns zero occurrences in either edition, so item 331&rsquo;s ISW is not located there at all. Every occurrence of &ldquo;parity&rdquo; is either &ldquo;disparity&rdquo; or a discussion of <em>galaxy-spin</em> handedness belonging to <a href="#ARG-E05">ARG-E05</a>, so item 341&rsquo;s CMB point-parity statistic is not located there. Item 342&rsquo;s low-variance statistic is not located there either; the related anomaly the source does discuss is the vanishing two-point correlation function, which is a different measurement and is <a href="#ARG-E01">ARG-E01</a>&rsquo;s. Item 326&rsquo;s Cold Spot appears once, as a coordinate label printed inside a figure reproduced from Copi, Huterer, Schwarz &amp; Starkman&rsquo;s review, and is not argued from. The six items&rsquo; vocabulary &mdash; &ldquo;hemispheric power asymmetry&rdquo;, &ldquo;parity asymmetry&rdquo;, &ldquo;variance anomalies&rdquo; &mdash; is near verbatim the enumeration in Schwarz et al., CQG 33:184001 (2016) and the section headings of Planck 2018 VII. The most economical reading is that this cluster was assembled from a review of the anomaly literature rather than from the geocentric text it is credited to.</p>

<p><strong>The fifth item drifts a different way, and the enum only holds one value, so it is named here: item 339 is <code>reversed</code>.</strong> &ldquo;CMB hemispheric power asymmetry.&rdquo; stands on the list as a proof. In the source the hemispheric power asymmetry arrives as a quotation of the WMAP nine-year team reporting that they had traced it to asymmetric instrument beams and largely removed it, and the reply Sungenis writes underneath is that &ldquo;power asymmetries are not the cause of the Axis of Evil.&rdquo; He declines to use it. He is not conceding it &mdash; the distinction matters and the refutation keeps it &mdash; but the list is nonetheless running as an independent witness the one item its own authority set aside.</p>

<p><strong>The sixth, item 336, is <code>scope_widened</code>.</strong> The source&rsquo;s conclusion is hedged and disjunctive: the CMB&rsquo;s characteristics &ldquo;<em>suggest</em>&rdquo; that our local system is &ldquo;<em>either</em> a central source <em>or</em> the central depository or &lsquo;sink&rsquo;&rdquo; for the radiation (7th ed., Vol. I, p. 365). Bennett&rsquo;s technical chapter is more cautious still, listing four possible explanations for the correlations &mdash; systematic error, an unexpected foreground, cosmology, or a pure statistical fluke &mdash; and noting as its seventh summary point that it is &ldquo;becoming more likely that the large scale microwave sky has a <em>local</em> cause&rdquo;. &ldquo;Cosmic isotropy violations.&rdquo; states as established what the source states as a suggestion between disjuncts.</p>

<p><strong>The refutation above answers the source, not the fragment.</strong> It concedes the anomalies at the strength Planck gives them, quotes Planck calling their existence uncontested, keeps the significance question open, and puts the weight on two things the source itself supplies: the coordinates printed on the figure at p. 366, which show the two directional features of this cluster lying 56&deg; and 72&deg; off the axis the argument is built on, and the p. 371 sentence in which the source declines the item the list is selling. That is the pattern this project keeps finding &mdash; compression running consistently towards more certainty than the author was willing to state &mdash; with an unusually sharp instance here, because the compression did not merely firm up a hedge. It recruited four claims the source was not making and one it had explicitly put down.</p>""",
    ),

    verdict_challenge=dict(challenged=False, proposed_verdict=None, reasoning=None),

    people=["PER-SUNGENIS", "PER-BOUW"],
    related=["E01", "E03", "E04", "E05", "E06", "E09", "E11", "E13", "E17"],

    sources=[
        dict(label="Sungenis & Bennett, Galileo Was Wrong, 7th ed. (2013), complete Vols. 1–3 — "
                   "the anomaly-direction figure and its caption at Vol. I p. 366, the WMAP "
                   "beam-symmetrization passage and reply at p. 371, the hedged conclusion at "
                   "p. 365, Bennett's 26-anomaly list and four-possibilities passage at "
                   "Vol. II pp. 386–391",
             url="https://archive.org/details/galileo-was-wrong-the-church-was-right-sungenis-vol-1-3-complete"),
        dict(label="Sungenis & Bennett, Galileo Was Wrong (2006 “GWW_Final” printing) — the "
                   "Scientific American / Eriksen block quotation at Vol. I pp. 164–165, "
                   "including the “type of observational artifact” clause",
             url="https://archive.org/details/GallileoWasWrong"),
        dict(label="Sungenis, “Cosmological Evidence Shows Central and Non-Moving Earth”, "
                   "Proceedings of the NPA vol. 8, College Park MD 2011 — the same Eriksen "
                   "quotation and the same Schwarz figure caption, in a conference paper",
             url="https://isidore.co/misc/Physics%20papers%20and%20books/Cosmology/Copernican%20principle/from%20DeLano%20or%20his%20blog%20or%20some%20other%20website/abstracts_5969.pdf"),
        dict(label="Planck 2018 results VII, Isotropy and Statistics of the CMB, A&A 641:A7 — "
                   "“the existence of these features is uncontested”, the dipole-modulation "
                   "direction (221°, −20°), the 1.6% parity probability after look-elsewhere, "
                   "the mask-dependence of the low-variance anomaly, and the polarization nulls",
             url="https://arxiv.org/abs/1906.02552"),
        dict(label="Schwarz, Copi, Huterer & Starkman, “CMB Anomalies after Planck”, "
                   "CQG 33:184001 (2016) — the five-anomaly enumeration and the joint-significance "
                   "argument, which is the strongest form of this case",
             url="https://arxiv.org/abs/1510.07929"),
        dict(label="Copi, Huterer, Schwarz & Starkman, “Large-Angle Anomalies in the CMB”, "
                   "Advances in Astronomy 2010:847541 — the review the source's p. 366 figure "
                   "is taken from, and cites by name three pages later",
             url="https://arxiv.org/abs/1004.5602"),
        dict(label="Eriksen et al., “Asymmetries in the CMB anisotropy field”, ApJ 605:14 (2004) — "
                   "the original hemispherical power asymmetry",
             url="https://arxiv.org/abs/astro-ph/0307507"),
        dict(label="Mackenzie et al., “Evidence against a supervoid causing the CMB Cold Spot”, "
                   "MNRAS 470:2328 (2017) — the 2dF–VST ATLAS redshift survey of the Cold Spot core",
             url="https://academic.oup.com/mnras/article/470/2/2328/3752440"),
        dict(label="Szapudi et al., “Detection of a supervoid aligned with the cold spot of the "
                   "cosmic microwave background”, MNRAS 450:288 (2015) — the explanation that was "
                   "then tested",
             url="https://academic.oup.com/mnras/article/450/1/288/994945"),
        dict(label="“The CMB cold spot under the lens: ruling out a supervoid interpretation” "
                   "(arXiv:2211.16139) — lensing odds of about 1:13 to 1:20 against a large void",
             url="https://arxiv.org/abs/2211.16139"),
        dict(label="Santos & Zhao, “Preferred axis in the CMB parity asymmetry” — the parity axis "
                   "near the CMB dipole, read by its own authors as suggesting “a non-cosmological "
                   "origin of the large scale anomalies”",
             url="http://staff.ustc.edu.cn/~wzhao7/c_index_files/main.files/nova2.pdf"),
        dict(label="Francis & Peacock, “An estimate of the local ISW signal and its impact on CMB "
                   "anomalies”, MNRAS 406:14 (2010) — removing the local ISW reduces the low-ℓ "
                   "anomalies and the ecliptic node-line coincidence",
             url="https://academic.oup.com/mnras/article/406/1/14/1067322"),
        dict(label="Planck 2015 results XXI, The integrated Sachs-Wolfe effect, A&A 594:A21 — "
                   "joint detection at 4σ, about 3σ from Planck alone",
             url="https://www.aanda.org/articles/aa/full_html/2016/10/aa25831-15/aa25831-15.html"),
        dict(label="Hang, Alam, Cai & Peacock, “Stacked CMB lensing and ISW signals around "
                   "superstructures in the DESI Legacy Survey”, MNRAS 507:510 (2021) — combined "
                   "A_ISW = 0.68 ± 0.50, consistent with ΛCDM",
             url="https://academic.oup.com/mnras/article/507/1/510/6330470"),
        dict(label="Aluri et al., “Is the observable Universe consistent with the cosmological "
                   "principle?”, CQG 40:094001 (2023) — the live case that the FLRW paradigm may "
                   "need modifying",
             url="https://arxiv.org/abs/2207.05765"),
        dict(label="MacAndrew (GeocentrismDebunked), “Sungenis Fails the CMB Challenge” — an "
                   "independent audit of the same chapter's calculations",
             url="https://www.geocentrismdebunked.org/sungenis-fails-cmb-challenge/"),
    ]),
}
