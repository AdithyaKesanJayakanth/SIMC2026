---
tags:
  - simc
---

# Floating-point precision

> [!abstract] In one line
> Computers store real numbers with ~16 significant decimal digits (64-bit "double"), so every arithmetic result carries a rounding error of about $10^{-16}$ relative to the true value.

## The idea

A real number like $\pi = 3.14159265358979\ldots$ has infinitely many decimal places. A computer's 64-bit float stores only ~15.9 of them. The rest is rounded off. This is not a bug — it is a fundamental physical constraint of finite memory.

The key number to memorise: **machine epsilon** $\varepsilon_\text{mach} \approx 2.2 \times 10^{-16}$. Any two floating-point numbers that differ by less than $\varepsilon_\text{mach}$ times their magnitude are *indistinguishable* to the computer.

This becomes critical when:
1. You claim two independently computed quantities should be equal (numerical verification).
2. An algorithm's correctness depends on distinguishing numbers that are nearly equal (eigenvalue ordering).

```python
import sys
print(sys.float_info.epsilon)   # 2.220446049250313e-16
# Two "equal" numbers up to machine precision:
a = 1.0
b = 1.0 + 1e-17   # b == a in floating point!
print(a == b)     # True — the difference is below epsilon
```

