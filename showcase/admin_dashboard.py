"""
Showcase 2 — Admin Dashboard
A modern analytics dashboard with live-updating metrics, auto-refresh panels,
search, error handling, and scroll-reveal animations.
Demonstrates: AutoRefresh, ActiveSearch, StatCard, ErrorPage, LoadingButton,
Toast, Tabs, Badge, Table, Fx effects.
"""

import random
from typing import Any

from fasthtml.common import (
    H3,
    H4,
    H5,
    A,
    Br,
    Code,
    Div,
    FastHTML,
    P,
    Small,
    Span,
    Strong,
    serve,
)

from faststrap import (
    Alert,
    Badge,
    Button,
    Card,
    Col,
    ErrorPage,
    FormGroup,
    Fx,
    Icon,
    Input,
    ListGroup,
    ListGroupItem,
    Row,
    StatCard,
    Table,
    TabPane,
    Tabs,
    ThemeToggle,
    ToastContainer,
    add_bootstrap,
)
from faststrap.presets import ActiveSearch, AutoRefresh, LoadingButton, toast_response

app = FastHTML()
add_bootstrap(app)


# ─── Mock Data ───────────────────────────────────────────────────────
USERS: list[dict[str, Any]] = [
    {
        "id": 1,
        "name": "Alice Johnson",
        "email": "alice@example.com",
        "role": "Admin",
        "status": "Active",
    },
    {
        "id": 2,
        "name": "Bob Smith",
        "email": "bob@example.com",
        "role": "Editor",
        "status": "Active",
    },
    {
        "id": 3,
        "name": "Charlie Brown",
        "email": "charlie@example.com",
        "role": "Viewer",
        "status": "Inactive",
    },
    {
        "id": 4,
        "name": "Diana Prince",
        "email": "diana@example.com",
        "role": "Admin",
        "status": "Active",
    },
    {
        "id": 5,
        "name": "Eve Adams",
        "email": "eve@example.com",
        "role": "Editor",
        "status": "Active",
    },
    {
        "id": 6,
        "name": "Frank Castle",
        "email": "frank@example.com",
        "role": "Viewer",
        "status": "Inactive",
    },
    {
        "id": 7,
        "name": "Grace Hopper",
        "email": "grace@example.com",
        "role": "Admin",
        "status": "Active",
    },
    {
        "id": 8,
        "name": "Hank Pym",
        "email": "hank@example.com",
        "role": "Editor",
        "status": "Active",
    },
]


def sidebar() -> Any:
    """Dashboard sidebar navigation."""
    links = [
        ("speedometer2", "Dashboard", "/", True),
        ("people-fill", "Users", "#users", False),
        ("bar-chart-fill", "Analytics", "#analytics", False),
        ("gear-fill", "Settings", "#settings", False),
        ("bell-fill", "Notifications", "#notifs", False),
    ]
    return Div(
        Div(
            H4(
                Icon("grid-fill", cls="me-2 text-primary"),
                "FastStrap",
                cls="text-white mb-0",
            ),
            cls="p-3 border-bottom border-secondary",
        ),
        Div(
            *[
                A(
                    Icon(icon, cls="me-3"),
                    label,
                    href=href,
                    cls=(
                        "d-flex align-items-center px-3 py-2 text-decoration-none rounded mb-1"
                        f" {'bg-primary text-white' if active else 'text-white-50'}"
                    ),
                )
                for icon, label, href, active in links
            ],
            cls="p-3",
        ),
        Div(
            ThemeToggle(
                current_theme="dark",
                endpoint="/api/toggle-theme",
                show_label=True,
                label_text="Dark Mode",
            ),
            cls="p-3 mt-auto border-top border-secondary",
        ),
        cls="d-flex flex-column bg-dark vh-100 position-fixed",
        style="width: 250px;",
    )


def dashboard_content() -> Any:
    """Main dashboard content."""
    return Div(
        # ── Top Bar ──────────────────────────────────────────
        Div(
            Row(
                Col(
                    H3("Dashboard", cls=f"mb-0 {Fx.fade_in}"),
                    cols=12,
                    md=6,
                ),
                Col(
                    Div(
                        ActiveSearch(
                            endpoint="/api/search-users",
                            target="#search-panel",
                            placeholder="Search users...",
                            debounce=300,
                            cls="form-control-sm",
                        ),
                        cls="d-flex justify-content-end",
                    ),
                    cols=12,
                    md=6,
                ),
                cls="align-items-center mb-4",
            ),
            cls="border-bottom pb-3 mb-4",
        ),
        # Search results panel (hidden by default)
        Div(id="search-panel"),
        # ── Stat Cards (Auto-Refreshing) ─────────────────────
        Div(
            Row(
                Col(
                    AutoRefresh(
                        endpoint="/api/stats/users",
                        target="#stat-users",
                        interval=10000,
                    ),
                    id="stat-users",
                    cols=12,
                    md=6,
                    lg=3,
                    cls="mb-4",
                ),
                Col(
                    AutoRefresh(
                        endpoint="/api/stats/revenue",
                        target="#stat-revenue",
                        interval=10000,
                    ),
                    id="stat-revenue",
                    cols=12,
                    md=6,
                    lg=3,
                    cls="mb-4",
                ),
                Col(
                    AutoRefresh(
                        endpoint="/api/stats/orders",
                        target="#stat-orders",
                        interval=10000,
                    ),
                    id="stat-orders",
                    cols=12,
                    md=6,
                    lg=3,
                    cls="mb-4",
                ),
                Col(
                    AutoRefresh(
                        endpoint="/api/stats/uptime",
                        target="#stat-uptime",
                        interval=10000,
                    ),
                    id="stat-uptime",
                    cols=12,
                    md=6,
                    lg=3,
                    cls="mb-4",
                ),
            ),
            cls=f"{Fx.fade_in}",
        ),
        # ── Main Content Tabs ────────────────────────────────
        Div(
            Tabs(
                ("users-tab", "Users", True),
                ("analytics-tab", "Analytics"),
                ("settings-tab", "Settings"),
                variant="pills",
                cls="mb-4",
            ),
            Div(
                TabPane(
                    # Users table
                    Div(
                        Div(
                            H5("Team Members", cls="mb-0"),
                            LoadingButton(
                                Icon("plus-lg", cls="me-2"),
                                "Add User",
                                endpoint="/api/add-user",
                                target="#toast-container",
                                variant="primary",
                            ),
                            cls="d-flex justify-content-between align-items-center mb-3",
                        ),
                        Table(
                            thead=[
                                "Name",
                                "Email",
                                "Role",
                                "Status",
                                "Actions",
                            ],
                            data=[
                                [
                                    Div(
                                        Div(
                                            u["name"][0],
                                            cls=(
                                                "rounded-circle bg-primary text-white"
                                                " d-flex align-items-center justify-content-center me-2"
                                            ),
                                            style="width: 32px; height: 32px; font-size: 14px;",
                                        ),
                                        u["name"],
                                        cls="d-flex align-items-center",
                                    ),
                                    u["email"],
                                    Badge(
                                        u["role"],
                                        variant="primary" if u["role"] == "Admin" else "secondary",
                                        pill=True,
                                    ),
                                    Badge(
                                        u["status"],
                                        variant="success" if u["status"] == "Active" else "danger",
                                        pill=True,
                                    ),
                                    Div(
                                        Button(
                                            Icon("pencil"),
                                            variant="primary",
                                            outline=True,
                                            size="sm",
                                            cls="me-1",
                                        ),
                                        Button(
                                            Icon("trash"),
                                            variant="danger",
                                            outline=True,
                                            size="sm",
                                        ),
                                    ),
                                ]
                                for u in USERS
                            ],
                            striped=True,
                            hover=True,
                            responsive=True,
                            cls=f"{Fx.fade_in}",
                        ),
                    ),
                    tab_id="users-tab",
                    active=True,
                ),
                TabPane(
                    Div(
                        Row(
                            Col(
                                Card(
                                    H5("Revenue Trend", cls="card-title"),
                                    Div(
                                        P(
                                            "Chart placeholder — in production, use",
                                            Br(),
                                            Code("Faststrap.charts"),
                                            " (coming in v0.6.0)",
                                            cls="text-muted text-center py-5",
                                        ),
                                        cls="bg-body-tertiary rounded",
                                    ),
                                    cls=f"{Fx.fade_in} {Fx.hover_lift}",
                                ),
                                cols=12,
                                lg=8,
                                cls="mb-4",
                            ),
                            Col(
                                Card(
                                    H5("Top Pages", cls="card-title"),
                                    ListGroup(
                                        *[
                                            ListGroupItem(
                                                Div(
                                                    Span(page, cls="fw-medium"),
                                                    Badge(
                                                        f"{views}",
                                                        variant="primary",
                                                        pill=True,
                                                    ),
                                                    cls="d-flex justify-content-between",
                                                )
                                            )
                                            for page, views in [
                                                ("/dashboard", 1247),
                                                ("/products", 892),
                                                ("/settings", 543),
                                                ("/users", 432),
                                            ]
                                        ],
                                        flush=True,
                                    ),
                                    cls=f"{Fx.fade_in} {Fx.delay_sm}",
                                ),
                                cols=12,
                                lg=4,
                                cls="mb-4",
                            ),
                        ),
                    ),
                    tab_id="analytics-tab",
                ),
                TabPane(
                    Card(
                        H5("Application Settings", cls="card-title"),
                        FormGroup(
                            Input(
                                name="app_name",
                                value="My Application",
                            ),
                            label="Application Name",
                        ),
                        FormGroup(
                            Input(
                                name="support_email",
                                type="email",
                                value="support@example.com",
                            ),
                            label="Support Email",
                        ),
                        LoadingButton(
                            "Save Settings",
                            endpoint="/api/save-settings",
                            target="#toast-container",
                            variant="primary",
                        ),
                        cls=f"{Fx.fade_in}",
                    ),
                    tab_id="settings-tab",
                ),
                cls="tab-content",
            ),
            cls=f"{Fx.slide_up} {Fx.delay_sm}",
        ),
        # Toast container
        ToastContainer(position="top-end"),
        cls="p-4",
        style="margin-left: 250px;",
    )


@app.get("/")
def home() -> Any:
    return Div(
        sidebar(),
        dashboard_content(),
        cls="d-flex",
    )


# ─── API Endpoints ───────────────────────────────────────────────────
@app.get("/api/stats/users")
def stats_users() -> Any:
    val = 1247 + random.randint(-5, 15)
    return StatCard(
        title="Total Users",
        value=f"{val:,}",
        icon="people-fill",
        trend=f"+{random.randint(1, 10)}",
        trend_label="today",
        cls=f"{Fx.fade_in}",
    )


@app.get("/api/stats/revenue")
def stats_revenue() -> Any:
    val = 48200 + random.randint(-500, 800)
    return StatCard(
        title="Revenue",
        value=f"${val:,.0f}",
        icon="currency-dollar",
        trend=f"+{random.randint(1, 8)}%",
        trend_label="this week",
        cls=f"{Fx.fade_in}",
    )


@app.get("/api/stats/orders")
def stats_orders() -> Any:
    val = 342 + random.randint(-5, 12)
    return StatCard(
        title="Orders",
        value=str(val),
        icon="cart-fill",
        trend=f"+{random.randint(1, 15)}",
        trend_label="this month",
        cls=f"{Fx.fade_in}",
    )


@app.get("/api/stats/uptime")
def stats_uptime() -> Any:
    return StatCard(
        title="Uptime",
        value="99.9%",
        icon="check-circle-fill",
        cls=f"{Fx.fade_in}",
    )


@app.get("/api/search-users")
def search_users(q: str = "") -> Any:
    if len(q) < 2:
        return ""
    results = [
        u for u in USERS if q.lower() in u["name"].lower() or q.lower() in u["email"].lower()
    ]
    if not results:
        return Alert("No users found", variant="info", dismissible=True)
    return Card(
        ListGroup(
            *[
                ListGroupItem(
                    Div(
                        Strong(u["name"]),
                        Br(),
                        Small(u["email"], cls="text-muted"),
                    ),
                    Badge(u["role"], variant="primary", pill=True),
                    cls="d-flex justify-content-between align-items-center",
                )
                for u in results
            ],
            flush=True,
        ),
        cls=f"mb-4 {Fx.fade_in} {Fx.shadow_soft}",
    )


@app.post("/api/add-user")
def add_user() -> Any:
    return toast_response(
        content="",
        message="New user invitation sent!",
        variant="success",
    )


@app.post("/api/save-settings")
def save_settings() -> Any:
    return toast_response(
        content="",
        message="Settings saved successfully.",
        variant="success",
    )


@app.post("/api/toggle-theme")
def toggle_theme() -> Any:
    return toast_response(
        content="",
        message="Theme toggled!",
        variant="info",
    )


@app.get("/error")
def error_page() -> Any:
    return ErrorPage(
        404,
        action_text="Go Home",
        action_href="/",
    )


serve()
