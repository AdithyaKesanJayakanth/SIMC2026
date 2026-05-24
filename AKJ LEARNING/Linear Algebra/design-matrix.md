---
tags:
  - simc
---

# Design matrix

> [!abstract] In one line
> The design matrix is your data spreadsheet expressed as a single matrix $X$: each row is one sample (a vector of measurements), each column is one feature.

## The idea

Imagine your lab results loaded into a spreadsheet:

| Sample | Wavenumber 1 | Wavenumber 2 | … | Wavenumber 1000 |
|--------|-------------|-------------|---|----------------|
| Mix 1  | 0.42        | 0.87        | … | 0.11           |
| Mix 2  | 0.39        | 0.91        | … | 0.14           |
| …      | …           | …           | … | …              |
| Mix 50 | 0.55        | 0.76        | … | 0.09           |

That spreadsheet *is* the design matrix $X$. There's nothing new here — you're just giving the spreadsheet a name and treating it as a matrix so you can do math on the whole thing at once.

In Python (NumPy) terms:

```python
X = np.zeros((n, p))
# X[i, j] = absorbance of sample i at wavenumber j
# n = number of samples     (rows)
# p = number of wavenumbers (columns)
```

**Key reading:** Row $i$ of $X$ is the full spectrum of sample $i$ — a vector in $p$-dimensional space. The design matrix stacks all $n$ of those sample-vectors.

