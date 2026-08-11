# -*- coding: utf-8 -*-
"""Batch 10 — B07. "Refraction is invoked ad hoc to rescue curvature."

ONE item, not three: item 221, "Refraction invoked for curvature." The brief that
commissioned this treatment said three; `assign.ASSIGN` maps exactly one item to B07
and the built dataset agrees (data/flat-earth-origins-provenance.json, cluster B07,
one row, ITEM-221). Reported in record_problems, not edited here.

Cluster record on entry: originator="Samuel Rowbotham", originator_work="Zetetic
Astronomy", year="1849", real_source=None, verdict=MISLEADING. The verdict is
CHALLENGED here — see `verdict_challenge` and note 9. The year is challenged in
record_problems, on the B04 precedent.

Research notes for whoever picks this up next.

1. WHERE THE ARGUMENT ACTUALLY LIVES, AND IT IS NOT WHERE THE RECORD SAYS. The whole
   refraction rebuttal is Zetetic Astronomy, 3rd ed. 1881, ch. II, the block that
   follows EXPERIMENT 9, at printed pp. 31-35 (sacred-texts za14.htm). Read in that
   order it is FOUR moves, not one:
     (a) p. 31 — he accepts a surveyors' allowance and applies it: "The only
         modification which can be made in the above calculations is the allowance for
         refraction, which is generally considered by surveyors to amount to one-twelfth
         the altitude. of the object observed." (the stray full stop is in the
         sacred-texts transcription). In 1881 he attributes it: "which the ordnance
         surveyors have adopted". The 1865 first book edition has the same rule with a
         weaker attribution — "considered by surveyors generally" (Gutenberg #69892,
         Section 13 area). That HARDENING between editions is itself worth a line.
     (b) pp. 31-32 — the shilling-in-a-basin analogy, ending in the rule: "Refraction
         can only exist when the medium surrounding the observer is different to that in
         which the object is placed."
     (c) pp. 32-33 — THE CONTROL EXPERIMENT, which is the hedge and the reason this
         entry exists. "There is no doubt, however, that it is possible for the
         atmosphere to have different temperature and density at two stations six miles
         apart; and some degree of refraction would thence result; but ..." — two
         barometers, two thermometers, two hygrometers, matched, one set carried to each
         end of the sightline, read at three o'clock, notes compared midway. Result: no
         difference. Conclusion, stated FLAT: "Hence it was concluded that refraction had
         not played any part in the observation, and could not be allowed for, nor
         permitted to influence, in any way whatever, the general result." Then the
         Dublin Bay theodolite repeat of 1851, pp. 33-34, same protocol.
     (d) p. 34 — the Encyclopaedia Britannica "Levelling" extract, and then, in his own
         voice: "It will be seen from the above that, in practice, refraction need not be
         allowed for."
   DO NOT quote (c) up to the "but" and stop. That is the hedge rule violated on our
   side. The concession and the flat conclusion travel together and the passage block
   here carries both.

2. THE 1865 / 1881 SPLIT, CHECKED 2026-08-10, DO NOT "CORRECT" BACK.
   Present in the 1865 first book edition (Gutenberg #69892, and the Google scan
   archive.org/details/zeteticastronom00rowbgoog, which is the same edition): the
   Britannica extract in a FULLER form, carrying the formula derivation as well as the
   refraction paragraph; the one-twelfth allowance; and the lens-divergence account of
   "spherical excess" without the word collimation.
   NOT located in that 1865 transcription: "barometer", "hygrometer" (zero hits), and
   the shilling-in-a-basin analogy. The control experiment and the basin analogy are
   located in the 1881 third edition. The 16-page 1849 pamphlet was not reached.

3. THE ANSWER TO THE CONTROL EXPERIMENT, WHICH IS THE LOAD-BEARING PARAGRAPH. His test
   compares the atmosphere HORIZONTALLY, at one height, at the two ends. Terrestrial
   refraction is set by the VERTICAL gradient of refractive index along the ray. Hirt et
   al. 2010 give the working relation, k = 503(p/T^2)(0.0343 + dT/dz), p in hPa, T in K,
   dT/dz in K/m — no term in it is a difference between endpoints. Worse for the test:
   horizontal uniformity is the condition under which a stratified atmosphere refracts
   most REGULARLY, not the condition under which it stops refracting. So the protocol
   returns "no refraction" precisely in the case the standard model handles best.
   This is not hindsight-mongering about Victorian kit — the point is about what the
   test could measure in principle, and the entry says so in his favour.

4. THE ARITHMETIC, ALL OF IT REPRODUCED HERE 2026-08-10.
   (a) k = 1 threshold. Setting k = 1 in Hirt's relation with p = 1013 hPa and
       T = 288 K: 503 x (1013/82944) = 6.1431, so 1/6.1431 = 0.16279, minus 0.0343
       gives dT/dz = +0.128 K/m. About +0.13 degrees per metre of inversion and a
       curved surface photographs flat. Hirt et al. report measured gradients of
       1-2 K/m shortly after sunset and a k range of -4 to +16 at 1.8 m over grass.
       k = 1 is deep inside the routine range, not an exotic case.
   (b) THE COLLIMATION NUMBER, AND IT IS THE BEST THING IN THIS ENTRY. In 1881 he
       relocates the word "refraction" INTO the telescope (ch. II, EXPERIMENT 11,
       p. 41: "there existed a certain degree of refraction, or, as it is called
       technically, 'collimation'") and gives it a magnitude from J. F. Heather,
       A Treatise on Mathematical Instruments, p. 103, as he quotes it: "the maximum
       error being only 1/1000 of a foot" over "ten chains (220 yards)". Under
       TANGENTIAL HORIZON (p. 272) he calls that "fully sufficient" to explain the
       1870 Bedford result. Do the sum: 0.001 ft in 660 ft is 1.515e-6 rad = 0.313
       arcsec; over six statute miles (31,680 ft) that is 0.048 ft, i.e. 0.58 inch.
       THE YARDSTICK, CORRECTED 2026-08-11: it is what curvature produces at that
       range on HIS OWN arithmetic, not a discrepancy he offers collimation against at
       p. 35. At p. 35 the thing he applies to the fig. 3 case is the ATMOSPHERIC
       one-twelfth allowance, and the fig. 3 case (EXPERIMENT 1, pp. 11-13) is one
       where he reports the flag stayed visible and treats that as proof — "Such a
       condition was not observed". So compare against: 11 ft 8 in = 140 inches over
       six miles (EXPERIMENT 1), a factor of 243; 6 ft at three miles (EXPERIMENT 3,
       p. 17), 0.29 in, a factor of 250; and, at the one place he does deploy
       collimation against a reported observation, the 1870 Bedford result at p. 272,
       the "several feet" he says a magnified disc will "appear to be lifted up" —
       order a hundred. Do not re-pair the 240 with p. 35 as a discrepancy he needs to
       absorb; that hands a defender "you sized my substitute against a discrepancy I
       never asked it to explain". Also note WHAT Heather's sentence is: a residual after
       correct adjustment — a tolerance — which Rowbotham converts into a systematic
       divergence the lenses "necessarily produce".
   (c) Cape Bonavista, kept deliberately consistent with ARG-B04 rather than
       recomputed a second way: the curvature term is 8 in x (35-4)^2 = 640.7 ft, and
       the 491 ft he prints is that less the light's own 150 ft. His allowance is
       150/12 = 13 ft. The Britannica's own mean, one-seventh of 640.7, is about 92 ft;
       its strong-refraction figure, one-fifth, about 128 ft. Right kind of number,
       wrong independent variable, roughly seven times too small.
   DO NOT go on to claim refraction closes the Bonavista sighting. It does not, and
   B04 owns why (nominal versus geographic range). Scope stated in section 7.

5. THE NEAREST MODERN FORM IS DUBAY 200 PROOFS #71 AND IT HEDGES TOO. NOT A TRACED
   DESCENT — corrected 2026-08-11, do not re-promote it to "source". "...several news
   channels quickly claimed his picture to be a 'superior mirage' ... While these
   certainly do occur, the skyline in question was facing right-side up and clearly seen
   unlike a hazy illusory mirage, and on a ball-Earth 25,000 miles in circumference
   should be 2,400 feet below the horizon" (as reproduced at flatearth.ws/eric-dubay;
   quote the closing clause too — stopping at the concession is the hedge rule violated
   on our side). He CONCEDES the phenomenon and argues from the appearance of one
   photograph. Item 221 keeps neither the concession nor the photograph, but no line of
   descent has been shown either: the word "refraction" does not occur in the 200 Proofs
   text on that page (searched 2026-08-11; the only hits are site navigation), and item
   221 turns on that word. Treated as a parallel throughout. And his observation is half right in a way that
   costs him: Andrew Young's own taxonomy separates LOOMING — erect, sharp, no inverted
   or multiple images, "and therefore without mirages" — from mirage proper. So the news
   channels used the wrong word and Dubay caught them; the right word names an effect
   that does exactly what he says refraction cannot do. That is the kernel. Be generous
   about it; a lot of debunking really does say "refraction" without a number.

6. REFRACTION PREDATES THE DISPUTE BY CENTURIES AND THIS IS CHECKABLE. Lehn & van der
   Werf, "Atmospheric refraction: a history", Appl. Opt. 44:5624 (2005): Ptolemy's
   Optics Book V has the first detailed model; Tycho "was the first to measure
   atmospheric refraction properly", published 1596; Barentsz saw the Sun at Novaya
   Zemlya "5 deg 26' below the horizon" in January 1597, "the very first report of a
   scientifically documented and recognized mirage", now understood as ducting; Kepler
   accepted Tycho's tables in his 1604 Optics. For the SURVEYING coefficient
   specifically: Gauss's +0.13 comes from reciprocal vertical angles near Hannover, on the
   triangulation he ran through the 1820s — more than two decades before the 1849
   pamphlet. The Metabunk survey of old surveying texts dates the Gaussian coefficient to
   1826; that is a forum source, so the entry says "the 1820s" and rests nothing on the
   exact year.

7. THE FALSIFIABILITY ANSWER, WHICH IS WHAT THE ARGUMENT ACTUALLY DEMANDS. Three
   things make a correction non-ad-hoc and all three hold: it is measurable
   independently of the observation it explains (simultaneous reciprocal vertical
   angles; a thermistor mast; a radiosonde); it is fixed in advance and published (USNO
   builds a fixed 34' of horizontal refraction into the 50' depression that defines
   sunrise, worldwide, computed ahead of the event — quote USNO's own wording, "the
   average amount of atmospheric refraction at the horizon (34 arcminutes)"; the phrase
   "a nominal horizontal refraction of 34 minutes" is ANDREW YOUNG'S, on
   aty.sdsu.edu/explain/sunset_time.html, and was misattributed to USNO until
   2026-08-11); and it can come out wrong. State
   the falsifier explicitly in the body — a distant target photographed far beyond the
   geometric horizon with its BASE visible, undistorted, no vertical stretching, under a
   measured neutral profile. Every Chicago-from-Michigan frame has the lower floors
   missing and the remainder stretched, which is the prediction, not the escape.
   And cite Young against ourselves while doing it: "the refraction at any instant may
   differ by several minutes of arc from the most accurate value that can be
   calculated." The honest position is that the mean is fixed and the excursions are
   not, which is why the entry never says refraction is predictable to the arcsecond.

8. WHAT THIS ENTRY DOES NOT OWN. The lighthouse table and nominal-vs-geographic range:
   ARG-B04. The horizon dip and the three structural tests that kill collimation
   (face reversal, sqrt(h) scaling, area scaling of spherical excess): ARG-B02 — this
   entry adds only the magnitude check, which B02 does not carry. The canal trials
   themselves: ARG-B03. The engineering "no allowance" form: ARG-B05. The list's own
   mirage/ducting items: ARG-B13, already SELF-CONTRADICTED.

9. VERDICT. Challenged, to SELF-CONTRADICTED. The page defines that verdict as "the
   claim's own source, or another item on the same list, points the other way", and
   both limbs are satisfied on documented text: the source prints the coefficient,
   applies an allowance in his own lighthouse table AND inside Experiment 3 ("at an
   altitude, making allowance for refraction"), while the list carries item 263 "Mirage
   optical ducts." as a proof of its own. MISLEADING is defined as "real data, wrong
   conclusion made to look supported", and item 221 is not a data claim at all — it is
   a charge about the opponent's method. Sibling precedent runs the same way: B06 and
   B13 are both SELF-CONTRADICTED, both on this book. Recorded, not applied; the
   refutation is written so that it reads correctly under either label.

10. AMBIGUITY IN THE ITEM, NOTED RATHER THAN RESOLVED. "Refraction invoked for
    curvature." admits a second reading — that refraction is what produces the
    APPEARANCE of curvature. Rowbotham argues that too, at pp. 41-43 and 266-273, with
    the lens divergence. The compression block says so instead of picking one.
"""

ENTRY = {

"B07": dict(

    tldr=("Refraction was not invented to answer flat-earthers. Tycho Brahe measured it in the "
          "1590s, Gauss put the surveying coefficient at about 0.13 in the 1820s, and the US "
          "Naval Observatory computes its published sunrise times with 34 arcminutes of it. "
          "Rowbotham did not deny it either — he printed the coefficient in his own book and "
          "allowed for it in his own experiments. What he did was run a control that measured the "
          "wrong quantity: two thermometers at the two ends of a six-mile sightline cannot see the "
          "vertical temperature gradient that bends the ray. And the divergence-in-the-telescope "
          "he offered instead is, on the only magnitude the chapters read for this entry supply, "
          "about 240 times too small."),

    passage=dict(
        work="WRK-ROWBOTHAM-1865",
        pd=True,
        locator=("Zetetic Astronomy: Earth Not a Globe, 3rd ed. (London: Day, 1881), ch. II, the "
                 "discussion following EXPERIMENT 9, at printed pp. 32–34 (sacred-texts "
                 "transcription za14.htm; the refraction block runs pp. 31–35). The Encyclopædia "
                 "Britannica extract quoted in the gloss is at p. 34 of the same chapter, and in a "
                 "fuller form in the 1865 first book edition (Project Gutenberg #69892). No print "
                 "copy of either edition was consulted. Two stray marks in the sacred-texts "
                 "transcription — a full stop inside “one-twelfth the altitude. of the object "
                 "observed” at p. 31, and an opening quotation mark inside “the line of \"sight "
                 "passes” at p. 34 — are dropped where those sentences are quoted here"),
        quote=("There is no doubt, however, that it is possible for the atmosphere to have "
               "different temperature and density at two stations six miles apart; and some degree "
               "of refraction would thence result; but on several occasions the following steps "
               "were taken to ascertain whether any such differences existed. Two barometers, two "
               "thermometers, and two hygrometers, were obtained, each two being of the same make, "
               "and reading exactly alike. … One of each kind was then taken to the opposite "
               "station, and at three o'clock each instrument was carefully examined, and the "
               "readings recorded, and the observation to the flag, &c., then immediately taken. "
               "… the temperature, density, and moisture of the air did not differ at the two "
               "stations at the time the experiment with the telescope and flag-staff was made. "
               "Hence it was concluded that refraction had not played any part in the observation, "
               "and could not be allowed for, nor permitted to influence, in any way whatever, the "
               "general result.\n\n"
               "[p. 34, after quoting the Encyclopædia Britannica] It will be seen from the above "
               "that, in practice, refraction need not be allowed for. It can only exist when the "
               "line of sight passes from one medium into another of different density; or where "
               "the same medium differs at the point of observation and the point observed."),
        gloss="""<p><strong>Both halves are printed above on purpose.</strong> The concession &mdash; <em>&ldquo;There is no doubt, however, that it is possible &hellip; and some degree of refraction would thence result&rdquo;</em> &mdash; is where a hostile summary would stop, and stopping there would misrepresent him in our favour. He does not leave it as a possibility. He reports a test, and then states the conclusion flat: refraction <em>&ldquo;had not played any part &hellip; nor permitted to influence, in any way whatever, the general result&rdquo;</em>, and, a page later, that <em>&ldquo;in practice, refraction need not be allowed for.&rdquo;</em> That flat conclusion is what has to be answered, and it is what the refutation below answers.</p>

<p><strong>This is a control experiment, and it deserves the name.</strong> Two barometers, two thermometers and two hygrometers, matched against each other at noon so that each pair read alike, one of each carried to the far station, all six read at three o'clock, the sighting taken at that instant, the notes compared midway along the bank afterwards. The 1851 repeat across Dublin Bay, at pp. 33&ndash;34, runs the same protocol with a theodolite on Kingstown Pier and a flag at the Hill of Howth. Whatever else is true of Rowbotham, he did not wave the objection away; he built an apparatus for it. <a href="#ARG-D11">ARG-D11</a> is where the method that produced it is discussed.</p>

<p><strong>He is not against refraction. He allows for it, three separate times.</strong> In the same chapter, at p. 31, he takes an allowance from the surveyors and applies it to every row of his lighthouse table: <em>&ldquo;The only modification which can be made in the above calculations is the allowance for refraction, which is generally considered by surveyors to amount to one-twelfth the altitude of the object observed&rdquo;</em> &mdash; attributed in the 1881 edition to <em>&ldquo;the ordnance surveyors&rdquo;</em>, and in the 1865 first book edition, more loosely, to <em>&ldquo;surveyors generally&rdquo;</em>. In EXPERIMENT 3, in the same chapter, his own theodolite reading is described as falling on the target points <em>&ldquo;at an altitude, making allowance for refraction, equal to that of the observer&rdquo;</em> (the sacred-texts transcription carries no page marker on that page). And at p. 34 he reprints the <em>Encyclop&aelig;dia Britannica</em> article &ldquo;Levelling&rdquo;, which supplies the mechanism &mdash; <em>&ldquo;on account of the unequal densities of the air at different distances from the earth, the rays of light are incurvated by refraction&rdquo;</em> &mdash; and the coefficient: refraction <em>&ldquo;may at a mean compensate for about one-seventh of the curvature of the earth, it sometimes exceeds one-fifth, and at other times does not amount to one-fifteenth.&rdquo;</em> One-seventh is <em>k</em>&nbsp;&asymp;&nbsp;0.14, which is the 7/6 effective-radius rule still in the surveying textbooks. <strong>The number the list says was invented to rescue the globe is printed inside the founding text of the tradition, in both editions, in the same chapter as the argument against it.</strong></p>

<p><strong>The sentence that does not survive contact with the sentence above it.</strong> <em>&ldquo;It can only exist when the line of sight passes from one medium into another of different density&rdquo;</em> is an interface rule. The encyclopaedia paragraph he has just typeset describes a continuous gradient &mdash; air that thins with height, bending the ray all along its length, with no interface anywhere. Those two statements are on facing pages of the same chapter and they cannot both be right. The refutation takes the encyclopaedia's version, because it is the one his critics were actually using and the one that is true.</p>"""),

    steelman=dict(
        description="""<p><strong>SURFACE (weak &mdash; and it will lose).</strong> &ldquo;They don't understand optics; refraction is real, next question.&rdquo; Anyone who opens this way has not read the source and will be shown that within a sentence. Rowbotham reprints the refraction coefficient, cites the mechanism, applies an allowance to his own lighthouse table and to his own theodolite readings, and tested for the effect with matched instruments at both ends of the sightline. He is not ignorant of refraction. He has a position about it.</p>

<p><strong>DEEPER (true, incomplete).</strong> &ldquo;His interface rule is wrong &mdash; refraction happens in a gradient, not only at a boundary.&rdquo; Correct, and it is a real self-contradiction inside his own chapter. But on its own it invites the obvious reply: <em>fine, so there is some bending; you still have not told me how much there was over that canal on that morning, and you cannot, because nobody measured it.</em></p>

<p><strong>KERNEL.</strong> The strongest version is not about optics at all. It is a demand about method, and it runs: <em>you have a correction whose size you do not know, which you apply after the fact, in whatever amount the observation requires. When a distant target is visible that your model says should be hidden, it was refraction. When it is hidden, the atmosphere was standard. Name, in advance, the value for tomorrow. If you cannot, you are not correcting a measurement; you are absorbing a refutation.</em> And the modern literature makes this worse rather than better: Hirt and colleagues, measuring the refraction coefficient at 1.8&nbsp;m over grass with paired total stations at one-minute sampling, found it swinging <strong>between &minus;4 and +16</strong> on sunny summer days, and concluded that &ldquo;the frequently used Gaussian refraction coefficient of +0.13 is not suited for describing refraction effects in the lower atmosphere.&rdquo; A parameter with a working range of twenty, quoted from a geodesy journal rather than from a flat-earth pamphlet, is a serious thing to hand an opponent. The charge also lands on a great deal of actual debunking, which says &ldquo;refraction&rdquo; and stops, having measured nothing.</p>""",
        why_it_doesnt_save_claim="""<p><strong>Because refraction is an observable, and observables can be measured before the thing they explain.</strong> That is the whole difference between a correction and an excuse, and it is not a debating point &mdash; it is a set of instruments. The coefficient is recovered from simultaneous reciprocal vertical angles at the two ends of a line, which is how Gauss got +0.13 near Hannover around 1826 and how Hirt's total stations got their time series in 2008. It is recovered independently from a temperature profile: <em>k</em>&nbsp;=&nbsp;503(<em>p</em>/<em>T</em>&sup2;)(0.0343&nbsp;+&nbsp;&part;<em>T</em>/&part;<em>z</em>), which contains no free constant, only the lab-measured refractivity of air and hydrostatics. Put a thermistor mast or a radiosonde on the path and you have <em>k</em> without looking at the target at all. <strong>The excursions Hirt measured are not evidence that <em>k</em> is unknowable; they are the record of somebody knowing it, minute by minute, for thirty-three hours.</strong></p>

<p><strong>Because it is published in advance, at a fixed value, and used to predict.</strong> The US Naval Observatory defines sunrise and sunset as the moment the Sun's geometric zenith distance reaches 90.8333&deg; &mdash; a depression of 50 arcminutes which the office obtains, in its own words, by adding <em>&ldquo;the average apparent radius of the Sun (16 arcminutes) to the average amount of atmospheric refraction at the horizon (34 arcminutes)&rdquo;</em>. That 34&prime; is not tuned per observation. It is stamped into every rise and set time the office issues, for every latitude, years ahead, and the tables work. A quantity fixed in advance and used to make daily quantitative predictions across the whole planet is not an ad hoc rescue, whatever else it is.</p>

<p><strong>And because refusing it does not leave the argument with no adjustable parameter &mdash; it leaves it with a worse one.</strong> Having declined the atmospheric coefficient, Rowbotham needs something else to explain the theodolite results, and he supplies it: a divergence of the ray inside the telescope, which he calls <em>&ldquo;collimation, or refraction&rdquo;</em> and deploys against the horizon dip, against the 1870 Bedford Level result, and against the spherical excess of the Principal Triangulation of Great Britain. No measurement of it is located in the chapters read for this entry. The one magnitude he does give for it there, borrowed from Heather's <em>Treatise on Mathematical Instruments</em>, is about 240 times too small for the job &mdash; the arithmetic is in the refutation. The kernel's own standard, applied evenly, convicts the substitute long before it convicts the correction.</p>"""),

    refutation="""<p><strong>Concede the method complaint first, because it is a real one.</strong> A correction applied only when it is needed, in whatever amount is needed, would be exactly what this item says it is. Much popular debunking does behave that way: it names refraction, measures nothing, and moves on. If that were all there were, the charge would stick. So the question this entry has to answer is not <em>does light bend</em> &mdash; the source agrees that it does &mdash; but <strong>is the correction fixed independently of the observation it is used on</strong>. Three tests decide that, and refraction passes all three.</p>

<h4>1. It was measured, tabulated and argued about for centuries before anyone disputed the Earth's shape</h4>

<p>Ptolemy's <em>Optics</em>, Book V, already carries a detailed model of atmospheric refraction. Tycho Brahe <em>&ldquo;was the first to measure atmospheric refraction properly&rdquo;</em> and published his results in 1596; Kepler adopted Tycho's tables in his <em>Optics</em> of 1604. The extreme case was recorded before either was in print: in January 1597 Barentsz's party, wintering at Novaya Zemlya, saw the Sun when it was <em>&ldquo;5&deg;26&prime; below the horizon&rdquo;</em> &mdash; what Lehn and van der Werf call <em>&ldquo;the very first report of a scientifically documented and recognized mirage&rdquo;</em>, and what is now understood as optical ducting in a temperature inversion. For the surveying coefficient specifically, Gauss obtained his average value of <em>k</em>&nbsp;&asymp;&nbsp;+0.13 from reciprocal vertical angle measurements near Hannover, on the triangulation he ran through the 1820s. That is more than two decades before Rowbotham's 1849 pamphlet and nearly four before the first book edition. <strong>Nothing in that chronology was produced in response to this argument, because when it was produced this argument did not exist.</strong></p>

<h4>2. It is measured independently of the sighting it is used to explain</h4>

<p>Two routes, neither of which looks at the disputed target. The first is <em>simultaneous reciprocal vertical angles</em>: two instruments at the two ends of a line, each measuring the other's zenith angle at the same instant, from which <em>k</em> falls out directly. That is Gauss's method and it is still the standard one &mdash; Hirt and colleagues ran two pairs of total stations along adjacent lines of sight over five days in 2008 and logged <em>k</em> at one-minute sampling for thirty-three hours. The second route bypasses angles entirely: <em>k</em>&nbsp;=&nbsp;503(<em>p</em>/<em>T</em>&sup2;)(0.0343&nbsp;+&nbsp;&part;<em>T</em>/&part;<em>z</em>), with pressure in hectopascals, temperature in kelvin and the vertical temperature gradient in K/m. Every term is measurable with a barometer, a thermometer and a mast, and the constants come from the laboratory refractivity of air and from hydrostatics, not from any fit to a horizon photograph.</p>

<p>What those measurements show is that the atmosphere near the ground is far more variable than the textbook constant. Hirt et al. report <em>k</em> ranging <strong>from &minus;4 to +16</strong> at 1.8&nbsp;m over grass on sunny summer days, and say so bluntly: the Gaussian +0.13 <em>&ldquo;is not suited for describing refraction effects in the lower atmosphere.&rdquo;</em> This page is not going to hide that number, because it is the best card the argument has. What has to be said alongside it is where the number came from: <strong>a paper whose entire method is measuring the thing minute by minute.</strong> Variability established by measurement is not the same as a free parameter, and it is the opposite of an unmeasured one.</p>

<h4>3. It is fixed in advance and used to predict</h4>

<p>The US Naval Observatory defines sunrise and sunset as the instant the Sun's geometric zenith distance reaches 90.8333&deg;: a depression of 50 arcminutes which the office describes as <em>&ldquo;obtained by adding the average apparent radius of the Sun (16 arcminutes) to the average amount of atmospheric refraction at the horizon (34 arcminutes)&rdquo;</em> &mdash; what Andrew Young, cited below, calls <em>&ldquo;a nominal horizontal refraction of 34 minutes&rdquo;</em>. That 34&prime; is not adjusted per sighting; it is baked into every rise and set time the office publishes, computed years ahead, for every latitude. And the honest limit belongs in the same paragraph, stated by the same community rather than extracted from it: Andrew Young, whose SDSU pages on refraction are cited as the standard reference throughout this review, titles one of them <em>Why We Can't Predict Sunset Times Exactly</em>, because <em>&ldquo;the refraction at any instant may differ by several minutes of arc from the most accurate value that can be calculated.&rdquo;</em> <strong>The mean is fixed and published; the excursions are not predictable.</strong> That combination is what an honest physical correction looks like, and this entry claims nothing stronger.</p>

<h4>4. The control experiment measured the wrong quantity</h4>

<p>This is the paragraph that answers the source rather than the item, and it is the one that matters. Rowbotham's test compared the atmosphere <em>at the two ends</em>: matched barometers, thermometers and hygrometers, one set carried six miles, read at the same hour, notes compared afterwards. They agreed, and he concluded that refraction <em>&ldquo;had not played any part in the observation.&rdquo;</em></p>

<p>But look again at the relation in section 2. Refraction along a near-horizontal ray is set by <strong>&part;<em>T</em>/&part;<em>z</em>, the rate at which temperature changes with <em>height</em></strong>. No term in it is a difference between two stations. A thermometer at eye level at one end and an identical thermometer at eye level at the other can agree perfectly while the air one foot above the water is several degrees colder than the air ten feet above it &mdash; and that vertical structure, not the horizontal comparison, is what bends the ray. His instruments were sampling a direction the effect does not live in.</p>

<p>And the test fails in a second, sharper way, which does not depend on any modern equipment. <strong>Horizontal uniformity is the condition under which a stratified atmosphere refracts most regularly, not the condition under which it stops refracting.</strong> A path whose two ends read alike is a path where the layers run parallel to the surface all the way along &mdash; the textbook case, the one the standard correction is derived for. The protocol could register only a horizontal <em>anomaly</em>, and it returned a null; he read that null as the absence of refraction, when what it indicates is the well-behaved case. Nothing about this requires hindsight about instruments he could not have owned: the geometry of the objection was available in 1881, and the encyclopaedia paragraph on the facing page &mdash; air of <em>&ldquo;unequal densities at different distances from the earth&rdquo;</em> &mdash; states the vertical variable explicitly.</p>

<p>How much bending is available over still water? Set <em>k</em>&nbsp;=&nbsp;1 in the relation above with sea-level pressure and 288&nbsp;K, and the temperature gradient required works out at about <strong>+0.13&nbsp;K per metre</strong> &mdash; recomputed here on 2026-08-10. At <em>k</em>&nbsp;=&nbsp;1 the ray curves with the same radius as the Earth and a curved surface photographs flat. Hirt et al. report measured gradients of <strong>1 to 2&nbsp;K/m shortly after sunset</strong>, an order of magnitude past that threshold, over grass. Nobody recorded the profile over the Old Bedford Canal on the mornings in question, and this entry does not pretend otherwise. The claim is the narrow one: for that geometry &mdash; eye eight inches up, sightline grazing still water for six miles &mdash; a flat null sits well inside the range a curved Earth produces once the profile is allowed the values that are routinely measured, so the null does not pick out a plane. Which is why the experiment that decides is the one that changes the geometry: raise the sightline out of the surface layer and put a marker at the <em>midpoint</em> as well as the ends, so that curvature and a uniform bend make different predictions. Wallace did that in 1870 and Oldham in 1901. <a href="#ARG-B03">ARG-B03</a> owns those trials.</p>

<h4>5. What he put in refraction's place, and what it costs</h4>

<p>Declining the atmospheric coefficient does not leave the argument free of adjustable quantities. It leaves it with one, and the thing worth stopping on is that <strong>the substitute is also called &ldquo;refraction&rdquo;</strong>. At p.&nbsp;41, explaining why a levelled theodolite reads the sea horizon below the cross-hair, Rowbotham writes that in instruments of the best construction <em>&ldquo;there existed a certain degree of refraction, or, as it is called technically, &lsquo;collimation,&rsquo; or a slight divergence of the rays of light from the axis of the eye, on passing through the several glasses of the theodolite.&rdquo;</em> He then uses it as a universal solvent: for the horizon dip, for the Ordnance Survey's spherical excess (pp.&nbsp;263&ndash;264), and, under TANGENTIAL HORIZON at p.&nbsp;272, for the 1870 Bedford Level result, where he calls <em>&ldquo;the well-known and admitted refraction inseparable from the instruments employed &hellip; fully sufficient&rdquo;</em> to explain what the experimenters saw.</p>

<p>The one magnitude he supplies for it, in the chapters read for this entry, is quoted from J. F. Heather's <em>Treatise on Mathematical Instruments</em>: after adjustment the instrument is in order for any distance up to ten chains, <em>&ldquo;the maximum error being only 1/1000 of a foot.&rdquo;</em> Take him at his word and scale it, which is what he does when he says the effect is <em>&ldquo;considerable in distances of several miles.&rdquo;</em> One thousandth of a foot in 660 feet is an angle of 1.5&nbsp;&times;&nbsp;10<sup>&minus;6</sup> radians, about 0.31 arcseconds. Carried over six statute miles &mdash; 31,680 feet &mdash; it comes to 0.048 feet, or <strong>about half an inch</strong>. For collimation to stand in for curvature at these ranges it has to be able to produce what curvature produces there, and the yardstick is his own arithmetic throughout: 11 feet 8 inches over six miles for the boat of EXPERIMENT 1 (the fig.&nbsp;3 case, restated at p.&nbsp;35), 6 feet at three miles for EXPERIMENT 3, and &mdash; at the place where he actually deploys the substitute against a reported canal result, the 1870 Bedford Level trial at p.&nbsp;272 &mdash; the several feet he calls it <em>&ldquo;fully sufficient&rdquo;</em> to account for, writing that a hair's-breadth of dip, magnified, would <em>&ldquo;make it appear to be lifted up for several feet.&rdquo;</em> <strong>His substitute is short by a factor of roughly 240 against the first, roughly 250 against the second, and of order a hundred against the several feet of the third.</strong> (Recomputed here 2026-08-10 from the figures he prints.) Note also what Heather's sentence actually says &mdash; it is a statement of the <em>residual after correct adjustment</em>, a tolerance, which Rowbotham converts into a systematic divergence the lenses <em>&ldquo;necessarily produce&rdquo;</em>. The three structural reasons collimation cannot be the cause of the dip &mdash; it reverses under face-left/face-right, it cannot scale as &radic;<em>h</em>, and spherical excess grows with the area of a triangle while an instrument bias does not &mdash; are set out at <a href="#ARG-B02">ARG-B02</a>. This entry adds only the size, and the size is enough.</p>

<p>The same asymmetry shows in the allowance he does make. <em>&ldquo;One-twelfth the altitude of the object observed&rdquo;</em> is the right kind of number attached to the wrong variable: refraction scales with the square of the <em>distance</em>, not with the height of the target. On his own Cape Bonavista row the curvature term is 8 inches &times; (35&nbsp;&minus;&nbsp;4)&sup2;&nbsp;=&nbsp;641 feet, of which the 491 feet he prints is that figure less the light's own 150 feet. His rule deducts 150/12&nbsp;=&nbsp;13 feet. The <em>Encyclop&aelig;dia Britannica</em>'s own mean, one-seventh of the curvature, would take about 92 feet, and its strong-refraction figure, one-fifth, about 128. He is applying a seventh of the correction his own quoted authority specifies, and attaching it to a different quantity from the one that authority attaches it to. Where the one-twelfth rule came from has not been established here; it is not traced to a named surveying text in this entry, and no substitute origin is offered for it.</p>

<h4>6. What would refute this, named in advance</h4>

<p>The demand behind the item is fair and it deserves an answer in the form it was asked. Refraction lifts distant objects; it does not do so without leaving marks, and the marks are the falsifier.</p>

<ul style="font-family:var(--sans);font-size:.92rem">
<li><strong>Strong lift comes with distortion.</strong> Large positive <em>k</em> compresses, stretches and, past the critical gradient across part of the beam, inverts &mdash; which is why the taxonomy has separate names for looming, towering, stooping and superior mirage. A distant skyline photographed far beyond the geometric horizon <strong>with its bases visible, undistorted, no vertical stretching</strong>, under a measured neutral temperature profile, would falsify the account given here. Nothing answering that description was located in the material surveyed for this entry or for <a href="#ARG-B04">ARG-B04</a>, where the Lake Michigan photographs are examined; the frames looked at there have the lower floors missing and the remainder visibly stretched.</li>
<li><strong>It is episodic and correlated with the weather.</strong> The same target, from the same spot, at the same distance, appears one morning and is gone the next. A plane predicts a visibility limit set by luminous intensity and haze &mdash; monotonic, and indifferent to the temperature profile &mdash; <em>unless it imports the very refraction this item objects to</em>, which is what item 263 does. The observed correlation with the profile is the thing that needs explaining, and it is not a thing a plane with straight sightlines can generate.</li>
<li><strong>It is bounded, and the bound has a signature.</strong> At the coefficients <a href="#ARG-B04">ARG-B04</a> tabulates, 10 and 20 per cent, most of a 442-metre building is still hidden from 56.5 miles across Lake Michigan &mdash; 404 and 364 metres of it, against 453 with no refraction. Making the whole tower visible needs <em>k</em> up near 1, and <em>k</em> near 1 is a duct, which does not arrive quietly: it brings the compression, stretching and multiple imaging listed above. The escape hatch has a fingerprint on it.</li>
</ul>

<h4>7. The modern form of the item, and the concession inside it</h4>

<p>The nearest modern form of the same charge &mdash; not traced here as item 221's source &mdash; is Dubay's proof 71, about Joshua Nowicki's 2015 photograph of the Chicago skyline from across Lake Michigan: news channels called it a superior mirage, and <em>&ldquo;while these certainly do occur, the skyline in question was facing right-side up and clearly seen unlike a hazy illusory mirage, and on a ball-Earth 25,000 miles in circumference should be 2,400 feet below the horizon.&rdquo;</em> Read that carefully, because <strong>he is half right and the half he is right about is the interesting one.</strong> In the standard taxonomy &mdash; Andrew Young's, not one invented for this reply &mdash; an erect, sharp, undistorted lift is <em>looming</em>, and looming is explicitly classified as a refraction anomaly <em>without</em> inverted or multiple images <em>&ldquo;and therefore without mirages.&rdquo;</em> The news channels reached for the wrong word and Dubay caught them at it. But the right word names an effect that raises distant objects into view <em>while keeping them the right way up</em>, which is precisely the thing his objection assumes cannot happen. The true observation points the other way.</p>

<h4>8. Scope, stated plainly</h4>

<p>This entry settles one question: whether the refraction correction is fixed independently of the observations it is applied to. It is. It does <em>not</em> claim that refraction accounts for the long-range sightings in the source's lighthouse table &mdash; correcting his arithmetic leaves Cape Bonavista unexplained by geometry alone, and the reason is that a light list's stated range is a luminous figure rather than a horizon figure. That is <a href="#ARG-B04">ARG-B04</a>'s argument, not this one's. The canal trials are <a href="#ARG-B03">ARG-B03</a>, the dip and collimation are <a href="#ARG-B02">ARG-B02</a>, the engineering &ldquo;no allowance&rdquo; form is <a href="#ARG-B05">ARG-B05</a>. And the list's own position on atmospheric optics is not one position: it carries <em>&ldquo;Mirage optical ducts.&rdquo;</em> as proof item 263, where ducting is the mechanism being asserted, alongside item 221, where invoking it is the offence. <a href="#ARG-B13">ARG-B13</a> is where that pair is scored.</p>""",

    advocate=dict(
        best_defense=(
            "Four moves. First: you have just published, from a geodesy journal, that the "
            "refraction coefficient near the ground runs from minus four to plus sixteen, and "
            "that the standard value is 'not suited' for the layer where every one of these "
            "photographs is taken. That is my case, in your own citation. A quantity with a "
            "working range of twenty, whose value at any particular moment nobody recorded, is "
            "not a correction — it is the width of the goalposts. Second: your own authority "
            "says sunset times cannot be predicted exactly because refraction at any instant may "
            "be off by several arcminutes. So the fixed 34 arcminutes you are so proud of is an "
            "average that is known to be wrong in every individual case, which is the definition "
            "of a fudge applied uniformly. Third: you have convicted Parallax of not owning a "
            "thermistor mast. He ran the best control anybody could run in 1881 — six matched "
            "instruments, simultaneous readings, notes compared blind — and your answer is that "
            "he should have measured a vertical gradient nobody was measuring. By that standard "
            "Wallace's 1870 trial is worthless too: he did not measure the profile either, and "
            "you are happy to accept his result. You apply the modern requirement to the "
            "experiment whose answer you dislike, and waive it for the one you like. Fourth, and "
            "you will not enjoy this one: your collimation arithmetic is a hit on a subsidiary "
            "argument. Grant it. It does not restore your refraction, because I never needed "
            "collimation to be the whole story — I needed the curvature not to be there, and the "
            "flag was still visible. Show me the number for the gradient over that canal on that "
            "morning, or admit that you are back-filling."),
        survives=4,
        preemptive=(
            "Four, and the number is set by moves one and three; two and four are answered "
            "already. Do not soften any of the following. (a) The variability concession must "
            "STAY IN OUR OWN VOICE and stay adjacent to its answer. The body already prints the "
            "minus-four-to-plus-sixteen range and the 'not suited' quotation before answering "
            "them, and the answer is a single sentence that must not be deleted as "
            "throat-clearing: those numbers are the output of a paper whose method is measuring "
            "the coefficient minute by minute, so they establish that k is an observable, not "
            "that it is unknown. If an editor cuts the concession the section becomes the most "
            "attackable on the page. (b) On the third move, concede in public and immediately. "
            "The body was written to say — and must keep saying — that the objection is about "
            "what the protocol could measure IN PRINCIPLE, not about Victorian equipment: a "
            "comparison between two stations at one height contains no term for the vertical "
            "gradient, and horizontal uniformity is the well-behaved case rather than the "
            "refraction-free one. That argument was available in 1881 and is stated on the "
            "facing page of his own book. The Wallace tu quoque is answered by the same "
            "sentence and the answer must be explicit: Wallace's trial is not accepted because "
            "he measured a profile, but because he CHANGED THE GEOMETRY — raised sightline plus "
            "a midpoint marker, so that a uniform bend and a curved surface predict different "
            "things. That is what makes an experiment decide, and it is why section 4 ends on "
            "the midpoint marker rather than on the instruments. (c) Never write that refraction "
            "is predictable to the arcsecond, or that the Bedford null was 'just refraction' as "
            "though the value were known. The entry's position is the narrow one: at k = 1 a "
            "curved surface photographs flat, k = 1 needs about +0.13 K/m, and gradients an "
            "order of magnitude larger are measured after sunset — so the flat null is inside "
            "the predicted range for that geometry. Inside the predicted range is all we claim. "
            "(d) On the fourth move, take the concession and reprice it: the collimation "
            "arithmetic is not offered as a defence of refraction, it is offered as the even "
            "application of his own standard. He demands that a correction not be invoked "
            "without a measured magnitude, and the correction he substitutes has one magnitude "
            "in the chapters read here, off by a factor of 240. Keep those two sentences in the same "
            "paragraph or the point reads as a change of subject.")),

    straw_man=dict(
        identified=True,
        detail=("Yes, and it is the shilling in the basin. At pp. 31–32 the refraction his "
                "critics are said to be invoking is illustrated by a coin lying in a bowl of "
                "water viewed from the air — light crossing a boundary between two media — and "
                "the analogy is then dismissed on the ground that the flag and the observer at "
                "the Bedford Canal were both in the air, so no such boundary exists. Nobody was "
                "arguing that. The mechanism his critics used is the one printed two pages later "
                "in his own book, out of the Encyclopædia Britannica: rays continuously "
                "“incurvated by refraction” by “the unequal densities of the air at different "
                "distances from the earth”, with no interface anywhere on the path. The interface "
                "version is refuted and the gradient version is reported as answered. Our side "
                "has a matching temptation and this entry tries to avoid it: treating the paired "
                "barometers, thermometers and hygrometers as though they were a rhetorical "
                "gesture. They were a control experiment, honestly run, and the objection to them "
                "is about which variable they sampled, not about whether he bothered.")),

    compression=dict(
        assessed=True, drifted=True,
        list_phrasing="Refraction invoked for curvature.",
        source_wording=("&ldquo;There is no doubt, however, that it is possible for the atmosphere to "
                        "have different temperature and density at two stations six miles apart; and "
                        "some degree of refraction would thence result; but on several occasions the "
                        "following steps were taken to ascertain whether any such differences "
                        "existed.&rdquo; &mdash; Rowbotham, 3rd ed. 1881, ch. II, p. 32<br><br>"
                        "&ldquo;&hellip; several news channels quickly claimed his picture to be a "
                        "&lsquo;superior mirage,&rsquo; an atmospheric anomaly caused by temperature "
                        "inversion. While these certainly do occur, the skyline in question was facing "
                        "right-side up and clearly seen unlike a hazy illusory mirage, and on a "
                        "ball-Earth 25,000 miles in circumference should be 2,400 feet below the "
                        "horizon.&rdquo; &mdash; Dubay, <em>200 Proofs</em>, proof 71 "
                        "<em>(printed as a parallel, not as this item's traced source &mdash; see "
                        "below)</em>"),
        drift_type="hedge_dropped",
        note=("<strong>The source hedges and the item does not.</strong> Rowbotham grants that the "
              "atmosphere may differ over six miles and that <em>&ldquo;some degree of refraction "
              "would thence result&rdquo;</em>, then reports a control experiment &mdash; six matched "
              "instruments, simultaneous readings at the two ends &mdash; and only afterwards states "
              "the conclusion flat. Four words on the list carry neither the concession nor the "
              "experiment.<br><br>"
              "<strong>The Dubay text above is a parallel, not a traced source.</strong> Proof 71 is "
              "the nearest modern form of the same charge, and it hedges the same way &mdash; "
              "<em>&ldquo;while these certainly do occur&rdquo;</em> &mdash; before finishing the "
              "sentence flat. But it argues from the appearance of one photograph, it does not use "
              "the word &ldquo;refraction&rdquo; anywhere in the text reproduced at flatearth.ws "
              "(searched 2026-08-11), and no line of descent from it to item 221 is established in "
              "this entry. It is printed here so a reader can see the same concession being made "
              "in the modern literature; the drift type recorded above is computed on the "
              "Rowbotham comparison alone.<br><br>"
              "<strong>Three things travel with the claim in the source and none of them survives.</strong> "
              "<em>The coefficient:</em> at p. 34 Rowbotham reprints the <em>Encyclop&aelig;dia "
              "Britannica</em> article &ldquo;Levelling&rdquo;, which gives him the mechanism and the "
              "number &mdash; refraction &ldquo;may at a mean compensate for about one-seventh of the "
              "curvature of the earth&rdquo;, which is the modern 7/6 rule. <em>The allowance:</em> he "
              "applies a refraction correction to every row of his own lighthouse table and to his own "
              "theodolite reading in Experiment 3. <em>The test:</em> he did not assert that the "
              "correction was unavailable, he tried to measure whether it applied. A reader who meets "
              "only item 221 will think the tradition denies that light bends in air. Its founding text "
              "prints the coefficient for it, twice.<br><br>"
              "<strong>The item is also ambiguous, and the source supports both readings.</strong> "
              "&ldquo;Refraction invoked for curvature&rdquo; can mean <em>refraction is the excuse "
              "used to save curvature</em> &mdash; the cluster's reading, and the one the neighbouring "
              "items support &mdash; or <em>refraction is what produces the appearance of "
              "curvature</em>, which is the argument at pp. 41 and 266&ndash;273, where the dip and "
              "the spherical excess are blamed on a divergence inside the telescope that he also calls "
              "refraction. The compression is loose enough that both are available, and this note "
              "records that rather than picking one.<br><br>"
              "<code>scope_widened</code> was considered and rejected: it would describe the gap "
              "between Dubay's single photograph and the item's standing indictment of a method, "
              "and that is exactly the pairing this entry does not claim to have traced. "
              "<code>hedge_dropped</code> is recorded on the Rowbotham comparison, which is "
              "documented, and the reader has that text above.<br><br>"
              "<strong>The refutation answers the source, not the fragment:</strong> it grants that "
              "the correction is variable at the strength a geodesy journal states it, grants that the "
              "control experiment was honestly run, and puts the weight on what the control could "
              "sample &mdash; a comparison between two stations at one height contains no term for the "
              "vertical temperature gradient that bends the ray &mdash; and on the magnitude of the "
              "mechanism he substitutes.")),

    verdict_challenge=dict(
        challenged=True,
        proposed_verdict="SELF-CONTRADICTED",
        reasoning=(
            "MISLEADING is defined on this page as real data with a wrong conclusion made to look "
            "supported. Item 221 is not a data claim; it is a charge about the opponent's method, "
            "so the definition fits it awkwardly at best. SELF-CONTRADICTED is defined as the "
            "claim's own source, or another item on the same list, pointing the other way, and "
            "both limbs are satisfied on located text. The source: Zetetic Astronomy reprints the "
            "Encyclopaedia Britannica article \"Levelling\" at p. 34 of the 1881 third edition and "
            "at greater length in the 1865 first book edition, which supplies both the mechanism "
            "(rays \"incurvated by refraction\" by \"the unequal densities of the air at different "
            "distances from the earth\") and the coefficient (\"about one-seventh of the curvature "
            "of the earth\"); it applies a refraction allowance to every row of the lighthouse "
            "table at p. 31; and in EXPERIMENT 3 at p. 17 the author's own theodolite reading is "
            "described as taken \"at an altitude, making allowance for refraction\". The list: "
            "item 263, \"Mirage optical ducts.\", asserts atmospheric ducting as a mechanism in "
            "its own right, forty-two items further down the same list from the point where 221 "
            "charges that invoking it is illegitimate. "
            "Sibling precedent runs the same way and on the same book: B06, \"Surveyors assume a "
            "plane and make no allowance\", and B13, \"Mirage and optical ducting explain far "
            "sightings\", are both recorded SELF-CONTRADICTED. Against the change: the item does "
            "carry a genuine methodological complaint about corrections applied without measured "
            "magnitudes, and MISLEADING reads more naturally as a verdict on a complaint than "
            "on a contradiction. That is why this is filed as a challenge rather than treated as "
            "settled. The refutation above is written to read correctly under either label."),
    ),

    people=["PER-ROWBOTHAM", "PER-DUBAY"],
    related=["B02", "B03", "B04", "B05", "B06", "B13", "D11"],

    sources=[
        dict(label="Rowbotham (as “Parallax”), Zetetic Astronomy: Earth Not a Globe, 3rd ed. 1881 — "
                   "ch. II after EXPERIMENT 9, printed pp. 31–35: the one-twelfth allowance, the "
                   "shilling-in-a-basin analogy, “Refraction can only exist when the medium "
                   "surrounding the observer is different…”, the paired barometer/thermometer/"
                   "hygrometer control, the 1851 Dublin Bay repeat, the Encyclopædia Britannica "
                   "“Levelling” extract, and “in practice, refraction need not be allowed for”",
             url="https://sacred-texts.com/earth/za/za14.htm"),
        dict(label="Rowbotham 1881, 3rd ed., ch. II EXPERIMENT 11, printed pp. 41–43 — “there "
                   "existed a certain degree of refraction, or, as it is called technically, "
                   "‘collimation’”, and the Heather quotation, “the maximum error being only "
                   "1/1000 of a foot” over “ten chains (220 yards)”",
             url="https://sacred-texts.com/earth/za/za16.htm"),
        dict(label="Rowbotham 1881, 3rd ed., TANGENTIAL HORIZON, printed pp. 265–273 — “the "
                   "well-known and admitted refraction inseparable from the instruments employed, "
                   "is fully sufficient to explain” the 1870 Bedford Level observation",
             url="https://sacred-texts.com/earth/za/za45.htm"),
        dict(label="Rowbotham 1881, 3rd ed., “SPHERICAL EXCESS”, printed pp. 262–264 — collimation "
                   "offered as the cause of the Ordnance Survey's spherical excess",
             url="https://sacred-texts.com/earth/za/za43.htm"),
        dict(label="Rowbotham 1881, 3rd ed., EXPERIMENT 3, printed p. 17 — his own theodolite "
                   "sighting taken “at an altitude, making allowance for refraction, equal to that "
                   "of the observer”",
             url="https://sacred-texts.com/earth/za/za08.htm"),
        dict(label="Rowbotham, Zetetic Astronomy: Earth Not a Globe! (1865 first book edition), "
                   "Project Gutenberg #69892 — the fuller Encyclopædia Britannica “Levelling” "
                   "extract and the one-twelfth allowance attributed to “surveyors generally”; "
                   "searched 2026-08-10 for “barometer”, “hygrometer” and the basin analogy, none "
                   "of which is located in that transcription",
             url="https://www.gutenberg.org/ebooks/69892"),
        dict(label="Hirt, Guillaume, Wisbar, Bürki & Sternberg, “Monitoring of the refraction "
                   "coefficient in the lower atmosphere using a controlled set-up of simultaneous "
                   "reciprocal vertical angle measurements”, J. Geophys. Res. 115, D21102 (2010) — "
                   "Gauss's +0.13 from reciprocal angles near Hannover; measured k from −4 to +16 "
                   "at 1.8 m over grass; gradients of 1–2 K/m shortly after sunset; "
                   "k = 503(p/T²)(0.0343 + ∂T/∂z); “the frequently used Gaussian refraction "
                   "coefficient of +0.13 is not suited for describing refraction effects in the "
                   "lower atmosphere”",
             url="https://ddfe.curtin.edu.au/models/ERTM2160/pdf/Hirt2010_JGR_D21102_refraction_av.pdf"),
        dict(label="Lehn & van der Werf, “Atmospheric refraction: a history”, Applied Optics "
                   "44:5624 (2005) — Ptolemy's Optics Book V; Tycho “was the first to measure "
                   "atmospheric refraction properly”, published 1596; Kepler's 1604 Optics; "
                   "Barentsz at Novaya Zemlya, January 1597, the Sun “5°26′ below the horizon”, "
                   "“the very first report of a scientifically documented and recognized mirage”",
             url="https://home.cc.umanitoba.ca/~lehn/_Papers_for_Download/history_of_refr.pdf"),
        dict(label="US Naval Observatory, “Rise, Set, and Twilight Definitions” — sunrise and "
                   "sunset at a geometric zenith distance of 90.8333°; the 50-arcminute depression "
                   "“obtained by adding the average apparent radius of the Sun (16 arcminutes) to "
                   "the average amount of atmospheric refraction at the horizon (34 arcminutes)” "
                   "(fetched 2026-08-11)",
             url="https://aa.usno.navy.mil/faq/RST_defs"),
        dict(label="Andrew T. Young (SDSU), “Why We Can't Predict Sunset Times Exactly” — the "
                   "standard 50′ depression as “the sum of an average radius of 16 minutes, and a "
                   "nominal horizontal refraction of 34 minutes”, and “the refraction at any "
                   "instant may differ by several minutes of arc from the most accurate value that "
                   "can be calculated”",
             url="https://aty.sdsu.edu/explain/sunset_time.html"),
        dict(label="Andrew T. Young (SDSU), “Looming” — abnormal refraction raising distant "
                   "objects, “without inverted or multiple images — and therefore without "
                   "mirages”; the erect-image case Dubay's proof 71 assumes cannot occur",
             url="https://aty.sdsu.edu/mirages/mirsims/loom/loom.html"),
        dict(label="Andrew T. Young (SDSU), “The Horizon” — a near-horizontal ray's radius of "
                   "curvature is about 7× the Earth's, handled as an effective radius R′ = R × 7/6",
             url="https://aty.sdsu.edu/explain/atmos_refr/horizon.html"),
        dict(label="Bislin, “Deriving Equations for Atmospheric Refraction” — k = 0.143 (a = 7/6) "
                   "as the geodetic standard and k = 1 as the ducting case where “the earth "
                   "appears flat”",
             url="https://walter.bislins.ch/bloge/index.asp?page=Deriving+Equations+for+Atmospheric+Refraction"),
        dict(label="Bislin, “Rainy Lake Experiment: Refraction Measurements” — refraction "
                   "coefficients measured against survey-grade GNSS positions across sessions, an "
                   "independent determination of k on a real over-water sightline",
             url="https://walter.bislins.ch/bloge/index.asp?page=Rainy+Lake+Experiment%3A+Refraction+Measurements"),
        dict(label="Dubay, 200 Proofs Earth Is Not a Spinning Ball, proof 71 (Chicago skyline "
                   "across Lake Michigan, Joshua Nowicki 2015) — “While these certainly do occur, "
                   "the skyline in question was facing right-side up”; reproduced with rebuttals "
                   "at flatearth.ws",
             url="https://flatearth.ws/eric-dubay"),
        dict(label="Metabunk, “Curvature and Refraction in Surveying and Leveling Through History” "
                   "— nineteenth- and twentieth-century surveying texts giving the refraction "
                   "correction as a fraction of the curvature (Raymond 1901, one-seventh; Breed "
                   "1908, 0.57 ft per mile²), and the Gaussian coefficient of ~0.13 dated to 1826",
             url="https://www.metabunk.org/threads/curvature-and-refraction-in-surveying-and-leveling-through-history-old-books-etc.8856/"),
        dict(label="Bedford Level experiment — Wallace 1870 with a raised sightline and a midpoint "
                   "marker; Oldham 1901",
             url="https://en.wikipedia.org/wiki/Bedford_Level_experiment"),
    ]),
}
