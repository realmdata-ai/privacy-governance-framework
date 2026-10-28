# Privacy Governance Framework (PGF)

**1.0.0-rc.2 — author-conditioned content freeze, 28 October 2026**
Authors: **Alexey Neyman; Val Khvatov**. Regulatory reference date: **26 October 2026**.

PGF contains an Overview and 31 components in four levels, with reusable **Part A templates** and **Part B worked examples** for a fictional bank. It supports practical business decisions about privacy risk, benefits, controls and accountability.

## Start here

- [Framework Overview](PGF/00_Framework_Overview_EN.md)
- [Risk methodology — Document 18](PGF/18_Privacy_Risk_Assessment_Methodology_EN.md)
- [Risk appetite and business decisions — Document 8](PGF/08_Privacy_Risk_Appetite_Statement_EN.md)
- [PAMOLA implementation example](IMPLEMENTATION_PROFILE.md)
- [Glossary](PGF/GLOSSARY.md) · [Standards crosswalk](PGF/STANDARDS_CROSSWALK.md) · [Official references](references/README.md)

## What changed in rc.2

The configured integrated score maps directly to a risk band and matrix result. An individual metric deviation does not automatically replace that result with High or Near-certain. Observations, uncertainty and DPO dissent remain visible beside the authorised business decision. Legal prerequisites, evidence completeness, valid privacy claims and adopted release conditions remain separate. Templates are tool-neutral; examples name PAMOLA and distinguish illustrative workflows from actual capability evidence.

[Author approval and conditions](AUTHOR_APPROVAL.md) · [Freeze record](FREEZE.md) · [Validation scope/results](release/RC2_VALIDATION.md) · [Remaining publication work](PGF/RELEASE_READINESS.md)

## Reproducibility

`python tools/validate_release.py --quiet` checks structure and cross-references. `python tools/check_rc2.py` checks the rc.2 decision semantics, example arithmetic and integration. These checks do not prove legal compliance, anonymity, product capabilities or empirical calibration.

The separately versioned [companion previews](https://github.com/realmdata-ai/privacy-governance-framework/tree/823303d892ec0cb4e08e6860ca135ef5f15648da/companions) remain tied to rc.1 and are not rc.2 conformance evidence.

## Licence and citation

**CC BY 4.0 for framework text/templates is author-approved.** Final rights-owner attribution and licence issuance are tracked in [LICENCE_PROPOSED.md](LICENCE_PROPOSED.md); no script licence is invented. No DOI exists yet. See [CITATION.cff](CITATION.cff).

PGF is not a law, certification or guarantee of compliance. It is not affiliated with other similarly named frameworks.
