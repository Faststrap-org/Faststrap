"""Tests for Table.from_df() builder."""

from __future__ import annotations

import pandas as pd
from fasthtml.common import to_xml

from faststrap.components.display import Table


def test_table_from_df_with_pandas_dataframe() -> None:
    df = pd.DataFrame(
        [
            {"name": "Alice", "age": 25},
            {"name": "Bob", "age": 30},
        ]
    )
    table = Table.from_df(df, striped=True)  # type: ignore[attr-defined]
    html = to_xml(table)

    assert "<table" in html
    assert "table-striped" in html
    assert "Alice" in html
    assert "Bob" in html
    assert "<thead" in html
    assert "<tbody" in html


def test_table_from_df_supports_include_index_and_max_rows() -> None:
    df = pd.DataFrame(
        [
            {"name": "Alice", "age": 25},
            {"name": "Bob", "age": 30},
        ],
        index=["u1", "u2"],
    )
    table = Table.from_df(df, include_index=True, max_rows=1)  # type: ignore[attr-defined]
    html = to_xml(table)

    assert "u1" in html
    assert "u2" not in html
    assert "index" in html


def test_table_from_df_supports_list_of_dicts() -> None:
    rows = [{"city": "Lagos", "country": "Nigeria"}, {"city": "Nairobi", "country": "Kenya"}]
    table = Table.from_df(rows)  # type: ignore[attr-defined]
    html = to_xml(table)

    assert "Lagos" in html
    assert "Nairobi" in html
    assert "country" in html


def test_table_from_df_handles_empty_records() -> None:
    table = Table.from_df([], columns=["name", "age"])  # type: ignore[attr-defined]
    html = to_xml(table)
    assert "No data available" in html
    assert 'colspan="2"' in html


def test_table_from_df_rejects_unsupported_input() -> None:
    try:
        Table.from_df("bad-input")  # type: ignore[attr-defined]
        raise AssertionError("Expected TypeError for unsupported input")
    except TypeError as exc:
        assert "expects pandas/polars DataFrame or list[dict]" in str(exc)


def test_table_from_df_rejects_negative_max_rows() -> None:
    try:
        Table.from_df([], max_rows=-1)  # type: ignore[attr-defined]
        raise AssertionError("Expected ValueError for negative max_rows")
    except ValueError as exc:
        assert "max_rows must be >= 0" in str(exc)


def test_table_from_df_rejects_missing_requested_columns() -> None:
    df = pd.DataFrame([{"name": "Alice", "age": 25}])
    try:
        Table.from_df(df, columns=["name", "email"])  # type: ignore[attr-defined]
        raise AssertionError("Expected ValueError for unknown column")
    except ValueError as exc:
        assert "Requested columns not found" in str(exc)
