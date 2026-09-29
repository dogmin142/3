# SMT-S3 ONE SHOT

Two independent solver families: Z3 and cvc5.
Exact same `.smt2` bytes are hashed and sent to both solvers.
Acceptance criterion: every obligation returns `unsat` on both solvers.
Scope: exact integer arithmetic threshold layer only.
