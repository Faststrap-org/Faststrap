# FastStrap Component Development Specification

**A guide for building standardized, high-quality components for FastStrap.**

Use this as a template when creating any new component. Every component should follow these patterns for consistency and maintainability.

---

## Component Checklist

Before submitting a component, ensure:

- [ ] Follows naming conventions (file, function, parameters)
- [ ] Includes complete type hints
- [ ] Has comprehensive docstring with examples
- [ ] Supports both kwargs and fluent API (if complex)
- [ ] Handles Bootstrap variants/sizes correctly
- [ ] Merges user classes properly
- [ ] Works with HTMX attributes
- [ ] Has corresponding test file with 100% coverage
- [ ] Includes usage example in docstring
- [ ] Exported in `__init__.py`

---

## Component Template

### File Location
```
src/faststrap/components/{category}/{component_name}.py
```

Categories:
- `layout/` - Containers, grids, stacks
- `display/` - Cards, badges, avatars
- `feedback/` - Alerts, toasts, modals
- `navigation/` - Navbars, tabs, drawers
- `forms/` - Buttons, inputs, selects
- `advanced/` - DataTables, charts, steppers

### Basic Component Structure

```python
"""Module docstring describing the component."""

from typing import Any, Literal, Optional, Union
from fasthtml.common import Div, Button, Span  # Import needed FT objects
from faststrap.core.base import merge_classes

# Type aliases for better documentation
VariantType = Literal["primary", "secondary", "success", "danger", "warning", "info", "light", "dark"]
SizeType = Literal["sm", "md", "lg"]


def ComponentName(
    *children: Any,
    variant: VariantType = "primary",
    size: SizeType = "md",
    disabled: bool = False,
    **kwargs: Any
) -> Div:  # or appropriate FT type
    """Short one-line description of component.
    
    Longer description explaining what the component does, when to use it,
    and any special behaviors. Mention Bootstrap version/docs if relevant.
    
    Args:
        *children: Child elements (text, HTML, other components)
        variant: Bootstrap color variant (primary, secondary, etc.)
        size: Component size (sm, md, lg)
        disabled: Whether component is disabled
        **kwargs: Additional HTML attributes (cls, id, hx-*, data-*, etc.)
    
    Returns:
        Div (or appropriate FastHTML FT object) with Bootstrap classes applied
    
    Example:
        Basic usage:
        >>> ComponentName("Hello World", variant="success")
        
        With HTMX:
        >>> ComponentName("Load", variant="primary", hx_get="/api", hx_target="#result")
        
        Custom styling:
        >>> ComponentName("Custom", cls="mt-3 shadow-lg", id="my-component")
    
    Note:
        Any important notes about Bootstrap JS requirements, accessibility,
        or breaking changes from standard Bootstrap.
    
    See Also:
        Bootstrap docs: https://getbootstrap.com/docs/5.3/components/...
    """
    # Build Bootstrap classes
    base_classes = [f"component-base", f"component-{variant}"]
    
    if size != "md":  # Don't add md since it's default
        base_classes.append(f"component-{size}")
    
    if disabled:
        base_classes.append("disabled")
    
    # Merge with user-provided classes
    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes(" ".join(base_classes), user_cls)
    
    # Build attributes
    attrs = {"cls": all_classes, **kwargs}
    
    if disabled:
        attrs["disabled"] = True
        attrs["aria_disabled"] = "true"
    
    # Build and return component
    return Div(*children, **attrs)
```

---

## Complex Component (Fluent API)

For components with many optional parts (like Card with header/body/footer):

```python
from faststrap.core.base import ComponentBuilder

class ComponentNameBuilder(ComponentBuilder):
    """Fluent builder for ComponentName with optional parts."""
    
    def __init__(self, *children: Any, **kwargs: Any):
        super().__init__(*children, **kwargs)
        self.header: Optional[Any] = None
        self.footer: Optional[Any] = None
        self.variant: str = kwargs.get("variant", "primary")
    
    def with_header(self, header: Any) -> "ComponentNameBuilder":
        """Add header to component.
        
        Args:
            header: Header content
        
        Returns:
            Self for chaining
        """
        self.header = header
        return self
    
    def with_footer(self, footer: Any) -> "ComponentNameBuilder":
        """Add footer to component.
        
        Args:
            footer: Footer content
        
        Returns:
            Self for chaining
        """
        self.footer = footer
        return self
    
    def build(self) -> Div:
        """Build the final component.
        
        Returns:
            Div with all parts assembled
        """
        parts = []
        
        if self.header:
            parts.append(Div(self.header, cls="component-header"))
        
        parts.append(Div(*self.children, cls="component-body"))
        
        if self.footer:
            parts.append(Div(self.footer, cls="component-footer"))
        
        classes = merge_classes(
            f"component component-{self.variant}",
            self.attrs.get("cls", "")
        )
        
        return Div(*parts, cls=classes, **self.attrs)


def ComponentName(
    *children: Any,
    header: Optional[Any] = None,
    footer: Optional[Any] = None,
    variant: str = "primary",
    **kwargs: Any
) -> Union[Div, ComponentNameBuilder]:
    """Component with optional header/footer.
    
    Supports both kwargs and fluent API:
    
    Kwargs style:
        ComponentName("Body", header="Title", footer="Footer")
    
    Fluent style:
        ComponentName("Body").with_header("Title").with_footer("Footer").build()
    
    Args:
        *children: Main content
        header: Optional header content
        footer: Optional footer content
        variant: Color variant
        **kwargs: Additional attributes
    
    Returns:
        Built Div or builder for chaining
    """
    builder = ComponentNameBuilder(*children, variant=variant, **kwargs)
    
    # If using kwargs, build immediately
    if header or footer:
        if header:
            builder.with_header(header)
        if footer:
            builder.with_footer(footer)
        return builder.build()
    
    # If only children provided, also build immediately
    if not kwargs.get("_fluent_mode"):
        return builder.build()
    
    # Otherwise return builder for chaining
    return builder
```

---

## Bootstrap-Specific Patterns

### 1. Variants (Colors)
```python
VariantType = Literal[
    "primary", "secondary", "success", "danger", 
    "warning", "info", "light", "dark", "link"
]

# Apply as: f"btn-{variant}" or f"alert-{variant}"
```

### 2. Sizes
```python
SizeType = Literal["sm", "md", "lg"]

# Only add class if not "md":
if size != "md":
    classes.append(f"btn-{size}")
```

### 3. Outline Variants
```python
def Button(..., outline: bool = False, ...):
    variant_class = f"btn-{'outline-' if outline else ''}{variant}"
```

### 4. Dismissible Elements
```python
def Alert(..., dismissible: bool = False, ...):
    if dismissible:
        attrs["data_bs_dismiss"] = "alert"
        # Add close button
        close_btn = Button(
            Span("×", aria_hidden="true"),
            cls="btn-close",
            data_bs_dismiss="alert",
            aria_label="Close"
        )
```

### 5. Loading States
```python
def Button(..., loading: bool = False, ...):
    content = list(children)
    if loading:
        attrs["disabled"] = True
        content.insert(0, Span(
            cls="spinner-border spinner-border-sm me-2",
            role="status",
            aria_hidden="true"
        ))
```

### 6. Icons (Bootstrap Icons)
```python
def Button(..., icon: Optional[str] = None, ...):
    content = list(children)
    if icon:
        content.insert(0, I(cls=f"bi bi-{icon} me-2"))
```

### 7. Accessibility
```python
# Always include ARIA attributes when needed
attrs["role"] = "alert"  # For alerts
attrs["aria_label"] = "Close"  # For close buttons
attrs["aria_hidden"] = "true"  # For decorative elements

# Add aria-live for dynamic updates
if dynamic:
    attrs["aria_live"] = "polite"
```

---

## Testing Template

Create `tests/test_components/test_{component_name}.py`:

```python
"""Tests for ComponentName component."""

import pytest
from fasthtml.common import Div
from faststrap.components.category import ComponentName


class TestComponentBasic:
    """Basic functionality tests."""
    
    def test_renders_correctly(self):
        """Component renders with correct HTML structure."""
        component = ComponentName("Test content")
        html = str(component)
        
        assert isinstance(component, Div)
        assert "Test content" in html
        assert "component-base" in html
    
    def test_default_variant(self):
        """Component uses default variant."""
        component = ComponentName("Test")
        html = str(component)
        assert "component-primary" in html


class TestComponentVariants:
    """Test color variants."""
    
    @pytest.mark.parametrize("variant", [
        "primary", "secondary", "success", "danger", 
        "warning", "info", "light", "dark"
    ])
    def test_variant(self, variant):
        """All variants render correctly."""
        component = ComponentName("Test", variant=variant)
        html = str(component)
        assert f"component-{variant}" in html


class TestComponentSizes:
    """Test size variations."""
    
    def test_small_size(self):
        component = ComponentName("Test", size="sm")
        assert "component-sm" in str(component)
    
    def test_medium_size_no_class(self):
        """Medium is default, shouldn't add class."""
        component = ComponentName("Test", size="md")
        assert "component-md" not in str(component)
    
    def test_large_size(self):
        component = ComponentName("Test", size="lg")
        assert "component-lg" in str(component)


class TestComponentCustomization:
    """Test customization options."""
    
    def test_custom_classes(self):
        """User classes are merged with Bootstrap classes."""
        component = ComponentName("Test", cls="mt-3 shadow")
        html = str(component)
        assert "mt-3" in html
        assert "shadow" in html
        assert "component-base" in html
    
    def test_custom_id(self):
        """Custom ID is applied."""
        component = ComponentName("Test", id="my-component")
        assert 'id="my-component"' in str(component)
    
    def test_data_attributes(self):
        """Data attributes work correctly."""
        component = ComponentName("Test", data_value="123")
        assert 'data-value="123"' in str(component)


class TestComponentHTMX:
    """Test HTMX integration."""
    
    def test_hx_get(self):
        component = ComponentName("Load", hx_get="/api")
        assert 'hx-get="/api"' in str(component)
    
    def test_hx_post_with_target(self):
        component = ComponentName(
            "Submit",
            hx_post="/save",
            hx_target="#result"
        )
        html = str(component)
        assert 'hx-post="/save"' in html
        assert 'hx-target="#result"' in html


class TestComponentAccessibility:
    """Test accessibility features."""
    
    def test_disabled_has_aria(self):
        component = ComponentName("Test", disabled=True)
        html = str(component)
        assert "disabled" in html
        assert 'aria-disabled="true"' in html


class TestComponentEdgeCases:
    """Test edge cases and error conditions."""
    
    def test_empty_children(self):
        """Component works with no children."""
        component = ComponentName()
        assert isinstance(component, Div)
    
    def test_multiple_children(self):
        """Component accepts multiple children."""
        component = ComponentName("First", "Second", "Third")
        html = str(component)
        assert "First" in html
        assert "Second" in html
        assert "Third" in html
    
    def test_nested_components(self):
        """Components can be nested."""
        inner = ComponentName("Inner")
        outer = ComponentName(inner, variant="secondary")
        html = str(outer)
        assert "Inner" in html
        assert "component-secondary" in html


# If component has fluent API
class TestComponentFluentAPI:
    """Test fluent/builder pattern."""
    
    def test_fluent_chaining(self):
        """Fluent API allows method chaining."""
        component = ComponentName("Body") \
            .with_header("Title") \
            .with_footer("Footer") \
            .build()
        
        html = str(component)
        assert "Title" in html
        assert "Body" in html
        assert "Footer" in html
    
    def test_fluent_vs_kwargs_equivalent(self):
        """Fluent and kwargs produce same result."""
        fluent = ComponentName("Body") \
            .with_header("Title") \
            .build()
        
        kwargs = ComponentName("Body", header="Title")
        
        # Should produce equivalent HTML
        assert "Title" in str(fluent)
        assert "Body" in str(fluent)
        assert "Title" in str(kwargs)
        assert "Body" in str(kwargs)
```

---

## Documentation Template

Add to component docstring:

```python
"""
Component description.

Examples:
    Basic usage:
        >>> from faststrap import ComponentName
        >>> ComponentName("Hello", variant="success")
    
    With HTMX for dynamic updates:
        >>> ComponentName(
        ...     "Load More",
        ...     hx_get="/api/items",
        ...     hx_target="#items",
        ...     hx_swap="beforeend"
        ... )
    
    Fluent API for complex compositions:
        >>> ComponentName("Content") \\
        ...     .with_header("Title") \\
        ...     .with_footer(Button("Action")) \\
        ...     .build()
    
    Accessibility:
        >>> ComponentName(
        ...     "Important message",
        ...     role="alert",
        ...     aria_live="polite"
        ... )

Bootstrap Reference:
    https://getbootstrap.com/docs/5.3/components/component-name/

Args:
    *children: Component content
    variant: Bootstrap color variant
    size: Component size
    **kwargs: Additional HTML attributes

Returns:
    FastHTML Div element with Bootstrap classes

Note:
    Any special considerations, Bootstrap JS requirements, or
    accessibility concerns.
"""
```

---

## Naming Conventions

### File Names
- Snake case: `button.py`, `button_group.py`, `data_table.py`
- One component per file (unless tightly coupled, like ButtonGroup + Button)

### Function Names
- Pascal case: `Button()`, `Card()`, `DataTable()`
- Match Bootstrap component names when possible

### Parameter Names
- Snake case: `variant`, `size`, `disabled`, `hx_get`
- HTMX: `hx_get`, `hx_post` (underscores, not hyphens)
- Data: `data_value`, `data_bs_toggle` (underscores)
- ARIA: `aria_label`, `aria_hidden` (underscores)

### Type Aliases
- Suffix with "Type": `VariantType`, `SizeType`
- Use Literal for enums

---

## Common Mistakes to Avoid

1. ❌ **Forgetting to handle user classes**
   ```python
   # Wrong - overwrites user classes
   return Div(*children, cls="component-base", **kwargs)
   
   # Right - merges classes
   cls = merge_classes("component-base", kwargs.pop("cls", ""))
   return Div(*children, cls=cls, **kwargs)
   ```

2. ❌ **Not supporting HTMX attributes**
   ```python
   # Wrong - HTMX attrs won't work
   def Component(*children): ...
   
   # Right - accept **kwargs
   def Component(*children, **kwargs): ...
   ```

3. ❌ **Missing type hints**
   ```python
   # Wrong
   def Component(variant="primary"):
   
   # Right
   def Component(variant: Literal["primary", "secondary"] = "primary"):
   ```

4. ❌ **Adding "md" size class**
   ```python
   # Wrong - unnecessary class
   classes.append(f"btn-{size}")
   
   # Right - only for non-default sizes
   if size != "md":
       classes.append(f"btn-{size}")
   ```

5. ❌ **Returning builder instead of built component**
   ```python
   # Wrong - returns builder object
   return ComponentNameBuilder(*children)
   
   # Right - returns built Div
   return ComponentNameBuilder(*children).build()
   ```

---

## Component Priority List

Build in this order (easiest to hardest):

### Phase 1 (Foundation)
1. Button - Simplest, validates base patterns
2. Badge - Single element, easy
3. Alert - Dismissible, good for JS interaction
4. Card - Multi-part, tests fluent API
5. Container/Row/Col - Layout fundamentals

### Phase 2 (Interactive)
6. Toast - Bootstrap JS, auto-dismiss
7. Modal - Complex JS, backdrop
8. Drawer (Offcanvas) - Similar to Modal
9. Navbar - Complex structure, responsive
10. ButtonGroup - Composition pattern

### Phase 3 (Forms)
11. Input - Text, email, password variants
12. Select - Dropdown logic
13. Checkbox/Radio - Multiple choices
14. Switch - Toggle pattern
15. Form validation helpers

### Phase 4 (Advanced)
16. Tabs - State management
17. Accordion - Collapsible panels
18. DataTable - Sorting, filtering, pagination
19. Stepper - Multi-step forms
20. Charts - External library integration

---

## Ready to Build?

Use this spec for ANY component. The patterns are consistent, so once you build one, the rest follow naturally.

**Next step**: Pick a component from the priority list and create it following this template!