---
tags:
  - simc
---

# Eckart–Young theorem

> [!abstract] In one line
> The Eckart–Young theorem says the top-$k$ SVD truncation is the **best possible** rank-$k$ approximation of a matrix — no other rank-$k$ matrix is closer in Frobenius norm.

## The idea

Suppose you have a giant matrix (say, 924 spectra × 3401 wavelengths) and you want to summarise it with far fewer numbers. You could try random projections, hand-picked wavelengths, averaging — but the Eckart–Young theorem tells you the mathematically optimal answer: **just keep the top $k$ singular values**.

Think of it like a JPEG compressor that's provably the best compression possible for a given quality setting. When the report keeps $k^* = 8$ principal components, it's not an arbitrary choice or an aesthetic preference — the theorem guarantees that no other 8-dimensional representation of the data matrix loses less information (in the least-squares sense).

This converts PCA from "a heuristic that works in practice" into "provably optimal linear dimensionality reduction."

