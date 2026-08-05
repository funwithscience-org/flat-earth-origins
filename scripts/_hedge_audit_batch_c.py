# -*- coding: utf-8 -*-
"""Hedge-rule audit, batch C — C02, E01, E17.

Written 2026-08-05 against THE HEDGE RULE in scripts/deep.py. Each entry is a
`compression` block ready to be dropped into the argument's batch file (E17 in
deep_batch1.py, C02 in deep_batch2.py, E01 in deep_batch4.py).

Primary-source reach:
  C02  Rob Skiba, "The Bible and the Still Flat Earth" — REACHED, in full, as a
       PDF mirrored at s3.amazonaws.com/mychurchwebsite/c4890/. This is the
       named originator's own text and it settles the question the audit was
       asked: he asserts a physically stationary Earth and a physically moving
       sun, and does not entertain the observer's-appearance reading at any
       point. Corroborated by the "more than 200" compilation at
       worldslastchance.com, whose section headings ("Sun Moves, not the
       Earth", "Sun STOPS moving", "Sun moves BACKWARDS", "Earth is a
       Disk/Circle, not a ball", "Earth has 4 Corners/Quarters", "Earth has
       Pillars, and hangs on nothing") are the ones our C02 refutation already
       quotes verbatim without citing them.
       NOT REACHED: testingtheglobe.com and robschannel.com, both HTTP-only —
       WebFetch upgrades to HTTPS and the sites 302 back down, and the Wayback
       Machine was rejected by the proxy (403). Skiba's book "Testing the
       Globe" (2018) was not obtained; the assessment rests on his own PDF
       essay, not the book.
  E01  The Principle (2014) — the FILM ITSELF NOT REACHED; it is in copyright
       and not viewable. Verified instead: the distributor's press release
       carrying the official synopsis (PR Newswire, confirming our `passage`
       quote verbatim and supplying the interrogative frame around it), Rick
       DeLano's own scoping statement, Robert Sungenis's December 2013 press
       release, and Variety's review by a critic who watched the film. The
       assertion-strength finding rests on those four, not on the film's
       soundtrack.
  E17  NO SOURCE EXISTS. See the note at the foot of this file.
"""

HEDGE_C = {

"C02": dict(
    assessed=True, drifted=False,
    drift_type="none",
    list_phrasing=(
        "Eccles 1:5 sun rises and sets. / "
        "Joshua 10:13 sun stood still. / "
        "Habakkuk 3:11 sun and moon halted. / "
        "Isaiah 38 sundial reversal. / "
        "Sun's circuit divine metaphor."),
    source_wording=(
        "&ldquo;Indeed, without a doubt, Scripture is telling us the earth is not constantly "
        "moving. In fact, there is growing evidence within the scientific community revealing "
        "that the earth is not rotating either. It is quite stationary in every respect.&rdquo; "
        "&mdash; and, of the plain text, &ldquo;no one would ever think anything different from "
        "what it says.&rdquo;"),
    note=(
        "This comparison could have gone the other way, and it is worth saying why it did not. "
        "The concern was that the source might treat these verses as devotional or "
        "observer-relative language &mdash; how the sky looks from where a person stands &mdash; "
        "while the list re-presented them as physical claims about the sun&rsquo;s motion. That "
        "would be a category shift, and it is the commonest failure in this family. Read against "
        "the named source&rsquo;s own text, it is not what happened. Skiba states the conclusion "
        "in the flattest terms available: the earth is <em>not rotating either</em>, and is "
        "<em>quite stationary in every respect</em>. The appearance-from-the-observer reading is "
        "not conceded and then overrun; it is never entertained, and he adds that on a plain "
        "reading no one would think otherwise. The list items are bare verse labels and carry "
        "<em>less</em> assertion than the paragraphs they were drawn from, not more.</p>"
        "<p><strong>The treatment above is therefore aimed at the source&rsquo;s own claim</strong> "
        "&mdash; a stationary Earth asserted as fact, not a reading offered as devotion. One "
        "caveat we record rather than resolve: two Psalm 19 items sit in this cluster, though the "
        "compilations file those verses under headings about the firmament and the &ldquo;line&rdquo; "
        "of creation rather than under sun-motion.")),

"E01": dict(
    assessed=True, drifted=True,
    list_phrasing=(
        "CMB axis aligned with Earth. / "
        "Anisotropy toward Earth. / "
        "Cosmic anisotropy Earth-oriented. / "
        "Planck data Earth preference."),
    source_wording=(
        "&ldquo;unexpected evidence of a preferred direction in the cosmos, aligned with our "
        "<em>supposedly</em> insignificant Earth&rdquo; &mdash; framed by the same release as a "
        "question, &ldquo;What if everything you think you know about our Universe is wrong?&rdquo; "
        "Its producer: the film &ldquo;is not about geocentrism per se, but is instead an in-depth "
        "cinematic examination of the Copernican Principle itself.&rdquo;"),
    drift_type="hedge_dropped",
    note=(
        "The list states as fact what the film puts as a question. The distributor&rsquo;s synopsis "
        "opens <em>What if everything you think you know about our Universe is wrong?</em> and asks "
        "whether new evidence <em>reveals</em> a preferred direction; DeLano, asked directly, said "
        "the film is <em>not about geocentrism per se</em> but an examination of the Copernican "
        "Principle &mdash; though he has elsewhere called geocentrism a profoundly important part "
        "of the story, so the scoping is not consistent. A reviewer who watched it reports a film "
        "that seeds the conclusion without owning it, saying the patterns <em>seem</em> to align "
        "with the Earth. Ten numbered items keep none of that: <em>CMB axis aligned with "
        "Earth</em>, flat.</p>"
        "<p>The wider gap is one link further back. The papers the film draws on hedge harder than "
        "the film does &mdash; Land and Magueijo revisited their own axis in 2007 and found no "
        "evidence for the most general model under Bayesian comparison, and Planck 2018 VII says "
        "the extent to which these features evidence a violation of isotropy remains unclear. "
        "Certainty is added at every handoff.</p>"
        "<p><strong>None of which makes the anomaly go away, and the refutation above does not "
        "claim it does.</strong> It answers the film&rsquo;s actual claim &mdash; that the "
        "Copernican principle has been contradicted &mdash; while conceding that the alignments "
        "are real, reproducible and unexplained.")),

# E17 is a T3 entry: `passage` is None and no source has ever been identified for
# any of the seven items. There is therefore nothing to compare the list phrasing
# against. The honest record would be assessed=True (we did the work and the work
# terminated in "no source exists"), drifted=None (no verdict is possible), but
# build.py forbids that pair. Recorded as unassessed rather than inventing a
# comparand. See the summary returned with this file: the schema arguably needs a
# fourth state, e.g. assessed="no_source".
"E17": dict(assessed=False, drifted=None, list_phrasing=None,
            source_wording=None, drift_type=None, note=None),
}
