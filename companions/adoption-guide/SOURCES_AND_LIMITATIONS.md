# Sources and limitations

Preview 0.1.0-preview.1 · 27 October 2026 · Reference baseline: accepted English PGF 1.0.0-rc.1, content commit `02ff78357f3b24f607651f0bf9f01c6c279b587b`; later metadata freeze does not change the 32 content files used here. The package includes a relative-path SHA-256 baseline for those 32 files and a separately attributed matrix snapshot. This companion is separately versioned and does not amend PGF v1.

## 1. PGF source map

| Companion content | Frozen PGF source |
|---|---|
| Adoption sequence and immediate duties | [Overview, Quick start](../../PGF/00_Framework_Overview_EN.md), Section 4 |
| Roles, proportional organisation and authority | [Charter](../../PGF/02_Privacy_Governance_Charter_EN.md), Sections 4/8/9; [RACI](../../PGF/05_Privacy_RACI_Matrix_EN.md); [owner register](../../PGF/25_Process_Owner_Register_EN.md) |
| Scenario matrix, current authority and limits | [Risk appetite](../../PGF/08_Privacy_Risk_Appetite_Statement_EN.md), Part B Sections 3–5 |
| Source synthetic case and calculations | [Risk method](../../PGF/18_Privacy_Risk_Assessment_Methodology_EN.md), Part B Project 2 Sections 4.B.1–4.B.6 and Example 2.1-R |
| Historical legal/consultation/decision sequence | [DPIA method](../../PGF/19_DPIA_Methodology_and_Template_EN.md), Report DPIA-CS-TRAIN-01 |
| Processing facts and dataset states | [RoPA](../../PGF/21_Record_of_Processing_Activities_EN.md), expanded RoPA-CS-002; [inventory](../../PGF/23_Data_Inventory_and_Data_Flow_Maps_EN.md), DI-CS-0874 |
| Current risk/condition register | [Risk register](../../PGF/22_Privacy_Risk_Register_EN.md), PRR-CS-TRAIN-01 |
| Retention and erasure | [Retention policy](../../PGF/11_Data_Retention_and_Disposal_Policy_EN.md), Part B retention rows and Section 3.5 |
| Evidence integrity, validation and monitoring | [Tooling strategy](../../PGF/09_Privacy_Automation_and_Tooling_Strategy_EN.md), Sections 4/8; [monitoring](../../PGF/27_Privacy_Audit_and_Monitoring_Programme_EN.md); [metrics](../../PGF/28_Privacy_Metrics_Dashboard_EN.md) |

Some sources contain both Part A and Part B with repeated section numbers. The table names the part or worked record where necessary. Plain file links are used so that a reader can select the named heading without an ambiguous duplicate section anchor.

## 2. Primary references for further implementation work

These references support interpretation and further implementation; this companion does not claim a fresh complete legal review of every jurisdiction or a new standards crosswalk.

- [GDPR official text](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng/): accountability, lawful processing, rights, design, risk assessment, consultation and DPO tasks. Apply the version and national provisions relevant to the actual activity.
- [EDPB, DPIA/high-risk processing guidance collection](https://www.edpb.europa.eu/documents/guideline/data-protection-impact-assessments-high-risk-processing_en): DPIA interpretation and the referenced WP248 methodology; the adopted framework distinguishes these criteria from internal policy triggers.
- [EDPB, Article 25 guidelines](https://www.edpb.europa.eu/documents/guideline/guidelines-42019-on-article-25-data-protection-by-design-and-by-default_en): data protection by design and default.
- [NIST SP 800-226, final March 2025](https://csrc.nist.gov/pubs/sp/800/226/final): evaluating differential-privacy guarantees, assumptions and implementation hazards. A successful attack test is not a proof that a DP implementation is correct, and an unsuccessful attack is not proof of anonymity.
- [NIST SP 800-188, final September 2023](https://csrc.nist.gov/pubs/sp/800/188/final): de-identification techniques, governance and data-sharing arrangements.

No claim is made that these organisations endorse this companion or PGF.

## 3. What has and has not been reproduced

The companion reproduces arithmetic from given illustrative inputs: metric normalisation/weighting; severity and likelihood sums; matrix results; track (b); lifetime and proposed-budget calculations. It also checks record links and IDs and verifies that the accepted PGF content hashes are unchanged. The included verifier and its [report](reports/verification_report.json) record the checks performed. An absent adjacent PGF source is explicitly not checked unless required by the command option.

It has not reproduced attack experiments, raw-sample confidence intervals, generator training, DP-SGD implementation, a Rényi accountant, secure infrastructure, legal conclusions or actual decisions. None of those missing activities is filled by the arithmetic check. The source's intervals and measurements remain clearly labelled illustrative assumptions. The activity-level inherent Medium is inherited from the source DPIA; this companion derives S2's inherent calculation but does not invent a separate pre-PET S1 likelihood. It keeps the first generator's as-proposed failure distinct from the accepted configuration's inherent record. The narrow DP membership bound in the source is not used as a probability of re-identification here.

## 4. Scope boundaries

- The complete case is a fictional bank example; its role hierarchy, internal thresholds, conditions and retention periods do not automatically apply to smaller organisations or other sectors.
- Art. 6(1)(f), compatibility and G-36 conclusions in the case are the source's fictional records. A real controller must supply its own facts, applicable-law analysis and evidence.
- Calibration is separate from production credit decisions. The case's Medium acceptance does not authorise automated approval/refusal or the launch of a credit-scoring product.
- No external recipient or third-country flow is included. Adding one reopens recipient/transfer and other relevant assessments; synthesis is not a Chapter V exemption.
- The October ledger includes historical expenditure. It must not be read as a claim that the whole total had already been spent in March or as a new charge caused by this companion.
- The additional epsilon 0.4/delta 3×10^-6 run is a deliberately unexecuted teaching proposal. It fails both the current lifetime delta cap and the accepted project configuration; no result or acceptance is invented for it.
- Full application requires current law, adopted organisational rules, competent roles, real tests, implementation evidence, retention execution and independent review appropriate to the context. A documentation package alone supplies none of these operational facts.

## 5. Review and distribution status

The materials are a preview for author and technical review. Placement in the existing private repository is authorised separately from public distribution. They remain outside the accepted PGF v1 release and its public export. Authorship, rights, licence, public release and future integration retain their applicable approval gates. Existing source repositories remain unchanged.
