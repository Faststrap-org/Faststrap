"""
Example: Adding HTMX

Demonstrates: HTMX integration with Faststrap
Components: Button, Card, Spinner, Alert
Difficulty: Beginner

Learn how to add interactivity without JavaScript using HTMX.
"""

import time

from fasthtml.common import *

from faststrap import *

app = FastHTML()
add_bootstrap(app)


@app.get("/")
def home():
    return Container(
        H1("HTMX Examples", cls="mb-4"),
        Row(
            # Click to Load
            Col(
                Card(
                    H5("Click to Load", cls="card-title"),
                    P("Click the button to load content from the server.", cls="card-text"),
                    Button(
                        "Load Content",
                        variant="primary",
                        hx_get="/load-content",
                        hx_target="#content-area",
                        hx_swap="innerHTML",
                    ),
                    Div(id="content-area", cls="mt-3"),
                ),
                md=6,
            ),
            # Live Search
            Col(
                Card(
                    H5("Live Search", cls="card-title"),
                    Input(
                        "search",
                        placeholder="Type to search...",
                        hx_get="/search",
                        hx_trigger="keyup changed delay:500ms",
                        hx_target="#search-results",
                    ),
                    Div(id="search-results", cls="mt-3"),
                ),
                md=6,
            ),
        ),
        # Counter Example
        Card(
            H5("Interactive Counter", cls="card-title"),
            Div(
                H2("0", id="counter", cls="text-center my-3"),
                Div(
                    Button(
                        "Decrease",
                        variant="danger",
                        hx_post="/counter/decrease",
                        hx_target="#counter",
                        hx_swap="innerHTML",
                    ),
                    Button(
                        "Increase",
                        variant="success",
                        hx_post="/counter/increase",
                        hx_target="#counter",
                        hx_swap="innerHTML",
                    ),
                    cls="d-flex gap-2 justify-content-center",
                ),
            ),
            cls="mt-4",
        ),
        cls="py-5",
    )


# Counter state (in production, use session or database)
counter_value = 0


@app.get("/load-content")
def load_content():
    time.sleep(0.5)  # Simulate loading
    return Alert("Content loaded successfully from the server!", variant="success")


@app.get("/search")
def search(search: str = ""):
    if not search:
        return P("Start typing to see results...", cls="text-muted")

    # Simulate search results
    results = [f"Result for '{search}' #{i}" for i in range(1, 4)]
    return Div(*[P(result, cls="mb-1") for result in results], cls="border p-2 rounded")


@app.post("/counter/increase")
def increase():
    global counter_value
    counter_value += 1
    return str(counter_value)


@app.post("/counter/decrease")
def decrease():
    global counter_value
    counter_value -= 1
    return str(counter_value)


if __name__ == "__main__":
    serve(port=5019)
