# MATH-10R — REPAIR_LOG (Phase I, 19:12–19:30 CST)

## Authoritative sources
- Manuscript base: `projects/math-research/math10/manuscript/paper.tex` (frozen archive copy;
  math10 directory NOT modified — verified by absence of writes).
- `gauss (1).pdf`: **not found on the working host** (searched the usual download locations and
  home tree). The mission's repair list is internally consistent with
  the MATH-10 paper (Theorem 3 sharpness p.10, O'Hara/RS entries), so the math10 archive was
  used as the authoritative manuscript and the repair list as owner review comments. If
  gauss (1).pdf differs from the delivered paper.pdf, resend and diff.

## Repair 1 — Theorem 3 sharpness argument (the l0e−1 → l0e−2 error)
Original claimed the translate of `l0−1` is `l0e−1` and odd. Correct: `l0−1 = l0e+13`,
translate `= l0−1−15 = l0e−2`, which is EVEN. Rewrote the sharpness paragraph:
- b=12: l0e=6 → translate 4: g6(4)=2<3 ✓ (exact DP re-run)
- b=16: l0e=12 → translate 10: g6(10)=6<7 ✓
- b=8: l0e=0 degenerate (l0e−2<0): handled directly, l0−1=13, g6(13)=0<1 ✓
Also made the theorem statement explicit ("largest even parameter l0e−2 … whenever l0e≥2;
for b=8 verified directly") and spelled out the parity-skip step (even l−15 ≥ l0e−1 forces
l−15 ≥ l0e since l0e−1 is odd).

## Repair 2 — References verified against primary records (Crossref API, 19:14–19:20 CST)
| entry | was | now (verified) |
|---|---|---|
| O'Hara | JCTA 57 (1991) 67–80 | **JCTA A 53 (1990) 29–52, DOI 10.1016/0097-3165(90)90018-r** |
| Reiner–Stanton | J. Algebra 201 (1998) 154–170 | **J. Algebraic Combin. 7 (1998) 91–107, DOI 10.1023/A:1008623312887** |
| Stanley–Zanello | arXiv + "journal 2020" | **J. Combinatorics 11 (2020) 111–126**, DOI 10.4310/joc.2020.v11.n1.a5 |
| KUW | arXiv only | **ISSAC 2023, DOI 10.1145/3597066.3597113** + arXiv (theorem numbers from arXiv version, stated) |
| Chen–Jia | arXiv only | **Internat. J. Math. 32 (2021) 2140003**, DOI 10.1142/S0129167X21400036 |
| Dhand | arXiv only | **Discrete Math. 335 (2014) 20–24** |
| Sylvester | wrong title ("Note on the integral partitions…") | **"Proof of the hitherto undemonstrated fundamental theorem of invariants", Philos. Mag. (5) 5 (1878) 178–188; Coll. Papers 3, 117–126** — title corrected to the citation form used in SZ [11] and KUW [34] (archived primary PDFs) |
| Pak–Panova | already correct | C.R. Math. 351 (2013) 415–418 confirmed |
Books (Stanley EC2, Andrews) unchanged, standard citations.

## Repair 3 — Parity statements scoped
- Intro bullet: general slow-class pattern now labeled "observed, not proved, for k>6".
- §9.2: parity law relabeled "observed and conjectural for k>6; only the k=6 instance is used
  (and proved) in this paper".
- Classification remark: "conjectured phenomenon"; 26-family picture = exact-computation
  evidence only. The proved k=6 statements (odd zeros 1..13, Shift Law transport odd→even)
  are untouched.

## Repair 4 — Novelty language
Already qualified ("not found in the sources cited", "no stronger novelty claim"); verified
no priority assertions were introduced; abstract unchanged in this respect (one honesty fix:
"we prove naive transports cannot supply" → "we document precisely why the standard transports
do not supply").

## Repair 5 — Notation audit
Definitions (a_l(n), g_6, F^(6,b), Δ_b at center h=b²/8), admissibility (3l≥h; core starts
l≥3,6,11), residue indexing (r mod 60, wrapped classes r<15 via floor carry), threshold
formula (l0=l0e+14 with g6(0)=1 convention) — all re-checked against the certificates; the
intro's "grows like l²" was WRONG (branch polynomials are cubic in t, growth ~l³) and was
replaced by "grows without bound … degree-3 branch polynomials".

## Repair 6 — Typesetting
Recompiled with tectonic 0.15.0: no undefined references/citations; fixed 4 overfull-box
sites (E(6,b) display split, long \texttt break allowance, base-case display split, evidence
table set \small). 14 pp.

## Repair 7 (Phase II prerequisite) — exact critical-point gate
`verify_central.py` / `verify_clearance.py` in math10r used `float(root) >= T0` to select
derivative-root candidates (values were always re-evaluated exactly, but the gate itself was
floating). Replaced with exact sympy comparisons (`root >= T0` on CRootOf/algebraic numbers,
exact via isolation intervals). Smoke receipt: verify_clearance.py exit 0, 90/90 PASS, 1.1s.
math10 archive copies frozen with the old (harmless-but-implicit) gate; math10r is canonical.

## Files
Changed: math10r/manuscript/paper.tex (+ compiled paper.pdf), math10r/verification/
{verify_central.py, verify_clearance.py}.
Untouched: math06–math10 archives, harness, everything else.
