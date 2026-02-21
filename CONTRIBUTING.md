# Contributing to FastStrap

Thank you for your interest in contributing! FastStrap is community-driven, and we welcome contributions of all kinds.

---

## 🚀 Quick Start

```bash
# 1. Fork and clone
git clone https://github.com/YOUR_USERNAME/Faststrap.git
cd Faststrap

# 2. Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 3. Install with dev dependencies
pip install -e ".[dev]"

# 4. Create a branch
git checkout -b feature/my-component

# 5. Make changes and test
pytest

# 6. Submit PR
git push origin feature/my-component
```

---

## 📋 Ways to Contribute

### 1. Build Components

The easiest way to contribute! Pick from [ROADMAP.md](ROADMAP.md):

**Phase 4A Priority Components (v0.4.0):**
- Table (+ THead, TBody, TRow, TCell)
- Accordion (+ AccordionItem)
- Checkbox
- Radio
- Switch
- Range
- ListGroup (+ ListGroupItem)
- Collapse
- InputGroup
- FloatingLabel

**Phase 4B Components (v0.4.5):**
- FileInput
- Tooltip
- Popover
- Figure
- ConfirmDialog
- EmptyState
- StatCard
- Hero

**How to build:**
1. Copy `src/faststrap/components/forms/button.py` as template
2. Place in appropriate directory:
   - `forms/` - Buttons, inputs, selects, checkboxes
   - `display/` - Cards, badges, avatars, images
   - `feedback/` - Alerts, toasts, modals, spinners
   - `navigation/` - Navbars, tabs, breadcrumbs, drawers
   - `layout/` - Grid, containers, dividers
3. Follow patterns in [BUILDING_COMPONENTS.md](BUILDING_COMPONENTS.md)
4. Add tests in `tests/test_components/test_<component>.py`
5. Update `__init__.py` to export your component
6. Submit PR!

### 2. Write Tests

Improve test coverage (current: 84%, goal: 90%+):

```bash
# Run tests with coverage
pytest --cov=faststrap --cov-report=html

# Open coverage report
open htmlcov/index.html  # macOS
start htmlcov/index.html # Windows
```

Look for files with <90% coverage and add tests.

### 3. Improve Documentation

- Fix typos or unclear sections
- Add more examples to component docstrings
- Create tutorial blog posts
- Record video tutorials

### 4. Report Bugs

Found a bug? [Open an issue](https://github.com/Faststrap-org/Faststrap/issues/new) with:

- FastStrap version (`pip show faststrap`)
- FastHTML version
- Python version
- Minimal code to reproduce
- Expected vs actual behavior

### 5. Suggest Features

Have an idea? [Start a discussion](https://github.com/Faststrap-org/Faststrap/discussions/new)!

---

## 🏗️ Development Workflow

### Setting Up

```bash
# Clone your fork
git clone https://github.com/Faststrap-org/Faststrap.git
cd Faststrap

# Add upstream remote
git remote add upstream https://github.com/Faststrap-org/Faststrap.git

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install with dev dependencies
pip install -e ".[dev]"
```

### Making Changes

```bash
# Create feature branch
git checkout -b feature/my-awesome-feature

# Make changes...

# Run tests
pytest

# Check types
mypy src/faststrap

# Format code
black src/faststrap tests
ruff check src/faststrap tests --fix

# Commit
git add .
git commit -m "Add awesome feature"

# Push
git push origin feature/my-awesome-feature
```

### Submitting PR

1. **Update documentation** if you added/changed features
2. **Add tests** for new functionality
3. **Run full test suite**: `pytest`
4. **Format code**: `black .` and `ruff check .`
5. **Update CHANGELOG.md** under "Unreleased"
6. **Submit PR** with clear description

### Release checklist (required for tags/releases)

Before creating a release tag, confirm all of the following:

1. `src/faststrap/__init__.py` version is updated.
2. `CHANGELOG.md` has a matching release entry.
3. `README.md` and `ROADMAP.md` are aligned with shipped vs deferred scope.
4. No generated/debug artifacts are tracked (`coverage.xml`, `test_output.txt`, `pytest_fail.txt`, `test_fail.txt`, `debug_imports.py`).
5. Quality gates pass:
   - `black --check src tests examples showcase`
   - `ruff check src tests examples showcase`
   - `mypy src/faststrap`
   - `pytest -q`

---

## 📝 Code Style

### Python Style

- **Use Python 3.10+ type hints** (`str | None` not `Optional[str]`)
- **PascalCase for components** (`Button`, `Modal`)
- **snake_case for variables** (`user_name`, `is_active`)
- **Follow existing patterns** - look at similar components
- **Max line length: 100 characters**

### Component Requirements

Every component MUST have:

```python
"""Bootstrap ComponentName for [purpose]."""

from typing import Any, Literal
from fasthtml.common import Div
from ...core.base import merge_classes
from ...utils.attrs import convert_attrs

# Type aliases
VariantType = Literal["primary", "secondary", "success", "danger"]

def ComponentName(
    *children: Any,
    variant: VariantType = "primary",
    **kwargs: Any,
) -> Div:
    """Bootstrap ComponentName component.

    Args:
        *children: Component content
        variant: Bootstrap color variant
        **kwargs: Additional HTML attributes (cls, id, hx-*, data-*, etc.)

    Returns:
        FastHTML Div element

    Example:
        Basic usage:
        >>> ComponentName("Content", variant="success")

        With HTMX:
        >>> ComponentName("Load", hx_get="/api", hx_target="#result")

    See Also:
        Bootstrap docs: https://getbootstrap.com/docs/5.3/components/[name]/
    """
    # Build classes
    classes = ["component-base", f"component-{variant}"]
    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes(" ".join(classes), user_cls)

    # Build attributes
    attrs: dict[str, Any] = {"cls": all_classes}
    attrs.update(_convert_attrs(kwargs))

    return Div(*children, **attrs)
```

### Test Requirements

Every component MUST have tests:

```python
"""Tests for ComponentName."""

from fasthtml.common import to_xml
from faststrap.components.category import ComponentName

def test_component_basic():
    """Component renders correctly."""
    comp = ComponentName("Test")
    html = to_xml(comp)
    assert "Test" in html
    assert "component-base" in html

def test_component_variants():
    """Component supports all variants."""
    for variant in ["primary", "secondary", "success"]:
        comp = ComponentName("Test", variant=variant)
        assert f"component-{variant}" in to_xml(comp)

def test_component_custom_classes():
    """Component merges custom classes."""
    comp = ComponentName("Test", cls="custom")
    html = to_xml(comp)
    assert "component-base" in html
    assert "custom" in html

def test_component_htmx():
    """Component supports HTMX."""
    comp = ComponentName("Load", hx_get="/api")
    assert 'hx-get="/api"' in to_xml(comp)
```

**CRITICAL:** Always use `to_xml(component)`, never `str(component)`.

---

## 🧪 Testing

### Running Tests

```bash
# All tests
pytest

# With coverage
pytest --cov=faststrap

# Specific file
pytest tests/test_components/test_button.py

# Specific test
pytest tests/test_components/test_button.py::test_button_variants

# Verbose mode
pytest -v

# Stop on first failure
pytest -x
```

### Writing Tests

- **Aim for 100% coverage** of new code
- **Test all variants/sizes/options**
- **Test HTMX attributes**
- **Test custom classes merge correctly**
- **Test edge cases** (empty content, multiple children)

---

## 📦 Building & Publishing

### Local Build

```bash
# Install build tools
pip install hatch

# Build wheel and sdist
hatch build

# Check distribution
ls -lh dist/
```

### Publishing (Maintainers Only)

1. **Update version** in git tag:
   ```bash
   git tag v0.3.0
   git push origin v0.3.0
   ```

2. **Create GitHub Release** - This triggers automatic PyPI publish

3. **Verify on PyPI**: https://pypi.org/project/faststrap/

---

## 📚 Documentation Guidelines

### Component Docstrings

```python
def Component(*children, variant="primary", **kwargs):
    """Short one-line description.

    Longer description explaining what the component does,
    when to use it, and any special behaviors.

    Args:
        *children: Child elements (text, HTML, other components)
        variant: Bootstrap color variant (primary, secondary, etc.)
        **kwargs: Additional HTML attributes (cls, id, hx-*, data-*, etc.)

    Returns:
        Div (or appropriate FastHTML element) with Bootstrap classes

    Example:
        Basic usage:
        >>> Component("Hello", variant="success")

        With HTMX:
        >>> Component("Load", hx_get="/api", hx_target="#result")

        Custom styling:
        >>> Component("Custom", cls="mt-3 shadow-lg")

    Note:
        Any important notes about Bootstrap JS requirements,
        accessibility concerns, or usage gotchas.

    See Also:
        Bootstrap docs: https://getbootstrap.com/docs/5.3/components/...
    """
```

### README Sections

When adding new components, update:

1. **Available Components** table
2. **Examples** section (if component is commonly used)
3. **CHANGELOG.md** under "Unreleased"

---

## 🎯 Component Checklist

Before submitting component PR:

- [ ] Component file in correct directory
- [ ] Uses Python 3.10+ type hints (`str | None`)
- [ ] Includes `_convert_attrs()` for HTMX support
- [ ] Uses `merge_classes()` for CSS
- [ ] Comprehensive docstring with examples
- [ ] Test file with 8+ tests
- [ ] All tests pass: `pytest`
- [ ] Type checks pass: `mypy src/faststrap`
- [ ] Code formatted: `black .` and `ruff check .`
- [ ] Exported in `__init__.py` files
- [ ] Updated CHANGELOG.md

---

## 🤝 Code Review Process

1. **Automated checks** run on every PR (tests, linting, type checks)
2. **Manual review** by maintainers (usually within 48 hours)
3. **Feedback/changes** requested if needed
4. **Approval & merge** once checks pass

### Review Criteria

We look for:
- ✅ Code follows existing patterns
- ✅ Tests cover new functionality
- ✅ Documentation is clear
- ✅ No breaking changes (or discussed if needed)
- ✅ Bootstrap conventions followed

---

## 💬 Getting Help

Stuck? We're here to help!

- **Questions**: [GitHub Discussions](https://github.com/Evayoung/Faststrap/discussions)
- **Bugs**: [GitHub Issues](https://github.com/Evayoung/Faststrap/issues)
- **Chat**: [FastHTML Discord](https://discord.gg/fasthtml)

---

## 📜 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for making FastStrap better! 🎉**
