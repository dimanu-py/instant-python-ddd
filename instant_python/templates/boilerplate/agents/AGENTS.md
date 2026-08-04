# AI Agent Development Rules

## Core Principles

- **Baby Steps**: Always work in baby steps, one at a time. Never go forward more than one step.
- **Test-Driven Development**: Start with a failing test for any new functionality (TDD).
- **Progressive Revelation**: Never show all the code at once; only the next step.
- **Type Safety**: All code must be fully typed.
- **Simplicity First**: Use the simplest working solution; avoid unnecessary abstractions.
- **Small Components**: Classes and methods should be small.
- **Clear Naming**: Use clear, descriptive names for all variables and functions.
- **Incremental Changes**: Prefer incremental, focused changes over large, complex modifications.
- **Question Assumptions**: Always question assumptions and inferences.
- **Refactoring Awareness**: Highlight opportunities for refactoring and flag functions exceeding 20 lines.
- **Pattern Detection**: Detect and highlight repeated code patterns.
- **Persistence**: Persist through multiple attempts until resolution. Iterate thoroughly on complex problems.
- **TDD Workflow**: Test-Driven Development (TDD) is the default workflow: always write tests first.
- **Pair Programming**: Prefer pairing sessions for complex features and knowledge sharing.
- **Small Pull Requests**: Keep changes small and focused for easier review and faster integration.
- **Code Review Standards**: All code must be reviewed before merging, following project quality standards.
- **Knowledge Sharing**: Document decisions and share context with team members.

## Communication

- **Natural Expression**: Express all reasoning in a natural, conversational internal monologue.
- **Progressive Building**: Use progressive, stepwise building: start with basics, build on previous points, break down complex thoughts.
- **Simple Communication**: Use short, simple sentences that mirror natural thought patterns.
- **Avoid Rushing**: Never rush to conclusions; frequently reassess and revise.
- **Seek Clarification**: If in doubt, always ask for clarification before proceeding.
- **Contemplation Phase**: Every response must begin with a <CONTEMPLATOR> section: show all work, doubts, and natural thought progression.
- **Final Answer**: Only provide a <FINAL_ANSWER> if reasoning converges to a clear conclusion.
- **No Skipping**: Never skip the contemplation phase.
- **No Moralizing**: Never include moralizing warnings in the final answer.
- **Progress Indicators**: When outlining plans, use numbers/metrics and emojis to indicate progress.

## Code Standards

### General

- **OOP Design**: Use Object-Oriented Programming (OOP) for all components and features
- **Self-Documenting Code**: Avoid comments. Rely entirely on clear naming. Remove comments that describe obvious behavior or duplicate Git history (Arrange/Act/Assert labels, historical references, etc.).
- **Clear Naming**: Use descriptive, purpose-revealing names for all variables, functions, classes, and test functions.
- **Small Components**: Keep classes and methods small. Flag any function exceeding 20 lines.
- **Refactoring Awareness**: Highlight refactoring opportunities and detect repeated code patterns.
- **Graceful Error Handling**: Always implement proper error handling with meaningful messages and logging.
- **Fail Fast**: Design code to fail fast and fail clearly.
- **Error Context**: Provide sufficient context in error messages to enable quick problem resolution.
- **Input Validation**: Always validate and sanitize external inputs.
- **Security by Design**: Consider security implications in all design decisions.
- **Secrets Management**: Never hardcode secrets; use proper secret management systems.
- **Security Awareness**: Consider security implications in all design decisions.
- **Easy to Read**: Production code should be easy to read and understand without needing to inspect the implementation. Encapsulate behaviors in 
  variables or methods that describe the behavior performed.

### Testing

- **Unit Tests**: Fast, isolated tests for individual components (majority of test suite).
- **Integration Tests**: Test interactions between components and external systems (limited, focused).
- **E2E Tests**: Full system validation (minimal, critical user paths only).
- **Test Pyramid**: Follow the test pyramid - many unit tests, some integration tests, few E2E tests.
- **Failing Test First**: Always start with a failing test before implementing new functionality.
- **Single Test**: Write only one test at a time; never create more than one test per change.
- **Complete Coverage**: Ensure every new feature or bugfix is covered by a test.
- **Mocking**: use mocking tools to double collaborators that are external to the subject under test, i.e. a repository interface that will hide communication with database
- **Type Hints**: All test functions and helpers must have full type hints.
- **Focused Tests**: Keep each test focused and under 20 lines. Based on test desiderata to write good tests.
- **Clear Naming**: Use clear, descriptive names for test functions and variables.
- **No Comments**: Avoid comments; make code self-documenting through naming.
- **Simple Helpers**: Use helper methods (e.g., object mothers/factories) for repeated setup, but keep them simple and typed.
- **Strategic Mocking Rule**: Use `@patch` from unittest.mock ONLY for Python system modules (readline, atexit, subprocess, sys, os, etc.). Use doublex for all application code mocking. This provides clear separation: system modules = @patch, application code = doublex.
- **Simplest Setup**: Prefer the simplest test setup that covers the requirement.
- **Refactor Tests**: Refactor tests to remove duplication and improve readability.
- **Consistent Assertions**: Use one assertion style (expects) consistently throughout the suite.
- **Extract Helpers**: If a test setup is repeated, extract a helper or fixture.
- **Readable Tests**: Always keep tests readable and easy to modify.
- **Purpose-Driven Variables**: Use descriptive variable names that reflect their purpose in the test.

## Documentation Standards

- **User-Focused README**: README.md must be user-focused, containing only information relevant to table authors and end users.
- **Separate Dev Docs**: All technical documentation and conventions must be maintained in `docs/adrs/`
- **Separate Design Docs**: All design decisions, feature specifications, and architectural discussions must be maintained in `docs/design_docs/`
- **Conventions**: Reusable patterns and practices captured by the convention_keeper agent go in `docs/conventions/`
- **Specs**: Design documents capturing purpose, contract, and decisions live in `docs/specs/`
- **Feature Files**: Executable Gherkin scenarios live in `docs/features/`
- **Progress Tracking**: Session logs and agent progress go in `docs/progress/`
- **Error Examples**: User-facing documentation should include example error messages for common validation failures to help users quickly resolve issues.

```
docs/
├── conventions/     # Reusable conventions (organized by area)
├── specs/           # .md spec files (purpose, contract, decisions)
├── progress/        # Session and agent progress logs
├── tasks.json       # Task management (status: pending, spec_ready, in_progress, done, blocked)
```

## Tool usage

**NEVER** call tools like `pytest`, `black`, `mypy`, or similar directly. Always use the corresponding `make` or `task` target.

### Usage Rules
1. **Testing**: When running tests, use `make unit`, `make integration`, `make acceptance` or `make test` as appropriate.
2. **Formatting**: For formatting, use `make format` or `make check-format`.
3. **Type Checking**: For type checking, use `make check-typing`.
4. **Lint Checks**: For lint checks, use `make check-lint`.
5. **Building**: For building or updating the app, use `make build` or `make update`.
6. **Help**: If you are unsure which target to use, run `make help` to see all available options.
7. **New Operations**: If a new operation is needed, prefer adding a new Makefile target rather than running a tool directly.

### Good vs Bad Examples
```sh
# Good: Use make target for unit tests
make unit

# Bad: Call pytest directly
pytest tests
```

## Quick Reference for All AI Agents

When working on this project:

1. **Start every response with contemplation** 🌲
2. **Take baby steps** - one test, one file, one change at a time 👣
3. **Always write the failing test first** (TDD) ❌➡️✅
4. **Use make targets** - never call tools directly 🔧
5. **Keep code small and typed** - max 20 lines per method 📏
6. **Show your thinking process** - be conversational and progressive 💭
7. **Question everything** - assumptions, requirements, design choices ❓
8. **Run tests automatically** after every change 🧪
9. **Focus on simplicity** over cleverness ✨
10. **Ask for clarification** when in doubt 🤔

Remember: This is a high-quality, test-driven, incremental development environment. Quality over speed, clarity over cleverness, baby steps over big leaps. 