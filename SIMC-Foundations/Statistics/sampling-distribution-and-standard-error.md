---
tags:
  - simc
---

# Sampling distribution and standard error

> [!abstract] In one line
> A statistic computed from a sample is itself a random variable — take many samples and plot it, and you get the sampling distribution; its spread is the standard error.

## The idea

You measure the participation ratio $d_{\text{eff}}$ from 924 spectra. But those 924 spectra are one draw from a larger world of possible spectra. If you could repeat the experiment — collect a fresh batch of 924 — you'd get a slightly different $d_{\text{eff}}$.

The **sampling distribution** is the distribution of your statistic across all those imaginary repeat experiments. You never actually run them all, but the distribution exists conceptually — and its spread tells you how trustworthy your estimate is.

**Standard error (SE)** is the standard deviation of the sampling distribution. For the sample mean $\bar X$:

$$\mathrm{SE}(\bar X) = \frac{\sigma}{\sqrt{n}}$$

Bigger $n$ → tighter distribution → more trustworthy estimate. This $1/\sqrt{n}$ shrinkage is one of the most important facts in all of statistics.

```python
import numpy as np

rng = np.random.default_rng(0)
population = rng.normal(loc=5.0, scale=2.0, size=100_000)

# Simulate sampling distribution of the mean for n=30
sample_means = [rng.choice(population, size=30).mean() for _ in range(5_000)]
print(f"SE from simulation : {np.std(sample_means):.4f}")
print(f"SE from formula    : {population.std() / np.sqrt(30):.4f}")
# Both ≈ 0.365
```

