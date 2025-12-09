"""Phase 1 + 2 Complete Demo - All 12 Components Working."""

from fasthtml.common import H1, H2, A, Div, FastHTML, P, serve

from faststrap import (
    # Feedback
    Alert,
    # Display
    Badge,
    # Forms
    Button,
    ButtonGroup,
    Card,
    Col,
    # Layout
    Container,
    # Navigation
    Drawer,
    # Utils
    Modal,
    Navbar,
    Row,
    Toast,
    ToastContainer,
    add_bootstrap,
)

app = FastHTML()
add_bootstrap(app, theme="dark", use_cdn=True)


@app.route("/")
def home():
    return Div(
        # Navbar at top
        Navbar(
            Div(
                A("Home", href="/", cls="nav-link active"),
                A("Features", href="#features", cls="nav-link"),
                A("About", href="#about", cls="nav-link"),
                cls="navbar-nav me-auto",
            ),
            Div(Button("Login", variant="outline-primary", size="sm"), cls="d-flex"),
            brand="FastStrap",
            variant="dark",
            bg="dark",
            expand="lg",
        ),
        # Toast container (top-right)
        ToastContainer(
            Toast(
                "Welcome to FastStrap v0.2.0!",
                title="Success",
                variant="success",
                id="welcomeToast",
            ),
            position="top-end",
        ),
        # Main content
        Container(
            H1("FastStrap Phase 1 + 2 Complete!", cls="my-5"),
            P("All 12 components from Phase 1 and Phase 2 are working!", cls="lead mb-5"),
            # Modal trigger
            Button(
                "Open Modal",
                variant="primary",
                data_bs_toggle="modal",
                data_bs_target="#demoModal",
                cls="mb-4",
            ),
            # Drawer trigger
            Button(
                "Open Drawer",
                variant="secondary",
                data_bs_toggle="offcanvas",
                data_bs_target="#demoDrawer",
                cls="mb-4 ms-2",
            ),
            # ButtonGroup Section
            Div(
                H2("Button Groups", cls="h4 mb-3"),
                ButtonGroup(
                    Button("Left", variant="outline-primary"),
                    Button("Middle", variant="outline-primary"),
                    Button("Right", variant="outline-primary"),
                ),
                ButtonGroup(
                    Button("Top", variant="secondary"),
                    Button("Middle", variant="secondary"),
                    Button("Bottom", variant="secondary"),
                    vertical=True,
                    cls="ms-3",
                ),
                cls="mb-5",
            ),
            # Cards with Badges
            Row(
                Col(
                    Card(
                        P("Interactive card with modal trigger"),
                        Button(
                            "View Details",
                            variant="primary",
                            data_bs_toggle="modal",
                            data_bs_target="#demoModal",
                        ),
                        title="Card 1",
                        header=Badge("Featured", variant="success"),
                        cls="h-100",
                    ),
                    span=12,
                    md=4,
                ),
                Col(
                    Card(
                        P("Another card with badge"),
                        title="Card 2",
                        subtitle="With subtitle",
                        footer=Badge("99+", variant="danger", pill=True),
                        cls="h-100",
                    ),
                    span=12,
                    md=4,
                ),
                Col(
                    Card(
                        Alert("Card with alert inside!", variant="info"),
                        title="Card 3",
                        cls="h-100",
                    ),
                    span=12,
                    md=4,
                ),
                cls="mb-5",
            ),
            cls="py-5",
        ),
        # Modal (hidden by default)
        Modal(
            P("This is a modal dialog with Bootstrap JS!"),
            P("Click outside or press ESC to close."),
            modal_id="demoModal",
            title="Demo Modal",
            footer=Div(
                Button("Close", variant="secondary", data_bs_dismiss="modal"),
                Button("Save Changes", variant="primary"),
            ),
        ),
        # Drawer (hidden by default)
        Drawer(
            Div(
                H2("Menu", cls="h5 mb-3"),
                A("Dashboard", href="/dashboard", cls="d-block mb-2"),
                A("Settings", href="/settings", cls="d-block mb-2"),
                A("Profile", href="/profile", cls="d-block mb-2"),
                A("Logout", href="/logout", cls="d-block text-danger"),
            ),
            drawer_id="demoDrawer",
            title="Navigation",
            placement="start",
        ),
    )


if __name__ == "__main__":
    print("🚀 FastStrap Phase 1 + 2 Complete Demo")
    print("📍 Visit: http://localhost:5001")
    print("\n✅ Phase 1 Components (5):")
    print("   - Button, Badge, Alert, Card, Grid")
    print("\n✅ Phase 2 Components (5):")
    print("   - Toast, Modal, Drawer, Navbar, ButtonGroup")
    print("\n🎯 Total: 12 Components Ready for v0.2.0!")
    serve()
