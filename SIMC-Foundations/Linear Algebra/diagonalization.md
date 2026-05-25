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

## The math

A matrix $A$ with $n$ linearly independent eigenvectors can be written:

$$A = Q \Lambda Q^{-1}$$

For a real symmetric matrix:

$$A = Q \Lambda Q^\top$$

where the factorization holds because $Q^\top Q = I$ (orthonormal columns).

- $Q$ — matrix of eigenvectors as columns: $Q = [v_1 \mid v_2 \mid \cdots \mid v_n]$
- $\Lambda$ — diagonal matrix of eigenvalues: $\Lambda = \mathrm{diag}(\lambda_1, \lambda_2, \ldots, \lambda_n)$
- $Q^{-1}$ (or $Q^\top$ for symmetric) — change back from eigenbasis to standard basis

Two immediate corollaries fall out of the factorization:

$$\operatorname{tr}(A) = \operatorname{tr}(\Lambda) = \sum_i \lambda_i$$

$$\det(A) = \det(\Lambda) = \prod_i \lambda_i$$

> [!example] Tiny concrete example
> Q1's $M = \begin{pmatrix} 1 & 0 \\ \varepsilon & 1-\varepsilon \end{pmatrix}$, $\varepsilon = 0.1$.
>
> Eigenvalues: $\lambda_1 = 1$, $\lambda_2 = 0.9$; eigenvectors $v_1 = (0,1)$, $v_2 = (1,-1)/\sqrt{2}$ (un-normalised is fine here).
>
> $Q = \begin{pmatrix} 0 & 1 \\ 1 & -1 \end{pmatrix}$, $\Lambda = \begin{pmatrix} 1 & 0 \\ 0 & 0.9 \end{pmatrix}$.
>
> $\operatorname{tr}(M) = 1 + (1-\varepsilon) = 1.9 = 1 + 0.9$ ✓ (sum of eigenvalues).

> [!warning] Common confusion
> Not every matrix is diagonalisable — a defective matrix (repeated eigenvalue, too few eigenvectors) cannot be written as $Q\Lambda Q^{-1}$. However, **every real symmetric matrix is always diagonalisable** (Spectral Theorem), which covers covariance matrices, $X^\top X$, and Q1's $M$.

## Why this matters for the report

**Trace = sum of eigenvalues** is used directly in Q3(b): the total variance of the centred IR data equals $\operatorname{tr}(C) = \sum_j \mathrm{Var}_j \approx 7.90$, and because $C = Q\Lambda Q^\top$, this also equals $\sum_i \lambda_i$. The report uses this identity to compute the fraction of variance each principal component explains (Q3(c)'s explained-variance ratio $\lambda_i / \sum_j \lambda_j$).

Diagonalization is also the algebraic foundation for Q1(d)'s closed form and Q2(a)'s power-method proof — see [[matrix-powers-via-eigendecomposition]].

## Builds on
- [[eigenbasis-and-change-of-basis]]
- [[symmetric-matrix]]

## Leads to
- [[matrix-powers-via-eigendecomposition]]
- [[svd]]
