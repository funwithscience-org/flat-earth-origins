# -*- coding: utf-8 -*-
"""Batch 9 — R02. "Mach's principle / relational mechanics allows a fixed Earth."

Four items: 27 ("Mach's principle supports fixed Earth possibility."), 129 ("Mach's
inertia explanation."), 275 ("Mach inertia relation."), 295 ("Relational mechanics
fixed Earth.").

Research notes for whoever picks this up next.

1. WHICH COPY WAS READ, AND WHERE THE MATERIAL ACTUALLY SITS. Everything cited below was
   read in one file: the OCR text of the Internet Archive item `GallileoWasWrong`
   ("Gallileo was wrong_djvu.txt", 3,335,538 bytes). Its title page reads "Volume I /
   The Scientific Evidence", ISBN 0-9779640-0-0, and identifies itself as the Compact
   Disc version. The dating is not left to the title page: the author's introduction is
   signed "Robert Sungenis / April 25, 2006", the latest publication cited anywhere in
   the text is from 2006, and the string "2007" does not occur in it at all. So
   passage.work stays WRK-SUNGENIS-2006 and clusters.py's year=2006 is correct. (One
   loose end outside this file: works.py gives Vol. I the subtitle "The Scientific Case
   for Geocentrism", where this copy's title page reads "The Scientific Evidence".)
   An earlier draft of this entry called the same item a seventh edition of 2013
   containing "Chapters 1 to 6", and put the Machian material in Chapter 9, "Modern
   Science & the Acceptance of Geocentrism by Principle", at pp. 145-149. None of that
   survived checking against the file. The strings "Chapters 1 to 6", "Previous five
   editions", "Popov", "2013" and "Modern Science & the Acceptance of Geocentrism by
   Principle" are not located anywhere in that OCR text. Printed pages 145-149 of it are
   Chapter 3 — the cosmological principle, Ellis, Sagan, Hawking — with nothing Machian
   on them. The Machian material is Chapter 10, "Mathematical Models of a Geocentric
   Universe", at printed pages 625-629, which is also where the item's own table of
   contents puts it: "Nightingale's Geocentrism 625 / Lynden-Bell's Geocentrism 626 /
   Barbour and Bertotti's Geocentrism 628", under the running head "Chapter 10 Galileo
   Was Wrong". Page by page: the zero-angular-momentum paragraph, the "fixed and
   undisturbed cradle", "inadvertently vindicated geocentrism" and "completely exonerate
   ... if the universe is closed" are all on p. 627; the passage.quote, "geocentrism has
   been established ... in 1905", is on p. 628; "by assuming a non-rotating universe" and
   the "[e.g., the universe]" / "[e.g., the Earth]" brackets are on p. 629. Every locator
   in this entry now names the page the quotation is on. No record_problem is filed
   against clusters.py's year: the defect was ours, not that record's.

2. THE SOURCE IS NOT HEDGED HERE, AND THE LIST IS. This is the unusual case. The hedge
   rule assumes the compressed item is stronger than the book; on R02 it is weaker.
   Sungenis writes "geocentrism has been established by the very physics that sought to
   dethrone it in 1905" (p. 628) and "Mach's principle has inadvertently vindicated
   geocentrism" (p. 627). Item 27 says the principle "supports fixed Earth possibility".
   The enum has no value for a list that understates its source, so the block is recorded
   drifted=False / drift_type="none" rather than forced into the nearest box — and the
   note carries the finding that actually matters, which is that the compression loss on
   this cluster happened ONE LINK UPSTREAM, inside the source, between the journal papers
   and Chapter 10. Three documented instances are in the compression note.

3. THE KERNEL, AND IT IS IN THE SOURCE'S OWN PARAGRAPH. Sungenis quotes Lynden-Bell,
   Katz and Bicak's "general proof that the angular momentum of any closed universe is
   zero" and reads it as providing "the fixed and undisturbed cradle for the barycenter,
   the Earth". That theorem is the one result in the cited literature that most directly
   excludes a cosmos circulating once a day: rigid circulation of all distant matter
   carries an enormous total angular momentum that nothing cancels. He also records, in
   his own summary of Barbour and Bertotti, that they proceed "by assuming a non-rotating
   universe". Both sentences are on the pages the cluster descends from.

4. THE TWO RELATIONAL THEORIES DISAGREE, WHICH IS THE HEART OF THE ANSWER. "Relational
   mechanics" is not one theory.
     - Assis (Relational Mechanics ..., Apeiron 2014, ch. 18.8, pp. 363-364) DOES deliver
       full dynamical equivalence for an Earth at rest with the galaxies circulating —
       and then, in the next paragraph, grants exactly the same to every other frame:
       "any other frame of reference would be equally valid. Anyone or any arbitrary
       frame of reference can be considered really at rest". His worked example is a
       falling rock. So the theory that grants the geocentric description grants it to
       everything, which is why it cannot single out the Earth.
     - Barbour and Bertotti's best-matching programme (Nuovo Cimento B 38(1):1-27, 1977)
       and its relativistic descendant admit only the zero-total-angular-momentum sector.
       The Stanford Encyclopedia summary is explicit: the theory "includes only the sector
       of the solution space of Newtonian mechanics which ascribes zero angular momentum
       to the entire universe", and in shape dynamics "one *cannot* have a solution
       consisting of a single rotating body: the overall angular momentum of the universe
       must vanish."
   So the more Machian the theory, the less room there is for a circulating sky.

5. CITATION CHAIN. Sungenis's Barbour-Bertotti quotations are footnoted "cited in 'The
   Geocentric Papers,' Association for Biblical Astronomy, Cleveland, Ohio. p. 88",
   "p. 89" and "Ibid., p. 98" — i.e. taken from the ABA compilation (Bouw's
   organisation), not from Nuovo Cimento. Consistent with that, the volume number is
   given as "32B" three times in this OCR text — a footnote at p. 464, footnote 1201 at
   p. 628, and the bibliography entry at p. 1075 — and as "38:1" once, in an appendix at
   p. 1027. Crossref gives the paper as Nuovo Cimento B 38(1):1-27, March 1977
   (10.1007/BF02726208), so the majority reading in this volume is the wrong one. OCR
   confusion of 8 for 2 is possible and could not be ruled out from the text alone, but
   it would have to have gone one way three times and the other way once.

6. ASSIS IS NOT A GEOCENTRIST AND IS NOT DESCRIBED AS ONE. He is a living physicist
   (UNICAMP). Everything attributed to him here is a quotation of his book's argument or
   of his own stated limitations, never an attribution of belief about the Earth. Same
   discipline applies to Barbour, Bicak, Katz, Nightingale and the late Lynden-Bell and
   Bertotti: the word "Geocentrism" in those section headings is the quoting author's,
   and the entry says so rather than implying the physicists own it.

7. WHAT IS GENUINELY OPEN (the E01 discipline). Mach's principle is unfinished physics,
   not settled physics, and the entry says so in the body. Bondi and Samuel (Phys. Lett.
   A 228:121, 1997) enumerate eleven inequivalent statements and score general relativity
   differently against each. The Lynden-Bell result is conditional on a closed universe,
   which the authors state as their antecedent. None of that openness runs towards a
   fixed Earth, and the entry does not pretend the question of Mach's principle is
   closed in order to close the geocentric one.

8. TWO QUOTATIONS WITHDRAWN, AND WHY. (a) The steelman used to have Mach challenging the
   reader to "Try to fix Newton's bucket and rotate the heaven of fixed stars and then
   prove the absence of centrifugal forces," followed by our own sentence "That is not a
   misquotation and it is not out of context." It was. That wording is not located in the
   McCormack second English edition (archive item cu31924004010504, Open Court 1902) nor
   in the Galileo Was Wrong text, and where it came from was not traced. What Mach wrote,
   in the Appendix at p. 543, is a question he answers himself: "Can we fix Newton's
   bucket of water, rotate the fixed stars, and then prove the absence of centrifugal
   forces? The experiment is impossible, the idea is meaningless, for the two cases are
   not, in sense-perception, distinguishable from each other," followed by "I accordingly
   regard these two cases as the same case and Newton's distinction as an illusion." Both
   sentences are now printed, including the second, which helps the defender: quoting up
   to the question and stopping would be the hedge rule broken in our own favour.
   (b) The KERNEL used to credit "a companion note" of Popov's with reproducing the 0.76"
   parallax of Proxima Centauri geostatically. The words "parallax", "Proxima" and
   "arcsec" do not occur in the full text of arXiv:1301.6045v2, and the only companion
   document is a one-page corrigendum, Eur. J. Phys. 34 (2013) 817 (Crossref page range
   817-817), which could not be obtained. Rather than guess, the clause is deleted; the
   KERNEL stands on Popov's published Sun-Earth-Mars result and Assis's bulge and
   pendulum derivations, and "the parallaxes" has been dropped from its closing sentence
   because Assis's book does not derive one either (its four uses of "parallax" are all
   about Bessel and Aristarchus). If anyone obtains the corrigendum and the figure is in
   it, cite it by DOI 10.1088/0143-0807/34/3/817 and add it to sources.

9. VERDICT CHALLENGE FILED. STANDARD PHYSICS ("real, already explained, does not
   discriminate") sits badly next to our own cluster note, "Mach's principle is not a
   settled part of GR". Proposed MISLEADING, aligning R02 with R05, which is the same
   move on adjacent material. Reasoning and the counter-case are in verdict_challenge;
   the decision is the integrator's.
"""

ENTRY = {

"R02": dict(

    verdict_challenge=dict(
        challenged=True,
        proposed_verdict="MISLEADING",
        reasoning=(
            "STANDARD PHYSICS means “real, already explained, does not discriminate”. "
            "The first two clauses do not fit. Mach's principle is not an explained piece of "
            "standard physics but an unfinished research programme: Bondi and Samuel enumerate "
            "eleven inequivalent statements of it and general relativity satisfies some and "
            "violates others, which is what our own cluster note says when it records that the "
            "principle “is not a settled part of GR”. A verdict and a note that "
            "contradict each other on the summary line is the defect batch 8 found five times. "
            "MISLEADING — “real data, wrong conclusion made to look supported” — "
            "fits what is on the page: real, peer-reviewed papers by Lynden-Bell, Katz and "
            "Bičák and by Barbour and Bertotti, presented under the section headings "
            "“Lynden-Bell's Geocentrism” and “Barbour and Bertotti's Geocentrism”, "
            "quoted with “[e.g., the universe]” and “[e.g., the Earth]” supplied "
            "in brackets, and concluding that “geocentrism has been established”. The "
            "sharpest instance is the zero-angular-momentum theorem, quoted accurately and then "
            "read as support for the arrangement it excludes. "
            "The case for leaving the verdict alone, stated fairly: in Assis's relational "
            "mechanics the equivalence really does hold, so there is a reading on which the "
            "claim is true physics that fails to discriminate — which is exactly what "
            "STANDARD PHYSICS is for. I think that reading rescues one branch of a four-item "
            "cluster whose weight is carried by the other branch, but it is not a silly "
            "reading, and the change would move 4 items between verdict columns."),
    ),

    tldr=("Mach's principle is real, unfinished, and not one proposition — a standard "
          "survey enumerates eleven inequivalent versions and general relativity satisfies "
          "some and violates others. Two worked-out relational theories then answer this "
          "cluster's question in opposite directions: Assis's grants an Earth-at-rest "
          "description, and grants the same to every other frame including a falling rock's; "
          "Barbour and Bertotti's admits only solutions in which the whole universe's angular "
          "momentum is zero, which is the arrangement a sky circulating once a day cannot "
          "have. Galileo Was Wrong quotes a second zero-angular-momentum result — Lynden-Bell, "
          "Katz and Bičák's proof that any closed universe has none — and reads it as "
          "vindicating a fixed Earth."),

    passage=dict(
        work="WRK-SUNGENIS-2006",
        pd=False,
        locator=("Chapter 10, “Mathematical Models of a Geocentric Universe”, at "
                 "the page footer numbered 628 in the Internet Archive OCR text of item "
                 "GallileoWasWrong (title page: Volume I, The Scientific Evidence, ISBN "
                 "0-9779640-0-0). The section runs from p. 625 to p. 629 under the running "
                 "head “Chapter 10 Galileo Was Wrong”, and the item's table of "
                 "contents places its three headings at 625, 626 and 628. Pages verified "
                 "against the OCR text only; not checked against a print copy or page images."),
        quote=("Considering that Lynden-Bell's paper includes ten pages of the most rigorous "
               "mathematical analyses to date of Mach's principle (i.e., that the universe in "
               "rotation around a fixed Earth equates to an Earth in rotation within a fixed "
               "universe), geocentrism has been established by the very physics that sought to "
               "dethrone it in 1905."),
        gloss="""<p><strong>The sentence before it is the one that matters.</strong> A page earlier, summarising the same paper, the book reports that &ldquo;The Lynden-Bell team stresses several times their <em>general proof that the angular momentum of any closed universe is zero</em>,&rdquo; and continues: &ldquo;Interestingly enough, the null value for the angular momentum will provide the fixed and undisturbed cradle for the barycenter, the Earth, and thus Mach&rsquo;s principle has inadvertently vindicated geocentrism once again&rdquo; (p.&nbsp;627). The theorem is quoted correctly. It is the result which most directly rules out what the chapter wants: a universe whose distant matter circulates rigidly once a day carries an immense total angular momentum, and that is the quantity the theorem sets to zero. The reading offered here is that the rotating sky &ldquo;generates no angular momentum to twist or rotate the Earth&rdquo; &mdash; a statement about torque on one body, which is not what the proof is about.</p>
<p><strong>The condition is quoted and then dropped.</strong> The book states the antecedent itself: Lynden-Bell, Katz and Bi&ccaron;&aacute;k &ldquo;completely exonerate Mach&rsquo;s principle, at least, as they say, <em>if the universe is closed</em>&rdquo; (p.&nbsp;627). Their paper is titled <em>Mach&rsquo;s principle from the relativistic constraint equations</em> and its result is that Mach&rsquo;s principle follows from the constraints <em>provided the universe is closed</em>. The sentence quoted above, which is the one the list inherits, carries no trace of that condition &mdash; and closure is an open question the data do not currently favour: Planck&rsquo;s 2018 parameters give a curvature density &Omega;<sub>K</sub> = 0.0007 &plusmn; 0.0019 with lensing and BAO, consistent with flat.</p>
<p><strong>Whose word &ldquo;geocentrism&rdquo; is.</strong> Three consecutive section headings on these pages attach it to physicists&rsquo; names &mdash; &ldquo;Nightingale&rsquo;s Geocentrism&rdquo;, &ldquo;Lynden-Bell&rsquo;s Geocentrism&rdquo;, &ldquo;Barbour and Bertotti&rsquo;s Geocentrism&rdquo;. The papers under those headings are about Mach&rsquo;s principle and inertial frames. In the Barbour and Bertotti extract the geocentric reading is supplied inside the quotation marks by square brackets, which by convention are the quoting author&rsquo;s: &ldquo;a rigid, uniform shell of mass M<sub>0</sub> and radius R<sub>0</sub> <strong>[e.g., the universe]</strong>. The test body <strong>[e.g., the Earth]</strong> is near the center of the shell&rdquo; (p.&nbsp;629). The shell and the test body are the authors&rsquo;; the universe and the Earth are the reader&rsquo;s guide.</p>
<p><strong>The chain the quotations travelled.</strong> Every Barbour and Bertotti extract in this chapter is footnoted to &ldquo;The Geocentric Papers,&rdquo; Association for Biblical Astronomy, Cleveland, Ohio &mdash; at its pp.&nbsp;88, 89 and 98 &mdash; a movement compilation published by the organisation Gerardus Bouw ran, rather than the journal. Consistent with that route, the journal volume is given as &ldquo;32B&rdquo; three times in this text (a footnote at p.&nbsp;464, the footnote here at p.&nbsp;628, and the bibliography at p.&nbsp;1075) and as &ldquo;38:1&rdquo; once, in an appendix at p.&nbsp;1027; the paper is <em>Nuovo Cimento</em> B <strong>38</strong>(1):1&ndash;27, March 1977. OCR confusion of 8 for 2 could not be ruled out from the scan text alone, but it would have to have gone one way three times and the other way once.</p>""",
    ),

    steelman=dict(
        description="""<p><strong>SURFACE (weak &mdash; do not use).</strong> &ldquo;Mach&rsquo;s principle is philosophy, not physics.&rdquo; This loses immediately. Machian frame dragging is a measured effect: Gravity Probe B flew four gyroscopes to look for it and returned a frame-dragging drift of &minus;37.2 &plusmn; 7.2 mas/yr against a predicted &minus;39.2, alongside a geodetic drift of &minus;6,601.8 &plusmn; 18.3 against &minus;6,606.1. Anyone who dismisses the whole subject has conceded that they have not read it.</p>
<p><strong>DEEPER.</strong> The kinematic half of the claim is Mach&rsquo;s own, in print. In <em>The Science of Mechanics</em> he writes that &ldquo;the motions of the universe are the same whether we adopt the Ptolemaic or the Copernican mode of view. Both views are, indeed, equally correct&rdquo; (p.&nbsp;232), and in the Appendix he puts the bucket question himself and answers it in the same breath: &ldquo;Can we fix Newton&rsquo;s bucket of water, rotate the fixed stars, and then prove the absence of centrifugal forces? The experiment is impossible, the idea is meaningless, for the two cases are not, in sense-perception, distinguishable from each other.&rdquo; He then states the conclusion flatly: &ldquo;I accordingly regard these two cases as the same case and Newton&rsquo;s distinction as an illusion&rdquo; (p.&nbsp;543). Quote him as printed and the defence gets stronger, not weaker &mdash; it is not a dare left hanging but a verdict. What should <em>not</em> be quoted is the loose paraphrase this entry carried until now, in which Mach challenges the reader to &ldquo;try to fix Newton&rsquo;s bucket and rotate the heaven of fixed stars&rdquo;: that wording is not located anywhere in the McCormack second English edition (Open Court, 1902) or in the text of <em>Galileo Was Wrong</em>, and where it came from was not traced. On a page whose subject is quotations losing their qualifiers in transit, printing a variant would be the worst available error.</p>
<p><strong>KERNEL.</strong> The specific true thing is that somebody has done the sums, more than once, in peer-reviewed print. Luka Popov, <em>Eur. J. Phys.</em> 34:383 (2013), works the Sun&ndash;Earth&ndash;Mars system twice &mdash; once Copernican, once neo-Tychonic &mdash; and shows that with a Machian pseudo-potential standing in for the accelerated distant matter, the trajectories come out the same. Andr&eacute; Assis goes further: <em>Relational Mechanics and Implementation of Mach&rsquo;s Principle with Weber&rsquo;s Gravitational Force</em> derives the Earth&rsquo;s equatorial bulge and the precession of Foucault&rsquo;s pendulum from the rotation of the distant galaxies about a stationary Earth, and states the conclusion plainly: &ldquo;We have found a complete equivalence between ptolemaic and copernican world systems &hellip; not only kinematically or visually, but also dynamically.&rdquo; So the strongest form of R02 is not a plea for tolerance. It is: <em>there exists a published, quantitative, relational mechanics in which an Earth at rest with the cosmos turning about it reproduces the equatorial bulge, Foucault&rsquo;s precession and the Coriolis deflections.</em> Concede every word of that; it is true.</p>""",
        why_it_doesnt_save_claim="""<p>Because in that same book the equivalence is handed to <em>everything</em>. Two paragraphs after the Ptolemaic&ndash;Copernican section, Assis writes: &ldquo;As a matter of fact, any other frame of reference would be equally valid. Anyone or any arbitrary frame of reference can be considered really at rest, while the entire universe moves relative to this person according to his will.&rdquo; His worked example is a rock in free fall, which may be taken as permanently at rest while the Earth and all the galaxies accelerate towards it. A theory on which the falling rock&rsquo;s frame is as good as the Earth&rsquo;s has not made the Earth the centre of anything. It has abolished centres. The list needs a result about the Earth and relational mechanics supplies a result about frames.</p>
<p>And the other great relational programme, the one <em>Galileo Was Wrong</em> leans on by name, forbids the thing outright. Barbour and Bertotti built their dynamics to be invariant under time-dependent rotations, and the price of that invariance is that only the zero-total-angular-momentum solutions survive; in the relativistic descendant, as the Stanford Encyclopedia puts it, &ldquo;one <em>cannot</em> have a solution consisting of a single rotating body: the overall angular momentum of the universe must vanish.&rdquo; The book&rsquo;s own summary of the 1977 paper records the authors proceeding &ldquo;by assuming a non-rotating universe&rdquo;. So the two theories that have actually been written down disagree about the one question the cluster turns on, and the citation carries the word &ldquo;relational&rdquo; without carrying either theory&rsquo;s answer.</p>""",
    ),

    refutation="""<p><strong>First, what is conceded, and it is a lot.</strong> Machian effects are real and measured. A rotating mass does drag the local inertial frames inside and around it: Thirring wrote the shell calculation in 1918, Brill and Cohen showed in 1966 that the dragging becomes complete as a rotating shell approaches its own gravitational radius, and Gravity Probe B measured the effect in orbit &mdash; a frame-dragging drift of &minus;37.2 &plusmn; 7.2 mas/yr against a predicted &minus;39.2. The kinematic equivalence Mach asserted is real. And the relational programme is serious physics done by serious people, published in <em>Nuovo Cimento</em>, in <em>MNRAS</em>, in the <em>American Journal of Physics</em> and in the <em>European Journal of Physics</em>. Nothing below depends on treating any of that as fringe.</p>

<p><strong>Second, &ldquo;Mach&rsquo;s principle&rdquo; is not one proposition, and the ambiguity is doing the work.</strong> Bondi and Samuel set out eleven inequivalent statements that go under the name and score general relativity against each: Mach0, that the distant galaxies show no rotation relative to local inertial frames &mdash; an observational statement, and true; Mach3, that local inertial frames are affected by the cosmic distribution of matter &mdash; which general relativity satisfies; Mach2, that an isolated body in empty space has no inertia, and Mach7, that removing all matter removes space &mdash; which it does not satisfy. Einstein named the principle in 1918 as a goal of his theory and had recognised by that year that the theory did not deliver all of it. So a sentence of the form &ldquo;Mach&rsquo;s principle allows a fixed Earth&rdquo; has not said anything until it says which Mach, and the versions that general relativity actually satisfies are the ones about how inertial frames are <em>influenced</em>, not the ones that would let a planet be exempted from turning.</p>

<p><strong>Third, and this is the centre of it: the theorem quoted in support is the theorem that excludes the model.</strong> The chapter&rsquo;s strongest citation is Lynden-Bell, Katz and Bi&ccaron;&aacute;k, and what it takes from them is their &ldquo;general proof that the angular momentum of any closed universe is zero&rdquo;, read as providing &ldquo;the fixed and undisturbed cradle for the barycenter, the Earth&rdquo;. Read the theorem as written. It says that in a closed universe the <em>total</em> angular momentum of everything vanishes. A cosmos in which the Sun, the planets, the stars and the galaxies circulate rigidly about the Earth at 15.041&deg; per hour has an enormous total angular momentum and there is nothing left over to cancel it. The geocentric arrangement is precisely the configuration the theorem forbids.</p>

<p>The relational reply to that has to be met, because it is the best move available: in a theory where only relative motion is real, who is entitled to compute &ldquo;the angular momentum of the universe&rdquo; in some frame outside it and wave the answer at us? The reply is that the vanishing is not a quantity imported from outside. It is a constraint on the matter itself, which is why Lynden-Bell, Katz and Bi&ccaron;&aacute;k present their result as a vindication of Mach rather than of Newton. And Barbour and Bertotti reach the same restriction from the opposite end, with no background whatever: demand that a rigid, time-dependent rotation of the entire configuration be unobservable, and Dirac&rsquo;s analysis of the resulting constraints forces the total angular momentum to zero. Bondi and Samuel, cataloguing the versions, set this down as Mach5 &mdash; &ldquo;the total energy, angular and linear momentum of the universe are zero&rdquo; &mdash; false in Newtonian mechanics and in asymptotically flat spacetimes, while in relativistic cosmology, they write, &ldquo;it is claimed that the total angular momentum of a closed universe must vanish&rdquo;; and of the relational models themselves they observe that Newtonian theory admits solutions with nonzero angular momentum, such as a solar system in an otherwise empty universe, &ldquo;while relational models do not permit such solutions&rdquo;. Two independent routes to the same exclusion, both of them relational, and neither needing an absolute space to state it.</p>

<p>What the paper offers is the opposite service: with the angular momentum distribution as observed, the local inertial frames do not rotate relative to the distant matter &mdash; which is Mach0, the empirical statement, and it is the statement that the sky and the gyroscopes agree, leaving the Earth to turn under both.</p>

<p>The same reversal runs through the Barbour and Bertotti material. Their dynamics is built to be invariant under time-dependent rotations of the whole configuration, and what survives that construction is only the sector with zero total angular momentum; its relativistic descendant cannot accommodate a single rotating body at all, because the universe&rsquo;s overall angular momentum must vanish. The book&rsquo;s own paraphrase of the 1977 paper contains the words &ldquo;by assuming a non-rotating universe&rdquo;. Three of the four technical authorities marshalled here are Machian relationalists, and Machian relationalism is the framework in which a rotating cosmos is hardest to write down.</p>

<p><strong>Fourth, the one theory that does deliver the equivalence delivers it to everybody.</strong> Assis&rsquo;s relational mechanics really does reproduce the equatorial bulge, Foucault&rsquo;s precession and the Coriolis deflections from a rotation of the distant galaxies about a stationary Earth; the derivation is in chapter 18 and the conclusion is stated without hedging. It is also stated, on the same two pages, that &ldquo;any other frame of reference would be equally valid&rdquo; and that &ldquo;anyone or any arbitrary frame of reference can be considered really at rest, while the entire universe moves relative to this person according to his will&rdquo; &mdash; illustrated with a rock in free fall which may be held permanently at rest while the Earth and the galaxies accelerate upwards towards it. That is the whole content of the result: <em>frames are cheap</em>. It cannot be spent on the Earth without being spent on the rock, and a doctrine that makes the falling rock the centre of the universe has stopped being geocentrism.</p>

<p>Assis is also candid about the bill. His mechanics runs on Weber&rsquo;s force law and needs the relation H<sub>0</sub><sup>2</sup>/&rho; &asymp; G, of which he writes: &ldquo;We cannot say that this relation is exactly valid, due to uncertainties in the observational values&rdquo;. On the deflection of starlight by the Sun he writes &ldquo;we need further research in this direction before drawing final conclusions&rdquo;, and on the gravitational redshift he reports the calculations with Weber&rsquo;s law as still to be published as of that edition. And the cosmology comes attached: a universe infinite in space and time, not expanding, with Hubble&rsquo;s law produced by light losing energy to the intergalactic medium. Adopting relational mechanics to license a stationary Earth means adopting all of that, and the rest of this list does not.</p>

<p><strong>Fifth, the neo-Tychonic calculation and the assumption inside it.</strong> Popov&rsquo;s paper is the best single technical item in this cluster, and it says what it is: the analysis is carried out &ldquo;in the framework of Newtonian mechanics&rdquo;, &ldquo;the kinematical equivalence &hellip; is shown to be a consequence of the presence of pseudo-potential&rdquo;, and the model is defined by &ldquo;the assumption that orbits of distant masses around the Earth are synchronized with the Sun&rsquo;s orbit&rdquo;. That last clause is the entire annual mechanism, and it is granted rather than derived. Every distant galaxy must complete a circuit about the Earth once a year, phase-locked to where the Sun happens to be, and a second circuit once a sidereal day, with the two motions superposed and no dynamical account of what enforces either. The paper is honest about this. What it establishes is that <em>given</em> a pseudo-potential of the required form, the geostatic trajectories come out right &mdash; a statement about the consistency of a description, which is what the pseudo-potential was built to be.</p>

<p><strong>Sixth, the arithmetic of a turning cosmos.</strong> Two numbers bound the ambition. At an angular rate of one sidereal turn per day, a body co-moving with the sky reaches the speed of light at a radius of c/&Omega; = 4.11 &times; 10<sup>12</sup> m, about 27.5 astronomical units &mdash; inside the orbit of Neptune. Beyond that radius, being &ldquo;at rest with respect to the Earth&rdquo; is not a state matter can occupy, because the Earth-fixed rotating chart stops being a reference frame there; the co-ordinates survive, the frame does not. And the observational bound on a global circulation runs the other way by a wide margin: the required rate compared to the expansion rate is &Omega;/H<sub>0</sub> &asymp; 3 &times; 10<sup>13</sup>, while the Planck analysis of Saadeh and colleagues bounds the vector mode, the one associated with vorticity, at (&sigma;<sub>V</sub>/H)<sub>0</sub> &lt; 4.7 &times; 10<sup>&minus;11</sup> at 95% confidence, and disfavours anisotropic expansion at odds of 121,000:1. State the caveat ourselves rather than wait for it: that bound is derived within a perturbed relativistic cosmology, so a defender who rejects the framework will reject the number. The light-cylinder radius does not depend on the framework, and neither does the third section above, which is why the argument does not rest here.</p>

<p><strong>Seventh, what Mach actually wrote, which cuts both ways and is worth quoting at length because it is out of copyright and the geocentric literature quotes only its first half.</strong> In the McCormack translation, pp.&nbsp;231&ndash;232: &ldquo;Relatively, not considering the unknown and neglected medium of space, the motions of the universe are the same whether we adopt the Ptolemaic or the Copernican mode of view. Both views are, indeed, equally correct; <em>only the latter is more simple and more practical.</em> The universe is not twice given, with an earth at rest and an earth in motion; but only once, with its relative motions, alone determinable. It is, accordingly, not permitted us to say how things would be if the earth did not rotate. We may interpret the one case that is given us, in different ways. <em>If, however, we so interpret it that we come into conflict with experience, our interpretation is simply wrong.</em>&rdquo; Two sentences there do work against the use being made of him. The first denies that we are entitled to the counterfactual &mdash; &ldquo;how things would be if the earth did not rotate&rdquo; is exactly the sentence a geocentric proof needs and exactly the sentence Mach rules out of order. The second sets a constraint on interpretations that the pseudo-potential models have to meet like anything else.</p>

<p>And the earlier statement of the same idea, from 1872, is more explicit still about what the equivalence costs: &ldquo;if we think of the Earth at rest and the other celestial bodies revolving round it, there is no flattening of the earth, no Foucault&rsquo;s experiment, and so on &mdash; <em>at least according to our usual conception of the law of inertia.</em> Now, one can solve the difficulty in two ways: Either all motion is absolute, or our law of inertia is wrongly expressed &hellip; The law of inertia must be so conceived that exactly the same thing results from the second supposition as from the first.&rdquo; That is a research programme announced, not a result reported. Mach is saying that a geostatic account requires a rewritten law of inertia, and proposing to write one. A hundred and fifty years later the rewriting is still contested, still incomplete in the versions that exist, and &mdash; in the version with the most mathematical development, Barbour&rsquo;s &mdash; comes out against a rotating universe.</p>

<p><strong>Eighth, the dilemma, which is where this ends.</strong> Take &ldquo;the universe rotates about the Earth&rdquo; and ask what kind of statement it is. If it is a choice of description, then relational mechanics grants it, grants it equally to the Sun, to Mars and to a falling rock, and grants nothing about which body is at the centre &mdash; the same trade made at <a href="#ARG-R01">ARG-R01</a> and <a href="#ARG-R03">ARG-R03</a>. If it is a physical claim that the matter of the cosmos carries a real circulation, then it is a claim with consequences: a total angular momentum that the closed-universe theorem sets to zero, a co-rotation radius at 27.5 AU, a vorticity the microwave background constrains, and a required synchronisation of every distant galaxy with the Sun&rsquo;s annual position for which the published models supply a stipulation. Both horns are in the sources this cluster cites. The chapter takes the first horn&rsquo;s permission and the second horn&rsquo;s conclusion, and the four list items report the result as a finding of modern physics.</p>""",

    advocate=dict(
        best_defense=(
            "You have done something clever and it will not survive inspection. You answered "
            "Assis with Barbour and Barbour with Assis. They are different theories; neither "
            "is obliged to agree with the other, and a disagreement between two relational "
            "programmes is not an argument against relationalism any more than a disagreement "
            "between two quantum gravity programmes is an argument against gravity. On the "
            "merits you have conceded the thing that matters: there exists a published, "
            "quantitative mechanics in which an Earth at rest reproduces the bulge, the "
            "pendulum and the Coriolis deflection, and a second, published in the European "
            "Journal of Physics, that reproduces the planetary trajectories. You call that "
            "'frames are cheap'. We call it a working model, and "
            "your side spent three centuries insisting no such model could exist. "
            "Second, the zero-angular-momentum move is a sleight of hand. In a relational "
            "theory 'the angular momentum of the universe' is not a quantity you get to "
            "compute in some outside frame and wave at us; it is defined relative to the "
            "matter itself, and the relative configuration of Earth and sky is identical in "
            "the two pictures by your own admission. You cannot first grant that only "
            "relative motion is real and then convict us with an absolute quantity. "
            "Third, your Planck vorticity bound is circular and you nearly admit it. It is "
            "derived inside a perturbed FLRW model that assumes at the outset the very "
            "cosmology under dispute. Feeding a theory its own assumptions and reporting the "
            "output as a constraint on the alternative is not evidence. "
            "Fourth, the light cylinder is an artefact of insisting that the rotating chart "
            "be a global inertial frame, which nobody claims. In general relativity "
            "coordinate speeds exceed c routinely and harmlessly, and you know it. "
            "Fifth, on Mach: yes, he said the Copernican view is 'more simple and more "
            "practical'. Simplicity and practicality are not truth, and he said in the same "
            "breath that both views are equally correct. You quoted the sentence that helps "
            "you and left the one before it alone."),
        survives=4,
        preemptive=(
            "Four, and the number is driven by the second and third moves, not the first. "
            "Four concrete changes. "
            "(a) THE CIRCULARITY HIT IS THE DANGEROUS ONE and the body must not depend on the "
            "Planck bound. The sixth section already states the caveat in our own voice and "
            "says the argument does not rest there; keep that sentence adjacent to the number "
            "and never let an editor promote the vorticity limit into the TLDR. If the "
            "vorticity bound is ever moved earlier in the page, this entry becomes refutable "
            "by a first-year cosmology student. "
            "(b) THE ANGULAR-MOMENTUM REPLY IS NOW IN THE BODY, in its own paragraph in the "
            "third section, because the defender's version of it is good and this is an "
            "internal panel no reader sees. The answer there is that the theorem is not an "
            "absolute-space quantity smuggled in from outside: in a closed universe the total "
            "angular momentum vanishes as a constraint on the matter itself, which is exactly "
            "why Lynden-Bell, Katz and Bicak present it as a vindication of Mach rather than "
            "of Newton, and Barbour and Bertotti reach the same restriction from pure "
            "relational invariance under time-dependent rotations with no background at all, "
            "Dirac's first-class constraints doing the work. Bondi and Samuel, already in our "
            "sources, supply the third citation at Mach5. Two independent routes to the same "
            "exclusion, both of them relational. Do not let a future trim take that paragraph "
            "out; without it the strongest objection in this file goes unanswered on the page. "
            "(c) DO NOT LET THE 'YOU ANSWERED EACH WITH THE OTHER' CHARGE STAND UNMET. The "
            "reply is that we are not playing them off; each is answered on its own terms and "
            "the answers happen to differ. Assis's theory grants the description and grants it "
            "to the falling rock, which is a statement about Assis's theory alone. Barbour's "
            "excludes the circulation, which is a statement about Barbour's theory alone. The "
            "list cites both under one word. If the page ever compresses this into 'the "
            "relationalists disagree', we have committed the exact error the project exists to "
            "document. "
            "(d) ON MACH, the defender is right that simplicity is not truth and the text "
            "should not lean on 'more simple and more practical'. The load-bearing Mach "
            "sentences are the two that follow it: that we are not permitted to say how things "
            "would be if the earth did not rotate, and that an interpretation which conflicts "
            "with experience is simply wrong. The seventh section already italicises the "
            "second; make sure any future trim keeps both and drops the simplicity clause "
            "first."),
    ),

    straw_man=dict(
        identified=True,
        detail=("Three consecutive section headings in the chapter attach the word "
                "“Geocentrism” to the names of physicists — Nightingale, "
                "Lynden-Bell, and Barbour and Bertotti — whose papers are about Mach's "
                "principle and the determination of inertial frames. In the Barbour and "
                "Bertotti extract the geocentric reading is inserted inside the quotation "
                "marks in square brackets, which by convention belong to the quoting author: "
                "the authors' “rigid, uniform shell” becomes “[e.g., the "
                "universe]” and their “test body” becomes “[e.g., the "
                "Earth]”. A reader is left with the impression that named researchers "
                "hold a position on the Earth's motion; what the pages show is a reading "
                "supplied by the quoting author, from a movement compilation rather than from "
                "the journals, around quotations that are otherwise accurate."),
    ),

    compression=dict(
        assessed=True, drifted=False,
        list_phrasing=("Mach's principle supports fixed Earth possibility. / Relational "
                       "mechanics fixed Earth. / Mach's inertia explanation. / Mach inertia "
                       "relation. (items 27, 295, 129, 275)"),
        source_wording=("“geocentrism has been established by the very physics that sought "
                        "to dethrone it in 1905”; “Mach&rsquo;s principle has "
                        "inadvertently vindicated geocentrism”"),
        drift_type="none",
        note=("""<p><strong>This one runs the other way, and the honest record is that the list is milder than its source.</strong> Item 27 says Mach&rsquo;s principle &ldquo;supports fixed Earth <em>possibility</em>&rdquo;. Chapter 10 of <em>Galileo Was Wrong</em> says geocentrism &ldquo;has been established&rdquo; and that Mach&rsquo;s principle &ldquo;has inadvertently vindicated&rdquo; it. The seven <code>drift_type</code> values have no slot for a list that understates its source, and rather than force this into the nearest box it is recorded as <code>none</code> with the direction stated here. The refutation above answers the book&rsquo;s stronger version, which is the one that needed answering.</p>
<p><strong>The compression loss on this cluster is real, and it happened one link upstream.</strong> It is between the journals and Chapter 10, not between Chapter 10 and the list, and three instances are documented in the pages read for this entry. <em>One:</em> Lynden-Bell, Katz and Bi&ccaron;&aacute;k prove Mach&rsquo;s principle from the relativistic constraint equations <em>if the universe is closed</em>; the book quotes the condition on p.&nbsp;627 and the sentence that travels onward carries none of it. <em>Two:</em> their &ldquo;general proof that the angular momentum of any closed universe is zero&rdquo; is quoted accurately on p.&nbsp;627 and presented as providing &ldquo;the fixed and undisturbed cradle&rdquo; for the Earth, when a cosmos circulating once a day is the configuration that proof excludes. <em>Three:</em> the Barbour and Bertotti extract on p.&nbsp;629 carries &ldquo;[e.g., the universe]&rdquo; and &ldquo;[e.g., the Earth]&rdquo; supplied in brackets, under a heading naming the authors as geocentrists, and the book&rsquo;s own paraphrase a few lines earlier on the same page records them proceeding &ldquo;by assuming a non-rotating universe&rdquo;.</p>
<p><strong>Why that is a finding rather than a technicality.</strong> The project&rsquo;s thesis is that a claim degrades in transit and the degradation runs towards certainty. R02 is the case where the degradation can be located at a particular link: hedged, conditional results in <em>MNRAS</em> and <em>Nuovo Cimento</em>, reached through a movement compilation (&ldquo;The Geocentric Papers&rdquo;) rather than the journals, arrive in Chapter 10 with their antecedents stripped and their names re-labelled; the list then copies Chapter 10 faithfully, and even softens it. Blaming the list for this cluster would be blaming the wrong link.</p>"""),
    ),

    people=["PER-SUNGENIS", "PER-BOUW"],
    related=["R01", "R03", "R04", "R05", "R06", "R08", "R11", "A02", "A09", "A26"],

    sources=[
        dict(label="Sungenis & Bennett, Galileo Was Wrong: The Church Was Right — Internet "
                   "Archive item GallileoWasWrong (title page: Volume I, The Scientific "
                   "Evidence, ISBN 0-9779640-0-0). Chapter 10, “Mathematical Models of a "
                   "Geocentric Universe”, pp. 625–629: “Nightingale's Geocentrism” (625), "
                   "“Lynden-Bell's Geocentrism” (626), the zero-angular-momentum paragraph and "
                   "the “completely exonerate … if the universe is closed” sentence (627), "
                   "“Barbour and Bertotti's Geocentrism” and the “established … in 1905” "
                   "sentence (628), and the “[e.g., the universe]” extract (629)",
             url="https://archive.org/details/GallileoWasWrong"),
        dict(label="Mach, The Science of Mechanics (McCormack translation, second revised and "
                   "enlarged English edition, Open Court, 1902) — the Ptolemaic/Copernican "
                   "passage, “not permitted us to say how things would be if the earth did not "
                   "rotate”, and the “several leagues thick” bucket remark, at pp. 231–232 of "
                   "this public-domain printing; the bucket question itself and Mach's own "
                   "answer to it (“the two cases are not, in sense-perception, distinguishable "
                   "from each other … the same case and Newton's distinction as an illusion”) "
                   "in the Appendix at p. 543",
             url="https://archive.org/details/cu31924004010504"),
        dict(label="Lynden-Bell, Katz & Bičák, “Mach's principle from the relativistic "
                   "constraint equations”, MNRAS 272:150 (1995) — Mach's principle follows "
                   "from the constraints provided the universe is closed; the angular momentum "
                   "of a closed universe is zero",
             url="https://academic.oup.com/mnras/article/272/1/150/967275"),
        dict(label="Barbour & Bertotti, “Gravity and inertia in a Machian framework”, Nuovo "
                   "Cimento B 38(1):1–27 (1977) — the Leibniz group, invariance under "
                   "time-dependent rotations",
             url="https://link.springer.com/article/10.1007/BF02726208"),
        dict(label="Stanford Encyclopedia of Philosophy, “Absolute and Relational Space and "
                   "Motion: Post-Newtonian Theories” — Barbour–Bertotti best-matching admits "
                   "“only the sector … which ascribes zero angular momentum to the entire "
                   "universe”; in shape dynamics “the overall angular momentum of the universe "
                   "must vanish”",
             url="https://plato.stanford.edu/entries/spacetime-theories/"),
        dict(label="Bondi & Samuel, “The Lense–Thirring effect and Mach's principle”, Phys. "
                   "Lett. A 228:121 (1997) — eleven inequivalent statements of the principle "
                   "(Mach0–Mach10), scored against general relativity; Mach5, “the total energy, "
                   "angular and linear momentum of the universe are zero”, with the note that in "
                   "relativistic cosmology “it is claimed that the total angular momentum of a "
                   "closed universe must vanish”; and the derivation of relational models by "
                   "imposing first-class constraints that set the total angular momentum to zero",
             url="https://arxiv.org/abs/gr-qc/9607009"),
        dict(label="Assis, Relational Mechanics and Implementation of Mach's Principle with "
                   "Weber's Gravitational Force (Apeiron) — ch. 14.6 on Mach; ch. 18.8 "
                   "pp. 363–364, the Ptolemaic/Copernican equivalence and “any other frame of "
                   "reference would be equally valid”; the stated gaps on light deflection and "
                   "gravitational redshift; the tired-light, non-expanding cosmology",
             url="https://www.ifi.unicamp.br/~assis/Relational-Mechanics-Mach-Weber.pdf"),
        dict(label="Popov, “Newtonian–Machian analysis of the neo-Tychonian model of planetary "
                   "motions”, Eur. J. Phys. 34:383 (2013) — Newtonian framework, pseudo-"
                   "potential, and the assumption that distant masses' orbits are synchronised "
                   "with the Sun's",
             url="https://arxiv.org/abs/1301.6045"),
        dict(label="Saadeh et al., “How Isotropic is the Universe?”, Phys. Rev. Lett. 117:131302 "
                   "(2016) — vector mode (σ_V/H)₀ < 4.7×10⁻¹¹ at 95% CI; anisotropic expansion "
                   "disfavoured at 121,000:1",
             url="https://arxiv.org/abs/1605.07178"),
        dict(label="Everitt et al., “Gravity Probe B: Final Results of a Space Experiment to "
                   "Test General Relativity”, Phys. Rev. Lett. 106:221101 (2011) — frame "
                   "dragging −37.2 ± 7.2 mas/yr against a predicted −39.2",
             url="https://arxiv.org/abs/1105.3456"),
        dict(label="Planck 2018 results VI, A&A 641:A6 — curvature Ω_K = 0.0007 ± 0.0019, "
                   "the condition Lynden-Bell et al. attach to their Machian result",
             url="https://arxiv.org/abs/1807.06209"),
    ]),
}
