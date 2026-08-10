# -*- coding: utf-8 -*-
"""
Batch 9 — ARG-E10, "Zodiacal dust and Kuiper structure show ecliptic symmetry".
5 items (196, 332, 348, 349, 350), lane E, verdict STANDARD PHYSICS, cluster record
carrying originator=None, originator_work=None, year=None, real_source=None.

Research notes for whoever picks this up next.


1. THE ITEMS, AND WHERE THEY SIT ON THE SPECIMEN PAGE
------------------------------------------------------
  196  "Dust inflow Sun-Earth line."
  332  "Zodiacal contamination persistent."
  348  "Zodiacal cloud symmetry."
  349  "Kuiper clumps ecliptic."
  350  "Dust inflow apex mismatch."

All five were re-read off the live page at withthesun33.com/about-1 on 2026-08-09 and
match `corpus.py` character for character. Their neighbourhoods matter, because the list
has no headings and position is the only context an item carries:

  * 196 sits in a run of Earth-directed anomalies that slides into esoterica —
    "Solar oblateness constancy. Dust inflow Sun-Earth line. GRB anisotropy. Earth heart
    chakra symbolism. Zodiac cross rotation around center."
  * 348, 349 and 350 sit together in a run about reference frames and solar-system
    structure — "Gaia reduction flexible. Zodiacal cloud symmetry. Kuiper clumps
    ecliptic. Dust inflow apex mismatch. Oort cloud unnecessary."
  * 332 sits somewhere else entirely: inside the CMB-anomaly block, between "ISW
    correlations ecliptic-linked" and "Kinematic SZ ambiguity".

That last one is a record problem, not a writing problem, and it is reported up rather
than fixed here: `assign.py` is not this file's to edit. On the page it came from, item
332's referent is almost certainly the zodiacal-light FOREGROUND in microwave maps — the
standing question of whether the ecliptic-aligned low-multipole features survive
foreground modelling — which is ARG-E01 and ARG-E11 territory. The treatment below
answers it in both readings so that nothing is lost if the assignment stands.


2. PROVENANCE: THE SEARCH WAS RUN, AND IT TERMINATED IN AN ANSWER
-------------------------------------------------------------------
`compression.assessed` is set to "no_source", the E17 state. That is a result, not a
backlog item, and here is the route so it can be checked or overturned.

Texts searched in full, and only these:
  (A) Sungenis & Bennett, *Galileo Was Wrong* Vol. I, the 2006 GWW_Final scan, Internet
      Archive item `GallileoWasWrong`, file "Gallileo was wrong_djvu.txt" (3.3 MB OCR).
  (B) The complete seventh edition (2013), Volumes 1-3, Internet Archive item
      `galileo-was-wrong-the-church-was-right-sungenis-vol-1-3-complete` (5.5 MB OCR).
  (C) The separate Vol. II seventh-edition scan, item
      `GalileoWasWrongTheChurchSungenisRobertA.Bennett4276` (1.8 MB OCR).
  (D) van der Kamp, *De Labore Solis* (1988), the geocentricity.com PDF, via pdftotext.

Counts across (A)-(D), case-insensitive, whole-file:
  "Kuiper"          0, 0, 0, 0
  "gegenschein"     0, 0, 0, 0
  "Oort"            0, 0, 0, 0
  "dust ring"       0, 0, 0, 0
  "zodiacal light"  0, 0, 0, 0
  "zodiacal"        0, 1, 0, 0  — the single hit in (B) is Aquinas on "the zodiacal
                                  movement" of the starry heaven, in the chapter on the
                                  consensus of the Fathers. Astrological, not optical.
  "interplanetary" 22 in (B), every one about the aether (Maxwell quotations) or about
                   JPL radar and probe-navigation equations. None about dust.

Web searching for a geocentric or flat-earth argument from zodiacal-cloud or Kuiper-belt
structure returned nothing: the queries came back with the astronomical literature only.
A domain-restricted pass over geocentricity.com returned the Association for Biblical
Astronomy's standard pages, none on this subject.

There is also a hard chronological bound worth keeping. The first Kuiper-belt object,
1992 QB1, was found in August 1992; the mean-plane and orbital-clustering results item
349 would have to be drawing on are from 2014 onward. Item 349 therefore cannot descend
from the founding Tychonian texts — van der Kamp 1988, and Bouw's *Geocentricity* of
1992 — whatever else it descends from. That is a dating argument, not a search result,
and it holds independently of what any scan contains.

Conclusion recorded: untraced rather than guessed. Nobody is credited. E10 was one of
the 28 clusters the README flags as provisionally untraced; this audit came back
untraced, which is the opposite outcome to E13's.


3. THE HEDGE RULE WITH NO AUTHOR TO HEDGE — WHAT IT BINDS US TO ANYWAY
-----------------------------------------------------------------------
With no original there is no hedged sentence to answer, and the E17 precedent says to
answer the argument on its own terms. But there is a second source layer here that DOES
hedge, and the rule bites on it: the five items borrow their vocabulary wholesale from
working astronomy, and that literature is enormously more careful than the fragments.
"Kuiper clumps" compresses a mean-plane measurement that its own authors publish at
2.5 sigma with an explicit list of ways it could be an artefact. "Dust inflow apex
mismatch" compresses a flow-direction measurement whose error bars are +/-20 deg in
longitude and +/-10 deg in latitude and which moved by 30-50 deg in 2005 for reasons
still being modelled. So the discipline the hedge rule exists to enforce applies in full,
just aimed one layer over: represent the astronomy at the strength the astronomers state
it, including where it is unresolved. ARG-E01 is the precedent for saying so out loud,
and section 5 below does it.


4. THE PHYSICS HINGE, IN ONE SENTENCE
---------------------------------------
Measure the plane instead of naming it, and it is not the ecliptic. Two independent fits
to the same COBE/DIRBE data:

  Kelsall et al. 1998 (ApJ 508:44)   i = 2.03 +/- 0.02 deg,   Omega = 77.7 +/- 0.6 deg
  Cosmoglobe DR2 III (2024)          i = 2.195 +/- 0.007 deg, Omega = 75.6 +/- 0.1 deg

against the invariable plane at i = 1.58 deg, Omega = 107.6 deg (quoted in Volk &
Malhotra 2017) and the ecliptic at i = 0 by definition. Angles between planes, computed
in session 2026-08-09 by spherical trigonometry on those published values:

  K98 cloud plane  -> ecliptic 2.03 deg | invariable 1.03 deg | Venus orbit 1.37 deg
  DR2 cloud plane  -> ecliptic 2.19 deg | invariable 1.20 deg | Venus orbit 1.20 deg

On both fits the ecliptic is the WORST of the three fits to the dust. Four lines of
Python; anyone can redo it. The Venus column uses the J2000 elements i = 3.39471 deg,
Omega = 76.680 deg and is reported as arithmetic on published numbers — no dynamical
claim is made from it here, because none was needed and none was sourced.

The other decisive number is radial. Hayabusa2 measured the zodiacal light's dependence
on heliocentric distance from 0.76 to 1.06 AU — i.e. from outside Earth's orbit as well
as inside it — and found n(r) proportional to r^-1.30 +/- 0.08 (Tsumura et al., EPS
75:121, 2023), matching Helios and Pioneer from the 1970s-80s. The cloud's density is a
one-parameter function of distance FROM THE SUN. That is the shape of the claim these
items would have to break, and the test they would have to pass is stated in the body:
show a structure organised on geocentric distance or geocentric latitude.


5. WHAT IS GENUINELY LIVE HERE, AND MUST BE SAID SO
-----------------------------------------------------
Two of the five items touch open questions. Neither is geocentric, and neither is closed.

  (a) THE KUIPER BELT'S MEAN PLANE. Volk & Malhotra (AJ 154:62, 2017) measured the
      classical belt at i_m = 1.8 (+0.7/-0.4) deg, Omega_m = 77 (+18/-14) deg — within
      1 sigma of secular theory — and found the distant belt (50-80 au) off the expected
      plane at the ~97-99% level, floating an unseen planetary-mass body at a < 100 au as
      a cause. That result has an erratum and a contested history. Siraj, Chyba &
      Tremaine (MNRAS Letters 543:L27, 2025) report a warp relative to the invariable
      plane at 80-400 au at 2.52 and 2.74 sigma (false-alarm probabilities 4% and 2%),
      state that earlier studies found no significant warp in the distant belt, and
      attribute those nulls to resonant contamination, narrow semimajor-axis ranges and
      catalogue limits. OSSOS XIV, "The Plane of the Kuiper Belt" (AJ 158:49, 2019), is
      the survey-side treatment. This is unresolved. Do not write it as settled in either
      direction.

  (b) THE INTERSTELLAR DUST INFLOW. Sterken et al. (ApJ 812:141, 2015) put the flow at
      259 +/- 20 deg ecliptic longitude, 8 +/- 10 deg latitude, ~26 km/s, and report a
      shift of ~30 deg in latitude around 2005, up to 50 deg for the smallest grains,
      best explained by the Lorentz force in the inner heliosphere with time-dependent
      filtering at the heliospheric boundary. The direction is measured; the
      time-dependence is an active modelling problem.

The honest position is that both are live, and that neither has a geocentric reading
available: (a) is measured against the invariable plane and its candidate explanation is
a planet, (b) is a measurement of the SUN's motion relative to a named parcel of gas.


6. VERDICT
------------
STANDARD PHYSICS holds and is not challenged. The items are noun phrases naming real
structure; the structure is real, it is explained, and it does not discriminate. Worth
noting for the record that the SHARPER readings of 348 and 349 — "the zodiacal cloud is
symmetric about the ecliptic", "Kuiper-belt clumps lie in the ecliptic" — are each
contradicted by a specific measurement, which on this project's rubric is REFUTED. The
verdict was left alone because the items as written do not assert the sharp form, and
because "real, already explained, does not discriminate" is the more useful thing to say
to a reader. If a later reviewer disagrees, the numbers for the harder verdict are all
in section 4.

Two record problems reported up rather than written around: item 332's cluster
assignment, and the cluster `note` — "Solar-system material lies in the solar-system
plane. That is what a solar system is." — which renders beside the verdict chip and is
loose in exactly the way this treatment turns on. There is no single "solar-system
plane": the ecliptic, the invariable plane and the zodiacal cloud's symmetry surface are
three different planes, mutually inclined by one to two degrees, and the argument gets
stronger, not weaker, when that is said precisely.
"""

ENTRY = {

"E10": dict(

    tldr=("Solar-system dust does lie in a plane — and when the plane is measured rather "
          "than named, it is not ours. Two independent fits to the same COBE/DIRBE data put "
          "the zodiacal cloud's symmetry surface 2.03° and 2.19° away from Earth's orbital "
          "plane, tilted toward the invariable plane of the Sun and giant planets. The only "
          "component of that cloud whose shape depends on where the Earth is turns out to be a "
          "wake — a dust concentration trailing 0.2 AU behind us, with a hole where we are — "
          "and a wake is what a moving body leaves. No author was found for these five items; "
          "the search "
          "that ended in that answer is set out below."),

    passage=None,

    untraceable=r"""<p>There is no original to quote, and the search that established this is worth publishing because it is the point of the project. The specimen carries no citation for these five items &mdash; it carries none for any item &mdash; so the search ran outward through the literature the rest of the list demonstrably draws on. Here is what was searched, and where it stopped.</p>

<p><strong>Four texts, read end to end by keyword.</strong> (A) Sungenis &amp; Bennett, <em>Galileo Was Wrong</em> Vol.&nbsp;I, the 2006 <em>GWW_Final</em> scan at Internet Archive item <code>GallileoWasWrong</code>. (B) The complete seventh edition of 2013, Volumes&nbsp;1&ndash;3, at item <code>galileo-was-wrong-the-church-was-right-sungenis-vol-1-3-complete</code>. (C) The separate seventh-edition Vol.&nbsp;II scan at item <code>GalileoWasWrongTheChurchSungenisRobertA.Bennett4276</code>. (D) van der Kamp, <em>De Labore Solis</em> (1988), the PDF at geocentricity.com. In those four texts, searched in full: <strong>&ldquo;Kuiper&rdquo; returns zero occurrences, &ldquo;zodiacal light&rdquo; zero, &ldquo;dust ring&rdquo; zero, &ldquo;gegenschein&rdquo; zero, &ldquo;Oort&rdquo; zero.</strong> &ldquo;Zodiacal&rdquo; returns exactly one hit across all four, in (B): Aquinas on <em>the zodiacal movement</em> of the starry heaven, quoted in the chapter on the consensus of the Fathers, which is astrology and not optics. &ldquo;Interplanetary&rdquo; returns 22 hits in (B), every one of them either a Maxwell quotation about the aether or a discussion of JPL&rsquo;s probe-navigation equations. That is a statement about those four texts and the OCR routes used to read them, and about nothing else.</p>

<p><strong>A dating argument that does not depend on any scan.</strong> The first Kuiper-belt object, 1992&nbsp;QB1, was found in August&nbsp;1992. The mean-plane and orbital-clustering results that item&nbsp;349 would have to be compressing are from 2014 onward. So whatever else item&nbsp;349 descends from, it cannot descend from the movement&rsquo;s founding texts &mdash; van der Kamp&rsquo;s <em>De Labore Solis</em> (1988) or Bouw&rsquo;s <em>Geocentricity</em> (1992) &mdash; because the object of the claim had not been discovered when they were written. The same bound applies to item&nbsp;350: the Ulysses interstellar-dust measurements it compresses begin in 1992 and the sixteen-year synthesis is from 2015.</p>

<p><strong>What the vocabulary suggests, offered as a hypothesis and not as a finding.</strong> The five phrasings are compressed in a distinctive way &mdash; noun-plus-noun labels with the verb removed (&ldquo;Zodiacal cloud symmetry&rdquo;, &ldquo;Kuiper clumps ecliptic&rdquo;, &ldquo;Dust inflow apex mismatch&rdquo;) &mdash; and each maps onto a heading or an abstract-line in the technical literature rather than onto anything in the geocentric corpus. The most economical reading is that this cluster was assembled from a sweep of the astronomical literature for the words <em>ecliptic</em> and <em>Earth</em>, rather than inherited from an argument someone made. We have not established that, and we do not publish it as established. What is established is the negative: an originator was looked for and not found.</p>

<p><strong>Consequence for the rebuttal.</strong> The hedge rule says to answer the source&rsquo;s hedged wording rather than the list&rsquo;s compression. With no source, there is nothing to hedge &mdash; but the rule still binds, one layer over. These items are compressions of <em>working astronomy</em>, and that literature hedges heavily: the Kuiper-belt warp is published at 2.5&sigma; with the artefacts that could produce it listed by its own authors, and the dust-inflow direction carries &plusmn;20&deg; and &plusmn;10&deg; error bars and a 30&ndash;50&deg; excursion in 2005 that is still being modelled. The refutation below states those at the strength the papers state them, including where they are open.</p>
<p><strong>An honest note on our limits.</strong> No author found means we did not find one, not that none exists. These are one-line compressions with no citation in the specimen, and a claim of this shape can enter circulation through a broadcast, a livestream or an image caption that leaves nothing to search. A reader who can point us at someone who argued this in print, on air, anywhere datable, will improve the entry and we will publish the correction.</p>""",

    steelman=dict(
        description=r"""<p><strong>SURFACE (weak &mdash; do not use).</strong> &ldquo;Dust in the solar system, of course it is in the plane of the solar system.&rdquo; True, dismissive, and it concedes the interesting half of the case without noticing. Anyone who stops there has not looked at what is actually in the zodiacal cloud, and will be embarrassed by the first person who has.</p>

<p><strong>DEEPER.</strong> Coplanarity is a <em>prediction</em> of the accretion-disc account: material that condensed out of a rotating disc keeps the disc&rsquo;s angular momentum, and Poynting&ndash;Robertson drag then spirals the small grains inward toward the star. Ecliptic structure is therefore what heliocentrism forecasts, and the same forecast is confirmed elsewhere &mdash; debris discs are seen edge-on and face-on around other stars. True, and still incomplete, because it does not touch the specific Earth-referenced structures the items are pointing at.</p>

<p><strong>KERNEL.</strong> There really are structures in the interplanetary medium keyed to the Earth and to the Sun&ndash;Earth line, and a defender of these items is not making them up. Five of them, conceded in full:</p>
<p>(1) <strong>The Earth has its own circumsolar dust ring.</strong> Dermott et al. predicted it from resonant trapping (<em>Nature</em> 369:719, 1994) &mdash; &ldquo;the Earth is embedded in a circumsolar ring of asteroidal dust, and has a cloud of dust permanently in its wake&rdquo; &mdash; and Reach et al. confirmed it with COBE (<em>Nature</em> 374:521, 1995). It is a named component of the standard zodiacal model.</p>
<p>(2) <strong>The gegenschein is a real brightening at exactly the antisolar point</strong>, an 8&ndash;10&deg; patch first described by Brorsen in 1854, sitting precisely on the Sun&ndash;Earth line extended.</p>
<p>(3) <strong>The dust cloud&rsquo;s inner edge is at Earth&rsquo;s orbit.</strong> Juno&rsquo;s star-tracker impact detections map a cloud running from about 1 AU out to about 2 AU (Jorgensen et al., <em>JGR Planets</em> 126, 2021). Earth&rsquo;s orbit is where it stops.</p>
<p>(4) <strong>The whole infrared and microwave sky must be cleaned of an ecliptic-aligned foreground</strong> before anyone can read cosmology out of it. Planck devoted a paper to it (<em>Planck</em> 2013 results XIV).</p>
<p>(5) <strong>The interstellar dust really does arrive from a direction well away from the solar apex.</strong> It streams in from ecliptic longitude 259&deg;, latitude +8&deg;; the solar apex is at longitude 280&deg;, latitude +53&deg;. Those are 48&deg; apart. The item calls this a mismatch and it is one.</p>
<p>That is five real things, four of them with the Earth or the Sun&ndash;Earth line in them. The strong form of this cluster is not &ldquo;dust is in a plane&rdquo;; it is <em>&ldquo;the interplanetary medium has structure that is indexed to us, and your own models say so by name.&rdquo;</em></p>""",
        why_it_doesnt_save_claim=r"""<p>Because every one of the five, read at the resolution its own paper provides, turns out to be a signature of <strong>motion</strong> or of a <strong>Sun-centred geometry</strong>, and two of them are only intelligible if the Earth is going somewhere.</p>

<p><strong>The ring is a wake, and a wake has a direction.</strong> Mean-motion resonance is a relationship between two <em>orbital periods</em>; a body that does not orbit cannot trap anything in one. And the trapped material is not arranged symmetrically about the Earth. Reach&rsquo;s Spitzer mapping (<em>Icarus</em> 209:848, 2010) finds a relative scarcity of dust within 0.1 AU of the Earth and an enhancement centred <strong>0.2 AU behind</strong> us, 0.08 AU wide, about 3% brighter at 8&nbsp;&micro;m viewed from inside it; Reach&rsquo;s 1995 paper puts it as &ldquo;the region trailing the Earth being substantially more dense than that in the leading direction.&rdquo; A hole where we are and a blob behind us is not a halo centred on us. It is a track.</p>

<p><strong>The gegenschein is carried by the observer.</strong> It is a backscatter maximum at zero phase angle, so it appears at whatever direction is opposite the Sun <em>from wherever the observer happens to be</em>. Everyone in the cloud has one, and it is not evidence about where its owner is standing. The one version of the claim that would have been physical &mdash; a genuine dust concentration parked at the Sun&ndash;Earth L2 point &mdash; was tested and dropped in 1970, when better photometry showed no significant shadow and bounded any L2 contribution at a few per cent of the light.</p>

<p><strong>The inner edge is a removal, not a boundary.</strong> The reason the Juno cloud stops at 1 AU is that the Earth&rsquo;s gravity takes the grains out; the cloud&rsquo;s outer edge sits just past Mars and its inclination matches Mars&rsquo;s orbit, which is why Mars is the leading candidate source. A structure whose inner limit is set by a body sweeping through it is a structure that body is travelling in.</p>

<p><strong>A foreground is near, and near is not central.</strong> Zodiacal emission has to be subtracted because it lies between the telescope and the sky &mdash; that is what the word means. Its ecliptic alignment is the least surprising fact in the file: the dust orbits the Sun, we orbit inside it, so we see it as a band. And in the standard model the alignment is not even to <em>our</em> plane; see the numbers below.</p>

<p><strong>Two apexes, both of them the Sun&rsquo;s.</strong> The mismatch in item 350 is between the Sun&rsquo;s motion relative to the <em>Local Interstellar Cloud</em> and the Sun&rsquo;s motion relative to the mean of the nearby stars. Different reference material, different answer &mdash; and the dust direction agrees with the independently measured interstellar helium direction to 5&deg;, which is the confirmation that the dust is streaming with that cloud. Both quantities are motions of the solar system. An argument for a stationary Earth cannot spend either of them.</p>""",),

    refutation=r"""<p><strong>Start by granting the whole of it.</strong> The zodiacal cloud is real, it is roughly a flattened disc, the Kuiper belt is roughly a flattened torus, the Earth sits inside a resonant dust ring of its own, the gegenschein sits on our antisolar line, and the ecliptic foreground has to be modelled before anyone reads cosmology out of an infrared or microwave map. None of that is in dispute and nothing below denies any of it. What follows is what happens when each is measured to the precision its own literature provides.</p>

<h4>1. The plane is measured, and it is not ours</h4>

<p>&ldquo;Zodiacal cloud symmetry&rdquo; sounds like a statement about the ecliptic. It is not, because the cloud&rsquo;s symmetry surface has been fitted twice, independently, to the same COBE/DIRBE data, and both fits put it off the ecliptic in the same direction:</p>
<p style="margin-left:1.2em"><em>Kelsall et al.</em> (ApJ 508:44, 1998): inclination <em>i</em> = 2.03&deg; &plusmn; 0.02&deg;, ascending node &Omega; = 77.7&deg; &plusmn; 0.6&deg;.<br>
<em>Cosmoglobe DR2 III</em> (arXiv:2408.11004, 2024), refitting the same data: <em>i</em> = 2.195&deg; &plusmn; 0.007&deg;, &Omega; = 75.6&deg; &plusmn; 0.1&deg;.</p>
<p>Those are formal fit errors rather than a full systematics budget, and the two analyses differ by more than their error bars, which is the honest way to say that the systematics dominate. But they agree on the thing that matters: the surface is tilted, and tilted the same way. Compare the invariable plane &mdash; the angular-momentum plane of the Sun and planets, dominated by Jupiter &mdash; at <em>i</em> = 1.58&deg;, &Omega; = 107.6&deg; (Souami &amp; Souchay, A&amp;A 543:A133, 2012; the values as quoted by Volk &amp; Malhotra 2017). Spherical trigonometry on those published numbers, recomputed in session on 2026-08-09, gives the separations:</p>
<p style="margin-left:1.2em">Kelsall surface: <strong>2.03&deg; from the ecliptic</strong>, 1.03&deg; from the invariable plane, 1.37&deg; from Venus&rsquo;s orbital plane.<br>
Cosmoglobe surface: <strong>2.19&deg; from the ecliptic</strong>, 1.20&deg; from the invariable plane, 1.20&deg; from Venus&rsquo;s orbital plane.</p>
<p>On both fits, of the three candidate planes, <strong>the Earth&rsquo;s is the worst fit to the dust.</strong> The cloud is better described by the plane the giant planets define than by the plane we define. (The Venus column is arithmetic on the J2000 elements <em>i</em>&nbsp;=&nbsp;3.39471&deg;, &Omega;&nbsp;=&nbsp;76.680&deg;, reported as a numerical comparison; no dynamical claim is made from it here.) The reason zodiacal models carry an inclination and a node as free parameters at all is that the fit demands them: in the standard parameterisation each component &ldquo;is allowed to have a plane of symmetry that is different from the Ecliptic&rdquo; (San et al., A&amp;A 666:A107, 2022), because the data reject the assumption that it is not.</p>

<p>The radial structure settles the frame question by itself. Hayabusa2 measured the zodiacal light&rsquo;s brightness against heliocentric distance from 0.76 to 1.06 AU &mdash; from outside the Earth&rsquo;s orbit as well as inside it &mdash; and recovered a dust density going as <em>r</em><sup>&minus;1.30 &plusmn; 0.08</sup>, consistent with Helios and Pioneer four decades earlier (Tsumura et al., <em>Earth, Planets and Space</em> 75:121, 2023). One parameter, and the parameter is distance from the Sun.</p>

<h4>2. The one Earth-shaped thing in the cloud is a wake</h4>

<p>Here is the sentence that decides the cluster, and it comes from the model&rsquo;s own documentation: in the standard six-component description of the interplanetary dust, <strong>every component except one is distributed symmetrically about the Sun</strong> &mdash; the diffuse cloud, the three asteroidal band pairs and the circumsolar ring &mdash; and the exception is the <em>Earth-trailing feature</em> (San et al. 2022). The circumsolar ring is Earth-<em>resonant</em>, but it is a ring: axisymmetric about the Sun, and it would look the same wherever along it the Earth happened to be. The single component whose geometry depends on where the Earth actually is, rather than on where the Sun is, is not a shell around us. It is a blob behind us.</p>

<p>Its parameters are published. Spitzer mapping of the ring&rsquo;s azimuthal structure finds a relative scarcity of dust within 0.1 AU of the Earth, and an enhancement centred 0.2 AU <em>behind</em> the Earth with a width of 0.08 AU, showing as roughly a 3% brightening at 8&nbsp;&micro;m when viewed from inside it (Reach, <em>Icarus</em> 209:848, 2010). COBE saw the same asymmetry a decade and a half earlier: &ldquo;the region trailing the Earth being substantially more dense than that in the leading direction&rdquo; (Reach et al., <em>Nature</em> 374:521, 1995). Dermott et al. had predicted it before either measurement, from the physics of resonant trapping, and stated it as the Earth having &ldquo;a cloud of dust permanently in its wake&rdquo; (<em>Nature</em> 369:719, 1994).</p>

<p>Two things follow and they run in the same direction. First, mean-motion resonance is a commensurability between orbital periods; the trapping mechanism is not available to a body that does not orbit. Second, the asymmetry has a sense. A hole at the Earth and a concentration behind it is the shape a body ploughing through a medium leaves, and it points along the direction of travel. If the Earth stood still while the dust circulated, the leading and trailing sides would have no reason to differ.</p>

<p>And the ring is not ours alone. A circumsolar dust ring has been imaged near the orbit of Venus (Jones, Bewsher &amp; Brown, <em>Science</em> 342:960, 2013, with STEREO heliospheric imagers; mapped further in <em>Icarus</em> 288:172, 2017 and with Parker Solar Probe/WISPR in 2021) and evidence reported for one near Mercury&rsquo;s (Stenborg et al., ApJ 868:74, 2018). Resonant rings are what planets have. Ours is a member of a family, and membership of a family is the opposite of a privileged position.</p>

<h4>3. &ldquo;Dust inflow Sun&ndash;Earth line&rdquo;: the gegenschein travels with whoever is looking</h4>

<p>The brightening at the antisolar point is real, about 8&ndash;10&deg; across, first described by Theodor Brorsen in 1854, and it lies exactly on the Sun&ndash;Earth line extended. It is also a scattering effect: an opposition surge, the backscatter maximum that occurs at zero phase angle, where every illuminated grain in the line of sight is seen at full phase. Its location is defined by the geometry between the Sun, the observer and the dust &mdash; which means it is centred on the observer, wherever the observer is, and it therefore carries no information about where the observer is. The one version of the claim that would have been a genuine physical concentration &mdash; dust pooled at the Sun&ndash;Earth L2 point, casting a shadow &mdash; was tested and abandoned in 1970, when better photometry found no significant shadow and left L2 dust contributing at most a few per cent of the light.</p>

<p>The inflow itself is likewise Sun-directed rather than Earth-directed. Poynting&ndash;Robertson drag removes orbital angular momentum from small grains and spirals them <em>toward the Sun</em>; that is the transport mechanism that sustains the whole cloud, and it operates on heliocentric orbits. Where the Earth enters the story is as a sink, not a centre: Juno&rsquo;s star-tracker detections give a cloud running from roughly 1 AU to roughly 2 AU, with the inner edge set by the Earth&rsquo;s gravity clearing grains out and the outer edge just past Mars, the cloud&rsquo;s inclination matching Mars&rsquo;s orbit closely enough that Mars is the leading candidate for its source (Jorgensen et al., <em>JGR Planets</em> 126, e2020JE006509, 2021). A cloud whose inner boundary is the place a moving planet sweeps clean is a cloud that planet is moving through.</p>

<h4>4. &ldquo;Kuiper clumps ecliptic&rdquo;: it is a torus, its plane is not ours, and its clumps belong to Neptune</h4>

<p>The Kuiper belt is not a sheet in the ecliptic. Its main concentration extends about ten degrees out of the ecliptic with a more diffuse distribution several times further, which is why it is usually described as a torus; the dynamically cold classical population sits within roughly 10&deg;, the hot population reaches 30&deg;, and the scattered disc goes further still. A structure with a 30&deg; inclination spread is not evidence of confinement to a plane.</p>

<p>Its mean plane has been measured, and it is not the ecliptic either: Volk &amp; Malhotra (AJ 154:62, 2017) find the classical belt at <em>i<sub>m</sub></em> = 1.8&deg; (+0.7/&minus;0.4), &Omega;<sub>m</sub> = 77&deg; (+18/&minus;14), within 1&sigma; of what secular perturbation theory predicts for the forced plane at that semimajor axis. The plane a small-body population settles into is set by the long-term perturbations of the eight planets and varies with distance from the Sun &mdash; which is why there is no single &ldquo;solar-system plane&rdquo; to be symmetric about, and why the surface is warped rather than flat.</p>

<p>As for clumps: the Kuiper belt&rsquo;s genuine longitudinal structure is resonant, and the resonances are with <strong>Neptune</strong>. The plutinos sit in the 3:2 commensurability near 39.4 AU and their perihelia are organised relative to Neptune&rsquo;s longitude; the twotinos sit in the 2:1 near 47.7 AU. The clumping in the outer belt is indexed to the orbit of the outermost giant planet, not to the Earth and not to the ecliptic.</p>

<p><strong>And there is a live anomaly in here, which we state as live.</strong> Volk &amp; Malhotra reported the distant belt (50&ndash;80 au) off its expected plane at the ~97&ndash;99% confidence level and raised an unseen planetary-mass body inside about 100 au as a candidate cause. Siraj, Chyba &amp; Tremaine (MNRAS Letters 543:L27, 2025) find a warp relative to the invariable plane at 80&ndash;400 au and 80&ndash;200 au, at 2.52&sigma; and 2.74&sigma; &mdash; false-alarm probabilities of 4% and 2% &mdash; while reporting that earlier studies found no significant warp and attributing those nulls to resonant contamination and catalogue limits. Their own candidate explanation is a body of 0.06&ndash;1 Earth masses near 100&ndash;200 au. The related claim of orbital clustering among the extreme trans-Neptunian objects is contested in the same way: combining the Dark Energy Survey, OSSOS and the Sheppard&ndash;Trujillo survey with their selection functions, Napier et al. (<em>Planet. Sci. J.</em> 2:59, 2021) obtain a 24% joint probability that the sample is drawn from a uniform distribution and conclude the sample provides no evidence for angular clustering &mdash; against a prior analysis putting that probability at 0.2%. Anyone who tells you the outer solar system&rsquo;s geometry is fully understood is overstating. What is not on the table, in any of these papers, is the Earth: every one of these measurements is referred to the invariable plane or to a barycentric frame, and every proposed cause is a planet.</p>

<h4>5. &ldquo;Dust inflow apex mismatch&rdquo;: two apexes, both of them ours</h4>

<p>The mismatch is real and the item has it right. Sixteen years of Ulysses measurements put the interstellar dust streaming into the solar system from ecliptic longitude 259&deg; &plusmn; 20&deg;, latitude +8&deg; &plusmn; 10&deg;, at about 26 km/s (Sterken et al., ApJ 812:141, 2015). The solar apex &mdash; the direction of the Sun&rsquo;s motion relative to the local standard of rest, in Hercules near Vega at RA 18<sup>h</sup>28<sup>m</sup>, Dec +30&deg; &mdash; converts to ecliptic longitude 280.2&deg;, latitude +53.2&deg; (computed in session, J2000 obliquity). The two directions are <strong>48.3&deg;</strong> apart. That is the mismatch.</p>

<p>It is also expected, and its resolution is a second measurement rather than an excuse. The dust direction agrees with the independently determined inflow direction of interstellar neutral <em>helium</em> &mdash; about 255&deg;, +5&deg;, also about 26 km/s &mdash; to <strong>5.0&deg;</strong>, well inside the dust measurement&rsquo;s own error bars. The dust is streaming with the Local Interstellar Cloud, a particular parcel of gas the Sun is currently passing through. The solar apex is the Sun&rsquo;s motion relative to the average of the nearby stars. Two different reference materials, two different relative velocities, one of which is about 26 km/s and the other about 13 km/s. There is no puzzle in their disagreeing; there would be a puzzle in their agreeing.</p>

<p>What the item cannot do is convert either number into a stationary Earth, because both are motions <em>of the solar system</em>, measured by the Doppler and impact signatures of material passing through it. And the honest complication runs against the list rather than for it: the dust inflow direction is not even constant. It shifted by about 30&deg; in ecliptic latitude around 2005, up to 50&deg; for the smallest grains, which Sterken et al. attribute to the Lorentz force in the inner heliosphere plus time-dependent filtering at the heliospheric boundary over the solar cycle. That is an open modelling problem. A direction that changes with the solar magnetic cycle is a poor foundation for a claim about the centre of the universe.</p>

<h4>6. &ldquo;Zodiacal contamination persistent&rdquo;: true in both readings, and geocentric in neither</h4>

<p>This item sits, on the source page, inside the run of CMB anomalies rather than with the other four, so it has two plausible readings and both are answerable.</p>

<p><em>Read as a solar-system claim</em> &mdash; zodiacal emission is a persistent ecliptic-aligned foreground &mdash; it is simply true, and it is why Planck published a dedicated paper on the subject (<em>Planck</em> 2013 results XIV, A&amp;A 571:A14), fitting the emissivities of the diffuse cloud, the dust bands, the circumsolar ring and the Earth-trailing feature across nine frequencies. A foreground is by definition local; that is what distinguishes it from the background it contaminates. And the paper&rsquo;s own conclusion is that the zodiacal correction to the CMB maps is small compared with the CMB temperature power spectrum.</p>

<p><em>Read as a defence of the CMB anomalies</em> &mdash; the ecliptic-aligned low-multipole features are not explained away as zodiacal contamination &mdash; it is also broadly fair, and it belongs to <a href="#ARG-E01">ARG-E01</a> rather than here. The quadrupole&ndash;octopole alignment does persist across WMAP and Planck releases and across cleaning methods; Patel, Aluri &amp; Ralston (MNRAS 539:542) find the octopole &ldquo;consistently remains anomalously aligned with the quadrupole in all the CMB maps studied&rdquo; while also finding no preferred alignment among the low multipoles &#8467; = 2&ndash;61 taken collectively. E01 carries that debate and does not overstate it.</p>

<p>But notice what the item costs whoever plays it. If zodiacal dust does not produce the CMB&rsquo;s ecliptic alignment, then the ecliptic alignment of the dust and the ecliptic alignment of the microwave sky are two unrelated facts, and the first is not evidence for the second. The cluster cannot both offer solar-system ecliptic structure as cosmically significant and insist that solar-system ecliptic structure is not contaminating the cosmological maps.</p>

<h4>7. The test this cluster would have to pass</h4>

<p>State it plainly, because it is short. For any of these observations to bear on the Earth&rsquo;s position, some measured distribution would have to be organised on <strong>geocentric</strong> distance or geocentric latitude &mdash; density falling with distance from the Earth, or a symmetry surface passing through the Earth in a way no heliocentric surface does. Every quantity above is parameterised the other way: the cloud&rsquo;s density as a power law in heliocentric <em>r</em>; the cloud&rsquo;s symmetry surface as an inclination and node measured about the Sun; the Kuiper belt&rsquo;s mean plane referred to the invariable plane; the dust inflow as a velocity of the solar system relative to a named interstellar cloud. The one component in any of these models with the Earth in it is an offset trailing feature, and it is offset <em>because</em> the Earth moves.</p>

<p><strong>Verdict: standard physics.</strong> Every observation the five items name is real and none of them is contested by anyone here. The cluster fails not because the data are wrong but because the data are heliocentric in their construction: the solar system&rsquo;s material lies near a family of planes set by the planets&rsquo; secular perturbations, of which the ecliptic is one member and not the best-fitting one, and the ecliptic is the plane astronomers measure inclinations from for the ordinary reason that it is the plane we are travelling in. That is a coordinate convention, and mistaking a coordinate convention for a physical centre is the error at <a href="#ARG-E15">ARG-E15</a> and <a href="#ARG-R08">ARG-R08</a> in a different vocabulary. The genuinely open questions in this territory &mdash; the warp of the distant Kuiper belt, the solar-cycle wander of the interstellar dust inflow &mdash; are open, and their candidate explanations are an undiscovered planet and the heliospheric magnetic field.</p>""",

    advocate=dict(
        best_defense=(
            "Look at what you conceded. The Earth has its own dust ring. The gegenschein sits "
            "exactly on our anti-solar line. The dust cloud's inner edge is our orbit. The "
            "entire infrared and microwave sky has to be scrubbed of an ecliptic foreground "
            "before you are allowed to read cosmology out of it. The Kuiper belt's plane is a "
            "live controversy your own best paper resolves by postulating a planet nobody has "
            "seen. That is five Earth-referenced structures, and your answer to each one is a "
            "mechanism. Of course you have a mechanism. You always have a mechanism — that is "
            "what a mature research programme buys you, and it is not evidence. "
            "Now the part you should worry about. When the microwave sky lines up with the "
            "ecliptic, you call that a red flag for a local systematic, which is your own E01 "
            "argument. When the dust lines up with the ecliptic, you call it standard physics. "
            "So ecliptic alignment counts against us in both directions, and there is no "
            "measurement we could bring you that would count for us. That is not a rubric, it "
            "is a ratchet. And your headline finding proves the point rather than yours: you "
            "boast that the cloud's plane is two degrees off the ecliptic. Two degrees. You "
            "have confirmed to four significant figures that the dust between here and the "
            "stars lies in essentially our plane, and then you present the fourth digit as a "
            "refutation. Finally, on provenance: you searched four books, found nothing, and "
            "concluded there is no source. Absence of a citation in the four texts you could "
            "download is not evidence about a movement that publishes mostly on video."),
        survives=4,
        preemptive=(
            "Four, and it is the heads-I-win charge that earns the number, not the rest. Three "
            "specific requirements on the text. (a) The double-standard hit must be answered "
            "in the body, and section 6 as written is what answers it — the distinction is "
            "foreground versus background, not convenience: a LOCAL emitter aligning with the "
            "ecliptic is expected because that is where the local material orbits, while a "
            "COSMOLOGICAL signal aligning with the ecliptic is unexpected and is exactly why "
            "it reads as a systematics flag. That paragraph must stay adjacent to the Planck "
            "2013 XIV sentence; if an editor splits them, the strongest section becomes the "
            "weakest. (b) The 'two degrees is nothing' reply is fair and the text should not "
            "rest on the two degrees alone. It does not — the load is carried by the "
            "*direction* of the tilt (toward the invariable plane, away from ours, on two "
            "independent fits) and by the Earth-trailing feature's offset, and both are "
            "already in section 1 and section 2. Do not let a later edit compress those two "
            "sections into the single number. (c) On provenance, the wording must stay scoped "
            "to the four texts searched and must not be strengthened; the untraceable block "
            "already says so, and the dating bound on 1992 QB1 is the part that does not "
            "depend on any search at all. Keep it. One thing NOT to do: do not answer 'you "
            "always have a mechanism' by listing more mechanisms. Answer it with the test in "
            "section 7 — name the measurement that would have gone the other way."),
    ),

    straw_man=dict(
        identified=True,
        detail=("The cluster is aimed at a position no astronomer holds. Nothing in cosmology "
                "says the solar system should lack a preferred plane, and finding structure in "
                "the ecliptic embarrasses nobody: the flattening is a prediction of disc "
                "accretion and the ecliptic is the coordinate plane inclinations are measured "
                "from precisely because we orbit in it. The Copernican principle is a claim "
                "about our location in the universe, not a claim that the solar system is "
                "isotropic. Item 350 does the same thing more specifically: it presents the "
                "offset between the interstellar dust inflow and the solar apex as an anomaly "
                "for the standard account, when the standard account is what predicts the "
                "offset - the two directions are the Sun's motion relative to two different "
                "reference materials, and the published expectation is that they differ."),
    ),

    compression=dict(
        assessed="no_source", drifted=None, list_phrasing=None, source_wording=None,
        drift_type=None,
        note=r"""<p><strong>There is no original to hold these five items against, and the search that established that is published rather than summarised.</strong> Texts searched in full, and only these four: <em>Galileo Was Wrong</em> Vol.&nbsp;I in the 2006 scan at Internet Archive item <code>GallileoWasWrong</code>; the complete seventh edition of 2013, Volumes&nbsp;1&ndash;3, at item <code>galileo-was-wrong-the-church-was-right-sungenis-vol-1-3-complete</code>; the separate seventh-edition Vol.&nbsp;II scan at item <code>GalileoWasWrongTheChurchSungenisRobertA.Bennett4276</code>; and van der Kamp&rsquo;s <em>De Labore Solis</em> (1988) PDF at geocentricity.com. Across those four texts &ldquo;Kuiper&rdquo;, &ldquo;zodiacal light&rdquo;, &ldquo;dust ring&rdquo;, &ldquo;gegenschein&rdquo; and &ldquo;Oort&rdquo; each return zero occurrences; &ldquo;zodiacal&rdquo; returns one, in a quotation of Aquinas about the <em>zodiacal movement</em> of the starry heaven. Film audio and video material were not transcribed here and nothing above is a statement about them.</p>

<p><strong>A bound that holds whatever any scan contains.</strong> 1992&nbsp;QB1, the first Kuiper-belt object, was found in August 1992; the Kuiper mean-plane and clustering results item&nbsp;349 compresses date from 2014 onward, and the Ulysses interstellar-dust synthesis behind item&nbsp;350 is from 2015. Neither item can descend from the founding Tychonian texts, because the objects they name had not been observed when those books were written.</p>

<p><strong>Why this is a finding and not a gap.</strong> The comparison was attempted and it terminated in a result: these five items descend from nobody in particular. That is what the third state of this field is for. It also means the hedge rule has no author&rsquo;s sentence to protect &mdash; but the rule still binds one layer over, because the items are compressions of <em>working astronomy</em>, and that literature is far more careful than the fragments are. Two examples carried through the refutation above. The Kuiper-belt warp behind &ldquo;Kuiper clumps ecliptic&rdquo; is published by Siraj, Chyba &amp; Tremaine at 2.52&sigma; and 2.74&sigma; with false-alarm probabilities of 4% and 2%, and by Volk &amp; Malhotra at 97&ndash;99% confidence with an unseen planet floated as the cause; the inflow direction behind &ldquo;Dust inflow apex mismatch&rdquo; carries &plusmn;20&deg; and &plusmn;10&deg; error bars and moved by 30&ndash;50&deg; in 2005 for reasons still being modelled. The list states both flat. <strong>The refutation answers them at the strength the papers state them, and says where they are open</strong> &mdash; which is the <a href="#ARG-E01">ARG-E01</a> discipline applied to a cluster with no author of its own.</p>

<p><strong>One further note on the specimen&rsquo;s own arrangement.</strong> Four of the five items are consecutive or near-consecutive in a run about solar-system structure. The fifth, item&nbsp;332, sits inside the run of CMB anomalies, between &ldquo;ISW correlations ecliptic-linked&rdquo; and &ldquo;Kinematic SZ ambiguity&rdquo;, which is where a zodiacal <em>foreground</em> claim belongs. The refutation answers it in both readings so that the argument holds whichever way the assignment is eventually settled.</p>""",
    ),

    verdict_challenge=dict(challenged=False, proposed_verdict=None, reasoning=None),

    people=[],
    related=["E01", "E02", "E03", "E04", "E11", "E13", "E15", "E16", "E17"],

    sources=[
        dict(label="Kelsall et al., “The COBE Diffuse Infrared Background Experiment search for "
                   "the cosmic infrared background. II. Model of the interplanetary dust cloud”, "
                   "ApJ 508:44 (1998) — the smooth cloud at i = 2.03° ± 0.02°, Ω = 77.7° ± 0.6°, "
                   "as tabulated in the Cosmoglobe comparison below",
             url="https://ui.adsabs.harvard.edu/abs/1998ApJ...508...44K/abstract"),
        dict(label="Cosmoglobe DR2. III. Improved modeling of zodiacal light with COBE-DIRBE "
                   "through global Bayesian analysis, arXiv:2408.11004 (2024) — refit values "
                   "i = 2.195° ± 0.007°, Ω = 75.6° ± 0.1°, tabulated against Kelsall 1998",
             url="https://arxiv.org/html/2408.11004"),
        dict(label="San, Herman, Erikstad, Galloway & Watts, “COSMOGLOBE: Simulating zodiacal "
                   "emission with ZodiPy”, A&A 666:A107 (2022) — every component symmetric about "
                   "the Sun except the Earth-trailing feature; each component's symmetry plane "
                   "free to differ from the ecliptic",
             url="https://www.aanda.org/articles/aa/full_html/2022/10/aa44133-22/aa44133-22.html"),
        dict(label="Dermott, Jayaraman, Xu, Gustafson & Liou, “A circumsolar ring of asteroidal "
                   "dust in resonant lock with the Earth”, Nature 369:719 (1994) — the prediction, "
                   "and “a cloud of dust permanently in its wake”",
             url="https://ui.adsabs.harvard.edu/abs/1994Natur.369..719D"),
        dict(label="Reach et al., “Observational confirmation of a circumsolar dust ring by the "
                   "COBE satellite”, Nature 374:521 (1995) — “the region trailing the Earth being "
                   "substantially more dense than that in the leading direction”",
             url="https://www.nature.com/articles/374521a0"),
        dict(label="Reach, “Structure of the Earth's circumsolar dust ring”, Icarus 209:848 (2010) "
                   "— Spitzer/IRAC: depletion within 0.1 AU of Earth, enhancement centred 0.2 AU "
                   "behind Earth, width 0.08 AU, ~3% at 8 μm",
             url="https://authors.library.caltech.edu/records/97z32-0dg04"),
        dict(label="Jones, Bewsher & Brown, “Imaging of a circumsolar dust ring near the orbit of "
                   "Venus”, Science 342:960 (2013) — the Earth's resonant ring is one of a family",
             url="https://oro.open.ac.uk/39071"),
        dict(label="Stenborg et al., “Evidence for a circumsolar dust ring near Mercury's orbit”, "
                   "ApJ 868:74 (2018)",
             url="https://iopscience.iop.org/article/10.3847/1538-4357/aae6cb"),
        dict(label="Jorgensen et al., “Distribution of interplanetary dust detected by the Juno "
                   "spacecraft and its contribution to the zodiacal light”, JGR Planets 126, "
                   "e2020JE006509 (2021) — cloud from ~1 to ~2 AU, inner edge set by Earth's "
                   "gravity, inclination matching Mars",
             url="https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2020JE006509"),
        dict(label="Tsumura et al., “Heliocentric distance dependence of zodiacal light observed "
                   "by Hayabusa2#”, Earth, Planets and Space 75:121 (2023) — n(r) ∝ r^−1.30 ± 0.08 "
                   "measured from 0.76 to 1.06 AU",
             url="https://link.springer.com/article/10.1186/s40623-023-01856-x"),
        dict(label="Gegenschein — antisolar backscatter maximum, ~8–10° across, first described by "
                   "Brorsen in 1854; the L2 dust-concentration reading dropped in 1970 when better "
                   "photometry showed no significant shadow",
             url="https://en.wikipedia.org/wiki/Gegenschein"),
        dict(label="Volk & Malhotra, “The curiously warped mean plane of the Kuiper belt”, "
                   "AJ 154:62 (2017) — classical belt at i_m = 1.8°, Ω_m = 77°; distant belt off "
                   "the expected plane at ~97–99% confidence; invariable plane at i = 1.58°, "
                   "Ω = 107.6°",
             url="https://arxiv.org/abs/1704.02444"),
        dict(label="Siraj, Chyba & Tremaine, “Measuring the mean plane of the distant Kuiper "
                   "belt”, MNRAS Letters 543:L27 (2025) — warp at 80–400 au and 80–200 au at "
                   "2.52σ and 2.74σ; earlier null results and why the authors think they were null",
             url="https://arxiv.org/pdf/2508.14156"),
        dict(label="OSSOS. XIV. “The Plane of the Kuiper Belt”, AJ 158:49 (2019) — the survey-side "
                   "treatment of the same question",
             url="https://iopscience.iop.org/article/10.3847/1538-3881/ab24e1"),
        dict(label="Napier et al., “No evidence for orbital clustering in the extreme "
                   "trans-Neptunian objects”, Planet. Sci. J. 2:59 (2021) — DES + OSSOS + "
                   "Sheppard–Trujillo with selection functions, 24% joint probability of a "
                   "uniform underlying distribution",
             url="https://discovery-pp.ucl.ac.uk/10134772/1/Napier_2021_Planet._Sci._J._2_59.pdf"),
        dict(label="Sterken et al., “Sixteen years of Ulysses interstellar dust measurements in "
                   "the solar system. III.”, ApJ 812:141 (2015) — inflow from 259° ± 20°, "
                   "+8° ± 10° at ~26 km/s, matching the interstellar helium direction; the ~30–50° "
                   "latitude shift of 2005 attributed to the Lorentz force",
             url="https://iopscience.iop.org/article/10.1088/0004-637X/812/2/141"),
        dict(label="Solar apex — RA 18h28m, Dec +30°, in Hercules near Vega; ~13.4 km/s relative "
                   "to the local standard of rest. Converted here to ecliptic longitude 280.2°, "
                   "latitude +53.2° (J2000 obliquity), 48.3° from the dust inflow direction",
             url="https://en.wikipedia.org/wiki/Solar_apex"),
        dict(label="Souami & Souchay, “The solar system's invariable plane”, A&A 543:A133 (2012)",
             url="https://www.aanda.org/articles/aa/full_html/2012/07/aa19011-12/aa19011-12.html"),
        dict(label="Planck 2013 results. XIV. Zodiacal emission, A&A 571:A14 — emissivities fitted "
                   "for the diffuse cloud, bands, circumsolar ring and Earth-trailing feature; the "
                   "zodiacal correction to the CMB maps small compared with the CMB temperature "
                   "power spectrum",
             url="https://arxiv.org/abs/1303.5074"),
        dict(label="Patel, Aluri & Ralston, “CMB low multipole alignments across data releases”, "
                   "MNRAS 539:542 — the quadrupole–octopole alignment persists across releases, "
                   "while no preferred alignment is found among ℓ = 2–61 collectively",
             url="https://arxiv.org/html/2405.03024v1"),
        dict(label="Keller & Flynn, “Evidence for a significant Kuiper belt dust contribution to "
                   "the zodiacal cloud”, Nature Astronomy 6:731 (2022) — long-exposure-age grains "
                   "spiralling in under Poynting–Robertson drag",
             url="https://www.nature.com/articles/s41550-022-01647-6"),
        dict(label="Sungenis & Bennett, Galileo Was Wrong — complete seventh edition (2013), "
                   "Vols. 1–3; searched in full for zodiacal, Kuiper, gegenschein, Oort and "
                   "“dust ring”",
             url="https://archive.org/details/galileo-was-wrong-the-church-was-right-sungenis-vol-1-3-complete"),
        dict(label="Sungenis & Bennett, Galileo Was Wrong Vol. I — the 2006 scan, searched in full "
                   "for the same terms",
             url="https://archive.org/details/GallileoWasWrong"),
        dict(label="van der Kamp, De Labore Solis (1988) — searched in full for the same terms",
             url="https://geocentricity.com/bibastron/ts_history/de_labore.pdf"),
    ]),
}
