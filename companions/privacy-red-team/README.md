# Privacy Red-Team Playbook

**Preview 0.1.0-preview.1 — 27 October 2026. Private repository review copy.** This independent companion targets the accepted English PGF 1.0.0-rc.1. It is outside the PGF v1 release, creates no release dependency, and changes no PGF document. Authorship, rights and public distribution terms remain to be confirmed; no licence is granted by this preview.

Start with [the playbook](PLAYBOOK_EN.md), read the [complete worked campaign](WORKED_CAMPAIGN_EN.md), then follow the [worked test cards](cards/TEST_CARDS_EN.md). Use the [blank card](TEST_CARD_TEMPLATE.md) for a new assessment. [Primary references](REFERENCES.md) identify the evidence behind the method. [Coverage and limitations](COVERAGE_AND_LIMITATIONS.md) distinguish specified procedures from implemented tests.

The accompanying [toy fixtures](fixtures/examples.json) are wholly invented. Run `python verify_examples.py` from this directory to reproduce their arithmetic and observations with Python 3.11+ and the standard library. The verifier does not attack a system, train a model, validate a PET implementation or establish anonymity. Its fixed examples are teaching controls, not a benchmark of any product. No private attack library or client assessment has been copied into this package.

## Intended readers

Privacy engineers use the cards to produce evidence. Processing Owners and Legal use the findings in decisions. DPOs advise and independently monitor; Internal Audit may provide independent assurance. Readers need not begin with cryptographic proofs: the introduction explains what is protected, who can observe what, and why a successful computation can still disclose information.

## Package

| File | Use |
|---|---|
| PLAYBOOK_EN.md | Scope, campaign method, observations, decision semantics and PGF interfaces |
| TEST_CARD_TEMPLATE.md | A complete record for a repeatable test |
| cards/TEST_CARDS_EN.md | Twelve worked cards, including attack and evaluation controls |
| fixtures/examples.json | Invented data, observer scope and expected observations |
| verify_examples.py | Reproduces selected toy observations and statistical calculations |
| REFERENCES.md | Primary publications, dates, status and bounded use |
| COVERAGE_AND_LIMITATIONS.md | Coverage, gaps and remaining review work |

The preview validation record is in [reports/validation_preview.json](reports/validation_preview.json). Reproduce it with `python verify_examples.py > reports/validation_preview.json`. This record covers the invented examples only.

Use an approved assessment scope and minimise retained personal information in a real deployment. The examples require no real identifiers or production data. Thresholds in the cards are illustrative policy choices. An assessment must justify its own criteria before observing results.
