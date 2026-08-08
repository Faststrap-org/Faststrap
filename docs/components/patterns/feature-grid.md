# FeatureGrid

`Feature` and `FeatureGrid` are landing-page pattern components for value propositions, product capabilities, and benefits sections. They provide a clean, consistent way to showcase features with icons, titles, and descriptions.

!!! tip "Bootstrap Reference"
    [Bootstrap 5 Grid](https://getbootstrap.com/docs/5.3/layout/grid/)

---

## Quick Start

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="row g-4">
      <div class="col-md-4">
        <div class="p-3 border rounded-3 h-100">
          <div class="mb-3"><i class="bi bi-lightning-charge text-primary fs-3"></i></div>
          <h4 class="mb-2">FastHTML native</h4>
          <p class="text-muted mb-0">Build Bootstrap interfaces directly from Python.</p>
        </div>
      </div>
      <div class="col-md-4">
        <div class="p-3 border rounded-3 h-100">
          <div class="mb-3"><i class="bi bi-arrow-repeat text-primary fs-3"></i></div>
          <h4 class="mb-2">HTMX ready</h4>
          <p class="text-muted mb-0">Use hx_* attributes without custom JavaScript.</p>
        </div>
      </div>
      <div class="col-md-4">
        <div class="p-3 border rounded-3 h-100">
          <div class="mb-3"><i class="bi bi-palette text-primary fs-3"></i></div>
          <h4 class="mb-2">Themeable</h4>
          <p class="text-muted mb-0">Stay aligned with Bootstrap and Faststrap themes.</p>
        </div>
      </div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
FeatureGrid(
    Feature(
        "FastHTML native",
        "Build Bootstrap interfaces directly from Python.",
        icon="lightning-charge",
    ),
    Feature(
        "HTMX ready",
        "Use hx_* attributes without custom JavaScript.",
        icon="arrow-repeat",
    ),
    Feature(
        "Themeable",
        "Stay aligned with Bootstrap and Faststrap themes.",
        icon="palette",
    ),
    columns=3,
)
```
  </div>
</div>

---

## Visual Examples & Use Cases

### 1. Three-Column Feature Grid

```python
FeatureGrid(
    Feature("Fast", "Server-rendered and blazing fast.", icon="lightning"),
    Feature("Simple", "Clean Python API, no React needed.", icon="check-circle"),
    Feature("Secure", "Built-in CSRF and XSS protection.", icon="shield-check"),
    columns=3,
)
```

### 2. Two-Column Feature Grid

```python
FeatureGrid(
    Feature("Open Source", "Free forever, MIT licensed.", icon="github"),
    Feature("Community", "Backed by Answer.AI and contributors.", icon="people"),
    columns=2,
)
```

### 3. Feature Grid with Custom Icons

```python
FeatureGrid(
    Feature(
        "Custom Icons",
        "Use any Bootstrap Icon or pass a custom element.",
        icon="gear",
        icon_cls="bg-success text-white",
    ),
    columns=3,
)
```

### 4. Dark Mode Feature Grid

```python
FeatureGrid(
    Feature("Dark Mode", "Built-in dark mode support.", icon="moon"),
    Feature("Responsive", "Mobile-first, works everywhere.", icon="phone"),
    columns=2,
    row_cls="text-white",
)
```

---

## Practical Functionality

### 1. Landing Page Hero

```python
LandingLayout(
    Hero(
        title="Build Faster with Python",
        subtitle="152+ UI components for FastHTML",
        cta_text="Get Started",
        cta_href="/docs",
    ),
    FeatureGrid(
        Feature("Fast", "Pure Python, zero JS knowledge.", icon="lightning"),
        Feature("Secure", "Server-rendered and safe.", icon="shield"),
        Feature("Simple", "Clean, composable API.", icon="code"),
        columns=3,
    ),
)
```

### 2. Feature Grid Inside a Card

```python
Card(
    Card.Header("Why Faststrap?"),
    Card.Body(
        FeatureGrid(
            Feature("Zero JS", "No JavaScript required for core components.", icon="slash-circle"),
            Feature("HTMX", "Progressive enhancement with HTMX.", icon="arrow-repeat"),
            columns=2,
        )
    ),
)
```

---

## Parameter Reference

### `Feature`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `title` | `str` | required | Feature title. |
| `description` | `str` | required | Supporting feature copy. |
| `icon` | `str \| Any \| None` | `None` | Bootstrap icon name or custom element. |
| `icon_cls` | `str` | `"bg-primary text-white"` | Classes for the icon wrapper. |
| `icon_wrapper_cls` | `str \| None` | `None` | Extra icon wrapper classes. |
| `title_cls` | `str` | `"fs-4 fw-bold"` | Title classes. |
| `description_cls` | `str` | `"text-muted"` | Description classes. |
| `icon_wrapper_attrs` | `dict \| None` | `None` | Extra icon wrapper attributes. |
| `title_attrs` | `dict \| None` | `None` | Extra title attributes. |
| `description_attrs` | `dict \| None` | `None` | Extra description attributes. |
| `**kwargs` | `Any` | `{}` | Extra root attributes. |

### `FeatureGrid`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `*features` | `Any` | required | Feature elements. |
| `columns` | `int` | `3` | Number of columns at the medium breakpoint. |
| `row_cls` | `str \| None` | `None` | Extra row classes. |
| `col_cls` | `str \| None` | `None` | Extra column classes. |
| `row_attrs` | `dict \| None` | `None` | Extra row attributes. |
| `col_attrs` | `dict \| None` | `None` | Extra column attributes. |
| `**kwargs` | `Any` | `{}` | Extra root attributes. |

---

## API Reference

::: faststrap.components.patterns.feature.Feature
    options:
        show_source: true
        heading_level: 4

::: faststrap.components.patterns.feature.FeatureGrid
    options:
        show_source: true
        heading_level: 4
