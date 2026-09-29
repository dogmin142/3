#!/usr/bin/env python3
import hashlib,pathlib,shutil,subprocess,sys,json
solvers={'z3':['z3','-smt2'],'cvc5':['cvc5','--lang=smt2']}
missing=[s for s,c in solvers.items() if shutil.which(c[0]) is None]
if missing:
 print('SMT-S3 NOT ATTAINED — missing solvers: '+', '.join(missing));sys.exit(2)
rows=[];ok=True
for p in sorted(pathlib.Path('smt/specs').glob('*.smt2')):
 b=p.read_bytes();row={'spec':p.name,'sha256':hashlib.sha256(b).hexdigest()}
 for s,cmd in solvers.items():
  q=subprocess.run(cmd+[str(p)],capture_output=True,text=True,timeout=60)
  out=q.stdout.strip().splitlines()[0] if q.stdout.strip() else 'ERROR';row[s]=out;ok &= out=='unsat'
 rows.append(row)
print(json.dumps(rows,indent=2))
print('SMT-S3 ARITHMETIC STRUCTURAL PASS' if ok else 'SMT-S3 NOT ATTAINED')
sys.exit(0 if ok else 1)
