# Amazon Kiro

## Introduction

**Kiro** is an AI-powered code editor developed by **Amazon / AWS**, currently in **Preview** (invitation required). It is built on the premise of *spec-driven development* — rather than jumping straight to code generation, Kiro helps you define requirements, system design, and task breakdowns first, then uses those specs to generate consistent, well-reasoned code.

Under the hood Kiro runs AWS-hosted **Claude** models (currently supports Claude Sonnet 4.0), making it a strong choice for teams already working in the AWS ecosystem.

> Kiro 是来自 Amazon 的 AI 代码编辑器，目前还在 Preview 阶段需要申请才可以获得使用权限，据说使用的是 AWS 的 self-hosted Claude 模型，可以选择 Claude Sonnet 4.0.

![Kiro screenshot](https://kiro.dev/images/og-image.png)

---

## Requirements

| Item | Details |
|------|---------|
| **OS** | macOS, Windows 10/11, Linux |
| **Access** | Preview access required — sign up at [kiro.dev](https://kiro.dev) |
| **Account** | AWS Builder ID or IAM Identity Center account |
| **Internet** | Required |
| **Cost** | Free during Preview period |

---

## Installation

1. Request access at [https://kiro.dev](https://kiro.dev) and wait for the invitation email.
2. Download the Kiro installer from the invite link (`.dmg` / `.exe` / `.deb`).
3. Sign in with your **AWS Builder ID** or **IAM Identity Center** credentials.
4. Open or create a project — Kiro will prompt you to initialize a *spec*.

---

## Key Features

### Spec-Driven Development
Kiro's standout approach: before writing code it helps you author three artifacts:
1. **Requirements** — user stories and acceptance criteria
2. **Design** — architecture, data models, API contracts
3. **Tasks** — a prioritized breakdown of implementation work

The generated code stays aligned with these specs, which reduces drift as the project grows.

### AI Chat & Inline Edits
Like other AI IDEs, Kiro provides a chat panel and inline code generation. The difference is that chat responses are grounded in your project's spec documents.

### Agent-Based Automation
Kiro can autonomously execute tasks from the task list — creating files, writing implementations, and running commands — while keeping a log of every change for review.

### Hooks
*Hooks* are automated workflows triggered by file save events (e.g., "when I save a component file, auto-generate updated tests"). This keeps generated artifacts in sync without manual prompting.

### MCP Support
Kiro supports the **Model Context Protocol (MCP)**, allowing you to extend its context with external data sources (databases, APIs, documentation sites).

---

## Best Use Cases

| Use Case | Why Kiro Excels |
|----------|-----------------|
| **New projects / greenfield** | Spec-first workflow keeps architecture clean from day one |
| **AWS / cloud-native apps** | Native AWS integration and IAM-based auth |
| **Team alignment** | Specs serve as living documentation readable by both devs and stakeholders |
| **Large feature development** | Autonomous task execution with full audit trail |
| **Enterprises with compliance needs** | Self-hosted models on AWS, no data leaves your control plane |

---

## Tips & Best Practices

- **Invest time in the spec** — The quality of generated code directly correlates with the clarity of your requirements and design docs.
- **Review task breakdowns** — Before running autonomous agent tasks, review and adjust the task list to avoid unwanted changes.
- **Use Hooks for test generation** — Configure a hook to regenerate unit tests whenever implementation files are saved.
- **MCP for codebase context** — Connect Kiro to your internal docs or APIs via MCP for richer context-aware suggestions.

---

## Links

- 🌐 **Official Website**: [https://kiro.dev](https://kiro.dev)
- 📖 **Documentation**: [https://kiro.dev/docs](https://kiro.dev/docs)
- 📝 **Blog Announcement**: [https://aws.amazon.com/blogs/devops/introducing-kiro/](https://aws.amazon.com/blogs/devops/introducing-kiro/)
- 🐦 **Twitter / X**: [https://twitter.com/kiro_dev](https://x.com/kiro_dev)

