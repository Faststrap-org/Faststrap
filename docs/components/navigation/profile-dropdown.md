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
| `items` | `list[tuple[str, str]] \| list[tuple[str, str, dict]] \| None` | `None` | Menu entries as `(label, href)` tuples rendered as anchor links; an optional third dict element merges extra attributes onto the anchor. |
| `alignment` | `str` | `"end"` | Bootstrap dropdown menu alignment. |
| `avatar_size` | `int` | `32` | Avatar edge length in pixels (initials font scales automatically). |
| `layout` | `"horizontal" \| "stacked"` | `"stacked"` | `"horizontal"` places the subtitle beside the name on one line; `"stacked"` reproduces the original block layout. |
| `trigger_cls` / `menu_cls` / `item_cls` | `str` | `""` | Slot classes for the toggle, menu, and each item anchor. |
| `footer` | `Any \| None` | `None` | Element rendered after the items inside the menu (divider + padded section). |
| `**kwargs` | `Any` | | Extra wrapper attributes. |

```python
ProfileDropdown(
    "Alice Smith",
    subtitle="Administrator",
    src="/assets/avatars/alice.jpg",
    layout="horizontal",           # one-line trigger on desktop
    avatar_size=36,
    items=[
        ("Profile", "/profile"),
        ("Settings", "/settings"),
        ("Sign out", "/logout", {"data_testid": "logout"}),
    ],
    footer=Button("Switch workspace", variant="outline-secondary", size="sm"),
)
```

Global defaults work too: `set_component_defaults("ProfileDropdown", avatar_size=36, layout="horizontal")`.

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
- The trigger is a native `<button>` (`type="button"`, `data-bs-toggle="dropdown"`) so the menu opens with a mouse click, `Enter`, or `Space`, and is announced to screen readers with an `aria-label` matching the user's full name.
- Marked `@experimental`.

---

## API Reference

::: faststrap.components.navigation.profile_dropdown.ProfileDropdown
    options:
        show_source: true
        heading_level: 4
