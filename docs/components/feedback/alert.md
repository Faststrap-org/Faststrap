# Alert

Alerts provide contextual feedback messages for typical user actions with a handful of available and flexible alert messages.

!!! tip "Bootstrap Reference"
    [Bootstrap 5 Alerts](https://getbootstrap.com/docs/5.3/components/alerts/)

---

## Quick Start

<iframe
  src="https://preview.faststrap.dev/embed/Alert?variant=success&text=Your+profile+has+been+updated!"
  width="100%"
  height="140"
  frameborder="0"
  data-faststrap-preview
></iframe>

<div class="mb-3 text-end">
  <a href="https://preview.faststrap.dev/studio/Alert" target="_blank" class="btn btn-sm btn-outline-primary">
    ⚡ Open in FastStrap Studio →
  </a>
</div>

```python
Alert("Your profile has been updated!", variant="success")
```


---

## Visual Examples & Use Cases

### 1. Dismissible Alerts
Allow users to close the alert. This is handled automatically by Bootstrap's JS via FastStrap's `dismissible=True`.

!!! note "Code & Output"
<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="alert alert-warning alert-dismissible fade show w-100" role="alert">
      Important: Your session expires in 5 minutes.
      <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
Alert("Important: Your session expires in 5 minutes.", 
      variant="warning", dismissible=True)
```
  </div>
</div>

### 2. Rich Content
Alerts can contain headings, links, and multiple paragraphs.

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="alert alert-success w-100" role="alert">
      <h4 class="alert-heading">Well done!</h4>
      <p>Aww yeah, you successfully read this important alert message.</p>
      <hr>
      <p class="mb-0">Whenever you need to, be sure to use margin utilities to keep things nice and tidy.</p>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
from fasthtml.common import H4, P, Hr

Alert(
    H4("Well done!", cls="alert-heading"),
    P("Aww yeah, you successfully read this important alert message."),
    Hr(),
    P("Whenever you need to, be sure to use margin utilities to keep things nice and tidy."),
    variant="success"
)
```
  </div>
</div>

### 3. Icons
Adding icons to alerts significantly improves user recognition of message status.

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="alert alert-danger d-flex align-items-center w-100" role="alert">
      <i class="bi bi-exclamation-triangle-fill me-2"></i>
      <div>An error occurred while saving.</div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
Alert(
    " An error occurred while saving.", 
    variant="danger", 
    icon="exclamation-triangle-fill"
)
```
  </div>
</div>

---

## Practical Functionality

### 1. HTMX Integration (Auto-remove)
Commonly used for temporary notifications that should disappear after an HTMX update.

```python
# Alert is removed from DOM after being seen (requires custom JS or HTMX trick)
Alert(
    "Saved!", 
    variant="success", 
    hx_get="/clear_notification", 
    hx_trigger="load delay:3s" # Disappears after 3 seconds
)
```

---

## Advanced Customization

### 1. CSS Variables

| CSS Variable | Description |
| :--- | :--- |
| `--bs-alert-bg` | Background color. |
| `--bs-alert-color` | Text color. |
| `--bs-alert-border-color` | Border color. |
| `--bs-alert-padding-x` | Padding. |
| `--bs-alert-link-color` | Color for `<A>` tags inside. |

---

## Parameter Reference

| FastStrap Param | Type | Bootstrap Class | Description |
| :--- | :--- | :--- | :--- |
| `variant` | `str` | `.alert-{variant}` | Color theme. |
| `dismissible` | `bool` | `.alert-dismissible` | Adds a close button. |
| `icon` | `str` | - | Bootstrap icon name to prepend. |

::: faststrap.components.feedback.alert.Alert
    options:
        show_source: true
        heading_level: 4
