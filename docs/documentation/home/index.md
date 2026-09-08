# Instant Python

<div align="center">
    <b>Fast, easy and reliable project generator for your Python projects.</b>
</div>

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
</ul>

</td></tr></table></div>

## Quick Start

Once [installed](../getting_started/installation.md), generating a project takes two commands:

```bash
ipy config   # answer a few questions through an interactive wizard to create your ipy.yml configuration file
ipy init     # generate the project from that configuration file
```

- `ipy config` asks you about your project (name, Python version, project manager, template, dependencies, and more) and writes an `ipy.yml` configuration file in the current directory.
- `ipy init` reads that `ipy.yml` file and generates your new project.

See the [First Steps](../getting_started/first_steps.md) guide for a full walkthrough.

## Navigation Guide

This section provides a high-level overview of the `instant-python` documentation
so can quickly find what you need.

### For Users

- [Installation]: begin by learning how to install `instant-python`.
- [First Steps]: get started with the basic features of `instant-python`.
- [Privacy & Metrics]: learn about the anonymous usage data we collect and how to opt out.
- [Advanced Usage and Customization]: explore advanced features and customization options.

[Installation]: ../getting_started/installation.md
[First Steps]: ../getting_started/first_steps.md
[Privacy & Metrics]: ../getting_started/privacy_and_metrics.md
[Advanced Usage and Customization]: ../guide/index.md

### For Developers

- [Contributing]: learn how to contribute to `instant-python` development.
- [Releases]: understand our release process and versioning.
- [Security]: understand our security policies and reporting procedures.

[Contributing]: ../development/contributing.md
[Releases]: ../development/releases.md
[Security]: ../development/security.md

### Need help?

-   Join a discussion 💬 on [GitHub Discussions]
-   [Raise an issue][GitHub Issues] on GitHub

[GitHub Discussions]: https://github.com/dimanu-py/instant-python/discussions
[GitHub Issues]: https://github.com/dimanu-py/instant-python/issues

[//]: # (### Do Not Track)

[//]: # ()
[//]: # (In order to get better insights about the usage of the library, we collect anonymous usage data. The only)

[//]: # (data we collect is the commands you run. No personal data is collected as part of this request.)

[//]: # ()
[//]: # (You can disable this feature by setting the environment variable `INSTANT_PYTHON_NO_TRACK` to `1` or )

[//]: # (passing the `--no-track` option to any command.)
