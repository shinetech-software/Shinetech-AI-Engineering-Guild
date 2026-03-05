# OpenAI Codex CLI

## Introduction

**OpenAI Codex CLI** (also known as **Codex** or `codex`) is OpenAI's open-source, terminal-based AI coding agent. It runs directly in your terminal and uses OpenAI's models (primarily **o4-mini**, **o3**, and **GPT-4.1**) to autonomously read files, write code, run commands, and complete multi-step programming tasks — all from the command line.

Codex CLI is the terminal-native counterpart to ChatGPT's coding capabilities, designed for developers who want full control and scriptability.

> GPT Codex 是 OpenAI 推出的开源终端 AI 编程助手，可以在命令行中自主完成复杂编程任务。

---

## Requirements

| Item | Details |
|------|---------|
| **OS** | macOS, Linux, Windows (via WSL2) |
| **Node.js** | v22 or later |
| **Package manager** | npm |
| **API Key** | OpenAI API key (from [platform.openai.com](https://platform.openai.com)) |
| **Cost** | Pay-per-use via OpenAI API |

### Estimated API Cost
- **o4-mini** (default, recommended): Very cost-effective; most tasks cost a few cents
- **o3**: More powerful reasoning; higher cost per task

---

## Installation

```bash
# Install globally via npm
npm install -g @openai/codex

# Verify installation
codex --version

# Set your API key (required)
export OPENAI_API_KEY="sk-..."
# Or add to ~/.zshrc / ~/.bashrc

# Run an interactive session
codex

# Run a single task
codex "Add input validation to the login form"
```

---

## Key Features

### Agentic Code Execution
Codex operates as a full coding agent. Describe what you want — it reads your codebase, plans changes, writes code, executes tests, and iterates until the task is done.

```bash
codex "Write unit tests for all functions in src/utils.ts"
codex "Fix the flaky tests in the payment module"
codex "Migrate this Express app from CommonJS to ESM"
```

### Three Approval Modes
Codex CLI offers three levels of autonomy:

| Mode | Description |
|------|-------------|
| `suggest` (default) | Shows proposed changes; you approve each step |
| `auto-edit` | Reads and writes files automatically; asks before running commands |
| `full-auto` | Runs everything autonomously in a sandbox |

```bash
codex --approval-mode full-auto "Set up the CI workflow"
```

### Sandboxed Execution
On macOS, Codex runs commands in Apple Sandbox. On Linux, it uses Docker (if available). This isolates side effects and prevents runaway changes.

### Multimodal Input
Pass screenshots or images directly to Codex:
```bash
codex "Fix the layout so it matches this design" --image design-mockup.png
```

### Git-Aware
Codex reads your git history for context, creates branches, stages changes, and writes commit messages.

### Open Source
Codex CLI is fully open source under the Apache 2.0 license, meaning you can inspect, fork, and extend it.

---

## Best Use Cases

| Use Case | Why Codex CLI Excels |
|----------|----------------------|
| **Terminal-first workflows** | Zero context-switching — stay in your terminal |
| **Automated PR automation** | Run in CI to auto-fix linting errors or test failures |
| **Scripting & DevOps** | Write and debug shell scripts, Dockerfiles, CI pipelines |
| **Large-scale refactors** | Autonomous multi-file edits with full test execution |
| **Greenfield projects** | Scaffold an entire app from a single description |
| **Learning a new codebase** | Ask Codex to explain the architecture and walk through the code |

---

## Tips & Best Practices

- **Start with `suggest` mode** — Get comfortable with what Codex proposes before granting higher autonomy.
- **Use `full-auto` in sandboxes** — Great for CI environments where you want fully autonomous operation.
- **Create a `AGENTS.md`** — Add a `AGENTS.md` (or `CODEX.md`) file at your project root with instructions, conventions, and constraints.
- **Combine with `--image`** — For UI tasks, pass a screenshot so Codex can match visual designs.
- **Review with `git diff`** — Always review changes with git before committing to main.

---

## Links

- 🌐 **Official Announcement**: [https://openai.com/index/openai-codex-cli/](https://openai.com/index/openai-codex-cli/)
- 📦 **GitHub Repository**: [https://github.com/openai/codex](https://github.com/openai/codex)
- 📖 **npm Package**: [https://www.npmjs.com/package/@openai/codex](https://www.npmjs.com/package/@openai/codex)
- 🔑 **Get API Key**: [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)
- 💬 **OpenAI Community Forum**: [https://community.openai.com](https://community.openai.com)
