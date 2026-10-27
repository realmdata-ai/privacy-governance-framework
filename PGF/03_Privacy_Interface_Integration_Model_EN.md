---
title: "Privacy Governance Interface and Integration Model"
document_id: PGF-03
level: 1
release_version: 1.0.0-rc.1
status: release-candidate
authors: ["Alexey Neyman", "Val Khvatov"]
regulatory_reference_date: 2026-10-26
licence_proposed: "CC BY 4.0 (proposed; subject to rights-holder confirmation)"
source_provenance: "Derived from internal source set ver.2: Level1/3. Privacy_Interface_Integration_Model_Template and Example_ENG.docx.md; sha256 f9761d9bb3aa19c35629c1d087b4109d81b79bc732a47785c184717f7eebdfe1"
---
# PGF-03 — Privacy Governance Interface and Integration Model

*Privacy Governance Framework (PGF) · Level 1 — Strategic Documents · Release 1.0.0-rc.1 · Regulatory reference date: 26 October 2026*

> **Status and use.** Part A is a reusable template. Part B is a worked example for a fictional organisation (PanEuropean Bank AG); all names, figures, dates and records in Part B are illustrative. Nothing in this document is legal advice or a statement about any real organisation, product or provider.

# About This Document

The Privacy Governance Interface and Integration Model is Document 3 of the Privacy Governance Framework (PGF). It defines how privacy governance interfaces with existing corporate functions and governance models, so that the privacy model does not become an isolated silo that duplicates or conflicts with enterprise risk management (ERM), information security, ICT risk and operational resilience, Legal and Compliance, AI governance and model risk, IT, HR, Procurement and outsourcing, or other functions.

This document builds on the Privacy Governance Charter (Document 2), its parent document, and details the boundaries set out in the Charter's Section 4 (What Is Governed and Who Governs) and Section 10 (Scope and Boundaries of the Governance Model). Roles have the meaning fixed in the Charter (Section 8); the allocation of each process to roles is fixed in the RACI Matrix (Document 5) and is not redefined here. The interface map tells each function **where** it meets privacy; Document 5 tells it **who** is responsible, accountable, consulted and informed.

The template is designed for any large organisation operating across multiple jurisdictions. Sections 3.14 and 3.15 apply to financial entities subject to the EU Digital Operational Resilience Act (DORA) and outsourcing rules; other organisations record them as "not applicable" with a reason, or replace them with the equivalent sector regime.

# How to Use This Document

Part A is a drafting template. Bracketed text in bold italics marks a placeholder. Callouts marked **Guidance** explain what belongs in a section and are removed from the adopted document. Part B shows the same structure completed for a fictional large retail bank.

> **Guidance.** Before drafting, confirm that the Charter (Document 2) and the RACI Matrix (Document 5) exist at least in draft, and obtain an up-to-date organisation chart that names the owner of each corporate function. Without it, interfaces cannot be described concretely and the principles of Section 2 have nothing to be matched against.

# Table of Contents

**Part A — Template**  
1. Purpose of This Document  
2. Principles for Identifying Interface Points and Setting Demarcation Rules  
3. Interface Map with Corporate Functions (3.1–3.15)  
4. The "No Duplicate Registers" Rule  
5. Conflict-Resolution Matrix  
6. Relationship to Other Documents of the Model  
7. Review and Amendment  
8. Approval  
**Part B — Worked Example (fictional)** — Sections 1–8 as in Part A  
**Normative Basis and References**  
**International Adaptation**  
**Document History (PGF)**

# Part A — Template

Privacy Governance Interface and Integration Model of ***[Organisation Legal Name]***

Effective date: ***[DD Month YYYY]***   ·   Version: ***[x.x]***   ·   Document owner: ***[Executive Privacy Programme Owner (EPPO)]***   ·   Adopted by: ***[Executive Management]***

Version history (template)

| Version | Date | Changes |
| :---- | :---- | :---- |
| ***[1.0]*** | ***[DD.MM.YYYY]*** | ***[First version of the document]*** |
| ***[x.x]*** | ***[DD.MM.YYYY]*** | ***[Brief description of material changes]*** |

> **Guidance.** Record material changes only — in particular, changes to boundaries with corporate functions or to the arbitrators in the conflict-resolution matrix.

## 1. Purpose of This Document

This document defines how privacy governance at ***[organisation name]*** interfaces with existing corporate functions and governance models — enterprise risk management (ERM), information security, Data Governance, Legal and Compliance, AI governance and model risk, IT Management, HR, Procurement, Client Relationship, corporate management (strategy, budget, internal audit), the Governing Body and its committees, Finance and Accounting, Physical Security and Facilities, ***[ICT risk and operational resilience]*** and ***[outsourcing and ICT third-party risk]*** — so that the privacy model does not duplicate or conflict with them. It does not replace or absorb these functions; it fixes the boundaries and interface points between them and the privacy governance model.

> **Guidance.** If a function listed here is not a standalone function in your organisation, say so explicitly in the relevant section rather than leaving a gap: the absence of a function is itself a boundary to record, with the interim owner of its tasks. Where law requires a function (for example, deployer controls for a high-risk AI system, or an ICT risk control function for a financial entity), its absence is a compliance gap to be escalated, not a boundary.

## 2. Principles for Identifying Interface Points and Setting Demarcation Rules

> **Guidance.** Without explicit principles, the interface map becomes an arbitrary list. The principles below answer two questions: (1) why an interface point exists, and (2) why the boundary is drawn where it is. Every row of the Section 3 map is tagged with the principles applied.

Principles for Identifying Interface Points ("I")

* ***[I1 — Common object of record: an interface point exists wherever privacy governance and another function govern the same object — data, a risk, a vendor, an asset, a system, a model]***
* ***[I2 — Common end-to-end process: an interface point exists wherever both functions take part in the same process — for example, vendor onboarding, incident response, launching a new product]***
* ***[I3 — Shared consequences of a decision: an interface point exists wherever a decision of one function creates consequences or constraints for another]***
* ***[I4 — Common regulatory requirement: an interface point exists wherever the same requirement is addressed to privacy governance and to another function]***

Principles for Setting Demarcation Rules ("D")

* ***[D1 — Primacy of the object owner: the function that owns the object of record (data, a register, a process) keeps operational management of it; privacy governance adds privacy-specific attributes rather than taking it over]***
* ***[D2 — Statutory and gate precedence: where the law or a mandatory gate of the Charter (Section 11) assigns a decision or a statutory task to a specific role — for example, the GDPR breach-notification decision to the controller's designated member of Executive Management, DORA incident reporting to the ICT risk function, the legal compliance gate to Legal, or the DPO's statutory advice and contact-point tasks to the DPO — that allocation prevails over D1, whoever owns the object. D2 protects statutory tasks; it never creates a DPO decision right]***
* ***[D3 — Proportionality of intervention: privacy governance intervenes in another function only as far as necessary to manage privacy risk, without substituting for or duplicating that function]***
* ***[D4 — Single source of truth: where there is a choice between a separate privacy register or process and supplementing an existing corporate one, supplement the existing one (Section 4); independent statutory records required by law are always kept]***
* ***[D5 — Default escalation: if D1–D4 do not yield an unambiguous boundary, the matter is treated as a conflict and resolved under the Section 5 matrix]***

> **Guidance.** Apply D1–D5 in order of priority: D2 prevails over D1; D5 applies only where D1–D4 fail. Map the functions to the Three Lines Model where the organisation uses it: first line — Processing Owners and business units; second line — the EPPO and the privacy function, Legal and Compliance, Risk, the ICT risk function; third line — Independent Internal Audit. The DPO is an independent statutory function that advises all lines and is not part of any management line.

## 3. Interface Map with Corporate Functions

> **Guidance.** Detail the map to sub-domain level where a function is large and heterogeneous (Data Governance, in particular), and keep it at function level elsewhere. Keep the "Principles" column: it shows that the boundary was derived methodically. Use role names from the Charter and Document 5; "privacy" in a row means the privacy function under the EPPO unless another role is named. The DPO appears only in its statutory capacity (advice, monitoring, contact point).

3.1 ERM (Enterprise Risk Management)

| Sub-domain | Interface point | Demarcation rule | Principles |
| :---- | :---- | :---- | :---- |
| ***[Common risk register and taxonomy]*** | ***[The Privacy Risk Register is aggregated into the corporate risk register as a risk category]*** | ***[ERM owns the taxonomy and the register; the EPPO details specific privacy risks within the category (Document 22); each privacy risk record extends the ERM record and is also mapped to the operational-risk event type for clients, products and business practices and, where relevant, to ICT risk; track (a) is never netted]*** | ***[I1, D1, D4]*** |
| ***[Cascading risk appetite]*** | ***[The Privacy Risk Appetite Statement (Document 8) details the corporate risk appetite for the privacy category]*** | ***[The privacy tiers may not be looser than the corporate limit for the category; where the corporate appetite is looser than the privacy tiers, the privacy tiers prevail for rights-and-freedoms risk]*** | ***[I3, D1]*** |
| ***[Organisational consequences]*** | ***[Track (b) organisational-consequence levels (Document 18, Factor F; Document 8, Section 4)]*** | ***[Reported to ERM for the corporate risk profile; never offset rights-and-freedoms risk on track (a)]*** | ***[I3, D3]*** |

> **Guidance.** Add rows relevant to your organisation — for example, the risk-reporting cycle. The boundary with model risk is described once, in Section 3.5 (D4).

3.2 Information Security (CISO)

| Sub-domain | Interface point | Demarcation rule | Principles |
| :---- | :---- | :---- | :---- |
| ***[Access management (IAM)]*** | ***[Role-based access to systems processing personal data]*** | ***[The CISO owns the IAM platform; the privacy function defines "minimum necessary" access requirements]*** | ***[I1, D1, D3]*** |
| ***[Incident response]*** | ***[Response to a security event affecting personal data]*** | ***[The CISO owns detection, triage and technical containment (Document 5, row S7.1). A joint classification step at the start feeds two separate tracks: (1) the privacy function qualifies and records every personal data breach (S7.2, Art. 33(5)); the notification decision — Art. 33 to the competent supervisory authority (for cross-border processing, the lead SA) and Art. 34 to data subjects — is a controller decision taken by the designated member of Executive Management on mandatory DPO advice (S7.3); the DPO is the contact point for the SA; (2) for financial entities, the ICT risk function classifies and reports major ICT-related incidents to the financial supervisor (S7.4; Section 3.14). The clocks are never merged. Where the organisation acts as processor, it notifies the client controller without undue delay under Art. 33(2) and the contract (S7.5). Details: Document 14]*** | ***[I2, I4, D2]*** |

> **Guidance.** Add other information-security sub-domains — encryption and key management, vulnerability management, security monitoring (SOC).

3.3 Data Governance

> **Guidance.** Break Data Governance into its sub-domains — classification, metadata, catalogue, data security, DWH and BI, data integration, stewardship and data quality. For each, record whether there is an intersection with privacy and, if so, the boundary; where there is none, say so (example: Part B, Section 3.6).

| Data Governance sub-domain | Interface point | Demarcation rule | Principles |
| :---- | :---- | :---- | :---- |
| ***[Data Classification]*** | ***[The corporate classification scheme is the basis; privacy adds labels for special categories]*** | ***[The Head of Data Governance owns the scheme (Document 5, row S1); privacy does not create a parallel scheme]*** | ***[I1, D1, D4]*** |
| ***[Metadata Management]*** | ***[Metadata on origin, owner and purpose of data feed the RoPA and the Data Inventory]*** | ***[Data Governance owns the metadata platform; privacy consumes metadata and enriches it with privacy attributes (sensitivity category, residual tier, date of last DPIA), without a parallel lineage catalogue]*** | ***[I1, D1, D4]*** |
| ***[Data Catalogue]*** | ***[The unified catalogue identifies where personal data are processed; outputs of privacy transformations (pseudonymised and synthetic datasets) are registered as new objects]*** | ***[Data Governance owns the catalogue; privacy uses a "contains personal data" flag and registers its own transformation outputs in it]*** | ***[I1, D1, D4]*** |

> **Guidance.** The DPO should not report to the head of Data Governance (for example, a Chief Data Officer), who typically determines purposes and means of analytics processing. If it does, record the reporting line and the compensating measures (Document 4, Section 7). Disagreements between Data Governance and the privacy function are resolved under Section 5, not through a reporting line.

3.4 Legal and Compliance

| Sub-domain | Interface point | Demarcation rule | Principles |
| :---- | :---- | :---- | :---- |
| ***[Legal compliance gate]*** | ***[Lawful basis, Art. 9/10 condition, compatibility, transparency, Art. 22, transfer tool, statutory deadlines]*** | ***[Legal owns G-L, the G-36 test conclusion and the G-TIA determination (Charter, Section 11); the DPO advises]*** | ***[I4, D2]*** |
| ***[Contract work]*** | ***[Art. 28 contracts with processors; data-sharing agreements with independent controllers; Art. 26 arrangements]*** | ***[Legal drafts and negotiates; the Processing Owner decides on the engagement (Document 5, row S6.2); the DPO advises; terms follow Document 17]*** | ***[I2, D1, D3]*** |
| ***[AML/KYC compliance]*** | ***[Personal data processed for customer due diligence and transaction monitoring]*** | ***[Compliance owns the AML/KYC procedure; Legal confirms the lawful basis and permissible scope at G-L; restrictions on data subject rights under AML law are applied case by case under Document 15]*** | ***[I2, I4, D3]*** |
| ***[Regulatory monitoring]*** | ***[Changes in data protection and adjacent law]*** | ***[Legal and Privacy Officers identify changes; the EPPO is accountable for updating the Regulatory Applicability Matrix (Document 7, Section 6); the DPO advises]*** | ***[I4, D1]*** |
| ***[Litigation and requests from authorities (process G4.2, Document 24)]*** | ***[Disclosure of personal data to courts or authorities]*** | ***[Legal assesses whether the request is binding — including requests from third-country authorities, which are recognised only under an international agreement (Art. 48); the privacy function limits the disclosure to what is required]*** | ***[I3, D3]*** |

3.5 AI Governance and Model Risk

> **Guidance.** Record the organisation's AI governance function (AI system inventory, AI Act role and risk classification, provider or deployer duties) and its model-risk function (validation of accuracy, robustness and drift; prudential model-risk requirements where they apply). If an AI system that the organisation uses is high-risk under the EU AI Act, deployer controls must exist by the date the obligations apply — human oversight, log retention, information to affected persons and, for deployers of Annex III point 5(b) or 5(c) systems, a fundamental rights impact assessment (FRIA, Art. 27) that complements the DPIA. The organisation is a provider, with further duties, where it develops the system and puts it into service under its own name. Under the AI Act as amended by the AI Omnibus (in force 27 July 2026), obligations for Annex III high-risk systems apply from 2 December 2027; GDPR duties, including Art. 22, apply now. The NIST AI Risk Management Framework (Govern, Map functions) can structure the interface where no regulatory regime applies.

| Sub-domain | Interface point | Demarcation rule | Principles |
| :---- | :---- | :---- | :---- |
| ***[AI system inventory and classification]*** | ***[AI systems that process personal data or make or support decisions about individuals]*** | ***[The AI governance function owns the inventory and the AI Act classification and role determination; privacy adds a "processes personal data" flag and a link to the DPIA]*** | ***[I1, D1, D4]*** |
| ***[Model lifecycle (development, validation, monitoring)]*** | ***[Models trained on personal data or deciding about individuals]*** | ***[The model-risk function owns technical validation (accuracy, robustness, drift, bias testing); the Processing Owner owns the DPIA and the privacy measures in training and operation; Legal confirms the lawful basis at G-L; the DPO advises]*** | ***[I1, I3, D3]*** |
| ***[AI Act deployer duties, including the FRIA]*** | ***[Human oversight, logs, information to affected persons, FRIA for Annex III 5(b)/(c) systems]*** | ***[The AI governance function is responsible for preparing them; the Processing Owner is accountable; the DPO and Legal are consulted; the EPPO is informed (Document 5, statutory row "AI Act deployer duties"). The FRIA reuses the DPIA where the DPIA already covers an obligation (Art. 27(4))]*** | ***[I4, D2, D4]*** |
| ***[Explanation of individual decisions]*** | ***[Meaningful information about the logic of automated decisions (GDPR Arts. 13–15, 22) and, once applicable, the AI Act right to explanation (Art. 86)]*** | ***[The model-risk / AI function provides the technical explanation capability; the Processing Owner owns the explanation given to the individual; the DPO advises and monitors]*** | ***[I3, D1]*** |
| ***[Model registry]*** | ***[Models included in the model registry]*** | ***[The model-risk function owns the registry; privacy adds a personal-data flag and the DPIA link]*** | ***[I1, D1, D4]*** |

3.6 IT Management

| Sub-domain | Interface point | Demarcation rule | Principles |
| :---- | :---- | :---- | :---- |
| ***[Infrastructure and cloud management]*** | ***[Hosting of personal data, including the jurisdiction of hosting and remote access]*** | ***[IT owns the infrastructure and selects providers; Legal determines at G-L whether hosting or remote access constitutes a transfer, on the three cumulative criteria of EDPB Guidelines 05/2021 (exporter subject to the GDPR; data made available — including by remote access — to another controller, joint controller or processor, which may be a separate group entity; importer in a third country). Remote access by the organisation's own employees while abroad is not a transfer, though security and other obligations apply. A transfer passes G-TIA before it starts; the Processing Owner decides on the transfer tool (Documents 12 and 20)]*** | ***[I1, I4, D2, D3]*** |
| ***[Software development (SDLC)]*** | ***[Privacy by design in the development lifecycle]*** | ***[IT/Engineering own the development process; the hard requirements are G-L and DPIA triage before production, and a completed DPIA where triage requires one (Document 16)]*** | ***[I2, D3]*** |
| ***[Change management]*** | ***[Changes to systems processing personal data]*** | ***[IT owns change management; changes that alter purposes, data categories, recipients or risk are routed to the gates before deployment; a release is held until the gates are recorded]*** | ***[I2, D2, D3]*** |

> **Guidance.** Add other sub-domains — IT service management, and the like. Where a sub-domain has no intersection with privacy, record "[sub-domain] | Does not affect personal data | No intersection with privacy governance identified | —" rather than omitting it.

3.7 HR

| Sub-domain | Interface point | Demarcation rule | Principles |
| :---- | :---- | :---- | :---- |
| ***[Personnel data]*** | ***[Processing of employee and candidate data]*** | ***[HR owns the processing and the staff privacy notice; the privacy function assesses risks (for example, workplace-monitoring systems or HR analytics) and checks the notice against Document 1; the DPO advises; co-determination rights of employee representatives under national law are respected]*** | ***[I1, D1, D4]*** |
| ***[Training and awareness]*** | ***[Delivery of privacy training]*** | ***[HR delivers through the corporate LMS; the Privacy Operations Lead owns the content; the EPPO is accountable (Document 5, row S8); the DPO is consulted and runs its own awareness-raising (row S8.1)]*** | ***[I2, D1, D3]*** |

> **Guidance.** Add other sub-domains — disciplinary measures for breaches of privacy policies, and the like.

3.8 Procurement

| Sub-domain | Interface point | Demarcation rule | Principles |
| :---- | :---- | :---- | :---- |
| ***[Vendor due diligence]*** | ***[Assessment of a vendor's privacy risk]*** | ***[Procurement owns the due-diligence process; the privacy assessment is a mandatory module of it, accountable to the Privacy Operations Lead (Document 5, row S6.1; Document 17)]*** | ***[I2, D1, D4]*** |
| ***[Vendor register]*** | ***[Contract type (Art. 28 / data-sharing agreement / Art. 26) and privacy-assessment results per vendor]*** | ***[Procurement owns the vendor register; privacy adds its fields; for financial entities, see Section 3.15 for the DORA Register of Information]*** | ***[I1, D1, D4]*** |

3.9 Client Relationship (customer engagement, CRM, marketing)

| Sub-domain | Interface point | Demarcation rule | Principles |
| :---- | :---- | :---- | :---- |
| ***[Marketing consent management]*** | ***[Collection, storage and withdrawal of marketing consent]*** | ***[The Processing Owner (marketing) owns design, collection and withdrawal; the Privacy Operations Lead owns storage and proof of consent; the DPO advises on design (Document 5, row C5; Document 13)]*** | ***[I1, I4, D3]*** |
| ***[Profiling for personalisation]*** | ***[Use of behavioural data for personalised offers]*** | ***[The Processing Owner determines the business logic and owns the DPIA where required; Legal confirms the lawful basis; the DPO advises]*** | ***[I2, I3, D3]*** |
| ***[Complaints and enquiries]*** | ***[Customer complaints about the processing of personal data]*** | ***[The contact centre owns the general complaints process; privacy complaints are routed to the privacy operations team (Document 5, row C3); complaints addressed to the DPO are handled by the DPO under confidentiality (Art. 38(4)–(5))]*** | ***[I2, D2]*** |

3.10 Corporate Management (Strategy, Budget, Internal Audit)

| Sub-domain | Interface point | Demarcation rule | Principles |
| :---- | :---- | :---- | :---- |
| ***[Strategic planning]*** | ***[Initiatives introducing new types of processing]*** | ***[Corporate management owns planning; G-L and DPIA triage run at initiative assessment, before budget approval]*** | ***[I2, D3]*** |
| ***[Budgeting]*** | ***[Budget of the privacy programme and of the DPO]*** | ***[The general budget process allocates funds; the EPPO justifies the programme budget (Document 4); Executive Management ensures the DPO's resources (Art. 38(2)) through a separate budget line]*** | ***[I2, D1, D2]*** |
| ***[Internal audit]*** | ***[Independent assurance over the privacy programme]*** | ***[The Chief Audit Executive drafts and executes the internal-audit charter, the risk-based audit plan and significant plan changes; the Audit Committee approves them (IIA Global Internal Audit Standards 2024, Standards 6.2 and 9.4 — a governance basis, not a GDPR obligation); the DPO's compliance monitoring (Art. 39(1)(b)) is separate and is an input; privacy provides the audit object (Document 27) and does not audit itself]*** | ***[I2, D1]*** |

3.11 Governing Body and Committees

| Sub-domain | Interface point | Demarcation rule | Principles |
| :---- | :---- | :---- | :---- |
| ***[Governing Body committees (Risk, Audit)]*** | ***[Oversight of the programme]*** | ***[The committees oversee and receive assurance; they do not take management decisions or accept operational risk; consent applies only to matters their rules reserve]*** | ***[I1, D1]*** |
| ***[Privacy Risk Committee]*** | ***[Placement and mandate]*** | ***[A management-level committee chaired by the EPPO or a member of Executive Management, established by Executive Management; the DPO attends as an independent, non-voting adviser. It is not a Governing Body committee]*** | ***[I1, D1]*** |
| ***[Reporting to the Governing Body]*** | ***[Periodic reporting on the programme]*** | ***[The corporate secretariat sets the format; the EPPO prepares the programme report (Document 5, row G8.1; Document 31); the DPO's own report to the highest management level (row G8.2) is separate and goes to the Governing Body committee where the DPO considers it necessary]*** | ***[I2, D1, D3]*** |

3.12 Finance and Accounting

| Sub-domain | Interface point | Demarcation rule | Principles |
| :---- | :---- | :---- | :---- |
| ***[Shareholder register and corporate payments]*** | ***[Personal data of individual shareholders]*** | ***[Finance / Investor Relations owns the register and payments; retention and minimisation follow the retention schedule (Document 11)]*** | ***[I1, D1, D4]*** |
| ***[Payments and accounting]*** | ***[Personal data in payments to individuals and in accounting records]*** | ***[Finance owns the systems; the retention schedule sets which records are kept for tax and accounting law, to avoid excessive retention]*** | ***[I1, D1, D3]*** |

> **Guidance.** Add other sub-domains — corporate cards, treasury operations, and the like.

3.13 Physical Security and Facilities

| Sub-domain | Interface point | Demarcation rule | Principles |
| :---- | :---- | :---- | :---- |
| ***[Video surveillance (CCTV)]*** | ***[Recordings that may capture customers, employees and visitors]*** | ***[Physical security owns the infrastructure; the retention period and access rules follow the retention schedule and the video-surveillance notice; the lawful basis is confirmed at G-L]*** | ***[I1, D1, D3]*** |
| ***[Visitor logs]*** | ***[Visitor data — name, ID document, purpose, host]*** | ***[Facilities owns the registration process; the privacy function sets the minimum data and the retention period through the retention schedule]*** | ***[I1, D3]*** |

> **Guidance.** Add other sub-domains — physical access control, including biometric access, and the like.

3.14 ICT Risk and Operational Resilience (financial entities subject to DORA)

> **Guidance.** For financial entities, DORA (Regulation (EU) 2022/2554, applicable since 17 January 2025) sets an ICT risk management framework, an independent ICT risk control function, incident classification and reporting, resilience testing and ICT third-party risk rules. It is not a data protection law, and its incident track is separate from the GDPR breach track. NIS2 (Directive (EU) 2022/2555): where DORA applies as a sector-specific Union act, its ICT risk management and incident-reporting provisions apply instead of the corresponding NIS2 provisions (NIS2 Art. 4); non-financial group entities may still be in NIS2 scope under national transposition. Organisations outside DORA replace this section with their sector's operational-resilience regime or record it as not applicable.

| Sub-domain | Interface point | Demarcation rule | Principles |
| :---- | :---- | :---- | :---- |
| ***[ICT risk management framework]*** | ***[Protection of ICT assets that process personal data]*** | ***[The ICT risk function owns the framework (DORA Art. 6) under the management body's responsibility (Art. 5); privacy requirements for systems with personal data are fed in through the CISO and the asset register; no parallel privacy control framework]*** | ***[I1, I4, D1, D4]*** |
| ***[Major ICT-related incident classification and reporting]*** | ***[An incident that is both a personal data breach and a major ICT-related incident]*** | ***[The ICT risk function classifies under Commission Delegated Regulation (EU) 2024/1772 and reports to the financial supervisor under Commission Delegated Regulation (EU) 2025/301 and the related implementing standards (Document 5, row S7.4); the GDPR notification to the competent SA follows its own test and clock (Section 3.2). The two tracks share the joint classification step and facts, not decisions or deadlines]*** | ***[I2, I4, D2]*** |
| ***[Digital operational resilience testing]*** | ***[Tests, including threat-led penetration testing, that use production data containing personal data]*** | ***[The ICT risk function owns the testing programme; use of personal data in tests passes G-L and DPIA triage; test data are minimised or pseudonymised where the test objective allows]*** | ***[I2, D3]*** |
| ***[Cyber-threat information sharing]*** | ***[Indicators shared with other financial entities that may contain personal data]*** | ***[The CISO owns participation; Legal confirms the lawful basis for any personal data shared]*** | ***[I3, I4, D3]*** |

3.15 Outsourcing and ICT Third-Party Risk

> **Guidance.** Financial entities keep statutory registers of outsourcing arrangements (for example under the EBA Guidelines on outsourcing arrangements, EBA/GL/2019/02, and national law) and of ICT third-party contractual arrangements (DORA Register of Information, Art. 28(3)). DORA also prescribes key contractual provisions, including data location (Art. 30). Privacy does not create a third vendor register: it adds its fields (processor/controller role, Art. 28 status, transfer mechanism, TIA reference) and links them to these registers by a common vendor identifier.

| Sub-domain | Interface point | Demarcation rule | Principles |
| :---- | :---- | :---- | :---- |
| ***[Outsourcing governance and register]*** | ***[Outsourced functions that involve personal data]*** | ***[The outsourcing function owns the outsourcing register and the outsourcing assessment; the privacy due-diligence module (Document 17) is part of it]*** | ***[I1, I2, D1, D4]*** |
| ***[DORA Register of Information]*** | ***[ICT third-party arrangements that involve personal data]*** | ***[The ICT risk function (or the designated owner) maintains the Register of Information; privacy fields are linked to it, not copied]*** | ***[I1, I4, D1, D4]*** |
| ***[Contract terms]*** | ***[Data location, audit and access rights, exit]*** | ***[Legal aligns DORA Art. 30 terms, outsourcing terms and Art. 28(3) GDPR terms in one contract set; the Processing Owner decides on the engagement]*** | ***[I2, I4, D3]*** |

## 4. The "No Duplicate Registers" Rule

> **Guidance.** This rule applies principle D4. It prevents the privacy function from creating its own register of data, risks or vendors in parallel with an existing corporate register, which inevitably diverges over time. It does not remove independent statutory records that the law requires.

If the organisation already has a corporate register covering the same object of record, the privacy function ***[must]*** use that register and add privacy-specific fields, rather than creating a parallel register. One authoritative record is kept per fact; views, extracts and linked evidence records are allowed.

| Object of record | Priority source | Privacy-specific addition |
| :---- | :---- | :---- |
| ***[Data Catalogue]*** | ***[The corporate data and systems catalogue (Section 3.3)]*** | ***[Sensitivity label for personal data]*** |
| ***[Risk register]*** | ***[The corporate risk register (ERM)]*** | ***[Specific privacy risk, its residual tier and decider]*** |
| ***[Vendor register]*** | ***[Procurement's vendor register]*** | ***[Role (processor / independent controller / joint controller), contract type, privacy-assessment result]*** |
| ***[Outsourcing register; ICT third-party Register of Information (financial entities)]*** | ***[The outsourcing function's register; the DORA Register of Information (Section 3.15)]*** | ***[Link to the vendor's privacy fields; transfer mechanism and TIA reference]*** |
| ***[Asset/system register]*** | ***[The IT/InfoSec asset register]*** | ***[Flag for processing of personal data and its extent]*** |
| ***[Model registry; AI system inventory]*** | ***[The model-risk registry; the AI governance inventory (Section 3.5)]*** | ***[Personal-data flag and DPIA link; FRIA link where applicable]*** |

Statutory-records exception. Independent records required by law are always kept, even where they overlap with a corporate register — for example the record of processing activities (GDPR Art. 30), the breach record (Art. 33(5)), the DORA Register of Information and incident records, the PIPEDA record of every breach of security safeguards and the Québec confidentiality-incident register. They are linked to the corporate registers by common identifiers; they are not merged into them or replaced by them.

> **Guidance.** If no suitable corporate register exists, creating a privacy-specific register is permissible, but the decision and its rationale are recorded rather than adopted by default.

## 5. Conflict-Resolution Matrix

> **Guidance.** A conflict between a privacy requirement and another function's requirement is expected wherever D1–D4 do not yield a rule. Name specific arbitrators. Three limits apply to every row: (1) a G-L or G-TIA failure is not arbitrated — it means stop, redesign or suspend, and no function or committee can override it; (2) the DPO is never an arbitrator or decision-maker — it gives advice, which is recorded, and may escalate directly to Executive Management; a decision-maker who departs from the DPO's advice records the reasons (Document 18); (3) the final arbiter is ***[Executive Management]***; the Governing Body is informed and gives consent only where its rules reserve the matter.

| Conflict type | Example | Arbitrator (decision per Document 5) | Escalation | Resolution timeframe |
| :---- | :---- | :---- | :---- | :---- |
| ***[Privacy vs InfoSec]*** | ***[Security-log retention exceeds the retention schedule]*** | ***[EPPO and CISO jointly; DPO advice recorded]*** | ***[Privacy Risk Committee → Executive Management]*** | ***[X business days]*** |
| ***[Privacy vs ERM]*** | ***[The corporate risk appetite permits more risk than the Privacy Risk Appetite Statement]*** | ***[EPPO and the Chief Risk Officer jointly; the privacy tiers prevail for rights-and-freedoms risk]*** | ***[Executive Management (adopts both appetites); Governing Body Risk Committee informed]*** | ***[X business days]*** |
| ***[Privacy vs Data Governance]*** | ***[The classification scheme lacks detail for special categories]*** | ***[EPPO and the Head of Data Governance jointly]*** | ***[Privacy Risk Committee → Executive Management]*** | ***[X business days]*** |
| ***[Privacy vs Procurement]*** | ***[A commercially advantageous vendor fails privacy due diligence]*** | ***[The Processing Owner decides on the engagement (S6.2) on the due-diligence result; a failed G-L or G-TIA is not overridable]*** | ***[Privacy Risk Committee → Executive Management]*** | ***[X business days]*** |
| ***[Privacy vs a business unit]*** | ***[A product team wants to launch before G-L and DPIA triage are complete]*** | ***[No arbitration on the gate: the release is held until G-L and DPIA triage are recorded and, where required, the DPIA completed; disagreement on scope or measures — Processing Owner and EPPO]*** | ***[Privacy Risk Committee → Executive Management]*** | ***[Hold immediately; resolve within X business days]*** |
| ***[Privacy vs IT Management]*** | ***[A change to a system with personal data is to be deployed without impact triage]*** | ***[Change is held until triage is recorded; IT Management owner and EPPO]*** | ***[Privacy Risk Committee → Executive Management]*** | ***[X business days]*** |
| ***[Privacy vs AI governance / model risk]*** | ***[The model owner wants a broader dataset than minimisation allows]*** | ***[Processing Owner and EPPO, with the model-risk function; Legal confirms whether G-L is met]*** | ***[Privacy Risk Committee → Executive Management]*** | ***[X business days]*** |
| ***[Privacy vs Client Relationship]*** | ***[Marketing wants profiling beyond the scope assessed in the DPIA]*** | ***[The extension is held until the DPIA is updated; Processing Owner and EPPO]*** | ***[Privacy Risk Committee → Executive Management]*** | ***[X business days]*** |
| ***[Privacy vs ICT risk (DORA)]*** | ***[Disagreement on whether an incident record may contain full customer identifiers]*** | ***[Head of the ICT risk function and EPPO jointly; statutory reporting content prevails where the law prescribes it]*** | ***[Executive Management]*** | ***[X business days, never delaying a statutory report]*** |
| ***[Privacy vs Corporate Management]*** | ***[The budget does not fund the remediation of a breached risk limit]*** | ***[EPPO and the budget owner jointly]*** | ***[Executive Management; Governing Body committee informed]*** | ***[X business days]*** |

In all cases not resolved by the named arbitrators, the final decision is taken by ***[Executive Management]***, through one named member or the body as a whole, on the recommendation of the Privacy Risk Committee and after the DPO's advice. The Governing Body's committee is informed; its consent is needed only where its rules reserve the matter.

## 6. Relationship to Other Documents of the Model

This document builds on the Charter (Document 2) and details the boundaries of its Sections 4 and 10. Role allocation is fixed in the RACI Matrix (Document 5). This document sets external boundaries for:

* ***[the Privacy Risk Appetite Statement (Document 8) — alignment with the corporate risk appetite through the ERM interface, Section 3.1]***
* ***[the Data Classification Policy (Document 10) — the boundary with Data Governance, Section 3.3]***
* ***[the Data Breach Response Policy (Document 14) — the boundaries with information security and ICT risk, Sections 3.2 and 3.14]***
* ***[the Vendor and Third-Party Privacy Risk Policy (Document 17) — the boundaries with Procurement and outsourcing, Sections 3.8 and 3.15]***
* ***[the DPIA Methodology (Document 19) — the boundary with AI governance and the FRIA, Section 3.5]***
* ***[the Regulatory Applicability Matrix (Document 7) — the adjacent regimes (DORA, AI Act, NIS2, outsourcing) whose applicability it records]***

The conflict-resolution matrix (Section 5) applies to all documents of the model and is not duplicated in them.

## 7. Review and Amendment

This document is reviewed on the terms of the continuous-improvement principle (Charter, Section 7) and ***[the Policy Review Cycle, Document 29]***, and upon every change to the organisational structure that affects the corporate functions in Section 3. Amendments are prepared by ***[the EPPO]***, with the DPO's advice, and adopted by ***[Executive Management]***.

Procedure for Adding a New Corporate Function to the Map

> **Guidance.** Section 3 covers the functions existing at adoption. When a new function emerges (for example, an ESG/Sustainability function), extend the map under this procedure rather than waiting for the scheduled review.

* ***[Step 1 — apply I1–I4 to the new function and record whether an interface point exists; the absence of one is recorded explicitly]***
* ***[Step 2 — where an interface point exists, apply D1–D5 to set the demarcation rule]***
* ***[Step 3 — add the function as Section 3.16 onward, following the pattern of the existing sections; update Section 1]***
* ***[Step 4 — assess whether a new conflict type is needed in Section 5]***
* ***[Step 5 — record the change in the version history and route it for adoption]***

The procedure applies in reverse when a function is discontinued or merged: the corresponding section is deleted or consolidated, not left as a stale entry.

## 8. Approval

This document was adopted by ***[Executive Management]*** on ***[date]***, after the DPO's advice. Document owner: ***[EPPO]***.

# Part B — Worked Example (fictional)

PanEuropean Bank AG — Privacy Governance Interface and Integration Model

Effective date: 20 October 2026   ·   Version: 3.0   ·   Document owner: Chief Privacy Officer (EPPO)   ·   Adopted by: Management Board

*Fictional entity, prepared for illustration only.*

Fictional document history (illustrative)

| Version | Date | Changes |
| :---- | :---- | :---- |
| 1.0 | 1 March 2026 | First version, developed alongside the Privacy Governance Charter |
| 2.0 | 29 August 2026 | Sections 3.12 (Finance and Accounting) and 3.13 (Physical Security and Facilities) added for full coverage of the Charter's data domains; escalation matrix harmonised |
| 3.0 | 20 October 2026 | Aligned with Charter v3.0 and the RACI Matrix v4.0: Chief Privacy Officer as EPPO and owner; Group DPO limited to advice, monitoring and contact-point tasks — vetoes and final decisions removed; breach rows split into the GDPR track (HBDI) and the DORA track (ECB/BaFin); Sections 3.14 (ICT Risk and Operational Resilience) and 3.15 (Outsourcing and ICT Third-Party Risk) added; Section 3.5 rewritten around the Model Risk and AI Governance function and AI Act deployer duties; Management Board as single final arbiter; the Group DPO no longer reports to the CDO |

## 1. Purpose of This Document

This document defines how privacy governance at PanEuropean Bank AG interfaces with ERM, information security, Data Governance, Legal and Compliance, Model Risk and AI Governance, IT, HR, Procurement, Client Relationship, corporate management, the Supervisory Board and its committees, Finance and Accounting, Corporate Security and Facilities, ICT Risk Control (DORA), and the outsourcing function — so that the privacy model does not duplicate or conflict with them.

## 2. Principles for Identifying Interface Points and Setting Demarcation Rules

Principles for Identifying Interface Points ("I")

* I1 — Common object of record: for example, PanEuropean's Data Catalogue is used by both Data Governance and the privacy function
* I2 — Common end-to-end process: for example, onboarding a new vendor runs through Procurement, outsourcing and privacy due diligence as one process
* I3 — Shared consequences of a decision: for example, a CRO proposal to raise the fraud-risk appetite affects the privacy tiers for anti-fraud scoring
* I4 — Common regulatory requirement: for example, supervisory expectations on credit-scoring models (EBA Guidelines on loan origination and monitoring, EBA/GL/2020/06) and the AI Act's high-risk requirements are addressed to Model Risk and AI Governance, Credit Decisions and privacy at the same time

Principles for Setting Demarcation Rules ("D")

* D1 — Primacy of the object owner: Data Governance keeps the classification scheme; privacy adds the enhanced regime for special categories
* D2 — Statutory and gate precedence: the GDPR breach-notification decision belongs to the CRO (deputy COO) on mandatory Group DPO advice, and DORA reporting to ICT Risk Control, although the incident technically belongs to the CISO; G-L belongs to General Counsel whoever owns the system
* D3 — Proportionality of intervention: privacy does not dictate the engineering process; it requires G-L and DPIA triage before go-live
* D4 — Single source of truth: the Privacy Risk Register is part of the corporate risk register, not a standalone document
* D5 — Default escalation: unresolved boundaries (for example, the retention period of anti-fraud logs) go to the Section 5 matrix

Three Lines Model at PanEuropean: first line — Processing Owners and business units; second line — the Chief Privacy Officer's privacy function, General Counsel and Compliance, ERM, ICT Risk Control, Model Risk and AI Governance; third line — Group Internal Audit. The Group DPO advises all lines and is not part of any management line.

## 3. Interface Map with Corporate Functions

3.1 ERM (Chief Risk Officer)

| Sub-domain | Interface point | Demarcation rule | Principles |
| :---- | :---- | :---- | :---- |
| Common risk register and taxonomy | The Privacy Risk Register is part of the corporate risk register as the "Conduct & Privacy Risk" category | ERM owns the taxonomy and register; the Chief Privacy Officer details specific risks within the category; each record extends the ERM record and is also mapped to the operational-risk event type for clients, products and business practices and, where relevant, to ICT risk; track (a) is never netted | I1, D1, D4 |
| Cascading risk appetite | The Privacy Risk Appetite Statement details the corporate appetite for "Conduct & Privacy Risk" | Both are adopted by the Management Board; the privacy tiers prevail for rights-and-freedoms risk | I3, D1 |
| Organisational consequences | Track (b) levels for privacy scenarios (regulatory, financial, reputational) | Reported to ERM quarterly; never offset track (a) | I3, D3 |
| Risk-reporting cycle | Privacy risks in the quarterly risk report to the Risk Committee of the Supervisory Board | ERM sets the format; the Chief Privacy Officer prepares the privacy content | I2, D3 |
| Model risk for anti-fraud and scoring models | Accuracy and robustness of scoring and anti-fraud models affect risk to customers | Described once, in Section 3.5 (D4) | I3, D4 |

3.2 Information Security (CISO)

| Sub-domain | Interface point | Demarcation rule | Principles |
| :---- | :---- | :---- | :---- |
| Access management (IAM) | Role-based access for Credit Decisions, Digital Banking, Marketing and Customer Service staff | The CISO owns the IAM platform; Privacy Officers define the "minimum necessary" access scope per role | I1, D1, D3 |
| Encryption and key management | TLS 1.3 in transit, AES-256 at rest for customer data | The CISO implements and operates; privacy requires encryption for all personal data | I1, D1 |
| Vulnerability management | Vulnerabilities in core banking systems with customer data | The CISO runs patch management; the Privacy Operations Lead receives priority notice of vulnerabilities affecting systems with personal data | I3, D3 |
| Security monitoring (SOC) | Detection of anomalous activity involving customer data | The CISO owns the SOC; a mass export of customer data is escalated immediately to the Privacy Operations Lead as a potential personal data breach | I2, D1, D3 |
| Incident response | An incident affecting customer personal data | The CISO contains the incident and convenes a joint classification call with Privacy Officers and ICT Risk Control. Track 1 (GDPR): Privacy Officers qualify and record every breach (Chief Privacy Officer accountable); the CRO (deputy COO) decides on notification to the HBDI as lead SA within 72 hours of awareness, and on communication to customers where the risk is high, on mandatory Group DPO advice; the Group DPO is the contact point for the HBDI. Track 2 (DORA): ICT Risk Control classifies and reports major ICT-related incidents to the ECB/BaFin (Section 3.14). Where PanEuropean acts as processor for a group company, the head of the service unit notifies that controller without undue delay (Art. 33(2)) | I2, I4, D2 |

3.3 Data Governance (Chief Data Officer)

| Data Governance sub-domain | Interface point | Demarcation rule | Principles |
| :---- | :---- | :---- | :---- |
| Data Classification | The corporate classification scheme; privacy labels for special categories (health data for payment protection insurance; biometric data) | The CDO owns the scheme; privacy does not create a parallel one | I1, D1, D4 |
| Metadata Management | Metadata on origin and purpose of data feed PanEuropean's RoPA and Data Inventory | Data Governance owns the metadata platform; privacy consumes metadata and enriches it with privacy attributes (sensitivity category, residual tier, date of last DPIA) from the Bank's privacy engineering platform (PEP, illustrative), without a parallel catalogue | I1, D1, D4 |
| Data Security | Protective measures at storage and processing level | Shared with the CISO (Section 3.2); privacy sets requirements for special categories | I1, D3 |
| Data Catalogue | The unified catalogue identifies systems processing personal data; pseudonymised and synthetic datasets produced on PEP are registered as new objects | Data Governance owns the catalogue; privacy uses a "contains personal data" flag and registers PEP transformation outputs | I1, D1, D4 |
| DWH and BI | Customer data flowing into the data warehouse and BI | Data Governance and IT own the platform; customer identifiers are pseudonymised before loading into analytics layers, using PEP | I1, I3, D3 |
| Data Integration | Data flows between core banking, PEP and external providers | Data Governance and IT own the integration platform; flows involving third countries (remote support from India) are reflected in the Data Inventory and pass G-TIA; ETL jobs that process customer data or derived datasets pass privacy risk controls before production | I1, I4, D3 |
| Stewardship and data quality | The data-owner/steward role model | Data Governance owns the stewardship model; privacy adds personal-data duties to the data-steward role; Processing Owners are designated separately by the Management Board (Document 25, Section 10) | I1, D1, D4 |

The Group DPO does not report to the CDO; it reports directly to the Management Board (Document 4, Section 7). Disagreements between the CDO and the privacy function are resolved under Section 5, with the Management Board as final arbiter.

3.4 Legal and Compliance (General Counsel; Head of Compliance)

| Sub-domain | Interface point | Demarcation rule | Principles |
| :---- | :---- | :---- | :---- |
| Legal compliance gate | G-L, G-36 test conclusion and G-TIA determination | General Counsel owns them; the Group DPO advises | I4, D2 |
| Contract work | Art. 28 contracts with the core banking platform provider, Example Cloud Services Pvt Ltd and Example AI Provider Inc. (both fictional); the data-sharing agreement with EuroCredit Bureau (fictional, independent controller); the Art. 26 arrangement of the anti-fraud consortium | Legal drafts and negotiates; the relevant Processing Owner decides on the engagement; the Group DPO advises | I2, D1, D3 |
| Regulatory monitoring | Changes to GDPR, BDSG, national law and adjacent regimes in the five countries of operation | General Counsel and Privacy Officers identify changes; the Chief Privacy Officer is accountable for updating the Regulatory Applicability Matrix; the Group DPO advises | I4, D1 |
| AML/KYC compliance | Personal data in customer due diligence and transaction monitoring | Compliance owns the AML/KYC procedure; General Counsel confirms the lawful basis and scope at G-L; the prohibition on disclosing suspicious-activity reports is applied in rights handling case by case | I2, I4, D3 |
| Litigation and requests from authorities (process G4.2, Document 24) | Disclosure of customer data to a court or authority | General Counsel assesses whether the request is binding, including requests from third-country authorities (Art. 48); the Privacy Operations Lead limits the disclosure to what is required | I3, D3 |

3.5 Model Risk and AI Governance

PanEuropean's Model Risk and AI Governance function sits in the CRO area (second line). It maintains the AI system inventory and the model registry, determines each system's classification and PanEuropean's role (provider or deployer) under the AI Act, validates scoring and anti-fraud models, and coordinates AI Act deployer duties under the bank's AI Governance Policy. The retail credit-scoring system is a high-risk AI system under Annex III point 5(b); its high-risk obligations apply from 2 December 2027 under the AI Act as amended by the AI Omnibus (in force 27 July 2026). Because PanEuropean develops the scoring model itself, it is also the provider of that system. GDPR duties, including Art. 22, apply now and are recorded in `DPIA-CS-TRAIN-01`, `DPIA-CS-INFER-01` and `DPIA-CS-LAUNCH-01`. Anti-fraud detection is outside Annex III point 5(b).

| Sub-domain | Interface point | Demarcation rule | Principles |
| :---- | :---- | :---- | :---- |
| AI system inventory and classification | Credit scoring, anti-fraud models, the customer-service assistant (Example AI Provider Inc., fictional) | Model Risk and AI Governance owns the inventory and classification; privacy adds a personal-data flag and the DPIA link | I1, D1, D4 |
| Model lifecycle | Scoring and anti-fraud models trained on customer data or synthetic data generated from it | Model Risk and AI Governance validates accuracy, robustness, drift and bias; the Head of Credit Decisions owns the DPIAs and the privacy measures (synthetic training data on PEP); General Counsel confirms the lawful basis; the Group DPO advises | I1, I3, D3 |
| AI Act deployer and provider duties, including the FRIA | Human oversight, log retention, information to affected persons, FRIA for credit scoring | Model Risk and AI Governance prepares them; the Head of Credit Decisions is accountable; the Group DPO and General Counsel are consulted; the Chief Privacy Officer is informed. The FRIA for credit scoring is planned for completion before 2 December 2027 and reuses `DPIA-CS-INFER-01` where it already covers an obligation | I4, D2, D4 |
| Explanation of credit decisions | The customer's right to meaningful information about the logic and to an explanation of the decision | Model Risk and AI Governance provides the factor-level explanation capability; Credit Decisions owns the explanation given to the customer and the "Request a Review" process; the Group DPO advises and monitors | I3, D1 |
| Model registry | Scoring and anti-fraud models | Model Risk and AI Governance owns the registry; privacy adds the personal-data flag and the DPIA link | I1, D1, D4 |
| Market surveillance | Oversight of high-risk AI used by the bank by the market-surveillance authority | Under the AI Act, the financial supervisory authority acts as market-surveillance authority for high-risk AI systems used by credit institutions in connection with financial services (Art. 74(6)); Model Risk and AI Governance is the contact; GDPR matters remain with the HBDI | I4, D2 |

3.6 IT Management (CIO)

| Sub-domain | Interface point | Demarcation rule | Principles |
| :---- | :---- | :---- | :---- |
| Infrastructure and cloud management | Customer data in the EEA core banking infrastructure; remote technical support from India by Example Cloud Services Pvt Ltd (fictional) | IT owns the infrastructure and selects providers; remote access by this separate provider from India is a transfer (EDPB Guidelines 05/2021 criteria met): General Counsel determines G-TIA (`TIA-CLOUD-01`, standard contractual clauses under Art. 46), and the CIO as Processing Owner decides on the transfer tool and supplementary measures | I1, I4, D2, D3 |
| Software development (SDLC) | Privacy by design in Digital Banking products | Engineering owns the process; G-L and DPIA triage before production, and a completed DPIA where required | I2, D3 |
| Change management | Changes to core banking systems and PEP | IT owns change management; changes that alter purposes, data categories, recipients or risk are routed to the gates; the release is held until the gates are recorded | I2, D2, D3 |
| IT service management | Support tickets containing customer data | IT owns the ITSM platform; privacy requires minimisation of personal data in tickets and logs | I1, D3 |
| Software licence management | Licences, versions, cost — no personal data of customers | No intersection with privacy governance identified; the row is kept for completeness | — |

3.7 HR

| Sub-domain | Interface point | Demarcation rule | Principles |
| :---- | :---- | :---- | :---- |
| Personnel data | Employee and candidate data | HR owns the processing and the Staff Privacy Notice; Privacy Officers assess risks from workplace-monitoring systems and HR analytics; the works council's co-determination rights over technical monitoring systems are respected; the Group DPO advises | I1, D1, D4 |
| Training and awareness | Privacy training via the corporate LMS | HR delivers; the Privacy Operations Lead owns the content; the Chief Privacy Officer is accountable; the Group DPO is consulted and runs its own awareness activities | I2, D1, D3 |
| Disciplinary measures | Consequences of an employee's breach of privacy policies | HR owns the disciplinary process; the Chief Privacy Officer refers cases; the Group DPO may report monitoring findings but does not investigate disciplinary cases | I3, D1, D3 |

3.8 Procurement

| Sub-domain | Interface point | Demarcation rule | Principles |
| :---- | :---- | :---- | :---- |
| Vendor due diligence | Privacy assessment of the core banking platform provider, Example Cloud Services Pvt Ltd and Example AI Provider Inc. (both fictional) | Procurement owns the due-diligence process; the privacy module is accountable to the Privacy Operations Lead | I2, D1, D4 |
| Vendor register | Role, contract type and privacy-assessment result per vendor; EuroCredit Bureau recorded as an independent controller under a data-sharing agreement | Procurement owns the vendor register; privacy adds its fields and links them to the DORA Register of Information (Section 3.15) | I1, D1, D4 |

3.9 Client Relationship (customer engagement, CRM, marketing)

| Sub-domain | Interface point | Demarcation rule | Principles |
| :---- | :---- | :---- | :---- |
| Marketing consent management | Consent to e-mail and push marketing | The Head of Marketing owns design, collection and withdrawal; the Privacy Operations Lead keeps proof of consent in the consent management system (CMS), which IT Management operates separately from the CRM (Document 13); the Group DPO advises on design | I1, I4, D3 |
| Profiling for personalisation | Personalised offers in the app — pilot segment (100–9,999 customers), contact details and preferences from a single source (CRM), separate consent | The Head of Digital Banking determines the logic and owns G-DPIA: the recorded triage for this pilot found one WP248 rev.01 criterion (evaluation/profiling), so no DPIA is presumed; the Art. 35 test is recorded separately from the internal tier (Document 18, Example 4.1: Low). Any extension to transaction data, several sources or a large-scale population needs its own triage (highly personal financial data, matching or combining datasets, scale, national Art. 35(4) lists) and is not assumed to be DPIA-free. General Counsel confirms the consent basis; the Group DPO advises | I2, I3, D3 |
| Complaints and enquiries | Complaints about credit decisions or the processing of personal data | The contact centre owns the general complaints process; privacy complaints go to the privacy operations team; requests for human review of credit decisions go to Credit Decisions; complaints addressed to the Group DPO are handled by the Group DPO under confidentiality | I2, D2 |

3.10 Corporate Management (Strategy, Budget, Internal Audit)

| Sub-domain | Interface point | Demarcation rule | Principles |
| :---- | :---- | :---- | :---- |
| Strategic planning | New initiatives involving new types of customer-data processing | Corporate planning owns the process; G-L and DPIA triage run before budget approval | I2, D3 |
| Budgeting | Budget of the privacy programme, including the PEP rollout; resources of the Group DPO | The budget process allocates funds; the Chief Privacy Officer justifies the programme budget; the Group DPO has a separate budget line ensured by the Management Board (Art. 38(2)) | I2, D1, D2 |
| Internal audit | Independent assurance over the privacy programme | The Chief Audit Executive drafts the internal-audit charter and the risk-based audit plan; the Audit Committee of the Supervisory Board approves them; Group Internal Audit gives the annual opinion; the Group DPO's compliance audits are an input, not a substitute; privacy does not audit itself | I2, D1 |

3.11 Supervisory Board and Committees

| Sub-domain | Interface point | Demarcation rule | Principles |
| :---- | :---- | :---- | :---- |
| Risk Committee and Audit Committee of the Supervisory Board | Oversight of the privacy programme | Oversight and receipt of assurance; consent only for the three matters reserved under the Supervisory Board's rules: adoption and material amendment of the Charter; adoption and material amendment of the board-level privacy risk appetite (Privacy Risk Appetite Statement, Document 8, Section 3); removal of the Group DPO. Nothing else in the privacy area is reserved | I1, D1 |
| Privacy Risk Committee | Placement and mandate | A management-level committee established by the Management Board, chaired by the CRO; members: Chief Privacy Officer, CIO, CISO, General Counsel, Head of Compliance; the Group DPO attends as a non-voting adviser. It prepares decisions and decides only the classes delegated to it in writing | I1, D1 |
| Reporting | Quarterly programme reporting | The corporate secretariat sets the format; the Chief Privacy Officer reports to the Management Board and the Risk Committee; the Group DPO's own report goes to the Management Board and, where the Group DPO considers it necessary, to the Risk Committee | I2, D1, D3 |

3.12 Finance and Accounting (CFO)

| Sub-domain | Interface point | Demarcation rule | Principles |
| :---- | :---- | :---- | :---- |
| Shareholder register | Personal data of individual shareholders and dividend payments | Finance / Investor Relations owns the register and payments; retention and minimisation follow the retention schedule | I1, D1, D4 |
| Payments to individuals and accounting | Employee expense reimbursements; payments to sole-proprietor counterparties | Finance owns the systems; the retention schedule sets which records are kept for tax and accounting law | I1, D1, D3 |

3.13 Physical Security and Facilities

| Sub-domain | Interface point | Demarcation rule | Principles |
| :---- | :---- | :---- | :---- |
| Video surveillance (CCTV) | Recordings at branches and offices | Corporate Security owns the infrastructure; retention and access follow the retention schedule and the branch video-surveillance notice; the lawful basis is confirmed at G-L | I1, D1, D3 |
| Visitor logs | Visitor data at offices | Corporate Security / Facilities owns registration; the minimum data and retention period are set through the retention schedule | I1, D3 |

3.14 ICT Risk and Operational Resilience (DORA)

DORA applies to PanEuropean Bank AG as a whole, including its branches. The ICT Risk Control function (Head of ICT Risk Control, CRO area) is the independent ICT risk control function; the Management Board bears ultimate responsibility for ICT risk.

| Sub-domain | Interface point | Demarcation rule | Principles |
| :---- | :---- | :---- | :---- |
| ICT risk management framework | Protection of systems holding customer data | ICT Risk Control owns the framework; privacy requirements reach it through the CISO and the asset register | I1, I4, D1, D4 |
| Major ICT-related incident reporting | An incident that is also a personal data breach | ICT Risk Control classifies under Delegated Regulation (EU) 2024/1772 and reports to the ECB/BaFin under Delegated Regulation (EU) 2025/301; the GDPR track to the HBDI runs separately (Section 3.2); the joint classification call shares facts, not decisions or deadlines | I2, I4, D2 |
| Resilience testing | Threat-led penetration testing on production systems | ICT Risk Control owns the programme; test scenarios using customer data pass G-L and DPIA triage; pseudonymised data are used where the test objective allows | I2, D3 |
| Threat-intelligence sharing | Indicators shared with other financial entities | The CISO owns participation; General Counsel confirms the lawful basis for any personal data in shared indicators | I3, I4, D3 |
| NIS2 | Group non-financial subsidiaries | DORA applies to the bank as sector-specific law; whether a group service company falls under national NIS2 rules is assessed by that company and recorded in Document 7 | I4, D1 |

3.15 Outsourcing and ICT Third-Party Risk

| Sub-domain | Interface point | Demarcation rule | Principles |
| :---- | :---- | :---- | :---- |
| Outsourcing governance and register | Outsourced functions involving customer data (core banking platform; remote technical support) | The outsourcing function owns the outsourcing register and assessment under the EBA Guidelines on outsourcing arrangements and German banking law; the privacy due-diligence module is part of it | I1, I2, D1, D4 |
| DORA Register of Information | ICT third-party arrangements: the core banking platform provider, Example Cloud Services Pvt Ltd (remote technical support), Example AI Provider Inc. (both fictional), the external PEP technical support provider and the e-mail/push delivery service provider (both unnamed, illustrative). ICT Risk Control's illustrative classification: the core banking platform and the remote technical support are ICT services supporting critical or important functions (Art. 30(3) terms, tested exit strategy, ECB/BaFin informed under DORA Art. 28(3)); the others are not (Art. 30(2) terms); DORA requirements for tooling — Document 9, Section 4.2 | ICT Risk Control maintains the Register of Information; privacy fields (role, Art. 28 status, transfer mechanism, TIA reference) are linked to it by vendor identifier, not copied; EuroCredit Bureau is a data provider and independent controller, and whether it supports a critical or important function is a separate DORA test | I1, I4, D1, D4 |
| Contract terms | Data location, audit and access rights, exit | Legal aligns DORA, outsourcing and Art. 28 terms in one contract set; the Processing Owner (CIO for remote support; Head of Customer Service for the AI assistant) decides on the engagement | I2, I4, D3 |

## 4. The "No Duplicate Registers" Rule

Where PanEuropean already has a corporate register covering the same object of record, the privacy function uses it and adds privacy fields rather than creating a parallel register.

| Object of record | Priority source | Privacy-specific addition |
| :---- | :---- | :---- |
| Data Catalogue | PanEuropean's corporate data and systems catalogue (Section 3.3) | Sensitivity label (including health and biometric data) per system |
| Risk register | The corporate risk register ("Conduct & Privacy Risk") | Specific privacy risk (for example, re-identification risk in analytics data), residual tier and decider |
| Vendor register | Procurement's vendor register | Role (processor / independent controller / joint controller), contract type and privacy-assessment result |
| Outsourcing register; DORA Register of Information | The outsourcing function's register; ICT Risk Control's Register of Information | Link to privacy fields; transfer mechanism and TIA reference |
| Asset/system register | The IT/InfoSec asset register | Flag for processing of customer personal data and its extent |
| Model registry; AI system inventory | Model Risk and AI Governance | Personal-data flag, DPIA link, FRIA link (credit scoring) |

Statutory records kept independently and linked by identifier: the RoPA (Art. 30); the breach record of every personal data breach (Art. 33(5)); the DORA Register of Information and DORA incident records.

## 5. Conflict-Resolution Matrix

| Conflict type | Example | Arbitrator (decision per Document 5) | Escalation | Resolution timeframe |
| :---- | :---- | :---- | :---- | :---- |
| Privacy vs InfoSec | The CISO wants to keep anti-fraud system logs for 24 months; the retention schedule sets 12 months | Chief Privacy Officer and CISO jointly; Group DPO advice recorded | Privacy Risk Committee → Management Board | 10 business days |
| Privacy vs ERM | The CRO proposes raising the corporate fraud-risk appetite in a way that would require exceeding the privacy tier for anti-fraud scoring | Chief Privacy Officer and ERM; the privacy tiers prevail for rights-and-freedoms risk | Management Board (adopts both appetites; Supervisory Board consent where the board-level privacy risk appetite in Document 8, Section 3 changes — a reserved matter) | 15 business days |
| Privacy vs Data Governance | The classification scheme lacks a separate label for biometric data planned for app authentication | Chief Privacy Officer and CDO jointly | Privacy Risk Committee → Management Board | 10 business days |
| Privacy vs Procurement | A commercially advantageous cloud provider fails due diligence on the transfer criterion | General Counsel's G-TIA determination is binding — a failed G-TIA cannot be overridden; otherwise the CIO as Processing Owner decides on the due-diligence result | Privacy Risk Committee → Management Board | 10 business days |
| Privacy vs a business unit | Digital Banking wants to launch a new personalised-offers feature before DPIA triage is complete | The release is held until G-L and DPIA triage are recorded; scope disagreements between the Head of Digital Banking and the Chief Privacy Officer | Privacy Risk Committee → Management Board | Hold immediately; 5 business days |
| Privacy vs IT Management | IT wants to deploy a change to a core banking system without impact triage | The change is held until triage is recorded; CIO and Chief Privacy Officer | Privacy Risk Committee → Management Board | 10 business days |
| Privacy vs Model Risk and AI Governance | The scoring-model owner wants a broader set of transaction data than minimisation allows | Head of Credit Decisions and Chief Privacy Officer, with Model Risk and AI Governance; General Counsel confirms whether G-L is met | Privacy Risk Committee → Management Board | 10 business days |
| Privacy vs Client Relationship | Marketing wants profiling beyond the scope assessed | The extension is held until the assessment is updated; Head of Marketing and Chief Privacy Officer | Privacy Risk Committee → Management Board | 10 business days |
| Privacy vs ICT Risk Control (DORA) | Disagreement on whether a DORA incident record may contain full customer identifiers | Head of ICT Risk Control and Chief Privacy Officer jointly; prescribed reporting content prevails | Management Board | 5 business days, never delaying a statutory report |
| Privacy vs Corporate Management | The budget does not fund remediation of a breached risk limit in anti-fraud scoring | Chief Privacy Officer and CFO jointly | Management Board; Risk Committee of the Supervisory Board informed | 15 business days |

In all cases not resolved by the named arbitrators, the Management Board decides, on the recommendation of the Privacy Risk Committee and after the Group DPO's advice; where the decision departs from that advice, the reasons are recorded and the Group DPO may inform the Risk Committee of the Supervisory Board. The Supervisory Board is informed; its consent applies only to the matters reserved under its rules.

## 6. Relationship to Other Documents of the Model

This document builds on PanEuropean's Privacy Governance Charter and details the boundaries of its Sections 4 and 10; role allocation follows PanEuropean's RACI Matrix. It sets external boundaries for:

* the Privacy Risk Appetite Statement (Document 8) — alignment with the corporate risk appetite (Section 3.1)
* the Data Classification Policy (Document 10) — special categories (Section 3.3)
* the Data Breach Response Policy (Document 14) — the CISO, the GDPR track to the HBDI and the DORA track to the ECB/BaFin (Sections 3.2 and 3.14)
* the Vendor and Third-Party Privacy Risk Policy (Document 17) — Procurement, outsourcing and the Register of Information, applied to Example Cloud Services Pvt Ltd, Example AI Provider Inc. and EuroCredit Bureau (Sections 3.8 and 3.15)
* the DPIA Methodology (Document 19) — the credit-scoring DPIAs and the planned FRIA (Section 3.5)
* the Regulatory Applicability Matrix (Document 7) — DORA, the AI Act, NIS2 and outsourcing rules

The conflict-resolution matrix (Section 5) applies to all documents of PanEuropean's model and is not duplicated in them.

## 7. Review and Amendment

This document is reviewed under the continuous-improvement principle (Charter, Section 7) and the Policy Review Cycle (Document 29), and upon every change to PanEuropean's organisational structure that affects the functions in Section 3. Amendments are prepared by the Chief Privacy Officer, with the Group DPO's advice, and adopted by the Management Board; the Risk Committee of the Supervisory Board is informed.

Procedure for Adding a New Corporate Function to the Map

Should a new corporate function emerge at PanEuropean (for example, a dedicated ESG/Sustainability function, under discussion by the Management Board for 2027), the map is extended as follows:

* Step 1 — the Privacy Operations Lead applies I1–I4 and records whether an interface point exists
* Step 2 — where one exists, the Chief Privacy Officer applies D1–D5 to set the demarcation rule, with the Group DPO's advice
* Step 3 — the function is added as Section 3.16 onward; Section 1 is updated
* Step 4 — the Chief Privacy Officer assesses whether a new conflict type is needed in Section 5
* Step 5 — the change is recorded in the document history and adopted by the Management Board

The same procedure applies in reverse when a function is discontinued or merged.

## 8. Approval

Version 3.0 of this document was adopted by the Management Board of PanEuropean Bank AG on 20 October 2026, on the proposal of the Chief Privacy Officer and after the Group DPO's advice; the Risk Committee of the Supervisory Board was informed on 23 October 2026. Document owner: Chief Privacy Officer.

# Normative Basis and References

* Regulation (EU) 2016/679 (GDPR): Arts. 5(2), 22, 24, 26, 28, 30, 33–36, 37–39 (in particular 38(2)–(5) and 39(1)(b)), 48, 56.
* EDPB Guidelines 9/2022 on personal data breach notification under GDPR, version 2.0 (28 March 2023); EDPB Guidelines 07/2020 on the concepts of controller and processor; EDPB Guidelines 05/2021 on the interplay between Art. 3 and Chapter V, version 2.0 (§2.2 — criteria for a transfer); Article 29 Working Party, Guidelines on Data Protection Officers, WP243 rev.01 (§2.6 confidentiality; §3.5 conflict of interests).
* Regulation (EU) 2022/2554 (DORA): Arts. 5, 6 (including 6(4)), 17–19, 24–27, 28(3), 30, 45; Commission Delegated Regulation (EU) 2024/1772 (classification of ICT-related incidents); Commission Delegated Regulation (EU) 2025/301 (content and time limits of incident reports) and the related implementing technical standards.
* Directive (EU) 2022/2555 (NIS2), Art. 4 (sector-specific Union legal acts).
* Regulation (EU) 2024/1689 (AI Act), as amended by the AI Omnibus (in force 27 July 2026): Annex III point 5(b) and 5(c); Arts. 26, 27 (including 27(4)), 74(6) and 86; obligations for Annex III high-risk systems apply from 2 December 2027.
* EBA Guidelines on outsourcing arrangements (EBA/GL/2019/02); EBA Guidelines on loan origination and monitoring (EBA/GL/2020/06).
* IIA Global Internal Audit Standards 2024, Standards 6.2 and 9.4 (professional-practice basis).
* NIST AI Risk Management Framework 1.0 (January 2023) — voluntary reference for the template.
* Privacy Governance Charter (Document 2), Sections 4, 8, 10 and 11; Privacy RACI Matrix (Document 5); Privacy Risk Appetite Statement (Document 8); Privacy Risk Assessment Methodology (Document 18).

# International Adaptation

> **Guidance.** The interface model is jurisdiction-neutral; the box below names the counterpart regimes whose owners appear in Section 3 outside the EU. It does not claim compliance with any jurisdiction's law; applicability is recorded in Document 7.

* **United Kingdom (headline).** The ICO is the data protection regulator under UK GDPR and the DPA 2018, as amended by the Data (Use and Access) Act 2025; financial-sector operational-resilience and outsourcing rules are separate tracks with their own owners and regulators, mapped in Sections 3.14–3.15 instead of DORA.
* **Switzerland (headline).** The FDPIC is the data protection authority under the revFADP; breaches likely to result in a high risk are notified to the FDPIC as soon as possible. Financial-market supervision is a separate track, mapped in Sections 3.14–3.15.
* **Canada.** The privacy function's counterpart is the Privacy Officer under PIPEDA Principle 4.1 and the person in charge of the protection of personal information under Québec P-39.1 — accountability roles, not an EU DPO. Statutory records kept independently under Section 4 include the PIPEDA record of every breach of security safeguards (24 months) and the Québec confidentiality-incident register. For federally regulated financial institutions, prudential guidance on third-party risk and on technology and cyber risk is a separate track mapped in Sections 3.14–3.15.

# Document History (PGF)

| Release | Date | Summary |
| :---- | :---- | :---- |
| 1.0.0-rc.1 | 2026-10-26 | Canonical English Markdown; changes from internal ver.2: roles aligned with the Charter and the RACI role model (EPPO as owner; Executive Management adopts; Processing Owner decides within delegation; DPO advises, monitors, is the SA contact point and escalates); DPO vetoes, "final decisions", "mandatory approval" and authority to block removed and replaced by mandatory gates, holds and recorded advice; principle D2 rewritten as statutory and gate precedence; breach rows split into the GDPR track (controller decision on DPO advice to the competent/lead SA) and the DORA track (ICT risk function to the financial supervisor; Delegated Regulations 2024/1772 and 2025/301); new Sections 3.14 (ICT Risk and Operational Resilience, with NIS2 note) and 3.15 (Outsourcing and ICT Third-Party Risk, DORA Register of Information); Section 3.5 rebuilt as AI Governance and Model Risk with AI Act deployer duties and the FRIA (Annex III 5(b); application from 2 December 2027 under the AI Omnibus); "no duplicate registers" rule with statutory-records exception; Privacy Risk Committee recorded as management level; Governing Body committees as oversight; single final arbiter (Executive Management); internal-audit governance (Audit Committee approves charter and plan); customer-facing explanation owned by the Processing Owner; Art. 48 added; Three Lines mapping added; cross-references corrected (Section 3.16 onward; Privacy Risk Appetite Statement, Document 8); Part B example bank given a Model Risk and AI Governance function; Group DPO no longer reports to the CDO; fictional providers and PEP used; example dates shifted by −12 months; normative basis and international adaptation added. Integration pass: Part B DORA Register of Information row lists all five ICT arrangements with ICT Risk Control's illustrative classification (Document 17); CMS named for consent records; G4.2 cross-reference; privacy risk records mapped to the ERM record, operational-risk event type and ICT risk (Document 22) |
