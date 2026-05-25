---
tags:
  - simc
---

# Trace equals sum of eigenvalues

> [!abstract] In one line
> The trace of a matrix — the sum of its diagonal entries — always equals the sum of all its eigenvalues, no matter what basis you work in.

## The idea

Imagine you have a covariance matrix whose diagonal entries are the individual variances of each feature. Adding them up gives you the "total spread" in the data. Now PCA reshuffles that spread into a new coordinate system (the eigenvectors). The trace identity says: **the total spread is conserved** — it's just been redistributed into eigenvalues, not lost.

This is the matrix equivalent of "the total amount of water doesn't change when you pour it between containers of different shapes."

## The math

The trace is defined as the sum of diagonal entries of a square matrix. The identity says the trace equals the sum of eigenvalues.

$$\operatorname{tr}(C) = \sum_{i=1}^{M} \lambda_i$$

**Symbol glossary:**
- $C$ — any square $M \times M$ matrix (here, the covariance matrix)
- $\operatorname{tr}(C)$ — trace of $C$: sum of its diagonal entries $C_{11} + C_{22} + \cdots + C_{MM}$
- $\lambda_i$ — the $i$-th eigenvalue of $C$

**Proof sketch (two steps):**

1. **Diagonalization:** If $C = P D P^{-1}$ where $D = \operatorname{diag}(\lambda_1, \ldots, \lambda_M)$, then $\operatorname{tr}(C) = \operatorname{tr}(P D P^{-1})$.
2. **Cyclic property of trace:** $\operatorname{tr}(ABC) = \operatorname{tr}(CAB)$, so $\operatorname{tr}(P D P^{-1}) = \operatorname{tr}(P^{-1} P D) = \operatorname{tr}(D) = \sum_i \lambda_i$.

The cyclic property is the key: it means the result doesn't depend on which basis you use — it is **basis-invariant**.

> [!example] Tiny concrete example
> Let $C = \begin{pmatrix} 3 & 1 \\ 1 & 3 \end{pmatrix}$.
>
> Diagonal sum: $\operatorname{tr}(C) = 3 + 3 = 6$.
>
> Eigenvalues: characteristic equation $(3-\lambda)^2 - 1 = 0 \Rightarrow \lambda = 2$ or $\lambda = 4$.
>
> Sum of eigenvalues: $2 + 4 = 6$. ✓

> [!warning] Common confusion
> People sometimes think $\operatorname{tr}(C) = \sum \lambda_i$ only holds for diagonal or symmetric matrices. It holds for **any** square matrix with well-defined eigenvalues — symmetry just makes the eigenvalues real and the decomposition cleaner.

## Why this matters for the report

**Q3(b)** computes the covariance matrix $C \in \mathbb{R}^{M \times M}$ over the $\tilde{N} = 924$ cleaned spectra. The report states $\operatorname{tr}(C) \approx 7.90$ directly from the diagonal entries (sum of per-feature variances). Then in **Q3(c)**, after running `np.linalg.eigh` to get all eigenvalues, the report checks that $\sum_i \lambda_i \approx 7.90$ as well. These two computations take completely different paths — one never touches eigenvalues, the other never touches the diagonal — yet they must agree exactly. This agreement is used as an **independent sanity check** that the eigendecomposition is correct and no eigenvalues were accidentally dropped or mis-signed.

## Builds on
- [[trace]]
- [[eigenspectrum]]
- [[diagonalization]]

## Leads to
- [[participation-ratio]]
- [[explained-variance-ratio]]
