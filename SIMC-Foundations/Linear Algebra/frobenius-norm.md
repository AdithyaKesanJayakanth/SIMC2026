---
tags:
  - simc
---

# Frobenius norm

> [!abstract] In one line
> The Frobenius norm $\lVert A \rVert_F$ is the "total size" of a matrix — the square root of the sum of all squared entries — and it equals the square root of the sum of squared singular values.

## The idea

For a vector, the norm is $\sqrt{\sum x_i^2}$ — the usual Euclidean length. The Frobenius norm is the same idea extended to matrices: flatten the matrix into one long vector of entries, then take its Euclidean length. It captures how much "energy" or "signal" is stored in the matrix as a whole.

The elegant fact: $\lVert A \rVert_F^2 = \sum \sigma_i^2$. So the singular values, which decompose the matrix into rank-1 pieces, also partition its total energy. Throwing away a singular value $\sigma_i$ loses exactly $\sigma_i^2$ of Frobenius energy.

```python
frob = np.linalg.norm(A, 'fro')   # or equivalently:
frob = np.sqrt(np.sum(A**2))
frob = np.sqrt(np.sum(np.linalg.svd(A, compute_uv=False)**2))
```

