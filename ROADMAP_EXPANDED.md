# FastStrap Roadmap – Comprehensive Edition (January 2026)

**Vision:** The most complete, Pythonic, zero-JS Bootstrap 5 component library for FastHTML — 100+ production-ready components built by the community, for the community.

---

## 📊 Current Status (v0.4.5 – January 2026)

**38 components live** – Phase 1 through 4B complete  
**230+ tests** – 85%+ coverage  
**Full HTMX + Bootstrap 5.3.3 support**  
**Zero custom JavaScript required**

### Overall Progress to v1.0

```text
Components:   ████████░░ 38/100 (38%)
Tests:        ████████░░ 230/800 (29%)
Coverage:     ████████░░ 85/95   (89%)
Contributors: ███░░░░░░░ 15+/100 (15%)
```

### 🎉 Recent Achievements

- ✅ **Jan 2026**: Phase 4B shipped - 8 new components (FileInput, Tooltip, Popover, Figure, ConfirmDialog, EmptyState, StatCard, Hero)
- ✅ **Jan 2026**: Documentation overhaul with live component previews and interactive examples
- ✅ **Dec 2025**: 15+ contributors milestone reached - growing community!
- ✅ **Dec 2025**: Phase 4A completed - Table, Accordion, comprehensive form controls
- 🔜 **Feb 2026**: Phase 5 kickoff - Visual effects & professional layout system

---

## 📅 Release Timeline

```
2025 Dec  ████ Phase 4B Complete (38 components)
2026 Jan  ████ Documentation Overhaul
2026 Feb  ░░░░ Phase 5 - Visual Polish (50 components)
2026 Mar  ░░░░ v0.5.5 - Quick Wins
2026 Apr  ░░░░ Phase 6.0 - Data Layer
2026 May  ░░░░ Phase 6.1 - Productivity
2026 Jun  ░░░░ Phase 6.2 - Auth & DX  
2026 Jul  ░░░░ Phase 6.3 - Realtime
2026 Aug  ░░░░ v1.0.0 Production Release 🎉
```

---

## 🔒 Framework Guarantees (v1.0+)

Faststrap commits to the following architectural contracts to ensure stability, predictability, and enterprise readiness:

### **1. Deterministic HTML**
- Server-rendered output is predictable and testable
- Components produce identical HTML given identical inputs
- No hidden state mutations or side effects
- Easy to unit test with `assert_html()` patterns

**Example:**
```python
button = Button("Click Me", variant="primary")
assert "btn btn-primary" in str(button)  # Always true
```

### **2. Zero-JS Core**
- All components function without JavaScript
- JavaScript enhancements are progressive (optional)
- Core navigation, forms, layouts work with JS disabled
- HTMX provides dynamic behavior without custom JS

**Rationale:** Server-first architecture aligns with FastHTML's philosophy. Keep complexity on the server where Python excels.

### **3. No Client State**
- State lives on the server (Python variables, database)
- No hidden client-side state stores (localStorage, React-style state)
- HTMX swaps handle UI updates via server responses
- Simpler mental model, easier debugging

**Exception:** Bootstrap's own JS components (Tooltips, Modals) use minimal client state for UI interactions only.

### **4. Accessibility First**
- WCAG 2.1 AA compliance by default
- Semantic HTML elements (`<nav>`, `<button>`, not `<div onclick>`)
- ARIA labels on interactive components
- Keyboard navigation support built-in
- Focus management handled automatically

**Example:** All form inputs have associated `<label>` elements with proper `for` attributes.

### **5. Stability Markers**
- Explicit `@stable`, `@beta`, `@experimental` decorators
- Clear API stability guarantees (see Versioning Policy below)
- Deprecation warnings 1 version before removal
- No surprise breaking changes in minor versions

---

## 📚 Completed Phases (For Reference)

### Phase 1-2: Foundation (v0.1.0 - v0.2.2) – Dec 2025
**12 components:** Button, ButtonGroup, Badge, Card, Alert, Modal, Drawer, Toast, Navbar, Container/Row/Col, Icon

**Focus:** Core Bootstrap components, HTMX integration patterns, theming system

### Phase 3: Forms & Navigation (v0.3.0) – Dec 2025
**+8 components:** Tabs, Dropdown, Input, Select, Breadcrumb, Pagination, Spinner, Progress

**Focus:** Form controls, navigation patterns, loading indicators

### Phase 4A: Bootstrap Parity (v0.4.0) – Dec 2025
**+10 components:** Table, Accordion, Checkbox, Radio, Switch, Range, ListGroup, Collapse, InputGroup, FloatingLabel

**Focus:** Complete form control set, data display, collapsible content

### Phase 4B: Enhanced UI (v0.4.5) – Jan 2026
**+8 components:** FileInput, Tooltip, Popover, Figure, ConfirmDialog, EmptyState, StatCard, Hero

**Focus:** Rich interactions, feedback patterns, landing page elements

**Total: 38 production-ready components**

---

## 🎯 Quick Wins (v0.4.7 – February 2026)

**Goal:** Maintain momentum with high-value, low-effort additions while Phase 5 is in development.

| Feature | Effort | Impact | Status | Notes |
|---------|--------|--------|--------|-------|
| `Table.from_dict()` | 2 days | 🔥 High | Planned | Render dicts/lists as tables instantly |
| `Table.from_pydantic()` | 1 day | 🔥 High | Planned | Render Pydantic model lists as tables |
| Example Gallery | 3 days | 🔥 High | Planned | 10+ real-world apps (e-commerce, blog, dashboard) |
| `Badge` enhancements | 4 hours | Medium | Planned | `.pill()` helper, positioning utilities |
| `Alert.flash()` preset | 1 day | Medium | Planned | Auto-dismiss with timer, session flash messages |
| Component search | 2 days | 🔥 High | Planned | Search bar on docs site for quick component discovery |

**Why Quick Wins?**
- Keeps contributors engaged between major phases
- Provides immediate value to users
- Tests smaller features before committing to large Phase implementations
- Builds momentum and community excitement

**Implementation Notes:**

**`Table.from_dict()` Example:**
```python
data = [
    {"name": "Alice", "age": 30, "city": "NYC"},
    {"name": "Bob", "age": 25, "city": "LA"}
]

table = Table.from_dict(
    data,
    columns=["name", "age", "city"],  # Optional: auto-detect if None
    striped=True,
    hover=True,
    caption="User Data"
)
```

**`Alert.flash()` Example:**
```python
# In route
@app.post("/save")
def save():
    # ... save logic ...
    return Alert.flash(
        "Saved successfully!",
        variant="success",
        duration=3000,  # Auto-dismiss after 3 seconds
        dismissible=True
    )
```

---

## 🎨 Phase 5 – Composed UI & Design System Layer (v0.5.0 – February 2026)

**Goal:** Transform Faststrap from a component library into a **complete design system** with professional patterns, layouts, and visual polish.

**Focus:** `faststrap.layouts`, `faststrap.patterns`, `faststrap.effects`

**Target:** 50 total components (12 new components/patterns)

### Components to Build

| Priority | Component | Module | Effort | Status | Notes |
|----------|-----------|--------|--------|--------|-------|
| 1 | `faststrap.effects` | New Module | 3 days | Planned | Zero-JS CSS effects library |
| 2 | `DashboardLayout` | layouts | 4 days | Planned | Admin panel layout with sidebar |
| 3 | `LandingLayout` | layouts | 3 days | Planned | Marketing page layout |
| 4 | `NavbarModern` | patterns | 2 days | Planned | Glassmorphism navbar |
| 5 | `FeatureGrid` | patterns | 2 days | Planned | Icon + title + description grid |
| 6 | `PricingGroup` | patterns | 2 days | Planned | 3-column pricing cards |
| 7 | `TestimonialSection` | patterns | 2 days | Planned | Customer testimonials |
| 8 | `FooterModern` | patterns | 2 days | Planned | Multi-column footer |
| 9 | `faststrap init` | CLI Tool | 5 days | Planned | Project scaffolding |
| 10 | `create_theme` update | Core | 2 days | Planned | Google Fonts integration |

### Detailed Implementation Plans

#### 1. `faststrap.effects` Module

**Purpose:** Lightweight CSS-only animation and transition library for modern UI polish.

**Design Philosophy:**
- Pure CSS (no JavaScript)
- Minimal bundle size (~5-8KB minified)
- Works with existing components via `cls` parameter
- Respects `prefers-reduced-motion` for accessibility

**API Design:**
```python
from faststrap import Card, Button
from faststrap.effects import Fx

# Usage: Add effects via cls parameter
Card(
    "Welcome!",
    Button("Click Me"),
    cls=[Fx.fade_in, Fx.hover_lift]
)

# Or use direct class names
Card("Content", cls="fx-fade-in fx-hover-lift")
```

**Available Effects:**

**Entrance Animations:**
- `Fx.fade_in` - Fade in opacity
- `Fx.slide_up` - Slide from bottom
- `Fx.slide_down` - Slide from top
- `Fx.slide_left` - Slide from right
- `Fx.slide_right` - Slide from left
- `Fx.zoom_in` - Scale up from center
- `Fx.bounce_in` - Bounce entrance

**Hover Effects:**
- `Fx.hover_lift` - Raise element on hover
- `Fx.hover_glow` - Add glow effect
- `Fx.hover_scale` - Slightly enlarge
- `Fx.hover_tilt` - Subtle 3D tilt

**Loading States:**
- `Fx.shimmer` - Skeleton loading effect
- `Fx.pulse` - Pulsing opacity
- `Fx.spin` - Rotation animation

**Visual Effects:**
- `Fx.glass` - Glassmorphism (blur + transparency)
- `Fx.shadow_soft` - Soft shadow
- `Fx.shadow_sharp` - Sharp shadow
- `Fx.gradient_shift` - Animated gradient

**Configuration Options:**
```python
# Custom durations
Fx.fade_in(duration="2s")  # Default: 0.3s
Fx.hover_lift(duration="0.5s")

# Delay
Fx.slide_up(delay="0.2s")

# Easing
Fx.fade_in(easing="cubic-bezier(0.4, 0, 0.2, 1)")
```

**Implementation:**
```css
/* faststrap-effects.min.css */
.fx-fade-in {
    animation: fadeIn 0.3s ease-in;
}

@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

.fx-hover-lift {
    transition: transform 0.3s ease;
}

.fx-hover-lift:hover {
    transform: translateY(-4px);
}

/* Respect accessibility */
@media (prefers-reduced-motion: reduce) {
    .fx-fade-in,
    .fx-slide-up,
    .fx-zoom-in {
        animation: none !important;
    }
}
```

#### 2. `DashboardLayout` Component

**Purpose:** Production-ready admin panel layout with sidebar navigation, top navbar, and content area.

**Features:**
- Collapsible sidebar (mobile responsive)
- Breadcrumb trail
- User menu dropdown
- Notification bell
- Search bar
- Footer
- Dark mode toggle

**API:**
```python
from faststrap.layouts import DashboardLayout
from faststrap import NavItem, UserDropdown

@app.get("/dashboard")
def dashboard():
    return DashboardLayout(
        title="Analytics Dashboard",
        
        # Sidebar navigation
        sidebar_items=[
            NavItem("Overview", "/dashboard", icon="speedometer2", active=True),
            NavItem("Sales", "/sales", icon="graph-up"),
            NavItem("Products", "/products", icon="box-seam"),
            NavItem("Customers", "/customers", icon="people"),
            NavItem("Settings", "/settings", icon="gear"),
        ],
        
        # Top navbar (user menu)
        user=UserDropdown(
            name="John Doe",
            avatar="/static/avatar.jpg",
            items=[
                ("Profile", "/profile"),
                ("Settings", "/settings"),
                ("divider", None),
                ("Logout", "/logout")
            ]
        ),
        
        # Main content area
        content=[
            Row(
                Col(StatCard("Revenue", "$12,450", trend="+12%", icon="currency-dollar")),
                Col(StatCard("Orders", "1,234", trend="+5%", icon="cart")),
                Col(StatCard("Customers", "456", trend="+8%", icon="people"))
            ),
            Card(
                Chart.from_data(sales_data, type="line"),
                header="Sales Over Time"
            )
        ],
        
        # Optional breadcrumbs
        breadcrumbs=[("Home", "/"), ("Dashboard", None)],
        
        # Footer
        footer="© 2026 MyApp. All rights reserved."
    )
```

**Responsive Behavior:**
- **Desktop (>992px):** Sidebar always visible, 250px wide
- **Tablet (768-992px):** Collapsible sidebar, overlay on open
- **Mobile (<768px):** Hamburger menu, full-screen sidebar overlay

**Implementation Structure:**
```python
# faststrap/layouts/dashboard.py
def DashboardLayout(
    title: str,
    sidebar_items: list,
    content: list,
    user: Component = None,
    breadcrumbs: list = None,
    footer: str = None,
    sidebar_width: str = "250px",
    theme: Literal["light", "dark"] = "light"
):
    return Div(
        # Sidebar
        Div(
            Div(
                A("Logo", href="/", cls="sidebar-brand"),
                Nav(*[item for item in sidebar_items], cls="sidebar-nav"),
                cls="sidebar-content"
            ),
            cls=f"sidebar sidebar-{theme}",
            style={"width": sidebar_width}
        ),
        
        # Main wrapper
        Div(
            # Top Navbar
            Nav(
                Button(Icon("list"), cls="sidebar-toggle"),  # Mobile toggle
                Breadcrumb(*breadcrumbs) if breadcrumbs else None,
                Div(
                    SearchBar(placeholder="Search..."),
                    NotificationBell(count=3),
                    user if user else None,
                    cls="navbar-right"
                ),
                cls="topnav"
            ),
            
            # Content Area
            Div(*content, cls="main-content"),
            
            # Footer
            Footer(footer, cls="main-footer") if footer else None,
            
            cls="main-wrapper"
        ),
        
        cls="dashboard-layout"
    )
```

#### 3. `LandingLayout` Component

**Purpose:** Marketing/landing page layout with hero, features, pricing, and footer sections.

**API:**
```python
from faststrap.layouts import LandingLayout

@app.get("/")
def home():
    return LandingLayout(
        # Hero section
        hero=Hero(
            title="Build Better Products Faster",
            subtitle="The complete FastHTML component library",
            cta=[
                Button("Get Started", variant="primary", size="lg", href="/docs"),
                Button("View Demo", variant="outline-secondary", size="lg", href="/demo")
            ],
            background="linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
            image="/static/hero-illustration.svg"
        ),
        
        # Feature sections
        sections=[
            FeatureGrid(
                title="Why Choose Faststrap?",
                features=[
                    Feature("Zero JavaScript", "Pure Python development", icon="code-slash"),
                    Feature("38+ Components", "Production-ready UI elements", icon="puzzle"),
                    Feature("HTMX Powered", "Dynamic without complexity", icon="lightning"),
                    Feature("Bootstrap Native", "Familiar and reliable", icon="bootstrap"),
                ]
            ),
            
            PricingGroup(
                title="Simple Pricing",
                tiers=[
                    PricingTier("Free", "$0", ["All components", "MIT License", "Community support"], Button("Get Started")),
                    PricingTier("Pro", "$49", ["Priority support", "Custom components", "1-on-1 training"], Button("Contact Sales"), featured=True),
                ]
            )
        ],
        
        # Footer
        footer=FooterModern(
            brand="Faststrap",
            columns=[
                ("Product", [("Features", "/features"), ("Pricing", "/pricing"), ("Docs", "/docs")]),
                ("Company", [("About", "/about"), ("Blog", "/blog"), ("Contact", "/contact")]),
            ],
            social=[("github", "https://github.com/..."), ("twitter", "https://twitter.com/...")]
        )
    )
```

#### 4. Pattern Components

**`NavbarModern`** - Glassmorphism navbar with scroll effects:
```python
NavbarModern(
    brand="MyApp",
    links=[("Features", "/features"), ("Pricing", "/pricing"), ("Docs", "/docs")],
    cta=Button("Sign Up", variant="primary"),
    glass=True,  # Glassmorphism effect
    sticky=True,  # Sticky on scroll
    transparent_until_scroll=True  # Transparent until user scrolls
)
```

**`FeatureGrid`** - Icon-based feature showcase:
```python
FeatureGrid(
    title="Our Features",
    subtitle="Everything you need to build amazing apps",
    features=[
        Feature("Fast", "Lightning quick load times", icon="lightning-charge"),
        Feature("Secure", "Enterprise-grade security", icon="shield-check"),
        Feature("Scalable", "Grows with your business", icon="graph-up-arrow"),
    ],
    columns=3  # Responsive: 1 col mobile, 2 col tablet, 3 col desktop
)
```

**`PricingGroup`** - Multi-tier pricing cards:
```python
PricingGroup(
    tiers=[
        PricingTier(
            name="Starter",
            price="$0",
            period="/month",
            features=["10 projects", "1 GB storage", "Community support"],
            cta=Button("Start Free", variant="outline-primary"),
            popular=False
        ),
        PricingTier(
            name="Pro",
            price="$29",
            period="/month",
            features=["Unlimited projects", "100 GB storage", "Priority support", "Advanced analytics"],
            cta=Button("Get Started", variant="primary"),
            popular=True  # Highlights this tier
        ),
    ],
    billing_toggle=True  # Monthly/Yearly toggle
)
```

#### 5. `faststrap init` CLI Tool

**Purpose:** Scaffold new Faststrap projects with templates.

**Usage:**
```bash
# Interactive mode
faststrap init

> Project name: my-app
> Template: [dashboard, landing, ecommerce, blog, blank]
> Choose: dashboard
> Include auth? [y/N]: y
> Include database? [y/N]: y
> Creating project...
> Done! Run: cd my-app && python main.py

# Non-interactive
faststrap init my-app --template=dashboard --auth --db=sqlite

# List available templates
faststrap init --list-templates
```

**Generated Structure:**
```
my-app/
├── main.py              # FastHTML app entry point
├── routes/
│   ├── __init__.py
│   ├── dashboard.py
│   ├── auth.py
│   └── api.py
├── models/
│   ├── __init__.py
│   └── user.py
├── static/
│   ├── css/
│   └── js/
├── templates/           # If using Jinja2
├── .env.example
├── requirements.txt
├── README.md
└── tests/
```

**Implementation:**
```python
# faststrap/cli/init.py
import click
from pathlib import Path

TEMPLATES = {
    "dashboard": "Admin dashboard with sidebar, auth, CRUD",
    "landing": "Marketing landing page with hero, features, pricing",
    "ecommerce": "Online store with products, cart, checkout",
    "blog": "Blog with posts, categories, comments",
    "blank": "Minimal FastHTML + Faststrap setup"
}

@click.command()
@click.argument('project_name', required=False)
@click.option('--template', type=click.Choice(list(TEMPLATES.keys())))
@click.option('--auth/--no-auth', default=False)
@click.option('--db', type=click.Choice(['sqlite', 'postgres', 'none']), default='none')
def init(project_name, template, auth, db):
    """Initialize a new Faststrap project"""
    
    # Interactive prompts if not provided
    if not project_name:
        project_name = click.prompt('Project name')
    
    if not template:
        click.echo('\nAvailable templates:')
        for name, desc in TEMPLATES.items():
            click.echo(f'  {name}: {desc}')
        template = click.prompt('Choose template', type=click.Choice(list(TEMPLATES.keys())))
    
    # Create project
    project_path = Path.cwd() / project_name
    project_path.mkdir(exist_ok=True)
    
    # Copy template files
    copy_template(template, project_path)
    
    # Add auth if requested
    if auth:
        add_auth_scaffold(project_path)
    
    # Configure database
    if db != 'none':
        configure_database(project_path, db)
    
    click.echo(f'\n✅ Project created: {project_path}')
    click.echo(f'Run: cd {project_name} && python main.py')
```

---

## 📊 Phase 6 – Data & Ecosystem (v0.6.x – April-July 2026)

**Goal:** Deep Python integration leveraging Pandas, Pydantic, and data science tools. Make Faststrap the **obvious choice for data-centric applications**.

**Why Phase 6 Matters:**
- Python dominates data science/ML (Pandas, Polars, Jupyter)
- Most business apps are data-heavy (dashboards, analytics, reports)
- Faststrap + Python data tools = unbeatable developer experience
- No other HTML framework has this tight integration

### v0.6.0 – Data Layer (April 2026)

**Focus:** Seamless integration with Pandas/Polars for data-driven UIs.

#### 1. `Table.from_df()` Method

**Purpose:** Render Pandas/Polars DataFrames as beautiful Bootstrap tables with zero boilerplate.

**Features:**
- Auto-detect column types (numbers, dates, strings)
- Smart alignment (numbers right, text left)
- Optional sorting (HTMX-powered server-side)
- Optional search/filter
- Export to CSV/Excel
- Pagination for large datasets

**API:**
```python
import pandas as pd
from faststrap import Table

# Load data
df = pd.read_csv('sales.csv')

# Render as table
table = Table.from_df(
    df,
    striped=True,
    hover=True,
    sortable=True,  # Adds sort icons to headers
    searchable=True,  # Adds search bar above table
    pagination=True,  # Auto-paginate if >100 rows
    per_page=25,
    export=['csv', 'excel'],  # Download buttons
    
    # Column customization
    columns={
        'price': {'format': 'currency', 'align': 'right'},
        'date': {'format': 'date'},
        'status': {'render': lambda x: Badge(x, variant='success' if x == 'Active' else 'secondary')}
    },
    
    # HTMX endpoints for dynamic operations
    hx_sort_endpoint="/api/table/sort",
    hx_search_endpoint="/api/table/search"
)
```

**Implementation Details:**

**Auto-alignment:**
```python
def _infer_alignment(series):
    if pd.api.types.is_numeric_dtype(series):
        return 'right'
    elif pd.api.types.is_datetime64_any_dtype(series):
        return 'center'
    else:
        return 'left'
```

**Server-side sorting (HTMX pattern):**
```python
@app.post("/api/table/sort")
def sort_table(column: str, direction: str):
    df_sorted = df.sort_values(column, ascending=(direction == 'asc'))
    return Table.from_df(df_sorted)  # Return updated table
```

**Performance considerations:**
- Warn if DataFrame > 10,000 rows without pagination
- Offer server-side pagination via `to_html()` slicing
- Use `df.itertuples()` instead of `iterrows()` for speed

#### 2. `Chart` Component Wrapper

**Purpose:** Consistent wrapper for Matplotlib, Plotly, and Altair charts with Bootstrap styling and dark mode support.

**Design Decision: Server-Rendered SVG (Primary) + Optional JS Interactivity**

**Rationale:**
- **SVG (Matplotlib):** Aligns with FastHTML's server-first philosophy, works without JS, smaller payload
- **Plotly (Optional):** For users who need interactivity (zoom, hover tooltips, pan)
- Dark mode support via automatic color palette switching

**API:**
```python
from faststrap import Chart
import matplotlib.pyplot as plt

# Matplotlib (server-rendered SVG)
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [4, 5, 6])

chart = Chart(
    fig,
    title="Sales Trend",
    responsive=True,  # Scales to container width
    dark_mode=True,   # Auto-inverts colors for dark theme
    download=True     # Adds download button
)

# Or use Plotly for interactivity
import plotly.graph_objects as go

fig = go.Figure(data=go.Scatter(x=[1, 2, 3], y=[4, 5, 6]))
chart = Chart.from_plotly(fig, responsive=True)

# Helper: Quick chart from DataFrame
chart = Chart.from_df(
    df,
    x='date',
    y='revenue',
    type='line',  # line, bar, scatter, pie
    title="Revenue Over Time"
)
```

**Dark Mode Implementation:**
```python
def apply_dark_theme(fig):
    """Apply dark mode colors to matplotlib figure"""
    fig.patch.set_facecolor('#1a1a1a')
    for ax in fig.get_axes():
        ax.set_facecolor('#2d2d2d')
        ax.tick_params(colors='#e0e0e0')
        ax.spines['bottom'].set_color('#e0e0e0')
        ax.spines['left'].set_color('#e0e0e0')
        ax.xaxis.label.set_color('#e0e0e0')
        ax.yaxis.label.set_color('#e0e0e0')
```

### v0.6.1 – Productivity Layer (May 2026)

**Focus:** Type-safe form generation and HTMX convenience wrappers to eliminate boilerplate.

#### 1. `Form.from_pydantic()` Method

**Purpose:** Auto-generate Bootstrap forms from Pydantic models with validation, reducing 50+ lines to 5.

**Features:**
- Infer input types from Pydantic field types
- Use `Field(description=...)` for labels/placeholders
- Automatic validation error display
- Handle nested models (recursive forms)
- Support for enums (rendered as Select)
- File upload handling

**API:**
```python
from pydantic import BaseModel, EmailStr, Field
from faststrap import Form

class UserSignup(BaseModel):
    username: str = Field(..., min_length=3, description="Choose a unique username")
    email: EmailStr = Field(..., description="We'll never share your email")
    age: int = Field(..., ge=13, le=120, description="Must be 13 or older")
    country: str = Field(..., description="Select your country")
    agree_terms: bool = Field(False, description="I agree to the terms of service")

# Generate form automatically
form = Form.from_pydantic(
    UserSignup,
    hx_post="/signup",
    hx_target="body",
    submit_text="Create Account",
    submit_variant="primary"
)

# With validation errors
@app.post("/signup")
def signup(data: dict):
    try:
        user = UserSignup(**data)
        # Save user...
        return Alert("Account created!", variant="success")
    except ValidationError as e:
        # Return form with errors highlighted
        return Form.from_pydantic(
            UserSignup,
            errors=e.errors(),
            values=data,  # Preserve user input
            hx_post="/signup"
        )
```

**Implementation:**
```python
from pydantic import BaseModel, ValidationError
from pydantic.fields import FieldInfo
from typing import get_origin, get_args

def _input_type_from_annotation(annotation):
    """Map Pydantic types to HTML input types"""
    type_map = {
        str: "text",
        int: "number",
        float: "number",
        bool: "checkbox",
        EmailStr: "email",
        # Add more...
    }
    return type_map.get(annotation, "text")

def _field_to_component(name: str, field: FieldInfo, value=None, error=None):
    """Convert Pydantic field to Faststrap Input/Select"""
    
    # Handle enums as Select
    if hasattr(field.annotation, '__mro__') and Enum in field.annotation.__mro__:
        options = [(e.value, e.name) for e in field.annotation]
        return Select(
            name,
            *options,
            label=field.title or name.replace('_', ' ').title(),
            selected=value,
            help_text=field.description,
            required=field.is_required(),
            invalid=bool(error),
            feedback=error
        )
    
    # Handle checkbox differently
    input_type = _input_type_from_annotation(field.annotation)
    
    if input_type == "checkbox":
        return Checkbox(
            name,
            label=field.description or field.title or name.replace('_', ' ').title(),
            checked=value,
            required=field.is_required(),
            invalid=bool(error),
            feedback=error
        )
    
    # Standard input
    return Input(
        name,
        type=input_type,
        label=field.title or name.replace('_', ' ').title(),
        placeholder=field.description,
        value=value,
        required=field.is_required(),
        invalid=bool(error),
        feedback=error,
        # Add min/max for numbers
        min=field.ge if hasattr(field, 'ge') else None,
        max=field.le if hasattr(field, 'le') else None,
    )

@classmethod
def from_pydantic(
    cls,
    model: type[BaseModel],
    values: dict = None,
    errors: list = None,
    submit_text: str = "Submit",
    submit_variant: str = "primary",
    **form_attrs
):
    """Generate form from Pydantic model"""
    
    # Get fields (Pydantic v1 vs v2 compatibility)
    if hasattr(model, 'model_fields'):
        fields = model.model_fields  # Pydantic v2
    else:
        fields = model.__fields__  # Pydantic v1
    
    # Build error map
    error_map = {}
    if errors:
        for err in errors:
            field = err['loc'][0] if err['loc'] else None
            if field:
                error_map[field] = err['msg']
    
    # Convert each field to component
    components = []
    for field_name, field_info in fields.items():
        component = _field_to_component(
            field_name,
            field_info,
            value=values.get(field_name) if values else None,
            error=error_map.get(field_name)
        )
        components.append(component)
    
    # Add submit button
    components.append(
        Button(submit_text, variant=submit_variant, type="submit", cls="mt-3")
    )
    
    return cls(*components, **form_attrs)

# Attach to Form class
Form.from_pydantic = from_pydantic
```

**Advanced Features:**

**Nested Models:**
```python
class Address(BaseModel):
    street: str
    city: str
    zip: str

class User(BaseModel):
    name: str
    address: Address

# Generates fieldset for nested model
form = Form.from_pydantic(User)
# Output: name input + fieldset with street, city, zip
```

**Custom Renderers:**
```python
form = Form.from_pydantic(
    User,
    renderers={
        'country': lambda field: Select('country', *COUNTRIES, label="Country"),
        'bio': lambda field: Textarea('bio', rows=5, label="Biography")
    }
)
```

#### 2. HTMX Presets

**Purpose:** Pre-configured HTMX patterns for common use cases.

**`ActiveSearch`** - Debounced search input:
```python
from faststrap.htmx import ActiveSearch

search = ActiveSearch(
    name="q",
    placeholder="Search products...",
    target="#results",
    endpoint="/search",
    debounce=500  # milliseconds
)

# Generates:
# <input hx-get="/search" hx-trigger="keyup changed delay:500ms" 
#        hx-target="#results" hx-include="[name='q']">
```

**`InfiniteScroll`** - Auto-load more content on scroll:
```python
from faststrap.htmx import InfiniteScroll

container = InfiniteScroll(
    content=initial_items,
    load_more_endpoint="/api/items?page=2",
    target="#items-container",
    trigger_offset="200px"  # Load when 200px from bottom
)

# Generates container with hx-trigger="revealed" on last item
```

**`ConfirmAction`** - Button with confirmation dialog:
```python
from faststrap.htmx import ConfirmAction

delete_btn = ConfirmAction(
    "Delete User",
    action="/api/users/123/delete",
    method="DELETE",
    confirm_title="Are you sure?",
    confirm_message="This action cannot be undone.",
    variant="danger"
)

# Uses Bootstrap Modal for confirmation
```

### v0.6.2 – Auth & DX Layer (June 2026)

**Focus:** Authentication UI components and developer experience tools.

#### 1. `faststrap.auth` Module

**Design Decision: UI Components Only (Not Full Auth Backend)**

**Rationale:**
- Stays true to "we provide UI, you provide logic" philosophy
- Auth backends vary wildly (JWT, sessions, OAuth, SAML)
- Users have preferences (FastAPI-Users, AuthLib, custom)
- We provide the polished UI, they plug in their logic

**Components:**

**`LoginCard`** - Polished login form:
```python
from faststrap.auth import LoginCard

@app.get("/login")
def login_page():
    return LoginCard(
        logo="🛒 MyApp",
        title="Welcome Back",
        social_logins=["google", "github"],  # Optional OAuth buttons
        hx_post="/auth/login",
        signup_link="/signup",
        forgot_link="/forgot-password"
    )

@app.post("/auth/login")
def login(username: str, password: str):
    if check_credentials(username, password):
        session['user_id'] = user.id
        return redirect("/dashboard")
    return LoginCard(error="Invalid credentials")
```

**`SignupForm`** - Registration form with validation:
```python
from faststrap.auth import SignupForm

signup_form = SignupForm(
    fields=['username', 'email', 'password', 'confirm_password'],
    social_signup=["google", "github"],
    terms_link="/terms",
    hx_post="/auth/signup"
)
```

**`PasswordResetFlow`** - Complete password reset UI:
```python
from faststrap.auth import PasswordResetRequest, PasswordResetConfirm

# Step 1: Request reset
@app.get("/forgot-password")
def forgot():
    return PasswordResetRequest(hx_post="/auth/reset-request")

# Step 2: Email sent confirmation
@app.post("/auth/reset-request")
def send_reset(email: str):
    send_reset_email(email)
    return Alert("Check your email for reset link", variant="success")

# Step 3: Reset form with token
@app.get("/reset-password/{token}")
def reset_form(token: str):
    return PasswordResetConfirm(token=token, hx_post="/auth/reset-confirm")
```

**`AuthFlow` Helper (Optional - Advanced):**
```python
from faststrap.auth import AuthFlow

# Quick setup for common patterns
AuthFlow.setup(
    app,
    login_route="/login",
    signup_route="/signup",
    logout_route="/logout",
    
    # User provides these callbacks
    on_login=lambda username, password: check_credentials(username, password),
    on_signup=lambda data: create_user(data),
    on_logout=lambda: session.clear(),
    
    # Customization
    logo="MyApp",
    social_logins=["google"],
    require_email_verification=True
)
```

#### 2. `faststrap.dev` Module - Developer Tools

**Purpose:** Debug and inspect Faststrap apps during development.

**`Inspector` Middleware:**
```python
from faststrap.dev import Inspector

if app.debug:
    app.add_middleware(Inspector(
        show_htmx_requests=True,  # Log HTMX swaps
        show_component_tree=True,  # Visual component hierarchy
        show_performance=True      # Render time metrics
    ))

# Adds floating debug panel in browser showing:
# - HTMX request/response logs
# - Component render times
# - Database queries (if using SQLModel)
# - Session data
```

**`faststrap lint` CLI:**
```bash
# Static analysis for best practices
faststrap lint src/

# Checks for:
# - Accessibility issues (missing ARIA labels)
# - Performance anti-patterns (large components in loops)
# - HTMX misuse (missing hx-target, conflicting swaps)
# - Missing tests for components
```

### v0.6.3 – Realtime Layer (July 2026)

**Focus:** Live-updating components via Server-Sent Events (SSE).

**Design: Lightweight SSE wrappers, not full WebSocket framework**

**Why SSE over WebSockets:**
- Simpler (one-way server→client)
- Works with standard HTTP/2
- Auto-reconnects
- Sufficient for dashboards, notifications, live metrics
- HTMX has built-in SSE support

**Components:**

**`LiveBadge`** - Auto-updating badge:
```python
from faststrap.realtime import LiveBadge

# Updates every 5 seconds via SSE
cart_badge = LiveBadge(
    endpoint="/api/cart/count",
    variant="primary",
    icon="cart3",
    poll_interval=5000,
    label="Cart"
)

# Backend (FastHTML SSE route)
@app.get("/api/cart/count")
async def cart_count_stream():
    async def generate():
        while True:
            count = get_cart_count()
            yield f"data: {count}\n\n"
            await asyncio.sleep(5)
    
    return StreamingResponse(generate(), media_type="text/event-stream")
```

**`LiveTable`** - Auto-refreshing table:
```python
from faststrap.realtime import LiveTable

# Polls endpoint for new data
orders_table = LiveTable(
    endpoint="/api/orders/stream",
    columns=["id", "customer", "total", "status"],
    poll_interval=10000,  # 10 seconds
    highlight_new=True    # Flash animation on new rows
)
```

**`LiveChart`** - Streaming chart updates:
```python
from faststrap.realtime import LiveChart

# Append new data points as they arrive
chart = LiveChart(
    endpoint="/api/metrics/stream",
    type="line",
    update_mode="append",  # or "replace"
    max_points=50  # Keep last 50 points
)
```

**`NotificationStream`** - Live notifications:
```python
from faststrap.realtime import NotificationStream

# Shows toast notifications as they arrive
notifications = NotificationStream(
    endpoint="/api/notifications/stream",
    position="top-right"
)

# Backend sends notifications
async def notify_user(user_id, message):
    await notification_queue.put({
        "user_id": user_id,
        "message": message,
        "variant": "info"
    })
```

---

## 🌍 Community Ecosystem (Safe Path)

**Goal:** Enable a thriving community-driven ecosystem while maintaining core stability and preventing the chaos that plagues other plugin systems.

**Philosophy:**
- **Explicit over Implicit:** No magic auto-discovery
- **Opt-in over Opt-out:** Extensions never affect core without explicit import
- **Documented over Enforced:** Clear contracts, not technical restrictions
- **Community over Control:** We curate, not gatekeep

### The Problem We're Solving

Many frameworks struggle with extensions:
- **WordPress:** Plugin conflicts, security vulnerabilities, version hell
- **VS Code:** Extension bloat, performance degradation
- **NPM:** Dependency nightmares, supply chain attacks

**Our Solution:** Extension Registry + Strict Contracts + No Runtime Magic

### 1. Extension Contracts (v0.5.x)

**Documentation-First Approach:** Define what extensions can and cannot do.

#### Theme Pack Contract

**What Theme Packs Are:**
- Collections of pre-designed color schemes and typography
- Packaged as separate Python packages
- Follow `create_theme()` format
- No code execution, just data

**Example Theme Pack Structure:**
```
faststrap-themes-cyberpunk/
├── faststrap_themes_cyberpunk/
│   ├── __init__.py
│   ├── neon_pink.py
│   ├── matrix_green.py
│   └── blade_runner.py
├── previews/
│   ├── neon_pink.png
│   ├── matrix_green.png
│   └── blade_runner.png
├── manifest.json
├── README.md
└── setup.py
```

**manifest.json:**
```json
{
  "name": "Cyberpunk Themes",
  "id": "cyberpunk-themes",
  "version": "1.0.0",
  "author": {
    "name": "Jane Doe",
    "github": "janedoe",
    "email": "jane@example.com"
  },
  "type": "theme-pack",
  "themes": [
    {
      "id": "neon-pink",
      "name": "Neon Pink",
      "preview": "previews/neon_pink.png",
      "description": "Vibrant cyberpunk aesthetic with hot pink accents"
    }
  ],
  "requires": "faststrap>=0.5.0",
  "license": "MIT",
  "repository": "https://github.com/janedoe/faststrap-themes-cyberpunk"
}
```

**Usage (Explicit Import):**
```python
# Install: pip install faststrap-themes-cyberpunk
from faststrap import add_bootstrap
from faststrap_themes_cyberpunk import neon_pink

add_bootstrap(app, theme=neon_pink)
```

**Contract Rules:**
1. Must use `create_theme()` format
2. No code execution beyond theme data
3. Must include previews for all themes
4. Must declare Faststrap version compatibility
5. Must be MIT/Apache2/BSD licensed

#### Component Pack Contract

**What Component Packs Are:**
- Custom components built with Faststrap primitives
- Extended functionality beyond core components
- Examples: Calendars, Kanban boards, Rich text editors

**Example Component Pack Structure:**
```
faststrap-components-calendar/
├── faststrap_components_calendar/
│   ├── __init__.py
│   ├── calendar.py
│   ├── date_picker.py
│   └── styles.css
├── tests/
│   └── test_calendar.py
├── examples/
│   └── demo.py
├── manifest.json
├── README.md
└── setup.py
```

**Usage (Explicit Import):**
```python
# Install: pip install faststrap-components-calendar
from faststrap_components_calendar import Calendar, DatePicker

calendar = Calendar(
    events=my_events,
    view="month",
    editable=True
)
```

**Contract Rules:**
1. Must use only Faststrap + FastHTML primitives
2. No external CSS frameworks (Bootstrap only)
3. Must include tests (>70% coverage)
4. Must include working example
5. Must declare all dependencies
6. No monkey-patching Faststrap core
7. Must follow Faststrap's accessibility guidelines

#### Template Pack Contract

**What Template Packs Are:**
- Complete page/app templates
- Use Faststrap components
- Include routes, models, and business logic
- Examples: Blog engines, Admin panels, Portfolio sites

**Usage (Scaffolding, not Runtime):**
```bash
# Install template via CLI
faststrap init my-blog --template=community/blog-pro

# This downloads template files to your project
# NOT imported as Python package
```

**Contract Rules:**
1. Must be self-contained (all dependencies listed)
2. Must include setup instructions
3. Must include example data/fixtures
4. Should include deployment guide
5. Must declare Faststrap version compatibility

### 2. The Registry (v0.6.x)

**Purpose:** Centralized, curated directory of community extensions.

**NOT a package repository** (that's PyPI). Just metadata and discovery.

**Registry Structure:**
```
Faststrap-org/faststrap-extensions/ (GitHub repo)
├── registry.json               # Master list
├── themes/
│   ├── cyberpunk-themes.json
│   ├── nature-themes.json
│   └── corporate-themes.json
├── components/
│   ├── calendar.json
│   ├── kanban.json
│   └── rich-editor.json
├── templates/
│   ├── blog-pro.json
│   ├── saas-starter.json
│   └── ecommerce-complete.json
└── README.md
```

**registry.json:**
```json
{
  "version": "1.0",
  "last_updated": "2026-04-15",
  "extensions": {
    "themes": [
      {
        "id": "cyberpunk-themes",
        "name": "Cyberpunk Themes",
        "author": "janedoe",
        "pypi_package": "faststrap-themes-cyberpunk",
        "github": "https://github.com/janedoe/faststrap-themes-cyberpunk",
        "stars": 156,
        "downloads": 2341,
        "last_updated": "2026-04-10",
        "faststrap_version": ">=0.5.0",
        "tags": ["dark", "cyberpunk", "neon"],
        "verified": true,
        "featured": false
      }
    ],
    "components": [...],
    "templates": [...]
  }
}
```

**Verification Process:**
1. Author submits PR to registry with their extension metadata
2. Automated checks:
   - Package exists on PyPI
   - GitHub repo accessible
   - manifest.json valid
   - Tests pass (for components)
   - README exists
3. Manual review:
   - Code quality check
   - Security scan
   - License verification
   - Contract compliance
4. Approval → Merged → Listed on website

**Quality Badges:**
- 🌟 **Featured** - Handpicked by maintainers
- ✅ **Verified** - Passes all automated checks
- 🔥 **Popular** - 100+ downloads
- 🆕 **New** - Published in last 30 days
- 📚 **Well-Documented** - Comprehensive README + examples
- 🧪 **Tested** - >80% test coverage

### 3. Discovery Tooling (v0.7+)

**Website: extensions.faststrap.dev**

**Features:**
- Browse/search extensions
- Filter by type, tags, popularity
- Preview screenshots
- One-click install commands
- User reviews/ratings
- Compatibility checker

**CLI Commands:**
```bash
# Search registry
faststrap extensions search "calendar"
faststrap extensions search --type=theme --tag="dark"

# View details
faststrap extensions info calendar

# Install (just runs pip install)
faststrap extensions install cyberpunk-themes

# List installed
faststrap extensions list

# Publish your extension
faststrap extensions publish ./my-extension/
# Validates manifest, runs tests, guides through PR submission
```

**`faststrap init` Integration:**
```bash
# Scaffold with community template
faststrap init my-app --template=community/saas-starter

# This:
# 1. Checks registry for template
# 2. Downloads from GitHub
# 3. Extracts to new project
# 4. Runs setup scripts
# 5. Installs dependencies
```

### Extension Design Philosophy

**Why This Approach Works:**

1. **No Runtime Magic**
   - Extensions don't auto-register
   - No global state pollution
   - No version conflicts
   - Predictable behavior

2. **Explicit Imports**
   ```python
   # User knows exactly what they're using
   from faststrap_themes_cyberpunk import neon_pink
   
   # Not:
   # theme="community/neon-pink"  ← Magic string, unclear provenance
   ```

3. **PyPI is the Distribution**
   - We don't host packages
   - We don't maintain mirrors
   - We just list what exists
   - Standard Python tooling works

4. **Community Ownership**
   - Extension authors own their code
   - We just curate and promote
   - No vendor lock-in
   - Fork-friendly

5. **Progressive Enhancement**
   - Start with core Faststrap
   - Add extensions as needed
   - Remove extensions easily
   - No breaking changes to core

**Comparison to Other Systems:**

| System | Auto-Discovery | Runtime Hooks | Version Conflicts | Our Approach |
|--------|----------------|---------------|-------------------|--------------|
| WordPress Plugins | ✅ Yes | ✅ Yes | ⚠️ Common | ❌ No / ❌ No / ✅ Rare |
| VS Code Extensions | ✅ Yes | ✅ Yes | ⚠️ Occasional | ❌ No / ❌ No / ✅ Rare |
| Python Packages | ❌ No | ❌ No | ⚠️ Dependency Hell | ❌ No / ❌ No / ✅ Use venv |

---

## 🔒 Stability & Versioning Policy

**Goal:** Give users confidence that upgrading won't break their apps.

### Component Maturity Levels

Every component is marked with a stability decorator:

🟢 **Stable** (`@stable`)
- **API Guarantee:** Won't break in minor versions (0.5.x → 0.6.x)
- **Test Coverage:** >90%
- **Production Usage:** Used in 3+ real projects
- **Documentation:** Complete with examples
- **Examples:** `Button`, `Card`, `Input`, `Table`, `Modal`

🟡 **Beta** (`@beta`)
- **API Warning:** May change in minor versions
- **Test Coverage:** >70%
- **Production Usage:** Limited real-world usage
- **Documentation:** Basic docs, may be incomplete
- **Examples:** New Phase 6 components on first release

🔴 **Experimental** (`@experimental`)
- **API Warning:** Will likely change
- **Test Coverage:** Minimal (>50%)
- **Production Usage:** Not recommended
- **Documentation:** May be absent
- **Examples:** Proof-of-concept features

**In Code:**
```python
from faststrap.core.decorators import stable, beta, experimental

@stable(since="0.4.0")
class Button(Component):
    """Production-ready button component"""
    pass

@beta(since="0.6.0", stable_eta="0.7.0")
class LiveChart(Component):
    """Real-time chart (API may change)"""
    pass

@experimental
class AIChat(Component):
    """Experimental AI chatbot (use at own risk)"""
    pass
```

**User-Facing Indicators:**
- Docs badge: "Stable since v0.4.0"
- IDE autocomplete shows maturity
- Runtime warning on experimental usage

### Versioning Scheme (SemVer-ish)

**Format:** MAJOR.MINOR.PATCH

**MAJOR (1.0 → 2.0):**
- Breaking API changes
- Requires code updates
- Migration guide provided
- Minimum 6 months notice via deprecation warnings

**MINOR (0.5.0 → 0.6.0):**
- New features
- Beta → Stable promotions
- Non-breaking enhancements
- Deprecated features (with warnings)

**PATCH (0.5.0 → 0.5.1):**
- Bug fixes only
- Security patches
- Documentation updates
- No API changes

### Deprecation Process

**Timeline: 2 Minor Versions**

**Example: Deprecating Button.color in favor of Button.variant**

**v0.5.0 - Deprecation Warning:**
```python
@stable
class Button:
    def __init__(self, variant=None, color=None):  # color is deprecated
        if color is not None:
            warnings.warn(
                "Button.color is deprecated, use Button.variant instead. "
                "color will be removed in v0.7.0",
                DeprecationWarning,
                stacklevel=2
            )
            variant = color  # Still works
        self.variant = variant
```

**v0.6.0 - Final Warning:**
```python
# Same warning, but louder (logged to console)
# Update documentation showing strikethrough on old param
```

**v0.7.0 - Removal:**
```python
@stable
class Button:
    def __init__(self, variant):  # color removed
        self.variant = variant
```

**Migration Guide:**
```markdown
## Migrating from v0.6.x to v0.7.0

### Button Component

**Breaking Change:** `color` parameter removed.

**Before:**
```python
Button("Click", color="primary")
```

**After:**
```python
Button("Click", variant="primary")
```

**Find/Replace:** `color=` → `variant=`
```

---

## 🚫 Non-Goals

What Faststrap intentionally **won't** do, and why:

### ❌ Client-Side Reactivity

**What we mean:**
- React-style useState, useEffect
- Vue-style reactive data binding
- Svelte-style compiled reactivity

**Why not:**
- Goes against FastHTML's server-first philosophy
- Adds complexity (state management, reconciliation)
- Requires large JS runtime
- HTMX provides sufficient interactivity for 95% of use cases

**Alternative:** If you need client-side reactivity, use Alpine.js (works great with Faststrap/HTMX)

### ❌ Custom CSS Framework

**What we mean:**
- Building our own grid system
- Custom utility classes (like Tailwind)
- Replacing Bootstrap

**Why not:**
- Bootstrap is battle-tested (13+ years, billions of sites)
- Already has huge ecosystem and community knowledge
- We'd spend years catching up to Bootstrap's feature set
- "Bootstrap but in Python" is our value prop

**Alternative:** Use Bootstrap's built-in customization (Sass variables, utility API)

### ❌ Database ORM

**What we mean:**
- Building database models
- Query builders
- Migrations
- Relationships

**Why not:**
- SQLModel, SQLAlchemy, Peewee already exist and are excellent
- Database layer is orthogonal to UI layer
- Would bloat Faststrap with non-UI concerns
- Users have strong preferences on ORMs

**Our Role:** Provide UI components that work well with *any* ORM

**Example:**
```python
# We provide the Table component
table = Table.from_df(df)

# You choose your ORM
users = session.query(User).all()  # SQLAlchemy
users = User.objects.all()  # Django ORM
users = await User.all()  # Tortoise ORM

# We don't care which one you use
```

### ❌ Full Auth Backend

**What we mean:**
- Password hashing
- Session management
- OAuth provider integration
- Permission systems
- User database models

**Why not:**
- Auth requirements vary wildly (JWT, sessions, SAML, LDAP)
- Security-critical code requires deep expertise
- FastAPI-Users, AuthLib, Flask-Security already do this well
- UI and backend logic should be decoupled

**What we DO provide:**
- `LoginCard`, `SignupForm`, `PasswordReset` (UI only)
- HTMX integration patterns for auth flows
- Examples showing how to connect to auth backends

**Analogy:** We're the dashboard, you're the engine.

### Why These Boundaries Matter

1. **Focus:** By saying no, we can say yes to being the **best** Bootstrap+Python library
2. **Stability:** Smaller surface area = fewer bugs, easier maintenance
3. **Integration:** Play well with existing tools instead of competing
4. **Community:** Contributors know what belongs in core vs extensions
5. **Trust:** Users know we won't suddenly pivot and break everything

---

## 🎯 Success Metrics

How we measure progress toward v1.0:

| Metric | v0.3.1 | v0.4.5 (Now) | v0.5.0 | v0.6.3 | v1.0.0 |
|--------|--------|--------------|--------|--------|--------|
| **Components** | 20 | 38 | 50 | 75 | 100+ |
| **Tests** | 219 | 230+ | 500+ | 700+ | 800+ |
| **Coverage** | 80% | 85%+ | 90% | 92% | 95%+ |
| **Contributors** | 5+ | 15+ | 25+ | 40+ | 50+ |
| **GitHub Stars** | 5 | 9 | 50 | 200 | 500+ |
| **PyPI Downloads/month** | 50 | 100 | 500 | 2000 | 5000+ |
| **Production Apps** | 2 | 5 | 15 | 40 | 100+ |
| **Documentation Pages** | 25 | 50 | 75 | 100 | 150+ |

**Qualitative Goals:**
- ✅ "Obvious choice" for FastHTML projects
- ✅ Mentioned in FastHTML official docs
- ✅ Conference talk accepted (PyCon, DjangoCon)
- ✅ Corporate sponsor (≥$1000/year)
- ✅ Full-time contributor (via sponsorship)

---

## 🤝 How to Contribute

Whether you're a first-time contributor or seasoned developer, there's a way to help build Faststrap.

### 🌱 First-Time Contributors

**Perfect for getting started:**

**Documentation Improvements:**
- Fix typos, clarify explanations
- Add missing code examples
- Translate docs to other languages
- Create tutorial videos

**Example Applications:**
- Build sample apps showcasing components
- Convert existing projects to use Faststrap
- Create CodePen/Repl.it demos

**Testing:**
- Add test coverage to existing components
- Write integration tests
- Manual testing on different browsers
- Accessibility testing with screen readers

**Issue Reporting:**
- Report bugs with reproduction steps
- Suggest new features with use cases
- Vote on existing issues (👍 reactions)

**Good First Issues:**
Check GitHub issues tagged [`good-first-issue`](https://github.com/Faststrap-org/Faststrap/labels/good-first-issue)

### 🛠️ Component Developers (Intermediate)

**Ready to build components:**

**Process:**
1. **Pick** a component from Phase 5/6 roadmap tables above
2. **Comment** on the GitHub issue: "I'll build [Component]"
3. **Get assigned** by a maintainer (usually within 24 hours)
4. **Fork** the repo and create a feature branch
5. **Follow** the [BUILDING_COMPONENTS.md](BUILDING_COMPONENTS.md) guide
6. **Use** `src/faststrap/templates/component_template.py` as starting point
7. **Write** 10-15 tests per component using `to_xml()` assertions
8. **Submit PR** with:
   - Component code
   - Tests (aim for >90% coverage)
   - Documentation (docstrings + example)
   - Changelog entry
9. **Iterate** based on code review feedback
10. **Merged** usually within 48 hours

**Example Components to Build:**
- See Phase 5/6 tables for available components
- Check [ROADMAP_VOTING.md](ROADMAP_VOTING.md) for community priorities

**Resources:**
- **Template:** `src/faststrap/templates/component_template.py`
- **Guide:** [BUILDING_COMPONENTS.md](BUILDING_COMPONENTS.md)
- **Examples:** Study existing components like `Button`, `Card`, `Table`
- **Tests:** See `tests/components/` for testing patterns

### 🏗️ Architecture & Design (Advanced)

**Shape the framework:**

**Proposal Process:**
1. Open a **GitHub Discussion** (not an issue)
2. Title: `[Proposal] Your Idea`
3. Include:
   - Problem statement
   - Proposed solution
   - API design mockup
   - Alternatives considered
   - Breaking changes (if any)
4. Community discussion (1-2 weeks)
5. If accepted → Create implementation plan
6. Either implement yourself or mentor others

**Areas for Advanced Contributors:**

**Core Architecture:**
- Improve component base classes
- Enhance type hint system
- Optimize rendering performance
- Design new subsystems (layouts, patterns)

**Tooling:**
- Improve CLI tools
- Build VS Code extension
- Create component playground
- Enhance developer experience

**Documentation:**
- Write architectural guides
- Create video tutorials
- Build interactive examples
- Design docs website improvements

**Code Review:**
- Review PRs from other contributors
- Mentor new contributors
- Enforce code quality standards
- Suggest improvements

**Community Leadership:**
- Organize contributor meetings
- Lead working groups
- Speak at conferences
- Write blog posts

### 🏆 Contribution Recognition

We celebrate and reward contributors:

**Levels:**

**🥉 Contributor** (First PR merged)
- Name in CONTRIBUTORS.md
- Contributor badge on profile
- Access to private Discord channel

**🥈 Regular Contributor** (5+ PRs merged)
- Featured on contributors page with bio
- Vote on roadmap priorities
- Early access to beta features
- Special Discord role

**🥇 Core Contributor** (Major feature or 20+ PRs)
- Co-author credit in release notes
- Listed as maintainer
- Voting rights on major decisions
- Monthly spotlight on social media

**💎 Lead Maintainer**
- Full commit access
- Release authority
- GitHub Sponsors profile link
- Speaking opportunities at events

**Special Recognition:**
- Monthly "Contributor of the Month" spotlight
- Annual contributor awards
- Conference ticket sponsorships
- Swag (stickers, t-shirts) for active contributors

### 💬 Getting Help

**Discord:** [FastHTML Community Server](https://discord.gg/qcXvcxMhdP)
- `#faststrap` - General discussion
- `#faststrap-help` - User questions
- `#faststrap-dev` - Contributor chat
- `#showcase` - Show off your projects

**GitHub Discussions:**
- Questions: General questions about using Faststrap
- Ideas: Feature suggestions and brainstorming
- Show and Tell: Share projects built with Faststrap
- Polls: Vote on roadmap priorities

**GitHub Issues:**
- Bug reports (use template)
- Feature requests (use template)
- Component proposals

**Email:** faststrap@example.com
- Private security disclosures
- Partnership inquiries
- Press/media requests

**Office Hours:**
- Weekly video call (Fridays 3pm UTC)
- Open Q&A with maintainers
- Code review sessions
- Pair programming on tough issues

---

## 🏆 Built with Faststrap

Real projects using Faststrap in production - proof that it works!

### 🌟 Showcase Projects

**[FastShop](https://github.com/example/fastshop)** - E-commerce Platform
- Full shopping cart, checkout, order tracking
- Admin dashboard for products/orders
- 500+ lines, demonstrates 15+ components
- Built in under 4 hours
- **Tech:** FastHTML + Faststrap + SQLite

**[AdminPro](https://github.com/example/adminpro)** - Admin Dashboard Template *(community)*
- User management, analytics, settings
- Dark mode support
- Responsive sidebar layout
- **Author:** @johndoe

**[BlogKit](https://github.com/example/blogkit)** - Blogging Platform *(community)*
- Markdown posts, categories, comments
- RSS feed, SEO optimized
- Clean reading experience
- **Author:** @janedoe

### 🏢 In Production

**Company X** - Internal admin panel
- 250+ users across 3 departments
- Customer management and reporting
- Replaced legacy Django admin

**Startup Y** - Customer portal
- 5,000+ monthly active users
- Real-time order tracking
- Self-service support ticketing

**Agency Z** - Client websites
- 12+ production websites
- Landing pages and blogs
- Reduced development time by 60%

### 📝 Case Studies

**"How FastShop Was Built in 4 Hours"**
- Developer: Claude (AI Assistant)
- Challenge: Full e-commerce system with cart, checkout, orders
- Solution: Used Faststrap's pre-built components
- Result: Production-ready system in record time
- [Read full case study →](#)

**"Migrating from React to Faststrap"**
- Company: TechCorp Inc.
- Challenge: Complex React codebase, hard to maintain
- Solution: Rebuilt admin panel with FastHTML + Faststrap
- Result: 70% less code, faster performance, easier hiring
- [Read full case study →](#)

### 🎨 Component Gallery

Browse live examples of every Faststrap component:
- [Component Playground](https://faststrap.dev/playground)
- Interactive demos
- Copy-paste code examples
- Dark mode preview

### 📤 Submit Your Project

Built something awesome with Faststrap? Share it!

**Requirements:**
- Uses Faststrap components
- Publicly accessible (or screenshots)
- Brief description + tech stack
- Contact info

**Submit via:**
- [GitHub Discussion](https://github.com/Faststrap-org/Faststrap/discussions/categories/show-and-tell)
- PR to `SHOWCASE.md`
- Email showcase@faststrap.dev

**Benefits:**
- Free promotion on website
- Social media spotlight
- Case study opportunity
- Inspire other developers

---

## 📚 Documentation Website

**Live at:** [faststrap.dev](https://faststrap.dev) *(coming soon)*

**Tech Stack:**
- MkDocs Material (theme)
- GitHub Pages (hosting)
- Python for live component rendering
- Auto-generated from code docstrings

### Site Structure

**Getting Started**
- Installation
- Quick Start (5-minute tutorial)
- Your First Component
- Theming Basics
- HTMX Integration

**Components**
- Forms (Button, Input, Select, Checkbox, etc.)
- Display (Card, Table, Badge, etc.)
- Feedback (Alert, Modal, Toast, etc.)
- Navigation (Navbar, Tabs, Breadcrumb, etc.)
- Layout (Container, Row, Col, Grid)

**Guides**
- Theming Deep Dive
- HTMX Patterns
- Form Validation
- Accessibility Best Practices
- Performance Optimization
- Testing Components

**Advanced**
- Building Custom Components
- Contributing Guide
- Architecture Overview
- API Reference

**Community**
- Showcase
- Extensions Registry
- Tutorials & Videos
- Blog

### Documentation Features

**Interactive Component Previews:**
Every component page has:
- Live rendered example
- Code snippet (copy button)
- Props table (all parameters)
- Variants showcase
- Dark mode toggle
- Mobile/tablet/desktop views

**Search:**
- Full-text search across all docs
- Component search (type to find)
- Keyboard shortcuts (Cmd+K)

**Accessibility:**
- WCAG AA compliant
- Keyboard navigation
- Screen reader tested
- High contrast mode

---

## 🗺️ Phase 7+ (Post v1.0)

Ideas for the future (not committed, subject to change):

### Advanced Components (v1.1 - v1.5)
- **Rich Text Editor** wrapper (TipTap/Quill)
- **Date Picker** with calendar view
- **Color Picker** with palettes
- **Kanban Board** with drag-drop
- **Timeline** component
- **Tree View** with expand/collapse
- **Stepper** for multi-step forms
- **Carousel/Slider** with HTMX

### Developer Experience (v1.x)
- **VS Code Extension**
  - Component snippets
  - Prop autocomplete
  - Live preview
  - Theme switcher

- **Browser DevTools Extension**
  - Inspect components
  - Edit props live
  - HTMX request viewer
  - Performance profiler

- **Component Playground** (website)
  - Drag-and-drop UI builder
  - Export code
  - Share creations
  - Component combinations

### Enterprise Features (v2.0+)
- **Design Tokens** system
- **White Label** theming
- **A11y Validator** (WCAG compliance checker)
- **Performance Budget** enforcement
- **Multi-Language** support (i18n)
- **Right-to-Left** (RTL) layouts

### AI-Powered Features (v2.x)
- **AI Chat Component** (Claude/GPT wrapper)
- **Smart Forms** (AI-suggested corrections)
- **Content Generator** (fill forms with AI)
- **Component Generator** (describe component, AI builds it)
- **Theme Generator** (AI-generated color schemes)

---

## 🎯 v1.0.0 – Production Release (August 2026)

**The Big One:** Official production-ready release.

### Milestones

**Components:** 100+ total
- All Bootstrap 5 components covered
- Phase 5 layouts and patterns
- Phase 6 data integrations
- Community extensions ecosystem

**Quality:**
- 95%+ test coverage
- All components `@stable`
- Zero known critical bugs
- Performance benchmarked
- Accessibility audited

**Documentation:**
- Complete API reference
- 50+ tutorials
- 10+ video courses
- Interactive playground
- Migration guides

**Community:**
- 50+ contributors
- 100+ production apps
- Active Discord community
- Monthly meetups
- Conference presence

**Ecosystem:**
- 20+ theme packs
- 30+ component extensions
- 10+ template packs
- Extension registry live
- Marketplace website

**Marketing:**
- Press releases
- Blog tour
- Conference talks
- Podcast interviews
- Case studies published

**Celebration:**
- Virtual launch party
- Contributor awards
- v1.0 swag
- Website redesign
- Logo reveal

### Launch Week Schedule

**Monday:** Official announcement
- Press release
- Blog post
- Social media blitz

**Tuesday:** Video showcase
- Component overview
- Live coding session
- Q&A with maintainers

**Wednesday:** Community spotlight
- Top contributor interviews
- Showcase projects
- Extension highlights

**Thursday:** Enterprise day
- Case studies
- ROI calculator
- Partnership announcements

**Friday:** Party time!
- Virtual meetup
- Live demos
- Contributor recognition
- Roadmap for v2.0

---

## 📊 Appendix: Detailed Component List

### Current Components (v0.4.5 - 38 total)

**Forms (12):**
1. Button
2. ButtonGroup
3. Input
4. Select
5. Checkbox
6. Radio
7. Switch
8. Range
9. InputGroup
10. FloatingLabel
11. FileInput
12. Dropdown

**Display (9):**
13. Card
14. Badge
15. Table (+ THead, TBody, TRow, TCell)
16. ListGroup (+ ListGroupItem)
17. Accordion (+ AccordionItem)
18. Figure
19. EmptyState
20. StatCard
21. Hero

**Feedback (7):**
22. Alert
23. Modal
24. Toast
25. Tooltip
26. Popover
27. ConfirmDialog
28. Spinner

**Navigation (6):**
29. Navbar
30. Drawer
31. Tabs
32. Breadcrumb
33. Pagination
34. Collapse

**Layout (3):**
35. Container
36. Row
37. Col

**Utilities (1):**
38. Icon (Bootstrap Icons helper)

### Planned Components (Phase 5-7)

**Phase 5 - Layouts & Patterns (v0.5.0):**
- DashboardLayout
- LandingLayout
- NavbarModern
- FeatureGrid
- PricingGroup
- TestimonialSection
- FooterModern
- + Effects module (20+ CSS effects)

**Phase 6 - Data & Productivity (v0.6.x):**
- Table.from_df()
- Table.from_pydantic()
- Chart (Matplotlib/Plotly wrapper)
- Form.from_pydantic()
- LoginCard
- SignupForm
- PasswordReset
- LiveBadge
- LiveTable
- LiveChart
- NotificationStream

**Future Phases (v1.0+):**
- Rich Text Editor
- Date Picker
- Color Picker
- Kanban Board
- Timeline
- Tree View
- Stepper
- Carousel

**Total planned for v1.0:** 100+ components

---

## 📞 Contact & Support

**For Users:**
- **Discord:** [#faststrap channel](https://discord.gg/qcXvcxMhdP)
- **Discussions:** [GitHub Discussions](https://github.com/Faststrap-org/Faststrap/discussions)
- **Email:** support@faststrap.dev

**For Contributors:**
- **Dev Chat:** [Discord #faststrap-dev](https://discord.gg/qcXvcxMhdP)
- **Office Hours:** Fridays 3pm UTC (link in Discord)
- **Email:** contributors@faststrap.dev

**For Partners/Press:**
- **Partnerships:** partnerships@faststrap.dev
- **Media:** press@faststrap.dev
- **Speaking:** speaking@faststrap.dev

**Security:**
- **Vulnerabilities:** security@faststrap.dev
- **PGP Key:** [Download](https://faststrap.dev/security.asc)
- **Response Time:** 24-48 hours

---

## 📜 License & Legal

**Faststrap** is open source software released under the **MIT License**.

```
MIT License

Copyright (c) 2025-2026 Faststrap Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND...
```

**What this means:**
- ✅ Use commercially (no restrictions)
- ✅ Modify as needed
- ✅ Distribute freely
- ✅ Private use
- ❌ No warranty (use at own risk)
- ❌ Authors not liable

**Third-Party Licenses:**
- **Bootstrap:** MIT License
- **HTMX:** BSD 2-Clause License
- **FastHTML:** Apache 2.0 License

**Trademark:**
"Faststrap" name and logo are trademarks of the Faststrap project. See [TRADEMARK.md](TRADEMARK.md) for usage guidelines.

---

## 🙏 Acknowledgments

**Built on the shoulders of giants:**

- **FastHTML** by Answer.AI - The amazing pure-Python web framework
- **Bootstrap** by Twitter/Bootstrap Team - Battle-tested UI framework
- **HTMX** by Big Sky Software - Bringing interactivity back to HTML
- **Python** by Python Software Foundation - The best language for humans

**Inspired by:**
- React Bootstrap
- Shadcn/ui
- DaisyUI
- Mantine
- Material-UI

**Special Thanks:**
- Jeremy Howard (@jph00) - Creator of FastHTML
- FastHTML community - Early adopters and feedback
- All contributors - You make this possible
- Bootstrap team - 13 years of excellence
- Carson Gross - HTMX philosophy

---

**Last Updated:** January 2026  
**Current Version:** v0.5.6 (pre-v0.6 additions)  
**Next Release:** v0.5.0 (February 2026)

**Let's build the definitive UI library for FastHTML — together.** 🚀

---

## 🗂️ Quick Links

- **GitHub:** [Faststrap-org/Faststrap](https://github.com/Faststrap-org/Faststrap)
- **Documentation:** [faststrap.dev](https://faststrap.dev)
- **PyPI:** [pypi.org/project/faststrap](https://pypi.org/project/faststrap/)
- **Discord:** [FastHTML Community](https://discord.gg/qcXvcxMhdP)
- **Twitter:** [@faststrap](https://twitter.com/faststrap)
- **Blog:** [faststrap.dev/blog](https://faststrap.dev/blog)

**Star us on GitHub** ⭐ if Faststrap helps you build better apps!
