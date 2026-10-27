# ADP-07 — Lifetime ledger and failed proposed change

These are illustrative source values. Basic composition is used over one overlapping customer population; observers are conservatively treated as able to combine outputs. No disjointness proof or tighter compatible common accountant is supplied.

| Existing expenditure | Epsilon | Delta | Observation |
|---|---|---|---|
| Initial generator, Example 2.1 | 2.1 | 8×10^-6 | Output observed by Privacy Engineers; release to Data Science failed |
| Reconfigured generator, Example 2.1-R | 1.8 | 1×10^-9 | Privacy Engineers and Data Science observe the synthetic output |
| Federated consortium, all rounds included in the 26 October snapshot | 2.6 | 1×10^-9 | Consortium members |
| **26 October cumulative total** | **6.5** | **8.002×10^-6** | All three are already accounted for |

The March generator decision and the October cumulative snapshot are different facts. This table does not assign dates to individual federated rounds. This companion does not charge any entry a second time. It assumes the source's statement that there are no other DP mechanisms on this population and that the guarantees apply to the same customer-level privacy unit.

| Current illustrative cap | Total | Remaining headroom |
|---|---|---|
| Lifetime epsilon at most 10 | 6.5 | 3.5 |
| Lifetime delta at most 1×10^-5 | 8.002×10^-6 | 1.998×10^-6 |
| New epsilon spending in calendar year 2026 at most 7 | 6.5 | 0.5 |

Delta utilisation is 8.002×10^-6 / 1×10^-5 = **80.02%**, reaching the internal 80% warning level. None of the caps is a statutory safe harbour or evidence of anonymity. Calendar rollover does not reset lifetime epsilon or delta. A lower delta on a later run does not remove earlier delta.

## Hypothetical proposed change — not run

A proposed further run requests epsilon 0.4 at delta 3×10^-6. Prospective totals are epsilon **6.9** and delta **1.1002×10^-5**. Epsilon passes the illustrative lifetime and annual caps. Delta fails the lifetime cap by **1.002×10^-6**. The proposed configured delta also differs from the accepted project's 1×10^-9 setting. The old acceptance expires at the next calibration and cannot be stretched to cover this changed configuration.

**Disposition:** budget preflight FAIL; do not run; reopen the passport, applicable gates, evidence and decision for any revised proposal. No full-module PASS is claimed; test results for the proposal do not exist. This is a new teaching event, not a source event or a fictitious completed run. It adds no actual charge because it was not executed and no output was observed. An executed failed or cancelled run with observable output would require accounting.

In a real system, concurrent proposals require atomic reservation and charge logic. This record is not a production ledger implementation.
