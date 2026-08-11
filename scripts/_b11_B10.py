# -*- coding: utf-8 -*-
"""Batch 11 — B10. "Sun and Moon appear the same size; solar diameter constant."

Three items: 31 "Equal apparent size of Sun and Moon.", 97 "Constant solar
diameter.", 220 "Constant solar diameter." Verdict MISLEADING, kept.

Research notes for whoever picks this up next.

1. THIS IS TWO ARGUMENTS WITH TWO DIFFERENT DOCUMENTED ANCESTORS, AND NEITHER
   ANCESTOR IS THE TEXT OUR RECORD NAMES. The cluster record carries
   originator="Samuel Rowbotham", originator_work="Earth Not a Globe", year="1865".
   What the searches returned:

   (a) EQUAL APPARENT SIZE (item 31) -> THOMAS WINSHIP, *Zetetic Cosmogony*, 2nd ed.
       enl., Durban: T. L. Cullingworth, 1899. Winship derives the SAME 32-mile
       diameter for the Sun (printed pp. 119-120) and for the Moon (printed p. 71)
       from the same sextant procedure, and states the equality with a hedge that
       his own arithmetic then removes: "As to size, the moon is next in importance
       to the sun, if, indeed, she is not quite as large" (p. 71), followed three
       paragraphs later by "it is, by the above process, found to be about 32
       nautical miles in diameter." Do not stop at the "if, indeed" — the flat
       assertion is on the same page.
       The line reaches the later literature twice over: David Wardlaw Scott quotes
       the sun passage in *Terra Firma* (1901), printed pp. 173-174, crediting
       "Zetetic Cosmogony" p. 120; and Dubay's *200 Proofs* #147 (2015) states the
       modern form — equal apparent size, "measured with sextants to be of equal
       size and equal distance" — with #123 carrying the 32-mile figure for both
       bodies.

   (b) CONSTANT SOLAR DIAMETER (items 97, 220) -> WILLIAM CARPENTER, *One Hundred
       Proofs*, Baltimore 1885, proof 89, indexed in his own list as "Luminous
       objects." The constancy sentence in it is a QUOTATION FROM RICHARD A.
       PROCTOR, the astronomer the whole pamphlet is dedicated to ("The Greatest
       Astronomer of the Age"). Carpenter is not reporting a measurement; he is
       neutralising Proctor's objection that on a plane the Sun "should therefore
       look much larger" near the observer.

   NOT LOCATED in Rowbotham's 1865 first book edition (Gutenberg #69892, searched
   for diameter, apparent size, same size, angular, 32 miles, micrometer): the
   equal-size argument is not in that text, and the only constancy statement in it
   is Section 8's quotation of Sir Richard Philips. Rowbotham's own sun-and-moon
   magnitudes there are qualitative ("much smaller than the Earth"), and the 1881
   third edition puts the Moon NEARER than the Sun (ch. V, printed p. 104), which
   is the opposite of the equal-distance premise item 31 needs. Reported in
   record_problems; clusters.py was not edited — this agent owns one file.

2. THE BEST FINDING IN THE CLUSTER IS A UNITS ERROR, AND WINSHIP STATES IT IN HIS
   OWN WORDS. His method (p. 71): "Let the instrument with which the angular
   distance was taken be graduated to degrees, minutes and seconds, the minutes and
   seconds corresponding to miles and sixtieths of miles ON THE EARTH'S SURFACE"
   (emphasis ours) — then he applies that correspondence to an object at an unknown
   range. One minute of arc equals one nautical mile only for arcs subtended at the
   Earth's centre, because that is how the nautical mile was defined.
   OUR ARITHMETIC, reproducible: 1 nmi = 1852 m; 1 arcmin = 2.90888e-4 rad;
   1852 / 2.90888e-4 = 6,366,700 m. The rule silently places every object it is
   applied to at 6,367 km — the Earth's mean radius is 6,371 km. So "32 miles" is
   not a measurement of the Sun. It is the Earth's radius, arriving through the
   definition of the unit. And because the rule assigns the same range to everything
   it touches, it MANUFACTURES the "equal size and equal distance" that Dubay's #147
   reports as a finding.
   It also convicts him internally: he puts the Sun at 2,700 nautical miles
   ("AS CERTAIN AS THAT TWO AND TWO ARE FOUR"), but 2,700 x 0.009308 rad = 25.1 nmi,
   not 32. His two "practical and non-theoretical" numbers disagree by 27%.

3. THE FRAGMENT "CONSTANT SOLAR DIAMETER" IS AMBIGUOUS AND BOTH READINGS LOSE.
   Read as "constant through a day" it is true, and it is what a Sun 150 million km
   away predicts; the flat model cannot deliver it (see 4). Read as "constant
   through a year" it is false: 31'36" at aphelion to 32'42" at perihelion, which is
   3.4% and matches the orbit. The four words are true on the timescale that refutes
   the flat model and false on the timescale where the model would need them. Answer
   both readings; do not pick the convenient one.

4. THE ARITHMETIC THAT KILLS THE SMALL SUN, ON THE SOURCES' OWN NUMBERS. Angular
   size goes as 1/distance. At sunset the sub-solar point is a quarter of the way
   round the world; on Winship's own scale (45 deg of latitude = 2,700 nmi) that is
   at least about 5,400 nmi of ground distance.
     - Rowbotham 1881, sun under 700 statute miles up: sqrt(700^2 + 6215^2) = 6254;
       700/6254 = 0.11. The disc should set at about a ninth of its noon width,
       roughly 3.6' instead of 32'.
     - Winship, sun 2,700 nmi up: sqrt(2700^2 + 5400^2) = 6037; 2700/6037 = 0.45.
       Still a disc a bit under half its noon width, roughly 14'.
   Neither happens. The measured change across a day is the 0.004% that one Earth
   radius of observer displacement buys you.

5. THE TRADITION HOLDS BOTH CLAIMS AND THEY CONTRADICT EACH OTHER. Rowbotham 1865,
   Section 8: the horizon enlargement "is only an optical impression, as proved by
   actual measurement", followed by Philips on the micrometer — the angular measure
   is "identical" at horizon and meridian. Rowbotham 1881, ch. X (printed pp. 128-9,
   sacred-texts za28): the enlargement is real, atmospheric, and "a striking argument
   against the rotundity of the earth". Carpenter 1885 needs constancy. Three
   positions, two authors, one tradition; the list quotes whichever is convenient.
   Use this, but state it as a comparison of two editions and a third author, not as
   "Rowbotham contradicted himself" — the 1865 sentence is a quotation he endorses,
   and the 1881 chapter is a rewrite, so what changed is the book, not a man caught
   out in one paragraph.

6. THE PERSPECTIVE DEFENCE IS THE ONE A GOOD DEFENDER WILL PLAY, AND ROWBOTHAM'S
   OWN CHAPTER IX ANSWERS IT. He explains sunset by "the laws of perspective" and
   illustrates it with the Mont Cenis tunnel, quoting an observer for whom the far
   opening "seemed like a bright star" whose "volume increased" as the horses closed
   the distance (1881 ch. IX, printed p. 127, sacred-texts za27). That is a luminous
   source diminishing with distance, printed one chapter before he needs the Sun not
   to, and two chapters before Carpenter's rule that luminous bodies do not diminish
   at all. Perspective is not a different geometry; a vanishing point is where the
   angular size has fallen below what the eye resolves.

7. THE LIVE QUESTION, AND WHY IT DOES NOT TOUCH THIS. Whether the Sun's PHYSICAL
   diameter varies over the activity cycle is genuinely unresolved: Rozelot,
   Kosovichev & Kilcik, "How big is the Sun: Solar diameter changes over time"
   (arXiv:1804.06930; Sun and Geosphere 13(1):63-68, 2018) — "no consensus was
   reached on this issue". The candidate variations are of order a few km: Antia,
   Basu, Pintar & Pohl (arXiv:astro-ph/0001293) put an f-mode-inferred change at
   "about 5 km from minimum to maximum activity", ~10 milliarcsec against a disc of
   ~1,920". Say this. Do NOT let the page imply the solar-diameter literature is
   closed — that is the E14 precedent, where we had REFUTED over solar oblateness
   while it was open. It is also why the refutation below states the magnitudes
   rather than waving the question away.

8. MEASUREMENT PROVENANCE for the numbers used below. Sun 31'36" (aphelion) to
   32'42" (perihelion) and Moon 29'26" (apogee) to 33'30" (perigee) are from the
   comparison table in Wikipedia's "Solar eclipse"; the Moon's fuller 29.3'-34.1'
   range and the 38 mm/yr recession are from Wikipedia's "Moon". Mean angular
   diameters are ours: 2 x 695,700 / 149,598,000 rad = 31.97' for the Sun and
   2 x 1737.4 / 384,400 = 31.07' for the Moon, i.e. the Moon's mean disc is the
   SMALLER by about 3%, which is why annular eclipses exist at all. Horizontal
   parallaxes are also ours, from the same distances: arcsin(6371/384400) = 56.97'
   for the Moon against arcsin(6371/149,598,000) = 8.8" for the Sun. A percentage
   split of eclipse types was deliberately NOT used: the NASA five-millennium
   statistics page returned 404 at both paths tried, and the one secondary figure
   available ("about 60% of central eclipses are annular") was not run down to a
   primary, so the argument is made from the angular ranges instead.

9. VERDICT. MISLEADING kept, no challenge filed. The equal-size half rests on a
   true observation that is true in every model, so REFUTED would be wrong; the
   constancy half is true on one timescale and false on another, so REFUTED would be
   wrong there too. SELF-CONTRADICTED was weighed on the strength of point 5 and not
   taken: the contradiction is between two editions and two authors and is assembled
   BY US, not conceded in one text the way B05 and B06 concede theirs. What is wrong
   with this cluster is its record, not its verdict.

10. RECORD PROBLEMS, reported up, not edited. (i) originator/originator_work/year
    name Rowbotham 1865 for claims located in Winship 1899 and Carpenter 1885.
    (ii) The cluster is composite — one item with one ancestor, two items with
    another — which is the A09 situation. (iii) The cluster note's "the reason we
    have both total and annular eclipses" credits the Sun's 3.4% swing; the Moon's
    is nearly four times larger and its mean disc is the smaller of the two, so the
    Moon's distance variation is what produces the two eclipse types. That note
    renders beside the verdict chip. (iv) real_source is None for a cluster with a
    perfectly ordinary piece of real astronomy behind it. (v) Minor, for works.py:
    the 1899 preface calls the first edition "an unpretentious pamphlet of 48 pages"
    — a size, still not a date, so the record's "first edition date not established"
    stands and now has a corroborating detail.

11. QUOTE PROVENANCE. Winship read in the Google/archive.org scan, item
    ZeteticCosmogony, file "zetetic cosmogony_djvu.txt"; the OCR reads "tcund" where
    the word is plainly "found", and that is the only silent repair in the quote
    below. Page numbers are the scan's printed-page markers and were not checked
    against a print copy. Carpenter from Gutenberg #55387, which reproduces the
    Baltimore 1885 printing (Chew Street imprint and the Proctor dedication both
    present). Rowbotham 1865 from Gutenberg #69892; Rowbotham 1881 from sacred-texts
    za27/za28/za23. Dubay from the archive.org text of *200 Proofs*, item
    200ProofsEarthIsNotASpinningBall_201903. Proctor's own words were NOT reached:
    neither the sentence Carpenter quotes nor the "English Mechanic" letter of
    20 October 1871 he cites was located in any text searched for this entry, so
    both are treated throughout as Carpenter's report of Proctor and never as
    verified Proctor.
"""

ENTRY = {

"B10": dict(

    tldr=("Two claims here, and the texts located for them are two different books. "
          "“Equal apparent size” is true and undisputed; the work is done by a step the "
          "fragment drops — Winship's 1899 rule that a minute of arc on a sextant is a "
          "nautical mile, which holds only for arcs measured at the Earth's centre and "
          "therefore puts every object it is applied to at one Earth radius. The nearest "
          "statement located for “constant solar diameter” is Carpenter's proof 89 of 1885, "
          "where the words are a quotation from the astronomer he was arguing against. "
          "Measured, the disc holds steady through a day — which a Sun a few thousand miles "
          "up cannot manage — and swings 3.4% through a year, which is the orbit."),

    passage=dict(
        work="WRK-WINSHIP-1899",
        locator=("2nd ed., enl. (Durban: T. L. Cullingworth, 1899). The method and the Moon at "
                 "printed p. 71; the Sun at printed pp. 119–120. Pagination follows the printed-page "
                 "markers in the Google/archive.org scan (item ZeteticCosmogony) and was not checked "
                 "against a print copy. The p. 120 sentence is also quoted, with that page "
                 "attribution, by David Wardlaw Scott, Terra Firma (1901), printed pp. 173–174"),
        pd=True,
        quote=("Size, except in the case of very small stars, may be as easily determined. Let the "
               "instrument with which the angular distance was taken be graduated to degrees, "
               "minutes and seconds, the minutes and seconds corresponding to miles and sixtieths "
               "of miles on the earth's surface. … Instead of the diameter of the moon being 2,160 "
               "miles, as we are informed by the men of science of to-day, it is, by the above "
               "process, found to be about 32 nautical miles in diameter. … If the navigator "
               "neglects to apply the sun's semi-diameter to his observation at sea, he is 16 "
               "nautical miles (nearly) out in calculating the position his ship is in. A minute of "
               "arc on the sextant represents a nautical mile, and if the semi-diameter be 16 miles, "
               "the diameter is of course 32 miles. And as measured by the sextant, the sun's "
               "diameter is 32 minutes of arc, that is 32 nautical miles in diameter. Let him "
               "disprove this who can."),
        gloss=(
            "<p>This is where &ldquo;equal apparent size&rdquo; gets its teeth, and it is worth "
            "seeing what the equality is made of. Winship runs one procedure twice &mdash; sextant "
            "to the lower limb, sextant to the upper limb, difference read off as the diameter "
            "&mdash; and gets 32 nautical miles for the Moon on printed p. 71 and 32 for the Sun on "
            "p. 120. The equality is not observed at the end of the process; it is guaranteed at the "
            "start of it, because the rule he converts by assigns the same range to everything it is "
            "applied to. His own page has the hedge and then removes it: <em>&ldquo;the moon is next "
            "in importance to the sun, if, indeed, she is not quite as large&rdquo;</em>, and three "
            "paragraphs on, the flat figure.</p>"
            "<p><strong>The two items about constancy come from somewhere else.</strong> Carpenter, "
            "<em>One Hundred Proofs</em> (1885), proof 89, indexed by him as &ldquo;Luminous "
            "objects&rdquo;: <em>&ldquo;It is well known that the law regulating the apparent "
            "decrease in the size of objects as we leave them in the distance … is very different "
            "with luminous bodies from what it is in the case of those which are non-luminous. … "
            "Proctor says, in speaking of the Sun: &lsquo;his apparent size does not change,&rsquo; "
            "&mdash;far off or near.&rdquo;</em> The pamphlet is dedicated to Richard A. Proctor, "
            "&ldquo;The Greatest Astronomer of the Age&rdquo;, and the sentence about constancy is "
            "Proctor&rsquo;s, quoted inside a rebuttal of Proctor&rsquo;s objection that a traveller going far enough south "
            "would, on a plane, find that the Sun &ldquo;should therefore look much larger&rdquo;. Proctor&rsquo;s "
            "own text was not reached for this entry: neither that sentence nor the "
            "<em>English Mechanic</em> letter of 20 October 1871 that Carpenter cites was located in "
            "any text searched here, so both are reported as Carpenter&rsquo;s report of Proctor.</p>"
            "<p><strong>Where the modern statement of item 31 lives.</strong> Dubay, "
            "<em>200 Proofs</em> (2015), #147: the ball model, he writes, asks us to accept as "
            "coincidence what &ldquo;cannot be explained other than by natural design&rdquo;, the two "
            "bodies having &ldquo;been measured with sextants to be of equal size and equal "
            "distance&rdquo;. The sextant is Winship&rsquo;s, and #123 carries his 32-mile figure for "
            "both bodies. So the chain from the quoted page above to the item on the list is "
            "documented at every link, and the premise doing the work travels the whole way down "
            "it.</p>"),
    ),

    steelman=dict(
        description=(
            "Three real things sit underneath these items, and the easy bust misses all of them. "
            "<strong>First</strong>, Winship is describing a genuine nautical procedure correctly. A "
            "navigator taking a sun sight really does shoot the lower limb and add the "
            "semi-diameter, about 16&prime;, to reach the centre; the tables really do print that "
            "correction; and the sextant really does measure the Sun&rsquo;s angular diameter to "
            "better than an arcminute. He is not making up an instrument. <strong>Second</strong>, "
            "the coincidence in item 31 is real and astronomers say so in their own textbooks: two "
            "bodies whose distances differ by a factor of about 390 subtend almost the same angle, "
            "which is why total solar eclipses look the way they do and why the corona can be seen "
            "with the naked eye at all. Treating that as unremarkable would be "
            "the strawman. <strong>Third</strong>, Carpenter&rsquo;s observation about luminous "
            "objects is a real perceptual effect. A street lamp a mile off does not look "
            "proportionately smaller than one at fifty yards, because an unresolved bright source is "
            "seen as a glare disc whose size is set by scattering in the air and in the eye rather "
            "than by geometry. Anyone who has driven at night knows the phenomenon he is pointing "
            "at."),
        why_it_doesnt_save_claim=(
            "<p>Each of the three is true, and each points the other way.</p>"
            "<p><strong>The sextant measures an angle, and the conversion to miles is the whole "
            "argument.</strong> &ldquo;A minute of arc represents a nautical mile&rdquo; is a "
            "definition about arcs on the Earth&rsquo;s surface &mdash; the nautical mile was fixed "
            "as one minute of latitude. Applied to an object at unknown range it is not a "
            "measurement but an assumption, and the assumption is recoverable: 1852&nbsp;m divided "
            "by one arcminute in radians (2.90888&times;10<sup>&minus;4</sup>) is 6,367&nbsp;km, and "
            "the Earth&rsquo;s mean radius is 6,371&nbsp;km. The rule places every object it touches "
            "at one Earth radius. That is why the Sun and the Moon come out the same size and the "
            "same distance in his hands: the answer was in the unit. His own numbers show the seam "
            "&mdash; he puts the Sun 2,700 nautical miles up, and 2,700 multiplied by 32&prime; in "
            "radians is 25.1 nautical miles, not 32.</p>"
            "<p><strong>The coincidence is real, inexact and temporary, and it is silent about the "
            "Earth.</strong> The Moon&rsquo;s disc runs 29&prime;26&Prime; to 33&prime;30&Prime; and "
            "the Sun&rsquo;s 31&prime;36&Prime; to 32&prime;42&Prime;: the ranges overlap, which is "
            "the coincidence, and the Moon&rsquo;s swing is nearly four times the Sun&rsquo;s, which "
            "is not what two objects at one distance do. The Moon recedes 38&nbsp;mm a year, so the "
            "match is a phase we are living through rather than a fact about the world. And "
            "whichever way it is read, it is a claim about the ratio of two objects in the sky, from "
            "which nothing about the shape or the motion of the ground follows.</p>"
            "<p><strong>The glare effect is a reason to change instrument, not a law of "
            "nature.</strong> It is exactly because a bright source resists visual shrinking that "
            "the naked eye is the wrong tool and a filtered disc measured against a graticule is the "
            "right one &mdash; a point the tradition&rsquo;s founding text concedes, since "
            "Rowbotham&rsquo;s 1865 Section 8 settles the horizon question by appeal to the "
            "micrometer. Once the glare is removed there is a number, and the number is the one "
            "reported below.</p>"),
    ),

    refutation=(
        "<p>Two claims travel in this cluster and they need separating, because they come from "
        "different books and fail in different ways.</p>"

        "<h4>1. The two discs really are close to equal. That is the observation, and it is not in "
        "dispute.</h4>"
        "<p>The Sun&rsquo;s apparent diameter runs from 31&prime;36&Prime; near 4 July to "
        "32&prime;42&Prime; near 3 January; the Moon&rsquo;s from 29&prime;26&Prime; at apogee to "
        "33&prime;30&Prime; at perigee. Mean values, computed from the standard sizes and distances "
        "&mdash; 2&times;695,700&nbsp;km over 149,598,000&nbsp;km, and 2&times;1,737.4&nbsp;km over "
        "384,400&nbsp;km &mdash; are 31.97&prime; for the Sun and 31.07&prime; for the Moon. So the "
        "Moon&rsquo;s disc is on average the <em>smaller</em> of the two, by about 3%. That is not a "
        "quibble: it is why a central eclipse sometimes leaves a ring of photosphere all the way "
        "round, which is a direct visual demonstration that the two discs are not the same size. The "
        "equality is an overlap of two ranges, not an identity.</p>"
        "<p>It is also passing. The Moon recedes about 38&nbsp;mm a year, and published estimates "
        "of when it will stop being able to cover the Sun range between 650 million and 1.4 billion "
        "years from now. A coincidence with an expiry date is a poor foundation for a "
        "cosmology.</p>"

        "<h4>2. The step the item drops is where the argument lives, and it is a units error.</h4>"
        "<p>Nobody disagrees that the two look about the same size, so &ldquo;equal apparent "
        "size&rdquo; on its own settles nothing about the shape or the motion of the Earth. The "
        "source knows this, which is why "
        "the source says more: Winship&rsquo;s sextant procedure turns the angle into miles, and "
        "Dubay&rsquo;s #147 reports the output as the two bodies having been &ldquo;measured with "
        "sextants to be of equal size and equal distance&rdquo;. That conversion is the argument, "
        "and it does not work. One minute of arc corresponds to one nautical mile because the "
        "nautical mile was <em>defined</em> as a minute of latitude on the Earth&rsquo;s surface; the "
        "correspondence holds for arcs subtended at the Earth&rsquo;s centre and for nothing else. "
        "Applied to a body at unknown range it fixes that range: 1852&nbsp;m divided by "
        "2.90888&times;10<sup>&minus;4</sup>&nbsp;rad is 6,367&nbsp;km, against an Earth radius of "
        "6,371&nbsp;km. Every object measured this way comes back the same size and the same "
        "distance because the unit put it there. The &ldquo;equal distance&rdquo; is not a finding; "
        "it is the arithmetic reporting its own assumption.</p>"
        "<p>The two distances are, in fact, separately measured, and they are not equal. Take the "
        "cheapest observation: the Moon shows a large daily parallax and the Sun does not. From the "
        "same distances above, the horizontal parallax is arcsin(6371/384,400) = 56.97&prime; for "
        "the Moon and arcsin(6371/149,598,000) = 8.8&Prime; for the Sun &mdash; a factor of about "
        "390, the same factor as the distance ratio. Widely separated observers see the Moon "
        "displaced against the star field, at the same instant, by tens of arcminutes &mdash; a "
        "shift of the order of its own apparent width &mdash; where the Sun&rsquo;s displacement is "
        "under nine arcseconds. That is a measurement of the difference in distance, made with the "
        "same class of instrument Winship trusts.</p>"

        "<h4>3. &ldquo;Constant solar diameter&rdquo; is Proctor&rsquo;s sentence, borrowed.</h4>"
        "<p>Carpenter&rsquo;s proof 89 does not report a measurement of the Sun. It asserts a "
        "perceptual law &mdash; that luminous bodies do not shrink with distance the way ordinary "
        "objects do &mdash; and then quotes Proctor saying the Sun&rsquo;s apparent size does not "
        "change, in order to argue that Proctor&rsquo;s own objection to a flat Earth is therefore "
        "&ldquo;a counterfeit&mdash;a fraud&mdash;no valid objection at all&rdquo;. The move is "
        "defensive: it is offered to show that the constancy cannot be used against a plane. On the "
        "list it becomes an item of evidence in its own right.</p>"
        "<p>And the perceptual law is a reason to reach for an instrument, which is precisely what "
        "the tradition&rsquo;s founding text does. Rowbotham&rsquo;s 1865 Section 8 disposes of the "
        "enlarged horizon Sun by quoting Sir Richard Philips: take the angle &ldquo;either with a "
        "tube or micrometer&rdquo; and &ldquo;the measure is identical&rdquo; at the horizon and at "
        "the meridian. So the movement&rsquo;s first book concedes both the instrument and the "
        "result. Filter the glare, measure the disc, and there is a number.</p>"

        "<h4>4. The number destroys the near Sun, on the sources&rsquo; own figures.</h4>"
        "<p>Angular size falls as one over distance. When the Sun sets for an observer it is "
        "vertically over a point a quarter of the way around the world; on Winship&rsquo;s own scale "
        "&mdash; 45&deg; of latitude equals 2,700 nautical miles &mdash; that is a ground distance "
        "of at least about 5,400 nautical miles. Put his Sun 2,700 nautical miles up and its setting "
        "distance is &radic;(2700&sup2;+5400&sup2;) = 6,037, so the disc should set at 0.45 of its "
        "noon width, near 14&prime; instead of 32&prime;. Put Rowbotham&rsquo;s 1881 Sun &ldquo;less "
        "than 700 statute miles&rdquo; up (ch. V, printed p. 104) and it is worse: the ratio is "
        "0.11 &mdash; a setting disc some 3.6&prime; across, roughly a ninth of the noon Sun and a ninth "
        "of the full Moon. Nothing of the kind is seen. The setting Sun "
        "measures the same width as the noon Sun to well within a percent, which is what a body 150 "
        "million kilometres away predicts: the observer&rsquo;s own displacement of one Earth radius "
        "changes the distance by 0.004%.</p>"
        "<p>Refraction does alter the low Sun, and in the wrong direction for the argument. It lifts "
        "the lower limb more than the upper, squashing the disc vertically into the familiar oval, "
        "while leaving the horizontal width essentially untouched. So the horizontal measurement is "
        "the clean one, and it is flat all day.</p>"

        "<h4>5. Through a year the diameter is not constant, and the variation matches the "
        "orbit.</h4>"
        "<p>31&prime;36&Prime; to 32&prime;42&Prime; is a 3.4% swing, in step with an Earth&ndash;Sun "
        "distance that varies by about the same fraction: the distance is least in early January and "
        "greatest in early July, and the disc is largest and smallest on exactly those dates. That "
        "is what an elliptical orbit requires, and it is a measurement a reader can make &mdash; a "
        "solar filter, a fixed focal length, two photographs six months apart. So the fragment is "
        "false at the one timescale where it would "
        "be doing work against the globe, and true at the timescale where its truth is a problem for "
        "the flat model instead. Both halves of the measurement point the same way.</p>"

        "<h4>6. The tradition carries both claims, which is worth knowing before answering "
        "either.</h4>"
        "<p>Rowbotham&rsquo;s third edition of 1881 rewrites the 1865 section and reverses it. "
        "Chapter X (printed pp. 128&ndash;129) drops the micrometer quotation and argues that the "
        "low Sun is <em>really</em> enlarged by the denser damp air, concluding that &ldquo;the "
        "atmosphere surrounding a globe would not permit of anything like the same degree of "
        "enlargement&rdquo;. Carpenter, four years later, needs the opposite: no change at all. "
        "Both sit in the canon, and measurement is on the side of the 1865 sentence &mdash; the "
        "horizontal disc neither grows nor shrinks through a day &mdash; which leaves the 1881 "
        "chapter contradicted by the very steadiness Carpenter would go on to rely on. "
        "Chapter IX supplies the reason the enlargement reading fails on its own "
        "terms: Rowbotham&rsquo;s illustration of perspective there is the Mont Cenis tunnel, whose "
        "far opening &ldquo;seemed like a bright star&rdquo; and whose &ldquo;volume increased&rdquo; "
        "as the observer approached. A luminous source diminishing with distance, printed one "
        "chapter before the Sun is required not to.</p>"

        "<h4>7. One thing here is genuinely open, and it is not this.</h4>"
        "<p>Whether the Sun&rsquo;s physical diameter changes over the activity cycle is an "
        "unresolved question in the current literature, and this page does not claim otherwise: "
        "Rozelot, Kosovichev &amp; Kilcik (2018) write that despite dedicated space instruments "
        "&ldquo;no consensus was reached on this issue&rdquo;, and helioseismic estimates of the "
        "kind reported by Antia and colleagues put any change at &ldquo;about 5&nbsp;km from minimum "
        "to maximum activity&rdquo; &mdash; roughly ten milliarcseconds on a disc of about "
        "1,920&Prime;. That debate is four orders of magnitude below the annual orbital signal and "
        "five below the change a Sun a few thousand miles up would have to show between noon and "
        "sunset. It settles nothing here in either direction, which is exactly why it is stated "
        "rather than borrowed.</p>"
    ),

    advocate=dict(
        best_defense=(
            "You have refuted an arithmetic, not an observation. Strip Winship out entirely and the "
            "datum survives: the two discs match, and every culture that ever looked up noticed. "
            "Your 400-times-larger-and-400-times-further is an interpretation laid over that datum, "
            "not a rival measurement of it. On constancy you have conceded the point that matters "
            "&mdash; the disc does hold steady from morning to evening &mdash; and then rescued "
            "yourself with a geometry we do not accept. Our account of the setting Sun is "
            "perspective, not recession in a Euclidean box: the vanishing point is where the line of "
            "sight meets the eye-line, and objects approaching it are not simply far away. And note "
            "what you have had to admit in your own last paragraph: the solar-diameter literature is "
            "open, by your own citation. You cannot call an open measurement decisive when it suits "
            "you and open when it does not. Finally, your annual 3.4% is a number produced by the "
            "institutions whose model it confirms."),
        survives=4,
        preemptive=(
            "Strong enough that three answers must be in the body rather than left to the reader, "
            "and all three are above. <strong>(a) The perspective reply is answered from the "
            "source&rsquo;s own chapter, not from ours.</strong> Section 6 of the refutation quotes "
            "Rowbotham&rsquo;s Mont Cenis illustration, in which a luminous opening shrinks to "
            "&ldquo;a bright star&rdquo; with distance and grows on approach &mdash; his own "
            "exposition of perspective has luminous objects diminishing, one chapter before the Sun "
            "is asked not to. A vanishing point is not an alternative geometry; it is the range at "
            "which angular size drops below resolution, which is the same 1/distance law stated "
            "backwards. <strong>(b) The &ldquo;institutions produced the number&rdquo; move is cut "
            "off by reproducibility.</strong> Section 5 gives the amateur protocol explicitly "
            "&mdash; solar filter, fixed focal length, two frames six months apart &mdash; because "
            "the 3.4% is a measurement a reader can make, not a figure to be taken on authority; and "
            "the annular eclipse in section 1 is the same fact visible without instruments. "
            "<strong>(c) The open-question jab is pre-empted by stating the magnitudes.</strong> "
            "Section 7 does not merely concede that the solar-diameter debate is live; it gives its "
            "size, a few kilometres in 696,000, and shows it is four orders of magnitude below the "
            "orbital signal the argument would have to overturn. Cross-link "
            "<a href=\"#ARG-E14\">ARG-E14</a>, where the same care about an unresolved solar "
            "measurement is the reason that cluster&rsquo;s verdict was challenged."),
    ),

    straw_man=dict(
        identified=True,
        detail=(
            "Carpenter's proof 89 answers a quantitative objection by impugning the man who made "
            "it. Proctor's point, as Carpenter himself relays it, is that a traveller going far "
            "enough south that the North Star sits on the horizon should — if the Earth were a "
            "plane — find that “the Sun should therefore look much larger”. That is an ordinary "
            "consequence of the model and the right question to ask of it. Carpenter does not "
            "answer it with a measurement. He calls it “common scientific trickery”, then “a "
            "counterfeit—a fraud—no valid objection at all”, and concludes that a system harbouring "
            "such things “is a rotten system”. The objection was arithmetic and the reply was about "
            "character. Two smaller versions travel with it: Winship converts a units error into an "
            "unanswerable challenge — “We challenge the whole scientific world to disprove this "
            "statement” — and Dubay's #147 says the ball model “asks us to accept as coincidence” "
            "the matching discs, when the position he is describing is not a request but a dated, "
            "measured claim that includes the rate at which the coincidence is ending."),
    ),

    compression=dict(
        assessed=True, drifted=True,
        list_phrasing=("Equal apparent size of Sun and Moon. / Constant solar diameter. / "
                       "Constant solar diameter."),
        source_wording=("“A minute of arc on the sextant represents a nautical mile, and if the "
                        "semi-diameter be 16 miles, the diameter is of course 32 miles.” (Winship, "
                        "1899, p. 120) · “Proctor says, in speaking of the Sun: ‘his apparent size "
                        "does not change,’—far off or near. And then he forgets the fact!” "
                        "(Carpenter, 1885, proof 89)"),
        drift_type="force_upgraded",
        note=(
            "<p><strong>The two constancy items (97, 220) are the clean case, and the drift is a "
            "borrowed concession.</strong> The sentence they compress belongs to Richard A. Proctor, "
            "an astronomer arguing for a globe, and Carpenter quotes it inside a rebuttal &mdash; his "
            "purpose is to show that the constancy cannot be turned <em>against</em> a plane, which "
            "is why the paragraph ends by calling the objection a counterfeit rather than by "
            "reporting an observation. On the list the same words appear as a positive datum in the "
            "movement&rsquo;s own voice. Nothing was misquoted; the speech act moved, which is the "
            "<a href=\"#ARG-R01\">R01</a> pattern with the roles reversed &mdash; there a "
            "concession by their own author was re-used as a proof, here a sentence conceded by the "
            "other side is.</p>"
            "<p><strong>Item 31 drifts the other way, and the enum has no value for it.</strong> "
            "Winship&rsquo;s claim, and Dubay&rsquo;s after him, is not that the two discs look "
            "alike &mdash; it is that a sextant shows them to be &ldquo;of equal size and equal "
            "distance&rdquo;, 32 nautical miles across apiece. The item keeps only the part nobody "
            "disputes and drops the conversion that turns it into an argument. That is a compression "
            "which makes the claim <em>weaker</em> and simultaneously makes it look unanswerable, "
            "because what is left is a true statement about the sky. The published gap is therefore "
            "not that the list overstated its source but that it removed the source&rsquo;s only "
            "checkable step: a reader meeting &ldquo;equal apparent size of Sun and Moon&rdquo; is "
            "never shown the minute-of-arc-equals-a-nautical-mile rule and so never gets to notice "
            "that it hides an Earth radius. The refutation above answers the sources at full "
            "strength &mdash; the sextant derivation and Carpenter&rsquo;s luminous-object law "
            "&mdash; and not the fragments.</p>"
            "<p><strong>A third gap, in the fragment itself.</strong> &ldquo;Constant solar "
            "diameter&rdquo; names no interval, and the two readings have opposite truth values: "
            "constant through a day, not constant through a year. The annual variation is nowhere "
            "at issue in proof 89 as quoted above, so the annual reading is one the list makes "
            "available and neither of the texts quoted here supplies.</p>"),
    ),

    verdict_challenge=dict(challenged=False, proposed_verdict=None, reasoning=None),

    people=["PER-WINSHIP", "PER-CARPENTER", "PER-DUBAY", "PER-ROWBOTHAM"],
    related=["B02", "B04", "B07", "D13", "D19", "E14"],

    sources=[
        dict(label="Winship (as “Rectangle”), Zetetic Cosmogony, 2nd ed. enl. (Durban, 1899) — "
                   "archive.org scan; the sextant method and the Moon at printed p. 71, the Sun at "
                   "pp. 119–120, and the Sun's distance “as certain as that two and two are four”",
             url="https://archive.org/download/ZeteticCosmogony/zetetic%20cosmogony_djvu.txt"),
        dict(label="Scott, Terra Firma (1901), printed pp. 173–174 — quotes the Winship sextant "
                   "passage and cites Zetetic Cosmogony p. 120, with Scott's own hedge that he does "
                   "“not feel competent to decide” the Sun's exact size",
             url="https://archive.org/download/cu31924031764594/cu31924031764594_djvu.txt"),
        dict(label="Carpenter, One Hundred Proofs that the Earth Is Not a Globe (Baltimore, 1885), "
                   "proof 89, indexed “Luminous objects” — the Proctor quotation and the "
                   "“counterfeit—a fraud” reply; the pamphlet is dedicated to Proctor",
             url="https://www.gutenberg.org/ebooks/55387"),
        dict(label="Rowbotham, Zetetic Astronomy: Earth Not a Globe! (1865 first book edition), "
                   "Section 8 — the horizon enlargement is “only an optical impression, as proved by "
                   "actual measurement”, quoting Sir Richard Philips on the tube or micrometer. "
                   "Searched for diameter, apparent size, same size, angular, 32 miles and "
                   "micrometer: the equal-size argument is not located in this text",
             url="https://www.gutenberg.org/ebooks/69892"),
        dict(label="Rowbotham 1881, 3rd ed., ch. X (printed pp. 128–129) — the reversed position: "
                   "the low Sun is really enlarged, and “the atmosphere surrounding a globe would "
                   "not permit of anything like the same degree of enlargement”",
             url="https://sacred-texts.com/earth/za/za28.htm"),
        dict(label="Rowbotham 1881, 3rd ed., ch. IX (printed p. 127) — sunset by “the laws of "
                   "perspective”, illustrated by the Mont Cenis tunnel whose far opening “seemed "
                   "like a bright star” and whose “volume increased” on approach",
             url="https://sacred-texts.com/earth/za/za27.htm"),
        dict(label="Rowbotham 1881, 3rd ed., ch. V (printed p. 104) — the Sun “considerably less "
                   "than 700 statute miles above the earth”, the Moon nearer than the Sun, and all "
                   "luminaries within 1,000 miles",
             url="https://sacred-texts.com/earth/za/za23.htm"),
        dict(label="Dubay, 200 Proofs Earth Is Not a Spinning Ball (2015) — #147 for the equal "
                   "apparent size and the sextant appeal, #123 for the 32-mile Sun and Moon "
                   "attributed to “Flat-Earthers throughout the ages”",
             url="https://archive.org/download/200ProofsEarthIsNotASpinningBall_201903/200%20Proofs%20Earth%20is%20Not%20a%20Spinning%20Ball%21_djvu.txt"),
        dict(label="Angular diameters used above: Sun 31′36″–32′42″ and Moon 29′26″–33′30″, from "
                   "the comparison table in “Solar eclipse”",
             url="https://en.wikipedia.org/wiki/Solar_eclipse"),
        dict(label="Moon: angular diameter 29.3′–34.1′, mean distance 384,400 km, and recession of "
                   "38 mm per year",
             url="https://en.wikipedia.org/wiki/Moon"),
        dict(label="Rozelot, Kosovichev & Kilcik, “How big is the Sun: Solar diameter changes over "
                   "time”, Sun and Geosphere 13(1):63–68 (2018) — “no consensus was reached on this "
                   "issue”; the solar-diameter question is live and is stated as such",
             url="https://arxiv.org/abs/1804.06930"),
        dict(label="Antia, Basu, Pintar & Pohl, “Solar cycle variation in solar f-mode frequencies "
                   "and radius” — any cycle change is “about 5 km from minimum to maximum activity”, "
                   "roughly ten milliarcseconds on a 1,920″ disc",
             url="https://arxiv.org/abs/astro-ph/0001293"),
    ],
),
}
