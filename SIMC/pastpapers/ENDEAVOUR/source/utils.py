"""
utils.py — Shared utility functions for the SIMC 2024 Endeavour Challenge.
Provides rotation, flattening, plotting, and classification helpers used across all tasks.
"""

import numpy as np
import matplotlib.pyplot as plt
import os

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)


# =============================================================================
# Core rotation functions
# =============================================================================

def rotate_90_clockwise(image_2d):
    """Rotate a 2D image 90 degrees clockwise.
    Equivalent to: transpose then flip left-right.
    """
    return np.rot90(image_2d, k=-1)  # k=-1 is 90 CW


def get_four_rotations(image_2d):
    """Return all four clockwise rotations (0, 90, 180, 270) of a 2D image.
    Returns dict: {0: original, 90: rotated_90, 180: rotated_180, 270: rotated_270}
    """
    rotations = {}
    current = image_2d.copy()
    for angle in [0, 90, 180, 270]:
        rotations[angle] = current.copy()
        current = rotate_90_clockwise(current)
    return rotations


def flatten_rotation(flat_vector, L, angle):
    """Given a flattened vector of length L*L, reshape to 2D, rotate by angle (CW),
    and flatten back. This is how the flattened design matrix relates rotations.
    """
    img = flat_vector.reshape(L, L)
    if angle == 0:
        rotated = img
    elif angle == 90:
        rotated = np.rot90(img, k=-1)
    elif angle == 180:
        rotated = np.rot90(img, k=-2)
    elif angle == 270:
        rotated = np.rot90(img, k=-3)
    else:
        raise ValueError(f"Angle must be 0, 90, 180, or 270, got {angle}")
    return rotated.flatten()


# =============================================================================
# Classification helpers
# =============================================================================

def classify_by_comparison(patterns_2d, reference_2d):
    """Classify each 2D pattern by comparing against 4 rotations of the reference.
    Uses sum of squared differences (SSD) as the distance metric.
    Returns array of angles (0, 90, 180, 270) for each pattern.
    """
    rotations = get_four_rotations(reference_2d)
    angles = [0, 90, 180, 270]
    n = len(patterns_2d)
    labels = np.zeros(n, dtype=int)

    for i, pattern in enumerate(patterns_2d):
        best_angle = 0
        best_dist = np.inf
        for angle in angles:
            dist = np.sum((pattern - rotations[angle]) ** 2)
            if dist < best_dist:
                best_dist = dist
                best_angle = angle
        labels[i] = best_angle
    return labels


def classify_flat_by_comparison(design_matrix, L):
    """Classify flattened patterns (rows of design_matrix) by comparing against
    4 rotations of the first pattern (reference).
    """
    reference_flat = design_matrix[0]
    angles = [0, 90, 180, 270]
    n = design_matrix.shape[0]
    labels = np.zeros(n, dtype=int)

    # Generate all 4 rotations of the reference in flattened form
    ref_rotations = {}
    for angle in angles:
        ref_rotations[angle] = flatten_rotation(reference_flat, L, angle)

    for i in range(n):
        pattern = design_matrix[i]
        best_angle = 0
        best_dist = np.inf
        for angle in angles:
            dist = np.sum((pattern - ref_rotations[angle]) ** 2)
            if dist < best_dist:
                best_dist = dist
                best_angle = angle
        labels[i] = best_angle
    return labels


def classify_flat_by_correlation(design_matrix, L):
    """Classify flattened patterns using Pearson correlation against 4 rotations
    of the first pattern. More robust to noise than SSD.
    """
    reference_flat = design_matrix[0]
    angles = [0, 90, 180, 270]

    # Generate all 4 rotations of the reference in flattened form
    ref_rotations = {}
    for angle in angles:
        ref_rotations[angle] = flatten_rotation(reference_flat, L, angle)

    n = design_matrix.shape[0]
    labels = np.zeros(n, dtype=int)

    for i in range(n):
        pattern = design_matrix[i]
        best_angle = 0
        best_corr = -np.inf
        for angle in angles:
            corr = np.corrcoef(pattern, ref_rotations[angle])[0, 1]
            if corr > best_corr:
                best_corr = corr
                best_angle = angle
        labels[i] = best_angle
    return labels


# =============================================================================
# KMeans-based classification
# =============================================================================

def classify_with_kmeans(design_matrix, L, n_clusters=4, max_iter=100, n_init=10):
    """Classify patterns using KMeans clustering, then map clusters to orientations
    by comparing cluster centers against rotations of the first pattern.
    """
    from sklearn.cluster import KMeans

    km = KMeans(n_clusters=n_clusters, max_iter=max_iter, n_init=n_init, random_state=42)
    cluster_labels = km.fit_predict(design_matrix)

    # Map cluster IDs to rotation angles
    reference_flat = design_matrix[0]
    angles = [0, 90, 180, 270]
    ref_rotations = {angle: flatten_rotation(reference_flat, L, angle) for angle in angles}

    # For each cluster center, find the closest rotation of the reference
    angle_map = {}
    used_angles = set()

    # Compute all distances
    dist_matrix = np.zeros((n_clusters, 4))
    for c in range(n_clusters):
        center = km.cluster_centers_[c]
        for j, angle in enumerate(angles):
            dist_matrix[c, j] = np.sum((center - ref_rotations[angle]) ** 2)

    # Greedy assignment (best match first)
    for _ in range(n_clusters):
        c, j = np.unravel_index(np.argmin(dist_matrix), dist_matrix.shape)
        angle_map[c] = angles[j]
        dist_matrix[c, :] = np.inf
        dist_matrix[:, j] = np.inf

    # Convert cluster labels to angle labels
    orientation_labels = np.array([angle_map[c] for c in cluster_labels])
    return orientation_labels


def classify_with_kmeans_manual(design_matrix, L, n_clusters=4, max_iter=100, n_init=10):
    """KMeans without sklearn — pure numpy implementation for environments
    where sklearn is not available.
    """
    n, d = design_matrix.shape
    best_labels = None
    best_inertia = np.inf

    for init in range(n_init):
        rng = np.random.RandomState(42 + init)
        # KMeans++ initialization
        centers = np.zeros((n_clusters, d))
        idx = rng.randint(n)
        centers[0] = design_matrix[idx]

        for c in range(1, n_clusters):
            dists = np.min([np.sum((design_matrix - centers[j]) ** 2, axis=1)
                           for j in range(c)], axis=0)
            probs = dists / dists.sum()
            idx = rng.choice(n, p=probs)
            centers[c] = design_matrix[idx]

        # Iterate
        for _ in range(max_iter):
            # Assign
            dists = np.array([np.sum((design_matrix - centers[c]) ** 2, axis=1)
                             for c in range(n_clusters)])  # (k, n)
            labels = np.argmin(dists, axis=0)

            # Update centers
            new_centers = np.zeros_like(centers)
            for c in range(n_clusters):
                mask = labels == c
                if mask.sum() > 0:
                    new_centers[c] = design_matrix[mask].mean(axis=0)
                else:
                    new_centers[c] = centers[c]

            if np.allclose(centers, new_centers):
                break
            centers = new_centers

        inertia = sum(np.sum((design_matrix[labels == c] - centers[c]) ** 2)
                      for c in range(n_clusters))
        if inertia < best_inertia:
            best_inertia = inertia
            best_labels = labels.copy()
            best_centers = centers.copy()

    # Map cluster IDs to rotation angles
    reference_flat = design_matrix[0]
    angles = [0, 90, 180, 270]
    ref_rotations = {angle: flatten_rotation(reference_flat, L, angle) for angle in angles}

    dist_matrix = np.zeros((n_clusters, 4))
    for c in range(n_clusters):
        for j, angle in enumerate(angles):
            dist_matrix[c, j] = np.sum((best_centers[c] - ref_rotations[angle]) ** 2)

    angle_map = {}
    for _ in range(n_clusters):
        c, j = np.unravel_index(np.argmin(dist_matrix), dist_matrix.shape)
        angle_map[c] = angles[j]
        dist_matrix[c, :] = np.inf
        dist_matrix[:, j] = np.inf

    orientation_labels = np.array([angle_map[c] for c in best_labels])
    return orientation_labels


# =============================================================================
# Log-likelihood classification (for noisy/sparse tasks)
# =============================================================================

def log_likelihood_aligned(pattern, master_flat):
    """Compute log-likelihood that a pattern came from the master image
    in the same orientation, assuming Binomial noise (k=0 or 1).

    ln L = sum_i [ k_i * ln(mu_i) + (1-k_i) * ln(1-mu_i) ]

    pattern: 1D array of 0s and 1s (observed photon counts)
    master_flat: 1D array of average pixel values (probabilities), must be in (0,1)
    """
    eps = 1e-12  # avoid log(0)
    mu = np.clip(master_flat, eps, 1 - eps)
    return np.sum(pattern * np.log(mu) + (1 - pattern) * np.log(1 - mu))


def classify_by_log_likelihood(design_matrix, master_estimate, L):
    """Classify each pattern by computing log-likelihood for all 4 orientations
    of the master image and picking the most likely one.
    """
    angles = [0, 90, 180, 270]
    master_rotations = {angle: flatten_rotation(master_estimate, L, angle) for angle in angles}

    n = design_matrix.shape[0]
    labels = np.zeros(n, dtype=int)

    for i in range(n):
        pattern = design_matrix[i]
        best_angle = 0
        best_ll = -np.inf
        for angle in angles:
            ll = log_likelihood_aligned(pattern, master_rotations[angle])
            if ll > best_ll:
                best_ll = ll
                best_angle = angle
        labels[i] = best_angle
    return labels


def classify_by_log_likelihood_vectorized(design_matrix, master_estimate, L):
    """Vectorized version for large datasets. Returns labels and log-likelihood matrix."""
    eps = 1e-12
    angles = [0, 90, 180, 270]
    master_rotations = np.array([
        flatten_rotation(master_estimate, L, angle) for angle in angles
    ])  # (4, N_pixels)

    master_rotations = np.clip(master_rotations, eps, 1 - eps)

    # design_matrix: (n_patterns, N_pixels)
    # log_mu: (4, N_pixels), log_1_minus_mu: (4, N_pixels)
    log_mu = np.log(master_rotations)
    log_1_minus_mu = np.log(1 - master_rotations)

    # LL[r, i] = sum_j [ k_ij * log_mu[r,j] + (1-k_ij) * log_1_minus_mu[r,j] ]
    # = k_i . log_mu[r] + (1-k_i) . log_1_minus_mu[r]
    # = k_i . (log_mu[r] - log_1_minus_mu[r]) + sum_j log_1_minus_mu[r,j]

    log_ratio = log_mu - log_1_minus_mu  # (4, N_pixels)
    base_ll = log_1_minus_mu.sum(axis=1)  # (4,)

    # LL_matrix: (n_patterns, 4)
    ll_matrix = design_matrix @ log_ratio.T + base_ll[np.newaxis, :]

    best_rot_idx = np.argmax(ll_matrix, axis=1)
    labels = np.array([angles[idx] for idx in best_rot_idx])

    return labels, ll_matrix


# =============================================================================
# Sparse data helpers
# =============================================================================

def sparse_to_dense(row_indices, col_indices, n_patterns, n_pixels):
    """Convert sparse format (row, col indices of nonzero entries) to dense design matrix."""
    design_matrix = np.zeros((n_patterns, n_pixels), dtype=np.float64)
    design_matrix[row_indices, col_indices] = 1.0
    return design_matrix


def sparse_to_row_sums(row_indices, n_patterns):
    """Compute row sums (total photon count per pattern) from sparse format."""
    counts = np.bincount(row_indices, minlength=n_patterns)
    return counts


# =============================================================================
# Plotting helpers
# =============================================================================

def plot_four_rotations(image_2d, title="Reference pattern", save_name=None):
    """Plot a 2D image in its four clockwise rotations."""
    rotations = get_four_rotations(image_2d)
    fig, axes = plt.subplots(1, 4, figsize=(12, 3))
    for ax, (angle, img) in zip(axes, rotations.items()):
        ax.imshow(img, cmap='gray')
        ax.set_title(f"{angle}° CW")
        ax.axis('off')
    fig.suptitle(title, fontsize=14)
    plt.tight_layout()
    if save_name:
        plt.savefig(os.path.join(OUTPUT_DIR, save_name), dpi=150, bbox_inches='tight')
    plt.close()


def plot_design_matrix(design_matrix, labels=None, title="Design Matrix",
                       cmap='BuPu', save_name=None):
    """Plot unsorted and sorted design matrix side by side."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    axes[0].imshow(design_matrix, aspect='auto', cmap=cmap)
    axes[0].set_title("unsorted patterns")
    axes[0].set_xlabel("pattern's pixel (flattened)")
    axes[0].set_ylabel("pattern number")

    if labels is not None:
        sort_idx = np.argsort(labels)
        sorted_matrix = design_matrix[sort_idx]
        axes[1].imshow(sorted_matrix, aspect='auto', cmap=cmap)
        axes[1].set_title("patterns sorted by orientation class")
        axes[1].set_xlabel("pattern's pixel (flattened)")
        axes[1].set_ylabel("pattern number")

        # Add dashed lines between orientation blocks
        sorted_labels = labels[sort_idx]
        for angle in [90, 180, 270]:
            boundary = np.searchsorted(sorted_labels, angle)
            if 0 < boundary < len(sorted_labels):
                axes[1].axhline(y=boundary - 0.5, color='black', linestyle='--', linewidth=1)
    else:
        axes[1].text(0.5, 0.5, "No labels provided", ha='center', va='center',
                     transform=axes[1].transAxes)

    fig.suptitle(title, fontsize=14)
    plt.tight_layout()
    if save_name:
        plt.savefig(os.path.join(OUTPUT_DIR, save_name), dpi=150, bbox_inches='tight')
    plt.close()


def plot_class_averages(design_matrix, labels, L, title="Orientation Class Averages",
                        save_name=None):
    """Plot the average 2D image for each orientation class."""
    angles = [0, 90, 180, 270]
    fig, axes = plt.subplots(1, 4, figsize=(14, 3.5))

    for ax, angle in zip(axes, angles):
        mask = labels == angle
        if mask.sum() > 0:
            avg = design_matrix[mask].mean(axis=0).reshape(L, L)
            ax.imshow(avg, cmap='gray')
            ax.set_title(f"{angle}° (n={mask.sum()})")
        else:
            ax.set_title(f"{angle}° (empty)")
        ax.axis('off')

    fig.suptitle(title, fontsize=14)
    plt.tight_layout()
    if save_name:
        plt.savefig(os.path.join(OUTPUT_DIR, save_name), dpi=150, bbox_inches='tight')
    plt.close()


def count_orientations(labels):
    """Return a dict with counts for each orientation."""
    angles = [0, 90, 180, 270]
    counts = {angle: int(np.sum(labels == angle)) for angle in angles}
    return counts


def print_orientation_counts(labels, task_name=""):
    """Print orientation counts in a formatted way."""
    counts = count_orientations(labels)
    print(f"\n{'='*50}")
    print(f"  Orientation Counts — {task_name}")
    print(f"{'='*50}")
    for angle, count in counts.items():
        print(f"  {angle:>3}° : {count:>5} patterns")
    print(f"  {'Total':>4} : {sum(counts.values()):>5} patterns")
    print(f"{'='*50}\n")
    return counts
