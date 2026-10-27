---
title: "Privacy Automation and Tooling Strategy"
document_id: PGF-09
level: 1
release_version: 1.0.0-rc.1
status: release-candidate
authors: ["Alexey Neyman", "Val Khvatov"]
regulatory_reference_date: 2026-10-26
licence_proposed: "CC BY 4.0 (proposed; subject to rights-holder confirmation)"
source_provenance: "Derived from internal source set ver.2: Level1/9. Privacy_Automation_Tooling_Strategy_Template and Example_ENG.docx.md; sha256 1c3571a8380110da7eafe23b00a0d83261f19b7f5605110e18c096a5d12eb852"
---

# PGF-09 — Privacy Automation and Tooling Strategy

*Privacy Governance Framework (PGF) · Level 1 — Strategic Documents · Release 1.0.0-rc.1 · Regulatory reference date: 26 October 2026*

> **Status and use.** Part A is a reusable template. Part B is a worked example for a fictional organisation (PanEuropean Bank AG); all names, figures, dates and records in Part B are illustrative. Nothing in this document is legal advice or a statement about any real organisation, product or provider.

# **About This Document**

**Purpose.** Document 9 states which privacy calculations and processes must be automated, what any tooling used for them must demonstrate before its outputs are relied on, and how tooling capabilities are validated, re-certified, replaced and exited. It is the **single connection point** between the PGF and any tooling: every other PGF document refers to this document instead of describing tooling requirements itself.

**Scope.** The document is tool-neutral. It names no product, contains no product capability claims and makes no product a condition of applying any other PGF document. Automated outputs are evidence that supports human decisions; they never replace the legal compliance gate (G-L), the DPIA judgement required by GDPR Art. 35(7), the prior-consultation test (G-36), the transfer-equivalence test (G-TIA) or the controller's conclusion that information is anonymous.

**Relationships.** Document 18 (Privacy Risk Assessment Methodology) defines what is calculated; Document 8 (Privacy Risk Appetite Statement) sets the limits that are monitored; Document 5 (RACI Matrix) allocates the S9 "Operating the automation tooling" process; Document 11 (Data Retention and Disposal Policy) sets the retention of evidence packs; Document 17 (Vendor and Third-Party Privacy Risk Policy) assesses external tooling providers; Document 3 (Interface and Integration Model) links tooling to ICT risk, outsourcing and model risk; Document 2 (Privacy Governance Charter) relies only on capabilities validated and recorded under Section 8 of this document.

# **How to Use This Document**

Part A is a template. Text in ***[square brackets, bold italic]*** is a placeholder. Blocks marked **Guidance** are removed from the adopted version. Part B shows the template completed for the fictional PanEuropean Bank AG and its fictional internal platform, "the Bank's privacy engineering platform (PEP, illustrative)".

> **Guidance.** Mandatory automation and tool neutrality do not conflict. This document fixes **what** must be automated and **what evidence** tooling must produce; it never fixes **which** product does it. Any statement that a particular tool "meets" this document must be backed by the validation record of Section 8, not by a vendor statement, a specification or a certificate.

# **Table of Contents**

**About This Document**
**How to Use This Document**
**Part A — Template**
Glossary of Terms
1. Purpose of This Document
2. Principles for Building the Automation Strategy
3. Automation of the Model's Core Processes
4. Tooling Selection and Approval Criteria
5. The Tool-Neutral Governance Core Principle
6. Technology Implementation Package
7. Relationship to Other Documents of the Model
8. Review, Capability Validation and Re-certification
9. Approval
**Part B — Worked Example: PanEuropean Bank AG**
Glossary of Terms
1. Purpose of This Document
2. Principles for Building the Automation Strategy
3. Automation of the Model's Core Processes
4. Tooling Selection and Approval Criteria
5. The Tool-Neutral Governance Core Principle
6. Technology Implementation Package
7. Relationship to Other Documents of the Model
8. Review, Capability Validation and Re-certification
9. Approval
**Normative Basis and References**
**Document History (PGF)**

# **Part A — Template**

**Privacy Automation and Tooling Strategy of *[Organisation Legal Name]***

Effective date: ***[DD Month YYYY]***   ·   Version: ***[x.x]***   ·   Document owner: ***[Executive Privacy Programme Owner (EPPO)]***   ·   Adopted by: ***[Executive Management]***

***Version History***

| Version | Date | Changes |
| :---- | :---- | :---- |
| ***[1.0]*** | ***[DD.MM.YYYY]*** | ***[First version of the document]*** |
| ***[x.x]*** | ***[DD.MM.YYYY]*** | ***[Brief description of material changes]*** |

> **Guidance.** Record only material changes — in particular, a change to the classes of decisions subject to mandatory automation (Section 3.1), to the selection criteria (Section 4), to the validation and re-certification rules (Section 8), or a change of the primary tooling. A change of tooling does not require revising other PGF documents, provided the new tooling passes the validation of Section 8 against the criteria of Section 4.

## **Glossary of Terms**

*This table lists only the terms that this document itself defines; terms defined in another PGF document are not repeated here.*

| Term | Definition / Reference |
| :---- | :---- |
| Automation tooling | Any software, platform or service used to perform the classes of decisions in Section 3.1 or the targeted automation of Section 3.2, whether built in-house, open source or supplied by a third party. ***[Name of the organisation's tooling, if a separate definition is needed]*** |
| Technology Implementation Package (TIP) | The separately versioned set of technical specifications for the tooling in use (Section 6). It is outside the governance core and may change without amending this document, unless it affects Sections 3.1, 4 or 8. |
| Validation record | The record, kept under Section 8, of each tooling capability the organisation relies on: its status (specified / tested / deployed / planned / not verified), the evidence for that status, the version tested, known limitations and the date of the next re-check. Only capabilities recorded as tested and deployed may be relied on in a decision. |
| Conformance test suite | A documented, versioned and repeatable set of test cases — including negative cases — that checks whether the tooling produces the results this document and Document 18 require (Section 8.2). |
| Evidence pack | The versioned record of a calculation or transformation and of the decision taken on it (Document 18, Section 4.5). Integrity requirements — Section 4.1. |
| Fallback procedure | The predefined, conservative procedure used when the tooling is unavailable (Section 6). |
| Exit plan | The documented plan for replacing the tooling or its provider without loss of evidence, continuity or control (Section 6; for financial entities, DORA Art. 28(8)). |

## **1. Purpose of This Document**

This document establishes which privacy governance calculations and processes at ***[organisation name]*** must be performed by automated means, rather than manually or by unaided expert judgement, and what any tooling performing this automation must demonstrate. It does not name a product. The governance core — the Charter, the policies, the matrices and the methodology — remains valid whichever tooling is used, provided the tooling passes the validation of Section 8 against the criteria of Section 4.

The document covers the five core processes of the Privacy Governance Process Map (Document 24): Risk Calculation Project Development (C1, including the calculation component of a DPIA under Document 19, which applies Document 18), Request and Transformation (C2), Data Subject Rights (C3), Cross-Border Transfer (C4) and Consent Management (C5). The rules of those processes — what counts as valid consent, which rights apply, the conditions for a transfer — remain in their own documents; this document governs only their automation.

Automated results gain credibility for management, auditors and supervisory authorities only through the controls in this document: defined classes of automated decisions (Section 3.1), selection criteria (Section 4), validated capabilities (Section 8) and the integrity of evidence (Section 4.1). Even then, an automated output is **evidence for a human decision, not the decision**. A tool score does not establish that information is anonymous, that processing is lawful or that a residual risk is acceptable; the responsible roles of Documents 5 and 8 decide, and they remain alert to automation bias.

Automation of the governing processes (G1–G9) and of most supporting processes (S1–S8) is outside the scope of this document, except for the operation of the automation tooling itself (S9). Those processes rely on existing corporate systems (document management, service desk, learning management and similar) under the organisation's general IT strategy. The reliability of automated calculation for C1 and C4 depends on current classification data (S1, Document 10) and inventory data (S3, Document 23); their quality is an external precondition, not an outcome guaranteed by this document.

This document does not govern:

* vendor and third-party risk assessment when engaging external tooling — Document 17 (see also Section 4);
* data breach and incident response — Document 14;
* staff training and awareness — Document 30.

## **2. Principles for Building the Automation Strategy**

> **Guidance.** Without explicit principles, mandatory automation turns either into a blanket requirement for every process (unrealistic, and it undermines trust in the document) or into a non-binding recommendation that business units ignore when resources are short.

* ***[Targeted-mandate principle — automation is mandatory only for the classes of decisions in Section 3.1, where manual calculation creates an unacceptable risk of error or of inconsistency between cases.]***

* ***[Tool-neutral governance core principle — no PGF document makes a specific product a condition of its applicability. Product names may appear only in the Technology Implementation Package (Section 6) and, where an organisation chooses, in its own worked examples; no rule, decision or delegation may depend on them (test — Section 5).]***

* ***[Validated-capabilities-only principle — a capability is relied on in a decision only when the validation record (Section 8.1) shows it as tested and deployed in the version in use. A specification, a roadmap, a vendor statement or a certificate is not evidence that a capability is implemented.]***

* ***[Human-decision principle — automated outputs inform the decisions of the roles named in Documents 5 and 8; they never replace G-L, the DPIA judgement (Art. 35(7)), G-36, G-TIA or the controller's anonymity conclusion (Document 18, Section 3.3.0).]***

* ***[Lawful-processing principle — applying a privacy-enhancing technique (PET), training a synthetic-data generator or running a calculation on personal data is itself processing. It needs a lawful basis (Art. 6) and, where the purpose differs from the original one, a compatibility assessment (Art. 6(4)); DPIA triage applies. G-L runs before the tooling processes the data.]***

* ***[Documented-limitation principle — where the tooling lacks a validated implementation of a metric or test required by Document 18, the gap in the tool may be closed only by an external or manual calculation or test that is itself validated and actually produces the required result, with its uncertainty and evidence, so that every gate of Document 18 can be applied to it. A qualitative expert opinion cannot replace a missing mandatory result: it may inform the decision-maker, but it cannot support a PASS, an anonymity conclusion or a release, and the module outcome remains INCOMPLETE (Document 18, G-M5) and the release blocked until the required result exists. The limitation is recorded in the validation record and the evidence pack, and the decision-maker is told what is not covered. A recalculation made after the tooling is restored does not retrospectively legalise a release or decision that lacked mandatory evidence when it was made. The mandate for automation as the target state remains.]***

* ***[Separation of governance and technical implementation — this document fixes what the tooling must provide and how that is evidenced; how a specific tool implements it is fixed in the Technology Implementation Package (Section 6).]***

* ***[Completeness of core-process coverage — the strategy considers all five core processes (Document 24); for those not subject to mandatory automation, Section 3.2 sets a targeted automation trajectory.]***

* ***[Process-scope boundary principle — mandatory and targeted automation under this document cover only the core processes and S9; the quality of classification (S1) and inventory (S3) data is an external precondition.]***

## **3. Automation of the Model's Core Processes**

***3.1 Mandatory Automation***

> **Guidance.** For each class, explain why manual calculation creates an unacceptable risk — do not stop at stating that it "must be automated". The list is exhaustive for the purposes of mandatory automation.

| Class of Decisions | Why Automation Is Mandatory | Related PGF Document |
| :---- | :---- | :---- |
| ***[Privacy risk calculation]*** | ***[Applying the scenario-based likelihood model, the severity factors and the residual-risk mapping by hand, case by case, does not scale and creates a risk of inconsistent results between analysts and between countries. For de-identified, synthetic, aggregate or federated artefacts, the PET Assessment Module requires repeatable metric computation, confidence intervals and failure gates that cannot be reliably reproduced manually.]*** | ***[Document 18, Sections 3 and 4; Document 8, Section 4]*** |
| ***[Evidence-pack compilation]*** | ***[Manual assembly of the evidence for each decision is prone to omission and to undetected alteration; integrity requirements (Section 4.1) need technical support.]*** | ***[Document 18, Section 4.5; Document 5, Section 5.2]*** |
| ***[Monitoring of limits, expiries and re-assessment triggers]*** | ***[The cumulative privacy-loss ledger and any operational cap (Document 8, Section 3; Document 18, Section 3.3.6), the expiry of conditional acceptances (Document 8, Section 5) and the periodic re-assessment of anonymity conclusions (Document 18, Section 3.3.0) must be tracked continuously across many projects; manual tracking misses overruns and lapsed conditions.]*** | ***[Document 8, Sections 3 and 5; Document 18, Sections 3.3.0 and 3.3.6]*** |
| ***[Application of PET transformations]*** | ***[Manual application of pseudonymisation, de-identification or synthesis is prone to configuration error and cannot be reproduced for audit.]*** | ***[Document 18, Section 3.3; Document 5, Section 5.2]*** |

The list covers core processes C1 and C2 of Document 24. The remaining three core processes — Consent Management (C5), Data Subject Rights (C3) and Cross-Border Transfer (C4) — are not subject to mandatory automation but are not left outside the strategy: Section 3.2 defines their targeted automation.

***3.2 Targeted Automation of the Other Core Processes***

For C5, C3 and C4, automation is a target state, not a mandate. The organisation sets the order of priority using: (i) the volume of manual effort and operational risk removed; (ii) regulatory sensitivity, including statutory deadlines; (iii) the readiness of the systems concerned to integrate (the architecture map in Section 6). ***[The resulting priority and timeline]*** are fixed by the organisation. The criteria of Section 4 apply when a specific system is assessed for a process already selected; they do not set the priority. The rules of the processes remain in Documents 13, 15, 12 and 20.

| Core process | Rationale for Targeted Automation | Current Status / Related Document |
| :---- | :---- | :---- |
| ***[Consent Management (C5)]*** | ***[E.g. fewer errors in manual consent tracking; consent status available as a pre-filter before a PET transformation. Consent is checked in G-L as a lawful basis; it is not a risk factor in Document 18.]*** | ***[Target timeline / status; process rules — Document 13]*** |
| ***[Data Subject Rights (C3)]*** | ***[E.g. shorter response times; automatic blocking of active calculation projects when processing is restricted (Art. 18); propagation of erasure and withdrawal to derived personal data along the data lineage (Document 11)]*** | ***[Target timeline / status; process rules — Document 15]*** |
| ***[Cross-Border Transfer (C4)]*** | ***[E.g. less effort in maintaining transfer records; the severity of harm from disclosure (Document 18) supplied as an input where Document 20 requests it. The laws-and-practices assessment and the G-TIA determination remain legal work under Document 20 and are not automated scores.]*** | ***[Target timeline / status; process rules — Documents 12 and 20]*** |

## **4. Tooling Selection and Approval Criteria**

> **Guidance.** Criteria are requirements (what the tooling must provide and evidence), not a list of products. The approval of a specific tool against these criteria is a separate decision, recorded in the validation record (Section 8.1). Where the tooling is supplied by a third party, Document 17 applies in addition; these criteria precede that assessment and do not replace it.

| Criterion | Requirement |
| :---- | :---- |
| ***[Coverage of the methodology]*** | ***[The tooling implements the calculations Document 18 requires for the archetypes in use, including the PET Assessment Module's per-metric results, failure gates (G-M1 to G-M5), confidence intervals and the lifetime privacy-loss ledger. Any element not implemented is recorded as a limitation (Section 8.1).]*** |
| ***[Reproducibility]*** | ***[Every result can be traced to the tooling version, configuration, input data version and run parameters, and can be re-run with the same configuration. For randomised mechanisms (for example noise addition or synthetic-data generation), reproducibility means re-running from the recorded configuration with results within a stated statistical tolerance. Where random seeds are retained, they are protected at least as strictly as the source data, because a seed can allow the added noise to be reconstructed.]*** |
| ***[Evidence-pack integrity]*** | ***[The tooling produces evidence packs that meet Section 4.1, in a format readable without the tooling.]*** |
| ***[Security]*** | ***[Encryption, access control by role and need to know, logging of access and configuration changes, segregation of the tooling environment from production identifiers and from general analytics environments, and protection of generator parameters and intermediate outputs.]*** |
| ***[Data location and transfers]*** | ***[Hosting, support and processing locations comply with the Regulatory Applicability Matrix (Document 7) and the Cross-Border Data Transfer Policy (Document 12). Remote access by a separate provider from a third country is a transfer under Document 12.]*** |
| ***[Integration with existing systems]*** | ***[Data are exchanged with source systems without manual extracts; classification labels (Document 10) and lineage are carried with the data.]*** |
| ***[Minimisation]*** | ***[The tooling does not require more data than the calculation or transformation needs; source data are used only inside the controlled environment.]*** |
| ***[Provider viability, continuity and exit]*** | ***[The provider (in-house team or third party) has the financial and organisational capacity for long-term support, assessed on evidence (Document 17), not inferred from a support agreement. A tested fallback procedure and an exit plan exist (Section 6): evidence packs, configurations, ledgers and validation records can be exported in documented formats, and the organisation can switch tooling without losing evidence.]*** |
| ***[ICT third-party requirements (financial entities subject to DORA)]*** | ***[As set out in Section 4.2.]*** |
| ***[AI components]*** | ***[Where the tooling contains machine-learning components (for example PII detection or synthetic-data generators), their classification under the AI Act and their validation are recorded by the AI governance function (Document 3, Section 3.5).]*** |
| ***[Transparency of limitations]*** | ***[The provider discloses known limitations, untested attack classes and implementation hazards; the organisation records them in the validation record.]*** |
| ***[Testability]*** | ***[The tooling can run the conformance test suite of Section 8.2, including negative cases, and exposes the results needed to check them.]*** |

The criteria "Data location and transfers", "Integration", "Minimisation", "Provider viability, continuity and exit", "Security" and the DORA requirements apply to any tooling under Section 3.1 or 3.2. "Coverage of the methodology", "Reproducibility", "Evidence-pack integrity" and "Testability" are specific to tooling that performs the classes of decisions in Section 3.1.

***4.1 Evidence-Pack Integrity Requirements***

* ***[Content and provenance. Each evidence pack records the policy, configuration, dataset and run versions, the tooling version, the persons or service accounts involved, timestamps, every metric result with its threshold and confidence interval, failed or skipped tests, limitations, the G-L reference, the decision, the single decider and the DPO advice where applicable (Document 18, Section 4.5).]***
* ***[Sealing. Each version of an evidence pack is sealed: a cryptographic hash is computed over a manifest that lists every component and its own hash, and, where required, the manifest is signed with a key whose life cycle (generation, storage, rotation, revocation) is managed. A hash or signature proves that the bytes have not changed since sealing; it does not prove that the content is true, complete or lawful.]***
* ***[Superseding, not editing. A sealed version is never edited. A correction or update creates a new version that references the version it supersedes and states why.]***
* ***[Minimisation. Evidence packs contain metrics, configurations and decisions, not source records. Where personal data must be included (for example the names of deciders, or sample records needed to explain a failed test), they are kept in a separately sealed component so that they can be removed without breaking the integrity of the rest.]***
* ***[Retention by the applicable rule, including deletion. Evidence packs and their components are retained for the period that the applicable rule in the Data Retention and Disposal Policy (Document 11) sets — not automatically for the longest period found anywhere — and then deleted or redacted. Immutable or write-once storage does not override deletion, redaction or restriction duties; the storage design must allow them (for example by deleting or crypto-shredding the separately sealed personal-data component).]***
* ***[Minimal record after purge. After a pack or a component is deleted, a minimal record (identifier, dates, hash of the deleted component, reason for deletion) is kept only where this is lawful and necessary — for example to demonstrate the disposal — and for its own defined retention period.]***
* ***[Access. Access to evidence packs follows need to know; regulators and auditors receive copies or extracts on request, without direct access to the tooling.]***

***4.2 ICT Third-Party Requirements for Financial Entities (DORA)***

For a financial entity subject to Regulation (EU) 2022/2554 (DORA), external tooling and its support are ICT services provided by ICT third-party service providers:

* ***[the arrangement is entered in the register of information (DORA Art. 28(3)), maintained by the ICT risk or outsourcing function; privacy fields are linked to it by vendor identifier, not copied (Document 3, Section 3.15);]***
* ***[before the contract is concluded, the entity assesses whether the service supports a critical or important function, identifies and assesses the risks, including ICT concentration risk (Arts. 28(4) and 29), and performs due diligence;]***
* ***[the contract contains the key contractual provisions of Art. 30, including data location, access, audit, termination and exit assistance, and the additional provisions of Art. 30(3) where the service supports a critical or important function;]***
* ***[an exit strategy exists for ICT services supporting critical or important functions (Art. 28(8)) and is tested; the exit plan of Section 6 is aligned with it;]***
* ***[the classification of the arrangement (supporting a critical or important function, or not) is made by the ICT risk function and recorded under Document 17. "Critical ICT third-party service provider" is a designation made by the European Supervisory Authorities under Art. 31; it is not a status the entity assigns.]***

Where the tooling uses data processing services within the meaning of the Data Act, the switching rules of its Chapter VI are taken into account in the exit plan.

***4.3 Checklist for Differential Privacy Claims***

Any statement — by a provider, in a specification or in an evidence pack — that an output is protected by differential privacy is relied on only if it states the following (NIST SP 800-226; Document 18, Section 3.3.5):

| Element | What must be stated and checked |
| :---- | :---- |
| ***[Privacy unit]*** | ***[What is protected — one record, or all records of one person — and the per-person contribution bound where a person can contribute several records]*** |
| ***[Adjacency relation]*** | ***[Add/remove or replace one privacy unit]*** |
| ***[Mechanism and accountant]*** | ***[The mechanism and its parameters (for example noise multiplier, clipping norm, sampling rate, number of steps) and the privacy accountant used to compute ε at the stated δ]*** |
| ***[ε and δ]*** | ***[ε for the stated δ. δ is described neutrally as the additive term in the definition of approximate differential privacy.]*** |
| ***[Composition across releases]*** | ***[Every run on the same source population is entered in the lifetime ledger (Document 18, Section 3.3.6), including model-selection runs, previews and failed or cancelled runs whose outputs were observable. "Commit-only" accounting is not accepted without an analysis showing that no other output was observable. Post-processing of a released output does not consume additional budget.]*** |
| ***[Trust model and output access]*** | ***[Central or local model; who can see the final output, checkpoints, logs and previews; which outputs are not covered by the mechanism]*** |
| ***[Implementation audit]*** | ***[How the implementation was verified — library and version, code review, tests; known hazards (floating-point effects, sampling assumptions, side channels, bugs) and how they are addressed]*** |
| ***[Limits of empirical tests]*** | ***[Empirical attacks give lower bounds on leakage for the attacks tried; they neither prove nor disprove the formal guarantee]*** |

A claim missing any element is recorded as "not verified" in the validation record and makes the PET Assessment Module INCOMPLETE or FAILED where the claim is relied on (Document 18, gate G-M4 or G-M5).

***4.4 Synthetic Data and Other PET Claims***

* ***[Synthetic data are not safe by default. A synthetic dataset is a derived artefact that can disclose information about people in the source data; generators can memorise records, and published audits have found implementations whose empirical leakage exceeded the claimed guarantee. Before any synthetic dataset crosses a boundary of access, the tooling runs the empirical attack tests of Document 18, Section 3.3.2 (membership inference, closeness to training records, linkability and attribute inference against a control set), and the failure gates apply. Untested attack classes (for example model inversion on the generator's parameters) are recorded as limitations, with the compensating access restrictions.]***
* ***[Generation is a method, not a legal status. Whether a synthetic dataset is anonymous information is a controller conclusion under Recital 26 (Document 18, Section 3.3.0); until it is made, the dataset is treated as personal data (Documents 10 and 11).]***
* ***[Pseudonymisation is not anonymisation. Pseudonymised data remain personal data for whoever can attribute them with means reasonably likely to be used (Art. 4(5); EDPB Guidelines 01/2025). A recipient's realistic means are part of the contextual analysis (CJEU C-413/23 P *EDPS v SRB*), but that judgment does not decide generally that data stop being personal, or that Chapter V stops applying, whenever a recipient lacks the key; the controller's perspective, any processor's role and the full flow are assessed separately (Documents 12 and 20).]***
* ***[Different guarantees are not mixed. k-anonymity, l-diversity and t-closeness are properties of released records and do not protect against all inference attacks (Article 29 Working Party Opinion 05/2014, WP216); differential privacy is a property of a randomised mechanism. A tool configuration that states both describes them separately and states which one a decision relies on.]***
* ***[Federated learning, secure computation, trusted execution environments and homomorphic encryption are processing architectures or security measures; they do not by themselves change the legal status of data or remove a transfer (Document 12).]***

## **5. The Tool-Neutral Governance Core Principle**

No PGF document — the Charter (Document 2), the Interface and Integration Model (Document 3), the Organisational Design Strategy (Document 4), the RACI Matrix (Document 5), the Privacy Role Competency Framework (Document 6), the Regulatory Applicability Matrix (Document 7), the Privacy Risk Appetite Statement (Document 8), the policies (Documents 10–17) or the methodologies (Documents 18–20) — may make specific tooling a condition of its applicability. Changing the primary tooling ***[does not require]*** revising those documents, provided the new tooling passes the validation of Section 8 against the criteria of Section 4.

> **Guidance.** Neutrality test, applied at every review: (1) remove every product name from the document, including its worked examples; (2) confirm that no rule, threshold, delegation, decision, qualification or reporting line changes; (3) confirm that no example decision (for example a risk acceptance, a calibration or an anonymity conclusion) is justified by a product's capability rather than by recorded evidence; (4) confirm that no role requires a credential issued by a tool provider. A dependency found by the test is a design flaw in the document concerned and is corrected there.

***[A provider or community may publish, separately, an implementation profile that maps a specific product to the requirements of this document. Such a profile is never a PGF dependency, does not certify conformity with the PGF and is not referenced as a condition in any PGF document. Its capability statements are relied on only after validation under Section 8.]***

## **6. Technology Implementation Package**

> **Guidance.** The Technology Implementation Package (TIP) gives engineering teams the technical specification of the tooling in use, without cluttering governance documents meant for management, auditors and supervisory authorities.

The technical specifications of the tooling in use are kept outside the governance core, as a separately versioned TIP, comprising at least:

* ***[The PET Standard — the techniques used, their parameters and the conditions of use by data class (Document 10), with the DP statements of Section 4.3 and the attack tests of Document 18, Section 3.3]***
* ***[The evidence-pack specification — format, content, sealing and versioning (Section 4.1), and the readable export format]***
* ***[The control-to-artefact matrix — mapping each criterion of Section 4 to the technical artefact and the conformance test that evidences it]***
* ***[The integration runbook — how the tooling is connected to source systems, the data catalogue and the lineage service]***
* ***[The conformance test suite (Section 8.2) and its results]***
* ***[The continuity (fallback) procedure — for the classes of decisions in Section 3.1, a temporary switch to a predefined, conservative manual procedure that never approves a release or a transformation without the required calculation; logging of every decision taken under the fallback procedure; retrospective recalculation once the tooling is restored (which checks decisions taken under the fallback procedure but does not legalise a release that lacked mandatory evidence when it was made); a maximum duration and an escalation path if it is exceeded]***
* ***[The exit plan — how evidence packs, configurations, ledgers, lineage and validation records are exported in documented formats; how an alternative tool or provider is brought in; how continuity is preserved during the switch; aligned with the DORA exit strategy where applicable (Section 4.2)]***

The owner of the TIP is ***[the Privacy Operations Lead, with Privacy Engineer(s) and IT Management]***. Its review cadence ***[is independent of the review of this document and may be more frequent — for example at every version update of the tooling]***. A change to the TIP is not an amendment to this document unless it affects Section 3.1, Section 4 or Section 8.

The architecture coverage map below positions the tooling among the organisation's systems and states explicitly what it does not cover.

| System / scope point | Position relative to the automation tooling | Coverage status |
| :---- | :---- | :---- |
| ***[Source systems for personal data]*** (core banking, CRM, data warehouse and similar) | Feed data into the tooling for risk calculation and PET application, after G-L | In scope |
| ***[Automation tooling]*** | Risk calculation, PET application, evidence-pack compilation, ledger and expiry monitoring — core processes C1 and C2 (Document 24) | In scope |
| ***[Record of Processing Activities (RoPA) / Privacy Risk Register]*** | Receive references to calculations and decisions | In scope (output) |
| ***[Supervisory authority / external auditor]*** | Receives evidence packs or extracts on request | Recipient, not part of the tooling |
| ***[Consent management system]*** (C5) — where one exists | Not connected by default; integration where consent status is a pre-filter for a transformation | Targeted automation (Section 3.2) |
| ***[Data subject rights system]*** (C3) — where one exists | Not connected by default; integration where a restriction must block an active calculation or an erasure must propagate to derived data | Targeted automation (Section 3.2) |
| ***[Transfer records and TIA]*** (C4) — where a tool exists | May receive severity inputs that Document 20 requests; the legal assessment is not automated | Targeted automation (Section 3.2) |
| ***[Vendor and third-party risk assessment]*** | Assesses the tooling provider itself | Out of scope of this map — Document 17 |
| ***[Incident and breach response]*** | Not connected to the tooling | Out of scope — Document 14 |
| ***[Training and awareness]*** | Not connected to the tooling | Out of scope — Document 30 |

## **7. Relationship to Other Documents of the Model**

* ***[Is the single connection point between the PGF and tooling; other documents refer to this document instead of describing tooling requirements.]***
* ***[The technology budget (licences, infrastructure, support) is adopted separately from the privacy function's budget (Organisational Design Strategy, Document 4, Section 8).]***
* ***[The classes of decisions in Section 3.1 implement the methodology of Document 18 and the limits of Document 8; they are used in the activities of the RACI Matrix (Document 5, Sections 5.1 and 5.2); S9 (operating the tooling) is allocated in Document 5, Section 6.]***
* ***[The targeted automation of Section 3.2 is aligned with Documents 13, 15, 12 and 20, which set the rules of those processes.]***
* ***[The data-location criterion (Section 4) is aligned with Document 7 and Document 12.]***
* ***[External tooling is also assessed under Document 17, following the insourcing/outsourcing principle of Document 4, Section 3; the ICT third-party interface is in Document 3, Section 3.15.]***
* ***[Evidence packs are retained and disposed of under Document 11.]***
* ***[The Charter (Document 2) relies only on capabilities recorded as tested and deployed in the validation record (Section 8.1); the Privacy Role Competency Framework (Document 6) requires an internal tool-proficiency assessment, never a provider-issued certificate.]***

When the tooling changes or its version is materially updated, dependent documents are updated in one of two modes: (i) joint mode — the change is agreed by the owners of both documents because the content is technically specific to the tooling; (ii) unilateral mode with notification — the owner of the dependent document updates it and notifies the owner of this document.

| Document | Maintenance mode | What changes when the tooling changes |
| :---- | :---- | :---- |
| Document 9 (this document) | Joint | The TIP (Section 6) and the validation record (Section 8.1); Section 4 is revisited only if the new tooling reveals a gap in the criteria |
| Document 18 (Privacy Risk Assessment Methodology) | Joint | Which metrics and tests of the PET Assessment Module are available as validated implementations, and which are recorded as limitations; the methodology itself does not change |
| Document 19 (DPIA Methodology and Template) | Unilateral, with notification | References to the tooling used to record DPIAs and run calculations |
| Document 22 (Privacy Risk Register) | Unilateral, with notification | Versioning of calculation projects and register entries |

## **8. Review, Capability Validation and Re-certification**

***8.1 Validation Record***

***[The Privacy Operations Lead keeps a validation record for the tooling in use. For each capability that a PGF process relies on, it states: the capability; its status — specified, tested, deployed, planned, or not verified (status unknown is recorded as "not verified"); the evidence (conformance test run, independent validation report, evidence-pack reference); the tooling version; known limitations; and the date of the next re-check. Only capabilities that are both tested and deployed in the version in use may be relied on in a decision. A provider's statement, a specification or a certificate changes a status only when supported by the organisation's own test evidence.]***

***8.2 Conformance Test Suite***

***[Re-certification is based on a documented, versioned and repeatable conformance test suite, owned by the Privacy Operations Lead and executed by Privacy Engineer(s). It covers at least:]***

* ***[positive cases with known expected results for each metric, gate and mapping used (Document 18, Sections 3.2–3.4 and 4.4), including boundary values at exclusive thresholds and interval-based gate decisions;]***
* ***[negative cases: a G-L failure cannot be overridden by any score or signature; a missing or invalid metric yields INCOMPLETE, never a pass; a failed run whose output was observable is charged to the privacy-loss ledger; concurrent runs cannot jointly exceed the ledger or a cap; a release that would exceed the lifetime ledger fails; an evidence pack cannot be edited after sealing; a superseding version references its predecessor;]***
* ***[reproducibility: re-runs from recorded configurations give results within the stated tolerance;]***
* ***[export: evidence packs, ledgers and configurations can be exported and read without the tooling (exit plan).]***

***[The suite, its version and every run's results are kept in the TIP; a failed test is recorded in the validation record with the affected capability set to "not verified" until remediated.]***

***8.3 Independent Validation of Metric and Model Implementations***

***[Because tooling outputs feed risk-acceptance decisions, the implementation of the metrics, attack tests, accountants and any machine-learning components is validated independently of the persons who configure and operate the tooling — by [the model-risk or AI governance function, internal audit, or a qualified external party]. Validation covers conceptual soundness against Document 18, implementation correctness, data and parameter choices, and known limitations. Findings are recorded in the validation record. Certifications of the provider's information-security or privacy management (for example ISO/IEC 27001 or ISO/IEC 27701) are inputs to Document 17 and to Section 4; they do not replace the conformance test suite or this validation.]***

***8.4 Re-certification***

***[At least annually, and without delay upon a trigger, [the Privacy Operations Lead] confirms, on the basis of a conformance test suite run and the latest independent validation, that the tooling in use continues to meet Section 4. Approval at initial selection is not indefinite. Triggers include: a major version change; a change of provider or of control over the provider; a change of hosting or support location; a lapse or withdrawal of a certification that the organisation's selection relied on; a published attack or implementation flaw relevant to a technique in use; and a significant incident. The outcome is recorded whether or not the decision on the tooling changes. Where the outcome is negative, the responsible roles submit a remediation plan to the owner of this document within [time frame], the affected capabilities are set to "not verified" and the fallback procedure applies to them; if conformity is not achieved in time, the matter is escalated to [Executive Management] for a decision on alternative tooling under the exit plan.]***

***8.5 Review of This Document***

***[This document is reviewed [at least annually] under [the Policy Review Cycle, Document 29], and upon a change to the classes of decisions in Section 3.1, the criteria of Section 4, the core processes of Section 3.2 or the systems that automate them. The annual review also reconciles the priority and status of the targeted automation and assesses effectiveness against indicators such as: the share of decisions for which the validated automated calculation was used; the time to compile an evidence pack; the frequency and cumulative duration of fallback periods; the number of open validation findings. Changing the tooling does not by itself require revising this document if the new tooling passes Section 8 against Section 4. Amendments are adopted by [Executive Management] on the proposal of [the EPPO], after consulting [the Privacy Risk Committee] and the DPO.]***

## **9. Approval**

This document was adopted by ***[Executive Management]*** on ***[date]***. Document owner: ***[EPPO]***.

# **Part B — Worked Example: PanEuropean Bank AG**

**PanEuropean Bank AG — Privacy Automation and Tooling Strategy**

Effective date: 20 October 2026   ·   Version: 2.0   ·   Document owner: Chief Privacy Officer (EPPO)   ·   Adopted by: Management Board, 20 October 2026

*A fictional legal entity, provided solely for illustrative purposes.*

***Fictional Document History (illustrative)***

| Version | Date | Changes |
| :---- | :---- | :---- |
| 1.0 | 1 March 2026 | First version, developed alongside the Privacy Risk Appetite Statement. Owner at the time: Group DPO |
| 2.0 | 20 October 2026 | Re-baselined to the new role model on the creation of the Chief Privacy Officer (EPPO) position: Chief Privacy Officer as owner; adoption by the Management Board; validation record, conformance test suite, independent validation and exit plan added; evidence-pack integrity and DORA ICT third-party requirements added; capability statements limited to validated capabilities |

## **Glossary of Terms**

*The Part A glossary applies; the entries below add PanEuropean specifics.*

| Term | Definition / Reference |
| :---- | :---- |
| PEP | The Bank's privacy engineering platform (PEP, illustrative) — a fictional internal platform on which PanEuropean runs the calculations of Document 18, applies PET techniques and compiles evidence packs. Technical support for PEP is provided by an external provider that is not named in this example. PEP is used only as far as its capabilities are recorded as tested and deployed in the validation record (Section 8.1); no PanEuropean rule, decision or delegation depends on PEP. |

## **1. Purpose of This Document**

This document establishes which privacy calculations and processes at PanEuropean Bank AG are automated, and what any tooling must demonstrate before its outputs are used. PanEuropean currently uses PEP for core processes C1 and C2 (Section 3.1), including the calculation part of its DPIAs (Document 19). Its governance core — the Charter, the RACI Matrix, the Privacy Role Competency Framework, the Privacy Risk Appetite Statement and the methodology — does not depend on PEP and would remain valid if PEP were replaced by other tooling that passes Section 8. PEP outputs are evidence for the decisions of the roles named in Documents 5 and 8; they never replace Legal & Compliance's G-L record, the Processing Owner's DPIA, the G-36 conclusion, the G-TIA determination or an anonymity conclusion.

## **2. Principles for Building the Automation Strategy**

* Targeted mandate — four classes of decisions are subject to mandatory automation (Section 3.1); for example, intake of customer enquiries at the contact centre is not among them and may remain partly manual.

* Tool-neutral governance core — PanEuropean's Charter, RACI Matrix, Privacy Risk Appetite Statement and Privacy Role Competency Framework do not make PEP a condition of applicability; the platform appears in examples and in this document only. Privacy Engineers' proficiency in PEP is confirmed by an internal assessment (Document 6), not by a provider certificate.

* Validated capabilities only — the Charter and the methodology rely only on PEP capabilities recorded as tested and deployed (Section 8.1). Capabilities that are planned or not verified are listed as such.

* Human decision — PEP results feed the evidence pack; the decision is taken by the single decider under Document 8, Section 5.

* Lawful processing — every PEP run on customer data is covered by a G-L record (lawful basis, compatibility of purpose) and by DPIA triage; for example, training the synthetic-data generator for credit-scoring calibration is covered by DPIA-CS-TRAIN-01 (Document 19).

* Documented limitation — where PEP has no validated test for an attack class required by Document 18, the limitation is recorded and compensating controls are applied: model inversion on generator parameters (Document 18, Section 3.3.2) and gradient reconstruction in federated learning (Document 18, Section 3.3.3) are not tested; generator parameters and model updates stay in restricted environments.

* Separation of governance and technical implementation — technical details of PEP (interfaces, data formats, parameters) are in the TIP (Section 6), not here.

* Completeness of core-process coverage — all five core processes are considered; C5, C3 and C4 have a targeted trajectory (Section 3.2).

* Process-scope boundary — governing and most supporting processes run on existing corporate systems; the reliability of PEP calculations depends on the classification (S1) and inventory (S3) data maintained by Data Governance.

## **3. Automation of the Model's Core Processes**

***3.1 Mandatory Automation***

| Class of Decisions | Why Automation Is Mandatory at PanEuropean | Validation Status in PEP (Section 8.1) |
| :---- | :---- | :---- |
| Privacy risk calculation | Several hundred calculations a year across five countries — DPIAs, releases and transformation requests (C2) — cannot be performed consistently by hand; the PET Assessment Module requires repeatable metric computation, confidence intervals and gates | Tested and deployed (conformance test suite run of 2 October 2026, evidence pack EVP-2026-0052): threat-based likelihood (Document 18, Section 3.2), severity factors (Section 3.4) and the residual-tier mapping for Projects 1–4; PET Assessment Module for structured record-level, synthetic and aggregate releases (Sections 3.3.1, 3.3.2, 3.3.4), including the failure gates and the lifetime ledger. **Not covered:** unstructured data and large language models (Document 18, Section 2); model inversion on generator parameters; gradient-reconstruction tests — recorded limitations |
| Evidence-pack compilation | Every decision requires a complete, sealed record; manual assembly risks gaps and undetected changes | Tested and deployed: sealed manifest with component hashes; superseding versions; separately sealed personal-data component; export in a documented, tool-independent format. **Planned:** signing of manifests with a managed key (target: next major PEP version) |
| Monitoring of limits, expiries and re-assessment triggers | The lifetime privacy-loss ledger for the retail customer population (Document 8, Section 3: ε ≤ 10.0 and δ ≤ 1×10⁻⁵, operational cap ε ≤ 7.0 per calendar year), the expiry of conditional acceptances and the annual re-assessment of anonymity conclusions must be tracked across all projects | Tested and deployed: ledger with ε and δ per run, including failed and observed runs; warning to the Privacy Operations Lead and the Chief Privacy Officer when a planned run would exceed the remaining headroom or the annual cap; reminders for acceptance expiries and anonymity re-assessments; the Group DPO receives the same information for advice. Metric thresholds are set in Document 18, not in Document 8 |
| Application of PET transformations | Manual pseudonymisation or synthesis is error-prone and not reproducible for audit by Internal Audit or the HBDI | Tested and deployed: pseudonymisation of customer identifiers (keyed hashing, keys held outside PEP); synthetic-data generation with a differentially private generator (DP statement of Document 18, Section 3.3.5); configuration recorded in the evidence pack. Parameters are in the PET Standard (Section 6) |

This list covers core processes C1 and C2. Consent Management (C5), Data Subject Rights (C3) and Cross-Border Transfer (C4) are not subject to mandatory automation at PanEuropean; Section 3.2 fixes their targeted automation.

***3.2 Targeted Automation of the Other Core Processes***

The Chief Privacy Officer, with IT Management, sets the priority of further automation using the criteria of Part A. As of the adoption date: priority 1 is completing the integration of PanEuropean's Consent Manager (C5), because the base integration exists; priority 2 is integrating PanEuropean's Data Subject Rights Portal (C3), because of the statutory response deadlines and the need to propagate restriction and erasure to derived data; priority 3 is automating the maintenance of transfer records (C4), because the current number of transfers (Document 12) can be handled manually without missing deadlines. The rules of the processes remain in Documents 13, 15, 12 and 20.

| Core process | Rationale for Targeted Automation | Current Status / Related Document |
| :---- | :---- | :---- |
| Consent Management (C5) | PanEuropean's Consent Manager passes PEP a per-customer flag "use permitted for marketing analytics" as a pre-filter before a transformation; the target is to extend the integration to other consent-based uses | Partially implemented; priority 1; process rules — Document 13 |
| Data Subject Rights (C3) | Automatically blocking active PEP calculation projects when processing is restricted (Art. 18), and propagating erasure or consent withdrawal to derived personal datasets along the lineage, would replace manual reconciliation by the Privacy Operations Lead | Not implemented; priority 2; process rules — Document 15; propagation rules — Document 11 |
| Cross-Border Transfer (C4) | Structured transfer records linked to the RoPA and to TIA-CLOUD-01, TIA-PSI-01 and TIA-LLM-01 would reduce manual effort | Performed manually; priority 3; process rules — Documents 12 and 20 |

## **4. Tooling Selection and Approval Criteria**

The criteria of Part A apply unchanged. The table records PanEuropean's evidence for PEP; replacing PEP with other tooling would not change the criteria.

| Criterion | Evidence at PanEuropean (illustrative) |
| :---- | :---- |
| Coverage of the methodology | Validation record (Section 8.1): Document 18 Projects 1–4 and the PET Assessment Module for structured data tested and deployed; limitations listed in Section 3.1 |
| Reproducibility | Configuration, input-data version and tooling version recorded for every run; re-runs of randomised mechanisms within the stated tolerance (conformance test suite, EVP-2026-0052); random seeds of DP mechanisms are not retained after the run |
| Evidence-pack integrity | Section 4.1 requirements tested; manifest signing planned (Section 3.1) |
| Security | PEP runs in a segregated environment in PanEuropean's EEA data centres; role-based access for named Privacy Engineers; generator parameters and checkpoints never leave PEP; configuration changes and access logged; the CISO confirmed the controls |
| Data location and transfers | Hosting and processing in the EEA. Remote technical support for production systems by Example Cloud Services Pvt Ltd (fictional, India) is a transfer governed by Document 12 (TIA-CLOUD-01); support staff of the PEP support provider access PEP only from the EEA (illustrative assumption) |
| Integration | Interfaces with the core banking platform, the data catalogue and the lineage service tested per the integration runbook |
| Minimisation | Source data used only inside PEP; Data Science receives synthetic or pseudonymised data where the task allows (Document 16) |
| Provider viability, continuity and exit | The external PEP support provider was assessed under Document 17 on financial statements and continuity arrangements — the support agreement alone was not treated as evidence of viability. Fallback procedure and exit plan in the TIP; the last export test (October 2026) reproduced all evidence packs and ledgers in readable form |
| ICT third-party requirements (DORA) | The PEP support arrangement is recorded in the DORA Register of Information maintained by ICT Risk Control (Document 3, Section 3.15). ICT Risk Control assessed that it does not support a critical or important function (illustrative assessment, reviewed annually, recorded under Document 17); the contract nevertheless contains the Art. 30 provisions on data location, audit, termination and exit assistance |
| AI components | The synthetic-data generator and the PII detector are recorded in the AI system inventory; the Model Risk and AI Governance function classified them as not high-risk under the AI Act in this use (illustrative assessment) |
| Transparency of limitations | Known limitations disclosed by the support provider and found in testing are listed in the validation record |
| Testability | Conformance test suite run in full on 2 October 2026 (EVP-2026-0052) |

The universal criteria apply when assessing the systems used for targeted automation (PanEuropean's Consent Manager, Data Subject Rights Portal and transfer records); the calculation-specific criteria do not, because those systems do not perform calculations under Document 18.

***Conclusion on the Automation Need***

As of the adoption date, the capabilities recorded as tested and deployed in PEP cover the four classes of Section 3.1 for structured data, with the limitations listed there. No alternative tooling is engaged. The coverage statement is valid only for the PEP version tested and is re-confirmed at each re-certification (Section 8.4).

## **5. The Tool-Neutral Governance Core Principle**

The neutrality test of Part A was applied to PanEuropean's governance documents during the October 2026 re-baselining. Findings: the earlier Privacy Role Competency Framework required a provider-issued platform certificate (replaced by an internal proficiency assessment, Document 6); the earlier Privacy Risk Appetite Statement justified a lenient matrix cell by platform metrics (removed; the matrix is severity-led, Document 8). No remaining rule, decision or delegation depends on PEP. Replacing PEP would require only an update of the TIP and of the validation record and, for a new external provider, an assessment under Document 17.

## **6. Technology Implementation Package**

PEP's technical specifications are kept outside the governance core, in a separately versioned TIP comprising:

* PanEuropean's PET Standard — pseudonymisation by keyed hashing with keys held by IT Security; synthetic-data generation with a differentially private generator, with the DP statement for each project (Document 18, Section 3.3.5; for example DPIA-CS-TRAIN-01 uses a customer-level privacy unit and a Rényi DP accountant); record-level and aggregate disclosure controls with the thresholds of Document 18, Part B. k-anonymity and differential privacy are documented as separate guarantees, each with the cases where it is used
* The evidence-pack specification — sealed manifest, component hashes, separately sealed personal-data component, superseding versions, export format
* The control-to-artefact matrix — each criterion of Section 4 mapped to an artefact and a test (for example, "Reproducibility" → configuration log and re-run tests)
* The integration runbook — PEP connections to the core banking platform, the data catalogue and the lineage service
* The conformance test suite, version 1.2 (illustrative), and its run results
* The continuity (fallback) procedure — for the four classes of Section 3.1: a manual, conservative procedure under which no release or transformation is approved without the required calculation; every fallback decision logged and recalculated in PEP after restoration; maximum duration 10 business days, after which the Privacy Operations Lead escalates to the Chief Privacy Officer
* The exit plan — export of evidence packs, ledgers, configurations, lineage and validation records; steps to bring in alternative tooling or another support provider; aligned with ICT Risk Control's register entry

The owner of the TIP is the Privacy Operations Lead, with Privacy Engineer(s) and IT Management. It is reviewed at every PEP version update. A change to the TIP is not an amendment to this document unless it affects Section 3.1, 4 or 8.

| System / scope point | Position relative to PEP | Coverage status |
| :---- | :---- | :---- |
| PanEuropean's core banking platform and data warehouse | Data sources for PEP calculations and transformations, after G-L | In scope |
| PEP | Risk calculation (Document 18), PET application, evidence-pack compilation, ledger and expiry monitoring — C1 and C2 | In scope |
| PanEuropean's RoPA (Document 21) and Privacy Risk Register (Document 22) | Receive references to PEP calculations and decisions | In scope (output) |
| HBDI; Group Internal Audit; external auditor | Receive evidence packs or extracts on request | Recipients, not part of the tooling |
| PanEuropean's Consent Manager (C5) — integrated with online banking and the mobile app | Passes the "marketing analytics permitted" flag as a pre-filter before transformations for consent-based marketing analytics | Targeted automation, partially implemented |
| PanEuropean's Data Subject Rights Portal (C3) | Not connected to PEP; restriction and erasure are reconciled manually by the Privacy Operations Lead | Targeted automation, not implemented; open item (Section 8.5) |
| Transfer records and TIAs (C4) | Maintained manually; Document 20 may request severity inputs from PEP | Targeted automation, manual |
| Assessment of the PEP support provider | Separate assessment of the provider | Out of scope of this map — Document 17 |
| PanEuropean's incident response | Not connected to PEP | Out of scope — Document 14 |
| PanEuropean's staff training | Not connected to PEP | Out of scope — Document 30 |

## **7. Relationship to Other Documents of the Model**

* Is the single connection point between PEP and PanEuropean's governance documents.
* The technology budget for PEP (licences, infrastructure, support) is adopted separately from the privacy function's budget (Document 4, Section 8).
* The classes of Section 3.1 implement Document 18 and the limits of Document 8; they are used in the activities of the RACI Matrix (Document 5, Sections 5.1 and 5.2); S9 "Operating the PEP Platform" — Privacy Operations Lead accountable, Privacy Engineers responsible (Document 5, Section 6).
* The targeted automation of Section 3.2 is aligned with Documents 13, 15, 12 and 20.
* Data location is aligned with Document 7 and Document 12 (India as a recipient country for remote technical support).
* The PEP support provider is assessed under Document 17; the DORA register interface is in Document 3, Section 3.15; the AI-component interface is in Document 3, Section 3.5.
* Evidence packs are retained under Document 11.

| Document | Maintenance mode | What changes when PEP changes |
| :---- | :---- | :---- |
| Document 9 (this document) | Joint | TIP and validation record; Section 4 only if a gap in the criteria appears |
| Document 18 (Privacy Risk Assessment Methodology) | Joint | Which metrics and tests are available as validated implementations and which are recorded as limitations |
| Document 19 (DPIA Methodology and Template) | Unilateral, with notification | References to PEP as the recording and calculation tool |
| Document 22 (Privacy Risk Register) | Unilateral, with notification | Versioning of calculation projects and register entries |

## **8. Review, Capability Validation and Re-certification**

***8.1 Validation Record***

The Privacy Operations Lead keeps PEP's validation record. Summary as of 20 October 2026 (illustrative): 31 capabilities recorded — 24 tested and deployed, 2 planned (manifest signing; automated propagation of erasure to derived data), 5 not verified (including model inversion on generator parameters, gradient reconstruction, and disclosure testing for unstructured text). Capabilities that are planned or not verified are not relied on in any decision.

***8.2 Conformance Test Suite***

Conformance test suite version 1.2 (illustrative) was run in full on 2 October 2026 (EVP-2026-0052). It includes the negative cases of Part A — among them, a test confirming that a G-L failure blocks the calculation regardless of scores, that an observed failed run is charged to the ledger, and that two concurrent runs cannot jointly exceed the annual cap. Two defects found in an earlier run (an inclusive instead of exclusive threshold for one metric; an export that omitted the ledger's observer field) were corrected and re-tested before the run of 2 October 2026.

***8.3 Independent Validation***

The Model Risk and AI Governance function (CRO area, second line; Document 3, Section 3.5), which is independent of the Privacy Engineers who configure PEP, validated the metric, attack-test and accountant implementations in September 2026 (EVP-2026-0050, illustrative). Open findings: the untested attack classes listed in Section 3.1, recorded as limitations with compensating access restrictions. Information-security certifications held by the PEP support provider were considered under Document 17; they did not replace this validation.

***8.4 Re-certification***

PEP was re-certified on 2 October 2026 on the basis of the conformance test suite run and the independent validation; the next scheduled re-certification is due by 2 October 2027 (planned). Unscheduled re-certification is triggered by the events listed in Part A, including a change of control over the PEP support provider and any change to hosting or support locations. A negative outcome is recorded; Privacy Engineers and IT Management submit a remediation plan to the Chief Privacy Officer within 90 days; affected capabilities are set to "not verified" and the fallback procedure applies to them; if conformity is not achieved in time, the Chief Privacy Officer proposes to the Management Board a decision on alternative tooling under the exit plan. TIA re-evaluations follow their own legal and monitoring triggers (Document 20) and are not tied to PEP re-certification.

***8.5 Review of This Document***

This document is reviewed at least annually under PanEuropean's Policy Review Cycle (Document 29) and upon the triggers of Part A. The annual review reconciles the targeted automation of Section 3.2 and assesses effectiveness against indicators, with the following targets for the first year of version 2.0: validated PEP calculation used for 100% of Medium-and-above decisions in C1/C2; evidence pack compiled within one business day of the calculation; cumulative fallback duration below 10 business days a year; no open validation finding older than 12 months without a remediation plan. Open item for the next review: integration of the Data Subject Rights Portal with PEP (restriction and erasure propagation), currently handled manually. Amendments are adopted by the Management Board on the Chief Privacy Officer's proposal, after consulting the Privacy Risk Committee and the Group DPO.

## **9. Approval**

Version 1.0 (1 March 2026) was adopted by the Management Board; the Group DPO was document owner at that time. Version 2.0 was adopted by the Management Board on 20 October 2026 on the proposal of the Chief Privacy Officer, after consulting the Privacy Risk Committee and the Group DPO. Document owner: Chief Privacy Officer. Group DPO advice is on file.

# **Normative Basis and References**

* Regulation (EU) 2016/679 (GDPR): Arts. 4(5), 5(1)(c), 5(2), 6, 6(4), 18, 24, 25, 32, 35(7); Recital 26.
* Regulation (EU) 2022/2554 (DORA): Arts. 28 (incl. 28(3) register of information, 28(4) pre-contract assessment, 28(8) exit strategies), 29 (ICT concentration risk), 30 (key contractual provisions), 31 (designation of critical ICT third-party service providers).
* Regulation (EU) 2023/2854 (Data Act), Chapter VI — switching between data processing services.
* Regulation (EU) 2024/1689 (AI Act), as amended by the AI Omnibus — classification of AI components; dates per Document 7.
* CJEU, C-413/23 P, *EDPS v SRB*, 4 September 2025 (the recipient's means as part of the contextual analysis; not a general rule on Chapter V).
* EDPB Guidelines 01/2025 on pseudonymisation.
* EDPB Guidelines 02/2026 on anonymisation — public-consultation draft (8 July 2026), not final; orientation only.
* Article 29 Working Party, Opinion 05/2014 on Anonymisation Techniques (WP216).
* NIST SP 800-226, *Guidelines for Evaluating Differential Privacy Guarantees* (final, March 2025).
* NIST SP 800-188, *De-Identifying Government Data Sets*.
* ENISA, *Pseudonymisation techniques and best practices* (2019); ENISA, *Data Protection Engineering* (2022) — engineering guidance, not certification.
* ISO/IEC 20889 (de-identification techniques) and ISO/IEC 27559 (de-identification framework) — bibliographic pointers only; no clause-level mapping is claimed.

# **Document History (PGF)**

| Release | Date | Changes |
| :---- | :---- | :---- |
| 1.0.0-rc.1 | 2026-10-26 | Canonical English Markdown; changes from internal ver.2: product names, provider attributions and capability promises removed — Part B uses the fictional "Bank's privacy engineering platform (PEP, illustrative)" with capabilities stated only as validation-record statuses and documented limitations; document confirmed as the single connection point to tooling, with a strengthened neutrality test covering worked-example decisions and credentials, and a note that a separately published implementation profile is never a PGF dependency; principles added on validated capabilities only, human decision (no replacement of G-L, Art. 35(7), G-36, G-TIA or anonymity conclusions) and lawful processing for PET application; "threshold monitoring" replaced by monitoring of the lifetime privacy-loss ledger, acceptance expiries and anonymity re-assessments (thresholds set by Document 18); selection criteria extended — reproducibility for randomised mechanisms and seed protection, evidence-pack integrity (sealing, superseding not editing, minimisation, retention by the applicable rule including deletion, minimal record after purge only where lawful), security, exit and continuity, DORA ICT third-party requirements (Arts. 28–30, register of information, exit strategy; critical or important function terminology), AI components, testability; NIST SP 800-226 checklist for DP claims; synthetic data stated as not safe by default, with empirical attack testing per Document 18; k-anonymity and DP distinguished; pseudonymisation not anonymisation (C-413/23 P, EDPB Guidelines 01/2025); Section 8 rebuilt around a validation record, a documented repeatable conformance test suite with negative cases, independent validation and re-certification triggers; "required certification" replaced by defined triggers; ownership moved to the EPPO and adoption to Executive Management; Part B re-baselined as version 2.0 (20 October 2026) with targets instead of operating history; calqued terms ("perimeter", "closes the need") and the "EDPB criteria" attribution corrected; example dates shifted by −12 months; references added |
