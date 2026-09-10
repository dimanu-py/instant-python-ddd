# Privacy and Usage Metrics

!!! info "Anonymous Usage Data"
    To improve `instant-python` and provide a better experience to all users, we collect **anonymous usage metrics**.
    No personal or sensitive information is collected. 

This page explains what data we collect, why we collect it, and how to disable it if you prefer.

## Why We Collect Metrics

We collect anonymous usage data to:

- 📊 **Understand which features are most used** - This helps us prioritize improvements and new features
- 🐛 **Identify common errors** - We can proactively fix bugs that users encounter
- 🚀 **Improve user experience** - By understanding how people use the tool, we can make it better
- 📈 **Make data-driven decisions** - We can focus our efforts on what matters most to the community

**Your privacy is important to us.** We only collect the minimum data necessary to achieve these goals,
and we never collect personal information like file paths, project names, or any code content.

## What Data We Collect

### On Successful Command Execution

When you successfully run an `ipy` command, we collect:

| Data Field | Description | Example                                      |
|------------|-------------|----------------------------------------------|
| `ipy_version` | The version of instant-python you're using | `0.20.0`                                     |
| `operating_system` | Your operating system | `Linux`, `Darwin`, `Windows`                 |
| `command` | The command you executed | `config`, `init`                             |
| `python_version` | The Python version you configured | `3.12`                                       |
| `dependency_manager` | The package manager you selected | `uv`                                  |
| `template` | The project template you chose | `domain_driven_design`, `clean_architecture` |
| `built_in_features` | List of features you enabled | `["makefile", "value_objects"]`               |

### On Command Errors

When a command fails with an error, we collect:

| Data Field | Description | Example |
|------------|-------------|---------|
| `ipy_version` | The version of instant-python you're using | `1.2.3` |
| `operating_system` | Your operating system | `Linux`, `Darwin`, `Windows` |
| `command` | The command that failed | `config`, `init` |
| `error_type` | The type of error that occurred | `FileNotFoundError`, `ValueError` |
| `error_message` | The error message | `Configuration file not found` |

## What We DON'T Collect

We want to be transparent about what we **do not** collect:

- ❌ **No personal information** - We don't collect your name, email, IP address, or any identifiable information
- ❌ **No file paths** - We never collect the paths where you create projects
- ❌ **No project names** - Your project names remain completely private
- ❌ **No code content** - We never collect any of your code or file contents
- ❌ **No environment variables** - Except for the opt-out flag, we don't read your environment

## How to Disable Metrics Collection

If you prefer not to send usage metrics, you can easily disable this feature.

Set the `IPY_METRICS_ENABLE` environment variable to `false` or `0`:

### Linux/macOS

- Bash/Zsh:
    
    For a single command run:

    ```bash
    IPY_METRICS_ENABLE=false ipy config
    ```
  
    Permanently in your shell profile (_~/.bashrc_, _~/.zshrc_, etc.)
    
    ```bash
    export IPY_METRICS_ENABLE=false
    ```

- Fish:

    For a single command run:

    ```bash
    env IPY_METRICS_ENABLE=false ipy config
    ```
    
    Permanently in your shell profile (_~/.config/fish/config.fish_)
    
    ```fish
    set -Ux IPY_METRICS_ENABLE false
    ```

### Windows

- PowerShell

    For a single command:

    ```powershell
    $env:IPY_METRICS_ENABLE="false"; ipy config
    ```
    
    Permanently for the current user:

    ```powershell
    [Environment]::SetEnvironmentVariable("IPY_METRICS_ENABLE", "false", "User")
    ```

- CMD
    
    For a single command
    ```cmd
    set IPY_METRICS_ENABLE=false && ipy config
    ```
    
    Permanently for the current user:

    ```cmd
    setx IPY_METRICS_ENABLE "false"
    ```

## Questions or Concerns?

If you have any questions or concerns about our data collection practices:

- 💬 Start a discussion on [GitHub Discussions]
- 🐛 Report issues on [GitHub Issues]
- 🔒 For security concerns, see our [Security Policy]

We're committed to transparency and respect for your privacy. Thank you for helping us improve `instant-python`!

[GitHub Discussions]: https://github.com/dimanu-py/instant-python/discussions
[GitHub Issues]: https://github.com/dimanu-py/instant-python/issues
[Security Policy]: ../development/security.md

