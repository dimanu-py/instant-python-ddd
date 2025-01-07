.DEFAULT_GOAL := help

.PHONY: help
help:  ## Show this help.
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(firstword $(MAKEFILE_LIST)) | \
			awk 'BEGIN {FS = ":.*## "}; {printf "%-30s %s\n", $$1, $$2}'

.PHONY: test
test:  ## Run all test.
	{{cookiecutter.dependency_manager}} run pytest -n auto tests -ra

.PHONY: unit
unit:  ## Run unit test in changed files.
	scripts/tests/unit.sh

.PHONY: integration
integration:  ## Run integration test in changed files.
	scripts/tests/integration.sh

.PHONY: all-unit
all-unit:  ## Run all unit test.
	{{cookiecutter.dependency_manager}} run pytest -n auto -m "unit" -ra

.PHONY: all-integration
all-integration:  ## Run all integration test.
	{{cookiecutter.dependency_manager}} run pytest -n auto -m "integration" -ra

.PHONY: all-acceptance
all-acceptance:  ## Run all acceptance test.
	{{cookiecutter.dependency_manager}} run pytest -n auto -m "acceptance" -ra

.PHONY: coverage
coverage:  ## Run all test with coverage.
	{{cookiecutter.dependency_manager}} run coverage run --branch -m pytest tests
	{{cookiecutter.dependency_manager}} run coverage html
	$(BROWSER) htmlcov/index.html

.PHONY: local-setup
local-setup:  ## Setup git hooks and install dependencies.
	scripts/local-setup.sh
	make install

.PHONY: install
install:  ## Install dependencies.
	{% if cookiecutter.dependency_manager == "pdm" -%}
	pdm install
	{%- elif cookiecutter.dependency_manager == "uv" -%}
	uv sync --all-groups
	{%- endif %}

.PHONY: update
update:  ## Update dependencies.
	{% if cookiecutter.dependency_manager == "pdm" -%}
	pdm update
	{%- elif cookiecutter.dependency_manager == "uv" -%}
	uv sync --upgrade
	{%- endif %}

.PHONY: add-dep
add-dep:  ## Add a new dependency.
	scripts/add-dependency.sh

.PHONY: remove-dep
remove-dep:  ## Remove a dependency.
	scripts/remove-dependency.sh

.PHONY: check-typing
check-typing:  ## Run mypy type checking.
	{{cookiecutter.dependency_manager}} run mypy

.PHONY: check-lint
check-lint:  ## Run ruff linting check.
	{% if cookiecutter.dependency_manager == "pdm" -%}
	pdm run ruff check src tests
	{%- elif cookiecutter.dependency_manager == "uv" -%}
	uvx ruff check src tests
	{%- endif %}

.PHONY: lint
lint:  ## Apply ruff linting fix.
	{% if cookiecutter.dependency_manager == "pdm" -%}
	pdm run ruff check --fix src tests
	{%- elif cookiecutter.dependency_manager == "uv" -%}
	uvx ruff check --fix src tests
	{%- endif %}

.PHONY: check-format
check-format:  ## Run ruff format check.
	{% if cookiecutter.dependency_manager == "pdm" -%}
	pdm run ruff format --check src tests
	{%- elif cookiecutter.dependency_manager == "uv" -%}
	uvx ruff format --check src tests
	{%- endif %}

.PHONY: format
format:  ## Apply ruff format fix.
	{% if cookiecutter.dependency_manager == "pdm" -%}
	pdm run ruff format src tests
	{%- elif cookiecutter.dependency_manager == "uv" -%}
	uvx ruff format src tests
	{%- endif %}

.PHONY: pre-commit
pre-commit: check-typing check-lint check-format all-unit ## Run pre-commit checks.

.PHONY: pre-push
pre-push:  all-integration all-acceptance ## Run pre-push checks.

.PHONY: watch
watch:  ## Run all test with every change.
	{{cookiecutter.dependency_manager}} run ptw --runner "pytest -n auto tests -ra"

.PHONY: insert-template
insert-template:  ## Insert a template class among the existing ones.
	{{cookiecutter.dependency_manager}} run python -m scripts.insert_template

.PHONY: create-aggregate
create-aggregate:  ## Create a new aggregate inside contexts folder.
	{{cookiecutter.dependency_manager}} run python -m scripts.create_aggregate

.PHONY: show
show:  ## Show installed dependencies.
	{% if cookiecutter.dependency_manager == "pdm" -%}
	pdm list
	{%- elif cookiecutter.dependency_manager == "uv" -%}
	uv tree
	{%- endif %}

.PHONY: search
search:  ## Show package details.
	@read -p "Enter package name to search: " package;\
	{% if cookiecutter.dependency_manager == "pdm" -%}
	pdm show $$package
	{%- elif cookiecutter.dependency_manager == "uv" -%}
	uv pip show $$package
	{%- endif %}
