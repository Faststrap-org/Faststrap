# BottomNav

`BottomNav` provides a mobile-style fixed bottom navigation bar with touch-friendly items.
When no explicit `padding-bottom` is supplied, it emits a zero-padding fallback followed by `env(safe-area-inset-bottom, 0px)` for devices with a home indicator. If you supply your own `padding-bottom`, that value takes precedence and you are responsible for any additional safe-area spacing required by your design.

## Quick Start

```python
from faststrap import BottomNav, BottomNavItem

BottomNav(
    BottomNavItem("Home", href="/", icon="house", active=True),
    BottomNavItem("Search", href="/search", icon="search"),
    BottomNavItem("Profile", href="/profile", icon="person"),
)
```

## Common Usage

```python
BottomNav(
    BottomNavItem("Feed", href="/feed", icon="newspaper"),
    BottomNavItem("Saved", href="/saved", icon="bookmark"),
    BottomNavItem("Settings", href="/settings", icon="gear"),
    variant="light",
    fixed=True,
)
```

## Parameters

### `BottomNav`

| Parameter | Type | Default | Description |
|---|---|---|---|
| `*children` | `Any` | Required | `BottomNavItem` children |
| `variant` | `str \| None` | `None` | Color scheme (`light`, `dark`, or custom) |
| `fixed` | `bool \| None` | `True` | Fixed to viewport bottom |
| `labels` | `bool` | `True` | Reserved for label visibility behavior |
| `**kwargs` | `Any` | - | Additional HTML attributes |

### `BottomNavItem`

| Parameter | Type | Default | Description |
|---|---|---|---|
| `label` | `str` | Required | Item text |
| `href` | `str` | `"#"` | Link destination |
| `icon` | `str \| None` | `None` | Bootstrap icon name |
| `active` | `bool` | `False` | Active route styling |
| `cls` | `str \| None` | `None` | Extra classes |
| `**kwargs` | `Any` | - | Additional attributes |

::: faststrap.components.navigation.bottom_nav.BottomNav
    options:
        show_source: true
        heading_level: 4

::: faststrap.components.navigation.bottom_nav.BottomNavItem
    options:
        show_source: true
        heading_level: 4
