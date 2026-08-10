# -*- coding: utf-8 -*-
"""Batch 9 — E12. "Redshift symmetry concentric around Earth." / "Redshift quantization
concentric." (items 60, 355)

Research notes for whoever picks this up next.

1. THE WORK RECORD. clusters.py credits E12 to Gerardus Bouw, `Geocentricity`, 1992.
   That attribution was not confirmed from here and the text quoted below is not Bouw's.
   What was found instead, and what this entry rests on:
     * The item's exact vocabulary is Sungenis & Bennett's. Volume I, chapter 3 of
       `Galileo Was Wrong` carries a section headed "Galaxies: Spheres of Stars Centered
       Around the Earth" (the contents page calls it "Galaxies: Spheres of Stars around
       the Earth as Center") and the sentence "quantized and spherical distribution of
       the heavenly bodies centered on the Earth". Items 60 and 355 are that sentence
       with the verbs removed.
     * The DERIVATION the section compresses is D. Russell Humphreys', "Our galaxy is
       the centre of the universe, 'quantized' redshifts show", TJ (Journal of Creation)
       16(2):95-104, 2002. Humphreys supplies the geometry, the arithmetic and the
       one-in-a-trillion probability, and chapter 3 reproduces both: his Figure 8 at
       printed p. 431 (the two panels "Viewed from centre" / "2 million light-years
       from centre") and, at p. 432, his eq. (15) probability calculation block-quoted
       from "one cosmologist" with only the footnote naming him. An earlier picture at
       p. 296 is captioned "courtesy of R. Humphrey's article" (sic). The title is
       located at printed pp. 284, 296, 398, 432, 580, 631 and 694 of the OCR searched
       (note 7) - seven times, not the "twice" an earlier draft of this note said.
       Humphreys is NOT a geocentrist and says so on
       p. 100, in a sentence whose footnote 35 cites Bouw's `Geocentricity` (1992) as
       the geocentrism he is distinguishing himself from. Humphreys has no PER-* record,
       so he is named in prose and left out of `people`; do not invent an id for him.
     * Bouw does carry the argument, but the documented instance is later than 1992. The
       annotated index of `Geocentricity: Christianity in the Woodshed`, printed in
       Biblical Astronomer no. 143 (vol. 23), lists ch. 36 "Lesser Evidences", p. 533, as
       covering "distributions centered on the earth; ... quasar distribution; Tifft's
       phenomenon". The same issue announces that book as newly available; its ch. 37 is
       "The Axis of Evil", which dates the contents after 2005. The 1992 printing itself
       was not reachable from here.
   clusters.py was NOT touched. Reported up: originator/originator_work/year, the
   `real_source` line, AND the cluster `note` (see note 5). The `note` matters as much as
   the rest: build.py renders it as the basis line beside the verdict chip, where it is
   read by people who never open the entry, and the E12 note as it stands - "Quantization
   disappeared as sample sizes grew; the effect was an artefact of small, sparse redshift
   samples" - is refused twice over by section IV below. Proposed basis: "The periodicity
   survives only in frames defined by the Earth's motion, and the shell reading fails its
   own author's blurring criterion by a factor of eight; large-sample tests reduce it to
   ~2 sigma rather than eliminating it." Proposed real_source: "Tifft 1972-1984; Napier &
   Guthrie 1997 (galactocentric); Humphreys TJ 16(2), 2002." Anchor any edit on the
   cluster key "E12", never on the originator= line.

2. THE HEDGE CHECK CAME BACK CLEAN, AND THAT IS THE FINDING. Held against Sungenis &
   Bennett, the two list items say what the book says at the strength the book says it —
   `drift_type="none"`, like R02. The compression loss is one link upstream and it is
   large: Tifft's own reading of his pattern (a property imprinted on the redshift,
   quoted in the book two pages later and there called "ad hoc") becomes a map of space,
   and Humphreys' galactocentric conclusion, with its explicit disclaimer of geocentrism,
   becomes an Earth-centred one. Both conversions are made in the open, on the page,
   with the original wording printed alongside. Blaming the list for this cluster would
   be blaming the wrong link.

3. THE PHYSICS HINGE IS THE FRAME, AND IT IS INTERNAL. Napier & Guthrie's own abstract
   says the distribution is quantized "in the galactocentric frame of reference". Bajan
   et al.'s review states it flatly: "The periodicity was observed only in the case of
   galactocentric radial velocities or using CMB reference frame, not in the case of
   heliocentric radial velocity", and of Guthrie & Napier's 37.2 km/s result, "this
   periodicity appeared only if galactocentric redshifts were considered". So the signal
   requires an observer moving at 29.79 km/s about the Sun and ~240 km/s about the
   Galactic centre — Humphreys' own footnote 28 supplies both numbers. Sungenis notices
   and objects to it in as many words. A geostatic cosmology cannot spend this datum.

4. SECOND HINGE: THE SHELLS FAIL HUMPHREYS' OWN CRITERION. His eq. (13) says the groups
   blur when the scatter sigma exceeds the spacing delta-r. Peculiar velocity enters the
   INFERRED distance directly through his own eq. (5). Arithmetic recomputed here with
   his H = 75 km/s/Mpc and 1 Mpc = 3.2616 Mly, which reproduces his published 1.6 and
   3.1 Mly exactly:
       37.5 km/s -> 0.500 Mpc = 1.63 Mly      71.5 km/s -> 0.953 Mpc = 3.11 Mly
      300   km/s -> 4.000 Mpc = 13.05 Mly  = 8.0 x the 1.63 Mly spacing
      638   km/s -> 8.507 Mpc = 27.75 Mly  = 8.9 x the 3.11 Mly spacing
   638 km/s is the Virgo cluster's measured radial velocity dispersion (Kashibadze,
   Karachentsev & Karachentseva, A&A 635:A135, 2020, which also gives d = 16.5 Mpc and a
   virial radius of 1.7 Mpc = 5.5 Mly). His footnote 18 answers a DIFFERENT objection —
   how far a 300 km/s galaxy would travel in a billion years — but a redshift records the
   velocity, not the journey, so the smearing is instantaneous. Keep this separate from
   the statistics argument; it holds even if every periodicity claim is granted.

5. ON THE STATISTICS, BE MORE CAREFUL THAN OUR BASIS LINE IS. The 2dF paper everyone
   cites (Hawkins, Maddox & Merrifield, MNRAS 336:L13, 2002) tested the QSO/log(1+z)
   periodicity on 1647 galaxy-quasar pairs — the Burbidge-Karlsson claim, NOT Tifft's
   37.5 km/s galaxy comb. The largest published test of the galaxy comb found here is
   Bajan, Flin, Godlowski & Pervushin, Phys. Part. Nucl. Lett. 4(1):5-11 (2007): 2522
   Hercules Supercluster galaxies, peaks near 73 and 24 km/s surviving only at 2 sigma,
   conclusion "the existence of redshift periodicity among galaxies is not well
   established". That is weaker than "disappeared". Say 2 sigma out loud; a defender who
   knows the paper will otherwise use our overstatement.

6. SCALE DISCIPLINE. Sungenis's "evenly spaced layers ... seven north, seven south" is
   the deep pencil-beam survey of Broadhurst, Ellis, Koo & Szalay (Nature 343:726, 1990)
   — Koo is the "D. Koo" of the citation; "R. Krone" is Richard Kron. That periodicity is
   ~128 h^-1 Mpc, i.e. ~12,800 km/s, roughly 340 times the 37.5 km/s comb. Large-scale
   quasi-periodicity is a live topic (Yoshida et al. 2001 could not reproduce Broadhurst
   at better than ~1 in 10^3 in CDM; Ryabinkov & Kaminker, MNRAS 527:1813, 2023, report
   4-5 sigma structure at ~116 h^-1 Mpc in 176,962 SDSS DR12 LOWZ galaxies) and the page
   says so. It is anisotropic, which is the opposite of concentric, and it is a different
   phenomenon from the one this cluster rests on. Do not merge them.

7. QUOTE PROVENANCE. All Sungenis quotations are from the OCR text of the Internet
   Archive item `galileo-was-wrong-the-church-was-right-sungenis-vol-1-3-complete`
   (5,499,250 bytes, 134,983 lines), whose front matter reads "Seventh edition / Volume 1
   / ... Catholic Apologetics International Publishing, Inc., 2013 / Copyright (c) 2013",
   and adds that the previous five editions were in two volumes and published 2005-2010.
   Printed page numbers 417-420 are the page markers in that OCR; none of it has been
   checked against a print copy and the locator says so. Humphreys quotations are from
   the creation.com PDF of TJ 16(2), page numbers as printed in that PDF.
   One loose end left loose: Sungenis cites the Sky & Telescope news item as 84:128,
   August 1992; Humphreys cites what is evidently the same item as 84(2):28-29. The
   magazine was not consulted, so neither pagination is endorsed here.
"""

ENTRY = {

"E12": dict(

    tldr=("The redshift pattern this argument rests on exists only in a reference frame in "
          "which the Earth is moving. Tifft's ~72 km/s and Guthrie and Napier's ~37.5 km/s "
          "periodicities are reported in galactocentric or microwave-background redshifts, so "
          "producing the signal means first subtracting the Earth's 29.79 km/s orbit and the "
          "Sun's ~240 km/s circuit of the Galaxy — both numbers taken from the paper the "
          "geocentric version is built on. And it fails that paper's own test: galaxies' "
          "random motions of a few hundred km/s smear any distance inferred from a redshift by "
          "about eight shell spacings, which is why Tifft, who found the pattern, read it as a "
          "property of redshift rather than as a map."),

    passage=dict(
        work="WRK-SUNGENIS-2006",
        pd=False,
        locator=("Vol. I, ch. 3, under the section heading “Galaxies: Spheres of Stars Centered "
                 "Around the Earth”; printed p. 417 as paginated in the OCR of the Internet "
                 "Archive item galileo-was-wrong-the-church-was-right-sungenis-vol-1-3-complete, "
                 "whose front matter reads seventh edition, Volume 1, 2013. Not checked against "
                 "a print copy"),
        quote=("The above astronomers are not the only ones to discover such quantized and "
               "spherical distribution of the heavenly bodies centered on the Earth. In 1970, "
               "William G. Tifft … found that they were all distributed at specific spherical "
               "distances from Earth, namely, in multiples of 72 km/sec, and a smaller grouping "
               "of 36 km/sec."),
        gloss="""<p><strong>Two conversions happen in this sentence, and the book performs both of them in the open.</strong> The first is from a statement about redshifts to a statement about positions: Tifft measured the distribution of redshift <em>values</em>, and the sentence reports it as galaxies &ldquo;distributed at specific spherical distances from Earth&rdquo;. The second is the word <em>Earth</em>, which is not in the astronomy being cited.</p>

<p><strong>What Tifft made of his own pattern is printed two pages later in the same chapter.</strong> Sungenis and Bennett quote him &mdash; the redshift &ldquo;has imprinted on it a pattern that appears to have its origin in microscopic quantum physics&rdquo; &mdash; and then call that reading &ldquo;the ad hoc idea that something was &lsquo;imprinted&rsquo; on the light&rdquo;, adding that Tifft &ldquo;couldn&rsquo;t quite come to embrace his own results&rdquo;. Nothing is concealed. The author of the data is given his sentence and overruled, and the overruling is the argument. (The date is also loose: the Tifft quantization papers in Bajan et al.&rsquo;s bibliography begin in 1972, and the paper Sungenis&rsquo;s own footnote quotes is Tifft &amp; Cocke 1984.)</p>

<p><strong>The derivation being compressed belongs to someone who rejects the conclusion.</strong> The geometry, the arithmetic and the one-in-a-trillion probability all come from D. Russell Humphreys, &ldquo;Our galaxy is the centre of the universe, &lsquo;quantized&rsquo; redshifts show&rdquo;, <em>TJ</em> 16(2):95&ndash;104 (2002), and the borrowing is on the page rather than inferred. In the Internet Archive OCR used here the title appears seven times &mdash; printed pp. 284, 296, 398, 432, 580, 631 and 694 &mdash; and chapter 3 prints his working twice: his Figure 8 at p. 431, the two panels labelled &ldquo;Viewed from centre&rdquo; and &ldquo;2 million light-years from centre&rdquo;, and overleaf at p. 432 the probability calculation itself, <em>&delta;r</em>&nbsp;=&nbsp;1.6 million light years against a cosmos of radius &ldquo;about 20 billion light years&rdquo;, giving odds &ldquo;less than one out of a trillion&rdquo; &mdash; block-quoted from &ldquo;one cosmologist&rdquo;, with only the footnote naming which one. (A picture at p. 296 is likewise captioned &ldquo;courtesy of&rdquo; the same article.) Humphreys&rsquo; p. 100 states the difference himself: our galaxy is &ldquo;essentially at the centre of the cosmos, but not at rest with respect to it&rdquo;, which &ldquo;differs from geocentrism, which would have the Earth be at the exact centre and motionless with respect to it&rdquo;. Sungenis&rsquo;s own footnote records the same thing, noting that Humphreys and Gentry &ldquo;posit that the Earth has diurnal and translational motion&rdquo;. So the Earth-centred version is made with the distinction in view, not in ignorance of it.</p>

<p><strong>On the geocentrist literature more broadly.</strong> The annotated index of Bouw&rsquo;s <em>Geocentricity: Christianity in the Woodshed</em>, printed in <em>Biblical Astronomer</em> no. 143, lists &ldquo;Tifft&rsquo;s phenomenon&rdquo; and &ldquo;distributions centered on the earth&rdquo; among the contents of ch. 36, p. 533; the same issue announces that book as newly available, and its ch. 37 on the CMB &ldquo;axis of evil&rdquo; places the contents after 2005. The 1992 printing of <em>Geocentricity</em> was not reachable from here, and no claim is made here about what is in it.</p>"""),

    steelman=dict(
        description="""<p><strong>SURFACE (weak &mdash; do not use).</strong> &ldquo;Redshift quantization was never real; Tifft was a crank.&rdquo; This loses the exchange. Tifft published in the <em>Astrophysical Journal</em> for two decades; Guthrie and Napier reported the effect independently, in <em>MNRAS</em> and <em>A&amp;A</em>, and on the account <em>Galileo Was Wrong</em> quotes from Robert Matthews in <em>Science</em>, a referee required them to repeat the analysis on a fresh set of galaxies before publication &mdash; which they did, and the same figure came out. Anyone who opens with &ldquo;this was never in the literature&rdquo; will be shown the literature.</p>

<p><strong>DEEPER.</strong> The large-sample tests have weakened it. Bajan, Flin, God&#322;owski and Pervushin ran a power-spectrum analysis over 2522 Hercules Supercluster galaxies rather than a hand-picked subsample and found peaks near 73 and 24 km/s surviving only at the 2&sigma; level, concluding that &ldquo;the existence of redshift periodicity among galaxies is not well established&rdquo;. True, and incomplete: it concedes a residual and invites the reply that a bigger database might yet bring it back &mdash; which is exactly what those authors say they expect to settle the question.</p>

<p><strong>KERNEL.</strong> The strongest thing here is Humphreys&rsquo; geometry, and it is correct. If galaxies sit on concentric shells and redshift tracks distance, then an observer displaced from the centre by <em>a</em> sees each shell&rsquo;s radius vary between <em>r</em>&nbsp;&minus;&nbsp;<em>a</em> and <em>r</em>&nbsp;+&nbsp;<em>a</em>; the angular term contributes a standard deviation <em>a</em>/&radic;2 (his eq. 12), it adds in quadrature with the shell&rsquo;s own thickness (eq. 13), and the pattern washes out once the total exceeds the spacing. So a <em>sharp</em> radial comb really would imply that the observer is near the centre of the pattern, and the bound really would be the size of one spacing rather than the size of the universe. That is a genuine, non-obvious constraint, correctly derived by a physicist, and most people trying to bust it will get it wrong. Concede all of it.</p>""",
        why_it_doesnt_save_claim="""<p>Because the same equation, fed the numbers, deletes the shells &mdash; and the term that does it is one Humphreys names and then measures the wrong quantity for.</p>

<p>His eq. (5) converts a redshift into a distance by dividing by <em>H</em>. Anything that moves a galaxy&rsquo;s redshift therefore moves its inferred distance, and a peculiar velocity does that directly. Take his own working values, <em>H</em>&nbsp;=&nbsp;75&nbsp;km/s/Mpc and 1&nbsp;Mpc&nbsp;=&nbsp;3.2616&nbsp;million light years, which reproduce his published spacings of 1.6 and 3.1&nbsp;Mly exactly. A typical peculiar velocity of 300&nbsp;km/s displaces the inferred distance by 13.05&nbsp;Mly &mdash; <strong>8.0 times</strong> the 1.63&nbsp;Mly spacing his 37.5&nbsp;km/s interval implies. In the Virgo cluster, where Guthrie and Napier put their 71&nbsp;km/s periodicity, the measured radial velocity dispersion is 638&nbsp;&plusmn;&nbsp;35&nbsp;km/s (Kashibadze, Karachentsev &amp; Karachentseva, <em>A&amp;A</em> 635:A135, 2020), which is 27.75&nbsp;Mly of spurious depth against a 3.11&nbsp;Mly spacing &mdash; <strong>8.9 times</strong> &mdash; imposed on a bound cluster whose virial radius is 1.7&nbsp;Mpc, about 5.5&nbsp;Mly. By his eq. (13) and the sentence after it, that is not a faint blurring; his own Figure&nbsp;8 shows what a factor this size does to a comb.</p>

<p><strong>He does answer the objection, and the answer is to a different question.</strong> His footnote 18 reasons that a galaxy moving 300&nbsp;km/s &ldquo;would have to move in a straight line for a billion years to move 1 million light-years from its original location&rdquo;. That is about <em>displacement over time</em>. A redshift does not record where a galaxy has travelled; it records how fast it is going now, and the 300&nbsp;km/s enters the inferred distance the instant the spectrum is taken, whether the galaxy has been moving for a billion years or a day.</p>

<p>Which is precisely why the man who found the pattern did not read it as a map. A pattern that survives contamination eight times its own width cannot be a pattern in distance; it has to be a pattern in the redshift itself. Tifft said so. The geometry is right, and its conclusion is that the shells are not there to be centred on anybody.</p>"""),

    refutation="""<p>Four things have to be kept apart: what was measured, what frame it was measured in, what the measurement would have to mean to support the item, and what the sky actually looks like when it is mapped. The argument depends on running the first two together and skipping the third.</p>

<h4>I. What was measured, at full strength</h4>

<p>William Tifft, at Steward Observatory, reported from the early 1970s that galaxy redshifts cluster at preferred values with a spacing near 72&nbsp;km/s, later also 36&nbsp;km/s; with W. J. Cocke he wrote in <em>ApJ</em> 287:492 (1984) that there was &ldquo;very firm evidence that the redshifts of galaxies are quantized with a primary interval near 72 km s<sup>&minus;1</sup>&rdquo;. Bruce Guthrie and William Napier reported the effect independently through the 1990s, and their 1997 status report in the <em>Journal of Astrophysics and Astronomy</em> concluded for &ldquo;galactocentric periodicities of 37.5 km s<sup>&minus;1</sup> in field galaxies and loose groupings, and 71.1 km s<sup>&minus;1</sup> in the environment of dense clusters&rdquo;. These are real papers in real journals, and the episode the geocentric literature presents as drama &mdash; a referee, on the account <em>Galileo Was Wrong</em> quotes from <em>Science</em>, sending Guthrie and Napier back to repeat the analysis on a fresh set of galaxies &mdash; is peer review doing its job. This page disputes neither that the analyses were performed nor that the peaks appeared in the samples analysed.</p>

<h4>II. The frame &mdash; and this is the whole argument</h4>

<p>The periodicity is not a property of the numbers that come off the telescope. It is a property of those numbers after a velocity has been subtracted from them. Napier and Guthrie&rsquo;s own abstract locates the effect &ldquo;in the galactocentric frame of reference&rdquo;. Bajan and colleagues, reviewing the whole literature, put it without ornament: <em>&ldquo;The periodicity was observed only in the case of galactocentric radial velocities or using CMB reference frame, not in the case of heliocentric radial velocity&rdquo;</em>, and of Guthrie and Napier&rsquo;s 37.2&nbsp;km/s result, <em>&ldquo;this periodicity appeared only if galactocentric redshifts were considered&rdquo;</em>. Tifft&rsquo;s own later refinement went further in the same direction, moving to the frame in which the microwave background is isotropic.</p>

<p>Now put the corrections beside the signal, using the numbers Humphreys tabulates in his own footnote 28. The Earth&rsquo;s orbital speed is 29.79&nbsp;km/s &mdash; 0.79 of one 37.5&nbsp;km/s interval, so the annual swing in an uncorrected redshift is about 1.6 intervals. The Sun&rsquo;s velocity with respect to the Galactic centre is 240&nbsp;km/s, six and a half intervals. The Galaxy&rsquo;s velocity with respect to the microwave background is 556&nbsp;km/s, about fifteen. <strong>To make the comb appear you must first place the observer on a body moving at the first two of those speeds and take them out &mdash; and in the cosmic-background-rest-frame analyses, at all three.</strong> On a stationary central Earth there is nothing to subtract, and the quantity that would carry the pattern is the raw telescope-frame redshift.</p>

<p>Sungenis and Bennett see this and object to it directly, writing that Tifft &ldquo;deliberately ignores the rest frame upon which his telescope is seated, namely, Earth&rdquo; and &ldquo;arbitrarily chooses&rdquo; the microwave background instead. That is an accurate description of the situation and it is fatal to the item rather than to Tifft. The choice of frame is not arbitrary: it is the frame in which the signal is present. A geostatic cosmology is being asked to accept, as its evidence, a pattern that its own preferred frame does not display.</p>

<p><strong>The book has a printed answer to this, and it is the best thing in the whole cluster, so it gets quoted here rather than skirted.</strong> Volume II, chapter 10 &mdash; printed p. 298 of the same scan &mdash; concedes the frame problem and then turns it round: the subtraction <em>&ldquo;is only done for the first two motions &mdash; the orbit around the sun and the solar motion around the galaxy center, the galactocentric frame of reference! The Milky Way motion and the motion towards Leo &hellip; represent the largest component of the Earth&rsquo;s motion &mdash; about 600 km/s! &hellip; Unless, of course, the motions of the Earth are fictitious!&rdquo;</em> The premise is correct, which is why the &ldquo;first two&rdquo; above is stated carefully. The inference is not, and the counter-example is printed in the same book, one volume earlier. The footnote on p. 417 lists Tifft&rsquo;s papers on periodicity in the cosmic background rest frame &mdash; the book&rsquo;s own citation gives &ldquo;Global Redshift Periodicities: Association with the Cosmic Background Radiation&rdquo;, <em>Astrophysics and Space Science</em> 239:35 (1996), and &ldquo;Evidence for Quantized and Variable Redshifts in the CBR Rest Frame&rdquo; &mdash; and the Tifft passage block-quoted on p. 418 says the quantization is most obvious &ldquo;when viewed from an appropriate rest frame, especially the cosmic background rest frame&rdquo;. That is the frame in which the whole ~600 km/s <em>has</em> been taken out. Bajan and colleagues record the same pair of options and no third: galactocentric velocities <em>or</em> the CMB frame, never the heliocentric one.</p>

<p>So the reply does not survive the book&rsquo;s own pages. The periodicity is reported after two subtractions and after three; the one frame in which the reviews consulted here record its absence is the heliocentric one, which is already a subtraction along from what the telescope delivers. A geostatic cosmology has to call those subtractions fictitious in one breath and spend, in the next, a result that exists only once they have been made. The p. 298 argument is a reductio, and it stands or falls on one factual premise &mdash; that the comb shows up with the largest motion left in. Take the premise seriously and the analyses in the CBR rest frame are precisely where it fails: there the largest motion is not left in, and the peaks are still reported. The reductio has no absurdity to point at.</p>

<h4>III. What the pattern would have to be, to be shells</h4>

<p>This is argued in full in the steelman above and only the result is repeated here, because it is the load-bearing number. Converting a redshift to a distance divides by <em>H</em>, so peculiar velocities land in the inferred distance one for one. At Humphreys&rsquo; own <em>H</em>&nbsp;=&nbsp;75&nbsp;km/s/Mpc, an ordinary 300&nbsp;km/s peculiar velocity is 13.05&nbsp;million light years of false depth against a 1.63&nbsp;Mly shell spacing, and the Virgo cluster&rsquo;s measured 638&nbsp;km/s dispersion is 27.75&nbsp;Mly against a 3.11&nbsp;Mly spacing. Humphreys&rsquo; own criterion &mdash; the groups become indistinguishable once the scatter exceeds the spacing &mdash; is exceeded by a factor of eight or nine. His footnote 18 answers a question about how far galaxies travel rather than how fast they are going.</p>

<p>Those dispersions are not inferred from the model under dispute. They are the &ldquo;fingers of God&rdquo;: clusters that are compact on the sky and stretched along the line of sight in every redshift map ever made, in every direction, which is what a bound object with random internal motions looks like when its redshifts are plotted as distances. And the Virgo cluster&rsquo;s distance is fixed independently of redshift altogether, at 16.5&nbsp;Mpc, by surface-brightness fluctuations on its member galaxies.</p>

<h4>IV. What the statistics now say, stated at the strength the papers support</h4>

<p>Two corrections to the way this is usually reported, one in each direction.</p>

<p>The 2dF result that is normally cited against quantization &mdash; Hawkins, Maddox and Merrifield, <em>MNRAS</em> 336:L13 (2002), &ldquo;no evidence for a periodicity at the predicted frequency in log(1&nbsp;+&nbsp;<em>z</em>), or at any other frequency&rdquo;, with the earlier signal attributed to &ldquo;the combination of noise and the effects of the window function&rdquo; &mdash; was a test of the quasar periodicity in log(1&nbsp;+&nbsp;<em>z</em>) across 1647 galaxy&ndash;quasar pairs. That is the Burbidge&ndash;Karlsson claim, not Tifft&rsquo;s 37.5&nbsp;km/s comb, and using it as though it settled this cluster is sloppy.</p>

<p>The test that does bear directly is Bajan, Flin, God&#322;owski and Pervushin, <em>Physics of Particles and Nuclei Letters</em> 4(1):5&ndash;11 (2007). They took 2522 Hercules Supercluster galaxies &mdash; the whole structure, not the subsample with the best measurements &mdash; and found peaks near 73 and 24&nbsp;km/s at the 2&sigma; level. Their diagnosis of the earlier high significances is the ordinary one: <em>&ldquo;in all these investigations from database containing thousands of galaxies only a small number of them, namely, those with very accurate measurements, were taken into account&rdquo;</em>, and their conclusion is <em>&ldquo;In our opinion, the existence of redshift periodicity among galaxies is not well established&rdquo;</em>. <strong>Two sigma is not nothing and this page will not call it nothing.</strong> It is a long way below what the argument needs, and it is a long way below what Tifft and Napier and Guthrie reported; but the honest statement is that the effect shrank drastically when the selection was removed, not that it vanished.</p>

<h4>V. The map that shows the Earth in the middle</h4>

<p>The same chapter offers the Sloan Digital Sky Survey wedge diagram, with rings drawn on it, as independent confirmation: the picture &ldquo;shows Earth in the center of two wedge-shaped galaxy segments that also show galaxy density decreases as the distance from Earth increases&rdquo;. Both features are properties of the plot, not of the sky. A wedge diagram places each galaxy at its right ascension and its redshift, with the observer at the apex &mdash; the observer is at the origin the way a radar operator is at the centre of a radar screen, because that is the coordinate system. And the thinning with distance is the survey&rsquo;s flux limit: SDSS&rsquo;s main galaxy sample is cut at Petrosian <em>r</em>&nbsp;&lt;&nbsp;17.77&nbsp;mag, so the number of galaxies bright enough to make the catalogue falls with distance by construction. A survey that reached to a fixed distance in every direction and detected everything would produce neither feature.</p>

<p>The &ldquo;evenly spaced layers, seven north and seven south&rdquo; attributed in the same passage to Koo and &ldquo;Krone&rdquo; is a different result again: the deep pencil-beam survey of Broadhurst, Ellis, Koo and Szalay, <em>Nature</em> 343:726 (1990), whose spacing is about 128&nbsp;<em>h</em><sup>&minus;1</sup>&nbsp;Mpc &mdash; roughly 12,800&nbsp;km/s in redshift, some 340 times the interval this cluster is about. Stacking it onto Tifft&rsquo;s comb as one phenomenon is a scale error of two and a half orders of magnitude.</p>

<h4>VI. The part that is genuinely open, said plainly</h4>

<p>Large-scale quasi-periodicity in the galaxy distribution is a live question and this page is not going to pretend otherwise. Yoshida and collaborators built mock pencil-beam surveys from large N-body simulations and concluded that the regularity Broadhurst et al. found &ldquo;has a priori probability well below 10<sup>&minus;3</sup>&rdquo; in standard cold dark matter cosmologies &mdash; that is a result <em>against</em> the easy dismissal. More recently Ryabinkov and Kaminker (<em>MNRAS</em> 527:1813, 2023) analysed 176,962 SDSS DR12 LOWZ galaxies and reported a characteristic scale of 116&nbsp;&plusmn;&nbsp;10&nbsp;<em>h</em><sup>&minus;1</sup>&nbsp;Mpc with peak significances of 4&ndash;5&sigma; along some directions.</p>

<p>Two things follow, and neither helps the item. First, that structure is reported as <em>anisotropic</em> &mdash; direction-dependent &mdash; and a set of spheres centred on the observer is by definition the same in every direction. Second, a preferred separation of roughly that size is the one thing standard cosmology positively predicts: the baryon acoustic scale, detected as a bump in the correlation function of 46,748 SDSS luminous red galaxies over 3816 square degrees at a separation near 100&nbsp;<em>h</em><sup>&minus;1</sup>&nbsp;Mpc (Eisenstein et al., <em>ApJ</em> 633:560, 2005). Notice what that is. It is a statement about <em>pairs</em>: every galaxy has a slight excess of companions at that separation, so the universe really is threaded with a preferred spherical shell radius &mdash; one centred on the Milky Way, and equally on every other galaxy in the catalogue, which is why it singles out nobody. The related items in this family are worked at <a href="#ARG-E13">ARG-E13</a>.</p>

<h4>VII. Granting everything, the argument still cannot deliver the item</h4>

<p>Suppose the comb is real and spatial. The bound it yields is the one Humphreys derived: the observer lies within one spacing of the centre, which he gives as 1.6 million light years, or on the tightest interval he will use, about 100,000 light years &mdash; the diameter of our galaxy. At that resolution the Earth, the Sun and the Galactic centre are the same point, and no version of this argument can prefer one over another. That is why its author calls the result galactocentric and writes that it &ldquo;differs from geocentrism&rdquo;.</p>

<p>And the difference that matters is not location but motion. On his own reasoning &mdash; the microwave-background frame being &ldquo;presumably at rest with respect to the universe as a whole&rdquo; &mdash; the centre Humphreys derives is one our galaxy is <em>moving with respect to</em>, at the 556&nbsp;km/s he tabulates; the frame corrections that produce the signal in the first place presuppose an Earth orbiting a Sun that orbits a Galaxy. The list places items 60 and 355 among items asserting that the Earth does not move. This argument, run at full strength and granted every disputed premise, returns a centre that is roughly where we are and a us that is travelling away from it at half a thousand kilometres a second.</p>

<p><strong>Verdict: refuted.</strong> The periodicity did not survive at anything like its claimed significance once the samples stopped being hand-picked; the spatial reading fails its own author&rsquo;s criterion by a factor of eight; and the signal, where it is reported at all, lives in frames defined by the Earth&rsquo;s motion.</p>""",

    advocate=dict(
        best_defense=(
            "Four moves, and take the third and fourth seriously. First, your peculiar-velocity "
            "argument is circular. Peculiar velocities are not measured; they are what is left "
            "over after you subtract a Hubble flow from a redshift using distance indicators "
            "calibrated on the expanding-universe model you are defending. You have assumed the "
            "conclusion and called the residue an observation. Second, look at what you conceded "
            "in section VI. You told the reader that Yoshida could not reproduce Broadhurst's "
            "regularity in cold dark matter at better than one in a thousand, that Ryabinkov and "
            "Kaminker get four to five sigma for a periodic structure in 176,000 galaxies, and "
            "that the universe genuinely does have a preferred spherical shell radius. Your "
            "answer to a concentric-shell cosmology is a concentric-shell cosmology with the "
            "centre relabelled. Third, and this is the one you cannot wave away: you spent five "
            "hundred words establishing that Humphreys is a galactocentrist rather than a "
            "geocentrist. At the resolution of his own bound — a hundred thousand light years — "
            "that distinction does not exist. The Earth is inside the Milky Way. You have "
            "refuted a distinction nobody needed, and you have done it because the alternative "
            "was engaging the claim, which is that the cosmos has a centre and we are sitting "
            "at it. Fourth — and this one is in our book, in print, where you could have found "
            "it. Volume II, chapter 10, page 298 answers your frame section directly, and you "
            "do not mention it. The correction is only ever made for the first two motions, the "
            "orbit around the sun and the solar motion around the galactic centre. The Milky "
            "Way's own motion and the motion towards Leo — about 600 km/s, the largest "
            "component of the whole business — were not known then and were not taken out at "
            "all, and the quantum steps appear anyway, at intervals as low as 12 km/s. Either a "
            "600 km/s smearing that should obliterate a 12 km/s step somehow does not, or the "
            "motions of the Earth are fictitious. You quoted our objection to Tifft's choice of "
            "rest frame and left the reason for it on the page you did not turn to."),
        survives=4,
        preemptive=(
            "Four, driven by the first, third and fourth moves; the second is showy but "
            "answerable. Four concrete requirements on the text. (a) The circularity charge must be "
            "answered where the number is used, not later. Section III as written already does "
            "it — the fingers-of-God paragraph and the surface-brightness-fluctuation distance "
            "to Virgo are there precisely so that the 638 km/s is anchored to something no "
            "redshift-distance assumption produced — and that paragraph must stay adjacent to "
            "the arithmetic. If an editor ever moves it, the strongest section on the page "
            "becomes the most vulnerable one. (b) On the BAO reply, the answer is a distinction "
            "and it is in section VI: a correlation-function feature is a statement about pairs, "
            "so the shell exists around every galaxy at once and centres on none, and its scale "
            "is ~150 Mpc with a bump tens of Mpc wide, not a 0.5 Mpc comb. Keep the words "
            "'equally on every other galaxy in the catalogue' — deleting that clause loses the "
            "exchange. (c) On Earth-versus-Galaxy, concede the point immediately and openly, as "
            "section VII does: at 100,000 light years the distinction is unavailable, and the "
            "geocentric reading does not fail because it names the wrong point. It fails because "
            "the signal requires the Earth to be moving. Never rest weight on the Earth/Galaxy "
            "distinction as though it were the refutation; it is a scope finding about the list, "
            "and it belongs in the compression block, which is where it is. (d) The Volume II "
            "p. 298 objection must be quoted and answered inside section II, not left for the "
            "reader to discover; an unanswered printed rebuttal to the load-bearing section is "
            "the one thing that would sink the page. It is answered out of the book itself: the "
            "footnote at p. 417 lists Tifft's cosmic-background-rest-frame papers and the Tifft "
            "passage quoted at p. 418 puts the quantization in that frame, so the comb is "
            "reported both after two subtractions and after all three. Do NOT answer it by "
            "claiming the CMB correction is always applied — it is not, the galactocentric "
            "result is the one this cluster leads with, and section II said 'all three' once "
            "already and had to be corrected. Resist one further "
            "temptation: do not claim that redshift periodicity has been excluded outright. "
            "Bajan et al. report 2 sigma and say they expect a larger database to settle it, and "
            "a defender who knows that paper will use an overclaim to discredit the section."),
    ),

    straw_man=dict(
        identified=True,
        detail=("The section is built on attributed motive. Astronomers were reluctant to accept "
                "Tifft's findings, the book says, because they were “well aware of the dire "
                "implications it held against their cherished Big Bang theory”; Guthrie and "
                "Napier are said to have taken up the problem “with the express purpose of "
                "overturning Tifft's results”; and Tifft himself is described as “typical "
                "of modern scientists who often lock themselves into paradigms”, opting for an "
                "“ad hoc” idea rather than the face-value reading. Humphreys makes the "
                "same move more mildly: “I suggest that they are avoiding the obvious because "
                "galactocentricity brings into question their deepest worldviews.” But the "
                "reason for preferring an intrinsic reading is stated in the papers and is "
                "physical rather than ideological: the peaks are sharp — some of them, "
                "Humphreys notes, only a few km/s wide — and galaxies move at hundreds of "
                "km/s, so a pattern that survives at all cannot be a pattern in distance. Tifft "
                "gave that answer; the book prints it, and reads it as evasion."),
    ),

    compression=dict(
        assessed=True, drifted=False,
        list_phrasing=("Redshift symmetry concentric around Earth. / Redshift quantization "
                       "concentric. (items 60, 355)"),
        source_wording=("“Galaxies: Spheres of Stars Centered Around the Earth” (section heading); "
                        "“such quantized and spherical distribution of the heavenly bodies "
                        "centered on the Earth”; “distributed at specific spherical distances from "
                        "Earth, namely, in multiples of 72 km/sec”"),
        drift_type="none",
        note=("""<p><strong>Held against the book the items came from, these two are faithful, and if anything milder.</strong> The section heading in <em>Galileo Was Wrong</em> reads &ldquo;Galaxies: Spheres of Stars Centered Around the Earth&rdquo; and the sentence beneath it asserts a &ldquo;quantized and spherical distribution of the heavenly bodies centered on the Earth&rdquo;. Items 60 and 355 are that, with the nouns kept and the verbs dropped. The refutation above is aimed at the book&rsquo;s version, at the book&rsquo;s strength, and it would land no differently on the fragments.</p>

<p><strong>The compression loss on this cluster is real and it happened one link upstream, twice.</strong> Both instances are visible on the page, in the book itself, with the original wording printed alongside &mdash; which is what makes them documentable rather than alleged.</p>
<p><em>One: an interpretation is reversed.</em> Tifft measured a distribution of redshift <em>values</em> and read the pattern as a property of the redshift &mdash; it &ldquo;has imprinted on it a pattern that appears to have its origin in microscopic quantum physics&rdquo;. Chapter 3 reports his result as galaxies &ldquo;distributed at specific spherical distances from Earth&rdquo;, then quotes his sentence two pages later and calls it &ldquo;ad hoc&rdquo;. The astronomer&rsquo;s conclusion is not omitted; it is printed and overruled, and the overruling is the argument.</p>
<p><em>Two: a scope is widened from a galaxy to a planet.</em> The geometry, the arithmetic and the one-in-a-trillion figure are D. Russell Humphreys&rsquo;, from <em>TJ</em> 16(2):95&ndash;104 (2002), and chapter 3 reprints them &mdash; his Figure 8 at printed p. 431 and his probability calculation at p. 432, attributed in the body to &ldquo;one cosmologist&rdquo; and by name only in the footnote. His bound localises the centre to within 1.6 million light years, or on his tightest interval about 100,000 &mdash; the diameter of the Galaxy &mdash; and he writes that our galaxy is &ldquo;essentially at the centre of the cosmos, but not at rest with respect to it&rdquo;, which &ldquo;differs from geocentrism&rdquo;. <em>Galileo Was Wrong</em> records the same distinction in a footnote, noting that Humphreys and Gentry &ldquo;posit that the Earth has diurnal and translational motion&rdquo;, and then heads its own section &ldquo;Centered Around the Earth&rdquo;. An argument whose stated resolution is the width of a galaxy arrives on a proof list as a statement about a planet.</p>

<p><strong>Why record this as <code>none</code> rather than forcing it into a box.</strong> The seven drift types describe the step from a source to the list, and on that step nothing moved. Recording a drift here would put the loss at the wrong link and let the book off. The finding this cluster contributes to the review&rsquo;s thesis is the other one: a chain can degrade a claim without a single misquotation, because the degradation happens where one author reads another, in the open, with the disagreement printed. Compare <a href="#ARG-R02">ARG-R02</a>, where the same book compresses its sources the same way and the list again copies it faithfully.</p>"""),
    ),

    verdict_challenge=dict(challenged=False, proposed_verdict=None, reasoning=None),

    people=["PER-SUNGENIS", "PER-BOUW"],
    related=["E01", "E04", "E06", "E09", "E11", "E13", "E17"],

    sources=[
        dict(label="Sungenis & Bennett, Galileo Was Wrong: The Church Was Right — Internet "
                   "Archive OCR of the three-volume scan (front matter: seventh edition, "
                   "Volume 1, Catholic Apologetics International Publishing, 2013). Vol. I "
                   "ch. 3, pp. 417–420: “Galaxies: Spheres of Stars Centered Around the "
                   "Earth”, the Tifft quotation and the Sky & Telescope and Napier/Guthrie "
                   "material; pp. 410–412 for the quasar version; pp. 423–428 for the SDSS "
                   "wedge and the engagement with Hawkins et al.",
             url="https://archive.org/details/galileo-was-wrong-the-church-was-right-sungenis-vol-1-3-complete"),
        dict(label="D. Russell Humphreys, “Our galaxy is the centre of the universe, ‘quantized’ "
                   "redshifts show”, TJ (Journal of Creation) 16(2):95–104, 2002 — the shells "
                   "derivation, eqs. (5)–(15), the 1.6 and 3.1 million light-year spacings, the "
                   "peculiar-motion footnote 18, the velocity table in footnote 28, and the "
                   "disclaimer of geocentrism on p. 100 whose footnote 35 cites Bouw",
             url="https://dl0.creation.com/articles/p067/c06793/j16_2_95-104.pdf"),
        dict(label="Napier & Guthrie, “Quantized redshifts: a status report”, J. Astrophys. "
                   "Astr. 18:455–463 (1997) — “strongly quantized in the galactocentric frame "
                   "of reference”, 37.5 and 71.1 km/s",
             url="https://www.ias.ac.in/article/fulltext/joaa/018/04/0455-0463"),
        dict(label="Bajan, Flin, Godłowski & Pervushin, “On the investigations of galaxy "
                   "redshift periodicity”, Phys. Part. Nucl. Lett. 4(1):5–11 (2007) — 2522 "
                   "Hercules Supercluster galaxies, peaks at 2σ, “not well established”, and "
                   "the statement that the periodicity appears only in galactocentric or CMB "
                   "frames",
             url="http://www1.jinr.ru/Pepan_letters/panl_1_2007/02_baj.pdf"),
        dict(label="Hawkins, Maddox & Merrifield, “No periodicities in 2dF Redshift Survey "
                   "data”, MNRAS 336:L13 (2002) — the log(1+z) quasar periodicity on 1647 "
                   "galaxy–quasar pairs, not Tifft's galaxy comb",
             url="https://arxiv.org/abs/astro-ph/0208117"),
        dict(label="Kashibadze, Karachentsev & Karachentseva, “Structure and kinematics of the "
                   "Virgo cluster of galaxies”, A&A 635:A135 (2020) — distance 16.5 Mpc, "
                   "virial radius 1.7 Mpc, radial velocity dispersion 638 ± 35 km/s",
             url="https://arxiv.org/abs/2002.12820"),
        dict(label="Eisenstein et al., “Detection of the baryon acoustic peak…”, ApJ 633:560 "
                   "(2005) — 46,748 luminous red galaxies, 3816 deg², 0.72 h⁻³ Gpc³, a "
                   "correlation-function bump near 100 h⁻¹ Mpc: a preferred shell radius "
                   "around every galaxy",
             url="https://arxiv.org/abs/astro-ph/0501171"),
        dict(label="Broadhurst, Ellis, Koo & Szalay, “Large-scale distribution of galaxies at "
                   "the Galactic poles”, Nature 343:726 (1990) — the ~128 h⁻¹ Mpc pencil-beam "
                   "regularity that the “evenly spaced layers” passage is describing",
             url="https://www.nature.com/articles/343726a0"),
        dict(label="Yoshida et al., “Simulations of deep pencil-beam redshift surveys”, MNRAS "
                   "325:803 (2001) — the Broadhurst regularity has a priori probability well "
                   "below 10⁻³ in CDM",
             url="https://academic.oup.com/mnras/article/325/2/803/1164547"),
        dict(label="Ryabinkov & Kaminker, “Search for a possible quasi-periodic structure based "
                   "on data of the SDSS DR12 LOWZ”, MNRAS 527:1813 (2023) — 176,962 galaxies, "
                   "~116 ± 10 h⁻¹ Mpc, 4–5σ, and reported as anisotropic",
             url="https://academic.oup.com/mnras/article/527/2/1813/7280403"),
        dict(label="Strauss et al., “Spectroscopic target selection in the Sloan Digital Sky "
                   "Survey: the main galaxy sample”, AJ 124:1810 (2002) — the Petrosian "
                   "r < 17.77 flux limit that makes the wedge diagram thin out with distance",
             url="https://arxiv.org/abs/astro-ph/0206225"),
        dict(label="Tifft, “Discrete states of redshift and galaxy dynamics I”, ApJ 206:38 "
                   "(1976); Tifft & Cocke, “Global redshift quantization”, ApJ 287:492 (1984)",
             url="https://ui.adsabs.harvard.edu/abs/1976ApJ...206...38T/abstract"),
        dict(label="Biblical Astronomer no. 143 (vol. 23) — the annotated index of Bouw's "
                   "Geocentricity: Christianity in the Woodshed, listing “Tifft's phenomenon” "
                   "and “distributions centered on the earth” in ch. 36, p. 533, and announcing "
                   "the book as newly available",
             url="https://www.geocentricity.com/ba1/143.pdf"),
    ]),
}
