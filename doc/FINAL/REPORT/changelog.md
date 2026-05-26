# extras.md — change monitor for `SIMC2026_Preliminary_Q1_Q2.tex`

This file logs **every change** made when turning the handwritten notes into the
LaTeX preliminary report, and flags every **mistake**, **miss**, and **extra**.
Newest changes go at the top of the changelog. The tables below are the
standing record; keep them in sync with the coloured tags in the PDF.

**Source notes (sole basis for the math):**
- `notes/Note 26 May 2026.pdf` — Q1 parts a–b (rough)
- `notes/Note 26 May 2026 (2).pdf` — Q1 parts a–e, g (clean)
- `notes/task 2.pdf` — Q2 parts a–e

**Document built:** `SIMC2026_Preliminary_Q1_Q2.tex` (Q1 & Q2 only; Q3 to come).
**Tag legend (also rendered in the PDF):** 🟥 MISS · 🟧 CORRECTED · 🟦 EXTRA.

---

## 1. 🟧 MISTAKES found in the notes (corrected in the report)

| # | Location | What the notes had | What is correct | Why |
|---|----------|--------------------|-----------------|-----|
| M1 | **Q1(g)** time-varying ε | $\mathbf p(t)=1^{t}c_1+\bigl(1-\varepsilon(t)\bigr)^{t}c_2$ | $\mathbf p(t)=c_1\mathbf v_1+c_2\Bigl[\prod_{s=0}^{t-1}(1-\varepsilon_0e^{-s/t_0})\Bigr]\mathbf v_2$ | With a time-varying rate the matrices $\mathbf M(t)$ differ each step. They share the same eigenvectors (the eigenvectors don't depend on ε), so the $\mathbf v_2$ mode collects **one factor $(1-\varepsilon(s))$ per step** → a *product*, not the power $(1-\varepsilon(t))^t$. |
| M2 | **Q1(c)** linear combination | Used $c_1=1$ directly | $c_1=p_2(0)+\tfrac12$; equals 1 **only if** $p_2(0)=\tfrac12$ | The notes silently assumed the populations are normalised so $p_1(0)+p_2(0)=1$. Now stated explicitly; general form also given. |
| M3 | **Q2(d)(i)** PSD proof | $\mathbf w^\top(\mathbf X^\top\mathbf X)\mathbf w=\lVert \mathbf X^\top\mathbf w\rVert^2$ | $=\lVert \mathbf X\mathbf w\rVert^2$ | Typo: $(\mathbf X^\top\mathbf X)$ pairs with $\lVert\mathbf X\mathbf w\rVert^2$; $\lVert\mathbf X^\top\mathbf w\rVert^2$ belongs to the $\mathbf X\mathbf X^\top$ case. Result (PSD) unaffected. |
| M4 | **Q2(e)(i)** pseudocode label | "if $N\gg M$ compute $\mathbf X\mathbf X^\top$" | "if $N\ge M$ compute $\mathbf X^\top\mathbf X$" (the **smaller** matrix) | The notes' own stated reason ("the smaller matrix is cheaper") and their worked example (3×2 → used $\mathbf X^\top\mathbf X$, the 2×2) both contradict the label. Rule made consistent. |

---

