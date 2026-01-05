# Accordion

The `Accordion` component creates vertically collapsible panels perfect for FAQs, settings, and organizing large amounts of content in a compact space. Users can expand/collapse sections to focus on what matters.

!!! success "Goal"
    Master creating accordion panels, understand Bootstrap collapse classes, and build organized, space-efficient interfaces that improve content discoverability.

!!! tip "Bootstrap Reference"
    [Bootstrap 5 Accordion Documentation](https://getbootstrap.com/docs/5.3/components/accordion/)

---

## Quick Start

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="accordion" id="accordionExample">
      <div class="accordion-item">
        <h2 class="accordion-header">
          <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne">
            Section 1
          </button>
        </h2>
        <div id="collapseOne" class="accordion-collapse collapse show" data-bs-parent="#accordionExample">
          <div class="accordion-body">
            Content for section 1
          </div>
        </div>
      </div>
      <div class="accordion-item">
        <h2 class="accordion-header">
          <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTwo">
            Section 2
          </button>
        </h2>
        <div id="collapseTwo" class="accordion-collapse collapse" data-bs-parent="#accordionExample">
          <div class="accordion-body">
            Content for section 2
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
from faststrap import Accordion, AccordionItem

Accordion(
    AccordionItem("Content for section 1", title="Section 1", expanded=True),
    AccordionItem("Content for section 2", title="Section 2")
)
```
  </div>
</div>

---

## Visual Examples & Use Cases

### 1. FAQ Accordion - Classic Use Case

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="accordion">
      <div class="accordion-item">
        <h2 class="accordion-header">
          <button class="accordion-button" type="button">
            How do I get started?
          </button>
        </h2>
        <div class="accordion-collapse collapse show">
          <div class="accordion-body">
            Simply install Faststrap with <code>pip install faststrap</code> and follow our quick start guide.
          </div>
        </div>
      </div>
      <div class="accordion-item">
        <h2 class="accordion-header">
          <button class="accordion-button collapsed" type="button">
            Is it free to use?
          </button>
        </h2>
        <div class="accordion-collapse collapse">
          <div class="accordion-body">
            Yes! Faststrap is completely free and open-source under the MIT license.
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
Accordion(
    AccordionItem(
        "Simply install Faststrap with pip install faststrap and follow our quick start guide.",
        title="How do I get started?",
        expanded=True
    ),
    AccordionItem(
        "Yes! Faststrap is completely free and open-source under the MIT license.",
        title="Is it free to use?"
    )
)
```
  </div>
</div>

---

### 2. Flush Accordion - Edge-to-Edge Design

Remove borders for a cleaner, edge-to-edge look.

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="accordion accordion-flush">
      <div class="accordion-item">
        <h2 class="accordion-header">
          <button class="accordion-button collapsed" type="button">
            Account Settings
          </button>
        </h2>
        <div class="accordion-collapse collapse">
          <div class="accordion-body">
            Manage your account preferences here.
          </div>
        </div>
      </div>
      <div class="accordion-item">
        <h2 class="accordion-header">
          <button class="accordion-button collapsed" type="button">
            Privacy Settings
          </button>
        </h2>
        <div class="accordion-collapse collapse">
          <div class="accordion-body">
            Control your privacy options.
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
Accordion(
    AccordionItem("Manage your account preferences here.", title="Account Settings"),
    AccordionItem("Control your privacy options.", title="Privacy Settings"),
    flush=True  # ← Removes borders and backgrounds
)
```
  </div>
</div>

---

### 3. Always Open - Multiple Panels Expanded

Allow multiple panels to be open simultaneously.

```python
Accordion(
    AccordionItem(
        "Personal information form fields...",
        title="Personal Information",
        expanded=True
    ),
    AccordionItem(
        "Address form fields...",
        title="Address",
        expanded=True
    ),
    AccordionItem(
        "Payment form fields...",
        title="Payment Details"
    ),
    always_open=True  # ← Multiple panels can be open
)
```

**When to use `always_open`:**
- ✅ Multi-step forms where users need to see multiple sections
- ✅ Comparison views
- ✅ Settings pages with independent sections
- ❌ FAQs (better to close previous when opening new)

---

### 4. Custom Styling - Branded Accordions

```python
from faststrap import Accordion, AccordionItem, Icon

Accordion(
    AccordionItem(
        "Premium features include priority support, advanced analytics, and custom branding.",
        title=Div(Icon("star-fill", cls="text-warning me-2"), "Premium Features"),
        header_cls="bg-primary text-white",
        body_cls="bg-light"
    ),
    AccordionItem(
        "Standard features include all core components and community support.",
        title=Div(Icon("check-circle", cls="text-success me-2"), "Standard Features"),
        header_cls="bg-secondary text-white",
        body_cls="bg-light"
    )
)
```

---

## Practical Functionality

### Product Details Accordion

```python
from faststrap import Accordion, AccordionItem, Table

def ProductDetailsAccordion(product):
    return Accordion(
        AccordionItem(
            product.description,
            title="Description",
            expanded=True
        ),
        AccordionItem(
            Table(
                TBody(
                    Tr(Td("Material"), Td(product.material)),
                    Tr(Td("Weight"), Td(f"{product.weight} kg")),
                    Tr(Td("Dimensions"), Td(product.dimensions)),
                    Tr(Td("Color"), Td(product.color))
                )
            ),
            title="Specifications"
        ),
        AccordionItem(
            Div(*[review_card(r) for r in product.reviews]),
            title=f"Reviews ({len(product.reviews)})"
        ),
        AccordionItem(
            "Ships within 2-3 business days. Free shipping on orders over $50.",
            title="Shipping Information"
        ),
        flush=True
    )
```

---

### Settings Panel Accordion

```python
from faststrap import Accordion, AccordionItem, Switch, Select, Button

def SettingsAccordion():
    return Accordion(
        AccordionItem(
            Div(
                Switch("notifications", label="Email Notifications"),
                Switch("marketing", label="Marketing Emails"),
                Switch("updates", label="Product Updates"),
                cls="d-flex flex-column gap-2"
            ),
            title="Notifications",
            expanded=True
        ),
        AccordionItem(
            Div(
                Select(
                    "theme",
                    ("light", "Light"),
                    ("dark", "Dark"),
                    ("auto", "Auto"),
                    label="Theme"
                ),
                Select(
                    "language",
                    ("en", "English"),
                    ("es", "Spanish"),
                    ("fr", "French"),
                    label="Language"
                )
            ),
            title="Appearance"
        ),
        AccordionItem(
            Div(
                Button("Change Password", variant="primary", cls="mb-2"),
                Button("Enable 2FA", variant="outline-secondary", cls="mb-2"),
                Button("Delete Account", variant="danger")
            ),
            title="Security"
        ),
        always_open=True
    )
```

---

## Bootstrap CSS Classes Explained

### Core Accordion Classes

| Class | Purpose | Applied To |
|-------|---------|------------|
| `.accordion` | **Container** - Wraps all items | `<div>` wrapper |
| `.accordion-flush` | **Flush style** - Removes borders/backgrounds | `.accordion` container |
| `.accordion-item` | **Item wrapper** - Individual panel | Each panel `<div>` |
| `.accordion-header` | **Header** - Clickable title area | `<h2>` element |
| `.accordion-button` | **Toggle button** - Expand/collapse trigger | `<button>` element |
| `.accordion-button.collapsed` | **Collapsed state** - Panel is closed | `<button>` when closed |
| `.accordion-collapse` | **Content wrapper** - Collapsible area | `<div>` for content |
| `.accordion-body` | **Body** - Actual content | `<div>` inside collapse |
| `.collapse` | **Collapse behavior** - Bootstrap collapse plugin | Content wrapper |
| `.collapse.show` | **Expanded state** - Panel is open | When expanded |

### Data Attributes

| Attribute | Purpose | Value |
|-----------|---------|-------|
| `data-bs-toggle="collapse"` | **Enable collapse** - Activates collapse behavior | Always "collapse" |
| `data-bs-target="#id"` | **Target panel** - Which panel to toggle | ID of collapse div |
| `data-bs-parent="#id"` | **Parent accordion** - Close others when opening | ID of accordion (omit for always_open) |
| `aria-expanded` | **Accessibility** - Indicates expanded state | "true" or "false" |
| `aria-controls` | **Accessibility** - Links button to content | ID of collapse div |

---

## Responsive Accordion Patterns

### Mobile-Optimized Accordions

```python
from faststrap import Accordion, AccordionItem

# Flush style works great on mobile
Accordion(
    AccordionItem("Content 1", title="Section 1"),
    AccordionItem("Content 2", title="Section 2"),
    AccordionItem("Content 3", title="Section 3"),
    flush=True,  # ← Better for mobile (edge-to-edge)
    cls="mb-4"
)
```

---

## Core Faststrap Features

### Global Defaults with `set_component_defaults`

```python
from faststrap import set_component_defaults, Accordion

# All accordions flush style by default
set_component_defaults("Accordion", flush=True)

# Now all accordions inherit flush style
Accordion(
    AccordionItem("Content", title="Section")
)  # ← Automatically flush=True

# Override when needed
Accordion(
    AccordionItem("Content", title="Section"),
    flush=False  # ← Explicitly override
)
```

---

## Common Recipes

### The "Expandable Table Rows" Pattern

Use accordions for expandable details in tables.

```python
def ExpandableOrderRow(order):
    return Accordion(
        AccordionItem(
            Div(
                H5("Order Details"),
                Table(
                    TBody(
                        *[Tr(Td(item.name), Td(item.quantity), Td(f"${item.price}"))
                          for item in order.items]
                    )
                ),
                Div(
                    Strong("Total: "),
                    f"${order.total}",
                    cls="mt-2"
                )
            ),
            title=f"Order #{order.id} - {order.date}",
            header_cls="bg-light"
        ),
        flush=True
    )
```

---

### The "Nested Accordion" Pattern

Create hierarchical content structures.

```python
Accordion(
    AccordionItem(
        Accordion(
            AccordionItem("Sub-content 1", title="Sub-section 1"),
            AccordionItem("Sub-content 2", title="Sub-section 2"),
            flush=True
        ),
        title="Main Section 1"
    ),
    AccordionItem(
        "Regular content",
        title="Main Section 2"
    )
)
```

---

## Accessibility Best Practices

Faststrap automatically handles accessibility:

✅ **Automatic Features:**
- Semantic `<h2>` headers for each panel
- `<button>` elements for toggles (keyboard accessible)
- `aria-expanded` indicates open/closed state
- `aria-controls` links button to content
- `aria-labelledby` links content to header
- Unique IDs auto-generated

**Manual Enhancements:**

```python
Accordion(
    AccordionItem("Content", title="Section"),
    accordion_id="custom-accordion",  # Custom ID for programmatic control
    aria_label="FAQ accordion"  # Additional context
)
```

---

## Parameter Reference

### Accordion

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `*children` | `AccordionItem` | Required | Accordion items |
| `accordion_id` | `str \| None` | Auto-generated | Unique ID for accordion |
| `flush` | `bool` | `False` | Remove borders/backgrounds |
| `always_open` | `bool` | `False` | Allow multiple panels open |
| `**kwargs` | `Any` | - | Additional HTML attributes (cls, id) |

### AccordionItem

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `*children` | `Any` | Required | Panel content |
| `title` | `str` | `""` | Header text |
| `expanded` | `bool` | `False` | Initially expanded |
| `header_cls` | `str` | `""` | Additional header classes |
| `body_cls` | `str` | `""` | Additional body classes |
| `button_cls` | `str` | `""` | Additional button classes |
| `**kwargs` | `Any` | - | Additional HTML attributes |

::: faststrap.components.navigation.accordion.Accordion
    options:
        show_source: true
        heading_level: 4

::: faststrap.components.navigation.accordion.AccordionItem
    options:
        show_source: true
        heading_level: 4
