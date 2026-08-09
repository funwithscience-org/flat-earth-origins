# -*- coding: utf-8 -*-
"""Batch 6 — A05. "No measurable stellar parallax." 6 items, lane A-EXP.

Findings a future session should not have to re-derive.

1. OUR EDITION ATTRIBUTION IS WRONG, AND THE ERROR MATTERS FOR ANACHRONISM.
   The cluster credits the parallax material to Rowbotham 1865. It is not in
   the 1865 first book edition. Two independent full-text queries against
   Project Gutenberg #69892 (the 1865 Simpkin, Marshall printing) return the
   string "parallax" exactly twice — the title-page byline BY "PARALLAX" and
   the catalogue metadata. Its SECTION II, "The Earth no Axial or Orbital
   Motion", carries the air-gun test and the two-parallel-tubes test and does
   not mention annual parallax, Tycho, Kepler, Bessel or stellar distance.
   The parallax argument is an addition of the 1881 third edition, where it
   occupies ch. III, pp. 82-87 (sacred-texts za21.htm). Same pattern the B01
   and lighthouse siblings found: material credited to the early Rowbotham
   first appears decades later.

2. "ROWBOTHAM TOOK HIS PSEUDONYM FROM THE THING HE DENIED" IS NOT TRUE AS
   WRITTEN, and it is in the cluster `basis` string, i.e. on the page.
   (a) He adopted "Parallax" by the end of 1849 (Schadewald, The Plane Truth
   ch. 1: he "had abandoned the pseudonym S. Goulden and begun calling himself
   'Parallax'"), 32 years before he wrote a word about stellar parallax.
   (b) Schadewald's reading of the choice is the generic optical sense — the
   apparent change in an object's position with a change of viewpoint — which
   is the engine of Rowbotham's own perspective theory. He relied on it.
   (c) Even in 1881 he does not deny that stellar parallax is observed. He
   quotes Henderson's 0".98 and Bessel's 0".35 approvingly and reassigns the
   cause. The line is a pun that reads as a fact. Recommended replacement is
   in the report; the tldr here does not use it.

3. THE KERNEL IS BASE-LINE SCALING, AND THE EXPERIMENT EXISTS. Rowbotham
   identified the correct discriminating test — parallax is evidence of the
   Earth's orbit only if the displacement scales with the base line — and
   answered it with the two-parallel-tubes trial of pp. 79-81 of the same 1881
   chapter (za21.htm): two bored tubes "not less than six feet in length", "one
   yard asunder", axes "perfectly parallel", two observers knocking as a star
   near meridian enters each tube, result "a distinct period of time will
   elapse between the signals given". One yard IS three feet, so the p. 86
   sentence back-references it. We formerly wrote "No experiment follows. No
   apparatus…" in six places; that was false and is corrected (2026-08-09).
   The true refutation is stronger: the real angle over one yard is
   1.7e-12 arcsec against a naked-eye limit near 60 arcsec — ~13 orders of
   magnitude — so the audible lag measures the misalignment of his own tubes,
   amplified by the star's diurnal drift of up to ~15 arcsec per second of
   time. Run properly, the base-line test confirms the orbit.

4. THE LIST DOES NOT REVERSE ITS SOURCE; THE DESCENDANT DOES. Dubay's proof 19
   — "not a single inch of parallax can be detected in the stars" — is the
   reversal, and Rowbotham's text contains the detections. None of the six list
   items says that: 5/37/264 are scoped true statements promoted to proofs,
   8/240 are unsourced additions, 103 is faithful. drift_type corrected from
   "reversed" to "hedge_dropped" (2026-08-09), matching this block's own
   item-by-item tally. NOT FIXED HERE: the cluster label in clusters.py still
   reads "No measurable stellar parallax", which overstates the six items; it
   is outside this file and left for the parent.

5. STAR SIZES: NO SATURN. Graney's Church Life Journal piece gives Locher's
   figure as "any first-magnitude star well larger than the whole orbit of the
   Earth", and "Saturn" is not located in Graney & Grayson, arXiv 1003.4918.
   Our "as wide as Saturn's orbit, on Graney and Grayson's reconstruction" was
   an invented quantity and is corrected (2026-08-09).
"""

ENTRY = {

"A05": dict(
    tldr=("This cluster reads as a denial that parallax is measurable. Its own source prints "
          "the measurements: Henderson's 0.98 arcsec for Alpha Centauri, Bessel's 0.35 arcsec "
          "for a star in Cygnus, both quoted approvingly by Rowbotham. What he actually argued "
          "is that a three-foot base line gives the same displacement as the Earth's orbit — "
          "the right discriminating test — and he backed it with two six-foot tubes set a yard "
          "apart, an instrument some thirteen orders of magnitude too coarse to run it. Run it "
          "properly: over three feet 61 Cygni shifts by about 1.7 trillionths of an arcsecond, "
          "roughly eleven million times below what Gaia can resolve."),

    passage=dict(
        work="WRK-ROWBOTHAM-1865", pd=True,
        locator=("3rd ed., rev. and enl. (London: Day, 1881), ch. III “The Earth No Axial or "
                 "Orbital Motion”, pp. 82–87. Not in the 1865 first book edition — see gloss."),
        quote=(
            "Tycho Brahe, Kepler, and others, rejected the Copernican theory, principally on "
            "account of the failure to detect displacement or parallax of the fixed stars. "
            "[p. 82]\n\n"
            "Dr. Bradley declared that what many had called “parallax,” was merely “aberration.” "
            "But “Dr. Brinkley, in 1810, from his observations with a very fine circle in the "
            "Royal Observatory of Dublin, thought he had detected a parallax of 1″ in the bright "
            "star Lyra (corresponding to an annual displacement of 2″). This, however, proved to "
            "be illusory; and it was not till the year 1839, that Mr. Henderson …” [pp. 82–83]\n\n"
            "The parallax thus assigned α Centauri, is so very nearly a whole second in amount "
            "(0″.98), that we may speak of it as such. … “Professor Bessel made the parallax of "
            "a star in the constellation Cygnus to be 0″.35.” [pp. 83–84]\n\n"
            "… it is only necessary to state as an absolute truth the result of actual "
            "experiment, that, a given fixed star will, when observed from the two ends of a "
            "base line of not more than three feet, give a parallax equal to that which it is "
            "said is observed only from the two extremities of the earth's orbit. [p. 86]\n\n"
            "It is useless to say, in explanation, that this very minute displacement, is owing "
            "to the almost infinite distance of the fixed stars; because the very same stars "
            "show an equal degree of parallax from a very minute base line. [p. 86]"),
        gloss=(
            "<p><strong>The edition is not the one we credited, and the correction cuts both "
            "ways.</strong> Our cluster record attributes this material to Rowbotham 1865. It is "
            "not there. Two independent full-text queries against Project Gutenberg #69892 &mdash; "
            "the 1865 Simpkin, Marshall first book edition &mdash; return the string "
            "&ldquo;parallax&rdquo; twice, both times as the author&rsquo;s byline. That "
            "edition&rsquo;s SECTION II, <em>The Earth no Axial or Orbital Motion</em>, contains "
            "the vertical air-gun test and the two-parallel-tubes test and no discussion of annual "
            "parallax, of Tycho, Kepler, Bradley, Brinkley, Henderson or Bessel, and no statement "
            "about the distance or apparent size of the stars. The whole argument above is an "
            "addition of the <strong>1881 third edition</strong>, which grew the book from 221 to "
            "430 pages.</p>"
            "<p>That matters, because our own rule is that charging an author with ignoring data "
            "is a serious fault unless the data was available <em>to them, then</em>. Dating the "
            "passage to 1881 removes any excuse: it puts Rowbotham 43 years after Bessel, writing "
            "with Henderson&rsquo;s and Bessel&rsquo;s numbers open in front of him &mdash; he "
            "prints them &mdash; and it is in that setting that he answers them with an experiment "
            "whose apparatus cannot resolve the angle in dispute.</p>"
            "<p><strong>Note what he does not say.</strong> He does not say parallax is unobserved. "
            "He recites the failures (Tycho, Kepler, Brinkley&rsquo;s illusory second of arc), then "
            "the successes, then reassigns the successes to a three-foot base line. The compressed "
            "list items say the opposite of this, and so does the movement&rsquo;s modern "
            "descendant: Eric Dubay&rsquo;s proof 19 asserts that &ldquo;after 190,000,000 miles "
            "of supposed orbit around the Sun, not a single inch of parallax can be detected in "
            "the stars, proving we have not moved at all.&rdquo; Rowbotham&rsquo;s own chapter "
            "contains the inches.</p>"
            "<p><strong>And the pseudonym line is a pun, not a fact.</strong> Our basis string "
            "says he &ldquo;took his pseudonym from the thing he denied.&rdquo; He adopted "
            "&ldquo;Parallax&rdquo; by the end of 1849, dropping an earlier pseudonym, and "
            "Schadewald reads the choice as the ordinary optical sense of the word &mdash; the "
            "apparent change in a thing&rsquo;s position when the viewer moves &mdash; which is "
            "the mechanism his entire perspective account of sunset runs on. He named himself "
            "after a principle he used, three decades before he wrote about the astronomical "
            "measurement, and when he finally did write about it he conceded the observations. "
            "The sentence is too good to be true and should come off the page.</p>")),

    steelman=dict(
        description=(
            "<p><strong>SURFACE (weak &mdash; do not use).</strong> &ldquo;They think parallax has "
            "never been measured.&rdquo; Aimed at the fragment, and it misses the source by a wide "
            "margin. Rowbotham quotes the measurements. Anyone who opens with this is answering "
            "Dubay&rsquo;s 2015 paraphrase and will be shown the 1881 text.</p>"
            "<p><strong>DEEPER.</strong> Two of the six items are simply true, and the strongest "
            "one is a genuine classical objection. <em>&ldquo;No naked-eye parallax&rdquo;</em> is "
            "correct: the largest annual parallax of any star is Proxima&rsquo;s 768.07 mas, about "
            "0.77 arcsec, and the unaided eye resolves roughly one arcminute &mdash; eighty times "
            "coarser. <em>&ldquo;Lack of stellar parallax in early measurements&rdquo;</em> is also "
            "correct, and it is not a small fact: from Copernicus to Bessel, some three centuries, "
            "the predicted effect was looked for and not found, and every claimed detection before "
            "1837 collapsed. Hooke, Flamsteed and Bradley all tried; Bradley&rsquo;s search "
            "produced aberration and nutation instead of parallax; Calandrelli got four arcseconds "
            "for Vega and Brinkley one arcsecond for the same star in 1810, and both were "
            "illusory. This is exactly why Ptolemy and, far more rigorously, Tycho Brahe rejected "
            "a moving Earth.</p>"
            "<p><strong>KERNEL.</strong> Two things, and the second is the sharper.</p>"
            "<p><em>First, Tycho&rsquo;s version was a valid deduction from a false premise, and "
            "the false premise was an instrument.</em> Tycho could see that stars appeared to have "
            "real angular diameters. If a star subtends a measurable disc and must also be far "
            "enough away to show no parallax, then it is physically enormous &mdash; on "
            "Graney&rsquo;s rendering of Locher, who cites Tycho, any first-magnitude star &ldquo;well "
            "larger than the whole orbit of the Earth&rdquo;, and "
            "Ingoli&rsquo;s version has the fixed stars &ldquo;surpass or equal the size of the "
            "orbit circle of the Earth itself.&rdquo; That is a real physical absurdity derived by "
            "correct reasoning from an observation anyone could repeat. The observation was wrong, "
            "and not because Tycho was careless: the apparent discs are diffraction and "
            "atmospheric seeing, the point-spread function of the eye and later of the telescope, "
            "and nobody could have known that before Airy&rsquo;s <em>On the Diffraction of an "
            "Object-Glass with Circular Aperture</em> in 1835. The star-size argument is therefore "
            "not a stupid argument. It is a dated one, and the date is legible.</p>"
            "<p><em>Second, Rowbotham identified the correct discriminating test.</em> This is the "
            "best thing in the cluster and the list has thrown it away. He understood, correctly, "
            "that a measured stellar displacement is evidence for the Earth&rsquo;s orbit only if "
            "the displacement is <strong>caused by the base line</strong> &mdash; and therefore "
            "that the way to settle it is to change the base line and see whether the answer "
            "changes. That is a properly zetetic instinct and it is the right experiment. His "
            "claim is that a three-foot base line yields the same parallax as the orbit, which "
            "would show the effect has nothing to do with the Earth&rsquo;s position and "
            "everything to do with the observer&rsquo;s. If that were so, the entire distance "
            "ladder would fall in an afternoon.</p>"),
        why_it_doesnt_save_claim=(
            "<p><strong>Because the base-line test has been run, continuously, for 188 years, and "
            "it answers the other way.</strong> Parallax scales linearly with the base line and "
            "inversely with distance; that is not an assumption of the model but the definition of "
            "the quantity. 61 Cygni A shows 285.9949 &plusmn; 0.0599 mas on a one-astronomical-unit "
            "base line (Gaia DR3). Three feet is 6.1 &times; 10<sup>&minus;12</sup> of an "
            "astronomical unit, so on Rowbotham&rsquo;s base line the same star must shift by about "
            "1.7 &times; 10<sup>&minus;12</sup> arcsec &mdash; roughly eleven million times smaller "
            "than Gaia&rsquo;s median uncertainty of 0.02&ndash;0.03 mas. His &ldquo;equal degree "
            "of parallax from a very minute base line&rdquo; is not a marginal error. It is off by "
            "eleven orders of magnitude, and the only observation he offers for it is a pair of "
            "hand-aligned tubes on a wooden frame &mdash; a strange foundation in a book whose "
            "method is to take nothing for granted.</p>"
            "<p><strong>Because the naked-eye point dates the argument instead of supporting "
            "it.</strong> &ldquo;No naked-eye parallax&rdquo; is true and inert. It is the "
            "observation that <em>every</em> annual parallax is smaller than one arcsecond, which "
            "is what a heliocentric model with distant stars predicts. It stopped being an "
            "objection the moment the instruments crossed the threshold, and we can name the "
            "years: Struve on Vega in 1837, Bessel on 61 Cygni in 1838, Henderson on "
            "&alpha; Centauri in 1839.</p>"
            "<p><strong>And because the false premise underneath the strongest version has been "
            "measured.</strong> Real stellar angular diameters are milliarcseconds. The largest "
            "yet found, R Doradus, is 0.057 &plusmn; 0.005 arcsec &mdash; about one thousandth of "
            "the eye&rsquo;s resolution limit, and thirty per cent larger than Betelgeuse, which "
            "held the record for 75 years. Nobody has ever seen a stellar disc with the naked eye "
            "or through a Victorian telescope. What they saw was their own optics.</p>")),

    refutation=(
        "<p><strong>1. Answer the 1881 text, because the fragment is not what its author "
        "said.</strong> Rowbotham&rsquo;s chapter concedes more than the list does. He recites the "
        "history of failure &mdash; Tycho, Kepler, Bradley&rsquo;s reassignment of &ldquo;what "
        "many had called &lsquo;parallax&rsquo;&rdquo; to aberration, Brinkley&rsquo;s 1810 "
        "arcsecond for Vega that &ldquo;proved to be illusory&rdquo; &mdash; and then quotes the "
        "successes: 0&Prime;.98 for &alpha; Centauri, 0&Prime;.35 for Bessel&rsquo;s star in "
        "Cygnus. His position is not that the displacement is absent. It is that the displacement "
        "is real and has a different cause. That is a better argument than the one on the list, "
        "and it is the one we have to beat.</p>"

        "<p><strong>2. The chronology, stated precisely, because it decides how much blame is "
        "fair.</strong> Bessel published 61 Cygni in 1838; Struve had published Vega in 1837 and "
        "Henderson &alpha; Centauri in 1839. Take the three dates in Rowbotham&rsquo;s career "
        "separately.</p>"
        "<p><em>1849, the sixteen-page pamphlet, and the year he adopted the name "
        "&ldquo;Parallax&rdquo;.</em> Eleven years after Bessel &mdash; but scepticism was still "
        "defensible, and we should say so. Three results existed, all at the edge of what "
        "heliometers and filar micrometers could do, and they did not agree well. Struve got "
        "0.125&Prime; for Vega in 1837 and then <em>revised it to 0.261&Prime; in 1840</em>, which "
        "is twice the modern 0.130&Prime; and a move away from the truth. Henderson published one "
        "arcsecond for &alpha; Centauri against a modern 0.75&Prime;. Bessel&rsquo;s 0.3136&Prime; "
        "for 61 Cygni is about ten per cent above the modern 0.2860&Prime;, and a later reduction "
        "of his own data moved it further out, to 0.360&Prime;. Behind them lay a century of "
        "retracted claims. A well-informed sceptic in 1849 could reasonably have said: these are "
        "three heroic measurements at the limit of the art, they disagree, and claims of this kind "
        "have collapsed before. He would have been in a shrinking minority &mdash; the Royal "
        "Astronomical Society had already given Bessel its gold medal, and John Herschel called "
        "the result &ldquo;the greatest and most glorious triumph which practical astronomy has "
        "ever witnessed&rdquo; &mdash; but the position was available. The 1849 pamphlet does not "
        "take it; it does not discuss the matter at all.</p>"
        "<p><em>1865, the first book edition.</em> Twenty-seven years after Bessel, and still "
        "nothing. Its Section II, with the same title the 1881 chapter carries, argues against "
        "orbital motion from an air-gun and from two parallel tubes, and never mentions annual "
        "parallax. By this date the objection was strained: the results had been confirmed by "
        "other observers on other stars with other instruments, and the disagreements had begun "
        "to close rather than widen. But silence is not an error, and we should not score it as "
        "one.</p>"
        "<p><em>1881, the third edition.</em> Forty-three years after Bessel, and this is where "
        "the fault is. He now engages, prints the numbers, and answers them with a factual claim "
        "&mdash; three feet gives the same parallax as the orbit &mdash; introduced with the words "
        "&ldquo;it is only necessary to state as an absolute truth the result of actual "
        "experiment.&rdquo; The experiment is there, and it is the weak point. Seven pages "
        "earlier, at pp. 79&ndash;81 of the same chapter, he sets out the apparatus: two "
        "carefully-bored metallic tubes &ldquo;not less than six feet in length&rdquo;, placed "
        "&ldquo;one yard asunder&rdquo; on a wooden frame and adjusted so that their axes of "
        "vision &ldquo;shall be perfectly parallel to each other&rdquo;, directed at a notable "
        "fixed star a few seconds before its meridian time, with an observer at each tube "
        "knocking the moment the star enters his field. His reported result is that &ldquo;a "
        "distinct period of time will elapse between the signals given&rdquo; &mdash; the same "
        "star is &ldquo;not visible at the same moment by two parallel lines of sight &hellip; "
        "when only one yard asunder.&rdquo; One yard is three feet, so the p. 86 sentence we "
        "quote is a back-reference to that trial rather than a bare assertion.</p>"
        "<p><strong>The trouble is what the rig can resolve.</strong> Over a one-yard base line "
        "61 Cygni is displaced by about 1.7 &times; 10<sup>&minus;12</sup> arcsec, while a naked "
        "eye behind an unmagnifying six-foot tube resolves no better than about a minute of arc "
        "&mdash; some thirteen orders of magnitude coarser. Two genuinely parallel tubes a yard "
        "apart must therefore show the star at the same instant. A lag between the knocks "
        "measures one quantity only: the residual angle between the two axes, which the "
        "star&rsquo;s diurnal motion &mdash; up to about 15 arcsec per second of time &mdash; "
        "turns into a delay long enough to hear. Rowbotham sees the mechanism and reads it the "
        "other way, noting that &ldquo;a slight inclination of the tube, B, C, towards the first "
        "tube A, S, would be required for the star, S, to be seen through both tubes at the same "
        "instant.&rdquo; He names no star, no date, no observer and no measured angle, and he "
        "reports no alignment control &mdash; reversing the frame end for end, or repeating the "
        "trial on a second star, would have separated the sky from the woodwork. In a book whose "
        "founding rule is to proceed &ldquo;only by inquiry; to take nothing for granted,&rdquo; "
        "the one check that would have told him which of the two he was reading is the one not "
        "made. <strong>This is not anachronism, it is the opposite:</strong> he had the data, he "
        "quoted the data, and he set it aside on the authority of an instrument that reads out "
        "its own construction error.</p>"

        "<p><strong>3. The classical objection was rigorous, and it died of measurement.</strong> "
        "Ptolemy&rsquo;s reason for a stationary Earth, and far more sharply Tycho&rsquo;s, was "
        "that no stellar displacement is seen. Tycho&rsquo;s version is the one that deserves "
        "respect: stars appeared to have angular diameters, so a star distant enough to hide its "
        "parallax would have to be physically vast &mdash; larger than the whole orbit of the "
        "Earth, on Graney&rsquo;s account of Locher; Ingoli, following Tycho, has the fixed stars "
        "&ldquo;surpass or equal the size of the orbit circle of the Earth itself.&rdquo; Valid "
        "reasoning, absurd conclusion, and therefore &mdash; correctly, by the standards of the "
        "time &mdash; a reason to reject the premise. The premise that was false was the "
        "observation. Stars have no visible discs. What Tycho measured with the eye and what "
        "Galileo, Hevelius and Cassini measured with early telescopes (roughly 4&ndash;6 arcsec "
        "for Sirius and for &ldquo;an average fixed star&rdquo;) was the instrument&rsquo;s "
        "point-spread function: diffraction, plus seeing, plus the eye&rsquo;s own optics. Airy "
        "published the theory in 1835 &mdash; the image of a star &ldquo;will not be a point but a "
        "bright circle surrounded by a series of bright rings&rdquo; &mdash; and Graney and "
        "Grayson trace how slowly even professional astronomers absorbed it. True stellar "
        "diameters are three orders of magnitude smaller than the eye can resolve: the largest "
        "ever measured, R Doradus, is 0.057 arcsec against the eye&rsquo;s roughly 60 arcsec. "
        "<strong>Item 8, &ldquo;Constant stellar angular sizes&rdquo;, is therefore false twice "
        "over</strong> &mdash; the naked-eye sizes are not the stars, and the real sizes are not "
        "constant, running from under a milliarcsecond to 57 mas across the interferometric "
        "catalogues.</p>"

        "<p><strong>4. What parallax actually is, and why it discriminates.</strong> This is the "
        "part the cluster never engages. Parallax is not &ldquo;a small wobble astronomers "
        "report.&rdquo; It is a geometric consequence of the observer changing position, and a "
        "moving Earth predicts four specific things about it, all of which are observed:</p>"
        "<ul>"
        "<li><strong>It exists at all</strong>, and its size is set by the base line &mdash; one "
        "astronomical unit by convention, the full orbital diameter over six months.</li>"
        "<li><strong>Its period is exactly one year</strong>, and its phase is locked to the "
        "Earth&rsquo;s position in orbit. Nothing in a stationary-Earth account explains why the "
        "displacement should return to itself annually rather than daily, or on any other "
        "period.</li>"
        "<li><strong>The parallax ellipse is oriented</strong>: its major axis lies parallel to "
        "the ecliptic and its shape depends on the star&rsquo;s ecliptic latitude, a star at the "
        "ecliptic pole tracing a circle and one on the ecliptic tracing a line. That is the shape "
        "of the Earth&rsquo;s orbit projected onto the sky, and it is measured.</li>"
        "<li><strong>Its amplitude goes as 1/distance</strong>, and the distances are checkable "
        "independently &mdash; by VLBI radio astrometry, by eclipsing binaries, by cluster "
        "main-sequence fitting, by Cepheids. They agree.</li>"
        "</ul>"
        "<p>Modern astrometry does not measure a displacement and call it parallax. Gaia fits five "
        "parameters at once &mdash; two positions, two proper-motion components and one parallax "
        "&mdash; to years of observations, precisely so that the annual periodic term is separated "
        "from the secular linear one. Gaia DR3 publishes that solution for "
        "<strong>1,467,744,818 sources</strong> out of 1,811,709,771 total, with median parallax "
        "uncertainties of <strong>0.02&ndash;0.03 mas for G &lt; 15</strong>, 0.07 mas at G = 17 "
        "and 0.5 mas at G = 20. 61 Cygni, Bessel&rsquo;s star, now reads 285.9949 &plusmn; 0.0599 "
        "mas (A) and 286.0054 &plusmn; 0.0289 mas (B): 11.404 light years. Bessel, with a "
        "heliometer in 1838, got 0.3136&Prime; &mdash; ten per cent high and unmistakably the same "
        "quantity. Proxima Centauri reads 768.0665 &plusmn; 0.0499 mas, 4.2465 light years.</p>"

        "<p><strong>5. Item 103, &ldquo;Inconsistent stellar parallax&rdquo;, points at something "
        "real. Answer the real version.</strong> Parallax measurements have disagreed, sometimes "
        "publicly and embarrassingly. Struve doubled his own Vega value between 1837 and 1840. "
        "And the best modern case is the Pleiades: Hipparcos returned about 115&ndash;120 pc "
        "against a long-standing ~130 pc from every other method, a discrepancy serious enough to "
        "call stellar-evolution models into question. It was not waved away. Melis and colleagues "
        "settled it in 2014 by VLBI &mdash; a completely different instrument and technique &mdash; "
        "at 136.2 &plusmn; 1.2 pc, and Gaia DR2 then gave 136.67 &plusmn; 0.04 pc from a weighted "
        "mean of 1,595 stars. Hipparcos was the outlier, for reasons internal to its data "
        "reduction. Gaia&rsquo;s own systematics are published in the same spirit: Lindegren and "
        "colleagues report that quasar parallaxes, which should average zero, are offset by "
        "&ldquo;a few tens of microarcsec&rdquo;, varying with magnitude, colour and ecliptic "
        "latitude, and they publish the correction. <strong>That is the difference between the two "
        "enterprises.</strong> The inconsistencies are real, they are found by the people who made "
        "the measurements, they are quantified, and they are two to four orders of magnitude "
        "smaller than the parallaxes themselves. An inconsistency of tens of microarcseconds does "
        "not license the conclusion that a 768,000-microarcsecond parallax is imaginary.</p>"

        "<p><strong>6. Item 240, &ldquo;Stellar proper motion tiny&rdquo;, is a different "
        "phenomenon and it inverts.</strong> Proper motion is the star&rsquo;s own secular drift "
        "across the sky; parallax is the annual periodic loop caused by our motion. They are "
        "separately fitted parameters and confusing them is a category error. Nor is proper motion "
        "zero, or uniform. Halley detected it in 1718 by comparing Sirius, Arcturus and Aldebaran "
        "with the ancient catalogues &mdash; which by itself retires any rigid firmament, since a "
        "rigid sphere cannot have its lights drift relative to one another. Barnard&rsquo;s Star "
        "moves 10.3 arcsec per year, so the constellation it sits in visibly deforms within a "
        "human lifetime. Gaia DR3 publishes proper motions for the same 1.468 billion sources at "
        "0.02&ndash;0.03 mas/yr for G &lt; 15. And the pattern is the one the distance model "
        "predicts and the dome model has no reason to expect: <strong>the stars with the largest "
        "proper motions are the nearest ones</strong>. Barnard&rsquo;s Star, with the largest "
        "known proper motion, has a parallax of 546.9759 &plusmn; 0.0401 mas &mdash; 5.96 light "
        "years. Proxima, the nearest star at 768.07 mas, moves 3.85 arcsec per year. Convert "
        "through the distance and the velocities come out ordinary: Barnard&rsquo;s Star crosses "
        "the sky at about 89 km/s, a perfectly normal speed for a star in the galactic disc. On "
        "the same numbers a firmament a few thousand miles up requires those two stars to be "
        "creeping at centimetres per second while the rest of the sky holds rigid formation, and "
        "requires the correlation between apparent drift and apparent annual loop to be a "
        "coincidence. It is not a coincidence; it is the same distance appearing in both "
        "measurements.</p>"

        "<p><strong>7. What the cluster is, as a document.</strong> Six items, of which two "
        "(37 and 264) are the identical sentence &mdash; &ldquo;No naked-eye parallax.&rdquo; "
        "&mdash; entered twice, 227 apart. One of the three exact duplicate pairs in the whole "
        "461-item specimen falls inside this one cluster of six. Two more items (5 and 37/264) "
        "are true statements with their scope intact, sitting in a numbered list of evidence for a "
        "stationary Earth. Two (8 and 240) have no counterpart in either text we searched &mdash; "
        "the 1865 first book edition and the 1881 third edition&rsquo;s ch. III. "
        "One (103) is a fair compression of a real argument. That distribution is not what a "
        "reading of Rowbotham produces; it is what paraphrase-expansion of a handful of stock "
        "sentences produces, and the duplicate is the fingerprint.</p>"

        "<p><strong>Verdict: refuted.</strong> Parallax is measured, at 0.02 mas precision, for "
        "1.468 billion stars, with the annual period, the ecliptic-aligned ellipse and the "
        "inverse-distance amplitude that only a moving Earth predicts. The source&rsquo;s own "
        "chapter contains the measurements the list says do not exist, and the one claim that "
        "would defeat them &mdash; equal parallax from a three-foot base line &mdash; is wrong by "
        "eleven orders of magnitude, and the experiment offered for it measures the alignment of "
        "his own tubes.</p>"),

    advocate=dict(
        best_defense=(
            "You have spent most of your space agreeing with us. You concede that no parallax is "
            "visible to the naked eye, that three centuries of searching found nothing, that "
            "Tycho's objection was rigorous, that the first results disagreed with each other by "
            "factors of two, that Struve moved his own answer the wrong way, that Hipparcos got "
            "the Pleiades wrong by fifteen per cent, and that Gaia carries a published zero-point "
            "offset it has to correct out. Then you ask us to accept a quantity nobody can see, "
            "reported at a precision of twenty microarcseconds, by one spacecraft, through a "
            "five-parameter model whose parameters are not independently observable but are fitted "
            "simultaneously to the same data. That is not an observation, it is a reduction. "
            "Rowbotham's point survives your arithmetic because it was never arithmetic: the "
            "displacement you attribute to the Earth's orbit is an artefact of the instrument and "
            "the model, and the Pleiades episode is your own proof that a whole community can "
            "believe a wrong parallax for fifteen years until a different instrument contradicts "
            "it. You have shown that parallax measurements are revisable. We agree. Revisable "
            "measurements do not carry the weight of a cosmology."),
        survives=3,
        preemptive=(
            "Rated 3: it does not touch the physics, but it exploits our own honesty about "
            "systematics and it will land with a reader who skims. The body must pre-empt it in "
            "two specific ways, and section 5 above is written to do so. (a) State the ratio "
            "explicitly rather than leaving the reader to compute it: the systematics we admit to "
            "are tens of microarcseconds against parallaxes of hundreds of thousands of "
            "microarcseconds, i.e. one part in ten thousand, and an error bar four orders of "
            "magnitude below a signal is a reason to trust the signal, not to discard it. (b) Kill "
            "the 'one spacecraft, one model' move by naming the independent confirmations in the "
            "text, which section 5 does: the Pleiades were settled by VLBI radio astrometry before "
            "Gaia ever reported on them, and Gaia then agreed with VLBI to better than half a "
            "parsec. The Pleiades episode is the advocate's best card and it is ours &mdash; it is "
            "a worked example of an independent technique catching and correcting a parallax "
            "error, which is exactly the process the argument claims does not happen. Add one "
            "sentence to section 5 saying so in those words. Do not soften our admission of the "
            "Gaia zero point; delete it and the site is worse than the argument it is answering."),
    ),

    straw_man=dict(
        identified=True,
        detail=(
            "Yes, and it is quantitative rather than rhetorical. The modern descendant of this "
            "cluster, Dubay's proof 19, states that “after 190,000,000 miles of supposed "
            "orbit around the Sun, not a single inch of parallax can be detected in the stars, "
            "proving we have not moved at all.” No astronomer has claimed anything the "
            "sentence describes and no source in this lineage supports it — least of all "
            "Rowbotham, who prints 0″.98 and 0″.35 on facing pages. The straw man is "
            "of astronomy in one direction and of the movement's own founder in the other, which "
            "is unusual: the compression has manufactured a claim that neither side holds. The "
            "same proof also misattributes the whole objection to Tycho Brahe without mentioning "
            "that Tycho's version depended on stellar angular diameters that turned out to be "
            "diffraction."),
    ),

    compression=dict(
        assessed=True, drifted=True,
        list_phrasing=("Lack of stellar parallax in early measurements. / Constant stellar angular "
                       "sizes. / No naked-eye parallax. / Inconsistent stellar parallax. / Stellar "
                       "proper motion tiny. / No naked-eye parallax. — items 5, 8, 37, 103, 240, "
                       "264; 37 and 264 are the same sentence entered twice."),
        source_wording=("&ldquo;The parallax thus assigned &alpha; Centauri, is so very nearly a "
                        "whole second in amount (0&Prime;.98), that we may speak of it as such. … "
                        "&lsquo;Professor Bessel made the parallax of a star in the constellation "
                        "Cygnus to be 0&Prime;.35.&rsquo;&rdquo; … &ldquo;it is only necessary to "
                        "state as an absolute truth the result of actual experiment, that, a given "
                        "fixed star will, when observed from the two ends of a base line of not "
                        "more than three feet, give a parallax equal to that which it is said is "
                        "observed only from the two extremities of the earth&rsquo;s orbit.&rdquo;"),
        drift_type="hedge_dropped",
        note=(
            "<p><strong>The dominant drift is a qualifier doing no work.</strong> Items 5, 37 and "
            "264 keep their scope &mdash; <em>early</em> measurements, <em>naked-eye</em> parallax "
            "&mdash; and as written are simply true; what changes is that a scoped historical "
            "observation is entered as a numbered proof of a stationary Earth, where the reader "
            "supplies the generalisation the sentence withholds. Note what the list does "
            "<em>not</em> do: no item in it denies that parallax is detected. That denial arrives "
            "downstream, in Dubay&rsquo;s proof 19 &mdash; &ldquo;not a single inch of parallax "
            "can be detected in the stars, proving we have not moved at all&rdquo; &mdash; and "
            "<em>that</em> is a straight reversal of the source, which quotes two values to two "
            "decimal places, 0&Prime;.98 and 0&Prime;.35, and argues about their <em>cause</em>: a "
            "three-foot base line rather than a 186-million-mile one. That is a falsifiable claim "
            "about base-line scaling, and it is a different and stronger claim than &ldquo;no "
            "parallax exists.&rdquo; The reversal also shaped this cluster&rsquo;s label and the "
            "drift type this block used to carry, both of which read the downstream slogan back "
            "onto the six items; the drift type is corrected above. A summary that overstates the "
            "items it summarises is the same fault we are documenting.</p>"
            "<p><strong>The six items, one by one, because they are not all the same "
            "type.</strong></p>"
            "<ul>"
            "<li><strong>Items 5, 37 and 264</strong> &mdash; <em>hedge_dropped shading into "
            "force_upgraded</em>. &ldquo;Lack of stellar parallax in <em>early</em> "
            "measurements&rdquo; and &ldquo;No <em>naked-eye</em> parallax&rdquo; keep their "
            "qualifiers and are, as written, simply true. What changes is the speech act: a scoped "
            "historical observation appears in a numbered list of proofs of a stationary Earth, "
            "where the qualifier does no work and the reader supplies the missing generalisation. "
            "Nothing was misquoted; a true sentence was promoted to a proof.</li>"
            "<li><strong>Items 8 and 240</strong> &mdash; <em>unsourced_addition</em>. Neither is "
            "located in the 1865 first book edition (Project Gutenberg #69892) or in ch. III of "
            "the 1881 third edition, the two texts searched. &ldquo;Constant stellar angular "
            "sizes&rdquo; is Tycho&rsquo;s star-size objection arriving without Tycho and without "
            "the diffraction that dissolved it; &ldquo;Stellar proper motion tiny&rdquo; imports a "
            "phenomenon that appears in neither of those two texts and, on inspection, one that "
            "argues against him. "
            "Rowbotham&rsquo;s cosmos puts the stars a few thousand miles up; nothing in it "
            "explains why nearby stars by parallax should also be the fast-moving ones by proper "
            "motion.</li>"
            "<li><strong>Item 103</strong> &mdash; the one faithful compression. "
            "&ldquo;Inconsistent stellar parallax&rdquo; is a fair summary of Rowbotham&rsquo;s "
            "actual recital of Bradley, Brinkley and the illusory arcsecond, and it points at a "
            "real feature of the record. It is answered on the merits in the refutation, not "
            "dismissed.</li>"
            "</ul>"
            "<p><strong>And one structural note.</strong> Items 37 and 264 are the identical "
            "sentence, entered twice, 227 items apart &mdash; one of only three exact duplicate "
            "pairs in the entire 461-item specimen, and it falls inside a cluster of six. Six items "
            "on one topic, of which two are the same sentence, two have no source, one is true and "
            "inert and one is faithful. That is the shape of a list assembled by fanning "
            "paraphrases out of a few stock lines, not by reading Rowbotham.</p>")),

    verdict_challenge=dict(challenged=False, proposed_verdict=None, reasoning=None),

    people=["PER-ROWBOTHAM", "PER-PTOLEMY", "PER-DUBAY"],
    related=["A03", "A04", "A22", "A26", "B08", "D11"],

    sources=[
        dict(label="Rowbotham (as “Parallax”), Zetetic Astronomy: Earth Not a Globe, 3rd ed. 1881 — ch. III, pp. 82–87, the parallax passage quoted above",
             url="https://sacred-texts.com/earth/za/za21.htm"),
        dict(label="Rowbotham, Zetetic astronomy: Earth not a globe!, 1865 first book edition (Project Gutenberg #69892) — SECTION II contains no astronomical use of the word “parallax”",
             url="https://www.gutenberg.org/ebooks/69892"),
        dict(label="Schadewald, The Plane Truth, ch. 1 — Rowbotham “had abandoned the pseudonym S. Goulden and begun calling himself ‘Parallax’” by the end of 1849",
             url="https://www.cantab.net/users/michael.behrend/ebooks/PlaneTruth/pages/Chapter_01.html"),
        dict(label="Bessel, “On the parallax of 61 Cygni”, MNRAS 4:152 (1838)",
             url="https://ui.adsabs.harvard.edu/abs/1838MNRAS...4..152B/abstract"),
        dict(label="MacTutor biography of Bessel — the 0.314″ result and Herschel’s “greatest and most glorious triumph which practical astronomy has ever witnessed”",
             url="https://mathshistory.st-andrews.ac.uk/Biographies/Bessel/"),
        dict(label="ESA, “A history of astrometry, Part II” — Struve’s Vega 0.125″ (1837) revised to 0.261″ (1840) against a modern 0.130″; Henderson’s one arcsecond for α Centauri",
             url="https://sci.esa.int/web/gaia/-/53197-seeing-and-measuring-farther"),
        dict(label="ESA Gaia DR3 — 1,467,744,818 sources with five- or six-parameter astrometry; “median parallax uncertainties are 0.02-0.03 mas for G<15, 0.07 mas at G=17, 0.5 mas at G=20”",
             url="https://www.cosmos.esa.int/web/gaia/dr3"),
        dict(label="61 Cygni — Gaia DR3 parallaxes 285.9949 ± 0.0599 mas (A) and 286.0054 ± 0.0289 mas (B); 11.404 light years; Bessel’s 1838 centre value 313.6 ± 13.6 mas",
             url="https://en.wikipedia.org/wiki/61_Cygni"),
        dict(label="Proxima Centauri — Gaia DR3 parallax 768.0665 ± 0.0499 mas, 4.2465 light years, proper motion 3.85″/yr",
             url="https://en.wikipedia.org/wiki/Proxima_Centauri"),
        dict(label="Barnard’s Star — proper motion 10.3″/yr (Barnard 1916), Gaia DR3 parallax 546.9759 ± 0.0401 mas, 5.9629 light years",
             url="https://en.wikipedia.org/wiki/Barnard%27s_Star"),
        dict(label="Graney & Grayson, “On the telescopic disks of stars: a review and analysis of stellar observations from the early 17th through the middle 19th centuries” — Galileo, Hevelius and Cassini’s 4–6″ stellar “disks”, and Airy’s 1835 diffraction explanation",
             url="https://www.arxiv.org/pdf/1003.4918"),
        dict(label="Graney, “Science Against Copernicus in the Age of Galileo” (Church Life Journal) — Ingoli, after Tycho: heliocentrism requires “the fixed stars to be of such size, as they may surpass or equal the size of the orbit circle of the Earth itself”",
             url="https://churchlifejournal.nd.edu/articles/science-against-copernicus-in-the-age-of-galileo/"),
        dict(label="ESO, “The Biggest Star in the Sky” — R Doradus, angular diameter 0.057 ± 0.005 arcsec, the largest measured for any star but the Sun",
             url="https://www.eso.org/public/italy/news/eso9706/"),
        dict(label="Melis et al., “A VLBI resolution of the Pleiades distance controversy”, Science 345:1029 (2014) — 136.2 ± 1.2 pc against Hipparcos’s ~120 pc",
             url="https://www.science.org/doi/10.1126/science.1256101"),
        dict(label="Abramson, “The Distance to the Pleiades According to Gaia DR2” — 136.67 ± 0.04 pc from 1,595 stars, parallax 7.317 ± 0.002 mas",
             url="https://ar5iv.labs.arxiv.org/html/1808.02968"),
        dict(label="Lindegren et al., “Gaia Early Data Release 3: Parallax bias versus magnitude, colour, and position”, A&A 649:A4 (2021) — quasar parallaxes “systematically offset from the expected distribution around zero, by a few tens of microarcsec”",
             url="https://arxiv.org/abs/2012.01742"),
        dict(label="Rebuttals to Dubay, 200 Proofs — proof 19, “not a single inch of parallax can be detected in the stars, proving we have not moved at all”",
             url="https://flatearth.ws/eric-dubay"),
        dict(label="Stellar parallax — the history of failed attempts: Hooke 1674, Bradley 1729, Calandrelli’s 4″ for Vega, Brinkley’s 1″ in 1810",
             url="https://en.wikipedia.org/wiki/Stellar_parallax")]),
}
