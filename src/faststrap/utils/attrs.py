"""Attribute conversion utilities.

FastStrap components accept Python-friendly keyword arguments (e.g. `hx_get`,
`data_bs_toggle`, `aria_label`) and convert them to HTML attributes.

This module also provides lightweight support for:
- filtering out `None` values (so components can pass optional attrs safely)
- `style` passed as a dict (serialized to a CSS string)
- `css_vars` passed as a dict (merged into style as CSS variables)
- structured `data={...}` and `aria={...}` dictionaries
"""

from __future__ import annotations

import json
from typing import Any


def _to_kebab(s: str) -> str:
    return s.replace("_", "-")


def _css_key(s: str) -> str:
    """Convert pythonic CSS dict keys to CSS property names.

    - keep CSS variables `--x` as-is
    - convert underscores to hyphens
    """
    if s.startswith("--"):
        return s
    return _to_kebab(s)


def _style_to_string(style: dict[str, Any]) -> str:
    parts: list[str] = []
    for k, v in style.items():
        if v is None:
            continue
        parts.append(f"{_css_key(str(k))}: {_stringify_attr_value(v)}")
    return "; ".join(parts)


def _stringify_attr_value(value: Any) -> str:
    """Convert arbitrary values to stable attribute-safe strings."""
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (str, int, float)):
        return str(value)
    if isinstance(value, (list, tuple, set, dict)):
        return json.dumps(value, sort_keys=True, default=str)
    return str(value)


def _merge_style(existing: str | None, addition: str | None) -> str | None:
    if not addition:
        return existing
    if not existing:
        return addition
    # Ensure a single separator
    return f"{existing.rstrip('; ')}; {addition.lstrip('; ')}"


def convert_attrs(kwargs: dict[str, Any]) -> dict[str, Any]:
    """Convert Python kwargs to HTML attributes (hx_get -> hx-get).

    Rules:
    - `None` values are dropped
    - boolean `False` values are dropped (except `aria_*`, which are preserved)
    - boolean `True` values are kept (FastHTML will serialize appropriately)
    - `style` may be a `str` or a `dict` (dict is serialized)
    - `css_vars` may be a dict and will be merged into `style`
    - `data={...}` expands to `data-*`
    - `aria={...}` expands to `aria-*`

    Args:
        kwargs: Python-style keyword arguments

    Returns:
        HTML-style attributes with hyphens
    """
    converted: dict[str, Any] = {}

    # ---- Extract style/css_vars/data/aria ---------------------------------
    style_val = kwargs.get("style")
    css_vars_val = kwargs.get("css_vars")
    data_val = kwargs.get("data")
    aria_val = kwargs.get("aria")

    style_str: str | None = None

    if isinstance(style_val, dict):
        style_str = _style_to_string(style_val)
    elif isinstance(style_val, str):
        style_str = style_val.strip() or None
    elif style_val is None:
        style_str = None

    if isinstance(css_vars_val, dict):
        css_style: dict[str, Any] = {}
        for k, v in css_vars_val.items():
            if v is None:
                continue
            key = str(k)
            if not key.startswith("--"):
                key = f"--{_css_key(key)}"
            css_style[key] = v
        style_str = _merge_style(style_str, _style_to_string(css_style))

    # ---- Convert regular attributes ---------------------------------------
    for k, v in kwargs.items():
        if k in {"style", "css_vars", "data", "aria"}:
            continue

        # Keep cls as-is (FastHTML convention)
        if k == "cls":
            converted[k] = v
            continue

        # Normalize aria booleans as strings (preferred for HTML output)
        if k.startswith("aria_") and isinstance(v, bool):
            converted[_to_kebab(k)] = "true" if v else "false"
            continue

        # Drop None and False
        if v is None:
            continue
        if isinstance(v, bool) and v is False:
            continue

        converted[_to_kebab(k)] = v

    # ---- Expand structured data/aria dicts --------------------------------
    if isinstance(data_val, dict):
        for dk, dv in data_val.items():
            if dv is None:
                continue
            if isinstance(dv, bool):
                converted[f"data-{_to_kebab(str(dk))}"] = "true" if dv else "false"
            else:
                converted[f"data-{_to_kebab(str(dk))}"] = _stringify_attr_value(dv)

    if isinstance(aria_val, dict):
        for ak, av in aria_val.items():
            if av is None:
                continue
            if isinstance(av, bool):
                converted[f"aria-{_to_kebab(str(ak))}"] = "true" if av else "false"
            else:
                converted[f"aria-{_to_kebab(str(ak))}"] = _stringify_attr_value(av)

    # ---- Apply merged style if present ------------------------------------
    if style_str:
        converted["style"] = style_str

    return converted
