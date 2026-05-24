# SIMC 2.0 — Skill Tree

> A dependency-based learning roadmap for 3 team members starting from zero.
> Competition date: **May 24, 2026** | Prep window: **~10 weeks**
>
> **How to read this:** Skills are organized into Tiers (0–4). You must complete
> a skill's prerequisites (listed after the ←) before moving to it.
> The General track is MANDATORY for all 3 members. Then each member follows
> their Specialization track.

---

## Legend

```
[SKILL NAME]                        ← prerequisite1, prerequisite2    ~Xh  TAG
  "Brief description."
```

- **Unlocked** = all prerequisites completed
- Hours are per-skill, solo study + practice
- Tags: **ALL** = everyone | **MOD** = Modeller | **COD** = Coder | **COM** = Communicator

---

## TIER 0 — Ground Zero (Weeks 1–2, ~30h total)

> Everyone does everything here. No exceptions. This is the shared foundation.

### 0A. Math Foundations

```
[0A1] Basic Algebra                                          ← (none)        ~3h  ALL
  "Variables, equations, rearranging formulas, substitution.
   The language everything else is written in."

[0A2] Functions & Graphs                                     ← 0A1           ~3h  ALL
  "f(x) notation, plotting by hand, linear/quadratic/exponential shapes.
   You need to read and sketch graphs fluently."

[0A3] Units & Dimensions                                     ← 0A1           ~2h  ALL
  "Every quantity has units. Check that both sides of an equation match.
   Catches errors before they cascade."

[0A4] Rates of Change (Intuition)                            ← 0A2           ~2h  ALL
  "Speed is change in distance over time. Growth rate is change in
   population over time. Understand 'rate' before you see derivatives."
```

### 0B. Python Foundations

```
[0B1] Python Setup & Running Scripts                         ← (none)        ~1h  ALL
  "Install Python, run a .py file from terminal, use print() to see output."

[0B2] Variables, Types & Arithmetic                          ← 0B1           ~2h  ALL
  "int, float, string, bool. Arithmetic operators. Type conversion."

[0B3] Conditionals & Loops                                   ← 0B2           ~3h  ALL
  "if/elif/else, for loops, while loops. The control flow of every program."

[0B4] Functions                                              ← 0B3           ~3h  ALL
  "def, parameters, return values. Break problems into reusable pieces."

[0B5] Lists & Dictionaries                                   ← 0B3           ~2h  ALL
  "Storing collections of data. Indexing, slicing, iterating, .append()."

[0B6] Basic File I/O                                         ← 0B4, 0B5      ~1h  ALL
  "Reading data from .csv or .txt files. Writing results to files."
```

### 0C. Thinking Foundations

```
[0C1] What Is a Model?                                       ← (none)        ~2h  ALL
  "A simplified version of reality that captures the essential behavior.
   Maps, equations, simulations are all models."

[0C2] Assumptions & Simplifications                          ← 0C1           ~2h  ALL
  "Every model makes choices about what to ignore. State them explicitly,
   justify them, and know what breaks if they're wrong."

[0C3] Fermi Estimation                                       ← 0A1, 0C1      ~2h  ALL
  "Quick order-of-magnitude guesses. 'About how many?' questions.
   Essential for sanity-checking your model's output."
```

---

## TIER 1 — Core Literacy (Weeks 3–4, ~35h total)

> Still mostly shared, but specialization tracks begin to branch.
> Prerequisites from Tier 0 must be complete.

### 1A. Math for Modelling

```
[1A1] Differentiation Basics                                 ← 0A4           ~4h  ALL
  "Derivatives as slopes. Power rule, chain rule, product rule.
   Needed to write any equation involving rates."

[1A2] Integration Basics                                     ← 1A1           ~3h  ALL
  "The reverse of differentiation. Area under a curve. Total quantity
   from a rate. You've already used this in session 9."

[1A3] Intro to ODEs                                          ← 1A1           ~4h  ALL
  "dy/dt = f(y,t). Setting up equations from word problems. Separable
   ODEs. Your drainage sim is secretly solving ODEs."

[1A4] Probability Basics                                     ← 0A2           ~3h  ALL
  "Events, outcomes, P(A), P(A|B), expected value. Needed before
   you can add randomness to any model."
```

### 1B. Python for Modelling

```
[1B1] NumPy Fundamentals                                     ← 0B5           ~4h  ALL
  "Arrays, vectorized math, no more manual loops for math.
   np.array, np.linspace, np.zeros, broadcasting."

[1B2] Matplotlib Fundamentals                                ← 1B1           ~4h  ALL
  "plt.plot, plt.scatter, labels, titles, legends, plt.show().
   Every result you produce must become a plot."

[1B3] Classes & OOP Review                                   ← 0B4           ~2h  ALL
  "You used classes in the drainage sim. Solidify: __init__, methods,
   attributes, __repr__. Agents in simulations are objects."

[1B4] Euler's Method (Coded)                                 ← 1A3, 1B1      ~3h  ALL
  "You already did this in session 9. Now generalize: write a reusable
   euler_solve(f, y0, t_span, dt) function."
```

### 1C. Communication Basics

```
[1C1] Report Structure for SIMC                              ← 0C1           ~2h  ALL
  "Executive Summary → Problem Restatement → Assumptions → Model →
   Results → Strengths/Weaknesses → References."

[1C2] Writing About Math                                     ← 1A1, 1C1      ~2h  ALL
  "Introduce every equation with context. Define every variable.
   Interpret every result in words. No orphan equations."

[1C3] Making Good Plots                                      ← 1B2           ~2h  ALL
  "Labeled axes WITH UNITS, legends, appropriate scale (log vs linear),
   clear titles. A plot should be readable without the report."
```

### 1D. Team & Strategy

```
[1D1] Role Assignment                                        ← 0C1           ~1h  ALL
  "Assign Modeller, Coder, Communicator. Everyone contributes everywhere,
   but each person OWNS one track."

[1D2] 30-Hour Time Plan                                      ← 1D1           ~1h  ALL
  "Know the phase breakdown: Explore(3h) → Model v1(5h) → Model v2(7h)
   → Report(7h) → Presentation(4h) → Buffer(3h)."

[1D3] Git for Teams                                          ← 0B1           ~2h  ALL
  "Commit often, meaningful messages, branches for experiments.
   Never lose a working model chasing a better one."
```

---

## TIER 2 — Intermediate & Specialization Begins (Weeks 5–7, ~50h total)

> The tree branches. Each member focuses on their track while maintaining
> awareness of the others. Shared skills are marked ALL.

### 2A. Modeller Track

```
[2A1] Systems of ODEs                                        ← 1A3           ~5h  MOD
  "Predator-prey, SIR epidemic, coupled tanks. Multiple interacting
   quantities. Set up, find equilibria, interpret."

[2A2] Sensitivity Analysis                                   ← 1A3, 1B2      ~3h  MOD+ALL
  "Vary each parameter ±10%, rerun model, plot the change in output.
   Judges EXPECT this. Shows which assumptions matter."

[2A3] Model Validation                                       ← 1A3, 0C3      ~3h  MOD
  "Check code vs hand calculations (verification). Check model vs
   real data or known limits (validation)."

[2A4] Optimization Basics                                    ← 1A1           ~4h  MOD
  "Set derivative = 0 to find max/min. Constrained optimization
   (Lagrange multipliers concept). 'Find the best X.'"

[2A5] Phase Plane Analysis                                   ← 2A1           ~3h  MOD
  "Plot x vs y instead of x vs t. Nullclines, equilibria, stability.
   Qualitative insight without solving equations."

[2A6] Dimensional Analysis (Advanced)                        ← 0A3, 1A3      ~2h  MOD
  "Buckingham Pi theorem. Derive relationships between variables purely
   from their units. Surprisingly powerful shortcut."
```

### 2B. Coder Track

```
[2B1] SciPy ODE Solvers                                      ← 1B4           ~4h  COD
  "scipy.integrate.solve_ivp with RK45. Replace your Euler code.
   More accurate, handles stiff systems, adaptive step size."

[2B2] Monte Carlo Simulation                                 ← 1A4, 1B1      ~5h  COD
  "Generate 10,000 random scenarios, run model on each, plot distribution
   of outcomes. Handles uncertainty elegantly."

[2B3] Pandas Basics                                          ← 1B1           ~3h  COD
  "pd.read_csv, filtering, groupby, .describe(). If the competition
   gives you data, Pandas gets you exploring in minutes."

[2B4] Grid & Spatial Simulations                             ← 1B3, 1B4      ~4h  COD
  "Extend your drainage sim pattern. Finite differences for PDEs on grids.
   Heat diffusion, wave propagation, spatial spread."

[2B5] Agent-Based Modelling                                  ← 1B3           ~4h  COD
  "Individual agents with simple rules → complex emergent behavior.
   Crowds, traffic, ecosystems. Python class per agent type."

[2B6] Advanced Matplotlib                                    ← 1B2           ~3h  COD
  "Subplots, heatmaps (imshow), contour plots, colorbars, annotations.
   Multi-panel figures that tell a complete story."
```

### 2C. Communicator Track

```
[2C1] Executive Summary Writing                              ← 1C1           ~3h  COM
  "One page, standalone. Problem + approach + key result + conclusion.
   Write it LAST, polish it FIRST. Judges read this most."

[2C2] Assumption Documentation                               ← 0C2, 1C1      ~2h  COM
  "Numbered list. Each assumption gets a one-line justification.
   Reference back to these throughout the report."

[2C3] Results Presentation                                   ← 1C2, 1C3      ~3h  COM
  "Tables for exact numbers, plots for trends. Always include units.
   Discuss what results MEAN — never just show raw output."

[2C4] Strengths & Weaknesses Section                         ← 2C3, 2A2      ~2h  COM
  "Explicitly state what your model does well and where it fails.
   Propose extensions. Shows maturity. Judges love this."

[2C5] LaTeX/Markdown for Equations                           ← 1C2           ~3h  COM
  "Professional equation formatting. Even basic LaTeX in a Google Doc
   elevates readability enormously."

[2C6] Storytelling with Data                                 ← 2C3           ~3h  COM
  "Build a narrative arc: 'We expected X, found Y, because Z.'
   Guide the reader through your reasoning, don't dump results."

[2C7] Oral Presentation Structure                            ← 2C1           ~3h  COM
  "Open with real-world motivation, walk through your modelling journey,
   end with the punchline. NOT reading the report aloud."
```

### 2D. Shared Intermediate (ALL)

```
[2D1] Regression & Curve Fitting                             ← 1B1, 1A1      ~3h  ALL
  "np.polyfit, scipy.optimize.curve_fit. Fit lines/curves to data.
   Always plot the fit against the data to check."

[2D2] Linear Algebra Basics                                  ← 0A1, 1B1      ~3h  ALL
  "Vectors, matrices, np.dot, np.linalg.solve. Systems of linear
   equations appear everywhere in modelling."

[2D3] Discrete Models                                        ← 1A3           ~2h  ALL
  "x(n+1) = f(x(n)). When time steps are natural (yearly population,
   financial quarters). Simpler than ODEs for many problems."
```

---

## TIER 3 — Advanced & Competition-Ready (Weeks 8–9, ~35h total)

> Deeper specialization. Cross-training: each specialist teaches the
> others a 15-minute summary of their Tier 2 skills.

### 3A. Modeller Track (Advanced)

```
[3A1] Model Comparison & Selection                           ← 2A3           ~4h  MOD
  "Build 2–3 competing models. Compare using fit-to-data, simplicity,
   and predictive power. Pick the winner with evidence."

[3A2] Linear Programming                                     ← 2A4, 2D2      ~4h  MOD
  "Maximize/minimize a linear objective under linear constraints.
   scipy.optimize.linprog. Classic for resource allocation."

[3A3] Markov Chains                                          ← 1A4, 2D2      ~3h  MOD
  "State transitions with fixed probabilities. Matrix multiplication
   gives long-run behavior. Easy to simulate."

[3A4] Game Theory Basics                                     ← 2A4           ~3h  MOD
  "Nash equilibrium, dominant strategies. When the problem involves
   competing agents making decisions."

[3A5] PDE Concepts                                           ← 2A1, 2B4      ~3h  MOD
  "Heat equation, diffusion, wave equation. Won't solve analytically
   under time pressure, but know what they model."
```

### 3B. Coder Track (Advanced)

```
[3B1] Animation                                              ← 2B6           ~4h  COD
  "matplotlib.animation for showing simulation evolution over time.
   Extremely powerful for oral presentations."

[3B2] Graph Theory in Code                                   ← 2D2, 1B1      ~4h  COD
  "Nodes, edges, adjacency matrices. Dijkstra's shortest path, BFS.
   networkx library. Transport/infrastructure problems."

[3B3] Stochastic Simulation                                  ← 2B2           ~3h  COD
  "Adding randomness to deterministic models. Run many realizations,
   report distributions of outcomes, confidence intervals."

[3B4] Root Finding & Numerical Tools                         ← 2B1           ~3h  COD
  "scipy.optimize.brentq, fsolve. Finding equilibria, solving implicit
   equations. Convergence checks."

[3B5] Code Architecture for 30 Hours                         ← 2B1, 2B5      ~2h  COD
  "Modular functions, clear naming, docstrings. Your code must be
   readable by your teammates under time pressure."
```

### 3C. Communicator Track (Advanced)

```
[3C1] Visual Aids & Slide Design                             ← 2C7           ~3h  COM
  "One idea per slide. Figures > text. Diagrams of your model structure.
   Flow charts showing the modelling cycle."

[3C2] Handling Judge Q&A                                     ← 2C4, 2C7      ~3h  COM
  "Anticipate questions about assumptions, alternatives, limitations.
   Practice defending choices with confidence AND humility."

[3C3] Time Management (Presentation)                         ← 3C1           ~2h  COM
  "Rehearse to fit the time limit exactly. Know what to cut if running
   over. Smooth transitions between speakers."

[3C4] Technical Editing                                      ← 2C5           ~3h  COM
  "Consistency in notation, formatting, figure numbering, references.
   The report should look like one person wrote it."

[3C5] Figure Captioning & Cross-Referencing                  ← 2C3           ~2h  COM
  "Every figure gets a caption that tells you what to see. Text
   references: 'As shown in Figure 3...' Link analysis to visuals."
```

---

## TIER 4 — Integration & Mock Competition (Week 10, ~15h total)

> All tracks converge. The team works together as a unit.

```
[4A] Practice Problem #1 (Guided)                            ← Tier 2 done   ~6h  ALL
  "Full team attempt on a past SIMC-style problem with hints.
   Practice the 30-hour workflow in a compressed 6-hour session."

[4B] Practice Problem #2 (Unguided)                          ← 4A            ~6h  ALL
  "Second full attempt, no hints. Time yourselves. Write a mini-report.
   Identify bottlenecks in your team workflow."

[4C] Final Review & Gap Filling                              ← 4B            ~3h  ALL
  "Review both practice attempts. What skills were missing?
   Targeted study on weak spots. Last chance before competition."
```

---

## Dependency Map (Visual Summary)

```
TIER 0                  TIER 1                TIER 2                   TIER 3             TIER 4
─────                   ──────                ──────                   ──────             ──────

                                          ┌─ 2A1-6 (Modeller) ─── 3A1-5 (Mod Adv) ─┐
0A1-4 ──┐               1A1-4 ──┐         │                                         │
0B1-6 ──┼─ ALL ──────── 1B1-4 ──┼── ALL ──┼─ 2D1-3 (Shared)                        ├── 4A ── 4B ── 4C
0C1-3 ──┘               1C1-3 ──┘         │                                         │
                        1D1-3              ├─ 2B1-6 (Coder)   ─── 3B1-5 (Cod Adv) ─┤
                                          │                                         │
                                          └─ 2C1-7 (Comms)   ─── 3C1-5 (Com Adv) ─┘
```

---

## Weekly Schedule

| Week | Dates | Focus | Hours/person |
|------|-------|-------|--------------|
| 1 | Mar 16–22 | Tier 0A + 0B: Math & Python basics | ~15h |
| 2 | Mar 23–29 | Tier 0B + 0C: Finish Python, modelling mindset | ~15h |
| 3 | Mar 30–Apr 5 | Tier 1A + 1B: Calculus, NumPy, Matplotlib | ~18h |
| 4 | Apr 6–12 | Tier 1B + 1C + 1D: ODE coding, reports, team setup | ~17h |
| 5 | Apr 13–19 | Tier 2: Each member starts their specialization | ~18h |
| 6 | Apr 20–26 | Tier 2: Deep dive continues | ~16h |
| 7 | Apr 27–May 3 | Tier 2 finish + 2D shared skills | ~16h |
| 8 | May 4–10 | Tier 3: Advanced specialist skills | ~18h |
| 9 | May 11–17 | Tier 3 finish + cross-training sessions | ~17h |
| 10 | May 18–23 | Tier 4: Mock competitions + final prep | ~15h |

**Total: ~165 hours per person (~2.5 hours/day)**

---

## Who Does What During the 30-Hour Competition

| Phase | Hours | Modeller | Coder | Communicator |
|-------|-------|----------|-------|--------------|
| Explore | 0–3 | Lead assumptions & variables | Research similar models, find data | Restate problem, start assumption log |
| Model v1 | 3–8 | Formulate equations | Implement & debug | Document approach as you go |
| Model v2 | 8–16 | Sensitivity analysis, alt models | Refined simulation, visualization | Draft report sections in parallel |
| Report | 16–23 | Write math sections | Generate all figures, code appendix | Write narrative, edit everything |
| Presentation | 23–27 | Explain model choices | Create animations/demos | Build slides, rehearse team |
| Buffer | 27–30 | Sanity check results | Fix last bugs | Final proofread & polish |

---

## Cross-References

Every skill ID above maps to the detailed descriptions in [Skills.md](Skills.md) (domains A–O).
Use Skills.md for deep reading on any topic. Use THIS file to know **what order** to learn them in.
