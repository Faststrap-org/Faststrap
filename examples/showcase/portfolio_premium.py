from fasthtml.common import *

from faststrap import *


def render_achievement(title, value, icon):
    return Col(
        StatCard(
            title,
            value,
            icon=Icon(icon),
            variant="dark",
            inverse=True,
            cls="h-100 border-secondary",
        ),
        md=4,
        cls="mb-4",
    )


def home():
    # Navbar (Transparent effect)
    nav = Navbar(
        A("Showcase", href="#", cls="nav-link"),
        A("Expertise", href="#", cls="nav-link"),
        brand="CREATIVESTUDIO",
        expand="lg",
        variant="dark",
        bg="dark",
        sticky="top",
    )

    # Premium Hero with Background Image (Mockup)
    hero = Hero(
        "Design the Future",
        subtitle="We blend high-performance engineering with world-class aesthetics. Delivering digital experiences that leave a mark.",
        cta=Button("Start a Project", variant="primary", size="lg", cls="px-5"),
        bg_variant="dark",
        align="center",
        py="5",
        style="background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), url('https://images.unsplash.com/photo-1497215728101-856f4ea42174?auto=format&fit=crop&w=1920&q=80'); background-size: cover; background-position: center; min-height: 80vh; display: flex; align-items: center;",
    )

    # Stats Section (3 columns on desktop, 1 on mobile)
    stats = Section(
        Container(
            Row(
                render_achievement("Projects Delivered", "120+", "check-circle"),
                render_achievement("Coffee Consumed", "4.2k", "cup-hot"),
                render_achievement("Happy Clients", "85", "emoji-smile"),
            )
        ),
        cls="py-5 bg-dark",
    )

    # Featured Work (3 columns on desktop, 1 on mobile)
    work = Section(
        Container(
            H2("Featured Works", cls="text-center text-white mb-5"),
            Row(
                Col(
                    Card(
                        "UI/UX improvement for global retailer.",
                        title="E-Commerce Redesign",
                        img_top="https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=400&q=80",
                        cls="bg-dark text-white border-secondary mb-4",
                    ),
                    md=4,
                ),
                Col(
                    Card(
                        "Complex data viz for banking platform.",
                        title="FinTech Dashboard",
                        img_top="https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=400&q=80",
                        cls="bg-dark text-white border-secondary mb-4",
                    ),
                    md=4,
                ),
                Col(
                    Card(
                        "Optimizing workflows for teams.",
                        title="Developer Tooling",
                        img_top="https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&w=400&q=80",
                        cls="bg-dark text-white border-secondary mb-4",
                    ),
                    md=4,
                ),
            ),
        ),
        cls="py-5 bg-black",
    )

    return Title("Premium Portfolio"), Main(nav, hero, stats, work)


app = FastHTML()
add_bootstrap(app, theme="green-nature", mode="dark")


@app.route("/")
def get():
    return home()


if __name__ == "__main__":
    serve()
