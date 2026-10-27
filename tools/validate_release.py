#!/usr/bin/env python3
"""Validate the PGF Markdown release candidate (standard library only).

Usage:  python tools/validate_release.py [--root PATH] [--strict] [--json OUT]

Checks (each finding is ERROR or WARN):
  completeness      Overview + 31 components with canonical file names
  metadata          front matter keys/values, document_id, authors (order), release, reference date, status
  title             '# PGF-NN — <title>' block present
  forbidden         internal/vendor/legacy strings, Cyrillic, drafting markers (TODO/VERIFY)
  spelling          residual US spellings (WARN)
  links             local Markdown links and #anchors resolve
  xrefs             'Document NN' in 1..31; 'Document NN …, Section X.Y' resolves to a numbered heading in NN
  claims            known-wrong legal/method claims (regex rules with rationale)
  examples          canonical worked-example identifiers are used consistently
  disclosure        Overview has abstract, how-to-cite, competing interests, limitations, references
  readiness         PGF/RELEASE_READINESS.md exists; any 'open' P0 -> release NOT READY
Exit code: 0 = no ERROR, 1 = ERRORs found (or WARNs with --strict).
"""
import argparse, json, re, sys
from pathlib import Path

CANON = {
    "00": "00_Framework_Overview_EN.md",
    "01": "01_Privacy_Policy_EN.md",
    "02": "02_Privacy_Governance_Charter_EN.md",
    "03": "03_Privacy_Interface_Integration_Model_EN.md",
    "04": "04_Privacy_Organisational_Design_Strategy_EN.md",
    "05": "05_Privacy_RACI_Matrix_EN.md",
    "06": "06_Privacy_Role_Competency_Framework_EN.md",
    "07": "07_Regulatory_Applicability_Matrix_EN.md",
    "08": "08_Privacy_Risk_Appetite_Statement_EN.md",
    "09": "09_Privacy_Automation_and_Tooling_Strategy_EN.md",
    "10": "10_Data_Classification_Policy_EN.md",
    "11": "11_Data_Retention_and_Disposal_Policy_EN.md",
    "12": "12_Cross_Border_Data_Transfer_Policy_EN.md",
    "13": "13_Consent_Management_Policy_EN.md",
    "14": "14_Data_Breach_Response_Policy_EN.md",
    "15": "15_Data_Subject_Rights_Policy_EN.md",
    "16": "16_Privacy_by_Design_and_by_Default_Policy_EN.md",
    "17": "17_Vendor_and_Third_Party_Privacy_Risk_Policy_EN.md",
    "18": "18_Privacy_Risk_Assessment_Methodology_EN.md",
    "19": "19_DPIA_Methodology_and_Template_EN.md",
    "20": "20_Transfer_Impact_Assessment_Methodology_EN.md",
    "21": "21_Record_of_Processing_Activities_EN.md",
    "22": "22_Privacy_Risk_Register_EN.md",
    "23": "23_Data_Inventory_and_Data_Flow_Maps_EN.md",
    "24": "24_Privacy_Governance_Process_Map_EN.md",
    "25": "25_Process_Owner_Register_EN.md",
    "26": "26_Operational_Role_and_Staffing_Model_EN.md",
    "27": "27_Privacy_Audit_and_Monitoring_Programme_EN.md",
    "28": "28_Privacy_Metrics_Dashboard_EN.md",
    "29": "29_Policy_Review_Cycle_EN.md",
    "30": "30_Privacy_Awareness_and_Training_Programme_EN.md",
    "31": "31_Governance_Reporting_Template_EN.md",
}
SUPPORT = ["README.md", "CHANGELOG.md", "GLOSSARY.md", "STANDARDS_CROSSWALK.md",
           "SOURCE_MANIFEST.json", "RELEASE_READINESS.md"]
REQ_KEYS = ["title", "document_id", "release_version", "status", "authors",
            "regulatory_reference_date", "licence_proposed", "source_provenance"]
RELEASE, REFDATE = "1.0.0-rc.1", "2026-10-26"
AUTHORS = ["Alexey Neyman", "Val Khvatov"]

# (pattern, flags, message, severity, allowed_in)  allowed_in = set of doc ids where the hit is legitimate
FORBIDDEN = [
    (r"\bPAMOLA\b|\bAYITA\b", 0, "vendor product name (EDITORIAL_RULES §6)", "ERROR", set()),
    (r"\bAnthropic\b|\bClaude\b", 0, "real vendor name (EDITORIAL_RULES §6)", "ERROR", set()),
    (r"Realm Inveo|REALM Data|realm-data", 0, "organisation/product branding in body (§6)", "ERROR", {"00"}),
    (r"Privacy Management Framework", re.I, "legacy name; use Privacy Governance Framework (§1)", "ERROR", set()),
    (r"\bSupervision\b", 0, "calque 'Supervision' (§2)", "ERROR", set()),
    (r"\bcontours?\b", re.I, "calque 'contour' (§2)", "ERROR", set()),
    (r"Privacy\s*[/\-]\s*Risk Committee", 0, "committee spelling (§3)", "ERROR", set()),
    (r"[Ѐ-ӿ]", 0, "Cyrillic characters", "ERROR", set()),
    (r"[«»]", 0, "Russian guillemets", "ERROR", set()),
    (r"\bTODO\b|\bVERIFY\b|\bTBD\b|\bFIXME\b", 0, "drafting marker in canonical text", "ERROR", set()),
    (r"Russian-language|Russian original", re.I, "translation provenance leak", "ERROR", set()),
    (r"Section 4\.X|\bX\.n\b", 0, "placeholder section reference", "ERROR", set()),
    (r"\bEP-20\d\d-\d+", 0, "evidence-pack id must use EVP-YYYY-NNNN (§9)", "WARN", set()),
    (r"Technical Capability Map", 0, "undocumented product artefact (SUP 4.5)", "ERROR", set()),
    (r"fully closes", re.I, "promotional product claim (§6)", "ERROR", set()),
]
US = r"\b(organiz\w*|anonymiz\w*|pseudonymiz\w*|minimiz\w*|authoriz\w*|recogniz\w*|prioritiz\w*|behavior\w*|catalog|catalogs|labeled|labeling|modeling|fulfill|fulfillment|analyz\w*|favor\w*|center|centers|program|programs|defense|offense)\b"
OFFICIAL_US_OK = ["Privacy Management Program", "International Organization for Standardization",
                  "World Health Organization", "Organization for Economic"]

CLAIMS = [
    (r"\beleven\b[^.\n]{0,60}WP\s?248|WP\s?248[^.\n]{0,60}\beleven\b", "WP248 rev.01 has nine criteria"),
    (r"(30|thirty)[- ]day[^.\n]{0,40}(GDPR|Art\.? ?12)|(GDPR|Art\.? ?12\(3\))[^.\n]{0,60}\b30 days\b",
     "GDPR Art. 12(3): one month, extendable by two further months (not '30 days')"),
    (r"BaFin[^.\n]{0,80}(Art(icle|\.)? ?(33|34|36)\b|prior consultation)|(Art(icle|\.)? ?(33|36)\b|prior consultation)[^.\n]{0,80}BaFin",
     "BaFin is not the GDPR supervisory authority for Art. 33/36 (EDITORIAL_RULES §3, §4.4)"),
    (r"pseudonymi[sz]\w*[^.\n]{0,60}(is|as) (an )?anonymi[sz]ation (technique|method)",
     "pseudonymisation is not an anonymisation technique (Art. 4(5), Recital 26)"),
    (r"DPO[^.\n]{0,40}\b(prevails|veto)\b", "DPO does not prevail/veto (EDITORIAL_RULES §4.1)"),
    (r"DPO[^.\n]{0,60}\baccepts?\b[^.\n]{0,30}\b(residual )?risk", "DPO never accepts risk on the controller's behalf (§4.1)"),
    (r"\bno residual (re-?identification )?risk\b", "zero-risk anonymity test is not the legal standard (Recital 26)"),
    (r"Bill C-27[^.\n]{0,80}\b(in force|applies|requires)\b", "Bill C-27 died on prorogation (Jan 2025)"),
    (r"(probability|chance)[^.\n]{0,40}\bδ\b|\bδ\b[^.\n]{0,40}(probability|chance) (that|of) (the )?(guarantee|DP)",
     "δ is not 'the probability the DP guarantee fails' (EDITORIAL_RULES §5.6)"),
    (r"\bunrelated to cross-border\b|does not apply to (cross-border )?transfers?[^.\n]{0,30}Art(icle|\.)? ?36",
     "DPIA/Art. 36 may apply in parallel with a TIA (SUP-13)"),
]
LOGISTIC = re.compile(r"e\^?\s?ε\s?/\s?\(1\s?\+\s?e\^?\s?ε\)|exp\(\s?ε\s?\)\s?/\s?\(1|exp\(epsilon\)", re.I)

def parse_front_matter(text):
    if not text.startswith("---"):
        return None, text
    end = text.find("\n---", 3)
    if end < 0:
        return None, text
    fm, body = text[3:end].strip(), text[end + 4:]
    meta = {}
    for line in fm.splitlines():
        m = re.match(r"^([A-Za-z_]+):\s*(.*?)\s*(#.*)?$", line)
        if m:
            meta[m.group(1)] = m.group(2).strip()
    return meta, body

def slug(h):
    h = re.sub(r"[*_`]", "", h.strip().lower())
    h = re.sub(r"[^\w\- ]", "", h)
    return h.replace(" ", "-")

def headings(body):
    return [m.group(2) for m in re.finditer(r"^(#{1,6})\s+(.+?)\s*#*\s*$", body, re.M)]

def numbered(heads, body=""):
    nums = set()
    # bold pseudo-headings such as '***4.6 Processing Owner***' also count as numbered sections
    for m in re.finditer(r"^[*_]{1,3}(\d+(?:\.\d+)+)\.?\s", body, re.M):
        nums.add(m.group(1))
    for h in heads:
        m = re.match(r"^[*_]*(?:Section\s+|Part\s+[AB][\s—:-]+)?(\d+(?:\.\d+)*)\.?\b", h.strip())
        if m:
            nums.add(m.group(1))
    return nums

class Report:
    def __init__(self): self.items = []
    def add(self, sev, check, where, msg): self.items.append({"severity": sev, "check": check, "file": where, "message": msg})
    def count(self, sev): return sum(1 for i in self.items if i["severity"] == sev)

def lineno(text, pos): return text.count("\n", 0, pos) + 1

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=str(Path(__file__).resolve().parents[1]))
    ap.add_argument("--strict", action="store_true")
    ap.add_argument("--json")
    ap.add_argument("--quiet", action="store_true", help="print summary per check only")
    a = ap.parse_args()
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    root = Path(a.root); pgf = root / "PGF"; R = Report()
    docs = {}
    # completeness
    for nn, name in CANON.items():
        p = pgf / name
        if not p.exists():
            R.add("ERROR", "completeness", name, "missing canonical content file")
        else:
            docs[nn] = p.read_text(encoding="utf-8")
    for s in SUPPORT:
        if not (pgf / s).exists():
            R.add("ERROR", "completeness", s, "missing supporting file")
    extra = [p.name for p in pgf.glob("[0-3][0-9]_*.md") if p.name not in CANON.values()]
    for e in extra:
        R.add("WARN", "completeness", e, "unexpected numbered file in PGF/")

    parsed = {}
    for nn, text in docs.items():
        name = CANON[nn]
        meta, body = parse_front_matter(text)
        parsed[nn] = (meta or {}, body)
        if meta is None:
            R.add("ERROR", "metadata", name, "no front matter"); continue
        for k in REQ_KEYS:
            if k not in meta: R.add("ERROR", "metadata", name, f"missing key '{k}'")
        if nn != "00" and "level" not in meta: R.add("ERROR", "metadata", name, "missing key 'level'")
        if meta.get("document_id") != f"PGF-{nn}": R.add("ERROR", "metadata", name, f"document_id {meta.get('document_id')} != PGF-{nn}")
        if meta.get("release_version") != RELEASE: R.add("ERROR", "metadata", name, "release_version mismatch")
        if meta.get("regulatory_reference_date") != REFDATE: R.add("ERROR", "metadata", name, "regulatory_reference_date mismatch")
        auth = re.findall(r'"([^"]+)"', meta.get("authors", ""))
        if auth != AUTHORS: R.add("ERROR", "metadata", name, f"authors must be {AUTHORS} in this order, got {auth}")
        if meta.get("status") != "release-candidate": R.add("ERROR", "metadata", name, f"status is '{meta.get('status')}', expected release-candidate")
        if not re.search(r"sha256 [0-9a-f]{64}", meta.get("source_provenance", "")) and nn not in ("24",):
            R.add("WARN", "metadata", name, "source_provenance lacks sha256")
        if not re.search(rf"^# PGF-{nn} — \S", body, re.M):
            R.add("ERROR", "title", name, f"title block '# PGF-{nn} — …' not found")
        for need in ["Normative basis", "Document history"]:
            if nn != "00" and not re.search(rf"^#+\s.*{need}", body, re.M | re.I):
                R.add("ERROR", "structure", name, f"section '{need}…' missing")

    # forbidden strings & spelling
    for nn, (meta, body) in parsed.items():
        name = CANON[nn]
        for pat, fl, msg, sev, allowed in FORBIDDEN:
            if nn in allowed: continue
            for m in re.finditer(pat, body, fl):
                R.add(sev, "forbidden", f"{name}:{lineno(body, m.start())}", f"{msg}: '{m.group(0)}'")
        shielded = body
        for s in OFFICIAL_US_OK: shielded = shielded.replace(s, "")
        hits = re.findall(US, shielded)
        if hits:
            R.add("WARN", "spelling", name, f"{len(hits)} US spellings, e.g. {sorted(set(hits))[:6]}")

    # links & anchors
    allfiles = {p.name: p for p in pgf.glob("*.md")}
    anchors = {n: {slug(h) for h in headings(parse_front_matter(t)[1] if parse_front_matter(t)[0] is not None else t)} for n, t in
               ((p.name, p.read_text(encoding="utf-8")) for p in pgf.glob("*.md"))}
    for nn, (meta, body) in parsed.items():
        name = CANON[nn]
        for m in re.finditer(r"\[[^\]]*\]\(([^)\s]+)\)", body):
            target = m.group(1)
            if re.match(r"^(https?:|mailto:)", target): continue
            path, _, anc = target.partition("#")
            fname = Path(path).name if path else name
            if path and not (pgf / path).exists():
                R.add("ERROR", "links", f"{name}:{lineno(body, m.start())}", f"broken local link '{target}'"); continue
            if anc and fname in anchors and anc not in anchors[fname]:
                R.add("ERROR", "links", f"{name}:{lineno(body, m.start())}", f"anchor '#{anc}' not found in {fname}")

    # cross references
    nums = {nn: numbered(headings(body), body) for nn, (meta, body) in parsed.items()}
    xref = re.compile(r"Document\s+(\d{1,2})(?:\s*\([^)]{0,80}\))?(?:,?\s*(?:Section|§)\s*(\d+(?:\.\d+)*))?")
    for nn, (meta, body) in parsed.items():
        name = CANON[nn]
        for m in xref.finditer(body):
            d = int(m.group(1))
            if not 1 <= d <= 31:
                R.add("ERROR", "xrefs", f"{name}:{lineno(body, m.start())}", f"reference to non-existent Document {d}"); continue
            sec = m.group(2)
            tgt = f"{d:02d}"
            if sec and tgt in nums and nums[tgt] and sec not in nums[tgt]:
                R.add("WARN", "xrefs", f"{name}:{lineno(body, m.start())}", f"Document {d} Section {sec} not found among numbered headings")

    # claims
    for nn, (meta, body) in parsed.items():
        name = CANON[nn]
        for pat, why in CLAIMS:
            for m in re.finditer(pat, body, re.I):
                if why.startswith("BaFin") and re.search(r"separate|parallel|DORA|not the|distinct", m.group(0), re.I):
                    continue  # statement that correctly distinguishes the GDPR and financial-supervision channels
                if why.startswith("DPO") and re.search(r"\b(not|never|no|cannot|neither|nor|without)\b", m.group(0), re.I):
                    continue  # negated statement, e.g. 'the DPO does not accept risk' 
                R.add("ERROR", "claims", f"{name}:{lineno(body, m.start())}", f"{why} — '{m.group(0)[:90]}'")
        for m in LOGISTIC.finditer(body):
            ctx = body[max(0, m.start() - 600): m.end() + 600]
            if not re.search(r"hypothesis", ctx, re.I) or not re.search(r"prior", ctx, re.I):
                R.add("ERROR", "claims", f"{name}:{lineno(body, m.start())}",
                      "logistic(ε) bound used without stated hypothesis-test assumptions and priors (§5.6)")

    # worked-example identifiers: each ID should carry one risk tier wherever a tier is stated next to it
    tier_re = re.compile(r"\b((?:DPIA|TIA|PRR)-[A-Z0-9]+(?:-[A-Z0-9]+)*-\d{2})\b[^.\n|]{0,80}?\b(Low|Medium|High|Critical)\b")
    seen = {}
    for nn, (meta, body) in parsed.items():
        for m in tier_re.finditer(body):
            seen.setdefault(m.group(1), set()).add((m.group(2), CANON[nn]))
    for rid, s in seen.items():
        tiers = {t for t, _ in s}
        if len(tiers) > 1:
            R.add("WARN", "examples", rid, f"different tiers stated near this ID: {sorted(s)} — check residual vs inherent wording")

    # disclosure (Overview)
    if "00" in parsed:
        body = parsed["00"][1]
        for need in ["Abstract", "How to cite", "Competing interests", "Limitations", "References", "Quick start", "Document register"]:
            if not re.search(rf"^#+\s.*{need}", body, re.M | re.I):
                R.add("ERROR", "disclosure", CANON["00"], f"Overview section '{need}' missing")

    # readiness
    rr = pgf / "RELEASE_READINESS.md"
    ready = True
    if rr.exists():
        t = rr.read_text(encoding="utf-8")
        open_p0 = re.findall(r"^\|[^|\n]*\bP0\b[^\n]*\|\s*open\s*\|", t, re.M | re.I)
        if open_p0:
            ready = False
            R.add("WARN", "readiness", "RELEASE_READINESS.md", f"{len(open_p0)} P0 items still open")
    else:
        ready = False

    errs, warns = R.count("ERROR"), R.count("WARN")
    by = {}
    for i in R.items: by.setdefault((i["check"], i["severity"]), 0); by[(i["check"], i["severity"])] += 1
    if not a.quiet:
        for i in R.items: print(f"{i['severity']:5} {i['check']:12} {i['file']}: {i['message']}")
    print("\nSUMMARY by check:", ", ".join(f"{c}/{s}={n}" for (c, s), n in sorted(by.items())) or "none")
    print(f"ERROR={errs} WARN={warns} files={len(docs)}/32  MD-RC verdict: "
          + ("PASS" if errs == 0 and ready else "NOT READY"))
    if a.json: Path(a.json).write_text(json.dumps(R.items, indent=1, ensure_ascii=False), encoding="utf-8")
    sys.exit(1 if errs or (a.strict and warns) else 0)

if __name__ == "__main__":
    main()
