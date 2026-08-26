from fasthtml.common import FastHTML, Div, H1, H4, P, Hr, Section, Titled, serve
from faststrap import (
    add_bootstrap,
    create_theme,
    Container,
    Card,
    Row,
    Col,
    Button,
    Badge,
    Spinner,
    Progress,
)

# 1. Define a custom theme using the factory function
my_custom_theme = create_theme(
    primary="#ffd700",  # Gold
    secondary="#2c3e50",  # Dark Blue/Slate
    success="#27ae60",
    info="#2980b9",
    warning="#f39c12",
    danger="#c0392b",
    light="#f8f9fa",
    dark="#2c3e50",  # Custom dark background
)

# 2. Initialize the app
app = FastHTML()

# 3. Add Bootstrap ONCE at the app level with "auto" mode.
# This generates CSS for both light and dark modes, allowing instant toggling
# by just changing the 'data-bs-theme' attribute on the <html> tag.
add_bootstrap(app, theme=my_custom_theme, mode="auto")


@app.route("/")
def home():
    return Titled(
        "Faststrap Custom Themes",
        Container(
            H1("Custom Theme: Midnight Gold", cls="mb-4"),
            Card(
                Section(
                    P("This example shows a completely custom theme defined in Python."),
                    P("Toggling is instantaneous - no server request needed!"),
                    Div(
                        # Direct client-side attribute update for 'Wow' speed
                        Button(
                            "Light Mode",
                            onclick="document.documentElement.setAttribute('data-bs-theme', 'light')",
                            variant="light",
                            cls="me-2",
                        ),
                        Button(
                            "Dark Mode",
                            onclick="document.documentElement.setAttribute('data-bs-theme', 'dark')",
                            variant="dark",
                            cls="me-2",
                        ),
                        cls="mb-4",
                    ),
                    Hr(),
                    Row(
                        Col(
                            H4("Custom Primary (Gold)"),
                            Button("Gold Button", variant="primary", size="lg"),
                            P(
                                "The theme now overrides standard Bootstrap colors.",
                                cls="mt-2 text-muted",
                            ),
                            span=12,
                            md=6,
                        ),
                        Col(
                            H4("Components"),
                            Badge("Custom Badge", variant="primary", cls="me-1"),
                            Spinner(variant="primary"),
                            Progress(
                                75, variant="primary", striped=True, animated=True, cls="mt-3"
                            ),
                            span=12,
                            md=6,
                        ),
                        g=3,
                    ),
                    cls="p-4",
                )
            ),
            cls="mt-5",
        ),
    )


if __name__ == "__main__":
    serve()
