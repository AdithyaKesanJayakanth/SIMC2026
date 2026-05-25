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

## The math

Conceptual anchor: $\sigma_i$ measures how far the unit sphere gets stretched in the $i$-th SVD direction.

For $X \in \mathbb R^{N \times M}$ with SVD $X = U\Sigma V^\top$:

$$
\sigma_i = \sqrt{\lambda_i(X^\top X)}, \quad \sigma_i \ge 0
$$

Relationship between $X$, $X^\top X$, and $XX^\top$:

$$
X^\top X = V \Sigma^2 V^\top, \quad XX^\top = U\Sigma^2 U^\top
$$

- $\sigma_i$ — $i$-th singular value (non-negative, sorted descending)
- $\lambda_i(X^\top X)$ — $i$-th eigenvalue of $X^\top X$
- $U, V$ — orthonormal matrices of left/right singular vectors
- $\Sigma$ — diagonal matrix with singular values on the diagonal

> [!example] Tiny concrete example
> From the report's Q2(e) example: $X = \begin{pmatrix}1&0\\0&1\\1&1\end{pmatrix}$
>
> $X^\top X = \begin{pmatrix}2&1\\1&2\end{pmatrix}$, eigenvalues $\lambda = 1, 3$.
>
> Singular values: $\sigma_1 = \sqrt{3} \approx 1.73$, $\sigma_2 = \sqrt{1} = 1.0$.

> [!warning] Common confusion
> Singular values are NOT the same as eigenvalues, even for symmetric matrices. Eigenvalues can be negative; singular values never can. For symmetric PSD matrices (like covariance matrices), the singular values *equal* the eigenvalues. For general matrices, they differ.

## Why this matters for the report

**Q2(d):** The report introduces singular values as $\sigma_i = \sqrt{\lambda_i(X^\top X)}$. The PSD property of $X^\top X$ is what makes this square root valid. This is the algebraic bridge between eigendecomposition and SVD.

**Q2(e):** The power method is applied to the *smaller* of $X^\top X$ or $XX^\top$ to find the top eigenvalue $\lambda_1$; then $\sigma_1 = \sqrt{\lambda_1}$ via the Rayleigh quotient. In Q3, this translates to using the Gram matrix (924×924) rather than the covariance (3401×3401) for the same singular values.

**Q3(h):** The Eckart–Young theorem states the best rank-$k$ approximation error is $\sum_{i>k} \sigma_i^2$ — so singular values directly control how much information is kept or discarded in PCA compression.

## Builds on
- [[svd]]
- [[positive-semi-definite]]
- [[eigenvectors-and-eigenvalues]]

## Leads to
- [[xtx-xxt-duality]]
- [[frobenius-norm]]
- [[eckart-young-theorem]]
