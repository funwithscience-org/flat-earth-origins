# -*- coding: utf-8 -*-
"""Batch 8 — R04. The equivalence principle validates a local rest frame.

Research notes for whoever picks this up next.

1. THE VOLUME I CONTENTS PAGE IS REACHABLE AND THE ARGUMENT'S OWN TEXT IS NOT.
   The Internet Archive PDF at item GallileoWasWrong renders far enough for the
   fetcher to return the title page and the whole table of contents, and no
   further: title page "Volume I: The Scientific Evidence", ISBN 0-9779640-0-0,
   completion note dated 25 April 2006. That contents page is worth more than it
   looks. Chapter 10, "Mathematical Models of a Geocentric Universe" (p. 590),
   runs: Absolute Rest versus Relative Motion 591, The Gyroscopic Effect on Earth
   599, Einstein's Geocentrism 607, Thirring's Geocentrism 611, Rosser's 616,
   Bondi's 619, Brill and Cohen's 623, Moon and Spencer's 623, Moller's 624,
   Brown's 625, Nightingale's 625, Lynden-Bell's 626, Barbour and Bertotti's 628.
   That is where this cluster's argument lives, and it is a reading list of the
   real inertial-dragging literature. The section text itself was NOT read here.
   Volume and page are recorded; wording is not.

2. THE SAME CONTENTS PAGE CARRIES "The Failure of General Relativity" (ch. 5,
   p. 334) and "The Demise of Relativity Theory" (ch. 7, p. 441). Whatever the
   book is doing with relativity, it is not resting its case on it.

3. SUNGENIS HAS SAID SO IN HIS OWN WORDS, TWICE, IN DOCUMENTS THAT ARE READABLE.
   Reply to Discover Magazine (answering Phil Plait's Bad Astronomy post of
   14 September 2010): "A geocentrist appeals to Relativity not as proof or even
   evidence for geocentrism but merely to show modern scientists like Mr. Plait
   ... that, by using modern scientific concepts, geocentrism can have just as
   much scientific respectability as heliocentrism", and "the geocentrist makes
   his case for geocentrism on solid scientific evidence that has little or
   nothing to do with Relativity." And in the undated Simran Matthews interview:
   General Relativity "not only supports geocentrism as a 'relative' alternative,
   but also modified the postulates of STR". That is the R01 shape exactly — a
   permission, offered as a permission, arriving on the list as proof item.

4. TWO RECORD ISSUES, NEITHER TOUCHED, BOTH REPORTED UP.
   (a) works.py WRK-SUNGENIS-2006 gives the title as "Galileo Was Wrong: The
       Church Was Right" and Vol. I's subtitle as "The Scientific Case for
       Geocentrism". The 2006 scan's own title page reads "Galileo Was Wrong: The
       Scientific, Scriptural, Ecclesiastical and Patristic Evidence for
       Geocentrism / Volume I: The Scientific Evidence". Both strings are real —
       later editions carry the "Church Was Right" wording — but the imprint line
       does not say which edition it is describing.
   (b) The five items are not one argument. 316 is the equivalence principle;
       57 and 132 are the same claim with "local" removed; 28 and 130 are
       Einstein's relativity of motion and his conventionalist remark, which are
       R01's and R08's material. The verdict is right for all five, so this is
       not a verdict_challenge — it is a composition note for the parent.
"""

ENTRY = {

"R04": dict(
    tldr=("The equivalence principle is true, it has been tested to about a part in 10¹⁵, "
          "and it really does hand you a rest frame — it hands one to every freely falling "
          "observer in the universe, which is precisely why it singles the Earth out from "
          "nothing. Its whole content is the word local: a falling lift is indistinguishable "
          "from no gravity only across a region small enough that tidal effects stay under "
          "your instrument's threshold, and with a chip-sized gravimeter that threshold "
          "arrives at about 13 cm of height difference. Worse for the argument, the local "
          "frame the principle supplies is the non-rotating one a gyroscope defines — so it "
          "is not a licence for a stationary Earth, it is the standard against which the "
          "Earth's rotation is measured, and the Wettzell ring laser reads that rotation to "
          "better than a part in 10⁹."),

    passage=dict(
        work="WRK-SUNGENIS-2006", pd=False,
        locator=("Vol. I (2006), contents pages vi–xi of the Internet Archive scan (item "
                 "GallileoWasWrong), whose title page reads “Volume I: The Scientific "
                 "Evidence” and whose ISBN is 0-9779640-0-0. Chapter 10 opens at printed "
                 "p. 590; the section text at p. 607 was not read here"),
        quote=("The Failure of General Relativity 334 — The Demise of Relativity Theory 441 "
               "— Chapter 10: Mathematical Models of a Geocentric Universe 590 — Absolute "
               "Rest versus Relative Motion 591 — The Gyroscopic Effect on Earth 599 — "
               "Einstein's Geocentrism 607 — Thirring's Geocentrism 611"),
        gloss="""<p>What is quoted above is the book&rsquo;s own table of contents, and it is quoted because that is the part of this work we were able to read. The Internet Archive PDF renders far enough for a fetcher to return the front matter and the full contents listing and no further; the chapters themselves stop being retrievable long before p. 607. <strong>So the volume, chapter and page of this argument are recorded here and its wording is not.</strong> Anyone with the printed book should read ch. 10 pp. 590&ndash;637 and correct this entry.</p>
<p>Even so, the contents page settles three things a reader should have.</p>
<p><strong>Where the argument lives.</strong> Chapter 10, &ldquo;Mathematical Models of a Geocentric Universe&rdquo; (p. 590), runs: <em>Absolute Rest versus Relative Motion</em> 591, <em>The Gyroscopic Effect on Earth</em> 599, <em>Einstein&rsquo;s Geocentrism</em> 607, <em>Thirring&rsquo;s Geocentrism</em> 611, then Rosser 616, Bondi 619, Brill and Cohen 623, M&oslash;ller 624, Lynden-Bell 626, Barbour and Bertotti 628. That is not a list of cranks. Brill and Cohen&rsquo;s &ldquo;Rotating Masses and Their Effect on Inertial Frames&rdquo; (<em>Phys. Rev.</em> 143:1011, 1966) is a real result about a real effect, and the steelman below is built out of it.</p>
<p><strong>Which volume this is, in which year.</strong> In the 2006 printing these are chapters of <em>Volume I</em>. In the seventh edition of 2013 the work was rearranged into three volumes and chapters 7&ndash;13 became <em>Volume II</em> &mdash; the identity our ARG-E03 and ARG-R01 entries had to establish the hard way. So the same chapter 10 is Vol. I in 2006 and Vol. II in 2013, and page citations in the critical literature to &ldquo;vol. 1, 9th ed.&rdquo; will not line up with this scan&rsquo;s pagination. Ours is the 2006 first printing throughout.</p>
<p><strong>What the book announces about relativity.</strong> The same volume that models a geocentric universe on Thirring and Brill&ndash;Cohen also runs sections titled <em>The Failure of General Relativity</em> (ch. 5, p. 334) and <em>The Demise of Relativity Theory</em> (ch. 7, p. 441). That is not a contradiction on the authors&rsquo; part, and it should not be reported as one: the appeal to relativity is dialectical, and Sungenis says so himself in documents that are readable. Answering Phil Plait&rsquo;s <em>Bad Astronomy</em> post of 14 September 2010 he writes that <em>&ldquo;a geocentrist appeals to Relativity not as proof or even evidence for geocentrism&rdquo;</em> but to show that geocentrism &ldquo;can have just as much scientific respectability as heliocentrism&rdquo;, and adds that <em>&ldquo;the geocentrist makes his case for geocentrism on solid scientific evidence that has little or nothing to do with Relativity.&rdquo;</em> In an undated interview he puts the positive claim at its own strength: general relativity <em>&ldquo;not only supports geocentrism as a &lsquo;relative&rsquo; alternative&rdquo;</em>. A relative alternative, offered as respectability rather than evidence, is what the list has turned into &ldquo;Equivalence principle validation.&rdquo;</p>"""),

    steelman=dict(
        description="""<p><strong>SURFACE (weak &mdash; do not use).</strong> &ldquo;They do not understand the equivalence principle.&rdquo; There is no evidence for that here and the move loses the exchange. The chapter this cluster comes from is organised around Thirring, Rosser, Bondi, Brill and Cohen, M&oslash;ller, Lynden-Bell, and Barbour and Bertotti &mdash; the actual general-relativity literature on rotating frames and inertial dragging. Whatever is wrong with the conclusion, the reading behind it is not imaginary.</p>
<p><strong>DEEPER.</strong> &ldquo;Local is not global.&rdquo; True, and the whole answer in one line, but incomplete as stated, because it invites the obvious reply: <em>where does local end?</em> If the boundary is a hand-wave, the objection is a hand-wave. It is not a hand-wave, and the third section of the refutation gives the boundary in centimetres.</p>
<p><strong>KERNEL.</strong> The specific true thing is that Einstein himself did not stop at the falling lift. In the 1916 general-relativity paper he extended the equivalence heuristic to rotating systems, treating the centrifugal field an observer finds in a rotating frame as a gravitational field he may ascribe to the rest of the matter in the universe &mdash; and that Machian instinct was later given equations. Thirring in 1918, and Brill and Cohen in 1966, showed that a rotating mass shell really does drag the inertial frames in its interior around with it, the dragging becoming complete in the limit where the shell approaches its own gravitational radius. So the geocentric position here is not &ldquo;physics forbids it and we do not care&rdquo;. It is: <em>the local inertial frame is not laid down in advance, it is determined by the matter around it; there is a published mechanism by which distant matter fixes it; therefore an Earth taken as non-rotating with the cosmos turning about it is a physically discussable arrangement, not a category error.</em> Concede every word of that.</p>""",
        why_it_doesnt_save_claim="""<p>Because the kernel&rsquo;s own content is that <strong>the local inertial frame is a physical thing you can go and measure</strong> &mdash; and the moment it is physical rather than conventional, &ldquo;does the Earth turn with respect to it?&rdquo; stops being a matter of viewpoint and becomes a reading on an instrument. The equivalence principle is what makes the question well posed. It supplies the standard; the standard has been read; it reads 15.04&deg; per hour.</p>
<p>And the two halves of the kernel are not the same claim. The equivalence principle fixes a <em>local</em> frame at each event and says nothing whatever about how the matter of the universe is arranged or moving. Frame dragging is a statement about how the matter is arranged and moving &mdash; a solution of the field equations with a stress-energy tensor, boundary conditions and a fit to observation. The geocentric conclusion needs the second and cites the first. Nothing in the equivalence principle entails that the cosmos is a rotating shell, and no amount of local validity ever adds up to a cosmological one: that is what &ldquo;local&rdquo; means.</p>
<p>Finally, the licence is not exclusive. The principle grants a local rest frame to a free-falling observer in Neptune&rsquo;s atmosphere, to a probe in the Kuiper belt, and to a grain of dust in the Coma cluster, on exactly the same terms. A principle that hands a rest frame to everybody distinguishes nobody &mdash; the same symmetry that sinks the covariance argument at <a href="#ARG-R01">ARG-R01</a>.</p>"""),

    refutation="""<p><strong>First, the concession, in full.</strong> The equivalence principle is true and is among the best-tested statements in physics. The MICROSCOPE satellite&rsquo;s final result puts the E&ouml;tv&ouml;s ratio for titanium against platinum at &eta; = [&minus;1.5 &plusmn; 2.3 (stat) &plusmn; 1.5 (syst)] &times; 10<sup>&minus;15</sup> &mdash; no violation at a part in 10<sup>15</sup>. Will&rsquo;s standard statement of the Einstein equivalence principle has three parts: the weak principle holds; &ldquo;the outcome of any <em>local</em> non-gravitational experiment is independent of the velocity of the freely-falling reference frame in which it is performed&rdquo;; and &ldquo;the outcome of any <em>local</em> non-gravitational experiment is independent of where and when in the universe it is performed.&rdquo; Both operative clauses carry the same qualifier, and it is not decoration. A local rest frame is validated. The verdict on this cluster is <em>standard physics</em> for that reason and no other.</p>
<p><strong>Second, notice who else is covered.</strong> Every freely falling observer at every event in every spacetime gets the same licence. If the equivalence principle validated a stationary Earth it would equally validate a stationary Enceladus, a stationary asteroid and a stationary hydrogen atom in intergalactic space, each entitled to declare the rest of the universe in motion about it. The principle is universal, and a universal permission confers no distinction on any particular recipient. This is the same structure as the Kretschmann objection at <a href="#ARG-R01">ARG-R01</a>: an argument that the formalism is neutral cannot then be cited as evidence that the formalism favours you.</p>
<p><strong>Third, what &ldquo;local&rdquo; costs, in centimetres.</strong> The falling-lift picture is exact only in a uniform field, and the Earth&rsquo;s field is not uniform: it converges on a centre and falls off with distance. The residue is tidal, and it is the thing that tells you the region is not small enough. Two numbers fix the scale at the Earth&rsquo;s surface. Vertically, gravity weakens with height at 2<em>g</em>/<em>R</em> &asymp; 3.08 &times; 10<sup>&minus;6</sup> s<sup>&minus;2</sup> &mdash; the free-air gradient geodesists carry as 0.3086 mGal per metre. Horizontally, two plumb lines both point at the Earth&rsquo;s centre and so converge at <em>g</em>/<em>R</em> &asymp; 1.54 &times; 10<sup>&minus;6</sup> m s<sup>&minus;2</sup> for every metre of separation. Those two numbers are components of the Riemann tensor. They are the curvature, they are what geodesic deviation measures, and <strong>no change of coordinates removes them</strong>: the metric can be brought to Minkowski form and its first derivatives to zero at a point, never its second derivatives.</p>
<p>So the boundary of &ldquo;local&rdquo; is not a philosopher&rsquo;s vagueness. It is set by the sensitivity of whatever you carry into the lift, and it moves as instruments improve. A chip-scale MEMS gravimeter demonstrated at 40 &micro;Gal Hz<sup>&minus;&frac12;</sup> (4 &times; 10<sup>&minus;7</sup> m s<sup>&minus;2</sup>) resolves the vertical gradient across a height difference of 4&times;10<sup>&minus;7</sup> &divide; 3.086&times;10<sup>&minus;6</sup> &asymp; 0.13 m, and the same device recorded the solid-Earth tide &mdash; the Moon and Sun stretching the ground under a laboratory bench &mdash; which is a curvature effect being read out on a silicon chip. <strong>Thirteen centimetres.</strong> That is the size of the region over which the equivalence principle licenses you to say there is no gravity here, given a gravimeter you can hold in one hand. The claim on the list asks that the same licence be carried out to the edge of the observable universe, about 4.4 &times; 10<sup>26</sup> m. Between the warrant and the conclusion lie some twenty-seven orders of magnitude, and the warrant expires at the first of them.</p>
<p><strong>Fourth &mdash; and this is where the argument turns over &mdash; the frame the principle supplies is not rotating.</strong> A local inertial frame is not only one in free fall; its axes are the ones a gyroscope keeps, Fermi&ndash;Walker transported along the observer&rsquo;s worldline. Rotation with respect to that frame is a local, coordinate-free, physical observable, and it is not something the equivalence principle lets you talk your way out of. There is a clean technical reason why not. The centrifugal term in a rotating frame is a static field and can be traded against gravity in the equivalence-principle way; the Coriolis term cannot, because it depends on the test body&rsquo;s <em>velocity</em>, and no static gravitational field imitates a velocity-dependent force. What can imitate it is a gravitomagnetic field &mdash; off-diagonal time&ndash;space components of the metric &mdash; and producing one requires a specified distribution of moving matter. That is a dynamical claim, owed a solution, and it is not a consequence of the equivalence principle.</p>
<p>Meanwhile the observable has been read, repeatedly and by unrelated methods. Foucault&rsquo;s pendulum precesses at &Omega;&nbsp;sin&nbsp;&phi;, about 11.3&deg; per hour at the latitude of Paris, in a closed room with no view of the sky. Ring laser gyroscopes at Wettzell resolve the Earth&rsquo;s angular rate to better than one part in 10<sup>9</sup>. Gravity Probe B flew four gyroscopes precisely to test what a local inertial frame does, and returned a geodetic drift of &minus;6,601.8 &plusmn; 18.3 mas/yr against a predicted &minus;6,606.1, and a frame-dragging drift of &minus;37.2 &plusmn; 7.2 against &minus;39.2 &mdash; a confirmation of exactly the Machian-flavoured effect the steelman rests on, at roughly ten orders of magnitude too small to be a diurnal rotation. <strong>The equivalence principle does more than fail to deliver a stationary Earth. It defines the compass against which the Earth&rsquo;s rotation is measured, and the compass says 15.04&deg; per hour.</strong></p>
<p><strong>Fifth, the compass wobbles with the weather.</strong> This is the part a defender should be shown early rather than late. The Earth&rsquo;s rotation rate is not constant: length-of-day varies at the millisecond level, and &ldquo;shifts in zonal wind patterns and atmospheric circulation are responsible for around 90% of seasonal length of day variations&rdquo;, with El Ni&ntilde;o events associated with longer days and La Ni&ntilde;a with shorter ones. On the reading where the Earth is truly at rest and the cosmos physically turns about it, that signal has to be transferred to the cosmos: the rotation of every distant galaxy must speed up and slow down in step with the trade winds over the Pacific, and must do so instantaneously enough to keep the sky rigid. Angular momentum exchanged between the atmosphere and the solid Earth is a local bookkeeping entry; on the geocentric reading it becomes a cosmological one.</p>
<p><strong>Sixth, three different principles are being run together as one.</strong> The five items in this cluster are not five statements of a single claim. Item 316, &ldquo;Equivalence local labs rest&rdquo;, is the equivalence principle proper, and it keeps the qualifier that makes it true. Items 57 and 132 are the same sentence with &ldquo;local&rdquo; taken out, at which point they assert something that lies outside the principle&rsquo;s scope. Items 28 and 130, &ldquo;Einstein&rsquo;s equivalence of motion&rdquo; and &ldquo;Einstein admission of equivalence&rdquo;, are not about the equivalence principle at all: they are the general relativity of motion and Einstein&rsquo;s conventionalist remark about the sun and the earth, answered at <a href="#ARG-R01">ARG-R01</a> and <a href="#ARG-R08">ARG-R08</a>. Three principles, three different fates. The equivalence principle is local and true. General covariance is global and, since Kretschmann in 1917, empty of physical content. Machian dragging is dynamical, real, measured &mdash; and nobody in this literature has produced the cosmological solution that would be needed to scale it to a daily rotation, which is where <a href="#ARG-R05">ARG-R05</a> and <a href="#ARG-A09">ARG-A09</a> take it up. Presenting the three together makes one licence look like three convergent lines of support.</p>
<p><strong>Seventh, the source is more careful than the list, and the difference is the finding.</strong> The volume this cluster is credited to also contains sections titled <em>The Failure of General Relativity</em> and <em>The Demise of Relativity Theory</em>, and Sungenis has written that a geocentrist appeals to relativity &ldquo;not as proof or even evidence for geocentrism&rdquo;, and that the case rests on evidence &ldquo;that has little or nothing to do with Relativity&rdquo;. Take him at his word and this cluster is not evidence for anything, by its own originator&rsquo;s account; it is a claim of respectability. Decline to take him at his word and the appeal has to be run at full strength, in which case it collapses for the reasons above. Either way the list&rsquo;s flat &ldquo;Equivalence principle validation&rdquo; overstates the authority it is drawing on.</p>
<p><strong>Verdict: standard physics.</strong> The true content of the argument &mdash; that a local frame in which the Earth is at rest is physically legitimate &mdash; is uncontroversial, taught everywhere, and denied by nobody. It is true of every body in the universe, it holds over a region currently bounded at the decimetre scale by instruments you can buy, and the frame it certifies is the non-rotating one that Foucault, Wettzell and Gravity Probe B use to measure the Earth turning.</p>""",

    advocate=dict(
        best_defense=(
            "You have spent seven paragraphs refuting a claim we do not make. Sungenis says "
            "in print that relativity is not offered as proof or even evidence — you quote "
            "him saying it — so your 'the list overstates its source' is an objection to the "
            "list, not to us, and you have conceded our actual position twice over: the "
            "equivalence principle is valid, inertial frames are dragged by matter, and "
            "Gravity Probe B measured the dragging. Now look at what your instruments "
            "actually measure. Foucault, Wettzell and Gravity Probe B all measure rotation "
            "*relative to the local inertial frame*. We agree the Earth rotates relative to "
            "the local inertial frame. Our claim is that the local inertial frame is itself "
            "dragged round by the rotating cosmos, so your gyroscope is a participant in the "
            "phenomenon, not an independent umpire of it — and Brill and Cohen showed the "
            "dragging becomes complete as the shell approaches its gravitational radius, "
            "which is roughly the condition our universe satisfies. Your 'the local inertial "
            "frame is non-rotating by definition' is exactly that: a definition. The "
            "13-centimetre figure is a fine piece of arithmetic about tidal gradients and "
            "has no bearing on it, because we are not claiming the lift is a global inertial "
            "frame; we are claiming the cosmos determines which frames are inertial. That is "
            "Mach's principle, which Einstein endorsed, and you have just spent a paragraph "
            "conceding it."),
        survives=4,
        preemptive=(
            "This is strong and it must be answered in the body, not left to the reader. Two "
            "changes, both now made. (a) The refutation's fourth section no longer stops at "
            "'the frame is non-rotating'; it states WHY the Coriolis term escapes the "
            "equivalence trade — velocity dependence, which no static field imitates — so "
            "that the reply 'that is just your definition' has something physical to bite "
            "on. It is not a definition: it is that producing the observed velocity-dependent "
            "deflection requires gravitomagnetic metric components, and those require a "
            "specified moving matter distribution, which is a bill and not a principle. "
            "(b) The fifth section is new and exists entirely to answer this defence. Perfect "
            "dragging is granted arguendo; the question then becomes what the dragged sky has "
            "to do, and the answer is that it has to reproduce the Earth's rotation "
            "IRREGULARITIES — about 90% of the seasonal length-of-day variation is zonal "
            "winds, and El Niño lengthens the day. A cosmos dragged into rigid co-rotation "
            "with the Earth must accelerate and decelerate in step with Pacific weather. "
            "If pressed further, hold the line at the division of labour rather than at the "
            "physics: Brill–Cohen dragging is a claim about a matter distribution, so it is "
            "R05's and A09's to answer with a stress-energy tensor and a fit, not R04's. "
            "R04's job is only to establish that the equivalence principle does not supply "
            "that dynamics and never claimed to. Do not concede the reverse framing — that "
            "we must disprove perfect dragging — since the party asserting a cosmological "
            "solution owes the solution.")),

    straw_man=dict(
        identified=True,
        detail=("Yes, and it is a straw man of physics rather than of us specifically. The "
                "framing this cluster travels with — visible in the source's own section "
                "titles and stated outright in Sungenis's Simran Matthews interview, where "
                "special relativity is described as having 'allowed the world to temporarily "
                "escape the implications of the empirical evidence' — is that relativity was "
                "devised as an escape hatch from the interferometer results, and that "
                "physicists therefore deny what the equivalence principle plainly grants. "
                "Both halves misdescribe the position. No physicist denies that a local rest "
                "frame is legitimate; the objection has always been to the extrapolation, "
                "not to the principle. And Einstein's 1905 paper opens not with Michelson "
                "and Morley but with the asymmetry in how electrodynamics of the time "
                "treated a moving magnet versus a moving conductor. We take no view on "
                "anyone's reasons for holding a position; the historical claim is answerable "
                "on the documents, and the physical claim is answered above. Our own straw "
                "man to avoid is the mirror image: never write that the equivalence "
                "principle forbids an Earth-fixed frame. It does not, and saying so hands "
                "the exchange away.")),

    compression=dict(
        assessed=True, drifted=True,
        list_phrasing="Equivalence principle validation.",
        source_wording=("General Relativity &ldquo;not only supports geocentrism as a "
                        "&lsquo;<em>relative</em>&rsquo; alternative, but also modified the postulates "
                        "of STR&rdquo; &mdash; and &ldquo;a geocentrist appeals to Relativity "
                        "<em>not as proof or even evidence for geocentrism</em> but merely to show "
                        "&hellip; that &hellip; geocentrism can have just as much scientific "
                        "respectability as heliocentrism.&rdquo;"),
        drift_type="force_upgraded",
        note=("<p>The same trade as <a href=\"#ARG-R01\">ARG-R01</a>, one lane over. Sungenis offers "
              "relativity as a <em>relative alternative</em> conferring <em>respectability</em>, and "
              "states in as many words that it is not offered as proof or even as evidence. The list "
              "prints it as item 132, &ldquo;Equivalence principle validation&rdquo;, in a numbered "
              "series of evidence for a stationary Earth. Nothing has been misquoted; a permission has "
              "been promoted to a validation.</p>"
              "<p><strong>What was and was not compared.</strong> The book&rsquo;s own statement of the "
              "argument, at Vol. I ch. 10 p. 607 in the 2006 printing, was not read: the Internet "
              "Archive rendering of that volume stops returning text long before it. The comparison "
              "above is therefore made against two things we could read &mdash; the volume&rsquo;s "
              "contents page, which announces <em>The Failure of General Relativity</em> at p. 334 and "
              "<em>The Demise of Relativity Theory</em> at p. 441, and the author&rsquo;s own published "
              "characterisations of what the appeal to relativity is for. That is enough to establish "
              "the speech act and not enough to establish the sentence. Anyone reaching p. 607 should "
              "re-run this block.</p>"
              "<p><strong>A second drift, visible inside the list itself.</strong> Item 316 reads "
              "&ldquo;Equivalence local labs rest&rdquo; and keeps the qualifier the principle cannot "
              "do without; items 57 and 132 drop it. One compressed line retains the scope and two "
              "delete it, which is the whole disagreement in five words. Only one drift type can be "
              "recorded, and <em>force_upgraded</em> is the one carrying evidence from the source&rsquo;s "
              "side; the scope-widening is recorded here because a reader can check it against the "
              "corpus without leaving the page.</p>")),

    verdict_challenge=dict(challenged=False, proposed_verdict=None, reasoning=None),

    people=["PER-SUNGENIS"],
    related=["R01", "R03", "R05", "R06", "R08", "A09"],

    sources=[
        dict(label="Sungenis & Bennett, Galileo Was Wrong Vol. I (2006) — Internet Archive item "
                   "GallileoWasWrong. Title page “Volume I: The Scientific Evidence”, ISBN "
                   "0-9779640-0-0; the contents pages quoted above, including ch. 10 “Mathematical "
                   "Models of a Geocentric Universe” at p. 590. The chapter text itself did not "
                   "render for the tools used here",
             url="https://archive.org/details/GallileoWasWrong"),
        dict(label="Sungenis, “Reply to Discover Magazine's Critique of Geocentrism” (answering Phil "
                   "Plait's Bad Astronomy post of 14 September 2010) — “not as proof or even evidence "
                   "for geocentrism”; “little or nothing to do with Relativity”",
             url="https://isidore.co/misc/Physics%20papers%20and%20books/Cosmology/Copernican%20principle/Sungenis%20&%20De%20Lano/Response-to-Phil-Plait-of-Discover-Magazine.pdf"),
        dict(label="“Interview of Robert Sungenis by Simran Matthews on Geocentrism”, undated PDF — "
                   "general relativity “supports geocentrism as a ‘relative’ alternative”. Original "
                   "place of publication not established; read at this mirror",
             url="https://isidore.co/misc/Physics%20papers%20and%20books/Cosmology/Copernican%20principle/Sungenis%20&%20De%20Lano/Interview-with-Simran-Mathews-re-Geocentrism.pdf"),
        dict(label="Touboul et al., “MICROSCOPE Mission: Final Results of the Test of the Equivalence "
                   "Principle”, PRL 129:121102 (2022) — η(Ti,Pt) = [−1.5 ± 2.3 ± 1.5] × 10⁻¹⁵",
             url="https://arxiv.org/abs/2209.15487"),
        dict(label="Will, “The Confrontation between General Relativity and Experiment”, Living "
                   "Reviews in Relativity 17 (2014) — the three-part Einstein equivalence principle, "
                   "each clause scoped to “any local non-gravitational experiment”",
             url="https://link.springer.com/article/10.12942/lrr-2014-4"),
        dict(label="Middlemiss et al., “Measurement of the Earth tides with a MEMS gravimeter”, Nature "
                   "531:614 (2016) — 40 μGal Hz^−½ on a chip, solid-Earth tide resolved",
             url="https://www.nature.com/articles/nature17397"),
        dict(label="NAGT/SERC teaching activity, “Measuring the vertical gradient of gravity” — the "
                   "free-air gradient, 0.3086 mGal per metre",
             url="https://serc.carleton.edu/NAGTWorkshops/structure/SGT2012/activities/62799.html"),
        dict(label="Brill & Cohen, “Rotating Masses and Their Effect on Inertial Frames”, Phys. Rev. "
                   "143:1011 (1966) — named in Galileo Was Wrong's own ch. 10 section list at p. 623",
             url="https://link.aps.org/doi/10.1103/PhysRev.143.1011"),
        dict(label="Everitt et al., “Gravity Probe B: Final Results”, PRL 106:221101 (2011) — geodetic "
                   "−6,601.8 ± 18.3 mas/yr against −6,606.1 predicted; frame dragging −37.2 ± 7.2",
             url="https://arxiv.org/abs/1105.3456"),
        dict(label="Di Virgilio et al., EPJ C 82:824 (2022) — Earth rotation rate to better than one "
                   "part in 10⁹ with the Wettzell ring laser",
             url="https://link.springer.com/article/10.1140/epjc/s10052-022-10798-9"),
        dict(label="EarthScope Consortium, “A Day is Not Always 24 Hours” — zonal winds and "
                   "atmospheric circulation account for about 90% of seasonal length-of-day variation; "
                   "El Niño lengthens the day",
             url="https://www.earthscope.org/news/a-day-is-not-always-24-hours-how-earths-shifting-systems-cause-day-length-variation/")]),
}
