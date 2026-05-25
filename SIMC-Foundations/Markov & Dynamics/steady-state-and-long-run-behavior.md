---
tags:
  - simc
---

# Steady state and long-run behavior

> [!abstract] In one line
> The steady state is where a Markov system eventually settles — the $\lambda=1$ eigenvector survives forever while every mode with $|\lambda|<1$ decays to zero.

## The idea

Decompose the initial population into eigenvectors — think of them as "modes" of the system. Each mode evolves independently: mode $i$ gets multiplied by $\lambda_i^t$ at time $t$. If $|\lambda_i| < 1$, that mode shrinks toward zero. Only the mode with $\lambda = 1$ holds its ground. So in the long run, only the $\lambda=1$ component survives — that is the steady state.

In Q1 there are two modes: the $\lambda=1$ absorbing mode (all type-2) and the $\lambda = 1-\varepsilon$ transient mode (converts between types). The transient mode decays; the absorbing mode is what remains.

## The math

Write the initial state as a sum of eigenvectors:

$$P(0) = c_1 v_1 + c_2 v_2$$

Apply $M^t$ using the eigendecomposition rule $M^t v_i = \lambda_i^t v_i$:

$$P(t) = c_1 \lambda_1^t v_1 + c_2 \lambda_2^t v_2 = c_1 (1)^t v_1 + c_2 (1-\varepsilon)^t v_2$$

As $t \to \infty$, $(1-\varepsilon)^t \to 0$:

$$P(t) \;\xrightarrow{t\to\infty}\; c_1 v_1 = S(0)\begin{pmatrix}0\\1\end{pmatrix} = \begin{pmatrix}0\\S(0)\end{pmatrix}$$

All mass becomes type-2. The final state is the absorbing eigenvector scaled by the total initial population.

**Symbols:**
- $v_1 = (0,1)^\top$ — steady-state (absorbing) eigenvector, eigenvalue $\lambda_1 = 1$
- $v_2 = (1,-1)^\top$ — transient eigenvector, eigenvalue $\lambda_2 = 1-\varepsilon$
- $c_1 = S(0) = p_1(0)+p_2(0)$ — coefficient of the steady-state mode
- $c_2 = p_1(0)$ — coefficient of the transient mode

> [!example] Long-run convergence
> $P(0) = (60, 40)^\top$, $\varepsilon = 0.1$: $S(0) = 100$, $c_1=100$, $c_2=60$.
>
> $P(t) = 100\,(0,1)^\top + 60\,(0.9)^t\,(1,-1)^\top$
>
> At $t=50$: $(0.9)^{50} \approx 0.005$, so $P(50) \approx (0.3,\; 99.7)^\top$.
>
> At $t=200$: $(0.9)^{200} \approx 7\times10^{-10}$. Effectively $(0, 100)^\top$.

> [!warning] Common confusion
> The steady state is **not** the zero vector. Students sometimes confuse "the transient term vanishes" with "everything vanishes." The $c_1 v_1$ term has $\lambda_1 = 1$, so $1^t = 1$ for all $t$ — it never shrinks. What converges to zero is only the $|\lambda|<1$ part.

## Why this matters for the report

Q1(e) asks for the long-run limit of $P(t)$. The answer is $P \to (0, S(0))^\top$: all mass accumulates in type-2. This follows directly from the eigendecomposition (Q1(c)–(d)): the transient mode $(1-\varepsilon)^t \to 0$, leaving only $c_1 v_1$. Q1(g) then asks what changes when $\varepsilon$ varies with time — the answer requires understanding that the transient mode's decay becomes an infinite product rather than a power, which is covered in [[infinite-products-and-convergence]].

## Builds on
- [[matrix-powers-via-eigendecomposition]]
- [[absorbing-state]]
- [[column-stochastic-matrix]]

## Leads to
- [[geometric-decay]]
- [[infinite-products-and-convergence]]
