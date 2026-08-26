# Toggle Group

The `ToggleGroup` component renders a button group where only one item stays active at a time.

## Quick Start

```python
ToggleGroup(
    Button("List View", variant="outline-primary"),
    Button("Grid View", variant="outline-primary"),
    Button("Table View", variant="outline-primary"),
    name="view",
    values=["list", "grid", "table"],
)
```

## Usage Scenarios

### View Switcher

```python
ToggleGroup(
    Button("List", variant="outline-primary"),
    Button("Grid", variant="outline-primary"),
    Button("Map", variant="outline-primary"),
    name="view_mode",
    values=["list", "grid", "map"],
    active_index=0,
)
```

### Segmented Control

```python
ToggleGroup(
    Button("Day", variant="outline-secondary"),
    Button("Week", variant="outline-secondary"),
    Button("Month", variant="outline-secondary"),
    name="period",
    values=["day", "week", "month"],
    active_index=1,
)
```

### With Custom Active Class

```python
ToggleGroup(
    Button("On", variant="success"),
    Button("Off", variant="outline-danger"),
    name="power",
    values=["on", "off"],
    active_cls="active",
)
```

## Parameter Reference

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `*buttons` | `Any` | Required | Button elements to include in the group |
| `name` | `str \| None` | `None` | Name for the hidden input that stores the selected value |
| `values` | `list[str] \| None` | `None` | Values corresponding to each button |
| `active_index` | `int` | `0` | Index of the initially active button |
| `active_cls` | `str` | `"active"` | CSS class applied to the active button |
| `hidden_input` | `bool` | `True` | Whether to render a hidden input for form submission |
| `**kwargs` | `Any` | - | Additional HTML attributes |

## Accessibility

- Active button gets `aria-pressed="true"` and `aria-current="true"`.
- Inactive buttons get `aria-pressed="false"` and `aria-current="false"`.
- A hidden input is rendered for form submission when `name` is provided.

## API Reference

::: faststrap.components.forms.toggle_group.ToggleGroup
    options:
        show_source: true
        heading_level: 4
