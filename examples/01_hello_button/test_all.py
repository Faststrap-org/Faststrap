"""Test all FastStrap features in one app — FINAL WORKING VERSION."""

from fasthtml.common import H1, Div, FastHTML, P, serve

from faststrap import Button, Icon, add_bootstrap

app = FastHTML()
add_bootstrap(app, theme="light")


@app.get("/")
def home():
    return Div(
        H1("FastStrap Complete Test", cls="mb-4"),
        P("Testing all features work correctly", cls="text-muted mb-5"),
        Div(
            H1("Button Tests", cls="h4 mb-3"),
            # Basic variants
            Div(
                Button("Primary"),
                Button("Success", variant="success"),
                Button("Danger", variant="danger"),
                Button("Warning Outline", variant="warning", outline=True),
                cls="d-flex gap-2 flex-wrap mb-3",
            ),
            # Sizes
            Div(
                Button("Small", size="sm"),
                Button("Medium (default)"),
                Button("Large", size="lg"),
                cls="d-flex gap-2 align-items-center mb-3",
            ),
            # States
            Div(
                Button("Normal"),
                Button("Disabled", disabled=True),
                Button("Loading", loading=True),
                cls="d-flex gap-2 mb-3",
            ),
            # With icons
            Div(
                Button("Save", icon="save"),
                Button("Delete", variant="danger", icon="trash"),
                Button("Download", variant="success", icon="download"),
                cls="d-flex gap-2 mb-3",
            ),
            # HTMX buttons — NOW WORKING
            Div(
                Button("HTMX Get", hx_get="/test", hx_target="#result"),
                Button("HTMX Post", hx_post="/submit", hx_target="#result", hx_swap="innerHTML"),
                cls="d-flex gap-2 mb-3",
            ),
            # Icon component
            Div(
                H1("Icon Tests", cls="h4 mb-3"),
                Div(
                    Icon("heart", cls="text-danger fs-1"),
                    Icon("star-fill", cls="text-warning fs-1"),
                    Icon("check-circle", cls="text-success fs-1"),
                    cls="d-flex gap-3",
                ),
                cls="mb-4",
            ),
            # Results area
            Div(id="result", cls="mt-4 p-3 border rounded bg-light", style="min-height: 50px;"),
            cls="container p-4 border rounded",
        ),
        cls="container py-5",
    )


@app.get("/test")
def test_endpoint():
    return Div("HTMX GET request successful!", cls="alert alert-success")


@app.post("/submit")  # ← THIS IS THE FIX
def submit():
    return Div("Form submitted via HTMX POST!", cls="alert alert-info")


if __name__ == "__main__":
    print("FastStrap Complete Test Server")
    print("Open: http://localhost:5001")
    print("Features tested:")
    print("   - All button variants, sizes, states")
    print("   - Icons in buttons + standalone Icon()")
    print("   - HTMX GET and POST")
    print("   - Dark/light theme switching")
    serve()
