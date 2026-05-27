# Tasks 3g & 3h — explained

A plain-English companion to the last two parts of Question 3. 3g asks you to *compare* the two
clustering routes you already built (covariance in 3e, Gram in 3f). 3h is the payoff: use
everything to answer "how many unique food samples were there really?"

---

## 3g) Comparing the Two Approaches [3 points]

### The two routes you are comparing

| | 3e — covariance space | 3f — Gram space |
|---|---|---|
| matrix | $\mathbb{C} = \tfrac{1}{\widetilde N}\widetilde{\mathbb{X}}^\top\widetilde{\mathbb{X}}$ | $\mathbb{G} = \tfrac{1}{\widetilde N}\widetilde{\mathbb{X}}\widetilde{\mathbb{X}}^\top$ |
| size | $M \times M$ (feature space, $M=3041$) | $\widetilde N \times \widetilde N$ (sample space) |
| eigenvectors live in | feature space (combinations of frequencies) | sample space (one component per sample) |
| a sample's coordinates | its projections $\vec{\tilde x}_i\cdot\vec\nu_k$ onto the top eigenvectors | read **directly** off the eigenvector components |

### Why the two give the *same* answer (the math connection)

This is exactly the result from **Question 2d**. If $\vec v$ is an eigenvector of $\mathbb{C}$ with
eigenvalue $\lambda$, then left-multiplying by $\widetilde{\mathbb{X}}$ shows $\widetilde{\mathbb{X}}\vec v$ is an
eigenvector of $\mathbb{G}$ with the **same** eigenvalue $\lambda$:

$$
\mathbb{C}\vec v = \lambda\vec v
\;\Longrightarrow\;
\mathbb{G}\,(\widetilde{\mathbb{X}}\vec v) = \tfrac{1}{\widetilde N}\widetilde{\mathbb{X}}\widetilde{\mathbb{X}}^\top\widetilde{\mathbb{X}}\vec v
= \widetilde{\mathbb{X}}\,(\mathbb{C}\vec v) = \lambda\,(\widetilde{\mathbb{X}}\vec v).
$$

So $\mathbb{C}$ and $\mathbb{G}$ share the same nonzero eigenvalues — they are **two views of one underlying
structure**. The coordinates a sample gets in 3e and the coordinates it gets in 3f are related by
exactly this $\widetilde{\mathbb{X}}\vec v$ map (up to a $1/\sigma$ rescaling and a possible sign flip).
That is why **you should find the same number of clusters both ways** — task (i). Any small
visual differences come only from numerics: the two matrices are built and diagonalised
differently, and one may have a friendlier condition number, so its eigenvectors are estimated more
cleanly.

### Task (ii) — what "belonging to a cluster" *means* in each space

This is the conceptual heart of 3g. Both routes cluster the same vials, but the **coordinates**
they use are different in kind:

**(a) Covariance space (3e).** A sample's coordinates are *how strongly it expresses each pattern
of variation*. Each eigenvector $\vec\nu_k$ is a direction in feature space — a particular weighted
combination of the 3041 frequencies, i.e. a spectral "shape." The coordinate $\vec{\tilde x}_i\cdot\vec\nu_k$
says how much of that shape sample $i$ contains. **Belonging to a cluster = having a similar
chemical fingerprint**: two vials are close because their spectra are built from the same mix of
spectral features.

**(b) Gram space (3f).** Here the coordinates come straight from sample-to-sample similarity. The
entry $G_{ij}$ is the dot-product similarity between vials $i$ and $j$; each row of $\mathbb{G}$ is one
vial's "similarity fingerprint" to every other vial. The eigenvectors are already
$\widetilde N$-dimensional, so each component *is* a sample's coordinate. **Belonging to a cluster =
being highly similar to the same group of vials**: proximity means "these vials look like each
other," measured directly, without ever naming a feature direction.

> **One-line contrast.** Covariance space asks *"which spectral patterns does this vial contain?"*;
> Gram space asks *"which other vials does this one resemble?"* Same clusters, because resembling
> the same vials and containing the same patterns are two descriptions of the same fact.

---

