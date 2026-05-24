"""SIMC 2026 -- Reference Snippets: Statistical Tools

Core statistical routines: descriptive summaries, z-score normalisation,
confidence intervals for the mean, and normal-distribution fitting.  Every
function operates on a NumPy array and returns either a scalar, an ndarray,
or a NamedTuple so that fields can be accessed by name rather than by position.

Mathematical background
=======================

Descriptive statistics
-----------------------
Given a sample x = (x_1, ..., x_N) the canonical summaries are:

    sample mean         x_bar = (1/N) sum_i x_i
    sample std          s     = sqrt( (1/(N-1)) sum_i (x_i - x_bar)^2 )

The N-1 denominator (Bessel's correction) gives the unbiased estimator of the
population variance; use ``ddof=0`` for the MLE / population estimator.

Z-score normalisation
---------------------
The z-score standardises each observation relative to the sample mean and
standard deviation:

    z_i = (x_i - x_bar) / s

After transformation the sample has mean 0 and standard deviation 1 (not
exactly unit-normal in distribution -- that requires the population parameters
-- but the moments are exact for the sample).

Confidence interval for the mean
----------------------------------
For an unknown population variance the exact t-interval is

    CI = x_bar +/- t_{alpha/2, N-1} * s / sqrt(N)

where t_{alpha/2, N-1} is the upper alpha/2 quantile of the t-distribution
with N-1 degrees of freedom.  For N >= 30 this is numerically close to the
z-interval (t -> z as N -> inf), but the t-interval is exact for normally
distributed data at any sample size.

Normal distribution fitting
----------------------------
The method-of-moments / MLE estimators for the Gaussian family are:

    mu_hat    = x_bar          (sample mean)
    sigma_hat = s              (sample std, ddof=1)

After fitting, a Kolmogorov--Smirnov (KS) test against Normal(mu_hat, sigma_hat)
is performed.  A large p-value (> 0.05) is consistent with normality; a small
p-value suggests the data are non-Gaussian.
"""

from __future__ import annotations

from typing import NamedTuple

import numpy as np
from scipy import stats


# =============================================================================
# Descriptive statistics
# =============================================================================

class DescriptiveStats(NamedTuple):
    """Descriptive summary of a 1-D sample."""
    mean:   float
    std:    float
    minimum: float
    maximum: float
    median: float
    n:      int


def describe(sample: np.ndarray) -> DescriptiveStats:
    """Compute mean, standard deviation, range, median, and count of a sample.

    The standard deviation uses the unbiased (Bessel-corrected) divisor N-1.
    Non-finite values in ``sample`` are included in the computation and will
    propagate to the output; filter them with ``sample[np.isfinite(sample)]``
    beforehand if that is undesirable.

    Parameters
    ----------
    sample : ndarray of any shape
        The observations.  Multi-dimensional arrays are flattened to 1-D
        before computing any statistic.

    Returns
    -------
    stats : DescriptiveStats
        Named tuple with fields ``mean``, ``std``, ``minimum``, ``maximum``,
        ``median``, and ``n`` (sample size after flattening).

    Examples
    --------
    >>> desc = describe(np.array([1.0, 2.0, 3.0, 4.0, 5.0]))
    >>> desc.mean
    3.0
    >>> desc.std
    1.5811388300841898
    """
    x = sample.ravel().astype(np.float64)
    return DescriptiveStats(
        mean=float(x.mean()),
        std=float(x.std(ddof=1)),
        minimum=float(x.min()),
        maximum=float(x.max()),
        median=float(np.median(x)),
        n=int(x.size),
    )


# =============================================================================
# Z-score
# =============================================================================

