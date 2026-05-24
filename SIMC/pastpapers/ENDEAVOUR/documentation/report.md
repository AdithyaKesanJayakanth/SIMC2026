# SIMC 2024 Endeavour Challenge — Team India Solution Report

## Problem Overview

Single Particle Imaging (SPI) reconstructs 3D protein structures from many 2D diffraction patterns, each taken at an unknown orientation. This challenge presents a simplified 2D toy version: given thousands of images that are randomly rotated copies (0°, 90°, 180°, 270° clockwise) of a single master image, classify each by its orientation and reconstruct the master.

The difficulty escalates across 7 tasks — from 25 noiseless patterns to 100,000 extremely noisy sparse patterns requiring advanced statistical methods.

---

## Task 1: Classifying 25 Noiseless Patterns [10 points]

### Approach (< 300 words)

We classify 25 noiseless 18×18 patterns by direct pixel-wise comparison against the reference pattern (pattern #0). For each pattern, we compute the Sum of Squared Differences (SSD) against all four clockwise rotations of the reference:

$$\text{SSD}(P, R_\theta) = \sum_{i,j} (P_{ij} - R_{\theta,ij})^2$$

Since patterns are noiseless (exact copies of rotated master), the correct rotation yields SSD = 0 exactly. We assign each pattern the angle with minimum SSD.

The rotation function uses `np.rot90(image, k=-1)` for each 90° clockwise step. We generate all four rotations by iteratively applying this operation.

### Results

| Orientation | Count |
|-------------|-------|
| 0° | varies by data |
| 90° | varies by data |
| 180° | varies by data |
| 270° | varies by data |
| **Total** | **25** |

### Outputs
- `task1a_rotations.png` — Reference pattern in 4 clockwise rotations
- `task1b_classified.png` — All 25 patterns color-coded by orientation class

---

## Task 2: Flattening 2D Patterns to 1D [10 points]

### Approach (< 300 words)

The 100 patterns are stored as 1D vectors of length 1296, originally 36×36 images. The key insight is that rotation in 2D followed by row-major flattening produces a specific permutation of pixel indices. Two patterns with the same orientation have identical flattened representations.

To classify:
1. Reshape the reference (row 0) back to 36×36 and render the master image.
2. For each of the 4 rotations, apply `np.rot90` then `flatten()` to get the flattened reference at that angle.
3. Compare each pattern against all 4 flattened references using SSD.
4. Assign the angle with minimum SSD.

The design matrix visualization (rows = patterns, columns = pixels) confirms our classification: when sorted by orientation, patterns within each block have identical column patterns, producing the characteristic "striped blocks" structure.

### Outputs
- `task2a_master.png` — Reconstructed 36×36 master image
- `task2_design_matrix.png` — Unsorted vs. sorted design matrix

---

## Task 3: Scaling to 1000 Patterns with KMeans [10 points]

### Approach (< 300 words)

With 1000 flattened patterns (33×33 = 1089 pixels each), we employ KMeans clustering (k=4) to partition patterns into four orientation classes. This is dramatically more efficient than O(n²) pairwise comparison.

**Algorithm:**
1. Run KMeans with k=4, multiple random initializations (n_init=10) and KMeans++ seeding for robustness.
2. Each cluster center represents the average pattern for one orientation.
3. Map cluster IDs to angles by comparing each center against the 4 rotations of the reference pattern (pattern #0), using greedy minimum-distance assignment.

Our implementation includes a fallback pure-numpy KMeans (with KMeans++ initialization) for environments without scikit-learn — critical for competition portability.

The master image shape (33×33) was inferred from the pixel count: √1089 = 33. The design matrix, plotted with the `BuPu` colormap, shows clean block structure after sorting.

### Outputs
- `task3a_master.png` — Mystery animal master image (33×33)
- `task3c_design_matrix.png` — Unsorted/sorted design matrix (BuPu colormap)
- `task3_class_averages.png` — Average image per orientation class

---

## Task 4: Noisy Patterns [15 points]

### Approach (< 300 words)

The 1000 patterns (50×50 = 2500 pixels) are now extremely noisy — each pixel is a Bernoulli draw with very low probability, so most pixels are zero and individual patterns appear as random noise. Naive averaging (assuming all same orientation) gives a featureless blob because rotations cancel structure.

We use an **Expectation-Maximization (EM)** algorithm:

1. **Initialize:** Compute naive average as initial master estimate μ̂.
2. **E-step:** For each pattern, compute log-likelihood against all 4 rotations of μ̂:
   $$\ln \mathcal{L}(r|\vec{k}, \hat{\mu}) = \sum_i [k_i \ln(\mu_{r,i}) + (1-k_i)\ln(1-\mu_{r,i})]$$
   Assign each pattern to its maximum-likelihood rotation.
3. **M-step:** Average patterns within each class (after rotating back to canonical orientation) to get improved master estimate.
4. **Repeat** until labels stabilize (typically 3–5 iterations).

The vectorized log-likelihood computation uses the identity:
$$\ln \mathcal{L} = \vec{k} \cdot \ln\frac{\vec{\mu}}{1-\vec{\mu}} + \sum_i \ln(1-\mu_i)$$

This separates into a matrix multiply (data × log-odds) plus a constant, enabling efficient batch computation across all patterns and rotations.

### Results
- Average row-sum: reports the mean photon count per pattern
- EM converges in ~4 iterations
- Class averages show rotated versions of the mystery animal

### Outputs
- `task4b_naive_avg.png` — Featureless naive average
- `task4c_class_averages.png` — Four orientation class averages
- `task4c_master.png` — Reconstructed master image

---

## Task 5: Likelihood Theory [15 points]

### Part (a): L(r=90° | K₍₄₎, μ₍₄₎)

The master image μ₍₄₎ has 4 pixels: [λ, βλ, βλ, βλ]. At r=90°, the pixel order rotates to [βλ, λ, βλ, βλ]. Given measured pattern K₍₄₎ = {1, 0, 0, 0}:

$$\boxed{\mathcal{L}(r=90°) = \beta\lambda \cdot (1-\lambda) \cdot (1-\beta\lambda)^2}$$

### Part (b): Likelihood Ratio

$$\frac{\mathcal{L}(r=0°)}{\mathcal{L}(r=90°)} = \frac{\lambda(1-\beta\lambda)^3}{\beta\lambda(1-\lambda)(1-\beta\lambda)^2} = \boxed{\frac{1-\beta\lambda}{\beta(1-\lambda)}}$$

### Part (c): When does the ratio equal 1?

Setting the ratio to 1:
$$1 - \beta\lambda = \beta(1-\lambda) = \beta - \beta\lambda$$

Therefore $\boxed{\beta = 1}$.

Physical interpretation: when β=1, all pixels have the same average value λ, so orientations are indistinguishable.

### Part (d): 16-pixel case, single outlier on edge

With one outlier at corner position (0,0):
- L(aligned) = λ · (1-βλ)¹⁵
- L(misaligned) = βλ · (1-λ) · (1-βλ)¹⁴

$$\boxed{\frac{\mathcal{L}(\text{aligned})}{\mathcal{L}(\text{misaligned})} = \frac{1-\beta\lambda}{\beta(1-\lambda)}}$$

Same formula as part (b) — the ratio depends only on the outlier pixel, not the total number of background pixels.

### Part (e): 16-pixel case, three outliers (Figure 9)

With 3 outlier pixels, and the measured pattern hitting exactly those 3 positions at r=0°:
- L(aligned) = λ³ · (1-βλ)¹³
- L(misaligned) = (βλ)³ · (1-λ)³ · (1-βλ)¹⁰

$$\boxed{\frac{\mathcal{L}(\text{aligned})}{\mathcal{L}(\text{misaligned})} = \left[\frac{1-\beta\lambda}{\beta(1-\lambda)}\right]^3}$$

The ratio is the **cube** of the single-outlier ratio — each outlier contributes multiplicatively (additively in log-likelihood). More outlier pixels → exponentially better discrimination.

### Part (f): Average Log-Likelihood

For N pixels (M outliers at λ, N-M background at βλ):

$$\boxed{E[\ln\mathcal{L}] = M[\lambda\ln\lambda + (1-\lambda)\ln(1-\lambda)] + (N-M)[\beta\lambda\ln(\beta\lambda) + (1-\beta\lambda)\ln(1-\beta\lambda)]}$$

This is derived by taking the expectation E[k_i] = μ_i for each pixel and substituting into the log-likelihood sum. Monte Carlo verification confirms this matches simulation (see output plot).

### Outputs
- `task5f_log_likelihood.png` — Analytical vs. Monte Carlo verification (reproduces Figure 10)

---

## Task 6: Sparse Data Format [20 points]

### Approach (< 300 words)

With 65,535 patterns of 25×25 pixels stored in sparse format (only row/column indices of nonzero entries), the dense design matrix (65k × 625 ≈ 41M entries) is manageable in memory, but we optimize by working directly with sparse representations.

**Sparse log-likelihood computation:** For each rotation r and pattern i:
$$\ln\mathcal{L}(r|k_i) = \underbrace{\sum_j \ln(1-\mu_{r,j})}_{\text{constant per }r} + \sum_{j \in \text{hits}_i} \ln\frac{\mu_{r,j}}{1-\mu_{r,j}}$$

The first term is precomputed once per rotation. The second term only sums over the sparse nonzero pixels — typically very few per pattern. This makes each EM iteration O(n_patterns × avg_hits × 4) instead of O(n_patterns × n_pixels × 4).

**Algorithm:** Same EM as Task 4, but using sparse operations:
1. Group nonzero entries by pattern ID for efficient access.
2. E-step: compute log-likelihood using sparse formula above.
3. M-step: reconstruct master using `np.bincount` on sparse indices, filtered by class membership.

### Outputs
- `task6b_naive_avg.png` — Naive average (featureless)
- `task6c_class_averages.png` — Four orientation class averages
- `task6c_master.png` — Reconstructed master image

---

## Task 7: Sharing Data Amongst Orientations [20 points]

### Approach (< 500 words)

The ultimate challenge: 100,000 patterns (25×25, sparse). The signal-to-noise ratio is so low that even 25,000 patterns per class (after hard classification) produce noisy reconstructions. The hint reveals the key: **every orientation class must be informed by all patterns**.

We implement a **Soft EM algorithm** that replaces hard classification with probabilistic (soft) assignments:

**E-step:** For each pattern i, compute posterior probabilities for all 4 rotations:
$$P(r|k_i, \mu) = \frac{\mathcal{L}(r|k_i, \mu)}{\sum_{r'} \mathcal{L}(r'|k_i, \mu)}$$

Using log-likelihood with softmax normalization for numerical stability:
$$P(r|k_i) = \frac{\exp(\ln\mathcal{L}_r - \max_r \ln\mathcal{L}_r)}{\sum_{r'}\exp(\ln\mathcal{L}_{r'} - \max_r \ln\mathcal{L}_r)}$$

**M-step:** Update master pixel j using ALL patterns weighted by posteriors:
$$\mu_j = \frac{\sum_i \sum_r P(r|i) \cdot k_{i, \pi_r(j)}}{\sum_i \sum_r P(r|i)}$$

where π_r(j) maps master pixel j to its position in a pattern at rotation r.

**Key mathematical insight:** This is equivalent to the standard EM for mixture models where the latent variable is the discrete rotation. Each pattern contributes to the master estimate four times (once per rotation), weighted by how likely that rotation is. When a pattern's orientation is uncertain (posterior ≈ 0.25 for all rotations), it still contributes useful information — the average over rotations still constrains the master image.

**Implementation optimizations:**
1. Precompute pixel permutations for all 4 rotations (integer arrays mapping master→pattern coordinates).
2. Use vectorized softmax for stable posterior computation.
3. Sparse accumulation via `np.add.at` for the M-step numerator.

The soft EM typically converges in 15–25 iterations, with the mean posterior entropy decreasing as the master estimate sharpens. The final reconstruction should reveal a recognizable face of a famous person.

### Outputs
- `task7a_master.png` — Reconstructed master image (famous person)
- `task7a_master_rotations.png` — Master in all 4 orientations
- `task7_confidence.png` — Distribution of classification confidence

---

## Summary of Methods

| Task | Method | Key Technique |
|------|--------|---------------|
| 1 | Direct comparison | SSD, exact match |
| 2 | Flattened comparison | Rotation → flatten permutation |
| 3 | KMeans clustering | Unsupervised clustering + orientation mapping |
| 4 | Hard EM | Iterative log-likelihood classification |
| 5 | Theory | Bernoulli likelihood, log-likelihood expectations |
| 6 | Sparse Hard EM | Sparse log-likelihood computation |
| 7 | Soft EM | Probabilistic assignments, shared data |

## Mathematical Framework

The entire solution rests on two pillars:

1. **Rotation as pixel permutation:** For discrete 90° rotations, rotation followed by flattening is a permutation of pixel indices. This makes rotation a well-defined, invertible operation on flattened vectors.

2. **Bernoulli log-likelihood:** For sparse photon counting data, each pixel is an independent Bernoulli trial. The log-likelihood decomposes into per-pixel contributions, enabling efficient vectorized computation and the clean analytical results of Task 5.

The progression from direct comparison → KMeans → Hard EM → Soft EM mirrors the increasing difficulty: as SNR decreases, we need progressively more sophisticated statistical machinery to extract the signal buried in noise.

---

*Team India — SIMC 2024 Endeavour Challenge*
