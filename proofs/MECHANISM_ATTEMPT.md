# A representation-theoretic attempt at the constant 15

## Question and outcome

For
\[
 P_l(q)=\begin{bmatrix}l+6\\6\end{bmatrix}_q,\qquad
 g_6(l)=[q^{3l}](1-q)P_l(q),
\]
the proved Shift Law is
\[
 g_6(l)=g_6(l-15)\qquad(l\ \text{odd},\ l\ge17).
\]
This note attempts to explain the shift by a graded-representation identity rather than by
enumerating residues modulo a quasipolynomial period.  The attempt gives a natural virtual
representation in which the number 15 has a precise structural role, but it does **not**
produce a bijection or a proved graded-character identity.  Thus this is an honest failure,
not a new proof.

## 1. A useful cancellation

The reciprocal-product form of the Gaussian polynomial is
\[
 P_l(q)=\prod_{i=1}^{6}\frac{1-q^{l+i}}{1-q^i}.
\]
Consequently
\[
 (1-q)P_l(q)
 =\frac{\prod_{i=1}^{6}(1-q^{l+i})}{\prod_{i=2}^{6}(1-q^i)}.                 \tag{1}
\]
This identity is exact as an identity of formal power series.  In particular,
\[
 g_6(l)=[q^{3l}]
 \frac{\prod_{i=1}^{6}(1-q^{l+i})}{\prod_{i=2}^{6}(1-q^i)}.                 \tag{2}
\]
As a small exact sanity check, direct integer coefficient extraction verifies (2) for every
\(0\le l\le60\).  No assertion below depends on numerical extrapolation.

## 2. Virtual-representation interpretation

Let \(M\) be the graded vector space with one basis vector of weight \(j\) for each
\(j\in\{2,3,4,5,6\}\), and let \(N_l\) be the graded vector space with one basis vector of
weight \(l+i\) for each \(1\le i\le6\).  Define
\[
 \mathcal V_l=\operatorname{Sym}(M)\otimes\bigwedge N_l.
\]
Because the exterior algebra is virtual, its graded character is
\[
 \sum_{n\ge0}\dim(\mathcal V_l)_nq^n
 =\prod_{i=1}^{6}(1-q^{l+i})\prod_{j=2}^{6}(1-q^j)^{-1}.
\]
Equation (2) says precisely that
\[
 g_6(l)=\dim(\mathcal V_l)_{3l}.                                        \tag{3}
\]
Thus the Shift Law is equivalent to the assertion that the central weight spaces of the two
virtual graded spaces satisfy
\[
 \dim(\mathcal V_l)_{3l}=\dim(\mathcal V_{l-15})_{3(l-15)}.               \tag{4}
\]

This is a genuine representation-theoretic reformulation.  It also locates the difficulty
precisely.  Every exterior generator has weight \(l+i\), so replacing \(l\) by \(l-15\)
lowers every generator weight by 15.  At the same time the central weight changes by
\[
 3l-3(l-15)=45=3\cdot15.                                                \tag{5}
\]
Equation (5) explains why 15 is the natural *primitive* shift in this representation: a
transport of the central weight by 45 changes the exterior degree by three, if the symmetric
part is kept fixed.

## 3. The attempted promotion, and its obstruction

Write \(\mathcal V_l^{(r)}\) for the exterior-degree-\(r\) part.  Its graded character is
\[
 \sum_{n\ge0}\dim(\mathcal V_l^{(r)})_nq^n
 =e_{r}(q^{l+1},\ldots,q^{l+6})\prod_{j=2}^{6}(1-q^j)^{-1},                \tag{6}
\]
where \(e_r\) is the \(r\)-th elementary symmetric polynomial.

A natural attempted comparison is therefore between the degree-zero part at \(l\) and the
degree-three part at \(l-15\): multiplying each of the three exterior generator weights by
15 accounts for the 45-unit central-weight displacement in (5).  Unfortunately, this
comparison is not even support-compatible at the central weights.

Indeed, a degree-three monomial in \(\mathcal V_{l-15}^{(3)}\) has weight
\[
 (l-15)+(l-14)+(l-13)+i+j+k
 =3l-45+i+j+k,
\]
where \(1\le i<j<k\le6\).  Its weight is therefore at least
\[
 3l-45+(1+2+3)=3l-39>3(l-15)=3l-45.                                    \tag{7}
\]
Every degree-three monomial lies strictly above the central weight of
\(\mathcal V_{l-15}\), and multiplication by the symmetric factor can only increase weight.
Hence
\[
 (\mathcal V_{l-15}^{(3)})_{3(l-15)}=0.                                  \tag{8}
\]
Symmetrically, the degree-three part is empty at the central weight of \(\mathcal V_l\),
because its lowest weight is \(3l+6>3l\).  At both central weights the only exterior degrees
that can occur are 0, 1, and 2 (with the degree-2 term absent in a few small cases).

Thus the expected degree-three “promotion” is blocked by the exterior-degree boundary.  This
is the same sort of boundary obstruction that defeats direct Ferrers and rim-hook transports,
but it is visible at the level of graded characters rather than at the level of partitions.
It also shows why the result cannot come from a naive equality of the complete graded
characters: those characters are not equal, and (4) is only an equality of two individual
weight spaces.

## 4. The exact unproved lemma that would finish the attempt

The representation approach would prove the mechanism if the following statement could be
established:

> **Required weight-space lemma.**  For odd \(l\ge17\), there is a weight-preserving (after
> the displayed \(45\)-unit transport) bijection, or an equality of alternating character
> sums,
> \[
> (\mathcal V_l)_{3l}\cong(\mathcal V_{l-15})_{3l-45},
> \]
> constructed compatibly with the exterior product and the symmetric product.

In terms of the elementary-symmetric characters, this would require a sign- or
degree-preserving identity at the two single weights, not an equality of whole characters.
No such bijection or identity has been proved here.  The most direct degree-three attempt
is impossible by (8), so the lemma would require a substantially subtler
sign-reversing-involution or promotion argument, possibly mixing degrees 0, 1, and 2.

For completeness, the elementary-symmetric expansion of the weight-space difference is
\[
 [q^{3l}]\mathcal V_l-[q^{3(l-15)}]\mathcal V_{l-15}
 =
 Q_6(3l)-\sum_{i=1}^{6}Q_6(2l-i)+\sum_{1\le i<j\le6}Q_6(l-i-j)
 -
 \left(
 Q_6(3l-45)-\sum_{i=1}^{6}Q_6(2l-30-i)
 +\sum_{1\le i<j\le6}Q_6(l-15-i-j)
 \right),
\]
where \(Q_6\) is the denumerant with parts \(2,\ldots,6\), with the usual zero convention
for negative arguments.  The Shift Law says this whole expression is zero for odd \(l\ge17\).
The present attempt reorganizes this expression by exterior degree but does not cancel it
without the already-known quasipolynomial analysis.

## 5. What has and has not been achieved

* The constant 15 has a structural interpretation in the virtual representation
  \(\mathcal V_l\): it is the common decrement of the six exterior-generator weights, while
  the central target moves by three such decrements.
* The attempted degree-three promotion fails for a precise reason: exterior degree three is
  strictly above the relevant central weight.
* A required weight-space lemma is stated, but it is **unproved**.  Under the success
  criterion for this phase, that is a failure of the present attempt.
* The already-proved Shift Law remains valid; nothing here changes its proof.  This note does
  not claim a period-15 symmetry or a bijection.

Therefore no complete conceptual mechanism has been obtained.  The representation-theoretic
route leaves a sharp, concrete target: a degree-compatible transport between the central
weight spaces of \(\mathcal V_l\) and \(\mathcal V_{l-15}\), beyond the blocked degree-three
promotion.

STATUS: MECHANISM-OPEN
