"""SIMC 2026 -- Reference Snippets: Data Loading

Functions for loading common scientific data formats (CSV, NPZ, TXT, JSON)
into NumPy arrays and Python data structures.  Each loader follows the same
pattern: accept a filesystem path, validate the file, load the payload, and
return it in a predictable type so callers never have to inspect raw bytes.

Formats covered
===============

CSV  -- delimiter-separated tabular data; returns a NumPy float64 array plus
        a header list so column names travel with the matrix.
NPZ  -- NumPy's native compressed archive; returns the raw NpzFile so all
        named arrays are accessible by key without loading everything at once.
TXT  -- whitespace-delimited plain text produced by ``np.savetxt``; returns a
        NumPy float64 array suitable for direct computation.
JSON -- arbitrary nested data from a JSON file; returns a Python dict / list
        so that structured records (e.g. SIMC summary files) can be read back
        verbatim.

Usage example
=============

    data, headers = load_csv("data/input/scores.csv")
    archive       = load_npz("data/input/sample.npz")
    X             = archive["sample_larger"]
    matrix        = load_txt("data/input/matrix.txt")
    summary       = load_json("data/output/task8/task8_summary.json")
"""

from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any

import numpy as np


# =============================================================================
# CSV
# =============================================================================

def load_csv(
    path: str | Path,
    *,
    delimiter: str = ",",
    has_header: bool = True,
) -> tuple[np.ndarray, list[str]]:
    """Load a delimiter-separated value file into a NumPy float64 array.

    The loader reads the optional header row separately so that column names
    are returned alongside the data matrix.  All remaining rows are cast to
    ``float64``; cells that are empty or cannot be parsed (e.g. ``"N/A"``,
    ``""``) become ``np.nan`` so downstream functions receive a clean float
    array rather than raising at load time.

    Parameters
    ----------
    path : str or Path
        Path to the CSV (or TSV) file.
    delimiter : str, optional
        Field separator; default ``","``; use ``"\\t"`` for tab-separated files.
    has_header : bool, optional
        If ``True`` (default) the first row is treated as column names and
        returned in ``headers``; if ``False`` an empty list is returned and
        every row is parsed as numeric data.

    Returns
    -------
    data : ndarray of shape (M, N), dtype float64
        The numeric payload; rows are observations, columns are variables.
        Cells that cannot be cast to float are replaced with ``np.nan``.
    headers : list of str
        Column names extracted from the first row, or ``[]`` when
        ``has_header=False``.

    Notes
    -----
    For very large files (> 10^6 rows) prefer ``np.genfromtxt`` with
    ``dtype=float`` directly, which streams the file without building an
    intermediate list of lists.

    Examples
    --------
    >>> data, headers = load_csv("scores.csv")
    >>> data.shape
    (200, 5)
    >>> headers
    ['student_id', 'q1', 'q2', 'q3', 'q4']
    """
    path = Path(path)
    with path.open(newline="", encoding="utf-8") as fh:
        reader = csv.reader(fh, delimiter=delimiter)
        rows = list(reader)

    if has_header and rows:
        headers: list[str] = rows[0]
        data_rows = rows[1:]
    else:
        headers = []
        data_rows = rows

    def _to_float(cell: str) -> float:
        stripped = cell.strip()
        if stripped == "":
            return np.nan
        try:
            return float(stripped)
        except ValueError:
            return np.nan

    data = np.array(
        [[_to_float(cell) for cell in row] for row in data_rows],
        dtype=np.float64,
    )
    return data, headers


