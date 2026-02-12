# New Components Examples (v0.5.4)

This directory contains comprehensive examples demonstrating all new components added in Faststrap v0.5.4.

## Examples Overview

### Error Handling

#### 1. `error_pages.py` - ErrorPage Component

Full-page error displays for common HTTP errors and custom error scenarios.

**Features:**

- 404, 500, 403 error pages
- Custom error messages
- Backend error display
- Customizable icons and actions

**Run:**

```bash
python examples/05_new_components/error_pages.py
```

#### 2. `error_dialogs.py` - ErrorDialog Component

Modal error displays with retry functionality and HTMX integration.

**Features:**

- Basic error dialogs
- Error with retry button
- Different variants (danger, warning, info, success)
- Out-of-band swap integration

**Run:**

```bash
python examples/05_new_components/error_dialogs.py
```

---

### HTMX Presets

#### 3. `presets_interactions.py` - Interaction Presets

Demonstrates all 5 HTMX interaction presets with working endpoints.

**Features:**

- `ActiveSearch` - Live search with debouncing
- `InfiniteScroll` - Load more on scroll
- `AutoRefresh` - Auto-updating content
- `LazyLoad` - Load on visibility
- `LoadingButton` - Button with loading state

**Run:**

```bash
python examples/05_new_components/presets_interactions.py
```

#### 4. `presets_responses.py` - Response Helpers

Server-side response helpers for common HTMX patterns.

**Features:**

- `hx_redirect()` - Server-side redirects
- `hx_refresh()` - Full page refresh
- `toast_response()` - Toast notifications
- `@require_auth` - Route protection

**Run:**

```bash
python examples/05_new_components/presets_responses.py
```

---

### Form Components

#### 5. `form_components.py` - Form Enhancements

Demonstrates FormGroup, ThemeToggle, and SearchableSelect.

**Features:**

- `FormGroup` - Form field wrapper with validation
- `ThemeToggle` - Dark/light mode switch
- `SearchableSelect` - Server-side searchable dropdown
- Validation states and feedback

**Run:**

```bash
python examples/05_new_components/form_components.py
```

#### 6. `auth_pages.py` - AuthLayout Component

Complete authentication pages using AuthLayout.

**Features:**

- Login page
- Registration page
- Password reset page
- Form validation
- HTMX integration

**Run:**

```bash
python examples/05_new_components/auth_pages.py
```

---

### Pattern Components

#### 7. `pattern_components.py` - Patterns

Demonstrates FooterModern, Testimonial, and TestimonialSection.

**Features:**

- `FooterModern` - Multi-column footer with branding
- `Testimonial` - Customer testimonial cards
- `TestimonialSection` - Grid of testimonials
- Social links and navigation

**Run:**

```bash
python examples/05_new_components/pattern_components.py
```

---

## Quick Start

1. **Install Faststrap:**

   ```bash
   pip install faststrap
   ```

2. **Run any example:**

   ```bash
   python examples/05_new_components/error_pages.py
   ```

3. **Open browser:**
   Navigate to `http://localhost:5001` (or the port shown in terminal)

---

## Example Structure

Each example follows this pattern:

```python
from fasthtml.common import *
from faststrap import *

app = FastHTML()
add_bootstrap(app)

@app.get("/")
def home():
    return Container(
        # Component demonstrations
    )

serve()
```

---

## Key Learnings

### ErrorPage vs ErrorDialog

- **ErrorPage**: Full-page error displays (404, 500, etc.)
- **ErrorDialog**: Modal error displays for inline errors

### HTMX Presets

- Eliminate boilerplate for common patterns
- Server-side logic, zero client-side JS
- Composable and reusable

### Form Components

- **FormGroup**: Consistent form field structure
- **ThemeToggle**: Server-side theme persistence
- **SearchableSelect**: Replaces Select2/Choices.js

### Auth & Patterns

- **AuthLayout**: Centered auth page layout
- **FooterModern**: Professional multi-column footer
- **Testimonials**: Social proof components

---

## Next Steps

1. **Explore the examples** - Run each example to see components in action
2. **Read the docs** - Check `docs/components/` for detailed documentation
3. **Build something** - Use these components in your own FastHTML apps!

---

## Need Help?

- **Documentation**: [https://faststrap-org.github.io/Faststrap/](https://faststrap-org.github.io/Faststrap/)
- **GitHub**: [https://github.com/Faststrap-org/Faststrap](https://github.com/Faststrap-org/Faststrap)
- **Issues**: [https://github.com/Faststrap-org/Faststrap/issues](https://github.com/Faststrap-org/Faststrap/issues)

---

## Contributing

Found a bug or have an improvement? We welcome contributions!

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

See [CONTRIBUTING.md](../../CONTRIBUTING.md) for guidelines.
