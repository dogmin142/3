# SMT-S3 REPORT

Baseline: Smith v13.13
Source SHA-256: `c7a0fc2c7e27ff773ba184829de0138e3c619c39fa9532a1ba10a892359b7449`

## Protocol
Z3 and cvc5 consume identical SMT-LIB bytes. Acceptance requires `unsat` from both solvers for every exact obligation.

## CI evidence
GitHub Actions run `36608873441`, job `109544874466`, commit `8ba8fe4d76e64cf5170c388a028504cdab43f5de`:
- S01 `7aec315005890f65134beb8ca815b4f7a9cf5e5fe0ca111263ef2f2d5462a1b9`: Z3 `unsat`; cvc5 `unsat`.
- S02 `0fd68b8317d8058664044855a23d7b780fe9f6075873015363619c2eb195f1e0`: Z3 `unsat`; cvc5 `unsat`.
- S03 `0a57696266846f9fa7fad3107147d6aefa8e13fdd630170c7f7b28c7af15ca2f`: Z3 `unsat`; cvc5 `unsat`.

## Scope
The formulas use integer-variable products and are encoded as `QF_NIA`. PASS is limited to these exact arithmetic obligations. Matrix equivalence, Smith normal-form semantics, valuation/rank arguments and tower propagation remain separate proof obligations.

## Verdict
**SMT-S3 ARITHMETIC PASS.**
