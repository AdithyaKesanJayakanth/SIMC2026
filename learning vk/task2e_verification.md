# Task 2e — understanding the numerical verification

A plain-English companion to the hand calculation in `task1_guide.tex` (section 2e),
focused on the vector $\tfrac{1}{\sqrt2}(1,1)$ and why the two verification lines work.

## The setup

We apply the Power-Method / SVD recipe by hand to the rectangular matrix

$$
\mathbb{X} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \\ 1 & 1 \end{pmatrix}
\qquad (N=3 \text{ rows},\ M=2 \text{ columns}).
$$

Because $M=2 < N=3$, we iterate on the smaller symmetric matrix $\mathbb{X}^\top\mathbb{X}$:

$$
\mathbb{X}^\top\mathbb{X} = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix},
\qquad \text{eigenvalues } \{3,\,1\},
\qquad \sigma_1 = \sqrt{3}.
$$

The three numbers we extract:

| Quantity | Value | What it is |
|---|---|---|
| $\sigma_1$ | $\sqrt{3}$ | largest singular value (the stretch factor) |
| $\vec v_1$ | $\tfrac{1}{\sqrt2}(1,1)$ | unit **right** singular vector (input direction) |
| $\vec u_1$ | $\tfrac{1}{\sqrt6}(1,1,2)$ | unit **left** singular vector (output direction) |

## Where $\tfrac{1}{\sqrt2}(1,1)$ comes from

Solving $(\mathbb{X}^\top\mathbb{X} - 3I)\vec v = \vec 0$ only gives a **direction**: "equal parts
of both components," i.e. the arrow pointing diagonally along $(1,1)$.

A singular vector must have length exactly 1 (that's the convention — singular vectors are
pure direction-markers with no size). The arrow $(1,1)$ is too long: by Pythagoras its length
is $\sqrt{1^2+1^2} = \sqrt2$. So we shrink it by dividing by $\sqrt2$:

$$
\vec v_1 = \frac{1}{\sqrt2}\begin{pmatrix}1\\1\end{pmatrix},
\qquad \lVert\vec v_1\rVert^2 = \tfrac12(1+1) = 1. \ \checkmark
$$

**The $\tfrac{1}{\sqrt2}$ is just a shrink factor that makes the arrow the right size — nothing more.**

