# PGF Risk Model — Mathematical Specification and Validation Pack

**Version 0.1.0-preview.1** · review date 27 October 2026 · UK English · research companion to the Privacy Governance Framework (PGF) 1.0.0-rc.1

> **What this is.** This companion explains, formalises and tests the privacy risk model of PGF v1. It covers PGF-08 (risk appetite, matrix and acceptance authority) and PGF-18 (risk assessment methodology), together with their application in PGF-19, PGF-20 and PGF-22.
>
> **What it is not.** It is not part of PGF 1.0.0. It adds no legal obligation, and it is not a condition for using PGF. It is not legal advice, a certification, or evidence that any processing is lawful or anonymous. All organisations, people and figures in the examples are fictional or artificial.
>
> **Baseline.** The companion reproduces PGF v1 exactly as fixed in content commit `02ff78357f3b24f607651f0bf9f01c6c279b587b`. Where v1 seems ambiguous or inconsistent, the point is recorded in [ERRATA.md](ERRATA.md) for a future decision by the PGF authors. It is never silently corrected here.

## Status of this preview

| Part | File | Status in this preview |
|---|---|---|
| Introduction (layer A) | [docs/01_Introduction_EN.md](docs/01_Introduction_EN.md) | reviewable |
| Worked examples | [docs/03_Worked_Examples_EN.md](docs/03_Worked_Examples_EN.md) | RM-EX-01 and RM-EX-02 reviewable, with their machine-readable cases in `examples/`; RM-EX-03 to RM-EX-07 **pending** |
| Check grid (16 matrix cells, band boundaries, override and weight probes) | `examples/RM-GRID/` | reviewable (hand-derived expected values) |
| Review of earlier probabilistic formulas (layer C, research) | [docs/05_Legacy_Formula_Review_EN.md](docs/05_Legacy_Formula_Review_EN.md) | reviewable |
| Research counterexamples | `research/` | reviewable; 27 tests, standard library only |
| Errata and improvement register | [ERRATA.md](ERRATA.md) | reviewable (open register) |
| Mathematical specification of PGF v1 (layer B) | docs/02 | **pending** — drafted, under review; not included in this preview |
| Validation and limits | docs/04 | **pending** |
| Reference implementation, schemas, tests, one-command runner | — | **pending** — under reconciliation; not included in this preview |
| Clause-level source register | [SOURCE_REGISTER.json](SOURCE_REGISTER.json) | reviewable: 101 clause entries with PGF file hashes; every SR-ID cited in the included documents and examples resolves |

## Validation status — read before relying on any result

Validation has two separate steps:

1. **Blind execution and self-tests.** The reference implementation is written directly from the PGF v1 text. Its unit tests use hand-derived literal values, and its strict parsers reject malformed input.
2. **Reconciliation.** The implementation's outputs are compared, field by field, with expected results derived **independently** by hand arithmetic from the same PGF v1 text (`examples/*/expected.json`).

The companion counts as validated only when step 2 completes with no failures and no unexplained skips. **In this preview, reconciliation is not complete, so the reference implementation and its validation report are not included.** The PGF v1 layer therefore carries **no validation verdict** in this preview. Mismatches found so far have been traced either to implementation choices that are now being corrected, or to entries in [ERRATA.md](ERRATA.md) (E-01, E-09, E-10).

Whenever a verdict is given, a passed check will mean only that the stated property holds for the stated fixture. It will not mean that the model is empirically valid, that any processing is lawful, or that data are anonymous.

## How to run what is included

Requirements: Python 3.11 or later, standard library only.

```
cd companions/risk-model
python -I -B -m unittest discover -s research/tests   # 27 research counterexamples (layer C)
```

The one-command runner for the full validation pack will be added when reconciliation is complete.

## Three layers, kept apart

- **A — Introduction and worked examples.** A plain explanation, starting from a concrete case.
- **B — Exact formalisation of PGF v1.**
  - Its scores are **ordinal**: a likelihood score is not a probability, and the severity index is not an expected loss.
  - Tiers come from the PGF-08 matrix.
  - Gates — legal compliance (G-L), DPIA triage, the PET module (G-M1 to G-M5) and prior consultation (G-36) — are separate outcomes and are never folded into one score. Prior consultation is a recorded legal conclusion; the model never derives it from a tier.
- **C — Research.** A critical review of earlier probabilistic formulas: expected loss, noisy-OR, likelihood-ratio products, differential-privacy-to-risk translations and k-anonymity bounds. Each one is tested against exact counterexamples. None of it is part of PGF v1.

## Licence and publication

No licence is granted by this preview, and it is not published. Both depend on decisions outside this companion.
