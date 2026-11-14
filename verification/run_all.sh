#!/usr/bin/env bash
# MATH-10 verification suite: complete runnable proof certificates.
# Exact integer/rational arithmetic only. Exit 0 iff every certificate passes.
set -u
cd "$(dirname "$0")"
mkdir -p out
PY=python3
overall=0
run() {
  local name="$1"; shift
  echo "=== $name ==="
  local t0=$(date +%s)
  "$@" > "out/$name.out" 2>&1
  local rc=$?
  local t1=$(date +%s)
  tail -2 "out/$name.out"
  echo "--- $name: exit=$rc runtime=$((t1-t0))s"
  if [ $rc -ne 0 ]; then overall=1; fi
}
run g6_table            $PY g6_table.py
run counterexample_6_24 $PY counterexample_6_24.py
run verify_core         $PY verify_core.py
run verify_shift        $PY verify_shift.py
run verify_clearance    $PY verify_clearance.py
run verify_central      $PY verify_central.py
run shift_uniqueness    $PY shift_uniqueness.py
echo "SUITE OVERALL: $([ $overall -eq 0 ] && echo PASS || echo FAIL)"
exit $overall
