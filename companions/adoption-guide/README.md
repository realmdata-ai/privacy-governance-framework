# PGF Adoption Guide and Complete Worked Case

**Preview 0.2.0-preview.1 · 29 October 2026 · Review copy.** This separate companion targets published PGF 1.0.0 (tag `v1.0.0`). It changes no PGF source or release file and creates no new release dependency. Read the [compatibility note](PGF_1_0_0_COMPATIBILITY.md), including the disclosed Doc 08 / Doc 18 inconsistency, and [migration record](CHANGES.md). The repository documentation licence applies within its stated scope; this update grants no new software licence.

Start with the [adoption guide](ADOPTION_GUIDE_EN.md). It explains routes through PGF, proportionate roles, working duties and exit criteria. Then read the [complete worked case](COMPLETE_WORKED_CASE_EN.md), which reconstructs the synthetic calibration example already present in PGF. Inspect its [filled evidence bundle](evidence/00_INDEX.md) and [machine-readable case records](evidence/CASE_RECORDS.json). Use the [checklist](ADOPTION_CHECKLIST.md) against an actual adoption proposal.

## What the package provides

| Material | Purpose |
|---|---|
| ADOPTION_GUIDE_EN.md | Scope, routes, roles, adoption sequence, evidence and management actions |
| COMPLETE_WORKED_CASE_EN.md | A complete scenario from purpose and triage through calculations, historical decision, ledger and changed proposal |
| evidence/ | Filled passport, processing, legal/triage, metric, risk, decision, ledger and monitoring records with traceable IDs |
| ADOPTION_CHECKLIST.md | Questions with concrete evidence and exit criteria |
| SOURCES_AND_LIMITATIONS.md | Baseline, primary references, scope and reproducibility limits |
| verify_examples.py; schemas/; reports/ | Portable consistency checker, data contracts and reproducible report |

The case preserves the source's illustrative values. It does not run attacks, generate synthetic data, validate a real DP mechanism or authorise processing. Its given confidence intervals are not derived from a raw sample in this package. The proposed change is explicitly new and hypothetical; it was not executed. Reproducing the arithmetic is one check on teaching consistency, not evidence of legal compliance or anonymity.

## Reproduce the checks

From the repository root, with Python 3.11 or later and no third-party packages:

```bash
python -I companions/adoption-guide/verify_examples.py --require-pgf
```

The command writes [reports/verification_report.json](reports/verification_report.json). It validates the supplied JSON contracts, independently recomputes the teaching arithmetic, checks filled evidence IDs and local Markdown targets, checks the separation of observations, computed tiers and release constraints, and separately compares the adjacent `PGF/` content with [the frozen baseline](evidence/PGF_CONTENT_BASELINE.json). The [reference matrix snapshot](evidence/PGF_REFERENCE_MATRIX.json) is compared with PGF Document 08 when that source is available. The verifier uses only paths relative to this package; no internal working folders, user-specific paths or network access are needed.

For a copy of this companion without the surrounding repository, run `python -I verify_examples.py` from the package folder. Teaching arithmetic and package-local links still run. Missing external PGF sources and their links are reported explicitly as **NOT CHECKED**; the result is `PASS_COMPANION_ONLY_PGF_NOT_CHECKED`, not a claim that PGF integrity passed. Use `--require-pgf` when those external checks are required: absence then fails the run.

The standard-library contract validator executes only the JSON Schema keywords used by the three supplied schemas. Unsupported keywords, duplicate keys, non-finite inputs, missing required schemas and invalid values fail; it is not a general-purpose JSON Schema engine. A passing report means teaching arithmetic and documentation consistency, **not PET validation**.

The independent risk-model and red-team companions have their own scope and version; this guide does not depend on their completion.

Migration checks: 74 verifier checks with adjacent published PGF, plus ten portability/negative scenarios (including standalone operation, missing PGF, changed PGF, missing weighted input/schema and invalid records). The [quality report](reports/quality_checks_preview.json) records the outcomes. A standalone PASS explicitly excludes PGF integrity verification.
