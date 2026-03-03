# Commit Rules

## Required Format

Use strict Conventional Commit format:

`type(scope): subject`

## Allowed Types

- `feat`
- `fix`
- `style`
- `refactor`
- `test`
- `build`
- `docs`
- `perf`
- `chore`

## Scope Rules

Scope is optional. When used:

- Use generic module/component name derived from file paths.
- Example: `components/Button`, `utils/format`, `api/users`.
- Or omit scope entirely for simple commits.

## Subject Rules

- Use imperative verbs: `add`, `fix`, `update`, `refine`, `remove`, `prevent`.
- Use lower-case first word.
- Keep concise and outcome-focused.
- Keep under 72 characters.
- Do not end with period.

## Body Rules

Use exactly 3 bullets:

- What changed
- Why needed
- Risk/test note

## Wording Quality

Prefer corrected spelling and clearer wording:

- `picture` not `picutre`
- `insurance` not `insurnace`
- `lat lng` not `lag lng`

Prefer present imperative style instead of past tense:

- `add provider info` instead of `added provider info`
- `adjust dropdown layout` instead of `adjusted dropdown layout`
