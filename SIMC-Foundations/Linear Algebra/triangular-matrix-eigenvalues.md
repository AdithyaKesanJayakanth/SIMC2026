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

## The math

For a lower-triangular matrix $A$ with diagonal entries $A_{11}, A_{22}, \ldots, A_{nn}$:

$$
\det(A - \lambda I) = \prod_{i=1}^{n}(A_{ii} - \lambda) = 0
$$

Therefore the eigenvalues are:

$$
\lambda_i = A_{ii}, \quad i = 1, 2, \ldots, n
$$

This holds for both lower-triangular and upper-triangular matrices.

- $A_{ii}$ — the diagonal entry in row $i$, column $i$
- $\prod$ — product over all $i$ from 1 to $n$

> [!example] Tiny concrete example
> $$M = \begin{pmatrix}1-\varepsilon & 0\\ \varepsilon & 1\end{pmatrix} \quad \text{with } \varepsilon = 0.3$$
> $M$ is lower-triangular (the upper-right entry is 0). Read off the diagonal: eigenvalues are $\lambda_1 = 1$ and $\lambda_2 = 1 - 0.3 = 0.7$.
> Verify with the characteristic equation: $\det\begin{pmatrix}1-\varepsilon-\lambda & 0\\ \varepsilon & 1-\lambda\end{pmatrix} = (1-\varepsilon-\lambda)(1-\lambda) = 0$ ✓

> [!warning] Common confusion
> The shortcut gives eigenvalues, not eigenvectors. To find the eigenvectors you still need to solve $(A - \lambda_i I)v = 0$ for each eigenvalue. For $M$ above, $\lambda = 1$ gives eigenvector $(0,1)^\top$ and $\lambda = 1-\varepsilon$ gives $(1,-1)^\top$ — those require substitution, not just reading the diagonal.

## Why this matters for the report

**Q1(b):** This is the exact shortcut the report uses. The Markov matrix is:

$$
M = \begin{pmatrix}1-\varepsilon & 0\\ \varepsilon & 1\end{pmatrix}
$$

The upper-right entry is 0, making $M$ lower-triangular. The report immediately states $\lambda_1 = 1$, $\lambda_2 = 1-\varepsilon$ without expanding any determinant. This note explains *why* that one-line claim is valid. Every subsequent part of Q1 — the eigenvector decomposition, the closed-form $P(t)$, the long-run behavior — builds on having these two eigenvalues in hand.

## Builds on
- [[determinant-and-characteristic-equation]]
- [[eigenvectors-and-eigenvalues]]

## Leads to
- [[markov-matrix]]
