# MATH-10R Phase III — Hostile Referee Report
**Date:** 2026-11-13  
**Scope:** projects/math-research/math10r/ (manuscript, verification, independent verification, repair log)  
**Method:** Every claim below is grounded in a command I ran or a line I read. UNVERIFIED where I could not check.

---

## 1. Hidden assumptions / missing parameter values

| Item | Objection | Resolution |
|------|-----------|------------|
| **Admissibility 3l ≥ b²/8** | The paper defines admissibility as 3l ≥ h where h=b²/8. For b=8,12,16 this gives h=8,18,32 → l≥3,6,11. The core verification loops use `start = (h+2)//3` which computes 3,6,11 correctly. **CLEAN.** | RESOLVED |
| **l≥1 vs l≥k conventions** | The Gaussian polynomial $\genfrac{[}{]}{0pt}{}{l+6}{6}$ requires l≥0 for a nonempty rectangle. The paper uses l≥12 for the inclusion–exclusion identity (*) survival (Lemma 6), and l≥17/27 for the Shift Law. No claim is made for l<3 (b=8), l<6 (b=12), l<11 (b=16). The zero classification (l=1..13 odd) is a finite DP fact, not a convention. **CLEAN.** | RESOLVED |
| **g₆(0)=1 convention** | Paper Remark 1(iii): "g₆(0):=1 (from a₀(0)=1, a₀(−1)=0)". This makes the Shift Law instance l=15 true (g₆(15)=1=g₆(0)), but l=15 and l=0 are kept outside Theorem 1 because the box degenerates. The convention is explicitly stated and used only for the threshold formula l₀=l₀ₑ+14. **CLEAN (documented, non-essential).** | RESOLVED |
| **Wrapped residue classes r<15** | For odd r∈{1,3,5,7,9,11,13}, l=60t+r gives l−15=60(t−1)+(r+45). The branch polynomial for l−15 uses G_{r+45}(t−1). The code `Gsym(r)` handles floor division correctly: `(coef*r+off)//60` automatically produces the −1 carry. I verified r=7 at t=1,2,3 against r=52 at t=0,1,2 — exact match (see §2). The paper explains this in §6.2 "the wrap convention above". **CLEAN.** | RESOLVED |
| **l=15 instance exclusion** | Theorem 1 states "for every odd l≥17". l=15 is excluded (degenerate box, though g₆(15)=1=g₆(0) holds by convention). The finite base S4 checks l=17,19,21,23,25. l=15 is not in the theorem's domain. **CLEAN.** | RESOLVED |
| **b divisible by 4** | The family definition requires b≡0 (mod 4) so that h=b²/8 is integer and the subtractand $\genfrac{[}{]}{0pt}{}{b}{b/2}$ has integer middle index. Only b=8,12,16 are treated; b=24 appears only as a counterexample (Proposition 2.4). No hidden assumption — the divisibility is explicit in the definition. **CLEAN.** | RESOLVED |

---

## 2. Incorrect symbolic identities — independent evaluation of 3 branch identities

I evaluated three of the 30 identities $G_r(t) \equiv G_{r-15}(t)$ at t=0,1,2 against exact DP values of g₆, using the verification script's own `Gsym` construction (exact rational arithmetic, no floats).

| Pair | t | l = 60t+r | G_r(t) (branch) | l−15 | G_{r-15} (branch) | DP g₆(l) | DP g₆(l−15) | Match? |
|------|---|-----------|-----------------|------|-------------------|----------|-------------|--------|
| r=27 vs 12 | 0 | 27 | 8 | 12 | 8 | 8 | 8 | ✓ |
| | 1 | 87 | 395 | 72 | 395 | 395 | 395 | ✓ |
| | 2 | 147 | 2027 | 132 | 2027 | 2027 | 2027 | ✓ |
| r=17 vs 2 | 0 | 17 | 1 | 2 | 1 | 1 | 1 | ✓ |
| | 1 | 77 | 268 | 62 | 268 | 268 | 268 | ✓ |
| | 2 | 137 | 1630 | 122 | 1630 | 1630 | 1630 | ✓ |
| r=7 (wrapped) vs 52 at t−1 | 1 | 67 | 172 | 52 (t=0) | 172 | 172 | 172 | ✓ |
| | 2 | 127 | 1289 | 112 (t=1) | 1289 | 1289 | 1289 | ✓ |
| | 3 | 187 | 4251 | 172 (t=2) | 4251 | 4251 | 4251 | ✓ |

**All three test pairs (including the wrapped class) agree exactly at t=0,1,2 with independent DP.** The symbolic identities in `verify_shift.py` S3 are correct.

**Objection:** None found. The 30/30 branch identities are symbolically verified by `sp.simplify(Gsym(r) - Gsym(r-15)) == 0` and match DP values at all tested points.  
**Resolution:** RESOLVED — no incorrect identities detected.

---

## 3. Invalid positivity arguments — cubic minimum lemma (Lemma 14 / `nonneg`)

### 3.1 Lemma statement vs code

**Lemma 14 (paper):** For $C(t)\in\mathbb Z[t]$, deg≤3, positive leading coefficient (or nonnegative slope if deg≤1), $C(t)\ge0$ for all integers $t\ge T_0$ iff $C\ge0$ at the candidate set
$$\{T_0\} \cup \{\lfloor\rho\rfloor,\lceil\rho\rceil : \rho \text{ real root of } C',\ \rho>T_0\} \cap \{t\in\mathbb Z: t\ge T_0\}.$$

**Code (`verify_central.py` and `verify_clearance.py`):**
```python
cands = {T0}
d1 = sp.Poly(sp.diff(Dj, t), t)
if d1.degree() >= 1:
    for root in sp.real_roots(d1):
        if root.is_real and root >= T0:   # exact SymPy comparison, NO float
            f = int(sp.floor(root)); c = int(sp.ceiling(root))
            for x in (f, f + 1, c):
                if x >= T0: cands.add(x)
return all(Dj.subs(t, x) >= 0 for x in cands)
```

**Discrepancy:** The lemma says $\lfloor\rho\rfloor,\lceil\rho\rceil$; the code checks `f, f+1, c` where `f=floor`, `c=ceil`. When $\rho$ is not an integer, `f+1 == c`, so the set is $\{\lfloor\rho\rfloor,\lceil\rho\rceil\}$. When $\rho$ is an integer, `f=c=\rho`, and the code adds $\rho$ and $\rho+1$ (one extra point). This is **conservative** (more checks, never fewer) and therefore sound.

**Exact-comparison gate:** The condition `root >= T0` uses SymPy's `CRootOf` / algebraic number comparison, which is exact (root isolation intervals), not floating-point. The repair log (Repair 7) confirms the old `float(root) >= T0` was replaced. I verified by reading the current source — no `float(` appears in either certificate script.

### 3.2 Attempt to construct a breaking cubic

I tried to construct a cubic $C(t)$ with positive leading coefficient, $C(T_0)\ge0$, $C(\lfloor\rho\rfloor)\ge0$, $C(\lceil\rho\rceil)\ge0$ for all real roots $\rho>T_0$ of $C'$, but $C(t)<0$ at some other integer $t\ge T_0$.

**Result:** Impossible by the lemma's proof (which is correct). Between consecutive real roots of $C'$, $C$ is monotone on reals, hence on integers the minimum in each interval is at an endpoint. The endpoints are exactly $T_0$ or the integers adjacent to a root $\rho>T_0$. The code's candidate set covers these endpoints (plus the conservative $\rho+1$ when $\rho\in\mathbb Z$). No counterexample exists.

**Objection:** The lemma and its implementation are **sound**. The only minor issue is the lemma states $\lfloor\rho\rfloor,\lceil\rho\rceil$ while the code checks $f, f+1, c$ — but this only adds checks, never removes them.

**Resolution:** RESOLVED — no invalid positivity argument. The cubic test is correct and exactly implemented.

---

## 4. Finite-to-infinite transitions

| Transition | Claim | Verification |
|------------|-------|--------------|
| **Q₆ recurrence** | Depth 20 (from $\prod_{i=2}^6(1-q^i)$), base n=0..119, induction for all n≥0. | `verify_shift.py` S1: 60/60 recurrence classes symbolic PASS; base 0..119 PASS. For n≥120, n−d ≥ 100 ≥ 0 for all d≤20. Induction valid. **CLEAN.** |
| **Shift Law domain** | Theorem 1: odd l≥17. Core: l≥27 (both sides ≥12, identity (*) valid). Bases: l=17,19,21,23,25 by DP. | `verify_shift.py` S3 proves branch identities for all t (l≥27). S4 checks 5 bases. l=15 excluded (degenerate). **CLEAN.** |
| **Wrapped classes** | r<15 → comparison class r+45 at t−1. Requires t≥1 (l≥67). | Verified r=7 at t=1,2,3 matches r=52 at t=0,1,2 exactly. l=7,67,... not in domain (l≥17 for theorem, l≥27 for branch form). **CLEAN.** |
| **Equivalence tail** | t≥2 (l≥120) per class; core l≤121. Overlap at 120,121. | `verify_central.py` uses T0=2. `verify_core.py` loops l=start..121. Seam closed, overlap redundant. **CLEAN.** |
| **Even-class clearance** | Base: even l up to 120. Tail: t≥2 (l≥122), 30 even residues × 3 thresholds = 90 certs. | `verify_clearance.py` (A) base PASS for all three; (B) 90/90 tail PASS. **CLEAN.** |

**Objection:** None. All finite-to-infinite transitions are correctly closed with explicit overlap or base coverage.  
**Resolution:** RESOLVED.

---

## 5. Certificate completeness / reproducibility

I ran all four core verification scripts and the corruption suite:

| Script | Result | Notes |
|--------|--------|-------|
| `verify_core.py` | PASS (0 mismatches) | 119+116+111 = 336 values checked; equivalence unimodal ⇔ g₆≥Δ_b |
| `verify_clearance.py` | PASS (90/90 tail + bases) | maxdeg=3 reported in `verify_central.py` output |
| `counterexample_6_24.py` | CONFIRMED | l=46: g₆−Δ=0, margin −86; l=48: g₆−Δ=14, margin −11 |
| `g6_table.py` | PASS | Table 1 values match; zero classification l=1,3,5,7,9,11,13 |
| `corrupt_test.sh` | PASS (4/4 mutants detected) | Perturbed base, shift, sign flip, threshold — all caught |

**Structure confirmed:** `verify_central.py` output explicitly reports:
- (6,8): 480/480 PASS, h=8, Δ=1, maxdeg=3
- (6,12): 1080/1080 PASS, h=18, Δ=3, maxdeg=3
- (6,16): 1920/1920 PASS, h=32, Δ=7, maxdeg=3

**Total tail obligations:** 480+1080+1920 = 3480, matching the paper's claim.

**Objection:** None. All certificates run, pass, and detect deliberate corruption.  
**Resolution:** RESOLVED — INDEPENDENT_REPRODUCTION: PARTIAL (tail certificates not independently re-derived in `independent_check.py`, but all supplied scripts reproduce exactly).

---

## 6. Classification and sharpness

### 6.1 Thresholds and exceptional sets

From `g6_table.py` and `verify_core.py`:
- b=8 (Δ=1): g₆(l)<1 for odd l≤13 (all zeros); g₆(15)=1≥1. Exceptional set {3,5,7,9,11,13}. Threshold l₀=14. ✓
- b=12 (Δ=3): g₆(l)<3 for odd l≤19 (g₆(17)=1, g₆(19)=2); g₆(21)=3≥3. Exceptional set {7,9,11,13,15,17,19}. Threshold l₀=20. ✓
- b=16 (Δ=7): g₆(l)<7 for odd l≤25 (g₆(23)=4, g₆(25)=6); g₆(27)=8≥7. Exceptional set {11,13,15,17,19,21,23,25}. Threshold l₀=26. ✓

### 6.2 Sharpness argument (repaired)

Paper Theorem 3 proof: l₀ = l₀ₑ + 14, where l₀ₑ = min even l with g₆(l) ≥ Δ_b.
- b=8: l₀ₑ=0 (g₆(0)=1≥1). l₀=14. Last exception l=13 = l₀ₑ+13. Direct check g₆(13)=0<1. **CLEAN.**
- b=12: l₀ₑ=6 (g₆(6)=3≥3). l₀=20. Last exception l=19 = l₀ₑ+13. Translate: l−15=4 = l₀ₑ−2 (EVEN). g₆(4)=2<3 by clearance. **CLEAN.**
- b=16: l₀ₑ=12 (g₆(12)=8≥7). l₀=26. Last exception l=25 = l₀ₑ+13. Translate: l−15=10 = l₀ₑ−2 (EVEN). g₆(10)=6<7 by clearance. **CLEAN.**

The repair log (Repair 1) confirms the original error (claiming translate was l₀ₑ−1, odd) was fixed to l₀ₑ−2 (even) with parity skip (l₀ₑ−1 is odd, so l−15 ≥ l₀ₑ−1 forces l−15 ≥ l₀ₑ). The current manuscript text matches this corrected argument.

**Objection:** None. Thresholds and sharpness are verified against DP and the repaired proof is correct.  
**Resolution:** RESOLVED.

---

## 7. Bibliography accuracy — spot check (2 entries)

I spot-checked two entries that were corrected in Repair 2, using the Crossref API via the independent verification script's bibliography check (which reported "FATAL 0, MAJOR 0, MINOR 0"):

| Entry | Paper citation | Crossref record (verified by independent_check.py) |
|-------|----------------|-----------------------------------------------------|
| O'Hara | J. Combin. Theory Ser. A **53** (1990), 29–52. DOI 10.1016/0097-3165(90)90018-r | **Matches** — JCTA 53 (1990) 29-52 |
| Reiner–Stanton | J. Algebraic Combin. **7** (1998), 91–107. DOI 10.1023/A:1008623312887 | **Matches** — J. Algebraic Combinatorics 7 (1998) 91-107 |

(Stanley–Zanello was also verified: J. Combinatorics 11 (2020) 111-126.)

**Objection:** None. The corrected citations are accurate.  
**Resolution:** RESOLVED.

---

## 8. Self-containment

### 8.1 Undefined internal terms / mission history

The paper is self-contained mathematically. All notation (aₗ(n), g₆, F⁽⁶,ᵇ⁾ₗ, Δ_b, Q₆, M_j, G_r) is defined in §2–§6. No term requires external "mission history" to understand.

### 8.2 Reference to `proofs/MECHANISM_ATTEMPT.md`

**Paper §9 (Conjecture 9.1):** "see `proofs/MECHANISM_ATTEMPT.md` in the accompanying package for the strongest partial attempt found so far."

**Actual location:** the internal research archive `math10/proofs/MECHANISM_ATTEMPT.md` (in the predecessor archive, not initially in math10r). [Resolved: the file is now included at `proofs/MECHANISM_ATTEMPT.md` in this repository.]

**Issue:** The relative path `proofs/MECHANISM_ATTEMPT.md` is **broken for an external reader** who only has the math10r directory. The file exists in the sibling math10 archive but is not copied into math10r. The repair log (Repair 7) notes: "note that file currently lives at projects/math-research/math10/proofs/MECHANISM_ATTEMPT.md (math10r packaging will copy it; flag as MINOR if you consider the path reference broken for an external reader)."

**Assessment:** MINOR — the reference is to supplementary material, not part of the mathematical proof. The manuscript itself is complete without it. But for a submitted package, the file should be copied or the path corrected.

**Resolution:** OPEN-WITH-SCOPE — MINOR packaging issue, does not affect mathematical correctness.

---

## Summary of Objections

| # | Area | Status |
|---|------|--------|
| 1 | Hidden assumptions | RESOLVED |
| 2 | Symbolic identities | RESOLVED (3/30 spot-checked, all exact) |
| 3 | Positivity arguments | RESOLVED (lemma sound, implementation exact) |
| 4 | Finite-to-infinite | RESOLVED |
| 5 | Certificates/reproducibility | RESOLVED (all scripts PASS, corruption detected) |
| 6 | Classification/sharpness | RESOLVED |
| 7 | Bibliography | RESOLVED (2/2 spot-checked) |
| 8 | Self-containment | MINOR (MECHANISM_ATTEMPT.md path broken for external reader) |

---

## Final Verdict

**MATHEMATICS: PROVED**  
All core theorems (Shift Law, Equivalence, Classification, Counterexample) are supported by exact, reproducible certificates in exact integer/rational arithmetic. No mathematical gap remains.

**INDEPENDENT_REPRODUCTION: PARTIAL**  
The independent verification (`independent_check.py`) re-proves the Shift Law, finite core, classification, and counterexample from scratch (different DP, fresh SymPy). It does **not** independently re-derive the 3,480 tail certificates (it accepts them as documented). This meets the "PARTIAL" criterion.

**NOVELTY: APPARENTLY-NEW**  
The Shift Law for k=6, the exact central-gap equivalence on the certified domain, and the sharp exceptional-set classifications for b=8,12,16 are not found in the cited literature (Stanley–Zanello, KUW, Reiner–Stanton, KKM). The paper claims no more than "not found in the sources cited" — this is accurate.

**PUBLICATION_READINESS: READY-FOR-HUMAN-REVIEW**  
The manuscript compiles cleanly (14 pp, tectonic 0.15.0), all references resolve, all certificates pass, corruption tests detect mutants. The only packaging issue is the broken `MECHANISM_ATTEMPT.md` path (MINOR). The mathematics is complete and certified.

**VERDICT: APPROVED**  
With the single MINOR packaging fix (copy `MECHANISM_ATTEMPT.md` into math10r/proofs/ or correct the path), this work is approved for human review.

---

**Referee signature (automated):**  
Hostile subagent 36d4dc94-ac5c-4ae8-a56a-3dec36220061  
2026-11-13 19:33 CST

MATHEMATICS: PROVED
INDEPENDENT_REPRODUCTION: PARTIAL
NOVELTY: APPARENTLY-NEW
PUBLICATION_READINESS: READY-FOR-HUMAN-REVIEW
VERDICT: APPROVED
---

## Editor's note (parent mission, 19:45 CST — appended after referee settled)

1. **INDEPENDENT_REPRODUCTION timing.** The referee's PARTIAL reflects the state at writing.
   The Phase II verifier subsequently completed the tail re-certification independently:
   `verification_independent/tail_recert.py` re-derives all **3,480/3,480** tail obligations
   from its own product-form DP branch interpolants with exact derivative-root minimum testing
   (maxdeg 3, global minimum margin 2126 at (b,r,j,t)=(8,0,6,2)); INDEPENDENT_VERIFICATION.md
   final status is now `INDEPENDENT_REPRODUCTION: PASS`. Mission-level reproducibility: PASS.
2. **MINOR item 8.2 fixed.** `proofs/MECHANISM_ATTEMPT.md` now exists inside math10r (copied
   19:33 CST; the referee's read predates or races the copy) and the zip package includes it,
   so the paper's path reference resolves for an external reader.
The referee's APPROVED verdict stands with zero open proof obligations.
