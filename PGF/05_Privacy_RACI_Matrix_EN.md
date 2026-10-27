---
title: "Privacy RACI Matrix"
document_id: PGF-05
level: 1
release_version: 1.0.0-rc.1
status: release-candidate
authors: ["Alexey Neyman", "Val Khvatov"]
regulatory_reference_date: 2026-10-26
licence_proposed: "CC BY 4.0 (proposed; subject to rights-holder confirmation)"
source_provenance: "Derived from internal source set ver.2: Level1/5. Privacy_RACI_Matrix_Template and Example_ENG.docx.md; sha256 01d655e2a0cdb181409959ec70df714f4a3e347b6f9f2190a675d1be65db8249"
---
# PGF-05 — Privacy RACI Matrix

*Privacy Governance Framework (PGF) · Level 1 — Strategic Documents · Release 1.0.0-rc.1 · Regulatory reference date: 26 October 2026*

> **Status and use.** Part A is a reusable template. Part B is a worked example for a fictional organisation (PanEuropean Bank AG); all names, figures, dates and records in Part B are illustrative. Nothing in this document is legal advice or a statement about any real organisation, product or provider.

# **About This Document**

The Privacy RACI Matrix is Document 5 of the Privacy Governance Framework (PGF). It is the single source of truth for the distribution of responsibility (Responsible / Accountable / Consulted / Informed, plus a separate Approve/Decide column) across each top-level process and its key activities recorded in the process map (Document 24): governing processes G1–G9, core processes C1–C5 and supporting processes S1–S9.

This document takes precedence over the Process Owner Register (Document 25) — the latter is not maintained independently but is generated as a derivative (projection) of this matrix. This document is operationalised in the Operational Role & Staffing Model (Document 26), where the roles recorded here are mapped to specific filled positions. The roles themselves are defined in the Privacy Governance Charter (Document 2, Sections 8 and 9); their qualification profiles are in the Privacy Role Competency Framework (Document 6).

The allocation in this document follows one decision model for the whole framework:

* the **Controller** (the legal entity) is ultimately accountable (GDPR Arts. 5(2), 24); **Executive Management** adopts policies and takes management decisions, including acceptance of residual risk above delegated limits; the **Governing Body** oversees, receives assurance and may hold reserved consent matters;
* the **Executive Privacy Programme Owner (EPPO)** is Accountable for operating the programme;
* the **Processing Owner** is Accountable for processing-level decisions within the delegation granted by the controller;
* the **Data Protection Officer (DPO)** is Responsible/Accountable only for its own statutory tasks, is Consulted on every DPIA and on every decision with significant data protection impact, and is otherwise Consulted or Informed;
* **Independent Internal Audit** is Accountable for the independent assurance opinion, under an internal-audit charter and risk-based plan approved by the Governing Body's Audit Committee; **Legal** owns the legal compliance gate (G-L); the **CISO** owns security events and technical containment.

# **How to Use This Document**

Part A is a drafting template: replace the bracketed placeholders and keep the allocation logic unless a documented reason requires a change. Part B shows the template completed for a fictional bank.

| GUIDANCE  Before developing this document, confirm that the Privacy Governance Process Map (Document 24) has been approved at least in draft form — without a list of processes and activities there is nothing for the RACI matrix to map against. Also confirm that the Charter (Document 2) and the Interface & Integration Model (Document 3) have already recorded the roles that will be used as the matrix columns. Do not re-baseline a row mechanically (for example, by replacing every "DPO = A" with "EPPO = A"): decide each row by the nature of the decision. |
| :---- |

# **Table of Contents**

**Part A — Template**	  
**Glossary of Terms**	  
1. Purpose of This Document	  
2. Principles for Allocating Roles	  
3. Roles Included in the Matrix	  
4. RACI — Governing Processes (G1–G9)	  
5. RACI — Core Processes (C1–C5)	  
6. RACI — Supporting Processes (S1–S9) and Statutory Activities	  
7. Residual-Risk Acceptance Authority and Escalation	  
8. Relationship to Other Framework Documents	  
9. Review and Amendment	  
10. Approval	  
**Part B — Worked Example**	  
**Glossary of Terms**	  
1. Purpose of This Document	  
2. Principles for Allocating Roles	  
3. Roles Included in the Matrix	  
4. RACI — Governing Processes (G1–G9)	  
5. RACI — Core Processes (C1–C5)	  
6. RACI — Supporting Processes (S1–S9) and Statutory Activities	  
7. Residual-Risk Acceptance Authority and Escalation	  
8. Relationship to Other Framework Documents	  
9. Review and Amendment	  
10. Approval	  
**Normative Basis and References**	  
**International Adaptation**	  
**Document History (PGF)**

# **Part A — Template**

**Privacy RACI Matrix *[Legal name of organisation]***

Effective date: ***[DD Month YYYY]***   ·   Version: ***[x.x]***   ·   Document owner: ***[Executive Privacy Programme Owner (EPPO)]***   ·   Adopted by: ***[Executive Management]***   ·   Oversight: ***[Governing Body committee]***

***Version History***

| Version | Date | Changes |
| :---- | :---- | :---- |
| ***[1.0]*** | ***[DD.MM.YYYY]*** | ***[First version of the document]*** |
| ***[x.x]*** | ***[DD.MM.YYYY]*** | ***[Brief description of material changes]*** |
| **GUIDANCE**  *Maintain the version history from the document's first publication, recording only material changes — in particular, the appearance of a new process on the map (Document 24), a change in the set of roles, a change in delegated risk-acceptance tiers, or a change to escalation rules.* |  |  |

## **Glossary of Terms**

*This table lists only terms defined by this document itself; roles are defined in the Charter (Document 2, Sections 8 and 9).*

| Term | Definition / Reference |
| :---- | :---- |
| RACI | A model for allocating responsibility (Responsible / Accountable / Consulted / Informed) across privacy-related processes; the matrix assigning RACI roles to each process is established by this document. |
| Approve / Decide (D) | The body or role that formally adopts, approves or decides, where this differs from the Accountable role — for example, Executive Management adopting a policy that the EPPO is Accountable for drafting and maintaining, or the Executive Management member who accepts High residual risk. A role with a veto or a co-decision right is shown in this column, never in the C or I column. |
| Mandatory consultation (C\*) | A Consulted role whose advice must be sought and recorded before the decision is taken (for example, DPO advice on every DPIA, GDPR Art. 35(2)). Consultation is not approval: the decision-maker may depart from the advice only by recording reasons (Section 7). |

## **1. Purpose of This Document**

This document is the single source of truth for the distribution of responsibility for privacy governance processes at ***[organisation name]***. The matrix allocates roles (not individuals) across five types of involvement — Responsible, Accountable, Approve/Decide, Consulted, Informed — for each top-level process of the process map (Document 24) and its key activities. The document does not assign specific staff to roles (this is done by the Operational Role & Staffing Model, Document 26) and does not describe the operational procedures for performing the processes (these are recorded in the process map itself).

| GUIDANCE  *The matrix must cover processes across all three process groups of the process map — governing (G1–G9), core (C1–C5), and supporting (S1–S9). Do not limit the matrix to core processes only: governing and supporting processes regularly end up without a clear owner precisely because they are left out of the RACI.* |
| :---- |

## **2. Principles for Allocating Roles**

| GUIDANCE  *Without explicit principles, a RACI matrix quickly degenerates into a list where several roles are shown as Accountable for the same process — the first sign that the matrix will not be used in an actual conflict, because it fails to give an unambiguous answer as to who is responsible.* |
| :---- |

* ***[Single-Accountable principle — each process/activity may have only one role holding Accountable status; if responsibility is actually shared, this indicates that the process should be broken down into smaller activities rather than assigning two Accountable roles]***

* ***[Decision-by-nature principle — the Accountable role is chosen by the nature of the decision, not by the function that happens to perform the work: programme operation → EPPO; processing-level decisions within delegation → Processing Owner; legal compliance gate → Legal; security events → CISO; independent assurance → Independent Internal Audit; the DPO's own statutory tasks → DPO; adoption of policies and acceptance of residual risk above delegated limits → Executive Management]***

* ***[DPO-independence principle — the DPO is Responsible/Accountable only for its own statutory tasks (informing and advising, monitoring compliance including the compliance audits it organises under GDPR Art. 39(1)(b), awareness-raising, DPIA advice, cooperation with and contact point for the supervisory authority). The DPO is Consulted (C\*) on every DPIA and on every decision with significant data protection impact, and is otherwise Consulted or Informed. The DPO never authorises processing, accepts risk on the controller's behalf, determines purposes or means, holds a veto, or "prevails"]***

* ***[Roles-not-individuals principle — the matrix allocates responsibility among roles (EPPO, DPO, Privacy Operations Lead, etc.), not among named individuals; a change of staff member holding a role does not require revising the matrix]***

* ***[Responsible ≠ Accountable principle — Responsible performs the work, Accountable answers for the outcome to the level above; for most activities these are different roles. R and A may coincide for a specific decision task (for example, a Processing Owner accepting Low residual risk, the DPO's own advice, the Independent Internal Audit opinion, the Legal determination at the G-L gate), provided there is a single A and the independence of any review of that decision is preserved. What is prohibited is combining incompatible assurance and decision roles — for example, the DPO accepting risk it later monitors, or the programme owner issuing the independent assurance opinion on its own programme]***

* ***[Approval-is-not-consultation principle — a right to approve, co-decide or block is shown in the Approve/Decide column; the C and I columns never carry hidden approval rights]***

* ***[Minimal-consultation principle — a role is included as Consulted only if its input materially changes the decision; mandatory consultations required by law (for example, DPO advice on a DPIA) are always included and marked C\*]***

* ***[Mandatory-Informed principle — roles included as Informed receive notification as a matter of course, rather than requesting it; the absence of a role from the I column for a process that affects it is a completion error, not an economy. On rows performed by the DPO, "I" and "C" are subject to the confidentiality safeguard below (Art. 38(5))]***

***Definitions for the Purposes of This Document***

| Designation | Meaning | Definition |
| :---- | :---- | :---- |
| R | Responsible | ***[The role that directly performs the process/activity]*** |
| A | Accountable | ***[The role answering for the outcome to the level of management above; unique per process/activity]*** |
| D | Approve / Decide | ***[The body or role that formally adopts, approves or decides, where different from A; empty where A decides]*** |
| C / C\* | Consulted / mandatory consultation | ***[The role whose opinion is sought before the decision is made; C\* — advice must be sought and recorded]*** |
| I | Informed | ***[The role notified of the decision or its outcome after the fact]*** |

## **3. Roles Included in the Matrix**

| GUIDANCE  *The list of roles must match the roles recorded in the Charter (Document 2, Sections 8 and 9), the Organisational Design Strategy (Document 4), and the interface map (Document 3). Do not introduce new role names specifically for this matrix — doing so would violate the single-source-of-truth principle. A generic oversight label is not a role: name the body (Governing Body, its Risk or Audit Committee, or the management-level Privacy Risk Committee).* |  |  |
| :---- | :---- | :---- |
| **Role** | **Level / Affiliation** | **Source Defining the Role** |
| Governing Body (and its Risk / Audit Committees) | ***[Oversight tier — board of directors or supervisory board]*** | ***[Charter, Sections 8–9]*** |
| Executive Management | ***[Management tier — management board or executive committee; "EM member" = the designated member]*** | ***[Charter, Sections 8–9]*** |
| Executive Privacy Programme Owner (EPPO) | ***[Management tier — a designated executive; no separate new post is required; must not be the DPO]*** | ***[Charter, Section 8; Document 4, Section 4]*** |
| Privacy Risk Committee | ***[Management tier — management-level committee chaired by the EPPO or a member of Executive Management; the DPO attends as a non-voting adviser]*** | ***[Charter, Section 9; Document 4, Section 4]*** |
| Processing Owner | ***[Business line — a mandate held by an existing business-line head within delegated authority; outside the privacy function]*** | ***[Charter, Section 8; Document 6, Section 4.6; mandate holders — Document 25, Section 10]*** |
| Data Protection Officer (DPO) | ***[Independent statutory role (GDPR Arts. 37–39), outside the management hierarchy of the programme, with direct access to the highest management level]*** | ***[Charter, Section 8; Document 6, Section 4.1]*** |
| Privacy Operations Lead (POL) | ***[Management tier — runs day-to-day privacy operations; owns Risk Calculation Projects (Document 18); reports to the EPPO]*** | ***[Charter, Section 9; Document 4, Section 4]*** |
| Privacy Officer(s) / Privacy Engineer(s) | ***[Execution tier]*** | ***[Document 4, Section 5]*** |
| Data Protection Coordinator (DPC) | ***[Execution tier, a distributed role within the business unit]*** | ***[Document 4, Section 7]*** |
| Legal | ***[Owner of the legal compliance gate (G-L) and of legal determinations]*** | ***[Document 3, Section 3.4]*** |
| CISO / Information Security | ***[Owner of security events and technical containment]*** | ***[Document 3, Section 3.2]*** |
| ***[ICT risk function (financial entities subject to DORA)]*** | ***[Owner of ICT-related incident classification and reporting to the financial supervisor]*** | ***[Document 3, Sections 3.2 and 3.14]*** |
| Independent Internal Audit | ***[Third line; reports functionally to the Governing Body's Audit Committee]*** | ***[Document 3, Section 3.10; Document 27]*** |
| ***[Business unit]*** | ***[Owner of a product/process outside the privacy function; performs work for its Processing Owner]*** | ***[Document 3, Sections 3.9–3.10]*** |
| ***[IT Management]*** | ***[Owner of technical implementation]*** | ***[Document 3, Section 3.6]*** |
| ***[Data Governance / ERM / HR / Procurement]*** | ***[Supporting functions]*** | ***[Document 3, Sections 3.1, 3.3, 3.7, 3.8]*** |

> **Guidance.** The Controller is the legal entity, not a role in the matrix: it acts through Executive Management and the delegations recorded here. Where the Governing Body has reserved consent for a specific matter (for example, adoption of the Charter), show it in the Approve/Decide column together with Executive Management ("EM; Governing Body consent if reserved"); do not move management decisions or operational risk acceptance to the Governing Body.

## **4. RACI — Governing Processes (G1–G9)**

The governing processes in this section correspond to governing processes G1–G9 of the process map (Document 24). Each row carries its code. When the process map is revised (Section 9), the composition and codes of the rows in this section are brought into alignment within the same review cycle.

| GUIDANCE  Governing processes set the rules for all other processes. Accountable here is normally the EPPO (programme operation), with adoption by Executive Management in the Approve/Decide column and oversight by the Governing Body in the I column. Two governing processes contain activities that belong to other roles by their nature: compliance monitoring organised by the DPO (G6.1) and the internal-audit charter and plan approved by the Governing Body's Audit Committee (G6.2a) and the independent assurance opinion of Internal Audit (G6.2b); the programme report (G8.1) and the DPO's own report to the highest management level (G8.2). |  |  |  |  |  |
| :---- | :---- | :---- | :---- | :---- | :---- |
| **Process (Document 24)** | **R** | **A** | **D** | **C** | **I** |
| ***G1 — Privacy Strategy*** | Privacy Operations Lead | EPPO | Executive Management | DPO, Legal, CISO, ***[ERM]*** | Governing Body committee, all roles |
| ***G2.1 — Setting Risk Limits (Privacy Risk Appetite, Document 8)*** | EPPO, ***[ERM]*** | EPPO | Executive Management (Governing Body consent only if its rules so provide) | DPO, Legal, CISO, Processing Owners | Governing Body Risk Committee, Privacy Operations Lead |
| ***G2.2 — Risk Assessment Methodology (Document 18)*** | Privacy Operations Lead, ***[ERM]*** | EPPO | Privacy Risk Committee | DPO, Legal, CISO | Executive Management, Independent Internal Audit |
| ***G3 — Maintaining and Reviewing the RACI Model*** | Privacy Operations Lead | EPPO | Executive Management | DPO, Legal, Processing Owners | All roles |
| ***G4 — Regulatory Monitoring*** | Privacy Officer(s), Legal | EPPO | — | DPO | Privacy Operations Lead; Executive Management (material changes) |
| ***G4.2 — Public-Authority and Law-Enforcement Access Requests*** | Legal, Privacy Officer(s) | Legal | — | DPO, CISO | EPPO, Processing Owner |
| ***G5 — Developing Policies and Standards*** | Privacy Operations Lead | EPPO | Executive Management (Governing Body consent only where reserved) | DPO (C\*), Legal, CISO, Processing Owners | Governing Body committee, all roles |
| ***G5.1 — Privacy Notice and Transparency Management (Arts. 12–14): framework and organisation-wide notices*** | Privacy Operations Lead, Legal | EPPO | Executive Management (where the notice is adopted as part of Document 1) | DPO (C\*) | Processing Owners |
| ***G5.1 — Privacy Notice and Transparency Management: notice content for a processing activity*** | Privacy Officer(s), ***[Business unit]*** | Processing Owner | — | DPO (C\*), Legal | EPPO |
| ***G6.1 — Compliance Monitoring and DPO-Organised Audits (GDPR Art. 39(1)(b))*** | DPO, Privacy Officer(s) under DPO direction | DPO | — | EPPO, Legal, auditees | Executive Management; Governing Body Audit Committee where the DPO considers it necessary; Independent Internal Audit |
| ***G6.2a — Internal-Audit Charter/Mandate, Risk-Based Audit Plan and Significant Plan Changes (covering privacy)*** | ***[Chief Audit Executive]*** / Independent Internal Audit | ***[Chief Audit Executive]*** | Governing Body Audit Committee (approves) | Executive Management, EPPO, DPO (input to risk assessment) | Governing Body Risk Committee |
| ***G6.2b — Independent Assurance Opinion on the Programme (Document 27)*** | Independent Internal Audit (may be supplemented by an external auditor) | ***[Chief Audit Executive]*** | — | DPO, EPPO (as auditees and information sources) | Governing Body Audit Committee, Executive Management |
| ***G7 — Metrics and KPIs (Document 28)*** | Privacy Operations Lead | EPPO | — | DPO | Executive Management, Governing Body committee |
| ***G8.1 — Programme Reporting (Document 31)*** | Privacy Operations Lead | EPPO | — | DPO | Executive Management, Governing Body committee |
| ***G8.2 — DPO Report to the Highest Management Level (GDPR Art. 38(3))*** | DPO | DPO | — | — | Executive Management; Governing Body committee where the DPO considers it necessary; EPPO |
| ***G9 — Processing Owner Mandate Designation*** | Privacy Operations Lead (prepares the proposal and the Document 25 entry) | EPPO | Executive Management (designates the holder and the delegated tier) | DPO, Legal | The designated Processing Owner, Privacy Risk Committee (management level), Data Protection Coordinator of the line; Governing Body's Risk Committee (oversight) |

> **Guidance.** G9 is never self-appointment: the business line does not designate its own Processing Owner. Executive Management designates the holder and the delegated acceptance tier (Section 7) on the EPPO's proposal; the designee is Informed and confirms acceptance of the mandate.

> **Guidance — sub-processes of the process map.** The sub-processes added by Document 24 (Section 2.3) each have one row with a single "A": G4.2 and G5.1 above; C2.2 and the legitimate-interest part of C2.3 in Section 5.2; S6.3 in Section 6; G4.1 (Regulator Engagement, Inquiries and Inspections — G4.1(a) controller response, G4.1(b) DPO cooperation and contact point), C2.1 (AI Act classification and FRIA interface) and the Art. 26 part of C2.3 in the statutory-activities table of Section 6.

## **5. RACI — Core Processes (C1–C5)**

Subsections 5.1–5.5 are numbered in accordance with the current version of the Privacy Governance Process Map (Document 24): 5.1 corresponds to core process C1, 5.2 to C2, 5.3 to C3, 5.4 to C4, and 5.5 to C5. At each subsequent revision of the process map (Section 9), the numbering of this section is brought into alignment within the same review cycle, to prevent divergence between documents.

| GUIDANCE  *Core processes are broken down to the level of key activities — unlike governing and supporting processes, where a RACI at the level of the whole process is often sufficient. It is here that real conflicts of interest most often arise, requiring precise allocation of responsibility. The mandatory gates G-L, G-DPIA, G-36 and G-TIA (below) appear as explicit rows, so that no risk decision can be recorded before the gate that precedes it.* |
| :---- |

***Mandatory gates (identical wording across Documents 5, 8, 12, 14, 16, 18, 19, 20, 22, 24 and 31)***

* **G-L — Legal compliance gate.** Runs **before** any risk decision. Checks: lawful basis (Art. 6); condition for special-category data (Art. 9) or criminal-offence data (Art. 10); purpose compatibility (Art. 6(4)); transparency deliverable (Arts. 13/14); Art. 22 permissibility and safeguards; valid transfer tool and TIA outcome (Chapter V — the TIA where the mechanism requires one, see G-TIA); mandatory deadlines and statutory duties. **Failure means stop or redesign.** No risk appetite, risk acceptance, DPO opinion or metric can cure a G-L failure.
* **G-DPIA — DPIA triage.** Triggers: Art. 35(1); the Art. 35(3) cases; the SA lists under Art. 35(4); the **nine** WP248 rev.01 criteria (two or more → presumption that a DPIA is required). DPO advice is required on **every** DPIA (Art. 35(2)), whatever the score.
* **G-36 — Prior consultation.** G-36 is **evaluated** for every DPIA. It is a statutory test, independent of internal tiers.
  * **Trigger.** If the DPIA indicates that processing would still result in a **high risk to the rights and freedoms of natural persons** in the absence of further mitigating measures, the controller consults the competent SA **before processing starts** (Art. 36(1)). This applies irrespective of the internal tier.
  * **Internal tiers as an indicator.** An internal "High" or "Critical" residual tier is a strong indicator that the test is met. The legal conclusion is recorded separately, with reasons (Legal, with DPO advice).
  * **Stricter internal policy.** An organisation may adopt a stricter *internal policy* — e.g. "all residual High is routed to consultation". It must be labelled as internal policy, not as a GDPR obligation.
  * **During and after consultation.** Under Art. 36(2) the SA may give written advice within the statutory period, which may be extended; request information, which suspends the period; or use its Art. 58 powers, including a temporary or definitive limitation or ban.
  * **No authorisation by elapse.** An elapsed period, or the absence of SA comments, is **not** an authorisation or a certificate of lawfulness. G-L remains in force throughout, and the controller remains responsible.
* **G-TIA — Transfer equivalence, branched by mechanism.**
  * **Art. 45 adequacy.** Check that the decision covers the destination, sector and recipient (scope and eligibility, e.g. DPF certification), that it remains valid, and monitor it. There is no statutory obligation to redo the Commission's assessment. A stricter internal review is labelled as internal policy.
  * **Art. 46 appropriate safeguards (e.g. SCCs, BCRs).** A TIA plus supplementary measures (EDPB Recommendations 01/2020 v2.0, Step 2 and following).
  * **Art. 49 derogations.** Exceptional and interpreted restrictively. The specific conditions are documented.
  * G-L and DPIA duties apply under every mechanism.
  * The TIA under Art. 46 assesses the **laws and practices** of the destination: public-authority access, enforceable rights and redress, supplementary measures, and re-evaluation (CJEU C-311/18).
  * If essentially equivalent protection cannot be ensured, the transfer does not start or is suspended. Risk appetite cannot override this.
  * PETs, TEEs, homomorphic encryption and remote access are **not** automatic exemptions from Chapter V (EDPB Guidelines 05/2021).
  * A DPIA and Art. 36 may be needed in parallel with a TIA.
* **Statutory deadlines.** A missed statutory deadline is a breach of obligation and is escalated, even if an aggregate KPI stays green. Metrics state the denominator, how zero cases are handled, and the cut-off rule.

***5.1 Risk Calculation Project Development (C1)***

| Activity | R | A | D | C | I |
| :---- | :---- | :---- | :---- | :---- | :---- |
| ***[Preparing the risk calculation project charter]*** | Privacy Engineer(s) | Privacy Operations Lead | — | DPO | ***[Business unit]*** |
| ***[Determining whether the configuration is standard]*** | Privacy Engineer(s) | Privacy Operations Lead | — | DPO | — |
| ***[Approving the project via the standard track]*** | Privacy Engineer(s) | Privacy Operations Lead | — | — | DPO |
| ***[Methodological assessment of the charter via the non-standard track]*** | Privacy Operations Lead, Privacy Engineer(s) | EPPO | — | DPO, Legal, CISO | Privacy Risk Committee |
| ***[Deciding whether to approve a non-standard project]*** | EPPO | EPPO | Privacy Risk Committee | DPO | Executive Management (material change to the methodology) |
| ***[Registering the project in the risk calculation project register]*** | Privacy Engineer(s) | Privacy Operations Lead | — | — | ***[Business unit]***, DPO |

***5.2 Data Request and Transformation (C2; request → G-L → G-DPIA → DPIA → PET → decision)***

| Activity | R | A | D | C | I |
| :---- | :---- | :---- | :---- | :---- | :---- |
| ***[Intake and triage of the data processing request]*** | Privacy Officer(s) | Privacy Operations Lead | — | Processing Owner, ***[Business unit]*** | DPO |
| ***[G-L — legal compliance gate]*** | Legal, Privacy Officer(s) | Legal | — | DPO (C\*) | Processing Owner, EPPO |
| ***[C2.3 — Legitimate-interest assessment (Art. 6(1)(f), as part of G-L)]*** | Privacy Officer(s) | Legal | — | DPO (C\*) | Processing Owner, EPPO |
| ***[C2.2 — Children's data safeguards (where the activity concerns children)]*** | Privacy Officer(s), ***[Business unit]*** | Processing Owner | — | Legal, DPO | EPPO |
| ***[G-DPIA — DPIA triage]*** | Privacy Officer(s) | Processing Owner | — | DPO (C\*) | Privacy Operations Lead |
| ***[Conducting the DPIA (controller's assessment, GDPR Art. 35(1))]*** | Privacy Officer(s), ***[Business unit]*** | Processing Owner | — | DPO (C\*), CISO, Legal | EPPO |
| ***[DPO advice on the DPIA (GDPR Arts. 35(2), 39(1)(c))]*** | DPO | DPO | — | — | Processing Owner, EPPO |
| ***[Selecting an existing risk calculation project from the register]*** | Privacy Officer(s) | Privacy Operations Lead | — | — | DPO |
| ***[Selecting and applying privacy-enhancing techniques (PET)]*** | Privacy Engineer(s) | Privacy Operations Lead | — | CISO, IT Management | DPO |
| ***[Developing/configuring a new PET technique]*** | Privacy Engineer(s) | EPPO | Privacy Risk Committee (material change to the methodology) | DPO, IT Management | Executive Management |
| ***[Calculating residual risk and proposing mitigation measures (Document 18)]*** | Privacy Officer(s), Privacy Engineer(s) | Privacy Operations Lead | — | DPO (C\*), Legal, CISO | Processing Owner |
| ***[Accepting residual risk — Low tier]*** | Processing Owner | Processing Owner | — | DPO (C\* where a DPIA exists) | EPPO |
| ***[Accepting residual risk — Medium tier]*** | Processing Owner | Processing Owner | EPPO (concurrence) | DPO (C\*) | Privacy Risk Committee |
| ***[Accepting residual risk — High tier]*** | Processing Owner (proposes) | The single decider named by the delegation in force: ***[named Executive Management member]***, or the Privacy Risk Committee where a written delegation designates it | — | DPO (C\*), Legal, EPPO | Governing Body Risk Committee |
| ***[Critical tier — stop or redesign]*** | Processing Owner | Processing Owner | Executive Management (only if high risk remains after redesign and the controller proposes to proceed; G-36 evaluated and, where met, consultation first) | DPO (C\*), Legal, EPPO | Governing Body Risk Committee |
| ***[G-36 — evaluation of the Art. 36 test (recorded with reasons, for every DPIA)]*** | Legal | Legal | — | DPO (C\*) | Processing Owner, EPPO |
| ***[G-36 — prior consultation with the competent SA where the test is met (or where internal policy routes the case)]*** | EPPO, Processing Owner (prepare the Art. 36(3) submission) | ***[Named Executive Management member]*** | — | DPO (C\*; contact point for the SA), Legal | Governing Body Risk Committee |
| ***[Compiling the evidence pack]*** | Privacy Engineer(s) / Privacy Officer(s) | Privacy Operations Lead | — | — | Processing Owner, DPO |

***5.3 Data Subject Rights (C3)***

| Activity | R | A | D | C | I |
| :---- | :---- | :---- | :---- | :---- | :---- |
| ***[Intake and verification of the data subject request]*** | Privacy Officer(s) | Privacy Operations Lead | — | Legal | DPO |
| ***[Assessing the scope and method of fulfilling the request]*** | Privacy Officer(s) | Privacy Operations Lead | — | ***[Business unit]***, IT Management, Legal | DPO |
| ***[Fulfilling the request (access, rectification, erasure, restriction, portability, objection)]*** | ***[Business unit]*** / IT Management | Privacy Operations Lead | — | Legal | Processing Owner |
| ***[Human intervention and review of a decision based solely on automated processing (GDPR Art. 22(3))]*** | ***[Staff of the deciding unit with authority and competence to change the decision]*** | Processing Owner | — | DPO (on request) | Privacy Operations Lead |
| ***[Refusal, extension or restriction of a request (GDPR Arts. 12(3)–(5), 23 and national restrictions)]*** | Privacy Officer(s) | Privacy Operations Lead | — | Legal, DPO | Processing Owner |
| ***[Final response to the data subject (within one month, extendable under Art. 12(3))]*** | Privacy Officer(s) | Privacy Operations Lead | — | — | DPO |
| ***[Data subject contacts and complaints addressed to the DPO (GDPR Art. 38(4))]*** | DPO | DPO | — | Privacy Operations Lead (only as the DPO decides is needed to resolve the matter; confidentiality safeguard applies) | EPPO (aggregate or redacted reporting unless the DPO decides otherwise) |

> **Guidance — confidentiality of the DPO's work (Art. 38(5); WP243 rev.01, §2.6).** Where the EPPO, the Privacy Operations Lead or anyone else appears as "I" or "C" on a row performed by the DPO, this never means automatic disclosure of the content of a request made to the DPO or of the requester's identity. Disclosure follows need-to-know, purpose limitation, and secrecy or confidentiality under Art. 38(5) and applicable law; redaction or aggregate reporting is used where appropriate. The DPO decides how its own work is distributed. This does not prevent the DPO from investigating matters or discussing them with management.

***5.4 Cross-Border Data Transfer (C4; conditional subprocess)***

| Activity | R | A | D | C | I |
| :---- | :---- | :---- | :---- | :---- | :---- |
| ***[Identifying a cross-border transfer within the data flow (including remote access)]*** | Privacy Engineer(s) | Privacy Operations Lead | — | IT Management, CISO, Legal | DPO |
| ***[Mechanism check and, for Art. 46 safeguards, the transfer impact assessment (TIA) — laws and practices of the destination (Document 20); for Art. 45 adequacy, scope/eligibility/validity check and monitoring; for Art. 49, documented conditions]*** | Legal, Privacy Officer(s) | Legal | — | DPO (C\*), CISO | Processing Owner, EPPO |
| ***[Selecting the transfer tool and designing supplementary measures]*** | Legal (contractual), CISO (technical) | Processing Owner | — | DPO, Privacy Engineer(s) | Privacy Operations Lead |
| ***[G-TIA — determination by mechanism (Art. 45 / 46 / 49) and, where a TIA is required, whether essentially equivalent protection is ensured]*** | Legal | Legal | — | DPO (C\*) | Processing Owner, EPPO, Executive Management |
| ***[Decision to proceed with the transfer — only if G-L and G-TIA are passed and any DPIA/G-36 step is complete]*** | Processing Owner | The single decider under Section 7 (Processing Owner up to Medium; the named Executive Management member for High) — the decision record names one | — | DPO (C\*), EPPO | Privacy Risk Committee |
| ***[Suspension or termination where equivalence can no longer be ensured]*** | Processing Owner, Legal | Processing Owner | — | DPO | EPPO, Executive Management |
| ***[Periodic re-evaluation of the TIA]*** | Legal, Privacy Officer(s) | Legal | — | DPO | Processing Owner |

> **Guidance.** The depth of the transfer review depends on the mechanism: under Art. 45 adequacy, check scope, recipient eligibility and validity and monitor the decision (no statutory obligation to redo the Commission's assessment; any stricter internal review is labelled internal policy); under Art. 46 safeguards, a TIA plus supplementary measures is required; Art. 49 derogations are exceptional and their conditions are documented. G-L and DPIA duties apply under every mechanism. There is no "residual-risk acceptance" for a transfer that fails G-TIA. If essentially equivalent protection cannot be ensured, the transfer does not start or is suspended; no Processing Owner, Executive Management or Governing Body decision can override this.

***5.5 Consent Management (C5)***

| Activity | R | A | D | C | I |
| :---- | :---- | :---- | :---- | :---- | :---- |
| ***[Designing the consent request and mechanism (GDPR Arts. 4(11), 7)]*** | ***[Business unit]*** | Processing Owner | — | Legal, DPO | Privacy Operations Lead |
| ***[Collecting consent]*** | ***[Business unit]*** | Processing Owner | — | Legal | DPO |
| ***[Storing and recording consent (proof of consent, Art. 7(1))]*** | Privacy Engineer(s) / IT Management | Privacy Operations Lead | — | — | DPO |
| ***[Processing consent withdrawal (as easy as giving consent, Art. 7(3))]*** | ***[Business unit]*** / IT Management | Processing Owner | — | — | Privacy Operations Lead, DPO |

## **6. RACI — Supporting Processes (S1–S9) and Statutory Activities**

| GUIDANCE  *Supporting processes often inherit Responsible from adjacent corporate functions (Data Governance, IT, HR, Procurement) under the principle of asset-owner primacy (Document 3, Section 2) — the privacy function does not take over execution but remains Accountable or Consulted wherever the interface provides for it.* |  |  |  |  |  |
| :---- | :---- | :---- | :---- | :---- | :---- |
| **Process (Document 24)** | **R** | **A** | **D** | **C** | **I** |
| ***S1 — Data Classification*** | ***[Data Governance]*** | ***[Head of Data Governance]*** | — | EPPO, DPO, Privacy Engineer(s), Legal, CISO | Privacy Operations Lead |
| ***S2.1 — Retention Schedule (Document 11)*** | Privacy Operations Lead, Legal | EPPO | Executive Management (as policy, G5) | DPO, Processing Owners | All roles |
| ***S2.2 — Retention and Disposal Execution*** | ***[Business unit]*** / IT Management | Processing Owner | — | Legal | DPO, Privacy Operations Lead |
| ***S3 — Data Inventory*** | ***[Data Governance]*** | Privacy Operations Lead | — | Privacy Engineer(s), Processing Owners | DPO, EPPO |
| ***S4 — Record of Processing Activities (RoPA, Art. 30)*** | Privacy Officer(s) | Privacy Operations Lead | — | Processing Owners (confirm entries), ***[Data Governance]*** | DPO, EPPO |
| ***S5 — Privacy Risk Register*** | Privacy Operations Lead | EPPO | — | Processing Owners (risk owners of entries), DPO, CISO, ***[ERM]*** | Executive Management, Governing Body Risk Committee |
| ***S6.1 — Vendor Privacy Due Diligence (Document 17)*** | Privacy Officer(s), ***[Procurement]*** | Privacy Operations Lead | — | CISO, Legal | DPO |
| ***S6.2 — Engaging a Processor or Recipient (GDPR Art. 28 contract or data-sharing agreement)*** | ***[Procurement]***, Legal | Processing Owner | — | DPO, CISO, EPPO | Executive Management (arrangements for ICT services supporting critical or important functions, where DORA applies) |
| ***S6.3 — Corporate Transactions (M&A): Privacy Due Diligence and Data Migration*** | Legal, Privacy Officer(s); the EPPO leads the privacy workstream | ***[Processing Owner of the transaction]*** | — | DPO, CISO | Executive Management |
| ***S7.1 — Security Event Detection, Triage and Containment*** | CISO / ***[SOC]*** | CISO | — | Privacy Operations Lead | DPO |
| ***S7.2 — Personal Data Breach Qualification and Recording (every breach, Art. 33(5); Document 14)*** | Privacy Officer(s) | EPPO | — | DPO, CISO, Legal | Processing Owner |
| ***S7.3 — GDPR Notification Decision (Art. 33 to the competent SA — the lead SA for cross-border processing; Art. 34 to data subjects)*** | EPPO (prepares; files through the agreed SA channel) | Designated Executive Management member (with a named deputy for the 72-hour clock) | — | DPO (C\*; contact point for the SA), Legal, CISO | Governing Body Risk Committee, Processing Owner |
| ***S7.4 — DORA Major ICT-Related Incident Classification and Reporting to the Financial Supervisor (financial entities only)*** | ***[ICT risk function]***, CISO | ***[Head of the ICT risk function]*** | — | EPPO, DPO (where personal data are involved) | Executive Management, Governing Body Risk Committee |
| ***S7.5 — Processor extension: Notifying the Client Controller of a Personal Data Breach (where the organisation acts as processor; Art. 33(2))*** | Privacy Officer(s), CISO | ***[Owner of the client service]*** | — | Legal (contract terms), DPO | EPPO |
| ***S8 — Staff Training (Document 30)*** | ***[HR]*** (delivery) / Privacy Operations Lead (content) | EPPO | — | DPO | All roles |
| ***S8.1 — DPO Awareness-Raising Activities (GDPR Art. 39(1)(b))*** | DPO | DPO | — | Privacy Operations Lead | EPPO |
| ***S9 — Operating the Automation Tooling*** | Privacy Engineer(s) | Privacy Operations Lead | — | IT Management, CISO | DPO, EPPO |

> **Guidance.** S7.3 and S7.4 are separate tracks with separate owners, authorities and clocks. The GDPR track goes to the competent data protection supervisory authority; the DORA track goes to the financial supervisor. Neither replaces the other, and a financial supervisor is never the GDPR SA. Document 14 is authoritative for definitions and clocks.

> **Guidance — controller profile and processor extension.** This matrix is a controller profile: S7.2–S7.3 and the gates describe decisions the organisation takes as controller. Where the organisation acts as processor for a client (S7.5 and the processor obligations of Document 17), it notifies the client controller without undue delay after becoming aware of a breach and as the contract specifies (Art. 33(2)); it does not apply the controller's risk threshold and has no 72-hour clock of its own. The controller and processor roles are distinguished activity by activity (EDPB Guidelines 9/2022).

***Statutory activities outside the G/C/S rows***

| Activity | R | A | D | C | I |
| :---- | :---- | :---- | :---- | :---- | :---- |
| ***[Designating the DPO and communicating the contact details to the SA and publishing them (GDPR Art. 37(1), (7))]*** | EPPO, ***[HR]*** | Executive Management | Executive Management (Governing Body consent only if reserved) | Legal | Governing Body committee, DPO, all staff |
| ***[Ensuring DPO resources, access and independence (GDPR Art. 38(1)–(3), (6))]*** | EPPO | Executive Management | — | DPO | Governing Body committee |
| ***[G4.1(b) — Cooperation with the SA and acting as its contact point (GDPR Art. 39(1)(d)–(e))]*** | DPO | DPO | — | Legal, EPPO | Executive Management |
| ***[G4.1(a) — Controller response to SA inquiries, investigations and orders]*** | Legal, Privacy Operations Lead | EPPO | Executive Management (where the response commits the controller) | DPO (C\*) | Governing Body committee |
| ***[C2.3 — Joint-controller arrangement (GDPR Art. 26)]*** | Legal | Processing Owner | — | DPO, EPPO | Privacy Operations Lead |
| ***[C2.1 — Fundamental rights impact assessment and other AI Act deployer duties — interface only (Document 3, Section 3.5)]*** | ***[AI governance function]*** | Processing Owner | — | DPO, Legal | EPPO |

## **7. Residual-Risk Acceptance Authority and Escalation**

| GUIDANCE  *This section applies only after G-L has been passed. It records who may accept residual risk to the rights and freedoms of individuals at each tier and what additional step is mandatory. The threshold values separating the tiers are determined exclusively by the Privacy Risk Appetite Statement (Document 8) and the methodology (Document 18); they are not redefined here. Organisational consequences (regulatory, financial, reputational) are a separate track and never offset rights-and-freedoms risk.* |  |  |  |
| :---- | :---- | :---- | :---- |
| **Residual Tier (Document 8)** | **Who May Accept** | **Additional Mandatory Step** | **Timeframe** |
| ***[Low]*** | Processing Owner | Record. DPO advice where a DPIA exists. | ***[—]*** |
| ***[Medium]*** | Processing Owner, with EPPO concurrence | DPO advice recorded. Conditional acceptance carries an expiry date and is re-assessed on expiry. | ***[[X] business days]*** |
| ***[High]*** | **One** named member of Executive Management, or the Privacy Risk Committee where a written delegation designates it. Each decision record names a single effective decider. | G-36 evaluated and recorded. Prior consultation **whenever the Art. 36 test is met** (a High tier is a strong indicator; any stricter routing is labelled internal policy). DPO advice recorded. Governing Body committee informed. | ***[[X] business days; where consultation is required, processing does not start before the SA's written advice or the end of the Art. 36(2) period, and never in breach of any Art. 58 measure]*** |
| ***[Critical]*** | Not acceptable | Stop or redesign. If high risk remains after redesign, the G-36 test is evaluated and, where met, consultation precedes any processing. The decision sits with Executive Management. Reserved consent of the Governing Body applies only if its rules so provide. | ***[Immediately]*** |

***When the decision-maker does not follow DPO advice***

* ***[The decision-maker records the reasons for departing from the DPO's advice in the evidence pack before the decision takes effect]***
* ***[The DPO may escalate directly to the highest management level (Executive Management); the DPO informs the Governing Body committee if the DPO considers it necessary. Escalation does not suspend a decision unless Executive Management so decides; it never transfers the decision to the DPO]***
* ***[The DPO's advice and any escalation are recorded; neither the content of the advice nor the fact of escalation may be used to the DPO's detriment (GDPR Art. 38(3))]***

The escalation rule set out here does not replace the conflict-resolution matrix of the Interface & Integration Model (Document 3, Section 5) — that matrix applies to general disagreements between the privacy function and another corporate function (for example, over the prioritisation of initiatives or process organisation), whereas this section governs specifically the acceptance of residual risk and the handling of DPO advice — a specialised procedure established by the Charter (Section 8), not a general cross-functional mechanism. Escalation of programme metrics and findings to management and oversight bodies follows the master escalation matrix of Document 31, Section 6.4; that matrix does not change the acceptance authority above, never delays a statutory clock and does not affect the DPO's direct escalation channel or the independent channel of the Chief Audit Executive.

## **8. Relationship to Other Framework Documents**

This document builds on the Privacy Governance Process Map (Document 24) and allocates responsibility for the processes and activities listed there. This document:

* ***[Is the primary source for the Process Owner Register (Document 25) — the latter is not maintained independently but is generated as a projection of this matrix; a change of process owner is made here, not in the register]***

* ***[Is operationalised in the Operational Role & Staffing Model (Document 26) — there, the roles in this matrix are mapped to specific filled positions and individuals]***

* ***[The acceptance authority (Section 7) is tied to the tiers of the Privacy Risk Appetite Statement (Document 8, Section 5) and does not redefine the thresholds]***

* ***[The list of roles (Section 3) is aligned with the Charter (Document 2, Sections 8 and 9), the Organisational Design Strategy (Document 4), and the interface map (Document 3)]***

* ***[Records the RACI for designating the Processing Owner mandate (G9, Section 4); the mandate itself is established by the Charter (Document 2, Section 8); the role profile is in the Role Competency Framework (Document 6, Section 4.6); the register of current mandate holders is Document 25, Section 10]***

* ***[Incident definitions and clocks are those of the Data Breach Response Policy (Document 14); DPIA and prior-consultation procedure — Document 19; TIA — Document 20; independent assurance — Document 27]***

| GUIDANCE  *If the Process Owner Register (Document 25) contains an entry absent from this matrix, or vice versa, this indicates a divergence between sources of truth, not an alternative version of the responsibility allocation. This document always takes precedence — see the single-source-of-truth principle, Charter, Section 7.* |
| :---- |

## **9. Review and Amendment**

This document is reviewed under the terms established by the principle of continuous improvement (Charter, Section 7) and the ***[Policy Review Cycle, Document 29]***, and also whenever the Privacy Governance Process Map (Document 24), the delegated risk-acceptance tiers, or the organisational structure of the privacy function (Document 4) changes. Amendments are prepared by the EPPO, with DPO advice, and adopted by ***[Executive Management]***; the ***[Governing Body committee]*** is informed.

## **10. Approval**

This document was adopted by ***[Executive Management]*** on ***[date]***. Document owner: ***[EPPO]***.

# **Part B — Worked Example**

**PanEuropean Bank AG — Privacy RACI Matrix**

Effective date: 20 October 2026   ·   Version: 4.0   ·   Document owner: Chief Privacy Officer (EPPO)   ·   Adopted by: Management Board   ·   Oversight: Risk Committee of the Supervisory Board

*A fictional legal entity, presented solely for illustrative purposes.*

***Fictional document history (illustrative)***

| Version | Date | Changes |
| :---- | :---- | :---- |
| 1.0 | 1 March 2026 | First version of the document, developed concurrently with the Organisational Design Strategy |
| 2.0 | 22 August 2026 | Section 7 converted to the Processing Owner model: the residual-risk decision was split into "Assessment" and "Decision"; corrected the reference to the mandate holder register — Document 25, Section 10 |
| 3.0 | 18 September 2026 | Section 5 aligned with the Privacy Governance Process Map (Document 24): subsections 5.1–5.5 labelled as processes C1–C5; risk calculation project register maintained in PEP; added the row "Processing Owner Mandate Designation (G9)" to Section 4 |
| 4.0 | 20 October 2026 | Role model re-baselined after an internal review of DPO independence: Chief Privacy Officer designated as EPPO; Group DPO limited to its statutory tasks (advice, monitoring, DPIA advice, SA contact point); Approve/Decide column added; G-L, G-DPIA, G-36 and G-TIA rows added; G6 split into DPO compliance monitoring and Internal Audit assurance, with the Audit Committee approving the internal-audit charter and plan; Art. 38(5) confidentiality safeguard for DPO rows; processor extension row for Art. 33(2); G9 designation moved to the Management Board; GDPR breach notification separated from DORA reporting; Privacy Risk Committee re-established at management level; rows for the sub-processes of the process map version 2.0 (G4.1, G4.2, G5.1, C2.1–C2.3, S6.3) added; Processing Owner list extended to the mandate holders designated on 20 October 2026 |

## **Glossary of Terms**

*This table lists only terms defined by this document itself; terms used here but defined in another document are not repeated in this table.*

| Term | Definition / Reference |
| :---- | :---- |
| RACI | A model for allocating responsibility (Responsible / Accountable / Consulted / Informed) across privacy-related processes; the matrix assigning RACI roles to each process is established by this document. |
| Approve / Decide (D) | The body or role that formally adopts, approves or decides, where this differs from the Accountable role. |
| Mandatory consultation (C\*) | Advice that must be sought and recorded before the decision is taken; not an approval right. |

## **1. Purpose of This Document**

This document is the single source of truth for the distribution of responsibility for privacy governance processes at PanEuropean Bank AG. Before this matrix was adopted, the allocation of responsibility among the Group DPO, local Privacy Officer(s), and business units (Credit Decisions, Digital Banking, Marketing, Customer Service, Fraud Prevention) existed informally and was understood differently by different participants — this document records it explicitly and consistently across all five countries of presence. Version 4.0 also removes programme-management accountability from the Group DPO, which had accumulated in earlier versions, and assigns it to the Chief Privacy Officer as EPPO.

## **2. Principles for Allocating Roles**

* Single-Accountable principle — for example, the acceptability of Medium residual risk for the credit-scoring model is the responsibility of the Processing Owner (Head of Credit Decisions) alone, with the Chief Privacy Officer's concurrence shown in the Approve/Decide column; the Group DPO gives mandatory advice (C\*) but is never Accountable for the decision

* Decision-by-nature principle — the legal compliance gate (G-L) and the TIA equivalence determination belong to Legal; independent assurance belongs to Group Internal Audit; security events belong to the CISO; programme operation belongs to the Chief Privacy Officer

* DPO-independence principle — the Group DPO is R/A only for its own statutory tasks (rows G6.1, G8.2, C2 "DPO advice on the DPIA", C3 "contacts and complaints addressed to the DPO", S8.1 and SA cooperation); where others are C or I on these rows, the Group DPO decides what is shared, subject to Art. 38(5) and need-to-know

* Roles-not-individuals principle — when the specific Privacy Officer in Germany changes, the matrix is not revised

* Responsible ≠ Accountable principle — Privacy Engineer(s) apply PET techniques on PEP (R), but the Privacy Operations Lead is Accountable for that activity (A); R and A coincide only for specific decision tasks with a single A and an independent review route — for example, the Head of Credit Decisions accepting Low residual risk, which the Group DPO monitors and Group Internal Audit may review

* Approval-is-not-consultation principle — the Chief Privacy Officer's concurrence at the Medium tier and the Privacy Risk Committee's delegated authority at the High tier are shown explicitly (in the Approve/Decide or Accountable column), not hidden in C or I

* Minimal-consultation principle — the Chief Data Officer is included as Consulted only for processes where this reflects an actual interface point from the Interface & Integration Model (Document 3), not by default

* Mandatory-Informed principle — the Risk Committee of the Supervisory Board is Informed of every High-tier acceptance, every prior consultation with the HBDI, every notifiable personal data breach and every major ICT-related incident, without exception

***Definitions for the Purposes of This Document***

| Designation | Meaning | Definition |
| :---- | :---- | :---- |
| R | Responsible | The role that directly performs the process/activity |
| A | Accountable | The role answering for the outcome to the level of management above; unique per process/activity |
| D | Approve / Decide | The body or role that formally adopts, approves or decides, where different from A |
| C / C\* | Consulted / mandatory consultation | The role whose opinion is sought before the decision is made; C\* — advice must be sought and recorded |
| I | Informed | The role notified of the decision or its outcome after the fact |

## **3. Roles Included in the Matrix**

| Role | Level / Affiliation | Source Defining the Role |
| :---- | :---- | :---- |
| Supervisory Board (Aufsichtsrat) — Risk Committee, Audit Committee | Oversight tier; supervises the Management Board (AktG §111); reserved consent (AktG §111(4)) for exactly three privacy matters: the Charter, the board-level privacy risk appetite (Document 8, Section 3) and removal of the Group DPO | Charter, Sections 8–9 |
| Management Board (Vorstand) | Management tier; manages the bank and takes management decisions; designated member for privacy matters: the CRO | Charter, Sections 8–9 |
| Chief Privacy Officer (EPPO) | Management tier; reports to the CRO | Charter, Section 8; Organisational Design Strategy, Section 4 |
| Privacy Risk Committee | Management-level committee chaired by the CRO; members: Chief Privacy Officer, CIO, CISO, General Counsel, Head of Compliance; the Group DPO attends as a non-voting adviser | Charter, Section 9; Organisational Design Strategy, Section 4 |
| Processing Owner | Mandate held, by designation of the Management Board on the Chief Privacy Officer's proposal (G9), by the heads of Credit Decisions, Digital Banking, Marketing, Customer Service, Fraud Prevention, Insurance Distribution, Compliance (AML screening), Payment Services, Human Resources and Branch Network, the CIO for IT-operated processing, and the Chief Privacy Officer for the privacy function's own processing (holders — Document 25, Section 10) | Charter, Section 8; Document 6, Section 4.6 |
| Group DPO | Independent statutory role; reports directly to the Management Board | Charter, Section 8; Document 6, Section 4.1 |
| Privacy Operations Lead (POL) | Management tier; reports to the Chief Privacy Officer | Charter, Section 9; Organisational Design Strategy, Section 4 |
| Privacy Officer(s) / Privacy Engineer(s) | Execution | Organisational Design Strategy, Section 5 |
| Data Protection Coordinator (DPC) | Execution, a distributed role in the business lines | Organisational Design Strategy, Section 7 |
| Legal (General Counsel) | Owner of the legal compliance gate (G-L) | Interface & Integration Model, Section 3.4 |
| CISO | Owner of information security, security events and containment | Interface & Integration Model, Section 3.2 |
| ICT Risk Control function | DORA ICT risk function; owner of major ICT-related incident classification and reporting to the financial supervisor | Interface & Integration Model, Sections 3.2 and 3.14 |
| Group Internal Audit | Third line; reports functionally to the Audit Committee of the Supervisory Board | Interface & Integration Model, Section 3.10; Document 27 |
| IT Management (CIO) | Owner of technical implementation and PEP infrastructure | Interface & Integration Model, Section 3.6 |
| Chief Data Officer (CDO) | Data Governance (classification scheme, Data Catalogue) | Interface & Integration Model, Section 3.3 |
| Chief Risk Officer (CRO) / ERM | Management Board member; ERM taxonomy | Interface & Integration Model, Section 3.1 |
| Business units (Credit Decisions, Digital Banking, Marketing, Customer Service, Fraud Prevention, Insurance Distribution, Compliance, Payment Services, Human Resources, Branch Network) | Perform work for their Processing Owner | Interface & Integration Model, Sections 3.9–3.10 |

The Privacy Risk Committee is a management committee, not a committee of the Supervisory Board. The Supervisory Board and its Risk and Audit Committees appear in this matrix in three capacities: in the I column (oversight, receipt of reports and assurance); in the Approve/Decide column next to the Management Board where the Supervisory Board's rules of procedure reserve consent for a specific matter under AktG §111(4) — at PanEuropean, in the privacy area, only the adoption of the Privacy Governance Charter, the board-level privacy risk appetite (Document 8, Section 3) and the removal of the Group DPO; and, for the Audit Committee, as the approver of the internal-audit charter, the risk-based audit plan and significant plan changes (row G6.2a), under the bank's internal-audit charter and in line with the IIA Global Internal Audit Standards 2024 (Standards 6.2 and 9.4) — a governance and professional-practice basis, not a GDPR obligation. None of these capacities involves taking management decisions or accepting operational risk.

## **4. RACI — Governing Processes (G1–G9)**

The governing processes in this section correspond to governing processes G1–G9 of the Privacy Governance Process Map (Document 24). The former row "Developing the Privacy Risk Assessment Methodology" is now G2.2; the former "Compliance Audit" row is split into G6.1, G6.2a and G6.2b; the former "Reporting to the Supervisory Board" row is split into G8.1 and G8.2.

| Process (Document 24) | R | A | D | C | I |
| :---- | :---- | :---- | :---- | :---- | :---- |
| G1 — Privacy Strategy | Privacy Operations Lead | Chief Privacy Officer | Management Board | Group DPO, General Counsel, CISO, CRO | Risk Committee of the Supervisory Board, all roles |
| G2.1 — Setting Risk Limits (Privacy Risk Appetite) | Chief Privacy Officer, ERM | Chief Privacy Officer | Management Board (board-level appetite, Document 8 Section 3: with the Supervisory Board's consent — reserved consent matter) | Group DPO, General Counsel, CISO, Processing Owners | Risk Committee of the Supervisory Board, Privacy Operations Lead |
| G2.2 — Risk Assessment Methodology (Document 18) | Privacy Operations Lead, ERM | Chief Privacy Officer | Privacy Risk Committee | Group DPO, General Counsel, CISO | Management Board, Group Internal Audit |
| G3 — Maintaining and Reviewing the RACI Model | Privacy Operations Lead | Chief Privacy Officer | Management Board | Group DPO, General Counsel, Processing Owners | All roles |
| G4 — Regulatory Monitoring (GDPR, BDSG and national law, EDPB guidance, AI Act, DORA interfaces) | Privacy Officer(s), Legal | Chief Privacy Officer | — | Group DPO | Privacy Operations Lead; Management Board (material changes) |
| G4.2 — Authority Access Requests (prosecutors, courts, tax authorities; requests forwarded by processors under SCC Clause 15) | General Counsel, Privacy Officer(s) | General Counsel | — | Group DPO, CISO | Chief Privacy Officer, relevant Processing Owner |
| G5 — Developing Policies and Standards | Privacy Operations Lead | Chief Privacy Officer | Management Board (Supervisory Board consent for the Charter only) | Group DPO (C\*), General Counsel, CISO, Processing Owners | Risk Committee of the Supervisory Board, all roles |
| G5.1 — Privacy Notices: framework and Customer Privacy Notice | Privacy Officer(s), General Counsel | Chief Privacy Officer | Management Board for the Customer Privacy Notice (Document 1) | Group DPO (C\*) | Processing Owners |
| G5.1 — Privacy Notices: content for a processing activity | Privacy Officer(s), business unit | Relevant Processing Owner | — | Group DPO (C\*), General Counsel | Chief Privacy Officer |
| G6.1 — Compliance Monitoring and DPO-Organised Audits | Group DPO, Privacy Officer(s) under DPO direction | Group DPO | — | Chief Privacy Officer, General Counsel, auditees | Management Board; Audit Committee where the Group DPO considers it necessary; Group Internal Audit |
| G6.2a — Internal-Audit Charter, Risk-Based Audit Plan (including privacy audits) and Significant Plan Changes | Group Internal Audit | Chief Audit Executive | Audit Committee of the Supervisory Board (approves) | Management Board, Chief Privacy Officer, Group DPO (input to risk assessment) | Risk Committee of the Supervisory Board |
| G6.2b — Independent Assurance Opinion on the Programme | Group Internal Audit (supplemented by an external audit firm for specialist PET topics) | Chief Audit Executive | — | Group DPO, Chief Privacy Officer (as auditees) | Audit Committee of the Supervisory Board, Management Board |
| G7 — Metrics and KPIs | Privacy Operations Lead | Chief Privacy Officer | — | Group DPO | Management Board, Risk Committee of the Supervisory Board |
| G8.1 — Programme Reporting | Privacy Operations Lead | Chief Privacy Officer | — | Group DPO | Management Board, Risk Committee of the Supervisory Board |
| G8.2 — Group DPO Annual and Ad-Hoc Report to the Management Board | Group DPO | Group DPO | — | — | Management Board; Risk Committee where the Group DPO considers it necessary; Chief Privacy Officer |
| G9 — Processing Owner Mandate Designation | Privacy Operations Lead (proposal and Document 25 entry) | Chief Privacy Officer | Management Board (designates the holder and the delegated tier) | Group DPO, General Counsel | The designated head, Privacy Risk Committee (management level), Data Protection Coordinator of the line; Risk Committee of the Supervisory Board (oversight) |

## **5. RACI — Core Processes (C1–C5)**

Subsections 5.1–5.5 are numbered in accordance with the current version of the Privacy Governance Process Map (Document 24): 5.1, "Risk Calculation Project Development," corresponds to core process C1, 5.2 to C2, 5.3 to C3, 5.4 to C4, and 5.5 to C5. At each subsequent revision of the process map (Section 9), the numbering of this section is brought into alignment within the same review cycle. The mandatory gates G-L, G-DPIA, G-36 and G-TIA apply exactly as worded in Part A, Section 5.

***5.1 Risk Calculation Project Development (C1)***

The scoring model is presented as an illustrative example of a risk calculation project; the project development process applies equally to any risk calculation project at PanEuropean, regardless of product or business line. A "non-standard" project is one whose configuration falls outside the parameter ranges pre-approved in the methodology (Document 18).

| Activity | R | A | D | C | I |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Preparing the risk calculation project charter (e.g., for a new scoring model) in PEP | Privacy Engineer(s) | Privacy Operations Lead | — | Group DPO | Credit Decisions |
| Determining Whether the Configuration Is Standard | Privacy Engineer(s) | Privacy Operations Lead | — | Group DPO | — |
| Approving the Project via the Standard Track | Privacy Engineer(s) | Privacy Operations Lead | — | — | Group DPO |
| Methodological Assessment of the Charter via the Non-Standard Track | Privacy Operations Lead, Privacy Engineer(s) | Chief Privacy Officer | — | Group DPO, General Counsel, CISO | Privacy Risk Committee |
| Deciding Whether to Approve a Non-Standard Project | Chief Privacy Officer | Chief Privacy Officer | Privacy Risk Committee | Group DPO | Management Board (material change to the methodology) |
| Registering the Project in the PEP Risk Calculation Project Register | Privacy Engineer(s) | Privacy Operations Lead | — | — | Credit Decisions, Group DPO |

***5.2 Data Request and Transformation (C2)***

The credit-scoring case (`DPIA-CS-TRAIN-01` for model training on synthetic data generated on PEP; `DPIA-CS-LAUNCH-01` for production scoring) is used below as a running illustrative example; the allocation applies equally to any processing activity at PanEuropean. The residual tier of the credit-scoring case is the one recorded in Document 18 and Document 19; this document only shows who decides at each tier.

| Activity | R | A | D | C | I |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Intake and Triage of a New Data Processing Request (e.g., a new scoring feature) | Privacy Officer(s) | Privacy Operations Lead | — | Head of Credit Decisions (Processing Owner) | Group DPO |
| G-L — Legal Compliance Gate (Art. 6 basis; Art. 9 condition; Art. 22(2)(a) contract necessity and Art. 22(3) safeguards for scoring) | Legal, Privacy Officer(s) | General Counsel | — | Group DPO (C\*) | Processing Owner, Chief Privacy Officer |
| C2.3 — Legitimate-Interest Assessment (Art. 6(1)(f), as part of G-L) | Privacy Officer(s) | General Counsel | — | Group DPO (C\*) | Processing Owner, Chief Privacy Officer |
| C2.2 — Children's Data Safeguards (e.g., app marketing features switched off for users under 16) | Privacy Officer(s), business unit | Relevant Processing Owner | — | General Counsel, Group DPO | Chief Privacy Officer |
| G-DPIA — DPIA Triage | Privacy Officer(s) | Processing Owner | — | Group DPO (C\*) | Privacy Operations Lead |
| Conducting the DPIA (e.g., `DPIA-CS-LAUNCH-01`) | Privacy Officer(s), Credit Decisions | Head of Credit Decisions (Processing Owner) | — | Group DPO (C\*), CISO, General Counsel | Chief Privacy Officer |
| Group DPO Advice on the DPIA | Group DPO | Group DPO | — | — | Processing Owner, Chief Privacy Officer |
| Selecting an Existing Risk Calculation Project from the PEP Register | Privacy Officer(s) | Privacy Operations Lead | — | — | Group DPO |
| Selecting and Applying PET Techniques via PEP | Privacy Engineer(s) | Privacy Operations Lead | — | CISO, IT Management | Group DPO |
| Developing/Configuring a New PET Technique on PEP (when existing techniques are insufficient) | Privacy Engineer(s) | Chief Privacy Officer | Privacy Risk Committee (material change to the methodology) | Group DPO, IT Management | Management Board |
| Calculating Residual Risk and Proposing Mitigation Measures | Privacy Officer(s), Privacy Engineer(s) | Privacy Operations Lead | — | Group DPO (C\*), General Counsel, CISO | Processing Owner |
| Accepting Residual Risk — Low | Processing Owner | Processing Owner | — | Group DPO (C\* where a DPIA exists) | Chief Privacy Officer |
| Accepting Residual Risk — Medium | Processing Owner | Processing Owner | Chief Privacy Officer (concurrence) | Group DPO (C\*) | Privacy Risk Committee |
| Accepting Residual Risk — High | Processing Owner (proposes) | CRO (named Management Board member); for the classes of decision that the Management Board's written delegation assigns to it, the Privacy Risk Committee instead — each decision record names one | — | Group DPO (C\*), General Counsel, Chief Privacy Officer | Risk Committee of the Supervisory Board |
| Critical — Stop or Redesign | Processing Owner | Processing Owner | Management Board (only if high risk remains after redesign and the bank proposes to proceed; G-36 evaluated and, where met, consultation first) | Group DPO (C\*), General Counsel, Chief Privacy Officer | Risk Committee of the Supervisory Board |
| G-36 — Evaluation of the Art. 36 Test (recorded with reasons, for every DPIA) | Legal | General Counsel | — | Group DPO (C\*) | Processing Owner, Chief Privacy Officer |
| G-36 — Prior Consultation with the HBDI (lead SA) where the test is met or internal policy routes the case | Chief Privacy Officer, Processing Owner | CRO (named Management Board member) | — | Group DPO (C\*; contact point for the HBDI), General Counsel | Risk Committee of the Supervisory Board |
| Compiling the Evidence Pack (`EVP-YYYY-NNNN`) | Privacy Engineer(s) / Privacy Officer(s) | Privacy Operations Lead | — | — | Processing Owner, Group DPO |

***5.3 Data Subject Rights (C3)***

| Activity | R | A | D | C | I |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Intake and Verification of the Customer Request (including "Request a Review") | Privacy Officer(s) | Privacy Operations Lead | — | General Counsel | Group DPO |
| Assessing the Scope and Method of Fulfilling the Request | Privacy Officer(s) | Privacy Operations Lead | — | Digital Banking, IT Management, General Counsel | Group DPO |
| Fulfilling Access, Rectification, Erasure, Restriction, Portability and Objection Requests | Digital Banking / IT Management | Privacy Operations Lead | — | General Counsel | Relevant Processing Owner |
| Human Review of an Automated Credit Decision (Art. 22(3)) | Credit Decisions credit officers with authority to change the decision | Head of Credit Decisions (Processing Owner) | — | Group DPO (on request) | Privacy Operations Lead |
| Refusal, Extension or Restriction of a Request (including AML tipping-off restrictions under national law) | Privacy Officer(s) | Privacy Operations Lead | — | General Counsel, Group DPO, AML Officer | Relevant Processing Owner |
| Final Response to the Customer (within one month, extendable under Art. 12(3)) | Privacy Officer(s) | Privacy Operations Lead | — | — | Group DPO |
| Customer Contacts and Complaints Addressed to the Group DPO (Art. 38(4)) | Group DPO | Group DPO | — | Privacy Operations Lead (only as the Group DPO decides is needed to resolve the matter; confidentiality safeguard applies) | Chief Privacy Officer (aggregate or redacted reporting unless the Group DPO decides otherwise) |

> **Guidance — confidentiality of the Group DPO's work (Art. 38(5); WP243 rev.01, §2.6).** Where the Chief Privacy Officer, the Privacy Operations Lead or anyone else appears as "I" or "C" on a row performed by the Group DPO, this never means automatic disclosure of the content of a request made to the Group DPO or of the requester's identity. Disclosure follows need-to-know, purpose limitation, and secrecy or confidentiality under Art. 38(5) and applicable law; redaction or aggregate reporting is used where appropriate. The Group DPO decides how its own work is distributed. This does not prevent the Group DPO from investigating matters or discussing them with management.

***5.4 Cross-Border Data Transfer (C4; example: remote technical support by Example Cloud Services Pvt Ltd, India — `TIA-CLOUD-01`)***

Example Cloud Services Pvt Ltd is fictional. Remote access to production systems from India is a transfer (EDPB Guidelines 05/2021). The Processing Owner for this case is the CIO. The outcome of `TIA-CLOUD-01` is recorded in Document 20; this table shows only who does what.

| Activity | R | A | D | C | I |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Identifying a Cross-Border Transfer Within the Data Flow (including remote access) | Privacy Engineer(s) | Privacy Operations Lead | — | IT Management, CISO, General Counsel | Group DPO |
| Mechanism Check (no adequacy decision for India; SCCs under Art. 46) and TIA — Laws and Practices of India (`TIA-CLOUD-01`) | Legal, Privacy Officer(s) | General Counsel | — | Group DPO (C\*), CISO | CIO (Processing Owner), Chief Privacy Officer |
| Selecting the Transfer Tool (Standard Contractual Clauses) and Designing Supplementary Measures | Legal (contractual), CISO (technical) | CIO (Processing Owner) | — | Group DPO, Privacy Engineer(s) | Privacy Operations Lead |
| G-TIA — Determination Whether Essentially Equivalent Protection Is Ensured | Legal | General Counsel | — | Group DPO (C\*) | CIO, Chief Privacy Officer, Management Board |
| Decision to Proceed — only if G-L and G-TIA are passed and any DPIA/G-36 step is complete | CIO (Processing Owner) | Single decider under Section 7: CIO (Processing Owner) up to Medium; CRO for High — the decision record names one | — | Group DPO (C\*), Chief Privacy Officer | Privacy Risk Committee |
| Suspension or Termination where Equivalence Can No Longer Be Ensured | CIO, Legal | CIO (Processing Owner) | — | Group DPO | Chief Privacy Officer, Management Board |
| Periodic Re-Evaluation of the TIA | Legal, Privacy Officer(s) | General Counsel | — | Group DPO | CIO |

***5.5 Consent Management (C5)***

E-mail and push marketing is used below as the example. For the other consent purposes the Processing Owner is the Head of Digital Banking (personalised-offers pilot; app biometric log-in) and the Head of Insurance Distribution (PPI health data); the rows apply to them in the same way.

| Activity | R | A | D | C | I |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Designing the Consent Request for Marketing Communications and Profiling | Marketing | Head of Marketing (Processing Owner) | — | General Counsel, Group DPO | Privacy Operations Lead |
| Collecting Consent for Marketing Communications | Marketing | Head of Marketing (Processing Owner) | — | General Counsel | Group DPO |
| Storing and Recording Consent in the Consent Management System (CMS; separate from the CRM) | Privacy Engineer(s) / IT Management | Privacy Operations Lead | — | — | Group DPO |
| Processing Consent Withdrawal | Marketing / IT Management | Head of Marketing (Processing Owner) | — | — | Privacy Operations Lead, Group DPO |

## **6. RACI — Supporting Processes (S1–S9) and Statutory Activities**

| Process (Document 24) | R | A | D | C | I |
| :---- | :---- | :---- | :---- | :---- | :---- |
| S1 — Data Classification (including special categories for payment protection insurance) | Data Governance | CDO | — | Chief Privacy Officer, Group DPO, Privacy Engineer(s), General Counsel, CISO | Privacy Operations Lead |
| S2.1 — Retention Schedule | Privacy Operations Lead, Legal | Chief Privacy Officer | Management Board (as policy, G5) | Group DPO, Processing Owners | All roles |
| S2.2 — Retention and Disposal Execution | Digital Banking / IT Management | Relevant Processing Owner | — | General Counsel | Group DPO, Privacy Operations Lead |
| S3 — Data Inventory (Data Catalogue) | Data Governance | Privacy Operations Lead | — | Privacy Engineer(s), Processing Owners | Group DPO, Chief Privacy Officer |
| S4 — Record of Processing Activities (RoPA) | Privacy Officer(s) | Privacy Operations Lead | — | Processing Owners (confirm entries), Data Governance | Group DPO, Chief Privacy Officer |
| S5 — Privacy Risk Register ("Conduct & Privacy Risk") | Privacy Operations Lead | Chief Privacy Officer | — | Processing Owners, Group DPO, CISO, CRO | Management Board, Risk Committee of the Supervisory Board |
| S6.1 — Vendor Privacy Due Diligence (core banking platform provider, Example Cloud Services Pvt Ltd, Example AI Provider Inc.) | Privacy Officer(s), Procurement | Privacy Operations Lead | — | CISO, General Counsel | Group DPO |
| S6.2 — Engaging a Processor (Art. 28 contract) or Sharing Data with an Independent Controller (data-sharing agreement — e.g., EuroCredit Bureau) | Procurement, Legal | Relevant Processing Owner | — | Group DPO, CISO, Chief Privacy Officer | Management Board (arrangements for ICT services supporting critical or important functions under DORA) |
| S6.3 — Corporate Transactions (M&A): Privacy Due Diligence and Data Migration — no transaction in progress at 26 October 2026 | General Counsel, Privacy Officer(s); the Chief Privacy Officer leads the privacy workstream | Processing Owner of the transaction | — | Group DPO, CISO | Management Board |
| S7.1 — Security Event Detection, Triage and Containment | CISO / SOC | CISO | — | Privacy Operations Lead | Group DPO |
| S7.2 — Personal Data Breach Qualification and Recording (every breach) | Privacy Officer(s) | Chief Privacy Officer | — | Group DPO, CISO, General Counsel | Relevant Processing Owner |
| S7.3 — GDPR Notification Decision (Art. 33 to the HBDI as lead SA; Art. 34 to customers) | Chief Privacy Officer | CRO (designated Management Board member; deputy: COO) | — | Group DPO (C\*; contact point for the HBDI), General Counsel, CISO | Risk Committee of the Supervisory Board, relevant Processing Owner |
| S7.4 — DORA Major ICT-Related Incident Classification and Reporting to the Financial Supervisor (ECB/BaFin) | ICT Risk Control function, CISO | Head of ICT Risk Control | — | Chief Privacy Officer, Group DPO (where personal data are involved) | Management Board, Risk Committee of the Supervisory Board |
| S7.5 — Processor Extension: Notifying a Client Controller of a Breach (where PanEuropean acts as processor, e.g., payment services operated for a group company under an Art. 28 contract) | Privacy Officer(s), CISO | Head of Payment Services (owner of the client service; RoPA-P-PAY-01) | — | General Counsel (contract terms), Group DPO | Chief Privacy Officer |
| S8 — Staff Training on Privacy | HR (delivery) / Privacy Operations Lead (content) | Chief Privacy Officer | — | Group DPO | All roles |
| S8.1 — Group DPO Awareness-Raising Activities | Group DPO | Group DPO | — | Privacy Operations Lead | Chief Privacy Officer |
| S9 — Operating the PEP Platform | Privacy Engineer(s) | Privacy Operations Lead | — | IT Management, CISO | Group DPO, Chief Privacy Officer |

***Statutory activities outside the G/C/S rows***

| Activity | R | A | D | C | I |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Designating the Group DPO and Communicating the Contact Details to the HBDI (Art. 37(1), (7)); Removal of the Group DPO | Chief Privacy Officer, HR | Management Board | Management Board (removal: with the Supervisory Board's consent, reserved matter) | General Counsel | Risk Committee of the Supervisory Board, Group DPO, all staff |
| Ensuring Group DPO Resources, Access and Independence (Art. 38) | Chief Privacy Officer | Management Board | — | Group DPO | Risk Committee of the Supervisory Board |
| G4.1(b) — Cooperation with the HBDI and Concerned SAs; Contact Point | Group DPO | Group DPO | — | General Counsel, Chief Privacy Officer | Management Board |
| G4.1(a) — Bank Response to SA Inquiries, Investigations and Orders | Legal, Privacy Operations Lead | Chief Privacy Officer | Management Board (where the response commits the bank) | Group DPO (C\*) | Risk Committee of the Supervisory Board |
| C2.3 — Joint-Controller Arrangement for the Federated-Learning Anti-Fraud Consortium (Art. 26) | Legal | Head of Fraud Prevention (Processing Owner) | — | Group DPO, Chief Privacy Officer | Privacy Operations Lead |
| C2.1 — AI Act Deployer Duties for Credit Scoring, including the Fundamental Rights Impact Assessment — interface only | Model Risk / AI governance function | Head of Credit Decisions (Processing Owner) | — | Group DPO, General Counsel | Chief Privacy Officer |

## **7. Residual-Risk Acceptance Authority and Escalation**

This section applies only after G-L has been passed.

| Residual Tier (Document 8) | Who May Accept | Additional Mandatory Step | Timeframe |
| :---- | :---- | :---- | :---- |
| Low | Processing Owner | Record in the evidence pack. Group DPO advice where a DPIA exists. | — |
| Medium | Processing Owner, with the Chief Privacy Officer's concurrence | Group DPO advice recorded. Conditional acceptance carries an expiry date and is re-assessed on expiry. | 3 business days |
| High | The CRO as the named Management Board member; for the classes of decision that the Management Board's written delegation assigns to it, the Privacy Risk Committee instead. Each decision record names one decider — for example, the launch of a new scoring feature based on behavioural data | G-36 evaluated and recorded by General Counsel with Group DPO advice; prior consultation with the HBDI whenever the Art. 36 test is met. **Internal policy (not a GDPR obligation):** every residual High is routed to consultation unless General Counsel records, with reasons and Group DPO advice, that the Art. 36 test is not met. Group DPO advice recorded. Risk Committee of the Supervisory Board informed. | 5 business days; where consultation takes place, processing does not start before the HBDI's written advice or the end of the Art. 36(2) period (extended or suspended as the case may be), and never in breach of an Art. 58 measure; an elapsed period is not an authorisation |
| Critical | Not acceptable | Stop or redesign — for example, a proposal to use payment-transaction data for a behavioural pricing feature whose residual risk remains critical after the proposed measures. If high risk remains after redesign, the G-36 test is evaluated and, where met, consultation with the HBDI precedes any processing; the decision sits with the Management Board. The Supervisory Board's consent is not required unless its rules of procedure so provide. | Immediately |

A personal data breach is not a residual-risk acceptance decision: notification follows S7.3 and Document 14.

***When the decision-maker does not follow Group DPO advice***

* The decision-maker records the reasons for departing from the Group DPO's advice in the evidence pack before the decision takes effect
* The Group DPO may escalate directly to the Management Board and informs the Risk Committee of the Supervisory Board if the Group DPO considers it necessary; escalation does not transfer the decision to the Group DPO
* Neither the content of the Group DPO's advice nor the fact of escalation may be used to the Group DPO's detriment (Art. 38(3) GDPR; §38(2) with §6(4) BDSG)

The threshold values separating the residual risk levels from one another are determined exclusively by the PanEuropean Privacy Risk Appetite Statement and are not redefined here. The escalation rule does not replace the conflict-resolution matrix of the Interface & Integration Model (Section 5) — that matrix applies to general disagreements between the privacy function and another corporate function (e.g., the CDO), whereas this section governs specifically the acceptance of residual risk and the handling of Group DPO advice — a specialised procedure established by the PanEuropean Charter (Section 8), not a general cross-functional mechanism.

## **8. Relationship to Other Framework Documents**

This document builds on the Privacy Governance Process Map (Document 24) and allocates responsibility for the processes and activities listed there. This document:

* Is the primary source for the PanEuropean Process Owner Register (Document 25) — the latter is not maintained independently but is generated as a projection of this matrix

* Is operationalised in the PanEuropean Operational Role & Staffing Model (Document 26) — there, the roles in this matrix are mapped to specific filled positions (for example, "Privacy Officer, Germany" — a named individual)

* The acceptance authority (Section 7) is tied to the tiers of the PanEuropean Privacy Risk Appetite Statement (Section 5) and does not redefine the thresholds

* The list of roles (Section 3) is aligned with the Charter, the Organisational Design Strategy (Document 4), and the Interface & Integration Model (Document 3)

* Records the RACI for designating the Processing Owner mandate (G9, Section 4); the mandate is established by the PanEuropean Charter (Section 8); the role profile is in Document 6, Section 4.6; the register of current mandate holders is Document 25, Section 10

## **9. Review and Amendment**

This document is reviewed under the terms established by the principle of continuous improvement (Charter, Section 7) and the Policy Review Cycle, and also whenever the Privacy Governance Process Map (Document 24), the delegated risk-acceptance tiers, or the organisational structure of the privacy function (Document 4) changes. Amendments are prepared by the Chief Privacy Officer, with Group DPO advice, and adopted by the Management Board; the Risk Committee of the Supervisory Board is informed.

## **10. Approval**

Version 4.0 of this document was adopted by the Management Board of PanEuropean Bank AG on 20 October 2026, on the proposal of the Chief Privacy Officer and after Group DPO advice; the Risk Committee of the Supervisory Board was informed at its meeting of 23 October 2026. Document owner: Chief Privacy Officer. Earlier versions are listed in the fictional document history above.

# **Normative Basis and References**

* Regulation (EU) 2016/679 (GDPR): Arts. 5(2), 24 (controller accountability); 26 (joint controllers); 28 (processors); 33–34 (breach notification and communication); 35–36 (DPIA, prior consultation); 37–39 (DPO designation, position and tasks); Chapter V and Art. 44 (transfers).
* Article 29 Working Party, Guidelines on Data Protection Officers, WP243 rev.01 (endorsed by the EDPB), in particular §3.3 (instructions and independence), §3.4 (dismissal or penalty), §3.5 (conflict of interests), §2.6 (confidentiality, Art. 38(5) — reference for the confidentiality safeguard on DPO rows) and §4.1–4.2 (monitoring compliance; DPIA role).
* Article 29 Working Party, Guidelines on DPIA, WP248 rev.01 (nine criteria).
* CJEU C-453/21 *X-FAB Dresden* (9 February 2023) — conflict of interests assessed case by case; Member State dismissal protection; CJEU C-534/20 *Leistritz* (22 June 2022).
* EDPB, Coordinated Enforcement Action 2023 — Designation and position of data protection officers, report adopted 16 January 2024.
* CJEU C-311/18 *Schrems II*; EDPB Recommendations 01/2020 on supplementary measures; EDPB Guidelines 05/2021 on the interplay between Art. 3 and Chapter V.
* Regulation (EU) 2022/2554 (DORA), Arts. 5, 17–19 (management body responsibility; ICT-related incident management and reporting) — separate track for financial entities.
* German Stock Corporation Act (AktG) §111 (Supervisory Board supervises the management; §111(4) reserved consent); Federal Data Protection Act (BDSG) §38(2) with §6(4) (DPO dismissal protection) — Part B only.

# **International Adaptation**

| Jurisdiction | What changes in this matrix |
| :---- | :---- |
| UK (UK GDPR, DPA 2018 as amended by the DUAA 2025) | Headline: the DPO regime of UK GDPR Arts. 37–39 and the allocation model above apply; the competent authority is the ICO. |
| Switzerland (revFADP) | Headline: a data protection advisor is optional for private controllers (revFADP Art. 10). Where one is appointed and meets the independence conditions, the controller may consult the advisor instead of the FDPIC after a high-risk DPIA (Art. 23(4)); show that consultation in the G-36 row. |
| Canada — PIPEDA | The individual accountable for compliance under Principle 4.1 (the "Privacy Officer") is typically the EPPO in this matrix and may hold "A" for programme rows. That person is **not** an EU DPO: do not transfer the DPO's independence restrictions automatically, and do not assign the Privacy Officer the DPO-only rows. Breach rows follow PIPEDA (real risk of significant harm; report to the OPC and notify individuals as soon as feasible; records of every breach of security safeguards for 24 months); the GDPR 72-hour clock does not apply. |
| Canada — Québec (P-39.1) | The person exercising the highest authority is the person in charge of the protection of personal information by default and may delegate the function in writing; record the delegation in G9-style rows. Add rows for the privacy impact assessment before communicating personal information outside Québec, the confidentiality-incident register (all incidents) and notification of the Commission d'accès à l'information where there is a risk of serious injury. |

# **Document History (PGF)**

| Release | Date | Summary |
| :---- | :---- | :---- |
| 1.0.0-rc.1 | 2026-10-26 | Canonical English Markdown; changes from internal ver.2: role model re-baselined by decision type (EPPO, Processing Owner, Executive Management, Governing Body, Independent Internal Audit, Legal, CISO added; DPO limited to its statutory tasks and C\* on every DPIA); Approve/Decide column added; mandatory gates G-L, G-DPIA, G-36, G-TIA added as rows; residual-risk acceptance table aligned with EDITORIAL_RULES §4.3 (High → one named Executive Management decider, with G-36 evaluated for every DPIA and prior consultation whenever the Art. 36 test is met; Critical not acceptable); G6 split into DPO compliance monitoring and Internal Audit assurance, with the Audit Committee approving the internal-audit charter and plan; Art. 38(5) confidentiality safeguard for DPO rows; processor extension row for Art. 33(2); G9 designation by Executive Management (no self-appointment); G-TIA branched by mechanism (Art. 45 adequacy check / Art. 46 TIA plus supplementary measures / Art. 49 documented conditions); transfer cannot proceed after a failed G-TIA; GDPR breach notification separated from DORA reporting; Art. 22(3) human review assigned to the deciding business line; the generic oversight label of ver.2 replaced by named bodies; Processing Owner added to the role list; example dates shifted by −12 months; normative basis and international adaptation added. Integration pass: rows with a single "A" for the Document 24 sub-processes G4.1, G4.2, G5.1, C2.1, C2.2, C2.3 and S6.3; Part B Processing Owner list aligned with Document 25, Section 10; consent management system (CMS) named in C5; cross-reference to the master escalation matrix (Document 31). |
