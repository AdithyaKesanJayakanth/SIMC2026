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

## 🟥 Path C → understand **Q3** (cleaning, PCA & clustering of spectra)

*(assumes Paths A + B)*

**Phase 1 — probability → statistics bridge**
1. [[sample-spaces-events-axioms]]
2. [[random-variable]]
3. [[expectation]]
4. [[variance]]
5. [[mean-and-centering]]
6. [[covariance]]
7. [[covariance-matrix]]
8. [[diagonal-covariance-matrix]]

**Phase 2 — the spectral core (PCA)**
9. [[design-matrix]]
10. [[trace]]
11. [[trace-equals-sum-of-eigenvalues]] ← Q3(b): $\operatorname{tr}C\approx7.90$ as a check
12. [[eigenspectrum]]
13. [[eigenvectors-of-the-covariance-matrix]] ← keystone
14. [[principal-component-analysis]]
15. [[explained-variance-ratio]] ← why the "95% rule" is misleading
16. [[elbow-method]] ← $k^*=8$
17. [[participation-ratio]] ← **Q3(c)**: the *robust* intrinsic dimension $d_{\text{eff}}\approx8.7$
18. [[dimensionality-reduction]]

**Phase 3 — geometry, similarity, clustering**
19. [[vector-projection]]
20. [[cosine-similarity]] ← Q3(d): $v_1$ is a *contrast* direction (0.92 vs 0.67)
21. [[leader-clustering]] ← Q3(e): 25 clusters
22. [[gram-matrix]] ← Q3(f): the cheap route, same answer
23. [[eckart-young-theorem]] ← Q3(h)/§4: why keeping 8 components is *optimal*

**Phase 4 — why high dimensions are strange**
24. [[curse-of-dimensionality]]
25. [[surface-to-volume-ratio-high-dimensions]]
26. [[distance-concentration-high-dimensions]]
27. [[curse-of-sampling]]
28. [[manifold-hypothesis]]

**Phase 5 — uncertainty (the bootstrap)**
29. [[sampling-distribution-and-standard-error]]
30. [[bootstrap-resampling]] ← Q3(c): why the elbow is unstable but $d_{\text{eff}}$ holds
31. [[confidence-interval]] ← the $[7.6,10.0]$ interval

**Phase 6 — the chemistry payoff**
32. [[ir-spectroscopy]]
33. [[beer-lambert-law]]
34. [[pca-on-ir-spectra]] ← **the summit**

## ⭐ Beyond the report — the gap we should close

> [!warning] The one weakness our own ADVERSARY subagent flagged
> Q3(c) *asserts* a "multiplicative noise boundary" for the elbow but never derives a noise model. These two notes are the missing theory — be ready to defend this in the oral.
> 1. [[random-matrix-theory-intro]] — even pure noise has a predictable eigenvalue band
> 2. [[marchenko-pastur]] — the law that says exactly where the noise floor ends ($\lambda_\pm=\sigma^2(1\pm\sqrt\gamma)^2$)

## 🐍 Tooling track (read alongside anything)

[[python-for-java-devs]] · [[type-hints]] · [[numpy-basics]] · [[matplotlib-basics]] · [[histogram-bins]]

---

