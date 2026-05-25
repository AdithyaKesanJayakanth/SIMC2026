---
tags:
  - simc
---

# Eigenbasis and change of basis

> [!abstract] In one line
> Rewriting any vector as a weighted sum of eigenvectors so the matrix acts as pure scaling on each piece.

## The idea

Imagine you're describing a point in a city. You could use north/east street coordinates — that's the standard basis. Or you could use "distance along the highway" and "distance off the highway" — that's a basis tuned to the road network. If the traffic law only says "highway traffic doubles, side-street traffic doesn't move," then the highway/off-highway description makes the law trivially simple: each direction scales independently.

Eigenvectors are exactly that: the natural coordinates for a matrix $A$. Once you write a vector in terms of eigenvectors, $A$ just multiplies each coordinate by the matching eigenvalue — no mixing, no coupling.

```python
import numpy as np

A = np.array([[1, 0], [1e-2, 1 - 1e-2]])  # Q1's M with ε=0.01
vals, vecs = np.linalg.eig(A)             # eigenbasis

# Write P(0) in the eigenbasis
P0 = np.array([0.4, 0.6])
c = np.linalg.solve(vecs, P0)            # c[i] = coefficient of eigenvector i
print(c)   # → [1.0, 0.4]  (c1 = S(0), c2 = p1(0))
```

