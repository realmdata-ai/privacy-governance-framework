---
title: "Data Breach Response Policy"
document_id: PGF-14
level: 2
release_version: 1.0.0-rc.2
status: release-candidate
authors: ["Alexey Neyman", "Val Khvatov"]
regulatory_reference_date: 2026-10-26
licence_proposed: "CC BY 4.0 (author-approved; source-rights confirmation pending)"
source_provenance: "Derived from internal source set ver.2: Level2/14. Data-Breach-Response-Policy_ENG.docx.md; sha256 e925faf43209b77dd3626df9cc9b1c919249c72d1117fff6cf0b6acb901b8c4c"
---
# PGF-14 — Data Breach Response Policy

*Privacy Governance Framework (PGF) · Level 2 — Policies and Standards · Release 1.0.0-rc.2 · Regulatory reference date: 26 October 2026*

> **Status and use.** Part A is a reusable template. Part B is a worked example for a fictional organisation (PanEuropean Bank AG); the named implementation profile identifies a real product; the Bank, deployment, figures, dates and records in Part B are illustrative. Nothing in this document is legal advice or a statement about any real organisation, product or provider.

# About This Document

The Data Breach Response Policy is Document 14 of the Privacy Governance Framework (PGF). It governs how the organisation moves from a **security event** to a qualified **personal data breach**, how it records **every** personal data breach, how it assesses the risk to individuals, and how it decides on notification to the competent supervisory authority (SA) and communication to data subjects. It also fixes the boundaries with information security, with the DORA incident-reporting track for financial entities, and with the processor's duty to notify its controller.

Document 14 owns the PGF definitions of security event, personal data breach and privacy incident, and the breach and incident clocks; other PGF documents cite them (Editorial and Governance Rules, Sections 3 and 4.4). It does not create a separate risk methodology: the severity factors of the Privacy Risk Assessment Methodology (Document 18, Section 3.4) and the severity scale of the Privacy Risk Appetite Statement (Document 8, Section 4) are reused to describe harm, while the legal tests of Arts. 33 and 34 GDPR decide notification.

# How to Use This Document

Part A is a drafting template. Bracketed text in bold italics marks a placeholder. Callouts marked **Guidance** explain what a section should contain and are removed from the adopted document. Part B shows the template completed for a fictional pan-European retail bank as at 26 October 2026.

> **Guidance.** This document relies on the Privacy Governance Charter (Document 2, Sections 2 and 8 — harm types and decision rights), the RACI Matrix (Document 5, rows S7.1–S7.5), the Interface and Integration Model (Document 3, Sections 3.2 and 3.14), the Regulatory Applicability Matrix (Document 7, Sections 4.2 and 5) and the Privacy Risk Assessment Methodology (Document 18, Section 3.4). If these have not been adopted, start with them.

# Table of Contents

**Part A — Template**  
Glossary of Terms  
1. Purpose  
2. Scope and Qualification Sequence  
3. Breach Risk Assessment and Severity  
4. Status Relative to Information Security (CISO)  
5. Notification to Authorities  
6. Communication to Data Subjects  
7. Internal Escalation  
8. Investigation, Records and Documentation  
9. Roles and Responsibilities  
10. Relationship to Other Framework Documents  
11. Review and Amendment  
12. Approval  
**Part B — Worked Example: PanEuropean Bank AG** — Sections 1–12 as in Part A  
**Normative Basis and References**  
**International Adaptation**  
**Document History (PGF)**

# Part A — Template

**Data Breach Response Policy — *[Legal name of organisation]***

*Effective date: [DD Month YYYY] · Version: [x.x] · Document owner: [Executive Privacy Programme Owner (EPPO)] · Adopted by: [Executive Management] (Governing Body informed)*

***Version History***

| Version | Date | Changes |
| :---- | :---- | :---- |
| ***[1.0]*** | ***[DD Month YYYY]*** | ***[First version of the document]*** |
| ***[x.x]*** | ***[DD Month YYYY]*** | ***[Brief description of material changes]*** |

## Glossary of Terms

*This table lists only terms that this document defines or that need explicit differentiation from related terms in other framework documents.*

| Term | Definition / Reference |
| :---- | :---- |
| Security event | Any information-security event, whether or not personal data are involved — for example, an alert, a malware detection, a failed log-in pattern, a system outage or a lost device. Managed by the CISO under the information-security incident process (Section 4). |
| Personal data breach | GDPR Art. 4(12): a breach of security leading to the accidental or unlawful destruction, loss, alteration, unauthorised disclosure of, or access to, personal data transmitted, stored or otherwise processed. It covers confidentiality, integrity and availability breaches, including temporary loss of availability. **There is no harm threshold for the existence of a breach**: harm and risk determine notification only (Sections 3, 5, 6). |
| Privacy incident | A wider internal category for events that infringe data protection rules without being a breach of security — for example, processing without a lawful basis, an unlawful publication, or use of data for an incompatible purpose. A privacy incident is recorded and remediated under this document (Section 8); where it is also a personal data breach, the breach rules apply in full. |
| Awareness | The point at which the controller has a reasonable degree of certainty that a security incident has occurred that has led to personal data being compromised (EDPB Guidelines 9/2022). A short initial investigation to establish this is permitted; it must start promptly. The 72-hour clock of Art. 33(1) runs from awareness. |
| Breach record | The record of **every** personal data breach required by Art. 33(5): the facts, the effects, the remedial action taken, and the reasoning for the notification decisions. A statutory record, kept independently of other registers and linked to them by identifier (Document 3, Section 4). |
| Incident Management System (IMS) | ***[The incident-tracking system]*** in which the breach record, the privacy-incident record and the case file of each event are kept; the single authoritative record of the status, assessment and deadlines of each breach and privacy incident. It does not duplicate the risk register (Document 22) or the consent records (Document 13); it links to them. |
| Designated decider | The member of Executive Management designated by the controller to decide on notification under Arts. 33 and 34, with a named deputy so that the 72-hour clock can always be met (Document 5, row S7.3). |
| Competent SA; lead SA; concerned SA | The GDPR supervisory authority competent for the breach. For cross-border processing (Art. 4(23)) this is the **lead SA** of the main establishment (Art. 56(1)); the other authorities are **concerned SAs**. A financial supervisor is never the GDPR SA. |
| Major ICT-related incident | DORA term (Regulation (EU) 2022/2554, Art. 3(10)) for financial entities: an ICT-related incident classified as major under Commission Delegated Regulation (EU) 2024/1772. Reported to the financial supervisor on a separate track (Section 5.4). |

## 1. Purpose

This document governs the organisation's response to security events and privacy incidents that affect personal data: qualifying an event as a personal data breach, recording every breach, assessing the risk to the rights and freedoms of individuals, deciding on notification to the competent SA and communication to data subjects, coordinating the separate notification tracks of other regimes, internal escalation, investigation and documentation.

## 2. Scope and Qualification Sequence

> **Guidance.** Do not define a breach through harm to the data subject. The GDPR defines a personal data breach by what happened to the data (destruction, loss, alteration, unauthorised disclosure or access as a result of a breach of security); harm and risk matter only for notification. A breach with no foreseeable harm is still recorded. Define a wider "privacy incident" only as an addition, never as a replacement for the statutory concept.

This document applies to every event affecting personal data processed by ***[Organisation name]*** as controller, and, where ***[Organisation name]*** acts as processor for a client, to its duties towards that client controller (Section 5.3). Each event passes through the following sequence:

| Step | Question | Outcome | Owner (Document 5) |
| :---- | :---- | :---- | :---- |
| 1 — Security event | Has an information-security event occurred? | Detection, triage and containment start at once and continue in parallel with Steps 2–5 | ***[CISO]*** (S7.1) |
| 2 — Qualification | Did a breach of security lead to the destruction, loss, alteration, unauthorised disclosure of, or access to, **personal data** (Art. 4(12))? | Yes → personal data breach. No → security event only (closed under the CISO process) or, where data protection rules were infringed without a breach of security, privacy incident | ***[Privacy Officer(s)]***; ***[EPPO]*** accountable; ***[Legal]*** and ***[DPO]*** consulted (S7.2) |
| 3 — Record | Every personal data breach is entered in the breach record (Art. 33(5)) **whatever its risk** | Breach record opened in the ***[IMS]*** | ***[Privacy Officer(s)]***; ***[EPPO]*** accountable (S7.2) |
| 4 — Risk assessment | How likely is it that the breach results in harm to individuals, and how severe would that harm be? (Section 3) | Unlikely to result in a risk / risk / high risk, per affected group | ***[Privacy Officer(s)]*** with ***[CISO]***; ***[DPO]*** advice |
| 5 — Notification decisions | SA (Art. 33) and data subjects (Art. 34) — two separate tests and decisions (Sections 5–6) | Notify / do not notify, with reasons in the breach record | ***[Designated decider]*** on mandatory ***[DPO]*** advice (S7.3) |
| Parallel — DORA (financial entities) | Is the incident a major ICT-related incident? (Section 5.4) | Separate classification, reports and clocks to the financial supervisor | ***[ICT risk function]*** (S7.4) |

Qualification rules:

* ***[Data that the controller has concluded are anonymous information (Recital 26) are not personal data. The conclusion is the controller's: it is taken by the Processing Owner on Legal's assessment, with DPO advice, supported by the PET Assessment Module of Document 18 (Section 3.3.0), and re-assessed periodically (Document 2, Section 8). An unauthorised access to such a dataset is a security event; it also triggers an unscheduled re-assessment of the anonymity conclusion in the light of the facts of the event. Until Legal records that the conclusion still holds, the event is handled as a potential personal data breach and the 72-hour clock is managed as if it applied.]***
* ***[Pseudonymised data (Art. 4(5)) and encrypted data remain personal data. A breach affecting them is a personal data breach; pseudonymisation or encryption with an uncompromised key may reduce the likelihood of harm (Section 3) but does not remove the breach.]***
* ***[Not every personal data breach is detected by information-security monitoring. Breaches arising inside the organisation — a letter or e-mail sent to the wrong recipient, loss of a paper file, access by an employee within their access rights but without a business need — are qualified in the same way and enter the same record. Staff report them through ***[the reporting channel]*** without delay.]***
* ***[A privacy incident without a breach of security — for example, the re-identification by third parties of data the organisation published as anonymous — is recorded and remediated under this document. Whether it is also a personal data breach is a legal characterisation recorded by Legal with DPO advice; where the characterisation is uncertain, the organisation applies the breach procedure (Steps 3–5) as a precaution.]***
* ***[Qualification is not delayed until the investigation is complete. The internal target for completing Step 2 is [X] hours from the first report of the event; the target is not the start of the statutory clock (Section 5.1).]***

## 3. Breach Risk Assessment and Severity

> **Guidance.** The GDPR asks two different questions: is the breach **unlikely to result in a risk** to the rights and freedoms of natural persons (Art. 33(1)), and is it **likely to result in a high risk** (Art. 34(1))? Both depend on the **likelihood and the severity** of the potential consequences for individuals (Recitals 75–76; EDPB Guidelines 9/2022). Do not drop the likelihood dimension: a breach that has occurred is a fact, but whether harm will materialise is not. Do not create a second severity scale: reuse the Document 18 severity factors and the Document 8 severity scale to describe harm.

* ***[The assessment is made per affected individual or group of individuals with similar exposure. It considers at least (EDPB Guidelines 9/2022; Article 29 Working Party guidance endorsed by the EDPB; EDPB Guidelines 01/2021 on examples): the type of breach (confidentiality, integrity, availability); the nature, sensitivity and volume of the data, including special categories (Document 10) and data enabling fraud or identity theft; the ease of identifying individuals; the severity and permanence of the consequences; special characteristics of the individuals (for example, children or other vulnerable persons) and of the controller; the number of individuals affected.]***
* ***[Likelihood of harm materialising: whether the data were encrypted or pseudonymised with keys that were not compromised; whether the data were recovered or demonstrably deleted; whether the recipient is known, trusted and has confirmed deletion; the intent of the party who obtained access (error or malice); whether the data have already been misused or published; the duration of exposure.]***
* ***[Severity: described with the factors of Document 18, Section 3.4 (harm type, data class and special categories — including criminal-offence data (Art. 10) and inferred special-category data (Document 10) — vulnerability, scale, reach, automated-decision effect, reasonable expectations), on the severity scale of Document 8, Section 4 (Minor / Moderate / Significant / Catastrophic). The organisation may use the ENISA methodology for the assessment of the severity of personal data breaches (2013) as a calibration reference; it does not replace the legal tests.]***
* ***[Consent or any other lawful basis does not reduce severity. Whether data were disclosed to a party that could lawfully have received them is a likelihood factor (trustworthiness and intent of the recipient), not a severity factor.]***
* ***[Where individuals are affected differently, the assessment is not averaged: the notification decisions follow the most exposed group, and communication under Art. 34 is addressed at least to the individuals for whom the risk is high.]***
* ***[The residual-risk tiers of Document 8 (Low / Medium / High / Critical) for planned processing do not decide notification (Document 8, Section 4, mapping table). The breach severity level (Minor to Catastrophic) is used for internal escalation (Section 7).]***

| Assessment outcome | Supervisory authority (Art. 33) | Data subjects (Art. 34) | Breach record (Art. 33(5)) |
| :---- | :---- | :---- | :---- |
| ***[Unlikely to result in a risk to the rights and freedoms of natural persons]*** | ***[Not notified; the reasons are recorded and approved by the designated decider]*** | ***[Not required]*** | ***[Always]*** |
| ***[Risk (not unlikely), not high]*** | ***[Notified without undue delay and, where feasible, within 72 hours of awareness]*** | ***[Not required by Art. 34; voluntary information may be given]*** | ***[Always]*** |
| ***[High risk]*** | ***[Notified as above]*** | ***[Communicated without undue delay, unless an Art. 34(3) condition applies (Section 6)]*** | ***[Always]*** |

* ***[Internal policy (not a GDPR requirement): where there is genuine doubt whether a breach is unlikely to result in a risk, the organisation notifies the SA.]***

## 4. Status Relative to Information Security (CISO)

***[The CISO owns security events: detection, triage, technical containment, eradication and recovery (Document 5, row S7.1; Document 3, Section 3.2). Containment starts immediately and is never delayed by the qualification or notification steps; the notification steps run in parallel with containment, not after it.]***

***[The privacy function qualifies and records every personal data breach (S7.2). The notification decision is a controller decision of the designated decider on mandatory DPO advice (S7.3). The CISO supplies the facts, is consulted, and may neither take the notification decision nor block or delay it.]***

> **Guidance.** A joint classification step at the start of every event that may involve personal data — the CISO, the privacy function and, for financial entities, the ICT risk function — shares facts across the tracks. It does not merge their decisions or clocks (Document 3, Sections 3.2 and 3.14).

## 5. Notification to Authorities

### 5.1 GDPR — notification to the competent supervisory authority (Art. 33)

* ***[Where a personal data breach is not unlikely to result in a risk to the rights and freedoms of natural persons, the controller notifies the competent SA without undue delay and, where feasible, not later than 72 hours after having become aware of it (Art. 33(1)). A notification made after 72 hours is accompanied by the reasons for the delay.]***
* ***[The clock runs from awareness (Glossary), not from the end of the investigation and not from the moment the DPO or the decider reviews the case. Internal policy (stricter than the law): the organisation tracks the clock from the first credible indication that personal data may be affected — first detection by security monitoring, a report from any employee, or a notification from a processor — whichever is earliest.]***
* ***[Where not all information is available, the notification is made in phases without undue further delay (Art. 33(4)). An initial notification is not withheld to complete the investigation.]***
* ***[Content (Art. 33(3)): (a) the nature of the breach, including where possible the categories and approximate number of data subjects and of personal data records concerned; (b) the name and contact details of the DPO or other contact point; (c) the likely consequences of the breach; (d) the measures taken or proposed to address the breach, including measures to mitigate its possible adverse effects.]***
* ***[Decision: the designated decider decides whether to notify, on mandatory DPO advice (Document 5, row S7.3); Legal and the CISO are consulted; the EPPO prepares the notification and files it through the SA's designated channel; the DPO acts as contact point for the SA (Art. 39(1)(e)). Where the decider does not follow the DPO's advice, the decider records the reasons in the breach record and the DPO may escalate directly to Executive Management (Section 7).]***
* ***[Recipient: the competent SA. With establishments in several EEA States and cross-border processing (Art. 4(23)), the one-stop-shop mechanism applies and the notification goes to the lead SA (Art. 56(1)); the concerned SAs are not notified in parallel by default (EDPB Guidelines 9/2022). Where a breach concerns only a local establishment's processing and Legal records that it is a local case (Art. 56(2)), the SA of that Member State is competent. The lead and concerned SAs are recorded in Document 7, Section 4.2.]***

### 5.2 Processor duties towards the organisation

***[Where a breach occurs at a processor of the organisation, the processor notifies the organisation without undue delay after becoming aware of it (Art. 33(2)), in the form and within the time the contract specifies (Art. 28(3)(f); Document 17). The processor does not apply the controller's risk threshold and has no 72-hour clock of its own. The organisation's clock runs from its own awareness, which normally arises on receipt of the processor's notification. An independent controller with which data are shared (for example, under a data-sharing agreement) has its own Art. 33 duties; the agreement provides for mutual information.]***

### 5.3 Where the organisation acts as processor (Document 5, row S7.5)

***[Where the organisation processes personal data on behalf of a client controller, the controller and processor roles are distinguished activity by activity (EDPB Guidelines 9/2022; EDPB guide for SMEs on data breaches). For a breach in such an activity, the owner of the client service ensures that the client controller is notified without undue delay after the organisation becomes aware of it, with the information the contract requires, and assists the controller (Art. 28(3)(f)). The organisation does not decide on notification of the SA or of data subjects for that controller and does not apply its own 72-hour clock to the client's processing.]***

### 5.4 DORA — major ICT-related incidents (financial entities only)

> **Guidance.** Delete this subsection if the organisation is not a financial entity within the scope of DORA. Never merge the DORA and GDPR tracks: they have different tests, owners, recipients and clocks. One event may require both.

* ***[The ICT risk function classifies ICT-related incidents under Commission Delegated Regulation (EU) 2024/1772. A confidentiality breach can itself contribute to classifying an incident as major (data-loss criterion).]***
* ***[A major ICT-related incident is reported to the financial supervisor ([competent authority under DORA]) under Commission Delegated Regulation (EU) 2025/301 and the related implementing technical standards: an initial notification within 4 hours of classifying the incident as major and no later than 24 hours from becoming aware of it; an intermediate report within 72 hours of the initial notification; a final report within one month of the latest updated intermediate report. Each clock is tracked with its point of reference — classification, awareness, or the previous report.]***
* ***[Late classification and specific cases. Where an incident is classified as major only later — for example, on re-classification after new facts emerge, or after the 24-hour point of reference has passed — the ICT risk function applies the specific rules of Delegated Regulation (EU) 2025/301 for that case from the legal text (Document 7, Section 5) and records the reasons for the timing. A DORA re-classification never resets, extends or replaces the GDPR clock.]***
* ***[Where a major ICT-related incident has an impact on the financial interests of clients, the financial entity informs them without undue delay as soon as it becomes aware of it, together with the measures taken (DORA Art. 19(3)). Where the same clients are also data subjects to be informed under Art. 34 GDPR, the EPPO and the ICT risk function coordinate the content and timing; neither communication replaces the other.]***
* ***[Owner: the head of the ICT risk function (Document 5, row S7.4); the EPPO and the DPO are consulted where personal data are involved.]***

### 5.5 Other parallel notification tracks

* ***[NIS2 (Directive (EU) 2022/2555). For entities in scope of NIS2, significant incidents are reported to the CSIRT or competent authority as an early warning within 24 hours of becoming aware, an incident notification within 72 hours, and a final report within one month (NIS2 Art. 23(4)). For financial entities to which DORA applies as a sector-specific Union act, DORA's incident-reporting provisions apply instead of the corresponding NIS2 provisions (NIS2 Art. 4); the organisation records which regime applies to each legal entity (Document 7, Section 5).]***
* ***[Other sector or national regimes (for example, payment-services, telecommunications or trust-service rules) — recorded in Document 7, Section 5, with their own owners and clocks.]***
* ***[Law enforcement: where an event shows signs of a criminal offence (data theft, extortion, internal misuse), Legal coordinates contact with law-enforcement authorities (Document 3, Section 3.4). A request by law enforcement to delay communication to individuals is documented; it does not delay the notification of the SA.]***

## 6. Communication to Data Subjects

* ***[Where a personal data breach is likely to result in a high risk to the rights and freedoms of natural persons, the controller communicates the breach to the data subjects without undue delay (Art. 34(1)). The decision is taken by the designated decider on mandatory DPO advice, separately from the SA decision (Document 5, row S7.3).]***
* ***[Content (Art. 34(2)): a description in clear and plain language of the nature of the breach; the name and contact details of the DPO or other contact point; the likely consequences; the measures taken or proposed, including measures to mitigate possible adverse effects; and practical advice on what the individuals can do to protect themselves (for example, changing a password, monitoring accounts).]***
* ***[Communication is not required where (Art. 34(3)): (a) the controller had implemented appropriate technical and organisational protection measures, applied to the affected data, that render the data unintelligible to any person not authorised to access them, such as encryption; (b) the controller has taken subsequent measures which ensure that the high risk is no longer likely to materialise; or (c) it would involve disproportionate effort — in that case, a public communication or similar measure informs the individuals in an equally effective manner. The condition relied on is recorded with evidence. The SA may require communication (Art. 34(4)).]***
* ***[Channel: a dedicated message through the channel the individual normally uses with the organisation; where that channel may itself be compromised, an alternative channel. The communication is not combined with marketing or other content.]***
* ***[Support measures proportionate to the risk — for example, a dedicated helpline, account or credit monitoring, replacement of compromised credentials or cards — are decided by the EPPO with Legal and the business unit concerned.]***
* ***[For financial entities, client information under DORA Art. 19(3) is coordinated with this communication (Section 5.4).]***

## 7. Internal Escalation

> **Guidance.** The escalation ladder below governs who leads the response, how intensively it is resourced and who is informed, by breach severity level (Section 3). It does not change who decides on notification: that is always the designated decider, on DPO advice, at every severity level. The DPO advises and monitors; the DPO does not decide and does not "prevail".

| Breach severity level (Section 3) | Leads the response and investigation | Informed | Target |
| :---- | :---- | :---- | :---- |
| ***[Minor]*** | ***[Privacy Officer(s) under the Privacy Operations Lead]*** | ***[EPPO; DPO]*** | ***[Case closed within [X] business days]*** |
| ***[Moderate]*** | ***[Privacy Operations Lead]*** | ***[EPPO; DPO (advice); Processing Owner]*** | ***[[X] business days]*** |
| ***[Significant]*** | ***[EPPO]*** | ***[Designated decider; DPO; Processing Owner; CISO]*** | ***[Immediately on qualification]*** |
| ***[Catastrophic]*** | ***[EPPO, within the organisation's crisis-management structure]*** | ***[Designated decider and Executive Management immediately; Governing Body [Risk] Committee; Corporate Communications]*** | ***[Immediately]*** |

* ***[Disagreement on qualification or notification. The decider records the reasons where it departs from the DPO's advice; the DPO may escalate directly to the highest management level (Executive Management) and informs the Governing Body committee where the DPO considers it necessary. Escalation never transfers the decision to the DPO and never delays a notification that the decider has decided to make. Nothing in this procedure restricts the DPO's statutory tasks, including consulting the SA under Art. 39(1)(e).]***
* ***[Confidentiality (Art. 38(5)). Where the DPO is "I" or "C" in this process, this never means automatic disclosure of the content of a report made to the DPO or of the reporter's identity; need-to-know, redaction or aggregate reporting apply.]***
* ***[Executive Management is informed of every breach notified to an SA and of every breach at Significant or Catastrophic level; the Governing Body [Risk] Committee receives the breach summary in the programme report (Document 31) and is informed ad hoc at Catastrophic level.]***
* ***[Programme-level escalation of breach metrics (addressees and time limits) follows the master escalation matrix of Document 31, Section 6.4. That matrix never delays a breach clock or a notification decision, and it does not affect the DPO's direct escalation channel or the independent channel of the Chief Audit Executive.]***

## 8. Investigation, Records and Documentation

* ***[Breach record (Art. 33(5)). Every personal data breach is recorded in the IMS, whether or not it is notified: the facts (what happened, when, how detected, systems and data affected, approximate number of individuals and records), the effects and consequences, the remedial action, the risk assessment (Section 3), the notification decisions with their reasons, the DPO's advice, and the times of awareness and of each notification. The record is a statutory record and is kept independently of other registers (Document 3, Section 4).]***
* ***[Privacy incidents that are not personal data breaches are recorded in the same IMS under a separate category.]***
* ***[Incident investigation report: chronology, root cause, data and systems affected, assessment and its justification, measures taken, notifications and their timing, lessons learned, and links to any re-assessment of an anonymity conclusion, a DPIA or a TIA.]***
* ***[Evidence preservation and forensics: the CISO preserves logs and forensic evidence from the start, in a way that keeps the evidence admissible and limits further processing of personal data to what the investigation needs.]***
* ***[Ransom demands: any decision about a ransom payment is outside this policy; it belongs to Executive Management under the crisis-management and sanctions-screening rules and never replaces or delays notification.]***
* ***[Retention: the breach record and investigation report are kept for [period], and longer where regulatory or court proceedings are pending, until their conclusion. Statutory record periods of other regimes (Section 5.5; International Adaptation) are applied in addition.]***
* ***[Follow-up: lessons learned feed the Privacy Audit and Monitoring Programme (Document 27); a breach may trigger re-assessment of a risk calculation or anonymity conclusion (Document 18), a DPIA review (Document 19, step 4.9), a TIA re-evaluation (Document 20, Section 3.2), a vendor review (Document 17) and a Privacy Risk Register entry (Document 22).]***

## 9. Roles and Responsibilities

| Role | Responsibility (Document 5 row) |
| :---- | :---- |
| ***[CISO / Security Operations]*** | ***[Detects, triages and contains security events; establishes the technical facts; preserves evidence; consulted on qualification and notification; may not decide or block notification (S7.1)]*** |
| ***[Privacy Officer(s)]*** | ***[Qualify events as personal data breaches; open and maintain the breach record; prepare the risk assessment (S7.2)]*** |
| ***[EPPO]*** | ***[Accountable for qualification and recording of every breach (S7.2); prepares the notification decision and files notifications through the SA's channel (S7.3); leads the response at Significant and Catastrophic level; owns this policy]*** |
| ***[Designated decider (member of Executive Management) and named deputy]*** | ***[Decides on notification to the SA (Art. 33) and on communication to data subjects (Art. 34), on mandatory DPO advice; records reasons where it departs from the advice (S7.3)]*** |
| ***[DPO]*** | ***[Advises on qualification, risk assessment and every notification decision, including a decision not to notify; contact point for the SA (Art. 39(1)(e)); monitors compliance with this policy; may escalate to Executive Management. Does not decide on notification]*** |
| ***[Legal]*** | ***[Consulted on qualification and legal characterisation (including whether data were anonymous, and local-case conclusions under Art. 56(2)); reviews notifications and communications; coordinates law-enforcement contact (Document 3, Section 3.4)]*** |
| ***[Privacy Operations Lead]*** | ***[Leads investigation at Minor and Moderate level; prepares the investigation report; owns the functional requirements of the IMS (technical operation by IT Management)]*** |
| ***[Head of the ICT risk function] (financial entities)*** | ***[Classifies and reports major ICT-related incidents to the financial supervisor; coordinates client information under DORA Art. 19(3) (S7.4)]*** |
| ***[Owner of the client service] (where the organisation is a processor)*** | ***[Ensures notification of the client controller without undue delay and per contract (S7.5)]*** |
| ***[Processing Owner]*** | ***[Informed; supplies business context; implements remediation in its processing]*** |
| ***[HR]*** | ***[Owns any disciplinary process for internal misuse; does not conduct the breach investigation (Document 3, Section 3.7)]*** |
| ***[Corporate Communications]*** | ***[Owns public statements and media engagement, separately from the statutory notifications; the EPPO and Legal review privacy content]*** |
| ***[Governing Body [Risk] Committee]*** | ***[Oversight: informed of breach summaries and, ad hoc, of Catastrophic breaches]*** |

## 10. Relationship to Other Framework Documents

* Relies on the Privacy Governance Charter (Document 2) — harm types (Section 2) and decision rights, including recorded reasons where DPO advice is not followed (Section 8).
* Relies on the Interface and Integration Model (Document 3) — the boundary with information security (Section 3.2), law-enforcement requests (Section 3.4), HR (Section 3.7), ICT risk and DORA (Section 3.14), and the statutory-records exception (Section 4).
* Relies on the RACI Matrix (Document 5) — rows S7.1–S7.5.
* Relies on the Regulatory Applicability Matrix (Document 7) — breach thresholds, recipients and clocks by jurisdiction (Section 4.2), reference values for non-EU regimes (Section 4.3), and DORA and NIS2 (Section 5).
* Relies on the Privacy Risk Appetite Statement (Document 8, Section 4) — the severity scale; its residual-risk tiers do not decide notification.
* Relies on the Data Classification Policy (Document 10) — data class and special categories in the risk assessment.
* Interfaces with the Data Retention and Disposal Policy (Document 11) — breaches affecting archived datasets.
* Interfaces with the Cross-Border Data Transfer Policy (Document 12) and the TIA Methodology (Document 20, Section 3.2) — a security incident or public-authority request at an importer triggers re-evaluation of the TIA; public-authority access at an importer is recorded in the TIA record (Document 12, Section 7), and this document applies where it is also a personal data breach (every breach recorded, Art. 33(5)).
* Interfaces with the Consent Management Policy (Document 13) only through the communication channel; consent does not affect severity.
* Interfaces with the Vendor and Third-Party Privacy Risk Policy (Document 17) — processor notification terms (Art. 28(3)(f)) and vendor review after an incident.
* Relies on the Privacy Risk Assessment Methodology (Document 18) — severity factors (Section 3.4) and the PET Assessment Module for anonymity conclusions (Section 3.3.0).
* Interfaces with the DPIA Methodology (Document 19, step 4.9) — review of a DPIA after a relevant incident.
* Records processing context through the RoPA (Document 21) and risks through the Privacy Risk Register (Document 22).
* Is performed as supporting process S7 (sub-processes S7.1–S7.5) of the Privacy Governance Process Map (Document 24).
* Feeds the Privacy Audit and Monitoring Programme (Document 27), the Privacy Metrics Dashboard (Document 28) and Governance Reporting (Document 31).

## 11. Review and Amendment

This document is reviewed under the continuous-improvement principle (Document 2, Section 7) and the Policy Review Cycle (Document 29), and also after any breach at Catastrophic level, after any notified breach whose handling revealed a gap in this policy, and upon any change to a breach threshold, recipient or clock recorded in Document 7. Changes are adopted by ***[Executive Management]*** on the proposal of the ***[EPPO]***, after consulting the DPO.

## 12. Approval

This document was adopted by ***[Executive Management]*** on ***[date]***. Document owner: ***[EPPO]***.

# Part B — Worked Example: PanEuropean Bank AG

> **Implementation example.** In this Part B, PEP denotes the Bank's **PAMOLA implementation profile**, including separately integrated systems. The product is real; the Bank, deployment, configurations, records and numerical results are illustrative. The example demonstrates the intended workflow and is not evidence that every function is implemented in a released product or that these numbers were measured in a product run. See [the implementation profile](../IMPLEMENTATION_PROFILE.md). Part A remains tool-neutral.


**PanEuropean Bank AG — Data Breach Response Policy**

*Effective date: 20 October 2026 · Version: 2.0 · Document owner: Chief Privacy Officer · Adopted by: Management Board*

*A fictional legal entity, provided solely for illustrative purposes.*

***Fictional document history (illustrative)***

| Version | Date | Changes |
| :---- | :---- | :---- |
| 1.0 | 1 March 2026 | First version, adopted by the Management Board; owner then the Group DPO (programme tasks then sat with the DPO) |
| 2.0 | 20 October 2026 | Re-baselined to the role model of Charter v3.0 and the RACI Matrix v4.0: owner the Chief Privacy Officer; GDPR notification decision by the CRO (deputy COO) on mandatory Group DPO advice; Art. 4(12) breach definition and breach record for every breach; likelihood restored in the risk assessment; DORA track to ECB/BaFin separated |

## Glossary of Terms

The terms of Part A apply. In addition:

| Term | Definition / Reference |
| :---- | :---- |
| IMS (Incident Management System) | PanEuropean's incident-tracking system: holds the breach record (Art. 33(5)), the privacy-incident record and the case files; accessible to the Privacy Officers, the Chief Privacy Officer, the Group DPO, the CISO and ICT Risk Control on a need-to-know basis. Separate from the Consent Management System (Document 13) and from the Bank's privacy engineering platform (PEP, illustrative); linked to the Privacy Risk Register (Document 22) and to DORA incident records by identifier. |
| Designated decider | The CRO (Management Board member designated for privacy matters); deputy: the COO. |

## 1. Purpose

This policy governs PanEuropean Bank AG's response to security events and privacy incidents affecting the personal data of customers, employees and other individuals in all five countries of operation, and the coordination of the GDPR track with the DORA track.

## 2. Scope and Qualification Sequence

The Part A sequence applies. At PanEuropean: the CISO and the Security Operations Centre (SOC) handle Step 1; Privacy Officers qualify and record (Steps 2–3) under the Chief Privacy Officer, with General Counsel and the Group DPO consulted; the CRO (deputy COO) decides on notification (Step 5) on mandatory Group DPO advice; ICT Risk Control runs the DORA track. The internal target for qualification is **4 hours** from the first report of the event.

* **Example 1 — security event on an archive previously concluded anonymous (tabletop scenario, 2026).** Unauthorised access to an archived analytics dataset that the responsible Processing Owner had concluded was anonymous information, on General Counsel's assessment with Group DPO advice. The CISO handles the security event. Because the facts of the access (the attacker also obtained a public customer-reference table) could open a re-identification path, the anonymity conclusion is re-assessed at once (Document 18 PET Assessment Module, re-run with the attacker's auxiliary data). Until General Counsel records that the conclusion still holds, the event is handled as a potential personal data breach and the 72-hour clock is tracked. Had the archive contained pseudonymised data, it would have been a personal data breach from the outset.
* **Example 2 — misdirected account statement (actual fictional case, 14 July 2026).** A Retail Lending employee attached one customer's account statement (balances and twelve months of transactions) to a letter addressed to another customer. Not detected by security monitoring; reported by the recipient by telephone on 16 July 2026 at 10:20. A breach of security (failure of an organisational measure) leading to unauthorised disclosure: a personal data breach, qualified at 13:05 the same day and recorded.
* **Example 3 — re-identification from open statistics (tabletop scenario, 2026).** The aggregated credit-portfolio statistics released on the open-data portal (Document 18, Project 3, Example 3.1: PET assessment complete; residual Medium; anonymity conclusion by the Processing Owner on Legal & Compliance's assessment, Group DPO advice) are assumed, in the scenario, to allow a journalist to identify three customers in a large-loan cell by combining public commercial registers. Legal characterisation recorded by General Counsel: the publication was the bank's intended act, so the event is primarily an unlawful disclosure (Arts. 5(1)(a), 6 and 25) — a privacy incident; because it results from the failure of a protective measure, the bank applies the breach procedure as a precaution. Both the incident response and the re-assessment of the anonymity conclusion start in parallel; the release is withdrawn pending the re-assessment.

## 3. Breach Risk Assessment and Severity

Part A, Section 3 applies. Severity is described with the Document 18 factors on the Document 8 scale; ICT Risk Control's DORA classification is not used for the GDPR tests. PanEuropean applies the internal policy "notify the HBDI where in genuine doubt" (labelled internal policy).

| Case | Likelihood of harm | Severity (Document 8 scale) | Outcome | Decisions |
| :---- | :---- | :---- | :---- | :---- |
| Example 2 (one customer) | Reduced: the recipient is an identified private individual who returned the statement and confirmed in writing on 17 July 2026 that no copy was kept; no indication of misuse. Not removed: the content was read | Significant: twelve months of transactions can reveal sensitive inferences about one person; no special-category data | **Risk, not high** | HBDI notified on 17 July 2026 at 16:40 (within 72 hours of awareness on 16 July 2026, 10:20); Art. 34 not triggered; the customer was informed voluntarily by letter and offered a new account number |
| Example 3 (scenario; three identified customers, broad sample otherwise) | High for the three customers: published identification, intent to publish | Significant for the three (financial status disclosed publicly); Minor for the rest of the sample, whom the statistics do not identify | **High risk for the three customers** | HBDI notified; the three customers communicated with directly; assessment follows the most exposed group, not the average of the sample |
| Example 1 (scenario) | Depends on the re-assessment: if the anonymity conclusion holds, no personal data were affected | — | Security event only, or a breach if the conclusion fails | If the conclusion fails: qualification, record and Part A Section 3 assessment |

Had the Example 1 archive contained special-category data (for example, residual payment protection insurance health records), the re-assessment would have been mandatory and the event treated as a potential breach of special-category data from the start.

## 4. Status Relative to Information Security (CISO)

The CISO owns detection, triage and containment (Document 3, Section 3.2) and convenes a joint classification call with the Privacy Officers and ICT Risk Control for every event that may involve personal data. The call shares facts; the GDPR decision (CRO, Group DPO advice) and the DORA decision (Head of ICT Risk Control) remain separate. The CISO may not decide, block or delay a GDPR notification.

## 5. Notification to Authorities

**5.1 GDPR.** The HBDI is the lead SA for PanEuropean's cross-border processing; the CNIL, the Garante, the AEPD and the Prezes UODO are concerned SAs and are not notified in parallel by default (Document 7, Section 4.2). A breach affecting only one branch's local processing may be a local case under Art. 56(2) only on General Counsel's recorded conclusion. The Chief Privacy Officer prepares and files the notification through the HBDI's designated channel; the Group DPO is named as the contact point (Art. 33(3)(b)). The CRO decides; in the CRO's absence the COO decides, so that the 72-hour clock is always covered. The bank tracks the clock from the first credible indication (internal policy, stricter than the law), and notifies in phases where information is incomplete (Art. 33(4)).

**5.2 Processors.** Example Cloud Services Pvt Ltd (fictional, India; remote technical support) and Example AI Provider Inc. (fictional, United States; customer-service assistant) are processors, as are the core banking platform provider, the external PEP technical support provider and the e-mail/push delivery service provider (unnamed, illustrative; Document 17). Their contracts require notification of a personal data breach to PanEuropean without undue delay and in any case within **24 hours** of the processor becoming aware (illustrative contractual term), with the information needed for Art. 33(3) (Document 17). PanEuropean's clock runs from its own awareness, normally the receipt of the processor's notification. EuroCredit Bureau (fictional) is an **independent controller** under a data-sharing agreement, not a processor; it has its own Art. 33 duties, and the agreement provides for mutual information about breaches affecting shared data. The same applies to the PPI insurer and to the partner bank in India, which are also independent controllers. A security incident at Example Cloud Services Pvt Ltd also triggers re-evaluation of TIA-CLOUD-01 (Document 20, Section 3.2, trigger 6).

**5.3 PanEuropean as processor.** Where PanEuropean operates payment services for a group company under an Art. 28 contract, the head of the service unit providing the client service ensures that the group company (as controller) is notified without undue delay and per the contract (Document 5, row S7.5); PanEuropean does not decide on that controller's notifications and applies no 72-hour clock of its own to that processing.

**5.4 DORA.** ICT Risk Control (Head of ICT Risk Control) classifies ICT-related incidents under Delegated Regulation (EU) 2024/1772 and reports major ICT-related incidents to the ECB/BaFin under Delegated Regulation (EU) 2025/301: initial notification within 4 hours of classification as major and no later than 24 hours from awareness; intermediate report within 72 hours of the initial notification; final report within one month of the latest updated intermediate report; late classification and specific cases follow the legal text (Document 7, Section 5) with the reasons for the timing recorded. Client information under DORA Art. 19(3) is coordinated with any Art. 34 communication by the Chief Privacy Officer and ICT Risk Control. The DORA report to the ECB/BaFin never replaces the GDPR notification to the HBDI, and the HBDI notification never replaces the DORA report.

**5.5 Other tracks.** For PanEuropean, DORA applies instead of the corresponding NIS2 incident-reporting provisions (NIS2 Art. 4); non-financial group service companies assess their own NIS2 status (Document 7, Section 5). Law-enforcement contact is coordinated by General Counsel (Document 3, Section 3.4).

## 6. Communication to Data Subjects

Where the CRO decides that a breach is likely to result in a high risk, customers are informed without undue delay by a dedicated message in the banking app and by e-mail; where those channels may be compromised, by letter. The message contains the Art. 34(2) content and practical advice (for example, changing passwords, monitoring the account, how to recognise follow-up phishing). The Chief Privacy Officer, with General Counsel and the business line concerned, decides on support measures — a dedicated helpline and, where financial data enabling fraud are exposed, card replacement and account monitoring. Any reliance on an Art. 34(3) condition is recorded with evidence. The Group DPO advises on the communication decision and its content.

## 7. Internal Escalation

| Breach severity level | Leads | Informed | Target |
| :---- | :---- | :---- | :---- |
| Minor | Privacy Officer(s) under the Privacy Operations Lead | Chief Privacy Officer; Group DPO | Case closed within 10 business days |
| Moderate | Privacy Operations Lead | Chief Privacy Officer; Group DPO (advice); Processing Owner | Case closed within 15 business days |
| Significant | Chief Privacy Officer | CRO; Group DPO; Processing Owner; CISO | Immediately on qualification |
| Catastrophic | Chief Privacy Officer within the bank's crisis-management structure | CRO and the Management Board immediately; Risk Committee of the Supervisory Board; Corporate Communications | Immediately |

The CRO decides on notification at every level. Where the CRO departs from the Group DPO's advice, the reasons are recorded in the breach record; the Group DPO may escalate directly to the Management Board and inform the Risk Committee of the Supervisory Board where it considers it necessary. Example 2: the Group DPO advised notification of the HBDI and voluntary information to the customer; the CRO followed the advice.

## 8. Investigation, Records and Documentation

Every personal data breach and privacy incident is recorded in the IMS with the Part A content. Example 2 was recorded as breach record entry BR-2026-0117 (illustrative), with the investigation report and the Group DPO's advice; root cause: manual assembly of statement letters; remediation: automated envelope-content matching in the print workflow, completed 30 September 2026. Investigation reports and breach records are retained for 10 years (illustrative internal value), and longer while regulatory or court proceedings are pending. The tabletop scenario for Example 3 led to a standing instruction: any third-party claim of re-identification from an open release triggers both the breach procedure and an immediate re-assessment of the anonymity conclusion under Document 18 (the Processing Owner decides on Legal & Compliance's assessment, with Group DPO advice); the evidence of the re-assessment is linked to the incident record.

## 9. Roles and Responsibilities

| Role | Responsibility |
| :---- | :---- |
| CISO / SOC | Detection, triage, containment, evidence preservation; joint classification call (S7.1) |
| Privacy Officer(s) | Qualification and breach record (S7.2) |
| Chief Privacy Officer (EPPO) | Accountable for qualification and recording (S7.2); prepares and files notifications to the HBDI (S7.3); leads the response at Significant and Catastrophic level; owner of this policy |
| CRO (deputy: COO) | Decides on notification to the HBDI and on communication to customers, on mandatory Group DPO advice (S7.3) |
| Group DPO | Advises on qualification, assessment and every notification decision; contact point for the HBDI; monitors this policy; may escalate to the Management Board |
| General Counsel | Legal characterisation; local-case conclusions (Art. 56(2)); review of notifications; law-enforcement contact |
| Privacy Operations Lead | Investigation at Minor and Moderate level; investigation reports; functional owner of the IMS (technical operation by IT Management) |
| Head of ICT Risk Control | DORA classification and reporting to the ECB/BaFin; DORA Art. 19(3) client information (S7.4) |
| Head of the service unit providing a client service | Notification of a group-company controller where PanEuropean acts as processor (S7.5) |
| HR | Disciplinary process for internal misuse (Document 3, Section 3.7) |
| Corporate Communications | Public statements and media engagement, separately from statutory notifications |
| Risk Committee of the Supervisory Board | Oversight; informed of breach summaries quarterly (Document 31) and ad hoc at Catastrophic level |

## 10. Relationship to Other Framework Documents

The Part A relationships apply. In addition: the HBDI as lead SA and the concerned SAs are recorded in PanEuropean's Document 7, Section 4.2; DORA reporting to the ECB/BaFin in Document 7, Section 5 and Document 3, Section 3.14; processor notification terms for Example Cloud Services Pvt Ltd and Example AI Provider Inc. in Document 17; the open-data release used in Example 3 in Document 18, Project 3, Example 3.1.

## 11. Review and Amendment

This policy is reviewed under the Policy Review Cycle (Document 29), after any breach at Catastrophic level, after any notified breach whose handling revealed a gap, and upon any change to the breach rules in PanEuropean's Document 7. Changes are adopted by the Management Board on the proposal of the Chief Privacy Officer, after consulting the Group DPO.

## 12. Approval

Version 2.0 of this policy was adopted by the Management Board of PanEuropean Bank AG on 20 October 2026. Document owner: Chief Privacy Officer.

# Normative Basis and References

**EU law**
* Regulation (EU) 2016/679 (GDPR): Arts. 4(5), 4(12), 4(23), 5, 6, 25, 28(3)(f), 32, 33, 34, 38(5), 39(1)(e), 56, 60; Recitals 26, 75, 76, 85–88.
* Regulation (EU) 2022/2554 (DORA): Arts. 3(10), 17–19 (including Art. 19(3)); Commission Delegated Regulation (EU) 2024/1772 (classification of ICT-related incidents); Commission Delegated Regulation (EU) 2025/301 (content and time limits of incident reports) and the related implementing technical standards.
* Directive (EU) 2022/2555 (NIS2): Arts. 4 and 23.
* Proposal for a Digital Omnibus (data, GDPR and cyber-reporting amendments): proposal only; Council negotiating mandate agreed 21 October 2026; not enacted — the current GDPR rules, including the 72-hour clock, apply (Document 7, Section 5.1).

**Guidance**
* EDPB Guidelines 9/2022 on personal data breach notification under GDPR, version 2.0 (adopted 28 March 2023).
* EDPB Guidelines 01/2021 on examples regarding personal data breach notification.
* EDPB data protection guide for small business — data breaches (controller and processor roles).
* ENISA, Recommendations for a methodology of the assessment of severity of personal data breaches (December 2013) — calibration reference only.
* Article 29 Working Party, Guidelines on Data Protection Officers, WP243 rev.01 (§2.6, confidentiality).

**Canada (International Adaptation)**
* Personal Information Protection and Electronic Documents Act (PIPEDA), ss. 10.1–10.3; Breach of Security Safeguards Regulations (SOR/2018-64).
* Act respecting the protection of personal information in the private sector (Québec, P-39.1), ss. 3.5–3.8; Regulation respecting confidentiality incidents.

# International Adaptation

> **Guidance.** The GDPR is the baseline. The regimes below have their own tests, recipients and clocks; the GDPR 72-hour clock is never imported into them. Record the values that apply to the organisation in Document 7 (Sections 4.2–4.3) and cite them here.

* **United Kingdom (headline).** UK GDPR and the DPA 2018, as amended by the Data (Use and Access) Act 2025 (phased commencement): the same breach tests as the GDPR; notification to the ICO without undue delay and, where feasible, within 72 hours of awareness; communication to individuals where the risk is high; every breach documented.
* **Switzerland (headline).** revFADP: a breach of data security likely to result in a high risk is reported to the FDPIC as soon as possible; individuals are informed where necessary for their protection or where the FDPIC requires it.
* **Canada — PIPEDA.** A breach of security safeguards involving personal information under the organisation's control that creates a **real risk of significant harm** (assessed from the sensitivity of the information and the probability of misuse) is reported to the Office of the Privacy Commissioner of Canada and notified to the affected individuals **as soon as feasible** after the organisation determines that the breach has occurred; organisations and government institutions that may reduce the risk are also notified. A record of **every** breach of security safeguards is kept for **24 months** after the day the organisation determines the breach occurred. The accountable Privacy Officer (Principle 4.1) owns the process; this is not an EU DPO role.
* **Canada — Québec (P-39.1).** A **confidentiality incident** presenting a **risk of serious injury** is notified promptly to the Commission d'accès à l'information and to the persons concerned; reasonable measures are taken to reduce the risk of injury; a **register of all confidentiality incidents** is kept for the period set by the Regulation respecting confidentiality incidents. The person in charge of the protection of personal information is consulted on the risk assessment.
* **Canada — applicability.** Apply the applicability map of Document 7, Section 3.1. Alberta and British Columbia PIPA (including Alberta's mandatory breach reporting) and the public and health sectors are out-of-scope extensions. Bill C-36 is a proposal; PIPEDA remains in force. The OPC/OIPC guidance *Getting Accountability Right with a Privacy Management Program* is the Canadian programme reference.

The PIPEDA record and the Québec register are independent statutory records and are always kept, even where they overlap with the IMS (Document 3, Section 4).

# Document History (PGF)

| Release | Date | Summary |
| :---- | :---- | :---- |
| 1.0.0-rc.1 | 2026-10-26 | Canonical English Markdown; changes from internal ver.2: harm-based incident definition replaced by the sequence security event → personal data breach (Art. 4(12), no harm threshold) → breach record for every breach (Art. 33(5)) → risk assessment → separate SA (Art. 33) and data-subject (Art. 34) decisions; likelihood restored in the risk assessment (EDPB Guidelines 9/2022; ENISA 2013 as calibration reference); consent removed as a severity factor; Art. 33(1) statutory test, awareness, reasons for delay, phased notification (Art. 33(4)), Art. 33(3) content incl. DPO contact, Art. 34(2)–(4) content and exceptions added; notification decision moved from the DPO to the controller's designated Executive Management member on mandatory DPO advice (DPO never "prevails"; recorded reasons and escalation); CISO owns containment and may not decide or block notification; anonymity conclusions attributed to the Processing Owner on Legal's assessment (Document 18 PET module as evidence); lead SA / concerned SA wording corrected (one-stop-shop, local case Art. 56(2)); processor → controller path and processor-extension (S7.5) added; DORA separated as its own track (major ICT-related incident; Delegated Regulations 2024/1772 and 2025/301 with points of reference and late classification; client information Art. 19(3)); NIS2 relationship stated; undefined oversight label replaced by Executive Management and the Governing Body committee in escalation; IMS no longer cross-refers to a non-existent Document 11 register; evidence preservation, ransom and retention rules added; EuroCredit Bureau corrected to independent controller; fictional providers used; Canadian (PIPEDA, Québec), UK and Swiss variants added; owner EPPO, adopted by Executive Management; example dates shifted by −12 months, Examples 1 and 3 recast as tabletop scenarios consistent with Document 18, Example 3.1. Integration pass: criminal-offence and inferred special-category data named among severity inputs; public-authority access at importers linked to the TIA record; Part B processor list aligned with Document 17; cross-reference to the master escalation matrix (Document 31) |
| 1.0.0-rc.2 | 2026-10-28 | Author-approved publication direction; named PAMOLA implementation examples with tool-neutral templates; direct integrated-score mapping without automatic per-metric risk-tier overrides; observations, DPO dissent and the authorised business decision recorded separately from legal/release conditions. |
