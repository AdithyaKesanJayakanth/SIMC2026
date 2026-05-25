---
tags:
  - simc
---

# Positive semi-definite

> [!abstract] In one line
> A square matrix is positive semi-definite (PSD) if every "quadratic test" $w^\top A w$ comes out non-negative — it never assigns a negative "energy" to any vector.

## The idea

Picture a bowl: no matter which direction you walk away from the centre, the surface goes flat or upward — never downward. A PSD matrix is the algebraic version of that bowl. Formally, for *every* vector $w$, the scalar $w^\top A w \ge 0$.

The most natural PSD matrices in data science are built by squaring: $X^\top X$ and $XX^\top$ are always PSD, regardless of what $X$ contains. This is why variances are never negative — they're secretly the output of this squaring operation.

## The math

Conceptual anchor: $w^\top A w$ is the "quadratic form" of $A$; it measures how much $A$ stretches energy in direction $w$.

$$
A \text{ is PSD} \iff w^\top A w \ge 0 \;\forall\, w \iff \text{all eigenvalues of } A \ge 0
$$

For $A = X^\top X$ specifically:

$$
w^\top (X^\top X) w = (Xw)^\top (Xw) = \lVert Xw \rVert^2 \ge 0
$$

- $A$ — the square symmetric matrix being tested
- $w$ — any vector (same dimension as $A$'s rows/columns)
- $\lVert Xw \rVert^2$ — squared length, always $\ge 0$

> [!example] Tiny concrete example
> $X = \begin{pmatrix}1\\2\end{pmatrix}$, so $X^\top X = \begin{pmatrix}1 & 2\end{pmatrix}\begin{pmatrix}1\\2\end{pmatrix} = 5$ (a $1\times1$ matrix).
>
> For any $w \in \mathbb R^1$: $w^\top \cdot 5 \cdot w = 5w^2 \ge 0$. ✓
>
> Eigenvalue of 5 is just 5, which is $\ge 0$. ✓

> [!warning] Common confusion
> PSD does NOT mean all entries are non-negative — entries can be negative. It means the *eigenvalues* are non-negative. Also: PSD allows zero eigenvalues (positive *definite* requires strictly positive eigenvalues).

## Why this matters for the report

**Q2(d):** The report proves that $X^\top X$ is PSD via exactly the chain $w^\top X^\top X w = \lVert Xw \rVert^2 \ge 0$. This single inequality is what guarantees $\sigma_i = \sqrt{\lambda_i}$ makes sense — you can only take a square root of a non-negative number. Without PSD, singular values would be imaginary.

**Q3(b):** The covariance matrix $C = \frac{1}{N}\tilde X^\top \tilde X$ inherits this property. Every diagonal entry (feature variance) and every eigenvalue of $C$ is $\ge 0$. The `np.clip` in Q3(c) exists precisely because floating-point arithmetic can produce tiny negative eigenvalues ($\sim10^{-16}$) on what should be a PSD matrix.

## Builds on
- [[symmetric-matrix]]
- [[eigenvectors-and-eigenvalues]]

## Leads to
- [[xtx-xxt-duality]]
- [[covariance-matrix]]
- [[singular-values]]
