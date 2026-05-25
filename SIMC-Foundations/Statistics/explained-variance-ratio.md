---
tags:
  - simc
---

# Explained variance ratio

> [!abstract] In one line
> The fraction of total data variance that lives along each principal component — a score between 0 and 1 telling you how much "information" each direction holds.

## The idea

PCA rotates your data into a new coordinate system where each axis (principal component) captures as much variance as possible. But how much does each axis actually capture? The explained variance ratio answers: "Out of all the spread in the data, what percentage falls along component $k$?"

Think of it like splitting a pie. The total variance is the whole pie. Each eigenvalue is the size of one slice. The explained variance ratio is that slice expressed as a fraction of the whole.

```python
import numpy as np

# After np.linalg.eigh, eigenvalues in ascending order — flip to descending
lambdas = np.flip(eigenvalues)
ratios = lambdas / lambdas.sum()          # fraction per component
cumulative = np.cumsum(ratios)            # running total
```

