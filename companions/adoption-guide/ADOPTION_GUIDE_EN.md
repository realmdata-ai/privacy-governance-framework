# PGF Adoption Guide

Preview 0.1.0-preview.1 · English (UK) · 27 October 2026 · Review copy

## 1. What this guide helps you do

An organisation usually begins with a practical question: may this team use these data for this purpose, and what must be in place before it starts? A collection of policies is useful only when people can answer that question, produce the evidence and keep the decision current.

The Privacy Governance Framework (PGF) provides policies, methods, role definitions, registers and examples. This guide helps an adoption lead connect those components to the organisation's actual processing. It explains a proportionate route through the framework and provides a completed teaching case. It does not require every organisation to create a new privacy department or adopt all 32 content documents before any processing.

Three labels apply throughout:

- **Applicable legal duty:** a requirement of the law that applies to the organisation and processing. A rollout plan cannot postpone it.
- **Adopted internal control:** an organisational rule selected and approved for that context. It may be stricter than law.
- **Illustrative setting:** a number, role arrangement or scenario used to explain the method. It needs justification before use elsewhere.

The worked case reconstructs the accepted PGF example of a synthetic dataset used for credit-model calibration. It preserves its figures and decision history. It does not authorise a new data release, establish that a real product passed a test, or provide evidence of a real organisation's legal compliance.

## 2. Readers and the first decision

The adoption lead coordinates the programme. A **Processing Owner** is the business role accountable for a particular processing activity and its treatment plan. An **executive programme owner** coordinates the organisation's privacy programme; that function can be combined with an existing suitable role. The controller remains ultimately accountable. An EU statutory **DPO**, where required, advises and monitors independently and performs its statutory tasks; it does not approve business risk or replace the controller's decision.

Start by naming the processing activity, purpose, people affected, intended outputs, systems, recipients and responsible business role. Then distinguish four different questions:

1. Is the processing lawful, and are its legal obligations understood? This is the legal gate, G-L.
2. Is a DPIA required, and what assessment must happen before processing? This is the DPIA triage, G-DPIA.
3. If a DPIA is required, does the statutory test for prior consultation apply? G-36 is a reasoned legal conclusion, evaluated independently of the internal risk label.
4. After those steps and any other applicable gates, who may decide whether to proceed, with what conditions and expiry?

A low internal score does not settle the first three questions. An internally accepted High score does not substitute for a required prior consultation. An elapsed consultation period does not by itself authorise processing.

## 3. Choose a route by scope

| Route | Typical starting situation | Initial adoption focus | What makes the route more demanding |
|---|---|---|---|
| A — bounded activity | A small organisation has a limited number of understood activities, few recipients and no proposed public data release | An applicability record, named owners, processing inventory, notices, rights and breach handling, retention and vendor controls | Sensitive data, monitoring, new purposes, automation, transfers or a requirement to designate a DPO |
| B — established programme | Several business units already have policies and registers, but responsibilities and decisions are inconsistent | Reconcile existing records with the PGF role model, gates, risk method, conditions and review cycle | Inconsistent country requirements, unowned risks, expired decisions, incomplete evidence |
| C — engineering or regulated change | A new PET output, model, collaboration or transfer is proposed | Add the relevant methodology, project passport, measured evidence, transfer assessment and decision record before release | Additional recipients or outputs, repeated releases, unresolved mandatory tests, residual high risk or regulator conditions |

Organisation size alone does not choose the route. A small organisation with sensitive large-scale processing may need a deeper assessment than a large organisation's bounded administrative activity. A new processing proposal can use Route C while the wider programme follows Route B.

## 4. An adoption sequence with exit criteria

| Step | Work and PGF components | Required output | Exit criterion |
|---|---|---|---|
| 1. Establish scope and authority | Overview; 02 Charter; 04 organisation; 05 RACI; 06 roles; 25 owner register | Scope statement, named role holders and delegation/escalation record | Each processing activity and decision has an accountable role; statutory DPO independence is assessed where relevant |
| 2. Establish applicability and facts | 07 applicability; 10 classification; 21 RoPA; 23 inventory | Jurisdiction/purpose map; activity records; systems, data states, recipients and access locations | Processing is described sufficiently to assess lawfulness, obligations and change; unknown facts have owners and restrictions |
| 3. Operate duties from the start | 01 notices; 11 retention; 13 consent where used; 14 breaches; 15 rights; 16 design; 17 suppliers; 30 training | Working procedures, contact routes, logs, instructions and records | A person can exercise a right; an incident or withdrawal is acted on; retention is executed; new processing has design controls |
| 4. Assess a proposed activity or change | 08 appetite; 18 method if relied on; 19 DPIA; 12/20 transfers; 24 process path | Passport, G-L/triage records, scenario assessment and evidence; G-36 conclusion for each DPIA | Mandatory evidence exists and applicable gates are resolved; a transfer has its own valid mechanism and assessment |
| 5. Record the decision and boundaries | 08 authority; 22 risks; 09 evidence integrity/TIP; 25 roles | One effective decider, dated decision, conditions, expiry and evidence links | The decision covers the actual version, purpose, inputs, outputs and recipients; it does not override a failed legal gate |
| 6. Keep it current | 27 monitoring; 28 metrics; 29 review; 31 reporting; 26 staffing if useful | Monitoring plan, issue log, reassessment triggers and management reporting | An expired or changed decision cannot silently remain current; remediation is owned and tracked |

The sequence is a way to organise adoption work. It is not a permission to run unlawful processing until a later stage. Retention, valid consent where needed, withdrawal, rights deadlines and data protection by design apply when their legal conditions arise. Document 18 must be defined before a decision relies on its calculation.

## 5. A minimum set of evidence

For one activity, begin with a coherent set of records rather than parallel spreadsheets that disagree. Use stable identifiers and an index showing which record supports which claim. The [worked case](COMPLETE_WORKED_CASE_EN.md) and [filled evidence bundle](evidence/00_INDEX.md) demonstrate the following:

- A processing record describes purpose, lawful-basis references, data subjects/categories, recipients, transfers, retention and ownership. The data inventory adds actual datasets, systems, states, access and lineage.
- The project passport defines the assessed version, privacy unit, adversary and observable outputs. It fixes the relevant tests and thresholds before results are used.
- The legal and triage records state the conclusions, reasons, responsible roles and source references. A template cannot supply a real organisation's legal analysis.
- Measured or assumed evidence is labelled accurately. Missing mandatory evidence is visible and prevents a positive module result; an expert view is not a substitute for an absent required test.
- The decision identifies the authorised decider and conditions. The risk register links to it; it does not create approval by listing a tier.
- The monitoring record states what changes or expires, who notices and what happens before further processing.

A sealed evidence pack is an integrity mechanism, not an indefinite-retention exemption. Minimise personal information in the pack; apply appropriate access and deletion rules to any separately retained personal component.

## 6. Tailor roles without removing accountability

A small organisation may assign programme coordination to an existing suitable manager and use external advice. It need not reproduce the worked bank's CPO, board committees or staffing model. It still needs clear Processing Owners, lawful decision authority, sufficient resources and conflict checks. Where a statutory DPO is required, combining it with another position must preserve independence and avoid determining purposes and means in conflict with its monitoring task.

A regulated organisation may use its existing executive, risk and assurance arrangements. Align rather than duplicate them. The bank's division between Management Board and Supervisory Board is a jurisdiction-specific example, and its three reserved consent matters are not a universal PGF organisational requirement. Independent assurance and the DPO's statutory monitoring have distinct roles; neither transfers the controller's accountability.

## 7. Useful management decisions

| Situation | Appropriate decision record | Evidence needed before closing it |
|---|---|---|
| An owner is missing | Name the accountable business role and record the mandate; restrict the proposed change until required decisions are possible | Scope, competence/conflict checks and written delegation |
| A mandatory PET test is missing | Keep the outcome INCOMPLETE and assign a validation action | A valid result for the declared threat/output scope, not a retrospective opinion |
| A transfer mechanism is uncertain | Restrict or suspend the affected flow while the lawful route is resolved | Applicability, current mechanism, recipient/coverage check and assessment appropriate to that route |
| A DPIA indicates a need for prior consultation | Complete the statutory consultation step before the processing starts or resumes | Reasoned G-36 conclusion, submission/advice/order records as applicable and a valid subsequent decision |
| A conditional acceptance expires or inputs change | Reassess before further use that relies on the expired or out-of-scope decision | Updated facts, gates/evidence, risk assessment and current authorised decision |

The escalation thresholds, response times and risk-appetite values used by an adopter must be adopted and justified for its context. They do not change statutory deadlines or make a failed legal requirement acceptable.

## 8. A first review of adoption

Review a sample of actual activities, including one that stopped or changed. Follow each record from purpose to systems, from evidence to gate, and from gate to decision. Check whether current operations stay inside the decision's scope. Ask whether the organisation can find and act on an expired decision, an erasure request, a withdrawal, an incident and a supplier change.

Useful initial indicators include the share of in-scope activities with a confirmed owner and current triage; open legal-gate questions; overdue statutory cases; conditional acceptances past expiry; transfers with current required assessment; and missing mandatory evidence. Define denominators, cut-offs and zero-case behaviour before using a percentage. A green aggregate must not conceal an individual missed statutory deadline.

## 9. How to use the companion

Read the [complete worked case](COMPLETE_WORKED_CASE_EN.md), inspect the filled records in [the evidence index](evidence/00_INDEX.md), and use the [adoption checklist](ADOPTION_CHECKLIST.md) against your own circumstances. The [sources and limitations](SOURCES_AND_LIMITATIONS.md) explain the baseline, illustrative evidence and jurisdictional boundaries. This companion does not add requirements to the accepted PGF v1 or change its source files.
