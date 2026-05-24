"""
generate_test_data.py — Generates synthetic test data mimicking the endeavor.npz format.
Use this to test the solution code when the real data file is unavailable.

The generated data mirrors the problem specification:
  task1: (25, 18, 18)     — 25 noiseless 2D patterns
  task2: (100, 1296)       — 100 flattened 36x36 patterns
  task3: (1000, 1089)      — 1000 flattened 33x33 patterns
  task4: (1000, 2500)      — 1000 noisy flattened 50x50 patterns
  task6a, task6b: sparse   — row/col indices for 65,535 patterns of 25x25
  task7a, task7b: sparse   — row/col indices for 100,000 patterns of 25x25

Per-task seeds, noise scales, and the rotation choice set are loaded from
the gitignored ground_truth.py module so they are not exposed in source.
"""

import numpy as np
import os

try:
    from ground_truth import N_ROTATIONS, TASK_PARAMS   # private, gitignored
except ImportError:
    N_ROTATIONS = None
    TASK_PARAMS = None


def make_master_image(L, style='animal', seed=42):
    """Create a synthetic master image with asymmetric features
    so rotations are distinguishable."""
    rng = np.random.RandomState(seed)
    img = rng.rand(L, L) * 0.3  # low-intensity background

    # Add asymmetric features (like a face/animal)
    cx, cy = L // 2, L // 2

    # "Eye" in top-left quadrant
    r_eye = max(1, L // 8)
    for i in range(L):
        for j in range(L):
            if (i - cy // 2) ** 2 + (j - cx // 2) ** 2 < r_eye ** 2:
                img[i, j] = 0.9

    # "Nose" slightly off-center
    nose_r = max(1, L // 10)
    for i in range(L):
        for j in range(L):
            if (i - cy) ** 2 + (j - cx + L // 6) ** 2 < nose_r ** 2:
                img[i, j] = 0.7

    # Asymmetric stripe on one side
    img[L // 4: L // 4 + max(1, L // 8), L * 3 // 4:] = 0.85

    # Bright corner marker (top-right only — ensures asymmetry)
    marker_size = max(1, L // 10)
    img[:marker_size, -marker_size:] = 0.95

    return img


def rotate_image(img, k):
    """Rotate image by k*90 degrees clockwise."""
    return np.rot90(img, k=-k)


def generate_noiseless_patterns(master, n_patterns, seed=42):
    """Generate noiseless patterns with random rotations."""
    rng = np.random.RandomState(seed)
    rotations = rng.randint(0, N_ROTATIONS, size=n_patterns)
    patterns = np.array([rotate_image(master, r) for r in rotations])
    true_angles = rotations * 90
    return patterns, true_angles


def generate_noiseless_flat(master, n_patterns, seed=42):
    """Generate flattened noiseless patterns."""
    patterns, true_angles = generate_noiseless_patterns(master, n_patterns, seed)
    L = master.shape[0]
    flat = patterns.reshape(n_patterns, L * L)
    return flat, true_angles


def generate_noisy_flat(master, n_patterns, seed=42):
    """Generate noisy patterns using Binomial noise model.
    Each pixel value is the probability of detecting a photon.
    """
    rng = np.random.RandomState(seed)
    L = master.shape[0]
    rotations = rng.randint(0, N_ROTATIONS, size=n_patterns)
    patterns = []

    for r in rotations:
        rotated = rotate_image(master, r)
        # Binomial noise: each pixel independently fires with probability = pixel_value
        noisy = (rng.rand(L, L) < rotated).astype(float)
        patterns.append(noisy.flatten())

    flat = np.array(patterns)
    true_angles = rotations * 90
    return flat, true_angles


def generate_sparse_data(master, n_patterns, seed=42):
    """Generate sparse pattern data (row indices, col indices of nonzero entries).
    Master image pixel values are probabilities of photon detection.
    """
    rng = np.random.RandomState(seed)
    L = master.shape[0]
    N_pixels = L * L
    rotations = rng.randint(0, N_ROTATIONS, size=n_patterns)

    all_rows = []
    all_cols = []

    for i, r in enumerate(rotations):
        rotated = rotate_image(master, r).flatten()
        # Each pixel fires with probability = pixel_value (scaled down for sparsity)
        hits = rng.rand(N_pixels) < rotated
        pixel_indices = np.where(hits)[0]
        all_rows.extend([i] * len(pixel_indices))
        all_cols.extend(pixel_indices.tolist())

    row_indices = np.array(all_rows, dtype=np.int64)
    col_indices = np.array(all_cols, dtype=np.int64)
    true_angles = rotations * 90
    return row_indices, col_indices, true_angles


def generate_all(output_path="endeavor.npz"):
    """Generate all task data and save as .npz."""
    print("Generating synthetic test data...")

    # Task 1: 25 patterns, 18x18, noiseless
    p1 = TASK_PARAMS["task1"]
    master1 = make_master_image(18, seed=p1["master_seed"])
    task1, angles1 = generate_noiseless_patterns(master1, 25, seed=p1["pattern_seed"])
    print(f"  task1: {task1.shape} — true orientation distribution: {np.bincount(angles1 // 90, minlength=N_ROTATIONS)}")

    # Task 2: 100 patterns, 36x36, flattened, noiseless
    p2 = TASK_PARAMS["task2"]
    master2 = make_master_image(36, seed=p2["master_seed"])
    task2, angles2 = generate_noiseless_flat(master2, 100, seed=p2["pattern_seed"])
    print(f"  task2: {task2.shape} — true orientation distribution: {np.bincount(angles2 // 90, minlength=N_ROTATIONS)}")

    # Task 3: 1000 patterns, 33x33, flattened, noiseless
    p3 = TASK_PARAMS["task3"]
    master3 = make_master_image(33, seed=p3["master_seed"])
    task3, angles3 = generate_noiseless_flat(master3, 1000, seed=p3["pattern_seed"])
    print(f"  task3: {task3.shape} — true orientation distribution: {np.bincount(angles3 // 90, minlength=N_ROTATIONS)}")

    # Task 4: 1000 patterns, 50x50, flattened, noisy
    p4 = TASK_PARAMS["task4"]
    master4 = make_master_image(50, seed=p4["master_seed"])
    master4 *= p4["noise_scale"]  # scale down so most pixels are ~0 (sparse photon hits)
    task4, angles4 = generate_noisy_flat(master4, 1000, seed=p4["pattern_seed"])
    print(f"  task4: {task4.shape} — avg row sum: {task4.sum(axis=1).mean():.1f}")

    # Task 6: 65535 sparse patterns, 25x25
    p6 = TASK_PARAMS["task6"]
    master6 = make_master_image(25, seed=p6["master_seed"])
    master6 *= p6["noise_scale"]  # very sparse
    row6, col6, angles6 = generate_sparse_data(master6, 65535, seed=p6["pattern_seed"])
    print(f"  task6a: {row6.shape}, task6b: {col6.shape}")

    # Task 7: 100000 sparse patterns, 25x25
    p7 = TASK_PARAMS["task7"]
    master7 = make_master_image(25, seed=p7["master_seed"])
    master7 *= p7["noise_scale"]  # even sparser
    row7, col7, angles7 = generate_sparse_data(master7, 100000, seed=p7["pattern_seed"])
    print(f"  task7a: {row7.shape}, task7b: {col7.shape}")

    np.savez(output_path,
             task1=task1, task2=task2, task3=task3, task4=task4,
             task6a=row6, task6b=col6, task7a=row7, task7b=col7)
    print(f"\nSaved to {output_path}")

    # Also save ground truth for validation
    np.savez(output_path.replace('.npz', '_truth.npz'),
             angles1=angles1, angles2=angles2, angles3=angles3,
             angles4=angles4, angles6=angles6, angles7=angles7)
    print(f"Ground truth saved to {output_path.replace('.npz', '_truth.npz')}")


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(__file__))
    generate_all(os.path.join(base_dir, "endeavor.npz"))
