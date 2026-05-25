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

