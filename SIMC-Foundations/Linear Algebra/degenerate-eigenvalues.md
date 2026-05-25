---
tags:
  - simc
---

# Degenerate eigenvalues

> [!abstract] In one line
> Eigenvalues are degenerate when two or more share the same (or nearly the same) magnitude, causing the power method to fail because there is no single dominant direction to lock onto.

## The idea

The power method works by amplifying the dominant eigenvector more than all the others, every step. If two eigenvalues are tied — say $|\lambda_1| = |\lambda_2|$ — neither ever "wins". The iteration oscillates forever between the two competing directions, or spirals endlessly, depending on their signs.

Think of two equally matched tug-of-war teams: the rope never moves decisively either way. The power method needs one team to be strictly stronger.

Near-degeneracy is almost as bad: the rope inches slowly toward one side, but you need thousands of pulls before it moves far enough to declare a winner. At some point, the separation falls below floating-point precision and the computer can no longer tell which side is winning.

