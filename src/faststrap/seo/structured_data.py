"""Structured data (JSON-LD) helpers for SEO.

Provides helper methods for generating Schema.org structured data in JSON-LD format.
"""

from __future__ import annotations

import json
from typing import Any

from fasthtml.common import Script

_SCHEMA_DAY_ORDER = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]
_SCHEMA_DAY_MAP = {day.casefold(): day for day in _SCHEMA_DAY_ORDER}
_SCHEMA_DAY_MAP.update(
    {
        "mon": "Monday",
        "tue": "Tuesday",
        "tues": "Tuesday",
        "wed": "Wednesday",
        "thu": "Thursday",
        "thur": "Thursday",
        "thur.": "Thursday",
        "thurs": "Thursday",
        "fri": "Friday",
        "sat": "Saturday",
        "sun": "Sunday",
    }
)


def _schema_day_uri(day: str) -> str:
    return f"https://schema.org/{day}"


def _normalize_day_token(token: str) -> str | None:
    return _SCHEMA_DAY_MAP.get(token.strip().casefold())


def _expand_day_spec(days: str) -> list[str]:
    normalized = days.strip()
    if not normalized:
        return []

    if "," in normalized:
        expanded: list[str] = []
        for part in normalized.split(","):
            expanded.extend(_expand_day_spec(part))
        return expanded

    if "-" in normalized:
        start_raw, end_raw = normalized.split("-", 1)
        start = _normalize_day_token(start_raw)
        end = _normalize_day_token(end_raw)
        if start and end:
            start_idx = _SCHEMA_DAY_ORDER.index(start)
            end_idx = _SCHEMA_DAY_ORDER.index(end)
            if start_idx <= end_idx:
                return _SCHEMA_DAY_ORDER[start_idx : end_idx + 1]
            return _SCHEMA_DAY_ORDER[start_idx:] + _SCHEMA_DAY_ORDER[: end_idx + 1]

    single = _normalize_day_token(normalized)
    return [single] if single else []


class StructuredData:
    """Helper class for generating Schema.org structured data (JSON-LD).

    Provides static methods for common structured data types including
    Article, Product, Breadcrumb, Organization, and LocalBusiness.

    Example:
        Article structured data:
        >>> StructuredData.article(
        ...     headline="My Blog Post",
        ...     description="Post description",
        ...     image="https://example.com/image.jpg",
        ...     author="John Doe",
        ...     published="2026-02-12T10:00:00Z"
        ... )

        Product structured data:
        >>> StructuredData.product(
        ...     name="Amazing Product",
        ...     description="Product description",
        ...     image="https://example.com/product.jpg",
        ...     price="99.99",
        ...     currency="USD",
        ...     rating=4.5,
        ...     review_count=127
        ... )
    """

    @staticmethod
    def article(
        headline: str,
        description: str,
        image: str,
        author: str,
        published: str,
        modified: str | None = None,
        **kwargs: Any,
    ) -> Script:
        """Generate Article structured data (JSON-LD).

        Args:
            headline: Article headline/title
            description: Article description
            image: Article image URL
            author: Author name
            published: Published date (ISO 8601 format)
            modified: Modified date (ISO 8601 format), optional
            **kwargs: Additional Schema.org Article properties

        Returns:
            Script element with JSON-LD structured data

        Example:
            >>> StructuredData.article(
            ...     headline="10 Tips for Better Python Code",
            ...     description="Learn how to write cleaner Python",
            ...     image="https://example.com/python-tips.jpg",
            ...     author="Jane Smith",
            ...     published="2026-02-12T10:00:00Z",
            ...     modified="2026-02-12T14:30:00Z"
            ... )
        """
        data = {
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": headline,
            "description": description,
            "image": image,
            "author": {"@type": "Person", "name": author},
            "datePublished": published,
        }

        if modified:
            data["dateModified"] = modified

        # Add any additional properties
        data.update(kwargs)

        return Script(
            json.dumps(data, indent=2),
            type="application/ld+json",
        )

    @staticmethod
    def product(
        name: str,
        description: str,
        image: str,
        price: str,
        currency: str = "USD",
        rating: float | None = None,
        review_count: int | None = None,
        availability: str = "InStock",
        **kwargs: Any,
    ) -> Script:
        """Generate Product structured data (JSON-LD).

        Args:
            name: Product name
            description: Product description
            image: Product image URL
            price: Product price (as string)
            currency: Currency code (default: "USD")
            rating: Average rating (0-5)
            review_count: Number of reviews
            availability: Availability status (InStock, OutOfStock, PreOrder)
            **kwargs: Additional Schema.org Product properties

        Returns:
            Script element with JSON-LD structured data

        Example:
            >>> StructuredData.product(
            ...     name="Wireless Headphones",
            ...     description="Premium noise-cancelling headphones",
            ...     image="https://example.com/headphones.jpg",
            ...     price="199.99",
            ...     currency="USD",
            ...     rating=4.5,
            ...     review_count=342,
            ...     availability="InStock"
            ... )
        """
        data: dict[str, Any] = {
            "@context": "https://schema.org",
            "@type": "Product",
            "name": name,
            "description": description,
            "image": image,
            "offers": {
                "@type": "Offer",
                "price": price,
                "priceCurrency": currency,
                "availability": f"https://schema.org/{availability}",
            },
        }

        if rating is not None and review_count is not None:
            data["aggregateRating"] = {
                "@type": "AggregateRating",
                "ratingValue": rating,
                "reviewCount": review_count,
            }

        # Add any additional properties
        data.update(kwargs)

        return Script(
            json.dumps(data, indent=2),
            type="application/ld+json",
        )

    @staticmethod
    def breadcrumb(items: list[tuple[str, str]]) -> Script:
        """Generate BreadcrumbList structured data (JSON-LD).

        Args:
            items: List of (name, url) tuples representing breadcrumb items

        Returns:
            Script element with JSON-LD structured data

        Example:
            >>> StructuredData.breadcrumb([
            ...     ("Home", "https://example.com/"),
            ...     ("Products", "https://example.com/products"),
            ...     ("Laptops", "https://example.com/products/laptops")
            ... ])
        """
        list_items = [
            {
                "@type": "ListItem",
                "position": i + 1,
                "name": name,
                "item": url,
            }
            for i, (name, url) in enumerate(items)
        ]

        data = {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": list_items,
        }

        return Script(
            json.dumps(data, indent=2),
            type="application/ld+json",
        )

    @staticmethod
    def organization(
        name: str,
        url: str,
        logo: str,
        social_links: list[str] | None = None,
        **kwargs: Any,
    ) -> Script:
        """Generate Organization structured data (JSON-LD).

        Args:
            name: Organization name
            url: Organization website URL
            logo: Organization logo URL
            social_links: List of social media profile URLs
            **kwargs: Additional Schema.org Organization properties

        Returns:
            Script element with JSON-LD structured data

        Example:
            >>> StructuredData.organization(
            ...     name="Acme Corp",
            ...     url="https://acme.com",
            ...     logo="https://acme.com/logo.png",
            ...     social_links=[
            ...         "https://twitter.com/acmecorp",
            ...         "https://linkedin.com/company/acmecorp"
            ...     ]
            ... )
        """
        data: dict[str, Any] = {
            "@context": "https://schema.org",
            "@type": "Organization",
            "name": name,
            "url": url,
            "logo": logo,
        }

        if social_links:
            data["sameAs"] = social_links

        # Add any additional properties
        data.update(kwargs)

        return Script(
            json.dumps(data, indent=2),
            type="application/ld+json",
        )

    @staticmethod
    def local_business(
        name: str,
        address: dict[str, str],
        phone: str,
        hours: dict[str, str] | None = None,
        **kwargs: Any,
    ) -> Script:
        """Generate LocalBusiness structured data (JSON-LD).

        Args:
            name: Business name
            address: Address dict with keys: street, city, state, zip, country
            phone: Phone number
            hours: Opening hours dict (day: hours), e.g., {"Monday": "9:00-17:00"}
            **kwargs: Additional Schema.org LocalBusiness properties

        Returns:
            Script element with JSON-LD structured data

        Example:
            >>> StructuredData.local_business(
            ...     name="Joe's Coffee Shop",
            ...     address={
            ...         "street": "123 Main St",
            ...         "city": "Springfield",
            ...         "state": "IL",
            ...         "zip": "62701",
            ...         "country": "US"
            ...     },
            ...     phone="+1-555-123-4567",
            ...     hours={"Monday-Friday": "7:00-19:00", "Saturday-Sunday": "8:00-17:00"}
            ... )
        """
        data: dict[str, Any] = {
            "@context": "https://schema.org",
            "@type": "LocalBusiness",
            "name": name,
            "address": {
                "@type": "PostalAddress",
                "streetAddress": address.get("street", ""),
                "addressLocality": address.get("city", ""),
                "addressRegion": address.get("state", ""),
                "postalCode": address.get("zip", ""),
                "addressCountry": address.get("country", ""),
            },
            "telephone": phone,
        }

        if hours:
            # Convert hours dict to OpeningHoursSpecification
            opening_hours = []
            for days, time_range in hours.items():
                normalized_days = _expand_day_spec(days)
                day_of_week: str | list[str]
                if normalized_days:
                    day_of_week = [_schema_day_uri(day) for day in normalized_days]
                    if len(day_of_week) == 1:
                        day_of_week = day_of_week[0]
                else:
                    day_of_week = days

                opening_hours.append(
                    {
                        "@type": "OpeningHoursSpecification",
                        "dayOfWeek": day_of_week,
                        "opens": time_range.split("-")[0] if "-" in time_range else time_range,
                        "closes": time_range.split("-")[1] if "-" in time_range else time_range,
                    }
                )
            data["openingHoursSpecification"] = opening_hours

        # Add any additional properties
        data.update(kwargs)

        return Script(
            json.dumps(data, indent=2),
            type="application/ld+json",
        )
