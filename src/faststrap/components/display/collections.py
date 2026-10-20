"""Responsive list and collection-view primitives."""

from __future__ import annotations

from collections.abc import Callable, Iterable
from typing import Any, Literal
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

from fasthtml.common import A, Button, Div, Span

from ...core._stability import beta
from ...core.base import merge_classes
from ...core.registry import register
from ...utils.attrs import convert_attrs
from ...utils.icons import Icon

CollectionMode = Literal["list", "grid", "cards", "compact"]
ListDensity = Literal["compact", "comfortable", "spacious"]


def _merge_style(base: str, user_style: Any) -> str:
    if not user_style:
        return base
    if isinstance(user_style, dict):
        user_style = "; ".join(f"{key}: {value}" for key, value in user_style.items())
    return f"{base.rstrip('; ')}; {str(user_style).strip()}"


def _ensure_list_item(item: Any, wrapper_cls: str) -> Any:
    attrs = getattr(item, "attrs", None)
    if isinstance(attrs, dict) and attrs.get("role") == "listitem":
        return item
    return Div(item, cls=wrapper_cls, role="listitem")


@register(category="display")
@beta
def ListItem(
    *children: Any,
    title: Any | None = None,
    subtitle: Any | None = None,
    meta: Any | None = None,
    leading: Any | None = None,
    trailing: Any | None = None,
    href: str | None = None,
    selected: bool = False,
    active: bool = False,
    disabled: bool = False,
    loading: bool = False,
    density: ListDensity = "comfortable",
    lines: Literal[1, 2, 3] | None = None,
    **kwargs: Any,
) -> Div | A:
    """Render a flexible one-, two-, or three-line collection row.

    ``ListItem`` is designed for files, users, mobile settings, datasets, and
    other record summaries. Use the leading and trailing slots for avatars,
    icons, checkboxes, status badges, or actions.
    """
    if density not in {"compact", "comfortable", "spacious"}:
        raise ValueError("density must be 'compact', 'comfortable', or 'spacious'")
    if lines not in {None, 1, 2, 3}:
        raise ValueError("lines must be 1, 2, or 3")

    user_cls = kwargs.pop("cls", "")
    title_content = title if title is not None else (children[0] if children else None)
    extra_content = list(children[1:] if title is None and children else children)

    content_parts: list[Any] = []
    if title_content is not None:
        content_parts.append(Div(title_content, cls="faststrap-list-item-title"))
    if subtitle is not None:
        content_parts.append(Div(subtitle, cls="faststrap-list-item-subtitle"))
    if meta is not None:
        content_parts.append(Div(meta, cls="faststrap-list-item-meta"))
    content_parts.extend(extra_content)

    row_parts: list[Any] = []
    if leading is not None:
        row_parts.append(Div(leading, cls="faststrap-list-item-leading flex-shrink-0"))
    row_parts.append(Div(*content_parts, cls="faststrap-list-item-content flex-grow-1 min-w-0"))
    if trailing is not None:
        row_parts.append(Div(trailing, cls="faststrap-list-item-trailing flex-shrink-0"))
    if loading:
        row_parts.append(
            Span(
                Span(cls="spinner-border spinner-border-sm", aria_hidden="true"),
                Span("Loading", cls="visually-hidden"),
                cls="faststrap-list-item-loading-indicator",
                role="status",
            )
        )

    attrs: dict[str, Any] = {
        "cls": merge_classes(
            "faststrap-list-item d-flex align-items-center gap-3",
            f"faststrap-list-item-{density}",
            f"faststrap-list-item-lines-{lines}" if lines else "",
            "faststrap-list-item-selected" if selected else "",
            "faststrap-list-item-disabled" if disabled else "",
            "faststrap-list-item-action" if href else "",
            user_cls,
        )
    }
    attrs["role"] = "listitem"
    if selected:
        attrs["aria-current"] = "true"
    if disabled:
        attrs["aria-disabled"] = "true"
    if active:
        attrs["aria-current"] = "page" if href else "true"
        attrs["cls"] = merge_classes(attrs["cls"], "faststrap-list-item-active")
    if loading:
        attrs["aria-busy"] = "true"
        attrs["aria-disabled"] = "true"
        attrs["cls"] = merge_classes(attrs["cls"], "faststrap-list-item-loading")
    attrs.update(convert_attrs(kwargs))

    if href and not (disabled or loading):
        return A(*row_parts, href=href, **attrs)
    if href:
        if disabled or loading:
            attrs["tabindex"] = "-1"
    return Div(*row_parts, **attrs)


@register(category="display")
@beta
def ListView(
    *items: Any,
    density: ListDensity = "comfortable",
    divided: bool = True,
    flush: bool = False,
    label: str | None = None,
    empty: Any | None = None,
    loading: bool = False,
    loading_content: Any = "Loading...",
    **kwargs: Any,
) -> Div:
    """Render a vertical collection of ``ListItem`` surfaces."""
    if density not in {"compact", "comfortable", "spacious"}:
        raise ValueError("density must be 'compact', 'comfortable', or 'spacious'")

    user_cls = kwargs.pop("cls", "")
    content = [_ensure_list_item(item, "faststrap-list-view-item") for item in items]
    if loading:
        content = [
            Div(
                Div(loading_content, cls="faststrap-collection-loading", role="status"),
                cls="faststrap-collection-state-item",
                role="listitem",
            )
        ]
    elif not content and empty is not None:
        content = [
            Div(
                Div(empty, cls="faststrap-collection-empty", role="status"),
                cls="faststrap-collection-state-item",
                role="listitem",
            )
        ]

    attrs: dict[str, Any] = {
        "cls": merge_classes(
            "faststrap-list-view",
            f"faststrap-list-view-{density}",
            "faststrap-list-view-divided" if divided else "",
            "faststrap-list-view-flush" if flush else "",
            user_cls,
        ),
        "role": "list",
    }
    if label:
        attrs["aria-label"] = label
    attrs.update(convert_attrs(kwargs))
    return Div(*content, **attrs)


@register(category="display")
@beta
def GridList(
    *items: Any,
    min_width: str = "16rem",
    columns: int | None = None,
    gap: int | str = 3,
    label: str | None = None,
    empty: Any | None = None,
    loading: bool = False,
    loading_content: Any = "Loading...",
    **kwargs: Any,
) -> Div:
    """Render a responsive CSS grid for cards, files, products, or records."""
    if columns is not None and columns < 1:
        raise ValueError("columns must be at least 1")

    user_cls = kwargs.pop("cls", "")
    user_style = kwargs.pop("style", None)
    gap_value = f"{gap * 0.25}rem" if isinstance(gap, int) else str(gap)
    styles = [f"--fs-grid-min-width: {min_width}", f"--fs-grid-gap: {gap_value}"]
    if columns is not None:
        styles.append(f"--fs-grid-columns: {columns}")

    content = [_ensure_list_item(item, "faststrap-grid-list-item") for item in items]
    if loading:
        content = [
            Div(
                Div(loading_content, cls="faststrap-collection-loading", role="status"),
                cls="faststrap-grid-list-item faststrap-collection-state-item",
                role="listitem",
            )
        ]
    elif not content and empty is not None:
        content = [
            Div(
                Div(empty, cls="faststrap-collection-empty", role="status"),
                cls="faststrap-grid-list-item faststrap-collection-state-item",
                role="listitem",
            )
        ]

    attrs: dict[str, Any] = {
        "cls": merge_classes("faststrap-grid-list", user_cls),
        "role": "list",
        "style": _merge_style("; ".join(part for part in styles if part), user_style),
    }
    if label:
        attrs["aria-label"] = label
    attrs.update(convert_attrs(kwargs))
    return Div(*content, **attrs)


@register(category="display")
@beta
def CollectionView(
    *items: Any,
    mode: CollectionMode = "list",
    list_density: ListDensity = "comfortable",
    grid_min_width: str = "16rem",
    grid_columns: int | None = None,
    gap: int | str = 3,
    label: str | None = None,
    records: Iterable[Any] | None = None,
    list_renderer: Callable[[Any], Any] | None = None,
    card_renderer: Callable[[Any], Any] | None = None,
    empty: Any | None = None,
    loading: bool = False,
    loading_content: Any = "Loading...",
    **kwargs: Any,
) -> Div:
    """Render items as a vertical list, compact list, grid, or card grid.

    The application owns the selected mode. Pair this with ``ViewToggle`` and
    a query parameter or HTMX endpoint when users should choose the view.
    """
    if mode not in {"list", "grid", "cards", "compact"}:
        raise ValueError("mode must be 'list', 'grid', 'cards', or 'compact'")

    if records is not None and items:
        raise ValueError("Pass either items or records, not both")

    rendered_items = list(items)
    if records is not None and not loading:
        record_items = list(records)
        if record_items:
            renderer = list_renderer if mode in {"list", "compact"} else card_renderer
            renderer_name = "list_renderer" if mode in {"list", "compact"} else "card_renderer"
            if renderer is None:
                raise ValueError(f"{renderer_name} is required when records are provided")
            rendered_items = [renderer(record) for record in record_items]

    user_cls = kwargs.pop("cls", "")
    if mode in {"grid", "cards"}:
        return GridList(
            *rendered_items,
            min_width=grid_min_width,
            columns=grid_columns,
            gap=gap,
            label=label,
            empty=empty,
            loading=loading,
            loading_content=loading_content,
            cls=merge_classes(
                "faststrap-collection-view", f"faststrap-collection-view-{mode}", user_cls
            ),
            **kwargs,
        )

    density = "compact" if mode == "compact" else list_density
    return ListView(
        *rendered_items,
        density=density,
        label=label,
        empty=empty,
        loading=loading,
        loading_content=loading_content,
        cls=merge_classes(
            "faststrap-collection-view", f"faststrap-collection-view-{mode}", user_cls
        ),
        **kwargs,
    )


@register(category="display")
@beta
def ViewToggle(
    *,
    value: Literal["list", "grid", "cards"] = "list",
    endpoint: str | None = None,
    param: str = "view",
    options: tuple[Literal["list", "grid", "cards"], ...] = ("list", "grid"),
    labels: dict[str, str] | None = None,
    aria_label: str = "Choose view",
    hx_target: str | None = None,
    hx_swap: str = "outerHTML",
    push_url: bool = False,
    **kwargs: Any,
) -> Div:
    """Render an accessible list/grid view selector.

    When ``endpoint`` is supplied, options render as ordinary links with the
    selected value in a query parameter. ``hx_target`` optionally upgrades
    those links to HTMX requests. Without an endpoint, buttons expose data
    attributes for application-owned progressive enhancement.
    """
    allowed = {"list", "grid", "cards"}
    if value not in allowed or not options or any(option not in allowed for option in options):
        raise ValueError("value and options must use 'list', 'grid', or 'cards'")
    if value not in options:
        raise ValueError("value must be included in options")
    if not param.strip():
        raise ValueError("param must not be empty")

    icon_names = {"list": "list-ul", "grid": "grid-3x3-gap", "cards": "grid"}
    default_labels = {"list": "List", "grid": "Grid", "cards": "Cards"}
    label_map = {**default_labels, **(labels or {})}
    controls: list[Any] = []
    for option in options:
        active = option == value
        content = (
            Icon(icon_names[option], aria_hidden="true"),
            Span(label_map[option], cls="visually-hidden"),
        )
        control_cls = merge_classes(
            "btn btn-sm", "btn-primary" if active else "btn-outline-secondary"
        )
        if endpoint:
            parts = urlsplit(endpoint)
            query = [
                (key, item)
                for key, item in parse_qsl(parts.query, keep_blank_values=True)
                if key != param
            ]
            query.append((param, option))
            href = urlunsplit(
                (parts.scheme, parts.netloc, parts.path, urlencode(query), parts.fragment)
            )
            link_attrs: dict[str, Any] = {
                "href": href,
                "cls": control_cls,
                "aria_current": "true" if active else None,
                "aria_label": label_map[option],
            }
            if hx_target:
                link_attrs.update(
                    {
                        "hx_get": href,
                        "hx_target": hx_target,
                        "hx_swap": hx_swap,
                    }
                )
                if push_url:
                    link_attrs["hx_push_url"] = "true"
            controls.append(A(*content, **link_attrs))
        else:
            controls.append(
                Button(
                    *content,
                    type="button",
                    cls=control_cls,
                    aria_pressed="true" if active else "false",
                    aria_label=label_map[option],
                    **{"data-fs-view": option},
                )
            )

    user_cls = kwargs.pop("cls", "")
    attrs: dict[str, Any] = {
        "cls": merge_classes("faststrap-view-toggle btn-group", user_cls),
        "role": "group",
        "aria-label": aria_label,
    }
    attrs.update(convert_attrs(kwargs))
    return Div(*controls, **attrs)
