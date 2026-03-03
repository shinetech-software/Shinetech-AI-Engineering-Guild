# Git CZ Commit Assistant

Drafts and improves strict Conventional Commit messages from staged git changes, then guides final commit execution with Commitizen (`git cz`).

<img width="1289" height="636" alt="screenshot-2026-03-02_15-50-10" src="https://github.com/user-attachments/assets/ac2f4ab5-f700-4579-a07d-88e03aee8d94" />


## What this skill does

- Builds commit proposals from real staged diffs instead of generic guesses.
- Enforces strict Conventional Commit structure: `type(scope): subject`.
- Suggests 2-3 subject options with one recommended option.
- Produces exactly 3 body bullets (what changed, why needed, risk/test note).
- Uses recent history as guidance to keep style continuity while improving wording quality.

## Workflow

The skill follows this sequence:

1. Validate repository context with `git rev-parse --is-inside-work-tree`.
2. Stage tracked changes safely with `git add -u` and confirm staged entries.
3. Collect staged context:
   - `git diff --cached --name-only`
   - `git diff --cached --numstat`
   - `git diff --cached`
   - `git log --oneline -n 30`
4. Infer draft commit data with `scripts/infer_commit_draft.py`.
5. Present subject options, 3 body bullets, and history notes.
6. After confirmation, execute commit:
   - default: `git cz`
   - optional non-interactive: `git commit -m "..."`
7. Verify final result with `git log -1 --pretty=%B`.

## Rules enforced

From `references/commit_rules.md`:

- Allowed types: `feat`, `fix`, `style`, `refactor`, `test`, `build`, `docs`, `perf`, `chore`
- Subject style:
  - imperative verb
  - lower-case first word
  - under 72 chars
  - no trailing period
- Body format: exactly 3 bullets

## Inference behavior

`scripts/infer_commit_draft.py` outputs JSON with:

- `recommended_type`
- `recommended_scope`
- `recommended_subject`
- `subject_options`
- `body_bullets`
- `history_notes`
- `confidence`
- `dominant_file`
- `staged_files`

Type inference is heuristic:

- `test`: all staged files look like test files
- `docs`: all staged files are docs/readme-like
- `build`: dependency or build manifest files changed
- `fix`: patch contains fix-like terms repeatedly
- `refactor`: patch contains refactor-like terms repeatedly
- fallback: `feat`

## Known limitations

- Scope inference is currently not implemented (`infer_scope()` returns `None`).
- Body bullets are currently template-driven and may need user refinement.
- Heuristic type detection can be overridden when project context requires it.

## Repository files

- `SKILL.md` - skill definition and workflow
- `references/commit_rules.md` - commit formatting rules
- `references/history_review.md` - history wording guidance
- `scripts/infer_commit_draft.py` - commit draft inference engine
- `agents/openai.yaml` - agent metadata
