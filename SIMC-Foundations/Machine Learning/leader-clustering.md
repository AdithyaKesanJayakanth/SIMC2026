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

