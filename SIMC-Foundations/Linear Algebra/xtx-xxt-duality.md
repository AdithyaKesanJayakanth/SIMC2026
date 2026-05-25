---
tags:
  - simc
---

# $X^\top X$ / $XX^\top$ duality

> [!abstract] In one line
> The matrices $X^\top X$ and $XX^\top$ always share the same non-zero eigenvalues — so you can diagonalise whichever one is smaller and get the same answer.

## The idea

For a data matrix $X$ with $N$ rows (samples) and $M$ columns (features), $X^\top X$ is $M \times M$ and $XX^\top$ is $N \times N$. When $N \ll M$ (many features, few samples) the second is dramatically cheaper to diagonalise. The duality theorem says: don't worry — you get the same non-zero eigenvalues either way.

The intuition: $X^\top X$ encodes feature-feature similarity; $XX^\top$ encodes sample-sample similarity. They look completely different, yet they describe the same underlying linear map from opposite sides. Non-zero eigenvalues are an intrinsic property of that map, not of which side you look from.

## The math

Conceptual anchor: if a vector $v$ is an eigenvector of $X^\top X$ with eigenvalue $\lambda \ne 0$, then $Xv$ is an eigenvector of $XX^\top$ with the *same* $\lambda$.

**Proof:**

$$
X^\top X \, v = \lambda v \quad (\lambda \ne 0)
$$

Multiply both sides on the left by $X$:

$$
X X^\top (X v) = \lambda (X v)
$$

So $Xv$ is an eigenvector of $XX^\top$ with eigenvalue $\lambda$. The argument reverses (multiply by $X^\top$) to get the other direction. ∎

The zero eigenvalues may differ in count: the larger matrix has more zero eigenvalues to pad out its size.

- $X \in \mathbb R^{N \times M}$ — data matrix
- $X^\top X \in \mathbb R^{M \times M}$ — covariance structure (up to $1/N$)
- $XX^\top \in \mathbb R^{N \times N}$ — Gram / kernel matrix
- $\lambda$ — shared non-zero eigenvalue

> [!example] Tiny concrete example
> $X = \begin{pmatrix}1 & 0 \\ 0 & 2\end{pmatrix}$ (2×2, so both matrices are the same size here)
>
> $X^\top X = \begin{pmatrix}1&0\\0&4\end{pmatrix}$, eigenvalues $\{1, 4\}$.
>
> $XX^\top = \begin{pmatrix}1&0\\0&4\end{pmatrix}$, eigenvalues $\{1, 4\}$. ✓ (same here because $X$ is diagonal)
>
> For a non-square example: $X = \begin{pmatrix}1&2&3\end{pmatrix}$ (1×3). $X^\top X$ is 3×3 with eigenvalue 14 and two 0s. $XX^\top = [14]$ (1×1) with just eigenvalue 14. Non-zero eigenvalue matches.

> [!warning] Common confusion
> The eigenvectors of $X^\top X$ and $XX^\top$ are completely different objects (one lives in feature space, the other in sample space). Only the *eigenvalues* are shared. You cannot directly use a $v_i$ from $X^\top X$ as if it were a $u_i$ from $XX^\top$.

## Why this matters for the report

**Q2(d):** This is the key theoretical result the report proves. The statement "$X^\top X$ and $XX^\top$ share non-zero eigenvalues" is derived explicitly via the left-multiply proof above.

**Q3(f):** The IR data has $N=924$ samples and $M=3401$ features. Diagonalising the covariance $X^\top X$ costs $O(M^3) = O(3401^3)$ operations. Using the Gram matrix $XX^\top$ costs $O(N^3) = O(924^3)$ — about $13.5\times$ cheaper $(= (3401/924)^2)$. The duality guarantees the top-8 eigenvalues agree to $10^{-6}$. Same eigenvectors up to the $X/X^\top$ conversion. Same 25 clusters.

## Builds on
- [[transpose]]
- [[positive-semi-definite]]
- [[singular-values]]

## Leads to
- [[gram-matrix]]
