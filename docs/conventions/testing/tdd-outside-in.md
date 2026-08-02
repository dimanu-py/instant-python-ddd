# Outside-In TDD

## Convention

Every feature is built using Outside-In (London School) TDD. An acceptance test drives the outermost layer, 
and each inner layer is driven by the tests of the layer above it.

### Test pyramid

```
            ╱  acceptance  ╲            happy paths + critical errors — TestClient
           ╱  delivery unit ╲           all scenarios, use case mocked — doublex
          ╱  application unit ╲         business logic, ports mocked — doublex
         ╱  infra integration  ╲        real adapters (DB, IO) — pytest
```

| Type              | Layer tested          | Target                             | Mocking            | Tools                            |
|-------------------|-----------------------|------------------------------------|--------------------|----------------------------------|
| Acceptance        | delivery (full stack) | happy paths + critical errors      | real dependencies  | FastAPI TestClient, pytest       |
| Delivery unit     | delivery              | all scenarios (edge cases, errors) | use case mocked    | pytest, doublex or unittest.mock |
| Application unit  | application           | business rules, orchestration      | infra ports mocked | pytest, doublex or unittest.mock |
| Infra integration | infra                 | adapter correctness                | real DB/adapter    | pytest                           |

### TDD cycle per feature

```
1. Write acceptance test → Red
2. Implement delivery + stub application layer → Green
3. Write delivery unit tests (mock use case) → Red
4. Harden delivery code → Green
5. Write application unit tests → Red
6. Implement application layer (stub domain/infra) → Green
7. Continue for each inner layer until all are real
8. Write infra integration tests
```

Each step follows strict TDD: Red → Green → Refactor before moving to the next.

### Test markers

Tag every test file with a `@pytest.mark` marker indicating the layer under test:

| Marker               | Layer            | File location                           |
|----------------------|------------------|-----------------------------------------|
| `@pytest.mark.acceptance` | Delivery (full stack) | `test/<feature>/delivery/test_acceptance.py` |
| `@pytest.mark.unit`  | All unit tests   | `test/<feature>/**/test_*.py` (excluding acceptance) |

Class-level markers keep test files clean:

```python
@pytest.mark.acceptance
class TestRegisterUsageEvent:
    """Acceptance tests for POST /api/v1/events."""

    def test_valid_usage_event_returns_201_with_id_and_location(self, client: TestClient) -> None:
        ...
```

```python
@pytest.mark.unit
class TestRegisterUsageEventRouter:
    """Unit tests for POST /api/v1/events router."""

    def test_missing_required_field_returns_422(self, client: TestClient) -> None:
        ...
```

### Requirement references in test names

Link every test back to its EARS requirement using an `R<n>` tag in the docstring. This creates traceability between the spec file and the test suite:

```python
def test_valid_usage_event_returns_201_with_id_and_location(self, client: TestClient) -> None:
    """R1: Register a valid usage event with all fields."""
    ...
```

```python
def test_missing_required_field_returns_422(self, client: TestClient) -> None:
    """R2: Missing a required field returns 422."""
    ...
```

The `R<n>` tags correspond to the requirement ids in `docs/specs/<feature>.md`.

### Testing the delivery layer

Delivery tests use FastAPI `TestClient` against the ASGI app. Two categories:

**Acceptance tests** — one file per feature, covering the happy path and critical system errors. These test 
the real stack end-to-end. They are few and focus on proving the feature works.

```python
# tests/invoices/delivery/test_acceptance.py
from fastapi.testclient import TestClient

def test_create_invoice_returns_201_with_location(client: TestClient) -> None:
    response = client.post("/invoices", json={"amount": "100.00", "currency": "USD"})
    assert response.status_code == 201
    assert response.headers["location"] == "/invoices/1"
```

**Delivery unit tests** — cover every scenario the acceptance tests do not exercise: validation errors, malformed requests, edge cases, and error responses. The use case collaborator is mocked with doublex so the test stays in the delivery layer.

```python
# tests/invoices/delivery/test_router.py
from doublex import ANY_ARG, Mock, expect_call
from expects import expect, equal

def test_database_unavailable_returns_503(client: TestClient) -> None:
    from usage_events.delivery.router import _get_repository
    from usage_events.domain.usage_event_repository import UsageEventRepository

    repository = Mock(UsageEventRepository)
    expect_call(repository).save(ANY_ARG).raises(RuntimeError("Database connection failed"))

    client.app.dependency_overrides[_get_repository] = lambda: repository

    response = client.post("/api/v1/events", json=valid_payload)

    expect(response.status_code).to(equal(503))
```

### Testing the application layer

Application tests exercise use cases in isolation. Infra port dependencies are mocked with doublex. These tests cover business rules, orchestration logic, and error handling.

```python
# tests/invoices/application/test_create_invoice.py
from doublex import ANY_ARG, Mock, expect_call
from expects import expect, be_none, have_properties

def test_creates_invoice_and_saves() -> None:
    repo: Any = Mock(InvoiceRepository)
    expect_call(repo).save(ANY_ARG)
    use_case = CreateInvoiceUseCase(repo)
    event_id = use_case.execute(amount="100.00", currency="USD")

    expect(event_id).to_not(be_none)
    saved_event = repo.save.calls[0].args[0]
    expect(saved_event).to(have_properties(amount="100.00", currency="USD"))
```

### Testing the infra layer

Infra integration tests run against real dependencies (PostgreSQL, external services). They verify adapter contracts match what the domain port promises.

```python
# tests/invoices/infra/test_postgres_invoice_repository.py
def test_saves_and_retrieves_invoice(db_session: Session) -> None:
    repo = PostgresInvoiceRepository(db_session)
    invoice = InvoiceMother.completed()
    repo.save(invoice)
    retrieved = repo.get(invoice.id)
    assert retrieved == invoice
```

### Test directory structure

```
tests/
  invoices/
    delivery/
      test_acceptance.py        # full-stack happy paths
      test_router.py            # unit tests, use case mocked
    application/
      test_create_invoice.py    # unit tests, ports mocked
      test_list_invoices.py
    infra/
      test_postgres_invoice_repository.py  # integration tests
```

File naming: `test_<module>.py`, matching the module under test in `src/`.

### Object mothers

Test data factories live in `src/<feature>/domain/mothers/`. They are importable by both tests and production code (for seeding).

```
src/
  invoices/
    domain/
      mothers/
        invoice_mother.py       # domain.Mother.completed(), .with_items(...)
```

Mothers follow a builder pattern with sensible defaults and named methods for variations:

```python
# src/invoices/domain/mothers/invoice_mother.py
class InvoiceMother:
    @staticmethod
    def completed(**overrides: Any) -> Invoice:
        return Invoice(
            id=overrides.get("id", InvoiceId.new()),
            status=overrides.get("status", InvoiceStatus.COMPLETED),
            ...
        )
```

## Benefits

- **Safety net from the outside** — the acceptance test proves the feature works end-to-end before any layer is fully implemented.
- **Contract-first development** — delivery unit tests encode the HTTP contract (status codes, response shapes) before the use case exists.
- **Isolated, fast unit tests** — each layer is tested in isolation with mocked neighbours, keeping the suite fast.
- **Real adapter coverage** — infra integration tests catch database and IO issues that unit tests miss.
- **One Red-Green-Refactor per layer** — prevents building abstractions before they are driven by a test.

## Examples

### Good: Outside-In flow for create invoice

1. Write acceptance test: `POST /invoices → 201` → Red (no router)
2. Implement `delivery/router.py` → stubs `CreateInvoiceUseCase` → Green
3. Write delivery unit test: missing amount returns 422 → Red
4. Add validation to router → Green → Refactor
5. Write application test: use case calls repo.save → Red
6. Implement `CreateInvoiceUseCase` → Green
7. Write infra integration test: save and retrieve → Red
8. Implement `PostgresInvoiceRepository` → Green

### Bad: Starting from the domain layer

Write `Invoice` aggregate and `InvoiceRepository` port first, then build the use case, then add the router. No acceptance test exists until everything is wired. The domain might be over-engineered because no outer-layer test drove its shape.

### Bad: Mixing test layers

A delivery unit test that also asserts database queries. Slow, coupled, and duplicates both delivery unit and infra integration concerns.

## Real world examples

- `tests/` — all tests follow this structure
- `src/<feature>/domain/mothers/` — object mothers per feature

## Related agreements

- `docs/conventions/architecture/architecture.md` — the code structure these tests exercise
- `docs/conventions/testing/doublex-mocking.md` — doublex mocking patterns for repository ports
- `docs/agents/convention_guidelines.md` — document structure standard
