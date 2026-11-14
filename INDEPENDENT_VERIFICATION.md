# MATH-10R independent verification

I wrote and ran `verification_independent/independent_check.py`, using a product-form bounded-partition DP and fresh SymPy construction. It does not import or call the supplied certificates.

## Results

| Item | Independent result | Manuscript result | Grade |
|---|---|---|---|
| Shift law | Q6 recurrence/base/star identity PASS; all 30 odd residue branch identities PASS; bases 17,19,21,23,25 PASS | Theorem 1 | — |
| Equivalence core | Exact full coefficient DP, l through 121: b=8,12,16 all PASS | 3,480 tail obligations plus core | — |
| Classification | Exceptional sets exactly `{3,5,7,9,11,13}`, `{7,9,...,19}`, `{11,13,...,25}`; thresholds 14,20,26 | Theorem 3 | — |
| Sharpness | g6(4)=2, g6(10)=6, g6(13)=0; even translate is l0e-2 and parity skip works | repaired manuscript | — |
| Proposition 4 | (46,66): (165876,165790), margin -86; (48,70): (215262,215251), margin -11 | same values | — |
| Zero case | g6(6)=3 and the b=12,l=6 subtraction is zero/unimodal | same | — |

Commands and observed output:

```
python3 projects/math-research/math10r/verification_independent/independent_check.py
SHIFT Q6 recurrence/base/star/30 branch identities PASS
CORE 8 PASS exceptions [3, 5, 7, 9, 11, 13]
CORE 12 PASS exceptions [7, 9, 11, 13, 15, 17, 19]
CORE 16 PASS exceptions [11, 13, 15, 17, 19, 21, 23, 25]
PROP 46 66 (165876, 165790)
PROP 48 70 (215262, 215251)
```

The Q6 route derives the recurrence from `(1-x^2)...(1-x^6)`, interpolates six exact values per residue, checks 120 bases and all 60 recurrence classes, then checks the inclusion-exclusion identity for l=12..80. The branch comparison uses explicit floor carries and exact symbolic subtraction. This independently establishes the shift mechanism, but does not itself reproduce the manuscript's 3,480 tail certificates: the supplied tail scripts were read-only and not treated as independent evidence. Thus tail coverage is accepted as documented, not independently re-certified here. The admissibility starts computed are 3, 6, 11, and all tested cases use s>=0.

The 3,480 structure (480+1080+1920) and Lemma 14 procedure were inspected. The independent stress list includes negative-leading cubic, negative-slope linear, constant negative, quadratic with double derivative root, derivative root at T0, and an irrational CRootOf. Comparisons are exact SymPy comparisons; no `float(` occurs in the independent script. SymPy's `CRootOf >= Integer` comparison is exact (root isolation), not floating-point.

## Tail re-certification (independent follow-up)

I constructed and ran `verification_independent/tail_recert.py`, independently using the product-form bounded-partition DP (unrestricted parts followed by the six box factors). For each `b` in `{8,12,16}`, every residue `r=0,...,59`, and every `j=-1,...,h-2`, it computed seven exact DP values at `l=r+60t`, `t=2,...,8`. Six values were interpolated as the branch `M_{j,r}(t)` and the seventh was an independent interpolation check. The resulting `C_{j,r}=M_{j,r}-M_{h-1,r}` polynomials were tested for all integer `t>=2` by exact integer evaluation at `t=2` and at every integer adjacent to every isolated real root of the exact derivative (rational isolating intervals); no floating-point arithmetic was used.

Command and output:

```
python3 projects/math-research/math10r/verification_independent/tail_recert.py
TAIL_RECERT PASS 3480 certificates max_degree 3 minimum (2126, 8, 0, 6, 2)
```

Coverage is complete: `3 * 60 * (h-1) = 480 + 1080 + 1920 = 3480` certificates. Observed maximum degree was 3 (within the product-form degree bound <=5). The reported minimum is the exact value 2126, attained at `(b,r,j,t)=(8,0,6,2)`.

Bibliography spot checks through `api.crossref.org` returned exact matches: O'Hara, JCTA 53 (1990), 29-52; Reiner--Stanton, J. Algebraic Combinatorics 7 (1998), 91-107; Stanley--Zanello, J. Combinatorics 11 (2020), 111-126. No discrepancy: FATAL 0, MAJOR 0, MINOR 0.

Parity claims in Sections 1, 8, 9, and 11 are correctly scoped as observed/conjectural for k>6; degree is stated a-priori <=4 and observed <=3. The l<=121 plus t>=2 seam is documented, with no identified gap. Proposition 4 confirms M_{h-1}=0 for l=46 and 14 for l=48.

MATHEMATICS: PROVED
INDEPENDENT_REPRODUCTION: PASS
