"""FastStrap v0.2.2 - Complete Interactive Demo

Showcases all 12 components with real interactions and custom styling.
Theme toggle and toast trigger work WITHOUT extra JavaScript using HTMX!
"""

from fasthtml.common import H1, H2, H3, H4, A, Div, FastHTML, Li, NotStr, P, Script, Span, Ul, serve

from faststrap import (
    # Feedback
    Alert,
    # Display
    Badge,
    # Forms
    Button,
    ButtonGroup,
    ButtonToolbar,
    Card,
    Col,
    # Layout
    Container,
    # Navigation
    Drawer,
    # Utils
    Icon,
    Modal,
    Navbar,
    Row,
    Toast,
    ToastContainer,
    add_bootstrap,
)

app = FastHTML()
# Start with dark theme
current_theme = {"theme": "dark"}
add_bootstrap(app, theme=current_theme["theme"], use_cdn=True)


# ============================================================================
# HTMX ROUTE: Toggle Theme (No JavaScript needed!)
# ============================================================================
@app.route("/toggle-theme", methods=["POST"])
def toggle_theme():
    """Toggle between light and dark theme using HTMX."""
    # Toggle theme
    current_theme["theme"] = "light" if current_theme["theme"] == "dark" else "dark"

    # Return JavaScript to update HTML data-bs-theme attribute
    # This is the ONLY way to change theme without page reload
    return NotStr(
        f"""
        <script>
            document.documentElement.setAttribute('data-bs-theme', '{current_theme["theme"]}');
        </script>
        <span id="theme-status" class="badge bg-success">
            Theme changed to {current_theme["theme"].title()} mode!
        </span>
    """
    )


# ============================================================================
# HTMX ROUTE: Show Toast (No JavaScript needed!)
# ============================================================================
@app.route("/show-toast")
def show_toast():
    """Return a new toast that auto-shows using HTMX."""
    return Toast(
        Div(
            Icon("bell-fill", cls="me-2"),
            "This toast was triggered via HTMX! No custom JavaScript needed.",
        ),
        title="HTMX Magic ✨",
        variant="info",
        autohide=True,
        delay=4000,
        id="htmxToast",
        # Auto-show toast with inline script (Bootstrap's own JS)
        **{"data-bs-autohide": "true"},
    ), Script(
        """
        // Use Bootstrap's own JS to show the toast (not custom code)
        const toast = new bootstrap.Toast(document.getElementById('htmxToast'));
        toast.show();
    """
    )


@app.route("/")
def home():
    return Div(
        # ============================================================================
        # NAVBAR - Sticky top navigation
        # ============================================================================
        Navbar(
            Div(
                A("Home", href="/", cls="nav-link active"),
                A("Components", href="#components", cls="nav-link"),
                A("Docs", href="#docs", cls="nav-link"),
                A(
                    "GitHub",
                    href="https://github.com/Evayoung/Faststrap",
                    cls="nav-link",
                    target="_blank",
                ),
                cls="navbar-nav me-auto",
            ),
            Div(
                # HTMX Theme Toggle Button (No custom JS!)
                Button(
                    Icon("moon-stars-fill" if current_theme["theme"] == "dark" else "sun-fill"),
                    " Theme",
                    variant="outline-light",
                    size="sm",
                    cls="me-2",
                    hx_post="/toggle-theme",
                    hx_target="#theme-status",
                    hx_swap="innerHTML",
                ),
                Span(id="theme-status", cls="badge bg-secondary me-2"),
                Button(Icon("github"), " Star", variant="outline-light", size="sm"),
                cls="d-flex align-items-center",
            ),
            brand="FastStrap v0.2.2",
            brand_href="/",
            variant="dark",
            bg="primary",
            expand="lg",
            cls="shadow-lg",
            style="position: sticky; top: 0; z-index: 1030;",
        ),
        # ============================================================================
        # TOAST CONTAINER - Shows toasts dynamically
        # ============================================================================
        Div(
            id="toast-container-target",  # Target for HTMX toast injection
            **{"data-bs-position": "top-end"},
        ),
        ToastContainer(
            Toast(
                Div(
                    Icon("check-circle-fill", cls="me-2"),
                    "Welcome to FastStrap! All 12 components working perfectly.",
                ),
                title="Success",
                variant="success",
                autohide=True,
                delay=5000,
                id="welcomeToast",
            ),
            position="top-end",
            cls="p-3",
        ),
        # ============================================================================
        # HERO SECTION - With HTMX toast trigger button
        # ============================================================================
        Container(
            Div(
                H1(
                    Icon("lightning-charge-fill", cls="me-2"),
                    "FastStrap Demo",
                    cls="display-3 fw-bold mb-3",
                ),
                P(
                    "12 Bootstrap components in pure Python. Zero custom JavaScript required!",
                    cls="lead text-white-50 mb-4",
                ),
                Div(
                    Button(
                        Icon("play-fill"),
                        " Open Modal Demo",
                        variant="light",
                        size="lg",
                        data_bs_toggle="modal",
                        data_bs_target="#featureModal",
                        cls="me-2 mb-2",
                    ),
                    Button(
                        Icon("list"),
                        " Open Drawer Menu",
                        variant="outline-light",
                        size="lg",
                        data_bs_toggle="offcanvas",
                        data_bs_target="#menuDrawer",
                        cls="me-2 mb-2",
                    ),
                    # HTMX Toast Trigger Button (No custom JS!)
                    Button(
                        Icon("bell-fill"),
                        " Show Toast (HTMX)",
                        variant="info",
                        size="lg",
                        hx_get="/show-toast",
                        hx_target="#toast-container-target",
                        hx_swap="innerHTML",
                        cls="mb-2",
                    ),
                ),
                Alert(
                    Icon("info-circle-fill", cls="me-2"),
                    "Try the theme toggle and toast button above - they work with HTMX, no custom JavaScript!",
                    variant="info",
                    cls="mt-4",
                ),
                cls="text-center py-5 my-5 rounded-4",
                style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);",
            ),
            # ============================================================================
            # ALERTS SECTION
            # ============================================================================
            Div(
                H2(
                    Icon("exclamation-triangle-fill", cls="me-2"),
                    "Alerts with Icons",
                    cls="h3 mb-4",
                ),
                Row(
                    Col(
                        Alert(
                            Icon("check-circle-fill", cls="me-2"),
                            "Success! Your action completed successfully.",
                            variant="success",
                            dismissible=True,
                            cls="mb-3",
                        ),
                        span=12,
                        md=6,
                    ),
                    Col(
                        Alert(
                            Icon("info-circle-fill", cls="me-2"),
                            "Info: This is an informational message.",
                            variant="info",
                            dismissible=True,
                            cls="mb-3",
                        ),
                        span=12,
                        md=6,
                    ),
                    Col(
                        Alert(
                            Icon("exclamation-triangle-fill", cls="me-2"),
                            "Warning! Please review this carefully.",
                            variant="warning",
                            dismissible=True,
                            cls="mb-3",
                        ),
                        span=12,
                        md=6,
                    ),
                    Col(
                        Alert(
                            Icon("x-circle-fill", cls="me-2"),
                            "Error! Something went wrong.",
                            variant="danger",
                            dismissible=True,
                            cls="mb-3",
                        ),
                        span=12,
                        md=6,
                    ),
                ),
                cls="mb-5",
            ),
            # ============================================================================
            # BUTTONS & BUTTON GROUPS SECTION
            # ============================================================================
            Div(
                H2(Icon("cursor-fill", cls="me-2"), "Buttons & Groups", cls="h3 mb-4"),
                # Button variants
                Div(
                    H4("Variants", cls="h5 mb-3"),
                    Button("Primary", variant="primary", cls="me-2 mb-2"),
                    Button("Secondary", variant="secondary", cls="me-2 mb-2"),
                    Button("Success", variant="success", cls="me-2 mb-2"),
                    Button("Danger", variant="danger", cls="me-2 mb-2"),
                    Button("Warning", variant="warning", cls="me-2 mb-2"),
                    Button("Info", variant="info", cls="me-2 mb-2"),
                    Button("Light", variant="light", cls="me-2 mb-2"),
                    Button("Dark", variant="dark", cls="me-2 mb-2"),
                    cls="mb-4",
                ),
                # Button sizes
                Div(
                    H4("Sizes", cls="h5 mb-3"),
                    Button("Small", variant="primary", size="sm", cls="me-2"),
                    Button("Medium", variant="primary", cls="me-2"),
                    Button("Large", variant="primary", size="lg", cls="me-2"),
                    cls="mb-4",
                ),
                # Button groups
                Div(
                    H4("Button Groups", cls="h5 mb-3"),
                    ButtonGroup(
                        Button(Icon("align-start"), variant="outline-primary"),
                        Button(Icon("align-center"), variant="outline-primary"),
                        Button(Icon("align-end"), variant="outline-primary"),
                        cls="me-3 mb-2",
                    ),
                    ButtonGroup(
                        Button("1", variant="outline-secondary"),
                        Button("2", variant="outline-secondary"),
                        Button("3", variant="outline-secondary"),
                        Button("4", variant="outline-secondary"),
                        cls="me-3 mb-2",
                    ),
                    ButtonGroup(
                        Button(Icon("chevron-up"), variant="secondary"),
                        Button(Icon("chevron-down"), variant="secondary"),
                        vertical=True,
                        cls="mb-2",
                    ),
                    cls="mb-4",
                ),
                # Button toolbar
                Div(
                    H4("Button Toolbar", cls="h5 mb-3"),
                    ButtonToolbar(
                        ButtonGroup(
                            Button("Copy", variant="outline-primary"),
                            Button("Paste", variant="outline-primary"),
                            Button("Cut", variant="outline-primary"),
                        ),
                        ButtonGroup(
                            Button(Icon("type-bold"), variant="outline-secondary"),
                            Button(Icon("type-italic"), variant="outline-secondary"),
                            Button(Icon("type-underline"), variant="outline-secondary"),
                        ),
                        ButtonGroup(
                            Button(Icon("list-ul"), variant="outline-info"),
                            Button(Icon("list-ol"), variant="outline-info"),
                        ),
                    ),
                ),
                cls="mb-5",
            ),
            # ============================================================================
            # BADGES SECTION
            # ============================================================================
            Div(
                H2(Icon("tags-fill", cls="me-2"), "Badges", cls="h3 mb-4"),
                Div(
                    H4("Variants", cls="h5 mb-3"),
                    Badge("Primary", variant="primary", cls="me-2"),
                    Badge("Secondary", variant="secondary", cls="me-2"),
                    Badge("Success", variant="success", cls="me-2"),
                    Badge("Danger", variant="danger", cls="me-2"),
                    Badge("Warning", variant="warning", cls="me-2"),
                    Badge("Info", variant="info", cls="me-2"),
                    Badge("Light", variant="light", cls="me-2"),
                    Badge("Dark", variant="dark", cls="me-2"),
                    cls="mb-3",
                ),
                Div(
                    H4("Pills", cls="h5 mb-3"),
                    Badge("New", variant="primary", pill=True, cls="me-2"),
                    Badge("99+", variant="danger", pill=True, cls="me-2"),
                    Badge(Icon("check"), " Verified", variant="success", pill=True, cls="me-2"),
                    Badge(Icon("star-fill"), " Featured", variant="warning", pill=True, cls="me-2"),
                ),
                cls="mb-5",
            ),
            # ============================================================================
            # CARDS SECTION - Grid of feature cards
            # ============================================================================
            Div(
                H2(Icon("card-heading", cls="me-2"), "Cards Showcase", cls="h3 mb-4"),
                Row(
                    # Card 1: Zero JavaScript
                    Col(
                        Card(
                            Div(
                                Icon(
                                    "code-square", style="font-size: 3rem;", cls="text-primary mb-3"
                                ),
                                P(
                                    "Pure Python components. Theme toggle and toast work via HTMX!",
                                    cls="card-text",
                                ),
                                Button(
                                    Icon("arrow-right"),
                                    " Learn More",
                                    variant="primary",
                                    size="sm",
                                    data_bs_toggle="modal",
                                    data_bs_target="#learnModal",
                                ),
                            ),
                            header=Div(
                                "Zero Custom JavaScript",
                                Badge("HTMX", variant="success", pill=True, cls="float-end"),
                            ),
                            cls="h-100 shadow-sm",
                        ),
                        span=12,
                        md=6,
                        lg=4,
                        cls="mb-4",
                    ),
                    # Card 2: Fast Setup
                    Col(
                        Card(
                            Div(
                                Icon(
                                    "lightning-charge-fill",
                                    style="font-size: 3rem;",
                                    cls="text-warning mb-3",
                                ),
                                P(
                                    "Get started in seconds. No build steps or configuration needed.",
                                    cls="card-text",
                                ),
                            ),
                            header="Fast Setup",
                            footer=Span(
                                Icon("clock", cls="me-1"),
                                "< 30 seconds to start",
                                cls="text-muted small",
                            ),
                            cls="h-100 shadow-sm",
                        ),
                        span=12,
                        md=6,
                        lg=4,
                        cls="mb-4",
                    ),
                    # Card 3: Themes
                    Col(
                        Card(
                            Div(
                                Icon(
                                    "palette-fill", style="font-size: 3rem;", cls="text-info mb-3"
                                ),
                                P(
                                    "Full Bootstrap theming support. Light, dark, or custom themes.",
                                    cls="card-text",
                                ),
                                Alert(
                                    "Try the theme toggle button above!",
                                    variant="info",
                                    cls="mb-0 py-2",
                                ),
                            ),
                            header="Beautiful Themes",
                            subtitle="Built-in dark mode",
                            cls="h-100 shadow-sm",
                        ),
                        span=12,
                        md=6,
                        lg=4,
                        cls="mb-4",
                    ),
                    # Card 4: HTMX Integration
                    Col(
                        Card(
                            Div(
                                Icon("plugin", style="font-size: 3rem;", cls="text-success mb-3"),
                                P(
                                    "Full HTMX integration for dynamic updates without page reloads.",
                                    cls="card-text",
                                ),
                                ButtonGroup(
                                    Button("Docs", variant="outline-success", size="sm"),
                                    Button("Examples", variant="outline-success", size="sm"),
                                ),
                            ),
                            header="HTMX Ready",
                            cls="h-100 shadow-sm",
                        ),
                        span=12,
                        md=6,
                        lg=4,
                        cls="mb-4",
                    ),
                    # Card 5: Stats
                    Col(
                        Card(
                            Div(
                                H3("12+", cls="display-4 fw-bold text-primary mb-0"),
                                P("Components", cls="text-muted"),
                                Div(
                                    Badge("Phase 1", variant="primary", cls="me-1"),
                                    Badge("Phase 2", variant="success", cls="me-1"),
                                ),
                            ),
                            header="Component Library",
                            footer=Button(
                                "View Roadmap",
                                variant="outline-primary",
                                size="sm",
                                data_bs_toggle="modal",
                                data_bs_target="#roadmapModal",
                                cls="w-100",
                            ),
                            cls="h-100 shadow-sm text-center",
                        ),
                        span=12,
                        md=6,
                        lg=4,
                        cls="mb-4",
                    ),
                    # Card 6: Open Source
                    Col(
                        Card(
                            Div(
                                Icon("github", style="font-size: 3rem;", cls="mb-3"),
                                P(
                                    "Open source and community-driven. Contributions welcome!",
                                    cls="card-text",
                                ),
                                Div(
                                    Button(
                                        Icon("star-fill"),
                                        " Star on GitHub",
                                        variant="dark",
                                        size="sm",
                                        cls="w-100 mb-2",
                                    ),
                                    Button(
                                        Icon("chat-dots"),
                                        " Join Discussion",
                                        variant="outline-dark",
                                        size="sm",
                                        cls="w-100",
                                    ),
                                ),
                            ),
                            header="Open Source",
                            cls="h-100 shadow-sm",
                        ),
                        span=12,
                        md=6,
                        lg=4,
                        cls="mb-4",
                    ),
                ),
                cls="mb-5",
            ),
            # ============================================================================
            # GRID SYSTEM DEMO
            # ============================================================================
            Div(
                H2(Icon("grid-3x3-gap-fill", cls="me-2"), "Responsive Grid", cls="h3 mb-4"),
                P(
                    "Resize your browser to see the responsive grid in action!",
                    cls="text-muted mb-3",
                ),
                Row(
                    Col(
                        Div("Column 1", cls="p-3 bg-primary text-white text-center rounded"),
                        span=12,
                        md=4,
                        cls="mb-3",
                    ),
                    Col(
                        Div("Column 2", cls="p-3 bg-secondary text-white text-center rounded"),
                        span=12,
                        md=4,
                        cls="mb-3",
                    ),
                    Col(
                        Div("Column 3", cls="p-3 bg-success text-white text-center rounded"),
                        span=12,
                        md=4,
                        cls="mb-3",
                    ),
                ),
                Row(
                    Col(
                        Div("Wide Column", cls="p-3 bg-info text-white text-center rounded"),
                        span=12,
                        md=8,
                        cls="mb-3",
                    ),
                    Col(
                        Div("Narrow", cls="p-3 bg-warning text-dark text-center rounded"),
                        span=12,
                        md=4,
                        cls="mb-3",
                    ),
                ),
                cls="mb-5",
            ),
            cls="py-5",
        ),
        # ============================================================================
        # MODALS
        # ============================================================================
        # Feature Modal
        Modal(
            Div(
                P("FastStrap provides a complete set of Bootstrap components in pure Python:"),
                Ul(
                    Li(
                        Icon("check-circle-fill", cls="text-success me-2"),
                        "12+ pre-built components",
                    ),
                    Li(
                        Icon("check-circle-fill", cls="text-success me-2"),
                        "Full type hints for IDE support",
                    ),
                    Li(
                        Icon("check-circle-fill", cls="text-success me-2"),
                        "HTMX integration for dynamic features",
                    ),
                    Li(Icon("check-circle-fill", cls="text-success me-2"), "Dark mode and theming"),
                    Li(
                        Icon("check-circle-fill", cls="text-success me-2"), "Responsive grid system"
                    ),
                ),
                Alert(
                    Icon("lightbulb-fill", cls="me-2"),
                    "Theme toggle and toast trigger work with HTMX - no custom JavaScript needed!",
                    variant="info",
                ),
            ),
            modal_id="featureModal",
            title="FastStrap Features",
            size="lg",
            centered=True,
            footer=Div(
                Button("Close", variant="secondary", data_bs_dismiss="modal"),
                Button(Icon("download"), " Install Now", variant="primary"),
            ),
        ),
        # Learn More Modal
        Modal(
            Div(
                P("To get started with FastStrap:"),
                Div(
                    P("1. Install via pip:", cls="fw-bold mb-2"),
                    Div(
                        "pip install faststrap",
                        cls="bg-dark text-light p-3 rounded font-monospace mb-3",
                    ),
                    P("2. Add to your FastHTML app:", cls="fw-bold mb-2"),
                    Div(
                        "from faststrap import add_bootstrap, Button\nadd_bootstrap(app)",
                        cls="bg-dark text-light p-3 rounded font-monospace mb-3",
                        style="white-space: pre;",
                    ),
                    P("3. Start building!", cls="fw-bold"),
                ),
            ),
            modal_id="learnModal",
            title="Getting Started",
            footer=Button("Got it!", variant="primary", data_bs_dismiss="modal"),
        ),
        # Roadmap Modal
        Modal(
            Div(
                P("FastStrap development roadmap:"),
                Div(
                    Badge("v0.2.2", variant="success", pill=True, cls="mb-2"),
                    " - Current Release",
                    P("12 core components with HTMX integration", cls="text-muted small ms-4 mb-3"),
                ),
                Div(
                    Badge("v0.3.0", variant="primary", pill=True, cls="mb-2"),
                    " - Q1 2025",
                    P(
                        "Form components, Tabs, Dropdown, Pagination",
                        cls="text-muted small ms-4 mb-3",
                    ),
                ),
                Div(
                    Badge("v1.0.0", variant="secondary", pill=True, cls="mb-2"),
                    " - Q4 2025",
                    P(
                        "50+ components, component playground, video tutorials",
                        cls="text-muted small ms-4",
                    ),
                ),
            ),
            modal_id="roadmapModal",
            title="Development Roadmap",
            scrollable=True,
            footer=Button("Close", variant="secondary", data_bs_dismiss="modal"),
        ),
        # ============================================================================
        # DRAWER - Side navigation menu
        # ============================================================================
        Drawer(
            Div(
                H3("Navigation", cls="h5 mb-4"),
                # Navigation links with icons
                A(
                    Icon("house-fill", cls="me-2"),
                    "Home",
                    href="/",
                    cls="d-flex align-items-center text-decoration-none text-dark mb-3 p-2 rounded",
                ),
                A(
                    Icon("grid-fill", cls="me-2"),
                    "Components",
                    href="#components",
                    cls="d-flex align-items-center text-decoration-none text-dark mb-3 p-2 rounded",
                ),
                A(
                    Icon("book-fill", cls="me-2"),
                    "Documentation",
                    href="#docs",
                    cls="d-flex align-items-center text-decoration-none text-dark mb-3 p-2 rounded",
                ),
                A(
                    Icon("github", cls="me-2"),
                    "GitHub",
                    href="https://github.com/Evayoung/Faststrap",
                    target="_blank",
                    cls="d-flex align-items-center text-decoration-none text-dark mb-3 p-2 rounded",
                ),
                Div(cls="my-4", style="border-top: 1px solid #dee2e6;"),
                # Settings section with HTMX theme toggle
                H4("Settings", cls="h6 mb-3 text-muted"),
                Div(
                    Button(
                        Icon("moon-stars-fill", cls="me-2"),
                        "Toggle Theme (HTMX)",
                        variant="outline-secondary",
                        size="sm",
                        cls="w-100 mb-2",
                        hx_post="/toggle-theme",
                        hx_target="#theme-status",
                    ),
                    Button(
                        Icon("bell-fill", cls="me-2"),
                        "Show Toast (HTMX)",
                        variant="outline-info",
                        size="sm",
                        cls="w-100 mb-2",
                        hx_get="/show-toast",
                        hx_target="#toast-container-target",
                        hx_swap="innerHTML",
                    ),
                ),
                # Footer in drawer
                Div(
                    P("FastStrap v0.2.2", cls="text-muted small mb-1"),
                    Div(
                        Badge("12 Components", variant="primary", pill=True, cls="me-1"),
                        Badge("HTMX Ready", variant="success", pill=True),
                    ),
                    cls="mt-4",
                ),
            ),
            drawer_id="menuDrawer",
            title="Menu",
            placement="start",
            backdrop=True,
            cls="shadow-lg",
        ),
        # ============================================================================
        # MINIMAL BOOTSTRAP JS (Only for auto-showing welcome toast)
        # ============================================================================
        Script(
            """
            // Auto-show welcome toast when page loads (using Bootstrap's own JS)
            document.addEventListener('DOMContentLoaded', function() {
                const toastEl = document.getElementById('welcomeToast');
                if (toastEl && typeof bootstrap !== 'undefined') {
                    const toast = new bootstrap.Toast(toastEl);
                    toast.show();
                }
            });
            """
        ),
    )


if __name__ == "__main__":
    print("\n" + "=" * 70)
    print(" FastStrap v0.2.2 - Complete Interactive Demo")
    print("=" * 70)
    print("\n Visit: http://localhost:5001")
    print("\n" + "=" * 70 + "\n")
    serve()
