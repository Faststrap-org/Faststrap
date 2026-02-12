# Theme Toggle

The `ThemeToggle` component creates a dark/light mode switch with HTMX server-side persistence. It uses Bootstrap's form-switch styling with icon indicators and integrates seamlessly with session-based theme management.

!!! success "Goal"
    By the end of this guide, you'll be able to add a professional dark mode toggle to your app **with server-side persistence in minutes.**

---

## Quick Start

Here's the simplest way to add a theme toggle.

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="form-check form-switch d-flex align-items-center">
      <i class="bi bi-sun-fill me-2"></i>
      <input class="form-check-input" type="checkbox" role="switch" id="theme-demo">
      <label class="form-check-label ms-2" for="theme-demo">Dark Mode</label>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
ThemeToggle(
    current_theme="light",
    show_label=True
)
```
  </div>
</div>

---

## Visual Examples & Use Cases

### 1. Icon-Only Toggle

Minimal toggle without label.

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="form-check form-switch d-flex align-items-center">
      <i class="bi bi-moon-stars-fill me-2"></i>
      <input class="form-check-input" type="checkbox" role="switch" checked>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
# Clean, icon-only toggle
ThemeToggle(current_theme="dark")
```
  </div>
</div>

### 2. With Label

Show label for clarity.

```python
ThemeToggle(
    current_theme="dark",
    show_label=True,
    label_text="Dark Mode"
)
```

### 3. In Navbar

Common placement in navigation.

```python
Navbar(
    brand="MyApp",
    items=[
        NavItem("Home", href="/"),
        NavItem("About", href="/about"),
        # Theme toggle in navbar
        ThemeToggle(
            current_theme=req.session.get("theme", "light"),
            cls="ms-auto"
        )
    ]
)
```

---

## Practical Functionality

### Server-Side Theme Management

Complete theme system with persistence.

```python
# Initialize app with theme support
app = FastHTML()

# Theme toggle in layout
def BaseLayout(*content, req):
    theme = req.session.get("theme", "light")
    
    return Html(
        Head(
            Title("MyApp"),
            # Apply theme to body
            Script(f"document.documentElement.setAttribute('data-bs-theme', '{theme}')")
        ),
        Body(
            Navbar(
                brand="MyApp",
                items=[
                    ThemeToggle(
                        current_theme=theme,
                        show_label=True
                    )
                ]
            ),
            *content,
            data_bs_theme=theme
        )
    )

# Theme toggle endpoint
@app.post("/theme/toggle")
def toggle_theme(req):
    current = req.session.get("theme", "light")
    new_theme = "dark" if current == "light" else "light"
    req.session["theme"] = new_theme
    
    # Refresh page to apply theme
    from faststrap.presets import hx_refresh
    return hx_refresh()
```

### With Cookie Persistence

Store theme in cookies for non-authenticated users.

```python
@app.post("/theme/toggle")
def toggle_theme(req, res):
    current = req.cookies.get("theme", "light")
    new_theme = "dark" if current == "light" else "light"
    
    # Set cookie for 1 year
    res.set_cookie(
        "theme",
        new_theme,
        max_age=365*24*60*60,
        httponly=True
    )
    
    return hx_refresh()
```

### With Database Persistence

Save theme preference to user profile.

```python
@app.post("/theme/toggle")
def toggle_theme(req):
    user = req.session.get("user")
    if not user:
        return ErrorDialog(message="Please log in")
    
    # Toggle theme
    current = user.theme or "light"
    new_theme = "dark" if current == "light" else "light"
    
    # Save to database
    db.query(User).filter(User.id == user.id).update({
        "theme": new_theme
    })
    db.commit()
    
    # Update session
    req.session["user"].theme = new_theme
    
    return hx_refresh()
```

---

## Integration Patterns

### In Settings Page

```python
def SettingsPage(user):
    return Container(
        H1("Settings"),
        Card(
            H5("Appearance", cls="card-title"),
            FormGroup(
                ThemeToggle(
                    current_theme=user.theme,
                    show_label=True,
                    label_text="Dark Mode"
                ),
                help_text="Toggle between light and dark themes"
            ),
            cls="mb-3"
        )
    )
```

### With Auto Theme

Support system preference.

```python
def ThemeSelector(current_theme):
    return Div(
        H6("Theme"),
        Div(
            # Radio buttons for theme selection
            Radio("Light", name="theme", value="light", checked=current_theme=="light"),
            Radio("Dark", name="theme", value="dark", checked=current_theme=="dark"),
            Radio("Auto (System)", name="theme", value="auto", checked=current_theme=="auto"),
            hx_post="/theme/set",
            hx_trigger="change"
        )
    )

@app.post("/theme/set")
def set_theme(theme: str, req):
    req.session["theme"] = theme
    return hx_refresh()
```

### Smooth Transition

Add CSS for smooth theme transitions.

```css
/* Add to your CSS */
:root {
    transition: background-color 0.3s ease, color 0.3s ease;
}

body {
    transition: background-color 0.3s ease, color 0.3s ease;
}
```

---

## Parameter Reference

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `current_theme` | `str` | "auto" | Current theme ("light", "dark", "auto") |
| `endpoint` | `str` | "/theme/toggle" | Server endpoint for theme changes |
| `toggle_id` | `str` | "theme-toggle" | Unique ID for the toggle |
| `show_label` | `bool` | `False` | Whether to show label text |
| `label_text` | `str` | "Dark Mode" | Label text to display |
| `**kwargs` | `Any` | - | Additional HTML attributes |

---

## Best Practices

### ✅ Do This

```python
# Get theme from session
theme = req.session.get("theme", "light")
ThemeToggle(current_theme=theme)

# Provide visual feedback
@app.post("/theme/toggle")
def toggle_theme(req):
    # ... toggle logic ...
    return hx_refresh()  # Refresh to show change

# Support system preference
ThemeToggle(current_theme="auto")
```

### ❌ Don't Do This

```python
# Don't hardcode theme
ThemeToggle(current_theme="dark")  # Always dark!

# Don't forget to persist
@app.post("/theme/toggle")
def toggle_theme(req):
    # Toggle but don't save - lost on refresh!
    return hx_refresh()

# Don't use client-side only
# ThemeToggle requires server endpoint
```

---

## Complete Example

Full theme system implementation.

```python
from fasthtml.common import *
from faststrap import ThemeToggle, Navbar
from faststrap.presets import hx_refresh

app = FastHTML()

def get_theme(req):
    """Get theme from session or cookie."""
    return req.session.get("theme") or req.cookies.get("theme", "light")

def apply_theme(theme):
    """Apply theme to HTML."""
    return Script(f"""
        document.documentElement.setAttribute('data-bs-theme', '{theme}');
    """)

@app.get("/")
def home(req):
    theme = get_theme(req)
    
    return Html(
        Head(
            Title("MyApp"),
            apply_theme(theme)
        ),
        Body(
            Navbar(
                brand="MyApp",
                items=[
                    ThemeToggle(
                        current_theme=theme,
                        show_label=True
                    )
                ]
            ),
            Container(
                H1("Welcome to MyApp"),
                P("Try toggling the theme!")
            ),
            data_bs_theme=theme
        )
    )

@app.post("/theme/toggle")
def toggle_theme(req, res):
    current = get_theme(req)
    new_theme = "dark" if current == "light" else "light"
    
    # Save to session and cookie
    req.session["theme"] = new_theme
    res.set_cookie("theme", new_theme, max_age=365*24*60*60)
    
    return hx_refresh()
```

---

::: faststrap.components.forms.theme_toggle.ThemeToggle
    options:
        show_source: true
        heading_level: 4
