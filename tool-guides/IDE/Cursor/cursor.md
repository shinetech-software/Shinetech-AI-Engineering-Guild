# Cursor

![Cursor IDE](https://cursor.sh/brand/app-icon.svg)

## Introduction

Cursor is one of the most popular AI-powered code editors available today. It is a fork of Visual Studio Code, which means it retains the familiar VS Code interface and supports all VS Code extensions, themes, and keybindings — but adds a deeply integrated layer of AI assistance throughout the editing experience.

Cursor integrates with leading AI models including **GPT-4o**, **Claude Sonnet/Opus**, **Gemini**, and more. It supports features like inline code generation, multi-file editing ("Composer"), AI-powered chat, and context-aware code completion ("Tab").

> Cursor 是当前比较热门的 AI IDE，整合了大部分模型，有非常实用方便的功能。

![Cursor screenshot](https://cursor.sh/features.png)

---

## Requirements

| Item | Details |
|------|---------|
| **OS** | macOS 10.15+, Windows 10/11, Linux (Ubuntu 20.04+) |
| **Disk** | ~300 MB |
| **Internet** | Required (AI features call remote APIs) |
| **Account** | Free Cursor account required; Pro plan ($20/mo) for unlimited usage |
| **API Keys** | Optional — you can bring your own OpenAI / Anthropic key |

### Pricing

- **Hobby (Free)**: 2,000 completions / month, 50 slow premium requests
- **Pro ($20/mo)**: Unlimited completions, 500 fast premium requests / month
- **Business ($40/user/mo)**: Team features, centralized billing, privacy mode

---

## Installation

1. Download the installer from [cursor.sh](https://cursor.sh)
2. Run the installer for your platform (`.dmg`, `.exe`, or `.AppImage`)
3. Sign in or create a free Cursor account
4. Import your VS Code settings / extensions with one click (optional)

---

## Key Features

### Tab Completion
Cursor's signature feature — it predicts and auto-completes entire lines or blocks of code based on context, not just the current line.

### Cmd+K / Ctrl+K — Inline Edit
Select any code block and press `Cmd+K` (macOS) or `Ctrl+K` (Windows/Linux) to describe a change in plain English. Cursor rewrites the selection in-place.

### Chat (Cmd+L)
Open a side-panel AI chat that has full awareness of your codebase. Ask questions like "How does the authentication flow work?" and Cursor will answer with references to the relevant files.

### Composer (Multi-file editing)
The Composer feature lets you describe a larger task and Cursor will generate or modify multiple files at once. Ideal for scaffolding features, refactoring across modules, or writing tests.

### Codebase Indexing
Cursor indexes your entire project so the AI has context beyond just the open file — it can answer questions about the whole repo and make edits that respect existing patterns.

---

## Best Use Cases

| Use Case | Why Cursor Excels |
|----------|-------------------|
| **Greenfield development** | Scaffold entire features with Composer |
| **Refactoring legacy code** | Multi-file edits with full codebase context |
| **Code review / understanding** | Chat to understand unfamiliar codebases quickly |
| **Writing tests** | Generate comprehensive test suites from existing code |
| **Debugging** | Explain errors and suggest fixes inline |
| **Documentation** | Generate JSDoc / docstrings across a file or project |

---

## Tips & Best Practices

- **Use `.cursorrules`** — Add a `.cursorrules` file at the project root to give Cursor persistent instructions (e.g., preferred coding style, framework conventions).
- **Pin key files** — In chat, use `@filename` to explicitly reference files so the AI focuses on the right context.
- **Composer for big tasks** — Use Composer (not inline edit) when you need changes across multiple files.
- **Privacy Mode** — Enable "Privacy Mode" in Settings if you don't want your code sent to Cursor's servers for model training.

---

## Links

- 🌐 **Official Website**: [https://cursor.sh](https://cursor.sh)
- 📖 **Documentation**: [https://docs.cursor.sh](https://docs.cursor.sh)
- 🐦 **Twitter / X**: [https://twitter.com/cursor_ai](https://twitter.com/cursor_ai)
- 💬 **Community Forum**: [https://forum.cursor.sh](https://forum.cursor.sh)
- 📦 **Changelog**: [https://cursor.sh/changelog](https://cursor.sh/changelog)

