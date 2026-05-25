---
tags:
  - simc
---

# Random matrix theory intro

> [!abstract] In one line
> Even pure noise produces a predictable eigenvalue spectrum — so you can tell real signal eigenvalues apart from noise eigenvalues just by checking which side of a known boundary they fall on.

## The idea

Imagine filling a spreadsheet with completely random numbers — no structure, no pattern, just white noise — and then computing its covariance matrix and eigenvalues. You might expect the eigenvalues to scatter randomly too, maybe uniform, maybe chaotic. They don't. They obey a precise law.

This is the central surprise of Random Matrix Theory (RMT): randomness at the level of individual entries gives rise to deterministic, universal structure at the level of the spectrum. The eigenvalue histogram of a random covariance matrix fills a specific, predictable band — and that band has sharp edges.

Why does this matter? Because real data is signal plus noise. When you compute a covariance matrix from real measurements, some eigenvalues are driven by genuine chemical or physical variation (signal), and some are just the noise asserting itself. If you know the exact band that pure noise would produce, any eigenvalue above that band must be signal. You don't have to eyeball the scree plot and guess where the "elbow" is — the noise ceiling is a theorem.

This is the theoretical foundation the SIMC report was missing. The report identified an elbow at $k^* = 8$ for the IR spectra dataset, but it hand-waved the justification. RMT provides the principled answer: compute the noise ceiling, and count how many eigenvalues clear it.

The specific law that describes the noise band is the [[marchenko-pastur]] distribution, covered in the next note.

## The math

Consider an $N \times M$ matrix $W$ whose entries are drawn independently from a distribution with mean 0 and variance $\sigma^2$. Form the sample covariance:

$$C = \frac{1}{N} W^\top W$$

This is a [[covariance-matrix]], but built from pure noise. $C$ is $M \times M$ and has $M$ eigenvalues.

**The aspect ratio** is the key parameter:

$$\gamma = \frac{M}{N}$$

It tells you how "wide" vs "tall" the data matrix is. When $\gamma > 1$, you have more features than samples — the high-dimensional regime where noise is hardest to separate from signal.

**The noise ceiling** (derived in [[marchenko-pastur]]) is the largest eigenvalue the noise bulk can reach:

$$\lambda_+ = \sigma^2 \left(1 + \sqrt{\gamma}\right)^2$$

Any eigenvalue of $C$ that exceeds $\lambda_+$ cannot be explained by noise alone. It is a signal eigenvalue.

Symbol glossary:
- $N$ — number of samples (rows of $W$)
- $M$ — number of features (columns of $W$)
- $\sigma^2$ — variance of the noise entries
- $\gamma = M/N$ — aspect ratio
- $\lambda_+$ — upper edge of the noise bulk

> [!example] Tiny concrete example
> Suppose $N = 100$, $M = 400$, $\sigma^2 = 1$. Then $\gamma = 4$ and $\lambda_+ = 1 \cdot (1 + \sqrt{4})^2 = (1+2)^2 = 9$. Any eigenvalue of the sample covariance above 9 is signal. If the scree plot shows eigenvalues of 45, 12, 10.5, 8.2, 7.1, ... then only the first three clear the ceiling — three signal components.

> [!warning] Common confusion
> RMT assumes the noise entries are i.i.d. (independent, identically distributed). Real spectrometer noise is approximately i.i.d. across channels, so this holds well for IR data. But if the instrument has correlated noise bands (e.g., a fixed interference fringe), $\sigma^2$ is not uniform and the Marchenko–Pastur edge will be off. Always sanity-check by looking at whether the "noise" eigenvalues below $\lambda_+$ actually form the predicted histogram shape.

## Why this matters for the report

Q3(c) identifies $k^* = 8$ as the number of signal components, justified by the elbow in the eigenspectrum and the participation ratio $d_{\text{eff}} \approx 8.7$. The elbow is a visual heuristic; the participation ratio is a statistical summary. Neither one comes with a direct physical model of what "noise level" means for this dataset.

RMT closes that gap: it gives a first-principles bound $\lambda_+$ that depends only on the noise variance $\sigma^2$ and the aspect ratio $\gamma$. The claim "eigenvalues above the elbow are signal" can be replaced with the claim "eigenvalues above $\lambda_+$ are signal" — a statement that is provable, not just plausible. See [[marchenko-pastur]] for the exact numbers in the report's geometry ($\tilde N = 924$, $M = 3401$).

## Builds on
- [[covariance-matrix]]
- [[eigenspectrum]]

## Leads to
- [[marchenko-pastur]]
