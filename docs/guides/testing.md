# Testing Guide

This guide covers testing strategies for FastHTML apps built with Faststrap.

---

## Test Setup

```bash
pip install pytest httpx
```

Create `tests/conftest.py`:

```python
import pytest
from fasthtml.test import TestClient
from main import app

@pytest.fixture
def client():
    return TestClient(app)
```

---

## Testing Routes

```python
def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome" in response.text

def test_contact_form_get(client):
    response = client.get("/contact")
    assert response.status_code == 200
    assert "Contact Us" in response.text

def test_contact_form_post_valid(client):
    response = client.post("/contact", data={
        "name": "John Doe",
        "email": "john@example.com",
        "message": "Hello, this is a test message.",
    })
    assert response.status_code == 200
    assert "Message sent" in response.text

def test_contact_form_post_invalid(client):
    response = client.post("/contact", data={
        "name": "J",
        "email": "invalid",
        "message": "Short",
    })
    assert response.status_code == 200
    assert "Name must be at least 2 characters" in response.text
```

---

## Testing HTMX Requests

```python
def test_search_htmx(client):
    response = client.get(
        "/search",
        headers={"HX-Request": "true"},
        params={"q": "test"},
    )
    assert response.status_code == 200
    assert "result" in response.text.lower()
```

---

## Testing Components

```python
def test_button_renders():
    from faststrap import Button
    button = Button("Click me", variant="primary")
    html = to_html(button)
    assert 'class="btn btn-primary"' in html
    assert "Click me" in html

def test_card_renders():
    from faststrap import Card
    card = Card("Hello", header="Title")
    html = to_html(card)
    assert "Title" in html
    assert "Hello" in html
```

---

## Testing Validation

```python
def test_form_error_summary():
    from faststrap import FormErrorSummary
    errors = {"email": "Invalid email", "password": "Too short"}
    result = FormErrorSummary(errors)
    html = to_html(result)
    assert "Invalid email" in html
    assert "Too short" in html

def test_form_group_from_errors():
    from faststrap import FormGroupFromErrors, Input
    errors = {"email": "Invalid email"}
    result = FormGroupFromErrors(
        Input(name="email", type="email", value="bad"),
        "email",
        errors=errors,
    )
    html = to_html(result)
    assert "is-invalid" in html
    assert "Invalid email" in html
```

---

## Test Patterns

### Pattern 1: Happy Path

```python
def test_create_item_success(client):
    response = client.post("/items", data={
        "name": "New Item",
        "description": "Test item",
    })
    assert response.status_code == 200
    assert "New Item" in response.text
```

### Pattern 2: Validation Errors

```python
def test_create_item_validation_error(client):
    response = client.post("/items", data={
        "name": "",
        "description": "",
    })
    assert response.status_code == 200
    assert "Name is required" in response.text
```

### Pattern 3: Not Found

```python
def test_item_not_found(client):
    response = client.get("/items/99999")
    assert response.status_code == 404
```

---

## Running Tests

```bash
pytest tests/ -v
```

With coverage:

```bash
pytest tests/ --cov=src --cov-report=html
```

---

## See Also

- [First App Tutorial](../getting-started/first-app.md)
- [Validation Guide](../guides/validation.md)
