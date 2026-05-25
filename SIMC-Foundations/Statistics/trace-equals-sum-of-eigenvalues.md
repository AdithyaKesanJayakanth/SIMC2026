---
tags:
  - simc
---

# Trace equals sum of eigenvalues

> [!abstract] In one line
> The trace of a matrix — the sum of its diagonal entries — always equals the sum of all its eigenvalues, no matter what basis you work in.

## The idea

Imagine you have a covariance matrix whose diagonal entries are the individual variances of each feature. Adding them up gives you the "total spread" in the data. Now PCA reshuffles that spread into a new coordinate system (the eigenvectors). The trace identity says: **the total spread is conserved** — it's just been redistributed into eigenvalues, not lost.

This is the matrix equivalent of "the total amount of water doesn't change when you pour it between containers of different shapes."

