---
title: "DPIA Methodology and Template"
document_id: PGF-19
level: 2
release_version: 1.0.0-rc.1
status: release-candidate
authors: ["Alexey Neyman", "Val Khvatov"]
regulatory_reference_date: 2026-10-26
licence_proposed: "CC BY 4.0 (proposed; subject to rights-holder confirmation)"
source_provenance: "Derived from internal source set ver.2: Level2/19. DPIA-Methodology-and-Template_ENG.docx.md; sha256 d20a9144be300b1bf9f86b52b15c245fe0ac5bd03fa3163bee66f4b49fbc4ddd"
---

# PGF-19 — DPIA Methodology and Template

*Privacy Governance Framework (PGF) · Level 2 — Policies and Standards · Release 1.0.0-rc.1 · Regulatory reference date: 26 October 2026*

> **Status and use.** Part A is a reusable template. Part B is a worked example for a fictional organisation (PanEuropean Bank AG); all names, figures, dates and records in Part B are illustrative. Nothing in this document is legal advice or a statement about any real organisation, product or provider.

# **About This Document**

**Purpose.** Document 19 sets out when a data protection impact assessment (DPIA) is required (G-DPIA), how it is carried out and documented, how the DPO's advice is obtained and answered, how the prior-consultation test (G-36) is evaluated, and who takes the decision on the residual risk. A DPIA is an assessment of the risks to the rights and freedoms of natural persons (GDPR Art. 35(7)(c)), not only a calculation: it describes the processing, assesses necessity and proportionality, assesses the risks and records the measures that address them.

**Scope.** The method applies to every processing operation that is likely to result in a high risk to the rights and freedoms of natural persons, and to any processing that another PGF document or the organisation's own triggers send to a DPIA. It interfaces with, but does not replace, the legal compliance gate (G-L), the transfer impact assessment (Document 20) and the fundamental rights impact assessment of the AI Act (Section 4.11).

**Relationships.** The rights-and-freedoms risk assessment uses the calculation core of the Privacy Risk Assessment Methodology (Document 18). The residual-risk tiers and the acceptance authority come from the Privacy Risk Appetite Statement (Document 8). Roles follow the RACI Matrix (Document 5). DPIA outcomes are recorded in the Record of Processing Activities (Document 21) and the Privacy Risk Register (Document 22). A transfer impact assessment (Document 20) may be required in parallel. The full list is in Section 7.

# **How to Use This Document**

Part A is a template. Text in ***[square brackets, bold italic]*** is a fillable or illustrative placeholder. Blocks marked **Guidance** explain what a section should contain and are removed from the organisation's adopted version.

Part B shows the template completed for the fictional PanEuropean Bank AG, with an appendix of worked DPIA reports: three DPIAs for a credit-scoring model, one DPIA for a customer-service assistant based on a large language model, and summaries of the DPIAs behind other worked examples of the PGF.

> **Guidance.** Read this document together with Document 18 (how the risk is assessed) and Document 8 (what the tiers mean and who may accept them). This document does not reproduce their logic; it defines the procedure within which that logic is applied and the legal steps that sit around it. If Documents 8 and 18 have not yet been adopted, start with them.

Three rules apply throughout:

1. **Lawfulness first.** G-L runs before any risk decision. A G-L failure means stop or redesign; no score, tier, appetite, DPO opinion or metric can cure it.
2. **DPO advice on every DPIA.** Where a DPO is designated, the controller seeks the DPO's advice on every DPIA (Art. 35(2)), whatever the score or tier, and records how it responded.
3. **Prior consultation is a statutory test.** G-36 is evaluated for every DPIA, independently of internal tiers. An elapsed consultation period, or the absence of comments, is not an authorisation.

# **Table of Contents**

**About This Document**
**How to Use This Document**
**Part A — Template**
Glossary of Terms
1. Purpose
2. Scope of Application
3. Triage — When a DPIA Is Required (G-DPIA)
4. DPIA Procedure
5. DPIA Report Structure
6. Roles and Responsibilities
7. Relationship to Other Framework Documents
8. Review and Amendment
9. Approval
**Part B — Worked Example: PanEuropean Bank AG**
Glossary of Terms
1. Purpose
2. Scope of Application
3. Triage — When a DPIA Is Required (G-DPIA)
4. DPIA Procedure
5. DPIA Report Structure
6. Roles and Responsibilities
7. Relationship to Other Framework Documents
8. Review and Amendment
9. Approval
**Appendix to Part B — Worked DPIA Reports**
DPIA Register Excerpt
Report DPIA-CS-TRAIN-01
Report DPIA-CS-INFER-01
Report DPIA-CS-LAUNCH-01
Report DPIA-LLM-01
Summaries: DPIA-PSI-01 and DPIA-FL-01
**Normative Basis and References**
**International Adaptation**
**Document History (PGF)**

# **Part A — Template**

**DPIA Methodology and Template of *[Legal Name of the Organisation]***

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
| DPIA (Data Protection Impact Assessment) | The assessment required by GDPR Art. 35 where processing is likely to result in a high risk to the rights and freedoms of natural persons. It contains at least a systematic description of the processing and its purposes (including, where applicable, the legitimate interest pursued), an assessment of necessity and proportionality, an assessment of the risks to the rights and freedoms of data subjects, and the measures envisaged to address the risks (Art. 35(7)). The risk assessment uses the calculation core of Document 18. |
| Triage record | The documented outcome of G-DPIA for a processing operation: which statutory, supervisory-authority and WP248 criteria and which organisation-specific triggers apply, and the conclusion (DPIA required / not required, with reasons). A triage record is not a DPIA. |
| Organisation-specific trigger | A trigger adopted by the organisation in addition to the statutory and supervisory triggers (Section 3.2). It can only add DPIAs; it can never remove a DPIA required by law or by a supervisory-authority list. |
| DPO advice record | The content of the DPO's advice on a DPIA (Art. 35(2)), including reservations, and the decision-maker's documented response: followed, partly followed or not followed, with reasons. |
| G-36 record | The legal conclusion on the Art. 36(1) test, with reasons, and — where consultation takes place — the submission, the supervisory authority's written advice, information requests or measures, and how they were implemented. |
| FRIA interface | The link between a DPIA and the fundamental rights impact assessment that the AI Act requires from certain deployers of high-risk AI systems (Section 4.11). |

## **1. Purpose**

This document establishes how ***[Legal Name of the Organisation]*** decides whether a DPIA is required and how a DPIA is carried out, documented, advised on, decided and reviewed. It defines the triage criteria (Section 3), the procedure (Section 4), the minimum content of the report (Section 5) and the allocation of responsibilities (Section 6).

This document does not establish the method for assessing likelihood and severity — that is the Privacy Risk Assessment Methodology (Document 18) — and it does not set the tiers or the acceptance authority — that is the Privacy Risk Appetite Statement (Document 8). It does not decide lawfulness: that is G-L.

## **2. Scope of Application**

* ***[This document applies to every processing operation that the triage of Section 3 identifies as requiring a DPIA, whether or not another PGF document (for example, the Privacy by Design & by Default Policy, Document 16, Section 4) also refers to a DPIA gate.]***

* ***[This document determines when and how the rights-and-freedoms risk assessment of Document 18 is documented as a DPIA, who owns it, who advises, who evaluates G-36 and who decides. It does not change the content of the calculation.]***

* ***[A transfer of personal data to a third country is assessed under the Transfer Impact Assessment Methodology (Document 20). The two procedures are distinct but may both be required for the same processing: a transfer does not exclude a DPIA or the Art. 36 test, and a DPIA does not replace the transfer assessment. The DPIA records the outcome of the transfer gate (G-TIA) as an input, and the TIA may request elements of the DPIA's risk assessment.]***

* ***[Where the organisation is a processor for a client, the client controller carries out the DPIA; the organisation assists it as its processor (Art. 28(3)(f)). Where processing is carried out by joint controllers, the arrangement under Art. 26 allocates the DPIA tasks.]***

## **3. Triage — When a DPIA Is Required (G-DPIA)**

> **Guidance.** Triage separates three things that are often merged: the legal triggers (Section 3.1), the organisation's additional triggers (Section 3.2) and a scoring questionnaire (Section 3.4). Only the first are law or supervisory guidance. The questionnaire can widen the net or set the depth of the assessment; it can never remove a DPIA that Section 3.1 requires. Triage runs independently of any risk tier; an inherent High or Critical tier from a preliminary calculation is an additional indicator that a DPIA is required (Document 8, Section 4).

***3.1 Statutory and Supervisory Triggers***

A DPIA is required before the processing starts where any of the following applies:

| Source | Trigger |
| :---- | :---- |
| **A. Art. 35(1) — general test** | The processing, in particular using new technologies, and taking into account its nature, scope, context and purposes, is likely to result in a high risk to the rights and freedoms of natural persons. A single assessment may address a set of similar processing operations that present similar high risks. |
| **B. Art. 35(3) — listed cases** | (a) a systematic and extensive evaluation of personal aspects based on automated processing, including profiling, on which decisions are based that produce legal effects or similarly significantly affect the person; (b) processing on a large scale of special categories of data (Art. 9(1)) or of personal data relating to criminal convictions and offences (Art. 10); (c) a systematic monitoring of a publicly accessible area on a large scale. |
| **C. Supervisory-authority lists — Art. 35(4)** | The processing appears on the list of kinds of processing operations requiring a DPIA published by the competent supervisory authority. The authoritative source is the authority's own published list; the EDPB register of DPIA lists is used as an index, not as a substitute. A list published under Art. 35(5) (operations for which no DPIA is required) is checked in the same way, but does not override Sections 3.1.A, B or D. |
| **D. The nine WP248 rev.01 criteria** | (1) evaluation or scoring, including profiling and predicting; (2) automated decision-making with legal or similar significant effect; (3) systematic monitoring; (4) sensitive data or data of a highly personal nature (including, for example, financial data); (5) data processed on a large scale; (6) matching or combining datasets; (7) data concerning vulnerable data subjects; (8) innovative use or application of new technological or organisational solutions; (9) processing that in itself prevents data subjects from exercising a right or using a service or a contract. **Where two or more criteria are met, a DPIA is presumed to be required.** A single criterion may suffice in some cases; where the controller concludes that a DPIA is not required although two or more criteria are met, it documents the reasons. |

***[Art. 35(10): where the processing has a legal basis in Union or Member State law that regulates the specific processing operation and a DPIA was already carried out as part of a general impact assessment in the context of the adoption of that legal basis, a separate DPIA may not be required unless Member States deem it necessary. The exemption is applied only on a documented legal conclusion by [Legal], with DPO advice.]***

> **Guidance.** The nine criteria are those of the Article 29 Working Party's Guidelines on Data Protection Impact Assessment (WP248 rev.01, as last revised and adopted on 4 October 2017), endorsed by the EDPB on 25 May 2018. Do not renumber or extend them: organisation-specific triggers belong in Section 3.2. For cross-border processing, check the lists of the supervisory authorities of each Member State where the processing takes place or where data subjects are substantially affected.

***3.2 Organisation-Specific Triggers (Additional)***

In addition to Section 3.1, ***[the organisation]*** requires a DPIA in the following cases. These triggers are internal policy; they add DPIAs and never remove one.

| No. | Organisation-specific trigger |
| :---- | :---- |
| ***[O1]*** | ***[Training of a machine-learning model on personal data — before training begins, separately from the DPIA of the deployed system]*** |
| ***[O2]*** | ***[Use of an AI system (including large language models and agentic systems) to process personal data]*** |
| ***[O3]*** | ***[A material change to a business process affecting personal data, even without a new IT system (Document 16, Section 4)]*** |
| ***[O4]*** | ***[Processing of special categories of data, whatever the scale (Data Classification Policy, Document 10)]*** |
| ***[O5]*** | ***[Name and description of an additional trigger — completed if necessary]*** |

***3.3 Multiplicity of DPIAs for AI Systems***

For an AI system that processes personal data and that the organisation trains or deploys itself, the triggers may require several DPIAs for the same system, because they assess different aspects of risk:

* ***[Training-Dataset DPIA]*** — the data used to train or calibrate the model: lawful basis and purpose compatibility of the training use (Art. 6(4)), special categories, the disclosure risk of derived artefacts (Document 18, PET Assessment Module) and the cumulative privacy loss.

* ***[Deployed-System DPIA]*** — the system at the point of output: the harm that outputs or decisions can cause to individuals (including discrimination, inaccuracy, exclusion and inference of attributes not present in the input), Art. 22 permissibility and safeguards (Section 4.10) and the AI Act interface (Section 4.11).

* ***[Overall Product Pre-Launch DPIA]*** — the product of which the AI system is a component, before launch into production.

The DPIAs may be combined into one document where they are carried out together, provided each aspect is assessed and each decision is recorded. The absence of one aspect is not compensated for by the others. For a third-party AI service that the organisation uses but does not train, a single DPIA covers the use of the service.

***3.4 Triage Questionnaire***

For processing that does not clearly fall under Section 3.1, a questionnaire is used to structure the screening and to set the depth of the assessment. It assesses: the scale of processing (number of data subjects, using the bands of Document 18, Section 3.4, Factor C), the degree of automation of decisions, vulnerable data subjects, novelty of the technology, transfers outside the EEA and the data class (Document 10). The threshold above which a DPIA is required is set by ***[the EPPO, with DPO advice]*** and reviewed at least annually.

> **Guidance.** The questionnaire is a screening tool, not a legal test. It cannot override Section 3.1: if the Art. 35(3) cases, a supervisory-authority list or two or more WP248 criteria apply, a DPIA is required whatever the questionnaire score. A negative result is a triage record: it is documented with reasons, the DPO's advice on the triage is sought (Document 5, G-DPIA), and the record is kept in the evidence pack. A triage record is not a DPIA.

## **4. DPIA Procedure**

> **Guidance.** The steps follow the order of the PGF decision sequence: G-L → G-DPIA → description and necessity → risk assessment (Document 18) → measures → consultation and DPO advice → G-36 → decision → review. The step numbers are referenced by other PGF documents; keep them.

| Step | Content |
| :---- | :---- |
| 4.0 G-L (prerequisite) | ***[[Legal] confirms and records the legal compliance gate before any risk decision: lawful basis (Art. 6); Art. 9 condition or Art. 10 basis where relevant; purpose compatibility (Art. 6(4)); transparency deliverable (Arts. 13/14); Art. 22 permissibility and safeguards (Section 4.10); valid transfer tool and TIA outcome (Chapter V; Document 20); mandatory deadlines and statutory duties. A G-L failure stops the DPIA's decision path: the processing is stopped or redesigned. The DPIA may continue to inform the redesign.]*** |
| 4.1 Initiation | ***[The Processing Owner initiates the DPIA when a trigger of Section 3 applies; the Privacy Operations Lead registers it, assigns an identifier and links it to the RoPA record (Document 21). The DPIA is completed before the processing starts.]*** |
| 4.2 Systematic Description (Art. 35(7)(a)) | ***[Nature, scope, context and purposes; where the lawful basis is legitimate interests, the legitimate interest pursued and the balancing test; categories of data and data subjects; sources (including third parties and Art. 14 information); recipients, processors and joint controllers; transfers outside the EEA; retention; data flows; supporting assets (systems, people, processors).]*** |
| 4.3 Necessity and Proportionality (Art. 35(7)(b)) | ***[Whether the processing is necessary for the stated purpose and whether a less intrusive alternative exists; compliance with the Art. 5 principles (purpose limitation, data minimisation, accuracy, storage limitation); how the rights of Arts. 12–22 are ensured; processor and joint-controller arrangements (Arts. 26, 28); safeguards for transfers.]*** |
| 4.4 Rights-and-Freedoms Risk Assessment (Art. 35(7)(c)) | ***[The risk assessment uses the calculation core of Document 18, track (a): harm scenarios covering each harm type of Document 18, Factor A (or a reason why it is not relevant); likelihood per scenario — threat-based (Document 18, Section 3.2) for identified or pseudonymised data, PET Assessment Module (Section 3.3) for the disclosure scenario of a de-identified, synthetic, aggregate or federated artefact; severity per scenario (Section 3.4); inherent and residual tiers through the Document 8 matrix; the track (a) tier is the highest residual scenario tier. Select the Risk Calculation Project by archetype: identified processing that is meant to remain identified (including the use of third-party AI tools) uses the identified-processing archetype (archetype 4); base datasets awaiting a PET decision use archetype 1; releases and derived artefacts use archetypes 2–3. Organisational consequences (track (b)) are recorded separately and never offset track (a). The calculation is referenced by its project identifier and configuration version; the DPIA states the scenarios and results in narrative form.]*** |
| 4.5 Measures (Art. 35(7)(d)) | ***[The measures, safeguards and security mechanisms that address each scenario, and the mechanisms to demonstrate compliance (records, logs, tests, audits). Measures act on likelihood (Document 18, factor L3, or the PET Assessment Module) and only exceptionally on severity, where a measure demonstrably limits the consequences. Only implemented and evidenced measures reduce the residual tier; planned measures are listed with an owner and date.]*** |
| 4.6 Consultation and DPO Advice | ***[(a) DPO advice: the controller seeks the DPO's advice on every DPIA (Art. 35(2)), whatever the tier — on whether to carry out the DPIA, the method, the measures and whether the DPIA has been correctly carried out and its conclusions comply with the GDPR. The DPO advice record keeps the content of the advice, not only a reference. (b) Views of data subjects or their representatives (Art. 35(9)): sought where appropriate — for example through a customer panel, a survey, a consumer or employee representative — without prejudice to commercial or public interests or the security of processing; where they are not sought, the reasons are recorded. (c) Processors assist (Art. 28(3)(f)); AI system providers' instructions for use are taken into account (Section 4.11). (d) IT / Information Security on technical measures; [Legal] on G-L and G-36.]*** |
| 4.7 G-36 — Prior Consultation Test (Art. 36) | ***[G-36 is evaluated for every DPIA. It is a statutory test, independent of internal tiers. If the DPIA indicates that the processing would still result in a high risk to the rights and freedoms of natural persons in the absence of further mitigating measures, the controller consults the competent supervisory authority before processing starts (Art. 36(1)), irrespective of the internal tier. An internal High or Critical residual tier on track (a) is a strong indicator that the test is met; the legal conclusion is recorded separately, with reasons, by [Legal], with DPO advice. The organisation may adopt a stricter internal policy (for example, "all residual High is routed to consultation"); it is labelled as internal policy, not as a GDPR obligation. The controller — not the DPO — consults; the submission contains the information of Art. 36(3), including the DPIA and the DPO's contact details; the DPO acts as contact point for the supervisory authority (Art. 39(1)(e)). Under Art. 36(2) the supervisory authority may give written advice within eight weeks of receipt of the request, a period that may be extended by six weeks; the periods may be suspended until the authority has obtained information it has requested; and it may use its Art. 58 powers, including a temporary or definitive limitation or ban on processing. An elapsed period, or the absence of comments from the authority, is not an authorisation or a certificate of lawfulness. G-L remains in force throughout, and the controller remains responsible.]*** |
| 4.8 Decision and Sign-Off | ***[The single effective decider designated under Document 8, Section 5, for the residual track (a) tier decides — accept, accept with conditions and an expiry date, or do not accept. The decision is taken after G-36: where the test is met, after the consultation step. Critical is not acceptable: the processing is stopped or redesigned. Where the decider does not follow the DPO's advice, the decider records the reasons in the DPO advice record; the DPO may escalate directly to Executive Management and inform the Governing Body committee where the DPO considers it necessary. A refusal is recorded on the same footing as a positive decision. The DPO does not approve, reject, authorise or veto.]*** |
| 4.9 Review (Art. 35(11)) | ***[The DPIA is reviewed at least when there is a change in the risk represented by the processing: a change of purpose, data, recipients, technology, decision logic or threat landscape; model retraining; expiry of a conditional acceptance; a relevant incident; a supervisory-authority development. Each DPIA has a next-review date not later than [12] months for residual Medium and above. The organisation may publish a summary of the DPIA as a transparency measure; this is good practice, not a statutory obligation.]*** |

***4.10 Automated Decision-Making Module (Art. 22)***

Where the processing involves a decision based solely on automated processing, including profiling, which produces legal effects concerning the person or similarly significantly affects them, the DPIA records:

* ***[Whether Art. 22(1) applies, including where an automatically produced score plays a determining role in a decision taken by a third party or by a human who does not exercise genuine influence (CJEU C-634/21, *SCHUFA Holding (Scoring)*, 7 December 2023).]***

* ***[The exception relied on, which can only be one of Art. 22(2)(a) — necessary for entering into or performing a contract between the person and the controller; (b) — authorised by Union or Member State law to which the controller is subject and which lays down suitable safeguards; or (c) — based on the person's explicit consent. Legitimate interests are not an Art. 22(2) exception. Art. 22(4) restricts decisions based on special categories.]***

* ***[The safeguards of Art. 22(3) where (a) or (c) applies — at least the right to obtain human intervention on the part of the controller, to express one's point of view and to contest the decision — and how they are implemented and tested (for example, a review channel with staff authorised to change the decision; the Data Subject Rights Policy, Document 15).]***

* ***[The information given under Arts. 13(2)(f), 14(2)(g) and 15(1)(h): the existence of automated decision-making and meaningful information about the logic involved, as well as the significance and the envisaged consequences. The explanation must describe the procedure and principles actually applied, in a concise, transparent, intelligible and easily accessible form, so that the person can understand which personal data were used and how (CJEU C-203/22, *Dun & Bradstreet Austria*, 27 February 2025). Protecting the model against inversion or the controller's trade secrets may limit the disclosure of parameters, but does not remove the duty to explain; where protected information is at stake, it is handled as the applicable law provides.]***

* ***[Bias testing, model validation and monitoring as controls (Document 18, factor L3); the vulnerable groups affected (Document 18, Factor B).]***

***4.11 AI Act Interface (Deployers of High-Risk AI Systems)***

* ***[Where the processing uses an AI system classified as high-risk under the AI Act (Regulation (EU) 2024/1689, as amended by the AI Omnibus), the DPIA records the classification, the organisation's role (provider and/or deployer) and the application dates of the relevant obligations (Document 7). For high-risk systems listed in Annex III, the high-risk obligations apply from 2 December 2027; until then they are forthcoming and do not suspend any GDPR duty.]***

* ***[Deployers use the information that the provider must supply under AI Act Art. 13 (instructions for use) to carry out the DPIA (Art. 26(9)).]***

* ***[Deployers of the high-risk systems referred to in Annex III, point 5(b) (creditworthiness evaluation and credit scoring of natural persons, except systems used to detect financial fraud) and point 5(c), and certain other deployers, perform a fundamental rights impact assessment (FRIA) before first use (Art. 27). Where an obligation of Art. 27 is already met through the DPIA, the FRIA complements the DPIA (Art. 27(4)). The DPIA records the FRIA reference, or the date by which the FRIA will be completed, and the owner (the AI governance function).]***

* ***[The AI Act does not replace G-L, Art. 22, the DPIA or G-36.]***

## **5. DPIA Report Structure**

> **Guidance.** The fields below are the mandatory minimum content of the report. The organisation may add fields but may not omit those listed. Use the field names verbatim in every report.

| Report Field | Content |
| :---- | :---- |
| Identifier and Name of the Processing | ***[Unique DPIA number; RoPA record (Document 21); related TIA (Document 20) and Privacy Risk Register record (Document 22)]*** |
| Processing Owner and Dates | ***[The Processing Owner (the single owner of the DPIA); initiation date; report version and date]*** |
| Basis for Triage | ***[Triage record: Section 3.1 triggers (Art. 35(3) case; supervisory-authority list entry; WP248 criteria met and their number); Section 3.2 organisation-specific triggers; for AI systems, the DPIA type (Section 3.3)]*** |
| G-L Record | ***[Reference and outcome of G-L (step 4.0), including the lawful basis and, where relevant, the Art. 9 condition, Art. 22 exception and transfer outcome]*** |
| Description of Processing | ***[Per step 4.2, including the legitimate interest pursued where applicable]*** |
| Necessity and Proportionality Assessment | ***[Per step 4.3]*** |
| Rights-and-Freedoms Risk Assessment | ***[Per step 4.4: Risk Calculation Project and configuration version; harm scenarios and harm types; inherent and residual likelihood, severity and tier per scenario; track (a) tier; track (b) level, reported separately]*** |
| Risk-Mitigation Measures Applied | ***[Per step 4.5: implemented measures with evidence; planned measures with owner and date]*** |
| Automated Decision-Making (Art. 22) and AI Act | ***[Per Sections 4.10 and 4.11, or "not applicable" with reasons]*** |
| Consultations Conducted | ***[Views of data subjects or representatives (Art. 35(9)) — sought, with outcome, or not sought, with reasons; processors; IT / Information Security; other]*** |
| DPO Advice and Response | ***[Date and content of the DPO's advice; the decider's response: followed / partly followed / not followed, with reasons; any escalation by the DPO]*** |
| Consultation with the Supervisory Authority (G-36) | ***[Legal conclusion on the Art. 36(1) test (met / not met), with reasons, date and author; any internal-policy routing. Where consulted: competent supervisory authority, submission date, information requests and responses, written advice or Art. 58 measures, implementation; status. The lapse of the period or the absence of comments is recorded as such and is not treated as an authorisation]*** |
| Decision and Authorised Role | ***[The single effective decider under Document 8, Section 5; decision (accept / accept with conditions / do not accept); conditions; expiry date of a conditional acceptance; date]*** |
| Reference to the Evidence Pack | ***[Evidence pack identifier (EVP-YYYY-NNNN) in which the calculation, the advice, the G-36 record and the decision are kept]*** |
| Next Review Date | ***[Per step 4.9; not later than the expiry of a conditional acceptance]*** |

## **6. Roles and Responsibilities**

| Role | Responsibility |
| :---- | :---- |
| ***[Processing Owner]*** | ***[Accountable for the triage (G-DPIA) and for the DPIA of the processing it owns; provides the description of processing; takes the decision on residual risk up to the delegated tier (Document 8, Section 5); records reasons where the decision departs from the DPO's advice; proposes High cases to the designated decider; stops or redesigns at Critical]*** |
| ***[DPO]*** | ***[Gives advice on every DPIA (Art. 35(2)) and on triage, method, measures, the G-36 conclusion and the decision; monitors performance of the DPIA (Art. 39(1)(c)); is the contact point for the supervisory authority in a prior consultation (Art. 39(1)(e)); may escalate directly to Executive Management. The DPO does not approve, reject, authorise processing, accept risk or consult the supervisory authority on the controller's behalf]*** |
| ***[Legal]*** | ***[Accountable for G-L; records the legal conclusion on the Art. 36(1) test, with reasons and with DPO advice; prepares the consultation submission with the Processing Owner]*** |
| ***[EPPO]*** | ***[Owns this methodology; concurs in Medium acceptances (Document 8); informed of every DPIA outcome]*** |
| ***[Member of Executive Management designated by delegation (or the Privacy Risk Committee where a written delegation designates it)]*** | ***[Single decider for High residual risk; decides on the prior consultation where the G-36 test is met; decides after the consultation step]*** |
| ***[Privacy Operations Lead]*** | ***[Registers DPIAs and triage records; owns the Risk Calculation Project used (Document 18); compiles the evidence pack; tracks review dates]*** |
| ***[Privacy Officer(s)]*** | ***[Conduct DPIAs with the Processing Owner's team; prepare the report in the structure of Section 5]*** |
| ***[IT / Information Security]*** | ***[Advise on technical measures and evidence their implementation for factor L3]*** |
| ***[AI governance function]*** | ***[Records AI Act classification and roles; owns the FRIA where required (Section 4.11)]*** |

> **Guidance — confidentiality of the DPO's work (Art. 38(5); WP243 rev.01, §2.6).** Where others are "I" or "C" on a task performed by the DPO, this never means automatic disclosure of the content of a request made to the DPO or of the requester's identity. Disclosure follows need-to-know, purpose limitation, and secrecy or confidentiality under Art. 38(5) and applicable law; redaction or aggregate reporting is used where appropriate. The DPO decides how its own work is distributed.

## **7. Relationship to Other Framework Documents**

* Relies on the Privacy Risk Assessment Methodology (Document 18) for the rights-and-freedoms risk assessment (harm scenarios, likelihood, severity, PET Assessment Module, track (b)).

* Relies on the Privacy Risk Appetite Statement (Document 8) for the tiers, the matrix, the acceptance authority and the mandatory DPO-advice triggers.

* Roles follow the RACI Matrix (Document 5); the decision rights of the DPO and of management follow the Privacy Governance Charter (Document 2, Section 8).

* The Privacy by Design & by Default Policy (Document 16, Section 4) and the Data Classification Policy (Document 10) are sources of organisation-specific triggers.

* Art. 22 safeguards and the "Request a Review" function are operated under the Data Subject Rights Policy (Document 15).

* Transfers are assessed under the Transfer Impact Assessment Methodology (Document 20); both procedures may apply to the same processing.

* Processors' assistance and vendor due diligence follow the Vendor / Third-Party Privacy Risk Policy (Document 17).

* AI Act classification and application dates follow the Regulatory Applicability Matrix (Document 7).

* DPIA outcomes are recorded in the RoPA (Document 21) and in the Privacy Risk Register (Document 22).

* The DPIA is a step of the core process "Request & Transformation" of the Privacy Governance Process Map (Document 24).

* Tooling is connected through the Privacy Automation & Tooling Strategy (Document 9).

## **8. Review and Amendment**

This document is reviewed under the continuous-improvement principle of the Privacy Governance Charter (Document 2) and the ***[Policy Review Cycle, Document 29]***, and upon any material change to Document 18 or Document 8, to supervisory-authority lists or guidance on DPIAs, or to the AI Act application dates. Changes are adopted by ***[Executive Management]*** on the proposal of the ***[EPPO]***, after consulting the ***[Privacy Risk Committee]*** and the DPO.

## **9. Approval**

This document is adopted by ***[Executive Management]*** on ***[date]***. Document Owner: ***[EPPO]***.

# **Part B — Worked Example: PanEuropean Bank AG**

**PanEuropean Bank AG — DPIA Methodology and Template**

*Effective Date: 20 October 2026  ·  Version: 2.0  ·  Document Owner: Chief Privacy Officer (EPPO)  ·  Adopted by: Management Board*

*A fictional legal entity, provided solely for illustrative purposes.*

***Fictional Document History (illustrative)***

| Version | Date | Changes |
| :---- | :---- | :---- |
| 1.0 | 1 March 2026 | First version, adopted by the Management Board together with Documents 8, 18, 20 and 22. Owner at the time: Group DPO |
| 2.0 | 20 October 2026 | Re-baselined to the new role model on the creation of the Chief Privacy Officer (EPPO) position: Chief Privacy Officer as owner; acceptance by the single decider under Document 8, version 3.0; Group DPO advice on every DPIA |

## **Glossary of Terms**

*The Part A glossary applies; the entries below add PanEuropean specifics.*

| Term | Definition / Reference |
| :---- | :---- |
| HBDI | The Hessian Commissioner for Data Protection and Freedom of Information (Der Hessische Beauftragte für Datenschutz und Informationsfreiheit), PanEuropean's lead supervisory authority and the competent authority for prior consultation. BaFin and the ECB are financial supervisors and are not consulted under Art. 36. |
| PEP | The Bank's privacy engineering platform (PEP, illustrative) — a fictional internal platform on which the Bank records DPIAs and runs the calculations of Document 18. The procedure does not depend on PEP; the connection to tooling is governed by Document 9. |
| Interim procedure | The DPIA procedure applied before 1 March 2026, when version 1.0 of this document took effect. DPIAs carried out under it are re-performed under this document at their next review. |

## **1. Purpose**

This document establishes how PanEuropean Bank AG decides whether a DPIA is required and how DPIAs are carried out, advised on, decided and reviewed, using the Privacy Risk Assessment Methodology (Document 18) and the acceptance authority of the Privacy Risk Appetite Statement (Document 8, version 3.0).

## **2. Scope of Application**

This document applies to all PanEuropean processing of personal data of customers, applicants, counterparties and staff — including credit scoring, the customer-service assistant, anti-fraud matching with a partner bank, the federated-learning anti-fraud consortium, payment protection insurance (PPI) and biometric authentication — and to any other processing for which the triage of Section 3 requires a DPIA. Transfers are assessed in parallel under Document 20. Where PanEuropean processes personal data as a processor for a client, it assists the client's DPIA under the contract (Art. 28(3)(f)).

## **3. Triage — When a DPIA Is Required (G-DPIA)**

***3.1 Statutory and Supervisory Triggers***

The four sources of Part A, Section 3.1 apply unchanged: the Art. 35(1) test, the Art. 35(3) cases, the supervisory-authority lists under Art. 35(4), and the nine WP248 rev.01 criteria with the two-or-more presumption. Because PanEuropean offers services in five Member States, it checks the lists of the supervisory authorities of each of them. The authority's own published list is the source; the EDPB register is used as an index. Before each triage, the Privacy Officer checks the current version of each list.

| Member State | Supervisory authority and list | Entries the Bank checks first |
| :---- | :---- | :---- |
| Germany | The list adopted by the Datenschutzkonferenz (DSK) for the non-public sector under Art. 35(4) GDPR (commonly called the "Muss-Liste"), applied by the German supervisory authorities for private bodies, including the HBDI as PanEuropean's lead authority. (The Federal Commissioner, BfDI, is not the competent authority for a private bank.) | The list names kinds of processing operations with examples; the Bank checks the entries on scoring and creditworthiness assessment, large-scale profiling, and the combination of data from several sources |
| France | Commission nationale de l'informatique et des libertés (CNIL), Délibération n° 2018-327 of 11 October 2018 (list of processing operations requiring a DPIA), together with the CNIL's list of operations not requiring a DPIA | Entries on evaluation or scoring, including for credit decisions, and on profiling |
| Italy | Garante per la protezione dei dati personali — published list of processing operations subject to a DPIA under Art. 35(4) | Entries on scoring and profiling, and on matching or combining datasets |
| Spain | Agencia Española de Protección de Datos (AEPD) — published list of processing requiring a DPIA under Art. 35(4), and its list under Art. 35(5) | Entries on profiling and on assessment of solvency or creditworthiness |
| Poland | Prezes Urzędu Ochrony Danych Osobowych (UODO) — published list of kinds of processing operations requiring a DPIA | Entries on creditworthiness assessment and on automated decisions with legal or financial effects |

The table is a reference point only; it does not describe the full content of any list. A match with any list makes a DPIA mandatory regardless of the other criteria; the absence of a match does not exempt the processing from Section 3.1.A, B or D.

***3.2 PanEuropean Organisation-Specific Triggers (Additional)***

In addition to Section 3.1, PanEuropean requires a DPIA in the following cases. These triggers are internal policy and can only add DPIAs:

| No. | Organisation-specific trigger |
| :---- | :---- |
| O1 | Training or calibration of any machine-learning model on personal data or on artefacts derived from it — before training begins, separately from the DPIA of the deployed system |
| O2 | Use of an AI system (including large language models and agentic systems) to process personal data of customers or staff |
| O3 | A material change to a business process affecting personal data, even without a new IT system (Document 16, Section 4) |
| O4 | Processing of special categories of data or criminal-offence data, whatever the scale (Document 10) |
| O5 | Banking products for minors, or processing that targets customers on the register of financially vulnerable persons |
| O6 | A change to the PET configuration of a deployed model or release (for example, a new pseudonymisation method or new synthetic-generation parameters) that changes the risk profile |
| O7 | Connecting a new external data source or counterparty (for example, a new credit bureau, an anti-fraud matching partner or a new consortium member) to a deployed model |

***3.3 Multiplicity of DPIAs for PanEuropean AI Systems***

* For an AI system that PanEuropean itself trains and deploys and that processes personal data, the training-dataset, deployed-system and overall product pre-launch aspects are each assessed and decided. They may be documented as separate DPIAs or as one DPIA with separate decisions; the credit-scoring model uses three DPIAs (Appendix).

* For a third-party AI service that PanEuropean uses but does not train (for example, the customer-service assistant based on Example AI Provider Inc.'s model), a single DPIA covers the use of the service (DPIA-LLM-01).

* Retraining on new data triggers a new training-dataset assessment; a change of decision logic without retraining (for example, a new cut-off) triggers a new deployed-system assessment; a material product release triggers a new pre-launch assessment.

* The DPIAs of one system share an identifier root (DPIA-\<system\>-TRAIN / -INFER / -LAUNCH) for traceability in the RoPA (Document 21) and the Privacy Risk Register (Document 22).

* The Art. 22 module (Part A, Section 4.10) is part of the deployed-system DPIA.

***3.4 PanEuropean Triage Questionnaire***

The questionnaire structures the screening of processing that does not clearly fall under Section 3.1 and sets the depth of the assessment. Each answer adds the indicated points; a total of 6 points or more makes a DPIA mandatory under internal policy. The questionnaire never overrides Section 3.1.

| Question | Answer Options | Points |
| :---- | :---- | :---- |
| Number of data subjects affected (scale — Document 18, Section 3.4, Factor C, "Number of Affected Data Subjects") | < 100 / 100–9,999 / 10,000–999,999 / ≥ 1,000,000 | 0 / 1 / 2 / 3 |
| Is there an automated decision affecting the customer's access to a product or its terms? | No / Yes | 0 / 3 |
| Are vulnerable data subjects involved (minors, financially vulnerable customers)? | No / Yes | 0 / 2 |
| Is the technology or processing method new to PanEuropean (no approved Technology Implementation Package, Document 9)? | No / Yes | 0 / 2 |
| Is personal data transferred outside the EEA (Document 20)? | No / Yes, under an existing mechanism / Yes, a new mechanism or recipient | 0 / 1 / 3 |
| Data class under the Data Classification Policy (Document 10) | Public–Internal / Confidential / Restricted | 0 / 1 / 2 |

The 6-point threshold is set by the Chief Privacy Officer with Group DPO advice and is reviewed at least annually. Where the result is negative, the Processing Owner records the triage decision with reasons and with the Group DPO's advice on the triage; the Privacy Operations Lead keeps the triage record in the evidence pack on PEP.

## **4. DPIA Procedure**

The steps of Part A, Section 4 apply. PEP is used to record the DPIA, run the Document 18 calculation and keep the evidence pack; it does not take any decision.

| Step | Content |
| :---- | :---- |
| 4.0 G-L (prerequisite) | Legal & Compliance (General Counsel) records G-L before any risk decision. A G-L failure stops or sends back the proposal for redesign (Document 18, Example 4.2) |
| 4.1 Initiation | The Processing Owner initiates the DPIA; the Privacy Operations Lead registers it on PEP and links it to the RoPA record |
| 4.2 Systematic Description | Privacy Officer(s) and the Processing Owner's team complete the description, including the legitimate interest pursued where Art. 6(1)(f) is relied on; data classes are taken from the Data Inventory (Document 23) |
| 4.3 Necessity and Proportionality | Privacy Officer(s) check less intrusive alternatives, the Art. 5 principles and the rights of Arts. 12–22; where a PET is part of the design, the minimally sufficient technique is verified |
| 4.4 Rights-and-Freedoms Risk Assessment | Run on PEP under the Risk Calculation Project selected by archetype (Document 18, Projects 1–4): Project 4 for identified processing (credit decisions, the customer-service assistant, anti-fraud matching); Project 2 for synthetic training data; Project 3 for aggregate releases; Project 1 only for base datasets awaiting a PET decision. The report states scenarios, inherent and residual tiers, the track (a) tier and the track (b) level |
| 4.5 Measures | Implemented measures with evidence references from the Bank's register of technical and organisational measures; planned measures with owner and date |
| 4.6 Consultation and DPO Advice | Group DPO advice is sought on every DPIA, whatever the tier; the advice record keeps the content of the advice and the Processing Owner's response. Views of data subjects are sought where appropriate (for example, through the Bank's customer advisory panel); otherwise the reasons are recorded |
| 4.7 G-36 — Prior Consultation Test | Legal & Compliance records the legal conclusion on the Art. 36(1) test for every DPIA, with reasons and Group DPO advice. Where the test is met, the Bank (as controller) consults the HBDI before processing starts; the Chief Risk Officer, as the designated Management Board member, decides on the consultation, the Processing Owner and Legal & Compliance prepare the submission, and the Group DPO is the contact point for the HBDI. **Internal policy (not a GDPR obligation):** every residual High is routed to consultation unless General Counsel records, with reasons, that the test is not met. The lapse of the Art. 36(2) period, or the absence of comments from the HBDI, is not treated as an authorisation; G-L remains in force and PanEuropean remains responsible |
| 4.8 Decision and Sign-Off | The single decider under Document 8, Section 5, records the decision on PEP after the G-36 step: Low — Processing Owner; Medium — Processing Owner with the Chief Privacy Officer's concurrence (conditional acceptance, default expiry 12 months); High — the Chief Risk Officer, within 5 business days after the G-36 step is complete, with the Supervisory Board's Risk Committee informed; Critical — not acceptable, stop or redesign. Where the decider does not follow the Group DPO's advice, the reasons are recorded and the Group DPO may escalate directly to the Management Board |
| 4.9 Review | At the next-review date (not later than 12 months for Medium and above), on expiry of a conditional acceptance, and on the events of Section 3.3 and Part A, step 4.9 |

**Transitional rule.** Decisions taken before 23 October 2026, the date on which Document 8, version 3.0, took effect, were taken under the authority then in force (Document 8, versions 1.0 and 2.0), without Chief Privacy Officer concurrence (the position exists only from 20 October 2026). A conditional acceptance taken before that date is re-assessed under Document 8, version 3.0, at its expiry or at the next material change, and the Chief Privacy Officer's concurrence then applies to a Medium tier.

A complete set of worked reports is provided in the Appendix to Part B.

## **5. DPIA Report Structure**

The fields of Part A, Section 5 are used verbatim. At PanEuropean: the identifier is assigned on PEP; the evidence pack has the format EVP-YYYY-NNNN; the G-36 field names the HBDI as the competent authority; the decision field names one decider.

## **6. Roles and Responsibilities**

| Role | Responsibility |
| :---- | :---- |
| Processing Owner (Head of Credit Decisions; Head of Customer Service; Head of Fraud Prevention; Head of Digital Banking; CIO for IT-operated processing) | Accountable for the triage and the DPIA of the processing it owns; decides on Low and Medium residual risk (Medium with the Chief Privacy Officer's concurrence); proposes High cases to the Chief Risk Officer; records reasons where it departs from the Group DPO's advice |
| Group DPO | Advises on every DPIA and on every triage, on G-36 and on the decision; monitors DPIA performance; contact point for the HBDI; may escalate directly to the Management Board. Does not approve, reject, authorise processing or accept risk |
| Legal & Compliance (General Counsel) | Accountable for G-L; records the legal conclusion on the Art. 36(1) test with Group DPO advice; prepares the consultation submission with the Processing Owner |
| Chief Risk Officer (Management Board member) | Single designated decider for High residual risk and for prior consultation with the HBDI |
| Chief Privacy Officer (EPPO) | Owns this document; concurs in Medium acceptances; sets the triage-questionnaire threshold with Group DPO advice |
| Privacy Risk Committee | Prepares High cases for the Chief Risk Officer; does not decide |
| Privacy Operations Lead | Registers DPIAs and triage records on PEP; owns the Risk Calculation Projects; compiles evidence packs; tracks review dates |
| Privacy Officer(s) | Conduct DPIAs with the Processing Owner's team; prepare reports in the structure of Section 5 |
| CISO / IT Management | Advise on technical measures; evidence their implementation for factor L3 |
| AI governance function | Records the AI Act classification and the Bank's role; owns the FRIA for the credit-scoring model |

The confidentiality safeguard of Part A, Section 6 (Art. 38(5)) applies to the Group DPO's work.

## **7. Relationship to Other Framework Documents**

* Calculation core — PanEuropean's Privacy Risk Assessment Methodology (Document 18, version 1.2): Project 2 (Example 2.1-R) for DPIA-CS-TRAIN-01; Project 4 (Example 4.3) for DPIA-CS-INFER-01 and DPIA-CS-LAUNCH-01; Project 4 for DPIA-LLM-01 and DPIA-PSI-01.

* Tiers and acceptance authority — the Privacy Risk Appetite Statement (Document 8, version 3.0, Section 5).

* Roles — the RACI Matrix (Document 5, Section 5.2) and the Privacy Governance Charter (Document 2, Section 8).

* Organisation-specific triggers — the Privacy by Design & by Default Policy (Document 16, Section 4) and the Data Classification Policy (Document 10).

* Art. 22 safeguards and "Request a Review" — the Data Subject Rights Policy (Document 15).

* Transfers — the Cross-Border Data Transfer Policy (Document 12) and the Transfer Impact Assessment Methodology (Document 20): TIA-LLM-01 and TIA-PSI-01 run in parallel with DPIA-LLM-01 and DPIA-PSI-01.

* EuroCredit Bureau is an independent controller from which PanEuropean obtains data under a data-sharing agreement (Document 17); its own assessments are its responsibility.

* Retention of synthetic and derived datasets — the Data Retention & Disposal Policy (Document 11).

* DPIA outcomes — RoPA (Document 21) and Privacy Risk Register (Document 22).

* Process — "Request & Transformation" in the Privacy Governance Process Map (Document 24); tooling — Document 9.

## **8. Review and Amendment**

This document is reviewed annually under the Policy Review Cycle (Document 29) and upon any material change to Document 18 or Document 8, to a supervisory-authority list or to the AI Act application dates. Changes are adopted by the Management Board on the proposal of the Chief Privacy Officer, after consulting the Privacy Risk Committee and the Group DPO. This document is not a Supervisory Board reserved consent matter.

## **9. Approval**

Version 1.0 was adopted by the Management Board on 1 March 2026; the Group DPO was the document owner at that time. Version 2.0 was adopted by the Management Board on 20 October 2026, on the proposal of the Chief Privacy Officer (a position that exists from that date), after consulting the Privacy Risk Committee and the Group DPO. Document owner: Chief Privacy Officer. DPIAs started before 1 March 2026 under the interim procedure are re-performed under this document at their next review.

# **Appendix to Part B — Worked DPIA Reports**

The credit-scoring model (a high-risk AI system under the AI Act, Annex III point 5(b)) is the subject of three DPIAs under Section 3.3. The customer-service assistant is the subject of one DPIA. Summaries of two further DPIAs used elsewhere in the PGF follow. All calculations are those of Document 18 (Part B) and use the residual-risk matrix of Document 8, Section 4.

**DPIA Register Excerpt (status at 26 October 2026)**

| DPIA | Processing | Processing Owner | Risk Calculation | Track (a) residual tier | G-36 conclusion | Decision status |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| DPIA-CS-TRAIN-01 | Synthetic training data for the credit-scoring model | Head of Credit Decisions | Document 18, Project 2, Example 2.1-R | Medium | Test not met | Accepted with conditions (25 March 2026; expiry 25 March 2027 or next calibration) |
| DPIA-CS-INFER-01 | Production credit scoring — automated decisions | Head of Credit Decisions | Document 18, Project 4, Example 4.3 | High | Test met — HBDI consulted | Decision pending: Chief Risk Officer, after the consultation step |
| DPIA-CS-LAUNCH-01 | Credit-scoring product pre-launch | Head of Credit Decisions | Inherits Example 4.3 (High) + product-layer scenario | High | Covered by the same consultation | Decision pending: Chief Risk Officer; launch planned |
| DPIA-LLM-01 | Customer-service assistant (Example AI Provider Inc.) | Head of Customer Service | Document 18, Project 4 | Medium | Test not met | Accepted with conditions 25 June 2026; not in effect since 26 October 2026 — AI path suspended (TIA-LLM-01 on G-TIA hold), customer service human-only |
| DPIA-PSI-01 | Anti-fraud matching with a partner bank in India | Head of Fraud Prevention | Document 18, Project 4 | Medium | Test not met | Accepted with conditions (25 March 2026; expiry 25 March 2027) |
| DPIA-FL-01 | Federated-learning anti-fraud consortium (EU banks) | Head of Fraud Prevention | Document 18, Section 3.3.3 and Project 4 | Medium | Test not met | Accepted with conditions (15 May 2026; expiry 15 May 2027) |

The register also holds the DPIAs performed, on the G-DPIA triage outcome, for the processing recorded in RoPA-CREDIT-01, RoPA-FRAUD-01, RoPA-BIO-01, RoPA-PPI-01, RoPA-AML-01, RoPA-CCTV-01, RoPA-HR-01 and RoPA-CARD-01 (Document 21); they are not reproduced in this excerpt.

## **Report DPIA-CS-TRAIN-01**

| Report Field | Value |
| :---- | :---- |
| Identifier and Name of the Processing | DPIA-CS-TRAIN-01 — training dataset for the credit-scoring model: generation of a differentially private synthetic dataset (DP-CTGAN) from customer and EuroCredit Bureau data, and its use by Data Science for model calibration. RoPA record: RoPA-CS-002. Privacy Risk Register: PRR-CS-TRAIN-01 |
| Processing Owner and Dates | Head of Credit Decisions; initiated 14 March 2026 by Data Science on the Processing Owner's behalf; report version 1.0 dated 22 March 2026 |
| Basis for Triage | Organisation-specific trigger O1 (training of a model on personal data). WP248 criteria: data of a highly personal nature (financial data), large scale, matching or combining datasets → three criteria, presumption that a DPIA is required. DPIA type — training dataset (Section 3.3) |
| G-L Record | Legal & Compliance, 16 March 2026: lawful basis Art. 6(1)(f) — the legitimate interest in an accurate and non-discriminatory credit-risk model — with a recorded balancing test; compatibility of the training use with the original purposes assessed under Art. 6(4) and recorded; EuroCredit Bureau data used within the purposes permitted by the data-sharing agreement (EuroCredit Bureau is an independent controller); Art. 13/14 information covers model development; no special-category data in the source. G-L passed |
| Description of Processing | Purpose: calibrating the credit-scoring model on a synthetic dataset rather than on customer records. Source data: derived financial indicators, payment history, EuroCredit Bureau data of the Bank's applicants and customers (about 1.2 million customers, illustrative). The source data are used only inside the Bank's controlled PEP environment, by named Privacy Engineers, to train the generator; Data Science receives only the synthetic dataset. Generator parameters and checkpoints remain in PEP. Retention: per Document 11 for synthetic and derived datasets |
| Necessity and Proportionality Assessment | Calibration does not require access to customer records; a synthetic dataset with tested disclosure controls is a less intrusive alternative to giving Data Science the source data. Utility (Document 18, Section 4.B.6) is reported separately and is not used to offset disclosure risk. The synthetic records are generated by a model and may still disclose information about the people in the source data; this is why the PET Assessment Module is applied before any use |
| Rights-and-Freedoms Risk Assessment | Document 18, Project 2 (Sections 4.B.1–4.B.6), configuration 1.0 at the time of assessment (re-approved as configuration 1.1 on 20 October 2026); numerical result: Example 2.1-R. The first generator (Example 2.1: ε 2.1 at δ 8×10⁻⁶) failed the PET Assessment Module (ε gate and DP-configuration gate) and was not released; its run remains in the lifetime ledger. The reconfigured generator (ε 1.8 at δ 1×10⁻⁹) passed every gate, disclosure indicator 0.537 → S1 (disclosure through the synthetic dataset) likelihood Medium; severity index 7 → Significant; S1 Medium. S2 (misuse of source data or generator parameters inside PEP, threat-based): residual Low × Significant = Medium; inherent Medium × Significant = Medium. **Track (a) tier: Medium** (inherent Medium). Track (b): Moderate (reported to ERM). The fairness of credit decisions made with the calibrated model is assessed in DPIA-CS-INFER-01 |
| Risk-Mitigation Measures Applied | Differentially private generator training (privacy unit: one customer; Rényi DP accountant); per-customer contribution bound; δ configured at 1×10⁻⁹; gated membership, linkability (TP-SYN-LINK) and attribute-inference (TP-SYN-INF) tests; no exact copies of training records (DCR = 0 check); generator parameters kept inside PEP. Documented limitation: reconstruction of training records from the generator's parameters (model inversion) is not tested by the Bank; mitigated by keeping the parameters inside PEP |
| Automated Decision-Making (Art. 22) and AI Act | Not applicable to this DPIA: no decision is taken about individuals at the training stage. The model is a high-risk AI system (Annex III point 5(b)); data-governance requirements for training data are recorded by the AI governance function and are assessed with DPIA-CS-INFER-01 |
| Consultations Conducted | Views of data subjects: not sought for this DPIA, because the training step has no direct effect on individuals; views on the credit-scoring system as a whole were sought for DPIA-CS-INFER-01. IT Management and the CISO confirmed the PEP access controls |
| DPO Advice and Response | Group DPO advice, 24 March 2026: agreed with the Medium tier; advised (i) a per-run condition of ε ≤ 2.0, (ii) recording the model-inversion limitation in the evidence pack, and (iii) re-assessment before the next calibration. Response: followed in full |
| Consultation with the Supervisory Authority (G-36) | Evaluated. Legal & Compliance concluded on 24 March 2026, with Group DPO advice, that the Art. 36(1) test is not met — no scenario remains at a high risk to rights and freedoms after the measures — and recorded the reasons. No consultation |
| Decision and Authorised Role | Head of Credit Decisions (Processing Owner), 25 March 2026, with Group DPO advice, under Document 8, version 1.0: Medium accepted with conditions — ε ≤ 2.0 per generator run; every further DP run on the retail customer population is checked against the cumulative ledger before it starts (lifetime limits of Document 8, Section 3, from version 2.0: ε ≤ 10.0, δ ≤ 1×10⁻⁵; ledger at 26 October 2026: ε 6.5, δ ≈ 8.0×10⁻⁶). Expiry: 25 March 2027 or the next calibration, whichever is earlier. On re-assessment the decision is taken under Document 8, version 3.0, with the Chief Privacy Officer's concurrence |
| Reference to the Evidence Pack | EVP-2026-0012 |
| Next Review Date | The next calibration or 25 March 2027, whichever is earlier (planned) |

## **Report DPIA-CS-INFER-01**

| Report Field | Value |
| :---- | :---- |
| Identifier and Name of the Processing | DPIA-CS-INFER-01 — the deployed credit-scoring system: automated decisions on retail credit applications. RoPA record: RoPA-CS-003. Privacy Risk Register: PRR-CS-INFER-01 |
| Processing Owner and Dates | Head of Credit Decisions; initiated 2 April 2026; report version 1.0 dated 4 September 2026, after independent model validation |
| Basis for Triage | Art. 35(3)(a) — systematic and extensive evaluation of personal aspects based on automated processing, on which decisions with legal or similarly significant effects are based. WP248 criteria: evaluation or scoring; automated decision with legal effect; data of a highly personal nature (financial data); large scale; matching of datasets → five criteria. Supervisory-authority lists: entries on scoring/creditworthiness checked (Section 3.1). DPIA type — deployed system |
| G-L Record | Legal & Compliance, 31 August 2026: lawful basis Art. 6(1)(b) (steps at the applicant's request prior to entering into a credit contract), together with the Bank's creditworthiness-assessment obligations under applicable consumer-credit and banking law; Art. 22(2)(a) — necessity for entering into the contract, supported by the necessity record below (scope: clear approvals and clear refusals; borderline cases are not solely automated); Art. 22(3) safeguards designed and tested in pre-production (Section 4.10); Art. 13/14 information including meaningful information about the logic involved, its significance and envisaged consequences; EuroCredit Bureau data obtained from an independent controller with Art. 14 information; no special-category data used (Art. 22(4) not engaged). Legitimate interests are not relied on as an Art. 22 exception. G-L passed for the planned production design, on the basis of the necessity record |
| Description of Processing | **Planned production design — not yet running.** At 26 October 2026 no production decision has been taken with this model; the production launch is planned for 1 February 2027 and may not take place before the prior-consultation step is complete and the Chief Risk Officer has decided. Purpose: deciding on retail credit applications with a model calibrated as assessed in DPIA-CS-TRAIN-01; expected volume about 400,000 applications a year (illustrative planning assumption based on current application volumes). Data: application attributes (income, debt burden), transaction history, EuroCredit Bureau data. In the planned design, applications with clear approval or clear refusal scores are decided automatically; applications with scores in a borderline band around the cut-off are routed to a credit officer who decides before any decision takes effect; every applicant can obtain human review through "Request a Review" (Document 15) |
| Necessity and Proportionality Assessment | **Art. 22(2)(a) necessity record** (Legal & Compliance with the Head of Credit Decisions, 28 August 2026; evidence in EVP-2026-0047; figures are illustrative assumptions). Alternatives considered: (A) fully manual underwriting of every application; (B) model score as a recommendation only, with a credit officer deciding every application before effect; (C) solely automated approvals, with every intended refusal reviewed by a credit officer before effect; (D) solely automated decisions for clear cases, with borderline cases decided by a credit officer before effect and review on request for all. Assessment: (A) and (B) would require a credit-officer capacity estimated at several times the current team for about 400,000 applications a year and would replace the same-session decision offered in the digital channels with a turnaround of several business days; (C) would require pre-effect review of about 100,000 intended refusals a year; in the pre-production comparison (EVP-2026-0047), credit officers agreed with the model on clear refusals in about 98% of cases, while disagreement concentrated in the borderline band, so pre-effect review of clear refusals adds little protection at disproportionate cost and delay, whereas review of the borderline band addresses the cases in which human judgement changes outcomes. Result: (D) adopted — Art. 22(2)(a) is relied on only for clear approvals and clear refusals, for which no equally effective, less intrusive alternative was found feasible on these assumptions; borderline cases are not solely automated decisions. The record is re-assessed with production data at the first review. Proportionality further rests on the Art. 22(3) safeguards, minimisation of input variables (no variables that are proxies for protected characteristics without a documented justification and bias test), and the explanation provided to applicants. Re-use of scoring data for marketing is excluded (incompatible purpose — Art. 6(4)) and enforced by purpose binding on the data platform |
| Rights-and-Freedoms Risk Assessment | Document 18, Project 4 (Sections 4.D.1–4.D.6), configuration 1.0 at the time of assessment (re-approved as 1.1 on 20 October 2026); numerical result: Example 4.3. S1 — systematic adverse or discriminatory automated decisions, including through corrupted bureau data: residual likelihood Medium (index 6; inherent 9, Near-certain); severity index 9 → Catastrophic; residual **High** (inherent Critical). S2 — loss of confidentiality of application and bureau data: residual Medium × Significant = Medium (inherent High). S3 — re-use for marketing: not scored, prevented by G-L. **Track (a) tier: High** (S1; inherent Critical). Track (b): Significant (applicable regime, financial and reputational consequences), reported to ERM; it does not change track (a). The inherent Critical tier shows that bias testing, validation, monitoring and human review are indispensable conditions of the processing |
| Risk-Mitigation Measures Applied | Pre-deployment bias testing across protected characteristics and proxies; independent model validation; quarterly fairness and drift monitoring with alert thresholds; pre-effect decision by a credit officer for scores in the borderline band; human review on request by credit officers authorised to change the decision; data-quality controls on bureau input; access control, encryption, logging and penetration-tested interfaces (S2). Explanation to applicants: the main factors that led to the decision, how they were weighed in general terms and what could change the outcome; model parameters are not disclosed, which limits model-inversion risk but does not limit the explanation |
| Automated Decision-Making (Art. 22) and AI Act | Art. 22 applies; exception Art. 22(2)(a); safeguards Art. 22(3) — human intervention, expression of the applicant's point of view and contestation via "Request a Review"; information under Arts. 13(2)(f), 14(2)(g) and 15(1)(h) as described above (C-634/21; C-203/22). AI Act: PanEuropean develops the model and deploys it — it is provider and deployer of a high-risk system under Annex III point 5(b). The high-risk obligations, including the deployer's obligations under Art. 26 and the FRIA under Art. 27, apply from 2 December 2027 (forthcoming). The AI governance function will complete the FRIA before that date, building on this DPIA (Art. 27(4)); the provider documentation the Bank prepares under Art. 13 is used for this DPIA (Art. 26(9)) |
| Consultations Conducted | Views of data subjects (Art. 35(9)): the Bank's customer advisory panel discussed the design on 14 July 2026, and complaints about credit decisions taken under the Bank's current credit process over the previous 12 months were analysed. Applicants asked mainly for understandable reasons and a quick human review; both are reflected in the explanation design and in the review service levels of Document 15. CISO and IT Management on technical measures |
| DPO Advice and Response | Group DPO advice, 9 September 2026: agreed that the Art. 36(1) test is met because S1 remains at a high risk after the measures; advised consulting the HBDI before launch; advised adding the explanation text to the consultation file and fixing an alert threshold for the quarterly fairness monitoring. Response: followed in full |
| Consultation with the Supervisory Authority (G-36) | Evaluated. Legal & Compliance concluded on 10 September 2026, with Group DPO advice, that the Art. 36(1) test is met: S1 remains at a high risk to rights and freedoms after the measures, and no further measure available to the Bank reduces it without giving up automated decisions. Reasons recorded. On the Management Board's decision, the Bank submitted a request for prior consultation to the HBDI on 15 September 2026 (Art. 36(3) information, including this DPIA, DPIA-CS-LAUNCH-01 and the Group DPO's contact details). The HBDI requested further information on 6 October 2026; the Bank answered on 13 October 2026 (the period was suspended until the information was received). Status at 26 October 2026: the HBDI's written advice is awaited; the statutory period is running and may be extended. Production processing does not start before the consultation step is complete. Any written advice is implemented and recorded; any information request is answered; any Art. 58 measure is complied with. The lapse of the period, or the absence of comments, will be recorded as such and is not an authorisation |
| Decision and Authorised Role | Pending. Decider: the Chief Risk Officer, as the single designated Management Board member (Document 8, version 3.0, Section 5), within 5 business days after the G-36 step is complete; Group DPO advice recorded; the Supervisory Board's Risk Committee was informed of the consultation on 23 October 2026 and will be informed of the decision |
| Reference to the Evidence Pack | EVP-2026-0047 |
| Next Review Date | On receipt of the HBDI's advice; upon any material model update or change of decision logic; at the latest 12 months after the production launch |

## **Report DPIA-CS-LAUNCH-01**

| Report Field | Value |
| :---- | :---- |
| Identifier and Name of the Processing | DPIA-CS-LAUNCH-01 — pre-launch DPIA of the "Credit Scoring" product in Digital Banking services: from submission of the application in the mobile app or online banking to notification of the decision and any request for review. RoPA record: RoPA-CS-001. Privacy Risk Register: PRR-CS-LAUNCH-01 |
| Processing Owner and Dates | Head of Credit Decisions (Processing Owner), with the Head of Digital Banking for the channel; initiated 20 April 2026; report version 1.0 dated 7 September 2026 |
| Basis for Triage | Organisation-specific trigger O3 (new business process) and the pre-launch gate of Document 16; the Art. 35(3)(a) case of DPIA-CS-INFER-01 applies to the product as a whole. DPIA type — overall product pre-launch |
| G-L Record | As for DPIA-CS-INFER-01 (31 August 2026), extended to the channel: optional marketing fields separated from the application and off by default, with separate consent where used (Document 13). G-L passed |
| Description of Processing | Data-collection interface, temporary storage of the application draft, integration with the scoring model (assessed in DPIA-CS-TRAIN-01 and DPIA-CS-INFER-01), notification of the decision and of the explanation, and the "Request a Review" entry point |
| Necessity and Proportionality Assessment | The interface requests only the fields needed for the credit decision (Document 16, Section 4); marketing fields are separate and optional |
| Rights-and-Freedoms Risk Assessment | The product inherits the scenarios of DPIA-CS-INFER-01 (Document 18, Example 4.3): **High** (inherent Critical). One product-layer scenario was added under Project 4 — S4, loss of confidentiality of stored application drafts and notifications: likelihood L1 2 + L2 2 + L3 0 (session timeout, encryption of drafts, automatic deletion after 24 hours, tested) + L4 1 = 5 → Medium (inherent 8 → High); severity Restricted 3 + scale 2 (10,000–999,999 applicants) = 5 → Moderate; S4 residual Medium × Moderate = Low (inherent High × Moderate = Medium). **Track (a) tier of the product: High**, inherited from DPIA-CS-INFER-01 (not from DPIA-CS-TRAIN-01, whose tier is Medium) |
| Risk-Mitigation Measures Applied | Measures of DPIA-CS-TRAIN-01 and DPIA-CS-INFER-01 unchanged; at product level: session timeout, encryption of the stored draft, deletion of the draft after 24 hours unless the applicant asks to keep it, plain-language explanation screen with a direct link to "Request a Review" |
| Automated Decision-Making (Art. 22) and AI Act | As for DPIA-CS-INFER-01 |
| Consultations Conducted | Customer advisory panel (14 July 2026) on the explanation screen and the review entry point; CISO on the channel controls |
| DPO Advice and Response | Group DPO advice, 9 September 2026 (combined with DPIA-CS-INFER-01): advised that the product launch be covered by the same prior consultation and that the review entry point be visible on the decision screen. Response: followed in full |
| Consultation with the Supervisory Authority (G-36) | Evaluated together with DPIA-CS-INFER-01: test met (Legal & Compliance, 10 September 2026, with Group DPO advice). Covered by the prior consultation submitted to the HBDI on 15 September 2026; status as in DPIA-CS-INFER-01 |
| Decision and Authorised Role | Pending. Decider: the Chief Risk Officer, after the consultation step, within 5 business days after it is complete. The production launch is planned for 1 February 2027 and will not take place before the consultation step is complete and the Chief Risk Officer has decided; the conditions of DPIA-CS-TRAIN-01 and DPIA-CS-INFER-01 apply |
| Reference to the Evidence Pack | EVP-2026-0048 |
| Next Review Date | On receipt of the HBDI's advice; upon a material product change; at the latest 12 months after the launch |

## **Report DPIA-LLM-01**

The customer-service assistant uses a large language model provided by Example AI Provider Inc., a fictional US-based provider acting as PanEuropean's processor. The provider's attributes below are illustrative assumptions, not statements about any real provider. A single DPIA covers the use of the service (Section 3.3).

| Report Field | Value |
| :---- | :---- |
| Identifier and Name of the Processing | DPIA-LLM-01 — customer-service assistant: summarising incoming customer chat and e-mail messages for customer-service agents and drafting reply suggestions that an agent reviews, edits and sends. RoPA record: RoPA-LLM-01. Related TIA: TIA-LLM-01 (Document 20). Privacy Risk Register: PRR-LLM-01 |
| Processing Owner and Dates | Head of Customer Service; version 1.0 of 25 June 2025 was carried out under the interim procedure before the service went live; this report, version 2.0, re-performs the DPIA under this document and Document 18, Project 4, and is dated 18 June 2026 |
| Basis for Triage | Organisation-specific trigger O2 (use of an AI system). WP248 criteria: innovative use of new technological solutions; data of a highly personal nature (financial matters raised by customers); large scale → three criteria, presumption that a DPIA is required. DPIA type — single DPIA for a third-party AI service |
| G-L Record | Legal & Compliance, 15 June 2026: handling of customer enquiries on Art. 6(1)(b) where the enquiry concerns the customer's contract and Art. 6(1)(f) otherwise, with a balancing test recorded for the use of AI assistance (legitimate interest: timely and consistent handling of enquiries); the processor engaged under an Art. 28 contract; Art. 13 information updated to describe AI-assisted handling, the processor and the transfer; **Art. 9 outcome:** Legal & Compliance identified no Art. 9(2) condition for sending special-category data to the AI processor (the Bank does not rely on Art. 9(2)(e): information that a customer sends to the Bank is not data manifestly made public, and no other condition applies to this purpose). Special-category data are therefore excluded from the AI-processor path by design: the hardship, collections and complaints channels are excluded; every message passes a detector before any transfer, and the path is fail-closed — a message that the detector flags, or cannot classify (error, timeout or low confidence), is not sent and is routed to human-only handling in the Bank's own systems. Handling in the human-only path is outside this DPIA; its Art. 9 legal conclusion is recorded in the customer-service processing record (RoPA-CSV-01, Document 21): special-category content that customers volunteer is used only to the extent necessary to handle the enquiry and only where a condition applies — the establishment, exercise or defence of legal claims for complaints and disputes (Art. 9(2)(f)), or the customer's explicit consent where the Bank needs to use the information for a service the customer requests (Art. 9(2)(a)); otherwise it is not used and is deleted under Document 11. No general customer-service exception is relied on. Residual scope — special-category content that the detector misses: no Art. 9(2) condition covers it, so G-L is not passed for that content, and the permissible design is minimisation and remediation: the detector's false-negative rate is measured monthly on a labelled sample against a validation and escalation threshold (upper 95% bound ≤ 0.5%, illustrative) — a measure of detector quality, not a legal tolerance for transferring special-category content without an Art. 9(2) condition; every detected case is blocked or isolated and investigated immediately, whatever the overall rate; an agent who sees special-category content in an AI-processed conversation flags it, the Bank requests deletion at the provider and records the event as a privacy incident (Document 14); if the threshold is exceeded, the AI path is suspended for the channel until the detector is redesigned; no decision about customers is taken (Art. 22 not engaged); Chapter V: TIA-LLM-01 (G-TIA passed on 22 June 2026; on hold since 26 October 2026 — AI path suspended). G-L passed for the AI-processor path as designed (special-category data excluded, fail-closed); not passed for undetected special-category content, which is handled by the remediation and suspension rule above |
| Description of Processing | Data: the masked customer message being handled and internal knowledge-base articles; the assistant does not retrieve customer records from the CRM or any other system, and any extension of its inputs requires a new DPIA module and a re-evaluation of TIA-LLM-01. Before sending, the Bank masks account numbers (IBAN), card numbers and national identification numbers. Data subjects: customers contacting customer service (about 300,000 customers a year, illustrative). Recipient: Example AI Provider Inc. (processor, USA); fictional illustrative contract terms: deletion of prompts and outputs within 30 days and no training on customer data; sub-processors only with the Bank's prior specific or general written authorisation (Document 17). Customers may ask for human-only handling |
| Necessity and Proportionality Assessment | AI assistance reduces response times and improves consistency; the alternative of fully manual handling remains available on request. Minimisation: masking of identifiers, no retrieval of customer records (message being handled and knowledge-base articles only), exclusion of sensitive channels. The assistant never sends a message by itself; an agent reviews every draft. Re-use of conversation content for marketing or profiling is excluded (Art. 6(4)) and blocked by purpose binding |
| Rights-and-Freedoms Risk Assessment | Document 18, Project 4 (archetype 4, threat-based likelihood; no PET-module disclosure test is claimed for unstructured data). **S1 — loss of confidentiality of customer messages at or through the processor** (provider-side breach, unauthorised access by provider staff or sub-processors, use contrary to instructions; harm types: loss of confidentiality, identity fraud, financial loss, reputational harm): L1 2 (routine access by a processor) + L2 2 (opportunistic insider or partner) + L3 1 residual (masking tested by the Bank; provider controls evidenced through due diligence and contractual audit rights, not tested by the Bank) / 3 inherent + L4 1 (sector events) = 6 → Medium (inherent 8 → High). Severity: data class Confidential 2 + special categories 2 (scored conservatively: undetected special-category content cannot be excluded, although it is not permitted on this path) + vulnerability 0; scale 2 (10,000–999,999) + source aggregation 1 (scored conservatively: the message thread of the ticket is combined with knowledge-base content in one prompt; no customer records are retrieved); reach +1 (processor); ADM 0; provenance 0 → index 8 → Significant. S1 residual Medium × Significant = **Medium**; inherent High × Significant = High. **S2 — inaccurate or inappropriate AI-drafted reply sent to a customer** (wrong statement on fees or terms, information about another customer through a context mix-up; harm types: financial loss, loss of control, loss of confidentiality): L1 3 (every routed enquiry receives a draft) + L2 2 (known error modes of language models) + L3 1 residual (mandatory agent review; context limited to the customer's own ticket; quality-assurance sampling; automation bias not measured) / 3 inherent + L4 2 (near misses in the Bank's own pilot: incorrect fee statements caught in review) = 8 → High (inherent 10 → Near-certain). Severity: Confidential 2; scale 2 + aggregation 1; reach 0; ADM 0; provenance 0 → index 5 → Moderate. S2 residual High × Moderate = **Medium**; inherent Near-certain × Moderate = Medium. S3 — re-use of conversation content for marketing: not scored, prevented by G-L. Discrimination or adverse automated decisions: not relevant (no decisions). Public-authority access in the destination country: assessed in TIA-LLM-01 (laws and practices), not offset here. **Track (a) tier: Medium** (inherent High). Track (b): applicable regime +1 (supervised financial sector; ICT third-party arrangement), financial 1, reputational 1 → index 3 → Moderate, reported to ERM |
| Risk-Mitigation Measures Applied | Masking of identifiers before sending (tested monthly on a sample); exclusion of hardship, collections and complaints channels; fail-closed special-category detector with monthly false-negative measurement, agent flagging, deletion request and suspension rule; mandatory agent review of every draft; quality-assurance sampling of sent replies (3%); context limited to the customer's own ticket; Art. 28 contract with deletion and no-training terms (illustrative); audit rights; encryption in transit; access logging at the Bank; human-only handling on request. Planned: automated checks of fee and rate statements against the product catalogue (owner: Head of Customer Service; due 31 December 2026) |
| Automated Decision-Making (Art. 22) and AI Act | Art. 22: not applicable — the assistant takes no decision; an agent decides on every reply. AI Act: the assistant is not a high-risk system under Annex III in this use; customers do not interact with it directly. If the design changes so that customers interact with the system directly, the AI Act transparency obligations are assessed first |
| Consultations Conducted | Views of data subjects (Art. 35(9)): a customer survey in the pilot (May 2026) showed acceptance of AI-assisted drafting if a human reviews the reply and human-only handling is available; both are implemented. Example AI Provider Inc. provided information on its security measures and sub-processors (Art. 28(3)(f)). CISO on masking and logging |
| DPO Advice and Response | Group DPO advice, 20 June 2026: (i) extend the exclusion to the complaints channel — followed; (ii) raise the quality-assurance sample from 2% to 5% for the first three months — partly followed: the Head of Customer Service set 3% and recorded the reasons (agent capacity; the planned automated fee checks address the main error mode); the Group DPO was informed and did not escalate; (iii) score special categories conservatively — followed |
| Consultation with the Supervisory Authority (G-36) | Evaluated. Legal & Compliance concluded on 22 June 2026, with Group DPO advice, that the Art. 36(1) test is not met — no scenario remains at a high risk after the measures — and recorded the reasons. No consultation |
| Decision and Authorised Role | Head of Customer Service (Processing Owner), 25 June 2026, with Group DPO advice, under Document 8, version 1.0 then in force: Medium accepted with conditions — masking and quality-assurance controls maintained; TIA-LLM-01 then passed (22 June 2026); update 26 October 2026: TIA-LLM-01 is on G-TIA hold (legal assessment incomplete), the AI path is suspended under Clause 14(f) and customer service is human-only until a current pass is recorded, and this acceptance is not in effect meanwhile; any new sub-processor or change of the provider's terms triggers re-assessment. Expiry: 25 June 2027. On re-assessment the decision is taken under Document 8, version 3.0, with the Chief Privacy Officer's concurrence |
| Reference to the Evidence Pack | EVP-2026-0029 (version 1.0 of 2025: EVP-2025-0031) |
| Next Review Date | 25 June 2027 at the latest (planned); earlier upon a change of provider terms or sub-processors, a relevant incident, or a change in TIA-LLM-01 |

## **Summaries: DPIA-PSI-01 and DPIA-FL-01**

These DPIAs are not reproduced in full; their results are used in Documents 20 and 22.

| Field | DPIA-PSI-01 — anti-fraud matching with a partner bank in India | DPIA-FL-01 — federated-learning anti-fraud consortium |
| :---- | :---- | :---- |
| Processing and owner | PanEuropean learns which of its customers appear on the partner bank's list of identities linked to confirmed fraud, through a private set intersection protocol in which only PanEuropean receives the result; fraud analysts review every match before any action. Processing Owner: Head of Fraud Prevention. RoPA-PSI-01; TIA-PSI-01; PRR-PSI-01; evidence pack EVP-2026-0018 | Joint training of an anti-fraud model with other EU banks; each bank's customer data stay with that bank; only differentially private model updates leave it, through secure aggregation. Processing Owner: Head of Fraud Prevention. Art. 26 arrangement among the consortium members; RoPA-FL-01; evidence pack EVP-2026-0041; PRR-FL-01 |
| Triage | WP248: matching or combining datasets; data of a highly personal nature; large scale; possible effect on the use of a service → presumption | WP248: innovative technology; large scale; data of a highly personal nature → presumption |
| G-L | Art. 6(1)(f) — fraud prevention (Recital 47), balancing test recorded; Art. 10 and national-law questions on fraud-related data and banking confidentiality assessed by Legal & Compliance; Art. 14 information; Chapter V — TIA-PSI-01 (G-TIA passed for the one-sided design, 20 March 2026) | Art. 6(1)(f) — fraud prevention; Art. 26 arrangement; Chapter V — no third-country importer among the consortium members (General Counsel's transfer-status conclusion, re-checked on any change of membership) |
| Risk assessment (Document 18) | Project 4. S1 — wrongful match leading to adverse action (harm: adverse decision, financial loss, exclusion): L1 2 + L2 2 + L3 1 (analyst review before action; partner list quality required by contract, partly tested) + L4 2 (near misses from name transliteration in the pilot) = 7 → High (inherent 9 → Near-certain); severity Restricted 3 + scale 1 (100–9,999 matches a year) + aggregation 1 + provenance 1 (third-party source outside typical expectations) = 6 → Moderate; residual High × Moderate = **Medium** (inherent Medium). S2 — disclosure of customer relationships to the partner or in the destination country: L1 2 + L2 3 (including compelled use of the partner by an authority) + L3 1 (blinded protocol messages; key held by PanEuropean in the EEA; one-sided design without any output to the partner — no match result, intersection size or other result-dependent signal; input padded to a fixed public bound; independent protocol review — illustrative assumptions: TIA-PSI-01) + L4 0 = 6 → Medium (inherent 8 → High); severity Confidential 2 + scale 3 (≥ 1,000,000 identifiers input) + reach 1 = 6 → Moderate; residual Medium × Moderate = Low (inherent Medium). **Track (a): Medium** (inherent Medium) | S1 — disclosure through model updates or the final model: PET Assessment Module (Document 18, Section 3.3.3), attack set declared in the project passport. Mandatory (gated): (i) DP statement — privacy unit one customer; per-customer clipping, with the full noise for PanEuropean's customers added by PanEuropean to its own update before aggregation; Rényi DP accountant; ε 2.6 at δ 1×10⁻⁹ across all rounds (gate ε ≤ 3.0 — pass; entered in the lifetime ledger: cumulative ε 6.5, δ ≈ 8.0×10⁻⁶, within the Document 8 limits); (ii) secure aggregation — validated by an independent protocol review and a per-round check of the minimum number of participants (pass); (iii) membership inference on the final consortium model on a balanced set — AUC 0.53, 95% CI 0.52–0.54 (illustrative), gate on the upper bound < 0.60 — pass. Gradient-reconstruction test: classified as not applicable for the observers in scope, not as passed (Document 18, Part B, Section 3.3.3) — validated secure aggregation and access restriction mean that no consortium member and no coordinator can observe an individual bank's updates, so the threat the test addresses is excluded for them by control; the residual threat from aggregate updates and the final model is covered by the DP guarantee across all rounds (noise added by PanEuropean before aggregation) and by the mandatory membership test; the Bank has no validated test for this attack class and claims no measured result (documented limitation). If the validation of secure aggregation lapses, or an observer gains access to individual updates, the test becomes mandatory and the module outcome is INCOMPLETE (G-M5) until evidence exists. At the assessment date no mandatory result was missing. Outcome: PASS, disclosure indicator 0.30 (single weighted metric: normalised AUC) → likelihood Low (evidence EVP-2026-0041); severity Restricted 3 + scale 3 + reach 1 = 7 → Significant; Low × Significant = **Medium**. S2 — use of the joint model or updates by a member beyond the Art. 26 purpose: L1 1 + L2 2 + L3 1 + L4 0 = 4 → Medium (inherent 6 → Medium); severity 7 → Significant; Medium × Significant = **Medium**. **Track (a): Medium** (inherent Medium). Deployment of the model in transaction monitoring is covered by the transaction-monitoring DPIA |
| DPO advice, G-36, decision | Group DPO advice 23 March 2026, followed. G-36 evaluated — test not met (Legal & Compliance, 24 March 2026). Head of Fraud Prevention, 25 March 2026: Medium accepted with conditions (analyst review before any action; transliteration rules; TIA-PSI-01 valid with its partner-input controls); expiry 25 March 2027; re-assessment under Document 8, version 3.0 | Group DPO advice 12 May 2026, followed (classify the gradient-reconstruction test as not applicable for the observers in scope, with the stated reason and the INCOMPLETE fallback, and record the limitation in EVP-2026-0041). G-36 evaluated — test not met (Legal & Compliance, 13 May 2026). Head of Fraud Prevention, 15 May 2026: Medium accepted with conditions (ε ≤ 3.0 across all rounds; ledger check against Document 8, Section 3; membership changes trigger re-assessment); expiry 15 May 2027 |

# **Normative Basis and References**

**EU law and case law**
* Regulation (EU) 2016/679 (GDPR): Arts. 5, 6, 9, 10, 12–22, 24, 25, 26, 28(3)(f), 35, 36, 38, 39, 58; Recitals 47, 71, 75, 76, 84, 89–94.
* Regulation (EU) 2024/1689 (AI Act), as amended by the AI Omnibus (in force 27 July 2026): Annex III point 5(b); Arts. 13, 26(9), 27 (including 27(4)); high-risk obligations for Annex III systems apply from 2 December 2027.
* CJEU, C-634/21, *SCHUFA Holding (Scoring)*, 7 December 2023 (a score playing a determining role is an Art. 22 decision).
* CJEU, C-203/22, *Dun & Bradstreet Austria*, 27 February 2025 (meaningful information about the logic involved; explanation of the procedure and principles actually applied).
* CJEU, C-453/21, *X-FAB Dresden*, 9 February 2023 (DPO conflicts of interest assessed case by case).

**EDPB, Article 29 Working Party and supervisory authorities**
* Article 29 Working Party, Guidelines on Data Protection Impact Assessment (DPIA) and determining whether processing is "likely to result in a high risk" (WP248 rev.01, last revised and adopted 4 October 2017; endorsed by the EDPB on 25 May 2018) — nine criteria; https://www.edpb.europa.eu/documents/guideline/data-protection-impact-assessments-high-risk-processing_en
* Article 29 Working Party, Guidelines on Data Protection Officers (WP243 rev.01, revised 5 April 2017), §2.6 (confidentiality).
* Article 29 Working Party, Guidelines on Automated individual decision-making and Profiling (WP251 rev.01), endorsed by the EDPB.
* EDPB, register of national DPIA lists (index of the lists adopted under Art. 35(4) and (5)).
* Datenschutzkonferenz (DSK), list for the non-public sector under Art. 35(4) GDPR; CNIL, Délibération n° 2018-327 of 11 October 2018; the published Art. 35(4) lists of the Garante, the AEPD and the UODO — as current on the date of each triage.

**Standards and methods**
* ISO/IEC 29134:2023, *Information technology — Security techniques — Guidelines for privacy impact assessment* — bibliographic pointer; no clause-level mapping is claimed.
* CNIL, *Privacy Impact Assessment (PIA)* — methodology and knowledge bases.
* NIST, NISTIR 8062, *An Introduction to Privacy Engineering and Risk Management in Federal Systems* (January 2017).

# **International Adaptation**

The GDPR is the baseline of this methodology. Where other regimes apply, the organisation substitutes their tests:

* **UK GDPR / Data Protection Act 2018** (as amended by the Data (Use and Access) Act 2025, phased commencement): the DPIA and prior-consultation structure is retained; prior consultation is with the Information Commissioner, and the ICO's published list of processing likely to result in high risk replaces the EU supervisory-authority lists. Check the commenced text before relying on any change.
* **Switzerland (revFADP, in force since 1 September 2023):** a data protection impact assessment is required where processing may result in a high risk to the personality or fundamental rights of the data subject; where the assessment shows a high residual risk despite the measures, the Federal Data Protection and Information Commissioner (FDPIC) is consulted beforehand, unless the Act's exception for consulting a data protection adviser applies.
* **Canada — PIPEDA:** there is no general statutory PIA obligation for private-sector organisations; privacy impact assessments are an accountability practice expected under Schedule 1 (Principle 4.1) and in the OPC/OIPC guidance *Getting Accountability Right with a Privacy Management Program*. The Privacy Officer (Principle 4.1) is not an EU statutory DPO.
* **Canada — Québec (Act respecting the protection of personal information in the private sector, P-39.1, as amended by Law 25):** a privacy impact assessment is required for any project to acquire, develop or overhaul an information system or electronic service delivery involving personal information, and before communicating personal information outside Québec; the person in charge of the protection of personal information is consulted. Where a decision is based exclusively on automated processing, the person must be informed and may submit observations for review. Use the private-sector Act's own provisions (not those of the public-sector Act). The applicability map is in Document 7.
* No claim of full compliance with any jurisdiction is made.

# **Document History (PGF)**

| Release | Date | Changes |
| :---- | :---- | :---- |
| 1.0.0-rc.1 | 2026-10-26 | Canonical English Markdown; changes from internal ver.2: triage restructured into statutory triggers (Art. 35(1), Art. 35(3), supervisory-authority lists under Art. 35(4)) and the nine WP248 rev.01 criteria with the two-or-more presumption, with organisation-specific triggers labelled as additional (the "eleven criteria" claim removed); supervisory-authority list table rewritten (Germany: DSK list for the non-public sector, not the BfDI; unverifiable content claims removed; the authority's own list as source, the EDPB register as index); DPO advice required on every DPIA (Art. 35(2)) with a recorded response where it is not followed; DPIA redefined as a rights-and-freedoms assessment (Art. 35(7)) using Document 18 track (a), with the legitimate interest pursued, data subjects' views (Art. 35(9)) and review (Art. 35(11)); G-36 step inserted before the decision with the statutory test evaluated for every DPIA, the controller (not the DPO) consulting, Art. 36(2) advice, information requests and Art. 58 powers, and no authorisation by elapsed period; Art. 22 module (Art. 22(2)(a)–(c) only, Art. 22(3) safeguards, Art. 15(1)(h) meaningful information, C-634/21, C-203/22); AI Act interface (Art. 26(9); FRIA under Art. 27 for Annex III point 5(b), forthcoming from 2 December 2027); single effective decider under Document 8; DPO approval and joint-decision channels removed; worked DPIAs recomputed with Document 18 (Project 2 Example 2.1-R for training data; Project 4 Example 4.3 for production scoring; Project 4 for the assistant): DPIA-CS-TRAIN-01 Medium (G-36 not met), DPIA-CS-INFER-01 and DPIA-CS-LAUNCH-01 High (G-36 met, HBDI consulted before launch, decider Chief Risk Officer, launch planned); the former DPIA naming a real AI vendor replaced by DPIA-LLM-01 (customer-service assistant, fictional Example AI Provider Inc., Processing Owner Head of Customer Service, DPO advice recorded); summaries of DPIA-PSI-01 (with the partner-input leakage assumptions of TIA-PSI-01) and DPIA-FL-01 (attack set declared; gradient-reconstruction test not applicable for the observers in scope, INCOMPLETE fallback) added; production credit scoring described as a planned design with an Art. 22(2)(a) necessity record; Art. 9 outcome for the assistant (no Art. 9(2) condition; fail-closed exclusion); cut-off for earlier authority rules 23 October 2026; scale bands aligned with Document 18; evidence-pack identifiers in EVP-YYYY-NNNN format; product names and capability claims removed; example dates shifted by −12 months and fictional history re-baselined (version 2.0 of 20 October 2026); International adaptation and references added. Integration pass: assistant inputs aligned with the example registry and Documents 16, 21 and 23 (masked message being handled and knowledge-base articles; no retrieval of customer records — tiers unchanged); RoPA-CSV-01 and RoPA-FL-01 named; further DPIAs on the register noted without identifiers or tiers |
