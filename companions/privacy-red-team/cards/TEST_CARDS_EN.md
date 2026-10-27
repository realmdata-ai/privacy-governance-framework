# Worked privacy test cards

Preview 0.1.0-preview.1 · Review date: 27 October 2026 · All numerical criteria and data below are illustrative. The cards are procedures, not claims of an implemented attack library. See the [playbook](../PLAYBOOK_EN.md), [worked campaign](../WORKED_CAMPAIGN_EN.md), [fixtures](../fixtures/examples.json) and [references](../REFERENCES.md). A real campaign fills the target, observer, data and implementation records before execution.

## RT-01 — Singling out and correct record linkage

**Question and scope.** Can a public observer isolate and correctly link a protected person in the released table? The observer receives the release and a target's known age/zone; it does not receive the evaluator's identity mapping. Privacy unit: one person.

**Procedure.** Define the quasi-identifier transformation and allowed matching rule before testing. Produce a candidate set for every held-out target using the same release accessible to the observer. Report candidate-set size and correct links against evaluator-only ground truth. Do not claim a correct identity solely because one row looks similar. Repeat for declared auxiliary-data quality and overlapping-population scenarios.

**Controls, metric and criterion.** A planted unique target is the positive control; a deliberately ambiguous target with two candidates is the negative control for a unique-link claim. Report correct unique links / evaluated targets, false links, abstentions and candidate sizes. For sampled targets, use a suitable person-level interval; the four-row toy is an enumerated exercise and needs no inference interval. Toy criterion: any verified protected-target link is FAIL. One candidate matching age42/zoneB in fixtureWC-01 is the expected FAIL.

**Evidence and response.** Keep the matching rule, auxiliary schema, target-split hashes and a minimal link witness. Coarsen or remove the field combination, change the release/access model, then retest. A claim of `1/k` protection requires its own adversary assumptions; an equivalence-class size is not a universal bound on re-identification. Baseline: the same matching rule on a coarser release. PGF18/19; sourcesR2/R7.

## RT-02 — Sensitive-attribute inference beyond a baseline

**Question and scope.** Can a recipient infer an undisclosed sensitive attribute more accurately because of the release? The evaluator holds the attribute for testing; it is excluded from the observer's auxiliary inputs. Unit: person; utility predictions and harm are separately assessed.

**Procedure.** Fit or specify an attacker using only allowed inputs, on separate calibration data. Compare two matched conditions: auxiliary information alone and auxiliary information plus the release. Evaluate on held-out identities and declared subgroups. Check that the target attribute, its obvious proxy or evaluation label has not entered the attack input accidentally.

**Controls, metric and criterion.** Use an invented group with a planted attribute association as the positive control; use an independently permuted label as a negative control. State baseline accuracy, release-assisted accuracy, calibration, abstention and subgroup counts. The toy has six balanced-label persons: a majority-only baseline is 3/6, while a group rule predicts 6/6. The observed accuracy gain is 0.5 for this finite invented set. It is evidence of the constructed association, not a population estimate. A real criterion might restrict specified incremental disclosure, justified before results; no universal gain threshold is supplied.

**Result and response.** Toy criterion `gain >0.2` is FAIL. With unrepresentative auxiliary data or a missing held-out set, the deployment conclusion is INCOMPLETE. Retain both baseline and assisted predictions and data provenance. Remove or reduce the revealing association/access, then reassess the intended analytical use and harm. PGF18/19; sourcesR2/R4.

## RT-03 — Membership inference with operating point and base rate

**Question and scope.** Can an observer distinguish training members from non-members through the released model or synthetic dataset? Specify black-box scores, labels-only access, model parameters or released-data-only access separately. They are different tests.

**Procedure.** Separate attack calibration from evaluation. Use identity-disjoint member/non-member populations with comparable provenance. Fix score direction and the operating threshold before evaluating. Run a valid known-positive memorisation control and a negative control. Record every attack variant searched; do not select a favourable final threshold using test labels. For per-person targets, preserve within-person dependence in resampling.

**Metrics.** Report TP/FP/TN/FN, TPR/FPR with uncertainty, ROC/AUC if scores across thresholds exist, and TPR at a declared low FPR. The fixture hasTP 80, FN 20, FP 20, TN 980: TPR 0.8, FPR 0.02. Evaluation-set precision differs from deployment PPV: a prior 0.001 implies approximately 0.0385 PPV at that operating point. One confusion matrix cannot establish AUC. An AUC below0.5 may indicate invertible score direction; it is not automatically evidence of safety. Direction learned on calibration must be fixed for evaluation.

**Criterion and result.** For a fictitious configured FPR ceiling 0.001, zero FP / 1,000 negatives still has a valid Wilson 95% upper endpoint of about 0.00383. The confidence conclusion is **ceiling not established**. The separate frozen-PGF module mapping is **G-M1 FAIL**: the unfavourable bound exceeds the configured ceiling, so release is blocked. A larger sample might change the interval, but the current valid result is not re-labelled INCOMPLETE. Missing controls, an invalid split or an unestimated mandatory metric instead maps to **G-M5 INCOMPLETE**. The toy demonstrates routing for a configured criterion; it does not claim that FPR 0.001 is a universal privacy threshold or that a product passed. Retain score files, splits, thresholds, counts, interval method and query budget. Remediate/retrain or restrict output, then retest. PGF18/19; sourcesR1/R5/R6.

## RT-04 — Synthetic memorisation and exposed subgroups

**Question and scope.** Does a synthetic release reproduce protected records or expose rare groups more strongly than aggregate metrics suggest? Observer receives released rows only; evaluator has source and hold-out records. No access to a generator is assumed unless separately declared.

**Procedure.** Define exact-match and distance diagnostics, feature scaling and handling of categorical fields before evaluation. Compare against source-to-holdout distances and duplicate prevalence; a small distance alone is not a confirmed privacy breach. Evaluate source-membership or attribute attacks with the appropriate baseline. Report outlier and rare-group results as well as overall values.

**Controls, metric and criterion.** A deliberate source copy is the positive control for exact-match detection; a fabricated unrelated record checks indiscriminate matching. FixtureRT-04 has 3 exposed persons in a subgroup of 10 among 1,000 persons: aggregate exposure 0.003, subgroup exposure 0.3. A locally declared ceiling 0.1 on the at-risk subgroup is failed despite the low aggregate. This is a deliberately planted observation, not a measured generator result. For sampled groups use suitable intervals and multiplicity handling.

**Evidence and response.** Keep transformation/configuration hashes, split provenance, copy witnesses and subgroup denominators. Reduce memorisation, minimise access, change mechanism or reject the release as required by the adopted gates. New seeds alone are not remediation. A failed no-box attack neither proves privacy nor excludes attacks with model access. A DP claim needs its formal and implementation statement separately. PGF18/19; sourcesR1/R2/R4/R8.

## RT-05 — Reconstruction from exact outputs

**Question and scope.** Can a recipient recover individual facts by combining exact statistical answers? Observer receives only the specified answers, not raw records. Unit: the person-level bit or record represented by those outputs.

**Procedure.** Enumerate the equations and constraints actually available through tables, queries and public context. Attempt recovery using an independently specified reconstruction method; report what extra assumptions make a solution unique. Use held-out artificial ground truth to assess recovered values. Distinguish a unique recovery from one plausible solution among many.

**Controls, metric and criterion.** The toy releases `x1+x2=1` and `x1=1` for binary values. The second bit is therefore0. All2bits are uniquely recovered in this deliberately simple system. The negative variant exposes only the sum and leaves two possible assignments. Metrics: fraction uniquely recovered correctly, false recovery and unresolved values; sampled reconstruction needs a suitable uncertainty design. Toy criterion: any exact protected-bit recovery is FAIL.

**Evidence and response.** Retain permitted outputs, the reconstruction equations, assumptions and a compact recovery certificate. Reduce redundant exact answers, introduce a justified protective mechanism or change access. Test the union of outputs, not each table in isolation. This arithmetic example is not an implementation of large-scale database reconstruction or evidence that a DP mechanism fails. PGF18/19; sourcesR1/R2.

## RT-06 — Repeated releases and temporal differencing

**Question and scope.** Can one recipient combine outputs across time or related queries to recover a protected change? The observer retains earlier releases; deleting the latest local file does not remove prior observations.

**Procedure.** Build a release register by privacy unit, population, recipient and output. Identify overlap and changed inclusion rules. Reproduce permitted sequences and auxiliary context; compare single-release and combined inference. Include previewed, cancelled and failed runs if their outputs were observed. Do not assume event independence to aggregate attack success.

**Controls, metric and criterion.** The fixture releases count 100 for a group and count 99 for the same group excluding a known target. Both cells are large; their difference reveals the target's contribution 1. This is a FAIL under the toy criterion forbidding that exact contribution. A single-release negative variant has no matching subtraction answer. Metrics include exactly recovered contributions, query sequence, privacy units affected and inference uncertainty.

**Evidence and response.** Keep release IDs, recipient sets and an ordered witness, including earlier public outputs. Revise the release design and composition/linkage assessment. For genuine DP releases, verify the declared unit, accountant and observer scope; do not use a calendar reset or a product of unrelated attack probabilities as a privacy guarantee. Retest the entire observed sequence after changes. PGF18/19/27; sourcesR1/R2.

## RT-07 — PSI chosen and adaptive input disclosure

**Question and scope.** Can a party learn membership beyond the intended output policy by choosing inputs or repeating sessions? Specify which party receives a set, a cardinality, an aggregate or no result. A permitted result can itself reveal a sensitive fact.

**Procedure.** Enumerate allowed input construction, input-size bounds, commitment/validation rules, repeats and cross-session state. In an approved artificial environment compare queries containing known non-members with otherwise identical queries adding a target. Record all outputs visible to each party. A minimum set size alone is not a proof against this inference: many fillers may be known not to match.

**Controls, metric and criterion.** FixtureRT-07 uses two known non-member fillers. Cardinality 0 without `target-x` and1 after adding it reveals membership. A no-result observer receives identical fixed acknowledgements in the negative toy variant. Criterion: any forbidden result-dependent information to that observer is FAIL. This is a deterministic contract check for the fixture, not an estimate of cryptographic failure probability.

**Evidence and response.** Keep output contract, query/response witness, observer scope and protocol/implementation versions. Consider changing the recipient/output function and validating inputs; assess all channels under the revised design. Input commitment or larger batches may address some attacks but do not erase information intentionally returned by the function. A transfer and legal assessment remains separate. PGF18/20; sourceR3.

## RT-08 — PSI metadata and coalition assumptions

**Question and scope.** Does an observer excluded from the match result infer matches from message length, timing, retries or collusion? Use the declared coalition and key/control boundaries; do not average several powerful coalition scenarios into a reassuring scalar.

**Procedure.** Create balanced artificial inputs with equal public sizes but different intersection sizes. Capture outputs, packet/message lengths, ordering, errors and timing available to the observer. Test a predeclared distinguisher using separate calibration and evaluation runs. Explore only coalitions within the authorised scope, recording which assumptions would exclude them. Timing results require a realistic repeated design and environmental controls.

**Controls, metric and criterion.** The positive toy transcript length is64 + 8 times the match count; a two-state observer distinguishes0 versus 1 match perfectly. The negative variant always has length 128 and the same acknowledgement. Toy criterion: result-dependent length is FAIL; equality in two supplied transcripts supports only that narrow assertion. For a real implementation, absent timing evidence is INCOMPLETE, not PASS. Metrics include classifier advantage, confusion matrix, uncertainty and leakage channel.

**Evidence and response.** Retain sanitised transcripts and design assumptions; pad and normalise observable behaviour where appropriate, validate errors/retries and re-evaluate coalition/compulsion exposure. A cryptographic proof for a different adversary or leakage function does not cover this test. PGF18/20; sourceR3.

## RT-09 — Federated learning: model, update and transcript channels

**Question and scope.** Can a participant or coordinator recover membership, labels or attributes from model predictions, updates or protocol metadata? List horizontal/vertical setting, active/passive roles, access and collusion separately.

**Procedure.** Map every observation to the receiving party and training round. Compare a model-output attack with an allowed-transcript attack. A control excluding individual updates must be validated before declaring a gradient-reconstruction test not applicable. Evaluate final and intermediate models and aggregate releases within their declared DP scope. A claim about participant-level privacy cannot be inferred from a record-level experiment without justification.

**Controls, metric and criterion.** The fixture's model scores are constant 0.5, while transcript lengths 8/16deterministically track a binary label. The metadata rule recovers all 4 planted labels; the model-output score has no discrimination in the toy. Criterion: disclosure of an excluded label through the metadata contract is FAIL. A separate real inversion test without validated implementation is INCOMPLETE. Do not conflate these outcomes.

**Evidence and response.** Retain role/channel maps, update-access controls, per-round configuration and privacy accountant evidence where relevant. Fix the protocol observation or exclude that access with validated controls, then retest. Poisoning belongs here only when connected to a specific privacy harm or harmful decision; ordinary utility degradation is reported separately. PGF18/19/27; sourcesR1/R5.

## RT-10 — Auxiliary artefacts and observation-boundary accounting

**Question and scope.** Can a user, operator or recipient learn protected facts from logs, previews, checkpoints, diagnostics or model-selection outputs outside the declared release? The observer need not be an external attacker.

**Procedure.** Inventory generated artefacts and their readers. Use planted artificial markers to trace what can cross the declared boundary. Inspect retention, access changes, failed tasks and cancelled runs. For a DP claim, map each observed data-dependent output to the guarantee and accounting record; a final-release-only ledger is insufficient if earlier signals escaped.

**Controls, metric and criterion.** The toy run ledger includes a completed observed run costing epsilon 1.2 and a failed observed run costing 0.8. Both are charged: total 2.0. An unknown failed reservation cannot be treated as zero solely because no completion event exists. The positive control deliberately includes an observable preview; a non-observable abandoned internal run is distinguished only when the boundary evidence supports that conclusion. Missing output/audit evidence is INCOMPLETE.

**Evidence and response.** Record output type, observer, privacy unit, accountant statement and observation reason, with no raw production examples in a public report. Restrict/minimise artefacts and correct the accounting model before relying on a release claim. A generic canary trace does not mathematically measure epsilon or prove DP. PGF18/19/27; sourceR1.

## RT-11 — Evaluation and evidence negative controls

**Question and scope.** Would the assessment silently report PASS when a mandatory test is absent, a positive control fails, a denominator is empty or a result file is stale? This validates assessment behaviour, not a PET's empirical privacy.

**Procedure.** Inject one failure at a time into an invented result record: missing test, failed detector control, empty evaluation set, duplicated identities across splits, changed target hash or a scalar result lacking its observer. Retain the original input and expected disposition. A recorded finding must remain visible even when the overall campaign is incomplete.

**Controls, metric and criterion.** Expected status for an absent mandatory result or failed control is INCOMPLETE. A deliberately detected contract violation is FAIL even if another required test is missing. Only a complete, in-scope record meeting the declared criterion may be PASS. FixtureRT-11 includes absent-result and failed-control cases. An unrun attack is not given risk 0, and a status word such as "closed" cannot replace evidence.

**Evidence and response.** Preserve schema/version, negative fixture, actual disposition and reason. Hash integrity is checked against a trusted reference and separately from authenticity. Remediate the workflow or test implementation, then rerun the negative suite. This companion does not reuse a proprietary risk aggregator or assign numerical default priors to missing attacks. PGF18/27; sourcesR1/R2.

## RT-12 — Changes to inputs and purpose-linked harmful decisions

**Question and scope.** Does a schema, label, feature or audience change invalidate the previous privacy assessment or its stated legal/data-category boundary? The protected fact may be an inferred allegation or sensitive attribute, not a reconstructed raw row.

**Procedure.** Compare a versioned approved input/output specification with a changed one. Use artificial fields and keep the original meaning: a victim-side payment label, an offence-attributing label and a counterparty identifier are distinct inputs. Identify changed harm scenarios, recipients, observers and required legal review. Check that the workflow refers the change to the competent owner instead of silently preserving the previous tier or acceptance.

**Controls, metric and criterion.** Positive change: add an excluded offence-attributing label to the fixture's allowed feature list. Expected observation: a scope-change flag and reassessment requirement; the toy does not decide the legal interpretation or calculate a new real risk tier. Negative control: reorder an unchanged field list, preserving the same specification content. A workflow that continues to claim the old assessment covers the changed input is FAIL against the declared change-control criterion. Missing specification/provenance is INCOMPLETE.

**Evidence and response.** Keep the semantic schema diff, affected population/outputs and original decision reference. Re-open the applicable PGF gates and tests, record the new decision, and retest changed channels. A technical assertion that the file loads successfully does not settle necessity, lawfulness or harm. PGF18/19/20/27; sourceR2.
