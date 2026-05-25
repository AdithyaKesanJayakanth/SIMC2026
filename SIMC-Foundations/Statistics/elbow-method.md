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

