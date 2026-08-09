# -*- coding: utf-8 -*-
"""Batch 8 — B06. "Surveyors assume a plane and make no allowance."

Written 2026-08-09. This is the SURVEYING cluster. B01 owns the hydrostatic
premise ("water finds its level"), B04 owns light paths and the lighthouse
tables, B05 owns the ENGINEERING form of the no-allowance claim (canals, rail,
pipelines, bridges), B07 owns refraction-as-rescue. The ground held here is
survey practice specifically: datums, levelling procedure, triangulation,
cadastral survey, mine orientation.

Findings a future session should not have to re-derive.

1. THE PASSAGE IS NOT FROM 1849, AND THE TEXT DATES ITSELF. The cluster's
   originator_work/year read "Zetetic Astronomy", 1849 — the 16-page pamphlet.
   The surveying argument turns on a quoted Standing Order of the Houses of
   Lords and Commons on Railway Operations which the 1881 third edition dates
   to "the Session of 1862". A text quoting an 1862 Standing Order cannot be in
   an 1849 pamphlet. The earliest text we located is the 1865 first book
   edition, pp. 54-56 (Project Gutenberg #69892, verified on two independent
   mirrors), i.e. WRK-ROWBOTHAM-1865, whose own imprint field covers the 1881
   3rd ed. as well. passage.work is set to WRK-ROWBOTHAM-1865 here.
   >>> clusters.py ARG-B06 needed the same correction; it was reported by this
   agent (file not owned) and applied on 2026-08-09, in the house title form for
   this work: originator_work "Earth Not a Globe", year "1865".

2. THE BASIS LINE'S MECHANISM IS UNCONFIRMED. Our published basis says
   Rowbotham's "8 inches per mile squared" is "lifted from a surveying text".
   At 1881 ch. II p. 9 he introduces the figure flat — "From the summit of any
   such arc there will exist a curvature or declination of 8 inches in the
   first statute mile" — with no sourcing that we could locate on that page.
   The defensible statement, and the one used in the prose below, is narrower
   and checkable: 8 in/mile is exactly D^2/2R for one statute mile
   (0.0785 x 1.609^2 = 0.2032 m = 8.00 in), it is the first-mile value of the
   quantity the levelling literature calls the difference between the true and
   the apparent level, and it is the figure used in Simms's levelling treatise.
   >>> clusters.py ARG-B06 basis line needs rewording. NOT MADE HERE. Reported.

3. THE SELF-CONTRADICTION IS BETTER THAN THE ONE WE RECORDED, AND IT IS HIS
   OWN WITNESS. Rowbotham names the Ordnance Survey — "Every survey of this and
   other countries, whether ordnance or otherwise". Seven years before the 1865
   edition, that survey published Clarke's official account of the Principal
   Triangulation under the title "...and of the figure, dimensions and mean
   specific gravity of the Earth as derived therefrom" (1858), computing 289
   stations on the Airy ellipsoid with spherical excess carried. And in the
   1881 edition he cites that survey's own 108-mile Precelly-Kippure sight
   (Portlock) as evidence for himself.

4. THE DATUM IN THE STANDING ORDER IS A LEVEL SURFACE, AND THE ORDER SAYS SO.
   The 1865 text prints the order in full, including the clause requiring the
   datum line to "be referred to some fixed point stated in writing on the
   section" — a benchmark. British ordnance heights of that date ran from
   Ordnance Datum Liverpool, redefined from tidal observations at Victoria
   Dock in 1844. The "horizontal datum" he treats as proof of a plane is mean
   sea level read off a tide gauge.

5. THE BRITANNICA "LEVELLING" EXTRACT CUTS BOTH WAYS AND B04 ONLY USED HALF.
   B04 established that the article Rowbotham reprints at 1881 ch. II pp. 29-35
   gives him the refraction mechanism and the one-seventh coefficient. The
   other half is B06's: the article is a LEVELLING article, its subject is the
   difference between the true and apparent level, and its sentence "refraction
   may at a mean compensate for about one-seventh of the curvature of the
   earth" says in as many words that the formulae it supplies to levellers
   compute the earth's curvature. His own quoted authority is a surveying text
   making the allowance he says surveyors never make.

6. ONE-SEVENTH IS STILL THE NUMBER. Trimble Access's instrument-corrections
   page puts the earth-curvature correction at "approximately 16 [arcsec] per
   km measured distance" (= D/2R) and refraction at "approximately one-seventh
   of the earth curvature correction". Same coefficient, 160 years apart, in
   the manual of a machine surveyors carry.

7. FOUR OF THE FIVE ITEMS HAVE NO ANCESTOR WE COULD LOCATE HERE. Only item 223
   ("Surveying plane assumption.") matches the passage. Item 47 ("Surveying
   assumes stationary ground.") is a claim about MOTION, not shape. Items 382,
   383, 395 use vocabulary (equipotential, hydrology, mining) we did not locate
   in the passages searched. 383 ("Hydrology planar.") we read as the
   river-gradient claim of B01's item 384 ("River grades."), which is an
   inference from two words rather than anything the item says; on that reading
   the earliest text B01 could document for it is Carpenter 1885 proof 4, not
   Rowbotham. This is the R06 pattern: cluster-level attribution applied item by
   item without checking.

COULD NOT REACH: any copy or transcription of the 1849 pamphlet (B01 recorded
the same, 2026-08-07); the Encyclopaedia Britannica article "Levelling" in any
edition, so we could not read its tables or confirm which edition Rowbotham
quotes; Simms, A Treatise on the Principles and Practice of Levelling (1837 /
1875) directly — only a secondary listing; the chapter of the BLM Manual of
Surveying Instructions covering the tangent and secant methods for running a
true parallel of latitude (chapter 1 gave the 24-mile standard-parallel
interval only); Clarke 1858 itself, beyond its title and a contemporary MNRAS
notice.
"""

ENTRY = {

"B06": dict(

    tldr=("Rowbotham is right that a railway section is drawn to one datum line and that plane "
          "surveying ignores the earth's curvature over ordinary distances — concede both, they "
          "are in the manuals and in the Standing Order he quotes. The turn is what a survey "
          "datum is: in this trade horizontal means perpendicular to gravity, and the datum "
          "British ordnance heights ran from was mean sea level read off the Liverpool tide "
          "gauge — a level surface, not a plane. He then calls the Ordnance Survey as his "
          "witness, seven years after that survey published its Principal Triangulation under "
          "the title “and of the figure, dimensions and mean specific gravity of the Earth as "
          "derived therefrom”."),

    passage=dict(
        work="WRK-ROWBOTHAM-1865", pd=True,
        locator=("1st book ed. (London: Simpkin, Marshall; Bath: S. Hayward, 1865), Section I, "
                 "pp. 54-56 — Project Gutenberg #69892, sentences verified on two independent "
                 "mirrors. The same argument, revised and extended, at 3rd ed. rev. and enl. "
                 "(London: Day, 1881), ch. II, Experiment 13, pp. 47-57. Not the 1849 pamphlet: "
                 "see the gloss"),
        quote="""[1865, p. 54] It is commonly believed that surveyors when laying out railways and canals, are obliged to allow 8 inches per mile for the Earth's curvature …

[1865, p. 55, quoting the standing order] That the section be drawn to the same horizontal scale as the plan; and to a vertical scale of not less than one inch to every one hundred feet; and shall show the surface of the ground marked on the plan, the intended level of the proposed work, the height of every embankment, and the depth of every cutting; and a datum HORIZONTAL LINE, which shall be the same throughout the whole length of the work, or any branch thereof respectively; and shall be referred to some fixed point stated in writing on the section, near some portion of such work; and in the case of a canal, cut, navigation, turnpike, or other carriage road, or railway, near either of the termini.

[1865, p. 56] Every survey of this and other countries, whether ordnance or otherwise, is now carried out in connection with a horizontal datum, and therefore, as no other method proves satisfactory, it is virtually an admission by all the most practical scientific men of the day that the Earth cannot be other than a plane!

[1865, p. 56] … thus it is evident that the doctrine of the Earth's rotundity cannot be mixed up with the practical operations of civil engineers and surveyors, and to prevent the waste of time and the destruction of property which necessarily followed the doings of some who were determined to involve the convexity of the Earth's surface in their calculations, the very Government of the country has been obliged to interfere!

[1881 3rd ed., p. 57] In all these extensive surveys the doctrine of rotundity is, of necessity, entirely ignored; and the principle that the earth is a plane is practically adopted, and found to be the only one consistent with the results, and agreeing with the plans of the great surveyors and engineers of the day.""",
        gloss="""<p><strong>The text dates itself, and it is not 1849.</strong> The argument rests on a quoted Standing Order which the third edition introduces as &ldquo;<em>the Standing Orders of the Houses of Lords and Commons on Railway Operations, for the Session of 1862</em>&rdquo;. A text quoting an 1862 Standing Order cannot stand in a pamphlet published in 1849. The earliest text we located is the <strong>1865 first book edition</strong>, where the passage sits at pp.&nbsp;54&ndash;56; no copy or transcription of the sixteen-page 1849 pamphlet could be reached at all, and the same was recorded when <a href="#ARG-B01">ARG-B01</a> went looking for it. The 1881 revision extends the same argument with the Mont Fr&eacute;jus tunnel (completed 1871), the Suez Canal (opened 1869) and the Atlantic cable soundings; none of those was found in the portion of the 1865 text returned by our searches, and the first two postdate it. <strong>So this is a claim of the 1860s, sharpened in the 1880s.</strong></p>

<p><strong>What he actually claims is stronger than the list fragment, not weaker.</strong> The item that descends from this reads, in full, &ldquo;Surveying plane assumption.&rdquo; Rowbotham's sentence is an assertion about the entire profession and about Parliament: the horizontal datum is &ldquo;<em>virtually an admission by all the most practical scientific men of the day that the Earth cannot be other than a plane</em>&rdquo;, and the Standing Order exists, he says, because &ldquo;<em>the very Government of the country has been obliged to interfere</em>&rdquo; to stop engineers ruining works by putting convexity into their calculations. That is the version answered below. <strong>No purpose of that kind appears in the words of the order as he himself prints them</strong> &mdash; the clauses he quotes specify scales, an embankment and cutting schedule, a datum line constant along the work, and a requirement that the datum &ldquo;<em>be referred to some fixed point stated in writing on the section</em>&rdquo;.</p>

<p><strong>That last clause is the whole answer, and it is inside his own quotation.</strong> A datum line on a railway section is not a geometrical plane hung in space; it is a stated height above a physical benchmark. British ordnance heights of this period ran from <strong>Ordnance Datum Liverpool</strong>, redefined from tidal observations taken at Victoria Dock in 1844 &mdash; mean sea level read off a tide gauge. In his own Experiment 14 he prints a section diagram labelled &ldquo;<em>D, D, the datum line&mdash;the Trinity high water mark</em>&rdquo;, which is a tidal datum too. The surface every one of these works is referred to is the surface of the sea, and <a href="#ARG-B01">ARG-B01</a> establishes what that surface is.</p>

<p><strong>He calls the Ordnance Survey as his witness.</strong> &ldquo;<em>Every survey of this and other countries, whether ordnance or otherwise</em>&rdquo; &mdash; and seven years before the edition quoted here, the Ordnance Survey had published Captain A.&nbsp;R.&nbsp;Clarke's official account of the Principal Triangulation of Great Britain and Ireland under the title <em>Account of the observations and calculations of the Principal Triangulation; <strong>and of the figure, dimensions and mean specific gravity of the Earth as derived therefrom</strong></em> (London, 1858). It adjusted 289 stations by least squares, carried spherical excess through the triangles, computed each station's latitude and longitude on the Airy ellipsoid, and published a figure of the earth from the result. The witness he names had, in print, done the opposite of what he says every survey does.</p>

<p><strong>And in 1881 he quotes that very survey back at us.</strong> Experiment 14 of the third edition observes that &ldquo;<em>the length of some of the sides of the great triangles (in the English survey) is upwards of 100 miles</em>&rdquo;, and cites &ldquo;<em>Lieutenant-Colonel Portlock, R.E., who observed the station on Precelly, a mountain in South Wales, from the station on Kippure, a mountain about 10 miles south-west of Dublin&mdash;the distance between the stations being 108 miles</em>&rdquo;. Those are trigonometrical stations of the Principal Triangulation, and both are mountain tops &mdash; which is the only way to get a 108-mile sight, and the reason the survey put its stations there.</p>

<p><strong>The encyclopaedia article he reprints is a surveying article.</strong> Twenty-five pages earlier in the same chapter he typesets an extract from the <em>Encyclop&aelig;dia Britannica</em>, article &ldquo;<em>Levelling</em>&rdquo;. <a href="#ARG-B04">ARG-B04</a> takes what it gives him about refraction &mdash; the mechanism, the one-seventh mean, the variability. The half that belongs here is what the article is <em>about</em>: the difference between the true and the apparent level, which is the curvature term in levelling. Its own sentence says refraction &ldquo;<em>may at a mean compensate for about one-seventh of <strong>the curvature of the earth</strong></em>&rdquo;, and it closes &ldquo;<em>we have, therefore, made no allowance for refraction in the foregone formul&aelig;</em>&rdquo; &mdash; the foregone formul&aelig; being the ones that compute that curvature for a leveller to use. Rowbotham's comment on it is &ldquo;<em>It will be seen from the above that, in practice, refraction need not be allowed for</em>&rdquo;. He read a levelling manual's instruction not to apply a <em>fixed</em> refraction correction as permission to discard the curvature correction the manual was supplying.</p>""" ),

    steelman=dict(
        description="""<p><strong>SURFACE (weak &mdash; and a working surveyor will take it apart).</strong> &ldquo;Surveyors do allow for curvature.&rdquo; Said bare, this loses, because for the overwhelming majority of jobs they demonstrably do not. A crew setting out a subdivision, running a level circuit round a site, or staking a road never adds eight inches per mile to anything, and the textbooks say so in as many words: plane surveying is defined as the surveying in which the curvature of the earth is neglected. Anyone who opens by denying that has picked a fight with the manuals and will lose it.</p>

<p><strong>DEEPER (true, incomplete).</strong> &ldquo;Plane surveying is a bounded approximation with a published error.&rdquo; Correct. The standard texts put the limit at roughly 260&nbsp;km&sup2; (about 100 square miles) and the reason is arithmetic anyone can check: the spherical excess of a triangle on the earth is one arcsecond per <em>R</em>&sup2;&nbsp;sin&nbsp;1&Prime; of area, and with <em>R</em>&nbsp;=&nbsp;6371&nbsp;km that is one arcsecond per about 197&nbsp;km&sup2;. A 260&nbsp;km&sup2; figure therefore carries about 1.3&Prime; of excess &mdash; below what most instruments and most jobs can see, and above zero. The flat-earth site that runs this argument does the sum honestly and gets 20&nbsp;m of &ldquo;ignored curvature&rdquo; across a 100-square-mile block; the drop from a tangent plane over 16.1&nbsp;km is indeed 16,100&sup2;/(2&nbsp;&times;&nbsp;6,371,000)&nbsp;=&nbsp;20.3&nbsp;m. But stated alone this invites the obvious reply: <em>then when do they start allowing for it, and why does nothing ever go wrong if they don't?</em></p>

<p><strong>KERNEL &mdash; the true thing is that a leveller really does not add eight inches a mile, and the reason is a procedure built around the curvature.</strong> This is the specific correct observation at the bottom of the cluster, and it deserves to be stated in its strongest form. In differential levelling the instrument is set between two staves and the backsight and foresight are made <em>equal in length</em>. Both readings are then displaced by exactly the same curvature-and-refraction term, and the term cancels identically in the difference. The manual puts it plainly: &ldquo;<em>For most work it is sufficient to keep the foresight and backsight distances approximately equal so that the refraction and curvature effects cancel out.</em>&rdquo; So the surveyor makes no allowance &mdash; and this is not sloppiness or convention, it is the correct handling of a term that is really there. <strong>The instruction to balance the sights exists because the earth is curved.</strong> On a plane there would be nothing to cancel and the rule would not be in the book.</p>

<p><strong>Second half of the kernel: plane surveying's plane is horizontal, never vertical.</strong> The 20&nbsp;m figure is a drop from a <em>tangent plane</em>, and no survey on earth measures heights from a tangent plane. Elevations are referred to a level surface &mdash; the USGS glossary defines horizontal as &ldquo;<em>a direction perpendicular to the force of gravity</em>&rdquo; and the geodetic levelling manual calls the reference surfaces &ldquo;<em>level</em>&rdquo; or equipotential surfaces. What plane surveying approximates is the <em>horizontal position</em> computation over a small block. Item 382 of this cluster, &ldquo;Leveling equipotential planes&rdquo;, has already conceded the noun and is arguing about the adjective.</p>""",

        why_it_doesnt_save_claim="""<p><strong>Because every procedure that lets a surveyor ignore curvature is engineered around it, and each one fails in the direction a sphere predicts the moment you stop obeying it.</strong> Four cases, all from ordinary practice, none of them exotic.</p>

<p><em>Unbalanced sights.</em> The cancellation is exact only while the two sight lengths match. Let them differ and the combined curvature-and-refraction term enters at 0.0675<em>D</em>&sup2; metres with <em>D</em> in kilometres &mdash; 0.7&nbsp;mm at a 100&nbsp;m sight, 6.8&nbsp;cm at a kilometre. That is why the tolerance tables exist and why precise-levelling specifications cap the imbalance.</p>

<p><em>Trigonometric heighting.</em> You cannot balance anything when you shoot a single long ray with a total station, so the correction goes back in explicitly &mdash; and it is a switch on the instrument. Trimble's own documentation gives the earth-curvature correction as &ldquo;<em>approximately 16&Prime; per km measured distance</em>&rdquo;, which is <em>D</em>/2<em>R</em> to three figures, and puts refraction at &ldquo;<em>approximately one-seventh of the earth curvature correction</em>&rdquo;. <strong>That is the same one-seventh Rowbotham printed out of the Britannica.</strong></p>

<p><em>Level networks.</em> Run a long line north and the level surfaces themselves converge; the orthometric correction that a national levelling network applies is zero for a strictly east&ndash;west run and grows with the north&ndash;south component, because &ldquo;<em>level surfaces are irregular and converge toward the poles</em>&rdquo;. And when Britain ran its Second Geodetic Levelling it found mean sea level differing by 0.81&nbsp;ft between the Dunbar and Newlyn gauges &mdash; which is why Newlyn alone became the datum. On a plane surface of still water there is no such difference to find.</p>

<p><em>Cadastral survey.</em> The most aggressively planar survey system ever built, the American township grid, is interrupted on purpose. The BLM Manual: &ldquo;<em>The convergency is taken up at intervals by the running of standard parallels, on which the measurements are again made full &hellip; The usual interval between the standard parallels is 24 miles.</em>&rdquo; A surveyor running range lines north hits a correction line every 24 miles and starts again, because the meridians he is following are converging.</p>

<p>So the kernel is real and it points the other way. &ldquo;No allowance is made&rdquo; is true of a procedure whose entire design is an allowance.</p>"""),

    refutation="""<p><strong>Concede the observations first, because they are correct.</strong> Plane surveying exists, it is taught under that name, and it treats the survey area as a plane. Railway sections really are drawn to a single datum line running the length of the work, because the Standing Order Rowbotham quotes really does require it. A crew running levels really does not add eight inches per mile. None of that is in dispute, and a rebuttal that starts by denying it has lost the argument to any reader who has held a staff.</p>

<p><strong>1. &ldquo;Horizontal&rdquo; and &ldquo;datum&rdquo; are gravity words, and the Standing Order says so itself.</strong> The argument needs <em>horizontal datum line</em> to mean <em>plane</em>. In surveying it does not. The USGS glossary defines horizontal as &ldquo;<em>a direction perpendicular to the force of gravity</em>&rdquo; and level as &ldquo;<em>a line or surface whose segments are all horizontal</em>&rdquo;; the geodetic levelling manual states that the gravity field &ldquo;<em>can be represented as a series of surfaces of equal potential, termed &lsquo;level&rsquo; or equipotential surfaces</em>&rdquo;. A spirit level is a gravity instrument: the bubble finds the perpendicular to the local plumb line and nothing else. And the order Rowbotham prints does not stop at requiring a datum &mdash; it requires that the datum &ldquo;<em>be referred to some fixed point stated in writing on the section</em>&rdquo;. That fixed point is a benchmark, and British ordnance benchmarks of the 1860s carried heights above <strong>Ordnance Datum Liverpool</strong>, redefined from tidal observations at Victoria Dock in 1844. His own Experiment 14 labels a section diagram &ldquo;<em>the datum line&mdash;the Trinity high water mark</em>&rdquo;. The datum is the sea. Reading a sea-surface datum as proof of a plane is the equivocation <a href="#ARG-B01">ARG-B01</a> takes apart, arriving here by a different road.</p>

<p><strong>2. What plane surveying approximates, and what it never approximates.</strong> The plane in plane surveying is the horizontal-position plane over a limited block. Heights are never referred to it. The published limit is about 260&nbsp;km&sup2;, and the reason is checkable arithmetic rather than convention: spherical excess accumulates at one arcsecond per <em>R</em>&sup2;&nbsp;sin&nbsp;1&Prime;&nbsp;&asymp;&nbsp;197&nbsp;km&sup2; of triangle area, so a block of that size carries roughly 1.3&Prime; &mdash; small enough to drop for a boundary survey, and a quantity somebody has computed rather than assumed. The tangent-plane drop across the same block, about 20&nbsp;m over 16&nbsp;km, is not an error anybody is carrying, because no survey measures a height from a tangent plane. <strong>A stated threshold with a computed error term is the opposite of an assumption.</strong> The honest form of the flat-earth question &mdash; <em>at what point are they trained to factor it in?</em> &mdash; has a numerical answer in every textbook, and the answers below are the specific ones.</p>

<p><strong>3. Levelling: the allowance is a procedure, not a number.</strong> Set the level midway and make the backsight and foresight equal, and the curvature-and-refraction displacement is identical in both readings and cancels in the difference &mdash; &ldquo;<em>keep the foresight and backsight distances approximately equal so that the refraction and curvature effects cancel out</em>&rdquo;. Break the balance and the term reappears at 0.0675<em>D</em>&sup2; metres for <em>D</em> in kilometres: sub-millimetre at a hundred metres, 6.8&nbsp;cm at a kilometre. Reciprocal levelling across a river &mdash; the case where you cannot put the instrument in the middle &mdash; is done by observing both ways and meaning the results, which cancels the same term by a different trick. Every one of these is a technique for handling a real quantity. <strong>The eight inches Rowbotham says nobody allows for is the first-mile value of that quantity:</strong> the drop of a sphere below its tangent is <em>D</em>&sup2;/2<em>R</em>, and for one statute mile 0.0785&nbsp;&times;&nbsp;1.609&sup2;&nbsp;=&nbsp;0.2032&nbsp;m, which is 8.00 inches. It is the figure the nineteenth-century levelling literature carries &mdash; Simms's <em>Treatise on the Principles and Practice of Levelling</em> uses 8&nbsp;in per mile squared &mdash; and it is the subject of the encyclopaedia article Rowbotham reprints in the same chapter, whose whole business is the difference between the true and the apparent level.</p>

<p><strong>4. Where you cannot cancel it, it is a setting on the instrument.</strong> Trigonometric heights from a total station are single long rays with nothing to balance against, so the correction is applied outright, and the manufacturer's documentation states its size: the earth-curvature correction is &ldquo;<em>approximately 16&Prime; per km measured distance</em>&rdquo; &mdash; <em>D</em>/2<em>R</em> in arcseconds is 16.2 &mdash; and the refraction correction runs the other way at &ldquo;<em>approximately one-seventh of the earth curvature correction</em>&rdquo;, with coefficients of 0.13, 0.142 or 0.2 selectable. <strong>The one-seventh in a 2020s field-software manual is the one-seventh Rowbotham typeset out of the <em>Encyclop&aelig;dia Britannica</em> and dismissed.</strong> The refraction half of that inheritance is <a href="#ARG-B04">ARG-B04</a>'s and <a href="#ARG-B07">ARG-B07</a>'s; what matters here is that both halves come from an article about how to run a level.</p>

<p><strong>5. The extensive surveys, which is where the claim breaks outright.</strong> &ldquo;<em>In all these extensive surveys the doctrine of rotundity is, of necessity, entirely ignored</em>&rdquo;, and &ldquo;<em>every survey of this and other countries, whether ordnance or otherwise</em>&rdquo;. Take him at his word and go to the ordnance survey he names. Its Principal Triangulation, observed from 1791 and adjusted by Captain A.&nbsp;R.&nbsp;Clarke, was published in 1858 as <em>Account of the observations and calculations of the Principal Triangulation; and of the figure, dimensions and mean specific gravity of the Earth as derived therefrom</em> &mdash; 289 stations, adjusted by least squares, with the spherical excess of the triangles carried through the computation, positions reduced on the Airy ellipsoid, and a figure of the earth published out of the far end (from British data alone, <em>a</em>&nbsp;=&nbsp;20,927,005&nbsp;ft with flattening 1/299.33). The claim is not merely that these surveys used a curved earth; it is that deriving the shape of the earth <em>was one of the stated products</em>, on the title page, seven years before the edition quoted here. <strong>And the third edition cites that same survey approvingly</strong>, invoking Portlock's 108-mile sight from Kippure to Precelly. Those are two of its trig stations, and both are mountain summits &mdash; the elevation being exactly what buys the sight line.</p>

<p><strong>6. Cadastral survey: the flattest grid ever drawn is cut every 24 miles.</strong> The United States Public Land Survey lays townships out in nominal six-mile squares, which is as close to assuming a plane as surveying gets. It cannot close, because meridians converge, and the Manual of Surveying Instructions says what is done about it: &ldquo;<em>The convergency is taken up at intervals by the running of standard parallels, on which the measurements are again made full. On the standard parallels (first named &lsquo;correction lines&rsquo;) there are offsets in the range lines and two sets of corners &hellip; The usual interval between the standard parallels is 24 miles.</em>&rdquo; Every jog in the American township grid &mdash; visible from the air, and in the kink of any road that follows a range line &mdash; is a curvature allowance carried out with a chain by a surveyor who was, in every other respect, treating the ground as flat.</p>

<p><strong>7. Item 47, which is a different claim and answers itself underground.</strong> &ldquo;Surveying assumes stationary ground&rdquo; is about motion, not shape, and we did not locate any argument of that kind in the passages searched. Answered on its merits: the standard instrument for orienting a survey where the sky is not visible is the <strong>gyrotheodolite</strong>, and what it senses is the earth's rotation. A wheel spun at 20,000&nbsp;rpm and released near the meridian precesses into alignment with it, because &ldquo;<em>the gyroscopic reaction of spin and Earth's rotation results in precession of the spin axis in the direction of alignment with the plane of the meridian</em>&rdquo;. It is &ldquo;<em>the main instrument for orientation in mine surveying and in tunnel engineering</em>&rdquo;; it steered the Channel Tunnel; it gives the meridian to about 10 arcseconds; and it stops working within roughly 15&deg; of the pole, &ldquo;<em>where the angle between the earth's rotation and the direction of gravity is too small for it to work reliably</em>&rdquo;. That latitude dependence is a rotating sphere's signature, and it is the reason mine surveyors buy a different instrument at high latitudes. Above ground the same point is made by the geodetic datums themselves, which no longer pretend the ground is fixed: modern reference frames carry station velocities and epoch-dependent coordinates precisely because the crust moves.</p>

<p><strong>8. Item 395, mine surveys, and item 383.</strong> Mine surveying is where the argument is weakest rather than strongest: an underground survey is tied to the surface network through the shaft, oriented by an instrument that works only because the earth turns, and computed on the same national grid as everything above it. It is also, historically, where the mass of the earth was weighed &mdash; Airy's 1854 pendulum experiment in the Harton Colliery was published as an <em>Account of pendulum experiments undertaken in the Harton Colliery, for the purpose of determining the mean density of the Earth</em>, and &ldquo;mean specific gravity of the Earth&rdquo; is on the title page of the Ordnance Survey's triangulation report for the same reason. Item 383 is two words, &ldquo;Hydrology planar&rdquo;, and we read it as the river-gradient claim &mdash; an inference from those two words rather than anything the item states. On that reading the earliest text <a href="#ARG-B01">ARG-B01</a> could document for it is Carpenter's 1885 proof 4 rather than anything of Rowbotham's. The engineering form of the no-allowance argument &mdash; canals, rail, pipelines, bridges &mdash; is <a href="#ARG-B05">ARG-B05</a>'s and is not re-argued here.</p>

<p><strong>Verdict: self-contradicted, and by a witness of his own choosing.</strong> The argument's evidence is (i) an encyclopaedia article on levelling, whose subject is the difference between the true and the apparent level and which states that refraction offsets about one-seventh of the curvature of the earth; (ii) a Standing Order requiring a datum line referred to a fixed benchmark, on a network whose zero was a tide gauge; and (iii) the Ordnance Survey, whose principal publication of the period derived the figure and dimensions of the earth from the survey in question. All three were in the book. Two of them he printed himself.</p>""",

    advocate=dict(
        best_defense=(
            "You have conceded the case and then changed the subject. My claim is about what "
            "surveyors do, and you agree: plane surveying assumes a flat earth up to 260 square "
            "kilometres; a leveller adds nothing for curvature; the Standing Order requires one "
            "datum line for the whole length of the work. Your own citation shows the curvature "
            "correction on a total station is a checkbox an operator can switch OFF — nobody "
            "offers an off switch for a real physical effect. Balanced sights are not a "
            "cancellation of curvature, they are a cancellation of collimation error, and they "
            "would be good practice on a plane too. The ellipsoid you keep pointing at lives in "
            "the computations of national agencies, not in the field: millions of surveys fix "
            "property lines, build roads and sink shafts on a plane and close correctly. If the "
            "earth were curved that would be impossible — errors would accumulate and someone "
            "would notice. Correction lines every 24 miles prove convergence of meridians, which "
            "is a fact about a map projection, not about the shape of the ground. And your one "
            "honest admission is the biggest: the 20 metres across a 100-square-mile block is "
            "ignored, by your own arithmetic, in the surveys that lay out the world."),
        survives=4,
        preemptive=(
            "This is strong enough that three specific answers must be IN THE BODY, not left to "
            "the reader, and all three are already there — keep them if the entry is ever "
            "trimmed. (a) The off switch. Section 3 gives the size of the term rather than "
            "asserting its existence: 0.7 mm at a 100 m sight, 6.8 cm at a kilometre. It is "
            "switchable because at short range it is below tolerance and at long range it is "
            "not; that is a threshold, and thresholds are what the defence claims surveyors do "
            "not have. (b) The balanced-sight reinterpretation is the sharpest move available "
            "to them and section 3 must not be softened: balancing cancels collimation error AND "
            "the curvature-refraction term, and it is the standard text's own stated reason — "
            "quote it rather than paraphrase. On a plane there is no c+r term to cancel, so the "
            "rule would be half as motivated and the 0.0675*D^2 tolerance table would not exist. "
            "(c) 'Errors would accumulate and someone would notice' is the defence's best line "
            "and section 6 is the answer: they do, someone did, and the fix is printed in the "
            "BLM Manual as a 24-mile interval. Do not let 'convergence is a projection artefact' "
            "pass — the correction lines are run on the ground with a chain, and the jog is "
            "physically in the road. ONE ADDITION IF THE ENTRY IS EXTENDED: the strongest "
            "un-deployed datum is a direct measurement of level-surface non-parallelism — the "
            "0.81 ft discrepancy between the Dunbar and Newlyn tide gauges in the Second "
            "Geodetic Levelling, which currently sits only in the steelman. A plane surface of "
            "still water cannot produce two mean sea levels at different heights, and that is a "
            "measurement, not a computation.")),

    straw_man=dict(
        identified=True,
        detail=("The source supplies a motive for the Standing Order that the order's own text, "
                "as he prints it, does not contain: the requirement exists, he writes, to prevent "
                "“the waste of time and the destruction of property which necessarily followed "
                "the doings of some who were determined to involve the convexity of the Earth's "
                "surface in their calculations”, so that “the very Government of the country "
                "has been obliged to interfere.” The clauses he quotes specify scales, an "
                "embankment and cutting schedule, a datum line constant along the work, and a tie "
                "to a named fixed point. Engineers wrecking works by allowing for curvature is a "
                "story about the profession that the document is not evidence for, and a reader "
                "who only sees the quotation would take it for the order's own account of itself. "
                "Our side has a matching temptation to avoid: asserting that surveyors do allow for "
                "curvature, full stop. Mostly they do not, and saying otherwise hands the exchange "
                "to anyone who has run a level circuit.")),

    compression=dict(
        assessed=True, drifted=True,
        list_phrasing="Surveying assumes stationary ground.",
        source_wording=("“Every survey of this and other countries, whether ordnance or otherwise, "
                        "is now carried out in connection with a horizontal datum, and therefore, as no "
                        "other method proves satisfactory, it is virtually an admission by all the most "
                        "practical scientific men of the day that the Earth cannot be other than a "
                        "plane!” (1865, p. 56)"),
        drift_type="unsourced_addition",
        note=("<p>The drift here is not softening &mdash; the source is <em>more</em> emphatic than "
              "anything on the list, claiming an admission by the whole profession and an "
              "intervention by Parliament. The drift is that four of the cluster's five items are "
              "not the source's argument.</p>"
              "<p><strong>Item 223, &ldquo;Surveying plane assumption&rdquo;, is faithful</strong> and is "
              "what the refutation above answers, at the strength quoted. <strong>Item 47, "
              "&ldquo;Surveying assumes stationary ground&rdquo;, is a claim about motion, not "
              "shape</strong>; we did not locate any argument of that kind in the texts searched "
              "(1865 ed., Project Gutenberg #69892, the datum and survey passage at pp. 54&ndash;56; "
              "1881 3rd ed., ch. II Experiments 13&ndash;14 via the Internet Sacred Text Archive), and "
              "we did not run a full-text search of either edition for it. Items 382, 383 and 395 "
              "introduce vocabulary &mdash; equipotential surfaces, hydrology, mine surveying &mdash; "
              "for which we located no ancestor in those same passages; item 383, &ldquo;Hydrology "
              "planar&rdquo;, we read as the river-gradient claim, which is an inference from two "
              "words rather than anything the item states, and on that reading the earliest text "
              "<a href=\"#ARG-B01\">ARG-B01</a> could document for it is Carpenter's 1885 proof 4 "
              "rather than anything of Rowbotham's. Unreachable is not absent, and this is a statement "
              "about the passages we read, not about the corpus.</p>"
              "<p>That pattern &mdash; one cluster attribution applied to every item in the cluster &mdash; "
              "is the same failure recorded against ARG-R06 in the corrections log, and the same "
              "test applied to ARG-E13 moved the published totals in the other direction. It is "
              "worth stating plainly which way it cuts here: the surveying argument really is "
              "Rowbotham's, and it is his in a stronger form than the list states. Four items "
              "riding on it are of unestablished authorship.</p>")),

    verdict_challenge=dict(challenged=False, proposed_verdict=None, reasoning=None),

    people=["PER-ROWBOTHAM", "PER-CARPENTER"],
    related=["B01", "B02", "B04", "B05", "B07", "B09"],

    sources=[
        dict(label="Rowbotham (“Parallax”), Zetetic Astronomy: Earth Not a Globe, 1st book ed. 1865 "
                   "— the datum-line and survey passage at pp. 54–56 (Project Gutenberg #69892)",
             url="https://www.gutenberg.org/files/69892/old/69892-h/69892-h.htm"),
        dict(label="Rowbotham, 3rd ed. rev. and enl. (London: Day, 1881), ch. II Experiment 13, pp. 47–57 "
                   "— the Standing Orders of the Session of 1862 and “in all these extensive surveys”",
             url="https://sacred-texts.com/earth/za/za18.htm"),
        dict(label="Rowbotham, 1881 3rd ed., ch. II Experiment 14 — Portlock's 108-mile Kippure–Precelly "
                   "sight and the “Trinity high water mark” datum line",
             url="https://sacred-texts.com/earth/za/za19.htm"),
        dict(label="Rowbotham, 1881 3rd ed., ch. II Experiment 9, pp. 29–35 — the Encyclopædia Britannica "
                   "article “Levelling” as he reprints it, and his comment on it",
             url="https://sacred-texts.com/earth/za/za14.htm"),
        dict(label="Clarke, Account of the observations and calculations of the Principal Triangulation; and of "
                   "the figure, dimensions and mean specific gravity of the Earth as derived therefrom "
                   "(Ordnance Survey, 1858) — contemporary notice in MNRAS 19:194",
             url="https://academic.oup.com/mnras/article/19/5/194/1039968"),
        dict(label="Principal Triangulation of Great Britain — spherical excess carried through the triangles; "
                   "Clarke's adjustment of 289 stations on the Airy ellipsoid",
             url="https://en.wikipedia.org/wiki/Principal_Triangulation_of_Great_Britain"),
        dict(label="Alexander Ross Clarke — the 1858 report's contents and the ellipsoids derived from it",
             url="https://en.wikipedia.org/wiki/Alexander_Ross_Clarke"),
        dict(label="Ordnance datum — Ordnance Datum Liverpool redefined from 1844 tidal observations at "
                   "Victoria Dock; Newlyn 1915–21; the 0.81 ft Dunbar–Newlyn discrepancy",
             url="https://en.wikipedia.org/wiki/Ordnance_datum"),
        dict(label="Levelling — balanced backsight and foresight distances so that “refraction and curvature "
                   "effects cancel out”",
             url="https://en.wikipedia.org/wiki/Levelling"),
        dict(label="Trimble Access instrument corrections — earth-curvature correction “approximately 16″ per km”, "
                   "refraction “approximately one-seventh of the earth curvature correction”, coefficients "
                   "0.13 / 0.142 / 0.2",
             url="https://help.fieldsystems.trimble.com/trimble-access/latest/en/instrument-corrections.htm"),
        dict(label="Open Access Surveying Library, vertical datum chapter — level surfaces are equipotential, "
                   "converge toward the poles, and require an orthometric correction on north–south runs",
             url="https://jerrymahun.com/index.php/home/open-access/93-updating/432-chapter-f-vertical-datum?showall=1"),
        dict(label="Kozlowski, “Definition of Level” — USGS: horizontal is “a direction perpendicular to the "
                   "force of gravity”; USC&GS Manual of Geodetic Leveling on “level” or equipotential surfaces",
             url="https://jessekozlowski.wordpress.com/2020/02/19/definition-of-level/"),
        dict(label="BLM Manual of Surveying Instructions (1973), ch. 1 — standard parallels or “correction lines” "
                   "at the usual interval of 24 miles, taking up the convergency",
             url="https://www.cadastral.com/73manlc1.htm"),
        dict(label="Gyrotheodolite — senses the earth's rotation; main instrument for mine surveying and "
                   "tunnelling; unusable within about 15° of the pole",
             url="https://en.wikipedia.org/wiki/Gyrotheodolite"),
        dict(label="Airy, “Account of pendulum experiments undertaken in the Harton Colliery, for the purpose of "
                   "determining the mean density of the Earth” (Royal Society, read 1856)",
             url="https://royalsocietypublishing.org/rspl/article/doi/10.1098/rspl.1856.0007/107934/Account-of-pendulum-experiments-undertaken-in-the"),
        dict(label="Metabunk, “Curvature and Refraction in Surveying and Leveling Through History” — the "
                   "period levelling literature, including Simms's Treatise on … Levelling using 8 in per "
                   "mile squared (listing consulted; Simms itself not reached)",
             url="https://www.metabunk.org/threads/curvature-and-refraction-in-surveying-and-leveling-through-history-old-books-etc.8856/"),
        dict(label="The modern flat-earth statement of this argument, quoting the 260 km² plane-surveying "
                   "limit and computing 20 m of “ignored” curvature across it",
             url="https://www.galileolied.com/plane-surveying")]),
}
