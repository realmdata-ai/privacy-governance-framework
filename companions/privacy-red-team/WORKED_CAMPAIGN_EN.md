# Worked campaign: one dataset, two release channels

Preview 0.1.0-preview.1 · Review date: 27 October 2026
**Teaching case WC-01.** Every person, value and observation below is invented. This is a complete reasoning exercise, not a measured result for a PET product. Run `python verify_examples.py` to reproduce the selected observations. The campaign intentionally starts with leaky toy designs.

## 1. Business question and scope

A fictional statistics team wants to share a four-row transformed table and offer a partner a monthly matching service. Its approved purpose requires a broad distributional table and a match result for the statistics team only. The partner should receive neither per-person results nor intersection counts. The protected unit is one person across their rows and monthly sessions.

Version A exposes a table containing `age` and `zone`. It also returns an intersection count to the partner. The evaluator knows artificial ground truth to judge an attack; the adversary receives only its declared inputs and outputs.

## 2. Observation records

| Channel | Observer | Auxiliary knowledge | Observation allowed in version A |
|---|---|---|---|
| Public table | Public observer | The target is 42 and lives in zone B | Four age/zone rows |
| Matching API | Partner choosing inputs | Two filler identifiers known not to be in the other set | Exact intersection cardinality for each query |
| Model output | Public observer | As above | No model or score in this exercise |

The public observer can locate exactly one row with age42/zoneB. Controlled ground truth confirms that it is the target's row. The partner first submits the two fillers and receives 0, then adds `target-x` and receives 1. The difference identifies membership. No cryptographic key is attacked.

## 3. Predeclared questions and criteria

- RT-01: does the quasi-identifier release produce a unique correct link for the target? Illustrative criterion: any verified link of a protected target is unacceptable for this exercise.
- RT-07: does the forbidden partner output reveal target membership under the allowed two-query interaction? Criterion: any result-dependent count observed by that party is a design failure under the declared output contract.
- RT-03: can membership be inferred from a trained model? The campaign has no trained model or score output. Mark this narrowly NOT APPLICABLE for the model-output channel, with a trigger to re-open it if that access is introduced. Released-data-only membership inference is a separate question: without a specified generation process, source membership and a validated attack it is INCOMPLETE, even when no model is available.

The controls include a deliberately unique row for RT-01 and a deliberately count-revealing API for RT-07. A test unable to detect these controls is INCOMPLETE. Criterion selection occurs before execution.

## 4. Results of version A

| Card | Toy observation | Criterion result | Meaning |
|---|---|---|---|
| RT-01 | One matching released row for the target; ground truth confirms correctness | FAIL | The permitted table channel supports the tested link |
| RT-07 | Count0 without target, count1 with target | FAIL | Cardinality is a membership channel for this query design |
| RT-03, model-output channel | No model or score channel exists in this target | NOT APPLICABLE | Only this access channel is excluded |
| RT-03, released-data-only channel | Generation/membership/attack evidence is not specified | INCOMPLETE | Missing model access does not exclude released-data-only attacks |

These two findings remain distinct; neither is an estimate of total probability of harm. The existence of a strong cryptographic protocol would not remove an intended-output leak.

## 5. Treatment and a narrow retest

Version B removes the age/zone pair and provides only a broad, non-row-level count table. It changes the matching interface so the partner receives a fixed acknowledgement with fixed test-transcript length, independent of matches; only the statistics team receives the result. The production design would also require an assessment of timing, errors, retries, coalition assumptions, coercion and implementation behaviour.

The exercise's retest verifies that the removed quasi-identifier channel is absent and that the two supplied partner transcripts are identical. This produces a scoped PASS for those two toy assertions. It cannot prove that a real protocol has no side channel: without realistic implementation and protocol evidence, that broader question is INCOMPLETE. A failed search for other attacks must not be labelled proof of anonymity.

## 6. Evidence pack and governance handoff

The record contains target versions A/B; fixture and configuration hashes; observer and auxiliary-data descriptions; declared criteria; the selected query/response transcript; the target-match observation; controls; results; limitations; and reviewer/disposition references. Personal source records are unnecessary because the whole exercise is fabricated.

The Processing Owner takes the findings into the release decision under the adopted PGF process. Document18 receives the test evidence and missing-test scope; a DPIA under Document19 considers possible harm; a TIA under Document20, if applicable to a real arrangement, still requires its legal assessment; Document27 receives the remediation and retest evidence. The DPO advises and monitors. This exercise does not create a real legal or risk-acceptance decision.

## 7. What to carry into a real campaign

Replace the toy criteria with locally justified criteria, representative data, a declared independent privacy unit, validated attack implementations and an adequate uncertainty design. Retain known-positive controls. Expand the output contract to all actual channels. A test card is reusable only after its assumptions are checked against the new target.
