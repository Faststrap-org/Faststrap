"""Static-asset contract tests for Faststrap's JS/CSS runtime hooks.

Faststrap wires many component behaviors through data attributes consumed by
`modern-toast.js` and classes/keframes in its static CSS. These static checks
guard against the attribute-emitted-by-Python but never-consumed-in-assets
drift that browser-level bugs cause, without needing a browser.
"""

from pathlib import Path

SRC = Path(__file__).resolve().parent.parent / "src" / "faststrap" / "static"

MODERN_TOAST_JS = (SRC / "js" / "modern-toast.js").read_text(encoding="utf-8")
TOAST_CSS = (SRC / "css" / "faststrap-toast.css").read_text(encoding="utf-8")
VISUAL_CSS = (SRC / "css" / "faststrap-visual.css").read_text(encoding="utf-8")
INIT_JS = (SRC / "js" / "faststrap-init.js").read_text(encoding="utf-8")


# ── modern-toast.js ───────────────────────────────────────────────────────


def test_modern_toast_js_reads_stack_queue_data():
    # max_visible queue feature is actually consumed, not dead.
    assert "fsMaxVisible" in MODERN_TOAST_JS
    assert "enqueueToast" in MODERN_TOAST_JS
    assert "dequeueNext" in MODERN_TOAST_JS
    assert "faststrap-modern-toast-queued" in MODERN_TOAST_JS
    assert "faststrap-modern-toast-queued" in TOAST_CSS  # display:none exists


def test_modern_toast_js_keyboard_and_swipe_supported():
    assert "Escape" in MODERN_TOAST_JS
    assert "touchstart" in MODERN_TOAST_JS


def test_modern_toast_js_htmx_rescope():
    assert "htmx:afterSwap" in MODERN_TOAST_JS


# ── faststrap-toast.css animation variants ────────────────────────────────


def test_animation_variants_have_css_hooks():
    for variant in ("fade", "zoom", "none"):
        assert f'data-fs-animation="{variant}"' in TOAST_CSS
    assert "faststrap-modern-toast-fade-in" in TOAST_CSS
    assert "faststrap-modern-toast-zoom-in" in TOAST_CSS


def test_loading_intent_spinner_hook():
    assert 'data-fs-intent="loading"' in TOAST_CSS


def test_reduced_motion_guard_present():
    assert "prefers-reduced-motion" in TOAST_CSS


# ── faststrap-visual.css ──────────────────────────────────────────────────


def test_gradient_hover_none_suppressed_in_css():
    assert ".faststrap-gradient-button:not(.hover-none):hover" in VISUAL_CSS
    assert ".faststrap-gradient-button:not(.hover-none):focus" in VISUAL_CSS
    # hover="none" must also neutralize the global .btn:hover lift from core assets
    assert ".faststrap-gradient-button.hover-none:hover:not(:disabled)" in VISUAL_CSS
    assert ".faststrap-gradient-button.hover-none:focus" in VISUAL_CSS
    assert ".faststrap-gradient-button.hover-none:active:not(:disabled)" in VISUAL_CSS


def test_fab_css_hooks_present():
    assert "--fs-fab-size" in VISUAL_CSS
    assert "--fs-fab-inset" in VISUAL_CSS
    assert "fab-pill" in VISUAL_CSS


# ── faststrap-init.js ─────────────────────────────────────────────────────


def test_init_js_initializes_bootstrap_toasts():
    assert "gradient_button" not in INIT_JS
    assert ".toast" in INIT_JS
    assert "bootstrap.Toast" in INIT_JS
