"""Static site export for FastHTML + Faststrap applications."""

from __future__ import annotations

import re
import shutil
from pathlib import Path
from typing import Any
from urllib.parse import urljoin, urlparse

from starlette.testclient import TestClient


def _collect_static_files(app: Any, static_url: str = "/static") -> dict[str, Path]:
    """Collect static files from the Faststrap package and mounted directories."""
    static_files: dict[str, Path] = {}

    # Faststrap package static files
    try:
        from importlib.resources import as_file, files
        from faststrap import static as faststrap_static_pkg

        static_traversable = files("faststrap").joinpath("static")
        with as_file(static_traversable) as static_path:
            for file_path in static_path.rglob("*"):
                if file_path.is_file():
                    rel = file_path.relative_to(static_path)
                    static_files[f"{static_url}/{rel.as_posix()}"] = file_path
    except Exception:
        pass

    # Mounted static directories
    for route in getattr(app, "routes", []):
        if type(route).__name__ == "Mount":
            mount_path = getattr(route, "path", "")
            if mount_path == static_url:
                continue
            if hasattr(route, "app") and hasattr(route.app, "directory"):
                directory = Path(route.app.directory)
                if directory.exists():
                    for file_path in directory.rglob("*"):
                        if file_path.is_file():
                            rel = file_path.relative_to(directory)
                            url = f"{mount_path}/{rel.as_posix()}"
                            static_files[url] = file_path

    return static_files


def _rewrite_urls(html: str, base_path: str, static_url: str = "/static") -> str:
    """Rewrite absolute URLs to relative paths for static hosting.

    Args:
        html: Rendered HTML string
        base_path: Relative path from output root to the current page
        static_url: The static URL path to rewrite

    Returns:
        HTML with rewritten relative URLs
    """
    parsed = urlparse(base_path)
    depth = len(parsed.path.strip("/").split("/")) if parsed.path.strip("/") else 0

    def _rewrite_attr(match: re.Match) -> str:
        attr = match.group(1)
        url = match.group(2)
        if url.startswith(static_url):
            rel_depth = "../" * depth if depth > 0 else "./"
            new_url = f"{rel_depth}{url.lstrip('/')}"
            return f'{attr}="{new_url}"'
        if url.startswith("http://") or url.startswith("https://"):
            return match.group(0)
        if url.startswith("/") and not url.startswith("//"):
            rel_depth = "../" * depth if depth > 0 else "./"
            new_url = f"{rel_depth}{url.lstrip('/')}"
            return f'{attr}="{new_url}"'
        return match.group(0)

    html = re.sub(r'(href|src)="(/[^"]+)"', _rewrite_attr, html)
    return html


def _get_route_path(route: Any) -> tuple[str, str]:
    """Get the path and HTTP methods for a route.

    Returns:
        Tuple of (path, methods_string)
    """
    path = getattr(route, "path", None) or getattr(route, "path_format", "")
    methods = getattr(route, "methods", None)
    if methods:
        return path, ",".join(sorted(methods))
    return path, "GET,HEAD"


def export_static(
    app: Any,
    output_dir: str | Path = "dist",
    *,
    static_url: str = "/static",
    base_url: str = "",
    exclude_paths: list[str] | None = None,
    include_js: bool = True,
) -> Path:
    """Export a FastHTML + Faststrap app as static HTML/CSS/JS files.

    Args:
        app: FastHTML application instance
        output_dir: Output directory for static files
        static_url: The static URL path used by Faststrap
        base_url: Base URL for the site (used for canonical URLs)
        exclude_paths: List of path patterns to exclude from export
        include_js: Whether to include JavaScript assets

    Returns:
        Path to the output directory

    Raises:
        RuntimeError: If no GET routes are found
    """
    output_dir = Path(output_dir).resolve()
    exclude_paths = exclude_paths or []

    # Discover GET routes
    routes_to_export: list[tuple[str, Any]] = []
    for route in getattr(app, "routes", []):
        path, methods = _get_route_path(route)
        if "GET" not in methods or path == static_url:
            continue
        if any(path.startswith(ex) for ex in exclude_paths):
            continue
        routes_to_export.append((path, route))

    if not routes_to_export:
        raise RuntimeError("No GET routes found to export.")

    # Collect static files
    static_files = _collect_static_files(app, static_url)

    # Export static assets
    assets_dir = output_dir / static_url.lstrip("/")
    assets_dir.mkdir(parents=True, exist_ok=True)

    exported_assets: set[str] = set()
    for url, source in static_files.items():
        if not include_js and url.endswith(".js"):
            continue
        rel = url[len(static_url):]
        dest = assets_dir / rel.lstrip("/")
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, dest)
        exported_assets.add(url)

    # Render and export HTML pages
    client = TestClient(app)

    pages = 0
    for path, route in routes_to_export:
        response = client.get(path, follow_redirects=True)
        if response.status_code >= 400:
            continue

        html = response.text

        # Rewrite URLs
        if path == "/" or path == "":
            rel_path = ""
        else:
            rel_path = path.rstrip("/") + "/"

        html = _rewrite_urls(html, rel_path, static_url)

        # Write HTML file
        if path == "/" or path == "":
            dest = output_dir / "index.html"
        else:
            clean_path = path.strip("/")
            dest = output_dir / clean_path / "index.html"

        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(html, encoding="utf-8")
        pages += 1

    return output_dir, pages, len(exported_assets)
