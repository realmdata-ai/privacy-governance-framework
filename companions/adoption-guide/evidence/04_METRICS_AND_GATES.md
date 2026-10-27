# ADP-04 — Metrics and gate record

Imported illustrative values from PGF Document 18 Example 2.1-R. No attack was run by this companion. Intervals are source assumptions, not confidence intervals computed from a supplied raw sample.

| Mandatory item | Point/95%interval | Declared criterion | Gate check |
|---|---|---|---|
| MIA accuracy, balanced sample | 0.53 / 0.52–0.54 | <0.60 on orientation-invariant unfavourable bound | 0.54 < 0.60:Pass |
| MIA AUC | 0.55 / 0.54–0.56 | <0.60 on orientation-invariant unfavourable bound | 0.56 < 0.60:Pass |
| TPR at FPR0.1% | 0.2% / 0.11%–0.37% | ≤1.0% | 0.37% ≤ 1.0%:Pass |
| DCR P5 | 0.21 / 0.20–0.22 | ≥0.15; no exact copy(DCR = 0) | 0.20 ≥ 0.15; no exact copy assumed:Pass |
| NNDR median | 0.81 / 0.80–0.82 | >0.70 | 0.80 > 0.70:Pass |
| TP-SYN-LINK advantage | 0.01 / −0.005–0.025 | ≤0.05 | 0.025 ≤ 0.05:Pass |
| TP-SYN-INF advantage | 0.02 / 0.005–0.035 | ≤0.05 | 0.035 ≤ 0.05:Pass |
| Run epsilon | 1.8 | ≤2.0 | Pass |
| Configured delta | 1×10^-9 | 1×10^-9 | Pass |
| Full DP statement/mandatory coverage | Given in source assumptions | Valid statement and all required items | Conditional on the stated evidence, not newly verified |
| Lifetime/annualbudget | ADP-07 | Within adoptedcaps | Pass at26 October snapshot; delta warning reached |

Normalised weighted point estimates: accuracy0.30×0.25 = 0.075; AUC0.50×0.25 = 0.125; DCR(0.15/0.21)×0.25 = 0.1785714; NNDR((1−0.81)/0.30)×0.25 = 0.1583333. Sum 0.5369048≈0.537. Epsilon, delta, TPR, linkage and inference are gates here; they do not acquire invented weights.

On the source's complete illustrative evidence, module outcome PASS and indicator 0.537 imply S1 likelihood Medium. If a required result or valid DP statement were missing, the module would be INCOMPLETE. The model-inversion limitation is stated separately; keeping generator parameters out of the synthetic-data recipient's access is not a measured model-inversion result. Parameters/source misuse remains scenario S2.

The observed membership advantage is0.06 on the balanced sample (2×0.53−1); upperaccuracy0.54 corresponds to0.08 advantage. It is not a population probability of harm, and a balanced-test precision cannot be transplanted to a different membership base rate.
