"""Tests for assets module including mount_assets helper."""

import os
import pytest
from pathlib import Path
from fasthtml.common import FastHTML
from faststrap import mount_assets
from starlette.routing import Mount


def test_mount_assets_basic(tmp_path):
    """Test basic mount_assets functionality."""
    # Create test directory with a file
    assets_dir = tmp_path / "assets"
    assets_dir.mkdir()
    (assets_dir / "test.txt").write_text("test content")

    app = FastHTML()
    mount_assets(app, str(assets_dir), url_path="/assets")

    # Verify mount exists
    assert any(isinstance(route, Mount) and route.path == "/assets" for route in app.routes)


def test_mount_assets_custom_url_path(tmp_path):
    """Test mount_assets with custom URL path."""
    assets_dir = tmp_path / "images"
    assets_dir.mkdir()

    app = FastHTML()
    mount_assets(app, str(assets_dir), url_path="/img")

    # Verify mount at custom path
    assert any(isinstance(route, Mount) and route.path == "/img" for route in app.routes)


def test_mount_assets_custom_name(tmp_path):
    """Test mount_assets with custom name."""
    assets_dir = tmp_path / "assets"
    assets_dir.mkdir()

    app = FastHTML()
    mount_assets(app, str(assets_dir), url_path="/assets", name="custom_assets")

    # Verify mount with custom name
    mount_route = next(
        (route for route in app.routes if isinstance(route, Mount) and route.path == "/assets"),
        None,
    )
    assert mount_route is not None
    assert mount_route.name == "custom_assets"


def test_mount_assets_priority(tmp_path):
    """Test mount_assets priority parameter."""
    assets_dir = tmp_path / "assets"
    assets_dir.mkdir()

    app = FastHTML()

    # Add a route first
    @app.get("/test")
    def test_route():
        return "test"

    # Mount with priority=True (should be first)
    mount_assets(app, str(assets_dir), url_path="/assets", priority=True)

    # Verify mount is at the beginning
    assert isinstance(app.routes[0], Mount)
    assert app.routes[0].path == "/assets"


def test_mount_assets_no_priority(tmp_path):
    """Test mount_assets with priority=False."""
    assets_dir = tmp_path / "assets"
    assets_dir.mkdir()

    app = FastHTML()

    # Add a route first
    @app.get("/test")
    def test_route():
        return "test"

    initial_route_count = len(app.routes)

    # Mount with priority=False (should be last)
    mount_assets(app, str(assets_dir), url_path="/assets", priority=False)

    # Verify mount is at the end
    assert isinstance(app.routes[-1], Mount)
    assert app.routes[-1].path == "/assets"


def test_mount_assets_invalid_url_path(tmp_path):
    """Test mount_assets with invalid URL path."""
    assets_dir = tmp_path / "assets"
    assets_dir.mkdir()

    app = FastHTML()

    # Should raise ValueError for URL path not starting with /
    with pytest.raises(ValueError, match="url_path must start with"):
        mount_assets(app, str(assets_dir), url_path="assets")


def test_mount_assets_nonexistent_directory():
    """Test mount_assets with non-existent directory."""
    app = FastHTML()

    # Should raise FileNotFoundError
    with pytest.raises(FileNotFoundError, match="Static directory not found"):
        mount_assets(app, "/nonexistent/directory")


def test_mount_assets_file_not_directory(tmp_path):
    """Test mount_assets with a file instead of directory."""
    # Create a file instead of directory
    test_file = tmp_path / "test.txt"
    test_file.write_text("test")

    app = FastHTML()

    # Should raise ValueError
    with pytest.raises(ValueError, match="not a directory"):
        mount_assets(app, str(test_file))


def test_mount_assets_auto_name_generation(tmp_path):
    """Test automatic name generation from URL path."""
    assets_dir = tmp_path / "assets"
    assets_dir.mkdir()

    app = FastHTML()

    # Test various URL paths
    test_cases = [
        ("/assets", "assets"),
        ("/my-files", "my_files"),
        ("/img/uploads", "img_uploads"),
    ]

    for url_path, expected_name in test_cases:
        app_test = FastHTML()
        mount_assets(app_test, str(assets_dir), url_path=url_path)

        mount_route = next(
            (
                route
                for route in app_test.routes
                if isinstance(route, Mount) and route.path == url_path
            ),
            None,
        )
        assert mount_route is not None
        assert mount_route.name == expected_name


def test_mount_assets_multiple_directories(tmp_path):
    """Test mounting multiple directories."""
    # Create multiple directories
    assets_dir = tmp_path / "assets"
    images_dir = tmp_path / "images"
    uploads_dir = tmp_path / "uploads"

    assets_dir.mkdir()
    images_dir.mkdir()
    uploads_dir.mkdir()

    app = FastHTML()

    # Mount all directories
    mount_assets(app, str(assets_dir), url_path="/assets")
    mount_assets(app, str(images_dir), url_path="/img")
    mount_assets(app, str(uploads_dir), url_path="/uploads")

    # Verify all mounts exist
    mount_paths = [route.path for route in app.routes if isinstance(route, Mount)]
    assert "/assets" in mount_paths
    assert "/img" in mount_paths
    assert "/uploads" in mount_paths
