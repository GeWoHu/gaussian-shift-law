# A Shift Law for Central Gaps of Gaussian Binomial Coefficients

**Author:** Gerald W. Hu
**Status:** Public research preprint — **not peer reviewed**.
**Released:** 2026-11-13

## Principal result

Let `g₆(l)` denote the central gap of the Gaussian binomial coefficient
`[l+6 choose 6]_q` (the failure of strict unimodality at the middle rank).
The paper proves:

> **Shift Law.** For every odd integer `l ≥ 17`,
> `g₆(l) = g₆(l − 15)`.

Consequences proved in the package:

- Thresholds `l₀(6,8) = 14`, `l₀(6,12) = 20`, `l₀(6,16) = 26`, each sharp.
- Zero classification: `g₆(l) = 0` if and only if `l` is odd and `1 ≤ l ≤ 13`.
- Exceptional sets `E(6,8) = {3,5,7,9,11,13}` and analogues for `b = 12, 16`.
- Counterexample `(l, j) = (46, 66)` at `(b, k) = (6, 24)` to universal central
  dominance (and a second failure at `(48, 70)`).
- The combinatorial reason the constant is **15** remains **open** (Conjecture 9.1
  and `proofs/MECHANISM_ATTEMPT.md`).

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

## Reproduce

Requirements: Python ≥ 3.11, SymPy ≥ 1.12. No network access needed.

```bash
cd verification && bash run_all.sh          # ~25 min, prints PASS per script
cd verification_independent
python3 independent_check.py                # ~4 min
python3 tail_recert.py                      # ~10 min, ends: TAIL_RECERT PASS 3480
```

Each script exits non-zero on any mismatch. Precomputed expected values are
hard-coded from the manuscript; a corrupted certificate is detected (see
`verification/corrupt_test.sh` suite, 4/4 corruptions detected).

## Integrity

`MANIFEST.sha256` lists SHA-256 hashes of all 39 files in
`math10r-verification.zip` (attached to the `v1.0.0` release), with paths
relative to the ZIP root. After extracting the release ZIP:

```bash
sha256sum -c MANIFEST.sha256
```

## Layout

- `paper/paper.pdf`, `paper/paper.tex` — the manuscript (14 pages).
- `verification/` — certificate scripts + expected-output receipts + corruption suite.
- `verification_independent/` — second, independently written verifier.
- `proofs/MECHANISM_ATTEMPT.md` — strongest partial attempt at explaining the constant 15.
- `REPRODUCIBILITY.md` — environment, commands, expected outputs.
- `PRIORITY_LEDGER.md` — literature positioning (qualified; no priority claim made).
- `INDEPENDENT_VERIFICATION.md`, `REFEREE_REPORT.md`, `REPAIR_LOG.md` — audit trail.
- `VERDICT.md` — final verification verdict.

## Licensing

- Manuscript (`paper/`): **CC0 1.0 Universal** — see `LICENSE-CC0-1.0.txt`.
- Verification software and documentation: **MIT** — see `LICENSE-MIT.txt`.

## Caveats, stated plainly

- Not peer reviewed. The audit trail here is machine verification plus an
  adversarial internal review process, not journal refereeing.
- Novelty is stated as *apparently new* only; no priority is asserted. See
  `PRIORITY_LEDGER.md`.
- The parity pattern for `k > 6` is **observed/conjectural**, not proved.
