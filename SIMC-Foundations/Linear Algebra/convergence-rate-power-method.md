---
tags:
  - simc
---

# Convergence rate — power method

> [!abstract] In one line
> The power method converges geometrically: each iteration multiplies the error by $|\lambda_2/\lambda_1|$, so the number of steps needed scales as $1/(1-|\lambda_2/\lambda_1|)$.

## The idea

"Geometric convergence" means every step shrinks the error by the same multiplicative factor — like compound interest in reverse. If the ratio $r = |\lambda_2/\lambda_1|$ is 0.5, the error halves every iteration: 50%, 25%, 12.5%, … Reach machine precision in ~50 steps. If $r=0.99$, the error only drops by 1% per step — you need hundreds of steps to see any real progress.

The reason is simple: after $k$ multiplications, the "wrong" eigenvector components shrink by $r^k$ relative to $v_1$. So convergence is purely determined by how small $r$ is.

