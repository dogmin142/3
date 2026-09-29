# Dedekind v5.9 — FULL mathematical-claim ledger

Authoritative source SHA-256: `557a4902a9498da1e7f2f27b2feeba4d51b7b3f5451f1f56a2b1d71d9b8b00cc`.

Status vocabulary: `OPEN`, `SMT`, `LEAN`, `EXTERNAL`, `CLOSED`. FULL certification requires OPEN=0 and every EXTERNAL bridge to name its exact imported theorem/source rather than assume the target conclusion.

## G — global obstruction
G1 scalar-shift invariance — OPEN
G2 rank-one family independence — OPEN
G3 annihilator d_Q^2 — OPEN
G4 difference-coordinate quotient — OPEN
G5 alpha_1,p=0 — OPEN
G6 local cyclic decomposition — OPEN
G7 global Dedekind assembly — OPEN
G8 obstruction-ideal ordering/e_1=d_Q^2 — OPEN
G9 determinantal recovery/integrality — OPEN
G10 reference independence — OPEN

## C — counting/reconstruction
C1 finite local cardinality formula — OPEN
C2 first-difference reconstruction — LEAN(partial arithmetic atom)
C3 recovery of beta multiset — OPEN
C4 recovery of global module — OPEN

## D — determinantal/exterior layers
D1 rank-2 minor identity — OPEN
D2 rank-2 determinantal ideal identity — OPEN
D3 rank-3 minor identity — OPEN
D4 rank-3 determinantal ideal identity — OPEN
D5 e2 formula — OPEN
D6 e3 formula — OPEN
D7 dimension-3 specialization — OPEN
D8 dimension-4 Hodge bridge — OPEN
D9 residue-field consequence — OPEN

## H — Householder
H1 content/b_v/r_i integrality and scaling invariance — OPEN
H2 denominator valuation formula — OPEN
H3 local presentation — OPEN
H4 local invariant exponents — OPEN
H5 global cyclic assembly — OPEN
H6 generic exponent bounds — LEAN(partial arithmetic atom)
H7 Fitting ideal formula — OPEN
H8 cardinality bounds — OPEN
H9 equality cases — OPEN
H10 dyadic correction identity — OPEN
H11 class formula — OPEN
H12 primitive consequence — OPEN
H13 square-subgroup realization — OPEN

## E — exact nonprincipal example
E1 O_K and p^2=(2), p nonprincipal — OPEN
E2 Q^TQ=I and d_Q=p — OPEN
E3 exact minor valuations — OPEN
E4 final module decomposition — OPEN

## Certification gate
No `FULL PASS` until source bytes are present and hash-locked, SMT-native obligations have dual-solver certificates, Lean bridges compile with no sorry/admit/custom axiom, dependency/circularity audit is clean, and OPEN=0.
