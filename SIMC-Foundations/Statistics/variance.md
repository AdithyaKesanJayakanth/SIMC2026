---
tags:
  - simc
---

# Variance

> [!abstract] In one line
> Variance is the average squared distance from the mean — it measures how spread out a single feature is, and PCA hunts for the directions in which variance is largest.

## The idea

You already know variance from probability. Here's the quick recap through a geometric lens: imagine plotting all $n$ values of one feature on a number line. The mean $\bar{x}$ is the center. Variance asks: *on average, how far are the points from that center?* It squares the distances before averaging so that points above and below the mean don't cancel each other out.

Think of variance as the "width" of a distribution. A narrow spike has low variance; a wide spread has high variance.

**The key bridge to PCA:** PCA is essentially a search algorithm. It asks, "If I project all my data onto some direction (a line through the origin), which direction gives the projected points the most spread?" That spread *is* variance. PCA finds the direction of **maximum variance** first, then the direction of maximum remaining variance, and so on. Variance is the exact quantity PCA is maximizing at every step.

