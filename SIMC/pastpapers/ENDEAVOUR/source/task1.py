"""
Task 1: Classifying a few noiseless patterns [10 points]
=========================================================
Given: 25 idealized 2D patterns in task1 (shape: 25, 18, 18).
Goal:  Classify each by its clockwise rotation (0, 90, 180, 270)
       relative to the first pattern (reference).

Approach:
  Since patterns are noiseless, we use direct pixel-wise comparison.
  For each pattern, compute the sum of squared differences (SSD) against
  all 4 rotations of the reference. The rotation with SSD = 0 (exact match)
  gives the correct orientation.
"""

import numpy as np
import matplotlib.pyplot as plt
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from utils import (get_four_rotations, classify_by_comparison,
                   print_orientation_counts, OUTPUT_DIR)


def solve_task1(task1_data):
    """
    Solve Task 1 completely.

    Parameters
    ----------
    task1_data : ndarray, shape (25, 18, 18)
        The 25 noiseless 2D patterns.

    Returns
    -------
    labels : ndarray of int
        Orientation (0, 90, 180, 270) for each of the 25 patterns.
    """
    n_patterns = task1_data.shape[0]
    L = task1_data.shape[1]  # 18
    print(f"\nTask 1: {n_patterns} patterns, {L}x{L} pixels each")

    reference = task1_data[0]

    # -----------------------------------------------------------------
    # (a) Plot the reference in its four clockwise rotations
    # -----------------------------------------------------------------
    rotations = get_four_rotations(reference)
    fig, axes = plt.subplots(1, 4, figsize=(14, 3.5))
    for ax, (angle, img) in zip(axes, rotations.items()):
        ax.imshow(img, cmap='gray')
        ax.set_title(f"r = {angle}°", fontsize=12)
        ax.axis('off')
    fig.suptitle("Task 1(a): Reference pattern in four clockwise rotations", fontsize=14)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "task1a_rotations.png"), dpi=150, bbox_inches='tight')
    plt.close()
    print("  [1a] Saved reference rotations plot.")

    # -----------------------------------------------------------------
    # (b) Classify all 25 patterns
    # -----------------------------------------------------------------
    labels = classify_by_comparison(task1_data, reference)

    counts = print_orientation_counts(labels, "Task 1")

    # -----------------------------------------------------------------
    # Visualization: show all 25 patterns colored by orientation
    # -----------------------------------------------------------------
    color_map = {0: [0.7, 0.85, 1.0],      # blue
                 90: [1.0, 0.75, 0.75],     # red
                 180: [0.75, 1.0, 0.75],    # green
                 270: [1.0, 0.9, 0.7]}      # orange

    rows, cols = 5, 5
    fig, axes = plt.subplots(rows, cols, figsize=(12, 12))
    for idx in range(n_patterns):
        r, c = divmod(idx, cols)
        ax = axes[r][c]

        # Create RGB image with tinted background
        img = task1_data[idx]
        img_norm = (img - img.min()) / (img.max() - img.min() + 1e-12)
        rgb = np.zeros((L, L, 3))
        bg_color = color_map[labels[idx]]
        for ch in range(3):
            rgb[:, :, ch] = img_norm * (1 - 0.3) + 0.3 * bg_color[ch]

        ax.imshow(rgb)
        ax.set_title(f"#{idx}: {labels[idx]}°", fontsize=9)
        ax.axis('off')

    fig.suptitle("Task 1(b): All 25 patterns colored by orientation class", fontsize=14)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "task1b_classified.png"), dpi=150, bbox_inches='tight')
    plt.close()
    print("  [1b] Saved classified patterns plot.")

    return labels


if __name__ == "__main__":
    # Load data
    base_dir = os.path.dirname(os.path.dirname(__file__))
    data_path = os.path.join(base_dir, "endeavor.npz")

    if not os.path.exists(data_path):
        print("Data file not found. Generating synthetic test data...")
        from generate_test_data import generate_all
        generate_all(data_path)

    loaded = np.load(data_path)
    task1_data = loaded["task1"]
    labels = solve_task1(task1_data)
