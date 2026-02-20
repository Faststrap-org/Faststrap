"""Long-text clamping and expandable text component."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Button, Div, Span

from ...core.base import merge_classes
from ...utils.attrs import convert_attrs


def TextClamp(
    text: str,
    max_chars: int = 180,
    show_more: bool = True,
    expand_label: str = "Show more",
    collapse_label: str = "Show less",
    button_cls: str = "btn btn-link p-0 text-decoration-none",
    ellipsis: str = "...",
    **kwargs: Any,
) -> Div:
    """Render long text with optional expandable behavior."""
    safe_max = max(1, max_chars)
    if len(text) <= safe_max:
        attrs = {"cls": kwargs.pop("cls", "")}
        attrs.update(convert_attrs(kwargs))
        return Div(text, **attrs)

    preview_text = text[:safe_max].rstrip() + ellipsis
    user_cls = kwargs.pop("cls", "")
    attrs = {"cls": merge_classes("fs-text-clamp", user_cls)}
    attrs.update(convert_attrs(kwargs))

    preview = Span(preview_text, data_fs_preview="true")
    if not show_more:
        return Div(preview, data_fs_text_clamp="false", **attrs)

    full = Span(text, cls="d-none", data_fs_full="true")
    toggle_button = Button(
        expand_label,
        type="button",
        cls=button_cls,
        data_fs_text_toggle="true",
        data_fs_expand_label=expand_label,
        data_fs_collapse_label=collapse_label,
        aria_expanded="false",
    )
    return Div(preview, full, toggle_button, data_fs_text_clamp="true", **attrs)
