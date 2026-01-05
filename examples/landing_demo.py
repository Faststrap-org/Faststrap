"""Faststrap LandingLayout Demo.

Showcasing a clean full-width layout optimized for marketing sites.
"""

from fasthtml.common import H2, A, Div, FastHTML, Footer, P, serve

from faststrap import Button, Fx, Hero, Icon, LandingLayout, NavbarModern, add_bootstrap

app = FastHTML()
add_bootstrap(app, theme="green-nature", font_family="Inter")


@app.route("/")
def home():
    # Modern Glass Navbar
    nav = NavbarModern(
        brand=Div(Icon("lightning-fill", cls="me-2 text-success"), "FastCloud"),
        items=[
            A("Features", href="#", cls="nav-link"),
            A("Pricing", href="#", cls="nav-link"),
            Button("Launch App", cls="btn-success ms-lg-3"),
        ],
        glass=True,
    )

    # Hero Section
    hero = Hero(
        title="Deploy Your FastHTML Apps Globally",
        subtitle="The fastest way to go from local development to production with zero-JS layouts.",
        cta=Div(
            Button("Start Free Trial", cls="btn-success btn-lg px-5 me-2"),
            Button("Contact Sales", cls="btn-outline-success btn-lg px-5"),
            cls="d-flex justify-content-center mt-4",
        ),
        cls=f"{Fx.fade_in_up}",
    )

    # Simple Content Card
    content = Div(
        H2("Optimized for Performance", cls="text-center mb-4"),
        P(
            "FastCloud uses Faststrap's LandingLayout to ensure your marketing pages load instantly and look premium without a single line of custom JavaScript.",
            cls="lead text-center",
        ),
        cls="py-5",
    )

    footer = Footer(
        Div(
            Div("© 2026 FastCloud. Powered by Faststrap.", cls="text-muted"),
            cls="container text-center py-4 border-top mt-5",
        )
    )

    return LandingLayout(hero, content, navbar=nav, footer=footer)


if __name__ == "__main__":
    serve(port=5013)
