---
tags:
  - simc
---

# Determinant and characteristic equation

> [!abstract] In one line
> The characteristic equation $\det(A - \lambda I) = 0$ is the algebraic recipe that reveals exactly which values of $\lambda$ are eigenvalues.

## The idea

An eigenvalue $\lambda$ is special because subtracting it from the diagonal of $A$ makes the resulting matrix *singular* — it squashes some nonzero vector down to zero. A matrix is singular exactly when its determinant is zero. So you set $\det(A - \lambda I) = 0$ and solve for $\lambda$. The solutions are the eigenvalues.

For a $2 \times 2$ matrix the determinant is easy to remember: it's the product of the main diagonal minus the product of the off-diagonal.

```python
import numpy as np
A = np.array([[4, 1],
              [2, 3]])
# characteristic equation: det([[4-λ, 1],[2, 3-λ]]) = (4-λ)(3-λ) - 2 = 0
# λ^2 - 7λ + 10 = 0  →  λ = 2, 5
np.linalg.eigvals(A)   # array([5., 2.])
```

