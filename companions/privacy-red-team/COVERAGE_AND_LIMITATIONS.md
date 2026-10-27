# Coverage and limitations

Preview 0.1.0-preview.1, reviewed 27 October 2026. This record separates a written procedure from a reproduced observation and from product implementation evidence.

| Card | Written procedure | Reproduced in this package | Outside the current implementation |
|---|---|---|---|
| RT-01 linkage | Preview procedure | Four-row exact candidate-set exercise | Representative linkage attacks; auxiliary-data uncertainty; large-population evaluation |
| RT-02 attribute inference | Preview procedure | Invented baseline-versus-group-rule arithmetic | Trained attackers, calibration, realistic sensitive attributes and sample uncertainty |
| RT-03 membership | Preview procedure | Confusion matrix, prior-adjusted PPV, Wilson power counterexample | Attack training, score calibration, ROC/AUC intervals, shadow/reference models |
| RT-04 synthesis | Preview procedure | Planted subgroup exposure counterexample | Generator runs, realistic memorisation and distance/model attacks |
| RT-05 reconstruction | Preview procedure | Two binary variables with exact constraints | Large-scale query reconstruction or DP attack |
| RT-06 repeated releases | Preview procedure | Two-count differencing | Release-history ingestion, overlap estimation and adaptive workload |
| RT-07 PSI inputs | Preview procedure | Small explicit-set cardinality counterexample | Cryptographic protocol implementation and malicious-party validation |
| RT-08 PSI metadata | Preview procedure | Deliberately result-dependent lengths vs fixed lengths | Real timing, error/retry channels, coalition/key-control validation |
| RT-09 FL channels | Preview procedure | Planted label-correlated lengths vs constant model scores | Training, gradient inversion, secure aggregation validation, real protocol capture |
| RT-10 auxiliary artefacts | Preview procedure | Observable-run cost summation | System observation-boundary proof, production logging and RDP accountant |
| RT-11 evidence controls | Preview procedure | Missing/failed-control dispositions and input validation | Production workflow integration, signing, sealed storage and robust schema engine |
| RT-12 scope changes | Preview procedure | Added-field detection | Legal classification, semantic schema analysis and a real decision workflow |

## Interpretation limits

- Every reproduced example is wholly artificial. Matching its expected observation verifies a teaching calculation, not a PET or a real release.
- No private attack suite, application or archived client assessment was executed in this pass. Existing repository statements about attack counts, maturity or measured performance are not independently confirmed here.
- A fixture with a PASS status states that its explicit assertion is met. It does not establish a general defence, a formal privacy guarantee or lawful anonymity. Individual FAIL observations are preserved even if campaign coverage is incomplete.
- Card statuses describe measurement/evidence. When supplied to PGF, preserve its routing: a valid mandatory result with an unfavourable confidence bound beyond its configured threshold is G-M1 FAIL (release blocked); absent, invalid or unestimated mandatory evidence is G-M5 INCOMPLETE. In MIA-POWER-01 the confidence conclusion is "ceiling not established", while the module mapping is G-M1 FAIL. This companion does not relax a PGF failure condition or replace its legal gates.
- The Wilson calculation assumes a simple binomial experiment and independent trials; it is not an AUC interval or a general clustered-data method. Sampling design, repetitions, dependence and multiplicity need a real assessment design.
- The examples do not specify a universal unacceptable-success threshold. Local thresholds require a rationale tied to the protected population, harm, channel and adversary.
- The playbook has received an internal first review; it has not had independent methodological peer review. The primary-source check is not an exhaustive state-of-the-art survey.
- This preview does not define a calibrated probability-of-harm model, a scalar cross-attack risk score or a mathematical upper bound for unknown attacks. Those are distinct modelling questions.

## Before public release or deployment

Confirm authorship/rights and distribution terms; review anonymisation and indirect identifiability of any adapted real case; review the method against the risk-model companion; independently validate attack implementations selected for real use; review the source references and any legal interpretation. A public methodology may describe an attack family without distributing internal operational code or findings. Those review tasks do not create new requirements for the already accepted PGF v1 release.

## Verification performed on this preview

The author ran the standard-library verifier against 13 invented fixtures and checked local link targets, Python syntax and neutralisation terms. Detailed validation evidence and protected-source mapping are retained outside the companion. No PGF v1 file was edited.
