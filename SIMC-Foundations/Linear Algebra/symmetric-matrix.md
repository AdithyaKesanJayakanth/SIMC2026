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

## The math

A matrix $A \in \mathbb{R}^{n \times n}$ is symmetric when:

$$
A = A^\top \quad \Longleftrightarrow \quad A_{ij} = A_{ji} \text{ for all } i, j
$$

**Spectral theorem** (the big result): every real symmetric matrix $A$ can be written as:

$$
A = V \Lambda V^\top
$$

where:
- $V$ — an orthogonal matrix whose columns are the eigenvectors ($V^\top V = I$)
- $\Lambda$ — a diagonal matrix of real eigenvalues
- $V^\top = V^{-1}$ because the eigenvectors are orthonormal

- $A_{ij}$ — entry in row $i$, column $j$
- Orthonormal: columns of $V$ satisfy $v_i \cdot v_j = \delta_{ij}$ (1 if $i=j$, 0 otherwise)

> [!example] Tiny concrete example
> $$A = \begin{pmatrix}3 & 1\\ 1 & 3\end{pmatrix}$$
> Check symmetry: $A_{12} = 1 = A_{21}$ ✓.
> Eigenvalues: $\det(A - \lambda I) = (3-\lambda)^2 - 1 = 0 \Rightarrow \lambda = 2, 4$ (both real ✓).
> Eigenvectors: $(1,-1)/\sqrt{2}$ and $(1,1)/\sqrt{2}$ — orthogonal and unit-length ✓.

> [!warning] Common confusion
> Not every matrix with real eigenvalues is symmetric, and not every symmetric-looking pattern guarantees orthogonal eigenvectors for the *non-symmetric* case. The spectral theorem requires genuine symmetry $A = A^\top$. Also: use `np.linalg.eigh` (not `eig`) for symmetric matrices — `eig` can return tiny imaginary parts from floating-point noise.

## Why this matters for the report

**Q3(b):** The covariance matrix $C = \frac{1}{N}\tilde{X}^\top\tilde{X}$ is symmetric because $(X^\top X)^\top = X^\top (X^\top)^\top = X^\top X$. The report exploits this to use `np.linalg.eigh` in Q3(c), which is faster and numerically stabler than the general solver for this $3401 \times 3401$ matrix.

**Q2(d):** The Gram matrix $G = \frac{1}{N}\tilde{X}\tilde{X}^\top$ is also symmetric by the same argument. Both $C$ and $G$ having orthonormal eigenbases is what makes the duality between them (Q3f–g) so clean: the same singular vectors $U, V$ appear in both, just in different roles.

**Q3(c):** Calling `np.linalg.eigh` instead of `np.linalg.eig` is a deliberate choice documented in the report. It's valid precisely because $C$ is symmetric.

## Builds on
- [[transpose]]
- [[matrix]]

## Leads to
- [[positive-semi-definite]]
- [[diagonalization]]
- [[eigenspectrum]]
- [[gram-matrix]]
