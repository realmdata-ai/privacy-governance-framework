# PGF Companion Resources

**Updated 29 October 2026.** These independently versioned previews support review and feedback. Adoption Guide and Privacy Red-Team Playbook **0.2.0-preview.1** target published **PGF 1.0.0**, tag `v1.0.0`, DOI [10.5281/zenodo.23764105](https://doi.org/10.5281/zenodo.23764105). They do not change that release or form part of its Zenodo deposit.

The **risk-model companion remains 0.1.0-preview.1 and describes rc.1**. It has not been migrated to the published method. Its earlier metric-gate logic is not a requirement of PGF 1.0.0; full specification and independent reference reconciliation remain pending. Do not transfer its rules or test results to the updated companions without a separate review.

| Resource | Version / baseline | Start here | Contents |
|---|---|---|---|
| Adoption | 0.2.0-preview.1 / PGF 1.0.0 | [README](adoption-guide/README.md) | Adoption routes, complete case, eight filled records, JSON contracts and portable verifier |
| Privacy red teaming | 0.2.0-preview.1 / PGF 1.0.0 | [README](privacy-red-team/README.md) | Twelve test cards, worked campaign, thirteen attack/evaluation fixtures and six governance-handoff controls |
| Risk model | 0.1.0-preview.1 / rc.1 | [README](risk-model/README.md) | Introduction, two worked examples, formula review and 27 research counterexample tests; full specification/reference reconciliation pending |

## Reading order

Begin with the adoption guide and complete case, then the red-team playbook for evidence production. Both packages include an explicit [Doc 08 / Doc 18 compatibility note](adoption-guide/PGF_1_0_0_COMPATIBILITY.md). They follow Document 18's final direct calculation rules, retain individual observations and distinguish legal/budget/release constraints from the business decision. The source inconsistency is disclosed rather than silently edited.

Read the risk-model material separately, with its rc.1 baseline and errata visible. Neither updated package depends on that companion's completion.

## Reproducibility and interpretation

Each package documents its own command and coverage. A passing arithmetic check or unit test demonstrates only the stated property for the supplied inputs. It does not certify a PET implementation, prove anonymity, validate legal conclusions or establish empirical calibration of the PGF risk scales. Artificial data, assumed evidence and unverified claims are identified as such.

The risk-model package separates tests of research counterexamples from reconciliation against independently derived reference examples. A development run that omits reconciliation is not a complete validation pass.

## Version and distribution

See each package's README, limitations and migration record. The repository documentation licence applies within its stated scope; this update grants no new software licence or rights in third-party material. Provenance/licensing limitations in the unchanged risk-model snapshot remain explicit. No companion changes PGF 1.0.0 content, tag, master PDF or DOI deposit.
