"""Verify teaching arithmetic and package links; no PET or legal validation.

Python 3.11+, standard library only. No network, private folders or installed packages.
"""
from __future__ import annotations
import argparse
from decimal import Decimal
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import re
import sys

VERSION = "0.1.0-preview.1"
BASE = Path(__file__).resolve().parent
REPO = BASE.parent.parent
SCOPE = "teaching arithmetic and documentation/link checks, not PET validation"
RESULTS: list[dict] = []


def check(name, condition, detail=None, scope="companion"):
    RESULTS.append({"check": name, "passed": bool(condition), "scope": scope, "detail": detail})


def strict_json(path):
    if not path.is_file():
        raise ValueError("Required package input is missing: " + path.name)
    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise ValueError("Duplicate JSON key: " + key)
            result[key] = value
        return result
    def constant(value):
        raise ValueError("Non-finite JSON constant: " + value)
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=pairs,
                      parse_constant=constant)


def contract(value, schema, location="$"):
    # Execute only the documented keywords used by the supplied contracts.
    # Unsupported keywords fail; this is not a complete JSON Schema implementation.
    supported = {"$schema", "title", "description", "type", "required", "properties",
                 "additionalProperties", "items", "minItems", "maxItems", "uniqueItems",
                 "enum", "minLength", "pattern", "minimum", "maximum",
                 "exclusiveMinimum", "exclusiveMaximum"}
    unknown = set(schema) - supported
    if unknown:
        raise ValueError(location + ": unsupported contract keywords " + str(sorted(unknown)))
    kind = schema.get("type")
    number = isinstance(value, (int, float)) and not isinstance(value, bool)
    valid = {"object": isinstance(value, dict), "array": isinstance(value, list),
             "string": isinstance(value, str), "number": number,
             "integer": isinstance(value, int) and not isinstance(value, bool),
             "boolean": isinstance(value, bool)}
    if kind not in valid or not valid[kind]:
        raise ValueError(location + ": wrong or unsupported type")
    if number and not math.isfinite(value):
        raise ValueError(location + ": non-finite number")
    if "enum" in schema and value not in schema["enum"]:
        raise ValueError(location + ": outside enum")
    if isinstance(value, dict):
        if set(schema.get("required", [])) - set(value):
            raise ValueError(location + ": missing required fields")
        props = schema.get("properties", {})
        if schema.get("additionalProperties") is False and set(value) - set(props):
            raise ValueError(location + ": unknown fields")
        for key, item in value.items():
            if key in props:
                contract(item, props[key], location + "." + key)
    if isinstance(value, list):
        if len(value) < schema.get("minItems", 0) or len(value) > schema.get("maxItems", math.inf):
            raise ValueError(location + ": wrong item count")
        if schema.get("uniqueItems") and len({json.dumps(x, sort_keys=True) for x in value}) != len(value):
            raise ValueError(location + ": repeated items")
        for i, item in enumerate(value):
            contract(item, schema["items"], location + "[" + str(i) + "]")
    if isinstance(value, str):
        if len(value) < schema.get("minLength", 0):
            raise ValueError(location + ": string too short")
        if "pattern" in schema and re.search(schema["pattern"], value) is None:
            raise ValueError(location + ": pattern mismatch")
    if number:
        for keyword, bad in {"minimum": lambda x: value < x, "maximum": lambda x: value > x,
                             "exclusiveMinimum": lambda x: value <= x,
                             "exclusiveMaximum": lambda x: value >= x}.items():
            if keyword in schema and bad(schema[keyword]):
                raise ValueError(location + ": outside " + keyword)


def load_record(name, schema_name):
    value = strict_json(BASE / "evidence" / name)
    schema = strict_json(BASE / "schemas" / schema_name)
    contract(value, schema)
    check("input contract: " + name, True)
    return value


def dec(value):
    result = Decimal(str(value))
    if not result.is_finite():
        raise ValueError("A numeric input is not finite")
    return result


def verify():
    data = load_record("CASE_RECORDS.json", "case-records.schema.json")
    baseline = load_record("PGF_CONTENT_BASELINE.json", "pgf-content-baseline.schema.json")
    reference = load_record("PGF_REFERENCE_MATRIX.json", "pgf-reference-matrix.schema.json")
    baseline_paths = [entry["path"] for entry in baseline["files"]]
    check("32 distinct baseline paths", len(baseline_paths) == len(set(baseline_paths)) == 32)
    m = data["metrics"]
    weights = [Fraction(str(x)) for x in data["metric_weights"]]
    terms = [abs(Fraction(str(m["accuracy"])) - Fraction(1, 2)) / Fraction(1, 10),
             abs(Fraction(str(m["auc"])) - Fraction(1, 2)) / Fraction(1, 10),
             Fraction(15, 100) / Fraction(str(m["dcr_p5"])),
             (1 - Fraction(str(m["nndr_median"]))) / Fraction(3, 10)]
    indicator = sum(x * w for x, w in zip(terms, weights))
    expected = data["expected"]
    check("weights sum to one", sum(weights) == 1)
    check("independently derived disclosure indicator",
          abs(float(indicator) - expected["indicator"]) < 1e-12,
          {"fraction": str(indicator), "decimal": float(indicator)})
    check("indicator rounding", round(float(indicator), 3) == 0.537)
    check("indicator routing band", Fraction(1, 2) <= indicator <= 1 and expected["s1_likelihood"] == "Medium")
    severity = 3 + 0 + 0 + 3 + 1 + 0 + 0 + 0
    check("severity component sum", severity == expected["severity_index"])
    check("severity band", Decimal("6.5") <= severity < Decimal("8.5") and expected["severity"] == "Significant")
    check("source misuse residual sum", 1 + 1 + 0 + 1 == 3)
    check("source misuse inherent sum", 1 + 1 + 3 + 1 == 6)
    matrix = reference["matrix"]
    s1 = matrix["Significant"][expected["s1_likelihood"]]
    s2 = matrix["Significant"]["Low"]
    check("snapshot matrix lookup for S1 and S2", s1 == s2 == expected["track_a_residual"])
    check("snapshot inherent S2 matrix lookup", matrix["Significant"]["Medium"] == expected["track_a_inherent"])
    check("separate organisational track", 1 + 1 + 1 == expected["track_b_index"] and expected["track_b_level"] == "Moderate")
    for gate in data["gates"]:
        if ("upper" in gate) == ("lower" in gate):
            raise ValueError("Gate requires exactly one upper or lower bound")
        bound, threshold, op = dec(gate.get("upper", gate.get("lower"))), dec(gate["threshold"]), gate["comparison"]
        result = {"<": bound < threshold, "<=": bound <= threshold,
                  ">": bound > threshold, ">=": bound >= threshold}[op]
        check("given interval gate: " + gate["name"], result,
              {"bound": str(bound), "operator": op, "threshold": str(threshold),
               "input_status": "illustrative interval; not recomputed from raw observations"})
    ledger = data["ledger"]
    epsilon, delta = sum(dec(x) for x in ledger["epsilon_entries"]), sum(dec(x) for x in ledger["delta_entries"])
    check("lifetime epsilon sum", epsilon == dec(ledger["expected_epsilon"]), str(epsilon))
    check("lifetime delta sum", delta == dec(ledger["expected_delta"]), str(delta))
    check("lifetime caps", epsilon <= dec(ledger["epsilon_lifetime_cap"]) and delta <= dec(ledger["delta_lifetime_cap"]))
    check("annual epsilon pacing", epsilon <= dec(ledger["annual_2026_epsilon_cap"]))
    percentage = delta / dec(ledger["delta_lifetime_cap"]) * 100
    check("delta warning percentage", percentage == dec(ledger["expected_delta_utilisation_percent"]) and percentage >= 80, str(percentage))
    proposal = data["hypothetical_change"]
    next_epsilon, next_delta = epsilon + dec(proposal["epsilon"]), delta + dec(proposal["delta"])
    check("proposed epsilon sum", next_epsilon == dec(proposal["expected_total_epsilon"]))
    check("proposed delta sum", next_delta == dec(proposal["expected_total_delta"]))
    check("proposed delta excess", next_delta - dec(ledger["delta_lifetime_cap"]) == dec(proposal["expected_delta_excess"]))
    check("preflight fails delta while epsilon within both caps", next_delta > dec(ledger["delta_lifetime_cap"]) and next_epsilon <= dec(ledger["epsilon_lifetime_cap"]) and next_epsilon <= dec(ledger["annual_2026_epsilon_cap"]))
    check("proposal changes project delta", dec(proposal["delta"]) != Decimal("1e-9") and proposal["also_violates_current_project_delta_configuration"])
    check("no new expenditure from reconstruction or unexecuted proposal", dec(ledger["new_charge_from_reconstruction"]) == 0 and dec(proposal["new_charge"]) == 0 and proposal["status"] == "proposed_not_executed")
    ids = data["evidence_ids"]
    check("eight distinct evidence IDs", len(ids) == len(set(ids)) == 8)
    texts = [(p, p.read_text(encoding="utf-8")) for p in sorted(BASE.rglob("*.md"))]
    for identifier in ids:
        pattern = re.compile(r"^# " + re.escape(identifier) + r"\b", re.M)
        check("filled evidence record: " + identifier, any(pattern.search(text) for p, text in texts if p.parent.name == "evidence"))
    check("reference hash matches frozen baseline", any(x["path"] == reference["source_path"] and x["sha256"] == reference["source_sha256"] for x in baseline["files"]))
    missing, pgf_skipped, inspected = [], [], 0
    pgf_present = (REPO / "PGF").is_dir()
    for path, text in texts:
        for target in re.findall(r"\]\(([^)]+)\)", text):
            part = target.split("#")[0].strip("<>")
            if not part or re.match(r"[a-z]+:", part):
                continue
            inspected += 1
            resolved = (path.parent / part).resolve()
            if resolved.is_relative_to((REPO / "PGF").resolve()) and not pgf_present:
                pgf_skipped.append({"file": path.relative_to(BASE).as_posix(), "target": target})
            elif not resolved.exists():
                missing.append({"file": path.relative_to(BASE).as_posix(), "target": target})
    check("local Markdown links inspected", inspected >= 20, inspected)
    check("required local Markdown link targets exist", not missing, missing)
    pgf_status = "NOT_CHECKED_NOT_PRESENT"
    if pgf_present:
        changed = []
        for entry in baseline["files"]:
            path = REPO / entry["path"]
            if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != entry["sha256"]:
                changed.append(entry["path"])
        check("32 frozen PGF content hashes", len(baseline["files"]) == 32 and not changed, changed, "external_pgf")
        pgf_status = "PASS" if not changed else "FAIL"
        source_lines = (REPO / reference["source_path"]).read_text(encoding="utf-8").splitlines()
        starts = [i for i, line in enumerate(source_lines) if line.startswith("| Severity")]
        if not starts:
            raise ValueError("Referenced PGF matrix cannot be located")
        start = starts[-1]
        columns = [c.strip() for c in source_lines[start].strip("|").split("|")][1:]
        actual = {}
        for line in source_lines[start + 2:start + 6]:
            cells = [c.strip().replace("*", "") for c in line.strip("|").split("|")]
            actual[cells[0]] = dict(zip(columns, cells[1:]))
        check("reference matrix equals adjacent PGF source", actual == matrix, scope="external_pgf")
    return pgf_status, pgf_skipped


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--require-pgf", action="store_true", help="Fail if the adjacent PGF content is unavailable")
    parser.add_argument("--report", default="reports/verification_report.json", help="Report path relative to this package")
    args = parser.parse_args()
    report_path = BASE / args.report
    if Path(args.report).is_absolute() or not report_path.resolve().is_relative_to(BASE):
        parser.error("report must stay inside this package")
    pgf_status, skipped = "NOT_CHECKED", []
    try:
        pgf_status, skipped = verify()
        if args.require_pgf:
            check("adjacent PGF required", pgf_status != "NOT_CHECKED_NOT_PRESENT", scope="external_pgf")
    except (ValueError, KeyError, TypeError, OSError, ZeroDivisionError, ArithmeticError) as error:
        check("required input or verification error", False, type(error).__name__ + ": " + str(error))
    failures = sum(not x["passed"] for x in RESULTS)
    status = "FAIL" if failures else ("PASS" if pgf_status == "PASS" else "PASS_COMPANION_ONLY_PGF_NOT_CHECKED")
    report = {"package_version": VERSION, "status": status, "scope": SCOPE,
              "checks": len(RESULTS), "failures": failures,
              "external_pgf_status": pgf_status, "external_pgf_links_not_checked": skipped,
              "limitations": ["No attack, DP mechanism, accountant or statistical experiment is run.",
                              "Given intervals and legal/decision records remain illustrative.",
                              "Contract validator implements only keywords used by the supplied schemas."],
              "results": RESULTS}
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in report.items() if k not in {"results", "limitations", "external_pgf_links_not_checked"}}, indent=2))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
