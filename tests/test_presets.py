"""Tests for presets module (interactions, responses, auth)."""

from fasthtml.common import Response, to_xml

from faststrap.presets import (
    ActiveSearch,
    AutoRefresh,
    InfiniteScroll,
    LazyLoad,
    LoadingButton,
    hx_redirect,
    hx_refresh,
    hx_trigger,
    require_auth,
)


# Interaction Presets Tests
def test_active_search():
    """ActiveSearch creates search input with HTMX."""
    search = ActiveSearch(endpoint="/search", target="#results")
    html = to_xml(search)

    assert "/search" in html
    assert "#results" in html
    assert "hx-get" in html
    assert "hx-trigger" in html


def test_infinite_scroll():
    """InfiniteScroll creates scroll trigger."""
    scroll = InfiniteScroll(endpoint="/feed?page=2", target="#feed")
    html = to_xml(scroll)

    assert "/feed?page=2" in html
    assert "#feed" in html
    assert "hx-get" in html


def test_auto_refresh():
    """AutoRefresh creates polling element."""
    refresh = AutoRefresh(endpoint="/metrics", target="this", interval=5000)
    html = to_xml(refresh)

    assert "/metrics" in html
    assert "5000" in html or "5s" in html
    assert "hx-get" in html


def test_lazy_load():
    """LazyLoad creates lazy-loaded container."""
    lazy = LazyLoad(endpoint="/api/widget")
    html = to_xml(lazy)

    assert "/api/widget" in html
    assert "hx-get" in html


def test_loading_button():
    """LoadingButton creates button with loading state."""
    btn = LoadingButton("Save", endpoint="/save")
    html = to_xml(btn)

    assert "Save" in html
    assert "/save" in html
    assert "hx-indicator" in html or "htmx-indicator" in html


# Response Helpers Tests
def test_hx_redirect():
    """hx_redirect returns redirect response."""
    response = hx_redirect("/dashboard")

    assert isinstance(response, Response)
    assert response.headers.get("HX-Redirect") == "/dashboard"


def test_hx_refresh():
    """hx_refresh returns refresh response."""
    response = hx_refresh()

    assert isinstance(response, Response)
    assert response.headers.get("HX-Refresh") == "true"


def test_hx_trigger():
    """hx_trigger returns trigger response."""
    response = hx_trigger("showToast")

    assert isinstance(response, Response)
    assert "showToast" in response.headers.get("HX-Trigger", "")


def test_hx_trigger_with_detail():
    """hx_trigger supports event detail."""
    response = hx_trigger({"showToast": {"message": "Saved!"}})

    assert isinstance(response, Response)
    trigger_header = response.headers.get("HX-Trigger", "")
    assert "showToast" in trigger_header


# Auth Decorator Tests
def test_require_auth_decorator():
    """@require_auth decorator exists and is callable."""

    @require_auth(login_url="/login")
    def protected_route(req):
        return "Protected content"

    assert callable(protected_route)


def test_require_auth_custom_session_key():
    """@require_auth supports custom session key."""

    @require_auth(session_key="custom_user_id")
    def route(req):
        return "Content"

    assert callable(route)
