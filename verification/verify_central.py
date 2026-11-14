#!/usr/bin/env python3
"""MATH-09 Phase III (sound version): central-dominance equivalence certificates
for (k,b) in {(6,8),(6,12),(6,16)} with a SOUND cubic-capable nonnegativity test.

Fix vs phase3_central_6_12_16.py: observed tail difference polynomials D_{j,r}(t)
have degree 3 (not <= 2). The old test (value>=0 & slope>=0 & lead>=0 at t=2) is
NOT sufficient for cubics. New test: for positive-leading D of degree <= 3, the
minimum over integers t >= T0 is attained at T0 or at an integer near a positive
real root of D' >= T0; verify D >= 0 exactly at those finitely many candidates.
Degree <= 2 with positive lead is covered (derivative root check degenerates).

Run: python3 phase3_central_sound.py  (expect ~6-7 min)
"""
import sympy as sp
from itertools import combinations

def gauss_full(n, m):
    deg = m * (n - m)
    C = [0] * (deg + 1); C[0] = 1
    for i in range(1, m + 1):
        T = [0] * (deg + 1)
        for k in range(deg + 1):
            if C[k] == 0: continue
            j = k
            while j <= deg:
                T[j] += C[k]; j += i
        s = n - m + i
        C = [T[k] - (T[k - s] if k - s >= 0 else 0) for k in range(deg + 1)]
    return C

t = sp.symbols('t', integer=True, nonnegative=True)
N = 360
P = [0] * (N + 1); P[0] = 1
for part in (1, 2, 3, 4, 5, 6):
    for n in range(part, N + 1): P[n] += P[n - part]
D = {0: 1}
for i in (1, 2, 3, 4, 5, 6):
    D2 = {}
    for d, c in D.items():
        D2[d] = D2.get(d, 0) + c; D2[d + i] = D2.get(d + i, 0) - c
    D = D2
pp = {r: sp.interpolate([(tt, P[r + 60 * tt]) for tt in range(6)], t) for r in range(60)}
T0 = 2

def nonneg(Dj):
    """D(t) >= 0 for all integers t >= T0, D polynomial in t, degree <= 3."""
    p = sp.Poly(Dj, t); deg = p.degree()
    if deg < 0: return True
    if deg == 0: return p.LC() >= 0
    lc = p.LC()
    if deg >= 1 and lc < 0: return False  # unbounded below (catches 3-t)
    cands = {T0}
    d1 = sp.Poly(sp.diff(Dj, t), t)
    if d1.degree() >= 1:
        for root in sp.real_roots(d1):
            if root.is_real and root >= T0:
                f = int(sp.floor(root)); c = int(sp.ceiling(root))
                for x in (f, f + 1, c):
                    if x >= T0: cands.add(x)
    return all(Dj.subs(t, x) >= 0 for x in cands)

for b in (8, 12, 16):
    h = b * b // 8
    Bc = gauss_full(b, b // 2)
    assert sum(Bc) == int(sp.binomial(b, b // 2)) and Bc == Bc[::-1]
    Delta = Bc[h] - Bc[h - 1]
    half = b * b // 4
    dB = {j: (Bc[j + 1] if j + 1 <= half else 0) - (Bc[j] if 0 <= j <= half else 0)
          for j in range(-1, h)}
    def branch(coef, off, r):
        val = coef * r + off
        return pp[val % 60].subs(t, coef * t + val // 60)
    def Mexpr(r, j):
        def aexpr(off):
            s = branch(3, off, r)
            for i in range(1, 7): s -= branch(2, off - i, r)
            for i, jj in combinations(range(1, 7), 2): s += branch(1, off - i - jj, r)
            return s
        return sp.expand(aexpr(-h + j + 1) - aexpr(-h + j))
    fails = 0; checked = 0; maxdeg = 0
    for r in range(60):
        M7 = Mexpr(r, h - 1)
        for j in range(-1, h - 1):
            Dj = sp.expand(Mexpr(r, j) - M7 - (dB[j] - dB[h - 1]))
            maxdeg = max(maxdeg, sp.Poly(Dj, t).degree())
            checked += 1
            if not nonneg(Dj):
                fails += 1
                if fails <= 3: print("FAIL", b, r, j, Dj)
    print(f"(6,{b}) MINIMUM-BASED tail certificates: {checked - fails}/{checked} "
          f"PASS (h={h}, Delta={Delta}, maxdeg={maxdeg})", flush=True)
    assert fails == 0
