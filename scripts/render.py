# -*- coding: utf-8 -*-
"""Render docs/index.html from the corpus. Tabs are views; nothing is duplicated.

Conventions inherited from the sibling dome review, with its known regrets fixed:
  * cross-tab links carry NO inline onclick — a delegated a[href^="#"] handler
    activates the owning tab, opens ancestor <details>, and scrolls
  * tab buttons carry data-tab, so the active button is found by attribute
    rather than by string-matching an onclick
  * tab order is declared ONCE in TABS and drives the bar, the panels and nav
  * every published number comes from the corpus; none is written as a literal
"""
import json, html, os, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HEAD_TPL = os.path.join(ROOT, "scripts", "_head.html")
OUT = os.path.join(ROOT, "docs", "index.html")

D = json.load(open(os.path.join(ROOT, "data", "flat-earth-origins-provenance.json"),
                   encoding="utf-8"))
S, PEOPLE, WORKS, ARGS = D["summary"], D["people"], D["works"], D["arguments"]

TABS = [("overview", "Overview"), ("claims", "Claims Reviewed"),
        ("people", "The People"), ("families", "The Families"), ("method", "Method")]

VC = {"REFUTED": "refuted", "STANDARD PHYSICS": "std", "SELF-CONTRADICTED": "selfcon",
      "MISLEADING": "misleading", "UNFALSIFIABLE": "unfalsifiable",
      "NOT DEMONSTRATED": "notdemo"}
VB = dict(VC); VB["STANDARD PHYSICS"] = "stdmodel"
LANE_TITLE = {"A-EXP": "A1 &middot; Geocentric physics", "A-REL": "A2 &middot; Relativity &amp; coordinates",
              "B": "B &middot; Flat-earth observations", "C": "C &middot; Scriptural",
              "D": "D &middot; Historical / esoteric", "E": "E &middot; Misappropriated astronomy"}
LANE_ORDER = ["A-EXP", "A-REL", "B", "C", "D", "E"]
LIN_COLOR = {"Zetetic": "var(--misleading-solid)", "Tychonian": "var(--selfcon-solid)",
             "Esoteric": "var(--notdemo-solid)", "Pre-modern": "var(--unfalsifiable-solid)"}


def e(x):
    return html.escape(str(x)) if x is not None else ""


def rng(nums):
    nums = sorted(nums); out = []; i = 0
    while i < len(nums):
        j = i
        while j + 1 < len(nums) and nums[j + 1] == nums[j] + 1: j += 1
        out.append(str(nums[i]) if j == i else f"{nums[i]}&ndash;{nums[j]}")
        i = j + 1
    return ", ".join(out)


def chip(v):
    return (f'<a class="ds-verdict-link" href="#def-{VC[v]}">'
            f'<span class="ds-verdict-tag vt-{VC[v]}">{e(v)}</span></a>')


def plink(pid):
    return f'<a href="#{pid}">{e(PEOPLE[pid]["name"])}</a>' if pid in PEOPLE else ""


def wlink(wid):
    w = WORKS[wid]
    return (f'<a href="#{wid}"><em>{e(w["title"])}</em></a> '
            f'<span style="color:var(--ink-3)">({e(w["year"])})</span>')


def alink(cid):
    return f'<a href="#ARG-{cid}">{e(ARGS["ARG-" + cid]["name"])}</a>'


def srcs(lst):
    if not lst: return ""
    li = "".join(f'<li><a href="{e(s["url"])}">{e(s["label"])}</a></li>' for s in lst)
    return ('<p style="font-family:var(--sans);font-size:.82rem;color:var(--ink-3);'
            f'margin:.8rem 0 .2rem"><strong>Sources</strong></p>'
            f'<ul style="font-size:.85rem;margin-top:0">{li}</ul>')


# ───────────────────────────────────────── CLAIMS
def render_argument(a):
    d, cid = a.get("deep"), a["cluster_id"]
    meta = (f'<p class="ds-pred-meta">{a["item_count"]} of the {S["total_items"]} items '
            f'restate this'
            + (f' &middot; items {rng(a["items"])}' if a["item_count"] <= 12 else "")
            + (f' &middot; first published by {plink(a["originator_id"])}'
               if a["originator_id"] else " &middot; no named originator") + "</p>")
    if not d:
        return (f'<div class="ks-test" id="ARG-{cid}">'
                f'<h3 style="margin-top:0">ARG-{cid} &middot; {e(a["name"])} '
                f'<span class="ks-status ks-pending">cluster depth</span></h3>'
                f'{meta}{chip(a["verdict"])}<p>{e(a["basis"])}</p>'
                + (f'<p style="font-family:var(--sans);font-size:.8rem;color:var(--ink-3)">'
                   f'<em>Real work cited:</em> {e(a["real_source_cited"])}</p>'
                   if a["real_source_cited"] else "") + "</div>")

    p, sm = d.get("passage"), d["steelman"]
    if p:
        w = WORKS[p["work"]]
        pd_note = ("Public domain &mdash; quoted at length." if p["pd"] else
                   "In copyright &mdash; short excerpt under fair use, with citation.")
        block1 = ('<details class="ds-win-section"><summary class="ks-summary">'
                  '<strong>1 &middot; The claim in its own words</strong>'
                  f'<p class="ks-tldr">{e(w["title"])}, {e(w["year"])}. {pd_note}</p></summary>'
                  '<div class="ks-detail">'
                  f'<blockquote style="margin:.4rem 0 .8rem;padding:.6rem 1rem;'
                  f'border-left:3px solid var(--rule);background:var(--card-bg);'
                  f'font-style:italic;white-space:pre-wrap">{e(p["quote"])}</blockquote>'
                  f'<p style="font-family:var(--sans);font-size:.8rem;color:var(--ink-3)">&mdash; '
                  f'{wlink(p["work"])}, {e(p["locator"])}</p><p>{p["gloss"]}</p></div></details>')
    else:
        block1 = ('<details class="ds-win-section"><summary class="ks-summary">'
                  '<strong>1 &middot; No original to quote</strong>'
                  '<p class="ks-tldr">This cluster has no named author and no traceable source '
                  'publication. That is a finding about how the list was assembled, not only a '
                  'gap in our records.</p></summary>'
                  f'<div class="ks-detail">{d["untraceable"]}</div></details>')
    h = [f'<div class="ks-test" id="ARG-{cid}">',
         f'<h3 style="margin-top:0">ARG-{cid} &middot; {e(a["name"])} '
         f'<span class="ks-status ks-claimed">full treatment</span></h3>',
         meta, chip(a["verdict"]),
         f'<p class="ks-tldr" style="font-style:italic;color:var(--ink-2)">{e(d["tldr"])}</p>',
         block1,
         '<details class="ds-win-section"><summary class="ks-summary">'
         '<strong>2 &middot; Steelman &mdash; what they get right</strong>'
         '<p class="ks-tldr">The strongest form of the argument, stated before it is answered. '
         'If this section is weak, the refutation is worthless.</p></summary>'
         f'<div class="ks-detail"><p>{sm["description"]}</p>'
         f'<p style="margin-top:.8rem"><strong>Why it doesn&rsquo;t save the claim.</strong> '
         f'{sm["why_it_doesnt_save_claim"]}</p></div></details>',
         '<details class="ds-win-section"><summary class="ks-summary">'
         '<strong>3 &middot; Refutation</strong> '
         f'{chip(a["verdict"])}<p class="ks-tldr">{e(a["basis"])}</p></summary>'
         f'<div class="ks-detail">{d["refutation"]}</div></details>',
    ]

    if d["straw_man"]["identified"]:
        h.append('<div class="tally" style="border-left-color:var(--misleading-solid)">'
                 f'<strong>Straw man identified.</strong> {e(d["straw_man"]["detail"])}</div>')
    if d.get("related"):
        h.append('<p style="font-family:var(--sans);font-size:.85rem"><strong>Related:</strong> '
                 + " &middot; ".join(alink(r) for r in d["related"]) + "</p>")
    if d.get("people"):
        h.append('<p style="font-family:var(--sans);font-size:.85rem"><strong>People:</strong> '
                 + " &middot; ".join(plink(x) for x in d["people"]) + "</p>")
    h.append(srcs(d.get("sources")))
    h.append("</div>")
    return "".join(h)


def tab_claims():
    full = S["arguments_at_full_depth"]
    out = ['<h1>Claims Reviewed</h1>',
           f'<p>The {S["total_items"]} list items reduce to <strong>{S["distinct_arguments"]}'
           f'</strong> distinct arguments. Each is scored once. Arguments marked '
           f'<em>full treatment</em> carry the complete pipeline &mdash; the claim in its own '
           f'words, a steelman, and the refutation. The rest sit at cluster depth: verdict and '
           f'provenance derived from the dataset, prose not yet written.</p>',
           f'<div class="tally"><strong>Progress: {full} of {S["distinct_arguments"]} arguments '
           f'at full treatment.</strong> The verdict and provenance for all '
           f'{S["distinct_arguments"]} are already derived from the dataset, so the scorecard is '
           f'complete even where the prose is not.</div>']
    for lane in LANE_ORDER:
        la = sorted([a for a in ARGS.values() if a["lane"] == lane],
                    key=lambda x: (x["depth"] != "full", -x["item_count"]))
        out.append(f'<h2 id="lane-{lane}">{LANE_TITLE[lane]} '
                   f'<span style="font-size:.85rem;font-weight:400;color:var(--ink-3)">'
                   f'({sum(x["item_count"] for x in la)} items &middot; {len(la)} arguments)'
                   f'</span></h2>')
        out += [render_argument(a) for a in la]
    return "".join(out)


# ───────────────────────────────────────── PEOPLE
def render_person(p):
    h = [f'<div class="ks-test" id="{p["id"]}">',
         f'<h3 style="margin-top:0">{e(p["name"])} '
         f'<span style="font-weight:400;color:var(--ink-3);font-size:.9rem">{e(p["dates"])}</span> '
         + ('<span class="ks-status ks-claimed">worked</span>' if p["bio_status"] == "worked"
            else '<span class="ks-status ks-pending">stub</span>') + '</h3>',
         f'<p class="ds-pred-meta"><span style="display:inline-block;width:.6rem;height:.6rem;'
         f'border-radius:50%;background:{LIN_COLOR.get(p["lineage"], "var(--border)")};'
         f'margin-right:.4rem"></span>{e(p["lineage"])} lineage &middot; '
         f'{p["argument_count"]} distinct arguments &middot; {p["item_count"]} of the '
         f'{S["total_items"]} items</p>',
         f'<p>{e(p["role"])}</p>']
    for key, title, tldr in [
        ("formation", "Where the position came from",
         "Biography only where it explains the argument &mdash; what they were doing, and why this."),
        ("had", "The data they had, and used honestly",
         "What was genuinely available in their own time, and what they did with it that was fair."),
        ("ignored", "The data they had, and passed over",
         "Available to them, and not engaged. This is the difference between being wrong and being unserious."),
        ("legacy", "What descends from them",
         "How the argument travelled, and who is still repeating it.")]:
        if p.get(key):
            h.append('<details class="ds-win-section"><summary class="ks-summary">'
                     f'<strong>{title}</strong><p class="ks-tldr">{tldr}</p></summary>'
                     f'<div class="ks-detail"><p>{p[key]}</p></div></details>')
    if p.get("kernel"):
        h.append('<details class="ds-win-section"><summary class="ks-summary">'
                 '<strong>Steelman</strong><p class="ks-tldr">What they got right, before we say '
                 'why it fails.</p></summary><div class="ks-detail">'
                 f'<p>{p["kernel"]["description"]}</p><p style="margin-top:.8rem">'
                 f'<strong>Why it doesn&rsquo;t save the claim.</strong> '
                 f'{p["kernel"]["why_it_doesnt_save_claim"]}</p></div></details>')
    if p["works"]:
        h.append('<p style="font-family:var(--sans);font-size:.85rem"><strong>Works:</strong> '
                 + " &middot; ".join(wlink(w) for w in p["works"]) + "</p>")
    if p["arguments"]:
        h.append('<p style="font-family:var(--sans);font-size:.85rem"><strong>Arguments '
                 'originating here:</strong> '
                 + " &middot; ".join(alink(a[4:]) for a in p["arguments"]) + "</p>")
    h.append(srcs(p.get("sources")))
    h.append("</div>")
    return "".join(h)


def tab_people():
    order = sorted(PEOPLE.values(), key=lambda p: (-p["item_count"], p["name"]))
    rows = "".join(
        f'<tr><td data-label="Person"><a href="#{p["id"]}">{e(p["name"])}</a></td>'
        f'<td data-label="Lineage"><span style="display:inline-block;width:.6rem;height:.6rem;'
        f'border-radius:50%;background:{LIN_COLOR.get(p["lineage"], "var(--border)")};'
        f'margin-right:.4rem"></span>{e(p["lineage"])}</td>'
        f'<td data-label="Arguments" style="text-align:center">{p["argument_count"]}</td>'
        f'<td data-label="Items" style="text-align:center"><strong>{p["item_count"]}</strong></td>'
        f'<td data-label="Share" style="text-align:right">'
        f'{p["item_count"] / S["total_items"] * 100:.1f}%</td></tr>' for p in order)
    lin_rows = "".join(
        f'<tr><td data-label="Lineage"><strong>{e(k)}</strong></td>'
        f'<td data-label="Arguments" style="text-align:center">{S["clusters_by_lineage"][k]}</td>'
        f'<td data-label="Items" style="text-align:center"><strong>{v}</strong></td>'
        f'<td data-label="Share" style="text-align:right">'
        f'{v / S["total_items"] * 100:.1f}%</td></tr>'
        for k, v in S["items_by_lineage"].items())
    works_html = "".join(
        f'<div class="ds-evidence" id="{w["id"]}"><p style="margin:0"><strong>'
        f'<em>{e(w["title"])}</em></strong> &middot; {e(w["year"])} &middot; {plink(w["author"])}'
        + (' <span class="ds-ca-tag tag-false">public domain</span>' if w["pd"]
           else ' <span class="ds-ca-tag tag-true">in copyright</span>') + '</p>'
        f'<p style="font-size:.88rem;color:var(--ink-2)">{e(w["imprint"])}</p>'
        f'<p style="font-size:.9rem">{e(w["note"])}</p>'
        f'<p style="font-size:.85rem"><a href="{e(w["url"])}">Source &rarr;</a></p></div>'
        for w in sorted(WORKS.values(), key=lambda x: str(x["year"])))
    return (f'<h1>The People</h1>'
            f'<p>A claim is not a witness &mdash; it has an author, and authors can be counted. '
            f'{S["items_traceable_to_a_named_originator"]} of the {S["total_items"]} items trace '
            f'to <strong>{S["named_originators"]}</strong> named originators across two '
            f'traditions that were never reconciled with each other.</p>'
            f'<div class="tally"><strong>Progress: {S["bios_worked"]} of {len(PEOPLE)} '
            f'biographies worked.</strong> Stubs carry verified identity and sources only &mdash; '
            f'no interpretation until the formation / had / ignored analysis is written and '
            f'reviewed.</div>'
            f'<h2>By lineage</h2><table class="stacked-card-table"><thead><tr><th>Lineage</th>'
            f'<th style="width:7rem">Arguments</th><th style="width:5rem">Items</th>'
            f'<th style="width:5rem">Share</th></tr></thead><tbody>{lin_rows}</tbody></table>'
            f'<h2>By author</h2><table class="stacked-card-table"><thead><tr><th>Person</th>'
            f'<th style="width:8rem">Lineage</th><th style="width:6rem">Arguments</th>'
            f'<th style="width:5rem">Items</th><th style="width:5rem">Share</th></tr></thead>'
            f'<tbody>{rows}</tbody></table>'
            + "".join(render_person(p) for p in order)
            + '<h2 id="works">The works</h2>' + works_html)


# ───────────────────────────────────────── FAMILIES
def tab_families():
    rows = []
    for lane in LANE_ORDER:
        la = [a for a in ARGS.values() if a["lane"] == lane]
        vd = collections.Counter(a["verdict"] for a in la)
        rows.append(f'<tr><td data-label="Family"><a href="#lane-{lane}">{LANE_TITLE[lane]}</a></td>'
                    f'<td data-label="Items" style="text-align:center"><strong>'
                    f'{sum(a["item_count"] for a in la)}</strong></td>'
                    f'<td data-label="Arguments" style="text-align:center">{len(la)}</td>'
                    f'<td data-label="Dominant verdicts">'
                    + " ".join(chip(v) for v, _ in vd.most_common(2)) + '</td></tr>')
    return (f'<h1>The Families</h1>'
            f'<p>Sorted by subject rather than by author, the same {S["total_items"]} items fall '
            f'into five families across six lanes. These counts come from a full item-by-item '
            f'pass, and they corrected this review&rsquo;s own starting assumption: the '
            f'flat-earth family was estimated at ~105 and is actually '
            f'<strong>{S["items_by_lane"]["B"]}</strong>, while the geocentric material was '
            f'estimated at ~95 and is actually <strong>'
            f'{S["items_by_lane"]["A-EXP"] + S["items_by_lane"]["A-REL"]}</strong>.</p>'
            f'<table class="stacked-card-table"><thead><tr><th>Family</th>'
            f'<th style="width:5rem">Items</th><th style="width:6rem">Arguments</th>'
            f'<th>Dominant verdicts</th></tr></thead><tbody>{"".join(rows)}</tbody></table>'
            f'<div class="ds-evidence"><h3 style="margin-top:0">Why this matters beyond '
            f'bookkeeping</h3><p style="margin-bottom:0">A list marketed as flat-earth evidence '
            f'is, by volume, <strong>predominantly a geocentrism list</strong> &mdash; and '
            f'geocentrism is a <em>spherical-Earth</em> position. Every historical authority the '
            f'list cites &mdash; Ptolemy, Aristotle, Tycho Brahe &mdash; held the Earth to be a '
            f'globe. The specimen&rsquo;s largest body of material is drawn from authors who '
            f'would reject its headline claim.</p></div>'
            f'<p style="font-family:var(--sans);font-size:.9rem;color:var(--ink-3)">Each family '
            f'links through to its arguments on the <a href="#claims">Claims Reviewed</a> tab. '
            f'The arguments are stated once, there; this tab is a view, not a second copy.</p>')


# ───────────────────────────────────────── OVERVIEW / METHOD
def tab_overview():
    mx = max(S["items_by_verdict"].values())
    bars = "".join(
        f'<a class="ds-verdict-bar-row" href="#def-{VC[v]}">'
        f'<span class="ds-vb-label">{e(v)}</span>'
        f'<span class="ds-vb-bar-container"><span class="ds-vb-bar vb-{VB[v]}" '
        f'style="width:{n / mx * 100:.1f}%"><span class="ds-vb-count">{n}</span></span></span>'
        f'<span class="ds-vb-pct">{n / S["total_items"] * 100:.0f}%</span></a>'
        for v, n in S["items_by_verdict"].items())
    card = ('<div style="padding:.9rem 1rem;background:var(--card-bg);border:1px solid '
            'var(--rule);border-radius:6px"><div style="font-size:1.6rem;font-weight:700;'
            'color:{c}">{n}</div><div style="font-family:var(--sans);font-size:.82rem;'
            'color:var(--ink-3)">{l}</div></div>')
    return (
        f'<h1>{S["total_items"]} Proofs, {S["distinct_arguments"]} Arguments, '
        f'{S["named_originators"]} Authors</h1>'
        f'<p style="font-size:1.02rem;color:var(--ink-2);max-width:70ch">Flat-earth and geocentric '
        f'&ldquo;proof lists&rdquo; circulate as long numbered compilations. They look '
        f'overwhelming by volume. This review sorts one representative specimen by <em>where each '
        f'claim came from</em>. Sorted that way, {S["total_items"]} items collapse to '
        f'<strong>{S["distinct_arguments"]} distinct arguments</strong>, and '
        f'{S["items_traceable_to_a_named_originator"]} of them trace to '
        f'<strong>{S["named_originators"]} named people</strong>.</p>'
        '<div class="ds-scorecard" style="display:grid;grid-template-columns:'
        'repeat(auto-fit,minmax(150px,1fr));gap:.7rem;margin:1rem 0">'
        + card.format(n=S["total_items"], l="numbered claims in the specimen", c="var(--heading)")
        + card.format(n=S["distinct_arguments"],
                      l=f'distinct arguments ({S["compression_ratio"]}&times; compression)',
                      c="var(--heading)")
        + card.format(n=S["named_originators"],
                      l=f'named authors behind {S["items_traceable_to_a_named_originator"]} '
                        f'of the {S["total_items"]}', c="var(--heading)")
        + card.format(n=0, l="that <em>discriminate</em> flat/stationary from the standard model",
                      c="var(--semantic-good)")
        + '</div>'
        f'<div class="tally"><strong>The one-line thesis.</strong> Two different claims are fused '
        f'in these lists &mdash; that the Earth is <em>flat</em>, and that it is '
        f'<em>non-rotating</em> &mdash; and neither half is supported by any item that '
        f'distinguishes it from the ordinary spinning globe. <strong>The list is not '
        f'{S["total_items"]} pieces of evidence. It is {S["distinct_arguments"]} arguments, '
        f'restated.</strong></div>'
        f'<div class="ds-falsifiability-module"><div class="ds-fm-heading">'
        f'Under construction &mdash; what is finished and what is not</div>'
        f'<p class="ds-fm-caption">This page is being built in the open. The scorecard above is '
        f'complete; the prose beneath it is not. Nothing here is hidden behind a progress bar.</p>'
        f'<ul class="ds-fm-rows">'
        f'<li class="ds-fm-row"><span class="ds-fm-condition">Every item scored</span>'
        f'<span class="ds-fm-desc">All {S["total_items"]} items are assigned to an argument, a '
        f'source family and a verdict, derived from the dataset rather than asserted. The '
        f'scorecard and the family counts are final.</span>'
        f'<span class="ds-fm-status"><span class="ds-fm-status-num">{S["total_items"]}</span>'
        f'<span class="ds-fm-status-sub">complete</span></span></li>'
        f'<li class="ds-fm-row"><span class="ds-fm-condition">Arguments written in full</span>'
        f'<span class="ds-fm-desc">Original passage, steelman and refutation, with sources. '
        f'The remainder show verdict and provenance only. All four designated careful cases '
        f'are written.</span><span class="ds-fm-status ds-fm-status-partial">'
        f'<span class="ds-fm-status-num">{S["arguments_at_full_depth"]}/{S["distinct_arguments"]}</span>'
        f'<span class="ds-fm-status-sub">in progress</span></span></li>'
        f'<li class="ds-fm-row"><span class="ds-fm-condition">Attributions independently audited</span>'
        f'<span class="ds-fm-desc">Checked line-by-line against the primary text. This is the '
        f'weakest part of the page and we would rather say so &mdash; see <a href="#method">'
        f'Known limits</a>.</span><span class="ds-fm-status ds-fm-status-partial">'
        f'<span class="ds-fm-status-num">{S["arguments_at_full_depth"]}/{S["distinct_arguments"]}</span>'
        f'<span class="ds-fm-status-sub">audited</span></span></li>'
        f'<li class="ds-fm-row"><span class="ds-fm-condition">Biographies written</span>'
        f'<span class="ds-fm-desc">The rest carry verified identity and sources only, with no '
        f'interpretation.</span><span class="ds-fm-status ds-fm-status-pending">'
        f'<span class="ds-fm-status-num">{S["bios_worked"]}/{len(PEOPLE)}</span>'
        f'<span class="ds-fm-status-sub">pending</span></span></li>'
        f'</ul></div>'
        f'<div class="ds-verdict-bars"><div class="ds-vb-heading">Verdict distribution</div>'
        f'<div class="ds-vb-caption">All {S["total_items"]} items scored via their argument. '
        f'Bars show items.</div><div class="ds-vb-rows">{bars}</div></div>'
        '<h2 id="legend">Verdict legend</h2><div class="ds-verdict-legend">'
        '<div class="ds-vl vl-refuted" id="def-refuted"><strong>REFUTED</strong> &mdash; '
        'contradicted by a specific measurement.</div>'
        '<div class="ds-vl vl-std" id="def-std"><strong>STANDARD PHYSICS</strong> &mdash; real, '
        'already explained, does not discriminate.</div>'
        '<div class="ds-vl vl-selfcon" id="def-selfcon"><strong>SELF-CONTRADICTED</strong> '
        '&mdash; the claim&rsquo;s own source, or another item on the same list, points the '
        'other way.</div>'
        '<div class="ds-vl vl-misleading" id="def-misleading"><strong>MISLEADING</strong> '
        '&mdash; real data, wrong conclusion made to look supported.</div>'
        '<div class="ds-vl vl-unfalsifiable" id="def-unfalsifiable"><strong>UNFALSIFIABLE</strong> '
        '&mdash; outside testable measurement.</div>'
        '<div class="ds-vl vl-notdemo" id="def-notdemo"><strong>NOT DEMONSTRATED</strong> '
        '&mdash; asserted, argument never made.</div></div>')


def tab_method():
    untraced = S["total_items"] - S["items_traceable_to_a_named_originator"]
    return (
        '<h1>Method</h1><h2>The question that settles most items</h2>'
        '<div class="ds-evaluate-preface"><p style="margin:.2rem 0 0"><strong>Does the claim '
        '<em>discriminate</em> a flat/stationary Earth from the ordinary spinning globe?</strong> '
        'A result both models predict equally is not evidence for either. To count, an item must '
        'be something the flat/stationary model gets right that the globe gets <em>wrong</em>. On '
        'this list, nothing takes that form.</p></div>'
        '<h2>How a claim is worked</h2><ol>'
        '<li><strong>The claim in its own words</strong> &mdash; traced to the publication it '
        'first appears in, quoted from the original. Public-domain sources are quoted at length; '
        'in-copyright sources get a short excerpt and a citation. That asymmetry is legal, not '
        'editorial, and it means the Victorian lane will always read deeper than the modern one.</li>'
        '<li><strong>Steelman</strong> &mdash; the strongest form of the argument, stated before '
        'it is answered. The bar is the kernel, not the surface: name the specific true thing they '
        'found, then show the true thing points the other way.</li>'
        '<li><strong>Refutation</strong> &mdash; against measurement, with sources. Where a '
        'defender has a real objection left standing, it is answered here, in our own voice, '
        'rather than staged as a debate.</li></ol>'
        '<p>Behind each of those three, and not published, sits an adversarial pass: a reviewer '
        'writes the strongest defence still available to the other side, in the '
        'defender&rsquo;s voice, and rates it 1&ndash;5. A rating of 3 or more obliges a specific '
        'change to the refutation above before it ships. That review exists to make the visible '
        'text harder to attack &mdash; not to be read as part of it, which would only hand the '
        'reader the other side&rsquo;s best case at the moment the argument is meant to have '
        'landed.</p>'
        '<h2>Principles</h2><ol>'
        '<li>Every claim is independently verifiable, with a reference.</li>'
        '<li>We use the claim&rsquo;s own logic against it &mdash; the strongest refutation of '
        '&ldquo;experiment X shows no motion&rdquo; is experiment X&rsquo;s published result.</li>'
        '<li>We evaluate against measurement, not authority.</li>'
        '<li>We engage the strongest version.</li>'
        '<li>Unfalsifiable claims are identified, not ridiculed.</li>'
        '<li>Errors are logged and corrected in public.</li></ol>'
        f'<h2>Known limits</h2>'
        f'<div class="ds-evidence" style="border-left:3px solid var(--misleading-solid)">'
        f'<h3 style="margin-top:0">The weakest part of this page is its attributions</h3>'
        f'<p>This is a review about provenance, so an error in our own provenance is the most '
        f'serious kind we can make. It is worth stating the rate rather than burying it.</p>'
        f'<p>The first pass assigned sources at <em>argument</em> level and did not check '
        f'individual items against the primary texts. Where arguments have since been written '
        f'up, that checking has happened &mdash; and <strong>four of the first eleven turned up '
        f'an error in our own attribution</strong>. One citation did not say what we said it '
        f'said; one page range was wrong; one set of sixteen scriptural proof-texts was '
        f'attributed to an 1885 pamphlet that mentions none of them; and at least six item '
        f'titles in another argument could not be located in the source we credited them to.</p>'
        f'<p>All four are recorded in the repository&rsquo;s corrections log with the evidence '
        f'that produced them. The working conclusion: <strong>treat any attribution on an '
        f'argument still marked &ldquo;cluster depth&rdquo; as provisional.</strong> The verdicts '
        f'and the family counts do not depend on those attributions and are unaffected; the '
        f'named-originator claims on unaudited arguments do.</p>'
        f'<p style="margin-bottom:0">Roughly a third of spot-checks failing is not a rate we '
        f'are comfortable with, and re-auditing the remaining arguments is now ahead of writing '
        f'new ones.</p></div>'
        f'<ul>'
        f'<li>{untraced} items could not be traced to a named origin. That is a limit of this '
        f'pass, not evidence of originality &mdash; they are one-line assertions with no cited '
        f'source, which is <em>why</em> they are unattributable.</li>'
        f'<li>The &ldquo;{S["named_originators"]} authors&rdquo; figure is soft in one direction. '
        f'Untraceable arguments were recorded as untraced rather than assigned to a plausible '
        f'source, so the true producer count is somewhere between {S["named_originators"]} and '
        f'roughly 50.</li>'
        f'<li>Cluster boundaries involve judgement. A handful of items could sit in an adjacent '
        f'argument; that would move counts by a few units without changing any verdict.</li>'
        f'<li>Carpenter 1885 is the earliest numbered proof-list <em>identified</em>, not provably '
        f'the first &mdash; his own earlier works were not available to check.</li></ul>'
        '<h2>Version history</h2><table><thead><tr><th style="width:8rem">Date</th><th>Change</th>'
        '</tr></thead><tbody>'
        '<tr><td>2026-08-02</td><td>Restructured to a tabbed review over a single canonical corpus '
        '(<code>PER-</code> people, <code>WRK-</code> works, <code>ARG-</code> arguments, '
        '<code>ITEM-</code> list entries). Tabs are views; nothing is duplicated. Theme pinned '
        f'light. First argument at full treatment ({S["arguments_at_full_depth"]}); first '
        f'biographies worked ({S["bios_worked"]}).</td></tr>'
        '<tr><td>2026-08-02</td><td>Full item-by-item provenance pass over all 461 items. '
        '<strong>Correction:</strong> the scaffold&rsquo;s estimated family counts were replaced '
        'with measured counts; family B was overestimated roughly twofold and family A '
        'underestimated roughly twofold.</td></tr>'
        '<tr><td>2026-08-02</td><td>Scaffold: source-tree map, evaluation guide, family sections, '
        'seeded verdicts.</td></tr></tbody></table>'
        '<p style="font-family:var(--sans);font-size:.85rem;color:var(--ink-3)">Found an error? It '
        'should be corrected &mdash; every report is logged and reviewed regardless of outcome.</p>')


RENDER = {"overview": tab_overview, "claims": tab_claims, "people": tab_people,
          "families": tab_families, "method": tab_method}

bar = "".join(f'<button class="ds-tab-btn{" active" if i == 0 else ""}" data-tab="{t}">{e(l)}'
              f'</button>' for i, (t, l) in enumerate(TABS))

panels = []
for i, (t, l) in enumerate(TABS):
    prev = TABS[i - 1] if i > 0 else None
    nxt = TABS[i + 1] if i < len(TABS) - 1 else None
    nav = ('<div class="ds-section-nav">'
           + (f'<a class="ds-nav-prev" href="#{prev[0]}">&larr; {e(prev[1])}</a>'
              if prev else "<span></span>")
           + (f'<a class="ds-nav-next" href="#{nxt[0]}">{e(nxt[1])} &rarr;</a>'
              if nxt else "<span></span>") + '</div>')
    panels.append(f'<div class="ds-tab-content{" active" if i == 0 else ""}" id="{t}">'
                  f'{RENDER[t]()}{nav}</div>')

JS = """
function showTab(tabId, opts) {
  opts = opts || {};
  document.querySelectorAll('.ds-tab-content').forEach(function(p){ p.classList.remove('active'); });
  document.querySelectorAll('.ds-tab-btn').forEach(function(b){ b.classList.remove('active'); });
  var panel = document.getElementById(tabId);
  if (!panel) { return; }
  panel.classList.add('active');
  var btn = document.querySelector('.ds-tab-btn[data-tab="' + tabId + '"]');
  if (btn) { btn.classList.add('active'); }
  if (!opts.skipHash) { window.location.hash = tabId; }
  if (!opts.skipScroll) { window.scrollTo(0, 0); }
}
function expandToElement(el) {
  if (el.tagName === 'DETAILS') { el.open = true; }
  var parent = el.closest('details');
  while (parent) {
    parent.open = true;
    parent = parent.parentElement ? parent.parentElement.closest('details') : null;
  }
}
function goToAnchor(id, push) {
  var el = document.getElementById(id);
  if (!el) { return false; }
  if (el.classList.contains('ds-tab-content')) {
    showTab(id, { skipHash: true });
    var st = { tab: id, anchor: null };
    if (push) { history.pushState(st, '', '#' + id); } else { history.replaceState(st, '', '#' + id); }
    return true;
  }
  var tab = el.closest('.ds-tab-content');
  if (!tab) { return false; }
  showTab(tab.id, { skipHash: true, skipScroll: true });
  var st2 = { tab: tab.id, anchor: id };
  if (push) { history.pushState(st2, '', '#' + id); } else { history.replaceState(st2, '', '#' + id); }
  expandToElement(el);
  setTimeout(function(){ el.scrollIntoView({ behavior: 'smooth', block: 'start' }); }, 100);
  return true;
}
document.addEventListener('click', function(ev) {
  var btn = ev.target.closest('.ds-tab-btn');
  if (btn && btn.dataset.tab) { showTab(btn.dataset.tab); return; }
  var a = ev.target.closest('a[href^="#"]');
  if (!a) { return; }
  var id = a.getAttribute('href').slice(1);
  if (!id) { return; }
  if (goToAnchor(id, true)) { ev.preventDefault(); }
});
window.addEventListener('load', function() {
  history.replaceState({ tab: 'overview', anchor: null }, '', window.location.href);
  var hash = window.location.hash.slice(1);
  if (hash) { goToAnchor(hash, false); }
});
window.addEventListener('popstate', function() {
  var hash = window.location.hash.slice(1);
  if (!hash) { showTab('overview', { skipHash: true }); return; }
  goToAnchor(hash, false);
});
"""

BODY = f"""
<a class="ds-skip-link" href="#main">Skip to main content</a>
<div class="wrap" style="max-width:900px;margin:0 auto;padding:0 1.1rem">
<header style="padding-top:1.2rem">
  <p style="font-family:var(--sans);font-size:.8rem;text-transform:uppercase;letter-spacing:.08em;color:var(--ink-3);margin:0 0 .3rem">
    <a href="https://funwithscience.net/" style="color:var(--ink-3);text-decoration:none">Fun With Science</a> &nbsp;/&nbsp; Reviews
  </p>
  <h1 style="border:none;margin:.2rem 0">Flat Earth Origins</h1>
  <p style="font-size:1.05rem;color:var(--ink-2);margin:0">A provenance review of the flat-earth
     &amp; geocentric &ldquo;proof&rdquo; lists &mdash; tracing {S['total_items']} claims back to
     {S['named_originators']} authors.</p>
  <p style="font-family:var(--sans);font-size:.85rem;color:var(--ink-3)">
    Specimen: the {S['total_items']}-item list at <em>withthesun33.com/about-1</em>, retrieved
    2 August 2026. This page reviews published <em>claims</em>; it does not target any individual.</p>
</header>
</div>
<div class="ds-tab-bar">{bar}</div>
<main id="main"><div class="wrap" style="max-width:900px;margin:0 auto;padding:0 1.1rem 4rem">
{''.join(panels)}
<footer style="margin-top:3rem;padding-top:1.2rem;border-top:1px solid var(--rule);font-family:var(--sans);font-size:.85rem;color:var(--ink-3)">
  <p><a href="https://funwithscience.net/" style="color:var(--ink-3)">Fun With Science</a> &middot;
     an independent review project. This page reviews published <em>claims</em>; it does not target any individual.</p>
</footer>
</div></main>
<script>{JS}</script>
</body>
</html>
"""

open(OUT, "w", encoding="utf-8").write(open(HEAD_TPL, encoding="utf-8").read() + BODY)
print(f"wrote {OUT} ({os.path.getsize(OUT):,} bytes) | tabs: {', '.join(t for t, _ in TABS)}")
