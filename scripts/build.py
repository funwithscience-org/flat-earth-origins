# -*- coding: utf-8 -*-
"""Assemble data/flat-earth-origins-provenance.json — the single canonical corpus.

Everything the page renders comes from this file. Tabs are VIEWS over it; no
tab owns a copy of anything. Cross-references are by ID only:
  ARG-* argument   PER-* person   WRK-* work   ITEM-* raw list entry
"""
import json, csv, collections, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
DATA = os.path.join(ROOT, "data")

from corpus import ITEMS
from clusters import CLUSTERS
from assign import ASSIGN
from people import PEOPLE
from works import WORKS
from deep import DEEP

LANE_FAMILY = {"A-EXP": "A", "A-REL": "A", "B": "B", "C": "C", "D": "D", "E": "E"}
LANE_NAME = {
    "A-EXP": "A1 · Geocentric physics (experiments)",
    "A-REL": "A2 · Relativity & coordinate conventions",
    "B": "B · Flat-earth observations",
    "C": "C · Scriptural",
    "D": "D · Historical / esoteric",
    "E": "E · Misappropriated astronomy",
}
ORIGINATOR_PID = {
    "Samuel Rowbotham": "PER-ROWBOTHAM", "William Carpenter": "PER-CARPENTER",
    "Thomas Winship": "PER-WINSHIP", "Wilbur Glenn Voliva": "PER-VOLIVA",
    "Samuel Shenton": "PER-SHENTON", "Charles K. Johnson": "PER-JOHNSON",
    "Eric Dubay": "PER-DUBAY", "Mark Sargent": "PER-SARGENT", "Rob Skiba": "PER-SKIBA",
    "Bob Knodel": "PER-KNODEL", "Walter van der Kamp": "PER-VANDERKAMP",
    "Gerardus Bouw": "PER-BOUW", "Robert Sungenis": "PER-SUNGENIS",
    "Robert Sungenis & Robert Bennett": "PER-SUNGENIS",
    "Robert Sungenis & Rick DeLano": "PER-SUNGENIS", "Marshall Hall": "PER-MARSHALLHALL",
    "Helena Blavatsky; Manly P. Hall": "PER-BLAVATSKY", "Manly P. Hall": "PER-HALL",
    "William Walker Atkinson (as 'Three Initiates')": "PER-ATKINSON",
    "Mircea Eliade (misapplied)": "PER-ELIADE",
    "Claudius Ptolemy (via the modern movement)": "PER-PTOLEMY",
}
LINEAGE_OF = {p: r["lineage"] for p, r in PEOPLE.items()}
LINEAGE_LABEL = {"Zetetic": "Zetetic (flat-earth) lineage",
                 "Tychonian": "Tychonian (geocentric) lineage",
                 "Esoteric": "Esoteric / Traditionalist literature",
                 "Pre-modern": "Pre-modern astronomy"}

# ---- integrity -------------------------------------------------------
assert len(ITEMS) == 461
assert set(ASSIGN) == set(range(1, 462)), "assignment must cover items 1..461"
assert not {c for c in ASSIGN.values() if c not in CLUSTERS}
assert not (set(CLUSTERS) - set(ASSIGN.values()))
for cid, d in DEEP.items():
    assert cid in CLUSTERS, f"DEEP entry for unknown cluster {cid}"
    for pid in d.get("people", []):
        assert pid in PEOPLE, f"{cid} -> unknown person {pid}"
    for rid in d.get("related", []):
        assert rid in CLUSTERS, f"{cid} -> unknown argument {rid}"
    if d.get("passage") is None:
        assert d.get("untraceable"), f"{cid}: passage is None so `untraceable` is required"
    else:
        assert d["passage"]["work"] in WORKS, f"{cid} -> unknown work"
    vc = d.get("verdict_challenge")
    if vc is not None:
        assert isinstance(vc.get("challenged"), bool), f"{cid} verdict_challenge.challenged must be bool"
        if vc["challenged"]:
            assert vc.get("proposed_verdict") and vc.get("reasoning"), \
                f"{cid}: a challenged verdict needs proposed_verdict AND reasoning"
    # THE HEDGE RULE — refute the source's wording, not the list's compression.
    cp = d.get("compression")
    assert cp is not None, f"{cid}: `compression` is required (see the hedge rule in deep.py)"
    assert cp.get("assessed") in (True, False, "no_source"), \
        f"{cid} compression.assessed must be True, False or 'no_source'"
    DRIFTS = {"none", "hedge_dropped", "force_upgraded", "scope_widened",
              "reversed", "category_shifted", "unsourced_addition"}
    if cp["assessed"] is False:
        assert cp.get("drifted") is None, \
            f"{cid}: unassessed compression cannot claim a drift verdict either way"
    elif cp["assessed"] == "no_source":
        # The comparison was ATTEMPTED and terminated in a result: there is no
        # original to compare against. That is a finding about how the list was
        # assembled, not a backlog item, and it must not be counted as either
        # "unchecked" or "faithful".
        assert cp.get("drifted") is None, \
            f"{cid}: with no source there is nothing to have drifted from"
        assert cp.get("note"), \
            f"{cid}: 'no_source' must record what search was run and where it stopped"
    else:
        assert isinstance(cp.get("drifted"), bool), f"{cid} compression.drifted must be bool"
        assert cp.get("drift_type") in DRIFTS, f"{cid} compression.drift_type invalid: {cp.get('drift_type')}"
        if cp["drifted"]:
            assert cp["drift_type"] != "none", f"{cid}: drifted=True needs a drift_type"
            for f in ("list_phrasing", "source_wording", "note"):
                assert cp.get(f), f"{cid}: a recorded drift requires `{f}` — show the reader both texts"
        else:
            assert cp["drift_type"] == "none", f"{cid}: drifted=False must carry drift_type 'none'"

    s = d.get("advocate", {}).get("survives")
    assert isinstance(s, int) and 1 <= s <= 5, f"{cid} advocate.survives must be 1-5"
    if s >= 3:
        assert d["advocate"].get("preemptive"), f"{cid} survives>=3 requires a preemptive fix"
for pid, p in PEOPLE.items():
    for w in p["works"]:
        assert w in WORKS, f"{pid} -> unknown work {w}"
for wid, w in WORKS.items():
    assert w["author"] in PEOPLE, f"{wid} -> unknown author {w['author']}"

# ---- items -----------------------------------------------------------
items = []
for n, text in enumerate(ITEMS, start=1):
    cid = ASSIGN[n]
    c = CLUSTERS[cid]
    items.append({
        "id": f"ITEM-{n:03d}", "item_no": n, "text": text,
        "family": LANE_FAMILY[c["lane"]], "lane": c["lane"],
        "argument": f"ARG-{cid}", "cluster_id": cid, "cluster_name": c["name"],
        "originator": c["originator"], "originator_work": c["originator_work"],
        "originator_year": c["year"], "real_source_cited": c["real_source"],
        "verdict": c["verdict"],
    })

# ---- arguments -------------------------------------------------------
by_cluster = collections.defaultdict(list)
for r in items:
    by_cluster[r["cluster_id"]].append(r["item_no"])

arguments = {}
for cid, c in CLUSTERS.items():
    pid = ORIGINATOR_PID.get(c["originator"]) if c["originator"] else None
    d = DEEP.get(cid)
    arguments[f"ARG-{cid}"] = {
        "id": f"ARG-{cid}", "cluster_id": cid, "lane": c["lane"],
        "family": LANE_FAMILY[c["lane"]], "name": c["name"], "verdict": c["verdict"],
        "basis": c["note"], "originator": c["originator"], "originator_id": pid,
        "originator_work": c["originator_work"], "originator_year": c["year"],
        "real_source_cited": c["real_source"],
        "items": sorted(by_cluster[cid]), "item_count": len(by_cluster[cid]),
        "depth": "full" if d else "cluster",
        "deep": d,
    }

# ---- people (arguments attached by reference, never copied) ----------
people = {}
for pid, p in PEOPLE.items():
    owned = sorted(a for a, r in arguments.items() if r["originator_id"] == pid)
    people[pid] = dict(p, id=pid, arguments=owned, argument_count=len(owned),
                       item_count=sum(arguments[a]["item_count"] for a in owned))

works = {w: dict(v, id=w) for w, v in WORKS.items()}

# ---- derived counts --------------------------------------------------
seen, dupes = {}, []
for r in items:
    k = r["text"].strip().lower().rstrip(".")
    if k in seen: dupes.append((seen[k], r["item_no"], r["text"]))
    else: seen[k] = r["item_no"]

lane_items = collections.Counter(r["lane"] for r in items)
lane_clusters = collections.Counter(CLUSTERS[c]["lane"] for c in set(ASSIGN.values()))
verdict_items = collections.Counter(r["verdict"] for r in items)
verdict_clusters = collections.Counter(c["verdict"] for c in CLUSTERS.values())
orig_items = collections.Counter(r["originator"] or "(no named originator)" for r in items)
orig_clusters = collections.Counter(c["originator"] or "(no named originator)" for c in CLUSTERS.values())
named_items = sum(v for k, v in orig_items.items() if k != "(no named originator)")

lin_items, lin_clusters = collections.Counter(), collections.Counter()
for r in items:
    pid = ORIGINATOR_PID.get(r["originator"]) if r["originator"] else None
    lin_items[LINEAGE_LABEL.get(LINEAGE_OF.get(pid), "(no named originator)")] += 1
for c in CLUSTERS.values():
    pid = ORIGINATOR_PID.get(c["originator"]) if c["originator"] else None
    lin_clusters[LINEAGE_LABEL.get(LINEAGE_OF.get(pid), "(no named originator)")] += 1

cluster_size = collections.Counter(ASSIGN.values())
summary = {
    "specimen": "withthesun33.com/about-1 (Andy J. Consoli), retrieved 2026-08-02",
    "items_by_lineage": dict(lin_items.most_common()),
    "clusters_by_lineage": dict(lin_clusters.most_common()),
    "total_items": len(items),
    "distinct_arguments": len(set(ASSIGN.values())),
    "compression_ratio": round(len(items) / len(set(ASSIGN.values())), 2),
    "exact_duplicate_pairs": len(dupes),
    "named_originators": len([k for k in orig_clusters if k != "(no named originator)"]),
    "items_traceable_to_a_named_originator": named_items,
    "people_count": len(people), "works_count": len(works),
    "arguments_at_full_depth": sum(1 for a in arguments.values() if a["depth"] == "full"),
    "hedge_checked": sum(1 for a in arguments.values()
                         if a["deep"] and a["deep"]["compression"]["assessed"] is True),
    "hedge_drifted": sum(1 for a in arguments.values()
                         if a["deep"] and a["deep"]["compression"].get("drifted")),
    "hedge_no_source": sum(1 for a in arguments.values()
                           if a["deep"] and a["deep"]["compression"]["assessed"] == "no_source"),
    "bios_worked": sum(1 for p in people.values() if p["bio_status"] == "worked"),
    "items_by_family": dict(sorted(collections.Counter(r["family"] for r in items).items())),
    "items_by_lane": dict(sorted(lane_items.items())),
    "clusters_by_lane": dict(sorted(lane_clusters.items())),
    "items_by_verdict": dict(verdict_items.most_common()),
    "clusters_by_verdict": dict(verdict_clusters.most_common()),
    "largest_clusters": [
        {"cluster_id": c, "name": CLUSTERS[c]["name"], "items": n,
         "originator": CLUSTERS[c]["originator"]} for c, n in cluster_size.most_common(15)],
    "originator_ranking_by_items": [
        {"originator": k, "items": v, "distinct_arguments": orig_clusters[k]}
        for k, v in orig_items.most_common()],
    "exact_duplicates": [{"first_seen": a, "repeat": b, "text": t} for a, b, t in dupes],
}

# Advocate mode is an INTERNAL review artifact, not reader-facing. It is stripped
# from the published corpus and written to review/advocate.json instead. Objection
# handling that survives review belongs in the refutation prose, in the author's voice.
REVIEW = os.path.join(ROOT, "review")
advocate = {a: dict(arguments[a]["deep"]["advocate"], argument=a,
                    name=arguments[a]["name"], verdict=arguments[a]["verdict"])
            for a in arguments if arguments[a]["deep"]}
os.makedirs(REVIEW, exist_ok=True)
with open(os.path.join(REVIEW, "advocate.json"), "w", encoding="utf-8") as f:
    json.dump({"_note": "Internal only. Never rendered to docs/. A rating >=3 obliges a "
                        "preemptive change to the refutation prose.",
               "entries": advocate}, f, indent=2, ensure_ascii=False)
for a in arguments.values():
    if a["deep"]:
        a["deep"] = {k: v for k, v in a["deep"].items() if k != "advocate"}

corpus = {"summary": summary, "people": people, "works": works,
          "arguments": arguments, "clusters": CLUSTERS, "items": items}

with open(os.path.join(DATA, "flat-earth-origins-provenance.json"), "w", encoding="utf-8") as f:
    json.dump(corpus, f, indent=2, ensure_ascii=False)

flat = [{k: v for k, v in r.items() if k != "id"} for r in items]
with open(os.path.join(DATA, "flat-earth-origins-provenance.csv"), "w",
          encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(flat[0].keys()))
    w.writeheader(); w.writerows(flat)

print(f"items {len(items)} | arguments {len(arguments)} "
      f"({summary['arguments_at_full_depth']} at full depth) | "
      f"people {len(people)} ({summary['bios_worked']} worked) | works {len(works)}")
for k, v in sorted(lane_items.items()):
    print(f"  {LANE_NAME[k]:<45} {v:>4} items  {lane_clusters[k]:>3} arguments")
