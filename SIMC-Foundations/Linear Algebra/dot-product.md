---
tags:
  - simc
---

# Dot product

> [!abstract] In one line
> Multiply two vectors entry-by-entry, add everything up, get one number that measures how much the two vectors point the same way.

## The idea

Imagine two lists of numbers — say, intensity readings at $n$ wavelengths for two different samples. The dot product is the programmer's answer to "how similar are these lists?"

```
sum = 0
for i in range(n):
    sum += a[i] * b[i]
# sum IS the dot product
```

The result is a single number (a **scalar**), not a new vector. Think of it as a similarity score:
- Big positive → both lists "go up together"
- Near zero → the lists are unrelated (perpendicular)
- Negative → when one is large, the other tends to be small

