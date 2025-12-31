"""Demo app showcasing all Faststrap enhancements."""

from fasthtml.common import FastHTML, serve, Div, H1, H2, H3, P, Br, A, Title, Style, Script

from faststrap import (
    # Core
    add_bootstrap,
    # Theme
    create_theme,
    # Forms
    Button,
    CloseButton,
    ButtonGroup,
    Input,
    Select,
    # Display
    Card,
    Badge,
    # Feedback
    Alert,
    Modal,
    Drawer,
    Toast,
    SimpleToast,
    ToastContainer,
    Spinner,
    Progress,
    # Navigation
    Navbar,
    Dropdown,
    Tabs,
    TabPane,
    Breadcrumb,
    Pagination,
    # Utils
    Icon,
)

app = FastHTML()

# Example 1: Custom theme with device preference (RECOMMENDED)
custom_theme = create_theme(
    primary="red",
    secondary="#E9ECEF",
    info="#17A2B8",
    warning="#FFC107",
    danger="#DC3545",
    success="#28A745",
    light="#F8F9FA",
    dark="#343A40",
)

add_bootstrap(app, theme=custom_theme, mode="light", include_favicon=True)

# Alternative examples (commented out):
# add_bootstrap(app, theme="purple-magic", mode="native")  # Built-in theme with device preference
# add_bootstrap(app, theme="green-nature", mode="dark")    # Force dark mode
# add_bootstrap(app, theme="blue-ocean", mode="light")     # Force light mode



@app.route("/")
def home():
    return Div(
        # Navbar
        Navbar(
            brand="Faststrap Demo",
            items=[
                A("Home", href="#", cls="nav-link"),
                A("Docs", href="#", cls="nav-link"),
                A("GitHub", href="#", cls="nav-link"),
            ],
            bg="primary",
            variant="dark",
            sticky="top",
        ),
        # Breadcrumb
        Breadcrumb(
            (Icon("house"), "/"),
            ("Demo", None),
        ),
        # Hero section
        Div(
            H1("Faststrap Enhancements Demo", cls="display-4 fw-bold"),
            P("See all the new features: attrs/style, slot classes, themes, CloseButton, and more.", cls="lead"),
            Button("Open Modal", variant="primary", data_bs_toggle="modal", data_bs_target="#demoModal"),
            Button("Open Drawer", variant="success", data_bs_toggle="offcanvas", data_bs_target="#demoDrawer"),
            cls="py-5 text-center",
        ),
        # Components showcase
        showcase_section(),
        # Toast container
        ToastContainer(),
        # Modal
        demo_modal(),
        # Drawer
        demo_drawer(),
        cls="container",
    )


def showcase_section():
    return Div(
        H2("Component Enhancements", cls="mb-4"),
        # Button enhancements
        Card(
            H3("Button Enhancements", cls="card-title"),
            P("as_, css_vars, slot controls, CloseButton, etc."),
            Button("Primary", variant="primary"),
            Button("As Link", as_="a", href="#", variant="secondary"),
            Button("Loading", loading=True, spinner=True, loading_text="Working..."),
            Button("Icon + Spinner", icon="check-circle", spinner=True, css_vars={"--bs-btn-padding-y": "0.75rem"}),
            Button("Full Width", full_width=True, variant="info"),
            Button("Pill", pill=True, variant="warning"),
            Button("Active", active=True, variant="success"),
            cls="mb-3",
        ),
        # Card slot classes
        Card(
            H3("Card Slot Classes", cls="card-title"),
            P("header_cls, body_cls, footer_cls, title_cls, etc."),
            header=Div("Custom Header", cls="bg-primary text-white p-3"),
            body=Div("Custom body with padding", cls="p-4"),
            footer=Div("Custom footer", cls="text-muted"),
            header_cls="custom-header",
            body_cls="custom-body",
            footer_cls="custom-footer",
            cls="mb-3",
        ),
        # Modal slot classes
        Card(
            H3("Modal Slot Classes", cls="card-title"),
            P("dialog_cls, content_cls, header_cls, etc."),
            Button("Open Modal", variant="primary", data_bs_toggle="modal", data_bs_target="#modalSlots"),
            Modal(
                "Modal body with custom classes",
                title="Custom Modal",
                modal_id="modalSlots",
                dialog_cls="custom-dialog",
                content_cls="custom-content",
                header_cls="custom-header",
                body_cls="custom-body",
                footer_cls="custom-footer",
                footer=Button("Close", variant="secondary", data_bs_dismiss="modal"),
            ),
            cls="mb-3",
        ),
        # Drawer slot classes
        Card(
            H3("Drawer Slot Classes", cls="card-title"),
            P("header_cls, body_cls, title_cls, close_cls"),
            Button("Open Drawer", variant="success", data_bs_toggle="offcanvas", data_bs_target="#drawerSlots"),
            Drawer(
                "Drawer body with custom classes",
                title="Custom Drawer",
                drawer_id="drawerSlots",
                header_cls="custom-header",
                body_cls="custom-body",
                title_cls="custom-title",
                close_cls="custom-close",
            ),
            cls="mb-3",
        ),
        # Dropdown slot classes
        Card(
            H3("Dropdown Slot Classes", cls="card-title"),
            P("toggle_cls, menu_cls, item_cls"),
            Dropdown(
                "Option 1",
                "Option 2",
                "---",
                "Option 3",
                label="Dropdown",
                toggle_cls="custom-toggle",
                menu_cls="custom-menu",
                item_cls="custom-item",
            ),
            cls="mb-3",
        ),
        # Attrs/style enhancements
        Card(
            H3("Attrs/Style Enhancements", cls="card-title"),
            P("style dict, css_vars, data, aria"),
            Button(
                "Styled",
                variant="primary",
                style={"background-color": "#6F42C1", "border": "none"},
                css_vars={"--bs-btn-padding-y": "0.75rem", "--bs-btn-border-radius": "12px"},
                data={"id": "123", "type": "demo"},
                aria={"label": "Styled button"},
            ),
            cls="mb-3",
        ),
        # Theme demo
        Card(
            H3("Theme Demo", cls="card-title"),
            P("Built-in theme applied via create_theme"),
            Badge("Primary", variant="primary"),
            Badge("Secondary", variant="secondary"),
            cls="mb-3",
        ),
        # CloseButton
        Card(
            H3("CloseButton Helper", cls="card-title"),
            P("Reusable close button for alerts, modals, drawers"),
            Alert(
                "This alert uses CloseButton helper",
                variant="info",
                dismissible=True,
            ),
            cls="mb-3",
        ),
        # Tabs (with improved dark mode visibility)
        Tabs(
            ("overview", "Overview", True),
            ("features", "Features"),
            ("examples", "Examples"),
        ),
        Div(
            TabPane("Overview content - Notice the active tab is now more visible in dark mode", tab_id="overview", active=True),
            TabPane("Features content - Tabs work great with any theme", tab_id="features"),
            TabPane("Examples content - Try switching between light/dark modes", tab_id="examples"),
            cls="tab-content p-3",
        ),
        # Progress
        Progress(75, variant="success", striped=True, animated=True, label="75%"),
        Br(),
        # Spinner
        Spinner(size="sm", label="Small spinner"),
        Spinner(label="Default spinner"),
        Br(),
        # Pagination with custom CSS
        Div(
            Pagination(current_page=3, total_pages=10, size="lg", align="center"),
            cls="pagination-wrapper",
        ),
        # Toast demo - SimpleToast (no JavaScript required)
        Card(
            H3("SimpleToast Demo (No JavaScript)", cls="card-title"),
            P("Auto-hiding toast that works without JavaScript"),
            Button("Show Success Toast", variant="success", hx_get="/simple-toast/success", hx_target="#simpleToastContainer", hx_swap="beforeend"),
            Button("Show Error Toast", variant="danger", hx_get="/simple-toast/error", hx_target="#simpleToastContainer", hx_swap="beforeend"),
            Button("Show Info Toast", variant="info", hx_get="/simple-toast/info", hx_target="#simpleToastContainer", hx_swap="beforeend"),
            Div(id="simpleToastContainer", cls="mt-3"),
            cls="mb-3",
        ),
        # Custom CSS for pagination
        Style("""
            /* Ensure pagination items are properly layered */
            .pagination-wrapper .page-item .page-link {
                position: relative;
                z-index: 1;
            }
            .pagination-wrapper .page-item.active .page-link {
                z-index: 2;
            }
            /* Improve spacing between pagination numbers */
            .pagination-wrapper .page-item .page-link {
                margin: 0 2px;
            }
        """),
    )


def demo_modal():
    return Modal(
        "This modal demonstrates the new slot class overrides and CloseButton helper.",
        title="Demo Modal",
        modal_id="demoModal",
        dialog_cls="shadow-lg",
        content_cls="border-0",
        header_cls="bg-primary text-white",
        body_cls="p-4",
        footer_cls="border-0",
        footer=Div(
            Button("Close", variant="secondary", data_bs_dismiss="modal"),
            Button("Save changes", variant="primary"),
            cls="d-flex justify-content-end gap-2",
        ),
    )


def demo_drawer():
    return Drawer(
        "This drawer shows slot class overrides and CloseButton helper.",
        title="Demo Drawer",
        drawer_id="demoDrawer",
        header_cls="bg-success text-white",
        body_cls="p-4",
        title_cls="text-white",
        close_cls="btn-close-white",
    )


@app.route("/simple-toast/success")
def simple_toast_success():
    return SimpleToast("Operation completed successfully!", title="Success", variant="success", duration=3)

@app.route("/simple-toast/error")
def simple_toast_error():
    return SimpleToast("An error occurred. Please try again.", title="Error", variant="danger", duration=5)

@app.route("/simple-toast/info")
def simple_toast_info():
    return SimpleToast("This is an informational message.", title="Info", variant="info", duration=4)


if __name__ == "__main__":
    serve(port=8030)
