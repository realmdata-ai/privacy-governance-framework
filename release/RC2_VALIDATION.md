# PGF rc.2 — targeted validation

**28 October 2026.** Structural checker: **32/32, zero errors, zero warnings**. Targeted rc.2 suite: **174 passed, zero failed**. See [machine-readable results](RC2_VALIDATION.json).

## Scope

- Direct indicator calibration boundaries, invalid/missing-input handling and a counterexample with one large threshold deviation but a Low integrated score.
- Independently recomputed weighted arithmetic from the Markdown input values and configured weights for Examples 2.1, 2.1-R, 2.2, 3.1, 3.2 and 3.3. Tolerance accommodates displayed weight/rounding precision.
- Direct risk-band wording, DPO dissent, business decision record, separate G-L blocking and selected DPIA/risk-register integration.
- No active retired automatic G-M failure-to-tier algorithm or threat-control minimum-band override; historical rc.1 change rows are explicitly historical.
- Tool-neutral templates, complete component metadata, local links/section references and source-manifest output hashes.
- Three negative controls rejected: product requirement injected before Part B; retired forced-tier algorithm; broken local link. Original files restored after each control.

## Limits

These checks are structural integration and selected example arithmetic, not empirical calibration, legal review, product testing or a complete mathematical proof. The examples and reported confidence intervals remain illustrative. Existing rc.1 companion tests are not counted as rc.2 validation. The wider mathematical validation pack remains a separate research resource.

The author-approved content freeze does not establish the identity of an unconfirmed rights holder, issue a script licence, create the publication PDF or register a DOI. See [remaining publication steps](../PGF/RELEASE_READINESS.md).
