# Response Helpers

Server-side response utilities for common HTMX patterns. These eliminate boilerplate for HTMX server-side interactions.

## Import

```python
from faststrap.presets import (
    hx_redirect,
    hx_refresh,
    hx_trigger,
    hx_reswap,
    hx_retarget,
    toast_response,
    multi_response,
)
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
| `status_code` | `int` | `204` | HTTP success status code |

!!! note
    `HX-Redirect` should be returned with a `2xx` status code.
    A browser redirect like `303` bypasses HTMX header handling.

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

!!! note
    Event names should use HTMX-safe characters such as letters, numbers,
    `_`, `:`, `.`, and `-`.

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

## multi_response *(beta)*

Bundles a primary response with one or more out-of-band (OOB) swapped elements and an optional toast notification into a single response tuple compatible with both HTMX 2 and HTMX 4.

```python
from faststrap.presets import multi_response
from faststrap import Card, Badge, StatCard

@app.post("/tasks/complete")
def complete_task(task_id: int):
    # 1. Primary content for the invoking button's target
    primary = Button("Completed", variant="success", disabled=True)

    # 2. Out-of-band updates across the page
    badge_update = Badge("Done", id=f"status-{task_id}", hx_swap_oob="true")
    kpi_update = StatCard(title="Completed Tasks", value=15, id="kpi-completed", hx_swap_oob="outerHTML:#kpi-completed")

    return multi_response(
        primary,
        badge_update,
        kpi_update,
        toast=("Task marked as complete", "success"),
    )
```

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `primary` | `Any` | **required** | Primary response element targeted by the triggering request |
| `*oob_targets` | `Any` | `()` | Additional elements to swap out-of-band elsewhere in the DOM. Automatically gets `hx_swap_oob="true"` if not already set. |
| `toast` | `str \| tuple[str, str] \| Any \| None` | `None` | Optional toast message (`str`), `(message, variant)` tuple, or Toast element to swap into the toast container |
| `toast_container_id` | `str` | `"toast-container"` | ID of the target toast container |

---

## hx_reswap / hx_retarget

Dynamically change the swap strategy or target from the server:

```python
# Change swap strategy
return hx_reswap("outerHTML", content="<div>New content</div>")

# Change target
return hx_retarget("#error-panel", content=Alert("Error!"))
```
