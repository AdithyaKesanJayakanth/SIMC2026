---
tags:
  - simc
---

# Explained variance ratio

> [!abstract] In one line
> The fraction of total data variance that lives along each principal component — a score between 0 and 1 telling you how much "information" each direction holds.

## The idea

PCA rotates your data into a new coordinate system where each axis (principal component) captures as much variance as possible. But how much does each axis actually capture? The explained variance ratio answers: "Out of all the spread in the data, what percentage falls along component $k$?"

Think of it like splitting a pie. The total variance is the whole pie. Each eigenvalue is the size of one slice. The explained variance ratio is that slice expressed as a fraction of the whole.

```python
import numpy as np

# After np.linalg.eigh, eigenvalues in ascending order — flip to descending
lambdas = np.flip(eigenvalues)
ratios = lambdas / lambdas.sum()          # fraction per component
cumulative = np.cumsum(ratios)            # running total
```

## The math

The explained variance ratio for component $k$ is the $k$-th eigenvalue divided by the sum of all eigenvalues (which equals the trace of the covariance matrix).

$$r_k = \frac{\lambda_k}{\sum_{j=1}^{M} \lambda_j} = \frac{\lambda_k}{\operatorname{tr}(C)}$$

**Symbol glossary:**
- $r_k$ — explained variance ratio for component $k$ (a number in $[0, 1]$)
- $\lambda_k$ — $k$-th eigenvalue of the covariance matrix $C$, sorted descending
- $\sum_j \lambda_j = \operatorname{tr}(C)$ — total variance (sum of all eigenvalues)
- $M$ — number of features (here, 3401 frequency channels)

The cumulative explained variance after $K$ components is $\sum_{k=1}^{K} r_k$.

> [!example] Tiny concrete example
> Suppose a 3-feature dataset has covariance eigenvalues $\lambda_1 = 4$, $\lambda_2 = 1$, $\lambda_3 = 0.5$. Total = 5.5.
>
> $r_1 = 4/5.5 \approx 72.7\%$ — the first PC dominates.
> $r_2 = 1/5.5 \approx 18.2\%$
> $r_3 = 0.5/5.5 \approx 9.1\%$
>
> Cumulative: $r_1 + r_2 \approx 90.9\%$. Two components explain most of the data.

> [!warning] Common confusion
> The "95% rule" says: keep enough components to explain 95% of variance. This sounds principled but can be deeply misleading. If variance is spread uniformly across hundreds of components (as in high-dimensional noise), you may need hundreds of components to hit 95% — even if the data's true structure lives in just 8 directions. The threshold is arbitrary and dataset-dependent. Always cross-check with a threshold-free measure like the [[participation-ratio]].

## Why this matters for the report

**Q3(c)** reports $r_1 \approx 31\%$ — the first principal component alone carries nearly a third of the total variance in the IR spectra. The report also builds a cumulative table of $r_k$ values. However, it explicitly flags that the naive "95% rule" is misleading here: reaching 95% cumulative explained variance requires **667 components**, which would suggest the data is extremely high-dimensional. This is why the report rejects the 95% threshold as a dimensionality criterion and instead uses the [[participation-ratio]] and [[elbow-method]] as more informative diagnostics. The explained variance ratio is the raw ingredient for both.

## Builds on
- [[eigenspectrum]]
- [[variance]]
- [[trace-equals-sum-of-eigenvalues]]

## Leads to
- [[elbow-method]]
- [[participation-ratio]]
- [[dimensionality-reduction]]
