---
tags:
  - simc
---

# Participation ratio

> [!abstract] In one line
> A single threshold-free number that measures how many principal components meaningfully share the variance — large when variance is spread across many directions, small when one direction dominates everything.

## The idea

The elbow method asks you to draw a line and count. The participation ratio instead asks: if each eigenvalue were a vote on "how many dimensions matter," how many effective votes are cast? Eigenvalues that carry a lot of variance cast heavy votes; eigenvalues near zero barely register.

A useful analogy: imagine you have 100 coins. If one coin is worth $99 and the rest are worth $0.01 each, the "effective number of coins" is almost 1. If all 100 are worth $1 each, the effective number is 100. The participation ratio does exactly this accounting for eigenvalues.

```python
import numpy as np

lambdas = eigenvalues[eigenvalues > 0]   # clip rounding-level negatives
d_eff = lambdas.sum()**2 / (lambdas**2).sum()
print(f"Participation ratio: {d_eff:.2f}")
```

## The math

The effective dimensionality is the squared sum of eigenvalues divided by the sum of squared eigenvalues.

$$d_{\text{eff}} = \frac{\left(\displaystyle\sum_{i=1}^{M} \lambda_i\right)^2}{\displaystyle\sum_{i=1}^{M} \lambda_i^2}$$

**Symbol glossary:**
- $d_{\text{eff}}$ — effective dimensionality (a real number, not necessarily an integer)
- $\lambda_i$ — eigenvalues of the covariance matrix, all $\geq 0$ (positive semi-definite)
- $\sum \lambda_i = \operatorname{tr}(C)$ — total variance (appears in both numerator and [[explained-variance-ratio]])
- $\sum \lambda_i^2$ — "concentration" of variance; large when one $\lambda_i$ dominates

**Boundary cases:**
- All $M$ eigenvalues equal: $d_{\text{eff}} = M$ (maximum, fully spread).
- One eigenvalue nonzero, rest zero: $d_{\text{eff}} = 1$ (minimum, all variance in one direction).

The formula penalises concentration: if one $\lambda_i$ is huge, $\sum \lambda_i^2$ is large, shrinking $d_{\text{eff}}$ toward 1.

> [!example] Tiny concrete example
> Three eigenvalues: $\lambda = (4, 1, 1)$.
>
> $\sum \lambda_i = 6$, so numerator $= 36$.
>
> $\sum \lambda_i^2 = 16 + 1 + 1 = 18$.
>
> $d_{\text{eff}} = 36 / 18 = 2.0$.
>
> Interpretation: despite having 3 components, the effective dimensionality is 2 — the first eigenvalue is dominant enough that the third barely contributes.

> [!warning] Common confusion
> $d_{\text{eff}}$ is not the same as the number of components you'd keep with a 95% variance threshold. It is also not rounded to an integer — $d_{\text{eff}} = 8.7$ genuinely means "somewhere between 8 and 9 effective directions," which is exactly what the bootstrap CI formalises. Rounding to 9 and treating that as a hard cutoff re-introduces the arbitrariness the participation ratio was designed to avoid.

## Why this matters for the report

**Q3(c)** is the participation ratio's moment. After flagging that the elbow ($k^* = 8$) is not bootstrap-stable and that the 95% cumulative variance rule is misleading (requires 667 components), the report uses $d_{\text{eff}}$ as its **primary, robust intrinsic-dimension estimate**. The value is $d_{\text{eff}} \approx 8.7$, with a bootstrap confidence interval of $[7.6, 10.0]$. This is a statistically defensible claim: even after resampling the 924 spectra many times, the effective dimensionality stays anchored near 8–9. The convergence of the elbow ($k^* = 8$) and the participation ratio ($d_{\text{eff}} \approx 8.7$) is then cited in **Q3(h)** to support the physical interpretation that ~8–10 dominant molecules drive the IR spectral variation across the 25 sample clusters.

## Builds on
- [[explained-variance-ratio]]
- [[trace-equals-sum-of-eigenvalues]]

## Leads to
- [[dimensionality-reduction]]
