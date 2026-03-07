"""Tests for CDN asset composition and add_bootstrap behavior."""

from fasthtml.common import FastHTML

from faststrap.core.assets import (
    BOOTSTRAP_CSS_URL,
    BOOTSTRAP_ICONS_URL,
    BOOTSTRAP_JS_URL,
    _build_cdn_assets,
    add_bootstrap,
    get_assets,
)


def _hdrs_to_text(app: FastHTML) -> str:
    return "\n".join(str(h) for h in app.hdrs)


def test_build_cdn_assets_includes_expected_files_in_order():
    assets = _build_cdn_assets("0.5.8", include_favicon=True, include_js=True)
    rendered = [str(a) for a in assets]

    assert BOOTSTRAP_CSS_URL in rendered[0]
    assert BOOTSTRAP_ICONS_URL in rendered[1]
    assert "/css/faststrap-fx.css" in rendered[2]
    assert "/css/faststrap-layouts.css" in rendered[3]
    assert BOOTSTRAP_JS_URL in rendered[4]
    assert "/favicon.svg" in rendered[5]


def test_build_cdn_assets_excludes_js_when_disabled():
    assets = _build_cdn_assets("0.5.8", include_favicon=False, include_js=False)
    rendered = "\n".join(str(a) for a in assets)
    assert BOOTSTRAP_JS_URL not in rendered


def test_build_cdn_assets_excludes_favicon_when_disabled():
    assets = _build_cdn_assets("0.5.8", include_favicon=False, include_js=True)
    rendered = "\n".join(str(a) for a in assets)
    assert "/favicon.svg" not in rendered


def test_build_cdn_assets_uses_main_branch_ref_without_v_prefix():
    assets = _build_cdn_assets("main", include_favicon=True, include_js=False)
    rendered = "\n".join(str(a) for a in assets)
    assert "@main/src/faststrap/static" in rendered
    assert "@vmain/" not in rendered


def test_get_assets_cdn_includes_faststrap_css():
    assets = get_assets(use_cdn=True)
    rendered = "\n".join(str(a) for a in assets)
    assert "/css/faststrap-fx.css" in rendered
    assert "/css/faststrap-layouts.css" in rendered


def test_add_bootstrap_use_cdn_does_not_mount_static_routes():
    app = FastHTML()
    add_bootstrap(app, use_cdn=True)
    assert not hasattr(app, "_faststrap_static_url")
    assert not any(getattr(route, "name", "") == "faststrap_static" for route in app.routes)


def test_add_bootstrap_duplicate_call_raises():
    app = FastHTML()
    add_bootstrap(app, use_cdn=True)
    try:
        add_bootstrap(app, use_cdn=True)
        raise AssertionError("Expected duplicate add_bootstrap() guard")
    except RuntimeError as exc:
        assert "already been called" in str(exc)


def test_add_bootstrap_sets_guard_only_after_success(monkeypatch):
    app = FastHTML()

    def _boom(*args, **kwargs):  # type: ignore[no-untyped-def]
        raise RuntimeError("boom")

    monkeypatch.setattr("faststrap.core.assets.get_assets", _boom)

    try:
        add_bootstrap(app, use_cdn=True)
        raise AssertionError("Expected RuntimeError")
    except RuntimeError as exc:
        assert "boom" in str(exc)

    # Retry should not be blocked by duplicate-call guard.
    monkeypatch.setattr("faststrap.core.assets.get_assets", get_assets)
    add_bootstrap(app, use_cdn=True)
    assert BOOTSTRAP_CSS_URL in _hdrs_to_text(app)


def test_add_bootstrap_components_none_includes_js():
    app = FastHTML()
    add_bootstrap(app, use_cdn=True, components=None)
    assert BOOTSTRAP_JS_URL in _hdrs_to_text(app)


def test_add_bootstrap_components_empty_omits_js():
    app = FastHTML()
    add_bootstrap(app, use_cdn=True, components=[])
    assert BOOTSTRAP_JS_URL not in _hdrs_to_text(app)


def test_add_bootstrap_components_with_metadata_requires_js_includes_js():
    app = FastHTML()

    def modal_like() -> None:
        return None

    modal_like.__faststrap_metadata__ = {"requires_js": True}
    add_bootstrap(app, use_cdn=True, components=[modal_like])
    assert BOOTSTRAP_JS_URL in _hdrs_to_text(app)


def test_add_bootstrap_components_without_metadata_omits_js():
    app = FastHTML()

    def plain_component() -> None:
        return None

    add_bootstrap(app, use_cdn=True, components=[plain_component])
    assert BOOTSTRAP_JS_URL not in _hdrs_to_text(app)


def test_add_bootstrap_cdn_default_favicon_is_version_pinned():
    app = FastHTML()
    add_bootstrap(app, use_cdn=True, include_favicon=True)
    text = _hdrs_to_text(app)
    assert "cdn.jsdelivr.net/gh/Faststrap-org/Faststrap@v" in text
    assert "/src/faststrap/static/favicon.svg" in text


def test_add_bootstrap_cdn_custom_favicon_overrides_default():
    app = FastHTML()
    add_bootstrap(
        app, use_cdn=True, include_favicon=True, favicon_url="https://example.com/fav.svg"
    )
    text = _hdrs_to_text(app)
    assert "https://example.com/fav.svg" in text
    assert "/src/faststrap/static/favicon.svg" not in text
