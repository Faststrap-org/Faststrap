"""Tests for PWA module."""

from fasthtml.common import FastHTML
from starlette.testclient import TestClient

from faststrap.pwa import PwaMeta, add_pwa


def test_pwa_meta_generation():
    """Test PwaMeta component generates correct tags."""
    tags = PwaMeta(name="Test App", theme_color="#000000", icon_path="/icon.png")

    # Check for essential tags
    assert any(
        t.tag == "meta"
        and t.attrs.get("name") == "theme-color"
        and t.attrs.get("content") == "#000000"
        for t in tags
    )
    assert any(t.tag == "link" and t.attrs.get("rel") == "manifest" for t in tags)
    assert any(t.tag == "link" and t.attrs.get("rel") == "apple-touch-icon" for t in tags)


def test_add_pwa_injection():
    """Test add_pwa injects headers and routes."""
    app = FastHTML()

    add_pwa(app, name="My PWA", service_worker=True, offline_page=True)

    # Check headers injected
    assert len(app.hdrs) > 0
    # Check for service worker registration script
    assert any(h.tag == "script" and "navigator.serviceWorker.register" in str(h) for h in app.hdrs)

    # Check routes added
    route_paths = [r.path for r in app.routes]
    assert "/manifest.json" in route_paths
    assert "/sw.js" in route_paths
    assert "/offline" in route_paths


def test_add_pwa_no_sw():
    """Test add_pwa with service_worker=False."""
    app = FastHTML()

    add_pwa(app, service_worker=False)

    route_paths = [r.path for r in app.routes]
    assert "/manifest.json" in route_paths
    assert "/sw.js" not in route_paths


def test_manifest_route_returns_json():
    """Manifest route should return JSON payload directly."""
    app = FastHTML()
    add_pwa(app, name="My PWA")

    client = TestClient(app)
    response = client.get("/manifest.json")

    assert response.status_code == 200
    assert response.headers["content-type"].startswith("application/json")
    payload = response.json()
    assert payload["name"] == "My PWA"
    assert payload["start_url"] == "/"


def test_service_worker_route_returns_javascript():
    """Service worker route should return JS file without response double-wrapping."""
    app = FastHTML()
    add_pwa(app, service_worker=True)

    client = TestClient(app)
    response = client.get("/sw.js")

    assert response.status_code == 200
    assert "application/javascript" in response.headers["content-type"]
    assert "self.addEventListener" in response.text


def test_service_worker_uses_hardened_precache_and_runtime_caching():
    """Default service worker should be resilient and include runtime caching strategies."""
    app = FastHTML()
    add_pwa(app, service_worker=True)

    client = TestClient(app)
    response = client.get("/sw.js")

    assert response.status_code == 200
    sw = response.text
    assert "Promise.allSettled(PRECACHE_URLS.map((url) => cache.add(url)))" in sw
    assert "cache.put(request, response.clone())" in sw
    assert 'if (event.request.mode === "navigate")' in sw
    assert "staleWhileRevalidate(event.request)" in sw


def test_service_worker_accepts_cache_and_precache_configuration():
    """Service worker should reflect optional cache naming and additional precache URLs."""
    app = FastHTML()
    add_pwa(
        app,
        service_worker=True,
        cache_name="myapp-cache",
        cache_version="v2026-02-23",
        pre_cache_urls=("/health", "/assets/logo.png"),
    )

    client = TestClient(app)
    response = client.get("/sw.js")

    assert response.status_code == 200
    sw = response.text
    assert 'const CACHE_NAME = "myapp-cache-v2026-02-23";' in sw
    assert '"/health"' in sw
    assert '"/assets/logo.png"' in sw
