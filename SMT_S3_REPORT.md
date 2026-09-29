# SMT-S3 REPORT

Baseline: Smith v13.13
Source SHA-256: `c7a0fc2c7e27ff773ba184829de0138e3c619c39fa9532a1ba10a892359b7449`

Protocol: Z3 and cvc5 consume identical SMT-LIB bytes; runner records SHA-256 for every exact spec. Acceptance requires UNSAT from both solver families for every obligation.

Obligations: S01 supercritical integer threshold; S02 critical equality normalization; S03 subcritical integer threshold.

Scope: FULL-NATIVE only for the encoded Presburger arithmetic. Matrix left-right equivalence, Smith normal form, valuation/rank semantics and tower propagation are not claimed as native SMT evidence.

Verdict is supplied only from GitHub Actions execution evidence.
