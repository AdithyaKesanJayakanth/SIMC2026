---
tags:
  - simc
---

# Orthonormal basis

> [!abstract] In one line
> A set of mutually perpendicular unit vectors that spans a space — the cleanest possible coordinate system.

## The idea

A **basis** is a minimal set of vectors that can reach any point in your space by linear combination. An **orthonormal** basis adds two extra guarantees: every vector in the set has length exactly 1 (unit), and every pair of distinct vectors in the set is perpendicular (orthogonal). Think of the standard $x$-$y$-$z$ axes: unit length, 90° apart, can describe any point in 3D space. That's an orthonormal basis.

Why is this so useful? Because "coordinates in an orthonormal basis" are just dot products — no matrix inverse needed. If you want to know how much of a vector $x$ lies along basis vector $v_i$, you just compute $v_i \cdot x$. The computation is as simple as it gets.

```python
import numpy as np
# Check if columns of V form an orthonormal basis
V = np.linalg.eigh(C)[1]       # eigenvectors of a symmetric matrix
np.allclose(V.T @ V, np.eye(V.shape[1]))   # True if orthonormal
```

