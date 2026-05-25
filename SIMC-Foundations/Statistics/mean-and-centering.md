---
tags:
  - simc
---

# Mean and centering

> [!abstract] In one line
> Subtracting each feature's mean from every data point shifts the entire data cloud so its center lands exactly at the origin.

## The idea

You already know the mean: add everything up, divide by $n$. Centering is the next small step — it just moves the data.

Imagine a swarm of bees hovering somewhere in a room. "Centering" the swarm means you teleport the whole swarm so that its center of mass sits exactly at the room's center point. Every bee moves by the same offset; the *shape* of the swarm is unchanged. That's all centering does to a dataset.

Why bother? PCA only cares about **how the data spreads around its center** — it looks for the directions of maximum scatter. If the data cloud isn't centered at the origin, the math picks up a false "direction" toward wherever the cloud is floating. Centering removes that artifact before PCA starts.

