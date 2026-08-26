from fasthtml.common import (
    A,
    Div,
    FastHTML,
    H2,
    H5,
    Main,
    P,
    Section,
    Title,
    serve,
)

from faststrap import (
    Badge,
    Button,
    Card,
    Col,
    Container,
    Hero,
    Navbar,
    Row,
    add_bootstrap,
)


def render_project(title, desc, tags):
    return Card(
        P(desc),
        header=H5(title),
        footer=Div(*[Badge(t, variant="secondary", cls="me-1") for t in tags]),
        cls="h-100 shadow-sm",
    )


def home():
    # Navbar
    nav = Navbar(
        A("Home", href="#", cls="nav-link active"),
        A("Projects", href="#projects", cls="nav-link"),
        A("About", href="#about", cls="nav-link"),
        A("Contact", href="#contact", cls="nav-link"),
        brand="John Doe",
        expand="lg",
        sticky="top",
        bg="white",
        variant="light",
        cls="border-bottom",
    )

    # Hero
    hero = Hero(
        "Hi, I'm John Doe",
        subtitle="A Full-Stack Developer specializing in Python and FastHTML. Building high-performance web applications with minimal effort.",
        cta=Button("View My Work", href="#projects", variant="primary", size="lg"),
        align="center",
        py="5",
        cls="bg-light",
    )

    # Projects (3 columns on desktop, 1 on mobile)
    projects = Section(
        Container(
            H2("Projects", id="projects", cls="text-center mb-5"),
            Row(
                Col(
                    render_project(
                        "FastStrap",
                        "A Bootstrap components library for FastHTML",
                        ["Python", "Bootstrap", "HTMX"],
                    ),
                    md=4,
                    cls="mb-4",
                ),
                Col(
                    render_project(
                        "CyberDash",
                        "A security monitoring dashboard with real-time alerts",
                        ["FastAPI", "Redis", "D3.js"],
                    ),
                    md=4,
                    cls="mb-4",
                ),
                Col(
                    render_project(
                        "PyFolio",
                        "Automated portfolio generator for developers",
                        ["Markdown", "CI/CD"],
                    ),
                    md=4,
                    cls="mb-4",
                ),
            ),
        ),
        cls="py-5",
    )

    # Skills (using Badges)
    skills = Section(
        Container(
            H2("Skills", cls="text-center mb-4"),
            Div(
                Badge("Python", variant="primary", pill=True, cls="fs-5 m-1"),
                Badge("FastHTML", variant="info", pill=True, cls="fs-5 m-1"),
                Badge("Bootstrap", variant="purple", pill=True, cls="fs-5 m-1"),
                Badge("HTMX", variant="success", pill=True, cls="fs-5 m-1"),
                Badge("PostgreSQL", variant="dark", pill=True, cls="fs-5 m-1"),
                Badge("Docker", variant="secondary", pill=True, cls="fs-5 m-1"),
                cls="text-center",
            ),
        ),
        cls="py-5 bg-white",
    )

    # Footer
    footer = Div(
        Container(
            P("© 2026 John Doe. Built with FastStrap.", cls="text-muted mb-0"), cls="text-center"
        ),
        cls="py-4 border-top",
    )

    return Title("John Doe Portfolio"), Main(nav, hero, projects, skills, footer)


app = FastHTML()
add_bootstrap(app)


@app.route("/")
def get():
    return home()


if __name__ == "__main__":
    serve()
