#!/usr/bin/env python3
import hashlib,pathlib,shutil,subprocess,sys,json
solvers={'z3':['z3','-smt2'],'cvc5':['cvc5','--lang=smt2']}
missing=[s for s,c in solvers.items() if not shutil.which(c[0])]
if missing:
 print('SMT-S3 NOT ATTAINED: missing '+','.join(missing));sys.exit(2)
rows=[];ok=True
for p in sorted(pathlib.Path('smt').glob('*.smt2')):
 b=p.read_bytes();r={'spec':p.name,'sha256':hashlib.sha256(b).hexdigest()}
 for name,cmd in solvers.items():
  x=subprocess.run(cmd+[str(p)],capture_output=True,text=True,timeout=60)
  ans=x.stdout.strip().splitlines()[0] if x.stdout.strip() else 'ERROR';r[name]=ans;ok=ok and ans=='unsat'
 rows.append(r)
print(json.dumps(rows,indent=2));print('SMT-S3 ARITHMETIC PASS' if ok else 'SMT-S3 NOT ATTAINED');sys.exit(0 if ok else 1)
