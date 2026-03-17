"""Tests for HTML attribute conversion helpers."""

from faststrap.utils.attrs import convert_attrs


def test_convert_attrs_merges_style_and_css_vars() -> None:
    attrs = convert_attrs(
        {
            "style": {"margin_top": "1rem"},
            "css_vars": {"brand_color": "#fff"},
        }
    )
    style = attrs["style"]
    assert "margin-top: 1rem" in style
    assert "--brand-color: #fff" in style


def test_convert_attrs_stringifies_complex_values() -> None:
    attrs = convert_attrs(
        {
            "css_vars": {"config": {"alpha": 1, "beta": [1, 2]}},
            "data": {"payload": {"id": 5, "name": "Ada"}},
            "aria": {"meta": {"step": 2}},
        }
    )
    assert '--config: {"alpha": 1, "beta": [1, 2]}' in attrs["style"]
    assert attrs["data-payload"] == '{"id": 5, "name": "Ada"}'
    assert attrs["aria-meta"] == '{"step": 2}'


def test_convert_attrs_preserves_structured_false_values() -> None:
    attrs = convert_attrs({"data": {"enabled": False}, "aria": {"hidden": False}})
    assert attrs["data-enabled"] == "false"
    assert attrs["aria-hidden"] == "false"


def test_convert_attrs_preserves_direct_aria_false() -> None:
    attrs = convert_attrs({"aria_hidden": False})
    assert attrs["aria-hidden"] == "false"
