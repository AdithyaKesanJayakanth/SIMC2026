---
tags:
  - simc
---

# Matrix × vector

> [!abstract] In one line
> Multiplying a matrix by a vector feeds the vector through a transformation machine — each entry of the output is one row's worth of a dot product, and geometrically the arrow gets rotated and/or stretched.

## The idea

Think of a matrix as a function:

```
input vector  →  [MATRIX]  →  output vector
```

The matrix does *something* to the input vector — it might rotate it, scale it, squish it, or flip it — and out comes a new vector. This is the "machine" reading of a matrix from the previous note.

**How the machine works mechanically:** Each row of the matrix "talks to" the input vector and produces one number for the output. Specifically, each output entry is the sum of element-wise products of one matrix row with the input vector. If you've seen the dot product, that's exactly what's happening — more on that in [[dot-product]].

