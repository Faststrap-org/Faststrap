# Composition Guide

This guide covers how to compose Faststrap components to build complex UIs.

---

## Composing Cards

```python
from faststrap import Card, CardHeader, CardBody, CardFooter, Button, Badge

Card(
    CardHeader(
        "User Profile",
        Badge("Admin", variant="primary"),
    ),
    CardBody(
        H4("Jane Doe"),
        P("Software Engineer"),
        P("San Francisco, CA", cls="text-muted"),
    ),
    CardFooter(
        Button("Edit", variant="secondary", outline=True),
        Button("Delete", variant="danger"),
    ),
)
```

---

## Composing Forms

```python
from faststrap import Form, FormGroup, Input, Select, Checkbox, Button

Form(
    FormGroup("Full Name", Input(name="name", required=True)),
    FormGroup("Email", Input(name="email", type="email")),
    FormGroup("Role", Select(
        Option("Admin", value="admin"),
        Option("User", value="user"),
        name="role",
    )),
    FormGroup(
        Checkbox(name="active", label="Active", checked=True),
        label="",
    ),
    Button("Save", type="submit", variant="primary"),
    method="post",
    action="/users",
)
```

---

## Composing Layouts

```python
from faststrap import Stack, Cluster, Center, Card

Stack(
    # Header with actions
    Cluster(
        H2("Dashboard"),
        Button("Add Item", variant="primary"),
        justify="between",
        align="center",
    ),
    # Content area
    Card(
        Card.Body(
            # ... content
        ),
    ),
    gap=3,
)
```

---

## Nested Layouts

```python
from faststrap import Stack, Cluster, Center, Card

Center(
    Stack(
        Card(
            Card.Header("Login"),
            Card.Body(
                Form(
                    FormGroup("Email", Input(name="email", type="email")),
                    FormGroup("Password", Input(name="password", type="password")),
                    Button("Sign In", type="submit", variant="primary"),
                    method="post",
                    action="/login",
                ),
            ),
        ),
        P("Don't have an account?", cls="text-center"),
        Cluster(
            Button("Sign Up", variant="secondary", href="/register"),
            justify="center",
        ),
        gap=3,
    ),
    min_height="100vh",
)
```

---

## Composing with HTMX

```python
from faststrap import Stack, Card, Button, Toast

Stack(
    Card(
        Card.Header(
            Cluster(
                "Tasks",
                Button("Add", variant="primary", size="sm",
                       hx_get="/tasks/new", hx_target="#task-form"),
                justify="between",
            ),
        ),
        Card.Body(
            Div(id="task-list"),
            Div(id="task-form"),
        ),
    ),
    gap=3,
)
```

---

## merge_classes

Use `merge_classes` when building custom components:

```python
from faststrap import merge_classes

def MyButton(text: str, *, variant: str = "primary", **kwargs):
    user_cls = kwargs.pop("cls", "")
    base = f"btn btn-{variant}"
    return Button(text, cls=merge_classes(base, user_cls), **kwargs)
```

---

## When to Create Custom Components

Create a custom component when:
- You reuse the same composition pattern 3+ times
- You need to encapsulate complex logic
- You want a clean API for your team

Use composition when:
- The pattern is used 1-2 times
- The composition is simple
- You want flexibility

---

## See Also

- [Custom Components Guide](../guides/custom-components.md)
- [HTMX Integration Guide](../guides/htmx-integration.md)
- [First App Tutorial](../getting-started/first-app.md)
