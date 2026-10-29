# Compatibility with published PGF 1.0.0

**Companion 0.2.0-preview.1 · 29 October 2026.** Baseline: PGF tag `v1.0.0`, content commit `8ac8026aec3620f84c3046f2e13b2d747d321f57`; version DOI [10.5281/zenodo.23764105](https://doi.org/10.5281/zenodo.23764105). This companion does not amend that publication. Source-reference dates remain 26 October 2026 unless explicitly stated otherwise.

## Calculation, observations and decision

Follow [Document 18](../../PGF/18_Privacy_Risk_Assessment_Methodology_EN.md), Part A Sections 3.2, 3.3.0 and 4.2, with [Document 8](../../PGF/08_Privacy_Risk_Appetite_Statement_EN.md)'s matrix and decision authority. For complete valid inputs, calculate the configured indicator and map it once: `0 <= I < 0.5: Low`; `0.5 <= I <= 1: Medium`; `1 < I <= 2: High`; `I > 2: Near-certain`. These are ordinal bands, not probabilities. Do not retune weights, thresholds or the project after seeing a result.

A threshold deviation, reproduced attack or unfavourable confidence bound stays visible. It does not automatically replace the calculated likelihood with High or Near-certain. Record the DPO's advice, including dissent, and the authorised business decider's response. A card-level FAIL is a result against that card's criterion, not an automatic framework-wide risk override.

Missing, invalid or undefined selected weighted inputs or calculation configuration make the calculation INCOMPLETE: no invented tier, zero substitution or silent weight redistribution. Missing diagnostic evidence remains a coverage limitation, not PASS. Evidence needed for a DP guarantee or an anonymity conclusion must exist before that claim is made. A calculated tier alone does not establish either claim.

Confirmed legal failures, adopted budget caps and explicit release conditions are checked separately and can prevent release without changing the computed tier. A disputed legal interpretation is recorded with reasons, assumptions, alternatives, Legal/DPO advice and review date; uncertainty alone is not a confirmed G-L failure. No business decision cures an established legal prohibition or missing prerequisite.

## Known inconsistency in the published source

Document 8 Part B Section 4 still describes Near-certain by reference to a reproduced attack in Document 18 Example 2.2, and retains some gate-based descriptions. Document 18's final worked Example 2.2 explicitly computes `I = 1.441 -> High`, with no separate Near-certain override. Example 3.2 similarly computes `I = 1.203 -> High`. Document 18 Example 2.1-R also retains the heading “Gate on the unfavourable bound” in a table.

These are disclosed source inconsistencies. For this companion's calculations and handoff, use Document 18's explicit integrated-calculation rules and final numerical examples; retain the source's individual comparisons as observations. This is the companion's stated interpretation for reproducibility, not a silent correction or a claim that the published text is fully reconciled. The PGF files, tag, PDF and DOI deposit remain unchanged. Any source correction requires a separate future PGF version.

## Scope of this migration

This preview preserves artificial examples and separates arithmetic checks from real attack, DP implementation, legal and release evidence. It adds no calibrated probability model or new PET claim. PAMOLA may be identified as the illustrative Part B implementation profile; adoption and test cards remain tool-neutral. A named tool is not evidence that it implements or passed the described controls.

See the repository licence for the documentation grant. This migration grants no new software licence and does not relicense third-party material. Companion resources remain outside the PGF 1.0.0 Zenodo deposit.
