# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

SIMC 2026 preparation repository for India's 3-person team at the NUS Singapore International Mathematical & Computational Challenge (SIMC 2.0). Competition date: May 24, 2026. The competition gives teams ~30 hours to solve a real-world mathematical/computational modelling problem, write a report, and present to judges.

## Repository Structure

- `Code/` — Learning exercises organized by problem, each with `source/` and `documentation/` subdirectories
- `pastpapers/` — Full solutions to past SIMC competition papers (e.g., `ENDEAVOUR/` for the 2024 challenge). Each has `source/`, `documentation/`, and `outputs/` subdirectories
- `SIMC_LEARNING/` — Learning roadmaps, skill references, and practice problems
  - `SKILLS/` — Skill_Tree.md (ordered dependency-based learning plan), Skills.md (flat domain reference), core.md (quick-reference checklist)
  - `Practice problems/` — Self-contained modelling exercises (e.g., coffee cooling ODE)

## Running Code

No build system, package manager, or test framework. Scripts are standalone Python files run individually:

```bash
# Learning exercises (stdlib only — uses math)
python "Code/Drainage_problem/source/session 10 maincde.py"

# Past paper solutions (requires numpy, matplotlib; optional: scikit-learn)
python pastpapers/ENDEAVOUR/source/main.py            # Run all tasks
python pastpapers/ENDEAVOUR/source/main.py --task 1   # Run specific task
```

## Code Patterns

**Learning exercises** (`Code/`): Simple single-file scripts using only stdlib `math`. OOP for domain entities (e.g., `square` class in drainage sim), procedural simulation loops with explicit phases (rainfall → drain → transfer).

**Past paper solutions** (`pastpapers/`): Multi-module structure with a `main.py` runner importing per-task modules (`task1.py`–`task7.py`) and shared utilities (`utils.py`). Uses `numpy`, `matplotlib`, and `argparse`. Outputs (plots as `.png`) go to an `outputs/` directory.

## Conventions

- **File organization:** Each problem gets a folder with `source/` for `.py` files and `documentation/` for `.md` explanations
- **Documentation:** Every code file should have a companion `.md` doc explaining the math, implementation, and output
- **Learning materials** go under `SIMC_LEARNING/`, not `Code/`
- All non-code files use `.md` format
- The team uses 3 roles: Modeller (equations/analysis), Coder (implementation/simulation), Communicator (report/presentation)

## Context for Code Assistance

This is a learning-focused repo. When helping with code:
- Explain the mathematical reasoning alongside implementation
- Prefer simple, readable code over clever abstractions — the team is building foundational skills
- Connect new concepts back to existing work (e.g., the drainage sim uses Euler's method and OOP; the ENDEAVOUR solution shows modular multi-task structure)
- Code will be written under 30-hour competition pressure — favor clarity and modularity over optimization
