# -*- coding: utf-8 -*-
"""Batch 9 — D14. "Dark matter / dark energy / MOND are modern epicycles."

Four items: 86 "Dark matter patchwork like epicycles." · 351 "Oort cloud unnecessary." ·
352 "MOND epicycle analogy." · 353 "Dark energy patching."

Research notes for whoever picks this up next.

1. WHICH TEXT WAS READ, AND WHY IT MATTERS HERE MORE THAN USUAL. The cluster record
   credits Sungenis & Bennett, *Galileo Was Wrong*, Vol. I, 2006. That record is
   CORRECT, and this is the first D-lane entry where the edition trap in the
   curmudgeon's failure #3 could have bitten hard. Two full texts were pulled and
   searched:
     (a) the FIRST edition, Volume I, "The Scientific Evidence" (ISBN 0-9779640-0-0),
         archive.org item `GallileoWasWrong` — the edition our record names;
     (b) the SEVENTH edition (2013), all three volumes in one scan, archive.org item
         `galileo-was-wrong-the-church-was-right-sungenis-vol-1-3-complete`.
   The dark-matter material is Chapter 8, "The Physical Cause of Gravity", section
   *"'Dark' Problems for Modern Notions of Gravity"*, pp. 503–512 of the 2006 Vol. I.
   In the 2013 rearrangement the same section is Chapter 7 and sits in **Volume II**.
   So an entry that quotes "Vol. II" and an entry that quotes "Vol. I" can both be
   right; say which edition. Everything quoted below is from (a) unless marked.

2. THE HEADLINE FINDING IS A REVERSAL AND IT IS ITEM 352. The source does not put
   MOND on the epicycle side. Its sentence about MOND is favourable — *"An alternate
   theory called 'Modified Newtonian Dynamics' (MOND) is a little better in explaining
   the anomalies"* (2006 Vol. I, p. 504) — and by the seventh edition it has grown a
   whole approving passage on Riccardo Scarpa's globular-cluster work, closing on
   Scarpa's line "There is no need for dark matter in the universe" (2013, Vol. I,
   ch. 2). MOND is the source's preferred escape from dark matter; the list files it
   as another epicycle. That is `reversed` in the strict sense of the enum.

3. THE "EPICYCLE" ARGUMENT IN THE SOURCE IS AIMED SOMEWHERE ELSE ENTIRELY. It lives in
   Chapter 1, pp. 58–60, and its target is perturbation theory and general relativity:
   Fourier series are epicycles renamed (quoting Charles Lane Poor, *Gravitation versus
   Relativity*, 1922, p. 132), *"including, as we will see, the 'curved space' of
   General Relativity"*. Word-search of the 2006 Vol. I: 65 hits on "epicycl-", 63 on
   "dark matter" — and ZERO instances of the two within 1,500 characters of each other.
   Same result on the 2013 three-volume scan at a 2,000-character window. So the
   pairing the list makes is not located in either text searched. Do not upgrade that
   to "the source never says it"; it is a proximity search over two OCR scans.

4. THE INTERNAL TENSION IS THE KERNEL AND IT IS UNUSUALLY CLEAN. "Epicycle" is not a
   term of abuse in this book. It quotes J. L. McCauley approvingly — "Epicycles are
   just data analysis (Fourier series), they don't imply any underlying theory of
   mechanics" (2006 Vol. I, pp. 46–47) — its own Chapter 1 argues Copernicus used as
   many epicycles as Ptolemy, and its own geocentric model USES them: "the epicycles
   may exist because there is a designed imbalance in the distribution of matter in the
   universe" (p. 595). And two sentences after the epicycle complaint the book concedes
   that Fourier analysis could make a FLAT-EARTH universe "mathematically
   indistinguishable from one based on a spherical Earth" (pp. 59–60) — i.e. the
   argument the list is running is one the source explicitly says settles nothing.

5. ITEM 351 IS A DIFFERENT ARGUMENT WITH A DIFFERENT HOME. "Oort" and "Kuiper" return
   zero hits in both scans; the eleven "comet" hits in the 2006 Vol. I are all
   bibliographic (Van Flandern's book title) or incidental. The comet-reservoir-as-
   fudge argument is documented, but in the young-earth creationist literature about
   the AGE of the Solar System — e.g. ICR, Jake Hebert, "Comets: Signs of Youth" (2020),
   which leads on Sagan and Druyan's 1985 line that there is "not yet a shred of direct
   observational evidence for its existence". That is a claim about chronology, not
   about the Earth's motion, and it was not traced to a named source for THIS list.
   Filed as a record problem, not written around.

6. WHY THE VERDICT WAS NOT CHALLENGED. MISLEADING is right and REFUTED would be wrong.
   The dark-matter/MOND question is live at galaxy scales (radial acceleration relation;
   Skordis & Złośnik's relativistic MOND) and DESI DR2 has the dark-energy equation of
   state moving at 2.8–4.2σ. This is E01 territory and the entry says so out loud. What
   is misleading is the inference, not the observation of a residual.

7. QUOTE PROVENANCE. All quotations are from OCR scans, not print copies; the locators
   say so. The 2006 OCR renders "modern" as "modem" throughout (a scanner artefact,
   not the authors' spelling) and it is silently normalised in the quoted sentence —
   flagged in the gloss. Printed page numbers are those carried in the scan's running
   heads and were cross-checked against the volume's own table of contents.
"""

ENTRY = {

"D14": dict(

    tldr=("The book this comes from names MOND as the better alternative to dark matter, "
          "not as another epicycle — and its epicycle complaint is aimed at Fourier series "
          "and at general relativity's curved space. Grant the whole indictment anyway, "
          "dark matter wrong and MOND right, and you land in a universe whose galaxies "
          "rotate and whose Sun the Earth orbits, because MOND was derived from rotation "
          "curves. The historical moral is borrowed from a history that did not happen: "
          "Copernicus needed as many epicycles as Ptolemy, which the same book argues at "
          "length in its own first chapter."),

    passage=dict(
        work="WRK-SUNGENIS-2006",
        pd=False,
        locator=("Vol. I first edition, ISBN 0-9779640-0-0 (archive.org item GallileoWasWrong), "
                 "ch. 8 “The Physical Cause of Gravity”, section “‘Dark’ Problems for Modern "
                 "Notions of Gravity”, printed p. 503; page numbers from the scan's running "
                 "heads, cross-checked against the volume's contents list, not checked against "
                 "a print copy. The OCR renders “modern” as “modem” throughout and is "
                 "normalised here."),
        quote=("To compensate for this, modern science has invented the matter they need. "
               "According to the best estimates, the required matter makes up 95% of the "
               "universe yet with one major caveat - it cannot be seen or detected. The name "
               "given to this mysterious but as yet undiscovered substance is Dark Matter, "
               "and its cousin is Dark Energy."),
        gloss="""<p><strong>Read what the complaint is, and what it is not.</strong> This is a charge of <em>invention without detection</em> &mdash; the same charge the book presses again a chapter later, where dark matter and dark energy become &ldquo;convenient phantoms&rdquo; (p.&nbsp;563). It is not a charge of epicycling. The word &ldquo;epicycle&rdquo; belongs to a different argument in a different chapter, and it is pointed at a different target.</p>
<p><strong>Where the epicycle argument actually is.</strong> Chapter&nbsp;1, pp.&nbsp;58&ndash;60. Modern astronomy, the book says, still runs on epicycles: &ldquo;conceptually speaking they are still very much in use, although they are labeled with different names in order to conceal their identity.&rdquo; The authority is Charles Lane Poor&rsquo;s <em>Gravitation versus Relativity</em> (1922, p.&nbsp;132), and the things being called epicycles are <strong>perturbation theory, Fourier series, and &mdash; named explicitly &mdash; &ldquo;the &lsquo;curved space&rsquo; of General Relativity.&rdquo;</strong> A proximity search of the 2006 Volume&nbsp;I turns up 65 occurrences of &ldquo;epicycl&mdash;&rdquo; and 63 of &ldquo;dark matter&rdquo;, with no instance of the two inside 1,500 characters of each other; the same search over the 2013 three-volume scan at a 2,000-character window returns nothing either. The pairing is not located in the text we searched.</p>
<p><strong>On MOND the source runs the other way from the list.</strong> One page on from the quotation above: &ldquo;An alternate theory called &lsquo;Modified Newtonian Dynamics&rsquo; (MOND) <em>is a little better in explaining the anomalies</em>&rdquo; (p.&nbsp;504). By the seventh edition (2013) that has grown into an approving account of Riccardo Scarpa&rsquo;s globular-cluster work, closing on Scarpa&rsquo;s own sentence, &ldquo;There is no need for dark matter in the universe&rdquo; (Vol.&nbsp;I, ch.&nbsp;2). The one place the book puts MOND and dark matter on a level is a <em>quotation from someone else</em> &mdash; L&auml;mmerzahl, Preuss and Dittus, that for want of a detection &ldquo;all those attempts are on the same footing&rdquo; (p.&nbsp;505) &mdash; and that sentence levels them on evidence, not on ad-hocery.</p>
<p><strong>And &ldquo;epicycle&rdquo; is not an insult in this book.</strong> It quotes the physicist J.&nbsp;L.&nbsp;McCauley with approval &mdash; &ldquo;Epicycles are just data analysis (Fourier series), they don&rsquo;t imply any underlying theory of mechanics&rdquo; (pp.&nbsp;46&ndash;47) &mdash; its first chapter is largely an argument that Copernicus needed as many epicycles as Ptolemy, and its own geocentric cosmology uses them as a design feature: &ldquo;the epicycles may exist because there is a designed imbalance in the distribution of matter in the universe&rdquo; (p.&nbsp;595). Two sentences after the epicycle complaint the book grants that Fourier analysis could make a <em>flat-Earth</em> universe &ldquo;mathematically indistinguishable from one based on a spherical Earth&rdquo; (pp.&nbsp;59&ndash;60). On its own account, then, calling something an epicycle settles nothing about whether it is true.</p>
<p><strong>On editions.</strong> Our record dates this to Volume&nbsp;I, 2006, and that is the text quoted here. In the seventh edition of 2013 the same section was renumbered Chapter&nbsp;7 and moved into Volume&nbsp;II; both scans were searched and they agree on every sentence quoted above except the Scarpa passage, which is an addition to the later edition.</p>"""),

    steelman=dict(
        description="""<p><strong>SURFACE (weak &mdash; do not use).</strong> &ldquo;Dark matter has been detected, so the analogy fails.&rdquo; It has not. Four decades of direct-detection experiments have returned nothing: LZ&rsquo;s latest search, 417 live days taken between March 2023 and April 2025, reported no WIMP signal at all, and the thing it did detect was boron-8 solar neutrinos scattering coherently off xenon at 4.5&sigma; &mdash; the &ldquo;neutrino fog&rdquo; that will eventually floor this kind of search. Anyone who opens with &ldquo;we found it&rdquo; has handed the exchange over.</p>
<p><strong>DEEPER.</strong> The epicycle charge has a serious professional form and it is not this movement&rsquo;s invention. David Merritt &mdash; a working galactic-dynamics astronomer, author of <em>A Philosophical Approach to MOND</em> (Cambridge, 2020) &mdash; argues in &ldquo;Cosmology and convention&rdquo; (2017) that dark matter and dark energy are &ldquo;conventionalist&rdquo; in Popper&rsquo;s sense: &ldquo;auxiliary hypotheses that were invoked in response to observations that falsified the standard model as it existed at the time&rdquo;, putting cosmology in Lakatos&rsquo;s &ldquo;degenerating problemshift&rdquo;. That paper drew a published reply rather than silence. The complaint is live in the philosophy-of-science literature, and answering it by sneering at the word &ldquo;epicycle&rdquo; is answering the wrong person.</p>
<p><strong>KERNEL.</strong> The specific true thing is the <em>radial acceleration relation</em>. McGaugh, Lelli and Schombert (<em>Phys. Rev. Lett.</em> 117:201101, 2016) fitted 2,693 points across 153 galaxies of &ldquo;very different morphologies, masses, sizes, and gas fractions&rdquo; and found the acceleration a rotation curve actually shows is fixed by the acceleration the visible baryons alone would produce &mdash; &ldquo;the correlation persists even when dark matter dominates&rdquo;, so &ldquo;the dark matter contribution is fully specified by that of the baryons&rdquo;, with scatter &ldquo;small and largely dominated by observational uncertainties&rdquo;. Their own word for it is &ldquo;tantamount to a natural law for rotating galaxies&rdquo;. Milgrom wrote that law down in 1983 from a one-parameter modification of dynamics; the halo picture did not predict it, and deriving its tightness from galaxy formation is unfinished work. If you want the strongest version of &ldquo;the dark sector looks fitted rather than found&rdquo;, that is it &mdash; a regularity that one side predicted and the other side has to explain.</p>""",
        why_it_doesnt_save_claim="""<p>Because the kernel is an argument <em>between two theories of gravity</em>, and both of them are theories in which the Earth moves. MOND is a statement about what happens below an acceleration scale of roughly 1.2&times;10<sup>&minus;10</sup>&nbsp;m&nbsp;s<sup>&minus;2</sup>. It was extracted from galaxy rotation curves &mdash; which is to say, from the premise that galaxies rotate, that the Milky Way is one, and that the Sun is a moving point inside it. The Solar System sits far above that scale &mdash; nearly eight orders of magnitude above it at the Earth&rsquo;s orbit, and still four above it out at Neptune &mdash; and is left in the Newtonian regime untouched. Winning this argument outright delivers a cosmos in which the Galaxy turns, the Sun goes round it, and the Earth goes round the Sun. The prize belongs to Milgrom, and it is not on offer to anybody else.</p>
<p>And the source cannot spend the epicycle charge without spending its own model. Its named epicycle-under-a-new-name is &ldquo;the &lsquo;curved space&rsquo; of General Relativity&rdquo; &mdash; but general relativity is the machinery the same book leans on to make a stationary Earth respectable, in the chapter that runs through &ldquo;Einstein&rsquo;s Geocentrism&rdquo;, &ldquo;Thirring&rsquo;s Geocentrism&rdquo;, &ldquo;Bondi&rsquo;s Geocentrism&rdquo; and eight more (2006 Vol.&nbsp;I, ch.&nbsp;10; worked at <a href="#ARG-R01">ARG-R01</a>). If curve-fitting discredits a theory, it discredits the one doing the work here first.</p>"""),

    refutation="""<p><strong>Start by conceding the parts that are true, because most of them are.</strong> Dark matter has not been detected in a laboratory. The most sensitive experiment running, LZ, reported no WIMP across 417 live days ending April 2025 and instead made a 4.5&sigma; measurement of solar neutrinos &mdash; the background that will eventually limit the whole technique. Dark energy is a number nobody can derive from anything. The two together are about 95% of the energy budget, which is a startling thing to say out loud. And the residual that dark matter was introduced to cover is real: in the words the book quotes from <em>Discover</em>, &ldquo;in every single galaxy ever studied, the stars and gas move faster than Newton&rsquo;s laws say they should.&rdquo; None of that is in dispute here.</p>

<p><strong>1. The moral is borrowed from a history that did not happen &mdash; and the source proves it.</strong> The analogy only bites if epicycles were the thing wrong with Ptolemy, swept away by a simpler heliocentric picture. Historians of astronomy abandoned that story a long time ago, and <em>Galileo Was Wrong</em> spends its first chapter demolishing it, quoting Lakatos: &ldquo;The superior simplicity of the Copernican theory was just as much of a myth as its superior accuracy&hellip; each equant and eccentric removed has to be replaced by new epicycles and epicyclets&hellip; the &lsquo;simplicity balance&rsquo; between Ptolemy&rsquo;s and Copernicus&rsquo; system is roughly even&rdquo; (2006 Vol.&nbsp;I, pp.&nbsp;58&ndash;59). The book is right about this. So on its own account, epicycle-count never distinguished the true system from the false one, and &ldquo;that&rsquo;s an epicycle&rdquo; carries no verdict. What eventually settled the question was not tidiness but new physical facts nobody had before: Bradley&rsquo;s aberration in 1729, Bessel&rsquo;s parallax in 1838, and a dynamics that predicted quantities before they were measured. Which is exactly the test to apply here.</p>

<p><strong>2. Apply it: an epicycle buys one residual, a parameter that predicts is a different animal.</strong> Ptolemaic and Copernican circles were added one per discrepancy, and none of them told you anything you had not already put in. The standard cosmological model has <strong>six</strong> free parameters. Fix them on the microwave background&rsquo;s temperature spectrum, which Planck measured out to multipoles of order 2,500, and the polarisation spectra are then <em>predicted</em> to a few percent rather than fitted. Then comes the part an epicycle cannot imitate. The <em>baryon</em> density is measured a second time by a wholly unrelated route: primordial deuterium in high-redshift gas clouds, a nuclear-physics measurement of the first few minutes, which Cooke, Pettini and Steidel pinned to one percent, D/H = (2.527 &plusmn; 0.030)&times;10<sup>&minus;5</sup>, and which &ldquo;agrees to within 2 sigma&rdquo; with the value Planck reads off acoustic oscillations 380,000 years later. Those two numbers had no obligation to match. They match &mdash; and the total matter density is about five times larger than the baryon density both of them report. Two independent physics regimes agreeing that most of the matter is not made of atoms is not a curve fit.</p>

<p><strong>3. The one place the substance is separable from the gravity.</strong> In the Bullet Cluster (1E&nbsp;0657&ndash;558) the hot gas &mdash; which is most of the ordinary matter &mdash; was stripped and left behind in the collision, while the lensing mass stayed with the galaxies. Clowe and colleagues call the offset &ldquo;an 8-sigma significance spatial offset of the center of the total mass from the center of the baryonic mass peaks&rdquo; which &ldquo;cannot be explained with an alteration of the gravitational force law&rdquo;. Be honest about the state of that card rather than playing it as a trump: MOND partisans model the bullet-like lensing map in modified gravity (Angus, Famaey &amp; Zhao, <em>MNRAS</em> 371:138, 2006) and answer the collisionless residual that is left with an ordinary-looking hot dark component &mdash; 2&nbsp;eV active neutrinos in Angus, Shan, Zhao &amp; Famaey, <em>ApJ</em> 654:L13 (2007), an 11&nbsp;eV sterile neutrino in Angus, <em>MNRAS</em> 394:527 (2009). The Bullet also has its own bill outstanding on the other side, since the collision speed is uncomfortably high for structure formation in the standard model (Lee &amp; Komatsu, <em>ApJ</em> 718:60, 2010). It is a strong result under active dispute, which is a different thing from a closed case.</p>

<p><strong>4. Say plainly where the argument is genuinely open, because it is.</strong> The radial acceleration relation is real, MOND predicted it, and reproducing its tightness inside halo models is live work. Relativistic completions of MOND are not dead: the versions in which gravitational waves and ordinary matter do not travel on the same metric &mdash; the &ldquo;dark matter emulators&rdquo; &mdash; were killed by GW170817, which arrived alongside its gamma-rays instead of with the roughly 400 days of extra Shapiro delay those theories require (Boran, Desai, Kahya &amp; Woodard, <em>Phys. Rev. D</em> 97:041501, 2018), and Skordis and Z&#322;o&#347;nik then built a theory in which gravitational waves do travel at the speed of light, which also reproduces the microwave-background spectrum (<em>Phys. Rev. Lett.</em> 127:161302, 2021). On the other side of the dark sector, DESI&rsquo;s second data release combined with supernovae prefers an evolving equation of state over a cosmological constant at &ldquo;2.8&ndash;4.2&sigma; depending on which SNe sample is used&rdquo; &mdash; which is to say the &ldquo;dark energy&rdquo; entry in the ledger may not be a constant at all. Anybody who tells you the dark sector is settled is overselling, and this page will not.</p>

<p><strong>5. Now the sentence the whole cluster turns on.</strong> Grant every word of it. Suppose dark matter is a forty-year mistake, dark energy is a bookkeeping error, and MOND is right. What have the four items bought? A modification of dynamics at accelerations near 10<sup>&minus;10</sup>&nbsp;m&nbsp;s<sup>&minus;2</sup>, inferred from the rotation of galaxies, in which the Milky Way rotates, the Sun orbits its centre and the Earth orbits the Sun, and in which the Solar System &mdash; where the gravitational acceleration does not fall to the MOND scale until roughly 7,000&nbsp;AU from the Sun &mdash; behaves exactly as Newton said. Every candidate on the table here is a theory of how gravity works far from home. None of them has a term for where the centre is. The list is spending a live controversy on a conclusion neither party to it holds, which is the same trade it makes with the satellite planes at <a href="#ARG-E06">ARG-E06</a> and with the Hubble tension at <a href="#ARG-E09">ARG-E09</a>.</p>

<p><strong>6. Item 351 is a different claim and deserves its own answer.</strong> The Oort cloud has never been imaged; Sagan and Druyan said so in 1985 and creationist writers have been quoting the line ever since. But it is not a free postulate, it is an inference with a shape. Long-period comets arrive with original orbits piling up at semi-major axes of tens of thousands of astronomical units; they come in from every direction rather than hugging the ecliptic the way short-period comets do; and their ices could not have survived many passes close to the Sun. Those three facts together specify a roughly spherical reservoir, tens of thousands of AU out, and Sedna &mdash; perihelion 76&nbsp;AU &mdash; and 2012&nbsp;VP<sub>113</sub> are the candidate members found so far. &ldquo;Unnecessary&rdquo; is a claim that something else produces that arrival distribution, and it is owed the something else. It is also, whichever way it goes, an argument about the Sun&rsquo;s outskirts: an Oort cloud is by construction a swarm bound to and centred on the Sun, so abolishing it takes furniture out of the heliocentric house without shifting the Earth an inch.</p>

<p><strong>Verdict: misleading.</strong> The observation is sound &mdash; there is an unexplained residual, and two large entries in the cosmic ledger have never been seen. The inference is not. An unexplained residual in a theory is not evidence for a particular alternative, and it is least of all evidence for an alternative with no quantitative model of the residual. The word &ldquo;epicycle&rdquo; does the work that the argument cannot, by importing a verdict from a history that the source itself, in its first chapter, shows never happened.</p>""",

    advocate=dict(
        best_defense=(
            "You have written a very long piece of bookkeeping. Your headline finding is "
            "that Sungenis did not literally set the word 'epicycle' beside the words 'dark "
            "matter' — but he wrote something stronger in both places, that modern astronomy "
            "runs on epicycles under assumed names and that 95% of the universe was invented "
            "because the equations demanded it. A compressor who joins two sentences of the "
            "same book has compressed, not falsified. And look what you conceded to get "
            "there: no detection in forty years, the neutrino fog closing in, a relation "
            "MOND predicted and your side did not, and DESI now saying your cosmological "
            "constant is drifting. You have written our argument for us and then told us it "
            "points somewhere else. But 'it points somewhere else' is a much smaller claim "
            "than the one your verdict chip makes. Two more things. Your Bullet Cluster "
            "paragraph concedes the counter and then keeps the card anyway. And your "
            "parameter-counting move is the oldest trick in this trade: six parameters plus "
            "inflation plus a dark sector nobody can see plus a reionisation fudge is not "
            "six of anything — Ptolemy could have told you that a model looks parsimonious "
            "once you stop counting the parts you have decided are furniture."),
        survives=4,
        preemptive=(
            "Four, and the number is set by the last sentence rather than the first. Four "
            "changes, all of them already in the text above and all of which must stay there. "
            "(a) The concessions must come FIRST and in the author's own voice — section 0 of "
            "the refutation opens on the null results and the real residual, because a reader "
            "who meets our parameter-counting argument before our concession will read the "
            "concession as damage control. Never let an editor move it below the fold. "
            "(b) The parameter-counting section must not be left as a bare number: the "
            "defender's reply (\"six plus everything you are not counting\") is good, and the "
            "answer is the BBN cross-check, not the number six. Keep the deuterium paragraph "
            "welded to the six-parameter sentence — the force is that an independent physics "
            "regime returns the same baryon density, which no amount of parameter-hiding "
            "produces. (c) On the Bullet Cluster, keep both counters in the text. A card "
            "played as a trump and then quietly qualified is worse than a card played as what "
            "it is, and both counters are real ones — the MOND side has Angus/Famaey/Zhao on the "
            "lensing map and the Angus neutrino papers on the residual it leaves, and the cost on "
            "our own side is Lee/Komatsu. Do not let the neutrino answer be filed under "
            "Angus/Famaey/Zhao: that paper is analytic lensing, and a defender who opens it "
            "looking for neutrinos and finds none has been handed the exchange. (d) The discriminating "
            "sentence — MOND was derived from rotation curves, so winning it hands you a "
            "rotating Galaxy and an orbiting Earth — is the only paragraph here that touches "
            "the list's actual thesis, and it must not be buried in a summary. On tone: the "
            "defender is right that our finding is partly a bookkeeping finding. Say so. The "
            "bookkeeping matters because the item names MOND, and naming MOND is how you can "
            "tell the compressor was working from a summary of the book rather than the book."),
    ),

    straw_man=dict(
        identified=True,
        detail=("The argument is aimed at a cosmology that treats dark matter as settled, and "
                "at a history in which epicycles were the thing wrong with Ptolemy. Neither is "
                "the position of the people being argued against. Working cosmologists publish "
                "the non-detections themselves — LZ reported its own null — and the "
                "dark-matter-versus-modified-gravity question is argued out in the journals "
                "every year. On the history, the source is closer to the specialists than the "
                "list is: its own first chapter shows, correctly and at length, that Copernicus "
                "needed as many epicycles as Ptolemy. The list then uses the word as a term of "
                "abuse, which is the reading its own authority spent a chapter refuting."),
    ),

    compression=dict(
        assessed=True, drifted=True,
        list_phrasing=("86. Dark matter patchwork like epicycles. · 352. MOND epicycle "
                       "analogy. · 353. Dark energy patching. · 351. Oort cloud unnecessary."),
        source_wording=("“An alternate theory called ‘Modified Newtonian Dynamics’ (MOND) "
                        "<em>is a little better in explaining the anomalies</em>.” "
                        "(Vol. I, 2006, p. 504) &mdash; and, on the seventh edition&rsquo;s "
                        "expansion of the same passage, Scarpa quoted with approval: "
                        "<em>“There is no need for dark matter in the universe.”</em>"),
        drift_type="reversed",
        note=("<strong>Item 352 states the opposite of its source.</strong> In the book MOND is "
              "the way <em>out</em> of dark matter and is named as the better account of the "
              "anomalies; on the list it is filed alongside dark matter as another epicycle. "
              "The only place the book levels the two is a quotation from someone else &mdash; "
              "L&auml;mmerzahl, Preuss and Dittus, that for want of a detection &ldquo;all those "
              "attempts are on the same footing&rdquo; (Vol.&nbsp;I, 2006, p.&nbsp;505) &mdash; "
              "which levels them on evidence, not on ad-hocery, and is not the authors&rsquo; "
              "own sentence. "
              "<strong>Item 86 welds together two arguments the book keeps a chapter and four "
              "hundred pages apart.</strong> The dark-matter charge is <em>invention without "
              "detection</em> (ch.&nbsp;8, p.&nbsp;503; &ldquo;convenient phantoms&rdquo;, "
              "p.&nbsp;563). The epicycle charge is in ch.&nbsp;1, pp.&nbsp;58&ndash;60, and its "
              "targets are perturbation theory, Fourier series and &ldquo;the &lsquo;curved "
              "space&rsquo; of General Relativity&rdquo;. Searching the 2006 Volume&nbsp;I text "
              "for the two together returns nothing inside a 1,500-character window, and the "
              "2013 three-volume scan returns nothing inside 2,000; the pairing is not located "
              "in either text searched. "
              "<strong>Item 353 is the closest to faithful</strong> &mdash; dark energy is "
              "genuinely called a phantom there. "
              "<strong>Item 351 has no counterpart at all in the volume searched:</strong> "
              "&ldquo;Oort&rdquo;, &ldquo;Kuiper&rdquo; and &ldquo;comet cloud&rdquo; return "
              "zero hits in both scans, and the comet-reservoir-as-fudge argument is documented "
              "instead in young-earth creationist writing about the age of the Solar System. "
              "<strong>The refutation above answers the source and not the fragment:</strong> it "
              "concedes the non-detections at full strength, concedes the radial acceleration "
              "relation that MOND predicted, and puts the weight on what the source&rsquo;s own "
              "first chapter establishes &mdash; that epicycle-count never separated the true "
              "system from the false one &mdash; and on the fact that every alternative in play "
              "leaves the Earth in motion. The drift runs the usual direction: the book argues "
              "for a smaller universe and against Einstein&rsquo;s field equations; the list "
              "publishes a verdict on three research programmes, one of which the book was "
              "backing."),
    ),

    verdict_challenge=dict(challenged=False, proposed_verdict=None, reasoning=None),

    people=["PER-SUNGENIS"],
    related=["D11", "D12", "D13", "R01", "R12", "E01", "E06", "E09", "E12"],

    sources=[
        dict(label="Sungenis & Bennett, Galileo Was Wrong, Vol. I first edition (ISBN "
                   "0-9779640-0-0) — archive.org scan; the dark-matter section at ch. 8, "
                   "pp. 503–512, the MOND sentence at p. 504, the epicycle argument at "
                   "ch. 1, pp. 58–60, “convenient phantoms” at p. 563",
             url="https://archive.org/details/GallileoWasWrong"),
        dict(label="Galileo Was Wrong, seventh edition (2013), Vols I–III in one scan — the "
                   "same passages renumbered, plus the added Scarpa passage at Vol. I, ch. 2",
             url="https://archive.org/details/galileo-was-wrong-the-church-was-right-sungenis-vol-1-3-complete"),
        dict(label="Charles Lane Poor, Gravitation versus Relativity (Putnam, 1922) — the "
                   "“epicycles under new names” passage the source quotes from p. 132",
             url="https://archive.org/details/gravitationversu00pooruoft"),
        dict(label="Merritt, “Cosmology and convention” (2017), Studies in History and "
                   "Philosophy of Modern Physics — dark matter and dark energy as Popperian "
                   "“conventionalist stratagems”; the serious form of the epicycle charge",
             url="https://arxiv.org/abs/1703.02389"),
        dict(label="Man Ho Chan, “A Comment on ‘Cosmology and Convention’ by David Merritt”, "
                   "Journal for General Philosophy of Science (2019) — the published reply",
             url="https://link.springer.com/article/10.1007/s10838-019-09444-y"),
        dict(label="McGaugh, Lelli & Schombert, “Radial Acceleration Relation in Rotationally "
                   "Supported Galaxies”, Phys. Rev. Lett. 117:201101 (2016) — 2,693 points in "
                   "153 galaxies; “tantamount to a natural law for rotating galaxies”",
             url="https://arxiv.org/abs/1609.05917"),
        dict(label="Clowe et al., “A direct empirical proof of the existence of dark matter”, "
                   "ApJ 648:L109 (2006) — the 8σ Bullet Cluster offset",
             url="https://arxiv.org/abs/astro-ph/0608407"),
        dict(label="Angus, Famaey & Zhao, “Can MOND take a bullet? Analytical comparisons of "
                   "three versions of MOND beyond spherical symmetry”, MNRAS 371:138 (2006) — "
                   "analytic MONDian models producing a weak-lensing signal resembling "
                   "1E 0657-56; lensing and dynamics only, no neutrinos in it",
             url="https://arxiv.org/abs/astro-ph/0606216"),
        dict(label="Angus, Shan, Zhao & Famaey, “On the proof of dark matter, the law of "
                   "gravity and the mass of neutrinos”, ApJ 654:L13 (2007) — the Bullet is "
                   "collisionless-dominated in MOND too, resolved by “the ‘marriage’ of MOND "
                   "with ordinary hot neutrinos of 2eV”",
             url="https://arxiv.org/abs/astro-ph/0609125"),
        dict(label="Angus, “Is an 11 eV sterile neutrino consistent with clusters, the cosmic "
                   "microwave background and modified Newtonian dynamics?”, MNRAS 394:527 "
                   "(2009) — the sterile-neutrino version of the same move",
             url="https://arxiv.org/abs/0805.4014"),
        dict(label="Lee & Komatsu, “Bullet Cluster: A Challenge to ΛCDM Cosmology”, ApJ 718:60 "
                   "(2010) — the collision velocity problem on the standard-model side",
             url="https://arxiv.org/abs/1003.0939"),
        dict(label="Cooke, Pettini & Steidel, “One percent determination of the primordial "
                   "deuterium abundance”, ApJ 855:102 (2018) — D/H = (2.527 ± 0.030)×10⁻⁵, "
                   "BBN baryon density agreeing with Planck to within 2σ",
             url="https://arxiv.org/abs/1710.11129"),
        dict(label="Planck 2018 results VI, Cosmological parameters, A&A 641:A6 (2020) — the "
                   "six-parameter model, Ω_b h² = 0.02237 ± 0.00015, Ω_c h² = 0.1200 ± 0.0012 "
                   "(TT,TE,EE+lowE+lensing); corrigendum at A&A 652:C4 (2021)",
             url="https://arxiv.org/abs/1807.06209"),
        dict(label="Skordis & Złośnik, “New relativistic theory for Modified Newtonian "
                   "Dynamics”, Phys. Rev. Lett. 127:161302 (2021) — gravitational waves at c, "
                   "and a CMB spectrum",
             url="https://arxiv.org/abs/2007.00082"),
        dict(label="Boran, Desai, Kahya & Woodard, “GW170817 falsifies dark matter emulators”, "
                   "Phys. Rev. D 97:041501 (2018) — rules out theories “which dispense with the "
                   "need for dark matter by making ordinary matter couple to a different metric "
                   "from that of GW”; estimated differential Shapiro delay ~400 days against an "
                   "observed 1.7 s",
             url="https://arxiv.org/abs/1710.06168"),
        dict(label="DESI DR2 Results II: BAO measurements and cosmological constraints (2025) — "
                   "with SNe, a dynamical dark energy preferred over ΛCDM at 2.8–4.2σ",
             url="https://arxiv.org/abs/2503.14738"),
        dict(label="LZ dark matter search, results announced 8 December 2025 — 417 live days, "
                   "no WIMP signal, and a 4.5σ detection of ⁸B solar neutrinos (the neutrino fog)",
             url="https://www.brown.edu/news/2025-12-08/lz-dark-matter"),
        dict(label="Oort cloud — the inference from long-period comet orbits, the isotropy of "
                   "their arrival directions, and the Sedna / 2012 VP113 candidates; no direct "
                   "imaging",
             url="https://en.wikipedia.org/wiki/Oort_cloud"),
        dict(label="Jake Hebert, “Comets: Signs of Youth” (Institute for Creation Research, "
                   "2020) — the “Oort cloud is unnecessary” argument in its documented home, "
                   "the young-earth literature about the age of the Solar System",
             url="https://www.icr.org/article/comets-signs-of-youth/"),
    ]),
}
