---
tags:
  - simc
---

# Gram matrix

> [!abstract] In one line
> The Gram matrix $G = \frac{1}{N}\tilde X \tilde X^\top$ is the sample-space analogue of the covariance matrix — entry $(i,j)$ is the inner product (similarity) between samples $i$ and $j$.

## The idea

The covariance matrix tells you how features relate to each other (feature × feature). The Gram matrix flips the perspective: it tells you how *samples* relate to each other (sample × sample). Entry $G_{ij}$ measures how similar spectrum $i$ is to spectrum $j$ as an inner product.

When you have far fewer samples than features ($N \ll M$), the Gram matrix is the smaller object. Diagonalising it is cheaper, and by the $X^\top X / XX^\top$ duality, you get the same eigenvalues (and thus the same PCA directions) as if you'd diagonalised the giant covariance matrix.

```python
N_tilde = X_tilde.shape[0]
G = (X_tilde @ X_tilde.T) / N_tilde   # shape (N_tilde, N_tilde)
eigvals, eigvecs = np.linalg.eigh(G)
```

## The math

Conceptual anchor: $G_{ij} = \frac{1}{N}\tilde x_i \cdot \tilde x_j$ — it's a dot-product table of all pairs of mean-centred spectra.

$$
G = \frac{1}{N} \tilde X \tilde X^\top \in \mathbb R^{\tilde N \times \tilde N}
$$

Covariance (feature space): $C = \frac{1}{N}\tilde X^\top \tilde X \in \mathbb R^{M \times M}$

By $X^\top X / XX^\top$ duality: $G$ and $C$ share non-zero eigenvalues.

Cost comparison (diagonalisation):

$$
\text{Gram cost} \sim \tilde N^3, \quad \text{Covariance cost} \sim M^3, \quad \text{speedup} \approx \left(\frac{M}{\tilde N}\right)^2 = \left(\frac{3401}{924}\right)^2 \approx 13.5\times
$$

- $\tilde X \in \mathbb R^{\tilde N \times M}$ — mean-centred data, cleaned samples only
- $\tilde N$ — number of kept samples (924 in Q3)
- $M$ — number of features/channels (3401 in Q3)
- $G_{ij}$ — normalised inner product between sample $i$ and sample $j$

> [!example] Tiny concrete example
> Two spectra: $\tilde x_1 = (1, 0, -1)$, $\tilde x_2 = (0, 2, 0)$.
>
> $G = \frac{1}{2}\begin{pmatrix}1&0&-1\\0&2&0\end{pmatrix}\begin{pmatrix}1&0\\0&2\\-1&0\end{pmatrix} = \frac{1}{2}\begin{pmatrix}2&0\\0&4\end{pmatrix} = \begin{pmatrix}1&0\\0&2\end{pmatrix}$
>
> $G_{12} = 0$: the two spectra are orthogonal — completely different shapes.

> [!warning] Common confusion
> The Gram matrix eigenvectors are in *sample space* ($\tilde N$-dimensional), not feature space ($M$-dimensional). You cannot directly interpret them as spectral loadings. To recover the feature-space PCA directions $v_i$, you must apply one more matrix multiplication: $v_i \propto \tilde X^\top u_i$ where $u_i$ is a Gram eigenvector.

## Why this matters for the report

**Q3(f):** The report explicitly replaces the $3401 \times 3401$ covariance matrix with the $924 \times 924$ Gram matrix $G = \frac{1}{N}\tilde X\tilde X^\top$. The $\sim13.5\times$ speedup is computed as $(3401/924)^2$. The top-8 eigenvalues agree to $10^{-6}$ with those from the covariance approach — confirmed numerically. Crucially, the same 25 clusters emerge from both, validating that the duality holds not just in theory but in practice on this dataset.

## Builds on
- [[xtx-xxt-duality]]
- [[transpose]]
- [[symmetric-matrix]]

## Leads to
- [[pca-on-ir-spectra]]
