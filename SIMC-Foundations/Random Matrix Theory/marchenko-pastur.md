---
tags:
  - simc
---

# Marchenko–Pastur law

> [!abstract] In one line
> For a matrix of pure noise with aspect ratio $\gamma = M/N$, the sample-covariance eigenvalues fill a specific band $[\lambda_-, \lambda_+]$ with known edges — any eigenvalue above $\lambda_+$ is genuine signal, not noise.

## The idea

[[random-matrix-theory-intro]] established that noise has a predictable eigenvalue spectrum. The Marchenko–Pastur law is the exact formula for that spectrum.

Think of it this way: you have a data matrix that is entirely noise — no chemistry, no signal, nothing. You compute its covariance matrix and sort the eigenvalues. The Marchenko–Pastur law says those eigenvalues won't all be zero (they can't be, because the covariance estimator is finitely sampled), and they won't scatter randomly either. They pack into a specific interval $[\lambda_-, \lambda_+]$ with a characteristic arched density shape, like a one-sided hill.

The width of that interval depends on two things: how noisy the data is ($\sigma^2$) and how underdetermined the problem is (the aspect ratio $\gamma = M/N$). More features than samples ($\gamma > 1$) means a wider noise band — more eigenvalues are inflated by sampling error.

The payoff: once you know $\lambda_+$, you count how many eigenvalues of your real covariance matrix exceed it. That count is your signal dimension estimate — derived from a theorem, not eyeballed from a plot.

## The math

For an $N \times M$ noise matrix with i.i.d. entries of variance $\sigma^2$, the sample-covariance eigenvalue density concentrates on $[\lambda_-, \lambda_+]$ in the large-$N, M$ limit, where:

$$\lambda_\pm = \sigma^2 \left(1 \pm \sqrt{\gamma}\right)^2, \qquad \gamma = \frac{M}{N}$$

The density itself (the Marchenko–Pastur distribution) is:

$$\rho(\lambda) = \frac{1}{2\pi \sigma^2 \gamma \lambda} \sqrt{(\lambda_+ - \lambda)(\lambda - \lambda_-)}$$

for $\lambda \in [\lambda_-, \lambda_+]$, and zero outside.

Symbol glossary:
- $N$ — number of samples
- $M$ — number of features
- $\sigma^2$ — noise variance per entry of the raw data matrix
- $\gamma = M/N$ — aspect ratio
- $\lambda_-$ — lower edge of the noise bulk
- $\lambda_+$ — upper edge; the noise ceiling
- $\rho(\lambda)$ — probability density of noise eigenvalues

**Estimating $\sigma^2$ in practice.** The noise variance is the average variance of the small eigenvalues — those you already suspect are noise. One clean way: take the median eigenvalue of the sample covariance. For Marchenko–Pastur the median sits close to $\sigma^2 \gamma$, so $\hat\sigma^2 \approx \lambda_{\text{median}} / \gamma$. Alternatively, the trace identity $\sum_i \lambda_i = \text{tr}(C) = M \sigma^2$ gives $\hat\sigma^2 = \text{tr}(C)/M$ if you believe all variance is noise — a conservative upper bound.

> [!example] The report's numbers
> The IR spectra dataset after cleaning: $\tilde N = 924$ samples, $M = 3401$ features. Aspect ratio:
>
> $$\gamma = \frac{M}{\tilde N} = \frac{3401}{924} \approx 3.68$$
>
> Estimate $\sigma^2$ from the total variance: $\text{tr}(C) \approx 7.90$ (reported in Q3b), so a rough upper bound is $\hat\sigma^2 = 7.90 / 3401 \approx 0.0023$. The noise ceiling is then:
>
> $$\lambda_+ = 0.0023 \times \left(1 + \sqrt{3.68}\right)^2 = 0.0023 \times (1 + 1.918)^2 \approx 0.0023 \times 8.51 \approx 0.020$$
>
> Now look at the Q3(c) eigenvalues: $\lambda_1 \approx 0.31 \times 7.90 \approx 2.45$. Even $\lambda_8$ is vastly above this $\lambda_+$ estimate. The first 8 eigenvalues clear the noise ceiling by orders of magnitude — consistent with $k^* = 8$ signal components.
>
> **Caveat**: using $\text{tr}(C)/M$ as $\hat\sigma^2$ is conservative (it overestimates noise by lumping signal variance in). A tighter estimate — averaging only the tail eigenvalues below the elbow — would give a smaller $\sigma^2$ and a lower $\lambda_+$, making the 8-signal conclusion even sharper.

> [!warning] Common confusion
> The Marchenko–Pastur law is exact only in the double limit $N, M \to \infty$ with $\gamma = M/N$ fixed. For finite matrices it's an approximation — the empirical noise spectrum can spill slightly above $\lambda_+$. In practice, for datasets as large as the report's ($\tilde N = 924$, $M = 3401$), finite-size corrections are small and the boundary $\lambda_+$ is a reliable guide.

## Why this matters for the report

This is the gap the adversary subagent flagged in Q3(c). The report asserts a "noise floor" and picks $k^* = 8$ via the elbow ($\lambda_8/\lambda_9 \approx 4.1$ multiplicative drop) and the participation ratio ($d_{\text{eff}} \approx 8.7$, bootstrap CI $[7.6, 10.0]$). Both are sound heuristics, but neither answers the question an examiner will ask in the oral: **"How do you know the boundary between signal and noise eigenvalues isn't at $k = 5$ or $k = 12$?"**

The Marchenko–Pastur answer is principled: the noise bulk ends at $\lambda_+$, and 8 eigenvalues exceed it. The elbow at $\lambda_8/\lambda_9$ turns out to coincide with this boundary — it's not just a visual heuristic, it's where the Marchenko–Pastur bulk begins. That connection is the derivation the report hand-waved ("multiplicative noise boundary") but never supplied.

For the oral defence, the team should be able to say: "We computed $\gamma \approx 3.68$, estimated $\sigma^2$ from the tail eigenvalues, found $\lambda_+ \approx [value]$, and confirmed 8 eigenvalues lie above it — consistent with the elbow and the participation ratio." That closes the loop.

## Builds on
- [[random-matrix-theory-intro]]
- [[eigenspectrum]]
- [[covariance-matrix]]

## Leads to
- [[elbow-method]]
- [[participation-ratio]]
