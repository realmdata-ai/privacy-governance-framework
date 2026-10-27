# ADP-05 — Scenario risk record

Source: PGF Document 18 Project 2 / Example 2.1-R and Document 19 DPIA-CS-TRAIN-01.

| Input | S1: disclosure through synthetic output | S2: misuse of source data or parameters |
|---|---|---|
| Likelihood method | PET module; PASS and indicator 0.5369048 | Threat-based L1–L4 |
| Residual likelihood | Medium | 1 + 1 + 0 + 1 = 3, Low |
| Inherent likelihood | This companion does not invent a new pre-PET S1 likelihood; the source DPIA records activity-level inherent Medium | 1 + 1 + 3 + 1 = 6, Medium |
| Severity | Restricted 3 + scale 3 + aggregation 1 = 7 | Same 7 |
| Zero modifiers | Special-category/offence 0; vulnerability 0; internal reach 0; ADM 0 for a disclosure scenario; provenance 0 | Same |
| Severity band | 6.5 ≤ 7 < 8.5, Significant | Significant |
| Residual matrix result | Medium × Significant = Medium | Low × Significant = Medium |
| Inherent result used here | Activity-level inherent Medium is reproduced as stated in the source DPIA, not independently derived from a newly created S1 scenario | Medium × Significant = Medium |

**Activity track (a): Medium residual; Medium inherent**, as recorded by the source. The distinction above preserves what is calculated in this companion and what is inherited from the source. The first generator's as-proposed FAIL is not silently substituted for an inherent result of the accepted configuration.

Severity concerns harm about the real people in the source data; synthesis does not reduce the data class or remove that harm. Utility stays separate.

**Track (b):** applicable regime 1 + financial 1 + reputational 1 = 3, Moderate. The organisational level is reported to ERM and cannot offset track (a), a mandatory gate or a legal duty.

The initial generator's PET-module failure was unavailable for acceptance, even though its attack metrics passed. A weighted indicator never overrides a failed epsilon or configuration gate.
