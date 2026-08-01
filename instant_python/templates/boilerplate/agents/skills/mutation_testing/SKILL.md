---
name: mutation_testing
description: Mutation testing patterns for Python using mutmut. Use when analyzing Python code to find weak or missing tests, verifying pytest effectiveness, strengthening Python test suites, or validating TDD workflows in Python projects.
---

# Mutation Testing for Python

Mutation testing answers the question: **"Are my tests actually catching bugs?"**

Code coverage tells you what code your tests execute. Mutation testing tells you if your tests would **detect changes** to that code. A
test suite with 100% coverage can still miss 40% of potential bugs.

---

## Core Concept

**The Mutation Testing Process:**

1. **Generate mutants**: Introduce small bugs (mutations) into production code
2. **Run tests**: Execute your test suite against each mutant
3. **Evaluate results**: If tests fail, the mutant is "killed" (good). If tests pass, the mutant "survived" (bad - your tests missed the bug)

**The Insight**: A surviving mutant represents a bug your tests wouldn't catch.

## When to Use This Skill

Use mutation testing analysis when:

- Reviewing code changes on a branch
- Verifying test effectiveness after TDD
- Identifying weak tests that appear to have coverage
- Finding missing edge case tests
- Validating that refactoring didn't weaken test suite

**Integration with TDD:**

```
TDD Workflow                    Mutation Testing Validation
┌─────────────────┐             ┌─────────────────────────────┐
│ RED: Write test │             │                             │
│ GREEN: Pass it  │──────────►  │ After GREEN: Verify tests   │
│ REFACTOR        │             │ would kill relevant mutants │
└─────────────────┘             └─────────────────────────────┘
```

## Reviewing a Mutation Results

`mutmut` generates and runs the real mutants — there's no need to simulate them by hand. Use
this process to go from a `make mutate` run to a reject/approve decision:

### Step 1: Scope to What Changed

```bash
# Get files changed for this task
git diff main...HEAD --name-only | grep '\.py$' | grep -v 'test_'
```

mutmut may report on the whole codebase; only survived mutants in the code this task actually
changed are relevant to this review.

### Step 2: Run and Read Results

Run `make mutate`, then `uv run mutmut results` for the mutation score and the list of
survived mutants (see Integration with mutmut below).

### Step 3: Classify Each Relevant Survived Mutant

For every survived mutant in changed code, use `uv run mutmut show <id>` to see the exact
change, then decide:

1. **Is there a test that exercises this code path at all?**
2. **If yes, is the assertion specific enough that this mutant would have failed it?**
3. **If neither, is this actually an equivalent mutant** (see Equivalent Mutants below) rather
   than a real gap?

### Step 4: Act

| Category                       | Action                                                 |
|--------------------------------|--------------------------------------------------------|
| Killed                         | None — tests are effective                             |
| Survived, real gap             | Reject; `tdd_craftsman` must add/strengthen a test     |
| Survived, equivalent mutant    | None — not a real bug, but document why in the verdict |
| No test covers the line at all | Reject; `tdd_craftsman` must add a behavior test       |

## Mutant States and Metrics

mutmut itself reports killed/survived/timeout/skipped. "No Coverage" shows up as a plain
survived mutant, and "Equivalent" is never a label mutmut assigns — it's the judgment call
`judge` makes after inspecting a survived mutant that turns out to be unkillable.

### Mutant States

| State           | Meaning                         | Action                     |
|-----------------|---------------------------------|----------------------------|
| **Killed**      | Test failed when mutant applied | Good - tests are effective |
| **Survived**    | Tests passed with mutant active | Bad - add/strengthen test  |
| **No Coverage** | No test exercises this code     | Add behavior test          |
| **Timeout**     | Tests timed out (infinite loop) | Counted as detected        |
| **Equivalent**  | Mutant produces same behavior   | No action - not a real bug |

### Target Mutation Score

| Score  | Quality                                   |
|--------|-------------------------------------------|
| < 60%  | Weak test suite - significant gaps        |
| 60-80% | Moderate - many improvements possible     |
| 80-90% | Good - but still gaps to address          |
| > 90%  | Strong - but watch for equivalent mutants |

## Equivalent Mutants

Equivalent mutants produce the same behavior as the original code. They cannot be killed because there is no observable difference.

### Common Equivalent Mutant Patterns

**Pattern 1: Operations with identity elements**

```python
# Mutant in conditional where both branches have same effect
if whatever:
    number += 0  # Can mutate to -= 0, *= 1, /= 1 - all equivalent!
else:
    number += 0
```

**Pattern 2: Boundary conditions that don't affect outcome**

```python
# When max equals min, condition doesn't matter
max_val = max(a, b)
min_val = min(a, b)
if a >= b:  # Mutating to <= or < has no effect when a == b
    result = 10 ** (max_val - min_val)  # 10 ** 0 = 1 regardless
```

**Pattern 3: Dead code paths**

```python
# If this path is never reached, mutations don't matter
if impossible_condition:
    do_something()  # Mutating this won't affect behavior
```

**Pattern 4: None handling equivalences**

```python
# When value is never None in practice
if value is None:  # Mutating to == None has same effect
    return default
```

### How to Handle Equivalent Mutants

1. **Identify**: Analyze if mutation truly changes observable behavior
2. **Document**: Note why mutant is equivalent
3. **Accept**: 100% mutation score may not be achievable
4. **Consider refactoring**: Sometimes equivalent mutants indicate unclear code

### Python-Specific Gotchas

| Pattern                                      | Why It's Weak                       | How to Strengthen                   |
|----------------------------------------------|-------------------------------------|-------------------------------------|
| Testing `is None` only                       | Doesn't verify `== None` difference | Test with `""`, `0`, `[]`           |
| Testing `.get()` only with existing keys     | Doesn't verify default behavior     | Test missing keys                   |
| Testing list comprehensions with all matches | Doesn't verify filter logic         | Mix matching and non-matching items |
| Testing only happy path exceptions           | Doesn't verify exception conditions | Use `pytest.raises()`               |
| Testing only `and` with both True            | Doesn't verify operator choice      | Test with mixed True/False          |

## Integration with mutmut

### Running mutmut

```bash
# Always through the make target — never call mutmut directly
make mutate

# Under the hood, this runs:
uv run mutmut run
```

mutmut supports scoping a run to specific files/modules with Unix filename pattern matching
on the dotted module path:

```bash
uv run mutmut run "{{ general.source_name }}.module_name*"
```

`make mutate` exposes this as the `MUTATE_PATH` var, so you don't have to call
mutmut directly to scope a run:

```bash
make mutate MUTATE_PATH="{{ general.source_name }}.module_name*"
```

To derive the pattern from a changed file, drop the `.py` extension and replace `/` with `.`:

```bash
# {{ general.source_name }}/module_name/foo.py -> {{ general.source_name }}.module_name.foo*
CHANGED_FILE="{{ general.source_name }}/module_name/foo.py"
MUTATE_PATH="$(echo "$CHANGED_FILE" | sed 's/\.py$//; s#/#.#g')*"
```

### Reading results

```bash
# Mutation score + summary of killed/survived/timeout/skipped mutants
uv run mutmut results

# Inspect one mutant's diff
uv run mutmut show <id>

# Interactive browser — press f to retest a function, m to retest a module
uv run mutmut browse

# Apply a mutant to disk to see the change in context, then revert
uv run mutmut apply <id>
git checkout -- .
```