# A Shift Law for Central Gaps of Gaussian Binomial Coefficients

**Author:** Gerald W. Hu
**Status:** Public research preprint — **not peer reviewed**.
Revised 2026-11-13 (v1.1.0, external review); v1.1.1 cleanup candidate — see `CHANGELOG.md`.
**Released:** 2026-11-13

## Principal result

Let `g₆(l)` denote the central gap of the Gaussian binomial coefficient
`[l+6 choose 6]_q` (the failure of strict unimodality at the middle rank).
The paper proves:

> **Shift Law.** For every odd integer `l ≥ 17`,
> `g₆(l) = g₆(l − 15)`.

This identity is a consequence of classical invariant theory: `g₆(l)` is the
dimension of the degree-`l` component of the invariant ring of binary sextics,
whose Hilbert series is `(1 + t¹⁵) / ((1−t²)(1−t⁴)(1−t⁶)(1−t¹⁰))` (Grace–Young
1903); an equivalent generating function follows from Appendix A.2 of
Krattenthaler–Kronholm–Marsh (arXiv:2510.14124). The paper's elementary
quasipolynomial proof is a self-contained route to the same identity. The
central contributions are the equivalence and classification results below.

Consequences proved in the package:

- Thresholds `l₀(6,8) = 14`, `l₀(6,12) = 20`, `l₀(6,16) = 26`, each sharp.
- Zero classification: `g₆(l) = 0` if and only if `l` is odd and `1 ≤ l ≤ 13`.
- Exceptional sets `E(6,8) = {3,5,7,9,11,13}` and analogues for `b = 12, 16`.
- Counterexample `(l, j) = (46, 66)` at `(k, b) = (6, 24)` to universal central
  dominance (and a second failure at `(48, 70)`).
- A *partition-level* explanation of the constant 15 remains open
  (Conjecture 9.1 and `proofs/MECHANISM_ATTEMPT.md`); the
  representation-theoretic mechanism is classical.

## What this repository is

The manuscript plus the **complete machine-verification package**: every numeric
claim in the paper is backed by an exact-integer certificate script (Python 3 +
SymPy, no floating point in proof-critical paths), and the package includes an
independent re-derivation of all 3,480 tail obligations.

Verification receipts (all re-run from a clean extraction of the release ZIP):

| Script | Claim | Result |
|---|---|---|
| `verification/verify_shift.py` | Shift law base cases + translate structure | PASS |
| `verification/verify_core.py` | Finite core `l ≤ 121`, coefficient-level | PASS |
| `verification/verify_clearance.py` | Clearance `g₆(l) ≥ Δ_b` for `b = 8, 12, 16` | PASS (90/90) |
| `verification/verify_central.py` | Central dominance certificates | PASS |
| `verification/g6_table.py` | Zero classification | PASS |
| `verification/counterexample_6_24.py` | `(6,24,46)` counterexample | CONFIRMED |
| `verification_independent/independent_check.py` | Independent core re-derivation | PASS |
| `verification_independent/tail_recert.py` | All 3,480 tail obligations re-certified | PASS |
| `verification_independent/helper_contracts.py` | Production helper contracts (15 cases) | PASS |

## Reproduce

Requirements: Python ≥ 3.11, SymPy ≥ 1.12. No network access needed.

```bash
cd verification && bash run_all.sh          # ~25 min, prints PASS per script
cd ../verification_independent
python3 independent_check.py                # ~4 min
python3 tail_recert.py                      # ~10 min, ends: TAIL_RECERT PASS 3480
python3 helper_contracts.py                 # ~1 min, ends: HELPER_CONTRACTS PASS
```

Each script exits non-zero on any mismatch. Precomputed expected values are
hard-coded from the manuscript; deliberate certificate corruption is detected via
AssertionError only (`verification/corrupt_test.sh`, 4/4; harness crashes are
reported as HARNESS ERROR, not detection).

## Integrity

`MANIFEST.sha256` lists SHA-256 hashes of the files of
`math10r-verification.zip` (attached to the release), with paths relative to the
ZIP root; the manifest excludes its own hash. The Git checkout uses `paper/`
where the ZIP uses `manuscript/` (identical bytes); see `PACKAGE_NOTE.md`.
After extracting the release ZIP:

```bash
sha256sum -c MANIFEST.sha256
```

## Layout

- `paper/paper.pdf`, `paper/paper.tex` — the manuscript (15 pages).
- `verification/` — certificate scripts + expected-output receipts + corruption suite.
- `verification_independent/` — second, independently written verifier + helper-contract regressions.
- `proofs/MECHANISM_ATTEMPT.md` — superseded historical attempt (signed-character caveats noted).
- `REPRODUCIBILITY.md`, `CHANGELOG.md`, `AUDIT_SUMMARY.md` — commands, repairs, current audit state.
- `PRIORITY_LEDGER.md` — literature positioning (classical shift; remaining novelty unresolved).
- `INDEPENDENT_VERIFICATION.md`, `REFEREE_REPORT.md`, `REPAIR_LOG.md`, `HERMES_REVIEW.md` — historical audit trail.
- `VERDICT.md` — current disposition first; historical verdicts marked.

## Licensing

- Manuscript (`paper/`): **CC0 1.0 Universal** — see `LICENSE-CC0-1.0.txt`.
- Verification software and documentation: **MIT** — see `LICENSE-MIT.txt`.

## Caveats, stated plainly

- Not peer reviewed. The audit trail here is machine verification plus internal
  and one external (automated) review, not journal refereeing.
- The Shift Law itself is **classical** (binary-sextic invariant theory; see
  `PRIORITY_LEDGER.md`); the earlier *apparently-new* grade was withdrawn in
  v1.1.0. Novelty of the equivalence/classification results is **unresolved**,
  not certified.
- The representation-theoretic mechanism for the constant 15 is classical
  (multiplication by the degree-15 invariant); what remains open is a
  partition-level bijective explanation (proposed as a question; not shown open
  literature-wide).
- The parity pattern for `k > 6` is **observed/conjectural**, not proved.
