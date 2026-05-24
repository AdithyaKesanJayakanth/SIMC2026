"""
SIMC Probability — Exercise 03: Bayes' Theorem (the classic disease-test problem)

Setup (the canonical Bayes "gotcha" — get this in your bones):
    A disease affects 1% of a population.
    A test has:
      - Sensitivity (true positive rate)  = 99%   (P(test+ | disease) = 0.99)
      - Specificity (true negative rate) = 99%   (P(test- | healthy) = 0.99)
    You test positive. What is P(disease | test+)?

Intuition says ~99%. Bayes says ~50%. The simulation will prove it to you.

Goal: Simulate 1,000,000 people, compute the empirical P(disease | test+),
and verify it matches the Bayes calculation:
    P(D | T+) = P(T+ | D) * P(D) / P(T+)

Concepts you should hit while writing this:
- Prior, likelihood, posterior
- Total probability: P(T+) = P(T+|D)P(D) + P(T+|H)P(H)
- Why low base rate makes specificity matter more than sensitivity

DO NOT USE AI FOR THE IMPLEMENTATION. Code it yourself.

Companion note: SIMC/Probability/bayes-theorem.md
"""

import numpy as np

N_PEOPLE = 1_000_000
P_DISEASE = 0.01      # prior — base rate
SENSITIVITY = 0.99    # P(test+ | disease)
SPECIFICITY = 0.99    # P(test- | healthy) — so P(test+ | healthy) = 0.01


def simulate_population(n: int, rng: np.random.Generator) -> tuple[np.ndarray, np.ndarray]:
    """Generate two boolean arrays of length n:
      - has_disease[i] = True if person i has the disease
      - tested_positive[i] = True if person i's test came back positive

    Hint: rng.random(n) < threshold for Bernoulli draws.
    Hint: tested_positive depends on has_disease.
    """

    has_disease = rng.random(n) < P_DISEASE
    tested_positive = np.zeros(n, dtype=bool)
    for i in range(n):
        if has_disease[i]:
            tested_positive[i] = rng.random() < SENSITIVITY
        else:
            tested_positive[i] = rng.random() < (1 - SPECIFICITY)

    return (has_disease, tested_positive)



