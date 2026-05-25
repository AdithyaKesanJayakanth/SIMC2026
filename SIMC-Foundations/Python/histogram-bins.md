---
tags:
  - simc
---

# Choosing Histogram Bins

> [!abstract] Prerequisites
> [[matplotlib-basics]] — assumes you know `ax.hist()`.
> [[numpy-basics]] — uses `np.arange`.

## What `bins` does

`bins=N` (integer) divides your data's range into $N$ equal-width buckets and counts samples in each. The choice controls how much you **smooth** vs how much **detail** you see.

| Too few bins | Just right | Too many bins |
|---|---|---|
| Oversmoothed | Shape clear, noise low | Noisy, jagged |
| Loses structure | Tells the story | Tells no story |

## The two regimes

### 1. Continuous data → use a rule of thumb

For floats (heights, temperatures, normal samples, etc.), pick by formula or let matplotlib decide:

| Rule | Formula | When |
|---|---|---|
| **Sqrt** | $k = \sqrt{N}$ | Simple, works OK most of the time |
| **Sturges** | $k = \log_2(N) + 1$ | Small N, near-normal data |
| **Freedman-Diaconis** | $\text{width} = 2 \cdot \text{IQR} / N^{1/3}$ | Robust to outliers; what `bins='auto'` uses |

Or just delegate:

```python
ax.hist(samples, bins='auto')   # matplotlib chooses for you (uses FD)
```

For 10,000 continuous samples, `'auto'` usually picks ~50 bins.

### 2. Discrete data → snap bins to integer edges

==This is the case that trips everyone up.==

If your data is integer-valued (counts, dice rolls, streak lengths), `bins=10` will divide the *range* into 10 equal-width bins. If the range is 0-20, bin edges land at 0, 2, 4, ..., 20 — so two integer values cram into each bar. You lose information and the histogram looks chunky.

The fix: place bin edges at the **half-integers** so each integer value gets its own bin, centered on it:

```python
ax.hist(streak_lengths, bins=np.arange(0.5, 20.5, 1), edgecolor='black')
```

Produces edges `[0.5, 1.5, 2.5, ..., 19.5]`. Each integer from 1 to 19 gets a clean bar.

> [!tip] General formula for integer data
> ```python
> bins=np.arange(data.min() - 0.5, data.max() + 1.5, 1)
> ```
> Snaps the bins exactly to integer values regardless of your data range.

