from fasthtml.common import (
    A,
    Div,
    FastHTML,
    H2,
    H4,
    Main,
    P,
    Section,
    Title,
    serve,
)

from faststrap import (
    Accordion,
    AccordionItem,
    Button,
    Col,
    Container,
    Hero,
    Icon,
    Navbar,
    Row,
    StatCard,
    add_bootstrap,
)


def render_feature(icon, title, desc):
    return Col(
        Div(
            Icon(icon, cls="fs-1 text-primary mb-3"),
            H4(title),
            P(desc, cls="text-muted"),
            cls="h-100 p-4",
        ),
        md=4,
        cls="mb-4",
    )


def home():
    # Navbar
    nav = Navbar(
        A("Pricing", href="#", cls="nav-link"),
        A("Features", href="#", cls="nav-link"),
        A("Login", href="#", cls="nav-link ms-auto"),
        Button("Try for Free", variant="primary", cls="ms-2"),
        brand="FastCloud",
        expand="lg",
        bg="white",
        sticky="top",
        cls="border-bottom",
    )

    # Hero
    hero = Hero(
        "Deploy Python Web Apps in Seconds",
        subtitle="The all-in-one platform for FastHTML and Python developers. No more infrastructure headaches.",
        cta=Div(
            Button("Get Started", variant="primary", size="lg", cls="me-1"),
            Button("Book a Demo", variant="outline-primary", size="lg"),
        ),
        align="start",
        py="5",
        container=True,
        cls="bg-white",
    )

    # Features Section (3 columns on desktop)
    features = Section(
        Container(
            H2("Why FastCloud?", cls="text-center mb-5"),
            Row(
                render_feature(
                    "lightning",
                    "Instant Deployment",
                    "Push your code and we handle the build & hosting automatically.",
                ),
                render_feature(
                    "shield-check",
                    "Enterprise Security",
                    "SSL, DDoS protection, and isolated environments out of the box.",
                ),
                render_feature(
                    "graph-up",
                    "Autoscaling",
                    "Your app scales with your traffic. Only pay for what you use.",
                ),
            ),
        ),
        cls="py-5 bg-light",
    )

    # Metric Section (3 columns on desktop)
    metrics = Section(
        Container(
            Row(
                Col(
                    StatCard("Active Workers", "1,200+", trend="+15%", trend_type="up"),
                    md=4,
                    cls="mb-4",
                ),
                Col(
                    StatCard("Build Time (Avg)", "42s", trend="-2s", trend_type="up"),
                    md=4,
                    cls="mb-4",
                ),
                Col(StatCard("Uptime", "99.99%", trend="Stable"), md=4, cls="mb-4"),
            )
        ),
        cls="py-5",
    )

    # FAQ Section (Accordion)
    faq = Section(
        Container(
            H2("Frequently Asked Questions", cls="text-center mb-5"),
            Accordion(
                AccordionItem(
                    "We support all major versions of Python from 3.10 upwards.",
                    title="What Python versions are supported?",
                ),
                AccordionItem(
                    "Yes! Our free tier includes 1GB of bandwidth and 512MB RAM.",
                    title="Is there a free tier?",
                ),
                AccordionItem(
                    "Simply connect your repository and we'll auto-detect your FastHTML app.",
                    title="How do I migrate from Heroku?",
                ),
                accordion_id="faq-acc",
                flush=True,
                cls="mx-auto",
                style="max-width: 800px;",
            ),
        ),
        cls="py-5 bg-light",
    )

    # Footer
    footer = Div(
        Container(
            P("© 2026 FastCloud Inc. All rights reserved.", cls="text-muted mb-0"),
            cls="text-center",
        ),
        cls="py-4 border-top",
    )

    return Title("FastCloud SaaS"), Main(nav, hero, features, metrics, faq, footer)


app = FastHTML()
add_bootstrap(app)


@app.route("/")
def get():
    return home()


if __name__ == "__main__":
    serve()
