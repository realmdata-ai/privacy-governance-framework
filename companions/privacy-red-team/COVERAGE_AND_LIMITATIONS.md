# Coverage and limitations

Preview 0.2.0-preview.1, reviewed 29 October 2026. This record separates a written procedure from a reproduced observation and from product implementation evidence.

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
- Card statuses describe test criteria and evidence, separately from the PGF calculation and business decision. In MIA-POWER-01 the valid Wilson interval does not establish the declared ceiling, so the card criterion is FAIL. There is no automatic tier override. A missing selected weighted input prevents calculation; missing diagnostics are coverage limitations; missing evidence prevents the corresponding claim. An adopted release condition can block release separately. Six additional artificial handoff fixtures exercise these distinctions; they do not calculate a real risk or grant permission. The [compatibility note](PGF_1_0_0_COMPATIBILITY.md) explicitly records residual Doc 08 / Doc 18 inconsistencies.
- The Wilson calculation assumes a simple binomial experiment and independent trials; it is not an AUC interval or a general clustered-data method. Sampling design, repetitions, dependence and multiplicity need a real assessment design.
- The examples do not specify a universal unacceptable-success threshold. Local thresholds require a rationale tied to the protected population, harm, channel and adversary.
- The playbook has received an internal first review; it has not had independent methodological peer review. The primary-source check is not an exhaustive state-of-the-art survey.
- This preview does not define a calibrated probability-of-harm model, a scalar cross-attack risk score or a mathematical upper bound for unknown attacks. Those are distinct modelling questions.

## Before a real deployment or further release

Maintain attribution and the repository licence scope; confirm rights and terms for any newly introduced material; review anonymisation and indirect identifiability of any adapted real case; review the method against the risk-model companion; independently validate attack implementations selected for real use; review the source references and any legal interpretation. A public methodology may describe an attack family without distributing internal operational code or findings. Those review tasks do not create new requirements for the already accepted PGF v1 release.

## Verification performed on this preview

The author ran the standard-library verifier against 19 invented fixtures (13 attack/evaluation examples and six governance-handoff controls) and checked local link targets, Python syntax and neutralisation terms. Detailed validation evidence and protected-source mapping are retained outside the companion. No PGF v1 file was edited.
