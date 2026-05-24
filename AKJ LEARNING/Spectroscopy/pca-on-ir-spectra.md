---
tags:
  - simc
---

# PCA on IR Spectra

> [!abstract] In one line
> Stack your IR spectra into a matrix, run PCA, and the eigenvectors hand you back the chemical components hiding in the data — the number of large eigenvalues tells you how many components there are, the scores let you plot and cluster samples, and noise gets stripped away for free.

## The idea

You have, say, 50 IR spectra. Each one is a point in a 1000-dimensional space. That sounds hopeless to visualize or reason about. But here is the key: the [[beer-lambert-law]] says that if your samples are all mixtures of $k$ pure chemicals, every spectrum is a linear combination of those $k$ pure-component spectra. So all 50 points lie on (or near) a flat $k$-dimensional subspace inside that 1000-dimensional room — exactly what the [[manifold-hypothesis]] describes.

PCA is the algorithm that finds that subspace. It does not know anything about chemistry; it just finds the directions of maximum variance. But because the data has a linear chemical structure, those directions *are* the chemical directions. The math and the chemistry align perfectly.

## The math / mechanism

### Step 1 — Build the design matrix

Stack your $n$ spectra row-by-row:

$$\mathbf{X} \in \mathbb{R}^{n \times p}, \quad X_{ij} = \text{absorbance of sample } i \text{ at wavenumber } j$$

See [[design-matrix]].

### Step 2 — Center (and optionally scale)

Subtract the column mean from every column:

$$\tilde{\mathbf{X}} = \mathbf{X} - \mathbf{1}\bar{\mathbf{x}}^\top$$

where $\bar{\mathbf{x}} \in \mathbb{R}^p$ is the mean spectrum. See [[mean-and-centering]]. This removes the constant baseline offset common to all spectra.

### Step 3 — Build the covariance matrix

$$\mathbf{C} = \frac{1}{n-1} \tilde{\mathbf{X}}^\top \tilde{\mathbf{X}} \in \mathbb{R}^{p \times p}$$

$C_{ij}$ captures how much wavenumber $i$ and wavenumber $j$ co-vary across your samples. See [[covariance-matrix]].

### Step 4 — Eigendecomposition

Find the eigenvectors and eigenvalues of $\mathbf{C}$:

$$\mathbf{C} \mathbf{v}_r = \lambda_r \mathbf{v}_r$$

Sort by $\lambda_1 \geq \lambda_2 \geq \cdots \geq \lambda_p \geq 0$.

Each eigenvector $\mathbf{v}_r \in \mathbb{R}^p$ is a **loading vector** — a direction in wavenumber space. Each eigenvalue $\lambda_r$ tells you how much variance lies along that direction.

See [[eigenvectors-of-the-covariance-matrix]] and [[power-method]] for how these are computed.

### Step 5 — Read the eigenspectrum

Plot $\lambda_r$ versus $r$ (the scree plot). You will typically see:

$$\underbrace{\lambda_1, \lambda_2, \ldots, \lambda_k}_{\text{large}} \gg \underbrace{\lambda_{k+1}, \lambda_{k+2}, \ldots}_{\text{small, flat}}$$

The sharp drop — the "elbow" — marks $k$, the number of chemically distinct components. This works because Beer–Lambert confines the signal to a $k$-dimensional subspace; everything beyond that is noise. See [[eigenspectrum]].

> [!note] Why the scree plot works here (not just heuristics)
> In generic PCA, picking $k$ from a scree plot is a rule of thumb. For IR spectra governed by Beer–Lambert, it has a rigorous chemical interpretation: $k$ = number of pure components. The elbow is real structure, not noise.

### Step 6 — Project to get scores

For each spectrum $\tilde{\mathbf{x}}_i$, compute its **score** on PC $r$:

$$t_{ir} = \tilde{\mathbf{x}}_i \cdot \mathbf{v}_r$$

Stack the first $k$ scores for sample $i$ into a vector $\mathbf{t}_i \in \mathbb{R}^k$. This is [[dimensionality-reduction]]: you have gone from 1000 numbers per spectrum to $k$ numbers.

Plot $t_{i1}$ vs $t_{i2}$ (scores scatter plot). Chemically similar samples cluster together.

### Step 7 — Interpret the loadings

Each loading vector $\mathbf{v}_r \in \mathbb{R}^p$ has the same axis as a spectrum (wavenumber). Large positive or negative entries at a wavenumber mean that wavenumber is important for PC $r$. In favorable cases $\mathbf{v}_r$ looks like a recognizable functional-group absorption peak.

> [!warning] Common confusion
> Loadings are NOT pure-component spectra (except in the ideal noiseless case). They are the mathematical PCA axes, which are a rotation of the chemical axes. If you need actual pure-component spectra, use MCR-ALS (a follow-on method). For SIMC purposes, "loadings point to which wavenumbers matter" is enough.

