# Task 3f — why eigenvector *components* are the sample coordinates

A plain-English companion to the Gram-space step. In 3e you got a sample's coordinates by
*projecting* it onto feature-space directions. In 3f the coordinates fall out **directly** as the
components of the eigenvectors — no projection step. This note explains why that is not a
coincidence but the whole point of the Gram matrix.

## The setup

The Gram matrix is built from sample-to-sample similarities:

$$
\mathbb{G} = \tfrac{1}{\widetilde N}\,\widetilde{\mathbb{X}}\,\widetilde{\mathbb{X}}^\top,
\qquad
G_{ij} = \tfrac{1}{\widetilde N}\,\langle \vec{\tilde x}_i,\ \vec{\tilde x}_j\rangle .
$$

It is $\widetilde N \times \widetilde N$: **one row and one column per sample**, not per feature. Entry
$G_{ij}$ is the dot-product similarity between vials $i$ and $j$.

## The key step: the eigen-decomposition *is* a coordinate factorisation

$\mathbb{G}$ is symmetric and positive semi-definite, so it decomposes into its eigenvectors $\vec u_k$
(with eigenvalues $\lambda_k \ge 0$):

$$
\mathbb{G} = \sum_k \lambda_k\, \vec u_k\,\vec u_k^\top
\qquad\Longrightarrow\qquad
G_{ij} = \sum_k \lambda_k\, (u_k)_i\,(u_k)_j .
$$

Now **define** a coordinate vector for sample $i$ by reading the $i$-th component out of each
eigenvector and scaling by $\sqrt{\lambda_k}$:

$$
\vec y_i = \Big(\sqrt{\lambda_1}\,(u_1)_i,\ \ \sqrt{\lambda_2}\,(u_2)_i,\ \ \dots\Big).
$$

Then the inner product of two of these coordinate vectors is

$$
\langle \vec y_i, \vec y_j\rangle
= \sum_k \big(\sqrt{\lambda_k}(u_k)_i\big)\big(\sqrt{\lambda_k}(u_k)_j\big)
= \sum_k \lambda_k (u_k)_i (u_k)_j
= G_{ij}
$$

**exactly.** So the $\vec y_i$ are genuine coordinates whose dot products reproduce the original
similarities. And by construction:

> **The $i$-th component of eigenvector $\vec u_k$ (scaled by $\sqrt{\lambda_k}$) is the $k$-th
> coordinate of sample $i$.**

That is the answer to "why are the components the coordinates." The decomposition
$\mathbb{G} = \sum_k \lambda_k \vec u_k\vec u_k^\top$ is literally a factorisation of *similarity* into
*coordinates × coordinates*; reading it back gives you the coordinates for free.

Two ways to read the eigenvectors:

| Read… | …and you get |
|---|---|
| **down** one eigenvector $\vec u_k$ (all $\widetilde N$ components) | coordinate $k$ of *every* sample |
| **across** eigenvectors at a fixed index $i$ | the full coordinate vector $\vec y_i$ of sample $i$ |

Each eigenvector has $\widetilde N$ entries — one per sample — so its components are *already indexed by
sample*. There is nothing left to project onto.

