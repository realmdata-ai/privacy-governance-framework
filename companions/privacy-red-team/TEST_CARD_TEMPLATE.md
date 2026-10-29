# Test card template

Preview 0.2.0-preview.1 · Review date: 29 October 2026
**Status:** planned / executed / reviewed. **Criterion result:** PASS / FAIL / INCOMPLETE / NOT APPLICABLE.

| Field | Required content |
|---|---|
| attack_id / campaign_id | Stable identifiers; configuration and target version |
| Question and protected fact | What about which person, group or privacy unit might be disclosed? |
| Observer and output scope | Party, access, outputs, query budget, timing/length/metadata access |
| Auxiliary data | Source, knowledge, population overlap and assumed quality |
| Assumptions / exclusions | Trust, coalition, controls excluding channels; validation reference |
| Procedure | Repeatable steps, inputs, algorithm version and parameters |
| Evaluation design | Calibration/evaluation split, independent units, repetitions, subgroups |
| Positive / negative controls | Known disclosure and expected non-disclosure controls |
| Metric and baseline | Numerator/denominator, units, attack direction, baseline definition |
| Uncertainty and power | Method, confidence level, dependence, minimum useful sample size |
| Predeclared criterion | Locally justified threshold; exact boundary and missing-evidence rule |
| Observation and result | Counts, estimates, intervals, status and evidence references |
| Calculation role | Selected weighted input / review-only diagnostic / evidence for a specific claim; configured project and statistic |
| Calculation handoff | Supplied or separately calculated tier and reference; no tier if selected weighted inputs are missing; card status is separate |
| Claim support | Evidence for the particular DP/anonymity claim, or explicitly not substantiated |
| Separate release constraints | Confirmed legal prerequisite, adopted budget cap or explicit output/release condition; source, owner and status |
| Harm and decision link | Affected people; PGF scenario; DPO/Legal advice including dissent; authorised decider and response |
| Remediation / retest | Action, owner, due date, trigger and linked previous finding |
| Limitations | Untested channels, insufficient power and unverified assumptions |

No threshold in this template is a legal safe harbour. An empty required card field needs an explicit INCOMPLETE card disposition; it is not a successful negative result. Classify the resulting gap separately: selected weighted input, diagnostic, claim evidence or adopted release condition. Do not automatically replace a complete calculated tier because a diagnostic card is FAIL or INCOMPLETE. See the [compatibility note](PGF_1_0_0_COMPATIBILITY.md).
