# Footer Modern

The `FooterModern` component creates a professional multi-column footer with branding, link columns, social icons, and copyright. Perfect for landing pages and marketing sites with responsive grid layout.

!!! success "Goal"
    By the end of this guide, you'll be able to create beautiful, responsive footers **with zero CSS knowledge required.**

---

## Quick Start

Here's the simplest way to create a footer.

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <footer class="bg-dark text-light py-4">
      <div class="container">
        <div class="row">
          <div class="col-md-4">
            <h5>MyApp</h5>
            <p class="text-muted small">Building the future</p>
          </div>
          <div class="col-md-4">
            <h6 class="fw-bold mb-3">Product</h6>
            <p class="mb-2"><a href="/features" class="text-light text-decoration-none">Features</a></p>
            <p class="mb-2"><a href="/pricing" class="text-light text-decoration-none">Pricing</a></p>
          </div>
          <div class="col-md-4">
            <h6 class="fw-bold mb-3">Follow Us</h6>
            <div class="d-flex">
              <a href="#" class="text-light me-3 fs-4"><i class="bi bi-twitter"></i></a>
              <a href="#" class="text-light me-3 fs-4"><i class="bi bi-github"></i></a>
            </div>
          </div>
        </div>
        <hr class="border-light opacity-25 my-4">
        <p class="text-center text-muted small mb-0">© 2026 All rights reserved</p>
      </div>
    </footer>
  </div>
  <div class="preview-code" markdown>
```python
FooterModern(
    brand="MyApp",
    tagline="Building the future",
    columns=[
        {
            "title": "Product",
            "links": [
                {"text": "Features", "href": "/features"},
                {"text": "Pricing", "href": "/pricing"},
            ]
        }
    ],
    social_links=[
        {"icon": "twitter", "href": "https://twitter.com/myapp"},
        {"icon": "github", "href": "https://github.com/myapp"},
    ]
)
```
  </div>
</div>

---

## Visual Examples & Use Cases

### 1. Complete Footer

Full-featured footer with all sections.

```python
FooterModern(
    brand="MyCompany",
    tagline="Innovating since 2020",
    columns=[
        {
            "title": "Product",
            "links": [
                {"text": "Features", "href": "/features"},
                {"text": "Pricing", "href": "/pricing"},
                {"text": "Roadmap", "href": "/roadmap"},
                {"text": "Changelog", "href": "/changelog"},
            ]
        },
        {
            "title": "Company",
            "links": [
                {"text": "About", "href": "/about"},
                {"text": "Blog", "href": "/blog"},
                {"text": "Careers", "href": "/careers"},
                {"text": "Contact", "href": "/contact"},
            ]
        },
        {
            "title": "Legal",
            "links": [
                {"text": "Privacy", "href": "/privacy"},
                {"text": "Terms", "href": "/terms"},
                {"text": "Security", "href": "/security"},
            ]
        }
    ],
    social_links=[
        {"icon": "twitter", "href": "https://twitter.com/company"},
        {"icon": "github", "href": "https://github.com/company"},
        {"icon": "linkedin", "href": "https://linkedin.com/company/company"},
        {"icon": "youtube", "href": "https://youtube.com/@company"},
    ],
    copyright_text="© 2026 MyCompany Inc. All rights reserved."
)
```

### 2. Minimal Footer

Simple footer with just brand and copyright.

```python
FooterModern(
    brand="SimpleApp",
    copyright_text="© 2026 SimpleApp"
)
```

### 3. Light Theme Footer

Footer with light background.

```python
FooterModern(
    brand="LightApp",
    tagline="Clean and simple",
    bg_variant="light",
    text_variant="dark",
    columns=[
        {
            "title": "Links",
            "links": [
                {"text": "Home", "href": "/"},
                {"text": "About", "href": "/about"},
            ]
        }
    ]
)
```

---

## Practical Functionality

### With Logo

Use custom logo instead of text brand.

```python
from fasthtml.common import Img

FooterModern(
    brand=Img(
        src="/static/logo-white.png",
        alt="MyApp",
        style="max-width: 150px; height: auto;"
    ),
    tagline="Building amazing products",
    columns=[...]
)
```

### Newsletter Signup

Add newsletter form to footer.

```python
FooterModern(
    brand="MyApp",
    columns=[
        {
            "title": "Product",
            "links": [...]
        },
        {
            "title": "Newsletter",
            "links": []  # Empty, we'll add custom content
        }
    ]
)

# Or create custom footer section
def CustomFooter():
    return Footer(
        Container(
            Row(
                Col(
                    H5("MyApp"),
                    P("Stay updated", cls="text-muted")
                ),
                Col(
                    H6("Newsletter"),
                    Form(
                        InputGroup(
                            Input(type="email", placeholder="Your email"),
                            Button("Subscribe", variant="primary")
                        ),
                        hx_post="/newsletter/subscribe"
                    )
                )
            )
        ),
        cls="bg-dark text-light py-5"
    )
```

### Dynamic Links

Generate links from database.

```python
def AppFooter():
    # Get dynamic links
    product_pages = db.query(Page).filter(Page.category == "product").all()
    company_pages = db.query(Page).filter(Page.category == "company").all()
    
    return FooterModern(
        brand="MyApp",
        columns=[
            {
                "title": "Product",
                "links": [
                    {"text": page.title, "href": page.url}
                    for page in product_pages
                ]
            },
            {
                "title": "Company",
                "links": [
                    {"text": page.title, "href": page.url}
                    for page in company_pages
                ]
            }
        ],
        social_links=get_social_links()
    )
```

---

## Integration Patterns

### In Landing Layout

```python
def LandingLayout(*content):
    return Html(
        Head(...),
        Body(
            Navbar(...),
            Main(*content),
            FooterModern(
                brand="MyApp",
                tagline="Building the future",
                columns=[...],
                social_links=[...]
            )
        )
    )
```

### With Sticky Footer

Make footer stick to bottom on short pages.

```python
Html(
    Body(
        Div(
            Navbar(...),
            Main(*content, cls="flex-grow-1"),
            FooterModern(...),
            cls="d-flex flex-column min-vh-100"
        )
    )
)
```

### Multi-Language

Support multiple languages.

```python
def get_footer_links(lang="en"):
    translations = {
        "en": {
            "product": "Product",
            "features": "Features",
            "pricing": "Pricing",
        },
        "es": {
            "product": "Producto",
            "features": "Características",
            "pricing": "Precios",
        }
    }
    
    t = translations[lang]
    
    return FooterModern(
        brand="MyApp",
        columns=[
            {
                "title": t["product"],
                "links": [
                    {"text": t["features"], "href": f"/{lang}/features"},
                    {"text": t["pricing"], "href": f"/{lang}/pricing"},
                ]
            }
        ]
    )
```

---

## Parameter Reference

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `brand` | `str \| Any` | `None` | Brand name or logo element |
| `tagline` | `str \| None` | `None` | Optional tagline under brand |
| `columns` | `list[dict]` | `None` | Link columns with 'title' and 'links' |
| `social_links` | `list[dict]` | `None` | Social links with 'icon' and 'href' |
| `copyright_text` | `str \| None` | Auto | Copyright text |
| `bg_variant` | `str` | "dark" | Background color variant |
| `text_variant` | `str` | "light" | Text color variant |
| `**kwargs` | `Any` | - | Additional HTML attributes |

### Column Structure

```python
{
    "title": "Column Title",
    "links": [
        {"text": "Link Text", "href": "/url"},
        {"text": "Another Link", "href": "/url2"},
    ]
}
```

### Social Link Structure

```python
{
    "icon": "twitter",  # Bootstrap icon name
    "href": "https://twitter.com/username"
}
```

---

## Best Practices

### ✅ Do This

```python
# Organize links logically
columns=[
    {"title": "Product", "links": [...]},
    {"title": "Company", "links": [...]},
    {"title": "Legal", "links": [...]},
]

# Use semantic copyright
copyright_text="© 2026 MyCompany Inc. All rights reserved."

# Include important social links
social_links=[
    {"icon": "twitter", "href": "..."},
    {"icon": "github", "href": "..."},
]

# Match footer theme to site
FooterModern(bg_variant="dark", text_variant="light")
```

### ❌ Don't Do This

```python
# Don't overcrowd with too many columns
columns=[...10 columns...]  # Too many!

# Don't use broken links
{"text": "Page", "href": "#"}  # Use real URLs

# Don't forget copyright
# Always include copyright_text

# Don't mismatch colors
FooterModern(bg_variant="dark", text_variant="dark")  # Invisible!
```

---

::: faststrap.components.patterns.footer.FooterModern
    options:
        show_source: true
        heading_level: 4
