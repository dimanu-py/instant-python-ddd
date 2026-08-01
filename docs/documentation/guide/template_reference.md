# Template Reference

This page provides a complete reference of all built-in templates available in `instant-python`. When using [custom projects](custom_projects.md), you can reference these templates by their path in the `template` field.

!!! tip "Using Built-in Templates"
    You don't need to copy these templates to your custom template folder. Just reference the path shown below in your `main_structure.yml` file, and `instant-python` will automatically use the built-in template.

## How to Use Template Paths

When defining a file in your `main_structure.yml`, use the `template` field to specify which template to use:

```yaml
- name: makefile
  type: file
  template: scripts/makefile  # <- Use the path from the tables below
```

---

## Configuration Files

Templates for common configuration files used in Python projects.

| Template Name | Path | Description |
|--------------|------|-------------|
| `.gitignore` | `.gitignore` | Git ignore file for Python projects |
| `.pre-commit-config.yml` | `.pre-commit-config.yml` | Pre-commit hooks configuration |
| `.python-version` | `.python-version` | Python version specification file |
| `CITATION.cff` | `CITATION.cff` | Citation file format for academic software |
| `LICENSE` | `LICENSE` | Software license file |
| `mypy.ini` | `mypy.ini` | MyPy type checker configuration |
| `pyproject.toml` | `pyproject.toml` | Python project configuration file |
| `pytest.ini` | `pytest.ini` | Pytest configuration file |
| `README.md` | `README.md` | Project README file |
| `SECURITY.md` | `SECURITY.md` | Security policy file |

### Example Usage

```yaml
- name: .gitignore
  type: file
  template: .gitignore

- name: README
  type: file
  extension: .md
  template: README.md

- name: pyproject
  type: file
  extension: .toml
  template: pyproject.toml
```

---

## GitHub Templates

Templates for GitHub-specific files like workflows and issue templates.

| Template Name             | Path | Description                                            |
|---------------------------|------|--------------------------------------------------------|
| GitHub Action (Python)    | `github/action.yml` | GitHub Action workflow template that configures Python |
| CI Workflow               | `github/ci.yml` | Continuous Integration workflow                        |
| Release Workflow          | `github/release.yml` | Automated release workflow                             |
| Bug Report Issue Template | `github/bug_report.yml` | Issue template for bug reports                         |
| Feature Request Template  | `github/feature_request.yml` | Issue template for feature requests                    |

### Example Usage

```yaml
- name: .github
  type: directory
  children:
    - name: workflows
      type: directory
      children:
        - name: ci
          type: file
          extension: .yml
          template: github/ci.yml
        - name: release
          type: file
          extension: .yml
          template: github/release.yml
    - name: ISSUE_TEMPLATE
      type: directory
      children:
        - name: bug_report
          type: file
          extension: .yml
          template: github/bug_report.yml
        - name: feature_request
          type: file
          extension: .yml
          template: github/feature_request.yml
```

---

## Scripts

Utility scripts for common development tasks.

| Template Name | Path | Description |
|--------------|------|-------------|
| Makefile | `scripts/makefile` | Makefile with common commands |

### Example Usage

```yaml
- name: makefile
  type: file
  template: scripts/makefile
```

---

## FastAPI

Templates for FastAPI web applications.

| Template Name | Path | Description |
|--------------|------|-------------|
| Application Factory | `fastapi/application.py` | FastAPI application factory |
| Error Handlers | `fastapi/error_handlers.py` | Custom error handlers |
| Error Response | `fastapi/error_response.py` | Error response model |
| FastAPI Log Middleware | `fastapi/fastapi_log_middleware.py` | Logging middleware |
| Lifespan | `fastapi/lifespan.py` | Application lifespan management |
| Success Response | `fastapi/success_response.py` | Success response model |

### Example Usage

```yaml
- name: api
  type: directory
  python: True
  children:
    - name: application
      type: file
      extension: .py
      template: fastapi/application.py
    - name: error_handlers
      type: file
      extension: .py
      template: fastapi/error_handlers.py
    - name: lifespan
      type: file
      extension: .py
      template: fastapi/lifespan.py
```

---

## Event Bus

Templates for event-driven architecture with RabbitMQ.

| Template Name | Path | Description |
|--------------|------|-------------|
| Domain Event | `event_bus/domain_event.py` | Base domain event class |
| Domain Event JSON Deserializer | `event_bus/domain_event_json_deserializer.py` | JSON deserializer for events |
| Domain Event JSON Serializer | `event_bus/domain_event_json_serializer.py` | JSON serializer for events |
| Domain Event Subscriber | `event_bus/domain_event_subscriber.py` | Event subscriber interface |
| Event Aggregate | `event_bus/event_aggregate.py` | Event sourcing aggregate |
| Event Bus | `event_bus/event_bus.py` | Event bus interface |
| Exchange Type | `event_bus/exchange_type.py` | RabbitMQ exchange types |
| Mock Event Bus | `event_bus/mock_event_bus.py` | Mock event bus for testing |
| RabbitMQ Configurer | `event_bus/rabbit_mq_configurer.py` | RabbitMQ configuration |
| RabbitMQ Connection | `event_bus/rabbit_mq_connection.py` | RabbitMQ connection manager |
| RabbitMQ Consumer | `event_bus/rabbit_mq_consumer.py` | RabbitMQ message consumer |
| RabbitMQ Event Bus | `event_bus/rabbit_mq_event_bus.py` | RabbitMQ event bus implementation |
| RabbitMQ Queue Formatter | `event_bus/rabbit_mq_queue_formatter.py` | Queue name formatter |
| RabbitMQ Settings | `event_bus/rabbit_mq_settings.py` | RabbitMQ settings configuration |

### Example Usage

```yaml
- name: shared
  type: directory
  python: True
  children:
    - name: event_bus
      type: directory
      python: True
      children:
        - name: event_bus
          type: file
          extension: .py
          template: event_bus/event_bus.py
        - name: domain_event
          type: file
          extension: .py
          template: event_bus/domain_event.py
        - name: rabbit_mq_event_bus
          type: file
          extension: .py
          template: event_bus/rabbit_mq_event_bus.py
```

---

## Exceptions

Templates for custom exception classes.

| Template Name | Path | Description |
|--------------|------|-------------|
| Base Error | `exceptions/base_error.py` | Base exception class |
| Domain Error | `exceptions/domain_error.py` | Domain-specific exception |
| Domain Event Type Not Found Error | `exceptions/domain_event_type_not_found_error.py` | Event type not found exception |
| RabbitMQ Connection Not Established Error | `exceptions/rabbit_mq_connection_not_established_error.py` | RabbitMQ connection exception |

### Example Usage

```yaml
- name: shared
  type: directory
  python: True
  children:
    - name: exceptions
      type: directory
      python: True
      children:
        - name: base_error
          type: file
          extension: .py
          template: exceptions/base_error.py
        - name: domain_error
          type: file
          extension: .py
          template: exceptions/domain_error.py
```

---

## Logger

Templates for logging functionality.

| Template Name | Path | Description |
|--------------|------|-------------|
| File Logger | `logger/file_logger.py` | File-based logger implementation |
| File Rotating Handler | `logger/file_rotating_handler.py` | Rotating file handler |
| JSON Formatter | `logger/json_formatter.py` | JSON log formatter |

### Example Usage

```yaml
- name: shared
  type: directory
  python: True
  children:
    - name: logger
      type: directory
      python: True
      children:
        - name: file_logger
          type: file
          extension: .py
          template: logger/file_logger.py
        - name: json_formatter
          type: file
          extension: .py
          template: logger/json_formatter.py
```

---

## Persistence

Templates for database persistence with SQLAlchemy.

### Base Templates

| Template Name | Path | Description |
|--------------|------|-------------|
| Alembic Migrator | `persistence/alembic_migrator.py` | Alembic migration manager |
| Base | `persistence/base.py` | Base SQLAlchemy models |

### Asynchronous Persistence

| Template Name | Path | Description |
|--------------|------|-------------|
| Alembic Config | `persistence/async/alembic.ini` | Alembic configuration for async |
| Alembic Environment | `persistence/async/env.py` | Alembic environment script |
| Alembic Migration Template | `persistence/async/script.py.mako` | Migration script template |
| Async Engine Fixture | `persistence/async/async_engine_fixture.py` | Pytest fixture for async engine |
| Async Session | `persistence/async/async_session.py` | Async session factory |
| Models Metadata | `persistence/async/models_metadata.py` | SQLAlchemy metadata |
| Postgres Settings | `persistence/async/postgres_settings.py` | PostgreSQL settings |
| Async README | `persistence/async/README.md` | Documentation for async persistence |
| Async SQLAlchemy Repository | `persistence/async/sqlalchemy_repository.py` | Async repository pattern |

### Example Usage

```yaml
- name: shared
  type: directory
  python: True
  children:
    - name: persistence
      type: directory
      python: True
      children:
        - name: base
          type: file
          extension: .py
          template: persistence/base.py
        - name: async
          type: directory
          python: True
          children:
            - name: async_session
              type: file
              extension: .py
              template: persistence/async/async_session.py
            - name: sqlalchemy_repository
              type: file
              extension: .py
              template: persistence/async/sqlalchemy_repository.py
            - name: alembic
              type: file
              extension: .ini
              template: persistence/async/alembic.ini
```

---

## Agents

Templates for AI-assisted software development environment.

### Root Files

| Template Name | Path | Description |
|--------------|------|-------------|
| AGENTS.md | `agents/AGENTS.md` | Main project rules and guidelines for AI agents |

### Documentation (docs/)

| Template Name | Path | Description |
|--------------|------|-------------|
| Convention Guidelines | `agents/convention_guidelines.md` | Convention document structure standard |
| Leader Workflow | `agents/leader_workflow.md` | Full development pipeline description |
| TDD Outside-In | `agents/tdd_outside_in.md` | Outside-In TDD convention and test structure |
| Tasks JSON | `agents/tasks.json` | Task management file (status: pending, spec_ready, in_progress, done, blocked) |

### Agents

| Template Name | Path | Description |
|--------------|------|-------------|
| Convention Keeper | `agents/agents/convention_keeper.md` | Captures learnings into convention docs |
| Craftsman Leader | `agents/agents/craftsman_leader.md` | Orchestrates the full development pipeline |
| Judge | `agents/agents/judge.md` | Reviews code and runs mutation testing |
| Spec Partner | `agents/agents/spec_partner.md` | Debates and distills specs into .spec and .feature files |
| TDD Craftsman | `agents/agents/tdd_craftsman.md` | Implements features by Outside-In TDD |

### Commands

| Template Name | Path | Description |
|--------------|------|-------------|
| Code Review | `agents/commands/code_review.md` | Review pending changes for quality and maintainability |
| Commit | `agents/commands/commit.md` | Split changes into atomic conventional commits |
| Security Review | `agents/commands/security_review.md` | Security analysis and risk assessment |
| Technical Debt Review | `agents/commands/technical_debt_review.md` | Technical debt identification and prioritization |

### Skills

| Skill                         | Path                                           | Description                                                |
|-------------------------------|------------------------------------------------|------------------------------------------------------------|
| Complexity Review             | `agents/skills/complexity_review/SKILL.md`     | Evaluate technical proposals against complexity dimensions |
| Complexity Review (Reference) | `agents/skills/complexity_review/REFERENCE.md` | Reference for complexity review dimensions                 |
| Convention                    | `agents/skills/convention/SKILL.md`            | Create or update convention documentation                  |
| Hamburger Method              | `agents/skills/hamburger_method/SKILL.md`      | Slice features into vertical deliverable pieces            |
| Hamburger Method (Reference)  | `agents/skills/hamburger_method/REFERENCE.md`  | Reference for hamburger method patterns                    |
| Micro Steps Coach             | `agents/skills/micro_steps_coach/SKILL.md`     | Break down work into 1-3 hour micro-steps                  |
| Micro Steps Coach (Reference) | `agents/skills/micro_steps_coach/REFERENCE.md` | Reference for expand-contract patterns                     |
| Mutation Testing              | `agents/skills/mutation_testing/SKILL.md`      | Apply mutation testing analysis in Python                  |
| Spec                          | `agents/skills/spec/SKILL.md`                  | Create or update feature specifications                    |
| Story Splitting               | `agents/skills/story_splitting/SKILL.md`       | Split large stories using proven heuristics                |
| Story Splitting (Reference)   | `agents/skills/story_splitting/REFERENCE.md`   | Reference for story splitting patterns                     |
| Test Desiderata               | `agents/skills/test_desiderata/SKILL.md`       | Analyze test quality using Test Desiderata framework       |
| Test Desiderata (Reference)   | `agents/skills/test_desiderata/REFERENCE.md`   | Reference for the 12 test quality dimensions               |
| XP Refactor                   | `agents/skills/xp_refactor/SKILL.md`           | Apply XP Simple Design principles when refactoring         |

### Example Usage

```yaml
- name: AGENTS.md
  type: file
  extension: .md
  template: agents/AGENTS.md

- name: docs
  type: directory
  children:
    - name: conventions
      type: directory
      children:
        - name: convention_guidelines
          type: file
          extension: .md
          template: agents/convention_guidelines.md
        - name: testing
          type: directory
          children:
            - name: tdd_outside_in
              type: file
              extension: .md
              template: agents/tdd_outside_in.md
        - name: workflow
          type: directory
          children:
            - name: leader_workflow
              type: file
              extension: .md
              template: agents/leader_workflow.md
    - name: features
      type: directory
    - name: progress
      type: directory
    - name: tasks
      type: file
      extension: .json
      template: agents/tasks.json

- name: .agents
  type: directory
  children:
    - name: agents
      type: directory
      children:
        - name: craftsman_leader
          type: file
          extension: .md
          template: agents/agents/leader.md
        - name: spec_partner
          type: file
          extension: .md
          template: agents/agents/spec_partner.md
        - name: tdd_craftsman
          type: file
          extension: .md
          template: agents/agents/tdd_craftsman.md
        - name: judge
          type: file
          extension: .md
          template: agents/agents/judge.md
        - name: convention_keeper
          type: file
          extension: .md
          template: agents/agents/convention_keeper.md
    - name: commands
      type: directory
      children:
        - name: commit
          type: file
          extension: .md
          template: agents/commands/commit.md
        - name: technical_debt_review
          type: file
          extension: .md
          template: agents/commands/technical_debt_review.md
    - name: skills
      type: directory
      children:
        - name: code_review
          type: directory
          children:
            - name: SKILL
              type: file
              extension: .md
              template: agents/skills/code_review/spec_guidelines.md
        - name: security_review
          type: directory
          children:
            - name: SKILL
              type: file
              extension: .md
              template: agents/skills/security_review/spec_guidelines.md
        - name: complexity_review
          type: directory
          children:
            - name: SKILL
              type: file
              extension: .md
              template: agents/skills/complexity_review/spec_guidelines.md
            - name: REFERENCE
              type: file
              extension: .md
              template: agents/skills/complexity_review/REFERENCE.md
        - name: convention
          type: directory
          children:
            - name: SKILL
              type: file
              extension: .md
              template: agents/skills/convention/spec_guidelines.md
        - name: hamburger_method
          type: directory
          children:
            - name: SKILL
              type: file
              extension: .md
              template: agents/skills/hamburger_method/spec_guidelines.md
            - name: REFERENCE
              type: file
              extension: .md
              template: agents/skills/hamburger_method/REFERENCE.md
        - name: micro_steps_coach
          type: directory
          children:
            - name: SKILL
              type: file
              extension: .md
              template: agents/skills/micro_steps_coach/spec_guidelines.md
            - name: REFERENCE
              type: file
              extension: .md
              template: agents/skills/micro_steps_coach/REFERENCE.md
        - name: mutation_testing
          type: directory
          children:
            - name: SKILL
              type: file
              extension: .md
              template: agents/skills/mutation_testing/spec_guidelines.md
        - name: spec
          type: directory
          children:
            - name: SKILL
              type: file
              extension: .md
              template: agents/skills/spec/spec_guidelines.md
        - name: story_splitting
          type: directory
          children:
            - name: SKILL
              type: file
              extension: .md
              template: agents/skills/story_splitting/spec_guidelines.md
            - name: REFERENCE
              type: file
              extension: .md
              template: agents/skills/story_splitting/REFERENCE.md
        - name: test_desiderata
          type: directory
          children:
            - name: SKILL
              type: file
              extension: .md
              template: agents/skills/test_desiderata/spec_guidelines.md
            - name: REFERENCE
              type: file
              extension: .md
              template: agents/skills/test_desiderata/REFERENCE.md
        - name: xp_refactor
          type: directory
          children:
            - name: SKILL
              type: file
              extension: .md
              template: agents/skills/xp_refactor/spec_guidelines.md
```

---

## Complete Example

Here's a complete example showing how to create a custom project that uses multiple built-in templates:

```yaml
# main_structure.yml

- name: .gitignore
  type: file
  template: .gitignore

- name: README
  type: file
  extension: .md
  template: README.md

- name: pyproject
  type: file
  extension: .toml
  template: pyproject.toml

- name: makefile
  type: file
  template: scripts/makefile

- name: .github
  type: directory
  children:
    - name: workflows
      type: directory
      children:
        - name: ci
          type: file
          extension: .yml
          template: github/ci.yml

- name: src
  type: directory
  python: True
  children:
    - name: api
      type: directory
      python: True
      children:
        - name: application
          type: file
          extension: .py
          template: fastapi/application.py
        - name: error_handlers
          type: file
          extension: .py
          template: fastapi/error_handlers.py
    - name: shared
      type: directory
      python: True
      children:
        - name: exceptions
          type: directory
          python: True
          children:
            - name: base_error
              type: file
              extension: .py
              template: exceptions/base_error.py
        - name: logger
          type: directory
          python: True
          children:
            - name: file_logger
              type: file
              extension: .py
              template: logger/file_logger.py

- name: test
  type: directory
  python: True
```

This will create a project with:

- Configuration files (`.gitignore`, `README.md`, `pyproject.toml`)
- A `makefile` for common tasks
- GitHub CI workflow
- FastAPI application structure
- Shared utilities for exceptions and logging
- Test directory

---

## Template Resolution

Remember that when you specify a `template` path:

1. **First:** `instant-python` looks in your custom templates folder
2. **Second:** If not found, it checks the built-in templates using the path you specified
3. **Third:** If still not found, it creates an empty file

This allows you to:

- Override built-in templates by providing your own version in your custom templates folder
- Mix built-in templates with your custom templates
- Fall back to empty files if neither exists

For more information about custom projects, see the [Custom Projects](custom_projects.md) guide.

