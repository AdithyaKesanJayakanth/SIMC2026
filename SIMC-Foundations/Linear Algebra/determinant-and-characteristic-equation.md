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

## The math

For a $2 \times 2$ matrix the determinant is:

$$
\det\begin{pmatrix}a & b\\ c & d\end{pmatrix} = ad - bc
$$

The **characteristic equation** is obtained by asking: for which $\lambda$ does $(A - \lambda I)$ have no inverse?

$$
\det(A - \lambda I) = 0
$$

Expanding this determinant gives a polynomial in $\lambda$ (degree $n$ for an $n \times n$ matrix). The roots of this polynomial are the eigenvalues.

For a $2 \times 2$ matrix $A = \begin{pmatrix}a & b\\ c & d\end{pmatrix}$:

$$
(a - \lambda)(d - \lambda) - bc = 0 \quad \Longrightarrow \quad \lambda^2 - (a+d)\lambda + (ad - bc) = 0
$$

- $\lambda$ — the eigenvalue (unknown to solve for)
- $I$ — the identity matrix (same size as $A$)
- $A - \lambda I$ — the matrix $A$ with $\lambda$ subtracted from every diagonal entry

> [!example] Tiny concrete example
> $$A = \begin{pmatrix}3 & 1\\ 0 & 2\end{pmatrix}$$
> Characteristic equation: $\det\begin{pmatrix}3-\lambda & 1\\ 0 & 2-\lambda\end{pmatrix} = (3-\lambda)(2-\lambda) - 0 = 0$
> $\Rightarrow \lambda^2 - 5\lambda + 6 = 0 \Rightarrow (\lambda-3)(\lambda-2) = 0$
> Eigenvalues: $\lambda = 3$ and $\lambda = 2$. Notice these are exactly the diagonal entries — because $A$ is triangular (see [[triangular-matrix-eigenvalues]]).

> [!warning] Common confusion
> The characteristic equation finds *eigenvalues* (scalars). To find *eigenvectors* you then substitute each $\lambda$ back into $(A - \lambda I)v = 0$ and solve for $v$. The determinant step only gives you the scalars.

## Why this matters for the report

**Q1(b):** The report reads off the eigenvalues of $M = \begin{pmatrix}1-\varepsilon & 0\\ \varepsilon & 1\end{pmatrix}$ as $\lambda_1 = 1$ and $\lambda_2 = 1 - \varepsilon$. The justification is that $M$ is lower-triangular, so the characteristic equation factors immediately as $(1-\lambda)((1-\varepsilon)-\lambda) = 0$ — no cross terms, no quadratic formula needed. Understanding *why* that shortcut is valid requires knowing that the determinant of a triangular matrix equals the product of its diagonal, so the characteristic equation's roots are exactly the diagonal entries.

## Builds on
- [[matrix]]
- [[eigenvectors-and-eigenvalues]]

## Leads to
- [[triangular-matrix-eigenvalues]]
- [[diagonalization]]
