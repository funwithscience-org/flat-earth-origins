# -*- coding: utf-8 -*-
"""Batch 10 — D12. "Simplicity / common sense favours a fixed Earth."

Two items, not three: 83 "Simplicity favors geocentrism." and 181 "Simpler moving
sky." (ASSIGN maps only those two to D12; the batch brief said three. Reported up.)
Verdict NOT DEMONSTRATED, kept.

Research notes for whoever picks this up next.

1. THE SOURCE RECORD SURVIVES CONTACT, THE EDITION DOES NOT. clusters.py credits D12 to
   Rowbotham, "Zetetic Astronomy", 1849. The claim really is Rowbotham's and the words
   really are there — but they are in the 1865 BOOK, Section XIV ("General Summary —
   Application — Cui Bono?"), printed pp. 180–181, and again, lightly reworded, in the
   1881 third edition at ch. XV, pp. 352–353. The 16-page 1849 pamphlet
   (WRK-ROWBOTHAM-1849) was not reachable from here, so nothing in this entry rests on
   it and the passage is cited to WRK-ROWBOTHAM-1865. This is the project's documented
   failure mode (README "Known limits"; curmudgeon failure 3) and it is a `clusters.py`
   field, which this file does not own — reported up, NOT applied. Anchor any edit on
   the cluster key: the `originator=` line is byte-identical across B02, B06, B07, D12.

2. THE PASSAGE WAS RETRIEVED TWICE, INDEPENDENTLY, AND AGREES WORD FOR WORD. Project
   Gutenberg #69892 (transcribed from the 1865 Simpkin, Marshall printing) and the
   Google/Internet Archive scan `samuel_rowbotham_-_earth_not_a_globe` (title page:
   Simpkin, Marshall / Bath: S. Hayward, 1865) give the same sentences with the same
   spelling ("immoveable"). The archive scan supplies the printed page numbers.

3. WHAT THE SOURCE ACTUALLY ARGUES, WHICH IS NOT PARSIMONY. Rowbotham's complaint is
   that the rival system's motions are UNEARNED, not that they are numerous: he
   "challenge[s]" his opponents "to produce a single instance of so called proofs of
   these motions which does not involve an assumption". "Simple" appears in his summary
   as one adjective in a list of four — "plain, simple, and in every respect demonstrable
   philosophy ... borne out by every fairly instituted experiment" — and the weight is on
   the last two. He stakes his case on experiments (Bedford Level, B03; his sun-distance
   triangulation, Section III), not on elegance. Hence `scope_widened`: the list detaches
   the adjective and hands it to "geocentrism", a globe-Earth cosmology his own Section
   III argument (all luminaries within 6,000 miles) denies.

4. THE LEDGER, AND COUNT IT SYMMETRICALLY OR NOT AT ALL. An earlier draft counted chapter
   titles and got "six stipulations against two". That does not survive the text. Section 6
   DERIVES day, night and the seasons from Sections 4 and 5 in its own words ("Thus, day and
   night ... arise simply from the Sun's position in relation to the north pole"), so VI is
   his derivation, not his stipulation — concede it. XIII re-applies the perspective law of
   VII in modified form. XII is a miscellanea chapter whose first item is the phases. And
   "a tilted Earth turning as it orbits" is three stipulated inputs, not one: rotation,
   obliquity, revolution. Counted the same way on both sides it is FIVE against THREE
   (plane: IV, V, VII/XIII, a self-luminous half-lit Moon, a semi-transparent occulter;
   globe: rotation, tilt, orbit), and the ratio is not where the weight goes — Section VIII,
   the southern sky and the unseen occulter are unpaid, not merely numerous.

5. THE BEST SINGLE FIND IS SECTION VIII AND IT IS A GIFT. His Section III puts the Sun
   "under 4,000 miles" up; his Section VII has it recede rather than descend at sunset;
   so the disc should shrink by a factor of a few between noon and setting. Section VIII
   then quotes Sir Richard Phillips reporting that measurement gives the SAME angular
   diameter at horizon and meridian, and calls the enlargement "only an optical
   impression, as proved by actual measurement". He publishes the measurement his own
   geometry fails and explains the illusion instead. Do not overstate this: he is
   answering the perceived enlargement, not the constancy. The point is that the
   constancy is the datum, and the "simple" system needs an extra rule for it.

6. THE HISTORICAL INVERSION IS THE HEADLINE, BUT THE TWO TRANSLATIONS DO NOT AGREE ON THE
   ADJECTIVE — DO NOT SAY THEY DO. Ptolemy — the geocentric authority the same list cites
   at items 21 and 23 — grants the rotating-Earth hypothesis the celestial appearances in
   Almagest I.7 and rejects it on TERRESTRIAL physics, not on economy. THAT is what both
   renderings support and it is all the argument needs. They part on where "simpler" hangs:
   the unattributed CCSU text (Taliaferro) has "in accordance with this simpler conjecture",
   attaching it to the rival hypothesis; Toomer — the standard translation, credited at
   MPRL footnote 32 — has "at least from simpler considerations", attaching it to the level
   of argument. An earlier draft called Toomer an independent check that "says the same
   thing"; it does not, on that word. Claim only the concession. Copernicus runs the
   criterion the other way (I.6).

7. THE HONEST CAVEAT THAT KEEPS US OUT OF TROUBLE. "Copernicus was simpler / Ptolemy
   needed ever more epicycles" is a myth. Kuhn's count, quoted in Singham's Physics
   Today piece: "Both employed over thirty circles; there was little to choose between
   them in economy." Say so in the body. A defender who finds we suppressed it has us.

8. THE MOVEMENT'S OWN ASTRONOMER DISOWNED THE ARGUMENT. Bouw, replying to Faulkner on
   geocentricity.com: "Furthermore, simplicity and truth are not related", footnoted to
   Proverbs 1:22. In the same piece he scopes his one use of Occam's razor to the period
   "until 1729" — the year of Bradley's aberration. That is not this cluster's source, so
   it does not make the verdict SELF-CONTRADICTED under the rubric's wording ("the
   claim's own source, or another item on the same list"); it is decisive context and it
   lives in the refutation. Verdict left at NOT DEMONSTRATED, which is exactly right:
   asserted, and the argument that would license it never made.

9. NUMBERS USED, ALL REPRODUCIBLE. Light-cylinder radius for a one-sidereal-day rotation
   of the sky: c·T/2π = 2.998e8 × 86164.1 / 2π = 4.111e12 m = 27.5 AU; Neptune at
   30.07 AU is 1.09c. Solar angular diameter from R=6.957e8 m at 0.98329/1.01671 AU:
   32.5' to 31.4', a 3.4% annual swing. June sun-circle ground-track radius on the
   flat layout: (90−23.4)° × 69.1 mi/deg ≈ 4,600 miles.
"""

ENTRY = {

"D12": dict(

    tldr=("Simplicity is a real criterion — it is Newton's first Rule of Reasoning — but it "
          "decides nothing until someone states a measure and counts under it, and no such "
          "count appears in either of the two summary chapters of Rowbotham searched here. "
          "Made under the measure he invited, the count runs the other way: his own book "
          "stipulates the Sun's daily circuit, the annual change in its path, sunset and the "
          "eclipse apparatus separately, where a tilted Earth turning as it orbits delivers "
          "them from three. Ptolemy had already granted the rotating-Earth account the "
          "appearances of the stars and rejected it on terrestrial physics instead — and the "
          "modern movement's own astronomer wrote that simplicity and truth are not related."),

    passage=dict(
        work="WRK-ROWBOTHAM-1865",
        pd=True,
        locator=("Section XIV, “General Summary — Application — Cui Bono?”, printed pp. 180–181 "
                 "of the 1865 first book edition (Simpkin, Marshall / Bath: S. Hayward). "
                 "Retrieved twice from independent transcriptions — Project Gutenberg #69892 and "
                 "the Google/Internet Archive scan samuel_rowbotham_-_earth_not_a_globe — which "
                 "agree word for word, spelling included. The same passage, lightly reworded, "
                 "appears in the enlarged 1881 third edition at Chapter XV, pp. 352–353."),
        quote=("The Sun and its “system” of revolving bodies are now assumed to have a general "
               "and all-inclusive motion, in common with an endless series of other Suns and "
               "systems, around some other and “central Sun” which has been assumed to be the "
               "true axis and centre of the Universe! These assumed general motions with the "
               "particular and peculiar motions which are assigned to the various bodies in "
               "detail, together constitute a system so confused and complicated that it is "
               "almost impossible and always difficult of comprehension by the most active and "
               "devoted minds. The most simple and direct experiments, however, may be shown to "
               "prove that the Earth has no progressive motion whatever; and here again the "
               "advocates of this interminable and entangling arrangement are challenged to "
               "produce a single instance of so called proofs of these motions which does not "
               "involve an assumption—often a glaring falsehood—but always a point which is not, "
               "or cannot be demonstrated.\n\n"
               "… All these luminaries then, and the Sun itself, being so near to us, cannot be "
               "other than very small as compared with the Earth we inhabit. They are all in "
               "motion over the Earth, which is alone immoveable … This is a plain, simple, and "
               "in every respect demonstrable philosophy, agreeing with the evidence of our "
               "senses, borne out by every fairly instituted experiment, and never requiring a "
               "violation of those principles of investigation which the human mind has ever "
               "recognized, and depended upon in its every day life."),
        gloss="""<p><strong>Read what the adjective is doing.</strong> &ldquo;Simple&rdquo; arrives fourth in a list of four, and the three it travels with are the ones carrying the weight: <em>demonstrable</em>, <em>agreeing with the evidence of our senses</em>, <em>borne out by every fairly instituted experiment</em>. Rowbotham is not offering parsimony as a proof. He is describing a system he believes he has already demonstrated &mdash; by the canal sightings at <a href="#ARG-B03">ARG-B03</a> and by the plane-triangulation of Section III, which puts the Sun &ldquo;under 4,000 miles&rdquo; away and every visible object in the firmament &ldquo;within the distance of 6,000 miles&rdquo; &mdash; and adding that it is also plain. The other half of the passage is not a parsimony claim either. It is an <em>epistemic</em> complaint, and it ends in a challenge rather than a verdict: the rival&rsquo;s motions are objectionable because each one &ldquo;involve[s] an assumption &hellip; a point which is not, or cannot be demonstrated.&rdquo; Numerousness is his symptom; unprovedness is his charge.</p>
<p><strong>Whose system is being called simple.</strong> Rowbotham&rsquo;s is a plane with small luminaries a few thousand miles up. It is not the model item 83 credits with the virtue: <em>geocentrism</em>, in the list&rsquo;s other lineage, is a spherical Earth at the centre of a real Solar System of real planets at real distances &mdash; the thing Section III of this book is written to deny. Both lineages appear on the same 461-item list and both claim the same prize.</p>
<p><strong>The &ldquo;common sense&rdquo; half of the cluster name has a different home.</strong> Neither item scored here uses the phrase; both say <em>simplicity</em>. Where common sense is made to carry a numbered proof on its own is Carpenter 1885, proof 20: &ldquo;The common sense of man tells him&mdash;if nothing else told him&mdash;that there is an &lsquo;up&rsquo; and a &lsquo;down&rsquo; in nature &hellip; and this is a common sense proof that the Earth is not a globe.&rdquo; Carpenter is the distributor who turned Rowbotham&rsquo;s prose into discrete items, and that is the shape the appeal takes once it is in list form.</p>
<p><strong>On the work cited.</strong> Our cluster record for D12 names Rowbotham&rsquo;s 16-page 1849 pamphlet. No copy of that pamphlet was reachable from here, so this treatment quotes and cites only the 1865 book and its 1881 third edition &mdash; the texts that are readable, that carry the sentences, and that downstream compilers work from.</p>"""),

    steelman=dict(
        description="""<p><strong>SURFACE (weak &mdash; do not use).</strong> &ldquo;Simplicity is subjective, so the argument is empty.&rdquo; This loses immediately. Parsimony is not a folk prejudice: it is Newton&rsquo;s own first Rule of Reasoning in the <em>Principia</em> &mdash; nature does nothing in vain, and more causes are in vain when fewer will serve &mdash; and it is formalised today in model selection, where the penalty on free parameters is derived rather than asserted. Anyone who tells a geocentrist that simplicity has no place in science is being lectured back with Newton.</p>
<p><strong>DEEPER.</strong> The argument has a real historical pedigree on the other side too. Copernicus won converts on aesthetic grounds decades before anyone could measure a parallax, and the textbook story that his system was <em>computationally</em> simpler is false &mdash; so for two centuries the parsimony argument in this debate was made by heliocentrists, on premises that were partly wrong. A geocentrist who points that out is not scoring a cheap point.</p>
<p><strong>KERNEL.</strong> The strongest form is Rowbotham&rsquo;s own, and it is not about elegance at all. It is that a theory may not help itself to motions it has not earned, and in 1865 he could point at a live specimen. The passage above objects to &ldquo;some other and &lsquo;central Sun&rsquo; which has been assumed to be the true axis and centre of the Universe&rdquo; &mdash; and that was a real proposal in the astronomy of his day: J. H. von M&auml;dler&rsquo;s Central Sun hypothesis, which placed the centre of the system in the Pleiades. Astronomy dropped it; Wikipedia&rsquo;s biography of him records flatly that &ldquo;he got the location wrong.&rdquo; So when Rowbotham objects that the received picture had the entire system revolving about a centre that had merely been <em>assigned</em>, he is objecting to something real &mdash; M&auml;dler had inferred that centre from stellar proper motions, and the inference did not hold &mdash; and he names the specimen rather than gesturing at one. The general principle behind the complaint &mdash; that the number of things a theory <em>stipulates</em> is a fair thing to count against it &mdash; is the same principle modern cosmologists apply to themselves. Concede all of it.</p>""",
        why_it_doesnt_save_claim="""<p>Because the cure for an unearned premise is a measurement, and Rowbotham knew it, which is why his book is full of experiments rather than appeals to elegance. The central Sun went the way such proposals go when they are tested: it was dropped. Meanwhile the two motions actually at issue had already been caught in the act &mdash; Bradley announced stellar aberration in 1729, Bessel published the parallax of 61 Cygni in 1838, eleven years before the first pamphlet &mdash; and Rowbotham does not ignore either; he argues against them, at <a href="#ARG-A05">ARG-A05</a> and <a href="#ARG-A04">ARG-A04</a>. That is the tell. <strong>Both parties agree the question is settled by measurement.</strong> Once they do, parsimony has nothing left to decide, and an item that puts simplicity forward as a proof is claiming ground its own author was not standing on.</p>
<p>And the count, when someone finally makes it, does not come out his way. It comes out against him in his own chapters &mdash; narrowly, and only once the count is made the same way on both sides &mdash; and against the geocentric branch on a bill it pays in a different currency &mdash; a universe that has to turn, and a mechanism that has to make the turning invisible to a gyroscope. Both are worked below.</p>"""),

    refutation="""<p><strong>First, what would have to be true for this to be an argument.</strong> Parsimony does two jobs in science, and neither is the one asked of it here. It breaks ties between rivals that predict <em>the same observations</em> &mdash; and that job only arises once the rivals have been <em>shown</em> to predict the same observations, which is not free here: what lets a stationary Earth reproduce aberration, parallax and a ring laser is the added machinery counted in the sixth section below, and machinery bought to secure the tie is exactly what a tie-breaker may not help itself to. The second job is that it penalises free parameters in model selection, where the penalty is derived from how badly an over-flexible model predicts new data. Both jobs need a stated measure &mdash; simplicity of what, counted how &mdash; because there is no theory-neutral scale on which a description is simply Simpler. The Stanford Encyclopedia&rsquo;s survey of the problem is a good tour of why. No such measure, and no count under one, is offered in the two summary chapters searched for this entry: Section XIV of the 1865 edition and Chapter XV of the 1881 third edition. What is offered is an adjective.</p>

<p><strong>Second, the ledger, and it is Rowbotham&rsquo;s.</strong> The measure is <em>independently stipulated mechanisms</em>. It is named because it is not the neutral one &mdash; there is no neutral one &mdash; and it is used here because it is the measure this argument itself invites by complaining about &ldquo;assumed general motions&rdquo;. Take five appearances both accounts have to produce: the Sun&rsquo;s daily circuit; the annual change in its path; day and night with the seasons; sunset; and the Moon&rsquo;s phases and eclipses. One of the five is his own derivation and we concede it outright: Section 6 gets day, night and the seasons out of Sections 4 and 5 rather than stipulating them &mdash; &ldquo;Thus, day and night, long and short days, Winter and Summer, the long periods of alternate light and darkness at the pole, arise simply from the Sun&rsquo;s position in relation to the north pole&rdquo; &mdash; which is the same move the globe is making, and he is entitled to it. What is left stipulated on the plane: that the Sun travels a circle over it once in twenty-four hours (IV); that the diameter of that circle changes through the year, with nothing named that sets it (V); that horizontal parallels converge to a finite vanishing point, so that the Sun recedes rather than descends at evening (VII, and again in a modified form at XIII, where the ground rather than the object&rsquo;s centre becomes the datum of convergence); that the Moon is self-luminous with the luminosity &ldquo;confined to one-half its surface&rdquo; (XII, resting on IX); and that a &ldquo;body semi-transparent and well-defined&rdquo; passes in front of her to make a lunar eclipse (IX). Five, and the fifth line is generous, since two properties of the Moon and an extra satellite are three things counted as two. Against that, on the globe: the Earth turns daily, its axis is tilted to the plane of its orbit, and it goes round the Sun once a year. Three. The Moon is a saving to neither side; both accounts have one going round.</p>

<p>Five against three, named on both sides, is a much smaller result than a ledger usually wants to be, and a defender is entitled to say that a metric can be picked to win. So the weight does not go on the ratio. It goes on the fact that some of the plane&rsquo;s five are unpaid rather than merely numerous: nothing in Section V says what varies the diameter of the Sun&rsquo;s path; the semi-transparent body is inferred from two mid-century reports of a suspected second satellite of the Earth and is in no modern ephemeris; the southern sky is not answered at all; and Section VIII, next, prints a measurement the plane&rsquo;s own geometry fails.</p>

<p><strong>Third, what the simple system still owes.</strong> Section III puts the Sun under 4,000 miles up; Section VII has it recede rather than set. Take the June track over the Tropic of Cancer: a ground-track radius of about (90&nbsp;&minus;&nbsp;23.4)&deg; &times; 69.1 miles per degree &asymp; 4,600 miles. An observer under it at noon is 4,000 miles from the Sun; a quarter of a circuit later, when the Sun is setting for him, he is &radic;(6,508&sup2; + 4,000&sup2;) &asymp; 7,640 miles from it, and by the far side of the circle 10,040 miles. That is a factor of 1.9 by sunset and 2.5 by the far side, and a disc 1.9 times farther away subtends 1.9 times less. The measured angular diameter of the Sun does no such thing: it runs from about 32.5&prime; to 31.4&prime; and back over a <em>year</em>, a 3.4% swing set by the Earth&rsquo;s orbital eccentricity, and it does not halve between noon and sunset. Refraction near the horizon flattens the disc vertically by a fraction of its width; it does not shrink it by a factor of two. Rowbotham knew the datum and printed it. Section VIII quotes Sir Richard Phillips: &ldquo;If the angle of the Sun or Moon be taken either with a tube or micrometer when they appear so large to the eye in the horizon, the measure is identical when they are in the meridian&rdquo;, and Rowbotham calls the horizon enlargement &ldquo;only an optical impression, as proved by actual measurement.&rdquo; He is answering why the Sun <em>looks</em> bigger. The question his own geometry raises is why it does not <em>measure</em> smaller, and the section that would have to answer it is spent on an illusion.</p>

<p>Add the sky the plane cannot carry. Observers in Chile, South Africa and Australia see the same circumpolar stars turning about a common southern point, and the Sun stands above the Antarctic horizon for twenty-four hours in December &mdash; the observation Jeran Campanella flew south to make in 2024 and conceded in full. Each of those needs its own rule on a plane. On a globe they are the same rule as everything else.</p>

<p><strong>Fourth, the historical inversion, which is the part worth knowing.</strong> The argument that a moving sky is the economical option is not the ancient geocentric position. It is the position the ancient geocentrist declined to take. Ptolemy, in <em>Almagest</em> I.7, sets out the rotating-Earth hypothesis and writes &mdash; in the English text hosted at CCSU &mdash; that &ldquo;as far as the appearances of the stars are concerned, nothing would perhaps keep things from being in accordance with this simpler conjecture, but that in the light of what happens around us in the air such a notion would seem altogether absurd.&rdquo; Toomer, the standard modern translation, renders the same sentence differently at exactly the word one would most want to lean on: &ldquo;&hellip; although there is perhaps nothing in the celestial phenomena which would count against that hypothesis, at least from simpler considerations, nevertheless from what would occur here on Earth and in the air, one can see that such a notion is quite ridiculous.&rdquo; The CCSU wording hangs <em>simpler</em> on the rival hypothesis; Toomer hangs it on the level of argument. We do not need the stronger reading and do not claim it, because the concession is identical either way and the concession is the whole point: Ptolemy grants the rotating Earth the celestial appearances and rejects it on terrestrial physics &mdash; clouds and projectiles left behind by a turning Earth. The same list cites him by name at item 23, &ldquo;Ptolemaic predictive accuracy&rdquo; (<a href="#ARG-D03">ARG-D03</a>). Copernicus then runs the identical criterion the other way in Book I: &ldquo;we should be even more surprised if such a vast world should wheel completely around during the space of twenty-four hours rather than that its least part, the Earth, should&rdquo; (ch. 6), and cashes it in at ch. 9, where &ldquo;the stoppings, retrogressions, and progressions of the wandering stars are not their own, but are a movement of the Earth&rdquo; &mdash; one motion of the observer retiring a separate mechanism in every planet.</p>

<p><strong>Fifth, and this cuts against us, so it goes in the body.</strong> The familiar story that Ptolemy&rsquo;s system had to be propped up with ever more epicycles until Copernicus swept them away is false. Kuhn&rsquo;s count, as quoted in <em>Physics Today</em>: &ldquo;Both employed over thirty circles; there was little to choose between them in economy.&rdquo; Copernicus won early converts on aesthetics, not on arithmetic. The economy arrives with Kepler, who replaces the whole apparatus of circles with one ellipse per planet, and with Newton, who replaces the ellipses with one law. So the fair statement is that parsimony did not settle this question in 1543 either &mdash; measurement did, over the following three centuries, and 1729 and 1838 are the dates that matter. We are not claiming the elegance prize. We are saying nobody should.</p>

<p><strong>Sixth, the bill the moving sky runs up in the geocentric branch.</strong> Turn the whole sky about the Earth once a sidereal day and the tangential speed passes <em>c</em> at a radius of c&middot;T/2&pi; = 4.11&times;10<sup>12</sup> m, which is 27.5 AU &mdash; inside the Solar System. Neptune, at 30.07 AU, would be moving at 1.09<em>c</em>. The modern answer to this is not to make the model simpler but to buy an entity: a rotating universe, or a physical aether that drags the local inertial frames, so that the sky can turn without anything moving through space &mdash; and then a mechanism precise enough to reproduce, to nine digits, exactly what a spinning Earth would produce in a ring laser bolted to the ground. That is a large purchase, and it is the same purchase this list calls a &ldquo;modern epicycle&rdquo; when cosmologists make it (<a href="#ARG-D14">ARG-D14</a>). The dynamics of the rotating-universe repair are argued at <a href="#ARG-R01">ARG-R01</a> and <a href="#ARG-R05">ARG-R05</a>; what belongs here is only the accounting. A model that needs an added cosmological entity to survive contact with a tabletop instrument is not the economical one.</p>

<p><strong>Seventh, the argument&rsquo;s own side put it down.</strong> Gerardus Bouw, the modern geocentric movement&rsquo;s only credentialed astronomer, answering Danny Faulkner on geocentricity.com, wrote: &ldquo;Furthermore, simplicity and truth are not related&rdquo; &mdash; and footnoted it to Proverbs 1:22. In the same piece his single appeal to Occam&rsquo;s razor is scoped to a period that ended nearly three centuries ago: Faulkner &ldquo;ignores the application of Occam&rsquo;s razor at the point that until 1729, the observational evidence favored the Tychonic model.&rdquo; 1729 is Bradley and aberration. Bouw is not this cluster&rsquo;s source and his sentence does not decide its verdict, but it does tell a reader what kind of argument this is: one that the tradition&rsquo;s own technical wing declines to run, and that survives in the list because a one-line item is cheaper to carry than a caveat.</p>

<p><strong>Verdict: not demonstrated.</strong> Parsimony is asserted here, and the argument that would license it &mdash; a measure, a count under it, and a reason why the simpler description of a set of appearances should be the true account of what is moving &mdash; is not supplied in the chapters searched for this entry. Where a measure is supplied and a count is made, it goes against the claim in both branches: five stipulated mechanisms against three in Rowbotham&rsquo;s own chapters, several of them unpaid, and a bought cosmological entity in the geocentric one. And the conclusion does not rest on that, because the case for the Earth&rsquo;s motion has never rested on elegance. It rests on aberration, on parallax, on the ring laser and on the barycentric correction, and those are measurements, which is the currency both sides of this argument said they wanted to be paid in.</p>""",

    advocate=dict(
        best_defense=(
            "Start with your own first sentence about what parsimony legitimately does. You "
            "grant that it breaks ties between rivals that predict the same observations. That "
            "is precisely our claim about this case — the general-covariance argument at R01 "
            "says the two descriptions are kinematically equivalent — so by your own statement "
            "of the rule you have licensed this use of parsimony and then complained about it. "
            "The burden is now yours to show the rivals are not empirically equivalent, and "
            "until you discharge it you are not entitled to the word “illegitimate”. "
            "Second, you spend one paragraph saying parsimony is not evidence and then five arguing "
            "that our model is the less parsimonious one. You do think it is evidence. You "
            "just want to be holding it. Third, your count is a choice of metric wearing a "
            "lab coat. “Independently stipulated mechanisms” is your measure, chosen "
            "because it wins; count instead the number of bodies you must set in motion, or "
            "the number of things a competent observer must be wrong about, and we win. There "
            "is no neutral scale here — algorithmic complexity is language-dependent and "
            "Goodman showed syntactic simplicity is not projectible — so your ledger is "
            "rhetoric with arithmetic in it. Fourth, you concede that Copernicus was not "
            "simpler and that heliocentrists spent two centuries making a parsimony argument "
            "on false premises. You concede the movement's own astronomer says simplicity and "
            "truth are unrelated — which is our point, not yours: it says nobody wins on "
            "elegance, and you are the one who brought a ledger. Fifth, Rowbotham's actual "
            "challenge is still standing and you have not met it. He asked for one proof of "
            "the Earth's motions that does not involve an assumption. Aberration is a proof "
            "only if you already assume light behaves as your theory says between the star "
            "and the tube; the ring laser is a proof only if you already assume the local "
            "inertial frame is not set by the mass of a turning cosmos. Every item on your "
            "list is a measurement interpreted inside the theory it is offered to support. "
            "That is what he said in 1865 and you have quoted it approvingly without noticing "
            "that it is aimed at you."),
        survives=4,
        preemptive=(
            "Four, and the number is driven by the third and fifth moves. Five concrete "
            "requirements on the text, all met in the version above and none of them optional. "
            "(a) The refutation must OPEN by disclaiming parsimony as evidence and must CLOSE "
            "by saying the conclusion does not rest on the ledger — the first and last "
            "paragraphs are the answer to ‘you did it too’, and if an editor ever "
            "moves the ledger to the front the section becomes indefensible. (b) The measure "
            "must be NAMED where it is used (‘independently stipulated mechanisms’) "
            "and never described as the neutral one; the honest claim is that under the "
            "measure the argument's own author invited — he is the one counting "
            "‘assumed general motions’ — the count reverses. Do not reach for "
            "Kolmogorov complexity to rebut the metric objection; it concedes the point. "
            "(c) The Kuhn sentence stays in the body, in its own paragraph, flagged as "
            "cutting against us. A defender who discovers we knew the epicycle story was a "
            "myth and buried it in a footnote has earned the exchange. (d) On the "
            "theory-ladenness move, do not answer that some measurement is assumption-free; "
            "none is, and a defender who knows that will use the overclaim. Answer instead "
            "that the specific assumption the geocentric reading needs — that a turning "
            "cosmos sets the local compass of inertia — is itself a stipulated entity, "
            "so the reply costs the defender the very ledger he is disputing. That is why "
            "the sixth section is about accounting and refers the dynamics to R01 and R05 "
            "rather than re-arguing them; keep it that way. (e) The first paragraph's "
            "statement of what parsimony legitimately does must keep the clause that the "
            "tie-breaking job only arises once the rivals have been SHOWN to predict the same "
            "observations. Without it we have licensed the argument in our opening sentence "
            "and spend the rest of the entry objecting to a use we authorised, which is the "
            "defender's opening move above."),
    ),

    straw_man=dict(
        identified=True,
        detail=("The system being called confused and complicated is not the one that was being "
                "defended. A few lines above the quoted passage Rowbotham itemises the Earth's "
                "“a diurnal and an annual and various other motions”, adds the general "
                "motion of the Sun's system about a central Sun, and treats each entry as a "
                "separate thing assumed. In Newtonian celestial mechanics they are not separate "
                "assumptions: the “various other motions” - precession, nutation - "
                "follow from the torque on a spinning oblate Earth, and the planetary motions "
                "follow from one force law plus initial conditions. Counting the motions visible "
                "in the picture and reporting the total as the number of things the theory helps "
                "itself to is a description of a theory that nobody was arguing for. The part of "
                "the complaint that was fair is conceded rather than argued with: the central Sun "
                "really was a centre assigned on an inference that did not hold, and astronomy "
                "really did drop it."),
    ),

    compression=dict(
        assessed=True, drifted=True,
        list_phrasing=("“Simplicity favors geocentrism.” (item 83) · “Simpler moving sky.” (item 181)"),
        source_wording=("“These assumed general motions &hellip; together constitute a system so confused and "
                        "complicated that it is almost impossible and always difficult of comprehension "
                        "&hellip; The <em>most simple and direct experiments</em>, however, may be shown to "
                        "prove that the Earth has no progressive motion whatever; and here again the "
                        "advocates of this interminable and entangling arrangement <em>are challenged to "
                        "produce a single instance</em> of so called proofs of these motions which does not "
                        "involve an assumption &hellip; This is a plain, <em>simple</em>, and in every "
                        "respect <em>demonstrable</em> philosophy &hellip; <em>borne out by every fairly "
                        "instituted experiment</em>.”"),
        drift_type="scope_widened",
        note=("Three things travel with the word &ldquo;simple&rdquo; in <em>Earth Not a Globe</em> and none "
              "of them survives into the two list items. <strong>What it is an adjective of:</strong> in the "
              "book, &ldquo;simple&rdquo; is the fourth item in a list of four, and the load is on the other "
              "three &mdash; demonstrable, agreeing with the senses, borne out by experiment. The phrase "
              "&ldquo;the most simple and direct experiments&rdquo; modifies <em>experiments</em>, meaning "
              "methodologically plain, not model-economical. The list turns the adjective into the whole "
              "proof. <strong>Which system it is an adjective of:</strong> Rowbotham&rsquo;s simple system "
              "is a plane with every luminary inside 6,000 miles, established in his Section III by plane "
              "triangulation. Item 83 awards the virtue to <em>geocentrism</em> &mdash; in this list&rsquo;s "
              "other lineage a globe Earth at the centre of a real Solar System, which is the model Section "
              "III exists to deny. Both lineages are on the same 461-item list and only one of them can hold "
              "the prize. <strong>The speech act:</strong> his sentence about the rival system is a "
              "<em>challenge</em> &mdash; opponents &ldquo;are challenged to produce a single instance&rdquo; "
              "of a proof free of assumption &mdash; which is an invitation to answer. The list publishes a "
              "verdict. That is the same conversion caught at <a href=\"#ARG-R03\">ARG-R03</a>, where van der "
              "Kamp asks for a control experiment and the list prints the result he wanted tested: two "
              "lineages, a century apart, compressed in the same direction. "
              "<strong>The refutation above answers the source, not the fragment:</strong> it takes on the "
              "unearned-motions complaint at full strength, concedes that the central Sun he names was a real "
              "unmeasured stipulation that astronomy later dropped, and puts the weight on his own contents "
              "page and his own Section VIII rather than on the one-line item. A second drift value also "
              "fits &mdash; the conditional, challenge-shaped wording is restated flat, which is "
              "<em>hedge_dropped</em> &mdash; and the dominant one is recorded here."),
    ),

    verdict_challenge=dict(challenged=False, proposed_verdict=None, reasoning=None),

    people=["PER-ROWBOTHAM", "PER-CARPENTER", "PER-BOUW", "PER-PTOLEMY"],
    related=["D11", "D14", "D01", "D03", "D16", "R01", "R03", "R05", "R06", "R08", "R11",
             "A04", "A05", "A06", "B03"],

    sources=[
        dict(label="Rowbotham (“Parallax”), Zetetic Astronomy: Earth Not a Globe! (1865) — "
                   "Section XIV, the “confused and complicated” and “plain, simple” passage; "
                   "Section III, the Sun “under 4,000 miles”; Section VIII, the horizon "
                   "measurement. Project Gutenberg transcription of the 1865 printing",
             url="https://www.gutenberg.org/ebooks/69892"),
        dict(label="The same 1865 edition, Google/Internet Archive scan — independent second "
                   "retrieval of the Section XIV passage, printed pp. 180–181",
             url="https://archive.org/details/samuel_rowbotham_-_earth_not_a_globe"),
        dict(label="Rowbotham, 1881 third edition, ch. XV “General Summary — Application — Cui "
                   "Bono”, pp. 352–353 — the same passage, lightly reworded",
             url="https://www.sacred-texts.com/earth/za/za66.htm"),
        dict(label="Carpenter, One Hundred Proofs that the Earth Is Not a Globe (1885) — proof 20, "
                   "the explicit “common sense proof”",
             url="https://www.gutenberg.org/ebooks/55387"),
        dict(label="Ptolemy, Almagest I.7 — “this simpler conjecture” granted to the rotating "
                   "Earth and rejected on terrestrial grounds; English text hosted at CCSU, "
                   "translator not named on the page",
             url="https://bertie.ccsu.edu/naturesci/cosmology/ptolemy.html"),
        dict(label="Toomer's rendering of the same Almagest I.7 sentence, quoted in the Max Planck "
                   "MPRL study of Aristotle's and Ptolemy's approaches to geocentrism (its "
                   "footnote 32 credits the translation) — the standard scholarly rendering, "
                   "which differs from the CCSU text on where “simpler” attaches",
             url="https://www.mprl-series.mpg.de/studies/8/6/index.html"),
        dict(label="Copernicus, De revolutionibus Book I — ch. 6 on the vast world wheeling in "
                   "twenty-four hours, ch. 9 on retrogressions being “a movement of the Earth”; "
                   "English text hosted at CCSU, translator not named on the page",
             url="https://bertie.ccsu.edu/naturesci/cosmology/copernicus.html"),
        dict(label="Singham, “The Copernican myths”, Physics Today (Dec 2007) — Kuhn's count: "
                   "“Both employed over thirty circles; there was little to choose between them "
                   "in economy.”",
             url="https://physicstoday.aip.org/features/the-copernican-myths"),
        dict(label="Bouw, response to Faulkner, “Heliocentrism and Creationism” (geocentricity.com) "
                   "— “simplicity and truth are not related”, and Occam's razor scoped to “until "
                   "1729”",
             url="https://www.geocentricity.com/ba1/fresp/index.html"),
        dict(label="Baker, “Simplicity”, Stanford Encyclopedia of Philosophy — why parsimony needs "
                   "a stated measure and what evidential work it can and cannot do",
             url="https://plato.stanford.edu/entries/simplicity/"),
        dict(label="Bradley's discovery of stellar aberration, announced 1729 — the measurement "
                   "Bouw dates the razor's favourable verdict up to",
             url="https://en.wikipedia.org/wiki/Aberration_(astronomy)"),
        dict(label="Bessel's parallax of 61 Cygni, 1838 — eleven years before Rowbotham's first "
                   "pamphlet",
             url="https://en.wikipedia.org/wiki/61_Cygni"),
        dict(label="Johann Heinrich von Mädler — the Central Sun hypothesis placing the centre in "
                   "the Pleiades: “He got the location wrong”",
             url="https://en.wikipedia.org/wiki/Johann_Heinrich_von_M%C3%A4dler"),
        dict(label="The Final Experiment, Antarctica, December 2024 — the twenty-four-hour "
                   "southern midnight sun observed, and conceded, by Jeran Campanella",
             url="https://en.wikipedia.org/wiki/The_Final_Experiment_(expedition)"),
        dict(label="Di Virgilio et al., EPJ C 82:824 (2022) — the Wettzell ring laser reading the "
                   "Earth's rotation rate from a closed room to better than 1 part in 10⁹",
             url="https://link.springer.com/article/10.1140/epjc/s10052-022-10798-9"),
    ]),
}
