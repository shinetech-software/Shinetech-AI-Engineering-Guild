---
name: git-cz-commit-assistant
description: >-
  Prepare and improve strict Conventional Commit messages for any git repository, then guide final commit execution with Commitizen (`git cz`). Use when user asks to commit current changes, improve commit wording from staged diff, align messages with existing history while applying best-practice wording, enforce `type(scope): subject`, infer scope from file paths (especially `pages/...`), and generate concise commit body bullets before confirmation.
---

# Git CZ Commit Assistant

## Overview

Use this skill to produce high-quality commit messages from real staged changes, keep compatibility with `git cz`, and improve wording quality over weak historical patterns.

## Workflow

1. Confirm repository context.

- Run `git rev-parse --is-inside-work-tree`.
- Stop if not inside a git repository.

2. Stage tracked changes safely.

- Run `git add -u`.
- Run `git status --short`.
- Continue only when staged entries exist.

3. Collect commit context.

- Run `git diff --cached --name-only`.
- Run `git diff --cached --numstat`.
- Run `git diff --cached`.
- Run `git log --oneline -n 30`.

4. Draft commit proposal.

- Run `python3 ~/.codex/skills/git-cz-commit-assistant/scripts/infer_commit_draft.py`.
- Include exactly 3 body bullets from `body_bullets`:
  - what changed
  - why needed
  - risk/test note

5. Present and confirm before final commit command.

- Show 2 to 3 subject options and one recommended option.
- Show the 3-bullet body draft.
- Show history wording notes when returned.
- Ask for confirmation.

6. Execute final command.

- Default to `git cz`.
- If the user requests non-interactive flow, use `git commit -m` with approved text.

7. Verify result.

- Run `git log -1 --pretty=%B`.
- Confirm the committed subject matches strict Conventional Commit format.

## Message Rules

Read [references/commit_rules.md](references/commit_rules.md) and enforce it.

## History Guidance

Read [references/history_review.md](references/history_review.md) and improve wording quality for the new commit without rewriting old commits automatically.
