"""Bootstrap Modal component for dialog boxes."""

from __future__ import annotations

import hashlib
import json
from typing import Any, Literal

from fasthtml.common import H5, Div

from ...core.base import merge_classes
from ...core.registry import register
from ...core.theme import resolve_defaults
from ...core.types import SizeType
from ...utils.attrs import convert_attrs
from ..forms.button import CloseButton

_MODAL_ID_COUNTS: dict[str, int] = {}


def _unique_modal_id(base_id: str) -> str:
    count = _MODAL_ID_COUNTS.get(base_id, 0) + 1
    _MODAL_ID_COUNTS[base_id] = count
    if count == 1:
        return base_id
    return f"{base_id}-{count}"


def _stable_modal_id(
    children: tuple[Any, ...],
    *,
    title: str | None,
    size: SizeType | None,
    centered: bool,
    scrollable: bool,
    fullscreen: bool | str,
) -> str:
    digest = hashlib.sha1(
        json.dumps(
            {
                "title": title,
                "size": size,
                "centered": centered,
                "scrollable": scrollable,
                "fullscreen": fullscreen,
                "children_count": len(children),
            },
            sort_keys=True,
        ).encode("utf-8")
    ).hexdigest()[:10]
    return f"modal-{digest}-auto"


@register(category="feedback", requires_js=True)
def Modal(
    *children: Any,
    modal_id: str | None = None,
    title: str | None = None,
    footer: Any | None = None,
    size: SizeType | None = None,
    centered: bool | None = None,
    scrollable: bool | None = None,
    fullscreen: (
        bool | Literal["sm-down", "md-down", "lg-down", "xl-down", "xxl-down"] | None
    ) = None,
    static_backdrop: bool | None = None,
    fade: bool | None = None,
    dialog_cls: str | None = None,
    content_cls: str | None = None,
    header_cls: str | None = None,
    body_cls: str | None = None,
    footer_cls: str | None = None,
    title_cls: str | None = None,
    close_cls: str | None = None,
    **kwargs: Any,
) -> Div:
    """Bootstrap Modal component for dialog boxes and overlays.

    Args:
        *children: Modal body content
        modal_id: Unique ID for the modal (required for Bootstrap JS)
        title: Modal header title
        footer: Modal footer content
        size: Modal size (sm, lg, xl)
        centered: Vertically center modal
        scrollable: Make modal body scrollable
        fullscreen: Full-screen modal
        static_backdrop: Clicking backdrop doesn't close modal
        fade: Use fade animation
        **kwargs: Additional HTML attributes (cls, hx-*, data-*, etc.)
    """
    # Resolve API defaults
    cfg = resolve_defaults(
        "Modal",
        size=size,
        centered=centered,
        scrollable=scrollable,
        fullscreen=fullscreen,
        static_backdrop=static_backdrop,
        fade=fade,
        dialog_cls=dialog_cls,
        content_cls=content_cls,
        header_cls=header_cls,
        body_cls=body_cls,
        footer_cls=footer_cls,
        title_cls=title_cls,
        close_cls=close_cls,
    )

    c_size = cfg.get("size")
    c_centered = cfg.get("centered", False)
    c_scrollable = cfg.get("scrollable", False)
    c_fullscreen = cfg.get("fullscreen", False)
    c_static_backdrop = cfg.get("static_backdrop", False)
    c_fade = cfg.get("fade", True)
    c_dialog_cls = cfg.get("dialog_cls", "")
    c_content_cls = cfg.get("content_cls", "")
    c_header_cls = cfg.get("header_cls", "")
    c_body_cls = cfg.get("body_cls", "")
    c_footer_cls = cfg.get("footer_cls", "")
    c_title_cls = cfg.get("title_cls", "")
    c_close_cls = cfg.get("close_cls", "")

    # Ensure modal id
    if modal_id is None:
        base_id = _stable_modal_id(
            children,
            title=title,
            size=c_size,
            centered=c_centered,
            scrollable=c_scrollable,
            fullscreen=c_fullscreen,
        )
        modal_id = _unique_modal_id(base_id)

    # Build modal dialog classes
    dialog_classes = ["modal-dialog"]
    if c_size:
        dialog_classes.append(f"modal-{c_size}")
    if c_centered:
        dialog_classes.append("modal-dialog-centered")
    if c_scrollable:
        dialog_classes.append("modal-dialog-scrollable")
    if c_fullscreen:
        if c_fullscreen is True:
            dialog_classes.append("modal-fullscreen")
        else:
            dialog_classes.append(f"modal-fullscreen-{c_fullscreen}")

    # Build modal attributes
    modal_classes = ["modal"]
    if c_fade:
        modal_classes.append("fade")

    user_cls = kwargs.pop("cls", "")
    all_modal_classes = merge_classes(" ".join(modal_classes), user_cls)

    # Prevent accidental conflict with our explicit id
    kwargs.pop("id", None)

    attrs: dict[str, Any] = {
        "cls": all_modal_classes,
        "tabindex": "-1",
        "aria_labelledby": f"{modal_id}Label",
        "aria_hidden": "true",
    }

    # Static backdrop
    if c_static_backdrop:
        attrs["data_bs_backdrop"] = "static"
        attrs["data_bs_keyboard"] = "false"

    # Convert remaining kwargs
    attrs.update(convert_attrs(kwargs))

    # Build modal structure
    content_parts = []

    # Header
    if title:
        header = Div(
            H5(title, cls=merge_classes("modal-title", c_title_cls), id=f"{modal_id}Label"),
            CloseButton(cls=c_close_cls, data_bs_dismiss="modal"),
            cls=merge_classes("modal-header", c_header_cls),
        )
        content_parts.append(header)

    # Body
    body = Div(*children, cls=merge_classes("modal-body", c_body_cls))
    content_parts.append(body)

    # Footer
    if footer:
        footer_div = Div(footer, cls=merge_classes("modal-footer", c_footer_cls))
        content_parts.append(footer_div)

    # Assemble modal
    modal_content = Div(*content_parts, cls=merge_classes("modal-content", c_content_cls))
    modal_dialog = Div(modal_content, cls=merge_classes(" ".join(dialog_classes), c_dialog_cls))

    return Div(modal_dialog, id=modal_id, **attrs)
