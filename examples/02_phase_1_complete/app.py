"""Phase 1 Complete Demo - All Components Working."""

from fasthtml.common import FastHTML, Div, H1, H2, P, serve
from faststrap import (
    add_bootstrap,
    Button,
    Badge,
    Alert,
    Card,
    Container,
    Row,
    Col,
    Icon,
)

app = FastHTML()
add_bootstrap(app, theme="light")


@app.route("/")
def home():
    return Container(
        H1("FastStrap Phase 1 Complete! 🎉", cls="mb-4"),
        P("All 5 Phase 1 components are working!", cls="lead mb-5"),
        
        # Buttons Section
        Div(
            H2("Buttons", cls="h4 mb-3"),
            Div(
                Button("Primary"),
                Button("Success", variant="success"),
                Button("Danger", variant="danger"),
                Button("With Icon", icon="heart-fill", variant="info"),
                Button("Loading", loading=True, variant="warning"),
                cls="d-flex gap-2 flex-wrap mb-4"
            ),
        ),
        
        # Badges Section
        Div(
            H2("Badges", cls="h4 mb-3"),
            Div(
                Badge("New", variant="primary"),
                Badge("99+", variant="danger", pill=True),
                Badge(Icon("star-fill"), " Featured", variant="warning"),
                Badge("Sale", variant="success"),
                cls="d-flex gap-2 align-items-center mb-4"
            ),
        ),
        
        # Alerts Section
        Div(
            H2("Alerts", cls="h4 mb-3"),
            Alert("Success! Your changes were saved.", variant="success"),
            Alert(
                "Warning: Low disk space.",
                variant="warning",
                heading="Storage Alert",
                dismissible=True
            ),
            Alert("Info: New features available.", variant="info"),
            cls="mb-4"
        ),
        
        # Cards Section
        Div(
            H2("Cards", cls="h4 mb-3"),
            Row(
                Col(
                    Card(
                        "Basic card with title and content.",
                        title="Simple Card",
                        cls="h-100"
                    ),
                    span=12, md=4
                ),
                Col(
                    Card(
                        "Card with header, title, and footer.",
                        title="Featured Card",
                        header="Featured",
                        footer="Last updated 3 mins ago",
                        cls="h-100"
                    ),
                    span=12, md=4
                ),
                Col(
                    Card(
                        P("Card with all options enabled."),
                        Button("Action", variant="primary"),
                        title="Complete Card",
                        subtitle="With subtitle",
                        header=Badge("New", variant="success"),
                        footer="Card footer",
                        cls="h-100"
                    ),
                    span=12, md=4
                ),
                cls="mb-4"
            ),
        ),
        
        # Grid Section
        Div(
            H2("Grid System", cls="h4 mb-3"),
            Row(
                Col(Div("Col 1", cls="border p-3 text-center bg-light"), span=4),
                Col(Div("Col 2", cls="border p-3 text-center bg-light"), span=4),
                Col(Div("Col 3", cls="border p-3 text-center bg-light"), span=4),
            ),
            Row(
                Col(
                    Div("Full width on mobile, half on tablet", cls="border p-3 text-center bg-light"),
                    span=12, md=6
                ),
                Col(
                    Div("Full width on mobile, half on tablet", cls="border p-3 text-center bg-light"),
                    span=12, md=6
                ),
                cls="mt-3"
            ),
        ),
        
        cls="py-5"
    )


if __name__ == "__main__":
    print("🚀 FastStrap Phase 1 Complete Demo")
    print("📍 Visit: http://localhost:5001")
    print("\n✅ Components included:")
    print("   - Button (with variants, sizes, icons, loading)")
    print("   - Badge (with pill style)")
    print("   - Alert (with dismissible, heading)")
    print("   - Card (with header, footer, images)")
    print("   - Grid (Container, Row, Col with responsive layout)")
    serve()