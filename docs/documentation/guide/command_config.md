`instant-python` relies on a YAML file to know how your project should be generated. 
This configuration file must exist before running the [init] command in order to be able to create your
project.

!!! note "Prerequisites"
    Before running the `ipy config` command, make sure you have `instant-python` [installed](../getting_started/installation.md).

## Quick Navigation

- [Overview](#overview) - What the config command does
- [Usage](#usage) - How to run the config command
- [JSON Schema Support](#json-schema-support) - IDE autocompletion and validation
- [Configuration File Structure](#configuration-file-structure-and-restrictions) - All available options and their restrictions
    - [General](#general) - Project metadata
    - [Template](#template) - Project structure and features
    - [Git](#git) - Version control setup
    - [Dependencies](#dependencies) - Initial dependencies to install

## Overview

The command performs the following actions:

1. Creates an interactive wizard that asks you different questions about your project.
2. Generates an **ipy.yml** configuration file based on your answers.
3. Saves the configuration file in the current directory.

## Usage

You can create the configuration in two different ways: using the `config` command or writing it manually.

!!! tip "Use the config command to avoid unexpected errors"
    Although it's possible to create the configuration file manually, we recommend using the `config` command
    to avoid mistakes.

The `config` command walks you through an interactive wizard and produces the configuration file for you.
Running it will create an **ipy.yml** file in the current directory containing all your answers.

```bash
ipy config
```

The help message of the command provides more information about its usage and available options:

```bash
ipy config --help
```

## Configuration File Structure and Restrictions

The interactive wizard will ask you different questions to fill the following sections of the configuration file: [`general`](#general), 
[`template`](#template), [`git`](#git) and [`dependencies`](#dependencies).

!!! warning "Missing top level keys"
    If the configuration file is missing any of the top level keys, the [init] command will raise an error.
    Additionally, if some of the fields marked as _required_ is missing, the command will also raise an error.

### General

This section of the configuration file contains general information about the project to be created.

It has the following fields and restrictions:

| Field                       | Description                                        | Restrictions | Required |
|-----------------------------|----------------------------------------------------|--------------| ---------|
| `slug`                      | The name of your project folder and package.       | Cannot contain spaces or special characters, must fulfill toml specifications. | Yes |
| `source_name`               | The folder where your source code will be located. |    | Yes |
| `description`               | A short description of your project.               |    | Yes |
| `version`                   | The initial version of your project.               | |   Yes |
| `author`                    | The author of the project.                         |    | Yes |
| `license`                   | The license of the project.                        | Must be one of: `MIT`, `Apache` or `GPL`. | Yes |
| `python_version`            | The Python version to use in the project.          | Must be one of: `3.10`, `3.11`, `3.12` or `3.13`. | Yes |
| `dependency_manager`        | The project manager to use.                 | Must be either `uv`. | Yes |

### Template

This section of the configuration file contains information about the project structure and the built‑in features
to include in the project.

The library provides three built-in project structures: `standard`, `domain_driven_design` and `clean_architecture` and 
a list of different out-of-the-box implementation that you can select to be included in your project.

For a detail explanation of each project structure visit the [Default Project Structures], and for a detailed explanation
of each built-in feature visit the [Out-of-the-box Implementations] section.

| Field               | Description                                                               | Restrictions                                                                          | Required              |
|---------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------------------------|-----------------------|
| `specify_bounded_context` | Whether to specify a bounded context and aggregate root name. | Only available when the template is `domain_driven_design`.                           | No                    |
| `bounded_context`   | The name of the bounded context.                                          | Required if `specify_bounded_context` is `true`.                                      | Based on restrictions |
| `aggregate_name`    | The name of the aggregate root.                                          | Required if `specify_bounded_context` is `true`.                                      | Based on restrictions |
| `built_in_features` | A list of built-in features to include in the project.                          | Must be a list of features available at [Out-of-the-box Implementations]              | No |

### Git

This section of the configuration file contains information about Git initialization. You can decide whether to
initialize a Git repository in the project folder and provide your Git username and email.

| Field          | Description                                      | Restrictions                     | Required |
|----------------|--------------------------------------------------|----------------------------------|----------|
| `username`    | The Git username to set in the repository.        | Required if `initialize` is `true`. | Based on restrictions |
| `email`       | The Git email to set in the repository.           | Required if `initialize` is `true`. | Based on restrictions |

### Dependencies

In this section of the configuration file you can define the initial dependencies to install in the project.
If you don't want to install any dependencies, you can leave the `dependencies` section empty. But it's important
to keep the section in the file.

Each dependency can have the following fields and restrictions:

| Field        | Description                                      | Restrictions                               | Required              |
|--------------|--------------------------------------------------|--------------------------------------------|-----------------------|
| `name`       | The name of the dependency to install.           | Must be a valid Python package name.       | Yes                   |
| `version`    | The version of the dependency to install.        | Must be a valid version or `latest`         | Yes                   |
| `development` | Whether the dependency is a development dependency. | Must be either `true` or `false`.          | No                    |
| `group`      | The development dependency group.                 | Only available if `development` is `true`. | Based on restrictions |

## JSON Schema Support

`instant-python` provides a JSON Schema to help you write and validate your configuration files with autocompletion and validation in your IDE.

### What is a JSON Schema?

A JSON Schema is a specification that defines the structure and validation rules for JSON and YAML files. By using a schema, your IDE can:

- **Autocomplete** field names and values
- **Validate** your configuration in real-time
- **Show inline documentation** for each field
- **Detect errors** before running the command

### How to Use the Schema

The schema is available at:
```
https://raw.githubusercontent.com/dimanu-py/instant-python/main/schemas/ipy-schema.json
```

!!! tip "Schema autodetection"
If your configuration file is named `ipy.yml`, some IDEs may automatically detect and apply the schema
from [SchemaStore](https://www.schemastore.org/). However, as it may take some time to updated and listed there,
we recommend configuring it manually to ensure you are using the latest version.

#### For Visual Studio Code

Add the following line at the top of your `ipy.yml` file:

```yaml
# yaml-language-server: $schema=https://raw.githubusercontent.com/dimanu-py/instant-python/main/schemas/ipy-schema.json

general:
  slug: my-project
  # ...
```

Alternatively, you can configure it globally in your VS Code settings (`.vscode/settings.json`):

```json
{
  "yaml.schemas": {
    "https://raw.githubusercontent.com/dimanu-py/instant-python/main/schemas/ipy-schema.json": "ipy.yml"
  }
}
```

#### For PyCharm / IntelliJ IDEA

1. Open your `ipy.yml` file
2. At the top of the file, add:
   ```yaml
   # yaml-language-server: $schema=https://raw.githubusercontent.com/dimanu-py/instant-python/main/schemas/ipy-schema.json
   ```
3. PyCharm will automatically detect and use the schema

Alternatively, you can configure it manually:

1. Go to **Settings** → **Languages & Frameworks** → **Schemas and DTDs** → **JSON Schema Mappings**
2. Click the **+** button to add a new mapping
3. Set the **Schema URL** to: `https://raw.githubusercontent.com/dimanu-py/instant-python/main/schemas/ipy-schema.json`
4. Add a file pattern: `ipy.yml`

## Configuration File Examples

### Without initializing a git repository

In this example we create:

- A standard project without any built-in features
- No git repository
- No dependencies

```yaml
general:
  slug: python-project
  source_name: src
  description: Python Project Description
  version: "0.1.0"
  author: John Doe
  license: MIT
  python_version: "3.13"
  dependency_manager: uv
git:
  initialize: false
dependencies:
template:
  name: standard_project
```

### Initializing a git repository

In this example we create:

- A standard project without any built-in features
- A git repository with username and email
- No dependencies

```yaml
general:
  slug: python-project
  source_name: src
  description: Python Project Description
  version: "0.1.0"
  author: John Doe
  license: MIT
  python_version: "3.13"
  dependency_manager: uv
git:
  initialize: true
  username: johndoe
  email: johndoe@gmail.com
dependencies:
template:
  name: standard_project
```

### Domain Driven Design without specifying bounded context

In this example we create:

- A domain driven design project without specifying bounded context
- A git repository with username and email
- No dependencies
- No built-in features

```yaml
general:
  slug: python-project
  source_name: src
  description: Python Project Description
  version: "0.1.0"
  author: John Doe
  license: MIT
  python_version: "3.13"
  dependency_manager: uv
git:
  initialize: true
  username: johndoe
  email: johndoe@gmail.com
dependencies:
template:
  name: domain_driven_design
  specify_bounded_context: false
```

### Domain Driven Design specifying bounded context

In this example we create:

- A domain driven design project specifying bounded context, and therefore providing bounded context and aggregate name
- A git repository with username and email
- No dependencies
- No built-in features

```yaml
general:
  slug: python-project
  source_name: src
  description: Python Project Description
  version: "0.1.0"
  author: John Doe
  license: MIT
  python_version: "3.13"
  dependency_manager: uv
git:
  initialize: true
  username: johndoe
  email: johndoe@gmail.com
dependencies:
template:
  name: domain_driven_design
  specify_bounded_context: true
  bounded_context: backoffice
  aggregate_name: user
```

### Selecting built-in features

In this example we create:

- A clean architecture project
- A git repository with username and email
- No dependencies
- Some built-in features

```yaml
general:
  slug: python-project
  source_name: src
  description: Python Project Description
  version: "0.1.0"
  author: John Doe
  license: MIT
  python_version: "3.13"
  dependency_manager: uv
git:
  initialize: true
  username: johndoe
  email: johndoe@gmail.com
dependencies:
template:
  name: clean_architecture
  built_in_features:
    - value_objects
    - github_actions
    - makefile
```

### Installing dependencies

In this example we create:

- A standard project with some built-in features
- A git repository with username and email
- Some dependencies to install, both for development and production
- Some built-in features

```yaml
general:
  slug: python-project
  source_name: src
  description: Python Project Description
  version: "0.1.0"
  author: John Doe
  license: MIT
  python_version: "3.13"
  dependency_manager: uv
git:
  initialize: true
  username: johndoe
  email: johndoe@gmail.com
dependencies:
  - name: ty
    version: latest
    is_dev: true
    group: lint
  - name: pytest
    version: latest
    is_dev: true
    group: test
  - name: fastapi
    version: latest
template:
  name: standard_project
  built_in_features:
    - value_objects
    - github_actions
    - makefile
```

[init]: command_init.md
[Default Project Structures]: default_features.md#default-project-structures
[Out-of-the-box Implementations]: default_features.md#out-of-the-box-implementations