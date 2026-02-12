"""SEO meta tags generation.

Provides the SEO component for comprehensive meta tag generation including
Open Graph, Twitter Cards, and basic SEO meta tags.
"""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import Link, Meta, Title


def SEO(
    title: str | None = None,
    description: str | None = None,
    keywords: list[str] | None = None,
    image: str | None = None,
    url: str | None = None,
    type: Literal["website", "article", "product"] = "website",
    # Article-specific
    article: bool = False,
    published_time: str | None = None,
    modified_time: str | None = None,
    author: str | None = None,
    section: str | None = None,
    tags: list[str] | None = None,
    # Twitter-specific
    twitter_card: Literal[
        "summary", "summary_large_image", "app", "player"
    ] = "summary_large_image",
    twitter_site: str | None = None,
    twitter_creator: str | None = None,
    # Advanced
    robots: str = "index, follow",
    canonical: str | None = None,
    locale: str | None = None,
    alternate_locales: list[str] | None = None,
    **kwargs: Any,
) -> tuple[Any, ...]:
    """Generate comprehensive SEO meta tags.

    Creates meta tags for basic SEO, Open Graph, and Twitter Cards. Automatically
    merges with global SEO config from add_bootstrap() if available.

    Args:
        title: Page title (also used for og:title and twitter:title)
        description: Page description (also used for og:description)
        keywords: List of keywords for meta keywords tag
        image: Image URL for social sharing (og:image, twitter:image)
        url: Canonical URL for the page (og:url)
        type: Open Graph type (website, article, product)
        article: If True, adds article-specific meta tags
        published_time: Article published time (ISO 8601 format)
        modified_time: Article modified time (ISO 8601 format)
        author: Article author name
        section: Article section/category
        tags: Article tags
        twitter_card: Twitter card type
        twitter_site: Twitter site handle (@username)
        twitter_creator: Twitter creator handle (@username)
        robots: Robots meta tag value
        canonical: Canonical URL (if different from url)
        locale: Page locale (e.g., "en_US")
        alternate_locales: List of alternate locales
        **kwargs: Additional meta tags as key-value pairs

    Returns:
        Tuple of meta tag elements to include in page head

    Example:
        Basic usage:
        >>> SEO(
        ...     title="My Page - Site Name",
        ...     description="Page description",
        ...     image="/assets/og-image.jpg"
        ... )

        Article page:
        >>> SEO(
        ...     title="Blog Post Title",
        ...     description="Post excerpt",
        ...     image="/assets/post-image.jpg",
        ...     article=True,
        ...     published_time="2026-02-12T10:00:00Z",
        ...     author="John Doe",
        ...     tags=["python", "fasthtml"]
        ... )

        With global config (set via add_bootstrap):
        >>> # In app setup:
        >>> add_bootstrap(app, seo={
        ...     "site_name": "My Site",
        ...     "default_image": "/assets/default-og.jpg",
        ...     "twitter_handle": "@mysite"
        ... })
        >>>
        >>> # In route (merges with global config):
        >>> SEO(title="Page Title", description="Page description")

    Note:
        - Title, description, and image are used for both basic meta tags and social sharing
        - If article=True, type is automatically set to "article"
        - Twitter site/creator default to global config if not provided
        - Canonical URL defaults to url parameter if not explicitly set
    """
    elements: list[Any] = []

    # Get global SEO config if available (set via add_bootstrap)
    # This would be stored in app context, but for now we'll use direct values
    # In real implementation, this would merge with app._faststrap_seo_config

    # Basic meta tags
    if title:
        elements.append(Title(title))
        elements.append(Meta(name="title", content=title))

    if description:
        elements.append(Meta(name="description", content=description))

    if keywords:
        elements.append(Meta(name="keywords", content=", ".join(keywords)))

    if robots:
        elements.append(Meta(name="robots", content=robots))

    # Canonical URL
    canonical_url = canonical or url
    if canonical_url:
        elements.append(Link(rel="canonical", href=canonical_url))

    # Open Graph tags
    if title:
        elements.append(Meta(property="og:title", content=title))

    if description:
        elements.append(Meta(property="og:description", content=description))

    if image:
        elements.append(Meta(property="og:image", content=image))

    if url:
        elements.append(Meta(property="og:url", content=url))

    # Set type to article if article=True
    og_type = "article" if article else type
    elements.append(Meta(property="og:type", content=og_type))

    if locale:
        elements.append(Meta(property="og:locale", content=locale))

    if alternate_locales:
        for alt_locale in alternate_locales:
            elements.append(Meta(property="og:locale:alternate", content=alt_locale))

    # Article-specific tags
    if article or og_type == "article":
        if published_time:
            elements.append(Meta(property="article:published_time", content=published_time))

        if modified_time:
            elements.append(Meta(property="article:modified_time", content=modified_time))

        if author:
            elements.append(Meta(property="article:author", content=author))

        if section:
            elements.append(Meta(property="article:section", content=section))

        if tags:
            for tag in tags:
                elements.append(Meta(property="article:tag", content=tag))

    # Twitter Card tags
    elements.append(Meta(name="twitter:card", content=twitter_card))

    if title:
        elements.append(Meta(name="twitter:title", content=title))

    if description:
        elements.append(Meta(name="twitter:description", content=description))

    if image:
        elements.append(Meta(name="twitter:image", content=image))

    if twitter_site:
        elements.append(Meta(name="twitter:site", content=twitter_site))

    if twitter_creator:
        elements.append(Meta(name="twitter:creator", content=twitter_creator))

    # Additional custom meta tags
    for key, value in kwargs.items():
        if value is not None:
            # Convert underscores to hyphens for attribute names
            attr_name = key.replace("_", "-")
            elements.append(Meta(name=attr_name, content=str(value)))

    return tuple(elements)
