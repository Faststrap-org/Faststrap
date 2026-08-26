"""Flagship showcase — LedgerLeaf Finance.

Production-grade personal finance / fintech dashboard for Faststrap:

- BottomNav + BottomNavItem for slick mobile-first navigation
- Sheet (bottom drawer) for transaction entry with full form coverage
- Progress + ProgressBar for animated budget tracking
- Tabs (pill variant) for Activity / Budgets / Analytics switching
- KPICard for at-a-glance financial metrics
- FilterBar for budget category filtering
- SearchableSelect for payee / recipient search
- Dropdown + DropdownItem for card action menus
- Switch for notification/biometric preference toggles
- ThemeToggle with cookie persistence on every page
- ButtonToolbar for quick-action groups
- Custom CSS: cinematic entrance animations, spring micro-interactions,
  warm sage/slate financial aesthetic — light-first, dark-aware.
"""

from __future__ import annotations

import json
from typing import Any

from fasthtml.common import (
    H4,
    H5,
    H6,
    A,
    Button,
    Canvas,
    Div,
    FastHTML,
    Form,
    Input,
    Nav,
    Option,
    P,
    Script,
    Select,
    Small,
    Span,
    Strong,
    Style,
    serve,
)

from faststrap import (
    Badge,
    BottomNav,
    BottomNavItem,
    ButtonToolbar,
    Col,
    Dropdown,
    DropdownItem,
    FilterBar,
    Icon,
    InputGroup,
    InputGroupText,
    KPICard,
    Progress,
    Row,
    SearchableSelect,
    Sheet,
    Switch,
    Tabs,
    ThemeToggle,
    add_bootstrap,
    create_theme,
)
from faststrap.presets import hx_refresh

# ── Theme ──────────────────────────────────────────────────────────────────────
THEME_KEY = "ledgerleaf_theme"

LEDGERLEAF_THEME = create_theme(
    primary="#4B6A50",  # sage green
    secondary="#3F4349",  # charcoal
    success="#228257",
    danger="#D9534F",
    warning="#F6A33B",
    info="#418A94",
    light="#F4F6F4",
    dark="#181B19",
)

# ── Sample Data ──────────────────────────────────────────────────────────────
TRANSACTIONS = [
    {
        "id": "t1",
        "icon": "cart",
        "title": "Whole Foods Market",
        "category": "Groceries",
        "date": "Today, 10:24 AM",
        "amount": -124.50,
        "type": "negative",
    },
    {
        "id": "t2",
        "icon": "cup-hot",
        "title": "Blue Bottle Coffee",
        "category": "Dining",
        "date": "Today, 8:15 AM",
        "amount": -6.20,
        "type": "negative",
    },
    {
        "id": "t3",
        "icon": "lightning",
        "title": "Pacific Gas & Electric",
        "category": "Utilities",
        "date": "Yesterday",
        "amount": -84.00,
        "type": "negative",
    },
    {
        "id": "t4",
        "icon": "briefcase",
        "title": "Stripe Payout",
        "category": "Income",
        "date": "Oct 12",
        "amount": 2450.00,
        "type": "positive",
    },
    {
        "id": "t5",
        "icon": "car-front",
        "title": "Uber",
        "category": "Transport",
        "date": "Oct 11",
        "amount": -24.80,
        "type": "negative",
    },
    {
        "id": "t6",
        "icon": "display",
        "title": "Netflix",
        "category": "Subscriptions",
        "date": "Oct 10",
        "amount": -15.99,
        "type": "negative",
    },
    {
        "id": "t7",
        "icon": "house",
        "title": "Rent — Oct 2026",
        "category": "Housing",
        "date": "Oct 1",
        "amount": -1850.00,
        "type": "negative",
    },
    {
        "id": "t8",
        "icon": "bag",
        "title": "Amazon Order",
        "category": "Shopping",
        "date": "Sep 30",
        "amount": -63.40,
        "type": "negative",
    },
]

BUDGETS = [
    {"name": "Groceries", "icon": "cart", "spent": 420, "total": 600, "color": "primary"},
    {"name": "Dining Out", "icon": "cup-hot", "spent": 280, "total": 300, "color": "warning"},
    {"name": "Transport", "icon": "car-front", "spent": 95, "total": 200, "color": "info"},
    {"name": "Entertainment", "icon": "controller", "spent": 45, "total": 150, "color": "success"},
    {"name": "Subscriptions", "icon": "display", "spent": 78, "total": 80, "color": "danger"},
]

KPI_STATS = [
    ("Monthly Spend", "$2,394", "-$180 vs last month", "down", "arrow-down-circle"),
    ("Savings Rate", "24.8%", "+2.1% vs last month", "up", "piggy-bank"),
    ("Cashback Earned", "$48.20", "This month", "up", "gift"),
    ("Credit Score", "742", "+12 pts", "up", "shield-check"),
]

CARDS_DATA = [
    {
        "name": "Sapphire Reserve",
        "network": "VISA",
        "last4": "4821",
        "balance": 2340.50,
        "limit": 10000,
        "color": "#1a2744",
    },
    {
        "name": "Gold Cash Rewards",
        "network": "MC",
        "last4": "9302",
        "balance": 680.20,
        "limit": 5000,
        "color": "#7c5820",
    },
    {
        "name": "LedgerLeaf Savings",
        "network": "BANK",
        "last4": "1107",
        "balance": 14285.50,
        "limit": None,
        "color": "#2D4030",
    },
    {
        "name": "Virtual Card",
        "network": "VISA",
        "last4": "0042",
        "balance": 0.00,
        "limit": 500,
        "color": "#334155",
    },
]

RECIPIENTS = [
    ("alice_chen", "Alice Chen"),
    ("bob_martin", "Bob Martin"),
    ("charlie_davis", "Charlie Davis"),
    ("diana_kim", "Diana Kim"),
    ("evan_okafor", "Evan Okafor"),
    ("fiona_walsh", "Fiona Walsh"),
    ("george_lee", "George Lee"),
]

NOTIF_SETTINGS = [
    ("push_transactions", "Transaction Alerts", "Get notified for every card swipe"),
    ("push_budget", "Budget Warnings", "Alert when you hit 80% of a budget"),
    ("push_savings", "Savings Milestones", "Celebrate hitting savings goals"),
    ("push_offers", "Personalized Offers", "Cashback and partner deals"),
]

CHART_OPTIONS = {
    "type": "line",
    "data": {
        "labels": ["Oct 1", "Oct 5", "Oct 10", "Oct 15", "Oct 20", "Oct 25", "Oct 30"],
        "datasets": [
            {
                "label": "Spending",
                "data": [45, 120, 80, 210, 65, 180, 40],
                "borderColor": "#4B6A50",
                "backgroundColor": "rgba(75, 106, 80, 0.12)",
                "fill": True,
                "tension": 0.4,
                "pointRadius": 4,
                "pointHoverRadius": 6,
                "pointBackgroundColor": "#4B6A50",
            },
            {
                "label": "Income",
                "data": [0, 0, 0, 2450, 0, 0, 0],
                "borderColor": "#228257",
                "backgroundColor": "rgba(34, 130, 87, 0.08)",
                "fill": True,
                "tension": 0.4,
                "pointRadius": 4,
                "pointHoverRadius": 6,
                "pointBackgroundColor": "#228257",
            },
        ],
    },
    "options": {
        "responsive": True,
        "maintainAspectRatio": False,
        "plugins": {
            "legend": {"display": True, "position": "top"},
            "tooltip": {"mode": "index", "intersect": False},
        },
        "scales": {
            "x": {"grid": {"display": False}},
            "y": {"grid": {"color": "rgba(0,0,0,0.04)"}},
        },
    },
}

# ── CSS ───────────────────────────────────────────────────────────────────────
CSS = """
/* ═══════════════════════════════════════════════════════════
   LedgerLeaf · Premium Fintech CSS
   Philosophy: mobile-first, soft geometry (12-16px radii for
   cards, 50px for pill buttons), warm sage-and-slate palette.
   Atmospheric CSS only — Bootstrap + Faststrap do the layout.
   ═══════════════════════════════════════════════════════════ */

@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&display=swap');

/* ── Base shell ─────────────────────────────────────────── */
.ll-app {
  min-height: 100vh;
  background: #EFF3F1;
  color: #1a1e1b;
  font-family: "Outfit", system-ui, sans-serif;
  padding-bottom: 88px;
}

.ll-app[data-bs-theme="dark"] {
  background:
    radial-gradient(ellipse at 0% 0%, rgba(75, 106, 80, 0.15), transparent 40%),
    linear-gradient(180deg, #0a0e0b 0%, #0e1410 100%);
  color: #e5e9e6;
}

/* ── Mobile container ────────────────────────────────────── */
.ll-container {
  max-width: 640px;
  margin: 0 auto;
  padding: 1.5rem 1rem;
}

/* ── Entrance animations ─────────────────────────────────── */
@keyframes ll-slide-up {
  from { opacity: 0; transform: translateY(20px); }
  to   { opacity: 1; transform: translateY(0); }
}

@keyframes ll-fade-in {
  from { opacity: 0; }
  to   { opacity: 1; }
}

@keyframes ll-scale-in {
  from { opacity: 0; transform: scale(0.96); }
  to   { opacity: 1; transform: scale(1); }
}

@keyframes ll-shimmer {
  0%   { background-position: -400px 0; }
  100% { background-position: 400px 0; }
}

.ll-animate-up { animation: ll-slide-up 0.5s ease both; }
.ll-animate-fade { animation: ll-fade-in 0.4s ease both; }
.ll-animate-scale { animation: ll-scale-in 0.4s ease both; }

.ll-delay-1 { animation-delay: 0.08s; }
.ll-delay-2 { animation-delay: 0.16s; }
.ll-delay-3 { animation-delay: 0.24s; }
.ll-delay-4 { animation-delay: 0.32s; }
.ll-delay-5 { animation-delay: 0.40s; }

/* ── Top App Bar ────────────────────────────────────────── */
.ll-appbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.75rem;
}

.ll-avatar {
  width: 2.75rem;
  height: 2.75rem;
  border-radius: 50%;
  background: linear-gradient(135deg, #4B6A50, #2D4030);
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 1rem;
  box-shadow: 0 4px 12px rgba(75, 106, 80, 0.3);
}

.ll-greeting { line-height: 1.2; }

/* ── Balance Card ───────────────────────────────────────── */
.ll-balance-card {
  background: linear-gradient(135deg, #4B6A50 0%, #2D4030 60%, #1e2e22 100%);
  border-radius: 20px;
  padding: 2rem 1.75rem;
  color: #fff;
  box-shadow: 0 16px 40px rgba(75, 106, 80, 0.3);
  margin-bottom: 1.5rem;
  position: relative;
  overflow: hidden;
}

.ll-balance-card::before {
  content: "";
  position: absolute;
  top: -60%;
  right: -15%;
  width: 280px;
  height: 280px;
  background: radial-gradient(circle, rgba(255,255,255,0.12) 0%, transparent 70%);
  border-radius: 50%;
}

.ll-balance-card::after {
  content: "";
  position: absolute;
  bottom: -40%;
  left: -10%;
  width: 220px;
  height: 220px;
  background: radial-gradient(circle, rgba(255,255,255,0.06) 0%, transparent 70%);
  border-radius: 50%;
}

.ll-balance-label {
  font-size: 0.8rem;
  opacity: 0.72;
  font-weight: 500;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  position: relative;
  z-index: 1;
}

.ll-balance-amount {
  font-size: 3rem;
  font-weight: 800;
  line-height: 1;
  margin: 0.5rem 0;
  letter-spacing: -0.02em;
  position: relative;
  z-index: 1;
  display: flex;
  align-items: baseline;
  gap: 0.15rem;
}

.ll-balance-currency {
  font-size: 1.6rem;
  opacity: 0.75;
}

.ll-balance-trend {
  position: relative;
  z-index: 1;
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  background: rgba(255,255,255,0.12);
  border-radius: 50px;
  padding: 0.3rem 0.8rem;
  font-size: 0.82rem;
  font-weight: 600;
  margin-top: 0.75rem;
}

/* ── Action Buttons ─────────────────────────────────────── */
.ll-actions {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 0.5rem;
  margin-bottom: 1.75rem;
}

.ll-action-btn {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.45rem;
  color: #3F4349;
  text-decoration: none;
  font-size: 0.78rem;
  font-weight: 600;
  transition: transform 0.2s cubic-bezier(0.34, 1.56, 0.64, 1);
  cursor: pointer;
  background: none;
  border: none;
  padding: 0;
}

.ll-app[data-bs-theme="dark"] .ll-action-btn { color: #9AA09C; }

.ll-action-btn:hover { transform: translateY(-3px) scale(1.05); color: #4B6A50; }
.ll-app[data-bs-theme="dark"] .ll-action-btn:hover { color: #6A9070; }

.ll-action-icon {
  width: 3.75rem;
  height: 3.75rem;
  border-radius: 16px;
  background: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.4rem;
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.06);
  transition: box-shadow 0.2s ease;
}

.ll-action-btn:hover .ll-action-icon {
  box-shadow: 0 8px 24px rgba(75, 106, 80, 0.18);
}

.ll-app[data-bs-theme="dark"] .ll-action-icon {
  background: #1e2823;
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.25);
}

/* ── KPI Strip ──────────────────────────────────────────── */
.ll-kpi-strip {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 0.85rem;
  margin-bottom: 1.75rem;
}

.ll-kpi-card {
  background: #fff;
  border-radius: 14px;
  padding: 1rem 1rem 1rem 1.1rem;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.04);
  border: 1px solid rgba(0,0,0,0.04);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.ll-kpi-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
}

.ll-app[data-bs-theme="dark"] .ll-kpi-card {
  background: #1a1f1c;
  border-color: rgba(255,255,255,0.06);
  box-shadow: none;
}

.ll-kpi-icon {
  width: 2.2rem;
  height: 2.2rem;
  border-radius: 8px;
  background: rgba(75, 106, 80, 0.1);
  color: #4B6A50;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1rem;
  margin-bottom: 0.65rem;
}

.ll-app[data-bs-theme="dark"] .ll-kpi-icon {
  background: rgba(75, 106, 80, 0.2);
  color: #6A9070;
}

.ll-kpi-value {
  font-size: 1.35rem;
  font-weight: 700;
  letter-spacing: -0.02em;
  line-height: 1.1;
}

.ll-kpi-label {
  font-size: 0.72rem;
  color: #798086;
  font-weight: 500;
  margin-bottom: 0.2rem;
}

.ll-kpi-trend {
  font-size: 0.72rem;
  font-weight: 600;
  margin-top: 0.2rem;
}

/* ── Transaction List ───────────────────────────────────── */
.ll-tx-list {
  background: #fff;
  border-radius: 16px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.04);
  border: 1px solid rgba(0,0,0,0.04);
  overflow: hidden;
}

.ll-app[data-bs-theme="dark"] .ll-tx-list {
  background: #1a1f1c;
  border-color: rgba(255,255,255,0.06);
}

.ll-tx-item {
  display: flex;
  align-items: center;
  padding: 0.9rem 1rem;
  border-bottom: 1px solid rgba(0, 0, 0, 0.04);
  transition: background 0.15s ease;
  animation: ll-slide-up 0.4s ease both;
}

.ll-tx-item:hover { background: rgba(75, 106, 80, 0.03); }
.ll-tx-item:last-child { border-bottom: none; }

.ll-app[data-bs-theme="dark"] .ll-tx-item { border-bottom-color: rgba(255, 255, 255, 0.05); }
.ll-app[data-bs-theme="dark"] .ll-tx-item:hover { background: rgba(255,255,255,0.03); }

.ll-tx-icon {
  width: 2.75rem;
  height: 2.75rem;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.1rem;
  margin-right: 0.9rem;
  flex-shrink: 0;
  background: #F4F6F4;
  color: #4B6A50;
}

.ll-app[data-bs-theme="dark"] .ll-tx-icon {
  background: rgba(75, 106, 80, 0.15);
  color: #6A9070;
}

.ll-tx-details { flex-grow: 1; min-width: 0; }
.ll-tx-title {
  font-weight: 600;
  font-size: 0.9rem;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.ll-tx-subtitle { font-size: 0.75rem; color: #798086; }

.ll-tx-amount { font-weight: 700; font-size: 0.95rem; text-align: right; white-space: nowrap; }
.ll-tx-amount.negative { color: #1a1e1b; }
.ll-tx-amount.positive { color: #228257; }
.ll-app[data-bs-theme="dark"] .ll-tx-amount.negative { color: #e5e9e6; }
.ll-app[data-bs-theme="dark"] .ll-tx-amount.positive { color: #4ade80; }

/* ── Budget Cards ───────────────────────────────────────── */
.ll-budget-item {
  background: #fff;
  border-radius: 14px;
  padding: 1.1rem;
  margin-bottom: 0.75rem;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.04);
  border: 1px solid rgba(0,0,0,0.04);
  transition: transform 0.2s ease;
}

.ll-budget-item:hover { transform: translateX(3px); }

.ll-app[data-bs-theme="dark"] .ll-budget-item {
  background: #1a1f1c;
  border-color: rgba(255,255,255,0.06);
}

.ll-app .progress {
  height: 7px;
  border-radius: 4px;
  background: rgba(0, 0, 0, 0.06);
  margin-top: 0.7rem;
  overflow: hidden;
}

.ll-app[data-bs-theme="dark"] .progress { background: rgba(255, 255, 255, 0.08); }

/* ── Payment Card Display ────────────────────────────────── */
.ll-card-display {
  border-radius: 18px;
  padding: 1.5rem;
  color: #fff;
  position: relative;
  overflow: hidden;
  height: 210px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  cursor: pointer;
  transition: transform 0.25s ease, box-shadow 0.25s ease;
  box-shadow: 0 8px 32px rgba(0,0,0,0.2);
}

.ll-card-display:hover {
  transform: translateY(-4px) rotate(-0.5deg);
  box-shadow: 0 16px 48px rgba(0,0,0,0.28);
}

.ll-card-display::before {
  content: "";
  position: absolute;
  top: -50%;
  right: -20%;
  width: 200px;
  height: 200px;
  background: radial-gradient(circle, rgba(255,255,255,0.15) 0%, transparent 70%);
  border-radius: 50%;
}

.ll-card-number { font-size: 1rem; letter-spacing: 0.1em; opacity: 0.78; }
.ll-card-name { font-size: 0.8rem; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; opacity: 0.7; }
.ll-card-balance { font-size: 1.75rem; font-weight: 800; letter-spacing: -0.02em; }
.ll-card-network { font-size: 0.72rem; font-weight: 800; letter-spacing: 0.06em; opacity: 0.65; }

/* ── BottomNav ───────────────────────────────────────────── */
.ll-app .bottom-nav {
  background: rgba(255, 255, 255, 0.88);
  backdrop-filter: blur(24px) saturate(1.5);
  -webkit-backdrop-filter: blur(24px) saturate(1.5);
  border-top: 1px solid rgba(0, 0, 0, 0.06);
}

.ll-app[data-bs-theme="dark"] .bottom-nav {
  background: rgba(18, 23, 19, 0.92);
  border-top-color: rgba(255, 255, 255, 0.06);
}

.ll-app .bottom-nav .nav-link { color: #798086; font-size: 0.72rem; }
.ll-app .bottom-nav .nav-link.active { color: #4B6A50; }
.ll-app[data-bs-theme="dark"] .bottom-nav .nav-link.active { color: #6A9070; }

/* ── Sheet (bottom drawer) ──────────────────────────────── */
.ll-app .offcanvas-bottom {
  border-radius: 24px 24px 0 0;
  border-top: none !important;
  box-shadow: 0 -16px 60px rgba(0, 0, 0, 0.12);
}

.ll-app[data-bs-theme="dark"] .offcanvas-bottom { box-shadow: 0 -16px 60px rgba(0, 0, 0, 0.45); }

.ll-sheet-handle {
  width: 40px;
  height: 4px;
  background: rgba(0,0,0,0.15);
  border-radius: 2px;
  margin: 0 auto 1.25rem;
}

.ll-app[data-bs-theme="dark"] .ll-sheet-handle { background: rgba(255,255,255,0.15); }

/* ── Page Header ─────────────────────────────────────────── */
.ll-page-header {
  padding: 1.5rem 1rem 0.5rem;
  max-width: 640px;
  margin: 0 auto;
}

/* ── Profile Sections ────────────────────────────────────── */
.ll-profile-section {
  background: #fff;
  border-radius: 16px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.04);
  border: 1px solid rgba(0,0,0,0.04);
  overflow: hidden;
  margin-bottom: 1rem;
}

.ll-app[data-bs-theme="dark"] .ll-profile-section {
  background: #1a1f1c;
  border-color: rgba(255,255,255,0.06);
}

.ll-profile-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.85rem 1.1rem;
  border-bottom: 1px solid rgba(0,0,0,0.04);
}

.ll-profile-row:last-child { border-bottom: none; }

.ll-app[data-bs-theme="dark"] .ll-profile-row { border-bottom-color: rgba(255,255,255,0.05); }

/* ── Responsive (wider screens) ────────────────────────────  */
@media (min-width: 640px) {
  .ll-kpi-strip { grid-template-columns: repeat(4, 1fr); }
  .ll-actions { grid-template-columns: repeat(4, 1fr); gap: 1rem; }
}
"""

# ── App factory ───────────────────────────────────────────────────────────────
app = FastHTML()
add_bootstrap(app, theme=LEDGERLEAF_THEME, font_family="Outfit")


def theme_from_req(req) -> str:
    return req.session.get(THEME_KEY) or req.cookies.get(THEME_KEY, "light")


def ll_theme_toggle(theme: str, toggle_id: str, cls: str = "") -> Any:
    return ThemeToggle(
        current_theme=theme,
        endpoint="/theme/toggle",
        toggle_id=toggle_id,
        cls=cls,
    )


# ── Shared UI building blocks ─────────────────────────────────────────────────


def ll_bottom_nav(active: str = "home") -> Nav:
    return BottomNav(
        BottomNavItem("Home", icon="house-door-fill", active=(active == "home"), href="/"),
        BottomNavItem("Send", icon="send-fill", href="/send"),
        BottomNavItem("Cards", icon="credit-card-fill", href="/cards"),
        BottomNavItem("Profile", icon="person-circle", href="/profile"),
    )


def ll_appbar(theme: str, title: str = "", subtitle: str = "") -> Div:
    return Div(
        Div(
            Div("MR", cls="ll-avatar me-3"),
            (
                Div(
                    P("Good morning,", cls="mb-0 text-muted small"),
                    H5(title or "Michael", cls="mb-0 fw-bold"),
                )
                if not subtitle
                else Div(
                    H5(title, cls="mb-0 fw-bold"),
                    P(subtitle, cls="mb-0 text-muted small"),
                )
            ),
            cls="d-flex align-items-center",
        ),
        Div(
            ll_theme_toggle(theme, "ledgerleaf-home-theme-toggle", cls="me-2"),
            Button(
                Icon("bell"),
                cls="btn btn-link text-body p-0 position-relative",
                **{"data-bs-toggle": "offcanvas", "data-bs-target": "#notif-sheet"},
            ),
            cls="d-flex align-items-center gap-2",
        ),
        cls="ll-appbar",
    )


# ── Home page components ──────────────────────────────────────────────────────


def ll_balance_card() -> Div:
    return Div(
        Div("Total Balance", cls="ll-balance-label"),
        Div(
            Span("$", cls="ll-balance-currency"),
            Span("14,285.50"),
            cls="ll-balance-amount",
        ),
        Div(
            Icon("arrow-up-right", cls="me-1"),
            "+$2,450.00 income this month",
            cls="ll-balance-trend",
        ),
        Div(
            Div(
                Small("Income", cls="d-block opacity-75 mb-1", style="font-size:0.7rem"),
                Strong("$4,200.00"),
                cls="text-white",
            ),
            Div(
                Small("Expenses", cls="d-block opacity-75 mb-1", style="font-size:0.7rem"),
                Strong("$2,394.50"),
                cls="text-white",
            ),
            Div(
                Small("Net", cls="d-block opacity-75 mb-1", style="font-size:0.7rem"),
                Strong("+$1,805.50"),
                cls="text-white",
            ),
            cls="d-flex justify-content-between mt-4 pt-3",
            style="border-top: 1px solid rgba(255,255,255,0.14); position:relative; z-index:1;",
        ),
        cls="ll-balance-card ll-animate-scale",
    )


def ll_quick_actions() -> Div:
    actions = [
        ("send", "send-fill", "#", "new-tx-sheet", "Send"),
        ("receive", "qr-code-scan", "#", None, "Receive"),
        ("exchange", "arrow-left-right", "#", None, "Exchange"),
        ("history", "clock-history", "#", None, "History"),
    ]
    items = []
    for i, (_action_id, icon_name, href, sheet_id, label) in enumerate(actions):
        extra = {}
        if sheet_id:
            extra = {"data-bs-toggle": "offcanvas", "data-bs-target": f"#{sheet_id}"}
        items.append(
            A(
                Div(Icon(icon_name), cls="ll-action-icon"),
                Span(label, style="font-size:0.75rem"),
                href=href,
                cls=f"ll-action-btn ll-animate-up ll-delay-{i+1}",
                **extra,
            )
        )
    return Div(*items, cls="ll-actions")


def ll_kpi_strip() -> Div:
    cards = []
    for i, (label, val, trend, direction, icon_name) in enumerate(KPI_STATS):
        trend_cls = "text-success" if direction == "up" else "text-danger"
        cards.append(
            Div(
                Div(Icon(icon_name), cls="ll-kpi-icon"),
                P(label, cls="ll-kpi-label mb-0"),
                P(val, cls="ll-kpi-value mb-0"),
                P(trend, cls=f"ll-kpi-trend {trend_cls} mb-0"),
                cls=f"ll-kpi-card ll-animate-up ll-delay-{i+1}",
            )
        )
    return Div(*cards, cls="ll-kpi-strip mb-4")


def ll_transactions() -> Div:
    items = []
    for i, tx in enumerate(TRANSACTIONS):
        items.append(
            Div(
                Div(Icon(tx["icon"]), cls="ll-tx-icon"),
                Div(
                    Div(tx["title"], cls="ll-tx-title"),
                    Div(f"{tx['category']} · {tx['date']}", cls="ll-tx-subtitle"),
                    cls="ll-tx-details",
                ),
                Div(
                    f"{'+' if tx['type'] == 'positive' else ''}{tx['amount']:.2f}",
                    cls=f"ll-tx-amount {tx['type']}",
                ),
                cls="ll-tx-item",
                style=f"animation-delay:{i * 0.05}s",
            )
        )
    return Div(
        Div(
            H5("Recent Activity", cls="mb-0 fw-bold"),
            A("See All", href="#", cls="text-primary text-decoration-none small fw-600"),
            cls="d-flex justify-content-between align-items-center px-3 pt-3 pb-2",
        ),
        Div(*items, cls="ll-tx-list"),
        cls="mb-4",
    )


def ll_budgets_tab() -> Div:
    items = []
    for b in BUDGETS:
        pct = int((b["spent"] / b["total"]) * 100)
        over = pct >= 90
        items.append(
            Div(
                Div(
                    Div(
                        Div(
                            Icon(b["icon"]),
                            cls="ll-tx-icon me-2",
                            style="width:2rem;height:2rem;font-size:0.9rem;border-radius:8px",
                        ),
                        Div(b["name"], cls="fw-600"),
                    ),
                    Div(
                        Badge(
                            f"{pct}%",
                            variant="danger" if over else "light",
                            cls="" if over else "text-muted",
                        ),
                        Small(f"${b['spent']} / ${b['total']}", cls="ms-2 text-muted"),
                        cls="d-flex align-items-center",
                    ),
                    cls="d-flex justify-content-between align-items-center",
                ),
                Progress(value=pct, variant="danger" if over else b["color"]),
                cls="ll-budget-item ll-animate-up",
            )
        )
    return Div(
        Div(
            H5("Budget Tracker", cls="mb-0 fw-bold"),
            Badge("October", variant="secondary", cls="opacity-75"),
            cls="d-flex justify-content-between align-items-center mb-3",
        ),
        *items,
        cls="mb-4",
    )


def ll_analytics_tab() -> Div:
    chart_script = f"""
document.addEventListener('DOMContentLoaded', function() {{
    const ctx = document.getElementById('spending-chart');
    if (ctx && window.Chart) {{
        new Chart(ctx, {json.dumps(CHART_OPTIONS)});
    }}
}});
"""
    return Div(
        H5("Spending vs Income", cls="fw-bold mb-3"),
        Div(
            Canvas(id="spending-chart", style="width:100%;height:260px;display:block;"),
            cls="bg-white rounded-4 p-3 shadow-sm mb-4",
        ),
        Script(src="https://cdn.jsdelivr.net/npm/chart.js"),
        Script(chart_script),
        Div(
            KPICard(
                "October Summary",
                metrics=[
                    ("Total Spent", "$2,394", "-7.0%", "down"),
                    ("Largest Category", "Groceries", "$420", "neutral"),
                    ("Avg Daily Spend", "$77.23", "vs $83 last mo", "up"),
                    ("Subscriptions", "$78", "5 active", "neutral"),
                ],
                columns=2,
                cls="shadow-sm",
            ),
        ),
        cls="mb-4",
    )


def new_tx_sheet() -> Any:
    return Sheet(
        Div(
            Div(cls="ll-sheet-handle"),
            H4("New Transaction", cls="fw-bold mb-1"),
            P("Log a manual expense or income", cls="text-muted small mb-4"),
            Form(
                InputGroup(
                    InputGroupText("$"),
                    Input(
                        "amount",
                        input_type="number",
                        placeholder="0.00",
                        cls="form-control form-control-lg fw-bold",
                        step="0.01",
                    ),
                    cls="mb-3",
                ),
                Input("description", input_type="text", placeholder="Merchant or description", cls="form-control mb-3"),
                Select(
                    Option("Groceries"),
                    Option("Dining"),
                    Option("Transport"),
                    Option("Utilities"),
                    Option("Entertainment"),
                    Option("Income"),
                    Option("Housing"),
                    Option("Shopping"),
                    cls="form-select mb-3",
                ),
                Input("tx_date", input_type="date", cls="form-control mb-4"),
                Row(
                    Col(
                        Button(
                            "Add Expense",
                            cls="btn btn-danger w-100 fw-600",
                            style="border-radius:12px",
                        ),
                        md=6,
                        cls="mb-2",
                    ),
                    Col(
                        Button(
                            "Add Income",
                            cls="btn btn-success w-100 fw-600",
                            style="border-radius:12px",
                        ),
                        md=6,
                        cls="mb-2",
                    ),
                ),
                action="#",
                method="post",
            ),
        ),
        sheet_id="new-tx-sheet",
        height="auto",
    )


def notif_sheet() -> Any:
    return Sheet(
        Div(
            Div(cls="ll-sheet-handle"),
            H4("Notifications", cls="fw-bold mb-1"),
            P("3 new alerts", cls="text-muted small mb-4"),
            Div(
                Div(
                    Div(Icon("lightning-fill", cls="text-warning"), cls="ll-tx-icon"),
                    Div(
                        Div("Bill due soon", cls="ll-tx-title"),
                        Div("PG&E · $84.00 due in 3 days", cls="ll-tx-subtitle"),
                        cls="ll-tx-details",
                    ),
                    cls="ll-tx-item",
                ),
                Div(
                    Div(Icon("graph-up-arrow", cls="text-success"), cls="ll-tx-icon"),
                    Div(
                        Div("Stripe payout received", cls="ll-tx-title"),
                        Div("+$2,450.00 landed in checking", cls="ll-tx-subtitle"),
                        cls="ll-tx-details",
                    ),
                    cls="ll-tx-item",
                ),
                Div(
                    Div(Icon("exclamation-triangle-fill", cls="text-danger"), cls="ll-tx-icon"),
                    Div(
                        Div("Dining budget at 93%", cls="ll-tx-title"),
                        Div("$280 spent of $300 · 7 days left", cls="ll-tx-subtitle"),
                        cls="ll-tx-details",
                    ),
                    cls="ll-tx-item",
                ),
                cls="ll-tx-list mb-4",
            ),
            Button(
                "Mark all as read",
                cls="btn btn-outline-secondary w-100",
                style="border-radius:12px",
            ),
        ),
        sheet_id="notif-sheet",
        height="auto",
    )


# ── ROUTES ────────────────────────────────────────────────────────────────────


@app.get("/")
def index(req) -> Any:
    theme = theme_from_req(req)
    return Div(
        Style(CSS),
        Div(
            ll_appbar(theme),
            ll_balance_card(),
            ll_quick_actions(),
            ll_kpi_strip(),
            Tabs(
                ("tab-activity", "Activity", True),
                ("tab-budgets", "Budgets", False),
                ("tab-analytics", "Analytics", False),
                variant="pills",
                justified=True,
                cls="mb-4",
            ),
            Div(
                Div(ll_transactions(), id="tab-activity", cls="tab-pane fade show active"),
                Div(ll_budgets_tab(), id="tab-budgets", cls="tab-pane fade"),
                Div(ll_analytics_tab(), id="tab-analytics", cls="tab-pane fade"),
                cls="tab-content",
            ),
            cls="ll-container",
        ),
        ll_bottom_nav("home"),
        new_tx_sheet(),
        notif_sheet(),
        data_bs_theme=theme,
        cls="ll-app",
    )


@app.get("/api/recipients/search")
def recipients_search(q: str = "") -> Any:
    """HTMX search handler for recipient SearchableSelect on /send page."""
    from fasthtml.common import A as FTA

    q_lower = q.lower()
    hits = [
        (rid, name)
        for rid, name in RECIPIENTS
        if not q or q_lower in name.lower() or q_lower in rid.lower()
    ]
    if not hits:
        return Div(P("No contacts found.", cls="text-muted small px-3 py-2"), cls="list-group")
    return Div(
        *[
            FTA(
                name,
                href="#",
                cls="list-group-item list-group-item-action small",
                data_value=rid,
                data_fs_searchable_option="true",
            )
            for rid, name in hits
        ],
        cls="list-group",
    )


@app.get("/send")
def send_page(req) -> Any:
    theme = theme_from_req(req)

    return Div(
        Style(CSS),
        Div(
            ll_appbar(theme, "Send Money", "Transfer funds instantly"),
            Div(
                H5(
                    "Amount to Send",
                    cls="fw-bold mb-1 text-muted small text-uppercase",
                    style="letter-spacing:.06em",
                ),
                InputGroup(
                    InputGroupText("$"),
                    Input(
                        "send_amount",
                        input_type="number",
                        placeholder="0.00",
                        cls="form-control form-control-lg fw-bold fs-2",
                        style="border-radius:0 14px 14px 0;",
                        step="0.01",
                    ),
                    size="lg",
                    cls="mb-4 shadow-sm",
                ),
                H5("Send To", cls="fw-bold mb-2"),
                SearchableSelect(
                    "/api/recipients/search",
                    name="recipient",
                    initial_options=RECIPIENTS[:5],
                    placeholder="Search contacts...",
                    csp_safe=True,
                    cls="mb-4",
                ),
                H5("Payment Method", cls="fw-bold mb-2"),
                Div(
                    *[
                        Div(
                            Div(
                                Div(
                                    Span(f"•••• {c['last4']}", cls="fw-600"),
                                    Span(c["network"], cls="ms-2 text-muted small"),
                                ),
                                Span(c["name"], cls="text-muted small"),
                            ),
                            cls=f"form-check p-3 border rounded-3 mb-2 {'border-primary bg-primary bg-opacity-10' if i == 0 else ''}",
                            style="cursor:pointer",
                        )
                        for i, c in enumerate(CARDS_DATA[:3])
                    ],
                    cls="mb-4",
                ),
                Div(
                    Switch("instant", label="Instant Transfer (free)", checked=True, cls="mb-2"),
                    Switch("save_payee", label="Save as frequent payee"),
                    cls="mb-4 px-1",
                ),
                Row(
                    Col(
                        Button(
                            "Request",
                            cls="btn btn-outline-secondary w-100 fw-600",
                            style="border-radius:14px;min-height:3rem",
                        ),
                        md=4,
                        cls="mb-2",
                    ),
                    Col(
                        Button(
                            Icon("send-fill", cls="me-2"),
                            "Send Money",
                            cls="btn btn-primary w-100 fw-700",
                            style="border-radius:14px;min-height:3rem",
                        ),
                        md=8,
                        cls="mb-2",
                    ),
                ),
                cls="",
            ),
            cls="ll-container",
        ),
        ll_bottom_nav("send"),
        data_bs_theme=theme,
        cls="ll-app",
    )


@app.get("/cards")
def cards_page(req) -> Any:
    theme = theme_from_req(req)
    filter_q = req.query_params.get("type", "all")

    visible = (
        CARDS_DATA
        if filter_q == "all"
        else [c for c in CARDS_DATA if c["network"].lower() == filter_q]
    )

    card_displays = []
    for c in visible:
        card_displays.append(
            Div(
                # ── Top row: network chip + actions menu ─────
                Div(
                    Span(
                        c["network"],
                        cls="ll-card-network",
                        style="background:rgba(255,255,255,0.12);padding:0.2rem 0.6rem;border-radius:50px;font-size:0.7rem;font-weight:700;letter-spacing:0.08em;",
                    ),
                    Dropdown(
                        DropdownItem("View Transactions", href="#"),
                        DropdownItem("Set Spend Limit", href="#"),
                        DropdownItem("Freeze Card", href="#"),
                        DropdownItem("Report Lost / Stolen", href="#", cls="text-danger"),
                        label=Icon("three-dots"),
                        variant="link",
                        cls="text-white p-0",
                    ),
                    cls="d-flex justify-content-between align-items-center",
                ),
                # ── Middle: embossed card number + name ──────
                Div(
                    Div(f"•••• •••• •••• {c['last4']}", cls="ll-card-number mb-1"),
                    Div(c["name"], cls="ll-card-name"),
                ),
                # ── Bottom row: balance + valid thru ─────────
                Div(
                    Div(
                        Div(
                            "Balance",
                            style="font-size:0.65rem;opacity:0.65;letter-spacing:0.06em;text-transform:uppercase;",
                        ),
                        Div(f"${c['balance']:,.2f}", cls="ll-card-balance"),
                    ),
                    Div(
                        Div(
                            "Valid Thru",
                            style="font-size:0.65rem;opacity:0.65;letter-spacing:0.06em;text-transform:uppercase;",
                        ),
                        Div("12 / 28", style="font-size:0.85rem;font-weight:600;opacity:0.9;"),
                    ),
                    cls="d-flex justify-content-between align-items-end",
                ),
                cls="ll-card-display ll-animate-scale",
                style=f"background: linear-gradient(135deg, {c['color']} 0%, #0d1117 100%);",
            )
        )

    return Div(
        Style(CSS),
        Div(
            ll_appbar(theme, "My Cards", f"{len(CARDS_DATA)} cards linked"),
            FilterBar(
                *[
                    A(
                        label,
                        href=f"/cards?type={val}",
                        cls=f"btn btn-sm {'btn-primary' if filter_q == val else 'btn-outline-secondary'} me-1",
                    )
                    for val, label in [
                        ("all", "All"),
                        ("visa", "Visa"),
                        ("mc", "Mastercard"),
                        ("bank", "Bank"),
                    ]
                ],
                cls="mb-4",
            ),
            Div(*card_displays, cls="mb-4 d-grid gap-3"),
            Div(
                H5("Quick Actions", cls="fw-bold mb-3"),
                ButtonToolbar(
                    Button(
                        Icon("plus-circle", cls="me-2"), "Add Card", cls="btn btn-outline-primary"
                    ),
                    Button(
                        Icon("arrow-left-right", cls="me-2"),
                        "Transfer",
                        cls="btn btn-outline-secondary",
                    ),
                    Button(
                        Icon("download", cls="me-2"), "Statement", cls="btn btn-outline-secondary"
                    ),
                    cls="gap-2 flex-wrap",
                ),
                Div(
                    H5("Limits & Spending", cls="fw-bold mt-4 mb-3"),
                    Div(
                        Div(
                            Div("Sapphire Reserve", cls="fw-600 mb-1"),
                            Progress(value=23, variant="primary"),
                            Div(
                                Span("$2,340 used", cls="text-muted small"),
                                Span("$7,660 remaining", cls="small fw-600 text-success"),
                                cls="d-flex justify-content-between mt-1",
                            ),
                            cls="ll-budget-item",
                        ),
                        Div(
                            Div("Gold Cash Rewards", cls="fw-600 mb-1"),
                            Progress(value=14, variant="warning"),
                            Div(
                                Span("$680 used", cls="text-muted small"),
                                Span("$4,320 remaining", cls="small fw-600 text-success"),
                                cls="d-flex justify-content-between mt-1",
                            ),
                            cls="ll-budget-item",
                        ),
                    ),
                ),
            ),
            cls="ll-container",
        ),
        ll_bottom_nav("cards"),
        data_bs_theme=theme,
        cls="ll-app",
    )


@app.get("/profile")
def profile_page(req) -> Any:
    theme = theme_from_req(req)
    return Div(
        Style(CSS),
        Div(
            ll_appbar(theme, "Profile & Settings", "Michael Richardson"),
            Div(
                Div(
                    Div(
                        "MR",
                        cls="ll-avatar mx-auto mb-3",
                        style="width:4.5rem;height:4.5rem;font-size:1.5rem",
                    ),
                    H4("Michael Richardson", cls="fw-bold text-center mb-1"),
                    P("michael@example.com", cls="text-muted text-center small mb-0"),
                    Div(
                        Badge("Pro Member", variant="success", cls="me-2"),
                        Badge("Since 2023", variant="secondary"),
                        cls="d-flex justify-content-center gap-1 mt-2 mb-4",
                    ),
                    cls="",
                ),
                H6(
                    "Notifications",
                    cls="fw-bold text-uppercase small mb-2 text-muted",
                    style="letter-spacing:.06em",
                ),
                Div(
                    *[
                        Div(
                            Div(
                                Div(label, cls="fw-600 small"),
                                Div(desc, cls="text-muted", style="font-size:0.75rem"),
                            ),
                            Switch(notif_id, checked=(i < 2)),
                            cls="ll-profile-row",
                        )
                        for i, (notif_id, label, desc) in enumerate(NOTIF_SETTINGS)
                    ],
                    cls="ll-profile-section mb-4",
                ),
                H6(
                    "Security",
                    cls="fw-bold text-uppercase small mb-2 text-muted",
                    style="letter-spacing:.06em",
                ),
                Div(
                    Div(
                        Div("Biometric Login", cls="fw-600 small"),
                        Switch("biometric", checked=True),
                        cls="ll-profile-row",
                    ),
                    Div(
                        Div("Two-Factor Auth", cls="fw-600 small"),
                        Switch("twofa", checked=True),
                        cls="ll-profile-row",
                    ),
                    Div(
                        Div("Transaction PIN", cls="fw-600 small"),
                        A("Change", href="#", cls="text-primary text-decoration-none small fw-600"),
                        cls="ll-profile-row",
                    ),
                    cls="ll-profile-section mb-4",
                ),
                H6(
                    "Appearance",
                    cls="fw-bold text-uppercase small mb-2 text-muted",
                    style="letter-spacing:.06em",
                ),
                Div(
                    Div(
                        Div("Dark Mode", cls="fw-600 small"),
                        ll_theme_toggle(theme, "ledgerleaf-profile-theme-toggle"),
                        cls="ll-profile-row",
                    ),
                    cls="ll-profile-section mb-4",
                ),
                H6(
                    "Account",
                    cls="fw-bold text-uppercase small mb-2 text-muted",
                    style="letter-spacing:.06em",
                ),
                Div(
                    *[
                        Div(
                            Div(
                                label,
                                cls=f"fw-600 small {'text-danger' if label == 'Sign Out' else ''}",
                            ),
                            Icon("chevron-right", cls="text-muted"),
                            cls="ll-profile-row",
                            style="cursor:pointer",
                        )
                        for label in [
                            "Personal Info",
                            "Linked Accounts",
                            "Data & Privacy",
                            "Help & Support",
                            "Sign Out",
                        ]
                    ],
                    cls="ll-profile-section mb-4",
                ),
            ),
            cls="ll-container",
        ),
        ll_bottom_nav("profile"),
        data_bs_theme=theme,
        cls="ll-app",
    )


@app.post("/theme/toggle")
def toggle_theme(req) -> Any:
    req.session[THEME_KEY] = "dark" if theme_from_req(req) == "light" else "light"
    return hx_refresh()


if __name__ == "__main__":
    serve(port=5012)
