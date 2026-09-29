#!/usr/bin/env python3
import hashlib,pathlib,shutil,subprocess,sys,json
S={'z3':['z3','-smt2'],'cvc5':['cvc5','--lang=smt2']}
missing=[k for k,v in S.items() if not shutil.which(v[0])]
if missing: print('SMT-S3 NOT ATTAINED: missing '+','.join(missing));sys.exit(2)
rows=[];ok=True
for p in sorted(pathlib.Path('smt').glob('*.smt2')):
 row={'spec':p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
 for k,c in S.items():
  q=subprocess.run(c+[str(p)],capture_output=True,text=True,timeout=60)
  a=q.stdout.strip().splitlines()[0] if q.stdout.strip() else 'ERROR';row[k]=a;ok &= a=='unsat'
 rows.append(row)
print(json.dumps(rows,indent=2));print('SMT-S3 ARITHMETIC PASS' if ok else 'SMT-S3 NOT ATTAINED');sys.exit(0 if ok else 1)
