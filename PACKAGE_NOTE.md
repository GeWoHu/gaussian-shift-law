# PACKAGE NOTE — layout and license scope (verification ZIP)

This ZIP uses the **archive layout**: the manuscript lives in `manuscript/`
(`manuscript/paper.tex`, `manuscript/paper.pdf`). The public Git checkout uses
`paper/paper.pdf` and `paper/paper.tex` for the same byte-identical files.

`MANIFEST.sha256` validates **this ZIP layout only** (paths relative to this root;
the manifest file excludes its own hash). Run:

    sha256sum -c MANIFEST.sha256

Reproduction (from this root, Python >= 3.11 + SymPy >= 1.12):

    cd verification && bash run_all.sh
    cd ../verification_independent
    python3 independent_check.py
    python3 tail_recert.py
    python3 helper_contracts.py

License scope:
- Manuscript (`manuscript/` in this ZIP; `paper/` in Git): **CC0 1.0 Universal**
  — see LICENSE-CC0-1.0.txt.
- Verification software and documentation (everything else): **MIT**
  — see LICENSE-MIT.txt.

Status: public research preprint, not peer reviewed. Historical internal reports
(INDEPENDENT_VERIFICATION.md, REFEREE_REPORT.md, REPAIR_LOG.md, HERMES_REVIEW.md)
are audit-trail records; current status is in VERDICT.md and AUDIT_SUMMARY.md.
