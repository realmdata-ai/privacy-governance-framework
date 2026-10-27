# PGF Risk Model — Mathematical Specification and Validation Pack

## Part 3 — Worked Examples

*Version 0.1.0-preview.1 · research companion · UK English · status: preview for review, 27 October 2026*

Each example states its source inputs, the rule applied (with its `SOURCE_REGISTER.json` identifier), the substitution, intermediate results, the final tiers, the gates and evidence, and the limits of the decision. Machine-readable versions are in `examples/<CASE_ID>/input.json` (facts) and `examples/<CASE_ID>/expected.json` (hand-derived results). All arithmetic was done by hand and re-checked with plain arithmetic only; no model code was used to derive any expected value.

Notation follows Part 2: $L_1 \dots L_4$ likelihood factors, $\Lambda$ the likelihood index, $S$ the severity index, $\ell(\cdot)$ the likelihood band, $\sigma(\cdot)$ the severity band, $M(\text{severity}, \text{likelihood})$ the PGF-08 matrix. "Inherent" means $L_3$ set to 3 for a threat-based scenario, and the PET Assessment Module "as proposed" for a PET-module scenario (PGF-22 Part A glossary, line 86; clarification recorded as errata item E-10).

| Case | Content | Status |
| :---- | :---- | :---- |
| RM-EX-01 | Simple internal processing (artificial), Low | complete |
| RM-EX-02 | PSI anti-fraud matching, DPIA-PSI-01 as at 26 October 2026, High, G-36 met, decision pending | complete |
| RM-EX-03A–E, 03D-NEG-UNIT | Aggregate and synthetic releases — PET module PASS / FAIL / INCOMPLETE; privacy-unit mismatch | machine-readable cases complete; narrative *(pending in this preview)* |
| RM-EX-04 | High harm blocked by G-L | machine-readable case complete; narrative *(pending in this preview)* |
| RM-EX-05A, 05B | Federated learning: declared inputs vs offence-related extension (S2 inherent likelihood per the override clause, E-01; v1 example value as `v1_reported`) | machine-readable cases complete; narrative *(pending in this preview)* |
| RM-EX-06A–C | DP lifetime ledger: repeated releases, failed observable run, no calendar reset, re-labelled population | machine-readable cases complete; narrative *(pending in this preview)* |
| RM-EX-07-HIST, 07-CURRENT | Historical vs current decision status (PSI, 25 March 2026 superseded) | machine-readable cases complete; narrative *(pending in this preview)* |
| RM-GRID | 16 matrix cells; severity, likelihood, override, PET-outcome and track (b) boundaries | complete (`examples/RM-GRID/`) |

---

## RM-EX-01 — Simple internal processing (artificial)

### 1. Source inputs

All inputs are artificial (`"doc": "ARTIFICIAL"`). The case is the one walked through in Part 1, §4.

| Input | Value | Status |
| :---- | :---- | :---- |
| Processing | Customer-support ticket log; structured fields only (name, e-mail, order number, product, issue category, resolution status) | observation |
| People | ~2,500 customers a year | observation |
| Archetype | 4 — identified processing as permanent state | classification |
| Weights | $(w_B, w_C, w_D, w_E, w_G) = (1,1,1,1,1)$ | configuration (default) |
| G-L | PASS — contract-related handling, Art. 13 notice, no Art. 9/10 data, no Art. 22 decision, no transfer | artificial record |
| G-DPIA | not required — no statutory trigger, no WP248 criterion | artificial triage record |
| G-TIA | not engaged | observation |
| Scenarios | S1 loss of confidentiality (+ financial loss); S2 loss of control | scenario definition |

Likelihood inputs (scores on the PGF-18 §3.2 anchors):

| Factor | S1 | Evidence | S2 | Evidence |
| :---- | :----: | :---- | :----: | :---- |
| $L_1$ exposure | 2 | 12 named agents, daily (routine) | 1 | occasional extracts, named roles |
| $L_2$ threat source | 1 | vetted staff, no capable attacker (assumption) | 1 | unintended drift |
| $L_3$ control gap (residual) | 0 | access control, export disabled, log review — tested | 1 | extract approval — partly tested |
| $L_4$ history | 1 | sector events only | 0 | none known |

Severity inputs (identical for S1 and S2): data class Confidential, current; special categories absent; vulnerability none; 2,500 subjects a year; single source; not a pilot; within the organisation; no automated decision; direct collection with clear notice; no floor condition.

Track (b): regime none (0), financial/operational 0, reputational 1, sandbox none (0).

### 2. Likelihood

Rule (SR-18-A-LIK-INDEX, SR-18-A-LIK-BANDS): $\Lambda = L_1+L_2+L_3+L_4$; 0–3 Low, 4–6 Medium, 7–8 High, 9–11 Near-certain. Override (SR-18-A-LIK-OVERRIDE): if $L_3=3$ and $L_2\ge 2$, at least High.

| | S1 residual | S1 inherent | S2 residual | S2 inherent |
| :---- | :---- | :---- | :---- | :---- |
| Substitution | 2+1+0+1 | 2+1+3+1 | 1+1+1+0 | 1+1+3+0 |
| $\Lambda$ | 4 | 7 | 3 | 5 |
| Band | Medium | High | Low | Medium |
| Override | not engaged ($L_3=0$) | not engaged ($L_2=1$) | not engaged ($L_3=1$) | not engaged ($L_2=1$) |
| Level | **Medium** | **High** | **Low** | **Medium** |

### 3. Severity

Rule (SR-18-A-SEV-INDEX): $S = \max(0,\ w_B B + w_C C + w_D D + w_E E + w_G G)$, with B…G the sums of subfactor scores (SR-18-A-FACTOR-B … -G).

| Factor | Subfactor | Raw value | Score |
| :---- | :---- | :---- | :----: |
| B | data class | Confidential | 2 |
| B | age modifier | current | 0 |
| B | special categories | absent | 0 |
| B | vulnerability | none | 0 |
| C | subjects | 2,500 ∈ [100, 9,999] | 1 |
| C | aggregation | single source | 0 |
| D | reach | within organisation | 0 |
| E | ADM | no | 0 |
| G | provenance | direct, clear notice | 0 |

$B = 2,\ C = 1,\ D = E = G = 0$; $S = 1\cdot2 + 1\cdot1 + 0 + 0 + 0 = 3$. Band (SR-18-A-SEV-BANDS): $3 < 3.5$ → **Minor**. Floors (SR-18-A-SEV-FLOORS): neither condition holds → Minor. Same for S2.

### 4. Scenario tiers and track (a)

Matrix (SR-08-B-MATRIX):

| Scenario | Residual | Inherent |
| :---- | :---- | :---- |
| S1 | $M(\text{Minor}, \text{Medium})$ = **Low** | $M(\text{Minor}, \text{High})$ = Low |
| S2 | $M(\text{Minor}, \text{Low})$ = **Low** | $M(\text{Minor}, \text{Medium})$ = Low |

Track (a) (SR-08-A-TIER-DEF): residual $\max(\text{Low}, \text{Low})$ = **Low**; inherent **Low**. Target: equal to residual.

### 5. Track (b)

$\max(0,\ 0+0+1+0) = 1$ → 0–1 → **Minor** (SR-18-A-FACTOR-F). Reported separately; it does not enter the matrix.

### 6. Gates and decision

| Field | Value |
| :---- | :---- |
| G-L | PASS |
| G-DPIA | DPIA not required |
| PET module | NOT_APPLICABLE |
| G-36 | not evaluated (no DPIA) → required step: none |
| Residual tier (track (a)) | Low |
| Decision authority | Processing Owner (SR-08-B-AUTH) |
| DPO advice | not mandatory (no DPIA; no trigger in SR-08-B-DPOTRIG) |
| Processing status | in operation |
| May proceed | yes, once the Processing Owner records the acceptance |

### 7. Limits

* **Minor is a reading of the ordinal scale, not an estimate of the financial harm.** S1 includes financial loss through convincing phishing. The PGF-18 severity index has no input for the size of a loss: it scores the data class, special categories, vulnerability, scale, aggregation, reach, automated decision and provenance. The index of 3 therefore says "Confidential contact data of a few thousand people, kept in-house", not "a phishing loss would be small". The v1 arithmetic is correct; the gap is a property of the scale and is recorded as a limitation.
* **What makes the example bounded.** No free-text field; no payment-card, bank-account or identity-document data in the log; bulk export technically disabled and tested; access limited to 12 named agents; no processor, partner or publication; no decision about customers; current data from one system. Each of these is an input assumption, and the result holds only while all of them hold.
* **Consequence check an adopter should add.** For each scenario, document the worst credible outcome for one affected person and compare it with the PGF-08 severity descriptions (PGF-08 Part A lists "financial loss" as an example of Significant harm). Where the index band is lower than that description, either record the reasons the outcome is bounded (here: no payment data, so phishing must still trick the customer into a separate payment; the organisation's own fraud-reporting channel) or adopt a project-specific rule under PGF-18 Section 4.4, Step 6, which may only make the result stricter. Such a rule is an adopter's configuration, not part of v1, and it would change this example only if adopted.
* The likelihood scores rest on stated evidence and one documented assumption ($L_2$). If a capable attacker is identified ($L_2 \ge 2$) and the controls lapse ($L_3 = 3$), the override rule makes S1 at least High — but the tier stays Low, because the Minor row of the matrix is Low at every likelihood.
* The result is obsolete if free-text fields are introduced (special-category content could appear: Factor B +2 and possibly a severity floor, plus a G-L question), if bulk export is re-enabled, or if the log is shared with a processor (Factor D +1).
* Low is a statement about the PGF ordinal scales, not a probability of harm.

---

## RM-EX-02 — PSI anti-fraud matching (PGF-19 DPIA-PSI-01, as at 26 October 2026)

### 1. Source inputs

Source: PGF-19 Part B, *Summaries: DPIA-PSI-01 and DPIA-FL-01* (≈ lines 545–551); PGF-22 Part B, *Fully Expanded Record — PRR-PSI-01* (≈ lines 341–363). Fictional organisation: PanEuropean Bank AG.

**Processing.** The bank learns which of its customers appear on a partner bank's list of identities linked to confirmed fraud, through a private set intersection (PSI) protocol in which only the bank receives the result. Fraud analysts review every match before any action. Processing Owner: Head of Fraud Prevention. Calculation: PGF-18 Project 4 (archetype 4), default weights.

**Gates as recorded.**

| Gate | Recorded outcome | Source |
| :---- | :---- | :---- |
| G-L | PASS — Art. 6(1)(f); Art. 10 authorisation by national law with safeguards; banking confidentiality assessed; Art. 14 information | PGF-19 ≈ l. 549 |
| G-DPIA | DPIA required — four WP248 criteria | PGF-19 ≈ l. 548 |
| G-TIA | PASS for the one-sided design (20 March 2026); the former mutual-output design failed | PGF-22 ≈ l. 360 |
| G-36 | **MET** — Legal & Compliance (General Counsel), 26 October 2026, with Group DPO advice, with reasons | PGF-19 ≈ l. 551 |

**Scenario inputs.**

| Input | S1 — wrongful match → adverse action | S2 — disclosure of customer relationships |
| :---- | :---- | :---- |
| Factor A | adverse decision, financial loss, exclusion | loss of confidentiality |
| $L_1, L_2, L_3, L_4$ (residual) | 2, 2, 1, 2 | 2, 3, 1, 0 |
| $L_3$ evidence | analyst review before action; partner list quality by contract, partly tested | blinded messages; key in the EEA; one-sided output; padded input; protocol review (illustrative) |
| $L_4$ evidence | transliteration near misses in the pilot | — |
| Data class | Restricted (offence-related list) | Confidential (customer identifiers) |
| Special / criminal-offence data | present — Art. 10 | absent (identifiers carry no offence information) |
| Subjects | 100–9,999 matches a year | ≥ 1,000,000 identifiers input |
| Aggregation | two or more sources | 0 (implied by stated sum) |
| Reach | 0 (implied) | shared with a recipient |
| ADM | 0 (analyst review; implied) | no |
| Provenance | third-party source outside typical expectations | 0 (implied) |

PGF-19 states the S1 severity as "Restricted 3 + criminal-offence data 2 + scale 1 + aggregation 1 + provenance 1 = 8" and S2 as "Confidential 2 + scale 3 + reach 1 = 6"; subfactors not listed are encoded as score 0 with the derivation "implied by the stated sum" (ambiguity A-05), never as silent defaults.

**Track (b):** Moderate (PGF-22 ≈ l. 353; subfactor scores not stated).

### 2. Likelihood (threat-based, PGF-18 Part A §3.2)

Rules: $\Lambda = L_1+L_2+L_3+L_4$ with $L_1,L_2,L_3 \in \{0,\dots,3\}$, $L_4 \in \{0,1,2\}$ (SR-18-A-LIK-FACTORS, SR-18-A-LIK-INDEX); bands 0–3 Low, 4–6 Medium, 7–8 High, 9–11 Near-certain (SR-18-A-LIK-BANDS); override: if $L_3 = 3$ and $L_2 \ge 2$ the level is at least High (SR-18-A-LIK-OVERRIDE); inherent value: $L_3$ set to 3, other factors unchanged (SR-18-A-LIK-INHERENT).

**S1 — residual.**

| Step | Working | Result |
| :---- | :---- | :---- |
| Inputs | $L_1 = 2$, $L_2 = 2$ (known error mode: name transliteration), $L_3 = 1$ (analyst review before action; partner list quality required by contract, partly tested), $L_4 = 2$ (near misses in the bank's own pilot) | all in domain |
| Sum | $2 + 2 + 1 + 2$ | $\Lambda = 7$ |
| Band | $7 \in [7, 8]$ | High |
| Override | $L_3 = 1 \ne 3$ | not engaged |
| Level | | **High** |

**S1 — inherent.** $2 + 2 + 3 + 2 = 9 \in [9, 11]$ → Near-certain. Override: $L_3 = 3$, $L_2 = 2 \ge 2$ → at least High; Near-certain already satisfies it → **Near-certain**.

**S2 — residual.** $2 + 3 + 1 + 0 = 6 \in [4, 6]$ → Medium. Override: $L_3 = 1$ → not engaged → **Medium**.

**S2 — inherent.** $2 + 3 + 3 + 0 = 8 \in [7, 8]$ → High. Override: $L_3 = 3$, $L_2 = 3$ → at least High; no change → **High**.

### 3. Severity (PGF-18 Part A §3.4 and §4.3)

Rule: $S = \max(0,\ w_B B + w_C C + w_D D + w_E E + w_G G)$ with default weights $w = (1,1,1,1,1)$ (SR-18-A-SEV-INDEX, SR-18-A-PASSPORT); bands $S<3.5$ Minor, $3.5 \le S < 6.5$ Moderate, $6.5 \le S < 8.5$ Significant, $S \ge 8.5$ Catastrophic (SR-18-A-SEV-BANDS); then floors (SR-18-A-SEV-FLOORS).

| Factor | Subfactor | S1 input → score | S2 input → score | Rule |
| :---- | :---- | :---- | :---- | :---- |
| B | data class | Restricted → 3 | Confidential → 2 | SR-18-A-FACTOR-B |
| B | age modifier | current → 0 | current → 0 | SR-18-A-FACTOR-B; never applied to Art. 9/10 data |
| B | special / criminal-offence data | present, Art. 10 → +2 | absent → 0 | SR-18-B-FACTOR-B-SPECIAL |
| B | vulnerability | not listed → 0 (implied by stated sum) | not listed → 0 (implied) | SR-18-A-FACTOR-B |
| | **B** | 3 + 0 + 2 + 0 = **5** | 2 + 0 + 0 + 0 = **2** | |
| C | subjects | 100–9,999 matches a year → 1 | ≥ 1,000,000 identifiers → 3 | SR-18-A-FACTOR-C |
| C | source aggregation | two or more sources → +1 | not listed → 0 (implied) | SR-18-A-FACTOR-C |
| C | pilot | not a pilot → 0 (no separate discount) | not a pilot → 0 | SR-18-A-FACTOR-C |
| | **C** | 1 + 1 = **2** | 3 + 0 = **3** | |
| D | reach | not listed → 0 (implied; the adverse action is internal) | shared with a recipient → +1 | SR-18-A-FACTOR-D |
| E | automated decision | not listed → 0 (analyst review before any action) | no → 0 | SR-18-A-FACTOR-E |
| G | provenance | third-party source outside typical expectations → +1 | not listed → 0 (implied) | SR-18-A-FACTOR-G |

Substitution:

* S1: $S = 1\cdot5 + 1\cdot2 + 1\cdot0 + 1\cdot0 + 1\cdot1 = 8$; $\max(0, 8) = 8$; $6.5 \le 8 < 8.5$ → **Significant**.
* S2: $S = 1\cdot2 + 1\cdot3 + 1\cdot1 + 1\cdot0 + 1\cdot0 = 6$; $3.5 \le 6 < 6.5$ → **Moderate**.

Floors: S1 — floor (i) concerns "special-category data"; PGF-10 states that criminal-offence data are not a special category, so on the literal reading the floor is not engaged; on the alternative reading it would require at least Significant. The band is Significant either way (A-02). Floor (ii) (physical harm) is not engaged. S2 — no floor condition.

Check against v1: PGF-19 states S1 = "Restricted 3 + criminal-offence data 2 + scale 1 + aggregation 1 + provenance 1 = 8 → Significant" and S2 = "Confidential 2 + scale 3 + reach 1 = 6 → Moderate". Both are reproduced. Without the Art. 10 modifier S1 would be $8 - 2 = 6$ → Moderate, which is the superseded March 2026 figure (RM-EX-07).

### 4. Scenario tiers, track (a), target and track (b)

Matrix lookup $M(\text{severity row}, \text{likelihood column})$ (SR-08-B-MATRIX):

| Scenario | Residual cell | Residual tier | Inherent cell | Inherent tier |
| :---- | :---- | :---- | :---- | :---- |
| S1 | (Significant, High) | **High** | (Significant, Near-certain) | High |
| S2 | (Moderate, Medium) | **Low** | (Moderate, High) | Medium |

Track (a) (SR-08-A-TIER-DEF; SR-18-A-FINAL, Step 5): residual $\max(\text{High}, \text{Low})$ = **High**; inherent $\max(\text{High}, \text{Medium})$ = **High**. Scenarios are not averaged; S1 determines the tier.

Target (PGF-22, PRR-PSI-01): with tested transliteration rules and partner list-quality controls, S1 $L_3$: 1 → 0; $\Lambda = 2 + 2 + 0 + 2 = 6$ → Medium; $M(\text{Significant}, \text{Medium})$ = **Medium**. Low cannot be reached while S1 is Significant: every cell of the Significant row is at least Medium (SR-08-A-PRINC-SEVLED).

Track (b): **Moderate**, as recorded in PGF-22; the subfactor scores are not stated in v1, so no index is computed. It is reported to ERM and does not enter the matrix or change track (a) (SR-08-A-TRACKB).

### 5. Gates, evidence and decision — step by step

| Order | Step | Input / rule | Outcome |
| :---- | :---- | :---- | :---- |
| 1 | G-L (SR-18-A-GATES, order 1) | recorded PASS: Art. 6(1)(f); Art. 10 authorisation by national law with safeguards; Art. 14 information; transfer tool valid | **PASS** — the calculation may be used for a decision |
| 1a | G-TIA (Art. 46) | one-sided design passed 20 March 2026; pausing the sessions is not a G-TIA hold | **PASS** |
| 2 | G-DPIA (order 2) | four WP248 criteria → presumption | **DPIA required**; DPO advice required on the DPIA |
| 3 | Calculation (order 3) | §§2–4 above | residual track (a) **High**; inherent High; track (b) Moderate (separate) |
| 3a | PET module | v1 classifies DPIA-PSI-01 under Project 4 (archetype 4) | **NOT_APPLICABLE**; no diagnostic indicator (A-04) |
| 4 | G-36 (order 4; SR-19-B-STEP-4.7) | recorded legal conclusion: **MET** (Legal & Compliance, General Counsel, 26 October 2026, with Group DPO advice, reasons recorded). The High tier is a strong indicator and is consistent with it, but the conclusion is the recorded input, not derived from the tier | required step: **consult the supervisory authority before any further session**; submission not yet made |
| 5 | Acceptance (order 5; SR-08-B-AUTH) | residual High → single decider **Chief Risk Officer**, within 5 business days after the consultation step is complete; DPO advice recorded; Supervisory Board Risk Committee informed | **pending** |
| — | DPO-advice triggers (SR-08-B-DPOTRIG) | DPIA exists; Art. 10 data | advice mandatory — given 26 October 2026, followed |
| — | History | Medium accepted 25 March 2026 by the Head of Fraud Prevention under Document 8 v1.0 | **superseded**; confers no current authority (RM-EX-07) |

Resulting fields (kept separate):

| Field | Value |
| :---- | :---- |
| Gate outcomes | G-L PASS; G-TIA PASS; G-DPIA: DPIA required; PET module NOT_APPLICABLE; G-36 MET |
| Diagnostic indicator | none |
| Likelihood levels (residual) | S1 High; S2 Medium |
| Residual-risk tier (track (a)) | High |
| Processing status | Open — decision pending (prior consultation); sessions paused since 26 October 2026 |
| Decision on continuing | **may not proceed** until the consultation step is complete and the CRO has decided |

Had Legal recorded "test not met" with reasons, the required G-36 step would be "none" and the CRO would decide on the High tier directly; the tier alone does not settle G-36 in either direction.

### 6. Limits

* The likelihood scores and the protocol assumptions are illustrative v1 inputs; the companion reproduces them, it does not validate them. S2's Low residual tier rests on the one-sided design leaking nothing result-dependent to the partner — a security assumption recorded in TIA-PSI-01, not measured here.
* "May proceed = no" is a governance status: the consultation step and the CRO decision are outstanding. It is not a statement on lawfulness; G-L remains a separate, recorded PASS.
* Whether PSI belongs to archetype 3 (joint computation, PET module) rather than archetype 4 is an open classification point (A-04). Under v1 as written, the result is computed under Project 4.
