---
tags:
  - simc
---

# Matplotlib Basics

## What it is

==Matplotlib is Python's default plotting library== — the foundation
everyone learns first, and the thing every other Python plotting tool
either wraps or competes with. It was originally modeled on MATLAB's
plotting interface (which is why so many functions are `plt.this()` and
`plt.that()` — you're calling them on an implicit "current figure"
sitting in global state somewhere).

It has ==two coexisting API styles==:

1. **State-machine style** (`plt.plot`, `plt.xlabel`, `plt.show`) —
   terse, MATLAB-flavored, hidden global state. Fine for quick one-off
   scripts; a mess for anything with multiple subplots.
2. **Object-oriented (OO) style** (`fig, ax = plt.subplots()`, then
   `ax.plot`, `ax.set_xlabel`) — explicit, scalable, the right default.

You'll see both in the wild. ==Write the OO style; learn to read the
state-machine style.==

Alternatives exist — **seaborn** (statistical plots, prettier defaults,
built on top of matplotlib) and **plotly** (interactive, web-native) —
but matplotlib is the bedrock. Pairs with [[numpy-basics]] constantly:
NumPy arrays in, matplotlib plots out.

## Install / import

```python
import matplotlib.pyplot as plt   # the standard alias — always pyplot as plt
import numpy as np                 # almost always paired with NumPy
```

The `plt` alias is universal convention. Stick with it even if it feels
weird — every tutorial, every Stack Overflow answer, every textbook
uses `plt`.

> [!info] No clean Java analog
> Matplotlib has no direct Java equivalent worth comparing to. Java's
> plotting libraries (JFreeChart, XChart) exist but are clunky and
> rarely used outside enterprise. That said, the **pattern** of
> `fig, ax = plt.subplots()` is similar in spirit to Swing:
> "create a JFrame, then add components to it." `fig` is the window,
> `ax` is the panel you draw on.

## The two API styles

### State-machine (older, terse)

```python
plt.plot([1, 2, 3], [4, 5, 6])
plt.xlabel("x")
plt.title("Look ma, no axes object")
plt.show()
```

Matplotlib keeps a "current figure" in hidden global state. Every
`plt.xxx` call mutates it. Concise for a single plot, but as soon as
you want two subplots or want to pass a figure between functions, the
hidden state becomes a debugging nightmare.

### Object-oriented (recommended)

```python
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot([1, 2, 3], [4, 5, 6])
ax.set_xlabel("x")
ax.set_title("Explicit is better than implicit")
plt.show()
```

`fig` is the whole figure (the window/canvas); `ax` is the plotting
area (the actual axes with ticks and data). You call methods on `ax`
instead of going through `plt`. This scales cleanly: want a 2x2 grid?
`fig, axs = plt.subplots(2, 2)` and you get a 2D array of axes objects.

> [!tip] Default to the OO style
> ==Use `fig, ax = plt.subplots()` for everything==, even single
> plots. It's slightly more typing now but saves real pain later when
> you want subplots, custom DPI, multiple legends, or to hand a figure
> off to another function. Tutorials often use the state-machine style
> — learn to read it, but write the OO style yourself.

## The basic plot types

### Line plot

```python
fig, ax = plt.subplots()
xs = np.linspace(0, 2 * np.pi, 100)
ax.plot(xs, np.sin(xs), label="sin(x)")
ax.plot(xs, np.cos(xs), label="cos(x)")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Sine and cosine")
ax.legend()
plt.show()
```

Call `ax.plot` multiple times to overlay lines on the same axes. The
`label=` kwarg is what `ax.legend()` reads.

### Scatter plot

```python
xs = np.random.normal(size=200)
ys = np.random.normal(size=200)
fig, ax = plt.subplots()
ax.scatter(xs, ys, alpha=0.5, s=10)   # alpha = transparency, s = marker size
ax.set_xlabel("x")
ax.set_ylabel("y")
plt.show()
```

Useful kwargs: `alpha` (0 transparent, 1 opaque) for dense point clouds,
`s` for marker size, `c` for color (can be an array — color-by-value).

### Histogram

```python
samples = np.random.normal(loc=0, scale=1, size=10_000)  # 10k Normal samples
fig, ax = plt.subplots()
ax.hist(samples, bins=50, edgecolor="black")
ax.set_xlabel("value")
ax.set_ylabel("count")
ax.set_title("Histogram of 10,000 standard Normal samples")
plt.show()
```

`bins` controls how many buckets — too few hides structure, too many is
noisy. `edgecolor="black"` draws bar borders so adjacent bars are
visually distinct (the default makes them blur together).

### Bar plot

```python
categories = ["A", "B", "C", "D"]
heights = [3, 7, 2, 5]
fig, ax = plt.subplots()
ax.bar(categories, heights)
plt.show()
```

For ==already-bucketed categorical data==. Don't confuse with `hist`
(see common mistakes).

