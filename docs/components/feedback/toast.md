# Toast

Toasts are lightweight, non-blocking notifications. They are designed to mimic the push notifications popularized by mobile and desktop operating systems.

!!! tip "Bootstrap Reference"
    [Bootstrap 5 Toasts](https://getbootstrap.com/docs/5.3/components/toasts/)

---

## Quick Start

In FastStrap, we use `SimpleToast` for the most common case: a simple text message with a variant color.

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render" style="background: #f0f2f5;">
    <div class="toast show align-items-center text-white bg-success border-0" role="alert" aria-live="assertive" aria-atomic="true">
      <div class="d-flex">
        <div class="toast-body">
          Success! Item added to cart.
        </div>
        <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
      </div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
SimpleToast("Success! Item added to cart.", variant="success")
```
  </div>
</div>

---

## Visual Examples & Use Cases

### 1. SimpleToast Variants
Standard colors to communicate status.

!!! note "Code & Output"
    ```python
    SimpleToast("File uploaded.", variant="info")
    SimpleToast("Connection lost.", variant="danger")
    ```

### 2. Full Control (Standard Toast)
For rich content, headers, and custom timing, use the base `Toast` component.

!!! note "Code & Output"
<div class="component-preview">
  <div class="preview-header">Live Preview (Rich Toast)</div>
  <div class="preview-render" style="background: #f0f2f5;">
    <div class="toast show" role="alert" aria-live="assertive" aria-atomic="true">
      <div class="toast-header">
        <strong class="me-auto">Messenger</strong>
        <small>Just now</small>
        <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
      </div>
      <div class="toast-body">
        Your message has been sent.
      </div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
Toast(
    "Your message has been sent.",
    title="Messenger",
    cls="shadow-sm",
    delay=5000
)
```
  </div>
</div>

### 3. Toast Container
Toasts are often grouped. FastStrap handles the `ToastContainer` logic to ensure they stack correctly in the corner of the screen.

```python
from faststrap import ToastContainer, add_bootstrap

# 1. Add container to your main layout
app_layout = [
    MainView(),
    ToastContainer(position="bottom-end") # Global container
]
```

---

## Practical Functionality

### 1. Triggering Toasts via HTMX
The most common implementation is to return a Toast as part of an HTMX response (using `hx-swap="beforeend"` targetting the Toast Container).

```python
@app.route("/add_item")
def add_item():
    # ... logic ...
    return SimpleToast("Item Added", variant="success") # Appends to existing list
```

---

## Parameter Reference

| FastStrap Param | Type | Bootstrap Attribute | Description |
| :--- | :--- | :--- | :--- |
| `title` | `Any` | `.toast-header` | Optional header element/text. |
| `autohide` | `bool` | `data-bs-autohide` | If `True`, closes automatically. |
| `delay` | `int` | `data-bs-delay` | Duration in milliseconds before closing. |
| `position` | `str` | - | Location: `top-end`, `bottom-start`, etc. |

::: faststrap.components.feedback.toast.SimpleToast
    options:
        show_source: true
        heading_level: 4
