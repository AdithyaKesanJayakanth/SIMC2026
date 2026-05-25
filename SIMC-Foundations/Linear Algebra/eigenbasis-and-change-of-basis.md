---
tags:
  - simc
---

# Eigenbasis and change of basis

> [!abstract] In one line
> Rewriting any vector as a weighted sum of eigenvectors so the matrix acts as pure scaling on each piece.

## The idea

Imagine you're describing a point in a city. You could use north/east street coordinates — that's the standard basis. Or you could use "distance along the highway" and "distance off the highway" — that's a basis tuned to the road network. If the traffic law only says "highway traffic doubles, side-street traffic doesn't move," then the highway/off-highway description makes the law trivially simple: each direction scales independently.

Eigenvectors are exactly that: the natural coordinates for a matrix $A$. Once you write a vector in terms of eigenvectors, $A$ just multiplies each coordinate by the matching eigenvalue — no mixing, no coupling.

```python
import numpy as np

A = np.array([[1, 0], [1e-2, 1 - 1e-2]])  # Q1's M with ε=0.01
vals, vecs = np.linalg.eig(A)             # eigenbasis

# Write P(0) in the eigenbasis
P0 = np.array([0.4, 0.6])
c = np.linalg.solve(vecs, P0)            # c[i] = coefficient of eigenvector i
print(c)   # → [1.0, 0.4]  (c1 = S(0), c2 = p1(0))
```

## The math

Any vector can be decomposed as a weighted sum of eigenvectors — if those eigenvectors span the full space.

$$x = \sum_{i} c_i \, v_i$$

where the coefficients $c_i$ are found by solving $V c = x$ ($V$ is the matrix of eigenvectors as columns).

- $x$ — the vector you want to express
- $v_i$ — the $i$-th eigenvector of matrix $A$
- $c_i$ — the coordinate of $x$ along direction $v_i$ (the "eigenbasis coordinate")
- $V$ — matrix whose columns are eigenvectors $[v_1 \mid v_2 \mid \cdots]$

Then:

$$Ax = A\sum_i c_i v_i = \sum_i c_i \lambda_i v_i$$

Each eigenvector component gets scaled by its eigenvalue $\lambda_i$ — **no cross-mixing**.

> [!example] Tiny concrete example
> Q1's matrix $M$ has eigenvectors $v_1 = (0,1)$, $v_2 = (1,-1)$.
> Start with $P(0) = (0.4, 0.6)$.
>
> Solve $c_1 v_1 + c_2 v_2 = P(0)$:
> $$c_1(0,1) + c_2(1,-1) = (0.4, 0.6)$$
> From the first component: $c_2 = 0.4$.
> From the second: $c_1 - c_2 = 0.6 \Rightarrow c_1 = 1.0 = S(0)$.
>
> So $P(0) = 1.0\cdot v_1 + 0.4\cdot v_2$. The $c_1 = S(0)$ coefficient will survive forever; the $c_2 = p_1(0)$ coefficient decays.

> [!warning] Common confusion
> The eigenvectors $v_i$ must actually span the space — if $A$ is defective (repeated eigenvalue with too few eigenvectors), this decomposition fails. For symmetric and column-stochastic matrices like Q1's $M$, a full eigenbasis always exists.

## Why this matters for the report

**Q1(c)** is this step exactly. The report writes $P(0) = c_1 v_1 + c_2 v_2$ with $c_1 = S(0)$, $c_2 = p_1(0)$. Without the eigenbasis expansion, you cannot separate "the permanent part" ($c_1 v_1$, the absorbing steady state) from "the decaying transient part" ($c_2 v_2$). The decomposition is the hinge that makes the closed-form solution in Q1(d) possible.

**Q2(a)** uses the same idea at scale: the power-method proof expands the starting vector $x_0 = \sum a_i v_i$ in the eigenbasis of $X$. The $v_1$ term dominates because every other coefficient is multiplied by $(\lambda_i/\lambda_1)^k \to 0$.

## Builds on
- [[eigenvectors-and-eigenvalues]]
- [[orthonormal-basis]]
- [[vector]]

## Leads to
- [[diagonalization]]
- [[matrix-powers-via-eigendecomposition]]
