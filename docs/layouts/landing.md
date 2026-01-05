# LandingLayout

The `LandingLayout` component provides a clean, full-width layout optimized for landing pages and marketing sites. Perfect for product launches, portfolios, and promotional pages.

!!! success "Goal"
    Quickly build beautiful landing pages with navbar, content sections, and footer in a responsive layout.

---

## Quick Start

```python
from faststrap import LandingLayout, NavbarModern, Hero, Card

LandingLayout(
    # Content sections
    Hero(
        H1("Welcome to Our Product"),
        P("The best solution for your needs"),
        Button("Get Started", variant="primary", size="lg")
    ),
    Card("Feature section here"),
    
    # Navbar
    navbar=NavbarModern(
        brand="MyProduct",
        items=[
            ("Features", "#features"),
            ("Pricing", "#pricing"),
            ("Contact", "#contact")
        ]
    ),
    
    # Footer
    footer=Div(
        "© 2026 MyProduct. All rights reserved.",
        cls="text-center py-4"
    )
)
```

---

## Complete Example

```python
from faststrap import LandingLayout, NavbarModern, Hero, Card, Row, Col, Fx

@app.get("/")
def home():
    return LandingLayout(
        # Hero section
        Hero(
            H1("Build Faster with Faststrap", cls=Fx.fade_in),
            P("Modern Bootstrap components for FastHTML", cls=f"{Fx.fade_in} {Fx.delay_sm}"),
            Button("Get Started", variant="primary", size="lg", cls=f"{Fx.fade_in} {Fx.delay_md}"),
            variant="primary"
        ),
        
        # Features section
        Container(
            H2("Features", cls="text-center mb-5"),
            Row(
                Col(
                    Card(
                        Icon("lightning-fill", cls="text-primary fs-1"),
                        H4("Fast Development"),
                        P("Build UIs in pure Python"),
                        cls=f"{Fx.fade_in} {Fx.hover_lift}"
                    ),
                    md=4
                ),
                Col(
                    Card(
                        Icon("palette-fill", cls="text-success fs-1"),
                        H4("Beautiful Design"),
                        P("Bootstrap 5 components"),
                        cls=f"{Fx.fade_in} {Fx.hover_lift} {Fx.delay_sm}"
                    ),
                    md=4
                ),
                Col(
                    Card(
                        Icon("code-slash", cls="text-info fs-1"),
                        H4("Zero JavaScript"),
                        P("No JS knowledge required"),
                        cls=f"{Fx.fade_in} {Fx.hover_lift} {Fx.delay_md}"
                    ),
                    md=4
                )
            ),
            cls="py-5",
            id="features"
        ),
        
        # Navbar
        navbar=NavbarModern(
            brand="Faststrap",
            items=[
                ("Features", "#features"),
                ("Docs", "/docs"),
                ("GitHub", "https://github.com/...")
            ]
        ),
        
        # Footer
        footer=Div(
            Container(
                "© 2026 Faststrap. Built with ❤️ using FastHTML.",
                cls="text-center text-muted py-4"
            ),
            cls="bg-light border-top"
        )
    )
```

---

## Parameter Reference

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `*content` | `Any` | Required | Main content sections |
| `navbar` | `Any \| None` | `None` | Top navigation component |
| `footer` | `Any \| None` | `None` | Bottom footer component |
| `fluid` | `bool` | `False` | Use fluid container |
| `**kwargs` | `Any` | - | Additional HTML attributes |

::: faststrap.layouts.landing.LandingLayout
    options:
        show_source: true
        heading_level: 4
