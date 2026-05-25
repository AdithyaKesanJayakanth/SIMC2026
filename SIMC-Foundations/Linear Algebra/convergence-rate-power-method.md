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

## The math

Conceptual anchor: the error after $k$ iterations is the size of the non-dominant components relative to $v_1$, which decays exponentially.

Expand the starting vector in the eigenbasis: $x_0 = \sum_i c_i v_i$. After $k$ iterations (before normalisation):

$$
A^k x_0 = c_1 \lambda_1^k v_1 + c_2 \lambda_2^k v_2 + \cdots
$$

Factoring out $\lambda_1^k$:

$$
\frac{A^k x_0}{\lambda_1^k} = c_1 v_1 + c_2 \underbrace{\left(\frac{\lambda_2}{\lambda_1}\right)^k}_{\to 0} v_2 + \cdots
$$

Iteration count to reach error $\varepsilon$ from component $v_i$:

$$
k \sim \frac{\log(1/\varepsilon)}{\log(1/|\lambda_2/\lambda_1|)} \approx \frac{\log(1/\varepsilon)}{1 - |\lambda_2/\lambda_1|}
$$

(the approximation uses $\log(1/r)\approx 1-r$ for $r\approx1$).

- $r = |\lambda_2/\lambda_1|$ — the contraction ratio per step
- $k$ — iteration count
- $\varepsilon$ — target error

> [!example] Tiny concrete example
> $r = |\lambda_2/\lambda_1| = 0.29$ (from Q3's covariance matrix).
>
> Steps to reach $\varepsilon = 10^{-10}$: $k \approx \log(10^{10})/\log(1/0.29) \approx 23/1.24 \approx 19$ steps. Fast!
>
> Compare $r = 0.99$: $k \approx 23/0.01 = 2300$ steps. Extremely slow.

> [!warning] Common confusion
> "Geometric convergence" sounds fast, but the *base* of the geometric decay is $r$. If $r$ is close to 1, the geometry is nearly flat and convergence is painfully slow even though it is technically still geometric.

## Why this matters for the report

**Q2(b):** The report states convergence is geometric at rate $|\lambda_2/\lambda_1|$ and that the iteration count scales as $\sim 1/(1-|\lambda_2/\lambda_1|)$. This is the quantitative justification for why a wide spectral gap matters operationally — it determines how many matrix multiplications you actually have to do.

**Q2(c):** The report uses this formula to explain what happens as the gap closes: when $r \to 1$, the denominator $1-r \to 0$, so the iteration count blows up to infinity. This is the mathematical heart of the degenerate-eigenvalue failure mode.

## Builds on
- [[power-method]]
- [[spectral-gap]]

## Leads to
- [[degenerate-eigenvalues]]
- [[floating-point-precision]]
