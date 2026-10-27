---
title: "PGF Risk Model Companion — Review of Earlier Probabilistic Formulas (Research Layer C)"
companion_version: 0.1.0-preview.1
status: preview for review (27 October 2026)
pgf_baseline: "PGF 1.0.0-rc.1, content commit 02ff78357f3b24f607651f0bf9f01c6c279b587b"
---

# Review of Earlier Probabilistic Formulas (Research Layer C)

> **Status.** This is a research appendix. It is **not** part of PGF 1.0.0 and does not change any PGF rule, weight, scale or decision. The accepted PGF model is ordinal: its scores are not probabilities, and its weighted severity index is not an expected loss (docs/02). This appendix examines a separate family of probabilistic formulas from earlier internal working material (July 2026). It records which of them are mathematically sound, under what assumptions, and what they may be used for.

## 1. Why this review exists

Earlier working material proposed probabilistic and Bayesian formulas for privacy risk: expected loss, scenario mixtures, likelihood-ratio updating, chain decomposition, noisy-OR unions, and translations from differential-privacy parameters to "residual risk". Some are standard and correct. Some are correct only under assumptions that the material did not state. A few are not probability statements at all. Carrying them over unexamined would mix two different models and could understate risk.

**Method.** For each claim we record:
- the exact definition;
- the assumptions it needs;
- domain and units;
- a proof or a primary source;
- the inputs it needs to be computed;
- a validation case;
- a counterexample or limit;
- a disposition.

Counterexamples are computed exactly on explicit finite probability spaces, using rational arithmetic, in `research/legacy_math.py`. Their tests (`research/tests/test_legacy_counterexamples.py`, case IDs RX-01…RX-27) take expected values derived by hand, never from the function under test.

Each helper has a documented input domain and rejects inputs outside it — non-finite values, out-of-range probabilities and empty or mismatched inputs — before doing any arithmetic (RX-23…RX-27). The DP helpers use an overflow-free form for large finite ε. The degenerate priors 0 and 1 are handled exactly.

**Dispositions:**
- **adopted** — correct as stated, and usable in the research layer with its stated assumptions;
- **reference** — a correct standard definition, used as a reference only;
- **research** — usable only as a research hypothesis, with explicit assumptions and sensitivity analysis;
- **rejected** — not a valid probability or risk statement as written;
- **unresolved** — a term or claim that cannot be checked as written.

**Sources.** The source material is identified by neutral IDs:
- LG-SRC-01 — formula catalogue;
- LG-SRC-02 — per-technology substitution formulas;
- LG-SRC-03 — presentation slides;
- LG-SRC-04 — formula slides and an accompanying document;
- LG-PROTO-01 — a prior internal prototype's risk aggregation.

The private provenance (paths, versions, hashes) is kept outside this companion.

## 2. Summary

| Group | Sound as stated | Sound only with assumptions | Not sound as written |
|---|---|---|---|
| Expected loss, scenarios | linearity of expectation; chain rule | scenario mixture (needs a partition and a probability distribution over it); mitigation factor products (need independent failure of measures) | summing WP216 criteria as "orthogonal" events (double counting) |
| Unions of events | Boole–Fréchet bounds; inclusion–exclusion | noisy-OR (needs mutual independence) | "dependent chain" with an undefined coefficient; series accumulation mixing loss into a union |
| Bayesian updating | Bayes' rule; odds form | product of likelihood ratios (needs conditional independence) | — |
| Differential privacy | (ε, δ) definition; basic sequential composition; advantage bound in the hypothesis-testing game | parallel composition (needs add/remove adjacency and a data-independent partition) | "R_DP = Adv × L" as a probability of harm |
| Anonymity metrics | k-, l-, t- definitions; uniqueness ratio | 1/k (needs a stated adversary) | — |
| Attack metrics | TPR − FPR at a threshold; Wilson interval | AUC summaries (hide low-FPR exposure) | `max(0, 2·AUC − 1)` (clips inverted attacks) |
| Evidence status | — | — | "unmeasured = 0.5 × confidence" as a worst-case bound; "closed = effective" |

## 3. Claim-by-claim review

Notation follows the source unless stated otherwise:
- E_i — an event;
- L — a loss;
- p — a probability;
- π — a prior over adversary configurations;
- M_c — mitigation coverage;
- ε, δ — DP parameters.

All probabilities lie in [0, 1]. A loss L carries its own unit, and its scale must be stated.

### 3.1 Expected loss and scenario models

| ID | Claim (source) | Exact definition and assumptions | Validation / counterexample | Disposition |
|---|---|---|---|---|
| LC-01 | R = E[L] = Σ_i P(E_i)·L(E_i) (LG-SRC-01 §3) | Exact if the total loss is Σ_i L_i·1{E_i}. Linearity of expectation holds **without independence**. The real risk is **double counting**: when one harm is reachable through several events, the sum counts it more than once. Define losses per harm outcome, not per attack route. | RX-08: dependent events, linearity holds. RX-09: one harm of 10, reachable by singling-out and linkage (the same event); true E = 5, summed = 10 | adopted, with a per-harm loss definition |
| LC-02 | R_norm = Σ P̂_i·L̂_i with P̂, L̂ ∈ [0, 1] (§3) | This is an index, not a normalised expected loss. (R − R_min)/(R_max − R_min) needs stated bounds, and Σ P̂ L̂ can exceed 1. | — | research (index only; no probability meaning) |
| LC-03 | R = Σ_c π(c)·RI(c)·(1 − M_c), with RI = P_success·S (§4) | Valid as an expectation if: {c} is a partition of adversary configurations; Σ π(c) = 1; S(c) is a loss in one unit; and (1 − M_c) is the probability that the controls fail against c. π(c) is usually an expert judgement and needs sensitivity analysis (§17 of the source). | Scenario PSI table (LG-SRC-02 §5): the P_success values 0 or 1 are design assumptions, not measurements | research |
| LC-04 | 1 − M_c = Π_m (1 − η_{m,c}) (§13) | Exact only if the measures fail independently. Common-mode failures (shared keys, one operator) break it. | Same structure as RX-01/RX-02 | research (independence must be argued) |
| LC-05 | P(E) = P(B_1)·Π_s P(B_s ∣ B_1:s−1) (§6 "CD model") | The chain rule. It is exact when each factor is conditioned on all earlier stages. Replacing the conditionals with marginals is wrong under dependence. | RX-07: exposure ⇒ inference; true P(A∩B) = 1/2 = chain; product of marginals = 1/4 | adopted (chain rule); marginal products rejected |
| LC-06 | R_add = Σ w_i·R_i, Σw = 1 (§7) | A weighted index. It needs calibrated weights and commensurable scales. It is "honest" for orthogonal events only in the sense of LC-01, and the singling-out / linkage / inference criteria of WP216 are **not** orthogonal or mutually exclusive. | RX-09 | research (index); "orthogonal triad" claim rejected |

### 3.2 Unions of events

| ID | Claim | Exact definition and assumptions | Validation / counterexample | Disposition |
|---|---|---|---|---|
| LC-07 | P(∪E_i) = 1 − Π(1 − P(E_i)) "independent approximation" / noisy-OR (§7, §13; LG-PROTO-01) | Exact iff the events are mutually independent. Without a dependence model it is **neither conservative nor anti-conservative**: positive dependence makes it overstate, disjoint events make it understate. | RX-01: identical events, truth 1/2, noisy-OR 3/4. **RX-02: disjoint events, truth 1, noisy-OR 3/4 (understates).** RX-03: independent, exact | research (only with argued independence) |
| LC-08 | Bounds when dependence is unknown | Boole–Fréchet: max_i P(E_i) ≤ P(∪E_i) ≤ min(1, Σ P(E_i)). These bounds are sharp given the marginals alone. | RX-04: all three truths lie in [1/2, 1] | adopted (report the interval, not a point) |
| LC-09 | P_dep = 1 − Π(1 − p_i·d_i), d_i a "dependency / amplification coefficient" (§8; LG-SRC-02 §4) | d_i is not defined as any probability quantity. p_i·d_i can exceed 1, and the formula keeps the independence form whatever d_i is. | RX-05: p = 0.6, d = 2 → 1.2 | rejected |
| LC-10 | P_total = 1 − (1 − P_dep)(1 − P_ind) (§8) | Needs independence of the two branches; it inherits LC-09. | — | rejected (with LC-09) |
| LC-11 | R_agg = 1 − Π_q (1 − P_q·L_q) over a query series (LG-SRC-02 §8) | Puts a loss inside a union-of-probabilities formula. The result changes with the loss unit and can exceed 1. Repeated-release risk should instead be handled by composition (DP) or by explicit reconstruction analysis. | RX-06: L on a 1–5 scale → 1.5 | rejected |
| LC-12 | Φ_total = 1 − Π_j (1 − Φ_j) for system failures around a cryptographic process (§14) | Same as LC-07. Layer failures (keys, operators, implementation) are typically dependent. | — | research |

### 3.3 Bayesian updating

| ID | Claim | Exact definition and assumptions | Validation / counterexample | Disposition |
|---|---|---|---|---|
| LC-13 | Bayes' rule; posterior odds = prior odds × LR (§5) | Exact for a single observation, given a stated prior and likelihoods. | — | adopted |
| LC-14 | odds(H ∣ O) = odds(H)·Π_m LR_m, for several tests (§5; LG-SRC-02 §2) | Exact iff the observations are conditionally independent given H and given ¬H. Two tests that measure the same signal (the same attack on the same artefact, or derived metrics) double-count it. Base rates must be stated. | RX-10: duplicated test, exact posterior 3/4, LR product 9/10. RX-11: conditionally independent, exact | research (conditional independence must be argued per test pair) |

### 3.4 Differential privacy

| ID | Claim | Exact definition and assumptions | Validation / counterexample | Disposition |
|---|---|---|---|---|
| LC-15 | (ε, δ)-DP definition; privacy-loss random variable (§9) | Standard (Dwork and Roth 2014). It requires a stated privacy unit and adjacency relation (add/remove vs replace-one), the mechanism and its accountant. | — | reference |
| LC-16 | Posterior odds ≤ e^ε × prior odds (§9) | Holds for pure ε-DP (δ = 0). With δ > 0 it holds only outside an event of probability related to δ; it is not a pointwise guarantee. | RX-14 | adopted for δ = 0; research for δ > 0 |
| LC-17 | Adv_MIA ≲ (e^ε − 1)/(e^ε + 1) + δ (§9; LG-SRC-02 §3) | In the hypothesis-testing game with a balanced prior, any test satisfies TPR ≤ e^ε·FPR + δ and 1 − FPR ≤ e^ε(1 − TPR) + δ. The sharp maximum of TPR − FPR is (e^ε − 1 + 2δ)/(e^ε + 1) (Kairouz, Oh and Viswanath 2015; see also Wasserman and Zhou 2010; Dong, Roth and Su 2022). The legacy bound is valid, but looser when δ > 0. | RX-12: ε = ln 3, δ = 0 → 1/2, attained by randomised response (TPR 3/4, FPR 1/4). RX-13: δ = 0.1 → exact 0.55, legacy 0.60 | adopted, as a bound in the stated game |
| LC-18 | R_DP = Adv_MIA × L (LG-SRC-02 §3) | Advantage is a property of a distinguishing game with a 1/2 prior. It is not the probability that membership is disclosed, or that harm occurs, for a real population and prior. δ is not a general incident probability. | RX-14: prior 1/100 → posterior ≤ 3/102 ≈ 0.029, while Adv = 0.5 | rejected as a probability of harm. The bound itself may inform the PGF PET module only as stated evidence (docs/02) |
| LC-19 | ε_total = Σε_t, δ_total = Σδ_t (§9) | Basic sequential (adaptive) composition — a valid upper bound. Tighter accountants (advanced composition, Rényi/zCDP, PRV) need their own prerequisites. | Used by the reference ledger (PGF Doc 18 §3.3.6) | adopted |
| LC-20 | Parallel composition: ε_total = max_t ε_t for disjoint strata (§9) | Valid when each person can affect only one partition: add/remove adjacency, and a partition rule that does not depend on other records (McSherry 2009). Under replace-one adjacency, a record whose stratum label changes affects two partitions, giving ε_a + ε_b. | RX-15: add/remove → 1.0; replace-one with a label change → 1.5 | adopted, with the adjacency stated |
| LC-21 | "ε ≈ 2–2.5" and similar slide values (LG-SRC-03) | Not reproducible from the available material: no mechanism, privacy unit, accountant or run artefacts. | — | unresolved (archival claim, not a measurement) |

### 3.5 Anonymity and attack metrics

| ID | Claim | Exact definition and assumptions | Validation / counterexample | Disposition |
|---|---|---|---|---|
| LC-22 | k-anonymity: min_q ∣EC(q)∣ ≥ k; l-diversity incl. entropy l-diversity; t-closeness (§10) | Standard definitions (Sweeney 2002; Machanavajjhala et al. 2007; Li, Li and Venkatasubramanian 2007). | — | reference |
| LC-23 | P_singling-out ≤ 1/k (§10; LG-SRC-02 §1) | Holds only for an adversary who knows the target's quasi-identifiers, nothing about the other class members, and guesses uniformly. Background knowledge can raise it to 1. Homogeneity discloses attributes without re-identification. "Singling out" in the WP216 sense is not a probability. | RX-18: k = 3, adversary knows 2 others → 1. RX-19: homogeneous class → attribute disclosed with probability 1 | research (state the adversary) |
| LC-24 | P_unique = N_unique / N_total (§10) | A population-level sample statistic, not a per-record probability, and not interchangeable with 1/k. | — | reference |
| LC-25 | Adv_MIA = TPR − FPR (§11) | Correct at a fixed threshold. Report the threshold, and both orientations. | RX-16 | adopted |
| LC-26 | Risk_MIA = max(0, 2·AUC − 1) (§11; LG-SRC-02 §2, §6) | Clipping at zero hides an inverted but equally informative attack: AUC = 0.2 is as revealing as 0.8. PGF already uses orientation-invariant gates (Doc 18 §3.3.0). AUC is an average over thresholds and can hide exposure at low false-positive rates (Carlini et al. 2022). Report TPR at a fixed low FPR as well. | RX-16: perfectly inverted attack, legacy 0 vs actual 1. RX-17: AUC 0.55 (2AUC − 1 = 0.1), yet 1 in 10 members identified with certainty at FPR 0 | rejected (clipping); replaced by \|2·AUC − 1\| plus low-FPR TPR |
| LC-27 | Wilson interval for an attack success proportion (§11) | Standard (Wilson 1927). Use a one-sided upper bound for gate decisions, as in PGF. | — | adopted |
| LC-28 | I_struct = log₂∣Ω_before∣ − log₂∣Ω_after∣ (§13; LG-SRC-02 §4) | Hartley information. It equals the entropy reduction only for a uniform prior over Ω. | RX-20: 1 Hartley bit vs < 0.2 Shannon bits under a skewed prior | research (state the prior) |
| LC-29 | "PSI 0.33 → 0.24", "59% / 41%", "VFL 82.6 bits / 0.9996" (LG-SRC-03) | Run artefacts, data, configuration and metric definitions are not available in the reviewed material. | — | unresolved (archival; not reproduced) |

### 3.6 Synthetic data, utility and decisions

| ID | Claim | Exact definition and assumptions | Validation / counterexample | Disposition |
|---|---|---|---|---|
| LC-30 | DCR, NN-leakage, TSTR utility, feature-importance correlation (§12) | Proximity and utility statistics. They are useful diagnostics, **not privacy guarantees**: a high DCR does not exclude membership or attribute inference. | — | reference (diagnostic only) |
| LC-31 | Gate set including "CVPL ≤ τ_CVPL" (§12; LG-SRC-02 §2) | **CVPL is not defined** anywhere in the reviewed material. No definition is supplied here. | — | unresolved |
| LC-32 | Score = w_R(1 − R) + w_Q·Q + w_C·C − w_U·U (§16) | A compensatory score lets utility offset privacy failure. In PGF, utility never compensates a failed privacy gate (Doc 18 §3.3.0; docs/02). | — | rejected for gating; usable only to rank options that have already passed every gate |

### 3.7 Evidence status in the prior prototype (LG-PROTO-01)

| ID | Behaviour | Problem | Validation | Disposition |
|---|---|---|---|---|
| LC-33 | "R_upper" treats a not-measured attack as success probability 0.5 × confidence | Labelled worst case, but bounded by 0.5. With no measurement and no proven bound, the only sound upper bound is 1, and the honest status is UNKNOWN, kept separately from the value. | RX-21 | rejected as an upper bound |
| LC-34 | A finding whose lifecycle is CLOSED contributes p = 0 | Lifecycle status is not evidence. Only conformance evidence (PASS) makes a control count. | RX-22 | rejected |
| LC-35 | Noisy-OR within a group; then R_sys = 1 − Π(1 − G·Sev/5) | LC-07 (dependence) plus LC-11 (a severity scale inside a union). | RX-01, RX-02, RX-06 | rejected |
| LC-36 | "Partial" finding weight 0.3 | Unexplained constant; no calibration. | — | unresolved |

## 4. What this means for PGF v1

- PGF v1 uses none of the rejected formulas. Its likelihood and severity scores are ordinal, its tiers come from a matrix lookup, and its PET module keeps individual metric results, with gates and orientation-invariant confidence bounds (docs/02).
- Two lessons are consistent with v1 and are already reflected in it: missing mandatory evidence gives INCOMPLETE, not 0 or PASS; and utility never compensates a failed gate.
- Lessons for a future version, not adopted here:
  - report TPR at a fixed low FPR next to AUC (LC-26);
  - state the adjacency relation wherever parallel composition is claimed (LC-20).

  These are proposals for a later PGF decision and are listed in `ERRATA.md` as improvement candidates, not as defects of v1.

## 5. Primary sources

- C. Dwork, A. Roth, *The Algorithmic Foundations of Differential Privacy*, Foundations and Trends in TCS 9(3–4), 2014.
- P. Kairouz, S. Oh, P. Viswanath, "The Composition Theorem for Differential Privacy", ICML 2015.
- L. Wasserman, S. Zhou, "A Statistical Framework for Differential Privacy", JASA 105(489), 2010.
- J. Dong, A. Roth, W. Su, "Gaussian Differential Privacy", JRSS B 84(1), 2022.
- F. McSherry, "Privacy Integrated Queries", SIGMOD 2009 (parallel composition).
- S. Yeom, I. Giacomelli, M. Fredrikson, S. Jha, "Privacy Risk in Machine Learning: Analyzing the Connection to Overfitting", IEEE CSF 2018.
- N. Carlini, S. Chien, M. Nasr, S. Song, A. Terzis, F. Tramèr, "Membership Inference Attacks From First Principles", IEEE S&P 2022.
- L. Sweeney, "k-Anonymity: A Model for Protecting Privacy", IJUFKS 10(5), 2002.
- A. Machanavajjhala, D. Kifer, J. Gehrke, M. Venkitasubramaniam, "ℓ-Diversity: Privacy Beyond k-Anonymity", ACM TKDD 1(1), 2007.
- N. Li, T. Li, S. Venkatasubramanian, "t-Closeness: Privacy Beyond k-Anonymity and ℓ-Diversity", ICDE 2007.
- I. Dinur, K. Nissim, "Revealing Information while Preserving Privacy", PODS 2003.
- E. B. Wilson, "Probable Inference, the Law of Succession, and Statistical Inference", JASA 22(158), 1927.
- J. Pearl, *Probabilistic Reasoning in Intelligent Systems*, 1988 (noisy-OR and its independence assumption).
- Article 29 Working Party, Opinion 05/2014 on Anonymisation Techniques (WP216).
- NIST SP 800-226, *Guidelines for Evaluating Differential Privacy Guarantees* (final, 2025).
- NIST SP 800-188, *De-Identifying Government Datasets: Techniques and Governance* (2023).
- NIST IR 8062, *An Introduction to Privacy Engineering and Risk Management in Federal Systems* (2017).

*Bibliographic details are to be checked against the publishers' records before any external use.*
