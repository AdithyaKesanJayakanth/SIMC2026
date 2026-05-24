"""
Task 7: Sharing data amongst orientations [20 points]
=======================================================
Given: task7a (row indices) and task7b (col indices) of nonzero entries.
       100,000 patterns, each a flattened 25x25 pixel image.

Goal: Reconstruct the master image (a famous person's face).

KEY CHALLENGE:
  With ~100k patterns split across 4 orientations, each class gets ~25k patterns.
  But the signal is so weak that 25k patterns may not be enough to reconstruct
  clearly. The hint says: "every orientation class must be informed by ALL patterns."

APPROACH — Soft EM with shared data:
  Instead of hard classification (each pattern → one orientation), use soft
  probabilities: P(r_i = angle | pattern_i, master).

  Then the master estimate uses ALL patterns, weighted by their orientation
  probabilities. This effectively quadruples the data per class.

  Algorithm:
  1. Initialize master estimate (naive average).
  2. E-step: For each pattern, compute posterior P(r | pattern, master) for all 4 rotations.
  3. M-step: For each pixel j of the master,
       mu_j = [sum_i sum_r P(r|i) * k_{i,perm_r(j)}] / [sum_i sum_r P(r|i)]
     where perm_r(j) is the pixel index that maps to position j under rotation r.
  4. Repeat until convergence.

  This is a proper EM algorithm where the latent variable is the rotation of each pattern.
"""

import numpy as np
import matplotlib.pyplot as plt
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from utils import flatten_rotation, OUTPUT_DIR


def build_rotation_permutations(L):
    """Precompute the pixel permutation for each rotation.

    For rotation r applied to the master image, pixel j of the master
    maps to pixel perm[r][j] of the flattened rotated image.

    We need the inverse: given a flattened pattern at rotation r,
    pixel j of the pattern corresponds to pixel inv_perm[r][j] of the master.
    """
    N = L * L
    perms = {}
    inv_perms = {}

    for angle in [0, 90, 180, 270]:
        # Create identity vector
        identity = np.arange(N, dtype=float)
        # Flatten a rotation of the identity
        rotated = flatten_rotation(identity, L, angle)
        # perm[angle][j] tells us: pixel j of master → pixel perm[j] of rotated image
        perms[angle] = rotated.astype(int)
        # inv_perm[angle][j]: pixel j of rotated pattern → pixel inv_perm[j] of master
        inv = np.zeros(N, dtype=int)
        inv[rotated.astype(int)] = np.arange(N)
        inv_perms[angle] = inv

    return perms, inv_perms


def soft_em_sparse(row_indices, col_indices, n_patterns, n_pixels, L,
                   n_iter=30, verbose=True):
    """Soft EM algorithm for sparse data with shared information across orientations.

    Uses posterior probabilities instead of hard assignments.
    All patterns contribute to the master estimate (weighted by posteriors).
    """
    eps = 1e-12
    angles = [0, 90, 180, 270]
    N = n_pixels  # L*L

    # Precompute rotation permutations
    perms, inv_perms = build_rotation_permutations(L)

    # Build hits-per-pattern structure
    hits_list = [[] for _ in range(n_patterns)]
    for idx in range(len(row_indices)):
        hits_list[int(row_indices[idx])].append(int(col_indices[idx]))
    hits_list = [np.array(h, dtype=int) for h in hits_list]

    # Precompute number of hits per pattern
    n_hits = np.array([len(h) for h in hits_list])

    # Initialize master: column sums / n_patterns
    col_sums = np.bincount(col_indices.astype(int), minlength=N).astype(float)
    master = np.clip(col_sums / n_patterns, eps, 1 - eps)

    for iteration in range(n_iter):
        # Precompute rotated masters and their log terms
        rotated_masters = {}
        log_ratio = {}  # ln(mu/(1-mu))
        base_ll = {}    # sum of ln(1-mu) over all pixels

        for angle in angles:
            mu_r = np.clip(flatten_rotation(master, L, angle), eps, 1 - eps)
            rotated_masters[angle] = mu_r
            log_ratio[angle] = np.log(mu_r / (1 - mu_r))
            base_ll[angle] = np.sum(np.log(1 - mu_r))

        # E-step: compute log-posteriors for each pattern and rotation
        # (uniform prior → posterior proportional to likelihood)
        posteriors = np.zeros((n_patterns, 4))

        for i in range(n_patterns):
            hits = hits_list[i]
            for r_idx, angle in enumerate(angles):
                ll = base_ll[angle]
                if len(hits) > 0:
                    ll += log_ratio[angle][hits].sum()
                posteriors[i, r_idx] = ll

        # Convert log-likelihoods to probabilities (softmax)
        posteriors -= posteriors.max(axis=1, keepdims=True)  # numerical stability
        posteriors = np.exp(posteriors)
        posteriors /= posteriors.sum(axis=1, keepdims=True)

        # M-step: update master using ALL patterns weighted by posteriors
        # For master pixel j:
        #   numerator = sum_i sum_r P(r|i) * k_{i, perm_r(j)}
        #   denominator = sum_i sum_r P(r|i) = n_patterns * 4... wait no
        #
        # Actually: mu_j = expected fraction of times pixel j is "on" when aligned.
        # For pattern i with posterior P(r|i), if rotation is r, then the pattern's
        # pixel at position perm_r(j) corresponds to master pixel j.
        # So we check: did pattern i have a photon at position perm_r(j)?
        #
        # Efficient approach: for each (rotation, pattern), map hits to master coordinates.

        new_master_num = np.zeros(N)
        new_master_den = np.zeros(N)

        for r_idx, angle in enumerate(angles):
            # For this rotation, the inverse permutation maps pattern pixels → master pixels
            inv_perm = inv_perms[angle]

            # Weight for each pattern at this rotation
            weights = posteriors[:, r_idx]  # (n_patterns,)

            # Total weight contributed to denominator
            new_master_den += weights.sum()

            # For each pattern, its hits map to master coordinates via inv_perm
            for i in range(n_patterns):
                w = weights[i]
                if w < 1e-10:
                    continue
                hits = hits_list[i]
                if len(hits) > 0:
                    master_pixels = inv_perm[hits]
                    # Add weighted contributions
                    np.add.at(new_master_num, master_pixels, w)

        new_master = np.clip(new_master_num / (new_master_den + eps), eps, 1 - eps)

        # Check convergence
        change = np.max(np.abs(new_master - master))
        master = new_master

        if verbose:
            # Hard assignments for monitoring
            hard_labels = np.array([angles[idx] for idx in np.argmax(posteriors, axis=1)])
            entropy = -np.sum(posteriors * np.log(posteriors + eps), axis=1).mean()
            print(f"  Soft EM iter {iteration+1:2d}: max change={change:.6f}, "
                  f"avg entropy={entropy:.4f}, "
                  f"hard counts={[int(np.sum(hard_labels==a)) for a in angles]}")

        if change < 1e-6 and iteration > 2:
            if verbose:
                print("  Converged!")
            break

    # Final hard labels for reporting
    hard_labels = np.array([angles[idx] for idx in np.argmax(posteriors, axis=1)])
    return hard_labels, master, posteriors


def solve_task7(task7a, task7b):
    """
    Solve Task 7 completely.

    Parameters
    ----------
    task7a : ndarray — row indices of nonzero entries
    task7b : ndarray — column indices of nonzero entries
    """
    n_pixels = 625  # 25x25
    L = 25

    n_patterns = int(task7a.max()) + 1
    print(f"\nTask 7: {n_patterns} patterns, {L}x{L} pixels (sparse format)")
    print(f"  Total nonzero entries: {len(task7a)}")
    print(f"  Avg photons per pattern: {len(task7a)/n_patterns:.3f}")

    # -----------------------------------------------------------------
    # (a) Reconstruct using soft EM (sharing data across orientations)
    # -----------------------------------------------------------------
    print("\n  [7a] Running Soft EM (sharing data across all orientations)...")
    labels, master, posteriors = soft_em_sparse(
        task7a, task7b, n_patterns, n_pixels, L,
        n_iter=30, verbose=True)

    # Orientation counts
    for angle in [0, 90, 180, 270]:
        count = np.sum(labels == angle)
        print(f"    {angle:>3}°: {count:>6} patterns")

    # Plot reconstructed master
    fig, axes = plt.subplots(1, 4, figsize=(16, 4))
    for ax, angle in zip(axes, [0, 90, 180, 270]):
        rotated = flatten_rotation(master, L, angle).reshape(L, L)
        ax.imshow(rotated, cmap='gray')
        ax.set_title(f"Master at {angle}°")
        ax.axis('off')
    fig.suptitle("Task 7(a): Reconstructed master in all orientations", fontsize=14)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "task7a_master_rotations.png"), dpi=150, bbox_inches='tight')
    plt.close()

    # Large single master image
    fig, ax = plt.subplots(1, 1, figsize=(8, 8))
    ax.imshow(master.reshape(L, L), cmap='gray')
    ax.set_title("Task 7(a): Reconstructed master image (famous person)")
    ax.axis('off')
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "task7a_master.png"), dpi=150, bbox_inches='tight')
    plt.close()

    # Posterior uncertainty visualization
    max_posteriors = posteriors.max(axis=1)
    fig, ax = plt.subplots(1, 1, figsize=(8, 4))
    ax.hist(max_posteriors, bins=50, edgecolor='black', alpha=0.7)
    ax.set_xlabel("Max posterior probability")
    ax.set_ylabel("Number of patterns")
    ax.set_title("Task 7: Classification confidence distribution")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "task7_confidence.png"), dpi=150, bbox_inches='tight')
    plt.close()

    print("  [7a] Saved reconstructed master and confidence plots.")

    return labels, master


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(__file__))
    data_path = os.path.join(base_dir, "endeavor.npz")

    if not os.path.exists(data_path):
        print("Data file not found. Generating synthetic test data...")
        from generate_test_data import generate_all
        generate_all(data_path)

    loaded = np.load(data_path)
    task7a = loaded["task7a"]
    task7b = loaded["task7b"]
    labels, master = solve_task7(task7a, task7b)
