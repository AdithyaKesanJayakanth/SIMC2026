---
tags:
  - simc
---

# Vector norm and distance

> [!abstract] In one line
> The norm is the length of a vector (Pythagoras generalized to any number of dimensions); distance between two points is the norm of the vector connecting them.

## The idea

In 2D you know Pythagoras: a point at $(3, 4)$ is $\sqrt{3^2 + 4^2} = 5$ units from the origin. The **norm** is exactly that idea, stretched to $n$ dimensions.

Think of a vector as an array. The norm is:

```
length = 0
for i in range(n):
    length += x[i] ** 2
length = length ** 0.5
```

**Distance** between two samples (two arrays) is the norm of their difference — how far apart they sit in $n$-dimensional space.

A **unit vector** is a vector whose norm equals exactly 1 — like rescaling any arrow so it points the same way but has length 1. You divide every entry by the original length.

