# Theme Toggle

The `ThemeToggle` component creates a dark/light mode switch with HTMX server-side persistence.

## Quick Start

```python
ThemeToggle(current_theme="light", show_label=True)
```

## Usage Scenarios

### With Optional Icon

```python
ThemeToggle(current_theme="dark", show_icon=True)
```

### With Label

```python
ThemeToggle(current_theme="dark", show_label=True, label_text="Dark Mode")
```

### In Navbar

```python
Navbar(
    brand="MyApp",
    items=[
        NavItem("Home", href="/"),
        ThemeToggle(current_theme=req.session.get("theme", "light"), cls="ms-auto")
    ]
)
```

### Server-Side Theme Management

```python
@app.post("/theme/toggle")
def toggle_theme(req):
    current = req.session.get("theme", "light")
    new_theme = "dark" if current == "light" else "light"
    req.session["theme"] = new_theme
    from faststrap.presets import hx_refresh
    return hx_refresh()
```

## Parameter Reference

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `current_theme` | `str` | "auto" | Current theme ("light", "dark", "auto") |
| `endpoint` | `str` | "/theme/toggle" | Server endpoint for theme changes |
| `toggle_id` | `str` | "theme-toggle" | Unique ID for the toggle |
| `show_label` | `bool` | `False` | Whether to show label text |
| `label_text` | `str` | "Dark Mode" | Label text to display |
| `show_icon` | `bool` | `False` | Whether to show the decorative sun/moon icon |
| `**kwargs` | `Any` | - | Additional HTML attributes |

## Accessibility

- Uses `role="switch"` on the input for proper screen reader semantics.
- Label is associated via `for` and `id` attributes.
- Decorative icons use `aria-hidden="true"`.

## API Reference

::: faststrap.components.forms.theme_toggle.ThemeToggle
    options:
        show_source: true
        heading_level: 4
