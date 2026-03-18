"""Tests for ExportButton component."""

from fasthtml.common import to_xml

from faststrap import ExportButton


def test_export_button_get_href():
    html = to_xml(
        ExportButton(
            "Export CSV",
            endpoint="/export",
            export_format="csv",
            filename="data.csv",
        )
    )

    assert 'href="/export?format=csv&amp;filename=data.csv"' in html
    assert 'download="data.csv"' in html


def test_export_button_hx_post():
    html = to_xml(
        ExportButton(
            "Export",
            endpoint="/export",
            export_format="json",
            method="post",
            use_hx=True,
            hx_target="#results",
        )
    )

    assert "hx-post" in html
    assert "hx-target" in html


def test_export_button_post_form():
    html = to_xml(
        ExportButton(
            "Export",
            endpoint="/export",
            export_format="xlsx",
            method="post",
        )
    )

    assert 'method="post"' in html
    assert 'name="format"' in html


def test_export_button_repeats_multi_value_params_for_get_and_post():
    get_html = to_xml(
        ExportButton(
            endpoint="/export",
            extra_params={"team": ["ops", "eng"]},
        )
    )
    post_html = to_xml(
        ExportButton(
            endpoint="/export",
            method="post",
            extra_params={"team": ["ops", "eng"]},
        )
    )

    assert 'team=ops' in get_html
    assert 'team=eng' in get_html
    assert "['ops', 'eng']" not in get_html
    assert post_html.count('name="team"') == 2
    assert "['ops', 'eng']" not in post_html
