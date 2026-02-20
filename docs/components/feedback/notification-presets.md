# Notification Presets

Faststrap includes lightweight notification presets built on `Toast` and `Alert`.

These presets help teams standardize feedback UX across apps without rebuilding notification patterns per project.

## Import

```python
from faststrap import (
    NoticeToast, NoticeAlert,
    SuccessToast, ErrorToast, WarningToast, InfoToast
)
```

## Toast presets

```python
SuccessToast("Profile saved")
ErrorToast("Request failed")
WarningToast("Storage almost full")
InfoToast("New update available")
```

## Why this is useful

- Faster implementation of common success/error/warning/info states.
- Consistent message styles across pages and features.
- Keeps code readable (`SuccessToast("Saved")` is clearer than repeating variant setup).

## Common use cases

1. CRUD feedback after save/delete/update.
2. Auth events (signed in, session expired).
3. Form submission status.
4. Background task/result notifications.

## Generic toast

```python
NoticeToast("Custom message", kind="success", title="Done")
```

## Alert preset

```python
NoticeAlert("Something changed", kind="info")
```

## Choosing toast vs alert

- Use toast for transient, non-blocking feedback.
- Use alert for inline, persistent feedback near related UI.

## Note

For HTMX out-of-band responses, continue using:

```python
from faststrap.presets import toast_response
```

with a `ToastContainer` in your page layout.

## Example page layout for HTMX toast responses

```python
Container(
    ToastContainer(position="top-end"),
    Div(id="content"),
)
```
