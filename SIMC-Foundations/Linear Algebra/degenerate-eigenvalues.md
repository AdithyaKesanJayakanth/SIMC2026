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

## The math

Conceptual anchor: degeneracy closes the spectral gap to zero, making the convergence ratio $r = |\lambda_2/\lambda_1|$ equal to 1 and the geometric decay stop entirely.

The canonical failure case from Q2(c):

$$
X = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}, \quad \lambda_1 = 1,\; \lambda_2 = -1, \quad |\lambda_1| = |\lambda_2| = 1
$$

Start with $x_0 = (1, 1)^\top / \sqrt{2}$. Then:

$$
X x_0 = (1, -1)^\top/\sqrt{2}, \quad X^2 x_0 = (1, 1)^\top/\sqrt{2} = x_0
$$

The iterate returns to its starting point after 2 steps — an infinite cycle with no convergence.

Near-degenerate case: when $|\lambda_2/\lambda_1| = 1 - \delta$ for tiny $\delta$, the iteration count is $\sim 1/\delta$, which diverges as $\delta \to 0$.

> [!example] Tiny concrete example
> $X = \operatorname{diag}(1, -1)$, $x_0 = (1, 1)/\sqrt{2}$.
>
> Step 1: $Xx_0 = (1, -1)/\sqrt{2}$ → normalise → $(1, -1)/\sqrt{2}$
>
> Step 2: $X \cdot (1,-1)/\sqrt{2} = (1, 1)/\sqrt{2}$ → back to $x_0$.
>
> Oscillates forever between $(1,1)/\sqrt{2}$ and $(1,-1)/\sqrt{2}$. No convergence.

> [!warning] Common confusion
> Having repeated eigenvalues (e.g. $\lambda_1 = \lambda_2 = 5$) is a *different* kind of degeneracy — here any direction in the eigenspace is a valid answer, so the power method converges just fine (it finds *a* top eigenvector, just not a unique one). The destructive case is equal *magnitudes but different signs* (or complex eigenvalues in general), which creates oscillation.

## Why this matters for the report

**Q2(c):** The report uses $X = \operatorname{diag}(1, -1)$ as the explicit structural failure example. The iterate oscillates forever — this is not a numerical quirk but an algebraic inevitability. The report then extends this to the near-degenerate case: when floating-point noise ($\sim 10^{-16}$) is comparable to the eigenvalue separation, the computer cannot determine which eigenvalue is larger, so the ordering becomes ambiguous and the method's output is unreliable.

## Builds on
- [[spectral-gap]]
- [[power-method]]

## Leads to
- [[floating-point-precision]]
