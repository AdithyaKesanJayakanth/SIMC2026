---
tags:
  - simc
---

# Curse of Sampling

> [!abstract] In one line
> To sample a high-dimensional space at even crude resolution you need exponentially many points — far more than any experiment could ever collect.

## The idea

Suppose you want to cover a 1D line with evenly spaced measurements: 10 bins suffice to get a rough picture. Now cover a 2D square: you need $10 \times 10 = 100$ grid squares. A 3D cube: $10^3 = 1000$ cells. Each time you add one dimension you multiply the count by 10.

For 1000 dimensions: $10^{1000}$ sample points.

The estimated number of atoms in the observable universe is about $10^{80}$. You are short by $10^{920}$ atoms' worth of samples.

This means that for any real dataset — hundreds of IR spectra, thousands at best — your data is *infinitely* sparse compared to the space it nominally lives in. No matter how densely your samples seem packed, the vast majority of the 1000-D space has never been visited and never will be.

> [!example] Analogy
> You want to characterize the taste of every possible pizza by sampling one pizza for each combination of toppings. With 10 toppings and 3 options each (none / light / heavy), you already need $3^{10} = 59{,}049$ pizzas just to cover all combinations at the coarsest resolution. Add 10 more toppings and you need $3^{20} \approx 3.5$ billion. Real IR spectra have ~1000 "topping slots" (wavenumbers). The pizza shop burns down before you finish ordering.

