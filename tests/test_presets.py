"""Tests for presets module (interactions, responses, auth)."""

from fasthtml.common import Response, to_xml
from starlette.requests import Request
from starlette.responses import RedirectResponse

from faststrap.presets import (
    ActiveSearch,
    AutoRefresh,
    InfiniteScroll,
    LazyLoad,
    LoadingButton,
    LocationAction,
    OptimisticAction,
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


def test_infinite_scroll_threshold_modes():
    numeric_html = to_xml(
        InfiniteScroll(endpoint="/feed?page=2", target="#feed", threshold="0.5")
    )
    margin_html = to_xml(
        InfiniteScroll(endpoint="/feed?page=2", target="#feed", threshold="200px")
    )

    assert 'hx-trigger="intersect once threshold:0.5"' in numeric_html
    assert 'hx-trigger="faststrap:infinite-scroll once"' in margin_html
    assert 'data-fs-infinite-scroll="true"' in margin_html
    assert 'data-fs-infinite-margin="200px"' in margin_html


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


def test_optimistic_action_contract_attributes():
    """OptimisticAction emits apply/commit/rollback lifecycle attributes."""
    btn = OptimisticAction(
        "Archive",
        endpoint="/items/1/archive",
        target="#item-1",
        action_id="archive-1",
        payload={"item_id": 1},
    )
    html = to_xml(btn)

    assert "/items/1/archive" in html
    assert "faststrap:optimistic:apply" in html
    assert "faststrap:optimistic:commit" in html
    assert "faststrap:optimistic:rollback" in html
    assert 'data-faststrap-optimistic-id="archive-1"' in html
    assert "hx-on::before-request" in html
    assert "hx-on::after-request" in html
    assert "hx-on::response-error" in html


def test_optimistic_action_invalid_method_raises():
    """OptimisticAction validates allowed HTTP methods."""
    try:
        OptimisticAction("Run", endpoint="/jobs/1", method="trace")
        raise AssertionError("Expected ValueError for unsupported HTTP method")
    except ValueError as exc:
        assert "Unsupported HTTP method" in str(exc)


def test_location_action_has_geolocation_contract() -> None:
    """LocationAction should emit success/error event hooks and use geolocation."""
    btn = LocationAction(
        "Use Location",
        endpoint="/api/location",
        target="#location-result",
    )
    html = to_xml(btn)
    assert "navigator.geolocation.getCurrentPosition" in html
    assert "faststrap:location:success" in html
    assert "faststrap:location:error" in html
    assert "/api/location" in html
    assert "#location-result" in html


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


def test_require_auth_redirects_with_relative_next_url():
    @require_auth(login_url="/login")
    def protected_route(req):
        return "Protected content"

    request = Request(
        {
            "type": "http",
            "method": "GET",
            "path": "/dashboard",
            "query_string": b"tab=activity",
            "headers": [],
            "scheme": "https",
            "server": ("example.com", 443),
            "client": ("127.0.0.1", 1234),
            "session": {},
        }
    )
    response = protected_route(request)

    assert isinstance(response, RedirectResponse)
    assert response.headers["location"] == "/login?next=%2Fdashboard%3Ftab%3Dactivity"


def test_require_auth_preserves_existing_login_query_params():
    @require_auth(login_url="/login?source=marketing", redirect_param="next")
    def protected_route(req):
        return "Protected content"

    request = Request(
        {
            "type": "http",
            "method": "GET",
            "path": "/pricing",
            "query_string": b"",
            "headers": [],
            "scheme": "https",
            "server": ("example.com", 443),
            "client": ("127.0.0.1", 1234),
            "session": {},
        }
    )
    response = protected_route(request)

    assert isinstance(response, RedirectResponse)
    assert response.headers["location"] == "/login?source=marketing&next=%2Fpricing"


def test_require_auth_custom_session_key():
    """@require_auth supports custom session key."""

    @require_auth(session_key="custom_user_id")
    def route(req):
        return "Content"

    assert callable(route)
