"""Anchored, action-oriented feedback surface."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import Button, Div, Span

from ...core._stability import beta
from ...core.base import merge_classes
from ...core.registry import register
from ...core.types import VariantType
from ...utils.attrs import convert_attrs
from ...utils.icons import Icon


@register(category="feedback")
@beta
def Snackbar(
    *children: Any,
    variant: VariantType = "dark",
    title: str | None = None,
    action: Any | None = None,
    icon: str | None = None,
    dismissible: bool = True,
    placement: Literal["inline", "top", "bottom"] = "inline",
    duration: int | Literal["infinite"] = "infinite",
    **kwargs: Any,
) -> Div:
    """Render short-lived, action-oriented feedback near page content.

    Unlike ``Toast`` and ``ModernToast``, a snackbar is an inline/anchored
    surface intended to stay close to the action that produced it.
    ``duration`` is exposed as metadata for an application runtime; the core
    remains usable without custom JavaScript.
    """
    if placement not in {"inline", "top", "bottom"}:
        raise ValueError("placement must be inline, top, or bottom")
    if duration != "infinite" and (not isinstance(duration, int) or duration < 0):
        raise ValueError("duration must be a non-negative integer or 'infinite'")

    user_cls = kwargs.pop("cls", "")
    content: list[Any] = []
    if icon:
        content.append(Icon(icon, aria_hidden="true", cls="flex-shrink-0"))
    text_parts: list[Any] = []
    if title:
        text_parts.append(Span(title, cls="fw-semibold d-block"))
    text_parts.extend(children)
    content.append(Div(*text_parts, cls="flex-grow-1 min-w-0"))
    if action is not None:
        content.append(Div(action, cls="flex-shrink-0"))
    if dismissible:
        content.append(
            Button(
                type="button",
                cls="btn-close btn-close-white flex-shrink-0",
                data_bs_dismiss="alert",
                aria_label="Dismiss notification",
            )
        )

    attrs: dict[str, Any] = {
        "cls": merge_classes(
            "faststrap-snackbar alert d-flex align-items-center gap-2 mb-0",
            f"alert-{variant}" if variant != "dark" else "alert-dark",
            f"faststrap-snackbar-{placement}",
            user_cls,
        ),
        "role": "alert" if variant in {"danger", "warning"} else "status",
        "aria_live": "assertive" if variant in {"danger", "warning"} else "polite",
        "aria_atomic": "true",
        "data_fs_snackbar": "true",
        "data_fs_duration": str(duration),
    }
    attrs.update(convert_attrs(kwargs))
    return Div(*content, **attrs)
