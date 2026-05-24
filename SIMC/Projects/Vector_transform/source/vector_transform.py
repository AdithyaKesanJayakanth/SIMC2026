"""
=============================================
  Reversible vector transform (with optional Gaussian noise).

  - translate(vec, p)              : shift vec by displacement p
  - transform(vec, p, k)            : shift vec by k*p (scaled translation)
  - inverse_transform(...)          : undo by shifting by -k*p
  - apply_noise_to_element(x, s)    : multiplicative Gaussian noise, clamped ±5%
  - apply_noise_to_vector(vec, s)   : element-wise noise
  - noisy_transform(vec, p, k, s)   : transform then add per-element noise
=============================================
"""

import random


# ── Translate ────────────────────────────────────────────────────

def translate(vec, p):
    """
    Translate an n-D vector by the displacement vector p.

    Adds p to vec coordinate-by-coordinate. Works in any number of
    dimensions as long as vec and p are the same length.
    """
    out = []
    for i in range(len(vec)):
        out.append(vec[i] + p[i])
    return out


# ── Composed transform and its inverse ───────────────────────────

def transform(vec, p, k):
    """Translate by k*p (scaled translation)."""
    scaled = [k * pi for pi in p]
    return translate(vec, scaled)


def inverse_transform(vec, p, k):
    """Undo transform by translating by -k*p."""
    scaled_neg = [-k * pi for pi in p]
    return translate(vec, scaled_neg)


# ── Gaussian noise (multiplicative, clamped to ±5%) ──────────────

def apply_noise_to_element(x, sigma):
    """
    Multiply |x| by gauss(1, sigma), clamp the result to within ±5%
    of |x|, and restore the original sign.

    Sign is preserved manually (no numpy dependency).
    """
    noise_multiplier = random.gauss(1, sigma)

    upper_bound = 1.05 * abs(x)
    lower_bound = 0.95 * abs(x)

    output = abs(x) * noise_multiplier
    output = min(output, upper_bound)
    output = max(output, lower_bound)

    sign = 1 if x >= 0 else -1
    return float(sign * output)


def apply_noise_to_vector(vec, sigma):
    """Apply Gaussian noise element-wise."""
    return [apply_noise_to_element(x, sigma) for x in vec]


# ── Noisy transform ──────────────────────────────────────────────

def noisy_transform(vec, p, k, sigma):
    """Transform by k*p, then perturb each component with Gaussian noise."""
    return apply_noise_to_vector(transform(vec, p, k), sigma)


# ── Demo ─────────────────────────────────────────────────────────

if __name__ == "__main__":
    v = [0, 0, 0]
    p = [1, 0, 0]
    k = 2

    t = transform(v, p, k)
    r = inverse_transform(t, p, k)

    print(f"Original:    {v}")
    print(f"p, k:        {p}, {k}")
    print(f"Transformed: {t}")
    print(f"Recovered:   {r}")

    random.seed(0)
    nt = noisy_transform([10, -2, 5], [1, 1, 1], 2, sigma=0.02)
    print(f"Noisy([10,-2,5], p=[1,1,1], k=2, σ=0.02): {nt}")
