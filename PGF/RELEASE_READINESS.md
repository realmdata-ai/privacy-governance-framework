---
title: "PGF 1.0.0-rc.1 — Release Readiness"
document_id: PGF-READINESS
release_version: 1.0.0-rc.1
status: release-candidate
authors: ["Alexey Neyman", "Val Khvatov"]
regulatory_reference_date: 2026-10-26
---

# PGF 1.0.0-rc.1 — Release Readiness

**Purpose.** This report gives a disposition for every P0/P1 finding from the first internal audit (C1–C8, H1–H13) and the second internal review (SUP-01…18), and for the findings the reviewer raised during release preparation (B1-…, W2-…, W3-…, W4-…).

**Statuses:**
- **resolved** — corrected in the canonical text, with evidence.
- **partially resolved** — corrected within the stated scope; the remainder is listed under Known limitations.
- **open** — not corrected.

A finding is not resolved by a mass replacement of role labels.

**Review status** records the reviewer's position:
- **accepted** — the block was accepted on the current findings;
- **confirmed** — the specific correction was checked;
- **pending** — awaiting final cross-document review.

Neither status is external peer review or certification.

**Overall verdict — content (Markdown release candidate):** READY FOR REVIEW. All 32 content files are complete, and `tools/validate_release.py` passes. No P0 is open. Final cross-document acceptance by the reviewer is pending.

**Overall verdict — external publication:** gated by the rights and consent items in Section 4, and by the reviewer's final acceptance.

## 1. Content findings

| ID | Priority | Finding | Documents | Status | Evidence | Review status |
|---|---|---|---|---|---|---|
| C1 / SUP-01 | P0 | DPO acting as decision-maker | 02–06, 08, 10–17, 19–20, 22–31 | resolved | Role model in Doc 02 §8 and Doc 05: DPO R/A only for own statutory tasks, C* on every DPIA, no veto, no risk acceptance; Art. 38(5) confidentiality; DPO reports to the Management Board (Docs 02, 04, 26). Rows re-assigned by decision type, not relabelled | accepted (02/04/05/06/08); others confirmed or pending |
| C2 / SUP-02 / SUP-09 | P0 | Art. 36 triggered wrongly; residual high risk accepted internally | 02, 05, 08, 18, 19, 22, 24, 31 | resolved | G-36 is a statutory test evaluated for every DPIA; consultation whenever the test is met; an elapsed period is not an authorisation (EDITORIAL_RULES §4.2; Doc 18 §2.1; Doc 19 step 4.7; Doc 24 C2). CS case: consultation pending, not in production | accepted (08/18/19/22) |
| C3 / SUP-04 | P0 | Breach qualification relied on a harm predicate | 14, 24, 28 | resolved | Doc 14: Art. 4(12) breach without a harm threshold; every breach recorded (Art. 33(5)); separate SA and data-subject decisions; processor path; DORA track. Doc 28 M-S7-04 denominator includes unsent due notifications (W4-01) | confirmed (14 P0 scan; 28 W4-01) |
| C4 / SUP-11 | P0 | Pseudonymisation treated as anonymisation; anonymity by threshold; health data in an open release | 18, 10, 11, 16, 23 | resolved | Doc 18: data states; no metric is a safe harbour; Recital 26; C-413/23 P with stated limits; G-M3 grounds; Ex 3.3 blocked on stated facts (B1-05) | accepted (18) |
| C5 / SUP-12 / SUP-13 | P0 | TIA without a laws-and-practices assessment; appetite substituting for equivalence | 20, 12, 05, 24 | resolved | Doc 20 legal module; branches by mechanism (Art. 45/46/49); suspension under Clause 14(f); no "unrelated to cross-border"; dated US snapshot; LLM case on G-TIA HOLD; PSI with no output to the partner | accepted (20) |
| C6 / SUP-05 | P0 | DPO advice skipped for Low-risk DPIAs | 19, 08 | resolved | DPO advice on every DPIA (Art. 35(2)), with the decider's response recorded (Doc 19) | accepted (19) |
| C7 / SUP-07 | P0 | Supervisory Board making management decisions | all Part B | resolved | Management Board decides; Supervisory Board oversees; exactly three reserved consent matters (Charter, board-level appetite, DPO removal); Audit Committee approves the audit plan (B1-08) | accepted (02/05) |
| C8 / SUP-14 | P0 | Vendor neutrality: product claims and real vendors | Overview, 04, 06, 08, 09, 12, 16–23, 26, 27 | resolved | No product names or capability claims in Part A or Part B (validator `forbidden`); fictional providers; Doc 09 tool-neutral, and expert opinion cannot replace a missing result (W3-04); competing-interests statement (Overview §10) | confirmed (09) |
| SUP-03 | P0 | Risk reduced to re-identification | 08, 18, 19, 20 | resolved | Doc 18 two tracks: seven harm types; threat-based likelihood; PET module as a specialised module only | accepted (18) |
| SUP-08 / H1 | P0 | BaFin used as GDPR authority; GDPR and DORA clocks mixed | 03, 04, 07, 14, 17, 24–26 | resolved | Lead SA HBDI for GDPR; BaFin/ECB for DORA only; DORA clocks with points of reference and the late-classification branch (Docs 07, 14) | confirmed |
| SUP-10 | P1 | Calibration Catastrophic × Low = Medium | 08 | resolved | Severity-led matrix (Catastrophic × Low = High) | accepted |
| SUP-15 | P1 | "Eleven" WP248 criteria | 19 | resolved | Nine WP248 criteria plus labelled internal triggers | accepted |
| SUP-16 / H10 | P1 | Blanket retention; legal hold; AML row | 11, 01, 07 | resolved | Category/trigger matrix; GwG §8(4) year-end trigger separate from AMLR Art. 77 (W2-05); scoped legal hold; erasure cascade and off-cycle expiry (W3-02/03) | confirmed |
| SUP-17 / H5–H7 | P1 | Notice content; rights restrictions; Art. 28(3)/Art. 26 | 01, 15, 17 | resolved | 01A/01B with full Arts. 13/14 content; Doc 15 with CJEU case law and restrictions; Doc 17 with the full Art. 28(3) list and Art. 26 | confirmed (01, 15, 17 limited) |
| SUP-18 | P1 | Versions, terminology and metrics hiding missed statutory deadlines | all; 27–31 | resolved | Single release metadata; glossary; Doc 28 definition standard (no tolerance for statutory deadlines; Little's law with the mean, W4-02); Doc 31 chronology (W4-03) | confirmed (28) |
| H2 / H3 | P1 | Likelihood model; PET metric semantics | 18, 09 | resolved | Threat-based likelihood; orientation-invariant gates and confidence intervals (B1-03); DP ledger in ε and δ without calendar reset (B1-04); logistic(ε) only under stated assumptions | accepted |
| H4 | P1 | Doc 07: one-stop-shop, Art. 3, DORA scope, AI Omnibus, missing regimes | 07 | resolved | Art. 3(1); lead/concerned SAs; DORA bank-wide; AI Omnibus dates; CCD2, AMLR, Data Act; pending-changes block; Canada map | confirmed (W2-05/06) |
| H8 | P1 | Process-map logic (C2, C3, C4, S7); missing processes | 24 | resolved | Corrected flows; sub-processes G4.1, G4.2, G5.1, C2.1, C2.2, C2.3, S6.3 with RACI rows (Doc 05) and owners (Doc 25) | pending (full review) |
| H9 | P1 | AI Act deployer duties / FRIA | 03, 07, 19, 24 | resolved | AI-governance interface (Doc 03 §3.5); FRIA link (Doc 19); C2.1 | confirmed |
| H11 / H12 | P1 | Level 4 metrics and escalation; management-body training; DPO safeguards | 27–31 | resolved | Three assurance loops (Doc 27); master escalation matrix (Doc 31 §6.4); management-body, AI-literacy and contractor training (Doc 30); DPO safeguards (Docs 26, 30) | pending (full review) |
| H13 | P1 | Normative basis; crosswalk | all | resolved | "Normative basis and references" section in every component; `STANDARDS_CROSSWALK.md`; curated `references/` catalogue 0.2.0 | confirmed |
| INT-CA | P1 | Canada: applicability, PIPEDA/Québec, OPC programme mapping | 01, 07, 13–15, 19, 20, crosswalk | partially resolved | Applicability map (Doc 07); international adaptation boxes; OPC/OIPC mapping (Doc 02; crosswalk §4). Programme-level guidance only, by design | confirmed (scope) |
| DPF | P1 | DPF registry evidence; Swiss and UK routes | 07, 12, 17, 20 | resolved | DPF List check record (Doc 12 §4.1); Swiss-U.S. DPF and UK Extension as separate routes | confirmed |

## 2. Packaging findings

| ID | Priority | Finding | Status | Evidence |
|---|---|---|---|---|
| PK-1 | P1 | No English Markdown for Doc 30 | resolved | `PGF/30_Privacy_Awareness_and_Training_Programme_EN.md` |
| PK-2 | P1 | Doc 24 had no Markdown | resolved | `PGF/24_Privacy_Governance_Process_Map_EN.md` (Part A and Part B; all 23 processes in both parts — validator `completeness`) |
| PK-3 | P1 | Name collision | resolved | Canonical name PGF; validator `forbidden` |
| PK-4 | P1 | Authors, release metadata, provenance | resolved | Front matter in all files; `SOURCE_MANIFEST.json` (source → output + SHA-256) |
| PK-5 | P1 | Licence, citation, COI | partially resolved | `LICENCE_PROPOSED.md`, `CITATION.cff` draft, Overview §10; the final licence depends on rights confirmation (Section 4) |

## 3. Checks (run on 27 October 2026, America/Toronto)

| Check | Command | Result |
|---|---|---|
| Validator — completeness, metadata, structure, forbidden strings, spelling, links and anchors, cross-references, claim rules, example tiers, disclosure, readiness | `python tools/validate_release.py` | see the latest run in the handoff message |
| Source manifest | `python tools/export_publication.py --source-manifest` | 33 records (32 files; Doc 24 has two HTML sources) |
| Export | `python tools/export_publication.py --out <dir>` | see the handoff message |
| Integration of cross-document requests | internal integration log (not published) | 127 requests: applied 42, already satisfied 60, out of scope 22, deferred 2, not applied with reason 1 |
| Numerical examples | independent recalculation by the reviewer | Doc 18 (8 tables, 47 rows, 7 boundary cases), Docs 19/20/22 (8 scenarios); 0 arithmetic errors |

## 4. External publication gate (not a content gate)

| Gate | Status |
|---|---|
| H1 — consent of co-author Alexey Neyman (direction of changes, author order, platforms, licence, COI text; final approval of the exact release) | requested — not yet received |
| H2 — copyright holder of the internal source set "ver.2" | open |
| H3 — ORCID / affiliations | optional |
| Overview PDF, final LICENSE, DOI insertion, tag v1.0.0 | after H1/H2 (`publication/RELEASE_RUNBOOK.md`) |

## 5. Known limitations and deferred items (disclosed, not hidden)

- The Doc 18 methodology has not been empirically validated. Thresholds, caps (ε/δ) and the minimum cell size are illustrative internal settings.
- US law after the lapse of FISA s.702 (12 June 2026) has not been verified against primary sources. The worked LLM transfer is therefore on G-TIA HOLD.
- Deferred to 1.0.1:
  - Art. 10 data as a Factor B input in Doc 18 — adding it would require recalculating DPIA-PSI-01;
  - the AI Act Art. 86 application date in Doc 07 — not stated until verified.
- Not stated because unsourced: some national DPIA-list contents; routing of DORA reports between the ECB and BaFin; the retention period for the Québec incident register; Swiss and CASL numeric deadlines.
- No external peer review has been carried out.
