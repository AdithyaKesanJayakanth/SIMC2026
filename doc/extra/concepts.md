# SIMCC 2026 — Concept Roadmap

A complete list of concepts needed for the challenge *"A Linear Algebra Guide to
the Strange Life of High-Dimensional Data"*, ordered from foundational to most
challenging. Each concept is tagged by where it is used (Q1 / Q2 / Q3).

---

## Tier 0 — Absolute foundations (everything builds on these)

- **Vectors** — a column of numbers; components, direction, and magnitude (norm) `‖v‖ = √(v·v)` *(Q1, Q2, Q3)*
- **Dot product / inner product** — `v·w`, and what it measures (similarity, projection) *(Q2, Q3)*
- **Matrices** — rectangular arrays; reading dimensions (N×M) *(all)*
- **Matrix–vector multiplication** — the `(a b; c d)(x;y)` rule *(Q1)*
- **Matrix–matrix multiplication** — `(AB)ᵢₖ = Σⱼ AᵢⱼBⱼₖ`; dimension compatibility (cols of A = rows of B) *(Q2, Q3)*
- **Transpose** — `(Aᵀ)ᵢⱼ = Aⱼᵢ`; how it flips dimensions *(Q2, Q3)*
- **Identity matrix** and **determinant** of a 2×2 (`ad − bc`) *(Q1)*
- **Linear combinations** — `c₁v₁ + c₂v₂` *(Q1)*

## Tier 1 — Eigentheory (the conceptual heart)

- **Eigenvectors & eigenvalues** — `Mv = λv`; "scaling without rotating" *(Q1, Q2, Q3)*
- **Characteristic equation** — solving `det(M − λI) = 0` *(Q1)*
- **Eigendecomposition / diagonalization** — expressing dynamics in the eigenbasis *(Q1, Q3)*
- **Orthonormal basis of eigenvectors** — `vᵢ·vⱼ = 0` for i≠j, `vᵢ·vᵢ = 1` *(Q2, Q3)*

## Tier 2 — Q1 specifics: Markov dynamics

- **Markov matrices & the Markov property** (state depends only on present) *(Q1)*
- **Conservation laws** (showing `p₁+p₂` is constant) *(Q1)*
- **Discrete-time evolution via eigenvectors** — `P(t) = c₁λ₁ᵗv₁ + c₂λ₂ᵗv₂` *(Q1)*
- **Long-time / asymptotic behavior** — dominant eigenvalue takes over (steady state) *(Q1)*
- **Time-varying parameters** — handling `ε(t) = ε₀e^(−t/t₀)`; products/sums of evolving matrices *(Q1g)*

## Tier 3 — Q2 specifics: iterative methods & SVD

- **The Power Method** — iterating `xₖ₊₁ = Xxₖ / ‖Xxₖ‖` to find the dominant eigenvector *(Q2)*
- **Proof of convergence** — expand `x₀` in the eigenbasis, show non-dominant terms decay *(Q2a)*
- **Convergence rate & the spectral gap** — residual shrinks by `|λ₂/λ₁|` per step *(Q2b)*
- **Failure when the spectral gap closes** (`|λ₁|=|λ₂|`) — non-convergence vs. mere slowness *(Q2c)*
- **Finite-precision / floating-point sensitivity** — rounding noise (~10⁻¹⁶) competing with signal *(Q2c)*
- **Symmetric matrices & the spectral theorem** — real eigenvalues, orthonormal eigenvectors *(Q2d)*
- **Positive semi-definite (PSD) matrices** — `wᵀAw ≥ 0` ⟹ non-negative eigenvalues *(Q2d)*
- **The two products `XᵀX` and `XXᵀ`** — building symmetric matrices from a rectangular one; proving they share nonzero eigenvalues *(Q2d, Q3)*
- **Singular values** `σᵢ = √λᵢ` *(Q2)*
- **Singular Value Decomposition (SVD)** — `X = UΣVᵀ`; left/right singular vectors *(Q2, Q3)*
- **Geometric picture of SVD** — rotate → stretch → rotate; unit sphere → ellipsoid *(Q2)*
- **Algorithm design / pseudocode** — writing language-agnostic Power-Method-for-SVD, choosing `XᵀX` vs `XXᵀ` by cost when N≪M *(Q2e)*

