# New Tool Management System

## Purpose

Redefine how `instant-python` handles dependency managers, tool versions, and task runners in generated projects: `uv` becomes the only dependency manager, tool versions are managed either by `mise` or by external installation, and the `makefile` task runner is replaced by `taskfile` or native mise tasks.

## Behavior

The configuration wizard asks the following questions in order:

1. **Tool version manager**: how the user wants to manage tool versions (`mise` or `external`).
   - `mise`: the generated project declares its tools in `mise.toml`. During initialization, `instant-python` installs `mise` if it is not present, installs the declared tools (Python, `uv`, and optionally `task`), and then creates the virtual environment and installs dependencies with the `uv` provided by `mise`.
   - `external`: the current flow is kept. `instant-python` installs `uv` through its official installer if it is not present, installs the Python version through `uv`, generates `.python-version`, and installs dependencies as today.
2. **Task runner**: how the user wants to run project tasks. This question is asked **after** the built-in features selection, because selecting `github_actions` pre-selects `taskfile` as the default answer (mirroring today's behavior where `github_actions` always ships a makefile).
   - When `mise` was selected: the user chooses between **native mise tasks** or **taskfile** (no "none" option is offered in this flow).
     - Native mise tasks: the commands previously shipped in the makefile are written into the `[tasks]` section of `mise.toml`.
     - Taskfile: `task` is pinned to `latest` in `mise.toml` and installed, and a `taskfile.yml` file is generated with the same commands the makefile used to provide.
   - When `external` was selected: **taskfile** is the default. The user is asked whether they want to keep it; if they decline, no task runner is generated (`task_runner = "none"`). In this flow `instant-python` does **not** install the `task` binary; the user installs it themselves, which is consistent with the `external` contract of letting the user manage tools.
   - Task commands are OS-independent: when a task's command needs platform-specific shell syntax (e.g. `rm --force`, `find`, `grep`/`awk`, `ln -sf`, `read -p`), the logic is extracted into a Python helper script that detects the platform and runs the correct command. This applies to both native mise tasks and `taskfile`, so neither runner has a Windows limitation.

The `makefile` is removed as a built-in feature and no generated project contains a makefile anymore. The dependency manager question is removed from the wizard because `uv` is the only supported value; the wizard sets `dependency_manager` to `uv` without asking.

### Configuration model

New fields in the `general` section of the configuration file (`ipy.yml`):

- `tool_version_manager`: `mise` | `external`
- `task_runner`: `none` | `taskfile` | `mise` (where `mise` means native mise tasks)

`dependency_manager` remains in `general` but only accepts `uv`.

## Contract

- **Inputs** (`general` section):
  - `dependency_manager`: enum, only `"uv"`.
  - `tool_version_manager`: enum, `"mise"` or `"external"` — **required**.
  - `task_runner`: enum, `"none"`, `"taskfile"` or `"mise"` — **required**.
- **Cross-field constraint**: `task_runner == "mise"` is only valid when `tool_version_manager == "mise"`. With `tool_version_manager == "external"`, only `"none"` and `"taskfile"` are valid. `task_runner == "none"` combined with `tool_version_manager == "mise"` is valid at the configuration level even though the wizard never offers it.
- **Outputs** (generated project):
  - Always: `uv`-based `pyproject.toml` and virtual environment setup.
  - When `tool_version_manager == "mise"`: `mise.toml` with `[tools]` (`python` pinned to the selected version, `uv = "latest"`); no `.python-version`.
  - When `tool_version_manager == "external"`: `.python-version`; current `uv` installer flow; when `task_runner == "taskfile"` the `task` binary is NOT installed by `instant-python`.
  - When `task_runner == "taskfile"`: `taskfile.yml`; when combined with `mise`, `task = "latest"` is added to `[tools]` in `mise.toml`.
  - When `task_runner == "mise"`: `[tasks]` section inside `mise.toml`; no `taskfile.yml`.
  - When `task_runner == "none"`: no task file is generated.
  - Never: a `makefile`.

## Edge Cases

- `task_runner == "mise"` with `tool_version_manager == "external"`: rejected at configuration validation with a clear error message explaining that native mise tasks require the `mise` tool version manager.
- `dependency_manager` value other than `"uv"` (e.g. legacy `"pdm"` config files): rejected at validation with a clear error message telling the user `uv` is the only supported manager.
- Legacy config files that still list `makefile` in `template.built_in_features`: rejected at validation with an error message referencing the task runner configuration.
- Legacy config files that omit the new `tool_version_manager` and `task_runner` fields: rejected at validation with an error directing the user to re-run `ipy config`.
- `mise` not installed on the machine: `instant-python` installs it through the official installer before installing the declared tools.
- `github_actions` selected together with `task_runner == "none"`: the CI workflow is generated using raw `uv`/`uvx` commands instead of task-runner commands, so the pipeline still works without a task runner.
- `github_actions` selected and `task_runner` not decided yet: the task runner question is asked after the built-in features selection and defaults to `taskfile`, mirroring today's behavior where `github_actions` always ships a makefile.
- `github_actions` selected together with `tool_version_manager == "mise"`: the GitHub action setup step installs `mise` and lets it provide Python and `uv`; `actions/setup-python` is not used in this path.
- `precommit_hook` selected together with `task_runner == "none"`: the local lint and format hooks in `.pre-commit-config.yaml` are rendered with raw `uv`/`uvx` commands, so the hooks keep working without a task runner.
- `precommit_hook` selected together with an active task runner: the local lint and format hooks invoke the selected runner (`task check-lint` / `mise run check-lint`).
- Task runner selection offers no "both" option: native mise tasks and taskfile are mutually exclusive.
- The mise flow never offers `"none"` as a task runner option, but a hand-written config with `tool_version_manager == "mise"` and `task_runner == "none"` is valid and generates no task file.
- Dev-dependency and tool gating in `pyproject.toml` is currently keyed on the `makefile` built-in feature (`["github_actions", "makefile", "precommit_hook"]`); with the feature removed, the same gating must be keyed on an active task runner, otherwise a `taskfile.yml` (or native mise tasks) would reference tools that are not declared as dev dependencies.
- Windows: both `taskfile` and native mise tasks run on Windows because every task command that relies on unix-only syntax (`rm --force`, `find`, `grep`/`awk`, `ln -sf`, `read -p`) is implemented through a Python helper script that detects the platform and runs the correct command. No POSIX shell is required.
- `scripts/pre-commit.py`, `scripts/pre-push.py` and `scripts/post-merge.py` in the boilerplate invoke `make` (`make pre-commit`, `make pre-push`, `make build`, `make install`) but are not referenced by any project structure template, so they are never shipped into generated projects. They are dead boilerplate and are out of scope for this feature; the only live `make` references in generated projects are the makefile itself, the `.pre-commit-config.yaml` local hooks, and `ci.yml`.

## Decisions

- **Dependency manager question removed**: with `pdm` gone, `uv` is the only option, so asking the user adds no value. `dependency_manager` stays in the schema and defaults to `"uv"`.
  - Rationale: keeps `ipy.yml` backward compatible in shape and avoids breaking metrics/docs that read the field.
  - Alternative: keep the question with a single option. Rejected because a single-option prompt is noise.
- **`mise` and `task_runner` live in `general`**: `tool_version_manager` and `task_runner` are top-level `general` fields, and `makefile` is removed from the built-in features multiselect.
  - Rationale: these are cross-cutting decisions (they affect env setup, file rendering, CI, and scripts), not optional boilerplate features; the built-in features multiselect stays reserved for template-specific content.
  - Alternative: replacing the `makefile` built-in feature with a `taskfile` built-in feature toggle. Rejected because the flow described in the task is a conditional question chain (mise/external → task runner), which fits the `general` section better and keeps validation in `GeneralConfig`.
- **New `general` fields are required**: `tool_version_manager` and `task_runner` are required in the configuration file; a legacy `ipy.yml` missing them is rejected with an error directing the user to re-run `ipy config`.
  - Rationale: consistent with rejecting legacy `pdm`/`makefile` configs; failing loudly is safer than silently changing what existing configs generate.
  - Alternative: default missing fields to `external` + `none`. Rejected because it silently changes the output of existing configs without the user's knowledge.
- **`mise` manages Python too**: when `mise` is selected, `mise.toml` pins `python` and `uv` (and `task` when needed), and `.python-version` is not generated.
  - Rationale: a single source of truth for tool versions; `mise` is exactly the tool that manages versions, and mixing `mise` with a separate `.python-version` would create drift.
  - Alternative: `mise` only pins `uv`/`task` and Python keeps the current `.python-version` + `uv python install` flow. Rejected because it splits version management across two tools.
- **Poethepoet deferred**: `poethepoet` (tasks in `pyproject.toml`) is not included in this feature.
  - Rationale: taskfile and native mise tasks already cover the need; adding a third runner expands the matrix (question flow, CI rendering, validation, docs) without proven demand.
  - Alternative: ship it now. Rejected to keep this feature tight; it should be a follow-up issue with its own spec.
- **CI adapts to the task runner**: `ci.yml` and the GitHub action use the selected task runner's commands (`task <name>` or `mise run <name>`); with `task_runner == "none"` they fall back to raw `uv`/`uvx` commands.
  - Rationale: CI must keep working no matter the runner choice; hardcoding `make` after removing it would break every generated pipeline.
  - Alternative: force taskfile whenever `github_actions` is selected. Rejected as overly restrictive for the `mise` native path.
- **`mise.toml` over `.tool-versions`**: tools and native tasks are declared in `mise.toml`.
  - Rationale: the task explicitly names `mise.toml`, and `[tasks]` are only supported in the toml format, not in `.tool-versions`.
  - Alternative: `.tool-versions` for tools plus `mise.toml` for tasks. Rejected because it splits configuration across two files.
- **Task runner question asked after built-in features selection**: the wizard asks the tool version manager question early (general section), but the task runner question is asked after the features multiselect so the `github_actions` selection can pre-select `taskfile` as the default.
  - Rationale: the current wizard order is General → Template → Git → Dependencies; asking the task runner question before the template step would make the `github_actions` default impossible to compute.
  - Alternative: ask the task runner question unconditionally before the template step. Rejected because it breaks the `github_actions` default and diverges from today's "github_actions always ships a makefile" behavior.
- **GitHub action setup installs `mise` when `mise` is selected**: the `python_setup` composite action installs `mise` and lets it provide Python and `uv` instead of `actions/setup-python` + `pip install uv`.
  - Rationale: CI must use the same tool chain as the developer machine; `actions/setup-python` would pin a Python version independently of `mise.toml` and create drift.
  - Alternative: keep `actions/setup-python` and run raw `uv` in CI regardless of the local tool version manager. Rejected because the Python version would no longer come from a single source of truth.
- **Pre-commit local hooks adapt to the task runner**: the local `lint` and `format` hooks in `.pre-commit-config.yaml` invoke the selected runner (`task check-lint`, `mise run check-lint`) or, with `task_runner == "none"`, raw `uvx` commands.
  - Rationale: the hooks are the second live consumer of `make` in generated projects and must keep working after the makefile is gone.
  - Alternative: omit the local lint/format hooks when no task runner is active. Rejected because it silently weakens the pre-push checks that the `precommit_hook` feature promises.
- **Task commands are OS-independent via a Python helper script**: any task command (in `taskfile.yml` or in native mise tasks) that needs platform-specific shell syntax is implemented through a Python script that detects the platform and runs the correct command. The generated tasks reference the script instead of embedding unix-only syntax.
  - Rationale: the feature's goal is an OS-independent task runner; hardcoding unix commands (`rm --force`, `find`, `grep`/`awk`, `ln -sf`, `read -p`) would only move the Windows problem from the makefile to the new runner, and mise native tasks would require a POSIX shell.
  - Alternative 1: keep the unix commands as-is and document taskfile/native mise tasks as unix-only. Rejected because it defeats the stated goal.
  - Alternative 2: document native mise tasks as requiring a POSIX shell on Windows. Rejected in favor of making the commands themselves cross-platform.
- **Dev-dependency gating moves from the `makefile` feature to the task runner**: the `pyproject.toml` conditionals that today fire on `["github_actions", "makefile", "precommit_hook"]` fire instead on `github_actions` or `precommit_hook` or an active task runner.
  - Rationale: `taskfile.yml` and native mise tasks reference the same tools (ruff, mypy, pytest); without the gate change a project with a task runner but no github_actions would ship targets that call undeclared tools.
  - Alternative: keep gating on `github_actions` and `precommit_hook` only. Rejected because a task runner alone (no github_actions) would produce broken commands.
- **External flow does not install `task`**: with `tool_version_manager == "external"`, `instant-python` installs only `uv` and Python; the `task` binary required by `taskfile.yml` is installed by the user.
  - Rationale: `external` means the user manages tool versions; the current external flow installs only what the project cannot work without (uv/Python).
  - Alternative: install `task` in the external flow too. Rejected because it contradicts the "external install" contract and the current flow only installs uv/Python.

## Open Questions

None. All questions raised during review were resolved in the Decisions section.

## Requirements

### Dependency manager

- R1: The system SHALL support only `uv` as dependency manager.
- R2: WHEN a configuration file specifies a dependency manager other than `uv`, the system SHALL reject the configuration with an error message stating that `uv` is the only supported manager.
- R3: WHEN running the configuration wizard, the system SHALL set `dependency_manager` to `uv` without asking the user to select one.

### Tool version manager

- R4: WHEN running the configuration wizard, the system SHALL ask the user to select a tool version manager from `mise` and `external`.
- R5: WHEN the user selects `mise`, the system SHALL generate a `mise.toml` file declaring `python` at the selected version and `uv` at `latest`.
- R6: WHEN the user selects `mise` and `mise` is not installed, the system SHALL install `mise` before installing any declared tool.
- R7: WHEN the user selects `mise`, the system SHALL install the tools declared in `mise.toml` before creating the virtual environment.
- R8: WHEN the user selects `external`, the system SHALL install `uv` through its official installer when `uv` is not installed.
- R9: WHEN the user selects `external`, the system SHALL generate the `.python-version` file.
- R10: WHEN the user selects `mise`, the system SHALL NOT generate the `.python-version` file.

### Task runner

- R11: WHEN running the configuration wizard and the tool version manager is `mise`, the system SHALL ask the user to choose between native mise tasks and `taskfile`.
- R12: WHEN running the configuration wizard and the tool version manager is `external`, the system SHALL present `taskfile` as the default task runner and ask the user whether to keep it.
- R13: WHEN the user selects `github_actions` as a built-in feature, the task runner question SHALL default to `taskfile`.
- R14: WHEN the user chooses `taskfile`, the system SHALL generate a `taskfile.yml` file with the commands previously provided by the makefile.
- R15: WHEN the user chooses `taskfile` and the tool version manager is `mise`, the system SHALL declare `task` at `latest` in `mise.toml`.
- R16: WHEN the user chooses native mise tasks, the system SHALL write the tasks into the `[tasks]` section of `mise.toml`.
- R17: WHEN a task in a generated task runner uses platform-specific shell syntax, the system SHALL implement the command through a Python helper script that selects the command based on the detected platform.
- R18: WHEN the user chooses native mise tasks, the system SHALL NOT generate a `taskfile.yml` file.
- R19: WHEN the user does not choose any task runner, the system SHALL NOT generate a task file.
- R20: The system SHALL NOT generate a `makefile` in generated projects.
- R21: The system SHALL remove `makefile` from the list of supported built-in features.

### Validation and legacy configuration

- R22: WHEN a configuration specifies `task_runner` as `mise` and `tool_version_manager` as anything other than `mise`, the system SHALL reject the configuration with an error message explaining that native mise tasks require the `mise` tool version manager.
- R23: WHEN a configuration specifies `makefile` in `template.built_in_features`, the system SHALL reject the configuration with an error message referencing the task runner configuration.
- R24: WHEN a configuration omits `tool_version_manager` or `task_runner`, the system SHALL reject the configuration with an error message directing the user to re-run `ipy config`.

### Integrations

- R25: WHEN `github_actions` is selected and a task runner is active, the system SHALL render CI steps using that task runner's commands.
- R26: WHEN `github_actions` is selected and no task runner is active, the system SHALL render CI steps using raw `uv` and `uvx` commands.
- R27: WHEN `github_actions` is selected and the tool version manager is `mise`, the GitHub action setup step SHALL install `mise` and use it to provide Python and `uv`.
- R28: WHEN the `precommit_hook` feature is selected and a task runner is active, the local lint and format hooks in `.pre-commit-config.yaml` SHALL invoke the selected task runner.
- R29: WHEN the `precommit_hook` feature is selected and no task runner is active, the local lint and format hooks in `.pre-commit-config.yaml` SHALL invoke raw `uv` and `uvx` commands.
- R30: WHEN a task runner is active, the generated `pyproject.toml` SHALL declare the lint, test, and type-checking tooling that the removed `makefile` feature used to trigger.
- R31: WHEN the user chooses `taskfile` and the tool version manager is `external`, the system SHALL NOT install the `task` binary.

### Metrics, schema, and documentation

- R32: The system SHALL record `tool_version_manager` and `task_runner` in the usage metrics payload.
- R33: The system SHALL update `schemas/ipy-schema.json` so that `dependency_manager` only allows `uv`, `tool_version_manager` and `task_runner` are declared with their enums and the cross-field constraint, and `makefile` is removed from the `built_in_features` enum.
- R34: The system SHALL update the user documentation to reflect the removal of `pdm` and the `makefile`, and the new tool version manager and task runner options.

## Related Features

- `docs/specs/technical-debt-review.md` — documents the makefile's fragile `clean` target (DT-10); this feature removes the makefile entirely.
- `docs/specs/0001-metrics-middleware-refactor.md` — the metrics middleware spec; requirement R30 extends the metrics payload built around `ConfigSchema.for_metrics()`.
