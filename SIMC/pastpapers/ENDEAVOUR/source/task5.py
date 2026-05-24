"""
Task 5: Likelihood to succeed with noisy patterns [15 points]
==============================================================
This task is primarily theoretical — deriving likelihood expressions for the
Binomial noise model. We also provide computational verification.

NOISE MODEL:
  - Each pixel i has average value mu_i (probability of detecting a photon).
  - Photon count k_i is 0 or 1 (Binomial with n=1, i.e., Bernoulli).
  - P(k_i = 1 | mu_i) = mu_i
  - P(k_i = 0 | mu_i) = 1 - mu_i

MASTER IMAGE:
  - M "outlier" pixels have average value lambda.
  - Remaining (N - M) pixels have average value beta * lambda.
  - Rotation permutes which pixels are outliers.

=====================================================================
SOLUTIONS TO PARTS (a)-(f):
=====================================================================

--- Part (a): L(r=90° | K_{(4)}, mu_{(4)}) ---

Master mu_{(4)} = [lambda, beta*lambda, beta*lambda, beta*lambda]

At r=0°:   pixel order is [lambda, beta*lambda, beta*lambda, beta*lambda]
At r=90°:  pixel order is [beta*lambda, lambda, beta*lambda, beta*lambda]
At r=180°: pixel order is [beta*lambda, beta*lambda, lambda, beta*lambda]
At r=270°: pixel order is [beta*lambda, beta*lambda, beta*lambda, lambda]

Measured pattern K_{(4)} = {1, 0, 0, 0}

For r=90°: the pixel values in order are [beta*lambda, lambda, beta*lambda, beta*lambda]
  L(r=90°) = P(k1=1|beta*lambda) * P(k2=0|lambda) * P(k3=0|beta*lambda) * P(k4=0|beta*lambda)
           = (beta*lambda) * (1-lambda) * (1-beta*lambda)^2

--- Part (b): Ratio L(r=0°) / L(r=90°) ---

  L(r=0°)  = lambda * (1-beta*lambda)^3
  L(r=90°) = beta*lambda * (1-lambda) * (1-beta*lambda)^2

  Ratio = [lambda * (1-beta*lambda)^3] / [beta*lambda * (1-lambda) * (1-beta*lambda)^2]
        = (1-beta*lambda) / [beta * (1-lambda)]

--- Part (c): When does ratio = 1? ---

  (1-beta*lambda) / [beta * (1-lambda)] = 1
  1 - beta*lambda = beta * (1 - lambda)
  1 - beta*lambda = beta - beta*lambda
  1 = beta

  Answer: beta = 1

  This makes intuitive sense: when beta=1, all pixels have the same average
  value lambda, so all orientations are equally likely (no distinguishing feature).

--- Part (d): 16-pixel case, single outlier on edge ---

  Master mu_{(16)} is 4x4 with outlier at position (0,0).
  K_{(16)} = {1, 0, ..., 0} (only first pixel is 1)

  At r=0°:  outlier at position (0,0) → pixel index 0 has value lambda
  At r=90°: outlier at position (0,3) → pixel index 3 has value lambda

  For r=0° (aligned):
    Pixel 0 has mu=lambda, k=1 → contributes lambda
    Pixels 1-15 have k=0:
      - 14 background pixels with mu=beta*lambda → contribute (1-beta*lambda)^14
      - Wait: pixel 3 at r=90° would have lambda, but at r=0° pixel 3 is background.
    So for r=0°: pixel 0 = lambda, pixels 1-15 = beta*lambda
    L(aligned) = lambda * (1-beta*lambda)^15

  For r=90° (misaligned):
    Pixel 0 has mu=beta*lambda (it's a background pixel at r=90°)
    Pixel 3 has mu=lambda (it's the outlier at r=90°), k=0
    All other background pixels have k=0.

    L(misaligned) = beta*lambda * (1-lambda) * (1-beta*lambda)^14

  Ratio = L(aligned)/L(misaligned)
        = [lambda * (1-beta*lambda)^15] / [beta*lambda * (1-lambda) * (1-beta*lambda)^14]
        = (1 - beta*lambda) / [beta * (1 - lambda)]

  Same formula as Part (b)! The 16-pixel single-outlier case gives the
  same likelihood ratio as the 4-pixel case.

--- Part (e): 16-pixel case, THREE outliers (Figure 9) ---

  Now mu_{(16)} has 3 outlier pixels (at specific positions marked in red in Fig 9).
  K_{(16)} has photons at positions matching the r=0° outlier locations.

  At r=0°: all 3 outlier pixels have k=1, all 13 background pixels have k=0
  At r=90°: the 3 measured hits land on some mix of outlier/background positions

  The key insight: at r=0° all 3 hits align with outlier positions.
  At r=90°, how many of the 3 hit positions overlap with the rotated outlier positions?
  This depends on the specific positions of the outliers.

  In general, if at r=90° exactly p of the 3 hit pixels coincide with outlier
  positions and (3-p) are on background positions:

  L(aligned) = lambda^3 * (1-beta*lambda)^13
  L(misaligned) = lambda^p * (beta*lambda)^(3-p) * (1-lambda)^(3-q) * (1-beta*lambda)^(13-3+q+p)

  Wait, let me be more careful. Looking at Figure 9:

  The measured pattern K_{(16)} = {1,0,1,...,1,0,0,0} has 3 ones.
  These 3 positions correspond exactly to the outlier positions at r=0°.

  At r=0° (aligned):
    3 outlier pixels: k=1 each → lambda^3
    13 background pixels: k=0 each → (1-beta*lambda)^13
    L(aligned) = lambda^3 * (1-beta*lambda)^13

  At r=90° (misaligned), from Figure 9, the outlier positions shift.
  Looking at the figure: at r=90°, none of the original hit positions
  are outlier positions (the red squares move to different locations).
  So all 3 hits land on background positions.
    3 hit pixels at background: (beta*lambda)^3
    3 outlier pixels at r=90° with k=0: (1-lambda)^3
    10 remaining background with k=0: (1-beta*lambda)^10

  L(misaligned) = (beta*lambda)^3 * (1-lambda)^3 * (1-beta*lambda)^10

  Ratio = [lambda^3 * (1-beta*lambda)^13] / [(beta*lambda)^3 * (1-lambda)^3 * (1-beta*lambda)^10]
        = [1/(beta^3)] * [(1-beta*lambda)^3 / (1-lambda)^3]
        = [(1-beta*lambda) / (beta*(1-lambda))]^3

  So the ratio is the CUBE of the single-outlier ratio!
  This makes sense: 3 outliers give 3x the discriminating power (in log-likelihood).

--- Part (f): Average log-likelihood expression ---

  Given N pixels total, M outlier pixels (mu=lambda), (N-M) background (mu=beta*lambda).

  For an aligned pattern, expected photon count at:
    - outlier pixel: E[k_i] = lambda
    - background pixel: E[k_i] = beta*lambda

  Average log-likelihood:
    E[ln L] = sum_i E[k_i * ln(mu_i) + (1-k_i) * ln(1-mu_i)]
            = sum over M outlier pixels: lambda*ln(lambda) + (1-lambda)*ln(1-lambda)
            + sum over (N-M) background pixels: beta*lambda*ln(beta*lambda) + (1-beta*lambda)*ln(1-beta*lambda)
            = M * [lambda*ln(lambda) + (1-lambda)*ln(1-lambda)]
            + (N-M) * [beta*lambda*ln(beta*lambda) + (1-beta*lambda)*ln(1-beta*lambda)]

=====================================================================
"""

import numpy as np
import matplotlib.pyplot as plt
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from utils import OUTPUT_DIR


def likelihood_ratio_single_outlier(lam, beta):
    """L(aligned) / L(misaligned) for single outlier (Parts b, d)."""
    return (1 - beta * lam) / (beta * (1 - lam))


def avg_log_likelihood(N, M, lam, beta):
    """Average log-likelihood of an aligned pattern (Part f).

    E[ln L(aligned)] = M * [lambda*ln(lambda) + (1-lambda)*ln(1-lambda)]
                     + (N-M) * [beta*lambda*ln(beta*lambda) + (1-beta*lambda)*ln(1-beta*lambda)]
    """
    eps = 1e-30
    bl = beta * lam

    term_outlier = lam * np.log(lam + eps) + (1 - lam) * np.log(1 - lam + eps)
    term_background = bl * np.log(bl + eps) + (1 - bl) * np.log(1 - bl + eps)

    return M * term_outlier + (N - M) * term_background


def std_log_likelihood(N, M, lam, beta):
    """Standard deviation of log-likelihood of an aligned pattern.

    Each pixel contributes independently. For a Bernoulli pixel with
    probability p, the variance of [k*ln(p) + (1-k)*ln(1-p)] is:
      Var = p*(1-p) * [ln(p) - ln(1-p)]^2 = p*(1-p) * [ln(p/(1-p))]^2

    Total variance = sum over all pixels of individual variances.
    """
    eps = 1e-30

    # Outlier pixels (mu = lambda)
    log_odds_out = np.log((lam + eps) / (1 - lam + eps))
    var_outlier = lam * (1 - lam) * log_odds_out ** 2

    # Background pixels (mu = beta*lambda)
    bl = beta * lam
    log_odds_bg = np.log((bl + eps) / (1 - bl + eps))
    var_background = bl * (1 - bl) * log_odds_bg ** 2

    total_var = M * var_outlier + (N - M) * var_background
    return np.sqrt(total_var)


def monte_carlo_log_likelihood(N, M, lam, beta, n_samples=5000, seed=42):
    """Monte Carlo simulation of log-likelihood for verification."""
    rng = np.random.RandomState(seed)
    eps = 1e-30

    # Master image: M outlier pixels at lambda, (N-M) at beta*lambda
    mu = np.ones(N) * beta * lam
    mu[:M] = lam

    log_likelihoods = []
    for _ in range(n_samples):
        # Generate a pattern
        k = (rng.rand(N) < mu).astype(float)
        # Compute log-likelihood
        ll = np.sum(k * np.log(mu + eps) + (1 - k) * np.log(1 - mu + eps))
        log_likelihoods.append(ll)

    return np.mean(log_likelihoods), np.std(log_likelihoods)


def solve_task5():
    """
    Solve Task 5: generate all theoretical results and verification plots.
    """
    print("\n" + "=" * 60)
    print("  Task 5: Likelihood Theory for Noisy Patterns")
    print("=" * 60)

    # -----------------------------------------------------------------
    # (a) L(r=90° | K_{(4)}, mu_{(4)})
    # -----------------------------------------------------------------
    print("\n--- Part (a) ---")
    print("L(r=90°|K_{(4)},mu_{(4)}) = beta*lambda * (1-lambda) * (1-beta*lambda)^2")

    # -----------------------------------------------------------------
    # (b) Ratio L(0°)/L(90°)
    # -----------------------------------------------------------------
    print("\n--- Part (b) ---")
    print("L(r=0°)/L(r=90°) = (1-beta*lambda) / [beta*(1-lambda)]")

    # Numerical verification
    lam, beta = 0.05, 0.3
    L0 = lam * (1 - beta * lam) ** 3
    L90 = beta * lam * (1 - lam) * (1 - beta * lam) ** 2
    print(f"  Example (lambda={lam}, beta={beta}):")
    print(f"    L(0°) = {L0:.8f}, L(90°) = {L90:.8f}")
    print(f"    Ratio = {L0/L90:.6f}")
    print(f"    Formula = {likelihood_ratio_single_outlier(lam, beta):.6f}")

    # -----------------------------------------------------------------
    # (c) When does ratio = 1? → beta = 1
    # -----------------------------------------------------------------
    print("\n--- Part (c) ---")
    print("Ratio = 1 when beta = 1")
    print("Verification: ratio(lambda=0.05, beta=1.0) =",
          f"{likelihood_ratio_single_outlier(0.05, 1.0):.6f}")

    # -----------------------------------------------------------------
    # (d) 16-pixel, single outlier on edge
    # -----------------------------------------------------------------
    print("\n--- Part (d) ---")
    print("L(aligned)/L(misaligned) = (1-beta*lambda) / [beta*(1-lambda)]")
    print("Same formula as part (b) — single outlier gives same ratio regardless of N.")

    # -----------------------------------------------------------------
    # (e) 16-pixel, three outliers
    # -----------------------------------------------------------------
    print("\n--- Part (e) ---")
    print("L(aligned)/L(misaligned) = [(1-beta*lambda) / (beta*(1-lambda))]^3")
    print("The ratio is the CUBE of the single-outlier ratio.")
    print("More outliers = exponentially better discrimination in log-likelihood.")

    r1 = likelihood_ratio_single_outlier(lam, beta)
    print(f"  Single outlier ratio: {r1:.4f}")
    print(f"  Three outlier ratio:  {r1**3:.4f}")

    # -----------------------------------------------------------------
    # (f) Average log-likelihood and Monte Carlo verification
    # -----------------------------------------------------------------
    print("\n--- Part (f) ---")
    print("E[ln L(aligned)] = M*[lambda*ln(lambda) + (1-lambda)*ln(1-lambda)]")
    print("                  + (N-M)*[beta*lambda*ln(beta*lambda) + (1-beta*lambda)*ln(1-beta*lambda)]")

    # Generate verification plots (Figure 10)
    N = 625  # 25x25 pixels
    M = 25   # ~4% outlier pixels (roughly realistic)

    lambda_values = np.linspace(0.01, 0.10, 50)
    beta_values = [0.1, 0.2, 0.3, 0.4, 0.5]
    colors = ['blue', 'orange', 'green', 'red', 'purple']

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    for beta, color in zip(beta_values, colors):
        # Analytical
        means_analytical = [avg_log_likelihood(N, M, lam, beta) for lam in lambda_values]
        stds_analytical = [std_log_likelihood(N, M, lam, beta) for lam in lambda_values]

        ax1.plot(lambda_values, means_analytical, '-', color=color, linewidth=1.5)
        ax2.plot(lambda_values, stds_analytical, '-', color=color, linewidth=1.5)

        # Monte Carlo (at fewer points)
        mc_lambdas = lambda_values[::5]
        mc_means, mc_stds = [], []
        for lam in mc_lambdas:
            m, s = monte_carlo_log_likelihood(N, M, lam, beta, n_samples=3000)
            mc_means.append(m)
            mc_stds.append(s)

        ax1.scatter(mc_lambdas, mc_means, marker='x', color=color, s=30,
                   label=f"beta = {beta}")
        ax2.scatter(mc_lambdas, mc_stds, marker='x', color=color, s=30,
                   label=f"beta = {beta}")

    ax1.set_xlabel(r"$\lambda$")
    ax1.set_ylabel("mean log-likelihood")
    ax1.legend()
    ax1.set_title("Average log-likelihood")

    ax2.set_xlabel(r"$\lambda$")
    ax2.set_ylabel("std log-likelihood")
    ax2.legend()
    ax2.set_title("Std of log-likelihood")

    fig.suptitle("Task 5(f): Analytical (lines) vs Monte Carlo (crosses)", fontsize=14)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "task5f_log_likelihood.png"), dpi=150, bbox_inches='tight')
    plt.close()
    print("\n  [5f] Saved log-likelihood verification plot.")


if __name__ == "__main__":
    solve_task5()
