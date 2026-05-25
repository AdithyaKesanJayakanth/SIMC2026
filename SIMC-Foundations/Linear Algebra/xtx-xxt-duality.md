---
tags:
  - simc
---

# $X^\top X$ / $XX^\top$ duality

> [!abstract] In one line
> The matrices $X^\top X$ and $XX^\top$ always share the same non-zero eigenvalues — so you can diagonalise whichever one is smaller and get the same answer.

## The idea

For a data matrix $X$ with $N$ rows (samples) and $M$ columns (features), $X^\top X$ is $M \times M$ and $XX^\top$ is $N \times N$. When $N \ll M$ (many features, few samples) the second is dramatically cheaper to diagonalise. The duality theorem says: don't worry — you get the same non-zero eigenvalues either way.

The intuition: $X^\top X$ encodes feature-feature similarity; $XX^\top$ encodes sample-sample similarity. They look completely different, yet they describe the same underlying linear map from opposite sides. Non-zero eigenvalues are an intrinsic property of that map, not of which side you look from.

