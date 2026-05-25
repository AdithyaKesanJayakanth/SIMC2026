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

