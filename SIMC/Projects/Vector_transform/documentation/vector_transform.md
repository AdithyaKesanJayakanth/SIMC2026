# Reversible Vector Transform

## Mathematical Basis

The transform is a **scaled translation**: shift a vector along a fixed direction `p` by a scalar factor `k`.

```
transform(v, p, k)         = v + k * p
inverse_transform(v, p, k) = v - k * p
```

Because addition is exact on integers (and exact up to machine epsilon on floats), the transform is perfectly reversible as long as both `p` and `k` are known.

## Why This Transform?

- **Exactly reversible** — adding then subtracting `k*p` is an identity operation
- **Parameterised by two pieces** — a direction vector `p` and a scalar `k`
- **Discrete key** — when `k` is drawn from a small finite set, the transformed points form a structured pattern along the line `base + k*p`
- **Dimension-agnostic** — works for any n-D vector as long as `v` and `p` share the same length

## Implementation

- `translate(vec, p)` — core routine: returns `vec[i] + p[i]` coordinate-by-coordinate
- `transform(vec, p, k)` — scales `p` by `k`, then calls `translate`
- `inverse_transform(vec, p, k)` — scales `p` by `-k`, then calls `translate` to undo the shift
- Pure stdlib; no `numpy` or external dependencies

## Running

```bash
python Code/Vector_transform/source/vector_transform.py
```

Prints the original vector, the chosen `p` and `k`, the transformed vector, and the recovered vector (which should match the original).
