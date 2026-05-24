# Dataset Generator (v2 — weighted)

## Purpose

`generate_dataset_2.py` produces a second CSV of transformed vectors using the **same translation transform** as `generate_dataset.py`, but with two differences:

1. A **larger** set of allowed `k` values (11 instead of 5).
2. `k` is no longer drawn uniformly. It is drawn from a **discrete Gaussian** centered at `0`, so values near the ground truth are sampled much more often than far ones.

Your task: **recover a different (also hidden) ground-truth vector `BASE_TRUTH_2` using only this dataset.** The intended solving strategy is statistical — use the frequency of each unique row, not just its existence.

## The Transform

Same as v1:

```
transformed = base + k * p
```

- `base` is `BASE_TRUTH_2` — fixed, hidden, distinct from the v1 base.
- `p` is a single displacement vector, generated once per run from `P_VALUES`.
- `k` is now drawn for each row from `K_CHOICES = [-5, -4, ..., 4, 5]` with a non-uniform weight.

## The Weighting

Each candidate `k` is given a weight from the **discrete Gaussian** formula:

```
w(k) = exp( -k^2 / (2 * sigma^2) )
```

with `sigma = 1.5`. This produces relative weights that look like:

| k     | weight (relative) |
|-------|-------------------|
|  0    | 100%              |
| ±1    | ~80%              |
| ±2    | ~41%              |
| ±3    | ~14%              |
| ±4    | ~3%               |
| ±5    | ~0.4%             |

Python's `random.choices(K_CHOICES, weights=...)` then picks each `k` with probability proportional to its weight (it normalizes internally).

A typical 400-point run produces a clean bell shape:

```
k=-5 ( 1)
k=-4 ( 2)
k=-3 (15)  *****
k=-2 (58)  **********************
k=-1 (86)  **********************************
k= 0 (101) ****************************************
k= 1 (77)  ******************************
k= 2 (43)  *****************
k= 3 (15)  *****
k= 4 ( 2)
k= 5 ( 0)
```

## What the Dataset Contains

- **400 rows**, each a 5-dimensional integer vector
- Header row `t_0, t_1, t_2, t_3, t_4`
- Saved to `outputs/dataset_2.csv`
- The `k` column is **not** written to the file — it stays secret to a solver

## What is Hidden

- The ground-truth vector `BASE_TRUTH_2`
- The displacement vector `p`
- The exact `k` chosen on each row

What is **public** in the source file:
- `K_CHOICES`, `P_VALUES`, `SIGMA`, `SEED`, `N_POINTS`
- The fact that the sampling is a discrete Gaussian centered at `k = 0`

## Why Frequency Now Leaks the Answer

In v1, `k` was uniform over 5 values, so each unique row appeared roughly `400 / 5 ≈ 80` times. Frequency told you nothing — every line position was equally common, and you needed sort+median or brute force.

In v2, the row corresponding to `k = 0` **is the ground truth itself**, and it is sampled most often. Counting unique rows gives a frequency profile that mirrors the Gaussian — the most frequent row is the base.

## Recovery Strategy

```text
1. Read all 400 rows from dataset_2.csv
2. Count how many times each unique row appears
3. The unique row with the highest count is BASE_TRUTH_2
```

Optional consistency check (uses the structure, not the frequency):

```text
4. Differences between unique rows should all be integer multiples of p
5. Sorting unique rows along p should give a clean line of 11 points,
   spaced one p apart (some may be missing if very rare k values weren't drawn)
```

In a 400-point run, very rare `k` values (e.g. ±5) may produce **zero** rows. That is expected — Gaussian tails are thin. The recovery method does not need every `k` value to appear.

## Connection to SIMC 2024

The 2024 SIMC paper's challenge involved rotating proteins. The data was sampled in a way that weighted certain rotations (e.g. 90°) more than others, because of an energy-based likelihood model. The champion solution used **Bayesian probability** — the most likely rotation, given the weighted distribution, indicates the original orientation.

This v2 generator is a stripped-down version of the same idea:

- v1 = uniform sampling → solve with sort+median or brute force
- v2 = weighted sampling → solve with frequency / Bayesian intuition

## Running

```bash
python Code/Vector_transform/source/generate_dataset_2.py
```

Output goes to `Code/Vector_transform/outputs/dataset_2.csv`. The script also prints `BASE_TRUTH_2`, the chosen `p`, and the empirical k-frequency histogram for the run.

## Tuning Knobs

- **`SIGMA`** — smaller σ sharpens the peak at `k = 0` (easier to solve), larger σ flattens it toward uniform (harder).
- **`K_CHOICES`** — widening this beyond `[-5, 5]` adds more rare tail rows but does not change the recovery strategy.
- **`N_POINTS`** — fewer points means the rare `k` values are more likely to be entirely absent; the most-frequent-row strategy still works as long as the peak is reliably populated.
