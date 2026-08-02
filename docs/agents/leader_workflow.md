# Leader Workflow

## Convention

The development process follows a strict pipeline with a single human approval gate. Every feature with the `sdd` label passes 
through these phases:

```
Todo
    → [spec_partner]  conversation + requirements distillation → .md spec file with requirements and tasks recorded in Linear
    → ⏸ HUMAN APPROVES the scenarios
    → In Progress
    → [tdd_craftsman]  Red → Green → Refactor cycle (one test at a time)
    → [judge]          review + mutation testing
    → [convention_keeper]  capture learnings → update convention docs
    → Release
```

One feature at a time. One human approval gate: on the requirements scenarios, before writing production code.

### Phase details

1. **spec_partner**: the spec is born from conversation, not dictation. The agent debates edge cases, 
output contracts, and discarded alternatives with the human. The result is a reasoned `.md` spec file 
documenting decisions and their rationale. The same agent then distills the spec into executable requirements
using EARS convention to then be able to convert them into executable tests.
2. **Human approval gate**: the human must read and approve the spec and requirements before any production code is written. Approving late 
(after code exists) is expensive; approving the requirements is cheap and is the point of maximum leverage. The leader **stops** here and waits.
3. **tdd_craftsman**: one test at a time following the Three Laws of TDD: Red (write a failing test), Green (minimum code to pass), 
Refactor (clean up in green). No code is written that no test asks for.
4. **judge**: reviews all code and tests, then runs mutation testing. The review step is the whole 
game: agents draft, judgment prunes. Mutation testing validates that the test suite actually 
catches defects. Only when both review and mutation succeed does the leader run the **convention_keeper**.
5. **convention_keeper**: reviews the completed feature's artifacts (spec, progress logs, judge verdict), identifies new patterns or 
practices worth standardising, and creates or updates convention docs in `docs/conventions/`. Always asks the human to approve new convention files before finalising.

### Artifact map

| File                                  | Created by        | Content                                                       |
|---------------------------------------|-------------------|---------------------------------------------------------------|
| `docs/specs/<name>.md`                | spec_partner      | Spec conversation: purpose, contract, decisions, requirements |
| `instant_python/`, `test/`            | tdd_craftsman     | Production code and tests, carved by TDD                      |
| `docs/progress/tdd_<name>.md`         | tdd_craftsman     | Cycle log + requirement-to-test map                           |
| `docs/progress/judge_<name>.md`       | judge             | Review verdict + mutation score                               |
| `docs/conventions/`                   | convention_keeper | New or updated convention docs                                |

The Linear project tracks feature status: `Todo → In Progress → Release`. Sliced subtasks live as child issues of the feature issue.

### Anti-broken-telephone rule

Subagents write results to files (listed above) and return only the file reference, never 
the content through chat. This prevents information loss and keeps the audit trail on disk.

## Benefits

- **Single human gate** keeps approval cost low and leverage high — catch contract flaws before code exists.
- **Spec conversation** surfaces hidden edge cases that written requirements miss.
- **TDD strictness** ensures every line of code is justified by a failing test.
- **Mutation testing** proves the test suite catches real defects, not just that the code runs.
- **One feature at a time** prevents context switching and partial work.
- **File-based handoffs** prevent information loss across agent handovers.

## Examples

### Good: Following the full pipeline

A feature enters `Todo` in Linear. The leader launches `spec_partner`, which debates with the human, 
writes `docs/specs/new-feature.md`, then generates the requirements inside the same spec file. The leader
stops and asks the human to approve. 
The human reads the scenarios, approves them. 
The leader updates the issue to `In Progress`, launches `tdd_craftsman`. 
Once tests pass, `judge` reviews and runs mutation. All green → `convention_keeper` captures learnings and updates conventions. Issue status moves to `Release`.

### Bad: Skipping the spec conversation

A leader launches `tdd_craftsman` directly on a `Todo` feature because the requirements seem clear. The coder writes tests that pass but miss the actual business behavior. No spec file exists. The `judge` rejects for missing spec coverage, and everything rolls back.

### Bad: Two features in flight

The leader starts spec for feature A, then launches TDD for feature B while waiting for human approval on A. The coder on B is blocked by ambiguous scenarios, and the human now has two unapproved requirements to review. The pipeline ensures one feature at a time for a reason.

## Related agreements

- `docs/agents/convention_guidelines.md` — document structure standard
- `docs/agents/spec_guidelines.md` — spec generation guidelines
