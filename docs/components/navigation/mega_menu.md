# MegaMenu

**Planned** · `@experimental`

Premium expanded navigation component with multi-column link groups, featured items, and optional promotional content. Suitable for SaaS, documentation sites, and e-commerce headers.

---

## Quick Start

```python
from faststrap.components.navigation import MegaMenu
from faststrap import Card

MegaMenu(
    brand="MyApp",
    items=[
        {
            "label": "Products",
            "columns": [
                {"title": "Core", "links": [("Dashboard", "/dash"), ("Analytics", "/analytics")]},
                {"title": "Integrations", "links": [("Slack", "/slack"), ("GitHub", "/github")]},
            ],
            "featured": Card("New: AI Insights", header="Announcement"),
        },
        {"label": "Pricing", "href": "/pricing"},
        {"label": "Docs", "href": "/docs"},
    ],
    cta_text="Get Started",
    cta_href="/signup",
)
```

---

## Features

- Multi-column dropdown with section headings
- Featured/promotional content slot
- Keyboard-navigable (arrow keys, Escape to close)
- Accessible with ARIA roles and focus management
- Glass or solid background variants

---

## Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `brand` | `str \| Any` | required | Brand logo/name |
| `items` | `list[dict]` | required | Navigation items (see structure below) |
| `cta_text` | `str \| None` | `None` | Call-to-action button text |
| `cta_href` | `str \| None` | `None` | CTA link |
| `cta_variant` | `str` | `"primary"` | CTA button variant |
| `glass` | `bool` | `False` | Glassmorphism background |
| `sticky` | `bool` | `True` | Sticky on scroll |
| `expand` | `str` | `"lg"` | Responsive collapse breakpoint |
| `**kwargs` | `Any` | | Extra wrapper attributes |

### Item Structure

```python
# Simple link
{"label": "Pricing", "href": "/pricing"}

# Mega dropdown
{
    "label": "Products",
    "columns": [
        {
            "title": "Section Title",
            "links": [("Link Text", "/path"), ...],
        },
    ],
    "featured": Any,  # Optional promotional content
}
```

---

## Notes

- Requires minimal JS for dropdown toggle and keyboard navigation.
- Marked `@experimental`.
