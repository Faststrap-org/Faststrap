"""
Showcase - Furniture Store Landing
Inspired by the uploaded furniture reference layout.
Built fully with Faststrap + FastHTML components.
"""

from fasthtml.common import (
    H1,
    H2,
    H3,
    H4,
    A,
    Br,
    Div,
    FastHTML,
    Img,
    P,
    Span,
    Strong,
    Style,
    serve,
)

from faststrap import (
    Badge,
    Button,
    Card,
    Col,
    Container,
    FooterModern,
    Icon,
    Navbar,
    Row,
    add_bootstrap,
)

app = FastHTML()
add_bootstrap(app, font_family="Montserrat")

PRODUCTS = [
    (
        "Accent Lounge Chair",
        "$249",
        "https://images.unsplash.com/photo-1596162954151-cdcb4c0f70a8?w=800",
    ),
    (
        "Pastel Occasional Chair",
        "$189",
        "https://images.unsplash.com/photo-1505693416388-ac5ce068fe85?w=800",
    ),
    (
        "Round Walnut Table",
        "$320",
        "https://images.unsplash.com/photo-1505691938895-1758d7feb511?w=800",
    ),
    ("Soft Fabric Sofa", "$640", "https://images.unsplash.com/photo-1555041469-a586c61ea9bc?w=800"),
    (
        "Velvet Reading Chair",
        "$279",
        "https://images.unsplash.com/photo-1549187774-b4e9b0445b41?w=800",
    ),
    (
        "Minimal Daybed",
        "$520",
        "https://images.unsplash.com/photo-1583847268964-b28dc8f51f92?w=800",
    ),
]

FEATURED = [
    (
        "Industrial Side Table",
        "$120",
        "https://images.unsplash.com/photo-1616594039964-3b1c0801c4e7?w=800",
    ),
    (
        "Nordic TV Console",
        "$480",
        "https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?w=800",
    ),
    (
        "Floating Wall Shelf",
        "$80",
        "https://images.unsplash.com/photo-1556228453-efd6c1ff04f6?w=800",
    ),
    (
        "Compact Work Desk",
        "$260",
        "https://images.unsplash.com/photo-1519710164239-da123dc03ef4?w=800",
    ),
    (
        "Lounge Grey Armchair",
        "$350",
        "https://images.unsplash.com/photo-1615874959474-d609969a20ed?w=800",
    ),
]

BRANDS = [
    "WoodNature",
    "Golden Gallery",
    "Modern Living",
    "HighLight Home",
    "Nordic Scale",
]

NEWS = [
    (
        "The Art of Choosing Furniture That Complements Your Space",
        "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?w=1200",
    ),
    (
        "Sustainable Materials: The Future of Modern Furniture",
        "https://images.unsplash.com/photo-1615529182904-14819c35db37?w=1200",
    ),
    (
        "How Minimalist Decor Creates Calm Living Rooms",
        "https://images.unsplash.com/photo-1493663284031-b7e3aefcae8e?w=1200",
    ),
]

SHOWCASE_CSS = """
body { background: #f3f3f3; }
.fs-main-nav { background: rgba(255,255,255,.95); border-radius: .75rem; }
.fs-brand { font-size: 1.5rem; font-weight: 800; color: #111; text-transform: lowercase; letter-spacing: .04em; }
.fs-hero { background: #111; }
.fs-dark-section { background: #1a1d21; }
.fs-hover-lift { transition: transform .2s ease, box-shadow .2s ease; }
.fs-hover-lift:hover { transform: translateY(-4px); box-shadow: 0 14px 28px rgba(0,0,0,.16) !important; }
.fs-metric-card { background: linear-gradient(160deg,#1b2226,#2d363d); color: #fff; }
.fs-soft-banner { background: linear-gradient(160deg,#f6efe5,#fef8f0); }
.fs-quote { background: #171a1d; color: #fff; }
"""


def product_card(name: str, price: str, image: str):
    return Card(
        Img(src=image, cls="w-100 object-fit-cover rounded-top", style="height:180px;"),
        Div(
            Strong(name, cls="d-block mb-1"),
            Span(price, cls="text-muted"),
            cls="p-3",
        ),
        cls="border-0 shadow-sm h-100 fs-hover-lift",
    )


@app.get("/")
def home():
    return Div(
        Style(SHOWCASE_CSS),
        Container(
            Div(
                # Header
                Div(
                    Navbar(
                        brand=Span("sea", cls="fs-brand"),
                        items=[
                            Div(
                                A("Home", href="#home", cls="nav-link"),
                                A("Products", href="#products", cls="nav-link"),
                                A("About Us", href="#about", cls="nav-link"),
                                A("Trending", href="#featured", cls="nav-link"),
                                A("Deals", href="#deals", cls="nav-link"),
                                A("Contact", href="#footer", cls="nav-link"),
                                cls="navbar-nav me-auto mb-2 mb-lg-0",
                            ),
                            Div(
                                Button("Login", variant="outline-dark", size="sm", cls="me-2"),
                                Button("Sign Up", variant="dark", size="sm"),
                                cls="d-flex align-items-center",
                            ),
                        ],
                        variant="light",
                        expand="lg",
                        sticky="top",
                        container=True,
                        cls="shadow-sm fs-main-nav px-2",
                    ),
                    cls="pt-3 position-sticky top-0 z-3",
                ),
                # Hero
                Div(
                    Row(
                        Col(
                            Div(
                                Badge(
                                    "New Collection",
                                    variant="warning",
                                    cls="text-dark fw-bold mb-3",
                                ),
                                H1(
                                    Span("Furniture ", cls="text-warning"),
                                    "Solutions.",
                                    Br(),
                                    "Affordable Prices.",
                                    cls="display-4 fw-bold text-white",
                                ),
                                P(
                                    "Discover elegant, durable furniture built for modern living spaces. "
                                    "From curated chairs to premium cabinets, we help you furnish beautifully.",
                                    cls="text-light-emphasis mt-3 fs-5",
                                ),
                                Div(
                                    Button(
                                        "View Products",
                                        variant="warning",
                                        cls="text-dark fw-bold me-2",
                                    ),
                                    Button("Request Quote", variant="outline-light"),
                                    cls="mt-4",
                                ),
                                cls="p-5",
                            ),
                            lg=7,
                            cols=12,
                        ),
                        Col(
                            Div(
                                Img(
                                    src="https://images.unsplash.com/photo-1484101403633-562f891dc89a?w=1200",
                                    cls="w-100 rounded-3 object-fit-cover",
                                    style="height:100%; min-height:420px;",
                                ),
                                cls="h-100 p-3",
                            ),
                            lg=5,
                            cols=12,
                        ),
                        cls="g-0",
                    ),
                    id="home",
                    cls="rounded-4 overflow-hidden fs-hero mt-3",
                ),
                # What we produce
                Div(
                    Row(
                        Col(
                            H2("What We Produce.", cls="fw-bold text-white"),
                            P(
                                "Furniture categories crafted for every corner of your home and office.",
                                cls="text-light-emphasis",
                            ),
                            lg=4,
                            cols=12,
                        ),
                        Col(
                            Row(
                                Col(
                                    Card(
                                        Strong("BEDROOM"),
                                        P(
                                            "Comfort-first furniture built for peaceful rest.",
                                            cls="small text-muted",
                                        ),
                                        cls="p-3 border-0 h-100",
                                    ),
                                    md=6,
                                    cols=12,
                                ),
                                Col(
                                    Card(
                                        Strong("KITCHEN"),
                                        P(
                                            "Practical and stylish options for modern cooking spaces.",
                                            cls="small text-muted",
                                        ),
                                        cls="p-3 border-0 h-100",
                                    ),
                                    md=6,
                                    cols=12,
                                ),
                                Col(
                                    Card(
                                        Strong("LIVING ROOM"),
                                        P(
                                            "Sofas, chairs, and statement pieces for daily comfort.",
                                            cls="small text-muted",
                                        ),
                                        cls="p-3 border-0 h-100",
                                    ),
                                    md=6,
                                    cols=12,
                                ),
                                Col(
                                    Card(
                                        Strong("OFFICE"),
                                        P(
                                            "Ergonomic and productive workspace essentials.",
                                            cls="small text-muted",
                                        ),
                                        cls="p-3 border-0 h-100",
                                    ),
                                    md=6,
                                    cols=12,
                                ),
                                cls="g-3",
                            ),
                            lg=8,
                            cols=12,
                        ),
                    ),
                    cls="mt-5 p-4 rounded-4 fs-dark-section",
                ),
                # Products grid
                Div(
                    H2("Our Products", cls="fw-bold text-center"),
                    P(
                        "Carefully selected pieces to elevate comfort and style.",
                        cls="text-center text-muted mb-4",
                    ),
                    Row(
                        *[
                            Col(product_card(n, p, i), lg=4, md=6, cols=12, cls="mb-4")
                            for n, p, i in PRODUCTS
                        ],
                        cls="g-3",
                    ),
                    Div(Button("All Products", variant="outline-dark"), cls="text-center mt-2"),
                    id="products",
                    cls="mt-5",
                ),
                # Featured row + side panel
                Div(
                    Row(
                        Col(
                            H3("Featured Products", cls="fw-bold mb-3"),
                            Row(
                                *[
                                    Col(
                                        Card(
                                            Img(
                                                src=img,
                                                cls="w-100 object-fit-cover rounded-top",
                                                style="height:120px;",
                                            ),
                                            Div(
                                                Strong(name, cls="small d-block"),
                                                Span(price, cls="small text-muted"),
                                                cls="p-2",
                                            ),
                                            cls="border-0 shadow-sm h-100",
                                        ),
                                        md=4,
                                        cols=6,
                                        cls="mb-3",
                                    )
                                    for name, price, img in FEATURED
                                ],
                                cls="g-2",
                            ),
                            lg=8,
                            cols=12,
                            id="featured",
                        ),
                        Col(
                            Card(
                                Img(
                                    src="https://images.unsplash.com/photo-1555041469-a586c61ea9bc?w=1200",
                                    cls="w-100 object-fit-cover rounded-top",
                                    style="height:220px;",
                                ),
                                Div(
                                    Badge("UP TO 35% OFF", variant="warning", cls="text-dark"),
                                    H4("Perfect Cabinets For Your Living Room!"),
                                    P(
                                        "Limited-time pricing on handcrafted storage essentials.",
                                        cls="text-muted",
                                    ),
                                    Button("Shop Now", variant="warning", cls="text-dark fw-bold"),
                                    cls="p-3",
                                ),
                                cls="border-0 shadow-sm",
                            ),
                            lg=4,
                            cols=12,
                        ),
                    ),
                    cls="mt-5",
                ),
                # Why choose us + numbers + deals
                Div(
                    Row(
                        Col(
                            H3("Why Choose Us", cls="fw-bold"),
                            Row(
                                Col(
                                    Card(
                                        Span("01", cls="display-6 fw-bold text-warning"),
                                        Strong("Crafted with Precision"),
                                        P(
                                            "Quality-first construction in every piece.",
                                            cls="small text-muted",
                                        ),
                                        cls="border-0 shadow-sm p-3 h-100",
                                    ),
                                    md=6,
                                    cols=12,
                                    cls="mb-3",
                                ),
                                Col(
                                    Card(
                                        Span("02", cls="display-6 fw-bold text-warning"),
                                        Strong("Sustainable Materials"),
                                        P(
                                            "Eco-conscious sourcing and finishes.",
                                            cls="small text-muted",
                                        ),
                                        cls="border-0 shadow-sm p-3 h-100",
                                    ),
                                    md=6,
                                    cols=12,
                                    cls="mb-3",
                                ),
                                Col(
                                    Card(
                                        Span("03", cls="display-6 fw-bold text-warning"),
                                        Strong("Designed for Every Space"),
                                        P(
                                            "From compact apartments to large homes.",
                                            cls="small text-muted",
                                        ),
                                        cls="border-0 shadow-sm p-3 h-100",
                                    ),
                                    md=6,
                                    cols=12,
                                    cls="mb-3",
                                ),
                                Col(
                                    Card(
                                        Span("04", cls="display-6 fw-bold text-warning"),
                                        Strong("Reliable Delivery"),
                                        P(
                                            "On-time nationwide shipping support.",
                                            cls="small text-muted",
                                        ),
                                        cls="border-0 shadow-sm p-3 h-100",
                                    ),
                                    md=6,
                                    cols=12,
                                    cls="mb-3",
                                ),
                                cls="g-3",
                            ),
                            lg=8,
                            cols=12,
                            id="about",
                        ),
                        Col(
                            Card(
                                Div(
                                    Span("74353", cls="display-6 fw-bold"),
                                    P("Orders Delivered", cls="mb-4 text-light-emphasis"),
                                ),
                                Div(
                                    Span("6333", cls="display-6 fw-bold"),
                                    P("Happy Homes", cls="mb-4 text-light-emphasis"),
                                ),
                                Div(
                                    Span("20+", cls="display-6 fw-bold"),
                                    P("Cities Served", cls="mb-4 text-light-emphasis"),
                                ),
                                Div(
                                    Span("20+", cls="display-6 fw-bold"),
                                    P("Years Experience", cls="text-light-emphasis"),
                                ),
                                cls="p-4 border-0 fs-metric-card",
                            ),
                            lg=4,
                            cols=12,
                        ),
                    ),
                    cls="mt-5",
                ),
                Div(
                    Row(
                        Col(
                            Card(
                                Div(
                                    H4("Host Perfect Meals With Discounted Tables."),
                                    P(
                                        "Explore dining collections designed to make every gathering memorable.",
                                        cls="text-muted",
                                    ),
                                    Button(
                                        "Shop Tables", variant="warning", cls="text-dark fw-bold"
                                    ),
                                    cls="p-4",
                                ),
                                cls="border-0 fs-soft-banner h-100",
                            ),
                            lg=8,
                            cols=12,
                        ),
                        Col(
                            Card(
                                Div(
                                    Icon("quote", cls="display-4 text-warning"),
                                    P(
                                        "I absolutely love our new living room set. "
                                        "The craftsmanship is outstanding and delivery was seamless.",
                                        cls="text-light mb-3",
                                    ),
                                    Strong("John Doe", cls="text-warning"),
                                    cls="p-4",
                                ),
                                cls="border-0 fs-quote h-100",
                            ),
                            lg=4,
                            cols=12,
                        ),
                    ),
                    id="deals",
                    cls="mt-4",
                ),
                # Brands and News
                Div(
                    H3("Top Featured Brands.", cls="fw-bold mb-3"),
                    Row(
                        *[
                            Col(
                                Card(
                                    Strong(b),
                                    P("Quality partner", cls="small text-muted"),
                                    cls="border-0 shadow-sm p-3",
                                ),
                                md=4,
                                lg=2,
                                cols=6,
                                cls="mb-3",
                            )
                            for b in BRANDS
                        ],
                        cls="g-2",
                    ),
                    cls="mt-5",
                ),
                Div(
                    H3("News & Updates", cls="fw-bold mb-3"),
                    Row(
                        *[
                            Col(
                                Card(
                                    Img(
                                        src=img,
                                        cls="w-100 object-fit-cover rounded-top",
                                        style="height:180px;",
                                    ),
                                    Div(Strong(title), cls="p-3"),
                                    cls="border-0 shadow-sm h-100",
                                ),
                                lg=4,
                                cols=12,
                                cls="mb-3",
                            )
                            for title, img in NEWS
                        ],
                        cls="g-3",
                    ),
                    cls="mt-3 mb-5",
                ),
                # Footer
                FooterModern(
                    brand="sea",
                    tagline="Premium furniture solutions for elegant living.",
                    columns=[
                        {
                            "title": "Company",
                            "links": [
                                {"text": "About", "href": "#about"},
                                {"text": "Products", "href": "#products"},
                                {"text": "Contact", "href": "#footer"},
                            ],
                        },
                        {
                            "title": "Support",
                            "links": [
                                {"text": "Shipping", "href": "#"},
                                {"text": "Returns", "href": "#"},
                                {"text": "Help Center", "href": "#"},
                            ],
                        },
                    ],
                    social_links=[
                        {"icon": "instagram", "href": "#"},
                        {"icon": "facebook", "href": "#"},
                        {"icon": "twitter-x", "href": "#"},
                    ],
                    bg_variant="dark",
                    text_variant="light",
                    copyright_text="© 2026 Sea Furniture. All rights reserved.",
                    id="footer",
                    cls="rounded-4 mt-4",
                ),
                cls="py-4",
            ),
            cls="container-xl",
        ),
    )


serve()
