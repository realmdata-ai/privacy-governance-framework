---
title: "PGF Standards and Regulatory Crosswalk"
document_id: PGF-XWALK
release_version: 1.0.0-rc.1
status: release-candidate
authors: ["Alexey Neyman", "Val Khvatov"]
regulatory_reference_date: 2026-10-26
---

# PGF Standards and Regulatory Crosswalk

## How to read this crosswalk

This is a **conceptual mapping**, not a statement of conformity. It shows where a PGF document addresses the subject matter of an external requirement or outcome. It does **not** claim that adopting PGF makes an organisation compliant with any law, or conformant with any standard or framework, or certifiable under any of them. Whether a control works can only be shown by the evidence an adopting organisation produces.

| Column | Meaning |
|---|---|
| Source / version | The exact instrument or framework version mapped |
| Requirement / outcome | Article, principle, category or report topic |
| PGF location | Document (and section topic) where the subject is addressed |
| Evidence an adopter would hold | The artefact that would demonstrate operation |
| Coverage | **addressed** (the topic is handled in substance by the template) · **partial** (handled in part; see gap) · **interface** (handled by delegating to another function, e.g. InfoSec) · **not assessed** |
| Gap / note | What PGF does not cover, or what the adopter must add |

**Checked:** 26 October 2026, against the sources listed in §7. Where a clause-level text could not be read, the row maps at topic level and says so.

---

## 1. NIST Privacy Framework 1.0 (final, January 2020) — category level

NIST PF 1.1 is an **Initial Public Draft**. Its identifiers are **not** mixed into this table; see §1.1. Subcategory-level mapping (e.g. ID.IM-P1…P8) is not attempted in this release.

| Function | Category (PF 1.0 ID) | PGF location | Evidence an adopter would hold | Coverage | Gap / note |
|---|---|---|---|---|---|
| Identify-P | Inventory and Mapping (ID.IM-P) | Doc 21 RoPA; Doc 23 Data Inventory and Data Flow Maps; Doc 10 Data Classification | RoPA records; catalogue privacy metadata; flow maps incl. jurisdictions and remote access | addressed | Inventory relies on the organisation's corporate data catalogue (overlay design) |
| Identify-P | Business Environment (ID.BE-P) | Doc 2 Charter (mandate, objectives); Doc 3 Interface and Integration Model; Doc 7 Regulatory Applicability Matrix | Approved Charter; interface map; applicability matrix | partial | Stakeholder/individual expectations are addressed through the DPIA (Doc 19), not as a separate analysis |
| Identify-P | Risk Assessment (ID.RA-P) | Doc 18 Risk Assessment Methodology; Doc 19 DPIA; Doc 20 TIA; Doc 22 Privacy Risk Register | DPIA/TIA reports; risk calculations with evidence; register entries | addressed | Calculation core is not empirically validated (see Overview, Limitations) |
| Identify-P | Data Processing Ecosystem Risk Management (ID.DE-P) | Doc 17 Vendor and Third-Party Privacy Risk Policy; Doc 12 Cross-Border Transfer Policy | Due-diligence files; Art. 28 contracts; sub-processor list; TIAs | addressed | — |
| Govern-P | Governance Policies, Processes and Procedures (GV.PO-P) | Doc 1 Policy and notice; Doc 2 Charter; Doc 5 RACI; Doc 6 Competency Framework; Doc 7 | Adopted policies; RACI; role mandates; legal requirements register (Doc 7) | addressed | — |
| Govern-P | Risk Management Strategy (GV.RM-P) | Doc 8 Risk Appetite Statement; Doc 3 (ERM alignment) | Board-level appetite statement; acceptance authority table | addressed | Appetite operates only after the legal compliance gate (G-L) |
| Govern-P | Awareness and Training (GV.AT-P) | Doc 30 Awareness and Training Programme; Doc 6 | Training records; completion metrics | addressed | — |
| Govern-P | Monitoring and Review (GV.MT-P) | Doc 27 Audit and Monitoring Programme; Doc 28 Metrics Dashboard; Doc 29 Policy Review Cycle; Doc 31 Governance Reporting | Monitoring plan; independent audit opinion; dashboard; review log; board reports | addressed | Independent assurance by Internal Audit; DPO monitoring under Art. 39 is separate |
| Control-P | Data Processing Policies, Processes and Procedures (CT.PO-P) | Docs 11, 13, 15, 16 | Retention schedule; consent records; rights-request log; PbD gate records | addressed | — |
| Control-P | Data Processing Management (CT.DM-P) | Doc 15 Data Subject Rights; Doc 11 Retention and Disposal; Doc 13 Consent | Request handling evidence; deletion and disposal logs; propagation to processors and derived data | partial | Technical implementation of deletion and propagation is the adopter's |
| Control-P | Disassociated Processing (CT.DP-P) | Doc 18 (PET assessment module); Doc 16; Doc 9 | PET assessments with per-metric results; DP parameters and accounting | partial | Thematic depth does not by itself prove control effectiveness; empirical validation is the adopter's |
| Communicate-P | Communication Policies, Processes and Procedures (CM.PO-P) | Doc 1 (external notice part); Doc 31 | Published notice; material-change communications | partial | Complaint handling is covered at the interface level only |
| Communicate-P | Data Processing Awareness (CM.AW-P) | Doc 1; Doc 15; Doc 14 (notification of individuals) | Notices; ADM explanations; breach notifications | partial | — |
| Protect-P | All categories (PR.PO-P, PR.AC-P, PR.DS-P, PR.MA-P, PR.PT-P) | Doc 3 (InfoSec interface); Doc 14 | InfoSec policies and controls (outside PGF) | interface | PGF deliberately relies on the organisation's security programme (e.g. aligned to NIST CSF 2.0) |

### 1.1. NIST PF 1.1 (Initial Public Draft, April 2025)

No identifier-level mapping is made. The draft realigns with CSF 2.0 and adds AI and privacy content. Re-map when a final version is published.

### 1.2. Other NIST publications used as method references (not conformance claims)

- NISTIR 8062: privacy engineering objectives; problematic data actions — Doc 18.
- NIST SP 800-226 (final, March 2025): differential privacy — Doc 18 PET module; Doc 9.
- NIST SP 800-188: de-identifying government datasets — Doc 18.

---

## 2. EU — GDPR and EDPB (selected articles)

| GDPR provision | Subject | PGF location | Evidence | Coverage | Note |
|---|---|---|---|---|---|
| Art. 5, 24 | Principles; controller accountability | Doc 1; Doc 2; Doc 5 | Adopted policy; RACI; accountability records | addressed | |
| Art. 6, 9, 10 | Lawful basis; special categories; criminal-offence data | Doc 1; Doc 10; Doc 21; legal compliance gate (G-L) in Docs 8, 18, 19, 24 | Lawful-basis assessment per RoPA entry; Art. 9/10 condition | addressed | G-L failure cannot be cured by risk acceptance |
| Art. 7, 8 | Consent; children | Doc 13; Doc 7 (age-of-consent variation) | Consent records; withdrawal handling | addressed | |
| Art. 12–14 | Transparency | Doc 1 (external notice part) | Notice versions | addressed | |
| Art. 15–22 | Data subject rights; automated decisions | Doc 15; Doc 19 (Art. 22 checks) | Request log; restriction grounds; ADM safeguards | addressed | |
| Art. 25 | Data protection by design and by default | Doc 16; Doc 9 | Design-gate records; default settings evidence | addressed | |
| Art. 26, 28 | Joint controllers; processors | Doc 17 | Art. 26 arrangement; Art. 28(3) contract checklist | addressed | |
| Art. 30 | Records of processing | Doc 21 | RoPA | addressed | |
| Art. 32 | Security of processing | Doc 3 (InfoSec interface) | InfoSec controls | interface | |
| Art. 33, 34 | Breach notification and documentation | Doc 14 | Breach register (all breaches); notifications | addressed | Separate from DORA reporting |
| Art. 35, 36 | DPIA; prior consultation | Doc 19; Doc 18; Doc 8; Doc 24 | DPIA reports with DPO advice; Art. 36 consultation file | addressed | |
| Art. 37–39 | DPO | Doc 2; Doc 4; Doc 5; Doc 6; Doc 26 | Designation; independence safeguards; DPO reports | addressed | |
| Art. 44–49 | Transfers | Doc 12; Doc 20 | Transfer register; TIAs; SCCs | addressed | |

**EDPB / WP29 guidance used:**
- WP248 rev.01 (DPIA);
- WP243 rev.01 (DPO);
- Guidelines 07/2020 (controller and processor);
- Guidelines 05/2020 (consent);
- Guidelines 01/2022 (right of access);
- Guidelines 9/2022 (breach notification);
- Guidelines 05/2021 (Art. 3 and Chapter V interplay);
- Recommendations 01/2020 (supplementary measures);
- Guidelines 4/2019 (Art. 25);
- Guidelines 01/2025 (pseudonymisation);
- **Guidelines 02/2026 (anonymisation) — public-consultation draft**;
- WP29 Opinion 05/2014 (WP216, anonymisation techniques);
- the 2023 Coordinated Enforcement Framework report on DPOs.

These are guidance, not law.

**Sector and adjacent EU instruments** (interfaces only, not full programmes):
- **DORA** (Reg. (EU) 2022/2554; incident classification under Delegated Reg. (EU) 2024/1772, reporting under Delegated Reg. (EU) 2025/301) — Docs 3, 14, 17.
- **AI Act** (Reg. (EU) 2024/1689, as amended by the AI Omnibus in force 27 July 2026) — Docs 3, 7, 19.
- **NIS2** — Doc 3.
- **Data/GDPR Omnibus** — a proposal only (Council mandate 21 October 2026). Not applied.

---

## 3. ENISA (engineering guidance; not a certification scheme)

| Report | Topic | PGF location | Coverage |
|---|---|---|---|
| Pseudonymisation techniques and best practices (2019) | Techniques, threat models, attacks on pseudonymisation | Doc 18 (PET module; data-state definitions); Doc 16; Doc 9 | partial |
| Data Protection Engineering (2022) | Engineering approaches linked to design/default and DPIA | Doc 16; Doc 9; Doc 18 | partial |
| Recommendations for a methodology of the assessment of severity of personal data breaches (2013) | Breach severity factors | Doc 14 | partial |

---

## 4. Canada — topic-level mapping

**Applicability.** PIPEDA applies to private-sector organisations in the course of commercial activities, and to federal works, undertakings and businesses. Within a province whose private-sector law has been declared substantially similar (Québec, Alberta, British Columbia), that law applies to intra-provincial collection, use and disclosure. PIPEDA continues to apply to inter-provincial and international flows.

**Out of scope for this release (named extensions):**
- Alberta and BC PIPA;
- public-sector and health-sector statutes;
- Bill C-36 (*Protecting Privacy and Consumer Data Act*) — introduced 15 June 2026; a proposal, not law.

A Canadian Privacy Officer is **not** an EU statutory DPO.

### 4.1. OPC / OIPC Alberta / OIPC BC — *Getting Accountability Right with a Privacy Management Program* (2012)

| Programme element | PGF location | Evidence an adopter would hold | Coverage |
|---|---|---|---|
| Organisational commitment: senior management support | Doc 2 Charter; Doc 31 Governance Reporting | Charter adoption; board reporting | addressed |
| Designated Privacy Officer, with a mandate and resources | Doc 2; Doc 4; Doc 6 (Canadian Privacy Officer note) | Appointment; role profile | addressed |
| Privacy office / function | Doc 4 Organisational Design; Doc 26 Staffing Model | Organisation design; staffing | addressed |
| Reporting mechanisms | Doc 31; Doc 28 | Reports; dashboards | addressed |
| Personal information inventory | Doc 21; Doc 23 | RoPA / inventory | addressed |
| Policies: collection, use and disclosure; access and correction; retention and disposal; security; complaints | Docs 1, 11, 13, 15; Doc 3 (security) | Adopted policies | partial (complaints handled at interface level) |
| Risk assessment tools (incl. privacy impact assessment) | Docs 18, 19, 20 | PIAs / DPIAs / TIAs | addressed |
| Training and education | Doc 30 | Training records | addressed |
| Breach and incident management | Doc 14 | Breach records; reports | addressed |
| Service-provider management | Doc 17 | Contracts; oversight | addressed |
| External communication | Doc 1 (notice part) | Published notice | addressed |
| Oversight and review plan; assessment and revision of programme controls | Docs 27, 29 | Monitoring plan; review log | addressed |

### 4.2. PIPEDA (Schedule 1 principles; breach provisions)

| Requirement | PGF location | Coverage | Note |
|---|---|---|---|
| Principle 4.1 Accountability | Docs 2, 5 | addressed | Includes accountability for information transferred to service providers (Doc 17) |
| 4.2 Identifying purposes; 4.4 Limiting collection; 4.5 Limiting use, disclosure and retention | Docs 1, 11, 21 | addressed | |
| 4.3 Consent (meaningful consent) | Doc 13 | partial | GDPR lawful bases do not transpose to PIPEDA. Consent remains the primary model, subject to the Act's exceptions |
| 4.7 Safeguards | Doc 3 (interface) | interface | |
| 4.8 Openness | Doc 1 | addressed | |
| 4.9 Individual access (30-day response, extendable as the Act provides) | Doc 15 | partial | Canadian variant in International adaptation box |
| 4.10 Challenging compliance | Doc 15; Doc 1 | partial | |
| Breach of security safeguards: real risk of significant harm → report to OPC, notify individuals as soon as feasible; records of **every** breach kept for 24 months | Doc 14 | addressed | Do not import the GDPR 72-hour clock |

### 4.3. Québec — Act respecting the protection of personal information in the private sector (P-39.1, as amended by Law 25)

**Mapped at topic level.** Clause numbers are intentionally not asserted until checked against the consolidated official text.

| Topic | PGF location | Coverage |
|---|---|---|
| Person in charge of the protection of personal information (default: the person with the highest authority; delegable) | Docs 2, 4, 6 | addressed |
| Governance policies and practices, published in plain terms | Docs 1, 2 | addressed |
| Privacy impact assessment for information-system projects, and before communicating personal information outside Québec | Docs 19, 20 | partial |
| Confidentiality incidents: notification of the Commission d'accès à l'information and the persons concerned where there is a risk of serious injury; register of all incidents | Doc 14 | addressed |
| Consent (express consent for sensitive information); privacy by default for technological products and services | Docs 13, 16 | partial |
| Decisions based exclusively on automated processing: information and review | Docs 15, 19 | partial |
| Anonymisation: criteria and re-assessment under the applicable regulation | Doc 18 | partial |

---

## 5. ISO/IEC (bibliographic pointers only)

Bibliographic pointers only: ISO/IEC 27701:2025 (privacy information management systems; standalone edition), 29100, 29134, 27557, 27559, 20889, ISO 31000.

No clause-level mapping is made. Clause texts were not reviewed for this release, and the presence of a reference does not imply conformity.

---

## 6. Known limitations of this crosswalk

- Mapping at category or topic level hides gaps that only appear at subcategory or clause level.
- Coverage marks describe what the **template** addresses, not what an adopter has implemented.
- UK (UK GDPR / DUAA 2025) and Swiss (revFADP) differences appear only as headline notes in the International adaptation boxes. They are not mapped here.

## 7. Sources checked (26 October 2026)

For a maintained, dated catalogue of official sources with stable IDs, legal force and review dates, see **Curated privacy references** ([`../references/README.md`](../references/README.md)). The list below records only the sources checked for this crosswalk.


- NIST Privacy Framework page and PF 1.0 text: https://www.nist.gov/privacy-framework ; https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.01162020.pdf
- NIST SP 800-226 final: https://csrc.nist.gov/pubs/sp/800/226/final
- EDPB Guidelines 02/2026 on anonymisation (consultation): https://www.edpb.europa.eu/documents/guideline/guidelines-022026-on-anonymisation_en
- EDPB CEF report on DPOs (2024): https://www.edpb.europa.eu/system/files/2024-01/edpb_report_20240116_cef_dpo_en.pdf
- ENISA Pseudonymisation (2019): https://www.enisa.europa.eu/publications/pseudonymisation-techniques-and-best-practices ; Data Protection Engineering (2022): https://www.enisa.europa.eu/publications/data-protection-engineering
- OPC/OIPC accountability guidance: https://www.priv.gc.ca/en/privacy-topics/privacy-laws-in-canada/the-personal-information-protection-and-electronic-documents-act-pipeda/pipeda-compliance-help/pipeda-compliance-and-training-tools/gl_acc_201204/
- OPC breach guidance: https://www.priv.gc.ca/en/privacy-topics/privacy-for-businesses/privacy-breaches-at-your-business/gd_pb_201810/
- Québec P-39.1: https://www.legisquebec.gouv.qc.ca/fr/document/lc/p-39.1 ; CAI: https://www.cai.gouv.qc.ca/protection-renseignements-personnels/sujets-et-domaines-dinteret/principaux-changements-loi-25
- Bill C-36: https://www.parl.ca/legisinfo/en/bill/45-1/c-36
- Council mandate on the Digital Omnibus (21 Oct 2026): https://www.consilium.europa.eu/en/press/press-releases/2026/10/21/digital-rulebook-council-agrees-position-to-simplify-data-protection-privacy-and-cyber-reporting-rules/
- AI Omnibus entry into force: https://digital-strategy.ec.europa.eu/en/news/ai-omnibus-enters-force
- EBA DORA incident reporting standards: https://www.eba.europa.eu/activities/single-rulebook/regulatory-activities/operational-resilience/joint-technical-standards-major-incident-reporting
