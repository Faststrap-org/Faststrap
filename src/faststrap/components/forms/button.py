"""Bootstrap Button component with variants, sizes, and loading states."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import A, I, Span
from fasthtml.common import Button as FTButton

from ...core.base import merge_classes
from ...core.registry import register
from ...core.theme import resolve_defaults
from ...core.types import SizeType, VariantType
from ...utils.attrs import convert_attrs


@register(category="forms")
def CloseButton(
    *children: Any,
    white: bool = False,
    aria_label: str = "Close",
    **kwargs: Any,
) -> FTButton:
    """Bootstrap close button helper.

    This is used by components like Alerts, Modals, and Drawers.

    Args:
        *children: Optional children. Bootstrap typically uses an empty button.
        white: Use white close icon variant (useful on dark backgrounds)
        aria_label: Accessible label
        **kwargs: Additional HTML attributes (cls, data-*, hx-*, etc.)

    Returns:
        FastHTML Button element
    """
    user_cls = kwargs.pop("cls", "")
    classes = ["btn-close"]
    if white:
        classes.append("btn-close-white")

    cls = merge_classes(" ".join(classes), user_cls)
    attrs: dict[str, Any] = {"type": "button", "cls": cls, "aria_label": aria_label}
    attrs.update(convert_attrs(kwargs))
    return FTButton(*children, **attrs)


@register(category="forms")
def Button(
    *children: Any,
    as_: Literal["button", "a"] = "button",
    variant: VariantType | None = None,
    size: SizeType | None = None,
    outline: bool = False,
    disabled: bool = False,
    loading: bool = False,
    spinner: bool = True,
    loading_text: str | None = None,
    icon: str | None = None,
    icon_pos: Literal["start", "end"] = "start",
    icon_cls: str | None = None,
    spinner_pos: Literal["start", "end"] = "start",
    spinner_cls: str | None = None,
    full_width: bool = False,
    active: bool = False,
    pill: bool = False,
    css_vars: dict[str, Any] | None = None,
    style: dict[str, Any] | str | None = None,
    **kwargs: Any,
) -> FTButton | A:
    """Bootstrap Button component.

    Args:
        *children: Button content (text, elements)
        as_: Render as 'button' or 'a' tag (default: 'button')
        variant: Bootstrap color variant
        size: Button size (sm, lg)
        outline: Use outline style
        disabled: Disable button
        loading: Show loading spinner and disable
        spinner: Show spinner when loading
        loading_text: Text to show when loading
        icon: Bootstrap icon name
        icon_pos: Icon position ('start' or 'end')
        icon_cls: Custom classes for icon
        spinner_pos: Spinner position ('start' or 'end')
        spinner_cls: Custom classes for spinner
        full_width: Make button 100% width. Note: Can also be achieved via `cls='w-100'`.
        active: Set active state. Note: Can also be achieved via `cls='active'`.
        pill: Use rounded-pill style. Note: Can also be achieved via `cls='rounded-pill'`.
        css_vars: Custom CSS variables dictionary
        style: Custom inline style
        **kwargs: Additional HTML attributes (cls, id, hx-*, data-*, etc.)
    """

    # Auto-promote to anchor if href is provided
    if as_ == "button" and "href" in kwargs:
        as_ = "a"

    # Resolve API defaults
    # This automatically picks up global defaults for 'variant', 'size', etc. if the user didn't pass them
    cfg = resolve_defaults(
        "Button",
        variant=variant,
        size=size,
        outline=outline,
        disabled=disabled,
        full_width=full_width,
        pill=pill,
        active=active,
    )

    # Extract resolved values
    c_variant = cfg.get("variant", "primary")  # Hardest fallback
    c_size = cfg.get("size")
    c_outline = cfg.get("outline", False)
    c_full_width = cfg.get("full_width", False)
    c_pill = cfg.get("pill", False)
    c_active = cfg.get("active", False)
    c_disabled = cfg.get("disabled", False)

    # Build base classes
    if c_outline and c_variant != "link":  # "link" doesn't have outline variant
        classes = [f"btn-outline-{c_variant}"]
    else:
        classes = [f"btn-{c_variant}"]

    # Add size class if specified
    if c_size:
        classes.append(f"btn-{c_size}")

    if c_full_width:
        classes.append("w-100")

    if c_pill:
        classes.append("rounded-pill")

    if c_active:
        classes.append("active")

    # Merge with user classes
    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes("btn", " ".join(classes), user_cls)

    # Build attributes with proper conversion
    attrs: dict[str, Any] = {"cls": all_classes}

    # Optional style + css vars (handled by convert_attrs)
    if style is not None:
        kwargs["style"] = style
    if css_vars is not None:
        kwargs["css_vars"] = css_vars

    # Handle states
    if c_active:
        attrs["aria_pressed"] = "true"

    if loading:
        attrs["aria_busy"] = "true"

    # Disabled/loading behavior differs for <button> vs <a>
    if loading or c_disabled:
        if as_ == "button":
            attrs["disabled"] = True
        else:
            # Bootstrap recommends `.disabled` + aria-disabled for anchors
            attrs["aria_disabled"] = "true"
            attrs["tabindex"] = "-1"
            attrs["cls"] = merge_classes(attrs.get("cls", ""), "disabled")

    # Convert remaining kwargs (including hx_*, data_*, etc.)
    attrs.update(convert_attrs(kwargs))

    # Build content
    content = list(children)

    # Loading: optionally override/augment text
    if loading and loading_text is not None:
        content = [loading_text]

    # Spinner
    if loading and spinner:
        if spinner_pos == "start":
            default_spinner_cls = "spinner-border spinner-border-sm me-2"
        else:
            default_spinner_cls = "spinner-border spinner-border-sm ms-2"

        spinner_elem = Span(
            cls=spinner_cls or default_spinner_cls,
            role="status",
            aria_hidden="true",
        )
        if spinner_pos == "start":
            content.insert(0, spinner_elem)
        else:
            content.append(spinner_elem)

    # Icon
    if (not loading) and icon:
        if icon_pos == "start":
            default_icon_cls = f"bi bi-{icon} me-2"
        else:
            default_icon_cls = f"bi bi-{icon} ms-2"
        icon_elem = I(cls=icon_cls or default_icon_cls, aria_hidden="true")
        if icon_pos == "start":
            content.insert(0, icon_elem)
        else:
            content.append(icon_elem)

    # Render element
    if as_ == "a":
        # Ensure href exists
        if "href" not in attrs:
            attrs["href"] = "#"
        # Keep a11y semantics when used as a button
        attrs.setdefault("role", "button")
        return A(*content, **attrs)

    return FTButton(*content, **attrs)
