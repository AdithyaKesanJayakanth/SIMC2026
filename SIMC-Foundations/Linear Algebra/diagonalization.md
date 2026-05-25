---
tags:
  - simc
---

# Diagonalization

> [!abstract] In one line
> Factoring a matrix as $A = Q\Lambda Q^{-1}$ so it becomes a simple stretch-and-rotate sandwich.

## The idea

A diagonal matrix is the easiest possible matrix to work with: it just scales each axis independently, no mixing. Diagonalization says: even if $A$ looks complicated in the standard basis, there exists a change of coordinates (the eigenbasis) in which $A$ *is* diagonal.

The recipe: go into the eigenbasis ($Q^{-1}$), apply the diagonal scaling ($\Lambda$), come back out ($Q$). That sandwich — change basis, scale, undo — is all $A$ does.

For **symmetric matrices** (which includes covariance matrices and $X^\top X$), the eigenvectors are orthonormal, so $Q^{-1} = Q^\top$ and the factorization is the especially clean $A = Q\Lambda Q^\top$.

```python
import numpy as np

A = np.array([[2., 1.], [1., 2.]])   # symmetric
vals, Q = np.linalg.eigh(A)          # Q orthonormal, vals ascending
Lambda = np.diag(vals)

# Verify: A == Q @ Lambda @ Q.T
print(np.allclose(A, Q @ Lambda @ Q.T))   # True
print(np.trace(A), np.sum(vals))           # both = 4.0  (trace = sum of eigenvalues)
```

