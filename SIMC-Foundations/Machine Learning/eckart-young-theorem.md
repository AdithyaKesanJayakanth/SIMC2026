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

## The math

**Setup:** a matrix $X \in \mathbb{R}^{N \times M}$ with full SVD $X = U \Sigma V^\top$, where $\sigma_1 \ge \sigma_2 \ge \cdots \ge \sigma_r > 0$ are the [[singular-values|singular values]].

**The theorem:** the rank-$k$ truncation

$$X_k = \sum_{i=1}^{k} \sigma_i \mathbf{u}_i \mathbf{v}_i^\top$$

minimises the [[frobenius-norm|Frobenius norm]] of the error over **all** rank-$k$ matrices $B$:

$$\|X - X_k\|_F = \min_{\operatorname{rank}(B) \le k} \|X - B\|_F = \sqrt{\sum_{i > k} \sigma_i^2}$$

**Symbol glossary:**
- $\sigma_i$ — the $i$-th singular value (square root of $i$-th eigenvalue of $X^\top X$)
- $\mathbf{u}_i$ — $i$-th left singular vector (a direction in sample space)
- $\mathbf{v}_i$ — $i$-th right singular vector (a direction in feature space; same as $i$-th PC loading)
- $\|\cdot\|_F$ — [[frobenius-norm]]: $\|A\|_F = \sqrt{\sum_{ij} A_{ij}^2}$, the "total energy" in the matrix
- $\sum_{i > k} \sigma_i^2$ — the discarded energy; this is the squared error of the optimal approximation

The squared error equals the sum of **dropped** squared singular values. Equivalently, the retained energy fraction is $\sum_{i=1}^k \sigma_i^2 / \sum_i \sigma_i^2$ — the explained variance ratio.

**Connection to [[svd]]:** the proof uses the fact that any rank-$k$ matrix lives in a $k$-dimensional subspace, and $U\Sigma V^\top$ already found the best $k$ such dimensions.

> [!example] Tiny concrete example
> $X$ has singular values $\sigma = [10, 6, 3, 1]$. Truncate to $k=2$:
> - Retained energy: $10^2 + 6^2 = 136$
> - Total energy: $100 + 36 + 9 + 1 = 146$
> - Variance kept: $136/146 \approx 93\%$
> - Frobenius error: $\sqrt{9 + 1} = \sqrt{10} \approx 3.16$
>
> The theorem guarantees **no** rank-2 matrix does better than $\sqrt{10}$ error. You can stop searching.

> [!warning] Common confusion
> "Best rank-$k$ approximation" is in **Frobenius norm** (sum of squared entries). The theorem also holds in the spectral norm (largest singular value of the error), but NOT necessarily for other norms. Also: the theorem is about the **matrix** approximation; it doesn't say the $k$ retained components are the most interpretable or the most predictive for a downstream task — just the most energy-efficient.

## Why this matters for the report

Q3(h) and §4 (synthesis): the report concludes that keeping $k^* = 8$ principal components is the right choice for compressing the IR data. Eckart–Young is the justification that lifts this from "seems reasonable" to **provably optimal**.

Concretely: the 924 × 3401 centred data matrix $\tilde{X}$ has $924 \times 3401 \approx 3.14$ million entries. The rank-8 approximation stores $8 \times (924 + 3401) \approx 34{,}600$ numbers — a **425-fold reduction**. The theorem says this is the rank-8 matrix closest to $\tilde{X}$ in Frobenius norm, with squared error $\sum_{i > 8} \sigma_i^2$ corresponding to $\approx 45\%$ of variance discarded (so $\approx 55\%$ retained). No other 8-parameter-per-sample compression scheme can do better at preserving the full spectral dataset.

## Builds on
- [[svd]]
- [[singular-values]]
- [[frobenius-norm]]

## Leads to
- [[dimensionality-reduction]]
- [[principal-component-analysis]]
