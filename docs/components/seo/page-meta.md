# PageMeta

`PageMeta` is a higher-level head composer that combines SEO tags, canonical URL handling, optional PWA tags, and optional favicon links in one call.

It is designed for teams that want a single, predictable entry point for page head metadata without repeating multiple helpers.

## Import

```python
from faststrap import PageMeta
```

## What problem it solves

- Prevents accidental duplicate/conflicting tags in route-level code.
- Reduces repetitive `SEO(...) + PwaMeta(...) + favicon links` assembly.
- Makes head management easier for new contributors.

## Basic usage (SEO + canonical)

```python
PageMeta(
    title="Faststrap Docs",
    description="Build modern UI in Python",
    canonical="https://faststrap.dev/docs",
    image="https://faststrap.dev/og/docs.png",
)
```

## Include PWA tags

```python
PageMeta(
    title="My App",
    description="Installable FastHTML app",
    include_pwa=True,
    pwa_name="My App",
    pwa_short_name="MyApp",
    pwa_theme_color="#0d6efd",
)
```

## Include favicon links

```python
PageMeta(
    title="Dashboard",
    favicon_url="/assets/favicon.png",
)
```

## Real route example

```python
@app.get("/")
def home():
    return (
        PageMeta(title="Home", description="Welcome"),
        Container(H1("Home")),
    )
```

## SEO vs PageMeta (important)

### Use `SEO(...)` when:

- You only need SEO/social tags.
- You want complete manual control.
- You are building your own composition layer.

### Use `PageMeta(...)` when:

- You want one helper for SEO + canonical + optional PWA/favicon.
- You want dedupe behavior to reduce head conflicts.
- You want a cleaner onboarding experience for app teams.

## Decision guide

- Simple content page: `SEO(...)` is enough.
- Marketing/app shell pages with installability/favicons: prefer `PageMeta(...)`.
- Large codebase with many routes/layouts: prefer `PageMeta(...)` for consistency.

## Common use cases

1. Blog/article routes that need social previews and canonical.
2. Product/detail routes that need share-ready metadata with minimal boilerplate.
3. PWA-ready pages that need head tags in one place.

## API reference summary

- SEO-related: `title`, `description`, `keywords`, `image`, `url`, `canonical`, `robots`, `twitter_site`, `twitter_creator`, `locale`.
- PWA-related: `include_pwa`, `pwa_name`, `pwa_short_name`, `pwa_theme_color`, `pwa_background_color`.
- Assets/meta extras: `favicon_url`, `extra_meta`.

## Notes

- `PageMeta(...)` is additive convenience, not a replacement for advanced `StructuredData` usage.
- For JSON-LD schema, keep using `StructuredData.*(...)` alongside `PageMeta(...)`.
