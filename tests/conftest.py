"""Pytest configuration and fixtures."""

import pytest
from fasthtml.common import FastHTML


@pytest.fixture
def app():
    """Create a test FastHTML app."""
    return FastHTML()


@pytest.fixture
def render():
    """Helper to render FastHTML objects to string."""

    def _render(obj):
        return str(obj)

    return _render
