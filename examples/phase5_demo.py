"""
Phase 5 Demo: New Components Showcase

Demonstrates all Phase 5 components:
- Image (responsive images)
- Placeholder (skeleton loading)
- Carousel (image slider)
- SidebarNavbar (vertical sidebar)
- GlassNavbar (glassmorphism)
- Scrollspy (auto-updating nav)
"""

from fasthtml.common import (
    H1,
    H3,
    H4,
    H5,
    A,
    Div,
    FastHTML,
    Nav,
    P,
    serve,
)

from faststrap import (
    Card,
    Carousel,
    CarouselItem,
    Col,
    Container,
    Fx,
    GlassNavbar,
    Image,
    Placeholder,
    PlaceholderCard,
    Row,
    Scrollspy,
    SidebarNavbar,
    add_bootstrap,
)

app = FastHTML()
add_bootstrap(app)


@app.route("/")
def get():
    return Container(
        H1("Phase 5 Components Demo", cls=f"{Fx.fade_in} text-center mb-5"),
        # Image Component
        Card(
            H3("Image Component", cls="mb-3"),
            Row(
                Col(
                    H5("Fluid (Responsive)"),
                    Image(
                        src="https://via.placeholder.com/400x300",
                        alt="Responsive image",
                        fluid=True,
                    ),
                    md=4,
                ),
                Col(
                    H5("Thumbnail"),
                    Image(
                        src="https://via.placeholder.com/200x200",
                        alt="Thumbnail",
                        thumbnail=True,
                        rounded=True,
                    ),
                    md=4,
                ),
                Col(
                    H5("Rounded Circle"),
                    Image(
                        src="https://via.placeholder.com/150x150",
                        alt="Avatar",
                        rounded_circle=True,
                        align="center",
                    ),
                    md=4,
                ),
            ),
            cls="mb-5 p-4",
        ),
        # Placeholder Component
        Card(
            H3("Placeholder (Skeleton Loading)", cls="mb-3"),
            Row(
                Col(
                    H5("Glow Animation"),
                    Placeholder(width="100%", height="20px", animation="glow", cls="mb-2"),
                    Placeholder(width="75%", height="20px", animation="glow", cls="mb-2"),
                    Placeholder(width="50%", height="20px", animation="glow"),
                    md=4,
                ),
                Col(
                    H5("Wave Animation"),
                    Placeholder(width="100%", height="20px", animation="wave", cls="mb-2"),
                    Placeholder(width="80%", height="20px", animation="wave", cls="mb-2"),
                    Placeholder(width="60%", height="20px", animation="wave"),
                    md=4,
                ),
                Col(
                    H5("Card Skeleton"),
                    PlaceholderCard(
                        show_image=True, show_title=True, show_text=True, animation="glow"
                    ),
                    md=4,
                ),
            ),
            cls="mb-5 p-4",
        ),
        # Carousel Component
        Card(
            H3("Carousel (Image Slider)", cls="mb-3"),
            Carousel(
                CarouselItem(
                    Image(
                        src="https://via.placeholder.com/800x400/FF6B6B/FFFFFF?text=Slide+1",
                        cls="d-block w-100",
                        alt="Slide 1",
                    ),
                    caption_title="First Slide",
                    caption="This is the first slide with a caption",
                    active=True,
                ),
                CarouselItem(
                    Image(
                        src="https://via.placeholder.com/800x400/4ECDC4/FFFFFF?text=Slide+2",
                        cls="d-block w-100",
                        alt="Slide 2",
                    ),
                    caption_title="Second Slide",
                    caption="This is the second slide",
                ),
                CarouselItem(
                    Image(
                        src="https://via.placeholder.com/800x400/45B7D1/FFFFFF?text=Slide+3",
                        cls="d-block w-100",
                        alt="Slide 3",
                    ),
                    caption_title="Third Slide",
                    caption="This is the third slide",
                ),
                controls=True,
                indicators=True,
                interval=5000,
            ),
            cls="mb-5 p-4",
        ),
        # Premium Navbars
        Card(
            H3("Premium Navbars", cls="mb-3"),
            H5("Sidebar Navbar (Vertical)", cls="mt-4 mb-3"),
            P("Vertical sidebar with icons and theme support:", cls="text-muted"),
            Div(
                SidebarNavbar(
                    ("Dashboard", "/dashboard", "house"),
                    ("Users", "/users", "people"),
                    ("Analytics", "/analytics", "graph-up"),
                    ("Settings", "/settings", "gear"),
                    brand="Admin Panel",
                    theme="dark",
                    width="250px",
                ),
                style={"height": "400px", "position": "relative"},
            ),
            H5("Glass Navbar (Glassmorphism)", cls="mt-5 mb-3"),
            P("Modern navbar with blur and transparency:", cls="text-muted"),
            GlassNavbar(
                ("Home", "/"),
                ("Features", "/features"),
                ("Pricing", "/pricing"),
                ("Contact", "/contact"),
                brand="Glass App",
                blur_strength="medium",
                transparency=0.8,
                theme="light",
            ),
            cls="mb-5 p-4",
        ),
        # Scrollspy
        Card(
            H3("Scrollspy (Auto-updating Navigation)", cls="mb-3"),
            P("Navigation automatically highlights based on scroll position:", cls="text-muted"),
            # Simple navbar for scrollspy
            Nav(
                A("Section 1", href="#scrollspy-section1", cls="nav-link"),
                A("Section 2", href="#scrollspy-section2", cls="nav-link"),
                A("Section 3", href="#scrollspy-section3", cls="nav-link"),
                id="scrollspy-nav",
                cls="nav nav-pills mb-3",
            ),
            # Scrollspy content
            Scrollspy(
                Div(
                    H4("Section 1", id="scrollspy-section1"),
                    P("Content for section 1..." * 10),
                    cls="mb-4",
                ),
                Div(
                    H4("Section 2", id="scrollspy-section2"),
                    P("Content for section 2..." * 10),
                    cls="mb-4",
                ),
                Div(
                    H4("Section 3", id="scrollspy-section3"),
                    P("Content for section 3..." * 10),
                    cls="mb-4",
                ),
                target="#scrollspy-nav",
                offset=100,
                style={"height": "300px", "overflow-y": "auto", "position": "relative"},
            ),
            cls="mb-5 p-4",
        ),
        cls="py-5",
    )


if __name__ == "__main__":
    serve(port=5021)
