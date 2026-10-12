# SIMC 2026 — Endeavour Challenge

Working repository for the **Singapore International Mathematical and Computational Challenge (SIMC 2.0) 2026**, Endeavour
problem. Team: **K. Vishnu Kumar · Adithya Kesan Jayakanth · Adithya Anand**.

The challenge has three linked questions. One idea runs through all of them: a
high-dimensional system is governed by a small number of special directions.

| | Question | What it asks | Approach |
|---|---|---|---|
| **Q1** | Linear algebra of Markov matrices | Two interconverting populations: conservation, eigenspectrum, long-run behaviour, and what changes when the conversion rate decays over time | Eigen-decomposition by hand, then numerical validation of every closed form |
| **Q2** | The power method and the SVD | Why the power method converges, how fast, when it fails, and how to get an SVD out of it | Analytical proofs plus a worked 3 × 2 example |
| **Q3** | Design, covariance and Gram matrices | A 1,000 × 3,401 table of infrared spectra with planted errors. Clean it, then work out how many distinct samples there are | Cleaning, PCA, and clustering in two equivalent spaces |

---

## Results

### Q1: Markov matrices
- The matrix is column-stochastic, so the total population is conserved at every step.
- The eigenpairs are λ₁ = 1 with v₁ = (0, 1) (persistent) and λ₂ = 1 − ε with v₂ = (1, −1) (decaying). The population converges to the steady state (0, 1).
- With a decaying rate ε(t) = ε₀e^(−t/t₀), the decaying mode picks up one factor (1 − ε(s)) per step. That gives a cumulative product, not the power (1 − ε(t))ᵗ that our first notes had. The product converges to a positive limit, so type 1 is *not* fully depleted and freezes at a positive residue.
- Both closed forms match brute-force iteration to better than 10⁻¹⁰. The check is asserted in the notebook, so a wrong formula fails loudly.

### Q2: The power method and the SVD
- Proofs of convergence and of the rate |λ₂/λ₁|ᵏ set by the spectral gap.
- What happens when the gap closes, and the floating-point risks when |λ₂/λ₁| ≈ 1.
- XᵀX and XXᵀ are positive semi-definite and share their non-zero eigenvalues. To get the SVD cheaply, run the power method on the smaller of the two.

### Q3: How many drinks are in the table?

| Step | Result |
|---|---|
| (a) Cleaning | 40 empty vials (bimodal row-norm gap; the cut works for any threshold in [2, 4]) and 36 high-norm vials, leaving 924 |
| (b) Variance | Total variance tr(C) ≈ 7.90, concentrated in a few molecular bands |
| (c) PCA | λ₁/λ₂ ≈ 3.53; the elbow is at k = 8, an **eight-dimensional signal inside 3,401 dimensions** |
| (d) Leading eigenvector | A chemical contrast: close to a centred measurement (cos ≈ 0.92) and nothing like the mean spectrum (cos ≈ 0.03) |
| (e)/(f) Clustering | 25 clusters in covariance space and 25 in Gram space |
| (g) Comparison | The two clusterings match exactly (\|corr\| = 1 for matched clusters, 0 otherwise), as the SVD duality says they must |
| (h) Unique samples | **25**: PCA narrowed about 1,000 samples in 3,401 dimensions to 25, about 37 repeat measurements each (24 × 37 + 36 = 924) |

Our submitted answer: about 25 unique samples. After the 40 empty and 36 corrupted vials are
removed, the 924 genuine spectra form 25 tight clusters of about 37 replicate vials each. The
count is stable across a factor-of-two range of clustering radii, and the covariance and Gram
routes both return 25.

---

## Repository layout

```
Challenge_Question/          official problem statement + mystery_matrix1.npy
data/
  input/                     inputs used by the notebook
  output/                    every generated figure (Task 1 trajectories, TASK 3/ q3a–q3h)
src/main.ipynb               the full computational pipeline, Task 1 → Task 3, top to bottom
doc/
  FINAL/                     submitted report, proofs & derivations, AI usage log, figures
  FINAL/REPORT/              preliminary Q1–Q3 report (LaTeX) + changelog of every correction
  Q3_full_report.tex/.pdf    long-form Q3 write-up, built up from first principles
  extra/                     cheat sheet, concept roadmap, plain-language explainer, examiner Q&A prep
Final report & derivations/  the submission package
Presentation & defense deck/ cinematic HTML deck, PDF exports, Q3 slides
notes/                       scanned handwritten working (26 May)
learning/, learning vk/      per-task study guides (Task 1 guide, 2e, 3c, 3f, 3g/h)
AKJ LEARNING/, SIMC-Foundations/   concept notes: linear algebra, statistics, probability, ML, spectroscopy
practice/                    warm-up PCA experiments on toy and synthetic IR data
snippets/                    reusable loading / stats / ML / plotting helpers
templates/                   LaTeX templates for the preliminary and 10-page submission
SIMC/                        earlier training material: 2024 Endeavour past paper and practice projects
```

## Running it

```bash
pip install numpy matplotlib jupyter
jupyter notebook src/main.ipynb
```

Run the cells in order. Task 1 needs no data. Task 3 finds the repository root by itself, reads
`data/input/mystery_matrix1.npy`, and writes its figures to `data/output/TASK 3/`. Task 2 is
analytical only, so its solutions are in the reports and there is no code for it.

To rebuild the reports, compile `doc/FINAL/REPORT/SIMC2026_Preliminary_Q1_Q2_Q3.tex` and
`doc/Q3_full_report.tex` with `pdflatex`. The figures they include are in `doc/FINAL/figs/` and
`data/output/TASK 3/`.

## How the reports were checked

`doc/FINAL/REPORT/changelog.md` records every place the typed report departs from the
handwritten notes. It tags each item as a **mistake corrected**, a **part missed**, or
**content added** beyond the notes, and the same tags appear in colour in the PDF. AI
assistance is declared in `doc/FINAL/SIMC2026_AI_Usage_Log.pdf`, and the notebook's
docstrings carry their own notice.
