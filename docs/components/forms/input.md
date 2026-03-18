# Input

The `Input` component allows users to enter text, numbers, passwords, emails, and more. It wraps the standard HTML `<input>` element with comprehensive Bootstrap styling, validation states, and floating labels.

!!! tip "Bootstrap Reference"
    [Bootstrap 5 Form Controls Documentation](https://getbootstrap.com/docs/5.3/forms/form-control/)

---

## Quick Start

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="w-100">
      <label class="form-label">Full Name</label>
      <input type="text" class="form-control" placeholder="Enter your name">
    </div>
  </div>
  <div class="preview-code" markdown>
```python
Input("full_name", placeholder="Enter your name", label="Full Name")
```
  </div>
</div>

---

## Visual Examples & Use Cases

### 1. Types & Labels
FastStrap supports all HTML5 input types. Adding a `label` argument automatically creates a properly accessible `<label>` associated with the input.

!!! note "Code & Output"
<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="w-100 d-flex flex-column gap-3">
      <div>
        <label class="form-label">Email Address</label>
        <input type="email" class="form-control" placeholder="name@example.com">
      </div>
      <div>
        <label class="form-label">Password</label>
        <input type="password" class="form-control">
      </div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
Input("email", input_type="email", label="Email Address", placeholder="name@example.com")
Input("password", input_type="password", label="Password")
```
  </div>
</div>

### 2. Sizing
Match inputs to buttons or other components using `size`.

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="w-100 d-flex flex-column gap-3">
      <input type="text" class="form-control form-control-lg" placeholder="Large Input">
      <input type="text" class="form-control" placeholder="Default Input">
      <input type="text" class="form-control form-control-sm" placeholder="Small Input">
    </div>
  </div>
  <div class="preview-code" markdown>
```python
Input("large_input", placeholder="Large Input", size="lg")
Input("default_input", placeholder="Default Input")
Input("small_input", placeholder="Small Input", size="sm")
```
  </div>
</div>

### 3. Utility Text and Disabled State
Add flexible helper text below the input using `help_text`. Use `disabled` or `readonly` to restrict interaction.

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="w-100">
      <label class="form-label">Username</label>
      <input type="text" class="form-control" value="jdoe_archived" disabled>
      <div class="form-text">Must be 8-20 characters long.</div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
Input(
    "username",
    label="Username", 
    help_text="Must be 8-20 characters long.",
    disabled=True,
    value="jdoe_archived"
)
```
  </div>
</div>

---

## Practical Functionality

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="w-100 d-flex flex-column gap-3">
      <div class="has-validation">
        <input type="text" class="form-control is-valid" value="Correct!">
        <div class="valid-feedback">This username is available.</div>
      </div>
      <div class="has-validation">
        <input type="text" class="form-control is-invalid" value="Invalid data">
        <div class="invalid-feedback">Please provide a valid entry.</div>
      </div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
# Valid state (Green border)
Input("username", validation_state="valid", value="Correct!")

# Invalid state (Red border)
Input("username", validation_state="invalid", value="Invalid data")
```
  </div>
</div>

### 2. Floating Labels
Bootstrap's modern "Floating Label" pattern moves the label *inside* the input, floating up when the user types.

```python
<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="form-floating w-100">
      <input type="email" class="form-control" id="floatingInput" placeholder="name@example.com">
      <label for="floatingInput">Email Address</label>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
FloatingLabel(
    Input("email", placeholder="name@example.com"),
    label="Email Address"
)
```
  </div>
</div>

### 3. HTMX Integration
Trigger server requests on user input (e.g., live search).

```python
Input(
    "search",
    input_type="search",
    placeholder="Search users...",
    hx_get="/search_users",
    hx_trigger="keyup changed delay:500ms", # Wait 500ms after typing stops
    hx_target="#search-results"
)
```

---

## Advanced Customization

### 1. CSS Variables
Customize standard form colors and spacing.

| CSS Variable | Description |
| :--- | :--- |
| `--bs-body-bg` | Background color of input. |
| `--bs-body-color` | Text color. |
| `--bs-border-color` | Default border color. |
| `--bs-focus-ring-color` | Glow color when focused. |

### 2. Input Groups
Combine inputs with text or buttons using `InputGroup`.

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="input-group w-100">
      <span class="input-group-text">@</span>
      <input type="text" class="form-control" placeholder="Username">
      <span class="input-group-text">.com</span>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
InputGroup(
    InputGroupText("@"),
    Input("username", placeholder="Username"),
    InputGroupText(".com")
)
```
  </div>
</div>

---

## Parameter Reference

| FastStrap Param | Type | Bootstrap / HTML Attribute | Description |
| :--- | :--- | :--- | :--- |
| `name` | `str` | `name="..."` | Form field name. Required for form submission and label/input association. |
| `input_type` | `str` | `type="..."` | HTML5 input type (`text`, `password`, `email`, `number`, `date`, etc.). Default `text`. |
| `label` | `str` | `<label>` | Text for the associated label element. |
| `placeholder` | `str` | `placeholder="..."` | Ghost text shown when empty. |
| `value` | `Any` | `value="..."` | Initial value of the input. |
| `help_text` | `str` | `.form-text` | Helper text displayed below the input. |
| `size` | `str` | `.form-control-{size}` | Size: `sm` or `lg`. |
| `disabled` | `bool` | `disabled` | Disables interaction. |
| `readonly` | `bool` | `readonly` | Value is visible but not editable. |
| `required` | `bool` | `required` | analyzing browser validation. |

::: faststrap.components.forms.input.Input
    options:
        show_source: true
        heading_level: 4
