# Select

The `Select` component creates beautiful dropdown selection menus with full Bootstrap styling, validation support, and HTMX integration. Perfect for forms, filters, and any situation where users need to choose from a list of options.

!!! success "Goal"
    By the end of this guide, you'll master creating single and multi-select dropdowns, understand Bootstrap form classes, and build dynamic, responsive selection interfaces—all in pure Python.

---

## Quick Start

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="mb-3">
      <label for="country" class="form-label">Country</label>
      <select class="form-select" id="country" name="country">
        <option value="us">United States</option>
        <option value="uk">United Kingdom</option>
        <option value="ca">Canada</option>
        <option value="au">Australia</option>
      </select>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
from faststrap import Select

Select(
    "country",
    ("us", "United States"),
    ("uk", "United Kingdom"),
    ("ca", "Canada"),
    ("au", "Australia"),
    label="Country"
)
```
  </div>
</div>

---

## Visual Examples & Use Cases

### 1. Sizes - Match Your Design

Bootstrap provides three sizes for select elements. Use larger selects for important choices, smaller ones for compact interfaces.

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="mb-3">
      <label class="form-label">Large Select</label>
      <select class="form-select form-select-lg">
        <option>Choose an option...</option>
        <option>Option 1</option>
        <option>Option 2</option>
      </select>
    </div>
    <div class="mb-3">
      <label class="form-label">Default Select</label>
      <select class="form-select">
        <option>Choose an option...</option>
        <option>Option 1</option>
        <option>Option 2</option>
      </select>
    </div>
    <div class="mb-3">
      <label class="form-label">Small Select</label>
      <select class="form-select form-select-sm">
        <option>Choose an option...</option>
        <option>Option 1</option>
        <option>Option 2</option>
      </select>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
# Large - for prominent selections
Select("priority", ("high", "High"), ("medium", "Medium"), 
       label="Priority Level", size="lg")

# Default - standard forms
Select("category", ("tech", "Technology"), ("design", "Design"),
       label="Category")

# Small - compact interfaces, tables
Select("status", ("active", "Active"), ("inactive", "Inactive"),
       label="Status", size="sm")
```
  </div>
</div>

**When to use each size:**

| Size | Bootstrap Class | Use Case |
|------|----------------|----------|
| `lg` | `.form-select-lg` | Hero sections, primary filters, mobile-friendly forms |
| Default | `.form-select` | Standard forms, most use cases |
| `sm` | `.form-select-sm` | Data tables, compact toolbars, secondary filters |

---

### 2. Multiple Selection

Allow users to select multiple options by holding Ctrl/Cmd. Perfect for tags, categories, or multi-criteria filters.

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="mb-3">
      <label for="skills" class="form-label">Skills <small class="text-muted">(Hold Ctrl/Cmd to select multiple)</small></label>
      <select class="form-select" id="skills" name="skills" multiple size="5">
        <option value="python">Python</option>
        <option value="javascript">JavaScript</option>
        <option value="html">HTML/CSS</option>
        <option value="sql">SQL</option>
        <option value="docker">Docker</option>
      </select>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
Select(
    "skills",
    ("python", "Python"),
    ("javascript", "JavaScript"),
    ("html", "HTML/CSS"),
    ("sql", "SQL"),
    ("docker", "Docker"),
    label="Skills",
    help_text="Hold Ctrl/Cmd to select multiple",
    multiple=True
)
```
  </div>
</div>

---

### 3. Pre-selected Options

Set default selections using a third parameter in the option tuple.

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="mb-3">
      <label for="theme" class="form-label">Theme Preference</label>
      <select class="form-select" id="theme" name="theme">
        <option value="light">Light Mode</option>
        <option value="dark" selected>Dark Mode</option>
        <option value="auto">Auto (System)</option>
      </select>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
Select(
    "theme",
    ("light", "Light Mode"),
    ("dark", "Dark Mode", True),  # ← Pre-selected
    ("auto", "Auto (System)"),
    label="Theme Preference"
)
```
  </div>
</div>

---

### 4. Validation States

Show success, error, or warning states with Bootstrap's validation classes.

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="mb-3">
      <label for="valid-select" class="form-label">Valid Selection</label>
      <select class="form-select is-valid" id="valid-select">
        <option>Premium Plan</option>
      </select>
      <div class="valid-feedback">Great choice!</div>
    </div>
    <div class="mb-3">
      <label for="invalid-select" class="form-label">Invalid Selection <span class="text-danger">*</span></label>
      <select class="form-select is-invalid" id="invalid-select" required>
        <option value="">Choose...</option>
        <option>Option 1</option>
      </select>
      <div class="invalid-feedback">Please select an option.</div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
# Valid state
Select(
    "plan",
    ("premium", "Premium Plan", True),
    label="Valid Selection",
    cls="is-valid"
)

# Invalid state (requires custom feedback div)
from fasthtml.common import Div

Div(
    Select(
        "required_field",
        ("", "Choose..."),
        ("opt1", "Option 1"),
        label="Invalid Selection",
        required=True,
        cls="is-invalid"
    ),
    Div("Please select an option.", cls="invalid-feedback")
)
```
  </div>
</div>

---

## Practical Functionality

### HTMX Integration - Dynamic Filtering

Use HTMX to update content when selection changes, perfect for filters and dependent dropdowns.

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="card shadow-sm">
      <div class="card-body">
        <div class="mb-3">
          <label for="category-filter" class="form-label">Filter by Category</label>
          <select class="form-select" id="category-filter" name="category">
            <option value="all">All Categories</option>
            <option value="tech">Technology</option>
            <option value="design">Design</option>
            <option value="business">Business</option>
          </select>
        </div>
        <div id="results" class="alert alert-info">
          Select a category to filter results...
        </div>
      </div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
from faststrap import Select, Card

@app.get("/")
def home():
    return Card(
        Select(
            "category",
            ("all", "All Categories"),
            ("tech", "Technology"),
            ("design", "Design"),
            ("business", "Business"),
            label="Filter by Category",
            hx_get="/filter",           # ← Trigger on change
            hx_target="#results",       # ← Update this element
            hx_trigger="change"         # ← When user selects
        ),
        Div(id="results", cls="alert alert-info")
    )

@app.get("/filter")
def filter_results(category: str):
    # Your filtering logic here
    return Div(f"Showing {category} results...", cls="alert alert-success")
```
  </div>
</div>

---

### Dependent Dropdowns

Create cascading selects where one selection determines the options in another.

```python
@app.get("/")
def home():
    return Div(
        Select(
            "country",
            ("us", "United States"),
            ("uk", "United Kingdom"),
            ("ca", "Canada"),
            label="Country",
            hx_get="/cities",
            hx_target="#city-select",
            hx_trigger="change"
        ),
        Div(id="city-select"),  # Cities will load here
        cls="container my-4"
    )

@app.get("/cities")
def get_cities(country: str):
    cities = {
        "us": [("nyc", "New York"), ("la", "Los Angeles"), ("chi", "Chicago")],
        "uk": [("lon", "London"), ("man", "Manchester"), ("bir", "Birmingham")],
        "ca": [("tor", "Toronto"), ("van", "Vancouver"), ("mon", "Montreal")]
    }
    
    return Select(
        "city",
        *cities.get(country, []),
        label="City"
    )
```

---

## Bootstrap CSS Classes Explained

Understanding Bootstrap's select classes helps you customize and troubleshoot your forms.

### Core Classes

| Class | Purpose | When to Use |
|-------|---------|-------------|
| `.form-select` | **Base class** - Applies Bootstrap styling to `<select>` | Always use on select elements |
| `.form-select-lg` | **Large size** - Increases padding and font size | Important selections, mobile-friendly forms |
| `.form-select-sm` | **Small size** - Reduces padding and font size | Compact interfaces, data tables |
| `.form-label` | **Label styling** - Consistent label appearance | Always use on `<label>` elements |
| `.form-text` | **Help text** - Muted, smaller text below inputs | Provide hints or instructions |
| `.mb-3` | **Margin bottom** - Adds spacing between form groups | Wrap each select in a div with this class |

### Validation Classes

| Class | Purpose | Visual Effect |
|-------|---------|---------------|
| `.is-valid` | Indicates valid input | Green border, checkmark icon |
| `.is-invalid` | Indicates invalid input | Red border, X icon |
| `.valid-feedback` | Success message container | Green text below select |
| `.invalid-feedback` | Error message container | Red text below select |

### State Classes

| Class | Purpose | Effect |
|-------|---------|--------|
| `disabled` | Disables interaction | Grayed out, not clickable |
| `required` | Marks as required field | Browser validation, asterisk in label |
| `multiple` | Allows multiple selections | Shows multiple options, scrollable |

---

## Responsive Design with Bootstrap

Make your selects work beautifully on all screen sizes using Bootstrap's grid system.

```python
from faststrap import Container, Row, Col, Select

Container(
    Row(
        # Full width on mobile, half width on tablets+
        Col(
            Select(
                "first_name",
                ("mr", "Mr."), ("ms", "Ms."), ("dr", "Dr."),
                label="Title"
            ),
            cols=12,  # 100% width on mobile
            md=6      # 50% width on tablets and up
        ),
        Col(
            Select(
                "country",
                ("us", "USA"), ("uk", "UK"), ("ca", "Canada"),
                label="Country"
            ),
            cols=12,
            md=6
        )
    )
)
```

**Bootstrap Grid Classes:**

| Class | Breakpoint | Screen Width | Usage |
|-------|-----------|--------------|-------|
| `.col-{n}` | All | Any size | Base column width (1-12) |
| `.col-sm-{n}` | Small | ≥576px | Phone landscape |
| `.col-md-{n}` | Medium | ≥768px | Tablets |
| `.col-lg-{n}` | Large | ≥992px | Desktops |
| `.col-xl-{n}` | Extra Large | ≥1200px | Large desktops |

---

## Core Faststrap Features

### Global Defaults with `set_component_defaults`

Set default properties for all Select components in your app. Perfect for consistent styling across your application.

```python
from faststrap import set_component_defaults, Select

# Set defaults for all selects
set_component_defaults("Select", size="lg", required=True)

# Now all selects are large and required by default
Select("country", ("us", "USA"), ("uk", "UK"), label="Country")
# ↑ Automatically has size="lg" and required=True

# Override defaults when needed
Select("optional_field", ("a", "A"), ("b", "B"), 
       label="Optional", required=False)
# ↑ Explicitly set required=False to override
```

**Common Default Patterns:**

```python
# Admin panels - large, prominent selects
set_component_defaults("Select", size="lg")

# Data tables - compact selects
set_component_defaults("Select", size="sm")

# Forms - all fields required by default
set_component_defaults("Select", required=True)
```

---

## Common Recipes

### The "Please Select" Pattern

Add a placeholder option that forces users to make an active choice.

```python
Select(
    "plan",
    ("", "-- Please Select --"),  # Empty value
    ("basic", "Basic - $9/mo"),
    ("pro", "Pro - $29/mo"),
    ("enterprise", "Enterprise - Custom"),
    label="Choose Your Plan",
    required=True
)
```

### Grouped Options (Optgroups)

Organize related options into groups for better usability.

```python
from fasthtml.common import Select as FTSelect, OptGroup, Option

FTSelect(
    OptGroup(
        Option("New York", value="ny"),
        Option("Los Angeles", value="la"),
        label="Popular Cities"
    ),
    OptGroup(
        Option("Chicago", value="chi"),
        Option("Houston", value="hou"),
        Option("Phoenix", value="phx"),
        label="Other Cities"
    ),
    cls="form-select",
    name="city"
)
```

### Search Filter Select

Combine with a search input for filtering long lists.

```python
from faststrap import Input, Select, Card

Card(
    Input(
        "search",
        placeholder="Search countries...",
        hx_get="/search-countries",
        hx_target="#country-select",
        hx_trigger="keyup changed delay:300ms"
    ),
    Div(
        Select(
            "country",
            *[(code, name) for code, name in ALL_COUNTRIES],
            label="Country"
        ),
        id="country-select"
    ),
    header="Select Country"
)
```

---

## Accessibility Best Practices

Faststrap automatically handles accessibility, but here's what's happening under the hood:

✅ **Automatic Features:**
- Labels linked to selects via `for` and `id` attributes
- Required fields marked with `*` and `required` attribute
- Help text linked via `aria-describedby`
- Semantic HTML5 `<select>` elements

**Manual Enhancements:**

```python
Select(
    "language",
    ("en", "English"),
    ("es", "Spanish"),
    ("fr", "French"),
    label="Preferred Language",
    aria_label="Choose your preferred language",  # Screen reader description
    aria_required="true",                         # Explicitly mark as required
    help_text="This will be used for all communications"
)
```

---

## Parameter Reference

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `name` | `str` | Required | Form field name attribute |
| `*options` | `tuple` | Required | Options as `(value, label)` or `(value, label, selected)` |
| `label` | `str \| None` | `None` | Label text above select |
| `help_text` | `str \| None` | `None` | Helper text below select |
| `size` | `"sm" \| "lg" \| None` | `None` | Select size (default is medium) |
| `disabled` | `bool \| None` | `None` | Whether select is disabled |
| `required` | `bool \| None` | `None` | Whether select is required |
| `multiple` | `bool \| None` | `None` | Allow multiple selections |
| `cls` | `str` | `""` | Additional CSS classes |
| `**kwargs` | `Any` | - | Additional HTML attributes (id, hx-*, data-*, aria-*) |

::: faststrap.components.forms.select.Select
    options:
        show_source: true
        heading_level: 4
