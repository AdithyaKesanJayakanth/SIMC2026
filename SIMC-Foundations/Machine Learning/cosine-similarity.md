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

