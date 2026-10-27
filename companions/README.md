# PGF Companion Resources

**Preview 0.1.0-preview.1 · 27 October 2026**

These separately versioned resources support reading, implementing and testing the Privacy Governance Framework. They target the accepted English PGF 1.0.0-rc.1 and do not change its frozen content. Preview means ready for review and feedback; the scope and limitations of each resource remain explicit.

| Resource | Start here | Contents |
|---|---|---|
| Risk model | [README](risk-model/README.md) | Introduction, two worked examples, formula review and 27 research counterexample tests. Full specification and reference/golden reconciliation remain pending. |
| Privacy red teaming | [README](privacy-red-team/README.md) | Playbook, twelve test cards, a worked campaign and thirteen artificial fixtures. |
| Adoption | [README](adoption-guide/README.md) | Adoption routes, a complete worked case, checklist and filled evidence records. |

## Reading order

Begin with the adoption guide and its complete case for an end-to-end view. Read the risk-model introduction for calculation concepts, then the red-team playbook for evidence production. Mathematical and implementation details can be reviewed independently.

## Reproducibility and interpretation

Each package documents its own command and coverage. A passing arithmetic check or unit test demonstrates only the stated property for the supplied inputs. It does not certify a PET implementation, prove anonymity, validate legal conclusions or establish empirical calibration of the PGF risk scales. Artificial data, assumed evidence and unverified claims are identified as such.

The risk-model package separates tests of research counterexamples from reconciliation against independently derived reference examples. A development run that omits reconciliation is not a complete validation pass.

## Version and distribution

These previews are independent of the PGF v1 release package. Open questions are recorded locally, including in the risk-model errata register. Changes proposed there are not silently applied to PGF v1. Licensing and public distribution terms are to be confirmed before public release; this preview does not grant a new licence.
