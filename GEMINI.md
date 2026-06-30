<!-- GSD:project-start source:PROJECT.md -->

## Project

**Arabic PDF OCR & Categorization CLI**

A Command Line Interface (CLI) tool for batch processing Arabic PDF documents. It cleans the PDFs to improve OCR readability using division normalization and diacritic boosting, then passes the cleaned images directly to a Vision Model (Gemma 4 26B). The model categorizes each page based on user-provided categories at runtime, and the results are saved both to the PDF's page metadata and to a separate JSON/CSV report.

**Core Value:** Accurately pre-process and classify degraded Arabic documents (poor contrast/watermarks) into user-defined categories without losing fine typography.

### Constraints

- **Tech Stack**: Python CLI application.
- **AI Model**: Must interface directly with a Vision Model (e.g., Gemma 4 26B endpoint) using image inputs.
- **Output Requirements**: Must produce both modified PDFs (metadata injected) and structured reports.

<!-- GSD:project-end -->

<!-- GSD:stack-start source:codebase/STACK.md -->

## Technology Stack

- **Language:** Python
- **Environment:** virtual environment (`venv`)
- **Dependencies:** None yet (`requirements.txt` is empty)

<!-- GSD:stack-end -->

<!-- GSD:conventions-start source:CONVENTIONS.md -->

## Conventions

# Conventions

**Date:** 2026-06-30

No coding conventions established yet. Standard Python PEP 8 recommended.
<!-- GSD:conventions-end -->

<!-- GSD:architecture-start source:ARCHITECTURE.md -->

## Architecture

# Architecture

**Date:** 2026-06-30

Greenfield project. No architecture established yet.
<!-- GSD:architecture-end -->

<!-- GSD:skills-start source:skills/ -->

## Project Skills

No project skills found. Add skills to any of: `.agents/skills/`, `.agents/skills/`, `.cursor/skills/`, `.github/skills/`, or `.codex/skills/` with a `SKILL.md` index file.
<!-- GSD:skills-end -->

<!-- GSD:workflow-start source:GSD defaults -->

## GSD Workflow Enforcement

Before using Edit, Write, or other file-changing tools, start work through a GSD command so planning artifacts and execution context stay in sync.

Use these entry points:

- `/gsd-quick` for small fixes, doc updates, and ad-hoc tasks
- `/gsd-debug` for investigation and bug fixing
- `/gsd-execute-phase` for planned phase work

Do not make direct repo edits outside a GSD workflow unless the user explicitly asks to bypass it.
<!-- GSD:workflow-end -->

<!-- GSD:profile-start -->

## Developer Profile

> Profile not yet configured. Run `/gsd-profile-user` to generate your developer profile.
> This section is managed by `generate-claude-profile` -- do not edit manually.
<!-- GSD:profile-end -->
