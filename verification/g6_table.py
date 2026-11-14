#!/usr/bin/env python3
"""MATH-10: exact g6 table (paper Table 1) and zero classification (finite)."""
def dp_a(l, upto):
    A = [0]*(upto+1); A[0] = 1
    for i in range(1, 7):
        B = [0]*(upto+1)
        for n in range(upto+1):
            if A[n] == 0: continue
            m = n
            while m <= upto:
                B[m] += A[n]; m += i
        A = [B[n] - (B[n-l-i] if n-l-i >= 0 else 0) for n in range(upto+1)]
    return A
def g6(l):
    if l == 0: return 1
    A = dp_a(l, 3*l)
    return A[3*l] - A[3*l-1]
even = list(range(2, 15, 2))
odd = [15, 17, 19, 21, 23, 25, 27]
print("l      :", " ".join(f"{l:>4}" for l in even + odd))
print("g6(l)  :", " ".join(f"{g6(l):>4}" for l in even + odd))
zeros = [l for l in range(1, 14) if g6(l) == 0]
assert zeros == [1, 3, 5, 7, 9, 11, 13], zeros
assert all(g6(l) == g6(l-15) for l in (27,))
print("zero classification (finite l<=13): g6(l)=0 iff l odd, 1<=l<=13: PASS")
