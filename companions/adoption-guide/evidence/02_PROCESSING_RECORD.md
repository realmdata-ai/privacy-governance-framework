# ADP-02 — Processing and data-flow record

Source records: RoPA-CS-002; DI-CS-0873 source extract; DI-CS-0874 synthetic calibration dataset. Teaching reconstruction as at 26 October 2026.

| Field | Filled value |
|---|---|
| Processing Owner | Head of Credit Decisions (business responsibility) |
| Purpose | Calibration and validation of the credit-scoring model |
| People/data | Approximately1.2 million applicants/customers; derived financial indicators, payment history and bureau information |
| Legal record | Legal & Compliance G-L of16 March 2026, referenced rather than invented in the register |
| Data class/state | Restricted/personal data for source and synthetic artefact; no Art. 9/10 data in this defined source; no anonymity conclusion |
| Origin/lineage | Customer records and credit-bureau information → controlled extract → generator → synthetic artefact |
| Internal access | Named Privacy Engineers to source/parameters; Data Science to authorised synthetic artefact only |
| External recipients/transfer | None for this activity; EEA-only scope. No TIA for this defined flow. A newly available third-country recipient would reopen transfer triage |
| ADM boundary | Calibration stage takes no decision about individuals; production automated scoring has its own record and DPIA |
| Retention | Synthetic dataset: model version's operational life+2 years; extracts:30 days after validation; parameters:until dataset retirement — illustrative internal settings subject to applicable duties |
| Decision link | DPIA-CS-TRAIN-01, 25 March 2026, accepted Medium with conditions; expiry 25 March 2027 or next calibration |
| Record status | Active existing processing under the conditions; no new run authorised by this companion |

The RoPA describes the processing; the inventory describes real assets/access/lineage. Neither is a substitute for the other. This filled teaching record is not a claim of full Art. 30 compliance by any real organisation.
