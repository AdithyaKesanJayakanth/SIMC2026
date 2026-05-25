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

