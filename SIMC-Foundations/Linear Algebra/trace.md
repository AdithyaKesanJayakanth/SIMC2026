---
tags:
  - simc
---

# Trace

> [!abstract] In one line
> The trace of a square matrix is the sum of its diagonal entries — a single number that captures something deep about the matrix.

## The idea

Look only at the main diagonal of a square matrix and add those entries up. That's it. But this humble sum turns out to be **basis-invariant**: no matter which coordinate system you express the matrix in, the trace stays the same. It's a genuine property of the linear transformation, not an artifact of how you wrote it down.

One powerful consequence: the trace equals the sum of all eigenvalues. This means you can read off the "total size" of the eigenvalue spectrum from the diagonal entries alone — no eigenvalue computation needed.

```python
import numpy as np
A = np.array([[3, 1],
              [0, 5]])
np.trace(A)   # 3 + 5 = 8  (also = sum of eigenvalues 3 and 5)
```

## The math

For a square matrix $A \in \mathbb{R}^{n \times n}$, the trace is the sum of diagonal entries:

$$
\operatorname{tr}(A) = \sum_{i=1}^{n} A_{ii}
$$

The key algebraic property is **cyclicity** — you can rotate the matrices inside a trace:

$$
\operatorname{tr}(AB) = \operatorname{tr}(BA)
$$

even though $AB \neq BA$ in general. More generally, $\operatorname{tr}(ABC) = \operatorname{tr}(BCA) = \operatorname{tr}(CAB)$ (cyclic rotation only, not arbitrary reordering).

- $A_{ii}$ — the entry in the $i$-th row and $i$-th column of $A$
- $n$ — size of the square matrix

> [!example] Tiny concrete example
> $$A = \begin{pmatrix}3 & 7\\ 0 & 5\end{pmatrix}$$
> $\operatorname{tr}(A) = 3 + 5 = 8$. The eigenvalues of this upper-triangular matrix are 3 and 5 (diagonal entries), and $3 + 5 = 8$ ✓. Now check cyclicity: let $B = \begin{pmatrix}1&2\\0&1\end{pmatrix}$. $\operatorname{tr}(AB) = \operatorname{tr}\begin{pmatrix}3&13\\0&5\end{pmatrix} = 8$; $\operatorname{tr}(BA) = \operatorname{tr}\begin{pmatrix}3&9\\0&5\end{pmatrix} = 8$ ✓.

> [!warning] Common confusion
> Cyclicity does NOT mean you can freely reorder. $\operatorname{tr}(ABC) = \operatorname{tr}(BCA)$ but $\operatorname{tr}(ABC) \neq \operatorname{tr}(BAC)$ in general. Only cyclic rotations are safe.

## Why this matters for the report

**Q3(b):** After mean-centering, the covariance matrix $C = \frac{1}{N}\tilde{X}^\top\tilde{X}$ is computed. The report states $\operatorname{tr}(C) = \sum \mathrm{Var}_j \approx 7.90$ — the total variance across all 3401 frequency channels. Because trace equals the sum of eigenvalues, this same $7.90$ equals $\sum \lambda_i$, and it is **invariant** under the change to the eigenbasis. The report uses this invariance to verify that explained variance ratios (each $\lambda_i / \sum \lambda_j$) sum to exactly 1.

**Q3(c):** The participation ratio $d_{\text{eff}} = (\sum \lambda_i)^2 / \sum \lambda_i^2$ is computed directly from the eigenvalues — but the numerator $(\sum \lambda_i)^2 = \operatorname{tr}(C)^2$ and denominator $\sum \lambda_i^2 = \operatorname{tr}(C^2)$, both trace quantities.

## Builds on
- [[matrix]]

## Leads to
- [[trace-equals-sum-of-eigenvalues]]
- [[participation-ratio]]
