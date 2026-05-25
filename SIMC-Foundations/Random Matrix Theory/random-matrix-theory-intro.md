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

