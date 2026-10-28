# PAMOLA implementation profile

This named worked implementation restores the practical purpose of Part B: show how an organisation uses a tool to obtain calculations and compile documents. It is not a prerequisite for adopting PGF. The fictional Bank's implementation profile includes PAMOLA and any separately integrated systems; a workflow requirement is not a claim that a single product already implements it.

## One project, one traceable hand-off

| Stage | Input and output | Tool / human boundary |
|---|---|---|
| Project passport | Purpose, population, protected unit, adversary, output channel, metrics, thresholds and configuration version | Specialists define the context; the tool records and checks supplied values |
| Calculation | Metric values, normalisation, configured weighted indicator, severity-factor arithmetic and matrix lookup | The implementation computes configured arithmetic; contextual judgements are supplied and reviewed by people |
| DP, where claimed | Mechanism, adjacency, contribution bounds, accountant, per-run and composed epsilon/delta | A valid implementation and its supporting evidence are needed; a number in a form is insufficient |
| Evidence pack | Configuration, inputs or controlled references, outputs, run identity, uncertainty and known limitations | Link each output to its run; review what was measured and what was assumed |
| DPIA / TIA | Calculation evidence feeds the assessment record | Legal positions, necessity, proportionality and consultation conclusions are human assessments |
| Business decision | Benefits, consequences for individuals and the organisation, alternatives and conditions | The authorised business role decides under Document 8; a tool output is not the decision |

## Evidence labels

- **Measured:** provide the actual product/build version, run ID/date, configuration, protected input reference, output artefact, test procedure and reviewer. Do not use this label without the artefacts.
- **Illustrative:** a worked numerical assumption or fictional deployment record. The current PGF examples use this label; the package contains no real PAMOLA measurement run.
- **Specified:** a required or intended workflow/capability, pending implementation evidence.
- **Implemented / tested / deployed:** use only to the extent demonstrated by a versioned capability record; those stages are distinct.
- **Not verified / unavailable:** explicitly record the limitation. Whether it blocks a case depends on the adopted methodology, not on product branding.

In rc.2 the configured integrated indicator maps directly to the likelihood band; individual observations and DPO dissent accompany the business decision without automatic tier overrides. Selected weighted inputs must be valid and complete. Legal and adopted release conditions remain separate. No claim of product certification, anonymity, legal compliance or empirical calibration is made by this profile.
