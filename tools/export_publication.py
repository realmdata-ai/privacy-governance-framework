#!/usr/bin/env python3
"""Build a clean publication export of PGF from an explicit allowlist (standard library only).

Usage:
  python tools/export_publication.py                 # dry run: list what would be exported, run checks
  python tools/export_publication.py --out DIR       # write export to DIR (must not exist or be empty)
  python tools/export_publication.py --source-manifest   # (re)write PGF/SOURCE_MANIFEST.json

Default --out target is _INTERNAL/export/privacy-governance-framework (local, git-ignored).
Nothing is uploaded, pushed or published by this script.
"""
import argparse, fnmatch, hashlib, json, re, shutil, sys
from pathlib import Path

W = Path(__file__).resolve().parents[1]
ALLOWLIST = W / "publication" / "ALLOWLIST.txt"
DENY_PATH = [  # never exported, whatever the allowlist says
    "_INTERNAL/*", "_SUP_2026-10/*", "Privacy Governance Framework ver.2/*", "*/_AUDIT_2026-10/*",
    "*/_BUS_PGF/*", "CC_STATUS.md", "PGF/EDITORIAL_RULES.md", "DGF/*", "*G4A*", "*.docx", "*.pdf",
    "*.zip", "*.pyc", "*__pycache__*", ".git/*", "_REPO/*",
]
DENY_CONTENT = [  # strings that must not appear in exported text
    (r"_INTERNAL/|_INTERNAL\\", "internal workspace path"),
    (r"_SUP_2026|_AUDIT_2026|_BUS_PGF", "internal coordination folder"),
    (r"Box/WALKVBOX|C:[/\\]Users[/\\]", "local machine path"),
    (r"\bPAMOLA\b|\bAYITA\b", "vendor product name"),
    (r"\bG4A\b|REDTEAM", "internal red-team module"),
    (r"\bAsana\b|\bSRS-\d", "internal project artefact"),
]
TEXT_EXT = {".md", ".txt", ".json", ".cff", ".py", ".yml", ".yaml", ".html", ".css", ".csv"}

def sha256(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def read_allowlist():
    rules = []
    for line in ALLOWLIST.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"): continue
        src, _, dst = (s.strip() for s in line.partition("->"))
        rules.append((src, dst or None))
    return rules

def denied(rel):
    return any(fnmatch.fnmatch(rel, pat) for pat in DENY_PATH)

def plan():
    items, problems = [], []
    for src, dst in read_allowlist():
        matches = sorted(W.glob(src))
        if not matches: problems.append(f"allowlist entry matches nothing: {src}")
        for p in matches:
            if not p.is_file(): continue
            rel = p.relative_to(W).as_posix()
            if denied(rel):
                problems.append(f"DENIED by policy (allowlist conflict): {rel}"); continue
            target = dst if (dst and not dst.endswith("/")) else ((dst or "") + (rel if not dst else p.name))
            items.append((p, target))
    return items, problems

def scan(items):
    problems = []
    for p, target in items:
        if p.suffix.lower() not in TEXT_EXT: continue
        if target.startswith("tools/") or target == "publication/ALLOWLIST.txt":
            continue  # these files define the deny rules themselves and necessarily contain the patterns
        t = p.read_text(encoding="utf-8", errors="replace")
        for pat, why in DENY_CONTENT:
            for m in re.finditer(pat, t):
                problems.append(f"{target}: {why}: '{m.group(0)}'"); break
    return problems

def source_manifest():
    base = json.loads((W / "_INTERNAL/cc_work/baseline/baseline_manifest.json").read_text(encoding="utf-8"))
    out = []
    pgf = W / "PGF"
    for e in base:
        doc = e["doc"]
        cands = sorted(pgf.glob(f"{doc}_*_EN.md"))
        rec = {"document_id": f"PGF-{doc}", "source_path": f"Privacy Governance Framework ver.2/{e['source']}",
               "source_sha256": e["sha256"]}
        if cands:
            rec.update({"output_path": f"PGF/{cands[0].name}", "output_sha256": sha256(cands[0])})
        out.append(rec)
    (pgf / "SOURCE_MANIFEST.json").write_text(json.dumps({
        "release_version": "1.0.0-rc.1",
        "note": "Maps each canonical PGF Markdown file to the internal ver.2 source it was derived from. "
                "Source paths refer to the authors' local source set and are provided for provenance only.",
        "records": out}, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"wrote PGF/SOURCE_MANIFEST.json ({len(out)} records)")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out")
    ap.add_argument("--source-manifest", action="store_true")
    a = ap.parse_args()
    if hasattr(sys.stdout, "reconfigure"): sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if a.source_manifest:
        source_manifest(); return
    items, problems = plan()
    problems += scan(items)
    print(f"{len(items)} files in export plan")
    for p, t in items: print(f"  {t}")
    if problems:
        print("\nPROBLEMS:"); [print("  " + x) for x in problems]
    if not a.out:
        print("\nDry run only (use --out DIR to write)."); sys.exit(1 if problems else 0)
    if problems:
        sys.exit("Refusing to write export while problems exist.")
    out = Path(a.out).resolve()
    if out.exists() and any(out.iterdir()): sys.exit(f"{out} is not empty")
    for p, t in items:
        d = out / t; d.parent.mkdir(parents=True, exist_ok=True); shutil.copy2(p, d)
    lines = [f"{sha256(f)}  {f.relative_to(out).as_posix()}" for f in sorted(out.rglob("*")) if f.is_file()]
    (out / "MANIFEST.sha256").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"\nExport written to {out} ({len(lines)} files + MANIFEST.sha256)")

if __name__ == "__main__":
    main()
