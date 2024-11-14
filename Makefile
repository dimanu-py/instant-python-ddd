.DEFAULT_GOAL := help

.PHONY: help
help:  ## Show this help.
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(firstword $(MAKEFILE_LIST)) | \
			awk 'BEGIN {FS = ":.*## "}; {printf "%-30s %s\n", $$1, $$2}'

.PHONY: test
test:  ## Run all test.
	uv run pytest -n auto tests -ra

.PHONY: unit
unit:  ## Run unit test in changed files.
	scripts/tests/unit.sh

.PHONY: integration
integration:  ## Run integration test in changed files.
	scripts/tests/integration.sh

.PHONY: all-unit
all-unit:  ## Run all unit test.
	uv run pytest -n auto -m "unit" -ra

.PHONY: all-integration
all-integration:  ## Run all integration test.
	uv run pytest -n auto -m "integration" -ra

.PHONY: all-acceptance
all-acceptance:  ## Run all acceptance test.
	uv run pytest -n auto -m "acceptance" -ra

.PHONY: coverage
coverage:  ## Run all test with coverage.
	uv run coverage run --branch -m pytest tests
	uv run coverage html
	$(BROWSER) htmlcov/index.html

.PHONY: local-setup
local-setup:  ## Setup git hooks and install dependencies.
	scripts/local-setup.sh
	make install

.PHONY: install
install:  ## Install dependencies.
	uv sync --all-groups

.PHONY: update
update:  ## Update dependencies.
	uv sync --upgrade

.PHONY: add-dep
add-dep:  ## Add a new dependency.
	scripts/add-dependency.sh

.PHONY: remove-dep
remove-dep:  ## Remove a dependency.
	scripts/remove-dependency.sh

.PHONY: check-typing
check-typing:  ## Run mypy type checking.
	uv run mypy

.PHONY: check-lint
check-lint:  ## Run ruff linting check.
	uvx ruff check src tests

.PHONY: lint
lint:  ## Apply ruff linting fix.
	uvx ruff check --fix src tests

.PHONY: check-format
check-format:  ## Run ruff format check.
	uvx ruff format --check src tests

.PHONY: format
format:  ## Apply ruff format fix.
	uvx ruff format src tests

.PHONY: pre-commit
pre-commit: check-typing check-lint check-format all-unit ## Run pre-commit checks.

.PHONY: pre-push
pre-push:  all-integration all-acceptance ## Run pre-push checks.

.PHONY: watch
watch:  ## Run all test with every change.
	uv run ptw --runner "pytest -n auto tests -ra"

.PHONY: insert-template
insert-template:  ## Insert a template class among the existing ones.
	uv run python -m scripts.insert_template

.PHONY: create-aggregate
create-aggregate:  ## Create a new aggregate inside contexts folder.
	uv run python -m scripts.create_aggregate

.PHONY: show
show:  ## Show installed dependencies.
	uv tree

.PHONY: search
search:  ## Show package details.
	@read -p "Enter package name to search: " package;\
	uv pip show $$package