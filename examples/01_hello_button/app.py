"""Hello Button - Minimal FastStrap example."""

from fasthtml.common import H1, Div, FastHTML, P, serve

from faststrap import Button, add_bootstrap

app = FastHTML()
add_bootstrap(app, theme="dark")


@app.route("/")
def home():
    return Div(
        H1("Welcome to FastStrap! 🚀"),
        P("Beautiful Bootstrap components in pure Python"),
        Div(
            Button("Primary", variant="primary"),
            Button("Success", variant="success"),
            Button("Danger", variant="danger"),
            Button("With Icon", variant="info", icon="heart-fill"),
            Button("Loading", variant="warning", loading=True),
            cls="d-flex gap-2 flex-wrap",
        ),
        cls="container mt-5",
    )


if __name__ == "__main__":
    serve()
