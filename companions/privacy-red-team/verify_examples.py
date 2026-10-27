"""Reproduce invented teaching observations only; no external system is accessed."""
from __future__ import annotations
import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def wilson(successes: int, trials: int, z: float = 1.959963984540054):
    if trials <= 0 or not 0 <= successes <= trials:
        raise ValueError("A nonempty valid binomial sample is required")
    p = successes / trials
    den = 1 + z*z/trials
    centre = (p + z*z/(2*trials))/den
    half = z*math.sqrt(p*(1-p)/trials + z*z/(4*trials*trials))/den
    return max(0.0, centre-half), min(1.0, centre+half)

def auc(labels, scores):
    pos = [s for y, s in zip(labels, scores) if y == 1]
    neg = [s for y, s in zip(labels, scores) if y == 0]
    if len(labels) != len(scores) or not pos or not neg:
        raise ValueError("Both classes and aligned observations are required")
    return sum(1 if p > n else 0.5 if p == n else 0 for p in pos for n in neg)/(len(pos)*len(neg))

def criterion_status(result_present, positive_control, threshold_met=True):
    if not result_present or positive_control is not True:
        return "INCOMPLETE"
    return "PASS" if threshold_met else "FAIL"

def close(a, b):
    if not math.isclose(a, b, rel_tol=1e-10, abs_tol=1e-12):
        raise AssertionError(f"Expected {b!r}, observed {a!r}")

def reproduce(f):
    fid, d, expected = f["fixture_id"], f["data"], f["expected_observations"]
    if fid == "WC-01-LINK":
        aux = f["auxiliary_data"]
        rows = [r["row"] for r in d["released_rows"] if r["age"] == aux["target_age"] and r["zone"] == aux["target_zone"]]
        actual = {"matching_rows": rows, "criterion_result": "FAIL" if len(rows) == 1 else "PASS"}
    elif fid == "AIA-01":
        labels = d["sensitive_labels"]
        baseline = max(labels.count(0), labels.count(1))/len(labels)
        assisted = sum(d["attacker_rule"][g] == y for g, y in zip(d["groups"], labels))/len(labels)
        actual = {"majority_accuracy": baseline, "assisted_accuracy": assisted, "gain": assisted-baseline,
                  "criterion_result": "FAIL" if assisted-baseline > d["gain_ceiling"] else "PASS"}
    elif fid == "MIA-01":
        t, fpr = d["tp"]/(d["tp"]+d["fn"]), d["fp"]/(d["fp"]+d["tn"])
        pi = d["deployment_prior"]
        actual = {"tpr": t, "fpr": fpr, "ppv_at_declared_prior": pi*t/(pi*t+(1-pi)*fpr)}
    elif fid == "MIA-POWER-01":
        upper = wilson(d["false_positives"], d["negatives"])[1]
        exceeds = upper > d["claimed_fpr_ceiling"]
        if not d["measurement_valid"]:
            actual = {"wilson_95_upper": upper, "criterion_result": "INCOMPLETE",
                      "confidence_conclusion": "invalid_measurement", "pgf_module_mapping": "G-M5_INCOMPLETE"}
        else:
            actual = {"wilson_95_upper": upper, "criterion_result": "FAIL" if exceeds else "PASS",
                      "confidence_conclusion": "ceiling_not_established" if exceeds else "ceiling_established",
                      "pgf_module_mapping": "G-M1_FAIL" if exceeds else "MEASUREMENT_CRITERION_PASS"}
    elif fid == "SYN-SUBGROUP-01":
        sub = d["exposed_subgroup"]/d["subgroup"]
        actual = {"aggregate_rate": d["exposed"]/d["population"], "subgroup_rate": sub,
                  "criterion_result": "FAIL" if sub > d["subgroup_ceiling"] else "PASS"}
    elif fid == "RECON-01":
        solutions = [(a,b) for a in [0,1] for b in [0,1] if a+b == d["sum"] and a == d["x1"]]
        actual = {"x2": solutions[0][1], "unique_solutions": len(solutions), "criterion_result": "FAIL" if len(solutions) == 1 else "INCOMPLETE"}
    elif fid == "DIFF-01":
        actual = {"target_contribution": d["first_count"]-d["second_count"], "criterion_result": "FAIL"}
    elif fid == "PSI-01":
        c0, c1 = len(set(d["server_set"]) & set(d["query0"])), len(set(d["server_set"]) & set(d["query1"]))
        actual = {"count0": c0, "count1": c1, "target_membership": c1-c0 == 1, "criterion_result": "FAIL",
                  "revised_fixed_ack_equal": b"ack" == b"ack"}
    elif fid == "PSI-META-01":
        actual = {"leaky_lengths": [d["length_rule_base"] + d["length_rule_per_match"]*m for m in d["matches"]],
                  "revised_lengths": [d["revised_fixed_length"]]*len(d["matches"]), "criterion_result": "FAIL"}
    elif fid == "FL-META-01":
        accuracy = sum((length == 16) == bool(y) for y, length in zip(d["labels"], d["transcript_lengths"]))/len(d["labels"])
        actual = {"metadata_label_accuracy": accuracy, "model_score_auc": auc(d["labels"],d["model_scores"]), "criterion_result": "FAIL"}
    elif fid == "LEDGER-01":
        actual = {"charged_epsilon": sum(run["epsilon"] for run in d["runs"] if run["observed"]), "criterion_result": "FAIL_IF_FAILED_RUN_OMITTED"}
    elif fid == "CONTROL-01":
        actual = {"statuses": [criterion_status(c["result_present"],c["positive_control"]) for c in d["cases"]]}
    elif fid == "CHANGE-01":
        added = sorted(set(d["changed"])-set(d["approved"]))
        actual = {"added_fields": added, "reassessment_required": bool(added)}
    else:
        raise ValueError(f"Unknown teaching fixture: {fid}")
    for key, value in expected.items():
        if isinstance(value, float): close(actual[key], value)
        elif actual[key] != value: raise AssertionError(f"{fid}.{key}: {actual[key]!r} != {value!r}")
    return {"fixture_id": fid, "attack_id": f["attack_id"], "observer": f["observer"],
            "output_scope": f["output_scope"], "evidence_status": f["evidence_status"], "observations": actual,
            "expected_observation_check": "MATCH"}

def main():
    raw = (ROOT/"fixtures/examples.json").read_bytes()
    data = json.loads(raw)
    required = {"fixture_id","attack_id","observer","auxiliary_data","output_scope","evidence_status","data","expected_observations"}
    for f in data["fixtures"]:
        missing = required-set(f)
        if missing: raise ValueError(f"Missing fixture fields: {missing}")
    observations = [reproduce(f) for f in data["fixtures"]]
    # Evaluation controls: rejected inputs and preserved failure semantics.
    try: wilson(0,0)
    except ValueError: pass
    else: raise AssertionError("Empty denominator was silently accepted")
    assert criterion_status(False,None) == "INCOMPLETE"
    assert criterion_status(True,False) == "INCOMPLETE"
    assert criterion_status(True,True,False) == "FAIL"
    # Valid confidence-bound failure and missing evidence have distinct PGF mappings.
    power = next(f for f in data["fixtures"] if f["fixture_id"] == "MIA-POWER-01")
    assert reproduce(power)["observations"]["pgf_module_mapping"] == "G-M1_FAIL"
    invalid = json.loads(json.dumps(power))
    invalid["data"]["measurement_valid"] = False
    invalid["expected_observations"] = {"wilson_95_upper": power["expected_observations"]["wilson_95_upper"],
                                        "criterion_result": "INCOMPLETE", "confidence_conclusion": "invalid_measurement",
                                        "pgf_module_mapping": "G-M5_INCOMPLETE"}
    assert reproduce(invalid)["observations"]["pgf_module_mapping"] == "G-M5_INCOMPLETE"
    assert sorted(["time","amount"]) == sorted(["amount","time"])
    print(json.dumps({"companion_version": data["companion_version"],
                      "companion_status": data["companion_status"],
                      "review_date": data["review_date"],
                      "scope":"invented teaching examples only; no product/privacy guarantee",
                      "fixture_sha256":hashlib.sha256(raw).hexdigest(),
                      "fixtures_checked":len(observations), "observations":observations},indent=2))

if __name__ == "__main__": main()
