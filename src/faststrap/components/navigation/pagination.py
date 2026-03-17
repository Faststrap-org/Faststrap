"""Bootstrap Pagination component for page navigation."""

from __future__ import annotations

from typing import Any

from fasthtml.common import A, Li, Nav, Span, Ul

from ...core.base import merge_classes
from ...core.registry import register
from ...core.theme import resolve_defaults
from ...core.types import AlignType, SizeType
from ...utils.attrs import convert_attrs


@register(category="navigation")
def Pagination(
    current_page: int,
    total_pages: int,
    size: SizeType | None = None,
    align: AlignType | None = None,
    max_pages: int | None = None,
    base_url: str | None = None,
    show_first_last: bool | None = None,
    show_prev_next: bool | None = None,
    **kwargs: Any,
) -> Nav:
    """Bootstrap Pagination component for page navigation.

    Args:
        current_page: Current active page (1-indexed)
        total_pages: Total number of pages
        size: Pagination size (sm, lg)
        align: Alignment (start, center, end)
        max_pages: Maximum page numbers to show
        base_url: Base URL for page links
        show_first_last: Show first/last page buttons
        show_prev_next: Show previous/next buttons
        **kwargs: Additional HTML attributes
    """
    # Resolve API defaults
    cfg = resolve_defaults(
        "Pagination",
        size=size,
        align=align,
        max_pages=max_pages,
        base_url=base_url,
        show_first_last=show_first_last,
        show_prev_next=show_prev_next,
    )

    c_size = cfg.get("size")
    c_align = cfg.get("align", "start")
    c_max_pages = cfg.get("max_pages", 5)
    c_base_url = cfg.get("base_url", "#")
    c_show_first_last = cfg.get("show_first_last", False)
    c_show_prev_next = cfg.get("show_prev_next", True)

    # Build pagination classes
    classes = ["pagination"]
    if c_size:
        classes.append(f"pagination-{c_size}")

    # Alignment
    justify_class = {
        "center": "justify-content-center",
        "end": "justify-content-end",
    }.get(c_align)

    user_cls = kwargs.pop("cls", "")
    ul_cls = merge_classes(" ".join(classes), user_cls)

    # Calculate page range
    half = c_max_pages // 2
    start = max(1, current_page - half)
    end = min(total_pages, start + c_max_pages - 1)

    # Adjust if at end
    if end == total_pages:
        start = max(1, end - c_max_pages + 1)

    # Build page links
    links: list[Any] = []

    # First page
    if c_show_first_last and current_page > 1:
        links.append(
            Li(
                A("«", href=f"{c_base_url}?page=1", cls="page-link", aria_label="First"),
                cls="page-item",
            )
        )

    # Previous page
    if c_show_prev_next:
        prev_disabled = current_page == 1
        prev_page = max(1, current_page - 1)
        links.append(
            Li(
                (
                    A(
                        "‹",
                        href=f"{c_base_url}?page={prev_page}",
                        cls="page-link",
                        aria_label="Previous",
                    )
                    if not prev_disabled
                    else Span("‹", cls="page-link", aria_hidden="true")
                ),
                cls="page-item" + (" disabled" if prev_disabled else ""),
            )
        )

    # Page numbers
    for page in range(start, end + 1):
        active = page == current_page
        href = f"{c_base_url}?page={page}"
        links.append(
            Li(
                (
                    A(str(page), href=href, cls="page-link")
                    if not active
                    else Span(str(page), cls="page-link")
                ),
                cls="page-item" + (" active" if active else ""),
                aria_current="page" if active else None,
            )
        )

    # Next page
    if c_show_prev_next:
        next_disabled = current_page == total_pages
        next_page = min(total_pages, current_page + 1)
        links.append(
            Li(
                (
                    A(
                        "›",
                        href=f"{c_base_url}?page={next_page}",
                        cls="page-link",
                        aria_label="Next",
                    )
                    if not next_disabled
                    else Span("›", cls="page-link", aria_hidden="true")
                ),
                cls="page-item" + (" disabled" if next_disabled else ""),
            )
        )

    # Last page
    if c_show_first_last and current_page < total_pages:
        links.append(
            Li(
                A("»", href=f"{c_base_url}?page={total_pages}", cls="page-link", aria_label="Last"),
                cls="page-item",
            )
        )

    # Build pagination
    ul = Ul(*links, cls=ul_cls)

    # Convert remaining kwargs
    nav_attrs: dict[str, Any] = {"aria_label": "Page navigation"}
    nav_attrs.update(convert_attrs(kwargs))

    return Nav(ul, cls=justify_class, **nav_attrs)
