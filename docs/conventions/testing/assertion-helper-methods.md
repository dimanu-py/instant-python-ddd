# Semantic helper methods for setup and assertions

## Convention

Extract test steps into purpose-revealing helper methods named after the behavior they set up or
verify, so the test body reads as a story of what happens instead of a list of mechanics.

There are two kinds of helpers:

- **Setup helpers** arrange the world before the action: they set collaborator expectations,
  prepare inputs, or configure state. Name them for the behavior being arranged (e.g.
  `_should_charge_the_customer()` sets up the expectation that the payment goes through).
- **Assertion helpers** build or check the expected outcome: they derive the expected value or
  verify a result so the assertion stays a single readable line (e.g.
  `_expected_receipt_lines()`).

A test reads top to bottom: setup helpers, the action, then the assertion.

## Benefits

- The test reads top to bottom like a story: setup helpers, the action, then the assertion.
- Helper names explain what is arranged or verified without a comment.
- Repeated arrangements and expected values live in one method, not scattered inline in each test.
- Changes to a behavior's setup or to the expected shape are made in one place.
- A shared setup helper keeps its body in sync across every test that uses it.

## Examples

### Good: semantic setup helpers

```python
def test_should_charge_the_customer_when_checkout_succeeds(self) -> None:
    self._should_check_that_the_customer_has_balance()
    self._should_charge_the_customer()

    self._checkout.run(cart=self._cart)

    expect(self._payment_gateway).to(have_been_satisfied)

def _should_check_that_the_customer_has_balance(self) -> None:
    expect_call(self._payment_gateway).has_balance(self._customer).returns(True)

def _should_charge_the_customer(self) -> None:
    expect_call(self._payment_gateway).charge(self._customer, self._cart.total).returns(self._receipt)
```

The helper names describe the world being arranged, so the test body reads as a story.

### Good: assertion against a helper-built expected value

```python
def test_should_print_one_line_per_product_in_the_receipt(self) -> None:
    ...

    expect(self._printed_lines).to(equal(self._expected_receipt_lines()))

def _expected_receipt_lines(self) -> list[str]:
    return [f"{product.name}: {product.price}" for product in self._cart.products]
```

The expected value is derived in one place, so the assertion stays a single readable line.

### Bad: mechanic-by-mechanic setup inlined in the test

```python
def test_should_charge_the_customer_when_checkout_succeeds(self) -> None:
    expect_call(self._payment_gateway).has_balance(self._customer).returns(True)
    expect_call(self._payment_gateway).charge(self._customer, self._cart.total).returns(self._receipt)

    self._checkout.run(cart=self._cart)

    expect(self._payment_gateway).to(have_been_satisfied)
```

The intent is buried under wiring, and every test that shares this setup must repeat it.

### Bad: long expected value inlined in the assertion

```python
expect(self._printed_lines).to(equal([
    "apple: 1.20",
    "banana: 0.80",
    ...
]))
```

The intent is buried under data, and the test must be re-read line by line to see what it pins.

## Real world examples

- `test/initialize/infra/env_manager/test_uv_env_manager.py` — `_should_*` setup helpers arrange
  the console expectations so each test reads as a story
- `test/config/infra/question_wizard/test_questionary_console_wizard.py` —
  `_expected_events_with_section_headings()` builds the full chronological event log that the
  assertion compares against

## Related agreements

- `docs/conventions/testing/common-test-variables-in-setup-method.md` — where the shared inputs for
  these helpers come from
- `docs/conventions/testing/tdd-outside-in.md` — test structure and placement conventions
