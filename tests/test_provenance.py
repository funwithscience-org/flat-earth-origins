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
check("named originators == 20", len(named) == 20, sorted(named))
traced = sum(1 for r in ROWS if r["originator"])
# 366 -> 372 on 2026-08-08: ARG-E13 was recorded as untraced and the audit found an
# originator (Sungenis & Bennett), moving its 6 items into the traced column.
# 372 -> 356 on 2026-08-09: C02's attribution was withdrawn entirely. The sun-motion
# proof-texts have no modern originator - Bellarmine deploys Ecclesiastes 1:5 in 1615 -
# so its 16 items moved OUT of traced into the new pre-modern bucket. They did NOT
# become untraced, which stays at 89. Three buckets now, and they must sum to 461.
check("traced items == 356", traced == 356, traced)
check("the three origin buckets account for every item",
      traced + S["pre_modern_items"]
      + (S["total_items"] - traced - S["pre_modern_items"]) == S["total_items"])
check("untraced did not absorb the pre-modern cluster (still 89)",
      S["total_items"] - traced - S["pre_modern_items"] == 89,
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
for label, needle in [
    ("headline 461", "461"),
    ("headline 98 arguments", ">98<"),
    ("headline 20 authors", ">20<"),
    ("traced 356", "356 of the 461"),
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
check("R06 states the six unlocatable titles BEFORE refuting any of them",
      _r06.index("could not be found in the source") < _r06.index("Kind 1"))
check("R06 keeps the caveats on that count",
      "not located in the scanned text" in _r06 and "OCR quality is variable" in _r06)
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
_ABSENCE = [r"\bdoes not (?:contain|mention|cite|occur|appear|use|say)\b",
            r"\bdo not (?:contain|mention|cite|occur|appear)\b",
            r"\bnever (?:mentions|cites|uses|wrote|says|appears)\b",
            r"\bnowhere (?:in|does|appears)\b", r"\bcontains none of\b", r"\bis absent from\b"]
_SCOPE = re.compile(r"not located|text searched|full text|as quoted|scanned|the \d{4}|ed\.|"
                    r"edition|Vol\.|volume|ch\.|chapter|p{1,2}\.\s?\d|pamphlet|the PDF|"
                    r"we could read|searched", re.I)
_unscoped = 0
for _a in ARGS.values():
    _d = _a.get("deep")
    if not _d:
        continue
    _blocks = [_d.get("tldr") or "", _d.get("refutation") or "", _d.get("untraceable") or "",
               (_d.get("passage") or {}).get("gloss") or ""]
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

UNSCOPED_CEILING = 11
check(f"unscoped absence-claims do not increase ({_unscoped}/{UNSCOPED_CEILING})",
      _unscoped <= UNSCOPED_CEILING, _unscoped)

print()
if FAILURES:
    print(f"FAILED: {len(FAILURES)} check(s)\n  - " + "\n  - ".join(FAILURES))
    sys.exit(1)
print("All checks passed.")
