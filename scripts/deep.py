# -*- coding: utf-8 -*-
"""
DEEP — the full treatment for an argument, layered on top of its cluster record.

An argument with no DEEP entry renders at cluster depth (name, verdict, basis).
An argument WITH one renders the full pipeline:

    snippet  ->  original passage  ->  steelman  ->  refutation  ->  advocate

Schema:
  tldr               2-3 sentences, plain language, punchline first. ESCAPED on render.
  passage            {work, locator, quote, pd, gloss} - the claim in its own words.
                     pd=True  -> quote at length, link the scan
                     pd=False -> short fair-use excerpt only
  steelman           {description, why_it_doesnt_save_claim}
                     Aim for KERNEL tier, not SURFACE:
                       SURFACE - the easy bust anyone would make (usually wrong)
                       DEEPER  - true but incomplete
                       KERNEL  - name the specific true thing they found, then show
                                 the true thing points the other way
  refutation         raw HTML, the substantive answer
  advocate           {best_defense, survives (1-5), preemptive}
                     survives >= 3 obligates a concrete text change in `preemptive`
  straw_man          {identified: bool, detail: str|None} - do THEY misrepresent US
  people             [PER-*] ids implicated
  related            [ARG-*] ids
  sources            [{label, url}]
"""

DEEP = {

"A03": dict(
    verdict_challenge=dict(challenged=False, proposed_verdict=None,
                          reasoning=None),  # backfilled: predates the field
    tldr=("Airy filled a telescope with water and found stellar aberration unchanged. "
          "That null is exactly what Fresnel predicted before him and what relativity "
          "predicts today. Calling it a “failure” inverts what the experiment showed — "
          "and aberration exists at all only because the Earth moves."),

    passage=dict(
        work="WRK-VDK-1988", locator="subtitle, and ch. “The Unfailing Import of Airy's Failure”, p. 52",
        pd=False,
        quote=("In fact, this experiment was called “Airy's failure,” because it "
               "contradicted the heliocentric metaphysics. The term “Airy's failure” "
               "gives psychological insight to the thoughts of the experimenters "
               "during this era."),
        gloss=("Quoted from Sungenis &amp; Bennett, <em>Galileo Was Wrong</em> Vol. I, which "
               "inherits the phrase from van der Kamp. Note the passive voice — "
               "<em>was called</em> — and the claim about what Airy's contemporaries "
               "thought. Both are checkable, and both fail. Airy's own paper is titled "
               "neutrally: <em>“On a supposed alteration in the amount of Astronomical "
               "Aberration of light, produced by the passage of light through a "
               "considerable thickness of Refracting Medium,”</em> Proc. Roy. Soc. London "
               "(1871), pp. 35–39. It does not contain the word “failure.” The phrase is "
               "internal to the movement: its earliest documented use is van der Kamp's "
               "1988 subtitle, and Bouw's obituary credits him with the coinage by name.")),

    steelman=dict(
        description=(
            "The experiment is real, the null is real, and the reasoning behind it was "
            "sound for its moment. Wilhelm Klinkerfues, working from Thomas Young's "
            "stationary-aether theory, had argued that if aberration is caused by the "
            "Earth ploughing through a static aether, then slowing the light down inside "
            "the telescope should change the angle you must tilt it. Airy built the "
            "apparatus, mounted it in 1870, observed γ Draconis for two years, and found "
            "no change. Van der Kamp is also right about something more general and more "
            "serious: a null result cannot by itself distinguish “there is no motion” from "
            "“there is motion plus a compensating effect.” That is a real problem in "
            "philosophy of science, and it is the same underdetermination point Duhem and "
            "Quine made in more respectable company."),
        why_it_doesnt_save_claim=(
            "Because the null was <strong>predicted in advance, twice, by theories that "
            "assume the Earth moves</strong> — which is precisely the case underdetermination "
            "does not cover. Fresnel's dragging coefficient, published decades before Airy "
            "and already confirmed by Fizeau, says aether inside a medium of refractive "
            "index <em>n</em> is dragged at <em>v</em>(1 − 1/<em>n</em>²), exactly cancelling "
            "the slower light speed and restoring the vacuum angle. Special relativity gets "
            "the same result more cleanly: aberration is a transformation of the light ray's "
            "<em>direction</em> between frames, fixed by the relative velocity of source and "
            "observer, so a refracting medium downstream of that transformation cannot alter "
            "it. A result that two competing theories both predicted, and that a third "
            "(stationary aether) got wrong, is evidence against the third — not for a "
            "stationary Earth.")),

    refutation=(
        "<p>Three things have to be separated, because the argument depends on running "
        "them together.</p>"
        "<p><strong>1. What Airy measured.</strong> A null — no change in the aberration "
        "angle with a water-filled tube. Uncontested by anyone.</p>"
        "<p><strong>2. What the null rules out.</strong> Klinkerfues's stationary-aether "
        "prediction. That is a hypothesis about the <em>aether</em>, not about the Earth. "
        "Airy's result killed one aether model and left the Earth's motion untouched.</p>"
        "<p><strong>3. What aberration itself implies.</strong> This is the step the "
        "argument never takes, and it is fatal. Stellar aberration is the annual ~20.5″ "
        "elliptical wobble Bradley discovered in 1729, and it exists <em>because the "
        "observer is moving</em>. On a stationary Earth there is no relative velocity "
        "between source and observer, so there is no aberration to have a magnitude at "
        "all. The argument takes an experiment that measures a consequence of Earth's "
        "orbital motion, shows the magnitude is medium-independent, and reports this as "
        "evidence the Earth does not move. The phenomenon being measured is the "
        "refutation.</p>"
        "<p>The rebranding is the tell. An experiment whose result matched the standing "
        "prediction is not a failure in any sense a physicist would recognise; it is a "
        "confirmation. The word does no work except to make a confirmation sound like a "
        "scandal — and it entered the literature 117 years after the experiment, from "
        "outside physics.</p>"),

    advocate=dict(
        best_defense=(
            "You are being too quick. Fresnel drag is not an independent prediction — it is "
            "a coefficient reverse-engineered to save the aether theory from exactly this "
            "class of result, and Lorentz had to keep patching it. And your relativistic "
            "answer proves my point rather than yours: relativity explains the null by "
            "denying that absolute motion is detectable at all. If no experiment can detect "
            "absolute motion, then no experiment establishes that the Earth is absolutely "
            "moving either. You have not shown the Earth moves. You have shown the question "
            "cannot be settled — which is what geocentrists have been saying."),
        survives=4,
        preemptive=(
            "This defence is good enough that the page must answer it explicitly rather "
            "than leave it to the reader. Two responses, both already in the text above but "
            "worth stating in the body: (a) Fresnel's coefficient was not invented for Airy "
            "— Fizeau confirmed it experimentally in 1851, two decades earlier, on flowing "
            "water, so it is an independently tested prediction and not a patch; (b) the "
            "relativity point is conceded and does not help, because the claim on the list "
            "is not the modest “absolute motion is undetectable” but the specific "
            "“<em>this experiment shows the Earth is stationary</em>.” The modest claim is "
            "true and non-discriminating; the specific claim is false. The list needs the "
            "specific one and can only support the modest one. Cross-link this to "
            "<a href=\"#ARG-R01\">ARG-R01</a>, where the same trade is made explicitly.")),

    straw_man=dict(
        identified=True,
        detail=("The claim that the term reflects “the thoughts of the experimenters during "
                "this era” attributes to Airy and his contemporaries a dismay they left no "
                "record of. Airy reported a null against a hypothesis he was testing, in "
                "neutral language, in the ordinary way. The imputed embarrassment is "
                "supplied entirely by the phrase, coined 117 years later.")),

    people=["PER-VANDERKAMP", "PER-BOUW", "PER-SUNGENIS"],
    related=["A01", "A04", "A05", "R01", "R03"],

    sources=[
        dict(label="Airy 1871, Proc. Roy. Soc. London 20:35–39 — the original paper",
             url="https://en.wikipedia.org/wiki/Aberration_(astronomy)"),
        dict(label="van der Kamp, De Labore Solis (1988) — earliest documented use of the phrase",
             url="https://geocentricity.com/bibastron/ts_history/de_labore.pdf"),
        dict(label="Bouw's obituary crediting van der Kamp with the coinage",
             url="https://www.geocentricity.com/ba1/no084/obits.pdf"),
        dict(label="Fizeau experiment — Fresnel drag confirmed experimentally, 1851",
             url="https://en.wikipedia.org/wiki/Fizeau_experiment"),
        dict(label="Experimental basis of special relativity (Baez) — “in agreement with the prediction of SR”",
             url="https://math.ucr.edu/home/baez/physics/Relativity/SR/experiments.html"),
        dict(label="Royal Observatory Greenwich on Airy",
             url="https://www.royalobservatorygreenwich.org/articles.php?article=1069")]),
}

# ---- agent-written batches ------------------------------------------
from deep_batch1 import BATCH1
for _k, _v in BATCH1.items():
    assert _k not in DEEP, f"batch1 collides with a hand-written entry: {_k}"
    DEEP[_k] = _v
from deep_batch2 import BATCH2
for _k, _v in BATCH2.items():
    assert _k not in DEEP, f"batch2 collision: {_k}"
    DEEP[_k] = _v
