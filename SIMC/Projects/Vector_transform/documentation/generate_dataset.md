# Dataset Generator

## Purpose

`generate_dataset.py` produces a CSV of transformed vectors. A single hidden **ground-truth vector** is transformed 400 times. The CSV contains only the transformed outputs — the ground truth, the displacement direction, and the scalar used per row are not included.

Your task: **recover the original ground-truth vector using only the dataset and your knowledge of the transform.**

## The Transform

The transform is a **scaled translation**:

```
transformed = base + k * p
```

- `base` is the fixed (hidden) ground-truth vector.
- `p` is a **single** displacement direction vector. It is generated **once** at the start of the run and reused for every row. Its components are drawn from a small, undisclosed set of integers.
- `k` is a scalar, chosen **independently for each row** at random from a small, undisclosed finite set of integers (including at least one negative value).

The inverse is straightforward if you know `p` and `k`:

```
base = transformed - k * p
```

But the dataset does not give you `p` or `k` directly. You must recover `base` from the statistical structure of the data alone.

## What the Dataset Contains

- **400 rows**, each a transformed n-dimensional vector
- **Header row** with column labels `t_0, t_1, ..., t_{n-1}`
- All values are integers
- The file is saved as `outputs/dataset.csv`

## What is Hidden

- The ground-truth vector `base`
- The displacement direction vector `p`
- The scalar `k` used for each row
- The specific set of allowed values for `p`'s components and for `k`

## Hints for Recovery

Since every row is `base + k * p` for a fixed `p` and a random discrete `k`:

- All 400 points lie on a **single straight line** in n-D space, passing through `base` with direction `p`
- The line is sampled at only a handful of distinct positions (one per value of `k`), so the dataset has a small number of **distinct rows**, each repeated many times
- Counting the unique rows tells you how many values `k` can take
- Differences between unique rows are integer multiples of `p` — this lets you recover the direction up to sign and scale
- Once you have `p` (up to scale) and the set of `k` values, the ground truth `base` is the point on the line that corresponds to any specific `k` — you still need one more constraint to pin down exactly which point on the line is `base`

## Running

```bash
python Code/Vector_transform/source/generate_dataset.py
```

Output goes to `Code/Vector_transform/outputs/dataset.csv`.
