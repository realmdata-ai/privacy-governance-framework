"""Counterexamples and limits for legacy probabilistic formulas (research layer, not PGF v1).

Every expected value is derived by hand in the comment next to it (exact fractions on an explicit
finite space); the functions under test are never used to produce their own expected values.
Case IDs RX-nn match docs/05_Legacy_Formula_Review_EN.md.
"""
import sys
import unittest
from fractions import Fraction as F
from math import isclose, log
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import legacy_math as lm  # noqa: E402

HALF = F(1, 2)


class UnionOfEvents(unittest.TestCase):
    def test_rx01_noisy_or_overstates_identical_events(self):
        # Space {a, b}, each 1/2. E1 = E2 = {a}. Truth: P(E1 u E2) = P({a}) = 1/2.
        space = {"a": HALF, "b": HALF}
        self.assertEqual(lm.exact_union(space, [{"a"}, {"a"}]), F(1, 2))
        # Noisy-OR: 1 - (1/2)(1/2) = 3/4  -> overstates by 1/4.
        self.assertEqual(lm.legacy_noisy_or([HALF, HALF]), F(3, 4))

    def test_rx02_noisy_or_understates_disjoint_events(self):
        # E1 = {a}, E2 = {b}, disjoint, each 1/2. Truth: 1. Noisy-OR: 3/4 -> UNDERstates (not conservative).
        space = {"a": HALF, "b": HALF}
        self.assertEqual(lm.exact_union(space, [{"a"}, {"b"}]), F(1))
        self.assertEqual(lm.legacy_noisy_or([HALF, HALF]), F(3, 4))

    def test_rx03_noisy_or_exact_under_independence(self):
        # Two fair independent coins: E1 = first heads, E2 = second heads. Truth: 1 - 1/4 = 3/4.
        space = {(x, y): F(1, 4) for x in "HT" for y in "HT"}
        e1 = {o for o in space if o[0] == "H"}
        e2 = {o for o in space if o[1] == "H"}
        self.assertEqual(lm.exact_union(space, [e1, e2]), F(3, 4))
        self.assertEqual(lm.legacy_noisy_or([HALF, HALF]), F(3, 4))

    def test_rx04_frechet_bounds_contain_truth_in_all_cases(self):
        # Marginals 1/2, 1/2 -> bounds [max = 1/2, min(1, sum) = 1]; truths above: 1/2, 1, 3/4.
        lo, hi = lm.frechet_union_bounds([HALF, HALF])
        self.assertEqual((lo, hi), (F(1, 2), F(1)))
        for truth in (F(1, 2), F(1), F(3, 4)):
            self.assertTrue(lo <= truth <= hi)

    def test_rx05_dependent_chain_coefficient_breaks_probability_axioms(self):
        # p = 0.6, d = 2: 1 - (1 - 1.2) = 1.2 > 1 -> not a probability; d_i has no defined semantics.
        self.assertTrue(isclose(lm.legacy_dependent_chain([0.6], [2.0]), 1.2))

    def test_rx06_series_accumulation_mixes_loss_scale(self):
        # P = 0.3 with L on a 1..5 scale, L = 5: 1 - (1 - 1.5) = 1.5 > 1; result depends on the loss unit.
        self.assertTrue(isclose(lm.legacy_series_accumulation([0.3], [5.0]), 1.5))
        # Same event with L normalised to 1.0: 0.3 -> the 'probability' changes with the loss scale.
        self.assertTrue(isclose(lm.legacy_series_accumulation([0.3], [1.0]), 0.3))

    def test_rx07_chain_rule_vs_product_of_marginals(self):
        # Space {x, y} each 1/2. A = artifact exposed = {x}; B = inference succeeds = {x} (only if exposed).
        space = {"x": HALF, "y": HALF}
        a, b = {"x"}, {"x"}
        joint = lm.prob(space, a & b)                                    # 1/2
        chain = lm.prob(space, a) * lm.cond(space, b, a)                 # 1/2 * 1 = 1/2
        marginals = lm.prob(space, a) * lm.prob(space, b)                # 1/4
        self.assertEqual((joint, chain, marginals), (F(1, 2), F(1, 2), F(1, 4)))


class ExpectedLoss(unittest.TestCase):
    def test_rx08_linearity_holds_without_independence(self):
        # Dependent events E1 = E2 = {a} (P = 1/2), losses 3 and 5. E[3*1E1 + 5*1E2] = (3+5)/2 = 4.
        space = {"a": HALF, "b": HALF}
        lhs = sum(space[o] * (3 * (o == "a") + 5 * (o == "a")) for o in space)
        rhs = 3 * lm.prob(space, {"a"}) + 5 * lm.prob(space, {"a"})
        self.assertEqual(lhs, F(4))
        self.assertEqual(rhs, F(4))

    def test_rx09_double_counting_one_harm(self):
        # One person, one harm of size 10 if identified. Singling-out {a} implies linkage {a} (same event).
        # True expected harm: 10 * 1/2 = 5. Summing per-criterion terms counts it twice: 10/2 + 10/2 = 10.
        space = {"a": HALF, "b": HALF}
        true_harm = sum(space[o] * (10 if o == "a" else 0) for o in space)
        summed = 10 * lm.prob(space, {"a"}) + 10 * lm.prob(space, {"a"})
        self.assertEqual(true_harm, F(5))
        self.assertEqual(summed, F(10))


class BayesianUpdating(unittest.TestCase):
    def test_rx10_duplicated_evidence_double_counts(self):
        # H with prior 1/2; one signal s with P(s|H) = 3/4, P(s|not H) = 1/4 (LR = 3); test 2 repeats test 1.
        # Outcomes (h, s): (1,1) 3/8, (1,0) 1/8, (0,1) 1/8, (0,0) 3/8. Observed: both tests positive = s = 1.
        space = {(1, 1): F(3, 8), (1, 0): F(1, 8), (0, 1): F(1, 8), (0, 0): F(3, 8)}
        h = {o for o in space if o[0] == 1}
        both_positive = {o for o in space if o[1] == 1}
        # Exact: P(H | s) = (3/8) / (3/8 + 1/8) = 3/4.
        self.assertEqual(lm.exact_posterior(space, h, both_positive), F(3, 4))
        # Naive product of LRs: odds 1 * 3 * 3 = 9 -> 9/10 (overconfident).
        self.assertEqual(lm.legacy_lr_product_posterior(HALF, [F(3), F(3)]), F(9, 10))

    def test_rx11_lr_product_exact_under_conditional_independence(self):
        # Two conditionally independent signals, each LR 3 given H / not H (3/4 vs 1/4).
        space = {}
        for hv in (1, 0):
            for s1 in (1, 0):
                for s2 in (1, 0):
                    p1 = F(3, 4) if s1 == hv else F(1, 4)
                    p2 = F(3, 4) if s2 == hv else F(1, 4)
                    space[(hv, s1, s2)] = HALF * p1 * p2
        h = {o for o in space if o[0] == 1}
        obs = {o for o in space if o[1] == 1 and o[2] == 1}
        # Exact: (1/2 * 9/16) / (1/2 * 9/16 + 1/2 * 1/16) = 9/10.
        self.assertEqual(lm.exact_posterior(space, h, obs), F(9, 10))
        self.assertEqual(lm.legacy_lr_product_posterior(HALF, [F(3), F(3)]), F(9, 10))


class DifferentialPrivacy(unittest.TestCase):
    EPS = log(3)  # e^eps = 3

    def test_rx12_advantage_bound_pure_dp_is_tight(self):
        # (e^eps - 1)/(e^eps + 1) = 2/4 = 1/2; randomized response with keep-prob 3/4 attains TPR 3/4, FPR 1/4.
        self.assertTrue(isclose(lm.dp_max_advantage(self.EPS, 0.0), 0.5))
        self.assertTrue(isclose(lm.legacy_dp_advantage(self.EPS, 0.0), 0.5))
        self.assertEqual(F(3, 4) - F(1, 4), F(1, 2))

    def test_rx13_legacy_bound_with_delta_is_valid_but_loose(self):
        # delta = 1/10: exact max (3 - 1 + 0.2)/(3 + 1) = 0.55; legacy 0.5 + 0.1 = 0.6 >= 0.55.
        self.assertTrue(isclose(lm.dp_max_advantage(self.EPS, 0.1), 0.55))
        self.assertTrue(isclose(lm.legacy_dp_advantage(self.EPS, 0.1), 0.6))

    def test_rx14_advantage_is_not_probability_of_harm(self):
        # Prior 1/100 that the target is in the data: posterior <= 3*(1/99) / (1 + 3/99) = 3/102 ~ 0.0294,
        # while the balanced-game advantage is 0.5: Adv is a property of a test game, not P(harm).
        self.assertTrue(isclose(lm.pure_dp_posterior_bound(self.EPS, 0.01), 3 / 102))
        self.assertGreater(lm.dp_max_advantage(self.EPS, 0.0), 10 * lm.pure_dp_posterior_bound(self.EPS, 0.01))

    def test_rx15_parallel_composition_needs_add_remove_adjacency(self):
        # Two strata counts with Laplace scales 1/eps_a, 1/eps_b (eps_a = 0.5, eps_b = 1.0).
        # Add/remove one person: only one count changes -> max(0.5, 1.0) = 1.0.
        self.assertTrue(isclose(lm.max_privacy_loss_two_counts(1, 0, 2.0, 1.0), 0.5))
        self.assertTrue(isclose(lm.max_privacy_loss_two_counts(0, 1, 2.0, 1.0), 1.0))
        # Replace-one adjacency where the stratum label itself changes: both counts move -> 0.5 + 1.0 = 1.5.
        self.assertTrue(isclose(lm.max_privacy_loss_two_counts(1, 1, 2.0, 1.0), 1.5))


class MembershipInference(unittest.TestCase):
    def test_rx16_clipping_hides_inverted_attack(self):
        # Members score 0, non-members score 1 (perfectly separable, inverted): AUC = 0 -> legacy risk 0,
        # but flipping the decision gives a perfect attack (|2*AUC - 1| = 1, Youden 1).
        members, nonmembers = [F(0)] * 4, [F(1)] * 4
        auc = lm.exact_auc(members, nonmembers)
        self.assertEqual(auc, F(0))
        self.assertEqual(lm.legacy_mia_risk_from_auc(auc), F(0))
        self.assertEqual(lm.orientation_invariant_auc_distance(auc), F(1))
        self.assertEqual(lm.max_youden(members, nonmembers), F(1))

    def test_rx17_average_metric_hides_low_fpr_exposure(self):
        # 10 members, 10 non-members. One member scores 10 (certain hit); all others score 0 (ties).
        members = [F(10)] + [F(0)] * 9
        nonmembers = [F(0)] * 10
        # AUC: winning pairs 1*10 = 10, ties 9*10 = 90 -> (10 + 45) / 100 = 11/20; 2AUC - 1 = 1/10.
        auc = lm.exact_auc(members, nonmembers)
        self.assertEqual(auc, F(11, 20))
        self.assertEqual(2 * auc - 1, F(1, 10))
        # At FPR = 0 the attack still identifies 1 of 10 members with certainty (TPR 1/10).
        self.assertEqual(lm.tpr_at_fpr(members, nonmembers, F(0)), F(1, 10))


class KAnonymity(unittest.TestCase):
    def test_rx18_one_over_k_needs_stated_adversary(self):
        # Class of k = 3. No background knowledge: 1/3. Adversary knows 2 other members: 1/1 = 1 > 1/k.
        self.assertEqual(lm.reid_probability(3, 0), F(1, 3))
        self.assertEqual(lm.reid_probability(3, 2), F(1))

    def test_rx19_homogeneity_discloses_attribute_without_reidentification(self):
        # All three class members share the diagnosis -> attribute disclosed with probability 1.
        self.assertEqual(lm.attribute_disclosure(["D", "D", "D"], "D"), F(1))


class InformationMeasures(unittest.TestCase):
    def test_rx20_hartley_bits_assume_uniform_prior(self):
        # 4 states, observation rules out 2 -> Hartley: log2 4 - log2 2 = 1 bit.
        self.assertTrue(isclose(lm.hartley_bits(4, 2), 1.0))
        # Prior (0.97, 0.01, 0.01, 0.01); the observation removes two 0.01 states -> posterior (0.97, 0.01)/0.98.
        before = lm.shannon_bits([0.97, 0.01, 0.01, 0.01])
        after = lm.shannon_bits([0.97 / 0.98, 0.01 / 0.98])
        self.assertLess(before - after, 0.2)   # far less than 1 bit of actual uncertainty reduction


class EvidenceStatus(unittest.TestCase):
    def test_rx21_unmeasured_prior_is_not_an_upper_bound(self):
        # Legacy 'worst case' for a not-measured attack: 0.5 * confidence <= 0.5 for any confidence in [0, 1].
        # The attack may in fact always succeed (p = 1): a sound upper bound must be 1, status UNKNOWN.
        for c in (0.0, 0.5, 1.0):
            self.assertLessEqual(lm.legacy_unmeasured_upper(c), 0.5)
        self.assertEqual(lm.sound_unmeasured_upper(), F(1))
        self.assertLess(lm.legacy_unmeasured_upper(1.0), 1)

    def test_rx22_closed_lifecycle_is_not_conformance(self):
        # A finding CLOSED in the tracker without conformance evidence must not count as an effective control.
        self.assertTrue(lm.legacy_admissible("CLOSED"))
        self.assertFalse(lm.admissible("CLOSED", "NOT_MEASURED"))
        self.assertFalse(lm.admissible("CLOSED", "FAIL"))
        self.assertTrue(lm.admissible("OPEN", "PASS"))
        with self.assertRaises(ValueError):
            lm.admissible("CLOSED", "UNKNOWN_STATUS")


class InputValidation(unittest.TestCase):
    def test_rx23_invalid_spaces_and_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            lm.check_space({"a": F(1, 2)})                       # does not sum to 1
        with self.assertRaises(ValueError):
            lm.prob({"a": F(1)}, {"z"})                          # outcome outside the space
        with self.assertRaises(ValueError):
            lm.legacy_noisy_or([F(3, 2)])                        # not a probability
        with self.assertRaises(ValueError):
            lm.dp_max_advantage(-1.0, 0.0)


class Domains(unittest.TestCase):
    """RX-24..RX-27: documented input domains (early-review item RM-REV05)."""

    def test_rx24_dp_functions_reject_non_finite_and_out_of_domain(self):
        nan, inf = float("nan"), float("inf")
        for eps, delta in ((nan, 0.0), (inf, 0.0), (-0.1, 0.0), (1.0, nan), (1.0, -0.1), (1.0, 1.0)):
            with self.assertRaises(ValueError):
                lm.dp_max_advantage(eps, delta)
            with self.assertRaises(ValueError):
                lm.legacy_dp_advantage(eps, delta)
        for eps, prior in ((nan, 0.5), (1.0, nan), (1.0, -0.01), (1.0, 1.01)):
            with self.assertRaises(ValueError):
                lm.pure_dp_posterior_bound(eps, prior)

    def test_rx25_large_finite_eps_is_stable(self):
        # Limits by hand: as eps grows, (1 - e^-eps + 2 delta e^-eps)/(1 + e^-eps) -> 1; e^-1000 underflows to 0.
        self.assertEqual(lm.dp_max_advantage(1000.0, 0.0), 1.0)
        self.assertEqual(lm.dp_max_advantage(1000.0, 0.5), 1.0)
        # Legacy form tends to 1 + delta: a bound above 1, not a probability.
        self.assertEqual(lm.legacy_dp_advantage(1000.0, 0.25), 1.25)
        self.assertEqual(lm.pure_dp_posterior_bound(1000.0, 0.01), 1.0)
        # eps = 0: no information -> advantage = delta... exact (1 - 1 + 2d)/(1 + 1) = d.
        self.assertTrue(isclose(lm.dp_max_advantage(0.0, 0.2), 0.2))

    def test_rx26_degenerate_priors_are_exact(self):
        # Prior 0: adversary certain the target is absent -> posterior 0. Prior 1 -> posterior 1.
        self.assertEqual(lm.pure_dp_posterior_bound(1.0, 0.0), 0.0)
        self.assertEqual(lm.pure_dp_posterior_bound(1.0, 1.0), 1.0)
        # eps = 0 leaves the prior unchanged: 0.3 / (0.3 + 0.7 * 1) = 0.3.
        self.assertTrue(isclose(lm.pure_dp_posterior_bound(0.0, 0.3), 0.3))
        with self.assertRaises(ValueError):
            lm.legacy_lr_product_posterior(F(0), [F(2)])
        with self.assertRaises(ValueError):
            lm.legacy_lr_product_posterior(F(1), [F(2)])
        with self.assertRaises(ValueError):
            lm.legacy_lr_product_posterior(HALF, [F(0)])

    def test_rx27_other_helpers_reject_invalid_inputs(self):
        cases = [
            (lm.legacy_dependent_chain, ([0.5], [1.0, 2.0])),       # unequal lengths (no silent truncation)
            (lm.legacy_dependent_chain, ([0.5], [-1.0])),
            (lm.legacy_series_accumulation, ([float("nan")], [1.0])),
            (lm.max_privacy_loss_two_counts, (1, 0, 0.0, 1.0)),     # zero Laplace scale
            (lm.max_privacy_loss_two_counts, (1.5, 0, 1.0, 1.0)),   # non-integer count change
            (lm.exact_auc, ([], [F(1)])),
            (lm.max_youden, ([F(1)], [float("nan")])),
            (lm.tpr_at_fpr, ([F(1)], [F(0)], F(3, 2))),
            (lm.legacy_mia_risk_from_auc, (F(3, 2),)),
            (lm.reid_probability, (3, 3)),
            (lm.attribute_disclosure, ([], "D")),
            (lm.hartley_bits, (2, 4)),
            (lm.hartley_bits, (4, 0)),
            (lm.shannon_bits, ([0.5, 0.6],)),
            (lm.legacy_unmeasured_upper, (1.5,)),
            (lm.frechet_union_bounds, ([],)),
            (lm.exact_union, ({"a": F(1)}, [])),
            (lm.cond, ({"a": F(1), "b": F(0)}, {"a"}, {"b"})),     # conditioning on a null event
        ]
        for fn, args in cases:
            with self.subTest(fn=fn.__name__, args=args):
                with self.assertRaises(ValueError):
                    fn(*args)


if __name__ == "__main__":
    unittest.main()
