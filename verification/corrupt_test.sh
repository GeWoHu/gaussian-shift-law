#!/usr/bin/env bash
# MATH-10 deliberate certificate corruption tests.
# Each corruption MUST be detected (nonzero exit). If any mutant survives, this fails.
set -u
cd "$(dirname "$0")"
mkdir -p corrupt_tmp
survived=0

mutate() { # file sed_expr label
  local src="$1" expr="$2" label="$3"
  local dst="corrupt_tmp/$label.py"
  sed "$expr" "$src" > "$dst"
  cmp -s "$src" "$dst" && { echo "HARNESS ERROR: mutation '$label' changed nothing"; survived=1; return; }
  $PY "$dst" > "corrupt_tmp/$label.out" 2>&1
  local rc=$?
  if [ $rc -ge 126 ] || [ $rc -eq 2 ]; then
    echo "HARNESS ERROR (rc=$rc, crash not assertion): $label"; survived=1
  elif [ $rc -eq 0 ]; then
    echo "SURVIVED (BAD): $label"; survived=1
  elif grep -q "AssertionError" "corrupt_tmp/$label.out"; then
    echo "DETECTED: $label (AssertionError, exit $rc)"
  else
    echo "HARNESS ERROR (rc=$rc, non-assertion failure): $label"; survived=1
  fi
}
PY=python3

# 1. Perturb one induction-base value of Q6 in the shift certificate.
mutate verify_shift.py 's/assert all(qp\[n % 60\].subs(t, n \/\/ 60) == Q6\[n\] for n in range(120)), "S1 base"/Q6[77] += 1\n    assert all(qp[n % 60].subs(t, n \/\/ 60) == Q6[n] for n in range(120)), "S1 base"/' corrupt_base
# 2. Change the shift from 15 to 13 in the branch-identity loop.
mutate verify_shift.py 's/Gsym(r) - Gsym(r-15)/Gsym(r) - Gsym(r-13)/' corrupt_shift
# 3. Flip the sign of the compared quantity in the central certificates
#    (claims M_7 >= M_j instead of M_j >= M_7: a FALSE statement, must fail).
mutate verify_central.py 's/Mexpr(r, j) - M7/M7 - Mexpr(r, j)/1' corrupt_signflip
# 4. Raise the claimed clearance threshold above the true Delta_16=7
#    (g6(12)=8 < 9 falsifies the finite base claim).
mutate verify_clearance.py 's/TH = {8: 1, 12: 3, 16: 7}/TH = {8: 1, 12: 3, 16: 9}/' corrupt_threshold

echo "CORRUPTION SUITE: $([ $survived -eq 0 ] && echo 'PASS (all mutants detected)' || echo 'FAIL (mutant survived)')"
exit $survived
