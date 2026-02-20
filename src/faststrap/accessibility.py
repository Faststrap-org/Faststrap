"""Accessibility helpers for Faststrap."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import Div, Span

from .core.base import merge_classes
from .utils.attrs import convert_attrs

AriaLiveType = Literal["off", "polite", "assertive"]


def SkipLink(
    target: str = "#main-content",
    text: str = "Skip to main content",
    **kwargs: Any,
) -> Any:
    """Create a skip link for keyboard users."""
    from fasthtml.common import A

    user_cls = kwargs.pop("cls", "")
    cls = merge_classes(
        "visually-hidden-focusable position-absolute top-0 start-0 m-3 p-2 bg-body border rounded",
        user_cls,
    )
    attrs = {"href": target, "cls": cls}
    attrs.update(convert_attrs(kwargs))
    return A(text, **attrs)


def VisuallyHidden(
    *children: Any,
    focusable: bool = False,
    **kwargs: Any,
) -> Span:
    """Hide content visually while keeping it available to screen readers."""
    user_cls = kwargs.pop("cls", "")
    base_cls = "visually-hidden-focusable" if focusable else "visually-hidden"
    attrs = {"cls": merge_classes(base_cls, user_cls)}
    attrs.update(convert_attrs(kwargs))
    return Span(*children, **attrs)


def LiveRegion(
    *children: Any,
    politeness: AriaLiveType = "polite",
    atomic: bool = True,
    relevant: str = "additions text",
    **kwargs: Any,
) -> Div:
    """Create an ARIA live region for dynamic status messages."""
    user_cls = kwargs.pop("cls", "")
    attrs = {
        "cls": merge_classes("visually-hidden", user_cls),
        "aria_live": politeness,
        "aria_atomic": "true" if atomic else "false",
        "aria_relevant": relevant,
        "role": "status" if politeness == "polite" else "alert",
    }
    attrs.update(convert_attrs(kwargs))
    return Div(*children, **attrs)


def FocusTrap(
    *children: Any,
    autofocus_selector: str | None = None,
    **kwargs: Any,
) -> Div:
    """Create a focus trap container for dialogs and overlays."""
    user_cls = kwargs.pop("cls", "")
    attrs = {
        "cls": merge_classes(user_cls),
        "data_fs_focus_trap": "true",
        "tabindex": "-1",
    }
    if autofocus_selector:
        attrs["data_fs_autofocus"] = autofocus_selector
    attrs.update(convert_attrs(kwargs))
    return Div(*children, **attrs)
