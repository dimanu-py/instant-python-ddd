# Documentation Standard

## Convention

Every project convention (architectural decisions, style conventions, patterns) must be documented as a standalone Markdown file inside the `docs/conventions/` folder, organized by area (`architecture/`, `testing/`, `workflow/`). Each document follows a fixed structure with these sections in order: Convention, Benefits, Examples (good and bad), Real world examples, and Related agreements.

The goal is to provide AI agents and developers with self-contained, discoverable references that require
no extra context to understand.

## Rules

- Each convention goes in its own standalone Markdown file — never bundle multiple conventions into one doc.
- Place files in the correct area subfolder (`architecture/`, `testing/`, `database/`, etc -- these areas are examples).
- Include concrete good and bad examples with code blocks when applicable.
- Link to real files in the codebase that follow the convention in the "Real world examples" section.

## Benefits

- AI agents can consume individual docs without loading the entire knowledge base, reducing token usage.
- New team members find conventions faster through a browsable folder structure.
- Each doc is independently reviewable in PRs, making convention changes easy to track.
- The fixed structure ensures consistency and completeness across all documented conventions.

## Examples

### Good: Well-structured convention document

```markdown
# Name of the convention

## Convention

Convention description.

## Benefits

- List of why to use this convention.

## Examples

### Good: Definition of a good example

good example

### Bad: Definition of a bad example

bad example

## Real world examples

- Links to files following this convention

## Related agreements

- Links to agreements related to this convention if applies
```

### Bad: Convention buried in a monolithic file

```markdown
# Project Guidelines

## Architecture
We use hexagonal architecture...

## Testing
Use object mothers...

## Database
PostgreSQL with pgvector...
```

## Real world examples


## Related agreements

- All docs inside `docs/conventions` must follow this standard