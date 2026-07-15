# Faststrap — Agent Guide

This file provides context for AI agents building applications with Faststrap + FastHTML.

## What is Faststrap?

Faststrap is a Python component library for [FastHTML](https://github.com/AnswerDotAI/fasthtml) that provides **152+ UI components** built on Bootstrap 5. It enables building web apps, dashboards, portals, and data applications entirely in Python with zero JavaScript.

- **Install:** `pip install faststrap`
- **Docs:** https://faststrap-org.github.io/Faststrap/
- **GitHub:** https://github.com/Faststrap-org/Faststrap
- **PyPI:** https://pypi.org/project/faststrap/

## When to Use Faststrap

Use Faststrap when building:
- Web applications (SaaS, portals, admin panels)
- Data dashboards and analytics tools
- Landing pages and marketing sites
- Auth flows (login, register, forgot password)
- CRUD interfaces and form-heavy apps
- Real-time dashboards with SSE streaming
- Mobile-responsive web apps

## App Setup Pattern

```python
from fasthtml.common import FastHTML
from faststrap import add_bootstrap

app = FastHTML()
add_bootstrap(app)  # Required — adds Bootstrap 5.3 CSS/JS
```

## Component Import

```python
from faststrap import (
    # Layout
    Container, Row, Col, Stack, Cluster, Center,
    Hero, PageHeader, DashboardGrid, AspectRatio, Separator,
    # Forms
    Button, Input, Select, Form, FormGroup, Switch, Checkbox, Radio,
    SearchableSelect, MultiSelect, DateRangePicker, OTPInput, OTPInputGroup,
    # Display
    Card, Badge, Tag, Kbd, Avatar, AvatarGroup, Table, DataTable,
    StatCard, MetricCard, TrendCard, KPICard, Image, Carousel,
    CodeBlock, JsonViewer, Timeline, Stepper, EmptyState,
    # Feedback
    Alert, Toast, SimpleToast, Modal, Spinner, Progress, ProgressRing,
    Placeholder, Tooltip, Popover, ErrorPage, NotificationCenter,
    # Navigation
    Navbar, GlassNavbar, SidebarNavbar, Tabs, Accordion, Dropdown,
    Breadcrumb, Pagination, Drawer, BottomNav, Scrollspy, CommandPalette,
    # Patterns
    FeatureGrid, PricingGroup, PricingTier, TestimonialSection,
    FooterModern, Testimonial,
    # Layouts
    AuthLayout, DashboardLayout, LandingLayout,
    # Accessibility
    SkipLink, LiveRegion, VisuallyHidden, FocusTrap,
    # SEO
    SEO, PageMeta, StructuredData,
    # HTMX Presets
    ActiveSearch, InfiniteScroll, AutoRefresh, LazyLoad, LoadingButton,
    # PWA
    add_pwa, PwaMeta,
)
```

## Build Principles

1. **Faststrap components first** — check the import list above before writing raw HTML
2. **HTMX for interactions** — use hx_get, hx_post, hx_target, hx_swap for all dynamic behavior
3. **Bootstrap for layout** — Row/Col grid, flex utilities, spacing (mb-3, p-2, etc.)
4. **Custom CSS for polish only** — brand colors, gradients, custom visual treatments
5. **JavaScript only when needed** — PWA features, browser APIs, maps, media players
6. **Mobile-first** — start with single column (cols=1), expand with cols_md=2, cols_lg=3, etc.
7. **Dark mode** — use add_bootstrap(app, mode="dark") or ThemeToggle() component

## Component Patterns

### Cards
```python
Card(
    Card.Header("Title"),
    Card.Body("Content"),
    Card.Footer("Footer actions"),
    variant="primary",
)
```

### Forms
```python
Form(
    FormGroup("Email", Input(name="email", type="email", required=True)),
    FormGroup("Password", Input(name="password", type="password")),
    FormGroup("Remember me", Switch(name="remember")),
    Button("Sign In", type="submit", variant="primary"),
    method="post",
    action="/login",
)
```

### Tables
```python
# Static table
Table(
    THead(TRow(THead("Name"), THead("Email"))),
    TBody(
        TRow(TCell("Alice"), TCell("alice@example.com")),
    ),
    striped=True, hover=True,
)

# Data-driven table with sort/filter/pagination
DataTable(df=my_dataframe, page_size=20, sortable=True, filterable=True)
```

### HTMX Interactions
```python
# Live search
FilterBar(
    Input(placeholder="Search...", name="q"),
    hx_get="/api/search",
    hx_trigger="input changed delay:300ms",
    hx_target="#results",
)

# Infinite scroll
InfiniteScroll(url="/api/items", target="#list")

# Loading button
LoadingButton("Save", hx_post="/api/save", loading_text="Saving...")
```

### Dashboard Layout
```python
DashboardLayout(
    sidebar=SidebarNavbar(
        SidebarNavItem("Dashboard", icon="speedometer2", href="/"),
        SidebarNavItem("Users", icon="people", href="/users"),
        SidebarNavItem("Settings", icon="gear", href="/settings"),
    ),
    content=DashboardGrid(
        StatCard("Revenue", "$12K", "+5%", delta_color="success"),
        StatCard("Users", "1.2K", "+12%"),
        StatCard("Orders", "456", "+3%"),
        cols=3,
    ),
)
```

### Landing Page
```python
LandingLayout(
    Hero(
        title="Build Faster with Python",
        subtitle="152+ UI components for FastHTML",
        cta_text="Get Started",
        cta_href="/docs",
    ),
    FeatureGrid(
        Feature(icon="lightning", title="Fast", description="Pure Python"),
        Feature(icon="shield", title="Secure", description="Server-rendered"),
        Feature(icon="code", title="Simple", description="Clean API"),
    ),
    TestimonialSection(
        Testimonial("Amazing library!", author="Dev"),
    ),
    FooterModern(brand="MyApp"),
)
```

### Auth Pages
```python
AuthLayout(
    Card(
        Form(
            FormGroup("Email", Input(name="email", type="email")),
            FormGroup("Password", Input(name="password", type="password")),
            Button("Sign In", type="submit", variant="primary", w="100%"),
            method="post",
        ),
        title="Sign In",
    ),
    brand="MyApp",
)
```

## Data Science / Dashboard Components

```python
from faststrap import Chart, DataTable, FilterBar, DashboardGrid, MetricCard

# Chart (wraps matplotlib/plotly/altair)
Chart(fig=my_plotly_figure, responsive=True)

# DataFrame table
DataTable(df=pandas_df, sortable=True, exportable=True)

# Real-time metrics
MetricCard("CPU Usage", "45%", "+2%")
```

## Testing

```bash
cd Faststrap
python -m pytest -q   # 857+ tests passing
```
