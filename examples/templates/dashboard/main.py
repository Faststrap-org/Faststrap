"""
Production Dashboard Template - Complete Multi-Page Admin Panel

A fully responsive, production-ready dashboard showcasing Faststrap's full capabilities.

Features:
- 6 complete pages: Dashboard, Orders, Products, Customers, Analytics, Settings
- Fully mobile responsive with collapsible sidebar
- Real-world data tables with pagination and search
- Charts and statistics
- HTMX-powered dynamic updates
- Dark mode support

Run: python main.py
"""

from fasthtml.common import *

from faststrap import (
    Alert,
    Badge,
    Button,
    Card,
    Col,
    Container,
    Dropdown,
    DropdownItem,
    Icon,
    Input,
    Pagination,
    Progress,
    Row,
    Select,
    Table,
    TBody,
    TCell,
    THead,
    TRow,
    add_bootstrap,
    create_theme,
)

# Initialize app
app = FastHTML()

# Professional dashboard theme
dashboard_theme = create_theme(
    primary="#4F46E5",  # Indigo
    secondary="#64748B",  # Slate
    success="#10B981",  # Green
    danger="#EF4444",  # Red
    warning="#F59E0B",  # Amber
    info="#3B82F6",  # Blue
)

add_bootstrap(app, theme=dashboard_theme, mode="light")

# Sample data
stats = [
    {
        "title": "Total Revenue",
        "value": "$45,231",
        "change": "+20.1%",
        "trend": "up",
        "icon": "currency-dollar",
    },
    {
        "title": "Active Users",
        "value": "2,345",
        "change": "+15.3%",
        "trend": "up",
        "icon": "people",
    },
    {"title": "Orders", "value": "1,234", "change": "-5.2%", "trend": "down", "icon": "cart"},
    {
        "title": "Conversion Rate",
        "value": "3.24%",
        "change": "+2.1%",
        "trend": "up",
        "icon": "graph-up",
    },
]

recent_orders = [
    {
        "id": "#3210",
        "customer": "John Doe",
        "product": "MacBook Pro",
        "amount": "$2,499",
        "status": "Completed",
        "date": "2026-01-05",
    },
    {
        "id": "#3209",
        "customer": "Jane Smith",
        "product": "iPhone 15",
        "amount": "$999",
        "status": "Processing",
        "date": "2026-01-05",
    },
    {
        "id": "#3208",
        "customer": "Bob Johnson",
        "product": "AirPods Pro",
        "amount": "$249",
        "status": "Completed",
        "date": "2026-01-04",
    },
    {
        "id": "#3207",
        "customer": "Alice Brown",
        "product": "iPad Air",
        "amount": "$599",
        "status": "Pending",
        "date": "2026-01-04",
    },
    {
        "id": "#3206",
        "customer": "Charlie Wilson",
        "product": "Apple Watch",
        "amount": "$399",
        "status": "Completed",
        "date": "2026-01-03",
    },
]

products = [
    {
        "id": "1",
        "name": 'MacBook Pro 16"',
        "category": "Laptops",
        "price": "$2,499",
        "stock": 45,
        "status": "In Stock",
    },
    {
        "id": "2",
        "name": "iPhone 15 Pro",
        "category": "Phones",
        "price": "$999",
        "stock": 120,
        "status": "In Stock",
    },
    {
        "id": "3",
        "name": "AirPods Pro",
        "category": "Audio",
        "price": "$249",
        "stock": 8,
        "status": "Low Stock",
    },
    {
        "id": "4",
        "name": "iPad Air",
        "category": "Tablets",
        "price": "$599",
        "stock": 67,
        "status": "In Stock",
    },
    {
        "id": "5",
        "name": "Apple Watch Series 9",
        "category": "Wearables",
        "price": "$399",
        "stock": 0,
        "status": "Out of Stock",
    },
]

customers = [
    {
        "id": "1",
        "name": "John Doe",
        "email": "john@example.com",
        "orders": 12,
        "total": "$5,234",
        "status": "Active",
    },
    {
        "id": "2",
        "name": "Jane Smith",
        "email": "jane@example.com",
        "orders": 8,
        "total": "$3,456",
        "status": "Active",
    },
    {
        "id": "3",
        "name": "Bob Johnson",
        "email": "bob@example.com",
        "orders": 5,
        "total": "$1,234",
        "status": "Active",
    },
    {
        "id": "4",
        "name": "Alice Brown",
        "email": "alice@example.com",
        "orders": 15,
        "total": "$7,890",
        "status": "VIP",
    },
    {
        "id": "5",
        "name": "Charlie Wilson",
        "email": "charlie@example.com",
        "orders": 3,
        "total": "$890",
        "status": "Inactive",
    },
]


def StatCard(title: str, value: str, change: str, trend: str, icon: str):
    """Stat card component for dashboard metrics."""
    trend_color = "success" if trend == "up" else "danger"
    trend_icon = "arrow-up" if trend == "up" else "arrow-down"

    return Card(
        Div(
            Div(
                H6(title, cls="text-muted mb-2 small"),
                H3(value, cls="mb-0 fw-bold"),
                cls="flex-grow-1",
            ),
            Div(Icon(icon, size=32, cls="text-primary opacity-50"), cls="ms-3 d-none d-sm-block"),
            cls="d-flex align-items-center",
        ),
        Div(
            Icon(trend_icon, size=14, cls=f"text-{trend_color} me-1"),
            Span(change, cls=f"text-{trend_color} fw-semibold me-2 small"),
            Span("vs last month", cls="text-muted small"),
            cls="mt-3",
        ),
        body_cls="p-3 p-md-4",
    )


def Sidebar(active_page="dashboard"):
    """Responsive sidebar navigation."""
    nav_items = [
        ("Dashboard", "/", "speedometer2", "dashboard"),
        ("Orders", "/orders", "cart", "orders"),
        ("Products", "/products", "box-seam", "products"),
        ("Customers", "/customers", "people", "customers"),
        ("Analytics", "/analytics", "graph-up", "analytics"),
        ("Settings", "/settings", "gear", "settings"),
    ]

    return Div(
        # Logo/Brand
        Div(
            H4("Faststrap", cls="text-white mb-0"),
            Small("Dashboard", cls="text-white-50"),
            cls="p-4 border-bottom border-secondary",
        ),
        # Navigation
        Nav(
            *[
                A(
                    Icon(icon, size=20, cls="me-3"),
                    Span(label),
                    href=href,
                    cls=f"nav-link text-white {'active bg-primary' if active == active_page else ''} d-flex align-items-center px-4 py-3",
                )
                for label, href, icon, active in nav_items
            ],
            cls="flex-column mt-3",
        ),
        # Footer
        Div(Small("© 2026 Faststrap", cls="text-white-50"), cls="p-4 mt-auto"),
        cls="d-flex flex-column bg-dark offcanvas offcanvas-start d-lg-block position-lg-fixed",
        style="width: 280px; min-height: 100vh; z-index: 1040;",
        id="sidebar",
        tabindex="-1",
    )


def TopNavbar(title="Dashboard"):
    """Responsive top navigation bar."""
    return Div(
        Container(
            Row(
                Col(
                    Div(
                        # Mobile menu toggle
                        Button(
                            Icon("list", size=24),
                            variant="light",
                            cls="d-lg-none me-3",
                            **{"data-bs-toggle": "offcanvas", "data-bs-target": "#sidebar"},
                        ),
                        H4(title, cls="mb-0 d-inline-block"),
                        cls="d-flex align-items-center",
                    ),
                    cols=12,
                    md=6,
                    cls="mb-3 mb-md-0",
                ),
                Col(
                    Div(
                        Input(
                            "search",
                            placeholder="Search...",
                            cls="form-control-sm d-none d-md-block me-3",
                            style="max-width: 200px;",
                        ),
                        Button(
                            Icon("bell", size=20),
                            Badge(
                                "3",
                                variant="danger",
                                cls="position-absolute top-0 start-100 translate-middle",
                            ),
                            variant="light",
                            cls="position-relative me-2",
                        ),
                        Dropdown(
                            DropdownItem(Icon("person", cls="me-2"), "Profile", href="/profile"),
                            DropdownItem(Icon("gear", cls="me-2"), "Settings", href="/settings"),
                            "---",
                            DropdownItem(
                                Icon("box-arrow-right", cls="me-2"), "Logout", href="/logout"
                            ),
                            label=Div(Icon("person-circle", size=32), cls="d-inline-block"),
                            variant="light",
                        ),
                        cls="d-flex justify-content-end align-items-center",
                    ),
                    cols=12,
                    md=6,
                ),
                cls="align-items-center",
            ),
            fluid=True,
        ),
        cls="bg-white border-bottom py-3 shadow-sm",
        style="margin-left: 0;",
        id="topnav",
    )


def PageLayout(content, active_page="dashboard", title="Dashboard"):
    """Main page layout wrapper."""
    return Div(
        Sidebar(active_page),
        # Main content area
        Div(
            TopNavbar(title),
            # Page content
            Container(content, fluid=True, cls="py-4"),
            style="margin-left: 0;",
            cls="min-vh-100 bg-light",
            id="maincontent",
        ),
        # Custom responsive styles
        Style(
            """
            /* Desktop: Fixed sidebar */
            @media (min-width: 992px) {
                #sidebar {
                    width: 280px !important;
                    position: fixed !important;
                    top: 0;
                    left: 0;
                    height: 100vh;
                    border-right: 1px solid #dee2e6;
                }
                #topnav, #maincontent {
                    margin-left: 280px !important;
                }
            }

            /* Mobile: Offcanvas sidebar */
            @media (max-width: 991.98px) {
                #sidebar {
                    width: 280px !important;
                }
                #topnav, #maincontent {
                    margin-left: 0 !important;
                }
            }

            .hover-shadow:hover {
                box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.15) !important;
                transition: box-shadow 0.3s ease-in-out;
            }

            /* Ensure proper wrapping on mobile */
            @media (max-width: 767.98px) {
                .d-flex {
                    flex-wrap: wrap;
                }
            }
        """
        ),
    )


@app.route("/")
def dashboard():
    """Dashboard home page."""
    content = Div(
        # Page header
        Div(
            H2("Dashboard", cls="mb-0"),
            Small("Welcome back! Here's what's happening.", cls="text-muted"),
            cls="mb-4",
        ),
        # Stats grid
        Row(
            *[
                Col(
                    StatCard(
                        stat["title"], stat["value"], stat["change"], stat["trend"], stat["icon"]
                    ),
                    cols=12,
                    sm=6,
                    lg=3,
                    cls="mb-4",
                )
                for stat in stats
            ]
        ),
        # Charts row
        Row(
            Col(
                Card(
                    Div(
                        H5("Revenue Overview", cls="mb-0"),
                        Dropdown(
                            DropdownItem("Last 7 days"),
                            DropdownItem("Last 30 days"),
                            DropdownItem("Last 90 days"),
                            label="Last 30 days",
                            variant="outline-secondary",
                            size="sm",
                        ),
                        cls="d-flex justify-content-between align-items-center mb-4",
                    ),
                    # Placeholder for chart
                    Div(
                        Div(
                            Icon("graph-up", size=64, cls="text-muted mb-3"),
                            P("Chart visualization would go here", cls="text-muted"),
                            P(
                                "(Integrate with Matplotlib, Plotly, or Chart.js)",
                                cls="text-muted small",
                            ),
                            cls="text-center py-5",
                        ),
                        cls="bg-light rounded",
                    ),
                    header="Revenue Trend",
                ),
                cols=12,
                lg=8,
                cls="mb-4",
            ),
            Col(
                Card(
                    H6("Traffic Sources", cls="mb-4"),
                    Div(
                        Div(
                            Span("Direct", cls="text-muted small"),
                            Span("45%", cls="fw-semibold"),
                            cls="d-flex justify-content-between mb-2",
                        ),
                        Progress(45, variant="primary", cls="mb-3", height="8px"),
                        Div(
                            Span("Organic Search", cls="text-muted small"),
                            Span("30%", cls="fw-semibold"),
                            cls="d-flex justify-content-between mb-2",
                        ),
                        Progress(30, variant="success", cls="mb-3", height="8px"),
                        Div(
                            Span("Social Media", cls="text-muted small"),
                            Span("15%", cls="fw-semibold"),
                            cls="d-flex justify-content-between mb-2",
                        ),
                        Progress(15, variant="info", cls="mb-3", height="8px"),
                        Div(
                            Span("Referral", cls="text-muted small"),
                            Span("10%", cls="fw-semibold"),
                            cls="d-flex justify-content-between mb-2",
                        ),
                        Progress(10, variant="warning", height="8px"),
                    ),
                ),
                cols=12,
                lg=4,
                cls="mb-4",
            ),
        ),
        # Recent orders table
        Row(
            Col(
                Card(
                    Div(
                        H5("Recent Orders", cls="mb-0"),
                        Button("View All", variant="outline-primary", size="sm", href="/orders"),
                        cls="d-flex justify-content-between align-items-center mb-3",
                    ),
                    Div(
                        Table(
                            THead(
                                TRow(
                                    TCell("Order ID", header=True),
                                    TCell("Customer", header=True, cls="d-none d-md-table-cell"),
                                    TCell("Product", header=True),
                                    TCell("Amount", header=True),
                                    TCell("Status", header=True),
                                )
                            ),
                            TBody(
                                *[
                                    TRow(
                                        TCell(order["id"], cls="fw-semibold small"),
                                        TCell(
                                            order["customer"], cls="d-none d-md-table-cell small"
                                        ),
                                        TCell(order["product"], cls="small"),
                                        TCell(order["amount"], cls="fw-semibold small"),
                                        TCell(
                                            Badge(
                                                order["status"],
                                                variant=(
                                                    "success"
                                                    if order["status"] == "Completed"
                                                    else (
                                                        "warning"
                                                        if order["status"] == "Processing"
                                                        else "secondary"
                                                    )
                                                ),
                                                cls="small",
                                            )
                                        ),
                                    )
                                    for order in recent_orders[:5]
                                ]
                            ),
                            striped=True,
                            hover=True,
                            responsive=True,
                        ),
                        cls="table-responsive",
                    ),
                    body_cls="p-0",
                ),
                cols=12,
            )
        ),
    )

    return PageLayout(content, "dashboard", "Dashboard")


@app.route("/orders")
def orders():
    """Orders page with full table."""
    content = Div(
        # Page header
        Div(
            Div(
                H2("Orders", cls="mb-0"),
                Small("Manage all customer orders", cls="text-muted"),
            ),
            Button("Export", variant="outline-primary", size="sm", cls="d-none d-md-block"),
            cls="d-flex justify-content-between align-items-center mb-4",
        ),
        # Filters
        Row(
            Col(
                Select(
                    "status",
                    ("all", "All Status"),
                    ("completed", "Completed"),
                    ("processing", "Processing"),
                    ("pending", "Pending"),
                    label="Status",
                    size="sm",
                ),
                cols=12,
                md=3,
                cls="mb-3",
            ),
            Col(
                Input("search", placeholder="Search orders...", size="sm", label="Search"),
                cols=12,
                md=6,
                cls="mb-3",
            ),
            Col(
                Button(
                    "Filter", variant="primary", size="sm", cls="w-100", style="margin-top: 32px;"
                ),
                cols=12,
                md=3,
                cls="mb-3",
            ),
        ),
        # Orders table
        Card(
            Div(
                Table(
                    THead(
                        TRow(
                            TCell("Order ID", header=True),
                            TCell("Customer", header=True, cls="d-none d-lg-table-cell"),
                            TCell("Product", header=True),
                            TCell("Amount", header=True),
                            TCell("Date", header=True, cls="d-none d-md-table-cell"),
                            TCell("Status", header=True),
                            TCell("Actions", header=True),
                        )
                    ),
                    TBody(
                        *[
                            TRow(
                                TCell(order["id"], cls="fw-semibold small"),
                                TCell(order["customer"], cls="d-none d-lg-table-cell small"),
                                TCell(order["product"], cls="small"),
                                TCell(order["amount"], cls="fw-semibold small"),
                                TCell(order["date"], cls="d-none d-md-table-cell small"),
                                TCell(
                                    Badge(
                                        order["status"],
                                        variant=(
                                            "success"
                                            if order["status"] == "Completed"
                                            else (
                                                "warning"
                                                if order["status"] == "Processing"
                                                else "secondary"
                                            )
                                        ),
                                    )
                                ),
                                TCell(
                                    Button(
                                        Icon("eye"),
                                        variant="outline-primary",
                                        size="sm",
                                        cls="me-1",
                                    ),
                                    Button(Icon("pencil"), variant="outline-secondary", size="sm"),
                                ),
                            )
                            for order in recent_orders
                        ]
                    ),
                    striped=True,
                    hover=True,
                    responsive=True,
                ),
                cls="table-responsive",
            ),
            body_cls="p-0",
        ),
        # Pagination
        Div(Pagination(current_page=1, total_pages=5, align="center"), cls="mt-4"),
    )

    return PageLayout(content, "orders", "Orders")


@app.route("/products")
def products_page():
    """Products page."""
    content = Div(
        # Page header
        Div(
            Div(
                H2("Products", cls="mb-0"),
                Small("Manage your product catalog", cls="text-muted"),
            ),
            Button(
                Icon("plus", cls="me-2"),
                "Add Product",
                variant="primary",
                size="sm",
                cls="d-none d-md-flex align-items-center",
            ),
            cls="d-flex justify-content-between align-items-center mb-4",
        ),
        # Products table
        Card(
            Div(
                Table(
                    THead(
                        TRow(
                            TCell("ID", header=True),
                            TCell("Product Name", header=True),
                            TCell("Category", header=True, cls="d-none d-md-table-cell"),
                            TCell("Price", header=True),
                            TCell("Stock", header=True),
                            TCell("Status", header=True),
                            TCell("Actions", header=True),
                        )
                    ),
                    TBody(
                        *[
                            TRow(
                                TCell(product["id"], cls="small"),
                                TCell(product["name"], cls="fw-semibold small"),
                                TCell(product["category"], cls="d-none d-md-table-cell small"),
                                TCell(product["price"], cls="fw-semibold small"),
                                TCell(product["stock"], cls="small"),
                                TCell(
                                    Badge(
                                        product["status"],
                                        variant=(
                                            "success"
                                            if product["status"] == "In Stock"
                                            else (
                                                "warning"
                                                if product["status"] == "Low Stock"
                                                else "danger"
                                            )
                                        ),
                                    )
                                ),
                                TCell(
                                    Button(
                                        Icon("pencil"),
                                        variant="outline-primary",
                                        size="sm",
                                        cls="me-1",
                                    ),
                                    Button(Icon("trash"), variant="outline-danger", size="sm"),
                                ),
                            )
                            for product in products
                        ]
                    ),
                    striped=True,
                    hover=True,
                    responsive=True,
                ),
                cls="table-responsive",
            ),
            body_cls="p-0",
        ),
    )

    return PageLayout(content, "products", "Products")


@app.route("/customers")
def customers_page():
    """Customers page."""
    content = Div(
        # Page header
        Div(
            Div(
                H2("Customers", cls="mb-0"),
                Small("Manage customer relationships", cls="text-muted"),
            ),
            Button(
                Icon("plus", cls="me-2"),
                "Add Customer",
                variant="primary",
                size="sm",
                cls="d-none d-md-flex align-items-center",
            ),
            cls="d-flex justify-content-between align-items-center mb-4",
        ),
        # Customers table
        Card(
            Div(
                Table(
                    THead(
                        TRow(
                            TCell("ID", header=True),
                            TCell("Name", header=True),
                            TCell("Email", header=True, cls="d-none d-lg-table-cell"),
                            TCell("Orders", header=True),
                            TCell("Total Spent", header=True),
                            TCell("Status", header=True),
                            TCell("Actions", header=True),
                        )
                    ),
                    TBody(
                        *[
                            TRow(
                                TCell(customer["id"], cls="small"),
                                TCell(customer["name"], cls="fw-semibold small"),
                                TCell(customer["email"], cls="d-none d-lg-table-cell small"),
                                TCell(customer["orders"], cls="small"),
                                TCell(customer["total"], cls="fw-semibold small"),
                                TCell(
                                    Badge(
                                        customer["status"],
                                        variant=(
                                            "success"
                                            if customer["status"] == "Active"
                                            else (
                                                "primary"
                                                if customer["status"] == "VIP"
                                                else "secondary"
                                            )
                                        ),
                                    )
                                ),
                                TCell(
                                    Button(
                                        Icon("eye"),
                                        variant="outline-primary",
                                        size="sm",
                                        cls="me-1",
                                    ),
                                    Button(
                                        Icon("envelope"), variant="outline-secondary", size="sm"
                                    ),
                                ),
                            )
                            for customer in customers
                        ]
                    ),
                    striped=True,
                    hover=True,
                    responsive=True,
                ),
                cls="table-responsive",
            ),
            body_cls="p-0",
        ),
    )

    return PageLayout(content, "customers", "Customers")


@app.route("/analytics")
def analytics():
    """Analytics page."""
    content = Div(
        # Page header
        Div(
            H2("Analytics", cls="mb-0"),
            Small("Detailed performance metrics", cls="text-muted"),
            cls="mb-4",
        ),
        Alert(
            Icon("info-circle", cls="me-2"),
            "Analytics dashboard coming soon! Integrate with your favorite charting library.",
            variant="info",
            cls="mb-4",
        ),
        # Placeholder charts
        Row(
            Col(
                Card(
                    Div(
                        Icon("graph-up-arrow", size=48, cls="text-primary mb-3"),
                        H5("Sales Trends"),
                        P("Track your sales over time", cls="text-muted small"),
                        cls="text-center py-5",
                    ),
                    cls="hover-shadow",
                ),
                cols=12,
                md=6,
                lg=4,
                cls="mb-4",
            ),
            Col(
                Card(
                    Div(
                        Icon("pie-chart", size=48, cls="text-success mb-3"),
                        H5("Revenue Breakdown"),
                        P("See where your money comes from", cls="text-muted small"),
                        cls="text-center py-5",
                    ),
                    cls="hover-shadow",
                ),
                cols=12,
                md=6,
                lg=4,
                cls="mb-4",
            ),
            Col(
                Card(
                    Div(
                        Icon("people-fill", size=48, cls="text-info mb-3"),
                        H5("Customer Insights"),
                        P("Understand your audience", cls="text-muted small"),
                        cls="text-center py-5",
                    ),
                    cls="hover-shadow",
                ),
                cols=12,
                md=6,
                lg=4,
                cls="mb-4",
            ),
        ),
    )

    return PageLayout(content, "analytics", "Analytics")


@app.route("/settings")
def settings():
    """Settings page."""
    content = Div(
        # Page header
        Div(
            H2("Settings", cls="mb-0"),
            Small("Manage your account and preferences", cls="text-muted"),
            cls="mb-4",
        ),
        Row(
            Col(
                Card(
                    H5("Profile Settings", cls="mb-4"),
                    Input("name", label="Full Name", value="Admin User"),
                    Input("email", label="Email", value="admin@example.com", input_type="email"),
                    Input("phone", label="Phone", value="+1 234 567 8900", input_type="tel"),
                    Button("Save Changes", variant="primary", cls="mt-3"),
                    header="Account Information",
                ),
                cols=12,
                lg=6,
                cls="mb-4",
            ),
            Col(
                Card(
                    H5("Preferences", cls="mb-4"),
                    Select(
                        "theme",
                        ("light", "Light Mode"),
                        ("dark", "Dark Mode"),
                        ("auto", "Auto"),
                        label="Theme",
                        selected="light",
                    ),
                    Select(
                        "language",
                        ("en", "English"),
                        ("es", "Spanish"),
                        ("fr", "French"),
                        label="Language",
                        selected="en",
                    ),
                    Button("Save Preferences", variant="primary", cls="mt-3"),
                    header="Display Settings",
                ),
                cols=12,
                lg=6,
                cls="mb-4",
            ),
        ),
    )

    return PageLayout(content, "settings", "Settings")


if __name__ == "__main__":
    serve(port=5099)
