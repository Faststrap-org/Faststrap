# Notification Presets

Faststrap includes lightweight notification presets built on `Toast` and `Alert`.

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

## Generic toast

```python
NoticeToast("Custom message", kind="success", title="Done")
```

## Alert preset

```python
NoticeAlert("Something changed", kind="info")
```

## Note

For HTMX out-of-band responses, continue using:

```python
from faststrap.presets import toast_response
```

with a `ToastContainer` in your page layout.

