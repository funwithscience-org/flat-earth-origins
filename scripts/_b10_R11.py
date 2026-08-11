# -*- coding: utf-8 -*-
"""Batch 10 — R11. "No falsifier distinguishes the frames; multiple cosmologies fit the data."

Three items: 293 "No falsifier distinguishing frames.", 310 "Multiple cosmologies fit
data.", 318 "Horizon problem Earth initial data." Verdict SELF-CONTRADICTED, kept.

Research notes for whoever picks this up next.

1. WHICH TEXT THIS IS BUILT ON, AND THE EDITION TRAP. `clusters.py` credits R11 to Bouw's
   *Geocentricity* (1992, Association for Biblical Astronomy). No copy of the 1992 first
   edition was reachable from here. What IS reachable, complete, and OCR-searchable is the
   2013 edition, retitled *GEOCENTRICITY: CHRISTIANITY IN THE WOODSHED* (same imprint;
   ISBN 9781890120900; Internet Archive item `geocentricity-christianity-in-the-woodshed`,
   1.5 MB of djvu OCR). Every Bouw quotation in this entry is from that 2013 text and the
   locator says so, on the R03 precedent. Two independent corroborations that the same
   doctrine was in the 1992 book: Faulkner's review of the 1992 edition (*Journal of
   Creation* 15(2), 2001) reports "the essential difference between the heliocentric and
   Tychonian models is a co-ordinate change from the Sun to the Earth"; and Bouw's own
   reply to that review, "GEOCENTRICITY: A Fable for Educated Man?", restates the position
   while discussing the 1992 book by name. Do NOT upgrade the locator to "1992, p. N"
   without page images of the first edition.

2. THE SOURCE STATES THE SYMMETRY EXPLICITLY, WHICH IS THE WHOLE FINDING. Appendix E,
   p. 747: dynamical proofs "are not proofs of anything; nor are they proofs against the
   geocentric universe." Chapter 1, p. 4, with two hedges the list drops — it is attributed
   to other people and granted only partly: "The more subtle physicists ... will claim,
   with some justification, that we can neither prove nor disprove the geocentric universe;
   but that we likewise can neither prove nor disprove the non-geocentric universe either."
   Chapter 28, p. 425, applying it: the Earth's oblateness "offers no proof for either
   heliocentric or geocentric theories." A symmetric no-proof claim, filed on the list as
   proof #293. drift_type = force_upgraded, same mechanism as R01, different book.

3. THE SELF-CONTRADICTION IS INSIDE THE BOOK, NOT ONLY INSIDE THE LIST. This is what makes
   the verdict safe. p. 3: "every fundamental experiment ever devised to measure the speed
   of the earth through space measures a speed of zero" and "there is no difference between
   the equations describing the causes and motions of the geocentric universe and those
   describing ... the modern heliocentric universe." Both on one page. Then p. 523:
   "Geocentricity predicts that earth's lack of motion is absolute ... Geocentricity further
   predicts that rotation is relative. And that is exactly what fundamental experiments ...
   detect", and Sagnac has "been performed accurately enough to discern the period of
   absolute rotation of the firmament is the sidereal day". A model that PREDICTS can FAIL.
   He asserts a falsifiable model and then files the claim that no falsifier exists.

4. AND THE FIRMAMENT IS A PHYSICAL MEDIUM, WHICH IS THE KEY TO THE REFUTATION. p. 5: it "is
   a superdense medium that pervades all of space. It is the firmament that dictates the
   laws of physics, and it is the firmament that physically controls all motion." Appendix E
   p. 746: the accelerations "keep the star in its place in the inertial field of the
   universe which is the gravitational field of the firmament." So this is not a relabelling
   of coordinates; it is a dynamical cosmology, and dynamical cosmologies have consequences.
   CORRECTED 2026-08-11 against page images: this note previously said Appendix E "derives
   the rotating-frame accelerations (eq. 11) and stops there". It does not stop there. At
   p. 746, immediately after the sentence quoted above, Bouw writes "Of course, equation
   (11) is kinematic, not dynamic and we have to show the geocentric model is dynamically
   correct. To do that, all we have to do is to multiply both sides by the star's mass, m",
   giving F = ma (eq. 12), and then applies it to the sun, moon, planets, artificial
   satellites, stars and to the propagation of light. THAT is where it ends: no field
   equation, stress-energy tensor or cosmological solution appears anywhere in the appendix
   (pp. 740–747, eqs. 1–12), which is why there is no fit to run against his model.
   Note also that the appendix OPENS (pp. 740–741, eqs. 1–3) by calling the
   kinematic-to-dynamic step a "sleight of hand" — multiplying one side by m/m — which is
   Bouw's pre-emptive answer to §3's "his cosmos is not a relabelling". §3 now answers it
   on the merits rather than leaving it unengaged.

5. ITEM 310 HAS A REAL AND CHECKABLE PEDIGREE, AND BOUW CITES IT CORRECTLY. Chapter 36
   note 2 reads "Ellis, G. F. R., 1978. General Relativity and Gravitation, 9:87. Quote is
   from page 92." That paper is real: "Is the universe expanding?", GRG 9:87–94, whose
   abstract says spherically symmetric static spacetimes "can reproduce the same
   cosmological observations as the currently favored Friedmann-Robertson-Walker universes
   ... provided that the universe is inhomogeneous and our galaxy is situated close to one
   of its centers." Ellis wrote the escape clause into the same abstract — route (ii),
   "detailed physical and astrophysical arguments" — and thirty years later co-authored one
   of the tests (Uzan, Clarkson & Ellis, PRL 100:191303, 2008). That arc is the refutation.
   `clusters.py` carries `real_source=None` for R11; Ellis 1978 is the documented one.
   CAUTION before anyone applies that: `real_source` years feed the Overview's dating
   section and `tests/test_provenance.py` pins the cited-work median at 1933.

6. ITEM 318 IS THE ODD ONE AND I COULD NOT TIE IT TO THIS SOURCE. A search of the full
   2013 OCR text located no occurrence of the string "horizon problem"; the only cosmic
   "horizon" in it is the event horizon, used against the cosmological principle (p. 534).
   Bouw uses inflation APPROVINGLY at p. 104 — stretching the heavens, Isaiah 40:22, "Modern
   astronomy refers to that as inflation" — which is the opposite of running the horizon
   problem against the big bang. The item is answered on its merits in §5 of the refutation
   rather than pinned on Bouw. Worth an assignment review; it is not evidence that no
   geocentrist source carries it.

7. THE HONEST LIMIT, E01-STYLE. The void/LTB literature is not a clean kill and must not be
   written as one. Zhang & Stebbins (PRL 107:041301, 2011) "rules out the adiabatic void
   model"; Moss, Zibin & Scott (PRD 83:103515, 2011) find voids "in severe tension with the
   data"; but Zibin & Moss (CQG 28:164005, 2011) say the kSZ constraint is "considerably
   weakened (though still impressive) under a fully relativistic treatment" and flag
   "theoretical ambiguities and observational shortcomings". Quote the caveat. A defender
   who finds it and we did not gets to say we cherry-picked.
"""

ENTRY = {

"R11": dict(

    tldr=("Item 293 says no observation can decide between the frames — and then it is filed "
          "as a proof, in a list of proofs. Bouw states the symmetry himself: dynamical proofs, "
          "he writes, are “not proofs of anything; nor are they proofs against the geocentric "
          "universe.” The cluster welds two unlike claims together — a change of coordinates, "
          "which has no content to test and so can never be evidence, and a genuinely "
          "inhomogeneous universe with us near its centre, which is a real theory George Ellis "
          "published in 1978, which got tested (by Ellis among others), and whose Gpc-scale "
          "void versions — the ones proposed as a replacement for dark energy — were in "
          "severe tension with the data by 2011. Bouw's own "
          "firmament is the second kind of claim, not the first."),

    passage=dict(
        work="WRK-BOUW-1992",
        pd=False,
        locator=("Appendix E, “Derivation of the Geocentric Equations for a Daily-Rotating "
                 "Universe”, closing paragraph, printed p. 747. Quoted from the Internet "
                 "Archive OCR of the 2013 edition — GEOCENTRICITY: CHRISTIANITY IN THE "
                 "WOODSHED, Association for Biblical Astronomy, ISBN 9781890120900, archive "
                 "item geocentricity-christianity-in-the-woodshed — and not from the 1992 "
                 "first edition our work record names; not checked against a print copy. "
                 "Three plain OCR artefacts are corrected: a comma for the full stop after "
                 "“earth”, “fina!” for “final”, and a comma for the closing full stop."),
        quote=("the physics of the geocentric universe accounts perfectly for what we see and "
               "measure of the daily rotation whether that rotation is of the earth within the "
               "universe or the universe around the earth. In the final analysis, proofs based "
               "on dynamical equations are not proofs of anything; nor are they proofs against "
               "the geocentric universe."),
        gloss="""<p><strong>Read the second clause.</strong> &ldquo;<em>Nor are they proofs against the geocentric universe.</em>&rdquo; The sentence is symmetric on its face, and Bouw means it symmetrically: two chapters earlier he applies the same rule to the Earth&rsquo;s equatorial bulge and concludes that it &ldquo;offers no proof for either heliocentric or geocentric theories&rdquo; (ch. 28, p. 425). This is a claim that a whole class of argument settles nothing <em>for anybody</em>. On the list it becomes item 293 in a document whose title and structure present every line as a proof.</p>
<p><strong>The chapter-1 version carries two more hedges, and they are the ones that vanish.</strong> At p. 4 the proposition is <em>other people&rsquo;s</em> and is granted only in part: &ldquo;The more subtle physicists, many of whom know well that the geocentric evidence is overwhelming, will claim, <em>with some justification</em>, that we can neither prove nor disprove the geocentric universe; but that we <em>likewise</em> can neither prove nor disprove the non-geocentric universe either.&rdquo; Attributed, part-granted, and explicitly two-way. The middle clause is quoted here in full because it cuts against us and an earlier draft of this entry elided it: it is not a remark elsewhere on the page but part of the same sentence, and it is Bouw asserting in his own voice that the geocentric evidence <em>is</em> overwhelming. Cut it and he reads as more tentative than he is. That is the tension this entry is about, not a hedge we can hide behind.</p>
<p><strong>Where item 310 comes from, and it is a real citation.</strong> Bouw&rsquo;s chapter&nbsp;36 note&nbsp;2 reads &ldquo;Ellis, G. F. R., 1978. <em>General Relativity and Gravitation</em>, 9:87. Quote is from page 92&rdquo;, and the paper is exactly what he says it is: George Ellis, co-author of <em>The Large Scale Structure of Space-Time</em>, showing that spherically symmetric static spacetimes &ldquo;can reproduce the same cosmological observations as the currently favored Friedmann-Robertson-Walker universes &hellip; provided that the universe is inhomogeneous and our galaxy is situated close to one of its centers.&rdquo; Nothing in that chain is invented. Two things about the note need saying, though, and neither is in the item&rsquo;s favour. The note is <em>not</em> attached to the equivalence result: the sentence it footnotes, at p.&nbsp;534, is Ellis on the cosmological principle being &ldquo;assumed for a priori reasons and not tested by observation&rdquo;. And where Bouw handles the construction itself, at pp.&nbsp;538&ndash;539, he does not transmit it as one of several models that fit &mdash; he calls it &ldquo;an oddity among cosmological models&rdquo; which &ldquo;is not without its problems&rdquo;, and reads it as a model that &ldquo;the preponderance of geocentric evidence in cosmology has finally forced&rdquo;. That last reading is the tension in a sentence: a claim that the evidence <em>decides</em>, in the same book as the claim that nothing can. What the chain drops is Ellis&rsquo;s next sentence, which lists the routes out &mdash; and which the field then took.</p>
<p><strong>What is established here is that the doctrine is Bouw&rsquo;s in print, not that it is Bouw&rsquo;s in origin.</strong> He attributes the proposition on p.&nbsp;4 to &ldquo;the more subtle physicists&rdquo; &mdash; that is, to other people; item&nbsp;318 could not be located in this text at all; and no earlier claimant was tested in this pass. This project records origin in three states rather than two, and the third is available here: the origination credit in our record is provisional, and is published as such.</p>
<p><strong>On the edition.</strong> Our work record names <em>Geocentricity</em> (1992). No copy of that first edition was reachable from here, so every quotation in this treatment is from the 2013 edition, retitled <em>Geocentricity: Christianity in the Woodshed</em>, which is complete and searchable on the Internet Archive. That the same doctrine was in the 1992 book is corroborated twice from outside it: Danny Faulkner&rsquo;s review of the 1992 edition (<em>Journal of Creation</em> 15(2), 2001) reports the model as &ldquo;a co-ordinate change from the Sun to the Earth&rdquo;, and Bouw&rsquo;s published reply to that review restates the position while discussing the 1992 book by name.</p>"""),

    steelman=dict(
        description="""<p><strong>SURFACE (weak &mdash; do not use).</strong> &ldquo;Of course there is a falsifier: the Foucault pendulum / stellar parallax / a gyroscope.&rdquo; Every one of those is answered inside the model by a rotating firmament that drags the local inertial frame, and a defender who has read Bouw will say so in one line. Equally weak: &ldquo;unfalsifiable claims are worthless.&rdquo; The claim on the table is that <em>nothing</em> discriminates, which is a claim about the evidence, and it has to be met with evidence rather than with a slogan about Popper &mdash; particularly against an author who devotes a page to rejecting Popper by name (ch. 26, pp. 407&ndash;408).</p>
<p><strong>DEEPER.</strong> Underdetermination is real, and the specific logical point Bouw makes is simply valid. He quotes Charles Lane Poor on Einstein&rsquo;s use of aberration &mdash; &ldquo;How can an experiment, equally well explained by several different theories, be a &lsquo;crucial test&rsquo; in favor of one of them?&rdquo; (ch. 33, p. 473) &mdash; and that is correct as stated. A phenomenon derivable from two theories does not adjudicate between them. Anyone who wants to answer this cluster by denying that principle will lose, because the principle is ours too.</p>
<p><strong>KERNEL.</strong> The strongest form is not Bouw&rsquo;s and is not theology. It is that <em>a named, credentialed relativist published the construction</em>. Ellis, GRG 9:87 (1978): spherically symmetric static general-relativistic cosmologies reproduce the same observations as FLRW &ldquo;provided that the universe is inhomogeneous and our galaxy is situated close to one of its centers.&rdquo; No retraction, erratum or correction is attached to that paper on the publisher&rsquo;s record page, which is where we looked; it seeded a live literature on Lema&icirc;tre&ndash;Tolman&ndash;Bondi models, and Ellis went on to argue in general terms that the Copernican principle is an assumption rather than a measurement (&ldquo;Issues in the Philosophy of Cosmology&rdquo;, 2006). Add the honest state of the standard alternative: the horizon problem is a real problem, inflation is its standard cure, and whether inflation is falsifiable at all is a fight being conducted in <em>Physics Letters B</em> and in the pages of <em>Scientific American</em> by the people who built the subject. A defender who says &ldquo;your own field cannot agree on what would refute its account of the initial data&rdquo; is not making that up. Concede all of it.</p>""",
        why_it_doesnt_save_claim="""<p>Because Ellis wrote the way out in the same abstract, and then helped take it. The 1978 paper ends its own claim with a scope: only <em>(i)</em> unverifiable a priori assumptions, <em>(ii)</em> detailed physical and astrophysical arguments, or <em>(iii)</em> observation of the time variation of cosmological quantities could tell us we do not live in such a spacetime. That is not a declaration of permanent undecidability; it is a specification of what work would have to be done. Route <em>(iii)</em> became Uzan, Clarkson &amp; Ellis, <em>PRL</em> 100:191303 (2008), redshift drift as a test of the Copernican principle &mdash; Ellis co-authoring a test of his own construction. Route <em>(ii)</em> became Caldwell &amp; Stebbins, <em>PRL</em> 100:191302 (2008), Clarkson, Bassett &amp; Lu, <em>PRL</em> 101:011301 (2008), and Zhang &amp; Stebbins, <em>PRL</em> 107:041301 (2011). The underdetermination was a research programme with an address, and somebody went there.</p>
<p>And it does not save <em>this</em> cluster in particular, because the Ellis construction and the Tychonic model are not the same object. Ellis&rsquo;s is a spacetime with a stress-energy tensor, a metric and a Hubble diagram to fit; it makes the Earth&rsquo;s <em>galaxy</em> near a centre and says nothing whatever about the Earth. Bouw knows this and says so in his own book: the Milky Way &ldquo;could just as well be viewed as located at the center of the cosmic shells &hellip; and the earth is not exactly at the center of the F-stars and G-stars, either. But that is where Scripture comes into play&rdquo; (ch. 36, p. 556). The published construction reaches a galaxy; the remaining distance to a planet is covered, in the source&rsquo;s own words, by Scripture. That is a candid sentence and it is fatal to item 293, which claims the gap is closed by the <em>absence</em> of evidence rather than left open by it.</p>"""),

    refutation="""<p><strong>First, the concession, and it is larger than the list probably expects.</strong> Two of the three things this cluster asserts are true. A coordinate change to an Earth-centred, Earth-fixed frame is exact, legal and performed several million times a day by every satellite receiver on the planet; nothing observable distinguishes a description from its relabelling, and no experiment ever will. And &ldquo;multiple cosmologies fit the data&rdquo; is not a crank line: George Ellis published one in <em>General Relativity and Gravitation</em> 9:87 (1978), showing that a static, spherically symmetric, <em>inhomogeneous</em> spacetime reproduces the same cosmological observations as the expanding models &ldquo;provided that &hellip; our galaxy is situated close to one of its centers.&rdquo; Anyone answering this cluster by asserting that no reputable cosmologist has ever written down an us-near-the-centre universe is wrong on the record and deserves to lose the exchange.</p>

<p><strong>Second, the fork, which is where the cluster comes apart.</strong> Those two concessions are not the same concession, and they cannot both do the job the list needs.</p>
<p>A change of <em>frame</em> is undecidable because it has no content. There is nothing to test, so nothing tests it, so it can never be evidence for anybody &mdash; and the same sentence protects &ldquo;the Earth orbits the Sun&rdquo;, which is equally a statement about coordinates until you say what is doing the accelerating. Say this plainly rather than let it be extracted: the physical content on both sides is the <em>relative</em> motion of matter plus the local inertial structure, and that is measured, not chosen. A change of <em>cosmology</em> &mdash; a universe genuinely inhomogeneous about us &mdash; is the opposite kind of thing. It is a different spacetime with a different stress-energy content, so it makes different predictions, so it is testable. Item 293 is safe because it is empty; item 310 is interesting because it is not. Welding them together buys the emptiness of the first and the interest of the second and is entitled to neither.</p>

<p><strong>Third, and this is the part that answers the source rather than the fragment: Bouw&rsquo;s own model is on the testable side of that fork, and he puts it there himself.</strong> His cosmos is not a relabelling. The firmament, he writes at p. 5, &ldquo;is a superdense medium that pervades all of space. It is the firmament that dictates the laws of physics, and it is the firmament that physically controls all motion.&rdquo; In Appendix E the centrifugal and Coriolis terms of the rotating frame are not bookkeeping: they &ldquo;keep the star in its place in the inertial field of the universe which is the gravitational field of the firmament&rdquo; (p. 746). He has an answer ready to the charge that all this is relabelling, and it deserves one back: Appendix E opens (pp. 740&ndash;741) by calling the step from a kinematic to a dynamic equation a &ldquo;sleight of hand&rdquo; &mdash; multiplying one side by <em>m</em>/<em>m</em> and calling the product physical &mdash; and he is right that a factor of <em>m</em> confers nothing. But that factor is not what puts his cosmos on the testable side of the fork. The medium is. A firmament that &ldquo;physically controls all motion&rdquo; and whose gravitational field is what holds a star in its place is a substance with properties, not a convention, whichever side of the equation the mass sits on. At p. 523 the model is stated as making predictions in so many words &mdash; &ldquo;Geocentricity predicts that earth&rsquo;s lack of motion is absolute &hellip; Geocentricity further predicts that rotation is relative&rdquo; &mdash; and, a page earlier, Sagnac interferometry is said to have &ldquo;been performed accurately enough to discern the period of absolute rotation of the firmament is the sidereal day&rdquo; (p. 522). That is a quantitative measurement of a physical medium, claimed as a result. A theory that predicts can fail; a theory whose medium has a gravitational field has a stress-energy tensor and consequences. So the source asserts a falsifiable cosmology in the body of the book and, in Appendix E, the proposition that no dynamical argument can settle anything either way. Both cannot be load-bearing. <strong>The list bought the second and kept spending the first</strong> &mdash; items 1, 2, 3 and 10 of the same document are Michelson&ndash;Morley, Michelson&ndash;Gale, Sagnac and Michelson&ndash;Pease, offered as experimental proof.</p>

<p><strong>Fourth, what happened to the interesting half after 1978.</strong> Ellis did not claim the question was closed; he specified what would open it &mdash; detailed physical arguments, or observation of the time variation of cosmological quantities. Both routes were built. Redshift drift as a Copernican-principle test: Uzan, Clarkson &amp; Ellis, <em>PRL</em> 100:191303 (2008), with Ellis co-authoring a test of his own 1978 construction. A general consistency test on <em>H</em>(<em>z</em>) and distance: Clarkson, Bassett &amp; Lu, <em>PRL</em> 101:011301 (2008). The reionised universe used as a mirror, so that the blackbody spectrum of the microwave background reports on our own gravitational potential: Caldwell &amp; Stebbins, <em>PRL</em> 100:191302 (2008), whose limits &ldquo;exclude the largest voids which mimic cosmic acceleration&rdquo;. The kinematic Sunyaev&ndash;Zel&rsquo;dovich power spectrum: Zhang &amp; Stebbins, <em>PRL</em> 107:041301 (2011), which &ldquo;rules out the adiabatic void model as a viable alternative to dark energy&rdquo;. And the combined-data fit: Moss, Zibin &amp; Scott, <em>Phys. Rev. D</em> 83:103515 (2011), using supernovae, the full CMB spectrum, radial baryon acoustic oscillations, the local Hubble rate, ages, big-bang nucleosynthesis, the Compton <em>y</em>-distortion and &sigma;<sub>8</sub>, and finding voids &ldquo;in severe tension with the data&rdquo;.</p>
<p><strong>State the limit of that as carefully as the papers do.</strong> This is not a clean kill and must not be sold as one. Zibin &amp; Moss, <em>Class. Quantum Grav.</em> 28:164005 (2011), revisited the kSZ bound under a fully relativistic treatment and found its constraining power &ldquo;considerably weakened (though still impressive)&rdquo;, flagging &ldquo;several theoretical ambiguities and observational shortcomings which further qualify the results&rdquo; &mdash; while still concluding that &ldquo;a very large class of void models is ruled out by the combination of kSZ and other methods&rdquo;. What is established is narrower than &ldquo;we are not near a centre&rdquo;: it is that the specific Gpc-scale inhomogeneous models proposed as a replacement for dark energy do badly against the data. That is enough to settle the point at issue here, which is not whether such a universe is conceivable but whether <em>no falsifier exists</em>. Falsifiers were designed, published in <em>Physical Review Letters</em>, and applied.</p>

<p><strong>Fifth, item 318 and the horizon problem, which deserves a straight answer.</strong> The problem is real: in an expanding universe without inflation, patches of the last-scattering surface more than a degree or two apart were never in causal contact, yet their temperatures agree to about one part in 10<sup>5</sup>. It is also true that the standard cure is contested by serious people &mdash; Ijjas, Steinhardt &amp; Loeb, <em>Phys. Lett. B</em> 723:261 (2013), and again in <em>Scientific American</em> in February 2017, argued that inflation as practised had stopped being falsifiable; thirty-three physicists including Guth, Linde, Kaiser and Nomura replied in the same magazine in May 2017, and the authors replied to the reply. Pointing at that argument is not a foolish thing to do.</p>
<p>But does putting the observer at a centre solve it? Partly, and at a price that is itself measurable. A spherically symmetric model about us makes <em>angular</em> isotropy automatic, which is the appeal; it does not explain radial uniformity, which becomes a choice of initial data rather than a consequence of anything, so the tuning is moved rather than removed. And it converts a tuned initial condition into a tuned <em>position</em> &mdash; which, unlike the initial condition, can be measured. Alnes &amp; Amarzguioui, <em>Phys. Rev. D</em> 74:103520 (2006), computed how far off-centre an observer in such a model may sit before the induced dipole exceeds the observed one: &ldquo;within a radius of 15 Mpc from the center&rdquo;. Fifteen megaparsecs is roughly fifty million light-years. It is a bound on the position of a <em>galaxy</em>. None of the results cited above &mdash; Alnes &amp; Amarzguioui, Caldwell &amp; Stebbins, Clarkson, Bassett &amp; Lu, Zhang &amp; Stebbins, Moss, Zibin &amp; Scott &mdash; constrains an observer&rsquo;s position at better than megaparsec resolution, and at that resolution the Earth and the Milky Way are the same point. The source agrees: Bouw&rsquo;s own chapter 36 grants that the Milky Way would serve as well as the Earth and that the Earth is not at the centre of the nearby stellar distribution, then names Scripture as what closes the gap. One further note on provenance: a search of the full 2013 OCR text located no occurrence of the phrase &ldquo;horizon problem&rdquo;, and Bouw invokes inflation <em>approvingly</em> at p. 104, as the mechanism by which starlight reaches a young Earth. Item 318 is answered here on its merits; it is not laid at his door.</p>

<p><strong>Sixth, the cost of spending this argument.</strong> R11 is a universal solvent and it dissolves the hand that holds it. If dynamical arguments prove nothing either way, then Michelson&ndash;Gale is not evidence, Sagnac is not evidence, &ldquo;Airy&rsquo;s failure&rdquo; is not evidence and Miller&rsquo;s drift is not evidence &mdash; and every one of those appears elsewhere on this same list as an experiment that came out the geocentrist&rsquo;s way. <a href="#ARG-R03">ARG-R03</a> makes the same observation about the relativity principle; R11 is the sharper case, because R03 at least leaves the geocentrist his experiments while R11 explicitly retires them. Bouw took the consistent route and said what does the deciding: for a Bible believer, he writes at the conclusion of chapter 2, the scriptural point &ldquo;should be enough&rdquo; (p. 15). That is a coherent position. It is not, however, a proof, and it cannot be counted three times in a list of 461 of them.</p>

<p><strong>Verdict: self-contradicted.</strong> Not because the underlying physics is wrong &mdash; the frame half is trivially right and the cosmology half was a legitimate open question in 1978 &mdash; but because the three items cannot be held together with the rest of the document, or with each other, or with their own source. A claim that no observation discriminates, filed as an observation-based proof; a claim that the equations are identical, filed beside forty items claiming that the experiments came out one way; and a construction whose author specified the tests, ran one of them, and reported that the models it supports are in trouble.</p>""",

    advocate=dict(
        best_defense=(
            "You have spent four paragraphs refuting Lemaître–Tolman–Bondi void cosmology, "
            "which is not our model and never was. Bouw proposed no void, needed no "
            "replacement for dark energy, and is not touched by a kSZ bound on models built "
            "to abolish it. You found a literature with our shape and killed that instead. "
            "Second: you concede the frame point completely and then act as though the "
            "concession is a defeat. If a coordinate change has no content, then the "
            "sentence 'the Earth goes round the Sun' has no content either — you say so "
            "yourself — and every textbook that teaches it as a fact about the world is "
            "doing what you accuse us of. Third, your fifteen-megaparsec bound is the "
            "strangest thing on the page. That is a constraint derived inside a model that "
            "HAS a centre, and it says the data permit us to be at it. Standard cosmology "
            "has no centre at all; ours does; the measurement is consistent with ours. You "
            "have quoted a result in our favour and formatted it as a rebuke. Fourth, and "
            "worst: you have taken our author's honesty and called it contradiction. Bouw "
            "told his readers plainly that the astronomical evidence does not single out the "
            "Earth as against the Galaxy and that Scripture is what settles it. Every "
            "cosmologist on your citation list holds a metaphysical commitment they do not "
            "print on the same page as their data — and when three of them said so out loud "
            "about inflation, it took thirty-three signatures to shout them down. Bouw wrote "
            "his premise where you could find it. You found it, and used it against him."),
        survives=4,
        preemptive=(
            "Four, and the number is set by the first and third moves, not the fourth. Four "
            "concrete requirements on the body text, all of them already present and none of "
            "which may be edited out. (a) THE VOID-MODEL SECTION MUST STAY LABELLED. §4 "
            "answers item 310 and Ellis's construction, not Bouw's Tychonic cosmos, and the "
            "text says so — if an editor ever lets those paragraphs read as a refutation of "
            "Bouw, the strongest section becomes the most vulnerable. The reason Bouw's own "
            "model is not tested there is stated in §3 and in note 4 of this file: Appendix E "
            "(pp. 740-747) ends at F = ma for a single star (eq. 12); no field equation, "
            "stress-energy tensor or cosmological solution appears anywhere in it, so there is "
            "no fit to run. That is a statement about what the appendix contains, and it must "
            "stay one - and it must stay THAT one: the earlier wording, 'derives the "
            "rotating-frame accelerations and stops', was false about the appendix, which "
            "carries on past eq. 11 to F = ma and applies it to sun, moon, planets, satellites "
            "and light. Do not reintroduce it. (b) THE "
            "SYMMETRY MUST BE CONCEDED IN OUR OWN VOICE, FIRST. §2 already says that 'the "
            "Earth orbits the Sun' is equally a statement about coordinates until you say "
            "what is accelerating. Never let that sentence be deleted as a hostage to "
            "tidiness; it is the difference between a fair page and a page that gets quoted "
            "against us. (c) THE 15 Mpc BOUND MUST BE PRESENTED AS A BOUND ON A GALAXY. It "
            "is not offered as a refutation and must never be phrased as one; the work in "
            "that paragraph is done by the gap between a galaxy and a planet, and by Bouw's "
            "own sentence closing that gap with Scripture. (d) ON THE LAST MOVE, CONCEDE AND "
            "REDIRECT. The defender is right that Bouw's candour is a virtue and the page "
            "should say so — §6 already calls his position coherent. The answer is not that "
            "he was dishonest but that the LIST is doing something he did not: he wrote the "
            "premise where a reader could find it, and the list publishes the conclusion with "
            "the premise removed and the count inflated to three. Do not answer the "
            "inflation-schism jab by defending inflation; answer it by noting that the "
            "argument was conducted in public, in Physics Letters B and in a magazine, over "
            "which observations would settle it — which is the behaviour item 293 says is "
            "impossible."),
    ),

    straw_man=dict(
        identified=True,
        detail=("Two misrepresentations of the other side travel with this argument in the source. "
                "First, motive: relativity is described as \"the most sophisticated argument "
                "designed against the geocentric universe\" and as having been \"invented to keep "
                "the earth moving around the sun\" (ch. 1, p. 4). Special relativity was "
                "constructed to reconcile Maxwell's electrodynamics with mechanics; the geocentric "
                "question is not among the problems it was built to solve, and treating an "
                "unwelcome result as evidence of design against oneself is the move the source "
                "objects to when it is made about Scripture. Second, the target: the position "
                "attacked is that some experiment has proved the Earth to be in absolute motion. "
                "Mainstream physics has not made that claim since 1905, and the exception is one "
                "the movement itself cites: Dayton Miller, whose Mount Wilson ether-drift "
                "programme ran into the 1930s and whose summary paper is titled \"The Ether-Drift "
                "Experiment and the Determination of the Absolute Motion of the Earth\" (Rev. Mod. "
                "Phys. 5:203, 1933), is item 100 of this same list. Miller was a credentialed "
                "physicist, so anyone answering with a flat \"no physicist has ever held that\" "
                "loses the exchange in one move; what Miller was not is the mainstream, and it is "
                "the mainstream the source is describing. The claims actually made there are that the "
                "Earth rotates relative to the local inertial structure and revolves about the "
                "Solar-System barycentre - both relative, both measured - which is why the "
                "demand for a proof of absolute motion, and the report that none has been "
                "supplied, lands on Newton rather than on anyone now living."),
    ),

    compression=dict(
        assessed=True, drifted=True,
        list_phrasing="No falsifier distinguishing frames. / Multiple cosmologies fit data. / Horizon problem Earth initial data.",
        source_wording=("“the physics of the geocentric universe accounts perfectly for what we see "
                        "and measure of the daily rotation … In the final analysis, proofs based on "
                        "dynamical equations are not proofs of anything; <em>nor are they proofs "
                        "against the geocentric universe.</em>” (Appendix E, p. 747) — and, at p. 4, "
                        "“The more subtle physicists, many of whom know well that the geocentric "
                        "evidence is overwhelming, will claim, <em>with some justification</em>, "
                        "that we can neither prove nor disprove the geocentric universe; but that we "
                        "<em>likewise</em> can neither prove nor disprove the non-geocentric universe "
                        "either.”"),
        drift_type="force_upgraded",
        note=("The wording barely moves and the <em>speech act</em> moves completely, which is the "
              "R01 pattern in a different book. In <em>Geocentricity</em> the proposition is a "
              "<strong>symmetric disclaimer</strong>: dynamical arguments prove nothing for either "
              "side, and Bouw applies it against his own side too &mdash; the Earth&rsquo;s "
              "oblateness &ldquo;offers no proof for either heliocentric or geocentric theories&rdquo; "
              "(p. 425). On the list it appears three times in a document that presents every line "
              "as a proof, so a statement that the evidence is silent is filed as evidence. "
              "<strong>Two further qualifications are dropped on the way.</strong> At p. 4 the "
              "proposition belongs to <em>&ldquo;the more subtle physicists&rdquo;</em> and is granted "
              "only <em>&ldquo;with some justification&rdquo;</em>; the list states it flat and in the "
              "source&rsquo;s own name. And item 310&rsquo;s pedigree runs through a citation Bouw "
              "gets right &mdash; Ellis, <em>GRG</em> 9:87 (1978) &mdash; whose abstract attaches an "
              "explicit escape clause naming the arguments and observations that would decide the "
              "matter; the clause does not survive into the item, and the field spent 2008&ndash;2011 "
              "acting on it. <strong>Bouw&rsquo;s own handling of Ellis drifts the other way, and "
              "it is worth publishing against us as well as against the item:</strong> at p. 539 "
              "he calls the model &ldquo;an oddity among cosmological models&rdquo; that &ldquo;is "
              "not without its problems&rdquo;, and reads it not as underdetermination but as a "
              "model the &ldquo;preponderance of geocentric evidence in cosmology has finally "
              "forced&rdquo; &mdash; a claim that the evidence decides, which is nearer the opposite "
              "of item 310 than a restatement of it. <strong>The refutation above answers the "
              "source, not the fragment:</strong> "
              "it concedes the frame point outright, concedes that a reputable inhomogeneous "
              "cosmology was published in a mainstream journal and carries no retraction on the "
              "publisher&rsquo;s record, quotes the caveat that the void-model "
              "constraints are weaker than the headline results suggest, and puts the weight on the "
              "fact that Bouw&rsquo;s own firmament is a physical medium with a gravitational field "
              "that makes predictions he reports as measured. A third item, 318, invokes the horizon "
              "problem; a search of the full 2013 OCR text located no occurrence of that phrase, and "
              "Bouw invokes inflation approvingly at p. 104, so that item is answered on its merits "
              "rather than attributed to him."),
    ),

    verdict_challenge=dict(challenged=False, proposed_verdict=None, reasoning=None),

    people=["PER-BOUW"],
    related=["R01", "R02", "R03", "R05", "R06", "R08", "R12", "E01", "A02", "A03"],

    sources=[
        dict(label="Bouw, Geocentricity: Christianity in the Woodshed (2013 edition of "
                   "Geocentricity, Association for Biblical Astronomy) — full scan and OCR; "
                   "Appendix E conclusion p. 747, the ch. 1 statements pp. 3–5, the firmament's "
                   "predicted rotation p. 523 and the Sagnac sidereal-day claim p. 522, "
                   "oblateness p. 425, Ellis at pp. 538–539, the Milky-Way concession p. 556",
             url="https://archive.org/details/geocentricity-christianity-in-the-woodshed"),
        dict(label="Bouw, “GEOCENTRICITY: A Fable for Educated Man?” — his reply to Faulkner, "
                   "discussing the 1992 book by name: “Is the Scripture to be the final "
                   "authority on all matters on which it touches, or are scholars to be the "
                   "ultimate authority?”",
             url="https://www.geocentricity.com/~geocent1/ba1/fresp/index.html"),
        dict(label="Faulkner, “Geocentrism and Creation”, Journal of Creation 15(2), 2001 — a "
                   "review of the 1992 edition; “the essential difference between the "
                   "heliocentric and Tychonian models is a co-ordinate change from the Sun to "
                   "the Earth”",
             url="https://creation.com/geocentrism-and-creation"),
        dict(label="Ellis, “Is the universe expanding?”, Gen. Rel. Grav. 9:87–94 (1978) — the "
                   "construction Bouw cites, with its own escape clause in the abstract",
             url="https://link.springer.com/doi/10.1007/BF00760145"),
        dict(label="Ellis, “Issues in the Philosophy of Cosmology” (2006) — the Copernican "
                   "principle as an assumption, argued by the man who wrote the 1978 paper",
             url="https://arxiv.org/abs/astro-ph/0602280"),
        dict(label="Uzan, Clarkson & Ellis, “Time drift of cosmological redshifts as a test of "
                   "the Copernican principle”, PRL 100:191303 (2008)",
             url="https://arxiv.org/abs/0801.0068"),
        dict(label="Caldwell & Stebbins, “A Test of the Copernican Principle”, PRL 100:191302 "
                   "(2008) — spectral-distortion limits “exclude the largest voids which mimic "
                   "cosmic acceleration”",
             url="https://arxiv.org/abs/0711.3459"),
        dict(label="Clarkson, Bassett & Lu, “A general test of the Copernican Principle”, "
                   "PRL 101:011301 (2008)",
             url="https://arxiv.org/abs/0712.3457"),
        dict(label="Zhang & Stebbins, “Confirmation of the Copernican principle at Gpc radial "
                   "scale and above from the kinetic Sunyaev–Zel'dovich effect power spectrum”, "
                   "PRL 107:041301 (2011)",
             url="https://arxiv.org/abs/1009.3967"),
        dict(label="Moss, Zibin & Scott, “Precision cosmology defeats void models for "
                   "acceleration”, Phys. Rev. D 83:103515 (2011) — voids “in severe tension "
                   "with the data”",
             url="https://arxiv.org/abs/1007.3725"),
        dict(label="Zibin & Moss, “Linear kinetic Sunyaev–Zel'dovich effect and void models for "
                   "acceleration”, Class. Quantum Grav. 28:164005 (2011) — the caveat: the kSZ "
                   "constraint is “considerably weakened (though still impressive)” relativistically",
             url="https://arxiv.org/abs/1105.0909"),
        dict(label="Alnes & Amarzguioui, “CMB anisotropies seen by an off-center observer in a "
                   "spherically symmetric inhomogeneous universe”, Phys. Rev. D 74:103520 (2006) "
                   "— the observer must sit “within a radius of 15 Mpc from the center”",
             url="https://arxiv.org/abs/astro-ph/0607334"),
        dict(label="Ijjas, Steinhardt & Loeb, “Inflationary paradigm in trouble after "
                   "Planck2013”, Phys. Lett. B 723:261–266 (2013)",
             url="https://arxiv.org/abs/1304.2785"),
        dict(label="Ijjas, Steinhardt & Loeb, “Cosmic Inflation Theory Faces Challenges” "
                   "(“Pop Goes the Universe”), Scientific American, February 2017",
             url="https://www.scientificamerican.com/article/cosmic-inflation-theory-faces-challenges/"),
        dict(label="“A Cosmic Controversy”, Scientific American, 10 May 2017 — the reply signed "
                   "by 33 physicists including Guth, Kaiser, Linde and Nomura, with the authors' "
                   "counter-reply",
             url="https://www.scientificamerican.com/article/a-cosmic-controversy/"),
    ]),
}
