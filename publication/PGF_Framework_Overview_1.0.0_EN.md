# Privacy Governance Framework (PGF): Framework Overview and Component Guide

Version 1.0.0. Authors: Alexey Neyman; Val Khvatov. Copyright (c) 2026 REALM INVEO. CC BY 4.0.


## Publication and reading guide

**Version 1.0.0 | 28 October 2026**

**Authors:** Alexey Neyman; Val Khvatov. **Rights holder:** REALM INVEO. **Documentation licence:** CC BY 4.0.

This master document introduces the framework, its architecture and decision model and provides an annotated register of all 31 components. The editable supplement contains the complete English Markdown source set, glossary, conceptual crosswalk and curated references. The master is a reading and citation entry point; it does not replace the detailed templates.

The substantive method is the frozen rc.2 model. Publication metadata, rights attribution and presentation have been completed for version 1.0.0. The regulatory reference snapshot remains 26 October 2026.

**Reading route:** executives can begin with the overview, architecture and business-decision pages; programme owners can use the adoption route and document register; specialists can follow the component links and consult the risk-method and transfer templates.

The worked bank, deployment, configurations and numbers are illustrative. PAMOLA identifies a real implementation profile, not a prerequisite for adopting the framework or a certification of product capability. No external peer review, empirical calibration or automatic guarantee of compliance is claimed.

**Suggested citation:** Neyman, A., & Khvatov, V. (2026). *Privacy Governance Framework (PGF): Framework Overview and Component Guide* (Version 1.0.0). REALM INVEO. Use the version DOI shown in the Zenodo record.



## Contents




## Executive overview

The Privacy Governance Framework (PGF) is a set of 31 governance documents, organised in four levels:
1. strategic documents;
2. policies and standards;
3. the process model;
4. control, reporting and improvement.

Each document has a reusable template (Part A) and a worked example for a fictional pan-European retail bank (Part B). A process model of 23 processes, in governing, core and supporting groups, connects the documents to day-to-day operation.

PGF is built on four design choices:
- statutory legal-compliance gates are kept separate from managerial risk decisions;
- the Data Protection Officer remains independent, while an executive programme owner and accountable Processing Owners take the decisions;
- each fact has one authoritative register ("no duplicate registers"), and the data-governance documents are designed as overlays on an existing data-governance programme;
- the calculation of privacy risk is separate from the governance decision about which risk is acceptable.

The GDPR is the baseline. Adaptation guidance is given for Canada (PIPEDA and Québec's private-sector Act), with headline notes for the United Kingdom and Switzerland. A conceptual crosswalk relates PGF to the NIST Privacy Framework 1.0, ENISA engineering guidance and Canadian accountability guidance.


## Audience and scope

**Intended readers:**
- Data Protection Officers and privacy leads;
- executives and boards who oversee a privacy programme;
- risk, audit and compliance functions;
- data-governance and engineering teams that implement privacy controls;
- researchers and educators studying privacy governance.

**In scope:**
- governance of personal-data processing in a medium or large organisation, especially one operating in several jurisdictions;
- programme structure, mandates and decision rights;
- policies;
- risk methodology, including a specialised module for privacy-enhancing technologies (PETs);
- process ownership;
- monitoring and reporting.

**Out of scope or interface only:**
- information-security controls - PGF relies on the organisation's security programme;
- sector-specific regimes such as DORA (financial entities) and the EU AI Act - interfaces only, not full programmes;
- full legal analysis for any specific jurisdiction;
- certification.


## Positioning

- **What PGF is.** PGF is an operational implementation toolkit. It links legal requirements and risks to processes, roles, decisions, evidence and worked examples.
- **How it relates to NIST.** It complements the risk-based NIST Privacy Framework. NIST is not merely declarative: its Core, Profiles and Implementation Tiers define outcomes and let an organisation select priorities. PGF can help to implement a chosen NIST profile; it does not replace NIST, and its crosswalk is at category level.
- **Three kinds of rule.** Each rule in PGF is one of the following:
  - an applicable legal obligation;
  - an internal rule the organisation adopts (labelled as internal policy where it is stricter than the law);
  - an illustrative default to be calibrated.
- **Proportionality.** Adoption is modular and proportionate. The organisational form, roles and resources scale with the organisation; PGF requires neither a new post nor a new committee, nor every technical test in every context. Applicable legal duties apply from the start regardless of how much of PGF has been adopted (Section 4).
- **Canadian programme examples.** Compact departmental programme overviews such as those of the Canada Revenue Agency and of Innovation, Science and Economic Development Canada are useful examples of the same idea. They concern federal institutions; PGF claims no conformity with them.


## Design principles

1. **Lawfulness before risk.** A legal compliance gate (G-L) runs before any risk decision. It covers lawful basis, conditions for special-category and criminal-offence data, purpose compatibility, transparency, automated decisions, transfer tools and statutory deadlines. No risk appetite, committee decision, metric or opinion can cure a failure.
2. **Independent DPO; accountable decision-makers.**
   - The **controller** is accountable.
   - **Executive Management** decides; the **Governing Body** oversees.
   - An **Executive Privacy Programme Owner (EPPO)** runs the programme.
   - **Processing Owners** take decisions about their processing within delegated limits.
   - The **DPO** advises, monitors, gives advice on every DPIA, cooperates with the supervisory authority and may escalate. The DPO does not authorise processing or accept risk.
   - **Independent Internal Audit** provides assurance.
3. **Statutory gates are explicit:**
   - DPIA triage (G-DPIA);
   - prior consultation for residual high risk (G-36);
   - transfer equivalence with suspension (G-TIA);
   - breach recording and notification on separate GDPR, financial-sector and Canadian tracks.
4. **Calculation is separate from decision.**
   - Document 18 calculates risk on two tracks: risk to individuals' rights and freedoms, and organisational consequences.
   - Document 8 decides what is acceptable and who may accept it.
   - Organisational consequences never offset risk to individuals.
5. **PET metrics are evidence, not legal conclusions.** Anonymity is a contextual legal conclusion (GDPR Recital 26). Pseudonymised, synthetic, encrypted and federated data are distinct states. Differential-privacy claims must state the privacy unit, adjacency relation, accountant and composition.
6. **One authoritative record per fact.** Views, extracts and linked evidence records are allowed, and so are independent statutory records required by law.
7. **Overlay, not duplication.** Data classification, retention and inventory (Documents 10, 11 and 23) are written as privacy overlays on an existing corporate data-governance programme.
8. **Single source for law and tooling.** Document 7 states which requirement applies where. Document 9 is the only connection point to tooling, and the governance core does not depend on any product.


## A four-level operating architecture

The levels connect a mandate to operating rules, repeatable processes and continuing assurance. They are complementary: the policy set does not replace the work, and a process map does not replace ownership or evidence.

Document 02 is the parent Charter. Document 07 records applicable regimes; Document 08 defines appetite and authority; Document 18 defines calculation. DPIA/TIA records feed the RoPA and risk register. Monitoring, audit and reporting close the loop.

The privacy overlays for classification, retention and inventory use existing data-governance assets. Keep one authoritative register for each fact and use references rather than copied inventories.



| Level | Operating purpose | Components |
| --- | --- | --- |
| LEVEL 1 | Mandate, roles, applicability and appetite | 01-09 |
| LEVEL 2 | Policies, assessment methods and registers | 10-23 |
| LEVEL 3 | Processes, ownership and staffing | 24-26 |
| LEVEL 4 | Assurance, metrics, review and reporting | 27-31 |



## Roles and decision boundaries

The controller remains accountable. PGF assigns programme operation, calculation, advice, business decisions and assurance to distinguishable roles. One record identifies the effective decider.

An EPPO can be an existing executive; the framework does not require a new job title. The worked bank uses a CPO. The DPO's statutory advice and monitoring remain independent of programme operation and acceptance of business risk.



| Role | Primary contribution |
| --- | --- |
| Executive Management | Adopts policy, delegates authority and decides above delegated limits. |
| Governing Body | Oversees; receives assurance and gives reserved consent where its rules provide. |
| EPPO | Operates the privacy programme, maintains policy and coordinates implementation. |
| Processing Owner | Owns the business processing and its DPIA; decides within delegation. |
| DPO | Advises, monitors, escalates and records dissent; does not accept the controller's risk. |
| Privacy operations / engineers | Prepare the assessment and calculation, operate tooling and retain evidence. |
| Independent Internal Audit | Provides independent assurance over the programme. |



## From evidence to a business decision

Every record should connect the business objective and expected benefits to the processing design, its consequences and a responsible decision. The decision can be conditional, refused or sent for redesign without rewriting the computed tier.

**The common route**
1. Identify the processing, data and parties using classification, RoPA and inventory records.
2. Record the applicable legal position and any material uncertainty. A reasoned disputed position is distinguishable from an established missing prerequisite or prohibition.
3. Perform DPIA triage and the assessment where required; obtain DPO advice.
4. Apply the versioned calculation project and retain individual observations.
5. Evaluate prior consultation and, for transfers, the applicable transfer route.
6. Obtain the authorised business decision and record benefits, individual and organisational consequences, alternatives, DPO/Legal advice, the response, conditions and review date.
7. Update records, monitor conditions and re-assess when facts change.

A low technical indicator does not supply a lawful basis, an anonymity conclusion or a valid transfer mechanism. Conversely, a technical observation is not an automatic substitute for the calculated business-risk category. Documents 08, 18, 19 and 20 keep these decisions visible and connected.



## The risk model: one integrated route

The versioned project passport selects the scenario, inputs, thresholds, weights and calibration before a case is evaluated. For the PET disclosure scenario, the normalised weighted indicator maps directly to a likelihood band; likelihood and severity then use Document 08's matrix.

For identified-processing scenarios the threat-based sum uses the project's documented exposure, threat, control and event factors. Do not add an undisclosed minimum-band override or choose another project simply to obtain a preferred result.

The indicator is ordinal, not a calibrated probability of harm. The following ranges are the worked bank's illustrative calibration, not legal thresholds.



| Integrated indicator I | Likelihood band |
| --- | --- |
| 0 ≤ I < 0.5 | Low |
| 0.5 ≤ I ≤ 1.0 | Medium |
| 1.0 < I ≤ 2.0 | High |
| I > 2.0 | Near-certain (ordinal label) |


Individual deviations, uncertainty, attack observations and DPO dissent accompany the result. Missing/invalid selected weighted inputs make the calculation incomplete; they are not replaced with zero. Legal requirements, evidence needed for a privacy claim and adopted budget/release conditions remain separate. No new logarithmic or exponential calibration is introduced.


## Worked case: synthetic calibration data

**Illustrative case - Documents 18 and 19.** A fictional bank needs a synthetic dataset to calibrate a credit-scoring model. It uses a versioned project and the PAMOLA implementation profile to compute metrics and compile evidence. Training/calibration and production credit decisions have separate assessment records.

The first generator's selected weighted metrics produce the following contributions. Extra diagnostic observations and the actual DP parameters remain visible but do not trigger an automatic replacement of the integrated tier.



| Weighted metric | Normalised value | Weight | Contribution |
| --- | --- | --- | --- |
| MIA accuracy | 0.400 | 0.25 | 0.100 |
| MIA AUC | 0.700 | 0.25 | 0.175 |
| DCR P5 | 0.789 | 0.25 | 0.197 |
| NNDR median | 0.733 | 0.25 | 0.183 |


Using the unrounded input calculation, I = 0.656. This maps to Medium likelihood. With Significant severity, the Document 08 matrix gives Medium residual risk. The figure is not a 65.6% probability.

The generator has ε = 2.1 and δ = 8 × 10^-6, differing from the selected project configuration (ε ≤ 2.0 at δ = 10^-9). The Group DPO records the concern and the business owner chooses redesign. The computed tier stays Medium. This illustrates why score and business/release decision are distinct.


## Worked case: decision and continuing evidence

The reconfigured generator has ε = 1.8 at δ = 10^-9. Its indicator is 0.537, again giving Medium likelihood and Medium residual risk for the disclosure scenario. A separate source-data misuse scenario also gives Medium. The DPIA records the complete scenario assessment; it does not infer the production model's fairness from this synthetic-data result.

The Processing Owner records the conditional decision, DPO advice and review/expiry conditions. The first generator is not retroactively treated as approved. Because its output was observable, its privacy loss remains in the cumulative ledger.

**Illustrative ledger:** federated run 2.6 + first synthetic run 2.1 + reconfigured run 1.8 = ε 6.5; δ is composed separately under the stated assumptions. The bank's lifetime and annual caps are internal appetite choices, not statutory limits or anonymity guarantees. A budget condition can hold a release without changing its calculated tier.

**One business record retains:** the calibration objective and benefits; the selected project/version; input and metric evidence; the integrated result; consequences for individuals and the organisation; DPO/Legal advice; the business response; release conditions and review triggers.

All numbers and confidence intervals in this case are illustrative. They are not measurements from a supplied product run. A real implementation must identify the privacy unit, mechanism, accountant, configuration, observable outputs and evidence supporting the actual DP statement.



## A phased adoption route


For an organisation that needs a working programme before it adopts all 31 documents:

1. **Mandate and roles.** Adopt the Charter (02) and the RACI (05). Designate the EPPO, the Processing Owners and, where required, the DPO.
2. **Know your law and your processing.** Fill the Regulatory Applicability Matrix (07) and the RoPA (21), then start the Data Inventory (23).
3. **Decide what is acceptable.** Adopt the Risk Appetite Statement (08) with the gates G-L, G-DPIA and G-36.
4. **Operate the statutory processes:** DPIA (19), data subject rights (15), breach response (14), transfers and TIA (12, 20), and vendors (17).
5. **Publish the notice** (01, external part) and train staff (30).
6. **Close the loop.** Set up monitoring and an independent audit (27), a minimal metrics set (28) and board reporting (31).

The other documents add depth: classification, retention, consent, privacy by design, the PET methodology, the process map, the staffing model and the review cycle. Their full documentation can be adopted in phases as the programme matures.

**Phased adoption does not postpone legal duties.** From the start of any processing, the organisation must already:
- apply retention and deletion rules;
- obtain valid consent, and handle its withdrawal, where consent is the lawful basis;
- build data protection by design and by default into any new processing before it launches (Art. 25).

The documents only formalise these duties. Similarly, Document 18 must be in place before any decision or release that relies on its method.


## Strategic documents: mandate and interfaces




### 01 Privacy Policy and Notice

[Complete component](../PGF/01_Privacy_Policy_EN.md)

**Purpose:** the organisation's top-level data protection policy (01A, internal), together with the external privacy notice for a data-subject domain such as customers (01B).

**Contents:** data protection principles (GDPR Art. 5); controller and DPO identification; purposes with lawful bases and Art. 9 conditions; Art. 13/14 disclosures, including the source of the data and whether providing it is required; automated decision-making and profiling, with meaningful information about the logic; the right to object; recipients, transfers and retention; data subject rights; the right to complain.

**Relationships:** draws on the Charter (02) and the Regulatory Applicability Matrix (07). Other domain notices must not conflict with it.


### 02 Privacy Governance Charter

[Complete component](../PGF/02_Privacy_Governance_Charter_EN.md)

**Purpose:** establishes the programme - its objectives, mandate, governance bodies, decision rights and boundaries. It is the parent document of the model.

**Contents:** definitions of the roles (controller, Executive Management, Governing Body, EPPO, Processing Owner, DPO, Internal Audit); what is governed and who governs (Section 4); roles, mandates and decision rights, including the Processing Owner mandate (Section 8); the governance tiers - Oversight / Management / Execution, with the DPO and the Processing Owner outside the tiers (Section 9; detailed in Document 04); DPO independence and escalation; the governance gates; the programme's processes.

**Relationships:** parent of Documents 03, 04 and 05. Frames all other documents.


### 03 Privacy Governance Interface and Integration Model

[Complete component](../PGF/03_Privacy_Interface_Integration_Model_EN.md)

**Purpose:** defines interfaces with other corporate functions so that privacy does not duplicate them. The functions are enterprise risk, InfoSec, data governance, Legal, AI governance, IT, HR, Procurement, Finance and, where applicable, sector regimes (for financial entities, DORA ICT risk and incident reporting).

**Contents:** principles for identifying interface points; an interface map; the "no duplicate registers" rule; a conflict-resolution matrix.

**Relationships:** sets the external boundaries applied by Documents 08, 10, 14 and 17.


## Strategic documents: people and responsibility




### 04 Privacy Organisational Design Strategy

[Complete component](../PGF/04_Privacy_Organisational_Design_Strategy_EN.md)

**Purpose:** the strategic decision on the privacy function's position, sourcing, size and budget. The EPPO need not be a new post. Insourcing the DPO is a policy choice, since the GDPR allows a DPO on a service contract.

**Contents:** positioning; reporting lines, including the DPO's direct access to the highest management level; insourcing and outsourcing; headcount and scaling; budget; roadmap.

**Relationships:** operationalised by Document 26; draws on Document 06.


### 05 Privacy RACI Matrix

[Complete component](../PGF/05_Privacy_RACI_Matrix_EN.md)

**Purpose:** the single source of truth on responsibility for every process in the process map, allocated by the nature of each decision.

**Contents:** role list, including the EPPO and the Processing Owner; allocation principles; RACI tables for governing, core and supporting processes, the sub-processes of the process map and the statutory activities; escalation rules, including the recording of reasons when DPO advice is not followed.

**Relationships:** projected into Document 25 and operationalised in 26. Escalation thresholds come from 08.


### 06 Privacy Role Competency Framework

[Complete component](../PGF/06_Privacy_Role_Competency_Framework_EN.md)

**Purpose:** the qualification requirements for each privacy role, expressed vendor-neutrally.

**Contents:** competency profiles; independence requirements; periodic requalification, including AI literacy where relevant; for the DPO, expertise maintained with resources provided by the organisation.

**Relationships:** feeds Document 30; used by 26.


## Strategic documents: applicability, appetite and tooling




### 07 Regulatory Applicability Matrix

[Complete component](../PGF/07_Regulatory_Applicability_Matrix_EN.md)

**Purpose:** maps jurisdictions and sectors to the applicable requirements, so that other documents reference them instead of restating them.

**Contents:** applicability principles; jurisdictions and frameworks, including the competent supervisory authorities under the one-stop-shop; a jurisdiction × requirement matrix; adjacent regimes (DORA, AI Act, NIS2, AML, consumer credit, ePrivacy); a Canadian applicability map (PIPEDA, Québec); pending changes, kept distinct from law in force.

**Relationships:** input to Documents 01, 12, 14, 17, 19 and 20.


### 08 Privacy Risk Appetite Statement

[Complete component](../PGF/08_Privacy_Risk_Appetite_Statement_EN.md)

**Purpose:** the governance decision on which residual risk is acceptable and who may accept it, once the legal compliance gate has been passed.

**Contents:** the risk appetite statement; severity and likelihood scales; tiers mapped to the statutory high-risk test; acceptance authority by tier (Critical is not acceptable); conditional acceptance with an expiry date; an optional cumulative disclosure budget (lifetime ledger per source population); escalation.

**Relationships:** supplies scales and authority to Documents 18-20 and 22. Applied in the process map (24) and reported through 31.


### 09 Privacy Automation and Tooling Strategy

[Complete component](../PGF/09_Privacy_Automation_and_Tooling_Strategy_EN.md)

**Purpose:** which calculations and processes should be automated, and the tool-neutral criteria tooling must meet. It is the only connection point between PGF and any product.

**Contents:** automation principles; selection and approval criteria: reproducibility, evidence integrity, exit and continuity, and, for financial entities, DORA ICT third-party requirements; the tool-agnostic governance boundary; the technology implementation package; re-certification based on documented testing.

**Relationships:** aligned with Documents 04, 07, 12 and 17.


## Policies and standards: data lifecycle




### 10 Data Classification Policy (data-governance overlay)

[Complete component](../PGF/10_Data_Classification_Policy_EN.md)

**Purpose:** the privacy dimension of the corporate classification.

**Contents:** personal-data categories: non-personal, personal, special category (Art. 9), criminal-offence data (Art. 10), vulnerable data subjects; inferred sensitive data; the pseudonymised state; handling rules; declassification only through a documented legal determination.

**Relationships:** feeds Documents 18, 21 and 23.


### 11 Data Retention and Disposal Policy (data-governance overlay)

[Complete component](../PGF/11_Data_Retention_and_Disposal_Policy_EN.md)

**Purpose:** retention by category, purpose, basis, trigger and jurisdiction, with disposal on expiry.

**Contents:** retention principles; a matrix with explicit legal sources and exceptions (no blanket "longest period"); scoped legal holds with a defined release; disposal; derived data.

**Relationships:** draws on Documents 10 and 21; interacts with 15 and 12.


### 12 Cross-Border Data Transfer Policy

[Complete component](../PGF/12_Cross_Border_Data_Transfer_Policy_EN.md)

**Purpose:** rules and mechanisms for transfers outside the EEA.

**Contents:** what counts as a transfer, including remote access; transfer tools; a recipient → mechanism → basis matrix; TIA triggers; supplementary measures; suspension where equivalence cannot be ensured; PET-based joint processing is not an automatic exemption.

**Relationships:** triggers Document 20; recorded in 21.


## Policies and standards: consent, incidents and rights




### 13 Consent Management Policy

[Complete component](../PGF/13_Consent_Management_Policy_EN.md)

**Purpose:** requirements for consent where consent is the lawful basis - form, recording, withdrawal and renewal. Consent does not reduce the severity of harm.

**Contents:** consent standards; age of consent; recording; withdrawal and its propagation; Canadian meaningful-consent and express-consent variants.

**Relationships:** draws on Documents 01, 07 and 10.


### 14 Data Breach Response Policy

[Complete component](../PGF/14_Data_Breach_Response_Policy_EN.md)

**Purpose:** from security event to personal-data-breach determination.

**Contents:** **every** breach is recorded; risk assessment of likelihood and severity; notification to the competent supervisory authority (within 72 hours of awareness where required) and to individuals (where the risk is high); processor duties; a separate DORA track for financial entities; Canadian variants: real risk of significant harm and records of all breaches; the Québec register; The controller decides on DPO advice; disagreement is escalated.

**Relationships:** uses severity concepts from Document 18 and deadlines from 07.


### 15 Data Subject Rights Policy

[Complete component](../PGF/15_Data_Subject_Rights_Policy_EN.md)

**Purpose:** operational fulfilment of rights.

**Contents:** rights and their legal restrictions, including those under anti-money-laundering law; identity verification; one-month deadlines with extension; Art. 22 safeguards and explanations; notification of recipients; Canadian access variants.

**Relationships:** draws on Documents 01, 05 and 10; feeds 27 and 28.


## Policies and standards: design, suppliers and risk




### 16 Privacy by Design and by Default Policy

[Complete component](../PGF/16_Privacy_by_Design_and_by_Default_Policy_EN.md)

**Purpose:** embedding data protection in design and in default settings across the development lifecycle.

**Contents:** Art. 25 design requirements; default settings; legacy systems; a pre-launch gate that includes DPIA triage; illustrative engineering mechanisms.

**Relationships:** draws on Documents 09, 10, 18 and 19.


### 17 Vendor and Third-Party Privacy Risk Policy

[Complete component](../PGF/17_Vendor_and_Third_Party_Privacy_Risk_Policy_EN.md)

**Purpose:** managing processors, joint controllers and independent controllers.

**Contents:** due diligence; the complete Art. 28(3) contract checklist; the sub-processor chain; assistance and notification duties; deletion and return; Art. 26 arrangements; for financial entities, DORA ICT third-party requirements.

**Relationships:** draws on Documents 03, 10 and 18; feeds 22.


### 18 Privacy Risk Assessment Methodology

[Complete component](../PGF/18_Privacy_Risk_Assessment_Methodology_EN.md)

**Purpose:** the calculation core.

**Contents:** risk to individuals' rights and freedoms, with broad harm types and a likelihood based on threats, controls and exposure; organisational consequences on a separate track; a specialised PET assessment module, with integrated scoring and documented observations, for de-identified, synthetic and aggregate releases; composition across repeated releases; versioned risk calculation projects; evidence packs.

**Relationships:** takes its scales from Document 08; used by 14, 19, 20 and 22.


## Policies and standards: assessment and records




### 19 DPIA Methodology and Template

[Complete component](../PGF/19_DPIA_Methodology_and_Template_EN.md)

**Purpose:** DPIA triage and procedure.

**Contents:** triage under Art. 35(1), (3) and (4) and the nine WP248 criteria; DPO advice on every DPIA; a rights-and-freedoms assessment; prior consultation where high risk remains; the interface with the AI Act fundamental-rights impact assessment; the report structure.

**Relationships:** uses Document 18 and the authority table of 08; records in 21 and 22.


### 20 Transfer Impact Assessment Methodology

[Complete component](../PGF/20_Transfer_Impact_Assessment_Methodology_EN.md)

**Purpose:** assesses the destination's laws and practices - enforceable rights and redress, and access by public authorities - together with supplementary measures and re-evaluation.

**Contents:** triage; the legal assessment module; the risk calculation, as a secondary input; the decision: do not start, or suspend, where equivalence cannot be ensured; a Québec variant for communication outside Québec.

**Relationships:** triggered by Document 12; a DPIA (19) may be needed in parallel.


### 21 Record of Processing Activities (RoPA)

[Complete component](../PGF/21_Record_of_Processing_Activities_EN.md)

**Purpose:** the Art. 30 register, in controller and processor variants.

**Contents:** the mandatory field set; the lifecycle of records; the demarcation from the data inventory.

**Relationships:** records results from Documents 19 and 20; draws technical fields from 23.


## Policies and standards: risk and inventory




### 22 Privacy Risk Register

[Complete component](../PGF/22_Privacy_Risk_Register_EN.md)

**Purpose:** the lifecycle of privacy risks above Low.

**Contents:** inherent, residual and target risk; treatment; conditional acceptance with expiry; Art. 36 status; alignment with the enterprise risk register.

**Relationships:** fed by Documents 17, 19 and 20; source for 27 and 31.


### 23 Data Inventory and Data Flow Maps (data-governance overlay)

[Complete component](../PGF/23_Data_Inventory_and_Data_Flow_Maps_EN.md)

**Purpose:** privacy metadata on the corporate data catalogue, and flow maps.

**Contents:** catalogue fields; flow maps covering jurisdictions, remote access and recipients; update rules; lineage of derived datasets.

**Relationships:** source of technical fields for Document 21; triggers Document 20.


## Process model: execution and ownership




### 24 Privacy Governance Process Map

[Complete component](../PGF/24_Privacy_Governance_Process_Map_EN.md)

**Purpose:** the complete process model.

**Contents:** 23 processes in three groups: governing G1-G9, core C1-C5 and supporting S1-S9; value chains and event-driven decompositions with triggers, inputs, outputs, participants and metrics; interfaces to the RACI and owner register, with applicable sub-processes such as transfers, consent, DPIA and prior consultation; APQC-inspired hierarchy only; no APQC PCF conformity or use of PCF identifiers is claimed.


### 25 Process Owner Register

[Complete component](../PGF/25_Process_Owner_Register_EN.md)

**Purpose:** a board- and audit-facing projection of who is accountable for each process and sub-process. It is derived from the RACI (05) and the process map (24) and is not an independent source of truth.

**Contents:** register rows per process and sub-process; the register of Processing Owner mandate holders designated by Executive Management (Section 10).


### 26 Operational Role and Staffing Model

[Complete component](../PGF/26_Operational_Role_and_Staffing_Model_EN.md)

**Purpose:** maps roles to positions.

**Contents:** job descriptions; assignments; vacancy and succession; appointment and removal.

**DPO safeguards:** no penalty for performing DPO tasks; no automatic suspension for a lapsed certificate.


## Assurance, training and governance reporting




### 27 Privacy Audit and Monitoring Programme

[Complete component](../PGF/27_Privacy_Audit_and_Monitoring_Programme_EN.md)

**Purpose:** the DPO's compliance monitoring under Art. 39, kept separate from the independent assurance provided by Internal Audit, which reports to the Audit Committee.

**Contents:** verification criteria by level; schedule; non-conformity classification; independence; data sources.


### 28 Privacy Metrics Dashboard

[Complete component](../PGF/28_Privacy_Metrics_Dashboard_EN.md)

**Purpose:** operational and target metrics, each with a defined denominator, zero-case handling and cut-off.

**Statutory deadlines:** a missed statutory deadline is always escalated, even when the aggregate metric is green.


### 29 Policy Review Cycle

[Complete component](../PGF/29_Policy_Review_Cycle_EN.md)

**Purpose:** review frequency; ad hoc triggers, including regulatory changes recorded in Document 07; change classification; approval by Executive Management or its delegate; versioning.


### 30 Privacy Awareness and Training Programme

[Complete component](../PGF/30_Privacy_Awareness_and_Training_Programme_EN.md)

**Purpose:** baseline training for all staff; role-specific programmes; training for management bodies and Processing Owners; coverage of contractors; frequency; tracking; escalation.


### 31 Governance Reporting Template

[Complete component](../PGF/31_Governance_Reporting_Template_EN.md)

**Purpose:** reporting to Executive Management and the Governing Body.

**Contents:** metrics drawn only from Document 28; the High-risk profile, including the status of prior consultations; audit, incident and decision status; decisions requested.


## The process model in operation

Every privacy decision follows the same path:
1. Trigger: an initiative, a request, an incident or a regulatory change.
2. Classification and inventory (Documents 10, 21, 23).
3. Legal compliance gate (G-L).
4. DPIA triage (G-DPIA) and, where needed, a DPIA with DPO advice.
5. Calculation (Document 18).
6. Prior-consultation test (G-36), evaluated for every DPIA; consultation of the competent supervisory authority where high risk remains.
7. Decision by the single authorised decider (Document 8).
8. Records: RoPA, risk register and evidence pack.
9. Monitoring and reporting.

Transfers add the transfer-equivalence gate (G-TIA). Breaches follow Document 14, with a separate track for each notification regime.

The process map contains **23 processes**: G1-G9 (governing), C1-C5 (core) and S1-S9 (supporting). Document 25 identifies the current mandate holder and deputy; Document 26 describes the operational roles and capacity.

An evidence hand-off records what has been calculated and by whom, which conditions remain, the decider, advice and response, and the record updates. Reuse the existing RoPA, risk register and inventory identifiers. Avoid creating parallel registers for a PDF or a tool.



## Standards: mapping rather than certification

See [STANDARDS_CROSSWALK.md](../PGF/STANDARDS_CROSSWALK.md). In brief:
- **GDPR / EDPB.** The architecture covers the controller's core obligations: lawfulness, transparency, rights, design, processors, records, breaches, DPIA, DPO and transfers.
- **NIST Privacy Framework 1.0.** PGF maps conceptually to all five functions:
  - Identify-P, Govern-P and Control-P in substance;
  - Communicate-P in part;
  - Protect-P through the interface with the security programme.
- **ENISA.** The pseudonymisation and data protection engineering reports inform the PET module and privacy by design.
- **Canada.** PGF maps to the programme elements of *Getting Accountability Right with a Privacy Management Program*, with PIPEDA and Québec variants. Other Canadian regimes are named as extensions.

These are conceptual mappings, not claims of conformity.

The detailed crosswalk is in the editable supplement. It is a navigation aid: a mapped category does not establish satisfaction of every legal provision or normative clause. Adopters select applicable jurisdictions, roles and sectors, then retain the actual evidence used.

Security and sector programmes keep their own owners. PGF defines interfaces rather than absorbing the full security, enterprise-risk, AI-governance or financial-sector rulebook.



## Transfers and Canadian adaptation

**Transfer routes.** Documents 12 and 20 distinguish applicable adequacy routes, Article 46 safeguards/TIA work and exceptional derogations. A technical PET result is evidence about a design; it does not establish the legal route.

**EU-U.S. DPF, UK Extension and Swiss-U.S. DPF.** Use the official Data Privacy Framework List for the particular recipient and route. Record the legal entity, relevant framework participation, covered data/service scope, verification date and the evidence retained. Do not infer eligibility from a vendor's brand alone or assume that one route covers every transfer. Re-check when parties, services or certification status change.

**Canada.** The programme-level adaptation uses PIPEDA accountability guidance and the applicable provincial/sector regime, including Quebec's private-sector framework. A Canadian accountable privacy officer is not automatically the same role as a statutory EU DPO. The crosswalk references *Getting Accountability Right with a Privacy Management Program* and selected departmental programme examples; those examples are not a single universal Canadian law.

The source catalogue holds 44 selected entries, source IDs, official URLs, scope/status notes and review information. It is selective and contains a watchlist distinct from binding sources. Use the current applicable primary text before relying on an obligation or commencement date.



## PAMOLA: a concrete implementation example

Tool-neutral templates and named worked implementations coexist. In Part B, PEP denotes the fictional bank's PAMOLA implementation profile, including any separately integrated systems. A workflow requirement does not prove that one released product already implements it.

**Traceable hand-off**
1. Specialists define the project context, protected population/unit, adversary, output channel and versioned parameters.
2. The implementation computes the configured metrics, arithmetic, indicator and matrix lookup.
3. The evidence pack links configuration, inputs, results, uncertainty, limitations and run identity.
4. The DPIA/TIA uses the evidence together with human contextual and legal assessments.
5. The authorised business role records a decision, conditions and the response to DPO advice.

**Evidence labels:** measured results need actual build/run/configuration and output artefacts; illustrative numbers are assumptions; specified capabilities are requirements; implemented, tested and deployed are distinct claims; unavailable or unverified evidence is a limitation. The examples in this release are illustrative, not product benchmarks.

PGF can be implemented with another tool or an appropriate controlled process. No tool output takes over the controller's legal or business decision.



## Limits, provenance and version control

The method and thresholds have not been independently calibrated against real incidents or attack outcomes. The targeted checks establish selected arithmetic and integration, not empirical validity, anonymity, legal compliance or product capability. All adoption decisions require a context-specific assessment.

The GDPR is the baseline. Canadian material is programme-level adaptation; UK and Swiss material is selective. Corporate governance in the worked bank uses a German two-tier example and must be mapped to the adopter's actual structure. Security and sector rules remain interfaces.

**Provenance and interests.** The internal source set was developed in the context of REALM INVEO, which develops privacy-engineering software. Alexey Neyman and Val Khvatov are the authors. REALM INVEO is the confirmed rights holder. Named implementation examples are disclosed as such, without claiming external certification or independent peer review.

**Version basis.** The substantive method is the rc.2 freeze (commit 4feefbcbc75ba2abdba252981288dd820c68ee7c). Version 1.0.0 completes rights/licence metadata and publication presentation. The earlier freeze remains available. Advanced companions are separately versioned and excluded from this deposit; their older tests are not evidence of 1.0.0 conformance.

For future versions, record the source version, configuration, changed assumptions, affected examples and validation scope. A revised calibration does not silently rewrite an earlier decision.



## Selected primary references I

These are selected primary-source entry points. The complete curated catalogue, verification scopes and status notes are in the editable supplement. Links are not substitutes for checking the applicable text.

**EU-GDPR** - General Data Protection Regulation - Regulation (EU) 2016/679. [Official source](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng).

**EU-SCC-2021** - Standard Contractual Clauses - Commission transfer resources (Decision (EU) 2021/914). [Official source](https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/standard-contractual-clauses-scc_en).

**EU-ADEQUACY** - European Commission register of adequacy decisions. [Official source](https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/adequacy-decisions_en).

**WP29-DPO-243** - Guidelines on Data Protection Officers - WP243 rev.01. [Official source](https://www.cnil.fr/sites/default/files/atoms/files/guidelines_on_dpos_5_april_2017.pdf).

**WP29-DPIA-248** - DPIA and high-risk processing - EDPB endorsement of WP248 rev.01. [Official source](https://www.edpb.europa.eu/documents/guideline/data-protection-impact-assessments-high-risk-processing_en).

**EDPB-TRANSFER-01-2020** - Recommendations 01/2020 - supplementary transfer measures. [Official source](https://www.edpb.europa.eu/documents/recommendation/recommendations-012020-on-measures-that-supplement-transfer-tools-to_en).

**EDPB-PBD-04-2019** - Guidelines 4/2019 - Article 25, data protection by design and by default. [Official source](https://www.edpb.europa.eu/documents/guideline/guidelines-42019-on-article-25-data-protection-by-design-and-by-default_en).

**US-DPF-LIST** - Data Privacy Framework List (U.S. Department of Commerce) - participating organisations. [Official source](https://www.dataprivacyframework.gov/list).

**CH-US-DPF** - Swiss-U.S. Data Privacy Framework - FDPIC announcement and DPF Swiss FAQ. [Official source](https://www.edoeb.admin.ch/en/15082024-new-swiss-us-data-privacy-framework).




## Selected primary references II

These are selected primary-source entry points. The complete curated catalogue, verification scopes and status notes are in the editable supplement. Links are not substitutes for checking the applicable text.

**NIST-PF-1-0** - NIST Privacy Framework - Version 1.0. [Official source](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.01162020.pdf).

**NIST-IR-8062** - NIST IR 8062 - Privacy engineering and risk management in federal systems. [Official source](https://csrc.nist.gov/pubs/ir/8062/final).

**NIST-800-226** - NIST SP 800-226 - Guidelines for Evaluating Differential Privacy Guarantees. [Official source](https://csrc.nist.gov/pubs/sp/800/226/final).

**ENISA-ENGINEERING-2022** - ENISA - Data Protection Engineering. [Official source](https://www.enisa.europa.eu/publications/data-protection-engineering).

**CA-PIPEDA** - Personal Information Protection and Electronic Documents Act (PIPEDA). [Official source](https://laws-lois.justice.gc.ca/eng/acts/P-8.6/).

**CA-QC-PRIVATE** - Act respecting the protection of personal information in the private sector - P-39.1. [Official source](https://www.legisquebec.gouv.qc.ca/en/document/cs/P-39.1).

**CA-OPC-PROGRAMME** - OPC/OIPC - Getting Accountability Right with a Privacy Management Program. [Official source](https://www.priv.gc.ca/en/privacy-topics/privacy-laws-in-canada/the-personal-information-protection-and-electronic-documents-act-pipeda/pipeda-compliance-help/pipeda-compliance-and-training-tools/gl_acc_201204/).

**CA-OPC-BREACH** - OPC - Mandatory reporting of breaches of security safeguards. [Official source](https://www.priv.gc.ca/en/privacy-topics/privacy-for-businesses/privacy-breaches-at-your-business/gd_pb_201810/?seq_no=2).

**CJEU-XFAB-C453-21** - CJEU - X-FAB Dresden, C-453/21. [Official source](https://eur-lex.europa.eu/legal-content/en/TXT/?uri=CELEX%3A62021CJ0453).




## Licence, citation and the release files

**Copyright (c) 2026 REALM INVEO.** Authors: **Alexey Neyman; Val Khvatov**.

The original PGF framework text, templates, figures and original documentation in this record are licensed under **Creative Commons Attribution 4.0 International (CC BY 4.0)**. Users may share and adapt the licensed material, including commercially, subject to the licence terms. Give appropriate credit, link to the licence and indicate changes; do not imply endorsement.

External laws, standards and other third-party material retain their own terms. Product and organisation names do not grant trademark rights. The editable-document supplement excludes software utilities and raw/internal source materials. No separate software licence is created by this documentation licence.

[Licence and legal code](https://creativecommons.org/licenses/by/4.0/).

**Citation:** Neyman, A., & Khvatov, V. (2026). *Privacy Governance Framework (PGF): Framework Overview and Component Guide* (Version 1.0.0). REALM INVEO. Use the version DOI shown in the Zenodo record.

**Files:** this master overview; the complete editable framework ZIP; a validation-scope summary; a licence notice/full legal code; a README and checksums. The overview and editable supplement belong to one versioned publication record. Use the record's version DOI to identify a stable edition.

Document 18 and the remaining detailed components are in the editable ZIP. The master and supplement should be versioned together; retain the exact record/version when citing a component.

