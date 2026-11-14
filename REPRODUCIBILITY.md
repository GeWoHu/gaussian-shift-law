# MATH-10R — Reproducibility Record

Mission window: 2026-11-13 19:12–21:12 CST (closed T+~50 min).

## Environment
- Host: fedora, kernel 7.2.15-300.fc45.x86_64, AMD Ryzen AI MAX+ 395
- Python 3.15.2, sympy 1.14.0 — exact integer/rational arithmetic only.
  In the math10r certificates the derivative-root gate is an EXACT sympy comparison
  (`root >= T0` on CRootOf/algebraic numbers via isolation intervals); no floating-point
  value decides any certificate (referee-verified by source read; grep `float(` finds none
  in verify_central.py / verify_clearance.py certificate paths).
- LaTeX: tectonic 0.15.0. Bibliography verified against api.crossref.org (19:14–19:20 CST).

## Commands (from projects/math-research/math10r/)
```
bash verification/run_all.sh        # 7 certificates, receipts verification/out/*.out
bash verification/corrupt_test.sh   # 4 mutants, receipts verification/corrupt_tmp/*.out
bash run_full.sh                    # both, combined exit code
python3 verification_independent/independent_check.py   # independent re-derivation (verifier)
python3 verification_independent/tail_recert.py         # independent 3,480-obligation re-cert
```

## Observed outcomes (this mission)
- `math10r-suite2` durable job (19:26–19:33 CST): **FULL PASS** — g6_table PASS;
  counterexample CONFIRMED (−86 at degrees 132→133; −11 at 142→143); verify_core PASS
  (l ≤ 121, 3 families, 0 mismatches); verify_shift SHIFT LAW PROVED (S1–S4);
  verify_clearance PROVED (90/90 + bases); verify_central 480/480, 1080/1080, 1920/1920
  PASS (maxdeg=3); shift_uniqueness NUMERICAL only c=15.
- Corruption suite rerun 19:32 CST: **PASS, 4/4 detected** (corrupt_base, corrupt_shift,
  corrupt_signflip, corrupt_threshold; each exits nonzero; AssertionError receipts kept).
- Exact-comparison smoke (19:25 CST): verify_clearance.py exit 0, 90/90, 1.1 s.
- Independent verifier (round 1, 19:26–19:30): independent_check.py — shift mechanism,
  finite cores, classification, Prop 4 coefficients, Lemma stress cases (negative-leading,
  degenerate linear, constant negative, double derivative root, root at T0, irrational
  CRootOf), Crossref spot checks — all PASS; 0 discrepancies.
- Independent tail re-certification (19:33–19:41): tail_recert.py — **TAIL_RECERT PASS
  3480 certificates, max_degree 3**, minimum margin 2126 at (8,0,6,2).
- Hostile referee (19:33–19:43): ran verify_core/verify_clearance/counterexample/g6_table
  and corruption suite personally; spot-evaluated 3 branch identities including a wrapped
  class; VERDICT: APPROVED (see REFEREE_REPORT.md + editor's note).

## Deliberate corruption design note
Mutants must FALSIFY the certified statement (r1 lesson from MATH-10: two equivalent
mutants survived because the perturbed claim was still true). corrupt_signflip and
corrupt_threshold(7→9) falsify; corrupt_base and corrupt_shift falsify by data perturbation.

## Clean-extraction test
`math10r-verification.zip` extracted to a fresh directory and the fast certificates re-run
from the extraction (see VERDICT.md §Packaging for the observed PASS output).

## Hashes
MANIFEST.sha256 covers every package file (sha256sum -c verified before zipping; the
manifest itself is included in the zip after verification).

## v1.1.0 (2026-11-13, post-external-review)
Verifier contracts strengthened: `verify_central.py` rejects negative-leading
linear polynomials in `nonneg()`; `independent_check.py` now exits nonzero on any
finite-core mismatch and its lemma stress test calls a real minimum routine
(6 cases, including rejection of `3-x`); `corrupt_test.sh` accepts only
`AssertionError` failures as detection and flags harness crashes (rc >= 126,
syntax errors, unchanged mutants); `counterexample_6_24.py` asserts its premise
(`g6 >= Delta` at each counterexample). Commands unchanged. v1.1.0 receipts:
`verification/out/RUNALL_11.out`, `verification/out/CORRUPT_11.out`,
`verification_independent/INDEPENDENT_CHECK_11.out`,
`verification_independent/TAIL_RECERT_11.out`.

## v1.1.1 (2026-11-13) — helper contracts and packaging
New: `verification_independent/helper_contracts.py` regression-tests the PRODUCTION
helpers (`tail_recert.minint` contract incl. rejection of `3-t`; `verify_central.nonneg`
extracted verbatim). `tail_recert.py` now asserts on rejected (unbounded-below)
obligations; `independent_check.py` zero-extends outside the coefficient range so
g6(0)=1 per the paper convention (asserted). v1.1.1 receipts: RUNALL_111.out,
CORRUPT_111.out, INDEPENDENT_CHECK_111.out, TAIL_RECERT_111.out, HELPER_CONTRACTS_11.out.
