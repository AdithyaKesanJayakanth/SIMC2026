---
tags:
  - simc
---

# Surface-to-Volume Ratio in High Dimensions

> [!abstract] In one line
> In high dimensions a solid object is almost entirely surface — the interior essentially vanishes, so intuitions about "center" and "typical point" completely fail.

## The idea

Picture a peach. Most of it is flesh (interior); the skin is a thin layer you barely notice. Now imagine a 1000-D "peach." The skin has grown to swallow nearly the entire fruit. There is almost no flesh left. The object is all skin, no filling.

This sounds impossible, but it falls directly out of how volume scales with dimension.

Another way to see it: a unit cube in $d$ dimensions has side length 1, but an inscribed ball (touching the middle of each face) has radius $\tfrac{1}{2}$. As $d$ grows, the ball's volume shrinks to zero while the cube's stays 1. All the cube's "mass" ends up in the corners — i.e., at the surface — not near the center.

Consequence for data: if you sample points uniformly from a high-D ball, almost every point lands near the surface. There are essentially no "interior" points. Your intuition about what a "typical" or "average" data point looks like (sitting somewhere in the middle) is wrong.

