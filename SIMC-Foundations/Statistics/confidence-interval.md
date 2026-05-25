---
tags:
  - simc
---

# Confidence interval

> [!abstract] In one line
> A confidence interval is a range of values that plausibly contains the true unknown parameter — constructed so that the procedure captures the truth a specified fraction of the time (e.g. 95%).

## The idea

You estimate the intrinsic dimension as $d_{\text{eff}} \approx 8.7$ from one batch of 924 spectra. How much should you trust that number? The confidence interval answers: the true value almost certainly sits between 7.6 and 10.0.

The correct way to read "95% CI": if you repeated the whole experiment (collect 924 spectra, compute $d_{\text{eff}}$, build the CI) very many times, about 95% of those intervals would contain the true $d_{\text{eff}}$. One interval either contains the truth or it doesn't — the 95% is a property of the *procedure*, not of this one interval.

Intuition: narrow CI = your estimate is precise. Wide CI = high uncertainty; you need more data or a more stable statistic.

**"Stable under bootstrap"** means the CI is narrow — the statistic doesn't vary much from resample to resample — which is exactly what makes a CI useful.

```python
import numpy as np

rng = np.random.default_rng(0)

# Suppose d_eff values from 1000 bootstrap resamples
boot_d_eff = rng.normal(loc=8.7, scale=0.6, size=1000)  # simulated

ci_low, ci_high = np.percentile(boot_d_eff, [2.5, 97.5])
print(f"95% CI: [{ci_low:.1f}, {ci_high:.1f}]")
# ≈ [7.5, 9.9]  — matches the report's [7.6, 10.0]
```

## The math

**Percentile bootstrap CI** (the method used in Q3):

$$\mathrm{CI}_{1-\alpha} = \left[\hat\theta^*_{(\alpha/2)},\; \hat\theta^*_{(1-\alpha/2)}\right]$$

**Classic normal CI** for a mean (when the [[sampling-distribution-and-standard-error]] is approximately normal):

$$\mathrm{CI}_{95\%} = \bar X \pm 1.96\cdot\frac{\sigma}{\sqrt{n}}$$

- $1 - \alpha$ — confidence level (0.95 for a 95% CI; $\alpha = 0.05$)
- $\hat\theta^*_{(q)}$ — $q$-th quantile of the bootstrap distribution of $\hat\theta$
- $\bar X$ — sample mean
- $\sigma$ — population standard deviation (or estimated from data)
- $n$ — sample size
- $1.96$ — the $z$-score that cuts off 2.5% in each tail of the standard normal

> [!example] Tiny concrete example
> You measure reaction times in 25 people: mean = 300 ms, SD = 40 ms.
>
> $$\mathrm{SE} = \frac{40}{\sqrt{25}} = 8\,\text{ms}$$
>
> $$\mathrm{CI}_{95\%} = 300 \pm 1.96 \times 8 = [284,\; 316]\,\text{ms}$$
>
> You'd report: "The mean reaction time is 300 ms (95% CI: 284–316 ms)."

> [!warning] Common confusion
> A 95% CI does **not** mean "there is a 95% probability the true value is in this interval." The true value is fixed — it's either in the interval or it isn't. The 95% refers to the long-run success rate of the procedure across many hypothetical repetitions of the experiment. This is subtle but the distinction matters when interpreting results.

## Why this matters for the report

Q3(c) reports $d_{\text{eff}} \approx 8.7$ with bootstrap 95% CI $[7.6, 10.0]$. This is the primary output of the bootstrap analysis.

The CI does two things in the report:

1. **Validates the estimate.** The interval is reasonably narrow (width ≈ 2.4 out of a value of 8.7 — about 28% relative width), which confirms the participation ratio is a stable, trustworthy intrinsic-dimension estimate.

2. **Contrasts with the elbow.** The bare elbow $k^* = 8$ is not given a CI because its bootstrap distribution is too wide to be useful — it jumps erratically. The fact that $d_{\text{eff}}$ *can* be given a tight CI is the mathematical argument for preferring it over the elbow.

The notation "$[7.6, 10.0]$" appearing in the report is shorthand for exactly this percentile bootstrap interval.

## Builds on
- [[sampling-distribution-and-standard-error]]

## Leads to
- [[bootstrap-resampling]]
