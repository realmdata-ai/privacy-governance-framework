---
title: "Privacy Risk Assessment Methodology"
document_id: PGF-18
level: 2
release_version: 1.0.0-rc.1
status: release-candidate
authors: ["Alexey Neyman", "Val Khvatov"]
regulatory_reference_date: 2026-10-26
licence_proposed: "CC BY 4.0 (proposed; subject to rights-holder confirmation)"
source_provenance: "Derived from internal source set ver.2: Level2/18. Privacy-Risk-Assessment-Methodology_ENG.docx.md; sha256 b3b5fed18bf6da0ff1baf401f73036dd50b10ab0d543928dc89202547fc49991"
---

# PGF-18 — Privacy Risk Assessment Methodology

*Privacy Governance Framework (PGF) · Level 2 — Policies and Standards · Release 1.0.0-rc.1 · Regulatory reference date: 26 October 2026*

> **Status and use.** Part A is a reusable template. Part B is a worked example for a fictional organisation (PanEuropean Bank AG); all names, figures, dates and records in Part B are illustrative. Nothing in this document is legal advice or a statement about any real organisation, product or provider.

# **About This Document**

**Purpose.** Document 18 is the calculation core of the PGF for privacy risk. It defines (a) how risk to the rights and freedoms of individuals is assessed as a set of harm scenarios, each with a likelihood and a severity; (b) a specialised PET Assessment Module for de-identified, synthetic, aggregate and federated releases; and (c) how organisational consequences are recorded on a separate track. It does not decide whether processing is lawful, and it does not decide who may accept a residual risk.

**Scope.** The method covers:

* the rights-and-freedoms risk assessment used inside a DPIA (Document 19) and for other processing that a PGF document sends here for a risk calculation;
* the PET Assessment Module, used whenever a de-identified, synthetic, aggregate or federated artefact is produced, shared or published, or whenever a controller wishes to support a conclusion that information is anonymous;
* the severity scale reused, without a likelihood axis, for the classification of privacy incidents (Document 14).

The method does **not** replace the legal assessment of a transfer under the mechanism used (adequacy scope and validity under Art. 45; for Art. 46 safeguards, the laws and practices of the destination and supplementary measures; the conditions of an Art. 49 derogation — Document 20), vendor due diligence (Document 17), the legal compliance gate (G-L) or the statutory breach-notification tests (Document 14). Those documents may call the calculation core for a specific element (for example, the severity of harm if transferred data were disclosed), and only to that extent.

**Relationships.** Document 8 (Privacy Risk Appetite Statement) owns the tier scales, the residual-risk matrix and the acceptance authority. Document 19 (DPIA Methodology and Template) and Document 20 (Transfer Impact Assessment Methodology) apply this calculation core. Documents 11, 12, 16 and 17 use the PET Assessment Module as evidence for their own decisions. Results are recorded in the Privacy Risk Register (Document 22) and the RoPA (Document 21). The full list is in Section 6.

# **How to Use This Document**

Part A is a template for drafting the methodology. Text in ***[square brackets, bold italic]*** is a fillable or illustrative placeholder. Blocks marked **Guidance** explain what should go into a section and are removed from the organisation's adopted version.

Part B shows the same structure filled in for the fictional PanEuropean Bank AG, with four Risk Calculation Projects and numerical examples in the Appendix to Part B. The subsections of the projects are labelled 4.A–4.D (Projects 1–4). These labels are unrelated to the severity factors A–G of Section 3.4.

> **Guidance.** Read this document together with Document 8. Document 8 is the single source of the tier scales, the residual-risk matrix and the acceptance authority; this document calibrates what Document 8 deliberately does not establish — the factors, scores, metrics, thresholds and weights of the calculation. If Document 8 has not yet been adopted, start with it.

Three rules apply throughout the document:

1. **Lawfulness first.** The legal compliance gate (G-L) runs before any risk decision. A G-L failure means stop or redesign; no score, tier, appetite, metric or DPO opinion can cure it (Section 2.1).
2. **Two tracks, never offset.** Track (a) — risk to the rights and freedoms of individuals — informs DPIA conclusions, the prior-consultation test and acceptance. Track (b) — organisational consequences (regulatory, financial, reputational, operational) — is recorded separately and never lowers track (a).
3. **Numbers are evidence, not a legal safe harbour.** ε, δ, k, l, t, attack success rates or any other metric — and any DPO opinion — do not by themselves establish anonymity or lawfulness (Section 3.3.0).

# **Table of Contents**

**About This Document**
**How to Use This Document**
**Part A — Template**
Glossary of Terms
1. Purpose
2. Scope
2.1 Position in the Decision Sequence: Gates
3. Catalogue of Metrics and Factors for Privacy Risk Assessment
3.1 Architecture of the Methodology
3.2 Likelihood — Threat-Based Model and Base-Dataset Diagnostics
3.3 PET Assessment Module
3.3.0 Module Rules (Legal Status, Failure Gates, Normalisation, Uncertainty)
3.3.1 De-identification of Records ("Anonymisation Techniques")
3.3.2 Data Synthesis
3.3.3 Federated Learning / Joint Computation Without Data Centralisation
3.3.4 Aggregate Statistics and Tabular Releases
3.3.5 Differential Privacy Statements
3.3.6 Repeated Releases and Cumulative Disclosure
3.4 Severity Assessment Factors (Track (a)) and Organisational Consequences (Track (b))
Factor A — Harm Type (mandatory tag, not included in the sum)
Factor B — Intensity per Data Subject
Factor C — Scale
Factor D — Reach / Containment
Factor E — Automated Decision-Making with a Significant Effect
Factor F — Organisational Consequences (Track (b), not part of the severity index)
Factor G — Data Provenance and Reasonable Expectations
3.5 Other Metrics (Data Quality and Utility)
4. Privacy Risk Calculation Project
4.1 Purpose and Characteristics of the Project
4.2 Likelihood
4.3 Severity
4.4 Final Residual Risk Level and Decision Steps
4.5 Traceability of the Calculation and Evidence Pack
4.6 Other Metrics of PET Application
5. Roles and Responsibilities
6. Relationship to Other Framework Documents
7. Review and Amendment
8. Approval
**Part B — Worked Example: PanEuropean Bank AG**
Glossary of Terms
1. Purpose
2. Scope
3. Catalogue of Metrics and Factors (PanEuropean)
3.1 Architecture of the Methodology
3.2 Likelihood — Threat-Based Model and Base-Dataset Diagnostics
3.3 PET Assessment Module (3.3.0–3.3.6)
3.4 Severity Assessment Factors and Organisational Consequences
3.5 Other Metrics (Data Quality and Utility)
4. Privacy Risk Calculation Projects
Project 1 — Base Dataset Assessment (Sections 4.A.1–4.A.6)
Project 2 — Synthetic Dataset for Model Calibration (Sections 4.B.1–4.B.6)
Project 3 — Aggregate Statistics for the Bank's Open Data Portal (Sections 4.C.1–4.C.6)
Project 4 — Processing of Identified Data Without a De-identification Plan (Sections 4.D.1–4.D.6)
5. Roles and Responsibilities
6. Relationship to Other Framework Documents
7. Review and Amendment
8. Approval
**Appendix to Part B — Numerical Examples of Risk Calculation Projects**
Project 1 — Examples 1.1, 1.2
Project 2 — Examples 2.1, 2.1-R, 2.2
Project 3 — Examples 3.1, 3.2, 3.3 (blocked case)
Project 4 — Examples 4.1, 4.2 (and 4.2-R), 4.3
**Normative Basis and References**
**International Adaptation**
**Document History (PGF)**

# **Part A — Template**

**Privacy Risk Assessment Methodology *[Legal Name of the Organisation]***

*Effective Date: **[DD Month YYYY]**  ·  Version: **[x.x]**  ·  Document Owner: **[Executive Privacy Programme Owner (EPPO)]**  ·  Adopted by: **[Executive Management]***

# **Version History**

| Version | Date | Changes |
| :---- | :---- | :---- |
| ***[1.0]*** | ***[DD.MM.YYYY]*** | ***[Initial version of the document]*** |
| ***[x.x]*** | ***[DD.MM.YYYY]*** | ***[Brief description of material changes]*** |

## **Glossary of Terms**

*This table lists only terms defined by this document itself; terms defined in another PGF document are not repeated here.*

| Term | Definition / Reference |
| :---- | :---- |
| Risk Calculation Project | A versioned, case-specific configuration of the methodology: archetype, harm scenarios, likelihood factors, PET-module metrics and thresholds, severity scores, weights and failure gates. Structure — Section 4. |
| Harm scenario | A combination of a threat source, a problematic data action or event, and the harm type that would result for individuals (Factor A). Every Risk Calculation Project assesses at least one scenario per relevant harm type. |
| Track (a) — rights and freedoms | The assessment of likelihood and severity of harm to individuals. It informs DPIA conclusions, the G-36 prior-consultation test (as an indicator; the legal conclusion is separate) and risk acceptance (Document 8). |
| Track (b) — organisational consequences | Regulatory, financial, reputational and operational consequences for the organisation (Factor F). Recorded separately; never offsets track (a). |
| Pseudonymisation | Processing such that personal data can no longer be attributed to a specific data subject without the use of additional information kept separately and protected (GDPR Art. 4(5)). Pseudonymised data remain personal data for anyone who can attribute them with means reasonably likely to be used. Pseudonymisation is a security and data-minimisation measure, **not** an anonymisation technique (EDPB Guidelines 01/2025). |
| De-identification techniques | Transformations that reduce identifiability: generalisation, suppression, aggregation, noise addition, sampling, synthesis and similar. Applying a technique does not by itself change the legal status of the data. Structure — Section 3.3.1. |
| Anonymous information | A contextual legal conclusion under GDPR Recital 26 that information no longer relates to an identified or identifiable person, taking into account all the means reasonably likely to be used by the controller or by any other person. It is made by the controller on documented evidence (including PET Assessment Module results) and re-assessed periodically. Section 3.3.0. |
| Data Synthesis | The generation of an artificial dataset from a model trained on source data. Synthesis is a generation method, not a legal status: synthetic data can disclose information about the people in the source data. Structure — Section 3.3.2. |
| Federated Learning | Training of a model on data distributed across participants, where only derived artefacts (for example, parameter updates) leave each participant. A processing architecture; it does not by itself change the legal status of the data or of the artefacts. Structure — Section 3.3.3. |
| SMPC | Secure Multi-Party Computation — participants compute a function over combined inputs while exchanging only encrypted or secret-shared fragments. A processing architecture, addressed in Section 3.3.3. |
| PET Assessment Module | The specialised assessment applied to de-identified, synthetic, aggregate and federated artefacts: individual metric results, failure gates and a disclosure indicator. Section 3.3. |
| Failure gate | A condition that fails the PET Assessment Module (or makes it INCOMPLETE) regardless of any average: a mandatory metric outside its threshold, an unmitigated feasible disclosure path defined by the project, a prohibited attribute, a DP ledger overrun, or a missing or invalid result. Section 3.3.0. |
| Disclosure indicator | The weighted average of normalised metric results within the PET Assessment Module. An uncalibrated ordinal summary; it is **not** a probability. Section 3.3.0. |
| Privacy unit | In differential privacy, the entity whose contribution the guarantee protects (for example, one record, or all records of one customer). Section 3.3.5. |

## **1. Purpose**

This document defines the methodology for assessing privacy risk: the harm scenarios that must be considered, how the likelihood and the severity of each scenario are assessed, how the PET Assessment Module evaluates de-identified and synthetic artefacts, and how the results are combined into a residual-risk tier on the Document 8 scale. It is the calculation core used by the DPIA (Document 19) and, to the extent stated in Section 2, by other PGF processes.

This document does not decide on the lawfulness or permissibility of processing (that is the legal compliance gate, G-L, owned by ***[Legal]***), and it does not determine who may accept a risk of a given tier (that is Document 8, Section 5).

## **2. Scope**

* ***[This document applies to any processing of personal data for which another PGF document requires a risk assessment. It does not initiate an assessment on its own; it is invoked from the DPIA Methodology (Document 19), from the incident classification of Document 14 (severity only), and from documents that require evidence on a de-identified, synthetic, aggregate or federated artefact (for example, Documents 11, 12, 16 and 17).]***

* ***[For a transfer impact assessment (Document 20) and for vendor due diligence (Document 17), this document supplies only the calculation elements those documents expressly request (for example, the severity of harm if the transferred data were disclosed, or PET-module evidence on a de-identified artefact). The legal transfer assessment under the mechanism used (Art. 45, 46 or 49) — including, for Art. 46 safeguards, the destination's laws and practices and the effectiveness of supplementary measures — and the decision whether a transfer may start remain with Document 20 and cannot be replaced by a score or by risk appetite.]***

* ***[The assessment of likelihood and the assessment of severity (Section 3) are independent tracks within each harm scenario. They are combined only at the final mapping through the Document 8 matrix (Section 4.4).]***

* ***[The methodology applies to structured data. Unstructured data (text, images, audio) and large language models are not covered by the PET Assessment Module in this version; for them, the threat-based likelihood model (Section 3.2) and the severity factors (Section 3.4) apply, and the absence of a validated disclosure test is recorded as a limitation.]***

## **2.1 Position in the Decision Sequence: Gates**

Every calculation under this document sits inside the following sequence. The gates have identical wording across Documents 5, 8, 12, 14, 16, 18, 19, 20, 22, 24 and 31.

| Order | Gate / step | What happens | Owner |
| :---- | :---- | :---- | :---- |
| 1 | **G-L — Legal compliance gate** | Runs **before** any risk decision. Checks: lawful basis (Art. 6); condition for special-category data (Art. 9) or criminal-offence data (Art. 10); purpose compatibility (Art. 6(4)); transparency deliverable (Arts. 13/14); Art. 22 permissibility and safeguards; valid transfer tool and TIA outcome (Chapter V); mandatory deadlines and statutory duties. **Failure means stop or redesign.** No risk appetite, risk acceptance, DPO opinion or metric can cure a G-L failure. | ***[Legal]*** |
| 2 | **G-DPIA — DPIA triage** | Triggers: Art. 35(1); the Art. 35(3) cases; the supervisory authority lists under Art. 35(4); the nine WP248 rev.01 criteria (two or more → presumption that a DPIA is required). DPO advice is required on **every** DPIA (Art. 35(2)), whatever the score. | ***[Processing Owner; Document 19]*** |
| 3 | Calculation (this document) | Harm scenarios; likelihood (Section 3.2 or the PET Assessment Module, Section 3.3); severity (Section 3.4); residual tier per scenario through the Document 8 matrix; track (b) recorded separately. | ***[Privacy Operations Lead]*** |
| 4 | **G-36 — Prior consultation** | **Evaluated for every DPIA.** A statutory test, independent of internal tiers: if the DPIA indicates that processing would still result in a high risk to the rights and freedoms of natural persons in the absence of further mitigating measures, the controller consults the competent supervisory authority **before processing starts** (Art. 36(1)), irrespective of the internal tier. A residual **High** or **Critical** tier on track (a) is a strong indicator that the test is met; the legal conclusion is recorded separately, with reasons. Under Art. 36(2) the supervisory authority may give written advice within the statutory period (which may be extended), request information (which suspends the period), and use its Art. 58 powers, including a temporary or definitive limitation or ban. An elapsed period, or the absence of supervisory-authority comments, is **not** an authorisation or a certificate of lawfulness; G-L remains in force and the controller remains responsible. | ***[Legal records the conclusion, with DPO advice; the decision record names the effective decider under Document 8]*** |
| 5 | Risk acceptance | By the single decider designated under the delegation in Document 8, Section 5, for the residual tier; DPO advice recorded. Critical is not acceptable. | ***[One named decider per Document 8]*** |

For transfers, **G-TIA** (Document 20) applies in addition, branched by transfer mechanism:

* **Art. 45 adequacy** — check that the adequacy decision covers the destination, sector and recipient (scope and eligibility, for example the recipient's certification under the EU-U.S. Data Privacy Framework), that it remains valid, and monitor it. There is no statutory obligation to redo the Commission's assessment; any stricter internal review is labelled as internal policy.
* **Art. 46 appropriate safeguards** (for example standard contractual clauses or binding corporate rules) — a transfer impact assessment of the laws and practices of the destination (public-authority access, enforceable rights and redress), supplementary measures and re-evaluation (CJEU C-311/18; EDPB Recommendations 01/2020, version 2.0, Step 2 and following). If essentially equivalent protection cannot be ensured, the transfer does not start or is suspended; risk appetite cannot override this.
* **Art. 49 derogations** — exceptional and interpreted restrictively; the specific conditions are documented.

G-L and DPIA duties apply under every mechanism. PETs, trusted execution environments, homomorphic encryption and remote access are not automatic exemptions from Chapter V (EDPB Guidelines 05/2021). A DPIA and Art. 36 may be needed in parallel with a TIA.

> **Guidance.** The calculation in this document is meaningful only for processing that has passed G-L, or for a redesign being assessed before G-L is re-run. Where a calculation is performed on an as-found situation that failed G-L (for example, to classify an incident or to size a remediation), the evidence pack states "G-L failed — not available for acceptance" and no acceptance decision is recorded.

## **3. Catalogue of Metrics and Factors for Privacy Risk Assessment**

> **Guidance.** This section is the single catalogue of likelihood factors, PET-module metrics and severity factors from which Risk Calculation Projects (Section 4) draw. It does not itself produce a tier; the integration (scenarios, weights, thresholds, gates) is the subject of Section 4.

## **3.1 Architecture of the Methodology**

* ***[Two tracks. Track (a) assesses risk to the rights and freedoms of individuals. Track (b) records organisational consequences (Factor F). Track (b) never lowers, offsets or averages track (a).]***

* ***[Harm scenarios. Track (a) is assessed per harm scenario. Each Risk Calculation Project considers, as a minimum, whether each of the following harm types is relevant and, where relevant, assesses at least one scenario for it (Factor A): (1) unlawful processing or loss of control over one's data; (2) discrimination or adverse automated decisions; (3) financial loss; (4) identity fraud; (5) reputational and social harm; (6) physical or psychological harm, chilling effects and exclusion; (7) loss of confidentiality, integrity or availability. Re-identification is one threat source among others, not the definition of risk.]***

* ***[Likelihood. For processing of identified or identifiable data — including pseudonymised data — the likelihood of each scenario comes from threat sources, exposure, control effectiveness and event history (Section 3.2), in the spirit of NISTIR 8062 and the CNIL PIA method. Re-identification metrics are not used as the likelihood of harm from identified processing.]***

* ***[PET Assessment Module. For a de-identified, synthetic, aggregate or federated artefact, the likelihood of the disclosure scenario (singling out, linkability, inference, membership disclosure, reconstruction) is assessed through the PET Assessment Module (Section 3.3), which keeps individual metric results and applies failure gates. Other scenarios concerning the same processing (for example, insider misuse of the source data) still use Section 3.2.]***

* ***[Severity. Severity (Section 3.4) is determined by the nature, scope and context of the harm scenario; it does not depend on the PET technology applied. Controls and PETs act on likelihood, not on severity, unless a measure demonstrably limits the consequences themselves (documented in the scenario).]***

* ***[Unit of application. The practical unit is the Risk Calculation Project (Section 4): a configuration for a business case with a distinct risk profile. The organisation maintains as many projects as it has such cases.]***

* ***[Archetypes. A Risk Calculation Project is built around one of the following archetypes, which determine which parts of the catalogue apply.]***

| Archetype | Definition | Applicable Sections of the Methodology |
| :---- | :---- | :---- |
| ***[1]*** | ***[Base dataset — identified or pseudonymised data before a decision on a PET, or where no PET is planned for the dataset as such]*** | ***[3.2 (threat-based likelihood); base-dataset disclosure diagnostics (3.2, last part) as an input to PET planning; 3.4]*** |
| ***[2]*** | ***[De-identified release — record-level de-identification (2a) or aggregate/tabular statistics (2b) intended to be shared or published, including where the controller wishes to support a conclusion that the output is anonymous information. Pseudonymised data are **not** archetype 2; they are archetype 1 or 4.]*** | ***[3.3.0, 3.3.1 (2a) or 3.3.4 (2b), 3.3.5–3.3.6 where DP is used, 3.4]*** |
| ***[3]*** | ***[Synthetic data or federated/joint computation — the derived artefact (synthetic dataset, model update, secret-shared fragment, intersection result) crosses a boundary of access]*** | ***[3.3.0, 3.3.2 / 3.3.3, 3.3.5–3.3.6, 3.4]*** |
| ***[4]*** | ***[Identified processing — the data are identified or identifiable and remain so as the intended, permanent state of the processing, on a lawful basis confirmed by G-L]*** | ***[3.2 (threat-based likelihood); 3.4 in full]*** |
| ***[5]*** | ***[Name and definition of an additional archetype — completed if necessary]*** | ***[Applicable sections]*** |

> **Guidance.** The archetype is declared in the project passport (Section 4.1) and may not be changed without a revision of the project's configuration. For archetype 4, a reference to the G-L record confirming the lawful basis is mandatory; without it the calculation cannot be completed. No archetype fixes likelihood at a constant: likelihood is always assessed per scenario.

## **3.2 Likelihood — Threat-Based Model and Base-Dataset Diagnostics**

> **Guidance.** This subsection is the likelihood model for every harm scenario concerning identified or identifiable data (archetypes 1 and 4, and the non-disclosure scenarios of archetypes 2 and 3). It follows the logic of NISTIR 8062 (likelihood that a data action is problematic for individuals) and of the CNIL PIA method (risk sources, their capabilities, and the vulnerabilities of supporting assets). Scores are ordinal: they support a structured, reviewable judgement and are not probabilities.

***[For each harm scenario, the likelihood index is the sum of four factors, each assessed on documented evidence. Measures are taken into account through factor L3 only where their implementation is evidenced, not merely declared.]***

| Likelihood factor | 0 | 1 | 2 | 3 |
| :---- | :---- | :---- | :---- | :---- |
| ***[L1 — Exposure: how often and how broadly the data action occurs, or how broadly the data are accessible]*** | ***[Rare or one-off; machine-only or isolated environment]*** | ***[Periodic; restricted to named roles]*** | ***[Routine; broad internal access or access by a partner/processor]*** | ***[Continuous or systematic for the whole affected population; or public access]*** |
| ***[L2 — Threat source: capability and motivation of the relevant risk source, deliberate or accidental]*** | ***[No realistic source identified]*** | ***[Accidental only, or low capability]*** | ***[Opportunistic insider or partner; known error modes of a model or process]*** | ***[Motivated, capable attacker (e.g. organised fraud); or a known systematic error mode, e.g. proxy variables for protected characteristics]*** |
| ***[L3 — Control effectiveness gap: residual weakness after implemented measures]*** | ***[Measures implemented and tested, evidence in the evidence pack]*** | ***[Implemented, partially tested]*** | ***[Implemented but untested, or known weaknesses / open non-conformities]*** | ***[Absent or ineffective]*** |
| ***[L4 — Event history]*** | ***[No relevant events known]*** | ***[Events in comparable processing in the sector]*** | ***[Events or near misses in the organisation's own processing within the last [24] months]*** | ***—*** |

| Likelihood index (L1+L2+L3+L4) | Likelihood level (Document 8 scale) |
| :---- | :---- |
| ***[0 – 3]*** | ***[Low]*** |
| ***[4 – 6]*** | ***[Medium]*** |
| ***[7 – 8]*** | ***[High]*** |
| ***[9 – 11]*** | ***[Near-certain]*** |

***[The likelihood index is always an integer (a sum of integer factor scores); no weights apply to it.]***

* ***[Override rule: where a control is absent or ineffective (L3 = 3) against a capable or systematic threat source (L2 ≥ 2), the likelihood level is at least High, whatever the index.]***

* ***[Inherent and residual likelihood: the project records the inherent likelihood (L3 assessed as 3, i.e. without measures) and the residual likelihood (L3 as evidenced). The inherent value informs DPIA triage and the choice of measures; the residual value is used for the residual tier.]***

* ***[Consent, contract or any other legal basis does not reduce likelihood or severity. Lawfulness is checked by G-L; transparency quality is reflected in Factor G only as a matter of reasonable expectations.]***

* ***[Typical controls considered under L3: access control and segregation ("white room" or machine-only access), logging and monitoring, encryption and key management, the contractual and factual control instrument with a recipient (Art. 28 data processing agreement, Art. 26 arrangement or data-sharing agreement, with the due-diligence status under Document 17), a tested incident-response plan for the processing (Document 14), human review and contestation for automated decisions (Art. 22(3)), bias testing and model monitoring.]***

**Base-dataset disclosure diagnostics (archetype 1 only).** ***[Before a PET is chosen, the organisation may compute disclosure metrics on the quasi-identifier view of the base dataset (direct identifiers removed): re-identification proxy metrics (k-anonymity, l-diversity, t-closeness, uniqueness rate) and the attack battery of Section 3.3.1. The results describe how identifiable the data would remain if released without further transformation. They are an input to PET planning and to the choice of a Risk Calculation Project for the release; they are **not** the likelihood of any harm scenario concerning the base dataset itself, which is assessed with the threat-based model above.]***

## **3.3 PET Assessment Module**

> **Guidance.** The PET Assessment Module is a specialised module, not a universal DPIA or TIA formula. It applies whenever a de-identified, synthetic, aggregate or federated artefact crosses a boundary of access (sharing, publication, transfer, use by a wider group) and whenever the controller wishes to support a conclusion that information is anonymous. It provides evidence for the likelihood of the disclosure scenario only.

### **3.3.0 Module Rules (Legal Status, Failure Gates, Normalisation, Uncertainty)**

**Legal status.** ***[Results of this module are evidence, not a legal safe harbour. Meeting any threshold for ε, δ, k, l, t, uniqueness, attack success or any other metric — or a favourable DPO opinion — does not by itself establish that information is anonymous or that processing is lawful. Whether information is anonymous is a contextual legal conclusion under GDPR Recital 26, made by the controller: it considers all the means reasonably likely to be used, by the controller or by any other person, to identify a person directly or indirectly, taking into account the costs and time required, the available technology and its development. Identifiability is assessed relative to the recipient and its realistic means (CJEU C-582/14 *Breyer*; CJEU C-413/23 P *EDPS v SRB*); for an open publication, the recipient is anyone. Pseudonymised data remain personal data for whoever can attribute them (Art. 4(5); EDPB Guidelines 01/2025 on pseudonymisation). The EDPB Guidelines 02/2026 on anonymisation were published as a public-consultation draft (8 July 2026); they are not final and are used as orientation only. The three criteria of singling out, linkability and inference are those of Article 29 Working Party Opinion 05/2014 on Anonymisation Techniques (WP216).]***

**Periodic re-assessment.** ***[A conclusion that a released artefact is anonymous is re-assessed at least [annually] and whenever new auxiliary data, a new published attack, a new release from the same source population (Section 3.3.6) or a change of recipient becomes known. For open releases that cannot be withdrawn, the re-assessment also considers whether further releases must be stopped.]***

**Per-metric results.** ***[Every metric selected for the project is reported individually, with its threshold, its normalised value and whether it passed. A composite never replaces the individual results.]***

**Failure gates.** ***[The module FAILS, regardless of the disclosure indicator, if any of the following applies:]***

* ***[G-M1 — a mandatory metric is outside its threshold, applying the uncertainty rule below;]***
* ***[G-M2 — an unmitigated feasible disclosure path. For each attack in the project's attack set, the project passport states its scope (records, population and auxiliary data assumed), the baseline against which success is measured (for example chance level, or success on a control set of records that were not in the source data), the unacceptable-success level and the uncertainty rule. G-M2 fails where an attack's success exceeds its unacceptable level after the uncertainty rule is applied, or where a qualitative path that the project defines as unacceptable regardless of rate is found (for example, an exact copy of a source record in a synthetic release, or a published cell that attributes a sensitive value to an identifiable person). Success at or near the baseline, or below the unacceptable level once uncertainty is taken into account, does not fail G-M2; it is reported as observed success. Where an attack is also a weighted metric, its unacceptable level is the metric threshold (G-M1 and G-M2 then coincide). Attacks documented in the literature for the technique and parameters used are included in the attack set or their exclusion is justified;]***
* ***[G-M3 — the artefact contains an attribute that the project prohibits for the intended recipient. Two different grounds are distinguished: (a) the release would disclose identifiable special-category data without an applicable Art. 9(2) condition — this is also a G-L failure; (b) the organisation's internal policy excludes an attribute from a type of release (for example, no health-related attribute in open releases) — labelled as internal policy, stricter than the legal test. An attribute contained in information that is effectively anonymous under Recital 26 is not, as such, special-category personal data; whether the release is anonymous is the question that the module and the legal assessment answer;]***
* ***[G-M4 — for differential privacy: the DP statement of Section 3.3.5 is incomplete, or the lifetime cumulative ledger or an operational cap for the source population (Section 3.3.6) would be exceeded;]***
* ***[G-M5 — a mandatory metric or test is missing, invalid (outside its allowed domain or computed on a configuration that fails the domain rules below) or not assessed. A missing or invalid result never defaults to a passing value: the module outcome is INCOMPLETE, which blocks release in the same way as FAIL.]***

***[A failed or incomplete module means that the artefact may not be released, shared or treated as anonymous in its current form. For a FAIL, the as-proposed likelihood of the disclosure scenario is recorded as High. Conservative internal routing rule: where a G-M1 or G-M2 failure has been reproduced — it persists in every repetition and the whole confidence interval lies beyond the threshold — the as-proposed likelihood is recorded as Near-certain. This is an internal routing convention for evidence and incident classification; it does not mean that disclosure is near-certain for every person. The observed success (for example accuracy, true-positive rate at a low false-positive rate, share of records reconstructed) is always reported next to it. These values are not available for acceptance.]***

**Normalisation.** ***[Each weighted metric is normalised so that 0 corresponds to the no-disclosure baseline and 1 to the project threshold. Allowed domains and orientation:]***

| Metric type | Allowed domain and configuration | Normalised value |
| :---- | :---- | :---- |
| ***[Rate with a zero baseline (singling-out rate, linkage success, share of records reconstructed) — lower is safer]*** | ***[Value in [0, 1]; threshold in (0, 1]]*** | ***[value / threshold]*** |
| ***[Signed advantage with a zero baseline (inference advantage, CAP advantage, information gain expressed as an advantage) — lower is safer]*** | ***[Value in [−1, 1]; threshold in (0, 1]. A negative advantage (attack worse than its baseline) is recorded as observed; the gate and the indicator use the effective value max(0, value)]*** | ***[max(0, value) / threshold]*** |
| ***[Accuracy of a balanced membership test (baseline 0.5)]*** | ***[Accuracy in [0, 1]; threshold in (0.5, 1]. Orientation-invariant: an attack performing below chance can be inverted, so the gate and the indicator both use the effective accuracy 0.5 + \|accuracy − 0.5\|]*** | ***[advantage = 2 × \|accuracy − 0.5\|; normalised = \|accuracy − 0.5\| / (threshold − 0.5)]*** |
| ***[AUC-ROC (baseline 0.5)]*** | ***[AUC in [0, 1]; threshold in (0.5, 1]; the gate and the indicator both use the effective AUC 0.5 + \|AUC − 0.5\|]*** | ***[\|AUC − 0.5\| / (threshold − 0.5)]*** |
| ***[Bounded similarity ratio where 1 means no disclosure (e.g. NNDR) — higher is safer]*** | ***[Value in [0, 1]; threshold in [0, 1)]*** | ***[(1 − value) / (1 − threshold)]*** |
| ***[Unbounded distance where larger is safer (e.g. DCR percentile) — higher is safer]*** | ***[Value ≥ 0; threshold > 0, set from the holdout baseline. A value of 0 (an exact copy of a source record) is an unacceptable qualitative path under G-M2 and is not normalised]*** | ***[threshold / value]*** |
| ***[Formal DP parameters (ε, δ)]*** | ***[ε ≥ 0; 0 ≤ δ < 1]*** | ***[Not normalised and not averaged; checked as configuration gates (G-M1/G-M4) and documented in the DP statement (Section 3.3.5)]*** |

***[A threshold equal to the baseline, or on the wrong side of it (for example an accuracy threshold of 0.5 or less), makes the configuration invalid; the module is then INCOMPLETE (G-M5). A value outside its allowed domain is an invalid result (G-M5). Each threshold states whether it is inclusive. Unless the project passport states otherwise, thresholds of lower-is-safer metrics are exclusive upper limits (the metric passes only if its unfavourable bound is strictly below the threshold) and thresholds of higher-is-safer metrics are exclusive lower limits (it passes only if its unfavourable bound is strictly above the threshold); a value exactly at an exclusive threshold fails.]***

***[Weights are non-negative and sum to 1 over the weighted metrics. Gate-only and diagnostic metrics have no weight and are outside the indicator.]***

***[Membership-inference tests are run on a balanced set of members and non-members; the organisation also reports the true-positive rate at a low false-positive rate (for example, at FPR = 0.1%), because average accuracy or AUC can hide a small group of highly exposed records.]***

**Disclosure indicator.** ***[Disclosure indicator = Σ (normalised value × weight) over the weighted metrics. It is an uncalibrated ordinal summary for comparison between runs and is **not** a probability. It is translated into a likelihood level only for a module that has passed all gates. Because every weighted metric of a passing module has a normalised value of at most 1 and the weights sum to 1, the indicator of a passing module lies between 0 and 1; an indicator above 1 can arise only when a metric has failed, and the outcome is then FAIL.]***

| Module outcome | Likelihood level of the disclosure scenario |
| :---- | :---- |
| ***[PASS, indicator < 0.5]*** | ***[Low]*** |
| ***[PASS, 0.5 ≤ indicator ≤ 1.0]*** | ***[Medium]*** |
| ***[INCOMPLETE (G-M5)]*** | ***[Not assessed — release blocked; no likelihood level is assigned]*** |
| ***[FAIL (any gate)]*** | ***[High (as-proposed; not available for acceptance)]*** |
| ***[FAIL reproduced (internal routing rule above)]*** | ***[Near-certain (as-proposed; internal routing convention; observed success reported separately; not available for acceptance)]*** |

**Uncertainty.** ***[Attack metrics are estimates. The evidence pack records, for each attack metric, the evaluation sample size, the number of repetitions and a 95% confidence interval. The gate uses the unfavourable bound: the upper bound for a lower-is-safer metric, the lower bound for a higher-is-safer metric. For accuracy and AUC the unfavourable bound is orientation-invariant: it is the larger effective value over both ends of the interval, max(0.5 + \|lower − 0.5\|, 0.5 + \|upper − 0.5\|), so that an interval lying below chance, or crossing 0.5, is evaluated as strictly as one above it. For signed advantages the unfavourable bound is max(0, upper bound). Where that bound crosses the threshold while the point estimate does not, the metric fails unless the test is repeated with a larger sample. The disclosure indicator uses effective point estimates.]***

***[Interval methods. Binomial proportions (accuracy of a balanced test, hit rates, singling-out and linkage rates, precision at k, share of records reconstructed) use Wilson score intervals. AUC, advantages, information-gain measures and distance-based metrics use bootstrap percentile intervals; the passport states the resampling unit (record or person) and the number of resamples. "Repetitions" are independent re-runs of the attack with fresh random seeds and, where applicable, fresh member/non-member splits; the evidence pack reports the spread across repetitions as well as the interval. Where an example in this document is illustrative, interval bounds may be stated as assumptions; they must then be labelled as such and never presented as computed from real observations.]***

***[Boundary check (accuracy threshold exclusive, < 0.60):]***

| ***[Observed accuracy or interval]*** | ***[Effective unfavourable value]*** | ***[Gate]*** |
| :---- | :---- | :---- |
| ***[0.50]*** | ***[0.50]*** | ***[pass]*** |
| ***[0.40]*** | ***[0.60 (inverted)]*** | ***[fail — exactly at the exclusive threshold]*** |
| ***[0.60]*** | ***[0.60]*** | ***[fail — exactly at the exclusive threshold]*** |
| ***[0.10, interval [0.09, 0.11]]*** | ***[0.91]*** | ***[fail — an inverted attack is near-perfect]*** |
| ***[0.90]*** | ***[0.90]*** | ***[fail]*** |
| ***[0.52, interval [0.45, 0.58] (crosses 0.5)]*** | ***[max(0.55, 0.58) = 0.58]*** | ***[pass]*** |
| ***[0.45, interval [0.38, 0.52] (crosses 0.5)]*** | ***[max(0.62, 0.52) = 0.62]*** | ***[fail]*** |

**Default thresholds.** ***[The default thresholds in Part B are organisation-set illustrative values calibrated for a stated adversary profile and disclosure channel. They are not derived from a normative source. Releases to a broad or unlimited audience normally require stricter, context-based values; ISO/IEC 27559 and NIST SP 800-188 describe context-based approaches.]***

### **3.3.1 De-identification of Records ("Anonymisation Techniques")**

***[Applies to record-level outputs of generalisation, suppression, sampling, noise addition or similar techniques (archetype 2a). Pseudonymisation is not covered here: pseudonymised data stay in archetype 1 or 4. All three WP216 criteria — singling out, linkability and inference — are tested after transformation, not selectively.]***

| WP216 Criterion | Typical Simulation Methods | Metric Value Range | Direction to Reduce Risk |
| :---- | :---- | :---- | :---- |
| Singling out | ***[Singling-out test; detection via atypical values (outliers)]*** | ***[Proportion 0–1]*** | ***[Decrease]*** |
| Linkability | ***[Deterministic linkage; probabilistic linkage (Fellegi-Sunter); nearest-neighbour linkage (k-NN); linkage through membership in a distinct cluster]*** | ***[Proportion 0–1]*** | ***[Decrease]*** |
| Inference | ***[Correct-attribution-probability (CAP) family, e.g. categorical ZCAP, reported as advantage over the prior; normalised information gain (1 − H(S\|Q)/H(S)); ML-based inference attack, reported as advantage over a baseline model]*** | ***[0–1 after the stated transformation]*** | ***[Decrease]*** |
| Proxy metrics | ***[k-anonymity, l-diversity, t-closeness, uniqueness rate]*** | ***[k, l ≥ 1; t 0–1; uniqueness 0–1]*** | ***[Increase k and l; decrease t and uniqueness]*** |

> **Guidance.** k-anonymity does not protect against attribute inference within homogeneous classes (WP216); l-diversity and t-closeness address this only partially. Proxy metrics are reported but are not sufficient on their own. Each project states which metrics are mandatory (gated) and which are diagnostic only.

### **3.3.2 Data Synthesis**

***[The synthetic dataset is a derived artefact that can disclose information about people in the training data. The module tests membership disclosure, memorisation (closeness of synthetic records to training records), linkability and attribute inference. Where the generator is trained with differential privacy, the DP statement of Section 3.3.5 is mandatory.]***

| Method / Metric | What It Measures | Value Range | Direction to Reduce Risk |
| :---- | :---- | :---- | :---- |
| ***[Membership inference attack (MIA) — accuracy and AUC on a balanced evaluation set; TPR at low FPR]*** | ***[Whether an attacker can tell if a specific record was in the training data]*** | ***[Accuracy/AUC 0.5 (chance) – 1; TPR 0–1]*** | ***[Decrease towards 0.5 / towards the FPR]*** |
| ***[Distance to Closest Record (DCR), low percentile — compared with the holdout baseline]*** | ***[Whether synthetic records are closer to training records than unseen real records are]*** | ***[0 (identical) and above]*** | ***[Increase]*** |
| ***[Nearest-Neighbour Distance Ratio (NNDR)]*** | ***[Whether a synthetic record sits unusually close to one specific training record]*** | ***[0 – 1]*** | ***[Increase towards 1]*** |
| ***[Linkability test for synthetic data — linkage of synthetic records to records of an auxiliary dataset representing attacker knowledge, scored as advantage over a control set]*** | ***[Whether a synthetic record can be linked to a real person's record]*** | ***[Advantage 0 – 1]*** | ***[Decrease]*** |
| ***[Attribute-inference test for synthetic data — scored as advantage over a control set]*** | ***[Whether secret attributes of real people can be inferred]*** | ***[Advantage 0 – 1]*** | ***[Decrease]*** |
| ***[DP parameters of the generator (ε, δ) and accountant]*** | ***[The formal guarantee of the training mechanism — Section 3.3.5]*** | ***[ε ≥ 0; δ ≥ 0]*** | ***[Configuration gate, not averaged]*** |

> **Guidance.** Published methods exist for testing singling out, linkability and inference on synthetic data by comparing attack success on training records with success on a control set of unseen records. Reconstruction of training records from the generator's parameters (model inversion) is a separate threat. If the organisation has no validated test for it, it records the limitation and restricts access to the generator's parameters accordingly; it does not claim the risk is covered.

### **3.3.3 Federated Learning / Joint Computation Without Data Centralisation**

***[The tests apply to the artefacts that cross a participant's boundary — model updates, the aggregated model, encrypted fragments, the result of a set intersection — not to the source data that stay with the participant. Federated learning and SMPC are processing architectures; they do not change the legal status of the data, they do not remove the need for a lawful basis, and where participants are in different countries they do not by themselves exempt any flow from Chapter V (Document 12, Document 20).]***

| Method / Metric | What It Measures | Value Range | Direction to Reduce Risk |
| :---- | :---- | :---- | :---- |
| ***[DP on model updates (ε, δ, accountant, composition across all rounds)]*** | ***[Formal guarantee for the privacy unit across the whole training — Section 3.3.5]*** | ***[ε ≥ 0; δ ≥ 0]*** | ***[Configuration gate]*** |
| ***[Secure aggregation / output restriction]*** | ***[Whether individual updates are visible to the coordinator or to other participants]*** | ***[Yes/No, with scope]*** | ***[Control (L3 of Section 3.2 for the access scenario)]*** |
| ***[Membership inference on the final model]*** | ***[Whether membership of a record in a participant's data can be inferred from the shared model]*** | ***[Accuracy/AUC 0.5 – 1]*** | ***[Decrease]*** |
| ***[Gradient-leakage / reconstruction test on updates]*** | ***[Whether records can be reconstructed from updates]*** | ***[Method-specific]*** | ***[Decrease]*** |

> **Guidance.** Where a test is not available (for example, a validated gradient-reconstruction test), the organisation records the gap, relies on the controls that remove the threat (secure aggregation, DP across all rounds, restricted access to updates), and does not present the DP parameters as a measured attack result.

### **3.3.4 Aggregate Statistics and Tabular Releases**

***[Aggregates are not anonymous by construction. Tables, counts, means and model outputs can disclose information through small cells, differencing between overlapping tables or successive releases, and database-reconstruction attacks that solve for the underlying records from many published statistics. For archetype 2b the module applies statistical disclosure control (SDC) gates before any record-level test:]***

| Check | What It Measures | Typical gate |
| :---- | :---- | :---- |
| ***[Minimum cell size (threshold rule)]*** | ***[Smallest number of persons contributing to any published cell after suppression]*** | ***[≥ [10] — illustrative internal SDC setting, calibrated to context; not an anonymity guarantee]*** |
| ***[Dominance rule (for magnitude tables)]*** | ***[Whether one or a few contributors dominate a cell total]*** | ***[(n, k) rule set by the project]*** |
| ***[Differencing check]*** | ***[Whether any cell below the minimum can be derived by subtracting published cells, within the release and against all previous releases from the same population]*** | ***[No derivable cell below the minimum]*** |
| ***[Reconstruction test]*** | ***[Share of source records that can be reconstructed exactly from the full set of published statistics]*** | ***[≤ project threshold]*** |
| ***[Record-level attack battery on reconstructed records (Section 3.3.1)]*** | ***[Singling out, linkability and inference on what an attacker can reconstruct]*** | ***[Project thresholds]*** |
| ***[Prohibited-attribute check]*** | ***[Presence of an attribute the project prohibits for the recipient: identifiable special-category data without an Art. 9(2) condition (also a G-L failure), or an attribute excluded by internal policy (labelled as such)]*** | ***[None (G-M3)]*** |

***[Where the volume or granularity of statistics makes these checks unreliable, the organisation either reduces the release or uses a differentially private release mechanism with a full DP statement (Section 3.3.5).]***

### **3.3.5 Differential Privacy Statements**

***[Any claim that an artefact is protected by differential privacy is accompanied by a DP statement with at least the following elements (NIST SP 800-226):]***

| Element | Content |
| :---- | :---- |
| ***[Privacy unit]*** | ***[What is protected: one record, or all records of one person (person-level). Where a person can contribute several records, a contribution bound per person is stated.]*** |
| ***[Adjacency relation]*** | ***[Add/remove one privacy unit, or replace one privacy unit]*** |
| ***[Mechanism and accountant]*** | ***[The mechanism (e.g. DP-SGD with stated noise multiplier, clipping norm, sampling rate and number of steps/epochs; Laplace or Gaussian mechanism) and the privacy accountant used to compute ε at the chosen δ (e.g. Rényi DP or privacy-loss-distribution accounting)]*** |
| ***[ε and δ]*** | ***[ε for the stated δ. δ is the additive term in the definition of approximate (ε, δ)-DP; it is not "the probability that the guarantee fails". A common engineering heuristic is to choose δ well below 1/n for the population of privacy units n; where used, the project states n, the privacy unit and the accountant. This heuristic is not a legal test, not a universal obligation and not evidence of anonymity.]*** |
| ***[Composition]*** | ***[Total privacy loss across all training runs, rounds and releases from the same source population, including runs used for model selection, previews and failed or cancelled runs whose outputs were observable (Section 3.3.6)]*** |
| ***[Output access]*** | ***[Who can access which outputs (final model, intermediate checkpoints, logs, previews). Post-processing of a DP output does not consume additional budget; outputs not covered by the mechanism (e.g. non-private hyper-parameter search, debugging logs) are not protected by it.]*** |
| ***[Implementation assurance]*** | ***[How the implementation was verified (code review, tests, library version); known implementation hazards (floating-point, sampling assumptions) addressed]*** |
| ***[Limits of empirical tests]*** | ***[Empirical attacks give lower bounds on leakage for the attacks tried; they neither prove nor disprove the formal guarantee.]*** |

***[Relation between ε and membership-inference results. For a membership hypothesis test between two adjacent datasets, with a uniform prior (0.5) and an attacker who knows everything except the presence of the target privacy unit, any test's accuracy is bounded by (e^ε + δ)/(1 + e^ε); for pure ε-DP (δ = 0) the bound is e^ε/(1 + e^ε). This is a narrow worst-case bound under those stated assumptions. It is not a probability of re-identification and it is not used in the risk score. An observed MIA accuracy well below the bound is compatible with it: the bound describes the strongest possible attacker under the stated assumptions, the empirical test describes the attacks actually run. Neither is a universal anonymity guarantee.]***

### **3.3.6 Repeated Releases and Cumulative Disclosure**

* ***[Every new release, retraining or re-publication from the same source population requires a composition and linkage assessment: what an attacker learns by combining it with all earlier releases, including differencing across releases (Section 3.3.4).]***

* ***[For DP releases, the organisation keeps a **lifetime** privacy-loss ledger per source population and privacy unit. Outputs that have been released or observed stay in the composition permanently: there is no calendar reset. The ledger records ε **and** δ for every run, the accountant used, the privacy unit and the observers who had access. Re-using or copying a DP output (post-processing) does not consume additional budget; a new mechanism run on the source data does.]***

* ***[Composition across runs is computed with a method valid for all runs: basic composition (sum of the ε values and sum of the δ values) is always valid when each run's (ε, δ) guarantee holds; tighter composition (for example with Rényi DP or privacy-loss distributions) is used only where every run's accounting state is available in a compatible form. A later run at a smaller δ does not reduce the cumulative δ of earlier runs. Unless observer sets are shown to be separate and unable to combine outputs, all outputs on overlapping privacy units are composed as if one party had observed them.]***

* ***[An operational cap (for example, a maximum new ε per calendar year) may be set in addition, as an internal pacing rule. It never replaces the lifetime ledger.]***

* ***[Budget accounting covers every observable output: committed releases, but also failed or cancelled runs whose outputs, previews or logs were visible, outputs used for model or hyper-parameter selection, and parallel or reserved runs. "Commit-only" accounting (counting only released outputs) is not adopted unless an analysis shows that no other output was observable.]***

* ***[Where Document 8 sets a lifetime cumulative budget (ε and δ) or an operational cap per source population, a release that would exceed either fails the module (G-M4). A PASS that relies on the ledger states the ledger's assumptions (runs included, composition method, observer assumption).]***

## **3.4 Severity Assessment Factors (Track (a)) and Organisational Consequences (Track (b))**

> **Guidance.** Document 8 fixes the qualitative severity tiers (Minor / Moderate / Significant / Catastrophic). The point scale below is established once, here, for the whole catalogue; Risk Calculation Projects apply it without redefining it. The scale is ordinal: adding ordinal scores is a structured aid to judgement, not a measurement, and the band cut-points are reviewed with a sensitivity analysis at each review of this document (Section 7).

***[Severity is assessed per harm scenario. Factor A (harm type) is a mandatory tag. Factors B, C, D, E and G are scored and summed into the severity index for track (a). Factor F records organisational consequences on track (b) and is not part of the severity index. The organisation may add factors (H, …) but may not remove the harm types of Factor A.]***

| Factor | Description |
| :---- | :---- |
| ***[A]*** | ***[Harm type — mandatory tag identifying the harm type(s) of the scenario; not summed]*** |
| ***[B]*** | ***[Intensity of harm per data subject — data class, special categories, vulnerability of the affected persons]*** |
| ***[C]*** | ***[Scale — number of affected persons and aggregation of sources]*** |
| ***[D]*** | ***[Reach and containment — how far and how irreversibly the data or the effect spreads beyond the primary recipient]*** |
| ***[E]*** | ***[Automated decision-making with a significant effect — where the harm is produced through such a decision]*** |
| ***[F]*** | ***[Organisational consequences — track (b), recorded separately]*** |
| ***[G]*** | ***[Data provenance and reasonable expectations of the data subject]*** |
| ***[H]*** | ***[Name and description of an additional factor — completed if necessary]*** |

> **Guidance.** This catalogue takes into account the ENISA methodology for assessing the severity of personal data breaches (2013; SE = DPC × EI + CB) and the CNIL PIA severity scale (Negligible / Limited / Significant / Maximum) without adopting either in full. The ENISA model is calibrated for retrospective breach assessment with three factors: DPC (data processing context) is reflected in Factors B and C; EI (ease of identification) is reflected in the likelihood track (Section 3.2) or the PET Assessment Module (Section 3.3); CB (circumstances of breach) is reflected in Factor D. Factors A, E and G extend the catalogue beyond both references. Sources: ENISA, *Recommendations for a methodology of the assessment of severity of personal data breaches* (https://www.enisa.europa.eu/publications/dbn-severity); CNIL, *Privacy Impact Assessment (PIA)* methodology and templates (https://www.cnil.fr/en/privacy-impact-assessment-pia).

**Severity floors.** ***[Whatever the index, a scenario is rated at least Significant where it involves (i) disclosure of identifiable special-category data to an unlimited audience or their use to make decisions about the person, or (ii) a realistic risk of physical harm. Weights (Section 4.1) cannot lower a scenario below its floor.]***

**No double counting.** ***[A characteristic is scored in one factor only. For example, minors are scored under "Data Subject Vulnerability", not also through the data class; a PET or a control is reflected in likelihood (Section 3.2 or 3.3), not also as a severity discount.]***

### **Factor A — Harm Type (mandatory tag, not included in the sum)**

***[A tag that makes the scenario's harm type explicit in the evidence pack (Section 4.5). It is not a score. Every project records, for each harm type, either the scenario(s) assessed or a short reason why the harm type is not relevant.]***

| Value | Score | Explanation |
| :---- | :---- | :---- |
| ***Unlawful processing / loss of control*** | ***tag*** | ***Processing beyond what the person can expect or control (function creep, covert profiling, inability to exercise rights)*** |
| ***Discrimination / adverse automated decision*** | ***tag*** | ***Unjustified refusal, worse terms or unequal treatment, including through proxies for protected characteristics*** |
| ***Financial loss*** | ***tag*** | ***Direct or indirect monetary loss, higher cost of credit, fraud losses*** |
| ***Identity fraud*** | ***tag*** | ***Misuse of identity data to open accounts, take over accounts or impersonate*** |
| ***Reputational and social harm*** | ***tag*** | ***Embarrassment, stigma, damage to relationships or standing*** |
| ***Physical, psychological, chilling effects, exclusion*** | ***tag*** | ***Harm to health or safety; distress; self-censorship; exclusion from services*** |
| ***Loss of confidentiality, integrity or availability*** | ***tag*** | ***Unauthorised disclosure or access, alteration, loss of access to one's data*** |

> **Guidance.** The list reflects GDPR Recitals 75 and 85 (physical, material and non-material damage, including discrimination, identity theft or fraud, financial loss, damage to reputation, loss of confidentiality, and loss of control) and the problematic data actions and problems for individuals described in NISTIR 8062.

### **Factor B — Intensity per Data Subject**

### **Data Class**

***[Reflects the baseline sensitivity of the information under the organisation's data classification — the higher the class, the greater the intrusion into private life if the scenario materialises.]***

| Value | Score | Explanation |
| :---- | :---- | :---- |
| ***[Public]*** | ***[0]*** | ***[Publicly available information]*** |
| ***[Internal]*** | ***[1]*** | ***[Internal information of limited distribution]*** |
| ***[Confidential]*** | ***[2]*** | ***[Confidential, person-specific information]*** |
| ***[Restricted]*** | ***[3]*** | ***[Information of the highest sensitivity]*** |

> **Guidance.** Source: Data Classification Policy (Document 10).

***[Age of the data. Where the data are retrospective or stale (older than [5] years) and the scenario's harm depends on their currency, the data-class score may be reduced by 1. The reduction does not apply to special-category data or to permanent attributes (identity documents, health history). Synthetic data receive no data-class reduction: the severity of a disclosure scenario is the severity of disclosing the source information about real people; the protective effect of synthesis is assessed in the PET Assessment Module.]***

| Modifier | Score (applied to the "Data Class" score) | Explanation |
| :---- | :---- | :---- |
| ***Current data, or data whose harm does not depend on currency*** | ***0*** | ***Modifier does not apply*** |
| ***Retrospective or stale data (> [5] years), harm depends on currency*** | ***−1*** | ***Harm is reduced by the weaker link to the person's current situation, but not eliminated*** |

### **Special Categories of Data**

***[Special categories (Art. 9) and criminal-offence data (Art. 10) create harm qualitatively different from that of ordinary data. Their presence is also a G-L matter: a valid Art. 9(2) condition (or Art. 10 basis) is required for the processing, and identifiable special-category data may not be disclosed in an open release without such a condition. An organisation may adopt a stricter internal policy excluding such attributes from open releases altogether; it is labelled as internal policy.]***

| Value | Score | Explanation |
| :---- | :---- | :---- |
| ***[Present in the data concerned by the scenario]*** | ***[+2]*** | ***[Heightened, qualitatively different harm]*** |
| ***[Absent]*** | ***[0]*** | ***[Factor does not apply]*** |

> **Guidance.** Source: Data Classification Policy (Document 10), enhanced regime. The score is not raised by exposure arguments (for example, a wider circle of staff with access); exposure belongs to likelihood (Section 3.2).

### **Data Subject Vulnerability**

***[Reflects the heightened vulnerability of certain persons where the scenario's harm falls on them or is aggravated for them — for example, refusal of credit to financially vulnerable customers, or disclosure of the vulnerability marker itself.]***

| Value | Score | Explanation |
| :---- | :---- | :---- |
| ***The scenario does not specifically affect vulnerable persons*** | ***0*** | ***Factor does not apply*** |
| ***The scenario's harm falls on, or is aggravated for, vulnerable persons (e.g. elderly customers, persons in financial difficulty)*** | ***+1*** | ***Limited ability to protect their own interests*** |
| ***The scenario affects children*** | ***+2*** | ***Children merit specific protection (Recital 38)*** |

> **Guidance.** Source: GDPR Recitals 38 and 75. The organisation defines and documents its vulnerable categories in the project passport (Section 4.1).

### **Factor C — Scale**

### **Number of Affected Data Subjects**

***[The number of persons who would be affected if the scenario materialised. For a decision scenario, use the number of persons subject to the decision over the review period; for a disclosure scenario, the number of persons whose information is in the data concerned.]***

| Value | Score | Explanation |
| :---- | :---- | :---- |
| ***[< 100]*** | ***[0]*** | ***[Small scale]*** |
| ***[100 – 9,999]*** | ***[1]*** | ***[Moderate scale]*** |
| ***[10,000 – 999,999]*** | ***[2]*** | ***[Large scale]*** |
| ***[≥ 1,000,000]*** | ***[3]*** | ***[Mass scale]*** |

### **Source Aggregation**

***[Combining independent sources forms a more complete picture of the person and increases the harm if the scenario materialises.]***

| Value | Score | Explanation |
| :---- | :---- | :---- |
| ***The data originate from a single source/system*** | ***0*** | ***Factor does not apply*** |
| ***The data combine two or more independent sources/systems*** | ***+1*** | ***A more complete profile increases potential harm*** |

> **Guidance.** Source: the organisation's data flow map (Document 23).

### **Pilot Restriction**

***[A pilot limited to a small, documented group outside production is reflected through the "Number of Affected Data Subjects" score; there is no separate discount. The pilot's lawful basis is checked by G-L (for example, consent of employees is presumptively not freely given in an employment relationship — EDPB Guidelines 05/2020 on consent). When the pilot moves into production, the scale is reassessed (Section 7).]***

### **Factor D — Reach / Containment**

### **Base Tier**

***[The same data can create different harm depending on how broad and controllable the circle of recipients is: sharing with a partner means a partial loss of direct control; unconditional publication makes exposure unbounded and practically irreversible.]***

| Value | Score | Explanation |
| :---- | :---- | :---- |
| ***Data or effect remain within the organisation's own environment*** | ***0*** | ***Full direct organisational control*** |
| ***Data are shared with a partner, processor or other recipient*** | ***+1*** | ***Partial loss of direct control*** |
| ***Data are subject to open, unconditional publication*** | ***+2*** | ***Unbounded audience; practically irreversible*** |

> **Guidance.** The quality of the contractual and factual control at the recipient (Art. 28 data processing agreement, Art. 26 arrangement or data-sharing agreement, and the due-diligence status under Document 17) and the readiness of a tested incident-response plan are controls. They are assessed under likelihood factor L3 (Section 3.2), not as severity modifiers.

### **Factor E — Automated Decision-Making with a Significant Effect**

***[Applies to scenarios whose harm is produced through a decision based solely on automated processing that produces legal effects for the person or similarly significantly affects them (Art. 22) — including where an automatically produced score plays a determining role in a third party's decision (CJEU C-634/21 *SCHUFA Holding (Scoring)*). It also applies to integrity scenarios in which corrupted data feed such a decision. It does not apply to a pure disclosure scenario.]***

| Value | Score | Explanation |
| :---- | :---- | :---- |
| ***The scenario's harm is not produced through an automated decision with a significant effect*** | ***0*** | ***Factor does not apply*** |
| ***The scenario's harm is produced through such a decision*** | ***+2*** | ***The harm directly affects a significant decision about the person*** |

> **Guidance.** Art. 22 permissibility and safeguards are checked by G-L; for a high-risk AI system under the AI Act, the deployer's obligations (including, where applicable, the fundamental rights impact assessment of Art. 27) follow their own application dates and are recorded in the DPIA (Document 19).

### **Factor F — Organisational Consequences (Track (b), not part of the severity index)**

***[Records the consequences for the organisation if the scenario materialises — regulatory, financial, reputational and operational. Factor F is reported as a separate level on the same four-tier scale and is passed to enterprise risk management (Document 3). It never lowers, offsets or averages the track (a) tier, and it is not added to the severity index.]***

| Subfactor | Value | Score | Explanation |
| :---- | :---- | :---- | :---- |
| ***Applicable regime*** | ***Processing falls under a regime of heightened regulatory scrutiny (e.g. a high-risk AI system; sector supervision)*** | ***+1*** | ***Additional regulatory exposure*** |
| ***Applicable regime*** | ***No such regime*** | ***0*** | ***—*** |
| ***Financial and operational impact*** | ***Fines, remediation cost, compensation claims, service interruption — [ranges set by the organisation's ERM]*** | ***0 – 3*** | ***Per the ERM scale (Document 3)*** |
| ***Reputational impact*** | ***Media, customer or market reaction — [ranges set by ERM]*** | ***0 – 3*** | ***Per the ERM scale*** |
| ***Regulatory sandbox / experimental regime*** | ***Covered by a current, attributed regulator decision, within its scope and term*** | ***−1*** | ***Applies to track (b) only; never to track (a)*** |

| Track (b) index | Organisational consequence level |
| :---- | :---- |
| ***[0 – 1]*** | ***[Minor]*** |
| ***[2 – 3]*** | ***[Moderate]*** |
| ***[4 – 5]*** | ***[Significant]*** |
| ***[6 and above]*** | ***[Catastrophic]*** |

***[Track (b) index = max(0, sum of the subfactor scores): the sandbox reduction can lower the index to 0 but not below it.]***

> **Guidance.** Processing outside the stated purpose or without a documented lawful basis is not scored: it is a G-L failure (Section 2.1). Consent is a lawful basis, not a severity mitigant, and is not scored on either track. Source: Regulatory Applicability Matrix (Document 7) for the applicable regime; the organisation's ERM scales for financial, operational and reputational impact.

### **Factor G — Data Provenance and Reasonable Expectations**

***[How the organisation came to hold the data affects whether the processing matches the person's reasonable expectations, and therefore the harm of a loss-of-control scenario. Factor G does not score lawfulness: a missing lawful basis or a missing Art. 13/14 notice is a G-L failure. Provenance must be attributed in the project passport (Section 4.1), with reference to the "Data Source" field of the RoPA (Document 21); an unattributed provenance is a gate, not a default score.]***

| Value | Score | Explanation |
| :---- | :---- | :---- |
| ***Direct collection from the person, with clear and specific notice (Art. 13)*** | ***0*** | ***Base branch — processing within expectations*** |
| ***Direct collection, notice formally given but the purpose is described vaguely*** | ***+1*** | ***Processing at the edge of expectations (the transparency deliverable itself is checked by G-L)*** |
| ***Obtained from a third party or public register — the source is regulated and expected by the person, notice given (Art. 14)*** | ***0*** | ***Base branch*** |
| ***Obtained from a third party or public register — the source is outside the person's typical expectations*** | ***+1*** | ***Lower predictability for the person*** |
| ***Scraping / aggregation from open sources — the data identify the person, same context of publication*** | ***+1*** | ***Re-use the person may not expect*** |
| ***Scraping / aggregation from open sources — the data identify the person and are used outside the original context (recontextualised)*** | ***+2*** | ***Use outside the context in which the person published the data*** |
| ***Scraping / aggregation where the data do not relate to an identifiable person (Recital 26 test, Section 3.3.0)*** | ***0*** | ***Outside the scope of personal data — documented conclusion required*** |
| ***Third party without notice or without a lawful basis*** | ***GATE — G-L failure*** | ***Not scored; stop or redesign*** |
| ***Provenance other or unattributed*** | ***GATE — not scored*** | ***The calculation is not complete without attribution in the project passport, with reference to the RoPA (Document 21)*** |

> **Guidance.** Source: the "Data Source" field of the RoPA (Document 21). Notice for direct collection — Art. 13 GDPR; notice for data obtained from others — Art. 14 GDPR. The synthetic branch is not scored here: the severity of a disclosure scenario for synthetic data is assessed on the source data (Factor B).

***[The maximum score of each factor follows from its tables (B up to 7, C up to 4, D up to 2, E up to 2, G up to 2); no further caps apply.]***

## **3.5 Other Metrics (Data Quality and Utility)**

> **Guidance.** This subsection is a catalogue of metrics that the organisation can compute to assess the quality, applicability and utility of data after a PET has been applied. They do not take part in the risk calculation (Sections 3.2–3.4): they measure how fit the data are for a task, not how well they are protected. Which of these metrics apply, and with which thresholds, is determined for each Risk Calculation Project (Section 4.6).

| Metric | What It Measures | Value Range | Management Direction to Improve the Characteristic |
| :---- | :---- | :---- | :---- |
| ***[Preservation of distributions (for example, comparison of empirical distributions by column)]*** | ***[How closely the distribution of the transformed data corresponds to the source]*** | ***[Depends on the method; usually from 0 (identical) and above]*** | ***[Decrease — move toward 0]*** |
| ***[Preservation of correlations between fields]*** | ***[How well relationships between variables are preserved after transformation]*** | ***[Depends on the method]*** | ***[Minimise divergence from the source correlation structure]*** |
| ***[Distance between distributions (for example, a Wasserstein-type metric)]*** | ***[How statistically far the distribution of the transformed data is from the source]*** | ***[Depends on the method; usually from 0 and above]*** | ***[Decrease]*** |
| ***[Divergence between distributions (for example, a Kullback-Leibler-type metric)]*** | ***[The information difference between the distribution of the transformed and source data]*** | ***[From 0 (identical) and above]*** | ***[Decrease]*** |
| ***[Preservation of principal-component structure (for example, a PCA-distance-type metric)]*** | ***[How well the multidimensional structure of the data is preserved after transformation]*** | ***[Depends on the method]*** | ***[Decrease]*** |
| ***[Utility for a downstream task (for example, the quality of a model trained on the transformed data, relative to a model trained on the source data)]*** | ***[How fit the transformed data is for the task it was created for]*** | ***[Depends on the task metric (F1, AUC, etc.)]*** | ***[Increase — move toward the performance of the model on the source data]*** |
| ***[Robustness of utility under a change of task (for example, an AUC difference on an alternative task)]*** | ***[How well the transformed data retains fitness beyond the task it was created for]*** | ***[Depends on the task metric]*** | ***[Increase]*** |

These metrics are reported in the evidence pack alongside the risk metrics, but as a separate, explicitly labelled block — the decision on the acceptability of residual risk may not rely on high data quality/utility as compensation for elevated privacy risk.

## **4. Privacy Risk Calculation Project**

> **Guidance.** A Risk Calculation Project is a finished, versioned configuration of the methodology for a specific business case: the harm scenarios to be assessed; the likelihood factors (Section 3.2) or the PET-module metrics, thresholds, weights and gates (Section 3.3); the severity factors with their scores (Section 3.4); and the quality/utility metrics (Section 3.5). Not every catalogue element applies to every project. The organisation maintains as many projects as it has cases with distinct risk profiles. In the terminology of some technical platforms, a project corresponds to a pipeline. Subsections 4.1–4.6 below give the structure of one project; the organisation reproduces it for each project.

## **4.1 Purpose and Characteristics of the Project**

> **Guidance.** The project passport: what the project covers, why it needs its own configuration, and its formal characteristics. The technical calculation begins in Section 4.2.

* ***[Purpose — which business case the project covers and why it requires a separate configuration.]***

* ***[Scope — which datasets/processes the project applies to and which it does not.]***

* ***[Archetype and technology — the archetype (Section 3.1) and, for archetypes 2–3, the PET technology (Section 3.3).]***

| Characteristic | Value |
| :---- | :---- |
| ***[Project Owner]*** | ***[Privacy Operations Lead (configuration approved by the EPPO; DPO advice recorded)]*** |
| ***[Configuration Version]*** | ***[Version number, versioned separately from this document]*** |
| ***[Review Frequency]*** | ***[For example, annually and upon a material change in the business case, the data, the recipients or the threat landscape]*** |
| ***[Effective Date]*** | ***[Date from which the project is applied]*** |
| ***[Archetype]*** | ***[1 / 2a / 2b / 3 / 4 — Section 3.1]*** |
| ***[G-L Record]*** | ***[Reference to the G-L record for the processing (lawful basis, Art. 9/10 condition where relevant, purpose compatibility, transparency, Art. 22, Chapter V); mandatory for archetype 4 and for any release]*** |
| ***[Harm Scenarios]*** | ***[List of scenarios assessed (threat source → data action/event → harm type, Factor A), and the reasons why other harm types are not relevant]*** |
| ***[Adversary Profile × Disclosure Channel (archetypes 2–3)]*** | ***[Declared explicitly with reference to the recipient and the means reasonably likely to be used (Recital 26); if not declared, the strictest profile defined by the organisation applies]*** |
| ***[Mandatory (Gated) Metrics and Diagnostic Metrics (archetypes 2–3)]*** | ***[Which metrics are mandatory and gated (G-M1); which are diagnostic only]*** |
| ***[Unacceptable-Attack Definitions (G-M2, archetypes 2–3)]*** | ***[For each attack in the project's attack set: scope (records, population, auxiliary data), baseline, unacceptable-success level and uncertainty rule; qualitative paths treated as unacceptable regardless of rate]*** |
| ***[DP Statement (where DP is used)]*** | ***[Privacy unit; adjacency; mechanism and accountant; ε at the stated δ; composition; output access — Section 3.3.5; lifetime ledger entry (cumulative ε and δ) and any operational cap — Section 3.3.6]*** |
| ***[Weight Vector (w\_B, w\_C, w\_D, w\_E, w\_G)]*** | ***[Default (1, 1, 1, 1, 1); a corridor of 0.5–2.0 per factor, with written justification for any deviation; outside the corridor — EPPO approval with DPO advice]*** |
| ***[Diagnostic Alert Mode]*** | ***[Applies to diagnostic (non-gated) metrics only: Strict (halt and escalate to the Privacy Operations Lead and EPPO) or Lenient (continue, log for audit, Document 27). Mandatory metrics are always gated; no lenient mode applies to them.]*** |
| ***[Data Provenance Attribution (Factor G)]*** | ***[Reference to the "Data Source" field of the RoPA (Document 21); without attribution the calculation cannot be completed — a gate]*** |
| ***[Vulnerable Categories]*** | ***[Categories of vulnerable persons recognised for this project (Factor B)]*** |

* ***[A PET reduces identifiability; it does not by itself remove personal data. For archetypes 2–3, the PET-module metrics measure how well the transformed artefact resists the attacks tested, given the source data — they are a function of both datasets. A technique applied with unsuitable parameters may not reduce the actual risk, notwithstanding its formal use.]***

## **4.2 Likelihood**

> **Guidance.** For each harm scenario, likelihood is assessed either with the threat-based model (Section 3.2) or, for the disclosure scenario of archetypes 2–3, with the PET Assessment Module (Section 3.3). The project lists the factors or metrics used and any deviation from catalogue defaults, with reasons.

**A. Threat-based scenarios (Section 3.2).**

| Scenario | L1 Exposure | L2 Threat source | L3 Control gap (inherent / residual) | L4 History | Index (inherent / residual) | Level (inherent / residual) |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| ***[S1 …]*** | ***[0–3]*** | ***[0–3]*** | ***[3 / 0–3, with evidence reference]*** | ***[0–2]*** | ***[…]*** | ***[…]*** |

**B. PET Assessment Module (Section 3.3).**

| Metric (from the catalogue) | Mandatory (gated) or diagnostic? | Threshold for the project | Difference from the default threshold |
| :---- | :---- | :---- | :---- |
| ***[Metric 1]*** | ***[Mandatory/Diagnostic]*** | ***[Value]*** | ***[Same as default / differs — justification]*** |
| ***[Metric 2]*** | ***[Mandatory/Diagnostic]*** | ***[Value]*** | ***[Same as default / differs — justification]*** |
| ***[…]*** | ***[…]*** | ***[…]*** | ***[…]*** |

| Step | Options / Sub-steps | Description |
| :---- | :---- | :---- |
| ***[Step 1 — Per-metric results]*** | ***[All selected metrics]*** | ***[Each metric is computed and reported with its confidence interval (Section 3.3.0)]*** |
| ***[Step 2 — Failure gates]*** | ***[G-M1 to G-M5]*** | ***[If any gate fails, the module FAILS (or is INCOMPLETE under G-M5) regardless of Steps 3–5; the release is not made in its current form; the as-proposed likelihood is recorded as High, or Near-certain under the internal routing rule (Section 3.3.0)]*** |
| ***[Step 3 — Normalisation]*** | ***[Baseline-aware normalisation with allowed domains and orientation (Section 3.3.0)]*** | ***[0 = no-disclosure baseline; 1 = project threshold. Formal DP parameters are not normalised]*** |
| ***[Step 4 — Weighting]*** | ***[Category weight (e.g. a WP216 criterion or a group of technology metrics); metric weight within the category]*** | ***[Non-negative, summing to 1; justified and versioned separately from the thresholds]*** |
| ***[Step 5 — Disclosure indicator]*** | ***[Weighted average]*** | ***[Disclosure indicator = Σ (normalised value × weight). An uncalibrated ordinal summary; not a probability]*** |
| ***[Step 6 — Likelihood level]*** | ***[Module outcome table (Section 3.3.0)]*** | ***[PASS, indicator < 0.5 → Low; PASS, 0.5 ≤ indicator ≤ 1.0 → Medium; INCOMPLETE → not assessed; FAIL → High, or Near-certain under the internal routing rule (as-proposed only)]*** |

## **4.3 Severity**

> **Guidance.** The project lists the catalogue factors (Section 3.4) it uses for each scenario and any project-specific score, with reasons. A project-specific score may refine, but may not lower, a catalogue score below a severity floor.

| Factor (from the catalogue) | Applies to the project? | Score for the project | Difference from the default score |
| :---- | :---- | :---- | :---- |
| ***[Factor 1]*** | ***[Yes/No]*** | ***[Value]*** | ***[Same as default / differs — justification]*** |
| ***[Factor 2]*** | ***[Yes/No]*** | ***[Value]*** | ***[Same as default / differs — justification]*** |
| ***[…]*** | ***[…]*** | ***[…]*** | ***[…]*** |

| Step | Description |
| :---- | :---- |
| ***[Step 1 — Value of each applicable factor per scenario]*** | ***[For the specific scenario, determine the value of each applicable factor and its score]*** |
| ***[Step 2 — Weighting and summation]*** | ***[Severity index = w\_B·B + w\_C·C + w\_D·D + w\_E·E + w\_G·G, with a floor of 0, where B…G are the sums of the applicable subfactor scores (Section 3.4) and the weights come from the project passport (default 1). Factor A is a tag. Factor F is not part of the index: it is reported as a separate track (b) level]*** |
| ***[Step 3 — Mapping to a level]*** | ***[The severity index is mapped to the Document 8 severity scale through the table below; the severity floors of Section 3.4 then apply]*** |

| Severity index (sample) | Severity level (Document 8) |
| :---- | :---- |
| ***[index < 3.5]*** | ***[Minor]*** |
| ***[3.5 ≤ index < 6.5]*** | ***[Moderate]*** |
| ***[6.5 ≤ index < 8.5]*** | ***[Significant]*** |
| ***[index ≥ 8.5]*** | ***[Catastrophic]*** |

***[The intervals are contiguous and non-overlapping, so every index value — including fractional values produced by weights between 0.5 and 2.0 — maps to exactly one level, without rounding. With default weights the index is an integer and the bands read 0–3, 4–6, 7–8 and 9 or more.]***

***[A worked calculation is added on the project's first practical application.]***

## **4.4 Final Residual Risk Level and Decision Steps**

> **Guidance.** The likelihood level (Section 4.2) and the severity level (Section 4.3) of each scenario are combined through the residual-risk matrix of Document 8, Section 4, which is not reproduced here. The track (a) tier of the processing is the highest scenario tier; scenarios are never averaged, and track (b) never lowers track (a). Who may accept which tier is set by Document 8, Section 5.

| Step | Description |
| :---- | :---- |
| ***[Step 0 — G-L]*** | ***[Confirm and reference the G-L record. If G-L failed, stop: no tier is available for acceptance; the processing is stopped or redesigned (Section 2.1)]*** |
| ***[Step 1 — Likelihood per scenario]*** | ***[Result of Section 4.2 (inherent and residual)]*** |
| ***[Step 2 — Severity per scenario]*** | ***[Result of Section 4.3, after severity floors]*** |
| ***[Step 3 — Scenario tier]*** | ***[Both levels are mapped through the Document 8 matrix — result Low/Medium/High/Critical (inherent and residual)]*** |
| ***[Step 4 — PET-module outcome]*** | ***[For archetypes 2–3: if the module failed, the release is not available for acceptance, whatever the tier]*** |
| ***[Step 5 — Track (a) tier]*** | ***[Highest residual scenario tier]*** |
| ***[Step 6 — Additional project rules (if any)]*** | ***[For example, a mandatory increase by one step when a project-specific condition is met; such rules may only make the result stricter and require justification]*** |
| ***[Step 7 — G-36]*** | ***[Evaluate the Art. 36(1) test for every DPIA: does high risk to rights and freedoms remain in the absence of further mitigating measures? A High or Critical track (a) tier is a strong indicator. The legal conclusion and its reasons are recorded separately (Legal, with DPO advice). Where the test is met, the supervisory authority is consulted before processing starts (Section 2.1)]*** |
| ***[Step 8 — Acceptance]*** | ***[The single decider designated under Document 8, Section 5, for the residual tier decides; DPO advice is recorded where a DPIA exists and in every case at Medium and above; Critical is not acceptable]*** |
| ***[Step 9 — Track (b)]*** | ***[The organisational consequence level (Factor F) is reported separately to enterprise risk management (Document 3)]*** |

## **4.5 Traceability of the Calculation and the Evidence Pack**

### **Block 0 — Gates**

* ***[G-L record reference and outcome; G-DPIA triage outcome (Document 19); for transfers, the G-TIA reference (Document 20).]***

### **Block 1 — Project Passport**

* ***[Archetype; harm scenarios and the relevance statement for each Factor A harm type.]***

* ***[Adversary profile × disclosure channel (archetypes 2–3), or the "not declared → strictest profile" flag.]***

* ***[Weight vector (w\_B…w\_G) and the justification for any deviation; EPPO approval and DPO advice where outside the 0.5–2.0 corridor.]***

* ***[Diagnostic alert mode; list of mandatory (gated) metrics.]***

* ***[Data provenance attribution with reference to the "Data Source" field of the RoPA (Document 21).]***

### **Block 2 — Likelihood**

* ***[Threat-based scenarios: L1–L4 with evidence references for L3 (controls), inherent and residual index and level.]***

* ***[PET Assessment Module: every metric with value, threshold, normalised value, confidence interval and pass/fail; each failure gate and its outcome; disclosure indicator; module outcome (PASS/FAIL); DP statement; cumulative privacy-loss ledger entry (Section 3.3.6).]***

* ***[Justification for any deviation of a threshold from the default, with reference to the declared adversary profile and channel.]***

* ***[Documented limitations (tests not available, untested attack classes) and how they are mitigated.]***

### **Block 3 — Severity and Track (b)**

* ***[Full calculation per scenario across Factors B/C/D/E/G, the subfactors triggered, the severity floors applied, and the Factor A tag.]***

* ***[Track (b): Factor F subfactors and the organisational consequence level, reported separately.]***

### **Block 4 — Decision and Governance**

* ***[Scenario tiers (inherent and residual) and the track (a) tier obtained through the Document 8 matrix (Section 4.4).]***

* ***[G-36: the legal conclusion on the Art. 36(1) test, with reasons; where consultation took place, the submission date, the supervisory authority's written advice or information requests, and how the advice was implemented.]***

* ***[The DPO's advice — content, reservations and caveats, not merely a reference (\`dpo\_advice\_ref\`).]***

* ***[The decision of the single effective decider designated under Document 8, Section 5 (accept / do not accept / accept with conditions and expiry date), as a standalone mandatory item. Where the decision departs from the DPO's advice, the decider records the reasons (\`dpo\_advice\_not\_followed\_reasons\`); the DPO may escalate directly to Executive Management.]***

* ***[The pack is compiled for every calculation, whatever the tier. A missing mandatory element is a declared gap, not a silent default. A change to weights, thresholds, metrics or factors is a versioned change to the project configuration; previous versions are retained so that earlier decisions can be reproduced.]***

* ***[Delineation of decisions: this block records the decision on acceptance of the residual risk of a processing activity under Document 8. A conclusion that information is anonymous, or that an operation is not a transfer under Chapter V, is a separate legal conclusion of the controller. It is taken by the role designated by the controller's delegation (normally the Processing Owner, on Legal's assessment), with DPO advice; it is supported by — but never determined by — the results of this methodology. The DPO advises and monitors; the DPO does not make the determination.]***

## **4.6 Other PET Application Metrics**

> **Guidance.** The quality and utility metrics from the catalogue (Section 3.5) calculated in this project, with any deviation from default thresholds. They are reported in a separate block and never compensate for privacy risk.

| Metric (from catalogue 3.5) | Calculated in the project? | Threshold/benchmark for the project | Difference from the default |
| :---- | :---- | :---- | :---- |
| ***[Metric 1]*** | ***[Yes/No]*** | ***[Value]*** | ***[Same as default / differs — justification]*** |
| ***[…]*** | ***[…]*** | ***[…]*** | ***[…]*** |

## **5. Roles and Responsibilities**

| Role | Responsibility |
| :---- | :---- |
| ***[Executive Privacy Programme Owner (EPPO)]*** | ***[Owns this methodology (drafting and maintenance for adoption by Executive Management); approves the configuration of each Risk Calculation Project, including deviations from catalogue defaults; concurs in Medium acceptances (Document 8)]*** |
| ***[Privacy Operations Lead]*** | ***[Owns Risk Calculation Projects (Section 4.1); runs calculations; maintains configuration versions and the privacy-loss ledger (Section 3.3.6); initiates re-calculation and periodic re-assessment]*** |
| ***[Privacy Engineer(s)]*** | ***[Implement metrics, attacks and DP accounting; ensure traceability, confidence intervals and reproducibility (Section 4.5)]*** |
| ***[Legal]*** | ***[Owns G-L; records the legal conclusion on the Art. 36(1) test and on anonymity or transfer status, with DPO advice]*** |
| ***[DPO]*** | ***[Advises on every DPIA (Art. 35(2)) and on project configurations, scenario selection, the G-36 conclusion and anonymity conclusions; monitors compliance; may escalate directly to Executive Management. The DPO does not approve, accept risk, authorise processing or determine anonymity]*** |
| ***[Processing Owner]*** | ***[Decides on acceptance of residual risk up to the delegated tier (Document 8, Section 5); records reasons where the decision departs from DPO advice]*** |
| ***[Member of Executive Management / Privacy Risk Committee (under written delegation)]*** | ***[Decides on High residual risk, as the single decider designated by the delegation in force (Document 8, Section 5)]*** |
| ***[IT / Information Security]*** | ***[Provides the infrastructure for attack simulation and metric computation; evidences security controls used in L3]*** |

## **6. Relationship to Other Framework Documents**

* Relies on the Privacy Risk Appetite Statement (Document 8) — tier scales, the residual-risk matrix, the acceptance authority and any cumulative disclosure budget; this document calibrates the factors, metrics, thresholds and weights that Document 8 deliberately does not set.

* Relies on the Data Classification Policy (Document 10) — data class and special categories (Factor B).

* Relies on the Regulatory Applicability Matrix (Document 7) — applicable regimes for track (b) (Factor F) and legal facts used by G-L.

* Relies on the Consent Management Policy (Document 13) only through G-L (validity of consent where it is the lawful basis); consent is not a severity or likelihood factor.

* Relies on the Privacy Automation & Tooling Strategy (Document 9) — the single connection point between this tool-independent method and any technical implementation.

* Is applied within the DPIA Methodology (Document 19) as the risk calculation core, and within the TIA Methodology (Document 20) only for the calculation elements Document 20 requests; the legal transfer assessment remains in Document 20.

* Provides evidence (PET Assessment Module) to the Data Retention & Disposal Policy (Document 11), the Cross-Border Data Transfer Policy (Document 12), the Privacy by Design & by Default Policy (Document 16) and the Vendor / Third-Party Privacy Risk Policy (Document 17); the legal conclusions in those documents remain the controller's, with DPO advice.

* Interacts with the Data Breach Response Policy (Document 14) — the severity factors (Section 3.4) may be reused to describe the severity of an incident; Document 14 owns the breach definitions and the Art. 33/34 notification tests.

* Passes results to the Privacy Risk Register (Document 22) and the RoPA (Document 21).

* Defines the parameter space for Risk Calculation Projects developed under Calculation Project Development (C1) and applied in Request & Transformation (C2) of the Privacy Governance Process Map (Document 24). The register of active projects is maintained through each project's passport (Section 4.1); no separate register is created.

## **7. Review and Amendment**

This document is reviewed under the continuous improvement principle (Document 2, Privacy Governance Charter) and the Policy Review Cycle (Document 29), and also when a new PET or attack class appears, when the threat landscape changes materially, when guidance changes (for example, adoption of final EDPB guidelines on anonymisation), or when the Document 8 scales are revised. Each review includes a sensitivity analysis of the severity and likelihood band cut-points. Changes are adopted by ***[Executive Management]*** on the proposal of the ***[EPPO]***, after consulting the ***[Privacy Risk Committee]*** and the DPO.

Creating a new Risk Calculation Project, or changing the configuration of an existing one (weights, thresholds, metrics, factors), is a versioned change approved by the ***[EPPO]***; it does not require a full review of this document unless it affects the architecture (Section 3.1). A change to defaults does not retroactively revise decisions already made: reproducibility is ensured by retaining the configuration version in force at the time of the decision (Section 4.5).

A completed calculation becomes obsolete, and is re-run, upon a material change in the data, the recipients or parties, the threat landscape or the auxiliary data available to attackers; when a pilot moves to production; on expiry of a conditional acceptance; and on expiry of the review period in the project passport. For released artefacts, the periodic re-assessment of Section 3.3.0 applies. A decision based on an obsolete calculation is not valid for the changed case.

## **8. Approval**

This document was adopted by ***[Executive Management]*** on ***[date]***. Document owner: ***[EPPO]***. DPO advice: ***[reference]***.

# **Part B — Worked Example: PanEuropean Bank AG**

**PanEuropean Bank AG — Privacy Risk Assessment Methodology**

*Effective Date: 20 October 2026  ·  Version: 1.2  ·  Document Owner: Chief Privacy Officer (EPPO)  ·  Adopted by: Management Board*

*Fictional legal entity, provided solely for illustrative purposes.*

# **Fictional Document History (illustrative)**

| Version | Date | Changes |
| :---- | :---- | :---- |
| 1.0 | 1 March 2026 | First version of the methodology: two-track model, threat-based likelihood, PET Assessment Module with failure gates, four Risk Calculation Projects. Owner at the time: Group DPO |
| 1.1 | 22 August 2026 | Linked the privacy-loss ledger to the cumulative disclosure budget introduced in the Privacy Risk Appetite Statement (Document 8, version 2.0). Owner at the time: Group DPO |
| 1.2 | 20 October 2026 | Re-baselined to the new role model on the creation of the Chief Privacy Officer (EPPO) position: the Chief Privacy Officer becomes owner and approves project configurations; the Group DPO's role limited to advice; acceptance by the single decider under Document 8, version 3.0; lifetime privacy-loss ledger with an operational annual cap |

## **Glossary of Terms**

*This table lists only terms defined by this document itself; terms defined in another PGF document are not repeated here. The Part A glossary applies; the entries below add PanEuropean specifics.*

| Term | Definition / Reference |
| :---- | :---- |
| Risk Calculation Project | A versioned configuration of the methodology for a PanEuropean processing case: archetype, harm scenarios, likelihood factors, PET-module metrics, thresholds and gates, severity scores and weights. Structure — Section 4. |
| Pseudonymisation | As in Part A (Art. 4(5)). At PanEuropean, tokenised customer identifiers used in analytics are pseudonymised data and remain personal data; they are assessed as archetype 1 or 4, never as archetype 2. |
| Anonymous information | As in Part A (Recital 26). At PanEuropean, the conclusion is taken by the Processing Owner on Legal's assessment, with Group DPO advice, and is re-assessed at least annually. |
| Data Synthesis | As in Part A. At PanEuropean, synthetic datasets are generated on the Bank's privacy engineering platform (PEP, illustrative) and remain within the scope of personal-data controls until a documented anonymity conclusion is taken. |
| Federated Learning | As in Part A. Used in the anti-fraud consortium with other EU banks (Section 3.3.3). |
| SMPC | As in Part A. Addressed within Section 3.3.3. |
| PEP | The Bank's privacy engineering platform (PEP, illustrative) — a fictional internal platform on which the Bank runs the calculations of this methodology. The methodology does not depend on PEP; the connection to tooling is governed by Document 9. |

## **1. Purpose**

Defines PanEuropean Bank AG's methodology for assessing privacy risk: harm scenarios on two tracks, threat-based likelihood, the PET Assessment Module and the severity factors. Calculations are run on the Bank's privacy engineering platform (PEP, illustrative) in accordance with the Privacy Automation & Tooling Strategy (Document 9); the methodology itself is tool-independent. The decision on acceptance of a calculated residual risk is taken under PanEuropean's Privacy Risk Appetite Statement (Document 8), after the legal compliance gate.

## **2. Scope**

The methodology is applied for every DPIA (Document 19) and for every release, sharing or transfer of a de-identified, synthetic, aggregate or federated artefact (Documents 11, 12, 16, 17). For transfer impact assessments (Document 20) and vendor due diligence (Document 17), it supplies only the calculation elements those documents request; the legal transfer assessment under the mechanism used (Art. 45, 46 or 49) and the decision whether a transfer may start remain in Document 20. The severity factors are reused by Document 14 to describe incident severity; Document 14 owns the Art. 33/34 tests. Unstructured data and the Bank's LLM-based customer-service assistant are assessed with the threat-based model and severity factors only; no PET-module disclosure test for unstructured data is claimed.

**Gates.** The sequence G-L → G-DPIA → calculation → G-36 → acceptance of Part A, Section 2.1, applies unchanged. At PanEuropean, G-L is run by Legal & Compliance; the G-36 legal conclusion is recorded by Legal & Compliance with Group DPO advice; the competent supervisory authority for prior consultation is the lead supervisory authority, the Hessian Commissioner for Data Protection and Freedom of Information (HBDI). BaFin and the ECB are financial supervisors and are not consulted under Art. 36.

## **3. Catalogue of Metrics and Factors (PanEuropean)**

This section is the catalogue from which PanEuropean's Risk Calculation Projects (Section 4) draw. The thresholds are the catalogue defaults; a project may set a stricter threshold, or a different one with documented justification (Section 4).

## **3.1 Architecture of the Methodology**

PanEuropean applies the Part A architecture: two tracks, harm scenarios covering all seven harm types of Factor A, threat-based likelihood for identified processing, and the PET Assessment Module for de-identified, synthetic, aggregate and federated artefacts. The Bank maintains four Risk Calculation Projects (Section 4). No project is an automatic substitute for cases outside its scope: applying a project to a case requires a documented justification that the case fits the project's scope.

## **3.2 Likelihood — Threat-Based Model and Base-Dataset Diagnostics**

PanEuropean applies the four likelihood factors of Part A, Section 3.2, with the following anchors:

| Factor | PanEuropean anchors (examples) |
| :---- | :---- |
| L1 — Exposure | 0: machine-only pipeline or "white room" with no direct human access; 1: access by named Privacy Engineers or credit officers; 2: routine access across a business line, or access by a processor/partner; 3: every customer or applicant affected systematically (e.g. automated credit decisions), or public access |
| L2 — Threat source | 1: accidental error by vetted staff; 2: opportunistic insider, or known error modes of a scoring model (drift, proxy variables); 3: organised fraud groups targeting bank data, or a known systematic bias mode not yet excluded |
| L3 — Control gap | Evidence from the Bank's register of technical and organisational measures: access control and "white room" regime, encryption, logging, tested incident-response plan for the processing (Document 14), Art. 28 data processing agreement or Art. 26 arrangement with due-diligence status (Document 17), human review and contestation (Art. 22(3); Document 15), bias testing and independent model validation |
| L4 — Event history | 1: incidents in comparable processing reported in the sector; 2: events or near misses in PanEuropean's own processing within the last 24 months |

Likelihood index bands, the override rule and the inherent/residual distinction are as in Part A. Consent or another lawful basis never lowers likelihood.

**Base-dataset disclosure diagnostics (archetype 1).** Computed on the quasi-identifier view of a base dataset (direct identifiers removed), as a baseline for PET planning. They are not the likelihood of any scenario concerning the base dataset.

Re-identification proxy metrics:

| Metric | What It Measures | Default threshold |
| :---- | :---- | :---- |
| k-Anonymity Level | Minimum size of an equivalence class on the quasi-identifiers | k ≥ 5 |
| l-Diversity Level | Diversity of sensitive-attribute values within each class | l ≥ 3 |
| t-Closeness | Distance between the sensitive-attribute distribution in a class and in the whole dataset | t ≤ 0.15 |
| Uniqueness Rate | Share of records unique on their quasi-identifiers | < 1% |
| Replay Rate | Share of records recurring identically across releases/versions of the dataset | < 0.01 |

Attack battery mapped to the WP216 criteria:

| WP216 Criterion | Attack | Metric | Default threshold |
| :---- | :---- | :---- | :---- |
| Singling out | Singling-out test | singling\_out\_rate | < 1% |
| Singling out | Outlier disclosure — isolating a record through atypical values | outlier\_disclosure\_rate | Set per project |
| Singling out / Linkability | Deterministic linkage | det\_linkage\_rate | < 1% |
| Linkability | Fellegi-Sunter probabilistic linkage | linkage\_precision@100 | < 5% |
| Linkability | k-NN re-identification | knn\_linkage\_success | < 10% |
| Linkability | Clustering disclosure — linkage through membership in an isolated group | clustering\_disclosure\_rate | Set per project |
| Inference | Categorical ZCAP (CAP family), reported as advantage over the prior attribute distribution | zcap\_advantage | < 0.10 |
| Inference | Normalised information gain, 1 − H(S\|Q)/H(S) | inference\_info\_gain | < 0.30 |
| Inference | ML inference attack, advantage over a baseline model without quasi-identifiers | inference\_advantage | < 0.10 |

Deterministic linkage is mapped to both singling out and linkability: an exact match both isolates a record and links it to an external source. Outlier and clustering disclosure are assigned by substantive similarity of the risk measured. ZCAP measures attribute disclosure and is therefore an inference metric. The thresholds above are the Bank's illustrative defaults for a moderately resourced adversary using public or commercially available auxiliary data; they are not derived from a normative source, and meeting them does not by itself establish anonymity (Section 3.3.0).

## **3.3 PET Assessment Module**

### **3.3.0 Module Rules**

The Part A rules apply unchanged: results are evidence, not a legal safe harbour; anonymity is a contextual conclusion under Recital 26 relative to the recipient (C-582/14 *Breyer*; C-413/23 P *EDPS v SRB*); pseudonymised data remain personal data (EDPB Guidelines 01/2025); EDPB Guidelines 02/2026 on anonymisation are a public-consultation draft (8 July 2026) used as orientation only. Per-metric results, the failure gates G-M1 to G-M5, baseline-aware normalisation with its allowed domains, the disclosure indicator (not a probability), confidence intervals and the module outcome table apply as in Part A. For attack metrics, PanEuropean uses at least 5,000 evaluation records per class (members and non-members, or training and control records) and five repetitions, and reports a 95% confidence interval; the gate uses the unfavourable bound. The G-M2 attack set is defined in each project passport; unless a project states otherwise, the unacceptable-success level of an attack is the threshold of the corresponding metric in Sections 3.2 and 3.3.2–3.3.4, and two qualitative paths are unacceptable regardless of rate: an exact copy of a source record in a synthetic release (DCR = 0), and a published cell or combination of cells that attributes a sensitive value to fewer than 10 identifiable persons. G-M3 at PanEuropean: as **internal policy** (stricter than the legal test), health-related and other special-category attributes are excluded from every open release; separately, a release that would disclose identifiable special-category data without an applicable Art. 9(2) condition fails G-L. Every anonymity conclusion for a released artefact is re-assessed at least annually and upon any new release from the same source population.

### **3.3.1 De-identification of Records**

The proxy metrics and attack battery of Section 3.2 are applied to the transformed record-level dataset after de-identification; all three WP216 criteria are tested. Each project designates its mandatory (gated) metrics. Tokenised or hashed identifiers are pseudonymisation and are never assessed under this subsection as anonymisation.

### **3.3.2 Data Synthesis**

| Metric | What It Measures | Default threshold |
| :---- | :---- | :---- |
| MIA accuracy (balanced evaluation set; shadow-model attack) | Whether an attacker can tell if a record was in the generator's training data; normalised as advantage 2 × \|accuracy − 0.5\| (orientation-invariant; the gate uses the effective accuracy 0.5 + \|accuracy − 0.5\|) | < 60% (advantage < 0.20) |
| MIA AUC-ROC (loss-based attack) | The same, threshold-free | < 0.60 |
| MIA TPR at FPR = 0.1% | Exposure of the most vulnerable records | ≤ 1.0% (gate only) |
| DCR P5 | 5th percentile of the distance from synthetic records to the closest training record, compared with the same statistic for a holdout of real records | ≥ holdout baseline (project value) |
| NNDR median | Ratio of distances to the nearest and second-nearest training record | > 0.70 |
| Linkability advantage | Bank test procedure TP-SYN-LINK (illustrative): linkage of synthetic records to an auxiliary dataset representing attacker knowledge, success on training records minus success on a control set | ≤ 0.05 (gate only) |
| Attribute-inference advantage | Bank test procedure TP-SYN-INF (illustrative): inference of a secret attribute for training records versus a control set | ≤ 0.05 (gate only) |
| ε (generator, at the configured δ) | Formal DP guarantee of training (DP statement, Section 3.3.5) | ≤ 3.0 (configuration gate) |
| δ (configured) | Additive term of approximate DP, fixed by design | Set by the project with stated n, privacy unit and accountant (engineering heuristic: well below 1/n) |

TP-SYN-LINK and TP-SYN-INF are the Bank's own documented test procedures, following the published approach of comparing attack success on training records with success on a control set. Reconstruction of training records from the generator's parameters (model inversion) is not tested by the Bank. The limitation is recorded in every evidence pack and mitigated by keeping the generator's parameters inside the PEP environment, accessible only to named Privacy Engineers; only the synthetic dataset leaves that environment.

### **3.3.3 Federated Learning**

The only federated scheme is the anti-fraud consortium with other EU banks (Cross-Border Data Transfer Policy, Document 12; evidence pack EVP-2026-0041). Each bank's customer data stay with that bank; model updates leave it. The consortium members assess their joint-controllership arrangement under Art. 26; federated learning does not change the legal status of the data or of the updates. The project passport records the training inputs and labels and the G-L conclusion on Art. 10 (Document 19, DPIA-FL-01): only the customer's own transaction attributes and victim-side labels for confirmed unauthorised transactions are used; labels that attribute or suggest an offence by the customer, and counterparty identifiers, are excluded. Any change to the inputs re-opens G-L and the Factor B assessment.

| Metric / control | Default threshold |
| :---- | :---- |
| ε for the whole training (all rounds composed), per customer of a participating bank, at the configured δ | ≤ 3.0 (configuration gate) |
| δ (configured) | Set with stated n (customers of the participating bank), privacy unit and accountant |
| Secure aggregation — the coordinator sees only the aggregate update | Required (control) |
| MIA on the final consortium model (balanced set) | AUC < 0.60 |
| Gradient-reconstruction test on updates | Not available at the Bank — documented limitation |

Because no validated gradient-reconstruction test is available, the Bank does not claim a measured result for that attack class. In the project passport the test is classified as not applicable for the observers in scope, not as passed: validated secure aggregation and access restriction mean that no consortium member and no coordinator can observe an individual bank's updates, so the threat that the test addresses is excluded for them by control; the residual threat from aggregate updates and the final model is covered by the DP guarantee across all rounds and by the mandatory MIA test on the final model. The mandatory set is therefore: the DP configuration gates, validated secure aggregation, and the MIA test. If the validation of secure aggregation lapses, or an observer gains access to individual updates, the gradient-reconstruction test becomes mandatory and the module outcome is INCOMPLETE (G-M5) until evidence exists. Its decision on the consortium rests on the legal assessment (lawful basis, Art. 26 arrangement, Chapter V where relevant — Documents 12 and 20), the DP statement across all rounds, secure aggregation and restricted access to updates, with the limitation recorded in EVP-2026-0041.

### **3.3.4 Aggregate Statistics and Tabular Releases**

| Check | Default gate |
| :---- | :---- |
| Minimum cell size after suppression | ≥ 10 persons (illustrative internal SDC setting, calibrated to the release context; not an anonymity guarantee) |
| Differencing check within the release and against all previous releases from the same population | No derivable cell below 10 |
| Reconstruction test (exact reconstruction of source records from the published tables) | ≤ 1% of source records |
| Record-level attack battery on reconstructed records (Section 3.2 attack battery) | Project thresholds |
| Prohibited-attribute check | No health-related or other special-category attribute in an open release — PanEuropean internal policy (G-M3); a release disclosing identifiable special-category data without an Art. 9(2) condition would also fail G-L |
| Test scope | Every published table is within the scope of the checks above; a table outside the scope makes the module INCOMPLETE (G-M5) |

### **3.3.5 Differential Privacy Statements**

Every DP claim at PanEuropean carries the DP statement of Part A, Section 3.3.5. The Bank uses person-level privacy units (all records of one customer), with a per-customer contribution bound, and add/remove adjacency. The configured δ is chosen with a stated population n; as an engineering heuristic, the Bank sets δ ≤ 1/(100·n). This is an internal configuration choice, not a legal test and not evidence of anonymity. The relationship between ε and observed membership-inference results is stated as in Part A: the bound (e^ε + δ)/(1 + e^ε) on the accuracy of a membership test (uniform prior, adjacent datasets, worst-case attacker) is reported for information only and does not enter any score.

### **3.3.6 Repeated Releases and Cumulative Disclosure**

The Privacy Operations Lead keeps a lifetime privacy-loss ledger per source population (for example, the retail customer population) and per privacy unit, recording ε and δ, the accountant and the observers of each run; there is no calendar reset. Every mechanism run on source data is recorded, including runs used for model selection, previews and failed or cancelled runs whose outputs were observable; copies and post-processing of a released DP output are not charged again. Cumulative values are computed by basic composition (sum of ε, sum of δ) unless every run's accounting state allows a tighter, compatible method. All runs on the retail customer population are composed as if one party had observed all outputs, because the observer sets (consortium members, Data Science, Privacy Engineers) cannot be shown to be unable to combine them. A release that would exceed the lifetime budget or the operational annual cap set in Document 8, Section 3, fails the module (G-M4). Every new aggregate release is checked for differencing against all earlier releases from the same population.

## **3.4 Severity Assessment Factors and Organisational Consequences**

PanEuropean applies Factors A–G of Part A, Section 3.4, with the following values and examples. The severity index is w\_B·B + w\_C·C + w\_D·D + w\_E·E + w\_G·G per scenario (floor 0); Factor A is a tag; Factor F is reported separately as track (b). Severity floors and the no-double-counting rule apply.

### **Factor A — Harm Type (mandatory tag)**

| Value | Score | PanEuropean examples |
| :---- | :---- | :---- |
| Unlawful processing / loss of control | tag | Re-use of scoring data for marketing; profiling beyond the consented scope |
| Discrimination / adverse automated decision | tag | Unjustified credit refusal or worse terms; bias through proxies for protected characteristics |
| Financial loss | tag | Higher cost of credit after an erroneous score; fraud losses |
| Identity fraud | tag | Account opening with stolen KYC data |
| Reputational and social harm | tag | Disclosure of debt or arrears to the person's community |
| Physical, psychological, chilling effects, exclusion | tag | Distress after disclosure of financial difficulty; exclusion from essential banking services |
| Loss of confidentiality, integrity or availability | tag | Disclosure of transaction data; corrupted bureau data; loss of access to accounts |

### **Factor B — Intensity per Data Subject**

**Data Class** (Data Classification Policy, Document 10, Section 4.2):

| Value | Score | Explanation |
| :---- | :---- | :---- |
| Public | 0 | Public tariffs and product descriptions — non-personal data |
| Internal | 1 | Internal operating regulations — non-personal data |
| Confidential | 2 | Customer data (name, address, contact details), transaction data |
| Restricted | 3 | Credit-scoring data, anti-fraud features, identity documents |

Age modifier: −1 for retrospective data older than 5 years where the harm depends on currency; not for special-category data or identity documents. Synthetic data receive no data-class reduction.

**Special Categories of Data** — as in Part A, the modifier covers special-category data (Art. 9) and criminal-offence data (Art. 10). Special categories: health data provided when arranging payment protection insurance (PPI); biometric data used for authentication. Criminal-offence data: records that relate identifiable persons to alleged or established offences, such as fraud-case records (Document 10, Part B, Section 4.2) and the matches of the anti-fraud matching with the partner bank against its list of identities linked to confirmed fraud (Document 19, DPIA-PSI-01):

| Value | Score | Explanation |
| :---- | :---- | :---- |
| Present in the data concerned by the scenario | +2 | Heightened, qualitatively different harm |
| Absent | 0 | Factor does not apply |

**Data Subject Vulnerability** — PanEuropean recognises customers on its register of financially vulnerable persons (Vulnerable Customer Policy, internal) and minor product holders:

| Value | Score | Explanation |
| :---- | :---- | :---- |
| The scenario does not specifically affect vulnerable persons | 0 | Factor does not apply |
| The scenario's harm falls on, or is aggravated for, customers on the register of financially vulnerable persons (e.g. credit refusal), or discloses the vulnerability marker | +1 | Limited ability to protect their own interests |
| The scenario affects minor product holders | +2 | Children merit specific protection |

### **Factor C — Scale**

| Number of affected persons | Score |
| :---- | :---- |
| < 100 | 0 |
| 100 – 9,999 | 1 |
| 10,000 – 999,999 | 2 |
| ≥ 1,000,000 | 3 — up to the whole customer base (about 1.2 million retail customers, illustrative) |

Source aggregation: +1 where the data combine two or more independent sources (for example, application data + EuroCredit Bureau data + transaction history; data flow map, Document 23). Pilots receive no separate discount; their scale is scored as it is.

### **Factor D — Reach / Containment**

| Value | Score | Explanation |
| :---- | :---- | :---- |
| Data or effect remain within PanEuropean | 0 | Full direct control |
| Data shared with a partner, processor or other recipient (e.g. the anti-fraud consortium; an advertising partner) | +1 | Partial loss of direct control |
| Open, unconditional publication (PanEuropean open-data portal) | +2 | Unbounded audience; practically irreversible |

The quality of the recipient's contractual and factual control (Document 17) and the readiness of a tested incident-response plan (Document 14) are assessed under likelihood factor L3, not here.

### **Factor E — Automated Decision-Making with a Significant Effect**

Applies to scenarios whose harm is produced through PanEuropean's automated credit decision (Art. 22; C-634/21 *SCHUFA*), or through corrupted data feeding it: +2. Does not apply to pure disclosure scenarios, including disclosure of the data used to train the scoring model.

### **Factor F — Organisational Consequences (Track (b))**

| Subfactor | Value | Score |
| :---- | :---- | :---- |
| Applicable regime | High-risk AI system under the AI Act, Annex III point 5(b) (creditworthiness assessment; high-risk obligations apply from 2 December 2027) | +1 |
| Financial and operational impact | Per the Bank's ERM scale for "Conduct & Privacy Risk" (Document 3) | 0 – 3 |
| Reputational impact | Per the Bank's ERM scale | 0 – 3 |
| Regulatory sandbox | PanEuropean takes part in no sandbox as of the date of this document | 0 |

The track (b) level is reported to the Chief Risk Officer's ERM function and never offsets the track (a) tier.

### **Factor G — Data Provenance and Reasonable Expectations**

| Value | Score |
| :---- | :---- |
| Direct collection (product application, onboarding) with clear, specific notice (Document 1) | 0 |
| Direct collection, purpose described vaguely | +1 |
| EuroCredit Bureau data (independent controller; regulated source expected by customers; Art. 14 information given) | 0 |
| Third-party source outside customers' typical expectations | +1 |
| Scraping of public profiles — identifies the customer, same context | +1 |
| Scraping of public profiles — identifies the customer, recontextualised | +2 |
| Third party without notice or without a lawful basis | GATE — G-L failure |
| Other / unattributed provenance | GATE — calculation not complete |

Provenance is attributed in the project passport (Sections 4.A.1–4.D.1) with reference to the "Data Source" field of the RoPA (Document 21).

## **3.5 Other Metrics (Data Quality and Utility)**

These metrics assess the quality and utility of data after a PET has been applied. They are calculated on PEP but do not enter the privacy risk calculation (Sections 3.2–3.4), and high utility never compensates for privacy risk. Which metrics apply, and with which thresholds, is set per project (Sections 4.A.6–4.D.6).

Quality/fidelity metrics — preservation of the statistical properties of the data after transformation:

| Metric | What It Measures | Default threshold |
| :---- | :---- | :---- |
| KS Statistic | Maximum divergence between empirical distribution functions per column | < 0.1 (per column) |
| JS Divergence | Symmetric measure of distribution divergence per column | < 0.1 (per column) |
| Wasserstein Distance | "Transport cost" of moving one distribution into another | Context-dependent |
| KL Divergence | Asymmetric measure of distribution divergence | Lower is better |
| Pearson Correlation R² | Preservation of linear correlation between pairs of features | > 0.9 |
| Correlation Matrix Diff | Divergence between the full correlation matrices of the original and transformed data | Low divergence |
| PCA Distance | Divergence in principal-component structure | Context-dependent |

Utility metrics for structured data (metrics for unstructured data are outside the scope of this document):

| Metric | What It Measures | Default threshold |
| :---- | :---- | :---- |
| ML F1 Delta (TSTR) | Quality of a model trained on transformed data relative to a model trained on the original data (train-synthetic-test-real) | > 0.8 of the original model |
| AUC Delta | The same, for AUC-ROC | Context-dependent |

## **4. Privacy Risk Calculation Projects**

PanEuropean maintains four Risk Calculation Projects, each for a business case with its own configuration. Not every catalogue element applies to every project. Numerical examples are in the Appendix to Part B. For every project, the matrix used in Step 3 of Section 4.4 is the residual-risk matrix of PanEuropean's Privacy Risk Appetite Statement (Document 8, Section 4), and acceptance follows Document 8, Section 5.

# **Project 1 — Base Dataset Assessment (identified data, before a PET decision)**

## **4.A.1 Purpose and Project Characteristics**

* Purpose — assessing the rights-and-freedoms risk of an identified or pseudonymised dataset that is used internally before a decision on a PET (for example, during an internal audit by Privacy Engineers), or for which no PET is planned for the dataset as such; and recording base-dataset disclosure diagnostics as an input to PET planning. The project is also used for periodic re-assessment of deployed internal processing of such a dataset. When a PET is later applied (Projects 2 or 3), this calculation and its evidence pack are carried into the receiving project's evidence pack as the record of the pre-PET state.

* Scope — structured PanEuropean datasets not yet transformed by a PET, whether at the preliminary stage or already deployed. Not used for de-identified, synthetic or aggregate releases (Projects 2–3) or for identified processing whose permanent purpose is a business decision or customer contact (Project 4).

* Technology — no PET; threat-based likelihood (Section 3.2); diagnostics with the attack battery of Section 3.2.

| Characteristic | Value |
| :---- | :---- |
| Project owner | Privacy Operations Lead (configuration approved by the Chief Privacy Officer; Group DPO advice recorded) |
| Configuration version | 1.1 (version 1.0 of 1 March 2026 was approved by the Group DPO under the arrangements then in force) |
| Review cadence | Annually and upon a material change in the data, the circle of persons with access, or the threat landscape |
| Effective date | 20 October 2026 (configuration 1.1, re-approved by the Chief Privacy Officer on re-baselining) |
| Archetype | 1 — base dataset (Section 3.1) |
| G-L record | The G-L record of the processing for which the dataset is held (for the audit sample: RoPA record of the credit-scoring processing, Document 21; the audit purpose is compatible under Art. 6(4) and covered by the Bank's internal audit function) |
| Harm scenarios | S1 — unauthorised disclosure or misuse of the audit sample by persons with access (loss of confidentiality; identity fraud; financial loss). Other harm types not relevant: no decision about individuals is taken on the audit sample (no discrimination/ADM scenario); no publication |
| Weight vector (w\_B, w\_C, w\_D, w\_E, w\_G) | (1, 1, 1, 1, 1) — default |
| Diagnostic alert mode | Lenient — diagnostics only; values above default thresholds are logged for the Privacy Operations Lead and taken into account in PET planning |
| Data provenance attribution (Factor G) | Direct collection from the customer when applying for credit (RoPA, Document 21) |
| Vulnerable categories | As in Section 3.4 |

## **4.A.2 Likelihood**

**Threat-based (S1).** The four factors of Section 3.2 are assessed for each case; examples in the Appendix (Examples 1.1, 1.2).

**Base-dataset disclosure diagnostics.** All seven attack metrics of the Section 3.2 battery are computed on the quasi-identifier view at the default thresholds. They do not determine the likelihood of S1.

| WP216 Criterion | Metric | Metric weight | Threshold | Difference from the default |
| :---- | :---- | :---- | :---- | :---- |
| Singling out | Singling-out rate | 0.35 | 1% | Matches the default |
| Linkability | Deterministic linkage rate | 0.1167 | 1% | Matches the default |
| Linkability | Fellegi-Sunter precision@100 | 0.1167 | 5% | Matches the default |
| Linkability | k-NN linkage success | 0.1167 | 10% | Matches the default |
| Inference | ZCAP advantage | 0.10 | 0.10 | Matches the default |
| Inference | Normalised information gain | 0.10 | 0.30 | Matches the default |
| Inference | ML inference advantage | 0.10 | 0.10 | Matches the default |

| Step | Description |
| :---- | :---- |
| Step 1 — Per-metric results | Each metric reported with its 95% confidence interval |
| Step 2 — Normalisation | All seven metrics have a zero baseline: normalised value = value / threshold |
| Step 3 — Weighting | Category weights: singling out 0.35, linkability 0.35, inference 0.30; equal shares within a category |
| Step 4 — Disclosure indicator | Σ (normalised value × weight) — a diagnostic summary, not a probability; values ≥ 1.0, or any metric above its threshold, mean that the dataset would need substantial transformation before any release |

## **4.A.3 Severity**

| Factor | Subfactor | Score for the project | Difference from the default |
| :---- | :---- | :---- | :---- |
| A | Harm type | Loss of confidentiality; identity fraud; financial loss | Tag |
| B | Data class | Per the catalogue | Matches the default |
| B | Special categories of data | +2 where present | Matches the default (the exposure of a wider circle of staff is reflected in likelihood, not here) |
| B | Data subject vulnerability | Per the catalogue | Matches the default |
| C | Number of affected data subjects | Per the catalogue (size of the audit sample) | Matches the default |
| D | Base tier | Within PanEuropean = 0 | Matches the default |
| E | Automated decision-making | 0 — no decision is taken on the audit sample | Matches the default |
| G | Data provenance | 0 (direct collection, clear notice) | Matches the default |
| F (track (b)) | Organisational consequences | Assessed separately per case | Not part of the index |

Severity index = B + C + D + E + G (default weights), mapped with the intervals of Part A, Section 4.3 (index < 3.5 Minor; 3.5 to < 6.5 Moderate; 6.5 to < 8.5 Significant; ≥ 8.5 Catastrophic — with default weights 0–3, 4–6, 7–8, ≥ 9); severity floors apply.

## **4.A.4 Final Residual Risk Level**

| Step | Description |
| :---- | :---- |
| Step 0 — G-L | Confirm the G-L record; any processing outside it (for example, special-category data without an Art. 9(2) condition for the audit purpose) is a G-L failure — stop and remediate |
| Steps 1–3 | Likelihood (4.A.2) and severity (4.A.3) of S1 mapped through the Document 8 matrix |
| Step 4 — PET outcome | Not applicable (no release) |
| Step 5 — Track (a) tier | The S1 tier |
| Step 6 — Project rules | None |
| Step 7 — G-36 | Evaluated where the processing is subject to a DPIA |
| Step 8 — Acceptance | Per Document 8, Section 5 |
| Step 9 — Track (b) | Reported separately |

## **4.A.5 Traceability and Evidence Pack**

The evidence pack (Section 4.5 of Part A) contains: Block 0 — G-L record; Block 1 — archetype 1, scenario S1 and the relevance statement for the other harm types, weight vector, alert mode, provenance; Block 2 — L1–L4 for S1 with evidence for L3, and the seven diagnostic metrics with confidence intervals and the disclosure indicator; Block 3 — Factors B–G for S1 and the track (b) level; Block 4 — tier, G-36 conclusion where applicable, Group DPO advice where a DPIA exists or the tier is Medium or above, and the decision of the single designated decider.

## **4.A.6 Other PET-Application Metrics**

Not applicable — no PET has been applied. Quality and utility metrics (Section 3.5) are calculated in Projects 2 and 3.

# **Project 2 — Synthetic Dataset for Model Calibration**

## **4.B.1 Purpose and Project Characteristics**

* Purpose — assessing the disclosure risk of a synthetic dataset generated with a differentially private generator (DP-CTGAN) from credit-scoring data, before it is made available to Data Science for calibrating the credit-scoring model (Privacy by Design & by Default Policy, Document 16). This project is the calculation core of DPIA-CS-TRAIN-01 (Document 19).

* Scope — synthetic datasets derived from credit-scoring data; not record-level de-identified or aggregate releases (Project 3), not federated-learning artefacts (Section 3.3.3).

* Technology — data synthesis (Section 3.3.2), with DP training (Section 3.3.5).

| Characteristic | Value |
| :---- | :---- |
| Project owner | Privacy Operations Lead (configuration approved by the Chief Privacy Officer; Group DPO advice recorded) |
| Configuration version | 1.1 (version 1.0 of 1 March 2026 was approved by the Group DPO under the arrangements then in force) |
| Review cadence | Annually, upon retraining with an architecture change, and upon any new synthetic release from the same source population |
| Effective date | 20 October 2026 (configuration 1.1, re-approved by the Chief Privacy Officer on re-baselining) |
| Archetype | 3 — synthetic data (Section 3.1) |
| G-L record | Credit-scoring processing (RoPA record for model training, Document 21); lawful basis and purpose compatibility of model calibration confirmed by Legal & Compliance |
| Harm scenarios | S1 — disclosure of information about source customers through the synthetic dataset (membership, linkage, attribute inference) — PET Assessment Module. S2 — misuse of the source data or of the generator's parameters by persons with access inside PEP — threat-based. The fairness of decisions made with the calibrated model is assessed in the scoring scenario of Project 4 (Example 4.3), not here |
| Adversary profile × disclosure channel | Moderately resourced insider or contractor in Data Science with access to the synthetic dataset and to public or commercially available auxiliary data — matches the default |
| Mandatory (gated) metrics | MIA accuracy, MIA AUC, MIA TPR at FPR = 0.1%, DCR P5, NNDR median, linkability advantage (TP-SYN-LINK), attribute-inference advantage (TP-SYN-INF), ε, configured δ |
| Unacceptable attacks (G-M2) | Membership inference — baseline: chance on a balanced member/non-member set; unacceptable: upper 95% bound of accuracy ≥ 60%, of AUC ≥ 0.60, or of TPR at FPR 0.1% > 1.0%. TP-SYN-LINK and TP-SYN-INF — baseline: success on a control set of records not used in training; unacceptable: upper 95% bound of the advantage > 0.05. Qualitative: any exact copy of a training record (DCR = 0) |
| DP statement | Privacy unit: one customer (all records of the customer, contribution bound per customer); adjacency: add/remove one customer; mechanism: DP-SGD in the generator's training; accountant: Rényi DP; δ configured at 1×10⁻⁹ for a source population of about 1.2 million customers (engineering heuristic δ ≤ 1/(100·n)); output access: the synthetic dataset only — generator parameters and checkpoints stay in PEP; lifetime ledger and caps per Document 8, Section 3 (Section 3.3.6) |
| Weight vector (w\_B, w\_C, w\_D, w\_E, w\_G) | (1, 1, 1, 1, 1) — default |
| Diagnostic alert mode | Lenient for diagnostic metrics; all listed metrics are mandatory and gated |
| Data provenance attribution (Factor G) | Same source as Project 1 (direct collection at credit application) plus EuroCredit Bureau data (RoPA, Document 21) |
| Vulnerable categories | The vulnerability marker is not part of the source or synthetic dataset; the vulnerability score does not apply to S1/S2 |

* A synthetic dataset is a derived artefact that can disclose information about the people in the source data; the metrics of this project are a function of both datasets. The high utility of the synthetic dataset (Section 4.B.6) does not compensate for disclosure risk and is not part of the calculation.

## **4.B.2 Likelihood**

**S1 — PET Assessment Module.**

| Category | Metric | Weight | Project threshold | Difference from the default |
| :---- | :---- | :---- | :---- | :---- |
| Membership inference | MIA accuracy | 0.25 | < 60% (advantage < 0.20) | Matches the default |
| Membership inference | MIA AUC-ROC | 0.25 | < 0.60 | Matches the default |
| Membership inference | MIA TPR at FPR = 0.1% | Gate only | ≤ 1.0% | Matches the default |
| Memorisation | DCR P5 | 0.25 | ≥ 0.15 (holdout baseline for this source population) | Project value of the default rule |
| Memorisation | NNDR median | 0.25 | > 0.70 | Matches the default |
| Linkability | Linkability advantage (TP-SYN-LINK) | Gate only | ≤ 0.05 | Matches the default |
| Inference | Attribute-inference advantage (TP-SYN-INF) | Gate only | ≤ 0.05 | Matches the default |
| Formal DP | ε (at configured δ) | Gate only | ≤ 2.0 (instead of 3.0) | Stricter: the synthetic data calibrate a model used for automated credit decisions; the project chooses a tighter configuration than the default |
| Formal DP | δ (configured) | Gate only | 1×10⁻⁹ | Set from n ≈ 1.2 million with the heuristic of Section 3.3.5 |

| Step | Description |
| :---- | :---- |
| Step 1 — Per-metric results | All metrics with 95% confidence intervals |
| Step 2 — Failure gates | G-M1 (a metric outside its threshold on its unfavourable 95% bound); G-M2 (the attack set and qualitative paths of the passport); G-M4 (incomplete DP statement, or the Document 8 lifetime budget or annual cap exceeded); G-M5 (a missing or invalid result → INCOMPLETE) |
| Step 3 — Normalisation | MIA accuracy: \|accuracy − 0.5\| / 0.10 (equivalently advantage / 0.20); AUC: \|AUC − 0.5\| / 0.10; DCR P5: 0.15 / value (DCR = 0 fails G-M2 and is not normalised); NNDR: (1 − value) / 0.30 |
| Step 4 — Weighting | Membership inference 0.50, memorisation 0.50; equal shares within a category. ε and δ are gates and are not weighted |
| Step 5 — Disclosure indicator | Σ (normalised value × weight) — not a probability |
| Step 6 — Likelihood level | PASS, indicator < 0.5 → Low; PASS, 0.5 ≤ indicator ≤ 1.0 → Medium; INCOMPLETE → not assessed; FAIL → High, or Near-certain under the internal routing rule for a reproduced failure |

**S2 — threat-based.** L1 = 1 (named Privacy Engineers in the "white room"), L2 = 1 (accidental or low-capability misuse), L3 = 0 residual (white-room regime and logging tested; evidence in the Bank's register of measures) / 3 inherent, L4 = 1 (sector events). Residual index 3 → Low; inherent index 6 → Medium.

Numerical examples — Appendix to Part B, Examples 2.1, 2.1-R and 2.2.

## **4.B.3 Severity**

| Factor | Subfactor | Project score | Difference from the default |
| :---- | :---- | :---- | :---- |
| A | Harm type | S1, S2: loss of confidentiality; financial loss; reputational harm | Tag |
| B | Data class | Restricted = 3 | Matches the default — credit-scoring data are Restricted (Document 10, Section 4.2); no reduction for synthesis |
| B | Special categories | 0 — none in the source data | Matches the default |
| B | Vulnerability | 0 — the marker is not in the data | Matches the default |
| C | Number of affected data subjects | > 1,000,000 = 3 (the source population) | Matches the default |
| C | Source aggregation | +1 (application data + EuroCredit Bureau data + transaction history) | Matches the default |
| D | Base tier | Within PanEuropean = 0 | Matches the default |
| E | Automated decision-making | 0 — S1 and S2 are disclosure scenarios; the effect of training data on credit decisions is assessed in Example 4.3 | Matches the default rule |
| G | Data provenance | 0 | Matches the default |
| F (track (b)) | Applicable regime | +1 — the calibrated model is a high-risk AI system (AI Act, Annex III point 5(b)) | Track (b) only |

Severity index for S1 and S2 = 3 + 0 + 0 + 3 + 1 + 0 + 0 + 0 = 7 → Significant (default weights).

## **4.B.4 Final Residual Risk Level**

| Step | Description |
| :---- | :---- |
| Step 0 — G-L | Confirmed (G-L record above) |
| Steps 1–3 | S1: module outcome (4.B.2) × Significant; S2: Low × Significant = Medium (residual), Medium × Significant = Medium (inherent) |
| Step 4 — PET outcome | If the module fails, the synthetic dataset may not be released to Data Science |
| Step 5 — Track (a) tier | Highest of S1 and S2 |
| Step 6 — Project rules | None |
| Step 7 — G-36 | Evaluated in DPIA-CS-TRAIN-01 |
| Step 8 — Acceptance | Per Document 8, Section 5 |
| Step 9 — Track (b) | Reported separately |

Numerical examples — Appendix to Part B, Examples 2.1, 2.1-R and 2.2.

## **4.B.5 Traceability and Evidence Pack**

PEP compiles the evidence pack for every calculation under this project, whatever the result: Block 0 — G-L record and the G-DPIA outcome (DPIA-CS-TRAIN-01); Block 1 — archetype 3, scenarios S1–S2, adversary profile, DP statement, gated metrics; Block 2 — every metric with value, threshold, normalised value, 95% confidence interval and pass/fail, each gate, the disclosure indicator, the module outcome, the privacy-loss ledger entry, and the documented limitation on model-inversion testing; L1–L4 for S2; Block 3 — Factors B–G and the track (b) level; Block 4 — tiers, the G-36 conclusion, Group DPO advice and the decision of the single designated decider.

## **4.B.6 Other PET Application Metrics**

| Metric | Project threshold | Difference from the default |
| :---- | :---- | :---- |
| ML F1 Delta (TSTR) | > 0.8 of the original model | Matches the default |
| Pearson Correlation R² | > 0.9 | Matches the default — important for the interpretability of the scoring model |

Both are reported in a separate block and do not affect Section 4.B.2.

# **Project 3 — Aggregate Statistics for the Bank's Open Data Portal**

## **4.C.1 Purpose and Characteristics of the Project**

* Purpose — assessing aggregated credit-portfolio statistics intended for publication on PanEuropean's open-data portal, and providing the evidence for the controller's conclusion whether the published statistics are anonymous information (Recital 26). The decision to publish is taken under the Privacy by Design & by Default Policy (Document 16); the same release is used in Document 14 as an incident-classification scenario.

* Scope — aggregate statistics for unconditional publication to an unlimited audience (archetype 2b). Not used for datasets with controlled internal access (Projects 1–2).

* Technology — aggregation with generalisation and small-cell suppression; SDC gates (Section 3.3.4); record-level attack battery applied to records reconstructed from the published tables.

| Characteristic | Value |
| :---- | :---- |
| Project owner | Privacy Operations Lead (configuration approved by the Chief Privacy Officer; Group DPO advice recorded) |
| Configuration version | 1.1 (version 1.0 of 1 March 2026 was approved by the Group DPO under the arrangements then in force) |
| Review cadence | Before every release, annually for the anonymity conclusion, and upon any change in the composition of published aggregates |
| Effective date | 20 October 2026 (configuration 1.1, re-approved by the Chief Privacy Officer on re-baselining) |
| Archetype | 2b — aggregate/tabular release (Section 3.1) |
| G-L record | Publication purpose and compatibility confirmed by Legal & Compliance. A release that would disclose identifiable special-category data without an applicable Art. 9(2) condition fails G-L; in addition, PanEuropean's **internal policy** excludes health-related and other special-category attributes from every open release (G-M3; stricter than the legal test) |
| Harm scenarios | S1 — identification of customers or disclosure of their credit attributes from the published statistics (singling out, linkability, inference, differencing, reconstruction) — PET Assessment Module. Handling of the source microdata during preparation is covered by Project 1 |
| Adversary profile × disclosure channel | Broad range of attackers, public channel, with public registers and social-network data as auxiliary sources — stricter than the default; the recipient of an open release is anyone |
| Mandatory (gated) metrics | All SDC gates of Section 3.3.4 and all seven attack metrics on reconstructed records |
| Unacceptable attacks (G-M2) | Reconstruction — baseline 0; unacceptable: highest value over five runs > 1% of source records. Differencing — qualitative: any derivable cell below 10. Record-level attacks on reconstructed records — unacceptable levels = the metric thresholds, on the upper 95% bound. Qualitative: any cell attributing a sensitive value to fewer than 10 persons. Every published table must be within the test scope (otherwise G-M5) |
| Weight vector (w\_B, w\_C, w\_D, w\_E, w\_G) | (1, 1, 1, 1, 1) — default |
| Diagnostic alert mode | Not used — all metrics are gated |
| Data provenance attribution (Factor G) | Direct collection from the customer (credit-portfolio data, same source as Project 1; RoPA, Document 21) |

* Generalisation and suppression reduce, but do not by themselves remove, disclosure risk. The controller's anonymity conclusion relies on the module result and on the legal assessment, not on the fact that aggregation was applied.

## **4.C.2 Likelihood**

**SDC gates** (Section 3.3.4): minimum cell size ≥ 10; no derivable cell below 10 within the release or against previous releases; exact reconstruction ≤ 1% of source records; no special-category attribute.

**Attack battery on reconstructed records:**

| WP216 Criterion | Metric | Weight | Project threshold | Difference from the default |
| :---- | :---- | :---- | :---- | :---- |
| Singling out | Singling-out rate | 0.20 | 0.5% (instead of 1%) | Stricter: open publication is irreversible and the audience unlimited |
| Linkability | Deterministic linkage rate | 0.1667 | 1% | Matches the default |
| Linkability | Fellegi-Sunter precision@100 | 0.1667 | 5% | Matches the default |
| Linkability | k-NN linkage success | 0.1667 | 10% | Matches the default |
| Inference | Normalised information gain | 0.10 | 0.30 | Matches the default |
| Inference | ML inference advantage | 0.10 | 0.10 | Matches the default |
| Inference | ZCAP advantage | 0.10 | 0.10 | Matches the default |

The linkability category weight (0.50) is higher than in Project 1 (0.35): for an open release, linkage to external sources is the primary attack vector.

| Step | Description |
| :---- | :---- |
| Step 1 — Per-metric results | All SDC checks and attack metrics with confidence intervals |
| Step 2 — Failure gates | Any SDC gate or attack metric outside its threshold on its unfavourable bound fails the module (G-M1/G-M2); an attribute excluded by internal policy fails G-M3; a table outside the test scope makes the module INCOMPLETE (G-M5); identifiable special-category data without an Art. 9(2) condition also fail G-L |
| Step 3 — Normalisation | All seven attack metrics have a zero baseline: value / threshold |
| Step 4 — Weighting | Singling out 0.20, linkability 0.50, inference 0.30; equal shares within a category |
| Step 5 — Disclosure indicator | Σ (normalised value × weight) — not a probability |
| Step 6 — Likelihood level | PASS, indicator < 0.5 → Low; PASS, 0.5 ≤ indicator ≤ 1.0 → Medium; INCOMPLETE → not assessed; FAIL → High, or Near-certain under the internal routing rule (e.g. a reconstruction failure reproduced in every run) |

Numerical examples — Appendix to Part B, Examples 3.1, 3.2 and 3.3.

## **4.C.3 Severity**

| Factor | Subfactor | Project score | Difference from the default |
| :---- | :---- | :---- | :---- |
| A | Harm type | Loss of confidentiality; reputational and social harm; financial loss | Tag |
| B | Data class | Restricted = 3 | Matches the default — credit-portfolio data (Document 10, Section 4.2) |
| B | Special categories | Per the catalogue — see Example 3.3 (identifiable health data without an Art. 9(2) condition: G-L failure) | Matches the default |
| C | Number of affected data subjects | > 1,000,000 = 3 (the whole credit portfolio) | Matches the default |
| C | Source aggregation | 0 — single portfolio system | Matches the default |
| D | Base tier | Open publication = +2 | Matches the default |
| E | Automated decision-making | 0 — no individual decision | Matches the default |
| G | Data provenance | 0 | Matches the default |
| F (track (b)) | Organisational consequences | Reputational impact of a re-identification from an open release | Track (b) only |

Severity index for S1 = 3 + 0 + 3 + 0 + 2 + 0 + 0 = 8 → Significant.

## **4.C.4 Final Residual Risk Level**

| Step | Description |
| :---- | :---- |
| Step 0 — G-L | Confirmed. A release that would disclose identifiable special-category data without an applicable Art. 9(2) condition fails G-L and is blocked (Example 3.3); the internal no-health-attribute policy is checked under G-M3 |
| Steps 1–3 | S1: module outcome × Significant through the Document 8 matrix |
| Step 4 — PET outcome | A failed module blocks the release, whatever the tier |
| Step 5 — Track (a) tier | The S1 tier |
| Step 6 — Project rules | None |
| Step 7 — G-36 | Evaluated where the preparation of the release is subject to a DPIA |
| Step 8 — Acceptance and anonymity conclusion | Acceptance per Document 8, Section 5. Separately, the Processing Owner records the anonymity conclusion on Legal & Compliance's assessment, with Group DPO advice; the conclusion is re-assessed at least annually and before each new release |
| Step 9 — Track (b) | Reported separately |

## **4.C.5 Traceability and Evidence Pack**

PEP compiles the evidence pack for every calculation: Block 0 — G-L record including the prohibited-attribute check; Block 1 — archetype 2b, scenario S1, the broad adversary profile and its justification, gated metrics; Block 2 — every SDC check and attack metric with values, thresholds, normalised values, confidence intervals and pass/fail, the disclosure indicator and the module outcome, and the differencing check against all earlier releases; Block 3 — Factors B–G and the track (b) level; Block 4 — tier, Group DPO advice, the anonymity conclusion with its reasons and re-assessment date, and the decision of the single designated decider.

## **4.C.6 Other PET Application Metrics**

| Metric | Project threshold | Difference from the default |
| :---- | :---- | :---- |
| Correlation Matrix Diff | Low divergence | Matches the default — preservation of the correlation structure among published categories |

Task-specific utility metrics (ML F1 Delta, as in Section 4.B.6) are not used — the publication has no defined downstream analytical task.

# **Project 4 — Processing of Identified Data Without a De-identification Plan**

## **4.D.1 Purpose and Characteristics of the Project**

* Purpose — assessing the rights-and-freedoms risk of processing that uses identified customer data as its intended, permanent state, on a lawful basis confirmed by G-L — for example, personalised marketing offers on consent, or automated credit decisions on contract necessity with Art. 22(2)(a) and Art. 22(3) safeguards.

* Scope — any processing of identified (or pseudonymised) customer data without a plan for de-identification, whatever the lawful basis or purpose, including the use of third-party AI tools. Not used for de-identified or aggregate releases (Project 3) or for datasets awaiting a PET decision (Project 1).

* Technology — archetype 4; threat-based likelihood (Section 3.2) for every scenario.

| Characteristic | Value |
| :---- | :---- |
| Project owner | Privacy Operations Lead (configuration approved by the Chief Privacy Officer; Group DPO advice recorded) |
| Configuration version | 1.1 (version 1.0 of 1 March 2026 was approved by the Group DPO under the arrangements then in force) |
| Review cadence | Annually; upon any change of recipients (for example, advertising partners) or of the decision logic; upon expiry of a conditional acceptance |
| Effective date | 20 October 2026 (configuration 1.1, re-approved by the Chief Privacy Officer on re-baselining) |
| Archetype | 4 — identified processing (Section 3.1) |
| G-L record | Mandatory: lawful basis, Art. 9/10 condition where relevant, purpose compatibility, transparency deliverable, Art. 22 permissibility and safeguards, Chapter V where relevant. Example lawful bases: consent (Art. 6(1)(a); Consent Management Policy, Document 13) for personalised offers; contract necessity (Art. 6(1)(b)) with Art. 22(2)(a) for credit decisions |
| Harm scenarios | Defined per case; as a minimum, loss of control, discrimination/adverse ADM where a decision is taken, and loss of confidentiality are considered (Examples 4.1–4.3) |
| Weight vector (w\_B, w\_C, w\_D, w\_E, w\_G) | (1, 1, 1, 1, 1) — default |
| Diagnostic alert mode | Not applicable — no PET-module metrics |
| Data provenance attribution (Factor G) | Per case, with reference to the RoPA (Document 21) |
| Vulnerable categories | As in Section 3.4; applies to credit-decision scenarios affecting customers on the register of financially vulnerable persons |

* Archetype 4 does not fix likelihood at a constant. Identified data are not, by themselves, a "near-certain" harm: likelihood depends on the threat sources, the exposure, the effectiveness of the controls and the event history of each scenario.

## **4.D.2 Likelihood**

Threat-based for every scenario (Section 3.2), with inherent (L3 = 3) and residual values. Evidence for L3 is taken from the Bank's register of technical and organisational measures, the due-diligence status of recipients (Document 17), the tested incident-response plan (Document 14), and, for credit decisions, the human-review and contestation process (Document 15), bias testing and independent model validation. Numerical examples — Appendix to Part B, Examples 4.1, 4.2 and 4.3.

## **4.D.3 Severity**

| Factor | Subfactor | Score for the project | Difference from the default |
| :---- | :---- | :---- | :---- |
| A | Harm type | Per scenario | Tag |
| B | Data class | Confidential = 2 (contact data, preferences, interaction history) or Restricted = 3 (credit data) | Matches the default |
| B | Special categories | Per the catalogue | Matches the default |
| B | Vulnerability | Per the catalogue | Matches the default |
| C | Number of affected data subjects | Per the catalogue | Matches the default |
| C | Source aggregation | Per the catalogue | Matches the default |
| D | Base tier | Within PanEuropean = 0, or partner = +1 | Matches the default |
| E | Automated decision-making | +2 for scenarios whose harm is produced through the automated credit decision; 0 otherwise | Matches the default |
| G | Data provenance | Per the catalogue | Matches the default |
| F (track (b)) | Organisational consequences | Per case | Track (b) only |

| Step | Description |
| :---- | :---- |
| Step 1 — Value of each applicable factor per scenario | For each scenario, the value and score of each factor (table above) |
| Step 2 — Weighting and summation | Severity index = w\_B·B + w\_C·C + w\_D·D + w\_E·E + w\_G·G, floor 0 (default weights); Factor A is a tag; Factor F is reported separately |
| Step 3 — Mapping to a level | Intervals of Part A, Section 4.3: index < 3.5 Minor; 3.5 to < 6.5 Moderate; 6.5 to < 8.5 Significant; ≥ 8.5 Catastrophic (with default weights: 0–3, 4–6, 7–8, ≥ 9); severity floors apply |

## **4.D.4 Final Residual Risk Level**

| Step | Description |
| :---- | :---- |
| Step 0 — G-L | Mandatory record; a G-L failure stops the processing or sends it back for redesign (Example 4.2) |
| Steps 1–3 | Each scenario's likelihood and severity mapped through the Document 8 matrix (inherent and residual) |
| Step 4 — PET outcome | Not applicable |
| Step 5 — Track (a) tier | Highest residual scenario tier |
| Step 6 — Project rules | Group DPO advice is sought for every archetype-4 calculation that concerns automated decisions or a high-risk AI system, whatever the tier (Document 8, Section 5, triggers) |
| Step 7 — G-36 | Evaluated for every DPIA; Legal & Compliance records the conclusion with Group DPO advice |
| Step 8 — Acceptance | Per Document 8, Section 5 |
| Step 9 — Track (b) | Reported separately |

## **4.D.5 Traceability and Evidence Pack**

PEP compiles the evidence pack for each calculation: Block 0 — the G-L record (mandatory for archetype 4) and the G-DPIA outcome; Block 1 — scenarios and the relevance statement for each harm type; Block 2 — L1–L4 per scenario, inherent and residual, with evidence for L3; Block 3 — Factors B–G per scenario and the track (b) level; Block 4 — scenario tiers, the track (a) tier, the G-36 conclusion with reasons and, where consultation took place, the supervisory authority's written advice and its implementation, Group DPO advice, and the decision of the single designated decider.

## **4.D.6 Other PET Application Metrics**

Not applicable — archetype 4 does not use a PET for the processing assessed.

## **5. Roles and Responsibilities**

| Role | Responsibility |
| :---- | :---- |
| Chief Privacy Officer (EPPO) | Owns this methodology and proposes it for adoption by the Management Board; approves the configuration of each Risk Calculation Project, including deviations from catalogue defaults (Sections 4.A.1–4.D.1); concurs in Medium acceptances (Document 8) |
| Privacy Operations Lead | Owns the projects; runs calculations; maintains configuration versions and the privacy-loss ledger (Section 3.3.6); initiates re-calculation, periodic re-assessment and the annual re-assessment of anonymity conclusions |
| Privacy Engineer(s) | Implement metrics, attacks and DP accounting on PEP; ensure confidence intervals, traceability and reproducibility (Sections 4.A.5–4.D.5) |
| Legal & Compliance | Owns G-L; records the legal conclusion on the Art. 36(1) test and on anonymity or transfer status, with Group DPO advice |
| Group DPO | Advises on every DPIA and on project configurations, scenarios, G-36 conclusions and anonymity conclusions; monitors compliance; may escalate directly to the Management Board. Does not approve, accept risk, authorise processing or determine anonymity |
| Processing Owner (e.g. Head of Credit Decisions; Head of Digital Banking) | Decides on acceptance of residual risk up to the delegated tier (Document 8, Section 5); records reasons where the decision departs from Group DPO advice; records anonymity conclusions for releases in the Processing Owner's area on Legal & Compliance's assessment |
| Chief Risk Officer (Management Board member) | Single designated decider for High residual risk under the Management Board's delegation (Document 8, Section 5) |
| IT Management / Information Security | Provides the PEP infrastructure for attack simulation and metric computation; evidences the security controls used in L3 |

## **6. Relationship to Other Framework Documents**

* Relies on PanEuropean's Privacy Risk Appetite Statement (Document 8) — scales, matrix, acceptance authority, mandatory DPO-advice triggers and the cumulative disclosure budget.

* Relies on the Data Classification Policy (Document 10) — data class and special categories (Factor B).

* Relies on the Regulatory Applicability Matrix (Document 7) — the AI Act high-risk classification of credit scoring for track (b) and legal facts used by G-L.

* Relies on the Consent Management Policy (Document 13) only through G-L, where consent is the lawful basis (Project 4); consent is not a risk factor.

* Relies on the Privacy Automation & Tooling Strategy (Document 9) — the connection point between this methodology and PEP.

* Is applied in the DPIA Methodology (Document 19): Project 2 for DPIA-CS-TRAIN-01; Project 4 (Example 4.3) for DPIA-CS-INFER-01 and DPIA-CS-LAUNCH-01; and in the TIA Methodology (Document 20) only for the elements Document 20 requests.

* Provides PET-module evidence to the Data Retention & Disposal Policy (Document 11) — archival datasets; to the Privacy by Design & by Default Policy (Document 16) — publication on the open-data portal (Project 3) and synthetic training data (Project 2); to the Cross-Border Data Transfer Policy (Document 12) — the federated anti-fraud consortium (Section 3.3.3, EVP-2026-0041); and to the Vendor / Third-Party Privacy Risk Policy (Document 17). The legal conclusions in those documents are the controller's, with Group DPO advice.

* Interacts with the Data Breach Response Policy (Document 14) — the severity factors may be reused to describe incident severity; Document 14 owns breach definitions and the Art. 33/34 tests.

* Passes results to the Privacy Risk Register (Document 22) and the RoPA (Document 21).

* Defines the parameter space for Risk Calculation Projects developed under Calculation Project Development (C1) and applied in Request & Transformation (C2) of the Privacy Governance Process Map (Document 24); the register of active projects is maintained through the project passports (Sections 4.A.1–4.D.1).

## **7. Review and Amendment**

This document is reviewed under the continuous-improvement principle of the Privacy Governance Charter (Document 2) and the Policy Review Cycle (Document 29), and also upon the emergence of a new PET or attack class, upon revision of the scales of Document 8, upon adoption of final EDPB guidelines on anonymisation, and upon a PEP version change that affects the metrics or tests used. Each annual review includes a sensitivity analysis of the likelihood and severity band cut-points. Changes are adopted by the Management Board on the proposal of the Chief Privacy Officer, after consulting the Privacy Risk Committee and the Group DPO.

Creating a Risk Calculation Project, or changing the configuration of an existing one, is a versioned change approved by the Chief Privacy Officer; it does not require a full review of this document unless it affects the architecture (Section 3.1). A change to defaults does not retroactively revise decisions already made; reproducibility is ensured by preserving the configuration version in force at the time of the decision (Sections 4.A.5–4.D.5).

A completed calculation is re-run upon a material change to the dataset, the parties or recipients (for example, a change of advertising partner in Project 4), the threat landscape or available auxiliary data; when a pilot moves to production; on expiry of a conditional acceptance; and on expiry of the review period in the project passport (Sections 4.A.1–4.D.1). Anonymity conclusions for released artefacts are re-assessed at least annually (Section 3.3.0). A decision based on an obsolete calculation is not valid for the changed case. Initiating re-calculation is the responsibility of the Privacy Operations Lead (Section 5).

## **8. Approval**

Version 1.0 was adopted by the Management Board of PanEuropean Bank AG on 1 March 2026 and version 1.1 on 22 August 2026, together with version 2.0 of the Privacy Risk Appetite Statement (Document 8); the Group DPO was the document owner at that time. Version 1.2 was adopted by the Management Board on 20 October 2026, on the proposal of the Chief Privacy Officer (a position that exists from that date) and after consulting the Privacy Risk Committee and the Group DPO. This document is not a Supervisory Board reserved consent matter. Document owner: Chief Privacy Officer.

**APPENDIX TO PART B**

# **Appendix to Part B — Numerical Examples of Risk Calculation Projects**

This appendix contains numerical examples for the four Risk Calculation Projects of Section 4. Metric values are illustrative; the "Value" column is not part of a project's configuration, because a value is measured for a specific dataset at the time of assessment. The "Threshold" column reflects the threshold set in Sections 4.A.2–4.D.2. The residual-risk matrix used is that of PanEuropean's Document 8, Section 4:

| Severity \\ Likelihood | Low | Medium | High | Near-certain |
| :---- | :---- | :---- | :---- | :---- |
| **Minor** | Low | Low | Low | Low |
| **Moderate** | Low | Low | Medium | Medium |
| **Significant** | Medium | Medium | High | High |
| **Catastrophic** | High | High | Critical | Critical |

Contributions in the tables are rounded to three decimals; indicators are the sums of unrounded contributions. A disclosure indicator is an uncalibrated ordinal summary, not a probability.

**Chronology.** The decisions shown apply the acceptance authority in force from 23 October 2026 (Document 8, version 3.0, adopted on 20 October 2026 and effective on the Supervisory Board's consent on 23 October 2026; this document, version 1.2, adopted on 20 October 2026). The Chief Privacy Officer position exists from 20 October 2026; the current decision rules apply only from 23 October 2026. Where a case was first decided earlier (for example DPIA-CS-TRAIN-01 in Document 19), the earlier decision was taken under the authority then in force — without any Chief Privacy Officer involvement — and a conditional acceptance is re-assessed under the current rules at its expiry or at the next material change.

## **Project 1 — Base Dataset Assessment**

# **Example 1.1**

An internal-audit sample of credit-application data (not PET-transformed), accessed by named Privacy Engineers with a moderate level of access protection. G-L: confirmed (audit purpose compatible; no special-category data in the sample).

**Likelihood — scenario S1 (unauthorised disclosure or misuse of the audit sample):**

| Factor | Assessment | Score |
| :---- | :---- | :---- |
| L1 Exposure | Periodic access by named Privacy Engineers | 1 |
| L2 Threat source | Accidental or low-capability misuse by vetted staff | 1 |
| L3 Control gap (residual) | Access control and logging implemented; access reviews partially tested | 1 (inherent: 3) |
| L4 Event history | Insider misuse of analytics extracts reported in the sector | 1 |

Residual likelihood index = 1 + 1 + 1 + 1 = 4 → **Medium**. Inherent index = 1 + 1 + 3 + 1 = 6 → Medium.

**Base-dataset disclosure diagnostics (quasi-identifier view; default thresholds; not used as likelihood):**

| Metric | Value | Threshold | Normalised | Weight | Contribution |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Singling-out rate | 0.8% | 1% | 0.80 | 0.35 | 0.280 |
| Deterministic linkage rate | 0.9% | 1% | 0.90 | 0.1167 | 0.105 |
| Fellegi-Sunter precision@100 | 4% | 5% | 0.80 | 0.1167 | 0.093 |
| k-NN linkage success | 9% | 10% | 0.90 | 0.1167 | 0.105 |
| ZCAP advantage | 0.09 | 0.10 | 0.90 | 0.10 | 0.090 |
| Normalised information gain | 0.28 | 0.30 | 0.93 | 0.10 | 0.093 |
| ML inference advantage | 0.09 | 0.10 | 0.90 | 0.10 | 0.090 |

Disclosure indicator = 0.857. No metric exceeds its threshold, but every metric is at 80–93% of it: the quasi-identifier view could not be released without substantial transformation. This informs PET planning (Projects 2–3); it does not change the likelihood of S1.

**Severity — S1:**

| Factor | Subfactor | Value for the case | Score |
| :---- | :---- | :---- | :---- |
| A | Harm type | Loss of confidentiality; identity fraud; financial loss | tag |
| B | Data class | Confidential (Document 10) | 2 |
| B | Special categories | Absent | 0 |
| B | Vulnerability | Not specifically affected | 0 |
| C | Number of affected data subjects | 100–9,999 (audit sample) | 1 |
| C | Source aggregation | Single source | 0 |
| D | Base tier | Within PanEuropean | 0 |
| E | Automated decision-making | No decision on the audit sample | 0 |
| G | Data provenance | Direct collection, clear notice | 0 |

Severity index = 2 + 0 + 0 + 1 + 0 + 0 + 0 + 0 = 3 → **Minor**.

**Result:** Medium × Minor = **Low** (inherent: Medium × Minor = Low). Track (b): Minor. Acceptance: the Processing Owner of the credit-scoring processing (Head of Credit Decisions) records the decision (Document 8, Section 5); no separate DPIA exists for the audit sample.

# **Example 1.2**

The same sample, but access control has been weakened (a wider circle including external contractors), more fields are exposed, and health data from payment protection insurance (PPI) were accidentally included.

**Step 0 — G-L: failed as found.** The audit purpose has no Art. 9(2) condition for processing PPI health data, and their inclusion breaches data minimisation. The as-found state is not available for acceptance: the health attributes are removed from the sample, access is restricted again, and the event is passed to Document 14, which determines whether it is a personal data breach (Art. 4(12)) — in which case it is recorded under Art. 33(5) and assessed for notification — or another privacy incident. The calculation below documents the as-found state for incident classification and to verify the remediation.

**Likelihood — S1 (as found):**

| Factor | Assessment | Score |
| :---- | :---- | :---- |
| L1 Exposure | Routine access by a wider circle including contractors | 2 |
| L2 Threat source | Opportunistic insider; health data raise the motivation for misuse | 2 |
| L3 Control gap | Access control weakened — known weakness | 2 (inherent: 3) |
| L4 Event history | Sector events | 1 |

Index = 7 → **High** (inherent 8 → High).

**Diagnostics (as found):**

| Metric | Value | Threshold | Normalised | Weight | Contribution |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Singling-out rate | 1.5% | 1% | 1.50 | 0.35 | 0.525 |
| Deterministic linkage rate | 1.8% | 1% | 1.80 | 0.1167 | 0.210 |
| Fellegi-Sunter precision@100 | 7% | 5% | 1.40 | 0.1167 | 0.163 |
| k-NN linkage success | 15% | 10% | 1.50 | 0.1167 | 0.175 |
| ZCAP advantage | 0.15 | 0.10 | 1.50 | 0.10 | 0.150 |
| Normalised information gain | 0.40 | 0.30 | 1.33 | 0.10 | 0.133 |
| ML inference advantage | 0.15 | 0.10 | 1.50 | 0.10 | 0.150 |

Disclosure indicator = 1.507; all seven metrics exceed their thresholds (logged under the lenient diagnostic mode).

**Severity — S1 (as found):** B: Confidential 2 + special categories 2 + vulnerability 0 = 4; C: 1; D: 0; E: 0; G: 0. Severity index = 5 → **Moderate** (the special-category score is the default +2; the wider circle of persons with access is reflected in likelihood).

**Result (as found):** High × Moderate = **Medium** — recorded as "G-L failed — not available for acceptance". **After remediation** (health attributes deleted; access restricted to named Privacy Engineers): severity returns to 3 (Minor); likelihood L1 1 + L2 1 + L3 1 + L4 2 (an event in PanEuropean's own processing within the last 24 months) = 5 → Medium; Medium × Minor = **Low**, recorded by the Processing Owner with Group DPO advice, because the event concerned special-category data (Document 8, Section 5, triggers).

## **Project 2 — Synthetic Dataset for Model Calibration**

All three examples concern the same source population (about 1.2 million retail customers) and the project thresholds of Section 4.B.2: ε ≤ 2.0 at the configured δ = 1×10⁻⁹. Severity is the same in all three examples: severity index 7 → **Significant** (Section 4.B.3).

# **Example 2.1**

The first DP-CTGAN generator, trained before the project configuration was finalised: ε = 2.1 at δ = 8×10⁻⁶ (Rényi DP accountant; privacy unit one customer).

| Metric | Value | Threshold | Normalised | Weight | Contribution | Gate |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| MIA accuracy | 54% (advantage 0.08) | < 60% (advantage < 0.20) | 0.40 | 0.25 | 0.100 | Pass |
| MIA AUC-ROC | 0.57 | < 0.60 | 0.70 | 0.25 | 0.175 | Pass |
| MIA TPR at FPR = 0.1% | 0.4% | ≤ 1.0% | — | — | — | Pass |
| DCR P5 | 0.19 | ≥ 0.15 | 0.79 | 0.25 | 0.197 | Pass |
| NNDR median | 0.78 | > 0.70 | 0.73 | 0.25 | 0.183 | Pass |
| Linkability advantage (TP-SYN-LINK) | 0.02 | ≤ 0.05 | — | — | — | Pass |
| Attribute-inference advantage (TP-SYN-INF) | 0.03 | ≤ 0.05 | — | — | — | Pass |
| ε | 2.1 | ≤ 2.0 | — | — | — | **Fail (G-M1)** |
| δ (configured) | 8×10⁻⁶ | 1×10⁻⁹ | — | — | — | **Fail (G-M4 — DP statement does not match the project configuration)** |

Disclosure indicator = 0.656. The attack metrics pass on their unfavourable 95% bounds (evaluation design as in Example 2.1-R; for example, MIA accuracy 53.0%–55.0%, TPR at FPR 0.1% 0.26%–0.62%). **Module outcome: FAIL** — the ε gate and the DP-configuration gate fail, whatever the indicator. No attack was reproduced, so the as-proposed likelihood of S1 is **High**; High × Significant = High, recorded as "not available for acceptance". The synthetic dataset is not released to Data Science; the generator is reconfigured (Example 2.1-R).

The run is charged to the lifetime privacy-loss ledger (ε 2.1, δ 8×10⁻⁶), because its synthetic output was observed by Privacy Engineers inside PEP during the evaluation (Section 3.3.6). For comparison: the previous version of the method averaged the ε breach into a "probability" of 0.901 and, in a lenient mode, only logged it; under this methodology a breached mandatory threshold cannot be averaged away.

# **Example 2.1-R**

The reconfigured generator: higher noise multiplier, per-customer contribution bound, δ configured at 1×10⁻⁹; ε = 1.8 (Rényi DP accountant).

Evaluation design (illustrative assumptions, not the results of a real test): membership attacks on a balanced set of 5,000 training members and 5,000 holdout non-members; TP-SYN-LINK and TP-SYN-INF on 5,000 training records and a control set of 5,000 records not used in training; five repetitions (independent re-runs with fresh seeds and fresh member/non-member splits); 95% intervals — Wilson score intervals for proportions (accuracy, hit rates, linkage and inference success rates), bootstrap percentile intervals (2,000 resamples of records) for AUC, advantages and distances; all interval bounds shown are illustrative assumptions, not computed from real observations. The gate uses the orientation-invariant unfavourable bound.

| Metric | Value | 95% CI (illustrative) | Threshold | Gate on the unfavourable bound | Normalised | Weight | Contribution |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| MIA accuracy | 53% (advantage 0.06) | 52.0% – 54.0% | < 60% | Upper 54.0% — Pass | 0.30 | 0.25 | 0.075 |
| MIA AUC-ROC | 0.55 | 0.54 – 0.56 | < 0.60 | Upper 0.56 — Pass | 0.50 | 0.25 | 0.125 |
| MIA TPR at FPR = 0.1% | 0.2% (10 of 5,000 members) | 0.11% – 0.37% | ≤ 1.0% | Upper 0.37% — Pass | — | — | — |
| DCR P5 | 0.21 | 0.20 – 0.22 | ≥ 0.15 | Lower 0.20 — Pass; no record with DCR = 0 | 0.71 | 0.25 | 0.179 |
| NNDR median | 0.81 | 0.80 – 0.82 | > 0.70 | Lower 0.80 — Pass | 0.63 | 0.25 | 0.158 |
| Linkability advantage (TP-SYN-LINK) | 0.01 | −0.005 – 0.025 | ≤ 0.05 | Upper 0.025 — Pass | — | — | — |
| Attribute-inference advantage (TP-SYN-INF) | 0.02 | 0.005 – 0.035 | ≤ 0.05 | Upper 0.035 — Pass | — | — | — |
| ε | 1.8 | — (accountant output) | ≤ 2.0 | Pass | — | — | — |
| δ (configured) | 1×10⁻⁹ | — | 1×10⁻⁹ | Pass | — | — | — |

Observed membership success is close to chance (advantage 0.06; upper bound 0.08). It is reported, and it does not fail G-M2, whose unacceptable level for this attack is an accuracy of 60% or more.

Disclosure indicator = 0.537. **Module outcome: PASS**, 0.5 ≤ indicator ≤ 1.0 → likelihood of S1 **Medium** — conditional on the ledger check below (G-M4).

**Cumulative privacy loss (Section 3.3.6; G-M4).** Lifetime ledger for the retail customer population (privacy unit: one customer):

| Run | ε | δ | Accountant | Observers |
| :---- | :---- | :---- | :---- | :---- |
| Federated anti-fraud consortium, all rounds (EVP-2026-0041) | 2.6 | 1×10⁻⁹ | Rényi DP | Consortium members |
| Example 2.1 generator (output observed in PEP) | 2.1 | 8×10⁻⁶ | Rényi DP | Privacy Engineers |
| Example 2.1-R generator | 1.8 | 1×10⁻⁹ | Rényi DP | Privacy Engineers; Data Science (synthetic dataset) |
| **Cumulative (basic composition)** | **6.5** | **≈ 8.0×10⁻⁶** | Sum of ε and sum of δ | Composed as if one party observed all outputs |

Assumptions: no other DP mechanism has been run on this population; each run's (ε, δ) guarantee holds for the customer-level privacy unit; observers are treated as able to combine outputs (conservative); basic composition is used because the runs' accounting states are not combined in one accountant. Caps (Document 8, Section 3; illustrative internal appetite parameters, not legal thresholds): lifetime ε ≤ 10.0 and δ ≤ 1×10⁻⁵ — respected (headroom ε 3.5, δ about 2.0×10⁻⁶); operational cap on new spending in calendar year 2026, ε ≤ 7.0 — respected (6.5). The composed guarantee for the population is therefore (ε 6.5, δ ≈ 8.0×10⁻⁶): the δ of the Example 2.1 run stays in the ledger, and the new run's configured δ of 1×10⁻⁹ does not lower it. The PASS is conditional on these assumptions; any further DP run on this population is checked against the remaining headroom before it starts.

**DP bound, for information only.** Under the narrow assumptions of Section 3.3.5 (membership test between adjacent datasets, uniform prior, worst-case attacker), accuracy ≤ (e^1.8 + 10⁻⁹)/(1 + e^1.8) ≈ 0.858. The observed MIA accuracy of 53% is compatible with this bound; neither value is a re-identification probability or an anonymity guarantee.

**Scenario tiers.** S1: Medium × Significant = **Medium**. S2 (threat-based, Section 4.B.2): residual Low × Significant = Medium; inherent Medium × Significant = Medium. **Track (a) tier: Medium.** Track (b): applicable regime +1, financial 1, reputational 1 → index 3 → Moderate (reported to ERM; does not affect track (a)).

**Decision (DPIA-CS-TRAIN-01, Document 19).** G-36: Legal & Compliance concluded, with Group DPO advice, that the Art. 36(1) test is not met — no scenario remains at a high risk to rights and freedoms after the measures — and recorded the reasons. Acceptance under the current rules (Document 8, version 3.0): Medium — the Processing Owner (Head of Credit Decisions) with the Chief Privacy Officer's concurrence; Group DPO advice recorded; conditional acceptance expiring after 12 months or at the next calibration, whichever is earlier, and conditional on ε ≤ 2.0 per run and on the ledger caps. (Before 23 October 2026, when the current acceptance rules took effect, the Medium tier was accepted by the Processing Owner with Group DPO advice, without concurrence by a Chief Privacy Officer — see Chronology above.)

# **Example 2.2**

A hypothetical alternative configuration, shown for comparison: more DP-SGD epochs and a lower noise multiplier — that is, weaker privacy (privacy loss grows with the number of training steps and falls as the noise multiplier rises). ε = 3.8 at δ = 1.6×10⁻⁵.

| Metric | Value | Threshold | Normalised | Weight | Contribution | Gate |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| MIA accuracy | 63% (advantage 0.26) | < 60% (advantage < 0.20) | 1.30 | 0.25 | 0.325 | **Fail** |
| MIA AUC-ROC | 0.66 | < 0.60 | 1.60 | 0.25 | 0.400 | **Fail** |
| MIA TPR at FPR = 0.1% | 2.6% | ≤ 1.0% | — | — | — | **Fail** |
| DCR P5 | 0.11 | ≥ 0.15 | 1.36 | 0.25 | 0.341 | **Fail** |
| NNDR median | 0.55 | > 0.70 | 1.50 | 0.25 | 0.375 | **Fail** |
| Linkability advantage (TP-SYN-LINK) | 0.09 | ≤ 0.05 | — | — | — | **Fail** |
| Attribute-inference advantage (TP-SYN-INF) | 0.07 | ≤ 0.05 | — | — | — | **Fail** |
| ε | 3.8 | ≤ 2.0 | — | — | — | **Fail** |
| δ (configured) | 1.6×10⁻⁵ | 1×10⁻⁹ | — | — | — | **Fail** |

Disclosure indicator = 1.441. **Module outcome: FAIL** (G-M1, G-M2, G-M4). The membership failure was reproduced in all five repetitions with the whole 95% interval beyond the threshold (accuracy 62.1%–63.9%; TPR at FPR 0.1% 2.2%–3.1%), so under the internal routing rule the as-proposed likelihood is recorded as **Near-certain**. This is a routing convention: the observed success — an attack that is right about 63% of the time on a balanced set and identifies about 2.6% of members at a 0.1% false-positive rate — is reported alongside it, and it does not mean that every customer's membership is disclosed. Near-certain × Significant = High — not available for acceptance. Had this configuration been run on the source population, the lifetime ledger would have reached ε 10.3 and δ ≈ 2.4×10⁻⁵, above the Document 8 lifetime budget (G-M4).

## **Project 3 — Aggregate Statistics for the Open Data Portal**

Severity of S1 in Examples 3.1 and 3.2: severity index 8 → **Significant** (Section 4.C.3).

# **Example 3.1**

Sufficiently aggregated statistics: generalised categories, small cells suppressed. Singling-out threshold 0.5% (stricter than the default 1%); other thresholds at default.

**SDC gates:** smallest published cell 14 (≥ 10 — pass); differencing within the release and against the two previous releases — no derivable cell below 10 (pass); exact reconstruction 0.4% of source records, 0.35%–0.45% over five attack runs (highest value ≤ 1% — pass); every published table within the test scope (G-M5 — pass); attributes excluded by internal policy — none (G-M3 — pass).

Evaluation design (illustrative assumptions, not the results of a real test): record-level attacks on a random sample of 20,000 reconstructed records against an auxiliary dataset simulating public registers and social-network data; Fellegi-Sunter precision@100 over six repetitions (600 candidate pairs; independent re-runs with fresh random samples); 95% intervals — Wilson score intervals for proportions (precision@100, share of records reconstructed, singling-out and linkage rates), bootstrap percentile intervals (2,000 resamples of records) for information-gain and inference-advantage measures; all interval bounds shown are illustrative assumptions, not computed from real observations. The gate uses the unfavourable bound.

**Attack battery on reconstructed records:**

| Metric | Value | 95% CI (illustrative) | Threshold | Normalised | Weight | Contribution |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Singling-out rate | 0.3% | 0.23% – 0.39% | < 0.5% | 0.60 | 0.20 | 0.120 |
| Deterministic linkage rate | 0.2% | 0.15% – 0.27% | < 1% | 0.20 | 0.1667 | 0.033 |
| Fellegi-Sunter precision@100 | 1.5% (9 of 600) | 0.79% – 2.83% | < 5% | 0.30 | 0.1667 | 0.050 |
| k-NN linkage success | 3% | 2.77% – 3.25% | < 10% | 0.30 | 0.1667 | 0.050 |
| Normalised information gain | 0.12 | 0.11 – 0.13 | < 0.30 | 0.40 | 0.10 | 0.040 |
| ML inference advantage | 0.03 | 0.02 – 0.04 | < 0.10 | 0.30 | 0.10 | 0.030 |
| ZCAP advantage | 0.04 | 0.03 – 0.05 | < 0.10 | 0.40 | 0.10 | 0.040 |

The observed success is not zero — for example, 0.3% of reconstructed records can be singled out and 0.4% of source records are reconstructed exactly — but every value, including its unfavourable bound, is below the project's unacceptable-success level, so neither G-M1 nor G-M2 fails. The observed values are recorded in the evidence pack and taken into account in the legal anonymity assessment.

Disclosure indicator = 0.363 (0.303 at the default singling-out threshold of 1%). **Module outcome: PASS**, indicator < 0.5 → likelihood **Low**.

**Severity — S1:** B: Restricted 3 + special categories 0 + vulnerability 0; C: > 1,000,000 → 3, aggregation 0; D: open publication +2; E: 0; G: 0. Severity index = 8 → **Significant**.

**Result:** Low × Significant = **Medium**. The likelihood is Low because the module passed all gates; the tier is Medium because the consequences would be significant if the anonymity conclusion proved wrong. Track (b): reputational 1 → Minor.

**Decision.** The Processing Owner for the publication records the conclusion that the statistics are anonymous information, on Legal & Compliance's assessment against Recital 26 with "anyone" as the recipient, and with Group DPO advice; the module result is the evidence, not the conclusion. Acceptance of the Medium residual risk: the Processing Owner with the Chief Privacy Officer's concurrence; Group DPO advice recorded; conditional acceptance expiring after 12 months; re-assessment before each new release and at least annually.

# **Example 3.2**

Insufficiently generalised statistics — small groups in some categories of the credit portfolio. Same thresholds.

**SDC gates:** smallest published cell 3 (**fail**); differencing — two cells below 10 derivable from overlapping tables (**fail**); exact reconstruction 2.7% of source records (**fail** — attack reproduced); special-category attributes — none (pass).

**Attack battery on reconstructed records:**

| Metric | Value | Threshold | Normalised | Weight | Contribution |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Singling-out rate | 0.9% | 0.5% | 1.80 | 0.20 | 0.360 |
| Deterministic linkage rate | 1.2% | 1% | 1.20 | 0.1667 | 0.200 |
| Fellegi-Sunter precision@100 | 6% | 5% | 1.20 | 0.1667 | 0.200 |
| k-NN linkage success | 12% | 10% | 1.20 | 0.1667 | 0.200 |
| Normalised information gain | 0.25 | 0.30 | 0.83 | 0.10 | 0.083 |
| ML inference advantage | 0.08 | 0.10 | 0.80 | 0.10 | 0.080 |
| ZCAP advantage | 0.08 | 0.10 | 0.80 | 0.10 | 0.080 |

Disclosure indicator = 1.203 (1.023 at the default singling-out threshold; even then three linkage metrics and all three SDC gates fail). **Module outcome: FAIL** (G-M1, G-M2). The reconstruction failure was reproduced in all five runs (2.6%–2.8% of source records, wholly above 1%), so under the internal routing rule the as-proposed likelihood is recorded as **Near-certain**; the observed success — about 2.7% of source records reconstructed exactly, and singling out of 0.9% of reconstructed records (95% CI 0.78%–1.04%) — is reported alongside it. Near-certain × Significant = **High** — not available for acceptance. Publication is blocked; the statistics are redesigned (coarser categories, further suppression or a differentially private release mechanism with a DP statement) and re-assessed.

# **Example 3.3 — Blocked Case (G-L failure)**

The same portal and source data. The configured tests were run with a wide margin — every attack metric is at one tenth of its threshold — but a cross-tabulation added late in preparation crosses the attribute "active payment protection insurance (PPI)" with branch region, five-year age band and credit product. PPI is arranged with a health questionnaire, so the attribute reveals health-related information. The late table was outside the configured test scope.

Facts established in the pre-publication review: (1) several cells of the late table contain fewer than 10 customers and, combined with the public branch directory and age information, attribute PPI status to identifiable customers — the statistics would therefore disclose identifiable special-category data (health), not anonymous information; (2) no Art. 9(2) condition applies to publishing this information on an open portal; (3) customers were not informed of such a publication (Arts. 13/14); (4) the attribute is not necessary for the purpose of the portfolio statistics (data minimisation, Art. 5(1)(c)).

**Step 0 — G-L: failed** on facts (1)–(4). **The release is blocked.** No likelihood level, tier, risk appetite, metric or DPO opinion can make it acceptable. Independently, the late table was outside the test scope (G-M5 — INCOMPLETE), and the attribute is excluded from open releases by PanEuropean's internal policy (G-M3 — internal policy). The blocking reason is the G-L failure on these facts, not a general rule that a health-related attribute can never appear in anonymous statistics.

For the record only, the attack battery returned:

| Metric | Value | Threshold | Normalised | Weight | Contribution |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Singling-out rate | 0.05% | 0.5% | 0.10 | 0.20 | 0.020 |
| Deterministic linkage rate | 0.1% | 1% | 0.10 | 0.1667 | 0.017 |
| Fellegi-Sunter precision@100 | 0.5% | 5% | 0.10 | 0.1667 | 0.017 |
| k-NN linkage success | 1% | 10% | 0.10 | 0.1667 | 0.017 |
| Normalised information gain | 0.03 | 0.30 | 0.10 | 0.10 | 0.010 |
| ML inference advantage | 0.01 | 0.10 | 0.10 | 0.10 | 0.010 |
| ZCAP advantage | 0.01 | 0.10 | 0.10 | 0.10 | 0.010 |

Disclosure indicator = 0.100. The example shows why per-metric scores cannot replace gates: the attack battery tested the tables and attributes within its configured scope and could not detect a disclosure in a table outside it. Severity, recorded for information: B: Restricted 3 + special categories 2 = 5; C: 3; D: +2; E: 0; G: 0 → index 10 → Catastrophic (the severity floor for identifiable special-category data released to an unlimited audience would in any case require at least Significant).

**Consequences.** The release is stopped before publication; the attribute is removed and the full module is re-run, including the prohibited-attribute check, before any new publication decision. Had the statistics already been published, the event would be handled under Document 14 (personal data breach assessment, Art. 33(5) record and notification tests) and the release withdrawn from the portal as far as possible.

## **Project 4 — Processing of Identified Data Without a De-identification Plan**

# **Example 4.1**

Personalised offers delivered in PanEuropean's own mobile app to a pilot segment; granular consent with easy withdrawal in the app. G-L: confirmed (consent under Art. 6(1)(a) recorded under Document 13; Art. 13 notice). G-DPIA: one WP248 criterion (evaluation/profiling) — no presumption; triage recorded, no DPIA.

| Scenario | L1 | L2 | L3 (residual / inherent) | L4 | Index (residual / inherent) | Likelihood |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| S1 — loss of control: profiling beyond the consented scope | 3 (systematic for the pilot segment) | 1 (unintended drift of use) | 0 (purpose-bound pipeline; tested withdrawal) / 3 | 1 | 5 / 8 | Medium / High |
| S2 — loss of confidentiality of the marketing profile | 2 (routine access by the marketing team) | 2 (opportunistic insider) | 0 (tested access control) / 3 | 1 | 5 / 8 | Medium / High |

| Factor | Subfactor | Value | S1 | S2 |
| :---- | :---- | :---- | :---- | :---- |
| A | Harm type | S1: loss of control; S2: loss of confidentiality, reputational harm | tag | tag |
| B | Data class | Confidential (contact details, preferences) | 2 | 2 |
| B | Special categories / vulnerability | None / not specifically affected | 0 | 0 |
| C | Number of affected data subjects | 100–9,999 (pilot segment); single source (CRM) | 1 | 1 |
| D | Base tier | Within PanEuropean (own app) | 0 | 0 |
| E | Automated decision-making | Choice of an offer is not a decision with a significant effect | 0 | 0 |
| G | Data provenance | Direct collection, clear and specific notice | 0 | 0 |

Severity index: S1 = 3, S2 = 3 → **Minor**. Tiers: S1 Medium × Minor = Low; S2 Medium × Minor = Low (inherent: High × Minor = Low). **Track (a) tier: Low.** Consent is the lawful basis checked by G-L; it is not scored. Acceptance: the Processing Owner (Head of Digital Banking) records the decision; no DPIA exists, so Group DPO advice is not mandatory.

# **Example 4.2**

The same consent to personalisation, but offers are to be placed through an external advertising partner (demand-side platform, DSP), with the placement mentioned only in the general terms and conditions.

**Step 0 — G-L: failed as proposed.** Consent "hidden" in general terms is not specific and informed for disclosure to an advertising partner (EDPB Guidelines 05/2020 on consent); the partner's role (processor or independent controller) is undetermined; and the disclosure must also be checked against banking-confidentiality obligations under applicable national law. The proposal is stopped and redesigned. No tier is calculated for acceptance.

# **Example 4.2-R (after redesign)**

Redesign: a separate, specific consent for placement through an advertising partner, naming the purpose and the category of recipient, with withdrawal in the app; the DSP engaged as a processor under an Art. 28 data processing agreement and receiving only segment membership under rotating pseudonymous identifiers (which remain personal data). G-L: confirmed. G-DPIA: two WP248 criteria (evaluation/profiling; large scale) → DPIA performed (Document 19). Due diligence (Document 17) still shows open non-conformities (incomplete sub-processor list).

| Scenario | L1 | L2 | L3 (residual / inherent) | L4 | Index (residual / inherent) | Likelihood |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| S1 — loss of control: onward use of segment data in the advertising ecosystem | 2 (routine partner access) | 2 (commercial incentives for onward use) | 2 (open due-diligence non-conformities) / 3 | 1 | 7 / 8 | High / High |
| S2 — loss of confidentiality at the partner | 2 | 2 | 2 / 3 | 1 | 7 / 8 | High / High |

| Factor | Subfactor | Value | S1 | S2 |
| :---- | :---- | :---- | :---- | :---- |
| A | Harm type | S1: loss of control, chilling effect; S2: loss of confidentiality | tag | tag |
| B | Data class | Confidential | 2 | 2 |
| B | Special categories / vulnerability | None / not specifically affected | 0 | 0 |
| C | Number of affected data subjects | 10,000–999,999 (bank-wide segment); single source | 2 | 2 |
| D | Base tier | Shared with a partner | +1 | +1 |
| E | Automated decision-making | Not applicable | 0 | 0 |
| G | Data provenance | Direct collection, specific notice after redesign | 0 | 0 |

Severity index: S1 = 5, S2 = 5 → **Moderate**. Tiers: High × Moderate = **Medium** for both (inherent: High × Moderate = Medium). **Track (a) tier: Medium.** The partner's control quality now acts on likelihood (L3 = 2), not as a severity modifier.

**Decision.** G-36: Legal & Compliance concluded, with Group DPO advice, that the Art. 36(1) test is not met, and recorded the reasons. Acceptance: Medium — the Processing Owner (Head of Digital Banking) with the Chief Privacy Officer's concurrence; Group DPO advice recorded; conditional acceptance expiring after 90 days, on condition that the due-diligence non-conformities are closed. Re-assessment after closure: L3 = 0 → index 5 → Medium likelihood; Moderate × Medium = **Low**.

**Status at 26 October 2026.** The advertising-partner placement is not in operation. This example records the assessment and the conditional acceptance of the redesigned proposal, which has not been launched (Documents 13 and 17); a launch would require a current assessment, closure of the due-diligence non-conformities and an update of the Customer Privacy Notice (Document 1).

For comparison: the previous version of the method fixed likelihood at "Near-certain" for all identified processing and added partner and notice modifiers to severity (index 7, Significant), giving High without addressing the lawfulness defect.

# **Example 4.3 — Production Credit Scoring (DPIA-CS-INFER-01 / DPIA-CS-LAUNCH-01)**

Automated credit decisions on retail applications (about 400,000 applications a year, illustrative), using application data, EuroCredit Bureau data and transaction history. G-L: confirmed — contract necessity (Art. 6(1)(b)); Art. 22(2)(a) with Art. 22(3) safeguards (human intervention, expression of view, contest, explanation — Document 15); Art. 13/14 information including meaningful information about the logic involved. G-DPIA: several WP248 criteria (evaluation/scoring, automated decision with legal effect, large scale, matching of datasets) → DPIA performed (Document 19). The model is a high-risk AI system under the AI Act, Annex III point 5(b); high-risk obligations apply from 2 December 2027 (scheduled) and do not suspend GDPR duties.

| Scenario | L1 | L2 | L3 (residual / inherent) | L4 | Index (residual / inherent) | Likelihood |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| S1 — systematic adverse or discriminatory automated credit decisions, including through corrupted bureau data | 3 (in the planned production design clear approvals and clear refusals are decided automatically; borderline scores go to a credit officer before any decision takes effect (Document 19, Art. 22 necessity record)) | 2 (known error modes: drift, proxy variables) | 0 (pre-deployment bias testing, independent model validation, quarterly fairness monitoring, human review on request — tested) / 3 | 1 (sector events) | 6 / 9 | Medium / Near-certain |
| S2 — loss of confidentiality of application and bureau data (identity fraud, financial loss) | 2 (routine access by credit officers; bureau interface) | 3 (organised fraud groups) | 0 (access control, encryption, logging, penetration-tested) / 3 | 1 | 6 / 9 | Medium / Near-certain |
| S3 — re-use of scoring data for marketing | Not scored: incompatible purpose (Art. 6(4)) — prevented by G-L and enforced by purpose-binding in the data platform | | | | | |

| Factor | Subfactor | Value | S1 | S2 |
| :---- | :---- | :---- | :---- | :---- |
| A | Harm type | S1: discrimination/adverse ADM, financial loss, exclusion; S2: loss of confidentiality, identity fraud, financial loss | tag | tag |
| B | Data class | Restricted (credit data) | 3 | 3 |
| B | Special categories | None | 0 | 0 |
| B | Vulnerability | S1: refusals fall disproportionately on customers on the register of financially vulnerable persons; S2: marker not in the data | +1 | 0 |
| C | Number of affected data subjects | S1: 10,000–999,999 applicants a year; S2: > 1,000,000 applications retained | 2 | 3 |
| C | Source aggregation | Application + EuroCredit Bureau + transaction history | +1 | +1 |
| D | Base tier | Within PanEuropean | 0 | 0 |
| E | Automated decision-making | S1: harm produced through the automated decision; S2: disclosure scenario | +2 | 0 |
| G | Data provenance | Direct collection; EuroCredit Bureau data with Art. 14 information | 0 | 0 |

Severity index: S1 = 3 + 0 + 1 + 2 + 1 + 0 + 2 + 0 = 9 → **Catastrophic**; S2 = 3 + 0 + 0 + 3 + 1 + 0 + 0 + 0 = 7 → **Significant**.

**Tiers.** S1: inherent Near-certain × Catastrophic = Critical; residual Medium × Catastrophic = **High**. S2: inherent Near-certain × Significant = High; residual Medium × Significant = **Medium**. **Track (a) tier: High** (S1). Track (b): applicable regime +1, financial 2, reputational 2 → index 5 → Significant, reported to ERM; it does not change track (a).

**Decision.**
* G-36: Legal & Compliance concluded, with Group DPO advice, that the Art. 36(1) test is met. Scenario S1 remains at a high risk to rights and freedoms after the measures, and no further measure available to the Bank reduces it without giving up automated decisions. The reasons are recorded. PanEuropean therefore consults the HBDI before the production launch, implements any written advice and answers any information request. It does not treat an elapsed Art. 36(2) period, or the absence of comments, as an authorisation (Document 19 records the consultation). Status as at 26 October 2026: the consultation was submitted on 15 September 2026 and is pending; the production launch is planned for 1 February 2027 and will not take place before the consultation step is complete and the decision below has been taken. Automated decisions are therefore not yet in production.
* Acceptance: High — the single designated decider under the Management Board's delegation, the Chief Risk Officer, decides after the consultation; Group DPO advice recorded; the Supervisory Board's Risk Committee is informed.
* The inherent Critical tier is not a decision point. It shows that the bias-testing, validation, monitoring and human-review measures are indispensable conditions of the processing; their failure would trigger an immediate re-assessment.

For comparison: the previous version of the method fixed likelihood at "Near-certain" for identified data, which made the Bank's core credit scoring Critical by construction regardless of its controls.

# **Normative Basis and References**

**EU law and case law**
* Regulation (EU) 2016/679 (GDPR): Art. 4(1), 4(5), 4(12), 5, 6, 9, 10, 13, 14, 22, 24, 25, 26, 28, 32, 35, 36, 38, 39; Recitals 26, 38, 75, 76, 84, 85.
* Regulation (EU) 2024/1689 (AI Act), as amended by the AI Omnibus: Annex III point 5(b); Art. 27 (deployer fundamental rights impact assessment, where applicable); application dates as stated in Section 3.4 of Part B (Factor F) and Example 4.3.
* CJEU, C-582/14, *Breyer*, 19 October 2016 (means reasonably likely to be used; relative identifiability).
* CJEU, C-413/23 P, *EDPS v SRB* (identifiability assessed from the perspective of the recipient; pseudonymised data).
* CJEU, C-634/21, *SCHUFA Holding (Scoring)*, 7 December 2023 (a score playing a determining role is an Art. 22 decision).

**EDPB and Article 29 Working Party**
* Article 29 Working Party, Opinion 05/2014 on Anonymisation Techniques (WP216) — singling out, linkability, inference.
* Article 29 Working Party, Guidelines on Data Protection Impact Assessment (WP248 rev.01) — nine criteria; prior consultation where residual risk remains high.
* EDPB Guidelines 01/2025 on pseudonymisation (adopted 16 January 2025).
* EDPB Guidelines 02/2026 on anonymisation — **public-consultation draft (8 July 2026), not final**.
* EDPB Guidelines 05/2020 on consent under Regulation 2016/679.
* EDPB Opinion 28/2024 on certain data protection aspects related to the processing of personal data in the context of AI models.
* EDPB Recommendations 01/2020 on supplementary measures (referenced for the TIA boundary).

**Risk methods and engineering guidance**
* NIST, NISTIR 8062, *An Introduction to Privacy Engineering and Risk Management in Federal Systems* (January 2017).
* NIST SP 800-226, *Guidelines for Evaluating Differential Privacy Guarantees* (final, March 2025).
* NIST SP 800-188, *De-Identifying Government Datasets: Techniques and Governance* (2023).
* NIST SP 800-53 Rev. 5, control SI-19 *De-identification*, including enhancements SI-19(6) (differential privacy) and SI-19(8) (motivated intruder).
* CNIL, *Privacy Impact Assessment (PIA)* — methodology and knowledge bases.
* ENISA, *Recommendations for a methodology of the assessment of severity of personal data breaches* (2013).
* ENISA, *Pseudonymisation techniques and best practices* (2019).
* ENISA, *Data Protection Engineering* (2022).
* ISO/IEC 20889:2018, ISO/IEC 27559:2022, ISO/IEC 27557:2022 — bibliographic pointers only; no clause-level mapping is claimed.

**Research literature (methods named in this document)**
* Cox, L. A. (2008), "What's wrong with risk matrices?", *Risk Analysis* 28(2).
* Dinur, I. and Nissim, K. (2003), "Revealing information while preserving privacy", *PODS 2003* (database reconstruction).
* Carlini, N. et al. (2022), "Membership inference attacks from first principles", *IEEE Symposium on Security and Privacy* (evaluation at low false-positive rates).

# **International Adaptation**

The GDPR is the baseline of this methodology. The rights-and-freedoms scenarios, the threat-based likelihood model and the PET Assessment Module are jurisdiction-neutral; the legal tests are not. Where other regimes apply, the organisation substitutes their tests in G-L and in its anonymity conclusions:

* **UK GDPR / Data Protection Act 2018** (as amended by the Data (Use and Access) Act 2025): the same structure applies; prior consultation is with the Information Commissioner.
* **Switzerland (revFADP):** a DPIA and, where high risk remains, consultation of the FDPIC apply under the Swiss Act.
* **Canada:** under PIPEDA there is no statutory anonymisation standard; under Québec's private-sector Act (P-39.1) anonymisation is subject to its own criteria and regulation, and a privacy impact assessment is required in the cases the Act lists. The PET Assessment Module supplies evidence; the legal conclusion follows the applicable Act. The applicability map is in Document 7.

# **Document History (PGF)**

| Release | Date | Changes |
| :---- | :---- | :---- |
| 1.0.0-rc.1 | 2026-10-26 | Canonical English Markdown; changes from internal ver.2: two-track model (rights and freedoms vs organisational consequences, never offset) with seven harm types; threat-based likelihood for identified processing replaces fixed "Near-certain" for archetype 4; PET Assessment Module with per-metric results, failure gates, baseline-aware normalisation and a disclosure indicator that is not called a probability; ZCAP remapped to inference; undefined in-house metric removed; DP statement requirements (privacy unit, adjacency, accountant, composition, output access); narrow use of the e^ε/(1+e^ε) bound; neutral description of δ; repeated-release rules with a lifetime ε/δ ledger (no calendar reset) and an optional operational cap; G-M2 defined by project-specific attack sets with baselines and uncertainty rules, and a labelled internal routing rule for reproduced failures; normalisation domains and orientation, non-negative weights and an INCOMPLETE outcome for missing results; contiguous severity intervals for weighted indices; G-M3 distinguishing the Art. 9 legal test from internal policy; aggregate/SDC checks; pseudonymisation separated from anonymisation; Recital 26, C-413/23 P and EDPB Guidelines 02/2026 (draft) cited; G-L, G-DPIA and G-36 added to the decision sequence and G-TIA branched by transfer mechanism; DPO role limited to advice; consent and controls removed from severity; all worked examples recomputed (Example 3.3 rewritten as a G-L blocked case; Examples 2.1-R, 4.2-R and 4.3 added); product names and unsupported capability claims removed; example dates shifted by −12 months; references added. Integration pass: status of Example 4.2-R stated (assessed and conditionally accepted; advertising-partner placement not in operation at 26 October 2026). Review correction: Part B Factor B special-category modifier aligned with Part A (Art. 9 and Art. 10 data); no worked example of this document processes Art. 10 data, so no example changes (the re-assessment of the anti-fraud matching is in Document 19) |
