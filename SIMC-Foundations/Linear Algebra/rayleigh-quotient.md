---
tags:
  - simc
---

# Rayleigh quotient

> [!abstract] In one line
> Once you have an approximate eigenvector, the Rayleigh quotient is the formula that reads off its eigenvalue — it measures how much the matrix stretches that particular direction.

## The idea

The power method gives you a vector $\mathbf{b}$ that (hopefully) points along an eigenvector. But what is the corresponding eigenvalue? You need the stretch factor.

Here's the intuition: if $\mathbf{b}$ is truly an eigenvector, then $C\mathbf{b} = \lambda\mathbf{b}$. Both sides point the same way; the eigenvalue $\lambda$ is just the ratio of their lengths. The Rayleigh quotient computes that ratio cleanly using dot products.

Think of it this way: push $\mathbf{b}$ through the matrix $C$, then measure how much it grew (using a dot product instead of raw length, to handle the direction too).

