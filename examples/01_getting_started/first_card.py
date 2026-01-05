"""
Example: First Card

Demonstrates: Working with Card components
Components: Card, Badge, Button, Icon
Difficulty: Beginner

Learn how to create and customize Cards - one of the most versatile components.
"""

from fasthtml.common import *

from faststrap import *

app = FastHTML()
add_bootstrap(app)


@app.route("/")
def get():
    return Container(
        H1("Card Component Examples", cls="mb-4"),
        Row(
            # Basic Card
            Col(
                Card(
                    H5("Basic Card", cls="card-title"),
                    P("This is a simple card with a title and text.", cls="card-text"),
                    Button("Learn More", variant="primary"),
                ),
                md=4,
            ),
            # Card with Image
            Col(
                Card(
                    Img(src="https://placehold.co/400x200", cls="card-img-top"),
                    Div(
                        H5("Card with Image", cls="card-title"),
                        P("Cards can have images at the top.", cls="card-text"),
                        Button("View", variant="outline-primary"),
                        cls="card-body",
                    ),
                ),
                md=4,
            ),
            # Card with Badge and Icon
            Col(
                Card(
                    Div(
                        Icon("star-fill", cls="text-warning fs-1 mb-3"),
                        H5("Premium Feature", cls="card-title"),
                        Badge("New", variant="success", cls="mb-2"),
                        P("This card has icons and badges.", cls="card-text"),
                        Button("Upgrade", variant="warning"),
                        cls="text-center",
                    )
                ),
                md=4,
            ),
        ),
        cls="py-5",
    )


if __name__ == "__main__":
    serve(port=5019)
