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

