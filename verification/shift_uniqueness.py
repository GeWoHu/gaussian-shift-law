#!/usr/bin/env python3
"""MATH-10: NUMERICAL uniqueness scan for the shift constant (evidence, NOT proof).

For each odd c in {1,3,...,45}: test g6(l) == g6(l-c) for every odd l in [c+17, 129]
(the frozen MATH-09 window). Result labels: numerically established only.
"""
def dp_g(l):
    if l <= 0: return 1 if l == 0 else None
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
cache = {}
def G(l):
    if l not in cache: cache[l] = dp_g(l)
    return cache[l]
passing = []
for c in range(1, 46, 2):
    start = c + 17 + ((c + 17) % 2 == 0 and 1 or 0)  # first odd l in window
    ok = all(G(l) == G(l-c) for l in range(start, 130, 2))
    if ok: passing.append(c)
print("odd shifts c passing on window [c+17,129]:", passing)
assert passing == [15], passing
print("NUMERICAL: only c=15 survives (verified, not proved)")
