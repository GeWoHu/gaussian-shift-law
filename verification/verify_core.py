#!/usr/bin/env python3
"""MATH-10: finite-core equivalence, exact DP (paper Sec. 7.3).

For each family (6,b), b in {8,12,16}, and every admissible l <= 120:
    F_l = [l+6 choose 6]_q - q^{3l-h} [b choose b/2]_q  is unimodal
    if and only if  g6(l) >= Delta_b.
Pure exact integer arithmetic; no reduction assumptions (full coefficient list).
Exit 0 iff zero mismatches.
"""
import sys

def gauss(n, k):
    """coefficients of [n choose k]_q via q-Pascal recurrence (exact ints)"""
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

TH = {8: 1, 12: 3, 16: 7}
for b, D in TH.items():
    h = b*b//8
    B = gauss(b, b//2)
    assert B[h] - B[h-1] == D, f"Delta_{b} mismatch"
    start = (h + 2)//3  # 3l >= h
    mism = 0
    for l in range(start, 122):  # extended through 121 to close the core/tail seam
        s = 3*l - h
        A = gauss(l+6, 6)
        F = [A[n] - (B[n-s] if 0 <= n-s <= 2*h else 0) for n in range(6*l+1)]
        g = A[3*l] - A[3*l-1]
        if is_unimodal(F) != (g >= D):
            mism += 1
            print("MISMATCH", b, l, g)
    print(f"(6,{b}) finite core l={start}..121: equivalence unimodal <=> g6(l)>={D}: "
          f"{'PASS' if mism==0 else 'FAIL'} ({122-start} values, {mism} mismatches)")
    assert mism == 0
print("FINITE CORE: PROVED (exact coefficient-level verification, l <= 121)")
