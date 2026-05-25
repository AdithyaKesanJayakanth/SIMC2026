---
tags:
  - simc
---

# Leader clustering

> [!abstract] In one line
> Leader clustering is a greedy one-pass algorithm: scan points in order, start a new cluster whenever the current point is farther than radius $r$ from every existing cluster centre ("leader").

## The idea

Imagine you're sorting your classmates into friend groups by walking through the room once. You meet the first person — they become the leader of group 1. Every new person you meet, you check: am I within $r$ metres of an existing group? If yes, join it. If no, start a new group and become its leader. You never backtrack.

That's leader clustering. It's not the most powerful algorithm (it's greedy and order-dependent), but it's:
- **O(N · K)** — fast even for thousands of spectra
- **numpy-only** — no sklearn, no library installs
- **interpretable** — one radius parameter with a clear geometric meaning

The radius $r$ controls granularity: small $r$ → many small clusters, large $r$ → fewer big ones. The stable operating range turns out to be surprisingly wide in practice.

```python
import numpy as np

def leader_clustering(Z, r):
    """Z: (N, d) array of points. Returns list of leader indices."""
    leaders = [0]
    for i in range(1, len(Z)):
        dists = np.linalg.norm(Z[leaders] - Z[i], axis=1)
        if np.min(dists) > r:
            leaders.append(i)
    return leaders
```

The function uses [[vector-norm-and-distance|Euclidean distance]] in the projected (score) space.

## The math

**Input:** $N$ points $\{z_1, \dots, z_N\} \subset \mathbb{R}^d$, radius $r > 0$.

**Algorithm:**
1. Initialise: leaders $\mathcal{L} = \{z_1\}$.
2. For each $z_i$ ($i = 2, \dots, N$):
   $$\text{if } \min_{z_\ell \in \mathcal{L}} \|z_i - z_\ell\| > r, \quad \text{then } \mathcal{L} \leftarrow \mathcal{L} \cup \{z_i\}$$
3. Output: $|\mathcal{L}|$ clusters, each centred on its leader.

**Choosing $r$:** calibrate relative to the **median nearest-neighbour spacing** $\delta$ (the typical within-cloud gap):

$$\delta = \operatorname{median}_{i}\min_{j \neq i}\|z_i - z_j\|$$

Stable range: $r \in [6\delta,\, 12\delta]$ — clusters don't merge or fragment as $r$ varies.

- $r \ll \delta$: every point is its own cluster (over-splits)
- $r \gg \delta$: everything merges into one cluster (under-splits)
- $r \in [6\delta, 12\delta]$: robust plateau

> [!example] Tiny concrete example
> Four 1-D points: $z = [0, 1, 5, 6]$, $r = 2$.
> - $z_1 = 0$: no leaders yet → leader.
> - $z_2 = 1$: $|1-0| = 1 < 2$ → joins cluster 1.
> - $z_3 = 5$: $|5-0| = 5 > 2$ → new leader.
> - $z_4 = 6$: $|6-5| = 1 < 2$ → joins cluster 2.
>
> Result: 2 clusters $\{0,1\}$ and $\{5,6\}$. Correct grouping found in one pass.

> [!warning] Common confusion
> Leader clustering is **order-dependent**: shuffling the input can change which points become leaders and how many clusters appear. This is not a bug — it's a known property. For publication-quality results, run multiple shuffles and check that the cluster count stays stable. In Q3(e) the report verifies stability over a range of $r$, not over shuffles, which is a partial but accepted robustness check.

## Why this matters for the report

Q3(e): after projecting the 924 genuine spectra onto the top-4 eigenvectors (scores matrix $Z \in \mathbb{R}^{924 \times 4}$), leader clustering with radius $r$ in the stable band $[6\delta, 12\delta]$ consistently returns **25 clusters**. The report interprets this as ~25 distinct food samples, each with roughly 37 replicate vials — a clean biological story that falls out of a trivial numpy algorithm with no external dependencies. The stability across a 2× range of $r$ is the evidence that 25 is a real structure in the data, not an artefact of the threshold choice.

Q3(f)–(g) then confirm the same 25 clusters emerge from Gram-matrix PCA, cross-validating the result.

## Builds on
- [[vector-norm-and-distance]]
- [[cosine-similarity]]

## Leads to
- [[pca-on-ir-spectra]]
