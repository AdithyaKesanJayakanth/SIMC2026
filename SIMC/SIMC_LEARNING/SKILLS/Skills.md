# SIMC2.0 — Complete Skills Reference

> Every skill a team could need for the Singapore International Mathematical & Computational Challenge.
> Organised by domain. Use this as a checklist — divide topics across your 3 team members.

---

## A. Mathematical Modelling (Core Process)

### A1. The Modelling Cycle
Formulating real-world problems into mathematical language: **Problem → Assumptions → Variables → Model → Solve → Validate → Refine → Communicate**. This is the backbone of everything you do in SIMC.

### A2. Assumption Making & Justification
Deciding what to ignore and what to keep. Good assumptions simplify the problem without killing its realism. You must be able to state each assumption, explain why it's reasonable, and describe how your results change if the assumption is wrong.

### A3. Dimensional Analysis
Checking that every equation's units are consistent. Also useful for deriving relationships between variables without solving anything — surprisingly powerful for quick estimates.

### A4. Fermi Estimation
Rapid order-of-magnitude reasoning ("How many piano tuners in Chicago?"). Useful at the start of a problem when you have no data and need ballpark numbers to set parameters.

### A5. Sensitivity Analysis
Systematically varying each parameter to see how much the output changes. Tells you which assumptions matter most and which are safe to approximate. Judges expect this in every strong report.

### A6. Model Validation & Verification
Verification = "did we solve the equations right?" (check code against hand calculations). Validation = "did we write the right equations?" (check model against real data or known limiting cases).

### A7. Model Comparison & Selection
Building 2–3 competing models (e.g. linear vs. nonlinear, deterministic vs. stochastic) and using criteria like fit-to-data, simplicity, and predictive power to choose the best one.

---

## B. Differential Equations & Dynamical Systems

### B1. Ordinary Differential Equations (ODEs)
Equations relating a quantity to its rate of change. Most physical, biological, and economic models reduce to ODEs. Know how to set them up from word descriptions and solve simple ones analytically (separable, linear, exact).

### B2. Systems of ODEs
Multiple interacting quantities (e.g. predator-prey, SIR epidemic model, chemical reactions). Understand equilibrium points and how trajectories behave near them.

### B3. Phase Plane Analysis
Plotting one variable against another (instead of against time) to visualise system behavior — stability, cycles, convergence. Gives qualitative insight without solving the equations.

### B4. Partial Differential Equations (PDEs) — Conceptual
Heat equation, wave equation, diffusion. You won't solve these analytically under time pressure, but you should understand what they model and how to discretise them for numerical solution on a grid.

### B5. Difference Equations & Recurrences
Discrete-time analogues of ODEs: x(n+1) = f(x(n)). Natural for models where time steps are fixed (population each year, financial periods, iterative algorithms).

---

## C. Optimisation

### C1. Single-Variable Optimisation
Finding maxima/minima using calculus (set derivative to zero) or numerical search. Applicable whenever the problem says "find the best/most efficient/minimum cost."

### C2. Multivariable Optimisation
Gradient descent, Lagrange multipliers (for constrained problems). Needed when you're tuning multiple parameters simultaneously.

### C3. Linear Programming
Maximising/minimising a linear objective subject to linear inequality constraints. Classic for resource allocation, scheduling, and logistics problems. Know the simplex concept; use `scipy.optimize.linprog` to solve.

### C4. Integer & Combinatorial Optimisation
When variables must be whole numbers (assign people to tasks, select items with weight limits). Includes knapsack, assignment, and travelling salesman-type problems. Often solved with greedy heuristics or brute force for small inputs.

### C5. Multi-Objective Optimisation
When you need to optimise two conflicting goals simultaneously (e.g. minimise cost AND maximise quality). Understand Pareto fronts — the set of solutions where you can't improve one goal without worsening another.

---

## D. Probability & Statistics

### D1. Probability Distributions
Know the key distributions and when they apply: Uniform (equal chance), Normal/Gaussian (natural variation), Poisson (rare events per interval), Exponential (time between events), Binomial (n trials, k successes).

### D2. Expected Value & Variance
Summarising random outcomes with a single number (mean) and a measure of spread. Essential for comparing strategies under uncertainty.

### D3. Conditional Probability & Bayes' Theorem
Updating beliefs with new evidence. Useful when a problem gives partial information or sequential observations.

### D4. Monte Carlo Simulation
Using random sampling to estimate quantities that are hard to compute analytically. Generate thousands of random scenarios, run your model on each, and aggregate results. Extremely versatile.

### D5. Regression & Curve Fitting
Fitting a function (linear, polynomial, exponential) to data points using least squares. Know `numpy.polyfit` and `scipy.optimize.curve_fit`. Always plot the fit against the data.

### D6. Hypothesis Testing & Confidence Intervals (Basic)
Determining whether an observed pattern is real or due to chance. Useful if the problem provides noisy data and asks you to draw conclusions.

### D7. Markov Chains
Systems that transition between states with fixed probabilities. Models weather patterns, random walks, board games, queuing systems. Easy to simulate and analyse with matrix multiplication.

---

## E. Linear Algebra

### E1. Vectors & Matrices
Representing systems of equations, transformations, and data. Know matrix multiplication, transpose, inverse. Use `numpy` for all computation.

### E2. Solving Linear Systems (Ax = b)
Arises in network flow, equilibrium problems, fitting models. Use `numpy.linalg.solve`. Understand when systems have no solution or infinitely many.

### E3. Eigenvalues & Eigenvectors
Determine long-term behavior of linear dynamical systems and Markov chains. The dominant eigenvalue tells you growth/decay rates.

### E4. Least Squares (Overdetermined Systems)
When you have more data points than unknowns, find the "best fit" solution. Foundation of regression. Use `numpy.linalg.lstsq`.

---

## F. Graph Theory & Networks

### F1. Graph Fundamentals
Nodes, edges, directed vs. undirected, weighted graphs. Many real-world problems (transport, communication, social networks) naturally map to graphs.

### F2. Shortest Path Algorithms
Dijkstra's algorithm, BFS for unweighted graphs. Finding optimal routes in networks.

### F3. Minimum Spanning Trees
Connecting all nodes at minimum total cost (Kruskal's/Prim's). Useful for infrastructure design problems.

### F4. Network Flow & Matching
Maximum flow through a network (pipes, roads, bandwidth). Ford-Fulkerson concept. Matching problems (assigning agents to tasks optimally).

### F5. Connectivity & Clustering
Identifying components, bridges, bottlenecks. Community detection. Relevant when analysing network robustness or social structures.

---

## G. Discrete Mathematics & Combinatorics

### G1. Counting Principles
Permutations, combinations, inclusion-exclusion. Needed whenever the problem involves "how many ways" or "how many configurations."

### G2. Recurrence Relations
Defining sequences by their relationship to previous terms (Fibonacci-type). Often arise in discrete modelling and algorithm analysis.

### G3. Pigeonhole Principle & Extremal Arguments
Simple but powerful reasoning tools for proving bounds and existence results.

### G4. Algorithmic Thinking
Greedy algorithms, divide and conquer, dynamic programming. Not just for CS — these strategies help structure any sequential decision-making model.

---

## H. Calculus & Analysis

### H1. Differentiation (Single & Multi-variable)
Rates of change, finding extrema, Taylor approximations. The fundamental tool for analysing smooth models.

### H2. Integration
Computing areas, volumes, total quantities from rates. Numerical integration (trapezoidal rule, Simpson's rule) when analytical solutions aren't possible.

### H3. Taylor Series & Approximations
Approximating complex functions with polynomials near a point. Useful for simplifying models and understanding error in numerical methods.

### H4. Vector Calculus Basics
Gradients, divergence, line integrals — conceptual understanding. Relevant for flow, field, and spatial distribution problems.

---

## I. Numerical Methods (Computational)

### I1. Euler's Method
Simplest ODE solver: step forward using the derivative. You already know this. Understand its error (first-order) and when it fails (stiff systems, large steps).

### I2. Runge-Kutta Methods (RK4)
Fourth-order ODE solver — much more accurate than Euler for the same step size. Use `scipy.integrate.solve_ivp` with `method='RK45'`. This should be your default.

### I3. Root Finding
Newton's method, bisection method. Finding where f(x) = 0. Used in equilibrium calculations and implicit equations. `scipy.optimize.brentq` or `fsolve`.

### I4. Numerical Integration (Quadrature)
Computing definite integrals numerically. `scipy.integrate.quad`. Needed when antiderivatives don't exist in closed form.

### I5. Finite Difference Methods
Approximating PDEs on a grid by replacing derivatives with differences. Your drainage simulation already uses this idea. Extends naturally to heat diffusion, wave propagation, etc.

### I6. Iterative Methods & Convergence
Running a computation repeatedly until the answer stabilises. Know how to set convergence criteria (tolerance) and detect divergence.

---

## J. Simulation & Agent-Based Modelling

### J1. Cellular Automata
Grid of cells that update based on neighbor states (Conway's Game of Life, forest fire models). Your drainage simulation is essentially this. Good for spatial phenomena.

### J2. Agent-Based Models
Individual "agents" follow simple rules; complex system behavior emerges. Models crowds, traffic, ecosystems, economies. Python classes for agents + a simulation loop.

### J3. Discrete Event Simulation
Modelling systems as a sequence of events (customer arrivals, machine breakdowns). Useful for queuing and logistics problems.

### J4. Stochastic Simulation
Adding randomness to any deterministic model. Run many realisations and report distributions of outcomes rather than single numbers. Use `random` or `numpy.random`.

---

## K. Data Handling & Visualisation

### K1. NumPy
Array operations, vectorised math, random number generation. The foundation for all scientific Python. Avoid writing loops when NumPy can do it in one line.

### K2. Matplotlib
Line plots, scatter plots, bar charts, heatmaps, contour plots. Every result in your report should have a clear, labeled figure. Know `plt.subplot` for multi-panel figures.

### K3. Pandas (Basic)
Reading CSV/Excel data, filtering, grouping, summary statistics. If the problem gives you a dataset, Pandas gets you exploring it in minutes.

### K4. Visualization Best Practices
Labeled axes (with units), legends, titles, appropriate scales (log vs linear), colorbar for heatmaps. A clean plot communicates more than a page of text.

### K5. Animation (Optional but Impressive)
`matplotlib.animation` for showing how your simulation evolves over time. Especially powerful for spatial models and oral presentations.

---

## L. Domain-Specific Models (Common Problem Types)

### L1. Population Dynamics
Exponential growth, logistic growth, Lotka-Volterra predator-prey, SIR/SIS epidemic models. These are classic modelling exercises and appear frequently.

### L2. Diffusion & Heat Transfer
How substances or heat spread through a medium. Modelled by the diffusion equation; simulated on grids with finite differences.

### L3. Fluid Flow & Drainage
Water flow through networks, drainage basins, pipe systems. You've already started here — extend with conservation laws and Bernoulli's principle.

### L4. Traffic & Transportation
Vehicle flow on roads, congestion modelling, route optimisation. Can use differential equations (macroscopic) or agent-based (microscopic) approaches.

### L5. Resource Allocation & Scheduling
Distributing limited resources (budget, time, personnel) to maximise some objective. Linear programming and greedy algorithms dominate here.

### L6. Game Theory & Strategic Interaction
Nash equilibrium, dominant strategies, zero-sum games. Applies when the problem involves competing agents making decisions.

### L7. Financial & Economic Models
Compound interest, supply-demand equilibrium, cost-benefit analysis, risk assessment. Simple models with big impact.

### L8. Geometric & Spatial Problems
Packing, coverage, shortest paths in 2D/3D space, Voronoi diagrams. Computational geometry tools can help.

### L9. Environmental & Climate Models
Carbon cycles, energy balance, renewable resource management. Often combine ODEs with data fitting.

### L10. Network & Infrastructure Design
Placing facilities, designing routes, ensuring connectivity and redundancy. Graph theory meets optimisation.

---

## M. Report Writing & Communication

### M1. Executive Summary
One-page standalone summary: problem, approach, key results, main conclusion. Judges weight this heavily. Write it last, polish it first.

### M2. Problem Restatement
Rephrase the problem in your own words. Shows understanding. Clarify any ambiguities and state what you're actually solving.

### M3. Assumption Documentation
A numbered list of every assumption with a one-line justification. Reference back to these throughout the report.

### M4. Mathematical Exposition
Every equation introduced with context ("By Newton's second law..."), variables defined before use, and results interpreted in words after derivation.

### M5. Results Presentation
Tables for exact numbers, plots for trends. Always include units. Discuss what the results mean — don't just show them.

### M6. Strengths & Weaknesses Section
Explicitly state what your model does well and where it falls short. Propose extensions. This shows maturity and always impresses judges.

### M7. LaTeX / Markdown Formatting
Professional-looking equations and layout. Even basic LaTeX for equations in a Google Doc or Word document elevates your report's readability.

---

## N. Oral Presentation

### N1. Storytelling Structure
Open with the real-world motivation, walk through your modelling journey, end with the punchline (key result). Don't just read the report aloud.

### N2. Visual Aids
Slides with figures, diagrams, and animations — minimal text. One idea per slide.

### N3. Handling Judge Q&A
Anticipate questions about assumptions, alternative approaches, and limitations. Practice defending your choices with confidence and humility.

### N4. Time Management
Rehearse to fit the time limit exactly. Know what to cut if you're running over.

---

## O. Team Strategy & Competition Tactics

### O1. Role Division
Suggested split for a team of 3: **(1) Lead Modeller** — math formulation & analysis, **(2) Lead Coder** — implementation & visualisation, **(3) Lead Communicator** — report writing & presentation. Everyone contributes to all areas, but each person owns one.

### O2. Time Allocation (30-hour format)
| Phase | Hours | Activity |
|-------|-------|----------|
| Explore | 3–4 | Read problem, brainstorm, research, initial assumptions |
| Model v1 | 4–5 | Simple "toy" model — get something working fast |
| Model v2 | 6–8 | Refined model with code, sensitivity analysis |
| Report | 6–8 | Write, format, create figures |
| Presentation | 3–4 | Build slides, rehearse |
| Buffer | 2–3 | Debugging, polishing, sleep |

### O3. Version Control
Use Git (you're already set up). Commit working versions frequently so you can always roll back. Never lose a working model chasing a better one.

### O4. Parallel Workstreams
While one person codes the primary model, another can work on data visualisation or an alternative model approach. Maximise the 30 hours by working in parallel, not sequentially.

### O5. Sanity Checks Throughout
After every major step, ask: "Does this number make physical sense?" Fermi estimates and dimensional analysis catch errors early.
