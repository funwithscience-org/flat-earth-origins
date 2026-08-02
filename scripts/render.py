# -*- coding: utf-8 -*-
"""Render the updated review page: keep the scaffold's <head>/<style>, rebuild the body."""
import json, html, collections, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

HEAD_TPL = os.path.join(ROOT, "scripts", "_head.html")  # <head>+<style>, edit here for design changes
OUT = os.path.join(ROOT, "docs", "index.html")

d = json.load(open(os.path.join(ROOT, "data", "spinning-ball-provenance.json"), encoding="utf-8"))
S, CL, ROWS = d["summary"], d["clusters"], d["items"]

head = open(HEAD_TPL, encoding="utf-8").read()

VCLASS = {"REFUTED": "refuted", "STANDARD PHYSICS": "std", "SELF-CONTRADICTED": "selfcon",
          "MISLEADING": "misleading", "UNFALSIFIABLE": "unfalsifiable",
          "NOT DEMONSTRATED": "notdemo"}
VBAR = {"REFUTED": "refuted", "STANDARD PHYSICS": "stdmodel", "SELF-CONTRADICTED": "selfcon",
        "MISLEADING": "misleading", "UNFALSIFIABLE": "unfalsifiable",
        "NOT DEMONSTRATED": "notdemo"}

size = collections.Counter(r["cluster_id"] for r in ROWS)
items_by_cluster = collections.defaultdict(list)
for r in ROWS:
    items_by_cluster[r["cluster_id"]].append(r["item_no"])

def e(x):
    return html.escape(str(x)) if x is not None else ""

def rng(nums):
    """Compact an item-number list into ranges: 1,2,3,7 -> 1–3, 7"""
    nums = sorted(nums); out = []; i = 0
    while i < len(nums):
        j = i
        while j + 1 < len(nums) and nums[j + 1] == nums[j] + 1:
            j += 1
        out.append(str(nums[i]) if j == i else f"{nums[i]}–{nums[j]}")
        i = j + 1
    return ", ".join(out)

def cluster_table(lane, note=""):
    cids = [c for c in CL if CL[c]["lane"] == lane]
    cids.sort(key=lambda c: -size[c])
    rows_html = []
    for c in cids:
        k = CL[c]
        orig = f"<strong>{e(k['originator'])}</strong>" if k["originator"] else \
               "<span style='color:var(--ink-3)'>no named originator</span>"
        work = f"<br><span style='font-family:var(--sans);font-size:.78rem;color:var(--ink-3)'>{e(k['originator_work'])}{', ' + e(k['year']) if k['year'] else ''}</span>" \
               if k["originator_work"] else ""
        real = f"<div style='font-family:var(--sans);font-size:.75rem;color:var(--ink-3);margin-top:.3rem'><em>Real work cited:</em> {e(k['real_source'])}</div>" \
               if k["real_source"] else ""
        rows_html.append(f"""      <tr>
        <td data-label="Argument"><strong>{e(k['name'])}</strong>
            <div style="font-family:var(--sans);font-size:.75rem;color:var(--ink-3);margin-top:.25rem">items {rng(items_by_cluster[c])}</div></td>
        <td data-label="Count" style="text-align:center;font-variant-numeric:tabular-nums"><strong>{size[c]}</strong></td>
        <td data-label="Traced to">{orig}{work}</td>
        <td class="v-{VCLASS[k['verdict']]}" data-label="Verdict"><span class="ds-verdict-tag vt-{VCLASS[k['verdict']]}">{e(k['verdict'])}</span></td>
        <td data-label="Basis">{e(k['note'])}{real}</td>
      </tr>""")
    return f"""  <table class="stacked-card-table">
    <thead><tr><th>Distinct argument</th><th style="width:4rem">Items</th><th style="width:13rem">Traced to</th><th style="width:11rem">Verdict</th><th>Basis</th></tr></thead>
    <tbody>
{chr(10).join(rows_html)}
    </tbody>
  </table>"""

# ---------- verdict distribution bars ----------
vb = []
mx = max(S["items_by_verdict"].values())
for v, n in S["items_by_verdict"].items():
    pct = n / S["total_items"] * 100
    vb.append(f"""      <a class="ds-verdict-bar-row" href="#legend">
        <span class="ds-vb-label">{e(v)}</span>
        <span class="ds-vb-bar-container"><span class="ds-vb-bar vb-{VBAR[v]}" style="width:{n/mx*100:.1f}%"><span class="ds-vb-count">{n}</span></span></span>
        <span class="ds-vb-pct">{pct:.0f}%</span></a>""")

# ---------- originator ranking table ----------
LINEAGE_OF = {
    "Samuel Rowbotham": "Zetetic", "William Carpenter": "Zetetic",
    "Wilbur Glenn Voliva": "Zetetic", "Samuel Shenton": "Zetetic",
    "Charles K. Johnson": "Zetetic", "Eric Dubay": "Zetetic",
    "Mark Sargent": "Zetetic", "Rob Skiba": "Zetetic", "Bob Knodel": "Zetetic",
    "Walter van der Kamp": "Tychonian", "Gerardus Bouw": "Tychonian",
    "Robert Sungenis": "Tychonian", "Robert Sungenis & Robert Bennett": "Tychonian",
    "Robert Sungenis & Rick DeLano": "Tychonian", "Marshall Hall": "Tychonian",
    "Helena Blavatsky; Manly P. Hall": "Esoteric",
    "William Walker Atkinson (as 'Three Initiates')": "Esoteric",
    "Mircea Eliade (misapplied)": "Esoteric", "Manly P. Hall": "Esoteric",
    "Claudius Ptolemy (via the modern movement)": "Pre-modern",
}
LCOLOR = {"Zetetic": "var(--misleading-solid)", "Tychonian": "var(--selfcon-solid)",
          "Esoteric": "var(--notdemo-solid)", "Pre-modern": "var(--unfalsifiable-solid)"}
orank = []
for x in S["originator_ranking_by_items"]:
    o = x["originator"]
    if o == "(no named originator)":
        continue
    lin = LINEAGE_OF.get(o, "—")
    orank.append(f"""      <tr>
        <td data-label="Originator"><strong>{e(o)}</strong></td>
        <td data-label="Lineage"><span style="display:inline-block;width:.6rem;height:.6rem;border-radius:50%;background:{LCOLOR.get(lin,'var(--border)')};margin-right:.4rem"></span>{e(lin)}</td>
        <td data-label="Distinct arguments" style="text-align:center;font-variant-numeric:tabular-nums">{x['distinct_arguments']}</td>
        <td data-label="Items generated" style="text-align:center;font-variant-numeric:tabular-nums"><strong>{x['items']}</strong></td>
        <td data-label="Share of list" style="text-align:right;font-variant-numeric:tabular-nums">{x['items']/461*100:.1f}%</td>
      </tr>""")

lin_rows = []
for k, v in S["items_by_lineage"].items():
    lin_rows.append(f"""      <tr><td data-label="Lineage"><strong>{e(k)}</strong></td>
        <td data-label="Distinct arguments" style="text-align:center">{S['clusters_by_lineage'][k]}</td>
        <td data-label="Items" style="text-align:center"><strong>{v}</strong></td>
        <td data-label="Share" style="text-align:right">{v/461*100:.1f}%</td></tr>""")

dupe_rows = "".join(
    f"<li>Item <strong>#{x['repeat']}</strong> is a verbatim repeat of item <strong>#{x['first_seen']}</strong> — &ldquo;{e(x['text'])}&rdquo;</li>"
    for x in S["exact_duplicates"])

big = S["largest_clusters"][:6]
big_rows = "".join(
    f"""      <tr><td data-label="Argument"><strong>{e(x['name'])}</strong></td>
        <td data-label="Items restating it" style="text-align:center;font-variant-numeric:tabular-nums"><strong>{x['items']}</strong></td>
        <td data-label="Traced to">{e(x['originator']) or '<span style="color:var(--ink-3)">no named originator</span>'}</td></tr>"""
    for x in big)

BODY = f"""
<div class="wrap" style="max-width:900px;margin:0 auto;padding:1.2rem 1.1rem 4rem">

<header>
  <p style="font-family:var(--sans);font-size:.8rem;text-transform:uppercase;letter-spacing:.08em;color:var(--ink-3);margin:0 0 .3rem">
    <a href="https://funwithscience.net/" style="color:var(--ink-3);text-decoration:none">Fun With Science</a> &nbsp;/&nbsp; Reviews
  </p>
  <h1 style="border:none">461 Proofs, 98 Arguments, 20 Authors</h1>
  <h1 style="border:none;font-size:1.25rem;font-weight:400;color:var(--ink-2)">A provenance review of the flat-earth &amp; geocentric &ldquo;proof&rdquo; lists</h1>
  <p style="font-size:1.02rem;color:var(--ink-2);max-width:70ch">
    Flat-earth and geocentric &ldquo;proof lists&rdquo; circulate as long numbered compilations &mdash; 100 items, 200 items, 461 items.
    They look overwhelming by volume. This review takes one representative specimen and does the thing a numbered list is built to
    prevent: it sorts the claims by <em>where they came from</em>. Sorted that way, 461 items collapse to
    <strong>{S['distinct_arguments']} distinct arguments</strong>, and {S['items_traceable_to_a_named_originator']} of the 461
    trace to <strong>{S['named_originators']} named people</strong> &mdash; most of them dead, several of them contradicting each other,
    and two of them the movement&rsquo;s own founders.
  </p>
  <p style="font-family:var(--sans);font-size:.85rem;color:var(--ink-3)">
    Specimen: the 461-item list at <em>withthesun33.com/about-1</em>, retrieved 2 August 2026, used as a representative compilation.
    This page reviews published <em>claims</em>, never a person.
  </p>
  <span style="display:inline-block;background:var(--misleading);color:#1a1a1a;font-family:var(--sans);font-size:.7rem;font-weight:700;letter-spacing:.05em;padding:.1rem .45rem;border-radius:3px;vertical-align:middle">DRAFT</span>
  &nbsp;<span style="font-family:var(--sans);font-size:.85rem;color:var(--ink-3)">Provenance mapping and scorecard complete for all 461 items. Long-form writeups for the four careful cases still pending. Working slug <code>/spinning-ball-review/</code>.</span>
</header>

<nav style="font-family:var(--sans);font-size:.9rem;margin:1.6rem 0;padding:.8rem 1rem;background:var(--card-bg);border:1px solid var(--rule);border-radius:6px;line-height:1.9">
  <strong style="color:var(--ink-3);text-transform:uppercase;letter-spacing:.05em;font-size:.78rem">On this page</strong><br>
  <a href="#scorecard">Scorecard</a> &nbsp;&middot;&nbsp;
  <a href="#people">The Source Tree: people</a> &nbsp;&middot;&nbsp;
  <a href="#source-tree">The Source Tree: families</a> &nbsp;&middot;&nbsp;
  <a href="#evaluation-guide">Evaluation Guide</a> &nbsp;&middot;&nbsp;
  <a href="#fam-a1">A1. Geocentric experiments</a> &nbsp;&middot;&nbsp;
  <a href="#fam-a2">A2. Relativity</a> &nbsp;&middot;&nbsp;
  <a href="#fam-b">B. Flat-earth observations</a> &nbsp;&middot;&nbsp;
  <a href="#fam-c">C. Scriptural</a> &nbsp;&middot;&nbsp;
  <a href="#fam-d">D. Historical / esoteric</a> &nbsp;&middot;&nbsp;
  <a href="#fam-e">E. Misappropriated astronomy</a> &nbsp;&middot;&nbsp;
  <a href="#legend">Verdict legend</a>
</nav>

<!-- ============ SCORECARD ============ -->
<section id="scorecard">
  <h2 class="ds-vb-heading" style="font-size:1.15rem;color:var(--heading)">Scorecard</h2>
  <div class="ds-scorecard" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:.7rem;margin:1rem 0">
    <div style="padding:.9rem 1rem;background:var(--card-bg);border:1px solid var(--rule);border-radius:6px">
      <div style="font-size:1.6rem;font-weight:700;color:var(--heading)">461</div>
      <div style="font-family:var(--sans);font-size:.82rem;color:var(--ink-3)">numbered claims in the specimen</div></div>
    <div style="padding:.9rem 1rem;background:var(--card-bg);border:1px solid var(--rule);border-radius:6px">
      <div style="font-size:1.6rem;font-weight:700;color:var(--heading)">{S['distinct_arguments']}</div>
      <div style="font-family:var(--sans);font-size:.82rem;color:var(--ink-3)">distinct arguments they reduce to <span style="opacity:.6">({S['compression_ratio']}&times;)</span></div></div>
    <div style="padding:.9rem 1rem;background:var(--card-bg);border:1px solid var(--rule);border-radius:6px">
      <div style="font-size:1.6rem;font-weight:700;color:var(--heading)">{S['named_originators']}</div>
      <div style="font-family:var(--sans);font-size:.82rem;color:var(--ink-3)">named authors behind {S['items_traceable_to_a_named_originator']} of the 461</div></div>
    <div style="padding:.9rem 1rem;background:var(--card-bg);border:1px solid var(--rule);border-radius:6px">
      <div style="font-size:1.6rem;font-weight:700;color:var(--semantic-good)">0</div>
      <div style="font-family:var(--sans);font-size:.82rem;color:var(--ink-3)">that <em>discriminate</em> flat/stationary from the standard model</div></div>
  </div>

  <div class="tally"><strong>The one-line thesis.</strong> Two different claims are fused in these lists &mdash; that the Earth is <em>flat</em>,
    and that it is <em>non-rotating</em> &mdash; and neither half is supported by any item that distinguishes it from the ordinary spinning
    globe. The geocentric half cites real experiments whose published results point the other way. The flat half is Victorian folk
    observation, answered at book length before 1905. The remainder is scripture, symbolism and misread astronomy.
    <strong>The list is not 461 pieces of evidence. It is {S['distinct_arguments']} arguments, restated.</strong></div>

  <div class="ds-verdict-bars">
    <div class="ds-vb-heading">Verdict distribution</div>
    <div class="ds-vb-caption">All 461 items scored via their argument cluster. Bars show items; argument counts differ (see each family section).</div>
    <div class="ds-vb-rows">
{chr(10).join(vb)}
    </div>
  </div>

  <div class="ds-falsifiability-module">
    <div class="ds-fm-heading">What would change the verdict</div>
    <p class="ds-fm-caption">A single item that the flat/stationary model gets right and the globe gets <em>wrong</em>. On this list, the count is zero.</p>
    <ul class="ds-fm-rows">
      <li class="ds-fm-row"><span class="ds-fm-condition">A discriminating observation</span>
        <span class="ds-fm-desc">Any measurement whose outcome differs between the two models, where the flat/stationary prediction is the one that matches.</span>
        <span class="ds-fm-status ds-fm-status-zero"><span class="ds-fm-status-num">0</span><span class="ds-fm-status-sub">of 461</span></span></li>
      <li class="ds-fm-row"><span class="ds-fm-condition">An original argument</span>
        <span class="ds-fm-desc">An item not traceable to a source published before 2015. The unattributed remainder is unsourced, not novel.</span>
        <span class="ds-fm-status ds-fm-status-zero"><span class="ds-fm-status-num">0</span><span class="ds-fm-status-sub">identified</span></span></li>
      <li class="ds-fm-row"><span class="ds-fm-condition">A cited experiment that supports the claim</span>
        <span class="ds-fm-desc">Of the named experiments on the list &mdash; Michelson&ndash;Gale, Sagnac, Airy, Michelson&ndash;Pease, Miller, ring-laser gyros &mdash; the published result of every one is consistent with a rotating Earth.</span>
        <span class="ds-fm-status ds-fm-status-zero"><span class="ds-fm-status-num">0</span><span class="ds-fm-status-sub">of 6</span></span></li>
    </ul>
  </div>
</section>

<!-- ============ THE PEOPLE ============ -->
<section id="people">
  <h1 style="margin-top:2.2rem">The Source Tree, Part 1: The People</h1>
  <p>The rhetorical power of a numbered list is that each item reads as an independent witness. 461 witnesses is a crowd.
     But a claim is not a witness &mdash; it has an author, and authors can be counted. When every item on this list is traced
     back to the publication that first put it into circulation, the crowd resolves into
     <strong>{S['named_originators']} people</strong>, working in <strong>two largely separate traditions that were never
     reconciled with each other</strong>, plus a body of esoteric literature whose authors were not making claims about
     geography at all.</p>

  <div class="tally"><strong>The distribution is the finding.</strong> This is a movement with very few producers and very many
     distributors. One author &mdash; Samuel Rowbotham, writing in 1849&ndash;1865 &mdash; is behind
     {[x['items'] for x in S['originator_ranking_by_items'] if x['originator']=='Samuel Rowbotham'][0]} of the 461 items.
     One modern author, Robert Sungenis, across his three bylines, is behind 128. Between them, two men account for
     <strong>{(65+128)/461*100:.0f}% of a list that presents itself as 461 independent proofs</strong>.</div>

  <h2 style="color:var(--heading)">Two braided lineages</h2>
  <p>The list fuses two movements that are historically distinct, make incompatible claims, and have never merged.
     The <strong>zetetic</strong> tradition says the Earth is a flat plane. The <strong>Tychonian</strong> tradition says the
     Earth is a <em>sphere</em> that does not move. Every authority the list cites in its historical sections &mdash; Ptolemy,
     Aristotle, Tycho Brahe &mdash; held the Earth to be a globe. The list cites them against itself.</p>

  <table class="stacked-card-table">
    <thead><tr><th>Lineage</th><th style="width:8rem">Distinct arguments</th><th style="width:6rem">Items</th><th style="width:6rem">Share</th></tr></thead>
    <tbody>
{chr(10).join(lin_rows)}
    </tbody>
  </table>

  <div class="ds-hk-grid" style="margin:1.5rem 0">
    <div class="ds-evidence">
      <h3 style="margin-top:0">The zetetic line &mdash; and where the numbered list itself comes from</h3>
      <p style="font-size:.92rem"><strong>Samuel Rowbotham</strong> (&ldquo;Parallax&rdquo;), 1849 pamphlet &rarr; <em>Earth Not a Globe</em>, 1865.
         Origin of the Bedford Level experiment, &ldquo;water finds its level,&rdquo; horizon-at-eye-level, the perspective explanation
         of sunset, and the &ldquo;8 inches per mile squared&rdquo; formula &mdash; which he took from an encyclopaedia article on
         <em>surveying</em>, i.e. from the discipline that uses it to correct for the curvature he denied.</p>
      <p style="font-size:.92rem"><strong>William Carpenter</strong>, <em>One Hundred Proofs that the Earth Is Not a Globe</em>,
         Baltimore, 1885. <strong>This is where the format is born.</strong> There is no numbered proof-list in Rowbotham;
         Carpenter condensed Rowbotham&rsquo;s prose into 100 discrete numbered items, each ending &ldquo;&hellip;is a proof that the
         Earth is not a globe.&rdquo; Every list since &mdash; 100, 200, 461 &mdash; is his template.</p>
      <p style="font-size:.92rem"><strong>Wilbur Glenn Voliva</strong> reprinted Carpenter&rsquo;s pamphlet at Zion, Illinois in 1929
         and taught it in the town&rsquo;s schools. <strong>Charles K. Johnson</strong> (1972&ndash;2001) added the layer the
         Victorians had no use for: that the astronomers are not mistaken but <em>lying</em>.
         <strong>Eric Dubay&rsquo;s</strong> <em>200 Proofs</em> (2015) names Rowbotham, Carpenter, Winship, Scott and Blount&rsquo;s
         <em>Earth Review</em> in 17 of its 200 items and closes the list with a Rowbotham quotation.</p>
      <p style="font-size:.88rem;color:var(--ink-3)">Sources: Schadewald, <em>The Plane Truth</em>; Library of Congress, <a href="https://guides.loc.gov/flat-earth/books">The Flat Earth and its Advocates</a>; Carpenter 1885 (<a href="https://www.gutenberg.org/ebooks/55387">Project Gutenberg</a>); Pannofino, <em>Genealogy</em> 8:32 (2024).</p>
    </div>
    <div class="ds-evidence">
      <h3 style="margin-top:0">The Tychonian line &mdash; modern geocentrism</h3>
      <p style="font-size:.92rem"><strong>Walter van der Kamp</strong> founded the Tychonian Society in Canada in 1971.
         His 1988 book <em>De Labore Solis: Airy&rsquo;s Failure Reconsidered</em> is the earliest documented use of the phrase
         &ldquo;Airy&rsquo;s failure&rdquo; &mdash; a term that <strong>does not exist in physics</strong>. Every occurrence of it
         traces to this movement. Bouw&rsquo;s obituary of van der Kamp credits him with the coinage by name.</p>
      <p style="font-size:.92rem"><strong>Gerardus Bouw</strong> (PhD astronomy, Case Western Reserve), <em>Geocentricity</em>, 1992 &mdash;
         the movement&rsquo;s only credentialed astronomer. He rebuilt the model to accommodate stellar aberration, contradicting
         van der Kamp, and <strong>conceded in print that his model is observationally equivalent to heliocentrism</strong> and
         must therefore be chosen on theological rather than scientific grounds.</p>
      <p style="font-size:.92rem"><strong>Robert Sungenis &amp; Robert Bennett</strong>, <em>Galileo Was Wrong: The Church Was Right</em>
         (2006), and the 2014 film <em>The Principle</em>. This is the direct source of the list&rsquo;s Michelson&ndash;Gale,
         Sagnac, Miller, Foucault and CMB material. The film&rsquo;s narrator Kate Mulgrew publicly disavowed it, as did the
         physicists who appear in it &mdash; Lawrence Krauss, Michio Kaku, Max Tegmark, George Ellis and Julian Barbour.</p>
      <p style="font-size:.88rem;color:var(--ink-3)">Sources: <a href="https://www.geocentricity.com/bibastron/index.html">Association for Biblical Astronomy</a>; van der Kamp, <a href="https://geocentricity.com/bibastron/ts_history/de_labore.pdf"><em>De Labore Solis</em> (1988)</a>; <a href="https://www.geocentricity.com/ba1/no084/obits.pdf">Bouw&rsquo;s obituary of van der Kamp</a>; <a href="https://slate.com/technology/2014/04/lawrence-krauss-on-ending-up-in-the-geocentrism-documentary-the-principle.html">Krauss, Slate, 8 April 2014</a>.</p>
    </div>
  </div>

  <h2 style="color:var(--heading)">Who actually wrote these 461 claims</h2>
  <p style="font-family:var(--sans);font-size:.9rem;color:var(--ink-3)">Ranked by how many of the 461 items descend from them.
     &ldquo;Distinct arguments&rdquo; is how many separate ideas they contributed; &ldquo;items&rdquo; is how many list entries restate those ideas.</p>
  <table class="stacked-card-table">
    <thead><tr><th>Originator</th><th style="width:8rem">Lineage</th><th style="width:6rem">Distinct arguments</th><th style="width:5rem">Items</th><th style="width:5rem">Share</th></tr></thead>
    <tbody>
{chr(10).join(orank)}
    </tbody>
  </table>
  <p style="font-family:var(--sans);font-size:.85rem;color:var(--ink-3)">
     The remaining {[x['items'] for x in S['originator_ranking_by_items'] if x['originator']=='(no named originator)'][0]} items
     ({[x['distinct_arguments'] for x in S['originator_ranking_by_items'] if x['originator']=='(no named originator)'][0]} arguments)
     could not be traced to a specific published origin. That is a limitation of this review, not evidence of originality &mdash;
     they are mostly one-line assertions with no cited source at all, which is itself the reason they are unattributable.</p>

  <h2 style="color:var(--heading)">The scientists being cited against their own results</h2>
  <p>A distinct group of names appears on the list: real researchers whose real, published work is quoted as evidence for a
     conclusion it does not support. They are not part of either lineage. They are being conscripted.</p>
  <table class="stacked-card-table">
    <thead><tr><th style="width:14rem">Researcher &amp; result</th><th>What the paper actually reports</th></tr></thead>
    <tbody>
      <tr><td data-label="Researcher"><strong>Michelson, Gale &amp; Pearson</strong><br><span style="font-family:var(--sans);font-size:.78rem;color:var(--ink-3)">ApJ 61:140, 1925</span></td>
          <td data-label="Actual result">Predicted a 0.236 fringe shift for a rotating Earth; measured <strong>0.230 &plusmn; 0.005</strong>. It detected Earth&rsquo;s rotation and returned the rate to about 2%. The geocentrist Malcolm Bowden concedes the measurement in print.</td></tr>
      <tr><td data-label="Researcher"><strong>George Biddell Airy</strong><br><span style="font-family:var(--sans);font-size:.78rem;color:var(--ink-3)">Proc. Roy. Soc., 1871</span></td>
          <td data-label="Actual result">A water-filled telescope showed no change in stellar aberration &mdash; the result Fresnel&rsquo;s theory predicted in advance, and that special relativity predicts today. Aberration exists <em>because</em> the Earth moves. Airy&rsquo;s paper does not contain the word &ldquo;failure.&rdquo;</td></tr>
      <tr><td data-label="Researcher"><strong>Dayton Miller</strong><br><span style="font-family:var(--sans);font-size:.78rem;color:var(--ink-3)">Rev. Mod. Phys. 5:203, 1933</span></td>
          <td data-label="Actual result">Reported a non-null aether drift. Shankland <em>et al.</em> (Rev. Mod. Phys. 27:167, 1955) obtained his original data sheets and traced the signal to reading statistics and local temperature variation. Shankland had been Miller&rsquo;s own student &mdash; which undercuts the suppression narrative.</td></tr>
      <tr><td data-label="Researcher"><strong>Kate Land &amp; Jo&atilde;o Magueijo</strong><br><span style="font-family:var(--sans);font-size:.78rem;color:var(--ink-3)">PRL 95:071301, 2005</span></td>
          <td data-label="Actual result">Coined &ldquo;the axis of evil&rdquo; for a real CMB multipole alignment &mdash; then <strong>walked the significance back themselves</strong> in 2007, finding &ldquo;no evidence&rdquo; under Bayesian model comparison for the general case. Planck 2018 finds no matching anomaly in polarization.</td></tr>
      <tr><td data-label="Researcher"><strong>Damien Hutsem&eacute;kers</strong><br><span style="font-family:var(--sans);font-size:.78rem;color:var(--ink-3)">A&amp;A 441:915, 2005</span></td>
          <td data-label="Actual result">Quasar polarization vectors align over large scales &mdash; because black-hole spin axes align with the cosmic filaments the quasars sit in. Preferred directions differ by redshift slice and hemisphere, so there is no single axis, and none of them passes through the Earth.</td></tr>
      <tr><td data-label="Researcher"><strong>Anderson et al. / Turyshev et al.</strong><br><span style="font-family:var(--sans);font-size:.78rem;color:var(--ink-3)">PRL 81:2858, 1998 / PRL 108:241101, 2012</span></td>
          <td data-label="Actual result">The Pioneer anomaly was real, taken seriously for fourteen years, and <strong>resolved in 2012</strong> as anisotropic thermal recoil from the spacecraft&rsquo;s own electronics. <em>Nature Physics</em> ran the farewell editorial.</td></tr>
      <tr><td data-label="Researcher"><strong>Bessel (1838) &rarr; ESA Gaia</strong><br><span style="font-family:var(--sans);font-size:.78rem;color:var(--ink-3)">Gaia DR3, 2022</span></td>
          <td data-label="Actual result">The list claims stellar parallax has never been measured. Bessel measured 61 Cygni at 0.314&Prime; in 1838; Gaia DR3 publishes parallaxes for <strong>~1.47 billion sources</strong> at 0.02&ndash;0.03 mas precision for G&lt;15.</td></tr>
      <tr><td data-label="Researcher"><strong>Mircea Eliade</strong><br><span style="font-family:var(--sans);font-size:.78rem;color:var(--ink-3)">The Myth of the Eternal Return, 1949</span></td>
          <td data-label="Actual result">A historian of religion describing <em>symbolism</em> &mdash; the <em>axis mundi</em>, the sacred centre. He was not making a claim about geography. Jonathan Z. Smith later showed even Eliade&rsquo;s universality claim rests on a misreading of the ethnographic record.</td></tr>
    </tbody>
  </table>
</section>

<!-- ============ SOURCE TREE: FAMILIES ============ -->
<section id="source-tree">
  <h1 style="margin-top:2.2rem">The Source Tree, Part 2: The Families</h1>
  <p>Sorted by subject rather than by author, the same 461 items fall into five families. The counts below are from a full
     item-by-item pass, not an estimate &mdash; and they correct the working assumption this review started with, which had
     the flat-earth material as the largest bucket. It is the smallest.</p>

  <table class="stacked-card-table">
    <thead><tr><th>Family</th><th style="width:5rem">Items</th><th style="width:6rem">Arguments</th><th>Descends from</th><th style="width:9rem">Handling</th></tr></thead>
    <tbody>
      <tr><td data-label="Family"><strong><a href="#fam-a1">A1 &middot; Geocentric physics</a></strong><br><span style="font-family:var(--sans);font-size:.8rem;color:var(--ink-3)">named experiments</span></td>
          <td data-label="Items" style="text-align:center"><strong>101</strong></td><td data-label="Arguments" style="text-align:center">26</td>
          <td data-label="Source">van der Kamp &rarr; Bouw &rarr; Sungenis. Michelson&ndash;Morley, Michelson&ndash;Gale, Sagnac, Airy, Foucault, Miller, gyroscopes.</td>
          <td data-label="Handling"><strong>Primary focus.</strong> Real experiments, decisive answers, several invert the claim.</td></tr>
      <tr><td data-label="Family"><strong><a href="#fam-a2">A2 &middot; Relativity &amp; coordinates</a></strong><br><span style="font-family:var(--sans);font-size:.8rem;color:var(--ink-3)">general covariance</span></td>
          <td data-label="Items" style="text-align:center"><strong>81</strong></td><td data-label="Arguments" style="text-align:center">12</td>
          <td data-label="Source">Sungenis &amp; Bennett, <em>Galileo Was Wrong</em> Vol. I. The single most-repeated idea on the list.</td>
          <td data-label="Handling"><strong>Careful case.</strong> The true part must be conceded before the error is shown.</td></tr>
      <tr><td data-label="Family"><strong><a href="#fam-b">B &middot; Flat-earth observations</a></strong><br><span style="font-family:var(--sans);font-size:.8rem;color:var(--ink-3)">horizon, water, sight-lines</span></td>
          <td data-label="Items" style="text-align:center"><strong>54</strong></td><td data-label="Arguments" style="text-align:center">14</td>
          <td data-label="Source">Rowbotham &rarr; Carpenter &rarr; Dubay. Bedford Level, &ldquo;water finds its level,&rdquo; long-range visibility.</td>
          <td data-label="Handling"><strong>Link-out.</strong> Exhaustively rebutted elsewhere; summarised and cited.</td></tr>
      <tr><td data-label="Family"><strong><a href="#fam-c">C &middot; Scriptural</a></strong><br><span style="font-family:var(--sans);font-size:.8rem;color:var(--ink-3)">proof-texts</span></td>
          <td data-label="Items" style="text-align:center"><strong>69</strong></td><td data-label="Arguments" style="text-align:center">10</td>
          <td data-label="Source">Carpenter&rsquo;s scriptural proofs, extended by Rob Skiba&rsquo;s biblical-cosmology teaching.</td>
          <td data-label="Handling"><strong>Named, not mocked.</strong> Outside the testable domain.</td></tr>
      <tr><td data-label="Family"><strong><a href="#fam-d">D &middot; Historical / esoteric</a></strong><br><span style="font-family:var(--sans);font-size:.8rem;color:var(--ink-3)">symbolism, mythology</span></td>
          <td data-label="Items" style="text-align:center"><strong>83</strong></td><td data-label="Arguments" style="text-align:center">18</td>
          <td data-label="Source">Blavatsky, Manly P. Hall, the <em>Kybalion</em>; Eliade and Gu&eacute;non read as cosmography rather than as religious studies.</td>
          <td data-label="Handling"><strong>Secondary focus.</strong> The section other rebuttals skip.</td></tr>
      <tr><td data-label="Family"><strong><a href="#fam-e">E &middot; Misappropriated astronomy</a></strong><br><span style="font-family:var(--sans);font-size:.8rem;color:var(--ink-3)">real data, wrong inference</span></td>
          <td data-label="Items" style="text-align:center"><strong>73</strong></td><td data-label="Arguments" style="text-align:center">18</td>
          <td data-label="Source">Genuine observational cosmology, largely routed through <em>The Principle</em> (2014).</td>
          <td data-label="Handling"><strong>Focus.</strong> Data real, inference smuggled.</td></tr>
    </tbody>
  </table>

  <div class="ds-evidence">
    <h3 style="margin-top:0">A correction to this review&rsquo;s own starting assumption</h3>
    <p>This page was scoped on a bucketing sweep that estimated Family B (the Dubay/flat-earth material) at roughly 105 items,
       the largest single family. The full pass gives <strong>54</strong> &mdash; the <em>smallest</em>. The geocentric material,
       estimated at ~95, is actually <strong>182</strong> across its two lanes.</p>
    <p style="margin-bottom:0">This matters beyond bookkeeping. A list marketed as flat-earth evidence is, by volume,
       <strong>predominantly a geocentrism list</strong> &mdash; and geocentrism is a <em>spherical-Earth</em> position. The
       specimen&rsquo;s largest body of material is drawn from authors who would reject its headline claim.</p>
  </div>

  <details class="dedup-table">
    <summary><strong>How much of the list is literal repetition</strong></summary>
    <p>Three items are verbatim duplicates of earlier items:</p>
    <ul style="font-size:.9rem">{dupe_rows}</ul>
    <p>Beyond exact repeats, the concentration is heavy. The six largest argument clusters account for
       {sum(x['items'] for x in big)} of the 461 items between them:</p>
    <table class="dedup stacked-card-table">
      <thead><tr><th>Argument</th><th style="width:7rem">Items restating it</th><th style="width:13rem">Traced to</th></tr></thead>
      <tbody>{big_rows}</tbody>
    </table>
    <p style="font-size:.88rem;color:var(--ink-3)">The single most-repeated idea &mdash; that engineering and navigation systems use
       Earth-fixed coordinates &mdash; appears 28 times in different technical vocabularies (WGS84, ITRF, ECEF, ECI, barycentric,
       ephemeris, gauge, Hamiltonian). It is one argument, and the answer is one sentence: you navigate in the frame you stand in.</p>
  </details>
</section>

<!-- ============ EVALUATION GUIDE ============ -->
<section id="evaluation-guide">
  <h1>Evaluation Guide: How We Assess a &ldquo;Proof&rdquo;</h1>
  <p>Same standard as the sibling <a href="https://funwithscience.net/dome-model-review/">dome model review</a>. Six principles,
     and one question that does most of the work.</p>
  <ol>
    <li><strong>Every claim is independently verifiable.</strong> Where we cite a measurement, it is in the public record with a reference.</li>
    <li><strong>We use the claim&rsquo;s own logic against it.</strong> The strongest refutation of &ldquo;experiment X shows no motion&rdquo; is experiment X&rsquo;s published result.</li>
    <li><strong>We evaluate against measurement, not authority.</strong> A claim is wrong when a specific prediction fails a specific measurement.</li>
    <li><strong>We engage the strongest version.</strong> Airy&rsquo;s null result and the general-covariance argument have real content. We answer the strong form.</li>
    <li><strong>Unfalsifiable claims are identified, not ridiculed.</strong> Scripture and symbolism are named as outside the testable domain &mdash; a methodological note, not an insult.</li>
    <li><strong>Errors in this review should be reported.</strong> Every correction is logged in the version history &mdash; including the count correction above.</li>
  </ol>
  <div class="ds-evaluate-preface">
    <div class="ds-ep-heading">The question that settles most items</div>
    <p style="margin:.2rem 0 0"><strong>Does the claim <em>discriminate</em> a flat/stationary Earth from the ordinary spinning globe?</strong>
       A result both models predict equally &mdash; a Michelson&ndash;Morley null, &ldquo;relativity allows a stationary frame,&rdquo; a sunset &mdash;
       is not evidence for either. To count, an item must be something the flat/stationary model gets right that the globe gets <em>wrong</em>.
       On this list, nothing takes that form. That single test is why the scorecard reads <em>0</em>.</p>
  </div>
</section>

<!-- ============ A1 ============ -->
<section id="fam-a1">
  <h1>A1 &middot; Geocentric Physics <span style="font-size:1rem;font-weight:400;color:var(--ink-3)">(101 items &middot; 26 arguments &middot; van der Kamp &rarr; Bouw &rarr; Sungenis)</span></h1>
  <p>The respectable-looking half: footnoted appeals to named 19th- and 20th-century experiments. It is also the half that most
     often <em>inverts</em> under inspection &mdash; read honestly, the cited experiment supports a rotating Earth. Two of the
     four careful cases flagged in this review&rsquo;s brief live here.</p>
{cluster_table('A-EXP')}
</section>

<!-- ============ A2 ============ -->
<section id="fam-a2">
  <h1>A2 &middot; Relativity &amp; Coordinate Conventions <span style="font-size:1rem;font-weight:400;color:var(--ink-3)">(81 items &middot; 12 arguments &middot; Sungenis &amp; Bennett)</span></h1>
  <p>The largest concentration of items behind the smallest number of ideas: 81 entries restating twelve arguments, and two of
     those twelve account for 43 of the 81. <strong>Careful case.</strong> The true part has to be conceded first: general
     relativity does permit you to write physics in Earth-centred coordinates, and no experiment detects absolute motion.
     Neither fact makes the Earth physically stationary. In Earth-centred coordinates the rest of the universe acquires
     enormous fictitious forces &mdash; that difference is observable, and it is why nobody computes a Mars transfer orbit
     in an Earth-fixed frame.</p>
{cluster_table('A-REL')}
</section>

<!-- ============ B ============ -->
<section id="fam-b">
  <h1>B &middot; Flat-Earth Observations <span style="font-size:1rem;font-weight:400;color:var(--ink-3)">(54 items &middot; 14 arguments &middot; Rowbotham &rarr; Carpenter &rarr; Dubay &middot; link-out)</span></h1>
  <p>Horizon-at-eye-level, &ldquo;water finds its level,&rdquo; Bedford Level, long-range ship and lighthouse sightings. This is the
     Victorian zetetic canon, answered before 1905 and answered again continuously since. Per the plan, we state the governing
     answer and point to the standing rebuttals rather than re-deriving them.</p>
  <div class="tally"><strong>Governing answer.</strong> Most of this family is atmospheric refraction and sight-line geometry
     misread as flat-plane evidence; the rest is &ldquo;water is level&rdquo; restated with the ambiguity in &ldquo;level&rdquo; doing
     all the work. Full point-by-point treatment:
     <a href="https://flatearth.ws/eric-dubay">flatearth.ws &mdash; rebuttals to Dubay&rsquo;s 200 Proofs</a>.</div>
  <div class="ds-evidence">
    <h3 style="margin-top:0">The one that answers itself</h3>
    <p style="margin-bottom:0">Rowbotham&rsquo;s Bedford Level result (1838) used a two-point sightline eight inches above the water &mdash;
       the exact configuration in which refraction over a canal produces a false null. When Alfred Russel Wallace repeated it in 1870
       he changed two things: he raised the sightline to 13 feet, and he added a <em>third</em> marker at the midpoint. The middle
       marker stood high, and Wallace won the wager. Henry Yule Oldham replicated it with three poles in 1901. Modern citations
       of &ldquo;Bedford Level&rdquo; point at Rowbotham&rsquo;s two-point version, and treat the court&rsquo;s later voiding of the
       <em>wager</em> &mdash; a ruling about the enforceability of betting contracts &mdash; as though it reversed the measurement.</p>
  </div>
{cluster_table('B')}
</section>

<!-- ============ C ============ -->
<section id="fam-c">
  <h1>C &middot; Scriptural Appeals <span style="font-size:1rem;font-weight:400;color:var(--ink-3)">(69 items &middot; 10 arguments)</span></h1>
  <p>Psalms&rsquo; &ldquo;the world is established, it shall not be moved,&rdquo; Joshua&rsquo;s long day, Job&rsquo;s pillars and foundations,
     read as literal cosmology. Numbered scriptural proofs enter the genre with Carpenter in 1885 and are greatly expanded in the
     YouTube era by Rob Skiba&rsquo;s biblical-cosmology teaching.</p>
  <div class="tally"><strong>Governing verdict:</strong>
     <span class="ds-verdict-badge vb-unfalsifiable"><span class="ds-vb-glyph" aria-hidden="true">&empty;</span> OUTSIDE THE TESTABLE DOMAIN</span>.
     A theological reading of scripture is not a measurement and cannot be confirmed or refuted by one. We identify this once,
     without ridicule, and decline to litigate exegesis &mdash; noting only that many religious traditions have read these passages
     non-literally for most of their history, and that the question of what the text <em>means</em> is not settled by this review
     or by any instrument.</div>
  <div class="ds-evidence">
    <h3 style="margin-top:0">One internal note</h3>
    <p style="margin-bottom:0">The list cites <em>Isaiah 40:22</em> (&ldquo;the circle of the earth&rdquo;) and <em>Revelation 7:1</em>
       (&ldquo;the four corners of the earth&rdquo;) as separate proofs, and <em>Job 26:7</em> (&ldquo;he hangs the earth upon nothing&rdquo;)
       alongside the pillars-and-foundations texts. These describe different things. Read as literal cosmology they conflict with each
       other; read as poetry they conflict with nothing. The internal tension is a feature of the proof-text method, not of the texts.</p>
  </div>
{cluster_table('C')}
</section>

<!-- ============ D ============ -->
<section id="fam-d">
  <h1>D &middot; Historical, Mythological &amp; Esoteric <span style="font-size:1rem;font-weight:400;color:var(--ink-3)">(83 items &middot; 18 arguments)</span></h1>
  <p>Tycho and Ptolemy invoked as authorities, the zodiac and Atlas as evidence, temple architecture, the <em>axis mundi</em>, and
     symbolism read as encoded cosmography. Physics-oriented rebuttals skip all of this, which is exactly why it is worth addressing.
     Three things are going on, and they need separating.</p>
  <div class="ds-evidence">
    <p><strong>1. Appeal to antiquity is not measurement.</strong> That earlier cultures believed something is a fact about those
       cultures. And the specific authorities named here cut the other way: Plato, Aristotle, Ptolemy and Tycho Brahe all held the
       Earth to be a <em>sphere</em>. Aristarchus proposed heliocentrism in the third century BCE; Eratosthenes measured the Earth&rsquo;s
       circumference around 240 BCE and got it roughly right. &ldquo;All ancient cultures were geocentric&rdquo; is both an appeal to
       authority and false in detail.</p>
    <p><strong>2. Symbol resemblance is unfalsifiable pattern-matching.</strong> A mandala has a still centre; a cathedral is oriented
       east; a logo is drawn on a polar azimuthal projection. None of these is a measurement, and no observation could contradict them,
       which is precisely the problem. The UN emblem case is instructive in reverse: the azimuthal equidistant projection is a
       mathematically defined projection <em>of a sphere</em>, used for polar navigation because it preserves distance and bearing from
       the centre point only. The flat-earth map that resembles it is Alexander Gleason&rsquo;s 1892 chart &mdash; itself an azimuthal
       equidistant projection. The resemblance runs the other way.</p>
    <p><strong>3. The esoteric sources are not saying what they are quoted as saying.</strong> &ldquo;As above, so below&rdquo; is a
       12th-century Latin rendering of an 8th&ndash;9th-century Arabic alchemical maxim about transmutation, whose modern currency comes
       from <em>The Kybalion</em> &mdash; a 1908 Chicago New Thought pamphlet by William Walker Atkinson. Mircea Eliade and Ren&eacute;
       Gu&eacute;non wrote about the <em>axis mundi</em> as religious symbolism, not geography; Jonathan Z. Smith later showed that even
       Eliade&rsquo;s universality claim rests on a conflation in his ethnographic sources. The Dendera zodiac is a late-Ptolemaic
       ceiling (c. 50 BCE, Louvre E 13482) incorporating the Babylonian&ndash;Greek zodiac &mdash; evidence of Hellenistic astronomical
       transmission, and a <em>planisphere</em>, which is a projection of a spherical sky.</p>
    <p style="margin-bottom:0"><strong>4. Tycho and Ptolemy were superseded by measurement.</strong> That is the point, not an
       embarrassment. Geocentric models were accurate, sophisticated, and replaced because better instruments produced data they could
       not fit. The same standard is being applied here.</p>
  </div>
{cluster_table('D')}
</section>

<!-- ============ E ============ -->
<section id="fam-e">
  <h1>E &middot; Misappropriated Astronomy <span style="font-size:1rem;font-weight:400;color:var(--ink-3)">(73 items &middot; 18 arguments)</span></h1>
  <p>Genuine observational results &mdash; CMB large-angle anomalies, quasar surveys, the Hubble tension, spacecraft anomalies &mdash;
     quoted as if they imply a stationary or flat Earth. The data are real. The inference is inserted without warrant, and in several
     cases the result has since been resolved in the opposite direction.</p>
  <div class="ds-evidence">
    <h3 style="margin-top:0">Careful case: the CMB &ldquo;axis of evil&rdquo;</h3>
    <p>This one must be represented honestly, because overclaiming here would be the review&rsquo;s own worst error. The alignment
       is <strong>real and reproducible</strong>: the CMB quadrupole and octopole are unusually planar and their axes point in
       nearly the same direction. Whether this is a statistical fluke, a residual systematic, or new physics is a
       <strong>live question in cosmology</strong>, argued by serious people on both sides &mdash; Schwarz, Copi, Huterer and
       Starkman still maintain there is something to explain.</p>
    <p>What can be said firmly is narrower, and sufficient. Land and Magueijo, who coined the phrase, revisited it in 2007 and found
       the significance was not robust &mdash; &ldquo;no evidence&rdquo; for the general model under Bayesian comparison. The WMAP team
       and Planck 2018 both emphasise the look-elsewhere effect, and Planck finds no corresponding anomaly in polarization.</p>
    <p style="margin-bottom:0">And the geocentric reading is undercut by the anomaly&rsquo;s own geometry. The axis aligns with the
       <em>ecliptic and the dipole</em> &mdash; the solar system&rsquo;s plane and our own motion. That is the signature of a
       <em>local</em> contaminant: zodiacal dust, foreground residuals, scanning strategy. If the alignment means anything, the most
       likely thing it means is that part of the signal is <strong>not cosmological at all</strong> &mdash; which is the opposite of
       &ldquo;the cosmos is centred on us.&rdquo;</p>
  </div>
{cluster_table('E')}
</section>

<!-- ============ LEGEND ============ -->
<section id="legend">
  <h2 style="color:var(--heading)">Verdict legend</h2>
  <div class="ds-verdict-legend">
    <div class="ds-vl vl-refuted"><strong>REFUTED</strong> &mdash; a specific claim contradicted by a specific measurement.</div>
    <div class="ds-vl vl-std"><strong>STANDARD PHYSICS</strong> &mdash; the observation is real but already explained by ordinary physics; it does not discriminate.</div>
    <div class="ds-vl vl-selfcon"><strong>SELF-CONTRADICTED</strong> &mdash; the claim&rsquo;s own cited source, or another item on the same list, points the other way.</div>
    <div class="ds-vl vl-misleading"><strong>MISLEADING</strong> &mdash; real data, but presented so the wrong conclusion looks supported.</div>
    <div class="ds-vl vl-unfalsifiable"><strong>UNFALSIFIABLE</strong> &mdash; outside the domain of testable measurement (scripture, symbolism).</div>
    <div class="ds-vl vl-notdemo"><strong>NOT DEMONSTRATED</strong> &mdash; asserted, but the argument to the conclusion is not actually made.</div>
  </div>
  <p style="font-family:var(--sans);font-size:.85rem;color:var(--ink-3)">Same six-verdict scheme as the
     <a href="https://funwithscience.net/dome-model-review/">dome model review</a>, applied to a claim list instead of a prediction list.</p>
</section>

<!-- ============ PROCESS ============ -->
<section id="process">
  <h2 style="color:var(--heading)">How this review is built</h2>
  <p style="font-size:.95rem">Every verdict cites a public source or a reproducible calculation. We engage the strongest form of each
     argument. Unfalsifiable claims are named rather than mocked. Duplicate items are grouped and scored once per distinct argument, so
     the &ldquo;461&rdquo; headline does not inflate the work. Provenance attributions are traced to a specific publication with a date;
     where an attribution could not be established, the item is recorded as untraced rather than guessed.</p>
  <p style="font-size:.95rem"><strong>Known limits of this pass.</strong> {[x['items'] for x in S['originator_ranking_by_items'] if x['originator']=='(no named originator)'][0]} of
     461 items could not be traced to a named origin. Cluster boundaries involve judgement: a handful of items could defensibly sit in
     an adjacent cluster, which would move counts by a few units without changing any verdict. Carpenter&rsquo;s 1885 pamphlet is the
     earliest numbered proof-list <em>identified</em>, not provably the first &mdash; his own earlier works were not available to check.</p>

  <div class="ds-bn-header" style="margin-top:1.5rem"><h2 style="color:var(--heading);font-size:1.05rem">Version history</h2></div>
  <table>
    <thead><tr><th style="width:8rem">Date</th><th>Change</th></tr></thead>
    <tbody>
      <tr><td>2026-08-02</td><td>Full item-by-item provenance pass over all 461 items: {S['distinct_arguments']} distinct-argument clusters, {S['named_originators']} named originators, verdicts assigned to every item. Added the named source tree (Part 1). <strong>Correction:</strong> the scaffold&rsquo;s estimated family counts (~95 A / ~105 B / ~80 C / ~115 D / ~66 E) were replaced with measured counts (182 A / 54 B / 69 C / 83 D / 73 E). Family B was overestimated roughly twofold and Family A underestimated roughly twofold.</td></tr>
      <tr><td>2026-08-02</td><td>Scaffold: source-tree map, evaluation guide, family sections, seeded Family-A verdicts.</td></tr>
    </tbody>
  </table>
  <p style="font-family:var(--sans);font-size:.85rem;color:var(--ink-3)">Found an error in this review? It should be corrected &mdash; every report is logged and reviewed regardless of outcome.</p>
</section>

<footer style="margin-top:3rem;padding-top:1.2rem;border-top:1px solid var(--rule);font-family:var(--sans);font-size:.85rem;color:var(--ink-3)">
  <p><a href="https://funwithscience.net/" style="color:var(--ink-3)">Fun With Science</a> &middot; an independent review project.
     This page reviews published <em>claims</em>; it does not target any individual.</p>
</footer>

</div>
</body>
</html>
"""

open(OUT, "w", encoding="utf-8").write(head + BODY)
print(f"wrote {OUT} ({len(head + BODY):,} bytes)")
