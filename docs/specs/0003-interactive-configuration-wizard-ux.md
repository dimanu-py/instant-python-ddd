# Interactive Configuration Wizard UX

## Purpose

Improve the `ipy config` question-and-answer flow so users can see their progress, review every collected answer, and explicitly confirm before a configuration file is written, without replacing the questionnaire with a TUI.

## Behavior

The `ipy config` wizard remains a standard terminal questionnaire that asks one question at a time with concise wording and consistent punctuation. It runs through four sections in order — General, Template, Git, and Dependencies — each introduced by a progress heading of the form `[n/4] <Section title>`, where `n` is the one-based position and `4` is the total section count. The happy path stays quiet and fast; explanations are not embedded in every prompt, and detailed guidance belongs in validation errors and documentation.

### General section

The wizard starts with `[1/4] General` and asks for the project slug, source folder, description, initial version, author, license, Python version, and dependency manager.

### Template section

The wizard displays `[2/4] Template` and asks for the project structure and the optional built-in features. When the `domain_driven_design` structure is selected, it asks whether to specify a bounded context; when the user confirms, it asks for the bounded context name and the aggregate name. Built-in feature questions are not asked for a custom structure.

### Git section

The wizard displays `[3/4] Git` and asks whether to initialize a Git repository. The Git user name and email are requested only when initialization is enabled.

### Dependencies section

The wizard displays `[4/4] Dependencies` and first asks `Do you want to add initial dependencies?`. After each dependency it asks `Do you want to add another dependency?`, and the loop repeats until the user declines. An empty dependency name prints a validation message and re-asks the name prompt. Development group information is requested only for development dependencies.

### Review and confirmation

After the four sections, the wizard displays a summary of the collected answers grouped by configuration section. The review is built from the collected answers only: values that were neither collected nor supplied as prompt defaults do not appear. A section with no collected items shows its title followed by `None`; a list field with no items shows `None` as its value.

```text
Review configuration

General
  Project slug: example-project
  Source name: src
  Python version: 3.13

Template
  Name: standard_project
  Built in features: None

Git
  Initialize: False

Dependencies
  None
```

When dependencies were added, each row uses `name==version`, `name==version (dev)` for development dependencies, and `name==version (dev, group: <group>)` when a development group is set.

The wizard then asks `Save configuration? (Y/n)`, defaulting to confirmation. Confirming writes `ipy.yml` through the existing write path, so the YAML structure is unchanged. Declining reports that the configuration was discarded, does not create or overwrite a configuration file, and exits with status 0. Cancelling (interrupting a prompt with Ctrl+C) aborts the wizard immediately, writes nothing, and exits with a non-zero status.

## Contract

- **Inputs**:
  - Terminal answers for the general, template, git, and dependency questions that apply to the previous answers.
  - The answer to `Save configuration? (Y/n)`.
- **Outputs**:
  - A `[n/4] <Section title>` progress heading before each section's questions.
  - A summary of the collected answers grouped by configuration section.
  - `ipy.yml` written only when the user confirms the save, using the existing write path so the YAML structure is unchanged.
  - A message reporting that the configuration was discarded when the user declines; no file is created or overwritten.
  - Existing configuration values and YAML structure remain unchanged.

## Edge Cases

- The `domain_driven_design` structure is selected and the user confirms specifying a bounded context: the wizard asks for the bounded context name and the aggregate name.
- The `domain_driven_design` structure is selected and the user declines specifying a bounded context: no names are asked and `specify_bounded_context` is recorded as `False`.
- A structure other than `domain_driven_design` is selected: the gate question and the bounded context and aggregate questions are skipped.
- A custom structure is selected: built-in feature questions are skipped.
- Git initialization is declined: Git user name and email questions are skipped.
- No initial dependencies are added: the dependencies section shows `None` in the review and no "add another" prompt appears.
- A development dependency is added: the wizard asks for its development group; this question is skipped for non-development dependencies.
- An empty dependency name is entered: a validation message is shown and the name prompt is re-asked.
- The user declines `Save configuration? (Y/n)`: the wizard reports the discard, exits with status 0, and does not create or overwrite `ipy.yml`.
- The user cancels with Ctrl+C at any prompt: the wizard aborts, writes nothing, and exits with a non-zero status.
- `ipy.yml` already exists and the user confirms the save: the file is overwritten without an extra warning; the grouped review and explicit confirmation are the safety.
- The user presses Enter on the save prompt: the confirmation default applies and `ipy.yml` is written.

## Decisions

- **Remain a linear terminal questionnaire rather than a TUI.**
  - Rationale: the current flow is fast and familiar; a full-screen TUI would add rendering complexity and a new runtime dependency, contradicting the simple-terminal and no-new-dependency constraints.
  - Alternative: replace the questionnaire with a full-screen TUI. Rejected; listed explicitly as out of scope.
- **Progress via one heading per section.**
  - Rationale: `[n/4] <Section title>` before each section's questions gives orientation without noise, keeping the happy path quiet and fast.
  - Alternative: show a progress indicator on every prompt. Rejected because it clutters every question.
  - Alternative: show no progress at all. Rejected because users cannot tell how much work remains, which is the problem this spec solves.
- **Conditional questions driven by previous answers.**
  - Rationale: asking only what applies keeps prompts short and avoids forcing irrelevant answers, which is faster and less error-prone.
  - Alternative: ask every question unconditionally. Rejected because it forces irrelevant answers, such as DDD contexts for a non-DDD structure.
- **Review all answers and require explicit confirmation before writing.**
  - Rationale: users must be able to verify the complete result before anything is written; the wizard must never write unreviewed answers.
  - Alternative: write `ipy.yml` immediately after the last question. Rejected because the user cannot verify the result before the file is created.
- **Declining the save discards the collected answers.**
  - Rationale: declining is an explicit intent not to save; writing anyway would ignore the user and could overwrite an existing file.
  - Alternative: save anyway and let the user delete it later. Rejected.
- **Default the save answer to confirmation.**
  - Rationale: pressing Enter on `Save configuration? (Y/n)` confirms, keeping the happy path fast.
  - Alternative: default to declining. Rejected because it forces extra input on the common path.
- **Keep the `specify_bounded_context` gate question.**
  - Rationale: the gate lets DDD users skip the names when they want, and the schema and templates already model the flag. The real defect is that the gate's answer is never returned, leaving the names flow dead code; this spec includes the fix.
  - Alternative: remove the gate and always ask the names for DDD. Rejected because it forces the names on every DDD project and changes schema semantics.
- **No extra warning when `ipy.yml` already exists.**
  - Rationale: the grouped review plus the explicit `Save configuration? (Y/n)` confirmation is sufficient safety; an extra warning would add noise to the happy path.
  - Alternative: warn that the existing file will be overwritten. Rejected to keep the happy path quiet.
- **Cancelling aborts; declining exits with status 0.**
  - Rationale: an interrupt (Ctrl+C) is an explicit abort — write nothing, exit non-zero — while declining the save is a deliberate discard — report it and exit 0.
  - Alternative: treat Ctrl+C the same as declining. Rejected because an interrupt is not a decision about the configuration.
- **The review is built from the collected answers, not from the config schema.**
  - Rationale: schema-only defaults (such as `year`) and never-asked fields must not appear; the review only shows values collected from the user or supplied as prompt defaults.
  - Alternative: dump `ConfigSchema.to_primitives()`. Rejected because it would expose defaults and nulls the user never provided.
- **Saving reuses the existing write path.**
  - Rationale: confirming SHALL produce the same `ipy.yml` as today for the same answers; reusing `ConfigSchema.to_primitives()` and the current repository keeps the YAML structure unchanged.
  - Alternative: write from the review subset. Rejected because it would drop keys and break compatibility with existing files.

## Open Questions

None. All questions raised during review were resolved in the Decisions section.

## Requirements

### Section ordering and progress

- R1: WHEN the user starts `ipy config`, the system SHALL present the General, Template, Git, and Dependencies sections in that order.
- R2: WHEN a section starts, the system SHALL display a progress heading showing the section's one-based position, the total section count, and the section title before that section's questions.
- R3: The wizard SHALL ask one question per prompt with concise wording and consistent punctuation.
- R4: WHEN asking a question, the system SHALL NOT include validation rules or explanatory paragraphs in the prompt.

### Conditional questions

- R5: WHEN the user selects the `domain_driven_design` structure, the system SHALL ask whether to specify a bounded context.
- R6: WHEN the user selects the `domain_driven_design` structure AND confirms specifying a bounded context, the system SHALL ask for the bounded context name and the aggregate name.
- R7: WHEN the user selects the `domain_driven_design` structure AND declines specifying a bounded context, the system SHALL NOT ask for a bounded context name or an aggregate name.
- R8: WHEN the user selects a structure other than `domain_driven_design`, the system SHALL NOT ask whether to specify a bounded context.
- R9: WHEN the user selects a custom structure, the system SHALL NOT ask about built-in features.
- R10: WHEN the user declines Git initialization, the system SHALL NOT ask for a Git user name or email.
- R11: WHEN the user adds a development dependency, the system SHALL ask for its development group.
- R12: WHEN the user adds a non-development dependency, the system SHALL NOT ask for a development group.

### Dependencies

- R13: WHEN the user chooses to add initial dependencies, the system SHALL ask whether to add another dependency after each dependency is collected.
- R14: WHEN collecting dependencies, the system SHALL ask `Do you want to add initial dependencies?` before the first dependency and `Do you want to add another dependency?` before each subsequent one.
- R15: WHEN the user enters an empty dependency name, the system SHALL print a validation message and re-ask the dependency name prompt.

### Review and save

- R16: WHEN the wizard reaches the review, the system SHALL display the collected answers grouped by configuration section.
- R17: WHEN a section has no collected items, the system SHALL display the section title followed by `None`.
- R18: WHEN a field within a section has an empty list, the system SHALL display the field with `None` as its value.
- R19: WHEN the review displays a dependency, the system SHALL render it as `name==version`, with `(dev)` appended for development dependencies and `(dev, group: <group>)` when a development group is set.
- R20: WHEN the wizard asks whether to save the configuration, the system SHALL default the answer to confirmation.
- R21: WHEN the user confirms the save, the system SHALL write `ipy.yml` through the existing write path so the YAML structure is unchanged.
- R22: WHEN the user declines the save, the system SHALL report that the configuration was discarded.
- R23: WHEN the user declines the save, the system SHALL NOT create or overwrite a configuration file.
- R24: WHEN the user declines the save, the system SHALL exit with status 0.
- R25: WHEN the user cancels the wizard, the system SHALL abort without creating or overwriting a configuration file.
- R26: WHEN the user cancels the wizard, the system SHALL exit with a non-zero status.

### Non-functional

- R27: The wizard SHALL run as a standard terminal questionnaire.
- R28: The wizard SHALL NOT use a full-screen TUI.
- R29: WHEN the user confirms the save with the same answers, the system SHALL produce the same `ipy.yml` as today, keeping configuration values and YAML structure compatible with existing files.
- R30: The wizard SHALL render the new output (progress headings, review, discard message) readably without color or advanced terminal rendering.
- R31: The wizard SHALL collect answers through an injectable question-asking collaborator so a fake can substitute for interactive input in tests.
- R32: Each wizard step SHALL have unit test coverage that exercises its questions through the injectable collaborator.
- R33: The wizard SHALL NOT require a new runtime dependency.
- R34: The review SHALL NOT display values that were neither collected from the user nor supplied as prompt defaults.

## Out of Scope

- Full-screen TUI navigation.
- Moving backward between questions during initial collection.
- Editing an individual answer from the review screen.
- Loading and editing an existing `ipy.yml`.
- Non-interactive flags such as `--set` or `--reset`.
- Changes to the `init` command.

## Future Considerations

- Add an `Edit` choice to the review screen if users need to correct individual sections frequently.
- Prefill author and Git identity from existing local Git configuration.
- Replace internal template and feature identifiers with friendly display labels while preserving stored values.
- Add contextual validation messages for invalid free-text answers.

## Related Features

- `docs/specs/0002-new-tool-management-system.md` — lands after this feature; it removes the dependency manager question asked here, changes the built-in features multiselect (`makefile` is removed, `task_runner`/`tool_version_manager` become conditional wizard questions), and keeps the same General → Template → Git → Dependencies wizard order. This spec's review groups answers by configuration key, so it survives the new `general` fields 0002 introduces.
- `docs/specs/0001-metrics-middleware-refactor.md` — the metrics middleware reads the configuration produced by the wizard; this feature must keep the YAML structure it consumes unchanged. 0001's R10 ("SHALL NOT change existing CLI behavior or output") is scoped to middleware behavior and is not affected by the wizard's new headings, review, or confirmation output.
