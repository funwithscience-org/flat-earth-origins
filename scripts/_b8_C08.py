# -*- coding: utf-8 -*-
"""
ARG-C08 — Liturgy, calendar and eastward orientation as cosmology.  Batch 8.

Items 429, 431, 441, 442, 446, 447.  Verdict NOT DEMONSTRATED (unchallenged).

PROVENANCE — THE FIRST JOB.  The record had originator=None and the cluster was one of
the 28 untraced.  The search was run and it TERMINATED IN A RESULT: no modern author
could be found who argues from liturgy, calendar, orientation or the monastic hours to a
cosmology, and `pre_modern` was CONSIDERED AND REJECTED.  What was searched:

  * The specimen itself (withthesun33.com/about-1, re-fetched 2026-08-09).  It carries no
    citation of any kind, for these items or any others.  Heading reads "435 Pieces of
    Evidence The Earth is Not A Spinning Ball" over 461 numbered lines.
  * Sungenis & Bennett, GALILEO WAS WRONG Vol. I, through the Internet Archive's
    inside-the-book index for item `GallileoWasWrong`: "liturgical" returns 0 hits;
    "calendar" returns 7, all of them the Copernicus biography at scan pp. 49-51 plus one
    bibliography line (Duncan, THE CALENDAR, 1998, p. 1098).  So the movement's largest
    volume treats the ecclesiastical calendar as BIOGRAPHY — the problem that set
    Copernicus to work — and not as evidence.  That is the reverse of this cluster's use.
  * The ecclesiastical volume (archive scan ...Bennett4276 = Vol. II, 7th ed., 2013,
    chs 7-13) COULD NOT BE REACHED: the archive's inside-the-book endpoint returned
    HTTP 403 at the proxy on three attempts.  Recorded as UNCHECKED, never as clear.
  * Two other geocentric compendia, read end to end: scripturecatholic.com "Geocentrism"
    (2017) and trueorthodoxy.org "Geocentrism" (Dormition Skete, 2022, 40+ cited
    sources).  Both argue from scripture, the Fathers and the interferometry experiments.
    Neither runs a liturgical, calendrical, orientational or horological argument.
  * The neighbouring literature, because items 430/440 and 451-460 sit either side of
    these six and descend from Hall, Blavatsky and Eliade, and because "sacred time",
    "sacred calendar" and "orientation" are comparative-religion vocabulary.  Hall's
    solar chapter (SECRET TEACHINGS, "The Sun, A Universal Deity") is sacred-texts sta11;
    the slug was recorded here as sta12 until 2026-08-09, and sta12 is a different chapter,
    "The Zodiac and Its Signs".  sta11 was read for Christian festivals, the church
    calendar, eastward orientation and solar processions, and two of the four are in it:
    Hall dates the pagan "birthday of the Solar Man" to 25 December, and, quoting the
    anonymous Balliol treatise MANKIND THEIR ORIGIN AND DESTINY, reads the mid-August feast
    of the Assumption as an astronomical event.  (Hall does not name Dupuis anywhere in
    sta11 — do not credit him; the credit in that chapter is to the Balliol treatise.)
    What is NOT located in the text of that chapter as transcribed at sta11 is any
    conclusion about the motion or arrangement of the Earth, and nothing on church
    orientation or the monastic hours is located there either.  So the resemblance stays a
    resemblance: we do NOT claim Hall or Eliade as the source.

WHY NOT `pre_modern`.  The PRACTICES are demonstrably older than the movement —
Tertullian on eastward prayer c. 197, Gregory of Tours' star manual in the sixth century,
Bede's computus in 725.  But `pre_modern` is a state about where the ARGUMENT came from,
not where the practice came from, and the early texts contain the argument's negation:
Tertullian records the solar reading of eastward prayer as an OUTSIDERS' mistake and
answers it.  Setting pre_modern here would have credited antiquity with an inference
antiquity refused.  So: `compression.assessed="no_source"`, `passage=None`.

NO CHANGE IS PROPOSED TO clusters.py.  originator=None is already correct and the basis
line ("Ritual practice keyed to apparent sky motion is not a measurement of the sky") is
accurate.  Reported, not made: nothing in works.py or people.py needs touching either.

VERDICT.  SELF-CONTRADICTED was weighed — the monastic-timekeeping corpus this cluster
recruits is headed by a textbook that teaches a spherical Earth — and rejected, because
"the claim's own source" needs a source, and this cluster has none.  NOT DEMONSTRATED
("asserted, argument never made") is exact.  Left unchallenged.

TRAP AVOIDED, recorded here because it is the kind that survives into print: the
attractive line "the Gregorian reform ran on Copernican-derived numbers" is FALSE.
Lilio used the Alfonsine tables, not Reinhold's Prutenic ones (Christie, "Copernicus and
the calendar", 2014).  The draft sentence was cut before it was written into the page.
"""

ENTRY = {"C08": dict(

    tldr=("Everyone sees the same sunrise, so a rite keyed to it cannot choose between "
          "world-systems — and we went looking for whoever first argued from liturgy to "
          "cosmology and did not find them: the practices are ancient, the inference is not "
          "documented anywhere we could reach. Where the items describe the practice they are "
          "also loose — Easter runs on a reckoned table its own designers knew was drifting "
          "from the sky rather than on an observation, and the earliest churches in Rome were "
          "built facing the other way. The manual that ran monastic timekeeping, Bede's "
          "Reckoning of Time, teaches that the Earth is a sphere set in the middle of the "
          "universe."),

    passage=None,

    untraceable="""<p>There is no original to quote, and this time that is a conclusion rather than a shrug. The specimen carries no citation for these six items &mdash; it carries none for any item &mdash; so the search had to run outward, through the literature the rest of this list demonstrably draws on. Here is exactly what was searched and where it stopped, so that a reader who knows better can correct us.</p>

<p><strong>The movement&rsquo;s largest volume treats the calendar as biography, not as evidence.</strong> The Internet Archive&rsquo;s inside-the-book index for the scan of <em>Galileo Was Wrong</em> Vol.&nbsp;I (item <code>GallileoWasWrong</code>) returns <strong>zero</strong> hits for &ldquo;liturgical&rdquo; and <strong>seven</strong> for &ldquo;calendar&rdquo;. All seven are one passage of Copernicus biography at scan pp.&nbsp;49&ndash;51, plus a bibliography line. The passage reads, in the authors&rsquo; own words, &ldquo;In 1514 Copernicus was asked by Pope Leo X to use his talents to help fix the calendar&rdquo;, and it goes on to quote Copernicus&rsquo;s dedication to Paul&nbsp;III: &ldquo;For not many years ago under Leo X when the Lateran Council was considering the question of reforming the Ecclesiastical Calendar&hellip;&rdquo; That is the ecclesiastical calendar appearing as the <em>problem that set heliocentrism going</em>, which is the opposite of the use this cluster makes of it.</p>

<p><strong>What could not be reached.</strong> The ecclesiastical volume &mdash; the archive scan labelled &hellip;Bennett4276, which is Vol.&nbsp;II of the seventh edition, 2013, chs&nbsp;7&ndash;13 &mdash; has an inside-the-book endpoint that returned HTTP&nbsp;403 at our proxy on three attempts. That volume is therefore <em>unchecked</em>, and nothing below should be read as a statement about its contents.</p>

<p><strong>Two further geocentric compendia, read end to end.</strong> The <em>Geocentrism</em> essay at scripturecatholic.com (2017) and the <em>Geocentrism</em> page at trueorthodoxy.org (Dormition Skete, 2022, forty-odd cited sources) both argue from scripture, from patristic consensus and from the interferometry experiments. Neither builds an argument out of the liturgy, the calendar, the orientation of churches, processions or the monastic hours.</p>

<p><strong>And the literature next door.</strong> These six items sit inside a run of the list &mdash; temple architecture, iconography, the <em>axis mundi</em>, Masonic tracing boards &mdash; whose neighbours descend from Manly&nbsp;P. Hall, Blavatsky and Mircea Eliade, and &ldquo;sacred time&rdquo;, &ldquo;sacred calendar&rdquo; and &ldquo;orientation&rdquo; are that literature&rsquo;s vocabulary rather than the Tychonian movement&rsquo;s. We read Hall&rsquo;s solar chapter &mdash; <em>The Secret Teachings of All Ages</em>, &ldquo;The Sun, A Universal Deity&rdquo; (sacred-texts <code>sta11</code>) &mdash; and it does carry the move item&nbsp;429 makes, in miniature. Hall dates the pagan &ldquo;birthday of the Solar Man&rdquo; to 25&nbsp;December, and, quoting the treatise he credits to an anonymous Master of Arts of Balliol College, Oxford, <em>Mankind Their Origin and Destiny</em>, he reads the mid-August feast of the Assumption as an astronomical event: a phenomenon that &ldquo;gave rise to a festival which still exists&rdquo;. What is <em>not</em> located in the text of that chapter as transcribed at <code>sta11</code> is the step this cluster needs. Hall reads a Christian feast back to a solar cult &mdash; a claim about the genealogy of a religion &mdash; and draws no conclusion whatever about the motion or arrangement of the Earth; church orientation and the monastic hours are not located in that chapter either. So we record the resemblance as a resemblance and stop. We are not claiming Hall or Eliade as an author here.</p>

<p><strong>Why we did not record this as older than the movement.</strong> The tempting move was to file the cluster as pre-modern, since the practices unquestionably are: Tertullian is describing eastward prayer around 197, Gregory of Tours wrote a manual for timing the night office by the stars in the sixth century, Bede&rsquo;s computus is from 725. But that field records where an <em>argument</em> came from, not where a <em>practice</em> came from, and the early texts contain this argument&rsquo;s negation rather than its origin. Tertullian reports the solar reading of eastward prayer as a mistake made by outsiders looking in, and rejects it. Filing the cluster as pre-modern would have credited antiquity with an inference antiquity declined to make.</p>

<p><strong>An honest note on our limits.</strong> <em>No source found</em> means we did not find one, not that none exists. A one-line claim can begin in a broadcast, a comment thread or a caption that leaves nothing to search, and one volume we wanted was behind a 403. A reader who can point us at someone who actually argued this &mdash; in print, on air, anywhere datable &mdash; will improve this entry, and we will publish the correction.</p>""",

    steelman=dict(
        description="""<p><strong>SURFACE (weak &mdash; do not use).</strong> &ldquo;They think a ritual is a measurement.&rdquo; It is the line that writes itself and it beats nobody, because none of the six items says that. They say the liturgy is keyed to the sky, which is true, and they leave the inference to the reader. Attacking a sentence the list did not write is the failure this project exists to catch.</p>

<p><strong>DEEPER.</strong> Read as a cumulative case, the six are testimony rather than measurement: pre-Copernican Christendom really did organise its buildings, its clock and its year around a sun and moon that move over a stationary Earth, and it did so without embarrassment, in its most public and most conservative institutions. That is simply true, and any answer that flinches from it is dishonest. The Divine Office is timed by sunrise and sunset. Easter is set by an equinox and a full moon. Churches were built to face the sunrise. Nobody was pretending otherwise.</p>

<p><strong>KERNEL.</strong> The strongest version is not testimony at all but a quantitative point, and it is a good one. <em>Geocentric astronomy produced a calendar that works.</em> The 1582 reform&rsquo;s model came from Aloysius Lilius and was executed by Christopher Clavius, a convinced geocentrist, and the year length it locked in &mdash; 365.2425 days &mdash; came out of the Alfonsine tradition, whose tropical year of 365.2425463 days is startlingly close to it. Set against the modern tropical year of about 365.2422 days, the Gregorian mean year runs long by roughly 26 seconds, which is a day in something like 3,300 years. A Ptolemaic framework, with the Earth fixed, delivered a prediction that has held for four and a half centuries and is still what your phone runs on. Anyone who wants to say that geocentric astronomy was useless has to explain that.</p>""",
        why_it_doesnt_save_claim="""<p>Because the quantity that made it work is the one quantity the two systems agree on. A calendar needs recurrence intervals &mdash; the tropical year, the synodic month, the 19-year cycle that ties 235 lunations to 19 years &mdash; and those are periods of <em>relative</em> motion between the Earth, sun and moon. They have identical values whichever body you nail to the origin. That is precisely why a geocentric table could deliver them, and it is why delivering them discriminates nothing. Run the same inference on the rest of the Alfonsine apparatus and you have proved crystalline spheres and epicycles, which the defender does not want either.</p>

<p>And the reform&rsquo;s own occasion cuts the other way. The ten days deleted in October&nbsp;1582 were deleted because the ecclesiastical equinox, fixed at 21&nbsp;March, had drifted from the observed one. The Church corrected the calendar <em>towards</em> the sky. A scheme that has to be dragged back into line with observation is downstream of the observation, not evidence about it &mdash; and, by Copernicus&rsquo;s own account in the dedication to Paul&nbsp;III, that same unresolved Lateran problem is what set him to the more precise study that became <em>De revolutionibus</em>. The compression here is severe: the strongest form of the claim wins the point that geocentric astronomy was empirically competent, which every historian of astronomy already grants, and it wins nothing about the arrangement of the solar system.</p>""",),

    refutation="""<p><strong>1. What is missing is the argument.</strong> Six statements about religious practice are made and nothing is derived from them. Set them out and the gap is visible: <em>the liturgical calendar is solar</em>; <em>churches face east</em>; <em>processions are keyed to sun and moon</em>; <em>sacred calendars are anchored to Earth-based observation</em>; <em>eastward orientation assumes the sun&rsquo;s path</em>; <em>monastic timekeeping runs on geocentric sky cycles</em>. Every one of them is a claim about what people did. To reach a claim about what the world is like you need a further premise &mdash; roughly, <em>a rite keyed to an appearance encodes a commitment about what causes the appearance</em> &mdash; and that premise is neither stated nor defended anywhere in the specimen. It is also the premise the tradition itself denies, which is the subject of the next section. This is why the verdict is <em>not demonstrated</em> rather than <em>refuted</em>: there is no argument here to be wrong.</p>

<p>The structural answer is one sentence long. The apparent motion of the sun is common ground. It is what a rotating Earth predicts, what a rotating sky predicts, and what anyone standing outside at dawn sees. A practice built on an appearance that every model reproduces cannot select between the models. That holds however ancient, however widespread and however beautiful the practice is, and this page takes no position at all on whether facing east in prayer is right, or on the reasons the tradition gives for it. Those are not our business. What people did is checkable; what it proves about the shape of the world is the only thing in dispute.</p>

<p><strong>2. The inference is not new, and its oldest recorded appearance is as a mistake being corrected.</strong> Around 197, Tertullian wrote that outsiders &ldquo;believe that the sun is our god&rdquo;, and identified the reason exactly: &ldquo;The idea no doubt has originated from our being known to turn to the east in prayer.&rdquo; He is describing item&nbsp;446 &mdash; <em>liturgical eastward orientation assumes the sun&rsquo;s path</em> &mdash; being made by his contemporaries as an inference about Christian belief, and he rejects it. The reasons the tradition gave for the practice are theological throughout: the <em>Catholic Encyclopedia</em>&rsquo;s survey of the sources has Gregory of Nyssa explaining that &ldquo;the Orient contained man&rsquo;s original home, the earthly paradise&rdquo;, and Aquinas adding that &ldquo;Our Lord lived His earthly life in the East, and that from the East He shall come&rdquo;. Paradise, the Incarnation, the Second Coming. Whether those reasons are true is outside this review&rsquo;s scope and we express no view; the narrow, checkable point is that none of them is a claim about the sun&rsquo;s path, and the earliest datable person to read the practice as solar was an outsider who was told he had misread it.</p>

<p><strong>3. The east that is not east.</strong> If the orientation encoded a cosmology it would be precise, universal and stable. It is none of the three. Liturgical east is a convention explicitly detached from the compass: the standard description is that &ldquo;churches are always described as though the end with the main altar is at the east, whatever the reality&rdquo; &mdash; the same convention <a href="#ARG-D07">ARG-D07</a> uses to make the same point about symbolic direction. The reality is often something else. Rome reversed it: the earliest Christian churches there &ldquo;were all built with the entrance on the opposite side: to the east, like the Jewish temple in Jerusalem&rdquo;, a pattern that held into the eighth or ninth century and still stands in the great basilicas, whose apses face west. And where the orientations have actually been surveyed the encoding evaporates. A 2006 survey of English churches found &ldquo;practically no relationship with the feast days&rdquo;; a survey of 32 medieval churches in Lower Austria and northern Germany found only a few aligned to the patronal feast &ldquo;with no general trend&rdquo;; one further study got the saint&rsquo;s-day hypothesis to cover 43% of cases. The summary judgement is that as a body these churches &ldquo;can only be said to have been oriented approximately but not exactly to the geographical east&rdquo;. Approximate, local, sometimes reversed in the capital of the tradition: that is a builders&rsquo; convention responding to terrain, precedent and the plot they were given.</p>

<p><strong>4. The calendar is a table, and the people who built it said so.</strong> Item&nbsp;442 &mdash; <em>sacred calendars anchored to Earth-based observations</em> &mdash; states the reverse of the practice it invokes. The Easter computus is deliberately <em>not</em> observational. The equinox is fixed at 21&nbsp;March by decree whatever the sky does, and the moon used is a reckoned moon, tied to the Julian year through the 19-year cycle. The designers knew the approximation was drifting and recorded it: Bede noted the equinoctial drift in 725, the reckoned moon accumulates about a day of error every 310 years and was some four days out of step with the real moon by the sixteenth century, and the ecclesiastical full moon still drifts from the true one by more than three days per millennium. This is the opposite of anchoring to observation. It is a cycle, chosen for computability so that any monastery could find Easter without an astronomer, and its entire documented history is of the sky refusing to keep to it &mdash; culminating in the deletion of ten days in 1582 to put 21&nbsp;March back where the observation was. Item&nbsp;429 is loose in a smaller way: the liturgical year is luni-solar, not solar, because Easter and everything hanging off it are set by a full moon.</p>

<p><strong>5. The consensus is conceded, and it is scored once, next door.</strong> Yes: before Copernicus, educated Christendom held the Earth to be at rest at the centre, and its calendar, its architecture and its hours were built accordingly. We concede that without qualification, and a defender is entitled to insist on it. But two things follow that the cluster cannot afford. First, that claim is <a href="#ARG-C07">ARG-C07</a>&rsquo;s &mdash; patristic and church-tradition affirmation &mdash; and it is already scored there. These six items add no argument to it; they add six lines to a total. That is the mechanism this whole review is about, and here it is operating in the open: 461 items, six of them spent restating a claim the list has already made in another lane. Second, a consensus is a count of people, not a measurement, and this particular consensus is not the one the list needs. It was geocentric <em>and</em> spherical, which is why half of it argues against the other half of the specimen.</p>

<p><strong>6. Monastic timekeeping recruits a textbook that teaches a globe.</strong> Item&nbsp;447 is the one that can be followed to a specific document, and the document answers it. The standard manual of the monastic computus is Bede&rsquo;s <em>The Reckoning of Time</em>, written in 725 &mdash; the work that taught the medieval West how to find Easter and how to divide the year. In the course of explaining precisely the phenomenon monastic timekeeping had to cope with, the changing length of daylight through the seasons, Bede writes that the Earth &ldquo;is, in fact, a sphere set in the middle of the whole universe. It is not merely circular like a shield [or] spread out like a wheel, but resembles more a ball, being equally round in all directions&rdquo; (trans. Faith Wallis, 1999, p.&nbsp;91). The sky cycles item&nbsp;447 points at are in that book, and so is the globe. A list whose other lanes argue for a flat Earth cannot cite the monastic hours as a witness without calling the witness who says the Earth is a ball.</p>

<p>The practice itself was frankly practical. Gregory of Tours wrote a sixth-century handbook for the night office whose own title announces the job &mdash; <em>De cursu stellarum, ratio qualiter ad officium implendum debeat observari</em>, the method of observation by which the office is to be fulfilled &mdash; and Stephen McCluskey&rsquo;s study of it in <em>Isis</em> is titled, exactly, &ldquo;Gregory of Tours, Monastic Timekeeping, and Early Christian Attitudes to Astronomy&rdquo;. Monks watched which constellations had risen and rang the bell. That is a technique for knowing the hour at night without a clock. It commits its user to no cosmology whatever, which is why it worked equally well for Gregory, for Bede with his globe, and for a modern observer with an ephemeris.</p>

<p><strong>7. What would have counted.</strong> Every observation available to a sixth-century monk &mdash; the sun rising in the east, the stars wheeling overhead, the moon returning to the same phase every 29 and a half days &mdash; is reproduced identically by both models, which is why fourteen centuries of careful liturgical observation did not settle the question and could not have. The measurements that do discriminate needed instruments nobody had: stellar aberration in 1729, parallax in 1838, the ring-laser gyroscopes that now read the Earth&rsquo;s rotation to better than a part in 10<sup>9</sup>. Those are the arguments the list has to win, and it argues them in lane&nbsp;A. Six items about the liturgy neither help nor hurt them. They are, in the end, an accurate description of how a civilisation kept time, offered as though describing the clock told you about the sky.</p>""",

    advocate=dict(
        best_defense=(
            "You have refuted nothing, because you have answered a claim nobody made. Nobody "
            "says the Divine Office is an experiment. The six items are testimony, and "
            "testimony is a legitimate form of evidence: they record that the entire "
            "institutional apparatus of Western civilisation — its architecture, its clock, "
            "its year — was designed, over fifteen centuries, by people who took a stationary "
            "Earth under a moving sky as simple fact, and who were not fools. Your own "
            "concession in §5 gives the case away. And your best material argues our side. "
            "Tertullian confirms that everyone could see the practice was keyed to the "
            "sunrise; that outsiders drew a further conclusion he disliked does not unkey it. "
            "Your Bede passage concedes that the monastic computus is geocentric, which is "
            "what item 447 claims — sphericity is a separate question, and the C lane has "
            "never been the flat-Earth lane. Meanwhile you admit the Church built, on "
            "geocentric mathematics, a calendar accurate to a day in three millennia. If a "
            "framework predicts that well for that long, the burden is not on us."),
        survives=3,
        preemptive=(
            "Rated 3 because the cumulative-testimony reading is the version a competent "
            "defender will actually run, and a rebuttal that only says 'a ritual is not a "
            "measurement' loses to it in public. The concrete change is §5 of the refutation, "
            "which was written into the body specifically to meet this defence rather than "
            "left to the reader: it concedes the pre-Copernican consensus outright and without "
            "qualification, then makes the two moves the concession forces — the claim is "
            "ARG-C07's and is already scored there, so these six items add volume and no "
            "argument; and the consensus conceded is geocentric AND spherical, so it cannot be "
            "spent on the specimen's flat-Earth lanes. §6 does the same work on item 447 with "
            "a named text rather than a generalisation, and it deliberately does not claim "
            "that Bede's sphericity refutes geocentrism, only that it refutes recruiting the "
            "monastic corpus for a flat Earth. Two further guards for whoever revises this. "
            "First, do not answer the calendar point by saying the Gregorian reform used "
            "Copernican numbers — it did not; Lilio worked from the Alfonsine tables, not "
            "Reinhold's Prutenic ones, and that attractive sentence was cut in draft rather "
            "than published. Second, do not let §2 harden into 'the eastward turn has nothing "
            "to do with the sun'. It plainly has: east is defined by sunrise. The claim that "
            "survives contact is narrower and is the one made — the direction is common "
            "ground between all cosmologies, and the reasons the tradition recorded for facing "
            "it are theological, which the page reports without endorsing or disputing them."),),

    straw_man=dict(
        identified=True,
        detail=("The framing of item 447 — monastic timekeeping by “geocentric sky cycles”, "
                "offered as though it were a difficulty — implies that the moving-Earth account "
                "must deny that the sky appears to turn. It does not, and never has: the "
                "apparent diurnal motion is a prediction of the rotating-Earth model, computed "
                "to arcsecond precision in every ephemeris. The same goes for “sacred calendars "
                "anchored to Earth-based observations”, which describes ordinary positional "
                "astronomy — measurements are made from where the observer is standing — as if "
                "it were a concession extracted from the other side. Both items assume an "
                "opponent who disputes the appearances. No such opponent exists."),),

    compression=dict(
        assessed="no_source", drifted=None, list_phrasing=None, source_wording=None,
        drift_type=None,
        note=("There is no original to hold these six lines against, and the search that "
              "established it is set out in full under &ldquo;No original to quote&rdquo; above: "
              "the specimen cites nothing; the inside-the-book index for the scan of "
              "<em>Galileo Was Wrong</em> Vol.&nbsp;I returns no hits for &ldquo;liturgical&rdquo; "
              "and seven for &ldquo;calendar&rdquo;, all of them Copernicus biography at scan "
              "pp.&nbsp;49&ndash;51; two further geocentric compendia argue from scripture, the "
              "Fathers and the interferometry experiments instead; and the volume most likely to "
              "carry an ecclesiastical argument &mdash; the &hellip;Bennett4276 scan, Vol.&nbsp;II "
              "of the seventh edition &mdash; could not be reached, so it stands unchecked rather "
              "than clear. <strong>The hedge rule has nothing to bite on here, and that is itself "
              "the result.</strong> Where an argument has an author we can show the list "
              "hardening a hedge; here there is no hedge, because there is no sentence upstream "
              "of the fragment. This is the part of the list that grew by theme rather than by "
              "citation &mdash; six lines of accurate cultural description, filed as evidence, "
              "with the inferential step never taken by anyone we could name. We considered "
              "recording the cluster as older than the movement, since the practices plainly are, "
              "and rejected it: the ancient texts contain the argument&rsquo;s negation rather "
              "than its origin, and crediting antiquity with an inference antiquity declined to "
              "make would have been the same error in a new field."),),

    verdict_challenge=dict(challenged=False, proposed_verdict=None, reasoning=None),

    people=[],
    related=["C01", "C02", "C07", "C09", "D04", "D07", "D08"],

    sources=[
        dict(label="The specimen list — withthesun33.com/about-1 (Andy J. Consoli), items 429, "
                   "431, 441, 442, 446, 447; re-fetched 2026-08-09, no citation attached to any item",
             url="https://withthesun33.com/about-1"),
        dict(label="Sungenis & Bennett, Galileo Was Wrong Vol. I — Internet Archive item "
                   "GallileoWasWrong. Inside-the-book index searched 2026-08-09: “liturgical” 0 "
                   "hits, “calendar” 7 hits (scan pp. 49–51, Copernicus and the Lateran Council; "
                   "p. 1098, bibliography). The Vol. II scan …Bennett4276 could not be reached",
             url="https://archive.org/details/GallileoWasWrong"),
        dict(label="Copernicus, dedication of De revolutionibus to Paul III — “when the Lateran "
                   "Council the question of revising the ecclesiastical calendar was discussed, "
                   "it then remained unsettled”",
             url="https://hti.osu.edu/sites/hti.osu.edu/files/dedication_of_the_revolutions_of_the_heavenly_bodies_to_pope_paul_iii.pdf"),
        dict(label="Thony Christie, “Copernicus and the calendar” (2014) — Lilio used the "
                   "Alfonsine tables, not Copernicus or Reinhold's Prutenic Tables",
             url="https://thonyc.wordpress.com/2014/10/28/copernicus-and-the-calendar/"),
        dict(label="Tertullian, Apology 16 (c. 197) — “The idea no doubt has originated from our "
                   "being known to turn to the east in prayer”",
             url="https://www.newadvent.org/fathers/0301.htm"),
        dict(label="Catholic Encyclopedia (1911), “Orientation of Churches” — Gregory of Nyssa on "
                   "paradise in the east, Aquinas on the Second Coming, and the Roman basilicas "
                   "with apses to the west",
             url="https://www.newadvent.org/cathen/11305a.htm"),
        dict(label="Wikipedia, “Orientation of churches” — the Roman entrance-east pattern, and "
                   "the survey results on patronal-feast alignment (2006 English survey; 32 "
                   "medieval churches in Lower Austria and northern Germany; the 43% study)",
             url="https://en.wikipedia.org/wiki/Orientation_of_churches"),
        dict(label="Wikipedia, “Liturgical east and west” — “churches are always described as "
                   "though the end with the main altar is at the east, whatever the reality”",
             url="https://en.wikipedia.org/wiki/Liturgical_east_and_west"),
        dict(label="Wikipedia, “Computus” — the reckoned moon tied to the 19-year cycle, one day "
                   "of error per 310 years, four days out by the sixteenth century, Bede's note "
                   "of the drift in 725",
             url="https://en.wikipedia.org/wiki/Computus"),
        dict(label="Wikipedia, “Gregorian calendar” — mean year 365.2425 d against a tropical "
                   "year of 365.2422 d; Lilius and Clavius; the Alfonsine value 365.2425463 d; "
                   "the ten-day correction of 1582",
             url="https://en.wikipedia.org/wiki/Gregorian_calendar"),
        dict(label="British Library, “‘The Earth is, in fact, round’” — Bede, The Reckoning of "
                   "Time (725), trans. Faith Wallis 1999, p. 91: “a sphere set in the middle of "
                   "the whole universe … resembles more a ball”",
             url="https://blogs.bl.uk/digitisedmanuscripts/2018/05/the-earth-is-in-fact-round.html"),
        dict(label="Stephen C. McCluskey, “Gregory of Tours, Monastic Timekeeping, and Early "
                   "Christian Attitudes to Astronomy”, Isis 81(1), 1990",
             url="https://www.journals.uchicago.edu/doi/abs/10.1086/355246?journalCode=isis"),
        dict(label="Gregory of Tours, De cursu stellarum, ratio qualiter ad officium implendum "
                   "debeat observari — Haase edition, Internet Archive",
             url="https://archive.org/details/haasedecursu"),
        dict(label="scripturecatholic.com, “Geocentrism” (2017) — searched for a liturgical, "
                   "calendrical or orientational argument; argues from scripture, the Fathers and "
                   "the magisterium instead",
             url="https://www.scripturecatholic.com/geocentrism/"),
        dict(label="trueorthodoxy.org, “Geocentrism” (Dormition Skete, 2022, 40+ cited sources) — "
                   "same search, same result: scripture, patristic consensus and the "
                   "interferometry experiments",
             url="https://www.trueorthodoxy.org/teachings/con_geocentrism.html"),
        dict(label="Manly P. Hall, The Secret Teachings of All Ages (1928), “The Sun, A "
                   "Universal Deity” — sacred-texts sta11 (sta12 is “The Zodiac and Its "
                   "Signs”). Read 2026-08-09 for Christian festivals, the church calendar, "
                   "eastward orientation and processions: the 25 December and Assumption "
                   "passages are there, credited by Hall to an anonymous Master of Arts of "
                   "Balliol College, Oxford, Mankind Their Origin and Destiny; the "
                   "cosmological inference is not located in that chapter",
             url="https://sacred-texts.com/eso/sta/sta11.htm")])}
