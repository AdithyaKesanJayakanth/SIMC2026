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

## The math

Let $X_1, X_2, \ldots, X_n$ be independent draws from a distribution with mean $\mu$ and variance $\sigma^2$. The sample mean is $\bar X = \frac{1}{n}\sum_{i=1}^n X_i$.

By linearity of [[expectation]]:

$$E[\bar X] = \mu$$

By independence and linearity of [[variance]]:

$$\mathrm{Var}(\bar X) = \frac{\sigma^2}{n}$$

Standard error:

$$\mathrm{SE}(\bar X) = \sqrt{\mathrm{Var}(\bar X)} = \frac{\sigma}{\sqrt{n}}$$

- $\mu$ — the true population mean
- $\sigma^2$ — the true population variance
- $n$ — sample size
- $\mathrm{SE}$ — the standard deviation of the sampling distribution of $\bar X$

> [!example] Tiny concrete example
> Measuring the mass of coins. True mean $\mu = 5.0\,\text{g}$, $\sigma = 0.2\,\text{g}$.
>
> Sample size $n = 100$:
> $$\mathrm{SE} = \frac{0.2}{\sqrt{100}} = \frac{0.2}{10} = 0.02\,\text{g}$$
>
> Sample size $n = 400$: $\mathrm{SE} = 0.01\,\text{g}$ — half as wide just by quadrupling $n$.

> [!warning] Common confusion
> Standard error and standard deviation are not the same. The standard deviation $\sigma$ describes spread in the **data**. The standard error describes spread in the **statistic** (the estimate). A small SE does not mean the data has low variance — it means you have enough data to pin down the mean well.

## Why this matters for the report

Q3(c) reports the participation ratio $d_{\text{eff}} \approx 8.7$ with bootstrap CI $[7.6, 10.0]$. The half-width of that interval is essentially the standard error of $d_{\text{eff}}$ across bootstrap resamples. The report uses bootstrap precisely because there is no closed-form formula for $\mathrm{SE}(d_{\text{eff}})$ — the bootstrap numerically constructs the sampling distribution instead.

The report also flags that the bare elbow $k^* = 8$ is **not** bootstrap-stable: its sampling distribution is wide (the elbow shifts across resamples), whereas $d_{\text{eff}}$ has a narrow sampling distribution. This contrast — one statistic has a tight SE, the other does not — is exactly the concept on this page.

## Builds on
- [[expectation]]
- [[variance]]

## Leads to
- [[confidence-interval]]
- [[bootstrap-resampling]]
