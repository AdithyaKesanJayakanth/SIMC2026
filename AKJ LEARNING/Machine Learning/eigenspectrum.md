---
tags:
  - simc
---

# Eigenspectrum (scree plot)

> [!abstract] In one line
> Line up all the eigenvalues from biggest to smallest and look at how fast they fall off — that shape tells you how many directions actually matter, reading the data's intrinsic dimension directly from the graph.

## The idea

After PCA hands you a list of eigenvalues, you have a choice: keep all $p$ components (pointless — you haven't reduced anything) or keep some $k$ (the whole payoff). But how do you pick $k$?

The eigenspectrum answers this visually. Picture a bar chart where the first bar is the tallest, the second a bit shorter, and so on. If the bars drop off a cliff after position 3 and then flatline near zero for the remaining 997 — the data genuinely lives in 3 dimensions. The cliff tells you the intrinsic dimension.

This is the [[manifold-hypothesis]] made quantitative: if the eigenspectrum has a sharp elbow at $k$, the manifold is $k$-dimensional. The near-zero eigenvalues aren't extra information — they're noise.

The plot of $\lambda_i$ vs $i$ is called a **scree plot** (named after the rubble at the foot of a cliff — the flat tail IS the scree).

