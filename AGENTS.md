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
    Hero, PageHeader, DashboardGrid, SectionHeader, AspectRatio, Separator,
    # Forms
    Button, Input, Select, Form, FormGroup, Switch, Checkbox, Radio,
    SearchableSelect, MultiSelect, DateRangePicker, OTPInput, OTPInputGroup,
    LiveValidationField,
    # Display
    Card, Badge, Tag, Kbd, Avatar, AvatarGroup, Table, DataTable,
    StatCard, MetricCard, TrendCard, KPICard, Image, Carousel,
    CodeBlock, JsonViewer, Timeline, Stepper, EmptyState,
    # Feedback
    Alert, Toast, SimpleToast, Modal, Spinner, Progress, ProgressRing,
    Placeholder, Tooltip, Popover, ErrorPage, NotificationCenter,
    # Navigation
    Navbar, GlassNavbar, GlassNavItem, SidebarNavbar, Tabs, Accordion, Dropdown,
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
    # Theme
    ThemeToggle,
    # PWA
    add_pwa, PwaMeta,
)
from faststrap.presets import (
    # HTMX Presets & Responses
    ActiveSearch, InfiniteScroll, AutoRefresh, LazyLoad, LoadingButton,
    OptimisticAction, ConfirmPrompt, require_auth, toast_response,
    hx_redirect, hx_refresh, SSEStream,
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
8. **set_component_defaults()** — configure global defaults for Button, Card, Input, Alert at app startup for consistency
9. **Bootstrap utilities over custom CSS** — use d-none, d-md-block, p-2 p-lg-4, text-center text-lg-start instead of custom media queries

## Responsive Layout Rules

### Card Grids

Use `Row` + `Col` with responsive `cols_*` parameters:

```python
Row(
    Col(Card("A"), cols=12, cols_md=6, cols_lg=3),
    Col(Card("B"), cols=12, cols_md=6, cols_lg=3),
    Col(Card("C"), cols=12, cols_md=6, cols_lg=3),
    Col(Card("D"), cols=12, cols_md=6, cols_lg=3),
    g=3,
)
```

Breakpoints:
- `cols=12` — mobile (<768px): 1 per row
- `cols_md=6` — tablet (≥768px): 2 per row
- `cols_lg=3` — desktop (≥992px): 4 per row

### Common Patterns

**4 cards:** `cols=12, cols_md=6, cols_lg=3`
**3 cards:** `cols=12, cols_md=4, cols_lg=4`
**2 cards:** `cols=12, cols_md=6`
**1 featured + 2 side:** `Col(..., cols=12, cols_lg=8)` + `Col(..., cols=12, cols_lg=4)`

### Sidebar Layout

```python
Row(
    Col(
        SidebarNavbar(...),
        cols=12, cols_md=3,
        cls="d-none d-md-block",  # Hide on mobile
    ),
    Col(
        # Main content
        ...
        cols=12, cols_md=9,
    ),
)
```

Use `Drawer` or `BottomNav` for mobile navigation.

### Responsive Utilities

```python
# Show/hide at breakpoints
Div("Desktop only", cls="d-none d-lg-block")
Div("Mobile only", cls="d-block d-lg-none")

# Responsive spacing
Card("Content", cls="p-2 p-lg-4")
Div("Content", cls="mb-3 mb-md-4")

# Responsive text alignment
H1("Title", cls="text-center text-lg-start")
```

### Never do this

```python
# BAD: custom CSS media query
Div("Content", style="@media (min-width: 768px) { width: 50%; }")

# GOOD: Bootstrap utility
Div("Content", cls="col-12 col-md-6")
```

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

## UX Feedback Rules

User feedback is non-negotiable. Every action that mutates state must show loading, success, or error feedback.

### Button Loading State

Use `LoadingButton` for HTMX form submissions:

```python
from faststrap.presets import LoadingButton

LoadingButton(
    "Save",
    endpoint="/api/save",
    method="post",
    target="#form",
    variant="primary",
)
```

For non-HTMX forms, use `Button(loading=True)` with a `Spinner` indicator:

```python
Button(
    "Save",
    variant="primary",
    loading=True,
    spinner=True,
    loading_text="Saving...",
)
```

### Success / Error Feedback

```python
from faststrap import Toast, Alert, FormErrorSummary

# Success
Toast("Changes saved!", variant="success", duration=3000)

# Error
Toast("Something went wrong.", variant="danger", duration=5000)

# Inline error in forms
FormErrorSummary({"email": "Invalid email"}, title="Please fix:")
```

### Form Validation Feedback

```python
from faststrap import FormErrorSummary, FormGroupFromErrors

@app.post("/login")
def login(email: str, password: str):
    errors = validate(email, password)
    if errors:
        return (
            FormErrorSummary(errors),
            FormGroupFromErrors(Input(name="email", value=email), "email", errors=errors),
            FormGroupFromErrors(Input(name="password"), "password", errors=errors),
        )
    return Toast("Welcome!", variant="success"), Redirect("/dashboard")
```

## Testing

```bash
cd Faststrap
python -m pytest -q   # 890+ tests passing
```

## Deployment

### Static Export

For marketing sites, docs, and blogs:

```bash
python -m faststrap export main:app ./dist
```

See `docs/deployment/static-export.md` for full documentation.

### Dynamic Deployment

For apps with HTMX, sessions, or server-side logic:

- **Vercel:** Use `add_bootstrap(app, use_cdn=True)` and expose the ASGI app
- **Railway:** Standard FastHTML deployment with `python main.py`
- **Render:** Use `web: python main.py` in `Procfile`
- **Fly.io:** Use the Dockerfile or `fly launch`
- **VPS:** Use `gunicorn` or `uvicorn` with `main:app`

Always run `faststrap doctor` before deploying:

```bash
python -m faststrap doctor
```
