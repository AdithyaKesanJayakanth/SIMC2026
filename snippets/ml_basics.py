"""SIMC 2026 -- Reference Snippets: ML Basics and Monte Carlo

Machine-learning primitives and Monte Carlo simulation tools.

Organisation
============

ML basics
---------
KMeans           -- partition M points into K clusters via Lloyd's algorithm;
                    returns labels, centroids, and inertia.
PCA              -- project an (M, N) matrix onto its leading r principal
                    components; returns scores, component vectors, and the
                    explained-variance ratios.
k-Nearest Neighbours -- brute-force Euclidean search returning the k closest
                    training points and their distances for each query.
Anomaly detection -- Isolation Forest scores each point with an anomaly score
                    derived from expected isolation depth; flagged outliers are
                    returned alongside the raw scores.

Monte Carlo
-----------
monte_carlo_simulate -- run a user-supplied scalar experiment R times, using a
                    shared NumPy random Generator for reproducibility; returns
                    the full result vector plus mean, std, and a 95% empirical
                    confidence interval.

Mathematical background
=======================

KMeans inertia
--------------
Lloyd's algorithm minimises the within-cluster sum of squared distances:

    W = sum_{i=1}^{M} || x_i - c_{k(i)} ||_2^2

where c_{k(i)} is the centroid of the cluster that point i was assigned to.
Lower W means tighter clusters; W is guaranteed to decrease or stay the same
on each iteration.

PCA via SVD
-----------
PCA finds the orthonormal directions v_1, ..., v_r that maximise the variance
of the projected data.  The r-th direction solves:

    max_{||v||=1, v perp v_1..v_{r-1}} Var(X v)

and can be computed as the top-r right singular vectors of the centred data
matrix X_c = X - mean(X, axis=0).  The explained variance ratio for PC k is

    rho_k = lambda_k / sum_j lambda_j

where lambda_k = sigma_k^2 / (M - 1) is the sample variance along PC k.

Monte Carlo estimation
----------------------
The Monte Carlo estimator of E[f(X)] is the sample average of R independent
realisations:

    mu_hat_R = (1/R) sum_{r=1}^{R} f(X_r).

By the law of large numbers mu_hat_R -> E[f(X)] almost surely.  The standard
error scales as sigma_f / sqrt(R), so halving the error requires four times
as many repetitions.
"""

from __future__ import annotations

from typing import Callable, NamedTuple

import numpy as np
from sklearn.cluster import KMeans as _SKLearnKMeans
from sklearn.decomposition import PCA as _SKLearnPCA
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import NearestNeighbors


# =============================================================================
# KMeans
# =============================================================================

class KMeansResult(NamedTuple):
    """Output of a KMeans fit."""
    labels:    np.ndarray   # shape (M,) -- integer cluster assignments 0..K-1
    centroids: np.ndarray   # shape (K, N) -- cluster centres
    inertia:   float        # within-cluster sum of squared distances (W)


def fit_kmeans(
    data: np.ndarray,
    n_clusters: int,
    *,
    n_init: int = 10,
    random_state: int = 0,
) -> KMeansResult:
    """Fit KMeans and return cluster labels, centroids, and inertia.

    KMeans partitions M points into K non-overlapping clusters by alternating
    between two steps until the assignments no longer change:

        1. Assignment step -- each point is assigned to its nearest centroid
           under the Euclidean metric.
        2. Update step -- each centroid is recomputed as the arithmetic mean
           of its currently assigned points.

    The algorithm is run ``n_init`` times from different random starts;
    scikit-learn uses the k-means++ seeding heuristic which places the initial
    centroids with probability proportional to their squared distance from
    already-chosen centroids, dramatically reducing the probability of
    converging to a poor local minimum.  The run with the lowest inertia W is
    retained.

    Parameters
    ----------
    data : ndarray of shape (M, N)
        The M data points in N-dimensional feature space.  Features should be
        on comparable scales; standardise with ``z_score`` from
        ``statistical_tools.py`` if they are not.
    n_clusters : int
        Number of clusters K.  Must satisfy 1 <= K <= M.
    n_init : int, optional
        Number of random initialisations; default 10.
    random_state : int, optional
        Seed for reproducible results; default 0.

    Returns
    -------
    result : KMeansResult
        Named tuple with:
        - ``labels`` -- shape (M,) integer cluster assignments.
        - ``centroids`` -- shape (K, N) cluster centres.
        - ``inertia`` -- within-cluster sum of squared distances W.

    Examples
    --------
    >>> import numpy as np
    >>> rng = np.random.default_rng(0)
    >>> data = np.vstack([rng.normal([0,0], 0.3, (50,2)),
    ...                   rng.normal([5,5], 0.3, (50,2))])
    >>> km = fit_kmeans(data, n_clusters=2)
    >>> len(np.unique(km.labels))
    2
    """
    km = _SKLearnKMeans(n_clusters=n_clusters, n_init=n_init, random_state=random_state)
    km.fit(data)
    return KMeansResult(
        labels=km.labels_,
        centroids=km.cluster_centers_,
        inertia=float(km.inertia_),
    )


# =============================================================================
# PCA
# =============================================================================

class PCAResult(NamedTuple):
    """Output of a PCA projection."""
    scores:                   np.ndarray  # shape (M, r) -- projected coordinates
    components:               np.ndarray  # shape (r, N) -- principal axes (row vectors)
    explained_variance_ratio: np.ndarray  # shape (r,) -- fraction of variance per PC


