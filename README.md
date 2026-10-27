# Privacy Governance Framework (PGF)

**Release 1.0.0-rc.1** (release candidate) · Authors: **Alexey Neyman and Val Khvatov** · Regulatory reference date: **26 October 2026**

PGF is a set of **31 documents organised in four levels**. Each document has two parts:
- **Part A**, a reusable template;
- **Part B**, a worked example for a fictional pan-European bank.

The set comes with a 23-process governance model and is designed to help an organisation build and run a privacy programme:
- policies and governance mandates;
- risk appetite and risk assessment;
- DPIA and transfer impact assessment;
- records and inventories;
- process ownership;
- audit, metrics and board reporting.

> PGF is a **framework of templates and worked examples**. It is not a law, a standard or a certification scheme, and it is not legal advice. Using PGF does not by itself make an organisation compliant with the GDPR or any other law. It is not affiliated with, and should not be confused with, other privacy frameworks that have similar names. Its relationship to the NIST Privacy Framework, ENISA guidance and Canadian accountability guidance is a **conceptual mapping** ([`PGF/STANDARDS_CROSSWALK.md`](PGF/STANDARDS_CROSSWALK.md)).

## Start here

- [`PGF/00_Framework_Overview_EN.md`](PGF/00_Framework_Overview_EN.md) — purpose, architecture, quick start, document register, limitations, how to cite.
- [`PGF/GLOSSARY.md`](PGF/GLOSSARY.md) — roles, gates, data states, incident terms.
- [`PGF/STANDARDS_CROSSWALK.md`](PGF/STANDARDS_CROSSWALK.md) — GDPR/EDPB, NIST PF 1.0, ENISA, Canada.
- [Curated privacy references](references/README.md) — a dated catalogue of official laws, regulations and guidance with stable source IDs ([`references/CATALOGUE.md`](references/CATALOGUE.md), machine-readable [`references/registry.json`](references/registry.json)).

## The four levels

| Level | Documents |
|---|---|
| 1 — Strategic documents | 01 Privacy Policy and Notice · 02 Governance Charter · 03 Interface and Integration Model · 04 Organisational Design Strategy · 05 RACI Matrix · 06 Role Competency Framework · 07 Regulatory Applicability Matrix · 08 Risk Appetite Statement · 09 Automation and Tooling Strategy |
| 2 — Policies and standards | 10 Data Classification · 11 Retention and Disposal · 12 Cross-Border Transfers · 13 Consent · 14 Breach Response · 15 Data Subject Rights · 16 Privacy by Design and by Default · 17 Vendor and Third-Party Risk · 18 Risk Assessment Methodology · 19 DPIA · 20 Transfer Impact Assessment · 21 Records of Processing · 22 Privacy Risk Register · 23 Data Inventory and Flow Maps |
| 3 — Process model | 24 Process Map (23 processes: G1–G9, C1–C5, S1–S9) · 25 Process Owner Register · 26 Operational Role and Staffing Model |
| 4 — Control, reporting and improvement | 27 Audit and Monitoring · 28 Metrics Dashboard · 29 Policy Review Cycle · 30 Awareness and Training · 31 Governance Reporting |

## Repository contents

- `references/` — curated catalogue of primary sources (laws, regulations, guidance), with its JSON registry and schema.
- `PGF/` — the canonical English Markdown: Overview, 31 components, glossary, crosswalk, changelog, source manifest, release-readiness report.
- `tools/validate_release.py` — completeness, metadata, links and cross-reference checks, plus rule-based checks for known incorrect claims.
- `tools/export_publication.py` — builds the clean export from an allowlist.
- `CITATION.cff` — citation metadata (draft until the DOI exists).

## Citation

> Neyman, A., & Khvatov, V. (2026). *Privacy Governance Framework (PGF): A Four-Level Model for Enterprise Privacy Governance* (Version 1.0.0-rc.1). DOI pending.

## Licence

**Proposed:** CC BY 4.0 for the framework text and templates; MIT for the scripts. See `LICENCE_PROPOSED.md`. **No licence is in effect until the rights holders confirm it.**

## Status

This is a release candidate under review. See `PGF/RELEASE_READINESS.md` for the status of each finding and any known open items.
