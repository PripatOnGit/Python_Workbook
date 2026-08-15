# AGENTS.md

This repo is a Python learning and interview-prep workspace organized by roadmap phase rather than by ad hoc topic.

## Project goal

The goal is to help a learner build logic, Python fundamentals, problem-solving patterns, and future-facing topics in a structured revision flow.

## Important documents

- [README.md](README.md): overview of the project and study flow
- [ROADMAP.md](ROADMAP.md): phase-by-phase learning plan
- [Python_prep_plan.html](Python_prep_plan.html): full roadmap / visual learning plan

## Folder structure

Use the phase folders as the source of truth:

- P0_Logic_Foundations: decomposition, pseudocode, conditionals, loops, functions, debugging
- P1_Python_Fundamentals: Python basics, strings/lists, dicts/sets, exceptions, file I/O, OOP, modules
- P2_Problem_Solving_Patterns: arrays/strings, hashing, two pointers, recursion, stacks/queues, complexity
- P3_Data_Manipulation: NumPy, pandas, SQL, regex
- P4_Data_Engineering_Core: databases, ETL/ELT, APIs, Airflow, PySpark, cloud, Docker
- P5_GenAI_Agent_Building: LLMs, prompting, RAG, agents, frameworks, deployment
- 00_Reference: notes, cheat sheets, reusable patterns

## Working conventions

- Keep files inside the most relevant phase folder.
- Prefer small, focused files over broad combined scripts.
- Use descriptive names based on the concept or problem.
- When adding practice work, place it in the matching subfolder and add a brief README if needed.
- Keep solutions readable, explainable, and interview-friendly.
- Favor simple Python and explicit logic over clever one-liners.

## Code expectations

- Prefer plain Python unless the phase specifically requires a library.
- Use clear function names and simple input/output examples.
- If the task relates to a coding problem, include the problem intent in comments or a short docstring.
- For interview practice, emphasize logic clarity over optimization unless the task is specifically about performance.

## Validation

There is no large automated test suite for this repo. For quick validation, use:

- python -m py_compile path/to/file.py
- python path/to/file.py

Use the smallest validation command that checks the changed behavior.

## Agent instructions

- Do not move files into unrelated folders just to be convenient.
- If a new exercise fits a roadmap phase, place it there instead of creating a new top-level category.
- When creating new content, keep the repo easy to revise for interviews: small modules, clear names, and phase-based organization.
- If there is ambiguity, prefer the roadmap and current folder structure over ad hoc organization.
