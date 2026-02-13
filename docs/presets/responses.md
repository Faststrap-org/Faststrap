# Response Helpers

Server-side response utilities for common HTMX patterns. These eliminate boilerplate for HTMX server-side interactions.

## Import

```python
from faststrap.presets import hx_redirect, hx_refresh, hx_trigger, toast_response
```

---

## hx_redirect

Triggers a client-side redirect via the HTMX `HX-Redirect` header.

```python
@app.post("/login")
def login(email: str, password: str):
    # ... authenticate ...
    return hx_redirect("/dashboard")
```

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `url` | `str` | **required** | URL to redirect to |
| `status_code` | `int` | `200` | HTTP status code |

---

## hx_refresh

Triggers a full page refresh via HTMX `HX-Refresh` header.

```python
@app.post("/update-settings")
def update_settings():
    # ... update settings ...
    return hx_refresh()
```

!!! warning
    Use sparingly. Prefer targeted updates with `hx-target` when possible.

---

## hx_trigger

Triggers a client-side event via the `HX-Trigger` header.

```python
# Simple event
return hx_trigger("itemUpdated")

# Event with detail data
return hx_trigger("itemUpdated", detail={"id": 123})

# Multiple events
return hx_trigger({
    "itemUpdated": {"id": 123},
    "showNotification": {"message": "Saved!"}
})
```

---

## toast_response

**Killer feature**: Returns your normal HTMX response PLUS an out-of-band toast notification.

```python
@app.post("/save")
def save():
    return toast_response(
        content=Card("Record updated!"),   # Goes to hx-target
        message="Changes saved!",           # Appears as toast
        variant="success",
    )
```

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `content` | `Any` | **required** | Main response content |
| `message` | `str` | **required** | Toast message text |
| `variant` | `str` | `"success"` | Toast variant (success, danger, warning, info) |
| `toast_id` | `str` | `"toast-container"` | ID of the toast container |

!!! important "Requires ToastContainer"
    Your page must have a `ToastContainer` element:
    ```python
    ToastContainer(position="top-end")
    ```

---

## hx_reswap / hx_retarget

Dynamically change the swap strategy or target from the server:

```python
# Change swap strategy
return hx_reswap("outerHTML", content="<div>New content</div>")

# Change target
return hx_retarget("#error-panel", content=Alert("Error!"))
```
