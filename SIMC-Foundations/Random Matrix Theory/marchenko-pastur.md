---
tags:
  - simc
---

# Marchenko–Pastur law

> [!abstract] In one line
> For a matrix of pure noise with aspect ratio $\gamma = M/N$, the sample-covariance eigenvalues fill a specific band $[\lambda_-, \lambda_+]$ with known edges — any eigenvalue above $\lambda_+$ is genuine signal, not noise.

## The idea

[[random-matrix-theory-intro]] established that noise has a predictable eigenvalue spectrum. The Marchenko–Pastur law is the exact formula for that spectrum.

Think of it this way: you have a data matrix that is entirely noise — no chemistry, no signal, nothing. You compute its covariance matrix and sort the eigenvalues. The Marchenko–Pastur law says those eigenvalues won't all be zero (they can't be, because the covariance estimator is finitely sampled), and they won't scatter randomly either. They pack into a specific interval $[\lambda_-, \lambda_+]$ with a characteristic arched density shape, like a one-sided hill.

The width of that interval depends on two things: how noisy the data is ($\sigma^2$) and how underdetermined the problem is (the aspect ratio $\gamma = M/N$). More features than samples ($\gamma > 1$) means a wider noise band — more eigenvalues are inflated by sampling error.

The payoff: once you know $\lambda_+$, you count how many eigenvalues of your real covariance matrix exceed it. That count is your signal dimension estimate — derived from a theorem, not eyeballed from a plot.

