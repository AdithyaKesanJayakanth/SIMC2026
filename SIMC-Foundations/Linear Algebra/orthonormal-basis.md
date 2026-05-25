---
tags:
  - simc
---

# Orthonormal basis

> [!abstract] In one line
> A set of mutually perpendicular unit vectors that spans a space — the cleanest possible coordinate system.

## The idea

A **basis** is a minimal set of vectors that can reach any point in your space by linear combination. An **orthonormal** basis adds two extra guarantees: every vector in the set has length exactly 1 (unit), and every pair of distinct vectors in the set is perpendicular (orthogonal). Think of the standard $x$-$y$-$z$ axes: unit length, 90° apart, can describe any point in 3D space. That's an orthonormal basis.

Why is this so useful? Because "coordinates in an orthonormal basis" are just dot products — no matrix inverse needed. If you want to know how much of a vector $x$ lies along basis vector $v_i$, you just compute $v_i \cdot x$. The computation is as simple as it gets.

```python
import numpy as np
# Check if columns of V form an orthonormal basis
V = np.linalg.eigh(C)[1]       # eigenvectors of a symmetric matrix
np.allclose(V.T @ V, np.eye(V.shape[1]))   # True if orthonormal
```

## The math

Vectors $v_1, v_2, \ldots, v_k$ form an orthonormal set when:

$$
v_i \cdot v_j = \delta_{ij} = \begin{cases}1 & i = j \\ 0 & i \neq j\end{cases}
$$

If they also span the full space (or the subspace of interest), they form an **orthonormal basis**.

The expansion of any vector $x$ in an orthonormal basis is:

$$
x = \sum_{i=1}^{k}(v_i \cdot x)\, v_i
$$

The coordinate along $v_i$ is simply the dot product $v_i \cdot x$. No solving a linear system, no inverting a matrix.

- $\delta_{ij}$ — the Kronecker delta: 1 when $i = j$, 0 otherwise
- $v_i \cdot x$ — the scalar projection of $x$ onto $v_i$ (how much of $x$ points in the $v_i$ direction)

> [!example] Tiny concrete example
> The 2D standard basis $e_1 = (1,0)$, $e_2 = (0,1)$ is orthonormal.
> Now take $x = (3, 4)$. Expansion: $x = (e_1 \cdot x)\,e_1 + (e_2 \cdot x)\,e_2 = 3\,e_1 + 4\,e_2$ ✓.
>
> Another orthonormal basis: $v_1 = (1,1)/\sqrt{2}$, $v_2 = (1,-1)/\sqrt{2}$.
> $v_1 \cdot v_1 = 1$ ✓, $v_2 \cdot v_2 = 1$ ✓, $v_1 \cdot v_2 = 0$ ✓.
> Coordinates of $x=(3,4)$: $v_1 \cdot x = 7/\sqrt{2}$, $v_2 \cdot x = -1/\sqrt{2}$.
> Reconstruct: $(7/\sqrt{2})(1,1)/\sqrt{2} + (-1/\sqrt{2})(1,-1)/\sqrt{2} = (3,4)$ ✓.

> [!warning] Common confusion
> Orthogonal ≠ orthonormal. Orthogonal vectors are perpendicular but may have any length. Orthonormal = orthogonal + unit length. The eigenvectors from `np.linalg.eigh` are returned normalized (unit length), so they are orthonormal. Raw eigenvectors from pen-and-paper solutions are often orthogonal but not yet unit-length.

## Why this matters for the report

**Q1(c)/(d):** The eigenvectors of $M$ in Q1 are $v_1 = (0,1)$ and $v_2 = (1,-1)$, which are orthogonal but not orthonormal (they are not unit vectors). The report writes $P(0) = c_1 v_1 + c_2 v_2$ and solves for the coefficients $c_1, c_2$ by inspection. If the eigenbasis *were* orthonormal, the coefficients would just be dot products. In Q1 they are not, so the coefficients are found by solving the $2\times 2$ system directly.

**Q2(a):** The proof that the power method converges uses the orthonormal eigenbasis of the symmetric matrix $X$. Because the basis is orthonormal, expanding $x_0 = \sum_i (v_i \cdot x_0) v_i$ is clean and the $v_1$ component is guaranteed to be nonzero unless $x_0 \perp v_1$ exactly.

**Q3(e)/(g):** The projection $Z = \tilde{X}V_4$ (scores onto top-4 eigenvectors) is a coordinate change into part of an orthonormal eigenbasis. Because $V_4^\top V_4 = I$, the projection preserves inner products: distances in score space faithfully reflect distances in the original 3401-dimensional space. This is why clustering in score space (Q3e) gives the same 25 clusters as clustering in the full space.

## Builds on
- [[dot-product]]
- [[vector-norm-and-distance]]
- [[vector]]

## Leads to
- [[eigenbasis-and-change-of-basis]]
- [[diagonalization]]
- [[svd]]
