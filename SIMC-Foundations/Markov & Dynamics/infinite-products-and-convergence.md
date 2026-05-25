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

