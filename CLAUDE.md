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
    Hero, PageHeader, DashboardGrid,
    # Forms
    Button, Input, Select, Form, FormGroup, Switch, Checkbox, Radio,
    SearchableSelect, DatePicker, MultiSelect,
    # Display
    Card, Badge, Avatar, Table, DataTable, StatCard, Image,
    # Feedback
    Alert, Toast, Modal, Spinner, Progress, Placeholder,
    # Navigation
    Navbar, Tabs, Accordion, Dropdown, Breadcrumb, Pagination,
    SidebarNavbar, Drawer,
    # Patterns
    FeatureGrid, PricingGroup, TestimonialSection, FooterModern,
    # Layouts
    AuthLayout, DashboardLayout, LandingLayout,
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
            hx_post="/validate/email",
            hx_target="next .validation-msg",
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

## Testing

```bash
cd Faststrap
python -m pytest -q   # 857+ tests passing
```
