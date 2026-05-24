"""
Task 3: Scaling up to thousands of patterns [10 points]
========================================================
Given: 1000 flattened patterns in task3 (shape: 1000, 1089). Each was originally 33x33.
Goal:  Classify into four orientation classes. Use KMeans clustering.

Approach:
  Direct pairwise comparison (Task 2's method) works but is O(n * pixels * 4).
  For 1000 patterns this is fine, but KMeans is the recommended scalable approach.

  KMeans with k=4 will discover the four natural clusters (one per orientation).
  After clustering, we map each cluster to an orientation angle by comparing
  cluster centers against the 4 rotations of the reference pattern.

  We also need to guess the master image shape — the problem says 1089 pixels,
  which is 33x33.
"""

import numpy as np
import matplotlib.pyplot as plt
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from utils import (classify_with_kmeans, classify_with_kmeans_manual,
                   classify_flat_by_comparison, flatten_rotation,
                   print_orientation_counts, plot_design_matrix,
                   plot_class_averages, OUTPUT_DIR)


def solve_task3(task3_data):
    """
    Solve Task 3 completely.

    Parameters
    ----------
    task3_data : ndarray, shape (1000, 1089)
        The 1000 flattened noiseless patterns (originally 33x33).

    Returns
    -------
    labels : ndarray of int
        Orientation (0, 90, 180, 270) for each pattern.
    """
    n_patterns, n_pixels = task3_data.shape
    L = int(np.sqrt(n_pixels))  # 33
    print(f"\nTask 3: {n_patterns} patterns, {n_pixels} pixels each (L={L})")

    # -----------------------------------------------------------------
    # (a) Render the 2D master image
    # -----------------------------------------------------------------
    reference_2d = task3_data[0].reshape(L, L)

    fig, ax = plt.subplots(1, 1, figsize=(5, 5))
    ax.imshow(reference_2d, cmap='gray')
    ax.set_title(f"Task 3(a): Master image (mystery animal), {L}x{L}")
    ax.axis('off')
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "task3a_master.png"), dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  [3a] Rendered master image: {L}x{L} pixels.")

    # -----------------------------------------------------------------
    # (b) Classify using KMeans
    # -----------------------------------------------------------------
    try:
        labels = classify_with_kmeans(task3_data, L, n_clusters=4, max_iter=300, n_init=10)
        print("  Using sklearn KMeans.")
    except ImportError:
        print("  sklearn not available, using manual KMeans.")
        labels = classify_with_kmeans_manual(task3_data, L, n_clusters=4, max_iter=300, n_init=10)

    counts = print_orientation_counts(labels, "Task 3")

    # -----------------------------------------------------------------
    # (c) Plot unsorted and sorted design matrix with BuPu colormap
    # -----------------------------------------------------------------
    plot_design_matrix(task3_data, labels,
                       title="Task 3: Design Matrix (1000 patterns)",
                       cmap='BuPu', save_name="task3c_design_matrix.png")
    print("  [3c] Saved design matrix plots (BuPu colormap).")

    # Also plot class averages
    plot_class_averages(task3_data, labels, L,
                        title="Task 3: Orientation Class Averages",
                        save_name="task3_class_averages.png")

    return labels


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(__file__))
    data_path = os.path.join(base_dir, "endeavor.npz")

    if not os.path.exists(data_path):
        print("Data file not found. Generating synthetic test data...")
        from generate_test_data import generate_all
        generate_all(data_path)

    loaded = np.load(data_path)
    task3_data = loaded["task3"]
    labels = solve_task3(task3_data)
