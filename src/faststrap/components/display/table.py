"""Bootstrap Table component with responsive, striped, hover, and bordered variants."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import Div, Tbody, Td, Th, Thead, Tr
from fasthtml.common import Table as FTTable

from ...core._stability import beta, stable
from ...core.base import merge_classes
from ...utils.attrs import convert_attrs

# Table-specific types
TableVariantType = Literal[
    "primary", "secondary", "success", "danger", "warning", "info", "light", "dark"
]


@stable
def Table(
    *children: Any,
    striped: bool = False,
    striped_columns: bool = False,
    bordered: bool = False,
    borderless: bool = False,
    hover: bool = False,
    small: bool = False,
    variant: TableVariantType | None = None,
    responsive: bool | Literal["sm", "md", "lg", "xl", "xxl"] = False,
    caption_top: bool = False,
    **kwargs: Any,
) -> FTTable | Div:
    """Bootstrap Table component.

    A responsive, styled table with support for striped rows, hover effects,
    borders, and color variants.

    Args:
        *children: Table content (THead, TBody, or direct Tr elements)
        striped: Add zebra-striping to rows
        striped_columns: Add zebra-striping to columns
        bordered: Add borders on all sides
        borderless: Remove all borders
        hover: Enable hover state on rows
        small: Make table more compact
        variant: Bootstrap color variant for table background
        responsive: Make table horizontally scrollable. True for all breakpoints,
                   or specify breakpoint (sm, md, lg, xl, xxl)
        caption_top: Place caption at top of table
        **kwargs: Additional HTML attributes (cls, id, hx-*, data-*, etc.)

    Returns:
        FastHTML Table element, wrapped in Div if responsive

    Example:
        Basic table:
        >>> Table(
        ...     THead(TRow(TCell("Name", header=True), TCell("Age", header=True))),
        ...     TBody(TRow(TCell("Alice"), TCell("25")))
        ... )

        Striped and hoverable:
        >>> Table(
        ...     THead(...),
        ...     TBody(...),
        ...     striped=True,
        ...     hover=True
        ... )

        Responsive with variant:
        >>> Table(..., responsive=True, variant="dark")

        Responsive at breakpoint:
        >>> Table(..., responsive="lg")

    See Also:
        Bootstrap docs: https://getbootstrap.com/docs/5.3/content/tables/
    """
    # Build table classes
    classes = ["table"]

    if striped:
        classes.append("table-striped")

    if striped_columns:
        classes.append("table-striped-columns")

    if bordered:
        classes.append("table-bordered")

    if borderless:
        classes.append("table-borderless")

    if hover:
        classes.append("table-hover")

    if small:
        classes.append("table-sm")

    if variant:
        classes.append(f"table-{variant}")

    if caption_top:
        classes.append("caption-top")

    # Merge with user classes
    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes(" ".join(classes), user_cls)

    # Build attributes
    attrs: dict[str, Any] = {"cls": all_classes}
    attrs.update(convert_attrs(kwargs))

    # Create table
    table = FTTable(*children, **attrs)

    # Wrap in responsive container if needed
    if responsive:
        if responsive is True:
            responsive_cls = "table-responsive"
        else:
            responsive_cls = f"table-responsive-{responsive}"
        return Div(table, cls=responsive_cls)

    return table


@stable
def THead(
    *children: Any,
    variant: TableVariantType | None = None,
    **kwargs: Any,
) -> Thead:
    """Bootstrap table header section.

    Args:
        *children: Header rows (TRow elements)
        variant: Bootstrap color variant for header background
        **kwargs: Additional HTML attributes

    Returns:
        FastHTML Thead element

    Example:
        >>> THead(
        ...     TRow(TCell("Name", header=True), TCell("Email", header=True)),
        ...     variant="dark"
        ... )
    """
    classes = []

    if variant:
        classes.append(f"table-{variant}")

    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes(" ".join(classes), user_cls) if classes else user_cls

    attrs: dict[str, Any] = {}
    if all_classes:
        attrs["cls"] = all_classes
    attrs.update(convert_attrs(kwargs))

    return Thead(*children, **attrs)


@stable
def TBody(
    *children: Any,
    variant: TableVariantType | None = None,
    divider: bool = False,
    **kwargs: Any,
) -> Tbody:
    """Bootstrap table body section.

    Args:
        *children: Body rows (TRow elements)
        variant: Bootstrap color variant for body background
        divider: Add a thicker border on top (table-group-divider)
        **kwargs: Additional HTML attributes

    Returns:
        FastHTML Tbody element

    Example:
        >>> TBody(
        ...     TRow(TCell("Alice"), TCell("alice@example.com")),
        ...     TRow(TCell("Bob"), TCell("bob@example.com")),
        ...     divider=True
        ... )
    """
    classes = []

    if variant:
        classes.append(f"table-{variant}")

    if divider:
        classes.append("table-group-divider")

    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes(" ".join(classes), user_cls) if classes else user_cls

    attrs: dict[str, Any] = {}
    if all_classes:
        attrs["cls"] = all_classes
    attrs.update(convert_attrs(kwargs))

    return Tbody(*children, **attrs)


@stable
def TRow(
    *children: Any,
    variant: TableVariantType | None = None,
    active: bool = False,
    **kwargs: Any,
) -> Tr:
    """Bootstrap table row.

    Args:
        *children: Row cells (TCell elements)
        variant: Bootstrap color variant for row background
        active: Highlight row as selected/active
        **kwargs: Additional HTML attributes

    Returns:
        FastHTML Tr element

    Example:
        >>> TRow(TCell("Data 1"), TCell("Data 2"), variant="success")
        >>> TRow(TCell("Selected"), TCell("Row"), active=True)
    """
    classes = []

    if variant:
        classes.append(f"table-{variant}")

    if active:
        classes.append("table-active")

    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes(" ".join(classes), user_cls) if classes else user_cls

    attrs: dict[str, Any] = {}
    if all_classes:
        attrs["cls"] = all_classes
    attrs.update(convert_attrs(kwargs))

    return Tr(*children, **attrs)


@stable
def TCell(
    *children: Any,
    header: bool = False,
    variant: TableVariantType | None = None,
    active: bool = False,
    colspan: int | None = None,
    rowspan: int | None = None,
    scope: Literal["row", "col", "rowgroup", "colgroup"] | None = None,
    **kwargs: Any,
) -> Th | Td:
    """Bootstrap table cell (th or td).

    Args:
        *children: Cell content
        header: Render as th instead of td
        variant: Bootstrap color variant for cell background
        active: Highlight cell as selected/active
        colspan: Number of columns to span
        rowspan: Number of rows to span
        scope: Scope for header cells (row, col, rowgroup, colgroup)
        **kwargs: Additional HTML attributes

    Returns:
        FastHTML Th or Td element

    Example:
        >>> TCell("Header", header=True, scope="col")
        >>> TCell("Data", variant="warning")
        >>> TCell("Wide Cell", colspan=2)
    """
    classes = []

    if variant:
        classes.append(f"table-{variant}")

    if active:
        classes.append("table-active")

    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes(" ".join(classes), user_cls) if classes else user_cls

    attrs: dict[str, Any] = {}
    if all_classes:
        attrs["cls"] = all_classes

    if colspan:
        attrs["colspan"] = str(colspan)

    if rowspan:
        attrs["rowspan"] = str(rowspan)

    if scope and header:
        attrs["scope"] = scope

    attrs.update(convert_attrs(kwargs))

    if header:
        return Th(*children, **attrs)
    return Td(*children, **attrs)


@beta
def _table_from_df(
    data: Any,
    *,
    columns: list[str] | None = None,
    max_rows: int | None = None,
    include_index: bool = False,
    empty_text: str = "No data available",
    none_as: str = "",
    header_map: dict[str, str] | None = None,
    **table_kwargs: Any,
) -> FTTable | Div:
    """Build a table from pandas/polars data or list-of-dict records."""
    if max_rows is not None and max_rows < 0:
        msg = f"max_rows must be >= 0, got {max_rows}"
        raise ValueError(msg)

    resolved_columns: list[str]
    records: list[dict[str, Any]]
    index_values: list[str] | None = None

    if isinstance(data, list) and all(isinstance(item, dict) for item in data):
        records = list(data)
        if columns is not None:
            resolved_columns = columns
        else:
            key_order: list[str] = []
            seen_keys: set[str] = set()
            for item in records:
                for key in item.keys():
                    key_str = str(key)
                    if key_str not in seen_keys:
                        key_order.append(key_str)
                        seen_keys.add(key_str)
            resolved_columns = key_order
        if max_rows is not None:
            records = records[:max_rows]
    else:
        cls_name = data.__class__.__name__
        module_name = data.__class__.__module__

        if cls_name == "DataFrame" and module_name.startswith("pandas"):
            df = data
            if columns is not None:
                missing = [col for col in columns if col not in df.columns]
                if missing:
                    msg = f"Requested columns not found in DataFrame: {missing}"
                    raise ValueError(msg)
                df = df[columns]
            if max_rows is not None:
                df = df.head(max_rows)
            resolved_columns = [str(col) for col in df.columns]
            records = [
                {str(key): value for key, value in row.items()}
                for row in df.to_dict(orient="records")
            ]
            if include_index:
                index_values = [str(i) for i in df.index.tolist()]
        elif cls_name == "DataFrame" and module_name.startswith("polars"):
            df = data
            if columns is not None:
                missing = [col for col in columns if col not in df.columns]
                if missing:
                    msg = f"Requested columns not found in DataFrame: {missing}"
                    raise ValueError(msg)
                df = df.select(columns)
            if max_rows is not None:
                df = df.head(max_rows)
            resolved_columns = [str(col) for col in df.columns]
            records = [{str(key): value for key, value in row.items()} for row in df.to_dicts()]
        else:
            msg = (
                "Table.from_df() expects pandas/polars DataFrame or list[dict]. "
                f"Received: {data.__class__.__name__}"
            )
            raise TypeError(msg)

    if include_index and index_values is None:
        index_values = [str(i) for i in range(len(records))]

    visible_columns = list(resolved_columns)
    if include_index:
        visible_columns = ["index", *visible_columns]

    head_cells = [
        TCell((header_map or {}).get(col, col), header=True, scope="col") for col in visible_columns
    ]
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
        return Table(thead, tbody, **table_kwargs)

    body_rows: list[Tr] = []
    for idx, row in enumerate(records):
        row_cells: list[Td | Th] = []
        if include_index and index_values is not None:
            row_cells.append(TCell(index_values[idx], header=True, scope="row"))

        for col in resolved_columns:
            value = row.get(col)
            if value is None:
                rendered = none_as
            else:
                rendered = str(value)
            row_cells.append(TCell(rendered))

        body_rows.append(TRow(*row_cells))

    tbody = TBody(*body_rows)
    return Table(thead, tbody, **table_kwargs)


Table.from_df = _table_from_df  # type: ignore[attr-defined]
