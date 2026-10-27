---
title: "Transfer Impact Assessment Methodology"
document_id: PGF-20
level: 2
release_version: 1.0.0-rc.1
status: release-candidate
authors: ["Alexey Neyman", "Val Khvatov"]
regulatory_reference_date: 2026-10-26
licence_proposed: "CC BY 4.0 (proposed; subject to rights-holder confirmation)"
source_provenance: "Derived from internal source set ver.2: Level2/20. Transfer-Impact-Assessment-Methodology_ENG.docx.md; sha256 7961cc029d3bb5adef2e8931bf90ab4cdc83728c0f90d75050424abb2bf66c07"
---

# PGF-20 — Transfer Impact Assessment Methodology

*Privacy Governance Framework (PGF) · Level 2 — Policies and Standards · Release 1.0.0-rc.1 · Regulatory reference date: 26 October 2026*

> **Status and use.** Part A is a reusable template. Part B is a worked example for a fictional organisation (PanEuropean Bank AG); all names, figures, dates and records in Part B are illustrative. Nothing in this document is legal advice or a statement about any real organisation, product or provider.

# **About This Document**

**Purpose.** Document 20 sets out how the organisation decides whether a flow of personal data is a transfer to a third country or an international organisation (GDPR Chapter V), which transfer mechanism it relies on, and — for transfers relying on appropriate safeguards under Art. 46 — how it assesses whether the laws and practices of the destination allow the importer to comply with those safeguards, which supplementary measures are needed, and when a transfer must not start or must be suspended. This is the transfer-equivalence gate (G-TIA).

**Scope.** The method is a legal assessment. Its core — the laws and practices of the destination, enforceable rights and effective redress, the effectiveness of supplementary measures and re-evaluation — is performed in this document. The Privacy Risk Assessment Methodology (Document 18) supplies only the elements this document requests, for example the severity of harm if the transferred data were disclosed, or PET Assessment Module evidence on a de-identified artefact. No risk score, tier or risk appetite can replace or override the G-TIA outcome.

**Relationships.** The Cross-Border Data Transfer Policy (Document 12) sets the policy and the mechanism matrix; this document is its assessment procedure. A transfer is also processing: the legal compliance gate (G-L) and, where triggered, a DPIA and the Art. 36 test (Document 19) apply in parallel. Vendor due diligence is in Document 17. Roles follow the RACI Matrix (Document 5, Section 5.4). Outcomes are recorded in the RoPA (Document 21) and the Privacy Risk Register (Document 22). The full list is in Section 7.

# **How to Use This Document**

Part A is a template. Text in ***[square brackets, bold italic]*** is a fillable or illustrative placeholder. Blocks marked **Guidance** are removed from the adopted version. Part B shows the template completed for the fictional PanEuropean Bank AG, with three worked transfer impact assessments.

Four rules apply throughout:

1. **Two separate tests.** A transfer needs a lawful basis and compliance with the other GDPR provisions (G-L) **and** compliance with Chapter V (G-TIA). Passing one never cures a failure of the other.
2. **Branch by mechanism.** Art. 45 adequacy, Art. 46 appropriate safeguards and Art. 49 derogations follow different routes (Section 3.1). The full laws-and-practices assessment is the Art. 46 branch.
3. **Equivalence or no transfer.** If essentially equivalent protection cannot be ensured, the transfer does not start or is suspended. A failed G-TIA cannot be "accepted" by anyone.
4. **PETs are evidence, not exemptions.** Privacy-enhancing technologies, trusted execution environments, homomorphic encryption and remote-access arrangements are not automatic exemptions from Chapter V (EDPB Guidelines 05/2021); they may be supplementary measures whose effectiveness is assessed.

# **Table of Contents**

**About This Document**
**How to Use This Document**
**Part A — Template**
Glossary of Terms
1. Purpose
2. Scope of Application
3. Triage — Mechanism and When a TIA Is Required
4. TIA Procedure (Art. 46 Branch)
5. TIA Report Structure
6. Roles and Responsibilities
7. Relationship to Other Framework Documents
8. Review and Amendment
9. Approval
**Part B — Worked Example: PanEuropean Bank AG**
Glossary of Terms
1. Purpose
2. Scope of Application
3. Triage — Mechanism and When a TIA Is Required
4. TIA Procedure at PanEuropean
5. TIA Report Structure at PanEuropean
6. Roles and Responsibilities
7. Relationship to Other Framework Documents
8. Review and Amendment
9. Approval
**Appendix to Part B — Worked TIAs**
Report TIA-CLOUD-01
Report TIA-PSI-01
Report TIA-LLM-01
**Normative Basis and References**
**International Adaptation**
**Document History (PGF)**

# **Part A — Template**

**Transfer Impact Assessment Methodology of *[Legal Name of the Organisation]***

*Effective Date: **[DD Month YYYY]**  ·  Version: **[x.x]**  ·  Document Owner: **[Executive Privacy Programme Owner (EPPO)]**  ·  Adopted by: **[Executive Management]***

***Version History***

| Version | Date | Changes |
| :---- | :---- | :---- |
| ***[1.0]*** | ***[DD.MM.YYYY]*** | ***[First version of the document]*** |
| ***[x.x]*** | ***[DD.MM.YYYY]*** | ***[Brief description of material changes]*** |

## **Glossary of Terms**

*This table lists only terms defined by this document itself; terms defined in another PGF document are not repeated here.*

| Term | Definition / Reference |
| :---- | :---- |
| Transfer | A flow of personal data that meets the three cumulative criteria of EDPB Guidelines 05/2021 (version 2.0, Section 2.2): (1) the exporter — a controller or processor — is subject to the GDPR for the given processing; (2) the exporter discloses by transmission or otherwise makes the personal data available, including by remote access, to **another** controller, joint controller or processor (the importer); (3) the importer is in a third country, irrespective of whether it is itself subject to the GDPR, or is an international organisation. |
| TIA (Transfer Impact Assessment) | The documented assessment, for a transfer relying on an Art. 46 transfer tool, of whether the laws and practices of the destination, as relevant to the transfer, impinge on the effectiveness of the tool, and of the supplementary measures needed to ensure an essentially equivalent level of protection (CJEU C-311/18; EDPB Recommendations 01/2020, version 2.0). |
| G-TIA | The transfer-equivalence gate, branched by mechanism (Section 3.1). Its outcome is pass or fail; it is not a risk tier. |
| Adequacy check record | For a transfer relying on an Art. 45 adequacy decision: the record that the decision covers the destination, sector and recipient, that it remains valid, and how it is monitored. For the United States it follows the DPF check of Document 12, Part A, Section 4.1: exact legal entity and covered entities; framework (EU-U.S. DPF / UK Extension / Swiss-U.S. DPF); HR or non-HR coverage; official status wording and profile URL from the DPF List; date, reviewer and evidence reference; re-check triggers. Where an applicable Art. 45 decision covers the flow, no Art. 46 TIA is required as a general legal addition. |
| Derogation record | For a transfer relying on Art. 49: the specific derogation used, the facts showing that its conditions are met, and the assessment that no Art. 45 or Art. 46 mechanism is available or appropriate where the derogation so requires. |
| Transfer-status conclusion | A controller's legal conclusion, on documented evidence, that a given flow is or is not a transfer under Chapter V (Section 3.3). |

## **1. Purpose**

This document establishes how ***[Legal Name of the Organisation]*** identifies transfers, determines the transfer mechanism, carries out a TIA where the mechanism requires one, decides whether a transfer may start or continue, and suspends or terminates a transfer when essentially equivalent protection can no longer be ensured.

## **2. Scope of Application**

* ***[This document applies to every flow of personal data that meets the three criteria of a transfer (Glossary), including onward transfers by an importer and access by sub-processors in a third country, and to every flow for which a transfer-status conclusion is needed (Section 3.3).]***

* ***[An ordinary flow between recipients established in the EEA is not a Chapter V transfer; the three-criteria test still applies to every flow, including a disclosure to an international organisation, which can be a transfer wherever the organisation is located. A transfer is never defined only by the crossing of a geographic border. Remote access to data held in the EEA by an employee of the same legal entity (for example, while travelling) is not a transfer, because the data are not made available to another controller or processor; security and other GDPR obligations still apply, and the risks of access from a third country are considered under Art. 32 and in the DPIA where relevant. Remote access by a separate legal entity — including another entity of the same group, or a service provider — located in a third country is a transfer.]***

* ***[A transfer is also processing. G-L (lawful basis, transparency, Art. 9/10 conditions, Art. 22 and the other GDPR provisions) and, where triggered, a DPIA and the Art. 36 test (Document 19) apply in parallel with this document. A transfer does not exclude a DPIA or a prior consultation; a TIA does not replace either.]***

* ***[Requests from third-country courts, tribunals or administrative authorities to disclose personal data are handled under Art. 48 and the Cross-Border Data Transfer Policy (Document 12): a foreign judgment or decision is recognised or enforceable only if based on an international agreement, such as a mutual legal assistance treaty, without prejudice to other grounds for transfer under Chapter V.]***

## **3. Triage — Mechanism and When a TIA Is Required**

> **Guidance.** First establish whether the flow is a transfer (Glossary; Section 3.3 where a PET scheme or remote access raises the question). Then identify the mechanism. Only the Art. 46 branch requires a full TIA as a matter of law. Any stricter internal requirement — for example, a full review also for adequacy-based transfers — is labelled as internal policy.

***3.1 Mechanism Branches of G-TIA***

| Branch | What G-TIA requires | Outcome |
| :---- | :---- | :---- |
| **Art. 45 — adequacy decision** | Adequacy check record: the decision covers the destination, sector and recipient (scope and eligibility, for example the recipient's active certification under the EU-U.S. Data Privacy Framework for the relevant data); the decision remains valid; monitoring of amendments, suspension, repeal or annulment. There is no statutory obligation to redo the Commission's assessment. ***[Any stricter internal review — internal policy.]*** | Pass where scope, eligibility and validity are confirmed; otherwise the flow moves to another branch or does not start |
| **Art. 46 — appropriate safeguards** (standard contractual clauses, binding corporate rules, approved codes of conduct or certification mechanisms with binding commitments, and other Art. 46 tools) | A full TIA (Section 4): laws and practices of the destination as relevant to the transfer, enforceable rights and effective redress, supplementary measures and their effectiveness, procedural steps and re-evaluation | Pass only where essentially equivalent protection is ensured; otherwise the transfer does not start or is suspended (Section 4.8) |
| **Art. 49 — derogations for specific situations** | Derogation record: derogations are exceptional and interpreted restrictively; each is subject to the specific conditions of the derogation used, including the occasional or non-repetitive character where that derogation requires it (EDPB Guidelines 2/2018). ***[Any stricter internal rule, for example a ban on using derogations for repetitive transfers that the law would allow, is labelled internal policy.]*** | Pass only where the specific conditions are documented as met |

G-L and DPIA duties apply under every branch.

***3.2 When a TIA Is Performed or Re-Evaluated (Art. 46 Branch)***

| No. | Trigger |
| :---- | :---- |
| 1 | A new transfer relying on an Art. 46 tool — before the transfer starts |
| 2 | A new importer, destination, transfer tool or module, or a new onward transfer or sub-processor in a third country |
| 3 | An expansion of the data categories or volume, including special categories, or a change of purpose |
| 4 | A change in the technical scheme (for example, a move from transfer in clear text to a pseudonymised or split-processing scheme, or the reverse), including PET schemes treated as transfers under Section 3.3 |
| 5 | A relevant change in the laws or practices of the destination, a notification by the importer under the transfer tool (for example, SCC Clauses 14(e) and 15), or a relevant judgment, supervisory-authority decision or guidance |
| 6 | A security incident or a public-authority request at the importer (Document 14) |
| 7 | Scheduled re-evaluation: ***[at least annually]***, and more often where the TIA records conditions or open issues |

* A TIA is performed for each combination of importer, destination, transfer tool and data categories; a TIA for one importer does not extend to another, even under the same tool.

* Re-evaluation is tied to legal and monitoring events (above), not to the calendar of any tool or vendor certification.

***3.3 Transfer-Status Conclusions for PET Schemes and Remote Access***

Where it is unclear whether a flow is a transfer — for example, in federated learning, secure multi-party computation, private set intersection, homomorphic encryption, trusted execution environments or remote-access arrangements — ***[Legal]*** records a transfer-status conclusion:

* ***[The conclusion applies the three criteria of a transfer (Glossary) to the full flow and from the exporter's (controller's) perspective. The means reasonably likely to be used by the importer or by any other person, including authorities of the destination, are part of the contextual identifiability analysis (Recital 26; CJEU C-413/23 P, *EDPS v SRB*, 4 September 2025, paragraphs 105–110 — context, not a new rule for Chapter V). The importer's inability to attribute the data does not by itself take the exporter out of Chapter V: the data remain personal data for the exporter, and the role of a processor acting on the exporter's behalf is assessed separately. A processor path is never treated as outside the GDPR merely because the processor lacks the key. The EDPB and the EDPS have indicated that the implications of that judgment for Chapter V call for further EDPB guidance (EDPB-EDPS Joint Opinion 2/2026, adopted 10 February 2026, paragraph 19).]***

* ***[Evidence may include PET Assessment Module results (Document 18, Section 3.3) and a cryptographic or architectural review. A numerical threshold is evidence, not a legal criterion. PETs, trusted execution environments, homomorphic encryption and remote access are not automatic exemptions from Chapter V (EDPB Guidelines 05/2021).]***

* ***[The transfer-status determination is the controller's: it is recorded by [Legal] (at PanEuropean, General Counsel) at G-L on documented evidence, with DPO advice (Document 2, Section 8). The DPO does not make the determination.]***

* ***[Where the conclusion is that the flow is a transfer, or where it cannot be reached with confidence, the flow is treated as a transfer and Section 3.1 applies. Where the conclusion is that the flow is not a transfer, the processing remains subject to G-L, the RoPA (Document 21) and the DPIA duties; the conclusion is re-assessed upon any change of participants, parameters, technology, law or guidance, and at least annually.]***

## **4. TIA Procedure (Art. 46 Branch)**

> **Guidance.** The steps cover the six steps of EDPB Recommendations 01/2020 (version 2.0, adopted 18 June 2021): (1) know your transfers; (2) identify the transfer tool; (3) assess whether anything in the law or practice of the destination may impinge on the effectiveness of the tool; (4) identify and adopt supplementary measures; (5) take any formal procedural steps; (6) re-evaluate at appropriate intervals. The legal assessment of Step 3 draws on EDPB Recommendations 02/2020 on the European Essential Guarantees for surveillance measures. Where standard contractual clauses (Commission Implementing Decision (EU) 2021/914) are used, Clause 14 requires the parties to warrant, on the basis of such an assessment, that they have no reason to believe that the laws and practices of the destination prevent the importer from fulfilling its obligations.

| Step (this document) | EDPB step |
| :---- | :---- |
| 4.1 Initiation; 4.2 Description of the transfer | Step 1 — know your transfers |
| 4.3 Transfer tool | Step 2 — identify the transfer tool |
| 4.4 Legal assessment of laws and practices | Step 3 — assess the destination |
| 4.5 Supplementary measures | Step 4 — supplementary measures |
| 4.6 G-TIA determination and procedural steps | Step 5 — procedural steps |
| 4.7 Decision to proceed | — (PGF decision step) |
| 4.8 Suspension, termination and re-evaluation | Step 6 — re-evaluate |

| Step | Content |
| :---- | :---- |
| 4.1 Initiation | ***[The Privacy Operations Lead identifies a new transfer in the data flow (including remote access by a separate entity and onward transfers) or a trigger of Section 3.2, and registers the TIA with an identifier.]*** |
| 4.2 Description of the Transfer | ***[Exporter and importer, their roles (controller / processor / joint controller) and the transfer tool module; destination; purpose; data categories and data subjects; special categories; volume and frequency; format in which the data are accessible to the importer (clear text, pseudonymised, encrypted — and where the keys are held); onward transfers and sub-processors with their locations (Document 17); storage and access locations; retention at the importer. Source: the Data Inventory (Document 23) and the RoPA (Document 21).]*** |
| 4.3 Transfer Tool | ***[Branch and tool (Section 3.1). For standard contractual clauses, the module (controller-to-controller, controller-to-processor, processor-to-processor, processor-to-controller) and the docking and optional clauses used. For Art. 45 or Art. 49, the adequacy check record or derogation record replaces Steps 4.4–4.5.]*** |
| 4.4 Legal Assessment of Laws and Practices (mandatory module) | ***[[Legal] assesses and documents, with dated sources: (a) the laws of the destination that allow public authorities to access the data or to compel the importer to disclose them, as relevant to the importer, the sector and the data — assessed against the European Essential Guarantees: clear, precise and accessible rules; necessity and proportionality; independent oversight; effective remedies available to the data subject; (b) practices: how those laws are applied in practice, including to comparable importers and data, using relevant, objective, reliable, verifiable and publicly available information, and the importer's documented experience of requests (for example, transparency reports), without relying on subjective factors such as the mere likelihood that authorities will be interested in the data; (c) enforceable data-subject rights and effective administrative and judicial redress in the destination; (d) other laws that may impinge on the tool, for example data-localisation, log-retention or incident-reporting mandates; (e) the conclusion: whether, and for which elements of the transfer, the laws and practices impinge on the effectiveness of the tool. On request, Document 18 supplies the severity of harm if the transferred data were disclosed and PET-module evidence on de-identified artefacts; these inform the choice of measures and the DPIA, but do not decide the conclusion.]*** |
| 4.5 Supplementary Measures | ***[Technical, contractual and organisational measures that address the specific problem identified in Step 4.4 for the specific transfer. Effectiveness is assessed against that problem, not against a general risk score. Contractual and organisational measures alone generally cannot overcome access by public authorities that goes beyond what is necessary and proportionate; technical measures can be effective where the importer does not need the data in clear text — for example, strong encryption with keys held only in the EEA for storage, transfer of pseudonymised data that the importer and the authorities cannot attribute, or split or multi-party processing. Where the importer needs access to the data in clear text in the destination, EDPB Recommendations 01/2020 found no effective technical measure in the use cases it describes. Measures that address only misuse by the importer (for example, a no-training clause) are recorded but do not address public-authority access.]*** |
| 4.6 G-TIA Determination and Procedural Steps | ***[[Legal] determines, with DPO advice, whether essentially equivalent protection is ensured for the transfer as designed — pass or fail — and records the reasons. A pass may carry conditions (for example, a re-evaluation date or a design restriction). Procedural steps are completed (for example, contractual additions that do not contradict the standard contractual clauses). Consultations: DPO (advice, C*); IT / Information Security on technical measures; the importer on its practices; the DPIA team, where a DPIA exists or is triggered, so that the transfer outcome is an input to G-L and the DPIA and the Art. 36 test is evaluated there.]*** |
| 4.7 Decision to Proceed | ***[Only after G-L and G-TIA have passed, and any DPIA and G-36 step are complete, the single decider under Document 8, Section 5, decides whether the transfer starts or continues, for the residual track (a) tier taken from the DPIA or — where there is no DPIA — from a Document 18 calculation requested by this document: Processing Owner up to Medium (Medium with EPPO concurrence); one named member of Executive Management for High; Critical not acceptable. A failed G-TIA is not available for any decision: no tier, appetite or acceptance can authorise the transfer.]*** |
| 4.8 Suspension, Termination and Re-Evaluation | ***[If essentially equivalent protection cannot be ensured, the transfer does not start or is suspended. Under standard contractual clauses: the exporter suspends the transfer where it considers that no appropriate safeguards can be ensured, or if instructed by the competent supervisory authority (Clause 14(f)); the exporter also suspends where the importer is in breach of the clauses or unable to comply (Clause 16(b)). The exporter may terminate the contract as provided in Clause 14(f) or Clause 16(c); data already transferred are returned or deleted as provided in Clause 16(d). Where the exporter terminates under Clause 16(c), it informs the competent supervisory authority of the non-compliance. The competent supervisory authority may itself order the suspension of data flows (Art. 58(2)(j)). A suspended transfer resumes only after a new TIA and G-TIA pass. Re-evaluation follows Section 3.2; for adequacy-based transfers, the adequacy check record is monitored for changes in the decision's validity.]*** |

## **5. TIA Report Structure**

> **Guidance.** The fields below are the mandatory minimum. Use the field names verbatim in every report.

| Report Field | Content |
| :---- | :---- |
| Identifier and Importer | ***[Unique TIA number; importer, destination, role; RoPA record (Document 21); related DPIA (Document 19) and Privacy Risk Register record (Document 22)]*** |
| Processing Owner and Dates | ***[Processing Owner; Legal author of the assessment; report version and date]*** |
| Basis for Triage | ***[Transfer-status conclusion where relevant (Section 3.3); trigger of Section 3.2]*** |
| Description of the Transfer | ***[Per step 4.2]*** |
| Mechanism and Transfer Tool | ***[Branch (Art. 45 / 46 / 49) and tool or module; for Art. 45, the adequacy check record; for Art. 49, the derogation record]*** |
| Legal Assessment of Laws and Practices | ***[Per step 4.4: laws on public-authority access; practices; enforceable rights and redress; other relevant laws; sources and dates; conclusion]*** |
| Supplementary Measures and Their Effectiveness | ***[Per step 4.5: each measure, the problem it addresses, and whether it is effective against it]*** |
| Document 18 Elements Requested | ***[For example, the severity of harm if the data were disclosed; PET-module evidence; or "none"]*** |
| G-TIA Determination | ***[Pass / fail, with reasons and any conditions; date; author]*** |
| DPO Advice and Response | ***[Content of the DPO's advice; response: followed / partly followed / not followed, with reasons]*** |
| DPIA and G-36 Link | ***[Whether a DPIA exists or was triggered; its G-36 conclusion; or the triage record]*** |
| Decision and Authorised Role | ***[The single decider under Document 8, Section 5, for the residual track (a) tier; decision; conditions; expiry of a conditional acceptance — or "not available: G-TIA failed"]*** |
| Suspension, Termination and Supervisory Authority | ***[Whether the transfer was suspended (Clause 14(f) or 16(b)) or terminated (Clause 14(f) or 16(c)); whether the competent supervisory authority was informed (Clause 16(c)) or gave an instruction or order; dates; or "not applicable"]*** |
| Reference to the Evidence Pack | ***[EVP-YYYY-NNNN]*** |
| Next Re-Evaluation Date | ***[Per Section 3.2]*** |

## **6. Roles and Responsibilities**

| Role | Responsibility |
| :---- | :---- |
| ***[Legal]*** | ***[Responsible and accountable for the transfer-status conclusion, the mechanism check and, for Art. 46, the TIA of laws and practices; determines G-TIA with DPO advice; leads re-evaluation; executes and maintains the transfer tools]*** |
| ***[Processing Owner]*** | ***[Accountable for the choice of transfer tool and the supplementary measures; decides to proceed up to Medium, only after G-L and G-TIA have passed; suspends or terminates the transfer where equivalence can no longer be ensured]*** |
| ***[Member of Executive Management designated by delegation]*** | ***[Decides to proceed where the residual track (a) tier is High]*** |
| ***[DPO]*** | ***[Advises on the transfer-status conclusion, the TIA, G-TIA and the decision (C*); contact point for the supervisory authority. Does not determine transfer status, approve a transfer or accept risk]*** |
| ***[EPPO]*** | ***[Owns this document; consulted on the decision to proceed; concurs at Medium]*** |
| ***[Privacy Operations Lead]*** | ***[Accountable for identifying transfers in the data flow, including remote access by separate entities and onward transfers; registers TIAs; compiles evidence packs]*** |
| ***[Privacy Officer(s) / Privacy Engineer(s)]*** | ***[Prepare the description of the transfer; support the assessment of technical measures and PET evidence]*** |
| ***[IT / Information Security]*** | ***[Responsible for technical supplementary measures and evidence of their implementation]*** |
| ***[Procurement]*** | ***[Consulted on vendor due diligence (Document 17); does not decide the transfer mechanism]*** |

A failed G-TIA cannot be accepted by any role. The confidentiality safeguard for the DPO's work (Art. 38(5); WP243 rev.01, §2.6) applies as stated in Document 19, Section 6.

## **7. Relationship to Other Framework Documents**

* The Cross-Border Data Transfer Policy (Document 12) — policy, mechanism matrix, Art. 48 handling; this document is its assessment procedure.

* The DPIA Methodology (Document 19) — applies in parallel where triggered; the transfer outcome is an input to G-L and the DPIA, and G-36 is evaluated in the DPIA.

* The Privacy Risk Assessment Methodology (Document 18) — supplies only the elements requested (severity, PET evidence, or a calculation of the track (a) tier where there is no DPIA).

* The Privacy Risk Appetite Statement (Document 8, Section 5) — single decider for the decision to proceed, after G-TIA has passed.

* The RACI Matrix (Document 5, Section 5.4) — roles; the Privacy Governance Charter (Document 2, Section 8) — controller conclusions on transfer status.

* The Vendor / Third-Party Privacy Risk Policy (Document 17) — due diligence, Art. 28 terms and sub-processors; it does not replace the transfer assessment.

* The Data Breach Response Policy (Document 14) — incidents at an importer trigger re-evaluation.

* The Regulatory Applicability Matrix (Document 7) — destinations and applicable regimes; the Data Inventory (Document 23) — flows and locations.

* Outcomes — the RoPA (Document 21) and the Privacy Risk Register (Document 22); process — the Privacy Governance Process Map (Document 24, core process C4).

## **8. Review and Amendment**

This document is reviewed under the ***[Policy Review Cycle, Document 29]***, and upon any change to an adequacy decision relied on, to the standard contractual clauses, to EDPB guidance on transfers, or to Documents 8, 12 or 18 that affects this procedure. Changes are adopted by ***[Executive Management]*** on the proposal of the ***[EPPO]***, after consulting ***[Legal]***, the ***[Privacy Risk Committee]*** and the DPO.

## **9. Approval**

This document is adopted by ***[Executive Management]*** on ***[date]***. Document Owner: ***[EPPO]***.

# **Part B — Worked Example: PanEuropean Bank AG**

**PanEuropean Bank AG — Transfer Impact Assessment Methodology**

*Effective Date: 20 October 2026  ·  Version: 2.0  ·  Document Owner: Chief Privacy Officer (EPPO)  ·  Adopted by: Management Board*

*A fictional legal entity, provided solely for illustrative purposes.*

***Fictional Document History (illustrative)***

| Version | Date | Changes |
| :---- | :---- | :---- |
| 1.0 | 1 March 2026 | First version, adopted by the Management Board together with Documents 8, 18, 19 and 22. Owner at the time: Group DPO |
| 2.0 | 20 October 2026 | Re-baselined to the new role model: Chief Privacy Officer as owner; General Counsel determines G-TIA; decisions to proceed by the single decider under Document 8, version 3.0 |

## **Glossary of Terms**

*The Part A glossary applies; the entries below add PanEuropean specifics.*

| Term | Definition / Reference |
| :---- | :---- |
| HBDI | The Hessian Commissioner for Data Protection and Freedom of Information (Der Hessische Beauftragte für Datenschutz und Informationsfreiheit), PanEuropean's lead supervisory authority. |
| PEP | The Bank's privacy engineering platform (PEP, illustrative), on which TIAs and evidence packs are recorded. It takes no decision. |

## **1. Purpose**

This document establishes how PanEuropean Bank AG identifies transfers, determines the mechanism, carries out TIAs for transfers relying on Art. 46 tools, and suspends or terminates transfers where essentially equivalent protection cannot be ensured, for the transfers recorded in the Cross-Border Data Transfer Policy (Document 12).

## **2. Scope of Application**

At 26 October 2026, PanEuropean relies on standard contractual clauses (Art. 46) for three transfers, each with its own TIA:

| Transfer | Importer and destination | Role and tool | Processing Owner |
| :---- | :---- | :---- | :---- |
| Remote technical support with access to production systems | Example Cloud Services Pvt Ltd (fictional), India — a separate legal entity | Processor; SCCs, controller-to-processor module (Module 2) | CIO |
| Anti-fraud matching of shared customers by private set intersection | Partner bank (fictional), India | Independent controller; SCCs, controller-to-controller module (Module 1) | Head of Fraud Prevention |
| Customer-service assistant based on a large language model | Example AI Provider Inc. (fictional), USA | Processor; SCCs, Module 2 | Head of Customer Service |

The federated-learning anti-fraud consortium involves only banks established in the EU; General Counsel's transfer-status determination is that it involves no importer in a third country and no international organisation, so Chapter V is not engaged. The conclusion is re-checked whenever the consortium's membership, coordinator or hosting changes; G-L, the Art. 26 arrangement and DPIA-FL-01 apply regardless. Staff of PanEuropean Bank AG who access the Bank's systems while travelling outside the EEA do not make a transfer (same legal entity); the access is governed by the Bank's security policy.

## **3. Triage — Mechanism and When a TIA Is Required**

***3.1 Mechanism Branches***

Part A, Section 3.1 applies. PanEuropean's position for its current importers:

* **Art. 45:** no adequacy decision covers India. For the United States, the adequacy decision of 10 July 2023 on the EU-U.S. Data Privacy Framework (upheld by the General Court in T-553/23, *Latombe*, September 2025) applies only to certified organisations for the data covered by their certification. Example AI Provider Inc. is assumed, for this illustration, not to be certified; the Art. 45 branch is therefore not available for TIA-LLM-01. If a US importer is certified, PanEuropean records an adequacy check record (scope, eligibility, validity, monitoring) and does not redo the Commission's assessment.
* **Art. 46:** standard contractual clauses (Commission Implementing Decision (EU) 2021/914) for all three transfers, each with a full TIA.
* **Art. 49:** not used for any of the three transfers. Any proposed use requires a derogation record by Legal & Compliance; derogations are exceptional, interpreted restrictively and subject to the specific conditions of the derogation used, including the occasional or non-repetitive character where that derogation requires it.

***3.2 When a TIA Is Performed or Re-Evaluated***

The triggers of Part A, Section 3.2 apply. Each TIA is re-evaluated at least annually and on any trigger event; TIAs with conditions are re-evaluated on the dates fixed in their G-TIA determination. Re-evaluation is tied to legal and monitoring events, not to the calendar of any tool.

***3.3 Transfer-Status Conclusions***

Part A, Section 3.3 applies. Conclusions are taken by General Counsel on documented evidence, with Group DPO advice:

| Scheme | Conclusion | Evidence |
| :---- | :---- | :---- |
| Federated-learning anti-fraud consortium | No transfer: all consortium members and the aggregation service are established in the EU; no data are made available to an importer in a third country. Re-checked on any change of membership, coordinator or hosting | EVP-2026-0041 (Art. 26 arrangement; consortium membership; DP statement and secure aggregation as evidence for DPIA-FL-01) |
| Private set intersection with the partner bank in India | Treated as a transfer: the protocol messages that reach the partner are derived from PanEuropean customer identifiers, and General Counsel did not conclude that they are not personal data for the partner. Standard contractual clauses (Module 1) and a full TIA apply | TIA-PSI-01 |

## **4. TIA Procedure at PanEuropean**

The procedure of Part A, Section 4 applies, with the mapping to the six EDPB steps. Records are kept on PEP.

| Step | Content |
| :---- | :---- |
| 4.1 Initiation | The Privacy Operations Lead registers the TIA on identifying a new transfer (including remote access by a separate entity or an onward transfer) or a trigger of Section 3.2 |
| 4.2 Description of the Transfer | Privacy Officer(s) and the Processing Owner's team describe the transfer from the Data Inventory (Document 23) and the vendor file (Document 17), including sub-processors and the format in which data are accessible to the importer |
| 4.3 Transfer Tool | Legal & Compliance selects and maintains the tool and module |
| 4.4 Legal Assessment of Laws and Practices | Legal & Compliance performs the mandatory module for each destination, with dated sources, against the European Essential Guarantees; Document 18 elements are requested from the Privacy Operations Lead where needed |
| 4.5 Supplementary Measures | The Processing Owner selects measures with the CISO (technical) and Legal & Compliance (contractual); effectiveness is assessed against the problem identified in step 4.4 |
| 4.6 G-TIA Determination | General Counsel determines pass or fail, with reasons and conditions, after Group DPO advice. Where a DPIA exists or is triggered, the result is passed to the DPIA team for G-L and the DPIA |
| 4.7 Decision to Proceed | After G-L and G-TIA pass and any DPIA and G-36 step are complete: Processing Owner up to Medium (Medium with the Chief Privacy Officer's concurrence for decisions from 23 October 2026, when Document 8, version 3.0, took effect); the Chief Risk Officer for High; Critical not acceptable. A failed G-TIA is not available for decision |
| 4.8 Suspension, Termination and Re-Evaluation | The Processing Owner suspends the transfer under Clause 14(f) (or Clause 16(b)) when General Counsel determines that equivalence can no longer be ensured; termination under Clause 14(f) or 16(c), with return or deletion under Clause 16(d); where PanEuropean terminates under Clause 16(c), Legal & Compliance informs the HBDI; the Group DPO is the HBDI's contact point. A suspended transfer resumes only after a new TIA and G-TIA pass |

**Transitional rule.** TIAs carried out before 1 March 2026 followed the Bank's interim procedure and are re-performed under this document at their next re-evaluation. Decisions to proceed taken before 23 October 2026 (the date on which Document 8, version 3.0, took effect) were taken under the authority then in force, without Chief Privacy Officer concurrence (the position exists only from 20 October 2026); conditional acceptances are re-assessed under Document 8, version 3.0, at expiry.

## **5. TIA Report Structure at PanEuropean**

The fields of Part A, Section 5 are used verbatim. Evidence packs have the format EVP-YYYY-NNNN.

## **6. Roles and Responsibilities**

| Role | Responsibility |
| :---- | :---- |
| Legal & Compliance (General Counsel) | Transfer-status conclusions; mechanism check; TIA of laws and practices; G-TIA determination with Group DPO advice; re-evaluation; maintains the SCCs with the three importers |
| Processing Owners (CIO — TIA-CLOUD-01; Head of Fraud Prevention — TIA-PSI-01; Head of Customer Service — TIA-LLM-01) | Transfer tool and supplementary measures; decision to proceed up to Medium after G-L and G-TIA pass; suspension and termination |
| Chief Risk Officer | Decision to proceed where the residual track (a) tier is High |
| Group DPO | Advice on transfer-status conclusions, TIAs, G-TIA and decisions; contact point for the HBDI |
| Chief Privacy Officer (EPPO) | Owns this document; concurs at Medium; consulted on decisions to proceed |
| Privacy Operations Lead | Identifies transfers in the data flow; registers TIAs; compiles evidence packs |
| Privacy Officer(s) / Privacy Engineer(s) | Describe transfers; support the assessment of technical measures and PET evidence |
| CISO / IT Management | Technical supplementary measures and their evidence |
| Procurement | Vendor due diligence under Document 17; DORA classification of ICT third-party arrangements is handled under Document 17 |

## **7. Relationship to Other Framework Documents**

* Policy and mechanism matrix — Cross-Border Data Transfer Policy (Document 12).

* Parallel DPIAs — DPIA-LLM-01 and DPIA-PSI-01 (Document 19); TIA-CLOUD-01 has a triage record without DPIA.

* Document 18 elements — severity and threat-based calculations for TIA-CLOUD-01 (no DPIA), PET and protocol evidence for TIA-PSI-01.

* Decision authority — Document 8, version 3.0, Section 5; roles — Document 5, Section 5.4.

* Vendor due diligence and sub-processors — Document 17; incidents — Document 14; flows — Document 23.

* Outcomes — RoPA (Document 21) and Privacy Risk Register (Document 22): PRR-CLOUD-01, PRR-PSI-01, PRR-LLM-01.

* Process — Privacy Governance Process Map (Document 24, C4).

## **8. Review and Amendment**

This document is reviewed annually under the Policy Review Cycle (Document 29) and upon any change to an adequacy decision, the standard contractual clauses, EDPB guidance on transfers, or Documents 8, 12 or 18 affecting this procedure. Changes are adopted by the Management Board on the proposal of the Chief Privacy Officer, after consulting General Counsel, the Privacy Risk Committee and the Group DPO. This document is not a Supervisory Board reserved consent matter.

## **9. Approval**

Version 1.0 was adopted by the Management Board on 1 March 2026 (owner at the time: Group DPO). Version 2.0 was adopted by the Management Board on 20 October 2026 on the proposal of the Chief Privacy Officer, after consulting General Counsel, the Privacy Risk Committee and the Group DPO. Document owner: Chief Privacy Officer.

# **Appendix to Part B — Worked TIAs**

The legal assessments below are illustrative. They describe the laws of the destinations only at a general level and are not legal advice on those laws; a real TIA records dated, verifiable sources for each statement.

| Importer | Destination | Identifier | G-TIA | Track (a) tier | Decision status |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Example Cloud Services Pvt Ltd (remote technical support) | India | TIA-CLOUD-01 | Pass for the restricted design; clear-text access from India excluded | Medium | Accepted with conditions (CIO, 20 March 2026; expiry 20 March 2027) |
| Partner bank (anti-fraud matching) | India | TIA-PSI-01 | Fail for the mutual-output design (suspended 12 February 2026); pass for the one-sided design without output to the partner, on stated illustrative assumptions (20 March 2026) | High (DPIA-PSI-01; re-assessed 26 October 2026) | Decision pending — Chief Risk Officer, after the prior consultation of the HBDI (G-36 met, 26 October 2026); sessions paused. The conditional acceptance of 25 March 2026 (Head of Fraud Prevention) is superseded |
| Example AI Provider Inc. (customer-service assistant) | USA | TIA-LLM-01 | Pass of 22 June 2026 (historical); current status at 26 October 2026: **G-TIA incomplete — HOLD**, pending verification of the FISA Section 702 status; no transfers while on hold | Medium (DPIA-LLM-01) | Acceptance of 25 June 2026 not in effect: AI path suspended from 26 October 2026; customer service human-only |

## **Report TIA-CLOUD-01**

| Report Field | Value |
| :---- | :---- |
| Identifier and Importer | TIA-CLOUD-01 — Example Cloud Services Pvt Ltd (fictional), India, processor, remote technical support for the Bank's infrastructure with access to production systems. RoPA record: RoPA-CLOUD-01. Privacy Risk Register: PRR-CLOUD-01 |
| Processing Owner and Dates | CIO; assessment by Legal & Compliance; version 1.0 of 15 January 2025 under the interim procedure; this report, version 2.0, re-evaluation under this document dated 12 March 2026 |
| Basis for Triage | Remote access by a separate legal entity in a third country to data held in the EEA is a transfer (EDPB Guidelines 05/2021: exporter subject to the GDPR; data made available by remote access to another entity acting as processor; importer in India). Trigger: scheduled re-evaluation and first assessment under this document. DPIA: triage record — one WP248 criterion (large scale); no presumption; no DPIA; Group DPO advice on the triage recorded |
| Description of the Transfer | Support engineers of the importer in India administer infrastructure components remotely. Data accessible: system telemetry, configuration and application logs relating to the Bank's customer systems (about 1.2 million customers, illustrative). Format after redesign: direct and network identifiers in logs are tokenised before logs leave the Bank's environment, with tokenisation keys held only by the Bank in the EEA; free-text fields are removed. No sub-processors at the report date; any new sub-processor requires the Bank's prior written authorisation under the Art. 28 contract (Document 17) |
| Mechanism and Transfer Tool | Art. 46 — standard contractual clauses, Module 2 (controller-to-processor). No adequacy decision covers India |
| Legal Assessment of Laws and Practices | (a) Indian law gives public authorities powers to direct the interception, monitoring or decryption of information in any computer resource, on grounds that include national security and public order (Information Technology Act, 2000, section 69, and its rules), and directions issued by CERT-In under that Act require certain service providers to report cyber incidents and to maintain logs and provide them on request. (b) Practices: Legal & Compliance found no published information from the importer on government requests and limited public information on how these powers are applied to service providers handling foreign customer data. (c) Redress: on the information available, Legal & Compliance could not identify independent oversight and effective redress that EU data subjects could use against such access, comparable to the European Essential Guarantees. (e) Conclusion: for any access by the importer to production customer data in clear text, the laws and practices may impinge on the effectiveness of the SCCs, and this could not be excluded. Sources and dates are listed in the evidence pack |
| Supplementary Measures and Their Effectiveness | (1) Clear-text access to production customer data from India is excluded by design: support sessions run through a privileged-access gateway in the EEA that masks customer data on screen; where clear-text access is unavoidable (incident handling), it is performed by the importer's EEA-based staff or by Bank staff ("break-glass" procedure, logged and approved per session) — effective, because no clear-text customer data are made available in India. (2) Tokenisation of identifiers in logs with keys held only by the Bank in the EEA, and removal of free-text fields — effective for the logs, because neither the importer nor the authorities of the destination can attribute the tokens with means reasonably likely to be used (EDPB Recommendations 01/2020, use case on transfer of pseudonymised data). (3) Encryption in transit; session recording; least-privilege, time-limited access — security measures, effective against misuse but not by themselves against compelled access. (4) Contractual: SCC Clause 15 commitments on public-authority requests (notification, review of legality, challenge, data minimisation) — supporting measure only |
| Document 18 Elements Requested | Calculation of the track (a) tier for the decision to proceed (no DPIA), Project 4 configuration: S1 — compelled or unauthorised access to tokenised logs and telemetry at the importer: L1 2 + L2 3 (capable state or criminal actor) + L3 1 residual (tokenisation with keys in the EEA, tested; masking gateway tested) / 3 inherent + L4 1 = 7 → High (inherent 9 → Near-certain); severity: data class Confidential 2 + scale 3 (≥ 1,000,000) + reach 1 (processor) = 6 → Moderate; residual High × Moderate = **Medium** (inherent Near-certain × Moderate = Medium). S2 — loss of integrity or availability of customer data through a support error: L1 2 + L2 2 + L3 0 (change management, four-eyes principle, tested) / 3 + L4 1 = 5 → Medium (inherent 8 → High); severity Restricted 3 + scale 3 = 6 → Moderate; Medium × Moderate = Low (inherent Medium). **Track (a): Medium** (inherent Medium). Track (b): applicable regime +1 (ICT third-party arrangement of a financial entity), financial 1, reputational 1 → 3 → Moderate |
| G-TIA Determination | General Counsel, 12 March 2026, with Group DPO advice: **pass** for the restricted design (no clear-text customer data accessible in India; tokenised logs with keys in the EEA). Clear-text access to production customer data from India does not take place; a change in the design to permit it would require a new TIA and would not pass on the current assessment. Condition: re-evaluation by 12 March 2027 and on any trigger of Section 3.2 |
| DPO Advice and Response | Group DPO advice, 10 March 2026: supported the restricted design; advised testing the masking gateway quarterly and recording each break-glass session in the evidence pack. Response: followed in full |
| DPIA and G-36 Link | Triage record (no DPIA; one WP248 criterion); G-36 therefore not evaluated. A DPIA would be triggered by a change giving the importer access to customer data in clear text |
| Decision and Authorised Role | CIO (Processing Owner), 20 March 2026, with Group DPO advice, under Document 8, version 1.0: the transfer continues in the restricted design; Medium accepted with conditions (quarterly masking test; break-glass logging; no clear-text access from India). Expiry: 20 March 2027; re-assessment under Document 8, version 3.0, with the Chief Privacy Officer's concurrence |
| Suspension, Termination and Supervisory Authority | Not applicable — the transfer was not suspended; the element that could not pass (clear-text access from India) was removed from the design before this re-evaluation was concluded |
| Reference to the Evidence Pack | EVP-2026-0008 |
| Next Re-Evaluation Date | 12 March 2027 at the latest (planned); earlier on any trigger of Section 3.2, including any change in the Indian legal framework or in CERT-In directions |

## **Report TIA-PSI-01**

| Report Field | Value |
| :---- | :---- |
| Identifier and Importer | TIA-PSI-01 — partner bank (fictional), India, independent controller, anti-fraud matching of shared customers by private set intersection. RoPA record: RoPA-PSI-01. DPIA: DPIA-PSI-01. Privacy Risk Register: PRR-PSI-01 |
| Processing Owner and Dates | Head of Fraud Prevention; assessment by Legal & Compliance; version 1.0 of 10 February 2025 under the interim procedure; version 2.0 of 10 February 2026 (re-evaluation); this report, version 2.1, re-assessment of the redesigned scheme dated 20 March 2026 |
| Basis for Triage | Transfer-status conclusion (Part B, Section 3.3): treated as a transfer. Triggers: scheduled re-evaluation (version 2.0) and change of the technical scheme (version 2.1). A DPIA is required in parallel (DPIA-PSI-01) |
| Description of the Transfer | Purpose: anti-fraud — identifying PanEuropean customers whose identities are linked to confirmed fraud at the partner bank. Version 2.0 (mutual-output design): both banks learned the intersection, so the partner received a list of matched PanEuropean customers. Version 2.1 (one-sided design without output to the partner, from 1 April 2026): only PanEuropean learns which identities match; the partner receives PanEuropean's identifiers only in blinded form under a session key held by PanEuropean in the EEA, and receives no match result, no intersection size and no other signal that depends on the result. What the partner can still observe is stated in the supplementary-measures row. Monthly sessions; about 1.2 million customer identifiers input (illustrative) |
| Mechanism and Transfer Tool | Art. 46 — standard contractual clauses, Module 1 (controller-to-controller). No adequacy decision covers India |
| Legal Assessment of Laws and Practices | (a) As in TIA-CLOUD-01 for the general framework (Information Technology Act, 2000, section 69; CERT-In directions), and access by Indian authorities to information held by regulated financial institutions under applicable Indian law. (b) Practices: the partner bank reported no public-authority requests concerning data received from foreign banks; Legal & Compliance found limited public information on practice. (c) Redress: as in TIA-CLOUD-01. (e) Conclusion: for the mutual-output design, matched customer data in clear text at the partner could be accessed by authorities, and essentially equivalent protection could not be shown. For the one-sided design, the questions are whether the blinded elements can be attributed by the partner or by authorities, and what the partner, or an authority compelling it, can learn from the authorised output |
| Supplementary Measures and Their Effectiveness | Version 2.0: SCC Clause 15 commitments and transport encryption only — not effective against public-authority access to matched data in clear text. Version 2.1: (1) one-sided output — the intersection and its size are computed and revealed only to PanEuropean; the protocol variant is chosen so that the partner's view is independent of the result; (2) blinding of PanEuropean's identifiers with a session key held only by PanEuropean in the EEA, using a protocol variant designed to resist a partner that deviates from the protocol; (3) PanEuropean's input is padded to a fixed, publicly known bound (illustrative: 1.5 million elements) and message lengths and timing are made independent of the number of matches; (4) key rotation per session; (5) transport encryption; (6) SCC Clause 15 commitments. Observable leakage (version 2.1): the partner learns only the padded input bound and the fact and timing of a monthly session — information that does not depend on which or how many identities match. Because the partner receives no output, a crafted or compelled partner list (for example, chosen identities submitted at the request of an authority) yields nothing to the partner or the authority. Illustrative security assumptions: the protocol and its implementation were reviewed by an independent cryptographer against these properties (one-sided output, malicious-partner security, padding and length/timing independence), and the review is repeated on any change of protocol or library; the session key never leaves the EEA. Hygiene controls that do not carry the equivalence conclusion: the partner commits to its confirmed-fraud list before each session (signed hash) and warrants its authenticity; PanEuropean acts on a match only after analyst review and never sends case-specific information back through this channel — any later request to the partner about a specific match is a separate disclosure, assessed case by case. Effectiveness: under these assumptions, the measures are effective as split processing — neither the partner nor the authorities of the destination can recover PanEuropean customer identifiers, or learn whether any identity is a PanEuropean customer, with means reasonably likely to be used. If the independent review cannot confirm properties (1) and (3), the design falls back to the version 2.0 conclusion. PSI does not exempt the flow from Chapter V; it is assessed here as a supplementary measure |
| Document 18 Elements Requested | Severity of harm if the matched list (version 2.0) were disclosed in the destination: Restricted 3 (Document 10: an offence-related list) + criminal-offence data 2 (Art. 10: the matched customers are linked to confirmed fraud) + scale 2 + reach 1 → 8 → Significant (informative only; corrected on 26 October 2026 — the earlier figure, Confidential 2 + scale 2 + reach 1 = 5 → Moderate, used the wrong data class and omitted the Art. 10 modifier). Track (a) tier for the decision to proceed: from DPIA-PSI-01 — **High** (inherent High), as re-assessed on 26 October 2026 |
| G-TIA Determination | Version 2.0 — General Counsel, 10 February 2026, with Group DPO advice: **fail** for the mutual-output design. Version 2.1 — General Counsel, 20 March 2026, with Group DPO advice: **pass** for the one-sided design without output to the partner, on the stated illustrative security assumptions, on condition that no match result, intersection size or other result-dependent signal reaches the partner, the input padding and length/timing independence are maintained, the key remains in the EEA and the independent protocol review is current; a session that would breach these conditions is refused, and any evidence that the partner can observe a result-dependent signal leads to suspension under Clause 14(f); re-evaluation within 12 months |
| DPO Advice and Response | Group DPO advice, 9 February 2026: advised suspension of the mutual-output sessions — followed. Group DPO advice, 18 March 2026: supported the one-sided design; advised documenting the independent protocol review and testing transliteration rules for names — followed |
| DPIA and G-36 Link | DPIA-PSI-01: track (a) High (re-assessed 26 October 2026 with the Art. 10 severity modifier); G-36 re-evaluated — test met (Legal & Compliance, 26 October 2026, with Group DPO advice): the HBDI is consulted before any further session. Historical: the conclusion of 24 March 2026 (test not met) is superseded |
| Decision and Authorised Role | Version 2.0: not available — G-TIA failed. Version 2.1, historical: Head of Fraud Prevention (Processing Owner), 25 March 2026, with Group DPO advice, under Document 8, version 1.0: the one-sided transfer may start; Medium accepted with conditions (analyst review before any action on a match; no output of any kind to the partner; input padding and length/timing independence; key in the EEA; current independent protocol review; partner list commitment); expiry 25 March 2027. Superseded on 26 October 2026, when the DPIA was re-assessed at High. Current: decision pending — the Chief Risk Officer (Document 8, version 3.0, Section 5) decides after the prior-consultation step; the Head of Fraud Prevention paused the sessions on 26 October 2026, and no session is run until the consultation step and that decision are recorded (the next monthly session is not held). The G-TIA determination of 20 March 2026 is not affected |
| Suspension, Termination and Supervisory Authority | The Head of Fraud Prevention suspended the mutual-output sessions under SCC Clause 14(f) on 12 February 2026, following the G-TIA failure. The contract was not terminated; the clauses were amended consistently with the SCCs to reflect the one-sided design, and sessions resumed under it on 1 April 2026. No termination under Clause 16(c) took place, so no information to the HBDI was required under that clause; the Group DPO informed the Management Board of the suspension |
| Reference to the Evidence Pack | EVP-2026-0005 (version 2.0); EVP-2026-0016 (version 2.1) |
| Next Re-Evaluation Date | 20 March 2027 at the latest (planned); earlier upon any change of protocol, key management or participants, or of the Indian legal framework |

## **Report TIA-LLM-01**

Example AI Provider Inc. is fictional; its attributes are illustrative assumptions, not statements about any real provider.

| Report Field | Value |
| :---- | :---- |
| Identifier and Importer | TIA-LLM-01 — Example AI Provider Inc. (fictional), USA, processor, hosted large language model used by the customer-service assistant. RoPA record: RoPA-LLM-01. DPIA: DPIA-LLM-01. Privacy Risk Register: PRR-LLM-01 |
| Processing Owner and Dates | Head of Customer Service; assessment by Legal & Compliance; version 1.0 of 1 July 2025 under the interim procedure; this report, version 2.0, re-evaluation dated 22 June 2026 |
| Basis for Triage | Transfer: the Bank makes customer messages available to a processor established in the USA. Trigger: scheduled re-evaluation. DPIA in parallel: DPIA-LLM-01 |
| Description of the Transfer | Data: customer messages with account numbers, card numbers and national identification numbers masked before sending, and internal knowledge-base articles (no customer records are retrieved from the CRM or other systems); incidental special-category content cannot be excluded (DPIA-LLM-01). Format: clear text at the importer, which needs the content to generate summaries and drafts. Volume: messages of about 300,000 customers a year (illustrative). Illustrative contract terms: deletion of prompts and outputs within 30 days; no training on customer data. Sub-processors: hosting in the USA (illustrative); any new sub-processor requires the Bank's prior written authorisation (Document 17) |
| Mechanism and Transfer Tool | Art. 46 — standard contractual clauses, Module 2 (controller-to-processor). Art. 45: the importer is not certified under the EU-U.S. Data Privacy Framework — illustrative assumption, checked on 22 June 2026 — so the adequacy decision does not cover this transfer |
| Legal Assessment of Laws and Practices | (a) US law allows the collection of foreign intelligence information from electronic communication service providers, including under Section 702 of the Foreign Intelligence Surveillance Act (FISA); the importer may fall within the categories of providers concerned. Executive Order 14086 (October 2022) introduced limitations on signals-intelligence activities (necessity and proportionality, defined legitimate objectives) and a redress mechanism including the Data Protection Review Court; these safeguards apply to signals-intelligence activities generally and not only to DPF-certified recipients, and Legal & Compliance took them into account. (b) Practices: the importer's published transparency information (illustrative) reports no requests concerning EU business customers' content; (c) Redress: the EO 14086 mechanism is available to individuals in the EU through their supervisory authority. (d) Legal snapshot recorded by Legal & Compliance: *FISA Section 702* — the statutory authority was due to sunset on 12 June 2026, and a further short extension was not passed before that date (Congressional Record, 10 June 2026); floor statements in that record refer to the statute's transition rules, under which certifications already approved and directives issued under them continue in effect until their own expiry (stated as at least through March 2027). At the assessment date (22 June 2026) Legal & Compliance therefore treated the sunset of the statute as **not** ending collection, and assessed the transfer on the assumption that Section 702 collection continues. At the monitoring review of 26 October 2026, whether the statute had been reauthorised or amended after 12 June 2026, and on what terms, could not be confirmed from primary sources; the transition text itself had not yet been checked against the statute. *EO 14086* — the European Commission states that the safeguards of the Executive Order apply to all transfers to companies in the United States, whatever the transfer mechanism used (Commission page on EU-US data transfers, accessed 26 October 2026); no revocation was identified in the sources checked. *DPF adequacy decision* — in force at 26 October 2026; upheld by the General Court (T-553/23, *Latombe*, 3 September 2025); any further proceedings are monitored. The missing DPF certification of the fictional importer only closes the Art. 45 branch; it is not by itself a G-TIA failure. (e) Conclusion: at 22 June 2026, on the documented sources and the conservative assumption in (d), the laws and practices, taking the EO 14086 safeguards into account, do not prevent the importer from fulfilling its obligations under the SCCs for this transfer. At 26 October 2026: **legal assessment incomplete — pending verification of the statutory status of FISA Section 702 after 12 June 2026 (reauthorisation, amendment or continued lapse) and of the statutory transition text** |
| Supplementary Measures and Their Effectiveness | (1) Masking of identifiers before sending — reduces the data in scope; effective as minimisation, not as protection of the message content. (2) SCC Clause 15 commitments (notification of requests, review of legality, challenge, minimisation of disclosure) and an additional commitment to publish transparency information — supporting measures. (3) Exclusion of sensitive channels and routing of flagged messages to human-only handling — reduces exposure of the most sensitive content. (4) Encryption in transit and at rest at the importer — security measure; not effective against compelled access, because the importer holds the keys and needs the data in clear text. (5) No-training and 30-day deletion terms — address misuse by the importer, not public-authority access. Given the conclusion of step 4.4, no further technical measure is required for G-TIA; measures (1) and (3) are maintained as conditions |
| Document 18 Elements Requested | None beyond DPIA-LLM-01. Track (a) tier for the decision to proceed: from DPIA-LLM-01 — **Medium** (inherent High) |
| G-TIA Determination | General Counsel, 22 June 2026, with Group DPO advice: **pass** on the conservative assumption that Section 702 collection continues, on condition of re-evaluation within 12 months and immediately upon any change to FISA Section 702, to EO 14086 or its redress mechanism, to the status of the DPF adequacy decision, or to the importer's sub-processors or terms (historical determination). Monitoring review, 26 October 2026: **G-TIA incomplete — HOLD**. The items listed in point (e) of the legal assessment above could not be verified against primary legal sources, so the 22 June determination is not a current pass. Under the gate, an incomplete assessment does not allow transfers: no personal data are transferred to the importer until General Counsel records a current pass. A continued lapse of Section 702 would not by itself weaken the assessment, because it already assumed continuing collection; a reauthorisation with a wider scope or fewer safeguards could change it. If the verification shows that essentially equivalent protection cannot be ensured, the suspension continues under Clause 14(f) and the arrangement is terminated or redesigned |
| DPO Advice and Response | Group DPO advice, 20 June 2026: agreed with the pass; advised obtaining the importer's commitment to publish transparency information and recording the sources and their dates. Response: followed in full |
| DPIA and G-36 Link | DPIA-LLM-01: track (a) Medium; G-36 evaluated — test not met (Legal & Compliance, 22 June 2026) |
| Decision and Authorised Role | Historical: Head of Customer Service (Processing Owner), 25 June 2026, with Group DPO advice, under Document 8, version 1.0: the transfer could proceed; Medium accepted with conditions in DPIA-LLM-01 (expiry 25 June 2027). Current: following the G-TIA hold, the Head of Customer Service suspended the AI path on 26 October 2026 under Clause 14(f); customer enquiries are handled by human agents only, in the Bank's existing EU customer-service channel, until a current pass is recorded. The conditional acceptance of 25 June 2026 is not in effect while the hold applies; resumption requires a current G-TIA pass and a re-assessment under Document 8, version 3.0, with the Chief Privacy Officer's concurrence |
| Suspension, Termination and Supervisory Authority | Not applicable |
| Reference to the Evidence Pack | EVP-2026-0030 |
| Next Re-Evaluation Date | Verification of the open items against primary legal sources (target 30 November 2026); the AI path stays suspended until it is complete and a current pass is recorded; full re-evaluation 22 June 2027 at the latest; earlier on any change listed in the G-TIA determination |

# **Normative Basis and References**

**EU law and case law**
* Regulation (EU) 2016/679 (GDPR): Arts. 3, 5, 6, 26, 28, 32, 35, 36, 44–49, 58(2)(j); Recitals 26, 101–115.
* Commission Implementing Decision (EU) 2021/914 on standard contractual clauses for the transfer of personal data to third countries — Clauses 14, 15 and 16 (official Commission resources: https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/standard-contractual-clauses-scc_en).
* European Commission, register of adequacy decisions (https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/adequacy-decisions_en); Commission Implementing Decision of 10 July 2023 on the adequate level of protection under the EU-U.S. Data Privacy Framework.
* CJEU, C-311/18, *Data Protection Commissioner v Facebook Ireland and Schrems*, 16 July 2020.
* CJEU, C-413/23 P, *EDPS v SRB*, 4 September 2025, ECLI:EU:C:2025:645, paragraphs 105–110 (identifiability assessed in context; cited as context for Chapter V, not as a new rule), https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A62023CJ0413.
* EDPB-EDPS Joint Opinion 2/2026 on the Digital Omnibus proposal, adopted 10 February 2026, paragraph 19 (further guidance on the implications of *EDPS v SRB* for Arts. 26 and 28 and Chapter V), https://www.edpb.europa.eu/system/files/2026-02/edpb_edps_jointopinion_202602_digitalomnibus_en.pdf — an opinion on a proposal, not law.
* General Court, T-553/23, *Latombe v Commission*, 3 September 2025 (DPF adequacy decision upheld).

**EDPB guidance**
* EDPB Recommendations 01/2020 on measures that supplement transfer tools to ensure compliance with the EU level of protection of personal data, version 2.0, adopted 18 June 2021 (https://www.edpb.europa.eu/documents/recommendation/recommendations-012020-on-measures-that-supplement-transfer-tools-to_en).
* EDPB Recommendations 02/2020 on the European Essential Guarantees for surveillance measures, adopted 10 November 2020.
* EDPB Guidelines 05/2021 on the interplay between the application of Article 3 and the provisions on international transfers as per Chapter V of the GDPR, version 2.0, Section 2.2 and Example 8.1 (https://www.edpb.europa.eu/system/files/2023-02/edpb_guidelines_05-2021_interplay_between_the_application_of_art3-chapter_v_of_the_gdpr_v2_en_0.pdf).
* EDPB Guidelines 2/2018 on derogations of Article 49 under Regulation 2016/679.

**Destination laws (general level only)**
* United States: Foreign Intelligence Surveillance Act, Section 702 (50 U.S.C. 1881a), and the transition provisions of the statutes that enacted and reauthorised it — status after 12 June 2026 pending verification; Executive Order 14086 on Enhancing Safeguards for United States Signals Intelligence Activities (7 October 2022).
* Congressional Record, vol. 172, 10 June 2026 (House and Senate proceedings on Section 702), https://www.govinfo.gov/content/pkg/CREC-2026-06-10/pdf/CREC-2026-06-10.pdf (accessed 26 October 2026) — floor statements, not statutory text.
* European Commission, "EU-US data transfers" (page on the Data Privacy Framework and the application of the EO 14086 safeguards to all transfer mechanisms), https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/eu-us-data-transfers_en (accessed 26 October 2026).
* India: Information Technology Act, 2000, section 69; directions issued by CERT-In under that Act.

**Other**
* CNIL, *Guide pratique — Analyse d'impact des transferts de données (AITD)*, final version (2025) — practical method, consistent with the EDPB steps.

# **International Adaptation**

The GDPR is the baseline of this methodology. Where other regimes apply:

* **UK GDPR / Data Protection Act 2018** (as amended by the Data (Use and Access) Act 2025, phased commencement): transfers rely on UK adequacy regulations or on appropriate safeguards such as the International Data Transfer Agreement (IDTA) or the International Data Transfer Addendum to the EU standard contractual clauses, with a transfer risk assessment; the 2025 Act introduces a revised test for transfers — check the commenced text before relying on it.
* **Switzerland (revFADP):** transfers rely on the Federal Council's list of countries with adequate protection or on safeguards such as standard contractual clauses recognised by the FDPIC with Swiss adaptations. For the United States, the Swiss-U.S. Data Privacy Framework provides adequacy for recipients certified under it, from 15 September 2024 (FDPIC). It is a separate route: the recipient must hold the Swiss-U.S. certification, and an EU-U.S. DPF certification does not cover Swiss transfers. The check record follows Document 12, Part A, Section 4.1. The UK Extension to the EU-U.S. DPF is likewise separate and applies to transfers under UK law.
* **Canada — PIPEDA:** there is no adequacy regime; an organisation remains accountable for personal information it transfers to a third party for processing and uses contractual or other means to provide a comparable level of protection (Schedule 1, Principle 4.1.3); individuals should be informed that their information may be processed in another jurisdiction and may be accessible to its authorities.
* **Canada — Québec (P-39.1, as amended by Law 25):** before communicating personal information outside Québec, the enterprise conducts a privacy impact assessment that takes into account, among other things, the sensitivity of the information, the purposes, the protection measures (including contractual ones) and the legal framework of the destination; the communication requires a written agreement and may proceed only if the assessment shows that the information would receive adequate protection. Use the private-sector Act's own provisions. The applicability map is in Document 7.
* No claim of full compliance with any jurisdiction is made.

# **Document History (PGF)**

| Release | Date | Changes |
| :---- | :---- | :---- |
| 1.0.0-rc.1 | 2026-10-26 | Canonical English Markdown; changes from internal ver.2: transfer defined by the three cumulative criteria of EDPB Guidelines 05/2021 v2.0 (same-entity employee remote access is not a transfer; remote access by a separate entity is); G-TIA branched by mechanism (Art. 45 scope/eligibility/validity check and monitoring; Art. 46 full TIA with supplementary measures; Art. 49 exceptional and restrictive, subject to the conditions of each derogation); separate lawful-basis and Chapter V tests; Art. 48 pointer; mandatory legal module on laws and practices of the destination (public-authority access against the European Essential Guarantees, practices, enforceable rights and redress, other laws), performed in this document, with Document 18 limited to requested elements; supplementary-measure effectiveness assessed against the specific problem; "no start or suspension" where equivalence cannot be ensured, with SCC Clause 14(f) suspension, Clause 16(b)–(d) and the Clause 16(c) information duty cited correctly; the statement that Art. 36 is "unrelated to cross-border transfer" removed (DPIA and Art. 36 may apply in parallel); PETs, TEEs, homomorphic encryption and remote access not treated as exemptions; the former three-condition test for PET schemes (with a DPO determination and a numerical threshold) replaced by a controller transfer-status conclusion by Legal on documented evidence, with DPO advice; DPO decision and approval roles removed; single decider for the decision to proceed under Document 8; re-evaluation tied to legal and monitoring events, not to tool recertification; the three worked TIAs redone: TIA-CLOUD-01 (Processing Owner CIO; clear-text access from India excluded), TIA-PSI-01 (Head of Fraud Prevention; anti-fraud purpose; SCC Module 1; mutual-output design failed and was suspended under Clause 14(f); one-sided design passed), TIA-LLM-01 (replaces the former TIA naming a real AI vendor; Head of Customer Service; fictional Example AI Provider Inc. not DPF-certified as an illustrative assumption, which closes only the Art. 45 branch; dated US legal snapshot — FISA s.702 sunset of 12 June 2026 not treated as ending collection, status after that date recorded as legal assessment incomplete pending verification; EO 14086 and DPF status with dated sources); PSI observable leakage and illustrative partner-input assumptions stated; C-413/23 P and EDPB-EDPS Joint Opinion 2/2026 cited as context only (importer inability to attribute does not remove the exporter from Chapter V); intra-EEA flows and international organisations distinguished; the FL evidence pack renumbered EVP-2026-0041 and the FL consortium treated as intra-EU; evidence packs in EVP-YYYY-NNNN format; product names removed; example dates shifted by −12 months and the fictional history re-baselined (version 2.0 of 20 October 2026); International adaptation (UK IDTA/Addendum, Switzerland, PIPEDA, Québec assessment before communication outside Québec) and references added. Integration pass: TIA-LLM-01 data description aligned with DPIA-LLM-01 (knowledge-base articles; no retrieval of customer records). Review correction: in TIA-PSI-01, the Document 18 elements and the decision updated after the re-assessment of the parallel DPIA on 26 October 2026 (Art. 10 severity modifier; G-36 met; Chief Risk Officer decision pending; sessions paused); G-TIA unchanged |
