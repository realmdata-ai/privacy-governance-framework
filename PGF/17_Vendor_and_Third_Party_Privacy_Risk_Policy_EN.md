---
title: "Vendor and Third Party Privacy Risk Policy"
document_id: PGF-17
level: 2
release_version: 1.0.0-rc.1
status: release-candidate
authors: ["Alexey Neyman", "Val Khvatov"]
regulatory_reference_date: 2026-10-26
licence_proposed: "CC BY 4.0 (proposed; subject to rights-holder confirmation)"
source_provenance: "Derived from internal source set ver.2: Level2/17. Vendor-Third-Party-Privacy-Risk-Policy_ENG.docx.md; sha256 74ea6cbf409e644830d54f2a9ff2e56ddc2eb73f4da08ce8f3485a16ebfb83d0"
---

# PGF-17 — Vendor and Third-Party Privacy Risk Policy

*Privacy Governance Framework (PGF) · Level 2 — Policies and Standards · Release 1.0.0-rc.1 · Regulatory reference date: 26 October 2026*

> **Status and use.** Part A is a reusable template. Part B is a worked example for a fictional organisation (PanEuropean Bank AG); all names, figures, dates and records in Part B are illustrative. Nothing in this document is legal advice or a statement about any real organisation, product or provider.

# **About This Document**

**Purpose.** Document 17 governs how the organisation classifies, assesses, contracts with and oversees counterparties that process its personal data: processors and sub-processors (Art. 28), joint controllers (Art. 26) and independent controllers with which data are shared; and, for financial entities, how the privacy module connects to ICT third-party risk management under DORA.

**Scope.** Every counterparty that receives, accesses or otherwise processes personal data for which the organisation is controller, and the organisation's own role where it acts as processor for a client. Suppliers with no access to personal data are out of scope. The transfer rules are in Document 12 and Document 20; this document requires that they are met before data flow.

**Relationships.** Document 3 (Sections 3.8 and 3.15) — Procurement, outsourcing and the DORA Register of Information; Document 5 (rows S6.1, S6.2, S7.5) — roles; Document 11 — retention, deletion and legal hold; Document 12 — transfers, onward transfers and sub-processors; Document 14 — breach notification by processors; Document 15 — assistance with data subject rights; Document 16 — procurement criterion for data protection by design; Document 18 — the due-diligence status as an input to likelihood factor L3; Document 22 — vendor-assessment outcomes in the Privacy Risk Register.

# **How to Use This Document**

Part A is a template. Text in ***[square brackets, bold italic]*** is a fill-in or illustrative placeholder. Blocks marked **Guidance** are removed from the adopted version. Part B shows the template completed for the fictional PanEuropean Bank AG. Every provider named in Part B is fictional — Example Cloud Services Pvt Ltd, Example AI Provider Inc., EuroCredit Bureau, the partner bank and the unnamed core banking platform, PEP support and delivery service providers — and their attributes are illustrative assumptions.

> **Guidance.** Classify the role of each counterparty per processing activity before choosing a contract (EDPB Guidelines 07/2020). The same counterparty can be a processor for one activity and an independent controller for another. Financial entities connect this document to their outsourcing and ICT third-party registers instead of creating a third vendor register (Document 3, Section 3.15).

# **Table of Contents**

**About This Document**
**How to Use This Document**
**Part A — Template**
1. Purpose
2. Scope and Role Classification
3. Status Relative to Procurement, Outsourcing and ICT Third-Party Risk
4. Privacy Due Diligence
5. Contractual Requirements (5.1 Processors — Art. 28 Checklist; 5.2 Joint Controllers — Art. 26 Arrangement; 5.3 Independent Controllers — Data-Sharing Agreement; 5.4 Transfers; 5.5 ICT Third-Party Requirements for Financial Entities (DORA))
6. Vendor Categorisation and Reassessment Cadence
7. Sub-processor Management
8. Assistance Obligations and Breach Notification
9. Retention, Return and Deletion; Backups; Legal Hold; Exit
10. Roles and Responsibilities
11. Relationship to Other Framework Documents
12. Review and Amendment
13. Approval
**Part B — Worked Example: PanEuropean Bank AG** (same structure)
**Normative Basis and References**
**International Adaptation**
**Document History (PGF)**

# **Part A — Template**

**Vendor and Third-Party Privacy Risk Policy of *[Legal name of organisation]***

*Effective date: **[DD Month YYYY]**  ·  Version: **[x.x]**  ·  Document owner: **[Executive Privacy Programme Owner (EPPO)]**  ·  Adopted by: **[Executive Management]***

***Version History***

| Version | Date | Changes |
| :---- | :---- | :---- |
| ***[1.0]*** | ***[DD Month YYYY]*** | ***[First version of the document]*** |
| ***[x.x]*** | ***[DD Month YYYY]*** | ***[Brief description of material changes]*** |

## **1. Purpose**

This document governs the assessment and management of privacy risk in relationships with counterparties that process the organisation's personal data: role classification, privacy due diligence, contractual requirements, categorisation and reassessment, sub-processors, assistance and breach notification, retention and exit.

## **2. Scope and Role Classification**

| Role | Test | Instrument | Notes |
| :---- | :---- | :---- | :---- |
| ***[Processor (Art. 4(8), 28)]*** | ***[Processes personal data on behalf of the organisation and on its documented instructions; does not determine the purposes]*** | ***[Art. 28 contract (Section 5.1)]*** | ***[A processor that determines purposes and means becomes a controller for that processing (Art. 28(10))]*** |
| ***[Sub-processor]*** | ***[Engaged by a processor to carry out specific processing activities on the organisation's behalf]*** | ***[Flow-down contract between processor and sub-processor (Art. 28(4)); authorisation by the organisation (Section 7)]*** | ***[The processor remains fully liable for the sub-processor]*** |
| ***[Joint controller (Art. 26)]*** | ***[Jointly determines the purposes and means with the organisation (EDPB Guidelines 07/2020) — for example, a consortium that jointly designs and runs a shared processing operation]*** | ***[Art. 26 arrangement (Section 5.2)]*** | ***[Not a processor]*** |
| ***[Independent controller (recipient)]*** | ***[Receives or supplies data and determines its own purposes and means — for example, a credit bureau, an insurer, a partner bank in a data-matching scheme]*** | ***[Data-sharing agreement (Section 5.3)]*** | ***[Not a processor and not a joint controller unless purposes and means are determined jointly]*** |
| ***[Organisation acting as processor for a client]*** | ***[The organisation processes data on a client's behalf]*** | ***[Art. 28 contract with the client as controller]*** | ***[The organisation's own processor duties apply, including notification of breaches to the client (Section 8; Document 5, row S7.5; Document 14, Section 5.3)]*** |

* ***[Roles are classified per processing activity by [Legal], recorded in the vendor register and in the RoPA (Document 21). A counterparty without access to personal data is out of scope, even if it is an ICT third-party service provider for other purposes.]***
* ***[Sub-processors are covered through the processor's contractual obligations (Section 7); the organisation assesses them directly where they receive special-category data, are in a third country or support a critical or important function.]***

## **3. Status Relative to Procurement, Outsourcing and ICT Third-Party Risk**

***[Procurement owns the organisation's due-diligence process and vendor register; the privacy assessment is a mandatory module of that process, not a parallel process (Document 3, Section 3.8). For financial entities, the outsourcing function owns the outsourcing register and the ICT risk function owns the DORA Register of Information (Document 3, Section 3.15). Privacy fields — role, instrument (Art. 28 contract / Art. 26 arrangement / data-sharing agreement), transfer mechanism and TIA reference, due-diligence status — are linked to those registers by vendor identifier, not copied.]***

> **Guidance.** This is the same type of boundary as in Documents 13 and 16 (privacy as an overlay on the function that owns the underlying process; Document 3, principles D1 and D3), here over Procurement, outsourcing and ICT third-party risk.

## **4. Privacy Due Diligence**

***[The privacy module is completed before the contract is signed and before any personal data flow. Its depth depends on the data class and the role.]***

* ***[**Data and role.** The data classes the counterparty will access (Document 10) — special-category, criminal-offence or large-scale data require extended review — and its role (Section 2).]***
* ***[**Sufficient guarantees (Art. 28(1)).** Expert knowledge, reliability and resources to implement appropriate technical and organisational measures: security posture (for example ISO/IEC 27001:2022 certification or an independent assurance report, taken into account but not a substitute for the organisation's assessment), incident-response capability, staff confidentiality, its own records of processing (Art. 30(2)) and DPO where required.]***
* ***[**Data protection by design and by default.** Ability of the product or service to support minimisation, protective defaults, configurable retention, access control, logging, deletion and export (Document 16, Section 4, item 10).]***
* ***[**Location and transfers.** Where the data will be processed and accessed, including by sub-processors and support staff; whether the transfer criteria of Document 12 are met; if so, the mechanism and TIA (Document 20) before data flow.]***
* ***[**Sub-processors.** The current list, locations and functions (Section 7).]***
* ***[**AI-specific questions** (where the service includes an AI model): whether customer data are used for training or improvement; retention of prompts and outputs; logging; data-residency options; the provider's role under the AI Act (for example, provider of a general-purpose AI model, provider of an AI system, or neither) and the information it supplies to deployers; support for human oversight.]***
* ***[**Operational-resilience status (financial entities).** The ICT risk function's classification of the service under DORA (Section 5.5), recorded separately; privacy and operational criticality are different dimensions assessed in the same process.]***
* ***[**Outcome.** The due-diligence status — no open non-conformities / open non-conformities with remediation dates / not approved — is recorded in the vendor register and, where it bears on a processing scenario, in the Privacy Risk Register field "Vendor-Assessment Source" (Document 22). It is an input to likelihood factor L3 (control-effectiveness gap) in Document 18, not a severity modifier. Document 18 supplies a severity or threat-based likelihood for a processing scenario only on request; vendor due diligence itself stays in this document.]***
* ***[**Unacceptable findings.** A counterparty that cannot give the guarantees of Art. 28(1), or a flow that fails G-L or G-TIA, is not engaged — there is no risk acceptance for a legal failure. For other findings, the decision to engage, suspend or terminate is taken by the Processing Owner (Document 5, row S6.2) with DPO advice, under the acceptance authority of Document 8, Section 5 for the resulting residual risk.]***

## **5. Contractual Requirements**

***5.1 Processors — Art. 28 Checklist***

***[A processor is engaged only under a contract or other legal act in writing, including in electronic form (Art. 28(3), (9)). The contract sets out the subject-matter and duration of the processing, the nature and purpose of the processing, the type of personal data and categories of data subjects, and the obligations and rights of the controller. It stipulates, in particular, that the processor:]***

| Art. 28(3) | Requirement | Contract clause |
| :---- | :---- | :---- |
| ***[(a)]*** | ***[Processes the personal data only on documented instructions from the controller, **including with regard to transfers** of personal data to a third country or an international organisation, unless required to do so by Union or Member State law to which the processor is subject; in such a case, the processor informs the controller of that legal requirement before processing, unless that law prohibits such information on important grounds of public interest]*** | ***[Ref.]*** |
| ***[(b)]*** | ***[Ensures that persons authorised to process the personal data have committed themselves to confidentiality or are under an appropriate statutory obligation of confidentiality]*** | ***[Ref.]*** |
| ***[(c)]*** | ***[Takes all measures required pursuant to Art. 32 (security of processing)]*** | ***[Ref.; annex of technical and organisational measures]*** |
| ***[(d)]*** | ***[Respects the conditions of Art. 28(2) and (4) for engaging another processor (Section 7)]*** | ***[Ref.]*** |
| ***[(e)]*** | ***[Taking into account the nature of the processing, assists the controller by appropriate technical and organisational measures, insofar as this is possible, in responding to requests for exercising the data subject's rights (Chapter III; Document 15)]*** | ***[Ref.]*** |
| ***[(f)]*** | ***[Assists the controller in ensuring compliance with Arts. 32 to 36 — security, notification of personal data breaches, communication to data subjects, DPIA and prior consultation — taking into account the nature of processing and the information available to the processor]*** | ***[Ref.]*** |
| ***[(g)]*** | ***[At the choice of the controller, deletes or returns all the personal data after the end of the provision of services relating to processing, and deletes existing copies unless Union or Member State law requires storage of the personal data (Section 9)]*** | ***[Ref.]*** |
| ***[(h)]*** | ***[Makes available to the controller all information necessary to demonstrate compliance with Art. 28 and allows for and contributes to audits, including inspections, conducted by the controller or another auditor mandated by the controller]*** | ***[Ref.]*** |
| ***[Last subparagraph]*** | ***[With regard to point (h), the processor immediately informs the controller if, in its opinion, an instruction infringes the GDPR or other Union or Member State data protection provisions]*** | ***[Ref.]*** |

* ***[**Breach notification.** The processor notifies the organisation without undue delay after becoming aware of a personal data breach (Art. 33(2)), within the time and in the form the contract specifies, with the information needed for Art. 33(3). The processor does not apply the organisation's risk threshold and has no 72-hour clock of its own; the organisation's clock under Art. 33(1) runs from its own awareness, which normally arises on receipt of the processor's notification (Document 14, Section 5.2). An unreasonable delay by the processor remains an accountability issue for the organisation and a contract breach.]***
* ***[**Standard contractual clauses.** The Commission's standard contractual clauses between controllers and processors (Commission Implementing Decision (EU) 2021/915, Art. 28(7)) may be used in whole or as the basis of the contract. Where the processor is in a third country, the clauses for international transfers (Decision (EU) 2021/914, Module 2) cover both Art. 28 and Chapter V.]***
* ***[**Processor's own obligations.** The processor keeps its own records of processing (Art. 30(2)), cooperates with the supervisory authority (Art. 31) and designates a DPO where required (Art. 37); it is directly liable for its own obligations (Art. 82).]***

***5.2 Joint Controllers — Art. 26 Arrangement***

***[Where purposes and means are determined jointly, an arrangement determines, in a transparent manner, the respective responsibilities for compliance — in particular for the exercise of data subject rights and the information duties of Arts. 13 and 14 — unless these are determined by Union or Member State law. The arrangement may designate a contact point for data subjects; it duly reflects the respective roles and relationships towards data subjects; its essence is made available to data subjects (Art. 26(2)); data subjects may exercise their rights against each controller (Art. 26(3)). The arrangement also allocates breach handling, DPIA responsibilities, security measures for shared infrastructure, onboarding and exit of members, and the transfer status of any new member (Document 12).]***

***5.3 Independent Controllers — Data-Sharing Agreement***

***[Sharing with an independent controller requires a lawful basis for the disclosure (G-L) and a data-sharing agreement that sets out: the purposes of each party and the data shared; each party's own responsibility as controller (no instructions); the information each party gives to data subjects (Arts. 13–14); handling of requests and of rectification, erasure and restriction affecting shared data (Art. 19; Document 15); mutual information about personal data breaches affecting shared data — each party keeping its own Art. 33 duties; security of the exchange; onward disclosures; and, where relevant, data-quality and authenticity warranties and audit rights. No processor-style instructions or service levels are imposed on an independent controller.]***

***5.4 Transfers***

***[Where the transfer criteria of Document 12, Section 2 are met, the contract incorporates the mechanism chosen (Art. 45, 46 or 49) and the supplementary measures from the TIA (Document 20); the transfer does not start before G-TIA passes.]***

***5.5 ICT Third-Party Requirements for Financial Entities (DORA)***

> **Guidance.** Delete this subsection if the organisation is not a financial entity under Regulation (EU) 2022/2554 (DORA). DORA is not a data protection law; the ICT risk function owns these requirements, and privacy links to them. For financial entities, DORA applies instead of the corresponding NIS2 provisions (NIS2 Art. 4).

* ***[**All ICT services.** Every contractual arrangement for ICT services — whether or not it supports a critical or important function, and including AI and software-as-a-service tools — is entered in the register of information (DORA Art. 28(3); Commission Implementing Regulation (EU) 2024/2956) maintained by the ICT risk function, and its contract contains the key contractual provisions of Art. 30(2): a description of the services; the locations where services are provided and data processed and stored, with advance notice of changes; provisions on the availability, authenticity, integrity and confidentiality of data, including personal data; access, recovery and return of data in an easily accessible format on insolvency, resolution, discontinuation or termination; service-level descriptions; assistance in ICT incidents at no additional cost or at a cost determined ex ante; cooperation with the competent authorities; termination rights and minimum notice periods; and participation in ICT security awareness and training.]***
* ***[**Pre-contract assessment (Art. 28(4)).** Before entering an arrangement, the entity assesses whether it covers a function that is critical or important, identifies and assesses the relevant risks, including ICT concentration risk (Art. 29), performs due diligence and identifies conflicts of interest.]***
* ***[**Critical or important functions (CIF).** Whether an ICT service supports a critical or important function is the entity's own assessment, made by the ICT risk function. For such services, the contract also contains the provisions of Art. 30(3) — precise service levels, notice and reporting duties, business-contingency plans, participation in threat-led penetration testing where required, unrestricted rights of access, inspection and audit, and exit strategies with a transition period; the entity keeps a documented and tested exit strategy (Art. 28(8)) and informs the competent authority in a timely manner about planned arrangements for such services (Art. 28(3)).]***
* ***[**Critical ICT third-party service providers (CTPP).** "Critical ICT third-party service provider" is a designation made by the European Supervisory Authorities under Art. 31; it is not a status the entity assigns. The vendor register carries a separate flag for providers designated as CTPPs.]***
* ***[**One contract set.** Legal aligns the Art. 28 GDPR terms, the DORA Art. 30 terms and any outsourcing terms in one contract set (Document 3, Section 3.15); non-ICT outsourcing remains subject to the applicable outsourcing rules (for example the EBA Guidelines on outsourcing arrangements).]***

## **6. Vendor Categorisation and Reassessment Cadence**

> **Guidance.** Two dimensions are assessed separately, in the same process: the privacy role and risk (Sections 2 and 4) and, for financial entities, the DORA classification (Section 5.5). Not every processor supports a critical or important function, and not every ICT provider supporting such a function processes personal data.

| Counterparty | GDPR role and instrument | Transfer (Document 12) | DORA classification (ICT risk function) | Due-diligence status | Reassessment cadence | Processing Owner |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| ***[Name]*** | ***[Processor — Art. 28 contract / joint controller — Art. 26 arrangement / independent controller — data-sharing agreement]*** | ***[No / Yes — mechanism, TIA ID]*** | ***[Not an ICT service / ICT service, not CIF / ICT service supporting CIF / designated CTPP]*** | ***[Status; open non-conformities]*** | ***[e.g. annually for CIF or special-category data; every 2 years otherwise]*** | ***[Name]*** |

* ***[Ad hoc reassessment triggers: change of control; loss of a certification relied on; a personal data breach or security incident at the counterparty; a change of processing location, sub-processor or support location; a public-authority access request at the counterparty (Document 12); a material change to the service, including new AI features; and a change in the DORA classification.]***
* ***[Reassessment cadence is tied to the counterparty's risk and to legal events, not to the calendar of any tool or vendor certification. A TIA re-evaluation (Document 20) runs on its own triggers and may coincide with the reassessment.]***

## **7. Sub-processor Management**

* ***[Sub-processors are engaged only with the organisation's **prior written authorisation** (Art. 28(2)), specific or general. Under a general written authorisation, the processor informs the organisation of any intended addition or replacement of sub-processors at least [30] days in advance, giving the organisation the opportunity to object. The objection decision is taken by [the Processing Owner], with DPO advice — not by the DPO. Under a specific authorisation, the processor obtains the organisation's authorisation for each sub-processor before engagement.]***
* ***[The processor imposes the same data protection obligations on the sub-processor by contract (Art. 28(4)), in particular sufficient guarantees for appropriate technical and organisational measures, and remains fully liable to the organisation for the sub-processor's performance.]***
* ***[A sub-processor in a third country requires an appropriate transfer mechanism (for example SCC Module 3 between processor and sub-processor) and a re-evaluated TIA before it receives data (Document 12, Section 4.4).]***
* ***[The processor keeps an up-to-date list of sub-processors and provides it on request.]***

## **8. Assistance Obligations and Breach Notification**

* ***[**Personal data breaches.** Processors notify without undue delay and per the contract (Section 5.1); the notification contains the information needed for Art. 33(3), provided in phases where necessary. Independent controllers and joint controllers inform the organisation of breaches affecting shared data as the agreement or arrangement provides; each keeps its own Art. 33 duties.]***
* ***[**Data subject rights.** Processors retrieve, correct, restrict or delete data on the organisation's instructions within a time compatible with the organisation's statutory deadlines (Document 15, Section 5). For independent controllers, the agreement provides for passing on rectifications, erasures and restrictions (Art. 19) and for directing data subjects to the controller responsible for the copy concerned.]***
* ***[**DPIA and prior consultation.** Processors supply the information about their processing that the organisation needs for DPIAs and any prior consultation (Art. 28(3)(f)).]***
* ***[**Security incidents under DORA (financial entities).** ICT providers assist in ICT-related incidents as their contract provides (Art. 30(2)); DORA incident reporting is a separate track owned by the ICT risk function (Document 14, Section 5.4).]***
* ***[**Where the organisation is processor.** The organisation notifies its client controllers without undue delay and per the contract, applies no 72-hour clock of its own and does not decide on the client's notifications (Document 5, row S7.5).]***

## **9. Retention, Return and Deletion; Backups; Legal Hold; Exit**

* ***[**During the contract.** The processor retains data only as long as the instructions require; retention periods at the processor (for example, for logs, prompts or outputs) are stated in the contract and match the retention matrix (Document 11, Section 5).]***
* ***[**End of the contract.** At the organisation's choice, the processor deletes or returns all personal data and deletes existing copies, unless Union or Member State law requires storage (Art. 28(3)(g)); deletion is confirmed in writing, with the date and scope.]***
* ***[**Backups.** Data in the processor's backups are put beyond use and overwritten within the rotation period stated in the contract; if a backup is restored, deletions are re-applied before the system returns to service (Document 11, Section 6).]***
* ***[**Legal hold.** Where a legal hold is issued (Document 11, Section 7), the organisation instructs the processor in writing to preserve the specified records, scoped by matter, record category and period; the processor suspends deletion of those records only, and resumes deletion on release.]***
* ***[**Exit.** For ICT services supporting a critical or important function, the exit strategy (DORA Art. 28(8)) covers data return in a usable format, transition and continuity; exit is tested. For all processors, the exit plan includes the return or deletion confirmation above.]***

## **10. Roles and Responsibilities**

> **Guidance.** Roles follow the RACI Matrix (Document 5, rows S6.1 and S6.2) and introduce no new role names. The DPO advises; it does not approve assessments, consent to sub-processors or decide on suspension or termination.

| Role | Responsibility |
| :---- | :---- |
| ***[Procurement]*** | ***[Owns the due-diligence process and the vendor register; initiates the privacy module for every new counterparty with access to personal data]*** |
| ***[Privacy Operations Lead]*** | ***[Accountable for the privacy due-diligence module and reassessments (row S6.1); records outcomes in the vendor register and, where relevant, in the Privacy Risk Register (Document 22)]*** |
| ***[Processing Owner]*** | ***[Accountable for engaging a processor or sharing data with an independent controller (row S6.2), for objections to sub-processor changes, and for suspension or termination, after DPO advice and within the acceptance authority of Document 8]*** |
| ***[Legal]*** | ***[Classifies roles; drafts and negotiates Art. 28 contracts, Art. 26 arrangements and data-sharing agreements; aligns them with DORA and outsourcing terms; transfer mechanisms with Document 12]*** |
| ***[CISO / Information Security]*** | ***[Assesses the counterparty's security posture]*** |
| ***[ICT risk function (financial entities)]*** | ***[Classifies ICT services under DORA (CIF or not), maintains the register of information, concentration-risk and exit-strategy assessments]*** |
| ***[DPO]*** | ***[Advises on higher-risk counterparties (special-category data, AI services, third-country processing), on sub-processor objections and on suspension or termination; monitors compliance. Where the decision-maker does not follow the advice, it records its reasons and the DPO may escalate to Executive Management]*** |
| ***[Executive Management]*** | ***[Informed of arrangements for ICT services supporting critical or important functions; one named member decides where a residual risk is High (Document 8)]*** |
| ***[EPPO]*** | ***[Owns this document]*** |

## **11. Relationship to Other Framework Documents**

* Relies on the Interface and Integration Model (Document 3, Sections 3.8 and 3.15) — Procurement, outsourcing and the Register of Information.
* Relies on the RACI Matrix (Document 5, rows S6.1, S6.2 and S7.5) and on the acceptance authority of the Privacy Risk Appetite Statement (Document 8, Section 5).
* Relies on the Data Classification Policy (Document 10) — data class as the criterion for depth of review.
* Interacts with the Data Retention and Disposal Policy (Document 11) — retention at processors, deletion, backups and legal hold.
* Interacts with the Cross-Border Data Transfer Policy (Document 12) and the TIA Methodology (Document 20) — transfers, onward transfers and sub-processors.
* Interacts with the Data Breach Response Policy (Document 14, Sections 5.2–5.4) — processor notification, the organisation as processor, the DORA track.
* Interacts with the Data Subject Rights Policy (Document 15) — assistance and notification of recipients.
* Interacts with the Privacy by Design and by Default Policy (Document 16, Section 4) — procurement criterion.
* Feeds Document 18 (likelihood factor L3) and the Privacy Risk Register (Document 22, field "Vendor-Assessment Source").
* Documented in the RoPA (Document 21); executed as supporting process S6 on the process map (Document 24).

## **12. Review and Amendment**

This document is reviewed under ***[the Policy Review Cycle, Document 29]*** and whenever the law or guidance on processors, controllership or ICT third-party risk changes. Changes are adopted by ***[Executive Management]*** on the proposal of ***[the EPPO]***, after the DPO's advice.

## **13. Approval**

This document was adopted by ***[Executive Management]*** on ***[date]***. Document owner: ***[EPPO]***.

# **Part B — Worked Example: PanEuropean Bank AG**

**PanEuropean Bank AG — Vendor and Third-Party Privacy Risk Policy**

*Effective date: 20 October 2026  ·  Version: 2.0  ·  Document owner: Chief Privacy Officer (EPPO)  ·  Adopted by: Management Board, 20 October 2026*

*Fictional legal entity, provided solely for illustrative purposes.*

***Fictional Document History (illustrative)***

| Version | Date | Changes |
| :---- | :---- | :---- |
| 1.0 | 1 March 2026 | First version. Owner at the time: Group DPO |
| 2.0 | 20 October 2026 | Re-baselined to the new role model (Chief Privacy Officer as owner; Privacy Operations Lead accountable for due diligence; Processing Owners decide engagement, sub-processor objections and suspension with Group DPO advice); EuroCredit Bureau reclassified as an independent controller; full Art. 28(3) checklist; DORA terminology and register of information for all ICT services; one sub-processor rule aligned with Document 12; the LLM service limited to the customer-service assistant |

## **1. Purpose**

This document governs privacy risk in PanEuropean Bank AG's relationships with its processors — the core banking platform provider, Example Cloud Services Pvt Ltd, Example AI Provider Inc., the PEP support provider and the e-mail and push delivery service provider — and with the independent controllers and joint controllers with which it shares data: EuroCredit Bureau, the partner bank in India, the PPI insurer and the members of the federated-learning anti-fraud consortium.

## **2. Scope and Role Classification**

General Counsel classified each relationship per activity:

* **Processors:** the core banking platform provider (fictional, unnamed, EEA); Example Cloud Services Pvt Ltd (fictional, India — remote technical support with access to production systems); Example AI Provider Inc. (fictional, United States — large language model for the customer-service assistant); the external PEP support provider (unnamed, EEA support staff — Document 9); the e-mail and push delivery service provider (fictional, unnamed, EEA — Document 13).
* **Independent controllers:** EuroCredit Bureau (fictional, EEA) — PanEuropean reports credit agreements and defaults and receives bureau data and scores; each party determines its own purposes, so the relationship is controller-to-controller under a data-sharing agreement, not an Art. 28 contract and not joint control. The partner bank (fictional, India) — one-sided private set intersection for anti-fraud matching. The PPI insurer — underwriting and claims.
* **Joint controllers:** the members of the federated-learning anti-fraud consortium (EU banks), which jointly determine the purposes and means of the shared model (Art. 26).
* **PanEuropean as processor:** payment services operated for a group company under an Art. 28 contract (Document 5, row S7.5).

Suppliers without access to personal data (for example, a supplier of office stationery) are out of scope.

## **3. Status Relative to Procurement, Outsourcing and ICT Third-Party Risk**

Procurement owns PanEuropean's due-diligence process and vendor register; the privacy module is a mandatory part of it, accountable to the Privacy Operations Lead (Document 3, Section 3.8). The outsourcing function owns the outsourcing register under the EBA Guidelines on outsourcing arrangements and German banking law; ICT Risk Control (Head of ICT Risk Control) maintains the DORA Register of Information (Document 3, Section 3.15). Privacy fields are linked to both registers by vendor identifier, not copied. EuroCredit Bureau is a data provider and an independent controller; whether its service is an ICT service supporting a critical or important function is a separate DORA test made by ICT Risk Control, not presumed.

## **4. Privacy Due Diligence**

* **Core banking platform provider.** Full access to transactional and customer data as processor; processing in the EEA (no transfer); ISO/IEC 27001:2022 certification taken into account, not a substitute; sub-processor list reviewed; deletion and export capabilities tested. Status: no open non-conformities.
* **Example Cloud Services Pvt Ltd.** Remote technical support from India with access to production systems — a transfer (TIA-CLOUD-01, Document 20). Due diligence confirmed the restricted design: a privileged-access gateway in the EEA masks customer data on screen; clear-text "break-glass" access only by EEA-based PanEuropean staff; logs tokenised with keys held by PanEuropean in the EEA. Status: no open non-conformities.
* **US recipients relying on the DPF (Art. 45).** The vendor record holds the DPF check of Document 12, Part A, Section 4.1 — exact legal entity and covered entities, framework (EU-U.S. DPF, UK Extension or Swiss-U.S. DPF), HR or non-HR coverage, official status wording and profile URL, date, reviewer and evidence reference — and is re-checked at the annual re-certification date and on any status change. No fictional provider in this example relies on the DPF.
* **Example AI Provider Inc.** Large language model used by the customer-service assistant (Processing Owner: Head of Customer Service; Document 16, Section 4). AI-specific review: no training or improvement on PanEuropean data, prompts and outputs deleted within 30 days (illustrative contractual terms); no persistent store of customer records; data residency in the United States; one US hosting sub-processor; the provider is assumed, for this illustration, not to be certified under the EU-U.S. Data Privacy Framework, so SCC Module 2 and TIA-LLM-01 apply (Document 12). Due-diligence status: no open non-conformities. Transfer status at 26 October 2026: the G-TIA pass of 22 June 2026 is historical and the current re-evaluation is incomplete, so the transfer is on hold — the AI path is suspended under SCC Clause 14(f), customer service in the EU channel is human-only, and no personal data are sent to the provider until a current G-TIA pass is recorded (Document 12, Section 5; Document 20).
* **PEP support provider.** Support access to PEP only from the EEA (illustrative assumption); viability assessed on financial statements and continuity arrangements, not on the support agreement alone (Document 9). Status: no open non-conformities.
* **E-mail and push delivery service provider.** Contact data and suppression lists only; processing in the EEA; the contract obliges the provider to send only messages that have passed PanEuropean's live suppression check immediately before dispatch and to honour cancellations of queued messages at once, so that no message is sent after a withdrawal or objection; retained contact data of withdrawn customers are deleted within one business day of the daily synchronisation (Document 13, Section 6). Status: no open non-conformities.
* **EuroCredit Bureau.** Credit data with no special categories; processing in the EEA (no transfer, Document 12); lawful basis for reporting assessed at G-L (Document 1, Section 7); data-quality and dispute procedures reviewed.
* **Partner bank (India).** One-sided PSI for anti-fraud matching (Processing Owner: Head of Fraud Prevention) — treated as a transfer under SCC Module 1 (TIA-PSI-01). The G-TIA pass rests on the one-sided design without any output to the partner (Document 12, Section 3); due diligence covered the partner's ability to operate that protocol as reviewed and its confirmed-fraud list management, which is a hygiene control and does not carry the equivalence conclusion.
* **Feed into risk calculations.** Due-diligence status is used as evidence for likelihood factor L3 in Document 18 and recorded in the Privacy Risk Register field "Vendor-Assessment Source" (Document 22). Illustration: the advertising partner assessed for Document 18, Example 4.2-R had an incomplete sub-processor list; the open non-conformity set L3 = 2 and was a condition of the conditional acceptance — it did not change severity. That partner is not engaged at 26 October 2026.

## **5. Contractual Requirements**

***5.1 Processors — Art. 28 Checklist***

The contracts with all five processors contain every element of the Part A checklist: subject-matter, duration, nature and purpose, data types and categories of data subjects; documented instructions including on transfers; confidentiality; Art. 32 measures; sub-processor conditions (Section 7); assistance with data subject rights and with Arts. 32–36, including DPIAs and prior consultation; deletion or return at the end of the service; information and audits; and the duty to inform PanEuropean immediately of an instruction that, in the processor's opinion, infringes data protection law. The contracts with Example Cloud Services Pvt Ltd and Example AI Provider Inc. are concluded on the standard contractual clauses of Decision (EU) 2021/914, Module 2, with PanEuropean's annex of technical and organisational measures; the EEA processors' contracts follow the Commission's controller–processor clauses of Decision (EU) 2021/915.

* **Breach notification.** Each processor notifies PanEuropean of a personal data breach without undue delay and in any case within 24 hours of becoming aware (illustrative contractual term), with the information needed for Art. 33(3) (Document 14, Section 5.2). PanEuropean's 72-hour period runs from its own awareness, normally the receipt of the processor's notification; the processors have no 72-hour clock of their own.
* **Example AI Provider Inc.** Additionally: no use of PanEuropean data to train or improve models; deletion of prompts and outputs within 30 days; use limited to the customer-service assistant — any new use requires a new assessment (illustrative terms).

***5.2 Joint Controllers — Art. 26 Arrangement***

The federated-learning consortium arrangement (Processing Owner: Head of Fraud Prevention; Document 5, statutory activities) allocates: information to customers (each bank informs its own customers; the essence of the arrangement is published by each bank); rights requests (each bank answers for its customers' data and its own model updates; requests about the shared model are coordinated by the consortium contact point); breach handling for the aggregation infrastructure; DPIA responsibilities (each bank's DPIA for its participation — DPIA-FL-01 at PanEuropean); security of secure aggregation; and admission of new members, with a transfer-status re-check before any member, coordinator or host outside the EEA joins (Document 12, Section 3).

***5.3 Independent Controllers — Data-Sharing Agreements***

* **EuroCredit Bureau.** Data-sharing agreement: data reported and received; each party's purposes; Art. 14 information by the bureau and Art. 13 information by PanEuropean (Document 1, Section 9); handling of disputes and rectification (PanEuropean passes on corrections under Art. 19; the bureau answers for its own records and score); mutual information about breaches affecting shared data; secure exchange. No processor-style service levels are imposed on the bureau.
* **Partner bank.** Data-sharing agreement with SCC Module 1: purpose limited to anti-fraud matching; the protocol is one-sided without any output to the partner — the partner receives no match result, no intersection size and no result-dependent signal; PanEuropean's input is padded to a fixed public bound, and message lengths and timing do not depend on the number of matches; the partner observes only the padded input bound and the fact of the monthly session (Document 12, Section 3; TIA-PSI-01). The partner undertakes to run only the reviewed protocol version and to notify any change. Hygiene terms, which do not carry the equivalence conclusion: a warranty that the partner's list consists of confirmed-fraud cases with an audit trail, PanEuropean's audit right, a signed commitment to the list before each session, at most one session a month, and no case-specific follow-up through this channel. Any evidence that the partner can observe a result-dependent signal leads to suspension under Clause 14(f).
* **PPI insurer.** Distribution agreement with data-protection clauses: the insurer is controller for underwriting and claims and gives its own notice; PanEuropean forwards health data only on the customer's explicit consent and forwards withdrawals at once (Document 13).

***5.4 Transfers***

Transfers to Example Cloud Services Pvt Ltd (TIA-CLOUD-01), Example AI Provider Inc. (TIA-LLM-01) and the partner bank (TIA-PSI-01) rely on Art. 46 standard contractual clauses with the supplementary measures of each TIA (Document 12, Section 5). The transfer to Example AI Provider Inc. is on hold and suspended under Clause 14(f) at 26 October 2026 (Section 4). No other counterparty receives data outside the EEA.

***5.5 ICT Third-Party Requirements (DORA)***

* **Register of information.** All ICT arrangements — the core banking platform, Example Cloud Services Pvt Ltd, Example AI Provider Inc. (including the large language model service), the PEP support provider and the delivery service provider — are in the Register of Information maintained by ICT Risk Control, and each contract contains the Art. 30(2) provisions.
* **Critical or important functions (ICT Risk Control assessments, illustrative, reviewed annually).** The core banking platform and the remote technical support by Example Cloud Services Pvt Ltd support critical or important functions: their contracts contain the Art. 30(3) provisions, exit strategies exist and are tested annually, the concentration-risk assessment (Art. 29) is recorded, and ECB/BaFin were informed of the planned arrangements as DORA Art. 28(3) requires. Example AI Provider Inc., the PEP support provider and the delivery service provider do not support critical or important functions; the Art. 30(2) provisions apply to them.
* **CTPP status.** None of these fictional providers is designated as a critical ICT third-party service provider by the European Supervisory Authorities; the flag is reviewed with each register update.
* **Management Board.** Informed of arrangements for ICT services supporting critical or important functions (Document 5, row S6.2).

## **6. Vendor Categorisation and Reassessment Cadence**

| Counterparty | GDPR role and instrument | Transfer (Document 12) | DORA classification (ICT Risk Control, illustrative) | Due-diligence status | Reassessment cadence | Processing Owner |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Core banking platform provider (EEA) | Processor — Art. 28 contract | No | ICT service supporting CIF | No open non-conformities | Annually | CIO |
| Example Cloud Services Pvt Ltd (India) | Processor — Art. 28 contract with SCC Module 2 | Yes — TIA-CLOUD-01 | ICT service supporting CIF | No open non-conformities | Annually, and on any TIA trigger | CIO |
| Example AI Provider Inc. (United States) | Processor — Art. 28 contract with SCC Module 2; US hosting sub-processor | Yes — TIA-LLM-01; G-TIA incomplete — on hold, suspended under Clause 14(f) | ICT service, not CIF | No open non-conformities | Annually, and on any TIA trigger or new use; before any resumption | Head of Customer Service |
| PEP support provider (EEA support staff) | Processor — Art. 28 contract | No | ICT service, not CIF | No open non-conformities | Annually | CIO |
| E-mail and push delivery service provider (EEA) | Processor — Art. 28 contract | No | ICT service, not CIF | No open non-conformities | Every 2 years | Head of Marketing |
| EuroCredit Bureau (EEA) | Independent controller — data-sharing agreement | No | Separate DORA test by ICT Risk Control; not presumed critical | No open issues | Every 2 years, or on a change to the agreement | Head of Credit Decisions |
| Partner bank (India) | Independent controller — data-sharing agreement with SCC Module 1 | Yes — TIA-PSI-01 | Not an ICT service | No-output protocol and hygiene terms in force | Annually, and on any TIA trigger | Head of Fraud Prevention |
| PPI insurer (EEA) | Independent controller — distribution agreement | No | Not an ICT service | No open issues | Every 2 years | Head of Insurance Distribution |
| Federated-learning consortium members (EU) | Joint controllers — Art. 26 arrangement | No (intra-EU; EVP-2026-0041) | Shared infrastructure assessed by ICT Risk Control | Arrangement in force | Annually, and on any change of membership | Head of Fraud Prevention |

Ad hoc reassessments follow the Part A triggers. If due diligence or a reassessment reveals a finding that raises the residual risk of a processing scenario, the Processing Owner decides on engagement, remediation, suspension or termination with Group DPO advice, within the acceptance authority of Document 8, Section 5 (the Chief Risk Officer for a residual High); a legal failure — for example, a failed G-TIA — means no start or suspension, without acceptance. At the adoption date, no counterparty has required suspension or termination on this basis; the suspension of the earlier mutual-output PSI design in February 2026 was a G-TIA outcome (Document 12, Section 3).

## **7. Sub-processor Management**

PanEuropean gives its processors a general written authorisation (Art. 28(2)): each processor notifies any intended addition or replacement of a sub-processor at least 30 days in advance (illustrative contractual term), and the Processing Owner — the CIO for the core banking platform, Example Cloud Services Pvt Ltd and the PEP support provider; the Head of Customer Service for Example AI Provider Inc.; the Head of Marketing for the delivery service provider — decides whether to object, with Group DPO advice. A sub-processor in a third country requires SCC Module 3 between processor and sub-processor and a re-evaluated TIA before it receives data (Document 12, Section 4.4). Example Cloud Services Pvt Ltd uses no sub-processors at present; Example AI Provider Inc. uses a US hosting sub-processor covered by TIA-LLM-01 (illustrative). Each processor flows down the same obligations and remains fully liable.

## **8. Assistance Obligations and Breach Notification**

* **Processors** notify breaches within the contractual term of Section 5.1 and assist with data subject requests within five business days of PanEuropean's instruction (illustrative contractual term), so that PanEuropean meets its statutory deadlines (Document 15, Section 5). Example AI Provider Inc. holds no persistent store of customer records; its assistance consists of locating and deleting any prompts and outputs still within the 30-day period on PanEuropean's instruction.
* **EuroCredit Bureau, the partner bank and the PPI insurer** inform PanEuropean of breaches affecting shared data under their agreements and keep their own Art. 33 duties; corrections, erasures and restrictions are passed on under Art. 19 (Document 15, Section 3.2).
* **Consortium members** follow the breach and rights allocation of the Art. 26 arrangement.
* **DORA.** The CIF providers assist in ICT-related incidents as their contracts provide; ICT Risk Control owns the separate DORA reporting track (Document 14, Section 5.4).
* **PanEuropean as processor** notifies the group company under the contract (Document 14, Section 5.3).

## **9. Retention, Return and Deletion; Backups; Legal Hold; Exit**

* **Retention at processors** matches the retention matrix (Document 11, Section 5): Example AI Provider Inc. — prompts and outputs deleted within 30 days; Example Cloud Services Pvt Ltd — provider-side copies of remote-support logs deleted under the processing agreement; the delivery service provider — contact data of withdrawn customers deleted within one business day (Document 13, Section 6).
* **End of contract.** Deletion or return at PanEuropean's choice, with written confirmation of date and scope; for the core banking platform, return in a documented format is part of the exit strategy.
* **Backups.** Processors overwrite backups within a rotation period of at most 90 days (aligned with Document 11, Section 6) and re-apply deletions on any restore.
* **Legal hold.** General Counsel's scoped legal holds (Document 11, Section 7) are passed to the processors concerned in writing; deletion of the specified records only is suspended until release.
* **Exit.** Exit strategies for the two CIF arrangements are tested annually by ICT Risk Control with the CIO; the PEP exit plan is in Document 9.

## **10. Roles and Responsibilities**

| Role | Responsibility |
| :---- | :---- |
| Procurement | Owns the due-diligence process and the vendor register; initiates the privacy module |
| Privacy Operations Lead | Accountable for the privacy due-diligence module and reassessments (row S6.1); records outcomes in the vendor register and the Privacy Risk Register |
| Processing Owners (CIO; Head of Customer Service; Head of Marketing; Head of Credit Decisions; Head of Fraud Prevention; Head of Insurance Distribution) | Accountable for engagement or data sharing (row S6.2), sub-processor objections, suspension and termination, with Group DPO advice |
| General Counsel (Legal & Compliance) | Classifies roles; drafts Art. 28 contracts, Art. 26 arrangements and data-sharing agreements; aligns them with DORA and outsourcing terms and with Document 12 |
| CISO | Assesses security posture |
| Head of ICT Risk Control | DORA classification, Register of Information, concentration-risk and exit-strategy assessments |
| Group DPO | Advises on higher-risk counterparties (Example AI Provider Inc., Example Cloud Services Pvt Ltd, the partner bank), on sub-processor objections and on suspension or termination; monitors compliance |
| Management Board | Informed of arrangements for ICT services supporting critical or important functions; the Chief Risk Officer decides where a residual risk is High |
| Chief Privacy Officer (EPPO) | Owns this document |

## **11. Relationship to Other Framework Documents**

* Relies on PanEuropean's Interface and Integration Model (Document 3, Sections 3.8 and 3.15) and RACI Matrix (Document 5, rows S6.1, S6.2, S7.5).
* Relies on Document 8, Section 5 (acceptance authority) and Document 10 (data classes).
* Interacts with Document 11 (retention at processors, backups, legal hold), Document 12 and Document 20 (TIA-CLOUD-01, TIA-PSI-01, TIA-LLM-01; sub-processors), Document 13 (delivery service provider; PPI insurer), Document 14 (processor notification; DORA track), Document 15 (assistance; Art. 19), Document 16 (procurement criterion; the customer-service assistant) and Document 9 (PEP support provider).
* Feeds Document 18 (factor L3; Example 4.2-R) and Document 22 (field "Vendor-Assessment Source").
* Documented in the RoPA (Document 21); executed as supporting process S6 (Document 24).

## **12. Review and Amendment**

This document is reviewed under PanEuropean's Policy Review Cycle (Document 29), whenever the law or guidance on processors, controllership or ICT third-party risk changes, when the ESAs designate or de-designate a provider PanEuropean uses, and when a new counterparty category emerges. Changes are adopted by the Management Board on the Chief Privacy Officer's proposal, after Group DPO advice.

## **13. Approval**

Version 1.0 (1 March 2026) was adopted by the Management Board; the Group DPO was document owner at that time. Version 2.0 was adopted by the Management Board on 20 October 2026 on the Chief Privacy Officer's proposal, after Group DPO advice. Document owner: Chief Privacy Officer.

# **Normative Basis and References**

* Regulation (EU) 2016/679 (GDPR): Arts. 4(7)–(8), 19, 24, 26, 28 (incl. 28(1)–(4), (7), (9), (10)), 29, 30(2), 31, 32–36, 37, 44–46, 82.
* Commission Implementing Decision (EU) 2021/915 on standard contractual clauses between controllers and processors (Art. 28(7) GDPR); Commission Implementing Decision (EU) 2021/914 on standard contractual clauses for international transfers (Modules 1–3).
* EDPB Guidelines 07/2020 on the concepts of controller and processor in the GDPR, version 2.0.
* EDPB Guidelines 9/2022 on personal data breach notification under GDPR, version 2.0 (processor-to-controller notification; awareness).
* Regulation (EU) 2022/2554 (DORA): Arts. 28 (incl. 28(3) register of information, 28(4) pre-contract assessment, 28(8) exit strategies), 29 (ICT concentration risk), 30(2)–(3) (key contractual provisions), 31 (designation of critical ICT third-party service providers); Commission Implementing Regulation (EU) 2024/2956 (templates for the register of information); Directive (EU) 2022/2555 (NIS2), Art. 4.
* EBA Guidelines on outsourcing arrangements (EBA/GL/2019/02).
* ISO/IEC 27001:2022 (information security management systems) — taken into account in due diligence, not a substitute.
* Canada: PIPEDA, Schedule 1, Principle 4.1.3; Act respecting the protection of personal information in the private sector (Québec, P-39.1).

# **International Adaptation**

> **Guidance.** The GDPR is the baseline. The applicability map for Canada is in Document 7, Section 3.1. This box states what changes; it does not claim compliance with any jurisdiction's law.

* **United Kingdom (headline).** UK GDPR Art. 28 mirrors the EU requirements; the ICO's guidance on controllers and processors applies; international transfers from the UK use the UK tools (Document 12). The Data (Use and Access) Act 2025 amendments commence in phases.
* **Switzerland (headline).** Under the revFADP, processing may be assigned to a processor by contract or by law if the processor processes the data only as the controller itself would be permitted to and no legal or contractual confidentiality obligation prohibits it; the controller ensures that the processor guarantees data security, and the processor may assign processing to a third party only with the controller's prior authorisation.
* **Canada — PIPEDA.** The organisation remains responsible for personal information transferred to a third party for processing and uses contractual or other means to provide a comparable level of protection while the information is being processed by the third party (Principle 4.1.3). Breaches of security safeguards involving information under the organisation's control are assessed and recorded by the organisation (Document 14); contracts require the service provider to inform the organisation promptly.
* **Canada — Québec (P-39.1).** Personal information may be communicated without consent to a person or body to whom the organisation entrusts a mandate or a service contract where the communication is necessary for carrying it out; the mandate or contract is made in writing and specifies the measures the service provider must take to protect the confidentiality of the information, to use it only for the mandate, not to keep it after the mandate ends, and to notify the person in charge of the protection of personal information without delay of any violation or attempted violation of confidentiality, and allows the organisation to verify compliance. Before communicating personal information outside Québec, the organisation conducts a privacy impact assessment and concludes a written agreement (Document 12).

# **Document History (PGF)**

| Release | Date | Changes |
| :---- | :---- | :---- |
| 1.0.0-rc.1 | 2026-10-26 | Canonical English Markdown; changes from internal ver.2: role classification per activity added (processor, sub-processor, joint controller, independent controller, organisation as processor; EDPB Guidelines 07/2020) — the "joint-processing controller counterparty" category split into joint and independent controllers; EuroCredit Bureau reclassified as an independent controller under a data-sharing agreement (not a joint controller, not an Art. 28 processor); Art. 28(3)(a)–(h) checklist reproduced in full, including transfers in the instructions, the infringing-instruction duty, assistance with Arts. 32–36 (DPIA and prior consultation included), deletion or return subject to Union or Member State storage duties, and information and audits; Art. 28(4), (7), (9), (10) and SCC Decision (EU) 2021/915 referenced; Art. 26 arrangement and data-sharing agreement contents added; processor-to-controller breach notification without undue delay with no 72-hour clock of the processor's own; one sub-processor rule consistent with Document 12 (prior written authorisation, general authorisation with 30 days' prior notice and an objection decided by the Processing Owner with DPO advice; SCC Module 3 and re-evaluated TIA for third-country sub-processors) replacing "Group DPO's prior consent"; DORA terminology corrected (ICT services supporting critical or important functions assessed by the entity; CTPP designated by the ESAs under Art. 31), register of information and Art. 30(2) terms for all ICT services including the LLM service, Art. 30(3) terms, Art. 28(4) pre-contract assessment, exit strategy and concentration risk; due-diligence status feeds Document 18 likelihood factor L3 and the Privacy Risk Register, not severity; retention, deletion, backups, legal hold and exit section added; the DPO's approval of assessments and "non-delegable" suspension/termination authority replaced by Processing Owner decisions with DPO advice; Part B rebuilt with fictional providers only (real-vendor certifications and terms removed; Example AI Provider Inc. limited to the customer-service assistant, not DPF-certified as an illustrative assumption; Example Cloud Services Pvt Ltd remote support with the restricted design), the partner-bank contract reflecting the one-sided PSI design without any output to the partner (list warranty, audit right and session rules as hygiene terms only), the LLM transfer shown as on hold at the reference date, the PPI insurer, PEP support provider, delivery service provider and federated-learning consortium added; section references corrected; adoption moved to Executive Management; example dates shifted by −12 months; Normative basis and International adaptation (UK, Switzerland, PIPEDA Principle 4.1.3, Québec service contracts and assessment before communication outside Québec) added |
