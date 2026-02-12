"""
SEO Demo
Demonstrates SEO component and StructuredData helpers for comprehensive SEO metadata
"""

from fasthtml.common import *

from faststrap import *

app = FastHTML()
add_bootstrap(app)


@app.get("/")
def home():
    """Homepage with basic SEO."""
    return (
        SEO(
            title="FastStrap - Modern Bootstrap 5 for FastHTML",
            description="Build beautiful web UIs in pure Python with zero JavaScript knowledge. FastStrap brings Bootstrap 5 components to FastHTML.",
            keywords=["fasthtml", "bootstrap", "python", "web framework", "ui components"],
            image="https://example.com/assets/og-home.jpg",
            url="https://example.com/",
            twitter_site="@faststrap",
            locale="en_US",
        ),
        StructuredData.organization(
            name="FastStrap",
            url="https://example.com",
            logo="https://example.com/assets/logo.png",
            social_links=[
                "https://github.com/Faststrap-org/Faststrap",
                "https://twitter.com/faststrap",
            ],
        ),
        Container(
            H1("SEO Examples", cls="mb-4"),
            P("Click the links below to see different SEO implementations:", cls="lead"),
            Card(
                ListGroup(
                    ListGroupItem(
                        A(
                            "Blog Post (Article SEO)",
                            href="/blog/python-tips",
                            cls="text-decoration-none",
                        ),
                        cls="d-flex justify-content-between align-items-center",
                    ),
                    ListGroupItem(
                        A(
                            "Product Page (Product SEO)",
                            href="/product/123",
                            cls="text-decoration-none",
                        ),
                        cls="d-flex justify-content-between align-items-center",
                    ),
                    ListGroupItem(
                        A("Local Business Page", href="/business", cls="text-decoration-none"),
                        cls="d-flex justify-content-between align-items-center",
                    ),
                    flush=True,
                ),
                header="SEO Examples",
            ),
            Alert(
                H5("How to View SEO Tags", cls="alert-heading"),
                P("To see the generated SEO tags:"),
                Ol(
                    Li("Right-click on any page and select 'View Page Source'"),
                    Li("Look for meta tags in the <head> section"),
                    Li("Use browser dev tools (F12) to inspect the <head> element"),
                    Li("Use SEO tools like Facebook Debugger or Twitter Card Validator"),
                ),
                variant="info",
                cls="mt-4",
            ),
            cls="my-5",
        ),
    )


@app.get("/blog/python-tips")
def blog_post():
    """Blog post with article SEO and structured data."""
    return (
        SEO(
            title="10 Tips for Better Python Code - FastStrap Blog",
            description="Learn how to write cleaner, more maintainable Python code with these 10 essential tips from experienced developers.",
            keywords=["python", "coding", "best practices", "clean code"],
            image="https://example.com/assets/python-tips.jpg",
            url="https://example.com/blog/python-tips",
            article=True,
            published_time="2026-02-12T10:00:00Z",
            modified_time="2026-02-12T14:30:00Z",
            author="Jane Smith",
            section="Programming",
            tags=["python", "tutorial", "best-practices"],
            twitter_site="@faststrap",
            twitter_creator="@janesmith",
            locale="en_US",
        ),
        StructuredData.article(
            headline="10 Tips for Better Python Code",
            description="Learn how to write cleaner, more maintainable Python code",
            image="https://example.com/assets/python-tips.jpg",
            author="Jane Smith",
            published="2026-02-12T10:00:00Z",
            modified="2026-02-12T14:30:00Z",
        ),
        StructuredData.breadcrumb(
            [
                ("Home", "https://example.com/"),
                ("Blog", "https://example.com/blog"),
                ("Python Tips", "https://example.com/blog/python-tips"),
            ]
        ),
        Container(
            H1("10 Tips for Better Python Code", cls="mb-3"),
            P("By Jane Smith • Published Feb 12, 2026", cls="text-muted mb-4"),
            Alert(
                Icon("check-circle-fill", cls="me-2"),
                Strong("SEO Implemented: "),
                "This page includes article meta tags, Open Graph, Twitter Cards, and JSON-LD structured data.",
                variant="success",
            ),
            Card(
                H5("Article Content", cls="card-title"),
                P("This is where your blog post content would go..."),
                P("The page includes:"),
                Ul(
                    Li("Article-specific Open Graph tags (og:type=article)"),
                    Li("Published and modified timestamps"),
                    Li("Author information"),
                    Li("Article tags and section"),
                    Li("JSON-LD Article structured data"),
                    Li("Breadcrumb navigation structured data"),
                ),
            ),
            A("← Back to Examples", href="/", cls="btn btn-secondary mt-4"),
            cls="my-5",
        ),
    )


@app.get("/product/123")
def product_page():
    """Product page with product SEO and structured data."""
    return (
        SEO(
            title="Wireless Headphones - Premium Noise Cancelling | FastStrap Store",
            description="Experience superior sound quality with our premium wireless headphones. Active noise cancelling, 30-hour battery life, and comfortable design.",
            keywords=["headphones", "wireless", "noise cancelling", "audio"],
            image="https://example.com/assets/headphones.jpg",
            url="https://example.com/product/123",
            type="product",
            twitter_site="@faststrap",
            locale="en_US",
        ),
        StructuredData.product(
            name="Wireless Headphones - Premium Noise Cancelling",
            description="Experience superior sound quality with our premium wireless headphones",
            image="https://example.com/assets/headphones.jpg",
            price="199.99",
            currency="USD",
            rating=4.5,
            review_count=342,
            availability="InStock",
            brand="AudioTech",
            sku="WH-1000XM5",
        ),
        StructuredData.breadcrumb(
            [
                ("Home", "https://example.com/"),
                ("Products", "https://example.com/products"),
                ("Headphones", "https://example.com/products/headphones"),
                ("Wireless Headphones", "https://example.com/product/123"),
            ]
        ),
        Container(
            H1("Wireless Headphones - Premium Noise Cancelling", cls="mb-3"),
            Row(
                Col(
                    Image(
                        src="https://via.placeholder.com/400x400?text=Headphones",
                        alt="Wireless Headphones",
                        rounded=True,
                    ),
                    cols=12,
                    md=6,
                ),
                Col(
                    Alert(
                        Icon("check-circle-fill", cls="me-2"),
                        Strong("SEO Implemented: "),
                        "Product meta tags, pricing, ratings, and availability.",
                        variant="success",
                    ),
                    H3("$199.99", cls="text-primary mb-3"),
                    Div(
                        Icon("star-fill", cls="text-warning"),
                        Icon("star-fill", cls="text-warning"),
                        Icon("star-fill", cls="text-warning"),
                        Icon("star-fill", cls="text-warning"),
                        Icon("star-half", cls="text-warning"),
                        Span(" 4.5/5 (342 reviews)", cls="ms-2 text-muted"),
                        cls="mb-3",
                    ),
                    P(
                        "Experience superior sound quality with our premium wireless headphones. Active noise cancelling, 30-hour battery life, and comfortable design."
                    ),
                    Badge("In Stock", variant="success", cls="mb-3"),
                    Br(),
                    Button("Add to Cart", variant="primary", size="lg"),
                    cols=12,
                    md=6,
                ),
            ),
            A("← Back to Examples", href="/", cls="btn btn-secondary mt-4"),
            cls="my-5",
        ),
    )


@app.get("/business")
def local_business():
    """Local business page with LocalBusiness structured data."""
    return (
        SEO(
            title="Joe's Coffee Shop - Best Coffee in Springfield",
            description="Visit Joe's Coffee Shop for the best coffee in Springfield. Fresh roasted beans, cozy atmosphere, and friendly service.",
            keywords=["coffee shop", "springfield", "coffee", "cafe"],
            image="https://example.com/assets/coffee-shop.jpg",
            url="https://example.com/business",
            twitter_site="@joescoffee",
            locale="en_US",
        ),
        StructuredData.local_business(
            name="Joe's Coffee Shop",
            address={
                "street": "123 Main Street",
                "city": "Springfield",
                "state": "IL",
                "zip": "62701",
                "country": "US",
            },
            phone="+1-555-123-4567",
            hours={
                "Monday-Friday": "7:00-19:00",
                "Saturday-Sunday": "8:00-17:00",
            },
            priceRange="$$",
            servesCuisine="Coffee & Pastries",
        ),
        Container(
            H1("Joe's Coffee Shop", cls="mb-3"),
            P("Best Coffee in Springfield", cls="lead"),
            Alert(
                Icon("check-circle-fill", cls="me-2"),
                Strong("SEO Implemented: "),
                "LocalBusiness structured data with address, hours, and contact info.",
                variant="success",
                cls="mb-4",
            ),
            Row(
                Col(
                    Card(
                        H5("Location", cls="card-title"),
                        P("123 Main Street", Br(), "Springfield, IL 62701", Br(), "United States"),
                    ),
                    cols=12,
                    md=4,
                    cls="mb-3",
                ),
                Col(
                    Card(
                        H5("Hours", cls="card-title"),
                        P(
                            Strong("Mon-Fri: "),
                            "7:00 AM - 7:00 PM",
                            Br(),
                            Strong("Sat-Sun: "),
                            "8:00 AM - 5:00 PM",
                        ),
                    ),
                    cols=12,
                    md=4,
                    cls="mb-3",
                ),
                Col(
                    Card(
                        H5("Contact", cls="card-title"),
                        P(
                            Icon("telephone-fill", cls="me-2"),
                            "+1-555-123-4567",
                            Br(),
                            Icon("currency-dollar", cls="me-2"),
                            "Price Range: $$",
                        ),
                    ),
                    cols=12,
                    md=4,
                    cls="mb-3",
                ),
            ),
            A("← Back to Examples", href="/", cls="btn btn-secondary mt-4"),
            cls="my-5",
        ),
    )


serve()
