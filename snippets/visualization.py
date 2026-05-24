"""SIMC 2026 -- Reference Snippets: Visualization

Publication-ready plots for exploratory data analysis: heatmap, histogram,
scatter plot, Pearson correlation matrix, and clustering scatter plot.

Design principles
=================

Every function accepts a NumPy array as its primary data argument and a
``Path``-like output path.  Plots are saved as PNG at 150 dpi; the ``(fig,
ax)`` pair is also returned so the caller can apply additional formatting
(extra annotations, custom legends, axis rescaling) before calling
``fig.savefig`` again.  Nothing is printed to stdout and no figure windows are
opened, making these functions safe to call in headless server environments.

Titles and axis labels have sensible defaults that can be overridden via
keyword arguments.  Parent directories are created automatically if they do not
exist.

Dependencies
============

    numpy        -- array input
    matplotlib   -- all rendering
    scipy        -- not needed here; import only in the correlation helper if
                    the caller wants p-values alongside Pearson r

Quick-reference
===============

    plot_heatmap(matrix, path)                        2-D colour map
    plot_histogram(values, path)                      1-D frequency / density
    plot_scatter(x, y, path, labels=...)              2-D point cloud
    plot_correlation_matrix(data, path)               Pearson r grid
    plot_clustering(data, labels, path)               colour-coded clusters
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")   # non-interactive backend; safe in headless environments
import matplotlib.pyplot as plt


# =============================================================================
# Heatmap
# =============================================================================

def plot_heatmap(
    matrix: np.ndarray,
    output_path: str | Path,
    *,
    title: str = "Heatmap",
    xlabel: str = "Column",
    ylabel: str = "Row",
    cmap: str = "viridis",
    annotate: bool = False,
) -> tuple[plt.Figure, plt.Axes]:
    """Render a 2-D NumPy array as a colour-mapped heatmap and save to disk.

    Each cell (i, j) is coloured by ``matrix[i, j]`` using the supplied
    colourmap.  A colourbar is appended to the right of the axes so the reader
    can decode the scale without inspecting the raw values.  Figure dimensions
    scale with the matrix aspect ratio (capped at 12 × 10 inches) so that
    neither very wide nor very tall matrices produce a squashed image.

    When ``annotate=True`` each cell is labelled with its value, formatted to
    two decimal places.  This is only readable for small matrices (N <= ~15);
    for larger matrices leave ``annotate=False`` (the default).

    Parameters
    ----------
    matrix : ndarray of shape (M, N)
        The 2-D data to visualise.  Non-finite values (``np.nan``,
        ``np.inf``) are rendered as white (masked) by matplotlib.
    output_path : str or Path
        Destination PNG file path.  Parent directories are created if absent.
    title : str, optional
        Axes title; default ``"Heatmap"``.
    xlabel, ylabel : str, optional
        Axis labels; defaults ``"Column"`` and ``"Row"``.
    cmap : str, optional
        Matplotlib colourmap name; default ``"viridis"``.  Use ``"RdBu_r"``
        for data that spans negative to positive values (e.g. correlations).
    annotate : bool, optional
        If ``True``, print each cell's numeric value inside the cell;
        default ``False``.

    Returns
    -------
    fig : Figure
    ax  : Axes
    """
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    m, n = matrix.shape
    fig_w = min(2.0 + n * 0.5, 12.0)
    fig_h = min(2.0 + m * 0.5, 10.0)

    fig, ax = plt.subplots(figsize=(fig_w, fig_h))
    im = ax.imshow(matrix.astype(float), aspect="auto", cmap=cmap)
    fig.colorbar(im, ax=ax, shrink=0.8)

    if annotate:
        for i in range(m):
            for j in range(n):
                ax.text(j, i, f"{matrix[i, j]:.2f}", ha="center", va="center", fontsize=7)

    ax.set_title(title, fontsize=11)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    fig.tight_layout()
    fig.savefig(output_path, dpi=150)
    plt.close(fig)
    return fig, ax


# =============================================================================
# Histogram
# =============================================================================

def plot_histogram(
    values: np.ndarray,
    output_path: str | Path,
    *,
    bins: int | str = "auto",
    title: str = "Histogram",
    xlabel: str = "Value",
    ylabel: str = "Frequency",
    density: bool = False,
    color: str = "#4C72B0",
) -> tuple[plt.Figure, plt.Axes]:
    """Plot a histogram of a 1-D sample and save to disk.

    The histogram uses NumPy's ``"auto"`` bin rule by default, which picks
    between the Sturges and Freedman--Diaconis estimators depending on sample
    size and spread.  Setting ``density=True`` normalises the y-axis to a
    probability density so the histogram integrates to 1 and can be overlaid
    with a fitted PDF (e.g. the output of ``fit_normal`` from
    ``statistical_tools.py``).

    Multi-dimensional inputs are silently flattened to 1-D before binning.

    Parameters
    ----------
    values : ndarray of shape (N,) or (M, N)
        The sample observations.  Non-finite values are included in the
        computation and will shift the bin range; remove them beforehand if
        undesirable.
    output_path : str or Path
        Destination PNG file path.
    bins : int or str, optional
        Number of equal-width bins or NumPy binning strategy (e.g.
        ``"auto"``, ``"fd"``, ``"sturges"``); default ``"auto"``.
    title, xlabel, ylabel : str, optional
        Axes labels; see defaults above.  ``ylabel`` is overridden to
        ``"Density"`` when ``density=True``.
    density : bool, optional
        Normalise to probability density; default ``False`` (raw counts).
    color : str, optional
        Bar fill colour; default ``"#4C72B0"`` (Seaborn blue).

    Returns
    -------
    fig : Figure
    ax  : Axes
    """
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.hist(
        values.ravel(),
        bins=bins,
        density=density,
        color=color,
        edgecolor="white",
        linewidth=0.5,
    )
    ax.set_title(title, fontsize=11)
    ax.set_xlabel(xlabel)
    ax.set_ylabel("Density" if density else ylabel)
    fig.tight_layout()
    fig.savefig(output_path, dpi=150)
    plt.close(fig)
    return fig, ax


