---
name: spec
description: Create or update spec .md files in docs/specs/ using the established format. Use when a feature needs to be documented before implementing code.
---

# Spec

Creates or updates spec `.md` files inside `docs/specs/`. A spec captures a feature's purpose, behavior, contract, edge cases, and 
decisions before any code is written.
This project follows a lightweight Kiro-style flow: purpose/behavior/contract → EARS requirements → tasks → code. Code is not written 
until the spec is approved by a human.

## Format

Every spec document MUST include these sections in order:

```markdown
# Feature Name

## Purpose

One sentence describing what the feature does.

## Behavior

Precise prose describing what the feature does: inputs, processing, and outputs. No implementation details.

## Contract

- **Inputs**: request shape (path params, query params, body schema)
- **Outputs**: response shape (status codes, body schema)

## Edge Cases

Enumerated list of edge cases and how the system handles each:
- Case one: description
- Case two: description

## Decisions

Each decision with its rationale and the discarded alternative.
- **Decision**: what was chosen
- **Rationale**: why
- **Alternative**: what was rejected and why

## Open Questions

Unresolved items (mark as resolved or remove when decided).

## Requirements

Requirements are written in **EARS** (Easy Approach to Requirements Syntax). Each requirement
is a numbered paragraph following one of these five patterns:

| Pattern               | Template                                               |
|-----------------------|--------------------------------------------------------|
| **Ubiquitous**        | `The system SHALL <action>.`                           |
| **Event-driven**      | `WHEN <trigger>, the system SHALL <action>.`           |
| **State-driven**      | `WHILE <state>, the system SHALL <action>.`            |
| **Optional feature**  | `WHERE <optional feature>, the system SHALL <action>.` |
| **Unwanted behavior** | `IF <unwanted event> THEN the system SHALL <action>.`  |

Hard rules:

- Each requirement has a stable id: `R1`, `R2`, ...
- Each requirement MUST be verifiable by at least one concrete test.
- Don't mix several `SHALL`s in one requirement. Split it if there is more than one.
- Don't use soft verbs ("could", "may", "supports"). Only `SHALL` / `SHALL NOT`.

## Related Features

Reference to related spec files that already exist.
```

## Rules

- One spec per feature, named `docs/specs/<name>.md`
- Every claim must be convertible to a requirement. Each requirement will be converted into a test. If not testable, refine it or mark as open.
- Every decision must record the alternative that was rejected and why.
- Do not include implementation details or code.
