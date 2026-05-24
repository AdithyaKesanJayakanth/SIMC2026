# Gaussian Noise on Scalars and Vectors

## What this script does

Despite the folder name, this isn't an image-blur kernel — it simulates **multiplicative Gaussian measurement noise** applied to a single number or each element of a vector, with a hard clamp at ±5% of the original magnitude.

This is the kind of perturbation you'd use to model noisy sensor readings, jittered ground-truth values, or to stress-test a downstream algorithm against small input variations (similar in spirit to how the ENDEAVOUR past-paper tasks ramp up noise across patterns).

---

## The math

For each element $x$, the noisy output $\tilde{x}$ is:

$$
\tilde{x} = \operatorname{sign}(x) \cdot \operatorname{clamp}\!\big( |x| \cdot m,\; 0.95|x|,\; 1.05|x| \big)
\qquad
m \sim \mathcal{N}(1, \sigma^2)
$$

Where:

- $m$ is a **multiplicative noise factor** drawn from a Gaussian centred at 1 with standard deviation $\sigma$. Because the mean is 1 (not 0), the noise scales the value rather than shifting it.
- $\sigma$ controls the spread. With `sigma = 0.02`, ~68% of draws fall in $[0.98, 1.02]$ and ~95% in $[0.96, 1.04]$.
- The **clamp** to $[0.95|x|,\, 1.05|x|]$ caps the perturbation at ±5% even when the Gaussian draw is unusually large. This guarantees a bounded output regardless of $\sigma$.
- The sign of $x$ is reapplied at the end so negative inputs stay negative.

### Edge case: x = 0

If $x = 0$, then $|x| = 0$, the clamp window collapses to $[0, 0]$, and the output is exactly 0 — noise has no effect on zeros. Worth noting if zeros in your data carry meaning.

---

## Implementation walkthrough

### `apply_noise_toelement(x, sigma)`

Operates on a single scalar:

1. Draw a noise multiplier $m$ from `random.gauss(1, sigma)`.
2. Compute the candidate `output = |x| * m`.
3. Clamp into `[0.95|x|, 1.05|x|]` using `min` / `max`.
4. Re-apply the original sign via `np.sign(x)` and cast to `float`.

### `apply_noise_tovector(vec, sigma)`

Loops over the vector and calls `apply_noise_toelement` on each entry, returning a Python list of the noisy values. Each element gets its own independent noise draw.

### Parameters

| Name | Value | Meaning |
|------|-------|---------|
| `sigma` | `0.02` | Std dev of the Gaussian multiplier. ~2% relative noise before clamping. |
| Clamp band | `±5%` | Hard cap on per-element deviation, regardless of $\sigma$. |

---

## Example output

Running the script:

```
Original: 100, Noisy: 100.7421...
Original: [-1, 2, 3, 5, 0], Noisy: [-0.987..., 2.013..., 2.971..., 5.022..., 0.0]
```

Exact numbers vary every run because `random.gauss` is not seeded. Add `random.seed(N)` near the top if you need reproducibility.

---

## Notes / things to think about

- **Naming.** "Gaussian blur" usually refers to a 2D convolution kernel applied to images. This script is a 1D per-element noise injector. Consider renaming the folder to `Gaussian_noise/` to match what the code actually does.
- **Multiplicative vs additive noise.** Multiplicative noise scales with magnitude — small values get small absolute perturbations, large values get large ones. If you want a fixed absolute jitter, switch to `x + random.gauss(0, sigma)` (additive) instead.
- **Sigma vs clamp interaction.** With `sigma = 0.02`, the clamp at ±5% is rarely hit (it's ~2.5σ away). If you raise `sigma`, the clamp will kick in more often and the effective noise distribution becomes a truncated Gaussian, not a true Gaussian.
- **Unused import.** `math` is imported but never used.
- **Reproducibility.** No `random.seed(...)` is set, so each run gives different values. Fine for demos, not fine for unit tests or experimental comparisons.

---

## How to run

```bash
python "Projects/Gaussian_blur/source/gaussian_blur.py"
```

Stdlib + `numpy` only. No plots or files written.
