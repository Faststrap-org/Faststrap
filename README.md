# Faststrap

**Faststrap is a component-based extension for FastHTML that provides reusable UI elements (cards, modals, toasts, drawers, navbars, grids, etc.) using lightweight Bootstrap styling. Fully customizable, developer-friendly, and designed to keep the simplicity of FastHTML.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![FastHTML](https://img.shields.io/badge/FastHTML-0.2+-green.svg)](https://fastht.ml/)

---

## Why FastStrap?

FastHTML is amazing for building web apps in pure Python, but it lacks pre-built UI components. FastStrap fills that gap by providing:

✅ **20+ Bootstrap components** - Cards, Modals, Navbars, Forms, and more  
✅ **Zero JavaScript knowledge required** - It just works  
✅ **No build steps** - Pure Python, no npm/webpack/vite  
✅ **Full HTMX integration** - Dynamic updates without page reloads  
✅ **Dark mode built-in** - Automatic theme switching  
✅ **Type-safe** - Full type hints for better DX  
✅ **Pythonic API** - Kwargs or fluent style, your choice

---

## Quick Start

### Installation

```bash
pip install faststrap
```

### Hello World

```python
from fasthtml.common import FastHTML, serve
from faststrap import add_bootstrap, Card, Button

app = FastHTML()
add_bootstrap(app, theme="dark")

@app.route("/")
def home():
    return Card(
        "Welcome to FastStrap! Build beautiful UIs in pure Python.",
        title="Hello World 👋",
        footer=Button("Get Started", variant="primary", hx_get="/docs")
    )

serve()
```

That's it! You now have a modern, responsive web app with zero JavaScript.

---

## Core Concepts

### 1. Adding Bootstrap to Your App

```python
from fasthtml.common import FastHTML
from faststrap import add_bootstrap

app = FastHTML()

# Basic setup
add_bootstrap(app)

# With dark theme
add_bootstrap(app, theme="dark")

# Using CDN (default is local assets)
add_bootstrap(app, use_cdn=True)
```

### 2. Component API Styles

FastStrap supports two API styles - use what feels natural:

#### Kwargs Style (Simple)
```python
Card(
    "Content here",
    title="My Card",
    footer="Footer text",
    variant="primary",
    shadow=True
)
```

#### Fluent Style (Complex compositions)
```python
Card("Content") \
    .with_title("My Card") \
    .with_footer(Button("Action")) \
    .add_class("mt-3") \
    .build()
```

### 3. HTMX Integration

All components support HTMX attributes for dynamic behavior:

```python
Button(
    "Load More",
    variant="primary",
    hx_get="/api/items",
    hx_target="#items",
    hx_swap="beforeend"
)
```

---

## Available Components

### ✅ Phase 1 (Current - v0.1.0)
- [ ] **Button** - Variants, sizes, loading states, icons
- [ ] **Card** - Headers, footers, images, shadows
- [ ] **Alert** - Dismissible alerts with variants
- [ ] **Container/Row/Col** - Bootstrap grid system
- [ ] **Toast** - Auto-dismiss notifications

### 🚧 Phase 2 (Coming Soon - v0.2.0)
- [ ] **Navbar** - Responsive navigation with dropdowns
- [ ] **Modal** - Dialogs and confirmations
- [ ] **Drawer** - Offcanvas side panels
- [ ] **Input/Select** - Form components with validation
- [ ] **ButtonGroup** - Grouped buttons

### 🔮 Phase 3 (Planned - v0.3.0)
- [ ] **Tabs/Accordion** - Collapsible content
- [ ] **DataTable** - Sortable, filterable tables
- [ ] **Stepper** - Multi-step forms
- [ ] **Avatar/Badge** - User avatars and status badges
- [ ] **Timeline** - Event timelines

---

## Project Structure

```
faststrap/
├── src/faststrap/
│   ├── __init__.py              # Public API
│   ├── core/
│   │   ├── assets.py            # Bootstrap injection
│   │   ├── base.py              # Component base classes
│   │   └── theme.py             # Theme management
│   ├── components/
│   │   ├── layout/              # Grid, containers
│   │   ├── display/             # Cards, badges
│   │   ├── feedback/            # Alerts, toasts
│   │   ├── navigation/          # Navbars, tabs
│   │   ├── forms/               # Inputs, buttons
│   │   └── advanced/            # DataTables, charts
│   ├── utils/
│   │   ├── icons.py             # Bootstrap Icons
│   │   └── htmx.py              # HTMX helpers
│   └── templates/               # Page patterns
├── static/                      # Bootstrap assets
├── tests/                       # Pytest suite
├── examples/                    # Demo apps
└── docs/                        # Documentation site
```

---

## Development Setup

### Prerequisites
- Python 3.10+
- FastHTML 0.2+
- Git

### Local Development

```bash
# Clone the repo
git clone https://github.com/yourusername/faststrap.git
cd faststrap

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # or `.venv\Scripts\activate` on Windows

# Install with dev dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Run type checking
mypy src/faststrap

# Format code
black src/faststrap
ruff check src/faststrap
```

---

## Contributing

We welcome contributions! Here's how to get started:

### Component Development Checklist

When building a new component:

1. **Create component file** in appropriate `components/` subdirectory
2. **Implement component** following existing patterns
3. **Add type hints** - FastStrap is fully typed
4. **Write tests** - Aim for 100% coverage
5. **Add examples** - Include usage examples in docstrings
6. **Update `__init__.py`** - Export your component
7. **Document it** - Add to README and docs site

### Component Template

```python
# components/display/my_component.py
from typing import Literal, Optional, Any
from fasthtml.common import Div
from faststrap.core.base import merge_classes

VariantType = Literal["primary", "secondary", "success", "danger"]

def MyComponent(
    *children: Any,
    variant: VariantType = "primary",
    size: str = "md",
    **kwargs: Any
) -> Div:
    """Short description of component.
    
    Args:
        *children: Component content
        variant: Bootstrap color variant
        size: Component size
        **kwargs: Additional HTML attributes
    
    Returns:
        Div element with Bootstrap classes
    
    Example:
        MyComponent("Hello", variant="success")
    """
    classes = merge_classes(
        f"my-component my-component-{variant}",
        f"my-component-{size}",
        kwargs.pop("cls", None)
    )
    
    return Div(*children, cls=classes, **kwargs)
```

---

## Roadmap

### v0.1.0 (Current) - Foundation
- ✅ Core infrastructure
- ✅ Asset management
- ✅ Theme system
- 🚧 5 core components

### v0.2.0 - Navigation & Forms
- Navigation components
- Form components with validation
- Advanced HTMX patterns

### v0.3.0 - Advanced Features
- DataTables
- Charts integration
- Page templates
- Component playground

### v1.0.0 - Production Ready
- Full component library
- Comprehensive docs
- VS Code extension
- Community templates

---

## License

MIT License - see [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- **FastHTML** - The amazing pure-Python web framework
- **Bootstrap** - Battle-tested UI components
- **HTMX** - Dynamic interactions without JavaScript complexity
- **Our contributors** - Thank you! 🙏

---

## Support

- 📖 **Documentation**: [faststrap.readthedocs.io](https://faststrap.readthedocs.io)
- 🐛 **Issues**: [GitHub Issues](https://github.com/yourusername/faststrap/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/yourusername/faststrap/discussions)
- 🎮 **Discord**: Join [FastHTML Discord](https://discord.gg/fasthtml)

---

**Built with ❤️ by the FastStrap community**