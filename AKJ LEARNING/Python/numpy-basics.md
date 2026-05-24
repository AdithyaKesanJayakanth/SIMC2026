---
tags:
  - simc
---

# NumPy Basics

## What it is

NumPy is Python's array library — the foundation of nearly every scientific Python tool you'll touch (pandas, scipy, scikit-learn, PyTorch, JAX all sit on top of it). If you do anything numerical in Python that isn't trivial, you're using NumPy directly or indirectly.

The core object is the ==ndarray== (N-dimensional array): a ==homogeneous-type, contiguous-memory, fixed-shape== block of numbers. "Homogeneous" means every element is the same type (all `float64`, all `int32`, etc.) — unlike a Python list, which can mix ints, strings, dicts, and other lists. "Contiguous" means the data sits in one flat slab of memory, not scattered around the heap with pointer-chasing. That layout is what makes ndarrays fast.

The killer feature is ==vectorization==: operations apply to the whole array at once, without explicit loops. `arr * 2` doubles every element. `arr1 + arr2` adds them pairwise. This is both faster (the loop runs in C, not Python) AND more readable than the equivalent for-loop or list comprehension.

```python
# Python list: needs a comprehension
doubled = [x * 2 for x in my_list]

# NumPy: just multiply
doubled = arr * 2
```

## Why ndarrays beat Python lists

| Property | Python `list` | NumPy `ndarray` |
|---|---|---|
| Element type | Mixed (anything) | Homogeneous (one dtype) |
| Memory layout | Scattered (list of pointers) | Contiguous flat block |
| Speed (1M elements) | Slow (Python loop) | ~50-100x faster (C loop) |
| Math on whole array | `[x * 2 for x in xs]` | `arr * 2` |
| Element-wise add | `[a + b for a, b in zip(xs, ys)]` | `xs + ys` |
| Memory per int | ~28 bytes (Python object) | 8 bytes (`int64`) |
| Resizable | Yes (`.append()`) | No (fixed shape) |

> [!info] When to use which
> Use Python lists for small, mixed-type, frequently-resized data. Use ndarrays for anything numerical, large, or where you'll do math on every element.

## Java analogy

An ndarray is like a Java `double[]` or `int[][]` — fixed type, fixed shape, stored as a contiguous block — BUT with operator overloading. Java arrays force you to write the loop yourself; NumPy hides it.

```java
// Java: explicit loop required
double[] arr = new double[1000];
for (int i = 0; i < arr.length; i++) {
    arr[i] = arr[i] * 2;
}
```

```python
# NumPy: no loop visible
arr = arr * 2
```

Same operation, same O(n) cost — but NumPy's loop runs in compiled C, not interpreted Python, so it's typically 50-100x faster than the equivalent Python `for` loop. The Java loop is fast too (JIT-compiled), but it's still verbose.

## Creating arrays

```python
import numpy as np

np.array([1, 2, 3])           # from a Python list
np.array([[1, 2], [3, 4]])    # 2D from a nested list

np.zeros(5)                   # 1D: array([0., 0., 0., 0., 0.])
np.zeros((3, 4))              # 2D: 3 rows, 4 columns of zeros
np.ones(5)                    # array of ones
np.full((2, 3), 7)            # 2x3 array filled with 7

np.arange(0, 10, 2)           # like range: array([0, 2, 4, 6, 8])
np.linspace(0, 1, 5)          # 5 evenly-spaced points: [0., 0.25, 0.5, 0.75, 1.]

np.empty((3, 3))              # uninitialized — fast but contents are garbage
```

> [!tip] `arange` vs `linspace`
> `np.arange(start, stop, step)` is `stop`-EXCLUSIVE and you specify the step. `np.linspace(start, stop, num)` is `stop`-INCLUSIVE and you specify how many points. Use `linspace` when you want a known number of samples; use `arange` when you want a known step.

## Inspecting arrays

Every ndarray carries metadata:

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])

arr.shape    # (2, 3) — tuple of dimensions
arr.ndim     # 2 — number of dimensions
arr.size     # 6 — total elements
arr.dtype    # dtype('int64') — element type
```

> [!warning] Shape is a tuple — mind the trailing comma
> A 1D array of length 5 has shape `(5,)` — note the comma. `(5)` in Python is just the integer 5 in parens; `(5,)` is a 1-tuple. This trips people up when constructing arrays: `np.zeros(5)` and `np.zeros((5,))` both work, but `np.zeros((3, 4))` requires the tuple form because shapes with multiple dimensions must be tuples.

## Indexing and slicing

Just like Python lists, with extensions for multi-D:

```python
arr = np.array([10, 20, 30, 40, 50])

arr[0]        # 10
arr[-1]       # 50 (last)
arr[1:4]      # array([20, 30, 40])
arr[:3]       # array([10, 20, 30])
arr[::2]      # array([10, 30, 50]) — every other
arr[::-1]     # array([50, 40, 30, 20, 10]) — reversed

# 2D
mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
mat[1, 2]     # 6 — row 1, col 2 (preferred)
mat[1][2]     # 6 — also works but slower (creates intermediate row)
mat[1, :]     # array([4, 5, 6]) — full row 1
mat[:, 2]     # array([3, 6, 9]) — full column 2
mat[0:2, 1:]  # 2x2 submatrix
```

> [!warning] Slices return VIEWS, not copies
> ==Modifying a slice modifies the original array.== This is a major difference from Python lists (which return copies on slice). If you need an independent copy, call `.copy()` explicitly.
> ```python
> arr = np.array([1, 2, 3, 4, 5])
> sub = arr[1:4]
> sub[0] = 999
> print(arr)  # array([  1, 999,   3,   4,   5]) — original mutated!
> ```

