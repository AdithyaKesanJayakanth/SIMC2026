# Distance Functions — External Documentation

**File:** `distance_functions.py`
**Purpose:** SIMC Programming Homework — Euclidean distance between n-dimensional points

---

## Overview

This file contains two functions for computing Euclidean distance between points in n-dimensional space.

`euclidean_distance` computes the straight-line distance between two individual points.

`alldistances` uses `euclidean_distance` to compute the distance between every unique pair of points in a list.

---

## Background

The Euclidean distance between two points p1 and p2 in n-dimensional space is defined as:

```
d = sqrt( (p1[0]-p2[0])² + (p1[1]-p2[1])² + ... + (p1[n]-p2[n])² )
```

This is a generalisation of the Pythagorean theorem to any number of dimensions. For example in 2D it is the hypotenuse of a right triangle. In 3D it extends to three axes, and so on.

---

## Functions

### `euclidean_distance(p1, p2)`

Computes the Euclidean distance between two points.

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| p1 | list or tuple of numbers | First point. Example: `[1, 2, 3]` |
| p2 | list or tuple of numbers | Second point. Must have the same number of dimensions as p1. |

**Returns**

`float` — the distance between p1 and p2, or `None` if inputs are invalid.

**Robustness checks (in order)**

| Check | Situation | Behaviour |
|-------|-----------|-----------|
| None check | Either point is None | Prints error, returns None |
| Type check | Either point is not a list or tuple | Prints error, returns None |
| Empty check | Either point has no coordinates | Prints error, returns None |
| Dimension check | Points have different number of coordinates | Prints error, returns None |
| Coordinate check | Any coordinate is not an int or float | Prints error, returns None |

**Examples**

```python
euclidean_distance([0, 0], [3, 4])
# returns 5.0

euclidean_distance([0, 0, 1], [3, 0, 8])
# returns sqrt(9 + 0 + 49) = sqrt(58) ≈ 7.616

euclidean_distance(None, [1, 2])
# prints error, returns None

euclidean_distance([1, 2], [1, 2, 3])
# prints error, returns None

euclidean_distance([1, "a"], [2, 3])
# prints error, returns None
```

---

### `alldistances(points)`

Computes the Euclidean distance between every unique pair of points in a list.

For a list of n points this produces n×(n-1)/2 unique pairs. Each pair (i, j) is only computed once — (j, i) is never repeated.

**Time complexity: O(n²)**
This is mathematically unavoidable when computing all pairs. For every point in the list you must compare it against every other point, which requires two nested loops.

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| points | list of lists or list of tuples | A collection of points, all with the same number of dimensions. Example: `[[0,0], [3,4], [0,4]]` |

**Returns**

`dict` — keys are `(i, j)` index tuples, values are the distances between those points. Returns `None` if the list has fewer than 2 points.

**Robustness checks**

| Situation | Behaviour |
|-----------|-----------|
| List is empty or has only 1 point | Returns None |
| A specific pair fails in euclidean_distance | That pair is skipped, rest continue |

**Examples**

```python
alldistances([[0, 0], [3, 4], [0, 4]])
# returns {(0,1): 5.0, (0,2): 4.0, (1,2): 3.0}

alldistances([[0,0,1], [3,0,8], [0,4,4]])
# returns {(0,1): 7.616, (0,2): 5.0, (1,2): 7.549}

alldistances([[0, 0]])
# returns None
```

---

## How the functions relate

`alldistances` calls `euclidean_distance` internally for each pair. All robustness checks inside `euclidean_distance` are therefore automatically applied to every pair computed by `alldistances`.

```
alldistances(points)
    └── for every unique pair (i, j):
            └── euclidean_distance(points[i], points[j])
```

---

## Limitations

- Only lists and tuples are accepted as point inputs. Other iterables will be rejected by the type check.
- Coordinates must be integers or floats. Strings or other types will cause that pair to be skipped in `alldistances`.
- `alldistances` returns None silently when given fewer than 2 points. A print statement could be added for better clarity.
- Time complexity is O(n²). For very large lists this will be slow. There is no known way to reduce this when all pairs must be computed.
