---
tags:
  - simc
---

# Markov matrix

> [!abstract] In one line
> A Markov matrix is a square matrix $M$ that moves a population vector one step forward in time: $P(t+1) = M\,P(t)$.

## The idea

Think of a population split into two groups — type-1 and type-2. At every time step, some fraction of type-1 converts to type-2. A Markov matrix encodes those conversion rules: each column says "if the system is in state $j$, what fraction ends up in each state next?"

The key physical intuition: each column is a probability distribution over *where you go next*. Nothing disappears, nothing is created — the total population is conserved, step after step.

```python
import numpy as np

eps = 0.1
M = np.array([[1 - eps, 0],
              [eps,     1]])

P0 = np.array([100.0, 0.0])   # 100 type-1, 0 type-2
P1 = M @ P0                   # one step forward
print(P1)                      # [90. 10.]
```

