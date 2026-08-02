.DEFAULT_GOAL := help

.PHONY: help
help:  ## Show this help.
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(firstword $(MAKEFILE_LIST)) | \
			awk 'BEGIN {FS = ":.*## "}; {printf "%-30s %s\n", $$1, $$2}'

.PHONY: local-setup
local-setup:  ## Setup git hooks and install dependencies.
	@echo "\n⌛ Setting up the project...\n"
	@make install
	@uv run -m pre_commit install --hook-type pre-commit --hook-type commit-msg --hook-type pre-push

.PHONY: test
test:  ## Run all test.
	@echo "\n⌛ Running tests...\n"
	@uv run pytest test -ra

.PHONY: coverage
coverage:  ## Run all test with coverage.
	@echo "\n⌛ Running tests with coverage...\n"
	@uv run coverage run --branch -m pytest test
	@uv run coverage html
	@$(BROWSER) htmlcov/index.html

.PHONY: mutate
mutate:  ## Run mutation testing (optional: MUTATE_PATH=instant_python/<module>/).
	@echo "⌛ Running mutation testing...\n"
	@uv run mutmut run $(or $(MUTATE_PATH),instant_python)
	@uv run mutmut results

.PHONY: install
install:  ## Install dependencies.
	@echo "\n⌛ Installing dependencies...\n"
	@uv sync --all-groups

.PHONY: update
update:  ## Update dependencies.
	@echo "\n⌛ Updating dependencies...\n"
	@uv lock --upgrade
	@uv sync --all-groups

.PHONY: add-dep
add-dep:  ## Add a new dependency
	@uv add $(dep)

.PHONY: remove-dep
remove-dep:  ## Remove a dependency
	@uv remove $(dep)

.PHONY: check-typing
check-typing:  ## Run mypy type checking.
	@echo "\n⌛ Running type checking with mypy...\n"
	@uv run mypy

.PHONY: check-lint
check-lint:  ## Run ruff linting check.
	@echo "\n⌛ Running linting check...\n"
	@uvx ruff check instant_python test

.PHONY: lint
lint:  ## Apply ruff linting fix.
	@echo "\n⌛ Applying linting fixes...\n"
	@uvx ruff check --fix instant_python test

.PHONY: check-format
check-format:  ## Run ruff format check.
	@echo "\n⌛ Checking code formatting...\n"
	@uvx ruff format --check instant_python test

.PHONY: format
format:  ## Apply ruff format fix.
	@echo "\n⌛ Formatting project code...\n"
	@uvx ruff format instant_python test

.PHONY: autostyle
autostyle:  ## Apply all code style fixes.
	@echo "\n⌛ Applying all code style fixes...\n"
	@make format
	@make lint
	@git add . && git commit -m "style: apply code style fixes"

.PHONY: watch
watch:  ## Run all test with every change.
	@uv run ptw --runner "pytest -n auto test -ra"

.PHONY: show
show:  ## Show installed dependencies.
	@uv tree

.PHONY: search
search:  ## Show package details.
	@read -p "Enter package name to search: " package;\
	uv pip show $$package

.PHONY: tox
tox:  ## Run tox tests
	@uv run tox

.PHONY: audit
audit: # It audits dependencies and source code
	@echo "\n⌛ Running security audit...\n"
	@uv run -m pip_audit --progress-spinner off --ignore-vuln GHSA-4xh5-x5gv-qwph

.PHONY: secrets
secrets: # It checks for secrets in the source code
	@echo "\n⌛ Checking secrets...\n"
	@uv run -m pre_commit run gitleaks --all-files

.PHONY: build
build:  ## Build the project.
	@echo "\n⌛ Building the project...\n"
	@uv build

.PHONY: clean
clean: # It cleans up the project, removing the virtual environment and some files
	@echo "\n⌛ Cleaning up the project...\n"

	@uv run -m pre_commit clean)
	@uv run -m pre_commit uninstall --hook-type pre-commit --hook-type commit-msg)
	@rm --force --recursive .venv
	@rm --force --recursive `find . -type f -name '*.py[co]'`
	@rm --force --recursive `find . -name __pycache__`
	@rm --force --recursive `find . -name .ruff_cache`
	@rm --force --recursive `find . -name .mypy_cache`
	@rm --force --recursive `find . -name .pytest_cache`
	@rm --force --recursive .coverage
	@rm --force --recursive .coverage.*
	@rm --force --recursive coverage.xml
	@rm --force --recursive htmlcov

.PHONY: docs-serve
docs-serve:  ## Start server for documentation.
	@uv run mkdocs serve

.PHONY: claude
claude:  ## Create symlinks for Claude Code compatibility (CLAUDE.md → AGENTS.md, .claude → .agents).
	@echo "\n⌛ Creating Claude Code symlinks...\n"
	@ln -sf AGENTS.md CLAUDE.md
	@ln -sfn .agents .claude
	@ls -la CLAUDE.md .claude

.PHONY: opencode
opencode:  ## Create symlinks for OpenCode compatibility.
	@echo "\n⌛ Creating OpenCode symlinks...\n"
	@mkdir -p .opencode
	@rm -rf .opencode/commands
	@rm -rf .opencode/agents
	@ln -s ../.agents/commands .opencode/commands
	@ln -s ../.agents/agents .opencode/agents
	@ls -la .opencode