---
tags:
  - simc
---

# Singular values

> [!abstract] In one line
> The singular values $\sigma_i$ are the "stretch factors" of a matrix — how much it scales the $i$-th principal direction — and they equal the square roots of the eigenvalues of $X^\top X$.

## The idea

Every matrix $X$ (even non-square) stretches and rotates space. Singular values are the stretching amounts along the special directions found by the SVD. Think of the matrix as a printing press that squishes an ink blob into an ellipse: the singular values are the lengths of the ellipse's axes.

Unlike eigenvalues (which can be negative or complex), singular values are always real and non-negative — because they come from square-rooting eigenvalues of $X^\top X$, which is PSD.

```python
U, sigma, Vt = np.linalg.svd(X, full_matrices=False)
# sigma is an array of singular values, all >= 0, sorted descending
```

