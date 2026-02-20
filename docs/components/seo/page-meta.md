# PageMeta

`PageMeta` composes SEO + canonical + optional PWA + favicon tags with dedupe guarantees.

## Import

```python
from faststrap import PageMeta
```

## Basic usage

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

## Route example

```python
@app.get("/")
def home():
    return (
        PageMeta(title="Home", description="Welcome"),
        Container(H1("Home")),
    )
```

