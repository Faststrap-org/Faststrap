"""Compact mobile application toolbar."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import H1, A, Div, P

from ...core._stability import beta
from ...core.base import merge_classes
from ...core.registry import register
from ...utils.attrs import convert_attrs
from ...utils.icons import Icon


@register(category="layout")
@beta
def MobileToolbar(
    title: Any,
    *,
    subtitle: Any | None = None,
    back_href: str | None = None,
    back_label: str = "Go back",
    leading: Any | None = None,
    actions: Any | list[Any] | tuple[Any, ...] | None = None,
    variant: Literal["light", "dark", "surface"] = "surface",
    sticky: bool = False,
    **kwargs: Any,
) -> Div:
    """Render a compact, mobile-friendly app bar with composable slots."""
    if variant not in {"light", "dark", "surface"}:
        raise ValueError("variant must be 'light', 'dark', or 'surface'")

    user_cls = kwargs.pop("cls", "")
    leading_content = leading
    if back_href is not None:
        leading_content = A(
            Icon("arrow-left", aria_hidden="true"),
            href=back_href,
            cls="btn btn-sm btn-link text-reset p-2",
            aria_label=back_label,
        )

    title_parts = [H1(title, cls="h6 mb-0")]
    if subtitle is not None:
        title_parts.append(P(subtitle, cls="small mb-0 opacity-75"))

    action_items = (
        list(actions)
        if isinstance(actions, (list, tuple))
        else ([actions] if actions is not None else [])
    )
    attrs: dict[str, Any] = {
        "cls": merge_classes(
            "faststrap-mobile-toolbar d-flex align-items-center gap-2 px-3 py-2",
            f"faststrap-mobile-toolbar-{variant}",
            "position-sticky top-0" if sticky else "",
            user_cls,
        ),
        "role": "banner",
    }
    attrs.update(convert_attrs(kwargs))
    return Div(
        leading_content if leading_content is not None else Div(cls="d-none"),
        Div(*title_parts, cls="flex-grow-1 min-w-0"),
        Div(*action_items, cls="d-flex align-items-center gap-1 flex-shrink-0"),
        **attrs,
    )
