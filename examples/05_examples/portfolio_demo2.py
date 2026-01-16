from fasthtml.common import *

from faststrap import Button, Icon, add_bootstrap

# -------------------------------------------------------
# Custom CSS for Portfolio Landing Page
# -------------------------------------------------------
custom_css = """
.hero {
    background: linear-gradient(135deg, #4b6cb7 0%, #182848 100%);
    padding: 120px 0;
    color: white;
}
.hero-title {
    font-size: 3rem;
    font-weight: 700;
    animation: fadeDown 1s ease;
}
.hero-subtitle {
    font-size: 1.25rem;
    opacity: 0.9;
    max-width: 600px;
}
.section-title {
    font-size: 2.25rem;
    font-weight: 700;
    margin-bottom: 30px;
}
.portfolio-card {
    transition: all .3s ease;
    border-radius: 16px;
    overflow: hidden;
}
.portfolio-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 14px 25px rgba(0,0,0,0.15);
}
.portfolio-img {
    width: 100%;
    height: 200px;
    object-fit: cover;
}
.testimonial-box {
    background: #f8f9fa;
    border-radius: 14px;
    padding: 25px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.07);
}
@keyframes fadeDown {
    from { opacity: 0; transform: translateY(-20px); }
    to { opacity: 1; transform: translateY(0); }
}
"""
hrds = (
    Style(custom_css),
    # Link(rel="", href=""), add more custom head elements if needed
    # Script(src="", defer=True), add custom scripts if needed
    # Meta() add custom meta tags if needed
)
# -------------------------------------------------------
# App Initialization
# -------------------------------------------------------
app, rt = fast_app(hdrs=hrds)
add_bootstrap(app, theme="dark", use_cdn=False)


# -------------------------------------------------------
# Landing Page Route
# -------------------------------------------------------
@rt("/")
def landing():
    return Div(
        # ---------------- HERO SECTION -----------------
        Div(
            Div(
                H1(
                    "Hi, I'm Meshell — Software Engineer & AI Systems Architect",
                    cls="hero-title mb-3",
                ),
                P(
                    "I build scalable APIs, AI-driven systems, distributed backends, "
                    "and elegant cross-platform applications.",
                    cls="hero-subtitle mb-4",
                ),
                Div(
                    Button(
                        "View My Work",
                        variant="primary",
                        size="lg",
                        icon="arrow-right",
                        cls="me-3",
                        hx_get="#portfolio",
                        hx_target="#portfolio",
                    ),
                    Button("Hire Me", variant="success", size="lg", icon="chat-dots"),
                    cls="d-flex flex-wrap",
                ),
                cls="container",
            ),
            cls="hero",
        ),
        # ---------------- ABOUT SECTION -----------------
        Div(
            Div(
                H2("About Me", cls="section-title"),
                P(
                    """I’m a full-stack software engineer specialized in FastAPI,
                    distributed systems, SQLAlchemy, AI agent development, Kivy/KivyMD,
                    PyQt/PySide, Reflex, and modern backend architecture.
                    I build fast, reliable, secure, and user-focused applications.""",
                    cls="lead text-muted",
                ),
                cls="container py-5",
            ),
            id="about",
        ),
        # ---------------- PORTFOLIO SECTION -----------------
        Div(
            Div(
                H2("Portfolio", cls="section-title text-center mb-5"),
                Div(
                    # Project 1
                    Div(
                        Div(
                            Img(src="https://picsum.photos/600/400?1", cls="portfolio-img"),
                            Div(
                                H4("QRive — Verified Business Identity Platform", cls="fw-bold"),
                                P(
                                    "End-to-end Reflex + FastAPI platform for verified digital hubs."
                                ),
                                Button("View Details", outline=True, variant="primary", size="sm"),
                                cls="p-3",
                            ),
                            cls="portfolio-card bg-white shadow-sm",
                        ),
                        cls="col-md-4 mb-4",
                    ),
                    # Project 2
                    Div(
                        Div(
                            Img(src="https://picsum.photos/600/400?2", cls="portfolio-img"),
                            Div(
                                H4("Cooperative Financial Manager (Offline-First)", cls="fw-bold"),
                                P("KivyMD + FastAPI system for rural cooperatives."),
                                Button("View Details", outline=True, variant="primary", size="sm"),
                                cls="p-3",
                            ),
                            cls="portfolio-card bg-white shadow-sm",
                        ),
                        cls="col-md-4 mb-4",
                    ),
                    # Project 3
                    Div(
                        Div(
                            Img(src="https://picsum.photos/600/400?3", cls="portfolio-img"),
                            Div(
                                H4("Church Population Analytics Server", cls="fw-bold"),
                                P("SQLAlchemy + FastAPI + Permission-based analytics dashboard."),
                                Button("View Details", outline=True, variant="primary", size="sm"),
                                cls="p-3",
                            ),
                            cls="portfolio-card bg-white shadow-sm",
                        ),
                        cls="col-md-4 mb-4",
                    ),
                    cls="row",
                ),
                cls="container py-5",
            ),
            id="portfolio",
        ),
        # ---------------- TESTIMONIALS SECTION -----------------
        Div(
            Div(
                H2("What People Say", cls="section-title text-center mb-5"),
                Div(
                    # Testimonial 1
                    Div(
                        Div(
                            P(
                                "“One of the most reliable engineers I’ve worked with. "
                                "Understands systems deeply.”",
                                cls="mb-2",
                            ),
                            Strong("— CEO, Quoin Lab Technology"),
                            cls="testimonial-box",
                        ),
                        cls="col-md-4 mb-4",
                    ),
                    # Testimonial 2
                    Div(
                        Div(
                            P(
                                "“Delivers fast, clean architecture. Solves problems we "
                                "couldn’t even debug.”",
                                cls="mb-2",
                            ),
                            Strong("— Lead Engineer, Startup Founder"),
                            cls="testimonial-box",
                        ),
                        cls="col-md-4 mb-4",
                    ),
                    # Testimonial 3
                    Div(
                        Div(
                            P(
                                "“A machine learning and backend expert. Highly recommended.”",
                                cls="mb-2",
                            ),
                            Strong("— Research Partner"),
                            cls="testimonial-box",
                        ),
                        cls="col-md-4 mb-4",
                    ),
                    cls="row",
                ),
                cls="container py-5",
            ),
            id="testimonials",
        ),
        # ---------------- CONTACT SECTION -----------------
        Div(
            Div(
                H2("Contact Me", cls="section-title text-center"),
                P("Let’s build something great together.", cls="text-center text-muted mb-4"),
                Div(
                    Div(
                        Icon("envelope", cls="text-primary fs-2 mb-2"),
                        P("evayoungtech@gmail.com", cls="fw-bold"),
                        cls="text-center col-md-4 mb-4",
                    ),
                    Div(
                        Icon("phone", cls="text-primary fs-2 mb-2"),
                        P("+234 902 995 2120", cls="fw-bold"),
                        cls="text-center col-md-4 mb-4",
                    ),
                    Div(
                        Icon("github", cls="text-primary fs-2 mb-2"),
                        P("github.com/Faststrap-org", cls="fw-bold"),
                        cls="text-center col-md-4 mb-4",
                    ),
                    cls="row justify-content-center",
                ),
                cls="container py-5",
            ),
            id="contact",
        ),
    )


if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("\n📍 Visit: http://localhost:5000")
    print("\n" + "=" * 70)
    serve(port=5000)
