# Navbar

The `Navbar` is a responsive meta-component that serves as a navigation header for your application. It supports branding, links, dropdowns, and forms (like search).

!!! tip "Bootstrap Reference"
    [Bootstrap 5 Navbar](https://getbootstrap.com/docs/5.3/components/navbar/)

---

## Quick Start

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render p-0">
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary w-100 px-3">
      <a class="navbar-brand" href="#">🚀 FastStrap</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#nav01">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="nav01">
        <ul class="navbar-nav me-auto">
          <li class="nav-item"><a class="nav-link active" href="#">Home</a></li>
          <li class="nav-item"><a class="nav-link" href="#">Docs</a></li>
          <li class="nav-item"><a class="nav-link" href="#">Pricing</a></li>
        </ul>
      </div>
    </nav>
  </div>
  <div class="preview-code" markdown>
```python
Navbar(
    NavbarBrand("🚀 FastStrap", href="/"),
    NavItem("Home", href="/"),
    NavItem("Docs", href="/docs"),
    NavItem("Pricing", href="/pricing"),
    expand="lg",
    variant="dark",
    bg_variant="primary"
)
```
  </div>
</div>

---

## Visual Examples & Use Cases

### 1. Positioning & Sticky
Keep the navigation visible while scrolling using `sticky="top"` or `fixed="top"`.

```python
Navbar(..., sticky="top") # Pushes content down
Navbar(..., fixed="top")  # Floats over content
```

### 2. Dark vs Light Themes
Match your application's aesthetic.

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render p-0 flex-column overflow-hidden">
    <!-- Dark Navbar -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary w-100 px-3 border-bottom border-white-50">
      <a class="navbar-brand" href="#">Dark Brand</a>
    </nav>
    <!-- Light Navbar -->
    <nav class="navbar navbar-expand-lg navbar-light bg-light w-100 px-3">
      <a class="navbar-brand" href="#">Light Brand</a>
    </nav>
  </div>
  <div class="preview-code" markdown>
```python
# Dark brand: Primary background, light text
Navbar(NavbarBrand("Dark Brand"), variant="dark", bg_variant="primary")

# Light brand: Light background, dark text
Navbar(NavbarBrand("Light Brand"), variant="light", bg_variant="light")
```
  </div>
</div>

### 3. Adding a Search Form
Navbars are common places for search inputs.

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render p-0">
    <nav class="navbar navbar-expand-md navbar-light bg-light w-100 px-3">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">My App</a>
        <form class="d-flex" role="search">
          <input class="form-control form-control-sm me-2" type="search" placeholder="Search...">
          <button class="btn btn-sm btn-outline-success" type="submit">Search</button>
        </form>
      </div>
    </nav>
  </div>
  <div class="preview-code" markdown>
```python
Navbar(
    NavbarBrand("My App"),
    Form(
        Input("search", placeholder="Search...", size="sm", cls="me-2"),
        Button("Search", variant="outline-success", size="sm"),
        cls="d-flex"
    ),
    expand="md"
)
```
  </div>
</div>

---

## Technical Hierarchy (LLM Spec)

To build a correct Navbar, follow this nested structure:

1.  **Navbar** (Main Container)
    *   **Container** (Optional, for centered alignment)
        *   **NavbarBrand** (Text or Logo)
        *   **NavbarToggler** (Created automatically if `expand` is set)
        *   **NavbarCollapse** (Parent for menu items)
            *   **NavItem** (Single Link)
            *   **Dropdown** (Grouped Links)

---

## Parameter Reference

| FastStrap Param | Type | Bootstrap Class | Description |
| :--- | :--- | :--- | :--- |
| `expand` | `str` | `.navbar-expand-{val}` | Responsive breakpoint: `sm`, `md`, `lg`, `xl`. |
| `variant` | `str` | `.navbar-{variant}` | Text contrast: `light` (dark text) or `dark` (light text). |
| `bg_variant` | `str` | `.bg-{variant}` | Background color (e.g., `primary`, `white`). |
| `sticky` | `str` | `.sticky-top` | Position style. |
| `fixed` | `str` | `.fixed-top` | Floating position style. |

::: faststrap.components.navigation.navbar.Navbar
    options:
        show_source: false
        heading_level: 4
