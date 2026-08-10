# -*- coding: utf-8 -*-
"""
Batch 9 — ARG-E09, "Hubble tension shows we are at a special location".
2 items (98, 325), lane E, verdict MISLEADING, originator recorded null.

Research notes for whoever picks this up next, ordered by how much they change the
entry.

1. THE TWO ITEMS ARE TWO DIFFERENT HYPOTHESES, AND THEY DESTROY EACH OTHER.
   Item 98 is "Hubble tension observation bias."; item 325 is "Hubble tension location
   bias." In the actual literature those are two rival explanations of the same number:
   (a) the local distance ladder carries an unrecognised measurement systematic, which
   is Freedman's CCHP position, and (b) our neighbourhood is underdense and the outflow
   inflates local redshifts, which is Banik and Kroupa's position. If (a) is right there
   is no anomaly left to convert into a location. If (b) is right the measurements are
   fine and (a) is wrong. A list that scores both as separate proofs is double-counting
   two mutually exclusive escapes. The refutation below answers each on its own terms
   before pointing that out, because taking them one at a time is the only way to answer
   the strong version of either.

2. THE VOID READING IS LIVE, PUBLISHED AND ARGUED BY WORKING ASTRONOMERS — the E01
   precedent, and the page must keep saying so. Haslbauer, Banik & Kroupa 2020 (MNRAS
   499:2845) and Banik & Kalaitzidis 2025 (MNRAS 540:545) are refereed papers arguing
   that a ~300 Mpc, ~20% underdense region around the Local Group both exists and
   relieves the tension; the 2025 paper takes 42 BAO D_V measurements over twenty years
   and reports total chi-squared 75.7 for the void-free model against 47.3-51.2 for the
   void models, i.e. 3.3 sigma down to 1.1-1.4 sigma. That was the Royal Astronomical
   Society's National Astronomy Meeting story of July 2025 and it is where the "Earth
   sits in a giant void" headlines came from. Anyone who writes that the local-void
   reading is closed will lose the exchange to a reader with a search engine.

3. OUR OWN BASIS LINE IS STRONGER THAN THE LITERATURE SUPPORTS. clusters.py E09 reads
   "The local-void reading was tested directly on 1295 supernovae and excluded at
   4-5 sigma." Kenworthy, Scolnic & Riess 2019 (ApJ 875:145) is a real and important
   result, but what it excludes at 4-5 sigma is specifically large underdensities with
   |delta| > 20% modelled as a sharp-edged Lemaitre-Tolman-Bondi void in 0.023<z<0.15;
   their headline 5 sigma bound is delta < 27% on scales above 69 h^-1 Mpc. It does not
   close the reading, and it predates the 2020-2025 KBC-void work by up to six years.
   Reported in record_problems; clusters.py was NOT edited by this agent, and the prose
   below states the state of the dispute directly rather than commenting on our record.

4. THE MOVEMENT TEXT EXISTS, BUT IN AN OLDER VOCABULARY, AND IT IS NOT THE SOURCE OF
   THESE TWO ITEMS. Galileo Was Wrong Vol. I, chapter 3 ("Evidence Earth is in the
   Center of the Universe"), printed pp. 316-320 of the seventh edition, carries the
   whole argument shape — quote the void literature, note that a void requires giving up
   the Copernican principle, conclude a geocentric universe — built out of the 2008
   supernova-dimming papers rather than the Hubble tension. Sungenis quotes Clifton,
   Ferreira & Land 2008 (PRL 101:131302) at length and accurately, including their line
   that within standard inflationary cosmology "the probability of large, deep voids
   occurring is extremely small".
   The string "Hubble tension" returns ZERO occurrences in the djvu text of the Internet
   Archive scan galileo-was-wrong-the-church-was-right-sungenis-vol-1-3-complete
   (5.5 MB, 134,983 lines, all three volumes, downloaded whole and searched 2026-08-09);
   so do "KBC", "Keenan", "supervoid" and "Local Hole". "local void" returns one hit, in
   a list of foreground contaminants on p. 21534 of the text, unrelated. The term
   postdates the book. So the passage is quoted as the argument's ANCESTOR and the
   originator field stays empty: originator=None is not challenged here.

5. THE DECISIVE NUMBER IS THE CENTRING TOLERANCE, AND IT IS THE OPPOSITE OF A PROOF
   ABOUT THE EARTH. Off-centre observers in a void see a CMB dipole, which is what
   bounds how far off-centre you can be. Alnes & Amarzguioui (astro-ph/0607334) found
   for their void model that the observer "has to be located within a radius of ~15 Mpc
   from the center for the induced dipole to be less than that observed by the COBE
   satellite". 15 Mpc is 4.63e20 km, about 49 million light-years (a RADIUS, so the
   permitted ball is about twice that across), about 3.6e16 Earth diameters. That is the
   resolution of the claim. It cannot separate the Earth from the Sun, from Andromeda,
   or from any of thousands of galaxies.
   SCOPE, verified 2026-08-10 against the ar5iv full text of astro-ph/0607334, section V:
   the 15 Mpc bound is stated three sentences before "When compared to the size of the
   underdensity, which according to Fig. 2 is around 1500 Mpc", and the paper closes by
   calling these LTB models "an exotic alternative to dark energy". So the bound belongs
   to a ~1500 Mpc dark-energy-replacing bubble, roughly five times the ~300 Mpc void this
   cluster is about, and no centring bound for the shallower void was found in any paper
   cited on this page. The entry therefore does NOT rest on the number: it adds the
   insensitivity argument (note 6), which holds whichever way 15 Mpc moves.

6. THE ARITHMETIC IN NOTES 5 AND 7 WAS DONE IN-SESSION AND IS CHECKABLE: 1 Mpc = 3.0857e19
   km, so 15 Mpc = 4.629e20 km; divided by the Earth's mean diameter 12,742 km that is
   3.63e16; 15 Mpc / 0.3066 Mpc-per-Mly = 48.9 Mly. INSENSITIVITY: 1 AU = 1.496e8 km =
   4.85e-12 Mpc, so 15 Mpc / 1 AU = 3.09e12 — the tolerance must tighten by a factor of
   ~3e12, i.e. MORE THAN TWELVE orders of magnitude, before "the Earth rather than the
   Sun" is expressible. The review finding that proposed this argument said "more than
   fifteen orders of magnitude"; that is wrong by ~2.5 decades and the text says twelve.

7. THE EARTH-REFERENT IS NOT THE LIST'S INVENTION, AND THE ENTRY NOW SAYS SO. The single
   source cited for Banik's "our galaxy" quote is the University of Portsmouth / RAS
   release, whose headline is "Is Earth inside a huge void?" and whose body states, in the
   release's own voice, that "Earth and our solar system would need to be near the centre
   of a void about a billion light-years in radius and with a density about 20 per cent
   below the average" (fetched 2026-08-10). Writing "Banik says 'our galaxy', not 'the
   Earth'" as an unqualified punchline invited a reader to click our own link and find an
   apparent refutation in the title. The drift is real but it starts in science
   communication; the list hardened it. That is the stronger finding for this project, so
   the TLDR, section 7 and the compression note now attribute the swap where it happens.

TRAP AVOIDED. The tempting line — "a local void was ruled out years ago" — is available
from a 2026 review (Cai & Wang, arXiv:2606.20434, "a local Hubble bubble or cosmic void
solution has long been ruled out as a significant contribution") and it would still be a
mistake to write it flat, because Banik's group is publishing the other way in MNRAS in
the same period. The entry quotes both and takes no side. What it does instead is show
that the argument fails at the step nobody in that dispute is arguing about: the step
from "the Local Group's neighbourhood may be underdense" to "the Earth is the centre".
"""

ENTRY = {

"E09": dict(

    tldr=("The Hubble tension is real, unresolved, and the local-void reading of it is a "
          "live minority position argued in MNRAS by professional astronomers — so the "
          "answer is not that nobody thinks this. It is that the “special location” those "
          "models describe is a region tens of megaparsecs across centred on the Local "
          "Group, which cannot tell the Earth apart from Andromeda, let alone from the "
          "Sun; the astronomer behind the 2025 headlines says “our galaxy”, and his own "
          "university’s press release had already turned that into “Earth and our solar "
          "system” before any proof list touched it. And the two items cancel: if the "
          "tension is an observation bias in the "
          "distance ladder there is no anomaly left to locate anyone with, and if it is a "
          "location bias then the locating is done by an expanding relativistic universe "
          "measured with the redshifts, standard candles and standard rulers this list "
          "rejects elsewhere."),

    passage=dict(
        work="WRK-SUNGENIS-2006",
        locator=("Vol. I, chapter 3, “Evidence Earth is in the Center of the Universe”, "
                 "printed p. 319 of the seventh edition (2013); read in the Internet "
                 "Archive scan galileo-was-wrong-the-church-was-right-sungenis-vol-1-3-"
                 "complete, djvu text line 18,645. Not checked against a print copy."),
        pd=False,
        quote=("When we add to this the fact that no one has ever found physical evidence "
               "of the much needed Dark Energy to make the Copernican/Einsteinian model "
               "work, it is clear that current cosmology is merely a desperate attempt to "
               "avoid the simplest solution to their own Big Bang data — a geocentric "
               "universe."),
        gloss=("<p><strong>This passage is not the source of items 98 and 325, and we do not "
               "credit it as one.</strong> The items name the Hubble tension, a term that "
               "postdates this book: the string &ldquo;Hubble tension&rdquo; returns zero "
               "occurrences in the djvu text of the Internet Archive scan named above &mdash; "
               "5.5&nbsp;MB, 134,983 lines, all three volumes, downloaded whole and searched "
               "on 2026-08-09 &mdash; and so do &ldquo;KBC&rdquo;, &ldquo;Keenan&rdquo;, "
               "&ldquo;supervoid&rdquo; and &ldquo;Local Hole&rdquo;. The cluster&rsquo;s "
               "originator field stays empty. What this passage is, is the <em>ancestor</em>: "
               "the identical argument built out of the supernova-dimming literature of 2008 "
               "instead of the expansion-rate discrepancy of 2019, and the reason we can "
               "answer the strong form of the claim rather than a three-word fragment.</p>"

               "<p><strong>What Sungenis does with the science is careful in one respect and "
               "decisive in another.</strong> He quotes Clifton, Ferreira &amp; Land&rsquo;s "
               "<em>Living in a Void: Testing the Copernican Principle with Distant "
               "Supernovae</em> (Phys. Rev. Lett. 101:131302, 2008) at length and without "
               "trimming the inconvenient parts &mdash; including their statement that such a "
               "model would require us to &ldquo;live near the center of a spherically "
               "symmetric under-density, on a scale of the same order of magnitude as the "
               "observable Universe&rdquo;, and their remark that within standard inflationary "
               "cosmology &ldquo;the probability of large, deep voids occurring is extremely "
               "small&rdquo;. That is more scrupulous quotation than the list manages. The move "
               "happens afterwards. Clifton, Ferreira &amp; Land wrote a <em>test proposal</em>: "
               "the operative word is the one in their title, and their conclusion is that "
               "supernova surveys concentrated at redshift 0.1&ndash;0.4 would discriminate "
               "between the two paradigms. A paper designed to make the Copernican principle "
               "falsifiable is read as a paper reporting that it has been falsified.</p>"

               "<p><strong>Read the section&rsquo;s frame, too.</strong> It sits in a chapter "
               "titled <em>Evidence Earth is in the Center of the Universe</em>, and it opens "
               "with Edwin Hubble&rsquo;s 1937 sentences about a &ldquo;unique position &hellip; "
               "analogous, in a sense, to the ancient conception of a central Earth&rdquo;. "
               "Sungenis quotes enough of that passage to contain Hubble&rsquo;s own answer to "
               "it &mdash; that to &ldquo;restore homogeneity&rdquo; the observation &ldquo;must "
               "be compensated by spatial curvature&rdquo;. Hubble&rsquo;s escape from the "
               "unique position was geometry, not geocentrism, and the quotation carries the "
               "refutation of the use it is put to.</p>")),

    steelman=dict(
        description=("<p><strong>SURFACE (weak &mdash; do not use).</strong> &ldquo;The Hubble "
                     "tension is a measurement error and it will go away.&rdquo; This is the "
                     "easy dismissal and it is not supportable. A June 2026 review of the "
                     "decade calls it a discrepancy that has &ldquo;likely become a real crisis "
                     "for modern cosmology&rdquo;, persisting whether or not the early-Universe "
                     "side uses <em>Planck</em> and whether or not the late-Universe side uses "
                     "distance ladders at all. Riess and the SH0ES team put the local value at "
                     "73.04&nbsp;&plusmn;&nbsp;1.04 km&nbsp;s<sup>&minus;1</sup>Mpc<sup>&minus;1"
                     "</sup> against 67.4&nbsp;&plusmn;&nbsp;0.5 from <em>Planck</em>+&Lambda;CDM, "
                     "a five-sigma gap, and close their abstract with the sentence &ldquo;The "
                     "source of this now long-standing discrepancy between direct and "
                     "cosmological routes to determining the Hubble constant remains "
                     "unknown.&rdquo; That is the standing position of the people who made the "
                     "measurement.</p>"

                     "<p><strong>DEEPER.</strong> Both of the escapes the two items name are "
                     "real hypotheses with real advocates. On the measurement side, Freedman&rsquo;s "
                     "Chicago&ndash;Carnegie Hubble Program &mdash; run by the astronomer who led "
                     "the original Key Project that measured H<sub>0</sub> in the first place "
                     "&mdash; gets 70.39&nbsp;&plusmn;&nbsp;1.22&nbsp;(stat)&nbsp;&plusmn;&nbsp;"
                     "1.33&nbsp;(sys) from the tip of the red giant branch, and from JWST data "
                     "alone 68.81 (TRGB) and 67.80 (JAGB), concluding that their results are "
                     "&ldquo;consistent with the current standard &Lambda;CDM model, without the "
                     "need for the inclusion of additional new physics&rdquo;. On the location "
                     "side, Keenan, Barger &amp; Cowie measured the K-band luminosity density "
                     "rising by about half again beyond z&nbsp;&asymp;&nbsp;0.07 and said in 2013 "
                     "that an underdensity of that scale would be &ldquo;sufficient to resolve "
                     "the apparent tension&rdquo;; Haslbauer, Banik &amp; Kroupa built it into a "
                     "cosmological model in 2020; and in 2025 Banik &amp; Kalaitzidis took 42 "
                     "baryon-acoustic-oscillation distance measurements spanning twenty years and "
                     "found the void-free model gives a total &chi;<sup>2</sup> of 75.7 where the "
                     "void models give 47.3&ndash;51.2, cutting the discrepancy from 3.3&sigma; to "
                     "1.1&ndash;1.4&sigma;. Anyone who answers this cluster by saying the void "
                     "idea is fringe is simply wrong about the journals.</p>"

                     "<p><strong>KERNEL.</strong> The strongest form is not &ldquo;there is an "
                     "anomaly&rdquo;. It is that <em>cosmology has itself put the Copernican "
                     "principle on the table as a testable assumption and fitted models in which "
                     "we are not typical observers</em>. Clifton, Ferreira &amp; Land&rsquo;s 2008 "
                     "paper exists to make that assumption falsifiable. Camarena, Marra, Sakr "
                     "&amp; Clarkson open their 2022 study by stating that statistical homogeneity "
                     "may be reached only on far larger scales than usually assumed, that "
                     "&ldquo;we are not necessarily typical observers&rdquo;, and that the "
                     "Copernican principle &ldquo;could be recovered only on super-Hubble "
                     "scales&rdquo; &mdash; and then decline to assume it, letting CMB, BAO, "
                     "supernovae, local H<sub>0</sub>, cosmic chronometers, Compton "
                     "<em>y</em>-distortion and kinetic Sunyaev&ndash;Zel&rsquo;dovich data "
                     "constrain a &Lambda;LTB model with a free radial profile. A defender who "
                     "says &ldquo;professional cosmologists model us as non-typical observers "
                     "and publish the likelihoods&rdquo; is describing the literature "
                     "accurately.</p>"),

        why_it_doesnt_save_claim=("<p>Because the location those models make special is not the "
                                  "Earth, and the reason is a resolution limit rather than a "
                                  "preference. What bounds the observer&rsquo;s position inside a "
                                  "void is the microwave dipole: sit off-centre and the outflow "
                                  "gives you a dipole larger than the one we see. Alnes &amp; "
                                  "Amarzguioui worked this out for their spherically symmetric "
                                  "model and found the observer &ldquo;has to be located within a "
                                  "radius of ~15 Mpc from the center for the induced dipole to be "
                                  "less than that observed by the COBE satellite&rdquo;. Fifteen "
                                  "megaparsecs is about 49 million light-years. Every galaxy in "
                                  "the Local Group, the whole Local Sheet and thousands of others "
                                  "sit inside that tolerance, and the Earth is about 3.6&nbsp;&times;"
                                  "&nbsp;10<sup>16</sup> times smaller than it. That bound is "
                                  "theirs and it is for their own model &mdash; an underdensity "
                                  "they describe as &ldquo;around 1500 Mpc&rdquo; in extent, built "
                                  "as an alternative to dark energy rather than as a description of "
                                  "the ~300 Mpc local void argued for today &mdash; and no "
                                  "equivalent centring bound for that shallower void is present in "
                                  "any of the papers cited on this page. It does not matter which "
                                  "way the number moves. The Earth&ndash;Sun distance is "
                                  "4.8&nbsp;&times;&nbsp;10<sup>&minus;12</sup> Mpc, so the "
                                  "tolerance would have to tighten by a factor of about "
                                  "3&nbsp;&times;&nbsp;10<sup>12</sup> &mdash; more than twelve "
                                  "orders of magnitude &mdash; before a void model could express "
                                  "the difference between &ldquo;the Earth&rdquo; and &ldquo;the "
                                  "Sun&rdquo;. A hypothesis whose "
                                  "finest available &ldquo;here&rdquo; is a ball 49 million "
                                  "light-years in radius is not evidence about which body inside that "
                                  "ball is central; it cannot see the Earth at all. Indranil Banik, "
                                  "whose paper produced the 2025 headlines, states the referent "
                                  "himself: &ldquo;our galaxy is close to the centre of a large, "
                                  "local void.&rdquo; His university&rsquo;s release, quoting him, "
                                  "had already reworded that to &ldquo;Earth and our solar "
                                  "system&rdquo;, in the headline and in the body &mdash; so the "
                                  "substitution is inherited from the press office rather than "
                                  "invented by the list. It is a resolution error in both "
                                  "places.</p>"

                                  "<p>And the non-Copernican fits do not deliver what the kernel "
                                  "promises. Camarena, Marra, Sakr &amp; Clarkson, having refused "
                                  "to assume the Copernican principle, report that their &Lambda;LTB "
                                  "model beats &Lambda;CDM <em>only</em> if you restrict the "
                                  "supernovae to the 0.023&nbsp;&lt;&nbsp;z&nbsp;&lt;&nbsp;0.15 "
                                  "window used to fit H<sub>0</sub>: &ldquo;If one considers all "
                                  "the supernova sample, then the H<sub>0</sub> tension is not "
                                  "solved and the support for the &Lambda;LTB model vanishes.&rdquo; "
                                  "Their reconstructed local spacetime is a <em>shallow</em> void, "
                                  "&delta;<sub>L</sub>&nbsp;&asymp;&nbsp;&minus;0.04 out to about "
                                  "300 Mpc, which they note sits on the border of the 95% credible "
                                  "region of ordinary &Lambda;CDM expectation. The most careful "
                                  "non-Copernican analysis available ends with a mild "
                                  "underdensity of the kind the standard model predicts should "
                                  "exist &mdash; not with a privileged observer.</p>")),

    refutation=("<p><strong>1. The concession first, and it is not grudging.</strong> The Hubble "
                "tension is real and unresolved. Two routes to the same number disagree: the "
                "distance ladder gives 73.04&nbsp;&plusmn;&nbsp;1.04 (Riess et al., 2022) and the "
                "microwave background read through &Lambda;CDM gives 67.4&nbsp;&plusmn;&nbsp;0.5 "
                "(<em>Planck</em> 2018), about five sigma apart. It has survived a decade of "
                "attack from both ends. It is one of the two or three most-discussed open "
                "problems in physical cosmology, and this page takes no side on how it will be "
                "resolved. A reader should be suspicious of anyone &mdash; on either side of this "
                "argument &mdash; who says it is settled.</p>"

                "<p><strong>2. The two items are two rival explanations, and each one kills the "
                "other.</strong> This is not a debating point; it is what the words mean in the "
                "literature they come from. <em>Observation bias</em> is the hypothesis that the "
                "local measurement is wrong &mdash; a systematic in Cepheid photometry, in the "
                "supernova calibration, in the choice of anchor. <em>Location bias</em> is the "
                "hypothesis that the local measurement is right but describes an unrepresentative "
                "patch, because outflow from a nearby underdensity inflates redshifts within it. "
                "If the first is true, the 73 is an artefact, there is no discrepancy, and "
                "nothing remains from which to infer anybody&rsquo;s location. If the second is "
                "true, the photometry is fine and the first item is false. The list counts them "
                "as two proofs of one conclusion, when they are two mutually exclusive candidate "
                "explanations of one number &mdash; and the conclusion follows from neither.</p>"

                "<p><strong>3. Item 98, observation bias, at full strength.</strong> Take the "
                "strongest available version, which is not the list&rsquo;s. Wendy Freedman &mdash; "
                "who led the HST Key Project that produced the modern H<sub>0</sub> in the first "
                "place &mdash; runs a programme built specifically to check the ladder with "
                "methods that do not use Cepheids, and gets 70.39&nbsp;&plusmn;&nbsp;1.22&nbsp;"
                "(stat)&nbsp;&plusmn;&nbsp;1.33&nbsp;(sys) from the tip of the red giant branch, "
                "68.81 from JWST TRGB alone and 67.80 from JWST JAGB stars, concluding that these "
                "are &ldquo;consistent with the current standard &Lambda;CDM model&rdquo;. That is "
                "a serious, credentialed argument that the local number carries a systematic. "
                "Three things follow, and none of them is the item&rsquo;s conclusion. "
                "<em>First</em>, the specific systematic most often proposed has been tested and "
                "failed: Riess and collaborators observed more than a thousand Cepheids with JWST "
                "across the distance range of the ladder, found the mean HST&ndash;JWST distance "
                "difference to be &minus;0.01&nbsp;&plusmn;&nbsp;0.03 mag, and rejected "
                "unrecognised crowding of Cepheid photometry as the cause of the tension at 8.2 "
                "sigma &mdash; higher confidence than the tension itself. <em>Second</em>, if "
                "Freedman turns out to be right the item defeats itself, because the anomaly it "
                "is pointing at ceases to exist. <em>Third</em>, and decisively, every proposition "
                "in that dispute is about the photometry of variable stars in ten to forty other "
                "galaxies. Not one of them says anything about the Earth&rsquo;s shape, motion or "
                "position.</p>"

                "<p><strong>4. The other reading of &ldquo;observation bias&rdquo;, which the "
                "neighbouring items invite, refutes itself faster.</strong> Item 98 sits in a run "
                "&mdash; <em>Planck data Earth preference</em>, <em>Satellite stability "
                "Earth-frame</em>, <em>Flyby anomalies Earth-centered</em> &mdash; whose theme is "
                "that measurements come out Earth-favouring because Earth-bound observers make "
                "them. Grant the premise in full: yes, every measurement of H<sub>0</sub> is made "
                "from the Earth or from instruments launched from it. Then notice what the "
                "tension is. It is a <em>disagreement between two Earth-based measurements</em>. "
                "A bias shared by all observations made from here cannot produce a difference "
                "between two of them; the common factor cancels. Whatever is generating the "
                "five-sigma gap is precisely the thing the two methods do <em>not</em> share.</p>"

                "<p><strong>5. Item 325, location bias, at full strength &mdash; and it is the "
                "strongest thing in this cluster.</strong> There is a live, refereed case that we "
                "sit in a large underdensity. Keenan, Barger &amp; Cowie combined UKIDSS and "
                "2MASS photometry with five redshift surveys and found the K-band luminosity "
                "density climbing beyond z&nbsp;&asymp;&nbsp;0.07 to roughly 1.5 times the local "
                "value, concluding that an underdensity &ldquo;of roughly this scale and "
                "amplitude would be sufficient to resolve the apparent tension between direct "
                "measurements of the Hubble constant and those inferred by <em>Planck</em>&rdquo;. "
                "Haslbauer, Banik &amp; Kroupa turned that into a full model in 2020. Banik &amp; "
                "Kalaitzidis then tested it against something the void was not built to fit: 42 "
                "isotropically-averaged BAO distances published over twenty years, where the "
                "void-free model gives a total &chi;<sup>2</sup> of 75.7 and the void models "
                "47.3&ndash;51.2, reducing the discrepancy from 3.3&sigma; to 1.1&ndash;1.4&sigma;. "
                "Banik&rsquo;s own summary of that comparison, for the Royal Astronomical Society: "
                "&ldquo;a void model is about one hundred million times more likely than a "
                "void-free model with parameters designed to fit the CMB observations taken by "
                "the <em>Planck</em> satellite.&rdquo; The paper itself is more measured &mdash; "
                "these results &ldquo;could indicate a local void, which was motivated by "
                "considerations unrelated to BAO data or the Hubble tension&rdquo; &mdash; and it "
                "is that sentence this cluster deserves an answer to.</p>"

                "<p><strong>6. And the counter-evidence, given at the same strength, because the "
                "dispute is genuinely open.</strong> Kenworthy, Scolnic &amp; Riess assembled 1295 "
                "spectroscopic supernovae from 0.01&nbsp;&lt;&nbsp;z&nbsp;&lt;&nbsp;2.26, modelled "
                "a void with an inhomogeneous Lemaitre&ndash;Tolman&ndash;Bondi metric, and found "
                "the luminosity-distance&ndash;redshift relation inconsistent at 4&ndash;5 sigma "
                "with underdensities of |&delta;|&nbsp;&gt;&nbsp;20% of the kind galaxy-count "
                "studies had proposed, with a 5 sigma bound of &delta;&nbsp;&lt;&nbsp;27% on "
                "scales above 69&nbsp;h<sup>&minus;1</sup>&nbsp;Mpc. Wu &amp; Huterer modelled the "
                "local measurement in an N-body simulation including the real spatial "
                "distribution of supernovae and got a sample variance of 0.31 "
                "km&nbsp;s<sup>&minus;1</sup>Mpc<sup>&minus;1</sup> against the roughly 6 needed, "
                "noting that a void deep enough (&delta;&nbsp;&asymp;&nbsp;&minus;0.8 at ~150 Mpc) "
                "would be &ldquo;very unlikely&rdquo; and would violate existing constraints. And "
                "the most striking check comes from inside the void camp: Stiskalek, Desmond &amp; "
                "Banik fitted KBC-void models to direct Tully&ndash;Fisher distances from "
                "CosmicFlows-4 and found the velocity field prefers a void smaller than 70 Mpc "
                "&mdash; under a tenth of the fiducial size &mdash; and that the two profiles "
                "favoured by the Bayesian evidence bring the predicted local value only to "
                "within 3&sigma; of the four-anchor distance ladder they compare against. A 2026 "
                "review of the decade states "
                "flatly that a local Hubble bubble or void &ldquo;has long been ruled out as a "
                "significant contribution&rdquo;. We do not adjudicate that. We report that the "
                "case is contested by serious people on both sides, which is already more than "
                "the item admits.</p>"

                "<p><strong>7. Now the step nobody in that dispute is arguing about, which is "
                "where the item actually fails.</strong> Suppose the void wins outright. What has "
                "been established is that the region around the Local Group, out to something "
                "like 300 Mpc, is perhaps 20% below the cosmic mean, and that we are near its "
                "middle. How near is set by the microwave dipole, because an off-centre observer "
                "in an outflowing void sees a dipole: Alnes &amp; Amarzguioui found for their "
                "model that the observer must lie within about 15 Mpc of the centre for the "
                "induced dipole to stay under the COBE value. Fifteen megaparsecs is 49 million "
                "light-years. The Milky Way is 0.03 Mpc across; Andromeda is 0.78 Mpc away; the "
                "Virgo cluster is at about 16.5 Mpc. The centring constraint is a ball whose "
                "radius is roughly 3.6&nbsp;&times;&nbsp;10<sup>16</sup> Earth diameters, and "
                "every galaxy in "
                "the Local Group is inside it. There is no measurement here that distinguishes "
                "the Earth from the Sun, from Andromeda, or from a galaxy thirty million "
                "light-years away. Two scoping notes, both of which cut the same way. Their model "
                "is not this one: the underdensity they are centring the observer in is, in their "
                "words, &ldquo;around 1500 Mpc&rdquo; in extent and exists as an alternative to "
                "dark energy, and no centring bound computed for the ~300 Mpc void at issue here "
                "is present in any of the papers cited on this page. And the number is not "
                "load-bearing: the Earth&ndash;Sun separation is 4.8&nbsp;&times;&nbsp;"
                "10<sup>&minus;12</sup> Mpc, so the tolerance would have to tighten by more than "
                "twelve orders of magnitude before any void model could mean &ldquo;the "
                "Earth&rdquo; rather than &ldquo;the Sun&rdquo;. The claim&rsquo;s own advocate "
                "uses the right noun: <em>our "
                "galaxy</em> is near the centre &mdash; though, as the compression note below "
                "records, the press release carrying that quote had already converted it to "
                "&ldquo;Earth and our solar system&rdquo;. Either way, converting it into a "
                "statement about the Earth "
                "is not a stronger reading of the evidence; it is a claim at a resolution the "
                "evidence does not have.</p>"

                "<p><strong>8. &ldquo;Special&rdquo; is doing two jobs, and the item swaps "
                "them.</strong> In the void literature a special location means a "
                "<em>statistically atypical</em> one: our patch is emptier than average, which is "
                "surprising in &Lambda;CDM in proportion to how empty and how large it is. It does "
                "not mean a <em>geometrically privileged</em> one. Most of the volume of the "
                "cosmic web is underdense &mdash; voids are the common case, not the rare one "
                "&mdash; and the standard model expects observers to sit in mild ones; that is "
                "exactly why Camarena and colleagues could report a best-fit "
                "&delta;<sub>L</sub>&nbsp;&asymp;&nbsp;&minus;0.04 and call it borderline-normal "
                "rather than revolutionary. Nor is a void model a model of a centre: it is "
                "spherically symmetric <em>about a point</em>, chosen for tractability, embedded "
                "in a universe that carries on homogeneously outside it, expanding, with no edge "
                "and no middle. The item borrows the surprise of the first sense and the "
                "cosmology of the second.</p>"

                "<p><strong>9. The premise the argument cannot pay for.</strong> The Hubble "
                "tension is a disagreement between two estimates of the expansion rate of a "
                "general-relativistic expanding universe. Everything on both sides presupposes "
                "that: redshift as recession, supernovae of type Ia as standard candles "
                "calibrated through Cepheids or red giants in other galaxies, baryon acoustic "
                "oscillations as a standard ruler, and recombination physics at z&nbsp;&asymp;"
                "&nbsp;1100. The void solution does not weaken those assumptions; it adds one, "
                "the Lemaitre&ndash;Tolman&ndash;Bondi metric, which is a solution of Einstein&rsquo;s "
                "field equations, and it needs the Local Group&rsquo;s velocity relative to the "
                "microwave background as an input. Elsewhere the same list files dark matter and "
                "dark energy as modern epicycles (<a href=\"#ARG-D14\">ARG-D14</a>) and asserts "
                "that redshifts fall in quantized concentric shells around the Earth "
                "(<a href=\"#ARG-E12\">ARG-E12</a>) &mdash; a claim which, if it held, would "
                "break the smooth redshift&ndash;distance relation that both sides of the "
                "tension are built on, and with no smooth Hubble flow there is no Hubble "
                "constant and no tension to interpret. The two items can have the anomaly or "
                "they can have the "
                "conclusion. They cannot have both, because the anomaly is only visible through "
                "the machinery the conclusion discards.</p>"

                "<p><strong>10. What the void model says about our motion, which is the opposite "
                "of rest.</strong> A geocentric reading wants the Earth fixed at a centre. The "
                "void model does not offer that. Its whole mechanism is matter flowing outward "
                "from the underdensity toward the denser exterior &mdash; Banik&rsquo;s own "
                "description &mdash; and the Local Group is measured to be moving at about 620 "
                "km&nbsp;s<sup>&minus;1</sup> with respect to the frame in which the microwave "
                "background is isotropic. Haslbauer, Banik &amp; Kroupa use that velocity as one "
                "of the observables constraining their model. The best case for item 325 is "
                "therefore a model in which we are near the middle of a large underdensity and "
                "moving briskly through it, in an expanding universe, on a planet orbiting a "
                "star. Every one of those clauses is standard cosmology.</p>"

                "<p><strong>Verdict: misleading, and the misleading part is the word "
                "&ldquo;bias&rdquo;.</strong> Both items point at genuine, contested, well-funded "
                "research. Neither discriminates. On the observation reading the subject matter is "
                "variable stars in other galaxies; on the location reading it is the mean density "
                "of a large region around the Local Group, whose centre is pinned, at best, to "
                "within 49 million light-years. The "
                "list files both under a heading about the Earth, and the arithmetic of the "
                "underlying papers would be unchanged if the Earth were deleted from them.</p>"),

    advocate=dict(
        best_defense=(
            "Look at what you have just conceded. The tension is real and unresolved. The void "
            "reading is published in MNRAS and getting stronger, not weaker — a hundred million "
            "to one on BAO data, by your own quotation. Professional cosmologists have formally "
            "suspended the Copernican principle and fitted models in which we are not typical "
            "observers, and one of them says in print that we may sit near the centre of a "
            "structure a billion light-years across. Then, having conceded all of that, you "
            "retreat to a quibble about resolution: the centre is 'our galaxy', not 'the Earth'. "
            "For our purposes that is a distinction without a difference. We say the observer "
            "occupies a privileged spot; you have just spent six paragraphs conceding that "
            "leading astronomers think the observer may occupy a privileged spot, and then "
            "objected that they did not name the postcode. Your fifteen-megaparsec figure comes "
            "from one 2006 paper about one void profile — hardly a law of nature. Your "
            "'you cannot use the machinery you reject' move is worse: it is question-begging by "
            "construction. We are running an internal critique. On your own assumptions, with "
            "your own instruments, your own data say the observer is special; that is precisely "
            "the form a reductio takes, and complaining that we used your premises to reach it is "
            "complaining that the argument works. And you buried the best evidence in a gloss: "
            "Edwin Hubble looked at his own data, saw a unique position, called it intolerable, "
            "and reached for curvature to escape it. You quote him admitting the escape was "
            "motivated. That is our case, in the founder's own words."),
        survives=3,
        preemptive=(
            "Three, and the number is set by the reductio move, not by the rest. Two changes hold "
            "the entry together and both are already in the text; keep them there. FIRST, the "
            "internal-critique objection is answered by GRANTING it rather than by refusing the "
            "premises. Section 9 as written does not say 'you may not use our machinery'; it says "
            "that on the machinery the anomaly requires, the conclusion the list wants is already "
            "false — the Lemaitre-Tolman-Bondi metric is a solution of Einstein's equations "
            "embedded in an expanding FLRW background, the void model takes the Local Group's "
            "620 km/s motion relative to the CMB as an input, and section 10 states that the best "
            "case for item 325 is a model in which we move briskly through an expanding universe "
            "on a planet orbiting a star. A reductio that ends in heliocentrism is not a reductio "
            "of heliocentrism. That sentence must stay attached to section 9; split them and the "
            "strongest paragraph becomes the weakest. SECOND, the resolution argument is not a "
            "quibble and must not be allowed to read as one, so it stays quantified and stays "
            "attributed: 15 Mpc is Alnes and Amarzguioui's number for their model, it is scoped "
            "as such in section 7 — their model is a ~1500 Mpc dark-energy substitute, not the "
            "~300 Mpc void under discussion, and no centring bound for the latter was found in "
            "the cited literature. The answer to 'hardly a law of nature' is therefore not to "
            "restate the figure but to point out that it is not load-bearing: the Earth-Sun "
            "separation is 4.8e-12 Mpc, so the tolerance would have to tighten by more than "
            "twelve orders of magnitude before any void model could express the proposition 'the "
            "Earth rather than the Sun'. The conclusion survives the number being wrong in either "
            "direction, and section 7 must keep saying so. Also keep Banik's own noun — 'our "
            "galaxy' — in the text and in the compression block, because the defender's strongest "
            "rhetorical move is to treat that substitution as pedantry, and it is far easier to "
            "resist when the advocate's own witness is the one making the distinction — but keep "
            "it next to the press release's 'Earth and our solar system', which the compression "
            "note now quotes. A defender who clicks the single link we give for Banik's words "
            "lands on a page headlined 'Is Earth inside a huge void?'. Conceding that the "
            "substitution starts in the press office rather than on the list costs the argument "
            "nothing and removes the entry's most clickable vulnerability. THIRD, on "
            "Hubble 1937: do not litigate the quotation, because the quotation defeats the use "
            "without help. The passage Sungenis prints contains Hubble's own resolution — restore "
            "homogeneity by spatial curvature — and the gloss says so in one sentence. Leave it "
            "there and do not expand it; the 1937 material belongs to ARG-E17 and ARG-R12, and "
            "importing that fight into this entry would dilute the two items actually under "
            "review."),
    ),

    straw_man=dict(
        identified=True,
        detail=("The items are presented as facts modern cosmology must awkwardly accommodate, "
                "and both are in fact hypotheses cosmology raised, named and tested itself. "
                "'Hubble tension' is the field's own term for its own unsolved problem. The "
                "observation-bias reading is Freedman's position, argued from a JWST programme "
                "designed expressly to look for the systematic. The location-bias reading was "
                "put on the table by Keenan, Barger and Cowie in 2013 and is currently pressed "
                "hardest by Banik and Kroupa in MNRAS. The falsification test for the whole "
                "non-Copernican family was designed by Clifton, Ferreira and Land in Physical "
                "Review Letters in 2008, and Camarena and colleagues ran the fit in 2022 without "
                "assuming the Copernican principle at all. There is also an implied suppression "
                "the record does not support: every result on both sides of this cluster is in "
                "the open refereed literature, most of it on arXiv, and the void story was the "
                "Royal Astronomical Society's own press item at its 2025 national meeting."),
    ),

    compression=dict(
        assessed=True, drifted=True,
        list_phrasing=("Hubble tension observation bias. / Hubble tension location bias."),
        source_wording=("Banik &amp; Kalaitzidis, MNRAS 540:545 (2025), closing their abstract: "
                        "&ldquo;our results suggest that recent evidence of BAO observables "
                        "deviating from expectations in the homogeneous <em>Planck</em> cosmology "
                        "<strong>could indicate</strong> a local void, which was motivated by "
                        "considerations unrelated to BAO data or the Hubble tension.&rdquo; And "
                        "the same author, describing it for the Royal Astronomical Society in "
                        "2025: &ldquo;<strong>A potential solution</strong> to this inconsistency "
                        "is that <strong>our galaxy</strong> is close to the centre of a large, "
                        "local void.&rdquo;"),
        drift_type="hedge_dropped",
        note=("The comparison is run against the astronomy, because that is where the two items "
              "come from: no movement text naming the Hubble tension was located in the searches "
              "run for this entry, which are written out in the passage block above. Three things "
              "change in transit. <strong>The conditional goes.</strong> Every serious statement "
              "of the location reading is a conditional or a modal &mdash; <em>could indicate</em>, "
              "<em>a potential solution</em>, <em>might inflate redshifts</em>, and in Keenan, "
              "Barger &amp; Cowie&rsquo;s original, <em>would be sufficient to resolve</em> if the "
              "luminous matter traces the mass. A three-word noun phrase has no room for an "
              "antecedent, so the item states as a property of the world what its sources state as "
              "a hypothesis under test. <strong>The referent had already moved.</strong> Banik "
              "says "
              "&ldquo;our galaxy&rdquo;; Haslbauer, Banik &amp; Kroupa say &ldquo;around the Local "
              "Group&rdquo;; Clifton, Ferreira &amp; Land say &ldquo;near the center of a "
              "spherically symmetric under-density&rdquo;. But the swap to the planet is not the "
              "list&rsquo;s invention, and it would be convenient and false to say it was. The "
              "University of Portsmouth release that carries Banik&rsquo;s quote &mdash; the one "
              "linked in the sources below &mdash; is headlined <em>Is Earth inside a huge "
              "void?</em>, and says in its own voice that &ldquo;Earth and our solar system would "
              "need to be near the centre of a void about a billion light-years in radius and "
              "with a density about 20 per cent below the average&rdquo;. The drift from the "
              "galaxy to the planet begins in the professional communication of the result, and "
              "the list inherited it. What the list adds is the filing. In a news item "
              "&ldquo;Earth&rdquo; is ordinary shorthand for our cosmic neighbourhood; "
              "on a list of proofs that the Earth is "
              "not a spinning ball, filed between <em>Dipole anisotropy exact fit</em> and "
              "<em>Cold Spot preferred axis</em>, the same word becomes a claim about the planet "
              "&mdash; at "
              "a resolution roughly 3.6&nbsp;&times;&nbsp;10<sup>16</sup> times finer than the "
              "measurement supports. <strong>The dispute disappears.</strong> The same twelve "
              "months that produced the void headlines also produced a direct-distance test, "
              "co-authored by the void&rsquo;s own leading advocate, preferring a void under a "
              "tenth of the fiducial size. None of that survives compression, and the item that "
              "circulates carries none of it. <strong>The enum is approximate here and we say so "
              "rather than forcing it:</strong> <em>hedge_dropped</em> is recorded because the "
              "conditional is the largest single thing lost, but a case exists for "
              "<em>scope_widened</em> &mdash; a claim about the mean density of the Local "
              "Group&rsquo;s neighbourhood becomes a claim about the Earth&rsquo;s place in the "
              "cosmos &mdash; and the two items also stand in a relation the enum has no name "
              "for, since each is the negation of the other&rsquo;s premise. <strong>One drift "
              "runs the other way, and it is worth recording.</strong> The movement text quoted "
              "above is <em>less</em> hedged than the list: Sungenis writes that it &ldquo;is "
              "clear&rdquo; that cosmology is a desperate attempt to avoid a geocentric universe, "
              "while faithfully reproducing his sources&rsquo; own caveats a page earlier. The "
              "certainty in this cluster was not manufactured by the compression; it was there in "
              "1937, in 2008 and in 2013, and the list simply inherited it. <strong>The refutation "
              "above answers the source, not the fragment:</strong> it takes Banik &amp; "
              "Kalaitzidis&rsquo;s BAO result at its published strength, quotes the counter-"
              "evidence at its published strength, declines to declare the dispute over, and puts "
              "the weight on the step that neither side of it disputes &mdash; that the "
              "&ldquo;location&rdquo; in question is a region tens of megaparsecs across, and the "
              "Earth is not visible at that scale."),
    ),

    verdict_challenge=dict(challenged=False, proposed_verdict=None, reasoning=None),

    people=["PER-SUNGENIS"],
    related=["E01", "E02", "E04", "E06", "E11", "E12", "E13", "E17", "R12", "D14"],

    sources=[
        dict(label="Riess et al., “A Comprehensive Measurement of the Local Value of the "
                   "Hubble Constant with 1 km/s/Mpc Uncertainty from HST and the SH0ES Team”, "
                   "ApJL 934:L7 (2022) — H0 = 73.04 ± 1.04, a 5σ difference from Planck+ΛCDM, "
                   "and “the source of this now long-standing discrepancy … remains unknown”",
             url="https://arxiv.org/abs/2112.04510"),
        dict(label="Kenworthy, Scolnic & Riess, “The Local Perspective on the Hubble Tension: "
                   "Local Structure Does Not Impact Measurement of the Hubble Constant”, "
                   "ApJ 875:145 (2019) — 1295 SNe, LTB void modelling, |δ| > 20% excluded at "
                   "4–5σ and δ < 27% at 5σ above 69 h⁻¹ Mpc",
             url="https://arxiv.org/abs/1901.08681"),
        dict(label="Keenan, Barger & Cowie, “Evidence for a ~300 Mpc Scale Under-density in "
                   "the Local Galaxy Distribution”, ApJ 775:62 (2013) — the KBC void, and the "
                   "conditional claim that such an underdensity “would be sufficient to "
                   "resolve” the tension",
             url="https://arxiv.org/abs/1304.2884"),
        dict(label="Haslbauer, Banik & Kroupa, “The KBC void and Hubble tension contradict "
                   "ΛCDM on a Gpc scale — Milgromian dynamics as a possible solution”, "
                   "MNRAS 499:2845 (2020) — δ = 0.46 ± 0.06 between 40 and 300 Mpc around the "
                   "Local Group, with the Local Group's CMB-frame velocity as a constraint",
             url="https://arxiv.org/abs/2009.11292"),
        dict(label="Banik & Kalaitzidis, “Testing the local void hypothesis using baryon "
                   "acoustic oscillation measurements over the last twenty years”, "
                   "MNRAS 540:545 (2025) — 42 D_V measurements, χ² 75.7 void-free against "
                   "47.3–51.2 with a void, 3.3σ → 1.1–1.4σ",
             url="https://arxiv.org/abs/2501.17934"),
        dict(label="University of Portsmouth / RAS National Astronomy Meeting release, July "
                   "2025 — Banik: “A potential solution to this inconsistency is that our "
                   "galaxy is close to the centre of a large, local void”; ~1 billion "
                   "light-years radius, ~20% underdense. Note the release’s own framing, which "
                   "is where the Earth-referent enters: it is headlined “Is Earth inside a huge "
                   "void?” and writes that “Earth and our solar system would need to be near "
                   "the centre” of it",
             url="https://www.port.ac.uk/news-events-and-blogs/news/is-earth-inside-a-huge-void-sound-of-the-big-bang-hints-at-possible-solution-to-hubble-tension"),
        dict(label="Stiskalek, Desmond & Banik, “Testing the local supervoid solution to the "
                   "Hubble tension with direct distance tracers” (arXiv:2506.10518, v2 "
                   "September 2025) — CosmicFlows-4 Tully–Fisher distances prefer a void "
                   "under 70 Mpc, less than 10% of the fiducial size",
             url="https://arxiv.org/abs/2506.10518"),
        dict(label="Camarena, Marra, Sakr & Clarkson, “A void in the Hubble tension? The end "
                   "of the line for the Hubble bubble”, Class. Quantum Grav. 39:184001 (2022) "
                   "— a ΛLTB fit that does not assume the Copernican principle; support "
                   "vanishes on the full SN sample; best fit δ_L ≈ −0.04 out to ~300 Mpc",
             url="https://arxiv.org/abs/2205.05422"),
        dict(label="Wu & Huterer, “Sample variance in the local measurements of the Hubble "
                   "constant”, MNRAS 471:4946 (2017) — σ(H0_loc) = 0.31 km/s/Mpc against the "
                   "~6 required, and δ ≈ −0.8 at ~150 Mpc judged very unlikely",
             url="https://arxiv.org/abs/1706.09723"),
        dict(label="Freedman, Madore, Jang, Hoyt, Lee & Owens, “Status Report on the "
                   "Chicago-Carnegie Hubble Program: Measurement of the Hubble Constant Using "
                   "HST and JWST” (arXiv:2408.06153) — TRGB 70.39 ± 1.22 ± 1.33; JWST-only "
                   "TRGB 68.81 and JAGB 67.80; “consistent with the current standard ΛCDM "
                   "model”",
             url="https://arxiv.org/abs/2408.06153"),
        dict(label="Riess et al., “JWST Observations Reject Unrecognized Crowding of Cepheid "
                   "Photometry as an Explanation for the Hubble Tension at 8σ Confidence” "
                   "(arXiv:2401.04773) — HST−JWST mean distance difference −0.01 ± 0.03 mag",
             url="https://arxiv.org/abs/2401.04773"),
        dict(label="Clifton, Ferreira & Land, “Living in a Void: Testing the Copernican "
                   "Principle with Distant Supernovae”, Phys. Rev. Lett. 101:131302 (2008) — "
                   "the test proposal Galileo Was Wrong quotes; discriminates via the "
                   "redshift dependence of luminosity distance at z ~ 0.1–0.4",
             url="https://arxiv.org/abs/0807.1443"),
        dict(label="Alnes & Amarzguioui, “CMB anisotropies seen by an off-center observer in "
                   "a spherically symmetric inhomogeneous universe”, Phys. Rev. D 74:103520 "
                   "(2006; astro-ph/0607334) — the observer must sit within ~15 Mpc of the "
                   "void centre to keep the induced dipole below the COBE value",
             url="https://arxiv.org/abs/astro-ph/0607334"),
        dict(label="Zhang & Stebbins, “Confirmation of the Copernican principle at Gpc radial "
                   "scale and above from the kinetic Sunyaev-Zel'dovich effect power "
                   "spectrum”, PRL 107:041301 (2011) — the kSZ bound that rules out adiabatic "
                   "void models of dark-energy-mimicking depth; see ARG-R12 and ARG-E17",
             url="https://arxiv.org/abs/1009.3967"),
        dict(label="Cai & Wang, “The Hubble tension: A decade review” (arXiv:2606.20434, v2 "
                   "14 July 2026) — “likely become a real crisis for modern cosmology”, and "
                   "the review's judgement that a local bubble or void “has long been ruled "
                   "out as a significant contribution”",
             url="https://arxiv.org/abs/2606.20434"),
        dict(label="Sungenis & Bennett, Galileo Was Wrong, Vol. I ch. 3, 7th ed. 2013 — "
                   "Internet Archive three-volume scan (item galileo-was-wrong-the-church-"
                   "was-right-sungenis-vol-1-3-complete); djvu text downloaded whole and "
                   "searched for the Hubble-tension vocabulary",
             url="https://archive.org/details/galileo-was-wrong-the-church-was-right-sungenis-vol-1-3-complete"),
    ]),
}
