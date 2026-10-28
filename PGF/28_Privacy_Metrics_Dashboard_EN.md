---
title: "Privacy Metrics Dashboard"
document_id: PGF-28
level: 4
release_version: 1.0.0
status: publication-ready
authors: ["Alexey Neyman", "Val Khvatov"]
regulatory_reference_date: 2026-10-26
licence: "CC BY 4.0"
rights_holder: "REALM INVEO"
source_provenance: "Derived from internal source set ver.2: Level4/28. Privacy-Metrics-Dashboard_ENG.docx.md; sha256 96d6552201103cad901600a6c2adcd1d10e9e6fd397f0b7afc477bbc9553d56b"
---

# PGF-28 — Privacy Metrics Dashboard

*Privacy Governance Framework (PGF) · Level 4 — Control, Reporting and Improvement · Version 1.0.0 · Regulatory reference date: 26 October 2026*

> **Status and use.** Part A is a reusable template. Part B is a worked example for a fictional organisation (PanEuropean Bank AG); the named implementation profile identifies a real product; the Bank, deployment, figures, dates and records in Part B are illustrative. Nothing in this document is legal advice or a statement about any real organisation, product or provider.

# **About This Document**

**Purpose.** Document 28 is the single source of metric definitions for the privacy programme. It defines the Charter-goal metrics (Section 5) and the operational catalogue (Section 6), gives every metric of every process and sub-process of the Privacy Governance Process Map (Document 24) a stable identifier, and fixes for each metric its denominator, the treatment of zero cases and the cut-off rule. It also sets the publication cycle, data-quality rules and the thresholds that feed the master escalation matrix (Document 31, Section 6.4).

**Scope.** Programme-level indicators for day-to-day management of the programme by the Executive Privacy Programme Owner (EPPO) and the Privacy Operations Lead. Risk metrics of an individual assessment (likelihood, severity, PET-module metrics) belong to the Privacy Risk Assessment Methodology (Document 18); this document aggregates their outcomes.

**Relationships.** Each process card of Document 24 names its metrics; this document defines them (Section 6.10). The Privacy Audit and Monitoring Programme (Document 27) measures the audit and monitoring metrics independently and passes them on (Section 6.5). The Governance Reporting Template (Document 31) selects metrics from this catalogue for reporting and introduces none of its own. The Policy Review Cycle (Document 29) and the Privacy Awareness and Training Programme (Document 30) feed the review and training metrics.

# **How to Use This Document**

Part A is a template. Text in ***[square brackets, bold italic]*** is a placeholder or an illustrative value. Blocks marked **Guidance** are removed from the adopted version. Part B shows the template completed for the fictional PanEuropean Bank AG. Metric identifiers (CG-nn for Charter-goal metrics; M-<process>-nn for operational metrics) are the same in Part A and Part B, so that Documents 24, 27, 29, 30 and 31 can cite them.

> **Guidance.** Before drafting this document, confirm that the Charter (Document 2, Section 6) states measurable programme objectives — Section 5 operationalises them — and that the Process Map (Document 24) names the metrics of each process. If a process card has no metrics, close the gap in Document 24 and define the metric here; do not invent a parallel set elsewhere.

# **Table of Contents**

* Part A — Template: 1. Purpose · 2. Scope · 3. Dashboard Principles · 4. Roles and Responsibilities · 5. Charter-Goal Metrics · 6. Operational Metrics Catalogue (6.0 Metric definition standard; 6.1–6.9 headline metrics; 6.10 Process metric catalogue) · 7. Update Frequency and Publication · 8. Data Quality and Validation · 9. Automation and Tooling · 10. Thresholds and Escalation · 11. Access, Distribution and Boundary with Reporting · 12. Relationship to Other Framework Documents · 13. Review and Amendment · 14. Approval
* Part B — Worked Example (fictional): PanEuropean Bank AG, Sections 1–14
* Normative Basis and References
* Document History (PGF)

# **Part A — Template**

***Privacy Metrics Dashboard — [Full legal name of the organisation]***

Effective date: ***[DD Month YYYY]*** · Version: ***[x.x]*** · Document owner: ***[Privacy Operations Lead]*** · Accountable: ***[EPPO]*** · Approved by: ***[EPPO under delegation from Executive Management; Sections 5 and 6.6 — Executive Management]***

***Version History***

| Version | Date | Changes |
| :---- | :---- | :---- |
| ***[1.0]*** | ***[DD.MM.YYYY]*** | ***[Initial version of the document]*** |
| ***[x.x]*** | ***[DD.MM.YYYY]*** | ***[Brief description of material changes]*** |

> **Guidance.** Record only material changes: adding or removing a metric (Sections 5–6), changing a definition, denominator, zero-case or cut-off rule, a target or tolerance, the publication cycle (Section 7) or the thresholds (Section 10). A routine update of metric values is the operating cycle (Section 7), not a new version.

## **1. Purpose of the Document**

This document is Document 28 of the Privacy Governance Framework (PGF), the second document of Level 4 "Control, Reporting and Improvement". It sets out the continuously updated set of metrics for the management of the privacy programme — for example, open data subject requests, the share of requests answered within the statutory period, overdue DPIAs, the distribution of current residual-risk decisions by tier, breach notification timeliness — and the metrics that measure achievement of the programme objectives set in the Charter (Section 5).

The dashboard is a management tool. It gives the EPPO, the Privacy Operations Lead and process owners a current picture of the programme between reporting cycles, so that deviations are corrected before the next programme report (Document 31).

> **Guidance.** This document does not create a new source of privacy facts. It defines indicators derived from the records that the processes already keep (RoPA, Privacy Risk Register, Data Inventory, rights-request log, breach record, consent system, learning management system). A missing metric is closed here and named in the Document 24 card; it is never invented in a report.

The dashboard in raw form is not a board paper. Selection, trend interpretation and the rationale for requested decisions are prepared through the Governance Reporting Template (Document 31, Section 11).

## **2. Scope**

* Charter-goal metrics (Section 5) and operational metrics for every process and sub-process of the Process Map (Document 24) — governing (G1–G9, including G4.1, G4.2, G5.1), core (C1–C5, including C2.1–C2.3) and supporting (S1–S9, including S6.3 and the S7 and S8 sub-rows) — with an identifier per metric (Section 6.10)
* Does not replace or duplicate the RoPA (Document 21), the Privacy Risk Register (Document 22) or the Data Inventory (Document 23): the dashboard holds derived indicators, not copies of entries (the "no duplicate registers" rule, Document 3, Section 4)
* Does not replace the assessment-level metrics of Document 18 (likelihood and severity factors; PET-module metrics, including the criteria of singling out, linkability and inference from Article 29 Working Party Opinion 05/2014 on Anonymisation Techniques (WP216)); this document counts programme-level outcomes of those assessments
* Applies to all metrics, whether collected automatically (Section 9) or supplied manually by process owners
* Does not define the content or cadence of the programme report — that is Document 31; this document is its only metric source

## **3. Dashboard Principles**

* **Single definition.** This document is the only source of metric definitions. Document 31 selects and presents a subset and introduces no metric of its own; Document 24 names metrics and cites their identifiers
* **SMART definitions.** Every metric states its owner, source, numerator, denominator (or unit for counts and durations), zero-case rule, cut-off rule, frequency and target and tolerance (Section 6.0)
* **Statutory deadlines are hard limits.** A missed statutory deadline is a breach of obligation. It is listed per case, recorded in the issues log (Document 27, Section 10) and escalated under the master escalation matrix (Document 31, Section 6.4) even when the aggregate metric is green. Statutory metrics have a target of 100% (or 0 misses) and no tolerance band
* **No incentive against protection.** Approval rates, the share of initiatives that "passed", or the ratio of DPO advice followed are never targets. Where such information is useful for programme design it is a diagnostic indicator without target, owned by the EPPO
* **DPO independence.** Metrics about the DPO's statutory tasks measure timeliness, coverage and documentation only. They are never used to assess the content of the DPO's advice, nor in performance or disciplinary decisions about the DPO (GDPR Art. 38(3)); counts of contacts to the DPO are reported only in aggregate (Art. 38(5)) (Section 6.6)
* **No duplicate registers.** A metric may draw on register data, but the dashboard never becomes an alternative register (Document 3, Section 4)
* **Data quality before publication.** A value is published only after validation (Section 8); an unvalidated value carries a status flag
* **Proportionate frequency.** Frequency follows the speed at which the indicator can change and the risk involved (Section 7)
* **Use or remove.** A metric that supports no decision, monitoring task or objective is a candidate for removal at the next review (Section 13); statutory metrics are never removed while the duty applies

## **4. Roles and Responsibilities**

This section mirrors the participants of the "Metrics and KPIs" governing process (Document 24, Section 4.8; Document 5, row G7). Where they differ, Document 5 prevails.

| Role | Involvement | Comment |
| :---- | :---- | :---- |
| ***[Privacy Operations Lead]*** | ***[Responsible]*** | ***[Maintains the definitions; collects, validates, aggregates and publishes the dashboard (Section 7)]*** |
| ***[EPPO]*** | ***[Accountable]*** | ***[Accountable for the dashboard as part of running the programme; approves changes to the operational catalogue (Section 13)]*** |
| ***[DPO]*** | ***[Consulted]*** | ***[Advises on definitions; has read access to the whole dashboard for its own monitoring task (Art. 39(1)(b)); supplies the aggregate figures on its own statutory tasks (Section 6.6); does not approve the dashboard]*** |
| Process owners (the Accountable role in the Document 24 card; Document 25) | ***[Responsible for supply]*** | ***[Supply their process metrics on time and are accountable for their accuracy]*** |
| ***[Privacy Officer(s) / Privacy Engineer(s) / Data Protection Coordinator(s)]*** | ***[Consulted]*** | ***[Source of manually collected values (Section 9)]*** |
| ***[Independent Internal Audit]*** | ***[Informed]*** | ***[Uses the dashboard as a source of facts and reconciles it against audit evidence (Document 27); does not prepare it]*** |
| ***[Executive Management]*** | ***[Informed]*** | ***[Receives the programme report (Document 31) and the escalations of Section 10; adopts changes to Sections 5 and 6.6]*** |
| ***[Governing Body committee (Risk Committee)]*** | ***[Informed]*** | ***[Receives the programme report (Document 31); not a recipient of the raw dashboard]*** |

> **Guidance.** "Process owner" here means the Accountable role of a Document 24 process (Document 25). It is not the Processing Owner, who is the business owner of a processing activity and decides within its delegation (Document 5, Section 3). A Processing Owner reads the metrics of its own activities (Section 11).
## **5. Charter-Goal Metrics**

This category operationalises the programme objectives of the Charter (Document 2, Section 6). Each metric expresses one objective; none is invented independently. If the organisation's Charter words its objectives differently, align this section with the Charter, not with the example below. Where a Charter-goal metric is the same as an operational metric, it reuses the operational definition (Section 6) and is not collected twice.

> **Guidance.** Charter-goal metrics are reviewed in the reporting cycle (Document 31) and in the annual review (Section 13), not through the weekly threshold logic of Section 10. Two exceptions apply to every metric in this section: (1) events that are escalation triggers in their own right — a missed statutory deadline, a corrective order or fine of a supervisory authority — are escalated as events under the master escalation matrix (Document 31, Section 6.4) as soon as they occur; (2) a value outside tolerance is placed in the next programme report with a decision request (Document 31, Section 8).

| ID | Metric | Definition (numerator ÷ denominator; unit) | Zero case · Cut-off | Type · Target / tolerance |
| :---- | :---- | :---- | :---- | :---- |
| CG-01 | Regulatory compliance | (a) Material findings of supervisory authorities in inspections or investigations closed in the period (count); (b) missed statutory deadlines in the period (count = cases listed in M-C3-02 and M-S7-13, and misses in M-S7-05, M-S7-06, M-G4.1-01) | 0 is a valid value · event date (finding notified; deadline expired) | S · 0 / no tolerance; each case escalated as an event |
| CG-02 | Managing privacy as a risk | = M-C2-14: new or materially changed processing launched in the period with G-L and G-DPIA recorded before launch and, where required, a completed DPIA and residual-risk decision ÷ all such launches | "none in period" · go-live date | S · 100% / no tolerance |
| CG-03 | Protecting data subjects' interests | = M-C3-01 (statutory response period) and M-C3-12 (human review of automated decisions within the internal target) | per the referenced metrics | S and K · M-C3-01 100%; M-C3-12 ***[≥ X%]*** |
| CG-04 | Trust supported by evidence | Privacy due-diligence questionnaires from partners and institutional clients answered by the agreed date with evidence-pack references ÷ questionnaires due in the period | "none due" · due date | K · ***[≥ X%]*** / ***[tolerance Y%]*** |
| CG-05 | Privacy as a condition for using data | Lawful initiatives completed through the data transformation model ÷ lawful initiatives closed in the period (initiatives stopped at G-L reported separately and excluded) | "none closed" · closure date | D · no target, no tolerance (reference value used only for programme-design review) |
| CG-06 | Accountability backed by evidence | = M-C2-17: above-Low residual-risk decisions with a sealed evidence pack ÷ above-Low decisions taken in the period | "none in period" · decision date | K · 100% / ***[tolerance]*** |
| CG-07 | Efficiency through automation | Change of the median DPIA cycle time (intake to decision) against the documented baseline period, provided M-C2-03 stays at 100% | n/a before the baseline is set · decision date | K · ***[reduction of X% by date]*** / ***[Y p.p. behind plan]*** |
| CG-08 | Resilience to change | Days from the publication of a new or amended requirement in the official journal (or the official source) to the adopted change of the model; the change must in any case be in force before the date of application if that is earlier | "none in period" · adoption date of the change | K · ***[≤ X days and before the date of application]*** |

> **Guidance.** CG-05 is diagnostic on purpose. A target for the share of initiatives that "go through" creates pressure to approve; a low value is a prompt to review the design of the transformation model, never a reason to relax a gate. Do not add marketing-reach metrics (for example "campaigns referring to privacy practices"): they measure promotion, not protection, and privacy claims in marketing carry their own legal risk.

## **6. Operational Metrics Catalogue**

### **6.0 Metric definition standard**

Every metric in Sections 5 and 6 is defined with the fields below. The catalogue tables show the fields that vary; the owner and source are those of the process card in Document 24 unless stated.

| Field | Content |
| :---- | :---- |
| Identifier | CG-nn (Charter goal) or M-<process code>-nn (e.g. M-C3-01; sub-processes: M-G4.1-01). Identifiers are never reused after a metric is retired |
| Owner and source | Accountable role of the process (Document 25) and the system of record from which the value is extracted |
| Numerator / denominator | For ratios, the cases counted and the population they are counted against; for counts and durations, the unit |
| Zero-case rule | Z1 — ratio with an empty denominator: reported as "none due" or "none in period", never as 100% and never shown green. Z2 — count: 0 is a valid value. Z3 — duration: no cases → "n/a"; otherwise median and 90th percentile (P90) are reported, never an average alone, and for statutory clocks the maximum as well |
| Cut-off rule | K1 — event date: a case counts in the period in which the event occurred (receipt, awareness, decision, go-live); the period closes at 24:00 local time at head office on its last day; late-recorded cases are added to the correct period with a correction flag (Section 8). K2 — due date: statutory and deadline metrics count the cases whose deadline fell in the period; a case still open after its deadline is counted as missed at the cut-off; cases not yet due are shown as "open, not yet due". K3 — snapshot: stock metrics are measured at the cut-off time |
| Type | S — statutory: a legal duty or deadline; target 100% or 0 misses, no tolerance, every miss listed and escalated (Section 10). K — key indicator with an internal target and tolerance. R — monitored trend: direction only. D — diagnostic: no target, no tolerance, no zones; used only for analysis by its owner |
| Target, tolerance, zones | Target — the level the organisation aims for. Tolerance — the limit beyond which management action is mandatory. Zones: green = at or better than target; amber = worse than target but within tolerance; outside tolerance = an escalation level under Section 10. The target never lies inside the amber zone, and the green zone never extends beyond the target |
| Frequency | Publication cycle (Section 7) |

> **Guidance.** Do not include current values in this document — they belong to the live dashboard (Section 9). Do not express a statutory metric with a green band below 100%: a 98% "green" response rate hides two breaches of obligation.

### **6.1 Data Subject Rights (C3)**

| ID | Metric | Definition | Zero · Cut-off | Type · Target / tolerance |
| :---- | :---- | :---- | :---- | :---- |
| M-C3-01 | Requests answered within the statutory period | Requests answered within one month of receipt, or within a validly notified extension (Art. 12(3): by two further months where necessary, the data subject informed of the extension and its reasons within the first month) ÷ requests whose deadline fell in the period | Z1 "none due" · K2 (deadline computed from the date of receipt) | S · 100% / no tolerance |
| M-C3-02 | Requests overdue | Requests whose statutory deadline has passed without an answer, listed per case with owner and reason | Z2 · K2 | S · 0 / each case escalated |
| M-C3-03 | Time to fulfil, by right | Business days from receipt to answer, by right (Arts. 15–22) | Z3 · K1 (answer date) | K · median ***[≤ internal target]***; P90 ***[≤ Y]*** |
| M-C3-07 | Requests received, by type | Count of requests received, by right and channel | Z2 · K1 (receipt) | R |
| M-C3-08 | Extensions notified | Requests with a notified extension ÷ requests whose deadline fell in the period | Z1 · K2 | R (a rising share is reviewed; extensions are lawful only where necessary) |
| M-C3-09 | Requests awaiting identity information | Open requests in which additional information under Art. 12(6) has been requested | Z2 · K3 | R |
| M-C3-10 | Refusals, by ground | Requests refused in whole or part, by ground (Art. 12(5); restriction under Art. 23 law; inability to identify, Art. 11(2)) | Z2 · K1 (answer date) | R |
| M-C3-11 | Open requests | Requests received and not yet answered | Z2 · K3 | K · ***[≤ X]*** / ***[tolerance Y]*** |
| M-C3-12 | Human review of automated decisions | Requests for human intervention or contest under Art. 22(3) answered within the internal target ÷ such requests whose internal target date fell in the period | Z1 · K2 | K · ***[≥ X%]*** |

> **Guidance.** Set the target for M-C3-11 from the expected stock, not from intuition. By Little's law the expected number of open requests equals the intake rate multiplied by the time a request spends in the system: the law uses the arithmetic mean time in the system, not the median. An intake of 2 requests per day and a mean time in the system of 15 calendar days (counted from receipt to answer, with the same boundaries as M-C3-03) give a steady-state stock of about 30 open requests, i.e. about two weeks of intake (not one). The result is a planning approximation for a stable intake, not a forecast. The median and P90 of M-C3-03 remain separate metrics (durations of 15, 15 and 60 days have a median of 15 but a mean of 30, which would double the expected stock). Statutory compliance is measured by M-C3-01 and M-C3-02, never by an average response time.

### **6.2 DPIA, Risk Decisions and Prior Consultation (C2, S5, G2)**

| ID | Metric | Definition | Zero · Cut-off | Type · Target / tolerance |
| :---- | :---- | :---- | :---- | :---- |
| M-C2-14 | Launches with gates recorded before go-live | New or materially changed processing launched with G-L and G-DPIA recorded before go-live and, where required, a completed DPIA and residual-risk decision ÷ all launches and material changes in the period | Z1 · K1 (go-live) | S · 100% / each miss escalated |
| M-C2-03 | DPIAs with recorded DPO advice before the decision | DPIAs decided in the period with the DPO's advice recorded before the decision ÷ DPIAs decided in the period (Art. 35(2)) | Z1 · K1 (decision) | S · 100% |
| M-C2-04 | DPIAs with a recorded G-36 conclusion | DPIAs decided in the period with the G-36 conclusion and reasons recorded ÷ DPIAs decided in the period | Z1 · K1 (decision) | S · 100% |
| M-C2-05 | Overdue DPIAs | DPIAs in progress past their planned decision date, including DPIAs paused while awaiting a business response; paused DPIAs are shown as a separate line with their original due date and ageing. A new date counts only if a replan is approved and recorded, and the original date stays visible. A paused or overdue DPIA never permits launch (M-C2-14) | Z2 · K3 | K · target 0 / ***[tolerance X]*** |
| M-C2-16 | PET-module assessments with complete individual results | PET-module assessments (Document 18) in which every mandatory metric, review observation and the WP216 criteria (singling out, linkability, inference) are recorded individually, without averaging ÷ PET-module assessments completed in the period | Z1 · K1 | K · 100% |
| M-C2-17 | Above-Low decisions with an evidence pack | Residual-risk decisions above Low with a sealed evidence pack ÷ residual-risk decisions above Low taken in the period | Z1 · K1 (decision) | K · 100% |
| M-C2-09 | Prior consultations | Open prior consultations (Art. 36), listed with submission date, information requests from the supervisory authority and status; consultations closed in the period, with those in which the authority's written advice required changes or the authority used Art. 58 powers | Z2 · K3 (open); K1 (closed) | R · listed per case |
| M-S5-06 | Current residual-risk tiers, track (a) | Processing activities with a current residual-risk decision in the Privacy Risk Register by tier (Low, Medium, High) ÷ processing activities with a current decision (one record per activity) | Z1 · K3 | K · High ***[≤ X%]***; Critical: always 0 — a Critical record means processing stopped or not started (Document 8) |
| M-S5-07 | Organisational consequences, track (b) | Current track (b) levels, reported separately and never netted against track (a) | Z2 · K3 | R |
| M-S5-08 | High decisions | High residual-risk decisions taken in the period, listed with the single decider, the G-36 conclusion and the consultation status | Z2 · K1 (decision) | R · listed per case |
| M-S5-04 | Conditional acceptances past expiry | Conditional acceptances whose expiry date has passed without re-assessment | Z2 · K3 | K · 0 |
| M-S5-05 | Conditional acceptances expiring next quarter | Conditional acceptances whose expiry falls in the next quarter, listed | Z2 · K3 | R · listed |
| M-G2-05 | Cumulative disclosure-budget utilisation | Recorded privacy loss (ε, δ) per source population ÷ the limit set in Document 8; new spending in the calendar year ÷ any annual pacing cap | n/a where no budget applies · K3 | K · the Document 8 limit is a hard limit; ***[warning level X%]*** |

### **6.3 Vendors and Cross-Border Transfers (S6, C4)**

| ID | Metric | Definition | Zero · Cut-off | Type · Target / tolerance |
| :---- | :---- | :---- | :---- | :---- |
| M-S6-02 | Vendors reassessed on cadence | Counterparties whose reassessment fell due in the period and was completed by the due date (Document 17) ÷ counterparties whose reassessment fell due | Z1 · K2 | K · ***[100%]*** / ***[tolerance]*** |
| M-S6-05 | Counterparties with open non-conformities | Counterparties with at least one open privacy non-conformity | Z2 · K3 | R · listed |
| M-S6-06 | Overdue reassessments | Reassessments past their due date | Z2 · K3 | K · 0 |
| M-S6-07 | Critical ICT arrangements without a tested exit strategy | ICT services supporting critical or important functions without an exit strategy tested within its cycle (DORA; financial entities) | Z2 · K3 | K · 0 |
| M-C4-02 | Art. 46 transfers with a current TIA | Art. 46 transfers whose TIA was re-evaluated by its due date ÷ Art. 46 transfers whose re-evaluation fell due | Z1 · K2 | K · 100% |
| M-C4-07 | TIAs past their planned date | TIAs in progress past their planned completion date | Z2 · K3 | K · 0 |
| M-C4-03 | Transfers not started or suspended after a failed G-TIA | Count, listed with dates (a failed G-TIA is applied, not overridden) | Z2 · K1 | R · listed |
| M-C4-06 | Transfers on hold with G-TIA incomplete | Transfers whose G-TIA status is incomplete and which are on hold, listed with the days on hold and the date of the next legal step | Z2 · K3 | R · listed |

### **6.4 Training and Awareness (S8)**

The frequency of this category is ***[monthly]***: coverage does not change materially on a weekly horizon.

| ID | Metric | Definition | Zero · Cut-off | Type · Target / tolerance |
| :---- | :---- | :---- | :---- | :---- |
| M-S8-01 | Mandatory training completed on time | Persons in scope whose completion deadline fell in the period and who completed by the deadline ÷ persons whose deadline fell in the period | Z1 · K2 | K · ***[≥ X%]*** / ***[tolerance]*** |
| M-S8-05 | Mandatory training coverage | Persons in scope with a valid completion ÷ persons in scope (employees, and contractors and temporary staff with access to personal data — Document 30, Section 2) | Z1 · K3 | K · ***[≥ X%]*** / ***[tolerance]*** |
| M-S8-06 | Management-body training | Members of the management body who completed the periodic privacy and ICT-risk briefing in the last 12 months ÷ members in office (Document 30, Section 7) | Z1 · K3 | K · 100% |
| M-S8-07 | Contractor coverage | Contractors and temporary staff with access to personal data and a valid baseline completion ÷ such persons | Z1 · K3 | K · ***[≥ X%]*** |
| M-S8-09 | AI literacy | Persons operating or using AI systems on the organisation's behalf with a valid AI-literacy completion ÷ such persons | Z1 · K3 | K · ***[≥ X%]*** |
| M-S8-08 | Awareness reach | Aggregate reach of awareness activities (for example, unique intranet readers, campaign attendance); never tracked per person | Z2 · K1 | D |

### **6.5 Audit and Monitoring (G6)**

These metrics are measured by Document 27 and passed in; the dashboard does not recalculate them. Values change when a monitoring activity or audit engagement is completed, not on the weekly cycle.

| ID | Metric | Definition | Zero · Cut-off | Type · Target / tolerance |
| :---- | :---- | :---- | :---- | :---- |
| M-G6-01 | Coverage | Map processes covered by DPO monitoring (G6.1) or an internal-audit engagement (G6.2b) within the cycle ÷ processes planned for the cycle | Z1 · K3 | K · 100% by cycle end / ***[behind plan by ≤ X p.p.]*** |
| M-G6-03 | Remediation on schedule | Issues-log items closed by their agreed date ÷ items whose agreed date fell in the period | Z1 · K2 | K · ***[≥ X%]*** / ***[tolerance]*** |
| M-G6-04 | Recurring non-conformities | Non-conformities recorded again for the same process and criterion in the following cycle | Z2 · K1 | K · 0 |
| M-G6-05 | DPO monitoring plan completion | Monitoring activities completed ÷ activities in the DPO's own plan for the period (reported by the DPO; a shortfall is a resource signal under Art. 38(2), not a performance measure) | Z1 · K2 | R |
| M-G6-06 | Internal-audit privacy engagements completed | Privacy engagements completed ÷ privacy engagements in the internal-audit plan approved by the Audit Committee for the period (reported by the Chief Audit Executive) | Z1 · K2 | R |
| M-G6-07 | Issues-log items past their remediation date | G-L failures, missed statutory deadlines and audit or monitoring findings past their agreed remediation date | Z2 · K3 | K · 0 |

### **6.6 DPO Statutory Tasks — Timeliness, Coverage and Documentation**

This category measures whether the conditions for the DPO's statutory tasks are in place and whether the controller uses them (GDPR Arts. 35(2), 38, 39). It does not measure the content or "quality" of the DPO's advice, and no metric in this section may be used in the performance assessment, remuneration or any disciplinary matter concerning the DPO (Art. 38(3)). Changes to this section are adopted by ***[Executive Management]*** after consulting the DPO (Section 13).

| ID | Metric | Definition | Zero · Cut-off | Type · Target / tolerance |
| :---- | :---- | :---- | :---- | :---- |
| M-C2-03 | DPIAs with recorded DPO advice | See Section 6.2 (a controller duty under Art. 35(2)) | — | S · 100% |
| M-C2-18 | DPO advice by the agreed date | Advice requests answered by the date agreed with the DPO ÷ requests whose agreed date fell in the period; a shortfall is analysed as a resource question (Art. 38(2)) | Z1 · K2 | R |
| M-C2-11 | Departures from DPO advice with reasons recorded | Decisions not following the DPO's advice with the decider's reasons recorded ÷ decisions not following the DPO's advice (a decider duty) | Z1 · K1 (decision) | K · 100% |
| M-G6-05 | DPO monitoring plan completion | See Section 6.5 | — | R |
| M-G8-05 | DPO report delivered | The DPO's report to the highest management level (G8.2) delivered in the period (yes / no); content not measured | — · K1 | R |
| M-C3-13 | Contacts to the DPO | Contacts from data subjects to the DPO (Art. 38(4)) received and acknowledged within the internal target; aggregate counts only, no content or identity (Art. 38(5)) | Z2 · K1 | R |
| M-S8.1-01 | DPO awareness-raising activities | Awareness-raising activities organised by the DPO (Art. 39(1)(b)); count only | Z2 · K1 | R |
| M-C2-10 | Decisions departing from DPO advice | Count of decisions not following the DPO's advice, by process (owned by the EPPO; programme diagnostic) | Z2 · K1 | D |
| M-C1-07 | Committee decisions departing from DPO advice | Count of Privacy Risk Committee decisions on non-standard Risk Calculation Projects not following the DPO's advice | Z2 · K1 | D |
| M-C2-19 | Retrospective review of advice not followed | Cases in which advice was not followed and a later breach, audit finding or supervisory-authority position concerned the same issue (owned by the EPPO; used for lessons learned only) | Z2 · K1 | D |

> **Guidance.** Do not set a target for the share of DPO advice that is "confirmed" in hindsight or for the distribution of advice outcomes. Such ratios are structurally biased — advice that is followed rarely produces the incident that would "confirm" it — and a target would pressure the DPO to soften or harden advice to meet a number. The DPO's own report (G8.2) may present the DPO's view of these figures.

### **6.7 Incidents and Personal Data Breaches (S7)**

Definitions follow Document 14: every personal data breach is recorded (Art. 33(5)); harm and risk determine notification only. GDPR and DORA tracks are reported separately.

| ID | Metric | Definition | Zero · Cut-off | Type · Target / tolerance |
| :---- | :---- | :---- | :---- | :---- |
| M-S7-01 | Detection to containment | Hours from detection of a security event affecting personal data to containment (S7.1) | Z3 · K1 (detection) | K · median ***[≤ X h]***; P90 ***[≤ Y h]*** |
| M-S7-02 | First report to completed qualification | Hours from first credible report to completed breach qualification (S7.2) | Z3 · K1 (first report) | K · ***[internal target, Document 14]*** |
| M-S7-03 | Breaches recorded | Personal data breaches entered in the breach record ÷ breaches qualified in the period (Art. 33(5)) | Z1 · K1 (qualification) | S · 100% |
| M-S7-04 | Supervisory-authority notifications within 72 hours | Notifications to the competent (lead) supervisory authority made within 72 hours of becoming aware ÷ notifications due in the period. "Due" = every breach not concluded, with reasons, to be unlikely to result in a risk, whose 72-hour point fell in the period — including notifications still unsent at the cut-off. Reasons for delay do not make a late notification timely. The 72 hours are an outer limit: the duty is to notify without undue delay (Art. 33(1)) | Z1 "none due" · K2 (72-hour point from awareness) | S · 100% |
| M-S7-13 | Late or overdue notifications | Each notification sent more than 72 hours after awareness, and each due notification still unsent at the cut-off, listed per case with: hours since awareness; whether the reasons for the delay were given (Art. 33(1)); Legal's assessment, with the DPO's advice, of whether the delay was justified (EDPB Guidelines 9/2022 accept justified delays only exceptionally); every case escalated under Document 31, Section 6.4 | Z2 · K3 | S · 0 / each case escalated |
| M-S7-14 | Late notifications with reasons stated | Late notifications accompanied by reasons for the delay ÷ late notifications in the period (a separate statutory element, never netted with M-S7-04) | Z1 · K1 (notification) | S · 100% |
| M-S7-05 | Communications to data subjects | Breaches assessed as high risk for which data subjects were informed without undue delay, or an Art. 34(3) exception was recorded ÷ breaches assessed as high risk in the period | Z1 · K1 (assessment) | S · 100% |
| M-S7-06 | DORA reports on time | Initial, intermediate and final reports on major ICT-related incidents submitted within the time limits of Commission Delegated Regulation (EU) 2025/301, each measured from its own point of reference (Document 14, Section 5.4) ÷ reports due (financial entities only) | Z1 · K2 | S · 100% |
| M-S7-07 | Recurring breaches | Breaches with the same root cause as an earlier breach within 12 months | Z2 · K1 | K · 0 |
| M-S7-08 | Breaches recorded, by severity | Count of personal data breaches recorded in the period, by severity (Document 14, Section 3) | Z2 · K1 | R |
| M-S7-09 | Breaches notified and communicated | Count notified to the supervisory authority; count communicated to data subjects | Z2 · K1 | R |
| M-S7-10 | DORA major ICT-related incidents | Count of major ICT-related incidents reported to the financial supervisor (separate track) | Z2 · K1 | R |
| M-S7-11 | Processor notifications to client controllers | Breaches affecting client data notified to the client controller without undue delay and within the contractual term ÷ such breaches (S7.5) | Z1 · K1 | K · 100% |
| M-S7-12 | Open breach follow-up actions | Remediation actions from breach records open past their agreed date | Z2 · K3 | K · 0 |

### **6.8 Dashboard Data Quality (G7)**

| ID | Metric | Definition | Zero · Cut-off | Type · Target / tolerance |
| :---- | :---- | :---- | :---- | :---- |
| M-G7-01 | Metrics supplied on time | Metrics received from process owners by the publication cut-off ÷ metrics due in the cycle | Z1 · K2 | K · ***[≥ X%]*** |
| M-G7-02 | Time to publication | Hours from period close to publication | Z3 · K1 | K · ***[≤ X h]*** |
| M-G7-04 | Inconsistencies with audit evidence | Metrics found inconsistent with evidence in the annual reconciliation (Section 8) ÷ metrics reconciled | Z1 · K1 (reconciliation) | K · ***[≤ X%]*** |
| M-G7-05 | Corrected publications | Published values corrected afterwards with a correction flag | Z2 · K1 | R |

### **6.9 Regulatory Engagement (G4.1, G4.2)**

| ID | Metric | Definition | Zero · Cut-off | Type · Target / tolerance |
| :---- | :---- | :---- | :---- | :---- |
| M-G4.1-01 | Supervisory-authority deadlines met | Requests, orders and inquiries of a supervisory authority answered by the authority's deadline ÷ those whose deadline fell in the period; each miss listed | Z1 · K2 | S · 100% |
| M-G4.1-03 | Corrective measures and fines | Corrective measures (Art. 58(2)) and administrative fines (Art. 83) received, listed | Z2 · K1 | S · 0 / each escalated as an event |
| M-G4.1-04 | Open supervisory commitments past their date | Commitments made to a supervisory authority past their agreed date | Z2 · K3 | K · 0 |
| M-G4.1-05 | Complaints and inquiries via authorities | Complaints forwarded and inquiries opened by supervisory authorities, by type | Z2 · K1 | R |
| M-G4.2-01 | Authority access requests reviewed by Legal | Public-authority and law-enforcement access requests assessed by Legal before any disclosure ÷ requests answered | Z1 · K1 | K · 100% |

### **6.10 Process Metric Catalogue (Document 24)**

This table gives an identifier and a definition to every metric named in the Document 24 process cards, including the sub-processes. Metrics already defined in Sections 6.1–6.9 are referenced, not repeated. Owner and source are those of the process card (Document 24, Part A, Sections 4–6; owners per Document 25). Unless stated otherwise, durations use Z3 (median and P90) and K1, ratios use Z1, counts use Z2. Targets marked ***[X]*** are set by the organisation; "0" and "100%" targets are fixed by the nature of the control.

| ID | Process | Metric | Definition (numerator ÷ denominator or unit) | Cut-off | Type · Target |
| :---- | :---- | :---- | :---- | :---- | :---- |
| M-G1-01 | G1 | Time from trigger to adopted strategy | Days from the triggering event to adoption | K1 (adoption) | R |
| M-G1-02 | G1 | Strategy cycles completed on schedule | Cycles completed by the planned date ÷ cycles due | K2 | K · ***[X%]*** |
| M-G1-03 | G1 | Unscheduled strategy revisions | Count per year | K1 | R |
| M-G1-04 | G1 | Strategic priorities delivered on schedule | Priorities delivered by their date ÷ priorities due | K2 | K · ***[X%]*** |
| M-G2-01 | G2.1, G2.2 | Time since the last appetite / methodology review | Days since the last completed review, per document | K3 | K · ≤ review interval (Document 29) |
| M-G2-02 | G2 | Reviews started on schedule | Reviews started by the planned date ÷ reviews due | K2 | K · 100% |
| M-G2-03 | G2 | Decisions needing a documented deviation from the authority table | Decisions recorded with a deviation note ÷ residual-risk decisions in the period | K1 | D |
| M-G2-04 | G2 | Disagreements between ERM and privacy tiers | Count of cases recorded | K1 | R |
| M-G2-05 | G2.1 | Cumulative disclosure-budget utilisation | → Section 6.2 | — | — |
| M-G3-01 | G3 | Time from organisational change to RACI update | Days | K1 (update) | K · ***[X days]*** |
| M-G3-02 | G3 | Changes not reflected at quarter-end | Count | K3 | K · 0 |
| M-G3-03 | G3 | Document 25 / Document 5 discrepancies | Count found in audit or monitoring | K1 | K · 0 |
| M-G3-04 | G3 | Processes without a single Accountable role | Count of processes or sub-processes | K3 | K · 0 |
| M-G4-01 | G4 | Time from publication to assessment | Days from publication of a requirement to the recorded applicability assessment; the date of application is recorded alongside | K1 (assessment) | K · ***[X days]*** |
| M-G4-02 | G4 | Jurisdictions and sources tracked | Count | K3 | R |
| M-G4-03 | G4 | Changes identified externally | Applicable changes first identified by audit or an authority rather than by monitoring | K1 | K · 0 |
| M-G4-04 | G4 | Assessed changes leading to a revision | Revisions ÷ assessed applicable changes | K1 | D |
| M-G4.1-01 | G4.1 | Supervisory-authority deadlines met | → Section 6.9 | — | S · 100% |
| M-G4.1-02 | G4.1 | Time from receipt to registered matter | Days | K1 (receipt) | K · ***[X days]*** |
| M-G4.1-03 | G4.1 | Corrective measures and fines | → Section 6.9 | — | S · 0 |
| M-G4.1-04 | G4.1 | Open supervisory commitments past their date | → Section 6.9 | — | K · 0 |
| M-G4.1-05 | G4.1 | Complaints and inquiries via authorities | → Section 6.9 | — | R |
| M-G4.2-01 | G4.2 | Requests assessed by Legal before disclosure | → Section 6.9 | — | K · 100% |
| M-G4.2-02 | G4.2 | Authority deadlines met | Requests answered by the authority's deadline ÷ requests whose deadline fell in the period (median days reported alongside) | K2 | K · 100% |
| M-G4.2-03 | G4.2 | Disclosures broader than required | Count found in audit or monitoring | K1 | K · 0 |
| M-G4.2-04 | G4.2 | Third-country requests received by importers | Count notified by importers (input to TIA re-evaluation) | K1 | R |
| M-G5-01 | G5 | Time from need to adopted policy | Days | K1 (adoption) | R |
| M-G5-02 | G5 | Policies adopted as overlays | Overlays ÷ policies adopted | K1 | R |
| M-G5-03 | G5 | Policies needing unscheduled review in their first year | Count | K1 | R |
| M-G5-04 | G5 | Processes applying a policy without exceptions | Processes without an open exception ÷ processes in scope of the policy | K3 | R |
| M-G5-05 | G5 | Scheduled reviews completed by the due date | Reviews completed (new version or "reviewed, no changes required") by the due date ÷ reviews due (Document 29, Section 5) | K2 | K · 100% |
| M-G5-06 | G5 | Ad hoc review grounds acted on in time | Grounds on which a review was initiated within the initiation period ÷ grounds whose period ended (Document 29, Section 6) | K2 | K · 100% |
| M-G5-07 | G5 | Policy exceptions past expiry | Count of open exceptions past their expiry date | K3 | K · 0 |
| M-G5.1-01 | G5.1 | Processing changes launched before the notice update | Count | K1 (go-live) | K · 0 |
| M-G5.1-02 | G5.1 | RoPA entries not reflected in the notice | Count | K3 | K · 0 |
| M-G5.1-03 | G5.1 | Time from C2 decision to published notice update | Days | K1 (publication) | K · ***[X days]*** |
| M-G6-01 … M-G6-07 | G6 | Audit and monitoring metrics | → Section 6.5 | — | — |
| M-G6-02 | G6 | Time from plan to report | Days from the start of an engagement or monitoring activity to its report | K1 (report) | R |
| M-G7-01 … M-G7-05 | G7 | Dashboard data quality | → Section 6.8 | — | — |
| M-G7-03 | G7 | Management decisions based on the dashboard | Count of recorded decisions citing a dashboard metric | K1 | R |
| M-G8-01 | G8.1 | Reporting cycles on schedule | Reports presented by the planned date ÷ reports due | K2 | K · 100% |
| M-G8-02 | G8.1 | Time from period close to presentation | Days | K1 (presentation) | K · ***[X days]*** |
| M-G8-03 | G8.1 | Management decisions implemented on schedule | Decisions implemented by their date (with an implementation artefact) ÷ decisions due | K2 | K · ***[X%]*** |
| M-G8-04 | G8.1 | Requests for information beyond the report | Count of additional requests from Executive Management or the Governing Body committee, with their subject (completeness signal) | K1 (meeting) | R |
| M-G8-05 | G8.2 | DPO report delivered | → Section 6.6 | — | R |
| M-G9-01 | G9 | Time from change of head to designation | Days from the change to the Executive Management designation | K1 (designation) | K · ***[X days]*** |
| M-G9-02 | G9 | Designations needing an alternative arrangement | Alternative arrangements ÷ designations | K1 | D |
| M-G9-03 | G9 | Residual-risk decisions by a person not designated | Count | K1 | K · 0 |
| M-G9-04 | G9 | Mandate-register discrepancies | Count found in audit or monitoring | K1 | K · 0 |
| M-C1-01 | C1 | Projects registered or revised | Count | K1 | R |
| M-C1-02 | C1 | Time from initiation to registration, by track | Days | K1 (registration) | K · ***[X days]*** |
| M-C1-03 | C1 | Projects on the non-standard track | Non-standard ÷ projects registered | K1 | D |
| M-C1-04 | C1 | Overdue periodic project reviews | Count | K3 | K · 0 |
| M-C1-05 | C1 | Projects needing unscheduled review after an incident or finding | Such projects ÷ active projects | K1 | R |
| M-C1-06 | C1 | Projects used in C2 before approval | Count | K1 | K · 0 |
| M-C1-07 | C1 | Committee decisions departing from DPO advice | → Section 6.6 | — | D |
| M-C2-01 | C2 | DPIAs initiated / completed | Counts | K1 | R |
| M-C2-02 | C2 | Time from intake to decision, by residual tier | Days | K1 (decision) | K · ***[X days per tier]*** |
| M-C2-03, -04, -05 | C2 | DPO advice, G-36 conclusion, overdue DPIAs | → Section 6.2 | — | — |
| M-C2-06 | C2 | Evidence packs returned for rework | Returned ÷ submitted | K1 | K · ***[≤ X%]*** |
| M-C2-07 | C2 | Approved activities later involved in a breach | Activities with a breach in the period ÷ activities approved in the last 24 months | K1 | R |
| M-C2-08 | C2 | Launches at residual High | High launches ÷ launches | K1 | D |
| M-C2-09 | C2 | Prior consultations | → Section 6.2 | — | R |
| M-C2-10, -11, -18, -19 | C2 | Decisions and DPO advice | → Section 6.6 | — | — |
| M-C2-12 | C2 | Processing needing a retroactive DPIA | Count | K1 | K · 0 |
| M-C2-13 | C2 | Complaints about previously approved processing | Count | K1 | R |
| M-C2-14, -16, -17 | C2 | Gates before go-live; PET-module results; evidence packs | → Section 6.2 | — | — |
| M-C2-30 | C2 (privacy by design, Document 16) | Gate coverage | Launches and material changes with G-L and G-DPIA recorded before go-live ÷ all launches and material changes (same population as M-C2-14) | K1 (go-live) | S · 100% |
| M-C2-31 | C2 (Document 16) | Early engagement | Projects with a privacy design intake before development ÷ projects starting development | K1 | K · ***[≥ X%]*** |
| M-C2-32 | C2 (Document 16) | Defaults changed after launch | Count of defaults made more protective after launch because of a finding | K1 | R |
| M-C2-33 | C2 (Document 16) | Minimum-form handovers | Handovers in pseudonymised or tested synthetic form ÷ all handovers to product or data-science teams | K1 | K · ***[≥ X%]*** |
| M-C2-34 | C2 (Document 16) | Production-data exceptions past expiry | Count | K3 | K · 0 |
| M-C2-35 | C2 (Document 16) | Legacy review coverage | Systems reviewed ÷ systems in the review plan for the period | K2 | K · per plan |
| M-C2-36 | C2 (Document 16) | Design findings closed on time | Findings closed by their due date ÷ findings due | K2 | K · ***[≥ X%]*** |
| M-C2.1-01 | C2.1 | AI systems with a recorded classification | AI systems in C2 with an AI Act classification recorded ÷ AI systems in C2 | K3 | K · 100% |
| M-C2.1-02 | C2.1 | High-risk systems with a FRIA completed or scheduled | High-risk systems with a fundamental-rights impact assessment completed or scheduled before the applicable date ÷ high-risk systems | K3 | K · 100% |
| M-C2.2-01 | C2.2 | Children's-data initiatives with a design record | Initiatives involving children with a recorded safeguards design ÷ such initiatives | K1 | K · 100% |
| M-C2.2-02 | C2.2 | Complaints or authority inquiries on children's data | Count | K1 | R |
| M-C2.3-01 | C2.3 | Legitimate-interest processing with a recorded LIA | Activities on Art. 6(1)(f) with a current LIA ÷ activities on Art. 6(1)(f) | K3 | K · 100% |
| M-C2.3-02 | C2.3 | Joint-control relationships with an arrangement in force | Relationships with an Art. 26 arrangement ÷ joint-control relationships | K3 | K · 100% |
| M-C2.3-03 | C2.3 | Art. 21 objections upheld against LIA-based processing | Count | K1 | R |
| M-C3-01 … M-C3-13 | C3 | Data subject rights | → Sections 6.1 and 6.6 | — | — |
| M-C3-04 | C3 | Requests closed for inability to identify | Such closures ÷ requests answered | K1 | R |
| M-C3-05 | C3 | Refusals overturned or challenged via an authority | Refusals overturned internally or challenged through a supervisory authority ÷ refusals in the last 12 months | K1 | R |
| M-C3-06 | C3 | Complaints about incomplete or incorrect fulfilment | Count | K1 | R |
| M-C4-01 | C4 | Time from identification to proceed decision | Days | K1 (decision) | K · ***[X days]*** |
| M-C4-02, -03, -06, -07 | C4 | TIA currency; failed G-TIA; on hold; TIA backlog | → Section 6.3 | — | — |
| M-C4-04 | C4 | Transfers found without a documented mechanism | Count found in audit or monitoring | K1 | K · 0 |
| M-C4-05 | C4 | Adequacy-based transfers with lapsed recipient eligibility | Count (e.g. recipient no longer certified under an adequacy framework) | K3 | K · 0 |
| M-C5-01 | C5 | Time from withdrawal to halt of reliant processing | Hours | K1 (withdrawal) | K · ***[≤ X h]*** |
| M-C5-02 | C5 | Consent records with complete proof fields | Complete records ÷ active consent records (Art. 7(1)) | K3 | K · 100% |
| M-C5-03 | C5 | Processing after recorded withdrawal | Count found in audit or monitoring | K1 | K · 0 |
| M-C5-04 | C5 | Systemic consent issues escalated | Count | K1 | R |
| M-C5-05 | C5 | Consent withdrawal rate, per purpose | Withdrawals in the period ÷ active consents at the start of the period, per purpose | K1 | D |
| M-S1-01 | S1 | Data classified within the target time | Datasets classified within the target time ÷ new datasets | K1 | K · ***[X%]*** |
| M-S1-02 | S1 | Systems with fully labelled fields | Fully labelled systems ÷ systems in scope | K3 | K · ***[X%]*** |
| M-S1-03 | S1 | Re-classifications found in DPIAs or audits | Count | K1 | R |
| M-S1-04 | S1 | Incidents linked to misclassified data | Count | K1 | K · 0 |
| M-S2-01 | S2.2 | Objects disposed of on time | Objects disposed of by the end of their retention period ÷ objects whose period ended | K2 | K · 100% |
| M-S2-02 | S2.2 | Objects on legal hold, and their age | Count; median and maximum age in days | K3 | R |
| M-S2-03 | S2.2 | Data held beyond its period | Count of findings in audit or monitoring | K1 | K · 0 |
| M-S2-04 | S2.2 | Erasure requests blocked by overdue disposal | Count | K1 | K · 0 |
| M-S3-01 | S3 | Systems with personal data covered by the inventory | Covered ÷ systems with personal data | K3 | K · 100% |
| M-S3-02 | S3 | Time from change to updated entry | Days | K1 (update) | K · ***[X days]*** |
| M-S3-03 | S3 | Inventory / RoPA discrepancies | Count found in audit or monitoring | K1 | K · 0 |
| M-S3-04 | S3 | Transfers not identified in advance | Count | K1 | K · 0 |
| M-S4-01 | S4 | Activities registered within the target time | Activities registered within the target time after the decision ÷ activities decided | K1 | K · ***[X%]*** |
| M-S4-02 | S4 | Entries with all mandatory fields | Complete entries ÷ entries (Art. 30) | K3 | K · 100% |
| M-S4-03 | S4 | RoPA / reality discrepancies | Count found in audit or monitoring | K1 | K · 0 |
| M-S4-04 | S4 | Time to produce the RoPA on request | Hours from a supervisory-authority request to delivery (Art. 30(4)) | K1 | K · ***[≤ X h]*** |
| M-S5-01 | S5 | Time from identification to record | Days | K1 (record) | K · ***[X days]*** |
| M-S5-02 | S5 | Entries reviewed in the last quarter | Entries reviewed ÷ entries due for review | K2 | K · 100% |
| M-S5-03 | S5 | Risks reduced in tier after measures | Records whose tier fell ÷ records with completed measures | K1 | R |
| M-S5-04 … M-S5-08 | S5 | Expiry, tiers, track (b), High decisions | → Section 6.2 | — | — |
| M-S6-01 | S6.1 | Time to complete due diligence | Days | K1 (completion) | K · ***[X days]*** |
| M-S6-02, -05, -06, -07 | S6 | Reassessment, non-conformities, exit strategies | → Section 6.3 | — | — |
| M-S6-03 | S6.2 | Processor contracts with all Art. 28(3) terms | Compliant contracts ÷ processor contracts in force | K3 | K · 100% |
| M-S6-04 | S6 | Incidents at previously approved vendors | Count | K1 | R |
| M-S6.3-01 | S6.3 | Transactions with a privacy workstream from the start | Such transactions ÷ transactions started | K1 | K · 100% |
| M-S6.3-02 | S6.3 | Post-closing processing changes routed through C2 | Changes routed ÷ post-closing changes | K1 | K · 100% |
| M-S7-01 … M-S7-14 | S7.1–S7.5 | Incidents and breaches | → Section 6.7 | — | — |
| M-S8-01, -05 … -09 | S8 | Training and awareness | → Section 6.4 | — | — |
| M-S8-02 | S8 | Role-based programmes updated in the last year | Programmes updated in the last 12 months ÷ role-based programmes | K3 | K · 100% |
| M-S8-03 | S8 | Human-factor incidents before and after training | Count per cohort before and after completion | K1 | R |
| M-S8-04 | S8 | Post-training assessment results | Correct answers ÷ questions answered (aggregate, by module) | K1 | R |
| M-S8.1-01 | S8.1 | DPO awareness-raising activities | → Section 6.6 | — | R |
| M-S9-01 | S9 | Time from request to validated capability | Days | K1 | R |
| M-S9-02 | S9 | Availability | Available hours ÷ scheduled hours | K1 | K · ***[≥ X%]*** |
| M-S9-03 | S9 | Assessments performed with validated tooling | Assessments in the classes of mandatory automation using a tested and deployed capability ÷ such assessments (Document 9, Section 8.5) | K1 | K · ***[X%]*** |
| M-S9-04 | S9 | Incidents caused by tool failure | Count | K1 | K · 0 |
| M-S9-05 | S9 | Open validation findings | Count (Document 9, Section 8.3) | K3 | R |
| M-S9-06 | S9 | Fallback periods | Count and cumulative business days of manual fallback (Document 9, Section 8.5) | K1 | K · ***[≤ X days]*** |
| M-S9-07 | S9 | Evidence-pack lead time | Business days from calculation to sealed evidence pack | K1 | K · ***[≤ X]*** |
## **7. Update Frequency and Publication Procedure**

* The baseline cycle of the operational catalogue (Section 6) is ***[weekly]***; metrics collected automatically (Section 9) may be refreshed more often. Section 5 metrics follow the reporting cycle; categories 6.4 and 6.5 follow their own frequency (Sections 6.4, 6.5)
* Statutory metrics (type S) are additionally monitored case by case: a missed statutory deadline is escalated when it occurs, not at the next publication (Section 10)

> **Guidance.** The steps below mirror the "Metrics and KPIs" process (Document 24, Section 4.8). Do not introduce a sequence of steps incompatible with the process map.

* Cycle start — on schedule (once per ***[week]***) or when a process closes its reporting period
* Collection — from the process owners, manually or automatically (Section 9)
* Validation and aggregation — completeness, plausibility and conformity with the definitions in Section 6 (Section 8)
* Publication — ***[Privacy Operations Lead]*** publishes for the roles in Section 4 under the access rules of Section 11
* A metric not received by publication is flagged "overdue"; the last value is never shown without the flag
* A metric overdue for ***[2]*** consecutive cycles is recorded as a Medium deviation (Section 10)
* "Overdue" applies to metrics on the baseline cycle (Sections 6.1–6.3, 6.6–6.9 and the corresponding rows of Section 6.10); for categories 6.4 and 6.5 the previous value is carried forward with its actual update date until the category's own cycle ends

## **8. Data Quality and Validation**

* Each metric has one owner accountable for its accuracy — the Accountable role of the corresponding process in Document 24 (Part A, Sections 4–6; owners per Document 25). ***[Privacy Operations Lead]*** aggregates but does not recalculate source data
* Before publication ***[Privacy Operations Lead]*** checks conformity with the definition and flags unexplained changes against the previous cycle
* At least ***[annually]*** dashboard values are reconciled with evidence obtained independently in monitoring or audit (Document 27); the result is metric M-G7-04 (Section 6.8)
* A discrepancy found in reconciliation is resolved by correcting the collection method or the definition (Sections 5–6), not by a one-off change of the published value
* An error found after publication is corrected with a correction flag (M-G7-05); the value history is never rewritten without trace
* Metric data are aggregate. Where a metric is computed from personal data (for example, training completion or contacts to the DPO), the dashboard holds only the aggregate; per-person records stay in their system of record with its own access rules and retention
* Historical values are kept for ***[X years]*** for trend analysis and audit; retention of the underlying records follows Document 11 and the record-keeping rules of each source system

## **9. Automation and Tooling**

* The split between automated and manual collection follows the Privacy Automation and Tooling Strategy (Document 9, Section 3); this document does not select or evaluate tools
* Automated metrics are taken only from capabilities recorded as tested and deployed in the validation record (Document 9, Section 8.1); a metric produced by an unvalidated capability is published with a "not verified" flag
* Manually collected metrics are supplied by the process owner on the cycle of Section 7
* ***[The dashboard is presented in (a business-intelligence tool / a module of the automation tooling / another interface defined in Document 9)]***; manual values are entered into the same interface — no parallel tool is created
* Extending automated coverage is decided under Document 9 (Section 3.2, targeted automation; Section 8.5, annual review); this document records the coverage in force at each version

## **10. Thresholds and Escalation**

This section turns metric values into escalation levels. The addressees and the time limits for each level are those of the master escalation matrix in Document 31, Section 6.4, which applies to Documents 27–31 alike. The level names (Low, Medium, High, Critical) are shared across the framework, but this scale classifies a programme indicator, not the residual risk of a processing activity (Document 8) or an audit non-conformity (Document 27, Section 7).

| Level | Condition for K-type metrics | Condition for S-type (statutory) metrics |
| :---- | :---- | :---- |
| Low | Green, or amber in a single cycle; a single missed publication or one late supply of a value | — (no Low level for a statutory miss) |
| Medium | Amber for ***[2]*** consecutive cycles; a metric overdue for ***[2]*** cycles (Section 7) | — |
| High | Outside tolerance; or a value approaching a limit of the Privacy Risk Appetite Statement (Document 8) | Any single missed statutory deadline or statutory duty (each case), even when the aggregate stays green |
| Critical | A Document 8 limit exceeded (for example, a hard disclosure-budget limit or any Critical residual record not stopped); a systemic failure affecting several processes | Several missed statutory deadlines with a common cause; a miss concerning a supervisory-authority order, a prior consultation or a breach notification to the authority |

* R- and D-type metrics have no thresholds; their owner analyses them and reports material changes in the programme report (Document 31)
* Charter-goal metrics (Section 5) follow the rule stated in Section 5
* For category 6.5 the levels are informational: the escalation of an individual finding follows Document 27, Section 7; the dashboard shows the trend
* A Critical level does not by itself trigger an unscheduled audit; it is an input to the planning of monitoring (G6.1) and of the internal-audit plan (G6.2a) (Document 27, Section 6)

> **Guidance.** Never define a "yellow" or "amber" band for a statutory deadline. The zones of Section 6.0 apply only to K-type metrics; a statutory miss is always at least High, listed by case, recorded in the issues log (Document 27, Section 10) and escalated.

## **11. Access, Distribution and Boundary with Reporting**

* The dashboard in raw form is not a paper for ***[Executive Management]*** or the ***[Governing Body committee]***; selection, trends and decision requests reach them through the programme report (Document 31), which introduces no new metrics
* Full access — ***[EPPO]***, ***[Privacy Operations Lead]***; read access to the whole dashboard — ***[DPO]*** (monitoring under Art. 39(1)(b))
* Access to the metrics of a process — its process owner (Document 24)
* Read access to the metrics of their own processing activities — Processing Owners
* Read access for verification — ***[Independent Internal Audit]*** (Document 27), without the right to change values
* The dashboard is not distributed routinely to external parties. This is without prejudice to the investigative powers of a supervisory authority (GDPR Art. 58(1)(a)) and the duty to cooperate (Art. 31): information requested by an authority is provided in the form it requires (G4.1)

## **12. Relationship to Other Framework Documents**

* Section 5 expresses the programme objectives of the Charter (Document 2, Section 6) and is revised when they change (Section 13)
* Defines the metrics named in every process card of the Process Map (Document 24); Document 24 cites the identifiers of Section 6.10
* Receives the audit and monitoring metrics of the Privacy Audit and Monitoring Programme (Document 27, Section 11) and is reconciled against its evidence (Section 8)
* Is the only metric source of the Governance Reporting Template (Document 31); the master escalation matrix of Document 31, Section 6.4 sets the addressees and time limits for the levels of Section 10
* Receives the review metrics of the Policy Review Cycle (Document 29; M-G5-05, M-G5-06) and the training metrics of the Privacy Awareness and Training Programme (Document 30; Section 6.4)
* Does not duplicate the RoPA (Document 21), the Privacy Risk Register (Document 22) or the Data Inventory (Document 23)
* Uses the tiers of the Privacy Risk Appetite Statement (Document 8, Section 4) and its acceptance rules (Document 8, Section 5); breach metrics follow the Data Breach Response Policy (Document 14); rights metrics follow the Data Subject Rights Policy (Document 15, Section 5); privacy-by-design indicators follow Document 16, Section 8; vendor indicators follow Document 17
* Automated collection follows the Privacy Automation and Tooling Strategy (Document 9)
* Process owners correspond to the Process Owner Register (Document 25); staffing of the Privacy Operations Lead role is a matter for Document 26
* Section 6.6 is the only place where indicators on the DPO's statutory tasks are defined; the Privacy Role Competency Framework (Document 6) and the Privacy Organisational Design Strategy (Document 4) refer to it and do not add DPO performance targets

## **13. Review and Amendment**

This document is reviewed at least ***[annually]*** under the Policy Review Cycle (Document 29) and ad hoc when the Charter objectives change (Document 2, Section 6), when a process is added to or removed from Document 24, when a statutory deadline or a regulatory reporting duty changes (Document 7), or when the reconciliation of Section 8 reveals a systemic collection problem.

* Changes to Section 6 (except Section 6.6) are approved by ***[the EPPO under delegation from Executive Management]***, with the DPO consulted; they are listed in the next programme report (Document 31)
* Changes to Section 5 are adopted by ***[Executive Management]***, because they express the Charter objectives, and are reported to the ***[Governing Body committee]***
* Changes to Section 6.6 are adopted by ***[Executive Management]*** after consulting the DPO; the EPPO may propose but not approve them, because the EPPO is not the DPO's line manager and the section concerns the conditions of the DPO's independent tasks
* Retiring a metric does not delete its historical values; its identifier is not reused

## **14. Approval**

This document was approved by ***[approving body]*** on ***[date]***. Document owner: ***[Privacy Operations Lead]***. Accountable: ***[EPPO]***.

> **Guidance.** Operational approval sits with the EPPO, who is accountable for the programme's metrics (Document 5, row G7). The DPO advises but does not approve the dashboard: the DPO monitors compliance with the programme and must not approve the instrument by which the programme's performance is measured.
# **Part B — Worked Example (fictional)**

> **Implementation example.** In this Part B, PEP denotes the Bank's **PAMOLA implementation profile**, including separately integrated systems. The product is real; the Bank, deployment, configurations, records and numerical results are illustrative. The example demonstrates the intended workflow and is not evidence that every function is implemented in a released product or that these numbers were measured in a product run. See [the implementation profile](../IMPLEMENTATION_PROFILE.md). Part A remains tool-neutral.


***PanEuropean Bank AG — Privacy Metrics Dashboard***

Effective date: 23 October 2026 · Version: 3.0 · Document owner: Privacy Operations Lead · Accountable: Chief Privacy Officer (EPPO) · Adopted by: Management Board (20 October 2026); later changes to Section 6 (except 6.6) approved by the Chief Privacy Officer under the Board's delegation

*Fictional legal entity and fictional organisations, used solely for illustration.*

***Fictional document history (illustrative)***

| Version | Date | Changes |
| :---- | :---- | :---- |
| 1.0 | 1 May 2026 | Initial version (owner then: Group DPO, under the earlier allocation of programme tasks) |
| 2.0 | 21 August 2026 | Section on the Group DPO's role added (former versions 2.0 and 3.0 of the internal draft merged into one version) |
| 3.0 | 20 October 2026 (adopted by the Management Board; effective 23 October 2026, together with Document 8, version 3.0) | Re-baseline to the new role model: Chief Privacy Officer accountable, Group DPO consulted; metric identifiers for all Document 24 processes and sub-processes; denominators, zero-case and cut-off rules; statutory metrics without tolerance bands; target and tolerance defined once; Section 6.6 limited to timeliness, coverage and documentation of the Group DPO's statutory tasks; approval-type ratios made diagnostic |

For each K-type metric in Sections 5 and 6 below, PanEuropean sets a target and a tolerance; S-type metrics have a target of 100% (or zero misses) and no tolerance; R- and D-type metrics have none (Part A, Section 6.0). Current values are not part of this document: they are shown in the dashboard console (Section 9) and, selected, in the programme report (Document 31, Appendix A).

## **1. Purpose of the Document**

This document applies the Privacy Metrics Dashboard to PanEuropean Bank AG. It fixes the Charter-goal metrics (Section 5), the operational catalogue (Section 6) with PanEuropean's targets and tolerances, the publication cycle and the access rules, as at 23 October 2026.

The dashboard gives the Chief Privacy Officer and the Privacy Operations Lead a weekly picture of the programme between the quarterly programme reports (Document 31) — for example, a rise in overdue DPIAs in Digital Banking is visible at the next weekly publication, not only at quarter-end. The Group DPO has read access for its own monitoring.

The raw dashboard is not a paper for the Management Board or the Supervisory Board's Risk Committee; they receive the programme report (Document 31).

## **2. Scope**

* All Charter-goal metrics (Section 5) and the operational metrics of every process and sub-process of PanEuropean's Process Map (Document 24), with the identifiers of Part A, Section 6.10
* Does not duplicate the RoPA, the Privacy Risk Register (the bank's "Conduct & Privacy Risk" extension of the enterprise risk register) or the Data Inventory; uses indicators derived from them
* Does not include assessment-level metrics of Document 18 (for example, the individual PET-module results of the credit-scoring generator); the dashboard counts outcomes across the credit, anti-fraud, customer-service and marketing portfolio
* Covers both metrics collected through the Bank's privacy engineering platform (PEP, illustrative) and metrics supplied manually by the five Privacy Officers (Germany, France, Italy, Spain, Poland), the Privacy Engineers and the Data Protection Coordinators
* Does not include the structure or cadence of the programme report — Document 31

## **3. Dashboard Principles**

* Single definition: Document 31 selects and presents metrics from this catalogue only; for example, the consent withdrawal rate it may show is M-C5-05, defined here
* Statutory deadlines: every data subject request answered after its statutory deadline, every late notification to the Hessian Commissioner for Data Protection and Freedom of Information (Der Hessische Beauftragte für Datenschutz und Informationsfreiheit, HBDI) and every missed deadline of a supervisory authority is listed, entered in the issues log and escalated under Document 31, Section 6.4, whatever the quarterly percentage shows
* No incentive against protection: the share of initiatives completed through the transformation model (CG-05) is diagnostic; no metric rewards approvals
* Group DPO independence: Section 6.6 measures timeliness, coverage and documentation only; its figures are never used in the annual review of the Group DPO, which the Chair of the Management Board conducts and which is limited to conduct, availability and the use of resources (Document 4, Section 7)
* Proportionate frequency: PEP-supplied metrics (C1, C2, the disclosure-budget ledger and S9) are refreshed daily; most others weekly; training (Section 6.4) monthly; audit and monitoring (Section 6.5) when an activity is completed
* Use or remove: a metric that supported no decision during a year is reviewed for removal; statutory metrics are kept

## **4. Roles and Responsibilities**

| Role | Involvement | Comment |
| :---- | :---- | :---- |
| Privacy Operations Lead | Responsible | Maintains the definitions; collects, validates and publishes the dashboard weekly |
| Chief Privacy Officer (EPPO) | Accountable | Accountable for the dashboard; approves changes to Section 6 (except 6.6) under the Management Board's delegation |
| Group DPO | Consulted | Advises on definitions; read access to the whole dashboard for monitoring (Art. 39(1)(b)); supplies the aggregate figures of Section 6.6 |
| Process owners per Document 25 (for example, the Privacy Operations Lead for C3 and S4; the Head of ICT Risk Control for S7.4; HR and the Privacy Operations Lead for S8) | Responsible for supply | Supply their process metrics; accountable for their accuracy |
| Five Privacy Officers, Privacy Engineers, Data Protection Coordinators | Consulted | Source of manually collected values |
| Group Internal Audit | Informed | Read access; annual reconciliation with audit evidence (Document 27) |
| Management Board | Informed | Receives the programme report and escalations; adopts changes to Sections 5 and 6.6 |
| Risk Committee of the Supervisory Board | Informed | Receives the programme report (Document 31); not a recipient of the raw dashboard |
| Processing Owners (for example, the Heads of Credit Decisions, Digital Banking, Marketing, Customer Service, Fraud Prevention; the CIO) | Read access | Metrics of their own processing activities (Section 11) |
## **5. Charter-Goal Metrics**

The metrics below express the eight programme objectives of PanEuropean's Charter (Document 2, Section 6). They are reviewed in the quarterly programme report (Document 31) and the annual review (Section 13). Events captured by CG-01 — a missed statutory deadline, a corrective measure or a fine — are escalated as events under Document 31, Section 6.4 when they occur; a value outside tolerance goes into the next programme report with a decision request.

| ID | Objective (Charter, Section 6) | PanEuropean definition and source | Type · Target / tolerance |
| :---- | :---- | :---- | :---- |
| CG-01 | Compliance with the GDPR, the BDSG and the national law of each country of operation | (a) Material findings of supervisory authorities (HBDI as lead authority; concerned authorities) in the period; (b) missed statutory deadlines in the period (sum of the cases listed in M-C3-02 and M-S7-13, and the misses in M-S7-05, M-S7-06, M-G4.1-01) | S · 0 / no tolerance |
| CG-02 | Managing privacy as a risk | M-C2-14 (G-L, DPIA triage and limits check recorded before production) | S · 100% |
| CG-03 | Protecting customer interests | M-C3-01 (one month, or a validly notified extension under Art. 12(3)); M-C3-12 (Request a Review of an automated credit decision within 5 business days, internal target) | M-C3-01: S · 100%. M-C3-12: K · ≥ 95% / 90%; reported as "none due" until automated credit decisions start (launch planned 1 February 2027, Document 15) |
| CG-04 | Trust supported by evidence | Partner and institutional-client privacy due-diligence questionnaires answered by the agreed date with evidence-pack references ÷ questionnaires due | K · ≥ 95% / 90% |
| CG-05 | Privacy as a condition for using data | Lawful analytics and credit-scoring initiatives completed through the data transformation model ÷ lawful initiatives closed (initiatives stopped at G-L reported separately and excluded) | D · no target; the Charter's reference value of 90% is used only to trigger a review of the transformation model's design, never to judge an individual decision |
| CG-06 | Accountability backed by evidence | M-C2-17 (above-Low decisions with a sealed PEP evidence pack) | K · 100% / any shortfall is outside tolerance |
| CG-07 | Cost efficiency through automation | Reduction of the median DPIA cycle time against the documented pre-rollout baseline period, provided M-C2-03 stays at 100% | K · −30% within 18 months of completing the relevant PEP rollout stage / behind the planned trajectory by more than 10 percentage points |
| CG-08 | Resilience to change | Days from publication of a requirement to the adopted change of PanEuropean's model; the change must be in force before the date of application if that is earlier (Document 7, Section 6) | K · ≤ 90 days and before the date of application / ≤ 120 days where the date of application is later |

The former target metric "marketing campaigns referring to PanEuropean's privacy practices" has been withdrawn: it measured promotion, not protection, and the annual public privacy report (Document 30, Section 6.2) is not a campaign. The former "average response time to a request for human review" is replaced by M-C3-12, a share against a due date, because an average hides late cases.

## **6. Operational Metrics Catalogue**

PanEuropean applies the definitions, zero-case and cut-off rules and identifiers of Part A, Sections 6.0–6.10 without change. The cut-off is 24:00 CET on the last day of the period; the weekly period runs Monday to Sunday. The table below sets PanEuropean's targets and tolerances for the headline metrics. Metrics of Part A, Section 6.10 with a fixed "0" or "100%" apply as stated there; other R- and D-type metrics are monitored without targets in version 3.0.

| ID | Metric | PanEuropean specifics | Type · Target / tolerance |
| :---- | :---- | :---- | :---- |
| M-C3-01 | Requests answered within the statutory period | Deadline computed from receipt; no pause while awaiting identity information (internal rule, Document 15) | S · 100% |
| M-C3-02 | Requests overdue | Each case listed with the responsible Privacy Officer | S · 0 |
| M-C3-03 | Time to fulfil, by right | Business days; internal target 20 business days (Document 15) | K · P90 ≤ 20 business days / P90 ≤ 22 |
| M-C3-11 | Open requests | Planning intake about 2 requests per calendar day (about 730 a year); illustrative mean time in the system 15 calendar days (receipt to answer); expected stock by Little's law 2 × 15 = 30, i.e. about two weeks of intake — a planning approximation for a stable intake; the median and P90 are reported separately (M-C3-03) | K · ≤ 30 / ≤ 45 |
| M-C3-12 | Request a Review within 5 business days | From the planned launch of automated credit decisions; "none due" before | K · ≥ 95% / 90% |
| M-C2-14 | Launches with gates recorded before go-live | Includes Digital Banking app releases that change processing | S · 100% |
| M-C2-03 | DPIAs with recorded Group DPO advice | Advice recorded in the evidence pack before the decision | S · 100% |
| M-C2-04 | DPIAs with a recorded G-36 conclusion | Conclusion recorded by Legal & Compliance (General Counsel) with reasons | S · 100% |
| M-C2-05 | Overdue DPIAs | Paused DPIAs awaiting a business-unit response are included and shown as a separate line with original due date and ageing; a new date only through a replan approved by the Chief Privacy Officer and recorded (definition refined after the first reconciliation, Section 8) | K · 0 / ≤ 3 |
| M-C2-17 | Above-Low decisions with an evidence pack | PEP evidence pack, format EVP-YYYY-NNNN | K · 100% / any shortfall outside tolerance |
| M-S5-06 | Current residual tiers, track (a) | One record per processing activity in the Privacy Risk Register | K · High ≤ 10% / ≤ 15%; Critical always 0 |
| M-S5-04 | Conditional acceptances past expiry | Default expiry 12 months (Document 8) | K · 0 |
| M-G2-05 | Cumulative disclosure-budget utilisation | Retail customer population (privacy unit: one customer); lifetime limit ε ≤ 10.0 and δ ≤ 1×10⁻⁵; operational pacing cap ε ≤ 7.0 of new spending per calendar year (Document 8, Section 3) | K · within the limits (hard limit) / warning at 80% of either lifetime limit |
| M-S6-02 | Vendors reassessed on cadence | Cadence per Document 17, Section 6 | K · 100% / 95% |
| M-S6-07 | Critical ICT arrangements without a tested exit strategy | Core banking platform; Example Cloud Services Pvt Ltd remote support (ICT Risk Control) | K · 0 |
| M-C4-02 | Art. 46 transfers with a current TIA | TIA-CLOUD-01, TIA-PSI-01, TIA-LLM-01 | K · 100% |
| M-C4-06 | Transfers on hold with G-TIA incomplete | Listed with days on hold and the next legal step | R · listed |
| M-S8-01 | Mandatory training completed on time | Learning Hub records | K · ≥ 95% / 90% |
| M-S8-05 | Mandatory training coverage | Employees and in-scope contractors (Document 30, Section 2) | K · ≥ 98% / 95% |
| M-S8-06 | Management-body training | Management Board members (annual briefing, Document 30, Section 7) | K · 100% / any gap reported to the Chair of the Management Board |
| M-S8-09 | AI literacy | Staff operating or using AI systems, including the customer-service assistant and the credit-scoring model | K · ≥ 95% / 90% |
| M-G6-01 | Monitoring and audit coverage | First Group Internal Audit privacy engagement scheduled for Q4 2026 (Document 27) | K · 100% by cycle end / behind plan by ≤ 15 percentage points |
| M-G6-03 | Remediation on schedule | Issues log in the enterprise GRC platform | K · ≥ 90% / 80% |
| M-G6-07 | Issues-log items past their remediation date | Including G-L failures and missed statutory deadlines | K · 0 |
| M-S7-02 | First report to completed qualification | Internal target 4 hours (Document 14) | K · P90 ≤ 4 h / ≤ 8 h |
| M-S7-03 | Breaches recorded | Breach record in the incident management system | S · 100% |
| M-S7-04 | HBDI notifications within 72 hours | Denominator: notifications due in the period, including any still unsent | S · 100% |
| M-S7-13 | Late or overdue HBDI notifications | Listed per case with hours since awareness, reasons given (Art. 33(1)) and General Counsel's assessment with Group DPO advice; each escalated as a statutory item (Document 31, Section 6.4) | S · 0 |
| M-S7-05 | Communications to customers | Where high risk is found | S · 100% |
| M-S7-06 | DORA reports on time | Reports by ICT Risk Control to the ECB / BaFin under Commission Delegated Regulation (EU) 2025/301 (Document 14, Section 5.4) | S · 100% |
| M-G4.1-01 | Supervisory-authority deadlines met | HBDI and concerned authorities | S · 100% |
| M-G7-01 | Metrics supplied on time | By Monday 06:00 CET | K · ≥ 95% / 90% |
| M-G7-04 | Inconsistencies with audit evidence | Annual reconciliation | K · ≤ 5% / 10% |

***6.6 Group DPO Statutory Tasks***

PanEuropean applies Part A, Section 6.6 without additions. The Group DPO supplies M-C2-18, M-G6-05, M-G8-05, M-C3-13 and M-S8.1-01 in aggregate; contacts to the Group DPO are acknowledged within 5 business days (internal target, Document 15) and reported only as counts. The diagnostic indicators M-C2-10, M-C1-07 and M-C2-19 are owned by the Chief Privacy Officer, are reported only in aggregate to the Privacy Risk Committee and the Management Board, and are never used in the Group DPO's annual review. The former rows "quality of recommendations per audit findings", "proportionality of recommendations" and "retrospective confirmation of objections" with targets have been withdrawn (fictional document history, version 3.0).
## **7. Update Frequency and Publication Procedure**

* The baseline cycle of the operational catalogue (Section 6) is weekly, published by 10:00 CET on Mondays; categories 6.4 (training, monthly) and 6.5 (audit and monitoring, on completion) follow their own cycles
* PEP-supplied metrics (C1, C2, the disclosure-budget ledger M-G2-05, S9) are refreshed daily
* Statutory metrics are monitored case by case: the Privacy Operations Lead checks daily for requests, notifications and authority deadlines due within the next five business days and escalates any miss on the day it occurs (Document 31, Section 6.4)
* Cycle start — automatically on Monday 06:00 CET, after the previous week is closed in all sources
* Collection — automatically from PEP; manually from the five Privacy Officers, the Privacy Engineers and the Data Protection Coordinators for the other processes
* Validation and aggregation — by the Privacy Operations Lead by 09:00 CET; publication by 10:00 CET
* A metric not received by publication is flagged "overdue"; a metric overdue for 2 consecutive cycles is a Medium deviation (Section 10)
* In the quarter ended 30 June 2026 (version 1.0 in force from 1 May 2026), 8 of the 9 weekly cycles were published on schedule; the cycle of Monday 8 June 2026 was missed because of planned PEP maintenance and recorded as a Low deviation (M-G7-02)

## **8. Data Quality and Validation**

* Each metric has one owner accountable for its accuracy — the owner of the PanEuropean process in Document 24 (Part B, Section B2) and Document 25; the Privacy Operations Lead aggregates but does not recalculate source data
* Before each weekly publication the Privacy Operations Lead checks conformity with the definitions and flags unexplained changes
* Annually, dashboard values are reconciled with evidence obtained independently in Group DPO monitoring and Group Internal Audit engagements (Document 27); the first full reconciliation is planned with the first Internal Audit privacy engagement (Q4 2026) and will give the first value of M-G7-04
* A discrepancy found in reconciliation is resolved by correcting the method or definition. Example: the Group DPO's monitoring in September 2026 found that overdue DPIAs (M-C2-05) were reported without showing which were paused while a business unit prepared information, and that some paused DPIAs had been given new dates without an approved replan; the definition was refined in version 3.0 (paused DPIAs kept in the count, shown separately with original due date and ageing; new dates only by an approved replan) instead of correcting a single published value
* Errors after publication are corrected with a flag in the publication log (M-G7-05)
* The dashboard holds aggregates only. Training completion per employee stays in the Learning Hub; requests per customer stay in the rights-request log; contacts to the Group DPO stay in the Group DPO's own records
* Historical dashboard values are kept for 5 years (illustrative internal value); retention of source records follows Document 11

## **9. Automation and Tooling**

* The split between automated and manual collection follows the Privacy Automation and Tooling Strategy (Document 9, Section 3)
* PEP (the Bank's privacy engineering platform, illustrative) supplies the C1 and C2 metrics (calculations, PET-module results, evidence packs), the lifetime disclosure-budget ledger (M-G2-05) and the S9 metrics, from capabilities recorded as tested and deployed in the validation record (Document 9, Section 8.1)
* Data subject rights (C3) metrics are extracted from the Data Subject Rights Portal and the rights-request log; consent (C5) metrics from the Consent Manager; breach (S7) metrics from the incident management system; training (S8) metrics from the Learning Hub; RoPA (S4) and register (S5) metrics from those registers. These are not PEP functions; integrating the rights portal and the Consent Manager is a matter of Document 9, Section 3.2 (targeted automation) and its annual review (Document 9, Section 8.5)
* The dashboard is presented in the PEP dashboard console (illustrative); manually collected values are entered by the Privacy Operations Lead into the same interface

## **10. Thresholds and Escalation**

PanEuropean applies Part A, Section 10, with the addressees and time limits of the master escalation matrix in Document 31, Part B, Section 6.4.

| Level | Example at PanEuropean |
| :---- | :---- |
| Low | One weekly publication missed for a technical reason (8 June 2026); M-C2-05 at 1 for one week |
| Medium | Overdue DPIAs in Digital Banking above the target for 2 consecutive weeks; a metric overdue for 2 cycles |
| High | M-S5-06 above 15% High; M-G2-05 at 80% of a lifetime limit; any single access request answered after its statutory deadline; any HBDI notification sent more than 72 hours after awareness, or due and still unsent, whether or not reasons were given (M-S7-13) |
| Critical | A planned release that would exceed the lifetime disclosure budget; several statutory misses with a common cause; a missed deadline in a prior consultation or a missed response to an HBDI order |

## **11. Access, Distribution and Boundary with Reporting**

* The raw dashboard is not a Management Board or Supervisory Board paper; the Chief Privacy Officer presents selected metrics in the quarterly programme report (Document 31)
* Full access — Chief Privacy Officer, Privacy Operations Lead; read access to the whole dashboard — Group DPO and Deputy Group DPO
* Process owners see the metrics of their processes; for example, the Data Protection Coordinator for Credit Decisions sees the C2 metrics of Credit Decisions DPIAs, not those of Digital Banking or Marketing
* Processing Owners see the metrics of their own processing activities
* Group Internal Audit has read access for verification, without the right to change values
* The dashboard is not sent routinely to the HBDI, the concerned supervisory authorities (CNIL, Garante, AEPD, Prezes UODO), customers or other external parties. This is without prejudice to the authorities' investigative powers (GDPR Art. 58(1)(a)) and the duty to cooperate (Art. 31): information an authority requests is provided in the form it requires, through regulator engagement (G4.1)

## **12. Relationship to Other Framework Documents**

* Section 5 expresses the eight objectives of PanEuropean's Charter (Document 2, Section 6); the Charter's reference value for CG-05 is treated as diagnostic (Section 5)
* Defines the metrics of all processes and sub-processes of PanEuropean's Process Map (Document 24, Part B, Sections B2 and B4)
* Receives the audit and monitoring metrics from Document 27 and is reconciled against its evidence
* Is the only metric source of the programme report (Document 31); escalation addressees and time limits follow Document 31, Part B, Section 6.4
* Receives the review metrics from Document 29 and the training metrics from Document 30
* Uses the tiers and limits of Document 8 (Sections 3–5); breach metrics follow Document 14; rights metrics follow Document 15; privacy-by-design targets follow Document 16, Section 8; vendor metrics follow Document 17
* Automated collection follows Document 9; process owners follow Document 25; staffing of the Privacy Operations Lead role follows Document 26

## **13. Review and Amendment**

This document is reviewed at least once a year under the Policy Review Cycle (Document 29) — next scheduled review by 23 October 2027 (planned) — and ad hoc when the Charter objectives change, when a process is added to Document 24, when a statutory deadline or reporting duty changes (for example, on adoption of the Digital Omnibus, which is a proposal at 26 October 2026 — Document 7, Section 5.1), or when reconciliation with audit evidence reveals a systemic problem.

* Changes to Section 6 (except 6.6) — approved by the Chief Privacy Officer under the Management Board's delegation, Group DPO consulted; listed in the next programme report
* Changes to Section 5 — adopted by the Management Board and reported to the Risk Committee of the Supervisory Board
* Changes to Section 6.6 — adopted by the Management Board after consulting the Group DPO
* Retired metrics keep their history; identifiers are not reused

## **14. Approval**

Version 3.0 was adopted by the Management Board of PanEuropean Bank AG on 20 October 2026 and took effect on 23 October 2026, together with Document 8, version 3.0. Document owner: Privacy Operations Lead. Accountable: Chief Privacy Officer. The Group DPO's advice of 14 October 2026 (illustrative) on the definitions of Section 6.6 was followed. This document is not a Supervisory Board reserved consent matter.

# **Normative Basis and References**

* Regulation (EU) 2016/679 (GDPR): Arts. 5(2), 7(1), 12(3) and 12(6), 22(3), 24, 26, 28(3), 30, 31, 33, 34, 35(2), 36, 38(3)–(5), 39(1)(b), 58(1)(a) and 58(2), 83.
* Regulation (EU) 2022/2554 (DORA): Arts. 5, 13(6), 19, 28–30; Commission Delegated Regulation (EU) 2024/1772 (classification of ICT-related incidents) and Commission Delegated Regulation (EU) 2025/301 (content and time limits of incident reports) — for the S7.4 metrics of financial entities.
* Regulation (EU) 2024/1689 (AI Act), as amended by the AI Omnibus: Art. 4 (AI literacy), Art. 27 (fundamental-rights impact assessment) — for M-S8-09 and M-C2.1-02.
* Article 29 Working Party, Opinion 05/2014 on Anonymisation Techniques (WP216) — criteria of singling out, linkability and inference (M-C2-16).
* NIST Special Publication 800-55, *Measurement Guide for Information Security*, Volumes 1 and 2 (December 2024); ISO/IEC 27004:2016 (monitoring, measurement, analysis and evaluation); ISO/IEC 27701:2025 (privacy information management; clause on monitoring and measurement) — bibliographic pointers for the metric definition standard; no conformity is claimed.
* NIST Privacy Framework 1.0 (January 2020), Govern function, category GV.MT-P (monitoring and review) — crosswalk basis.
* Basel Committee on Banking Supervision, *Principles for effective risk data aggregation and risk reporting* (BCBS 239, 2013), and ECB *Guide on effective risk data aggregation and risk reporting* (May 2024) — reference for accuracy, completeness and timeliness of reports to the management body (Part B).
* Little's law (queueing theory: mean number in the system = arrival rate × mean time in the system, for a stable system) — used for the M-C3-11 target.

# **Document History (PGF)**

| Release | Date | Changes |
| :---- | :---- | :---- |
| 1.0.0-rc.1 | 2026-10-26 | Canonical English Markdown; changes from internal ver.2: title block, Part A / Part B headings, references and history added; role model applied (EPPO accountable for G7, Privacy Operations Lead responsible, DPO consulted with read access; DPO no longer approves the dashboard; Executive Management adopts Sections 5 and 6.6; Supervisory Board and the calqued committee term removed as approver and as raw-dashboard recipient); metric definition standard added (owner, source, numerator, denominator, zero-case rules Z1–Z3, cut-off rules K1–K3, types S/K/R/D); target, tolerance and zones defined once (green never beyond target); statutory metrics without tolerance bands — every missed statutory deadline listed and escalated even when the aggregate is green; "30-day statutory deadline" replaced by one month under Art. 12(3) with extension; averages replaced by median and P90; Little's-law error corrected ("a week's intake" → about two weeks; mean, not median, time in system); breach-notification timeliness split into on-time share over notifications due (incl. unsent), per-case listing of late or overdue notifications with reasons and legal assessment, and reasons-given share; paused DPIAs kept in the overdue count and shown separately with ageing; zone-to-level contradictions and the Section 5 escalation contradiction resolved; Critical residual risk "with a compensating plan" removed (Critical is not acceptable); "passed DPIA" replaced by gates and DPIA where required; approval-rate and marketing metrics withdrawn or made diagnostic; DPO metrics limited to timeliness, coverage and documentation, never used against the content of advice; "EDPB criteria" attributed to WP29 Opinion 05/2014 (WP216); identifiers given to every metric of every Document 24 process and sub-process (Section 6.10), including G4.1, G4.2, G5.1, C2.1–C2.3, S6.3, S7.1–S7.5, S8.1, prior consultations, track (b), disclosure budget, consent withdrawal, management-body and contractor training, AI literacy, DORA reports and data quality; references to Document 24 cards and to Document 9, Sections 3.2 and 8.5 corrected; regulators' access without prejudice to Art. 58(1)(a); HBDI given its full name; product branding replaced by the illustrative PEP; Part B dates shifted by −12 months, versions 2.0/3.0 of the internal draft merged, re-baseline version 3.0 adopted by the Management Board 20 October 2026 (effective 23 October 2026); UK spelling |
| 1.0.0-rc.2 | 2026-10-28 | Author-approved publication direction; named PAMOLA implementation examples with tool-neutral templates; direct integrated-score mapping without automatic per-metric risk-tier overrides; observations, DPO dissent and the authorised business decision recorded separately from legal/release conditions. |
| 1.0.0 | 2026-10-28 | First publication package; substantive method unchanged from the rc.2 freeze; rights holder REALM INVEO confirmed and documentation licence CC BY 4.0 issued. |
