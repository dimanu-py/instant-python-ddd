# Common test variables in setup_method

## Convention

When several tests in a class share variables that hold per-test state, initialize them in
`setup_method` instead of duplicating the initialization in every test or sharing a mutable object
across tests.

Keep a clear split:

- **Mutable per-test state** — objects a test reads, writes, or observes (an event log, a recorder,
  a buffer) are re-created in `setup_method`, so every test starts from the same clean slate.
- **Immutable shared fixtures** — data tests only read (canned answers, expected messages) stay as
  class attributes (`ClassVar`), since no test can corrupt them.

```python
class TestQuestionaryConsoleWizard:
    happy_path_answers: ClassVar[list[object]] = [...]

    def setup_method(self) -> None:
        self._event_log: list[str] = []
```

## Benefits

- Tests are isolated: a test can never see leftovers written by a previous test.
- Setup lives in one place, so adding a test cannot forget to initialize the shared state.
- Class-level mutable state disappears, removing order-dependent failures and `xdist` surprises.
- The test bodies stay focused on the behavior, not on re-building their inputs.

## Examples

### Good: mutable state in `setup_method`, immutable fixtures as class attributes

```python
class TestWizard:
    answers: ClassVar[list[object]] = [...]

    def setup_method(self) -> None:
        self._event_log: list[str] = []

    def test_first(self) -> None:
        ...  # starts with a fresh self._event_log

    def test_second(self) -> None:
        ...  # so does this one
```

### Bad: shared mutable class attribute

```python
class TestWizard:
    event_log: list[str] = []

    def test_first(self) -> None:
        self.event_log.append("...")

    def test_second(self) -> None:
        expect(self.event_log).to(equal([]))  # leaks the first test's entries
```

### Bad: duplicated inline initialization

```python
class TestWizard:
    def test_first(self) -> None:
        event_log: list[str] = []
        ...

    def test_second(self) -> None:
        event_log: list[str] = []
        ...  # same setup repeated; a third test can easily forget it
```

## Real world examples

- `test/config/infra/question_wizard/test_questionary_console_wizard.py` — `setup_method` creates
  `self._event_log`; `happy_path_answers` and `expected_question_messages` are `ClassVar` fixtures

## Related agreements

- `docs/conventions/testing/assertion-helper-methods.md` — build expected values in helpers so the
  assertion stays readable
- `docs/conventions/testing/tdd-outside-in.md` — test structure and placement conventions
