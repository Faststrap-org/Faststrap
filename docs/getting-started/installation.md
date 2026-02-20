# Installation

Getting started with FastStrap is easy.

## Prerequisites

- **Python 3.10** or higher
- **FastHTML 0.6** or higher

## Install via pip

```bash
pip install faststrap
```

## Local development install (editable)

If you want to test this exact repo locally before publishing:

```bash
cd Faststrap
python -m pip install -e .
```

Install dev tools too:

```bash
python -m pip install -e ".[dev]"
```

## Verify Installation

You can verify that FastStrap is installed correctly by running:

```bash
python -c "import faststrap; print(faststrap.__version__)"
```

## Run a local feature example

```bash
python examples/05_new_components/pre_v060_features.py
```

Then open the local URL shown by FastHTML (commonly `http://localhost:5000`).

---

# Configuration

## Basic Setup

To use FastStrap, you simply need to call `add_bootstrap()` on your FastHTML app instance. This injects the necessary CSS and JavaScript (CDN or local) into your application headers.

```python title="main.py"
from fasthtml.common import FastHTML
from faststrap import add_bootstrap

app = FastHTML()

# Initialize FastStrap
add_bootstrap(app)

@app.route("/")
def index():
    return "Hello FastStrap!"
```

## Dark Mode

FastStrap supports Bootstrap's color modes. You can force a specific mode or let it respect the user's system preference.

```python
# Force Dark Mode
add_bootstrap(app, mode="dark")

# Force Light Mode
add_bootstrap(app, mode="light")

# Auto (matches system preference)
add_bootstrap(app, mode="auto")
```

## Custom Themes

You can customize the primary colors of your application without writing CSS using `create_theme`.

```python
from faststrap import add_bootstrap, create_theme

# Create a custom theme
my_theme = create_theme(
    primary="#6f42c1",   # Purple
    secondary="#0dcaf0"  # Cyan
)

add_bootstrap(app, theme=my_theme)
```
