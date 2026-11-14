#!/usr/bin/env python3
"""MATH-10: Proposition 2.4 counterexample (6,24) at l=46 and l=48, exact integers."""
import sys

def gauss(n, k):
    C = [[1]] + [[] for _ in range(k)]
    for i in range(1, n+1):
        newC = [None]*(k+1); newC[0] = [1]
        for j in range(1, min(i, k)+1):
            a = C[j] if (j <= i-1 and C[j]) else [0]
            sh = [0]*(i-j) + C[j-1]
            L = max(len(a), len(sh))
            a = a + [0]*(L-len(a)); sh = sh + [0]*(L-len(sh))
            newC[j] = [x+y for x, y in zip(a, sh)]
        for j in range(min(i, k)+1, k+1):
            newC[j] = C[j] if C[j] else [0]
        C = newC
    return C[k]

def is_unimodal(seq):
    i = 0
    while i+1 < len(seq) and seq[i] <= seq[i+1]:
        i += 1
    return all(seq[j] >= seq[j+1] for j in range(i, len(seq)-1))

h = 72
B = gauss(24, 12)
Delta = B[h] - B[h-1]
assert Delta == 127, Delta
for l, jbad, val in [(46, 66, -86), (48, 70, -11)]:
    s = 3*l - h
    A = gauss(l+6, 6)
    g = A[3*l] - A[3*l-1]
    F = [A[n] - (B[n-s] if 0 <= n-s <= 2*h else 0) for n in range(6*l+1)]
    n0 = s + jbad   # margin M_j = D(s+j) = F[s+j+1] - F[s+j]
    d = F[n0+1] - F[n0]
    assert d == val, (l, d)
    assert not is_unimodal(F), l
    print(f"(6,24) l={l}: g6={g}, g6-Delta={g-Delta}, margin M_{jbad} = F[{n0+1}]-F[{n0}] "
          f"= {F[n0+1]}-{F[n0]} = {d}; F NOT unimodal -> central dominance fails")
print("COUNTEREXAMPLE (6,24,46)/(6,24,48): CONFIRMED (exact integers)")
