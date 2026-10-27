# Curation and maintenance

## Scope and authority

Prefer the issuing legislature, court, regulator or standards body. An industry response hosted on a regulator website is **not** the regulator's adopted guidance. Keep a source's legal force separate from the publisher and from its practical relevance.

Distinguish an original legal act, its consolidated text, amendments, commencement and application dates, territorial scope, sector scope and processing role. For guidance distinguish draft, consultation, final, revised, superseded and withdrawn. For NIST and professional standards pin the actual release used.

## Verification

The registry records **what was checked**, not a generic green checkmark:

- `official_page_reviewed`: metadata/status on an official page were inspected; not every provision was reviewed.
- `official_document_reviewed` and selected-section variants: the official document or relevant sections were inspected; still not a full clause-by-clause legal audit.
- `official_indexed_text_and_regulator_crosscheck` and similar variants: official indexed evidence or an official companion record supported the identification/status.
- `access_restricted` / access-limited variants: the official endpoint could not be read adequately by the automated reader. Preserve the source link and flag the limitation; do not claim the consolidated text was reviewed.
- Direct-fetch failure with indexed text is explicitly distinguished from a successful full-text fetch.

A 200 response, redirect, accessibility error, anti-bot screen or unsupported content type says little about legal validity. Do not silently replace an authoritative source with an unsourced blog, and do not mark a source repealed merely because its URL fails.

Before relying on a provision for a release, verify its exact wording, applicable version and status through the official source. Record the date, the reviewed section and the reason for any change. A major error or status change should trigger review of affected PGF documents.

## Update workflow

1. Update `registry.json` first; preserve stable `id` values.
2. Check official title, URL, version/status and scope. Move superseded items to a clearly marked historical state; retain traceability.
3. Update `verification.last_checked` only after a real check, and describe its scope.
4. Use `next_review_due` for manual maintenance: normally 90 days for core records and 30 days for drafts/proposals. Check release-critical sources again at release freeze.
5. Regenerate `CATALOGUE.md` from the registry and check local links, IDs and schema.
6. Review the diff. Explain which PGF documents may need attention. A catalogue update alone does not establish compliance.

No background monitoring, crawler or automatic law-to-risk update is implied by these rules.

## Risk-model and data extensions

Create separate, versioned collections later for risk scenarios, harms, controls, evidence and datasets. Each relation should name a stable source ID, an exact provision if available, relation type, rationale, applicability and evidence quality. Avoid copying a legal obligation into a risk score or treating a guidance recommendation as legislation.

Source IDs are navigation keys, not risk weights. A legal failure cannot be offset by utility or a lower aggregate score. Do not publish unsupported regulatory interpretations merely to fill a mapping table.

## Publication and rights

Only the catalogue, registry, schema and this guide are intended for the source repository. Do not bundle external PDFs, paid standards, legal databases or internal review material. Linking does not grant a licence to external material. Publish source records as of a fixed snapshot and retain a version history through Git.
