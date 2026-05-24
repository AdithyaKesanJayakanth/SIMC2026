# Practice Problem 1 — Coffee Cooling

## The Situation

You make a cup of coffee at **90°C**. The room is at **25°C**.
You want to drink it at **60°C** — warm but not scalding.

**How long do you have to wait?**

---

## The Physics (given to you)

Newton's Law of Cooling says:

> The rate at which an object cools is proportional to the difference between its temperature and the room temperature.

In math:

```
dT/dt = -k * (T - T_room)
```

Where:
- `T` = temperature of the coffee at time `t` (in °C)
- `T_room` = room temperature = 25°C (constant)
- `k` = cooling constant (how fast this particular cup cools)
- `t` = time in minutes

Assume `k = 0.05` (a reasonable value for a ceramic mug).

---

## Your Tasks

**Task 1 — Simulate it**
Use Euler's method (timestep `dt = 0.1` minutes) to simulate the coffee temperature
from `t = 0` to `t = 60` minutes. Print the temperature every 5 minutes.

**Task 2 — Find the answer**
At what time (in minutes) does the coffee reach 60°C?

**Task 3 — Plot it**
Plot temperature (y-axis) vs time (x-axis).
- Label both axes with units
- Add a horizontal dashed line at 60°C labelled "Drinking temperature"
- Mark the point where the curve crosses 60°C

---

## Starting Point

```python
T0 = 90        # initial temperature (°C)
T_room = 25    # room temperature (°C)
k = 0.05       # cooling constant
dt = 0.1       # time step (minutes)
t_end = 60     # simulate for 60 minutes
```

---

## What a Good Solution Looks Like

- Clean Euler loop
- A list/array storing `T` and `t` at each step
- The drinking-time printed clearly
- A well-labelled plot

---

## Bonus (if you finish fast)

What happens if you add milk immediately (drops temperature to 85°C instantly)?
Does that make the coffee reach drinking temperature *sooner or later* than waiting?
Simulate both cases on the same plot.
