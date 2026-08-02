# -*- coding: utf-8 -*-
"""
Fail-loud invariants for the provenance dataset and the rendered page.

House rule (carried from the sibling reviews): every numeric claim on the page must be
derived from the dataset, and every derived number must be asserted here. If you add a
new figure to docs/index.html, add a check for it below. Claims without tests rot.

Run:  python3 tests/test_provenance.py     (or tests/run.sh)
"""
import json, os, re, sys, collections

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
VERDICTS = {"REFUTED", "STANDARD PHYSICS", "SELF-CONTRADICTED",
            "MISLEADING", "UNFALSIFIABLE", "NOT DEMONSTRATED"}
bad_schema = [c for c, k in CLUSTERS.items() if set(k) != REQUIRED]
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
check("traced items == 366", traced == 366, traced)
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
check("Sungenis across all bylines == 128 items", sungenis == 128, sungenis)
check("Rowbotham + Sungenis == 42% of the list",
      round((65 + sungenis) / 461 * 100) == 42, (65 + sungenis) / 461 * 100)
check("largest cluster R08 == 28 items",
      collections.Counter(ASSIGN.values())["R08"] == 28)
check("exact duplicate pairs == 3", S["exact_duplicate_pairs"] == 3)

print("\n[4] page/dataset consistency")
# every figure asserted above must actually appear in the rendered page
for label, needle in [
    ("headline 461", "461"),
    ("headline 98 arguments", ">98<"),
    ("headline 20 authors", ">20<"),
    ("traced 366", "366 of the 461"),
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
check("all four careful cases are present in the corpus",
      all(f"ARG-{c}" in ARGS for c in ("A03", "A02", "R01", "E01")))

print()
if FAILURES:
    print(f"FAILED: {len(FAILURES)} check(s)\n  - " + "\n  - ".join(FAILURES))
    sys.exit(1)
print("All checks passed.")
