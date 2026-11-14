#!/usr/bin/env python3
"""MATH-09 canonical certificate: SHIFT LAW k=6.
Theorem: for every odd integer l >= 17, g_6(l) = g_6(l-15), where
g_6(l) = a_l(3l) - a_l(3l-1), a_l(n) = # partitions of n into at most 6 parts, each <= l.

Proof structure (all machine-checked here):
  S1. Q6(n) = p_{parts in {2,3,4,5,6}}(n) equals its period-60, degree<=4 branch
      polynomial F_{n mod 60}(n//60) for ALL n >= 0:
      - constant-coefficient recurrence from prod_{i=2}^6 (1-q^i), depth 20;
      - F satisfies it symbolically per class (60/60);
      - F == Q6 on base n = 0..119; induction on n.
  S2. Inclusion-exclusion survival: for l >= 12, subsets of size >= 3 have negative
      arguments (always) and pairs are nonnegative, giving
      g_6(l) = Q6(3l) - sum_i Q6(2l-i) + sum_{i<j} Q6(l-i-j)  (identity *).
      Audited against an independent DP for l = 12..80.
  S3. For each odd residue r mod 60 the branch polynomial of the RHS expression at
      l equals that at l-15 IDENTICALLY in t (30/30 symbolic checks). This proves (*)
      branch equality g_6(l) = g_6(l-15) for all odd l >= 27 (both sides >= 12).
  S4. Base cases l in {17,19,21,23,25} by exact DP (RHS below survival threshold).
"""
import sympy as sp
from itertools import combinations

def dp_g(l):
    c = 3*l
    A = [0]*(c+1); A[0] = 1
    for i in range(1, 7):
        B = [0]*(c+1)
        for n in range(c+1):
            if A[n] == 0: continue
            m = n
            while m <= c:
                B[m] += A[n]; m += i
        A = [B[n] - (B[n-l-i] if n-l-i >= 0 else 0) for n in range(c+1)]
    return A[c] - A[c-1]

def main():
    t = sp.symbols('t', integer=True)
    N = 300
    Q6 = [0]*(N+1); Q6[0] = 1
    for part in (2, 3, 4, 5, 6):
        for n in range(part, N+1):
            Q6[n] += Q6[n-part]
    D = {0: 1}
    for i in (2, 3, 4, 5, 6):
        D2 = {}
        for d, c in D.items():
            D2[d] = D2.get(d, 0) + c; D2[d+i] = D2.get(d+i, 0) - c
        D = D2
    qp = {r: sp.interpolate([(tt, Q6[r+60*tt]) for tt in range(5)], t) for r in range(60)}
    # S1
    for r in range(60):
        s = qp[r]
        for d, c in D.items():
            if d: s += c * qp[(r-d) % 60].subs(t, t + (r-d) // 60)
        assert sp.simplify(s) == 0, f"S1 recurrence class {r}"
    assert all(qp[n % 60].subs(t, n // 60) == Q6[n] for n in range(120)), "S1 base"
    print("S1 Q6 period-60 quasipolynomial (recurrence + base, all n>=0): PASS")
    # S2
    def Qx(n): return 0 if n < 0 else int(qp[n % 60].subs(t, n // 60))
    def star(l):
        s = Qx(3*l)
        for i in range(1, 7): s -= Qx(2*l-i)
        for i, j in combinations(range(1, 7), 2): s += Qx(l-i-j)
        return s
    assert all(star(l) == dp_g(l) for l in range(12, 81)), "S2 identity audit"
    print("S2 identity (*) vs independent DP, l=12..80: PASS")
    # S3
    def Gsym(r):
        def term(coef, off):
            val = coef*r + off
            return qp[val % 60].subs(t, coef*t + val // 60)
        s = term(3, 0)
        for i in range(1, 7): s -= term(2, -i)
        for i, j in combinations(range(1, 7), 2): s += term(1, -i-j)
        return sp.expand(s)
    for r in range(1, 60, 2):
        assert sp.simplify(Gsym(r) - Gsym(r-15)) == 0, f"S3 class {r}"
    print("S3 branch identity g(l) = g(l-15), 30/30 odd classes symbolic: PASS")
    # S4
    for l in (17, 19, 21, 23, 25):
        assert dp_g(l) == dp_g(l-15), f"S4 base {l}"
    print("S4 base cases l=17..25: PASS")
    print("SHIFT LAW k=6 PROVED: g_6(l) = g_6(l-15) for all odd l >= 17.")

if __name__ == "__main__":
    main()
