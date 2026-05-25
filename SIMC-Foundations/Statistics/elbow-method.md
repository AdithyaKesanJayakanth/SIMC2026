---
tags:
  - simc
---

# Elbow method

> [!abstract] In one line
> A visual heuristic for choosing how many principal components to keep by finding the "kink" where the eigenvalue curve bends sharply and the remaining values flatten to a noise floor.

## The idea

Plot the eigenvalues sorted in descending order. For data with real structure, you typically see a steep drop over the first few components, then a sudden levelling-off into a long, flat tail. That "elbow" — the kink where steep meets flat — marks the boundary between signal and noise.

A multiplicative version is often sharper than the visual: instead of eyeballing the plot, find the **largest ratio** $\lambda_k / \lambda_{k+1}$. The biggest jump tells you where the noise floor begins.

```python
import numpy as np

lambdas = np.flip(eigenvalues)          # descending order
ratios = lambdas[:-1] / lambdas[1:]     # λ_k / λ_{k+1} for each k
k_star = np.argmax(ratios) + 1          # +1 because k is 1-indexed
print(f"Elbow at k* = {k_star}, ratio = {ratios[k_star-1]:.2f}")
```

## The math

No formula is strictly required — the elbow is a heuristic. But the multiplicative version is:

$$k^* = \operatorname{arg\,max}_{k} \frac{\lambda_k}{\lambda_{k+1}}$$

**Symbol glossary:**
- $\lambda_k$ — $k$-th eigenvalue, sorted descending ($\lambda_1 \geq \lambda_2 \geq \cdots$)
- $\lambda_k / \lambda_{k+1}$ — multiplicative drop between consecutive eigenvalues
- $k^*$ — chosen number of components (the elbow position)

The intuition: genuine signal components are separated from each other by moderate ratios, but the last signal component sits just above a noise floor — so the ratio $\lambda_{k^*} / \lambda_{k^*+1}$ is disproportionately large.

> [!example] Tiny concrete example
> Eigenvalues: $3.2,\ 2.1,\ 1.8,\ 1.7,\ 0.4,\ 0.39,\ \ldots$
>
> Ratios: $3.2/2.1 \approx 1.5$, $\ 2.1/1.8 \approx 1.2$, $\ 1.8/1.7 \approx 1.1$, $\ 1.7/0.4 = 4.25 \leftarrow$ biggest.
>
> Elbow at $k^* = 4$. Keep 4 components.

> [!warning] Common confusion
> The elbow method looks objective but is actually **bootstrap-unstable**: resample the data slightly and the elbow can shift by several positions, especially if adjacent eigenvalues are close in value. A sharp visual kink in one sample can disappear in another. This is why the elbow should be treated as a quick first guess, not a final answer — use a statistically robust measure like the [[participation-ratio]] to confirm.

## Why this matters for the report

**Q3(c)** applies the multiplicative elbow to the IR spectra eigenspectrum. The largest consecutive ratio is $\lambda_8 / \lambda_9 \approx 4.1$, pinpointing $k^* = 8$ as the elbow. This is the report's first intrinsic-dimension estimate. However, the report immediately qualifies this result: the bare elbow is not bootstrap-stable, so it is **not** the primary dimensionality estimate. Instead, $k^* = 8$ serves as a corroborating data point alongside the [[participation-ratio]] result of $d_{\text{eff}} \approx 8.7$ (bootstrap CI $[7.6, 10.0]$). The two methods agree, which strengthens confidence in the $\approx 8$-dimensional structure of the data — but the participation ratio is the robust anchor, not the elbow.

## Builds on
- [[eigenspectrum]]
- [[explained-variance-ratio]]

## Leads to
- [[participation-ratio]]
