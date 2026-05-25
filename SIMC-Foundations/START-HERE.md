---
tags:
  - simc
---

# START HERE — SIMC Foundations

> [!abstract] What this is
> A self-contained study pack that takes you from the **basics of linear algebra, statistics, and probability** all the way to **completely understanding our SIMC 2026 report** — *"A Linear-Algebra Guide to the Strange Life of High-Dimensional Data"* (Q1 Markov populations, Q2 power method + SVD, Q3 PCA on IR spectra). 75 atomic notes. Open this folder as an Obsidian vault.

> [!tip] How to read it (the whole point)
> Every note ends with **Builds on** (its prerequisites, ↑) and **Leads to** (what it unlocks, ↓).
> **Pick any topic.** If you don't get it → follow **Builds on** down until you hit something you *do* know, then climb back up. If you've got it → follow **Leads to** to see where it's used. The three reading paths below are just the recommended climbs — each ends at the exact part of our report it explains.

> [!info] For the team
> Adithya Kesan Jayakanth · K Vishnu Kumar · Adithya Anand. Drag this whole folder into Obsidian (or read the `.md` files in anything). Notes you already saw in the vault are copied in; the new ones fill every gap between "basics" and "our report."

---

## 🟦 Path A → understand **Q1** (Markov matrices & the fate of a population)

**Phase 1 — the alphabet**
1. [[vector]]
2. [[what-is-a-dimension]]
3. [[matrix]]
4. [[matrix-vector-multiplication]]
5. [[dot-product]]
6. [[vector-norm-and-distance]]

**Phase 2 — the eigen-engine**
7. [[determinant-and-characteristic-equation]]
8. [[eigenvectors-and-eigenvalues]]
9. [[triangular-matrix-eigenvalues]] ← how Q1(b) reads off $\lambda=1,\,1-\varepsilon$ in one line
10. [[orthonormal-basis]]
11. [[eigenbasis-and-change-of-basis]] ← Q1(c): writing $P(0)=c_1v_1+c_2v_2$
12. [[diagonalization]]
13. [[matrix-powers-via-eigendecomposition]] ← Q1(d): turns $M^t$ into scalar powers

**Phase 3 — the dynamics**
14. [[markov-matrix]]
15. [[column-stochastic-matrix]] ← Q1(a) conservation in one line ($\mathbf 1^\top M=\mathbf 1^\top$)
16. [[absorbing-state]] ← type-2, the $\lambda=1$ trap
17. [[geometric-decay]]
18. [[steady-state-and-long-run-behavior]] ← Q1(e): all mass becomes type-2
19. [[infinite-products-and-convergence]] ← **Q1(g)**, the hardest part: product, not power; residue freezes

## 🟧 Path B → understand **Q2** (the power method & the SVD)

*(assumes Path A's eigen-engine)*
1. [[symmetric-matrix]]
2. [[positive-semi-definite]] ← Q2(d): $w^\top X^\top X w=\lVert Xw\rVert^2\ge0$
3. [[power-method]]
4. [[rayleigh-quotient]]
5. [[spectral-gap]] ← Q2(b): convergence at rate $|\lambda_2/\lambda_1|$
6. [[convergence-rate-power-method]]
7. [[degenerate-eigenvalues]] ← Q2(c): when the gap closes, it breaks
8. [[transpose]]
9. [[xtx-xxt-duality]] ← **Q2(d)**: the keystone — $X^\top X$ and $XX^\top$ share eigenvalues
10. [[singular-values]]
11. [[svd]]
12. [[frobenius-norm]]
13. [[floating-point-precision]] ← why "agree to $10^{-16}$" is the gold standard

