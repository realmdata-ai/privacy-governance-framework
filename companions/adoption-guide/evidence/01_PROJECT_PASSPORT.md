# ADP-01 — Project passport

Status: teaching reconstruction; no new run or release authorised.

| Field | Filled value |
|---|---|
| Source project | PGF Document 18 Project 2, Example 2.1-R; DPIA-CS-TRAIN-01 |
| Purpose | Calibrate a credit-scoring model without giving Data Science the source customer records |
| Source and population | Derived financial indicators, payment history and independently controlled credit-bureau information; approximately1.2 million customers |
| Artefact/state | Synthetic calibration dataset; Restricted/personal data; no anonymity conclusion |
| Privacy unit/adjacency | One customer across records; contribution bound per customer; add/remove one customer |
| Mechanism/accountant | DP-SGD generator training; Rényi DP accountant; current run epsilon 1.8 at delta 1×10^-9 (illustrative source statement) |
| Assessed observers | Internal Data Science insider/contractor with synthetic output and public or commercial auxiliary information; source/parameter access assessed separately |
| Observable output | Synthetic dataset to Data Science; generator parameters/checkpoints stay inside the controlled engineering environment |
| Scenarios | S1 disclosure through synthetic output; S2 misuse of source/parameters by authorised personnel |
| Weighted inputs | MIA accuracy, MIA AUC, DCR P5 and NNDR median; four weights of 0.25; use point estimates |
| Review-only observations | TPR@FPR0.1%, TP-SYN-LINK and TP-SYN-INF advantages, intervals and coverage |
| Separate claim/release evidence | Actual epsilon/delta and full DP statement; ledger and adopted budget; decision conditions |
| Test design | Source assumes5,000 members+5,000 non-members for balanced MIA;5,000 training+5,000 control records for linkage/inference; five fresh-seed/fresh-split repetitions; illustrative 95% intervals |
| Test boundary | Model inversion from generator parameters is not measured; source keeps parameters inside the controlled environment and records that limitation rather than a measured PASS |
| Rule version | Calculation reconstructed from published PGF 1.0.0 (tag `v1.0.0`); historical decision under then-effective rules, later current-authority conditions separately recorded |

All thresholds are adopted project settings in the fictional bank. An adopter needs its own measurement design and validation of the mechanism, accountant, implementation and observation boundary. Reproducing this passport's text does not supply those facts.
