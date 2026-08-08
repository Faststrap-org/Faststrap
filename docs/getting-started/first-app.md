# First App Tutorial

This tutorial walks you through building your first FastHTML + Faststrap application from scratch. By the end, you will have a working web app with a form, validation, and toast notifications.

---

## Prerequisites

- Python 3.9+
- `pip` or `uv`
- A code editor

---

## Step 1: Install FastHTML and Faststrap

```bash
pip install fasthtml faststrap
```

Verify the installation:

```bash
python -c "import fasthtml; import faststrap; print('OK')"
```

---

## Step 2: Create Your App

Create `main.py`:

```python
from fasthtml.common import *
from faststrap import *

app, rt = fast_app()

# Add Bootstrap and Faststrap assets to every page
@app.before
def add_bootstrap(req, resp):
    return add_bootstrap(req, resp)

@rt("/")
def get():
    return (
        PageMeta(
            title="My First App",
            description="Built with FastHTML and Faststrap",
        ),
        Container(
            H1("Welcome to Faststrap"),
            P("This is your first FastHTML app with Bootstrap styling."),
        ),
    )

serve()
```

Run the app:

```bash
python main.py
```

Open `http://localhost:8000` in your browser.

---

## Step 3: Add a Card and Button

```python
from fasthtml.common import *
from faststrap import *

app, rt = fast_app()

@app.before
def add_bootstrap(req, resp):
    return add_bootstrap(req, resp)

@rt("/")
def get():
    return (
        PageMeta(title="My First App", description="Built with FastHTML and Faststrap"),
        Container(
            H1("Welcome"),
            P("This is a card built with Faststrap."),
            Card(
                Card.Body(
                    H4("Getting Started"),
                    P("Faststrap makes it easy to build beautiful UIs in Python."),
                    Button("Learn More", variant="primary", href="/docs"),
                ),
            ),
            cls="py-5",
        ),
    )

serve()
```

---

## Step 4: Add a Form

```python
from fasthtml.common import *
from faststrap import *

app, rt = fast_app()

@app.before
def add_bootstrap(req, resp):
    return add_bootstrap(req, resp)

@rt("/")
def get():
    return (
        PageMeta(title="Contact", description="Get in touch"),
        Container(
            H1("Contact Us"),
            Card(
                Card.Body(
                    Form(
                        FormGroup("Name", Input(name="name", type="text", required=True)),
                        FormGroup("Email", Input(name="email", type="email", required=True)),
                        FormGroup("Message", Textarea(name="message", rows=4)),
                        Button("Send Message", type="submit", variant="primary"),
                        method="post",
                        action="/contact",
                    ),
                ),
            ),
            cls="py-5",
        ),
    )

@rt("/contact")
def post(name: str, email: str, message: str):
    return (
        PageMeta(title="Thanks", description="Message sent"),
        Container(
            Toast("Message sent! We'll be in touch.", variant="success"),
            cls="py-5",
        ),
    )

serve()
```

---

## Step 5: Add Validation

```python
from fasthtml.common import *
from faststrap import *

app, rt = fast_app()

@app.before
def add_bootstrap(req, resp):
    return add_bootstrap(req, resp)

@rt("/")
def get():
    return (
        PageMeta(title="Contact", description="Get in touch"),
        Container(
            H1("Contact Us"),
            Card(
                Card.Body(
                    Form(
                        FormGroup("Name", Input(name="name", type="text", required=True)),
                        FormGroup("Email", Input(name="email", type="email", required=True)),
                        FormGroup("Message", Textarea(name="message", rows=4)),
                        Button("Send Message", type="submit", variant="primary"),
                        method="post",
                        action="/contact",
                    ),
                ),
            ),
            cls="py-5",
        ),
    )

@rt("/contact")
def post(name: str, email: str, message: str):
    errors = {}
    if not name or len(name) < 2:
        errors["name"] = "Name must be at least 2 characters"
    if not email or "@" not in email:
        errors["email"] = "Please enter a valid email address"
    if not message or len(message) < 10:
        errors["message"] = "Message must be at least 10 characters"

    if errors:
        return (
            PageMeta(title="Contact", description="Get in touch"),
            Container(
                FormErrorSummary(errors),
                Card(
                    Card.Body(
                        Form(
                            FormGroup("Name", Input(name="name", value=name)),
                            FormGroup("Email", Input(name="email", value=email, type="email")),
                            FormGroup("Message", Textarea(name="message", rows=4)),
                            Button("Send Message", type="submit", variant="primary"),
                            method="post",
                            action="/contact",
                        ),
                    ),
                ),
                cls="py-5",
            ),
        )

    return (
        PageMeta(title="Thanks", description="Message sent"),
        Container(
            Toast("Message sent! We'll be in touch.", variant="success"),
            cls="py-5",
        ),
    )

serve()
```

---

## Step 6: Add HTMX Interactivity

```python
from fasthtml.common import *
from faststrap import *

app, rt = fast_app()

@app.before
def add_bootstrap(req, resp):
    return add_bootstrap(req, resp)

@rt("/")
def get():
    return (
        PageMeta(title="Search", description="Search users"),
        Container(
            H1("Search Users"),
            Input(
                type="search",
                placeholder="Type to search...",
                name="q",
                hx_get="/search",
                hx_target="#results",
                hx_swap="innerHTML",
                hx_trigger=Debounce(300),
                cls="form-control mb-3",
            ),
            Div(id="results"),
            cls="py-5",
        ),
    )

@rt("/search")
def get(q: str):
    if not q:
        return Div("Start typing to search...")
    results = [u for u in USERS if q.lower() in u["name"].lower()]
    if not results:
        return Div("No results found.")
    return Div(*[P(f"{u['name']} - {u['email']}") for u in results])

serve()
```

---

## Step 7: Add Dark Mode

```python
from fasthtml.common import *
from faststrap import *

app, rt = fast_app()

@app.before
def add_bootstrap(req, resp):
    return add_bootstrap(req, resp, mode="dark")

@rt("/")
def get():
    return (
        PageMeta(title="Dark Mode App", description="Faststrap with dark mode"),
        Container(
            H1("Dark Mode Enabled"),
            P("This app uses Faststrap's dark mode support."),
            Button("Toggle Theme", variant="primary"),
            cls="py-5",
        ),
    )

serve()
```

---

## Summary

You have built a FastHTML + Faststrap app with:

- Bootstrap styling via `add_bootstrap`
- Cards, Buttons, and Forms
- Server-side validation with `FormErrorSummary`
- HTMX search with `Debounce`
- Toast notifications
- Dark mode support

Next steps:

- Explore the [Component Reference](../components/index.md)
- Read the [HTMX Integration Guide](../guides/htmx-integration.md)
- Learn about [Theming](../guides/theming.md)
