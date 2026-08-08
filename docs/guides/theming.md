# Theming Guide

Faststrap supports light mode, dark mode, and custom themes. This guide covers all theming options.

---

## Built-in Themes

Faststrap includes two built-in Bootstrap themes:

| Mode | CSS Variable | Description |
| --- | --- | --- |
| `light` | `data-bs-theme="light"` | Bootstrap's default light theme |
| `dark` | `data-bs-theme="dark"` | Bootstrap's dark theme |

---

## Setting Up Dark Mode

```python
from faststrap import add_bootstrap

app, rt = fast_app()

@app.before
def add_bootstrap(req, resp):
    return add_bootstrap(req, resp, mode="dark")
```

### Persistent Dark Mode with Cookies

```python
from faststrap import add_bootstrap

@app.before
def add_bootstrap(req, resp):
    theme = req.cookies.get("theme", "light")
    return add_bootstrap(req, resp, mode=theme)

@rt("/toggle-theme")
def get(req, resp):
    current = req.cookies.get("theme", "light")
    new_theme = "dark" if current == "light" else "light"
    resp.set_cookie("theme", new_theme)
    return RedirectResponse("/")
```

---

## Custom Themes

### Creating a Custom Theme

```python
from faststrap import Theme, create_theme, add_bootstrap

my_theme = create_theme(
    name="brand",
    primary="#5B6CFF",
    secondary="#6C757D",
    success="#198754",
    danger="#DC3545",
    warning="#FFC107",
    info="#0DCAF2",
    light="#F8F9FA",
    dark="#212529",
    font_family="Inter, sans-serif",
)

add_bootstrap(app, theme=my_theme)
```

### Applying Theme Variants

```python
from faststrap import theme_variant_css
from fasthtml.common import Style

Style(
    theme_variant_css(
        ".premium-card",
        light={
            "background": "rgba(255, 255, 255, 0.78)",
            "border": "1px solid rgba(0, 0, 0, 0.05)",
        },
        dark={
            "background": "rgba(15, 23, 42, 0.62)",
            "border": "1px solid rgba(255, 255, 255, 0.05)",
        },
    )
)
```

---

## Global Component Defaults

Use `set_component_defaults` to configure default styling for all instances of a component:

```python
from faststrap import set_component_defaults

# All Buttons default to primary variant with rounded corners
set_component_defaults("Button", {
    "variant": "primary",
    "rounded": True,
})

# All Cards have a shadow
set_component_defaults("Card", {
    "shadow": "sm",
})
```

### Clearing a Default

Pass `None` to clear a configured default for a single instance:

```python
# Uses global default: variant="primary"
Button("Submit")

# Override global default: variant="danger"
Button("Delete", variant="danger")

# Clear global default entirely
Button("Plain", variant=None)
```

---

## CSS Variables

Faststrap exposes CSS variables for advanced customization:

```css
:root {
  --bs-primary: #5B6CFF;
  --bs-body-bg: #F8F9FA;
  --bs-body-color: #212529;
}

[data-bs-theme="dark"] {
  --bs-body-bg: #0F172A;
  --bs-body-color: #F1F5F9;
}
```

You can inject custom CSS via `add_bootstrap`:

```python
add_bootstrap(app, custom_css="""
  :root {
    --bs-primary: #5B6CFF;
  }
""")
```

---

## Bootstrap Icons

Bootstrap Icons are included by default. Use them with the `Icon` utility:

```python
from faststrap import Icon

Icon("heart")
Icon("star-fill", cls="text-warning")
Icon("gear", size="lg")
```

---

## Google Fonts

```python
from faststrap import add_bootstrap

add_bootstrap(
    app,
    font_family="Inter:wght@400;500;600;700",
    font_weights=["400", "500", "600", "700"],
)
```

---

## See Also

- [First App Tutorial](../getting-started/first-app.md)
- [Custom Components Guide](../guides/custom-components.md)
