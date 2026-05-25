---
tags:
  - simc
---

# Transpose

> [!abstract] In one line
> Flipping a matrix so its rows become columns and its columns become rows.

## The idea

Imagine printing a matrix on a piece of paper and then rotating it 90° along the main diagonal — every entry that was in row $i$, column $j$ ends up in row $j$, column $i$. That's the transpose.

In NumPy it's just `.T`:

```python
import numpy as np
A = np.array([[1, 2, 3],
              [4, 5, 6]])   # shape (2, 3)
A.T                         # shape (3, 2)
```

If $X$ is your data matrix with rows = samples and columns = features, then $X^\top$ has rows = features and columns = samples. Switching which axis is "rows" is something the report does immediately in Q3 — the file loads transposed.

