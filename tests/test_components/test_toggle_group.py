"""Tests for ToggleGroup component."""

from fasthtml.common import to_xml

from faststrap import Button
from faststrap.components.forms import ToggleGroup


def test_toggle_group_basic():
    group = ToggleGroup(Button("A"), Button("B"))
    html = to_xml(group)
    assert 'data-fs-toggle-group="true"' in html
    assert 'data-fs-toggle-item="true"' in html
    assert "active" in html


def test_toggle_group_values_and_hidden_input():
    group = ToggleGroup(
        Button("Newest"),
        Button("Popular"),
        name="sort",
        values=["new", "popular"],
        active_index=1,
    )
    html = to_xml(group)
    assert 'name="sort"' in html
    assert 'value="popular"' in html
