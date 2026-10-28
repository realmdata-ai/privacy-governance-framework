---
title: "Regulatory Applicability Matrix"
document_id: PGF-07
level: 1
release_version: 1.0.0
status: publication-ready
authors: ["Alexey Neyman", "Val Khvatov"]
regulatory_reference_date: 2026-10-26
licence: "CC BY 4.0"
rights_holder: "REALM INVEO"
source_provenance: "Derived from internal source set ver.2: Level1/7. Regulatory_Applicability_Matrix_Template_and_Example_ENG.docx.md; sha256 3792b39563fa6b000559b14fbcc01e0d0d633a1afbc0d1e1000f81c0d97e3b70"
---
# PGF-07 — Regulatory Applicability Matrix

*Privacy Governance Framework (PGF) · Level 1 — Strategic Documents · Version 1.0.0 · Regulatory reference date: 26 October 2026*

> **Status and use.** Part A is a reusable template. Part B is a worked example for a fictional organisation (PanEuropean Bank AG); all names, figures, dates and records in Part B are illustrative. Nothing in this document is legal advice or a statement about any real organisation, product or provider.

# About This Document

The Regulatory Applicability Matrix is Document 7 of the Privacy Governance Framework (PGF). It records which data protection framework, and which adjacent regime, applies in which jurisdiction and to which activity of the organisation, and fixes the specific requirements that differ between them — lawful-basis particulars, breach thresholds, recipients and clocks, rights deadlines, representatives and registration, localisation, privacy-officer mandates, and transfer mechanisms.

It is an input to the Privacy Policy and Notice (Document 1), the Cross-Border Data Transfer Policy (Document 12), the Data Breach Response Policy (Document 14), the Vendor and Third-Party Privacy Risk Policy (Document 17), the DPIA Methodology (Document 19), the TIA Methodology (Document 20) and other documents (Section 7). These documents do not redefine regulatory requirements; they cite this matrix.

The matrix records applicability; it does not replace legal opinions on the content of a requirement. Law in force, adopted law not yet applicable, proposals and draft guidance are recorded as separate facts, with dates.

# How to Use This Document

Part A is a drafting template. Bracketed text in bold italics marks a placeholder. Callouts marked **Guidance** are removed from the adopted document. Part B shows the template completed for a fictional pan-European retail bank as at 26 October 2026.

> **Guidance.** Before drafting, obtain from Legal the list of jurisdictions in which the organisation is established or whose law applies to it for another reason (for example, because it offers goods or services to residents there), and the list of countries to which it transfers personal data. An error in these lists devalues the rest of the matrix.

# Table of Contents

**Part A — Template**  
1. Purpose of This Document  
2. Principles for Building the Matrix  
3. List of Jurisdictions and Applicable Frameworks (3.1 Applicability Map — Canada)  
4. The "Jurisdiction × Requirement" Matrix  
5. Adjacent Regulatory Acts, Pending Changes and Interpretive Sources  
6. Review Process Upon a Change in Legislation  
7. Relationship to Other Documents of the Model  
8. Review and Amendment  
9. Approval  
**Part B — Worked Example (fictional)** — Sections 1–9 as in Part A  
**Normative Basis and References**  
**International Adaptation**  
**Document History (PGF)**

# Part A — Template

Regulatory Applicability Matrix of ***[Organisation Legal Name]***

Effective date: ***[DD Month YYYY]***   ·   Version: ***[x.x]***   ·   Document owner: ***[Executive Privacy Programme Owner (EPPO)]***   ·   Adopted by: ***[Executive Management]***

Version history (template)

| Version | Date | Changes |
| :---- | :---- | :---- |
| ***[1.0]*** | ***[DD.MM.YYYY]*** | ***[First version of the document]*** |
| ***[x.x]*** | ***[DD.MM.YYYY]*** | ***[Brief description of material changes]*** |

> **Guidance.** Record material changes only — entry into a new jurisdiction, a change in applicable law, a new adjacent regime, or a change in a breach or rights deadline.

## 1. Purpose of This Document

This document maps the jurisdictions whose law applies to ***[organisation name]*** to the applicable data protection frameworks and adjacent regimes, and fixes the requirements that differ between them, so that other documents of the model cite it rather than redefining requirements independently.

> **Guidance.** Without this document, each policy carries its own, incomplete and gradually diverging version of the regulatory requirements. The matrix prevents that by being the single place where applicability is decided.

## 2. Principles for Building the Matrix

> **Guidance.** Territorial scope is a legal test, not a business label. Under the GDPR, the Regulation applies to processing in the context of the activities of an establishment in the Union, regardless of where the processing takes place (Art. 3(1)); Art. 3(2) applies only to controllers or processors **not established** in the Union that offer goods or services to, or monitor the behaviour of, individuals in the Union. Other jurisdictions have their own tests (for example, the "real and substantial connection" applied under PIPEDA, or the extraterritorial provisions of the UK GDPR, the revFADP, Brazil's LGPD or India's DPDP Act). Record the test that makes each jurisdiction applicable.

* ***[Territorial-scope principle — a jurisdiction is listed because its law applies to the organisation under that law's own territorial test: establishment (e.g., GDPR Art. 3(1)), targeting or monitoring by a non-established organisation (e.g., GDPR Art. 3(2)), or an equivalent test. Where several national laws implement or supplement one regime (e.g., national GDPR derogations), each national law's own territorial rule is recorded]***
* ***[Presence versus transfer — a country to which data are only transferred for processing (e.g., a service provider's location) does not thereby become a jurisdiction listed in Section 3; it is governed by the Cross-Border Data Transfer Policy (Document 12). Whether an operation is a transfer follows the three cumulative criteria of EDPB Guidelines 05/2021 (exporter subject to the GDPR; data made available, including by remote access, to another controller, joint controller or processor; importer in a third country); remote access by the organisation's own employees while abroad is not a transfer]***
* ***[Cumulative-requirements principle — where two applicable frameworks set different but cumulative requirements on the same matter, the organisation may adopt the stricter one as a single design standard; this is a design choice, not a legal rule. Where requirements contradict each other (e.g., mandatory retention under AML law versus erasure), the conflict is resolved by a legal opinion and recorded, not by "strictest wins"]***
* ***[Single-source-of-truth principle — each requirement is fixed here once; dependent documents cite it. A divergence between this matrix and a dependent document triggers immediate reconciliation; pending reconciliation, the most recent legal opinion applies, and where none exists, the more protective requirement]***
* ***[Mandatory-review-trigger principle — any change in applicable law, its date of application, or authoritative guidance initiates a review (Section 6) without waiting for the scheduled cycle]***
* ***[Law-in-force principle — law in force, adopted law not yet applicable, legislative proposals and draft guidance are recorded separately (Section 5.1); a proposal never changes an obligation]***

## 3. List of Jurisdictions and Applicable Frameworks

> **Guidance.** For each jurisdiction, record the territorial hook, the framework, and the competent supervisory authority with its role. Under the GDPR one-stop-shop, an organisation with establishments in several Member States has one **lead supervisory authority** for cross-border processing — the authority of its main establishment (Art. 56(1)); the authorities of other Member States where it is established or whose residents are substantially affected are **concerned supervisory authorities** (Art. 4(22)), cooperating under Art. 60; a local case may be handled by a local authority (Art. 56(2)). A financial or sectoral supervisor is never the data protection authority; list it separately because adjacent regimes report to it. Flag countries that are only recipients of transfers separately.

| Jurisdiction | Territorial hook / presence status | Primary framework | Competent data protection authority and role | Representative / registration duty | Other supervisors (separate tracks) |
| :---- | :---- | :---- | :---- | :---- | :---- |
| ***[Jurisdiction 1 — e.g., the Member State of the main establishment]*** | ***[Establishment — head office (GDPR Art. 3(1))]*** | ***[GDPR + national data protection law]*** | ***[Name — lead SA for cross-border processing]*** | ***[None (EU-established); DPO contact communicated to the SA (Art. 37(7))]*** | ***[e.g., financial supervisor]*** |
| ***[Jurisdiction 2 — e.g., a Member State with a branch]*** | ***[Establishment — branch (GDPR Art. 3(1))]*** | ***[GDPR + national law]*** | ***[Name — concerned SA; local cases under Art. 56(2)]*** | ***[None]*** | ***[e.g., host-state authority]*** |
| ***[Jurisdiction 3 — e.g., a non-EU country whose law applies because the organisation offers services to its residents — such as Brazil (LGPD), India (Digital Personal Data Protection Act 2023), California (CCPA as amended by the CPRA) or Saudi Arabia (Personal Data Protection Law)]*** | ***[Targeting / extraterritorial provision of that law]*** | ***[Name the specific statute]*** | ***[Name of the authority]*** | ***[Local representative or registration where that law requires it]*** | ***[…]*** |
| ***[Jurisdiction 4 — e.g., United Kingdom, Switzerland or Canada]*** | ***[…]*** | ***[UK GDPR + DPA 2018 / revFADP / PIPEDA and provincial law — see Section 3.1]*** | ***[ICO / FDPIC / OPC and provincial commissioners]*** | ***[…]*** | ***[…]*** |

Countries that are only recipients of personal data (not listed above): ***[specify, with a reference to Document 12]***.

### 3.1 Applicability Map — Canada

This map is stated once here and cited by other documents.

| Situation | Applicable private-sector law |
| :---- | :---- |
| Private-sector organisation collecting, using or disclosing personal information in the course of commercial activities in a province without a substantially similar private-sector law | PIPEDA |
| Private-sector organisation operating intra-provincially in Québec, Alberta or British Columbia, which have substantially similar laws | The provincial law — Québec: Act respecting the protection of personal information in the private sector (P-39.1); Alberta and British Columbia: their Personal Information Protection Acts |
| Personal information crossing provincial or national borders in the course of commercial activities | PIPEDA (in addition to any applicable provincial law) |
| Federal works, undertakings or businesses (e.g., banks, airlines, telecommunications) | PIPEDA, including for employee information |

Out-of-scope extensions: Alberta and British Columbia PIPA content, public-sector privacy laws and health-sector privacy laws are named here for completeness but are not developed in the PGF; an organisation subject to them extends the matrix. Bill C-36 (*Protecting Privacy and Consumer Data Act*, introduced 15 June 2026, at second reading) is a proposal and does not replace PIPEDA (Section 5.1).

## 4. The "Jurisdiction × Requirement" Matrix

> **Guidance.** Columns should show requirements that genuinely differ between the organisation's jurisdictions. Where a requirement is identical across all listed jurisdictions (for example, the GDPR 72-hour clock across EU Member States), record it once as a baseline row and keep only deviations in the country rows. Keep a separate column where the **composition** of a duty differs even if the number does not. Adjacent regimes with their own clocks (for example, DORA for financial entities) are recorded in Section 5, not mixed into the data protection columns.

### 4.1 Legal particulars

| Jurisdiction | Lawful-basis particulars | Special categories and biometrics | Digital-consent age (GDPR Art. 8 or equivalent; information-society services offered on the basis of consent only) | Minors' contractual capacity | Employee data | Mandatory DPIA list; DPO / privacy-officer mandate |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| ***[Jurisdiction 1]*** | ***[National particulars beyond the baseline bases]*** | ***[National conditions or safeguards]*** | ***[e.g., 16]*** | ***[National civil and banking law]*** | ***[National employment-data rules; employee-representation rights]*** | ***[SA list under Art. 35(4); national DPO threshold beyond Art. 37]*** |
| ***[Jurisdiction 2]*** | ***[…]*** | ***[…]*** | ***[…]*** | ***[…]*** | ***[…]*** | ***[…]*** |

> **Guidance.** The Art. 8 age differs between Member States (13–16) but applies only where an information-society service is offered directly to a child and the basis is consent. Products offered on the basis of a contract are governed by national rules on minors' legal capacity and parental or court consent; record those separately.

### 4.2 Breach, rights, transfers and organisational duties

| Jurisdiction | Breach threshold | Breach recipient | Breach clock and records | Data-subject access deadline | Default transfer mechanism | Data localisation | Representative / registration | Privacy-officer mandate |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| ***[Baseline — EU/EEA, GDPR]*** | ***[Notify the SA unless the breach is unlikely to result in a risk; communicate to individuals where the risk is high]*** | ***[Competent SA — lead SA for cross-border processing (EDPB Guidelines 9/2022)]*** | ***[Without undue delay and, where feasible, within 72 hours of becoming aware; every breach recorded (Art. 33(5)); processor → controller without undue delay (Art. 33(2))]*** | ***[One month, extendable by two months (Art. 12(3))]*** | ***[Adequacy (Art. 45) where it covers the recipient; otherwise SCCs or other Art. 46 tool with TIA; Art. 49 only exceptionally, interpreted restrictively and subject to the conditions of the derogation used]*** | ***[None in the GDPR; check sectoral rules]*** | ***[Art. 27 representative only for non-EU organisations under Art. 3(2)]*** | ***[DPO where Art. 37(1) or national law requires]*** |
| ***[Jurisdiction-specific deviation]*** | ***[…]*** | ***[…]*** | ***[…]*** | ***[…]*** | ***[…]*** | ***[…]*** | ***[…]*** | ***[…]*** |

> **Guidance.** In the access-deadline column, also record whether supervisory-authority practice in the jurisdiction treats the period as paused while identity information requested under Art. 12(6) is awaited (Document 15, Section 5). Where practice differs or is unclear, record that the organisation computes the deadline from receipt and does not rely on a pause.

### 4.3 Reference values for frequently used non-EU regimes

> **Guidance.** The rows below are headline reference values for the regimes covered by the PGF's international adaptation. Confirm each value against the consolidated text before adoption; for other regimes (for example, LGPD, the DPDP Act, CCPA/CPRA or a Saudi PDPL), complete the row from a legal opinion.

| Regime | Breach threshold, recipient and clock | Access deadline | Representative / registration | Privacy-officer mandate | Localisation / transfer rule |
| :---- | :---- | :---- | :---- | :---- | :---- |
| UK GDPR + DPA 2018 (as amended by the Data (Use and Access) Act 2025, phased commencement) | Same test as the GDPR; to the ICO within 72 hours of awareness where feasible; individuals where the risk is high | One month, extendable by two months; DUAA rules on the running of the period apply as commenced | UK representative for non-UK organisations within the UK's extraterritorial scope; data protection fee payable to the ICO unless exempt | DPO under UK GDPR Art. 37 | No localisation; UK transfer rules (adequacy regulations, UK transfer instruments) |
| Switzerland — revFADP | Breach likely to result in a high risk: to the FDPIC as soon as possible; individuals where necessary for their protection or where the FDPIC requires | 30 days | Swiss representative for foreign controllers where the revFADP so requires | Data protection advisor optional | No localisation; disclosure abroad to countries with adequate protection or with safeguards |
| Canada — PIPEDA | Breach of security safeguards creating a real risk of significant harm: report to the OPC and notify individuals as soon as feasible; records of **every** breach of security safeguards kept for 24 months | 30 days (extension possible in limited cases with notice) | None | Individual(s) accountable for compliance (Principle 4.1) | No localisation; comparable protection for transfers to service providers by contract (Principle 4.1.3) |
| Québec — P-39.1 | Confidentiality incident presenting a risk of serious injury: notify the Commission d'accès à l'information and the persons concerned promptly; register of **all** confidentiality incidents | 30 days | None | Person in charge of the protection of personal information (by default the person with the highest authority; delegable in writing); title and contact details published | No localisation; a privacy impact assessment and written agreement before communicating personal information outside Québec |

The GDPR 72-hour clock is never imported into Canadian or Swiss rows.

### 4.4 Other material particulars

***[National particulars not covered above — for example, post-mortem data rights, national identifier rules, banking secrecy, credit-information systems, video surveillance, telemarketing opt-out registers.]***

When describing the default transfer mechanism, record the Art. 49 derogations as exceptional, interpreted restrictively and subject to the specific conditions of the derogation used — including the "occasional" limit for the contract and legal-claims derogations and the "non-repetitive" limit for the residual compelling-legitimate-interests derogation, where applicable (EDPB Guidelines 2/2018); they do not replace the primary mechanism. A stricter organisational rule is labelled as internal policy. When describing DPO or privacy-officer mandates, record national thresholds that add to the Art. 37(1) core-activities test; the role profile is in Document 6.

## 5. Adjacent Regulatory Acts, Pending Changes and Interpretive Sources

> **Guidance.** Not every act that affects privacy governance is a data protection law. Operational-resilience, AI, consumer-credit, anti-money-laundering, electronic-communications, banking-secrecy and data-access regimes create obligations that intersect with privacy. Record them here, with their own owners, recipients and clocks, so that Sections 3–4 remain a map of data protection law. Every entry carries a review trigger (Section 6).

| Act | Nature of regulation | Intersection with privacy | Owner of the separate track | Related document |
| :---- | :---- | :---- | :---- | :---- |
| ***[Operational-resilience regulation, e.g., DORA for financial entities]*** | ***[ICT risk management and incident reporting — not a data protection law]*** | ***[A separate reporting track for major ICT-related incidents to the financial supervisor; ICT third-party register and contract terms intersecting with vendor due diligence]*** | ***[ICT risk function]*** | ***[Documents 3 (Sections 3.14–3.15), 14, 17]*** |
| ***[Cybersecurity regime, e.g., NIS2]*** | ***[Cybersecurity risk management and incident notification]*** | ***[For entities where a sector-specific act such as DORA applies, that act's provisions apply instead (NIS2 Art. 4); otherwise a separate notification track]*** | ***[CISO]*** | ***[Documents 3, 14]*** |
| ***[AI regulation, e.g., the EU AI Act]*** | ***[Risk-tiered regulation of AI systems — not a data protection law]*** | ***[High-risk classification of certain automated processing (e.g., creditworthiness assessment); deployer duties including the FRIA, which complements the DPIA]*** | ***[AI governance function]*** | ***[Documents 3 (Section 3.5), 19]*** |
| ***[Sector rules on consumer credit, AML, electronic marketing, banking secrecy, credit-information systems, data access]*** | ***[…]*** | ***[…]*** | ***[…]*** | ***[…]*** |

This list is not exhaustive and does not replace a legal opinion on the applicability of a specific act.

> **Guidance.** This section may also include voluntary industry codes, ethical commitments and supervisory guidance without the force of law, where non-compliance would carry material reputational or other consequences. The EPPO proposes their inclusion on that basis, with Legal's and the DPO's advice; inclusion is not automatic.

### 5.1 Pending Changes (not law in force)

> **Guidance.** Record legislative proposals, adopted acts not yet applicable and draft guidance here, with their stage and date. They are review triggers; they do not change obligations until adopted and applicable.

| Item | Stage and date | What would change | Action |
| :---- | :---- | :---- | :---- |
| ***[Proposal / draft guidance]*** | ***[Stage, date, source]*** | ***[Summary]*** | ***[Watch; impact assessment when adopted]*** |

### 5.2 Sources and Standards Addressed in Other Documents

> **Guidance.** This table is a pointer, not the substance of a requirement. It keeps interpretive guidance, case law and technical standards traceable to the document that applies them.

| Source | Source type | Why not addressed in substance here | Document where addressed |
| :---- | :---- | :---- | :---- |
| ***[Regulator guidance on a requirement fixed in Sections 3–4]*** | ***[Interpretive guidance without the force of law]*** | ***[Details how a requirement is applied, not where it applies]*** | ***[Document applying it]*** |
| ***[Case law setting an interpretive standard]*** | ***[Precedent]*** | ***[Sets a criterion for a methodology]*** | ***[Document using the criterion]*** |
| ***[International technical standard]*** | ***[Voluntary standard]*** | ***[Methodological basis, not a legal requirement]*** | ***[Document using it]*** |
| ***[Component of a mechanism fixed in Section 4, e.g., an SCC clause]*** | ***[Part of a mechanism already referenced]*** | ***[Requires a substantive assessment]*** | ***[Document carrying out the assessment]*** |

## 6. Review Process Upon a Change in Legislation

> **Guidance.** Use the Regulatory Monitoring process (Document 5, row G4) — do not create a parallel monitoring process for this document.

| Stage | Role (Document 5) | Timeframe |
| :---- | :---- | :---- |
| ***[Identifying a change in law, its date of application, or authoritative guidance]*** | ***[Privacy Officer(s) and Legal — Responsible; EPPO — Accountable; DPO — Consulted]*** | ***[Continuous]*** |
| ***[Assessing the impact on this matrix]*** | ***[Legal — Responsible for the legal assessment; EPPO — Accountable; DPO — Consulted]*** | ***[[X] business days from identification]*** |
| ***[Updating the matrix]*** | ***[Privacy Operations Lead]*** | ***[[X] business days after the assessment]*** |
| ***[Cascading notification to dependent documents]*** | ***[Privacy Operations Lead — notifies the owners of Documents 1, 12, 14, 20 and, for adjacent regimes (Section 5), Documents 3, 6, 17, 18, 19 and 21]*** | ***[Immediately after the update]*** |
| ***[Adopting a material change]*** | ***[Executive Management, on the EPPO's proposal, after the DPO's advice; Governing Body committee informed]*** | ***[Per the Policy Review Cycle (Document 29), or before the date of application if earlier]*** |

A change that does not alter any requirement for processing (for example, the renaming of an authority) is recorded by the EPPO without escalation; the materiality criterion is whether an actual requirement changes.

## 7. Relationship to Other Documents of the Model

This document is an input to:

* ***[the Privacy Policy and Notice (Document 1) — jurisdiction-specific information duties, rights and authorities]***
* ***[the Cross-Border Data Transfer Policy (Document 12) — recipient countries and mechanisms]***
* ***[the Data Breach Response Policy (Document 14) — breach thresholds, recipients and clocks, and the separate adjacent-regime tracks]***
* ***[the TIA Methodology (Document 20) — requirements specific to the jurisdiction of data origin]***
* ***[the Interface and Integration Model (Document 3, Sections 3.5, 3.14 and 3.15) — AI governance, ICT risk and outsourcing interfaces for the adjacent regimes in Section 5]***
* ***[the Vendor and Third-Party Privacy Risk Policy (Document 17) — ICT third-party and outsourcing requirements]***
* ***[the Privacy Role Competency Framework (Document 6) — DPO and privacy-officer mandates]***
* ***[the Privacy Risk Assessment Methodology (Document 18) — legal facts used by G-L and track (b)]***
* ***[the DPIA Methodology (Document 19) — national Art. 35(4) lists and AI Act FRIA interplay]***
* ***[the Record of Processing Activities (Document 21) — the record-keeping duty and its national particulars]***

> **Guidance.** A dependent document whose requirement differs from this matrix signals divergence between sources of truth. Reconcile immediately; pending reconciliation, the most recent legal opinion applies and, absent one, the more protective requirement. Updating a dependent document without updating this matrix is a process error.

## 8. Review and Amendment

This document is reviewed under the continuous-improvement principle (Charter, Section 7) and ***[the Policy Review Cycle, Document 29]***, and immediately upon a change in applicable law (Section 6). Amendments are prepared by ***[the EPPO]***, with Legal's assessment and the DPO's advice, and adopted by ***[Executive Management]***; non-material changes are recorded by ***[the EPPO]*** (Section 6).

## 9. Approval

This document was adopted by ***[Executive Management]*** on ***[date]***. Document owner: ***[EPPO]***.

# Part B — Worked Example (fictional)

PanEuropean Bank AG — Regulatory Applicability Matrix

Version: 3.0   ·   Adopted: 20 October 2026   ·   Effective date: 10 November 2026 (scheduled)   ·   Document owner: Chief Privacy Officer (EPPO)   ·   Adopted by: Management Board

*Fictional entity, prepared for illustration only.*

Fictional document history (illustrative)

| Version | Date | Changes |
| :---- | :---- | :---- |
| 1.0 | 1 March 2026 | First version, developed alongside the Charter |
| 2.0 | 22 September 2026 | Pointer table for interpretive sources added; precise GDPR citations; transfer mechanisms per recipient |
| 3.0 | Adopted 20 October 2026; effective 10 November 2026 (scheduled) | Supervisory-authority roles under the one-stop-shop (HBDI lead; CNIL, Garante, AEPD and Prezes UODO concerned); breach notification routed to the HBDI; DORA recorded as a bank-wide regime with its own owner and recipient; AI Act dates updated after the AI Omnibus; CCD2, AMLR, ePrivacy and national marketing rules, banking secrecy, credit-information rules, NIS2, the Data Act and the GDPR Procedural Regulation added; German employee-data position updated after CJEU C-34/21; pending-changes block added; ownership moved to the Chief Privacy Officer and adoption to the Management Board |

## 1. Purpose of This Document

This document maps the law applicable to PanEuropean Bank AG in its five countries of establishment — Germany, France, Italy, Spain and Poland — and the adjacent regimes that apply to it as a credit institution. Before it was adopted, the customer privacy notice and internal procedures described each country's requirements separately and had diverged; this matrix is now the single source cited by the Privacy Policy and Notice, the Cross-Border Data Transfer Policy, the Data Breach Response Policy and the TIA Methodology.

## 2. Principles for Building the Matrix

* Territorial scope — the GDPR applies to PanEuropean under Art. 3(1): all processing takes place in the context of the activities of its head office in Frankfurt am Main (main establishment) or its branches in France, Italy, Spain and Poland, which are establishments in the Union; Art. 3(2) does not apply to PanEuropean. If PanEuropean offered banking services in a sixth EEA country without a branch, it would do so under the freedom to provide services notified under the CRD passporting procedure; the GDPR would still apply under Art. 3(1), and Legal would determine which national data protection provisions of that country apply under their own territorial rules.
* Presence versus transfer — India (remote technical support by Example Cloud Services Pvt Ltd, fictional; the partner bank for anti-fraud matching) and the United States (Example AI Provider Inc., fictional, customer-service assistant) are recipient countries governed by the Cross-Border Data Transfer Policy, not jurisdictions in Section 3.
* Cumulative-requirements principle — where national rules differ but are cumulative, PanEuropean may adopt a single design standard; for example, the app's biometric log-in stores the template only on the customer's device in all five countries. This is an internal design choice. Contradictory requirements (for example, AML record retention versus an erasure request) are resolved by General Counsel's legal opinion, not by "strictest wins".
* Single source of truth — the GDPR breach rule (72 hours from awareness, lead SA) is fixed here once; the Data Breach Response Policy cites it.
* Mandatory review trigger — a change in the law of any of the five countries, in EU law, or in the date of application of an adjacent regime triggers an unscheduled review.
* Law in force — proposals such as the Digital Omnibus are recorded in Section 5.1 and do not change PanEuropean's obligations.

## 3. List of Jurisdictions and Applicable Frameworks

| Jurisdiction | Territorial hook / presence status | Primary framework | Competent data protection authority and role | Representative / registration duty | Other supervisors (separate tracks) |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Germany | Head office and main establishment, Frankfurt am Main (Hesse); German credit institution licence DE-CI-48213 (Art. 3(1)) | GDPR + Federal Data Protection Act (BDSG) | Der Hessische Beauftragte für Datenschutz und Informationsfreiheit (HBDI) — **lead SA** for cross-border processing (Art. 56(1)) | None; Group DPO contact communicated to the HBDI (Art. 37(7)) | ECB (SSM) and BaFin — prudential supervision; DORA incident reporting |
| France | Branch — establishment (Art. 3(1)); CRD branch passport | GDPR + Loi n° 78-17 du 6 janvier 1978 relative à l'informatique, aux fichiers et aux libertés | CNIL — **concerned SA** (Art. 4(22)); local cases under Art. 56(2) | None; DPO contact communicated where national law requires | Host-Member-State authorities for the matters reserved to them |
| Italy | Branch — establishment (Art. 3(1)); CRD branch passport | GDPR + Codice in materia di protezione dei dati personali (D.Lgs. 196/2003, as amended by D.Lgs. 101/2018) | Garante per la protezione dei dati personali — **concerned SA**; local cases under Art. 56(2) | None; DPO contact communicated where national law requires | Host-Member-State authorities for the matters reserved to them |
| Spain | Branch — establishment (Art. 3(1)); CRD branch passport | GDPR + Ley Orgánica 3/2018, de Protección de Datos Personales y garantía de los derechos digitales (LOPDGDD) | Agencia Española de Protección de Datos (AEPD) — **concerned SA**; local cases under Art. 56(2) | None; DPO designation communicated to the AEPD | Host-Member-State authorities for the matters reserved to them |
| Poland | Branch — establishment (Art. 3(1)); CRD branch passport | GDPR + Ustawa z dnia 10 maja 2018 r. o ochronie danych osobowych | Prezes Urzędu Ochrony Danych Osobowych (President of the Personal Data Protection Office, UODO) — **concerned SA**; local cases under Art. 56(2) | None; DPO contact communicated where national law requires | Host-Member-State authorities for the matters reserved to them |

Countries that are only recipients of personal data: India and the United States — governed by the Cross-Border Data Transfer Policy (Document 12), not this matrix.

From 2 April 2027, cross-border complaint handling and enforcement procedures between the HBDI and the concerned SAs follow the GDPR Procedural Regulation (EU) 2025/2518 (Section 5).

### 3.1 Applicability Map — Canada

Not applicable: PanEuropean has no establishment in Canada and does not offer services to individuals there. The map in Part A, Section 3.1 applies if that changes.

## 4. The "Jurisdiction × Requirement" Matrix

### 4.1 Legal particulars

| Jurisdiction | Lawful-basis particulars | Special categories and biometrics | Digital-consent age (Art. 8; ISS on consent only) | Minors' contractual capacity | Employee data | Mandatory DPIA list; DPO mandate |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Germany | GDPR bases; BDSG supplements them for specific situations | BDSG §22 sets conditions and a list of appropriate safeguards for special categories | 16 (no national derogation) | Civil-law rules on minors' legal capacity and parental or court consent; accounts for minors opened only with legal representatives | After CJEU C-34/21 *Hauptpersonalrat* (30 March 2023), the compatibility of §26(1) BDSG with Art. 88(2) GDPR is questionable; PanEuropean relies on Art. 6(1)(b), (c) or (f) GDPR directly for employee data and applies §26 BDSG only as far as it remains applicable. Technical monitoring of employees is subject to works-council co-determination under the Works Constitution Act (§87(1) no. 6 BetrVG), not to employee consent | List of the German supervisory authorities under Art. 35(4); DPO mandatory under BDSG §38 where at least 20 persons are constantly engaged in automated processing — in addition to Art. 37(1), which already requires a DPO for PanEuropean's core activities |
| France | GDPR bases | CNIL guidance on biometric authentication; PanEuropean's device-only template design applies | 15 | National civil law | National employment law; staff-representative consultation where applicable | CNIL list under Art. 35(4); DPO under Art. 37(1) |
| Italy | GDPR bases | Garante safeguard measures for genetic, biometric and health data (Codice Art. 2-septies); Garante general provision on biometrics (12 November 2014) | 14 (Codice Art. 2-quinquies) | National civil law | National employment law, including rules on remote monitoring of workers | Garante list under Art. 35(4); DPO under Art. 37(1) |
| Spain | GDPR bases; LOPDGDD specific provisions (e.g., credit information systems, Art. 20; video surveillance, Art. 22) | AEPD guidance applied; strict necessity assessment for biometric processing | 14 (LOPDGDD Art. 7) | National civil law | LOPDGDD digital-rights provisions for employees | AEPD list under Art. 35(4); LOPDGDD Art. 34 lists categories of entities that must designate a DPO, including credit institutions |
| Poland | GDPR bases | No national biometric rule recorded; GDPR Art. 9 applies | 16 (no national derogation) | National civil law | Labour Code rules on employee data and monitoring | UODO list under Art. 35(4); DPO under Art. 37(1) |

### 4.2 Breach, rights, transfers and organisational duties

All five countries apply the GDPR without national deviation on the items below, so they are recorded once.

| Item | Rule for PanEuropean (all five countries) |
| :---- | :---- |
| Breach threshold | Notify unless the breach is unlikely to result in a risk to the rights and freedoms of individuals (Art. 33(1)); communicate to individuals where the risk is high (Art. 34). Every breach is recorded (Art. 33(5)) |
| Breach recipient | The HBDI as lead SA for cross-border processing, under the one-stop-shop (EDPB Guidelines 9/2022). A breach affecting only one branch's local processing may be a local case under Art. 56(2); General Counsel records that conclusion. The concerned SAs are not notified in parallel by default |
| Breach clock | Without undue delay and, where feasible, within 72 hours of becoming aware; phased notification permitted where information is not yet available. A processor notifies PanEuropean without undue delay (Art. 33(2)); where PanEuropean is processor for a group company, it notifies that controller in the same way and does not apply its own 72-hour clock |
| Data-subject access deadline | One month from receipt, extendable by two further months where necessary, with the customer informed within the first month (Art. 12(3)). Supervisory-authority practice on pausing the period while identity information requested under Art. 12(6) is awaited differs among the five countries; PanEuropean computes every deadline from receipt and relies on no pause (internal rule, Document 15) |
| Default transfer mechanism | India: no adequacy decision — standard contractual clauses (Commission Implementing Decision (EU) 2021/914) with transfer impact assessments (Art. 46). United States: adequacy decision for the EU-U.S. Data Privacy Framework (10 July 2023) applies only to certified recipients; Example AI Provider Inc. (fictional) is not certified (illustrative assumption), so standard contractual clauses with a TIA apply (currently on hold, Document 20). Certification is checked per flow on the official DPF List (Document 12, Section 4.1); the UK Extension and the Swiss-U.S. DPF are separate routes for UK and Swiss transfers. Art. 49 derogations are exceptional, interpreted restrictively and subject to the specific conditions of the derogation used (EDPB Guidelines 2/2018); internal policy (not a legal requirement): each use requires General Counsel's written justification, case by case |
| Data localisation | None under the GDPR. Banking secrecy, outsourcing and DORA contract rules (data location terms) apply as adjacent regimes (Section 5) |
| Representative / registration | No Art. 27 representative (EU-established); no general registration duty in the five countries; DPO contact communicated to the HBDI and, where national law requires, to the concerned SAs |
| DPO mandate | Group DPO designated for the bank (Art. 37(1)(b) and national rules in Section 4.1); one DPO for the group under Art. 37(2), easily accessible from each establishment |

### 4.3 Reference values for non-EU regimes

Not used: PanEuropean has no establishment in, and offers no services to, the United Kingdom, Switzerland or Canada. Transfers to India and the United States are governed by Document 12.

### 4.4 Other material particulars

| Jurisdiction | Particular |
| :---- | :---- |
| Germany | Contractual banking secrecy; electronic-marketing rules (Section 5); scoring rules in BDSG §31, whose compatibility with the GDPR was called into question by CJEU C-634/21 *SCHUFA* (7 December 2023) |
| France | Post-mortem data directives (Loi n° 78-17, Art. 85); banking secrecy (Code monétaire et financier, Art. L511-33); CNIL guidance on cookies and trackers |
| Italy | Code of conduct for private credit-information systems approved by the Garante; national register of objections for telemarketing |
| Spain | Credit information systems (LOPDGDD Art. 20); blocking of data before erasure (LOPDGDD Art. 32); video surveillance in branches (LOPDGDD Art. 22) |
| Poland | Banking secrecy and creditworthiness-data rules under the Banking Law; statutory check of the PESEL-reservation register before granting credit |

Age threshold in the app. The Art. 8 age matters only for information-society services offered to a child on the basis of consent — at PanEuropean, optional marketing features in the app. As an internal design choice, those features are switched off for every user under 16 in all five countries. Account opening and other contract-based services for minors follow national civil law on legal capacity and parental consent.

Biometric log-in. The app's biometric log-in stores the template only on the customer's device in all five countries, with a non-biometric alternative always available; the basis is explicit consent (Art. 9(2)(a)), which is freely given only because the alternative exists (EDPB Guidelines 05/2020).

National DPIA lists. The supervisory-authority lists under Art. 35(4) are checked for each country by the Privacy Officers; in any case, automated creditworthiness assessment is a DPIA case under Art. 35(3)(a), and biometric authentication meets at least two WP248 rev.01 criteria. The procedure is in the DPIA Methodology (Document 19).

## 5. Adjacent Regulatory Acts, Pending Changes and Interpretive Sources

| Act | Nature of regulation | Intersection with privacy | Owner of the separate track | Related document |
| :---- | :---- | :---- | :---- | :---- |
| DORA — Regulation (EU) 2022/2554 (applies since 17 January 2025), with Commission Delegated Regulations (EU) 2024/1772 and 2025/301 | ICT risk management, incident reporting, resilience testing and ICT third-party risk for financial entities — not a data protection law. Applies to PanEuropean as a whole, including its branches | A **major ICT-related incident** is classified under Delegated Regulation 2024/1772 and reported to the financial supervisor (ECB/BaFin) under Delegated Regulation 2025/301 and the related implementing standards: an initial notification within 4 hours of classifying the incident as major and no later than 24 hours from becoming aware of it; an intermediate report within 72 hours of the initial notification; a final report within one month of the latest updated intermediate report. The Regulation also contains rules for late classification and specific cases, which are applied from the legal text. This track is separate from the GDPR notification to the HBDI and is never merged with it. The Register of Information (Art. 28(3)) and contract terms (Art. 30) intersect with vendor due diligence for Example Cloud Services Pvt Ltd and Example AI Provider Inc. (both fictional). EuroCredit Bureau is an independent controller supplying data; whether it supports a critical or important function is a separate DORA test | ICT Risk Control (Head of ICT Risk Control) | Documents 3 (Sections 3.14–3.15), 14, 17 |
| NIS2 — Directive (EU) 2022/2555 | Cybersecurity risk management and incident notification | For PanEuropean, DORA applies as the sector-specific Union act, so its ICT risk management and incident-reporting provisions apply instead of the corresponding NIS2 provisions (NIS2 Art. 4). Non-financial group service companies assess their own national NIS2 status | CISO; group service companies | Document 3, Section 3.14 |
| AI Act — Regulation (EU) 2024/1689, as amended by the AI Omnibus (separate act, in force 27 July 2026) | Risk-tiered regulation of AI systems — not a data protection law | Credit scoring of natural persons is high-risk (Annex III, point 5(b)), with a carve-out for fraud detection; Annex III point 5(c) covers risk assessment and pricing for life and health insurance, relevant to the insurer of PPI products. Obligations for Annex III high-risk systems apply from **2 December 2027**; prohibited practices and other provisions follow their own dates and apply as scheduled; AI Act dates never suspend GDPR duties. As deployer, PanEuropean must ensure human oversight, log retention, information to affected persons and a fundamental rights impact assessment for credit scoring (Arts. 26, 27), and uses the information supplied under the AI Act for its DPIA (Art. 26(9); Document 19); affected persons gain a right to explanation (Art. 86). Because PanEuropean develops its scoring model, it also has provider duties. The financial supervisory authority acts as market-surveillance authority for high-risk AI used by credit institutions (Art. 74(6)). Under the GDPR, a credit score that a lender draws on strongly can itself be an Art. 22 decision (CJEU C-634/21, 7 December 2023), and the explanation of automated decisions must enable the person to understand the procedure and principles actually applied (CJEU C-203/22 *Dun & Bradstreet Austria*, 27 February 2025) | Model Risk and AI Governance; Processing Owner: Head of Credit Decisions | Documents 3 (Section 3.5), 19 |
| Consumer Credit Directive — Directive (EU) 2023/2225 (CCD2); national measures apply from 20 November 2026 (scheduled) | Consumer-credit conduct rules | Creditworthiness assessment may not use special-category data or data obtained from social networks; where the assessment involves automated processing, the consumer may request human intervention, a clear explanation and a review (Art. 18). Applies through national transposition in each of the five countries | Head of Credit Decisions; General Counsel | Documents 1 (Section 8), 19 |
| AML — Regulation (EU) 2024/1624 (AMLR, applies from 10 July 2027) and Directive (EU) 2024/1640 (AMLD6); national AML law until then | Customer due diligence, monitoring and reporting | Lawful basis (legal obligation) for KYC data; record retention — current national rule, e.g. Germany: 5 years under GwG §8(4), counted from the end of the calendar year in which the business relationship ended (other cases have their own trigger; branch-country AML law may differ); scheduled rule from 10 July 2027: AMLR Art. 77 (5 years, counted as that Article provides), not applied to the current national rule; prohibition on disclosing suspicious-activity reports restricts access rights | Head of Compliance | Documents 1 (Sections 7, 11), 11, 15 |
| ePrivacy Directive 2002/58/EC and national rules on cookies and electronic marketing — Germany: TDDDG §25 (terminal equipment) and UWG §7 (unsolicited communications); France: Loi n° 78-17, Art. 82; Italy: Codice Arts. 122 and 130; Spain: LSSI Arts. 21–22; Poland: Electronic Communications Law (2024) | Electronic-communications privacy and marketing rules | Consent for non-essential cookies and for electronic marketing, with national exceptions; these rules differ materially by country | Head of Marketing; Head of Digital Banking | Documents 1 (Section 14), 13 |
| PSD2 — Directive (EU) 2015/2366 as transposed; successor instruments proposed | Payment services, including third-party provider access to accounts | Third-party provider access at the customer's request is a separate data flow with its own lawful basis and RoPA entry; for entities under DORA, major ICT-related incidents, including payment-related ones, are reported under DORA | Head of Digital Banking | Documents 13, 21 |
| Banking secrecy (national law and contract in each of the five countries) | Confidentiality duties of credit institutions | Limits disclosure to third parties beyond the GDPR; relevant to vendor access, group sharing and authority requests | General Counsel | Documents 3 (Section 3.4), 17 |
| Credit-information rules (national law and codes of conduct; Section 4.4) | Rules on credit bureaus and credit-information systems | Conditions for reporting to and obtaining data from EuroCredit Bureau (independent controller) and for scoring | Head of Credit Decisions; General Counsel | Documents 1 (Sections 7–9), 17 |
| Data Act — Regulation (EU) 2023/2854 (applies from 12 September 2025) | Access to and use of data; switching between data-processing services | Headline: cloud-switching and interoperability rules for data-processing services used by the bank; the GDPR prevails for personal data | CIO; General Counsel | Document 17 |
| GDPR Procedural Regulation — Regulation (EU) 2025/2518 (adopted; applies from 2 April 2027) | Procedural rules for cross-border GDPR enforcement | Complaint handling and procedural rights of the parties in lead-SA cases involving the HBDI and the concerned SAs | General Counsel; Group DPO as contact point | Documents 14, 15 |
| Whistleblowing Directive — Directive (EU) 2019/1937 as transposed | Protection of reporting persons | Confidentiality of reporters' identities and personal data in reporting channels | Head of Compliance | Document 3 (Section 3.7) |
| PanEuropean Fair AI in Lending Commitment (a public, voluntary commitment by PanEuropean, 2026, based on an industry code) | Voluntary commitment — no legal sanction | Annual independent test of scoring models for unjustified discrimination, with aggregated results published; non-compliance carries material reputational risk, which is why it is included | Head of Credit Decisions | Document 1 (Section 3) |

This list is not exhaustive and does not replace a legal opinion on the applicability of a specific act.

### 5.1 Pending Changes (not law in force)

| Item | Stage and date | What would change | Action |
| :---- | :---- | :---- | :---- |
| Digital Omnibus (data, GDPR and cyber-reporting amendments) | Proposal. Council negotiating mandate agreed 21 October 2026; negotiations with the European Parliament pending. Not enacted | Among other things, changes to breach notification, including a longer deadline. The current GDPR rules, including the 72-hour clock, apply | Watch; impact assessment on adoption (General Counsel) |
| EDPB Guidelines 02/2026 on anonymisation | Public-consultation draft (8 July 2026); not final | Interpretation of anonymisation | Watch; Document 18 owner assesses on adoption |
| Payment-services reform (PSD3 / Payment Services Regulation) | Legislative proposals | Payment-services rules, including fraud prevention and data sharing | Watch (Head of Digital Banking) |
| Financial data access (FiDA) | Legislative proposal | Access to customer financial data by third parties | Watch (Head of Digital Banking) |

AI Omnibus: no longer pending — in force since 27 July 2026 and reflected in Section 5.

### 5.2 Sources and Standards Addressed in Other Documents

| Source | Source type | Why not addressed in substance here | Document where addressed |
| :---- | :---- | :---- | :---- |
| WP243 rev.01 (Article 29 Working Party guidelines on DPOs) | Interpretive guidance | Independence and tasks of the DPO (Arts. 37–39) | Privacy Role Competency Framework, Document 6 |
| WP248 rev.01 (Article 29 Working Party guidelines on DPIA) | Interpretive guidance | DPIA triage criteria and methodology | DPIA Methodology and Template, Document 19 |
| ISO/IEC 29134:2023 (privacy impact assessment) | Technical standard | Structure of the DPIA | DPIA Methodology and Template, Document 19 |
| ISO/IEC 27557:2022 (organisational privacy risk management); ISO/IEC 20889:2018 (de-identification techniques); ISO/IEC 27559:2022 (de-identification framework) | Technical standards | Methodological basis for privacy risk assessment and for assessing de-identification measures | Privacy Risk Assessment Methodology, Document 18 |
| ISO/IEC 27701 (privacy information management system) | Management-system standard | Programme controls; not a risk-calculation method | Standards crosswalk; Document 27 |
| EDPB Guidelines 01/2025 on pseudonymisation; CJEU C-413/23 P *EDPS v SRB* (relative approach to identifiability) | Interpretive guidance; case law | Legal status of pseudonymised data | Privacy Risk Assessment Methodology, Document 18 |
| ENISA methodology for assessing the severity of personal data breaches (2013) | Technical guidance of an EU agency | Incident severity classification | Data Breach Response Policy, Document 14 |
| EDPB Guidelines 9/2022 on personal data breach notification, version 2.0 | Interpretive guidance | Breach notification under the one-stop-shop; processor-to-controller escalation | Data Breach Response Policy, Document 14 |
| EDPB Recommendations 01/2020, version 2.0 | Interpretive guidance | Supplementary measures for transfers | TIA Methodology, Document 20 |
| CJEU C-311/18 *Schrems II* (16 July 2020) — "essentially equivalent" standard | Case law | Legal criterion for the transfer assessment | TIA Methodology, Document 20 |
| Commission Implementing Decision (EU) 2021/914, Clause 14 | Component of the SCC mechanism | Assessment of local laws and practices affecting compliance with the clauses | TIA Methodology, Document 20 |
| GDPR Art. 36 (prior consultation) | Procedural requirement | Arises as the G-36 step of the DPIA and TIA methodologies, not as a jurisdictional fact | DPIA Methodology (Document 19); TIA Methodology (Document 20) |
| GDPR Art. 30 (records of processing activities) | Legal requirement | Does not differ between the five countries | Record of Processing Activities (RoPA), Document 21 |

## 6. Review Process Upon a Change in Legislation

| Stage | Role | Timeframe |
| :---- | :---- | :---- |
| Identifying a change | Privacy Officers for the relevant country and General Counsel — Responsible; Chief Privacy Officer — Accountable; Group DPO — Consulted | Continuous |
| Assessing the impact on this matrix | General Counsel — Responsible for the legal assessment; Chief Privacy Officer — Accountable; Group DPO — Consulted | 10 business days from identification |
| Updating the matrix | Privacy Operations Lead | 5 business days after the assessment |
| Cascading notification | Privacy Operations Lead — notifies the owners of the Privacy Policy and Notice (Document 1), the Cross-Border Data Transfer Policy (Document 12), the Data Breach Response Policy (Document 14) and the TIA Methodology (Document 20) and, for adjacent regimes, the owners of Documents 3, 6, 17, 18, 19 and 21 | Immediately after the update |
| Adopting a material change | Management Board, on the Chief Privacy Officer's proposal, after the Group DPO's advice; Risk Committee of the Supervisory Board informed | Per the Policy Review Cycle, or before the date of application if earlier |

Example of a non-material change: the renaming of an authority with no change to any processing requirement — recorded by the Chief Privacy Officer without escalation. Example of a material change: a change to the Art. 8 age in one of the five countries, or the adoption of the Digital Omnibus — adopted by the Management Board, with the app settings and the Data Breach Response Policy updated before the date of application.

## 7. Relationship to Other Documents of the Model

This matrix is an input to:

* the Privacy Policy and Notice (Document 1) — authorities, rights and information duties in the five countries; CCD2 and AI Act information on automated credit decisions
* the Cross-Border Data Transfer Policy (Document 12) — India and the United States as recipient countries and the mechanism for each recipient
* the TIA Methodology (Document 20) — requirements specific to the five countries of data origin
* the Data Breach Response Policy (Document 14) — notification to the HBDI as lead SA within 72 hours of awareness, and the separate DORA track to the ECB/BaFin
* the Interface and Integration Model (Document 3, Sections 3.5, 3.14 and 3.15) — AI Act, DORA and outsourcing interfaces
* the Vendor and Third-Party Privacy Risk Policy (Document 17) — DORA ICT third-party requirements for Example Cloud Services Pvt Ltd and Example AI Provider Inc.; EuroCredit Bureau as an independent controller
* the Privacy Role Competency Framework (Document 6) — DPO mandates (BDSG §38; LOPDGDD Art. 34)
* the Privacy Risk Assessment Methodology (Document 18) — legal facts used by G-L and track (b), and the standards in Section 5.2
* the DPIA Methodology and Template (Document 19) — national Art. 35(4) lists and the FRIA for credit scoring
* the Record of Processing Activities (Document 21) — the Art. 30 record

## 8. Review and Amendment

This document is reviewed under the continuous-improvement principle (Charter, Section 7) and the Policy Review Cycle (Document 29), and immediately upon a change in the law of any of the five countries or in EU law (Section 6). Amendments are prepared by the Chief Privacy Officer, with General Counsel's assessment and the Group DPO's advice, and adopted by the Management Board; non-material changes are recorded by the Chief Privacy Officer.

## 9. Approval

Version 3.0 of this document was adopted by the Management Board of PanEuropean Bank AG on 20 October 2026, on the proposal of the Chief Privacy Officer and after the Group DPO's advice, and takes effect on 10 November 2026 (scheduled); the Risk Committee of the Supervisory Board was informed on 23 October 2026. Document owner: Chief Privacy Officer.

# Normative Basis and References

**EU law**
* Regulation (EU) 2016/679 (GDPR): Arts. 3, 4(16), 4(22), 8, 9, 12(3), 22, 27, 30, 33–37, 44–49, 56, 60, 88.
* Regulation (EU) 2025/2518 (procedural rules for GDPR enforcement) — adopted; applies from 2 April 2027.
* Regulation (EU) 2022/2554 (DORA); Commission Delegated Regulation (EU) 2024/1772 (classification of ICT-related incidents); Commission Delegated Regulation (EU) 2025/301 (content and time limits of incident reports) and the related implementing technical standards (EBA, joint technical standards on major incident reporting).
* Directive (EU) 2022/2555 (NIS2), Art. 4.
* Regulation (EU) 2024/1689 (AI Act), as amended by the AI Omnibus (in force 27 July 2026; European Commission, "AI Omnibus enters into force"): Annex III points 5(b) and 5(c); Arts. 26, 27, 74(6), 86.
* Directive (EU) 2023/2225 (CCD2), Art. 18.
* Regulation (EU) 2024/1624 (AMLR), Art. 77; Directive (EU) 2024/1640 (AMLD6).
* Directive 2002/58/EC (ePrivacy); Directive (EU) 2015/2366 (PSD2); Regulation (EU) 2023/2854 (Data Act); Directive (EU) 2019/1937 (whistleblowing).
* Commission Implementing Decision (EU) 2021/914 (standard contractual clauses); EU-U.S. Data Privacy Framework adequacy decision of 10 July 2023, upheld by the General Court in T-553/23 *Latombe* (September 2025); European Commission register of adequacy decisions.

**Case law**
* CJEU C-34/21 *Hauptpersonalrat der Lehrerinnen und Lehrer* (30 March 2023); C-634/21 *SCHUFA Holding (Scoring)* (7 December 2023); C-203/22 *Dun & Bradstreet Austria* (27 February 2025); C-311/18 *Schrems II* (16 July 2020); C-413/23 P *EDPS v SRB*.

**Guidance**
* EDPB Guidelines 9/2022 on personal data breach notification, version 2.0 (28 March 2023); EDPB Guidelines 05/2020 on consent; EDPB Guidelines 05/2021 on the interplay between Art. 3 and Chapter V, version 2.0; EDPB Guidelines 2/2018 on derogations of Art. 49; EDPB Guidelines 01/2025 on pseudonymisation; EDPB Guidelines 02/2026 on anonymisation (public-consultation draft, 8 July 2026); Council of the EU press release on the Digital Omnibus negotiating mandate (21 October 2026).

**National law (Part B)**
* Germany: Money Laundering Act (GwG) §8(4) with §10(3) sentence 1 no. 1 (AML record retention and its start); BDSG §§22, 26, 31, 38; Works Constitution Act (BetrVG) §87(1) no. 6; TDDDG §25; UWG §7. France: Loi n° 78-17 (Arts. 45, 82, 85); Code monétaire et financier, Art. L511-33. Italy: D.Lgs. 196/2003 as amended by D.Lgs. 101/2018 (Arts. 2-quinquies, 2-septies, 122, 130). Spain: Ley Orgánica 3/2018 (Arts. 7, 20, 22, 32, 34); LSSI (Arts. 21–22). Poland: Act of 10 May 2018 on the protection of personal data; Electronic Communications Law (2024).

**Canada (Part A, Section 3.1)**
* Personal Information Protection and Electronic Documents Act (PIPEDA), including the breach provisions and the Breach of Security Safeguards Regulations (SOR/2018-64); Act respecting the protection of personal information in the private sector (Québec, P-39.1); Bill C-36, *Protecting Privacy and Consumer Data Act* (45th Parliament, 1st session; introduced 15 June 2026; at second reading).

# International Adaptation

> **Guidance.** The GDPR is the baseline of this matrix. The rows of Section 4.3 give the headline values for the UK, Switzerland, PIPEDA and Québec; the Canadian applicability map is in Section 3.1 and is cited by all other documents. This document does not claim compliance with any jurisdiction's law.

* **United Kingdom (headline).** UK GDPR and the DPA 2018, as amended by the Data (Use and Access) Act 2025, with phased commencement: record which provisions have commenced on the date of each review. The ICO is the authority; a UK representative and the data protection fee are recorded in Section 3 where they apply.
* **Switzerland (headline).** The revFADP (in force since 1 September 2023) applies under its own territorial rule to effects in Switzerland; the FDPIC is the authority; breach notification is risk-based ("as soon as possible" where a high risk is likely); a Swiss representative may be required for foreign controllers.
* **Canada.** Apply the applicability map in Section 3.1: PIPEDA for commercial activities outside provinces with substantially similar laws and for inter-provincial and international flows and federal works; Québec P-39.1 for intra-provincial activities in Québec (person in charge; privacy impact assessment before communicating personal information outside Québec; confidentiality-incident register; express consent for sensitive information; information on decisions based exclusively on automated processing). Alberta and British Columbia PIPA and the public and health sectors are out-of-scope extensions. Bill C-36 is a proposal (Section 5.1 of Part A); PIPEDA remains in force. The OPC/OIPC guidance *Getting Accountability Right with a Privacy Management Program* is the Canadian programme reference.

# Document History (PGF)

| Release | Date | Summary |
| :---- | :---- | :---- |
| 1.0.0-rc.1 | 2026-10-26 | Canonical English Markdown; changes from internal ver.2: territorial-scope principle rewritten (Art. 3(1) for the EU-established bank; Art. 3(2) only for non-EU organisations; CRD passporting wording corrected); one-stop-shop roles recorded (HBDI lead SA; CNIL, Garante, AEPD and Prezes UODO concerned SAs) and breach notification routed to the lead SA per EDPB Guidelines 9/2022; GDPR Procedural Regulation (EU) 2025/2518 added (applies 2 April 2027); DORA recorded as a bank-wide regime with the term "major ICT-related incident", classification under Delegated Regulation 2024/1772 and reporting under Delegated Regulation 2025/301 with points of reference; AI Act updated for the AI Omnibus (in force 27 July 2026; Annex III from 2 December 2027) with deployer duties, FRIA, Art. 86 and Art. 74(6), and SCHUFA condition and *Dun & Bradstreet* added; German employee-data position updated after C-34/21 (works-council co-determination, not consent); Spain biometrics kept generic; ePrivacy and national marketing rules, CCD2, AMLR/AMLD6, banking secrecy, credit-information rules, NIS2 (lex specialis note), Data Act, PSD2 and whistleblowing added; pending-changes block separated from law in force (Digital Omnibus, Bill C-36, draft EDPB guidance); template internationalised (diversified examples replacing 152-FZ, PIPL and an unspecified PDPL; new columns for breach threshold, recipient and clock, access deadline, representative and registration, localisation and privacy-officer mandate; Art. 8 age separated from contractual capacity; reference values for UK, Switzerland, PIPEDA and Québec); Canadian applicability map stated once (Section 3.1); "strictest requirement" reframed as a design choice for cumulative requirements; ISO/IEC 27701 pointer corrected (ISO/IEC 27557, 20889, 27559 added); RoPA "not yet developed" remark deleted; roles aligned with the RACI role model (EPPO owner; Executive Management adopts); fictional providers used; example dates shifted by −12 months. Integration pass: Art. 12(6) pause practice recorded (Part B: no pause relied on, internal rule); AI Act Art. 26(9) DPIA link added |
| 1.0.0-rc.2 | 2026-10-28 | Author-approved publication direction; named PAMOLA implementation examples with tool-neutral templates; direct integrated-score mapping without automatic per-metric risk-tier overrides; observations, DPO dissent and the authorised business decision recorded separately from legal/release conditions. |
| 1.0.0 | 2026-10-28 | First publication package; substantive method unchanged from the rc.2 freeze; rights holder REALM INVEO confirmed and documentation licence CC BY 4.0 issued. |
