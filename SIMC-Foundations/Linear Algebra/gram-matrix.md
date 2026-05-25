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

