---
tags:
  - simc
---

# Absorbing state

> [!abstract] In one line
> An absorbing state is one you can enter but never leave — once the system reaches it, it stays there forever.

## The idea

Picture a roach motel: things check in but they don't check out. In Q1, type-2 is the roach motel. Every time step, some type-1 converts to type-2, but type-2 never converts back. Eventually everything ends up type-2.

The formal signature: the column of $M$ that corresponds to the absorbing state has a 1 on the diagonal and 0s everywhere else — it maps the state to itself with probability 1.

