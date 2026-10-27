# Privacy Red-Team Playbook

Version 0.1.0-preview.1 · Preview · Reference/review date: 27 October 2026

## 1. Why this playbook exists

A team can remove names, encrypt a computation, synthesise records or distribute training across several institutions and still disclose information about people. An output can reveal membership in a sensitive list; several acceptable-looking tables can expose a small group when combined; a model can remember an unusual training record; a protocol can reveal labels through message lengths. The relevant question is what an observer can infer in the complete processing arrangement.

Privacy red teaming deliberately tests that question against a declared target. It helps an organisation find and correct unwanted disclosure before release and re-examine earlier decisions when new evidence appears. It supplies evidence to governance. It does not itself establish a lawful basis, decide whether information is legally anonymous, or authorise an international transfer.

The practical unit is a **test card**. It identifies the person-level fact to protect, the adversary's access, auxiliary knowledge, allowed queries, observations, success measure and uncertainty. A result without those details is difficult to interpret or reproduce. The same numerical metric can describe very different attacks.

For example, an AUC near 0.5 for a model-output membership test says little about a protocol transcript that explicitly lists participating identifiers. The two tests expose different channels. The correct report preserves that difference rather than averaging it away.

## 2. A small running example

A fictional organisation proposes to release a small synthetic dataset and to run a monthly matching service with a partner. The public dataset contains invented categories and transaction-like values. The partner service should reveal matches to the organisation only. We ask:

1. Can a public observer combine a released quasi-identifier with auxiliary information to identify one source person?
2. Can the synthetic release expose membership or a sensitive attribute, especially for rare groups?
3. Can repeated matching queries, cardinalities or message lengths reveal membership to the partner?
4. Can previews, debug logs or selection results reveal more than the approved release?

The files under `fixtures/` reduce these questions to transparent toy observations. Each fixture names its observer and output scope. They are not measurements of a deployed system. More complex deployment tests need representative datasets, realistic protocols and independently validated attack implementations.

## 3. Keep five statements separate

| Statement | Evidence needed | What it does not establish |
|---|---|---|
| A technique has a formal guarantee | Precise definition, assumptions, mechanism and proof/accountant applicable to the implementation | That every operational output is covered |
| An attack found a disclosure | Valid attack, target population, access conditions and reproducible result | The legal conclusion or total probability of harm |
| A test did not find an unacceptable disclosure | Valid controls, sufficient power, declared attack set and uncertainty | Absence of other attacks or proof of anonymity |
| The assessment covered its mandatory scope | Versioned applicability and coverage record | Completeness against every possible adversary |
| Processing may proceed | Competent controller decision after applicable legal and assessment gates | A decision that the red team can make on the controller's behalf |

NIST SP 800-226 treats implementation and system hazards as important to evaluating differential privacy [R1]. NIST SP 800-188 considers release models and governance alongside de-identification techniques [R2]. These are reasons to inspect the entire path to an observer, including auxiliary outputs.

## 4. Define the assessment boundary

Record a versioned target anchor: system or pipeline version, configuration, source population, privacy unit, artefacts, decision date and responsible owner. A privacy unit may be all records of one person, not an arbitrary row. For a graph it may be an edge or a node; the choice changes the question and must be explicit.

Draw the processing and observation path in simple terms. Include source data, extracted features, generator or model, intermediate artefacts, previews, API responses, logs, checkpoints, reports, recipients and retention. A list of component names without outputs and observers is insufficient.

For each observer, state:

- what it receives and what it can query;
- what it already knows, including its own records and public or purchased auxiliary information;
- whether it can choose, adapt, repeat or poison inputs;
- whether it can observe message sizes, timing, ordering or identifiers;
- who it may collude with and which trust assumptions exclude that coalition;
- the time, computation, expertise and query budget considered realistic.

An exclusion needs a reason and supporting control. "Not tested" is not a reason to mark a channel absent. If the control that excludes a channel stops being valid, applicability must be re-evaluated.

## 5. Roles and campaign records

The Processing Owner defines the business activity and owns treatment and operational decisions within the adopted governance. Legal evaluates applicable law and gates. The DPO gives advice and monitors independently. A test lead designs the assessment and records limitations; an engineer executes the approved tests. Where independence matters, someone other than the pipeline producer validates attack implementations and reviews the findings.

Use these records:

1. **Campaign plan:** target anchor, questions, authorisation, scope and observers.
2. **Applicability matrix:** attack/channel combinations; mandatory, conditional, excluded or not assessed, with reasons.
3. **Pre-registration:** metrics, splits, controls, repetitions, criteria and stopping rules.
4. **Execution records:** input hashes, configuration, code/environment version, results and failures.
5. **Findings:** affected fact/population, observation, harm scenario, confidence and uncertainty.
6. **Disposition:** remediation owner, restricted use or pause where necessary, retest condition and governance references.

A newly applicable mandatory test is not silently dropped to retain a previous PASS. Configuration changes create a new recorded version. Failed tuning runs remain traceable; retaining necessary evidence does not justify retaining source records indefinitely.

## 6. Establish that a test can detect the problem

Before using a negative result, run a known-positive control. A deliberately copied synthetic record should be detectable by an exact-match diagnostic; a deliberately result-dependent transcript should be distinguishable. Run a suitable negative control as well to detect trivial artefacts, label leakage, accidental overlap and indiscriminate flags.

These controls validate a limited behaviour of the test. They do not prove that the test detects every realistic failure. A test that succeeds only because member and non-member populations come from different distributions may measure dataset shift rather than training membership.

If a control fails, preserve the observed result and mark its interpretation provisional or INCOMPLETE. Investigate before relying on it. A missing implementation, exception, empty evaluation set or missing label is not a successful negative test.

## 7. Measurement and uncertainty

### 7.1 Counts, populations and splits

State the denominator and unit for every fraction. Separate calibration data from final evaluation data. Prevent identity overlap across splits at the privacy-unit level, including duplicate rows belonging to one person. Fix attack direction, threshold and subgroup analysis using calibration data rather than selecting whichever evaluation result appears favourable.

For a membership test record TP, FP, TN and FN, not just an aggregate score. Report TPR, FPR and relevant confidence intervals. Report ROC/AUC where a range of score thresholds is available; one confusion matrix does not determine AUC. Low-FPR performance matters because identifying a small set of people confidently can be harmful even when average accuracy looks modest [R5].

### 7.2 Base rates

A balanced evaluation set is useful for comparison, but its precision does not transfer automatically to deployment. With a membership prior `pi`, sensitivity `t` and false-positive rate `f`, the implied positive predictive value is:

`PPV = pi*t / (pi*t + (1-pi)*f)`

This calculation assumes those operating characteristics apply to the deployment population. In the toy example, `t=0.8`, `f=0.02`, `pi=0.001` gives PPV about 3.85%. It does not make the test harmless: it changes what an attack claim means and may create harmful false accusations.

### 7.3 Intervals and power

Name the interval method, confidence level, independent unit and resampling design. A binomial interval for a simple fixed-rate experiment is not automatically an appropriate AUC or clustered-identity interval. Use a method compatible with dependencies and report subgroup sizes.

The verifier shows the two-sided Wilson 95% interval for simple binomial teaching cases. With zero false positives among 1,000 negatives, the upper endpoint is about 0.00383. That experiment cannot establish FPR below 0.001 at that confidence level. The confidence conclusion is that the ceiling has not been established; it is not evidence of zero risk. This is still a valid interval estimate. Under the frozen PGF routing, a valid mandatory measurement whose unfavourable confidence bound crosses its configured threshold maps to **G-M1 FAIL** and blocks release. Missing, invalid or unestimated mandatory evidence maps to **G-M5 INCOMPLETE**. Do not convert a valid threshold failure into INCOMPLETE merely because a larger sample might narrow the interval.

Run-to-run variation and statistical uncertainty are different. Document both. Do not treat five repeated runs of the same 100 persons as 500 independent people. Adjust a pre-registered multiple-comparison strategy when searching many subgroups or attack variants.

### 7.4 Useful diagnostics and their limits

Distances, exact matches, uniqueness, k/l/t properties, utility scores and formal DP parameters are not interchangeable. Distance can reflect ordinary population similarity or feature scaling. An empirical privacy audit can discover implementation failures but does not prove differential privacy. A failed attack supplies evidence of its own limits. Utility is reported separately and does not cancel a privacy finding.

## 8. Results and coverage

Use a result per card, observer and configuration:

- **PASS:** the declared criteria are met, required evidence and controls exist, and uncertainty is within the pre-registered acceptance rule.
- **FAIL:** a declared unacceptable observation or criterion is established; show the result and uncertainty.
- **INCOMPLETE:** mandatory evidence or applicability is missing, a control or evaluation design is invalid, or a required measurement has not been estimated. A valid confidence interval that exceeds a configured threshold remains a FAIL under the PGF mapping; it is not moved here solely because its precision is insufficient to establish compliance.
- **NOT APPLICABLE:** the question does not arise for the stated observer and version, with a documented reason and validation of any control excluding it.

Report attack success separately from these criterion outcomes. PASS can coexist with non-zero measured disclosure below an illustrative internal threshold; it never means zero risk. A successful observation can be provisional if the test has failed its controls. Resolve that uncertainty without suppressing the observation.

A campaign preserves every known FAIL even if other mandatory tests are INCOMPLETE. It does not average either away. Show mandatory coverage as a list of tests and channels with status and reasons. A percentage can supplement that list, but does not replace it. No probability is assigned to unknown attacks in this playbook, and no aggregate "upper risk bound" is computed from arbitrary default priors.

## 9. Retain enough evidence to reproduce the conclusion

A minimal finding includes campaign/card ID; target and privacy unit; observer and auxiliary-data specification; test/configuration/environment version; split hashes; controls; query transcript or sanitised observation; counts and uncertainty method; declared criterion; result; limitations; timestamps; reviewer and disposition references.

Protect raw records separately from the report. Where a small example is needed, prefer artificial data. Apply access restrictions and retention to evidence components; a sealed manifest is not a reason to retain personal information forever. Hashes establish integrity relative to a trusted reference; they do not by themselves authenticate the producer or prove the computation was correct.

Different audiences may receive redacted extracts from one traceable evidence record. Keep the mapping from a reported figure to the underlying observation. A slide or spreadsheet number with no run/configuration provenance remains unverified.

## 10. Feed results into PGF without changing it

| PGF interface | Evidence supplied | Decision retained by governance |
|---|---|---|
| Document 18: risk method and PET module | Declared adversary/channel, controls, metrics, intervals, failed or missing tests | Method application, legal anonymity conclusion and applicable module gates |
| Document 19: DPIA | Harm scenarios, affected populations, demonstrated residual disclosure and uncertainties | Lawfulness, necessity, proportionality, G-36 conclusion and risk decision |
| Document 20: TIA | What each recipient can observe, recover, combine or be compelled to provide; effectiveness limits of measures | Destination-law assessment and transfer mechanism determination |
| Document 27: monitoring and assurance | Reproducible findings, evidence references, unresolved scope and retest results | Independent assurance and remediation oversight under the adopted model |

A disclosure finding may also require assessment under the breach-response process. The red team records facts; it does not apply a harm filter to decide that a personal data breach does not exist.

This companion uses PGF reference points rather than adding controls to the frozen PGF text. It is a preview aid, not a dependency of PGF v1. A full risk score, calibrated expected-loss model and reference risk calculator belong to the separate risk-model companion.

## 11. Retest and monitoring

Retest on a material change to inputs, labels, source population, recipient, output function, protocol, model, software, auxiliary data, query policy, coalition assumptions or mitigation. A new attack method can invalidate a prior coverage claim. A change to the control excluding a channel re-opens that channel.

A retest links to the previous finding and configuration. It records whether the earlier disclosure is prevented, reduced or still present; it does not erase the earlier report. A narrower post-remediation test cannot silently replace a broader earlier campaign.

## 12. First use

Begin with one realistic processing activity, one owner and a small number of high-consequence observations. Complete the target and observer records before choosing metrics. Run the teaching fixtures to understand the reporting conventions, then design validated tests for the real implementation. Keep the distinction between a demonstration, a product test and an independent assessment visible throughout.
