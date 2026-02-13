# Welcome to FastStrap

<p align="center">
  <img src="assets/logo.svg" alt="FastStrap Logo" width="200" style="margin: 0 auto; display: block;" />
</p>

<p align="center" style="font-size: 1.2rem; margin-top: 1rem;">
  <b>Modern Bootstrap 5 components for FastHTML.</b><br>
  Build beautiful web UIs in pure Python with zero JavaScript knowledge.
</p>

<div align="center">
  <a href="getting-started/installation/" class="md-button md-button--primary">Get Started</a>
  <a href="components/forms/button/" class="md-button">Browse Components</a>
</div>

---

## The Vision

FastStrap aims to be the **standard component library for FastHTML**, providing 100+ production-ready Bootstrap 5 components. It combines the power of **Python**, the simplicity of **FastHTML**, and the maturity of **Bootstrap** into a single, cohesive experience.

## Why FastStrap?

FastHTML is amazing for building web apps in pure Python, but building UI from scratch can be time-consuming. FastStrap bridges the gap by providing a comprehensive set of **production-ready Bootstrap 5 components** that just work.

- :material-language-python: **Pure Python**

    ---

    No JavaScript, HTML, or CSS knowledge required. Define your UI with Python classes and intuitive keyword arguments.

- :material-flash: **FastHTML Native**

    ---

    Built specifically for FastHTML. Seamlessly integrates with HTMX for dynamic, SPA-like experiences without the complexity.

- :material-bootstrap: **Bootstrap 5.3**

    ---

    Leverages the world's most popular CSS framework. Responsive, accessible, and themeable out of the box.

- :material-eye: **Type Safe**

    ---

    Modern Python 3.10+ type hints for specific arguments. Great IDE support with auto-completion.

{ .grid .cards }

## At a Glance

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="card shadow-sm" style="max-width: 400px; width: 100%;">
      <div class="card-body">
        <h5 class="card-title">Welcome Back</h5>
        <div class="mb-3">
          <label class="form-label">Username</label>
          <input type="text" class="form-control" placeholder="Enter username">
        </div>
        <div class="mb-3">
          <label class="form-label">Password</label>
          <input type="password" class="form-control">
        </div>
        <button class="btn btn-primary w-100 mt-3">Login</button>
      </div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
@app.route("/")
def home():
    return Card(
        Input(label="Username", placeholder="Enter username"),
        Input(label="Password", type="password"),
        Button("Login", variant="primary", cls="w-100 mt-3"),
        title="Welcome Back",
        style={"max-width": "400px", "margin": "2rem auto"}
    )
```
  </div>
</div>

## Features

- **67 Components**: From Buttons to Modals, Navbars to Tables, SearchableSelect to ErrorPage.
- **HTMX Presets**: ActiveSearch, InfiniteScroll, AutoRefresh, LazyLoad, LoadingButton — zero JS.
- **SEO Module**: SEO meta tags, Open Graph, Twitter Cards, and JSON-LD structured data.
- **Zero Build Step**: No webpack, no npm, no node_modules.
- **Dark Mode**: Automatic or user-toggled dark mode support.
- **HTMX Ready**: `hx_*` attributes are first-class citizens.
- **Icons Included**: Built-in helper for Bootstrap Icons.
- **Visual Effects**: Scroll-reveal animations, hover effects, and transitions — CSS only.

## Stats

- **67 components** implemented.
- **250+ tests** passing.
- **5 HTMX presets** + **4 response helpers**.
- **100% Python**.

## License

FastStrap is licensed under the [MIT License](https://opensource.org/licenses/MIT).
