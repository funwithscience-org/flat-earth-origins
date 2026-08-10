# -*- coding: utf-8 -*-
"""
Fail-loud invariants for the provenance dataset and the rendered page.

House rule (carried from the sibling reviews): every numeric claim on the page must be
derived from the dataset, and every derived number must be asserted here. If you add a
new figure to docs/index.html, add a check for it below. Claims without tests rot.

Run:  python3 tests/test_provenance.py     (or tests/run.sh)
"""
import json, os, re, sys, html, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))

from corpus import ITEMS            # noqa: E402
from clusters import CLUSTERS       # noqa: E402
from assign import ASSIGN           # noqa: E402

FAILURES = []


def check(label, cond, detail=""):
    if cond:
        print(f"  PASS  {label}")
    else:
        print(f"  FAIL  {label}  {detail}")
        FAILURES.append(label)


D = json.load(open(os.path.join(ROOT, "data", "flat-earth-origins-provenance.json"),
                   encoding="utf-8"))
S, ROWS = D["summary"], D["items"]
PEOPLE, WORKS, ARGS = D["people"], D["works"], D["arguments"]
PAGE = open(os.path.join(ROOT, "docs", "index.html"), encoding="utf-8").read()
ADVOCATE = json.load(open(os.path.join(ROOT, "review", "advocate.json"), encoding="utf-8"))

print("\n[1] corpus integrity")
check("corpus holds exactly 461 items", len(ITEMS) == 461, len(ITEMS))
check("every item 1..461 is assigned", set(ASSIGN) == set(range(1, 462)),
      sorted(set(range(1, 462)) - set(ASSIGN))[:5])
check("no item assigned to an undefined cluster",
      not {c for c in ASSIGN.values() if c not in CLUSTERS})
check("no cluster defined but unused", not (set(CLUSTERS) - set(ASSIGN.values())),
      sorted(set(CLUSTERS) - set(ASSIGN.values())))
check("dataset row count matches corpus", len(ROWS) == 461, len(ROWS))
check("item 461 is flagged truncated in source", "truncated" in ITEMS[460].lower())

print("\n[2] cluster schema")
REQUIRED = {"lane", "name", "originator", "originator_work", "year",
            "real_source", "verdict", "note"}
OPTIONAL = {"pre_modern"}   # a third origin state; see the clusters.py docstring
VERDICTS = {"REFUTED", "STANDARD PHYSICS", "SELF-CONTRADICTED",
            "MISLEADING", "UNFALSIFIABLE", "NOT DEMONSTRATED"}
bad_schema = [c for c, k in CLUSTERS.items() if not REQUIRED <= set(k) <= REQUIRED | OPTIONAL]
check("every cluster carries the full field set", not bad_schema, bad_schema[:3])
bad_verdict = [c for c, k in CLUSTERS.items() if k["verdict"] not in VERDICTS]
check("every verdict is one of the six", not bad_verdict, bad_verdict[:3])
check("no verdict left PENDING",
      not [c for c, k in CLUSTERS.items() if k["verdict"] == "PENDING"])
no_note = [c for c, k in CLUSTERS.items() if not (k["note"] or "").strip()]
check("every cluster states a basis", not no_note, no_note[:3])
# an attributed cluster must name the work, not just the person
half = [c for c, k in CLUSTERS.items() if k["originator"] and not k["originator_work"]]
check("every named originator has a cited work", not half, half[:3])
dated = [c for c, k in CLUSTERS.items() if k["originator_work"] and not k["year"]]
check("every cited work has a year", not dated, dated[:3])

print("\n[3] derived headline numbers")
n_clusters = len(set(ASSIGN.values()))
check("distinct arguments == 98", n_clusters == 98, n_clusters)
check("summary agrees with recomputed cluster count",
      S["distinct_arguments"] == n_clusters)
named = {k["originator"] for k in CLUSTERS.values() if k["originator"]}
# 20 -> 19 on 2026-08-09: "Mircea Eliade (misapplied)" was withdrawn from D04/D05. He
# introduced nothing into the flat-earth canon - he reported how myths structure sacred
# space and said the multiplicity of centres raises no difficulty - so naming him an
# ORIGINATOR put a real scholar on the People tab as author of a flat-earth argument.
# He is in `real_source` now, which is the field for whose genuine work is being cited.
check("named originators == 19", len(named) == 19, sorted(named))
traced = sum(1 for r in ROWS if r["originator"])
# 366 -> 372 on 2026-08-08: ARG-E13 was recorded as untraced and the audit found an
# originator (Sungenis & Bennett), moving its 6 items into the traced column.
# 372 -> 356 on 2026-08-09: C02's attribution was withdrawn entirely. The sun-motion
# proof-texts have no modern originator - Bellarmine deploys Ecclesiastes 1:5 in 1615 -
# so its 16 items moved OUT of traced into the new pre-modern bucket. They did NOT
# become untraced, which stays at 89. Three buckets now, and they must sum to 461.
check("traced items == 348", traced == 348, traced)   # -8, D04+D05, per above
check("the three origin buckets account for every item",
      traced + S["pre_modern_items"]
      + (S["total_items"] - traced - S["pre_modern_items"]) == S["total_items"])
check("untraced accounts for the rest (97)",
      S["total_items"] - traced - S["pre_modern_items"] == 97,
      S["total_items"] - traced - S["pre_modern_items"])
check("summary traced count agrees",
      S["items_traceable_to_a_named_originator"] == traced)
check("compression ratio == 4.7", abs(S["compression_ratio"] - 4.7) < 0.05,
      S["compression_ratio"])

lane = collections.Counter(r["lane"] for r in ROWS)
EXPECT_LANE = {"A-EXP": 101, "A-REL": 81, "B": 54, "C": 69, "D": 83, "E": 73}
check("lane item counts match published figures", dict(lane) == EXPECT_LANE, dict(lane))
check("lane counts sum to 461", sum(lane.values()) == 461)

verdict = collections.Counter(r["verdict"] for r in ROWS)
EXPECT_VERDICT = {"REFUTED": 95, "UNFALSIFIABLE": 92, "STANDARD PHYSICS": 90,
                  "MISLEADING": 88, "NOT DEMONSTRATED": 63, "SELF-CONTRADICTED": 33}
check("verdict item counts match published bars",
      dict(verdict) == EXPECT_VERDICT, dict(verdict))
check("verdict counts sum to 461", sum(verdict.values()) == 461)

orig = collections.Counter(r["originator"] for r in ROWS if r["originator"])
check("Rowbotham == 65 items", orig["Samuel Rowbotham"] == 65,
      orig["Samuel Rowbotham"])
sungenis = sum(v for k, v in orig.items() if k.startswith("Robert Sungenis"))
check("Sungenis across all bylines == 134 items", sungenis == 134, sungenis)  # +6 from E13
check("Rowbotham + Sungenis == 43% of the list",
      round((65 + sungenis) / 461 * 100) == 43, (65 + sungenis) / 461 * 100)
check("largest cluster R08 == 28 items",
      collections.Counter(ASSIGN.values())["R08"] == 28)
check("exact duplicate pairs == 3", S["exact_duplicate_pairs"] == 3)

print("\n[4] page/dataset consistency")
# every figure asserted above must actually appear in the rendered page
# Bare-number needles are a trap. ">20<" passed for two days after the author count
# became 19, because it matched a table cell holding an ITEM count of 20. Six tests in
# this suite have now been retargeted for pinning a string that meant something else.
# RULE: assert a number together with the words that give it its meaning, and derive
# the number from the corpus rather than typing it.
for label, needle in [
    ("headline 461", f'{S["total_items"]} items'),
    ("headline 98 arguments", f'{S["distinct_arguments"]}</strong>'),
    ("author count in context", f'{S["named_originators"]} named'),
    ("traced in context", f'{S["items_traceable_to_a_named_originator"]} of them trace'),
    ("traced 348", "348 of the 461"),
    ("compression 4.7x", "4.7&times;"),
    ("family A total 182", "<strong>182</strong>"),
    ("family B total 54", "<strong>54</strong>"),
]:
    check(f"page states {label}", needle in PAGE, needle)

for v in VERDICTS:
    check(f"page renders a bar for {v}", f">{v}</span>" in PAGE)

# NB: "placeholder" occurs legitimately in prose (A22: "not a placeholder").
# Test for the scaffold's own markers, not the word.
check("page carries no leftover scaffold placeholder markers",
      "DRAFT / PLACEHOLDER" not in PAGE
      and "illustrative placeholder" not in PAGE.lower()
      and "Writeup instance" not in PAGE
      and "fill here" not in PAGE.lower())
check("verdict_challenge present on every full-depth argument",
      all("verdict_challenge" in (a.get("deep") or {})
          for a in ARGS.values() if a["depth"] == "full"))
_chal = [a["id"] for a in ARGS.values()
         if (a.get("deep") or {}).get("verdict_challenge", {}).get("challenged")]
check(f"challenged verdicts carry a proposal and reasoning ({len(_chal)} challenged)",
      all((a["deep"]["verdict_challenge"].get("proposed_verdict")
           and a["deep"]["verdict_challenge"].get("reasoning"))
          for a in ARGS.values()
          if (a.get("deep") or {}).get("verdict_challenge", {}).get("challenged")))
check("page logs the family-count correction",
      "Correction:" in PAGE and "overestimated" in PAGE)
check("page names the specimen and retrieval date",
      "withthesun33.com/about-1" in PAGE and "2 August 2026" in PAGE)
check("canonical URL matches the repo slug (funwithscience.net/flat-earth-origins/)",
      PAGE.count("https://funwithscience.net/flat-earth-origins/") == 3
      and "spinning-ball-review" not in PAGE,
      PAGE.count("https://funwithscience.net/flat-earth-origins/"))
check("page keeps the claims-not-people disclaimer",
      "does not target any individual" in PAGE)
check("structural: tables balanced",
      len(re.findall(r"<table", PAGE)) == len(re.findall(r"</table>", PAGE)))
check("structural: sections balanced",
      len(re.findall(r"<section", PAGE)) == len(re.findall(r"</section>", PAGE)))

print("\n[4b] corpus cross-references")
for pid, p in PEOPLE.items():
    check(f"{pid} works all resolve", all(w in WORKS for w in p["works"]))
check("every work has a resolvable author",
      all(w["author"] in PEOPLE for w in WORKS.values()))
check("every argument's originator_id resolves",
      all(a["originator_id"] in PEOPLE for a in ARGS.values() if a["originator_id"]))
deep = [a for a in ARGS.values() if a["depth"] == "full"]
check("at least one argument at full depth", len(deep) >= 1, len(deep))
for a in deep:
    d = a["deep"]
    # T3-unattributed arguments have no passage; they owe an `untraceable` explanation
    if d.get("passage") is None:
        check(f"{a['id']} (no passage) explains its untraceability",
              bool(d.get("untraceable")))
        check(f"{a['id']} untraceable text concedes our own research limit",
              "not that none exists" in d.get("untraceable", ""))
    else:
        check(f"{a['id']} passage cites a known work", d["passage"]["work"] in WORKS)
        check(f"{a['id']} in-copyright quote stays short (fair use)",
              d["passage"]["pd"] or len(d["passage"]["quote"].split()) <= 60,
              len(d["passage"]["quote"].split()))
    check(f"{a['id']} steelman has both halves",
          bool(d["steelman"]["description"]) and bool(d["steelman"]["why_it_doesnt_save_claim"]))
    sv = ADVOCATE["entries"][a["id"]]["survives"]
    check(f"{a['id']} advocate rating is 1-5", isinstance(sv, int) and 1 <= sv <= 5, sv)
    check(f"{a['id']} advocate >=3 carries a preemptive fix",
          sv < 3 or bool(ADVOCATE["entries"][a["id"]].get("preemptive")))
    check(f"{a['id']} related args all resolve",
          all(f"ARG-{r}" in ARGS for r in d.get("related", [])))
    check(f"{a['id']} people all resolve", all(x in PEOPLE for x in d.get("people", [])))
    check(f"{a['id']} cites at least 3 sources", len(d.get("sources", [])) >= 3)
worked = [p for p in PEOPLE.values() if p["bio_status"] == "worked"]
check("at least one biography worked", len(worked) >= 1, len(worked))
for p in worked:
    for f in ("formation", "had", "ignored", "legacy"):
        check(f"{p['id']} has {f}", bool(p.get(f)))
    check(f"{p['id']} has a kernel with both halves",
          bool(p["kernel"]) and bool(p["kernel"]["why_it_doesnt_save_claim"]))
    check(f"{p['id']} cites sources", len(p.get("sources", [])) >= 2)
check("every person carries at least one source",
      all(p.get("sources") for p in PEOPLE.values()),
      [p["id"] for p in PEOPLE.values() if not p.get("sources")])

print("\n[4c] tab shell + deep-linking")
body = PAGE.split("<body>", 1)[1]
page_ids = set(re.findall(r'\bid="([^"]+)"', body))
page_links = set(re.findall(r'href="#([^"]+)"', body))
dead = sorted(page_links - page_ids)
check("every internal anchor resolves to a defined id", not dead, dead[:6])
script = body.split("<script>", 1)[1] if "<script>" in body else ""
markup = body.split("<script>", 1)[0]
panels = set(re.findall(r'class="ds-tab-content[^"]*"\s+id="([^"]+)"', markup))
buttons = set(re.findall(r'data-tab="([^"]+)"', markup))
check("every tab button targets a real panel", buttons <= panels, sorted(buttons - panels))
check("every panel has a button", panels <= buttons, sorted(panels - buttons))
check("five tabs rendered", len(panels) == 5, sorted(panels))
check("no inline onclick anywhere (dome retired it)", "onclick" not in body)
check("delegated anchor handler present", 'a[href^="#"]' in script)
check("expandToElement present (deep links open ancestor details)",
      "expandToElement" in script)
check("popstate handler present", "popstate" in script)
check("skipHash/skipScroll contract present",
      "skipHash" in script and "skipScroll" in script)
check("theme is pinned light (no dark media query)",
      "prefers-color-scheme" not in PAGE)
check("print rule still unhides tab panels", "ds-tab-content{display:block!important}" in PAGE)
check("details/table markup balanced",
      body.count("<details") == body.count("</details>")
      and body.count("<table") == body.count("</table>"))

# NB: the substring "advocate" legitimately appears in a Library of Congress
# source title ("The Flat Earth and its Advocates"). Test for the panel, not the word.
check("advocate mode panel is INTERNAL - never rendered to the page",
      "Advocate mode" not in PAGE and "Best defence available" not in PAGE
      and "defense_survives" not in PAGE and "best_defense" not in PAGE)
check("advocate mode is stripped from the published corpus",
      not any("advocate" in (a.get("deep") or {}) for a in ARGS.values()))
check("every full-depth argument still has an internal advocate record",
      all(a["id"] in ADVOCATE["entries"] for a in ARGS.values() if a["depth"] == "full"))

_r01 = ARGS["ARG-R01"]
if _r01["depth"] == "full":
    _rt = json.dumps(_r01["deep"])
    check("R01 concedes general covariance without hedging",
          "no preferred frame in general relativity" in _rt)
    # The phrase "relativity forbids an Earth-fixed frame" appears in R01's
    # straw_man field as the error to AVOID. Test the refutation, which is what
    # a reader sees as our position, and test for the concession being present.
    _rr = _r01["deep"]["refutation"]
    check("R01 refutation states outright that an Earth-fixed chart is legitimate",
          "Anyone answering this argument by asserting that physics forbids an "
          "Earth-fixed frame is wrong" in _rr)
    check("R01 refutation does not assert a preferred frame exists in GR",
          "general relativity has a preferred frame" not in _rr)
    check("R01 carries the Kretschmann cuts-both-ways move", "Kretschmann" in _rt)
    check("R01 carries the relabelling-vs-different-model crux",
          "not a rival model" in _rt or "relabelling" in _rt.lower())
    check("R01 notes the equivalence concession costs them the rest of the list",
          "withdraw every experimental item" in _rt
          or "own refutation side by side" in _rt)
check("no treatment cites the superseded Bouw source (see corrections entry 1)",
      "geocentric-gobbledegook" not in json.dumps(ARGS),
      "creation.com/geocentric-gobbledegook is Faulkner on Marshall Hall, not Bouw")

print("\n[5] attribution guards (see claude/source-genealogy.md)")
# claims the research flagged as unverified must not appear as fact
check("does not assert Carpenter 1885 as provably the FIRST numbered list",
      "the first numbered" not in PAGE.lower())
check("uses 'earliest documented use' for Airy's failure coinage",
      "earliest documented use" in PAGE)
check("does not name Nathan Oakley (no citable source)",
      "Oakley" not in PAGE)
check("does not name Paul Ellwanger (not a geocentrist)",
      "Ellwanger" not in PAGE)
check("does not claim Dubay plagiarised",
      "plagiar" not in PAGE.lower())
# E01 (CMB axis of evil) is a designated careful case. Whatever depth it is
# rendered at, the page must concede the significance debate is unresolved —
# overclaiming here would be this review's own worst error.
_e01 = ARGS["ARG-E01"]
_concede = ("genuinely open" in PAGE or "live question in cosmology" in PAGE)
check("CMB careful case concedes the debate is unresolved", _concede)
check("CMB basis text still carries the CAREFUL CASE marker",
      "CAREFUL CASE" in _e01["basis"])
if _e01["depth"] == "full":
    _t = json.dumps(_e01["deep"])
    check("E01 states plainly that the anomaly is NOT resolved",
          "have not been resolved" in _t or "unresolved" in _t)
    check("E01 does not claim the anomaly is debunked or explained away",
          "anomaly is debunked" not in _t and "have been explained away" not in _t)
    # NB: check the REFUTATION, not the whole deep record — advocate text is
    # stripped from the published corpus, so phrases living only there will miss.
    _ref = _e01["deep"]["refutation"]
    check("E01 refutation carries the ecliptic/local-frame argument",
          "ecliptic" in _ref and "points inward" in _ref)
    check("E01 carries the axis-is-not-a-centre argument",
          "axis is not a centre" in _t.lower() or "not a centre" in _t.lower())
    check("E01 represents the pro-anomaly camp by name",
          "Starkman" in _t and "Schwarz" in _t)
check("all four careful cases are present in the corpus",
      all(f"ARG-{c}" in ARGS for c in ("A03", "A02", "R01", "E01")))

# ---------------------------------------------------------------------
print("\n[6] the hedge rule — refute the source, not the list's compression")

_deep = {a: r for a, r in ARGS.items() if r["deep"]}
check("every full treatment carries a compression record",
      all("compression" in r["deep"] for r in _deep.values()))

_assessed = {a: r["deep"]["compression"] for a, r in _deep.items()
             if r["deep"]["compression"]["assessed"] is True}
_nosrc = {a: r["deep"]["compression"] for a, r in _deep.items()
          if r["deep"]["compression"]["assessed"] == "no_source"}
_drifted = {a: c for a, c in _assessed.items() if c["drifted"]}

check("the published hedge-check count matches the corpus",
      S["hedge_checked"] == len(_assessed) and S["hedge_drifted"] == len(_drifted)
      and S["hedge_no_source"] == len(_nosrc),
      (S["hedge_checked"], len(_assessed), S["hedge_drifted"], len(_drifted)))
check("'no source' is counted apart from 'not yet checked'",
      all(a not in _assessed for a in _nosrc))
check("a no-source entry records where the search stopped",
      all(c["note"] and c["drifted"] is None for c in _nosrc.values()))
check("unassessed entries make no claim about faithfulness either way",
      all(r["deep"]["compression"]["drifted"] is None
          for r in _deep.values() if r["deep"]["compression"]["assessed"] is False))
check("every recorded drift shows the reader BOTH texts",
      all(c["list_phrasing"] and c["source_wording"] and c["note"]
          for c in _drifted.values()))
check("every recorded drift names a drift type",
      all(c["drift_type"] not in (None, "none") for c in _drifted.values()))

# The drift is a finding, not an internal note: if we recorded one it must reach
# the page. This is the check that stops the rule becoming a private spreadsheet.
for _a, _c in sorted(_drifted.items()):
    check(f"{_a}'s drift is published, not just recorded",
          html.escape(_c["list_phrasing"]) in PAGE)
check("the drift blocks render under an honest heading",
      _drifted == {} or "The list overstates its own source" in PAGE)

# The rule itself is a promise to the reader; it has to be visible so they can
# hold us to it. Losing this text in a restructure is how the promise rots.
check("the hedge rule is published on the Method tab",
      "Refute the source, not the summary" in PAGE)
check("the rule states the anti-strawman half",
      "at the strength they wrote it" in PAGE)
check("the rule states the no-escape-hatch half",
      "is not an escape hatch" in PAGE)

# --- the three mis-aimed refutations, fixed 2026-08-05 ---------------
# These regressed once already. Each check pins the SOURCE-facing move, so a
# future edit that drifts back to refuting the list's fragments turns them red.
_r08 = ARGS["ARG-R08"]["deep"]["refutation"]
check("R08 answers the book's conventionalism before the items",
      "conventional origin is not a conventional dynamics" in _r08)
check("R08 restores the condition on the Einstein/Infeld quotation",
      "<em>if</em> the laws of physics" in _r08 and "<em>then</em>" in _r08)
check("R08 states that the source names no instrument",
      "no instrument is named at all" in _r08)
check("R08 labels the 28 items as the list's addition, not the authors'",
      "the list&rsquo;s addition, not the" in _r08)
check("R08 does not open by refuting the fragments",
      _r08.index("what the book actually argues") < _r08.index("Kind 1"))

_r06 = ARGS["ARG-R06"]["deep"]["refutation"]
check("R06 concedes the source's sentence is correct",
      "What the source says is correct" in _r06)
# NB the wording moved on 2026-08-09 from "could not be found in the source" to
# "could not be located in the volume we were able to search" - the absence-claim
# rule requires naming the text searched. Test the INTENT (stated before anything is
# refuted) and the scoping, not one phrasing.
_r06_absence = _r06.find("could not be located in")
check("R06 scopes its unlocatable-titles claim to the text actually searched",
      _r06_absence > 0 and "volume we were able to search" in _r06)
check("R06 states the unlocatable titles BEFORE refuting any of them",
      0 < _r06_absence < _r06.index("Kind 1"))
# Test the three caveats themselves, not the sentence that used to carry them.
check("R06 keeps the caveats on that count",
      "multi-volume work" in _r06 and "OCR quality is variable" in _r06
      and "unable to re-run the search independently" in _r06)
check("R06 leaves the anthropic reversal unsettled rather than asserting it",
      "unsettled rather than claim a reversal" in _r06)
check("R06 attributes the remaining items to an unknown author",
      "whose author we do not know" in _r06)

_a10 = ARGS["ARG-A10"]["deep"]["refutation"]
check("A10 opens by stating that Rowbotham GRANTS co-rotation",
      "He claims the opposite" in _a10 and "the atmosphere revolves" in _a10)
check("A10 no longer argues for co-rotation as though it were disputed",
      "The atmosphere is inside the cabin." not in _a10)
# NB: the old wrong name is quoted once on the Method tab, in the disclosure of
# this very error. That occurrence must SURVIVE; only the live name must change.
check("A10's cluster name no longer states the reverse of its source",
      "co-rotate" not in ARGS["ARG-A10"]["name"]
      and "co-rotate" not in json.dumps(ARGS["ARG-A10"]["deep"]["tldr"]))
check("the Method tab still owns up to the old wrong name",
      "the atmosphere can&rsquo;t co-rotate" in PAGE)

# --- batch 6: family D and the Rowbotham audit -----------------------
for _a in ("ARG-D06", "ARG-D07", "ARG-B01", "ARG-B04", "ARG-A05"):
    check(f"{_a} is written in full", ARGS[_a]["depth"] == "full")
check("family D is no longer at zero coverage",
      any(r["depth"] == "full" for r in ARGS.values() if r["lane"] == "D"))

# The UNFALSIFIABLE lane is where we are most likely to sneer. This is the guard
# the social-section framing asks for, applied early to the two D treatments.
_dtext = json.dumps([ARGS[a]["deep"] for a in ("ARG-D06", "ARG-D07")]).lower()
for _bad in ("grift", "charlatan", "hoax", "gullible", "crackpot", "nonsense",
             "delusion", "ridiculous", "absurd belief", "obviously false"):
    check(f"family D avoids loaded word: {_bad!r}", _bad not in _dtext)
check("family D does not adjudicate whether God exists",
      "god does not exist" not in _dtext and "god is not real" not in _dtext
      and "proves there is no god" not in _dtext)

# The three edition corrections. Each was credited to a work that provably cannot
# contain the passage; a regression here means someone restored the old dating.
check("A05 is dated to the 1881 third edition, not 1865",
      ARGS["ARG-A05"]["originator_year"] == "1881")
check("B04 is dated to the 1881 third edition, not 1849",
      ARGS["ARG-B04"]["originator_year"] == "1881")
# NB: both treatments quote our old wrong line in order to withdraw it in public.
# Those occurrences must SURVIVE. What must not survive is the claim ASSERTED as
# fact, which lives in the cluster basis line.
check("the withdrawn pseudonym claim is no longer asserted as fact",
      "pseudonym from the thing he denied" not in ARGS["ARG-A05"]["basis"])
check("the withdrawn Book of Dzyan claim is no longer asserted as fact",
      "Dzyan" not in ARGS["ARG-D07"]["basis"])
check("both withdrawals are shown to the reader, not just made quietly",
      "pseudonym from the thing he denied" in PAGE and "Dzyan" in PAGE)
check("D07 credits Hall first, matching the items",
      ARGS["ARG-D07"]["originator"].startswith("Manly P. Hall"))

# Our own error rate is derived, never typed. If the log and the page disagree,
# the page is claiming an honesty it has not got.
check("the page states the derived correction count, not a literal",
      f'{S["arguments_with_a_correction"]} of the {S["arguments_at_full_depth"]}' in PAGE)
check("corrections log is not silently shrinking",
      S["corrections_logged"] >= 11, S["corrections_logged"])

# R01 is the calibration case: the wording barely moves, the speech act does.
if "ARG-R01" in _assessed:
    check("R01 is recorded as a concession repurposed as a proof",
          _assessed["ARG-R01"]["drift_type"] == "force_upgraded")
# A03 is the other calibration case: historiography restated as optics.
if "ARG-A03" in _assessed:
    check("A03 is recorded as a category shift, not a simple exaggeration",
          _assessed["ARG-A03"]["drift_type"] == "category_shifted")

# ---------------------------------------------------------------------
section = lambda t: print(f"\n{t}")
section("[7] guards from the curmudgeon sweep, 2026-08-09")
# The sweep found 45 confirmed defects and four SYSTEMIC patterns. Prose about a
# pattern rots; these are the patterns as executable checks. See
# review/CURMUDGEON-SWEEP-2026-08-09.md.

# --- Pattern: an edit lands on the wrong record ----------------------
# The E03 correction was applied to E01 because the two carried a byte-identical
# originator/work/year line and the edit replaced the first match. No total moved,
# so nothing went red. Pin the specific records that collided.
check("E01 keeps its own work record (the E03 edit landed here once)",
      ARGS["ARG-E01"]["originator_work"] == "The Principle (film)"
      and ARGS["ARG-E01"]["originator_year"] == "2014")
check("E03 carries the correction that was written for it",
      ARGS["ARG-E03"]["originator_year"] == "2013"
      and "Galileo Was Wrong" in ARGS["ARG-E03"]["originator_work"])

# --- Pattern: a corrected originator string with no PER-* mapping -----
# D07's originator was flipped Hall-first and ORIGINATOR_PID was not updated, so
# originator_id silently became None: the card printed "no named originator" above a
# TLDR naming Blavatsky, and the lineage totals were out by D07's twelve items.
_unmapped = [a["id"] for a in ARGS.values() if a["originator"] and not a["originator_id"]]
check("every named originator resolves to a person", not _unmapped, _unmapped)

# --- Pattern: a withdrawn claim still asserted somewhere --------------
# A retraction is worthless while the retracted sentence is still rendered. Each
# entry: the phrase, and how many times it may legitimately appear (the Method tab
# and corrections log QUOTE these in order to withdraw them - those must survive).
WITHDRAWN = [
    ("naming himself after the measurement", 0),   # PER-ROWBOTHAM formation
    ("pseudonym from the thing he denied", 1),     # Method tab owns up to it
    ("atmosphere can&rsquo;t co-rotate", 1),       # ditto
]
for _phrase, _allowed in WITHDRAWN:
    _n = PAGE.count(_phrase)
    check(f"withdrawn claim not re-asserted: {_phrase[:38]!r} ({_n}/{_allowed})",
          _n <= _allowed, _n)

# --- Pattern: absence asserted from a single passage ------------------
# Nine confirmed findings collapse into one rule: never write "the source does not
# contain X"; write "X is not located in [the text actually searched]". This is a
# RATCHET, not an allowlist - the current count is debt recorded in the sweep report,
# and it may fall but never rise.
#
# EXTENDED 2026-08-09 after the batch-8 sweep. The rule held nowhere it was checked
# and failed in four of twelve targets — because the banned construction had MIGRATED
# INTO FIELDS THIS TEST DID NOT SCAN (`compression.note`, the cluster `note`) and into
# phrasings the regex did not match ("nobody has produced", "did not treat"). The
# sweep's verdict is worth keeping verbatim: *writers have learned the regex, not the
# rule.* That is the standing hazard with any lint aimed at prose — closing the two
# holes is cheap, but it does not make the next paraphrase safe, and a clean run here
# is not evidence that no unscoped absence claim was written.
_ABSENCE = [r"\bdoes not (?:contain|mention|cite|occur|appear|use|say|treat|discuss)\b",
            r"\bdo not (?:contain|mention|cite|occur|appear|treat)\b",
            r"\bdid not (?:treat|mention|discuss|address)\b",
            r"\bnever (?:mentions|cites|uses|wrote|says|appears|treats)\b",
            # Narrowly aimed. A first cut used a bare `\bnobody (has|in|ever)\b` and it
            # fired on four rhetorical uses that assert nothing about a source at all
            # ("descends from nobody in particular", "nobody hedged it"). That matters
            # more than the false-positive count: a lint that cries wolf is precisely
            # what teaches writers to paraphrase around it, which is the failure this
            # extension was written to fix. So match the CLAIM SHAPE — nobody has
            # produced / published / is on record — not the word "nobody".
            r"\bnobody (?:\w+ ){0,4}?(?:has |is |are )?(?:produced|published|is on record|are on record|obtained)\b",
            r"\bno one (?:\w+ ){0,4}?(?:has )?(?:produced|published|obtained|is on record)\b",
            r"\bnowhere (?:in|does|appears)\b", r"\bcontains none of\b", r"\bis absent from\b"]
# A claim about OUR OWN corpus is already scoped: "not in the 461 items" names the
# exact text searched, and the reader has it on the Claims tab to check. Those were
# always meant to be allowed — the original ceiling of 4 was described as mostly this
# class — but the regex had no way to say so, so they were being counted as debt.
_SCOPE = re.compile(r"not located|text searched|full text|as quoted|scanned|the \d{4}|ed\.|"
                    r"edition|Vol\.|volume|ch\.|chapter|p{1,2}\.\s?\d|pamphlet|the PDF|"
                    r"we could read|searched|the 461 items|200 Proofs|"
                    r"the specimen|this corpus|our corpus", re.I)
_unscoped = 0
for _a in ARGS.values():
    _d = _a.get("deep")
    if not _d:
        continue
    # `compression.note` and the cluster `note` are added because that is exactly where
    # the constructions went once the four original fields were policed. Both render to
    # the reader, so an unscoped claim there costs the same as one in the refutation.
    _blocks = [_d.get("tldr") or "", _d.get("refutation") or "", _d.get("untraceable") or "",
               (_d.get("passage") or {}).get("gloss") or "",
               (_d.get("compression") or {}).get("note") or "",
               _a.get("note") or ""]
    for _t in _blocks:
        if not isinstance(_t, str):
            continue
        for _p in _ABSENCE:
            for _m in re.finditer(_p, _t, re.I):
                if not _SCOPE.search(_t[max(0, _m.start() - 160):_m.end() + 160]):
                    _unscoped += 1
# --- the pre-modern origin state ------------------------------------
# C02's attribution was corrected twice and then withdrawn: Carpenter was wrong,
# Skiba was wrong the other way, and substituting Bouw was rejected on verification
# as repeating the error one step upstream. Some arguments are simply older than
# anyone we could name. Guard the state so it cannot decay back into a false credit.
_pm = {a["id"]: a["pre_modern"] for a in ARGS.values() if a.get("pre_modern")}
check("pre-modern arguments credit nobody as originator",
      all(ARGS[a]["originator"] is None for a in _pm), list(_pm))
check("each pre-modern argument cites an earliest DOCUMENTED use",
      all(p.get("earliest_documented_use") for p in _pm.values()))
check("pre-modern never claims to have found the FIRST use",
      all("first " not in p["earliest_documented_use"].lower() for p in _pm.values()))
check("C02 is recorded as older than the movement, not credited to a modern author",
      "ARG-C02" in _pm and ARGS["ARG-C02"]["originator"] is None)
check("C02 names the repopularisers who carried it, without calling them authors",
      len(_pm.get("ARG-C02", {}).get("repopularised", [])) >= 2)
check("the page renders the pre-modern state rather than a blank",
      "older than the movement" in PAGE and "Listed as distributors, not authors" in PAGE)

# 11 -> 4 on 2026-08-09 after the sweep-application pass rescoped seven of them.
#
# 2026-08-09, later: the batch-8 sweep found the rule failing in 4 of 12 targets while
# this counter sat at 4, because the constructions had moved into fields the check did
# not read. Widening the net took the true count to 16; tightening two over-eager new
# patterns and teaching _SCOPE that "the 461 items" IS a named text took it to 8; and
# rewriting the four genuine offenders (A05, A07, R01, R04 — the same ones the sweep
# confirmed) took it back to 4. The number is unchanged and means something different:
# it was measuring less than it claimed to before.
#
# The 4 that remain are the regex's limits rather than writing faults, and are recorded
# here so nobody spends an afternoon rediscovering them:
#   D07  "anything it does not say can be assigned to the inner teaching" — describes
#        the unfalsifiability structure; asserts nothing about any source. A false hit.
#   R06  "'Spontaneous symmetry breaking' does not occur in it" — a word-count search of
#        a named document, evidenced by the neighbouring "occurs three times".
#   C04  "absent from Skiba's teaching document" — names the text; the scope is the
#        sentence, which is what the rule asks for, just not in words _SCOPE knows.
#   C05  "the verses do not contain" — the verses are enumerated a paragraph earlier.
# Chasing these to zero would mean tuning the regex until the number looks good, which
# is the opposite of the point.
#
# RATCHET: this number goes down, never up.
UNSCOPED_CEILING = 4
check(f"unscoped absence-claims do not increase ({_unscoped}/{UNSCOPED_CEILING})",
      _unscoped <= UNSCOPED_CEILING, _unscoped)

# ---------------------------------------------------------------------
print("\n[8] the two clocks — the Overview's dating argument")
# The Overview now makes a claim of its own rather than just tallying: the experiments
# this tradition cites stop in the 1930s, and everything cited after 1950 is other
# people's astronomy reinterpreted. Every figure in that section is derived in build.py
# from each cluster's `real_source`, so it moves when the dataset moves. These checks
# exist so it cannot move SILENTLY — the prose around the numbers would go stale first.
_cw = S["cited_work_years"]
check("dated-work window spans Bellarmine to the present",
      _cw["earliest"] == 1615 and _cw["latest"] >= 2020, _cw)
check("median year of cited work is 1933 (Miller's aether drift)",
      S["cited_work_median_year"] == 1933, S["cited_work_median_year"])
check("cited-work median is pre-war, which is the whole point of the section",
      S["cited_work_median_year"] < 1950)
# THE PRE-1930 SHARE IS A MOVING NUMBER AND THE PROSE MUST TRACK IT BOTH WAYS.
# History: written first as "pre-1930 is a majority" and it failed — 53 of 107 was one
# item SHORT of half — so it became a guard against writing "most". Then the batch-8
# repair pass corrected B06's and D11's years and gave C07 its Bellarmine citation, more
# clusters became datable, and the share crossed 50%. Re-pinning a new literal pair would
# just queue up the same failure next time.
#
# So assert the INVARIANT instead of the snapshot: the page's wording must agree with the
# arithmetic in whichever direction the arithmetic currently runs. Under half, "most" is
# forbidden. Over half, the page is free to say it — but it must not still be hedging as
# though it were under, because that is the same defect pointing the other way.
_p30, _pdated = S["items_citing_pre1930_work"], S["items_citing_dated_work"]
_share = _p30 / _pdated
_claims_most = "most of those items rest" in PAGE.lower()
check(f"pre-1930 share is a real fraction of the dated set ({_p30}/{_pdated} = {_share:.0%})",
      0.35 <= _share <= 0.75, _share)
check("page's wording matches which side of half the share falls on",
      _claims_most == (_share >= 0.5), (round(_share, 3), _claims_most))
# render.py picks the sentence form from the arithmetic, so pin whichever branch is live.
_pair = (f'before 1930: {_p30} of {_pdated}' if _share >= 0.5
         else f'{_p30} of those {_pdated} items rest')
check("page states the pre-1930 pair exactly as the dataset computes it",
      _pair in PAGE, (_p30, _pdated, _pair))
# The load-bearing claim: post-1950 citations are not experiments. If a NON-lane-E
# cluster ever acquires a post-1950 real_source, "nine of ten are misappropriated
# astronomy" stops being true and the paragraph has to be rewritten, not renumbered.
check("R12 is the only post-1950 citation outside misappropriated astronomy",
      S["post1950_all_lane_E_except"] == ["R12"], S["post1950_all_lane_E_except"])
check("post-1950 group stays small enough for the paragraph's framing",
      8 <= len(S["post1950_cited_clusters"]) <= 12, S["post1950_cited_clusters"])
# Page-side: assert each number WITH the words that give it meaning (the [4] rule).
# The spelled-out counts go through render.w() in the page, so DERIVE THE WORD HERE TOO
# rather than typing "Twenty-seven". A literal in the test is the same rot as a literal
# in the page — it just fails a commit later, when the cause is harder to see.
sys.path.insert(0, os.path.join(ROOT, "scripts"))
from render import w as _w                                              # noqa: E402
_n50 = len(S["post1950_cited_clusters"])
_nE = _n50 - len(S["post1950_all_lane_E_except"])
for label, needle in [
    ("median cited year", f'median year of that work is {S["cited_work_median_year"]}'),
    ("pre-1930 item count", _pair),   # same live branch as the check above
    ("dated-argument count spelled out",
     f'{_w(S["cited_work_years"]["clusters"], cap=True)} arguments cite a dated piece'),
    # Rewritten 2026-08-10 after the Overview audit: "nine of ten" was an artifact of
    # first-year dating. Only the lane-E count is stable across both readings, so only it
    # is stated flatly; both denominators are published as a range.
    ("post-1950 lane-E count",
     f'{_w(S["post1950_lane_E_count"], cap=True)} arguments cite post-1950 work'),
    ("both datings published as a range",
     f'{len(S["post1950_cited_clusters"])} by the earlier date, '
     f'{len(S["post1950_by_last_year"])} by the later one'),
]:
    check(f"two-clocks section states {label}", needle in PAGE, needle)
# WITHDRAWN 2026-08-10. The page used to claim the tradition "has not produced a new
# experiment in about ninety years". The Overview audit showed the chronology could not
# carry it — every experiment in that list was run by an outsider, so it measured citation
# and not production — and The Final Experiment (Union Glacier, December 2024) falsifies
# the interval outright. The replacement claim is stronger and checkable: the authority is
# borrowed, the movement's own experiments are few, and the modern ones went against it.
check("page does NOT reinstate the withdrawn ninety-year claim",
      "not produced a new experiment in about ninety years" not in PAGE)
check("page states the borrowed-authority claim that replaced it",
      "experimental authority in this tradition is almost entirely borrowed" in PAGE.lower()
      or "Every one of those experiments was run by someone outside the movement" in PAGE)
check("page carries the movement's own experiments, both ends",
      "Bedford Level in 1838" in PAGE and "Wallace" in PAGE and "Oldham" in PAGE)
check("page carries The Final Experiment and what it returned",
      "The Final Experiment" in PAGE and "Union Glacier" in PAGE
      and "Campanella" in PAGE and "midnight sun" in PAGE)
check("Knodel is described as a sound DESIGN, not a competently run measurement",
      "competently run" not in PAGE and "a sound design" in PAGE,
      "ARG-A07 declines to lean on the reading as data; the Overview must not either")
check("the Knodel paragraph carries A07's own caveat rather than asserting past it",
      "reported figure, not a documented measurement" in PAGE)
check("post-1950 design-intent claim is scoped, not blanket",
      "none of it was designed to be one" not in PAGE
      and "gathered to characterise the universe rather" in PAGE)
check("two-clocks section closes on Knodel, the one real experiment, and its result",
      "Knodel" in PAGE and "15 degrees per hour" in PAGE and "ARG-A07" in PAGE)
# The psychology section. It is argument, not arithmetic, so pin the concessions —
# these are the sentences most likely to be trimmed away by a later tightening pass,
# and without them the section is just an accusation.
check("persistence section concedes the steelman rather than only asserting",
      "heliocentrism does not refute human significance" in PAGE
      and "It declines to adjudicate it" in PAGE)
check("persistence section defines the fringe/denial boundary as a testable moment",
      "a prediction fails" in PAGE and "does not update" in PAGE)
check("persistence section names both lineages and their different needs",
      "zetetic" in PAGE.lower() and "Tychonian" in PAGE)

print()
if FAILURES:
    print(f"FAILED: {len(FAILURES)} check(s)\n  - " + "\n  - ".join(FAILURES))
    sys.exit(1)
print("All checks passed.")
