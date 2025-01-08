<div align="center">
  <h1>⚡️ Instant Boilerplate for Python SaaS ⚡️</h1>
  <strong>Start your Python project right away</strong>
</div>

<p align="center">
  <a href="#requirements">Requirements</a>&nbsp;&nbsp;•&nbsp;
  <a href="#use">How To Use</a>&nbsp;&nbsp;•&nbsp;
  <a href="#options">Customization options</a>&nbsp;&nbsp;•&nbsp;
</p>

## Resources

This template is inspired by pmareke repository. You can find his template in the link bellow:

[![Web](https://img.shields.io/badge/GitHub-pmareke-14a1f0?style=for-the-badge&logo=github&logoColor=white&labelColor=101010)](https://github.com/pmareke/fastapi-boilerplate)

<a name=requirements></a>
## Requirements

This project allows you to work with different Python versions. All of them are managed using [pyenv](https://github.com/pyenv/pyenv), so
before using this template you should follow these steps:

1. Install pyenv:
    ```bash
    curl https://pyenv.run | bash
    ```

2. Set you bash profile to load pyenv. In my case I use fish:

    ```bash
    set -Ux PYENV_ROOT $HOME/.pyenv
    fish_add_path $PYENV_ROOT/bin
   ```
   
    Then, add the following line to `~/.config/fish/config.fish`:

    ```bash
    echo pyenv init - | source >> ~/.config/fish/config.fish
    ```

> [!NOTE]
> If you are using a different shell, please follow the instructions in the [pyenv documentation](https://github.com/pyenv/pyenv?tab=readme-ov-file#b-set-up-your-shell-environment-for-pyenv)


<a name=use></a>
## How To Use

In order to use this template and start your project follow these steps:

1. Install [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/installation.html)
    ```bash
    pip install --user cookiecutter
    ```
2. Get the url of the template repository and run:
    ```bash
    cookiecutter gh:dimanu-py/python-skeleton
   ```
3. Answer the questions to customize your project.
4. Run the `make local-setup` command to be able to run the hooks inside [hooks](./domain_driven_design/{{cookiecutter.project_slug}}/scripts/hooks) folder.

> [!NOTE]
> If you want to ignore the hooks folder, you can remove it and just run `make install` command.

5. Happy coding


<a name=options></a>
## Customization Options: What this template offers

The template offers some customization options that you can choose when you first run the `cookiecutter` command.


### Project Structure

First of all, it will ask you to decide if you want to use a [Domain Driven Design](https://medium.com/@jonathanloscalzo/domain-driven-design-principios-beneficios-y-elementos-primera-parte-aad90f30aa35)
approach or just a simpler approach with a _src_ and _tests_ folders.

<details><summary>Simple Approach</summary>

This template will create a simple project structure with the following folders:

- The [`src`](./standard/{{cookiecutter.project_slug}}/src) folder contains the production code.
- The [`tests`](./standard/{{cookiecutter.project_slug}}/tests) folder contains the tests for the production code.

> [!NOTE]
> This approach is recommended for simple projects or when you are not sure what kind of architecture you will follow.
> It will just create the typical folders for you to get started with your project.

</details>

<details><summary>Domain Driven Design</summary>

This template will create a more complex project structure following DDD principles. The folder hierarchy will follow vertical slicing
and scream architecture to explode domain language in the project. The following folders will be created:
```text
├── Makefile
├── mypy.ini
├── pyproject.toml
├── pytest.ini
├── scripts
├── src
│  ├── contexts
│  │  ├── shared
│  │  └── bounded_context_name
│  │     ├── shared
│  │     └── aggregate_name
│  │        ├── application
│  │        ├── domain
│  │        └── infra
│  └── delivery
└── tests
   ├── contexts
   │  └── bounded_context_name
   │     ├── shared
   │     └── aggregate_name
   │        ├── application
   │        ├── domain
   │        └── infra
   └── delivery
```

The production code goes inside the [`src`](./domain_driven_design/{{cookiecutter.project_slug}}/src) folder. Which is divided into two main folders:
- The [`contexts`](./domain_driven_design/{{cookiecutter.project_slug}}/src/contexts) folder will contain all the bounded contexts of the application:
    - Each [`bounded context`](./domain_driven_design/{{cookiecutter.project_slug}}/src/contexts/{{cookiecutter.bounded_context_name}}) has the main business logic of a specific domain.
      Inside each bounded context you will find one or more aggregates that represent a specific part of the domain. Each module is divided into
      the following subfolders:
        - The [`domain`](./domain_driven_design/{{cookiecutter.project_slug}}/src/contexts/{{cookiecutter.bounded_context_name}}/{{cookiecutter.aggregate_name}}/domain) folder contains the business rules, entities and value objects.
        - The [`application`](./domain_driven_design/{{cookiecutter.project_slug}}/src/contexts/{{cookiecutter.bounded_context_name}}/{{cookiecutter.aggregate_name}}/application) folder contains use cases and handlers
        - The [`infra`](./domain_driven_design/{{cookiecutter.project_slug}}/src/contexts/{{cookiecutter.bounded_context_name}}/{{cookiecutter.aggregate_name}}/infra) folder contains the implementation of the interfaces defined in the domain
          for I/O operations like database, buses etc.
            - The [`shared`](./domain_driven_design/{{cookiecutter.project_slug}}/src/contexts/{{cookiecutter.bounded_context_name}}/shared) folder contains code that is shared across multiple modules of the bounded context.
    - The [`shared`](./domain_driven_design/{{cookiecutter.project_slug}}/src/contexts/shared) folder contains code that is shared across multiple bounded contexts.
- The [`delivery`](./domain_driven_design/{{cookiecutter.project_slug}}/src/delivery) folder contains the entry points of the application, these would be your API controllers, web frontend,
  mobile frontend, etc.

The [`tests`](./domain_driven_design/{{cookiecutter.project_slug}}/tests) folder follows a similar structure to the production code.
- The [`contexts`](./domain_driven_design/{{cookiecutter.project_slug}}/tests/contexts) folder contains the tests for the main business logic of the application. It follows the same structure
as the production code, separating the bounded contexts into different folders and modules. Each module will contain tests that represent the
following:
    - The [`domain`](./domain_driven_design/{{cookiecutter.project_slug}}/tests/contexts/{{cookiecutter.bounded_context_name}}/{{cookiecutter.aggregate_name}}/domain) folder should contain mother objects and tests for the entities and value objects.
    - The [`application`](./domain_driven_design/{{cookiecutter.project_slug}}/tests/contexts/{{cookiecutter.bounded_context_name}}/{{cookiecutter.aggregate_name}}/application) folder should contain tests for the use cases and handlers.
    - The [`infra`](./domain_driven_design/{{cookiecutter.project_slug}}/tests/contexts/{{cookiecutter.bounded_context_name}}/{{cookiecutter.aggregate_name}}/infra) folder should contain tests for the implementation of the interfaces defined in the domain.
- The [`delivery`](./domain_driven_design/{{cookiecutter.project_slug}}/tests/delivery) folder should contain the acceptance or end-to-end tests.

</details>

### Script Utilities and Makefile

The template will create a [Makefile](./domain_driven_design/{{cookiecutter.project_slug}}/Makefile) that contains some useful commands 
to avoid writing repetitive commands. 

> [!IMPORTANT]
> Depending on the project structure you choose, the Makefile will contain different commands. Typically, 
> for a standard project the Makefile will contain fewer commands.

<details><summary>Complete list of Make commands</summary>

- `help`: shows all the available commands
- `test`: runs all the tests
- `unit`: detects changes on domain or application changes and runs the bounding context corresponding tests
- `all-unit`: runs all domain and application tests in all bounded contexts. **These tests must be marked as unit tests**
- `integration`: detects changes on infra and runs the bounding context corresponding tests
- `all-integration`: runs all infra tests in all bounded contexts. **These tests must be marked as integration tests**
- `all-acceptance`: runs all acceptance tests
- `coverage`: runs all the tests with coverage
- `local-setup`: sets up the local environment
- `install`: installs all dependencies
- `update`: updates dependencies
- `add-dep`: installs a new dependency. Asks for the dependency name, if it's a dev dependency or not and its group.
- `remove-dep`: removes a dependency. Asks for the dependency name and its group.
- `check-typing`: runs static type checking with mypy
- `check-lint`: checks linting with ruff
- `lint`: lints the code with ruff
- `check-format`: check formats with ruff
- `format`: formats the code with ruff
- `pre-commit`: runs the pre-commit checks (check types, checks linting, checks format and runs all unit tests)
- `pre-push`: runs integration and acceptance tests
- `watch`: runs a watch session to run all the tests on file changes
- `insert-template`: inserts one of the templates classes in a desired file.
- `create-aggregate`: generates all the hexagonal architecture folder structure for a new aggregate in both src and tests folders.
- `show`: shows all dependencies installed
- `search`: show information about the specified package

</details>

On the other hand, the template will contain a [scripts](./domain_driven_design/{{cookiecutter.project_slug}}/scripts) folder that contains 
some utilities to help you with your project. 

> [!IMPORTANT]
> As in the Makefile, the scripts available will depend on the project structure you choose. Typically, 
> for a standard project the scripts will be fewer.

<details><summary>List of available scripts</summary>

- Hooks folder with scripts related to git hooks.
- Templates folder with some useful classes that you can use with the `insert-template` command. The script [`insert_template.py`](./domain_driven_design/{{cookiecutter.project_slug}}/scripts/insert_template.py)
is the script that will be executed.
- Tests folder with some scripts to be able to execute the test only of the files that have changed. The commands `unit` and `integratio`
depend on these scripts.
- Scripts to add and remove dependencies in the project in an interactive way.
- Script to create a new aggregate following the hexagonal architecture.

</details>

### Dependencies

The template can work with either [pdm](https://pdm-project.org/en/latest/) or [uv](https://docs.astral.sh/uv/) dependency managers.

With either dependency manager, the template will allow you to install some default dependencies. Additionally, it will ask you if you
want to install any other dependencies. The following dependencies are available by default:

<details><summary>Testing</summary>

- [pytest](https://docs.pytest.org/en/stable/): testing runner.
- [pytest-xdist](https://pypi.org/project/pytest-xdist/): pytest plugin to run the tests in parallel.
- [expects](https://pypi.org/project/expects/): an expressive assertion library for Python.
- [doublex](https://pypi.org/project/doublex/): a test doubles library for Python.
- [doublex-expects](https://pypi.org/project/doublex-expects/): a plugin for doublex that integrates with expects.
- [coverage](https://pypi.org/project/coverage/): a code coverage tool.

</details>

<details><summary>Code Style</summary>

- [mypy](https://github.com/python/mypy): a static type checker.
- [yapf](https://github.com/google/yapf): a Python formatter.
- [ruff](https://github.com/astral-sh/ruff): a Python linter and formatter.

</details>

### Out of the Box Implementations

If you choose the DDD approach, the template contains some out of the box implementations that are typical in complex projects. The following
classes will be implemented in the [`shared`](./domain_driven_design/{{cookiecutter.project_slug}}/src/contexts/shared) folder:

- `ValueObject`: base value object class that uses generic types to ensure correct type definition and encapsulates common behaviors.
- `StringValueObject`: implementation of value object for strings, typical for any text value object.
- `Uuid`: implementation of value object for UUIDs, typical for any UUID value object.
- `IncorrectValueTypeError`: custom exception for incorrect value types.
- `RequiredValueError`: custom exception when no value is passed to any value object.