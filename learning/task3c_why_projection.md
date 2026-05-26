# Task 3c — why we project onto directions

A plain-English companion to section 3c ("Computing the Eigenspectrum"). The whole part hinges
on one move: **projecting each measurement onto a direction and looking at the spread of the
results.** This note explains why that move is the heart of PCA.

## The objects in play

After cleaning and mean-centering, the data is the matrix $\widetilde{\mathbb{X}}$ of size
$\widetilde N \times M$ — one row $\vec{\tilde x}_i \in \mathbb{R}^M$ per sample (here $M = 3041$
frequencies). The **covariance matrix** is

$$
\mathbb{C} = \frac{1}{\widetilde N}\,\widetilde{\mathbb{X}}^\top\widetilde{\mathbb{X}}
\qquad (M \times M,\ \text{symmetric, PSD}).
$$

We never look at the 3041 raw numbers of a sample directly. Instead we ask a simpler question
over and over: *along this one direction, how much does the data vary?*

## What "projecting" actually means

Pick a direction — a unit vector $\vec w \in \mathbb{R}^M$. Projecting a measurement onto it is just
a dot product:

$$
z_i = \vec{\tilde x}_i \cdot \vec w.
$$

This collapses a 3041-dimensional point down to **one number**: its coordinate along $\vec w$.
Think of it as the shadow the data point casts on the $\vec w$-axis. Do this for all
$\widetilde N$ samples and you get a 1-D cloud of shadows $z_1, \dots, z_{\widetilde N}$.

## Why we care about the spread of those shadows

Because the data is mean-centered, the shadows average to zero, so their **variance** is

$$
\operatorname{Var}(z) = \frac{1}{\widetilde N}\sum_{i=1}^{\widetilde N} z_i^2 = \vec w^\top \mathbb{C}\, \vec w.
$$

This is the key identity. It says: *the variance of the data along direction $\vec w$ is exactly
$\vec w^\top\mathbb{C}\vec w$.* A direction with **large** variance is one along which samples spread out
and look different from each other — that is where the *information* lives. A direction with
**tiny** variance is one along which every sample looks the same — it tells you nothing about how
the samples differ. So projecting is how we *measure the usefulness of a direction*.

