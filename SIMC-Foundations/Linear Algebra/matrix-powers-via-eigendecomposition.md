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

