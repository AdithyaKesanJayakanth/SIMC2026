---
tags:
  - simc
---

# Vector projection

> [!abstract] In one line
> Projecting a vector onto a direction gives its "shadow" on that line — one number that is the coordinate of the point along that axis.

## The idea

Shine a torch straight down onto a ruler lying flat. The shadow of a pencil on the ruler is the pencil's **projection** — it tells you how far along the ruler the pencil "really is" if you ignore the up-down part.

In math: you have a data point $\mathbf{x}$ (a list of $n$ measurements). You want to know how much of that point lies along some direction $\hat{\mathbf{u}}$ (a unit vector). The answer is one number — the **scalar projection**:

```
score = 0
for i in range(n):
    score += x[i] * u_hat[i]   # just a dot product
```

That single number `score` is the new coordinate of $\mathbf{x}$ on the axis defined by $\hat{\mathbf{u}}$.

This is exactly how PCA compresses data: each of the $m$ samples is projected onto the top $k$ principal directions, replacing $n$ original numbers per sample with just $k$ new numbers per sample.

