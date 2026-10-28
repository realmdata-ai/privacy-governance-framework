---
title: "Privacy Risk Register"
document_id: PGF-22
level: 2
release_version: 1.0.0
status: publication-ready
authors: ["Alexey Neyman", "Val Khvatov"]
regulatory_reference_date: 2026-10-26
licence: "CC BY 4.0"
rights_holder: "REALM INVEO"
source_provenance: "Derived from internal source set ver.2: Level2/22. Privacy-Risk-Register_ENG.docx.md; sha256 3d6cfc01549f91142bc4c656896b3fa56e99f4f70c65b5359ed027843fad418e"
---

# PGF-22 — Privacy Risk Register

*Privacy Governance Framework (PGF) · Level 2 — Policies and Standards · Version 1.0.0 · Regulatory reference date: 26 October 2026*

> **Status and use.** Part A is a reusable template. Part B is a worked example for a fictional organisation (PanEuropean Bank AG); the named implementation profile identifies a real product; the Bank, deployment, figures, dates and records in Part B are illustrative. Nothing in this document is legal advice or a statement about any real organisation, product or provider.

# **About This Document**

**Purpose.** Document 22 defines the privacy risk record: the fields that the organisation adds to its enterprise risk register so that a privacy risk can be followed through its lifecycle — from identification, through the decision on the residual risk and any treatment, to re-assessment and closure. It records results; it does not calculate them.

**Scope.** The register records risks to the rights and freedoms of individuals (track (a)) identified by DPIAs (Document 19), transfer impact assessments (Document 20), vendor assessments (Document 17) and other sources, together with the decisions taken on them, the status of the prior-consultation test (G-36) and of the transfer gate (G-TIA), and the organisational consequences reported separately (track (b)). Under the "No Duplicate Registers" rule (Document 3, Section 4), it is a privacy-specific extension of the enterprise risk register, not a parallel register.

**Relationships.** Risks are calculated with the Privacy Risk Assessment Methodology (Document 18); tiers and the acceptance authority come from the Privacy Risk Appetite Statement (Document 8); roles follow the RACI Matrix (Document 5, S5). The RoPA (Document 21) describes the processing; the register references it. The register feeds the Privacy Audit & Monitoring Programme (Document 27), the Privacy Metrics Dashboard (Document 28) and the Governance Reporting Template (Document 31).

# **How to Use This Document**

Part A is a template. Text in ***[square brackets, bold italic]*** is a fillable or illustrative placeholder. Blocks marked **Guidance** are removed from the adopted version. Part B shows the template completed for the fictional PanEuropean Bank AG, with an excerpt of the register and two fully expanded records.

> **Guidance.** The register follows the risk-management concepts of ISO 31000 — identification, analysis, evaluation, treatment, monitoring and review, recording and reporting — as a bibliographic reference only; no clause-level conformity is claimed. Three PGF rules shape it: a G-L failure is never recorded as an accepted risk; track (b) never offsets track (a); every decision names a single effective decider.

# **Table of Contents**

**About This Document**
**How to Use This Document**
**Part A — Template**
Glossary of Terms
1. Purpose
2. Scope of Application
3. Privacy Risk Record Structure
4. Record Lifecycle
5. Alignment with the Enterprise Risk Register
6. Roles and Responsibilities
7. Relationship to Other Framework Documents
8. Review and Amendment
9. Approval
**Part B — Worked Example: PanEuropean Bank AG**
Glossary of Terms
1. Purpose
2. Scope of Application
3. Privacy Risk Record Structure at PanEuropean
4. Record Lifecycle at PanEuropean
5. Alignment with the Enterprise Risk Register at PanEuropean
6. Roles and Responsibilities
7. Relationship to Other Framework Documents
8. Review and Amendment
9. Approval
**Appendix to Part B — Register Excerpt**
Fully Expanded Record — PRR-CS-INFER-01
Fully Expanded Record — PRR-PSI-01
**Normative Basis and References**
**Document History (PGF)**

# **Part A — Template**

**Privacy Risk Register of *[Legal Name of the Organisation]***

*Effective Date: **[DD Month YYYY]**  ·  Version: **[x.x]**  ·  Document Owner: **[Executive Privacy Programme Owner (EPPO)]**  ·  Adopted by: **[Executive Management]***

***Version History***

| Version | Date | Changes |
| :---- | :---- | :---- |
| ***[1.0]*** | ***[DD.MM.YYYY]*** | ***[First version of the document]*** |
| ***[x.x]*** | ***[DD.MM.YYYY]*** | ***[Brief description of material changes]*** |

## **Glossary of Terms**

*This table lists only terms defined by this document itself; terms defined in another PGF document are not repeated here.*

| Term | Definition / Reference |
| :---- | :---- |
| PRR | Privacy Risk Register. Used as the identifier prefix of a privacy risk record (for example, "PRR-PSI-01"). |
| ERM | Enterprise risk management — the organisation's enterprise-wide risk framework and its risk register, which own the overall taxonomy. This document extends the ERM record with privacy-specific fields (Section 5). |
| Inherent risk | The track (a) tier of the processing without the measures assessed (Document 18: likelihood with control-gap factor L3 at its maximum; the PET Assessment Module as proposed). |
| Residual risk | The track (a) tier after the implemented and evidenced measures (Document 18). This is the tier on which the decision under Document 8, Section 5, is taken. |
| Target risk | The track (a) tier that the risk owner plans to reach, with a target date and the treatment actions needed. |
| Treatment option | The choice made for the risk, using ISO 31000 concepts: avoid (do not start, stop or redesign the processing); modify likelihood or consequences (additional measures); share (for example, contractual allocation with a processor or joint controller — accountability for track (a) is never transferred); retain (accept the residual risk, possibly with conditions). |
| Conditional acceptance | A decision to accept a residual risk subject to stated conditions and an expiry date, after which the risk is re-assessed and decided again (Document 8, Section 5). |

## **1. Purpose**

This document establishes the content of a privacy risk record and the rules for creating, deciding, escalating, re-assessing and closing it, so that each privacy risk can be followed through its lifecycle and each decision on it can be traced to its evidence.

This document does not calculate likelihood, severity or tiers — that is Document 18 — and does not decide who may accept a tier — that is Document 8, Section 5. It records the results and the decisions.

## **2. Scope of Application**

* ***[This document applies to every risk to the rights and freedoms of individuals with a residual track (a) tier above Low recorded in a DPIA (Document 19), a transfer impact assessment or a calculation requested by it (Document 20), a vendor assessment (Document 17), or a calculation performed under Document 18 for a risk identified through another source (Section 4.1). The organisation may also record Low risks; that choice is documented.]***

* ***[Sources of risk include: DPIAs; TIAs; vendor privacy due diligence (Document 17); audits and monitoring (Document 27); privacy incidents and personal data breaches (Document 14); complaints and data-subject-rights trends (Document 15); supervisory-authority inquiries; and regulatory change (Document 7).]***

* ***[A G-L failure (for example, processing without a lawful basis, a missing Art. 9 condition, or a missed statutory deadline) is not a risk to be accepted. It is recorded as a compliance issue in the issues log with an owner and a remediation date, and the processing is stopped or redesigned. It may give rise to a privacy risk record for the remediation period, but never to an "accepted" status.]***

* ***[A failed G-TIA is not a risk to be accepted. The transfer does not start or is suspended (Document 20, Section 4, step 4.8); the record shows the status "Suspended" or "Not accepted".]***

* ***[This document does not replace the enterprise risk register (Section 5) or the independent statutory records required by law (for example, the Art. 33(5) breach record), which are always kept separately.]***

## **3. Privacy Risk Record Structure**

> **Guidance.** The fields below are the mandatory minimum privacy-specific extension of an ERM record. Where the organisation has no enterprise risk register — a documented decision, not a default (Section 5) — they constitute a standalone record.

| Record Field | Content |
| :---- | :---- |
| Risk Identifier | ***[Unique PRR number; ERM record identifier where integrated]*** |
| Processing Activity | ***[RoPA record identifier (Document 21); the risk references the description of the processing and does not duplicate it]*** |
| Risk Source and Links | ***[Source type (DPIA / TIA / vendor assessment / audit / incident / complaint or rights trend / supervisory-authority inquiry / regulatory change); identifiers of the DPIA, TIA and evidence pack (EVP-YYYY-NNNN)]*** |
| Vendor-Assessment Source | ***[Where the risk involves a processor, joint controller or other recipient: the vendor assessment under Document 17, its date and status (open non-conformities feed Document 18, factor L3)]*** |
| Harm Scenarios | ***[Summary of the scenarios assessed (threat source → event → harm type, Document 18, Factor A) and the scenario that determines the tier — in narrative form, without recalculation]*** |
| Inherent Risk (track (a)) | ***[Low / Medium / High / Critical, per Document 18 and the Document 8 matrix]*** |
| Residual Risk (track (a)) | ***[Low / Medium / High / Critical — current value, updated at each re-assessment]*** |
| Target Risk and Date | ***[Planned tier and date, or "equal to residual" with reasons]*** |
| Track (b) Level | ***[Organisational consequence level (Document 18, Factor F) — reported to ERM separately; it never offsets track (a)]*** |
| Treatment Option | ***[Avoid / modify likelihood or consequences / share / retain — with the actions, owners and dates]*** |
| Risk Owner | ***[The Processing Owner of the processing (first line) — responsible for the treatment plan and for proposing the decision. The privacy function does not own the risks of business processing]*** |
| Decision and Single Decider | ***[The single effective decider under Document 8, Section 5, for the residual tier (one person or body); decision: accept / accept with conditions / do not accept; date; EPPO concurrence where required]*** |
| Conditions and Expiry | ***[For a conditional acceptance: the conditions and the expiry date; re-assessment is due on expiry]*** |
| DPO Advice | ***[Reference to the DPO advice record; whether the advice was followed, partly followed or not followed, with the decider's reasons; any escalation by the DPO]*** |
| G-36 Status | ***[For risks from a DPIA: evaluated (yes/no); legal conclusion — test met / not met — with date and author; any internal-policy routing; where consulted: submission date, supervisory-authority response (written advice / information request / Art. 58 measure / none yet), implementation. A lapse of the period or the absence of comments is recorded as such, never as an authorisation]*** |
| G-TIA Status | ***[For risks involving a transfer: mechanism (Art. 45 / 46 / 49); outcome (pass / fail); date; conditions; suspension or termination where applicable (Document 20)]*** |
| Status | ***[Per the status table below]*** |
| Next Review Date | ***[Not later than the expiry of a conditional acceptance; per Document 19, step 4.9, and Document 20, Section 3.2]*** |
| Change History | ***[Chronology of changes to tiers, decisions and statuses, with dates and reasons — retained for audit (Document 27)]*** |

***Status Values***

| Status | Definition |
| :---- | :---- |
| Open — assessment or decision pending | ***[The risk is recorded; the decision has not yet been taken (for example, a High risk awaiting the completion of a prior consultation). Processing that requires the decision does not start]*** |
| In treatment | ***[Treatment actions are under way to reach the target risk before or after a decision]*** |
| Accepted — conditional (expiry) | ***[The single decider has accepted the residual risk subject to conditions and an expiry date; on expiry, or on breach of a condition, the risk is re-assessed and decided again]*** |
| Accepted | ***[A Low residual risk accepted without conditions (where Low risks are recorded)]*** |
| Not accepted — stopped or redesign | ***[The residual risk was not accepted (including any Critical tier); the processing does not start, is stopped or is being redesigned]*** |
| Suspended | ***[A transfer suspended because G-TIA failed or equivalence can no longer be ensured (Document 20, Section 4, step 4.8)]*** |
| Closed | ***[The processing has ended or the risk no longer exists; the record is kept as history]*** |

***[Where the ERM register uses its own status taxonomy, the organisation maps these statuses to it rather than introducing new ones, provided that "Accepted — conditional (expiry)", "Suspended" and "Not accepted" remain distinguishable.]***

## **4. Record Lifecycle**

| Event | Content |
| :---- | :---- |
| 4.1 Creation | ***[A record is created when a DPIA, TIA or vendor assessment is completed with a residual track (a) tier within scope (Section 2), or when another source identifies a privacy risk and a calculation under Document 18 has been performed for it; an audit or incident investigation does not replace that calculation. The creation date and the initial inherent and residual tiers are recorded and kept in the change history.]*** |
| 4.2 Decision and Escalation | ***[The decision is taken by the single decider under Document 8, Section 5, within the timeframes set there: Low — Processing Owner; Medium — Processing Owner with EPPO concurrence; High — one named member of Executive Management (or the Privacy Risk Committee where a written delegation designates it), after the G-36 step; Critical — not acceptable. The register records the decider, the DPO advice and, where the advice is not followed, the reasons. Governing Body committees are informed of High decisions.]*** |
| 4.3 Re-Assessment | ***[On the expiry of a conditional acceptance; on the review events of Document 19 (step 4.9) and Document 20 (Section 3.2); on a material change to the processing, the recipients, the threat landscape or the law; after a relevant incident. The result updates the residual tier and the status and is recorded in the change history. A changed calculation method does not retroactively change earlier decisions; it applies at the next re-assessment.]*** |
| 4.4 Closure | ***[When the processing ends (in step with the archiving of the RoPA record, Document 21) or the risk no longer exists. Closed records are retained as history, not deleted.]*** |

## **5. Alignment with the Enterprise Risk Register**

This document implements the "No Duplicate Registers" rule (Document 3, Section 4) for privacy risk:

* ***[The enterprise risk register (ERM) is the authoritative register and owns the overall taxonomy. The privacy risk record is an extension of an ERM record, not a separate register.]***

* ***[Mapping: privacy risks are mapped to the ERM taxonomy, including the operational-risk and compliance-risk categories the organisation uses (for a financial institution, typically the operational-risk event types for clients, products and business practices, and ICT risk where relevant).]***

* ***[Track (b) — organisational consequences — is reported to ERM on the ERM scales; track (a) is reported in the privacy risk record. ERM aggregation, limits and heat maps use track (b) and the count of track (a) tiers; they never net a track (a) tier against a benefit or against another risk.]***

* ***[The privacy risk appetite (Document 8) details the enterprise-wide risk appetite for the privacy category; per-process ceilings are hard limits, and aggregation serves portfolio monitoring only.]***

* ***[Reporting: the register supplies the privacy content of the ERM report to Executive Management and the Governing Body committee (Document 31), including High decisions, open prior consultations, conditional acceptances near expiry and suspended transfers.]***

Where the organisation has no enterprise risk register, the decision to maintain this register on its own is documented explicitly.

## **6. Roles and Responsibilities**

| Role | Responsibility |
| :---- | :---- |
| ***[EPPO]*** | ***[Accountable for the register as a process (S5): its structure, completeness and reporting; concurs in Medium acceptances]*** |
| ***[Privacy Operations Lead]*** | ***[Responsible for maintaining records, tracking decisions, conditions, expiry dates and review dates; prepares the privacy content of risk reports]*** |
| ***[Processing Owner]*** | ***[Risk owner of the records for its processing; responsible for the treatment plan; takes or proposes the decision under Document 8]*** |
| ***[Single decider under Document 8]*** | ***[Takes the decision recorded in the register (Processing Owner up to the delegated tier; named member of Executive Management for High)]*** |
| ***[DPO]*** | ***[Consulted on records and decisions; advice recorded; does not approve or accept risk; may escalate directly to Executive Management]*** |
| ***[Legal]*** | ***[Records G-36 conclusions and G-TIA determinations referenced in the register]*** |
| ***[ERM (risk management function)]*** | ***[Consulted on the alignment of records with the ERM taxonomy and scales; receives track (b) levels]*** |
| ***[CISO]*** | ***[Consulted on security-related scenarios and measures]*** |
| ***[Executive Management / Governing Body committee]*** | ***[Informed through risk reports; the Governing Body committee is informed of High decisions and prior consultations]*** |

## **7. Relationship to Other Framework Documents**

* Records results calculated under the Privacy Risk Assessment Methodology (Document 18) without recalculating them.

* Applies the tiers, acceptance authority and timeframes of the Privacy Risk Appetite Statement (Document 8, Section 5).

* Is populated from the DPIA Methodology (Document 19), the TIA Methodology (Document 20) and the Vendor / Third-Party Privacy Risk Policy (Document 17), and from audits (Document 27), incidents (Document 14) and rights trends (Document 15).

* References the RoPA (Document 21) without duplicating its descriptions.

* Is aligned with the enterprise risk register through the Interface & Integration Model (Document 3, Section 3.1, and the "No Duplicate Registers" rule, Section 4).

* Feeds the Privacy Metrics Dashboard (Document 28) and the Governance Reporting Template (Document 31).

* Roles follow the RACI Matrix (Document 5, S5).

## **8. Review and Amendment**

This document is reviewed ***[at least once a year]*** under the ***[Policy Review Cycle, Document 29]***, and upon any change to Document 8 affecting the acceptance authority or timeframes, or to Document 18 affecting the interpretation of recorded tiers (without retroactive recalculation of records). Changes are adopted by ***[Executive Management]*** on the proposal of the ***[EPPO]***, after consulting the ***[Privacy Risk Committee]*** and the DPO.

## **9. Approval**

This document is adopted by ***[Executive Management]*** on ***[date]***. Document Owner: ***[EPPO]***.

# **Part B — Worked Example: PanEuropean Bank AG**

> **Implementation example.** In this Part B, PEP denotes the Bank's **PAMOLA implementation profile**, including separately integrated systems. The product is real; the Bank, deployment, configurations, records and numerical results are illustrative. The example demonstrates the intended workflow and is not evidence that every function is implemented in a released product or that these numbers were measured in a product run. See [the implementation profile](../IMPLEMENTATION_PROFILE.md). Part A remains tool-neutral.


**PanEuropean Bank AG — Privacy Risk Register**

*Effective Date: 20 October 2026  ·  Version: 2.0  ·  Document Owner: Chief Privacy Officer (EPPO)  ·  Adopted by: Management Board*

*A fictional legal entity, provided solely for illustrative purposes.*

***Fictional Document History (illustrative)***

| Version | Date | Changes |
| :---- | :---- | :---- |
| 1.0 | 1 March 2026 | First version, adopted by the Management Board together with Documents 8, 18, 19 and 20; records created earlier in the ERM register were migrated. Owner at the time: Group DPO |
| 2.0 | 20 October 2026 | Re-baselined to the new role model: Chief Privacy Officer as owner; single decider under Document 8, version 3.0; G-36 and G-TIA status fields; inherent, residual and target risk; treatment option; conditional acceptance with expiry; vendor-assessment source |

## **Glossary of Terms**

*The Part A glossary applies; the entries below add PanEuropean specifics.*

| Term | Definition / Reference |
| :---- | :---- |
| Conduct & Privacy Risk | The category of PanEuropean's enterprise-wide risk appetite to which privacy risk records are aggregated (Document 8, Section 3); privacy loss events are also mapped to the operational-risk event types used by the Bank's ERM. |
| HBDI | The Hessian Commissioner for Data Protection and Freedom of Information, PanEuropean's lead supervisory authority. |

## **1. Purpose**

This document establishes PanEuropean Bank AG's privacy risk record as an extension of the Bank's enterprise risk register, which is owned by the Chief Risk Officer's risk management function.

## **2. Scope of Application**

PanEuropean records all completed DPIA, TIA and vendor-assessment outcomes, including Low ones. The extension was adopted because complete records improve trend reporting; Low records are not escalated. G-L failures are recorded as compliance issues in the issues log (Document 27), not as accepted risks; failed G-TIA outcomes are recorded with the status "Suspended" or "Not accepted".

## **3. Privacy Risk Record Structure at PanEuropean**

The fields of Part A, Section 3 are used verbatim. At PanEuropean: the record is aggregated to the "Conduct & Privacy Risk" category and mapped to the ERM operational-risk event types; the G-36 field names the HBDI as competent authority; the record is kept on PEP (the Bank's privacy engineering platform, illustrative) and linked to the ERM record. The statuses of Part A, Section 3 are mapped one-to-one to the ERM statuses by the Chief Privacy Officer and the Chief Risk Officer's risk management function.

## **4. Record Lifecycle at PanEuropean**

| Event | Content |
| :---- | :---- |
| 4.1 Creation | The Privacy Operations Lead creates the record on completion of a DPIA, TIA or vendor assessment, or after a Document 18 calculation for a risk identified through an audit, incident, complaint, supervisory-authority inquiry or regulatory change |
| 4.2 Decision and Escalation | Per Document 8, version 3.0, Section 5: Low — Processing Owner; Medium — Processing Owner with the Chief Privacy Officer's concurrence within 3 business days (default expiry 12 months); High — the Chief Risk Officer within 5 business days after the G-36 step is complete, with the Supervisory Board's Risk Committee informed; Critical — not acceptable, stop or redesign (redesign decision within 10 business days). Decisions taken before 23 October 2026, the date on which Document 8, version 3.0, took effect, were taken under the authority then in force, without Chief Privacy Officer concurrence; they are re-assessed under version 3.0 at expiry |
| 4.3 Re-Assessment | On expiry of a conditional acceptance; at the DPIA and TIA review dates (Document 19, step 4.9; Document 20, Section 3.2); upon a material change, an incident or a change in law or guidance |
| 4.4 Closure | When the processing ends, in step with the archiving of the RoPA record |

## **5. Alignment with the Enterprise Risk Register at PanEuropean**

* The enterprise risk register, owned by the Chief Risk Officer's risk management function, is the authoritative register; each privacy risk record is an extension of an ERM record.

* Mapping: "Conduct & Privacy Risk" category of the risk appetite; operational-risk event types for clients, products and business practices; ICT risk for records involving ICT third-party arrangements (for example, PRR-CLOUD-01).

* Track (b) levels are reported to ERM; track (a) tiers are never netted. The Privacy Risk Appetite Statement (Document 8) details the enterprise-wide appetite for the category and may not exceed its limit.

* The quarterly risk report to the Management Board and the Supervisory Board's Risk Committee (Document 31) includes: High decisions and open prior consultations; conditional acceptances expiring in the next quarter; suspended transfers; and track (b) levels. Its privacy content is prepared by the Privacy Operations Lead for the Chief Privacy Officer. The Group DPO's own report to the Management Board (Document 31) is separate.

## **6. Roles and Responsibilities**

| Role | Responsibility |
| :---- | :---- |
| Chief Privacy Officer (EPPO) | Accountable for the register; concurs in Medium acceptances |
| Privacy Operations Lead | Maintains records on PEP; tracks decisions, conditions, expiries and review dates; prepares the privacy content of risk reports |
| Processing Owners — Head of Credit Decisions (CS records), Head of Customer Service (PRR-LLM-01), Head of Fraud Prevention (PRR-PSI-01, PRR-FL-01), CIO (PRR-CLOUD-01) | Risk owners; treatment plans; decisions up to Medium (with Chief Privacy Officer concurrence for decisions from 23 October 2026); proposals for High |
| Chief Risk Officer | Single decider for High; owner of the enterprise risk register through the risk management function |
| Group DPO | Consulted on records and decisions; advice recorded; may escalate directly to the Management Board |
| Legal & Compliance (General Counsel) | Records G-36 conclusions and G-TIA determinations |
| CISO | Consulted on security-related scenarios |
| Supervisory Board Risk Committee | Informed of High decisions, prior consultations and the quarterly report (oversight only) |

## **7. Relationship to Other Framework Documents**

* Calculations — Document 18 (version 1.2); tiers and authority — Document 8 (version 3.0).

* Sources — Document 19 (DPIAs), Document 20 (TIAs), Document 17 (vendor assessments), Document 27 (audits), Document 14 (incidents), Document 15 (rights trends).

* Processing descriptions — RoPA (Document 21); flows — Document 23.

* ERM alignment — Document 3; reporting — Documents 28 and 31; roles — Document 5.

* Tooling — the Privacy Automation & Tooling Strategy (Document 9).

## **8. Review and Amendment**

This document is reviewed at least annually under the Policy Review Cycle (Document 29) and upon any change to Document 8 or Document 18 that affects the records. Changes are adopted by the Management Board on the proposal of the Chief Privacy Officer, after consulting the Privacy Risk Committee and the Group DPO.

## **9. Approval**

Version 1.0 was adopted by the Management Board on 1 March 2026 (owner at the time: Group DPO). Version 2.0 was adopted by the Management Board on 20 October 2026 on the proposal of the Chief Privacy Officer, after consulting the Privacy Risk Committee and the Group DPO. Document owner: Chief Privacy Officer.

# **Appendix to Part B — Register Excerpt**

Status at 26 October 2026. Tiers are track (a) unless stated; they are taken from the DPIAs and TIAs of Documents 19 and 20, calculated under Document 18.

| Risk Identifier | Source and links | Risk owner | Inherent → residual (target) | Track (b) | Treatment | Decision (single decider) | G-36 / G-TIA | Status |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| PRR-CS-TRAIN-01 | DPIA-CS-TRAIN-01; EVP-2026-0012; RoPA-CS-002 | Head of Credit Decisions | Medium → Medium (target: Medium) | Moderate | Retain with conditions (ε ≤ 2.0 per run; ledger check) | Head of Credit Decisions, 25 March 2026, Group DPO advice followed | G-36 evaluated — not met | Accepted — conditional (expiry 25 March 2027 or next calibration) |
| PRR-CS-INFER-01 | DPIA-CS-INFER-01; EVP-2026-0047; RoPA-CS-003 | Head of Credit Decisions | Critical → High (target: High — structural for automated decisions) | Significant | Modify likelihood (bias testing, validation, monitoring, human review); retain decision pending | Pending — Chief Risk Officer after the consultation step | G-36 met — HBDI consulted (submitted 15 September 2026; information request 6 October, answered 13 October 2026; advice awaited) | Open — decision pending (prior consultation) |
| PRR-CS-LAUNCH-01 | DPIA-CS-LAUNCH-01; EVP-2026-0048; RoPA-CS-001 | Head of Credit Decisions | Critical → High (inherited from DPIA-CS-INFER-01) | Significant | As PRR-CS-INFER-01; product-layer controls | Pending — Chief Risk Officer; launch planned 1 February 2027 | Covered by the same consultation | Open — decision pending (prior consultation) |
| PRR-LLM-01 | DPIA-LLM-01; TIA-LLM-01; EVP-2026-0029; EVP-2026-0030; RoPA-LLM-01; vendor assessment of Example AI Provider Inc. (Document 17) | Head of Customer Service | High → Medium (target: Medium — S1 remains Medium × Significant; the planned automated fee checks lower the likelihood of S2) | Moderate | Modify likelihood (masking, fail-closed special-category detector, agent review, QA sampling; planned automated checks); avoid for special-category content (excluded from the AI path) | Head of Customer Service, 25 June 2026; Group DPO advice partly followed (QA sample 3% instead of 5%), reasons recorded | G-36 evaluated — not met; G-TIA Art. 46 — pass of 22 June 2026 (historical); current status at 26 October 2026: incomplete — HOLD; AI path suspended, customer service human-only | Suspended — G-TIA hold (26 October 2026); the conditional acceptance of 25 June 2026 is not in effect until a current G-TIA pass is recorded |
| PRR-PSI-01 | DPIA-PSI-01; TIA-PSI-01; EVP-2026-0018; EVP-2026-0016; RoPA-PSI-01; partner due diligence (Document 17) | Head of Fraud Prevention | High → High (target: Medium, once transliteration and list-quality controls are tested; Low is not reachable while S1 severity is Significant) | Moderate | Avoid (mutual-output design stopped); modify likelihood (one-sided design without any output to the partner, analyst review); retention of the residual risk only by the decision after the consultation step | Pending — Chief Risk Officer after the consultation step (historical: Head of Fraud Prevention, 25 March 2026, Medium accepted with conditions — superseded 26 October 2026) | G-36 re-evaluated — met (Legal & Compliance, 26 October 2026; Group DPO advice followed); HBDI to be consulted before any further session (submission planned); G-TIA Art. 46 — fail for the mutual-output design (suspended 12 February 2026), pass for the one-sided design without output to the partner (20 March 2026; conditional on the independent protocol review, input padding and no result-dependent signal to the partner) | Open — decision pending (prior consultation); sessions paused since 26 October 2026 |
| PRR-CLOUD-01 | TIA-CLOUD-01 (Document 18 calculation requested by Document 20); EVP-2026-0008; RoPA-CLOUD-01; vendor assessment of Example Cloud Services Pvt Ltd (Document 17) | CIO | Medium → Medium (target: Medium) | Moderate | Avoid (no clear-text access from India); modify likelihood (tokenisation, masking gateway) | CIO, 20 March 2026; Group DPO advice followed | No DPIA (triage record); G-TIA Art. 46 — pass for the restricted design (12 March 2026) | Accepted — conditional (expiry 20 March 2027) |
| PRR-FL-01 | DPIA-FL-01; EVP-2026-0041; RoPA-FL-01 (Document 21) | Head of Fraud Prevention | Medium → Medium (target: Medium) | Moderate | Modify likelihood (DP across all rounds, secure aggregation); share (Art. 26 arrangement — accountability not transferred) | Head of Fraud Prevention, 15 May 2026; Group DPO advice followed | G-36 evaluated — not met; Chapter V not engaged (intra-EU consortium; conclusion re-checked on membership change); Art. 10 not engaged on the specified training inputs (G-L boundary recorded 26 October 2026) — any extension of labels or features triggers re-assessment | Accepted — conditional (expiry 15 May 2027) |

All conditional acceptances above that were decided before 23 October 2026 (the date on which Document 8, version 3.0, took effect) are re-assessed at expiry under Document 8, version 3.0, with the Chief Privacy Officer's concurrence for a Medium tier. PRR-PSI-01 is no longer among them: it was re-assessed on 26 October 2026 after a review correction (the Art. 10 severity modifier of Document 18 had been omitted), and its conditional acceptance of 25 March 2026 is superseded.

## **Fully Expanded Record — PRR-CS-INFER-01**

| Record Field | Value |
| :---- | :---- |
| Risk Identifier | PRR-CS-INFER-01; ERM record in the "Conduct & Privacy Risk" category; operational-risk event type "clients, products and business practices" |
| Processing Activity | RoPA-CS-003 — automated decisions on retail credit applications (planned production design; not yet running at 26 October 2026; launch planned 1 February 2027, not before the consultation step and the decision) |
| Risk Source and Links | DPIA-CS-INFER-01 (Document 19); calculation Document 18, Project 4, Example 4.3; evidence pack EVP-2026-0047 |
| Vendor-Assessment Source | EuroCredit Bureau (independent controller; data-sharing agreement) — assessment under Document 17 current; data quality of bureau input is a control under factor L3 |
| Harm Scenarios | S1 — systematic adverse or discriminatory automated credit decisions, including through corrupted bureau data (discrimination/adverse automated decision, financial loss, exclusion) — determines the tier. S2 — loss of confidentiality of application and bureau data (Medium). S3 — re-use for marketing: prevented by G-L |
| Inherent Risk (track (a)) | Critical (S1: Near-certain × Catastrophic) |
| Residual Risk (track (a)) | High (S1: Medium × Catastrophic) |
| Target Risk and Date | High — the residual risk of S1 cannot be reduced further without giving up automated decisions; measures keep the likelihood at Medium |
| Track (b) Level | Significant (applicable regime, financial and reputational consequences) — reported to ERM; does not change track (a) |
| Treatment Option | Modify likelihood: pre-deployment bias testing, independent validation, quarterly fairness and drift monitoring with alert thresholds, pre-effect decision by a credit officer in the borderline score band (Art. 22(2)(a) necessity record, Document 19), human review on request, bureau data-quality controls; retention of the residual risk subject to the decision after the consultation |
| Risk Owner | Head of Credit Decisions (Processing Owner) |
| Decision and Single Decider | Pending. Decider: the Chief Risk Officer (Document 8, version 3.0, Section 5), within 5 business days after the G-36 step is complete |
| Conditions and Expiry | To be set in the decision; expected conditions: implementation of any HBDI written advice; quarterly fairness monitoring; re-assessment upon any material model update and at the latest 12 months after launch |
| DPO Advice | Group DPO advice of 9 September 2026 (test met; consult before launch; explanation text and fairness alert threshold) — followed in full |
| G-36 Status | Evaluated. Legal & Compliance, 10 September 2026, with Group DPO advice: test met. Prior consultation with the HBDI submitted 15 September 2026; information request 6 October 2026, answered 13 October 2026 (period suspended until receipt); written advice awaited; period running. Production processing does not start before the consultation step is complete. A lapse of the period or the absence of comments will be recorded as such and is not an authorisation |
| G-TIA Status | Not applicable — no transfer outside the EEA |
| Status | Open — decision pending (prior consultation) |
| Next Review Date | On receipt of the HBDI's advice |
| Change History | 4 September 2026 — record created from DPIA-CS-INFER-01 (inherent Critical, residual High). 15 September 2026 — prior consultation submitted. 6 and 13 October 2026 — HBDI information request and answer. 23 October 2026 — Supervisory Board Risk Committee informed |

## **Fully Expanded Record — PRR-PSI-01**

| Record Field | Value |
| :---- | :---- |
| Risk Identifier | PRR-PSI-01; ERM record in the "Conduct & Privacy Risk" category; operational-risk event type "clients, products and business practices" |
| Processing Activity | RoPA-PSI-01 — anti-fraud matching of shared customers with a partner bank in India |
| Risk Source and Links | DPIA-PSI-01 (Document 19; evidence pack EVP-2026-0018); TIA-PSI-01 (Document 20; evidence packs EVP-2026-0005 and EVP-2026-0016); calculation Document 18, Project 4 |
| Vendor-Assessment Source | Partner-bank due diligence under Document 17 (independent controller; SCC Module 1); no open non-conformities at 20 March 2026 |
| Harm Scenarios | S1 — wrongful match leading to adverse action against a customer (adverse decision, financial loss, exclusion); a match links the customer to confirmed fraud, a criminal offence, so the data concerned are criminal-offence data (Art. 10) — determines the tier. S2 — disclosure of customer relationships to the partner or in the destination country: Low after the one-sided redesign without any output to the partner — the partner observes only the padded input bound and the fact of the session, not the intersection or its size, so a crafted or compelled list yields nothing (illustrative security assumptions and independent protocol review: TIA-PSI-01) |
| Inherent Risk (track (a)) | High (S1: Near-certain × Significant; S2: High × Moderate = Medium). Re-assessed 26 October 2026; the former inherent Medium (S1 Near-certain × Moderate) omitted the Art. 10 severity modifier |
| Residual Risk (track (a)) | High (S1: High × Significant — severity Restricted 3 + criminal-offence data 2 + scale 1 + aggregation 1 + provenance 1 = 8). Re-assessed 26 October 2026; the former residual Medium (S1 severity 6, Moderate) is superseded |
| Target Risk and Date | Medium, once transliteration rules and partner list-quality controls are tested (S1 factor L3 from 1 to 0: likelihood index 6 → Medium; Medium × Significant = Medium); Low is not reachable while S1 severity is Significant. Target date to be set in the Chief Risk Officer's decision |
| Track (b) Level | Moderate |
| Treatment Option | Avoid: the mutual-output design was stopped. Modify likelihood: one-sided output, blinding with a key held in the EEA, analyst review before any action, transliteration rules. Retention of the residual High only by the Chief Risk Officer's decision after the prior-consultation step; until then the sessions are paused |
| Risk Owner | Head of Fraud Prevention (Processing Owner) |
| Decision and Single Decider | Pending. Decider: the Chief Risk Officer (Document 8, version 3.0, Section 5), within 5 business days after the G-36 step (prior consultation of the HBDI) is complete. Historical: Head of Fraud Prevention, 25 March 2026, under Document 8, version 1.0 (before the Chief Privacy Officer position existed): Medium accepted with conditions — superseded on 26 October 2026; no longer a current acceptance |
| Conditions and Expiry | To be set in the decision. The controls of the superseded acceptance remain in force as conditions of the design: analyst review before any action on a match; no match results sent to the partner; key held only in the EEA; G-TIA remains passed. The expiry of 25 March 2027 lapsed with the superseded acceptance |
| DPO Advice | Group DPO advice of 9 February 2026 (suspend the mutual-output sessions), 18 March 2026 (TIA-PSI-01: support for the one-sided design; document the protocol review; test transliteration rules) and 23 March 2026 (DPIA-PSI-01) — followed. Advice of 26 October 2026 on the re-assessment (G-36 test met; consult the HBDI before any further session; pause the sessions) — followed |
| G-36 Status | Re-evaluated. Legal & Compliance (General Counsel), 26 October 2026, with Group DPO advice: test met — S1 high risk remains after the analyst-review measure (residual likelihood High; near misses from name transliteration), the harm attaches to being linked to a criminal offence, and the further measures that would lower the likelihood are not yet tested. Prior consultation of the HBDI before any further session; submission to be decided by the Chief Risk Officer (planned). A lapse of the Art. 36(2) period or the absence of comments will not be treated as an authorisation. Historical: 24 March 2026 — test not met, on the calculation without the Art. 10 modifier; superseded |
| G-TIA Status | Art. 46 (SCC Module 1). Fail for the mutual-output design (10 February 2026) — sessions suspended under SCC Clause 14(f) on 12 February 2026. Pass for the one-sided design (20 March 2026), on the stated illustrative assumptions and residual leakage, on condition that the partner-input controls are enforced and of re-evaluation within 12 months |
| Status | Open — decision pending (prior consultation); sessions paused since 26 October 2026 |
| Next Review Date | On receipt of the HBDI's advice; TIA re-evaluation by 20 March 2027 (planned) |
| Change History | 10 February 2026 — G-TIA failed for the mutual-output design; record status "Suspended" from 12 February 2026. 20 March 2026 — G-TIA passed for the one-sided design. 25 March 2026 — DPIA-PSI-01 completed; residual risk accepted with conditions at the former Medium tier (superseded on 26 October 2026); status "Accepted — conditional". 1 April 2026 — sessions resumed under the one-sided design. 26 October 2026 — re-assessment triggered by a review correction (the Art. 10 severity modifier of Document 18 had been omitted): inherent and residual High; G-36 re-evaluated — met; the acceptance of 25 March 2026 superseded; sessions paused by the Head of Fraud Prevention; status "Open — decision pending (prior consultation)". Planned: the Chief Risk Officer's decision on the submission to the HBDI; information of the Supervisory Board Risk Committee; the next monthly session is not held |

# **Normative Basis and References**

* Regulation (EU) 2016/679 (GDPR): Arts. 5(2), 24, 33(5), 35, 36, 44–46; Recitals 75–77, 84.
* ISO 31000:2018, *Risk management — Guidelines*, and ISO/IEC 27557:2022, *Organizational privacy risk management* — bibliographic pointers only; no clause-level conformity is claimed.
* NIST, NISTIR 8062, *An Introduction to Privacy Engineering and Risk Management in Federal Systems* (January 2017).
* Article 29 Working Party, Guidelines on Data Protection Impact Assessment (WP248 rev.01).
* EDPB Recommendations 01/2020 on supplementary measures, version 2.0 (for G-TIA status).

# **Document History (PGF)**

| Release | Date | Changes |
| :---- | :---- | :---- |
| 1.0.0-rc.1 | 2026-10-26 | Canonical English Markdown; changes from internal ver.2: record extended with inherent, residual and target risk, treatment option (ISO 31000 concepts, bibliographic only), track (b) level reported separately, risk owner as the first-line Processing Owner, single decider, conditional acceptance with expiry, DPO advice and response, G-36 status (evaluated / met / consultation dates / supervisory-authority response), G-TIA status, DPIA/TIA/evidence-pack links and vendor-assessment source (Document 17); status taxonomy revised ("Open — decision pending", "In treatment", "Accepted — conditional (expiry)", "Accepted", "Not accepted — stopped or redesign", "Suspended", "Closed"); G-L failures and failed G-TIA outcomes excluded from acceptance; risk sources widened (vendor assessments, complaints and rights trends, supervisory-authority inquiries, regulatory change); ERM linkage aligned with ISO 31000 concepts, operational-risk mapping and no netting of track (a); calqued board terminology and DPO approval roles removed (DPO consulted; decisions per Document 8; Supervisory Board Risk Committee informed); Part B register recomputed from Documents 18–20: PRR-CS-TRAIN-01 Medium conditionally accepted; PRR-CS-INFER-01 and PRR-CS-LAUNCH-01 High pending the HBDI prior consultation and the Chief Risk Officer's decision; PRR-LLM-01 (replaces the two former records for the real-vendor case), PRR-PSI-01 (owner Head of Fraud Prevention, anti-fraud; review correction of 26 October 2026: re-assessed High with the Art. 10 severity modifier, G-36 met, Chief Risk Officer decision pending, sessions paused), PRR-CLOUD-01 (owner CIO) and PRR-FL-01 added or recomputed; two fully expanded records; cut-off for the earlier authority rules set at 23 October 2026 (Document 8, version 3.0, effective date); PSI residual leakage and LLM pending US-law verification shown; evidence packs in EVP-YYYY-NNNN format; example dates shifted by −12 months and fictional history re-baselined (version 2.0 of 20 October 2026); calqued terms replaced; references added |
| 1.0.0-rc.2 | 2026-10-28 | Author-approved publication direction; named PAMOLA implementation examples with tool-neutral templates; direct integrated-score mapping without automatic per-metric risk-tier overrides; observations, DPO dissent and the authorised business decision recorded separately from legal/release conditions. |
| 1.0.0 | 2026-10-28 | First publication package; substantive method unchanged from the rc.2 freeze; rights holder REALM INVEO confirmed and documentation licence CC BY 4.0 issued. |
