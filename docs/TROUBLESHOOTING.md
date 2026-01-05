# Troubleshooting Guide

Common issues and solutions when using Faststrap.

---

## Static Files Not Loading (404 Errors)

### Symptoms
- Bootstrap styles not applied
- Components look unstyled
- Console shows 404 errors for `/static/css/bootstrap.min.css`
- Dark background with light text

### Solution (Fixed in v0.4.6+)
This bug has been fixed! Update to the latest version:

```bash
pip install --upgrade faststrap
```

If you're still experiencing issues, try:

```python
# Option 1: Use CDN mode
add_bootstrap(app, use_cdn=True)

# Option 2: Explicitly mount static files
from starlette.staticfiles import StaticFiles
from pathlib import Path

static_path = Path(__file__).parent / "static"
app.mount("/static", StaticFiles(directory=static_path), name="static")
add_bootstrap(app, static_url="/static")
```

---

## Theme Not Applied with fast_app()

### Symptoms
- Text appears light/washed out
- Dark mode styles not working
- `data-bs-theme` attribute missing from HTML

### Cause
`fast_app()` doesn't automatically apply `app.htmlkw` to the auto-generated `<html>` tag when you return `Div()` directly.

### Solution
Add `data_bs_theme` to your root element:

```python
app, rt = fast_app()
add_bootstrap(app, mode="light")

@rt("/")
def get():
    return Div(
        YourContent(),
        data_bs_theme="light",  # ← Add this
    )
```

**Or use FastHTML() for automatic theme application:**

```python
app = FastHTML()
add_bootstrap(app, mode="light")  # Automatically sets data-bs-theme on <html>

@app.route("/")
def get():
    return Div(YourContent())  # ✅ Theme applied automatically
```

---

## Styles Not Loading with Custom Html() + Head()

### Symptoms
- Using `Html()`, `Head()`, `Body()` manually
- Faststrap styles not applied
- Only seeing raw HTML

### Cause
When you manually create `Html()` + `Head()`, you bypass FastHTML's automatic header injection.

### Solution
Include `*app.hdrs` in your `Head()`:

```python
app = FastHTML()
add_bootstrap(app)

@app.route("/")
def get():
    return Html(
        Head(
            Title("My App"),
            Meta(charset="utf-8"),
            *app.hdrs,  # ← Required for Faststrap styles
        ),
        Body(
            Card("Hello World")
        )
    )
```

**Or use fast_app() and return components directly:**

```python
app, rt = fast_app()
add_bootstrap(app)

@rt("/")
def get():
    return Card("Hello World")  # ✅ Headers included automatically
```

---

## Two Initialization Patterns

Faststrap supports both FastHTML initialization patterns:

### Pattern 1: fast_app() (Simple)

**Best for:** Quick prototypes, simple apps, learning

```python
from fasthtml.common import *
from faststrap import add_bootstrap, Card, Button

app, rt = fast_app()
add_bootstrap(app)

@rt("/")
def get():
    return Card(
        "Welcome!",
        Button("Click Me", variant="primary")
    )  # ✅ Auto-wrapped, headers included

serve()
```

**Pros:**
- ✅ Less boilerplate
- ✅ Auto-includes headers
- ✅ Simpler for beginners

**Cons:**
- ❌ Less control over `<head>`
- ❌ Need to add `data_bs_theme` manually for themes

### Pattern 2: FastHTML() (Full Control)

**Best for:** Complex apps, custom SEO, production sites

```python
from fasthtml.common import *
from faststrap import add_bootstrap, Card, Button

app = FastHTML()
add_bootstrap(app)

@app.route("/")
def get():
    return Html(
        Head(
            Title("My App"),
            Meta(name="description", content="..."),
            *app.hdrs,  # ← Required
        ),
        Body(
            Card("Welcome!", Button("Click", variant="primary"))
        )
    )

serve()
```

**Pros:**
- ✅ Full control over `<head>`
- ✅ Easy to add meta tags per route
- ✅ Better for SEO
- ✅ Theme applied automatically

**Cons:**
- ❌ More boilerplate
- ❌ Must remember `*app.hdrs`

---

## Component Not Rendering

### Symptoms
- Component appears as plain text
- No Bootstrap styling applied

### Common Causes

**1. Missing import:**
```python
# ❌ Wrong
from faststrap import add_bootstrap
Card("Hello")  # NameError

# ✅ Correct
from faststrap import add_bootstrap, Card
Card("Hello")
```

**2. Forgot to call add_bootstrap():**
```python
# ❌ Wrong
app = FastHTML()
# Missing: add_bootstrap(app)

# ✅ Correct
app = FastHTML()
add_bootstrap(app)
```

**3. Using wrong parameter names:**
```python
# ❌ Wrong
Button("Click", color="primary")  # No 'color' parameter

# ✅ Correct
Button("Click", variant="primary")
```

---

## Icons Not Showing

### Symptoms
- Icon component renders but shows nothing
- Empty space where icon should be

### Solution

Icons use Bootstrap Icons. Make sure you're using valid icon names from [Bootstrap Icons](https://icons.getbootstrap.com/):

```python
# ✅ Correct
Icon("check-circle")
Icon("arrow-right")
Icon("heart-fill")

# ❌ Wrong (invalid names)
Icon("checkmark")  # Use "check-circle" instead
Icon("right-arrow")  # Use "arrow-right" instead
```

---

## HTMX Not Working

### Symptoms
- HTMX attributes not triggering
- No dynamic updates

### Solution

Make sure you're using the correct HTMX attribute format:

```python
# ✅ Correct - use underscores
Button("Load More", hx_get="/more", hx_target="#content")

# ❌ Wrong - dashes don't work in Python
Button("Load More", hx-get="/more")  # SyntaxError
```

Faststrap automatically converts `hx_get` → `hx-get` in the HTML output.

---

## Need More Help?

- **Documentation**: [Faststrap Docs](https://faststrap.dev)
- **Examples**: Check `examples/` directory
- **GitHub Issues**: [Report a bug](https://github.com/Faststrap-org/Faststrap/issues)
- **Discord**: Join the FastHTML community

---

## Quick Checklist

Before asking for help, verify:

- [ ] Latest Faststrap version: `pip install --upgrade faststrap`
- [ ] Called `add_bootstrap(app)` after creating app
- [ ] Using correct initialization pattern (fast_app vs FastHTML)
- [ ] Included `*app.hdrs` if using manual `Html()` + `Head()`
- [ ] Using valid Bootstrap class names and component parameters
- [ ] Checked browser console for errors
- [ ] Verified static files are loading (check Network tab)
