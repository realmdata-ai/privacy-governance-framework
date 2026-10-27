---
title: "Data Inventory and Data Flow Maps"
document_id: PGF-23
level: 2
release_version: 1.0.0-rc.1
status: release-candidate
authors: ["Alexey Neyman", "Val Khvatov"]
regulatory_reference_date: 2026-10-26
licence_proposed: "CC BY 4.0 (proposed; subject to rights-holder confirmation)"
source_provenance: "Derived from internal source set ver.2: Level2/23. Data-Inventory-and-Data-Flow-Maps_ENG.docx.md; sha256 e98bc3bbb5ef8af0d0cf3a005e14153b8a2da61c83dee759d7b90e12168f0863"
---

# PGF-23 — Data Inventory and Data Flow Maps

*Privacy Governance Framework (PGF) · Level 2 — Policies and Standards · Release 1.0.0-rc.1 · Regulatory reference date: 26 October 2026*

> **Status and use.** Part A is a reusable template. Part B is a worked example for a fictional organisation (PanEuropean Bank AG); all names, figures, dates and records in Part B are illustrative. Nothing in this document is legal advice or a statement about any real organisation, product or provider.

# **About This Document**

**Purpose.** Document 23 sets the privacy metadata that the organisation adds to its corporate data catalogue — for systems, datasets and unstructured repositories that hold personal data — and the privacy-specific requirements for data flow maps: where data are held, from which jurisdictions and by whom they are accessed, which external recipients receive them, how derived datasets descend from their sources, and how an erasure reaches every derived copy.

**Scope.** All systems, datasets (including derived, pseudonymised and synthetic datasets), unstructured repositories and AI artefacts that hold personal data, and all flows of personal data between them and to external recipients. The document is tagged [DG]: maintaining a data catalogue is a Data Governance function; this document is a privacy overlay on the corporate catalogue, not a parallel catalogue.

**Relationships.** The boundary with Data Governance is set in the Interface and Integration Model (Document 3, Section 3.3). The data class, data state and the shared metadata attributes come from the Data Classification Policy (Document 10, Section 6.1). The Record of Processing Activities (Document 21) is authoritative on purposes, lawful bases and transfers at process level; this document is authoritative on location, access and flows. Whether a flow is a transfer is decided under the Cross-Border Data Transfer Policy (Document 12, Section 2.1) and the TIA Methodology (Document 20). Retention and the erasure cascade follow Document 11. Roles follow the RACI Matrix (Document 5, row S3).

# **How to Use This Document**

Part A is a template. Text in ***[square brackets, bold italic]*** is a fillable or illustrative placeholder. Blocks marked **Guidance** are removed from the adopted version. Part B shows the template completed for the fictional PanEuropean Bank AG, with an excerpt of the catalogue, a flow-map excerpt and three fully expanded records.

> **Guidance.** The boundary rule with Data Governance is established in the Interface and Integration Model (Document 3, Section 3.3). If that model has not yet been adopted, start there.

# **Table of Contents**

**About This Document**
**How to Use This Document**
**Part A — Template**
Glossary of Terms
1. Purpose
2. Status of the Privacy Overlay over Data Governance
3. Scope
4. Privacy Metadata Added to the Corporate Catalogue
5. Data Flow Map — Privacy-Specific Requirements
6. Rules for Updating and Distributing Privacy Metadata (6.1–6.6)
7. Roles and Responsibilities
8. Relationship to Other Framework Documents
9. Review and Amendment
10. Approval
**Part B — Worked Example (fictional): PanEuropean Bank AG** (same structure)
**Appendix to Part B — Example Catalogue Records and Flow Map**
**Normative Basis and References**
**International Adaptation**
**Document History (PGF)**

# **Part A — Template**

**Data Inventory and Data Flow Maps [DG] of *[Legal name of the organisation]***

*Effective date: **[DD Month YYYY]** · Version: **[x.x]** · Document owner: **[Head of Data Governance]**, with the privacy overlay maintained by **[the EPPO]** · Adopted by: **[Executive Management]***

***Version History***

| Version | Date | Changes |
| :---- | :---- | :---- |
| ***[1.0]*** | ***[DD.MM.YYYY]*** | ***[Initial version of the document]*** |
| ***[x.x]*** | ***[DD.MM.YYYY]*** | ***[Brief description of material changes]*** |

## **Glossary of Terms**

*This table lists only terms defined by this document itself; terms used here but defined in another document are not repeated in this table.*

| Term | Definition / Reference |
| :---- | :---- |
| Catalogue record | A record of the corporate data catalogue for a system, a dataset or an unstructured repository, identified DI-…; this document adds privacy metadata to it. |
| Access jurisdiction | A country or international organisation from which a person or entity can access the data — including by remote access — as distinct from the country where the data are physically held. |
| External recipient | A legal entity outside the organisation to which data are disclosed or made available: a processor, a joint controller, an independent controller, or a public authority where the law requires disclosure. |
| Lineage | The recorded descent of a derived dataset (pseudonymised extract, feature store, synthetic dataset, model, aggregate) from its source records. |
| Erasure propagation route | The recorded way in which an erasure, a withdrawal of consent or a restriction reaches a derived dataset or a copy (Document 11, Section 3.5). |

## **1. Purpose**

This document establishes the privacy metadata that ***[organisation name]*** adds to its corporate data catalogue and the privacy-specific requirements for its data flow maps. It makes visible where personal data are held and accessed, which external recipients receive them, which flows may be transfers under Chapter V, how derived datasets relate to their sources, and how erasure and restriction reach every copy.

## **2. Status of the Privacy Overlay over Data Governance**

***[Confirm that the organisation has an operating corporate data catalogue owned by the Data Governance function (Chief Data Officer or equivalent). Boundary rule: Data Governance owns the catalogue as a whole — the list of systems and datasets, schemas, technical fields and the technical flow map. The privacy function does not keep a parallel list of systems; it adds a "contains personal data" flag and the privacy metadata of Section 4 to the existing catalogue records, and registers the outputs of its own transformations (pseudonymised and synthetic datasets) in the catalogue as new records.]***

> **Guidance.** This boundary rule is set in the Interface and Integration Model (Document 3, Section 3.3, "Data Catalogue" and "Metadata Management") and is only applied here.

## **3. Scope**

* ***[All systems that store or process personal data, whether hosted on the organisation's own infrastructure, in the cloud or by processors.]***
* ***[Datasets, including derived datasets — pseudonymised extracts, feature stores, synthetic datasets, training datasets, model artefacts and aggregates — each registered as its own record with its lineage (Section 6.2).]***
* ***[Unstructured repositories — enterprise content management, e-mail archives, file shares — and AI artefacts — prompts and outputs of AI services, retrieval indexes and embeddings, model weights — where they contain or can reveal personal data.]***
* ***[All flows of personal data between catalogue records and to external recipients, including remote access by external entities and access from abroad by the organisation's own staff (Section 5).]***
* ***[All categories of data subjects: customers, prospects, guarantors, beneficial owners, payees, employees, candidates, visitors, counterparties' staff and shareholders, as applicable.]***
* ***[Automated privacy tooling (Document 9) that computes directly on personal data — for example synthetic-data generation, application of privacy-enhancing techniques or risk metrics on source data — is registered as a system on the same basis as any other system; its role as a metadata tool (Section 6) does not replace that registration.]***

This document does not govern:

* data classification — the data class and data state are set by Document 10;
* technical information-security measures — the boundary with the CISO is set in Document 3, Section 3.2;
* purposes and lawful bases — recorded in the RoPA (Document 21);
* the legal assessment of transfers — the transfer-status conclusion and the TIA belong to Documents 12 and 20; this document flags flows that may meet the transfer criteria and records the outcome.

## **4. Privacy Metadata Added to the Corporate Catalogue**

> **Guidance.** The fields below are the mandatory minimum privacy addition to a catalogue record. They do not override the catalogue's technical fields (system owner, storage format and so on). Fields marked "Document 10" are attributes of the shared metadata standard (Document 10, Section 6.1); they are referenced, not maintained in parallel.

| Field | Content |
| :---- | :---- |
| "Contains Personal Data" Flag | ***[Yes / No; set on registration or when personal data are discovered (for example during a DPIA, an audit or automated discovery). A system or repository missing from the catalogue is first registered by Data Governance; the privacy function keeps no record outside the catalogue]*** |
| Data Class and Data State (Document 10, attribute (i)) | ***[Level / category and data state (personal, pseudonymised, synthetic, encrypted, anonymous information) under Document 10, Sections 4.1–4.3; the maximum on each axis among the data held]*** |
| Categories of Data Subjects and Data | ***[Categories of data subjects; categories of data held, including special-category (Art. 9) and criminal-offence (Art. 10) content; approximate volume]*** |
| Hosting Jurisdiction | ***[Country or region where the data are physically held, including backups — a technical field, authoritative here]*** |
| Access Jurisdictions | ***[Countries or international organisations from which the data can be accessed, and by whom: the organisation's own staff (same legal entity), a group entity, a processor or another external entity; including remote access for support or administration]*** |
| External Recipients | ***[Each external recipient with its role (processor, joint controller, independent controller, public authority), its establishment, and a reference to the vendor or counterparty record (Document 17)]*** |
| Cross-Border Flow Flag | ***[Set where a flow or access by an external entity may meet the three cumulative criteria of a transfer (Document 12, Section 2.1): (1) the exporter is subject to the GDPR for the processing; (2) it discloses or makes the data available, including by remote access, to another controller, joint controller or processor; (3) that importer is in a third country or is an international organisation, wherever located. Not set for an ordinary flow between recipients established in the EEA, nor for access by the organisation's own staff while abroad (no other entity); never set or cleared on geography alone. A flag triggers the transfer-status review and, for the Art. 46 branch, the TIA (Document 20)]*** |
| Transfer Reference | ***[TIA identifier (Document 20), transfer-status conclusion (Document 20, Section 3.3) or Art. 49 derogation record (Document 12), as applicable; "not applicable" with a reference where a conclusion found no transfer]*** |
| RoPA References | ***[RoPA-… records of the processing activities that use this record (Document 21)]*** |
| Date of Last DPIA (Document 10, attribute (iii)) | ***[Date of the last DPIA covering processing that uses this record; the organisation may extend it to the DPIA identifier. DPIAs are performed per processing activity, so a system record shows the DPIAs of the activities that use it, or the triage outcome where none was required]*** |
| Residual Risk Tier (Document 10, attribute (ii)) | ***[Taken from the DPIA or the Document 18 calculation as recorded in the Privacy Risk Register (Document 22); not calculated here; "no residual-risk decision" where none was required]*** |
| Transformation Provenance and Lineage (Document 10, attributes (iv) and the organisation's lineage fields) | ***[For a derived dataset: the source records (DI-…), the technique or a reference to the PET Standard (Document 9), the run or version; for a source: the derived records that descend from it]*** |
| Reference to Evidence Pack (Document 10, attribute (v)) | ***[EVP-YYYY-NNNN for any formal decision on the record — residual-risk acceptance, anonymity conclusion, exception or class correction]*** |
| Retention and Erasure Propagation Route | ***[Row of the retention matrix of Document 11 applied to the record; how an erasure, consent withdrawal or restriction reaches the record and its derived copies (Section 6.6)]*** |
| Date of the Record's Last Privacy Review | ***[Date; review frequency — Section 6.4]*** |

## **5. Data Flow Map — Privacy-Specific Requirements**

* ***[Each flow of personal data is shown as a separate link on the flow map, whether or not both ends are in the same jurisdiction. Four link types are distinguished: (a) internal flow between catalogue records; (b) disclosure to an external recipient; (c) remote access by an external entity (processor, group entity or other) to data held by the organisation; (d) access from abroad by the organisation's own staff.]***
* ***[Each link records: the data categories, frequency and volume, the protection in transit and at the receiving end (for example encryption, tokenisation, masking), the RoPA record it serves and, for links (b) and (c), the recipient's role and the vendor or counterparty record (Document 17).]***
* ***[Links (b) and (c) that may meet the three transfer criteria carry the cross-border flow flag (Section 4) and a transfer reference. The flag triggers a review; it does not substitute for the transfer-status conclusion or the TIA. Link (d) is not a transfer; security and the other GDPR duties still apply. Disclosure to an international organisation is flagged wherever it is located. Where a transfer-status conclusion is unclear, the flow is treated as a transfer.]***
* ***[Privacy-enhancing techniques, trusted execution environments, homomorphic encryption and remote-access arrangements do not by themselves clear the flag (EDPB Guidelines 05/2021); they are recorded as protection of the link.]***
* ***[The flow map is maintained by Data Governance as part of the technical catalogue; the privacy function does not keep a parallel map, but verifies at each review that links (b) and (c) and the flags are complete.]***

## **6. Rules for Updating and Distributing Privacy Metadata**

***6.1 Metadata Standard***

***[This document does not set its own metadata standard. Attributes shared with the Data Classification Policy (Document 10, Section 6.1) are populated and distributed under that document's rules. The format of the fields specific to this document (Section 4) and their machine-readable representation are set in a technical specification outside the governance core (Document 9, Technology Implementation Package).]***

***6.2 Propagation on Data Transformation and Lineage***

* ***[The "contains personal data" flag, the data class and the data state follow the data through copying, derived computation and export. A derived dataset inherits, on each axis separately, at least the highest level and category among its sources, and the data state that reflects how it was produced (Document 10, Section 6.2).]***
* ***[Every derived dataset is registered as a new catalogue record with its lineage: source records, technique and run. Source records list the records derived from them.]***
* ***[Aggregation, masking, pseudonymisation, encryption or synthesis do not by themselves lower the class or remove the flag. Synthetic datasets in particular stay in the category of their source until an anonymity conclusion is made (Document 10, Section 6.2; Document 11, Section 3.2): synthetic records are generated by a model trained on personal data and can still disclose information about people in the source data.]***
* ***[The flag is removed or the category lowered to non-personal only on the controller's documented conclusion that the record is anonymous information under Recital 26 — taken by [the Processing Owner] on [Legal]'s assessment, with DPO advice, supported by the PET Assessment Module of Document 18 and its evidence pack — and re-assessed periodically. If a re-assessment does not confirm the conclusion, the record returns to its earlier class.]***

***6.3 Automatic and Manual Updates***

***[Automatic updating through integration with source systems has priority. Automated discovery scans structured stores, unstructured repositories and cloud services for personal data at least [annually] and on onboarding of a new system; findings outside the catalogue are registered by Data Governance. Manual updating is a fallback and is spot-checked.]***

***6.4 Review Frequency***

***[Privacy metadata are reviewed: (a) on a change of the purpose of processing, a system, an external recipient or an access jurisdiction; (b) on a non-conformity found in an audit (Document 27); (c) at least as often as set for this document by the Policy Review Cycle (Document 29). Reviews are not tied to the re-certification of any tool.]***

***6.5 Record Decommissioning***

***[When a system is decommissioned or a flow ends, Data Governance moves the catalogue record to an archived status under its own procedures. The privacy metadata and evidence packs linked to the record are kept for the period set in Document 11 for evidence and decision records, and are not deleted automatically with the system. The privacy function does not itself initiate decommissioning; that belongs to Data Governance and the Data Owner. Remaining personal data are disposed of under Document 11 before the record is archived.]***

***6.6 Erasure Propagation Hooks***

* ***[Each record states its erasure propagation route (Section 4). An erasure on request, at the end of a retention period or on withdrawal of consent where consent was the basis propagates along the lineage to every derived record that has not been concluded anonymous — pseudonymised copies, feature stores, synthetic datasets, training sets and models (Document 11, Section 3.5).]***
* ***[For models and synthetic datasets the Processing Owner records, on Legal's assessment with DPO advice, a contextual conclusion on the current artefact: whether it still contains, or allows the extraction of, the person's data. Where erasure is required, the artefact is restricted at once and erased or regenerated without undue delay by a stated deadline; exclusion from the next scheduled run alone is used only where the recorded conclusion shows that the current artefact no longer contains the person's data or that an Art. 17(3) exception applies.]***
* ***[Batch or reconciliation runs never extend a retention period or a request deadline. Categories with short periods (for example video recordings) expire automatically at the end of each period, independently of any batch run. Restrictions under Art. 18 and Art. 17(3) exceptions move the data to the restricted state (Document 11, Section 4.1) on every record along the lineage.]***
* ***[Where the route depends on a processor, the record names the processor and the contractual deletion confirmation (Document 17).]***

## **7. Roles and Responsibilities**

| Role | Responsibility |
| :---- | :---- |
| ***[Data Governance (Chief Data Officer)]*** | ***[Owns the corporate catalogue and the flow map; approves changes to the catalogue's structure; registers systems, repositories and derived datasets; runs automated discovery (Document 5, row S3: Responsible)]*** |
| ***[Data Steward]*** | ***[Maintains catalogue records at the level of specific systems and datasets, including lineage]*** |
| ***[Data Owner (business unit)]*** | ***[States the purpose for which a system is used, on which the Data Steward and Privacy Officer(s) set the flag and the class]*** |
| ***[Privacy Operations Lead]*** | ***[Accountable for the privacy overlay (Document 5, row S3); resolves non-conformities escalated by Privacy Officer(s) and Privacy Engineer(s), including discrepancies with the RoPA (Document 21, Section 5)]*** |
| ***[Privacy Officer(s) / Privacy Engineer(s)]*** | ***[Implement and distribute the privacy metadata; verify that external-recipient and remote-access links and cross-border flags are complete; escalate non-conformities to the Privacy Operations Lead]*** |
| ***[Legal]*** | ***[Records the transfer-status conclusion for flagged flows and schemes on documented evidence (Document 20, Section 3.3); the conclusion is returned to the record]*** |
| ***[Processing Owner]*** | ***[Consulted on records used by its processing; records the contextual conclusion on derived artefacts for erasure (Section 6.6)]*** |
| ***[DPO]*** | ***[Informed (Document 5, row S3); advises on transfer-status conclusions and on the metadata standard; may review the inventory in the compliance monitoring it organises (Art. 39(1)(b)). The DPO does not make the transfer-status determination and does not own the catalogue]*** |

## **8. Relationship to Other Framework Documents**

* Relies on the Data Classification Policy (Document 10, Section 6.1) for the shared metadata attributes (data class and state, residual risk tier, date of last DPIA, transformation provenance, evidence pack); this document adds the fields specific to systems, repositories and flows.
* Is the source of technical fields for the RoPA (Document 21): authoritative on location, access and flows; the RoPA is authoritative on purposes, lawful bases and transfers at process level.
* The cross-border flow flag triggers the transfer-status review and, where applicable, the TIA (Document 20); the transfer criteria are those of Document 12, Section 2.1.
* Is an input to the DPIA (Document 19): the systematic description of processing uses this catalogue.
* The residual risk tier is taken from the DPIA or the Document 18 calculation as recorded in the Privacy Risk Register (Document 22); this document does not calculate risk.
* Retention, the restricted state and the erasure cascade follow Document 11; external recipients link to the vendor and counterparty records of Document 17.
* Tooling for metadata automation is connected through the Privacy Automation and Tooling Strategy (Document 9); this document names no platform.
* Completeness and accuracy are tested in the Privacy Audit and Monitoring Programme (Document 27).
* The boundary with Data Governance is set in the Interface and Integration Model (Document 3, Section 3.3).
* The process is supporting process S3 of the Privacy Governance Process Map (Document 24).

## **9. Review and Amendment**

This document is reviewed under the Policy Review Cycle (Document 29). An unscheduled review is required on a material change to the corporate catalogue and on a change of law, case law or guidance affecting the definition of a transfer (Document 7). Amendments are prepared by ***[the Head of Data Governance]*** with ***[the EPPO]*** for the privacy overlay, with DPO advice, and adopted by ***[Executive Management]***.

## **10. Approval**

This document is adopted by ***[Executive Management]*** on ***[date]***. Document owner: ***[Head of Data Governance]***; privacy overlay maintained by ***[the EPPO]***.

# **Part B — Worked Example (fictional): PanEuropean Bank AG**

**PanEuropean Bank AG — Data Inventory and Data Flow Maps [DG]**

*Effective date: 20 October 2026 · Version: 2.0 · Document owner: Chief Data Officer, with the privacy overlay maintained by the Chief Privacy Officer · Adopted by: Management Board*

*A fictional organisation, prepared solely for illustrative purposes.*

***Fictional document history (illustrative)***

| Version | Date | Changes |
| :---- | :---- | :---- |
| 1.0 | 1 March 2026 | First version, adopted by the Management Board; owners then the CDO and the Group DPO |
| 2.0 | 20 October 2026 | Re-baselined to Charter v3.0 and the RACI Matrix v4.0: single owner (CDO) with the privacy overlay maintained by the Chief Privacy Officer; access jurisdictions, external recipients, lineage and erasure-propagation fields added; cross-border flag defined by the three transfer criteria; the former PET-scheme exclusion test removed; synthetic datasets no longer declassified by generation; reviews decoupled from tool re-certification; catalogue excerpt corrected and extended (data warehouse, document management, consent management system, customer-service assistant, federated-learning node, delivery provider) |

## **Glossary of Terms**

The terms of Part A apply. Local term: **Corporate data catalogue** — the CDO's catalogue of systems, datasets and flows, with the privacy extension described in this document.

## **1. Purpose**

This document establishes the privacy overlay over PanEuropean Bank AG's corporate data catalogue: which systems, datasets and repositories hold personal data, where they are held and accessed, which external recipients receive data, and how derived datasets and erasures are traced.

## **2. Status of the Privacy Overlay over Data Governance**

PanEuropean's corporate data catalogue is owned by the Chief Data Officer and covers all data types. This document creates no parallel catalogue: Privacy Officers and Privacy Engineers add the "contains personal data" flag and the fields of Section 4 to existing records, and register the pseudonymised and synthetic datasets produced on the Bank's privacy engineering platform (PEP, illustrative) as new records (Document 3, Section 3.3).

## **3. Scope**

All systems, datasets and repositories of PanEuropean Bank AG and its branches in Germany, France, Italy, Spain and Poland that hold personal data of customers, prospects, guarantors, beneficial owners, payees, employees, candidates, branch visitors and counterparties' staff. Specific records are kept in the catalogue itself; the Appendix shows an excerpt. Unstructured repositories in scope include the Legal & Compliance document-management system and the customer-service message archive; AI artefacts in scope include prompts and outputs of the customer-service assistant (none sent since 26 October 2026), the credit-scoring model artefacts and the federated-learning model updates. PEP is registered as a system (DI-PEP-01) because it computes on personal data; its role as a metadata tool (Section 6) is separate.

## **4. Privacy Metadata Added to the Corporate Catalogue at PanEuropean**

PanEuropean applies the fields of Part A, Section 4, with these choices:

* **Date of last DPIA.** Extended to the DPIA identifier and date (Document 10, attribute (iii)).
* **Residual risk tier.** Taken from the DPIA or the Document 18 calculation as recorded in the Privacy Risk Register (Document 22).
* **Lineage.** Recorded through Document 10 attributes (iv), (vi) "Set processed" and (vii) "Processing tool" for datasets produced on PEP, and through the catalogue's lineage fields for other derived datasets.
* **Access jurisdictions.** Recorded per access route: PanEuropean staff (one legal entity in five EEA countries), processors' staff, group entities, other external entities.
* **Retention.** The name of the row of Document 11, Part B, Section 5.

## **5. Data Flow Map at PanEuropean — Privacy-Specific Requirements**

* The four link types of Part A, Section 5 are used. Flows between the branches are internal flows of one legal entity in the EEA; they are not transfers.
* **Flagged flows** (Appendix, flow map): remote technical support by Example Cloud Services Pvt Ltd (fictional, India) — transfer, TIA-CLOUD-01; anti-fraud matching with the partner bank in India by private set intersection — treated as a transfer, TIA-PSI-01; the customer-service assistant of Example AI Provider Inc. (fictional, USA) — transfer, TIA-LLM-01, on G-TIA hold, no data sent since 26 October 2026; customer-instructed payments to payees' banks outside the EEA — assessed by General Counsel and, where they are transfers, carried out under Art. 49(1)(b)/(c) on the derogation record (Document 12).
* **Not flagged, with a recorded conclusion:** the federated-learning anti-fraud consortium — all members and the aggregation service are established in the EU, so no importer is in a third country (General Counsel's conclusion, EVP-2026-0041); the conclusion is re-checked on any change of membership, coordinator or hosting, and the privacy-enhancing techniques are not the reason for it.
* **Not flagged:** EuroCredit Bureau (independent controller, EEA), the core banking platform provider, the PEP support provider and the e-mail and push delivery provider (processors, EEA) and the PPI insurer (independent controller, EEA); access by PanEuropean staff travelling outside the EEA (same legal entity) — governed by the CISO's remote-access rules.
* The CDO's team maintains the flow map; Privacy Officers verify the completeness of external-recipient and remote-access links at each review.

## **6. Rules for Updating and Distributing Privacy Metadata at PanEuropean**

***6.1 Metadata Standard***

The shared attributes (i)–(vii) are those of Document 10, Part B, Section 6.1. The fields specific to this document are stored as an extension of the corporate catalogue in a machine-readable format and synchronised with PEP through its integration interface (Document 9). PEP's role as a metadata tool is distinct from its registration as a system (Section 3).

***6.2 Propagation on Data Transformation and Lineage***

* A synthetic dataset generated for model calibration is registered as a new record with the class and state of its source until an anonymity conclusion is made: the calibration dataset DI-CS-0874 is Restricted / Personal data, state "synthetic", derived from DI-CS-0873 (Appendix). Its generation does not declassify it.
* Pseudonymised analytics extracts in the data warehouse remain personal data (state "pseudonymised").
* The only record moved to non-personal is the published credit-portfolio statistics, on the Processing Owner's anonymity conclusion on Legal & Compliance's assessment with Group DPO advice, re-assessed annually and before each further release (Document 10, Part B, Section 6.2).

***6.3 Automatic and Manual Updates***

Automatic updating through PEP's integration with the catalogue has priority. The CDO's automated discovery scans structured stores and the document-management system quarterly and on onboarding of a system; systems outside the integration are updated manually and spot-checked by Privacy Officers.

***6.4 Review Frequency***

Privacy metadata are reviewed at least annually, in the fourth quarter, together with the Processing Owners' RoPA attestation (Document 21), and on any change of purpose, system, external recipient or access jurisdiction, or a non-conformity found in an audit (Document 27). Reviews are not tied to the re-certification of PEP (Document 9, Section 5).

***6.5 Record Decommissioning***

When a system is decommissioned or a flow ends (for example on a vendor replacement), the CDO's team archives the catalogue record after the remaining data have been disposed of under Document 11; the privacy metadata and evidence packs are kept under the Document 11 row "Evidence packs and decision records".

***6.6 Erasure Propagation Hooks***

* Pseudonymised extracts and feature stores: the Privacy Operations Lead propagates erasure through PEP's lineage records within 5 business days of the trigger (illustrative internal deadline), well within the one-month response period for a request; the monthly run only verifies completion.
* Synthetic calibration dataset and generator: within 5 business days, the Head of Credit Decisions records a contextual conclusion on the current artefacts on Legal & Compliance's assessment, with Group DPO advice; where erasure is required, the artefacts are restricted at once and regenerated without the customer's data within 30 days (illustrative), and the customer is excluded from every later run (Document 11, Part B, Section 3.5).
* Branch video: overwritten automatically after 72 hours (illustrative), independently of any batch run.
* Processors (Example Cloud Services Pvt Ltd, Example AI Provider Inc., the core banking platform provider, the delivery provider): deletion under the processing agreements, with deletion confirmation recorded.
* Automated propagation along lineage is planned (Document 9); until it is validated, the Privacy Operations Lead propagates and reconciles manually within the deadlines above.

## **7. Roles and Responsibilities**

| Role | Responsibility |
| :---- | :---- |
| Data Governance (CDO) | Owns the corporate catalogue and the flow map; registers systems, repositories and derived datasets; runs automated discovery |
| Data Steward | Maintains records at the level of specific systems and datasets, including lineage |
| Data Owner (business unit) | States the purpose for which a system is used — for example Credit Decisions for the credit-scoring infrastructure |
| Privacy Operations Lead | Accountable for the privacy overlay (Document 5, row S3); resolves non-conformities and discrepancies with the RoPA; runs manual erasure propagation until automation is validated |
| Privacy Officer(s) / Privacy Engineer(s) | Implement the privacy metadata through PEP; verify external-recipient and remote-access links and flags; escalate non-conformities |
| General Counsel (Legal & Compliance) | Records transfer-status conclusions for flagged flows and schemes, with Group DPO advice (Document 20, Section 3.3) |
| Processing Owners | Consulted on records used by their processing; record contextual conclusions on derived artefacts for erasure |
| Group DPO | Informed; advises on transfer-status conclusions and the metadata standard; may review the inventory in its Art. 39(1)(b) monitoring; makes no determination |

## **8. Relationship to Other Framework Documents**

* Shared attributes from Document 10, Part B, Section 6.1; this document adds system, repository and flow fields.
* Technical source for PanEuropean's RoPA (Document 21); each catalogue record lists its RoPA references and each RoPA record its DI-… references.
* Flagged flows are assessed under Documents 12 and 20 (TIA-CLOUD-01, TIA-PSI-01, TIA-LLM-01); the federated-learning conclusion is in Document 12, Part B, Section 3.
* Residual risk tiers as recorded in the Privacy Risk Register (Document 22).
* Retention and erasure cascade under Document 11; counterparties under Document 17; tooling through Document 9; audits under Document 27; boundary with Data Governance in Document 3, Section 3.3; process S3 of Document 24.

## **9. Review and Amendment**

This document is reviewed under the Policy Review Cycle (Document 29). An unscheduled review is required on a material change to the corporate catalogue and on a change to the Regulatory Applicability Matrix (Document 7) or to guidance that affects the definition of a transfer. Amendments are prepared by the CDO with the Chief Privacy Officer for the privacy overlay, with Group DPO advice, and adopted by the Management Board.

## **10. Approval**

Version 2.0 of this document was adopted by the Management Board of PanEuropean Bank AG on 20 October 2026, on the proposal of the Chief Data Officer and the Chief Privacy Officer and after Group DPO advice. Document owner: Chief Data Officer; privacy overlay maintained by the Chief Privacy Officer. Version 1.0 (1 March 2026) was adopted by the Management Board.

# **Appendix to Part B — Example Catalogue Records and Flow Map**

Status at 26 October 2026. Residual tiers are track (a) tiers taken from the DPIA or the Document 18 calculation as recorded in the Privacy Risk Register (Document 22). "Flag" is the cross-border flow flag of Section 4.

**Catalogue excerpt**

| Record | Hosting / access jurisdictions | Class and state | External recipients (role) | Flag and transfer reference | RoPA (Document 21) | DPIA or triage (attribute (iii)); residual tier (attribute (ii)) |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| DI-CORE-001 — Core banking platform | EEA (provider's data centres) / PanEuropean staff (EEA); provider's EEA staff | Restricted / Personal data (highest class held: credit and AML records) | Core banking platform provider (processor, EEA) | No | RoPA-CARD-01; RoPA-CREDIT-01; RoPA-AML-01; RoPA-P-PAY-01 | Triage per activity; no system-level decision |
| DI-CRM-014 — CRM: customer profile | Germany / PanEuropean staff (EEA) | Confidential / Personal data | None | No | RoPA-CSV-01; RoPA-MKT-01; RoPA-OFFER-01 | No DPIA (triage records of the activities); no residual-risk decision |
| DI-CRED-01 — Credit application and decision system | Germany / PanEuropean staff (EEA) | Restricted / Personal data | EuroCredit Bureau (independent controller, EEA) | No | RoPA-CREDIT-01; RoPA-CS-001; RoPA-CS-003 | DPIA-CS-INFER-01 and DPIA-CS-LAUNCH-01 for the planned automated design — High; decision pending |
| DI-CS-0873 — Credit-scoring extract (generator source) | Germany (PEP) / named Privacy Engineers | Restricted / Personal data | None | No | RoPA-CS-002 | DPIA-CS-TRAIN-01 — Medium |
| DI-CS-0874 — Synthetic calibration dataset | Germany (PEP; Data Science workspace) / Data Science | Restricted / Personal data; synthetic — no anonymity conclusion | None | No | RoPA-CS-002 | DPIA-CS-TRAIN-01 — Medium (EVP-2026-0012) |
| DI-CS-INFER-01 — Credit-scoring model infrastructure (pre-production) | Germany / Credit Decisions, Model Risk and AI Governance | Restricted / Personal data | None | No | RoPA-CS-003; RoPA-CS-001 | DPIA-CS-INFER-01 — High (inherent Critical); not in production; launch planned 1 February 2027 |
| DI-DWH-01 — Analytical data warehouse | Germany / PanEuropean analysts (EEA) | Restricted / Personal data; pseudonymised in analytical layers | None | No | RoPA-FRAUD-01; RoPA-CS-002 (validation extracts); portfolio analytics | Triage per activity |
| DI-ECM-01 — Legal & Compliance document-management system | Germany / Legal and Compliance roles | Restricted / Personal data; Art. 10 content possible | None | No | RoPA-AML-01; RoPA-CREDIT-01 | Triage per activity |
| DI-AML-01 — AML/KYC and screening system | Germany / Compliance, Fraud Prevention | Restricted / Personal data; criminal-offence data (Art. 10) | Screening-list provider (processor, EEA) | No | RoPA-AML-01 | DPIA performed (Document 21, RoPA-AML-01) |
| DI-CSV-01 — Customer-service system and message archive | Germany / PanEuropean agents (EEA) | Confidential / Personal data; may contain volunteered special-category content | None (link to DI-LLM-01 suspended) | No | RoPA-CSV-01; RoPA-LLM-01 | No DPIA for the human-only path (triage) |
| DI-LLM-01 — Customer-service assistant integration (masking gateway and API) | Germany (gateway) / importer's staff and US hosting sub-processor | Confidential / Personal data (masked message being handled and internal knowledge-base articles; no retrieval of customer records) | Example AI Provider Inc. (processor, USA) | Yes — TIA-LLM-01; G-TIA incomplete — HOLD; suspended under Clause 14(f) since 26 October 2026; no data sent | RoPA-LLM-01 | DPIA-LLM-01 — Medium; acceptance not in effect while the hold applies |
| DI-CLOUD-01 — Remote-support environment (privileged-access gateway with masking; tokenised logs and telemetry) | Germany / India (remote access by Example Cloud Services Pvt Ltd); EEA staff for break-glass | Confidential / Personal data; logs pseudonymised (tokens, keys held by PanEuropean in the EEA) | Example Cloud Services Pvt Ltd (processor, India) | Yes — TIA-CLOUD-01 (remote access by a separate entity) | RoPA-CLOUD-01 | No DPIA (triage); PRR-CLOUD-01 — Medium |
| DI-PSI-01 — Private set intersection node (PanEuropean side) | Germany / Fraud Prevention analysts | Restricted / Personal data; Art. 10 content (matches against the partner's list of identities linked to confirmed fraud) | Partner bank (independent controller, India) — receives only blinded, padded protocol messages; no match result, intersection size or other result-dependent signal | Yes — treated as a transfer; TIA-PSI-01 | RoPA-PSI-01 | DPIA-PSI-01 — High (re-assessed 26 October 2026; sessions paused) |
| DI-FL-01 — Federated-learning node and model-update exchange | Germany / Fraud Prevention data scientists; consortium aggregation service (EU) | Restricted / Personal data (local features: the customer's own transaction attributes; label: confirmed unauthorised transaction, customer as victim — no offence-attributing labels or counterparty data, so not category 4; DPIA-FL-01, G-L); model updates with differential privacy, through secure aggregation — the techniques do not change the legal status | Consortium members and aggregation service (joint controllers, EU) | No — intra-EU; General Counsel's conclusion (EVP-2026-0041); re-checked on membership change | RoPA-FL-01 | DPIA-FL-01 — Medium |
| DI-CMS-01 — Consent management system | Germany / IT Management; Privacy Operations | Internal / Personal data (consent records; biometric consent stored as a status only — no biometric data) | None; feeds marketing tools, the app, the CRM and PEP (permission flag) | No | RoPA-MKT-01; RoPA-OFFER-01; RoPA-PPI-01; RoPA-BIO-01 | Triage per activity |
| DI-MKT-02 — E-mail and push delivery service | EEA (provider) / provider's EEA staff | Confidential / Personal data (contact details, suppression list) | E-mail and push delivery service provider (processor, EEA) | No | RoPA-MKT-01 | No DPIA (triage) |
| DI-PEP-01 — The Bank's privacy engineering platform (PEP, illustrative) | Germany / Privacy Engineers; PEP support provider's EEA staff | Restricted / Personal data (source extracts during transformation) | PEP support provider (processor, EEA) | No | RoPA-CS-002; RoPA-FL-01; RoPA-PPI-01 | As for the activities served |
| DI-VID-01 — Branch video-surveillance recorders | Each branch country / branch security staff; security provider | Internal / Personal data | Branch security provider (processor, EEA) | No | RoPA-CCTV-01 | DPIA performed (Document 21, RoPA-CCTV-01) |

**Flow-map excerpt (external and remote-access links)**

| Link | From → to | Type | Data and frequency | Protection | Status |
| :---- | :---- | :---- | :---- | :---- | :---- |
| F-CLOUD-1 | DI-CLOUD-01 ← Example Cloud Services Pvt Ltd (India) | (c) remote access by an external entity | Masked support sessions; tokenised logs and telemetry; continuous | Privileged-access gateway in the EEA masking customer data; break-glass by EEA staff; tokenisation with keys in the EEA; session recording | Transfer — TIA-CLOUD-01; SCC Module 2 |
| F-PSI-1 | DI-PSI-01 → partner bank (India) | (b) disclosure to an independent controller | Blinded protocol messages derived from customer identifiers, padded to a fixed public bound; monthly session (paused since 26 October 2026 pending the prior consultation and the Chief Risk Officer's decision) | One-sided protocol — only PanEuropean learns the matches; length and timing independent of the number of matches; blinding key in the EEA | Treated as a transfer — TIA-PSI-01; SCC Module 1 |
| F-LLM-1 | DI-LLM-01 → Example AI Provider Inc. (USA) | (b) disclosure to a processor | Masked message being handled and knowledge-base articles | Masking; fail-closed special-category detector; exclusion of hardship, collections and complaints channels | Transfer — TIA-LLM-01; suspended since 26 October 2026 (no data sent) |
| F-FL-1 | DI-FL-01 → consortium aggregation service (EU) | (b) disclosure to joint controllers | Differentially private model updates per training round | Secure aggregation; noise added by PanEuropean before aggregation | Not a transfer — intra-EU (EVP-2026-0041) |
| F-CRED-1 | DI-CRED-01 ↔ EuroCredit Bureau (EEA) | (b) disclosure to an independent controller | Credit agreements and payment defaults; bureau information and scores; per application and monthly | Encrypted channel; data-sharing agreement | Not a transfer (EEA) |
| F-PAY-1 | DI-CORE-001 → payees' banks outside the EEA | (b) customer-instructed disclosure | Payment data per payment order | Payment-network security | Where a transfer: Art. 49(1)(b)/(c) on General Counsel's derogation record (Document 12) |
| F-STAFF-1 | PanEuropean staff abroad → Bank systems | (d) access by the organisation's own staff | As needed | CISO remote-access rules | Not a transfer (same legal entity) |

## **Fully Expanded Record — DI-CRM-014**

| Field | Value |
| :---- | :---- |
| "Contains Personal Data" Flag | Yes |
| Data Class and Data State | Confidential / Personal data (Document 10, Part B, Section 4.2: customer contact details, product holdings, service tickets, marketing preferences). Credit-scoring and AML data are not held in this system |
| Categories of Data Subjects and Data | Retail and SME customers and prospects (about 1.2 million customers, illustrative); identification and contact data, product holdings, service history, marketing preferences (consent status read from DI-CMS-01, not stored as the master) |
| Hosting Jurisdiction | Germany (PanEuropean data centre, Frankfurt am Main) |
| Access Jurisdictions | PanEuropean staff in the five EEA countries of presence (one legal entity); no access by external entities |
| External Recipients | None |
| Cross-Border Flow Flag | No |
| Transfer Reference | Not applicable |
| RoPA References | RoPA-CSV-01 (customer service), RoPA-MKT-01 (marketing selection), RoPA-OFFER-01 (personalised-offers pilot) |
| Date of Last DPIA | No DPIA: the triage records of the activities that use the system concluded that no DPIA was required (for the personalised-offers pilot, one WP248 criterion — Document 18, Example 4.1). Any new use of the profile — for example extending personalisation to transaction data — goes through G-DPIA before launch. The credit-scoring DPIAs do not cover this record: the credit-scoring datasets are DI-CS-0873, DI-CS-0874 and DI-CRED-01 |
| Residual Risk Tier | No residual-risk decision; the personalised-offers pilot was calculated Low (Document 18, Example 4.1) |
| Transformation Provenance and Lineage | Source record; no derived dataset descends from it at present |
| Reference to Evidence Pack | Not applicable (no formal decision on the record) |
| Retention and Erasure Propagation Route | Document 11 row "Account and contract data"; erasure on request executed in the CRM by IT Management within the request deadline; marketing suppression on the day of withdrawal (Document 13) |
| Date of the Record's Last Privacy Review | 20 October 2026; next review by 31 December 2027 (planned) |

## **Fully Expanded Record — DI-CLOUD-01**

| Field | Value |
| :---- | :---- |
| "Contains Personal Data" Flag | Yes |
| Data Class and Data State | Confidential / Personal data (as assessed in TIA-CLOUD-01, Document 20); identifiers in logs tokenised (pseudonymised), keys held only by PanEuropean in the EEA |
| Categories of Data Subjects and Data | Customers whose records appear in system telemetry, configuration and application logs (about 1.2 million customers, illustrative); free-text fields removed |
| Hosting Jurisdiction | Germany — the systems and logs are hosted in PanEuropean's EEA environment; the provider does not host customer data |
| Access Jurisdictions | India — remote administration by support engineers of Example Cloud Services Pvt Ltd through the masking gateway; EEA — break-glass access by the provider's EEA-based staff or PanEuropean staff, logged and approved per session |
| External Recipients | Example Cloud Services Pvt Ltd (fictional; processor; Art. 28 contract with SCC Module 2; vendor record under Document 17) |
| Cross-Border Flow Flag | Yes — remote access by a separate legal entity in a third country meets the three transfer criteria (Document 12, Section 2.1) |
| Transfer Reference | TIA-CLOUD-01 (G-TIA pass for the restricted design, 12 March 2026; EVP-2026-0008) |
| RoPA References | RoPA-CLOUD-01 |
| Date of Last DPIA | No DPIA: triage record — one WP248 criterion (large scale) |
| Residual Risk Tier | Medium — Document 18 calculation requested by Document 20, recorded as PRR-CLOUD-01; CIO decision 20 March 2026, expiry 20 March 2027 |
| Transformation Provenance and Lineage | Tokenised logs derived from application logs of the customer systems; tokenisation keys in the EEA |
| Reference to Evidence Pack | EVP-2026-0008 |
| Retention and Erasure Propagation Route | Document 11 row "Remote-support access logs" for the Bank-side access logs; provider-side copies deleted under the processing agreement with deletion confirmation |
| Date of the Record's Last Privacy Review | 12 March 2026 (with the TIA); next review by 12 March 2027 (planned) or on any TIA trigger |

## **Fully Expanded Record — DI-CS-0874**

| Field | Value |
| :---- | :---- |
| "Contains Personal Data" Flag | Yes |
| Data Class and Data State | Restricted / Personal data; state "synthetic" — no anonymity conclusion has been made, so the dataset keeps the category of its source (Document 10, Section 6.2; Document 11, Section 3.2) |
| Categories of Data Subjects and Data | Synthetic records modelled on applicants and customers in the source extract (about 1.2 million customers, illustrative); derived financial indicators, payment-history features, bureau-data features |
| Hosting Jurisdiction | Germany (PEP; Data Science workspace) |
| Access Jurisdictions | Data Science (PanEuropean staff, EEA) only |
| External Recipients | None; not published, not shared |
| Cross-Border Flow Flag | No |
| Transfer Reference | Not applicable |
| RoPA References | RoPA-CS-002 |
| Date of Last DPIA | DPIA-CS-TRAIN-01, 25 March 2026 |
| Residual Risk Tier | Medium — Document 18, Example 2.1-R; accepted with conditions by the Head of Credit Decisions (PRR-CS-TRAIN-01) |
| Transformation Provenance and Lineage | Differentially private generator, ε 1.8 at δ 1×10⁻⁹, privacy unit one customer (Document 10 attribute (iv)); set processed DI-CS-0873 (attribute (vi)), itself derived from DI-CORE-001 and DI-CRED-01; processing tool PEP synthetic-data pipeline version 2.3, run of 20 March 2026 (attribute (vii)) |
| Reference to Evidence Pack | EVP-2026-0012 |
| Retention and Erasure Propagation Route | Document 11 row "Synthetic calibration datasets (no anonymity conclusion)". Erasure route: contextual conclusion on the current dataset and generator by the Head of Credit Decisions within 5 business days, on Legal & Compliance's assessment with Group DPO advice; where erasure is required, immediate restriction and regeneration without the customer's data within 30 days (illustrative); the customer is excluded from every later run (Document 11, Part B, Section 3.5) |
| Date of the Record's Last Privacy Review | 25 March 2026; next review at the next calibration or by 25 March 2027 (planned) |

# **Normative Basis and References**

* Regulation (EU) 2016/679 (GDPR): Arts. 4(1), 4(5), 4(9), 5(1)(e), 5(2), 17, 18, 19, 26, 28, 30, 32, 35, 44–49; Recital 26.
* EDPB Guidelines 05/2021 on the interplay between the application of Article 3 and the provisions on international transfers as per Chapter V of the GDPR, version 2.0 (Section 2.2; Example 8.1 — employee remote access).
* EDPB Guidelines 01/2025 on pseudonymisation; EDPB Guidelines 02/2026 on anonymisation (public-consultation draft, July 2026 — not final).
* CJEU C-413/23 P *EDPS v SRB* (4 September 2025) — the recipient's means are part of the contextual analysis; the judgment does not decide generally that Chapter V stops applying whenever a recipient cannot attribute the data.
* NIST Privacy Framework 1.0 (January 2020), Identify-P — Inventory and Mapping (ID.IM-P) — crosswalk reference only.
* NIST SP 800-53 Rev. 5, controls CM-8, CM-12, CM-13 and PM-5(1) — bibliographic reference only.

# **International Adaptation**

> **Guidance.** The GDPR is the baseline. The applicability map for Canada is in Document 7, Section 3.1. This document does not claim compliance with any jurisdiction's law.

* **United Kingdom (headline).** The same inventory supports UK GDPR records and the UK transfer rules; record flows from the UK separately, because transfer tools and adequacy regulations differ (Document 12, International adaptation).
* **Switzerland (headline).** Record disclosures abroad under the revFADP separately from EU transfers; the Federal Council's list of adequate countries is the reference for flagging.
* **Canada — PIPEDA.** No statutory inventory, but the accountability principle (Schedule 1, Principle 4.1) and the OPC/OIPC guidance *Getting Accountability Right with a Privacy Management Program* expect a personal information inventory. Record transfers to third parties for processing, including outside Canada, so that the organisation can show contractual or other means of comparable protection (Principle 4.1.3) and inform individuals.
* **Canada — Québec (P-39.1).** Because the flag is defined by legal criteria, not by a fixed border, the organisation can add a "communication outside Québec" flag: before communicating personal information outside Québec, a privacy impact assessment is required and the communication is subject to a written agreement. The confidentiality-incident register is kept separately (Document 14).

# **Document History (PGF)**

| Release | Date | Changes |
| :---- | :---- | :---- |
| 1.0.0-rc.1 | 2026-10-26 | Canonical English Markdown; changes from internal ver.2: title block and structure per the editorial rules; translation residue removed (guillemets, duplicated title, hyphenated "privacy-" compounds); headings harmonised ("Relationship to Other Framework Documents", "Review and Amendment"); scope extended to datasets, derived datasets, unstructured repositories and AI artefacts, and to all categories of data subjects; privacy metadata extended (data state, categories of data subjects and data, access jurisdictions including remote access, external recipients with roles, transfer reference, RoPA references, lineage, retention and erasure propagation route); cross-border flag defined by the three cumulative criteria of EDPB Guidelines 05/2021 v2.0 (not intra-EEA flows as such, not geography alone; international organisations included; employee remote access is not a transfer, remote access by a separate entity is); four link types for flow maps; the former three-condition PET-scheme exclusion test and the DPO's role in it removed (transfer-status conclusion by Legal, DPO advice); synthetic generation no longer a ground for declassification (Document 11, Section 3.2); automated discovery; erasure propagation hooks (Document 11, Section 3.5: contextual conclusion on the current artefact, restriction and erasure by a deadline, no extension by batch runs, automatic expiry of short-period categories); single document owner (Data Governance) with the privacy overlay maintained by the EPPO; reviews decoupled from tool re-certification; Part B rebuilt: DI-CRM-014 consistent with the RoPA (Confidential customer profile, no DPIA, not the credit-scoring training record — the training data are DI-CS-0873 and DI-CS-0874, Restricted, DPIA-CS-TRAIN-01 Medium); DI-CLOUD-01 Confidential as in TIA-CLOUD-01, hosted in the EEA with remote access from India; residual tiers aligned with the Privacy Risk Register; real-vendor LLM record replaced by DI-LLM-01 (Example AI Provider Inc.; on hold, suspended); PSI with no output to the partner; federated-learning, data warehouse, document management, AML, customer-service, consent management, delivery-provider, PEP and video records added; flow-map excerpt added; example dates shifted by −12 months; normative basis and international adaptation added. Review correction: DI-PSI-01 marked with Art. 10 content and the DPIA-PSI-01 tier updated (High, 26 October 2026; sessions paused) |
