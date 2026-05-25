---
tags:
  - simc
---

# Matrix powers via eigendecomposition

> [!abstract] In one line
> Raising a matrix to the $t$-th power becomes raising each eigenvalue to the $t$-th power — scalar arithmetic, not matrix arithmetic.

## The idea

Multiplying a matrix by itself repeatedly looks expensive. But once you diagonalise — once you know the eigenbasis — it's almost trivial. Each eigenvector component just gets its eigenvalue multiplied in once per step. After $t$ steps, the component along $v_i$ has been multiplied by $\lambda_i$ exactly $t$ times, giving $\lambda_i^t$.

Think of it like compound interest: if you start with £$c_i$ in an account with interest rate $\lambda_i$, after $t$ years you have $c_i \lambda_i^t$. Different accounts, different rates, completely independent.

```python
import numpy as np

eps = 0.1
M = np.array([[1, 0], [eps, 1 - eps]])
vals, Q = np.linalg.eig(M)
Qinv = np.linalg.inv(Q)

def M_power(t):
    # Efficient: scale eigenvalues, no t-fold matrix multiply
    return Q @ np.diag(vals**t) @ Qinv

P0 = np.array([0.4, 0.6])
print(M_power(50) @ P0)       # fast closed form
print(np.linalg.matrix_power(M, 50) @ P0)   # brute force — same answer
```

## The math

For a diagonalisable matrix $A = Q\Lambda Q^{-1}$:

$$A^t = Q \Lambda^t Q^{-1}$$

where $\Lambda^t = \mathrm{diag}(\lambda_1^t, \lambda_2^t, \ldots, \lambda_n^t)$.

Applying to a vector $x = \sum_i c_i v_i$ written in the eigenbasis:

$$A^t x = \sum_i c_i \lambda_i^t v_i$$

- $A^t$ — the matrix multiplied by itself $t$ times
- $\lambda_i^t$ — the $i$-th eigenvalue raised to the $t$-th power (a scalar!)
- $c_i$ — initial coefficient of $x$ along eigenvector $v_i$
- $v_i$ — the $i$-th eigenvector (its direction is unchanged by any power of $A$)

**Why the formula works:** $A^2 = (Q\Lambda Q^{-1})(Q\Lambda Q^{-1}) = Q\Lambda^2 Q^{-1}$ because the $Q^{-1}Q$ in the middle collapses to $I$. The same cancellation repeats $t-1$ times.

> [!example] Tiny concrete example
> Q1 with $\varepsilon = 0.1$, $P(0) = (0.4,\, 0.6)$, $c_1 = 1.0$, $c_2 = 0.4$, $v_1 = (0,1)$, $v_2 = (1,-1)$.
>
> At $t = 20$:
> - $\lambda_1^{20} = 1^{20} = 1$ (steady state, permanent)
> - $\lambda_2^{20} = 0.9^{20} \approx 0.122$ (decaying transient)
>
> $$P(20) = 1.0 \cdot (0,1) + 0.4 \cdot 0.122 \cdot (1,-1) = (0.049,\; 0.951)$$
>
> Brute-force iteration of $M^{20}P(0)$ gives the same answer to floating-point precision.

> [!warning] Common confusion
> The formula $A^t = Q\Lambda^t Q^{-1}$ requires $A$ to be **diagonalisable**. Also, do not confuse $A^t$ (matrix power, $t$ applications of $A$) with $A^\top$ (transpose). Different symbols, completely different operations.

## Why this matters for the report

**Q1(d)** is this formula in full: the closed-form solution $P(t) = c_1 v_1 + c_2 (1-\varepsilon)^t v_2$ is exactly $M^t P(0) = \sum_i c_i \lambda_i^t v_i$ with $\lambda_1 = 1$ and $\lambda_2 = 1 - \varepsilon$. Without this, you could only get $P(t)$ by iterating $M$ numerically $t$ times — no formula, no insight.

**Q2(a)** uses the same engine: the power method's starting vector expands as $x_0 = \sum a_i v_i$, and after $k$ applications of $X$, the expansion becomes $X^k x_0 = \sum a_i \lambda_i^k v_i$. The ratio $\lambda_i^k / \lambda_1^k = (\lambda_i/\lambda_1)^k \to 0$ for $i > 1$, so only the $v_1$ component survives — that is the entire convergence proof for the power method.

## Builds on
- [[diagonalization]]
- [[eigenbasis-and-change-of-basis]]

## Leads to
- [[steady-state-and-long-run-behavior]]
- [[markov-matrix]]
