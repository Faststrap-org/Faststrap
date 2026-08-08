# PageMeta

`PageMeta` is a higher-level head composer that combines SEO tags, canonical URL handling, optional PWA tags, and optional favicon links in one call.

It is designed for teams that want a single, predictable entry point for page head metadata without repeating multiple helpers.

---

## Quick Start

```python
from faststrap import PageMeta

PageMeta(
    title="Faststrap Docs",
    description="Build modern UI in Python",
    canonical="https://faststrap.dev/docs",
    image="https://faststrap.dev/og/docs.png",
)
```

---

## Visual Examples & Use Cases

### 1. Basic SEO Page

```python
PageMeta(
    title="Home",
    description="Welcome to my app",
)
```

Renders:
```html
<title>Home - Welcome to my app</title>
<meta name="description" content="Welcome to my app">
```

### 2. Full PageMeta with PWA

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

### 3. With Favicon

```python
PageMeta(
    title="Dashboard",
    favicon_url="/assets/favicon.png",
)
```

---

## Practical Functionality

### 1. Route-Level Usage

```python
@app.get("/")
def home():
    return (
        PageMeta(title="Home", description="Welcome"),
        Container(H1("Home")),
    )
```

### 2. SEO vs PageMeta Decision Guide

| Scenario | Recommended |
|----------|-------------|
| Simple content page | `SEO(...)` |
| Marketing/app shell with PWA | `PageMeta(...)` |
| Large codebase with many routes | `PageMeta(...)` for consistency |

### 3. With Structured Data

```python
@app.get("/product")
def product():
    return (
        PageMeta(
            title="Product",
            description="Buy our product",
            image="https://example.com/og.png",
        ),
        StructuredData.Product(
            name="Product",
            description="Buy our product",
            brand="Brand",
        ),
        Container(H1("Product")),
    )
```

---

## Parameter Reference

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `title` | `str` | `None` | Page title. |
| `description` | `str` | `None` | Meta description. |
| `keywords` | `str \| None` | `None` | Meta keywords. |
| `image` | `str \| None` | `None` | Open Graph image URL. |
| `url` | `str \| None` | `None` | Canonical URL. |
| `canonical` | `str \| None` | `None` | Canonical URL (alias for `url`). |
| `robots` | `str \| None` | `None` | Robots meta content. |
| `twitter_site` | `str \| None` | `None` | Twitter site handle. |
| `twitter_creator` | `str \| None` | `None` | Twitter creator handle. |
| `locale` | `str \| None` | `None` | Locale for Open Graph. |
| `include_pwa` | `bool` | `False` | Include PWA meta tags. |
| `pwa_name` | `str \| None` | `None` | PWA application name. |
| `pwa_short_name` | `str \| None` | `None` | PWA short name. |
| `pwa_theme_color` | `str \| None` | `None` | PWA theme color. |
| `pwa_background_color` | `str \| None` | `None` | PWA background color. |
| `favicon_url` | `str \| None` | `None` | Custom favicon URL. |
| `extra_meta` | `dict \| None` | `None` | Additional meta tags. |
| `**kwargs` | `Any` | `{}` | Additional attributes. |

---

## API Reference

::: faststrap.seo.page_meta.PageMeta
    options:
        show_source: true
        heading_level: 4
