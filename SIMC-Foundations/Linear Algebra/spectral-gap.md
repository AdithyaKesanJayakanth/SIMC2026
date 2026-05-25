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

## The math

Conceptual anchor: the spectral gap quantifies how "cleanly separated" the top eigenvalue is from its rivals.

$$
\text{spectral gap} = \left|\frac{\lambda_2}{\lambda_1}\right|, \quad |\lambda_1| > |\lambda_2|
$$

After $k$ power-method iterations, the residual component in direction $v_2$ is suppressed by:

$$
\left(\frac{|\lambda_2|}{|\lambda_1|}\right)^k \to 0 \text{ as } k\to\infty
$$

- $\lambda_1$ — largest-magnitude eigenvalue
- $\lambda_2$ — second-largest-magnitude eigenvalue
- $k$ — number of iterations

> [!example] Tiny concrete example
> $A = \operatorname{diag}(6, 2)$. Spectral gap $= 2/6 = 1/3$.
>
> After 5 iterations the $v_2$ contamination is $(1/3)^5 \approx 0.4\%$ — practically gone.
>
> Now try $A = \operatorname{diag}(6, 5.9)$. Gap $= 5.9/6 \approx 0.98$. After 5 iterations: $(0.98)^5 \approx 90\%$ contamination remains. Convergence is glacial.

> [!warning] Common confusion
> The spectral gap is a *ratio*, not a difference. $\lambda_1=100, \lambda_2=99$ has a huge absolute difference of 1 but a gap ratio of 0.99 — nearly degenerate. The *ratio* determines convergence speed, not the raw separation.

## Why this matters for the report

**Q2(b):** The report defines geometric convergence explicitly in terms of $|\lambda_2/\lambda_1|$ and labels this the spectral gap. A wide gap is stated as the condition for a "fast and stable" power-method run.

**Q3(c):** The IR covariance matrix has $\lambda_1/\lambda_2 \approx 3.5$ (i.e. gap $\approx 0.29$). The report uses this explicitly to argue that the top principal component is strongly dominant, giving the power method reliable fast convergence and confirming there is meaningful low-dimensional structure in the spectra.

## Builds on
- [[eigenvectors-and-eigenvalues]]
- [[power-method]]

## Leads to
- [[convergence-rate-power-method]]
- [[degenerate-eigenvalues]]
