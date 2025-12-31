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

<div class="grid cards" markdown>

-   :material-language-python: **Pure Python**
    ---
    No JavaScript, HTML, or CSS knowledge required. Define your UI with Python classes and intuitive keyword arguments.

-   :material-flash: **FastHTML Native**
    ---
    Built specifically for FastHTML. Seamlessly integrates with HTMX for dynamic, SPA-like experiences without the complexity.

-   :material-bootstrap: **Bootstrap 5.3**
    ---
    Leverages the world's most popular CSS framework. Responsive, accessible, and themeable out of the box.

-   :material-eye: **Type Safe**
    ---
    Modern Python 3.10+ type hints for specific arguments. Great IDE support with auto-completion.

</div>

## At a Glance

```python
from fasthtml.common import FastHTML, serve
from faststrap import add_bootstrap, Card, Button, Input

app = FastHTML()
add_bootstrap(app)

@app.route("/")
def home():
    return Card(
        Input(label="Username", placeholder="Enter username"),
        Input(label="Password", type="password"),
        Button("Login", variant="primary", cls="w-100 mt-3"),
        title="Welcome Back",
        style={"max-width": "400px", "margin": "2rem auto"}
    )

serve()
```

## Features

- **38+ Components**: From Buttons to Modals, Navbars to Tables.
- **Zero Build Step**: No webpack, no npm, no node_modules.
- **Dark Mode**: Automatic or user-toggled dark mode support.
- **HTMX Ready**: `hx_*` attributes are first-class citizens.
- **Icons Included**: Built-in helper for Bootstrap Icons.

## Stats

- **38 components** implemented.
- **230+ tests** passing.
- **100% Python**.

## License

FastStrap is licensed under the [MIT License](https://opensource.org/licenses/MIT).
