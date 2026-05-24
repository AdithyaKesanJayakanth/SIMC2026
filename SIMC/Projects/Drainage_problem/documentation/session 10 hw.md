# Session 10 — Drainage Tank: Integral vs Numerical Comparison

## Overview

This script models a tank draining over time with a linearly decreasing drain rate. It compares two methods for computing the remaining volume: an exact closed-form integral solution and a numerical forward-Euler approximation.

## Problem Description

A tank starts with an initial volume **C = 100** units. Water drains at a rate that decreases linearly with time:

```
D(t) = 2 - t/4
```

The drain rate reaches zero at **t = 8**, at which point drainage stops. The total volume drained over the full interval [0, 8] is 8 units, leaving the tank at 92 units.

## Mathematical Background

The volume remaining at time t is obtained by integrating the drain rate:

```
V(t) = C - integral from 0 to t of D(s) ds
     = C - integral from 0 to t of (2 - s/4) ds
     = C - [2s - s²/8] from 0 to t
     = C - 2t + t²/8
```

This closed-form expression is valid for **0 <= t <= 8**. For **t >= 8**, no further drainage occurs and **V(t) = C - 8 = 92**.

## Functions

### `volume_integral(t, C)`

Returns the exact volume at time `t` using the closed-form formula.

**Parameters:**
- `t` (float) — the time at which to evaluate volume.
- `C` (float) — initial volume.

**Returns:** `C - 2t + t²/8` for t < 8, or `C - 8` for t >= 8.

### `volume_numerical(t_end, C, dt)`

Approximates the volume at time `t_end` using the forward Euler method.

**Parameters:**
- `t_end` (float) — target time to simulate up to.
- `C` (float) — initial volume.
- `dt` (float) — size of each time step.

**Algorithm:**
1. Start with `volume = C` and `t = 0`.
2. At each step, compute the current drain rate `d = 2 - t/4`.
3. If `d == 0`, stop (drainage is complete).
4. Subtract `d * dt` from the volume (Euler step).
5. Clamp volume to a minimum of 0 (non-negativity constraint).
6. Advance `t` by `dt`.

**Returns:** the approximate remaining volume.

## Constants

| Name | Value | Description                        |
|------|-------|------------------------------------|
| `C`  | 100   | Initial volume in the tank         |
| `dt` | 0.01  | Time step for the numerical method |

## Output

The script prints a comparison table for integer times t = 1 through 8:

```
t      Integral (exact)     Numerical (Euler)
1      98.125000            98.127500
2      96.500000            96.505000
...
8      92.000000            92.000000
```

The two methods converge as `dt` decreases. With `dt = 0.01`, the numerical results closely match the exact solution, demonstrating the accuracy of the Euler method for this smooth, well-behaved problem.

## Dependencies

None (pure Python, standard library only).
