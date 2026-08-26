import time

from fasthtml.common import H1, H2, H3, A, Button, Div, FastHTML, Form, Label, P, Style, serve

# Import ALL components from the completed FastStrap library
from faststrap import (
    # Feedback & Modals
    Alert,
    # Display & Icons
    Breadcrumb,
    ButtonGroup,
    Card,
    Col,
    # Layout & Containers
    Container,
    Drawer,
    Dropdown,
    Icon,
    # Forms
    Input,
    Modal,
    # Navigation & Interaction
    Navbar,
    Pagination,
    Progress,
    Row,
    Select,
    Spinner,
    TabPane,
    Tabs,
    Toast,
    ToastContainer,
    # Core
    add_bootstrap,
)

# --- Configuration ---
APP_TITLE = "FastAuth SaaS Platform"
custom_css = """
    body { background-color: #121212; }
    .card { background-color: #1e1e1e; border-color: #333; }
    .text-white-60 { color: rgba(255, 255, 255, 0.6); }
    .hero-section { background-color: #1a1a1a; }
    """
hdrs = Style(custom_css)

app = FastHTML(title=APP_TITLE, hdrs=hdrs)
add_bootstrap(app)

# --- Components ---


def signup_form() -> Form:
    """A login form built with Input, Select, and ButtonGroup components."""
    return Form(
        Input(
            "email",
            input_type="email",
            label="Email Address",
            placeholder="Your work email",
            help_text="We'll send a magic link.",
            required=True,
        ),
        Input(
            "name",
            label="Full Name",
            placeholder="Jane Doe",
            required=True,
        ),
        Select(
            "role",
            ("eng", "Engineer", True),
            ("des", "Designer"),
            ("mgt", "Manager"),
            label="Your Role",
        ),
        ButtonGroup(
            Button(
                "Sign Up",
                variant="primary",
                hx_post="/signup",
                hx_target="#signup-status",
                cls="shadow",
            ),
            Button("Login", variant="outline-light", cls="shadow-sm"),
            cls="mt-4",
        ),
        Div(id="signup-status", cls="mt-3"),
        cls="p-4",
    )


def feature_tabs() -> Div:
    """A feature showcase using Tabs and TabPane components."""
    return Div(
        H3("Key Features", cls="h4 mb-4 text-white-60"),
        Tabs(
            ("tab-1", "Authentication", True),
            ("tab-2", "Storage"),
            ("tab-3", "Analytics"),
            variant="pills",
            align="center",
            cls="mb-3",
        ),
        Div(
            TabPane(
                Div(
                    Icon("shield-fill-check", cls="display-4 text-success mb-3"),
                    P(
                        "Secure, fast, and multi-factor authentication built-in.",
                        cls="text-white-60",
                    ),
                    Button("Read Docs", variant="link", size="sm"),
                ),
                tab_id="tab-1",
                active=True,
            ),
            TabPane(
                Div(
                    Icon("server", cls="display-4 text-primary mb-3"),
                    P("Globally distributed, low-latency data storage.", cls="text-white-60"),
                ),
                tab_id="tab-2",
            ),
            TabPane(
                Div(
                    Icon("graph-up", cls="display-4 text-warning mb-3"),
                    P("Real-time data visualization and metrics.", cls="text-white-60"),
                ),
                tab_id="tab-3",
            ),
            cls="tab-content text-center py-4 bg-dark rounded shadow-lg",
        ),
    )


# --- Routes ---


@app.route("/")
def home():
    """Main application layout."""
    return Div(
        # Top Navigation Bar
        Navbar(
            A("Features", href="#features", cls="nav-link"),
            Dropdown(
                "Docs",
                "API Reference",
                "Support",
                "---",
                "Status",
                label="Help Center",
                variant="outline-primary",
                size="sm",
                cls="ms-2",
            ),
            brand="FastAuth",
            brand_href="/",
            variant="dark",
            bg="dark",
            expand="lg",
            cls="shadow-lg mb-0 border-bottom border-secondary",
        ),
        # Main Hero Section
        Container(
            Breadcrumb(("Home", "/"), ("Get Started", None)),
            Row(
                # Column 1: Feature Showcase (7 columns wide on large screens)
                Col(
                    Div(
                        H1("Build Faster. Ship Sooner.", cls="display-4 fw-bold text-white mb-3"),
                        P(
                            "The only platform you need for Authentication, Storage, and Analytics. Start free.",
                            cls="lead text-white-60 mb-5",
                        ),
                        # Loading/Progress Indicators
                        H3("System Status", cls="h5 mt-5 mb-3 text-white-60"),
                        Progress(
                            100,
                            variant="success",
                            label="System Online",
                            striped=True,
                            animated=True,
                        ),
                        Div(
                            Spinner(variant="success", size="sm", cls="me-2 mt-3"),
                            Label("Live Monitoring...", cls="text-success small"),
                        ),
                    ),
                    span=12,
                    lg=7,
                    cls="py-5",
                ),
                # Column 2: Sign-up Card (5 columns wide on large screens)
                Col(
                    Card(
                        H2("Create Account", cls="h3 mb-4 text-center text-white"),
                        signup_form(),
                        footer=P(
                            "Already a user?",
                            A("Sign In", href="/login", cls="ms-1"),
                            cls="small text-center",
                        ),
                        cls="shadow-lg h-100",
                    ),
                    span=12,
                    lg=5,
                    cls="d-flex align-items-center justify-content-center py-5",
                ),
            ),
        ),
        # Secondary Feature Section
        Container(
            Div(id="features", cls="mt-5 pt-5"),
            Row(Col(feature_tabs(), span=12, lg=8, cls="mx-auto")),
            # Additional Components (Modal Trigger, Pagination, Alert)
            Div(
                Button(
                    Icon("info-circle", cls="me-2"),
                    "See License Details",
                    variant="info",
                    data_bs_toggle="modal",
                    data_bs_target="#licenseModal",
                    cls="mt-5 shadow-sm",
                ),
                Pagination(current_page=2, total_pages=5, align="end", size="sm", cls="mt-5"),
                Alert(
                    Icon("exclamation-triangle-fill", cls="me-2"),
                    "The demo environment is running v0.3.0 of FastStrap. Performance may vary.",
                    variant="warning",
                    cls="mt-5",
                ),
                cls="py-5",
            ),
        ),
        # Hidden Components (Modal, Toast, Drawer)
        Modal(
            P("FastAuth operates under a permissive MIT license."),
            P("This ensures maximum flexibility for your projects."),
            modal_id="licenseModal",
            title="License Agreement",
            footer=Button("Close", variant="secondary", data_bs_dismiss="modal"),
        ),
        # Toast and Drawer are not triggered in this static demo but are included in the app.
        ToastContainer(
            Toast(
                "Form submitted successfully!", title="Success", variant="success", id="submitToast"
            ),
            position="top-end",
        ),
        Drawer(Div(P("Drawer content")), drawer_id="menuDrawer", title="Menu"),
    )


@app.route("/signup", methods=["POST"])
def api_signup() -> Div:
    """Mock API endpoint for sign-up (HTMX target)."""
    # Simulate a 1-second delay for a loading state demonstration
    time.sleep(1)

    # After submission, trigger the Toast (Requires a little JS/HTMX, but we'll simulate the response)

    # We use a Spinner here to showcase a transient loading state
    return Div(
        Alert(
            Icon("check-circle-fill", cls="me-2"),
            "Registration successful! Check your email for the magic link.",
            variant="success",
            hx_swap_oob="true",  # HTMX out-of-band swap to show the Toast
        ),
    )


if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("🚀 Running FastAuth: Modern SaaS Landing Page Demo")
    print("📍 Visit: http://localhost:5001")
    print("=" * 70)
    serve()
