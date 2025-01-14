.DEFAULT_GOAL := help

.PHONY: help
help:  ## Show this help.
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(firstword $(MAKEFILE_LIST)) | \
			awk 'BEGIN {FS = ":.*## "}; {printf "%-30s %s\n", $$1, $$2}'

.PHONY: test
test:  ## Run all test.
	{{cookiecutter.dependency_manager}} run pytest -n auto tests -ra

.PHONY: coverage
coverage:  ## Run all test with coverage.
	{{cookiecutter.dependency_manager}} run coverage run --branch -m pytest tests
	{{cookiecutter.dependency_manager}} run coverage html
	@xdg-open "${PWD}/htmlcov/index.html"

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
