# Select

The `Select` component creates dropdown selection menus with full Bootstrap styling, validation support, and HTMX integration.

## Quick Start

```python
Select("country", ("us", "United States"), ("uk", "United Kingdom"), ("ca", "Canada"), ("au", "Australia"), label="Country")
```

## Usage Scenarios

### Sizes

```python
Select("priority", ("high", "High"), ("medium", "Medium"), label="Priority Level", size="lg")
Select("category", ("tech", "Technology"), ("design", "Design"), label="Category")
Select("status", ("active", "Active"), ("inactive", "Inactive"), label="Status", size="sm")
```

### Multiple Selection

```python
Select("skills", ("python", "Python"), ("javascript", "JavaScript"), ("html", "HTML/CSS"), ("sql", "SQL"), ("docker", "Docker"), label="Skills", help_text="Hold Ctrl/Cmd to select multiple", multiple=True)
```

### Pre-selected Options

```python
Select("theme", ("light", "Light Mode"), ("dark", "Dark Mode", True), ("auto", "Auto (System)"), label="Theme Preference")
```

### Validation States

```python
Select("plan", ("premium", "Premium Plan", True), label="Valid Selection", cls="is-valid")
```

## Parameter Reference

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `name` | `str` | Required | Form field name attribute |
| `*options` | `tuple` | Required | Options as `(value, label)` or `(value, label, selected)` |
| `label` | `str \| None` | `None` | Label text above select |
| `help_text` | `str \| None` | `None` | Helper text below select |
| `size` | `"sm" \| "lg" \| None` | `None` | Select size (default is medium) |
| `disabled` | `bool \| None` | `None` | Whether select is disabled |
| `required` | `bool \| None` | `None` | Whether select is required |
| `multiple` | `bool \| None` | `None` | Allow multiple selections |
| `cls` | `str` | `""` | Additional CSS classes |
| `**kwargs` | `Any` | - | Additional HTML attributes (id, hx-*, data-*, aria-*) |

## Accessibility

- Labels are linked to selects via `for` and `id` attributes.
- Required fields are marked with `required` attribute and a red asterisk in the label.
- Help text is linked via `aria-describedby`.

## API Reference

::: faststrap.components.forms.select.Select
    options:
        show_source: true
        heading_level: 4
