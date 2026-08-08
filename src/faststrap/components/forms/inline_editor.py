"""Inline editor component for server-driven edit flows."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import Div, Span
from fasthtml.common import Form as FTForm
from fasthtml.common import Input as FTInput

from ...core._stability import stable
from ...core.base import merge_classes
from ...core.registry import register
from ...utils.attrs import convert_attrs
from .button import Button

InlineEditorMethod = Literal["get", "post", "put", "patch"]


@register(category="forms")
@stable
def InlineEditor(
    name: str,
    value: str = "",
    *,
    display: Any | None = None,
    editing: bool = False,
    endpoint: str | None = None,
    edit_endpoint: str | None = None,
    method: InlineEditorMethod = "post",
    input_type: str = "text",
    save_label: str = "Save",
    cancel_label: str = "Cancel",
    edit_label: str = "Edit",
    hx_target: str | None = None,
    hx_swap: str = "outerHTML",
    input_cls: str | None = None,
    actions_cls: str | None = None,
    **kwargs: Any,
) -> Div:
    """Render a compact inline display/edit surface.

    Apps can render `editing=False` for the read view and return
    `editing=True` from an HTMX endpoint for the edit view.
    """
    if method not in {"get", "post", "put", "patch"}:
        msg = f"method must be one of get, post, put, patch; got {method!r}"
        raise ValueError(msg)

    user_cls = kwargs.pop("cls", "")
    attrs: dict[str, Any] = {
        "cls": merge_classes(
            "faststrap-inline-editor d-inline-flex align-items-center gap-2", user_cls
        ),
        "data_fs_inline_editor": "true",
    }
    attrs.update(convert_attrs(kwargs))

    target = hx_target
    if target is None and attrs.get("id"):
        target = f"#{attrs['id']}"

    if not editing:
        edit_attrs: dict[str, Any] = {}
        if edit_endpoint:
            edit_attrs["hx_get"] = edit_endpoint
            if target:
                edit_attrs["hx_target"] = target
            edit_attrs["hx_swap"] = hx_swap

        return Div(
            Span(display if display is not None else value, cls="faststrap-inline-editor-value"),
            Button(edit_label, variant="link", size="sm", cls="p-0", **edit_attrs),
            **attrs,
        )

    form_attrs: dict[str, Any] = {
        "method": method,
        "cls": "d-inline-flex align-items-center gap-2",
    }
    if endpoint:
        form_attrs["action"] = endpoint
        form_attrs[f"hx_{method}"] = endpoint
        if target:
            form_attrs["hx_target"] = target
        form_attrs["hx_swap"] = hx_swap

    input_attrs = {
        "type": input_type,
        "name": name,
        "value": value,
        "cls": merge_classes("form-control form-control-sm", input_cls),
        "aria_label": f"Edit {name}",
    }

    actions = Div(
        Button(save_label, type="submit", variant="primary", size="sm"),
        Button(cancel_label, type="button", variant="secondary", outline=True, size="sm"),
        cls=merge_classes("d-inline-flex gap-2", actions_cls),
    )

    return Div(FTForm(FTInput(**input_attrs), actions, **convert_attrs(form_attrs)), **attrs)
