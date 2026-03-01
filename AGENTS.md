# Repository Guidelines

## Project Structure & Module Organization
This repository is a Markdown knowledge base for coding interviews and system design.

- `README.md`: top-level index across all tracks.
- `dsa/`: core data-structures-and-algorithms topic guides (for example, `trees.md`, `dynamic-programming.md`).
- `patterns/`: 45 pattern deep dives named with numeric prefixes (`01-...md` to `45-...md`).
- `patterns/questions/`: pattern-aligned "top 10 questions" playbooks, also numerically prefixed.
- `system-design/`: 20 system design study modules (`01-...md` to `20-...md`).

Keep new files in the most specific folder and follow the existing numbered ordering when extending sequenced content.

## Build, Test, and Development Commands
There is no compile/build pipeline in this repo; contribution flow is content editing + review.

- `rg --files`: list repository files quickly.
- `rg -n "TODO|FIXME" .`: find unfinished notes before opening a PR.
- `git diff -- . ':!*.png'`: review textual changes before commit.
- `git status`: confirm only intended files changed.

If you use a Markdown linter locally, run it before submitting (optional but recommended).

## Coding Style & Naming Conventions
- Use clear Markdown structure: one `#` title, then logical `##`/`###` sections.
- Prefer concise, interview-oriented writing with actionable bullets.
- Keep filenames lowercase kebab-case; for sequenced guides, preserve `NN-topic-name.md`.
- Use relative links for cross-references (for example, `./README.md`, `../dsa/graphs.md`).
- Avoid large, unstructured paragraphs; use short sections and lists.

## Testing Guidelines
Automated tests are not configured. Validate changes through content quality checks:

- Verify links and anchors you touched resolve correctly.
- Confirm numbering/order remains consistent in index files.
- Preview Markdown rendering to catch heading/list formatting issues.

## Commit & Pull Request Guidelines
Current history is minimal and merge-based (for example, `Merge feature/portability`).

- Prefer focused commits with imperative subjects (for example, `Add DP pattern question set`).
- Keep branch naming descriptive (for example, `feature/patterns-graph-refresh`).
- PRs should include: purpose, changed paths, structural impacts (renames/reordering), and any follow-up work.
- When editing indexes, mention how ordering/link integrity was verified.
