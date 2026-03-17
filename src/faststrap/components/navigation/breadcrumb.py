"""Bootstrap Breadcrumb component for navigation trail."""

from __future__ import annotations

from typing import Any

from fasthtml.common import A, Li, Nav, Ol

from ...core.base import merge_classes
from ...core.registry import register
from ...utils.attrs import convert_attrs


@register(category="navigation")
def Breadcrumb(
    *items: tuple[Any, str | None] | tuple[Any, str | None, bool],
    **kwargs: Any,
) -> Nav:
    """Bootstrap Breadcrumb component for navigation trail.

    Args:
        *items: Breadcrumb items as (label, href) or (label, href, active)
        **kwargs: Additional HTML attributes
    """
    crumbs: list[Any] = []
    last_idx = len(items) - 1

    for idx, item in enumerate(items):
        if len(item) == 3:
            label, href, active = item
        elif len(item) == 2:
            label, href = item
            active = idx == last_idx
        else:
            raise ValueError(
                f"Breadcrumb item must be (label, href) or (label, href, active), got {item}"
            )

        item_cls = "breadcrumb-item" + (" active" if active else "")

        if active or href is None:
            crumbs.append(Li(label, cls=item_cls, aria_current="page"))
        else:
            crumbs.append(Li(A(label, href=href), cls=item_cls))

    # Build breadcrumb
    user_cls = kwargs.pop("cls", "")
    ol_cls = merge_classes("breadcrumb", user_cls)

    nav_attrs: dict[str, Any] = {"aria_label": "breadcrumb"}
    nav_attrs.update(convert_attrs(kwargs))

    return Nav(Ol(*crumbs, cls=ol_cls), **nav_attrs)
