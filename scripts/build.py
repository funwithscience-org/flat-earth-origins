# -*- coding: utf-8 -*-
"""Build the provenance dataset + summary statistics. Run from the repo root."""
import json, csv, collections, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
DATA = os.path.join(ROOT, "data")
from corpus import ITEMS
from clusters import CLUSTERS
from assign import ASSIGN

LANE_FAMILY = {"A-EXP": "A", "A-REL": "A", "B": "B", "C": "C", "D": "D", "E": "E"}
LANE_NAME = {
    "A-EXP": "A1 · Geocentric physics (experiments)",
    "A-REL": "A2 · Relativity & coordinate conventions",
    "B": "B · Flat-earth observations",
    "C": "C · Scriptural",
    "D": "D · Historical / esoteric",
    "E": "E · Misappropriated astronomy",
}

# ---- integrity checks -------------------------------------------------
assert len(ITEMS) == 461
assert set(ASSIGN) == set(range(1, 462)), "assignment must cover items 1..461"
missing = {c for c in ASSIGN.values() if c not in CLUSTERS}
assert not missing, f"assigned to undefined clusters: {sorted(missing)}"
unused = set(CLUSTERS) - set(ASSIGN.values())
assert not unused, f"clusters defined but never used: {sorted(unused)}"

# ---- build rows -------------------------------------------------------
rows = []
for n, text in enumerate(ITEMS, start=1):
    cid = ASSIGN[n]
    c = CLUSTERS[cid]
    rows.append({
        "item_no": n,
        "text": text,
        "family": LANE_FAMILY[c["lane"]],
        "lane": c["lane"],
        "cluster_id": cid,
        "cluster_name": c["name"],
        "originator": c["originator"],
        "originator_work": c["originator_work"],
        "originator_year": c["year"],
        "real_source_cited": c["real_source"],
        "verdict": c["verdict"],
    })

# ---- exact-duplicate detection ---------------------------------------
seen, dupes = {}, []
for r in rows:
    key = r["text"].strip().lower().rstrip(".")
    if key in seen:
        dupes.append((seen[key], r["item_no"], r["text"]))
    else:
        seen[key] = r["item_no"]

# ---- counts -----------------------------------------------------------
fam_items = collections.Counter(r["family"] for r in rows)
lane_items = collections.Counter(r["lane"] for r in rows)
lane_clusters = collections.Counter(CLUSTERS[c]["lane"] for c in set(ASSIGN.values()))
cluster_size = collections.Counter(ASSIGN.values())
verdict_items = collections.Counter(r["verdict"] for r in rows)
verdict_clusters = collections.Counter(CLUSTERS[c]["verdict"] for c in CLUSTERS)

# originator tally: items and clusters per named originator
orig_items = collections.Counter()
orig_clusters = collections.Counter()
for r in rows:
    orig_items[r["originator"] or "(no named originator)"] += 1
for cid, c in CLUSTERS.items():
    orig_clusters[c["originator"] or "(no named originator)"] += 1

named_items = sum(v for k, v in orig_items.items() if k != "(no named originator)")

# ---- lineage rollup ---------------------------------------------------
LINEAGE = {
    "Samuel Rowbotham": "Zetetic (flat-earth) lineage",
    "William Carpenter": "Zetetic (flat-earth) lineage",
    "Wilbur Glenn Voliva": "Zetetic (flat-earth) lineage",
    "Samuel Shenton": "Zetetic (flat-earth) lineage",
    "Charles K. Johnson": "Zetetic (flat-earth) lineage",
    "Eric Dubay": "Zetetic (flat-earth) lineage",
    "Mark Sargent": "Zetetic (flat-earth) lineage",
    "Rob Skiba": "Zetetic (flat-earth) lineage",
    "Bob Knodel": "Zetetic (flat-earth) lineage",
    "Walter van der Kamp": "Tychonian (geocentric) lineage",
    "Gerardus Bouw": "Tychonian (geocentric) lineage",
    "Robert Sungenis": "Tychonian (geocentric) lineage",
    "Robert Sungenis & Robert Bennett": "Tychonian (geocentric) lineage",
    "Robert Sungenis & Rick DeLano": "Tychonian (geocentric) lineage",
    "Marshall Hall": "Tychonian (geocentric) lineage",
    "Helena Blavatsky; Manly P. Hall": "Esoteric / Traditionalist literature",
    "William Walker Atkinson (as 'Three Initiates')": "Esoteric / Traditionalist literature",
    "Mircea Eliade (misapplied)": "Esoteric / Traditionalist literature",
    "Manly P. Hall": "Esoteric / Traditionalist literature",
    "Claudius Ptolemy (via the modern movement)": "Pre-modern astronomy",
}
lin_items = collections.Counter()
lin_clusters = collections.Counter()
for r in rows:
    lin_items[LINEAGE.get(r["originator"], "(no named originator)")] += 1
for cid, c in CLUSTERS.items():
    lin_clusters[LINEAGE.get(c["originator"], "(no named originator)")] += 1

summary = {
    "specimen": "withthesun33.com/about-1 (Andy J. Consoli), retrieved 2026-08-02",
    "items_by_lineage": dict(lin_items.most_common()),
    "clusters_by_lineage": dict(lin_clusters.most_common()),
    "total_items": len(rows),
    "distinct_arguments": len(set(ASSIGN.values())),
    "compression_ratio": round(len(rows) / len(set(ASSIGN.values())), 2),
    "exact_duplicate_pairs": len(dupes),
    "named_originators": len([k for k in orig_clusters if k != "(no named originator)"]),
    "items_traceable_to_a_named_originator": named_items,
    "items_by_family": dict(sorted(fam_items.items())),
    "items_by_lane": dict(sorted(lane_items.items())),
    "clusters_by_lane": dict(sorted(lane_clusters.items())),
    "items_by_verdict": dict(verdict_items.most_common()),
    "clusters_by_verdict": dict(verdict_clusters.most_common()),
    "largest_clusters": [
        {"cluster_id": cid, "name": CLUSTERS[cid]["name"], "items": n,
         "originator": CLUSTERS[cid]["originator"]}
        for cid, n in cluster_size.most_common(15)
    ],
    "originator_ranking_by_items": [
        {"originator": k, "items": v, "distinct_arguments": orig_clusters[k]}
        for k, v in orig_items.most_common()
    ],
    "exact_duplicates": [
        {"first_seen": a, "repeat": b, "text": t} for a, b, t in dupes
    ],
}

with open(os.path.join(DATA, "flat-earth-origins-provenance.json"), "w", encoding="utf-8") as f:
    json.dump({"summary": summary, "clusters": CLUSTERS, "items": rows},
              f, indent=2, ensure_ascii=False)

with open(os.path.join(DATA, "flat-earth-origins-provenance.csv"), "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader()
    w.writerows(rows)

# ---- console report ---------------------------------------------------
print(f"items                : {summary['total_items']}")
print(f"distinct arguments   : {summary['distinct_arguments']}  "
      f"({summary['compression_ratio']}x compression)")
print(f"exact duplicate pairs: {summary['exact_duplicate_pairs']}")
print(f"named originators    : {summary['named_originators']}")
print(f"items traceable      : {named_items} / 461 "
      f"({named_items/461*100:.0f}%)\n")
print("ITEMS BY LANE")
for k, v in sorted(lane_items.items()):
    print(f"  {LANE_NAME[k]:<45} {v:>4} items  {lane_clusters[k]:>3} arguments")
print("\nITEMS BY VERDICT")
for k, v in verdict_items.most_common():
    print(f"  {k:<22} {v:>4} items  {verdict_clusters[k]:>3} arguments")
print("\nTOP ORIGINATORS BY ITEM COUNT")
for d in summary["originator_ranking_by_items"][:14]:
    print(f"  {str(d['originator'])[:52]:<52} {d['items']:>4} items  "
          f"{d['distinct_arguments']:>2} args")
print("\nEXACT DUPLICATES")
for d in summary["exact_duplicates"]:
    print(f"  #{d['first_seen']} == #{d['repeat']}  {d['text']}")

print("\nITEMS BY LINEAGE")
for k, v in lin_items.most_common():
    print(f"  {k:<38} {v:>4} items ({v/461*100:4.1f}%)  {lin_clusters[k]:>2} arguments")
