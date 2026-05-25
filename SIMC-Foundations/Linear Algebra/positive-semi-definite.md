---
tags:
  - simc
---

# Positive semi-definite

> [!abstract] In one line
> A square matrix is positive semi-definite (PSD) if every "quadratic test" $w^\top A w$ comes out non-negative — it never assigns a negative "energy" to any vector.

## The idea

Picture a bowl: no matter which direction you walk away from the centre, the surface goes flat or upward — never downward. A PSD matrix is the algebraic version of that bowl. Formally, for *every* vector $w$, the scalar $w^\top A w \ge 0$.

The most natural PSD matrices in data science are built by squaring: $X^\top X$ and $XX^\top$ are always PSD, regardless of what $X$ contains. This is why variances are never negative — they're secretly the output of this squaring operation.

