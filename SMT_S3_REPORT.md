# SMT-S3 REPORT

Baseline: Smith v13.13
Source SHA-256: `c7a0fc2c7e27ff773ba184829de0138e3c619c39fa9532a1ba10a892359b7449`

## Protocol
- Solver family 1: Z3
- Solver family 2: cvc5
- Both consume identical SMT-LIB files.
- `run_s3.py` records SHA-256 for every exact spec.
- Acceptance: Z3=UNSAT and cvc5=UNSAT for every obligation.

## Obligations
- S01: supercritical integer threshold implication.
- S02: critical equality normalization.
- S03: subcritical integer threshold implication.

## Scope qualification
These three obligations are FULL-NATIVE only for the encoded Presburger-arithmetic layer. They do not by themselves verify matrix left-right equivalence, Smith normal form semantics, valuation identities, residual rank arguments, or propagation/tower statements.

## Current verdict
PENDING CI EXECUTION. No SMT-S3 PASS is claimed until the GitHub Actions run returns UNSAT for all specs on both solver families.
