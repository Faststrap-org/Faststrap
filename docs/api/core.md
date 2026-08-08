# API Reference

This section provides automatically generated documentation from the FastStrap source code. It is useful for looking up exact parameter names and types.

## Core Utilities

### `merge_classes`

`merge_classes(base, user)` combines a base class string with user-provided classes, deduplicating while preserving order.

```python
from faststrap import merge_classes

merged = merge_classes("btn btn-primary", "btn-lg custom")
# Result: "btn btn-primary btn-lg custom"
```

This is the standard way FastStrap components merge default Bootstrap classes with user overrides. Use it when authoring custom components.

### `convert_attrs`

`convert_attrs()` converts Python-friendly kwargs such as `hx_get`, `data_bs_toggle`, `aria_label`, `style={...}`, and `css_vars={...}` into valid HTML attributes.

```python
from faststrap import convert_attrs

attrs = {"cls": "btn btn-primary"}
attrs.update(
    convert_attrs(
        {
            "hx_post": "/save",
            "hx_target": "#result",
            "data": {"mode": "inline"},
            "css_vars": {"brand_color": "#5B6CFF"},
        }
    )
)
```

For component authors, routing `**kwargs` through `convert_attrs(kwargs)` is the standard way to preserve HTMX support and attribute conversion consistently.

### `UNSET` Sentinel

`UNSET` is a sentinel value used to distinguish "not provided" from `None`. Component defaults are stored as `UNSET` and resolved at render time, allowing you to pass `None` explicitly to clear a default.

```python
from faststrap import UNSET, set_component_defaults, get_component_defaults

set_component_defaults("Button", {"variant": "primary"})
defaults = get_component_defaults("Button")
# Clear a default by passing None: Button("Click", variant=None)
```

See [Component Defaults](../api/defaults.md) for the full API reference on `UNSET`.

::: faststrap.core.base.merge_classes
    options:
        show_root_heading: true
        show_source: true

::: faststrap.utils.attrs.convert_attrs
    options:
        show_root_heading: true
        show_source: true

## Attributes Helper

::: faststrap.utils.attrs.convert_attrs
    options:
        show_root_heading: true
        show_source: true

## Application Setup

::: faststrap.core.assets.add_bootstrap
    options:
        show_root_heading: true
        show_source: true

::: faststrap.core.assets.get_assets
    options:
        show_root_heading: true
        show_source: true

::: faststrap.core.assets.mount_assets
    options:
        show_root_heading: true
        show_source: true

::: faststrap.utils.static_management.get_faststrap_static_url
    options:
        show_root_heading: true
        show_source: true

::: faststrap.utils.static_management.cleanup_static_resources
    options:
        show_root_heading: true
        show_source: true

## Theme System

Notes:
- `add_bootstrap()` supports `font_family` and `font_weights` for Google Fonts injection.
- `set_component_defaults()` modifies process-global defaults. Configure it at application startup before rendering components.
- Component calls can pass `None` to clear a configured default for that instance.
- `convert_attrs()` is available from `faststrap` directly for custom components and wrappers.
- `BaseComponent` / `Component` are extension points for third-party class-based components; built-ins remain function-based.
- `BaseComponent.merge_attrs()` applies `convert_attrs()` so class-based components keep the same attribute conversion behavior as function-based components.

### When To Use `BaseComponent`

Use `BaseComponent` only when a class-based API is genuinely helpful, for example:

- stateful third-party component libraries
- reusable abstractions with internal helper methods
- advanced wrappers that benefit from inheritance

For normal FastStrap components, prefer plain function-based components such as
`Button(...)`, `Card(...)`, or `Row(...)`. That remains the default style across
the framework.

::: faststrap.core.base.Component
    options:
        show_root_heading: true
        show_source: true

::: faststrap.core.base.BaseComponent
    options:
        show_root_heading: true
        show_source: true

::: faststrap.core.theme.create_theme
    options:
        show_root_heading: true
        show_source: true

::: faststrap.core.theme.get_builtin_theme
    options:
        show_root_heading: true
        show_source: true

::: faststrap.core.theme.list_builtin_themes
    options:
        show_root_heading: true
        show_source: true

::: faststrap.core.theme.set_component_defaults
    options:
        show_root_heading: true
        show_source: true

::: faststrap.core.theme.reset_component_defaults
    options:
        show_root_heading: true
        show_source: true

## Component Discovery

Faststrap exposes a small registry so users and agents can discover existing components before inventing new wrappers.

```python
from faststrap import (
    find_components,
    get_component,
    get_components_by_pattern,
    list_component_metadata,
    list_components,
)

list_components(category="display")
find_components("card")
get_components_by_pattern("toast")
metadata = list_component_metadata()
Button = get_component("Button")
```

::: faststrap.core.registry.list_components
    options:
        show_root_heading: true
        show_source: true

::: faststrap.core.registry.find_components
    options:
        show_root_heading: true
        show_source: true

::: faststrap.core.registry.get_components_by_pattern
    options:
        show_root_heading: true
        show_source: true

::: faststrap.core.registry.list_component_metadata
    options:
        show_root_heading: true
        show_source: true

::: faststrap.core.registry.get_component
    options:
        show_root_heading: true
        show_source: true

## Theme Variant CSS

Use `theme_variant_css()` when a polished component needs small light/dark CSS differences without repeating selector boilerplate.

```python
from fasthtml.common import Style
from faststrap import theme_variant_css

Style(
    theme_variant_css(
        ".premium-card",
        light={"background": "rgba(255, 255, 255, 0.78)"},
        dark={"background": "rgba(15, 23, 42, 0.62)"},
    )
)
```

::: faststrap.core.theme.theme_variant_css
    options:
        show_root_heading: true
        show_source: true

