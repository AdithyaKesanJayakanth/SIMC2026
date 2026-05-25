---
tags:
  - simc
---

# Expectation

> [!abstract] In one line
> The expectation of a random variable is its long-run average — what you'd get if you repeated the experiment infinitely many times and averaged the results.

## The idea

Flip a fair coin, win £1 on heads, lose £1 on tails. Play 10 000 times. You'll end up near £0 — that's the expectation: $E[X] = 0$. It's the centre of mass of the probability distribution.

Analogy: place weights equal to $P(X=x)$ at each point $x$ on a number line. The expectation is the balance point.

Two crucial properties that make expectation useful everywhere:

1. **Linearity** — $E[aX + bY] = aE[X] + bE[Y]$, always, even if $X$ and $Y$ are dependent. This is the workhorse identity behind almost every derivation in statistics.
2. **Expectation of a constant** — $E[c] = c$.

```python
import numpy as np

rng = np.random.default_rng(42)
x = rng.integers(1, 7, size=100_000)   # fair die

print(x.mean())          # ≈ 3.5  (the true E[X])
# E[X] = (1+2+3+4+5+6)/6 = 3.5
```

## The math

The expectation is the **probability-weighted average** of all values.

**Discrete:**

$$E[X] = \sum_{x} x \, P(X = x)$$

**Continuous:**

$$E[X] = \int_{-\infty}^{\infty} x \, f(x) \, dx$$

**Linearity** (the most-used identity):

$$E[aX + bY] = a\,E[X] + b\,E[Y]$$

- $x$ — a specific value the random variable can take
- $P(X=x)$ — probability of that value (discrete case)
- $f(x)$ — probability density (continuous case)
- $a, b$ — constants

> [!example] Tiny concrete example
> Die roll, $X \in \{1,2,3,4,5,6\}$, each with probability $\frac{1}{6}$.
>
> $$E[X] = \frac{1}{6}(1+2+3+4+5+6) = \frac{21}{6} = 3.5$$
>
> Note: 3.5 is not a value the die can show. Expectation is a theoretical average, not a possible outcome.

> [!warning] Common confusion
> $E[g(X)] \ne g(E[X])$ in general (Jensen's inequality). For example, $E[X^2] \ne (E[X])^2$ — the gap between these two quantities is exactly the [[variance]]: $\mathrm{Var}(X) = E[X^2] - (E[X])^2$.

## Why this matters for the report

The participation ratio in Q3(c) is defined as:

$$d_{\text{eff}} = \frac{\left(\sum_i \lambda_i\right)^2}{\sum_i \lambda_i^2}$$

Both the numerator and denominator are sums (averages, up to scaling) over the eigenvalue distribution — they are expectations if you treat the empirical eigenvalue distribution as a discrete probability distribution. This is exactly the "probability-weighted average" idea.

More directly, the standard error formula $\sigma/\sqrt{n}$ — which underlies the bootstrap CI $[7.6, 10.0]$ in Q3(c) — comes from the expectation and variance of a sample mean. Without understanding expectation, the CI has no foundation.

## Builds on
- [[random-variable]]

## Leads to
- [[variance]]
- [[sampling-distribution-and-standard-error]]
