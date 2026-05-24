"""
Third dataset generator — translation transform + Gaussian noise.

Differences from generate_dataset_2.py:
- New (private) ground-truth vector (BASE_TRUTH_3).
- Same weighted k sampling (discrete Gaussian centered at k=0).
- Each transformed vector is perturbed component-wise by multiplicative
  Gaussian noise (sigma = 0.02), clamped to ±5%. Output values are floats.

Solver hint: the transform is no longer exactly reversible. The k=0 row is
still the most common output, but instead of a single repeated row you'll
see a tight cluster of nearly identical floats around BASE_TRUTH_3.
"""

import math
import os
import random
import sys

# Pull noise from the sibling Gaussian_blur project.
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, "..", "..", "Gaussian_blur", "source"))

from vector_transform import transform, inverse_transform
from gaussian_blur import apply_noise_tovector  # noqa: E402

try:
    from ground_truth import BASE_TRUTH_3   # private, gitignored
except ImportError:
    BASE_TRUTH_3 = None


# ── Config ───────────────────────────────────────────────────────

N_POINTS    = 400
SEED        = 13
P_VALUES    = [-3, -2, 1, 3, 4, 6]
K_CHOICES   = [-2, -1, 0, 1, 2]
SIGMA_K     = 1.5    # discrete Gaussian width for k sampling
SIGMA_NOISE = 0.02   # multiplicative noise on each output component
DECIMALS    = 4      # decimal places in the CSV


# ── Weighting ────────────────────────────────────────────────────

def gaussian_weights(ks, sigma):
    """Discrete Gaussian weights centered at k=0."""
    return [math.exp(-(k * k) / (2.0 * sigma * sigma)) for k in ks]


# ── Generation ───────────────────────────────────────────────────

def generate_noisy_dataset(base, n, p, k_choices, weights, sigma_noise):
    """Return n (k, noisy_transformed) pairs using weighted random k."""
    rows = []
    for _ in range(n):
        k = random.choices(k_choices, weights=weights, k=1)[0]
        t = apply_noise_tovector(transform(base, p, k), sigma_noise)
        rows.append((k, t))
    return rows


def save_csv(rows, path, dim, decimals=DECIMALS):
    """Save noisy transformed vectors as an aligned CSV (k is hidden)."""
    header = [f"t_{i}" for i in range(dim)]
    formatted = [[f"{v:.{decimals}f}" for v in row[1]] for row in rows]
    width = max(len(s) for row in formatted for s in row)
    width = max(width, max(len(h) for h in header))

    with open(path, "w") as f:
        f.write(", ".join(h.rjust(width) for h in header) + "\n")
        for row_strs in formatted:
            f.write(", ".join(s.rjust(width) for s in row_strs) + "\n")


# ── Main ─────────────────────────────────────────────────────────

if __name__ == "__main__":
    random.seed(SEED)

    dim = len(BASE_TRUTH_3)
    p = [random.choice(P_VALUES) for _ in range(dim)]
    weights = gaussian_weights(K_CHOICES, SIGMA_K)

    rows = generate_noisy_dataset(
        BASE_TRUTH_3, N_POINTS, p, K_CHOICES, weights, SIGMA_NOISE
    )

    here = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.path.join(here, "..", "outputs")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "dataset_3.csv")

    save_csv(rows, out_path, dim=dim)

    counts = {k: 0 for k in K_CHOICES}
    for k, _ in rows:
        counts[k] += 1

    # Approximate reversibility: undo the translation, then measure how far
    # the recovered vector is from the true base (per-component max error).
    max_err = 0.0
    for k, t in rows:
        recovered = inverse_transform(t, p, k)
        for r, b in zip(recovered, BASE_TRUTH_3):
            max_err = max(max_err, abs(r - b))

   
    max_c = max(counts.values()) or 1
    for k in K_CHOICES:
        bar_len = int(40 * counts[k] / max_c)
        print(f"  k={k:>2}  ({counts[k]:>3})  {'*' * bar_len}")
