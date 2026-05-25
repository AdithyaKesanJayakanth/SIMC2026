---
tags:
  - simc
---

# Curse of Dimensionality

> [!abstract] In one line
> Your 2D and 3D intuition is wrong in high dimensions — space becomes so vast and so weird that naive data analysis quietly breaks.

## The idea

You know how a 2D map works: two numbers pin any location, "nearby" means something sensible, and you can cover a city with a modest grid of squares. Now imagine your data has 1000 numbers per point (like one IR spectrum per sample). The "space" those points live in has 1000 dimensions — and it behaves nothing like a city map.

Three specific disasters happen, each strange enough to deserve its own note:

1. **"All skin, no filling"** — objects in high dimensions have almost all their volume jammed into a thin shell at the surface. The center is essentially empty. → [[surface-to-volume-ratio-high-dimensions]]

2. **"Everything is equally far"** — distances pile up as you add axes, and eventually every pair of points is nearly the same large distance apart, making "nearest neighbour" meaningless. → [[distance-concentration-high-dimensions]]

3. **"You can never collect enough data"** — covering the space at any useful resolution requires exponentially many samples, far more than any real experiment can provide. → [[curse-of-sampling]]

Together they mean: if your data actually *lived* in all 1000 dimensions, you could never analyze it. Luckily, real data doesn't — see [[manifold-hypothesis]].

