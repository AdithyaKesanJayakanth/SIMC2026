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

def z_score(sample: np.ndarray, *, ddof: int = 1) -> np.ndarray:
    """Standardise a sample to zero mean and unit standard deviation.

    Each observation is transformed by

        z_i = (x_i - mean(x)) / std(x, ddof=ddof).

    With ``ddof=1`` (default) the denominator is the unbiased sample standard
    deviation; with ``ddof=0`` it is the population (MLE) estimator, which is
    appropriate when ``sample`` is the entire population.

    If the standard deviation is zero (constant input), the function raises a
    ``ValueError`` rather than silently returning ``nan`` or ``inf``, because
    a constant sample carries no information that can be meaningfully
    standardised.

    Parameters
    ----------
    sample : ndarray of shape (N,) or any shape
        Observations to standardise.  Multi-dimensional arrays are flattened
        to 1-D; the returned array has shape ``(sample.size,)``.
    ddof : int, optional
        Delta degrees of freedom for the standard deviation; default 1.

    Returns
    -------
    z : ndarray of shape (sample.size,), dtype float64
        The standardised sample with mean 0 and standard deviation 1.

    Raises
    ------
    ValueError
        If the computed standard deviation is zero.

    Examples
    --------
    >>> z = z_score(np.array([2.0, 4.0, 4.0, 4.0, 5.0, 5.0, 7.0, 9.0]))
    >>> z.mean()   # doctest: +ELLIPSIS
    0.0
    >>> z.std(ddof=1)
    1.0
    """
    x = sample.ravel().astype(np.float64)
    mu = x.mean()
    sigma = x.std(ddof=ddof)
    if sigma == 0.0:
        raise ValueError(
            "z_score: sample standard deviation is zero -- cannot standardise a constant sample."
        )
    return (x - mu) / sigma


# =============================================================================
# Confidence interval for the mean
# =============================================================================

class ConfidenceInterval(NamedTuple):
    """Two-sided confidence interval for the population mean."""
    lower:            float
    upper:            float
    centre:           float   # sample mean = point estimate
    confidence_level: float
    n:                int


def confidence_interval_mean(
    sample: np.ndarray,
    *,
    confidence: float = 0.95,
) -> ConfidenceInterval:
    """Compute the two-sided t-interval for the population mean.

    Uses the Student-t distribution with N-1 degrees of freedom.  This is
    the exact interval when the population is normally distributed and the
    variance is unknown.  For N >= 30 the difference from the z-interval
    (which assumes known variance) is negligible.

    The half-width of the interval is

        h = t_{alpha/2, N-1} * s / sqrt(N),

    where alpha = 1 - confidence, s is the sample standard deviation (ddof=1),
    and t_{alpha/2, N-1} is the upper alpha/2 quantile of t(N-1).

    Parameters
    ----------
    sample : ndarray of shape (N,)
        The 1-D observations.  Flattened to 1-D if multi-dimensional.
    confidence : float, optional
        Coverage probability in (0, 1); default 0.95 for a 95 percent
        two-sided interval.

    Returns
    -------
    ci : ConfidenceInterval
        Named tuple with ``lower``, ``upper``, ``centre`` (sample mean),
        ``confidence_level``, and ``n``.

    Raises
    ------
    ValueError
        If the sample has fewer than 2 observations (degrees of freedom = 0).

    Examples
    --------
    >>> import numpy as np
    >>> rng = np.random.default_rng(0)
    >>> ci = confidence_interval_mean(rng.normal(0, 1, 100))
    >>> ci.lower < 0 < ci.upper   # zero should be inside the 95% CI
    True
    """
    x = sample.ravel().astype(np.float64)
    n = x.size
    if n < 2:
        raise ValueError(
            "confidence_interval_mean: need at least 2 observations (got {n})."
        )
    mean = x.mean()
    se = x.std(ddof=1) / np.sqrt(n)
    # scipy.stats.t.interval returns (lower, upper) centred on `loc` with
    # standard error `scale` for the given coverage level.
    lower, upper = stats.t.interval(confidence, df=n - 1, loc=mean, scale=se)
    return ConfidenceInterval(
        lower=float(lower),
        upper=float(upper),
        centre=float(mean),
        confidence_level=confidence,
        n=n,
    )


