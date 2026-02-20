# ToggleGroup

`ToggleGroup` makes a group of buttons behave like a single-select control.

It is ideal when you want radio-like visual selection behavior, but with custom button styling and no custom JavaScript setup in app code.

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

## Why this is useful

- Removes repeated "activate one, deactivate others" boilerplate.
- Keeps your sort/filter/tab selectors visually consistent.
- Works with existing `Button(...)` variants and custom classes.

## Common use cases

1. Sorting controls: Newest / Popular / Trending.
2. Pricing toggles: Monthly / Yearly.
3. View mode selectors: Grid / List / Compact.
4. Lightweight tab-like controls when you only need active visuals.

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

## HTMX integration example

```python
ToggleGroup(
    Button("Newest", variant="outline-primary", hx_get="/posts?sort=new", hx_target="#posts"),
    Button("Popular", variant="outline-primary", hx_get="/posts?sort=popular", hx_target="#posts"),
    Button("Top", variant="outline-primary", hx_get="/posts?sort=top", hx_target="#posts"),
    name="sort",
    values=["new", "popular", "top"],
)
```

`ToggleGroup` handles active visual state. Your route logic still decides behavior and response.

## API

- `*buttons`: Buttons or clickable elements.
- `name`: Optional field name for hidden input.
- `values`: Optional submitted values per button.
- `active_index`: Initially active button index.
- `active_cls`: Active class name (default: `"active"`).
- `hidden_input`: Whether to include hidden input when `name` is provided.

## Notes

- If `values` is provided, it must match the number of buttons.
- If `name` is set, selected value is synced to hidden input for form submission.
