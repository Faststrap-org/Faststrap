"""Unified page head composer for SEO + PWA metadata."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import Link, Meta, Title

from ..pwa.core import PwaMeta
from ..utils.static_management import create_favicon_links
from .meta import SEO


def _head_key(node: Any) -> tuple[str, str]:
    tag = getattr(node, "tag", "")
    attrs = getattr(node, "attrs", {}) or {}

    if tag == "title":
        return ("title", "title")
    if tag == "meta":
        if "name" in attrs:
            return ("meta:name", str(attrs["name"]).lower())
        if "property" in attrs:
            return ("meta:property", str(attrs["property"]).lower())
    if tag == "link":
        rel = str(attrs.get("rel", "")).lower()
        href = str(attrs.get("href", ""))
        if rel in {"canonical", "manifest", "icon", "shortcut icon", "apple-touch-icon"}:
            return (f"link:{rel}", href)
    return (tag, repr(attrs))


def _dedupe(elements: list[Any]) -> tuple[Any, ...]:
    seen: dict[tuple[str, str], Any] = {}
    order: list[tuple[str, str]] = []

    for element in elements:
        key = _head_key(element)
        if key not in seen:
            order.append(key)
        seen[key] = element

    return tuple(seen[key] for key in order)


def PageMeta(
    title: str | None = None,
    description: str | None = None,
    keywords: list[str] | None = None,
    image: str | None = None,
    url: str | None = None,
    canonical: str | None = None,
    type: Literal["website", "article", "product"] = "website",
    robots: str = "index, follow",
    twitter_site: str | None = None,
    twitter_creator: str | None = None,
    locale: str | None = None,
    include_pwa: bool = False,
    pwa_name: str | None = None,
    pwa_short_name: str | None = None,
    pwa_theme_color: str = "#ffffff",
    pwa_background_color: str = "#ffffff",
    favicon_url: str | None = None,
    extra_meta: dict[str, Any] | None = None,
) -> tuple[Any, ...]:
    """Compose page metadata with deduplication guarantees."""
    elements: list[Any] = []

    if title is not None:
        elements.append(Title(title))
    elements.extend(
        SEO(
            title=title,
            description=description,
            keywords=keywords,
            image=image,
            url=url,
            canonical=canonical,
            type=type,
            robots=robots,
            twitter_site=twitter_site,
            twitter_creator=twitter_creator,
            locale=locale,
        )
    )

    if include_pwa:
        elements.extend(
            PwaMeta(
                name=pwa_name or title or "Faststrap App",
                short_name=pwa_short_name or pwa_name or "Faststrap",
                description=description,
                theme_color=pwa_theme_color,
                background_color=pwa_background_color,
            )
        )

    if favicon_url:
        elements.extend(create_favicon_links(favicon_url))

    if extra_meta:
        for key, value in extra_meta.items():
            if value is None:
                continue
            attr = key.replace("_", "-")
            elements.append(Meta(name=attr, content=str(value)))

    elements.append(Link(rel="canonical", href=canonical or url or ""))

    cleaned: list[Any] = []
    for element in elements:
        attrs = getattr(element, "attrs", {}) or {}
        if (
            getattr(element, "tag", "") == "link"
            and str(attrs.get("rel", "")).lower() == "canonical"
            and attrs.get("href", "") == ""
        ):
            continue
        cleaned.append(element)
    return _dedupe(cleaned)
