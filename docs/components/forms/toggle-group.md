# ToggleGroup

`ToggleGroup` makes a group of buttons behave like a single-select control.

## Import

```python
from faststrap import ToggleGroup, Button
```

## Basic usage

```python
ToggleGroup(
    Button("Newest", variant="outline-primary"),
    Button("Popular", variant="outline-primary"),
    Button("Top Rated", variant="outline-primary"),
)
```

Only one button stays active at a time.

## With submitted form value

```python
ToggleGroup(
    Button("Newest", variant="outline-secondary"),
    Button("Popular", variant="outline-secondary"),
    name="sort",
    values=["new", "popular"],
    active_index=0,
)
```

This adds a hidden input so the selected value submits with your form.

## API

- `*buttons`: Buttons or clickable elements.
- `name`: Optional field name for hidden input.
- `values`: Optional submitted values per button.
- `active_index`: Initially active button index.
- `active_cls`: Active class name (default: `"active"`).
- `hidden_input`: Whether to include hidden input when `name` is provided.

