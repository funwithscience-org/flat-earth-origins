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


D = json.load(open(os.path.join(ROOT, "data", "spinning-ball-provenance.json"),
                   encoding="utf-8"))
S, ROWS = D["summary"], D["items"]
PAGE = open(os.path.join(ROOT, "docs", "index.html"), encoding="utf-8").read()

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
    ("R08 cluster size 28", "28 times"),
]:
    check(f"page states {label}", needle in PAGE, needle)

for v in VERDICTS:
    check(f"page renders a bar for {v}", f">{v}</span>" in PAGE)

check("page carries no leftover placeholder text",
      "placeholder" not in PAGE.lower())
check("page logs the family-count correction",
      "Correction:" in PAGE and "overestimated" in PAGE)
check("page names the specimen and retrieval date",
      "withthesun33.com/about-1" in PAGE and "2 August 2026" in PAGE)
check("page keeps the claims-not-people disclaimer",
      "does not target any individual" in PAGE)
check("structural: tables balanced",
      len(re.findall(r"<table", PAGE)) == len(re.findall(r"</table>", PAGE)))
check("structural: sections balanced",
      len(re.findall(r"<section", PAGE)) == len(re.findall(r"</section>", PAGE)))

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
check("CMB section concedes the debate is live",
      "live question in cosmology" in PAGE)

print()
if FAILURES:
    print(f"FAILED: {len(FAILURES)} check(s)\n  - " + "\n  - ".join(FAILURES))
    sys.exit(1)
print("All checks passed.")
