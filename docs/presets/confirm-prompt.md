# ConfirmPrompt

`ConfirmPrompt` renders a reusable Bootstrap modal confirmation dialog. Use it when you need a lightweight confirmation step before a destructive or important action.

This is an alternative to wrapping every button with `hx-confirm` individually. The modal can be triggered from any button using `data-bs-toggle="modal"` and `data-bs-target="#prompt-id"`.

---

## Quick Start

```python
from faststrap import ConfirmPrompt, Button

# Render the prompt somewhere in your layout (e.g. inside MainView)
ConfirmPrompt("Are you sure you want to delete this item?")

# Trigger it from a button
Button(
    "Delete Item",
    variant="danger",
    data_bs_toggle="modal",
    data_bs_target="#faststrap-confirm-prompt",
)
```

---

## Visual Examples & Use Cases

### 1. Basic Confirmation

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="modal fade" tabindex="-1" data-bs-backdrop="static" id="faststrap-confirm-prompt">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-body">Are you sure you want to delete this item?</div>
          <div class="modal-footer">
            <button data-bs-dismiss="modal" type="button" class="btn btn-secondary">Cancel</button>
            <button data-bs-dismiss="modal" type="button" class="btn btn-danger">Delete</button>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
ConfirmPrompt("Are you sure you want to delete this item?")
```
  </div>
</div>

### 2. Custom Confirm Text and Variant

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="modal fade" tabindex="-1" data-bs-backdrop="static" id="faststrap-confirm-prompt">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-body">Delete this project permanently?</div>
          <div class="modal-footer">
            <button data-bs-dismiss="modal" type="button" class="btn btn-secondary">Cancel</button>
            <button data-bs-dismiss="modal" type="button" class="btn btn-danger">Yes, delete</button>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
ConfirmPrompt(
    "Delete this project permanently?",
    confirm_button_text="Yes, delete",
    confirm_button_variant="danger",
)
```
  </div>
</div>

---

## Practical Functionality

### 1. HTMX Confirmation Pattern

```python
from faststrap import ConfirmPrompt, Button

# In your layout:
ConfirmPrompt("Delete this item?", id="delete-confirm")

# In your item list:
Button(
    "Delete",
    variant="danger",
    data_bs_toggle="modal",
    data_bs_target="#delete-confirm",
    hx_delete=f"/items/{item_id}",
    hx_target="#item-list",
    hx_swap="outerHTML",
)
```

### 2. Multiple Confirmation Prompts

```python
# Each prompt needs a unique ID
ConfirmPrompt("Delete item?", id="delete-item-confirm")
ConfirmPrompt("Archive project?", id="archive-project-confirm")

# Trigger with matching data-bs-target
Button("Delete", data_bs_toggle="modal", data_bs_target="#delete-item-confirm")
Button("Archive", data_bs_toggle="modal", data_bs_target="#archive-project-confirm")
```

### 3. With Server-Side Logic

```python
@app.post("/items/{item_id}/delete")
def delete_item(item_id: int):
    item = get_item(item_id)
    if not item:
        return Alert("Item not found", variant="warning")
    db.delete(item)
    return Toast("Item deleted", variant="success")
```

---

## Parameter Reference

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `message` | `str` | `"Are you sure?"` | Confirmation message to display. |
| `confirm_button_text` | `str \| None` | `None` | Text for the confirm button. Defaults to the capitalized first word of the message. |
| `cancel_button_text` | `str \| None` | `None` | Text for the cancel button. Defaults to `"Cancel"`. |
| `confirm_button_variant` | `str` | `"danger"` | Bootstrap variant for the confirm button. |
| `id` | `str` | `"faststrap-confirm-prompt"` | HTML ID for the modal (used with `data-bs-target`). |
| `**kwargs` | `Any` | `{}` | Additional HTML attributes passed to the modal container. |

---

## API Reference

::: faststrap.presets.interactions.ConfirmPrompt
    options:
        show_source: true
        heading_level: 4
