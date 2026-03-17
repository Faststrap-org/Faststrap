"""Phase 3 Complete Demo - All 20 Components (12 + 8 New)

Showcases all new Phase 3 components alongside existing ones.
"""

from fasthtml.common import H1, H2, H3, A, Div, FastHTML, Li, P, Ul, serve

from faststrap import (
    Alert,
    Badge,
    Breadcrumb,
    # Phase 1+2 (12 components)
    Button,
    Card,
    Col,
    Container,
    Dropdown,
    Icon,
    Input,
    Navbar,
    Pagination,
    Progress,
    ProgressBar,
    Row,
    Select,
    Spinner,
    TabPane,
    # Phase 3 NEW (8 components)
    Tabs,
    add_bootstrap,
)

app = FastHTML()
add_bootstrap(app, mode="dark", use_cdn=True)


@app.route("/")
def home():
    return Div(
        # ============================================================================
        # NAVBAR
        # ============================================================================
        Navbar(
            Div(
                A("Home", href="/", cls="nav-link active"),
                A("Components", href="#components", cls="nav-link"),
                A(
                    "GitHub",
                    href="https://github.com/Faststrap-org/Faststrap",
                    cls="nav-link",
                    target="_blank",
                ),
                cls="navbar-nav me-auto",
            ),
            Div(Button("Get Started", variant="outline-light", size="sm"), cls="d-flex"),
            brand="FastStrap v0.3.0",
            brand_href="/",
            variant="dark",
            bg="primary",
            expand="lg",
            cls="shadow-lg mb-4",
        ),
        # ============================================================================
        # BREADCRUMB
        # ============================================================================
        Container(
            Breadcrumb((Icon("house-fill"), "/"), ("Components", "/components"), ("Phase 3", None)),
            cls="mb-4",
        ),
        # ============================================================================
        # HERO SECTION
        # ============================================================================
        Container(
            Div(
                H1(
                    Icon("lightning-charge-fill", cls="me-2"),
                    "FastStrap Phase 3 Complete!",
                    cls="display-4 fw-bold mb-3",
                ),
                P(
                    "20 Bootstrap components in pure Python. 8 new components added!",
                    cls="lead text-white-50 mb-4",
                ),
                Alert(
                    Icon("check-circle-fill", cls="me-2"),
                    "All 20 components are working perfectly!",
                    variant="success",
                    cls="mb-0",
                ),
                cls="text-center py-5 rounded-4 mb-5",
                style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);",
            ),
            # ============================================================================
            # TABS DEMO
            # ============================================================================
            Div(
                H2(Icon("folder-fill", cls="me-2"), "Tabs Navigation", cls="h3 mb-4"),
                # Horizontal tabs
                Tabs(("home", "Home", True), ("profile", "Profile"), ("contact", "Contact")),
                Div(
                    TabPane(
                        P("Home tab content. Click other tabs to switch!"),
                        tab_id="home",
                        active=True,
                    ),
                    TabPane(P("Profile tab content with information."), tab_id="profile"),
                    TabPane(P("Contact tab content with form."), tab_id="contact"),
                    cls="tab-content p-3 border border-top-0 rounded-bottom",
                ),
                # Pills variant
                H3("Pills Style", cls="h5 mt-4 mb-3"),
                Tabs(
                    ("tab1", "Tab 1", True), ("tab2", "Tab 2"), ("tab3", "Tab 3"), variant="pills"
                ),
                Div(
                    TabPane("Pills Tab 1 content", tab_id="tab1", active=True),
                    TabPane("Pills Tab 2 content", tab_id="tab2"),
                    TabPane("Pills Tab 3 content", tab_id="tab3"),
                    cls="tab-content p-3 mt-3",
                ),
                cls="mb-5",
            ),
            # ============================================================================
            # DROPDOWN DEMO
            # ============================================================================
            Div(
                H2(Icon("three-dots-vertical", cls="me-2"), "Dropdowns", cls="h3 mb-4"),
                Div(
                    # Regular dropdown
                    Dropdown(
                        "Action",
                        "Another action",
                        "---",  # Divider string
                        "Separated link",
                        label="Dropdown",
                        variant="primary",
                        cls="me-2 mb-2",
                    ),
                    # Split button
                    Dropdown(
                        "Edit",
                        "Delete",
                        "---",  # Divider string
                        "Archive",
                        label="Split Button",
                        variant="success",
                        split=True,
                        cls="me-2 mb-2",
                    ),
                    # Dropup
                    Dropdown(
                        "Item 1",
                        "Item 2",
                        "Item 3",
                        label="Dropup",
                        variant="info",
                        direction="up",
                        cls="me-2 mb-2",
                    ),
                    # Different sizes
                    Dropdown(
                        "Small",
                        "Menu",
                        label="Small",
                        variant="secondary",
                        size="sm",
                        cls="me-2 mb-2",
                    ),
                    Dropdown(
                        "Large", "Menu", label="Large", variant="warning", size="lg", cls="mb-2"
                    ),
                ),
                cls="mb-5",
            ),
            # ============================================================================
            # FORMS DEMO
            # ============================================================================
            Div(
                H2(Icon("ui-checks", cls="me-2"), "Form Components", cls="h3 mb-4"),
                Row(
                    Col(
                        # Input examples
                        H3("Text Inputs", cls="h5 mb-3"),
                        Input(
                            "email",
                            input_type="email",
                            label="Email Address",
                            placeholder="Enter email",
                            help_text="We'll never share your email",
                            required=True,
                        ),
                        Input(
                            "password",
                            input_type="password",
                            label="Password",
                            placeholder="Enter password",
                            required=True,
                        ),
                        Input(
                            "username", label="Username", placeholder="Choose username", size="lg"
                        ),
                        span=12,
                        md=6,
                        cls="mb-4",
                    ),
                    Col(
                        # Select examples
                        H3("Select Menus", cls="h5 mb-3"),
                        Select(
                            "country",
                            ("us", "United States"),
                            ("uk", "United Kingdom"),
                            ("ca", "Canada"),
                            ("au", "Australia"),
                            label="Country",
                            required=True,
                        ),
                        Select(
                            "size",
                            ("s", "Small"),
                            ("m", "Medium", True),
                            ("l", "Large"),
                            ("xl", "Extra Large"),
                            label="Size",
                            help_text="Select your preferred size",
                        ),
                        Select(
                            "tags",
                            ("python", "Python"),
                            ("js", "JavaScript"),
                            ("rust", "Rust"),
                            ("go", "Go"),
                            label="Technologies",
                            multiple=True,
                            size="lg",
                        ),
                        span=12,
                        md=6,
                        cls="mb-4",
                    ),
                ),
                cls="mb-5",
            ),
            # ============================================================================
            # PAGINATION DEMO
            # ============================================================================
            Div(
                H2(Icon("chevron-double-left", cls="me-2"), "Pagination", cls="h3 mb-4"),
                # Default pagination
                H3("Default", cls="h6 mb-3"),
                Pagination(current_page=5, total_pages=10, cls="mb-3"),
                # Large centered
                H3("Large Centered", cls="h6 mb-3"),
                Pagination(current_page=3, total_pages=8, size="lg", align="center", cls="mb-3"),
                # Small with first/last
                H3("Small with First/Last", cls="h6 mb-3"),
                Pagination(
                    current_page=7, total_pages=15, size="sm", show_first_last=True, cls="mb-3"
                ),
                cls="mb-5",
            ),
            # ============================================================================
            # LOADING STATES
            # ============================================================================
            Div(
                H2(Icon("hourglass-split", cls="me-2"), "Loading States", cls="h3 mb-4"),
                # Spinners
                H3("Spinners", cls="h5 mb-3"),
                Div(
                    Spinner(variant="primary", cls="me-2"),
                    Spinner(variant="success", cls="me-2"),
                    Spinner(variant="danger", cls="me-2"),
                    Spinner(variant="warning", cls="me-2"),
                    Spinner(variant="info", cls="me-2"),
                    Spinner(spinner_type="grow", variant="primary", cls="me-2"),
                    Spinner(spinner_type="grow", variant="success", cls="me-2"),
                    Spinner(size="sm", variant="secondary"),
                    cls="mb-4",
                ),
                # Progress bars
                H3("Progress Bars", cls="h5 mb-3"),
                Progress(25, variant="primary", label="25%", cls="mb-3"),
                Progress(50, variant="success", label="50%", cls="mb-3"),
                Progress(75, variant="info", striped=True, label="75%", cls="mb-3"),
                Progress(
                    90, variant="warning", striped=True, animated=True, label="90%", cls="mb-3"
                ),
                # Stacked progress
                H3("Stacked Progress", cls="h5 mb-3"),
                Div(
                    ProgressBar(15, variant="success"),
                    ProgressBar(30, variant="info"),
                    ProgressBar(20, variant="warning"),
                    cls="progress mb-3",
                ),
                # Custom height
                Progress(80, variant="primary", label="80%", height="30px", cls="mb-3"),
                cls="mb-5",
            ),
            # ============================================================================
            # ALL COMPONENTS GRID
            # ============================================================================
            Div(
                H2(Icon("grid-3x3-gap-fill", cls="me-2"), "All 20 Components", cls="h3 mb-4"),
                Row(
                    # Phase 1+2 Components
                    Col(
                        Card(
                            H3("Phase 1+2 (12)", cls="h5 mb-3"),
                            Ul(
                                Li(Icon("check", cls="text-success me-2"), "Button & ButtonGroup"),
                                Li(Icon("check", cls="text-success me-2"), "Badge"),
                                Li(Icon("check", cls="text-success me-2"), "Card"),
                                Li(Icon("check", cls="text-success me-2"), "Alert"),
                                Li(Icon("check", cls="text-success me-2"), "Toast"),
                                Li(Icon("check", cls="text-success me-2"), "Modal"),
                                Li(Icon("check", cls="text-success me-2"), "Drawer"),
                                Li(Icon("check", cls="text-success me-2"), "Navbar"),
                                Li(Icon("check", cls="text-success me-2"), "Container/Row/Col"),
                                Li(Icon("check", cls="text-success me-2"), "Icon"),
                                cls="list-unstyled",
                            ),
                            header=Badge("Complete", variant="success"),
                            cls="h-100",
                        ),
                        span=12,
                        md=6,
                        cls="mb-4",
                    ),
                    # Phase 3 Components
                    Col(
                        Card(
                            H3("Phase 3 NEW (8)", cls="h5 mb-3"),
                            Ul(
                                Li(Icon("star-fill", cls="text-warning me-2"), "Tabs & TabPane"),
                                Li(Icon("star-fill", cls="text-warning me-2"), "Dropdown"),
                                Li(Icon("star-fill", cls="text-warning me-2"), "Input"),
                                Li(Icon("star-fill", cls="text-warning me-2"), "Select"),
                                Li(Icon("star-fill", cls="text-warning me-2"), "Breadcrumb"),
                                Li(Icon("star-fill", cls="text-warning me-2"), "Pagination"),
                                Li(Icon("star-fill", cls="text-warning me-2"), "Spinner"),
                                Li(Icon("star-fill", cls="text-warning me-2"), "Progress"),
                                cls="list-unstyled",
                            ),
                            header=Badge("NEW!", variant="warning"),
                            cls="h-100",
                        ),
                        span=12,
                        md=6,
                        cls="mb-4",
                    ),
                ),
                cls="mb-5",
            ),
            cls="py-5",
        ),
    )


if __name__ == "__main__":
    print("\n" + "=" * 70)
    print(" FastStrap v0.2.4 - Phase 3  Complete Demo")
    print("=" * 70)
    print("\n Visit: http://localhost:5001")
    print("\n Total: 20 Components!")
    print("\n" + "=" * 70 + "\n")
    serve(port=5010)
