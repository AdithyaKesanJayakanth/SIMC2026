---
tags:
  - simc
---

# What is a dimension

> [!abstract] In one line
> A dimension is just one slot in your vector — the number of dimensions equals the number of features, which equals the length of the array that describes one data point.

## The idea

Imagine giving someone directions to a spot:

- **1D:** "Go 3 metres forward." One number tells you everything. A number line.
- **2D:** "Go 3 east, 5 north." Two numbers. A flat map.
- **3D:** "Go 3 east, 5 north, 2 up." Three numbers. The real world.

The pattern: **dimension = how many numbers you need to pin down one point = the length of the vector.**

Now consider an IR spectrum. The instrument fires infrared light at a sample and measures how much is absorbed at, say, 1000 different wavenumbers. One sample produces 1000 readings:

```python
spectrum = np.zeros(1000)   # one sample = one vector of length 1000
```

That single sample is a **point in 1000-dimensional space**. You cannot draw it. Your brain cannot picture it. That is fine — mathematics works perfectly in any number of dimensions, even billions.

> [!note] "High-dimensional data"
> When people say a dataset is high-dimensional, they just mean each data point is described by a long vector — many features per sample. IR spectra are a classic example.

