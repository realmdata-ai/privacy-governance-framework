"""Research extensions (NOT part of PGF v1): exact finite-space checks of probabilistic formulas
found in earlier working materials (legacy review, docs/05_Legacy_Formula_Review_EN.md).

Two kinds of functions:
  * exact_*  -- compute a quantity exactly on an explicit finite probability space (Fractions);
  * legacy_* -- reproduce a legacy shortcut formula *as stated*, so tests can show where it is
               exact, where it is only a bound, and where it fails.
Nothing here is a production risk calculator or a DP mechanism.

Input domains: every function validates its inputs before any arithmetic and raises ValueError
outside its documented domain. No function silently returns NaN, inf or a truncated result.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import product as cartesian
from math import exp, isfinite, log, prod
from typing import Dict, FrozenSet, Hashable, Iterable, Sequence, Tuple

Outcome = Hashable
Space = Dict[Outcome, Fraction]          # outcome -> probability (must sum to 1)
Event = FrozenSet[Outcome]


# ---------------------------------------------------------------- input domains
def _finite(x, name: str):
    if isinstance(x, bool) or not isinstance(x, (int, float, Fraction)) or not isfinite(float(x)):
        raise ValueError(f"{name} must be a finite real number, got {x!r}")
    return x


def _unit(x, name: str, *, open_low: bool = False, open_high: bool = False):
    _finite(x, name)
    if x < 0 or x > 1 or (open_low and x == 0) or (open_high and x == 1):
        lo, hi = "(" if open_low else "[", ")" if open_high else "]"
        raise ValueError(f"{name} must lie in {lo}0, 1{hi}, got {x!r}")
    return x


def _same_length(a: Sequence, b: Sequence, what: str) -> None:
    if not a or len(a) != len(b):
        raise ValueError(f"{what}: inputs must be non-empty and of equal length")


def _check_dp(eps, delta) -> None:
    if _finite(eps, "eps") < 0:
        raise ValueError("eps must be >= 0")
    _unit(delta, "delta", open_high=True)


def _check_scores(members: Sequence, nonmembers: Sequence) -> None:
    if not members or not nonmembers:
        raise ValueError("member and non-member score lists must be non-empty")
    for s in list(members) + list(nonmembers):
        _finite(s, "score")


# ---------------------------------------------------------------- finite probability spaces
def check_space(space: Space) -> None:
    if not space:
        raise ValueError("empty probability space")
    if any((not isinstance(p, Fraction)) or p < 0 for p in space.values()):
        raise ValueError("probabilities must be non-negative Fractions")
    if sum(space.values()) != 1:
        raise ValueError("probabilities must sum to exactly 1")


def prob(space: Space, event: Iterable[Outcome]) -> Fraction:
    check_space(space)
    ev = set(event)
    unknown = ev - set(space)
    if unknown:
        raise ValueError(f"event contains outcomes outside the space: {sorted(map(str, unknown))}")
    return sum((space[o] for o in ev), Fraction(0))


def exact_union(space: Space, events: Sequence[Iterable[Outcome]]) -> Fraction:
    if not events:
        raise ValueError("need at least one event")
    return prob(space, set().union(*map(set, events)))


def cond(space: Space, a: Iterable[Outcome], given: Iterable[Outcome]) -> Fraction:
    pg = prob(space, given)
    if pg == 0:
        raise ValueError("conditioning on a null event")
    return prob(space, set(a) & set(given)) / pg


# ---------------------------------------------------------------- union of events
def legacy_noisy_or(ps: Sequence[Fraction]) -> Fraction:
    """1 - prod(1 - p_i): exact only if the events are mutually independent."""
    if not ps:
        raise ValueError("noisy-OR needs at least one probability")
    for p in ps:
        _unit(p, "noisy-OR input")
    return 1 - prod((1 - p for p in ps), start=Fraction(1))


def frechet_union_bounds(ps: Sequence[Fraction]) -> Tuple[Fraction, Fraction]:
    """Sharp bounds on P(union) when only the marginals are known: [max p_i, min(1, sum p_i)]."""
    if not ps:
        raise ValueError("need at least one marginal")
    for p in ps:
        _unit(p, "marginal")
    return max(ps), min(Fraction(1), sum(ps, Fraction(0)))


def legacy_dependent_chain(ps: Sequence[float], ds: Sequence[float]) -> float:
    """1 - prod(1 - p_i * d_i) with an undefined 'dependency coefficient' d_i (legacy form).
    Domain: p_i in [0, 1]; d_i finite and >= 0 (the legacy material gives no further constraint)."""
    _same_length(ps, ds, "legacy_dependent_chain")
    for p, d in zip(ps, ds):
        _unit(p, "p_i")
        if _finite(d, "d_i") < 0:
            raise ValueError("d_i must be >= 0")
    return 1 - prod(1 - p * d for p, d in zip(ps, ds))


def legacy_series_accumulation(ps: Sequence[float], losses: Sequence[float]) -> float:
    """1 - prod(1 - P_q * L_q): legacy accumulation that mixes a loss scale into a union formula.
    Domain: P_q in [0, 1]; L_q finite and >= 0 on whatever scale the caller uses."""
    _same_length(ps, losses, "legacy_series_accumulation")
    for p, l in zip(ps, losses):
        _unit(p, "P_q")
        if _finite(l, "L_q") < 0:
            raise ValueError("L_q must be >= 0")
    return 1 - prod(1 - p * l for p, l in zip(ps, losses))


# ---------------------------------------------------------------- Bayesian updating
def exact_posterior(space: Space, hypothesis: Iterable[Outcome], observed: Iterable[Outcome]) -> Fraction:
    return cond(space, hypothesis, observed)


def legacy_lr_product_posterior(prior: Fraction, lrs: Sequence[Fraction]) -> Fraction:
    """odds_post = odds_prior * prod(LR_m): exact only under conditional independence of the
    observations given H and given not-H. Domain: prior in (0, 1); each LR finite and > 0."""
    _unit(prior, "prior", open_low=True, open_high=True)
    for lr in lrs:
        if _finite(lr, "likelihood ratio") <= 0:
            raise ValueError("likelihood ratios must be > 0")
    odds = prior / (1 - prior) * prod(lrs, start=Fraction(1))
    return odds / (1 + odds)


# ---------------------------------------------------------------- DP and hypothesis testing
def dp_max_advantage(eps: float, delta: float) -> float:
    """Largest TPR - FPR of any test distinguishing neighbouring datasets under (eps, delta)-DP,
    from the hypothesis-testing region TPR <= e^eps FPR + delta and 1-FPR <= e^eps (1-TPR) + delta
    (Kairouz, Oh and Viswanath 2015): (e^eps - 1 + 2 delta) / (e^eps + 1).
    Domain: eps finite and >= 0; delta in [0, 1). Evaluated in the overflow-free form
    (1 - e^-eps + 2 delta e^-eps) / (1 + e^-eps), so a large finite eps tends to 1 without overflow."""
    _check_dp(eps, delta)
    t = exp(-eps)
    return (1 - t + 2 * delta * t) / (1 + t)


def legacy_dp_advantage(eps: float, delta: float) -> float:
    """Legacy 'Adv <~ (e^eps - 1)/(e^eps + 1) + delta' (valid but looser when delta > 0).
    Same domain as dp_max_advantage; overflow-free form (1 - e^-eps)/(1 + e^-eps) + delta.
    The legacy value can exceed 1 (large eps with delta > 0): it is a bound, not a probability."""
    _check_dp(eps, delta)
    t = exp(-eps)
    return (1 - t) / (1 + t) + delta


def pure_dp_posterior_bound(eps: float, prior: float) -> float:
    """Upper bound on an adversary's posterior belief that the target is in the data, under pure
    eps-DP and prior `prior` (posterior odds <= e^eps * prior odds).
    Domain: eps finite and >= 0; prior in [0, 1]. Degenerate priors are exact: prior 0 -> 0 and
    prior 1 -> 1 (an adversary who is already certain learns nothing). Evaluated as
    prior / (prior + (1 - prior) e^-eps), which cannot overflow or divide by zero for prior > 0."""
    _check_dp(eps, 0.0)
    _unit(prior, "prior")
    if prior == 0:
        return 0.0
    return prior / (prior + (1 - prior) * exp(-eps))


def max_privacy_loss_two_counts(delta_a: int, delta_b: int, scale_a: float, scale_b: float) -> float:
    """Worst-case log density ratio of two independent Laplace-noised counts when neighbouring
    datasets change the counts by delta_a and delta_b: |da|/b_a + |db|/b_b.
    Domain: integer count changes; Laplace scales finite and > 0."""
    for d in (delta_a, delta_b):
        if isinstance(d, bool) or not isinstance(d, int):
            raise ValueError("count changes must be integers")
    for b in (scale_a, scale_b):
        if _finite(b, "Laplace scale") <= 0:
            raise ValueError("Laplace scales must be > 0")
    return abs(delta_a) / scale_a + abs(delta_b) / scale_b


# ---------------------------------------------------------------- MIA metrics
def exact_auc(member_scores: Sequence[Fraction], nonmember_scores: Sequence[Fraction]) -> Fraction:
    """AUC = P(score_member > score_nonmember) + 1/2 P(tie), by full enumeration."""
    _check_scores(member_scores, nonmember_scores)
    wins = Fraction(0)
    for m, n in cartesian(member_scores, nonmember_scores):
        wins += 1 if m > n else Fraction(1, 2) if m == n else 0
    return wins / (len(member_scores) * len(nonmember_scores))


def _thresholds(member_scores, nonmember_scores):
    scores = list(member_scores) + list(nonmember_scores)
    return sorted(set(scores)) + [max(scores) + 1]


def max_youden(member_scores: Sequence[Fraction], nonmember_scores: Sequence[Fraction]) -> Fraction:
    """max over thresholds (both orientations) of |TPR - FPR|."""
    _check_scores(member_scores, nonmember_scores)
    best = Fraction(0)
    for t in _thresholds(member_scores, nonmember_scores):
        tpr = Fraction(sum(s >= t for s in member_scores), len(member_scores))
        fpr = Fraction(sum(s >= t for s in nonmember_scores), len(nonmember_scores))
        best = max(best, abs(tpr - fpr))
    return best


def tpr_at_fpr(member_scores: Sequence[Fraction], nonmember_scores: Sequence[Fraction], fpr_max: Fraction) -> Fraction:
    """Largest TPR over thresholds whose FPR <= fpr_max (score >= t predicts 'member')."""
    _check_scores(member_scores, nonmember_scores)
    _unit(fpr_max, "fpr_max")
    best = Fraction(0)
    for t in _thresholds(member_scores, nonmember_scores):
        fpr = Fraction(sum(s >= t for s in nonmember_scores), len(nonmember_scores))
        if fpr <= fpr_max:
            best = max(best, Fraction(sum(s >= t for s in member_scores), len(member_scores)))
    return best


def legacy_mia_risk_from_auc(auc: Fraction) -> Fraction:
    """max(0, 2 AUC - 1): clips an inverted (AUC < 0.5) but equally informative attack to zero."""
    _unit(auc, "AUC")
    return max(Fraction(0), 2 * auc - 1)


def orientation_invariant_auc_distance(auc: Fraction) -> Fraction:
    _unit(auc, "AUC")
    return abs(2 * auc - 1)


# ---------------------------------------------------------------- k-anonymity
def reid_probability(class_size: int, known_others: int) -> Fraction:
    """Probability of picking the target in its equivalence class when the adversary can exclude
    `known_others` members from background knowledge and guesses uniformly among the rest."""
    for n in (class_size, known_others):
        if isinstance(n, bool) or not isinstance(n, int):
            raise ValueError("class size and known_others must be integers")
    if not 0 <= known_others < class_size:
        raise ValueError("known_others must be in [0, class_size)")
    return Fraction(1, class_size - known_others)


def attribute_disclosure(sensitive_values: Sequence[Hashable], value: Hashable) -> Fraction:
    """Probability that a member of the class has `value`, for an adversary who only knows that
    the target is in the class (homogeneity attack when it is 1)."""
    if not sensitive_values:
        raise ValueError("equivalence class must be non-empty")
    return Fraction(sum(v == value for v in sensitive_values), len(sensitive_values))


# ---------------------------------------------------------------- information measures
def hartley_bits(n_before: int, n_after: int) -> float:
    """Domain: integers with 1 <= n_after <= n_before."""
    for n in (n_before, n_after):
        if isinstance(n, bool) or not isinstance(n, int):
            raise ValueError("state counts must be integers")
    if not 1 <= n_after <= n_before:
        raise ValueError("need 1 <= n_after <= n_before")
    return log(n_before, 2) - log(n_after, 2)


def shannon_bits(ps: Sequence[float]) -> float:
    """Domain: a finite probability vector (non-negative, sums to 1 within 1e-9)."""
    if not ps:
        raise ValueError("empty distribution")
    for p in ps:
        _unit(p, "probability")
    if abs(sum(ps) - 1) > 1e-9:
        raise ValueError("probabilities must sum to 1")
    return -sum(p * log(p, 2) for p in ps if p > 0)


# ---------------------------------------------------------------- evidence status and admissibility
def legacy_unmeasured_upper(confidence: float, prior: float = 0.5) -> float:
    """Legacy 'worst case' for an attack that was not measured: prior * confidence."""
    _unit(confidence, "confidence")
    _unit(prior, "prior")
    return prior * confidence


def sound_unmeasured_upper() -> Fraction:
    """With no measurement and no proven bound, the only sound upper bound on a success
    probability is 1; the honest status is UNKNOWN, recorded separately from the value."""
    return Fraction(1)


def legacy_admissible(lifecycle: str) -> bool:
    """Legacy-style rule: a finding whose lifecycle is CLOSED counts as resolved."""
    return lifecycle == "CLOSED"


def admissible(lifecycle: str, conformance: str) -> bool:
    """A control counts as effective only on conformance evidence; lifecycle alone is not evidence."""
    if conformance not in {"PASS", "FAIL", "NOT_MEASURED"}:
        raise ValueError(f"unknown conformance status {conformance!r}")
    return conformance == "PASS"
