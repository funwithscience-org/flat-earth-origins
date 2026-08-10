# -*- coding: utf-8 -*-
"""Batch 9 — D19. Eclipse and lunar cycles (Saros, Metonic, node, draconic month).

Research notes for whoever picks this up next.

1. THE RECORD SAYS UNTRACED AND THE RECORD IS WRONG. clusters.py carries D19 with
   originator=None, originator_work=None, year=None, real_source=None, verdict
   UNFALSIFIABLE, and the name "Eclipse and lunar cycles are tuned to human
   timekeeping". A search for the design/tuning claim came back with nothing citable.
   A search for the four NAMED QUANTITIES came back immediately, and with a clean
   chain: Rowbotham puts all four in one place — Saros, node, apogee, and the 18-to-19
   year repeat — in the eclipse chapter, and the argument he builds on them is not a
   design claim at all. It is that eclipse prediction is done by cycles rather than by
   theory, so predictive accuracy is no argument for the globe. That claim descends
   intact to Eric Dubay ("Total Eclipse of the Mind", 11 July 2018, which quotes the
   1881 wording) and to the Flat Earth Society wiki page "Astronomical Prediction
   Based on Patterns", whose opening line is "This page will demonstrate that
   prediction in astronomy is based solely on patterns in the sky."
   clusters.py was NOT touched. Six things reported up: originator, originator_work,
   year and real_source (all null), the verdict (see verdict_challenge), and the
   cluster name, which is the field that produced the wrong verdict in the first place.
   D19 sits in the untraced-31 bucket; if the attribution is accepted, the README's
   97-items / 31-clusters figure and the 348-of-461 traced figure both move by 4 items.

2. TWO EDITIONS, AND THEY ARE NOT THE SAME TEXT. The theory-independence paragraph and
   the Saros/node/apogee sentence are both in the 1865 edition — Project Gutenberg
   ebook #69892, Section 9, "Cause of Solar and Lunar Eclipses". The DIY method that
   supplies the Metonic material — tabulate forty years of almanacs, watch the
   eclipses repeat "on arriving to the items of the nineteenth and twentieth years" —
   is in the enlarged third edition of 1881, ch. XI, pp. 130-157, and is not located
   in the 1865 Gutenberg text. The 1881 opening sentence also reads "Those who are
   unacquainted", where 1865 reads "Persons who are unacquainted". This is the
   Rowbotham 1865-vs-1881 trap the curmudgeon file lists as recurring failure 3; the
   locator names which sentence came from which edition and by what route.

3. THE THREE LOAD-BEARING SENTENCES ARE ALL BORROWED FROM ORTHODOX ASTRONOMY.
   Rowbotham footnotes the Saros/node/apogee sentence to Professor Partington's
   Lectures on Natural Philosophy, p. 370; the "precision of astronomy arises, not from
   theories" sentence to Sir Richard Phillips, A Million of Facts, p. 388; and the
   flat "No particular theory is required to calculate Eclipses" to "Somerville's
   'Physical Sciences,' p. 46" — i.e. Mary Somerville, On the Connexion of the
   Physical Sciences, an exposition of Laplace. CAUTION: that sentence is not located
   in the Project Gutenberg transcription of Somerville (ebook #52869, a later
   unnumbered edition whose pagination does not match "p. 46"); an early edition was
   not reachable from here. So the entry attributes it exactly as Rowbotham does and
   no further, and says so in the gloss. Do not upgrade that to "Somerville wrote"
   without page images of an early edition.

4. THE ARITHMETIC IS ALL REPRODUCIBLE AND WAS REDONE HERE. With the standard mean
   months (synodic 29.530589 d, draconic 27.212221 d, anomalistic 27.554550 d):
   223 synodic = 6585.321 d, 242 draconic = 6585.358 d, 239 anomalistic = 6585.537 d.
   The synodic/draconic gap of 0.036 d moves the Moon 0.48 deg past the node each
   repeat, which reproduces NASA's published "about 0.5 deg"; dividing the solar
   eclipse limit window by that drift gives 64-77 repeats, 1162-1395 years, against
   NASA's published 69-87 eclipses over 1226-1550 years. The saros remainder
   0.3213 d is 115.7 deg of Earth rotation, against NASA's "~8 hours or ~120 deg".
   The continued fraction of tropical year / synodic month = 12.368266 is
   [12; 2,1,2,1,1,17,3,196,...], convergents 12/1, 25/2, 37/3, 99/8, 136/11, 235/19,
   4131/334, 12628/1021 — the Metonic is the sixth, and it is good because the NEXT
   partial quotient is 17. Keep the 235/19 residual at 0.087 d (2 h 5 m); do not quote
   NASA's fourth decimal for 223 synodic months alongside a recomputation, because
   their 6585.3223 and the recomputed 6585.3213 differ in the last place and a
   defender will spend the discrepancy rather than the argument.

5. WHERE THE GENUINELY LIVE THING IS, AND IT IS NOT WHERE THE LIST PUTS IT. The limit
   on eclipse prediction today is Delta-T, the difference between dynamical and
   universal time — i.e. the Earth's own irregular rotation. EclipseWise states the
   phase-time error of the lunar theory is "of the order of 1/40 second" and "much
   smaller than the uncertainties in predicted values of Delta-T". Stephenson,
   Morrison & Hohenkerk (Proc. R. Soc. A 472:20160404, 2016) measure the long-term
   change in the length of day at +1.78 +/- 0.03 ms/cy against a tidal prediction of
   +2.3 +/- 0.1 ms/cy, leaving a non-tidal residual, and they say their ~1500-year
   quasi-oscillation "should be treated guardedly" and that extrapolating beyond the
   dataset "is dependent on the reality of the 1500 year oscillation". That is the
   E01 pattern: say it is open, because it is. It also cuts the list's way twice over
   and both directions must be stated — the residual exists only because the Earth
   spins, and it is measured FROM the Babylonian eclipse records the argument cites.

6. THE ADVOCATE'S BEST LINE IS "VSOP87 IS THE CHALDEAN TABLES WITH MORE TERMS", AND IT
   IS GOOD. It is answered in the body rather than left to the reader; see `preemptive`.
   Do not answer it by claiming the ephemerides are unfitted — they are fitted, in
   masses and initial conditions. Answer it on what is fitted versus what is derived.
"""

ENTRY = {

"D19": dict(

    tldr=("Rowbotham's actual claim is that eclipses are predicted from repeating cycles "
          "rather than from any theory of the solar system, and for Babylonian practice "
          "that is true — so what is wrong here is an inference, not a mystery. The four "
          "list items say something else: that the cycles are locked and tuned. They are "
          "neither. The Saros slips about half a degree off the lunar node every repeat, "
          "which is why eclipse series are born, run for roughly 69 to 87 eclipses and "
          "die; the Metonic cycle is a continued-fraction convergent that arithmetic hands "
          "you free, and the humans picked the one short enough to check inside a "
          "lifetime. What "
          "actually limits eclipse prediction now is not gravity but ΔT — the Earth's own "
          "irregular rotation — and the size of that residual is an open measurement."),

    passage=dict(
        work="WRK-ROWBOTHAM-1865",
        pd=True,
        locator=("Zetetic Astronomy: Earth Not a Globe (London: Simpkin, Marshall, 1865), "
                 "Section 9, “Cause of Solar and Lunar Eclipses” — read from the Project "
                 "Gutenberg transcription, ebook #69892. The same three sentences stand in "
                 "the enlarged 3rd ed. of 1881 at ch. XI, pp. 130–157 (sacred-texts scan, "
                 "za29.htm), where the first opens “Those who are unacquainted” rather than "
                 "“Persons who are unacquainted”. Rowbotham's own footnotes: the Saros "
                 "sentence is his quotation of Professor Partington, Lectures on Natural "
                 "Philosophy, p. 370; the last sentence is footnoted “Somerville's ‘Physical "
                 "Sciences,’ p. 46”. Not checked against a print copy of either edition."),
        quote=("Persons who are unacquainted with the methods of calculating Eclipses and "
               "other astronomical phenomena, are prone to look upon the correctness of "
               "these calculations as powerful arguments in favour of the doctrine of the "
               "Earth's rotundity and the Newtonian philosophy generally. But this is "
               "erroneous. Whatever theory is adopted, or if all theories are discarded, "
               "the same results may follow, because the necessary data may be tabulated "
               "and employed independently of all theory…\n\n"
               "The Chaldeans, however, must have made a long series of observations "
               "before they could discover their “Saros” or lunar period of 6,585⅓ days, "
               "or about 18 years; at which time, as they had learnt, the place of the "
               "Moon, her node and apogee return nearly to the same situation with "
               "respect to the Earth and the Sun, and, of course, a series of nearly "
               "similar Eclipses occur.\n\n"
               "“No particular theory is required to calculate Eclipses; and the "
               "calculations may be made with equal accuracy independent of every "
               "theory.”"),
        gloss="""<p><strong>Read what the argument is for.</strong> Rowbotham is not saying the lunar cycles are tuned to anything. He is making an epistemological claim about a method: eclipse prediction runs on tabulated recurrences, so the fact that it works is not a vote for the Newtonian picture. Every one of the four quantities the list names — the node, the Saros, the nineteen-year repeat, the return to the node — is in this chapter, and none of them is offered as a marvel. They are offered as bookkeeping, and bookkeeping is exactly what he wants them to be.</p>
<p><strong>Whose sentences these are.</strong> The three that carry the weight are all borrowings from the astronomy he is arguing against. The Saros sentence, with its <em>node</em> and <em>apogee</em>, is Rowbotham quoting Professor Partington&rsquo;s <em>Lectures on Natural Philosophy</em> at p. 370. Between them sits Sir Richard Phillips, <em>A Million of Facts</em>, p. 388: &ldquo;The precision of astronomy arises, not from theories, but from prolonged observations, and the regularity of the motions, or the <em>ascertained uniformity of their irregularities</em>.&rdquo; That last clause is the whole of celestial mechanics described by a hostile witness who did not notice what he had said &mdash; the irregularities are the perturbations, and ascertaining their uniformity is what the theory is <em>for</em>.</p>
<p><strong>On the Somerville footnote, at Rowbotham&rsquo;s strength and no further.</strong> The flat sentence &mdash; the one the modern versions quote &mdash; is footnoted to &ldquo;Somerville&rsquo;s &lsquo;Physical Sciences,&rsquo; p. 46&rdquo;, meaning Mary Somerville&rsquo;s <em>On the Connexion of the Physical Sciences</em>, a book written to expound Laplace&rsquo;s celestial mechanics to a general reader. That sentence is not located in the Project Gutenberg transcription of Somerville (ebook #52869), which is a later and much enlarged edition whose pagination cannot match &ldquo;p. 46&rdquo;; an early edition was not reachable from here. So this page reports the attribution as Rowbotham printed it and does not assert that Somerville wrote it. What is not in doubt is the shape of the borrowing: the flat-earth case on eclipses is built out of quotations from people who held the Earth to be a globe going round the Sun.</p>
<p><strong>What 1881 added.</strong> The third edition expands the chapter with a do-it-yourself recipe &mdash; collect forty years of almanacs, tabulate the eclipses, and &ldquo;on arriving to the items of the nineteenth and twentieth years, he will perceive that some of the eclipses in the earlier part of the table will have been now repeated&rdquo;. That paragraph is not located in the 1865 Gutenberg text, and it is the one Eric Dubay reproduces in 2018. It is also where the list&rsquo;s item 365 comes from: the nineteen-year repeat is the Metonic cycle, arrived at by counting rather than by naming.</p>
<p><strong>Where it travels, and where it did not.</strong> The words &ldquo;Saros&rdquo;, &ldquo;Metonic&rdquo; and &ldquo;node&rdquo; are not located in the Project Gutenberg text of Carpenter&rsquo;s <em>One Hundred Proofs that the Earth Is Not a Globe</em> (1885, ebook #55387), the pamphlet that gave this genre its numbered format. So this material did not reach the modern list through the Victorian proof-list at all: it stayed in Rowbotham&rsquo;s prose chapter for a century and was lifted back out of it directly &mdash; by Dubay in 2018, quoting the 1881 paragraph, and by the Flat Earth Society wiki, which cites Rowbotham&rsquo;s chapter by name. That is a small but clean piece of evidence for the project&rsquo;s general finding: the distributors are not copying each other so much as returning to the same few originals.</p>""",),

    steelman=dict(
        description="""<p><strong>SURFACE (weak &mdash; do not use).</strong> &ldquo;The Babylonians could not really predict eclipses.&rdquo; They could. Ptolemy preserved Babylonian timings of three lunar eclipses from about 719 BC and used them to fix the Moon&rsquo;s mean motion &mdash; a fact this page learned from Rowbotham&rsquo;s own quotation. Equally weak: &ldquo;the Saros is just a coincidence, so there is nothing to explain.&rdquo; That concedes the interesting half of the question and answers none of the four items.</p>
<p><strong>DEEPER.</strong> Prediction by recurrence genuinely works, for a while, without any commitment about what is orbiting what. This is not a flat-earth insight; it is the standing instrumentalist reading of Ptolemaic astronomy, and it is what Osiander&rsquo;s unsigned preface to <em>De revolutionibus</em> says in 1543. A defender who says only this has said something no historian of astronomy will contest.</p>
<p><strong>KERNEL.</strong> The strongest version is Rowbotham&rsquo;s own and it is a claim about the logic of evidence, not about the sky. <em>Predictive success underdetermines the mechanism.</em> A kinematic scheme fitted to past positions can reproduce future positions while remaining silent, or wrong, about causes; Ptolemy&rsquo;s tables did it for centuries. So &ldquo;we predicted the eclipse to the second, therefore the Earth is a globe&rdquo; is not a valid inference standing alone, and Rowbotham was right to say the naive form of it proves nothing. He is also right, and unusually careful, about who he is aiming at: his sentence names &ldquo;persons who are unacquainted with the methods of calculating eclipses&rdquo;. He is attacking a popular argument, and he says so. Concede the logic, concede the history, and concede the target.</p>""",
        why_it_doesnt_save_claim="""<p>Because the concession is about <em>prediction by recurrence</em>, and none of the four items is about that. They assert that the recurrences are <strong>locked</strong> and <strong>tuned</strong> &mdash; and a lock is a physical claim with an observable consequence, which is that it does not come apart. These do. The Moon arrives about half a degree past its node on each Saros repeat, so an eclipse series drifts across the eclipse window, runs 69 to 87 eclipses over 1226 to 1550 years, and stops; new ones start. Locks do not have birth dates and death dates, and these are catalogued.</p>
<p>And the underdetermination argument cannot be spent here anyway, because the four quantities the items name are <em>defined inside the model being rejected</em>. A node is where an inclined orbital plane crosses the ecliptic. A draconic month is the time to return to that node. Neither term has a referent without a Moon on a tilted orbit around a body that also orbits the Sun. The items borrow the globe model&rsquo;s vocabulary to argue against it, which is why their own numbers can be checked against the theory&rsquo;s predictions &mdash; and they agree.</p>
<p>Finally, the historical claim has an expiry date that has passed. Prediction by cycle was the state of the art when Rowbotham wrote. It is not the method now, and the modern method is quoted below in its own words.</p>"""),

    refutation="""<p><strong>First, concede the history, because it is his and it is correct.</strong> Eclipses were predicted from recurrences long before anyone had the mechanism. Ptolemy preserved Babylonian timings of lunar eclipses from around 719 BC; the Saros gives reliable warning of lunar eclipses and of solar eclipse <em>possibilities</em>; and none of that requires knowing what orbits what. The general point behind it is stronger still and is not a flat-earth invention: a scheme fitted to past positions can reproduce future ones while saying nothing true about causes. Anyone who answers this argument with &ldquo;we predicted it, therefore globe&rdquo; has walked into the one trap Rowbotham actually set.</p>

<p><strong>Second, what the Saros is, in numbers, because the numbers answer three of the four items by themselves.</strong> The cycle exists because three different lunar months nearly &mdash; not exactly &mdash; agree. Using the standard mean values, 223 synodic months come to 6585.321 days, 242 draconic months to 6585.358 days, and 239 anomalistic months to 6585.537 days. NASA publishes the same three commensurabilities and the same summary: &ldquo;a period of approximately 6,585.3 days (18 years 11 days 8 hours)&rdquo;. Note what the spread means. The three totals disagree by about a fifth of a day, and that disagreement is not noise around a lock &mdash; it <em>is</em> the mechanism by which the pattern decays.</p>

<p><strong>Third, item 363, &ldquo;lunar node locks.&rdquo; It is the one item here that makes a claim we can watch fail.</strong> The synodic-to-draconic gap of 0.036 days puts the Moon about 0.48&deg; past the node on each repeat &mdash; recomputed here, and the same half-degree NASA reports when it writes that &ldquo;the Moon&rsquo;s node shifts eastward by about 0.5&ordm; with each cycle&rdquo;. A solar eclipse is possible while the New Moon falls within the ecliptic limits, which the same predictors give as ranging &ldquo;from 15.39&deg; to 18.59&deg; because of the eccentricity of the Moon&rsquo;s (and Earth&rsquo;s) orbit&rdquo;. Divide that window by the drift and a series survives 64 to 77 repeats, or 1162 to 1395 years, before it walks out of the window entirely; NASA&rsquo;s catalogued figure, counted from the actual series, is 69 to 87 eclipses over 1226 to 1550 years. A back-of-envelope division landing that close to the catalogue is the sign that the decay mechanism is understood, not mysterious. Their own explanation is the flat contradiction of the item: &ldquo;A Saros series doesn&rsquo;t last indefinitely because the three lunar months are not perfectly commensurate with one another.&rdquo; Saros series are numbered, dated, born and buried. Whatever that is, it is not a lock.</p>

<p><strong>Fourth, item 364, &ldquo;Saros cycle human time.&rdquo; This one is backwards on its face.</strong> The Saros is 6585&#8531; days. The awkward third of a day is the defining feature: it is 115.7&deg; of Earth rotation &mdash; NASA rounds it to &ldquo;~8 hours or ~120&ordm;&rdquo; &mdash; so the next eclipse in a series lands roughly a third of the way round the planet from the last one. That is precisely what a cycle fitted to human timekeeping would <em>not</em> do. It fits no calendar unit, it does not close on a whole day, and the ancients had to stack three Saroses into the <em>exeligmos</em> of 19,756 days to get the geography back. A period whose most famous property is that it does not divide into days is a poor candidate for a period tuned to days.</p>

<p><strong>Fifth, item 365, &ldquo;Metonic precision.&rdquo; The precision is a theorem, and the choice was human.</strong> Nineteen tropical years run 6939.602 days and 235 synodic months run 6939.688 days &mdash; a gap of 0.087 days, about two hours. It is a striking fit and it needs no designer, because it is what continued fractions do. The ratio of the tropical year to the synodic month is 12.368266, whose continued-fraction expansion begins [12; 2, 1, 2, 1, 1, 17, 3, 196, &hellip;], and whose convergents run 12/1, 25/2, 37/3, 99/8, 136/11, <strong>235/19</strong>, 4131/334, 12628/1021. The Metonic cycle is the sixth convergent, and it is unusually good for its size for a purely arithmetical reason: the next partial quotient is 17, and a large partial quotient always leaves the convergent before it looking uncannily exact. Better ones exist and nobody built a calendar on them. Wait 334 years and the error falls to 41 minutes; wait 1021 and it falls to under 3 minutes. Those are more precise and they are useless, because a calendar has to be checkable by the people using it. Meton introduced the 19-year scheme at Athens in 432 BC and the Babylonians had standardised a 19-year intercalation in the late sixth century BC; Callippus quadrupled it to 76 years and dropped a day. The tuning in this story was done by astronomers picking from a list that arithmetic handed them, and the calendars were then cut to fit &mdash; which is the opposite of the item&rsquo;s direction of travel.</p>

<p><strong>Sixth, item 366, &ldquo;draconic month tuning.&rdquo; The draconic month is an output of the theory the argument says is unnecessary.</strong> It differs from the sidereal month because the Moon&rsquo;s nodes regress under the Sun&rsquo;s pull, completing a circuit of the ecliptic in 18.612958 years (6798.383 days). That regression is not fitted; it is derived. And the closely related quantity &mdash; the precession of the lunar perigee, 8.848 years &mdash; is where Newtonian gravity came closest to dying. Clairaut&rsquo;s first-order solution in 1747 made the perigee precess at the same rate as the node regresses, about half the observed value, and the discrepancy was resolved only by carrying the expansion to higher order. Worked to that order the theory returns 8.728 years against 8.848 observed, and 18.704 against 18.615. Those two numbers are the argument&rsquo;s own vocabulary being predicted, from the mechanism it says is not required, in the hardest case the mechanism ever faced.</p>

<p><strong>Seventh, how eclipses are actually predicted now &mdash; in the predictors&rsquo; own words.</strong> The modern canons do not use the Saros. The published method for the five-millennium catalogues takes the Sun from &ldquo;VSOP87 theory constructed by P. Bretagnon and G. Francou [1988]&rdquo; and the Moon from &ldquo;theory ELP-2000/82 of M. Chapront-Touze and J. Chapront [1983]&rdquo; &mdash; solutions of the equations of motion, not tables of recurrences. The Saros survives as an <em>index</em>, a way of filing eclipses into families, which is a different job from computing one. And the residual error of the lunar theory in those predictions is stated as &ldquo;of the order of 1/40 second&rdquo;.</p>

<p><strong>Eighth, and this is the part that is genuinely open, so say so plainly.</strong> That 1/40 second is not the limit on the prediction. The predictors say their timing errors are &ldquo;much smaller than the uncertainties in predicted values of &Delta;T&rdquo;, and &Delta;T is the gap between uniform dynamical time and the time kept by the turning Earth. It is not derivable; it has to be measured, and for antiquity it is measured from ancient eclipse records &mdash; the same Babylonian, Chinese, Greek and Arab observations this argument invokes. Stephenson, Morrison and Hohenkerk (<em>Proc. R. Soc. A</em> 472:20160404, 2016) analysed 720 BC to AD 2015 and found the length of day increasing at +1.78 &plusmn; 0.03 ms per century, against a tidal-braking prediction from lunar laser ranging of +2.3 &plusmn; 0.1 ms per century. The difference is a real non-tidal residual, usually attributed to post-glacial rebound and core&ndash;mantle coupling, and it is not settled. The authors are careful about the rest too: their ~1500-year quasi-oscillation &ldquo;should be treated guardedly&rdquo;, and extrapolating the length of day beyond the data &ldquo;is dependent on the reality of the 1500 year oscillation&rdquo;. So the honest statement is that the biggest uncertainty in predicting an eclipse is an unresolved question about the Earth&rsquo;s rotation &mdash; and that fact runs against the list in both of its parts, because the residual exists only if the Earth spins, and the record used to measure it is the eclipse archive the argument cites as theory-free.</p>

<p><strong>Ninth, what eclipse prediction actually discriminates &mdash; and it is not the <em>when</em>.</strong> Rowbotham is right that the date and hour of an eclipse can be got from recurrences. The Saros cannot give the <em>where</em>: its third-of-a-day remainder throws the next one roughly 116&deg; of longitude away, so placing the shadow requires the rotation rate of the body the shadow falls on. What the modern canons publish is an umbral track &mdash; a central line in latitude and longitude on a specified reference ellipsoid, contact times to the second, and the duration of totality at each point &mdash; decades ahead, and it is met. That prediction is a statement about the shape of the surface intercepting the shadow and the rate at which it turns. It is not a cycle, and it is not neutral between models.</p>

<p><strong>Verdict, stated where the disagreement is.</strong> There is a real argument here and it is not unfalsifiable. Its factual core &mdash; that eclipses were once predicted by recurrence without a mechanism &mdash; is true, and its inference does not follow: from &ldquo;this particular argument for the globe is weak&rdquo; nothing whatever follows about the shape of the Earth, and from four near-commensurabilities that visibly decay nothing follows about tuning. This treatment&rsquo;s writer thinks the scorecard label is the wrong one and has recorded the disagreement rather than writing around it; it is in the panel below.</p>""",

    advocate=dict(
        best_defense=(
            "You have spent nine paragraphs agreeing with me and one paragraph changing the "
            "subject. My claim was never that the Moon was tuned by somebody. It is that the "
            "accuracy of eclipse prediction is not evidence for your model, and you concede "
            "that in your first sentence. So take the concession seriously and look at what "
            "you offered instead. VSOP87 and ELP-2000/82 are trigonometric series with "
            "thousands of fitted terms, constructed to reproduce an observational record and "
            "then run forward. That is what my tables were, with worse arithmetic. Calling "
            "yours a 'solution of the equations of motion' does not change what it is doing. "
            "Then your own eighth section hands me the case. You admit the limiting quantity "
            "is Delta-T; you admit Delta-T cannot be derived; you admit it is fitted to the "
            "ancient eclipse records — my records, the ones I said were the real source of "
            "the precision — and you admit the residual after tidal braking is unexplained "
            "and that the periodicity your own authors fitted 'should be treated guardedly'. "
            "So the honest summary of your position is that your theory predicts eclipses "
            "except for the part that matters, which you get by fitting to the observations, "
            "which is my method wearing a lab coat. Sir Richard Phillips said it in the "
            "sentence you quoted against me and I will take it as it stands: the precision "
            "of astronomy arises not from theories but from prolonged observations."),
        survives=4,
        preemptive=(
            "Four, and the number is set by the second and third moves, not the first. Three "
            "concrete changes. (a) The 'VSOP87 is my tables with more terms' hit has to be "
            "answered in the body, and NOT by claiming the ephemerides are unfitted — they "
            "are fitted, and a defender who knows that will use an overclaim to discredit "
            "the section. Answer it on the ratio of fitted to derived: what is fitted is a "
            "small set of constants (masses, and the initial position and velocity of each "
            "body), and what comes out is the entire structure of periodic terms — their "
            "frequencies, amplitudes and phases — which is not adjustable once the constants "
            "are set. A recurrence table has as many free parameters as it has entries; a "
            "dynamical solution has a few dozen, and is then obliged to get the rest right "
            "or fail. The Clairaut case in section six is the demonstration and should be "
            "cross-referenced explicitly at that point: the perigee rate could not be fitted, "
            "it came out wrong by a factor of two, and it nearly killed the theory. Nothing "
            "in a Chaldean table can be wrong by a factor of two, because nothing in it is "
            "predicted. (b) The Delta-T concession must not be softened, but its scope must "
            "be stated in the same breath or it reads as the surrender the defender says it "
            "is: Delta-T is ONE scalar function of time, the accumulated phase of the "
            "Earth's rotation, constrained by hundreds of independent records and used "
            "unchanged across eclipses, occultations and transits. It is not a per-eclipse "
            "adjustment, and a model that needed one free number per prediction would be the "
            "recurrence table, not the ephemeris. Add that sentence to section eight. "
            "(c) On the Phillips quotation, concede the rhetorical point and take the clause "
            "he wrote next — 'the ascertained uniformity of their irregularities' — because "
            "that is the sentence conceding that the deviations are lawful, which is the "
            "whole claim. Do not accuse Phillips of anything; he was writing a book of facts "
            "and this is a fair reading of his own words. Finally, on tone: the defender is "
            "right that we agree with Rowbotham about the inference from predictive success, "
            "and the page should say that in the first paragraph rather than the ninth. It "
            "does."),
    ),

    straw_man=dict(
        identified=True,
        detail=("Half a straw man, and the missing half is the interesting part. Rowbotham "
                "names his target honestly - he writes that it is 'persons who are "
                "unacquainted with the methods of calculating eclipses' who treat predictive "
                "accuracy as proof of the Earth's rotundity, which is a fair description of a "
                "popular argument and not of anything an astronomer publishes. The case "
                "actually made from eclipses is about the geometry of the umbral track on a "
                "turning body, and the case made from the lunar cycles is that their rates "
                "are derived from the dynamics rather than fitted. Neither is addressed. The "
                "list then deletes the qualification, so a paragraph that carefully limited "
                "itself to the uninformed version arrives as a general refutation. That "
                "deletion is the list's doing, not Rowbotham's.")),

    compression=dict(
        assessed=True, drifted=True,
        list_phrasing=("Lunar node locks. / Saros cycle human time. / Metonic precision. / "
                       "Draconic month tuning."),
        source_wording=("“Whatever theory is adopted, or if all theories are discarded, the same "
                        "results may follow, because the necessary data may be tabulated and "
                        "employed <em>independently of all theory</em>… The Chaldeans, however, "
                        "must have made a long series of observations before they could discover "
                        "their ‘Saros’ or lunar period of 6,585⅓ days, or about 18 years; at "
                        "which time… the place of the Moon, her <em>node</em> and <em>apogee</em> "
                        "return nearly to the same situation.”"),
        drift_type="category_shifted",
        note=("The source is making a claim about a <em>method of calculation</em>: that eclipse "
              "prediction runs on tabulated recurrences, so its accuracy is not an argument for "
              "the Newtonian system. That is a historical and epistemological claim, and in its "
              "own domain it is largely right. The four list items make a <em>physical</em> claim "
              "about the cycles themselves &mdash; that the node <strong>locks</strong>, that the "
              "Saros is fitted to <strong>human time</strong>, that the draconic month is "
              "<strong>tuned</strong>. Rowbotham&rsquo;s chapter supplies every one of the four "
              "quantities and none of the four assertions; the words &ldquo;locks&rdquo; and "
              "&ldquo;tuning&rdquo; are the list&rsquo;s, and they reverse the argument they came "
              "from. He wanted the cycles to be <em>mere</em> bookkeeping, dull enough that no "
              "theory was needed to run them. The list wants them to be marvels. "
              "<strong>The refutation above answers his version first</strong> &mdash; it concedes "
              "the underdetermination point outright, concedes the Babylonian history, and puts "
              "the weight on what the modern method actually is &mdash; and only then answers the "
              "four items on their own terms, which is where the near-commensurabilities turn out "
              "to be visibly decaying rather than locked. Two further compressions are worth "
              "recording. The source&rsquo;s own qualifier, that the bad inference belongs to "
              "&ldquo;persons who are unacquainted with the methods of calculating eclipses&rdquo;, "
              "is dropped. And the three sentences the argument rests on are all Rowbotham "
              "quoting orthodox nineteenth-century astronomy &mdash; Partington, Sir Richard "
              "Phillips, and a footnote to Somerville &mdash; which the compressed items leave no "
              "room to show, so a reader meets as flat-earth doctrine a passage that is mostly "
              "other people&rsquo;s textbooks.")),

    verdict_challenge=dict(
        challenged=True,
        proposed_verdict="MISLEADING",
        reasoning=("UNFALSIFIABLE is the wrong label and the cluster name is the reason it was "
                   "chosen. The name reads the four items as a design claim - cycles 'tuned to "
                   "human timekeeping' - and a design claim is indeed unfalsifiable. But a search "
                   "for a source that makes the design claim returned nothing citable, while a "
                   "search for the four named quantities returned a documented lineage in one "
                   "chapter: Rowbotham's eclipse chapter, where the Saros, the node, the apogee "
                   "and the nineteen-year repeat all appear, and where the argument built on them "
                   "is that eclipse prediction is theory-independent. That argument descends "
                   "intact to Dubay in 2018 and to the Flat Earth Society wiki. It is checkable, "
                   "and it has been checked: its factual core about ancient practice is true, and "
                   "the inference from it does not follow, which is what MISLEADING is for on "
                   "this page. Taken as claims about the cycles themselves the items are not "
                   "unfalsifiable either - they are falsified, since the Saros drifts about half "
                   "a degree off the node per repeat and its series are catalogued as beginning "
                   "and ending. A reasonable second opinion is SELF-CONTRADICTED, on the ground "
                   "that a node and a draconic month are quantities defined only by an inclined "
                   "orbital plane crossing the ecliptic, so the items cite the globe model's own "
                   "measurements against it; that reading is recorded here but not proposed, "
                   "because the primary source is arguing about method rather than about the "
                   "cycles and MISLEADING fits the source better. This is a proposal only: "
                   "clusters.py was not edited. Four further fields in that record are reported "
                   "up rather than changed - originator, originator_work, year and real_source "
                   "are all null for a cluster that now has a named author, a dated work and an "
                   "identifiable real astronomy behind it."),
    ),

    people=["PER-ROWBOTHAM", "PER-DUBAY"],
    related=["D03", "D01", "D11", "D12", "D13", "D16", "A22", "C02"],

    sources=[
        dict(label="Rowbotham (“Parallax”), Zetetic Astronomy: Earth Not a Globe (1865), "
                   "Section 9 “Cause of Solar and Lunar Eclipses” — Project Gutenberg #69892; "
                   "the theory-independence paragraph, the Partington quotation of the Saros, "
                   "and the Somerville footnote",
             url="https://www.gutenberg.org/ebooks/69892"),
        dict(label="Rowbotham, Zetetic Astronomy, 3rd ed. enl. (1881), ch. XI, pp. 130–157 — "
                   "the enlarged version, with the almanac-tabulation method and the "
                   "“nineteenth and twentieth years” repeat",
             url="https://sacred-texts.com/earth/za/za29.htm"),
        dict(label="Eric Dubay, “Total Eclipse of the Mind” (11 July 2018) — reproduces the "
                   "1881 wording; the modern carrier of the argument",
             url="https://ericdubay.wordpress.com/2018/07/11/total-eclipse-of-the-mind/"),
        dict(label="Flat Earth Society wiki, “Astronomical Prediction Based on Patterns” — "
                   "“This page will demonstrate that prediction in astronomy is based solely "
                   "on patterns in the sky”; cites Rowbotham and Sir Robert Ball",
             url="https://wiki.tfes.org/Astronomical_Prediction_Based_on_Patterns"),
        dict(label="NASA GSFC eclipse site, “Eclipses and the Saros” — the three "
                   "commensurabilities, the ~120° shift per cycle, the ~0.5° node drift, and "
                   "series of 69–87 eclipses lasting 1226–1550 years",
             url="https://eclipse.gsfc.nasa.gov/SEsaros/SEsaros.html"),
        dict(label="EclipseWise, “Solar Eclipse Predictions with VSOP87 and ELP2000/82” — the "
                   "actual modern method, the ~1/40 s phase error, and “much smaller than the "
                   "uncertainties in predicted values of ΔT”",
             url="https://eclipsewise.com/solar/SEhelp/ve82-predictions.html"),
        dict(label="Stephenson, Morrison & Hohenkerk, “Measurement of the Earth's rotation: "
                   "720 BC to AD 2015”, Proc. R. Soc. A 472:20160404 (2016) — +1.78 ± 0.03 "
                   "ms/cy observed against +2.3 ± 0.1 ms/cy tidal, and the guarded ~1500-year "
                   "oscillation",
             url="https://pmc.ncbi.nlm.nih.gov/articles/PMC5247521/"),
        dict(label="EclipseWise, “Periodicity of Solar Eclipses” — the ecliptic limits, "
                   "“from 15.39° to 18.59° because of the eccentricity of the Moon's (and "
                   "Earth's) orbit”, and the 173.3-day eclipse season",
             url="https://eclipsewise.com/solar/SEhelp/SEperiodicity.html"),
        dict(label="Metonic cycle — 6939.602 d against 6939.689 d, Meton 432 BC, the "
                   "Babylonian 19-year intercalation of the late sixth century BC, and the "
                   "Callippic 76-year refinement",
             url="https://en.wikipedia.org/wiki/Metonic_cycle"),
        dict(label="Lunar node — nodal regression of 18.612958 years (6798.383 days), "
                   "retrograde, described as a precession rate rather than a resonance",
             url="https://en.wikipedia.org/wiki/Lunar_node"),
        dict(label="Fitzpatrick, Celestial Mechanics (Univ. of Texas), historical note on "
                   "lunar theory — Clairaut's factor-of-two perigee failure and its "
                   "second-order resolution; 8.728 vs 8.848 yr, 18.704 vs 18.615 yr",
             url="https://farside.ph.utexas.edu/teaching/celestial/Celestial/node114.html"),
        dict(label="Mary Somerville, On the Connexion of the Physical Sciences — Project "
                   "Gutenberg #52869; the edition searched for Rowbotham's footnoted sentence",
             url="https://www.gutenberg.org/ebooks/52869"),
        dict(label="Carpenter, One Hundred Proofs that the Earth Is Not a Globe (1885) — "
                   "Project Gutenberg #55387; searched for this material, see the note on "
                   "where the argument does and does not travel",
             url="https://www.gutenberg.org/ebooks/55387"),
    ]),
}
