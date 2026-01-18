"""Tests for PWA module."""

from fasthtml.common import FastHTML, Link, Meta, Script

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
    assert any(
        h.tag == "script" and "navigator.serviceWorker.register" in str(h) for h in app.hdrs
    )

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
