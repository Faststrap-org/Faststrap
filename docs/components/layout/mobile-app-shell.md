# MobileAppShell

Responsive application shell that composes existing Faststrap navigation primitives for desktop and mobile layouts. It does not replace `Navbar`, `SidebarNavbar`, `Drawer`, or `BottomNav`; it gives those surfaces predictable responsive slots.

## Quick Start

```python
from faststrap import BottomNav, BottomNavItem, MobileAppShell, Navbar

MobileAppShell(
    "Dashboard content",
    desktop_nav=Navbar(brand="Console"),
    mobile_nav=Navbar(brand="Console", expand="none"),
    bottom_nav=BottomNav(
        BottomNavItem("Home", href="/", icon="house", active=True),
        BottomNavItem("Profile", href="/profile", icon="person"),
    ),
)
```

## Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `*children` | `Any` | `()` | Main page content. |
| `desktop_nav` | `Any \| None` | `None` | Content shown from `breakpoint` upward. |
| `mobile_nav` | `Any \| None` | `None` | Content shown below `breakpoint`. |
| `sidebar` | `Any \| None` | `None` | Desktop sidebar, laid out beside `<main>` from `breakpoint` upward. |
| `drawer` | `Any \| None` | `None` | Drawer/offcanvas slot, usually paired with a trigger. |
| `mobile_toolbar` | `Any \| None` | `None` | Mobile-only top toolbar. |
| `bottom_nav` | `Any \| None` | `None` | Mobile-only bottom navigation. |
| `safe_area` | `bool` | `True` | Adds bottom safe-area padding around main content. |
| `breakpoint` | `Literal["sm", "md", "lg", "xl", "xxl"]` | `"lg"` | Bootstrap breakpoint at which desktop navigation/sidebar replace mobile navigation. |
| `content_id` | `str \| None` | `"main-content"` | ID for the `<main>` landmark; use `None` to omit it when composing multiple shells. |
| `content_cls` | `str \| None` | `None` | Additional classes for the `<main>` content region. |
| `**kwargs` | `Any` | | Shell attributes, including `id`, `data_*`, and `hx_*`. |

The shell renders a `main-content` landmark by default. With a sidebar, the shell places the sidebar and main region in a shared desktop flex row; below the configured breakpoint the sidebar is hidden and the main content remains in the mobile flow. `BottomNav` already applies its own bottom safe-area inset, so the shell does not add a second inset to that slot. Pass navigation components through the slots rather than duplicating their markup in the page body.

::: faststrap.components.layout.mobile_app_shell.MobileAppShell
    options:
        show_source: true
