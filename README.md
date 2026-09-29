# Smith SMT-S3 clean-room verification

Baseline: `Smith_v13_13_VERIFYMAX_REWRITE.tex`

Z3 and cvc5 consume identical SMT-LIB bytes. Every obligation encodes hypotheses plus negated arithmetic conclusion; `UNSAT` from both independent solver families is required.

Native SMT scope is limited to exact integer-arithmetic threshold obligations. Matrix equivalence, Smith normal form semantics, valuation/rank semantics, and tower propagation remain outside native SMT scope.