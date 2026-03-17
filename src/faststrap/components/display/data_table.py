"""DataTable component for sortable, searchable, paginated data views."""

from __future__ import annotations

import hashlib
import json
import math
from typing import Any, Literal
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

from fasthtml.common import A, Div, Form, Input, Li, Nav, Span, Ul

from ...core._stability import beta
from ...core.base import merge_classes
from ...core.registry import register
from ...utils.attrs import convert_attrs
from .table import Table, TBody, TCell, THead, TRow, _normalize_table_data

SortableDirection = Literal["asc", "desc"]
ResponsiveType = Literal["sm", "md", "lg", "xl", "xxl"]

_DATA_TABLE_ID_COUNTS: dict[str, int] = {}


def _unique_table_id(base_id: str) -> str:
    count = _DATA_TABLE_ID_COUNTS.get(base_id, 0) + 1
    _DATA_TABLE_ID_COUNTS[base_id] = count
    if count == 1:
        return base_id
    return f"{base_id}-{count}"


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
    ).hexdigest()[:10]
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
    push_url: bool = False,
    table_id: str | None = None,
    table_cls: str | None = None,
    table_attrs: dict[str, Any] | None = None,
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
        table_attrs: Extra attributes applied to the table element.
        **kwargs: Additional HTML attributes for the wrapper.
    """
    if pagination and page < 1:
        msg = f"page must be >= 1, got {page}"
        raise ValueError(msg)
    if pagination and per_page < 1:
        msg = f"per_page must be >= 1, got {per_page}"
        raise ValueError(msg)

    resolved_columns, records, index_values = _normalize_table_data(
        data,
        columns=columns,
        max_rows=max_rows,
        include_index=include_index,
    )

    full_count = len(records)
    total_count = total_rows if total_rows is not None else full_count

    if pagination and endpoint is None and base_url is None:
        total_pages = math.ceil(total_count / per_page) if total_count else 1
        start = (page - 1) * per_page
        records = records[start : start + per_page]
    elif pagination:
        total_pages = math.ceil(total_count / per_page) if total_count else 1
    else:
        total_pages = 1

    if isinstance(sortable, list):
        sortable_columns = [col for col in sortable if col in resolved_columns]
    elif sortable:
        sortable_columns = list(resolved_columns)
    else:
        sortable_columns = []

    if sort not in sortable_columns:
        sort = None

    visible_columns = list(resolved_columns)
    if include_index:
        visible_columns = ["index", *visible_columns]

    wrapper_id = kwargs.pop("id", None) or table_id
    if wrapper_id is None:
        wrapper_id = _unique_table_id(
            _stable_table_id(
                columns=visible_columns,
                row_count=full_count,
                include_index=include_index,
                sortable=bool(sortable_columns),
                searchable=searchable,
                pagination=pagination,
            )
        )

    if hx_target is None:
        hx_target = f"#{wrapper_id}"

    link_base = endpoint or base_url

    base_params: dict[str, Any] = {}
    if filters:
        base_params.update(filters)
    if pagination:
        base_params["per_page"] = per_page
    if search:
        base_params[search_param] = search
    if sort:
        base_params["sort"] = sort
        base_params["direction"] = direction

    head_cells: list[Any] = []
    for col in visible_columns:
        header_label = (header_map or {}).get(col, col)
        if col in sortable_columns and link_base:
            current = sort == col
            next_dir: SortableDirection = "desc" if current and direction == "asc" else "asc"
            params = {**base_params, "sort": col, "direction": next_dir, "page": page}
            url = _build_url(link_base, params)
            link = A(
                header_label,
                (
                    Span(
                        "asc" if current and direction == "asc" else "desc",
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
                    hx_swap=hx_swap,
                    push_url=push_url,
                ),
            )
            aria_sort = "ascending" if current and direction == "asc" else "descending"
            head_cells.append(TCell(link, header=True, scope="col", aria_sort=aria_sort))
        else:
            head_cells.append(TCell(header_label, header=True, scope="col"))

    thead = THead(TRow(*head_cells))

    if not records:
        tbody = TBody(
            TRow(
                TCell(
                    empty_text,
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
                rendered = none_as if value is None else str(value)
                row_cells.append(TCell(rendered))

            body_rows.append(TRow(*row_cells))

        tbody = TBody(*body_rows)

    table_kwargs = table_attrs.copy() if table_attrs else {}
    table_kwargs["cls"] = merge_classes(table_kwargs.get("cls"), table_cls)

    table = Table(
        thead,
        tbody,
        striped=striped,
        hover=hover,
        bordered=bordered,
        responsive=responsive,
        **table_kwargs,
    )

    parts: list[Any] = []

    if searchable:
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
                    "hx_swap": hx_swap,
                }
            )
            if push_url:
                input_attrs["hx_push_url"] = "true"

        search_form = Form(
            Input(**input_attrs),
            cls="mb-3",
        )
        parts.append(search_form)

    parts.append(table)

    if pagination and total_pages > 1:
        pager_links: list[Any] = []
        for page_num in range(1, total_pages + 1):
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
                        hx_swap=hx_swap,
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
    wrapper_attrs.update(convert_attrs(kwargs))

    return Div(*parts, **wrapper_attrs)
