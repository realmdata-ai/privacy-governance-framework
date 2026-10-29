# Complete worked case — a synthetic calibration dataset

Preview 0.2.0-preview.1 · 29 October 2026 · Reconstructed PGF teaching case

## 1. What the case establishes

This case reconstructs **DPIA-CS-TRAIN-01**, PGF Document 19, using Document 18 Project 2 and Example 2.1-R. All organisations, values, test intervals and decisions are illustrative. The source does not report real attack experiments. This companion reproduces its reasoning and arithmetic; it does not run a generator, validate a deployed PET or create a new processing authorisation.

The business purpose is to calibrate a credit-scoring model using a synthetic dataset instead of giving Data Science the customer records. The source population is approximately 1.2 million customers. The source information and derived synthetic dataset remain **Restricted / personal data**; no anonymity conclusion is made. The training-data DPIA does not authorise production automated credit decisions, which have separate assessments in PGF.

Two times must remain distinct: the original processing decision was made on **25 March 2026**; the cumulative privacy-loss snapshot used here is **26 October 2026**. The later snapshot does not invent an earlier expenditure or re-charge historical runs. The [evidence index](evidence/00_INDEX.md) links the records that fill this case.

## 2. Scope and data flow

Customer/application records and independently controlled credit-bureau data → controlled source extract → generator training inside the privacy engineering environment → authorised synthetic output → internal Data Science calibration. Source extracts, generator parameters and checkpoints stay inside the controlled environment. There are no external recipients or third-country transfers in this activity. A separate supplier or transfer would change those facts and reopen the assessment.

The protected unit for DP is **one customer, including that customer's records**, with a contribution bound. The adjacency relation is add/remove one customer. The relevant observer for the synthetic output is a moderately resourced insider or contractor in Data Science with public or commercially available auxiliary information. Personnel with access to the source or generator are covered by a separate misuse scenario.

## 3. Filled records and legal triage

| Record | Filled teaching conclusion | Evidence reference |
|---|---|---|
| Processing record | Internal calibration on synthetic data; Head of Credit Decisions owns the activity; source/derived data and retention are recorded | [ADP-02](evidence/02_PROCESSING_RECORD.md) |
| Legal gate | Source example records Art. 6(1)(f), a balancing test, Art. 6(4) compatibility and transparency; no Art. 9/10 data in this defined source | [ADP-03](evidence/03_TRIAGE_AND_LEGAL.md) |
| DPIA triage | Financial data, large scale and matching/combining datasets; a DPIA is required in the example | [ADP-03](evidence/03_TRIAGE_AND_LEGAL.md) |
| Transfer triage | No importer outside the EEA and no external recipient in scope; no TIA for this flow | [ADP-02](evidence/02_PROCESSING_RECORD.md) |
| Project passport | Output, observers, mandatory tests, thresholds and DP statement are fixed | [ADP-01](evidence/01_PROJECT_PASSPORT.md) |

These are reconstructed fictional conclusions, not legal advice for another bank. An adopter must provide its own applicable-law analysis, actual data facts and evidence. Consent is not added as a scoring mitigant, and utility is not used to offset a legal failure or silently lower the individual-harm score. Adopted release conditions are checked separately.

## 4. First design: Medium calculation, separate redesign decision

Example 2.1 used epsilon 2.1 and delta 8×10^-6, differing from the selected project's epsilon at most 2.0 at configured delta 1×10^-9. Its four point-estimate terms give `(0.40 + 0.70 + 0.15/0.19 + (1-0.78)/0.30)/4 = 0.6557018`, rounded to **0.656 -> Medium likelihood**. Severity remains Significant, so the computed S1 risk is **Medium**. The configuration differences are recorded, the Group DPO raises the concern and the Head of Credit Decisions chooses redesign. The output is not released to Data Science; no automatic High or Near-certain override is applied. Because Privacy Engineers observed the output, epsilon 2.1 and delta 8×10^-6 remain charged in the lifetime ledger. Withholding the release does not erase that observation.

## 5. Reconfigured design: the numerical assessment

The reconfigured run has epsilon 1.8 at delta 1×10^-9. All mandatory test values and intervals are illustrative source assumptions; they were not recomputed from a real test sample by this companion. [ADP-04](evidence/04_METRICS_AND_GATES.md) gives the full table and its boundaries.

The four weighted terms are:

| Term | Calculation from the point estimate | Weighted contribution |
|---|---|---|
| Membership accuracy | abs(0.53−0.50)/0.10 = 0.30 | 0.30×0.25 = 0.075 |
| Membership AUC | abs(0.55−0.50)/0.10 = 0.50 | 0.50×0.25 = 0.125 |
| DCR P5 | 0.15/0.21 = 0.7142857 | 0.1785714 |
| NNDR median | (1−0.81)/0.30 = 0.6333333 | 0.1583333 |
| **Disclosure indicator** | Sum of weighted terms | **0.5369048 ≈ 0.537** |

The indicator is an ordinal index, not a probability of re-identification. The configured point estimates enter this calculation. Comparisons against the stated unfavourable interval bounds remain evidence observations; they are not a second tier calculation. The complete indicator falls in the source band 0.5–1.0, so S1 likelihood is **Medium**. DP/configuration evidence, claim support, the adopted budget and decision conditions are checked separately. See the [source-compatibility note](PGF_1_0_0_COMPATIBILITY.md) for retained gate terminology in the published tables.

Severity is 3 for Restricted data + 0 special-category/offence modifier + 0 vulnerability modifier + 3 for scale + 1 for source aggregation + 0 internal reach + 0 automated-decision effect in this disclosure scenario + 0 provenance = **7 → Significant**. S1 is therefore **Medium likelihood × Significant severity = Medium**.

S2 concerns misuse of source data or generator parameters inside the controlled environment. Residual likelihood is 1+1+0+1 = **3 → Low**; inherent likelihood with unmitigated L3 is 1+1+3+1 = **6 → Medium**. Severity stays Significant. Both Low×Significant and Medium×Significant map to **Medium**. The activity's track (a) residual and inherent tiers are **Medium**. Track (b) is 1 applicable-regime +1 financial +1 reputational = **3 → Moderate**, reported separately and not netted against track (a).

## 6. Consultation and the historical decision

The source records Group DPO advice on 24 March 2026: a per-run epsilon condition of at most 2.0, disclosure of the model-inversion test limitation and reassessment before the next calibration. The advice was followed. The business record presents the calibration benefit (avoid source-record access by Data Science), the Medium individual-risk result, separate Moderate organisational consequences, alternatives (redesign, restricted use or no release), the advice and response, conditions and review triggers. No monetary cost or additional historical dissent is invented. Legal & Compliance separately evaluated G-36 on 24 March and recorded that the statutory test was not met, with reasons; this is not an automatic conclusion derived from the word Medium.

On **25 March 2026**, the Head of Credit Decisions accepted Medium with conditions under the then-effective authority. The CPO did not concur in that March decision: that position was created later. The acceptance expires on **25 March 2027 or the next calibration, whichever comes first**. Reassessment under the rules effective from 23 October 2026 requires the Processing Owner with CPO concurrence for Medium. The DPO advises rather than accepts the risk. [ADP-06](evidence/06_DECISION_AND_CHRONOLOGY.md) distinguishes the two authority periods.

## 7. Lifetime accounting at 26 October

The source snapshot includes three already-observable expenditures: initial generator (not released) 2.1/8×10^-6; reconfigured generator 1.8/1×10^-9; and the federated model's all-rounds expenditure 2.6/1×10^-9. Basic composition gives **epsilon 6.5; delta 8.002×10^-6**. The illustrative lifetime caps are epsilon 10 and delta 1×10^-5. The 2026 epsilon pacing cap is7. All are respected, but delta utilisation is **80.02%**, so the adopted warning level is reached.

This reconstruction adds **zero** new expenditure. It reports the source ledger and does not manufacture another release. The conservative observer/overlap assumptions and exact arithmetic are in [ADP-07](evidence/07_LEDGER_AND_CHANGE.md).

## 8. A change that the old decision cannot authorise

For teaching, suppose a proposed further run requests epsilon0.4 and delta3×10^-6. This proposal is **not a source event** and has not been run. The lifetime preflight would be epsilon6.9 and delta 1.1002×10^-5. Epsilon is within both illustrative caps; delta exceeds the lifetime cap by1.002×10^-6. Its configured delta also falls outside the existing project's1×10^-9 setting. These are two separate release-constraint observations. The proposal has no new measurement inputs, so no new calculated tier or complete assessment is claimed; the old Medium acceptance does not cover it.

The action is to stop before execution, record the proposal as unapproved and reopen the passport, gates and decision for any changed design. New selected weighted inputs and claim evidence are not available: calculation INCOMPLETE, no computed tier, no new claim of test PASS or acceptance. The proposal is not charged merely because it was calculated: no run or observable output occurred. If an actual failed or cancelled run had produced observable output, it would require accounting under the observation boundary. Calendar rollover would not reset either lifetime total.

## 9. Monitoring and disposal

Named Privacy Engineers control source/parameter access; Data Science receives only the authorised synthetic artefact. Monitoring checks new outputs, recipients, auxiliary-data assumptions, attack evidence, accountant/implementation changes, the ledger and decision expiry. Erasure and retention follow the contextual rules of the source: extracts30 days after validation; parameters until synthetic-dataset retirement; synthetic calibration dataset for the model version's operational life plus2 years, all illustrative internal settings subject to applicable duties. A monthly reconciliation does not postpone a deadline. [ADP-08](evidence/08_MONITORING_AND_RETENTION.md) supplies owners and action triggers.

## 10. What an adopter must replace

Replace the fictional legal analysis, organisational delegations, data and test evidence with your own. Rejustify thresholds, scope, privacy unit, observations, statistical design and retention. Keep the relationships between claims, gates, decisions and monitoring. A reproduced sum demonstrates arithmetic; it does not establish anonymity, actual DP implementation correctness or legal permission to process.
