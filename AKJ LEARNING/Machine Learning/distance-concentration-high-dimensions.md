---
tags:
  - simc
---

# Distance Concentration in High Dimensions

> [!abstract] In one line
> In high dimensions all pairwise distances converge to nearly the same value, so "nearest neighbour" becomes meaningless and noise drowns out every real signal.

## The idea

Imagine you're in a crowd and you want to find your closest friend. In a small room (2D), some people are clearly nearer than others — easy. Now stretch that room into 1000 dimensions. Distances pile up from every axis, and by the time you're done, every person is roughly the same enormous distance from you. Your "nearest friend" is barely closer than a stranger on the far side of the space. The concept of "near" has dissolved.

There are two separate mechanisms that cause this:

**Mechanism 1 — Distance grows with dimension.** Euclidean distance sums squared differences over all $p$ axes. Even if each individual axis contributes tiny random noise, those contributions accumulate. The noise itself pushes every point away from every other.

**Mechanism 2 — Relative contrast collapses.** Even if max and min distances both grow, the *ratio* of their difference to the minimum distance goes to zero. You lose the ability to distinguish "close" from "far."

> [!example] Analogy
> Imagine measuring how loud two songs are, adding one random instrument at a time. Each instrument adds a little noise to both songs. Eventually both songs are so dominated by random noise that you can't tell which was originally louder. The signal is drowned; only the noise remains.

