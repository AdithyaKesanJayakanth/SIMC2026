"""
SIMC Probability — Exercise 02: Conditional Probability

Goal: Simulate drawing 2 cards (without replacement) from a standard 52-card deck.
Empirically verify:
    P(2nd card is an ace | 1st card is an ace) = 3 / 51

Concepts you should hit while writing this:
- Conditional probability: P(A | B) = P(A and B) / P(B)
- Sampling without replacement (state changes the sample space)
- Restriction: condition by FILTERING simulated trials (only count trials
  where the condition holds), then compute frequency of A within those.

DO NOT USE AI FOR THE IMPLEMENTATION. Code it yourself.

Companion note: SIMC/Probability/conditional-probability.md
"""

import numpy as np

N_TRIALS = 10000

# A deck: 52 cards. Aces are cards 0..3 (or pick any 4 indices — doesn't matter).
DECK_SIZE = 52
ACES = {0, 1, 2, 3}


def draw_two_cards(rng: np.random.Generator) -> tuple[int, int]:
    """Draw 2 distinct cards from a 52-card deck without replacement.

    Hint: rng.choice with replace=False, size=2
    """
    cards = np.arange(0, DECK_SIZE)
    draws = rng.choice(cards , replace=False , size=2)
    return tuple(draws)


def is_ace(card: int) -> bool:
    return card in ACES


