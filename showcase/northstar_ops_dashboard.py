"""Flagship showcase - Northstar Ops dashboard.

Premium analytics/admin reference for Faststrap:

- Bootstrap and Faststrap components for layout, controls, and data surfaces
- server-rendered filters and table state with zero custom JavaScript
- custom CSS reserved for atmosphere, hierarchy, and premium dashboard finish
"""

from __future__ import annotations

from collections import Counter
from datetime import date
from io import StringIO
from typing import Any
from urllib.parse import urlencode

from fasthtml.common import (
    H1,
    H3,
    H4,
    A,
    Div,
    FastHTML,
    Input,
    Li,
    P,
    Small,
    Span,
    Strong,
    Style,
    Ul,
    serve,
)
from starlette.responses import Response

from faststrap import (
    Card,
    Chart,
    Col,
    DashboardGrid,
    DashboardLayout,
    DataTable,
    DateRangePicker,
    ExportButton,
    FilterBar,
    Fx,
    Icon,
    KPICard,
    MetricCard,
    MultiSelect,
    NotificationCenter,
    RangeSlider,
    Row,
    SearchBar,
    Select,
    ThemeToggle,
    TrendCard,
    add_bootstrap,
    create_theme,
)
from faststrap.presets import hx_refresh

THEME_KEY = "northstar_theme"

NORTHSTAR_THEME = create_theme(
    primary="#6A6FF5",
    secondary="#111C33",
    success="#12B886",
    danger="#FF6B6B",
    warning="#F59F00",
    info="#4DABF7",
)

CSS = """
/* ═══════════════════════════════════════════════════════════
   Northstar · Premium CSS redesign
   Philosophy: precision dashboard geometry — 4-8px radii,
   sharp separator lines, intentional accent indicators.
   The goal is "operational clarity", not rounded-corner comfort.
   ═══════════════════════════════════════════════════════════ */

/* ── Page atmosphere ──────────────────────────────────────── */
.northstar-app {
  min-height: 100vh;
  background:
    radial-gradient(ellipse at 0% 0%, rgba(106, 111, 245, 0.2), transparent 28%),
    radial-gradient(ellipse at 100% 6%, rgba(77, 171, 247, 0.14), transparent 24%),
    linear-gradient(180deg, #070d1c 0%, #0a1221 48%, #0d1728 100%);
  color: #e2e8f0;
}

.northstar-app[data-bs-theme="light"] {
  background:
    radial-gradient(ellipse at 0% 0%, rgba(106, 111, 245, 0.08), transparent 30%),
    radial-gradient(ellipse at 100% 8%, rgba(77, 171, 247, 0.07), transparent 26%),
    linear-gradient(180deg, #edf2ff 0%, #f4f7fd 48%, #f0f4fb 100%);
  color: #0f172a;
}

/* ── Layout shell ─────────────────────────────────────────── */
.northstar-shell .dashboard-layout { min-height: 100vh; }

/* Sidebar — clean vertical rail */
.northstar-shell #sidebar-wrapper {
  background: linear-gradient(180deg, rgba(8, 14, 28, 0.97), rgba(10, 17, 33, 0.94)) !important;
  border-right: 1px solid rgba(255, 255, 255, 0.06) !important;
  backdrop-filter: blur(20px);
  box-shadow: 1px 0 0 rgba(255, 255, 255, 0.04), 20px 0 48px rgba(2, 6, 23, 0.3);
}

.northstar-app[data-bs-theme="light"] .northstar-shell #sidebar-wrapper {
  background: linear-gradient(180deg, rgba(255, 255, 255, 0.99), rgba(244, 248, 255, 0.97)) !important;
  border-right: 1px solid rgba(15, 23, 42, 0.08) !important;
  box-shadow: 1px 0 0 rgba(15, 23, 42, 0.04), 16px 0 40px rgba(15, 23, 42, 0.07);
}

.northstar-shell .sidebar-sticky { min-height: 100vh; }

/* Top navbar */
.northstar-shell .navbar {
  background: rgba(7, 13, 28, 0.78) !important;
  border-bottom: 1px solid rgba(255, 255, 255, 0.06) !important;
  backdrop-filter: blur(18px);
}

.northstar-app[data-bs-theme="light"] .northstar-shell .navbar {
  background: rgba(255, 255, 255, 0.88) !important;
  border-bottom: 1px solid rgba(15, 23, 42, 0.08) !important;
}

/* Transparent main content area */
.northstar-shell .main-content-wrapper,
.northstar-shell .main-content-wrapper > footer {
  background: transparent !important;
}

.northstar-shell .main-content-wrapper .container-fluid {
  padding-inline: 1.5rem;
}

/* ── Brand ────────────────────────────────────────────────── */
.northstar-brand {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  color: #f8fafc !important;
}

.northstar-app[data-bs-theme="light"] .northstar-brand { color: #0f172a !important; }

.northstar-brand-mark {
  width: 2rem;
  height: 2rem;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 6px;
  background: linear-gradient(135deg, #6a6ff5, #4dabf7);
  color: #fff;
  font-size: 0.88rem;
  box-shadow: 0 2px 12px rgba(106, 111, 245, 0.38);
  flex-shrink: 0;
}

/* ── Sidebar nav ──────────────────────────────────────────── */
.northstar-nav {
  display: grid;
  gap: 0.2rem;
}

.northstar-nav-link {
  display: flex;
  align-items: center;
  gap: 0.7rem;
  padding: 0.65rem 0.82rem;
  border-radius: 5px;
  color: rgba(203, 213, 225, 0.7);
  text-decoration: none;
  font-size: 0.86rem;
  font-weight: 500;
  letter-spacing: 0.01em;
  transition: color 0.15s ease, background 0.15s ease;
}

.northstar-nav-link:hover,
.northstar-nav-link:focus-visible {
  color: #e2e8f0;
  background: rgba(255, 255, 255, 0.06);
}

/* Active state — left accent bar instead of gradient bubble */
.northstar-nav-link.active {
  color: #fff;
  background: rgba(106, 111, 245, 0.12);
  border-left: 2px solid #6a6ff5;
  padding-left: calc(0.82rem - 2px);
}

.northstar-app[data-bs-theme="light"] .northstar-nav-link {
  color: rgba(51, 65, 85, 0.78);
}

.northstar-app[data-bs-theme="light"] .northstar-nav-link:hover,
.northstar-app[data-bs-theme="light"] .northstar-nav-link:focus-visible {
  color: #0f172a;
  background: rgba(15, 23, 42, 0.05);
}

.northstar-app[data-bs-theme="light"] .northstar-nav-link.active {
  color: #3b4ee0;
  background: rgba(106, 111, 245, 0.08);
  border-left-color: #5b6cff;
}

/* Sidebar bottom divider */
.northstar-theme-wrap {
  margin-top: auto;
  padding-top: 1rem;
  border-top: 1px solid rgba(255, 255, 255, 0.06);
}

.northstar-app[data-bs-theme="light"] .northstar-theme-wrap {
  border-top-color: rgba(15, 23, 42, 0.07);
}

/* ── Userbar ──────────────────────────────────────────────── */
.northstar-userbar { display: flex; align-items: center; gap: 0.75rem; }

/* Square avatar — more premium than circle */
.northstar-avatar {
  width: 2.1rem;
  height: 2.1rem;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 6px;
  background: rgba(106, 111, 245, 0.15);
  border: 1px solid rgba(106, 111, 245, 0.22);
  color: #a5b4fc;
  font-size: 0.78rem;
  font-weight: 700;
  letter-spacing: 0.04em;
}

.northstar-app[data-bs-theme="light"] .northstar-avatar {
  background: rgba(106, 111, 245, 0.08);
  border-color: rgba(106, 111, 245, 0.16);
  color: #4451d6;
}

/* ── Section kicker pill ──────────────────────────────────── */
.northstar-kicker {
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
  padding: 0.32rem 0.7rem;
  border-radius: 4px;
  background: rgba(106, 111, 245, 0.12);
  color: #a5b4fc;
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  border: 1px solid rgba(106, 111, 245, 0.18);
}

.northstar-app[data-bs-theme="light"] .northstar-kicker {
  background: rgba(106, 111, 245, 0.08);
  border-color: rgba(106, 111, 245, 0.15);
  color: #3b4ee0;
}

/* ── Data cards ───────────────────────────────────────────── */
/* Unified glass card — sharp corners, no pill shape */
.northstar-data-card,
.northstar-grid-card {
  border: 1px solid rgba(255, 255, 255, 0.07) !important;
  border-radius: 8px !important;
  background: linear-gradient(180deg,
    rgba(255, 255, 255, 0.045),
    rgba(255, 255, 255, 0.025)) !important;
  backdrop-filter: blur(14px);
  box-shadow:
    inset 0 1px 0 rgba(255, 255, 255, 0.05),
    0 16px 48px rgba(2, 6, 23, 0.2);
}

.northstar-app[data-bs-theme="light"] .northstar-data-card,
.northstar-app[data-bs-theme="light"] .northstar-grid-card {
  border-color: rgba(15, 23, 42, 0.08) !important;
  background: linear-gradient(180deg,
    rgba(255, 255, 255, 0.98),
    rgba(246, 249, 255, 0.96)) !important;
  backdrop-filter: none;
  box-shadow:
    inset 0 1px 0 rgba(255, 255, 255, 0.9),
    0 2px 8px rgba(15, 23, 42, 0.05),
    0 12px 40px rgba(15, 23, 42, 0.06);
}

.northstar-data-card .card-body,
.northstar-grid-card .card-body {
  padding: 1.25rem 1.35rem;
}

/* Grid metric cards — thin top accent line only */
.northstar-grid-card {
  overflow: hidden;
  position: relative;
}

.northstar-grid-card::before {
  content: "";
  position: absolute;
  inset: 0 0 auto 0;
  height: 2px;
  background: linear-gradient(90deg, rgba(106, 111, 245, 0.9), rgba(77, 171, 247, 0.15));
}

/* Typography inside cards — explicit colour to override Bootstrap */
.northstar-data-card h1, .northstar-data-card h2,
.northstar-data-card h3, .northstar-data-card h4,
.northstar-grid-card h1,  .northstar-grid-card h2,
.northstar-grid-card h3,  .northstar-grid-card h4,
.northstar-data-card strong, .northstar-grid-card strong {
  color: #f0f4ff;
}

.northstar-app[data-bs-theme="light"] .northstar-data-card h1,
.northstar-app[data-bs-theme="light"] .northstar-data-card h2,
.northstar-app[data-bs-theme="light"] .northstar-data-card h3,
.northstar-app[data-bs-theme="light"] .northstar-data-card h4,
.northstar-app[data-bs-theme="light"] .northstar-grid-card h1,
.northstar-app[data-bs-theme="light"] .northstar-grid-card h2,
.northstar-app[data-bs-theme="light"] .northstar-grid-card h3,
.northstar-app[data-bs-theme="light"] .northstar-grid-card h4,
.northstar-app[data-bs-theme="light"] .northstar-data-card strong,
.northstar-app[data-bs-theme="light"] .northstar-grid-card strong {
  color: #0f172a;
}

.northstar-data-card .text-muted,
.northstar-grid-card .text-muted {
  color: rgba(148, 163, 184, 0.78) !important;
}

.northstar-app[data-bs-theme="light"] .northstar-data-card .text-muted,
.northstar-app[data-bs-theme="light"] .northstar-grid-card .text-muted {
  color: #64748b !important;
}

/* ── Filter bar ───────────────────────────────────────────── */
.northstar-filter-bar { row-gap: 1rem; }

/* 4-column responsive grid layout */
.northstar-filter-bar .d-flex.flex-wrap.gap-3.align-items-end {
  display: grid !important;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 1rem !important;
  width: 100%;
}

.northstar-filter-bar .ms-auto.d-flex.gap-2 {
  margin-left: 0 !important;
  justify-content: flex-start;
}

/* Form labels — small-caps style */
.northstar-filter-bar .form-label,
.northstar-data-card .form-label {
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: rgba(148, 163, 184, 0.78);
}

.northstar-app[data-bs-theme="light"] .northstar-filter-bar .form-label,
.northstar-app[data-bs-theme="light"] .northstar-data-card .form-label {
  color: #64748b;
}

/* Inputs — sharp geometry */
.northstar-filter-bar .form-select,
.northstar-filter-bar .form-control,
.northstar-filter-bar .form-range,
.northstar-data-card .form-select,
.northstar-data-card .form-control {
  border-radius: 5px;
  border: 1px solid rgba(255, 255, 255, 0.08);
  background: rgba(255, 255, 255, 0.04);
  color: #f0f4ff;
  font-size: 0.875rem;
}

.northstar-app[data-bs-theme="light"] .northstar-filter-bar .form-select,
.northstar-app[data-bs-theme="light"] .northstar-filter-bar .form-control,
.northstar-app[data-bs-theme="light"] .northstar-data-card .form-select,
.northstar-app[data-bs-theme="light"] .northstar-data-card .form-control {
  border-color: rgba(15, 23, 42, 0.09);
  background: rgba(255, 255, 255, 0.96);
  color: #0f172a;
}

.northstar-filter-bar .form-select:focus,
.northstar-filter-bar .form-control:focus,
.northstar-data-card .form-select:focus,
.northstar-data-card .form-control:focus {
  border-color: rgba(106, 111, 245, 0.4);
  box-shadow: 0 0 0 3px rgba(106, 111, 245, 0.1);
}

/* Buttons in filter/data areas */
.northstar-filter-bar .btn,
.northstar-data-card .btn {
  min-height: 2.6rem;
  border-radius: 5px;
  font-weight: 600;
  font-size: 0.85rem;
  letter-spacing: 0.01em;
}

/* Theme toggle area */
.northstar-data-card .form-check.form-switch {
  padding: 0.75rem 0.95rem;
  border: 1px solid rgba(255, 255, 255, 0.07);
  border-radius: 6px;
  background: rgba(255, 255, 255, 0.025);
}

.northstar-app[data-bs-theme="light"] .northstar-data-card .form-check.form-switch {
  border-color: rgba(15, 23, 42, 0.08);
  background: rgba(255, 255, 255, 0.86);
}

/* ── Dashboard grid ───────────────────────────────────────── */
.northstar-grid-span-2 { grid-column: span 2; }

/* ── Table ────────────────────────────────────────────────── */
.northstar-table-shell .form-control {
  border-radius: 5px;
  min-height: 2.6rem;
  font-size: 0.875rem;
}

.northstar-table-shell .table {
  --bs-table-bg: transparent;
  --bs-table-color: #cbd5e1;
  --bs-table-border-color: rgba(255, 255, 255, 0.06);
  --bs-table-striped-bg: rgba(255, 255, 255, 0.018);
  --bs-table-hover-bg: rgba(106, 111, 245, 0.07);
  margin-bottom: 0;
}

.northstar-app[data-bs-theme="light"] .northstar-table-shell .table {
  --bs-table-color: #1e293b;
  --bs-table-border-color: rgba(15, 23, 42, 0.07);
  --bs-table-striped-bg: rgba(15, 23, 42, 0.018);
  --bs-table-hover-bg: rgba(106, 111, 245, 0.05);
}

/* Column headers */
.northstar-table-shell th {
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: rgba(165, 180, 252, 0.85);
  background: rgba(255, 255, 255, 0.025);
  padding-top: 0.85rem;
  padding-bottom: 0.85rem;
}

.northstar-app[data-bs-theme="light"] .northstar-table-shell th {
  color: #3b4ee0;
  background: rgba(106, 111, 245, 0.05);
}

.northstar-table-shell td { vertical-align: middle; }

/* Pagination */
.northstar-table-shell .pagination {
  margin-top: 1rem;
  margin-bottom: 0;
}

.northstar-table-shell .page-link {
  border-radius: 5px !important;
  border: 1px solid rgba(255, 255, 255, 0.07);
  background: rgba(255, 255, 255, 0.03);
  color: #cbd5e1;
  font-size: 0.84rem;
  transition: background 0.15s ease, border-color 0.15s ease, color 0.15s ease;
}

.northstar-table-shell .page-link:hover {
  background: rgba(255, 255, 255, 0.07);
  border-color: rgba(106, 111, 245, 0.22);
  color: #fff;
}

.northstar-app[data-bs-theme="light"] .northstar-table-shell .page-link {
  border-color: rgba(15, 23, 42, 0.09);
  background: rgba(255, 255, 255, 0.9);
  color: #334155;
}

.northstar-table-shell .page-item.active .page-link {
  background: #5b6cff;
  border-color: transparent;
  color: #fff;
  box-shadow: 0 4px 12px rgba(91, 108, 255, 0.28);
}

/* Table action button */
.northstar-table-shell .btn {
  border-radius: 5px;
  font-size: 0.84rem;
  font-weight: 600;
}

/* Fix badge color for light mode */
.northstar-app[data-bs-theme="light"] .badge.text-bg-primary { color: #fff !important; }

/* ── Responsive ────────────────────────────────────────────── */
@media (max-width: 1199.98px) {
  .northstar-filter-bar .d-flex.flex-wrap.gap-3.align-items-end {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  .northstar-grid-span-2 { grid-column: span 1; }
}

@media (max-width: 767.98px) {
  .northstar-shell .main-content-wrapper .container-fluid {
    padding-inline: 0.875rem;
  }

  .northstar-filter-bar .d-flex.flex-wrap.gap-3.align-items-end {
    grid-template-columns: 1fr;
  }

  .northstar-userbar { gap: 0.5rem; }
}
"""
ACCOUNTS: list[dict[str, Any]] = [
    {
        "account": "Nova Freight",
        "team": "enterprise",
        "region": "North America",
        "health": "Healthy",
        "mrr": 42000,
        "expansion": 9000,
        "risk": 18,
        "owner": "Amina Yusuf",
        "renewal": "2026-05-11",
        "sla": 98,
        "nps": 58,
    },
    {
        "account": "Cinder Retail",
        "team": "growth",
        "region": "Europe",
        "health": "Watch",
        "mrr": 16000,
        "expansion": 4200,
        "risk": 44,
        "owner": "Luca Moretti",
        "renewal": "2026-06-02",
        "sla": 94,
        "nps": 41,
    },
    {
        "account": "Helix Health",
        "team": "enterprise",
        "region": "North America",
        "health": "Healthy",
        "mrr": 36000,
        "expansion": 7800,
        "risk": 24,
        "owner": "Bayo Martins",
        "renewal": "2026-07-18",
        "sla": 97,
        "nps": 63,
    },
    {
        "account": "Atlas Cloud",
        "team": "platform",
        "region": "Europe",
        "health": "Healthy",
        "mrr": 22000,
        "expansion": 5800,
        "risk": 21,
        "owner": "Nina Cole",
        "renewal": "2026-08-09",
        "sla": 99,
        "nps": 55,
    },
    {
        "account": "Verdant Labs",
        "team": "growth",
        "region": "Africa",
        "health": "At Risk",
        "mrr": 12000,
        "expansion": 1800,
        "risk": 72,
        "owner": "Idris Bello",
        "renewal": "2026-04-28",
        "sla": 88,
        "nps": 29,
    },
    {
        "account": "Northpath Energy",
        "team": "enterprise",
        "region": "Middle East",
        "health": "Healthy",
        "mrr": 28500,
        "expansion": 6400,
        "risk": 30,
        "owner": "Sara Khan",
        "renewal": "2026-09-04",
        "sla": 96,
        "nps": 51,
    },
    {
        "account": "Ridge Finance",
        "team": "platform",
        "region": "North America",
        "health": "Watch",
        "mrr": 18000,
        "expansion": 3300,
        "risk": 47,
        "owner": "Elijah Grant",
        "renewal": "2026-10-15",
        "sla": 92,
        "nps": 38,
    },
    {
        "account": "Orchid Mobility",
        "team": "growth",
        "region": "Asia Pacific",
        "health": "Healthy",
        "mrr": 14500,
        "expansion": 2950,
        "risk": 33,
        "owner": "Mei Tan",
        "renewal": "2026-05-27",
        "sla": 95,
        "nps": 47,
    },
    {
        "account": "Summit Grid",
        "team": "platform",
        "region": "Europe",
        "health": "At Risk",
        "mrr": 11000,
        "expansion": 900,
        "risk": 78,
        "owner": "Jonas Beck",
        "renewal": "2026-06-21",
        "sla": 86,
        "nps": 22,
    },
    {
        "account": "Lattice Works",
        "team": "support",
        "region": "Africa",
        "health": "Watch",
        "mrr": 9000,
        "expansion": 1100,
        "risk": 53,
        "owner": "Teni Adebayo",
        "renewal": "2026-11-02",
        "sla": 90,
        "nps": 34,
    },
    {
        "account": "Pulse Care",
        "team": "support",
        "region": "Middle East",
        "health": "Healthy",
        "mrr": 13000,
        "expansion": 2100,
        "risk": 26,
        "owner": "Omar Nasser",
        "renewal": "2026-07-01",
        "sla": 97,
        "nps": 49,
    },
    {
        "account": "Beacon Chain",
        "team": "enterprise",
        "region": "Asia Pacific",
        "health": "Watch",
        "mrr": 25500,
        "expansion": 5100,
        "risk": 39,
        "owner": "Ada Ekwueme",
        "renewal": "2026-08-20",
        "sla": 93,
        "nps": 46,
    },
]

ALERTS = [
    ("Renewal risk review due for Verdant Labs", "#"),
    ("EMEA adoption report is ready", "#"),
    ("North America pipeline cleared 112%", "#"),
    ("Three accounts need executive follow-up", "#"),
]

app = FastHTML()
add_bootstrap(
    app,
    theme=NORTHSTAR_THEME,
    mode="auto",
    font_family="Plus Jakarta Sans",
    include_favicon=False,
)


def current_theme(req: Any) -> str:
    theme = req.session.get(THEME_KEY, "dark")
    return theme if theme in {"light", "dark"} else "dark"


def sidebar_link(icon: str, label: str, href: str = "#", active: bool = False) -> A:
    return A(
        Span(Icon(icon), cls="fs-5"),
        Span(label),
        href=href,
        cls=f"northstar-nav-link{' active' if active else ''}",
    )


def parse_state(req: Any) -> dict[str, Any]:
    params = req.query_params
    return {
        "team": params.get("team", "all"),
        "region": params.get("region", "all"),
        "health": params.getlist("health") or ["Healthy", "Watch", "At Risk"],
        "risk_cap": int(params.get("risk_cap", "80")),
        "start_date": params.get("start_date", ""),
        "end_date": params.get("end_date", ""),
        "sort": params.get("sort"),
        "direction": params.get("direction", "asc"),
        "search": params.get("q", ""),
        "page": int(params.get("page", "1")),
        "per_page": int(params.get("per_page", "8")),
    }


def visible_accounts(state: dict[str, Any]) -> list[dict[str, Any]]:
    selected_health = set(state["health"])
    start = date.fromisoformat(state["start_date"]) if state["start_date"] else None
    end = date.fromisoformat(state["end_date"]) if state["end_date"] else None
    filtered: list[dict[str, Any]] = []

    for row in ACCOUNTS:
        renewal = date.fromisoformat(row["renewal"])
        if state["team"] != "all" and row["team"] != state["team"]:
            continue
        if state["region"] != "all" and row["region"] != state["region"]:
            continue
        if row["health"] not in selected_health:
            continue
        if row["risk"] > state["risk_cap"]:
            continue
        if start and renewal < start:
            continue
        if end and renewal > end:
            continue
        filtered.append(row)

    return filtered


def export_params(state: dict[str, Any]) -> dict[str, Any]:
    params: dict[str, Any] = {
        "team": state["team"],
        "region": state["region"],
        "health": state["health"],
        "risk_cap": state["risk_cap"],
    }
    if state["start_date"]:
        params["start_date"] = state["start_date"]
    if state["end_date"]:
        params["end_date"] = state["end_date"]
    return params


def currency(value: float | int) -> str:
    return f"${value:,.0f}"


def pct(value: float | int) -> str:
    return f"{value:.0f}%"


def sparkline(values: list[float], *, stroke: str = "#6A6FF5") -> str:
    if not values:
        values = [0, 0]
    width = 180
    height = 58
    min_v = min(values)
    max_v = max(values)
    spread = max(max_v - min_v, 1)
    step = width / max(len(values) - 1, 1)
    points: list[str] = []

    for idx, value in enumerate(values):
        x = idx * step
        y = height - ((value - min_v) / spread) * (height - 10) - 5
        points.append(f"{x:.1f},{y:.1f}")

    return f"""
    <svg viewBox="0 0 {width} {height}" width="{width}" height="{height}" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M0 {height-4} L{width} {height-4}" stroke="rgba(148,163,184,0.22)" stroke-width="1"/>
      <polyline points="{' '.join(points)}" stroke="{stroke}" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
      <circle cx="{points[-1].split(',')[0]}" cy="{points[-1].split(',')[1]}" r="4" fill="{stroke}"/>
    </svg>
    """


def trend_svg(values: list[float], *, stroke: str, fill: str) -> str:
    if not values:
        values = [0, 0]
    width = 560
    height = 220
    padding = 20
    min_v = min(values)
    max_v = max(values)
    spread = max(max_v - min_v, 1)
    step = (width - padding * 2) / max(len(values) - 1, 1)
    labels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    points: list[str] = []

    for idx, value in enumerate(values):
        x = padding + idx * step
        y = height - padding - ((value - min_v) / spread) * (height - padding * 2)
        points.append(f"{x:.1f},{y:.1f}")

    area_points = " ".join(
        points + [f"{width-padding},{height-padding}", f"{padding},{height-padding}"]
    )
    label_nodes = "".join(
        f'<text x="{padding + idx * step:.1f}" y="{height-4}" fill="rgba(148,163,184,0.82)" font-size="12" text-anchor="middle">{labels[idx]}</text>'
        for idx in range(len(labels))
    )

    return f"""
    <svg viewBox="0 0 {width} {height}" width="100%" height="{height}" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient id="northstarArea" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stop-color="{fill}" stop-opacity="0.34"/>
          <stop offset="100%" stop-color="{fill}" stop-opacity="0.03"/>
        </linearGradient>
      </defs>
      <polygon points="{area_points}" fill="url(#northstarArea)"/>
      <polyline points="{' '.join(points)}" fill="none" stroke="{stroke}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
      {label_nodes}
    </svg>
    """


def bars_svg(values: list[int], *, colors: list[str]) -> str:
    width = 560
    height = 220
    max_v = max(values) if values else 1
    bar_w = 72
    gap = 24
    start = 36
    labels = ["Enterprise", "Growth", "Platform", "Support"]
    parts = [f'<rect x="0" y="0" width="{width}" height="{height}" rx="18" fill="transparent"/>']

    for idx, value in enumerate(values):
        bar_height = (value / max_v) * 135 if max_v else 0
        x = start + idx * (bar_w + gap)
        y = 160 - bar_height
        parts.append(
            f'<rect x="{x}" y="{y}" width="{bar_w}" height="{bar_height}" rx="18" fill="{colors[idx % len(colors)]}" opacity="0.92"/>'
        )
        parts.append(
            f'<text x="{x + bar_w/2}" y="184" fill="rgba(148,163,184,0.86)" font-size="12" text-anchor="middle">{labels[idx]}</text>'
        )
        parts.append(
            f'<text x="{x + bar_w/2}" y="{y - 10}" fill="rgba(226,232,240,0.92)" font-size="12" text-anchor="middle">{value}</text>'
        )

    return f'<svg viewBox="0 0 {width} {height}" width="100%" height="{height}" xmlns="http://www.w3.org/2000/svg">{"".join(parts)}</svg>'


def summary_values(rows: list[dict[str, Any]]) -> dict[str, Any]:
    if not rows:
        return {
            "mrr": 0,
            "accounts": 0,
            "avg_nps": 0,
            "at_risk": 0,
            "retention": 0,
            "win_rate": 0,
            "avg_sla": 0,
            "forecast": 0,
        }

    total_mrr = sum(row["mrr"] for row in rows)
    total_expansion = sum(row["expansion"] for row in rows)
    avg_nps = sum(row["nps"] for row in rows) / len(rows)
    avg_sla = sum(row["sla"] for row in rows) / len(rows)
    at_risk = len([row for row in rows if row["health"] == "At Risk"])
    watch = len([row for row in rows if row["health"] == "Watch"])

    return {
        "mrr": total_mrr,
        "accounts": len(rows),
        "avg_nps": avg_nps,
        "at_risk": at_risk,
        "retention": min(128, 102 + round(total_expansion / max(total_mrr, 1) * 100)),
        "win_rate": max(42, 61 - watch),
        "avg_sla": avg_sla,
        "forecast": total_mrr + total_expansion,
    }


def revenue_series(rows: list[dict[str, Any]]) -> list[float]:
    base = summary_values(rows)["mrr"]
    factors = [0.78, 0.82, 0.88, 0.93, 0.97, 1.0]
    return [round(base * factor) for factor in factors]


def team_pipeline(rows: list[dict[str, Any]]) -> list[int]:
    counts = Counter(row["team"] for row in rows)
    weights = {"enterprise": 9, "growth": 6, "platform": 5, "support": 4}
    ordered = ["enterprise", "growth", "platform", "support"]
    return [counts.get(team, 0) * weights[team] + 12 for team in ordered]


def hidden_state_inputs(state: dict[str, Any], *, exclude: set[str] | None = None) -> list[Any]:
    exclude = exclude or set()
    inputs: list[Any] = []
    mapping = {
        "team": state["team"],
        "region": state["region"],
        "risk_cap": state["risk_cap"],
        "start_date": state["start_date"],
        "end_date": state["end_date"],
    }

    for key, value in mapping.items():
        if key in exclude or value in ("", None):
            continue
        inputs.append(Input(name=key, input_type="hidden", value=str(value)))

    if "health" not in exclude:
        for value in state["health"]:
            inputs.append(Input(name="health", input_type="hidden", value=value))

    return inputs


def table_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [
        {
            "Account": row["account"],
            "Team": row["team"].title(),
            "Region": row["region"],
            "Health": row["health"],
            "MRR": currency(row["mrr"]),
            "Risk": pct(row["risk"]),
            "Renewal": row["renewal"],
        }
        for row in rows
    ]


def table_component(state: dict[str, Any], rows: list[dict[str, Any]]) -> Any:
    return Div(
        DataTable(
            table_rows(rows),
            sortable=["Account", "Team", "Region", "MRR", "Renewal"],
            sort=state["sort"],
            direction=state["direction"] if state["direction"] in {"asc", "desc"} else "asc",
            searchable=True,
            search=state["search"],
            search_placeholder="Search accounts, regions, and revenue...",
            search_param="q",
            pagination=True,
            page=state["page"],
            per_page=state["per_page"],
            base_url="/",
            filters=export_params(state),
            table_cls="align-middle",
            bordered=False,
            empty_text="No accounts match the current operating window.",
        ),
        cls="northstar-table-shell",
    )


def dashboard_content(state: dict[str, Any]) -> Any:
    rows = visible_accounts(state)
    summary = summary_values(rows)
    trend_values = revenue_series(rows)
    pipeline_values = team_pipeline(rows)

    return Div(
        DashboardGrid(
            MetricCard(
                "Monthly recurring revenue",
                currency(summary["mrr"]),
                delta="+8.6%",
                delta_type="up",
                icon=Icon("currency-dollar", cls="fs-4 text-primary"),
                icon_bg="bg-primary-subtle",
                cls="northstar-grid-card",
            ),
            MetricCard(
                "Managed accounts",
                summary["accounts"],
                delta="+4 this month",
                delta_type="up",
                icon=Icon("people", cls="fs-4 text-info"),
                icon_bg="bg-info-subtle",
                cls="northstar-grid-card",
            ),
            TrendCard(
                "Expansion signal",
                currency(summary["forecast"] - summary["mrr"]),
                delta="+6.1%",
                delta_type="up",
                sparkline=sparkline([value / 1000 for value in trend_values], stroke="#6A6FF5"),
                sparkline_safe=True,
                cls="northstar-grid-card",
            ),
            MetricCard(
                "Accounts at risk",
                summary["at_risk"],
                delta=f"{state['risk_cap']}% cap",
                delta_type="down" if summary["at_risk"] else "neutral",
                icon=Icon("exclamation-triangle", cls="fs-4 text-danger"),
                icon_bg="bg-danger-subtle",
                cls="northstar-grid-card",
            ),
            Div(
                Card(
                    Div(
                        H3("Revenue momentum", cls="h5 mb-1"),
                        P(
                            "Six-month run rate trend across the current operating window.",
                            cls="text-muted mb-4",
                        ),
                        Chart(
                            trend_svg(trend_values, stroke="#6A6FF5", fill="#6A6FF5"),
                            backend="svg",
                            allow_unsafe_html=True,
                        ),
                    ),
                    cls="northstar-grid-card border-0",
                ),
                cls="northstar-grid-span-2",
            ),
            Div(
                Card(
                    Div(
                        H3("Team pipeline", cls="h5 mb-1"),
                        P("Weighted opportunity load by delivery lane.", cls="text-muted mb-4"),
                        Chart(
                            bars_svg(
                                pipeline_values, colors=["#6A6FF5", "#4DABF7", "#12B886", "#F59F00"]
                            ),
                            backend="svg",
                            allow_unsafe_html=True,
                        ),
                    ),
                    cls="northstar-grid-card border-0",
                ),
                cls="northstar-grid-span-2",
            ),
            KPICard(
                "Operating benchmarks",
                metrics=[
                    ("Net retention", pct(summary["retention"]), "+4 pts", "up"),
                    ("Win rate", pct(summary["win_rate"]), "+2 pts", "up"),
                    ("Average SLA", pct(summary["avg_sla"]), "Stable", "neutral"),
                    ("Forecasted MRR", currency(summary["forecast"]), "+5.9%", "up"),
                ],
                columns=2,
                cls="northstar-grid-card",
            ),
            TrendCard(
                "Support load",
                f"{sum(pipeline_values)} items",
                delta="-3.2%",
                delta_type="up",
                sparkline=sparkline([value / 1000 for value in pipeline_values], stroke="#12B886"),
                sparkline_safe=True,
                cls="northstar-grid-card",
            ),
            gap=1.25,
            min_card_width=260,
        ),
        Card(
            Div(
                Div(
                    Div(
                        H3("Account watchlist", cls="h4 mb-1"),
                        P(
                            "Server-rendered table state with search, sort, pagination, and export.",
                            cls="text-muted mb-0",
                        ),
                    ),
                    ExportButton(
                        "Export CSV",
                        endpoint="/export/accounts",
                        export_format="csv",
                        filename="northstar-accounts.csv",
                        extra_params=DataTable.export_params(
                            sort=state["sort"],
                            direction=state["direction"],
                            search=state["search"],
                            filters=export_params(state),
                            include_pagination=True,
                            page=state["page"],
                            per_page=state["per_page"],
                        ),
                        variant="secondary",
                        outline=True,
                    ),
                    cls="d-flex flex-column flex-lg-row justify-content-between gap-3 mb-4",
                ),
                table_component(state, rows),
            ),
            cls="northstar-data-card border-0 mt-4",
        ),
    )


@app.get("/")
def home(req) -> Any:
    state = parse_state(req)
    theme = current_theme(req)
    rows = visible_accounts(state)
    summary = summary_values(rows)

    date_endpoint = "/?" + urlencode(
        [
            ("team", state["team"]),
            ("region", state["region"]),
            *[("health", value) for value in state["health"]],
            ("risk_cap", state["risk_cap"]),
        ],
        doseq=True,
    )

    sidebar_items = [
        sidebar_link("grid-1x2-fill", "Overview", "#", active=True),
        sidebar_link("bar-chart-fill", "Revenue", "#"),
        sidebar_link("people-fill", "Accounts", "#"),
        sidebar_link("shield-check", "Operations", "#"),
        sidebar_link("gear-fill", "Settings", "#"),
    ]

    user_bar = Div(
        NotificationCenter(
            *ALERTS,
            count=len(ALERTS),
            title="Northstar alerts",
            menu_cls="shadow border-0 rounded-4",
            button_cls="text-decoration-none text-reset",
        ),
        Div(
            Span("MY", cls="northstar-avatar"),
            Div(
                Strong("Maya Yusuf", cls="d-block"),
                Small("Revenue Operations", cls="text-body-secondary"),
            ),
            cls="d-flex align-items-center gap-2",
        ),
        cls="northstar-userbar",
    )

    filter_bar = FilterBar(
        Select(
            "team",
            ("all", "All teams", state["team"] == "all"),
            ("enterprise", "Enterprise", state["team"] == "enterprise"),
            ("growth", "Growth", state["team"] == "growth"),
            ("platform", "Platform", state["team"] == "platform"),
            ("support", "Support", state["team"] == "support"),
            label="Team",
        ),
        Select(
            "region",
            ("all", "All regions", state["region"] == "all"),
            ("North America", "North America", state["region"] == "North America"),
            ("Europe", "Europe", state["region"] == "Europe"),
            ("Africa", "Africa", state["region"] == "Africa"),
            ("Middle East", "Middle East", state["region"] == "Middle East"),
            ("Asia Pacific", "Asia Pacific", state["region"] == "Asia Pacific"),
            label="Region",
        ),
        MultiSelect(
            "health",
            ("Healthy", "Healthy"),
            ("Watch", "Watch"),
            ("At Risk", "At Risk"),
            label="Health",
            selected=state["health"],
        ),
        RangeSlider(
            "risk_cap",
            label="Risk cap",
            min_value=10,
            max_value=90,
            step=5,
            value=state["risk_cap"],
            value_suffix="%",
        ),
        *hidden_state_inputs(state, exclude={"team", "region", "health", "risk_cap"}),
        method="get",
        mode="apply",
        action="/",
        apply_label="Apply view",
        reset_label="Reset",
        reset_href="/",
        form_cls="northstar-filter-bar",
    )

    side_panel = Card(
        Div(
            H4("Window and theme", cls="h5 mb-1"),
            P(
                "Adjust the renewal window or switch visual mode without leaving the page shell.",
                cls="text-muted mb-4",
            ),
            DateRangePicker(
                start_value=state["start_date"] or None,
                end_value=state["end_date"] or None,
                presets=[
                    ("Next 30 days", "2026-04-01", "2026-04-30"),
                    ("Q2", "2026-04-01", "2026-06-30"),
                    ("H2", "2026-07-01", "2026-12-31"),
                ],
                action=date_endpoint,
                method="get",
                apply_label="Update window",
                form_cls="mb-4",
            ),
            Div(
                Div(
                    Small("Current scope", cls="text-uppercase text-muted fw-semibold"),
                    H3(currency(summary["mrr"]), cls="h3 mt-2 mb-1"),
                    P(
                        f"{summary['accounts']} active accounts in this view.",
                        cls="text-muted mb-0",
                    ),
                    cls="border rounded-4 p-3 mb-3 northstar-data-card",
                ),
                Div(
                    Small("Theme preference", cls="text-uppercase text-muted fw-semibold"),
                    Div(
                        ThemeToggle(
                            current_theme=theme,
                            endpoint="/theme/toggle",
                            show_label=True,
                            label_text="Dark mode",
                            toggle_id="northstar-theme-toggle",
                        ),
                        cls="mt-2",
                    ),
                    cls="border rounded-4 p-3 northstar-data-card",
                ),
            ),
        ),
        cls="northstar-data-card border-0",
    )

    page_content = Div(
        Div(
            Span(
                Icon("stars"),
                "Northstar operations suite",
                cls="northstar-kicker mb-3",
            ),
            H1(
                "A premium dashboard surface built with Faststrap components.",
                cls="display-5 fw-bold mb-3",
            ),
            P(
                "This showcase is meant to prove the heavier product side of Faststrap: dense analytics, filters, exports, and operational storytelling without abandoning Bootstrap's foundations.",
                cls="fs-5 text-muted mb-0",
            ),
            cls=f"rounded-4 p-4 p-lg-5 mb-4 border northstar-data-card {Fx.base} {Fx.fade_in}",
        ),
        Row(
            Col(
                SearchBar(
                    placeholder="Search accounts, metrics, or commands...",
                    endpoint="/api/search",
                    target="#search-results",
                    cls="mb-4",
                ),
                cols=12,
            ),
        ),
        Div(id="search-results", cls="mb-4"),
        Row(
            Col(
                Card(
                    Div(
                        H3("Filters", cls="h5 mb-1"),
                        P(
                            "Constrain the operating lens before reviewing metrics and account health.",
                            cls="text-muted mb-4",
                        ),
                        filter_bar,
                    ),
                    cls="northstar-data-card border-0",
                ),
                lg=8,
                cls="mb-4",
            ),
            Col(side_panel, lg=4, cls="mb-4"),
        ),
        dashboard_content(state),
    )

    return Div(
        Style(CSS),
        Div(
            DashboardLayout(
                page_content,
                title=Div(
                    Span(Icon("activity"), cls="northstar-brand-mark"),
                    Span("Northstar", cls="fw-bold fs-4"),
                    cls="northstar-brand",
                ),
                sidebar_items=[Div(*sidebar_items, cls="northstar-nav")],
                user=user_bar,
                footer="Northstar is a flagship Faststrap dashboard showcase.",
                theme=theme,
            ),
            cls="northstar-shell",
        ),
        cls="northstar-app",
        data_bs_theme=theme,
    )


@app.get("/api/search")
def search(q: str = ""):
    suggestions = [
        "Accounts overview",
        "Revenue metrics",
        "Risk analysis",
        "Team performance",
        "Export CSV",
        "Date range filter",
    ]
    if not q:
        return P("Type to search...", cls="text-muted mb-0")
    filtered = [s for s in suggestions if q.lower() in s.lower()]
    if not filtered:
        return P(f"No results for '{q}'", cls="text-muted mb-0")
    return Ul(
        *[Li(A(s, href="#", cls="text-decoration-none")) for s in filtered],
        cls="list-unstyled mb-0",
    )


@app.post("/theme/toggle")
def toggle_theme(req) -> Any:
    req.session[THEME_KEY] = "light" if current_theme(req) == "dark" else "dark"
    return hx_refresh()


@app.get("/export/accounts")
def export_accounts(req) -> Response:
    state = parse_state(req)
    rows = visible_accounts(state)
    output = StringIO()
    output.write("Account,Team,Region,Health,MRR,Risk,Renewal\n")
    for row in rows:
        output.write(
            f"{row['account']},{row['team']},{row['region']},{row['health']},{row['mrr']},{row['risk']},{row['renewal']}\n"
        )

    return Response(
        output.getvalue(),
        media_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="northstar-accounts.csv"'},
    )


if __name__ == "__main__":
    serve(port=5011)
