---
tags:
  - simc
---

# Bootstrap resampling

> [!abstract] In one line
> Bootstrap resampling replaces the impossible task of "repeat the whole experiment" with the practical trick of resampling your existing data with replacement — many times — to map out the sampling distribution of any statistic.

## The idea

You have $n$ data points. You can't go back and collect another $n$ from nature. But you *can* pretend your dataset is the population, draw $n$ points from it **with replacement**, and compute the statistic on that fake resample. Do this 1000 times and you have 1000 values of the statistic — that histogram is your estimated sampling distribution.

"With replacement" is crucial: each resample will have some original points appearing twice or three times, and others missing entirely. That variability is what mimics real-world sampling uncertainty.

The beauty: no formula required. Whatever your statistic — a median, a ratio of sums, the elbow of a scree plot, the participation ratio — bootstrap handles it the same way.

```python
import numpy as np

rng = np.random.default_rng(0)
data = rng.normal(5.0, 2.0, size=924)    # pretend these are your spectra stats

def participation_ratio(vals):
    lam = np.sort(vals)[::-1]
    return lam.sum()**2 / (lam**2).sum()

n_boot = 1000
boot_stats = np.array([
    participation_ratio(rng.choice(data, size=len(data), replace=True))
    for _ in range(n_boot)
])

ci_low, ci_high = np.percentile(boot_stats, [2.5, 97.5])
print(f"Bootstrap 95% CI: [{ci_low:.2f}, {ci_high:.2f}]")
```

## The math

Let $\hat\theta$ be a statistic computed from sample $\{x_1, \ldots, x_n\}$.

**Bootstrap algorithm:**
1. For $b = 1, \ldots, B$: draw $\{x_1^*, \ldots, x_n^*\}$ by sampling $n$ times **with replacement** from $\{x_1, \ldots, x_n\}$.
2. Compute $\hat\theta_b^*$ on the $b$-th resample.
3. The bootstrap distribution $\{\hat\theta_1^*, \ldots, \hat\theta_B^*\}$ approximates the [[sampling-distribution-and-standard-error]].

**Bootstrap standard error:**

$$\widehat{\mathrm{SE}}_{\text{boot}} = \sqrt{\frac{1}{B-1}\sum_{b=1}^B \left(\hat\theta_b^* - \bar\theta^*\right)^2}$$

**Percentile confidence interval** (simplest form):

$$\text{CI}_{95\%} = \left[\hat\theta^*_{(0.025)},\; \hat\theta^*_{(0.975)}\right]$$

- $B$ — number of bootstrap resamples (1000 is standard; the report uses 1000)
- $\hat\theta_b^*$ — statistic on the $b$-th resample
- $\bar\theta^*$ — mean of all bootstrap statistics
- $\hat\theta^*_{(q)}$ — the $q$-th quantile of the bootstrap distribution

> [!example] Tiny concrete example
> Five data points: $\{2, 4, 4, 6, 8\}$. Mean = 4.8.
>
> One bootstrap resample (with replacement): $\{4, 8, 2, 4, 4\}$. Mean = 4.4.
> Another: $\{6, 6, 2, 8, 4\}$. Mean = 5.2.
>
> After 1000 such resamples, the spread of those means gives the bootstrap SE for the mean.

> [!warning] Common confusion
> Bootstrap does **not** create new information — it only redistributes the information already in your sample. It fails when your sample is too small to represent the population, or when you have heavy dependencies (e.g., time series where nearby points are correlated). The 924 spectra in Q3 are treated as approximately i.i.d. replicates, which makes bootstrap valid.

## Why this matters for the report

Q3(c) is the core application. The report bootstraps the 924 spectra **1000 times**: each resample is a random draw of 924 rows (with replacement) from the 924 genuine spectra. On each resample it computes:

- The bare elbow $k^*$ — the position of the largest multiplicative drop in the eigenspectrum.
- The participation ratio $d_{\text{eff}} = (\sum\lambda)^2 / \sum\lambda^2$.

Finding: the elbow $k^*$ is **unstable** — it jumps between values across resamples, so it has a wide bootstrap distribution. The participation ratio $d_{\text{eff}} \approx 8.7$ is **stable** — the bootstrap distribution is tight, yielding CI $[7.6, 10.0]$. This is why the report trusts $d_{\text{eff}}$ over the elbow as the intrinsic dimension estimate.

## Builds on
- [[sampling-distribution-and-standard-error]]

## Leads to
- [[confidence-interval]]
- [[participation-ratio]]
