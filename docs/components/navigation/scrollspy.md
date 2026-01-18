# Scrollspy

Automatically update navigation based on scroll position.

## Basic Usage

```python
from faststrap import Scrollspy

# In your navigation
Nav(
    A("Section 1", href="#section1"),
    A("Section 2", href="#section2"),
    A("Section 3", href="#section3"),
    id="navbar"
)

# Scrollspy container
Scrollspy(
    Div(H2("Section 1", id="section1"), P("Content...")),
    Div(H2("Section 2", id="section2"), P("Content...")),
    Div(H2("Section 3", id="section3"), P("Content...")),
    target="#navbar"
)
```

## API Reference

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `*children` | Any | - | Scrollable content |
| `target` | str | Required | Selector for navigation element |
| `offset` | int | 10 | Offset from top (px) |
| `method` | str | "auto" | Scroll method: "auto" or "position" |
| `**kwargs` | Any | - | Additional HTML attributes |

## Examples

### Documentation Sidebar

```python
# Sidebar navigation
Div(
    Nav(
        A("Introduction", href="#intro", cls="nav-link"),
        A("Installation", href="#install", cls="nav-link"),
        A("Usage", href="#usage", cls="nav-link"),
        id="docNav",
        cls="flex-column"
    ),
    cls="col-md-3"
)

# Main content with scrollspy
Div(
    Scrollspy(
        Section(H2("Introduction", id="intro"), P("...")),
        Section(H2("Installation", id="install"), P("...")),
        Section(H2("Usage", id="usage"), P("...")),
        target="#docNav"
    ),
    cls="col-md-9"
)
```

### Table of Contents

```python
# TOC
Nav(
    A("Overview", href="#overview"),
    A("Features", href="#features"),
    A("Pricing", href="#pricing"),
    id="toc"
)

# Content
Scrollspy(
    Div(H2("Overview", id="overview"), P("...")),
    Div(H2("Features", id="features"), P("...")),
    Div(H2("Pricing", id="pricing"), P("...")),
    target="#toc",
    offset=100
)
```

## Accessibility

- Maintains keyboard navigation
- Updates ARIA attributes automatically
- Works with screen readers

## See Also

- [Navbar](navbar.md) - Navigation component
- [Tabs](tabs.md) - Tabbed navigation
