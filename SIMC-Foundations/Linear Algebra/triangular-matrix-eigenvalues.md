---
tags:
  - simc
---

# Triangular matrix eigenvalues

> [!abstract] In one line
> For any triangular matrix, the eigenvalues are exactly the entries sitting on the main diagonal — no computation required.

## The idea

A lower-triangular matrix has zeros everywhere above the main diagonal; an upper-triangular matrix has zeros everywhere below. When you form $A - \lambda I$ for a triangular matrix, you're just subtracting $\lambda$ from each diagonal entry — the off-diagonal structure is unchanged. The determinant of a triangular matrix is always the product of its diagonal entries. So the characteristic equation $\det(A - \lambda I) = 0$ becomes:

$$
(A_{11} - \lambda)(A_{22} - \lambda) \cdots (A_{nn} - \lambda) = 0
$$

which gives $\lambda = A_{11}, A_{22}, \ldots, A_{nn}$ immediately.

```python
import numpy as np
M_eps = 0.3
M = np.array([[1 - M_eps, 0],
              [M_eps,     1]])
np.linalg.eigvals(M)   # array([1. , 0.7]) — diagonal entries, in some order
```

