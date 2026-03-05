# Claude Code

## Introduction

**Claude Code** is Anthropic's official **terminal-based agentic coding tool**. Unlike IDE plugins, Claude Code runs entirely in your terminal as a CLI agent — it can read files, write code, execute commands, run tests, and iterate until a task is complete, all from your command line.

Powered by **Claude Sonnet** and **Claude Opus**, Claude Code is designed for developers who prefer staying in the terminal and want an AI that can autonomously handle large, multi-step coding tasks with minimal hand-holding.

> Claude Code 是 Anthropic 官方推出的终端 AI 编程助手，直接在命令行中运行，能够自主完成复杂的多步骤编程任务。

---

## Requirements

| Item | Details |
|------|---------|
| **OS** | macOS, Linux, Windows (via WSL2) |
| **Node.js** | v18 or later |
| **Package manager** | npm, yarn, or pnpm |
| **API Key** | Anthropic API key (from [console.anthropic.com](https://console.anthropic.com)) |
| **Cost** | Pay-per-use via Anthropic API (no flat subscription) |

### Estimated API Cost
Claude Code is token-heavy by nature (it reads your files for context). Typical sessions cost **$0.05 – $5.00** depending on codebase size and task complexity. Use `claude --model claude-3-5-haiku-latest` for cheaper iterations.

---

## Installation

```bash
# Install globally via npm
npm install -g @anthropic-ai/claude-code

# Verify installation
claude --version

# Set your API key
export ANTHROPIC_API_KEY="sk-ant-..."
# Or add to your shell profile (~/.zshrc, ~/.bashrc)

# Start an interactive session
claude
```

---

## Key Features

### Agentic Task Execution
Claude Code operates as a fully autonomous agent: give it a goal in plain English, and it will plan, implement, test, and iterate without step-by-step prompting.

```bash
claude "Refactor the authentication module to use JWT instead of session cookies"
```

### File Read / Write / Execute
Claude Code can:
- **Read** any file in your project for context
- **Write** new files or modify existing ones
- **Run** shell commands, test suites, linters, and build tools
- **Browse** the web (when given permission) to look up documentation

### Interactive & Non-interactive Modes
- `claude` — starts an interactive REPL session
- `claude "task description"` — executes a single task and exits
- `claude --print` — outputs the result without executing side effects (dry run)

### Permissions System
Before performing destructive operations (deleting files, running scripts), Claude Code asks for explicit permission. You can pre-approve categories of actions.

### Context Window Management
Claude Code automatically manages what files to include in context based on relevance, keeping API costs down while maintaining accuracy.

### Git Integration
Works seamlessly with Git — can commit changes, create branches, and write meaningful commit messages.

---

## Best Use Cases

| Use Case | Why Claude Code Excels |
|----------|------------------------|
| **Large refactors** | Autonomously updates dozens of files in one session |
| **Greenfield scaffolding** | Build an entire project structure from a description |
| **Bug fixing** | Reproduce, diagnose, and fix bugs end-to-end |
| **Test generation** | Write comprehensive test suites for existing code |
| **CI/CD scripting** | Author or debug complex shell scripts and pipelines |
| **Code migration** | Migrate APIs, frameworks, or language versions across a codebase |
| **Terminal-centric workflows** | Developers who live in the terminal without needing an IDE |

---

## Tips & Best Practices

- **Use `CLAUDE.md`** — Create a `CLAUDE.md` file at your project root with project-specific instructions (tech stack, conventions, do's and don'ts). Claude Code reads this automatically.
- **Start with a small scope** — For first use, try a well-defined task on a single file before unleashing it on the whole codebase.
- **Review diffs before accepting** — Use `git diff` to inspect every change before committing.
- **Use `--model` flag** — Switch between Sonnet (fast/cheap) and Opus (powerful/expensive) depending on task complexity.
- **Pipe into scripts** — `claude --print "..." ` can be piped into other shell tools for automation.

---

## Links

- 🌐 **Official Page**: [https://www.anthropic.com/claude-code](https://www.anthropic.com/claude-code)
- 📖 **Documentation**: [https://docs.anthropic.com/en/docs/claude-code](https://docs.anthropic.com/en/docs/claude-code)
- 📦 **npm Package**: [https://www.npmjs.com/package/@anthropic-ai/claude-code](https://www.npmjs.com/package/@anthropic-ai/claude-code)
- 🔑 **Get API Key**: [https://console.anthropic.com](https://console.anthropic.com)
- 💬 **Discord Community**: [https://discord.gg/anthropic](https://discord.gg/anthropic)
