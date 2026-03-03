#!/usr/bin/env python3
"""Infer strict Conventional Commit draft from staged changes."""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass


@dataclass
class NumstatEntry:
    path: str
    added: int
    deleted: int


def run_git(repo: str, args: list[str], check: bool = True) -> str:
    cmd = ["git", "-C", repo, *args]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if check and result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or f"git command failed: {' '.join(cmd)}")
    return result.stdout


def parse_numstat(text: str) -> list[NumstatEntry]:
    entries: list[NumstatEntry] = []
    for raw in text.splitlines():
        parts = raw.split("\t")
        if len(parts) != 3:
            continue
        added_raw, deleted_raw, path = parts
        if added_raw == "-" or deleted_raw == "-":
            continue
        try:
            added = int(added_raw)
            deleted = int(deleted_raw)
        except ValueError:
            continue
        entries.append(NumstatEntry(path=path, added=added, deleted=deleted))
    return entries


def infer_type(files: list[str], patch: str) -> str:
    lower_files = [f.lower() for f in files]
    lower_patch = patch.lower()

    def all_match(predicate) -> bool:
        return bool(lower_files) and all(predicate(f) for f in lower_files)

    if all_match(lambda f: "/test/" in f or "_test." in f or ".test." in f or "/spec/" in f):
        return "test"

    if all_match(lambda f: f.endswith(".md") or "/docs/" in f or "readme" in f):
        return "docs"

    build_files = [
        "package.json", "package-lock.json", "yarn.lock", "pnpm-lock.yaml",
        "cargo.toml", "cargo.lock", "go.mod", "go.sum",
        "requirements.txt", "pipfile", "poetry.lock",
        "pom.xml", "build.gradle", "gradle.properties",
        "pubspec.yaml", "pubspec.lock",
    ]
    if any(any(bf in f for bf in build_files) for f in lower_files):
        return "build"

    fix_terms = ["fix", "bug", "crash", "error", "exception", "fail", "wrong", "incorrect"]
    fix_score = sum(lower_patch.count(term) for term in fix_terms)

    if fix_score >= 3:
        return "fix"

    refactor_terms = ["refactor", "reformat", "rename", "move", "extract", "simplify"]
    refactor_score = sum(lower_patch.count(term) for term in refactor_terms)

    if refactor_score >= 2:
        return "refactor"

    return "feat"


def infer_scope(path: str) -> str | None:
    return None


def subject_options(commit_type: str, scope: str | None, dominant_file: str) -> list[str]:
    templates: list[str] = []
    stem = os.path.splitext(os.path.basename(dominant_file))[0] if dominant_file else "application"

    templates.append(f"add {stem} functionality")
    templates.append(f"update {stem} implementation")
    templates.append(f"improve {stem} behavior")

    seen: set[str] = set()
    cleaned: list[str] = []
    for subject in templates:
        s = re.sub(r"\s+", " ", subject.strip())
        s = s[:72].rstrip(" .")
        if not s or s in seen:
            continue
        seen.add(s)
        cleaned.append(s)
        if len(cleaned) == 3:
            break

    if not cleaned:
        cleaned = ["update application behavior"]

    scope_str = f"({scope})" if scope else ""
    return [f"{commit_type}{scope_str}: {item}" for item in cleaned]


def body_bullets(staged_files: list[str]) -> list[str]:
    file_count = len(staged_files)
    file_list = ", ".join(os.path.basename(f) for f in staged_files[:3])
    if file_count > 3:
        file_list += f" (+{file_count - 3} more)"

    return [
        f"What changed: modified {file_list}.",
        "Why needed: improve functionality or fix an issue.",
        "Risk/test: validate changes manually before pushing.",
    ]


def history_notes(log_text: str) -> list[str]:
    notes: list[str] = []
    lower_log = log_text.lower()

    typo_fixes = {
        "picutre": "picture",
        "teh ": "the ",
        "android": "Android",
        "ios": "iOS",
    }
    for wrong, correct in typo_fixes.items():
        if wrong in lower_log:
            notes.append(f"Prefer `{correct}` instead of `{wrong}`.")

    past_tense_pattern = re.compile(r"^[a-f0-9]+\s+\w+(\([^)]*\))?:\s+(added|handled|changed|adjusted|integrated|updated)\b", re.IGNORECASE)
    if any(past_tense_pattern.match(line) for line in log_text.splitlines()):
        notes.append("Prefer imperative mood: use `add`, `handle`, `change`, `adjust`, `integrate` instead of past tense.")

    return notes


def main() -> int:
    repo = os.getcwd()
    if len(sys.argv) == 3 and sys.argv[1] == "--repo":
        repo = sys.argv[2]

    try:
        in_repo = run_git(repo, ["rev-parse", "--is-inside-work-tree"]).strip()
        if in_repo != "true":
            raise RuntimeError("not inside a git repository")

        staged_names = run_git(repo, ["diff", "--cached", "--name-only"]).strip().splitlines()
        staged_names = [s for s in staged_names if s.strip()]

        if not staged_names:
            print(json.dumps({"error": "no staged changes"}, indent=2))
            return 0

        numstat = parse_numstat(run_git(repo, ["diff", "--cached", "--numstat"]))
        patch = run_git(repo, ["diff", "--cached"])
        log_text = run_git(repo, ["log", "--oneline", "-n", "30"], check=False)

        dominant = ""
        if numstat:
            dominant_entry = max(numstat, key=lambda e: (e.added + e.deleted, e.added))
            dominant = dominant_entry.path
        else:
            dominant = staged_names[0]

        scope = infer_scope(dominant)
        commit_type = infer_type(staged_names, patch)
        options = subject_options(commit_type, scope, dominant)
        bullets = body_bullets(staged_names)
        notes = history_notes(log_text)

        confidence = 0.5
        if dominant:
            confidence += 0.15
        if commit_type in ("fix", "refactor"):
            confidence += 0.15
        if len(staged_names) > 1:
            confidence += 0.1
        confidence = min(confidence, 0.9)

        result = {
            "recommended_type": commit_type,
            "recommended_scope": scope,
            "recommended_subject": options[0],
            "subject_options": options,
            "body_bullets": bullets,
            "history_notes": notes,
            "confidence": round(confidence, 2),
            "dominant_file": dominant,
            "staged_files": staged_names,
        }
        print(json.dumps(result, indent=2))
        return 0
    except Exception as exc:
        print(json.dumps({"error": str(exc)}))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
