---
title: "Privacy Risk Appetite Statement"
document_id: PGF-08
level: 1
release_version: 1.0.0-rc.1
status: release-candidate
authors: ["Alexey Neyman", "Val Khvatov"]
regulatory_reference_date: 2026-10-26
licence_proposed: "CC BY 4.0 (proposed; subject to rights-holder confirmation)"
source_provenance: "Derived from internal source set ver.2: Level1/8. Privacy_Risk_Appetite_Statement_Template and Example_ENG.docx.md; sha256 eaa0995c90a731383863e0aa34aada81d9c0266ddb7f0252d586ca33ab821ca6"
---

# PGF-08 — Privacy Risk Appetite Statement

*Privacy Governance Framework (PGF) · Level 1 — Strategic Documents · Release 1.0.0-rc.1 · Regulatory reference date: 26 October 2026*

> **Status and use.** Part A is a reusable template. Part B is a worked example for a fictional organisation (PanEuropean Bank AG); all names, figures, dates and records in Part B are illustrative. Nothing in this document is legal advice or a statement about any real organisation, product or provider.

# **About This Document**

**Purpose.** Document 8 sets the boundaries of acceptable privacy risk: the likelihood, severity and residual-risk tiers, the residual-risk matrix, who may accept a residual risk of each tier, and when the DPO's advice and further escalation are mandatory. It turns the result of the Privacy Risk Assessment Methodology (Document 18) into a decision rule.

**Scope.** The appetite applies only to processing that has passed the legal compliance gate (G-L). Risk appetite does not decide lawfulness, does not replace the statutory prior-consultation test (G-36) and does not override the transfer-equivalence test (G-TIA). Organisational consequences are a separate track and never offset risk to the rights and freedoms of individuals.

**Relationships.** Document 18 calculates the tiers; Document 19 (DPIA) and Document 20 (TIA) apply them; Document 5 (RACI) and Document 6 (Privacy Role Competency Framework) reuse the tiers and authorities; Document 22 (Privacy Risk Register) records decisions; Document 14 (Data Breach Response Policy) owns breach notification tests; Document 3 (Interface & Integration Model) links the appetite to enterprise risk management; Document 31 (Governance Reporting Template) reports to the Governing Body.

# **How to Use This Document**

Part A is a template. Text in ***[square brackets, bold italic]*** is a placeholder. Blocks marked **Guidance** are removed from the adopted version. Part B shows the template completed for the fictional PanEuropean Bank AG.

> **Guidance.** This document is the single source of the residual-risk tiers (Low / Medium / High / Critical) and of the acceptance authority that the Privacy Governance Charter (Document 2), the RACI Matrix (Document 5, Section 7) and the Privacy Role Competency Framework (Document 6) rely on. Do not introduce an alternative scale. The acceptance authority must match Section 5 of this document verbatim in those documents.

# **Table of Contents**

**About This Document**
**How to Use This Document**
**Part A — Template**
Glossary of Terms
1. Purpose of This Document
2. Principles for Constructing Risk Appetite
3. Risk Appetite Statement
4. Likelihood, Severity and Residual-Risk Tiers
5. Acceptance Authority, Escalation and Mandatory DPO Advice
6. Relationship to Other Framework Documents
7. Review and Amendment
8. Approval
**Part B — Worked Example: PanEuropean Bank AG**
Glossary of Terms
1. Purpose of This Document
2. Principles for Constructing Risk Appetite
3. Risk Appetite Statement
4. Likelihood, Severity and Residual-Risk Tiers
5. Acceptance Authority, Escalation and Mandatory DPO Advice
6. Relationship to Other Framework Documents
7. Review and Amendment
8. Approval
**Normative Basis and References**
**Document History (PGF)**

# **Part A — Template**

**Privacy Risk Appetite Statement *[Legal name of the organisation]***

Effective date: ***[DD Month YYYY]***   ·   Version: ***[x.x]***   ·   Document owner: ***[Executive Privacy Programme Owner (EPPO)]***   ·   Adopted by: ***[Executive Management]***   ·   ***[Governing Body consent, where its rules reserve it]***

***Version History***

| Version | Date | Changes |
| :---- | :---- | :---- |
| ***[1.0]*** | ***[DD.MM.YYYY]*** | ***[First version of the document]*** |
| ***[x.x]*** | ***[DD.MM.YYYY]*** | ***[Brief description of material changes]*** |

> **Guidance.** Record only material changes — in particular, changes to the matrix, to the acceptance authority, to the cumulative disclosure budget, or a change in enterprise-wide risk appetite that requires recalculating the limit for the privacy category.

## **Glossary of Terms**

*This table lists only terms defined by this document itself; terms defined in another PGF document are not repeated here.*

| Term | Definition / Reference |
| :---- | :---- |
| Privacy Risk Appetite | The amount and type of privacy risk the organisation is willing to accept in pursuit of its objectives, expressed through the residual-risk tiers, the acceptance authority (Section 5) and any quantitative limits (Section 3). Set top-down by ***[Executive Management]***, under the oversight of ***[the Governing Body]***. |
| Risk tolerance / limit | The operational boundary derived from the appetite for a specific tier, process or population — for example, the delegated tier up to which a Processing Owner may accept residual risk, or the cumulative disclosure budget (Section 3). |
| Track (a) / track (b) | Track (a): risk to the rights and freedoms of individuals. Track (b): organisational consequences (regulatory, financial, reputational, operational). Defined in Document 18, Section 3.1. Track (b) never offsets track (a). |
| Residual-risk tier | Low, Medium, High or Critical — the track (a) result after the organisation's measures, obtained through the matrix of Section 4 for each harm scenario; the highest scenario tier is the tier of the processing. |
| Cumulative disclosure budget | An optional limit on the total privacy loss (for differentially private releases, in ε and δ) or on the total disclosure (for other releases) that the organisation accepts per source population over the lifetime of that population's ledger, without calendar reset; it may be complemented by an operational cap on new spending per period (Section 3). |

## **1. Purpose of This Document**

This document establishes the boundaries of acceptable privacy risk at ***[organisation name]***: which residual tier may be accepted, by whom and with which mandatory steps; which tier is never accepted; and when the DPO's advice and further escalation are required. It does not describe how risk is calculated (Document 18), and it does not decide whether processing is lawful (G-L, owned by ***[Legal]***).

> **Guidance.** Risk appetite is not about reducing risk to zero: decisions on lawful processing weigh residual risk against the purpose the processing serves. This document makes that weighing predictable and auditable. It never makes unlawful processing acceptable.

## **2. Principles for Constructing Risk Appetite**

> **Guidance.** Without explicit principles, risk appetite turns either into a declaration that "privacy risk is unacceptable" (which paralyses processing) or into thresholds disconnected from the organisation's actual distribution of authority.

* ***[Principle of lawfulness first — the legal compliance gate (G-L) runs before any risk decision: lawful basis (Art. 6); condition for special-category data (Art. 9) or criminal-offence data (Art. 10); purpose compatibility (Art. 6(4)); transparency deliverable (Arts. 13/14); Art. 22 permissibility and safeguards; valid transfer tool and TIA outcome (Chapter V); mandatory deadlines and statutory duties. Failure means stop or redesign. No risk appetite, risk acceptance, DPO opinion or metric can cure a G-L failure.]***

* ***[Principle of the probabilistic nature of risk — risk is expressed per harm scenario as a combination of likelihood and severity of harm to individuals (Document 18), not as a binary "acceptable/unacceptable".]***

* ***[Principle of severity-led calibration — a lower likelihood never reduces the residual tier of a Catastrophic scenario below High, nor of a Significant scenario below Medium. Any relaxation of a matrix cell requires independent evidence (for example, validated loss-event data or an independent model validation), never the metrics of a particular tool, and is decided by ***[Executive Management]***.]***

* ***[Principle of two tracks — organisational consequences (track (b)) are reported to enterprise risk management separately and never lower, offset or average the rights-and-freedoms tier (track (a)).]***

* ***[Principle of top-down appetite with bottom-up monitoring — the appetite and its limits are set top-down by ***[Executive Management]*** within the enterprise-wide risk appetite and under ***[Governing Body]*** oversight; individual decisions are aggregated bottom-up in the Privacy Risk Register (Document 22) and reported against those limits (Document 3, Section 3.1; Document 31).]***

* ***[Principle of proportionality between authority and tier — the right to accept residual risk is assigned to roles with sufficient authority and qualification for the tier (Document 6); each decision record names one effective decider. The DPO advises; the DPO never accepts risk, authorises processing or holds a veto.]***

* ***[Principle of alignment with enterprise-wide risk appetite — the privacy risk appetite refines, and may not contradict, the enterprise-wide risk appetite (Document 3, Section 3.1).]***

* ***[Principle of accounting for special categories — special categories of personal data are an input to severity (Document 18, Factor B) and a G-L condition (Art. 9(2)); they also trigger mandatory DPO advice (Section 5).]***

## **3. Risk Appetite Statement**

> **Guidance.** The statement is short and declarative. It is adopted by Executive Management; where the Governing Body's rules reserve its consent for the statement, that consent is obtained and recorded. The Governing Body oversees and receives reporting; it does not take operational acceptance decisions.

***[Executive Management] of [organisation name]*** adopts the following privacy risk appetite, within the enterprise-wide risk appetite:

* ***[Unlawful processing is outside appetite. Processing that fails the legal compliance gate (G-L) is stopped or redesigned; it is never accepted at any tier.]***

* ***[Critical residual risk to the rights and freedoms of individuals is not acceptable (zero tolerance). Processing is stopped or redesigned; there is no acceptance channel for Critical.]***

* ***[High residual risk is accepted only by one designated member of Executive Management (or by the Privacy Risk Committee where a written delegation designates it), after the prior-consultation test (G-36) has been evaluated and, where it is met, after consultation of the competent supervisory authority; with the DPO's advice recorded and the Governing Body committee informed.]***

* ***[Medium and Low residual risk may be accepted within the authority delegated under Section 5, provided that the aggregate privacy risk stays within the limit for the privacy category in the enterprise-wide risk appetite.]***

* ***[Optional parameter — cumulative disclosure budget: for each source population ([population]) and privacy unit ([privacy unit]), the lifetime cumulative privacy loss of all differentially private releases and trainings whose outputs have been released or observed does not exceed ε = [X] and δ = [Y], composed with [basic composition / a compatible accountant] (Document 18, Section 3.3.6). Released outputs stay in the composition permanently; there is no calendar reset. [Optional operational cap: new spending does not exceed ε = [Z] per [calendar year] — an internal pacing rule that never replaces the lifetime limit.] For non-DP releases from the same population, each new release requires a composition and linkage assessment. The budget is a risk limit, not evidence of anonymity.]***

This statement is reviewed with the frequency established in Section 7 and may not be relaxed by any role below ***[Executive Management]***.

## **4. Likelihood, Severity and Residual-Risk Tiers**

> **Guidance.** This document does not describe how likelihood or severity is calculated — that is Document 18. This section fixes the tiers, their conceptual content and how they combine. It also maps the internal tiers to the GDPR risk thresholds, which are legal tests and remain separate from the tiers.

***Likelihood Scale***

Likelihood is assessed per harm scenario by Document 18. For processing of identified or identifiable data (including pseudonymised data), it reflects threat sources, exposure, the effectiveness of controls and event history (Document 18, Section 3.2). For a de-identified, synthetic, aggregate or federated release, the likelihood of the disclosure scenario is taken from the PET Assessment Module (Document 18, Section 3.3), whose disclosure indicator is not a probability and whose failure gates prevail over any average. This document does not set the numerical thresholds.

| Tier | Conceptual Description |
| :---- | :---- |
| ***[Low]*** | ***[Identified processing: limited exposure, no capable threat source, measures implemented and tested. Release: the PET Assessment Module passes all gates with a low disclosure indicator]*** |
| ***[Medium]*** | ***[Identified processing: routine or systematic exposure or a known error mode, mitigated by tested measures. Release: the module passes all gates, but some metrics are close to their thresholds]*** |
| ***[High]*** | ***[Identified processing: a capable threat source or known weaknesses in the measures. Release: the module fails a gate (the release is not made in its current form)]*** |
| ***[Near-certain]*** | ***[Identified processing: systematic exposure to a capable source with absent or ineffective measures, or repeated events. Release: an attack has been reproduced against the artefact]*** |

***Severity Scale (track (a) — harm to individuals)***

Severity is assessed by Document 18 per harm scenario, from the harm type, the data class and special categories, the vulnerability of the persons affected, the scale, the reach of the data or effect, the involvement of an automated decision with significant effect, and the reasonable expectations of the persons concerned. Consent or another lawful basis is checked by G-L; it is not a severity factor.

| Tier | Conceptual Description |
| :---- | :---- |
| ***[Minor]*** | ***[An inconvenience for the person that is easily remedied, with no lasting harm]*** |
| ***[Moderate]*** | ***[Limited, reversible harm to the person]*** |
| ***[Significant]*** | ***[Real, tangible harm to the person — e.g. a discriminatory or erroneous decision, disclosure of sensitive information, financial loss]*** |
| ***[Catastrophic]*** | ***[Severe, potentially irreversible harm — e.g. systemic discrimination, exclusion from essential services, irreversible public disclosure of special-category data, risk to physical safety]*** |

***Organisational Consequence Scale (track (b) — reported separately)***

| Tier | Conceptual Description |
| :---- | :---- |
| ***[Minor]*** | ***[No measurable effect on the organisation]*** |
| ***[Moderate]*** | ***[Low-level, measurable regulatory, financial or reputational effect]*** |
| ***[Significant]*** | ***[Material regulatory, financial or reputational consequences]*** |
| ***[Catastrophic]*** | ***[Consequences threatening the organisation's licence, operations or continued existence]*** |

Track (b) levels are reported to enterprise risk management (Document 3, Section 3.1) and to the Governing Body (Document 31). They do not enter the matrix below.

***Residual-Risk Tier Matrix (track (a))***

| Severity \\ Likelihood | Low | Medium | High | Near-certain |
| :---- | :---- | :---- | :---- | :---- |
| **Minor** | ***[Low]*** | ***[Low]*** | ***[Low]*** | ***[Low]*** |
| **Moderate** | ***[Low]*** | ***[Low]*** | ***[Medium]*** | ***[Medium]*** |
| **Significant** | ***[Medium]*** | ***[Medium]*** | ***[High]*** | ***[High]*** |
| **Catastrophic** | ***[High]*** | ***[High]*** | ***[Critical]*** | ***[Critical]*** |

> **Guidance.** The matrix is severity-led: in the Catastrophic row no cell is below High, and in the Significant row no cell is below Medium. An organisation may make its matrix stricter. It may relax a cell only where the cell remains within these floors and the relaxation is justified by independent evidence and decided by Executive Management. The tiers must match those used in Document 5, Section 7, and Document 6; renaming them requires revising both documents.

***Rationale for Matrix Cell Calibration***

Every cell whose tier is not the template value, and every cell the organisation considers a substantive appetite decision, is recorded with the rationale and the evidence relied on. If no cell departs from the template, this is stated explicitly.

| Matrix Cell (Severity × Likelihood) | Assigned Tier | Rationale and Independent Evidence |
| :---- | :---- | :---- |
| ***[Severity] × [Likelihood]*** | ***[Tier]*** | ***[Reason for the tier, with reference to the independent evidence or decision]*** |

> **Guidance.** Keep the rationale record as a separate, auditable artefact. The same principle applies to the severity-weight corridor and to the PET-module thresholds within a Risk Calculation Project (Document 18).

***Mapping of Internal Tiers to GDPR Thresholds***

The GDPR thresholds are legal tests. The internal tiers are indicators that feed those tests; they never replace them.

| GDPR notion | Legal test | Relationship to internal tiers | Owner |
| :---- | :---- | :---- | :---- |
| DPIA required (Art. 35(1), (3), (4)) | "Likely to result in a high risk"; the Art. 35(3) cases; supervisory-authority lists; two or more of the nine WP248 rev.01 criteria → presumption | Triage (G-DPIA) runs independently of any tier. An inherent High or Critical tier is an additional indicator that a DPIA is required | ***[Processing Owner; Document 19]*** |
| DPO advice on a DPIA (Art. 35(2)) | Required on every DPIA | Independent of the tier | ***[Processing Owner seeks it]*** |
| Prior consultation (Art. 36(1)) — G-36 | High risk to rights and freedoms would remain in the absence of further mitigating measures | Evaluated for every DPIA, irrespective of the tier. A residual High or Critical tier is a strong indicator that the test is met; the legal conclusion is recorded separately with reasons. Where met, the supervisory authority is consulted before processing starts | ***[Legal records the conclusion, with DPO advice]*** |
| Personal data breach notification (Arts. 33–34) | Supervisory authority: unless the breach is unlikely to result in a risk; individuals: high risk | Document 14 owns these tests; every breach is recorded (Art. 33(5)) whatever its tier. The severity scale may describe the harm, but no tier here decides notification | ***[Document 14]*** |
| DORA major ICT-related incident | Classification criteria of Commission Delegated Regulation (EU) 2024/1772 | Not mapped: separate track, separate owner (ICT risk function) and financial supervisor | ***[ICT risk function]*** |
| Transfer rules (Chapter V) — G-TIA | Branched by mechanism: Art. 45 adequacy — the decision covers the destination, sector and recipient and remains valid (monitored; no statutory duty to redo the Commission's assessment; any stricter internal review is internal policy); Art. 46 safeguards — TIA of the laws and practices of the destination with supplementary measures (C-311/18; EDPB Recommendations 01/2020, version 2.0, Step 2 and following); Art. 49 derogations — exceptional, conditions documented | Not mapped: tiers do not decide transfers. Under Art. 46, if essentially equivalent protection cannot be ensured, the transfer does not start or is suspended; appetite cannot override this. G-L and DPIA duties apply under every mechanism | ***[Document 20]*** |

## **5. Acceptance Authority, Escalation and Mandatory DPO Advice**

> **Guidance.** This section is the source referenced by the RACI Matrix (Document 5, Section 7). Reproduce tiers and rules verbatim there. The table shows the delegation rule; each actual decision record names exactly one effective decider selected under the delegation in force.

| Residual Tier (track (a), after G-L passed) | Who May Accept | Additional Mandatory Step | Decision Timeframe |
| :---- | :---- | :---- | :---- |
| ***[Low]*** | ***[Processing Owner]*** | ***[Record. DPO advice where a DPIA exists.]*** | ***[—]*** |
| ***[Medium]*** | ***[Processing Owner, with EPPO concurrence]*** | ***[DPO advice recorded. Conditional acceptance carries an expiry date and is re-assessed on expiry.]*** | ***[[X] business days]*** |
| ***[High]*** | ***[One named member of Executive Management, or the Privacy Risk Committee where a written delegation designates it. Each decision record names a single effective decider.]*** | ***[G-36 evaluated and recorded. Prior consultation whenever the Art. 36 test is met (a High tier is a strong indicator; any stricter routing is labelled internal policy). DPO advice recorded. Governing Body committee informed.]*** | ***[[X] business days after the G-36 step is complete]*** |
| ***[Critical]*** | ***[Not acceptable]*** | ***[Stop or redesign. If high risk remains after redesign, the G-36 test is evaluated and, where met, consultation precedes any processing. The decision sits with Executive Management. Reserved consent of the Governing Body applies only if its rules so provide.]*** | ***[Processing stopped or not started immediately; redesign decision within [X] business days]*** |

***Rules applying to all tiers:***

* ***[G-L first. The table applies only after G-L has passed. A G-L failure is never accepted.]***

* ***[Single decider. Each decision record names one effective decider under the delegation in force. Joint or alternative deciders are not used.]***

* ***[DPO advice. The DPO advises on every DPIA (Art. 35(2)) and in every case at Medium and above. Where the decider does not follow the DPO's advice, the decider records the reasons, and the DPO may escalate directly to the highest management level (Executive Management), informing the Governing Body committee if the DPO considers it necessary. The DPO does not approve, reject, veto or "prevail".]***

* ***[Prior consultation. The absence of comments from the supervisory authority, or the lapse of the Art. 36(2) period, is not an authorisation or a certificate of lawfulness. The authority may give written advice, request information (suspending the period) or use its Art. 58 powers, including a limitation or ban. G-L remains in force and the controller remains responsible.]***

* ***[Qualification. The authority to decide at a tier is held only by a person whose qualification for that tier is confirmed under Document 6; where it is not confirmed, the decision passes to the next level of the delegation. This rule does not apply to the DPO, whose position is protected by Art. 38(3).]***

* ***[Organisational consequences. Track (b) levels are reported to enterprise risk management; they never offset the track (a) tier or change who may accept it.]***

***Table of Mandatory DPO Advice and Escalation Triggers***

Regardless of the residual tier, the following conditions require the DPO's advice before the decision and, where stated, escalation. Multiple triggers in one case lead to a single combined DPO advice.

| Trigger | Triggering Condition | Required Step | Note |
| :---- | :---- | :---- | :---- |
| ***[PET-module failure]*** | ***[A mandatory metric fails, a known feasible attack succeeds, a prohibited attribute is present, or the cumulative disclosure budget would be exceeded (Document 18, Section 3.3.0)]*** | ***[The release is not made in its current form; the EPPO is informed; DPO advice on the redesign]*** | ***[No lenient mode applies to mandatory metrics; diagnostic metrics may be logged for audit (Document 27)]*** |
| ***[Automated decisions or high-risk AI]*** | ***[Processing involves a decision under Art. 22, or a high-risk AI system under applicable regulation]*** | ***[DPO advice regardless of the tier; Legal confirms Art. 22 permissibility and safeguards in G-L]*** | ***[AI Act obligations follow their own application dates and are recorded in the DPIA (Document 19)]*** |
| ***[Non-standard weighting]*** | ***[A severity weight outside the corridor set by Document 18]*** | ***[EPPO approval and DPO advice]*** | ***[Within the corridor, a written justification in the project passport suffices]*** |
| ***[Special categories]*** | ***[Special-category (Art. 9) or criminal-offence (Art. 10) data are processed]*** | ***[DPO advice regardless of the tier; Legal confirms the Art. 9(2)/Art. 10 condition in G-L]*** | ***[Applies even where the tier is Low]*** |
| ***[Anonymity conclusion]*** | ***[The controller intends to treat a released artefact as anonymous information]*** | ***[DPO advice; Legal assessment under Recital 26; periodic re-assessment]*** | ***[Metrics are evidence, not a legal safe harbour (Document 18, Section 3.3.0)]*** |

## **6. Relationship to Other Framework Documents**

This document:

* ***[Is aligned with the enterprise-wide risk appetite through the Interface & Integration Model (Document 3, Section 3.1) — the limit for the privacy risk category may not exceed the value approved at enterprise level.]***

* ***[Is applied by the Privacy Risk Assessment Methodology (Document 18) — Document 18 calculates likelihood, severity and the scenario tiers; this document fixes the scales, the matrix, the acceptance authority and the cumulative disclosure budget.]***

* ***[Serves as the decision checkpoint in the core process of the Privacy Governance Process Map (Document 24) — "Decision on the Acceptability of Residual Risk" — and in the RACI Matrix (Document 5, Section 5).]***

* ***[Is the source of the tiers and acceptance authority used in the RACI Matrix (Document 5, Section 7) and the Privacy Role Competency Framework (Document 6, Section 4).]***

* ***[Is applied in the DPIA Methodology (Document 19), including the G-36 step, and in the TIA Methodology (Document 20) only within the limits of G-TIA.]***

* ***[Provides the severity scale that the Data Breach Response Policy (Document 14) may use to describe incident severity; Document 14 owns the breach definitions and notification tests.]***

* ***[Is the source of the limits and authority used by the Privacy Risk Register (Document 22).]***

* ***[Is a criterion for the risk-based orientation of reviews under the Privacy Audit & Monitoring Programme (Document 27).]***

* ***[Is reflected in periodic reporting to the Governing Body through the Governance Reporting Template (Document 31).]***

> **Guidance.** If another PGF document contains tiers or acceptance rules that differ from this document, this is a synchronisation error, not an alternative version: this document prevails for tiers and authority; Document 18 prevails for the calculation method.

## **7. Review and Amendment**

This document is reviewed ***[at least once a year]*** under the Policy Review Cycle (Document 29), and immediately upon a change in the enterprise-wide risk appetite, a material change in regulatory requirements (Document 7), a change to Document 18 that affects the scales, or an incident that showed a mismatch between actual risk and the tiers. Changes are adopted by ***[Executive Management]*** on the proposal of the ***[EPPO]***, after consulting the ***[Privacy Risk Committee]*** and the DPO; ***[Governing Body consent is obtained where its rules reserve it]***. Responding to an incident in which the actual risk of an implemented decision exceeded its tier is a matter for Document 14 and Document 27; this document is revised only if the incident shows that the tiers or authorities themselves need to change.

## **8. Approval**

This document was adopted by ***[Executive Management]*** on ***[date]***. ***[Governing Body consent: [date], where reserved.]*** Document owner: ***[EPPO]***. DPO advice: ***[reference]***.

# **Part B — Worked Example: PanEuropean Bank AG**

**PanEuropean Bank AG — Privacy Risk Appetite Statement**

Effective date: 23 October 2026 (on the Supervisory Board's consent to Section 3)   ·   Version: 3.0   ·   Document owner: Chief Privacy Officer (EPPO)   ·   Adopted by: Management Board, 20 October 2026   ·   Supervisory Board consent to Section 3 (reserved consent matter): 23 October 2026

*A fictional legal entity, provided solely for illustrative purposes.*

***Fictional Document History (illustrative)***

| Version | Date | Changes |
| :---- | :---- | :---- |
| 1.0 | 1 March 2026 | First version: tiers, residual-risk matrix, acceptance authority by tier, mandatory DPO-advice triggers, mapping of internal tiers to GDPR thresholds. Owner at the time: Group DPO |
| 2.0 | 22 August 2026 | Added a cumulative disclosure budget for differentially private releases (Section 3); clarified the reporting of organisational consequences to the "Conduct & Privacy Risk" category of the enterprise risk appetite. Owner at the time: Group DPO |
| 3.0 | 20 October 2026 (effective 23 October 2026) | Re-baselined to the new role model on the creation of the Chief Privacy Officer (EPPO) position: Chief Privacy Officer as owner; Chief Privacy Officer concurrence for Medium; the Chief Risk Officer as single decider for High; Group DPO advice only; the cumulative disclosure budget restated as a lifetime ledger limit (ε and δ, no calendar reset) with an operational annual cap |

## **Glossary of Terms**

*This table lists only terms defined by this document itself; terms defined in another PGF document are not repeated here. The Part A glossary applies; the entries below add PanEuropean specifics.*

| Term | Definition / Reference |
| :---- | :---- |
| Privacy Risk Appetite | The appetite set by the Management Board for the "Conduct & Privacy Risk" category of PanEuropean's enterprise-wide risk appetite, expressed through the tiers, the acceptance authority and the cumulative disclosure budget of this document. |
| Privacy Risk Committee | A management-level committee chaired by the Chief Risk Officer (a Management Board member); the Chief Privacy Officer is a member and the Group DPO attends as a non-voting adviser. It is not a committee of the Supervisory Board. |
| Retail customer population | The source population of all retail customers of PanEuropean (about 1.2 million, illustrative), used for the cumulative disclosure budget. |

## **1. Purpose of This Document**

This document establishes the boundaries of acceptable privacy risk at PanEuropean Bank AG. Before it was adopted, decisions on residual risk for products such as scoring models, the anti-fraud system and cross-border support arrangements were made case by case, without common tiers. The document fixes the tiers and the acceptance authority used in PanEuropean's RACI Matrix (Document 5) and Privacy Role Competency Framework (Document 6), and it applies only after Legal & Compliance has passed the legal compliance gate (G-L).

## **2. Principles for Constructing Risk Appetite**

* Lawfulness first — no PanEuropean risk decision is taken on processing that has not passed G-L; for example, a proposal to share customer segments with an advertising partner on the strength of general terms and conditions was stopped at G-L and redesigned (Document 18, Example 4.2).

* Probabilistic nature of risk — risk is assessed per harm scenario; for example, for an anti-fraud transaction block, the likelihood of a false positive and its severity for the customer are assessed, not a "safe/unsafe" label.

* Severity-led calibration — PanEuropean adopts the template matrix without relaxation; no likelihood, however low, brings a Catastrophic scenario below High or a Significant scenario below Medium.

* Two tracks — consequences for PanEuropean (supervisory measures, fines, reputation, licence) are reported to the Chief Risk Officer's ERM function as track (b) and never lower the tier for customers.

* Top-down appetite with bottom-up monitoring — the Management Board sets the appetite for "Conduct & Privacy Risk" within the enterprise-wide risk appetite, with the Supervisory Board's consent to the statement in Section 3; accepted decisions are aggregated in the Privacy Risk Register (Document 22) and reported quarterly against the limits (Document 31).

* Proportionality between authority and tier — Processing Owners decide up to Medium within their delegation; the Chief Risk Officer decides High; each decision record names one decider. The Group DPO advises and may escalate directly to the Management Board; the Group DPO does not approve or accept risk.

* Alignment with the enterprise-wide risk appetite (Interface & Integration Model, Document 3, Section 3.1).

* Special categories — health data (payment protection insurance, PPI) and biometric data are inputs to severity, require an Art. 9(2) condition confirmed in G-L, and trigger mandatory Group DPO advice (Section 5).

## **3. Risk Appetite Statement**

The Management Board of PanEuropean Bank AG adopts the following privacy risk appetite within the "Conduct & Privacy Risk" category of the enterprise-wide risk appetite. Under the Supervisory Board's rules of procedure, this statement is a reserved consent matter (§111(4) sentence 2 AktG) — one of exactly three privacy matters reserved for the Supervisory Board's consent, together with the Privacy Governance Charter and the removal of the Group DPO (Document 2). Nothing else in this document requires Supervisory Board consent. The Supervisory Board's consent is recorded in Section 8.

* Unlawful processing is outside appetite: processing that fails G-L is stopped or redesigned and is never accepted.

* Critical residual risk to customers' or other individuals' rights and freedoms is not acceptable. The processing is stopped or redesigned.

* High residual risk is accepted only by the Chief Risk Officer, as the member of the Management Board designated by the Board's delegation, after the G-36 test has been evaluated and, where it is met, after consultation of the Hessian Commissioner for Data Protection and Freedom of Information (HBDI); with the Group DPO's advice recorded and the Supervisory Board's Risk Committee informed.

* Medium and Low residual risk may be accepted within the authority delegated under Section 5, provided that the aggregate privacy risk stays within the "Conduct & Privacy Risk" limit.

* Cumulative disclosure budget: for the retail customer population (privacy unit: one customer), the lifetime cumulative privacy loss of all differentially private releases and trainings whose outputs have been released or observed (including the federated anti-fraud consortium and synthetic training data) does not exceed ε = 10.0 and δ = 1×10⁻⁵, composed by basic composition unless the Privacy Operations Lead documents a tighter, compatible accountant. There is no calendar reset. As an internal pacing rule, new spending does not exceed ε = 7.0 per calendar year. Every non-DP release from the same population requires a composition and linkage assessment (Document 18, Section 3.3.6). The budget is a risk limit; it is not evidence of anonymity. The values ε = 10.0, δ = 1×10⁻⁵ and ε = 7.0 per year are illustrative internal appetite parameters, not legal thresholds.

This statement is reviewed under Section 7 and may not be relaxed by any role below the Management Board.

## **4. Likelihood, Severity and Residual-Risk Tiers**

PanEuropean's Privacy Risk Assessment Methodology (Document 18) calculates likelihood and severity per harm scenario. This section fixes the tiers and how they combine.

***Likelihood Scale***

| Tier | Conceptual Description and PanEuropean Example |
| :---- | :---- |
| Low | Limited exposure, no capable threat source, tested measures; or a release that passes all PET-module gates with a low disclosure indicator. Example: aggregate portfolio statistics passing all disclosure-control gates (Document 18, Example 3.1) |
| Medium | Routine or systematic exposure or a known error mode, mitigated by tested measures; or a release that passes all gates with some metrics close to their thresholds. Example: automated credit decisions with tested bias monitoring and human review (Document 18, Example 4.3) |
| High | A capable threat source or known weaknesses in the measures; or a release that fails a gate. Example: customer segments shared with an advertising partner whose due diligence has open non-conformities (Document 18, Example 4.2-R) |
| Near-certain | Systematic exposure to a capable source with absent or ineffective measures; or an attack reproduced against a release. Example: a synthetic dataset whose membership attack was reproduced in every test run (Document 18, Example 2.2) |

***Severity Scale (track (a))***

| Tier | Conceptual Description and PanEuropean Example |
| :---- | :---- |
| Minor | An easily remedied inconvenience — e.g. an irrelevant personalised offer |
| Moderate | Limited, reversible harm — e.g. the need for re-verification; unwanted onward use of marketing segments |
| Significant | Real harm — e.g. an unjustified credit refusal; disclosure of credit or health information about identifiable customers |
| Catastrophic | Severe, potentially irreversible harm — e.g. systemic discrimination in credit scoring affecting many customers; exclusion from essential banking services |

***Organisational Consequence Scale (track (b))***

| Tier | PanEuropean Example |
| :---- | :---- |
| Minor | No measurable effect |
| Moderate | A supervisory information request; limited remediation cost |
| Significant | A formal supervisory procedure or a fine; material media attention |
| Catastrophic | A threat to the banking licence or to the continuity of operations |

Track (b) levels are reported to the Chief Risk Officer's ERM function and in the quarterly governance report (Document 31). They do not enter the matrix.

***Residual-Risk Tier Matrix***

PanEuropean adopts the template matrix without relaxation.

| Severity \\ Likelihood | Low | Medium | High | Near-certain |
| :---- | :---- | :---- | :---- | :---- |
| **Minor** | Low | Low | Low | Low |
| **Moderate** | Low | Low | Medium | Medium |
| **Significant** | Medium | Medium | High | High |
| **Catastrophic** | High | High | Critical | Critical |

***Rationale for Matrix Cell Calibration***

| Matrix Cell (Severity × Likelihood) | Assigned Tier | Rationale and Independent Evidence |
| :---- | :---- | :---- |
| **Significant × Low** | Medium | Severity-led: harm of this kind to customers (e.g. an unjustified credit refusal) warrants Processing Owner acceptance with the Chief Privacy Officer's concurrence and Group DPO advice, however low the likelihood. No independent evidence would justify a lower tier at present; the cell is reviewed annually with the loss-event data held by the ERM function. |
| **Catastrophic × Low** | High | Severity-led, in line with the CNIL PIA approach that risks of maximum severity must be reduced whatever their likelihood: a scenario that could cause severe, irreversible harm always reaches the Management Board level and the G-36 evaluation. Low likelihood shown by the metrics of a particular tool is not accepted as a reason to relax this cell. |
| All other cells | Template value | No departure from the template |

***Worked examples (from Document 18)***

| Case | Likelihood | Severity | Tier | Decision path |
| :---- | :---- | :---- | :---- | :---- |
| New personalised-offers feature in Digital Banking, own app, granular consent (Document 18, Example 4.1) | Medium (threat-based) | Minor | Low | Processing Owner (Head of Digital Banking) records the decision; no DPIA, so Group DPO advice is not mandatory |
| Processing health data when reviewing a PPI application — G-L: Art. 9(2) condition confirmed by Legal & Compliance; DPIA performed | Low (tested access controls; limited circle of underwriters) | Significant (special-category data used to decide about the person — severity floor) | Medium | Processing Owner (Head of Insurance Distribution) with the Chief Privacy Officer's concurrence; Group DPO advice mandatory (special categories; DPIA); conditional acceptance with expiry; G-36 evaluated — test not met, reasons recorded |
| Production credit scoring (Document 18, Example 4.3; DPIA-CS-INFER-01 / DPIA-CS-LAUNCH-01) | Medium (residual) | Catastrophic (systemic discrimination scenario) | High | G-36: test met — HBDI consulted before the production launch; Chief Risk Officer decides after the consultation; Group DPO advice recorded; Supervisory Board Risk Committee informed |
| Synthetic training data for the scoring model (Document 18, Example 2.1-R; DPIA-CS-TRAIN-01) | Medium (PET module passed) | Significant | Medium | Under version 3.0: Head of Credit Decisions with the Chief Privacy Officer's concurrence; Group DPO advice; expiry after 12 months or at the next calibration. The original decision (before 20 October 2026) was taken by the Head of Credit Decisions with Group DPO advice under the version then in force and is re-assessed under version 3.0 at expiry |

***Mapping of Internal Tiers to GDPR Thresholds***

The Part A mapping applies. At PanEuropean: the competent supervisory authority for prior consultation is the lead supervisory authority, HBDI; BaFin and the ECB are financial supervisors and are not consulted under Art. 36; DORA incident classification and reporting are handled by the ICT risk function on a separate track; breach notification tests are applied under Document 14.

## **5. Acceptance Authority, Escalation and Mandatory DPO Advice**

| Residual Tier (track (a), after G-L passed) | Who May Accept | Additional Mandatory Step | Decision Timeframe |
| :---- | :---- | :---- | :---- |
| **Low** | Processing Owner | Record in the evidence pack. Group DPO advice where a DPIA exists. | — |
| **Medium** | Processing Owner, with the Chief Privacy Officer's concurrence | Group DPO advice recorded. Conditional acceptance carries an expiry date (default 12 months) and is re-assessed on expiry. | 3 business days |
| **High** | The Chief Risk Officer, as the Management Board member designated by the Board's written delegation (the Privacy Risk Committee does not decide; it prepares the case) | G-36 evaluated and recorded by Legal & Compliance; prior consultation of the HBDI whenever the Art. 36 test is met. Group DPO advice recorded. Supervisory Board Risk Committee informed. | 5 business days after the G-36 step is complete |
| **Critical** | Not acceptable | Stop or redesign. If high risk remains after redesign, the G-36 test is evaluated and, where met, consultation precedes any processing; the decision sits with the Management Board. This is not a Supervisory Board reserved consent matter; the Supervisory Board's Risk Committee is informed. | Processing stopped or not started immediately; redesign decision within 10 business days |

This table is the source for the escalation rules of PanEuropean's RACI Matrix (Document 5, Section 7) and for the Processing Owner profile in the Privacy Role Competency Framework (Document 6, Section 4); they are revised together with this table. A Processing Owner may decide at a tier only where the qualification for that tier is confirmed under Document 6; otherwise the decision passes to the next level of the delegation. Each decision record names one decider. Where the decider does not follow the Group DPO's advice, the decider records the reasons, and the Group DPO may escalate directly to the Management Board and inform the Supervisory Board's Risk Committee if the Group DPO considers it necessary. The lapse of the Art. 36(2) period, or the absence of comments from the HBDI, is not treated as an authorisation; G-L remains in force and PanEuropean remains responsible.

***Table of Mandatory Group DPO Advice and Escalation Triggers***

| Trigger | Triggering Condition | Required Step | Note |
| :---- | :---- | :---- | :---- |
| **PET-module failure** | A mandatory metric fails, an attack succeeds, a prohibited attribute is present, or the cumulative disclosure budget would be exceeded (Document 18) | The release is not made in its current form; the Chief Privacy Officer is informed; Group DPO advice on the redesign | Examples: Document 18, Examples 2.1, 2.2, 3.2, 3.3 |
| **Automated decisions or high-risk AI** | Credit decisions under Art. 22; the credit-scoring model as a high-risk AI system (AI Act, Annex III point 5(b); high-risk obligations apply from 2 December 2027) | Group DPO advice regardless of the tier; Legal & Compliance confirms Art. 22(2)(a) and the Art. 22(3) safeguards in G-L | Example: Document 18, Example 4.3 |
| **Non-standard weighting** | A severity weight outside the 0.5–2.0 corridor of Document 18 | Chief Privacy Officer approval and Group DPO advice | No current PanEuropean project uses a non-standard weight |
| **Special categories** | Health data (PPI), biometric data or other Art. 9/10 data | Group DPO advice regardless of the tier; Art. 9(2) condition confirmed in G-L | Applies even where the tier is Low |
| **Anonymity conclusion** | A released artefact is to be treated as anonymous information (e.g. open-data statistics) | Group DPO advice; Legal & Compliance assessment under Recital 26; annual re-assessment | Example: Document 18, Example 3.1 |

## **6. Relationship to Other Framework Documents**

* Aligned with PanEuropean's enterprise-wide risk appetite through the Interface & Integration Model (Document 3, Section 3.1) — the "Conduct & Privacy Risk" limit is not exceeded.

* Applied by PanEuropean's Privacy Risk Assessment Methodology (Document 18), which calculates the tiers for each scenario.

* Serves as the decision checkpoint in the core process of the Privacy Governance Process Map (Document 24) — "Decision on the Acceptability of Residual Risk" — and in the RACI Matrix (Document 5, Section 5).

* Source of the tiers and acceptance authority in the RACI Matrix (Document 5, Section 7) and the Privacy Role Competency Framework (Document 6, Section 4).

* Applied in the DPIA Methodology (Document 19), including the G-36 step, and in the TIA Methodology (Document 20) within the limits of G-TIA.

* Provides the severity scale that the Data Breach Response Policy (Document 14) may use to describe incident severity; Document 14 owns the notification tests.

* Source of the limits and authority for the Privacy Risk Register (Document 22).

* Taken into account by the Privacy Audit & Monitoring Programme (Document 27) when setting the frequency and depth of reviews.

* Decisions accumulate in the Privacy Risk Register (Document 22) and are reported quarterly, and ad hoc for High decisions, to the Supervisory Board's Risk Committee through the Governance Reporting Template (Document 31).

## **7. Review and Amendment**

This document is reviewed at least once a year under the Policy Review Cycle (Document 29), and immediately upon a change in the enterprise-wide risk appetite, a material change in regulatory requirements (Regulatory Applicability Matrix, Document 7) — for example, a change to the AI Act application timeline for scoring models — a change to Document 18 that affects the scales, or an incident that showed a mismatch between actual risk and the tiers. Changes are adopted by the Management Board on the proposal of the Chief Privacy Officer, after consulting the Privacy Risk Committee and the Group DPO; changes to Section 3 require the Supervisory Board's consent. Responding to an incident in which the actual risk of an implemented decision exceeded its tier is a matter for the Data Breach Response Policy (Document 14) and the Privacy Audit & Monitoring Programme (Document 27).

## **8. Approval**

Versions 1.0 (1 March 2026) and 2.0 (22 August 2026) were adopted by the Management Board with the Supervisory Board's consent to Section 3; the Group DPO was the document owner at that time. Version 3.0 was adopted by the Management Board on 20 October 2026, on the proposal of the Chief Privacy Officer (a position that exists from that date) and after consulting the Privacy Risk Committee and the Group DPO; it took effect on 23 October 2026, when the Supervisory Board gave its consent to Section 3. Document owner: Chief Privacy Officer. Group DPO advice is on file.

# **Normative Basis and References**

* Regulation (EU) 2016/679 (GDPR): Arts. 5(2), 6, 9, 10, 22, 24, 33, 34, 35, 36, 38, 39, 58; Recitals 75, 76, 84.
* Article 29 Working Party, Guidelines on Data Protection Impact Assessment (WP248 rev.01).
* Article 29 Working Party, Opinion 05/2014 on Anonymisation Techniques (WP216).
* CJEU, C-311/18, *Data Protection Commissioner v Facebook Ireland and Schrems* (transfer equivalence); EDPB Recommendations 01/2020 on supplementary measures.
* CJEU, C-453/21, *X-FAB Dresden* (DPO conflicts of interest assessed case by case).
* German Stock Corporation Act (AktG), §111 — supervision by the Supervisory Board; §111(4) sentence 2 — transactions subject to Supervisory Board consent.
* Regulation (EU) 2024/1689 (AI Act), as amended by the AI Omnibus: Annex III point 5(b).
* Regulation (EU) 2022/2554 (DORA) and Commission Delegated Regulation (EU) 2024/1772 (classification of ICT-related incidents) — separate track, not mapped.
* NIST, NISTIR 8062, *An Introduction to Privacy Engineering and Risk Management in Federal Systems* (January 2017).
* NIST SP 800-226, *Guidelines for Evaluating Differential Privacy Guarantees* (final, March 2025).
* CNIL, *Privacy Impact Assessment (PIA)* methodology.
* Financial Stability Board, *Principles for an Effective Risk Appetite Framework* (2013).
* ISO 31000:2018 and ISO/IEC 27557:2022 — bibliographic pointers only; no clause-level mapping is claimed.

# **Document History (PGF)**

| Release | Date | Changes |
| :---- | :---- | :---- |
| 1.0.0-rc.1 | 2026-10-26 | Canonical English Markdown; changes from internal ver.2: G-L made a precondition of any appetite decision; acceptance authority aligned with the PGF decision model (DPO advises and never approves; High decided by one designated member of Executive Management with the G-36 evaluation; Critical not acceptable — the former joint acceptance channel removed); mapping of internal tiers to GDPR thresholds (Arts. 35, 36, 33–34) added, with DORA and Chapter V kept separate; likelihood redefined per Document 18 (threat-based for identified processing; PET module for releases) instead of re-identification exposure only; organisational consequences separated as track (b); consent removed as a severity factor; Part B calibration made severity-led (Catastrophic × Low = High; Significant × Low = Medium) and the tool-metric justification removed; Low tier requires DPO advice where a DPIA exists; Supervisory Board limited to oversight, information and reserved consent (§111(4) AktG), decisions taken by the Management Board or its delegates; optional cumulative disclosure budget per source population added as a lifetime ε/δ ledger limit (no calendar reset) with an optional operational cap; transfer row of the GDPR mapping branched by mechanism (Arts. 45, 46, 49); Part B re-baselined as version 3.0 (adopted 20 October 2026, effective on Supervisory Board consent 23 October 2026) with earlier versions kept as fictional history; Section 3 identified as one of exactly three Supervisory Board reserved consent matters; "bottom-up aggregation" replaced by top-down appetite with bottom-up monitoring; worked examples moved from footnotes into the body and aligned with Document 18; example dates shifted by −12 months; calqued governance terms replaced by the PGF controlled vocabulary; references added |
