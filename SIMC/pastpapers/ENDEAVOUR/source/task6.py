"""
Task 6: Scaling up with sparse data format [20 points]
========================================================
Given: task6a (row indices) and task6b (col indices) of nonzero entries.
       65,535 patterns, each a flattened 25x25 pixel image.
       Data is stored in sparse format: only (row, col) of nonzero pixels.

Goal: Reconstruct the true 2D master image.

Approach:
  1. Compute average row-sum (average photons per pattern) from sparse data.
  2. Reconstruct naive average (assuming all same orientation).
  3. Use EM with log-likelihood classification to determine orientations.
  4. Average within classes, rotate back to canonical, to reconstruct master.

  Key challenge: Cannot materialize full dense matrix (65535 x 625 ≈ 41M entries).
  Instead, work directly with sparse representations where possible.
"""

import numpy as np
import matplotlib.pyplot as plt
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from utils import (flatten_rotation, OUTPUT_DIR)


def sparse_row_sums(row_indices, n_patterns):
    """Compute per-pattern photon counts from sparse indices."""
    return np.bincount(row_indices.astype(int), minlength=n_patterns)


def sparse_col_sums(row_indices, col_indices, n_patterns, n_pixels):
    """Compute per-pixel total photon count (column sums) from sparse data."""
    return np.bincount(col_indices.astype(int), minlength=n_pixels).astype(float)


def sparse_class_average(row_indices, col_indices, labels, angle, n_pixels):
    """Compute the average pattern for patterns classified as a given angle.
    Works directly from sparse indices without materializing the full matrix.
    """
    # Find which patterns belong to this class
    pattern_mask = (labels == angle)
    pattern_ids = set(np.where(pattern_mask)[0])
    n_in_class = pattern_mask.sum()

    if n_in_class == 0:
        return np.zeros(n_pixels)

    # Sum pixel values for patterns in this class
    pixel_sums = np.zeros(n_pixels)
    for i in range(len(row_indices)):
        if row_indices[i] in pattern_ids:
            pixel_sums[col_indices[i]] += 1.0

    return pixel_sums / n_in_class


def sparse_class_average_fast(row_indices, col_indices, labels, angle, n_pixels):
    """Vectorized version using boolean indexing."""
    pattern_mask = (labels == angle)
    n_in_class = pattern_mask.sum()
    if n_in_class == 0:
        return np.zeros(n_pixels)

    # Mask: which sparse entries belong to patterns of this class
    entry_mask = pattern_mask[row_indices]
    # Sum the column indices
    pixel_sums = np.bincount(col_indices[entry_mask].astype(int), minlength=n_pixels).astype(float)
    return pixel_sums / n_in_class


def em_sparse(row_indices, col_indices, n_patterns, n_pixels, L,
              n_iter=20, verbose=True):
    """EM algorithm for sparse pattern data.

    Instead of materializing the full design matrix, we compute log-likelihoods
    directly from the sparse representation.

    For each pattern i and rotation r:
      ln L(r | pattern_i) = sum over hit pixels j: ln(mu_r[j])
                          + sum over miss pixels j: ln(1-mu_r[j])
                          = sum_j ln(1-mu_r[j]) + sum over hits: ln(mu_r[j]/(1-mu_r[j]))

    The first term is constant for each rotation (sum over all pixels).
    The second term only needs the hit pixels (sparse!).
    """
    eps = 1e-12
    angles = [0, 90, 180, 270]

    # Initialize: naive average (all same orientation)
    col_sums = sparse_col_sums(row_indices, col_indices, n_patterns, n_pixels)
    master = np.clip(col_sums / n_patterns, eps, 1 - eps)

    # Precompute: for each pattern, which pixels were hit
    # Group sparse entries by pattern ID
    pattern_hits = {}
    for idx in range(len(row_indices)):
        pid = int(row_indices[idx])
        cid = int(col_indices[idx])
        if pid not in pattern_hits:
            pattern_hits[pid] = []
        pattern_hits[pid].append(cid)

    # Convert to arrays for speed
    hits_list = [np.array(pattern_hits.get(i, []), dtype=int) for i in range(n_patterns)]

    labels = np.zeros(n_patterns, dtype=int)

    for iteration in range(n_iter):
        # Compute master rotations
        master_rotations = {}
        for angle in angles:
            rotated = flatten_rotation(master, L, angle)
            master_rotations[angle] = np.clip(rotated, eps, 1 - eps)

        # Precompute base log-likelihood (all-miss term) for each rotation
        base_ll = {}
        log_ratio = {}
        for angle in angles:
            mu_r = master_rotations[angle]
            base_ll[angle] = np.sum(np.log(1 - mu_r))
            log_ratio[angle] = np.log(mu_r / (1 - mu_r))

        # E-step: classify each pattern
        new_labels = np.zeros(n_patterns, dtype=int)
        for i in range(n_patterns):
            hits = hits_list[i]
            best_ll = -np.inf
            best_angle = 0
            for angle in angles:
                ll = base_ll[angle]
                if len(hits) > 0:
                    ll += log_ratio[angle][hits].sum()
                if ll > best_ll:
                    best_ll = ll
                    best_angle = angle
            new_labels[i] = best_angle

        n_changed = np.sum(new_labels != labels)
        labels = new_labels

        if verbose:
            print(f"  EM iter {iteration+1:2d}: {n_changed:6d} labels changed")

        if n_changed == 0 and iteration > 0:
            if verbose:
                print("  Converged!")
            break

        # M-step: re-estimate master from classified patterns
        master_estimates = []
        for angle in angles:
            class_avg = sparse_class_average_fast(
                row_indices, col_indices, labels, angle, n_pixels)
            # Rotate back to canonical
            back_angle = (360 - angle) % 360
            rotated_back = flatten_rotation(class_avg, L, back_angle)
            master_estimates.append(rotated_back)

        master = np.mean(master_estimates, axis=0)
        master = np.clip(master, eps, 1 - eps)

    return labels, master


def solve_task6(task6a, task6b):
    """
    Solve Task 6 completely.

    Parameters
    ----------
    task6a : ndarray — row indices of nonzero entries
    task6b : ndarray — column indices of nonzero entries
    """
    n_pixels = 625  # 25x25
    L = 25

    # Determine number of patterns
    n_patterns = int(task6a.max()) + 1
    print(f"\nTask 6: {n_patterns} patterns, {L}x{L} pixels (sparse format)")
    print(f"  Total nonzero entries: {len(task6a)}")

    # -----------------------------------------------------------------
    # (a) Average row-sum (photons per pattern)
    # -----------------------------------------------------------------
    row_sums = sparse_row_sums(task6a, n_patterns)
    avg_row_sum = row_sums.mean()
    print(f"\n  [6a] Average row-sum (photons per pattern): {avg_row_sum:.4f}")
    print(f"       That's {avg_row_sum:.2f} photon hits out of {n_pixels} pixels "
          f"({avg_row_sum/n_pixels*100:.3f}% hit rate)")

    # -----------------------------------------------------------------
    # (b) Naive average assuming all same orientation
    # -----------------------------------------------------------------
    col_sums = sparse_col_sums(task6a, task6b, n_patterns, n_pixels)
    naive_avg = (col_sums / n_patterns).reshape(L, L)

    fig, ax = plt.subplots(1, 1, figsize=(5, 5))
    ax.imshow(naive_avg, cmap='gray')
    ax.set_title("Task 6(b): Naive average (all same orientation)")
    ax.axis('off')
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "task6b_naive_avg.png"), dpi=150, bbox_inches='tight')
    plt.close()
    print("  [6b] Saved naive average (should be featureless).")

    # -----------------------------------------------------------------
    # (c) EM classification and master reconstruction
    # -----------------------------------------------------------------
    print("\n  [6c] Running EM on sparse data...")
    labels, master = em_sparse(
        task6a, task6b, n_patterns, n_pixels, L,
        n_iter=25, verbose=True)

    # Count orientations
    for angle in [0, 90, 180, 270]:
        count = np.sum(labels == angle)
        print(f"    {angle:>3}°: {count:>6} patterns")

    # Plot the four class averages
    fig, axes = plt.subplots(1, 4, figsize=(16, 4))
    for ax, angle in zip(axes, [0, 90, 180, 270]):
        class_avg = sparse_class_average_fast(
            task6a, task6b, labels, angle, n_pixels)
        ax.imshow(class_avg.reshape(L, L), cmap='gray')
        ax.set_title(f"{angle}° (n={np.sum(labels==angle)})")
        ax.axis('off')
    fig.suptitle("Task 6(c): Orientation class averages", fontsize=14)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "task6c_class_averages.png"), dpi=150, bbox_inches='tight')
    plt.close()

    # Plot reconstructed master
    fig, ax = plt.subplots(1, 1, figsize=(6, 6))
    ax.imshow(master.reshape(L, L), cmap='gray')
    ax.set_title("Task 6(c): Reconstructed master image")
    ax.axis('off')
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "task6c_master.png"), dpi=150, bbox_inches='tight')
    plt.close()

    print("  [6c] Saved class averages and reconstructed master.")

    return labels, master


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(__file__))
    data_path = os.path.join(base_dir, "endeavor.npz")

    if not os.path.exists(data_path):
        print("Data file not found. Generating synthetic test data...")
        from generate_test_data import generate_all
        generate_all(data_path)

    loaded = np.load(data_path)
    task6a = loaded["task6a"]
    task6b = loaded["task6b"]
    labels, master = solve_task6(task6a, task6b)
