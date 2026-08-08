# Error Handling Guide

This guide covers error handling patterns for FastHTML apps built with Faststrap.

---

## Error Types

| Error | HTTP Status | Component |
| --- | --- | --- |
| Validation errors | 200 (form re-render) | `FormErrorSummary` |
| Not found | 404 | `ErrorPage` |
| Server error | 500 | `ErrorPage` |
| Authorization | 403 | `ErrorPage` |
| User action | 200 | `ErrorDialog` |
| Success feedback | 200 | `Toast` |

---

## ErrorPage

`ErrorPage` renders a styled error page for 404, 500, and other HTTP errors.

```python
from faststrap import ErrorPage

@app.get("/items/{item_id}")
def get_item(item_id: int):
    item = get_item_or_404(item_id)
    if not item:
        return ErrorPage(
            code=404,
            title="Item Not Found",
            message="The item you're looking for doesn't exist.",
            back_href="/items",
        )
    return ItemPage(item)
```

### Custom Error Pages

```python
ErrorPage(
    code=500,
    title="Something went wrong",
    message="We're working on fixing this.",
    icon="exclamation-triangle",
    show_details=True,
)
```

---

## ErrorDialog

`ErrorDialog` renders an error in a Bootstrap modal for inline errors.

```python
from faststrap import ErrorDialog

ErrorDialog(
    "Failed to save changes",
    details="The server returned an unexpected response.",
    variant="danger",
)
```

---

## Form Errors

See [Validation Guide](../guides/validation.md) for complete form validation patterns.

Quick example:

```python
from faststrap import FormErrorSummary, FormGroupFromErrors

@app.post("/login")
def login(email: str, password: str):
    errors = validate(email, password)
    if errors:
        return (
            FormErrorSummary(errors),
            FormGroupFromErrors(Input(name="email", value=email), "email", errors=errors),
            FormGroupFromErrors(Input(name="password"), "password", errors=errors),
        )
    return RedirectResponse("/dashboard")
```

---

## Toast Notifications

```python
from faststrap import Toast

# Success
Toast("Changes saved successfully!", variant="success")

# Error
Toast("Something went wrong. Please try again.", variant="danger")

# Warning
Toast("Your session expires in 5 minutes.", variant="warning")

# Info
Toast("New features are available.", variant="info")
```

---

## Complete Error Flow

```python
from fasthtml.common import *
from faststrap import *

app, rt = fast_app()

@app.before
def add_bootstrap(req, resp):
    return add_bootstrap(req, resp)

@rt("/items/{item_id}/delete")
def delete_item(item_id: int, req, resp):
    item = get_item(item_id)
    if not item:
        return ErrorPage(404, "Item Not Found", back_href="/items")

    if not can_delete(item, req):
        return ErrorPage(403, "Forbidden", message="You don't have permission to delete this item.")

    try:
        db.delete(item)
        return Toast("Item deleted successfully", variant="success")
    except Exception as e:
        return ErrorDialog(
            "Delete Failed",
            details=str(e),
            variant="danger",
        )

serve()
```

---

## See Also

- [Validation Guide](../guides/validation.md)
- [HTMX Integration Guide](../guides/htmx-integration.md)
- [Form Errors Component Reference](../components/forms/form-errors.md)
