---
title: "Data Retention and Disposal Policy"
document_id: PGF-11
level: 2
release_version: 1.0.0-rc.1
status: release-candidate
authors: ["Alexey Neyman", "Val Khvatov"]
regulatory_reference_date: 2026-10-26
licence_proposed: "CC BY 4.0 (proposed; subject to rights-holder confirmation)"
source_provenance: "Derived from internal source set ver.2: Level2/11. Data-Retention-Disposal-Policy_ENG.docx.md; sha256 f47b66c7d59f75a7a7b8b2e2904fd359a579e28c8b43be9290b53edfce11e6ae"
---

# PGF-11 — Data Retention and Disposal Policy

*Privacy Governance Framework (PGF) · Level 2 — Policies and Standards · Release 1.0.0-rc.1 · Regulatory reference date: 26 October 2026*

> **Status and use.** Part A is a reusable template. Part B is a worked example for a fictional organisation (PanEuropean Bank AG); all names, figures, dates and records in Part B are illustrative. Nothing in this document is legal advice or a statement about any real organisation, product or provider.

# **About This Document**

**Purpose.** Document 11 sets how long personal data are kept and how they are disposed of: for each data category it records the purpose and basis, the trigger, the jurisdiction, the duration and the exceptions. It adds a restricted (blocked) state for data kept only to meet a legal obligation or under a restriction, a scoped legal-hold procedure, rules for derived data (anonymous information, synthetic data, training datasets, open releases) and the retention of evidence packs and decision records.

**Scope.** All personal data to which the Data Classification Policy (Document 10) has assigned a data class. The document is tagged [DG]: it is a privacy overlay on the corporate records retention schedule, not a parallel schedule.

**Relationships.** Data class — Document 10; processing activities — Document 21; customer-facing retention statements — Document 1 (01B, Section 11), which mirrors the matrix; erasure on request — Document 15; consent records — Document 13; anonymity conclusions and the PET Assessment Module — Document 18; evidence-pack integrity — Document 9, Section 4.1; transfers of archived data — Document 12.

# **How to Use This Document**

Part A is a template. Text in ***[square brackets, bold italic]*** is a fill-in or illustrative placeholder. Blocks marked **Guidance** are removed from the adopted version. Part B shows the template completed for the fictional PanEuropean Bank AG; periods marked "illustrative internal value" are design choices of the fictional bank, not legal requirements.

> **Guidance.** Build on the Data Classification Policy (Document 10) and the RoPA (Document 21). Do not fill the matrix with a single period per data domain: a statutory retention duty covers specific record types, not "all customer data". Validate every statutory period against the current consolidated text of the law of each jurisdiction before adoption.

# **Table of Contents**

**About This Document**
**How to Use This Document**
**Part A — Template**
1. Purpose
2. Status as a Privacy Overlay on Data Governance
3. Scope (3.1 Anonymous Information; 3.2 Synthetic Datasets; 3.3 Model Training Datasets; 3.4 Open Data Publication; 3.5 Erasure and Withdrawal Cascade to Derived Data)
4. Retention Principles (4.1 Restricted Retention State)
5. Retention Period Matrix
6. Disposal Procedure (6.1 Evidence Packs and Decision Records)
7. Exceptions (Legal Hold, Investigations, Portfolio Transfer)
8. Roles and Responsibilities
9. Relationship to Other Framework Documents
10. Review and Amendment
11. Approval
**Part B — Worked Example: PanEuropean Bank AG** (same structure)
**Normative Basis and References**
**International Adaptation**
**Document History (PGF)**

# **Part A — Template**

**Data Retention and Disposal Policy of *[Legal name of organisation]***

*Effective date: **[DD Month YYYY]**  ·  Version: **[x.x]**  ·  Document owner: **[Executive Privacy Programme Owner (EPPO)]**  ·  Corporate retention schedule owned by: **[Head of Data Governance / Records Management]**  ·  Adopted by: **[Executive Management]***

***Version History***

| Version | Date | Changes |
| :---- | :---- | :---- |
| ***[1.0]*** | ***[DD Month YYYY]*** | ***[First version of the document]*** |
| ***[x.x]*** | ***[DD Month YYYY]*** | ***[Brief description of material changes]*** |

## **1. Purpose**

This document establishes retention periods for personal data by category and process, and the procedure for their disposal on expiry. Like the Data Classification Policy (Document 10), it is a privacy overlay on the existing corporate records retention schedule of ***[organisation name]***.

## **2. Status as a Privacy Overlay on Data Governance**

***[Confirm that the organisation has a corporate records retention schedule owned by Data Governance / Records Management. Boundary rule: Data Governance owns the schedule as a whole, including non-personal records (financial, operational, corporate); the privacy function adds the rows and fields specific to personal data, special-category data and criminal-offence data. Erasure on a data subject's request is governed by the Data Subject Rights Policy (Document 15); an earlier erasure under such a request takes precedence over a scheduled period unless an exception under Art. 17(3) applies, in which case the data move to the restricted state (Section 4.1).]***

> **Guidance.** The boundary rule is set in the Interface and Integration Model (Document 3, Section 3.3) and is applied here.

## **3. Scope**

* All personal data to which Document 10 has assigned a data class, whatever the format or location.
* The unit of regulation is the "data category / process" (record type), not an individual record; the matrix (Section 5) fixes the boundary.

This document does not govern:

* data classification — Document 10;
* disposal as a technical operation (secure erasure, cryptographic erasure, media sanitisation) — the boundary with IT and Information Security is set in Document 3, Section 3.2; the standards applied are named in Section 6;
* erasure as a request-handling procedure — Document 15;
* transfers of archived data to a third country — Document 12.

Boundaries of application to derived data:

***3.1 Anonymous Information***

* ***[Data are outside this document only while the controller's conclusion that they are anonymous information under Recital 26 stands. The conclusion is taken by the Processing Owner on Legal's assessment, with DPO advice, supported by the PET Assessment Module of the Privacy Risk Assessment Methodology (Document 18, Section 3.3); it considers the means reasonably likely to be used by the controller or by any other person, and is re-assessed at least [annually] and whenever new auxiliary data, a new attack, a further release from the same source population or a change of recipient becomes known. If a re-assessment does not confirm the conclusion, the data return to the scope of this document and to their earlier row of the matrix. Techniques follow the PET Standard (Document 9, Section 6).]***

***3.2 Synthetic Datasets***

* ***[Synthetic datasets generated from personal data are treated as personal data in the data class of their source (Document 10, Section 4.3) and are governed by this document. Synthetic records are generated by a model and may still disclose information about people in the source data; checks and restrictions under Document 18, Section 3.3.2, apply before use or disclosure. A synthetic dataset is never "public" or "open" by default: it leaves the scope of this document only through an anonymity conclusion under Section 3.1, and it may be published only under Section 3.4.]***

***3.3 Model Training Datasets***

* ***[Training datasets built on personal data (including pseudonymised data) are governed by this document and are retained only as long as the purpose requires — typically until the model version is decommissioned, plus any period needed for validation evidence. Where prudential model-risk or internal-model requirements, or other law, require retention of data histories for validation or back-testing, that basis and period are recorded as a separate row; otherwise the data are deleted at the end of the period or made anonymous under Section 3.1. The AI Act's documentation and record-keeping duties for high-risk AI systems concern the technical documentation (Art. 18) and automatically generated logs (Art. 19), not the retention of raw training data as such. Model validation is a matter for [the model-risk / AI governance function], which notifies [the Data Steward] of a model's decommissioning date (Document 3, Section 3.5).]***

***3.4 Open Data Publication***

* ***[Open publication of information derived from personal data is permitted only where: (a) G-L is passed — a release that would disclose identifiable special-category data without an applicable Art. 9(2) condition fails G-L, and any stricter internal policy (for example, no special-category attributes in any open release) is labelled as internal policy; (b) the PET Assessment Module of Document 18 is passed for the release; and (c) the Processing Owner has recorded, on Legal's assessment with DPO advice, the conclusion that the released information is anonymous, with "anyone" as the recipient. The conclusion is made before each release and re-assessed at least [annually]; because a publication cannot be withdrawn, the re-assessment also decides whether further releases must stop. The source data stay in their own row of the matrix; the release record is kept under Section 6.1.]***

***3.5 Erasure and Withdrawal Cascade to Derived Data***

* ***[When personal data must be erased — at the end of a retention period, on an erasure request (Art. 17) or on withdrawal of consent where consent was the basis — erasure is propagated along the data lineage to every derived dataset that is personal data, including pseudonymised copies, feature stores, analytics extracts and synthetic datasets for which no anonymity conclusion has been made. For models and synthetic datasets trained on the data, the [Processing Owner] records whether the person's data must be removed by retraining or regeneration, or whether exclusion from the next scheduled training or generation run is sufficient, and the reasons; at minimum, the data are excluded from every subsequent run. Data covered by a standing anonymity conclusion (Section 3.1) are not affected. Exceptions under Art. 17(3) move the data to the restricted state (Section 4.1) instead of erasure.]***

## **4. Retention Principles**

* ***[Retention limited by purpose — the period is set by the purpose for which the data were collected (Document 1), not by storage capacity. When the purpose is fulfilled, the data are deleted unless a separate legal basis requires further retention of specific records (Art. 5(1)(e)).]***

* ***[Scoped retention, not the longest period for everything — where several bases with different periods apply to a data category, each subset of records is kept for the period its own basis requires. A longer statutory period for some record types (for example accounting records) does not justify keeping the whole customer file for that period. Records kept only for a longer basis enter the restricted state (Section 4.1); the rest are deleted. The matrix records each basis and its record types separately.]***

* ***[Trigger, not creation date — each period runs from a defined trigger (end of the relationship, end of the calendar year in which a record was created, closure of a case, date of a decision); the matrix states it in a separate column, as the applicable law defines it.]***

* ***[Jurisdiction — where branches or subsidiaries are subject to different national rules, the matrix states the jurisdiction of each row; a German period is not applied to a French branch record, and vice versa.]***

* ***[Anonymisation as an alternative to deletion — permitted only through an anonymity conclusion under Section 3.1 and only where it does not conflict with the basis for retention.]***

* ***[Minimisation of retention records — logs, evidence packs and minimal records kept after disposal contain no more personal data than needed and have their own periods (Sections 6 and 6.1).]***

***4.1 Restricted Retention State***

***[The restricted (blocked) state applies to: (a) records kept after the primary purpose has ended only to meet a statutory retention duty (for example commercial, tax or anti-money-laundering record-keeping); (b) data whose processing is restricted at the data subject's request under Art. 18; (c) data under a legal hold (Section 7). In this state the data are stored, flagged, segregated or access-restricted to the roles that need them for the specific purpose, and not used for any other purpose. For (b), processing other than storage takes place only with the data subject's consent, for legal claims, for the protection of another person's rights or for important public interest (Art. 18(2)). The state ends with deletion at the end of the relevant period, or on the lifting of the restriction or release of the hold, when the record returns to its ordinary row.]***

## **5. Retention Period Matrix**

> **Guidance.** The matrix is the central artefact. Each row corresponds to a data category or process recorded in the RoPA (Document 21) and linked to a data class (Document 10). State the purpose and basis, the trigger, the jurisdiction, the duration and the exceptions for each row; where one domain contains record types with different bases, split it into rows.

| Data Category / Record Type | Data Class (Document 10) | Purpose and Basis | Trigger | Jurisdiction | Retention Period | Exceptions / Restricted State | Disposal Method |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| ***[Category 1]*** | ***[level / category / state]*** | ***[purpose; law / contract]*** | ***[event]*** | ***[country]*** | ***[period]*** | ***[legal hold; Art. 18; restricted state]*** | ***[method / system]*** |
| ***[Category 2]*** | ***[level / category / state]*** | ***[purpose; law / contract]*** | ***[event]*** | ***[country]*** | ***[period]*** | ***[…]*** | ***[…]*** |

## **6. Disposal Procedure**

* ***[Technical mechanism — irrecoverable deletion from record systems, cryptographic erasure for encrypted stores, or physical destruction of media, applied under standards approved by IT and Information Security (for example NIST SP 800-88, Guidelines for Media Sanitization, and ISO/IEC 27040). Where categories are served by different systems (CRM, analytics platform, video-surveillance system, HR system) or held by a processor, state the mechanism per system or provider; for processors, disposal is an Art. 28(3)(g) contract duty, evidenced by a deletion confirmation or certificate of destruction.]***

* ***[Organisational procedure — run frequency [e.g. monthly or quarterly] → automated identification of records that have reached the end of their period under Section 5 → check against active legal holds, Art. 18 restrictions and open requests (Section 7) → deletion, restricted state or anonymisation (Section 3.1) → propagation to derived data (Section 3.5) → entry in the disposal log.]***

* ***[Backups — records deleted in the primary system but still in backups are put beyond use: the backup copy is not used to restore them outside a disaster-recovery procedure, and if it is restored, the deletion is re-applied before the system returns to service; the copy is overwritten within [maximum backup rotation period].]***

* ***[Disposal log — date, category, volume, method, system and responsible role; no content of the disposed records. Retained for [period], because it evidences compliance with storage limitation.]***

***6.1 Evidence Packs and Decision Records***

* ***[Evidence packs, DPIA reports, TIAs, risk-acceptance and anonymity-conclusion records are retained by the applicable rule — for example, for as long as the processing or the released artefact exists and afterwards for [period] in which the decision can be examined by the supervisory authority or in legal proceedings — not by default for the longest period found in the schedule. A longer period applies only where a specific rule requires it (for example, the AI Act technical-documentation period for a provider of a high-risk AI system) or under a legal hold.]***
* ***[Integrity: sealed versions, superseded rather than edited (Document 9, Section 4.1). Immutable storage does not override deletion or redaction duties; personal data inside evidence packs are kept in separately sealed components so that they can be deleted at the end of their own period.]***
* ***[After a pack or component is purged, a minimal record (identifier, dates, hash, reason for deletion) is kept only where lawful and necessary — for example to demonstrate the disposal — and for its own defined period.]***

## **7. Exceptions**

* ***[Legal hold — scheduled disposal is suspended for specified records where they are relevant to actual or reasonably anticipated litigation, a regulatory or supervisory investigation, or a statutory request. The hold is issued by [Legal] and is **scoped**: it names the matter, the record categories, systems and custodians, and the period of the records concerned; it does not suspend disposal of unrelated records. Data under hold are in the restricted state (Section 4.1).]***

* ***[Review — each active hold is reviewed by [Legal] at least every [three months]; the review confirms the scope or narrows it, or releases the hold. A hold may not remain in force without review.]***

* ***[Release — on release, records whose ordinary period has already expired are disposed of within [X days] of the release. A separate off-cycle disposal run is not required only if the next scheduled cycle falls within those [X days]. The release, its date and the disposal are recorded.]***

* ***[Regulatory investigation — where a supervisory authority or financial supervisor requests that records be preserved, a legal hold is issued under the rules above.]***

* ***[Portfolio transfer / reorganisation — where a data portfolio is sold or transferred (M&A, assignment), the acquirer becomes a controller in its own right and sets its own retention under its own legal bases. The transfer agreement contains contractual commitments on retention and deletion where needed; the transferor deletes or restricts its own copies under its own matrix. Where the acquirer is in a third country, Document 12 applies.]***

## **8. Roles and Responsibilities**

| Role | Responsibility |
| :---- | :---- |
| ***[EPPO]*** | ***[Accountable for the retention schedule's personal-data dimension (Document 5, row S2.1): drafts and maintains this document and the matrix for adoption by Executive Management]*** |
| ***[Privacy Operations Lead, Legal]*** | ***[Responsible for preparing the matrix rows; Legal validates statutory periods and triggers per jurisdiction]*** |
| ***[Head of Data Governance / Records Management]*** | ***[Owns the corporate retention schedule as a whole and the non-personal-data rows]*** |
| ***[Processing Owner]*** | ***[Accountable for retention and disposal execution for its processing (Document 5, row S2.2); confirms triggers; decides the cascade for models and synthetic datasets (Section 3.5); takes anonymity conclusions on Legal's assessment (Section 3.1)]*** |
| ***[Data Steward / IT]*** | ***[Executes disposal, restriction and anonymisation technically; receives notice of model decommissioning]*** |
| ***[Legal]*** | ***[Issues, reviews and releases legal holds; assesses identifiability for anonymity conclusions; validates statutory periods]*** |
| ***[DPO]*** | ***[Advises on the matrix, exceptions and anonymity conclusions; monitors compliance; informed of disposal-cycle results. The DPO does not approve periods, exceptions or anonymity conclusions]*** |

## **9. Relationship to Other Framework Documents**

* Builds on the Data Classification Policy (Document 10) and the RoPA (Document 21).
* Executed as supporting process S2 on the Privacy Governance Process Map (Document 24); roles per the RACI Matrix (Document 5, Section 6).
* Informs the privacy notice (Document 1, 01B, Section 11), which mirrors the matrix without duplicating it.
* Interacts with the Data Subject Rights Policy (Document 15) — erasure and restriction on request (Sections 3.5 and 4.1).
* Interacts with the Cross-Border Data Transfer Policy (Document 12) — archives held by a provider in a third country.
* Uses the Privacy Risk Assessment Methodology (Document 18) — PET Assessment Module and anonymity conclusions (Section 3).
* Interfaces with the model-risk / AI governance function (Document 3, Section 3.5) for training datasets.
* Interacts with the Consent Management Policy (Document 13) — consent validity is set there; this document sets how long proof of consent is kept.
* Interacts with the Data Breach Response Policy (Document 14) — archived data may be affected by a breach; every breach is recorded under Art. 33(5).
* Interacts with the Privacy by Design and by Default Policy (Document 16) — default retention for new data categories.
* Evidence-pack integrity — Document 9, Section 4.1.

## **10. Review and Amendment**

This document is reviewed under ***[the Policy Review Cycle, Document 29]*** and upon any change in retention law in a jurisdiction of presence. Changes are adopted by ***[Executive Management]*** on the proposal of ***[the EPPO]***, after consulting ***[the Privacy Risk Committee]*** and the DPO.

## **11. Approval**

This document was adopted by ***[Executive Management]*** on ***[date]***. Document owner: ***[EPPO]***.

# **Part B — Worked Example: PanEuropean Bank AG**

**PanEuropean Bank AG — Data Retention and Disposal Policy**

*Effective date: 20 October 2026  ·  Version: 2.0  ·  Document owner: Chief Privacy Officer (EPPO)  ·  Corporate retention schedule owned by: Chief Data Officer (Data Governance)  ·  Adopted by: Management Board, 20 October 2026*

*Fictional legal entity, provided solely for illustrative purposes.*

***Fictional Document History (illustrative)***

| Version | Date | Changes |
| :---- | :---- | :---- |
| 1.0 | 1 March 2026 | First version. Owners at the time: Data Governance (CDO) and Group DPO |
| 2.0 | 20 October 2026 | Re-baselined to the new role model (Chief Privacy Officer as owner; Group DPO advice only); the blanket customer-data period replaced by record-type rows aligned with the Customer Privacy Notice (Document 1); AML rows split into the current German rule and the scheduled AMLR rule; restricted state, scoped legal hold, erasure cascade and evidence-pack rows added; synthetic data no longer treated as public by default |

## **1. Purpose**

This document establishes retention periods for PanEuropean Bank AG's personal data in its five countries of presence and the procedure for their disposal. It replaced branch-by-branch practices with one matrix aligned with Data Governance.

## **2. Status as a Privacy Overlay on Data Governance**

PanEuropean's corporate retention schedule is owned by Data Governance under the CDO; Data Stewards and IT execute disposal. The Chief Privacy Officer owns the personal-data dimension of the matrix; Processing Owners are accountable for execution in their processing (Document 5, rows S2.1 and S2.2). The Group DPO advises.

## **3. Scope**

All personal data of PanEuropean Bank AG and its branches in Germany, France, Italy, Spain and Poland to which Document 10 has assigned a data class, including data shared with EuroCredit Bureau (an independent controller, which applies its own retention) and data made available to processors in India and the United States (Document 12).

***3.1 Anonymous Information***

The credit-portfolio statistics published on the open-data portal (Document 18, Example 3.1) are outside this document while the conclusion that they are anonymous information stands; the conclusion was recorded by the Processing Owner for the publication on Legal & Compliance's assessment with Group DPO advice and is re-assessed annually and before every further release. No other dataset at PanEuropean is currently treated as anonymous.

***3.2 Synthetic Datasets***

The synthetic calibration dataset for the credit-scoring model (DPIA-CS-TRAIN-01; Document 18, Example 2.1-R) is Restricted / Personal data with the state "synthetic" (Document 10). It is available only to Data Science for calibration and is retained under the matrix row "Synthetic calibration datasets". It is not published and is not reclassified as public.

***3.3 Model Training Datasets***

The source extracts used to train the synthetic-data generator stay inside PEP (Document 9) and are deleted 30 days after the generator run is validated (illustrative internal value); the generator's parameters are deleted when the synthetic dataset is retired. Credit-decision records of the production scoring process (inputs, score, outcome, human review) are kept under their own row. Where the model-risk function requires data histories for validation or back-testing of a model, it records the basis and the period as a separate row, approved through the Chief Privacy Officer; no such row exists at present. The Model Risk and AI Governance function notifies the Data Steward of each model version's decommissioning date (Document 3, Section 3.5).

***3.4 Open Data Publication***

PanEuropean's only open-data initiative is the publication of aggregated credit-portfolio statistics. Each release requires G-L, a PASS of the PET Assessment Module and an anonymity conclusion as described in Part A, Section 3.4. PanEuropean's internal policy (stricter than the legal test) excludes health-related and other special-category attributes from every open release; a release disclosing identifiable special-category data without an Art. 9(2) condition would also fail G-L (Document 18, Example 3.3).

***3.5 Erasure and Withdrawal Cascade to Derived Data***

An erasure on request or at the end of a period is propagated, through PEP's lineage records, to pseudonymised analytics extracts and feature stores, which are cleaned in the next monthly run. For the synthetic calibration dataset and the generator, the Head of Credit Decisions decided (with Group DPO advice) that a customer whose data are erased is excluded from the next generator run and that the dataset is not regenerated earlier unless a re-assessment under Document 18 shows a specific disclosure risk for that customer. Withdrawal of marketing consent removes the customer from marketing-analytics extracts in the next run (Document 13). Automated propagation is planned (Document 9, Section 3.2); until then, the Privacy Operations Lead reconciles it manually.

## **4. Retention Principles**

The principles of Part A apply unchanged. Example of scoped retention: when a current account is closed, only the records that commercial and tax law requires — books, vouchers and business correspondence relevant for accounting — are kept, in the restricted state, for the statutory accounting retention period under applicable commercial and tax law for each record type, counted as that law provides (for German records, the Commercial Code (HGB) and the Fiscal Code (AO); for branch records, the law of the branch country); marketing preferences, app usage data and other account data are deleted. This mirrors the Customer Privacy Notice (Document 1, 01B, Section 11).

***4.1 Restricted Retention State***

Records in the restricted state are flagged in the source system, moved to an archive with access limited to Finance, Tax, Compliance or Legal as the purpose requires, and excluded from analytics, marketing and model training. Art. 18 restrictions on request are applied by the Privacy Operations Lead in the systems concerned (Document 15).

## **5. Retention Period Matrix**

| Data Category / Record Type | Data Class | Purpose and Basis | Trigger | Jurisdiction | Retention Period | Exceptions / Restricted State | Disposal Method |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Account and contract data (current accounts, loans, cards) | Confidential / Personal data | Performance of the contract (Art. 6(1)(b)) | End of the banking relationship | All | Duration of the relationship; then deleted, except the records in the next row | Legal hold; Art. 18 | Deletion in core banking and CRM |
| Accounting-relevant records (books, vouchers, business correspondence relevant for accounting) | Confidential / Personal data | Statutory record-keeping (Art. 6(1)(c)) | As the applicable law provides (for German records, the end of the calendar year in which the record was created or received) | DE: HGB, AO; FR, IT, ES, PL: national commercial and tax law | Statutory accounting retention period under applicable commercial and tax law, per record type | Restricted state for the whole period; legal hold | Deletion in the archive |
| AML/KYC records (identification data, due-diligence records, transaction records) — current rule | Restricted / Personal data; Art. 10 content where present (Document 10) | Anti-money-laundering record-keeping (Art. 6(1)(c); Art. 10 authorisation by AML law) | Germany: end of the calendar year in which the business relationship ended (GwG §8(4) with §10(3) sentence 1 no. 1); other cases (for example occasional transactions) have their own starting point under the Act | DE: GwG; FR, IT, ES, PL: national AML law, which may set a different period or starting point (recorded per branch in the corporate schedule) | Germany: 5 years from the trigger; branch countries: as national AML law provides. A longer period only where the law requires or permits it in a specific case | Restricted state (access: Compliance); legal hold | Deletion in the AML system and archive |
| AML/KYC records — scheduled rule from 10 July 2027 | Restricted / Personal data; Art. 10 content where present | Regulation (EU) 2024/1624 (AMLR), Art. 77 | As set by AMLR Art. 77 (after the end of the business relationship or the date of an occasional transaction) | All five countries (directly applicable) | 5 years, counted as Art. 77 provides, with the limited extensions that Article allows. **Not applied before 10 July 2027** | As above | As above |
| Credit applications that did not lead to a contract | Restricted / Personal data | Pre-contractual steps (Art. 6(1)(b)); defence against claims | Date of the decision | All | 6 months, unless the applicant contests the decision (illustrative internal value, as in Document 1) | Legal hold if contested | Deletion |
| Credit-decision records (inputs, score, outcome, human review) | Restricted / Personal data | Creditworthiness assessment; Art. 22(3) safeguards; defence against claims | End of the credit agreement | All | For the life of the credit agreement and afterwards as long as claims relating to it can be raised (limitation period under applicable civil law) | Legal hold; restricted state after the end of the agreement | Deletion |
| PPI health data | Restricted / Special category | Arranging the insurance or forwarding the claim (Art. 9(2)(a)); legal claims about the bank's role as distributor (Art. 9(2)(f)) | Completion of the application or the claim | All | Only as long as needed to arrange the insurance or forward the claim; then for the limitation period for claims about the bank's role; never retained for credit purposes (as in Document 1) | Restricted state after completion (access: Insurance Distribution, Legal) | Deletion; pseudonymised copies on PEP deleted with the source |
| Biometric template of the app's biometric module | Restricted / Special category | Authentication on explicit consent (Art. 9(2)(a)) | Customer disables biometric log-in, uninstalls the app or resets the device | All | Stored only on the customer's device; deleted on the trigger by the app. PanEuropean holds no server-side template. Log-in through the device operating system's own biometric function involves no biometric data at PanEuropean and is not a row of this matrix | — | Deletion on the device by the app |
| Branch video recordings | Internal / Personal data | Security of premises and staff (Art. 6(1)(f)) | Date of recording | DE: short period in line with the guidance of the German supervisory authorities (DSK orientation guidance on video surveillance by non-public bodies); FR, IT, ES, PL: national law and supervisory-authority guidance | 72 hours (illustrative internal value), or the period stated in the branch notice where national rules require a different one | Legal hold for an incident under investigation (extract only) | Automatic overwrite |
| Customer-service chat records | Confidential / Personal data | Handling of the enquiry; quality assurance | Date of the conversation | All | 12 months (illustrative internal value, as in Document 1); prompts and outputs at Example AI Provider Inc. (fictional processor) deleted within 30 days under the contract (illustrative assumption) | Legal hold; Art. 18 | Deletion; processor deletion confirmation |
| Marketing consent records (proof of consent) | Internal / Personal data | Demonstrating consent (Art. 7(1)) | Withdrawal or expiry of consent | All | For the duration of consent and afterwards as long as needed to demonstrate it, at most 3 years (as in Document 1). Validity of consent itself is set by Document 13 | — | Deletion in the consent management system |
| Data subject request records | Internal / Personal data | Demonstrating compliance with Arts. 12–22 (Art. 5(2)) | Closure of the request | All | 3 years (illustrative internal value) | Legal hold if a complaint or proceedings are pending | Deletion |
| Evidence packs and decision records (DPIA, TIA, risk acceptance, anonymity conclusions) | Restricted / Personal data (deciders' names; samples where unavoidable) | Accountability (Art. 5(2)); supervisory review | End of the processing, or withdrawal of the released artefact or of the conclusion | All | For the life of the processing or release and afterwards 3 years (illustrative internal value); personal-data components minimised and deleted at the end of the period; longer only where a specific rule requires it (Section 6.1) or under a legal hold | Superseded, not edited; minimal record after purge only where lawful and necessary | Deletion or crypto-shredding of the separately sealed component (Document 9, Section 4.1) |
| Remote-support access logs (Example Cloud Services Pvt Ltd, fictional, India — tokenised logs) | Internal / Personal data (pseudonymised) | Security monitoring (Art. 32); DORA ICT logging | Date of the event | Bank-side: all; provider-side: as assessed in TIA-CLOUD-01 (Document 20), including destination-country log-retention rules | Bank-side: 1 year (illustrative internal value); provider-side copies deleted under the processing agreement | Legal hold | Deletion; provider deletion confirmation |
| Employee records | Restricted / Personal data (special-category content where present) | Employment contract; employment, tax and social-security law | End of employment, or the trigger set by the specific law | Per country | Per record type under national employment, tax and social-security law; no single blanket period | Restricted state for statutory records; legal hold | Deletion in the HR system |
| Records of unsuccessful job candidates | Confidential / Personal data | Recruitment; defence against claims | Rejection | Per country | About 6 months after rejection — for example to cover the limitation period for discrimination claims under national law (illustrative internal value); longer only with the candidate's consent to a talent pool | Legal hold if a claim is raised | Deletion |
| Pseudonymised analytics extracts | Restricted / Personal data (pseudonymised) | Analytics on a compatible purpose (Art. 6(4)) | End of the analytics project | All | Duration of the project + 3 months (illustrative internal value); erasure cascade applies (Section 3.5) | — | Deletion on PEP and in the data warehouse |
| Synthetic calibration datasets (no anonymity conclusion) | Restricted / Personal data (synthetic) | Calibration and validation of the credit-scoring model version (DPIA-CS-TRAIN-01) | Decommissioning of the model version | All | Operational life of the model version + 2 years for model-validation evidence (illustrative internal value) | Exclusion of erased customers from the next run (Section 3.5) | Deletion on PEP |
| Generator source extracts and parameters | Restricted / Personal data | Generation of synthetic calibration data | Validation of the generator run / retirement of the synthetic dataset | All | Extracts: 30 days after validation; parameters: until the synthetic dataset is retired (illustrative internal values) | — | Deletion on PEP |
| Published credit-portfolio statistics | Public / Non-personal (anonymous information) | Publication | — | — | Outside this document while the anonymity conclusion stands; the release record is kept under the evidence-pack row | If the conclusion is not confirmed, further releases stop and the source rows apply | — |

## **6. Disposal Procedure**

Disposal runs monthly. For structured customer, credit and analytics data, an automated run on PEP and in the source systems identifies records that have reached the end of their period, checks them against the register of legal holds, Art. 18 restrictions and open requests, and then deletes them, moves them to the restricted state or excludes them from derived datasets (Section 3.5). Categories served by separate systems — branch video (video-surveillance system), HR (HR system) — are disposed of with those systems' own means on the same schedule and with the same logging. Processors (Example Cloud Services Pvt Ltd, Example AI Provider Inc., both fictional) dispose of data under their processing agreements and confirm deletion. Media are sanitised under the standards approved by IT Security (NIST SP 800-88; ISO/IEC 27040). The Data Steward coordinates across categories.

Backups: deleted records are put beyond use; backup copies are overwritten within the rotation cycle of at most 90 days; if a backup is restored, deletions are re-applied before the system returns to service.

The disposal log (date, category, volume, method, system, responsible role; no record content) is available to the Chief Privacy Officer, the Group DPO and, on request, the HBDI and Group Internal Audit; it is retained for 5 years (illustrative internal value).

***6.1 Evidence Packs and Decision Records***

Evidence packs are sealed and superseded, not edited (Document 9, Section 4.1). Personal data in them (deciders' names, any sample records) are held in a separately sealed component that is deleted or crypto-shredded at the end of the evidence-pack period; after a purge, PEP keeps a minimal record (identifier, dates, hash, reason) for 3 years to demonstrate the disposal (illustrative internal value). For the credit-scoring model, PanEuropean as provider of a high-risk AI system keeps the technical documentation for the period set by AI Act Art. 18 once the high-risk obligations apply (from 2 December 2027); this concerns the documentation, not raw training data.

## **7. Exceptions**

As of the effective date, no legal hold is in effect. General Counsel issues a hold for any matter that becomes the subject of litigation, a supervisory investigation (HBDI or another data protection authority) or a financial-supervisory examination (ECB/BaFin) and that requires preservation. Each hold names the matter, record categories, systems, custodians and period; Legal & Compliance reviews every active hold at least every three months and narrows or releases it. On release, records whose ordinary period has expired are disposed of within 30 days; a separate run is not required only if the next monthly run falls within those 30 days. The Chief Privacy Officer receives a quarterly list of active holds and releases; the Group DPO is informed.

Upon a sale or transfer of a credit portfolio, the acquirer becomes a controller in its own right; the transfer agreement contains contractual commitments on retention and deletion, and PanEuropean deletes or restricts its own copies under this matrix. No such transaction is planned.

## **8. Roles and Responsibilities**

| Role | Responsibility |
| :---- | :---- |
| Chief Privacy Officer (EPPO) | Accountable for the personal-data dimension of the schedule (Document 5, row S2.1); proposes this document to the Management Board |
| Privacy Operations Lead; General Counsel (Legal & Compliance) | Prepare matrix rows; Legal & Compliance validates statutory periods and triggers for each country |
| Chief Data Officer (Data Governance) | Owns the corporate retention schedule and the non-personal-data rows |
| Processing Owners (for example Head of Credit Decisions, Head of Customer Service, Head of Digital Banking, Head of Marketing) | Accountable for disposal execution in their processing (Document 5, row S2.2); confirm triggers; decide the cascade for models and synthetic datasets; take anonymity conclusions on Legal & Compliance's assessment |
| Data Steward; IT Management | Execute disposal, restriction and anonymisation; receive notice of model decommissioning |
| General Counsel (Legal & Compliance) | Issues, reviews and releases legal holds; assesses identifiability for anonymity conclusions |
| Group DPO | Advises on the matrix, holds and anonymity conclusions; monitors compliance; informed of disposal results |

## **9. Relationship to Other Framework Documents**

* Builds on Document 10 (data class and state) and Document 21 (RoPA).
* Executed as supporting process S2 (Document 24); roles per Document 5, Section 6.
* Mirrored in the Customer Privacy Notice (Document 1, 01B, Section 11): account and contract data, AML/KYC (current and scheduled rules), declined credit applications, credit-decision records, PPI health data, chat records, marketing consent records and branch video are stated there in the same terms.
* Interacts with Document 15 (erasure, restriction), Document 12 (provider logs in India), Document 18 (anonymity conclusions, PET module), Document 3, Section 3.5 (model decommissioning), Document 13 (consent validity versus proof of consent), Document 14 (breaches affecting archived data), Document 16 (default retention for new data categories) and Document 9 (evidence-pack integrity, lineage tooling).

## **10. Review and Amendment**

This document is reviewed under PanEuropean's Policy Review Cycle (Document 29) and upon any change in retention law in the five countries — including the application of AMLR Art. 77 from 10 July 2027, which requires the AML rows to be re-validated before that date (planned for the review in the second quarter of 2027). Changes are adopted by the Management Board on the Chief Privacy Officer's proposal, after consulting the Privacy Risk Committee and the Group DPO.

## **11. Approval**

Version 1.0 (1 March 2026) was adopted by the Management Board; Data Governance (CDO) and the Group DPO were owners at that time. Version 2.0 was adopted by the Management Board on 20 October 2026 on the Chief Privacy Officer's proposal, after consulting the CDO, the Privacy Risk Committee and the Group DPO. Document owner: Chief Privacy Officer. Group DPO advice is on file.

# **Normative Basis and References**

* Regulation (EU) 2016/679 (GDPR): Arts. 5(1)(c), 5(1)(e), 5(2), 6, 7(1), 9(2)(a), 9(2)(f), 10, 17 (incl. 17(3)), 18, 22(3), 28(3)(g), 30, 32, 33(5); Recital 26.
* Regulation (EU) 2024/1624 (AMLR), Art. 77 — applies from 10 July 2027.
* German Money Laundering Act (GwG), §8(4) with §10(3) sentence 1 no. 1 — current German AML record retention and its starting point.
* German Commercial Code (HGB) and Fiscal Code (AO) — statutory accounting retention for accounting-relevant records; periods per the current consolidated text.
* Regulation (EU) 2024/1689 (AI Act), as amended by the AI Omnibus: Arts. 18 (documentation keeping) and 19 (automatically generated logs); high-risk obligations for Annex III systems apply from 2 December 2027.
* Regulation (EU) 2022/2554 (DORA) — ICT logging and record-keeping, as an adjacent regime.
* Datenschutzkonferenz (DSK), orientation guidance on video surveillance by non-public bodies.
* Article 29 Working Party, Opinion 05/2014 on Anonymisation Techniques (WP216); EDPB Guidelines 02/2026 on anonymisation — public-consultation draft (8 July 2026), not final.
* NIST SP 800-88, *Guidelines for Media Sanitization*; ISO/IEC 27040 (storage security) — bibliographic pointers.
* ISO 15489-1 (records management) — bibliographic pointer.

# **International Adaptation**

> **Guidance.** The GDPR is the baseline. The applicability map for Canada is in Document 7, Section 3.1. This document does not claim compliance with any jurisdiction's law.

* **United Kingdom (headline).** UK GDPR storage limitation and the rights to erasure and restriction mirror the EU text; statutory record-keeping periods follow UK company, tax and anti-money-laundering law; the Data (Use and Access) Act 2025 amendments commence in phases.
* **Switzerland (headline).** Under the revFADP, personal data are destroyed or anonymised as soon as they are no longer needed for the purpose; statutory retention duties under Swiss law (for example accounting) apply per record type.
* **Canada — PIPEDA.** Personal information is retained only as long as necessary for the identified purposes (Schedule 1, Principle 4.5), with minimum and maximum periods set by guidelines; information used to make a decision about an individual is retained long enough to allow access (Principle 4.5.2); information no longer required is destroyed, erased or made anonymous (Principle 4.5.3).
* **Canada — Québec (P-39.1).** When the purpose has been achieved, personal information is destroyed or anonymised to be used for serious and legitimate purposes, subject to retention periods set by law; anonymisation must follow generally accepted best practices and the criteria and terms of the Québec regulation on the anonymisation of personal information.

# **Document History (PGF)**

| Release | Date | Changes |
| :---- | :---- | :---- |
| 1.0.0-rc.1 | 2026-10-26 | Canonical English Markdown; changes from internal ver.2: matrix restructured as category + purpose/basis + trigger + jurisdiction + duration + exceptions + disposal method; blanket "all customer data 10 years" replaced by scoped rows — contract data for the relationship, then only accounting-relevant records for the statutory accounting retention period under applicable commercial and tax law (HGB/AO limited to accounting records; no unverified period asserted); AML split into the current German rule (GwG §8(4): 5 years from the end of the calendar year in which the relationship ended; branch-country law may differ) and a separate scheduled row for AMLR Art. 77 from 10 July 2027; "longest competing basis" rule replaced by scoped retention with a restricted (blocked) state covering statutory retention, Art. 18 restriction and legal hold; legal hold made scoped, periodically reviewed and released with a defined disposal deadline (the inverted off-cycle rule corrected); portfolio transfer reworded (acquirer as independent controller; contractual commitments); HR split into employees (per record type and country) and candidates (about 6 months, e.g. limitation period for discrimination claims); branch video shortened in line with national supervisory guidance (DSK, generic); PPI health data limited to arranging the insurance and claim limitation, never for credit; biometric row limited to processing the organisation controls; evidence packs and decision records given their own row (retention by the applicable rule, superseding not editing, deletion of personal-data components, minimal record after purge only where lawful); erasure and withdrawal cascade to derived personal data not concluded anonymous; anonymity conclusions taken by the Processing Owner on Legal's assessment with DPO advice (no DPO determination), supported by the Document 18 PET module and re-assessed periodically; synthetic data no longer "public/open" by default; open releases conditioned on G-L, the PET module and an anonymity conclusion (special-category exclusion labelled internal policy); AI Act Arts. 18/19 cited precisely (documentation and logs, not raw training data); prudential data-history needs recorded as separate rows; disposal standards and processor deletion confirmations added; ownership moved to the EPPO with adoption by Executive Management; Part B aligned with the Customer Privacy Notice (Document 1) and re-baselined as version 2.0 (20 October 2026); example dates shifted by −12 months; calqued "perimeter" removed; references and international adaptation added |
