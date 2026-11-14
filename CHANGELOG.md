# CHANGELOG — gaussian-shift-law

## v1.1.1 (candidate, 2026-11-13) — cleanup of exposition, verifier contracts, citations, packaging
No theorem statement changed. Maps each finding of the v1.1.0 recheck audit to its repair.

1. **Staircase bullet rewritten** (§9.2): correct domains — for l>=6, subtracting
   (5,4,3,2,1,0) bijects strict partitions with exactly 6 positive parts, largest part
   <= l, onto partitions into exactly 6 positive parts, largest part <= l-5 (inverse adds
   delta; positivity and width bounds preserved; weight drops by 15). Contradictory
   "captures the exact-6-row summand" sentence removed; failure to give l -> l-15 stated.
2. **Arithmetic sentence repaired** (§5): at l=12, i+j=11 the pair arguments are 1 and 0,
   not -1 and -2; spurious negative-index exception removed. Q6(m)=p(m)-p(m-1) identity kept.
3. **Production tail helper hardened** (`verification_independent/tail_recert.py::minint`):
   explicit contract; rejects negative-leading nonconstant polynomials (3-t -> None);
   zero/constant cases explicit; degree bound asserted; caller fails on rejected obligations.
   New regression `helper_contracts.py` tests the production helpers themselves (15 cases,
   3 brute-force cross-checked).
4. **Independent g(0) fixed** (`independent_check.py`): zero extension outside the
   coefficient range; explicit assertion g6(0)=1; nondegenerate values unchanged.
5. **Sample-cubic explanation corrected** (Appendix): C'(t)=30(240t^2+28t-1) has roots
   (-7±sqrt(109))/120, both below 2; candidate set reduces to {t=2}. The prior claim of a
   derivative root exceeding 2 was wrong and is removed.
6. **Mechanism note labeled** (`proofs/MECHANISM_ATTEMPT.md`): marked superseded historical
   attempt; distinguishes alternating virtual characters prod(1-q^d) from ordinary
   exterior-algebra Hilbert series prod(1+q^d); classical invariant-ring mechanism is now
   established background, not an open representation-theoretic problem.
7. **Directionality wording narrowed** (§9.2 item 4): justified absence of global period-15
   symmetry only.
8. **References**: `sec:intro` label added (no `??` in PDF); Grace–Young corrected to
   J. H. Grace and A. Young, *The Algebra of Invariants*, 1903 (catalog-verified; no page
   locator claimed); Pak–Panova arXiv:1410.7087 title corrected to *Bounds on Kronecker and
   q-binomial coefficients* (arXiv-verified); Stanley section locator and Andrews chapter
   locator removed (not verified); companion preprints M06–M09 labeled unpublished with no
   stable identifier and marked not relied upon for theorems.
9. **Author/disclosure**: LaTeX author is the human author alone; AI assistance moved to an
   Acknowledgments and disclosure section.
10. **Layout**: all overfull boxes eliminated (was 4); fixed version date retained.
11. **Equivalence wording**: "consequence of the classical Hilbert series" (no unproved
    logical equivalence asserted).
12. **(k,b)=(6,24)** label order corrected in README/CITATION/release prose; numerical
    counterexamples unchanged.
13. **Packaging**: verification ZIP now contains README.md, both license texts, CHANGELOG,
    AUDIT_SUMMARY, and PACKAGE_NOTE.md (ZIP layout vs Git layout; license scope); manifest
    generated last, excludes its own hash; reproduction commands executable as written from
    a clean extraction; counts programmatically computed.
14. **VERDICT.md** restructured: current disposition first; original v1.0.0 close and v1.1.0
    addendum marked historical. HERMES_REVIEW.md labeled as an abridgment.

## v1.1.0 (2026-11-13, published) — major revision after external review
Reframing around classical invariant theory + KKM App A.2; five textual errors fixed;
first round of verifier-contract hardening. See HERMES_REVIEW.md and the v1.1.0 release.

## v1.0.0 (2026-11-13, published) — initial public research preprint
Shift Law + complete exact-integer verification package.
