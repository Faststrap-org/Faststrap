from fasthtml.common import FastHTML, Div, H2, H4, P, Hr, Section, Titled, serve
from faststrap import add_bootstrap, Container, Card, Row, Col, Button, Badge, Alert

# 1. Initialize the app
app = FastHTML()

# 2. Add Bootstrap ONCE at the app level
# Faststrap provides built-in themes: blue-ocean, purple-magic, green-nature, indigo-night, etc.
# The mode="auto" generates CSS that works for light, dark, and system preference.
add_bootstrap(app, theme="blue-ocean", mode="auto")


@app.route("/")
def home():
    return Titled(
        "Faststrap Built-in Themes",
        Container(
            Card(
                Section(
                    H2("Built-in Theme: Blue Ocean"),
                    P(
                        "This example demonstrates instantaneous toggling between light and dark modes."
                    ),
                    Div(
                        # Direct client-side attribute update for 'Wow' speed
                        Button(
                            "Switch to Light",
                            onclick="document.documentElement.setAttribute('data-bs-theme', 'light')",
                            variant="light",
                            cls="me-2",
                        ),
                        Button(
                            "Switch to Dark",
                            onclick="document.documentElement.setAttribute('data-bs-theme', 'dark')",
                            variant="dark",
                            cls="me-2",
                        ),
                        cls="mb-4",
                    ),
                    Hr(),
                    Row(
                        Col(
                            H4("Buttons"),
                            Div(
                                Button("Primary", variant="primary", cls="me-1"),
                                Button("Secondary", variant="secondary", cls="me-1"),
                                Button("Success", variant="success", cls="me-1"),
                                Button("Danger", variant="danger", cls="me-1"),
                                cls="mb-3",
                            ),
                            H4("Badges"),
                            Div(
                                Badge("New", variant="primary", cls="me-1"),
                                Badge("Update", variant="success", pill=True, cls="me-1"),
                                Badge("Alert", variant="danger", cls="me-1"),
                            ),
                            span=12,
                            md=6,
                        ),
                        Col(
                            H4("Alerts"),
                            Alert("This is a success alert!", variant="success"),
                            Alert("Be careful with this one.", variant="warning"),
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
