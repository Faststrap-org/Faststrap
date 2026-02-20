# tests/conftest.py
"""Pytest configuration and fixtures."""

import sys
from pathlib import Path

import pytest
from fasthtml.common import FastHTML, to_xml

# Ensure tests import local src/ package, not an older site-packages install.
SRC_PATH = Path(__file__).resolve().parents[1] / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))


@pytest.fixture
def app():
    """Create a test FastHTML app with FastStrap."""
    from faststrap import add_bootstrap

    app = FastHTML()
    add_bootstrap(app, use_cdn=True)  # Use CDN for tests
    return app


@pytest.fixture
def render():
    """Helper to render FastHTML objects to string."""
    return to_xml


@pytest.fixture
def render_pretty():
    """Helper to render with indentation for debugging."""

    def _render_pretty(obj):
        import xml.dom.minidom as minidom

        xml_str = to_xml(obj)
        try:
            dom = minidom.parseString(f"<root>{xml_str}</root>")
            return dom.toprettyxml(indent="  ")
        except Exception:
            return xml_str  # Return raw if parsing fails

    return _render_pretty


# Helper to check if Bootstrap JS components work
@pytest.fixture
def bootstrap_js_available():
    """Check if Bootstrap JS is available (for integration tests)."""
    return True  # Set to False to skip JS-dependent tests
