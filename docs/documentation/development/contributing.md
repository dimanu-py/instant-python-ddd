# Contributing

First off, **thank you** for wanting to improve **Instant Python** package! Whether you're fixing a typo or building a whole new feature,
your help makes the library better for everyone.

## Before You Start

1. **Search first**: check for existing [issues](https://github.com/dimanu-py/instant-python/issues) before opening a new one. You might
    find that your issue has already been reported or even fixed in a pull request.
2. **Security issues**: report privately via our [`Security Policy`](https://dimanu-py.github.io/instant-python/home/security/); **do not** raise a public issue for vulnerabilities.

## Start Contributing

!!! info
    All examples assume you have [`mise`](https://mise.jdx.dev) installed, which provisions `task` and the rest of the toolchain. For more information about the Taskfile, see the [Tooling](#tooling) section.

### Common Steps

All contributions have some common steps, whether you're fixing a bug, adding a feature, or improving documentation.

1. **Fork the Repository**: Click the fork button on the repository page.

2. **Clone Your Fork**:

    ```bash
    git clone git+ssh://git@github.com/<your-username>/instant-python.git
    ```

3. **Setup the Development Environment**: Create a virtual environment, install all dependencies, and setup custom pre-commit hooks.

    ```bash
    task local-setup
    ```

4. **Create a Feature Branch**: Create a feature branch from the `main` branch.

    ```bash
    git switch -c feat/<branch-name>
    ```

### Contributing with Code

If you want to implement a new feature, fix a bug, or improve the codebase, it's time to get your hands dirty!

1. **Time to Code**: Make your changes.

2. **Quality Checks**: Run the following commands to ensure your code is formatted, linted, and passes the test suite.

    ```bash
    task format
    task lint
    task test
    ```

3. **Commit Your Changes**: Commit your changes with a descriptive commit message.
    
    !!! info
        More information about our commit message guidelines can be found in the [Commit Message Guidelines](#commit-message-guidelines) section.

    ```bash
    git add .
    git commit -m "feat(configuration): implement validation of general information section" -S --signoff  # we only accept signed and signed-off commits
    ```

4. **Push Your Changes**: Push your changes to your fork.

    ```bash
    git push -u origin feat/<branch-name>
    ```

5. **Open a Pull Request**: Open a pull request against the `main` branch and fill out our [`pull request template`](https://github.com/dimanu-py/instant-python/blob/main/.github/pull_request_template.md).
    
    !!! info
        More information about our pull request guidelines and feedback can be found in the [Pull Request Guidelines](#pull-request-guidelines) section.

### Contributing with Documentation

If you want to contribute to the documentation, you can do so by editing the Markdown files in the `docs` directory. 
The documentation is built using [MkDocs](https://www.mkdocs.org/) and can be previewed locally running the following command:

```bash
task docs-serve
```

Once you have made your changes, you can follow these steps to contribute:

1. **Commit Your Changes**: Commit your changes with a descriptive commit message.

    !!! info
        More information about our commit message guidelines can be found in the [Commit Message Guidelines](#commit-message-guidelines) section.

    ```bash
    git add .
    git commit -m "feat(configuration): implement validation of general information section" -S --signoff  # we only accept signed and signed-off commits
    ```

2. **Push Your Changes**: Push your changes to your fork.

    ```bash
    git push -u origin feat/<branch-name>
    ```

3. **Open a Pull Request**: Open a pull request against the `main` branch and fill out our [`pull request template`](https://github.com/dimanu-py/instant-python/blob/main/.github/pull_request_template.md).

    !!! info
        More information about our pull request guidelines and feedback can be found in the [Pull Request Guidelines](#pull-request-guidelines) section.

   
<a name="commit-message-guidelines"></a>
## Commit Message Guidelines

This project follows **[Conventional Commits](https://www.conventionalcommits.org)** enforced by 
**[Commitizen](https://commitizen-tools.github.io)** as a pre-commit hook and 
**[Semantic Versioning](https://semver.org)** used by [python-semantic-release](https://python-semantic-release.readthedocs.io).

!!! info
    More information about versioning and releases can be found in the [Releases](https://dimanu-py.github.io/instant-python/home/releases/) page.

!!! important
    This repository only accepts signed and signed-off commits, check [GitHub documentation](https://docs.github.com/en/authentication/managing-commit-signature-verification/signing-commits) if you need help with that.

### How to Write a Good Commit Message

- **Structure**: Each commit message must consist of a type, an optional scope, and a concise description (e.g., `feat(template): create template for github action`).
- **Types**: Common types include:
    - `feat`: Implementing new code, modifying existing behavior or removing existing code (minor release).
    - `fix`: Bug fix or fix of failing tests due to behavior changes (patch release).
    - `docs`: Documentation update.
    - `refactor`: Code change that modifies existing code without altering its behavior.
    - `perf`: Performance improvement (patch release).
    - `test`: Change related to tests (adding, updating, removing tests).
    - `build`: Changes that affect the build system (new dependencies, tools, ...) (patch release).
    - `ci`: Pipeline changes (GitHub Actions, make commands, ...).
- **Scope**: Use the scope to clarify what part of the codebase is affected (e.g., `commands`, `configuration`, `project-creator`). We specify the first level folders in the scope.
- **Description**: Use the imperative mood ("add", "fix", "update", ...; not "added", "fixed", "updates", ...).
- **Body (optional)**: Explain what and why vs. how. Reference issues if relevant.
- **Breaking Changes**: Append `!` to the commit type or start the body with `BREAKING CHANGE:` if the commit introduces an API or behavioral change (major release).

<a name="pull-request-guidelines"></a>
## Pull Request Guidelines

!!! important
    Only code owners are allowed to merge a pull request.

- Use our [`pull request template`](https://github.com/dimanu-py/instant-python/blob/main/.github/pull_request_template.md).
- **Keep PRs Focused**: Submit one logical change per pull request. Avoid bundling unrelated changes together.
- **Descriptive Titles and Summaries**: Use clear, descriptive PR titles and fill out all sections of the PR template, especially the motivation and context.
- **Reference Issues**: Link related issues by number (e.g., `Closes #123`) to enable automatic closing and better tracking.
- **Checklist Completion**: Ensure all items in the PR template checklist are addressed before requesting a review.
- **Passing Checks Required**: PRs must pass all CI checks (format, lint, tests, coverage, ...) before being considered for review (enforced with branch rules).
- **Request Reviews Thoughtfully**: Assign reviewers only after your PR is ready and all checks pass.
- **Rebase or Update**: If your branch is behind `main`, rebase or merge the latest changes before requesting a review (enforced with branch rules).
- **No Force Pushes on Shared Branches**: Only force-push to your own feature branches, not shared or open PR branches (enforced with branch rules).
- **Explain Breaking Changes**: Clearly highlight any breaking changes in the PR description and label/tag accordingly.
- **Documentation and Tests**: Update documentation and tests as needed for your changes.

### How to Write Good Feedback

We follow [Conventional Comments](https://conventionalcomments.org) to keep reviews clear and actionable.

- **Start with a label**: praise:, nitpick:, suggestion:, issue:, or question:.
- **Indicate blockers correctly**: If the pull request must not be merged until the comment is resolved, add the blocking modifier in parentheses after the label, e.g. issue (blocking):.
- **Be specific**: quote the relevant code or line numbers.
- **Stay constructive & courteous**: focus on the code, not the coder.
- **Offer alternatives when pointing out issues**.

<a name="tooling"></a>
## Tooling

!!! important
    All default project commands use [`task`](https://taskfile.dev), provisioned via [`mise`](https://mise.jdx.dev) from `mise.toml`.


!!! important
    You must have **UV** installed to use the most of the default project commands.

The project provides a [`Taskfile`](https://github.com/dimanu-py/instant-python/blob/main/Taskfile.yml) with some helpful commands,
this commands must be run from the root of the project. For more details on each command, run `task` or `task --list-all`.

- **Environment Setup:** Run `task local-setup` to create a virtual environment, install all dependencies (development + production), and install pre-commit hooks.
- **Install Dependencies:** Run `task install` to install all dependencies (development + production).
- **Code Formatting:** Run `task check-format` to check for code format issues and `task format` to automatically format code using Ruff.
- **Linting:** Run `task check-lint` to check code quality using Ruff for static analysis and `task lint` to automatically fix linting issues.
- **Testing:** Run `task test` to execute all tests.
- **Coverage:** Run `task coverage` to generate a test coverage report.
- **Build:** Run `task build` to build the project.
- **Audit:** Run `task audit` to audit dependencies for known vulnerabilities.
- **Secrets Scanning:** Run `task secrets` to scan for secrets in the hole codebase.
- **Environment Cleanup:** Run `task clean` to remove the virtual environment, caches, and all generated files.

There are some additional commands that can be used during development:

- **Update Dependencies:** Run `task update` to update all dependencies to their latest versions.
- **Adding / Removing Dependencies:** Use `task add-dep` or `task remove-dep` to add or remove dependencies from the project.
- **Run test in watch mode:** Run `task watch` to run tests in watch mode, automatically re-running tests when files change.
- **Serve Documentation:** Run `task docs-serve` to serve the documentation locally, allowing you to preview changes in real-time.

## Donating

If you find this library useful and want to help, you can also give it a star on GitHub or donate in the following link

[![Donate](https://img.shields.io/badge/Buy_me_a_coffee-5d83f5?style=for-the-badge&logo=ko-fi&logoColor=white&__cf_chl_managed_tk__=pmd_sOkOcrsQ4T6MRVPX2TeB_mbk2ZryAIn3rNigWIBBC6U-1633993526-0-gqNtZGzNAyWjcnBszQkl)](https://buymeacoffee.com/dimanu.py)


_Thank you for helping make **Instant Python** package awesome!_
