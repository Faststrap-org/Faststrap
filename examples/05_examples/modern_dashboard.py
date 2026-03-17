"""
FastStrap Modern Dashboard - Proper FastHTML Implementation
Using correct Style element in headers for custom CSS.
"""

from fasthtml.common import (
    H1,
    H3,
    H4,
    H5,
    H6,
    A,
    Br,
    Div,
    FastHTML,
    Li,
    P,
    Small,
    Span,
    Strong,
    Style,
    Ul,
    serve,
)

from faststrap import (
    # Feedback
    Alert,
    # Display
    Badge,
    Breadcrumb,
    # Forms
    Button,
    Col,
    # Layout
    Container,
    Drawer,
    Dropdown,
    DropdownDivider,
    Icon,
    Input,
    Modal,
    # Navigation
    Navbar,
    Pagination,
    Progress,
    ProgressBar,
    Row,
    Select,
    # Utilities
    Spinner,
    TabPane,
    Tabs,
    Toast,
    ToastContainer,
    # Core
    add_bootstrap,
)

# ==============================================
# CUSTOM CSS FOR MODERN DESIGN
# ==============================================
custom_css = """
:root {
    --bg-start: #0d1117;
    --bg-end: #1a1f29;
    --card-glass: rgba(255, 255, 255, 0.06);
    --border-glass: rgba(255, 255, 255, 0.12);

    --primary-color: #4e8df5;
    --primary-glow: rgba(78, 141, 245, 0.35);

    --accent-purple: #a779ff;
    --accent-cyan: #3ed4ff;

    --success: #3dd68c;
    --warning: #ffd36b;
    --danger: #ff6b6b;

    --shadow-lg: 0 20px 40px rgba(0,0,0,0.45);
    --shadow-soft: 0 10px 20px rgba(0,0,0,0.25);

    --radius-lg: 18px;
    --radius-md: 12px;

    --transition: 0.3s ease;
}

body {
    background: linear-gradient(135deg, var(--bg-start), var(--bg-end));
    font-family: 'Inter', sans-serif;
    color: #e5e7eb;
    letter-spacing: 0.1px;
}

/** -------------------------
    GLOBAL ENHANCEMENTS
-------------------------- */
.glass-card {
    background: var(--card-glass);
    backdrop-filter: blur(14px);
    border: 1px solid var(--border-glass);
    border-radius: var(--radius-lg);
    box-shadow: var(--shadow-soft);
    transition: var(--transition);
}

.glass-card:hover {
    border-color: rgba(255,255,255,0.18);
    transform: translateY(-4px);
}

/** Typography */
.gradient-text {
    background: linear-gradient(90deg, var(--primary-color), var(--accent-purple));
    -webkit-background-clip: text;
    color: transparent;
}

/** -------------------------
    BUTTONS
-------------------------- */
.btn-glow {
    transition: var(--transition);
}

.btn-glow:hover {
    box-shadow: 0 0 18px var(--primary-glow);
    transform: translateY(-2px);
}

.btn-primary {
    background: var(--primary-color) !important;
    border: none !important;
}

.btn-outline-light:hover {
    background: rgba(255,255,255,0.1) !important;
}

/** -------------------------
    FORM FIELDS
-------------------------- */
.form-control-glass {
    background: rgba(255,255,255,0.07) !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    color: white !important;
    border-radius: var(--radius-md) !important;
    transition: var(--transition) !important;
}

.form-control-glass:focus {
    background: rgba(255,255,255,0.1) !important;
    border-color: var(--primary-color) !important;
    box-shadow: 0 0 0 3px rgba(78,141,245,0.25) !important;
}

/** -------------------------
    STATS CARDS
-------------------------- */
.stats-card {
    text-align: center;
    padding: 25px 10px;
}

.stats-card .icon {
    font-size: 2.5rem;
    margin-bottom: 12px;
    color: var(--accent-cyan);
}

/** -------------------------
    PROGRESS BAR
-------------------------- */
.progress {
    height: 10px;
    border-radius: var(--radius-md);
}

.progress-bar {
    background: linear-gradient(90deg, var(--accent-cyan), var(--accent-purple));
}

/** -------------------------
    NAVBAR + DRAWER
-------------------------- */
.navbar.glass-card {
    padding: 10px 18px;
    border-radius: var(--radius-md);
}

.offcanvas {
    background: var(--bg-start) !important;
    border-right: 1px solid var(--border-glass);
}

/** -------------------------
    HERO SECTION
-------------------------- */
.dashboard-hero {
    background: linear-gradient(
        135deg,
        rgba(78,141,245,0.15),
        rgba(167,121,255,0.12)
    );
    border-radius: var(--radius-lg);
    padding: 55px 20px;
    box-shadow: var(--shadow-soft);
}

/** -------------------------
    HOVER ACTIVITY LIST
-------------------------- */
.activity-item {
    padding: 12px 10px;
    border-bottom: 1px solid rgba(255,255,255,0.08);
    transition: var(--transition);
}

.activity-item:hover {
    background: rgba(255,255,255,0.04);
    padding-left: 16px;
}

/** MEDIA QUERIES */
@media (max-width: 768px) {
    .navbar.glass-card {
        border-radius: 0;
    }
}

"""

# ==============================================
# APP INITIALIZATION
# ==============================================
hdrs = (
    Style(custom_css),
    # Add more headers if needed
)

app = FastHTML(hdrs=hdrs)
add_bootstrap(app, mode="dark", use_cdn=True)


# ==============================================
# DASHBOARD ROUTE
# ==============================================
@app.get("/")
def dashboard():
    return Div(
        # ==============================================
        # SIDEBAR DRAWER
        # ==============================================
        Drawer(
            Div(
                # Logo
                Div(
                    H3(
                        Icon("lightning-charge-fill", cls="me-2 text-primary"),
                        "FastStrap",
                        cls="h4 mb-0 gradient-text",
                    ),
                    Small("Modern Dashboard", cls="text-muted"),
                    cls="mb-4 pb-3 border-bottom border-secondary",
                ),
                # Navigation
                H5("Navigation", cls="text-uppercase small text-muted mb-3"),
                Ul(
                    Li(
                        A(
                            Icon("speedometer2", cls="me-2 text-primary"),
                            "Dashboard",
                            href="#",
                            cls="nav-link active py-2 rounded",
                        ),
                        cls="nav-item mb-1",
                    ),
                    Li(
                        A(
                            Icon("bar-chart", cls="me-2 text-info"),
                            "Analytics",
                            href="#",
                            cls="nav-link py-2 rounded",
                        ),
                        cls="nav-item mb-1",
                    ),
                    Li(
                        A(
                            Icon("people", cls="me-2 text-success"),
                            "Team",
                            href="#",
                            cls="nav-link py-2 rounded",
                        ),
                        cls="nav-item mb-1",
                    ),
                    Li(
                        A(
                            Icon("gear", cls="me-2 text-warning"),
                            "Settings",
                            href="#",
                            cls="nav-link py-2 rounded",
                        ),
                        cls="nav-item mb-1",
                    ),
                    cls="nav flex-column mb-4",
                ),
                # Stats
                Div(
                    H6("System Status", cls="text-uppercase small text-muted mb-3"),
                    Div(
                        Div(
                            Small("Components", cls="d-block text-muted"),
                            Strong("20", cls="d-block h4 mb-0 text-success"),
                            cls="mb-3",
                        ),
                        Div(
                            Small("Performance", cls="d-block text-muted"),
                            Progress(85, variant="success", cls="mt-1 mb-2"),
                            cls="mb-3",
                        ),
                        Div(
                            Small("Uptime", cls="d-block text-muted"),
                            Span(
                                Icon("circle-fill", cls="status-online me-1"),
                                "All Systems Operational",
                                cls="text-success",
                            ),
                            cls="mb-2",
                        ),
                    ),
                    cls="glass-card border-0 p-3",
                ),
                cls="p-3",
            ),
            drawer_id="sidebar",
            title="",
            placement="start",
            cls="bg-dark",
        ),
        # ==============================================
        # MAIN CONTENT
        # ==============================================
        Div(
            # Top Navigation
            Navbar(
                Div(
                    Button(
                        Icon("list", cls="fs-4"),
                        cls="btn btn-outline-light me-2 btn-glow",
                        data_bs_toggle="offcanvas",
                        data_bs_target="#sidebar",
                    ),
                    Breadcrumb(("Dashboard", "/"), ("Overview", None)),
                    cls="d-flex align-items-center",
                ),
                Div(
                    Dropdown(
                        "View Profile",
                        "Settings",
                        DropdownDivider(),
                        "Logout",
                        label=Div(
                            Icon("person-circle", cls="me-2"),
                            "Alex Johnson",
                            cls="d-inline-flex align-items-center",
                        ),
                        variant="outline-light",
                        cls="btn-glow",
                    ),
                    cls="d-flex",
                ),
                brand="",
                bg="dark",
                variant="dark",
                expand="lg",
                cls="glass-card mb-4 border-0",
            ),
            # Main Container
            Container(
                # Welcome Banner
                Div(
                    Row(
                        Col(
                            Div(
                                H1(
                                    "FastStrap Dashboard",
                                    cls="display-4 fw-bold mb-3 gradient-text",
                                ),
                                P(
                                    Icon("check-circle-fill", cls="text-success me-2"),
                                    "20 components • 100% Python • Zero JavaScript",
                                    cls="lead mb-4",
                                ),
                                Div(
                                    Button(
                                        Icon("rocket-takeoff", cls="me-2"),
                                        "Get Started",
                                        variant="primary",
                                        size="lg",
                                        cls="btn-glow pulse me-3 mb-2",
                                    ),
                                    Button(
                                        "View Components",
                                        variant="outline-light",
                                        size="lg",
                                        cls="btn-glow mb-2",
                                    ),
                                    cls="d-flex flex-wrap",
                                ),
                                cls="py-4",
                            ),
                            span=12,
                        ),
                    ),
                    cls="dashboard-hero glass-card border-0",
                ),
                # Stats Cards
                Row(
                    Col(
                        Div(
                            Div(
                                Icon("activity", cls="icon text-info"),
                                H3("98.5%", cls="mb-1 fw-bold"),
                                Small("Uptime", cls="text-muted d-block"),
                                cls="stats-card",
                            ),
                            cls="glass-card border-0 shadow-lg h-100",
                        ),
                        span=12,
                        md=3,
                        cls="mb-4",
                    ),
                    Col(
                        Div(
                            Div(
                                Icon("arrow-up-right", cls="icon text-success"),
                                H3("+42%", cls="mb-1 fw-bold"),
                                Small("Growth", cls="text-muted d-block"),
                                cls="stats-card",
                            ),
                            cls="glass-card border-0 shadow-lg h-100",
                        ),
                        span=12,
                        md=3,
                        cls="mb-4",
                    ),
                    Col(
                        Div(
                            Div(
                                Icon("people", cls="icon text-warning"),
                                H3("1.2K", cls="mb-1 fw-bold"),
                                Small("Users", cls="text-muted d-block"),
                                cls="stats-card",
                            ),
                            cls="glass-card border-0 shadow-lg h-100",
                        ),
                        span=12,
                        md=3,
                        cls="mb-4",
                    ),
                    Col(
                        Div(
                            Div(
                                Icon("lightning-charge", cls="icon text-danger"),
                                H3("20", cls="mb-1 fw-bold"),
                                Small("Components", cls="text-muted d-block"),
                                cls="stats-card",
                            ),
                            cls="glass-card border-0 shadow-lg h-100",
                        ),
                        span=12,
                        md=3,
                        cls="mb-4",
                    ),
                ),
                # Tabs Section
                Div(
                    Tabs(
                        ("forms", "Forms", True),
                        ("components", "Components"),
                        ("analytics", "Analytics"),
                        variant="pills",
                        cls="mb-3",
                    ),
                    Div(
                        # Forms Tab (Active)
                        TabPane(
                            Row(
                                Col(
                                    Div(
                                        H4("Contact Form", cls="mb-4 gradient-text"),
                                        Div(
                                            Div(
                                                Small("Full Name", cls="form-label"),
                                                Input(
                                                    "name",
                                                    placeholder="Enter your name",
                                                    required=True,
                                                    cls="form-control-glass mb-3",
                                                ),
                                                cls="mb-3",
                                            ),
                                            Div(
                                                Small("Email Address", cls="form-label"),
                                                Input(
                                                    "email",
                                                    input_type="email",
                                                    placeholder="name@example.com",
                                                    help_text="We'll never share your email with anyone else.",
                                                    required=True,
                                                    cls="form-control-glass mb-3",
                                                ),
                                                cls="mb-3",
                                            ),
                                            Div(
                                                Small("Select Plan", cls="form-label"),
                                                Select(
                                                    "plan",
                                                    ("personal", "Personal Plan"),
                                                    ("team", "Team Plan", True),
                                                    ("enterprise", "Enterprise Plan"),
                                                    cls="form-control-glass mb-3",
                                                ),
                                                cls="mb-3",
                                            ),
                                            Div(
                                                Small("Message", cls="form-label"),
                                                Input(
                                                    "message",
                                                    placeholder="Tell us about your project...",
                                                    input_type="textarea",
                                                    rows=4,
                                                    cls="form-control-glass mb-3",
                                                ),
                                                cls="mb-3",
                                            ),
                                            Div(
                                                Button(
                                                    "Submit", variant="primary", cls="btn-glow me-2"
                                                ),
                                                Button(
                                                    "Cancel",
                                                    variant="outline-light",
                                                    cls="btn-glow",
                                                ),
                                                cls="mt-3",
                                            ),
                                        ),
                                        cls="p-4",
                                    ),
                                    cls="glass-card border-0 h-100",
                                ),
                                span=12,
                                md=6,
                                cls="mb-4",
                            ),
                            Row(
                                Col(
                                    Div(
                                        H4("Interactive Components", cls="mb-4 gradient-text"),
                                        Div(
                                            H5("Dropdown Examples", cls="h6 mb-3"),
                                            Div(
                                                Dropdown(
                                                    "Edit Profile",
                                                    "Account Settings",
                                                    DropdownDivider(),
                                                    "Logout",
                                                    label="User Menu",
                                                    variant="primary",
                                                    cls="btn-glow me-2 mb-3",
                                                ),
                                                Dropdown(
                                                    "Option 1",
                                                    "Option 2",
                                                    "Option 3",
                                                    label="More Options",
                                                    variant="outline-light",
                                                    cls="btn-glow mb-4",
                                                ),
                                                cls="mb-4",
                                            ),
                                            H5("Button Styles", cls="h6 mb-3"),
                                            Div(
                                                Button(
                                                    "Primary",
                                                    variant="primary",
                                                    cls="btn-glow me-2 mb-2",
                                                ),
                                                Button(
                                                    "Success",
                                                    variant="success",
                                                    cls="btn-glow me-2 mb-2",
                                                ),
                                                Button(
                                                    "Warning",
                                                    variant="warning",
                                                    cls="btn-glow me-2 mb-2",
                                                ),
                                                Button(
                                                    "Danger",
                                                    variant="danger",
                                                    cls="btn-glow me-2 mb-2",
                                                ),
                                                cls="mb-4",
                                            ),
                                            H5("Spinners", cls="h6 mb-3"),
                                            Div(
                                                Spinner(variant="primary", cls="me-2"),
                                                Spinner(
                                                    variant="success",
                                                    spinner_type="grow",
                                                    cls="me-2",
                                                ),
                                                Spinner(variant="warning", size="sm", cls="me-2"),
                                                Spinner(
                                                    variant="danger", spinner_type="grow", size="sm"
                                                ),
                                                cls="mb-4",
                                            ),
                                        ),
                                        cls="p-4",
                                    ),
                                    cls="glass-card border-0 h-100",
                                ),
                                span=12,
                                md=6,
                                cls="mb-4",
                            ),
                            tab_id="forms",
                            active=True,
                            cls="p-3",
                        ),
                        # Components Tab
                        TabPane(
                            Row(
                                Col(
                                    Div(
                                        H4("Progress Indicators", cls="mb-4 gradient-text"),
                                        Div(
                                            Div(
                                                Small("Project Completion", cls="form-label"),
                                                Progress(
                                                    75,
                                                    variant="success",
                                                    label="75%",
                                                    cls="mb-4 progress-bar-animated",
                                                ),
                                                cls="mb-3",
                                            ),
                                            Div(
                                                Small("Resource Usage", cls="form-label"),
                                                Progress(
                                                    60,
                                                    variant="info",
                                                    striped=True,
                                                    label="60%",
                                                    cls="mb-4",
                                                ),
                                                cls="mb-3",
                                            ),
                                            Div(
                                                Small("Storage", cls="form-label"),
                                                Progress(
                                                    90, variant="danger", label="90%", cls="mb-4"
                                                ),
                                                cls="mb-3",
                                            ),
                                            Div(
                                                Small("Stacked Progress", cls="form-label"),
                                                Div(
                                                    ProgressBar(40, variant="success"),
                                                    ProgressBar(30, variant="warning"),
                                                    ProgressBar(20, variant="danger"),
                                                    cls="progress mb-4",
                                                ),
                                                cls="mb-3",
                                            ),
                                        ),
                                        cls="p-4",
                                    ),
                                    cls="glass-card border-0 h-100",
                                ),
                                span=12,
                                md=6,
                                cls="mb-4",
                            ),
                            Row(
                                Col(
                                    Div(
                                        H4("Alerts & Notifications", cls="mb-4 gradient-text"),
                                        Div(
                                            Alert(
                                                Icon("info-circle-fill", cls="me-2"),
                                                "System update scheduled for tonight.",
                                                variant="info",
                                                dismissible=True,
                                                cls="mb-3",
                                            ),
                                            Alert(
                                                Icon("check-circle-fill", cls="me-2"),
                                                "All systems are operational.",
                                                variant="success",
                                                dismissible=True,
                                                cls="mb-3",
                                            ),
                                            Alert(
                                                Icon("exclamation-triangle-fill", cls="me-2"),
                                                "Warning: Storage at 90% capacity.",
                                                variant="warning",
                                                dismissible=True,
                                                cls="mb-3",
                                            ),
                                            Alert(
                                                Icon("lightning-charge-fill", cls="me-2"),
                                                "New components available in v0.3.0!",
                                                variant="primary",
                                                dismissible=True,
                                                cls="mb-4",
                                            ),
                                            H5("Pagination", cls="h6 mb-3"),
                                            Pagination(
                                                current_page=3,
                                                total_pages=10,
                                                size="sm",
                                                show_first_last=True,
                                                align="center",
                                                cls="mb-3",
                                            ),
                                        ),
                                        cls="p-4",
                                    ),
                                    cls="glass-card border-0 h-100",
                                ),
                                span=12,
                                md=6,
                                cls="mb-4",
                            ),
                            tab_id="components",
                            cls="p-3",
                        ),
                    ),
                    cls="glass-card border-0 shadow-lg mb-4",
                ),
                # Footer
                Row(
                    Col(
                        Div(
                            H5("About FastStrap", cls="mb-3 gradient-text"),
                            P(
                                "Build beautiful, modern web interfaces with pure Python. "
                                "20+ Bootstrap components ready for production.",
                                cls="text-muted mb-3",
                            ),
                            Div(
                                Button(
                                    Icon("github", cls="me-2"),
                                    "GitHub",
                                    variant="outline-light",
                                    size="sm",
                                    cls="btn-glow me-2 mb-2",
                                ),
                                Button(
                                    Icon("book", cls="me-2"),
                                    "Documentation",
                                    variant="outline-light",
                                    size="sm",
                                    cls="btn-glow me-2 mb-2",
                                ),
                                Button(
                                    Icon("discord", cls="me-2"),
                                    "Community",
                                    variant="outline-light",
                                    size="sm",
                                    cls="btn-glow mb-2",
                                ),
                            ),
                            cls="p-4",
                        ),
                        cls="glass-card border-0 h-100",
                    ),
                    span=12,
                    md=4,
                    cls="mb-4",
                ),
                Row(
                    Col(
                        Div(
                            H5("Quick Stats", cls="mb-3 gradient-text"),
                            Ul(
                                Li(
                                    Span(
                                        Badge("20", variant="primary", cls="badge-neon me-2"),
                                        "Components Available",
                                    ),
                                    cls="mb-2",
                                ),
                                Li(
                                    Span(
                                        Badge("100%", variant="success", cls="badge-neon me-2"),
                                        "Bootstrap 5 Compatible",
                                    ),
                                    cls="mb-2",
                                ),
                                Li(
                                    Span(
                                        Badge("0", variant="warning", cls="badge-neon me-2"),
                                        "JavaScript Required",
                                    ),
                                    cls="mb-2",
                                ),
                                Li(
                                    Span(
                                        Badge("MIT", variant="info", cls="badge-neon me-2"),
                                        "Open Source License",
                                    ),
                                ),
                                cls="list-unstyled",
                            ),
                            cls="p-4",
                        ),
                        cls="glass-card border-0 h-100",
                    ),
                    span=12,
                    md=4,
                    cls="mb-4",
                ),
                Row(
                    Col(
                        Div(
                            H5("Theme", cls="mb-3 gradient-text"),
                            Div(
                                Button(
                                    Icon("sun", cls="me-2"),
                                    "Light Mode",
                                    variant="outline-light",
                                    size="sm",
                                    hx_post="/theme/light",
                                    hx_target="body",
                                    cls="btn-glow me-2 mb-2",
                                ),
                                Button(
                                    Icon("moon", cls="me-2"),
                                    "Dark Mode",
                                    variant="primary",
                                    size="sm",
                                    hx_post="/theme/dark",
                                    hx_target="body",
                                    cls="btn-glow mb-2",
                                ),
                                Br(),
                                Small("Click to toggle themes", cls="text-muted"),
                            ),
                            cls="p-4",
                        ),
                        cls="glass-card border-0 h-100",
                    ),
                    span=12,
                    md=4,
                    cls="mb-4",
                ),
                # Toast Container
                ToastContainer(
                    Toast(
                        Icon("check-circle-fill", cls="me-2"),
                        "Dashboard loaded successfully!",
                        title="Welcome",
                        variant="success",
                        autohide=True,
                        delay=3000,
                        id="welcomeToast",
                    ),
                    position="top-end",
                ),
                # Welcome Modal
                Modal(
                    Div(
                        H4("🚀 Welcome to FastStrap!", cls="modal-title gradient-text"),
                        P("You're viewing a modern dashboard built with 100% Python."),
                        Ul(
                            Li(Icon("check", cls="text-success me-2"), "20+ Bootstrap components"),
                            Li(Icon("check", cls="text-success me-2"), "Glassmorphism design"),
                            Li(Icon("check", cls="text-success me-2"), "Dark theme optimized"),
                            Li(Icon("check", cls="text-success me-2"), "HTMX ready"),
                            cls="mb-3",
                        ),
                        Div(
                            Alert(
                                Icon("lightning", cls="me-2"),
                                "Try the form inputs and interactive components!",
                                variant="info",
                                dismissible=True,
                            ),
                            cls="mt-3",
                        ),
                        cls="p-3",
                    ),
                    modal_id="welcomeModal",
                    title="",
                    footer=Div(
                        Button(
                            "Get Started",
                            variant="primary",
                            data_bs_dismiss="modal",
                            cls="btn-glow",
                        ),
                        Button("View Docs", variant="outline-light", cls="btn-glow"),
                    ),
                ),
                cls="py-4",
            ),
            cls="ms-0 ms-lg-4",
        ),
    )


# ==============================================
# ADDITIONAL ROUTES FOR FUNCTIONALITY
# ==============================================


@app.route("/theme/<mode>")
def toggle_theme(mode: str):
    """HTMX endpoint to toggle theme."""
    if mode == "light":
        return """
        <script>
        document.documentElement.setAttribute('data-bs-theme', 'light');
        document.body.style.background = 'linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%)';
        </script>
        """
    else:
        return """
        <script>
        document.documentElement.setAttribute('data-bs-theme', 'dark');
        document.body.style.background = 'linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%)';
        </script>
        """


@app.route("/api/stats")
def get_stats():
    """API endpoint for live stats (HTMX compatible)."""
    import random

    return Div(
        Row(
            Col(
                Div(
                    Strong(f"{random.randint(95, 100)}%", cls="h4 mb-0"),
                    Small("Uptime", cls="text-muted d-block"),
                    cls="text-center",
                ),
                span=3,
                cls="mb-3",
            ),
            Col(
                Div(
                    Strong(f"+{random.randint(30, 50)}%", cls="h4 mb-0"),
                    Small("Growth", cls="text-muted d-block"),
                    cls="text-center",
                ),
                span=3,
                cls="mb-3",
            ),
            Col(
                Div(
                    Strong(f"{random.randint(1200, 1300)}", cls="h4 mb-0"),
                    Small("Users", cls="text-muted d-block"),
                    cls="text-center",
                ),
                span=3,
                cls="mb-3",
            ),
            Col(
                Div(
                    Strong("20", cls="h4 mb-0"),
                    Small("Components", cls="text-muted d-block"),
                    cls="text-center",
                ),
                span=3,
                cls="mb-3",
            ),
        )
    )


if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("🎨 FASTSTRAP MODERN DASHBOARD")
    print("=" * 70)
    print("\n✨ Features:")
    print("   • Glassmorphism design with gradients")
    print("   • All forms working perfectly")
    print("   • 20+ FastStrap components showcased")
    print("   • Modern dark theme with custom CSS")
    print("   • HTMX integration for interactivity")
    print("   • Responsive & mobile-friendly")
    print("\n📍 Visit: http://localhost:5000")
    print("\n🎯 Interactive Elements:")
    print("   • Click ☰ to open sidebar")
    print("   • Try all form inputs")
    print("   • Click alerts to dismiss")
    print("   • Switch themes with buttons")
    print("   • Watch toast notifications")
    print("\n" + "=" * 70)
    serve(port=5000)
