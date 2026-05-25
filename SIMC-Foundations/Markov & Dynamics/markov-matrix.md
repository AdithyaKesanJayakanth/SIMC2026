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

## The math

The matrix equation says: the state at time $t+1$ is a linear combination of columns of $M$, weighted by the current state.

$$P(t+1) = M\,P(t)$$

Applying $M$ repeatedly gives the state at any time:

$$P(t) = M^t\,P(0)$$

**Symbols:**
- $P(t) \in \mathbb{R}^n$ — state vector at time $t$ (population counts or fractions)
- $M \in \mathbb{R}^{n \times n}$ — the transition matrix
- $M_{ij}$ — fraction of population in state $j$ that moves to state $i$

For Q1 specifically:

$$M = \begin{pmatrix} 1-\varepsilon & 0 \\ \varepsilon & 1 \end{pmatrix}, \quad \varepsilon \in (0,1)$$

Type-1 shrinks by $\varepsilon$ each step; type-2 gains exactly what type-1 loses. Nothing leaves.

> [!example] One step, concrete numbers
> $P(0) = (80, 20)^\top$, $\varepsilon = 0.2$.
>
> $P(1) = \begin{pmatrix}0.8 & 0\\0.2 & 1\end{pmatrix}\begin{pmatrix}80\\20\end{pmatrix} = \begin{pmatrix}64\\36\end{pmatrix}$
>
> Total: $64 + 36 = 100 = 80 + 20$. Conservation holds.

> [!warning] Common confusion
> The indices: $M_{ij}$ is the fraction flowing **from** $j$ **to** $i$ (column $j$ describes state $j$'s output). Students often flip rows and columns, writing a row-stochastic matrix instead. Q1 uses the column-stochastic convention, so $P$ is a column vector and the update is $M\,P$, not $P^\top M$.

## Why this matters for the report

Q1 is entirely built on this equation. Part (a) uses the column structure to prove conservation. Parts (b)–(e) diagonalise $M$ to get a closed-form $P(t)$. Part (g) extends to a time-varying $M(t)$ where a different matrix is applied each step — the Markov-matrix framework is what makes that generalisation clean.

## Builds on
- [[matrix-vector-multiplication]]
- [[matrix]]

## Leads to
- [[column-stochastic-matrix]]
- [[absorbing-state]]
- [[steady-state-and-long-run-behavior]]
