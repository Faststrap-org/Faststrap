"""Tests for ErrorPage component."""

from fasthtml.common import to_xml

from faststrap.components.feedback import ErrorPage


def test_error_page_404():
    """ErrorPage renders default 404 page."""
    title, content = ErrorPage(404)
    html = to_xml(content)

    assert "404" in to_xml(title)
    assert "Page Not Found" in html
    assert "doesn't exist" in html
    assert "Go Home" in html


def test_error_page_500():
    """ErrorPage renders default 500 page."""
    title, content = ErrorPage(500)
    html = to_xml(content)

    assert "500" in to_xml(title)
    assert "Server Error" in html
    assert "Something went wrong" in html


def test_error_page_403():
    """ErrorPage renders default 403 page."""
    title, content = ErrorPage(403)
    html = to_xml(content)

    assert "403" in to_xml(title)
    assert "Access Denied" in html
    assert "permission" in html


def test_error_page_custom_message():
    """ErrorPage supports custom backend error messages."""
    title, content = ErrorPage(500, message="Database connection timeout")
    html = to_xml(content)

    assert "Database connection timeout" in html
    assert "Server Error" in html  # Title still uses default


def test_error_page_custom_title():
    """ErrorPage supports custom title."""
    title, content = ErrorPage(403, title="Premium Feature")
    html = to_xml(content)

    assert "Premium Feature" in html


def test_error_page_custom_action():
    """ErrorPage supports custom action button."""
    title, content = ErrorPage(404, action_text="Back to Dashboard", action_href="/dashboard")
    html = to_xml(content)

    assert "Back to Dashboard" in html
    assert "/dashboard" in html


def test_error_page_no_action():
    """ErrorPage can hide action button."""
    title, content = ErrorPage(500, action_text=None)
    html = to_xml(content)

    assert "Go Home" not in html


def test_error_page_hide_code():
    """ErrorPage can hide error code display."""
    title, content = ErrorPage(404, show_code=False)
    html = to_xml(content)

    # Code should not be in large display format
    assert "display-1" not in html


def test_error_page_custom_code():
    """ErrorPage supports custom error codes."""
    title, content = ErrorPage(
        418, title="I'm a teapot", message="This server refuses to brew coffee", icon="cup-hot"
    )
    html = to_xml(content)

    assert "418" in html
    assert "I'm a teapot" in html
    assert "refuses to brew coffee" in html


def test_error_page_custom_classes():
    """ErrorPage merges custom classes."""
    title, content = ErrorPage(404, cls="custom-error")
    html = to_xml(content)

    assert "custom-error" in html
    assert "min-vh-100" in html  # Default class preserved


def test_error_page_returns_tuple():
    """ErrorPage returns (Title, Div) tuple for FastHTML routes."""
    result = ErrorPage(404)

    assert isinstance(result, tuple)
    assert len(result) == 2
    # First element should be Title
    assert "404" in to_xml(result[0])
