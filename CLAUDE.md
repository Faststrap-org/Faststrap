# CLAUDE.md

This file helps Claude assist developers building applications with Faststrap + FastHTML.

## What is Faststrap?

Faststrap is a Python component library for [FastHTML](https://github.com/AnswerDotAI/fasthtml) that provides **152+ UI components** built on Bootstrap 5. It lets you build web apps, dashboards, and portals entirely in Python — no JavaScript required.

**Install:** `pip install faststrap`
**Docs:** https://faststrap-org.github.io/Faststrap/
**GitHub:** https://github.com/Faststrap-org/Faststrap

## How to Help Developers Build with Faststrap

When a developer asks you to build an app, dashboard, or page with Faststrap:

1. **Use Faststrap components first** — don't write raw Bootstrap HTML when a Faststrap component exists.
2. **Use HTMX for interactions** — not custom JavaScript. HTMX is the standard interaction layer.
3. **Use Bootstrap for layout** — rows, cols, grid utilities for responsive structure.
4. **Use custom CSS only for polish** — brand colors, gradients, visual refinements that Bootstrap doesn't cover.
5. **JavaScript only when necessary** — PWA features, browser APIs, maps, media — things HTMX/Bootstrap can't handle.

## Quick Setup

```python
from fasthtml.common import FastHTML, serve
from faststrap import add_bootstrap, Button, Card, Alert, Navbar

app = FastHTML()
add_bootstrap(app)  # Adds Bootstrap 5.3 CSS/JS + Bootstrap Icons

@app.get("/")
def home():
    return Navbar(
        Navbar.Brand("MyApp"),
        Navbar.Collapse(
            Navbar.Item("Home", href="/"),
            Navbar.Item("Dashboard", href="/dashboard"),
        ),
    ), Card(
        "Welcome to my app!",
        Button("Get Started", variant="primary"),
    )
```

## Component Import Pattern

```python
from faststrap import (
    # Layout
    Container, Row, Col, Stack, Cluster, Center,
    Hero, PageHeader, DashboardGrid, SectionHeader, AspectRatio, Separator,
    # Forms
    Button, Input, Select, Form, FormGroup, Switch, Checkbox, Radio,
    SearchableSelect, MultiSelect, DateRangePicker, OTPInput, OTPInputGroup,
    LiveValidationField, OTPInput, OTPInputGroup,
    # Display
    Card, Badge, Tag, Kbd, Avatar, AvatarGroup, Table, DataTable,
    StatCard, MetricCard, TrendCard, KPICard, Image, Carousel,
    CodeBlock, JsonViewer, Timeline, Stepper, EmptyState,
    # Feedback
    Alert, Toast, SimpleToast, Modal, Spinner, Progress, Placeholder,
    # Navigation
    Navbar, GlassNavbar, GlassNavItem, Tabs, Accordion, Dropdown,
    Breadcrumb, Pagination, SidebarNavbar, Drawer,
    # Patterns
    FeatureGrid, PricingGroup, TestimonialSection, FooterModern,
    # Layouts
    AuthLayout, DashboardLayout, LandingLayout,
    # Accessibility
    SkipLink, LiveRegion, VisuallyHidden, FocusTrap,
    # Theme
    ThemeToggle,
)
```

## Common App Patterns

### Dashboard Layout
```python
from faststrap import DashboardLayout, SidebarNavbar, DashboardGrid, StatCard

@app.get("/dashboard")
def dashboard():
    return DashboardLayout(
        sidebar=SidebarNavbar(
            SidebarNavItem("Overview", icon="speedometer2", href="/"),
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

### Auth Pages
```python
from faststrap import AuthLayout, Card, Form, FormGroup, Input, Button

@app.get("/login")
def login():
    return AuthLayout(
        Card(
            Form(
                FormGroup("Email", Input(name="email", type="email")),
                FormGroup("Password", Input(name="password", type="password")),
                Button("Sign In", type="submit", variant="primary", w="100%"),
                method="post",
                action="/login",
            ),
            title="Sign In",
        ),
        brand="MyApp",
    )
```

### Forms with HTMX Validation
```python
from faststrap import Form, FormGroup, Input, Button, LiveValidationField

Form(
    FormGroup("Email",
        LiveValidationField(
            Input(name="email", type="email"),
            validate_url="/validate/email",
            label="Email",
        ),
    ),
    FormGroup("Password", Input(name="password", type="password")),
    Button("Register", type="submit"),
    method="post",
    action="/register",
)
```

### Data Table with Filters
```python
from faststrap import DataTable, FilterBar, Select, Input

FilterBar(
    Select(["All", "Active", "Inactive"], name="status"),
    Input(placeholder="Search...", name="q"),
    hx_get="/api/users",
    hx_target="#user-table",
)
DataTable(df=users_df, page_size=20, sortable=True, exportable=True)
```

### Landing Page
```python
from faststrap import LandingLayout, Hero, FeatureGrid, TestimonialSection, FooterModern

LandingLayout(
    Hero(
        title="Build Faster with Python",
        subtitle="152+ UI components for FastHTML",
        cta_text="Get Started",
        cta_href="/docs",
    ),
    FeatureGrid(
        Feature(icon="lightning", title="Fast", description="Pure Python, zero JS"),
        Feature(icon="shield", title="Secure", description="Server-rendered"),
        Feature(icon="code", title="Simple", description="Clean API"),
    ),
    TestimonialSection(
        Testimonial("Amazing library!", author="Dev", role="Engineer"),
    ),
)
```

## Component Categories

| Category | Components | Use For |
|----------|-----------|---------|
| Forms | Button, Input, Select, Form, Switch, Checkbox, etc. | User input, data entry |
| Display | Card, Badge, Avatar, Table, Chart, Image | Content presentation |
| Feedback | Alert, Toast, Modal, Spinner, Progress | User notifications |
| Navigation | Navbar, Tabs, Accordion, Drawer, Sidebar | App structure |
| Layout | Container, Row, Col, Stack, Hero, Grid | Page layout |
| Patterns | FeatureGrid, Pricing, Testimonials | Landing pages |
| Presets | ActiveSearch, InfiniteScroll, LoadingButton | HTMX interactions |

## Key Rules

- **Never write raw HTML** when a Faststrap component exists for the same purpose
- **Always use `add_bootstrap(app)`** in the app setup — components won't work without it
- **Use HTMX for all dynamic behavior** — `hx_get`, `hx_post`, `hx_target`, etc.
- **Mobile-first** — start with `cols=1`, expand with `cols_md=2`, `cols_lg=3`, etc.
- **Dark mode** — use `add_bootstrap(app, mode="dark")` or `ThemeToggle()`
- **Bootstrap classes work** — `mb-3`, `text-center`, `d-flex`, etc. are all valid
- **Icons** — use Bootstrap Icons via `Icon("icon-name")` or raw class `bi bi-icon-name`
- **UX feedback is required** — every action must show loading, success, or error state. Use `LoadingButton`, `Toast`, `Alert`, `FormErrorSummary`, and `hx-indicator`. Never ship a button that does nothing visible when clicked.
- **set_component_defaults()** — configure global defaults for Button, Card, Input, Alert at app startup
- **Bootstrap utilities over custom CSS** — use d-none, d-md-block, p-2 p-lg-4 instead of custom media queries

## Responsive Layout Rules

### Card Grids

```python
Row(
    Col(Card("A"), cols=12, cols_md=6, cols_lg=3),
    Col(Card("B"), cols=12, cols_md=6, cols_lg=3),
    Col(Card("C"), cols=12, cols_md=6, cols_lg=3),
    Col(Card("D"), cols=12, cols_md=6, cols_lg=3),
    g=3,
)
```

- `cols=12` — mobile: 1 per row
- `cols_md=6` — tablet: 2 per row
- `cols_lg=3` — desktop: 4 per row

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

Use `Drawer` or `BottomNav` for mobile.

### Responsive Utilities

```python
# Show/hide
Div("Desktop", cls="d-none d-lg-block")
Div("Mobile", cls="d-block d-lg-none")

# Responsive spacing
Card("Content", cls="p-2 p-lg-4")
Div("Content", cls="mb-3 mb-md-4")
```

## UX Feedback Patterns

### Button Loading State

```python
from faststrap import LoadingButton

LoadingButton(
    "Save",
    endpoint="/api/save",
    method="post",
    target="#form",
    variant="primary",
)
```

For non-HTMX forms:

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

# Success toast
Toast("Changes saved!", variant="success", duration=3000)

# Error toast
Toast("Something went wrong.", variant="danger", duration=5000)

# Inline form errors
FormErrorSummary({"email": "Invalid email"}, title="Please fix:")
```

### Form Validation Flow

```python
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
