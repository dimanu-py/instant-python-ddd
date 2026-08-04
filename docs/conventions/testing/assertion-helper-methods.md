# Assertion helper methods

## Convention

When an expected value is long or derived from several pieces of data, extract a purpose-revealing
helper method that builds it, so the assertion stays a single readable line and the test documents
the shape of the expected result.

```python
def test_should_display_section_heading_before_its_questions(self) -> None:
    ...

    expect(self._event_log).to(equal(self._expected_events_with_section_headings()))

def _expected_events_with_section_headings(self) -> list[str]:
    events: list[str] = []
    for heading, questions in sections:
        events.append(f"heading: {heading}")
        events.extend(f"question: {question}" for question in questions)
    return events
```

## Benefits

- The assertion reads top to bottom: run the action, then compare against one named value.
- The helper name explains what the expectation represents without a comment.
- Building the expected value in one place keeps it consistent and reusable across tests.
- Changes to the expected shape are made in one method, not scattered inline in each assertion.

## Examples

### Good: assertion against a helper-built expected value

```python
def test_should_display_section_heading_before_its_questions(self) -> None:
    fake_questionary = FakeQuestionary(answers=self.happy_path_answers, event_log=self._event_log)

    with patch("builtins.print", side_effect=record_heading):
        QuestionaryConsoleWizard(questionary=fake_questionary).run()

    expect(self._event_log).to(equal(self._expected_events_with_section_headings()))
```

### Bad: long expected value inlined in the assertion

```python
expect(self._event_log).to(equal([
    "heading: [1/4] General",
    "question: Enter the name of the project (CANNOT CONTAIN SPACES)",
    "question: Enter the name of the source folder",
    ...
]))
```

The intent is buried under data, and the test must be re-read line by line to see what it pins.

## Real world examples

- `test/config/infra/question_wizard/test_questionary_console_wizard.py` —
  `_expected_events_with_section_headings()` builds the full chronological event log that the
  assertion compares against

## Related agreements

- `docs/conventions/testing/common-test-variables-in-setup-method.md` — where the shared inputs for
  these assertions come from
- `docs/conventions/testing/tdd-outside-in.md` — test structure and placement conventions
