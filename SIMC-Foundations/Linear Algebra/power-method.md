---
tags:
  - simc
---

# Power method

> [!abstract] In one line
> A dead-simple repeat-until-settled algorithm: multiply by the matrix, renormalize, repeat — and the vector automatically swings to point along the strongest eigenvector.

## The idea

You need to find the eigenvector of the covariance matrix, but you don't know it. Here's the surprisingly simple trick:

1. Start with any random unit vector $\mathbf{b}$ (a random array, normalized to length 1).
2. Multiply it by the matrix $C$ (the covariance matrix).
3. The result is not a unit vector anymore — normalize it back to length 1.
4. Repeat steps 2–3 until the vector stops changing.

That's it. The vector converges to the eigenvector with the **largest** eigenvalue.

**Why does this work?** Any starting vector can be written as a mix of all the eigenvectors. Each time you multiply by $C$, every component gets scaled by its eigenvalue. The component along the biggest eigenvalue grows fastest — it dominates the others after enough multiplications. Normalizing keeps the numbers from exploding. Eventually, only the biggest-eigenvalue direction survives.

Think of it like compound interest: if you invest a mix of currencies but one currency has a 10% return and others have 1%, after 50 years almost everything is in the 10% currency regardless of how you started.

## The algorithm

**Pseudocode:**

```python
import numpy as np  # see [[numpy-basics]]

def power_method(C, num_iterations=1000):
    n = C.shape[0]
    b = np.random.randn(n)          # random starting vector
    b = b / np.linalg.norm(b)       # normalize to unit length

    for _ in range(num_iterations):
        b_new = C @ b               # matrix-vector multiply
        b = b_new / np.linalg.norm(b_new)   # renormalize

    return b   # converged to top eigenvector
```

`C @ b` is matrix-vector multiplication. `np.linalg.norm(b)` is $\|\mathbf{b}\|$.

**Convergence check** (optional but useful): if `b_new / norm(b_new)` barely changes between iterations, you're done. In practice, 100–500 iterations is usually plenty.

