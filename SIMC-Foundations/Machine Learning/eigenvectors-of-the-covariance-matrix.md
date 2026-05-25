---
tags:
  - simc
---

# Eigenvectors of the Covariance Matrix

> [!abstract] In one line
> When you find the eigenvectors of the covariance matrix, each one points along a direction the data actually spreads, and its eigenvalue tells you exactly how much spread there is in that direction.

## The idea

Imagine a cloud of data points plotted in 2D. The cloud isn't a perfect circle — it's an elongated ellipse tilted at some angle. There's a long axis (the direction the data spreads most) and a short axis (the direction it barely varies).

The eigenvectors of the [[covariance-matrix]] are exactly those axes. They are the skeleton of the data cloud.

Each eigenvector is a direction, and its paired eigenvalue $\lambda$ is a number that says: "the data, measured only along *this* direction, has variance $\lambda$."

- **Biggest eigenvalue → longest axis → most informative direction.** A point's position along this axis tells you the most about it.
- **Smallest eigenvalue → shortest axis → near-flat direction.** Almost nothing interesting happens here; it's mostly noise.
- All eigenvectors are **mutually perpendicular** (orthogonal), so the axes don't overlap or double-count.

Think of it like finding the natural coordinate system that the data itself prefers, instead of the arbitrary x/y/z axes the instrument recorded.

