"""
Faststrap v0.9.0 Navigation Demo

Demonstrates navigation components:
- SearchBar: global search input with HTMX support
- ProfileDropdown: authenticated user menu
"""

from fasthtml.common import FastHTML, Div, H1, P, Ul, Li, A, Small, serve
from faststrap import add_bootstrap, Container, Navbar, SearchBar, ProfileDropdown

app = FastHTML()
add_bootstrap(app, theme="indigo-night", mode="light")


@app.get("/")
def home():
    return Container(
        Navbar(
            SearchBar(
                placeholder="Search components...",
                endpoint="/search",
                target="#search-results",
                cls="ms-auto me-3",
            ),
            ProfileDropdown(
                "Alex Developer",
                subtitle="alex@example.com",
                items=[
                    ("Profile", "/profile"),
                    ("Settings", "/settings"),
                    ("Sign out", "/logout"),
                ],
            ),
            brand="Faststrap v0.9.0",
            brand_href="/",
        ),
        Div(id="search-results", cls="mt-3"),
        H1("Navigation Components", cls="display-5 fw-bold mb-4 mt-4"),
        P(
            "SearchBar provides a polished global search input with optional HTMX integration. "
            "ProfileDropdown renders an authenticated user menu with avatar/initials and action links.",
            cls="lead text-muted",
        ),
        cls="my-5",
    )


@app.get("/search")
def search(q: str = ""):
    results = [
        ("Button", "Standard actions and loading states"),
        ("Card", "Base content surface"),
        ("DataTable", "Search, sort, and pagination"),
        ("Input", "Text inputs and textareas"),
        ("Modal", "Bootstrap modal wrapper"),
        ("Navbar", "Standard Bootstrap navbar"),
    ]
    if not q:
        return P("Type something to search...", cls="text-muted")
    filtered = [(name, desc) for name, desc in results if q.lower() in name.lower()]
    if not filtered:
        return P(f"No results for '{q}'", cls="text-muted")
    return Ul(
        *[
            Li(
                A(name, href=f"/docs/components/{name.lower()}", cls="text-decoration-none"),
                Small(desc, cls="text-muted d-block"),
            )
            for name, desc in filtered
        ],
        cls="list-unstyled",
    )


if __name__ == '__main__':
    serve()
