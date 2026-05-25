---
tags:
  - simc
---

# Geometric decay

> [!abstract] In one line
> Geometric decay is what happens when you multiply by the same factor $r \in (0,1)$ at every step — the quantity shrinks by the same *proportion* each time, giving a straight line on a log axis.

## The idea

Fold a piece of paper in half repeatedly. After $t$ folds you have $1/2^t$ of the original thickness. Each fold is the same operation — multiplying by $1/2$. That's geometric decay.

In a Markov chain, every eigenvalue $|\lambda| < 1$ creates a mode that decays geometrically. The transient mode in Q1 multiplies by $(1-\varepsilon)$ every time step. After $t$ steps it has decayed to $(1-\varepsilon)^t$ of its starting size.

The key signature: **linear on a log scale**. If you plot $\ln |c_2 \lambda^t|$ vs $t$, you get slope $\ln \lambda$ — a constant, no matter the time.

```python
import numpy as np
import matplotlib.pyplot as plt

eps = 0.1
t = np.arange(100)
mode = (1 - eps) ** t          # geometric decay

plt.semilogy(t, mode)          # straight line on log-y axis
plt.xlabel("t")
plt.ylabel("transient mode amplitude")
plt.title("Geometric decay: straight line on a log axis")
plt.show()
```

## The math

Starting from coefficient $c_2$, after $t$ steps the transient mode has amplitude:

$$a(t) = c_2\,(1-\varepsilon)^t$$

For the limit to be zero, we need $|1-\varepsilon| < 1$, which holds for $\varepsilon \in (0, 1)$.

Taking the log: $\ln a(t) = \ln c_2 + t\ln(1-\varepsilon)$. Slope $= \ln(1-\varepsilon) < 0$.

The **half-life** — time to reduce by half — is $t_{1/2} = \ln 2 \,/\, |\ln(1-\varepsilon)|$. For small $\varepsilon$, $\ln(1-\varepsilon) \approx -\varepsilon$, so $t_{1/2} \approx \ln 2\,/\,\varepsilon$.

**Symbols:**
- $\varepsilon \in (0,1)$ — conversion rate; larger $\varepsilon$ = faster decay
- $\lambda_2 = 1-\varepsilon$ — eigenvalue of the transient mode
- $c_2 = p_1(0)$ — initial coefficient of the transient mode

> [!example] How fast does it decay?
> $\varepsilon = 0.05$ (slow conversion): after $t = 100$ steps,
> $(0.95)^{100} = e^{100\ln 0.95} \approx e^{-5.13} \approx 0.006$.
> Still $0.6\%$ left after 100 steps.
>
> $\varepsilon = 0.5$ (fast conversion): after $t = 10$ steps,
> $(0.5)^{10} \approx 0.001$. Essentially gone in 10 steps.

> [!warning] Common confusion
> Geometric decay requires a **constant** base. If $\varepsilon$ changes each step, the product is NOT $(1-\varepsilon)^t$. You cannot just substitute the average $\bar\varepsilon$ and use $\overline{(1-\varepsilon)}^t$ — that gives the wrong answer. This is exactly the trap in Q1(g). When $\varepsilon(t)$ varies, the correct expression is an infinite product $\prod_s (1-\varepsilon(s))$. See [[infinite-products-and-convergence]].

## Why this matters for the report

Q1(d) gives the closed form $P(t) = c_1 v_1 + c_2(1-\varepsilon)^t v_2$. The factor $(1-\varepsilon)^t$ is pure geometric decay — the transient mode amplitude at time $t$. Q1(e) then uses $\lim_{t\to\infty}(1-\varepsilon)^t = 0$ to conclude that $P \to c_1 v_1$. Understanding why this limit is zero (and when it might NOT be zero, as in Q1(g)) is the core of the Markov chain's long-run analysis.

## Builds on
- [[eigenvectors-and-eigenvalues]]

## Leads to
- [[steady-state-and-long-run-behavior]]
- [[infinite-products-and-convergence]]
