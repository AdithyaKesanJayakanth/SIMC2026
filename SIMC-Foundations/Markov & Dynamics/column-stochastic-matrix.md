---
tags:
  - simc
---

# Column-stochastic matrix

> [!abstract] In one line
> A column-stochastic matrix is one whose columns each sum to 1, guaranteeing that total population mass is conserved at every time step.

## The idea

Imagine each column of $M$ as a bucket of paint being poured out. The column says how much goes to each output state. If the fractions in the bucket add up to exactly 1, none is created and none is destroyed — conservation is baked in by construction.

This is precisely why the Q1 matrix works: $\varepsilon$ leaves the type-1 column and lands in the type-2 column. The two fractions $(1-\varepsilon)$ and $\varepsilon$ sum to 1.

```python
import numpy as np

eps = 0.3
M = np.array([[1 - eps, 0],
              [eps,     1]])

# Verify column sums
print(M.sum(axis=0))   # [1. 1.] — both columns sum to 1
```

