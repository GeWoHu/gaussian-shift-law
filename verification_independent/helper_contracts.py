#!/usr/bin/env python3
"""v1.1.1 helper-contract regression: tests the PRODUCTION helpers themselves.
tail_recert.minint  : explicit contract (None = unbounded below on integers t>=2)
verify_central.nonneg: extracted production definition (rejects negative-leading linears)
Exit 0 only if every case matches its independently computed expectation."""
import importlib.util, sympy as S, re

def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m

t = S.Symbol('t')
tr = load('verification_independent/tail_recert.py', 'tail_recert')
minint = tr.minint  # production helper

# --- minint contract cases (expectations verified by hand/brute force) ---
assert minint(3 - t) is None                                    # decreasing linear
assert minint(-t**3 - 1) is None                                # negative-leading cubic
assert minint(S.Integer(0)) == (0, 2)                           # zero polynomial
assert minint(S.Integer(-5)) == (-5, 2)                         # negative constant: v<0 -> caller fails
assert minint((t - 2)**2) == (0, 2)                             # minimum 0 at boundary
assert minint(t**2 - 4*t + 6) == (2, 2)                         # vertex at 2
assert minint(t**3 - 2) == (6, 2)                               # increasing on t>=2
assert minint(t**3 - 8*t**2 + 16*t - 4) == (-4, 4)              # interior integer min -4 < boundary 4
assert minint((t - 1)**2) == (1, 2)                             # critical point below boundary
assert minint(t**3 - 12*t) == (-16, 2)                          # critical point exactly at boundary
assert minint(t**3 - 15*t) == (-22, 2)                          # irrational critical point sqrt(5)>2
# brute-force cross-check of the three negative-interior cases on t in [2, 200]
for poly, val in [(t**3 - 8*t**2 + 16*t - 4, -4), (t**3 - 12*t, -16), (t**3 - 15*t, -22)]:
    assert min(int(poly.subs(t, k)) for k in range(2, 201)) == val

# --- verify_central.nonneg production definition ---
src = open('verification/verify_central.py').read()
mm = re.search(r"def nonneg\(Dj\):.*?\n(?=\nfor b in)", src, re.S)
assert mm, 'nonneg definition not found'
tt = S.Symbol('t'); T0 = 2
ns = {'sp': S, 't': tt, 'T0': T0}
exec(mm.group(0), ns)
nonneg = ns['nonneg']
assert nonneg(3 - tt) is False                                  # the historical false accept
assert nonneg(-tt**3 + tt) is False
assert nonneg((tt - 2)**2) is True
assert nonneg(tt**3 - 15*tt) is False                           # negative at t=2
assert nonneg(tt**3 + tt) is True

print('HELPER_CONTRACTS PASS 15 cases (11 minint incl. 3 brute-forced, 4 nonneg)')
