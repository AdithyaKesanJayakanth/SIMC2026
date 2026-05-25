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

