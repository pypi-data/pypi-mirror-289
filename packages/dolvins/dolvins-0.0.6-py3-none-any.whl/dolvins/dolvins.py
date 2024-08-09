import math
import numpy as np
import mpmath as mp
import pandas as pd
from tqdm import tqdm
from functools import reduce
from mpmath import mp, sqrt, pi, exp


# GENERAL MATH ----------------------------------------------


def next_power_of_two(x: int) -> int:
    """returns the next power of two greater than or equal to x"""
    return 1 << (x - 1).bit_length()


def gcd_of_list(numbers: list) -> int:
    """returns the gcd of a list of numbers"""
    return int(reduce(math.gcd, numbers))


def previous_power_of_two(x: int) -> int:
    """rounds down x to the nearest power of two"""
    return 1 << (x.bit_length() - 1)


def next_power_of_ten(n: int) -> int:
    """returns the next power of 10 greater than or equal to x"""
    if n <= 0:
        return 10
    exponent = math.ceil(math.log10(n))
    return 10 ** exponent


# -----------------------------------------------------------


# OBJECTS ---------------------------------------------------


class Hyperplane:
    """Hyperplane object and functionality"""

    def __init__(self, normal: np.array, coef: float):
        self.normal = normal
        self.coef = coef

    def project_point(self, *point: float) -> np.array:
        """projects a point onto the hyperplane

        Args:
            point (floats): the vector/point to project

        Returns:
            np.array: the projected point
        """
        vector = np.array(list(point))

        k = (self.coef - np.dot(self.normal, vector)) / (
            np.dot(self.normal, self.normal)
        )

        return vector + (k * self.normal)


# -----------------------------------------------------------


# PROBABILITY AND RANDOM VARIABLES --------------------------


def sterlings_approximation(n: int) -> float:
    """returns ~n! using sterlings approximation"""
    if n == 0 or n == 1:
        return 1
    else:
        n = mp.mpf(str(n))
        return sqrt(2 * pi * n) * (n / exp(1)) ** n


def permutate(n: int, r: int, sterlings: bool):
    """
    Args:
        n (int): number of objects
        r (int): number you are choosing where order matters
        sterlings (bool): whether to use Sterling's approximation

    Returns:
        int: n permutate r (using Sterling's approximation if specified)
    """
    n = mp.mpf(str(n))
    r = mp.mpf(str(r))
    n_minus_r = mp.mpf(str(n - r))
    
    if not sterlings:
        return mp.factorial(n) / mp.factorial(n_minus_r)
    else:
        return sterlings_approximation(n) / sterlings_approximation(n_minus_r)


def combinate(n: int, r: int, sterlings: bool):
    """
    Args:
        n (int): number of objects
        r (int): number you are choosing (order does not matter)
        sterlings (bool): whether to use Sterling's approximation

    Returns:
        int: n combinate r (using Sterling's approximation if specified)
    """
    n = mp.mpf(str(n))
    r = mp.mpf(str(r))
    n_minus_r = mp.mpf(str(n - r))

    if not sterlings:
        return mp.factorial(n) / (mp.factorial(r) * mp.factorial(n_minus_r))
    else:
        return sterlings_approximation(n) / (sterlings_approximation(r) * sterlings_approximation(n_minus_r))


def discrete_distribution_prob(exp: pd.Series, obs: pd.Series):
    """takes in the expected distribution and returns the exact probability
    of the observation

    Args:
        exp (pd.Series): the ground truth (expected) distribution
        obs (pd.Series): the observed distribution

    Returns:
        mp.mpf: the probability of observing the observed distribution
            given the expected distribution
    """
    percent_exp = exp / exp.sum()

    prob_freq_df = pd.concat([percent_exp, obs], axis=1)
    prob_freq_df.columns = ["Probability", "Frequency"]

    individual_seq_prob = mp.mpf(1)
    for _, row in prob_freq_df.iterrows():
        individual_seq_prob *= mp.power(mp.mpf(row["Probability"]), row["Frequency"])

    to_combinate = int(obs.sum())
    combinations = mp.mpf(1)

    for freq in prob_freq_df["Frequency"]:
        combinations *= combinate(n=to_combinate, r=int(freq), sterlings=False)
        to_combinate -= int(freq)

    result = combinations * individual_seq_prob
    return result
    

def min_distr_score(combo: tuple, exp: pd.Series, num_obs: int) -> float:
    """calculates the minimum distribution score  (as measured by absolute difference
    between percentages) and returns it
    
    Args:
        combo (tuple): the current allocation of observations already made
        exp (pd.Series): the expected (ground-truth) distribution
        num_obs (int): total number of observations

    Returns: 
        float: the distribution score
    """
    to_allocate = num_obs - sum(combo)
    percent_exp = np.array(exp / exp.sum())

    remaining_pcts = percent_exp[:-len(combo)]
    to_allocate_pcts = remaining_pcts / sum(remaining_pcts)

    optimal_allocations = [pct * to_allocate for pct in to_allocate_pcts]
    rounded_allocations = np.floor(optimal_allocations).astype(int)

    decimal_parts = [opt - floor for opt, floor in zip(optimal_allocations, rounded_allocations)]
    indices_sorted_by_decimal = np.argsort(-np.array(decimal_parts))

    remainder = to_allocate - sum(rounded_allocations)
    for i in indices_sorted_by_decimal:
        if remainder > 0:
            rounded_allocations[i] += 1
            remainder -= 1
        else:
            break

    final_allocations = np.concatenate([rounded_allocations, np.array(combo)])
    final_pcts = final_allocations / sum(final_allocations)

    score = sum(np.abs(percent_exp - final_pcts))

    return score


def generate_combinations(threshold: float, exp: pd.Series, num_obs: int) -> set:
    """returns a set of all possible combinations of num_classes integers that
    add up to num_obs and have an distribution >= (equal to or wose) threshold 

    Args:
        threshold (float): distribution score of the observation
        exp (pd.Series): the expected (ground-truth) distribution
        num_obs (int): total number the classes should sum

    Returns:
        set: the set of all possible combinations of class values that
            add up to num_obs
    """
    memo = {(0, 0): {()}}
    num_classes = len(exp)

    for i in range(1, num_classes + 1):
        for (length, errors) in set(memo.keys()):

            seqs = memo[(length, errors)]
            
            if i == num_classes:
                if (i, num_obs) in memo:
                    memo[(i, num_obs)].update(
                        {(num_obs - errors,) + combo for combo in seqs}
                    )
                else:
                    memo[(i, num_obs)] = {
                        (num_obs - errors,) + combo for combo in seqs
                    }               

            else:
                for error_amt in range(0, num_obs - errors + 1):

                    if (i, errors + error_amt) in memo:
                        memo[(i, errors + error_amt)].update(
                            {(error_amt,) + combo for combo in seqs if min_distr_score(combo=(error_amt,) + combo, exp=exp, num_obs=num_obs) >= threshold}
                        )
                    else:
                        memo[(i, errors + error_amt)] = {
                            (error_amt,) + combo for combo in seqs if min_distr_score(combo=(error_amt,) + combo, exp=exp, num_obs=num_obs) >= threshold
                        }

            del memo[(length, errors)]

        print(f"length {i} sequences generated.")

    return memo[(num_classes, num_obs)]


# DISTRIBUTION ANALYSIS -------------------------------------


def E(exp: pd.Series, obs: pd.Series) -> float:
        """performs an E-test on an expected distribution and observed distribution

        Args:
            exp (pd.Series): the expected (ground-truth) distribution
            obs (pd.Series): the observed distribution

        Returns:
            float: the E-value
        """
        print(f"Running E-Test...")

        e_val = 0
        threshold = min_distr_score(combo=tuple(obs), exp=exp, num_obs=obs.sum())
        combinations = generate_combinations(threshold=threshold, exp=exp, num_classes=len(obs), num_obs=obs.sum())

        for combination in tqdm(combinations, total=len(combinations), desc='Compiling Probabalities'):
            prob = discrete_distribution_prob(exp=exp, obs=pd.Series(combination))
            e_val += prob

        return e_val


# -----------------------------------------------------------

if __name__ == '__main__':
    pass