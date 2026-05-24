# Session 10 — Grid-Based Drainage Simulation

## Overview

This script simulates water flow across a 3x3 terrain grid over discrete time steps. Each cell has a terrain type (lowland, mountain, or ocean) that determines how it receives, absorbs, and transfers water. The simulation models rainfall accumulation on mountains, ground absorption across all cells, and lateral water transfer from overflowing cells to their neighbours.

## Problem Description

A simplified 2D landscape is represented as a grid of cells. Rain falls on elevated terrain (mountains), water drains into the ground at each cell, and any excess water beyond a cell's capacity flows outward to adjacent cells. Over many time steps the system reaches a steady state where inflow and outflow balance.

## Terrain Types

| Terrain   | Rainfall | Capacity | Drain Rate | Transfer Rate |
|-----------|----------|----------|------------|---------------|
| Lowland   | 0.0      | 100.0    | 5.0        | 1.0           |
| Mountain  | 100.0    | 20.0     | 10.0       | 24.0          |
| Ocean     | 0.0      | inf      | 0.0        | 0.0           |

- **Rainfall**: water added to the cell each time step.
- **Capacity**: maximum water a cell can hold before excess spills to neighbours.
- **Drain Rate**: water absorbed into the ground (removed from the system) each step.
- **Transfer Rate**: maximum water that can flow out of the cell per step when over capacity.

## Grid Layout

```
(0,0) lowland    (0,1) lowland    (0,2) lowland
(1,0) lowland    (1,1) mountain   (1,2) lowland
(2,0) lowland    (2,1) lowland    (2,2) ocean
```

The mountain sits at the centre, and the ocean acts as a sink in the bottom-right corner.

## Classes

### `square`

Represents a single grid cell.

**Constructor parameters:**
- `row` (int) — row index in the grid.
- `col` (int) — column index in the grid.
- `name` (str) — terrain type: `"lowland"`, `"mountain"`, or `"ocean"`.

**Attributes:**
- `water0` — current water level (starts at 0).
- `rainfall` — water added per time step.
- `capacity` — maximum water before overflow.
- `drain_rate` — water absorbed into the ground per step.
- `transfer_rate` — maximum outflow per step.

**Methods:**
- `rainfall_apply()` — adds one step of rainfall to the cell.
- `drain()` — removes up to `drain_rate` water (ground absorption). Water cannot go below 0.

## Functions

### `neighbour(row, col)`

Returns a list of orthogonally adjacent `square` objects (up/down/left/right). Uses Manhattan distance == 1 to identify neighbours.

### `waterdisplay(terrain)`

Prints the water level of every cell in a grid layout for visual inspection.

### `global_update(terrain, time)`

Advances the simulation by `time` steps. Each step has three phases:

1. **Rainfall** — every cell receives its per-step rainfall amount.
2. **Drainage** — each cell absorbs water into the ground (up to its drain rate).
3. **Transfer** — cells whose water exceeds capacity push excess to neighbours.
   - Excess = `water0 - capacity`.
   - Transferable amount is capped at the cell's `transfer_rate`.
   - The transferable amount is split equally among 4 potential neighbours (share = transferable / 4).
   - Each neighbour receives at most its remaining capacity (`capacity - water0`).
   - A separate delta dictionary ensures all transfers are calculated before any are applied (simultaneous update — no cascading within a single step).

## Execution

The script runs the simulation for **1000 time steps**, then prints the final water levels across the grid using `waterdisplay()`.

## Dependencies

- `math` (standard library) — used for `math.inf` (ocean capacity).
