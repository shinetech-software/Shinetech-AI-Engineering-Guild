# History Review Guidance

## Goal

Review recent commits to keep style continuity while improving new commit quality.

## Process

1. Read `git log --oneline -n 30`.
2. Extract common scope patterns already used in the repository.
3. Detect weak wording patterns and avoid repeating them.
4. Keep compatibility with project conventions when they are valid.
5. Improve only the new commit proposal.

## Do Not

- Do not rewrite old commits automatically.
- Do not force low-value style changes when scope/type is already clear.
- Do not ignore staged diff evidence in favor of history patterns.

## Heuristics

- Reuse known scopes where they make sense.
- If history contains typo or tense issues, emit a short guidance note.
- Keep proposal deterministic from staged changes, not random phrasing.
