---
title: "PGF Glossary"
document_id: PGF-GLOSSARY
release_version: 1.0.0-rc.1
status: release-candidate
authors: ["Alexey Neyman", "Val Khvatov"]
regulatory_reference_date: 2026-10-26
---

# PGF Glossary

This glossary is the authoritative list of terms used across the Privacy Governance Framework (PGF). Individual documents may keep short local glossaries, but those must not contradict it. Statutory terms follow the GDPR unless stated otherwise.

## Roles and bodies

| Term | Definition |
|---|---|
| **Controller** | The natural or legal person that, alone or jointly, determines the purposes and means of processing (GDPR Art. 4(7)). In PGF the controller is the organisation as a legal entity, not one of its bodies. It is ultimately accountable for compliance (Art. 5(2), 24). |
| **Executive Management** | The body that manages the organisation, e.g. a management board or executive committee. It adopts privacy policies, unless the Governing Body has reserved a specific adoption. It takes management decisions, including the acceptance of residual risk above delegated limits. |
| **Governing Body** | The body that oversees Executive Management, e.g. a board of directors or a supervisory board, together with its committees (Risk, Audit). It oversees the programme and receives assurance. It may hold reserved consent matters. It does not run the privacy programme. |
| **Executive Privacy Programme Owner (EPPO)** | The executive accountable for running the privacy programme: policies, processes, metrics, training and reporting. May be a Chief Privacy Officer, a Head of Privacy or another designated executive. No separate new post is required. The EPPO is not the DPO. |
| **Processing Owner** | The business owner of a processing activity. Within the delegation granted by the controller, takes authorised management decisions about that activity, including the acceptance of residual risk up to the delegated tier. |
| **Data Protection Officer (DPO)** | The statutory role under GDPR Arts. 37–39. The DPO informs and advises, monitors compliance (including compliance audits it organises), gives advice on DPIAs, and cooperates with and is the contact point for the supervisory authority. The DPO acts independently, reports directly to the highest management level, and is accountable for the quality of its own tasks. The DPO does not authorise processing, accept risk on the controller's behalf or determine purposes and means. |
| **Privacy Officer (Canada)** | The individual accountable for compliance under PIPEDA Principle 4.1, or the person in charge of the protection of personal information under Québec's private-sector Act. Not equivalent to an EU statutory DPO. |
| **Privacy Operations Lead** | Runs day-to-day privacy operations. Owns Risk Calculation Projects (Document 18). |
| **Data Protection Coordinator (DPC)** | An Execution-tier role inside a business unit that ensures the operational application of the model in that unit. A communication channel between the business unit and the privacy function; no decision authority (Documents 4 and 5). |
| **Governance tiers** | Oversight / Management / Execution — the three tiers of the privacy function (Document 4, Section 4). The DPO and the Processing Owner sit outside the tiers. |
| **Processing Owner mandate** | The designation, by Executive Management on the EPPO's proposal (process G9), of the holder of the Processing Owner role and its delegated tier. A business line cannot designate itself; the current holders are recorded in Document 25, Section 10. |
| **Privacy Risk Committee** | A management-level committee chaired by the EPPO or a member of Executive Management. The DPO attends as an independent, non-voting adviser. |
| **Independent Internal Audit** | The third line. Gives the independent assurance opinion on the privacy programme and reports functionally to the Governing Body's Audit Committee. |
| **Competent supervisory authority (SA)** | The GDPR data protection authority competent for the processing. For cross-border processing this is the lead SA (Art. 56) together with the concerned SAs. Never a financial supervisor. |
| **Financial supervisor** | An authority supervising financial entities (e.g. BaFin, the ECB). It receives DORA ICT-incident reports and handles prudential matters. Not a GDPR SA. |

## Gates and decisions

| Term | Definition |
|---|---|
| **Legal compliance gate (G-L)** | The check, run before any risk decision, of: lawful basis; Art. 9/10 conditions; purpose compatibility; transparency; Art. 22 permissibility and safeguards; transfer tool and TIA outcome; statutory deadlines. A failure means stop or redesign. It cannot be cured by risk acceptance. |
| **DPIA triage (G-DPIA)** | The determination whether a DPIA is required under: Art. 35(1) and (3); the supervisory-authority lists under Art. 35(4); the nine criteria of WP248 rev.01. |
| **Prior consultation (G-36)** | Consultation of the competent SA before processing starts, where a DPIA indicates that processing would still result in a high risk to the rights and freedoms of natural persons after the controller's measures (Art. 36). |
| **Transfer equivalence (G-TIA)** | The requirement that a transfer outside the EEA ensures essentially equivalent protection, taking account of the laws and practices of the destination. If it cannot be ensured, the transfer does not start or is suspended. |
| **Residual risk** | The risk to the rights and freedoms of individuals remaining after measures, rated on the PGF tiers Low, Medium, High and Critical (Document 8). |
| **Organisational consequences** | Regulatory, financial, operational and reputational consequences for the organisation. Assessed on a separate track. Never offsets risk to individuals. |
| **Conditional acceptance** | Acceptance of a Medium or High residual risk subject to conditions and an expiry date. The risk is re-assessed on expiry. |

## Data states

| Term | Definition |
|---|---|
| **Personal data** | Any information relating to an identified or identifiable natural person (Art. 4(1)). |
| **Pseudonymised data** | Data processed so that it can no longer be attributed to a specific person without additional information kept separately (Art. 4(5)). It remains personal data for anyone who can attribute it with means reasonably likely to be used. Pseudonymisation is not an anonymisation technique. |
| **Anonymous information** | Information that does not relate to an identified or identifiable person, taking account of all the means reasonably likely to be used by the controller or by any other person (Recital 26). It is a contextual legal conclusion, recorded by the controller on documented evidence and re-assessed periodically. No metric threshold creates a safe harbour. |
| **Synthetic data** | Data generated by a model. A generation method, not a legal status. |
| **Encrypted data** | Data protected by encryption. A security measure; the data remains personal. |
| **Federated learning / secure computation** | Processing architectures that limit data movement. They do not by themselves change the legal status of the data or exempt a flow from Chapter V. |

## Incidents

| Term | Definition |
|---|---|
| **Security event** | Any information-security event, handled by InfoSec. |
| **Personal data breach** | A breach of security leading to the accidental or unlawful destruction, loss, alteration, unauthorised disclosure of, or access to, personal data (Art. 4(12)). There is no harm threshold for whether a breach exists. Every breach is documented (Art. 33(5)). Risk determines only whether the SA and individuals must be notified. |
| **Awareness** | The point at which the controller has a reasonable degree of certainty that a security incident has occurred that has led to personal data being compromised (EDPB Guidelines 9/2022). The 72-hour clock of Art. 33(1) runs from awareness (Document 14). |
| **Breach record** | The record of every personal data breach required by Art. 33(5): facts, effects, remedial action and the reasoning for the notification decisions. A statutory record, kept independently and linked to other registers by identifier (Document 14). |
| **Privacy incident** | A wider internal category that includes unlawful processing without a security breach. |
| **Major ICT-related incident** | A DORA category for financial entities, classified under Delegated Regulation (EU) 2024/1772 and reported to the financial supervisor. Separate from GDPR breach notification. |
| **Breach of security safeguards (Canada)** | A PIPEDA concept. Reportable to the OPC, with notification of individuals, where it creates a real risk of significant harm. Records of every breach are kept for 24 months. |
| **Confidentiality incident (Québec)** | A concept under the Québec private-sector Act. Notifiable where there is a risk of serious injury. All incidents are recorded in a register. |

## Privacy-enhancing technology (PET) terms

| Term | Definition |
|---|---|
| **PET assessment module** | The specialised part of Document 18 for de-identified, synthetic and aggregate releases. Individual metric results are retained, and failure gates apply. |
| **Differential privacy (DP)** | A formal property of a randomised mechanism, parameterised by ε (and, for approximate DP, δ). Statements must specify the privacy unit, the adjacency relation, the mechanism and accountant, and composition across releases. |
| **WP29 anonymisation criteria** | Singling out, linkability and inference (Article 29 Working Party, Opinion 05/2014, WP216). |
| **Risk Calculation Project** | A versioned, documented configuration of the Document 18 calculation for a class of processing. |
| **Evidence pack** | The documented record of a risk calculation and decision: inputs, results, opinions, decision, conditions. Identifier format `EVP-YYYY-NNNN`. Retained according to Document 11. |

## Process model

| Term | Definition |
|---|---|
| **Process groups** | Governing (G1–G9), core (C1–C5) and supporting (S1–S9) processes (Document 24). The model is inspired by the APQC Process Classification Framework hierarchy; it does not claim PCF levels or identifiers. |
| **Process owner** | The role that is Accountable ("A") for a process or sub-process in the RACI Matrix (Document 5). There is no separate "owner badge"; where a process is split into sub-rows with different Accountable roles (for example S7.1–S7.5), each sub-row has its own owner (Documents 24 and 25). |
| **Sub-process** | A part of a process with its own Accountable role or trigger, numbered under its parent. Besides the Document 5 sub-rows (G2.1/G2.2, G6.1/G6.2a/G6.2b, G8.1/G8.2, S2.1/S2.2, S6.1/S6.2, S7.1–S7.5, S8.1), Document 24 adds: G4.1 Regulator Engagement, Inquiries and Inspections; G4.2 Public-Authority and Law-Enforcement Access Requests; G5.1 Privacy Notice and Transparency Management; C2.1 AI Act Classification and FRIA Interface; C2.2 Children's Data Safeguards; C2.3 Legitimate-Interest Assessment and Joint-Controller Arrangements; S6.3 Corporate Transactions (M&A). |
| **No duplicate registers** | One authoritative record per fact. Views, extracts and linked evidence records are allowed. Independent statutory records required by law are always allowed. |
