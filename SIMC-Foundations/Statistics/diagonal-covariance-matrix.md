---
tags:
  - simc
---

# Diagonal covariance matrix

> [!abstract] In one line
> A diagonal covariance matrix means every feature is uncorrelated with every other — and rotating to principal component axes is exactly the operation that turns the covariance matrix diagonal.

## The idea

Start with the [[covariance-matrix]] in the original feature space. It has lots of off-diagonal entries — those non-zero covariances represent redundant information (features moving together).

Now imagine rotating your entire data cloud to a new set of axes. You want to find the *special* rotation where, in the new coordinate system, no feature correlates with any other. In that system the covariance matrix would look like this:

$$\begin{pmatrix} \lambda_1 & 0 & 0 & \cdots \\ 0 & \lambda_2 & 0 & \cdots \\ 0 & 0 & \lambda_3 & \cdots \\ \vdots & & & \ddots \end{pmatrix}$$

All off-diagonals are zero. Every new axis varies independently. The diagonal entries $\lambda_1, \lambda_2, \ldots$ are just the variances along each new axis.

**This is PCA's whole trick:** find the rotation that diagonalizes $C$. The new axes are the **principal components**; the diagonal entries of the diagonalized matrix are the **eigenvalues** of $C$, each equal to the variance captured by its principal component. The rotation itself is encoded in the **eigenvectors** of $C$ (see [[eigenvectors-of-the-covariance-matrix]]).

