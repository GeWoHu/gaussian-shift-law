# MATH-10R — VERDICT (2026-11-13, closed T+~55 of 120 min)

## Mission
Repair the MATH-10 Shift Law manuscript, independently verify its claims, adversarially
review, and package for external human review. Verification/repair only — no new research.

## Final Decision (reported independently)

**Mathematics: PROVED**
Theorem 1 (Shift Law, odd l≥17), Theorem 2 (central-gap equivalence on (6,8),(6,12),(6,16)
× admissible l; 3,480 tail obligations + core l≤121), Theorem 3 (exact exceptional sets;
sharp thresholds 14/20/26 with the repaired l0e−2 translate argument), Proposition 4
((6,24,46)/(6,24,48)), and Lemma 14 (cubic minimum test) survived: (a) the full certificate
suite (7/7 PASS, exact arithmetic, exact derivative-root comparisons), and (b) an independent
verifier working from its own code paths — including an independent re-certification of all
3,480 tail obligations (tail_recert.py: TAIL_RECERT PASS, maxdeg 3, min margin 2126).

**Independent reproduction: PASS**
Clean extraction of math10r-verification.zip into a fresh directory reproduced verify_core,
counterexample, g6_table, verify_clearance, verify_shift (exit 0, "SHIFT LAW k=6 PROVED")
from the extraction alone. Deliberate corruption: 4/4 mutants detected (falsifying mutants;
equivalent-mutant lesson from MATH-10 applied).

**Novelty: APPARENTLY-NEW**
Qualified claim only — "not found in the sources cited"; no priority assertion (verified
present tense in manuscript §1/§10 and PRIORITY_LEDGER.md). Referee and independent verifier
both concur; human literature review remains the gate before submission.

**Publication readiness: READY-FOR-HUMAN-REVIEW**
Hostile referee (separate session, Nemotron-3-Ultra-550B): all 8 attack areas RESOLVED with
documented evidence (including personal reruns of the fast certificates, the corruption
suite, and hand evaluation of 3 branch identities including a wrapped residue class);
VERDICT: APPROVED. Its single MINOR item (MECHANISM_ATTEMPT.md path) was fixed before close.
No failed proof obligations. Verifier round-1 PARTIAL (tails) was closed by the independent
3,480/3,480 re-certification.

**Release gate: BLOCKED — awaiting explicit owner authorization.**
No public release, no repository push, no journal submission performed. No automatic MATH-11.

## Repairs executed (Phase I; full detail REPAIR_LOG.md)
1. Theorem 3 sharpness: translate is l0e−2 (even), not l0e−1; b=8 (l0e=0) separated as the
   direct case; all three threshold cases rechecked (g6(4)=2<3, g6(10)=6<7, g6(13)=0<1).
2. References verified against primary records: O'Hara JCTA 53 (1990) 29–52; Reiner–Stanton
   J. Algebraic Combin. 7 (1998) 91–107; SZ J. Combinatorics 11 (2020) 111–126; KUW ISSAC
   2023; Chen–Jia IJM 32 (2021); Dhand Discrete Math. 335 (2014); Sylvester title corrected
   to the KUW/SZ citation form.
3. Parity statements relabeled: proved content is k=6 only; kl≡2 (mod 4) pattern labeled
   observed/conjectural for k>6.
4. Notation audit: intro growth claim corrected (degree-3 branches, not l²); conventions,
   admissibility starts, wrapped-class indexing, threshold formula re-checked.
5. Typesetting: 4 overfull-box fixes; no undefined references; 14 pp.
6. Certificate exactness: derivative-root candidate gate switched from float() to exact
   sympy comparisons in the math10r canonical scripts.

## Open items (explicit, unresolved by design)
- Combinatorial mechanism for the constant 15: OPEN (documented honest failure).
- Uniqueness of shift 15: numerically established only (labeled as such in paper and scripts).
- Extension to (6,20)/(6,24) and k>6: open, unchanged scope.
- gauss (1).pdf was not found on this host; the frozen math10 archive served as the
  authoritative manuscript (logged). If it differs from the delivered paper, diff on receipt.

## Packaging
math10r/: manuscript/paper.tex + paper.pdf (14 pp), verification/ (7 certificates +
run_all.sh + corrupt_test.sh + receipts out/, corrupt_tmp/), verification_independent/
(independent_check.py, tail_recert.py), proofs/MECHANISM_ATTEMPT.md, INDEPENDENT_VERIFICATION.md,
REFEREE_REPORT.md (+ editor's note), REPAIR_LOG.md, PRIORITY_LEDGER.md, REPRODUCIBILITY.md,
VERDICT.md, CHECKPOINT.json, EXTRACTION_TEST.out, MANIFEST.sha256, math10r-verification.zip.
Clean-extraction reproduction receipt: EXTRACTION_TEST.out (all exit 0).
Archives math06–math10 untouched (no writes; verified).

---

## ADDENDUM — v1.1.0 after external review (Hermes, 2026-11-13, HERMES_REVIEW.md)
- Mathematics: PROVED — unchanged; all certificates, thresholds, exceptional sets,
  and both (6,24) counterexamples reproduced by the external reviewer independently.
- Novelty: DOWNGRADED. The Shift Law is an immediate consequence of the classical
  Hilbert series of the binary-sextic invariant ring and follows from KKM
  Appendix A.2(1)-(2) (a source already in the bibliography). The earlier
  APPARENTLY-NEW grade is withdrawn. Remaining claimed contributions: the
  central-gap equivalence over the certified domain, the exact exceptional-set
  classifications with sharp thresholds, and the certified (6,24) failure —
  novelty of these was not established either way.
- Mechanism: the representation-theoretic mechanism is classical (degree-15 odd
  generator E; multiplication by E). The open problem is restated at the
  partition level only.
- The internal blanket "all resolved / APPROVED" referee verdict was too strong:
  five textual errors and four verifier-contract weaknesses (none overturning a
  result) had been missed; all repaired in v1.1.0 and re-verified.
- Publication readiness: READY-FOR-HUMAN-SPECIALIST-REVIEW (supersedes
  READY-FOR-HUMAN-REVIEW wording of v1.0.0).
