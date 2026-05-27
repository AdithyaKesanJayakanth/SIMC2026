# SIMC 2026 — High-D / PCA / IR Cheat Sheet

Keep this open during the challenge. Everything you should not have to re-derive.

---

## 0. Conventions

- `X` is shape `(M, N)`: **M samples (rows)** × **N features (columns)**. Sklearn convention.
- "Centered" = column-mean subtracted.
- λ = eigenvalue, V = matrix of eigenvectors (as columns), Σ = covariance matrix.

---

## 1. Variance, covariance, correlation

For samples `x_1,…,x_M`:

```
mean       x̄ = (1/M) Σ x_i
variance   Var(x) = (1/(M-1)) Σ (x_i − x̄)²          ← Bessel: divide by M-1
std dev    s = √Var
covariance Cov(x, y) = (1/(M-1)) Σ (x_i − x̄)(y_i − ȳ)
correl.    ρ(x, y) = Cov(x, y) / (s_x · s_y)         ← ∈ [−1, 1]
z-score    z_i = (x_i − x̄) / s
```

---

## 2. Covariance matrix

For **centered** `X_c`:

```
C = (1 / (M − 1)) · X_cᵀ X_c         shape (N, N), symmetric, PSD
```

- `C[i,i]` = Var(feature i).
- `C[i,j]` = Cov(feature i, feature j).
- **Diagonal C** ⇔ features are linearly uncorrelated. PCA's goal: find a basis where C becomes diagonal.
- `trace(C) = Σ C[i,i] = Σ λ_k` = total variance, **invariant under rotation**.

---

## 3. Worked numeric example (memorize the mechanics)

Centered data, M=4, N=2:

```
X_c = [[ 2,  2],
       [-2, -2],
       [ 1, -1],
       [-1,  1]]
```

Column means are zero (verify). Compute `X_cᵀ X_c`:

```
[[2·2+(-2)·(-2)+1·1+(-1)·(-1),    2·2+(-2)·(-2)+1·(-1)+(-1)·1],
 [...same by symmetry...,           2·2+(-2)·(-2)+(-1)·(-1)+1·1]]
= [[10, 6],
   [ 6,10]]
```

Divide by M−1 = 3:

```
C = (1/3) · [[10, 6],
              [ 6,10]]
trace(C) = 20/3 ≈ 6.667
det(C)   = (100 − 36)/9 = 64/9
```

Characteristic equation: `λ² − trace·λ + det = 0`:

```
λ² − (20/3)λ + 64/9 = 0
Δ = (20/3)² − 4·(64/9) = 400/9 − 256/9 = 144/9
√Δ = 12/3 = 4
λ₁ = (20/3 + 4)/2 = 32/6 = 16/3 ≈ 5.333
λ₂ = (20/3 − 4)/2 =  8/6 =  4/3 ≈ 1.333
```

Eigenvectors: for `[[a,b],[b,a]]` they are `(1, 1)/√2` and `(1, −1)/√2`. Sanity-check: `[[10,6],[6,10]] @ [1,1] = [16,16] = 16·[1,1]` ✓.

Explained variance ratios:

```
evr₁ = (16/3) / (20/3) = 0.80
evr₂ = ( 4/3) / (20/3) = 0.20
```

So PC1 captures 80% of variance, PC2 captures 20%. PC1 lies along `(1,1)/√2` — the diagonal — which is exactly where the spread is largest. **This is what an eigenspectrum reading looks like in 2-D.**

---

