---
tags:
  - simc
---

# Spectral gap

> [!abstract] In one line
> The spectral gap is the ratio $|\lambda_2/\lambda_1|$ between the two largest-magnitude eigenvalues — it measures how much the dominant direction stands out from the rest.

## The idea

Imagine a hill surrounded by gently sloping ground. The "spectral gap" is roughly how much taller the hill is compared to the next-tallest feature. If the gap is wide, you can spot the hill instantly; if everything is nearly the same height, you have to squint.

For the power method: starting from a random vector, each multiplication by $A$ amplifies the $v_1$ component by $\lambda_1$ while scaling the $v_2$ component by $\lambda_2$. After $k$ steps the $v_2$ contribution is shrunk by $(\lambda_2/\lambda_1)^k$ relative to $v_1$. Wide gap → that fraction is small → fast convergence.

```python
# Spectral gap for a matrix A
eigvals = np.sort(np.abs(np.linalg.eigvalsh(A)))[::-1]
gap = eigvals[1] / eigvals[0]   # closer to 0 = better separated
```

