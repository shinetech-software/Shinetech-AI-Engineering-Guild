# Claude Code — Agent Teams Setup Guide

> **Audience:** Beginners and intermediate users who want to orchestrate multiple Claude Code agents working in parallel on complex tasks.

---

## Table of Contents

1. [What Are Claude Code Agent Teams?](#1-what-are-claude-code-agent-teams)
2. [How Agent Teams Work](#2-how-agent-teams-work)
3. [Prerequisites](#3-prerequisites)
4. [Installation & Authentication](#4-installation--authentication)
5. [Key Concepts](#5-key-concepts)
6. [Setting Up Your First Agent Team](#6-setting-up-your-first-agent-team)
7. [Using CLAUDE.md to Guide Agents](#7-using-claudemd-to-guide-agents)
8. [Running Agent Teams in Practice](#8-running-agent-teams-in-practice)
9. [Common Use Cases](#9-common-use-cases)
10. [Best Practices](#10-best-practices)
11. [Troubleshooting](#11-troubleshooting)
12. [Further Reading](#12-further-reading)

---

## 1. What Are Claude Code Agent Teams?

Claude Code **Agent Teams** (also called *multi-agent* or *subagent* mode) let you run multiple Claude Code instances simultaneously, each tackling a different part of a larger problem. Instead of one agent working through a huge task step-by-step, you can split the work, run agents in parallel, and finish much faster.

Think of it like a software development team:

| Role | Claude Equivalent |
|------|-------------------|
| Tech Lead / Project Manager | **Orchestrator agent** – breaks down the task and coordinates work |
| Individual Developer | **Subagent** – executes a specific, focused subtask |

A typical workflow:
```
User Prompt
    └── Orchestrator (Claude Code)
            ├── Subagent A → writes unit tests
            ├── Subagent B → implements the feature
            └── Subagent C → updates documentation
```

---

## 2. How Agent Teams Work

Claude Code's multi-agent system relies on a few core ideas:

- **Orchestrator spawns subagents** – The orchestrator uses the `Task` tool to launch Claude subagents with a specific prompt and context.
- **Subagents run in isolated contexts** – Each subagent gets its own conversation window and set of tools, so they don't interfere with each other.
- **Agents communicate through the filesystem** – Subagents read and write files; the orchestrator collects results by reading those files.
- **Parallel execution** – Multiple subagents can run at the same time, drastically reducing total time for large tasks.

---

## 3. Prerequisites

Before you start, make sure you have the following:

| Requirement | Notes |
|---|---|
| **Node.js 18+** | Required to run Claude Code. Install from [nodejs.org](https://nodejs.org). |
| **npm 8+** | Comes bundled with Node.js. |
| **Anthropic API key** | Sign up at [console.anthropic.com](https://console.anthropic.com) and create an API key. |
| **Claude Code CLI** | Installed via npm (see next section). |

To check your Node.js and npm versions:
```bash
node --version   # should print v18.x.x or higher
npm --version    # should print 8.x.x or higher
```

---

## 4. Installation & Authentication

### Step 1 — Install Claude Code

```bash
npm install -g @anthropic-ai/claude-code
```

Verify the installation:
```bash
claude --version
```

### Step 2 — Authenticate

Claude Code needs your Anthropic API key to work. Run:

```bash
claude
```

On first launch, the CLI will guide you through authentication. You will be asked to either:
- Log in via browser (OAuth), **or**
- Provide your `ANTHROPIC_API_KEY` environment variable directly.

To set the API key in your shell profile (recommended for teams):

```bash
# Add to ~/.bashrc, ~/.zshrc, or your shell profile
export ANTHROPIC_API_KEY="sk-ant-..."
```

Then reload your shell:
```bash
source ~/.zshrc   # or source ~/.bashrc
```

### Step 3 — Verify setup

```bash
claude --help
```

You should see the Claude Code help menu. You are ready to go! ✅

---

## 5. Key Concepts

Before jumping into agent teams, it is helpful to understand these terms:

### Orchestrator
The **top-level** Claude Code agent. It receives your high-level goal, decides how to break it into subtasks, and uses the `Task` tool to delegate work to subagents. The orchestrator is the agent you interact with directly.

### Subagent
A **child** Claude Code instance launched by the orchestrator. Each subagent is given a focused prompt and has access to its own set of tools (shell, file read/write, etc.). Subagents report results back to the orchestrator.

### Task Tool
A built-in Claude Code tool that allows the orchestrator to **spawn a new subagent**. When using agent teams, you will often see prompts that say something like:  
> *"Launch three agents in parallel: one for tests, one for implementation, one for docs."*

### CLAUDE.md
A special Markdown file you can place in your project root (or any subdirectory) to give persistent instructions and context to Claude Code agents. Think of it as a **README for Claude**. Agents read this file automatically at the start of each session.

### Permissions & Safety
Claude Code asks for your permission before performing sensitive actions (writing files, running shell commands, etc.). In agent team mode, you can choose to **grant blanket permissions** for the session so agents can work uninterrupted — but use this carefully.

---

## 6. Setting Up Your First Agent Team

Let us walk through a practical example: you have a new feature request and want three agents to work in parallel — one writing tests, one implementing the feature, and one updating the README.

### Step 1 — Navigate to your project

```bash
cd /path/to/your/project
```

### Step 2 — Create a CLAUDE.md file (optional but recommended)

```bash
touch CLAUDE.md
```

Add your project context (see [Section 7](#7-using-claudemd-to-guide-agents) for details).

### Step 3 — Start Claude Code

```bash
claude
```

### Step 4 — Give the orchestrator a multi-agent prompt

Once the Claude Code prompt is open, describe your goal and explicitly ask for parallel agents:

```
I need to add a user login feature to this project.

Please spawn three subagents to work in parallel:
1. Agent 1: Write unit tests for the login feature in tests/test_login.py
2. Agent 2: Implement the login feature in src/auth.py
3. Agent 3: Update README.md with login setup instructions

Each agent should work independently. Once all three are done, summarize what was completed.
```

Claude Code will begin orchestrating the agents. You will see output like:

```
Launching subagent 1: Writing unit tests...
Launching subagent 2: Implementing login feature...
Launching subagent 3: Updating README...
[Subagent 1 complete] ✅
[Subagent 2 complete] ✅
[Subagent 3 complete] ✅
Summary: All three tasks completed successfully.
```

### Step 5 — Review the results

Check the files that were modified by the subagents:

```bash
git diff --stat
```

---

## 7. Using CLAUDE.md to Guide Agents

A `CLAUDE.md` file is one of the most powerful ways to customize agent behavior for your project. Place it in your project root and Claude Code agents will read it automatically.

### Recommended CLAUDE.md structure

```markdown
# Project Overview
Brief description of what this project does.

# Tech Stack
- Language: Python 3.11
- Framework: FastAPI
- Database: PostgreSQL
- Test runner: pytest

# Coding Conventions
- Use type hints on all functions.
- Write docstrings for public methods.
- Follow PEP 8 style guidelines.

# Project Structure
src/          # Application source code
tests/        # Unit and integration tests
docs/         # Documentation

# Common Commands
- Run tests: `pytest tests/`
- Start server: `uvicorn src.main:app --reload`
- Lint: `ruff check src/`

# Agent Instructions
- Always run tests after making code changes.
- Never modify files in the `config/` directory without explicit user approval.
- Prefer small, focused commits.
```

### CLAUDE.md in subdirectories

You can also place `CLAUDE.md` files in subdirectories. Agents pick up context from the most relevant directory first. This is useful for monorepos where each package has its own conventions.

```
my-monorepo/
├── CLAUDE.md          ← Project-wide instructions
├── backend/
│   └── CLAUDE.md      ← Backend-specific instructions
└── frontend/
    └── CLAUDE.md      ← Frontend-specific instructions
```

---

## 8. Running Agent Teams in Practice

### Launching with extended thinking

For very complex orchestration tasks, enable extended thinking to give the orchestrator more time to plan:

```bash
claude --thinking
```

Then describe your multi-agent task as usual.

### Granting permissions for uninterrupted runs

In agent team mode, agents may need to perform many file operations. To avoid repeated permission prompts, you can run:

```bash
claude --dangerously-skip-permissions
```

> ⚠️ **Warning:** Only use `--dangerously-skip-permissions` in trusted environments (e.g., CI/CD pipelines or local machines you control). This flag allows agents to execute shell commands, write files, and make changes without asking for approval each time.

### Running in headless / CI mode

For automated pipelines, use the `--print` flag to run non-interactively:

```bash
claude --print "Run the full test suite and fix any failing tests. Use multiple agents if needed."
```

Combine with `--output-format json` to capture structured output:

```bash
claude --print "Analyse the codebase and identify dead code." --output-format json
```

### Using the `--sub-agent` flag (advanced)

When you need fine-grained control, you can manually launch individual agents from separate terminal sessions:

**Terminal 1 — Orchestrator:**
```bash
claude
```

**Terminal 2 — Dedicated subagent:**
```bash
claude --sub-agent "Refactor all async functions in src/api/ to use proper error handling."
```

Each terminal runs an independent agent. You coordinate between them manually by sharing file paths or commit SHAs.

---

## 9. Common Use Cases

| Use Case | Example Prompt |
|---|---|
| **Parallel feature development** | "Spawn 3 agents: one for the backend endpoint, one for the frontend component, one for the API tests." |
| **Large codebase refactoring** | "Split the refactoring of `src/` across 4 agents, each handling a different module." |
| **Automated code review** | "Use two agents: one to review security issues, one to review performance issues." |
| **Documentation generation** | "Launch agents to document each module in `src/` simultaneously." |
| **Test suite generation** | "Create unit tests for every file in `src/services/` using parallel agents." |
| **Dependency upgrades** | "Use multiple agents to upgrade dependencies and fix any breaking changes across packages." |
| **Multi-language projects** | "Spawn a Python agent and a TypeScript agent to work on their respective parts simultaneously." |

---

## 10. Best Practices

### ✅ Do

- **Write clear, focused prompts per subagent.** The more specific you are, the better the output. Include file paths, function names, and acceptance criteria.
- **Use `CLAUDE.md` for persistent context.** Don't repeat project conventions in every prompt — put them in `CLAUDE.md`.
- **Review agent output before committing.** Always run `git diff` and your test suite before merging agent-generated changes.
- **Start with small tasks.** If you are new to agent teams, begin with 2–3 subagents on a small feature before scaling up.
- **Use version control as a safety net.** Make sure your working directory is clean (`git status`) before launching agents so you can easily revert if needed.

### ❌ Avoid

- **Giving agents overlapping responsibilities.** If two agents edit the same file concurrently, you risk merge conflicts. Scope each agent to distinct files or modules.
- **Using `--dangerously-skip-permissions` on production systems.** Always sandbox agent runs on local or CI environments.
- **Expecting agents to share memory.** Each subagent has an independent context. If agents need shared state, use the filesystem (write a summary file that others can read).
- **Ignoring agent output.** Even successful runs should be reviewed — agents can make plausible-sounding but incorrect changes.

---

## 11. Troubleshooting

### Agent doesn't start

**Symptom:** Running `claude` shows an authentication error.  
**Fix:** Make sure your `ANTHROPIC_API_KEY` environment variable is set:
```bash
echo $ANTHROPIC_API_KEY   # should print your key
```
If empty, re-export it:
```bash
export ANTHROPIC_API_KEY="sk-ant-..."
```

---

### Agents keep asking for permission

**Symptom:** Every file operation triggers a permission prompt, slowing down the run.  
**Fix:** Use `--dangerously-skip-permissions` (only in safe environments):
```bash
claude --dangerously-skip-permissions
```
Alternatively, add a permissions rule to your `CLAUDE.md`:
```markdown
# Permissions
You are allowed to read, write, and execute files in this project directory without asking for confirmation.
```

---

### Subagents produce conflicting changes

**Symptom:** Multiple agents edited the same file; git shows conflicts.  
**Fix:**
1. Run `git diff` to see what changed.
2. Manually resolve conflicts or ask a single agent to merge: `claude "Review the conflicting changes in src/auth.py and produce a clean, combined version."`
3. In future runs, assign non-overlapping files/modules to each agent.

---

### Agent gets stuck in a loop

**Symptom:** An agent keeps retrying the same action with no progress.  
**Fix:** Press `Ctrl+C` to stop the agent, then re-run with a more specific prompt that tells the agent exactly what to do when it hits that step.

---

### API rate limit errors

**Symptom:** You see `429 Too Many Requests` errors.  
**Fix:**
- Reduce the number of parallel agents (start with 2 instead of 5).
- Add a short delay between agent launches.
- Upgrade your Anthropic plan for higher rate limits at [console.anthropic.com](https://console.anthropic.com).

---

## 12. Further Reading

- [Claude Code Official Documentation](https://docs.anthropic.com/en/docs/claude-code/overview)
- [Claude Code Multi-Agent Guide](https://docs.anthropic.com/en/docs/claude-code/sub-agents)
- [Building Effective Agents (Anthropic)](https://www.anthropic.com/research/building-effective-agents)
- [Claude Code GitHub Repository](https://github.com/anthropics/claude-code)
- [Anthropic API Console](https://console.anthropic.com)

---

*Last updated: March 2026 | Maintained by Shinetech AI Engineering Guild*
