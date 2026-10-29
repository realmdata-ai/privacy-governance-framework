# Primary references and method provenance

Preview 0.2.0-preview.1 — review date: 29 October 2026. Bibliographic source pages last checked: 26 October 2026. These references support particular concepts; no blanket conformance claim is made. Official publication pages and paper abstracts/metadata were reviewed during preparation on 26 October 2026. A full technical literature review and validation of particular attack implementations remain separate work. No third-party paper, private code or restricted report is reproduced here.

| ID | Primary source | Status and date | Use in this preview |
|---|---|---|---|
| R1 | [NIST SP 800-226, Guidelines for Evaluating Differential Privacy Guarantees](https://csrc.nist.gov/pubs/sp/800/226/final) | Final, March 2025 | System/implementation hazards, guarantee scope and accounting. Does not supply the toy thresholds |
| R2 | [NIST SP 800-188, De-Identifying Government Datasets: Techniques and Governance](https://csrc.nist.gov/pubs/sp/800/188/final) | Final, September 2023 | Release models, re-identification studies and governance. Its governmental context is retained |
| R3 | [NIST Privacy-Enhancing Cryptography: PSI/PSO](https://csrc.nist.gov/Projects/pec/psi) | Official project reference page, checked 2026-10-26 | Distinguishes set/cardinality/asymmetric output functions and their assumptions; not a certification of an implementation |
| R4 | [ENISA, Data Protection Engineering](https://www.enisa.europa.eu/publications/data-protection-engineering) | Published 27 January 2022 | Selection/configuration of technical and organisational measures |
| R5 | [Carlini et al., Membership Inference Attacks From First Principles](https://arxiv.org/abs/2112.03570) | Author preprint v2, 12 April 2022; IEEE S&P 2022 paper | Membership evaluation at low false-positive rates; assumptions of the attack and evaluation |
| R6 | [Shokri et al., Membership Inference Attacks Against Machine Learning Models](https://www.ieee-security.org/TC/SP2017/papers/313.pdf) | IEEE S&P 2017 original paper | Basic training-membership threat model. No claim that one attack covers all channels |
| R7 | [EDPB Guidelines 02/2026 on Anonymisation](https://www.edpb.europa.eu/documents/guideline/guidelines-022026-on-anonymisation_en) | Version 1, 8 July 2026; official page says public consultation ongoing at check date | Legal-context reading only. Draft guidance is not treated as enacted law or a source of universal attack-score thresholds |
| R8 | [Stadler, Oprisanu and Troncoso, Synthetic Data – Anonymisation Groundhog Day](https://www.usenix.org/conference/usenixsecurity22/presentation/stadler) | USENIX Security 2022 | Empirical limits of assuming synthesis guarantees privacy; not a universal result for all later methods |
| R9 | [Ward, Wang and Cheng, Privacy Auditing Synthetic Data Release through Local Likelihood Attacks](https://arxiv.org/abs/2508.21146) | Author preprint, last revised 8 May 2026 (v2) | Recent reading queue for released-data-only membership attacks. No implementation/result from this paper has been reproduced here |

## Internal method inputs

Internal source IDs IM-01–IM-07 identify provenance retained outside this companion for reviewers with access. They are not citations to a publicly available implementation or evidence that a product has passed testing. The internal mapping records paths, source hashes, repository commits where available, review depth and adaptation decisions.

| Neutral source ID | Methodological contribution used | Treatment |
|---|---|---|
| IM-01 | Canonical attack taxonomy, coverage records and detector controls | Test planning and result-state concepts adapted; original risk aggregation is not adopted |
| IM-02 | Cross-party output, chosen-input and coalition analysis | Generic PSI cards with invented inputs and observations |
| IM-03 | Separation of model, update and protocol-transcript channels | Generic FL card; no customer/system identity or archived measurement is reproduced |
| IM-04 | Comparable adversary contracts, separate member/non-member evaluation and known-positive controls | Evaluation-design requirements adapted; no private attack implementation copied |
| IM-05 | Attack metric interfaces and quasi-identifier/attribute testing | Used to identify test families and reporting needs, without product-capability claims |
| IM-06 | Evidence, conformance, lifecycle and change-control specifications | Evidence template and negative-test scenarios adapted |
| IM-07 | Earlier risk-model overview and attack-to-control analysis | Used for the educational sequence and coverage; numerical claims remain outside this preview |

The public-facing wording uses neutral roles and fully artificial teaching fixtures. Content reuse for internal drafting does not settle rights to public distribution or a public licence. Those decisions remain open.
