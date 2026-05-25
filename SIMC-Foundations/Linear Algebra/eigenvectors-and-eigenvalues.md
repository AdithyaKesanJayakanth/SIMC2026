---
tags:
  - simc
---
			
# Eigenvectors and eigenvalues

> [!abstract] In one line
> Most vectors get rotated when you push them through a matrix; eigenvectors are the special directions that come out pointing the same way — just stretched or shrunk by a factor called the eigenvalue.

## The idea

Think of a matrix as a machine that takes a vector in, transforms it, and spits a (usually different) vector out. Feed it a random arrow: it rotates AND rescales the arrow. The output points somewhere new.

But for a few magic directions, the machine only rescales — no rotation at all. The arrow goes in, and a longer (or shorter, or flipped) version of the exact same arrow comes out. Those special arrows are **eigenvectors**. The stretch factor is the **eigenvalue**.

Analogy: imagine a rubber sheet being stretched horizontally. Most arrows drawn on the sheet rotate as the sheet deforms. But an arrow pointing purely left-right just gets longer — it's an eigenvector of the stretch, with eigenvalue = the stretch ratio.

