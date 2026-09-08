<div align="center">
  <h1>⚡️ Instant Boilerplate for Python Projects ⚡️</h1>
  <strong>Fast, easy and reliable project generator for your Python projects.</strong>
</div>

<p align="center">
  <a href="https://dimanu-py.github.io/instant-python/getting_started/installation/">Getting Started</a>&nbsp;&nbsp;•&nbsp;
  <a href="https://dimanu-py.github.io/instant-python/guide/">Usage</a>&nbsp;&nbsp;•&nbsp;
  <a href="https://dimanu-py.github.io/instant-python/guide/custom_projects/">How to: Custom Projects</a>&nbsp;&nbsp;•&nbsp;
  <a href="https://dimanu-py.github.io/instant-python/guide/default_features/#ai-agents">AI Agent Harness</a>
</p>

<div align="center"><table><tr><td>
<b>Instant Python</b> replaces extensive manual setup with a simple command to get started quickly. Its motivation is to emulate
commands like `ng new` or `create-react-app`, but for Python projects.

<br>

<b>Why use Instant Python?</b> Generating your Python project with Instant Python lets you:

<ul style="list-style-type: none">
  <li>⏱️ Slash folder & config setup time to seconds</li>
  <li>🐍 Instantly install & switch between any Python version</li>
  <li>🔧 Effortlessly configure your favorite project manager</li>
  <li>📁 Kickstart with ready-made or fully custom project structures</li>
  <li>🔄 Initialize a Git repo in just a few clicks</li>
  <li>📦 Auto-install all your go-to dependencies</li>
  <li>🚀 Ship with production-ready boilerplates out of the box</li>
  <li>🤖 Include a complete AI agent setup for assisted development</li>
</ul>

</td></tr></table></div>

## 🚀 Quick Start

Once [installed](https://dimanu-py.github.io/instant-python/getting_started/installation/), generating a project takes two commands:

```bash
ipy config   # answer a few questions through an interactive wizard to create your ipy.yml configuration file
ipy init     # generate the project from that configuration file
```

- `ipy config` asks you about your project (name, Python version, project manager, template, dependencies, and more) and writes an `ipy.yml` configuration file in the current directory.
- `ipy init` reads that `ipy.yml` file and generates your new project.

See the [First Steps](https://dimanu-py.github.io/instant-python/getting_started/first_steps/) guide for a full walkthrough.

## ✨ NEW ✨ Create Fully Customized Projects

Take full control of your project generation! With **custom templates**, you can:

- 🎨 Design your own project structure that matches your architectural patterns (like Hexagonal Architecture)
- 📝 Create reusable file templates with your standardized code and best practices
- 🔄 Enforce consistency across all your Python projects
- ⚡ Eliminate repetitive boilerplate and setup tasks

Whether you have a standardized project structure you always use or specific architectural patterns you want to enforce, 
custom templates let you generate projects exactly the way you want them. 
[Learn how to create your first custom template](https://dimanu-py.github.io/instant-python/guide/custom_projects/) and level up your project generation workflow!

## 🤖 AI Agents Setup

Generate projects with a pre-configured AI agent environment to assist your development workflow. When you include the
`ai_agents` built-in feature, your project comes with:

- **`AGENTS.md`** — Project rules and guidelines that configure AI agents to follow your coding standards
- **Skills** — Reusable instruction sets for common tasks: code review, refactoring, story splitting, test analysis, and more
- **Commands** — On-demand workflows for recurring operations: committing changes, running security reviews, analyzing technical debt
- **Architecture Decision Records (ADR)** — Templates to document and track technical decisions
- **Design Docs** — Templates to capture feature requirements and implementation plans

All generated under `docs/` and `.agents/` directories, ready to use with any AI coding assistant that supports agent configuration.
[See all available skills and commands](https://dimanu-py.github.io/instant-python/guide/default_features/#ai-agents).

## Navigation Guide

This section provides a high-level overview of the `instant-python` documentation
so can quickly find what you need.

### For Users

- [Installation]: begin by learning how to install `instant-python`.
- [First Steps]: get started with the basic features of `instant-python`.
- [Privacy & Metrics]: learn about the anonymous usage data we collect and how to opt out.
- [Advanced Usage and Customization]: explore advanced features and customization options.

[Installation]: https://dimanu-py.github.io/instant-python/getting_started/installation/
[First Steps]: https://dimanu-py.github.io/instant-python/getting_started/first_steps/
[Privacy & Metrics]: https://dimanu-py.github.io/instant-python/getting_started/privacy_and_metrics/
[Advanced Usage and Customization]: https://dimanu-py.github.io/instant-python/guide/

### For Developers

- [Contributing]: learn how to contribute to `instant-python` development.
- [Releases]: understand our release process and versioning.
- [Security]: understand our security policies and reporting procedures.

[Contributing]: https://dimanu-py.github.io/instant-python/development/contributing/
[Releases]: https://dimanu-py.github.io/instant-python/development/releases/
[Security]: https://dimanu-py.github.io/instant-python/development/security/

### Need help?

-   Join a discussion 💬 on [GitHub Discussions]
-   [Raise an issue][GitHub Issues] on GitHub

[GitHub Discussions]: https://github.com/dimanu-py/instant-python/discussions
[GitHub Issues]: https://github.com/dimanu-py/instant-python/issues

## 🔒 Privacy & Usage Metrics

To improve `instant-python` and provide a better experience, we collect **anonymous usage metrics**. 
No personal or sensitive information is collected.

**What we collect:**
- Command executed and IPY version
- Operating system type
- Python version, dependency manager, and template choices
- Error types (when commands fail)

**What we DON'T collect:**
- No file paths, project names, or code content
- No personal information or IP addresses

**How to opt out:**
Set the environment variable `IPY_METRICS_ENABLE=false`

For complete details, see our [Privacy & Metrics documentation](https://dimanu-py.github.io/instant-python/getting_started/privacy_and_metrics/).

