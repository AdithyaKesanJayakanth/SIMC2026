---
tags:
  - simc
---

# Covariance matrix

> [!abstract] In one line
> The covariance matrix is a single square grid that records the variance of every feature and the covariance between every pair — it is the complete description of how your data spreads, and it is what PCA factorizes.

## The idea

You have $p$ features. Each pair of features has a covariance. Instead of keeping $p^2$ separate numbers scattered around, you pack them all into one tidy square grid: the **covariance matrix** $C$.

Think of it like a mileage chart on a road map: rows and columns both label the same set of cities (features), and each cell holds the "distance" (covariance) between the row-city and the column-city. The diagonal cells are the city's distance to itself — which is its variance.

For IR spectra with 1000 wavenumber channels, $C$ is a $1000 \times 1000$ grid. That's one million entries, but only about half a million are unique (because $C_{ij} = C_{ji}$). PCA reduces all of that to a handful of eigenvectors — that's the payoff.

