---
tags:
  - simc
---

# Cosine similarity

> [!abstract] In one line
> Cosine similarity measures the **angle** between two vectors — pure direction, zero sensitivity to magnitude — so two spectra that differ only in intensity still score 1.0.

## The idea

Imagine two arrows shot from the origin. Dot product cares about both their lengths AND the angle. Cosine similarity strips out the lengths and keeps only the angle part. Two arrows pointing in exactly the same direction score 1.0; perpendicular arrows score 0; opposite arrows score −1.

Why does that matter for spectra? A sample measured at double the concentration gives a spectrum that is numerically twice as large everywhere, but the *shape* is identical. Cosine similarity ignores the scaling and compares shapes — which is exactly what you want when comparing spectral fingerprints.

Contrast with Euclidean distance ([[vector-norm-and-distance]]): distance grows with magnitude, so a double-concentration replicate looks "far" from the original. Cosine similarity correctly calls them twins.

```python
import numpy as np

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
```

## The math

The cosine of the angle $\theta$ between two vectors equals their dot product divided by the product of their norms.

$$\cos(\mathbf{a}, \mathbf{b}) = \frac{\mathbf{a} \cdot \mathbf{b}}{\|\mathbf{a}\|\,\|\mathbf{b}\|}$$

- $\mathbf{a}, \mathbf{b}$ — vectors in $\mathbb{R}^M$ (e.g. two IR spectra, each with $M = 3401$ channels)
- $\mathbf{a} \cdot \mathbf{b}$ — [[dot-product]]: $\sum_j a_j b_j$
- $\|\mathbf{a}\|, \|\mathbf{b}\|$ — [[vector-norm-and-distance|Euclidean norms]]
- Result — a scalar in $[-1, 1]$; $1$ = identical direction, $0$ = orthogonal, $-1$ = opposite

**Scale-free:** replacing $\mathbf{a}$ with $c\mathbf{a}$ (any $c > 0$) leaves the result unchanged — the $c$ cancels top and bottom.

> [!example] Tiny concrete example
> $\mathbf{a} = (3, 4)$, $\mathbf{b} = (6, 8)$ — same direction, double length.
> - $\mathbf{a} \cdot \mathbf{b} = 18 + 32 = 50$
> - $\|\mathbf{a}\| = 5$, $\|\mathbf{b}\| = 10$
> - $\cos = 50 / (5 \times 10) = 1.0$ — perfect match despite different magnitudes.
>
> Now try $\mathbf{a} = (1, 0)$, $\mathbf{b} = (0, 1)$: dot $= 0$, so $\cos = 0$ — orthogonal, no similarity.

> [!warning] Common confusion
> Cosine similarity is **not** a distance; it's a similarity score. If you need a proper metric, convert: $d = 1 - \cos(\mathbf{a},\mathbf{b})$, or use $\arccos$ to get the actual angle in radians. Also, cosine similarity is undefined for zero vectors — always check norms before dividing.

## Why this matters for the report

Q3(d) directly computes cosine similarity to interpret the leading principal component $\mathbf{v}_1$.

The report checks $\cos(\mathbf{v}_1, \text{mean-centred spectrum}) \approx 0.92$ — a high score — showing $\mathbf{v}_1$ strongly aligns with the shape of a typical centred spectrum. Then it checks $\cos(\mathbf{v}_1, \text{raw spectrum}) \approx 0.67$ — much lower. The drop happens because the raw spectrum includes an overall-intensity offset (the mean) that $\mathbf{v}_1$ does **not** encode; $\mathbf{v}_1$ captures contrast between spectral bands, not absolute brightness. Cosine similarity makes this distinction crisp and scale-free — Euclidean distance would have muddied the comparison with irrelevant magnitude differences.

## Builds on
- [[dot-product]]
- [[vector-norm-and-distance]]

## Leads to
- [[leader-clustering]]
- [[pca-on-ir-spectra]]
