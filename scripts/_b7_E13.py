# -*- coding: utf-8 -*-
"""
Batch 7 — ARG-E13, "Supernova dimming, BAO, birefringence and Lyman-alpha
anisotropy". 6 items, lane E, verdict NOT DEMONSTRATED, recorded originator NONE.

THIS ENTRY CORRECTS OUR OWN RECORD. E13 was one of 30 arguments carrying
`originator: None`, and it was assigned here as the second-ever audit of that
label (E17 was the first). The audit does not confirm it. Three of the six items
have a documented ancestor in Sungenis & Bennett's *Galileo Was Wrong* — two of
them beyond reasonable doubt, on the strength of a lexical match the list could
not have produced independently:

  * item 358 "Cosmic birefringence ecliptic."  -> Vol. II, ch. 10, the section
    on Nodland & Ralston (1997) under the literal subheading "Birefringence:",
    whose punchline is a polarization axis "in the ecliptic plane along the
    equinox". Birefringence AND ecliptic, in the same three pages.
  * item 334 "Supernova dimming alternatives." -> Vol. I, ch. 2, the footnote
    that sets out the SNIa dimming result, cites Riess 1998, and then cites
    Celerier's inhomogeneous (LTB void) reading as the alternative.
  * item 194 "Photon spin alignment." -> probably Vol. I, ch. 3, pp. 413-415,
    quoting Urban & Zhitnitsky on aligned "polarisation angles of photons".
    Weaker: E04 already owns the quasar-polarization material, so 194 may simply
    be a duplicate of item 321 filed into the wrong cluster.

Three items — 335 (BAO), 356 (Tully-Fisher), 357 (Lyman-alpha) — were not found
anywhere. The words do not occur in the 5.4 MB full text of all three volumes,
in DeLano's blog, or in Sungenis's 2011 NPA paper. Search log is in the gloss.

Consequence for the page: the "30 untraced" figure is soft, and the two audits
run so far have returned two different answers. E17 really was traceless; E13 is
half-traced. `compression.assessed` is True here, not "no_source".

RESTRAINT, inherited from E01 and E03 and required by the physics. Three of the
underlying results are live: cosmic birefringence sits at 3.6 sigma and its own
authors decline to assign it cosmological significance; the Tully-Fisher
zero-point dipole is real at 877:1 odds; DESI DR2 BAO is in 2.3 sigma tension
with CMB-preferred LambdaCDM and prefers evolving dark energy. Nothing here may
be written as though cosmology were finished. The LTB void model is likewise
treated as what it was: a serious published alternative to dark energy, killed
by measurement rather than by preference.

Numbers taken from the papers cited, checked against arXiv metadata 2026-08-08.
"""

ENTRY = {

"E13": dict(

    tldr=("Two of these six items are traceable after all, which makes our own record wrong: "
          "they descend from Sungenis and Bennett, not from nobody. The other four name real "
          "measurements and stop — and two of those, BAO and the Lyman-alpha forest, are the "
          "standard rulers that broke the void model the supernova item needs. The one "
          "anisotropy in the cluster that is genuinely measured, a 4 per cent dipole in "
          "Tully–Fisher distances, is explained by our own motion."),

    passage=dict(
        work="WRK-SUNGENIS-2006",
        pd=False,
        locator=("Vol. II, ch. 10 “Technical and Summary Analysis of Geocentrism”, the section "
                 "“Nodland, Ralston (1997)” and its subheading “Birefringence:”, pp. 380–383 as "
                 "paginated in the archive.org scan of the 2013 edition. The supernova material "
                 "is elsewhere: Vol. I, ch. 2, footnote on p. 252."),
        # Trimmed 2026-08-08: the full excerpt ran 66 words against our 60-word
        # fair-use ceiling for in-copyright works. Cut the COBE aside and the
        # "data does not lie" line; the two directions and the conclusion remain.
        quote=("There seems that the statistical analysis is pointing out two directions of "
               "polarization: 1. The Cosmic Microwave Background dipole direction toward the "
               "Leo-Virgo clusters … 2. A new direction in the ecliptic plane along the "
               "equinox … We interpret the galactic polarization data as indicative of "
               "sources that are geocentric: symmetric around AND centered on the Earth!"),
        gloss="""<p><strong>This entry began as an audit of the word <em>untraced</em>, and the word did not survive it.</strong> ARG-E13 is one of thirty arguments our record carries with <code>originator: None</code>. Only one of the thirty &mdash; <a href="#ARG-E17">ARG-E17</a> &mdash; had ever been tested. E13 was the second test, and it came back the other way.</p>

<p><strong>What was found, and how firmly.</strong> Three of the six items have a documented ancestor; the case is strongest for two of them.</p>
<ul>
<li><strong>Item 358, &ldquo;Cosmic birefringence ecliptic.&rdquo;</strong> &mdash; the passage quoted above. Volume II devotes three pages to Nodland and Ralston's 1997 claim of a cosmological rotation of radio-galaxy polarization, gives it a subheading reading simply <em>Birefringence:</em>, and closes by placing the axis <em>&ldquo;in the ecliptic plane along the equinox&rdquo;</em>. The item's two content words are <em>birefringence</em> and <em>ecliptic</em>, and they occur together, as the section's heading and its punchline, in a geocentrist book. That is not a coincidence one should talk oneself out of.</li>
<li><strong>Item 334, &ldquo;Supernova dimming alternatives.&rdquo;</strong> &mdash; Volume I, chapter 2, in a footnote: <em>&ldquo;The 1a Supernovae explosions were dimmer than expected &hellip; So what is making it speed up? &hellip; it forces the introduction of &lsquo;dark energy&rsquo;&hellip;&rdquo;</em>, citing Riess et al. 1998 by title and then Marie-No&euml;lle C&eacute;l&eacute;rier as the alternative reading. The item names the alternative; the source supplies it.</li>
<li><strong>Item 194, &ldquo;Photon spin alignment.&rdquo;</strong> &mdash; probably Volume I, ch. 3, pp. 413&ndash;415, which quotes Urban and Zhitnitsky on <em>&ldquo;polarisation angles of photons &hellip; these vectors tend to identify an axis in the sky&rdquo;</em> and adds that the axis points along <em>&ldquo;the [sun-earth] ecliptic or equinox&rdquo;</em>, citing Hutsem&eacute;kers. Held loosely: polarization is the photon's spin state, so the compression is available, but <a href="#ARG-E04">ARG-E04</a> already owns the quasar-polarization items and 194 may simply be a duplicate of item 321 filed into the wrong cluster.</li>
</ul>

<p><strong>What was searched, and where it stopped.</strong> Full-text search of the 5.4 MB OCR of all three volumes of <em>Galileo Was Wrong</em> (archive.org, 2013 ed.) and separately of the Volume II scan; Sungenis's 2011 Natural Philosophy Alliance paper <em>Cosmological Evidence Shows Central and Non-Moving Earth</em>; Rick DeLano's blog <em>Magisterial Fundies</em> by feed query; the Association for Biblical Astronomy material at geocentricity.com; the zetetic compilations (Rowbotham, Carpenter, Dubay, Skiba); and open web search on the item strings. <strong>Three items returned nothing anywhere.</strong> <em>Baryon acoustic</em>, <em>BAO</em> as a term of art, <em>Lyman</em> and <em>Tully&ndash;Fisher</em> (other than one mention of the Fisher&ndash;Tully catalogue inside the redshift-quantization material that belongs to <a href="#ARG-E12">ARG-E12</a>) do not occur in the geocentric literature we can reach. On DeLano's blog the feed returns zero hits for all four terms while returning ten for <em>dipole</em>, which is the shape of a real absence rather than a failed query.</p>

<p><strong>The correction to our own record.</strong> The cluster record and all six item records read <code>originator: None</code>, <code>real_source_cited: None</code>. For items 334, 358 and probably 194 that is wrong, and the fix is Sungenis &amp; Bennett, <em>Galileo Was Wrong</em>, at the locators above. The general lesson is worse than the particular one: <em>untraced</em> was a label applied at triage and never tested, and the first two tests of it have returned two different answers. <strong>Thirty is an upper bound, not a count.</strong></p>

<p><strong>Two observations about how the list was assembled</strong>, offered as observations and not as findings. First, the specimen page heads this block <em>&ldquo;435 Pieces of Evidence The Earth is Not A Spinning Ball&rdquo;</em> while its own banner advertises <em>&ldquo;461 REASONS&hellip;&rdquo;</em>; the list overran its own heading by twenty-six at some point and nobody updated the number. Second, these six are bare noun phrases with no result and no inference &mdash; which is what our <code>NOT DEMONSTRATED</code> verdict already says &mdash; and their neighbours run <em>Kinematic SZ ambiguity</em>, <em>Planck systematics Earthward</em>, <em>Copernican principle assumption</em>, <em>MOND epicycle analogy</em>. That is the vocabulary of the papers that <em>answer</em> this argument, not of the books that make it, and item 194 sits four lines from <em>Earth heart chakra symbolism</em>. Whatever produced the block, it was sweeping a technical vocabulary rather than following a source. We cannot show that, and we do not assert it.</p>"""),

    steelman=dict(
        description="""<p><strong>Surface (weak, and wrong here).</strong> <em>These are just jargon words with nothing behind them.</em> Tempting, because four of the six really are bare labels &mdash; and it would be a bad answer, because behind every label is a real result, two of them currently unsettled. Dismissing the vocabulary is not answering the argument.</p>

<p><strong>Deeper (true, incomplete).</strong> <em>Every one of these observations is interpreted inside a cosmological model, so the model-dependence is not a scandal.</em> True. Also unusable on its own, because it is precisely what the argument says, and left there it collapses into &ldquo;all measurement is theory-laden&rdquo;, which concedes the floor.</p>

<p><strong>Kernel (the specific true thing).</strong> Take the supernova item at full strength, because at full strength it is a real position held by real cosmologists. In 1998 and 1999 two teams found distant type Ia supernovae fainter than a decelerating universe predicts &mdash; Riess and 15 collaborators on 16 objects, Perlmutter and 31 collaborators on 42 &mdash; and the standard reading is accelerating expansion driven by dark energy, which took the 2011 Nobel Prize. But the observation is a magnitude&ndash;redshift relation, and the inference to acceleration goes through the assumption that the universe is homogeneous on large scales. Drop that assumption and the same faintness follows from geometry: if we sit near the centre of a Gpc-scale underdensity, light from outside it traverses regions expanding at different rates and distant supernovae are dimmed without any acceleration at all. <strong>This is not a fringe manoeuvre.</strong> Marie-No&euml;lle C&eacute;l&eacute;rier set it out in <em>Astronomy &amp; Astrophysics</em> in 2000, writing that a straight reading of the data <em>&ldquo;does not exclude the possibility of ruling out the Cosmological Principle&mdash;and cosmological constant&mdash;hypotheses&rdquo;</em>, and Lema&icirc;tre&ndash;Tolman&ndash;Bondi void models were developed for a decade afterwards in <em>Physical Review D</em> and <em>JCAP</em>. The list's item points at a real, published, non-crank alternative.</p>

<p>And two of the other items point at things that are open <em>now</em>. Cosmic birefringence &mdash; a rotation of the CMB polarization plane, which would violate parity &mdash; is measured at &beta; = 0.342&deg; (+0.094/&minus;0.091) by Eskilt and Komatsu across Planck and WMAP, excluding zero at 3.6&sigma;; the same group's Planck PR4 analysis explicitly declines to assign it cosmological significance until the polarized foregrounds are better understood. And a dipole in Tully&ndash;Fisher distances is not hypothetical: Stiskalek, Desmond and Lavaux find a zero-point dipole of 0.087 &plusmn; 0.019 mag in CosmicFlows-4, a 4.1 &plusmn; 0.9 per cent dipole in the Hubble parameter, favoured over isotropy at odds of 877:1. Someone naming these is naming live measurements, not imaginary ones.</p>""",

        why_it_doesnt_save_claim="""<p><strong>The void model was killed by the other items on this list.</strong> That is the whole answer, and it is unusually clean. The BAO scale is a standard ruler that can be measured both across the line of sight and along it; a radial inhomogeneity distorts the two differently, so BAO is exactly the instrument for testing whether we sit at the centre of one. Zumalac&aacute;rregui, Garc&iacute;a-Bellido and Ruiz-Lapuente ran that test in <em>JCAP</em> in 2012: adding higher-redshift BAO forces a central density &Omega;<sub>in</sub> &gt; 0.2, where the supernovae the void was invented to explain require &Omega;<sub>in</sub> &lt; 0.15 &mdash; 3&sigma; apart &mdash; and the constrained models are &ldquo;ruled out at high confidence&rdquo;. Moss, Zibin and Scott reached the same place from a wider set (supernovae, the full CMB spectrum, radial BAO, local expansion rate, age, nucleosynthesis, the Compton <em>y</em>-distortion and &sigma;<sub>8</sub>): voids predict too low a local Hubble rate, suffer an old-age problem, and predict far less local structure than is seen. Caldwell and Stebbins had already used the blackbody purity of the CMB spectrum to exclude the largest acceleration-mimicking voids, and Zhang and Stebbins used the kinetic Sunyaev&ndash;Zel'dovich power measured by ACT and SPT to exclude the adiabatic void outright. <strong>So item 335 does not support item 334. It is what refuted it.</strong></p>

<p><strong>The void also needs worse fine-tuning than the thing it was invented to avoid.</strong> Blomqvist and M&ouml;rtsell showed that supernova data alone permit an observer displaced up to 15 per cent of the void's scale radius, but once the observed CMB dipole is included the observer must sit within about <em>one per cent</em> of the centre. A model adopted to avoid an unexplained energy density ends by requiring us to be parked at the middle of a gigaparsec structure to a part in a hundred.</p>

<p><strong>The birefringence signal has no direction, which is the one property the item asserts.</strong> &beta; is a single isotropic rotation angle &mdash; a monopole. It has no axis, no pole, and nothing to align with the ecliptic. The <em>anisotropic</em> component, which is the only thing that could have a direction, is consistent with zero: SPT-3G sets a 95 per cent upper limit on its amplitude of 1.2&times;10<sup>&minus;4</sup>, tightening to 0.53&times;10<sup>&minus;4</sup> with a lensing prior. The item's distinguishing word names the part of the measurement that is not there.</p>

<p><strong>And the Tully&ndash;Fisher dipole resolves the wrong way for the argument.</strong> Stiskalek, Desmond and Lavaux go on to show that once a radially varying velocity dipole is allowed, the anisotropic zero-point model is capturing local flow &mdash; peculiar motion, or systematics &mdash; rather than any anisotropy of expansion, and the inferred bulk-flow curve is &ldquo;fully consistent with expectations from the standard cosmological model&rdquo;. The measured directionality in Tully&ndash;Fisher distances is the signature of the observer <em>moving</em>. It is evidence against a stationary Earth, produced by the item that was offered in favour of one.</p>"""),

    refutation="""<p><strong>What this cluster is.</strong> Six lines, each naming a real measurement and stopping there: <em>Photon spin alignment. Supernova dimming alternatives. BAO fits geocentric models. Tully&ndash;Fisher scatter direction. Lyman-alpha anisotropy. Cosmic birefringence ecliptic.</em> No number, no direction, no observer, no inference. The verdict <strong>NOT DEMONSTRATED</strong> is about that and survives the discovery of a source: knowing where two of the labels came from tells us what argument they gesture at, and the gesture still contains no argument. So the sections below supply the missing inference in its strongest available form and answer that.</p>

<p><strong>1 &middot; Supernova dimming, and the model that was built on it.</strong> The observation is solid and forty years of instrument-building went into it: type Ia supernovae are standardizable, their peak brightness recoverable from the shape of the light curve, and beyond <em>z</em> &asymp; 0.5 they are fainter than a matter-only universe predicts. Riess et al. (1998) and Perlmutter et al. (1999) both found it; the standard reading is accelerated expansion. The geocentric reading is the inhomogeneous one, and it is a real published model &mdash; a Lema&icirc;tre&ndash;Tolman&ndash;Bondi void of gigaparsec scale with us near the middle, reproducing the same magnitude&ndash;redshift curve with no cosmological constant. C&eacute;l&eacute;rier's 2000 paper is the standard reference and its own summary is careful: the data <em>&ldquo;can thus be interpreted as implying <strong>either</strong> a strictly positive cosmological constant in a homogeneous universe <strong>or</strong> large scale inhomogeneity with no constraint on &Lambda;&rdquo;</em>. That is a disjunction, offered as a call for better data, and better data arrived.</p>

<p>The void model failed four independent tests, none of them philosophical. <em>Radial versus transverse rulers:</em> adding high-redshift BAO splits the required central density from the supernova-required value by 3&sigma; and rules the constrained models out at high confidence (Zumalac&aacute;rregui et al. 2012). <em>Spectral purity:</em> a large void distorts the CMB blackbody through the reionized gas that reflects our own light back to us, and the observed spectrum excludes the largest acceleration-mimicking voids (Caldwell &amp; Stebbins 2008). <em>Kinetic Sunyaev&ndash;Zel'dovich:</em> gas clouds off the centre would see a large CMB dipole and scatter it, and the required signal exceeds the ACT and SPT limits (Zhang &amp; Stebbins 2011). <em>Everything else at once:</em> voids predict too low a local expansion rate, are too old, and produce too little local structure (Moss, Zibin &amp; Scott 2011). And the fine-tuning cost is severe: once the CMB dipole is used, our position is pinned to within about 1 per cent of the void's scale radius (Blomqvist &amp; M&ouml;rtsell 2010).</p>

<p><strong>2 &middot; BAO, which is the murder weapon and not the alibi.</strong> Before recombination, photons and baryons were a single fluid; a pressure wave ran out from each overdensity until the photons decoupled and left the baryons stranded in a shell about 147 Mpc across. That shell shows up today as a bump in the galaxy correlation function at a known physical size &mdash; a standard ruler. It was detected in 2005 in 46,748 SDSS luminous red galaxies as a peak at 100 <em>h</em><sup>&minus;1</sup> Mpc, fixing the distance to <em>z</em> = 0.35 to 5 per cent, and independently in the 2dF survey. DESI DR2 now measures it across more than 14 million galaxies and quasars.</p>

<p>Two things follow. The first is that <em>&ldquo;BAO fits geocentric models&rdquo;</em> inverts the record: the ruler's transverse-versus-radial comparison is the discriminating test for radial inhomogeneity, and it is the test the void failed. The second is a concession that must be made plainly, because the alternative is the overclaiming this project exists to avoid: <strong>BAO is not currently a quiet field.</strong> DESI DR2 is in mild, 2.3&sigma; tension with the parameters preferred by the CMB under flat &Lambda;CDM, and fits better with a time-evolving dark-energy equation of state. Cosmology is moving. It is not moving toward a stationary Earth &mdash; every one of those measurements is a measurement of an expanding universe, made with a ruler laid down 13.8 billion years ago &mdash; but nobody reading this page should be told the model is finished.</p>

<p><strong>3 &middot; Lyman-alpha, on either reading.</strong> The item does not say which anisotropy it means, so take both. <em>Reading one, the forest:</em> neutral hydrogen along the line of sight to a distant quasar absorbs at 121.6 nm, redshifted differently at each intervening cloud, so a single spectrum is a one-dimensional core sample of the intergalactic medium. Its clustering <em>is</em> anisotropic &mdash; radial and transverse correlations differ &mdash; and this is not an embarrassment: the anisotropy comes from peculiar velocities along the line of sight (redshift-space distortion) and is used as a measurement. DESI's first-year Lyman-alpha analysis used more than 420,000 forest spectra against 700,000 quasars to fix the expansion rate at <em>z</em> = 2.33 to 2 per cent, <em>H</em> = (239.2 &plusmn; 4.8)(147.09 Mpc/<em>r</em><sub>d</sub>) km s<sup>&minus;1</sup> Mpc<sup>&minus;1</sup>. An anisotropy predicted by gravitational infall in an expanding universe, measured to two per cent, is not evidence of centrality.</p>

<p><em>Reading two, the fine-structure constant.</em> Webb and colleagues reported in 2011 that quasar absorption spectra from Keck and the VLT fit a spatial dipole in &alpha; at 4.2&sigma;, pointing to RA 17.5 &plusmn; 0.9 h, dec &minus;58 &plusmn; 9&deg;. That was a serious claim, and it has been substantially undermined by instrumental work rather than by argument: Whitmore and Murphy (2015) found long-range wavelength-scale distortions in both spectrographs capable of producing effects of the observed size, and the ESPRESSO measurement toward HE 0515&minus;4414, calibrated with a laser frequency comb, gives &Delta;&alpha;/&alpha; = 1.3 &plusmn; 1.3<sub>stat</sub> &plusmn; 0.4<sub>sys</sub> ppm &mdash; consistent with no variation. Note also where the dipole pointed. It is nowhere near the CMB dipole apex, nowhere near the low-multipole axis of <a href="#ARG-E01">ARG-E01</a>, and nowhere near the Nodland&ndash;Ralston axis. <strong>The claimed axes do not agree with one another</strong>, and they are described collectively as pointing at the Earth only because every direction on the sky passes through the observer who drew it.</p>

<p><strong>4 &middot; Birefringence, where the source is traceable and superseded.</strong> Nodland and Ralston reported in <em>Physical Review Letters</em> in 1997 that the polarization plane of radio galaxies rotates with distance in a way correlated with a fixed direction in space &mdash; and hedged it themselves: <em>&ldquo;Barring hidden systematic bias in the data, the correlation indicates a new cosmological effect.&rdquo;</em> The bias was found within weeks. Eisenstein and Bunn showed the Monte-Carlo significance rested on an incorrect null hypothesis, and that the correct one weakens the case. Carroll and Field re-analysed the same data and found no statistically significant signal. Wardle, Perley and Cohen went to better-resolved sources and reported a least-squares slope <em>&ldquo;only 2% of their claimed effect&rdquo;</em>. Three rebuttals in the same journal within five months; the claim did not survive 1997. Volume II of <em>Galileo Was Wrong</em> nevertheless presents it as standing, adds that the axis lies on the equinox line, and concludes that the sources are <em>&ldquo;symmetric around AND centered on the Earth&rdquo;</em>.</p>

<p>Meanwhile the phrase <em>cosmic birefringence</em> has been taken over by a different and better measurement, and it is genuinely live. Minami and Komatsu (2020) mitigated the polarization-angle calibration problem that had limited every earlier attempt, by fitting the miscalibration and the birefringence angle simultaneously against the Galactic foreground, and found &beta; = 0.35&deg; &plusmn; 0.14&deg;. Eskilt and Komatsu (2022), combining Planck and WMAP across 23&ndash;353 GHz, report &beta; = 0.342&deg; (+0.094/&minus;0.091), excluding zero at 3.6&sigma;, with no frequency dependence. This <strong>must not be described as settled in either direction</strong>: the same group's PR4 analysis found &beta; falling as the Galactic mask grows and wrote that they <em>&ldquo;choose not to assign cosmological significance to the measured value of &beta; until we improve our knowledge of the foreground polarization&rdquo;</em>. If it holds it is parity violation, which would be a major result.</p>

<p>It would also be no use here, for a structural reason. The measured &beta; is <em>isotropic</em>: one angle, applied to the whole sky, the monopole of the birefringence field. It has no direction and therefore nothing to align with the ecliptic. The component that <em>would</em> have a direction is the anisotropic one, and it is consistent with zero &mdash; SPT-3G gives a 95 per cent upper limit of 1.2&times;10<sup>&minus;4</sup> on its amplitude, 0.53&times;10<sup>&minus;4</sup> under a lensing prior. So the item pairs a 1997 result that was refuted with a 2020 result that has no ecliptic in it.</p>

<p><strong>5 &middot; Tully&ndash;Fisher, the only item where a directional anomaly is actually detected.</strong> The Tully&ndash;Fisher relation ties a spiral galaxy's luminosity to its rotation width, giving distances independent of redshift, with a scatter of a few tenths of a magnitude. If that scatter had a preferred direction, distances would be systematically longer on one side of the sky. It does: Stiskalek, Desmond and Lavaux (MNRAS, 2026) fit a zero-point dipole of 0.087 &plusmn; 0.019 mag in the CosmicFlows-4 W1 sample &mdash; 4.1 &plusmn; 0.9 per cent expressed as a dipole in <em>H</em><sub>0</sub> &mdash; with Bayesian odds of 877:1 over isotropy, and 0.049 &plusmn; 0.013 mag in Pantheon+ supernovae. Concede all of it. Then read their next sentence: allowing the velocity dipole to vary with distance shows the anisotropic zero-point is absorbing <em>local flow</em>, and the resulting bulk-flow curve is fully consistent with the standard model. The dipole is what you get when the observer is being carried through a lumpy universe at a few hundred km/s &mdash; the same motion that produces the CMB dipole at 369.82 &plusmn; 0.11 km/s. It is a measurement of our velocity. A stationary Earth predicts zero.</p>

<p><strong>6 &middot; Photon spin alignment.</strong> Photon spin is polarization, and the aligned-polarization claim is the quasar material handled at <a href="#ARG-E04">ARG-E04</a>: Hutsem&eacute;kers et al. found quasar polarization vectors correlated over ~1 Gpc, the effect is real and replicated, and the mechanism now on the table is that black-hole spin axes align with the filaments the quasars sit in. The preferred directions differ between redshift slices and hemispheres, so there is no single axis and none through the Earth. The item adds nothing to E04 except a second entry in the running total.</p>

<p><strong>7 &middot; The question the whole cluster fails.</strong> Ask what any of this would distinguish. Not one item separates a flat, stationary Earth from an ordinary spinning globe &mdash; every measurement here is of objects between 300 Mpc and the surface of last scattering, and every one is equally available on either account. Worse for the argument, the measurements are <em>produced by</em> the motion they are cited against: observed wavelengths in every survey quoted above are corrected to the solar-system barycentre before anything else happens, which is the Earth's orbital and rotational velocity entered as a calibration step in the pipeline that yields the numbers.</p>

<p>The internal consistency is no better. The void model item 334 needs is an expanding-universe model with a 13.8-billion-year history, no firmament, no dome and no edge; it puts us near the middle of a large underdensity, which is a claim about position in a cosmos that is <em>not</em> revolving about us. That is not the claim the rest of the list makes, and it is not a claim any flat-earth cosmology can hold. And the giveaway sits one line up in the list itself: item 333 is <em>&ldquo;Kinematic SZ ambiguity&rdquo;</em>, and the kinetic Sunyaev&ndash;Zel'dovich effect is the measurement that excluded the void that item 334 requires. The list is carrying its own refutation as the adjacent entry, which is what happens when a vocabulary is swept rather than an argument followed.</p>""",

    straw_man=dict(
        identified=True,
        detail=("The straw man is of standard cosmology, and it is implicit in the word "
                "'alternatives'. The items are framed as though model-dependence were something "
                "cosmologists conceal and an outsider has noticed. The record is the reverse: the "
                "inhomogeneous alternative to dark energy was proposed by a cosmologist in "
                "Astronomy & Astrophysics, developed for a decade in Physical Review D and JCAP, "
                "and killed by cosmologists using BAO, the kSZ effect, the CMB spectrum and the "
                "local structure amplitude. The Copernican principle is treated in that "
                "literature as a hypothesis to be tested, and the titles say so — Caldwell and "
                "Stebbins call theirs a modern test of the Copernican principle, Zhang and "
                "Stebbins call theirs a confirmation of it at gigaparsec scale. Answering this "
                "cluster honestly means conceding that the alternative was taken seriously and "
                "pointing out that the people who took it seriously are the ones who refuted it.")),

    verdict_challenge=dict(challenged=False, proposed_verdict=None, reasoning=None),

    compression=dict(
        assessed=True, drifted=True,
        list_phrasing=("Cosmic birefringence ecliptic. / Supernova dimming alternatives. / "
                       "Photon spin alignment."),
        source_wording=("&ldquo;A new direction in the ecliptic plane along the equinox &hellip; "
                        "We interpret the galactic polarization data as indicative of sources "
                        "that are geocentric&rdquo; (Vol. II, p. 383) &middot; &ldquo;The 1a "
                        "Supernovae explosions were dimmer than expected &hellip; See also "
                        "Marie-No&euml;lle C&eacute;l&eacute;rier who concludes: &lsquo;a "
                        "straight reading of these data does not exclude the possibility of "
                        "ruling out the Cosmological Principle&rsquo;&rdquo; (Vol. I, p. 252 n.) "
                        "&middot; &ldquo;polarisation angles of photons &hellip; tend to identify "
                        "an axis in the sky&rdquo; (Vol. I, p. 413, quoting Urban &amp; "
                        "Zhitnitsky)"),
        drift_type="hedge_dropped",
        note="""<p><strong>Read the first finding before the drift, because it is larger than the drift.</strong> This comparison was supposed to be impossible. ARG-E13 is recorded with no originator, and the audit was expected to return <em>no source</em>, as it did for <a href="#ARG-E17">ARG-E17</a>. It did not. Items 334 and 358 have a documented ancestor in <em>Galileo Was Wrong</em>, and item 194 probably does. <strong>Our record is wrong about this cluster, and the &ldquo;30 untraced arguments&rdquo; figure is an upper bound rather than a count</strong> &mdash; two of the thirty have now been tested and they came back differently. The remaining twenty-eight carry a label nobody has checked. See the gloss for the search log and the exact locators.</p>

<p><strong>Now the drift.</strong> Where an ancestor exists, the hedge is stripped at every step of the way down. C&eacute;l&eacute;rier's sentence is triple-hedged &mdash; <em>a straight reading</em> of the data <em>does not exclude</em> the <em>possibility</em> of ruling out the Cosmological Principle &mdash; and her paper's own conclusion is a disjunction that asks for more data, not a result. Sungenis reproduces the hedge honestly in his footnote. The list keeps neither: <em>&ldquo;Supernova dimming alternatives&rdquo;</em>, numbered, inside a document titled <em>Pieces of Evidence The Earth is Not A Spinning Ball</em>. A conditional non-exclusion has become an item of proof. The same happens to item 358 twice over: Nodland and Ralston wrote <em>&ldquo;Barring hidden systematic bias in the data&hellip;&rdquo;</em>, the hidden bias was demonstrated by three independent groups within five months, and neither the qualifier nor its vindication is anywhere in the two-word item.</p>

<p><strong>The enum is a loose fit and it should be said rather than hidden.</strong> <code>hedge_dropped</code> is recorded because the dominant move is the loss of the source's qualifiers, but two things are going on that no value in the list names. One is a <em>date shift</em>: item 358 attaches a term whose current referent is a 2020 CMB measurement to a 1997 radio-galaxy claim that was refuted in 1997, so the item is carrying a live word in front of a dead result. The other is that <strong>these items are not assertions at all</strong> &mdash; they are topic labels, and a label cannot drop a hedge by itself. The assertion is supplied by the frame the labels sit in. That is a different mechanism from the compression documented at <a href="#ARG-A03">ARG-A03</a> or <a href="#ARG-R01">ARG-R01</a>, where a sentence was rewritten; here nothing was rewritten, and the strength was added by the title of the page.</p>

<p><strong>Three items had nothing to compare against.</strong> Items 335 (BAO), 356 (Tully&ndash;Fisher) and 357 (Lyman-alpha) were not found in any source we could reach: the terms do not occur in the full text of all three volumes of <em>Galileo Was Wrong</em>, in Sungenis's 2011 conference paper, in DeLano's blog, in the Association for Biblical Astronomy material, or in the zetetic compilations. For those three the honest description is the E17 one &mdash; the claim descends from nobody in particular, and the refutation above answers them on their own terms rather than an author's. <em>Not found</em> is not <em>does not exist</em>: a line this short could have come from a forum post or a video caption, and a reader who can point us at an original would improve this entry. But the split within one cluster is itself the finding. Half of E13 has a book behind it and half has nothing, and the two halves are indistinguishable on the page.</p>"""),

    advocate=dict(
        survives=3,
        best_defense=("Start with what you just conceded, because it is fatal to your framing. You "
                      "filed this cluster under 'no originator' and published that as a finding "
                      "about how our literature grows — and then, when someone finally looked, the "
                      "sources were sitting in the book you have been citing all along. Your "
                      "'untraced' category is an artefact of your own reading, not of our sloppiness. "
                      "Now the substance. You concede that the supernova result does not entail dark "
                      "energy, that a void reading was published in Astronomy & Astrophysics and "
                      "developed for a decade, that cosmic birefringence stands at 3.6 sigma with its "
                      "own authors unwilling to call it settled, that a Tully-Fisher dipole is "
                      "favoured 877 to 1, and that DESI's own BAO is in tension with the CMB and "
                      "prefers an evolving dark energy nobody can name. Every one of those is a place "
                      "where the data underdetermine the model and the model is chosen on principle. "
                      "The principle chosen is the Copernican one, and you admit it is an assumption "
                      "that got promoted. So the honest reading of my six lines is not 'the Earth is "
                      "proved central'; it is 'in six separate places the interpretation depends on "
                      "assuming we are nowhere special, and that assumption is doing the work.' You "
                      "have not refuted that. You have illustrated it, and then told me the tests "
                      "that were run inside the assumption came out in its favour."),
        preemptive=("Rated 3: this must be answered in the body, not left to the reader, and one "
                    "concrete change is required. ADD a short paragraph to the refutation, after "
                    "section 2, headed on the distinction between an assumption and a tested "
                    "hypothesis, making the point the defence turns on: the Copernican principle "
                    "entered cosmology as an assumption and left it as a measurement, and the "
                    "papers cited in this entry are the mechanism — Caldwell & Stebbins title "
                    "theirs a modern test of the Copernican principle, Zhang & Stebbins a "
                    "confirmation at gigaparsec radial scale, and the void was excluded by data "
                    "that could have gone the other way and did not. A hypothesis that survives a "
                    "test it could have failed is not the same object as the assumption it started "
                    "as; cross-link ARG-R12, where that trade is the whole argument. Two further "
                    "moves to pre-empt. (1) 'You corrected your own record, so your provenance "
                    "work is unreliable.' Concede the correction loudly and publish it — that is "
                    "what review/corrections.json is for — and note that the correction runs in "
                    "the direction of giving the source MORE credit, not less: we found that "
                    "someone had written these claims down carefully, with citations, and that the "
                    "list dropped the care. (2) 'DESI's own tension shows the model is in "
                    "trouble.' Grant it without hedging. Then note that a shift from a cosmological "
                    "constant to an evolving equation of state is a change of one parameter inside "
                    "an expanding universe measured with a 147 Mpc ruler laid down 13.8 billion "
                    "years ago, and that no version of that result moves the Earth to the centre "
                    "or stops it turning.")),

    people=["PER-SUNGENIS"],
    related=["E01", "E02", "E03", "E04", "E09", "E11", "E12", "E17", "R12"],

    sources=[
        dict(label="Sungenis & Bennett, Galileo Was Wrong, Vols. I–III (2013 ed.) — full text; birefringence/ecliptic at Vol. II ch. 10, supernova footnote at Vol. I p. 252",
             url="https://archive.org/download/galileo-was-wrong-the-church-was-right-sungenis-vol-1-3-complete/Galileo%20Was%20Wrong%20The%20Church%20Was%20Right%20Sungenis%20Vol%201-3%20Complete_djvu.txt"),
        dict(label="The specimen list — withthesun33.com/about-1 (Andy J. Consoli), items 194 and 334–358",
             url="https://withthesun33.com/about-1"),
        dict(label="Riess et al. 1998, AJ 116:1009 — Observational evidence from supernovae for an accelerating universe",
             url="https://arxiv.org/abs/astro-ph/9805201"),
        dict(label="Perlmutter et al. 1999, ApJ 517:565 — Measurements of Omega and Lambda from 42 high-redshift supernovae",
             url="https://arxiv.org/abs/astro-ph/9812133"),
        dict(label="Célérier 2000, A&A 353:63 — Do we really see a cosmological constant in the supernovae data? (the inhomogeneous alternative, cited by Sungenis)",
             url="https://arxiv.org/abs/astro-ph/9907206"),
        dict(label="Zumalacárregui, García-Bellido & Ruiz-Lapuente 2012, JCAP 10:009 — BAO rules out constrained void models at high confidence",
             url="https://arxiv.org/abs/1201.2790"),
        dict(label="Moss, Zibin & Scott 2011, PRD 83:103515 — Precision cosmology defeats void models for acceleration",
             url="https://arxiv.org/abs/1007.3725"),
        dict(label="Caldwell & Stebbins 2008, PRL 100:191302 — CMB spectral distortion excludes the largest acceleration-mimicking voids",
             url="https://arxiv.org/abs/0711.3459"),
        dict(label="Zhang & Stebbins 2011, PRL 107:041301 — kSZ confirmation of the Copernican principle at Gpc radial scale",
             url="https://arxiv.org/abs/1009.3967"),
        dict(label="Blomqvist & Mörtsell 2010, JCAP 05:006 — with the CMB dipole, the observer must sit within ~1% of the void scale radius",
             url="https://arxiv.org/abs/0909.4723"),
        dict(label="Eisenstein et al. 2005, ApJ 633:560 — BAO detection in 46,748 SDSS luminous red galaxies",
             url="https://arxiv.org/abs/astro-ph/0501171"),
        dict(label="DESI DR2 2025, PRD 112:083515 — BAO from >14 million galaxies and quasars; 2.3σ tension with CMB-preferred ΛCDM",
             url="https://arxiv.org/abs/2503.14738"),
        dict(label="DESI 2024 IV — BAO from the Lyman-alpha forest, 420,000 forest spectra, H(z=2.33) to 2%",
             url="https://arxiv.org/abs/2404.03001"),
        dict(label="Nodland & Ralston 1997, PRL 78:3043 — the original birefringence claim ('barring hidden systematic bias')",
             url="https://arxiv.org/abs/astro-ph/9704196"),
        dict(label="Eisenstein & Bunn 1997, PRL 79:1957 — the significance rests on an incorrect null hypothesis",
             url="https://arxiv.org/abs/astro-ph/9704247"),
        dict(label="Carroll & Field 1997, PRL 79:2394 — re-analysis finds no statistically significant signal",
             url="https://arxiv.org/abs/astro-ph/9704263"),
        dict(label="Wardle, Perley & Cohen 1997, PRL 79:1801 — resolved sources give a slope 2% of the claimed effect",
             url="https://arxiv.org/abs/astro-ph/9705142"),
        dict(label="Minami & Komatsu 2020, PRL 125:221301 — cosmic birefringence β = 0.35° ± 0.14°",
             url="https://arxiv.org/abs/2011.11254"),
        dict(label="Eskilt & Komatsu 2022 — Planck + WMAP, β = 0.342° (+0.094/−0.091), 3.6σ",
             url="https://arxiv.org/abs/2205.13962"),
        dict(label="Diego-Palazuelos et al. 2022 (Planck PR4) — 'we choose not to assign cosmological significance to β'",
             url="https://arxiv.org/abs/2201.07682"),
        dict(label="SPT-3G 2025, Open J. Astrophys. 8 — anisotropic birefringence amplitude < 1.2×10⁻⁴ (95%)",
             url="https://arxiv.org/abs/2510.07928"),
        dict(label="Webb et al. 2011, PRL 107:191101 — the claimed 4.2σ spatial dipole in the fine-structure constant",
             url="https://arxiv.org/abs/1008.3907"),
        dict(label="Whitmore & Murphy 2015, MNRAS 447:446 — long-range wavelength distortions in Keck and VLT spectra",
             url="https://arxiv.org/abs/1409.4467"),
        dict(label="Murphy et al. 2022, A&A 658:A123 — ESPRESSO with a laser frequency comb: Δα/α = 1.3 ± 1.3 ± 0.4 ppm",
             url="https://arxiv.org/abs/2112.05819"),
        dict(label="Stiskalek, Desmond & Lavaux, MNRAS (2026) — Tully–Fisher zero-point dipole is local flow, not H0 anisotropy",
             url="https://arxiv.org/abs/2509.14997"),
        dict(label="Sungenis 2011, NPA Proceedings — 'Cosmological Evidence Shows Central and Non-Moving Earth' (searched; contains none of these six topics)",
             url="https://isidore.co/misc/Physics%20papers%20and%20books/Cosmology/Copernican%20principle/from%20DeLano%20or%20his%20blog%20or%20some%20other%20website/abstracts_5969.pdf"),
        dict(label="FlatEarth.ws — geocentrism is incompatible with the flat-earth model; the Tychonic sources hold the Earth to be a globe",
             url="https://flatearth.ws/geocentrism")]),
}
