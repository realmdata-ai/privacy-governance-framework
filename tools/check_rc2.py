"""Targeted rc.2 conformance/arithmetic checks, not empirical or legal validation."""
from pathlib import Path
from decimal import Decimal
import hashlib
import json
import math
import re
import sys

ROOT=Path(__file__).resolve().parents[1]
checks=[]
def check(name,condition,detail=''):
    checks.append({'check':name,'passed':bool(condition),'detail':detail})
def read(doc):
    return next((ROOT/'PGF').glob(f'{doc:02d}_*_EN.md')).read_text(encoding='utf-8')
def band(i):
    if i is None or not math.isfinite(i) or i<0:
        return 'INCOMPLETE'
    return 'Low' if i<.5 else 'Medium' if i<=1 else 'High' if i<=2 else 'Near-certain'

d18=read(18);d8=read(8)
for score,want in [(0,'Low'),(.499999,'Low'),(.5,'Medium'),(1,'Medium'),
                   (1.000001,'High'),(2,'High'),(2.000001,'Near-certain'),(None,'INCOMPLETE'),
                   (float('nan'),'INCOMPLETE'),(-1,'INCOMPLETE')]:
    check('band '+str(score),band(score)==want,want)
for rule in ['0 ≤ I < 0.5','0.5 ≤ I ≤ 1.0','1.0 < I ≤ 2.0','I > 2.0']:
    check('published calibration '+rule,rule in d18)

def section(example):
    match=re.search(r'^# \*\*Example '+re.escape(example)+r'(?:\*\*| —)[^\n]*\n',d18,re.M)
    assert match,example
    end=re.search(r'^# \*\*Example ',d18[match.end():],re.M)
    return d18[match.end():match.end()+end.start()] if end else d18[match.end():]
def number(s):
    match=re.search(r'[-+]?\d+(?:\.\d+)?',s)
    assert match,s
    return float(match.group())/(100 if '%' in s[:match.end()+1] else 1)
def table_rows(text):
    return [[c.strip() for c in line.strip().strip('|').split('|')]
            for line in text.splitlines() if line.startswith('|')]

for ex in ['2.1','2.1-R','2.2','3.1','3.2','3.3']:
    text=section(ex);rows=table_rows(text)
    header=next(row for row in rows if row[0]=='Metric' and 'Normalised' in row)
    vi,ti,wi=header.index('Value'),header.index('Threshold'),header.index('Weight')
    total=0;weights=0;count=0
    for row in rows:
        if len(row)!=len(header) or row==header or not re.fullmatch(r'\d+(?:\.\d+)?',row[wi]):continue
        value,threshold,weight=number(row[vi]),number(row[ti]),float(row[wi])
        if row[0] in ['MIA accuracy','MIA AUC-ROC']:
            normal=abs(value-.5)/(threshold-.5)
        elif row[0]=='DCR P5':
            normal=threshold/value
        elif row[0]=='NNDR median':
            normal=(1-value)/(1-threshold)
        else:normal=value/threshold
        total+=normal*weight;weights+=weight;count+=1
    result=re.search(r'Disclosure indicator = (\d+\.\d+)',text)
    check('example '+ex+' reported indicator exists',result is not None)
    if result:
        reported=float(result.group(1))
        check('example '+ex+' weighted arithmetic',abs(total-reported)<.0012,
              f'raw recomputation {total:.8f}; published {reported}; weighted rows {count}')
        check('example '+ex+' weights sum',abs(weights-1)<.001,f'{weights}')
        if ex!='3.3':
            # 3.3 is legally blocked; its indicator is informative, not permission to process.
            check('example '+ex+' direct band recorded',
                  bool(re.search(r'likelihood(?: of S1)? (?:\*\*)?'+re.escape(band(reported)),text)),band(reported))

# An isolated threshold deviation is review evidence, not a second tier input.
integrated=.01*8+.99*0
check('threshold-deviation counterexample remains Low',band(integrated)=='Low',f'I={integrated}; deviating metric normalised to 8')
check('no new nonlinear calibration', 'No new logarithmic or exponential transformation is introduced' in d18)
check('DPO dissent recorded','dissenting opinion' in d18 and 'decider records the response' in d18)
check('missing selected input explicit','If a selected weighted input' in d18 and 'INCOMPLETE' in d18)
check('legal block retained','**Step 0 — G-L: failed**' in section('3.3') and '**The release is blocked.**' in section('3.3'))
check('business record includes both tracks','Single business decision record' in d8 and 'organisational consequences' in d8)
check('Doc 19 first generator tied out','also calculated Medium (indicator 0.656)' in read(19))
check('PSI residual High preserved','residual High × Significant' in read(19) and 'DPIA-PSI-01' in read(22))
check('FL residual Medium preserved','DPIA-FL-01' in read(19) and 'Medium' in read(19))

for p in sorted((ROOT/'PGF').glob('[0-3][0-9]_*_EN.md')):
    text=p.read_text(encoding='utf-8')
    active='\n'.join(s for s in text.splitlines() if not s.startswith('| 1.0.0-rc.1 |'))
    check(p.name+' no retired algorithm',not re.search(
        r'G-M[1-5]|Override rule:|module FAILS|FAIL reproduced|Mandatory metrics are always gated|passes all gates|passed all gates',active))
    if p.name[:2]!='00':
        pb=re.search(r'^#+\s.*Part B\b',text,re.M)
        check(p.name+' tool-neutral template',bool(pb) and not re.search(r'\bPAMOLA\b',text[:pb.start()]))
    check(p.name+' no malformed table row',not any(s.startswith('|') and not s.rstrip().endswith('|') for s in text.splitlines()))

manifest=json.loads((ROOT/'PGF/SOURCE_MANIFEST.json').read_text(encoding='utf-8'))
for rec in manifest['records']:
    if rec.get('output_path'):
        check(rec['document_id']+' manifest hash',
              hashlib.sha256((ROOT/rec['output_path']).read_bytes()).hexdigest()==rec['output_sha256'])

summary={'scope':'rc.2 structural integration and selected worked-example arithmetic; not empirical, legal or product validation',
         'passed':sum(c['passed'] for c in checks),'failed':sum(not c['passed'] for c in checks),'checks':checks}
if '--json' in sys.argv:
    target=Path(sys.argv[sys.argv.index('--json')+1]);target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps(summary,indent=2,ensure_ascii=False),encoding='utf-8')
for c in checks:
    if not c['passed']:print('FAIL:',c['check'],c['detail'])
print(f"rc.2 targeted checks: {summary['passed']} passed, {summary['failed']} failed")
sys.exit(1 if summary['failed'] else 0)
