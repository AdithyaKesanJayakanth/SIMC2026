"""
Second dataset generator — same translation transform, weighted k sampling.

Differences from generate_dataset.py:
- New (private) ground-truth vector (BASE_TRUTH_2).
- Non-uniform sampling: discrete Gaussian centered at k=0.
  So the row corresponding to BASE_TRUTH_2 itself (the k=0 row) is the
  most common output, and rows further from it are rarer.

Solver hint: with weighted data, the most-frequent unique row is the
ground truth. (No more "all rows equally likely" — frequency now leaks
information about which row is the base.)
"""

import math
import os
import random

from vector_transform import transform, inverse_transform

try:
    from ground_truth import BASE_TRUTH_2   # private, gitignored
except ImportError:
    BASE_TRUTH_2 = None


# ── Config ───────────────────────────────────────────────────────

N_POINTS  = 400
SEED      = 7
P_VALUES  = [-3, -2, 1, 3, 4, 6]
K_CHOICES = [-2, -1, 0, 1, 2]
SIGMA     = 1.5   # discrete Gaussian width — smaller = sharper peak at k=0


# ── Weighting ────────────────────────────────────────────────────

def gaussian_weights(ks, sigma):
    """Discrete Gaussian weights centered at k=0."""
    return [math.exp(-(k * k) / (2.0 * sigma * sigma)) for k in ks]


# ── Generation ───────────────────────────────────────────────────

def generate_weighted_dataset(base, n, p, k_choices, weights):
    """Return n (k, transformed) pairs using weighted random k."""
    rows = []
    for _ in range(n):
        k = random.choices(k_choices, weights=weights, k=1)[0]
        t = transform(base, p, k)
        rows.append((k, t))
    return rows


def save_csv(rows, path, dim):
    """Save transformed vectors as a simple aligned CSV (k is hidden)."""
    header = [f"t_{i}" for i in range(dim)]
    all_vals = [str(v) for row in rows for v in row[1]]
    width = max(len(s) for s in all_vals)
    width = max(width, max(len(h) for h in header))

    with open(path, "w") as f:
        f.write(", ".join(h.rjust(width) for h in header) + "\n")
        for row in rows:
            f.write(", ".join(str(v).rjust(width) for v in row[1]) + "\n")


# ── Main ─────────────────────────────────────────────────────────

if __name__ == "__main__":
    random.seed(SEED)

    dim = len(BASE_TRUTH_2)
    p = [random.choice(P_VALUES) for _ in range(dim)]
    weights = gaussian_weights(K_CHOICES, SIGMA)

    rows = generate_weighted_dataset(BASE_TRUTH_2, N_POINTS, p, K_CHOICES, weights)

    here = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.path.join(here, "..", "outputs")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "dataset_2.csv")

    save_csv(rows, out_path, dim=dim)


    counts = {k: 0 for k in K_CHOICES}
    for k, _ in rows:
        counts[k] += 1

    print(f"Base truth   : {BASE_TRUTH_2}")
    print(f"Fixed p      : {p}")
    print(f"k choices    : {K_CHOICES}")
    print(f"sigma        : {SIGMA}")
    print(f"Points       : {len(rows)}")
    print(f"Saved to     : {out_path}")
    max_c = max(counts.values()) or 1
    for k in K_CHOICES:
        bar_len = int(40 * counts[k] / max_c)
        print(f"  k={k:>2}  ({counts[k]:>3})  {'*' * bar_len}")
