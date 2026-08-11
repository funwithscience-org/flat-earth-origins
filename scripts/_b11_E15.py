# -*- coding: utf-8 -*-
"""Batch 11 — E15. "VLBI, interferometry and Gaia reductions assume an Earth frame."

Three items: 345 "VLBI Earth-fixed.", 346 "Interferometry ground assumption.",
347 "Gaia reduction flexible." Cluster verdict MISLEADING, kept.

Research notes for whoever picks this up next.

1. THE RECORD SAYS UNTRACED AND IT ONLY PARTLY SURVIVES. clusters.py has
   originator=None, originator_work=None, year=None, real_source=None. The argument
   behind item 345 is in print, page-located, and it is much more specific than our
   cluster name suggests. Galileo Was Wrong, seventh edition, Volume I, chapter 2,
   Objection #14 ("Don't Earthquakes and Tsunamis Retard the Earth's Rotation?"),
   printed pp. 205-206, holds a full paragraph on VLBI: the method "is flawed and
   presumes the Earth is rotating before it interprets the data", NASA and JPL
   "obtain the VLBI measurement from only one stellar source", radio wavelengths give
   "poor resolution", and therefore "all VLBI measurements are invalid to prove
   whether the Earth is rotating".

   Route: the djvu.txt OCR of Internet Archive item
   `galileo-was-wrong-the-church-was-right-sungenis-vol-1-3-complete` (5.5 MB,
   downloaded and word-searched in session 2026-08-10). In that file Volume I is
   chapters 1-6, Volume II chapters 7-13, Volume III chapters 14-17, each volume
   restarting its printed pagination — so "Vol. I p. 205" and "Vol. II p. 248" below
   are different pages, not a contradiction. Ten hits on "VLBI", all in that one
   paragraph pair.

   THIS IS A CONTENT MATCH, NOT A DEMONSTRATED CHAIN. The list carries no citations
   anywhere (re-checked against the live page this session). Do NOT set
   originator="PER-SUNGENIS" — that is precisely the guess the three-state rule
   forbids, and E14 made the same call on the same evidence. real_source is the field
   that can carry it. See note 9.

2. DATING, AND IT MATTERS. The VLBI paragraph is not located in the 2006 Volume I at
   all: the 3.3 MB djvu.txt OCR of Internet Archive item `GallileoWasWrong` returns
   zero hits on "VLBI" and zero on "Very Long Baseline". The objection it sits inside
   answers newspaper coverage of the March 2011 Tohoku earthquake, so the paragraph
   is post-2011 and reaches the reader through the seventh edition of 2013. The work
   record WRK-SUNGENIS-2006 renders as "…, 2006" above the quote; the locator says
   seventh edition in words. Same shape as the Vol. II citation in _b9_E08.

3. GAIA IS NOT IN THE BOOK. "Gaia" occurs exactly once in that 5.5 MB seventh-edition
   text, inside a block-quoted ESO press release about dark matter (Moni Bidin, Vol. I
   ch. 2, printed p. 245), where it is named as a future mission that will help. There
   is no astrometric-reduction material to compare item 347 against in the text
   searched. That is what drives drift_type="unsourced_addition".

4. THE KERNEL, AND IT IS THE BEST THING IN THIS ENTRY. The objection names its own
   test and the test is the actual design of the instrument. Verbatim: the only way to
   distinguish source motion from Earth motion "is for them to allow the VLBI to
   absorb radiation from at least three sources, if not more. If it is found that all
   the other sources are moving in the same precise way as the original source, then
   there is evidence that the Earth is rotating." Charlot et al. 2020 (the ICRF3
   paper, arXiv:2010.13625), Sect. 2: "In general, VLBI sessions are 24-hour long in
   order to separate parameters for polar motion and nutation … Each session generally
   observes a few tens to a few hundreds of sources"; the RDV sessions "assemble a
   network of 15 to 20 stations, allowing for observation of 80-100 sources each
   time." 6,206 S/X sessions, 167 telescopes on 126 sites, 3 Aug 1979 to 27 Mar 2018.
   The criterion the source sets was met before the source set it.

5. AND THE HONEST OTHER HALF, WHICH MUST STAY IN THE TEXT. A rigidly turning sky
   produces the same common motion, so the multi-source design does not by itself
   separate a turning Earth from a turning heaven — that is R01/R11 underdetermination
   and this entry concedes it in its own voice, twice. Note the consequence for the
   source, which is sharper than the concession: the book's own cosmology says the
   universe "rotates around the Earth once per day, and in that rotation it carries
   the stars with it" (Vol. I ch. 2, printed p. 229). On that model every source moves
   "in the same precise way" by construction, so the test the book proposes could not
   have discriminated anything even if NASA had run it. Same structure as the E08
   finding: the source names a discriminator its own model cannot deliver.

6. WHAT DOES BEAR ON THE EARTH RATHER THAN THE SKY, and the numbers, all checked
   2026-08-10:
     * Free core nutation. Krasna, Bohm & Schuh, A&A 555:A29 (2013): period
       -431.18 +/- 0.10 sidereal days, amplitude of order 100 uas, from VLBI 1984-2011,
       "caused by the fact that the ellipsoidal liquid core inside the visco-elastic
       Earth's mantle rotates around an axis which is slightly misaligned with the axis
       of the mantle." Rosat & Lambert, A&A 503:287 (2009) get -429.6 +/- 0.6 d
       (Q = 16,683 +/- 884) from VLBI nutation and -426.9 +/- 1.2 d (Q = 16,630 +/-
       3,562) from superconducting gravimeters, and conclude the two are "comparable
       within the error bars". Do NOT write that the two agree perfectly: they sit
       about two days apart on error bars of ~1 day, and the paper says comparable.
     * Ring laser. Schreiber et al., PRL 107:173904 (2011): 16 m^2 helium-neon ring at
       Wettzell, flicker floor "just below 10^-8" of the Earth rate, Apr-Jul 2010,
       detects the Chandler and annual wobbles with "excellent agreement with the
       independent measurements by VLBI". A ground interferometer with no sky in it.
       DO NOT claim this settles Earth-versus-ether rotation; a geocentrist reads the
       Sagnac term as ether rotation, which is A02's fight, not this one.
     * ICRF3 noise floor 0.03 mas; median uncertainty ~0.1 mas in RA, 0.2 in Dec; 500
       sources at 0.03-0.06 mas. Against the book's own Vol. II p. 248 figure of 0.05
       arcsec for Hubble, that is a factor of 1,667.
     * Galactocentric acceleration, ICRF3: 5.83 +/- 0.23 uas/yr toward
       alpha = 270.2 +/- 2.3, delta = -20.2 +/- 3.6, within 10 deg of the Galactic
       centre, "detected at the 25 sigma level"; dipolar field amplitude 0.0058 mas/yr.
       Gaia EDR3 independently: 5.05 +/- 0.35 uas/yr, (2.32 +/- 0.16) x 10^-10 m/s^2,
       from ~1.6 million quasars (Gaia Collaboration, Klioner et al., A&A 649:A9). The
       two are consistent at roughly the two-sigma level, not identical; say that.

7. THE ARITHMETIC, REPRODUCED HERE 2026-08-10.
     (a) Fringe spacing. lambda = c/8.4 GHz = 3.569 cm. Over an 8,000 km baseline,
         lambda/B = 4.461e-9 rad = 0.920 mas; over the "8000 miles" the book pictures
         (12,875 km), 0.572 mas. ICRF3's 0.03 mas noise floor is ~31 times finer than
         the 8,000 km fringe spacing, because the observable is the centroid of the
         fringe pattern, not its width.
     (b) One picosecond of group delay is 0.300 mm of light travel; ICRF3's delay model
         is quoted at 1 ps accuracy (the "consensus model", Eubanks 1991).
     (c) The book's earthquake extrapolation: 0.5 us x 25,000 quakes x 10,000 yr = 125 s.
         The arithmetic is right. The input is not — JPL's computed figure for the
         M9.0 Tohoku event, one of the largest instrumentally recorded, was 1.8 us, and
         the book assigns more than a quarter of that to each of 25,000 events a year.
     (d) A daily-rotating heaven keeps tangential speeds below c only inside
         c/Omega = 4.11e12 m = 27.5 AU = 3.8 light-hours. DO NOT deploy this as a
         knockdown: the book meets it head-on at Vol. I p. 229, arguing that space
         itself rotates and the stars are carried, so nothing moves through space
         faster than light. Deploying it as if unanswered would be exactly the
         fragment-beating the hedge rule forbids.

8. WHAT THE SOURCE GETS RIGHT, AND IT IS CONCEDED FIRST. The earthquake numbers really
   are computed rather than measured, and JPL says so in the release the book is
   attacking: "The computed change in the length of day caused by earthquakes is much
   smaller than the accuracy with which scientists can currently measure changes in the
   length of the day." The next sentence is the answer: "Over the course of a year, the
   length of the day increases and decreases by about a millisecond, or about 550 times
   larger than the change caused by the Japanese earthquake." Lead with the concession.
   The book's "recorded history has shown that there is no evidence of any appreciable
   difference between solar time and sidereal time" is answered by the eclipse record:
   Delta T is about +17,190 s at -500, and the observed lengthening of the mean solar
   day runs about +1.7 ms/cy against a tidal +2.3 ms/cy (Stephenson, Morrison &
   Hohenkerk, Proc. R. Soc. A 472:20160404, 2016).

9. VERDICT. MISLEADING was tested against REFUTED and kept. The source's PREMISES are
   contradicted by specific measurements and the entry says so; its CONCLUSION — that
   VLBI alone does not establish which body turns — is conceded, because it is true and
   non-discriminating, which is the R01 answer rather than a refutation. Meanwhile item
   347's kernel is real (the Gaia frame's orientation and spin are fixed externally, and
   there is a published -17 uas parallax bias), which is "real data, wrong conclusion" —
   MISLEADING exactly. A single label cannot say all that; MISLEADING is the one that
   misdescribes least, and the refutation states in its own voice what the verdict does
   and does not range over so a defender cannot mine the gap. No verdict_challenge filed.

10. DEFECTS IN OUR OWN RECORD, reported up, NOT edited here (this agent owns one file).
    Anchor every edit on the cluster key "E15", never on the originator= line.
      (i)   E15 real_source is None above a page-located ancestor and two named modern
            literatures (ICRF3; the Gaia EDR3 astrometric solution).
      (ii)  The cluster NAME, "…assume an Earth frame", describes the R08 convenience-
            frame argument. The located source argues something else and something
            stronger: that VLBI presupposes rotation and reads one source at a time, so
            it cannot demonstrate rotation. The name renders beside the verdict chip for
            readers who never expand the entry.
      (iii) The cluster note's "microsecond precision" was not verified from anything
            read for this entry, and the note is silent on Gaia, one of its three items.
      (iv)  WRK-SUNGENIS-2006 renders the year 2006 above a passage that is not located
            in the 2006 text. Recurring, not new.
"""

ENTRY = {

"E15": dict(

    tldr=("The book's objection is that VLBI reads one radio source at a time and so cannot "
          "tell a moving Earth from a moving source — and it names the fix itself: observe "
          "three or more and see whether they all move together. That is how geodetic VLBI is "
          "run: the sessions behind ICRF3 generally last 24 hours and observe a few tens to a "
          "few hundreds of radio sources each. VLBI on its own does not decide a turning Earth "
          "against a turning sky, and "
          "this page does not claim it does — but the objection's factual premises fail, "
          "including the one about poor resolution: an 8,000 km baseline at 8.4 GHz resolves "
          "0.92 milliarcseconds, some fifty times finer than the 0.05 arcseconds the same book "
          "gives for Hubble, and ICRF3 pins source positions to a noise floor of 0.03."),

    passage=dict(
        work="WRK-SUNGENIS-2006",
        pd=False,
        locator=("Seventh edition (2013), Vol. I, ch. 2, Objection #14 (“Don't Earthquakes and "
                 "Tsunamis Retard the Earth's Rotation?”), printed pp. 205–206 of the djvu.txt "
                 "OCR of Internet Archive item "
                 "galileo-was-wrong-the-church-was-right-sungenis-vol-1-3-complete, in which "
                 "Vol. I is chapters 1–6 and each volume restarts its pagination. Not checked "
                 "against a print copy"),
        quote=("The method commonly used is VLBI or Very Long Baseline Interferometry. … "
               "because VLBI is commonly used by NASA and JPL under the assumption that the "
               "Earth is rotating, they find it perfectly justifiable to obtain the VLBI "
               "measurement from only one stellar source."),
        gloss="""<p><strong>Read where this sits before reading what it says.</strong> The paragraph is not part of a discussion of reference frames. It is the second half of an answer to Objection #14, which is about newspaper reports that the March 2011 Tōhoku earthquake shortened the day and moved the Earth&rsquo;s axis. The book&rsquo;s reply has two limbs: that those figures were calculated rather than measured, and that the one instrument which could measure them is disqualified. The VLBI paragraph is the second limb.</p>
<p><strong>The claim is a circularity charge, not a frame-convention point.</strong> In the sentences around the quotation the book says the method &ldquo;is flawed and presumes the Earth is rotating before it interprets the data&rdquo;, that a phase difference between two stations might mean the source moved rather than the Earth, and that longer radio wavelengths &ldquo;create poor resolution&rdquo;, so an apparent shift &ldquo;may, indeed, be only a false reading&rdquo;. The conclusion is stated flatly and without qualification, and there is no hedge here to shelter behind: <em>&ldquo;Without this methodology, all VLBI measurements are invalid to prove whether the Earth is rotating.&rdquo;</em></p>
<p><strong>And it names its own test.</strong> That is the most important sentence in the passage and the reason this entry exists. The remedy the book prescribes is to &ldquo;allow the VLBI to absorb radiation from at least three sources, if not more. If it is found that all the other sources are moving in the same precise way as the original source, then there is evidence that the Earth is rotating.&rdquo; A falsifiable criterion, offered voluntarily. The refutation below takes it up.</p>
<p><strong>Dating.</strong> The objection answers coverage of a 2011 earthquake, so it is later than the 2006 first volume, and it reads that way in the record: the string <em>VLBI</em> is not located anywhere in the 3.3 MB OCR text of the 2006 Vol. I (Internet Archive item GallileoWasWrong), which returns zero hits on it and on <em>Very Long Baseline</em>. The work record beside this quotation renders the year 2006; the passage quoted here reaches print in the seventh edition of 2013.</p>
<p><strong>Two of the cluster&rsquo;s three items go beyond this page.</strong> Item 346 generalises from VLBI to interferometry as such. Item 347 is about Gaia, and Gaia&rsquo;s astrometric reduction is not located anywhere in the 5.5 MB seventh-edition text searched: the word <em>Gaia</em> occurs once in that file, inside a block-quoted ESO press release about dark matter at Vol. I p. 245, where the mission is named as future work that will help settle a question. Whatever item 347 descends from, it is not located in this book.</p>
<p><strong>An internal tension worth knowing about.</strong> The resolution premise here is contradicted elsewhere in the same seventh edition. At Vol. II, ch. 10, printed p. 248, under the heading <em>On Telescope Limits</em>, the book states that &ldquo;the highest angular resolutions can be achieved by interferometry&rdquo;, gives the Very Large Telescope Interferometer&rsquo;s target of 0.001 arcseconds and Hubble&rsquo;s 0.05 arcseconds, and thereby states the principle &mdash; resolution goes as wavelength divided by <em>baseline</em> &mdash; that makes the ch. 2 objection wrong. Different chapters, different volumes, and the technical chapters are Bennett&rsquo;s; this is offered as a tension in the text, not as an accusation.</p>
<p><strong>What this passage is being cited as.</strong> The nearest located published statement of the argument in item 345, and nothing more. The list carries no citations at all, so descent is a content match rather than a demonstrated chain, and the cluster&rsquo;s originator field stays empty.</p>"""),

    steelman=dict(
        description="""<p><strong>SURFACE (weak &mdash; do not use).</strong> &ldquo;VLBI proves the Earth rotates, so the item is simply false.&rdquo; It does not, and saying so hands the exchange away. What VLBI delivers is Earth orientation parameters: the transformation between a frame tied to the crust and a frame tied to distant radio sources. A rigidly turning sky reproduces that transformation exactly. Anybody who opens with &ldquo;VLBI proves rotation&rdquo; will be corrected by someone quoting the IERS conventions.</p>
<p><strong>DEEPER.</strong> The frames really are conventional and the reductions really are Earth-referenced. The ITRF is fixed to the crust by construction. Gaia&rsquo;s astrometric solution does not determine its own orientation or spin at all: those six degrees of freedom are supplied from outside, and for EDR3 they were fixed &ldquo;by means of 2269 ICRF3 S/X sources&rdquo; with identified optical counterparts. Radio astrometry hands optical astrometry its axes.</p>
<p><strong>KERNEL.</strong> The strongest form is not about frames but about priors, and it is correct. Every one of these reductions runs on an assumed dynamical model of the Earth and the solar system, and estimates <em>corrections</em> to it rather than the thing itself. Gaia EDR3 takes its solar-system ephemeris from INPOP10e; ICRF3 models the Earth&rsquo;s spin axis with the MHB nutation of Mathews, Herring and Buffett (2002) and its station positions from ITRF2014, complete with plate velocities. And the systematics are not hypothetical: the Gaia collaboration found that its own quasars, whose parallax must be zero, came out at a median of about &minus;17&nbsp;&mu;as. So there is a real, admitted bias in exactly the quantity heliocentrism is supposed to rest on, sitting inside a pipeline that was handed the answer as an input. Stated that way the argument is not silly at all.</p>""",
        why_it_doesnt_save_claim="""<p>Because a model that publishes its own residuals is the opposite of a circular one, and because the quantities the charge says are assumed have been measured.</p>
<p>Take the &minus;17&nbsp;&mu;as parallax bias first. Nobody hid it and nobody found it from outside: Lindegren and colleagues found it in the collaboration&rsquo;s own data, by looking at objects whose true parallax is known to be zero, and calibrated its dependence on magnitude, colour and sky position against quasars, Large Magellanic Cloud stars and physical binaries. That is a systematic being measured against physical standards and published as a correction table. And the size settles what it can carry: 17&nbsp;&mu;as against 61&nbsp;Cygni&rsquo;s parallax of about 286,000&nbsp;&mu;as.</p>
<p>Then take the assumed motion. If the barycentric ephemeris were simply presupposed and never tested, the residual pattern of quasar motions would be unconstrained noise. It is not. ICRF3 estimated the acceleration of the solar system barycentre directly from 40 years of delays &mdash; 5.83 &plusmn; 0.23 &mu;as/yr, pointing within 10&deg; of the Galactic centre, &ldquo;detected at the 25&sigma; level&rdquo; &mdash; and Gaia, optically and independently, got (2.32 &plusmn; 0.16) &times; 10<sup>&minus;10</sup>&nbsp;m/s<sup>2</sup>, or 5.05 &plusmn; 0.35 &mu;as/yr, consistent with the radio value at about the two-sigma level. The ICRF3 paper is explicit about which part of the observer&rsquo;s motion is conventional and which is measured: the constant velocity &ldquo;is absorbed into the reported source positions by convention&rdquo;, and the acceleration is fitted. A pipeline that names its own conventions and then measures the residual is doing the reverse of assuming its conclusion.</p>"""),

    refutation="""<p><strong>Start with what the source has right, because part of it is right and the agency conceded it first.</strong> The Tōhoku figures the objection attacks really were computed rather than observed. JPL&rsquo;s own release says so: Richard Gross&rsquo;s &ldquo;calculations indicate&rdquo; a shortening of about 1.8 microseconds and a figure-axis shift of about 17 centimetres, and &mdash; in the same release &mdash; &ldquo;the computed change in the length of day caused by earthquakes is much smaller than the accuracy with which scientists can currently measure changes in the length of the day.&rdquo; A reader who has only met the newspaper version has met something firmer than the science. The book noticed that, and it was worth noticing.</p>

<h4>1. The test the objection names is the design of the instrument</h4>

<p>The passage does not merely complain; it specifies what would settle the matter. Observe &ldquo;at least three sources, if not more&rdquo;, and if they are all &ldquo;moving in the same precise way&rdquo;, then &ldquo;there is evidence that the Earth is rotating.&rdquo; That criterion has been satisfied continuously since before the objection was written, and the reason is stated in the standard reference for the frame. Charlot and colleagues, describing the data behind ICRF3: <em>&ldquo;In general, VLBI sessions are 24-hour long in order to separate parameters for polar motion and nutation and to average out unmodeled geophysical effects which vary on a diurnal basis. Each session generally observes a few tens to a few hundreds of sources.&rdquo;</em> The Research and Development VLBA sessions &ldquo;assemble a network of 15 to 20 stations, allowing for observation of 80&ndash;100 sources each time.&rdquo; The frame rests on 6,206 dual-frequency sessions from 167 telescopes on 126 sites, running from 3 August 1979 to 27 March 2018, with more than a million observations collected in 2017 alone, and it publishes positions for 4,536 sources of which 303 define the axes.</p>

<p>The estimation does the separating the objection asks for, and it does it in the open. Source positions are estimated <em>globally</em> &mdash; one position per source across four decades &mdash; while the Earth orientation parameters are estimated <em>session by session</em>. An individual source that wandered would show up as a bad global position; a common rotation shows up in the session parameters. With tens to hundreds of sources spread over the sky per session, the rotation is over-determined by orders of magnitude. Even the residual common motion, the part that survives after the rotation is removed, has been measured rather than assumed: 5.83 &plusmn; 0.23 &mu;as/yr, at 25&sigma;, pointing within ten degrees of the Galactic centre &mdash; the solar system&rsquo;s own orbital acceleration, showing up as a dipole in quasar proper motions.</p>

<h4>2. What that does not establish, said plainly</h4>

<p>It does not separate a turning Earth from a turning heaven. If the whole sky is rigidly carried round once a day, every source moves &ldquo;in the same precise way&rdquo; too, and the delays come out identical. That is the general underdetermination point, and it belongs to <a href="#ARG-R01">ARG-R01</a> and <a href="#ARG-R11">ARG-R11</a>, not here; this page concedes it and will not pretend that a bigger source list refutes geocentrism by itself.</p>

<p><strong>But notice what that concession costs the objection.</strong> The book&rsquo;s cosmology, stated at Vol. I p. 229, is that &ldquo;the universe rotates around the Earth once per day, and in that rotation it carries the stars with it&rdquo;, so that relative to the universe containing them &ldquo;the stars are not moving at all, save for the minuscule movements of their proper motion.&rdquo; On that model, all sources moving together is guaranteed in advance. The test the book proposes as the way to get &ldquo;evidence that the Earth is rotating&rdquo; is therefore a test its own cosmology renders incapable of returning an answer either way. It is offered as a standard science has failed to meet; science meets it thousands of times a year, and on the source&rsquo;s own physics meeting it could never have proved anything. Both halves of that are findings, and the second is the sharper one.</p>

<h4>3. The resolution premise is backwards</h4>

<p>&ldquo;Longer wavelengths create poor resolution&rdquo; is true only with the baseline held fixed, and the baseline is the whole point of the technique. Angular resolution goes as wavelength divided by aperture, and in VLBI the aperture is the separation between antennas. At the standard 8.4&nbsp;GHz the wavelength is 3.57&nbsp;cm; across an 8,000&nbsp;km baseline the fringe spacing is 0.92 milliarcseconds, and across the &ldquo;8000 miles&rdquo; the passage itself pictures, 0.57 milliarcseconds. (Recomputed here 2026-08-10.) Measurement then does better than the fringe spacing, because what is estimated is the centroid of a fringe pattern from a broad synthesised band, not the width of one fringe: ICRF3 reports a noise floor of 0.03&nbsp;mas in individual source coordinates, with 500 sources between 0.03 and 0.06&nbsp;mas. Set the fringe spacing against the number the same book prints at Vol. II p. 248 for Hubble &mdash; 0.05 arcseconds, or 50&nbsp;mas &mdash; and the &ldquo;poor resolution&rdquo; instrument resolves about fifty times finer before any centroiding at all.</p>

<p>The same routine output disposes of the suggestion that a VLBI shift &ldquo;may, indeed, be only a false reading&rdquo;. Phase-referenced VLBI measures trigonometric parallaxes of Galactic masers to typically &plusmn;20 &mu;as, at best &plusmn;5 &mu;as, yielding distances such as 11.1 &plusmn; 0.8 kpc from a parallax of 0.090 &plusmn; 0.006 mas. Whatever one concludes about which body turns, an instrument returning annual parallaxes at that precision is not producing noise.</p>

<h4>4. There is something in the VLBI data that is about the Earth and not about the sky</h4>

<p>The celestial pole&rsquo;s motion contains a free retrograde term with a period of &minus;431.18 &plusmn; 0.10 sidereal days and an amplitude of order 100 &mu;as, extracted from VLBI over 1984&ndash;2011. It is the free core nutation, and it exists because &ldquo;the ellipsoidal liquid core inside the visco-elastic Earth&rsquo;s mantle rotates around an axis which is slightly misaligned with the axis of the mantle.&rdquo; Its period is set by the flattening of the boundary between the Earth&rsquo;s core and its mantle and by the rate at which the Earth turns; it is a resonance of the planet&rsquo;s interior, not a feature of anything overhead.</p>

<p>And it is not only in the sky measurements. The same resonance shows up in diurnal Earth tides recorded by superconducting gravimeters &mdash; instruments in basements, weighing the local pull of gravity, with no astronomical input at all. Rosat and Lambert obtain &minus;429.6 &plusmn; 0.6 days with a quality factor of 16,683 &plusmn; 884 from VLBI nutation, and &minus;426.9 &plusmn; 1.2 days with 16,630 &plusmn; 3,562 from the gravimeters, and conclude that the estimates are &ldquo;comparable within the error bars&rdquo;. The two numbers are close rather than identical, and the honest statement is theirs, not a stronger one. A geocentric reading has to hold that the heavens&rsquo; nutation happens to carry a 430-day resonance matching one independently visible in a gravimeter in Germany.</p>

<p>The ground-based interferometer of item 346 belongs here too, and it points the other way from the item. The 16&nbsp;m<sup>2</sup> ring laser at Wettzell reaches a flicker floor just below one part in 10<sup>8</sup> of the Earth&rsquo;s rotation rate and detected the Chandler and annual wobbles directly, in &ldquo;excellent agreement with the independent measurements by VLBI&rdquo;. A device bolted to bedrock, which never looks at a star, reproduces polar motion derived from quasars. It does not settle rotation against a rotating ether &mdash; that is <a href="#ARG-A02">ARG-A02</a>&rsquo;s argument, and the Sagnac term is frame-dependent in the way geocentrists exploit. What it does settle is that &ldquo;the interferometer is on the ground&rdquo; is not an assumption smuggled into a result; it is a statement about where the instrument is, of the same kind as <a href="#ARG-R08">ARG-R08</a>.</p>

<h4>5. Gaia: the flexibility is real, is bounded, and is published</h4>

<p>Item 347 has a genuine referent. Gaia&rsquo;s global astrometric solution does not fix its own orientation or spin; for EDR3 those were tied down &ldquo;by means of 2269 ICRF3 S/X sources&rdquo; with identified optical counterparts, and the ephemeris of the spacecraft and planets was taken from INPOP10e. So yes: axes imposed from outside, dynamics supplied as input. What follows from that is much less than the item suggests, for three reasons.</p>

<p>First, what is undetermined is <em>orientation and spin of the axes</em>, and parallax is not an orientation. Rotating a catalogue&rsquo;s axes changes no star&rsquo;s distance. Second, the known bias in the parallaxes is measured against objects with a known answer: quasars, whose parallax must be zero, came out at a median of about &minus;17&nbsp;&mu;as in EDR3, and the dependence on magnitude, colour and position was mapped using quasars, LMC stars and physical binaries. Seventeen microarcseconds is the size of the acknowledged error; the parallaxes it sits on run to hundreds of thousands of microarcseconds for nearby stars, and Gaia DR3 publishes 1,467,744,818 of them. Third, and decisively for the charge of circularity, the same reduction was used to measure the observer&rsquo;s own acceleration &mdash; (2.32 &plusmn; 0.16) &times; 10<sup>&minus;10</sup>&nbsp;m/s<sup>2</sup> from about 1.6 million quasars, agreeing at roughly two sigma with the radio value ICRF3 obtained by an entirely different technique. An assumption cannot be confirmed at 25&sigma; by the residuals of the analysis that supposedly assumed it.</p>

<h4>6. The historical claim, since the passage rests weight on it</h4>

<p>The paragraph closes by asserting that &ldquo;recorded history has shown that there is no evidence of any appreciable difference between solar time and sidereal time&rdquo;, and that a geocentric cosmos is a flywheel whose &ldquo;tremendous inertia … can neither be increased or decreased&rdquo;. Read as the claim that the historical record shows no change in the Earth&rsquo;s rotation, it is the one part of the argument that recorded history answers directly. Babylonian, Chinese, Arab and European eclipse timings, reduced against uniform time, give a clock discrepancy of about +17,190 seconds &mdash; nearly five hours &mdash; at 500&nbsp;BC, and a mean solar day lengthening at roughly 1.7&nbsp;ms per century against a tidal expectation of 2.3. The modern instruments say the same on short timescales: the length of day breathes by about a millisecond over a year, with an annual harmonic of 0.34&nbsp;ms peaking on 3 February and a semiannual one of 0.29&nbsp;ms, tracking the angular momentum the atmosphere exchanges with the solid Earth. A flywheel whose rate cannot be increased or decreased does not have a seasonal cycle set by the jet stream.</p>

<h4>7. What the verdict ranges over</h4>

<p>Not the proposition that VLBI settles which body turns; that is conceded above, twice. The cluster asserts that these reductions <em>presuppose</em> the answer and so cannot bear on it, and the finding is that the premises offered for that are false &mdash; the single source, the poor resolution, the unchanged historical record &mdash; while the frame-conventions that are real were named, bounded and measured by the people running the pipelines. The bias in Gaia&rsquo;s parallaxes is 17 microarcseconds and was published by Gaia. The orientation of Gaia&rsquo;s frame comes from ICRF3 and Gaia says so on the page. The solar system&rsquo;s acceleration was measured twice, in two wavebands, by two collaborations. Real data, and a conclusion the data will not carry.</p>""",

    advocate=dict(
        best_defense=(
            "You have conceded the only thing that matters and then buried it under equipment "
            "specifications. Your own section 2 says VLBI cannot separate a turning Earth from "
            "a turning heaven — so every number after that is decoration. Three replies. "
            "First, on our 'own test': read the paragraph in context. It is answering the "
            "specific claim that VLBI measured an earthquake changing the rotation rate, and "
            "JPL admits in your own citation that the change is below what they can measure. "
            "You have taken a remark about one contested measurement and treated it as a "
            "standing challenge about the whole technique, then declared victory by quoting a "
            "review paper about session scheduling. Second, your free core nutation argument "
            "assumes what it proves. The 431-day resonance is a parameter in the MHB nutation "
            "model, which was fitted to the same VLBI data inside a rotating-Earth theory, and "
            "the gravimeter agreement is agreement between two analyses that share that theory "
            "and its tidal model — and your own numbers sit two days apart. That is a "
            "consistency check on a model, not an independent detection of a spinning core. "
            "Third, on Gaia you are cheerful about a pipeline that took its ephemeris from "
            "INPOP, its axes from a radio catalogue, and still had to correct a systematic "
            "offset in the very quantity at issue after the fact. You call that publishing "
            "residuals. We call it a model with enough free parameters to absorb whatever the "
            "sky does. And you have not answered the original point at all: the transformation "
            "your instruments output is a relation between two frames, and which of them "
            "moves is precisely what nobody has measured."),
        survives=4,
        preemptive=(
            "Four, driven by the second and third moves. The first is answerable and already "
            "answered, but the answer must stay in the body and not migrate to a footnote: the "
            "book's own conclusion sentence is general — 'all VLBI measurements are invalid to "
            "prove whether the Earth is rotating' — so the generalisation is the source's, not "
            "ours, and the entry quotes it in the gloss for exactly this reason. Do not let an "
            "editor trim that quotation as redundant; without it this defence lands. "
            "On the second move the defender is partly right and the text must not overclaim: "
            "the FCN paragraph already says the two periods are close rather than identical and "
            "quotes Rosat and Lambert's own word, 'comparable'. Keep it. But add nothing "
            "stronger, and never write that the gravimeters independently confirm the core — "
            "what they show is a resonance at the same frequency in a terrestrial measurement, "
            "which is a coincidence a geocentric reading must absorb rather than a proof it "
            "cannot survive. The load-bearing claim is narrower and safer: the resonance is "
            "parameterised by the Earth's interior, so a moving-heavens account has to explain "
            "why the sky is tuned to the core-mantle boundary. "
            "On the third move, concede the shape and refuse the inference, in the body: yes, "
            "the ephemeris is an input and the bias was found afterwards; the question is "
            "whether the free parameters could have absorbed a stationary Earth, and the answer "
            "is that they demonstrably did not absorb the barycentre's galactic acceleration, "
            "which came out at 25 sigma in the radio and independently in the optical. That "
            "sentence is the reply to 'enough free parameters', and it must sit next to the "
            "concession rather than three paragraphs later. "
            "Finally, do not let anyone upgrade the language on rotation. 'VLBI measures Earth "
            "orientation' is correct; 'VLBI proves the Earth rotates' is not, and a defender "
            "who catches us writing the second gets to discredit the section on the one point "
            "where we agree with him.")),

    straw_man=dict(
        identified=True,
        detail=("The passage tells the reader that NASA and JPL, being satisfied the Earth "
                "rotates, 'find it perfectly justifiable to obtain the VLBI measurement from "
                "only one stellar source', and that this is why they 'can have no means of "
                "determining whether the movement was due to the Earth or the source'. Both "
                "halves misdescribe the practice. A geodetic session runs 24 hours precisely "
                "in order to separate polar motion from nutation, and observes tens to "
                "hundreds of sources; source positions are estimated globally across the whole "
                "four-decade data set while the orientation parameters are estimated session "
                "by session, which is the separation the passage says is never attempted. The "
                "imputed reasoning — that a belief in rotation is what makes the shortcut seem "
                "acceptable — is supplied by the paragraph, not by anything in the analysts' "
                "documentation.")),

    compression=dict(
        assessed=True, drifted=True,
        list_phrasing="VLBI Earth-fixed.",
        source_wording=("&ldquo;The method commonly used is VLBI or Very Long Baseline "
                        "Interferometry. &hellip; because VLBI is commonly used by NASA and JPL "
                        "under the assumption that the Earth is rotating, they find it perfectly "
                        "justifiable to obtain the VLBI measurement from only one stellar "
                        "source.&rdquo;"),
        drift_type="unsourced_addition",
        note=("<strong>This one drifts in the unusual direction, and then adds two items on top "
              "of it.</strong> The source is firmer and far more specific than the list. The "
              "phrase &ldquo;Earth-fixed&rdquo; is the list&rsquo;s; what the passage at Vol. I "
              "pp. 205&ndash;206 argues is that VLBI presupposes rotation, is "
              "run on one source at a time, and is therefore worthless as evidence &mdash; "
              "&ldquo;all VLBI measurements are invalid to prove whether the Earth is "
              "rotating&rdquo;. The three-word item keeps the suspicion and drops both the "
              "checkable premise and the source&rsquo;s own proposed test, which was to observe "
              "&ldquo;at least three sources, if not more&rdquo; and see whether they move "
              "together. Dropping the falsifiable part is what turns an argument that can be "
              "answered into an item that cannot be.<br><br>"
              "<strong>Then the additions.</strong> Item 347 attributes a claim about "
              "Gaia&rsquo;s astrometric reduction to a literature where it is not located: in "
              "the 5.5 MB OCR text of the seventh edition searched for this entry, "
              "<em>Gaia</em> occurs once, inside a quoted ESO press release about dark matter at "
              "Vol. I p. 245. Item 346 widens VLBI to interferometry in general, which is a "
              "<code>scope_widened</code> reading if taken on its own; <code>unsourced_addition</code> "
              "is recorded for the cluster because it is the plainest and most checkable of the "
              "three, and because a reader can verify it with one search.<br><br>"
              "<strong>The refutation answers the source, not the fragment.</strong> It takes up "
              "the circularity charge at full strength, concedes in its own voice that VLBI does "
              "not separate a turning Earth from a turning sky, and puts the weight where the "
              "source put it &mdash; on the number of sources, on resolution, and on whether "
              "recorded history shows the rotation changing. It also records the thing the "
              "compression hides: on the book&rsquo;s own cosmology, where the rotating universe "
              "&ldquo;carries the stars with it&rdquo;, the test the book proposes could not have "
              "returned an answer either way.")),

    verdict_challenge=dict(challenged=False, proposed_verdict=None, reasoning=None),

    people=["PER-SUNGENIS"],
    related=["A02", "A03", "E01", "E08", "R01", "R08", "R11"],

    sources=[
        dict(label="Charlot et al., “The third realization of the International Celestial "
                   "Reference Frame by very long baseline interferometry”, A&A 644:A159 (2020) — "
                   "sessions “24-hour long … a few tens to a few hundreds of sources”; 4,536 "
                   "sources, 303 defining; 6,206 S/X sessions, 1979–2018; noise floor 0.03 mas; "
                   "solar-system acceleration 5.83 ± 0.23 µas/yr at 25σ. The arXiv v1 PDF is the "
                   "copy read for this entry",
             url="https://arxiv.org/abs/2010.13625"),
        dict(label="Gaia Collaboration, Klioner et al., “Gaia Early Data Release 3: Acceleration "
                   "of the Solar System from Gaia astrometry”, A&A 649:A9 (2021) — "
                   "(2.32 ± 0.16)×10⁻¹⁰ m/s², 5.05 ± 0.35 µas/yr, ~1.6 million quasars",
             url="https://www.aanda.org/articles/aa/full_html/2021/05/aa39734-20/aa39734-20.html"),
        dict(label="Lindegren et al., “Gaia Early Data Release 3: The astrometric solution”, "
                   "A&A 649:A2 (2021) — the frame fixed “by means of 2269 ICRF3 S/X sources”; "
                   "ephemeris INPOP10e; 1.468 billion sources with full astrometry",
             url="https://www.aanda.org/articles/aa/full_html/2021/05/aa39709-20/aa39709-20.html"),
        dict(label="Lindegren et al., “Gaia Early Data Release 3: Parallax bias versus magnitude, "
                   "colour, and position”, A&A 649:A4 (2021) — quasars at a median parallax of "
                   "about −17 µas, calibrated against quasars, the LMC and physical binaries",
             url="https://www.aanda.org/articles/aa/full_html/2021/05/aa39653-20/aa39653-20.html"),
        dict(label="Krásná, Böhm & Schuh, “Free core nutation observed by VLBI”, A&A 555:A29 "
                   "(2013) — period −431.18 ± 0.10 sidereal days, amplitude ~100 µas, VLBI "
                   "1984–2011, caused by the ellipsoidal liquid core rotating about an axis "
                   "misaligned with the mantle’s",
             url="https://www.aanda.org/articles/aa/full_html/2013/07/aa21585-13/aa21585-13.html"),
        dict(label="Rosat & Lambert, “Free core nutation resonance parameters from VLBI and "
                   "superconducting gravimeter data”, A&A 503:287 (2009) — −429.6 ± 0.6 d from "
                   "nutation, −426.9 ± 1.2 d from gravimeters, “comparable within the error bars”",
             url="https://www.aanda.org/articles/aa/full_html/2009/31/aa11489-08/aa11489-08.html"),
        dict(label="Schreiber et al., “How to Detect the Chandler and the Annual Wobble of the "
                   "Earth with a Large Ring Laser Gyroscope”, PRL 107:173904 (2011) — 16 m² ring "
                   "at Wettzell, flicker floor just below 10⁻⁸ of the Earth rate, “excellent "
                   "agreement with the independent measurements by VLBI”",
             url="https://link.aps.org/doi/10.1103/PhysRevLett.107.173904"),
        dict(label="Reid & Honma, “Micro-Arcsecond Radio Astrometry” (Ann. Rev. A&A 52:339, 2014) "
                   "— VLBI maser parallaxes at typically ±20 µas, best ±5 µas; 0.090 ± 0.006 mas "
                   "giving 11.1 ± 0.8 kpc",
             url="https://ned.ipac.caltech.edu/level5/March14/Reid/Reid2.html"),
        dict(label="JPL, “Japan quake may have shortened Earth days, moved axis” (2011) — the "
                   "1.8 µs and 17 cm figures are calculated, and “the computed change … is much "
                   "smaller than the accuracy with which scientists can currently measure changes "
                   "in the length of the day”",
             url="https://www.jpl.nasa.gov/news/japan-quake-may-have-shortened-earth-days-moved-axis/"),
        dict(label="Stephenson, Morrison & Hohenkerk, “Measurement of the Earth’s rotation: "
                   "720 BC to AD 2015”, Proc. R. Soc. A 472:20160404 (2016) — the eclipse record "
                   "behind ΔT and the ~1.7 ms/cy lengthening of the mean solar day",
             url="https://royalsocietypublishing.org/doi/10.1098/rspa.2016.0404"),
        dict(label="ΔT (timekeeping) — the smoothed historical value of about +17,190 s at −500, "
                   "and the +1.7 ms/cy observed against a tidal +2.3 ms/cy",
             url="https://en.wikipedia.org/wiki/%CE%94T_(timekeeping)"),
        dict(label="Day length fluctuations — annual LOD amplitude 0.34 ms maximising 3 February, "
                   "semiannual 0.29 ms, driven by atmospheric angular momentum",
             url="https://en.wikipedia.org/wiki/Day_length_fluctuations"),
        dict(label="Sungenis & Bennett, Galileo Was Wrong, 7th ed. (2013), Vols. 1–3 — Internet "
                   "Archive scan; the VLBI paragraph at Vol. I ch. 2, printed pp. 205–206; the "
                   "rotating universe that “carries the stars with it” at Vol. I p. 229; "
                   "“On Telescope Limits” at Vol. II ch. 10, printed p. 248",
             url="https://archive.org/details/galileo-was-wrong-the-church-was-right-sungenis-vol-1-3-complete"),
        dict(label="Sungenis & Bennett, Galileo Was Wrong Vol. I (2006 CD issue) — the text in "
                   "which VLBI is not located; searched for this entry",
             url="https://archive.org/details/GallileoWasWrong"),
    ]),
}
