# FastStrap

**Modern Bootstrap 5 components for FastHTML - Build beautiful web UIs in pure Python with zero JavaScript knowledge.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![FastHTML](https://img.shields.io/badge/FastHTML-0.6+-green.svg)](https://fastht.ml/)
[![PyPI version](https://img.shields.io/pypi/v/faststrap.svg)](https://pypi.org/project/faststrap/)
[![Tests](https://github.com/Faststrap-org/Faststrap/workflows/Tests/badge.svg)](https://github.com/Faststrap-org/Faststrap/actions)

---

## Why FastStrap?

FastHTML is amazing for building web apps in pure Python, but it lacks pre-built UI components. FastStrap fills that gap by providing:

✅ **40+ Bootstrap components** - Buttons, Cards, Modals, Forms, Navigation, and more  
✅ **Zero JavaScript knowledge required** - Components just work  
✅ **No build steps** - Pure Python, no npm/webpack/vite  
✅ **Full HTMX integration** - Dynamic updates without page reloads  
✅ **Dark mode built-in** - Automatic theme switching  
✅ **Type-safe** - Full type hints for better IDE support  
✅ **Pythonic API** - Intuitive kwargs style
✅ **Enhanced customization** - Slot classes, CSS variables, themes, and more

---

## Quick Start

### Installation

```bash
pip install faststrap
```

### Hello World

```python
from fasthtml.common import FastHTML, serve
from faststrap import add_bootstrap, Card, Button, create_theme

app = FastHTML()

# Use built-in theme or create custom
theme = create_theme(primary="#7BA05B", secondary="#48C774")
add_bootstrap(app, theme=theme, theme="dark")

@app.route("/")
def home():
    return Card(
        "Welcome to FastStrap! Build beautiful UIs in pure Python.",
        header="Hello World 👋",
        footer=Button("Get Started", variant="primary")
    )

serve()
```

That's it! You now have a modern, responsive web app with zero JavaScript.

---

## Enhanced Features

### 1. Enhanced Attribute Handling

Faststrap now supports advanced attribute handling:

```python
from faststrap import Button

# Style dict and CSS variables
Button(
    "Styled Button",
    style={"background-color": "#7BA05B", "border": "none"},
    css_vars={"--bs-btn-padding-y": "0.75rem", "--bs-btn-border-radius": "12px"},
    data={"id": "123", "type": "demo"},
    aria={"label": "Styled button"},
)

# Filter None/False values automatically
Button("Test", disabled=None, hidden=False)  # None/False values are dropped
```

### 2. CloseButton Helper

Reusable close button for alerts, modals, and drawers:

```python
from faststrap import CloseButton, Alert

# Use in alerts
Alert(
    "This alert uses CloseButton helper",
    variant="info",
    dismissible=True,
)

# Use in modals/drawers (automatically used)
```

### 3. Expanded Button Component

More control over button appearance and behavior:

```python
from faststrap import Button

# Render as link
Button("As Link", as_="a", href="/page", variant="secondary")

# Loading states with custom text
Button("Loading", loading=True, loading_text="Please wait...", spinner=True)

# Full width, pill, active states
Button("Full Width", full_width=True, variant="info")
Button("Pill", pill=True, variant="warning")
Button("Active", active=True, variant="success")

# Icon and spinner control
Button("Icon + Spinner", icon="check-circle", spinner=True, icon_pos="start")
```

### 4. Slot Class Overrides

Fine-grained control over component parts:

```python
from faststrap import Card, Modal, Drawer, Dropdown

# Card with custom slot classes
Card(
    "Content",
    header="Custom Header",
    footer="Custom Footer",
    header_cls="bg-primary text-white p-3",
    body_cls="p-4",
    footer_cls="text-muted",
)

# Modal with custom classes
Modal(
    "Modal content",
    title="Custom Modal",
    dialog_cls="shadow-lg",
    content_cls="border-0",
    header_cls="bg-primary text-white",
    body_cls="p-4",
)

# Drawer with custom classes
Drawer(
    "Drawer content",
    title="Custom Drawer",
    header_cls="bg-success text-white",
    body_cls="p-4",
)

# Dropdown with custom classes
Dropdown(
    "Option 1", "Option 2",
    label="Custom Dropdown",
    toggle_cls="custom-toggle",
    menu_cls="custom-menu",
    item_cls="custom-item",
)
```

### 5. Theme System

Create and apply custom themes:

```python
from faststrap import create_theme, add_bootstrap

# Create custom theme
my_theme = create_theme(
    primary="#7BA05B",
    secondary="#48C774",
    info="#36A3EB",
    warning="#FFC107",
    danger="#DC3545",
    success="#28A745",
    light="#F8F9FA",
    dark="#343A40",
)

# Use built-in themes
add_bootstrap(app, theme="green-nature")  # or "blue-ocean", "dark-mode", etc.

# Or use custom theme
add_bootstrap(app, theme=my_theme)
```

Available built-in themes:
- `green-nature`
- `blue-ocean`
- `purple-magic`
- `red-alert`
- `orange-sunset`
- `teal-oasis`
- `indigo-night`
- `pink-love`
- `cyan-sky`
- `gray-mist`
- `dark-mode`
- `light-mode`

### 6. Registry Metadata

Components now include metadata about JavaScript requirements:

```python
from faststrap.core.registry import list_components, get_component

# List all components
components = list_components()

# Check if component requires JS
modal = get_component("Modal")
# Modal is registered with requires_js=True
```

---

## Available Components (38 Total)

### ✅ Phase 1+2 (v0.1.0 - v0.2.2) - 12 Components

| Component | Description | Status |
|-----------|-------------|--------|
| **Button** | Buttons with variants, sizes, loading states | ✅ |
| **ButtonGroup** | Grouped buttons and toolbars | ✅ |
| **Badge** | Status indicators and labels | ✅ |
| **Card** | Content containers with headers/footers | ✅ |
| **Alert** | Dismissible alerts with variants | ✅ |
| **Modal** | Dialog boxes and confirmations | ✅ |
| **Drawer** | Offcanvas side panels | ✅ |
| **Toast** | Auto-dismiss notifications | ✅ |
| **Navbar** | Responsive navigation bars | ✅ |
| **Container/Row/Col** | Bootstrap grid system | ✅ |
| **Icon** | Bootstrap Icons helper | ✅ |

### ✅ Phase 3 (v0.3.0) - 8 New Components

| Component | Description | Status |
|-----------|-------------|--------|
| **Tabs** | Navigation tabs and pills | ✅ |
| **Dropdown** | Contextual menus with split buttons | ✅ |
| **Input** | Text form controls with validation | ✅ |
| **Select** | Dropdown selections (single/multiple) | ✅ |
| **Breadcrumb** | Navigation trail with icons | ✅ |
| **Pagination** | Page navigation with customization | ✅ |
| **Spinner** | Loading indicators (border/grow) | ✅ |
| **Progress** | Progress bars with animations | ✅ |

### ✅ Phase 4A (v0.4.0) - 10 Components

| Component | Description | Status |
|-----------|-------------|--------|
| **Table** | Responsive data tables | ✅ |
| **Accordion** | Collapsible panels | ✅ |
| **Checkbox** | Checkbox form controls | ✅ |
| **Radio** | Radio button controls | ✅ |
| **Switch** | Toggle switch variant | ✅ |
| **Range** | Slider input control | ✅ |
| **ListGroup** | Versatile lists | ✅ |
| **Collapse** | Show/hide content | ✅ |
| **InputGroup** | Prepend/append addons | ✅ |
| **FloatingLabel** | Animated label inputs | ✅ |

### ✅ Phase 4B (v0.4.5) - 8 Components

| Component | Description | Status |
|-----------|-------------|--------|
| **FileInput** | File uploads with preview | ✅ |
| **Tooltip** | Contextual hints | ✅ |
| **Popover** | Rich overlays | ✅ |
| **Figure** | Image + caption | ✅ |
| **ConfirmDialog** | Modal confirmation preset | ✅ |
| **EmptyState** | Placeholder component | ✅ |
| **StatCard** | Metric display card | ✅ |
| **Hero** | Landing page hero section | ✅ |

### 🗓️ Phase 5+ (v0.5.0 - v1.0.0)

- **Sidebar**, **Footer**, **DashboardLayout**
- **DataTable** with sorting/filtering/pagination
- **FormWizard**, **Stepper**
- **Timeline**, **ProfileDropdown**, **SearchBar**
- **Carousel**, **MegaMenu**, **NotificationCenter**
- And 40+ more components...

**Target: 100+ components by v1.0.0 (Aug 2026)**

See [ROADMAP.md](ROADMAP.md) for complete timeline.

---

## Core Concepts

### 1. Adding Bootstrap to Your App

```python
from fasthtml.common import FastHTML
from faststrap import add_bootstrap, create_theme

app = FastHTML()

# Basic setup (includes default FastStrap favicon)
add_bootstrap(app)

# With dark theme
add_bootstrap(app, theme="dark")

# Custom theme
theme = create_theme(primary="#7BA05B", secondary="#48C774")
add_bootstrap(app, theme=theme)

# Using CDN
add_bootstrap(app, use_cdn=True)
```

### 2. Using Components

All components follow Bootstrap's conventions with Pythonic names:

```python
from faststrap import Button, Badge, Alert, Input, Select, Tabs

# Button with HTMX
Button("Save", variant="primary", hx_post="/save", hx_target="#result")

# Form inputs
Input("email", input_type="email", label="Email Address", required=True)
Select("country", ("us", "USA"), ("uk", "UK"), label="Country")

# Navigation tabs
Tabs(
    ("home", "Home", True),
    ("profile", "Profile"),
    ("settings", "Settings")
)
```

### 3. HTMX Integration

All components support HTMX attributes:

```python
# Dynamic button
Button("Load More", hx_get="/api/items", hx_swap="beforeend")

# Live search input
Input("search", placeholder="Search...", hx_get="/search", hx_trigger="keyup changed delay:500ms")

# Dynamic dropdown
Select("category", ("a", "A"), ("b", "B"), hx_get="/filter", hx_trigger="change")
```

### 4. Responsive Grid System

```python
from faststrap import Container, Row, Col

Container(
    Row(
        Col("Left column", cols=12, md=6, lg=4),
        Col("Middle column", cols=12, md=6, lg=4),
        Col("Right column", cols=12, md=12, lg=4)
    )
)
```

---

## Examples

### Form with Validation

```python
from faststrap import Input, Select, Button, Card

Card(
    Input(
        "email",
        input_type="email",
        label="Email Address",
        placeholder="you@example.com",
        required=True,
        help_text="We'll never share your email"
    ),
    Input(
        "password",
        input_type="password",
        label="Password",
        required=True,
        size="lg"
    ),
    Select(
        "country",
        ("us", "United States"),
        ("uk", "United Kingdom"),
        ("ca", "Canada"),
        label="Country",
        required=True
    ),
    Button("Sign Up", variant="primary", type="submit", cls="w-100"),
    header="Create Account"
)
```

### Navigation with Tabs

```python
from faststrap import Tabs, TabPane, Card

Card(
    Tabs(
        ("profile", "Profile", True),
        ("settings", "Settings"),
        ("billing", "Billing")
    ),
    Div(
        TabPane("Profile content here", tab_id="profile", active=True),
        TabPane("Settings content here", tab_id="settings"),
        TabPane("Billing content here", tab_id="billing"),
        cls="tab-content p-3"
    )
)
```

### Loading States

```python
from faststrap import Spinner, Progress, Button

# Spinner in button
Button(
    Spinner(size="sm", label="Loading..."),
    " Processing...",
    variant="primary",
    disabled=True
)

# Progress bar
Progress(75, variant="success", striped=True, animated=True, label="75%")

# Stacked progress
Div(
    ProgressBar(30, variant="success"),
    ProgressBar(20, variant="warning"),
    ProgressBar(10, variant="danger"),
    cls="progress"
)
```

### Pagination

```python
from faststrap import Pagination, Breadcrumb

# Breadcrumb
Breadcrumb(
    (Icon("house"), "/"),
    ("Products", "/products"),
    ("Laptops", None)
)

# Page navigation
Pagination(
    current_page=5,
    total_pages=20,
    size="lg",
    align="center",
    show_first_last=True
)
```

---

## Project Structure

```
faststrap/
├── src/faststrap/
│   ├── __init__.py              # Public API
│   ├── core/
│   │   ├── assets.py            # Bootstrap injection + favicon
│   │   ├── base.py              # Component base classes
│   │   ├── registry.py          # Component registry
│   │   └── theme.py             # Theme system
│   ├── components/
│   │   ├── forms/               # Button, Input, Select
│   │   ├── display/             # Card, Badge
│   │   ├── feedback/            # Alert, Toast, Modal, Spinner, Progress
│   │   ├── navigation/          # Navbar, Drawer, Tabs, Dropdown, Breadcrumb, Pagination
│   │   └── layout/              # Container, Row, Col
│   ├── static/                  # Bootstrap assets + favicon
│   │   ├── css/
│   │   │   ├── bootstrap.min.css
│   │   │   └── bootstrap-icons.min.css
│   │   ├── js/
│   │   │   └── bootstrap.bundle.min.js
│   │   └── favicon.svg          # Default FastStrap favicon
│   ├── templates/               # Component templates
│   └── utils/
│       ├── icons.py             # Bootstrap Icons
│       ├── static_management.py # Assets extended helper functions
│       └── attrs.py             # Centralized attribute conversion
├── tests/                       # 219 tests (80% coverage)
├── examples/                    # Demo applications
│   └── demo_all.py              # Comprehensive demo
└── docs/                        # Documentation
```

---

## Development

### Prerequisites

- Python 3.10+
- FastHTML 0.6+
- Git

### Setup

```bash
# Clone repository
git clone https://github.com/Faststrap-org/Faststrap.git
cd Faststrap

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install with dev dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Run with coverage
pytest --cov=faststrap

# Type checking
mypy src/faststrap

# Format code
black src/faststrap tests
ruff check src/faststrap tests
```

---

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Quick Contribution Guide

1. **Pick a component** from [ROADMAP.md](ROADMAP.md) Phase 4
2. **Follow patterns** in [BUILDING_COMPONENTS.md](BUILDING_COMPONENTS.md)
3. **Write tests** - Aim for 100% coverage (8-15 tests per component)
4. **Submit PR** - We review within 48 hours

---

## Documentation

- 📖 **Component Spec**: [COMPONENT_SPEC.md](COMPONENT_SPEC.md)
- 🏗️ **Building Guide**: [BUILDING_COMPONENTS.md](BUILDING_COMPONENTS.md)
- 🗺️ **Roadmap**: [ROADMAP.md](ROADMAP.md)
- 🤝 **Contributing**: [CONTRIBUTING.md](CONTRIBUTING.md)
- 📝 **Changelog**: [CHANGELOG.md](CHANGELOG.md)

---

## Roadmap

### v0.3.1 (Current - December 2025)
- ✅ 20 components (12 + 8 new)
- ✅ 219 tests, 80% coverage
- ✅ Centralized `convert_attrs()` utility
- ✅ Default FastStrap favicon
- ✅ Full HTMX integration
- ✅ Enhanced customization (slot classes, CSS vars, themes)
- ✅ Component defaults system with `resolve_defaults()`

### v0.4.0 (Phase 4A - Complete)
- ✅ Table, Accordion, Checkbox, Radio, Switch
- ✅ Range, ListGroup, Collapse, InputGroup, FloatingLabel
- ✅ 30 components total

### v0.4.5 (Phase 4B - Complete)
- ✅ FileInput, Tooltip, Popover, Figure
- ✅ ConfirmDialog, EmptyState, StatCard, Hero
- ✅ 38 components total

### v0.5.0 (Phase 5 - Mar 2026)
- Sidebar, Footer, DashboardLayout
- Timeline, Carousel, MegaMenu
- 50 components total

### v1.0.0 (Target Aug 2026)
- 100+ components
- Component playground
- Full documentation website
- Video tutorials
- Production ready

See [ROADMAP.md](ROADMAP.md) for complete timeline.

---

## Stats

- **38 components** across 5 categories
- **219+ passing tests**
- **Zero custom JavaScript** required
- **Full HTMX integration**
- **Enhanced customization** with slot classes, CSS variables, and themes

---

## Support

- 📖 **Documentation**: [GitHub README](https://github.com/Faststrap-org/Faststrap#readme)
- 🐛 **Bug Reports**: [GitHub Issues](https://github.com/Faststrap-org/Faststrap/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/Faststrap-org/Faststrap/discussions)
- 🎮 **Discord**: [FastHTML Community](https://discord.gg/qcXvcxMhdP)

---

## License

MIT License - see [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- **FastHTML** - The amazing pure-Python web framework
- **Bootstrap** - Battle-tested UI components
- **HTMX** - Dynamic interactions without complexity
- **Contributors** - Thank you! 🙏

---

**Built with ❤️ for the FastHTML community**