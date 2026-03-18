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
from ...core.theme import resolve_defaults
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
        indexed_records = list(enumerate(records))
        indexed_records.sort(
            key=lambda item: _sort_key(item[1].get(sort)),
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
        wrapper_id = _unique_table_id(
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
                    hx_swap=hx_swap,
                    push_url=push_url,
                ),
            )
            aria_sort = (
                "ascending" if current and c_direction == "asc" else "descending" if current else None
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
                    "hx_swap": hx_swap,
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
                hidden_inputs.extend(Input(type="hidden", name=str(key), value=item) for item in normalized)
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

    parts.append(table)

    if c_pagination and total_pages > 1:
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


DataTable.export_params = datatable_export_params  # type: ignore[attr-defined]
