---
tags:
  - simc
---

# Symmetric matrix

> [!abstract] In one line
> A matrix equal to its own transpose — and the reason its eigenvalues are always real and its eigenvectors always perpendicular.

## The idea

A symmetric matrix is its own mirror image across the main diagonal: the entry in row $i$, column $j$ equals the entry in row $j$, column $i$. Equivalently, $A = A^\top$.

Why does symmetry matter so much? Because of the **spectral theorem**: every real symmetric matrix has (1) entirely real eigenvalues and (2) an eigenbasis of mutually orthogonal unit vectors. No complex numbers, no weird repeated-eigenvalue pathology — a beautifully clean structure you can always rely on.

Both the covariance matrix and the Gram matrix in the report are symmetric. That's not an accident — it's a consequence of how they're built from $X^\top X$ and $XX^\top$.

```python
import numpy as np
C = X.T @ X           # always symmetric: (X^T X)^T = X^T X
np.allclose(C, C.T)   # True

eigenvalues, eigenvectors = np.linalg.eigh(C)  # eigh = symmetric solver
```

Note `eigh` instead of `eig` — it exploits symmetry for speed and guarantees real outputs.

