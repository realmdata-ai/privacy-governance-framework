# PGF Risk Model — Mathematical Specification and Validation Pack

## Part 1 — Introduction

*Version 0.1.0-preview.1 · research companion · UK English · status: preview for review, 27 October 2026*

> **Status.** This companion is a research and validation aid. It is **not** part of PGF 1.0.0, it adds no legal obligation, and nothing in it is a condition for using the accepted PGF v1. It describes and tests the risk model of PGF v1 exactly as fixed in the content baseline (commit `02ff78357f3b24f607651f0bf9f01c6c279b587b`, documents PGF-08, PGF-18, PGF-19, PGF-20, PGF-22 and PGF-28). Where v1 appears ambiguous or inconsistent, the point is recorded for a future decision; it is not silently corrected here. All organisations, people and figures in the examples are fictional or artificial. Nothing here is legal advice.

---

## 1. Why this companion exists

Privacy is often claimed in a word: "the data are anonymised", "we use federated learning", "the release is differentially private". None of those words, on its own, tells a reader whether a particular person could be harmed by a particular use of data, or who decided that the remaining risk was acceptable.

The Privacy Governance Framework (PGF) takes a different position. A privacy claim is supported only by a **reproducible assessment** of the risk that a **specific processing activity** creates for **people**, with stated thresholds, recorded evidence and a named, accountable decision. The calculation rules for that assessment are in PGF-18 (Privacy Risk Assessment Methodology); the scales, the matrix that combines them and the acceptance authority are in PGF-08 (Privacy Risk Appetite Statement); the procedure in which they are applied is in PGF-19 (DPIA Methodology).

Those documents are written as policy templates with a worked example. This companion restates the same model in three separated layers:

| Layer | Content | Where |
| :---- | :---- | :---- |
| A | A plain explanation and an end-to-end example, readable without the PGF vocabulary | this document |
| B | An exact formal specification of the PGF v1 model — every symbol, domain, rule and boundary, with a clause-level source map | Part 2 (`02_Mathematical_Specification_EN.md`), `SOURCE_REGISTER.json` |
| C | A critical review of probabilistic extensions (expected loss, noisy-OR, Bayesian evidence, DP-to-probability claims) that are **not** part of PGF v1 | Parts 4–5 (separate) *(pending in this preview)* |

Worked, hand-checked examples (Part 3) and machine-readable cases (`examples/`) let an independent reviewer reproduce every number.

**Intended readers.** A privacy engineer who has to compute the result; a risk analyst who has to place it in an enterprise risk framework; a Data Protection Officer (DPO) who has to advise on it; and an independent reviewer who has to check that the result follows from the rules and the evidence.

---

## 2. A concrete problem

Before any symbol, consider one small, ordinary case. It is entirely artificial and is used again, with full arithmetic, as case **RM-EX-01** in Part 3.

**The data and the people.** An organisation's customer-support team keeps a log of support tickets. For each ticket it records the customer's name, e-mail address, order number, product, an issue category chosen from a fixed list, and the resolution status. There is no free-text field. About 2,500 customers raise a ticket each year. The information was collected directly from the customers, who were told at the point of contact what it is used for.

**The use.** Twelve named support agents use the log, every working day, to answer the tickets. The log stays in the organisation's own ticketing system; nothing is shared with a partner or published.

**What could go wrong for a person (the harm).** Two things are worth assessing:

* *S1 — loss of confidentiality.* Someone with access — or someone using an agent's credentials — copies the log and it is disclosed or misused; a customer then receives convincing phishing messages quoting their real order, and may lose money.
* *S2 — loss of control.* The ticket data drift into another use that the customer was never told about, such as targeting marketing campaigns.

Other kinds of harm are considered and set aside with a reason: no decision about a customer is taken from the log (so no discrimination or automated-decision harm), no identity documents are held, and no special-category information is recorded.

**Who or what is the adversary.** For S1, the realistic threat source is a careless or low-capability insider; there is no evidence of a motivated, organised attacker targeting this log. For S2, there is no adversary in the usual sense: the threat is an unintended drift of purpose.

**What is observed.** The organisation has role-based access control, has disabled bulk export from the ticketing tool, and reviews access logs monthly; these measures have been tested and the test records are kept. Extracts for any other purpose need an approval that has been implemented but only partly tested. In the sector, misuse of similar support data by insiders has been reported; the organisation itself has no recorded incident.

**What has to be decided.** Whether the processing may continue as designed; if so, who may accept the remaining risk; and whether any further legal step is needed.

**What makes the case bounded.** The example is deliberately small, and its assumptions do real work: no free-text field (so no health or other sensitive details can creep in); no payment or identity-document data in the log; bulk export technically disabled; access limited to named staff; no sharing, publication or decision about customers. If any of these fails, the case is no longer the one assessed below. Note also that S1 names a financial loss through phishing: the PGF severity scale does not measure the size of that loss. It scores attributes of the data and the processing (kind of data, scale, reach and so on), so the result below is a reading of the ordinal scale, not an estimate of how much money a customer could lose.

---

## 3. Key ideas

### 3.1 Privacy is not the same as confidentiality or security

Information security protects information assets — their confidentiality, integrity and availability — mainly for the organisation's sake. Privacy risk, in the sense used here, concerns **the rights and freedoms of the people the data are about**. The two overlap (a breach of confidentiality can harm a person), but they are not the same:

* processing can be perfectly secure and still harm people — for example, a well-protected credit model that systematically refuses credit through proxies for protected characteristics;
* a security event can leave people's confidentiality intact — for example, a stolen laptop holding strongly encrypted data whose key was never exposed, where working copies of the data remain available (if no copy remained, the loss of availability could itself harm people);
* privacy harms include outcomes that are not security events at all: being profiled beyond what one was told, being excluded from a service, being wrongly linked to an offence.

PGF-18 therefore assesses **harm scenarios**: a threat source, a problematic data action or event, and the type of harm that would follow for individuals. It asks every assessment to consider seven harm types (unlawful processing or loss of control; discrimination or adverse automated decisions; financial loss; identity fraud; reputational and social harm; physical or psychological harm, chilling effects and exclusion; and loss of confidentiality, integrity or availability). Re-identification is one threat source among others; it is not the definition of privacy risk.

### 3.2 Risk to people versus consequences for the organisation

PGF keeps two tracks that are never netted against each other:

* **Track (a)** — risk to the rights and freedoms of individuals. This is the track on which the processing is decided.
* **Track (b)** — consequences for the organisation: regulatory, financial, reputational, operational. This is reported to enterprise risk management on its own scale.

A large expected fine does not make a harm to people "more acceptable" or "less acceptable", and a negligible business impact does not lower the harm to people. In the support-log case, the organisation's own exposure is small (track (b) Minor); that fact plays no part in the track (a) result.

### 3.3 Inherent, residual and target risk

* **Inherent risk** is the risk as if the organisation's measures were absent or ineffective. It shows how much the outcome depends on those measures.
* **Residual risk** is the risk after the measures that are actually implemented **and evidenced**. Decisions are taken on the residual risk.
* **Target risk** is the level the risk owner plans to reach, with actions and a date.

In the support-log case the inherent likelihood of S1 is High and the residual likelihood is Medium, because the access controls are implemented and tested. Measures that are only planned do not count towards the residual value.

### 3.4 What a control does

In PGF v1, a control acts on **likelihood**, not on severity. Access control makes the misuse of a log less likely; it does not make the harm of a misuse smaller when it happens. Severity changes only where a measure demonstrably limits the consequences themselves, and that must be documented in the scenario. Consent, contract or any other legal basis is checked separately (see §3.8) and never lowers either likelihood or severity.

### 3.5 Evidence and uncertainty

Each number in the assessment must come from somewhere. The companion labels every input with its **status**:

| Status | Meaning | Example |
| :---- | :---- | :---- |
| Observation | A recorded fact | 2,500 customers raised a ticket last year |
| Estimate | A measured quantity with sampling uncertainty | the success rate of a membership-inference attack, with a 95% interval |
| Formal guarantee | A property proved for a mechanism under stated assumptions | a differential-privacy statement (ε, δ) for a stated privacy unit |
| Assumption | A judgement or a declared, unproven premise | "no motivated attacker targets this log" |

The ordinal scores of PGF v1 (for example "exposure = 2") are **structured judgements** on documented evidence. They are not measurements and not probabilities. Where a quantity is estimated, PGF v1 requires the unfavourable end of its confidence interval to be used at a gate; a missing or invalid result never counts as a pass.

### 3.6 Privacy unit and unit of analysis

Two "units" are easily confused, and both matter:

* The **protected unit** (in differential privacy, the **privacy unit**) is the entity whose presence, attributes or linkage a guarantee or a test is about — one record, or all records of one person. Every disclosure claim needs it stated, not only a formal one. An empirical membership-inference, linkage or subgroup test must say what "membership" or "a hit" refers to (a record or a person), how several records of the same person are treated, and how per-record results are aggregated into the reported rate; a test run per record can understate the exposure of a person who contributes many records. The formal differential-privacy statement of PGF-18, Section 3.3.5, is the special case in which the unit is part of a proved guarantee, together with the adjacency relation and a contribution bound per person.
* The **unit of analysis** of the PGF model is the **harm scenario** within a **Risk Calculation Project** for one processing activity. Likelihood and severity are assessed per scenario; the tier of the processing is the **worst** scenario tier. Scenarios are never averaged. The number of people affected enters only as a severity input (scale), not as a multiplier of probabilities. Choosing the scenarios — and the people each scenario concerns — is a substantive modelling decision whether or not any formal guarantee is claimed.

### 3.7 Scores are not probabilities

PGF v1 combines ordinal judgements by adding small integers and reading the sum against fixed bands. This is a reviewable convention, not a probability calculus: a likelihood index of 6 is not "twice as likely" as 3, and a severity index is not an expected loss. Where PGF v1 computes a weighted average of normalised attack metrics (the "disclosure indicator" of the PET Assessment Module), it says explicitly that this is an uncalibrated ordinal summary, not a probability. The bank-specific weights and thresholds in the PGF examples are illustrative policy settings of a fictional organisation, not universal norms.

### 3.8 Gates come before scores

Some questions are not risk questions at all, and no score can answer them:

* **G-L — legal compliance gate.** Is there a lawful basis, a condition for special-category data or an authorisation for criminal-offence data, a compatible purpose, the required transparency, permissible automated decision-making, a valid transfer tool? A failure means stop or redesign. No tier, appetite, metric or DPO opinion can cure it.
* **G-DPIA — DPIA triage.** Is a data protection impact assessment required? This is decided by the legal triggers, independently of any tier.
* **PET Assessment Module gates (G-M1 … G-M5)** — for de-identified, synthetic, aggregate or federated releases only. A failed or incomplete module blocks the release whatever its average score.
* **G-36 — prior consultation.** For every DPIA, the legal question whether high risk would remain without further mitigation. An internal High tier is a strong indicator, but the legal conclusion is recorded separately, with reasons, by the organisation's designated Legal function, after DPO advice. (This is the PGF allocation of the task; it does not add a headcount or a professional-licence requirement.)

The companion keeps these outcomes as separate fields: a **gate outcome** (PASS / FAIL / INCOMPLETE), a **diagnostic indicator**, a **likelihood tier**, a **residual-risk tier**, the **processing status** and the **decision** on whether processing may start or continue. They are never collapsed into one number.

---

## 4. The simple case, end to end

This section walks through the support-log case in words and small sums. Part 2 gives the formal rules; Part 3 repeats the case with every clause reference.

### Step 0 — Gates

* **G-L.** The lawful basis (handling the customer's own request) is recorded, the customers were informed at collection, the purpose is unchanged, there are no special-category or criminal-offence data, no automated decisions and no transfer. G-L: **PASS** (artificial record).
* **G-DPIA.** None of the nine screening criteria of the European DPIA guidelines is met (no sensitive data, no large scale, no profiling, no automated decision). A DPIA is **not required**; the triage is recorded with reasons.
* **PET module.** Not applicable: nothing is de-identified, synthesised, aggregated or released.
* **G-36.** Not evaluated: it is evaluated for every DPIA, and there is no DPIA.

### Step 1 — Scenarios

S1 (loss of confidentiality, with possible financial loss) and S2 (loss of control). Other harm types are set aside with the reasons given in §2.

### Step 2 — Evidence

| Fact | Status | Used for |
| :---- | :---- | :---- |
| 12 named agents use the log daily | observation | exposure |
| No motivated attacker identified; staff vetted | assumption, documented | threat source |
| Access control, export disabled, monthly log review — tested | observation (test record) | control gap, S1 |
| Extract approval workflow — implemented, partly tested | observation | control gap, S2 |
| Insider misuse of similar data reported in the sector; none in-house | observation | event history |
| ~2,500 customers a year | observation | scale |
| Contact data, current, single system, direct collection with clear notice | observation | severity |

### Step 3 — How likely is each scenario?

PGF-18 asks four questions, each answered with 0 to 3 points (the last with 0 to 2), and adds the answers:

| Question | S1 | S2 |
| :---- | :----: | :----: |
| Exposure — how often and how broadly is the data action carried out? | 2 (routine, daily) | 1 (occasional extracts) |
| Threat source — how capable and motivated? | 1 (accidental, low capability) | 1 (unintended drift) |
| Control gap — how weak are the measures in place? | 0 (implemented and tested) | 1 (implemented, partly tested) |
| Event history | 1 (sector events) | 0 (none known) |
| **Sum (residual)** | **4** | **3** |
| Sum without measures (control gap set to 3) | 7 | 5 |

The sum is read against fixed bands: 0–3 Low, 4–6 Medium, 7–8 High, 9–11 Near-certain. So S1 is **Medium** (High without measures) and S2 is **Low** (Medium without measures). A special rule would raise the result to at least High where the controls are absent against a capable or systematic threat source; it is not engaged here, because the threat source scores only 1.

### Step 4 — How severe would the harm be?

Severity is the sum of points for the kind of data (contact data: 2), special categories (none: 0), vulnerable people (none: 0), number of people (100 to 9,999: 1), combination of sources (one system: 0), reach beyond the organisation (none: 0), an automated decision with significant effect (none: 0) and how the data were obtained (directly, with clear notice: 0). For both scenarios the sum is **3**, which falls in the lowest band (below 3.5): **Minor**. No severity floor applies.

"Minor" here is what the attribute-based scale yields for contact data of a few thousand people kept in-house. It is **not** an independent judgement that a phishing loss suffered by a customer would be small: the scale has no input for the amount of money at stake. An adopter who considers that a scenario's consequence may be worse than its index suggests should add a documented consequence check — for example, a review of the worst credible outcome for one person in each scenario against the PGF-08 severity descriptions ("an easily remedied inconvenience" for Minor; "financial loss" is given as an example of Significant), and a project-specific rule that may only make the result stricter (PGF-18, Section 4.4, Step 6). The companion records this as a limitation of the v1 scale; it does not change the v1 result.

### Step 5 — Combine likelihood and severity

The PGF-08 matrix is read with severity as the row and likelihood as the column:

| Severity \ Likelihood | Low | Medium | High | Near-certain |
| :---- | :---- | :---- | :---- | :---- |
| Minor | Low | Low | Low | Low |
| Moderate | Low | Low | Medium | Medium |
| Significant | Medium | Medium | High | High |
| Catastrophic | High | High | Critical | Critical |

S1: Minor × Medium = **Low** (without measures: Minor × High = Low). S2: Minor × Low = **Low** (without measures: Minor × Medium = Low).

### Step 6 — The tier of the processing

The tier of the processing on track (a) is the **highest** scenario tier: max(Low, Low) = **Low**. Track (b) is recorded separately: the organisation's consequences are Minor.

### Step 7 — Decision

Under PGF-08 Section 5, a **Low** residual tier may be accepted by the **Processing Owner** — here the head of customer support — who records the decision in the evidence pack. DPO advice is not mandatory, because there is no DPIA and none of the mandatory-advice triggers (special-category or criminal-offence data, automated decisions, PET-module failure, non-standard weights, an anonymity conclusion) applies. No prior consultation is needed. Processing may continue once the decision is recorded.

### What the result does not say

* It does not say that a breach "will not happen", nor give a probability that it will.
* It does not prove that the processing is lawful; that was a separate gate.
* It depends on stated evidence. If bulk export is re-enabled, or free-text fields are added in which customers can describe health problems, the assessment is obsolete and must be re-run.
* It reflects a policy choice: in the PGF-08 matrix, a Minor harm is Low at every likelihood. An organisation may adopt a stricter matrix; it may not relax the severity-led floors without independent evidence.

---

## 5. A harder case in one paragraph

Case **RM-EX-02** applies the same steps to a fictional bank's anti-fraud matching with a partner bank abroad, using a private set intersection protocol (PGF-19, DPIA-PSI-01, as re-assessed on 26 October 2026). A match links a customer to a list of identities associated with confirmed fraud — criminal-offence data — so the severity of the wrongful-match scenario is 8 (Significant), and its residual likelihood is 7 (High): the processing is **High**. The legal conclusion on prior consultation was recorded separately as "test met". The result is not a launch: the sessions are paused, the supervisory authority is to be consulted before any further session, and only then may the designated Chief Risk Officer decide. An earlier acceptance at Medium, calculated without the criminal-offence modifier, is kept as superseded history (case RM-EX-07 *(pending in this preview)*).

---

## 6. How to read the rest of the pack

| Part | Content |
| :---- | :---- |
| Part 2 — Mathematical Specification | Every symbol with domain, unit, direction and status; the scales and bands; the matrix; tracks; aggregation; gate order; PET module; DP lifetime ledger; acceptance authority; clause map |
| Part 3 — Worked Examples | RM-EX-01 and RM-EX-02 complete; RM-EX-03 to RM-EX-07 narratives *(pending in this preview)*; with sources, substitutions, intermediate results, tiers, gates, evidence and limits |
| Parts 4–5 *(pending in this preview)* | Validation and limits; review of research extensions and legacy formulas (separate layer C) |
| `examples/` | Machine-readable inputs and hand-derived expected results (RM-EX-01 to RM-EX-07 and the boundary grid `RM-GRID`); the reference implementation and its one-command runner *(pending in this preview)* |
| `SOURCE_REGISTER.json` | Clause-level map from every rule used here to the PGF v1 document, part, section and file hash |

A passing check in this pack means exactly the property it states: that a result follows from the PGF v1 rules and the stated inputs. It does not mean that a processing activity is lawful, that data are anonymous, or that the PGF scales have been empirically validated.
