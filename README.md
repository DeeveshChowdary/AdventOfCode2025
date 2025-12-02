# Advent of Code 2025 — Solutions

## Overview

Advent of Code is an annual set of programming puzzles released each December. Each day contains two related problems that encourage algorithmic thinking, design trade-offs, and concise implementation.

This repository contains my solutions for Advent of Code 2025. Implementations emphasize clarity and correctness, with reasonable attention to performance where needed. The project also includes small utilities for input loading and timing, plus notes on algorithms and recurring patterns.

## Purpose

- Collect per-day solutions in a consistent, reviewable format suitable for a technical portfolio.
- Provide runnable, testable code that demonstrates problem-solving and practical Python engineering.
- Retain short notes about algorithm choices and reusable helpers to speed up subsequent problems.

## Repository structure

Top-level layout:

```
advent-of-code-2025/
├── README.md
├── data/
│   ├── day01/
│   │   ├── sample.txt
│   │   └── input.txt
│   ├── day02/
│   │   ├── sample.txt
│   │   └── input.txt
│   └── ...
├── src/
│   └── python/
│       ├── day01/
│       │   ├── part1.py
│       │   ├── part2.py
│       │   └── README.md
│       ├── day02/
│       │   ├── part1.py
│       │   ├── part2.py
│       │   └── README.md
│       └── ...
├── utils/
│   ├── input_loader.py
│   ├── timing.py
│   └── helpers.py
├── scripts/
│   ├── run_day.py
│   └── new_day.py
└── notes/
    ├── algorithms.md
    └── patterns.md
```

Key notes:
- `data/dayNN/` — contains `input.txt` (your personal puzzle input) and `sample.txt` (the example from the problem statement).
- `src/python/dayNN/` — solution code split into `part1.py` and `part2.py`. Per-day `README.md` files summarize the approach and complexity.
- `utils/` — shared helpers (input parsing, timing helpers, and small utility routines).
- `scripts/run_day.py` — convenience script to run a day/part and optionally time it.
- `notes/` — short algorithm references and reusable patterns.

## Running solutions locally

Prerequisites:
- Python 3.10+ is recommended.
- A virtual environment is suggested for reproducibility.

Typical workflow:

1. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies if a requirements file is present:

```bash
pip install -r requirements.txt
```

3. Run a specific part directly (explicit input path):

```bash
python src/python/day01/part1.py data/day01/input.txt
python src/python/day01/part2.py data/day01/input.txt
```

Each `partX.py` is expected to accept (or be easily adapted to accept) an input file path and print the result to stdout. Per-day `README.md` files show the exact invocation when a different interface is used.

4. Use the runner script (if present):

```bash
python scripts/run_day.py --day 01 --part 1
python scripts/run_day.py --day 01 --part 2 --sample
```

If `scripts/run_day.py` is not yet implemented or has a different CLI, run the part scripts directly as shown above.