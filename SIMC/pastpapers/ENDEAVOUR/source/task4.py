"""
Task 4: Noisy patterns [15 points]
====================================
Given: 1000 noisy flattened patterns in task4 (shape: 1000, 2500). Originally 50x50.
Goal:  Determine the true 2D master image from very noisy measurements.

Approach:
  Each pattern is extremely noisy (sparse photon counts). Individual patterns
  are unrecognizable, but averaging many aligned patterns reveals structure.

  Strategy:
  1. Compute average row-sum (average total pixel value per pattern).
  2. Render naive average assuming all same orientation (featureless blob).
  3. Use iterative refinement:
     a. Start with naive average as initial master estimate.
     b. Classify each pattern by log-likelihood against 4 rotations of estimate.
     c. Average within each class to get improved master estimates.
     d. Repeat until convergence.
  This is essentially an Expectation-Maximization (EM) algorithm.
"""

import numpy as np
import matplotlib.pyplot as plt
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from utils import (flatten_rotation, classify_by_log_likelihood,
                   classify_by_log_likelihood_vectorized, log_likelihood_aligned,
                   print_orientation_counts, plot_class_averages, OUTPUT_DIR)


def estimate_master_from_classes(design_matrix, labels, L):
    """Given classified patterns, estimate master image by averaging
    each class (after rotating back to canonical orientation).
    """
    eps = 1e-6
    n_pixels = design_matrix.shape[1]
    master_estimates = []

    for angle in [0, 90, 180, 270]:
        mask = labels == angle
        if mask.sum() == 0:
            master_estimates.append(np.ones(n_pixels) * 0.5)
            continue

        class_patterns = design_matrix[mask]
        # Rotate each pattern back to 0° orientation
        # If pattern was at angle X, rotating by -X (i.e., 360-X) brings it back
        back_angle = (360 - angle) % 360
        rotated_back = np.array([flatten_rotation(p, L, back_angle) for p in class_patterns])
        master_estimates.append(rotated_back.mean(axis=0))

    # Average all four estimates of the master
    combined = np.mean(master_estimates, axis=0)
    combined = np.clip(combined, eps, 1 - eps)
    return combined


def em_classify_noisy(design_matrix, L, n_iter=20, verbose=True):
    """Iterative EM-like algorithm for classifying noisy patterns.

    1. Initialize: naive average (all patterns assumed same orientation)
    2. E-step: classify each pattern by max log-likelihood
    3. M-step: re-estimate master from classified patterns
    4. Repeat until convergence
    """
    n_patterns, n_pixels = design_matrix.shape
    eps = 1e-6

    # Initialize: naive average
    master_estimate = np.clip(design_matrix.mean(axis=0), eps, 1 - eps)

    prev_labels = np.zeros(n_patterns, dtype=int)

    for iteration in range(n_iter):
        # E-step: classify patterns
        labels, ll_matrix = classify_by_log_likelihood_vectorized(
            design_matrix, master_estimate, L)

        # Check convergence
        n_changed = np.sum(labels != prev_labels)
        if verbose:
            total_ll = np.max(ll_matrix, axis=1).sum()
            print(f"  EM iter {iteration+1:2d}: {n_changed:5d} labels changed, "
                  f"total LL = {total_ll:.1f}")

        if n_changed == 0 and iteration > 0:
            if verbose:
                print("  Converged!")
            break

        prev_labels = labels.copy()

        # M-step: re-estimate master from classified patterns
        master_estimate = estimate_master_from_classes(design_matrix, labels, L)

    return labels, master_estimate


def solve_task4(task4_data):
    """
    Solve Task 4 completely.

    Parameters
    ----------
    task4_data : ndarray, shape (1000, 2500)
        The 1000 noisy flattened patterns (originally 50x50).

    Returns
    -------
    labels : ndarray of int
        Orientation (0, 90, 180, 270) for each pattern.
    master : ndarray, shape (2500,)
        Estimated master image (flattened).
    """
    n_patterns, n_pixels = task4_data.shape
    L = int(np.sqrt(n_pixels))  # 50
    print(f"\nTask 4: {n_patterns} patterns, {n_pixels} pixels each (L={L})")

    # -----------------------------------------------------------------
    # (a) Average pattern's total pixel value (average row-sum)
    # -----------------------------------------------------------------
    row_sums = task4_data.sum(axis=1)
    avg_row_sum = row_sums.mean()
    print(f"\n  [4a] Average row-sum (total pixel value per pattern): {avg_row_sum:.4f}")
    print(f"       This means on average {avg_row_sum:.1f} photons detected per pattern")
    print(f"       out of {n_pixels} pixels ({avg_row_sum/n_pixels*100:.2f}% hit rate)")

    # -----------------------------------------------------------------
    # (b) Naive average assuming all same orientation
    # -----------------------------------------------------------------
    naive_avg = task4_data.mean(axis=0).reshape(L, L)

    fig, ax = plt.subplots(1, 1, figsize=(5, 5))
    ax.imshow(naive_avg, cmap='gray')
    ax.set_title("Task 4(b): Naive average (all assumed same orientation)")
    ax.axis('off')
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "task4b_naive_avg.png"), dpi=150, bbox_inches='tight')
    plt.close()
    print("  [4b] Saved naive average image (featureless).")

    # -----------------------------------------------------------------
    # (c) EM-based classification and reconstruction
    # -----------------------------------------------------------------
    print("\n  [4c] Running EM classification...")
    labels, master_estimate = em_classify_noisy(task4_data, L, n_iter=30, verbose=True)

    counts = print_orientation_counts(labels, "Task 4")

    # Plot the four orientation class averages
    fig, axes = plt.subplots(1, 4, figsize=(16, 4))
    for ax, angle in zip(axes, [0, 90, 180, 270]):
        mask = labels == angle
        if mask.sum() > 0:
            class_avg = task4_data[mask].mean(axis=0).reshape(L, L)
            ax.imshow(class_avg, cmap='gray')
            ax.set_title(f"{angle}° (n={mask.sum()})")
        else:
            ax.set_title(f"{angle}° (empty)")
        ax.axis('off')
    fig.suptitle("Task 4(c): Orientation class averages (rotated)", fontsize=14)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "task4c_class_averages.png"), dpi=150, bbox_inches='tight')
    plt.close()

    # Plot the reconstructed master image
    fig, ax = plt.subplots(1, 1, figsize=(6, 6))
    ax.imshow(master_estimate.reshape(L, L), cmap='gray')
    ax.set_title("Task 4(c): Reconstructed master image")
    ax.axis('off')
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "task4c_master.png"), dpi=150, bbox_inches='tight')
    plt.close()

    # Show all 4 rotations of the reconstructed master
    fig, axes = plt.subplots(1, 4, figsize=(16, 4))
    for ax, angle in zip(axes, [0, 90, 180, 270]):
        rotated = flatten_rotation(master_estimate, L, angle).reshape(L, L)
        ax.imshow(rotated, cmap='gray')
        ax.set_title(f"Master at {angle}°")
        ax.axis('off')
    fig.suptitle("Task 4(c): Reconstructed master in all orientations", fontsize=14)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "task4c_master_rotations.png"), dpi=150, bbox_inches='tight')
    plt.close()

    print("  [4c] Saved class averages and reconstructed master images.")

    return labels, master_estimate


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(__file__))
    data_path = os.path.join(base_dir, "endeavor.npz")

    if not os.path.exists(data_path):
        print("Data file not found. Generating synthetic test data...")
        from generate_test_data import generate_all
        generate_all(data_path)

    loaded = np.load(data_path)
    task4_data = loaded["task4"]
    labels, master = solve_task4(task4_data)
