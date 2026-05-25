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

## The math

Conceptual anchor: $\lVert A \rVert_F^2$ is the total variance or energy stored in the matrix, partitioned by singular values.

$$
\lVert A \rVert_F = \sqrt{\sum_{i,j} A_{ij}^2} = \sqrt{\sum_i \sigma_i^2}
$$

For a rank-$k$ approximation $A_k = \sum_{i=1}^k \sigma_i u_i v_i^\top$, the approximation error is:

$$
\lVert A - A_k \rVert_F^2 = \sum_{i > k} \sigma_i^2
$$

- $A_{ij}$ — entry in row $i$, column $j$
- $\sigma_i$ — $i$-th singular value of $A$
- $A_k$ — best rank-$k$ approximation (Eckart–Young)

> [!example] Tiny concrete example
> $A = \begin{pmatrix}1 & 2 \\ 3 & 4\end{pmatrix}$
>
> Entry-wise: $\lVert A \rVert_F = \sqrt{1 + 4 + 9 + 16} = \sqrt{30} \approx 5.48$
>
> Singular values of $A$ are $\sigma_1 \approx 5.465$, $\sigma_2 \approx 0.366$.
>
> Check: $\sqrt{5.465^2 + 0.366^2} = \sqrt{29.87 + 0.13} = \sqrt{30}$ ✓

> [!warning] Common confusion
> The Frobenius norm is NOT the same as the matrix 2-norm (spectral norm). The 2-norm equals $\sigma_1$ (largest singular value) and measures the worst-case stretching. The Frobenius norm measures total energy across all directions. Eckart–Young holds for *both* norms, but the Frobenius version is what the report uses.

## Why this matters for the report

**Q3(h):** The Eckart–Young theorem, invoked in the synthesis section, states that the top-$k$ PCA projection is the *best possible* rank-$k$ approximation in the Frobenius norm — minimising $\lVert \tilde X - \tilde X_k \rVert_F^2 = \sum_{i>k}\sigma_i^2$. The report uses this to justify keeping 8 components: they capture ~55% of total variance (= 55% of $\lVert C \rVert_F^2$), and the remaining $\sum_{i>8}\sigma_i^2$ is the provably minimal achievable error for any rank-8 representation. The Frobenius norm is the exact metric that makes "optimal compression" a precise mathematical statement.

## Builds on
- [[vector-norm-and-distance]]
- [[matrix]]
- [[singular-values]]

## Leads to
- [[eckart-young-theorem]]
