---
tags:
  - simc
---

# Absorbing state

> [!abstract] In one line
> An absorbing state is one you can enter but never leave — once the system reaches it, it stays there forever.

## The idea

Picture a roach motel: things check in but they don't check out. In Q1, type-2 is the roach motel. Every time step, some type-1 converts to type-2, but type-2 never converts back. Eventually everything ends up type-2.

The formal signature: the column of $M$ that corresponds to the absorbing state has a 1 on the diagonal and 0s everywhere else — it maps the state to itself with probability 1.

## The math

An absorbing state $i$ means: **once you're in state $i$, you stay in state $i$**. In matrix terms, the $i$-th column of $M$ is the standard basis vector $e_i$.

For Q1, state 2 (type-2) is absorbing. The second column of $M$ is:

$$M[:,2] = \begin{pmatrix}0\\1\end{pmatrix} = e_2$$

This is exactly $M_{22}=1,\ M_{12}=0$: type-2 stays type-2 with probability 1.

**Connection to eigenvalues:** An absorbing state corresponds to eigenvalue $\lambda = 1$. The eigenvector equation $Mv = v$ says "this state is fixed." For Q1:

$$M\begin{pmatrix}0\\1\end{pmatrix} = \begin{pmatrix}1-\varepsilon & 0\\\varepsilon & 1\end{pmatrix}\begin{pmatrix}0\\1\end{pmatrix} = \begin{pmatrix}0\\1\end{pmatrix}$$

So $v_1 = (0,1)^\top$ is the eigenvector for $\lambda_1 = 1$.

**Symbols:**
- $e_i$ — standard basis vector with a 1 in position $i$
- $\lambda_1 = 1$ — eigenvalue corresponding to the absorbing state
- $v_1 = (0,1)^\top$ — the absorbing eigenvector (all mass in type-2)

> [!example] Spot the absorbing state
> $M = \begin{pmatrix}0.7 & 0 \\ 0.3 & 1\end{pmatrix}$
>
> Column 2: $(0, 1)^\top$ — a 1 on the diagonal, 0 above. State 2 is absorbing.
> Column 1: $(0.7, 0.3)^\top$ — type-1 splits between both states. Not absorbing.
>
> Start at $P(0) = (100, 0)^\top$. After many steps: $P(t) \to (0, 100)^\top$.

> [!warning] Common confusion
> An absorbing state has eigenvalue 1, but **not every eigenvalue-1 state is absorbing**. A system can have $\lambda=1$ as part of a cycle (e.g., a doubly-connected graph where you oscillate). Absorbing specifically means the column is a standard basis vector — a genuine one-way trap, not just a fixed point of a reversible chain.

## Why this matters for the report

Q1(b) identifies the two eigenvalues of $M$: $\lambda_1 = 1$ (the absorbing state, all-type-2 eigenvector $v_1 = (0,1)^\top$) and $\lambda_2 = 1-\varepsilon$ (the transient mode). The absorbing state is what determines where the system ends up in Q1(e): all mass flows into $v_1 = (0,1)^\top$ over time because it is the only eigenvalue that doesn't decay.

## Builds on
- [[markov-matrix]]
- [[eigenvectors-and-eigenvalues]]

## Leads to
- [[steady-state-and-long-run-behavior]]
