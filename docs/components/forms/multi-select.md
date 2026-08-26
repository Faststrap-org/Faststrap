# Multi Select

The `MultiSelect` component creates a dropdown that allows selecting multiple options.

## Quick Start

```python
MultiSelect(
    "skills",
    ("python", "Python"),
    ("javascript", "JavaScript"),
    ("html", "HTML/CSS"),
    ("sql", "SQL"),
    ("docker", "Docker"),
    label="Skills",
    help_text="Hold Ctrl/Cmd to select multiple",
)
```

## Usage Scenarios

### Pre-selected Values

```python
MultiSelect(
    "tags",
    ("python", "Python"),
    ("javascript", "JavaScript"),
    ("react", "React"),
    selected=["python", "react"],
    label="Tags",
)
```

### With Validation State

```python
MultiSelect(
    "categories",
    ("tech", "Technology"),
    ("design", "Design"),
    label="Categories",
    required=True,
    disabled=False,
)
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
| `selected` | `Iterable[str] \| None` | `None` | Pre-selected values |
| `cls` | `str` | `""` | Additional CSS classes |
| `**kwargs` | `Any` | - | Additional HTML attributes (id, hx-*, data-*, aria-*) |

## Accessibility

- Labels are linked to selects via `for` and `id` attributes.
- Required fields are marked with `required` attribute and a red asterisk in the label.
- Help text is linked via `aria-describedby`.
- The `multiple` attribute is automatically added for multi-selection.

## API Reference

::: faststrap.components.forms.multi_select.MultiSelect
    options:
        show_source: true
        heading_level: 4
