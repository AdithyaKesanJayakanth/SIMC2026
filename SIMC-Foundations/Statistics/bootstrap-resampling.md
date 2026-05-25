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

