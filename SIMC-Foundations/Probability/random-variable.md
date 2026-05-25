---
tags:
  - simc
---

# Random variable

> [!abstract] In one line
> A random variable is a number you attach to each possible outcome of a random experiment — it turns raw "what happened" into something you can calculate with.

## The idea

Imagine rolling a die. The outcome is one of six symbols: ⚀ ⚁ ⚂ ⚃ ⚄ ⚅. A random variable $X$ says: "I'll map every face to its number." Now you can write $P(X = 3)$, compute averages, compare experiments — all of which would be awkward with raw symbols.

**Discrete** random variable: takes a countable list of values, each with a probability. Think coin flips, spectrum vial counts, cluster labels.

**Continuous** random variable: takes any value in an interval, described by a probability *density* $f(x)$ — the probability of landing in a tiny range $[x, x+dx]$ is $f(x)\,dx$.

```python
import numpy as np

# Simulate 10 000 rolls of a fair die (discrete R.V.)
rng = np.random.default_rng(0)
rolls = rng.integers(1, 7, size=10_000)   # values 1–6

probs = {k: (rolls == k).mean() for k in range(1, 7)}
# Each value should be ≈ 0.167
```

The bridge to statistics: once you have a random variable, you can ask "what does it average to?" and "how spread out is it?" — that is exactly [[expectation]] and [[variance]].

## The math

A random variable $X$ on a sample space $\Omega$ is a function $X: \Omega \to \mathbb{R}$.

For a **discrete** R.V. the probability mass function (PMF) satisfies:

$$\sum_{x} P(X = x) = 1$$

For a **continuous** R.V. the probability density function (PDF) satisfies:

$$\int_{-\infty}^{\infty} f(x)\,dx = 1$$

- $\Omega$ — the sample space (all possible outcomes)
- $P(X = x)$ — probability that the variable takes value $x$ (discrete)
- $f(x)$ — density at point $x$ (continuous); NOT a probability itself

> [!example] Tiny concrete example
> Fair coin flip. $\Omega = \{H, T\}$. Define $X(H) = 1$, $X(T) = 0$.
> Then $P(X=1) = 0.5$ and $P(X=0) = 0.5$. Sum = 1. ✓
> This is the **Bernoulli(0.5)** random variable — the simplest possible case.

> [!warning] Common confusion
> A random variable is **not** random once you observe it. After you roll the die and see a 4, $X = 4$ is just the number 4 — fixed. The randomness lives in the *process* before observation, not in the number itself.

## Why this matters for the report

Q3(a) treats each spectrum's row-norm as a numerical measurement of a vial — exactly the idea of assigning a number to an outcome. The 924 retained spectra (and the 36 outliers) are identified by thresholding this number. Any reasoning about "is this norm typical or extreme?" implicitly uses the concept of a random variable: the norm is a function of the random experiment "pick a vial."

More directly, Q3(c) treats each eigenvalue $\lambda_i$ as a quantity whose stability across bootstrap resamples needs measuring — which requires thinking of the statistic as a random variable that varies from sample to sample.

## Builds on
- [[sample-spaces-events-axioms]]

## Leads to
- [[expectation]]
- [[variance]]
