---
tags:
  - simc
---

# Vector

> [!abstract] In one line
> A vector is an ordered list of numbers — a Python list, or in practice a NumPy array — and geometrically it's an arrow pointing from the origin to a specific spot in space.

## The idea

In Python you'd write:

```python
import numpy as np
x = np.array([2.0, 5.0, 1.0])   # a NumPy array — what you'll use all competition
# a plain list [2.0, 5.0, 1.0] works too, but NumPy gives you the math for free
```

That's a vector. The order matters: position 0 is `2.0`, position 1 is `5.0`, position 2 is `1.0`. Swap them and you get a different vector.

Geometrically, picture each number as a coordinate — the first along the x-axis, the second along the y-axis, and so on. The vector is an arrow that starts at the origin (all zeros) and ends at that specific point. The arrow has a **direction** (which way it points) and a **magnitude** (how long it is).

One row of a data table is a vector. If you measure the height, weight, and temperature of a patient, that one patient is the vector `{height, weight, temperature}`.

