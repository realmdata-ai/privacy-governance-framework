---
title: "Cross-Border Data Transfer Policy"
document_id: PGF-12
level: 2
release_version: 1.0.0-rc.1
status: release-candidate
authors: ["Alexey Neyman", "Val Khvatov"]
regulatory_reference_date: 2026-10-26
licence_proposed: "CC BY 4.0 (proposed; subject to rights-holder confirmation)"
source_provenance: "Derived from internal source set ver.2: Level2/12. Cross-Border-Data-Transfer-Policy_ENG.docx.md; sha256 6132bf8108b24179e042a0fcfd133fed981aebf93d9dfc6a19890d687c4e01b1"
---

# PGF-12 — Cross-Border Data Transfer Policy

*Privacy Governance Framework (PGF) · Level 2 — Policies and Standards · Release 1.0.0-rc.1 · Regulatory reference date: 26 October 2026*

> **Status and use.** Part A is a reusable template. Part B is a worked example for a fictional organisation (PanEuropean Bank AG); all names, figures, dates and records in Part B are illustrative. Nothing in this document is legal advice or a statement about any real organisation, product or provider.

# **About This Document**

**Purpose.** Document 12 sets the organisation's rules for transfers of personal data under Chapter V GDPR: what counts as a transfer, which mechanism may be used (Art. 45, 46 or 49), when the transfer-equivalence gate (G-TIA) passes or fails, what happens when equivalence cannot be ensured, how privacy-enhancing technologies and joint-processing architectures are treated, how onward transfers and sub-processors are controlled, and how public-authority requests are handled.

**Scope.** Every flow of personal data that meets, or may meet, the three cumulative criteria of a transfer (Section 2). The procedure for transfer impact assessments (TIAs) is in Document 20; this document sets the policy that Document 20 applies.

**Relationships.** Document 20 (Transfer Impact Assessment Methodology) — triage, TIA procedure, transfer-status conclusions; Document 7 — recipient countries and jurisdiction particulars; Document 10 — data class and data state; Document 17 — counterparty due diligence and processor contracts; Documents 19 and 18 — DPIA and risk calculation, which may run in parallel with a TIA; Document 21 — RoPA; Document 5, Section 5.4 — roles in core process C4.

# **How to Use This Document**

Part A is a template. Text in ***[square brackets, bold italic]*** is a fill-in or illustrative placeholder. Blocks marked **Guidance** are removed from the adopted version. Part B shows the template completed for the fictional PanEuropean Bank AG; the providers named there — Example Cloud Services Pvt Ltd, Example AI Provider Inc. and the partner bank — are fictional, and their attributes are illustrative assumptions.

> **Guidance.** Build on the Regulatory Applicability Matrix (Document 7) and the Data Classification Policy (Document 10). Use the gate wording of Section 7 exactly as stated: the same wording appears in Documents 5, 8, 18, 19 and 20.

# **Table of Contents**

**About This Document**
**How to Use This Document**
**Part A — Template**
1. Purpose
2. Scope and What Is a Transfer
3. Privacy-Enhancing Technologies, Joint-Processing Architectures and Remote Access
4. Transfer Mechanisms (4.1 Adequacy; 4.2 Appropriate Safeguards; 4.3 Derogations; 4.4 Onward Transfers and Sub-processors; 4.5 Requests from Third-Country Authorities)
5. "Recipient → Mechanism → Basis" Matrix
6. Conditions Triggering a TIA or Re-Evaluation
7. G-TIA Outcome, Supplementary Measures, Suspension and Public-Authority Access
8. Documentation in the RoPA
9. Roles and Responsibilities
10. Relationship to Other Framework Documents
11. Review and Amendment
12. Approval
**Part B — Worked Example: PanEuropean Bank AG** (same structure)
**Normative Basis and References**
**International Adaptation**
**Document History (PGF)**

# **Part A — Template**

**Cross-Border Data Transfer Policy of *[Legal name of organisation]***

*Effective date: **[DD Month YYYY]**  ·  Version: **[x.x]**  ·  Document owner: **[Executive Privacy Programme Owner (EPPO)]**  ·  Legal owner of transfer assessments: **[Legal]**  ·  Adopted by: **[Executive Management]***

***Version History***

| Version | Date | Changes |
| :---- | :---- | :---- |
| ***[1.0]*** | ***[DD Month YYYY]*** | ***[First version of the document]*** |
| ***[x.x]*** | ***[DD Month YYYY]*** | ***[Brief description of material changes]*** |

## **1. Purpose**

This document establishes the rules and permissible mechanisms for transfers of personal data to importers in third countries or to international organisations, and the decisions that must be taken before a transfer starts, while it continues and when it must stop. ***[Where the organisation is also subject to other transfer regimes (for example UK, Swiss or Canadian law), add them under the International Adaptation box.]***

## **2. Scope and What Is a Transfer**

**2.1 The three cumulative criteria.** A flow of personal data is a transfer under Chapter V when all three criteria of EDPB Guidelines 05/2021 (version 2.0, Section 2.2) are met:

1. the exporter — a controller or processor — is subject to the GDPR for the given processing;
2. the exporter discloses by transmission or otherwise makes the personal data available, including by remote access, to **another** controller, joint controller or processor (the importer);
3. the importer is in a third country, irrespective of whether it is itself subject to the GDPR for the processing, or is an international organisation.

A transfer is not defined by geography alone. An ordinary flow between recipients established in the EEA is not a Chapter V transfer because criterion 3 is not met; but an international organisation can be an importer wherever it is located, and the three criteria are applied to every flow, including within a group.

**2.2 Typical cases.**

* ***[Remote access by an employee of the same legal entity — for example, while travelling — is not a transfer, because the data are not made available to another controller or processor (EDPB Guidelines 05/2021, Example 8.1). Security and the other GDPR obligations still apply; the risks of access from a third country are addressed under Art. 32 and, where relevant, in the DPIA.]***
* ***[Remote access by a separate legal entity in a third country — a service provider, or another entity of the same group — to data held in the EEA is a transfer. A separate group entity can be an importer. The organisation never states that "any remote access is a transfer"; it applies the three criteria.]***
* ***[Onward transfers by an importer, and access by a sub-processor in a third country, are transfers in their own right (Section 4.4).]***
* ***[Customer-instructed flows (for example international payments to a beneficiary's bank) are assessed under the three criteria and, where they are transfers, under a mechanism of Section 4.]***

**2.3 Data states.** Pseudonymised, encrypted, tokenised and synthetic data remain personal data in the controller's hands until the controller concludes otherwise (Document 10, Section 4.3). The realistic means of the importer are part of the contextual analysis of whether data made available to it are personal data for it (CJEU C-413/23 P *EDPS v SRB*). That judgment does not decide generally that Chapter V stops applying whenever a recipient cannot attribute the data: ***[Legal]*** assesses the exporter's and controller's perspective, any processor's role and the full flow — including onward access and access by authorities of the destination — separately. A processor path is never declared outside the GDPR or outside Chapter V merely because the processor lacks the key. While the legal conclusion is unclear, the flow is treated as a transfer.

**2.4 Anonymous information.** Information that the controller has concluded is anonymous information (Recital 26) is outside Chapter V while the conclusion stands. The conclusion is taken by ***[the Processing Owner]*** on ***[Legal]***'s assessment, with DPO advice, supported by the PET Assessment Module of Document 18 (Section 3.3), and it names the recipients considered; it is re-assessed periodically (Document 11, Section 3.1). Synthetic datasets without such a conclusion are personal data and remain within this document.

**2.5 Other duties in parallel.** A transfer is also processing: G-L (lawful basis, transparency, Art. 9 and Art. 10 conditions, Art. 22) and, where triggered, a DPIA and the Art. 36 test apply in parallel with this document (Documents 19 and 20). A Chapter V mechanism is not a lawful basis.

* The unit of regulation is the combination of importer, destination, transfer tool and data categories; the RoPA (Document 21) records each transfer at process level and refers to this document and to the TIA (Document 20).

## **3. Privacy-Enhancing Technologies, Joint-Processing Architectures and Remote Access**

> **Guidance.** Federated learning, secure multi-party computation, private set intersection, homomorphic encryption, trusted execution environments, differential privacy and remote-access arrangements create a temptation to assume that, because records do not "physically" cross the border, Chapter V does not apply. That assumption is not made.

* ***[PETs, trusted execution environments, homomorphic encryption and remote access are **not** automatic exemptions from Chapter V (EDPB Guidelines 05/2021). Where a flow is a transfer, a PET is assessed as a possible **supplementary measure** under Art. 46 (EDPB Recommendations 01/2020) — never as a substitute for a mechanism.]***
* ***[Whether a scheme involves a transfer is decided by a **transfer-status conclusion** recorded by [Legal] on documented evidence, with DPO advice (Document 20, Section 3.3). The conclusion applies the three criteria of Section 2.1 and the data-state rules of Section 2.3. Evidence may include PET Assessment Module results (Document 18, Section 3.3) and a cryptographic or architectural review; a numerical threshold is evidence, not a legal criterion. The DPO advises and does not make the determination.]***
* ***[Where the conclusion is that the scheme is a transfer, or where it cannot be reached with confidence, the scheme is treated as a transfer and Section 4 applies. Where the conclusion is that it is not a transfer, G-L, the RoPA and DPIA duties still apply.]***
* ***[A DPIA and the Art. 36 test may be required in parallel with a TIA for the same scheme.]***

| Scheme / Process | Artefact or Access Crossing a Boundary | Transfer-Status Conclusion (Legal, with DPO advice) | Mechanism and Supplementary Measures | Evidence | Re-Assessment |
| :---- | :---- | :---- | :---- | :---- | :---- |
| ***[E.g. federated learning for process X]*** | ***[Model updates]*** | ***[Transfer / not a transfer / treated as a transfer pending conclusion]*** | ***[Art. 46 tool + PET as supplementary measure, or "not applicable"]*** | ***[EVP-YYYY-NNNN]*** | ***[Triggers and frequency]*** |

***[A conclusion is re-assessed upon any change of participants, coordinator, hosting, parameters or technology, a new published attack relevant to the technique, a change in law, case law or guidance (including supervisory-authority practice on such schemes), and at least [annually]. A change of risk appetite does not change a legal conclusion.]***

## **4. Transfer Mechanisms**

G-TIA is branched by mechanism. G-L and DPIA duties apply under every mechanism.

***4.1 Art. 45 — Adequacy Decisions***

***[Check that the adequacy decision covers the destination, sector and recipient (scope and eligibility — for example, for the United States, the recipient's active certification under the EU-U.S. Data Privacy Framework for the data concerned), that it remains valid, and monitor it (amendment, suspension, repeal, annulment). There is no statutory obligation to redo the Commission's assessment; any stricter internal review is labelled as internal policy.]***

***4.2 Art. 46 — Appropriate Safeguards***

* ***[Standard contractual clauses (Commission Implementing Decision (EU) 2021/914), in the module matching the parties' roles: Module 1 controller-to-controller, Module 2 controller-to-processor, Module 3 processor-to-processor, Module 4 processor-to-controller.]***
* ***[Binding corporate rules for transfers within a group of undertakings, or a group of enterprises engaged in a joint economic activity, approved by the competent supervisory authority under the consistency mechanism (Arts. 47, 63–64).]***
* ***[Approved codes of conduct or certification mechanisms with binding and enforceable commitments of the importer (Art. 46(2)(e)–(f)); contractual clauses or administrative arrangements authorised by the competent supervisory authority (Art. 46(3)).]***
* ***[Every Art. 46 transfer requires, before it starts, a TIA of the laws and practices of the destination as relevant to the transfer — public-authority access, enforceable rights and effective redress — and of the supplementary measures needed, with re-evaluation (CJEU C-311/18; EDPB Recommendations 01/2020, version 2.0, Step 2 and following; Document 20).]***

***4.3 Art. 49 — Derogations for Specific Situations***

***[Derogations are exceptional, interpreted restrictively and subject to the specific conditions of the derogation used, including occasional or non-repetitive limits where applicable (EDPB Guidelines 2/2018). They are not a substitute for a mechanism under Arts. 45 or 46 for a structural transfer where such a mechanism is available. Each use is supported by a derogation record (Document 20) stating the derogation, the facts showing that its conditions are met and, where the derogation requires it, why no Art. 45 or 46 mechanism is used. Any stricter internal rule is labelled as internal policy.]***

***4.4 Onward Transfers and Sub-processors***

* ***[An onward transfer by the importer to a third party in a third country, including to a sub-processor, is permitted only under the conditions of the transfer tool (for example the onward-transfer and sub-processing clauses of the SCCs) and is covered by the TIA or a new TIA (Document 20, Section 3.2).]***
* ***[Sub-processors of a processor are engaged only with the organisation's prior written authorisation (Art. 28(2)), specific or general, in the form set by the Vendor and Third-Party Privacy Risk Policy (Document 17). Under a general written authorisation, the processor informs the organisation of any intended addition or replacement at least [30] days in advance, giving it the opportunity to object; the organisation's decision is taken by [the Processing Owner], with DPO advice. Where the sub-processor is in a third country, the onward transfer is covered by an appropriate mechanism (for example SCC Module 3) and the TIA is re-evaluated before the sub-processor receives data.]***
* ***[The processor keeps an up-to-date list of sub-processors and provides it on request.]***

***4.5 Requests from Third-Country Authorities***

***[A judgment of a court or tribunal, or a decision of an administrative authority, of a third country requiring disclosure of personal data is recognised or enforceable only if based on an international agreement, such as a mutual legal assistance treaty, in force between the requesting third country and the Union or a Member State, without prejudice to other grounds for transfer under Chapter V (Art. 48). Requests received by the organisation directly are referred to [Legal] before any response.]***

## **5. "Recipient → Mechanism → Basis" Matrix**

> **Guidance.** One row per combination of importer, destination, tool and data categories, consistent with the recipient countries recorded in the Regulatory Applicability Matrix (Document 7, Section 3) and with the RoPA (Document 21). The matrix states the policy position; the TIA record (Document 20) holds the assessment.

| Recipient Country / IO | Importer and Role | Transfer Criteria Met? | Mechanism (Art. 45 / 46 / 49) | TIA / G-TIA | Basis Reference |
| :---- | :---- | :---- | :---- | :---- | :---- |
| ***[Country 1]*** | ***[controller / processor; intra-group / third party]*** | ***[Yes / No / treated as transfer]*** | ***[e.g. SCC Module 2]*** | ***[TIA ID; pass / fail; date]*** | ***[contract / decision]*** |

## **6. Conditions Triggering a TIA or Re-Evaluation**

* ***[A TIA is performed before any new Art. 46 transfer starts, and re-evaluated on the triggers of Document 20, Section 3.2: a new importer, destination, tool or sub-processor; an expansion of data categories or volume, including special-category or criminal-offence data; a change of purpose or of the technical scheme (including a move to or from a PET scheme); a relevant change in the laws or practices of the destination, a notification by the importer (for example under SCC Clauses 14(e) and 15) or a relevant judgment or guidance; a security incident or a public-authority request at the importer; and the scheduled re-evaluation, at least [annually].]***
* ***[Re-evaluation is tied to legal and monitoring events, not to the calendar of any tool or vendor certification.]***
* ***[For Art. 45 transfers, the adequacy check record is monitored; for Art. 49 transfers, the derogation record is re-checked for each use or at the frequency it states.]***

## **7. G-TIA Outcome, Supplementary Measures, Suspension and Public-Authority Access**

* ***[**G-TIA.** For an Art. 46 transfer, the TIA establishes whether, with supplementary measures, essentially equivalent protection is ensured. If it cannot be ensured, the transfer **does not start or is suspended**. Risk appetite, risk acceptance, a DPO opinion or a metric cannot override this: a failed G-TIA cannot be "accepted" by anyone. The G-TIA determination is made by [Legal], with DPO advice.]***
* ***[**Supplementary measures** are chosen for the specific problem identified in the TIA — for example encryption with keys held only in the EEA, pseudonymisation or tokenisation with the additional information kept in the EEA, split or multi-party processing, masking of data on screen, restriction of clear-text access to EEA-based staff — and their effectiveness against that problem is documented. Contractual and organisational measures alone are rarely sufficient against public-authority access.]***
* ***[**Decision to proceed.** Only after G-L and G-TIA have passed and any DPIA and G-36 step is complete, the single decider under Document 8, Section 5, takes the decision to proceed on the residual risk to rights and freedoms: the Processing Owner up to Medium (with EPPO concurrence at Medium), one named member of Executive Management for High; Critical is not acceptable.]***
* ***[**Suspension and termination.** Under the SCCs, the exporter suspends the transfer where it considers that no appropriate safeguards can be ensured, or if instructed by the competent supervisory authority (Clause 14(f)), and where the importer is in breach of the clauses or unable to comply (Clause 16(b)); it may terminate the contract as provided in Clause 14(f) or 16(c), and data already transferred are returned or deleted (Clause 16(d)). Where the exporter terminates under Clause 16(c), it informs the competent supervisory authority. These are duties of the exporter (the controller); the DPO is the supervisory authority's contact point. The competent supervisory authority may itself order the suspension of data flows (Art. 58(2)(j)). A suspended transfer resumes only after a new TIA and a passed G-TIA. Details — Document 20, Section 4.]***
* ***[**Parallel DPIA and Art. 36.** The SCC procedure above is not a prior consultation under Art. 36. Where the DPIA for the same processing indicates high residual risk, the G-36 test is evaluated in parallel (Document 19).]***
* ***[**Public-authority access requests.** The importer notifies [Legal] and the DPO promptly of any request or direct access by a public authority of the destination, unless prohibited by the law of that country, reviews the legality of the request, challenges it where there are grounds, and discloses the minimum permissible (SCC Clause 15). The organisation records each notification, its assessment and the outcome in the TIA record of the transfer (Document 20) — not in a separate register — and re-evaluates the TIA. Where the request or access is also a personal data breach, Document 14 applies in addition; every breach is recorded under Art. 33(5).]***

## **8. Documentation in the RoPA**

***[Every transfer is recorded in the RoPA (Document 21) at process level: importer and country (or international organisation), mechanism and, for Art. 49, the derogation and suitable safeguards documented (Art. 30(1)(e) and (2)(c)), with the TIA identifier (Document 20). The RoPA is the single list of active transfers; this document does not keep a separate register. A processing activity that involves a PET scheme concluded not to be a transfer remains in the RoPA as processing; its RoPA entry refers to the transfer-status conclusion and its evidence pack instead of a mechanism.]***

## **9. Roles and Responsibilities**

> **Guidance.** Roles follow the RACI Matrix (Document 5, Section 5.4, core process C4) and introduce no new role names.

| Role | Responsibility |
| :---- | :---- |
| ***[Privacy Operations Lead]*** | ***[Accountable for identifying transfers in the data flow (with Privacy Engineers responsible); initiates the TIA]*** |
| ***[Legal]*** | ***[Responsible and accountable for the TIA (laws and practices of the destination), the G-TIA determination, transfer-status conclusions, derogation and adequacy check records, and re-evaluation; contracts and maintains the transfer tools; informs the competent supervisory authority under Clause 16(c) where the exporter terminates]*** |
| ***[Processing Owner]*** | ***[Accountable for choosing the transfer tool and supplementary measures (with Legal and the CISO), for the decision to proceed up to Medium only after G-L and G-TIA pass, for suspension where equivalence cannot be ensured, and for decisions on sub-processor notifications]*** |
| ***[Executive Management (one named member)]*** | ***[Decides to proceed where the residual risk is High; informed of G-TIA failures and suspensions]*** |
| ***[DPO]*** | ***[Mandatory advice (C\*) on the TIA, G-TIA, transfer-status conclusions and the decision to proceed; contact point for the supervisory authority; monitors compliance. The DPO does not determine transfer status, select the mechanism or approve transfers]*** |
| ***[EPPO]*** | ***[Owns this document; concurs at Medium; informed of G-TIA outcomes]*** |
| ***[CISO / Information Security]*** | ***[Responsible for technical supplementary measures; consulted on identification and on the TIA]*** |
| ***[Privacy Officer(s) / Privacy Engineer(s)]*** | ***[Support Legal in preparing the TIA; identify transfers and PET-scheme artefacts in data flows]*** |
| ***[Procurement]*** | ***[Consulted on counterparty due diligence (Document 17); does not assess the transfer mechanism]*** |

## **10. Relationship to Other Framework Documents**

* Builds on the Regulatory Applicability Matrix (Document 7) and the Data Classification Policy (Document 10).
* Applied through the Transfer Impact Assessment Methodology (Document 20): triage, TIA, transfer-status conclusions, suspension.
* Uses the Privacy Risk Assessment Methodology (Document 18) only for the elements Document 20 requests (for example severity of harm if transferred data were disclosed; PET-module evidence on a de-identified artefact); Document 18 supplies no transfer decision.
* Roles — Document 5, Section 5.4; decision to proceed — Document 8, Section 5; gates — Documents 18 and 19.
* Documented in the RoPA (Document 21) and the Data Inventory (Document 23).
* Interacts with Document 11 (archives at a provider in a third country), Document 14 (incidents and public-authority access that are breaches), Document 16 (design choices that avoid or minimise transfers) and Document 17 (counterparty due diligence, processor contracts and sub-processor authorisation).
* Executed as conditional core process C4 on the Privacy Governance Process Map (Document 24).

## **11. Review and Amendment**

This document is reviewed under ***[the Policy Review Cycle, Document 29]*** and immediately upon a change in the status of an adequacy decision, a relevant judgment or guidance, or a relevant change in the law of a destination. Changes are adopted by ***[Executive Management]*** on the proposal of ***[the EPPO]***, after consulting ***[Legal]***, ***[the Privacy Risk Committee]*** and the DPO.

## **12. Approval**

This document was adopted by ***[Executive Management]*** on ***[date]***. Document owner: ***[EPPO]***.

# **Part B — Worked Example: PanEuropean Bank AG**

**PanEuropean Bank AG — Cross-Border Data Transfer Policy**

*Effective date: 20 October 2026  ·  Version: 2.0  ·  Document owner: Chief Privacy Officer (EPPO)  ·  Legal owner of transfer assessments: General Counsel  ·  Adopted by: Management Board, 20 October 2026*

*Fictional legal entity, provided solely for illustrative purposes.*

***Fictional Document History (illustrative)***

| Version | Date | Changes |
| :---- | :---- | :---- |
| 1.0 | 1 March 2026 | First version. Owner at the time: Group DPO |
| 2.0 | 20 October 2026 | Re-baselined to the new role model (Chief Privacy Officer as owner; General Counsel responsible for TIAs, G-TIA and transfer-status conclusions; Group DPO advice only); the former test for excluding PET schemes from Chapter V (numerical threshold, DPO determination and legal opinion) replaced by the three transfer criteria and transfer-status conclusions; the mutual-output PSI design suspended and replaced (Section 3); mechanism branches Art. 45/46/49 and the sub-processor rule aligned with Documents 17 and 20 |

## **1. Purpose**

This document establishes the rules for transfers of personal data by PanEuropean Bank AG. At 26 October 2026 there are three transfers under Art. 46 — remote technical support by Example Cloud Services Pvt Ltd (India), anti-fraud matching with a partner bank (India) and the customer-service assistant of Example AI Provider Inc. (United States) — and one joint-processing scheme, the federated-learning anti-fraud consortium, that General Counsel concluded is not a transfer.

## **2. Scope and What Is a Transfer**

PanEuropean applies the three criteria of Part A, Section 2.1:

* **Remote technical support** — Example Cloud Services Pvt Ltd (fictional) is a separate legal entity in India with remote access to PanEuropean's production systems as processor: a transfer. Tokenisation of identifiers in logs (keys held by PanEuropean in the EEA) is a supplementary measure; it does not take the flow outside Chapter V.
* **Staff travelling outside the EEA** — employees of PanEuropean Bank AG who access the Bank's systems while abroad do not make a transfer (same legal entity); the access is governed by the CISO's remote-access rules and, where relevant, the DPIA.
* **EuroCredit Bureau** (fictional) — an independent controller established in the EEA: not a transfer (criterion 3 not met); data sharing is governed by a data-sharing agreement (Document 17).
* **Branches** — the branches in France, Italy, Spain and Poland are part of the same legal entity in the EEA: not transfers.
* **Customer-instructed international payments** — payment data sent to a beneficiary's bank outside the EEA on the customer's order are assessed by General Counsel under the three criteria and, where they are transfers, under Art. 49(1)(b) or (c); the derogation record identifies the derogation relied on, explains why the transfer is necessary for the customer's payment order and how the conditions of that derogation, as interpreted in EDPB Guidelines 2/2018, are met for this flow, and is reviewed annually. Internal policy (not a legal requirement): every use of Art. 49 requires General Counsel's written justification (Document 7).
* **Anonymous information** — the published credit-portfolio statistics (Document 18, Example 3.1) are outside Chapter V while the anonymity conclusion stands (Document 11, Section 3.1). No other dataset is treated as anonymous; synthetic datasets are personal data (Document 10).

EuroCredit Bureau and all other recipients in the EEA are outside this document; India and the United States are the recipient countries (Document 7, Section 3).

## **3. Privacy-Enhancing Technologies, Joint-Processing Architectures and Remote Access**

| Scheme / Process | Artefact or Access Crossing a Boundary | Transfer-Status Conclusion (General Counsel, with Group DPO advice) | Mechanism and Supplementary Measures | Evidence | Re-Assessment |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Federated-learning anti-fraud consortium (Processing Owner: Head of Fraud Prevention) | Model updates with differential privacy (noise added by PanEuropean before aggregation), through secure aggregation | **Not a transfer**: all consortium members and the aggregation service are established in the EU; no data are made available to an importer in a third country (criterion 3 not met). The PETs are not the reason for the conclusion | Not applicable. G-L (Art. 6(1)(f)), the Art. 26 arrangement and DPIA-FL-01 apply | EVP-2026-0041 | On any change of membership, coordinator or hosting; at least annually |
| Private set intersection with the partner bank in India (Processing Owner: Head of Fraud Prevention) | Blinded protocol messages derived from PanEuropean customer identifiers | **Treated as a transfer**: General Counsel did not conclude that the messages are not personal data for the partner | Art. 46 — SCC Module 1; PSI assessed as a supplementary measure (Document 20, TIA-PSI-01) | TIA-PSI-01 | As in TIA-PSI-01 |
| Remote technical support by Example Cloud Services Pvt Ltd | Remote access to production systems; tokenised logs | **Transfer** (separate entity with remote access) | Art. 46 — SCC Module 2; masking gateway, EEA break-glass, tokenisation with keys in the EEA | TIA-CLOUD-01 | As in TIA-CLOUD-01 |

***Case 1 — Federated Learning for the Anti-Fraud Consortium***

PanEuropean trains an anti-fraud model jointly with other EU banks without centralising transaction data. The federated architecture does not change the legal status of the data or of the model updates, and it would not exempt a flow from Chapter V. The consortium involves no third-country importer, so Chapter V is not engaged; if a member, coordinator or hosting provider outside the EEA joined, the flow would be re-assessed under Section 2 and, if it is a transfer, an Art. 46 tool and a TIA would be required, with differential privacy and secure aggregation assessed as supplementary measures. The PET Assessment Module result for DPIA-FL-01 (Document 18, Section 3.3.3) is evidence for the DPIA, not for the transfer status: the DP configuration gates (ε 2.6 at δ 1×10⁻⁹ across all rounds, per customer; gate ε ≤ 3.0), validated secure aggregation and the membership-inference test on the final model are the mandatory set; the gradient-reconstruction test is classified "not applicable for observers in scope" because validated secure aggregation and access restrictions exclude that threat by control — it is not a passed test, and if the secure-aggregation validation lapsed, the test would become mandatory and the module INCOMPLETE until it is run. DPIA-FL-01: track (a) Medium (Document 19).

***Case 2 — Private Set Intersection for Anti-Fraud Matching***

Purpose: PanEuropean learns which of its customers appear on the partner bank's list of identities linked to confirmed fraud; fraud analysts review every match before any action. The two banks are independent controllers; the lawful basis is Art. 6(1)(f) (fraud prevention), with Art. 10 and banking-confidentiality questions assessed by Legal & Compliance in G-L (DPIA-PSI-01).

History: the original mutual-output design, in which both banks learned the intersection, failed G-TIA on 10 February 2026 (TIA-PSI-01, version 2.0): matched customer data in clear text at the partner could not be protected against public-authority access in a way that ensures essentially equivalent protection. The Head of Fraud Prevention suspended the sessions under SCC Clause 14(f) on 12 February 2026; the contract was not terminated. The one-sided design (only PanEuropean learns the matches; blinding key held by PanEuropean in the EEA; key rotation per session) passed G-TIA on 20 March 2026 (TIA-PSI-01, version 2.1), and sessions resumed on 1 April 2026.

A design in which the partner learns the size of the intersection is not sufficient: through a chosen or very small input, or repeated or adaptive sessions, the intersection size could tell the partner — or an authority compelling it — whether chosen identities are PanEuropean customers, and minimum set sizes or session limits do not close that path. The G-TIA pass in TIA-PSI-01 (Document 20) therefore rests on a one-sided design without any output to the partner: the intersection and its size are revealed only to PanEuropean; PanEuropean's input is padded to a fixed public bound and message lengths and timing do not depend on the number of matches; the partner observes only the padded input bound and the fact of the monthly session; the protocol and implementation are reviewed by an independent cryptographer against these properties (illustrative assumption). The partner commits to its confirmed-fraud list before each session and warrants its authenticity, and no case-specific follow-up runs through this channel; these are hygiene controls and do not carry the equivalence conclusion. Any evidence that the partner can observe a result-dependent signal leads to suspension under Clause 14(f), and any change of protocol triggers re-evaluation. The partner-bank contract carries the list-authenticity warranty, audit right and session rules (Document 17). DPIA-PSI-01: track (a) Medium (Document 19).

## **4. Transfer Mechanisms**

* **Art. 45:** no adequacy decision covers India. For the United States, the adequacy decision of 10 July 2023 on the EU-U.S. Data Privacy Framework (upheld by the General Court in T-553/23, *Latombe*, 3 September 2025) applies only to certified organisations for the data covered by their certification; Example AI Provider Inc. is assumed, for this illustration, not to be certified, so the Art. 45 branch is not available for its transfer. For any certified US importer, Legal & Compliance records an adequacy check record and does not redo the Commission's assessment.
* **Art. 46:** standard contractual clauses (Commission Implementing Decision (EU) 2021/914) — Module 2 with Example Cloud Services Pvt Ltd and with Example AI Provider Inc.; Module 1 with the partner bank — each with a TIA (Document 20). PanEuropean has no group entities outside the EEA and uses no binding corporate rules.
* **Art. 49:** used only for customer-instructed payments where General Counsel's derogation record so concludes (Section 2); not used for the three transfers above.
* **Onward transfers and sub-processors:** the contracts with Example Cloud Services Pvt Ltd and Example AI Provider Inc. allow sub-processors only with PanEuropean's prior written authorisation (Art. 28(2)); PanEuropean gives a general written authorisation under which the processor notifies any intended addition or replacement at least 30 days in advance (illustrative contract term), and the Processing Owner (CIO; Head of Customer Service) decides whether to object, with Group DPO advice; a sub-processor in a third country requires an appropriate mechanism (SCC Module 3 between processor and sub-processor) and a re-evaluated TIA before it receives data (Document 17). Example Cloud Services Pvt Ltd uses no sub-processors at present; Example AI Provider Inc. uses a US hosting sub-processor covered by TIA-LLM-01 (illustrative). The partner bank, as an independent controller, may make onward transfers only under the onward-transfer clause of Module 1.
* **Requests from third-country authorities:** handled under Art. 48 and Part A, Section 4.5.

## **5. "Recipient → Mechanism → Basis" Matrix**

| Recipient Country | Importer and Role | Transfer Criteria Met? | Mechanism | TIA / G-TIA | Basis Reference |
| :---- | :---- | :---- | :---- | :---- | :---- |
| India | Example Cloud Services Pvt Ltd (fictional) — processor; remote technical support with access to production systems (Processing Owner: CIO) | Yes (separate entity; remote access) | Art. 46 — SCC Module 2 | TIA-CLOUD-01 — pass for the restricted design (no clear-text customer data accessible in India), 12 March 2026 | Art. 28 contract with SCCs; RoPA-CLOUD-01 |
| India | Partner bank (fictional) — independent controller; anti-fraud matching by one-sided private set intersection (Processing Owner: Head of Fraud Prevention) | Treated as a transfer (Section 3) | Art. 46 — SCC Module 1 | TIA-PSI-01 — mutual-output design failed and was suspended (February 2026); one-sided design pass, 20 March 2026 | Data-sharing agreement with SCCs; RoPA-PSI-01 |
| United States | Example AI Provider Inc. (fictional) — processor; customer-service assistant (Processing Owner: Head of Customer Service); not DPF-certified (illustrative assumption); illustrative terms: deletion within 30 days, no training on customer data | Yes | Art. 46 — SCC Module 2 | TIA-LLM-01 — pass of 22 June 2026 (historical); current status at 26 October 2026: G-TIA incomplete — HOLD; transfers suspended (Clause 14(f)), customer service human-only | Art. 28 contract with SCCs; RoPA-LLM-01 |
| EU (consortium members) | Federated-learning consortium — joint controllers (Art. 26) | No (no third-country importer) | Not applicable | Transfer-status conclusion; EVP-2026-0041 | Art. 26 arrangement |

## **6. Conditions Triggering a TIA or Re-Evaluation**

The triggers of Part A apply. Each TIA is re-evaluated at least annually on the date fixed in its G-TIA determination (TIA-CLOUD-01 by 12 March 2027; TIA-PSI-01 by 20 March 2027; TIA-LLM-01 by 22 June 2027 — all planned) and earlier on any trigger: for Example Cloud Services Pvt Ltd, any change that would allow clear-text access to customer data from India or any change in Indian law or cybersecurity directions; for the partner bank, any change of protocol, key management, session controls or participants; for Example AI Provider Inc., any change to US surveillance law or its redress mechanism, to the status of the DPF adequacy decision, or to the provider's sub-processors or terms, or an extension of the assistant to new uses. Re-evaluation is not tied to the re-certification of any tool.

## **7. G-TIA Outcome, Supplementary Measures, Suspension and Public-Authority Access**

* Supplementary measures (details in Document 20): for remote support — a privileged-access gateway in the EEA that masks customer data on screen, "break-glass" clear-text access only by EEA-based staff, logged per session, tokenisation of identifiers in logs with keys held only by PanEuropean in the EEA, and encryption in transit; for private set intersection — one-sided output, blinding with a session key held in the EEA, key rotation and the session controls of TIA-PSI-01; for the customer-service assistant — masking of account, card and national identification numbers before sending, exclusion of sensitive channels, SCC Clause 15 commitments and encryption, with the residual exposure of message content assessed in TIA-LLM-01.
* Decisions to proceed (Document 8, Section 5; all taken before 23 October 2026 under Document 8, version 1.0, and re-assessed under version 3.0 at expiry): CIO for remote support (20 March 2026); Head of Fraud Prevention for private set intersection (25 March 2026); Head of Customer Service for the assistant (25 June 2026; not in effect since 26 October 2026 — transfers suspended under the G-TIA hold until a current pass is recorded). The tiers come from the DPIA or the Document 18 calculation requested by Document 20: remote support Medium, private set intersection Medium (DPIA-PSI-01), assistant Medium (DPIA-LLM-01).
* Suspension: the mutual-output PSI sessions were suspended under SCC Clause 14(f) on 12 February 2026 (Section 3). No contract has been terminated; had PanEuropean terminated under Clause 16(c), Legal & Compliance would have informed the HBDI, for which the Group DPO is the contact point.
* Parallel DPIA and G-36: DPIA-PSI-01, DPIA-LLM-01 and DPIA-FL-01 ran in parallel with the TIAs; G-36 was evaluated in each, and the test was not met (Document 19). For remote support, DPIA triage found no DPIA required (one WP248 criterion).
* Public-authority access: Example Cloud Services Pvt Ltd, the partner bank and Example AI Provider Inc. must notify General Counsel and the Group DPO promptly of any request or direct access by an authority of India or the United States, unless prohibited by the law of that country, and must challenge requests where there are grounds (SCC Clause 15). Notifications, assessments and outcomes are recorded in the TIA record and trigger re-evaluation; where the event is also a personal data breach, Document 14 applies. As of the adoption date, no such notification has been received.

## **8. Documentation in the RoPA**

The three transfers are recorded in PanEuropean's RoPA (Document 21) — RoPA-CLOUD-01, RoPA-PSI-01, RoPA-LLM-01 — with importer, country, mechanism (SCCs) and TIA identifier. The federated-learning consortium is recorded in the RoPA as processing under an Art. 26 arrangement, with a reference to the transfer-status conclusion and EVP-2026-0041 in place of a mechanism; it is not listed as a transfer. Customer-instructed payments relying on Art. 49 are recorded with the derogation and the reference to General Counsel's derogation record.

## **9. Roles and Responsibilities**

| Role | Responsibility |
| :---- | :---- |
| Privacy Operations Lead | Accountable for identifying transfers in data flows (Privacy Engineers responsible); initiates TIAs |
| General Counsel (Legal & Compliance) | Responsible and accountable for the TIAs (laws and practices of India and the United States), the G-TIA determinations, transfer-status conclusions (federated learning, private set intersection), derogation and adequacy check records and re-evaluation; maintains the SCCs; informs the HBDI under Clause 16(c) if PanEuropean terminates |
| Processing Owners — CIO (remote support), Head of Fraud Prevention (private set intersection, federated learning), Head of Customer Service (assistant) | Accountable for the transfer tool and supplementary measures, the decision to proceed up to Medium (with Chief Privacy Officer concurrence at Medium under Document 8, version 3.0) after G-L and G-TIA pass, suspension, and responses to sub-processor notifications |
| Chief Risk Officer | Decides to proceed where the residual risk is High (none at present); the Management Board is informed of G-TIA failures and suspensions |
| Group DPO | Mandatory advice on TIAs, G-TIA determinations, transfer-status conclusions and decisions to proceed; contact point for the HBDI; monitors compliance |
| Chief Privacy Officer (EPPO) | Owns this document; concurs at Medium; informed of G-TIA outcomes |
| CISO | Designs and operates technical supplementary measures (masking gateway, tokenisation, key management) |
| Privacy Officer(s) / Privacy Engineer(s) | Support Legal & Compliance in preparing TIAs; identify transfers and PET-scheme artefacts |
| Procurement; ICT Risk Control | Counterparty due diligence (Document 17); the classification of ICT third-party arrangements under DORA — whether a service supports a critical or important function — is made by ICT Risk Control and recorded in the DORA Register of Information (Document 3, Section 3.15), not in this document |

## **10. Relationship to Other Framework Documents**

* Builds on the Regulatory Applicability Matrix (Document 7) — India and the United States as recipient countries — and on the Data Classification Policy (Document 10).
* Applied through Document 20 — TIA-CLOUD-01, TIA-PSI-01, TIA-LLM-01 and the transfer-status conclusions.
* Interacts with Document 11 (logs held by the remote-support provider), Document 14 (incidents at importers), Document 16 (design choices such as the one-sided PSI and the masking gateway), Document 17 (due diligence; Art. 28 contracts; sub-processor authorisation; DORA register interface), Document 19 (DPIAs in parallel) and Document 18 (elements requested by Document 20).
* Roles — Document 5, Section 5.4; decisions to proceed — Document 8, Section 5.
* Documented in the RoPA (Document 21) and the Data Inventory (Document 23); executed as core process C4 (Document 24).
* The Customer Privacy Notice (Document 1, 01B, Section 10) describes these transfers to customers.

## **11. Review and Amendment**

This document is reviewed under PanEuropean's Policy Review Cycle (Document 29) and immediately upon a change in the status of the EU-U.S. Data Privacy Framework adequacy decision, a relevant judgment or EDPB guidance, a relevant change in Indian or US law, or a new published attack on a technique used as a supplementary measure. Changes are adopted by the Management Board on the Chief Privacy Officer's proposal, after consulting General Counsel, the Privacy Risk Committee and the Group DPO.

## **12. Approval**

Version 1.0 (1 March 2026) was adopted by the Management Board; the Group DPO was document owner at that time. Version 2.0 was adopted by the Management Board on 20 October 2026 on the Chief Privacy Officer's proposal, after consulting General Counsel and the Group DPO. Document owner: Chief Privacy Officer. Group DPO advice is on file.

# **Normative Basis and References**

* Regulation (EU) 2016/679 (GDPR): Arts. 4(26), 6, 9, 10, 26, 28(2), 28(4), 30(1)(e), 32, 35, 36, 44–49 (incl. 45, 46(2)–(3), 47, 48, 49(1)), 58(2)(j), 63–64; Recital 26.
* Commission Implementing Decision (EU) 2021/914 on standard contractual clauses for the transfer of personal data to third countries (Clauses 8, 9, 14, 15, 16).
* Commission Implementing Decision (EU) 2023/1795 on the adequate level of protection under the EU-U.S. Data Privacy Framework (10 July 2023); General Court, T-553/23, *Latombe v Commission*, 3 September 2025.
* CJEU, C-311/18, *Data Protection Commissioner v Facebook Ireland and Schrems* (Schrems II).
* CJEU, C-413/23 P, *EDPS v SRB*, 4 September 2025 (the recipient's means as part of the contextual analysis; not a general rule on Chapter V).
* EDPB Guidelines 05/2021 on the interplay between the application of Article 3 and the provisions on international transfers as per Chapter V of the GDPR, version 2.0 (Section 2.2; Example 8.1).
* EDPB Recommendations 01/2020 on measures that supplement transfer tools, version 2.0.
* EDPB Guidelines 2/2018 on derogations of Article 49 under Regulation 2016/679.
* EDPB/EDPS Joint Opinion 02/2026 on the Digital Omnibus proposal, §19 (Chapter V implications of a recipient-relative approach still require guidance) — context only; the Digital Omnibus is a proposal, not law.
* EDPB Guidelines 01/2025 on pseudonymisation.
* Regulation (EU) 2022/2554 (DORA), Arts. 28–31 — ICT third-party risk, as an adjacent regime.

# **International Adaptation**

> **Guidance.** The GDPR is the baseline. The applicability map for Canada is in Document 7, Section 3.1. This document does not claim compliance with any jurisdiction's law.

* **United Kingdom (headline).** Transfers from the UK follow the UK GDPR as amended by the Data (Use and Access) Act 2025, whose changes to the transfer regime commence in phases — record which provisions apply at each review. UK transfer tools include the International Data Transfer Agreement (IDTA) and the International Data Transfer Addendum to the EU standard contractual clauses; UK adequacy regulations are checked for the destination.
* **Switzerland (headline).** Under the revFADP, personal data may be disclosed abroad to countries that the Federal Council has listed as providing adequate protection, or with appropriate safeguards — for example the EU standard contractual clauses with the adaptations recognised by the FDPIC — or under the statutory exceptions; a transfer assessment is documented in the same way as a TIA.
* **Canada — PIPEDA.** PIPEDA does not prohibit transfers outside Canada. The organisation remains accountable for information transferred to a third party for processing and uses contractual or other means to provide a comparable level of protection (Schedule 1, Principle 4.1.3); individuals are informed that their information may be processed in another jurisdiction and accessed by its authorities (OPC guidance on processing personal data across borders).
* **Canada — Québec (P-39.1).** Before communicating personal information outside Québec, the organisation conducts a privacy impact assessment that considers, among other things, the sensitivity of the information, the purpose, the protection measures and the legal framework of the destination, and communicates the information only if the assessment shows that it would receive adequate protection; the communication is subject to a written agreement. The assessment is documented with the TIA where both apply.

# **Document History (PGF)**

| Release | Date | Changes |
| :---- | :---- | :---- |
| 1.0.0-rc.1 | 2026-10-26 | Canonical English Markdown; changes from internal ver.2: transfer defined by the three cumulative criteria of EDPB Guidelines 05/2021 v2.0 §2.2 (not by geography alone; international organisations included; same-entity employee remote access is not a transfer; remote access by a separate provider or group entity is); data-state rules added, including the limits of C-413/23 P (importer's means part of the analysis; processor paths never declared outside Chapter V merely for lack of a key; unclear flows treated as transfers); the former three-condition exclusion test for PET schemes (numerical threshold, DPO determination, legal opinion) replaced by controller transfer-status conclusions by Legal with DPO advice; PETs, TEEs, homomorphic encryption, PSI and federated learning treated as possible supplementary measures, not exemptions; the statement that Art. 36 is "unrelated" to transfers removed (DPIA and Art. 36 may apply in parallel); mechanism branches Art. 45 / 46 / 49 with adequacy scope and eligibility checks, BCR approval through the consistency mechanism, Art. 46(2)(e)–(f) and 46(3) tools, and Art. 49 wording per EDPB Guidelines 2/2018 (exceptional, restrictive, conditions of each derogation); G-TIA failure means no start or suspension and cannot be accepted; SCC Clauses 14(f), 15 and 16 cited correctly, with the Clause 16(c) information duty assigned to the exporter (the DPO as contact point); Art. 48 added; one sub-processor rule (prior written authorisation, general authorisation with prior notice and objection window) aligned with Document 17; public-authority requests recorded in the TIA record instead of an undefined separate register; DPO changed from Accountable to mandatory adviser — Legal R/A for TIA and G-TIA, Processing Owner for tool, measures and decision to proceed; Part B rebuilt with fictional providers (Example Cloud Services Pvt Ltd; Example AI Provider Inc., not DPF-certified as an illustrative assumption; partner bank for anti-fraud matching), the PSI purpose corrected to anti-fraud matching with the one-sided design and its intersection-size leakage stated, the suspended mutual-output design recorded, the federated-learning consortium recorded as intra-EU (no transfer, EVP-2026-0041; gradient-reconstruction test "not applicable for observers in scope" by validated control), RoPA identifiers corrected and real-vendor references removed; DORA terminology corrected (critical or important functions; classification by ICT Risk Control); adoption moved to Executive Management; example dates shifted by −12 months; International adaptation (UK IDTA/Addendum, Switzerland, PIPEDA, Québec assessment before communication outside Québec) and references added |
