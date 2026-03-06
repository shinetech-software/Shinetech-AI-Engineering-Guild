# Google Antigravity

## Introduction

**Antigravity** (also referred to as *Project IDX* or the newer *Firebase Studio*) is Google's AI-powered, browser-based development environment. It brings together Google's first-party AI models — primarily **Gemini** — and optionally **Claude** (via the Anthropic partnership) into a fully cloud-hosted IDE experience accessible from any browser, with no local installation required.

Antigravity / Firebase Studio is designed for full-stack web and mobile development, with built-in support for Android/iOS emulators, Firebase services, and one-click deployment to Google Cloud.

> Antigravity 是来自 Google 的 AI 代码编辑器，提供 Claude 和 Gemini 模型。

![Antigravity / Firebase Studio](https://firebase.google.com/images/brand-guidelines/logo-standard.png)

---

## Requirements

| Item | Details |
|------|---------|
| **Browser** | Any modern browser (Chrome recommended) |
| **OS** | Any (fully browser-based, no local install) |
| **Account** | Google account required |
| **Internet** | Required — the IDE runs entirely in the cloud |
| **Cost** | Free tier available; usage limits apply |

---

## Getting Started

1. Visit [https://firebase.studio](https://firebase.studio) (or [https://idx.google.com](https://idx.google.com) for Project IDX).
2. Sign in with your **Google account**.
3. Create a new workspace by choosing a template (Next.js, Flutter, Angular, Python, etc.) or import a GitHub repository.
4. The workspace launches in your browser with a VS Code-based interface, a cloud-hosted terminal, and built-in AI assistance.

---

## Key Features

### Browser-Based IDE
No installation needed. Your entire development environment — editor, terminal, runtime, and preview — runs in Google's cloud. You can pick up work from any device.

### Gemini AI Integration
Gemini is available for:
- Chat-based coding assistance
- Inline code suggestions
- Code explanation and documentation generation
- Generating boilerplate and components

### Multi-Model Support
Choose between **Gemini** (Google) and optionally **Claude** (Anthropic) for different tasks or personal preference.

### Built-in Emulators
For mobile development, Antigravity/IDX ships with Android and iOS (web preview) emulators directly in the browser — no Xcode or Android Studio required.

### Firebase & Google Cloud Integration
One-click integration with Firebase (Firestore, Auth, Hosting) and easy deployment to Google Cloud Run or App Engine.

### Dev Container Support
Workspaces are backed by **Nix**-based dev containers, ensuring reproducible environments defined in a `.idx/dev.nix` file — sharable across the team.

---

## Best Use Cases

| Use Case | Why Antigravity Excels |
|----------|------------------------|
| **Quick prototyping** | Start coding in seconds — no environment setup |
| **Flutter / mobile development** | Built-in Android emulator and Flutter toolchain |
| **Firebase-backed apps** | Tight integration with Firebase services |
| **Chromebook / low-powered devices** | Everything runs in the cloud, not locally |
| **Teaching & demos** | Share a workspace URL for live collaboration |
| **Google Cloud deployments** | One-click deploy to Cloud Run, App Engine |

---

## Tips & Best Practices

- **Use `.idx/dev.nix`** to pin exact tool versions and share reproducible environments with teammates.
- **Enable Gemini suggestions** via the Gemini panel in the sidebar for chat-based assistance.
- **Import from GitHub** to quickly spin up an existing project without any local setup.
- **Use the built-in emulator** for mobile previews instead of installing a full local SDK.

---

## Links

- 🌐 **Firebase Studio**: [https://firebase.studio](https://firebase.studio)
- 🌐 **Project IDX**: [https://idx.google.com](https://idx.google.com)
- 📖 **Documentation**: [https://firebase.google.com/docs/studio](https://firebase.google.com/docs/studio)
- 📝 **Blog**: [https://firebase.blog](https://firebase.blog)
- 🐦 **Twitter / X**: [https://twitter.com/googledevs](https://twitter.com/googledevs)

