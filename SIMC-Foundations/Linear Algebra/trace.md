---
tags:
  - simc
---

# Trace

> [!abstract] In one line
> The trace of a square matrix is the sum of its diagonal entries — a single number that captures something deep about the matrix.

## The idea

Look only at the main diagonal of a square matrix and add those entries up. That's it. But this humble sum turns out to be **basis-invariant**: no matter which coordinate system you express the matrix in, the trace stays the same. It's a genuine property of the linear transformation, not an artifact of how you wrote it down.

One powerful consequence: the trace equals the sum of all eigenvalues. This means you can read off the "total size" of the eigenvalue spectrum from the diagonal entries alone — no eigenvalue computation needed.

```python
import numpy as np
A = np.array([[3, 1],
              [0, 5]])
np.trace(A)   # 3 + 5 = 8  (also = sum of eigenvalues 3 and 5)
```

