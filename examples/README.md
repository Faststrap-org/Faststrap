# Faststrap Examples

Welcome to the Faststrap examples! This directory contains a comprehensive collection of examples organized by complexity and use case to help you learn and build with Faststrap.

## 📚 Directory Structure

```
examples/
├── README.md (you are here)
├── 01_getting_started/     # Start here if you're new
├── 02_components/          # Learn individual components
├── 03_real_world_apps/     # Complete applications
├── 04_advanced/            # Advanced patterns
└── 05_integrations/        # Third-party integrations
```

---

## 🚀 Getting Started

### New to Faststrap?

**Start with these examples in order:**

1. **[01_getting_started/hello_world.py](01_getting_started/hello_world.py)** - Your first Faststrap app
2. **[01_getting_started/first_card.py](01_getting_started/first_card.py)** - Working with components
3. **[01_getting_started/simple_form.py](01_getting_started/simple_form.py)** - Building forms
4. **[01_getting_started/adding_htmx.py](01_getting_started/adding_htmx.py)** - Adding interactivity

### Already familiar with FastHTML?

Jump straight to:
- **[02_components/](02_components/)** - Component-focused examples
- **[03_real_world_apps/](03_real_world_apps/)** - Full applications

---

## 📂 What's in Each Directory

### 01_getting_started/ - For Beginners

**Perfect for:** Python developers new to web development or Faststrap

Simple, focused examples that introduce core concepts one at a time.

- `hello_world.py` - Minimal Faststrap app
- `first_card.py` - Using your first component
- `simple_form.py` - Building a basic form
- `adding_htmx.py` - Adding interactivity with HTMX

**Run an example:**
```bash
cd examples/01_getting_started
python hello_world.py
# Open http://localhost:5000
```

---

### 02_components/ - Component Gallery

**Perfect for:** Learning how to use specific components

Focused examples demonstrating each component's features and use cases.

**Organized by category:**
```
02_components/
├── forms/          # Button, Input, Select, etc.
├── display/        # Card, Table, Badge, etc.
├── feedback/       # Alert, Modal, Spinner, etc.
├── navigation/     # Navbar, Tabs, Dropdown, etc.
└── layout/         # Grid, Container, Hero, etc.
```

**Example:**
```bash
cd examples/02_components/forms
python button_showcase.py
```

---

### 03_real_world_apps/ - Complete Applications

**Perfect for:** Seeing Faststrap in production-ready applications

Full-featured applications demonstrating best practices, architecture, and real-world patterns.

#### Available Apps:

**🛒 E-commerce Store** (`ecommerce/`)
- Product catalog with search and filters
- Shopping cart with HTMX
- Checkout flow
- Admin panel

**📝 Blog Platform** (`blog/`)
- Post listing and detail pages
- Markdown support
- Comments system
- Admin dashboard

**📊 Admin Dashboard** (`dashboard/`)
- Responsive sidebar navigation
- Data tables with pagination
- Charts and statistics
- User management

**🎨 Portfolio Site** (`portfolio/`)
- Project showcase
- About page
- Contact form
- Responsive design

**🚀 SaaS Landing Page** (`saas_landing/`)
- Hero section with effects
- Feature highlights
- Pricing tables
- Call-to-action sections

**🧮 Calculator** (`calculator/`)
- Interactive calculator UI
- HTMX-powered calculations
- Keyboard support
- History tracking

**🎮 Tic-Tac-Toe Game** (`game/`)
- Interactive game board
- Win detection
- Score tracking
- Reset functionality

**Run an app:**
```bash
cd examples/03_real_world_apps/ecommerce
python app.py
```

---

### 04_advanced/ - Advanced Patterns

**Perfect for:** Experienced developers looking for advanced techniques

Advanced patterns, custom themes, and optimization techniques.

- `custom_themes.py` - Creating custom Bootstrap themes
- `htmx_patterns.py` - Advanced HTMX patterns
- `effects_showcase.py` - All Faststrap effects in action
- `responsive_design.py` - Advanced responsive patterns
- `component_defaults.py` - Using `set_component_defaults`

---

### 05_integrations/ - Third-Party Integrations

**Perfect for:** Integrating Faststrap with other tools

Examples showing how to integrate Faststrap with databases, validation libraries, and more.

- `database_tables.py` - SQLAlchemy integration
- `pydantic_forms.py` - Pydantic validation
- `media_players.py` - FastHTML Audio/Video integration
- `authentication.py` - User authentication patterns

---

## 🎯 Quick Reference

### By Use Case

| I want to... | Go to... |
|--------------|----------|
| Learn Faststrap basics | `01_getting_started/` |
| See how a specific component works | `02_components/{category}/` |
| Build an e-commerce site | `03_real_world_apps/ecommerce/` |
| Build a blog | `03_real_world_apps/blog/` |
| Build an admin panel | `03_real_world_apps/dashboard/` |
| Create custom themes | `04_advanced/custom_themes.py` |
| Use Faststrap with a database | `05_integrations/database_tables.py` |
| Add form validation | `05_integrations/pydantic_forms.py` |

### By Component

| Component | Example Location |
|-----------|-----------------|
| Button | `02_components/forms/button_showcase.py` |
| Card | `02_components/display/card_showcase.py` |
| Form | `02_components/forms/form_showcase.py` |
| Table | `02_components/display/table_showcase.py` |
| Modal | `02_components/feedback/modal_showcase.py` |
| Navbar | `02_components/navigation/navbar_showcase.py` |
| Effects (Fx) | `04_advanced/effects_showcase.py` |

---

## 💡 Tips for Learning

1. **Start Simple** - Begin with `01_getting_started/` even if you're experienced
2. **Run the Code** - Don't just read, run each example and experiment
3. **Read the Docs** - Each example references relevant documentation
4. **Modify and Break** - Change the code to see what happens
5. **Build Something** - Use examples as templates for your own projects

---

## 🔧 Running Examples

All examples are standalone Python files that can be run directly:

```bash
# Navigate to example directory
cd examples/01_getting_started

# Run the example
python hello_world.py

# Open your browser
# http://localhost:5000
```

**Requirements:**
- Python 3.10+
- Faststrap installed (`pip install faststrap`)

---

## 📖 Documentation

For detailed component documentation, visit:
- **Online Docs**: https://faststrap-org.github.io/Faststrap/
- **Local Docs**: Run `mkdocs serve` from project root

---

## 🤝 Contributing Examples

Have a great example to share? We'd love to include it!

**Guidelines:**
- Keep it focused on one concept or use case
- Include comments explaining key parts
- Follow existing example structure
- Test that it runs without errors

Submit a PR with your example in the appropriate directory.

---

## 🆘 Need Help?

- **Documentation**: Check the [official docs](https://faststrap-org.github.io/Faststrap/)
- **Issues**: [GitHub Issues](https://github.com/Faststrap-org/Faststrap/issues)
- **Discussions**: [GitHub Discussions](https://github.com/Faststrap-org/Faststrap/discussions)

---

## 📝 Example Template

Starting a new example? Use this template:

```python
"""
Example: [Brief Description]

Demonstrates: [What this example shows]
Components: [List of components used]
Difficulty: [Beginner/Intermediate/Advanced]
"""

from fasthtml.common import *
from faststrap import *

app, rt = fast_app()

@rt("/")
def get():
    return Container(
        H1("Example Title"),
        # Your example code here
    )

serve()
```

---

**Happy coding with Faststrap! 🚀**
