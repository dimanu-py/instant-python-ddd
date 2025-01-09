# Customization Before Using

The template will prompt some questions to customize our project. The different options and decisions we will be making are described bellow.

## Project Structure

Depending on your choice during the setup, your project structure will look like this:

### Standard Approach

This approach is recommended for simple projects or when you are not sure what kind of architecture you will follow.
It will just create the typical folders for you to get started with your project.

```
├── Makefile
├── mypy.ini
├── pyproject.toml
├── scripts
├── src
└── tests
```

### DDD Approach

This template will create a more complex project structure following DDD principles. The folder hierarchy will follow vertical slicing
and scream architecture to explode domain language in the project. The following folders will be created:

```
├── Makefile
├── mypy.ini
├── pyproject.toml
├── scripts
├── src
│  ├── contexts
│  │  └── bounded_context_name
│  │     ├── application
│  │     ├── domain
│  │     └── infra
└── tests
   └── contexts
      └── bounded_context_name
```

The production code goes inside the _src_ folder. Which is divided into two main folders:
- The _contexts_ folder will contain all the bounded contexts of the application:
    - Each _bounded context_ has the main business logic of a specific domain.
      Inside each bounded context you will find one or more aggregates that represent a specific part of the domain. Each module is divided into
      the following subfolders:
        - The _domain_ folder contains the business rules, entities and value objects.
        - The _application_ folder contains use cases and handlers
        - The _infra_ folder contains the implementation of the interfaces defined in the domain
          for I/O operations like database, buses etc.
            - The _shared_ folder contains code that is shared across multiple modules of the bounded context.
    - The _shared_ folder contains code that is shared across multiple bounded contexts.
- The _delivery_ folder contains the entry points of the application, these would be your API controllers, web frontend,
  mobile frontend, etc.

The _tests_ folder follows a similar structure to the production code.
- The _contexts_ folder contains the tests for the main business logic of the application. It follows the same structure
  as the production code, separating the bounded contexts into different folders and modules. Each module will contain tests that represent the
  following:
    - The _domain_ folder should contain mother objects and tests for the entities and value objects.
    - The _application_ folder should contain tests for the use cases and handlers.
    - The _infra_ folder should contain tests for the implementation of the interfaces defined in the domain.
- The _delivery_ folder should contain the acceptance or end-to-end tests.

---

## Script Utilities and Makefile

### Make Commands

The template includes a _Makefile_ to automate common tasks. Here are some useful commands:

```{important}
The commands available will depend on the project structure you choose. Typically,
for a standard project the makefile will containe fewer commands.
```

| Command         | Description                           |
|-----------------|---------------------------------------|
| `make help`     | Show available commands                |
| `make test`     | Run all tests                          |
| `make unit`     | Run unit tests for changed files       |
| `make all-unit`  | Run all unit tests                    |
| `make integration` | Run integration tests for changed files |
| `make all-integration` | Run all integration tests          |
| `make all-acceptance` | Run all acceptance tests            |
| `make coverage` | Run coverage tests                     |
| `make install`  | Install all dependencies               |
| `make update` | Update all dependencies                |
| `make clean`    | Clean up the project                   |
| `make add-dep`  | Add a new dependency                   |
| `make remove-dep` | Remove a dependency                  |
| `make format`   | Format code with Ruff                  |
| `make lint`     | Lint code with Ruff                    |
| `make local-setup` | Set up the local development environment |

### Scripts Utilities

On the other hand, the template will contain a _scripts_ folder that contains
some utilities to help you with your project.

```{important}
The scripts available will depend on the project structure you choose. Typically,
for a standard project the scripts will be fewer.
```

- Hooks folder with scripts related to git hooks.
- Templates folder with some useful classes that you can use with the `insert-template` command. The script *insert_template.py*
  is the script that will be executed.
- Tests folder with some scripts to be able to execute the test only of the files that have changed. The commands `unit` and `integratio`
  depend on these scripts.
- Scripts to add and remove dependencies in the project in an interactive way.
- Script to create a new aggregate following the hexagonal architecture.

---

## Out of the Box Features

If you choose the DDD approach, the template contains some out of the box implementations that are typical in complex projects. You
will find the following implementations under the _shared_ folder inside _contexts_:

- Common value objects that are used across multiple bounded contexts: `ValueObject` base class, `StringValueObject`, `Uuid` etc.
- Common custom exceptions related to these general value objects: `IncorrectValueTypeError`, `RequiredValueError` etc.
- Basic implementation of SQLAlchemy for database operations.

---

## Dependencies

The template can work with either [pdm](https://pdm-project.org/en/latest/) or [uv](https://docs.astral.sh/uv/) dependency managers.

With either dependency manager, the template will allow you to install some default dependencies. Additionally, it will ask you if you
want to install any other dependencies. The following dependencies are available by default:

### Testing

- [pytest](https://docs.pytest.org/en/stable/): testing runner.
- [pytest-xdist](https://pypi.org/project/pytest-xdist/): pytest plugin to run the tests in parallel.
- [expects](https://pypi.org/project/expects/): an expressive assertion library for Python.
- [doublex](https://pypi.org/project/doublex/): a test doubles library for Python.
- [doublex-expects](https://pypi.org/project/doublex-expects/): a plugin for doublex that integrates with expects.
- [coverage](https://pypi.org/project/coverage/): a code coverage tool.

### Code Style

- [mypy](https://github.com/python/mypy): a static type checker.
- [yapf](https://github.com/google/yapf): a Python formatter.
- [ruff](https://github.com/astral-sh/ruff): a Python linter and formatter.
