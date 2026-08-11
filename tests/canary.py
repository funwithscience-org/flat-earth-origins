#!/usr/bin/env python3
"""Mutation test for the invariant suite: break one thing, confirm it goes red, restore.

A check that has never failed is unverified, and on 2026-08-11 two of them turned out to
be decorative. Run this after adding checks, not just after adding claims:

    python3 tests/canary.py

Take one of this harness was itself invalid. Damage from one mutation leaked into
the next because a restored source file can land with an mtime that still matches the
.pyc compiled from the mutated version, so Python served stale bytecode and three
'CAUGHT' results were catching the wrong thing. tests/run.sh now clears __pycache__
first, and this harness re-runs the suite after each restore rather than assuming it
worked.

Adding a mutation is cheap and worth doing whenever a check is added. A SKIP means the
mutation string no longer matches the source - fix the harness, it is not a pass."""
import subprocess, shutil, os
ROOT='/home/claude/spinning-ball-review'
F={k:f'{ROOT}/scripts/{k}.py' for k in ('clusters','assign','render','build','people','works')}
def run():
    r=subprocess.run(['bash','tests/run.sh'],cwd=ROOT,capture_output=True,text=True)
    out=r.stdout+r.stderr
    return r.returncode,[l.strip()[6:].strip() for l in out.splitlines() if l.strip().startswith('FAIL')]
def clean():
    rc,_=run(); return rc==0
M=[
 ("verdict flipped on a cluster",'clusters','verdict="MISLEADING", note="Mach','verdict="REFUTED", note="Mach'),
 ("originator silently changed",'clusters','originator="Eric Dubay"','originator="Samuel Rowbotham"'),
 ("a cluster's lane changed",'clusters','"B08": dict(lane="B"','"B08": dict(lane="E"'),
 ("pre-modern given an originator",'clusters','"C02": dict(lane="C"','"C02": dict(lane="C", originator_OVERRIDE="x"'),
 ("an item reassigned",'assign','1:"A01",2:"A02"','1:"A02",2:"A02"'),
 ("strapline reverts to the false claim",'render',"{S['total_items']} claims sorted by where","tracing {S['total_items']} claims back to"),
 ("'most' claimed of a minority",'render',"Most of those items rest on something published","Nearly all of those items rest on something published"),
 ("ninety-year claim reinstated",'render','experimental authority in this tradition is','tradition has not produced a new experiment in about ninety years and the authority is'),
 ("Knodel called competently run",'render',"design, the right instrument for the quantity","measurement, competently run, on the quantity"),
 ("flow balance assert disabled",'build','assert sum(b["itemCount"] for b in _bands)','assert True or sum(b["itemCount"] for b in _bands)'),
 ("a person's lineage flipped",'people','lineage="Tychonian",','lineage="Zetetic",'),
 ("SOURCE NOT LOCATED removed",'render',"'SOURCE NOT LOCATED'","''"),
 # the 2026-08-11 biography integration: seventeen agent returns in three wire-formats,
 # normalised by one script. These are the failure modes that survive a diff read.
 ("a bio reverts to stub",'people','    bio_status="worked",\n    formation=(\n        "A signwriter','    bio_status="stub",\n    formation=(\n        "A signwriter'),
 ("escaped markup left in a bio",'people','"A signwriter in Dover','"&lt;p&gt;A signwriter in Dover'),
 ("CDATA wrapper left in a bio",'people','"A signwriter in Dover','"<![CDATA[A signwriter in Dover'),
 ("markup leaks into an escaped field",'people','role=(\n        "Institutional, not originating','role=(\n        "<em>Institutional</em>, not originating'),
 ("kernel keeps the renderer's own heading",'people','description=(\n            "For the whole of his active career','description=(\n            "<strong>The kernel.</strong> For the whole of his active career'),
 ("a dated changelog row goes live again",'render',"'light. First arguments at full treatment; first biographies worked.</td></tr>'",'f\'light. First arguments at full treatment; first biographies worked ({S["bios_worked"]}).</td></tr>\''),
 ("plagiarism attributed to a person",'people','"is a statement about a source','"is what Dubay plagiarised. That is a statement about a source'),
]
assert clean(), "tree not green before starting"
res=[]
for name,f,old,new in M:
    p=F[f]; src=open(p).read()
    if old not in src: res.append((name,'SKIP','target not found')); continue
    shutil.copy(p,p+'.bak'); open(p,'w').write(src.replace(old,new,1))
    rc,fails=run()
    shutil.move(p+'.bak',p)
    ok=clean()
    res.append((name,'CAUGHT' if rc!=0 else 'MISSED', (fails[0][:60] if fails else '—') + ('' if ok else '  [RESTORE FAILED]')))
w=max(len(r[0]) for r in res)
for n,v,d in res: print(f"  {v:<7} {n:<{w}}  {d}")
print(f"\n  caught {sum(1 for r in res if r[1]=='CAUGHT')}/{len(res)}   MISSED {sum(1 for r in res if r[1]=='MISSED')}   skipped {sum(1 for r in res if r[1]=='SKIP')}")
