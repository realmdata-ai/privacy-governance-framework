# Changelog — Privacy Governance Framework (PGF)

All notable changes are recorded here. Versions follow semantic versioning: MAJOR for structural or normative-model changes, MINOR for substantive content changes, PATCH for corrections.

## [1.0.0-rc.1] — 2026-10-26 (release candidate; not yet published)

First public release candidate. Derived from the authors' internal source set **"ver.2"**. That set was never publicly released, and this is **not** a second public version.

### Identity and packaging
- Canonical name **Privacy Governance Framework (PGF)**. The internal name "Privacy Management Framework" is retired.
- Authors: Alexey Neyman and Val Khvatov.
- Canonical master is English **Markdown**: Overview plus 31 components in `PGF/`.
  - New Markdown for Document 24 (built from the two internal HTML process maps).
  - New Markdown for Document 30 (recovered from the internal English DOCX).
- Uniform metadata front matter in every file: document ID, release, status, authors, regulatory reference date, source provenance with SHA-256.
- UK English throughout. Internal "Version 1.0–4.0" labels of the fictional example policies are kept separate from the PGF release version.

### Governance model
- Roles redefined:
  - Controller accountable;
  - Executive Management decides;
  - Governing Body oversees, with reserved consent matters allowed;
  - Executive Privacy Programme Owner runs the programme;
  - Processing Owner decides within delegation;
  - DPO independent (advises, monitors, escalates; never authorises processing or accepts risk);
  - Independent Internal Audit gives assurance.
- Mandatory gates applied consistently: legal compliance gate before any risk decision; DPIA triage with DPO advice on every DPIA; Art. 36 prior consultation for residual high risk; transfer equivalence with suspension.
- Breach handling: every personal data breach recorded. GDPR, DORA and Canadian notification tracks separated.

### Risk methodology (Document 18 and dependants)
- Two tracks: risk to individuals' rights and freedoms with broad harm types; organisational consequences kept separate.
- A PET assessment module with failure gates for de-identified, synthetic and aggregate releases.
- Data states distinguished: pseudonymised, anonymous, synthetic, encrypted, federated.
- No metric or opinion is treated as a legal safe harbour.
- Differential-privacy statements require privacy unit, adjacency, accountant and composition.

### Neutrality and examples
- Vendor products and real third-party providers removed from templates and worked examples. Fictional providers are used instead.
- Worked example (PanEuropean Bank AG, fictional) aligned to a single snapshot at the regulatory reference date.
- Art. 10 (criminal-offence data) severity modifier applied consistently (review finding W4-04). Doc 18 Part B now matches Part A. The anti-fraud matching case (DPIA-PSI-01 / PRR-PSI-01) was re-assessed on 26 October 2026: residual High; Art. 36 prior consultation test met; Chief Risk Officer decision pending; sessions paused. The earlier Medium acceptance is kept as superseded history.

### Standards and international adaptation
- New `STANDARDS_CROSSWALK.md`: NIST Privacy Framework 1.0 at category level; GDPR/EDPB; ENISA; Canada (OPC/OIPC accountability guidance, PIPEDA, Québec).
- International adaptation boxes added to legally regulated templates.
- New `GLOSSARY.md`.

*Detailed per-document changes are in each document's "Document history (PGF)" section and in `RELEASE_READINESS.md`.*
