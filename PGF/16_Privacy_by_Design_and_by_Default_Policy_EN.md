---
title: "Privacy by Design and by Default Policy"
document_id: PGF-16
level: 2
release_version: 1.0.0-rc.1
status: release-candidate
authors: ["Alexey Neyman", "Val Khvatov"]
regulatory_reference_date: 2026-10-26
licence_proposed: "CC BY 4.0 (proposed; subject to rights-holder confirmation)"
source_provenance: "Derived from internal source set ver.2: Level2/16. Privacy-by-Design-and-by-Default-Policy_ENG.docx.md; sha256 7c6affe86b891768771fd13d45f1fa242d476c487ec8e7c2b1755748ef5a1261"
---

# PGF-16 — Privacy by Design and by Default Policy

*Privacy Governance Framework (PGF) · Level 2 — Policies and Standards · Release 1.0.0-rc.1 · Regulatory reference date: 26 October 2026*

> **Status and use.** Part A is a reusable template. Part B is a worked example for a fictional organisation (PanEuropean Bank AG); all names, figures, dates and records in Part B are illustrative. Nothing in this document is legal advice or a statement about any real organisation, product or provider.

# **About This Document**

**Purpose.** Document 16 implements data protection by design and by default (GDPR Art. 25): appropriate technical and organisational measures, designed to implement the data protection principles effectively and to integrate the necessary safeguards, both when the means of processing are determined and while the processing takes place; and defaults that process only the personal data necessary for each specific purpose.

**Scope.** New and existing (legacy) products, systems, business processes and data handovers that involve personal data, and the procurement of products, services and processors used for them. The document sets mandatory controls, design and default elements per principle, the pre-launch gate, engineering methods given as illustrations, and effectiveness indicators. A DPIA (Document 19) is one instrument within this document where Art. 35 is triggered; it is not the whole of data protection by design.

**Relationships.** Document 3 (Interface and Integration Model) — the boundary with the SDLC owner; Document 9 — tooling and the PET Standard; Document 10 — data class and data state; Document 11 — default retention, anonymity conclusions and open-data publication; Document 12 — transfers; Document 17 — procurement and processors; Document 18 — gates (Section 2.1) and the PET Assessment Module (Section 3.3); Document 19 — DPIA triage and DPIAs.

# **How to Use This Document**

Part A is a template. Text in ***[square brackets, bold italic]*** is a fill-in or illustrative placeholder. Blocks marked **Guidance** are removed from the adopted version. Part B shows the template completed for the fictional PanEuropean Bank AG. Engineering methods and standards are cited as references for the reader; they are not certification requirements and do not imply that any tool implements them.

> **Guidance.** Build on the Charter (the "privacy by design" principle) and on the Interface and Integration Model (Document 3, principles D1 and D3), which set the boundary with the SDLC owner. Use the gate wording of Section 4, item 6, exactly as stated in Document 18, Section 2.1.

# **Table of Contents**

**About This Document**
**How to Use This Document**
**Part A — Template**
1. Purpose
2. Scope
3. Status Relative to the SDLC
4. Mandatory Controls
5. Design and Default Elements per Principle
6. Illustrative Mechanisms and Engineering Methods
7. Existing (Legacy) Processing
8. Effectiveness of Measures and Indicators
9. Roles and Responsibilities
10. Relationship to Other Framework Documents
11. Review and Amendment
12. Approval
**Part B — Worked Example: PanEuropean Bank AG** (same structure)
**Normative Basis and References**
**Document History (PGF)**

# **Part A — Template**

**Privacy by Design and by Default Policy of *[Legal name of organisation]***

*Effective date: **[DD Month YYYY]**  ·  Version: **[x.x]**  ·  Document owner: **[Executive Privacy Programme Owner (EPPO)]**  ·  Adopted by: **[Executive Management]***

***Version History***

| Version | Date | Changes |
| :---- | :---- | :---- |
| ***[1.0]*** | ***[DD Month YYYY]*** | ***[First version of the document]*** |
| ***[x.x]*** | ***[DD Month YYYY]*** | ***[Brief description of material changes]*** |

## **1. Purpose**

This document establishes how the organisation embeds data protection by design and by default in its products, systems, processes and procurement, its status relative to the software development lifecycle (SDLC), the mandatory controls for higher-risk contexts, and how the effectiveness of the measures is evidenced.

## **2. Scope**

> **Guidance.** This document is a policy, not a development procedure. It does not take over the SDLC, design review or product launch, which belong to the engineering and product teams (Document 3, principle D1); it intervenes only as far as needed to implement Art. 25 and manage privacy risk (principle D3).

* ***[**Art. 25(1) — by design.** Taking into account the state of the art, the cost of implementation and the nature, scope, context and purposes of processing, as well as the risks of varying likelihood and severity for the rights and freedoms of natural persons, the organisation implements appropriate technical and organisational measures — such as pseudonymisation — designed to implement the data protection principles effectively and to integrate the necessary safeguards. The duty applies when the means of processing are determined **and** at the time of the processing itself; it is therefore continuous, not a one-off launch check.]***

* ***[**Art. 25(2) — by default.** By default, only personal data necessary for each specific purpose are processed. The obligation applies to the amount of personal data collected, the extent of their processing, the period of their storage and their accessibility; in particular, by default personal data are not made accessible without the individual's intervention to an indefinite number of natural persons.]***

* ***[**Documented trade-offs.** Each design decision record states the Art. 25(1) factors considered — state of the art, cost of implementation, nature, scope, context and purposes, and risks — and the measures chosen. Cost may influence the choice among effective measures; it never justifies omitting a measure that is necessary to implement a principle effectively (EDPB Guidelines 4/2019).]***

* ***[**Coverage.** New products, systems and features; material changes to existing processing; business-process changes without a new system; data handovers inside the organisation; existing (legacy) processing (Section 7); and the procurement of products, services and processors (Section 4, item 10). Where an approved certification mechanism under Art. 42 exists for the processing, it may be used as an element to demonstrate compliance (Art. 25(3)); it does not replace this document.]***

* ***[**Freedom of information.** Item 9 refers to freedom-of-information (FOI) requests only where an FOI regime applies to the organisation (typically public or hybrid bodies).]***

## **3. Status Relative to the SDLC**

***[The owner of the SDLC (the engineering or product function) keeps operational control of the development process. The privacy function adds the requirements of this document — early engagement, the controls of Section 4, the design and default elements of Section 5 and the pre-launch gate — without taking over that process (Document 3, principles D1 and D3).]***

> **Guidance.** An established boundary of the same type is the "profiling for personalisation" interface (Document 3, Section 3.9): the business defines the personalisation logic and owns any DPIA; Legal confirms the lawful basis; the DPO advises. The same pattern applies to every product and function in scope.

## **4. Mandatory Controls**

> **Guidance.** The baseline requirement is the pre-launch gate (item 6). The organisation may extend it with specific controls for higher-risk contexts, as in items 1–5 and 7–10; each is a specialised application of the same gates and of the risk method of Document 18, not a separate system. When adapting the template, narrow the list to the contexts relevant to the organisation, but keep item 6.

The privacy function — a Privacy Engineer, a Privacy Officer or a designated privacy champion (Section 6) — is engaged at the concept stage or during early architectural design of a new product, system or material change, before development begins, not only at the pre-launch gate. Early engagement is a condition of effective defaults: minimal collection, opt-in rather than opt-out and restricted default access can be implemented reliably and in full only when they are built into the architecture from the outset; added afterwards on top of technical decisions already made, they tend to be incomplete or easy to bypass. Early engagement does not replace or narrow the pre-launch gate; it reduces the likelihood that the gate will reveal a problem requiring rework.

1. ***[**Data handovers to product teams and Data Science.**]*** Any handover of a dataset to a product or Data Science team for development, analysis or experimentation is accompanied by a data-class and data-state check (Document 10) and uses the minimum data form necessary for the task — pseudonymised data, or synthetic data that has passed the PET Assessment Module (Document 18, Section 3.3.2), according to the PET Standard (Document 9, Section 6). Pseudonymised data remain personal data (Art. 4(5)); synthetic data remain personal data until the controller concludes otherwise (Document 10). Access to directly identifiable (non-pseudonymised) data requires a separate justification and a decision by the Processing Owner of the product or system, with DPO advice, for a fixed period.

2. ***[**Training AI.**]*** Before a machine-learning model is trained on personal data, DPIA triage (G-DPIA) covers the training dataset itself, not only the finished product: the presence of special-category data (Document 10); the lawful basis and compatibility (Art. 6(4)) of using the data for training, which may differ from the basis for collection; and the AI Act classification of the system and the organisation's role as provider and/or deployer (Document 19, Section 4.11). Excluding special-category data from training is the default, but bias detection and correction may exceptionally require them where strictly necessary and with the safeguards of AI Act Art. 10(5) — this is assessed, not excluded by rule. Whether training, inference and the product are covered by one DPIA with lifecycle modules or by separate DPIAs is an organisational choice (Art. 35(1) allows one assessment for a set of similar processing operations); each lifecycle stage must be covered.

3. ***[**Processing personal data using AI.**]*** Using an AI system (including large language models and agentic systems) to process personal data is a distinct processing activity recorded in the RoPA (Document 21) and subject to G-L and DPIA triage before launch. Particular attention is paid to the inference of attributes not present in the input, to Art. 22 permissibility and safeguards (Document 19, Section 4.10; Document 15, Section 3.5), and to AI literacy of the staff who use the system (AI Act Art. 4).

4. ***[**DWH, RAG and ECM systems.**]*** Systems that aggregate data from several sources (data warehouse, DWH), retrieve personal data and inject them into AI prompts (retrieval-augmented generation, RAG) or store unstructured content (enterprise content management, ECM) are registered in the Data Inventory (Document 23) with their data class. A combined dataset is classified at least at the highest class among its sources, and higher where aggregation increases the impact. For RAG, access control and source classification are preserved on retrieval; sending prompts to an external model provider is assessed under the Cross-Border Data Transfer Policy (Document 12) where the transfer criteria are met.

5. ***[**Embedding in business processes.**]*** The gate of item 6 applies not only to new IT systems but also to a change in a business process that affects personal data without a new system (for example, a new manual review procedure). The process owner may not treat the control as satisfied because the systems involved were assessed earlier for other purposes. For processes in automated workflows, ***[IT Management]*** implements the technical controls; for processes without automation, the process owner initiates the gate.

6. ***[**Pre-launch gate (baseline requirement).**]*** No new processing or material change is launched into production until **G-L** (legal compliance gate) and **G-DPIA** (DPIA triage) have been recorded, exactly as worded in Document 18, Section 2.1. Where triage requires a DPIA, it is completed under Document 19, DPO advice is recorded (Art. 35(2)) and **G-36** is evaluated before any acceptance; where the Art. 36 test is met, the competent supervisory authority is consulted before processing starts. Where a transfer is involved, **G-TIA** applies (Document 20). A G-L failure means stop or redesign. The gate is implemented as a pre-launch decision point on the process map (Document 24).

7. ***[**Default configuration (Art. 25(2)).**]*** By default, a new product, feature or system: collects only the fields needed for the purpose, with optional fields off (opt-in); limits the extent of processing to the stated purpose (no secondary uses switched on by default); presets the retention period to the minimum needed under the applicable rule (Document 11), not to the platform maximum; restricts access to the minimum set of users, with any extension on a justified request; and does not make personal data accessible to an indefinite number of persons without the individual's intervention (for example, public profiles, shared links or open publication are off). Interfaces do not steer users towards less protective options (EDPB Guidelines 03/2022); the most protective settings apply by default for minors.

8. ***[**Test and staging environments.**]*** Test, staging and development environments use synthetic data that have passed the PET Assessment Module (Document 18, Section 3.3.2) or masked data, under the PET Standard (Document 9, Section 6). Synthetic records are generated by a model and may still disclose information about the individuals in the source data; the checks and restrictions of Document 18 — including the unacceptable-attack gate (G-M2) and record-proximity tests such as distance to closest record — apply before use or disclosure, and no statement that a synthetic dataset contains no source records is made except for a tested artefact, with its scope and evidence. Using production personal data in a test environment is an exception, decided by the Processing Owner of the system with DPO advice, for a fixed period and with deletion at the end.

9. ***[**Open data and freedom of information.**]*** Publishing data on the organisation's own initiative and disclosing data in response to FOI requests (where an FOI regime applies) can make data available irrevocably to an unlimited audience — the accessibility limb of Art. 25(2). A release of statistics or other information derived from personal data proceeds only where: (a) G-L passes; (b) the PET Assessment Module of Document 18 (Section 3.3.4 for aggregate releases) passes with "anyone" as the recipient; and (c) the controller has concluded that the released information is anonymous information (Recital 26) — a conclusion taken by the Processing Owner on Legal's assessment, with DPO advice, and re-assessed periodically (Document 11, Section 3.4). There is no universal rule that a given attribute can never appear in anonymous statistics: an attribute within information that is effectively anonymous is not, as such, special-category personal data; a release that would disclose identifiable special-category data without an applicable Art. 9(2) condition fails G-L; and the organisation may adopt a stricter internal policy excluding special-category attributes from open releases (enforced through the prohibited-attribute gate G-M3 of Document 18), labelled as internal policy. For FOI disclosures, the decision to disclose a third party's personal data contained in a requested document is taken by the owner of the FOI process on Legal's assessment, with DPO advice.

10. ***[**Procurement of products, services and processors.**]*** Products, services and processors are chosen with regard to their ability to support data protection by design and by default (Recital 78; EDPB Guidelines 4/2019): configurable minimisation and retention, protective defaults, access control, logging, deletion and export. The criterion is part of vendor due diligence (Document 17, Section 4).

## **5. Design and Default Elements per Principle**

> **Guidance.** EDPB Guidelines 4/2019 (version 2.0) set out key design and default elements for each principle of Art. 5. Use the table as a checklist in design reviews and record which elements apply and how they are evidenced. The elements are examples; the measures must be appropriate to the processing.

| Principle (Art. 5) | Key design and default elements (examples) | Typical evidence |
| :---- | :---- | :---- |
| ***[Lawfulness]*** | ***[Lawful basis identified before design; processing limited to what the basis allows; consent and withdrawal built in where consent is the basis (Document 13)]*** | ***[G-L record]*** |
| ***[Fairness]*** | ***[No deceptive design; respect for reasonable expectations; human intervention where decisions affect people; non-discrimination testing of models; no exploitation of vulnerability]*** | ***[UX review; bias-test results]*** |
| ***[Transparency]*** | ***[Information at the right point in the user journey, layered, in clear language; explanation of automated decisions (Document 15)]*** | ***[Notice versions; screenshots]*** |
| ***[Purpose limitation]*** | ***[Purpose binding in data platforms; compatibility assessment before re-use (Art. 6(4)); separation of datasets by purpose]*** | ***[Purpose tags; compatibility records]*** |
| ***[Data minimisation]*** | ***[Only necessary fields; pseudonymisation or aggregation as early as possible; minimum data form for handovers (Section 4, item 1)]*** | ***[Field-level justification; data-flow map]*** |
| ***[Accuracy]*** | ***[Validation at entry; correction paths; data-quality monitoring of inputs to decisions]*** | ***[Data-quality metrics]*** |
| ***[Storage limitation]*** | ***[Retention configured at design; automated disposal; erasure cascade to derived data (Document 11)]*** | ***[Retention settings; disposal log]*** |
| ***[Integrity and confidentiality]*** | ***[Access control by default, encryption, logging, segregation of environments, tested incident response (Document 14)]*** | ***[Security test results]*** |
| ***[Accountability]*** | ***[Design decisions, trade-offs and gate outcomes recorded and retrievable; effectiveness indicators (Section 8)]*** | ***[Design decision records; evidence packs]*** |

## **6. Illustrative Mechanisms and Engineering Methods**

> **Guidance.** This section is a non-binding list of examples, not a mandatory minimum. Each team may choose its mechanism, provided the controls of Section 4 and the elements of Section 5 are met. The methods below are cited bibliographically; they are engineering guidance, not certification schemes, and their use does not by itself demonstrate compliance.

* ***[**Privacy design intake** — a point of contact with a Privacy Engineer at the terms-of-reference or architecture stage, before development; it does not replace the pre-launch gate.]***
* ***[**Design review gate** — a privacy checklist (Section 5) confirmed before moving to development.]***
* ***[**Privacy champion** — a team member with basic privacy training who is the first point of contact for Section 4 questions; does not replace the privacy function or the DPO's advice.]***
* ***[**Automated checks in CI/CD** — for example, scanning test configurations and logs for personal data and checking default access settings.]***
* ***[**Privacy threat modelling** — systematic identification of privacy threats in the data-flow design (for example, linkability, identifiability, non-repudiation, detectability, disclosure, unawareness and non-compliance threat categories), feeding the harm scenarios of Document 18.]***
* ***[**Engineering strategies and techniques** — data-oriented strategies (minimise, separate, abstract, hide) and process-oriented strategies (inform, control, enforce, demonstrate), and techniques such as pseudonymisation, anonymisation, data masking, privacy-enhancing computation and user-side controls, as described in ENISA, *Data Protection Engineering* (2022).]***
* ***[**Privacy engineering objectives** — predictability, manageability and disassociability as design objectives alongside security objectives, and the analysis of problematic data actions (NIST IR 8062, 2017).]***
* ***[**Consumer products** — privacy by design requirements across the lifecycle of consumer goods and services, including consumer communication, privacy controls and preferences, and end of life (ISO 31700-1:2023).]***
* ***[**Privacy requirements in user stories and acceptance tests** — each story touching personal data carries its purpose, data fields, retention and access rules; acceptance tests verify them.]***

## **7. Existing (Legacy) Processing**

***[Art. 25 applies to processing that already exists, not only to new processing (EDPB Guidelines 4/2019). The organisation keeps a risk-based plan to review existing processing against Sections 4 and 5, starting with systems holding the highest data classes or supporting decisions about individuals. Gaps are recorded with an owner and remediation date; where a gap means that a principle is not implemented effectively, the remediation is prioritised, and where it is a G-L failure, the processing is stopped or redesigned. Material changes to legacy processing pass the pre-launch gate (Section 4, item 6).]***

## **8. Effectiveness of Measures and Indicators**

> **Guidance.** EDPB Guidelines 4/2019 require that measures be effective and that the controller can demonstrate it. State each indicator with its denominator, how zero cases are reported and the cut-off rule, following the metric conventions of the Privacy Metrics Dashboard (Document 28). A statutory duty missed in a single case is escalated even if an aggregate indicator is green.

| Indicator | Definition (denominator; zero cases; cut-off) | Target |
| :---- | :---- | :---- |
| ***[Gate coverage]*** | ***[Launches and material changes in the period with G-L and G-DPIA recorded before go-live ÷ all launches and material changes in the period; "none in period" reported as such; cut-off: go-live date]*** | ***[100%]*** |
| ***[Early engagement]*** | ***[Projects with a privacy design intake before development ÷ projects starting development in the period]*** | ***[≥ X%]*** |
| ***[Defaults changed after launch]*** | ***[Number of default settings made more protective after launch because of a finding (indicator of design gaps)]*** | ***[Trend down]*** |
| ***[Minimum-form handovers]*** | ***[Data handovers to product or Data Science teams in pseudonymised or tested synthetic form ÷ all handovers]*** | ***[≥ X%]*** |
| ***[Production data in test]*** | ***[Open exceptions for production data in test environments; exceptions past their expiry]*** | ***[0 past expiry]*** |
| ***[Legacy review coverage]*** | ***[Systems reviewed under Section 7 ÷ systems in the review plan for the period]*** | ***[Per plan]*** |
| ***[Findings closure]*** | ***[Design-related audit or incident findings closed by their due date ÷ findings due in the period]*** | ***[≥ X%]*** |

## **9. Roles and Responsibilities**

| Role | Responsibility |
| :---- | :---- |
| ***[Processing Owner]*** | ***[Accountable for applying this document to its processing: design decisions and trade-offs, the gate outcomes, DPIA ownership where required, exceptions for identifiable data or production data in test, and anonymity conclusions on Legal's assessment]*** |
| ***[Engineering / product teams]*** | ***[Own the SDLC and the embedding mechanism (Section 6); implement the controls of Section 4 before launch]*** |
| ***[Privacy Operations Lead]*** | ***[Runs triage tracking and the effectiveness indicators; owns Document 18 calculations]*** |
| ***[Privacy Engineer(s)]*** | ***[Apply PETs (Document 9); take part in design reviews and threat modelling]*** |
| ***[Data Science / AI]*** | ***[Implement items 1–3 for model training and use]*** |
| ***[AI governance / model-risk function]*** | ***[AI Act classification and provider/deployer duties; bias testing; model validation (Document 3, Section 3.5)]*** |
| ***[IT Management]*** | ***[Implements default configurations, segregation of test environments and controls in automated workflows (items 5, 7, 8)]*** |
| ***[Data Governance (CDO)]*** | ***[Registers DWH, RAG and ECM systems and their class in the Data Inventory (item 4); initiates open-data releases (item 9)]*** |
| ***[Legal]*** | ***[G-L; identifiability assessment for anonymity conclusions; FOI assessments]*** |
| ***[DPO]*** | ***[Advises on design, on DPIAs (Art. 35(2)), on exceptions and on anonymity conclusions; monitors compliance. Does not approve DPIA outcomes, decide exceptions or take anonymity conclusions]*** |
| ***[EPPO]*** | ***[Owns this document and the legacy review plan]*** |

## **10. Relationship to Other Framework Documents**

* Relies on the Charter — the "privacy by design" principle, operationalised here.
* Relies on the Interface and Integration Model (Document 3, principles D1 and D3; Sections 3.5 and 3.9).
* Relies on the Privacy Automation and Tooling Strategy (Document 9, Section 6) — the PET Standard.
* Relies on the Data Classification Policy (Document 10) — data class and data state.
* Interacts with the Data Retention and Disposal Policy (Document 11) — default retention; anonymity conclusions (Section 3.1); synthetic datasets (Section 3.2); open-data publication (Section 3.4).
* Interacts with the Cross-Border Data Transfer Policy (Document 12) — external model providers and remote access.
* Interacts with the Consent Management Policy (Document 13) — consent and withdrawal by design.
* Interacts with the Data Subject Rights Policy (Document 15) — rights by design, including Art. 22 safeguards.
* Interacts with the Vendor and Third-Party Privacy Risk Policy (Document 17) — procurement criterion (item 10).
* Relies on the Privacy Risk Assessment Methodology (Document 18) — gates (Section 2.1), PET Assessment Module (Section 3.3) and risk calculation.
* Relies on the DPIA Methodology (Document 19) — triage, DPIA, Art. 22 module and AI Act interface.
* Documented in the RoPA (Document 21) and the Data Inventory (Document 23); executed as a pre-launch decision gate on the process map (Document 24).
* Feeds the Privacy Metrics Dashboard (Document 28) with the indicators of Section 8; training of privacy champions — Document 30.

## **11. Review and Amendment**

This document is reviewed under ***[the Policy Review Cycle, Document 29]*** and whenever new categories of technology (for example, new classes of AI systems) or new guidance on Art. 25 emerge. Changes are adopted by ***[Executive Management]*** on the proposal of ***[the EPPO]***, after the DPO's advice.

## **12. Approval**

This document was adopted by ***[Executive Management]*** on ***[date]***. Document owner: ***[EPPO]***.

# **Part B — Worked Example: PanEuropean Bank AG**

**PanEuropean Bank AG — Privacy by Design and by Default Policy**

*Effective date: 20 October 2026  ·  Version: 2.0  ·  Document owner: Chief Privacy Officer (EPPO)  ·  Adopted by: Management Board, 20 October 2026*

*Fictional legal entity, provided solely for illustrative purposes.*

***Fictional Document History (illustrative)***

| Version | Date | Changes |
| :---- | :---- | :---- |
| 1.0 | 1 March 2026 | First version. Owner at the time: Group DPO |
| 2.0 | 20 October 2026 | Re-baselined to the new role model (Chief Privacy Officer as owner; Processing Owners decide exceptions and anonymity conclusions on General Counsel's assessment; Group DPO advice only); pre-launch gate restated as G-L plus G-DPIA triage; design and default elements per principle, legacy review plan and effectiveness indicators added; synthetic data treated as personal data until a conclusion; open-data rules aligned with Document 11; the customer-service assistant described as the AI use case, with its transfer on hold since 26 October 2026 |

## **1. Purpose**

This document implements data protection by design and by default for all PanEuropean Bank AG products, systems and processes that involve personal data — from credit scoring and fraud prevention to marketing personalisation and the customer-service assistant.

## **2. Scope**

All entities and branches of PanEuropean Bank AG in its five countries of presence; all customer-facing products (app, online banking, branches, contact centre), internal systems (core banking platform, customer-relationship system, data warehouse, document management, the Bank's privacy engineering platform (PEP, illustrative)), business processes and data handovers; existing processing under the legacy review plan (Section 7); and procurement through Document 17. No FOI regime applies to PanEuropean as a private bank; item 9 therefore covers only open-data releases on its own initiative.

## **3. Status Relative to the SDLC**

The SDLC of the Digital Banking, Card Services and Retail Lending product and engineering teams remains under their operational ownership (Document 3, principles D1 and D3). An established boundary of this type (Document 3, Section 3.9): the Head of Digital Banking defines the business logic of the personalised-offers pilot and owns its assessment; General Counsel confirms the lawful basis; the Group DPO advises. The same pattern applies to the credit-scoring model: Credit Decisions and Data Science define the model's architecture, the Model Risk and AI Governance function validates it and tests it for bias, the Head of Credit Decisions decides on the use of specific features as Processing Owner, and the Group DPO advises.

## **4. Mandatory Controls**

A Privacy Engineer or the team's privacy champion (Section 6) is engaged at the concept stage of every new application feature and every material change, before architectural design begins, separately from the pre-launch gate.

***1. Data handovers to product teams and Data Science***

By default, Data Science receives customer data for developing and calibrating scoring models only as pseudonymised data (direct identifiers replaced by tokens, which remain personal data) or as synthetic data generated on PEP with a differentially private generator and tested in the PET Assessment Module — for the credit-scoring model, the synthetic calibration dataset of DPIA-CS-TRAIN-01 (Document 18, Example 2.1-R: module PASS), classified Restricted / personal data, data state "synthetic" (Document 10). Access to directly identifiable data to debug a specific anomaly is an exception decided by the Head of Credit Decisions with Group DPO advice, for at most 10 business days (illustrative internal value), and logged.

***2. Training AI***

The calibration of the credit-scoring model is covered by DPIA-CS-TRAIN-01 — track (a) Medium; decided on 25 March 2026 by the Head of Credit Decisions with Group DPO advice; conditional acceptance expiring on 25 March 2027 or at the next calibration (Document 19). The DPIA covers EuroCredit Bureau data in the source (obtained from an independent controller, so the basis and compatibility for model development were checked separately from the basis of collection); the exclusion of health and other special-category data from model features (Document 1, Section 8); and the AI Act classification — a high-risk system under Annex III, point 5(b), for which PanEuropean is provider as well as deployer, with high-risk obligations applying from 2 December 2027 (Document 7). Whether bias detection requires special-category data under AI Act Art. 10(5) is assessed by the Model Risk and AI Governance function with General Counsel; at present no special-category data are used, and bias testing works on documented proxies. As an organisational choice, PanEuropean covers the credit-scoring lifecycle by three DPIAs — training (DPIA-CS-TRAIN-01), inference (DPIA-CS-INFER-01) and product launch (DPIA-CS-LAUNCH-01) — rather than one DPIA with modules.

***3. Processing personal data using AI***

* **Automated credit scoring (planned).** DPIA-CS-INFER-01 and DPIA-CS-LAUNCH-01: track (a) High; the Art. 36 test was met, and the prior consultation of the HBDI was submitted on 15 September 2026 and is pending; the Chief Risk Officer's decision is pending; production launch is planned for 1 February 2027, not before the consultation step and the decision. At 26 October 2026, credit decisions are taken by credit staff. The Art. 22(2)(a) necessity record and the "Request a Review" safeguards are in DPIA-CS-INFER-01 (Document 19, Section 4.10) and Document 15, Section 3.5.
* **Customer-service assistant.** The assistant summarises incoming chat and e-mail messages for customer-service agents and drafts reply suggestions that an agent reviews, edits and sends; it uses a large language model of Example AI Provider Inc. (fictional, United States), a processor. Processing Owner: Head of Customer Service. Design measures: masking of account, card and national identification numbers before sending; a fail-closed special-category detector, whose false-negative threshold is a validation and escalation metric, not a legal tolerance — detected cases are blocked and investigated at once; an agent reviews every reply; deletion of prompts and outputs at the provider within 30 days and no training on customer data (illustrative contractual terms, Document 17). DPIA-LLM-01 assessed track (a) as Medium. **Status at 26 October 2026:** the G-TIA pass of TIA-LLM-01 (22 June 2026) is historical; the current re-evaluation is incomplete, so the transfer is on hold — the AI path is suspended under SCC Clause 14(f), customer service in the EU channel is handled by agents without the assistant, and the acceptance under DPIA-LLM-01 is not in effect until a current G-TIA pass is recorded (Document 12, Section 5; Document 20). Staff who use the assistant when it resumes receive AI literacy training (AI Act Art. 4; Document 30).
* **Federated-learning anti-fraud consortium.** Recorded in the RoPA as processing under an Art. 26 arrangement (Document 12, Section 3); DPIA-FL-01: track (a) Medium.

***4. DWH, RAG and ECM systems***

PanEuropean's analytical data warehouse, which combines data from Retail Lending, Card Services and Digital Banking, is registered in the Data Inventory (Document 23) separately from its sources and classified **Restricted** — at least the highest class among its sources (credit-scoring data are Restricted, Document 10), with no downgrade. The customer-service assistant (currently suspended, item 3) does not retrieve customer records from the warehouse or other systems: by design it receives only the masked message being handled and articles from the internal knowledge base; any extension to retrieval of customer records would require a new DPIA module under DPIA-LLM-01 and re-evaluation of TIA-LLM-01. The Legal & Compliance document-management system, which stores scans of credit agreements and customer due-diligence documents, is registered separately and classified Restricted, with access limited to Legal and Compliance roles.

***5. Embedding in business processes***

In the planned credit-decision process, the routing of borderline-band scores to credit officers for a decision before effect, and the "Request a Review" human-review process, were assessed as separate business-process scenarios within DPIA-CS-INFER-01, although the core banking platform had been assessed earlier for other purposes: human handling widens the circle of staff with access to the rationale of decisions, so access is limited to authorised credit officers and logged.

***6. Pre-launch gate***

No new product, process or material change involving personal data goes into production until G-L and G-DPIA triage are recorded (Document 18, Section 2.1); where triage requires a DPIA, it is completed under Document 19, Group DPO advice is recorded and G-36 is evaluated before the decision. Examples: the personalised-offers pilot — G-L confirmed, one WP248 criterion, no DPIA required, track (a) Low (Document 18, Example 4.1); remote technical support by Example Cloud Services Pvt Ltd — no DPIA required (one criterion), G-TIA passed for the restricted design (TIA-CLOUD-01, Document 20). The gate is a pre-launch decision point on PanEuropean's process map (Document 24).

***7. Default configuration***

* Marketing consent and personalised offers are off when an account is opened; opt-in requires a separate action (Document 13).
* The app's marketing and personalisation features are off for every user under 16 (internal design choice, Document 7).
* Biometric log-in is off by default; the template is created and stored only on the customer's device, and a PIN or password log-in is always available (Document 10, Section 4.5).
* Retention for new data categories is preset to the minimum under the applicable rule in the retention matrix (Document 11), not to the platform maximum.
* Retail Lending staff see a customer's full credit history only for customers in their own portfolio; wider access requires a justified request through the Data Owner.
* No customer data are published or shared by link by default; the open-data portal publishes only releases passing item 9.

***8. Test and staging environments***

Development and test environments for scoring models use the synthetic calibration dataset and other synthetic or masked datasets that passed the PET Assessment Module; synthetic datasets are personal data at PanEuropean and are handled as Restricted (Document 10; Document 11, Section 3.2). Real customer data in a test environment are permitted only to reproduce a specific production incident, on a decision by the Processing Owner of the system with Group DPO advice, for at most 10 business days (illustrative internal value), with deletion confirmed at the end.

***9. Open data***

PanEuropean's only open-data initiative is the publication of aggregated credit-portfolio statistics (Document 11, Section 3.4). The permissible release of Document 18, Example 3.1 passed G-L and the PET Assessment Module (likelihood Low, severity Significant, residual Medium) and is published on the Processing Owner's conclusion that it is anonymous information, taken on Legal & Compliance's assessment with "anyone" as the recipient and with Group DPO advice, and re-assessed annually and before every further release. Example 3.2 failed the module and was not published. Example 3.3 was blocked at G-L on its facts — a late cross-tabulation would have disclosed identifiable health-related information (PPI status) with no Art. 9(2) condition, no notice and no necessity — not on a universal rule; in addition, PanEuropean's **internal policy** (stricter than the legal test) excludes health-related and other special-category attributes from every open release, enforced through G-M3. Document 14 (Part B, Section 2, Example 3) uses the permissible release as a tabletop incident scenario.

***10. Procurement***

Document 17 due diligence includes the data-protection-by-design criterion of Part A, item 10. For the customer-service assistant, it covered configurable retention at the provider, the exclusion of customer data from model training, data-residency options and the availability of deletion confirmations.

## **5. Design and Default Elements per Principle**

The Part A table is used as the design-review checklist in Digital Banking, Card Services and Retail Lending. Examples of PanEuropean elements: purpose binding on PEP that prevents re-use of scoring data for marketing (purpose limitation; DPIA-CS-INFER-01); field-level justification for every new app form (minimisation); the CMS as the single consent source (lawfulness; Document 13); retention presets and monthly disposal runs (storage limitation; Document 11); explanation of credit decisions through "Request a Review" (transparency and fairness; Document 15); and design decision records filed with the evidence pack of each assessment (accountability).

## **6. Illustrative Mechanisms and Engineering Methods**

At the terms-of-reference stage of any new application feature, Digital Banking involves a Privacy Engineer before architectural design begins, separately from the design-review gate. A privacy checklist based on Section 5 is confirmed at the design-review gate. Each Digital Banking product team has a privacy champion who has completed basic privacy training (Document 30). The CI/CD pipeline scans test configurations and logs for personal data. For new data flows involving AI or external providers, Privacy Engineers run a privacy threat-modelling session using the threat categories listed in Part A, and the resulting harm scenarios feed the Document 18 calculation.

## **7. Existing (Legacy) Processing**

The Chief Privacy Officer adopted a legacy review plan on 20 October 2026 (illustrative). The first cycle covers systems holding Restricted data or supporting decisions about customers — the core banking platform, the card systems, the customer-relationship system and the data warehouse — and is planned for completion by 31 December 2027 (planned). Each review records gaps against Sections 4 and 5 with an owner and remediation date in the Privacy Risk Register (Document 22) or, for compliance gaps, in the issues log (Document 27).

## **8. Effectiveness of Measures and Indicators**

PanEuropean reports the Part A indicators quarterly in the Privacy Metrics Dashboard (Document 28), with the targets: gate coverage 100% (each launch without a recorded gate is escalated individually); early engagement at least 90%; minimum-form handovers at least 95%; no production-data exception past its expiry; legacy review coverage per plan; design-related findings closed by their due date at least 90% (illustrative internal targets). The first full quarter of reporting under version 2.0 is the fourth quarter of 2026 (planned).

## **9. Roles and Responsibilities**

| Role | Responsibility |
| :---- | :---- |
| Processing Owners (Head of Credit Decisions; Head of Digital Banking; Head of Customer Service; Head of Fraud Prevention; CIO for IT-operated processing; the Processing Owner for the open-data publication) | Apply this document to their processing; decide exceptions for identifiable data or production data in test, with Group DPO advice; own DPIAs; take anonymity conclusions on General Counsel's assessment |
| Digital Banking / Card Services / Retail Lending (engineering) | Own the SDLC and the embedding mechanism; implement Section 4 controls before launch |
| Privacy Operations Lead | Tracks triage and the Section 8 indicators; owns Document 18 calculations |
| Privacy Engineer(s) | Apply PETs on PEP; take part in design reviews and threat modelling |
| Data Science / Credit Decisions | Implement items 1–3 for credit scoring and anti-fraud |
| Model Risk and AI Governance function | AI Act classification and provider/deployer duties; bias testing; model validation |
| IT Management | Implements default configurations, segregation of test environments and controls in automated routing (items 5, 7, 8) |
| Data Governance (CDO) | Registers the warehouse and the document-management system in the Data Inventory; initiates open-data releases |
| General Counsel (Legal & Compliance) | G-L; identifiability assessments for anonymity conclusions |
| Group DPO | Advises on design, DPIAs, exceptions and anonymity conclusions; monitors compliance |
| Chief Privacy Officer (EPPO) | Owns this document and the legacy review plan |

## **10. Relationship to Other Framework Documents**

* Relies on the Charter and PanEuropean's Interface and Integration Model (Document 3, Sections 3.5 and 3.9).
* Relies on Document 9 (PEP, the PET Standard) and Document 10 (Restricted class of the warehouse and synthetic datasets; biometric template).
* Interacts with Document 11 (retention presets; synthetic datasets; open-data publication), Document 12 (the assistant's provider; federated learning), Document 13 (consent off by default), Document 14 (Example 3 tabletop scenario), Document 15 (Request a Review), Document 17 (procurement criterion; the assistant's provider) and Document 1 (planned automated credit decisions).
* Relies on Document 18 (Examples 2.1-R, 3.1–3.3, 4.1) and Document 19 (DPIA-CS-TRAIN-01, DPIA-CS-INFER-01, DPIA-CS-LAUNCH-01, DPIA-LLM-01, DPIA-FL-01).
* Documented in the RoPA (Document 21) and the Data Inventory (Document 23); executed as a pre-launch gate (Document 24); indicators in Document 28; training in Document 30; review cycle in Document 29.

## **11. Review and Amendment**

This document is reviewed under PanEuropean's Policy Review Cycle (Document 29), whenever new categories of technology emerge that are not covered by Section 4, before the planned launch of automated credit decisions, and on completion of the first legacy review cycle. Changes are adopted by the Management Board on the Chief Privacy Officer's proposal, after Group DPO advice.

## **12. Approval**

Version 1.0 (1 March 2026) was adopted by the Management Board; the Group DPO was document owner at that time. Version 2.0 was adopted by the Management Board on 20 October 2026 on the Chief Privacy Officer's proposal, after Group DPO advice. Document owner: Chief Privacy Officer.

# **Normative Basis and References**

* Regulation (EU) 2016/679 (GDPR): Arts. 4(5), 5, 6(4), 9(2), 22, 25(1)–(3), 35, 36, 42; Recitals 26 and 78.
* EDPB Guidelines 4/2019 on Article 25 Data Protection by Design and by Default, version 2.0 (adopted 20 October 2020).
* EDPB Guidelines 03/2022 on deceptive design patterns in social media platform interfaces, version 2.0.
* EDPB Guidelines 01/2025 on pseudonymisation; Article 29 Working Party Opinion 05/2014 on anonymisation techniques (WP216); EDPB Guidelines 02/2026 on anonymisation — public-consultation draft (July 2026), not final.
* ENISA, *Data Protection Engineering* (2022) — engineering guidance, not certification.
* NIST IR 8062, *An Introduction to Privacy Engineering and Risk Management in Federal Systems* (January 2017).
* ISO 31700-1:2023, *Consumer protection — Privacy by design for consumer goods and services — Part 1: High-level requirements* (voluntary standard).
* NIST SP 800-226, *Guidelines for Evaluating Differential Privacy Guarantees* (final, March 2025).
* Regulation (EU) 2024/1689 (AI Act), as amended by the AI Omnibus: Art. 4 (AI literacy), Art. 10(5), Annex III point 5(b); high-risk obligations for Annex III systems apply from 2 December 2027.
* Québec: Act respecting the protection of personal information in the private sector (P-39.1) — confidentiality by default for technological products or services offered to the public (see Document 13, International Adaptation).

# **Document History (PGF)**

| Release | Date | Changes |
| :---- | :---- | :---- |
| 1.0.0-rc.1 | 2026-10-26 | Canonical English Markdown; changes from internal ver.2: Art. 25(1) factors (state of the art, cost, nature, scope, context, purposes, risks) and the continuing "time of processing" duty added, with documented trade-offs; Art. 25(2) completed (extent of processing; accessibility limb); Art. 25(3) certification noted; PbD no longer reduced to a DPIA — the pre-launch gate restated as G-L plus G-DPIA triage per Document 18, Section 2.1, with a DPIA, DPO advice and G-36 where triage requires; EDPB Guidelines 4/2019 design and default elements per principle, a legacy-processing section and effectiveness indicators (with denominators and zero-case rules) added; illustrative engineering methods citing ENISA *Data Protection Engineering* (2022), NIST IR 8062 and ISO 31700-1:2023 (bibliographic, not certification); the "non-anonymised versus pseudonymised" error corrected (access to directly identifiable data); synthetic data treated as personal data until a controller conclusion, with the W2-02 rule on statements about source records; three-DPIA rule labelled as an organisational choice; AI Act provider/deployer role, Art. 10(5) bias-detection exception and Art. 4 AI literacy added; DWH classification corrected to at least the highest source class; open-data rules aligned with Documents 11 and 18 (G-L, PET module PASS, anonymity conclusion by the Processing Owner on Legal's assessment with DPO advice; no universal attribute ban; the special-category exclusion labelled as internal policy, G-M3); FOI marked as applicable only where an FOI regime applies; procurement criterion (Recital 78) added; DPO approvals and "non-delegable proportionality decisions" replaced by Processing Owner decisions with DPO advice; Part B aligned with the canonical cases (DPIA-CS-TRAIN-01 Medium; credit scoring planned with the HBDI consultation pending; the customer-service assistant of Example AI Provider Inc. in place of the internal-staff LLM use, with its transfer on hold and the DPIA-LLM-01 acceptance not in effect at the reference date; real-vendor terms removed); adoption moved to Executive Management; example dates shifted by −12 months; Normative basis added |
