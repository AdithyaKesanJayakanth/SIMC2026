---
tags:
  - simc
---

# Column-stochastic matrix

> [!abstract] In one line
> A column-stochastic matrix is one whose columns each sum to 1, guaranteeing that total population mass is conserved at every time step.

## The idea

Imagine each column of $M$ as a bucket of paint being poured out. The column says how much goes to each output state. If the fractions in the bucket add up to exactly 1, none is created and none is destroyed — conservation is baked in by construction.

This is precisely why the Q1 matrix works: $\varepsilon$ leaves the type-1 column and lands in the type-2 column. The two fractions $(1-\varepsilon)$ and $\varepsilon$ sum to 1.

```python
import numpy as np

eps = 0.3
M = np.array([[1 - eps, 0],
              [eps,     1]])

# Verify column sums
print(M.sum(axis=0))   # [1. 1.] — both columns sum to 1
```

## The math

The column-stochastic condition is a one-line algebraic statement using the all-ones row vector $\mathbf{1}^\top$:

$$\mathbf{1}^\top M = \mathbf{1}^\top$$

This says: summing down every column of $M$ gives 1. It is the key to proving conservation.

**Proof that $S(t) = S(0)$ for all $t$:**

$$S(t+1) = \mathbf{1}^\top P(t+1) = \mathbf{1}^\top M\,P(t) = \mathbf{1}^\top P(t) = S(t)$$

Each equality is just a substitution; the stochastic condition does all the work.

**Symbols:**
- $\mathbf{1}^\top = (1,1,\ldots,1)$ — row vector of ones
- $M$ — column-stochastic transition matrix
- $S(t) = \mathbf{1}^\top P(t) = \sum_i p_i(t)$ — total population

> [!example] Checking Q1's matrix
> $M = \begin{pmatrix}1-\varepsilon & 0\\\varepsilon & 1\end{pmatrix}$
>
> Column 1 sum: $(1-\varepsilon) + \varepsilon = 1$. ✓
> Column 2 sum: $0 + 1 = 1$. ✓
>
> So $\mathbf{1}^\top M = \mathbf{1}^\top$, and total mass $S = p_1 + p_2$ is conserved.

> [!warning] Common confusion
> **Row-stochastic vs column-stochastic.** Many textbooks define Markov matrices with *rows* summing to 1 and write the update as $P(t+1)^\top = P(t)^\top M$. The two conventions are transposes of each other. Q1 uses the column-stochastic convention with column vectors, so always check which way the multiplication goes before applying a formula from another source.

## Why this matters for the report

Q1(a) asks you to prove that $S = p_1 + p_2$ is conserved. The one-line proof is $\mathbf{1}^\top M = \mathbf{1}^\top$: column-stochastic directly implies conservation. The report derives this by noticing the $\varepsilon$ terms cancel — the column-stochastic identity is exactly what that cancellation *means* in matrix language.

## Builds on
- [[markov-matrix]]
- [[matrix]]

## Leads to
- [[steady-state-and-long-run-behavior]]
- [[absorbing-state]]
