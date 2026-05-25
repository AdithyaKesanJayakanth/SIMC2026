---
tags:
  - simc
---

# Matrix

> [!abstract] In one line
> A matrix is a rectangular grid of numbers — a NumPy 2-D array (a list of lists) — and you can read it three ways: a table of data, a stack of vectors, or a machine that transforms vectors.

## The idea

In Python (NumPy):

```python
import numpy as np
A = np.array([
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0],
])
# A.shape == (2, 3)  →  2 rows, 3 columns
```

That is a matrix. Nothing more exotic than a 2-D array.

**Three lenses — same object, different uses:**

1. **A table of data.** Rows are observations, columns are variables. Exactly like a spreadsheet.

2. **A stack of vectors.** Each row `A[i]` is a row-vector. Each column is a column-vector. You can think of the matrix as either "rows stacked on top of each other" or "columns placed side by side."

3. **A transformation machine.** Feed a vector in, get a (possibly different) vector out. This is the key lens for understanding eigenvectors and PCA. The matrix rotates, stretches, or squishes the input vector to produce the output.

