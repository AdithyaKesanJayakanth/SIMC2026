---
tags:
  - simc
---

# Infinite products and convergence

> [!abstract] In one line
> When the decay rate itself changes over time, the transient mode's amplitude is a product — not a power — and if the rates sum to a finite total, the product converges to a positive limit rather than zero.

## The idea

Normally geometric decay looks like $(1-\varepsilon)^t$: multiply by the same number $t$ times. But Q1(g) asks what happens when $\varepsilon$ is different at every step. Now you're multiplying a *sequence* of different numbers:

$$(1-\varepsilon_0)(1-\varepsilon_1)(1-\varepsilon_2)\cdots$$

This is an **infinite product**, not a power. Whether it converges to zero or to something positive is a real question — and the answer is non-obvious and surprising.

The key fact: if the individual factors are all in $(0,1)$ but their sum $\sum_s \varepsilon_s < \infty$ (the rates are decreasing fast enough), the product converges to a **positive limit** $\Pi_\infty > 0$. This means the transient mode never fully vanishes — a permanent residue is frozen in.

Contrast with constant $\varepsilon$: then $\sum_s \varepsilon = \infty$, the product $\to 0$, and everything ends up in type-2. Time-varying rates that decay fast enough break this conclusion.

## The math

With time-varying rate $\varepsilon(t) = \varepsilon_0 e^{-t/t_0}$, the transient mode after $T$ steps has amplitude:

$$a(T) = c_2 \prod_{s=0}^{T-1}(1-\varepsilon(s))$$

Taking logs: $\ln a(T) = \ln c_2 + \sum_{s=0}^{T-1}\ln(1-\varepsilon(s))$.

Since $\ln(1-x) \approx -x$ for small $x$:

$$\ln a(T) \approx \ln c_2 - \sum_{s=0}^{T-1}\varepsilon(s)$$

**The convergence test** (analogous to the series-to-product correspondence):

$$\prod_{s=0}^{\infty}(1-\varepsilon(s)) > 0 \iff \sum_{s=0}^{\infty}\varepsilon(s) < \infty$$

For $\varepsilon(s) = \varepsilon_0 e^{-s/t_0}$, the sum is a geometric series:

$$\sum_{s=0}^{\infty}\varepsilon_0 e^{-s/t_0} = \frac{\varepsilon_0}{1-e^{-1/t_0}} < \infty$$

So the product converges to $\Pi_\infty = \exp\!\left(-\sum_s \varepsilon(s)\right) > 0$.

**The residue:** the transient mode freezes at $c_2 \Pi_\infty \neq 0$, meaning type-1 is never fully depleted. There is a permanent nonzero population in the transient mode.

**Symbols:**
- $\varepsilon(s) = \varepsilon_0 e^{-s/t_0}$ — time-varying conversion rate
- $\Pi_\infty = \prod_{s=0}^{\infty}(1-\varepsilon(s))$ — the infinite product limit
- $c_2 \Pi_\infty$ — the frozen residue in the $v_2$ direction
- $t_0$ — timescale over which $\varepsilon$ decays

> [!example] Infinite product vs power — side by side
> $\varepsilon_0 = 0.1$, $t_0 = 10$.
>
> **Constant-rate formula (wrong for this case):** $(1-0.1)^t \to 0$ as $t\to\infty$.
>
> **Correct infinite product:**
> $\sum_s \varepsilon_0 e^{-s/10} = 0.1/(1-e^{-0.1}) \approx 0.1/0.095 \approx 1.05$.
> $\Pi_\infty \approx e^{-1.05} \approx 0.35$.
>
> So the transient mode retains 35% of its initial amplitude — the type-1 residue is $c_2 \times 0.35 \approx 10^{-3}$ for the Q1 parameters (confirmed numerically in Q1(h)).

> [!warning] Common confusion
> **Applying the constant-rate formula to a time-varying system.** When $\varepsilon(t)$ decreases to zero, it is tempting to say "eventually $\varepsilon \approx 0$, so there's essentially no more conversion, so type-1 never fully depletes... but it still approaches zero." Wrong. The correct test is whether $\sum\varepsilon(s)$ is finite, not whether $\varepsilon(s) \to 0$. A rate can go to zero but still have an infinite sum (e.g., $\varepsilon(s) = 1/s$), in which case the product still goes to zero. The exponentially decaying rate in Q1(g) has a *finite* sum — that is the precise reason the residue is nonzero.

## Why this matters for the report

Q1(g) is the hardest part of the question and the one most likely to trip up a team. With $\varepsilon(t) = \varepsilon_0 e^{-t/t_0}$, the report shows that $M(t)$ changes each step but keeps the same eigenvectors, so the transient-mode amplitude accumulates one factor $(1-\varepsilon(s))$ per step. Because $\sum \varepsilon(s) < \infty$, the product $\Pi_\infty > 0$, and the residue $c_2 \Pi_\infty$ is frozen — numerically $\approx 10^{-3}$ (Q1(h)). The classic mistake is writing $(1-\bar\varepsilon)^t$ using some average rate, which incorrectly predicts full convergence to type-2.

## Builds on
- [[geometric-decay]]

## Leads to
- [[steady-state-and-long-run-behavior]]
