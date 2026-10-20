"""DataTable component for sortable, searchable, paginated data views."""

from __future__ import annotations

import hashlib
import json
import math
from collections.abc import Callable, Iterator, Mapping
from typing import Any, Literal, cast
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

from fasthtml.common import A, Div, Form, Input, Li, Nav, Span, Ul

from ...core._ids import uniquify_id
from ...core._stability import beta
from ...core.base import merge_classes
from ...core.registry import register
from ...core.theme import resolve_defaults
from ...utils.attrs import convert_attrs
from .collections import GridList, ListItem
from .table import Table, TBody, TCell, THead, TRow, _normalize_table_data

SortableDirection = Literal["asc", "desc"]
ResponsiveType = Literal["sm", "md", "lg", "xl", "xxl"]
MobileMode = Literal["scroll", "cards", "stack"] | None


def _stable_table_id(
    *,
    columns: list[str],
    row_count: int,
    include_index: bool,
    sortable: bool,
    searchable: bool,
    pagination: bool,
) -> str:
    digest = hashlib.sha1(
        json.dumps(
            {
                "columns": columns,
                "row_count": row_count,
                "include_index": include_index,
                "sortable": sortable,
                "searchable": searchable,
                "pagination": pagination,
            },
            sort_keys=True,
        ).encode("utf-8")
    ).hexdigest()[:16]
    return f"datatable-{digest}-auto"


def _normalize_query_value(value: Any) -> str | list[str] | None:
    if value is None:
        return None
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (list, tuple, set)):
        return [str(item) for item in value]
    return str(value)


def _build_url(base_url: str, params: dict[str, Any]) -> str:
    parts = urlsplit(base_url)
    existing = dict(parse_qsl(parts.query, keep_blank_values=True))
    merged: dict[str, Any] = {**existing}
    for key, value in params.items():
        normalized = _normalize_query_value(value)
        if normalized is None:
            continue
        merged[str(key)] = normalized
    query = urlencode(merged, doseq=True)
    return urlunsplit((parts.scheme, parts.netloc, parts.path, query, parts.fragment))


def _pagination_window(
    current: int,
    total: int,
    *,
    wing: int = 2,
) -> list[int | None]:
    """Return visible page numbers, using None as an ellipsis marker."""
    if total <= 0:
        return []
    if total <= (wing * 2) + 5:
        return list(range(1, total + 1))

    visible = {1, total}
    visible.update(range(max(1, current - wing), min(total, current + wing) + 1))

    window: list[int | None] = []
    previous: int | None = None
    for page_num in sorted(visible):
        if previous is not None and page_num - previous > 1:
            window.append(None)
        window.append(page_num)
        previous = page_num
    return window


def _matches_search(
    row: dict[str, Any],
    *,
    columns: list[str],
    query: str,
    index_value: str | None = None,
) -> bool:
    needle = query.casefold()
    values: list[Any] = [row.get(col) for col in columns]
    if index_value is not None:
        values.insert(0, index_value)
    return any(needle in ("" if value is None else str(value)).casefold() for value in values)


def _sort_key(value: Any) -> tuple[int, int, Any]:
    if value is None:
        return (1, 1, "")
    if isinstance(value, bool):
        return (0, 0, int(value))
    if isinstance(value, (int, float)):
        return (0, 0, value)
    return (0, 1, str(value).casefold())


def datatable_export_params(
    *,
    sort: str | None = None,
    direction: SortableDirection = "asc",
    search: str | None = None,
    search_param: str = "q",
    filters: dict[str, Any] | None = None,
    include_pagination: bool = False,
    page: int | None = None,
    per_page: int | None = None,
) -> dict[str, Any]:
    """Build query params for exporting DataTable state.

    This helper mirrors the DataTable query contract and is intended to be passed
    into ExportButton(extra_params=...).
    """
    params: dict[str, Any] = {}

    if filters:
        for key, value in filters.items():
            normalized = _normalize_query_value(value)
            if normalized is None:
                continue
            params[str(key)] = normalized

    if sort:
        params["sort"] = sort
        params["direction"] = direction

    if search is not None:
        params[search_param] = search

    if include_pagination:
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page

    return params


def datatable_query_params(
    *,
    sort: str | None = None,
    direction: SortableDirection = "asc",
    search: str | None = None,
    search_param: str = "q",
    filters: dict[str, Any] | None = None,
    page: int | None = None,
    per_page: int | None = None,
) -> dict[str, Any]:
    """Build the common DataTable query contract for links and handlers."""
    return datatable_export_params(
        sort=sort,
        direction=direction,
        search=search,
        search_param=search_param,
        filters=filters,
        include_pagination=page is not None or per_page is not None,
        page=page,
        per_page=per_page,
    )


def datatable_page_url(
    base_url: str,
    *,
    page: int,
    per_page: int | None = None,
    sort: str | None = None,
    direction: SortableDirection = "asc",
    search: str | None = None,
    search_param: str = "q",
    filters: dict[str, Any] | None = None,
) -> str:
    """Build a URL for one DataTable page while preserving current state."""
    params = datatable_query_params(
        sort=sort,
        direction=direction,
        search=search,
        search_param=search_param,
        filters=filters,
        page=max(1, page),
        per_page=per_page,
    )
    return _build_url(base_url, params)


def _link_attrs(
    url: str,
    *,
    endpoint: str | None,
    hx_target: str | None,
    hx_swap: str | None,
    push_url: bool,
) -> dict[str, Any]:
    attrs: dict[str, Any] = {"href": url}
    if endpoint:
        attrs["hx_get"] = url
        if hx_target:
            attrs["hx_target"] = hx_target
        if hx_swap:
            attrs["hx_swap"] = hx_swap
        if push_url:
            attrs["hx_push_url"] = "true"
    return attrs


@register(category="display")
@beta
def DataTable(
    data: Any,
    *,
    columns: list[str] | None = None,
    header_map: dict[str, str] | None = None,
    max_rows: int | None = None,
    include_index: bool = False,
    empty_text: str = "No data available",
    none_as: str = "",
    striped: bool = True,
    hover: bool = True,
    bordered: bool = False,
    responsive: bool | ResponsiveType = True,
    sortable: bool | list[str] = False,
    sort: str | None = None,
    direction: SortableDirection = "asc",
    searchable: bool = False,
    search: str | None = None,
    search_param: str = "q",
    search_placeholder: str = "Search...",
    search_debounce: int = 300,
    pagination: bool = False,
    page: int = 1,
    per_page: int = 25,
    total_rows: int | None = None,
    endpoint: str | None = None,
    base_url: str | None = None,
    filters: dict[str, Any] | None = None,
    hx_target: str | None = None,
    hx_swap: str | None = "outerHTML",
    poll_interval: int | None = None,
    poll_morph: bool = False,
    push_url: bool = False,
    table_id: str | None = None,
    table_cls: str | None = None,
    table_attrs: dict[str, Any] | None = None,
    mobile_mode: MobileMode = "scroll",
    mobile_breakpoint: ResponsiveType = "md",
    mobile_sortable: bool = True,
    mobile_title: str | None = None,
    mobile_subtitle: str | None = None,
    mobile_meta: list[str] | None = None,
    mobile_hidden: list[str] | None = None,
    mobile_card_cls: str | None = None,
    mobile_card_attrs: dict[str, Any] | None = None,
    mobile_card_renderer: Callable[[dict[str, Any]], Any] | None = None,
    mobile_field_renderers: dict[str, Callable[[Any, dict[str, Any]], Any]] | None = None,
    **kwargs: Any,
) -> Div:
    """DataTable with optional sorting, search, and pagination.

    Args:
        data: List of dicts or pandas/polars DataFrame.
        columns: Optional column order.
        header_map: Optional display name mapping for headers.
        max_rows: Optional max rows to render (pre-pagination).
        include_index: Include index column for DataFrame or list data.
        empty_text: Text to display when no records exist.
        none_as: Substitute for None values.
        striped: Enable zebra striping.
        hover: Enable row hover styles.
        bordered: Enable borders.
        responsive: Wrap table in Bootstrap responsive container.
        sortable: True for all columns or a list of sortable columns.
        sort: Current sort column.
        direction: Current sort direction.
        searchable: Render a search input.
        search: Current search value.
        search_param: Query param name for search.
        search_placeholder: Placeholder text for search input.
        search_debounce: Debounce (ms) for HTMX search input.
        pagination: Enable pagination controls.
        page: Current page (1-indexed).
        per_page: Rows per page.
        total_rows: Total rows across all pages (server-side).
        endpoint: HTMX endpoint for server-side updates.
        base_url: Base URL for standard links (fallback).
        filters: Extra query params to preserve in links.
        hx_target: HTMX target selector.
        hx_swap: HTMX swap strategy for links/search.
        push_url: If True, enable hx-push-url for links.
        table_id: Explicit wrapper id (auto-generated if omitted).
        table_cls: Extra CSS classes for the table element.
        mobile_mode: ``"scroll"`` retains the responsive table. ``"cards"``
            renders a responsive card grid below ``mobile_breakpoint``;
            ``"stack"`` renders flatter stacked record rows there.
        mobile_breakpoint: Bootstrap breakpoint where cards change back to the
            semantic table.
        mobile_sortable: Show a compact sort control in cards/stack mode when
            a server endpoint or base URL is configured.
        mobile_title: Column used as each card title. Defaults to the first
            data column.
        mobile_subtitle: Optional column rendered beneath the title.
        mobile_meta: Columns rendered as labeled metadata in each card.
        mobile_hidden: Columns excluded from generated mobile cards.
        mobile_card_cls: Extra classes applied to every generated mobile card.
        mobile_card_attrs: Attributes applied to every generated mobile card.
            Do not include ``id`` because one attribute set is reused for
            multiple records.
        mobile_card_renderer: Optional callable that receives a row dictionary
            and returns custom FastHTML content for its mobile presentation.
        mobile_field_renderers: Mapping of column names to callables receiving
            ``(value, row)`` and returning content for that mobile field.
        table_attrs: Extra attributes applied to the table element.
        **kwargs: Additional HTML attributes for the wrapper.
    """
    cfg = resolve_defaults(
        "DataTable",
        striped=striped,
        hover=hover,
        bordered=bordered,
        responsive=responsive,
        sortable=sortable,
        searchable=searchable,
        pagination=pagination,
        per_page=per_page,
        direction=direction,
        empty_text=empty_text,
        none_as=none_as,
    )

    c_striped = cfg.get("striped", striped)
    c_hover = cfg.get("hover", hover)
    c_bordered = cfg.get("bordered", bordered)
    c_responsive = cfg.get("responsive", responsive)
    c_sortable = cfg.get("sortable", sortable)
    c_searchable = cfg.get("searchable", searchable)
    c_pagination = cfg.get("pagination", pagination)

    if mobile_mode not in {None, "scroll", "cards", "stack"}:
        raise ValueError("mobile_mode must be None, 'scroll', 'cards', or 'stack'")
    if mobile_breakpoint not in {"sm", "md", "lg", "xl", "xxl"}:
        raise ValueError("mobile_breakpoint must be a Bootstrap breakpoint")
    c_per_page = cfg.get("per_page", per_page)
    c_direction = cfg.get("direction", direction)
    c_empty_text = cfg.get("empty_text", empty_text)
    c_none_as = cfg.get("none_as", none_as)

    if c_pagination and page < 1:
        msg = f"page must be >= 1, got {page}"
        raise ValueError(msg)
    if c_pagination and c_per_page < 1:
        msg = f"per_page must be >= 1, got {c_per_page}"
        raise ValueError(msg)

    resolved_columns, records, index_values = _normalize_table_data(
        data,
        columns=columns,
        max_rows=max_rows,
        include_index=include_index,
    )
    mobile_columns = set(resolved_columns)
    requested_mobile_columns = set(mobile_meta or []) | set(mobile_hidden or [])
    requested_mobile_columns.update(mobile_field_renderers or {})
    if mobile_title is not None:
        requested_mobile_columns.add(mobile_title)
    if mobile_subtitle is not None:
        requested_mobile_columns.add(mobile_subtitle)
    unknown_mobile_columns = requested_mobile_columns - mobile_columns
    if unknown_mobile_columns:
        names = ", ".join(sorted(unknown_mobile_columns))
        raise ValueError(f"Unknown mobile column(s): {names}")

    if isinstance(c_sortable, list):
        sortable_columns = [col for col in c_sortable if col in resolved_columns]
    elif c_sortable:
        sortable_columns = list(resolved_columns)
    else:
        sortable_columns = []

    if search:
        filtered_records: list[dict[str, Any]] = []
        filtered_index_values: list[str] | None = [] if index_values is not None else None
        for idx, row in enumerate(records):
            current_index = index_values[idx] if index_values is not None else None
            if _matches_search(
                row,
                columns=resolved_columns,
                query=search,
                index_value=current_index if include_index else None,
            ):
                filtered_records.append(row)
                if filtered_index_values is not None and current_index is not None:
                    filtered_index_values.append(current_index)
        records = filtered_records
        if filtered_index_values is not None:
            index_values = filtered_index_values

    if sort not in sortable_columns:
        sort = None
    elif endpoint is None:
        active_sort = cast(str, sort)
        indexed_records = list(enumerate(records))
        indexed_records.sort(
            key=lambda item: _sort_key(item[1].get(active_sort)),
            reverse=c_direction == "desc",
        )
        records = [record for _, record in indexed_records]
        if index_values is not None:
            index_values = [index_values[idx] for idx, _ in indexed_records]

    full_count = len(records)
    total_count = total_rows if total_rows is not None else full_count

    if c_pagination and endpoint is None and base_url is None:
        total_pages = math.ceil(total_count / c_per_page) if total_count else 1
        start = (page - 1) * c_per_page
        records = records[start : start + c_per_page]
        if index_values is not None:
            index_values = index_values[start : start + c_per_page]
    elif c_pagination:
        total_pages = math.ceil(total_count / c_per_page) if total_count else 1
    else:
        total_pages = 1

    visible_columns = list(resolved_columns)
    if include_index:
        visible_columns = ["index", *visible_columns]

    wrapper_id = kwargs.pop("id", None) or table_id
    if wrapper_id is None:
        wrapper_id = uniquify_id(
            _stable_table_id(
                columns=visible_columns,
                row_count=full_count,
                include_index=include_index,
                sortable=bool(sortable_columns),
                searchable=c_searchable,
                pagination=c_pagination,
            )
        )

    if hx_target is None:
        hx_target = f"#{wrapper_id}"

    link_base = endpoint or base_url

    base_params: dict[str, Any] = {}
    if filters:
        base_params.update(filters)
    if c_pagination:
        base_params["per_page"] = c_per_page
    if search:
        base_params[search_param] = search
    if sort:
        base_params["sort"] = sort
        base_params["direction"] = c_direction

    effective_hx_swap = "morph" if (poll_morph and hx_swap == "outerHTML") else hx_swap

    head_cells: list[Any] = []
    for col in visible_columns:
        header_label = (header_map or {}).get(col, col)
        if col in sortable_columns and link_base:
            current = sort == col
            next_dir: SortableDirection = "desc" if current and c_direction == "asc" else "asc"
            params = {**base_params, "sort": col, "direction": next_dir, "page": page}
            url = _build_url(link_base, params)
            link = A(
                header_label,
                (
                    Span(
                        "asc" if current and c_direction == "asc" else "desc",
                        cls="ms-1 text-muted small",
                    )
                    if current
                    else None
                ),
                cls="text-decoration-none",
                **_link_attrs(
                    url,
                    endpoint=endpoint,
                    hx_target=hx_target,
                    hx_swap=effective_hx_swap,
                    push_url=push_url,
                ),
            )
            aria_sort = (
                "ascending"
                if current and c_direction == "asc"
                else "descending" if current else None
            )
            head_cells.append(TCell(link, header=True, scope="col", aria_sort=aria_sort))
        else:
            head_cells.append(TCell(header_label, header=True, scope="col"))

    thead = THead(TRow(*head_cells))

    if not records:
        tbody = TBody(
            TRow(
                TCell(
                    c_empty_text,
                    colspan=max(1, len(visible_columns)),
                    cls="text-center text-muted",
                )
            )
        )
    else:
        body_rows: list[Any] = []
        for idx, row in enumerate(records):
            row_cells: list[Any] = []
            if include_index and index_values is not None:
                row_cells.append(TCell(index_values[idx], header=True, scope="row"))

            for col in resolved_columns:
                value = row.get(col)
                rendered = c_none_as if value is None else str(value)
                row_cells.append(TCell(rendered))

            body_rows.append(TRow(*row_cells))

        tbody = TBody(*body_rows)

    table_kwargs = table_attrs.copy() if table_attrs else {}
    table_kwargs["cls"] = merge_classes(table_kwargs.get("cls"), table_cls)

    table = Table(
        thead,
        tbody,
        striped=c_striped,
        hover=c_hover,
        bordered=c_bordered,
        responsive=c_responsive,
        **table_kwargs,
    )

    parts: list[Any] = []

    if c_searchable:
        input_attrs: dict[str, Any] = {
            "type": "search",
            "name": search_param,
            "value": search or "",
            "placeholder": search_placeholder,
            "cls": "form-control",
            "autocomplete": "off",
        }
        if endpoint:
            input_attrs.update(
                {
                    "hx_get": link_base,
                    "hx_target": hx_target,
                    "hx_trigger": f"keyup changed delay:{search_debounce}ms",
                    "hx_swap": effective_hx_swap,
                }
            )
            if push_url:
                input_attrs["hx_push_url"] = "true"
        hidden_inputs: list[Any] = []
        preserved_params = filters.copy() if filters else {}
        if sort:
            preserved_params["sort"] = sort
            preserved_params["direction"] = c_direction
        if c_pagination:
            preserved_params["per_page"] = c_per_page
            preserved_params["page"] = 1

        for key, value in preserved_params.items():
            normalized = _normalize_query_value(value)
            if normalized is None or str(key) == search_param:
                continue
            if isinstance(normalized, list):
                hidden_inputs.extend(
                    Input(type="hidden", name=str(key), value=item) for item in normalized
                )
            else:
                hidden_inputs.append(Input(type="hidden", name=str(key), value=normalized))

        search_form_attrs: dict[str, Any] = {"cls": "mb-3"}
        if link_base and not endpoint:
            search_form_attrs["method"] = "get"
            search_form_attrs["action"] = link_base

        search_form = Form(
            *hidden_inputs,
            Input(**input_attrs),
            **search_form_attrs,
        )
        parts.append(search_form)

    if mobile_mode in {"cards", "stack"}:
        parts.append(Div(table, cls=f"d-none d-{mobile_breakpoint}-block"))
        if mobile_sortable and sortable_columns and link_base:
            sort_links: list[Any] = []
            for col in sortable_columns:
                current = sort == col
                mobile_next_dir: SortableDirection = (
                    "desc" if current and c_direction == "asc" else "asc"
                )
                params = {**base_params, "sort": col, "direction": mobile_next_dir}
                if c_pagination:
                    params["page"] = 1
                url = _build_url(link_base, params)
                label = (header_map or {}).get(col, col)
                sort_links.append(
                    A(
                        label,
                        Span(" (sorted)" if current else "", cls="visually-hidden"),
                        cls=merge_classes(
                            "btn btn-sm",
                            "btn-primary" if current else "btn-outline-secondary",
                        ),
                        aria_label=f"Sort by {label}"
                        + (f", currently {c_direction}" if current else ""),
                        **_link_attrs(
                            url,
                            endpoint=endpoint,
                            hx_target=hx_target,
                            hx_swap=effective_hx_swap,
                            push_url=push_url,
                        ),
                    )
                )
            parts.append(
                Div(
                    Span("Sort:", cls="small fw-semibold me-1"),
                    *sort_links,
                    cls=f"d-{mobile_breakpoint}-none d-flex flex-wrap align-items-center gap-2 mb-3",
                    role="group",
                    aria_label="Sort records",
                )
            )
        parts.append(
            _mobile_presentation(
                records,
                columns=resolved_columns,
                header_map=header_map,
                none_as=c_none_as,
                title_column=mobile_title,
                subtitle_column=mobile_subtitle,
                meta_columns=mobile_meta,
                hidden_columns=mobile_hidden,
                card_cls=mobile_card_cls,
                card_attrs=mobile_card_attrs,
                card_renderer=mobile_card_renderer,
                field_renderers=mobile_field_renderers,
                mode=cast(Literal["cards", "stack"], mobile_mode),
                breakpoint=mobile_breakpoint,
                empty_text=c_empty_text,
                reserved_id=wrapper_id,
            )
        )
    else:
        parts.append(table)

    if c_pagination and total_pages > 1:
        pager_links: list[Any] = []
        for page_num in _pagination_window(page, total_pages):
            if page_num is None:
                pager_links.append(
                    Li(
                        Span("...", cls="page-link"),
                        cls="page-item disabled",
                        aria_hidden="true",
                    )
                )
                continue
            active = page_num == page
            if link_base:
                params = {**base_params, "page": page_num}
                url = _build_url(link_base, params)
                link = A(
                    str(page_num),
                    cls="page-link",
                    **_link_attrs(
                        url,
                        endpoint=endpoint,
                        hx_target=hx_target,
                        hx_swap=effective_hx_swap,
                        push_url=push_url,
                    ),
                )
            else:
                link = Span(str(page_num), cls="page-link")

            pager_links.append(
                Li(
                    link,
                    cls="page-item" + (" active" if active else ""),
                    aria_current="page" if active else None,
                )
            )

        pager = Nav(
            Ul(*pager_links, cls="pagination"),
            cls="mt-3",
            aria_label="Data table pagination",
        )
        parts.append(pager)

    wrapper_attrs: dict[str, Any] = {
        "id": wrapper_id,
        "cls": merge_classes("faststrap-data-table", kwargs.pop("cls", "")),
    }
    if poll_interval and (endpoint or base_url):
        wrapper_attrs["hx_get"] = endpoint or base_url
        wrapper_attrs["hx_trigger"] = f"every {poll_interval}s"
        wrapper_attrs["hx_target"] = f"#{wrapper_id}"
        wrapper_attrs["hx_swap"] = effective_hx_swap
    wrapper_attrs.update(convert_attrs(kwargs))

    return Div(*parts, **wrapper_attrs)


DataTable.export_params = datatable_export_params  # type: ignore[attr-defined]
DataTable.query_params = datatable_query_params  # type: ignore[attr-defined]
DataTable.page_url = datatable_page_url  # type: ignore[attr-defined]


def _mobile_presentation(
    records: list[dict[str, Any]],
    *,
    columns: list[str],
    header_map: dict[str, str] | None,
    none_as: str,
    title_column: str | None,
    subtitle_column: str | None,
    meta_columns: list[str] | None,
    hidden_columns: list[str] | None,
    card_cls: str | None,
    card_attrs: dict[str, Any] | None,
    card_renderer: Callable[[dict[str, Any]], Any] | None,
    field_renderers: dict[str, Callable[[Any, dict[str, Any]], Any]] | None,
    mode: Literal["cards", "stack"],
    breakpoint: ResponsiveType,
    empty_text: str,
    reserved_id: str,
) -> Div:
    """Build the small-screen card representation for ``DataTable``."""
    hidden = set(hidden_columns or [])
    title_key = title_column or (columns[0] if columns else None)
    subtitle_key = subtitle_column if subtitle_column in columns else None
    if title_key in hidden:
        title_key = None
    if subtitle_key in hidden:
        subtitle_key = None
    default_meta = [column for column in columns if column not in {title_key, subtitle_key}]
    selected_meta = default_meta if meta_columns is None else meta_columns
    metadata = [column for column in selected_meta if column in columns and column not in hidden]
    card_defaults = dict(card_attrs or {})
    if "id" in card_defaults:
        raise ValueError("mobile_card_attrs cannot include 'id'; cards need unique IDs")
    cards: list[Any] = []
    for row in records:
        if card_renderer is not None:
            attrs = card_defaults.copy()
            if "id" in attrs:
                raise ValueError("mobile_card_attrs cannot include 'id'; cards need unique IDs")
            attrs["cls"] = merge_classes("faststrap-data-table-card", card_cls, attrs.get("cls"))
            cards.append(Div(card_renderer(row), **attrs))
            continue
        title = _mobile_value(row.get(title_key), none_as) if title_key else None
        subtitle = _mobile_value(row.get(subtitle_key), none_as) if subtitle_key else None
        fields = [
            Div(
                Span((header_map or {}).get(column, column), cls="faststrap-data-table-card-label"),
                Span(
                    (
                        field_renderers[column](row.get(column), row)
                        if field_renderers and column in field_renderers
                        else _mobile_value(row.get(column), none_as)
                    ),
                    cls="faststrap-data-table-card-value",
                ),
                cls="faststrap-data-table-card-field",
            )
            for column in metadata
        ]
        attrs = card_defaults.copy()
        attrs["cls"] = merge_classes("faststrap-data-table-card", card_cls, attrs.get("cls"))
        cards.append(ListItem(*fields, title=title, subtitle=subtitle, lines=3, **attrs))

    seen_ids = {reserved_id}
    for card in cards:
        for element_id in _iter_element_ids(card):
            if element_id in seen_ids:
                raise ValueError(
                    f"mobile card content contains duplicate or reserved element id {element_id!r}"
                )
            seen_ids.add(element_id)

    if not cards:
        cards.append(Div(empty_text, cls="text-center text-muted py-4"))
    if mode == "cards":
        content = GridList(*cards, min_width="100%", gap=2, cls="faststrap-data-table-cards")
    else:
        content = Div(*cards, cls="faststrap-data-table-stack")
    return Div(content, cls=f"d-{breakpoint}-none")


def _iter_element_ids(node: Any) -> Iterator[str]:
    """Yield explicit IDs recursively from FastHTML elements and containers."""
    attrs = getattr(node, "attrs", None)
    if isinstance(attrs, Mapping) and attrs.get("id") is not None:
        yield str(attrs["id"])
    children = getattr(node, "children", None)
    if children is not None:
        yield from _iter_element_ids(children)
    elif isinstance(node, (list, tuple)):
        for child in node:
            yield from _iter_element_ids(child)


def _mobile_value(value: Any, none_as: str) -> str:
    return none_as if value is None else str(value)
