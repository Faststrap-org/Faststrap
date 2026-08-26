"""Flagship showcase — Nexus Admin Dashboard.

Production-grade analytics dashboard for Faststrap:

- StatCard + AutoRefresh for live-updating KPI panels (10s interval)
- ActiveSearch with debounce for real-time user filtering
- Tabs (pills) with Users, Analytics, and Settings panes
- Chart.js bar chart for monthly revenue (Analytics tab)
- LoadingButton with toast feedback for Add User / Save Settings
- Dark-first dashboard shell with a fixed premium contrast palette
- ErrorPage at /error route
- Responsive: Bootstrap offcanvas sidebar for mobile
- Custom CSS: Inter font, sidebar gradient, stat card glow accent,
  skeleton pulse, hover row highlight — cinematic but minimal.
"""

from __future__ import annotations

import json
import random
from typing import Any

from fasthtml.common import (
    H3,
    H5,
    H6,
    A,
    Canvas,
    Div,
    FastHTML,
    P,
    Script,
    Small,
    Span,
    Strong,
    Style,
    serve,
)

from faststrap import (
    Alert,
    Badge,
    Card,
    Col,
    ErrorPage,
    FormGroup,
    Fx,
    Icon,
    Input,
    ListGroup,
    ListGroupItem,
    PageMeta,
    Row,
    StatCard,
    Table,
    TabPane,
    Tabs,
    ToastContainer,
    add_bootstrap,
    create_theme,
)
from faststrap.presets import ActiveSearch, AutoRefresh, LoadingButton, toast_response

# ── Theme ──────────────────────────────────────────────────────────────────────
NEXUS_THEME = create_theme(
    primary="#6366F1",  # indigo
    secondary="#64748B",  # slate
    success="#10B981",
    danger="#F43F5E",
    warning="#F59E0B",
    info="#0EA5E9",
    dark="#0D1117",
    light="#F8FAFC",
)

app = FastHTML()
add_bootstrap(app, theme=NEXUS_THEME, font_family="Inter", mode="dark")

# ── Mock Data ──────────────────────────────────────────────────────────────────
USERS: list[dict[str, Any]] = [
    {
        "id": 1,
        "name": "Alice Johnson",
        "email": "alice@nexus.io",
        "role": "Admin",
        "status": "Active",
        "joined": "Jan 2024",
    },
    {
        "id": 2,
        "name": "Bob Smith",
        "email": "bob@nexus.io",
        "role": "Editor",
        "status": "Active",
        "joined": "Feb 2024",
    },
    {
        "id": 3,
        "name": "Charlie Brown",
        "email": "charlie@nexus.io",
        "role": "Viewer",
        "status": "Inactive",
        "joined": "Mar 2024",
    },
    {
        "id": 4,
        "name": "Diana Prince",
        "email": "diana@nexus.io",
        "role": "Admin",
        "status": "Active",
        "joined": "Jan 2024",
    },
    {
        "id": 5,
        "name": "Eve Adams",
        "email": "eve@nexus.io",
        "role": "Editor",
        "status": "Active",
        "joined": "Apr 2024",
    },
    {
        "id": 6,
        "name": "Frank Castle",
        "email": "frank@nexus.io",
        "role": "Viewer",
        "status": "Inactive",
        "joined": "May 2024",
    },
    {
        "id": 7,
        "name": "Grace Hopper",
        "email": "grace@nexus.io",
        "role": "Admin",
        "status": "Active",
        "joined": "Jun 2024",
    },
    {
        "id": 8,
        "name": "Hank Pym",
        "email": "hank@nexus.io",
        "role": "Editor",
        "status": "Active",
        "joined": "Jul 2024",
    },
]

REVENUE_DATA = {
    "type": "bar",
    "data": {
        "labels": [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
        ],
        "datasets": [
            {
                "label": "Revenue ($K)",
                "data": [38, 45, 52, 41, 63, 71, 58, 66, 79, 84, 92, 108],
                "backgroundColor": "rgba(99,102,241,0.75)",
                "borderColor": "#6366F1",
                "borderWidth": 2,
                "borderRadius": 6,
                "borderSkipped": False,
            },
            {
                "label": "Expenses ($K)",
                "data": [22, 28, 31, 25, 38, 42, 35, 39, 46, 51, 55, 62],
                "backgroundColor": "rgba(100,116,139,0.45)",
                "borderColor": "#64748B",
                "borderWidth": 1,
                "borderRadius": 6,
                "borderSkipped": False,
            },
        ],
    },
    "options": {
        "responsive": True,
        "maintainAspectRatio": False,
        "plugins": {
            "legend": {"position": "top", "labels": {"usePointStyle": True}},
            "tooltip": {"mode": "index", "intersect": False},
        },
        "scales": {
            "x": {"grid": {"display": False}},
            "y": {
                "beginAtZero": True,
                "grid": {"color": "rgba(0,0,0,0.05)"},
                "ticks": {"callback": "function(v){ return '$'+v+'K'; }"},
            },
        },
    },
}

TOP_PAGES = [
    ("/dashboard", "4,821 views", "+12%", "success"),
    ("/products", "3,109 views", "+8%", "success"),
    ("/users", "2,047 views", "-2%", "danger"),
    ("/settings", "1,384 views", "+0%", "secondary"),
    ("/analytics", "987 views", "+18%", "success"),
]

RECENT_ACTIVITY = [
    ("Alice Johnson", "Exported user report", "2 min ago", "people-fill", "primary"),
    ("Bob Smith", "Updated product #4821", "14 min ago", "pencil-fill", "warning"),
    ("System", "Backup completed", "1 hour ago", "hdd-fill", "success"),
    ("Diana Prince", "Revoked API key", "3 hours ago", "key-fill", "danger"),
    ("Grace Hopper", "Added new workspace", "Yesterday", "folder-plus", "info"),
]

# ── CSS ────────────────────────────────────────────────────────────────────────
CSS = """
/* ════════════════════════════════════════════════════════════
   Nexus Admin · Premium Dashboard CSS
   Philosophy: cinematic dark sidebar, airy white content,
   stat card accent glow, micro-animations on every row.
   Atmospheric only — Bootstrap/Faststrap own layout.
   ════════════════════════════════════════════════════════════ */

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

/* ── Shell ──────────────────────────────────────────────────── */
.nx-shell {
  display: flex;
  min-height: 100vh;
  font-family: "Inter", system-ui, sans-serif;
}

/* ── Sidebar ────────────────────────────────────────────────── */
.nx-sidebar {
  width: 260px;
  background: linear-gradient(180deg, #0d1117 0%, #161b22 100%);
  display: flex;
  flex-direction: column;
  position: fixed;
  top: 0; left: 0; bottom: 0;
  z-index: 1040;
  transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 4px 0 24px rgba(0,0,0,0.25);
}

@media (max-width: 991px) {
  .nx-sidebar { transform: translateX(-100%); }
  .nx-sidebar.show { transform: translateX(0); }
  .nx-main { margin-left: 0 !important; }
}

.nx-sidebar-brand {
  padding: 1.5rem 1.5rem 1rem;
  border-bottom: 1px solid rgba(255,255,255,0.06);
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.nx-brand-icon {
  width: 2.2rem;
  height: 2.2rem;
  border-radius: 8px;
  background: linear-gradient(135deg, #6366F1, #818CF8);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1rem;
  color: #fff;
  box-shadow: 0 4px 12px rgba(99,102,241,0.4);
}

.nx-brand-text {
  font-size: 1.15rem;
  font-weight: 800;
  color: #fff;
  letter-spacing: -0.02em;
}

.nx-brand-badge {
  font-size: 0.6rem;
  background: rgba(99,102,241,0.25);
  color: #818CF8;
  border-radius: 4px;
  padding: 0.1rem 0.35rem;
  font-weight: 600;
  letter-spacing: 0.04em;
  margin-left: auto;
}

.nx-nav-section {
  padding: 1rem 0.75rem 0.5rem;
}

.nx-nav-label {
  font-size: 0.65rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #4B5563;
  padding: 0 0.75rem;
  margin-bottom: 0.35rem;
}

.nx-nav-link {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.6rem 0.75rem;
  border-radius: 8px;
  color: #9CA3AF;
  text-decoration: none;
  font-size: 0.88rem;
  font-weight: 500;
  position: relative;
  transition: background 0.15s ease, color 0.15s ease;
  margin-bottom: 0.1rem;
}

.nx-nav-link:hover {
  background: rgba(255,255,255,0.05);
  color: #E5E7EB;
}

.nx-nav-link.active {
  background: rgba(99,102,241,0.15);
  color: #818CF8;
}

.nx-nav-link.active::before {
  content: "";
  position: absolute;
  left: -0.75rem;
  top: 50%;
  transform: translateY(-50%);
  width: 3px;
  height: 60%;
  background: #6366F1;
  border-radius: 0 2px 2px 0;
}

.nx-nav-link .nx-icon {
  width: 1.75rem;
  height: 1.75rem;
  border-radius: 6px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.9rem;
  flex-shrink: 0;
  background: rgba(255,255,255,0.04);
}

.nx-nav-link.active .nx-icon {
  background: rgba(99,102,241,0.25);
  color: #818CF8;
}

.nx-sidebar-footer {
  padding: 1rem 1.25rem;
  border-top: 1px solid rgba(255,255,255,0.06);
  margin-top: auto;
}

.nx-user-chip {
  display: flex;
  align-items: center;
  gap: 0.65rem;
  border-radius: 10px;
  padding: 0.6rem;
  background: rgba(255,255,255,0.04);
  cursor: pointer;
  transition: background 0.15s ease;
}

.nx-user-chip:hover { background: rgba(255,255,255,0.08); }

.nx-user-avatar {
  width: 2rem;
  height: 2rem;
  border-radius: 50%;
  background: linear-gradient(135deg, #6366F1, #818CF8);
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 0.75rem;
  flex-shrink: 0;
}

/* ── Main Content ───────────────────────────────────────────── */
.nx-main {
  margin-left: 260px;
  flex: 1;
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  background: #F8FAFC;
}

/* ── Top Bar ────────────────────────────────────────────────── */
.nx-topbar {
  background: rgba(255,255,255,0.9);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid rgba(0,0,0,0.06);
  padding: 0.75rem 1.5rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: sticky;
  top: 0;
  z-index: 100;
}

.nx-breadcrumb {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  font-size: 0.82rem;
  color: #6B7280;
}

.nx-breadcrumb-current {
  color: #111827;
  font-weight: 600;
}

.nx-topbar-actions {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.nx-notif-btn {
  width: 2.25rem;
  height: 2.25rem;
  border-radius: 50%;
  border: 1px solid rgba(0,0,0,0.08);
  background: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #6B7280;
  cursor: pointer;
  position: relative;
  transition: background 0.15s ease;
}

.nx-notif-btn:hover { background: #F3F4F6; }

.nx-notif-dot {
  position: absolute;
  top: 4px; right: 4px;
  width: 7px; height: 7px;
  background: #F43F5E;
  border-radius: 50%;
  border: 1.5px solid #fff;
}

/* ── Content Area ───────────────────────────────────────────── */
.nx-content { padding: 2rem 1.5rem; flex: 1; }

/* ── Stat Cards ─────────────────────────────────────────────── */
.nx-stat-accent {
  height: 3px;
  border-radius: 2px;
  margin-bottom: 1rem;
}

/* ── Activity Feed ──────────────────────────────────────────── */
.nx-activity-item {
  display: flex;
  align-items: flex-start;
  gap: 0.75rem;
  padding: 0.85rem 0;
  border-bottom: 1px solid rgba(0,0,0,0.04);
}

.nx-activity-item:last-child { border-bottom: none; }

.nx-activity-icon {
  width: 2.2rem;
  height: 2.2rem;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.85rem;
  flex-shrink: 0;
}

/* ── Table Enhancements ─────────────────────────────────────── */
.table > tbody > tr > td { vertical-align: middle; padding: 0.9rem 0.75rem; }
.table > tbody > tr { transition: background 0.12s ease; }
.table > tbody > tr:hover { background: rgba(99,102,241,0.04); }

/* ── Skeleton Pulse ─────────────────────────────────────────── */
@keyframes nx-pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.4; }
}

.nx-skeleton {
  animation: nx-pulse 1.5s ease infinite;
  background: #E5E7EB;
  border-radius: 6px;
}

/* ── Mobile hamburger ───────────────────────────────────────── */
.nx-hamburger {
  display: none;
  width: 2.25rem;
  height: 2.25rem;
  border-radius: 8px;
  border: 1px solid rgba(0,0,0,0.1);
  background: #fff;
  align-items: center;
  justify-content: center;
  cursor: pointer;
}

@media (max-width: 991px) {
  .nx-hamburger { display: flex; }
}
"""

# ── Chart JS init ──────────────────────────────────────────────────────────────
CHART_SCRIPT = f"""
document.addEventListener('DOMContentLoaded', function() {{
  const ctx = document.getElementById('revenue-chart');
  if (!ctx || !window.Chart) return;
  const config = {json.dumps(REVENUE_DATA)};
  // Override tick callback (can't serialize as func in JSON)
  config.options.scales.y.ticks.callback = function(v) {{ return '$' + v + 'K'; }};
  new Chart(ctx, config);
}});
"""


# ── UI Helpers ─────────────────────────────────────────────────────────────────


def nx_sidebar() -> Any:
    nav_items = [
        ("speedometer2", "Dashboard", "/", True),
        ("people-fill", "Users", "#users", False),
        ("bar-chart-fill", "Analytics", "#analytics", False),
        ("bell-fill", "Notifications", "#notifs", False),
    ]
    settings_items = [
        ("gear-fill", "Settings", "#settings", False),
        ("shield-lock", "Security", "#", False),
    ]
    return Div(
        # Brand
        Div(
            Div(Icon("grid-fill"), cls="nx-brand-icon"),
            Span("Nexus", cls="nx-brand-text"),
            Span("v2", cls="nx-brand-badge"),
            cls="nx-sidebar-brand",
        ),
        # Main nav
        Div(
            Div("Main", cls="nx-nav-label"),
            *[
                A(
                    Div(Icon(ic), cls="nx-icon"),
                    label,
                    href=href,
                    cls=f"nx-nav-link {'active' if active else ''}",
                )
                for ic, label, href, active in nav_items
            ],
            cls="nx-nav-section",
        ),
        # Settings nav
        Div(
            Div("Settings", cls="nx-nav-label"),
            *[
                A(
                    Div(Icon(ic), cls="nx-icon"),
                    label,
                    href=href,
                    cls=f"nx-nav-link {'active' if active else ''}",
                )
                for ic, label, href, active in settings_items
            ],
            cls="nx-nav-section",
        ),
        # Footer: user chip + shell note
        Div(
            Div(
                Div("SC", cls="nx-user-avatar"),
                Div(
                    Div("Sarah Chen", cls="text-white small fw-600 mb-0"),
                    Div("Admin", cls="text-secondary", style="font-size:0.72rem"),
                ),
                cls="nx-user-chip mb-2",
            ),
            Div(
                Icon("moon-stars-fill", cls="me-2 text-primary"),
                Span("Dark shell", cls="small fw-600 text-white"),
                cls="d-flex align-items-center text-secondary small",
            ),
            cls="nx-sidebar-footer",
        ),
        cls="nx-sidebar",
        id="nx-sidebar",
    )


def nx_topbar() -> Any:
    return Div(
        # Left: mobile hamburger + breadcrumb
        Div(
            Div(
                Icon("list", style="font-size:1.2rem; color:#374151"),
                cls="nx-hamburger me-3",
                **{
                    "data-bs-toggle": "collapse",
                    "data-bs-target": "#nx-sidebar",
                    "onclick": "document.getElementById('nx-sidebar').classList.toggle('show')",
                },
            ),
            Div(
                Icon("house-fill", cls="me-1 opacity-50"),
                Span("/ "),
                Span("Dashboard", cls="nx-breadcrumb-current"),
                cls="nx-breadcrumb",
            ),
            cls="d-flex align-items-center",
        ),
        # Right: search + notif + avatar
        Div(
            ActiveSearch(
                endpoint="/api/search-users",
                target="#search-panel",
                placeholder="Search users...",
                debounce=300,
                cls="form-control-sm",
                style="width:200px",
            ),
            Div(
                Icon("bell-fill", style="font-size:0.9rem"),
                Div(cls="nx-notif-dot"),
                cls="nx-notif-btn",
            ),
            Div(
                Div("SC", cls="nx-user-avatar"),
                cls="d-flex ms-1",
            ),
            cls="nx-topbar-actions",
        ),
        cls="nx-topbar",
    )


def role_badge(role: str) -> Any:
    color = {"Admin": "primary", "Editor": "warning", "Viewer": "secondary"}.get(role, "secondary")
    return Badge(role, variant=color, pill=True)


def nx_users_table() -> Any:
    return Table(
        thead=["", "Name", "Email", "Role", "Status", "Joined", "Actions"],
        data=[
            [
                Div(
                    Div(
                        u["name"][0],
                        cls="rounded-circle text-white d-flex align-items-center justify-content-center fw-700",
                        style=(
                            f"width:32px;height:32px;font-size:13px;background:"
                            f"{'#6366F1' if u['role']=='Admin' else '#F59E0B' if u['role']=='Editor' else '#64748B'};"
                        ),
                    ),
                ),
                Div(
                    Strong(u["name"], cls="d-block small"),
                    Small(f"ID #{u['id']}", cls="text-muted"),
                ),
                Small(u["email"], cls="text-muted"),
                role_badge(u["role"]),
                Badge(
                    u["status"],
                    variant="success" if u["status"] == "Active" else "danger",
                    pill=True,
                ),
                Small(u["joined"], cls="text-muted"),
                Div(
                    LoadingButton(
                        Icon("pencil"),
                        endpoint=f"/api/edit-user/{u['id']}",
                        target="#toast-container",
                        variant="primary",
                        outline=True,
                        size="sm",
                        cls="me-1",
                    ),
                    LoadingButton(
                        Icon("trash"),
                        endpoint=f"/api/delete-user/{u['id']}",
                        target="#toast-container",
                        variant="danger",
                        outline=True,
                        size="sm",
                    ),
                ),
            ]
            for u in USERS
        ],
        hover=True,
        responsive=True,
        cls=f"align-middle {Fx.fade_in}",
    )


def nx_activity_feed() -> Any:
    items = [
        Div(
            Div(
                Icon(icon),
                cls=f"nx-activity-icon bg-{color} bg-opacity-10 text-{color}",
            ),
            Div(
                Div(
                    Strong(name, cls="small"),
                    Small(f" · {time}", cls="text-muted"),
                ),
                Small(action, cls="text-muted"),
            ),
            cls="nx-activity-item",
        )
        for name, action, time, icon, color in RECENT_ACTIVITY
    ]
    return Card(
        H6("Recent Activity", cls="fw-700 mb-3"),
        Div(*items),
        cls=f"{Fx.fade_in}",
    )


def nx_stat_col(endpoint: str, stat_id: str, color: str, initial: Any = None, cols: int = 3) -> Any:
    return Col(
        Div(cls=f"nx-stat-accent bg-{color}"),
        # AutoRefresh targets itself so the accent bar is preserved.
        # initial= provides immediate content — no blank-state flash.
        AutoRefresh(
            endpoint=endpoint,
            target="this",
            interval=10000,
            content=initial,
        ),
        id=stat_id,
        cols=12,
        md=6,
        lg=cols,
        cls="mb-4",
    )


# ── Routes ─────────────────────────────────────────────────────────────────────


@app.get("/")
def home() -> Any:
    return Div(
        Style(CSS),
        PageMeta(
            title="Nexus Admin — Dashboard",
            description="Production-grade analytics dashboard built with Faststrap.",
        ),
        Script(src="https://cdn.jsdelivr.net/npm/chart.js"),
        # Layout shell
        Div(
            nx_sidebar(),
            # Main column
            Div(
                nx_topbar(),
                Div(
                    # Search results panel
                    Div(id="search-panel", cls="mb-4"),
                    # Page title
                    Div(
                        Div(
                            H3("Dashboard", cls="fw-800 mb-0", style="letter-spacing:-0.03em"),
                            P("Welcome back, Sarah.", cls="text-muted mb-0"),
                            cls="",
                        ),
                        LoadingButton(
                            Icon("plus-lg", cls="me-2"),
                            "Add User",
                            endpoint="/api/add-user",
                            target="#toast-container",
                            variant="primary",
                        ),
                        cls="d-flex justify-content-between align-items-center mb-4",
                    ),
                    # Stat cards — pre-populated on page load, refreshed every 10 s
                    Row(
                        nx_stat_col(
                            "/api/stats/users", "stat-users", "primary", initial=stats_users()
                        ),
                        nx_stat_col(
                            "/api/stats/revenue", "stat-revenue", "success", initial=stats_revenue()
                        ),
                        nx_stat_col(
                            "/api/stats/orders", "stat-orders", "warning", initial=stats_orders()
                        ),
                        nx_stat_col(
                            "/api/stats/uptime", "stat-uptime", "info", initial=stats_uptime()
                        ),
                        cls="mb-2",
                    ),
                    # ── Tabs ────────────────────────────────────
                    Tabs(
                        ("tab-users", "Users", True),
                        ("tab-analytics", "Analytics", False),
                        ("tab-settings", "Settings", False),
                        variant="pills",
                        cls="mb-4",
                    ),
                    Div(
                        # ── Users tab ───────────────────────────
                        TabPane(
                            Row(
                                Col(
                                    Card(
                                        Div(
                                            H5("Team Members", cls="mb-0 fw-700"),
                                            Badge(
                                                f"{len(USERS)} total",
                                                variant="light",
                                                cls="text-muted",
                                            ),
                                            cls="d-flex align-items-center gap-2 mb-3",
                                        ),
                                        nx_users_table(),
                                        cls=f"{Fx.fade_in}",
                                    ),
                                    cols=12,
                                    lg=8,
                                    cls="mb-4",
                                ),
                                Col(
                                    nx_activity_feed(),
                                    cols=12,
                                    lg=4,
                                    cls="mb-4",
                                ),
                            ),
                            tab_id="tab-users",
                            active=True,
                        ),
                        # ── Analytics tab ────────────────────────
                        TabPane(
                            Row(
                                Col(
                                    Card(
                                        H5("Monthly Revenue vs Expenses", cls="fw-700 mb-4"),
                                        Div(
                                            Canvas(
                                                id="revenue-chart",
                                                style="width:100%;height:320px;display:block;",
                                            ),
                                            style="height:320px;",
                                        ),
                                        Script(CHART_SCRIPT),
                                        cls=f"{Fx.fade_in}",
                                    ),
                                    cols=12,
                                    lg=8,
                                    cls="mb-4",
                                ),
                                Col(
                                    Card(
                                        H5("Top Pages", cls="fw-700 mb-3"),
                                        ListGroup(
                                            *[
                                                ListGroupItem(
                                                    Div(
                                                        Div(
                                                            Span(page, cls="fw-600 small d-block"),
                                                            Small(views, cls="text-muted"),
                                                        ),
                                                        Badge(
                                                            change,
                                                            variant=color,
                                                            pill=True,
                                                            cls="ms-auto",
                                                        ),
                                                        cls="d-flex align-items-center justify-content-between w-100",
                                                    )
                                                )
                                                for page, views, change, color in TOP_PAGES
                                            ],
                                            flush=True,
                                        ),
                                        cls=f"{Fx.fade_in}",
                                    ),
                                    cols=12,
                                    lg=4,
                                    cls="mb-4",
                                ),
                            ),
                            tab_id="tab-analytics",
                        ),
                        # ── Settings tab ─────────────────────────
                        TabPane(
                            Row(
                                Col(
                                    Card(
                                        H5("Application Settings", cls="fw-700 mb-3"),
                                        FormGroup(
                                            Input(name="app_name", value="Nexus Dashboard"),
                                            label="Application Name",
                                        ),
                                        FormGroup(
                                            Input(
                                                "support_email",
                                                input_type="email",
                                                value="support@nexus.io",
                                            ),
                                            label="Support Email",
                                        ),
                                        FormGroup(
                                            Input(name="domain", value="https://nexus.io"),
                                            label="Primary Domain",
                                        ),
                                        LoadingButton(
                                            Icon("check-lg", cls="me-2"),
                                            "Save Settings",
                                            endpoint="/api/save-settings",
                                            target="#toast-container",
                                            variant="primary",
                                        ),
                                        cls=f"{Fx.fade_in}",
                                    ),
                                    cols=12,
                                    lg=6,
                                    cls="mb-4",
                                ),
                                Col(
                                    Card(
                                        H5("Danger Zone", cls="fw-700 mb-3 text-danger"),
                                        P(
                                            "These actions are irreversible. Proceed with caution.",
                                            cls="text-muted small mb-3",
                                        ),
                                        Div(
                                            LoadingButton(
                                                Icon("arrow-repeat", cls="me-2"),
                                                "Reset All Settings",
                                                endpoint="/api/reset",
                                                target="#toast-container",
                                                variant="danger",
                                                outline=True,
                                                cls="me-2 mb-2",
                                            ),
                                            LoadingButton(
                                                Icon("trash", cls="me-2"),
                                                "Delete All Data",
                                                endpoint="/api/delete-all",
                                                target="#toast-container",
                                                variant="danger",
                                                cls="mb-2",
                                            ),
                                            cls="d-flex flex-wrap",
                                        ),
                                        cls=f"border-danger border-opacity-25 {Fx.fade_in}",
                                    ),
                                    cols=12,
                                    lg=6,
                                    cls="mb-4",
                                ),
                            ),
                            tab_id="tab-settings",
                        ),
                        cls="tab-content",
                    ),
                    cls="nx-content",
                ),
                cls="nx-main",
            ),
            cls="nx-shell",
        ),
        # Toast container
        ToastContainer(position="top-end"),
    )


# ── API endpoints ───────────────────────────────────────────────────────────────


@app.get("/api/stats/users")
def stats_users() -> Any:
    val = 1247 + random.randint(-5, 20)
    return StatCard(
        title="Total Users",
        value=f"{val:,}",
        icon=Icon("people-fill"),
        trend=f"+{random.randint(1, 10)}",
        trend_label="today",
        cls=f"{Fx.fade_in}",
    )


@app.get("/api/stats/revenue")
def stats_revenue() -> Any:
    val = 48200 + random.randint(-500, 1200)
    return StatCard(
        title="Monthly Revenue",
        value=f"${val:,.0f}",
        icon=Icon("currency-dollar"),
        trend=f"+{random.randint(2, 12)}%",
        trend_label="vs last month",
        cls=f"{Fx.fade_in}",
    )


@app.get("/api/stats/orders")
def stats_orders() -> Any:
    val = 342 + random.randint(-5, 18)
    return StatCard(
        title="Orders",
        value=str(val),
        icon=Icon("cart-fill"),
        trend=f"+{random.randint(1, 20)}",
        trend_label="this week",
        cls=f"{Fx.fade_in}",
    )


@app.get("/api/stats/uptime")
def stats_uptime() -> Any:
    val = round(99.8 + random.uniform(-0.1, 0.15), 2)
    return StatCard(
        title="Uptime",
        value=f"{val}%",
        icon=Icon("check-circle-fill"),
        trend="Healthy",
        trend_label="all systems",
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
        return Alert("No users found.", variant="info", dismissible=True, cls="mb-0")
    return Card(
        ListGroup(
            *[
                ListGroupItem(
                    Div(
                        Div(
                            u["name"][0],
                            cls="rounded-circle text-white d-flex align-items-center justify-content-center fw-700 me-3 flex-shrink-0",
                            style="width:32px;height:32px;font-size:13px;background:#6366F1;",
                        ),
                        Div(
                            Strong(u["name"], cls="d-block small"),
                            Small(u["email"], cls="text-muted"),
                        ),
                        role_badge(u["role"]),
                        cls="d-flex align-items-center",
                    )
                )
                for u in results
            ],
            flush=True,
        ),
        cls=f"mb-4 {Fx.fade_in}",
    )


@app.post("/api/add-user")
def add_user() -> Any:
    return toast_response("", message="Invitation sent successfully!", variant="success")


@app.post("/api/save-settings")
def save_settings() -> Any:
    return toast_response("", message="Settings saved.", variant="success")


@app.post("/api/reset")
def reset_settings() -> Any:
    return toast_response("", message="Settings reset to defaults.", variant="warning")


@app.post("/api/delete-all")
def delete_all() -> Any:
    return toast_response("", message="All data has been deleted.", variant="danger")


@app.post("/api/edit-user/{user_id}")
def edit_user(user_id: int) -> Any:
    return toast_response(
        "", message=f"User #{user_id} edit dialog would open here.", variant="info"
    )


@app.post("/api/delete-user/{user_id}")
def delete_user(user_id: int) -> Any:
    return toast_response("", message=f"User #{user_id} removed.", variant="danger")


@app.get("/error")
def error_page() -> Any:
    return ErrorPage(404, action_text="Back to Dashboard", action_href="/")


if __name__ == "__main__":
    serve(port=5010)
