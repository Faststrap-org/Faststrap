# Modal

Modals are "dialogs" that appear in front of the application content. They provide critical information, require user confirmation, or host complex forms.

!!! tip "Bootstrap Reference"
    [Bootstrap 5 Modals](https://getbootstrap.com/docs/5.3/components/modal/)

---

## Quick Start

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render" style="background: #f0f2f5;">
    <div class="modal position-static d-block" tabindex="-1">
      <div class="modal-dialog m-0">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Example Modal</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <p>Hello! This is a modal dialog.</p>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button type="button" class="btn btn-primary">Save</button>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
# The Trigger
trigger = Button("Launch Modal", data_bs_toggle="modal", data_bs_target="#myModal")

# The Modal Definition
modal = Modal(
    "Hello! This is a modal dialog.", 
    title="Example Modal", 
    modal_id="myModal",
    footer=Button("Save", variant="primary")
)
```
  </div>
</div>

---

## Visual Examples & Use Cases

### 1. Sizing
Specify the viewport width using `size`.

<div class="component-preview">
  <div class="preview-header">Live Preview (Sizing)</div>
  <div class="preview-render p-0 flex-column overflow-hidden" style="background: #f0f2f5;">
    <!-- Small Modal -->
    <div class="modal position-static d-block" tabindex="-1">
      <div class="modal-dialog modal-sm m-2">
        <div class="modal-content">
          <div class="modal-header"><h5 class="modal-title fs-6">Small Modal</h5></div>
        </div>
      </div>
    </div>
    <!-- Large Modal -->
    <div class="modal position-static d-block" tabindex="-1">
      <div class="modal-dialog modal-lg m-2">
        <div class="modal-content">
          <div class="modal-header"><h5 class="modal-title fs-6">Large Modal</h5></div>
        </div>
      </div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
Modal(..., size="sm") # Small
Modal(..., size="lg") # Large
```
  </div>
</div>

### 2. Centered & Scrollable
Handle long content or improve ergonomics by centering the dialog.

<div class="component-preview">
  <div class="preview-header">Live Preview (Centered)</div>
  <div class="preview-render" style="background: #f0f2f5;">
    <div class="modal position-static d-block" tabindex="-1">
      <div class="modal-dialog modal-dialog-centered m-0">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Vertically Centered</h5>
          </div>
          <div class="modal-body">
            <p>This modal is centered on the screen.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
Modal(
    "This modal is centered on the screen.", 
    centered=True, 
    title="Vertically Centered"
)
```
  </div>
</div>

### 3. Static Backdrop
Prevents closing the modal when clicking the shaded background. Useful for high-stakes forms or "must-read" alerts.

```python
Modal(..., static_backdrop=True)
```

---

## Practical Functionality

### 1. ConfirmDialog (Preset)
FastStrap provides a specialized `ConfirmDialog` for standard "Are you sure?" scenarios. It simplifies the API by pre-configuring the "Yes/No" buttons.

```python
from faststrap import ConfirmDialog

ConfirmDialog(
    "Delete this post? This cannot be undone.",
    title="Confirm Deletion",
    dialog_id="confirmDelete",
    confirm_text="Yes, Delete It",
    variant="danger",
    hx_delete="/post/1", # Action on confirm
    hx_target="#post-1"
)
```
::: faststrap.components.feedback.confirm.ConfirmDialog
    options:
        show_source: false
        heading_level: 4

### 2. Real-time Loading
You can put HTMX content inside a modal body to load data only when opened.

```python
Modal(
    Div(hx_get="/api/user_details", hx_trigger="intersect once"), # Loads when modal opens
    title="User Profile",
    modal_id="profileModal"
)
```

---

## Focus Trap (Accessibility)

Trap keyboard focus inside the modal and optionally set autofocus:

```python
Modal(
    "Secure content",
    title="Accessible Dialog",
    focus_trap=True,
    autofocus_selector="#first-field",
)
```

## Parameter Reference

| FastStrap Param | Type | Bootstrap Attribute | Description |
| :--- | :--- | :--- | :--- |
| `title` | `str` | `.modal-title` | Text for the top header. |
| `footer` | `Any` | `.modal-footer` | Elements to put in bottom row. |
| `size` | `str` | `.modal-{size}` | `sm`, `lg`, `xl`, `fullscreen`. |
| `centered` | `bool` | `.modal-dialog-centered` | Vertically centers the dialog. |
| `scrollable` | `bool` | `.modal-dialog-scrollable` | Makes body scrollable independently. |
| `static_backdrop` | `bool` | `data-bs-backdrop` | `static` prevents click-to-close. |
| `keyboard` | `bool` | `data-bs-keyboard` | If `False`, Escape key won't close it. |

::: faststrap.components.feedback.modal.Modal
    options:
        show_source: false
        heading_level: 4
