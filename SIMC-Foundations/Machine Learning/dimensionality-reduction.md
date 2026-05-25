---
tags:
  - simc
---

# Dimensionality reduction

> [!abstract] In one line
> The actual payoff move — replace each sample's 1000 original numbers with just $k$ numbers (its coordinates along the top $k$ principal components), keeping the signal and discarding the noise directions.

## The idea

You've done all the work: centered the data, built the covariance matrix, found the eigenvectors, read the eigenspectrum, decided you need $k = 3$ components. Now what?

You take every spectrum (a vector of 1000 numbers) and re-express it in the new coordinate system defined by the top 3 PCs. Instead of saying "this spectrum has intensity 0.42 at wavelength 847 nm, 0.39 at 848 nm, ..., (997 more numbers)", you now say "this spectrum is at position $(z_1, z_2, z_3) = (2.1, -0.4, 0.9)$ in PC space."

That triple of numbers — the **scores** — is the complete, compressed description of the spectrum. And crucially: the directions you threw away (PCs 4 through 1000) were almost all noise. So you haven't just compressed — you've **denoised**.

Think of it like shadows: a 3D object casts a 2D shadow. If you choose the right light direction, the shadow captures the object's shape almost perfectly. PCA finds that optimal light direction.

