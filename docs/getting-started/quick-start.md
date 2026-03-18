# Quick Start

Get your first FastStrap application running in less than a minute.

## 1. Create your application

Create a new file named `app.py`:

```python title="app.py"
from fasthtml.common import FastHTML, serve, H1, P
from faststrap import add_bootstrap, Container, Hero, Button

# 1. Initialize FastHTML
app = FastHTML()

# 2. Inject FastStrap (Bootstrap 5)
add_bootstrap(app)

# 3. Define your first page
@app.route("/")
def home():
    return Container(
        Hero(
            title="FastStrap is Live!",
            subtitle="Building beautiful Python UIs has never been easier.",
            action=Button("View Components", variant="primary", href="/components"),
            align="center"
        )
    )

# 4. Run the server
if __name__ == "__main__":
    serve()
```

## 2. Run it

Execute the script:

```bash
python app.py
```

Open your browser to [http://localhost:5001](http://localhost:5001) and see your styled Hero section!

---

## Building Your UI

FastStrap components follow a standard pattern: **Children first, then keyword arguments.**

### Adding Components

You can nest components just like HTML:

```python
from faststrap import Card, Button, Input

Card(
    Input("email", label="Email", placeholder="you@example.com"),
    Button("Join Waitlist", variant="primary", full_width=True),
    title="Get Notified"
)
```

### Adding HTMX Interactivity

FastStrap components are designed for HTMX. Use `hx_` attributes to make your UI dynamic without writing any JavaScript.

```python
Button(
    "Delete", 
    variant="danger", 
    hx_delete="/items/1", 
    hx_target="#item-list"
)
```

## Next Steps

- Explore the [Component Gallery](components/forms/button.md)
- Learn about [Dark Mode and Theming](customization.md)
- Check the [Grid System](layout/grid.md) for complex layouts
