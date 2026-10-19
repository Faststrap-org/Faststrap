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
| `desktop_nav` | `Any \| None` | `None` | Content shown from the large breakpoint upward. |
| `mobile_nav` | `Any \| None` | `None` | Content shown below the large breakpoint. |
| `sidebar` | `Any \| None` | `None` | Desktop sidebar slot. |
| `drawer` | `Any \| None` | `None` | Drawer/offcanvas slot, usually paired with a trigger. |
| `mobile_toolbar` | `Any \| None` | `None` | Mobile-only top toolbar. |
| `bottom_nav` | `Any \| None` | `None` | Mobile-only bottom navigation. |
| `safe_area` | `bool` | `True` | Adds bottom safe-area padding around main content. |
| `content_cls` | `str \| None` | `None` | Additional classes for the `<main>` content region. |
| `**kwargs` | `Any` | | Shell attributes, including `id`, `data_*`, and `hx_*`. |

The shell renders a `main-content` landmark. Pass navigation components through the slots rather than duplicating their markup in the page body.

::: faststrap.components.layout.mobile_app_shell.MobileAppShell
    options:
        show_source: true
