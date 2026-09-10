In previous sections you have learned all the features and configurations that `instant-python` provides to create your projects.

This section will provide a detailed explanation of all the default features that you can include in your projects. After reading
this section, you will be able to understand all the options available when creating your configuration file and how they will affect
the generated project.

## Development Environment Manager

Previously, `instant-python` let you choose between [_uv_](https://docs.astral.sh/uv) or [_pdm_](https://pdm-project.org/en/latest/) to handle you project environment
and Python version.
Since the first version was published, `uv` has gain a lot of popularity. Our data shows that all users have use `uv`. 
For that reason, we are dropping `pdm` as an option, in order to make setup simpler and keep the questions to the things that matter
when creating the project.

As before, `instant-python` will automatically download `uv` if it's not installed, and create a virtual environment. This will
allow you to install your dependencies and run tasks out of the box.

## Git Repository

You will be able to configure your project as a git repository automatically. `instant-python` will use the `username` and
`email` fields from the configuration file to set up your git identity.

If you choose to create a git repository, it will create a _README.md_ file and the _.gitignore_ file
configured for Python projects.

## Default Project Structures

There are some project templates already configured that you can use to create the folder structure of your project 
following a specific pattern.

!!! important "Folder organization is not architecture"
    These templates do not reflect your architecture, but the folder structure of your project. There is a key difference between these concepts.

### Domain Driven Design

Follows DDD pattern and screaming architecture organization.

Separates the source code and test folder in bounded contexts and aggregates.
Each aggregate will contain the known _domain_, _application_ and _infra_ layers. This template will allow you to create 
your first bounded context and aggregate automatically.

```
├── src
│  ├── bounded_context_name
│  │  └── aggregate_name
│  │  │  ├── application
│  │  │  ├── domain
│  │  │  └── infra
│  │  └── shared
│  ├── shared
│  └── delivery
│     └── api
└── tests
   ├── bounded_context_name
   │  └── aggregate_name
   │  │  ├── application
   │  │  ├── domain
   │  │  └── infra
   │  └── shared
   ├── shared
   └── delivery
      └── api
```

### Clean Architecture

Will create your folders following the clean architecture pattern.

Separates the source code and test folder in _domain_, _application_, _infrastructure_ and _delivery_ layers.

```
├── src
│  ├── application
│  ├── domain
│  ├── infra
│  └── delivery
│     └── api
└── tests
   ├── acceptance
   ├── unit
   └── integration
```

### Standard Project

Will create your project with the common pattern of source code and test folder.

```
├── src
└── tests
```

## Out-of-the-box Implementations

When creating a new configuration file, you will be able to include some boilerplate and implementation code
that will help you to start your project.

!!! tip "Use as a starting point"
    These implementations are completely subjective and personal. This does not mean that you must implement
    them in the same way or that they are the best way to implement them. You can use them as a starting point
    and iterate them as you need.

!!! warning "Availability"
    These implementations are only available when using one of the [default project structures](#default-project-structures).

### GitHub actions and workflows

A common feature in projects is to have a CI/CD pipeline that will run some tasks. This option will include the following:

- A GitHub action that will set up your Python environment in your pipeline using the dependency manager you selected.
- A workflow that will check linting, formatting, and static analysis of your code. Make an analysis of your code quality, audit
  your dependencies, analyze for any leakage of secrets and run all tests generating a coverage report.
- A workflow that will create a new version tag for your project, update a CHANGELOG.md file and generates a new release in GitHub using
  `semantic-release`. You can get a deeper understanding of this workflow in the [releases section](../development/releases.md).

!!! info "Default tools"
    When selecting this feature, by default, the library will include `mypy` as a type checker, `ruff` as a linter and formatter, and
    `pytest` as a test runner. If you want to use different tools, you can change them later in the workflow file.

!!! info "Make commands"
    Some of the steps in this workflow uses some of the make commands presented in the [makefile section](#makefile).

### GitHub issues templates

This feature will include two GitHub issues templates that you can use to create issues in your project:

- A bug report template that will help you to report bugs in your project.
- A feature request template that will help you to request new features in your project.

### Precommit hooks

Precommit hooks are a great way to ensure that your code is always in a good state before committing it to the repository.

This boilerplate will include a precommit hook that will run the following tasks before committing your code:

- Check for any large files that should not be committed to the repository.
- Check for files that have the same name but only differ in case, which can cause issues in some file systems.
- Check the format of toml and yaml files
- Check for any merge conflicts that have not been resolved.
- Check for any secrets that have been leaked in the code.
- Check for the format of commit messages, ensuring they follow the conventional commit format.

Additionally, it will include two pre-push hooks:

- One that will check for any linting error
- One to check for any formatting error

### Security file

This feature will include a _SECURITY.md_ file that will help the users of your project
to report security issues in your project. It will include:

- Steps explaining how to report security issues.
- How we will handle security issues and disclosure.

### Citation file

When working on open source projects, it's common to include a _CITATION.cff_ file that will
allow users to cite your project when using it in their research or projects.

This feature will include a _CITATION.cff_ file that will help users to cite your project.

### Logger

Logging messages in an application it's a common task.

This boilerplate will include a basic logger that creates a handler for
production with logging ERROR level and a handler for development with logging DEBUG
level. These handlers will be logging messages into a file that will be rotated every day.

It will also include a json formatter that formats the message with the time the logg was made,
the level, the name or title of the message and the message itself.

### FastAPI

[FastAPI](https://fastapi.tiangolo.com/) has become one of the most popular frameworks to create APIs in Python. This boilerplate will include:

- A main file where the FastAPI is created
- Two error handlers configured, one that captures unexpected errors that will raise a 500 status code, and another
  handler that catches `DomainError` instances and raises a 400 status code by default.
- When logger built-in feature is selected, it will include a middleware that will log all requests and a handler to
  be able to log Pydantic validation errors.
- A lifespan that will execute the migrations with alembic when the application starts.
- A decoupled implementation to model your success and error responses.

### Makefile

A Makefile is a common tool to run tasks in your project. This feature is specially useful when automating tasks and
avoid remembering all the commands.

!!! warning "Windows compatibility"
    If you are running `instant-python` in a Windows environment, the Makefile will not work out of the box. You would need
    to install a tool like [GNU Make for Windows](https://gnuwin32.sourceforge.net/packages/make.htm) or use a different task runner.

The default Makefile will include the following commands:

| Command             | Description                                 |
|---------------------|---------------------------------------------|
| `make help`         | Show available commands                     |
| `make local-setup`  | Set up the local development environment    |
| `make install`      | Install all dependencies                    |
| `make update`       | Update all dependencies                     |
| `make add-dep`      | Add a new dependency                        |
| `make remove-dep`   | Remove a dependency                         |
| `make test`         | Run all tests                               |
| `make unit`         | Run all unit tests                          |
| `make integration`  | Run all integration tests                   |
| `make acceptance`   | Run all acceptance tests                    |
| `make coverage`     | Run coverage tests                          |
| `make watch`        | Run tests in watch mode                     |
| `make check-typing` | Runs type checker                           |
| `make check-lint`   | Checks lint code with Ruff                  |
| `make lint`         | Fixes lint errors code with Ruff            |
| `make check-format` | Checks format code with Ruff                |
| `make format`       | Format code with Ruff                       |
| `make secrets`      | Analyzes source code for leakage of secrets |
| `make audit`        | Identifies vulnerabilities in dependencies  |
| `make clean`        | Cleans up the project metadata files        |
| `make show`         | Show all installed dependencies             |
| `make search`       | Show details of a specific package          |

!!! info "Test commands"
    The commands `unit`, `integration` and `acceptance` are defined based on the assumption that you will mark your tests with
    the `@pytest.mark.unit`, `@pytest.mark.integration` and `@pytest.mark.acceptance` custom decorators.
    If this is not your case, you can change the commands as needed in the Makefile to match your test structure.

Some of these commands will be added only based on the features and/or dependencies you set in the configuration file:

| Command             | Condition                                                                                         |
|---------------------|---------------------------------------------------------------------------------------------------|
| `make test`         | If `pytest` is install or if either `makefile` or `github_actions` built in features are selected |
| `make unit`         | If `pytest` is install or if either `makefile` or `github_actions` built in features are selected |
| `make integration`  | If `pytest` is install or if either `makefile` or `github_actions` built in features are selected |
| `make acceptance`   | If `pytest` is install or if either `makefile` or `github_actions` built in features are selected |
| `make coverage`     | If `pytest` is install or if either `makefile` or `github_actions` built in features are selected |
| `make watch`        | If `pytest-watch` is install                                                                      |
| `make check-lint`   | If `ruff` is install or if either `makefile` or `github_actions` built in features are selected   |
| `make lint`         | If `ruff` is install or if either `makefile` or `github_actions` built in features are selected   |
| `make check-format` | If `ruff` is install or if either `makefile` or `github_actions` built in features are selected   |
| `make format`       | If `ruff` is install or if either `makefile` or `github_actions` built in features are selected   |
| `make secrets`      | If `precommit_hook` built in feature is selected                                                  |
| `make audit`        | If `github_actions` built in feature is selected                                                  |

### Asynchronous SQL Alchemy

SQL Alchemy is a popular ORM for Python, and with the introduction of async and await in Python, it has become
a powerful tool to manage databases. This boilerplate will include:

- A basic implementation of a repository pattern that will allow you to create a repository for each entity in your project.
- A class to encapsulate postgres settings

### Asynchronous migrations

Along with SQL Alchemy it's typical to use Alembic to manage database migrations. This boilerplate will include everything
needed to configure the migrations and run them asynchronously.

### Value objects and exceptions

Value object pattern is a design pattern that emphasizes the use of immutable objects to represent values in a system. It encourages the creation of small, focused classes that encapsulate domain logic.

They act as behavior magnets and try to avoid the code smells of anemic domain models and primitive obsession among others.

Value objects are characterized by:

- Immutability: Once created, a value object's state cannot be changed
- Value equality: Two value objects are equal if their values are equal, regardless of identity
- Self-validation: Value objects validate their state upon construction
- Domain semantics: They represent meaningful concepts in the domain rather than primitive types

!!! info "New versions use `value-objects-sindri`"
    `instant-python` versions previous to 0.18.0 implemented value objects directly in the generated project.
    All these implementations have been moved to the [`value-objects-sindri`](https://pypi.org/project/value-objects-sindri/) library 
    to promote reusability and better maintenance.
    When selecting this feature, the generated project will include `value-objects-sindri` as a prod dependency, and
    `object-mother-sindri` as dev dependency for tests.

Along with `value-object-sindri` to model value objects, this feature will include:

1. A base exception class that you can use to create your own exceptions:

    ???+ example "Implementation"
    
        ```python
        class BaseError(Exception, ABC):
            def __init__(self, message: str) -> None:
                self._message = message
                super().__init__(self._message)
        
            @property
            def message(self) -> str:
                return self._message
        ```

2. A `DomainError` class that extends the base exception class. You can use this class to raise domain errors in your application.

    ???+ example "Implementation"
    
        ```python
        class DomainError(BaseError):
            ...
        ```

### Event bus

In complex applications, it's common to use an event bus to communicate between different parts of the application. This boilerplate
will set up a decoupled implementation of an event bus using RabbitMQ. This implementation will include:

- An `EventAggregate` class that will allow you to create your aggregates and publish events automatically.
    
    ???+ example "EventAggregate"
    
        ```python
        class EventAggregate(Aggregate):
            _domain_events: list[DomainEvent]
        
            def __init__(self) -> None:
                self._domain_events = []
        
            def record(self, event: DomainEvent) -> None:
                self._domain_events.append(event)
        
            def pull_domain_events(self) -> list[DomainEvent]:
                recorded_domain_events = self._domain_events
                self._domain_events = []
        
                return recorded_domain_events
        ```

- Modeled domain events that will be published through the event bus.
- Interface for the event bus and subscriber.
- Concrete implementation of the event bus using RabbitMQ

### AI Agents

This feature sets up a complete environment for AI-assisted software development by including an `AGENTS.md` file with project
rules, a collection of specialized agents for orchestrating development phases, skills for common tasks, and commands for
recurring workflows. When selected, it creates the following structure in your project:

```
├── AGENTS.md
├── docs
│   ├── conventions
│   │   └── testing
│   │       └── tdd_outside_in.md
│   ├── specs
│   ├── agents
│   │   ├── convention_guidelines.md
│   │   ├── leader_workflow.md
│   │   └── spec_guidelines.md
│   ├── progress
│   └── tasks.json
└── .agents
    ├── agents
    │   ├── convention_keeper.md
    │   ├── judge.md
    │   ├── leader.md
    │   ├── spec_partner.md
    │   └── tdd_craftsman.md
    ├── commands
    │   ├── commit.md
    │   └── technical_debt_review.md
    └── skills
        ├── code_review
        ├── complexity_review
        ├── hamburger_method
        ├── micro_steps_coach
        ├── mutation_testing
        ├── security_review
        ├── story_splitting
        ├── test_desiderata
        └── xp_refactor
```

The generated `AGENTS.md` includes a **repository knowledge map** that lists every documentation area — conventions,
specs, progress logs, and agent guidelines — so agents know where to read and write information. Subagent prompts
instruct agents to read this map first for orientation.

#### Two Workflows

This feature supports two usage modes. You can use one, both, or neither — they are independent.

**1. Skills & Commands (manual workflow):** Use the [skills](#skills) and [commands](#commands) directly with any AI agent. These are general-purpose tools for code review, refactoring, commit organization, security analysis, story splitting, and more. No subagents required. Open a chat and invoke a skill or command by name.

**2. Agent harness (pipeline workflow):** Use the [orchestration agents](#orchestration-agents) for a structured development pipeline where each phase (spec → TDD → review → conventions) is handled by a specialized subagent. This requires invoking the `leader` subagent.

!!! tip "Subagents are optional"
    The agent harness subagents are **not mandatory**. You can use just the skills and commands without ever invoking a subagent, combine 
    them as needed, or ignore the entire harness and use only `AGENTS.md` as a project rules reference.

#### Task Management

!!! info "Default local task management"
    By default, `instant-python` will use a local system to track tasks so users do not
    require setting up any external tooling. This can be easily changed to use a remote system
    such as Jira, GitHub, Linear, etc.

Features are tracked through `docs/tasks.json` which defines the project's task queue:

```json
{
  "project": "<project-name>",
  "description": "<project-description>",
  "rules": {
    "one_feature_at_a_time": true,
    "require_tests_to_close": true,
    "require_approved_spec_to_implement": true,
    "valid_status": ["pending", "spec_ready", "in_progress", "done", "blocked"],
    "sdd_required_when": "feature has \"sdd\": true"
  },
  "tasks": []
}
```

Valid statuses: `pending` → `spec_ready` → `in_progress` → `done` (or `blocked`).

Features flagged with `"sdd": true` must go through the spec conversation (see [Orchestration Agents](#orchestration-agents)) before any
code is written. The `spec_partner` slices the feature into nested `subtasks` inside `docs/tasks.json` (dot-separated ids such as
`feature`, `feature.1`, `feature.1.2`), so the feature stays the parent task of its sliced pieces.

#### Orchestration Agents

!!! warning "Personal Starting Point"
    This agent harness is extremely personal and reflects specific development preferences. You are expected to customize
    the agents, skills, commands, and prompts to match your own workflow. Treat it as a starting point, not a definitive setup.

The development pipeline is coordinated by a leader agent and executed by specialized subagents:

| Agent                 | Role                                                           |
|-----------------------|----------------------------------------------------------------|
| **leader**            | Orchestrates the full pipeline; never writes code or tests     |
| **spec_partner**      | Debates and distills specs into `docs/specs/<name>.md` with EARS requirements and slices tasks |
| **tdd_craftsman**     | Implements one feature by strict Outside-In TDD                |
| **judge**             | Reviews code and runs mutation testing; approves or rejects    |
| **convention_keeper** | Captures learnings into reusable convention docs               |

!!! info "Manual Invocation Required"
    Subagents are not triggered automatically. You must manually invoke the `leader` agent using the `/agent` command
    in opencode to start the development pipeline. The leader will then delegate to the appropriate subagents.

#### Skills

Each skill provides detailed instructions for an AI agent to perform a specific task effectively.

| Skill                   | When to use                                                                                   | What it does                                                                                                       |
|-------------------------|-----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| **code_review**         | Reviewing pending, uncommitted changes                                                        | Reviews test quality, maintainability, simplicity, and alignment with project rules and standards                 |
| **complexity_review**   | Evaluating technical solutions or designs; proposing system architectures                     | Questions every complexity driver, proposes progressively simpler alternatives, identifies what can be postponed   |
| **hamburger_method**    | Breaking down large features into layers; composing minimal vertical slices                   | Applies the Hamburger Method to slice features into vertical deliverable pieces                                    |
| **micro_steps_coach**   | Facing large refactorings; making breaking changes                                            | Breaks down work into 1-3 hour micro-steps, applies expand-contract pattern for safe changes                       |
| **mutation_testing**    | Analyzing test effectiveness; validating refactoring                                          | Runs mutation testing with `mutmut`, analyzes surviving mutants to identify weak tests and missing edge cases     |
| **security_review**     | Analyzing code, architecture, or system security                                              | Performs pragmatic risk analysis identifying real vulnerabilities and lightweight, high-value mitigations         |
| **story_splitting**     | Stories that feel too large or vague; multiple features bundled together                      | Detects oversized stories and applies splitting heuristics                                                         |
| **test_desiderata**     | Analyzing test files; reviewing test quality                                                  | Evaluates tests across 12 quality dimensions using Kent Beck's Test Desiderata framework                           |
| **xp_refactor**         | Cleaning up existing code; reducing duplication                                               | Applies XP Simple Design principles, prioritizes refactors by ROI                                                  |

#### Commands

Commands define recurring workflows that an AI agent can execute on demand.

| Command                     | Description                                                                                                                  |
|-----------------------------|------------------------------------------------------------------------------------------------------------------------------|
| **commit**                  | Splits uncommitted changes into atomic conventional commits with user confirmation before each decision                      |
| **technical_debt_review**   | Identifies and prioritizes technical debt in the codebase including code smells, weak tests, and outdated dependencies       |
