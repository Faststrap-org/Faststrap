# ProfileDropdown

`@experimental`

Authenticated user menu for dashboards and portals.

---

## Quick Start

```python
from faststrap import ProfileDropdown

ProfileDropdown(
    "Alice Smith",
    subtitle="Administrator",
    items=[
        ("Profile", "/profile"),
        ("Settings", "/settings"),
        ("Sign out", "/logout"),
    ],
)
```

---

## Features

- Avatar with image or automatic initials fallback
- Optional subtitle/role display
- Dropdown menu with account actions
- Menu items render as real `<a>` links, so navigation works without extra JavaScript

---

## Parameters

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `name` | `str` | required | User display name. |
| `subtitle` | `str \| None` | `None` | Optional role, team, or email shown below the name. |
| `src` | `str \| None` | `None` | Optional avatar image URL. When omitted, initials are shown. |
| `items` | `list[tuple[str, str]] \| None` | `None` | Menu items as ``(label, href)`` tuples rendered as anchor links. |
| `alignment` | `str` | `"end"` | Bootstrap dropdown menu alignment. |
| `**kwargs` | `Any` | | Extra wrapper attributes. |

---

## Usage Examples

### Basic Profile Menu

```python
ProfileDropdown(
    "Alice Smith",
    items=[
        ("Profile", "/profile"),
        ("Settings", "/settings"),
        ("Sign out", "/logout"),
    ],
)
```

### With Avatar Image

```python
ProfileDropdown(
    "Bob Jones",
    src="/assets/avatars/bob.jpg",
    subtitle="Editor",
    items=[("Profile", "/profile"), ("Sign out", "/logout")],
)
```

### Without Menu Items

```python
ProfileDropdown("Alice Smith", subtitle="Admin")
```

---

## Notes

- Requires Bootstrap Dropdown JavaScript for toggle behavior; menu item links are plain anchors and navigate without extra JS.
- The trigger is keyboard-accessible (`tabindex="0"`, `role="button"`, `aria-expanded`/`aria-haspopup`).
- Marked `@experimental`.

---

## API Reference

::: faststrap.components.navigation.profile_dropdown.ProfileDropdown
    options:
        show_source: true
        heading_level: 4
