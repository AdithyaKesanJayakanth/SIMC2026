"""
Dataset generator for the translation transform.

- One fixed "base truth" vector.
- One randomly generated displacement vector p (components from P_VALUES).
- For each of 400 points, k is randomly chosen from K_CHOICES.
- Transformed vector = base + k * p.
- Translation is always reversible: base = transformed - k*p.
"""

import os
import random

from vector_transform import transform, inverse_transform

try:
    from ground_truth import BASE_TRUTH   # private, gitignored
except ImportError:
    BASE_TRUTH = None


# ── Config ───────────────────────────────────────────────────────

N_POINTS     = 400
SEED         = 42
P_VALUES     = [-3, -2, 1, 3, 4, 6]
K_CHOICES    = [-2, -1, 0, 1, 2]


# ── Generation ───────────────────────────────────────────────────

def generate_dataset(base, n, p, k_choices):
    """Return n (k, transformed) pairs using a single fixed p and random k."""
    rows = []
    for _ in range(n):
        k = random.choice(k_choices)
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

    dim = len(BASE_TRUTH)
    p = [random.choice(P_VALUES) for _ in range(dim)]   # one random p

    rows = generate_dataset(BASE_TRUTH, N_POINTS, p, K_CHOICES)

    here = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.path.join(here, "..", "outputs")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "dataset.csv")

    save_csv(rows, out_path, dim=dim)

    ok = all(inverse_transform(t, p, k) == BASE_TRUTH for k, t in rows[:10])

    print(f"Base truth  : {BASE_TRUTH}")
    print(f"Fixed p     : {p}")
    print(f"k choices   : {K_CHOICES}")
    print(f"Points      : {len(rows)}")
    print(f"Saved to    : {out_path}")
    print(f"Reversible  : {ok}")
    print()
    print("First 3 rows (k  ->  transformed):")
    for k, t in rows[:3]:
        print(f"  k={k}  ->  {t}")
