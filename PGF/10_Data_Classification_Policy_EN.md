---
title: "Data Classification Policy"
document_id: PGF-10
level: 2
release_version: 1.0.0-rc.1
status: release-candidate
authors: ["Alexey Neyman", "Val Khvatov"]
regulatory_reference_date: 2026-10-26
licence_proposed: "CC BY 4.0 (proposed; subject to rights-holder confirmation)"
source_provenance: "Derived from internal source set ver.2: Level2/10. Data-Classification-Policy_ENG.docx.md; sha256 d470be3aee8ef20c190bce397b2f16d3d129faa3140cbc5c40bbb8fbf7e1d207"
---

# PGF-10 — Data Classification Policy

*Privacy Governance Framework (PGF) · Level 2 — Policies and Standards · Release 1.0.0-rc.1 · Regulatory reference date: 26 October 2026*

> **Status and use.** Part A is a reusable template. Part B is a worked example for a fictional organisation (PanEuropean Bank AG); all names, figures, dates and records in Part B are illustrative. Nothing in this document is legal advice or a statement about any real organisation, product or provider.

# **About This Document**

**Purpose.** Document 10 adds a privacy dimension to the organisation's corporate data classification standard: personal-data categories (including special categories under GDPR Art. 9 and criminal-offence data under Art. 10 as separate categories), the legal data state (personal, pseudonymised, anonymous information, synthetic, encrypted), an enhanced regime for the most sensitive categories, and labelling rules that carry the class with the data.

**Scope.** All data of the organisation, at the level of fields, documents, datasets and systems. The document is tagged [DG]: classification is a Data Governance function; this document is a privacy overlay on the corporate standard and does not create a parallel scheme.

**Relationships.** The data class is an input to Document 18 (severity factor "Data Class" and "Special Categories of Data"), Document 11 (retention matrix), Document 12 (transfers), Document 14 (breach severity), Documents 21 and 23 (RoPA, inventory); the boundary with Data Governance is set in Document 3, Section 3.3; tooling is connected through Document 9.

# **How to Use This Document**

Part A is a template. Text in ***[square brackets, bold italic]*** is a fill-in or illustrative placeholder. Blocks marked **Guidance** are removed from the adopted version. Text without brackets is either the PGF's recommended fixed policy (Sections 4.3–4.5, 5 and 6.2) or a statement about how the PGF documents fit together.

> **Guidance.** Do not change the category names of Section 4.2 after adoption: Documents 11, 12, 14, 18, 21 and 23 refer to them by name. Do not merge data states (Section 4.3) into categories: a pseudonymised or synthetic dataset keeps the category of the information it carries about people until the controller concludes that it is anonymous information.

# **Table of Contents**

**About This Document**
**How to Use This Document**
**Part A — Template**
Glossary of Terms
1. Purpose
2. Status as a Privacy Overlay on Data Governance
3. Scope
4. Classification Scheme (4.1 Baseline Sensitivity Levels; 4.2 Personal Data Dimension; 4.3 Data State; 4.4 Inferred and Derived Sensitive Data; 4.5 Biometric Authentication)
5. Special-Category and Criminal-Offence Data — Enhanced Regime (5.1–5.4)
6. Labelling and Label Distribution Rules (6.1–6.5)
7. Roles and Responsibilities
8. Links to Other Framework Documents
9. Review Cycle
10. Approval
**Part B — Worked Example: PanEuropean Bank AG** (same structure)
**Normative Basis and References**
**International Adaptation**
**Document History (PGF)**

# **Part A — Template**

**Data Classification Policy of *[Legal name of the organisation]***

Effective date: ***[DD Month YYYY]*** · Version: ***[x.x]*** · Document owner: ***[Head of Data Governance (CDO)]*** · Privacy dimension (Sections 4.2–5) maintained by: ***[Executive Privacy Programme Owner (EPPO)]*** · Adopted by: ***[Executive Management]***

***Version History***

| Version | Date | Changes |
| :---- | :---- | :---- |
| ***[1.0]*** | ***[DD Month YYYY]*** | ***[First version of the document]*** |
| ***[x.x]*** | ***[DD Month YYYY]*** | ***[Brief description of material changes]*** |

> **Guidance.** The template version and any adopted version are independent of the PGF release number. Record only material changes, for example a new category, a change to the enhanced regime or to the declassification procedure.

## **Glossary of Terms**

*This table lists only the terms defined by this document itself; terms defined in another PGF document are not repeated here.*

| Term | Definition / Reference |
| :---- | :---- |
| DG (Data Governance) | The organisation's corporate function that sets the single data classification standard (Section 4.1). The [DG] tag means that Data Governance is consulted when this document is drafted and reviewed (Document 29); it does not imply that Data Governance alone owns the privacy dimension. |
| Data class | The combination of the baseline sensitivity level (Section 4.1) and the personal-data category (Section 4.2), recorded together with the data state (Section 4.3). Other PGF documents refer to the data class by name and do not redefine it. |
| Data state | The legal status qualifier of a unit of data: personal data, pseudonymised data, anonymous information, synthetic data, or encrypted data (Section 4.3). |
| Inferred sensitive data | Data that reveal special-category or criminal-offence information indirectly, through deduction or combination, including derived features and model outputs (Section 4.4). |
| Declassification | Moving a unit of data to a lower category or to the "Non-personal" category. Permitted only under Section 6.2. |
| Data Steward | A Data Governance role, not defined by this document; maintains classification and labels for systems and datasets (Section 7). Its qualification is set by Data Governance standards, not by Document 6. |

## **1. Purpose**

This document establishes a data classification scheme covering personal data, special categories of personal data and criminal-offence data, the legal data state, and the rules for handling data in each class.

The document is tagged [DG]: classification is by nature a Data Governance function, not a privacy-exclusive one. It is built as a privacy overlay on the existing corporate classification standard of ***[organisation name]***, not as a stand-alone standard.

## **2. Status as a Privacy Overlay on Data Governance**

***[Before developing this document, confirm that the organisation has a corporate Data Classification Standard in force, typically supported by a corporate data catalogue owned by Data Governance (Chief Data Officer or equivalent). Demarcation rule: Data Governance owns the classification scheme and its execution; the privacy function does not create a parallel scheme but adds the personal-data dimension, the data state and the enhanced regime to the existing sensitivity levels.]***

> **Guidance.** The demarcation rule is set in the Interface and Integration Model (Document 3, Section 3.3, "Data Classification" sub-domain) and is applied here. If Document 3 has not been adopted, start there.

## **3. Scope**

* All data processed by ***[organisation name]***, whatever the format (structured or unstructured) or location (own infrastructure, cloud, processors).
* Classification applies to a unit of data (field, document, dataset, system); the granularity is set in the labelling standard (Section 6).

This document does not govern:

* risk assessment — the data class is an input to the Privacy Risk Assessment Methodology (Document 18), not a result of it;
* retention periods and disposal — the Data Retention and Disposal Policy (Document 11), by reference to the data class;
* technical information-security measures — the boundary with the CISO is set in Document 3, Section 3.2;
* lawful bases and conditions for processing — checked in the legal compliance gate (G-L); consent standards are in the Consent Management Policy (Document 13) and jurisdiction particulars in the Regulatory Applicability Matrix (Document 7).

## **4. Classification Scheme**

The scheme has two orthogonal axes — (a) baseline sensitivity levels inherited from the corporate DG standard and (b) personal-data categories added by this document — plus the data state (Section 4.3), which qualifies the legal status of the unit of data.

***4.1 Baseline Sensitivity Levels (Inherited from the DG Standard)***

The table illustrates a typical four-level corporate standard. Replace it with the levels in force at ***[organisation name]***, or confirm that they match.

| Level | Description |
| :---- | :---- |
| ***[Level 1, e.g., Public]*** | Data intended for unrestricted distribution. |
| ***[Level 2, e.g., Internal]*** | Data for internal use; disclosure does not create material harm. |
| ***[Level 3, e.g., Confidential]*** | Data whose disclosure creates harm to individuals or to the organisation. |
| ***[Level 4, e.g., Restricted]*** | Data with the highest sensitivity and the strictest access controls. |

***4.2 Personal Data Dimension (Added by This Document)***

The categories below are the PGF's recommended default. Wording that depends on a jurisdiction is shown as an example.

| Category | Definition |
| :---- | :---- |
| ***[Category 1 — Non-personal data]*** | ***[Information that does not relate to an identified or identifiable natural person. Includes information that the controller has concluded is anonymous information under Section 6.2 — a contextual conclusion under Recital 26 based on means reasonably likely to be used, not a statement that re-identification is impossible.]*** |
| ***[Category 2 — Personal data]*** | ***[Any information relating to an identified or identifiable natural person (Art. 4(1); for other jurisdictions see Document 7). Includes pseudonymised data (Section 4.3).]*** |
| ***[Category 3 — Special category (Art. 9)]*** | ***[The categories of Art. 9(1): data revealing racial or ethnic origin, political opinions, religious or philosophical beliefs or trade-union membership; genetic data; biometric data processed for the purpose of uniquely identifying a natural person; data concerning health; data concerning a natural person's sex life or sexual orientation. The list in Art. 9(1) is exhaustive. Includes inferred special-category data (Section 4.4). Biometric data are tracked as a separately monitored subcategory, because national rules diverge widely (Document 7).]*** |
| ***[Category 4 — Criminal-offence data (Art. 10)]*** | ***[Personal data relating to criminal convictions and offences or related security measures, including allegations and suspicions of offences where they relate to an identifiable person. This is **not** a special category: processing requires official authority or authorisation by Union or Member State law providing appropriate safeguards (Art. 10), not an Art. 9(2) condition. The controls of Section 5 apply to it in full.]*** |
| ***[Category 5 — Vulnerable data subject (marker)]*** | ***[A marker applied in addition to category 2, 3 or 4 for data of minors and other vulnerable data subjects. Consent rules for information-society services offered to children (Art. 8 and national ages, Document 7) are distinct from contractual capacity under national civil law; the Consent Management Policy (Document 13) sets the consent regime.]*** |

> **Guidance.** Do not introduce weights for "level × category" combinations here: Document 18 calibrates how the data class affects severity. Fix the category names verbatim after adoption.

***4.3 Data State (Legal Status Qualifier)***

Every unit of personal data, and every unit derived from personal data, carries one of the following states. The states are distinct and are never merged.

| Data state | Meaning | Effect on the category |
| :---- | :---- | :---- |
| Personal data | Identified or identifiable | Category 2, 3 or 4 as applicable |
| Pseudonymised data | Processed so that the data can no longer be attributed to a specific person without additional information kept separately and protected (Art. 4(5)) | Remains personal data — same category as the source — for anyone who can attribute it with means reasonably likely to be used (EDPB Guidelines 01/2025). Pseudonymisation is a security and minimisation measure, not anonymisation. A recipient's realistic means are part of the contextual analysis of a disclosure (CJEU C-413/23 P *EDPS v SRB*), but the judgment does not establish that pseudonymised data cease to be personal data, or that Chapter V stops applying, whenever a recipient lacks the additional information; the controller's perspective, a processor's role and the full flow are assessed separately, and while the conclusion is unclear the data are treated as personal (Document 12). The category in the controller's own catalogue does not change |
| Anonymous information | A contextual legal conclusion under Recital 26, made by the controller on documented evidence and re-assessed periodically (Section 6.2) | Category 1 while the conclusion stands |
| Synthetic data | A generation method, not a legal status | Keeps the category of the source until an anonymity conclusion is made; synthetic records can disclose information about people in the source data |
| Encrypted data | A security measure | Remains personal data in the category of the plaintext |

Federated learning and secure computation are processing architectures; they do not change the state of the data or of the artefacts exchanged (Document 18, Section 3.3.3).

***4.4 Inferred and Derived Sensitive Data***

* Data that reveal special-category information **indirectly**, by deduction or by combining or comparing data, are special-category data (CJEU C-184/20 *OT*, 1 August 2022; CJEU C-252/21 *Meta Platforms v Bundeskartellamt*, 4 July 2023). The test is whether the data are capable of revealing such information, not whether the controller intends to use them for that purpose.
* ***[Example: payment-transaction data. Payments to a trade union, a political party, a religious community, a clinic, a pharmacy or an addiction-support service can reveal Art. 9 information. Raw transaction data are classified as personal data with a "may reveal special categories" flag; any derived feature, label, segment or model output that categorises transactions or customers by such a characteristic is classified as category 3.]***
* Derived features, models and model outputs built to infer a category 3 or category 4 characteristic are classified in that category. Features that act as proxies for protected characteristics are flagged for the bias testing required by the DPIA (Document 19).
* Where an AI system needs special-category data for bias detection and correction, the conditions of AI Act Art. 10(5) apply in addition to G-L; the dataset is category 3.
* A derived dataset inherits the maximum level and the maximum category of its sources (Section 6.2), unless the derivation demonstrably removes the sensitive content and the removal is recorded.

***4.5 Biometric Authentication***

* ***[Authentication through the operating system's own biometric function on the customer's device, where the organisation receives only a pass/fail assertion and never receives or controls a template: the organisation does not process biometric data for that step. The authentication event is classified as category 2.]***
* ***[Biometric processing performed by the organisation's own software — for example a biometric module embedded in the organisation's app, or remote identity verification comparing a selfie with an identity document — is processing of biometric data for unique identification by the organisation as controller, even where the template is stored only on the customer's device: category 3, with an Art. 9(2) condition (typically explicit consent with a non-biometric alternative) and the controls of Section 5.]***
* ***[The register of Section 5 and the retention matrix of Document 11 include only biometric processing that the organisation performs or controls.]***

## **5. Special-Category and Criminal-Offence Data — Enhanced Regime**

The enhanced regime applies to category 3 (special category) and category 4 (criminal-offence data) alike. The legal conditions differ (an Art. 9(2) condition versus Art. 10 authorisation) and are checked in G-L; the controls are the same. None of the elements below may be set aside by a Data Owner or Data Steward. Category 5 (vulnerable data subject) has a narrower regime set by the Consent Management Policy (Document 13) and Document 18's vulnerability factor.

***5.1 Mandatory DPIA Regardless of Triage Outcome***

For any processing operation involving category 3 or 4 data, a DPIA (Document 19) is carried out; the triage questionnaire is used only to set the scope of the assessment. This is **internal policy**, stricter than Art. 35(3)(b), which requires a DPIA for processing of such data on a large scale.

***5.2 Stricter Escalation Threshold***

This document does not set escalation thresholds. The presence of category 3 or 4 data raises severity through the "Special Categories of Data" component of Factor B in the Privacy Risk Assessment Methodology (Document 18, Section 3.4), so that the same scenario reaches a higher residual tier sooner. In addition, DPO advice is required for every decision on such processing, whatever the tier (Document 8, Section 5). Acceptance authority follows Document 8, Section 5 unchanged:

| Residual tier (after G-L passed) | Who may accept | Additional mandatory step |
| :---- | :---- | :---- |
| Low | ***[Processing Owner]*** | Record; DPO advice (required for category 3/4 data) |
| Medium | ***[Processing Owner, with EPPO concurrence]*** | DPO advice recorded; conditional acceptance carries an expiry date |
| High | ***[One named member of Executive Management]*** | G-36 evaluated and recorded; prior consultation of the competent supervisory authority whenever the Art. 36 test is met; DPO advice recorded; Governing Body committee informed |
| Critical | Not acceptable | Stop or redesign |

***5.3 Access Restriction***

Access to category 3 and 4 data is granted on a need-to-know basis with role-based access control and logging of every access.

***5.4 Mandatory Protective Measures — No Exceptions at the Data Owner or Data Steward Level***

At least one protective measure from the PET Standard (Technology Implementation Package, Document 9, Section 6) — for example pseudonymisation, de-identification, synthesis with tested disclosure controls, or an architectural measure such as device-bound storage — is applied to category 3 and 4 data wherever the purpose allows. Where the purpose makes a measure impossible (for example, production screening that must match names against official lists), an exception may be granted only by ***[the Processing Owner with EPPO concurrence]***, with DPO advice recorded, compensating controls specified and an expiry date set. A Data Owner or Data Steward may not grant or claim an exception.

> **Guidance.** Do not name specific tooling here; tooling is connected through Document 9. Architectural measures (for example storing a template only on the user's device) are recorded as such and not described as a privacy-enhancing technique.

## **6. Labelling and Label Distribution Rules**

***6.1 Metadata Standard***

***[Each unit of data carries at least the following five metadata attributes. The label format and its machine-readable representation are set in a technical specification outside the governance core (Document 9, Technology Implementation Package).]***

| Attribute | Who Populates It, and When | Rule on Copy/Export |
| :---- | :---- | :---- |
| (i) ***[Data class (level / category) and data state (Sections 4.1–4.3)]*** | ***[Data Steward with a Privacy Officer — at initial classification and at each review (Section 6.4)]*** | ***[Maximum on each axis separately; data state carried unchanged unless Section 6.2 applies]*** |
| (ii) ***[Residual risk tier]*** | ***[From the Document 18 calculation or the DPIA (Document 19) — not set by this document]*** | ***[Inherited unchanged unless a new assessment is made]*** |
| (iii) ***[Date of last DPIA]*** | ***[From the DPIA (Document 19), where applicable]*** | ***[Inherited unchanged]*** |
| (iv) ***[Transformation provenance]*** | ***[Where the unit results from a PET transformation: the technique (or a reference to the PET Standard, Document 9) and the class of the source]*** | ***[Inherited when copying an already transformed dataset; empty for untransformed data]*** |
| (v) ***[Reference to evidence pack]*** | ***[For any formal decision on the unit — residual-risk acceptance, anonymity conclusion, exception (Section 5.4), class correction (Section 6.5)]*** | ***[Inherited unchanged; mandatory for category 3 and 4 data and for any declassification (Section 6.2)]*** |

***[Attributes (iv) and (v) are descriptive fields, not a further classification axis. (iv) states what was done; (v) gives a verifiable reference to the evidence and the decision. One without the other is insufficient.]***

> **Guidance.** These fields are the minimum privacy metadata for enriching the corporate data catalogue without a parallel catalogue (Document 3, Section 3.3, "Metadata Management").

***6.2 Label Distribution Across Systems and Declassification***

* The label follows the data through copying, derived computation and export. A derived dataset inherits, separately on each axis, the highest sensitivity level and the highest category among its sources, and the data state that reflects how it was produced (for example "pseudonymised" or "synthetic").
* **Declassification to category 1 (non-personal)** is permitted only on the basis of the controller's documented conclusion that the unit is anonymous information under Recital 26: the conclusion is taken by ***[the Processing Owner]*** on ***[Legal]***'s assessment, with DPO advice, supported by the PET Assessment Module of Document 18 (Section 3.3) and its evidence pack, and states the recipients considered (for an open publication, anyone). It is re-assessed at least ***[annually]*** and whenever new auxiliary data, a new published attack, a further release from the same source population or a change of recipient becomes known (Document 18, Section 3.3.0). If the re-assessment does not confirm the conclusion, the unit returns to its earlier category.
* Aggregation, masking, pseudonymisation, encryption or synthesis do **not** by themselves declassify data. Synthetic datasets in particular stay in the category of their source until a conclusion under the previous paragraph is made.
* A lower **sensitivity level** for personal data (for example from Restricted to Confidential after removing special-category fields) is permitted when the removal is verified and recorded in attribute (v).
* The result of any transformation is registered in the corporate data catalogue as a new tracked object.
* Systems that cannot store or transmit the label are entered in an exceptions register with a remediation plan.

***6.3 Automated and Manual Labelling***

Automated labelling has priority. Manual labelling is a fallback for unstructured data that cannot be recognised automatically and is spot-checked. Automated classifiers for inferred sensitive data (Section 4.4) are validated before reliance (Document 9, Section 8).

***6.4 Label Review Frequency***

Labels are reviewed: (a) when the purpose of processing changes; (b) upon a non-conformity found in an audit (Document 27); (c) at least as often as this document is reviewed (Section 9) under the Policy Review Cycle (Document 29) — as applied to the labels, not to the text of the document.

***6.5 Ad Hoc Correction of Misclassification***

A class or attribute found to have been assigned in error outside the review cycle, and not covered by a declassification under Section 6.2, is corrected through a streamlined procedure: the Data Steward records the proposed correction and its rationale; a Privacy Officer confirms the new class; the correction is applied and logged with a reference in attribute (v). Corrections to or from category 3 or 4 are reported to the DPO. Disagreements are resolved under Section 7.

## **7. Roles and Responsibilities**

| Role | Responsibility |
| :---- | :---- |
| ***[Head of Data Governance (CDO)]*** | ***[Accountable for the classification process (Document 5, row S1): owns the baseline sensitivity levels (Section 4.1), the corporate data catalogue and the execution of classification]*** |
| ***[EPPO]*** | ***[Drafts and maintains the personal-data dimension, the data states and the enhanced regime (Sections 4.2–5) as policy content for adoption by Executive Management; concurs in exceptions under Section 5.4]*** |
| ***[Processing Owner]*** | ***[Decides exceptions under Section 5.4 (with EPPO concurrence) and takes anonymity conclusions for declassification under Section 6.2 on Legal's assessment]*** |
| ***[Legal]*** | ***[Assesses Art. 9(2) conditions and Art. 10 authorisations in G-L; assesses identifiability under Recital 26 for anonymity conclusions]*** |
| ***[DPO]*** | ***[Advises (C) on the scheme, on exceptions, on anonymity conclusions and on any decision concerning category 3 or 4 data; monitors compliance. The DPO does not approve classes, exceptions or declassifications]*** |
| ***[Data Steward (a Data Governance role)]*** | ***[Maintains classification and labels for systems and datasets; may not exempt itself from Section 5]*** |
| ***[Data Owner (business unit)]*** | ***[States the purpose of processing, from which the Data Steward and a Privacy Officer determine the class; may not exempt itself from Section 5]*** |
| ***[Privacy Officer(s) / Privacy Engineer(s)]*** | ***[Implement the privacy dimension of labelling and label distribution; confirm corrections (Section 6.5); escalate non-conformities]*** |

The full R/A/C/I breakdown of the "Data Classification" process is in the RACI Matrix (Document 5, Section 6, row S1); the table above summarises it for this document.

A disagreement between the Data Steward and a Privacy Officer over a class, or a challenge by the Data Owner, is decided by ***[the Head of Data Governance]*** after consulting ***[the EPPO]*** and, for category 3 or 4 data, the DPO. If the disagreement persists, it is resolved under the conflict-resolution matrix of the Interface and Integration Model (Document 3, Section 5), with ***[Executive Management]*** as final arbiter. The decision and its reasons are recorded in attribute (v).

## **8. Links to Other Framework Documents**

* Feeds the RoPA (Document 21) and the Data Inventory and Data Flow Maps (Document 23) with the data class.
* Feeds the Data Retention and Disposal Policy (Document 11): retention is set by reference to the data class.
* Uses the Regulatory Applicability Matrix (Document 7) for jurisdiction-specific special-category, criminal-offence and biometric rules and for consent ages.
* The data class and the presence of category 3 or 4 data are inputs to Document 18 (Section 3.4, Factor B); this document does not calculate risk. Acceptance authority — Document 8, Section 5.
* Evidence packs referenced in attribute (v) feed the Privacy Risk Register (Document 22).
* Protective measures (Section 5.4) and labelling tooling are connected through Document 9.
* Qualification of Privacy Officers and Engineers — Document 6; Data Governance roles are qualified by their own function.
* Labels and attributes (iv)–(v) are the basis for conformity checks under Document 27.
* The boundary with Data Governance — Document 3, Section 3.3.
* Review frequency — Document 29.
* Transfers of classified data — Document 12; consent standards for category 3 data — Document 13; incident severity — Document 14; proportionality of data subject request verification — Document 15; privacy-by-design controls — Document 16; depth of vendor due diligence — Document 17.

## **9. Review Cycle**

The review frequency and triggers for an ad hoc review are set by the Policy Review Cycle (Document 29). An ad hoc review is mandatory when applicable law or case law affecting the definition of special-category, criminal-offence or biometric data changes (Document 7), and when the corporate DG standard changes.

## **10. Approval**

This document was adopted by ***[Executive Management]*** on ***[date]***. Document owner: ***[Head of Data Governance (CDO)]***; privacy dimension maintained by ***[EPPO]***.

# **Part B — Worked Example: PanEuropean Bank AG**

**PanEuropean Bank AG — Data Classification Policy**

Effective date: 20 October 2026 · Version: 2.0 · Document owner: Chief Data Officer (Data Governance) · Privacy dimension maintained by: Chief Privacy Officer (EPPO) · Adopted by: Management Board, 20 October 2026

*A fictional legal entity, presented solely for illustrative purposes.*

***Fictional Document History (illustrative)***

| Version | Date | Changes |
| :---- | :---- | :---- |
| 1.0 | 1 March 2026 | First version. Owners at the time: Data Governance (CDO) and Group DPO |
| 1.1 | 1 October 2026 | Section 5.2 aligned with the escalation model then in force; age-threshold wording in Section 4.2 aligned with the Regulatory Applicability Matrix (Document 7); Document 9 title unified |
| 2.0 | 20 October 2026 | Re-baselined to the new role model: CDO as owner, Chief Privacy Officer maintaining the privacy dimension, Group DPO advice only; criminal-offence data separated from special categories; data states, inferred sensitive data and the biometric distinction added; declassification only through a controller anonymity conclusion; acceptance authority aligned with Document 8, version 3.0 |

## **Glossary of Terms**

*The Part A glossary applies unchanged.*

## **1. Purpose**

This document establishes PanEuropean Bank AG's data classification scheme across its five countries of presence, covering personal data, special-category data (health data, biometric data, inferred special-category data), criminal-offence data, the data state, and the rules for handling each class.

The document is tagged [DG]: PanEuropean's corporate classification standard is owned by Data Governance under the Chief Data Officer; this document adds the privacy overlay.

## **2. Status as a Privacy Overlay on Data Governance**

PanEuropean's corporate Data Classification Standard and the corporate data catalogue are owned by Data Governance under the CDO; day-to-day maintenance is delegated to Data Stewards (one steward supports the privacy function at 15% FTE, Document 4). The Chief Privacy Officer maintains the personal-data dimension, the data states and the enhanced regime without a parallel scheme (Document 3, Section 3.3). The Group DPO advises; it does not report to the CDO.

Labelling and PET transformations are supported by the Bank's privacy engineering platform (PEP, illustrative) within the limits of its validation record (Document 9, Section 8).

## **3. Scope**

* All data processed by PanEuropean Bank AG — by the head office in Germany and the branches in France, Italy, Spain and Poland — whatever the format or location (core banking, data lake, cloud infrastructure).
* India and the United States are recipient countries, not countries of presence; transfers are governed by Document 12.

This document does not govern, at PanEuropean: risk assessment (Document 18); retention (Document 11); InfoSec measures for transactional and anti-fraud data (Document 3, Section 3.2); lawful bases and conditions (G-L; Documents 7 and 13).

## **4. Classification Scheme**

***4.1 Baseline Sensitivity Levels***

PanEuropean's corporate DG standard has four levels: Public, Internal, Confidential, Restricted.

***4.2 Personal Data Dimension***

PanEuropean applies the five categories of Part A unchanged. Application to the main data domains:

| Data Domain | Level | Category | Data State |
| :---- | :---- | :---- | :---- |
| Public tariffs and product descriptions | Public | Non-personal | — |
| Internal operating procedures | Internal | Non-personal | — |
| Customer data: name, address, contact details | Confidential | Personal data | Personal |
| Transactional data (payment history) | Confidential | Personal data, flagged "may reveal special categories" (Section 4.4) | Personal |
| Transaction categories or customer segments derived from payments to trade unions, political parties, religious communities, clinics or pharmacies | Restricted | Special category (inferred, Art. 9) — not created by design (Section 5); the classification applies if such data are ever created or received | Personal |
| Credit-scoring data and anti-fraud features (special-category data and their proxies excluded by design) | Restricted | Personal data | Personal |
| Pseudonymised analytics extracts (keyed hashing of customer identifiers) | Restricted | Personal data | Pseudonymised |
| Synthetic calibration dataset for the credit-scoring model (DPIA-CS-TRAIN-01) | Restricted | Personal data | Synthetic — no anonymity conclusion |
| Published credit-portfolio statistics (Document 18, Example 3.1) | Public | Non-personal | Anonymous information (controller conclusion; annual re-assessment) |
| Biometric template generated by the biometric module of PanEuropean's app and stored only on the customer's device | Restricted | Special category (Art. 9) | Personal |
| Log-in through the device operating system's own biometric function (PanEuropean receives only a pass/fail assertion) | Confidential | Personal data (authentication event; no biometric data processed by PanEuropean) | Personal |
| Health data provided when arranging payment protection insurance (PPI) | Restricted | Special category (Art. 9) | Personal |
| AML/KYC files (identification and due-diligence records) | Restricted | Personal data | Personal |
| Screening results containing adverse media or allegations of offences, and fraud-case records concerning alleged or established offences | Restricted | Criminal-offence data (Art. 10) — processed under the authorisation of AML law (German Money Laundering Act (GwG) and branch-country AML law; Regulation (EU) 2024/1624 from 10 July 2027) or other Union or Member State law, as confirmed by Legal & Compliance in G-L | Personal |
| Sanctions-list hits and politically-exposed-person status | Restricted | Personal data (not Art. 10 data as such; reclassified where the record concerns an alleged or established offence) | Personal |
| Data of minor holders of children's banking products | Restricted | Personal data + marker "Vulnerable data subject" | Personal |

Transactional data are Confidential, not Restricted: the class reflects the nature of the data, not their value to fraudsters, which the CISO's information-security classification covers (Document 3, Section 3.2). Derived features that reveal special categories are Restricted and category 3.

Vulnerable data subjects: the digital-consent ages in the five countries range from 14 to 16 (Document 7, Section 4.1); they apply only to information-society services offered on the basis of consent. Contractual capacity for children's banking products follows national civil law. As an internal design choice, marketing features of the app are off for users under 16 (Document 7).

## **5. Special-Category and Criminal-Offence Data — Enhanced Regime**

This section applies to category 3 and category 4 entries. Data of minor product holders (category 5 marker) are covered by Document 13 and by Document 18's vulnerability factor.

| Entry | Legal basis checked in G-L | Mandatory Control |
| :---- | :---- | :---- |
| Biometric template of the app's biometric module | Biometric data for unique identification, Art. 9(1); explicit consent (Art. 9(2)(a)), freely given because a non-biometric log-in is always available | Template generated and stored only on the customer's device; PanEuropean holds no server-side template. Document 7 records CNIL guidance on biometric authentication for France; PanEuropean applies the device-only design in all five countries as an internal design choice |
| PPI health data | Health data, Art. 9(1); explicit consent (Art. 9(2)(a)) and Art. 9(2)(f) where needed for legal claims; the insurer is a separate controller for underwriting and claims | DPIA before product launch; pseudonymisation in the underwriting-support environment on PEP; never used for credit scoring |
| Inferred special-category transaction features | Art. 9(1) by indirect revelation (C-184/20; C-252/21). No Art. 9(2) condition is available for marketing or credit scoring; for any other use, G-L would require a specific Art. 9(2) condition — in practice explicit consent obtained as such (specific, informed, separate from the service terms and withdrawable); a request for a budgeting service is not by itself explicit consent | **Chosen design: PanEuropean does not create such categories.** The transaction-categorisation taxonomy used for the budgeting tool, analytics and models contains no category for trade unions, political parties, religious communities, health providers or pharmacies; such payments are mapped to generic categories (for example "Other payments"), and no feature, label or segment inferring an Art. 9 characteristic is derived for marketing, scoring or any other purpose. Raw transaction data keep the "may reveal special categories" flag. Any proposal to introduce such a category requires G-L with a specific Art. 9(2) condition and a DPIA before development (Document 19) |
| Screening and fraud-case records with Art. 10 content | Art. 10 — authorisation by AML law and other Union or Member State law | Access restricted to Compliance and Fraud Prevention; every access logged; alerts, including false positives, handled by Compliance (AML Officer) and Fraud Prevention under AML procedures; the Group DPO advises on the processing design and is not involved in individual alerts |

***5.1 Mandatory DPIA Regardless of Triage Outcome***

PanEuropean applies the internal policy of Part A: the launch of payment protection insurance required a DPIA regardless of the triage questionnaire, because the dataset contains health data; the same applies to any new use of biometric data or of criminal-offence data.

***5.2 Stricter Escalation Threshold***

The "Special Categories of Data" component of Factor B in PanEuropean's methodology adds +2 to the severity index where category 3 or 4 data are concerned by the scenario (Document 18, Section 3.4). Group DPO advice is required for every decision on such processing, whatever the tier (Document 8, Section 5, table of mandatory DPO-advice triggers). Acceptance authority — Document 8, version 3.0, Section 5, unchanged:

| Residual Tier | Who Decides | Additional Mandatory Step | Timeframe |
| :---- | :---- | :---- | :---- |
| Low | Processing Owner | Recorded in the evidence pack; Group DPO advice (required for category 3/4 data) | — |
| Medium | Processing Owner, with the Chief Privacy Officer's concurrence | Group DPO advice recorded; conditional acceptance expires (default 12 months) | 3 business days |
| High | The Chief Risk Officer, as the Management Board member designated by the Board's delegation | G-36 evaluated by Legal & Compliance; prior consultation of the HBDI whenever the Art. 36 test is met; Group DPO advice recorded; Supervisory Board Risk Committee informed | 5 business days after the G-36 step |
| Critical | Not acceptable | Stop or redesign; any decision after redesign sits with the Management Board | Immediately |

Example: the PPI health-data application review — Low likelihood × Significant severity = Medium; accepted by the Head of Insurance Distribution with the Chief Privacy Officer's concurrence; Group DPO advice recorded; G-36 evaluated, test not met (Document 8, Part B).

***5.3 Access Restriction***

Access to screening and fraud-case records is limited to Compliance and Fraud Prevention on a need-to-know basis; every access is logged; access from other units (for example Digital Banking) is not technically granted.

***5.4 Mandatory Protective Measures — No Exceptions at the Data Owner or Data Steward Level***

| Data Category | Protective Measure | Applied In |
| :---- | :---- | :---- |
| Biometric template | Architectural measure: device-bound storage, no central template; non-biometric alternative | Mobile app |
| PPI health data | Pseudonymisation (remains personal data) and access restriction | Underwriting-support environment on PEP |
| Analytics and modelling extracts | Pseudonymisation, or synthetic data from a differentially private generator that has passed the PET Assessment Module (Document 18, Section 3.3.2); special-category fields excluded unless a DPIA and an Art. 9(2) condition support their use | Data lake, data warehouse and BI |
| AML screening data in test environments | Synthetic data that has passed the PET Assessment Module | Non-production environments |
| AML screening data in production | **Exception** (Section 5.4 of Part A): matching against official lists requires clear names, so pseudonymisation is not possible. Decided by the Processing Owner for AML screening (Head of Compliance — Document 25, Section 10) with the Chief Privacy Officer's concurrence and Group DPO advice; compensating controls — access restriction, logging, no export to analytics; expiry 12 months | Screening system |

Parameters of the techniques (for example the DP statement of each generator and the disclosure-control thresholds) are set in PanEuropean's PET Standard (Document 9, Section 6). Differential privacy and k-anonymity are recorded there as separate guarantees; this document does not set parameters.

## **6. Labelling and Label Distribution Rules**

***6.1 Metadata Standard***

PEP populates the five attributes of Part A in the corporate data catalogue and adds two platform-specific fields (vi)–(vii). Example: the synthetic calibration dataset for the credit-scoring model.

| Attribute | Example Value (Synthetic Calibration Dataset) |
| :---- | :---- |
| (i) Data class and data state | Restricted / Personal data; state: synthetic — no anonymity conclusion has been made, so the dataset stays in the category of its source (Section 6.2) |
| (ii) Residual risk tier | Medium — Document 18, Example 2.1-R; decision under DPIA-CS-TRAIN-01 (Document 19) |
| (iii) Date of last DPIA | 25 March 2026 (DPIA-CS-TRAIN-01) |
| (iv) Transformation provenance | Differentially private generator; ε 1.8 at δ 1×10⁻⁹; privacy unit one customer; Rényi DP accountant (Document 18, Section 3.3.5); source class Restricted / Personal data (credit-scoring data) |
| (v) Reference to evidence pack | EVP-2026-0012 — records the PET Assessment Module result, the lifetime-ledger entry and the acceptance decision of the Head of Credit Decisions, with Group DPO advice |
| (vi) Set processed | DI-CS-0873 — the immediate predecessor dataset (credit-scoring extract); its own attribute (i) records its class |
| (vii) Processing tool | PEP synthetic-data pipeline, version 2.3, run of 20 March 2026 |

Attribute (i) describes the current dataset, not its source. Fields (iv)–(vii) document how the dataset was produced and on what evidence it is used; they do **not** declassify it. The dataset is made available only to Data Science for model calibration, as decided under DPIA-CS-TRAIN-01.

***6.2 Label Distribution Across Systems and Declassification***

* Data catalogue: owned by Data Governance (CDO); pseudonymised and synthetic datasets produced on PEP are registered as new tracked objects with their data state.
* Data warehouse and BI: customer identifiers are pseudonymised before loading into analytical layers; the data remain personal data.
* Data integration: flows involving recipients in India and the United States are reflected in the Data Inventory (Document 23) and pass G-TIA under Document 12; ETL jobs that process personal data or derived datasets pass a privacy control before production.
* Declassification example: the credit-portfolio statistics published on the open-data portal (Document 18, Example 3.1) were moved to category 1 only after the Processing Owner for the publication recorded the conclusion that they are anonymous information, on Legal & Compliance's assessment with "anyone" as the recipient and with Group DPO advice; the conclusion is re-assessed annually and before every further release from the same population.

***6.3 Automated and Manual Labelling***

In core banking and the data lake, labelling is automated by the built-in classifier and PEP's ingestion pipelines; the classifier for inferred special-category transaction features is recorded in PEP's validation record (Document 9, Section 8). Manual labelling remains a fallback for scanned KYC documents and is spot-checked by the Data Steward.

***6.4 Label Review Frequency***

Labels are reviewed at least as often as this document (Section 9) and ad hoc — for example when payment protection insurance is relaunched in a new configuration, when the screening-list provider changes, or when a new transaction-categorisation feature is introduced.

***6.5 Ad Hoc Correction of Misclassification***

Example: the "Contact Centre Enquiry History" dataset was first classified Internal / Non-personal. During a contact-centre audit, the Data Steward found call transcripts mentioning customers' health and proposed reclassification to Restricted / Special category. A Privacy Officer confirmed the new class within 3 business days; the correction was applied and logged, and the Group DPO was informed because the correction concerned category 3 data. The DPIA triage for the contact-centre processing was re-run.

## **7. Roles and Responsibilities**

| Role | Responsibility at PanEuropean |
| :---- | :---- |
| Chief Data Officer (Data Governance) | Accountable for classification (Document 5, row S1); owns the sensitivity levels, the data catalogue and the execution of classification |
| Chief Privacy Officer (EPPO) | Maintains the privacy dimension, data states and enhanced regime; concurs in exceptions under Section 5.4 |
| Processing Owners (for example Head of Credit Decisions, Head of Fraud Prevention) | Decide exceptions with Chief Privacy Officer concurrence; take anonymity conclusions on Legal & Compliance's assessment |
| General Counsel (Legal & Compliance) | Confirms Art. 9(2) conditions and Art. 10 authorisations in G-L; assesses identifiability for anonymity conclusions |
| Group DPO | Advises on the scheme, exceptions, anonymity conclusions and every decision on category 3 or 4 data; informed of corrections to or from those categories; monitors compliance |
| Data Steward (a Data Governance role, 15% FTE for the privacy function) | Maintains classification and labels; may not exempt itself from Section 5 |
| Data Owners (Digital Banking, Credit Decisions and other business units) | State the purpose of processing; may not exempt themselves from Section 5 |
| Privacy Officer(s) / Privacy Engineer(s) | Implement labelling on PEP; confirm corrections; escalate non-conformities |

Under PanEuropean's RACI Matrix (Document 5, Section 6), row S1: Responsible — Data Governance; Accountable — CDO; Consulted — Chief Privacy Officer, Group DPO, Privacy Engineer(s), General Counsel, CISO; Informed — Privacy Operations Lead.

A disagreement over a class (for example between Digital Banking and a Privacy Officer over a new product) is decided by the CDO after consulting the Chief Privacy Officer and, for category 3 or 4 data, the Group DPO. A persisting disagreement is resolved under Document 3, Section 5, with the Management Board as final arbiter. The decision and its reasons are recorded in attribute (v).

## **8. Links to Other Framework Documents**

* Feeds PanEuropean's RoPA (Document 21) and Data Inventory (Document 23).
* Feeds the Data Retention and Disposal Policy (Document 11), including retention of the biometric, health and Art. 10 entries of Section 5.
* Uses the Regulatory Applicability Matrix (Document 7) — the five countries of presence, biometrics, consent ages and AML law.
* Inputs to Document 18 (Section 3.4, Factor B); acceptance under Document 8, Section 5.
* Evidence packs referenced in attribute (v) feed the Privacy Risk Register (Document 22).
* Protective measures and PEP are connected through Document 9 (PET Standard, Section 6; validation record, Section 8).
* Qualification of privacy roles — Document 6.
* Conformity checks — Document 27; Data Governance boundary — Document 3, Section 3.3; review — Document 29.
* Transfers to India and the United States — Document 12; consent for PPI health data and biometrics — Document 13; incident severity — Document 14; request verification — Document 15; design controls including model training and Data Science datasets — Document 16; due diligence depth (for example for EuroCredit Bureau, an independent controller) — Document 17.

## **9. Review Cycle**

This document is reviewed under PanEuropean's Policy Review Cycle (Document 29). An ad hoc review is mandatory when national or supervisory-authority rules on biometric authentication in banking apps change in any of the five countries (Document 7), when case law on inferred sensitive data develops, and when the corporate Data Classification Standard changes.

## **10. Approval**

Version 1.0 (1 March 2026) and version 1.1 (1 October 2026) were adopted by the Management Board; Data Governance (CDO) and the Group DPO were owners at that time. Version 2.0 was adopted by the Management Board on 20 October 2026 on the joint proposal of the CDO and the Chief Privacy Officer, after consulting the Group DPO. Document owner: Chief Data Officer; privacy dimension maintained by the Chief Privacy Officer.

# **Normative Basis and References**

* Regulation (EU) 2016/679 (GDPR): Arts. 4(1), 4(5), 4(14), 4(15), 8, 9, 10, 18, 35(3)(b); Recitals 26, 51.
* CJEU, C-184/20, *OT v Vyriausioji tarnybinės etikos komisija*, 1 August 2022 (data indirectly revealing special-category information).
* CJEU, C-252/21, *Meta Platforms and Others v Bundeskartellamt*, 4 July 2023 (Art. 9 applies to data capable of revealing sensitive information).
* CJEU, C-413/23 P, *EDPS v SRB*, 4 September 2025 (the recipient's means as part of the contextual analysis; not a general rule on pseudonymised data or Chapter V).
* EDPB/EDPS Joint Opinion 02/2026 on the Digital Omnibus proposal, §19 (Chapter V implications of a recipient-relative approach still require guidance) — context only.
* EDPB Guidelines 01/2025 on pseudonymisation.
* EDPB Guidelines 02/2026 on anonymisation — public-consultation draft (8 July 2026), not final.
* Article 29 Working Party, Opinion 05/2014 on Anonymisation Techniques (WP216).
* Regulation (EU) 2024/1689 (AI Act), as amended by the AI Omnibus: Art. 10(5).
* Regulation (EU) 2024/1624 (AMLR) — applies from 10 July 2027; German Money Laundering Act (GwG) for the current regime.
* NIST SP 800-188, *De-Identifying Government Data Sets*; NIST SP 800-226 (final, March 2025).
* ISO/IEC 27001:2022, Annex A controls 5.12 (classification of information) and 5.13 (labelling of information) — bibliographic pointer; ISO/IEC 27559 and ISO/IEC 20889 — bibliographic pointers only.

# **International Adaptation**

> **Guidance.** The GDPR is the baseline. The applicability map for Canada is in Document 7, Section 3.1. This document does not claim compliance with any jurisdiction's law.

* **United Kingdom (headline).** UK GDPR Arts. 9 and 10 mirror the EU categories; conditions for special-category and criminal-offence data are completed by the Data Protection Act 2018 (Schedule 1), as amended by the Data (Use and Access) Act 2025 with phased commencement.
* **Switzerland (headline).** The revFADP's "sensitive personal data" is a single, wider list that includes, among others, data on administrative and criminal proceedings or sanctions and data on social-assistance measures; map them to categories 3 and 4 and apply the enhanced regime.
* **Canada — PIPEDA.** There is no closed list of sensitive data: sensitivity depends on context (Schedule 1, Principle 4.3.4), with health and financial information generally treated as sensitive. Use category 3 for information that is sensitive in its context and record the reasoning; the form of consent and safeguards follow from sensitivity (Principles 4.3 and 4.7).
* **Canada — Québec (P-39.1).** Personal information is sensitive when, by its nature or the context of its use or communication, it entails a high level of reasonable expectation of privacy; secondary uses and communications of sensitive information require express consent. Map such information to category 3. Anonymisation for Québec purposes follows the Québec regulation on the anonymisation of personal information.

# **Document History (PGF)**

| Release | Date | Changes |
| :---- | :---- | :---- |
| 1.0.0-rc.1 | 2026-10-26 | Canonical English Markdown; changes from internal ver.2: criminal-offence data (Art. 10) separated from special categories as its own category with the same controls and its own legal test; inferred special-category data added (C-184/20, C-252/21) with the bank-transaction example; data states added (personal, pseudonymised, anonymous information, synthetic, encrypted) with pseudonymised data kept personal (Art. 4(5), EDPB Guidelines 01/2025, C-413/23 P); declassification only through the controller's documented anonymity conclusion (Processing Owner on Legal's assessment with DPO advice, Document 18 PET module, periodic re-assessment) — synthetic data no longer declassified to "non-personal"; operating-system biometric authentication distinguished from biometric processing by the organisation's own software; AML/sanctions screening reworded (Art. 10 content under AML-law authorisation; sanctions hits and politically-exposed-person status not Art. 10 data as such) and the credit bureau removed from the screening example; AML alerts handled by Compliance, not the DPO; mandatory DPIA labelled internal policy; mandatory PET rule given a documented exception route; DPO changed from Accountable/approver to advisor (S1 accountable: Head of Data Governance); escalation table aligned with Document 8 (single decider, G-36, Critical not acceptable); Art. 8 consent age separated from contractual capacity; adoption moved to Executive Management; ε and k-anonymity no longer combined as one parameter set; example evidence-pack identifiers changed to EVP-YYYY-NNNN; example dates shifted by −12 months; calqued terms and inconsistent titles corrected; references and international adaptation added. Integration pass: Processing Owner for AML screening named (Head of Compliance, Document 25) |
