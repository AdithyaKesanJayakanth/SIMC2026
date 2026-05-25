---
tags:
  - simc
---

# Floating-point precision

> [!abstract] In one line
> Computers store real numbers with ~16 significant decimal digits (64-bit "double"), so every arithmetic result carries a rounding error of about $10^{-16}$ relative to the true value.

## The idea

A real number like $\pi = 3.14159265358979\ldots$ has infinitely many decimal places. A computer's 64-bit float stores only ~15.9 of them. The rest is rounded off. This is not a bug — it is a fundamental physical constraint of finite memory.

The key number to memorise: **machine epsilon** $\varepsilon_\text{mach} \approx 2.2 \times 10^{-16}$. Any two floating-point numbers that differ by less than $\varepsilon_\text{mach}$ times their magnitude are *indistinguishable* to the computer.

This becomes critical when:
1. You claim two independently computed quantities should be equal (numerical verification).
2. An algorithm's correctness depends on distinguishing numbers that are nearly equal (eigenvalue ordering).

```python
import sys
print(sys.float_info.epsilon)   # 2.220446049250313e-16
# Two "equal" numbers up to machine precision:
a = 1.0
b = 1.0 + 1e-17   # b == a in floating point!
print(a == b)     # True — the difference is below epsilon
```

## The math

Conceptual anchor: every floating-point operation introduces a relative error of at most $\varepsilon_\text{mach}$; over many operations, errors can accumulate.

$$
\text{fl}(x) = x (1 + \delta), \quad |\delta| \le \varepsilon_\text{mach} \approx 2.2 \times 10^{-16}
$$

Two computed quantities $a$ and $b$ that should be equal: instead of $a = b$ check:

$$
|a - b| < \varepsilon_\text{tol} \cdot \max(|a|, |b|)
$$

For the numerical checks in the report, $\varepsilon_\text{tol} = 10^{-16}$ is the gold standard (single-operation accuracy). For multi-step algorithms, $10^{-10}$ to $10^{-6}$ is typical.

- $\varepsilon_\text{mach}$ — machine epsilon, $\approx 2.2 \times 10^{-16}$ for 64-bit doubles
- $\text{fl}(x)$ — floating-point representation of $x$
- $\delta$ — relative rounding error, $|\delta| \le \varepsilon_\text{mach}$

> [!example] Tiny concrete example
> In Q1(f), the closed-form solution and the iterated matrix multiplication both compute $P(t)$ for $t=100$ steps. They should give the same result. The report finds they agree to $10^{-16}$ — meaning the difference $|P_\text{closed} - P_\text{iter}|$ is below the rounding floor. This confirms the implementation is correct.
>
> Contrast: if they agreed to only $10^{-6}$, that would suggest a bug or a poorly conditioned matrix.

> [!warning] Common confusion
> "Agreement to $10^{-16}$" does NOT mean the answer is accurate to 16 decimal places in an absolute sense. It means the *two implementations agree with each other* at the machine-precision level — they have the same rounding errors. The result could still be far from the true mathematical answer if the problem is ill-conditioned.

## Why this matters for the report

**Q1(f):** The report's numerical verification that iterated $M^t P(0)$ and the closed-form $c_1 v_1 + c_2(1-\varepsilon)^t v_2$ agree to $10^{-16}$ is the gold standard for confirming a correct implementation. This is the tightest possible check you can make in floating-point arithmetic.

**Q2(c):** In the near-degenerate eigenvalue case, the separation between $|\lambda_1|$ and $|\lambda_2|$ can fall below $\varepsilon_\text{mach}$. At that point, the computer genuinely cannot determine which eigenvalue is larger — the eigenvalue ordering becomes ambiguous and the power method's output is meaningless.

**Q3(c):** The covariance matrix $C$ is PSD in exact arithmetic, but floating-point errors produce tiny negative eigenvalues ($\sim -10^{-16}$). The `np.clip(..., 0, None)` call in Q3(c) corrects these to zero — a standard defensive practice when extracting singular values from a nearly-PSD matrix.

## Builds on
nothing — start here

## Leads to
- [[degenerate-eigenvalues]]
