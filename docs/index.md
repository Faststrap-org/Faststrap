# Welcome to FastStrap

<p align="center">
  <img src="assets/logo.svg" alt="FastStrap Logo" width="200" style="margin: 0 auto; display: block;" />
</p>

<p align="center" style="font-size: 1.2rem; margin-top: 1rem;">
  <b>Python-native UI components for FastHTML apps, dashboards, and data tools.</b><br>
  Build production web interfaces in pure Python, with Bootstrap polish and HTMX flow.
</p>

<div align="center">
  <a href="getting-started/installation/" class="md-button md-button--primary">Get Started</a>
  <a href="components/forms/button/" class="md-button">Browse Components</a>
</div>

---

## The Vision

FastStrap aims to be the **standard UI layer for FastHTML**: a Python-native toolkit for product apps, admin panels, data dashboards, scientific tools, and AI-assisted interfaces. It combines the power of **Python**, the simplicity of **FastHTML**, the interactivity of **HTMX**, and the maturity of **Bootstrap** into a single, cohesive experience.

The core stays lightweight and dependency-conscious, while the broader ecosystem is growing toward richer data, visualization, and agent-friendly workflows.

## Built For

- :material-application-braces: **Product and admin apps**

    ---

    Forms, navigation, layouts, modals, notifications, auth screens, and production-ready Bootstrap surfaces.

- :material-chart-box: **Dashboards and analytics**

    ---

    DataTable, metric cards, KPI cards, charts, maps, polling, SSE helpers, and structured display primitives.

- :material-flask-outline: **Scientific and modelling tools**

    ---

    Compose Python-first interfaces for workflows such as modelling dashboards, internal research apps, and operational data tools.

- :material-robot-outline: **AI-ready interfaces**

    ---

    Registered components, metadata, structured outputs, and a roadmap for richer agent-facing surfaces without turning core into a heavy framework.

{ .grid .cards }

## Why FastStrap

FastHTML is amazing for building web apps in pure Python, but building complete interfaces from scratch can be time-consuming. FastStrap bridges the gap by providing a comprehensive set of **production-ready Bootstrap 5 components** that work for both classic web apps and data-heavy tools.

- :material-language-python: **Pure Python**

    ---

    Define your UI with Python functions and intuitive keyword arguments. Drop into HTML, CSS, or HTMX when you need the extra control.

- :material-flash: **FastHTML Native**

    ---

    Built specifically for FastHTML. Seamlessly integrates with HTMX for dynamic, SPA-like experiences without the complexity.

- :material-bootstrap: **Bootstrap 5.3**

    ---

    Leverages the world's most popular CSS framework. Responsive, accessible, and themeable out of the box.

- :material-eye: **Type Safe**

    ---

    Modern Python 3.10+ type hints for specific arguments. Great IDE support with auto-completion.

- :material-database-eye: **Data-App Friendly**

    ---

    Tables, metric displays, polling, streaming helpers, charts, maps, Markdown, Mermaid, JSON, and code rendering for practical internal tools.

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
        Input("username", label="Username", placeholder="Enter username"),
        Input("password", label="Password", input_type="password"),
        Button("Login", variant="primary", cls="w-100 mt-3"),
        title="Welcome Back",
        style={"max-width": "400px", "margin": "2rem auto"}
    )
```
  </div>
</div>

## Features

- **230+ exports**: Components and helpers across forms, display, navigation, and layouts.
- **HTMX Presets**: ActiveSearch, InfiniteScroll, AutoRefresh, LazyLoad, LoadingButton, OptimisticAction, LocationAction, PollUntil, SSEStream, ConfirmPrompt, Debounce, SwapOnEvent.
- **SEO Module**: SEO meta tags, Open Graph, Twitter Cards, and JSON-LD structured data.
- **PWA Module**: one-call installable app setup (manifest, service worker, install flow).
- **Zero Build Step**: No webpack, no npm, no node_modules.
- **Dark Mode**: Automatic or user-toggled dark mode support.
- **HTMX Ready**: `hx_*` attributes are first-class citizens.
- **Icons Included**: Built-in helper for Bootstrap Icons.
- **Visual Effects**: Scroll-reveal animations, hover effects, and transitions  CSS only.
- **Data UI**: DataTable, Chart, MetricCard, TrendCard, KPICard, DashboardGrid.
- **Renderers**: Markdown, SVG, Mermaid.

## Showcase Layer

Faststrap now has a dedicated `showcase/` layer for polished, production-style references.

- `novaflow_ai_saas.py`
- `fastcloud_generated_saas.py` (compact minimal-good example)
- `northstar_ops_dashboard.py`
- `agency_portfolio.py`
- `carenest_clinic.py`
- `ledgerleaf_finance.py`
- `learnloop_academy.py`
- `lexbridge_corporate.py`
- `forgedocs_platform.py`

See the Showcase section in the docs for the current flagship set and screenshot conventions.

## Stats

- **166 registered UI components** implemented.
- **230+ components, helpers, presets, and integrations** available.
- **12 interaction presets** + **5 hx helpers** + **1 response helper** + **2 SSE helpers** + **1 auth decorator** = **21 preset utilities**.
- **100% Python**.

## Next Steps

- Browse the [Component Index](components/index.md).
- Read the [Architecture Guide](guides/architecture.md) to understand the render model.
- Use the [Upgrade Guide](guides/upgrading.md) when moving between Faststrap versions.
- Review the repository `ROADMAP.md` for future component and integration direction.

## License

FastStrap is licensed under the [MIT License](https://opensource.org/licenses/MIT).
