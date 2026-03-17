"""Safe Markdown rendering component with optional dependencies."""

from __future__ import annotations

import importlib
from typing import Any, cast

from fasthtml.common import Div, NotStr

from ...core.base import merge_classes
from ...core.registry import register
from ...utils.attrs import convert_attrs

DEFAULT_ALLOWED_TAGS = [
    "p",
    "br",
    "pre",
    "code",
    "blockquote",
    "ul",
    "ol",
    "li",
    "strong",
    "em",
    "a",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
    "hr",
    "table",
    "thead",
    "tbody",
    "tr",
    "th",
    "td",
]

DEFAULT_ALLOWED_ATTRIBUTES: dict[str, list[str]] = {
    "a": ["href", "title", "target", "rel"],
    "code": ["class"],
    "th": ["align"],
    "td": ["align"],
}

DEFAULT_ALLOWED_PROTOCOLS = ["http", "https", "mailto"]


def _load_markdown_module() -> Any:
    try:
        return importlib.import_module("markdown")
    except ImportError as exc:
        msg = "Markdown rendering requires `markdown`. Install with `pip install faststrap[markdown]`."
        raise ImportError(msg) from exc


def _load_bleach_module() -> Any:
    try:
        return importlib.import_module("bleach")
    except ImportError as exc:
        msg = (
            "Sanitized markdown rendering requires `bleach`. "
            "Install with `pip install faststrap[markdown]`."
        )
        raise ImportError(msg) from exc


def render_markdown(
    text: str,
    *,
    sanitize: bool = True,
    extensions: list[str] | None = None,
    allowed_tags: list[str] | None = None,
    allowed_attributes: dict[str, list[str]] | None = None,
    allowed_protocols: list[str] | None = None,
) -> str:
    """Render markdown text into HTML with optional sanitization."""
    markdown_module = _load_markdown_module()
    html = cast(
        str,
        markdown_module.markdown(
            text,
            extensions=extensions or ["extra", "sane_lists", "tables", "fenced_code"],
        ),
    )

    if not sanitize:
        return html

    bleach_module = _load_bleach_module()
    return cast(
        str,
        bleach_module.clean(
            html,
            tags=allowed_tags or DEFAULT_ALLOWED_TAGS,
            attributes=allowed_attributes or DEFAULT_ALLOWED_ATTRIBUTES,
            protocols=allowed_protocols or DEFAULT_ALLOWED_PROTOCOLS,
            strip=True,
        ),
    )


@register(category="display")
def Markdown(
    text: str,
    *,
    sanitize: bool = True,
    extensions: list[str] | None = None,
    allowed_tags: list[str] | None = None,
    allowed_attributes: dict[str, list[str]] | None = None,
    allowed_protocols: list[str] | None = None,
    **kwargs: Any,
) -> Div:
    """Render markdown into a styled container.

    This component is optional and requires extra dependencies:
    `pip install faststrap[markdown]`
    """
    html = render_markdown(
        text,
        sanitize=sanitize,
        extensions=extensions,
        allowed_tags=allowed_tags,
        allowed_attributes=allowed_attributes,
        allowed_protocols=allowed_protocols,
    )

    user_cls = kwargs.pop("cls", "")
    attrs: dict[str, Any] = {
        "cls": merge_classes("faststrap-markdown", user_cls),
    }
    attrs.update(convert_attrs(kwargs))
    return Div(NotStr(html), **attrs)
