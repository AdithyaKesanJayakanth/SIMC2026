"""
Task 2: Flattening 2D patterns into 1D representation [10 points]
==================================================================
Given: 100 flattened patterns in task2 (shape: 100, 1296). Each was originally 36x36.
Goal:  Classify into four orientation classes relative to the first pattern.

Approach:
  1. Reshape the first row back to 36x36 to render the master image.
  2. For classification, generate 4 rotations of the reference in flattened form.
  3. Compare each pattern against all 4 flattened rotations using SSD.
  4. The rotation with minimum SSD gives the classification.

Key insight: even though pixels are flattened, rotation in 2D followed by
re-flattening produces a specific permutation of the pixel indices. Two patterns
with the same orientation will have identical flattened representations.
"""

import numpy as np
import matplotlib.pyplot as plt
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from utils import (classify_flat_by_comparison, flatten_rotation,
                   print_orientation_counts, plot_design_matrix, OUTPUT_DIR)


def solve_task2(task2_data):
    """
    Solve Task 2 completely.

    Parameters
    ----------
    task2_data : ndarray, shape (100, 1296)
        The 100 flattened noiseless patterns (originally 36x36).

    Returns
    -------
    labels : ndarray of int
        Orientation (0, 90, 180, 270) for each pattern.
    """
    n_patterns, n_pixels = task2_data.shape
    L = int(np.sqrt(n_pixels))  # 36
    print(f"\nTask 2: {n_patterns} patterns, {n_pixels} pixels each (L={L})")

    # -----------------------------------------------------------------
    # (a) Render the 2D master image
    # -----------------------------------------------------------------
    reference_2d = task2_data[0].reshape(L, L)

    fig, ax = plt.subplots(1, 1, figsize=(5, 5))
    ax.imshow(reference_2d, cmap='gray')
    ax.set_title(f"Task 2(a): Master image (reference), {L}x{L} pixels")
    ax.axis('off')
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "task2a_master.png"), dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  [2a] Rendered master image: {L}x{L} pixels.")

    # Also show all 4 rotations
    fig, axes = plt.subplots(1, 4, figsize=(14, 3.5))
    for ax, angle in zip(axes, [0, 90, 180, 270]):
        rotated_flat = flatten_rotation(task2_data[0], L, angle)
        ax.imshow(rotated_flat.reshape(L, L), cmap='gray')
        ax.set_title(f"r = {angle}°")
        ax.axis('off')
    fig.suptitle("Task 2(a): Reference in four rotations", fontsize=14)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "task2a_rotations.png"), dpi=150, bbox_inches='tight')
    plt.close()

    # -----------------------------------------------------------------
    # (b) Classify all 100 patterns
    # -----------------------------------------------------------------
    labels = classify_flat_by_comparison(task2_data, L)
    counts = print_orientation_counts(labels, "Task 2")

    # -----------------------------------------------------------------
    # Visualization: unsorted and sorted design matrix
    # -----------------------------------------------------------------
    plot_design_matrix(task2_data, labels,
                       title="Task 2: Design Matrix",
                       cmap='gray', save_name="task2_design_matrix.png")
    print("  [2b] Saved design matrix plots.")

    return labels


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(__file__))
    data_path = os.path.join(base_dir, "endeavor.npz")

    if not os.path.exists(data_path):
        print("Data file not found. Generating synthetic test data...")
        from generate_test_data import generate_all
        generate_all(data_path)

    loaded = np.load(data_path)
    task2_data = loaded["task2"]
    labels = solve_task2(task2_data)
