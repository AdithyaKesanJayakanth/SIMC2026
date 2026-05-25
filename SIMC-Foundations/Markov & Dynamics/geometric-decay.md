---
tags:
  - simc
---

# Geometric decay

> [!abstract] In one line
> Geometric decay is what happens when you multiply by the same factor $r \in (0,1)$ at every step — the quantity shrinks by the same *proportion* each time, giving a straight line on a log axis.

## The idea

Fold a piece of paper in half repeatedly. After $t$ folds you have $1/2^t$ of the original thickness. Each fold is the same operation — multiplying by $1/2$. That's geometric decay.

In a Markov chain, every eigenvalue $|\lambda| < 1$ creates a mode that decays geometrically. The transient mode in Q1 multiplies by $(1-\varepsilon)$ every time step. After $t$ steps it has decayed to $(1-\varepsilon)^t$ of its starting size.

The key signature: **linear on a log scale**. If you plot $\ln |c_2 \lambda^t|$ vs $t$, you get slope $\ln \lambda$ — a constant, no matter the time.

```python
import numpy as np
import matplotlib.pyplot as plt

eps = 0.1
t = np.arange(100)
mode = (1 - eps) ** t          # geometric decay

plt.semilogy(t, mode)          # straight line on log-y axis
plt.xlabel("t")
plt.ylabel("transient mode amplitude")
plt.title("Geometric decay: straight line on a log axis")
plt.show()
```

