---
title: "Record of Processing Activities"
document_id: PGF-21
level: 2
release_version: 1.0.0-rc.1
status: release-candidate
authors: ["Alexey Neyman", "Val Khvatov"]
regulatory_reference_date: 2026-10-26
licence_proposed: "CC BY 4.0 (proposed; subject to rights-holder confirmation)"
source_provenance: "Derived from internal source set ver.2: Level2/21. Record-of-Processing-Activities_ENG.docx.md; sha256 24fdaa8d3b0121d9c9479e944e2f3acce293c29051f07f80babe66b6ff3e5f5a"
---

# PGF-21 — Record of Processing Activities

*Privacy Governance Framework (PGF) · Level 2 — Policies and Standards · Release 1.0.0-rc.1 · Regulatory reference date: 26 October 2026*

> **Status and use.** Part A is a reusable template. Part B is a worked example for a fictional organisation (PanEuropean Bank AG); all names, figures, dates and records in Part B are illustrative. Nothing in this document is legal advice or a statement about any real organisation, product or provider.

# **About This Document**

**Purpose.** Document 21 defines the record of processing activities (RoPA) required by Art. 30 GDPR: the fields of a controller record (Art. 30(1)) and of a processor record (Art. 30(2)), the lifecycle of a record, and the demarcation from the Data Inventory and Data Flow Maps (Document 23). The RoPA records every processing activity of the organisation, not only those that need a DPIA or a TIA.

**Scope.** All processing activities of the organisation as controller, as joint controller and, where the organisation acts for a client, as processor. The RoPA describes processing activities; it is not a log of individual requests, consents or incidents. Those have their own records: the rights-request log (Document 15), the consent management system (Document 13) and the breach record (Document 14).

**Relationships.** DPIA outcomes (Document 19), TIA outcomes (Document 20) and risk decisions recorded in the Privacy Risk Register (Document 22) are referenced from the record, not reproduced in it. The data class and data state come from the Data Classification Policy (Document 10); retention from the Data Retention and Disposal Policy (Document 11); transfer mechanisms from the Cross-Border Data Transfer Policy (Document 12). Roles follow the RACI Matrix (Document 5, row S4). The register is maintained under supporting process S4 of the Privacy Governance Process Map (Document 24).

# **How to Use This Document**

Part A is a template. Text in ***[square brackets, bold italic]*** is a fillable or illustrative placeholder. Blocks marked **Guidance** explain what the section should contain and are removed from the adopted version. Part B shows the template completed for the fictional PanEuropean Bank AG, with an excerpt of the register and three fully expanded records: a controller record linked to a DPIA, a controller record that carries an Art. 9 legal conclusion, and a processor record under Art. 30(2).

> **Guidance.** Build the register from the DPIA and TIA methodologies (Documents 19 and 20) and the Data Classification Policy (Document 10). The register records the results of those documents; it does not repeat their logic or recalculate risk. A residual-risk tier appears in a record only as a reference to the decision that set it.

# **Table of Contents**

**About This Document**
**How to Use This Document**
**Part A — Template**
Glossary of Terms
1. Purpose
2. Scope of Application
3. Record Structure (3.1 Controller Record; 3.2 Processor Record; 3.3 Supplementary Fields)
4. Record Lifecycle
5. Demarcation from the Data Inventory
6. Roles and Responsibilities
7. Relationship to Other Framework Documents
8. Review and Amendment
9. Approval
**Part B — Worked Example (fictional): PanEuropean Bank AG** (same structure)
**Appendix to Part B — Register Excerpt and Fully Expanded Records**
**Normative Basis and References**
**International Adaptation**
**Document History (PGF)**

# **Part A — Template**

**Record of Processing Activities (RoPA) of *[Legal name of the organisation]***

*Effective date: **[DD Month YYYY]** · Version: **[x.x]** · Document owner: **[EPPO]** · Adopted by: **[Executive Management]***

***Version History***

| Version | Date | Changes |
| :---- | :---- | :---- |
| ***[1.0]*** | ***[DD.MM.YYYY]*** | ***[First version of the document]*** |
| ***[x.x]*** | ***[DD.MM.YYYY]*** | ***[Brief description of material changes]*** |

## **Glossary of Terms**

*This table lists only terms defined by this document itself; terms used here but defined in another document are not repeated in this table.*

| Term | Definition / Reference |
| :---- | :---- |
| RoPA (Record of Processing Activities) | The register of processing activities maintained under Art. 30 GDPR (and equivalent requirements of other applicable regimes); its structure, mandatory fields and maintenance procedure are established by this document. |
| Processing activity | A set of processing operations serving one purpose or a closely related set of purposes, under one lawful basis per purpose and one Processing Owner; the unit of registration in the RoPA. |
| Controller record / processor record | A record kept by the organisation as controller (Art. 30(1)) or as processor for a client controller (Art. 30(2)). |

## **1. Purpose**

This document establishes the structure, maintenance procedure and lifecycle of the register of processing activities required by Art. 30 GDPR ***[or the equivalent requirement of the applicable regime]***. It defines the mandatory fields of a controller record and of a processor record, the events that create, update, review and archive a record, the roles that maintain the register, and the demarcation from the Data Inventory (Document 23).

This document does not assess the risk of a processing activity. That is the task of the DPIA Methodology (Document 19), the TIA Methodology (Document 20) and the Privacy Risk Assessment Methodology (Document 18); their results are referenced in the record and are not recalculated here.

## **2. Scope of Application**

* ***[This document applies to every processing activity of the organisation as controller or joint controller, and to every processing activity it carries out as processor on behalf of a client controller. A separate set of mandatory fields applies to each role (Sections 3.1 and 3.2); where the organisation is both controller and processor for different activities, it keeps both kinds of record and distinguishes them activity by activity.]***

* ***[Every processing activity is registered, whether or not it requires a DPIA (Document 19) or a TIA (Document 20). Those methodologies apply to a subset of activities; the register covers all of them.]***

* ***[The register is kept in writing, including in electronic form (Art. 30(3)). It is made available to the competent supervisory authority on request (Art. 30(4)); the role responsible for providing it is [the Privacy Operations Lead], with [the DPO] informed as the supervisory authority's contact point.]***

* ***[Art. 30(5) derogation. The obligation does not apply to an enterprise or organisation employing fewer than 250 persons unless the processing it carries out is likely to result in a risk to the rights and freedoms of data subjects, the processing is not occasional, or the processing includes special categories of data (Art. 9(1)) or personal data relating to criminal convictions and offences (Art. 10). Because regular processing of customer or employee data is rarely occasional, the derogation seldom removes the obligation for the processing that matters most (Article 29 Working Party position paper on the Art. 30(5) derogations, endorsed by the EDPB). Where the derogation applies only in part, records are kept for the processing that falls outside it.]***

* ***[Proposals to widen the Art. 30(5) derogation form part of the EU simplification ("omnibus") proposals, including the Digital Omnibus. They are proposals, not law: at the regulatory reference date the Council has agreed its negotiating mandate on the Digital Omnibus (21 October 2026) and negotiations with the European Parliament are pending. The current Art. 30(5) applies until an amendment is adopted and applicable.]***

* ***[This document does not replace the Data Inventory (Document 23) for the technical description of systems and data flows. Each register is authoritative within its own domain (Section 5).]***

## **3. Record Structure**

> **Guidance.** The fields in Sections 3.1 and 3.2 are the mandatory minimum, mapped to Art. 30(1) and Art. 30(2). The organisation may add industry- or jurisdiction-specific fields but may not omit those listed. Where a field does not apply, write "not applicable" with the reason (for example "no representative — established in the EU"), never leave it blank.

***3.1 Controller Record (Art. 30(1))***

| Record Field | Art. 30(1) | Content |
| :---- | :---- | :---- |
| Identifier and Name of the Processing Activity | — | ***[Unique record number (RoPA-…); short name of the activity]*** |
| Controller, Representative and DPO Contact | (a) | ***[Name and contact details of the controller; where applicable, of any joint controller and of the controller's representative under Art. 27 (a controller not established in the Union that is subject to Art. 3(2)); contact details of the DPO]*** |
| Joint Controller and Arrangement | (a) | ***[Name and contact details of each joint controller; reference to the Art. 26 arrangement and to the point of contact for data subjects; "not applicable" where there is none]*** |
| Purposes of Processing | (b) | ***[Specific, explicit and legitimate purposes — not a generic formulation such as "service improvement"]*** |
| Categories of Data Subjects | (c) | ***[Customers, prospects, guarantors, beneficial owners, payees, employees, candidates, visitors, counterparties' staff, etc.]*** |
| Categories of Personal Data | (c) | ***[Per the classification of Document 10: data class (level / category) and data state (personal, pseudonymised, synthetic, encrypted — Document 10, Section 4.3); special-category data (Art. 9) and criminal-offence data (Art. 10) noted separately]*** |
| Categories of Recipients | (d) | ***[Recipients to whom the data have been or will be disclosed, by role: processors, joint controllers, independent controllers, public authorities where disclosure is required by law; recipients in third countries or international organisations named as such. Internal units are not recipients in the sense of Art. 4(9); they may be listed separately as "internal access"]*** |
| Transfers to Third Countries or International Organisations | (e) | ***[For each transfer: importer and country (or international organisation); mechanism — Art. 45 adequacy (scope and eligibility checked), Art. 46 tool, or Art. 49 derogation; TIA identifier (Document 20) for the Art. 46 branch; for a transfer under the second subparagraph of Art. 49(1), the documentation of suitable safeguards. A flow is a transfer only if the three criteria of Document 12, Section 2.1 are met; where there is none, "not applicable" with a reference to the transfer-status conclusion where one was needed]*** |
| Time Limits for Erasure | (f) | ***[Period or criterion, by reference to the row of the retention matrix of Document 11 — not restated here]*** |
| Technical and Organisational Security Measures | (g) | ***[General description (Art. 32(1)) — detail in the security documentation and, for privacy-enhancing techniques, the Technology Implementation Package (Document 9)]*** |

***3.2 Processor Record (Art. 30(2))***

For processing that the organisation carries out as processor on behalf of a client controller, the record contains the fields below. The purposes, lawful basis and retention are determined by the controller and are not redefined in the processor record; the processor follows the controller's documented instructions.

| Record Field | Art. 30(2) | Content |
| :---- | :---- | :---- |
| Identifier and Name | — | ***[Unique record number (RoPA-P-…); name of the service provided to the client]*** |
| Processor, Representative and DPO Contact | (a) | ***[Name and contact details of the organisation as processor, of its representative where Art. 27 applies, and of its DPO]*** |
| Controller(s) on Whose Behalf the Organisation Acts | (a) | ***[Name and contact details of each controller, of its representative where applicable and of its DPO; reference to the Art. 28 contract]*** |
| Sub-processors | (a) | ***[Each other processor engaged, with the controller's prior specific or general written authorisation (Art. 28(2))]*** |
| Categories of Processing Carried Out for Each Controller | (b) | ***[The processing operations performed under the contract]*** |
| Transfers to Third Countries or International Organisations | (c) | ***[As in Section 3.1, including, for a transfer under the second subparagraph of Art. 49(1), the documentation of suitable safeguards; transfers only on the controller's documented instructions]*** |
| Technical and Organisational Security Measures | (d) | ***[General description (Art. 32(1))]*** |
| Breach Notification to the Controller | — | ***[Contractual notification term; the processor notifies the controller without undue delay after becoming aware of a breach (Art. 33(2)), applies no controller risk threshold and has no 72-hour clock of its own (Document 14)]*** |

***3.3 Supplementary Fields (Organisation-Defined)***

These fields are not required by Art. 30 but make the register usable for accountability (Art. 5(2), 24) and for the other PGF documents. They reference other records; they do not duplicate them.

| Record Field | Content |
| :---- | :---- |
| Processing Owner | ***[The designated mandate holder accountable for the activity (Document 25, Section 10)]*** |
| Lawful Basis and Conditions | ***[Art. 6(1) basis per purpose; Art. 9(2) condition or Art. 10 authorisation where relevant; for legitimate interests, reference to the balancing test; for further processing, the Art. 6(4) compatibility assessment; for consent, a reference to the consent management system as the single source of consent status (Document 13) — the RoPA records the activity, not individual consents]*** |
| Source of Data | ***[Where data are not obtained from the data subject: the source (Art. 14(2)(f))]*** |
| Automated Decision-Making / Profiling | ***[Whether Art. 22 decisions are taken; the Art. 22(2) exception and the Art. 22(3) safeguards; profiling; or "not applicable"]*** |
| AI System and AI Act Role | ***[Where an AI system is used: provider or deployer role, classification and reference to the AI system inventory (Document 3, Section 3.5); or "not applicable"]*** |
| Transparency | ***[Reference to the notice or section that informs data subjects (Arts. 13–14; Document 1)]*** |
| Reference to the Data Inventory | ***[DI-… identifiers of the systems and datasets that hold the data (Document 23); the identification scheme is the metadata standard of Document 10, Section 6.1]*** |
| G-DPIA Outcome and DPIA Reference | ***[Triage record (DPIA required / not required, with the criteria applied — Document 19, Section 3.1) and DPIA identifier where performed. A DPIA is not excluded because the lawful basis is a legal obligation: Art. 35(10) exempts only where its specific conditions are met]*** |
| Residual-Risk Decision Reference | ***[Tier and decision as recorded in the Privacy Risk Register (Document 22) or the DPIA, with the single decider and the date — shown by reference only; "no residual-risk decision" where none was required]*** |
| Evidence Pack | ***[EVP-YYYY-NNNN reference, where a formal calculation or decision exists]*** |
| Status | ***[Planned / Active / Suspended (with reason and date) / Archived]*** |
| Dates | ***[Created; last updated; Processing Owner's last attestation; next review (Section 4)]*** |

## **4. Record Lifecycle**

| Event | Content |
| :---- | :---- |
| 4.1 Creation | ***[A record is created on intake of a request for a new processing activity (Document 24, process C2), before the processing starts and whether or not a DPIA or TIA is required. A planned activity is registered with status "Planned"; DPIA and TIA identifiers are added to the same record when those assessments are completed — no second record is created. Recording does not depend on any approval: the register records all processing, including processing that is later stopped or redesigned]*** |
| 4.2 Update | ***[The record is updated on a material change to the purpose, data categories, recipients, transfers, retention, system or Processing Owner. The Processing Owner notifies the [Privacy Operations Lead] of such changes before they take effect. A change to the cross-border element triggers the TIA or transfer-status review (Document 20, Section 3.2) and the record is updated on its outcome; a suspension of a transfer or of the processing is recorded with the date and reason]*** |
| 4.3 Review and Attestation | ***[At least once a year the Processing Owner confirms in writing that the record is complete and current (attestation), and [Privacy Officer(s)] check the record against the Data Inventory (Section 5). The review is tied to the record, not to any tool's certification cycle]*** |
| 4.4 Consistency Check | ***[At each review and after any change to a linked DPIA, TIA, risk-register entry or inventory record, the identifiers, tiers, statuses and data classes in the record are reconciled with those records; a discrepancy is resolved under Section 5]*** |
| 4.5 Archiving | ***[When the processing ends, the record is moved to "Archived" — not deleted — with the date and reason. Archived records are accountability records, kept under the retention row of Document 11 that applies to evidence and decision records, not under the row of the customer data they describe]*** |

## **5. Demarcation from the Data Inventory**

The register (this document) and the Data Inventory (Document 23) describe the same processing from different angles and do not duplicate each other:

* ***[The register is authoritative on purposes, lawful bases, categories of data subjects and recipients, transfers as attributes of a processing activity, and retention criteria. The register is the single list of active transfers at process level (Document 12, Section 8); the Data Inventory's cross-border flag identifies the flows that implement them.]***

* ***[The Data Inventory is authoritative on where data are physically held, from which jurisdictions they are accessed, which systems and external recipients the flows connect, and the technical lineage of derived datasets.]***

* ***[Categories of personal data are described in the register at a level sufficient for risk assessment and for answering data subject requests; tables, fields and storage systems are recorded only in the Data Inventory.]***

* ***[Consistency check. Each record lists its DI-… references and each inventory record lists the RoPA records it supports; a record whose data class, transfer status or DPIA reference differs from the linked inventory record is flagged for reconciliation.]***

A discrepancy found during an audit, a review or the handling of a data subject request is resolved by ***[the Privacy Operations Lead]*** under the rules above, with the Processing Owner for content and Data Governance for technical fields — not by an arbitrary choice between the two sources.

## **6. Roles and Responsibilities**

| Role | Responsibility |
| :---- | :---- |
| ***[Privacy Operations Lead]*** | ***[Accountable for the completeness and accuracy of the register as a whole (Document 5, row S4); ensures that every new processing activity is registered; resolves discrepancies with the Data Inventory (Section 5); provides the register to the supervisory authority on request (Art. 30(4))]*** |
| ***[Privacy Officer(s)]*** | ***[Create and update records on intake, after DPIAs and TIAs and on notified changes; run the annual consistency check]*** |
| ***[Processing Owner]*** | ***[Provides the substantive description of purposes, data and recipients; notifies material changes before they take effect; confirms entries and attests annually that the records for its activities are complete and current (Document 5, row S4: Consulted — confirms entries)]*** |
| ***[Data Governance]*** | ***[Consulted on records that reference the Data Inventory; ensures that DI-… identifiers are consistent (Document 23)]*** |
| ***[Privacy Engineer(s)]*** | ***[Consulted on technical fields drawn from the Data Inventory; maintain any integration that pulls those fields]*** |
| ***[Legal]*** | ***[Records the lawful basis, Art. 9/10 conditions, transfer-status conclusions and Art. 49 derogation records that the register references (G-L)]*** |
| ***[DPO]*** | ***[Informed of the state of the register (Document 5, row S4); may review it as part of the compliance monitoring it organises (Art. 39(1)(b)); is the supervisory authority's contact point when the register is requested. The DPO does not approve or gate the entry of records]*** |

## **7. Relationship to Other Framework Documents**

* Records the outcomes of the DPIA Methodology (Document 19) and of the TIA Methodology (Document 20) by reference.
* Is the single list of active transfers at process level (Document 12, Section 8); the transfer-status conclusions and TIAs are kept in Document 20.
* Uses the data class and data state of the Data Classification Policy (Document 10) and the retention rows of Document 11.
* References residual-risk decisions recorded in the Privacy Risk Register (Document 22) and in DPIAs; it does not record risk independently.
* Is used to identify the processing activities affected by a data subject request (Document 15); individual requests are kept in the rights-request log, not in the register.
* Lists consent-based processing activities consistently with the Consent Management Policy (Document 13); consent status is held in the consent management system.
* Is demarcated from the Data Inventory (Document 23) under Section 5.
* Is maintained under supporting process S4 and updated from core process C2 of the process map (Document 24).
* Roles follow the RACI Matrix (Document 5) as the single source of truth; Processing Owners are listed in Document 25, Section 10.

## **8. Review and Amendment**

This document is reviewed under the Policy Review Cycle (Document 29) and whenever applicable law changes the mandatory fields (Section 3). Amendments are prepared by ***[the EPPO]***, with DPO advice, and adopted by ***[Executive Management]***.

## **9. Approval**

This document is adopted by ***[Executive Management]*** on ***[date]***. Document owner: ***[EPPO]***.

# **Part B — Worked Example (fictional): PanEuropean Bank AG**

**PanEuropean Bank AG — Record of Processing Activities (RoPA)**

*Effective date: 20 October 2026 · Version: 2.0 · Document owner: Chief Privacy Officer · Adopted by: Management Board*

*A fictional organisation, prepared solely for illustrative purposes.*

***Fictional document history (illustrative)***

| Version | Date | Changes |
| :---- | :---- | :---- |
| 1.0 | 1 March 2026 | First version, adopted by the Management Board; owner then the Group DPO (programme tasks then sat with the DPO) |
| 2.0 | 20 October 2026 | Re-baselined to Charter v3.0 and the RACI Matrix v4.0: owner the Chief Privacy Officer; Art. 27 representative and Art. 30(2) processor fields added; Processing Owner attestation and consistency check added; DPO approval of records removed; register excerpt corrected (credit-scoring tiers and status, customer-service assistant on hold, anti-fraud matching purpose, federated-learning record, DPIA triage for video surveillance and AML screening, processor record) |

## **Glossary of Terms**

The terms of Part A apply. Local term: **Register platform** — the RoPA module of PanEuropean's GRC system, in which records are kept; technical fields are pulled from the corporate data catalogue (Document 23) through an interface maintained by the Privacy Engineers.

## **1. Purpose**

This document establishes the structure and procedure of PanEuropean Bank AG's register of processing activities. It covers all of the Bank's processing activities and records the results of the DPIAs (Document 19) and TIAs (Document 20) by reference.

## **2. Scope of Application**

The register covers all processing by PanEuropean Bank AG and its branches in Germany, France, Italy, Spain and Poland (one legal entity): as controller — for example credit scoring, anti-fraud matching with a partner bank by private set intersection, customer service, payment protection insurance (PPI) distribution, biometric log-in, marketing, AML/KYC screening, branch video surveillance, HR and card payments; as joint controller — the federated-learning anti-fraud consortium with other EU banks (Art. 26); and as processor — payment services operated for a group company of PanEuropean Financial Holding SE under an Art. 28 contract. EuroCredit Bureau, the partner bank in India and the PPI insurer are independent controllers, recorded as recipients.

The register is kept in electronic form. On a request from the HBDI (lead SA) or a concerned SA, the Privacy Operations Lead provides an export within 24 hours (internal target); the Group DPO, as the SAs' contact point, is informed.

PanEuropean employs well over 250 persons, and its processing is regular and includes special-category and criminal-offence data, so the Art. 30(5) derogation does not apply to any of its activities. PanEuropean is established in the Union; no Art. 27 representative is required, and the field reads "not applicable — controller established in the EU".

## **3. Record Structure at PanEuropean**

PanEuropean applies the fields of Part A, Sections 3.1–3.3 unchanged, with these local choices:

* **Controller and DPO contact.** PanEuropean Bank AG, Frankfurt am Main; Group DPO, dpo@paneuropean-bank.example (Group DPO and Deputy Group DPO).
* **Data class.** Level / category and data state of Document 10 (for example "Restricted / Personal data; synthetic").
* **Retention.** The name of the row of the retention matrix (Document 11, Part B, Section 5).
* **Transfers.** Importer, country, mechanism and TIA identifier as in Document 12, Part B, Section 5; customer-instructed international payments refer to General Counsel's Art. 49(1)(b)/(c) derogation record (Document 12, Part B, Section 2).
* **Consent.** Consent-based activities are exactly those of the single list in Document 13, Part B, Section 2; the record refers to the consent management system (CMS) for consent status.
* **Evidence pack.** EVP-YYYY-NNNN of the decision supporting the record.

As processor, PanEuropean keeps Art. 30(2) records for the payment services it operates for a group company (record RoPA-P-PAY-01, Appendix).

## **4. Record Lifecycle at PanEuropean**

| Event | Content |
| :---- | :---- |
| 4.1 Creation | Privacy Officer(s) register the record on the Register platform on intake of a request for new processing (Document 24, C2), with status "Planned"; DPIA, TIA and evidence-pack identifiers are added to the same record when available |
| 4.2 Update | Processing Owners notify material changes to the Privacy Operations Lead before they take effect; a change to the cross-border element triggers re-evaluation under Document 20 and the record is updated on its outcome; suspensions are recorded with date and reason (for example the customer-service assistant, 26 October 2026) |
| 4.3 Review and Attestation | Each Processing Owner attests its records annually, in the fourth quarter; Privacy Officer(s) check the records against the Data Inventory. Reviews are not tied to the re-certification of any tool (Document 9, Section 5) |
| 4.4 Consistency Check | After any change to a linked DPIA, TIA, Privacy Risk Register entry or inventory record, and at least quarterly, an automated comparison on the Register platform flags differing identifiers, tiers, statuses and data classes; flagged items are resolved within 10 business days (internal target) |
| 4.5 Archiving | When processing ends, the record is archived with date and reason and kept under the Document 11 row "Evidence packs and decision records" — for the life of the processing and afterwards 3 years (illustrative internal value) — not under the row of the customer data it describes |

## **5. Demarcation from the Data Inventory at PanEuropean**

* The register is authoritative on purposes, lawful bases, recipients, transfers at process level and retention criteria.
* PanEuropean's Data Inventory (Document 23) is authoritative on where data are held and accessed and on the flows between systems and external recipients. For example, the systems supported by Example Cloud Services Pvt Ltd (fictional) are hosted in the EEA; the Indian provider has remote access for technical support, which is a transfer (TIA-CLOUD-01). The register records the transfer as an attribute of RoPA-CLOUD-01; the inventory records the hosting location (EEA) and the access jurisdiction (India) of DI-CLOUD-01.
* Tables, fields and storage systems appear only in the inventory.
* Each record lists its DI-… references and each inventory record lists its RoPA references; discrepancies are resolved by the Privacy Operations Lead with the Processing Owner and the Data Steward.

## **6. Roles and Responsibilities**

| Role | Responsibility |
| :---- | :---- |
| Privacy Operations Lead | Accountable for the register (Document 5, row S4); provides it to the HBDI on request; resolves discrepancies with the Data Inventory |
| Privacy Officer(s) | Create and update records on the Register platform; run the consistency check |
| Processing Owners (Document 25, Section 10) | Describe their activities, notify changes before they take effect, confirm entries and attest annually |
| General Counsel (Legal & Compliance) | Records lawful bases, Art. 9/10 conditions, transfer-status conclusions and Art. 49 derogation records referenced by the register |
| Data Governance (CDO) | Consulted on DI-… references; Data Steward maintains the catalogue side |
| Privacy Engineer(s) | Maintain the interface that pulls technical fields from the catalogue |
| Group DPO | Informed; may review the register in the compliance monitoring it organises (Art. 39(1)(b)); contact point for the HBDI when the register is requested; does not approve records |

## **7. Relationship to Other Framework Documents**

* DPIAs (Document 19): DPIA-CS-TRAIN-01, DPIA-CS-INFER-01, DPIA-CS-LAUNCH-01, DPIA-LLM-01, DPIA-PSI-01 and DPIA-FL-01 are referenced from the corresponding records (Appendix).
* TIAs and transfer-status conclusions (Document 20): TIA-CLOUD-01, TIA-PSI-01 and TIA-LLM-01; the federated-learning consortium is recorded with General Counsel's conclusion that it involves no transfer (EVP-2026-0041).
* Data classes and states from Document 10; retention rows from Document 11; transfers as listed in Document 12, Part B, Section 5.
* Risk decisions by reference to the Privacy Risk Register (Document 22): PRR-CS-TRAIN-01, PRR-CS-INFER-01, PRR-CS-LAUNCH-01, PRR-LLM-01, PRR-PSI-01, PRR-CLOUD-01, PRR-FL-01.
* Consent-based activities exactly as in Document 13; rights requests handled under Document 15 using the register to find the activities concerned.
* Inventory references to Document 23; register process S4 of Document 24; Processing Owners from Document 25, Section 10.

## **8. Review and Amendment**

This document is reviewed annually under the Policy Review Cycle (Document 29) and on any material change to Documents 10, 12, 19 or 20. Amendments are prepared by the Chief Privacy Officer, with Group DPO advice, and adopted by the Management Board.

## **9. Approval**

Version 2.0 of this document was adopted by the Management Board of PanEuropean Bank AG on 20 October 2026, on the proposal of the Chief Privacy Officer and after Group DPO advice. Document owner: Chief Privacy Officer. Version 1.0 (1 March 2026) was adopted by the Management Board with the Group DPO as owner.

# **Appendix to Part B — Register Excerpt and Fully Expanded Records**

Status at 26 October 2026. The excerpt shows the main records. Tiers are track (a) residual tiers as decided in the DPIA or recorded in the Privacy Risk Register; the register does not set them. "Transfer" follows the three criteria of Document 12, Section 2.1.

| Identifier | Processing activity | Processing Owner | Lawful basis (and Art. 9/10) | Transfer | DPIA / triage; tier and decision | Status |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| RoPA-CS-001 | Credit-scoring product in the app and online banking (application to decision notice and "Request a Review") | Head of Credit Decisions | Art. 6(1)(b); Art. 22(2)(a) with Art. 22(3) safeguards | No | DPIA-CS-LAUNCH-01 — High (inherited); decision pending (Chief Risk Officer) after the HBDI consultation | Planned — launch planned 1 February 2027 |
| RoPA-CS-002 | Credit-scoring model calibration on a synthetic dataset | Head of Credit Decisions | Art. 6(1)(f), Art. 6(4) compatibility recorded | No | DPIA-CS-TRAIN-01 — Medium; accepted with conditions 25 March 2026 | Active |
| RoPA-CS-003 | Automated decisions on retail credit applications (clear approvals and refusals automated; borderline band decided by a credit officer before effect) | Head of Credit Decisions | Art. 6(1)(b); Art. 22(2)(a) with Art. 22(3) safeguards | No | DPIA-CS-INFER-01 — High (inherent Critical); G-36 met; HBDI consulted 15 September 2026, advice awaited; decision pending (Chief Risk Officer) | Planned — not in production; credit decisions currently taken by credit staff |
| RoPA-CREDIT-01 | Creditworthiness assessment by credit staff and credit bureau reporting | Head of Credit Decisions | Art. 6(1)(c) (creditworthiness assessment); Art. 6(1)(f) (reporting to EuroCredit Bureau) | No | G-DPIA triage: evaluation or scoring, large scale and financial data of a highly personal nature (WP248 criteria) → DPIA required — performed; on the DPIA register (Document 19), not reproduced here; the planned automated design is assessed in DPIA-CS-INFER-01 | Active |
| RoPA-CSV-01 | Handling of customer enquiries by human agents (chat, e-mail, phone) | Head of Customer Service | Art. 6(1)(b) / 6(1)(f); Art. 9(2)(f) or 9(2)(a) only as recorded (expanded record below) | No | Triage record — one WP248 criterion (large scale); no DPIA (the AI-assisted path is assessed in DPIA-LLM-01) | Active — sole channel since 26 October 2026 |
| RoPA-LLM-01 | AI assistance for customer-service agents (summaries and draft replies; an agent reviews every reply) — Example AI Provider Inc. (processor) | Head of Customer Service | Art. 6(1)(b) / 6(1)(f); no Art. 9(2) condition — special-category data excluded from the AI path | USA — SCC Module 2; TIA-LLM-01: pass of 22 June 2026 historical; G-TIA incomplete — HOLD since 26 October 2026 | DPIA-LLM-01 — Medium; acceptance of 25 June 2026 not in effect while the hold applies | Suspended — AI path suspended under Clause 14(f) on 26 October 2026; customer service human-only |
| RoPA-PSI-01 | Anti-fraud matching of shared customers with a partner bank by one-sided private set intersection (only PanEuropean learns matches; no output to the partner) | Head of Fraud Prevention | Art. 6(1)(f); Art. 10 — the partner's list and the matches relate to confirmed fraud (criminal offences): authorisation by applicable national law permitting fraud-prevention processing by credit institutions, with safeguards, recorded by Legal & Compliance in G-L | India — treated as a transfer; SCC Module 1; TIA-PSI-01 (one-sided design passed 20 March 2026) | DPIA-PSI-01 — High (re-assessed 26 October 2026); G-36 met; Chief Risk Officer decision pending after the HBDI consultation; the conditional acceptance of 25 March 2026 is superseded | Paused since 26 October 2026 — no session until the consultation step and the Chief Risk Officer's decision are recorded (the record stays in the register) |
| RoPA-FL-01 | Federated-learning anti-fraud model with EU banks — model updates only, differential privacy and secure aggregation | Head of Fraud Prevention | Art. 6(1)(f); joint controllers (Art. 26) for the shared model; Art. 10 not engaged — training labels limited to confirmed unauthorised transactions with the customer as victim; offence-attributing labels and counterparty data excluded (G-L boundary recorded 26 October 2026; re-assessed on any change of inputs) | Not a transfer — intra-EU consortium (General Counsel's conclusion; EVP-2026-0041; re-checked on membership change) | DPIA-FL-01 — Medium; accepted with conditions 15 May 2026 | Active |
| RoPA-FRAUD-01 | Fraud prevention and transaction monitoring, including automated fraud-suspicion blocking | Head of Fraud Prevention | Art. 6(1)(f); Art. 6(1)(c) where AML law requires monitoring; Art. 22(2)(a) for blocking; Art. 10 for fraud-case records | No | DPIA required by internal policy (criminal-offence data; Document 10, Section 5.1) — performed; on the DPIA register (Document 19), not reproduced here | Active |
| RoPA-CLOUD-01 | Remote technical support of the Bank's infrastructure by Example Cloud Services Pvt Ltd (processor) | CIO | Art. 6(1)(f) (secure and available systems); Art. 32 | India — SCC Module 2; TIA-CLOUD-01 (restricted design passed 12 March 2026) | Triage record — no DPIA (one WP248 criterion); Document 18 calculation Medium; CIO decision 20 March 2026 | Active |
| RoPA-MKT-01 | E-mail and push marketing of PanEuropean products | Head of Marketing | Art. 6(1)(a) — consent status in the CMS | No | Triage record — one WP248 criterion (large scale); no DPIA | Active |
| RoPA-OFFER-01 | Personalised offers in the app (pilot) | Head of Digital Banking | Art. 6(1)(a), separate consent — status in the CMS | No | No DPIA (one WP248 criterion); Document 18 Example 4.1 — Low | Active (pilot) |
| RoPA-BIO-01 | Biometric log-in through the app's own biometric module (template only on the device) | Head of Digital Banking | Explicit consent, Art. 9(2)(a) — status in the CMS; PIN/password alternative always available | No | DPIA required by internal policy (biometric data; Document 10, Section 5.1) — performed; on the DPIA register (Document 19), not reproduced here | Active |
| RoPA-PPI-01 | Arranging payment protection insurance as distributor and forwarding claims | Head of Insurance Distribution | Art. 6(1)(b); explicit consent Art. 9(2)(a) — status in the CMS; Art. 9(2)(f) for legal claims | No | DPIA before launch (health data; Document 10, Section 5.1); application review — Medium, accepted by the Head of Insurance Distribution with the Chief Privacy Officer's concurrence (Document 8, Part B) | Active |
| RoPA-AML-01 | KYC/AML customer due diligence, sanctions and politically-exposed-person screening | Head of Compliance | Art. 6(1)(c) (GwG and branch-country AML law; AMLR from 10 July 2027); Art. 10 authorisation by AML law | No | DPIA required: large-scale screening involving Art. 10 data (Art. 35(3)(b); Document 10, Section 5.1); a lawful basis in law does not exempt (Art. 35(10) conditions not met) — performed; on the DPIA register (Document 19), not reproduced here | Active |
| RoPA-CCTV-01 | Video surveillance of branch premises (security of customers, staff and premises) | Head of Branch Network | Art. 6(1)(f) and national video-surveillance rules (Document 7) | No | G-DPIA triage: systematic monitoring of publicly accessible areas (Art. 35(3)(c)) across the branch network in five countries; the Art. 35(4) lists are checked per country (Document 7) → DPIA required — performed; on the DPIA register (Document 19), not reproduced here | Active |
| RoPA-HR-01 | HR administration of employees and candidates | Head of Human Resources | Art. 6(1)(b)/(c); employment-law basis under national law (in Germany BDSG §26, read in the light of CJEU C-34/21); Art. 9(2)(b) for special-category content (for example health data for sick-leave, religious affiliation for German church tax) | No | G-DPIA triage: employees as vulnerable data subjects and special-category data (WP248 criteria) → DPIA required — performed; on the DPIA register (Document 19), not reproduced here | Active |
| RoPA-CARD-01 | Card payments, payment execution and settlement | Head of Payment Services | Art. 6(1)(b); Art. 6(1)(c) for payment-services and AML obligations | Customer-instructed payments to third-country payees: assessed under the three criteria; where a transfer, Art. 49(1)(b)/(c) on General Counsel's derogation record (Document 12) | G-DPIA triage: large scale and financial data of a highly personal nature → DPIA required — performed; on the DPIA register (Document 19), not reproduced here | Active |
| RoPA-DSR-01 | Handling and logging of data subject requests | Chief Privacy Officer | Art. 6(1)(c) with Arts. 12–22; Art. 5(2) | No | Triage record — no DPIA | Active |
| RoPA-P-PAY-01 | **Processor record (Art. 30(2))** — payment services operated for a group company | Head of Payment Services (owner of the client service) | Determined by the controller | As instructed by the controller (none at present) | Controller's responsibility | Active |

Credit decisions stay with credit staff until the planned launch; the credit-scoring records RoPA-CS-001 and RoPA-CS-003 describe the planned production design and will be set to "Active" only after the consultation step and the Chief Risk Officer's decision. "Consulted" does not mean "approved": the HBDI's advice is awaited and an elapsed period would not be an authorisation.

## **Fully Expanded Record — RoPA-CS-002**

| Record Field | Value |
| :---- | :---- |
| Identifier and Name | RoPA-CS-002 — calibration of the credit-scoring model on a differentially private synthetic dataset |
| Controller, Representative and DPO Contact | PanEuropean Bank AG, Frankfurt am Main; representative: not applicable — controller established in the EU; Group DPO, dpo@paneuropean-bank.example |
| Joint Controller and Arrangement | Not applicable. EuroCredit Bureau is an independent controller that supplied bureau data under the data-sharing agreement (Document 17); it does not determine the purposes or means of the calibration |
| Purposes of Processing | Calibrating and validating the credit-scoring model on a synthetic dataset rather than on customer records |
| Categories of Data Subjects | Applicants and customers whose data were used to train the generator (about 1.2 million customers, illustrative) |
| Categories of Personal Data | Source extract (DI-CS-0873): derived financial indicators, payment history, EuroCredit Bureau data — Restricted / Personal data. Synthetic dataset (DI-CS-0874): Restricted / Personal data, state "synthetic" — no anonymity conclusion (Document 10, Section 4.3); synthetic records can still disclose information about people in the source data. No special-category or criminal-offence data |
| Categories of Recipients | No external recipients. Internal access: Data Science (synthetic dataset only); named Privacy Engineers (source extract, inside PEP) |
| Transfers | Not applicable — no data made available outside the EEA |
| Time Limits for Erasure | Document 11 rows "Synthetic calibration datasets (no anonymity conclusion)" — operational life of the model version + 2 years (illustrative) — and "Generator source extracts and parameters" — extracts 30 days after validation; erasure cascade of Document 11, Section 3.5 applies |
| Security Measures | Source data used only inside the Bank's privacy engineering platform (PEP, illustrative); differentially private generator (ε 1.8 at δ 1×10⁻⁹ for the current dataset, privacy unit one customer; per-run condition ε ≤ 2.0); PET Assessment Module tests (Document 18, Section 3.3.2); role-based access and logging |
| Processing Owner | Head of Credit Decisions |
| Lawful Basis and Conditions | Art. 6(1)(f) — accurate and non-discriminatory credit-risk model — with a recorded balancing test; Art. 6(4) compatibility assessment recorded (G-L, Legal & Compliance, 16 March 2026); Art. 13/14 information covers model development (Document 1) |
| Source of Data | Customer records and EuroCredit Bureau data held by the Bank (Art. 14(2)(f) information given) |
| Automated Decision-Making / Profiling | Not applicable to this record (decisions: RoPA-CS-003) |
| AI System and AI Act Role | Development of a high-risk AI system (AI Act Annex III, point 5(b)); PanEuropean is provider and deployer; high-risk obligations apply from 2 December 2027; AI system inventory of the Model Risk and AI Governance function |
| Transparency | Customer Privacy Notice (Document 1, 01B), Section 7 — model development with pseudonymised and synthetic data |
| Reference to the Data Inventory | DI-CS-0873 (source extract); DI-CS-0874 (synthetic calibration dataset); lineage from DI-CORE-001 and DI-CRED-01 (Document 23) |
| G-DPIA Outcome and DPIA Reference | DPIA-CS-TRAIN-01 (Document 19) |
| Residual-Risk Decision Reference | DPIA-CS-TRAIN-01 — Medium; accepted with conditions by the Head of Credit Decisions on 25 March 2026, with Group DPO advice, under Document 8, version 1.0; expiry 25 March 2027 or the next calibration; re-assessment under Document 8, version 3.0, with the Chief Privacy Officer's concurrence (PRR-CS-TRAIN-01) |
| Evidence Pack | EVP-2026-0012 |
| Status | Active |
| Dates | Created 14 March 2026; updated 25 March 2026 after the DPIA decision; last attestation 20 October 2026; next review at the next calibration or by 25 March 2027, whichever is earlier (planned) |

## **Fully Expanded Record — RoPA-CSV-01**

This record carries the Art. 9 legal conclusion for the human-only customer-service path referred to in DPIA-LLM-01 (Document 19).

| Record Field | Value |
| :---- | :---- |
| Identifier and Name | RoPA-CSV-01 — handling of customer enquiries by human agents in the Bank's own customer-service systems (chat, e-mail, phone) |
| Controller, Representative and DPO Contact | PanEuropean Bank AG; representative: not applicable — controller established in the EU; Group DPO, dpo@paneuropean-bank.example |
| Joint Controller and Arrangement | Not applicable |
| Purposes of Processing | Answering customer enquiries and service requests; quality assurance of replies |
| Categories of Data Subjects | Customers and prospective customers who contact customer service (about 300,000 customers a year, illustrative) |
| Categories of Personal Data | Contact details, product and account information needed for the enquiry, message content — Confidential / Personal data. Customers sometimes volunteer special-category information (for example health information in a hardship or complaint context); such content is handled only under the Art. 9 conclusion below |
| Categories of Recipients | None by default. Where an enquiry concerns PPI, the PPI insurer (independent controller) receives the information needed for the claim under RoPA-PPI-01 |
| Transfers | Not applicable — EEA systems only. No data are sent to Example AI Provider Inc. while RoPA-LLM-01 is suspended |
| Time Limits for Erasure | Document 11 row "Customer-service chat records" — 12 months (illustrative); special-category content that is not used under the conclusion below is deleted without waiting for the end of that period |
| Security Measures | Role-based access for customer-service agents; logging; restricted handling queue for hardship, collections and complaints; encryption in transit and at rest |
| Processing Owner | Head of Customer Service |
| Lawful Basis and Conditions | Art. 6(1)(b) where the enquiry concerns the customer's contract; Art. 6(1)(f) otherwise (timely and consistent handling of enquiries). **Art. 9 conclusion (Legal & Compliance, 15 June 2026; confirmed 26 October 2026 for the human-only operation):** special-category content that customers volunteer is used only to the extent necessary to handle the enquiry and only where a condition applies — the establishment, exercise or defence of legal claims for complaints and disputes (Art. 9(2)(f)), or the customer's explicit consent where the Bank needs to use the information for a service the customer requests (Art. 9(2)(a)). Otherwise it is not used and is deleted under Document 11. No general customer-service exception is relied on |
| Source of Data | The customer |
| Automated Decision-Making / Profiling | Not applicable — no automated decisions about customers |
| AI System and AI Act Role | Not applicable to this record (AI assistance: RoPA-LLM-01, suspended) |
| Transparency | Customer Privacy Notice (Document 1, 01B), Section 7 |
| Reference to the Data Inventory | DI-CSV-01 (customer-service system); DI-CRM-014 (customer profile, read access) |
| G-DPIA Outcome and DPIA Reference | Triage record: one WP248 criterion (large scale); special-category content is occasional and volunteered, not processed systematically — no presumption; no DPIA for the human-only path; Group DPO advice on the triage recorded; the AI-assisted path is assessed in DPIA-LLM-01 |
| Residual-Risk Decision Reference | No residual-risk decision required |
| Evidence Pack | Not applicable (G-L record of 15 June 2026 held with DPIA-LLM-01, EVP-2026-0029) |
| Status | Active — sole customer-service channel since 26 October 2026 |
| Dates | Created 1 March 2026; updated 26 October 2026 (AI path suspended; human-only operation); last attestation 26 October 2026; next review by 26 October 2027 (planned) |

## **Fully Expanded Record — RoPA-P-PAY-01 (Processor Record, Art. 30(2))**

| Record Field | Value |
| :---- | :---- |
| Identifier and Name | RoPA-P-PAY-01 — payment processing services operated for a group company |
| Processor, Representative and DPO Contact | PanEuropean Bank AG as processor; representative: not applicable; Group DPO, dpo@paneuropean-bank.example |
| Controller(s) on Whose Behalf PanEuropean Acts | A service company of the PanEuropean Financial Holding SE group (fictional), established in Germany, as controller for its customers' payment data; its DPO contact as stated in the Art. 28 contract |
| Sub-processors | Core banking platform provider (EEA), with the controller's general written authorisation under the contract |
| Categories of Processing Carried Out for the Controller | Execution and settlement of the controller's customers' payment orders; reconciliation; storage of payment records for the controller; return or deletion at the end of the contract |
| Transfers | None, except customer-instructed payments to third-country payees on the controller's documented instructions; the controller determines the mechanism |
| Security Measures | As for the Bank's own payment processing (RoPA-CARD-01); logical separation of the controller's data |
| Breach Notification to the Controller | Without undue delay after PanEuropean becomes aware of a breach, and as the contract specifies; PanEuropean applies no risk threshold of its own and has no 72-hour clock of its own for this processing (Document 14; Document 5, row S7.5) |
| Owner of the Client Service | Head of Payment Services |
| Status and Dates | Active; created 1 March 2026; last updated 20 October 2026; next review by 20 October 2027 (planned) |

# **Normative Basis and References**

* Regulation (EU) 2016/679 (GDPR): Arts. 4(9), 5(2), 6, 9(2)(a), (b) and (f), 10, 13–14, 22, 24, 26, 27, 28, 30(1)–(5), 32, 33(2), 35(3), 35(10), 37(7), 44–49 (incl. the second subparagraph of Art. 49(1)).
* Article 29 Working Party, Position paper on the derogations from the obligation to maintain records of processing activities pursuant to Article 30(5) GDPR (19 April 2018), endorsed by the EDPB.
* Article 29 Working Party, Guidelines on Data Protection Impact Assessment, WP248 rev.01 (nine criteria).
* EDPB Guidelines 05/2021 on the interplay between the application of Article 3 and the provisions on international transfers as per Chapter V of the GDPR, version 2.0 (Section 2.2).
* EDPB Guidelines 07/2020 on the concepts of controller and processor in the GDPR.
* German Federal Data Protection Act (BDSG) §26; CJEU C-34/21 *Hauptpersonalrat der Lehrerinnen und Lehrer* (30 March 2023) — Part B only.
* Regulation (EU) 2024/1689 (AI Act), as amended by the AI Omnibus (in force 27 July 2026): Annex III, point 5(b); high-risk obligations for Annex III systems apply from 2 December 2027.
* Digital Omnibus — proposal; Council negotiating mandate agreed 21 October 2026; not enacted. The current Art. 30(5) applies.

# **International Adaptation**

> **Guidance.** The GDPR is the baseline. The applicability map for Canada is in Document 7, Section 3.1. This document does not claim compliance with any jurisdiction's law.

* **United Kingdom (headline).** UK GDPR Art. 30 requires the same controller and processor records; the Data (Use and Access) Act 2025 commences in phases — check at each review whether a commenced provision changes the record-keeping duty. The competent authority is the ICO.
* **Switzerland (headline).** The revFADP requires controllers and processors to keep a register of processing activities (Art. 12), with a minimum content similar to Art. 30; the implementing ordinance exempts enterprises with fewer than 250 employees whose processing presents a low risk of infringing personality. Federal bodies report their registers to the FDPIC.
* **Canada — PIPEDA.** There is no statutory register of processing activities. The accountability principle (Schedule 1, Principle 4.1) requires policies and practices that give effect to the principles, including identifying purposes (4.2) and limiting retention (4.5); the OPC/OIPC guidance *Getting Accountability Right with a Privacy Management Program* recommends a personal information inventory. The RoPA can serve that purpose; record the purposes identified at or before collection and the form of consent relied on (meaningful consent). Breach records (24 months) are kept separately (Document 14).
* **Canada — Québec (P-39.1).** There is no RoPA as such. The register supports the duties of the person in charge of the protection of personal information: governance policies and practices, privacy impact assessments (including before communicating personal information outside Québec), and the register of confidentiality incidents, which is kept separately (Document 14). Record express consent for sensitive information and the information given about decisions based exclusively on automated processing.

# **Document History (PGF)**

| Release | Date | Changes |
| :---- | :---- | :---- |
| 1.0.0-rc.1 | 2026-10-26 | Canonical English Markdown; changes from internal ver.2: title block and structure per the editorial rules; Art. 30(1) fields mapped one by one, including the Art. 27 representative, recipients in third countries and international organisations, and the documentation of suitable safeguards for Art. 49(1) second-subparagraph transfers; Art. 30(2) processor record added as a variant section (representative, DPO, sub-processors, breach notification to the controller); Art. 30(3) written/electronic form; Art. 30(5) wording corrected ("likely to result in a risk") and pending omnibus changes recorded as proposals only; supplementary fields (Processing Owner, lawful basis and conditions, AI Act role, transparency, G-DPIA outcome, residual-risk decision by reference, status) added; recording no longer depends on DPO approval, and the DPO is informed and monitors; Processing Owners notify changes and attest annually; consistency check with the Data Inventory; review decoupled from tool re-certification; archived records retained as accountability records; demarcation with the Data Inventory (Document 23 authoritative on location, access and flows; the RoPA the single list of transfers at process level); Part B rebuilt: credit-scoring records aligned with the DPIAs (DPIA-CS-TRAIN-01 Medium, decided by the Head of Credit Decisions; DPIA-CS-INFER-01 and DPIA-CS-LAUNCH-01 High, HBDI consultation pending, launch planned, not in production; clear cases automated and borderline cases decided by a credit officer); EuroCredit Bureau recorded as an independent controller, not a joint controller; the former real-vendor LLM record replaced by RoPA-LLM-01 (Example AI Provider Inc.; G-TIA hold; AI path suspended; human-only operation) and a human-only customer-service record carrying the Art. 9 conclusion; PSI purpose corrected to anti-fraud matching with no output to the partner; federated-learning record added (Art. 26; no transfer; EVP-2026-0041); "no DPIA required" for AML screening and video surveillance replaced by the G-DPIA triage outcome; HR record with BDSG §26 and Art. 9(2)(b); consent-based records aligned with Document 13; card payments with the Art. 49 derogation route; processor record for group payment services; hosting of the remote-support case corrected (EEA hosting, remote access from India); evidence packs in EVP-YYYY-NNNN format; product and vendor names removed; adoption moved to the Management Board; example dates shifted by −12 months; normative basis and international adaptation added. Review correction: RoPA-PSI-01 states the Art. 10 basis and the status after the re-assessment of 26 October 2026 (High; sessions paused) |
