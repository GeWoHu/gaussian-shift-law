#!/usr/bin/env python3
"""MATH-10: even-class clearance certificate (paper Sec. 7.4).

Claim certified:
  g6(l) >= Delta_8=1 for every even l >= 2;
  g6(l) >= Delta_12=3 for every even l >= 6;
  g6(l) >= Delta_16=7 for every even l >= 12.
Method:
  (A) finite base: exact DP for even l up to 120 (per-threshold start);
  (B) tail l >= 122: g6(l) = G_r(t) branch polynomial (identity (*) valid l >= 12),
      30 even residue classes; sound minimum test (MATH-10 Lemma, cubic-capable)
      applied to G_r(t) - Delta_b at T0 = 2. Exact integer/rational arithmetic.
Exit 0 iff all checks pass.
"""
import sympy as sp
from itertools import combinations

t = sp.symbols('t', integer=True)
T0 = 2

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

# Q6 branch interpolants (same construction as verify_shift.py S1)
N = 300
Q6 = [0]*(N+1); Q6[0] = 1
for part in (2, 3, 4, 5, 6):
    for n in range(part, N+1):
        Q6[n] += Q6[n-part]
qp = {r: sp.interpolate([(tt, Q6[r+60*tt]) for tt in range(5)], t) for r in range(60)}

def Gsym(r):
    def term(coef, off):
        val = coef*r + off
        return qp[val % 60].subs(t, coef*t + val // 60)
    s = term(3, 0)
    for i in range(1, 7):
        s -= term(2, -i)
    for i, j in combinations(range(1, 7), 2):
        s += term(1, -i-j)
    return sp.expand(s)

def nonneg(C, T0=T0):
    """C(t) >= 0 for all integers t >= T0; degree <= 3 sound minimum test."""
    p = sp.Poly(C, t); deg = p.degree()
    if deg < 0: return True
    if deg == 0: return p.LC() >= 0
    lc = p.LC()
    if deg >= 2 and lc < 0: return False
    if deg == 1 and lc < 0: return False
    cands = {T0}
    d1 = sp.Poly(sp.diff(C, t), t)
    if d1.degree() >= 1:
        for root in sp.real_roots(d1):
            if root.is_real and root >= T0:
                f = int(sp.floor(root)); c = int(sp.ceiling(root))
                for x in (f, f+1, c):
                    if x >= T0: cands.add(x)
    return all(C.subs(t, x) >= 0 for x in cands)

TH = {8: 1, 12: 3, 16: 9}
START = {8: 2, 12: 6, 16: 12}

# (A) finite base
for b, D in TH.items():
    ok = all(dp_g(l) >= D for l in range(START[b], 121, 2))
    print(f"(A) finite base (6,{b}): even l={START[b]}..120 all g6>= {D}: {'PASS' if ok else 'FAIL'}")
    assert ok, f"finite base (6,{b})"

# (B) tail: 30 even classes x 3 thresholds = 90 certificates
for b, D in TH.items():
    fails = 0; checked = 0
    for r in range(0, 60, 2):
        C = sp.expand(Gsym(r) - D)
        checked += 1
        if not nonneg(C):
            fails += 1
            print("FAIL", b, r, C)
    print(f"(B) (6,{b}) tail clearance: {checked-fails}/{checked} even-class certificates PASS (t >= 2, l >= 122)")
    assert fails == 0, f"clearance (6,{b})"

print("CLEARANCE: g6(l) >= Delta_b on the even classes for b=8,12,16: PROVED (base+tail)")
