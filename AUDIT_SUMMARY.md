# AUDIT SUMMARY — current state vs. historical logs (v1.1.1 candidate, 2026-11-13)

This is a distilled, current audit summary for the public package. It separates
**current verification receipts** from **historical internal logs**.

## Current acceptance status (v1.1.1 candidate)

| Gate | Result | Receipt (current run) |
|---|---|---|
| Canonical certificate suite (7 scripts, exact arithmetic) | PASS | `verification/out/RUNALL_111.out` |
| Corruption suite (4 mutants, AssertionError-only detection) | PASS | `verification/out/CORRUPT_111.out` |
| Independent core checker (core l<=121, mismatches assert) | PASS | `verification_independent/INDEPENDENT_CHECK_111.out` |
| Independent tail recertification (all 3,480 obligations) | PASS | `verification_independent/TAIL_RECERT_111.out` |
| Production helper contracts (15 cases, incl. 3 brute-forced) | PASS | `verification_independent/HELPER_CONTRACTS_11.out` |
| Falsification: core-mismatch injection -> AssertionError, rc=1 | PASS | this summary (2026-11-13 session) |
| Falsification: counterexample premise falsified -> rc=1 | PASS | this summary |
| Falsification: forced unbounded obligation -> guard fails; sentinel conversion would silently pass | PASS | this summary |
| Falsification: missing interpreter -> HARNESS ERROR, not DETECTED | PASS | this summary |
| LaTeX build: 0 undefined refs, 0 `??`, 0 overfull boxes, 15 pages | PASS | build log inspected 2026-11-13 |

Coverage census (reconstructed, not inferred from volume): tail obligations are
exactly 3 * 60 * (h-1) = 480 + 1080 + 1920 = 3,480 for b in {8,12,16}; finite core
is every admissible l <= 121; clearance is 90/90 base+tail obligations. These match
the domains certified in the manuscript.

## Known limitations (unchanged, stated plainly)

- Not peer reviewed; no human specialist has assessed the remaining
  equivalence/classification contribution or its novelty. Novelty of those results
  is UNRESOLVED, not certified.
- The Shift Law itself is classical (binary-sextic invariant theory; KKM Appendix A.2).
- Uniqueness of the shift 15 is numerically verified, not proved; the parity pattern
  for k>6 is observed/conjectural; a partition-level mechanism is an open question,
  not shown open literature-wide.
- `INDEPENDENT_VERIFICATION.md`, `REFEREE_REPORT.md`, `REPAIR_LOG.md`, `HERMES_REVIEW.md`
  are historical audit-trail documents; their blanket verdicts predate the v1.1.0/v1.1.1
  corrections and are marked as such where applicable.

## Artifact identity

Baseline tag: v1.1.0 @ 6f32c42. The v1.1.1 candidate changes exposition, verifier
contracts, citations, and packaging only; no theorem statement is altered
(see CHANGELOG.md). Manifest and asset hashes are generated after all files are final.
