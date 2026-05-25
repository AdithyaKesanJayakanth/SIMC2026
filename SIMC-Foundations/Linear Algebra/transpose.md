---
tags:
  - simc
---

# Transpose

> [!abstract] In one line
> Flipping a matrix so its rows become columns and its columns become rows.

## The idea

Imagine printing a matrix on a piece of paper and then rotating it 90° along the main diagonal — every entry that was in row $i$, column $j$ ends up in row $j$, column $i$. That's the transpose.

In NumPy it's just `.T`:

```python
import numpy as np
A = np.array([[1, 2, 3],
              [4, 5, 6]])   # shape (2, 3)
A.T                         # shape (3, 2)
```

If $X$ is your data matrix with rows = samples and columns = features, then $X^\top$ has rows = features and columns = samples. Switching which axis is "rows" is something the report does immediately in Q3 — the file loads transposed.

## The math

Entry $(i,j)$ of $A^\top$ equals entry $(j,i)$ of $A$. That is, we reflect across the main diagonal.

$$
(A^\top)_{ij} = A_{ji}
$$

The most important algebraic rule is how the transpose interacts with products — it reverses the order:

$$
(AB)^\top = B^\top A^\top
$$

- $A$ — any $m \times n$ matrix
- $B$ — any $n \times p$ matrix
- $(AB)^\top$ — a $p \times m$ matrix

> [!example] Tiny concrete example
> $$A = \begin{pmatrix}1 & 2\\ 3 & 4\end{pmatrix} \qquad A^\top = \begin{pmatrix}1 & 3\\ 2 & 4\end{pmatrix}$$
> Row 1 of $A$ becomes column 1 of $A^\top$; row 2 becomes column 2.
> Check the product rule: let $B=\begin{pmatrix}5\\6\end{pmatrix}$. Then $AB=\begin{pmatrix}17\\39\end{pmatrix}$ and $(AB)^\top=\begin{pmatrix}17&39\end{pmatrix}$. Also $B^\top A^\top=\begin{pmatrix}5&6\end{pmatrix}\begin{pmatrix}1&3\\2&4\end{pmatrix}=\begin{pmatrix}17&39\end{pmatrix}$. ✓

> [!warning] Common confusion
> Students write $(AB)^\top = A^\top B^\top$ — wrong! The order flips: $(AB)^\top = B^\top A^\top$. Think of it like putting on shoes and socks: you put socks on first, so you take shoes off first when reversing.

## Why this matters for the report

**Q3(a):** The IR data file loads with shape $3401 \times 1000$, but the report notes it is "stored transposed." Taking `.T` turns it into the expected $1000 \times 3401$ (samples × features) form before any analysis.

**Q3(b)/(f):** The covariance matrix $C = \frac{1}{N}\tilde{X}^\top \tilde{X}$ and the Gram matrix $G = \frac{1}{N}\tilde{X}\tilde{X}^\top$ are both built using the transpose. Understanding that $(X^\top X)$ and $(XX^\top)$ are different shapes — but share nonzero eigenvalues (Q2d) — depends entirely on knowing what the transpose does.

## Builds on
- [[matrix]]
- [[vector]]

## Leads to
- [[symmetric-matrix]]
- [[gram-matrix]]
- [[xtx-xxt-duality]]
- [[covariance-matrix]]
