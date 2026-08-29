# Security Guide

This page covers security considerations when building FastHTML applications with Faststrap components.

---

## HTMX Safety

Faststrap's HTMX presets and components that emit `hx-*` attributes follow these safety principles:

### CSRF Protection

FastHTML's `FastHTML` app includes CSRF protection by default. When using HTMX-presets that submit forms (`OptimisticAction`, `LocationAction`, `ActionButtons`), the CSRF token is automatically included:

```python
from fasthtml.common import FastHTML
from faststrap import ActionButtons

app = FastHTML()  # CSRF enabled by default

# HTMX requests from ActionButtons include the CSRF token automatically
ActionButtons(submit_text="Save", cancel_url="/")
```

If you disable CSRF (not recommended), HTMX presets that submit forms will fail silently or return 403.

### Open Redirect Prevention

Presets like `LocationAction` accept a `redirect_url` parameter. **You must validate this URL server-side** to prevent open redirect vulnerabilities:

```python
from faststrap import LocationAction
from urllib.parse import urlparse

def is_safe_url(url: str) -> bool:
    parsed = urlparse(url)
    return not parsed.netloc or parsed.netloc == request.url.hostname

# Only use user-supplied redirect URLs after validation
LocationAction(
    "Save",
    redirect_url="/dashboard" if is_safe_url(user_input) else "/",
    ...
)
```

### Server-Side Validation

HTMX makes it easy to build reactive UIs, but **all client-side state must be re-validated server-side**. This is especially important for:

- `ActiveSearch` — the search query must be validated/sanitized before database use.
- `DataTable` — sort column, direction, page number, and filters must be validated.
- `InfiniteScroll` — the cursor/offset must be validated.
- `OptimisticAction` — the optimistic state must be reconciled with authoritative server state.

```python
# Example: validate DataTable sort parameters server-side
@app.get("/users")
def get_users(sort: str = "name", direction: str = "asc", page: int = 1):
    allowed_sort = {"name", "email", "created_at"}
    if sort not in allowed_sort:
        sort = "name"
    if direction not in ("asc", "desc"):
        direction = "asc"
    # ... proceed with validated params
```

---

## XSS Prevention

### Markdown Sanitization

The `Markdown` component can render user-supplied content. Use the `sanitize` parameter to strip dangerous HTML:

```python
from faststrap import Markdown

# Sanitize user content (recommended)
Markdown(user_content, sanitize=True)

# Only skip sanitization if you fully trust the content source
Markdown(trusted_content, sanitize=False)
```

The sanitizer uses [bleach](https://bleach.readthedocs.io/) under the hood and strips `<script>` tags, event handler attributes, `javascript:` URLs, and dangerous CSS expressions. Install the markdown extra to enable sanitization: `pip install faststrap[markdown]`.

### SVG Sanitization

The `render_svg()` utility also supports sanitization:

```python
from faststrap import render_svg
safe_svg = render_svg(user_svg_string, sanitize=True)
```

### HTML in Component Attributes

Never inject untrusted data directly into HTML attributes:

```python
# DANGEROUS — do not do this
Div(cls=user_supplied_class)  # Could contain event handlers

# SAFE — escape or validate
from fasthtml.common import escape
Div(cls=escape(user_supplied_class))
```

---

## DataTable Security

When using `DataTable` with server-side pagination, sorting, or filtering:

### Sort Column Injection

Never pass user-supplied sort values directly to your database query:

```python
# DANGEROUS — SQL injection via sort column
query = f"SELECT * FROM users ORDER BY {sort}"  # Don't do this

# SAFE — whitelist allowed columns
allowed = {"name", "email", "created_at"}
sort_col = sort if sort in allowed else "name"
query = f"SELECT * FROM users ORDER BY {sort_col}"
```

### Per-Page Limits

Enforce maximum `per_page` values to prevent excessive response sizes:

```python
per_page = min(int(user_per_page), 100)  # Cap at 100
```

### Search String Sanitization

Sanitize search strings before using them in SQL `LIKE` clauses or ORM queries:

```python
import re
clean_search = re.sub(r"[^a-zA-Z0-9\s]", "", raw_search)
```

---

## File Upload Security

When using `FileUpload` or `Dropzone` components:

```python
from faststrap import FileUpload
from werkzeug.utils import secure_filename
import os

ALLOWED_EXTENSIONS = {".png", ".jpg", ".pdf"}
MAX_SIZE = 5 * 1024 * 1024  # 5 MB

def validate_upload(filename: str) -> bool:
    ext = os.path.splitext(filename)[1].lower()
    return ext in ALLOWED_EXTENSIONS

safe_name = secure_filename(user_filename)
```

---

## Authentication & Authorization

### `require_auth` Preset

The `require_auth` decorator protects HTMX endpoints:

```python
from faststrap.presets import require_auth

@app.get("/admin/data")
@require_auth
def admin_data():
    # Only accessible to authenticated users
    ...
```

**Important:** `require_auth` checks for a session-based authentication pattern. You must implement the corresponding session management in your app. It does not replace a full authentication framework.

### Component-Level Authorization

Faststrap components do not enforce authorization. You must check permissions in your route handlers.

---

## Content Security Policy (CSP)

Faststrap components emit inline styles and HTMX `hx-*` attributes. If you enforce a strict CSP, you may need:

```html
<meta http-equiv="Content-Security-Policy"
      content="default-src 'self'; script-src 'self' 'unsafe-inline' cdn.jsdelivr.net; style-src 'self' 'unsafe-inline' cdn.jsdelivr.net; img-src 'self' data:;">
```

Adjust CDN domains based on your asset configuration.

---

## Dependency Security

### CDN vs Local Assets

By default, Faststrap loads Bootstrap, HTMX, and other assets from CDN. For maximum security, vendor these assets locally:

```python
from faststrap import add_bootstrap, get_assets

add_bootstrap(app, cdn=False)  # Serve assets locally
get_assets(app, dest="./static/faststrap")
```

See the [Static Files Guide](../STATIC_FILES.md) for details.

---

## Reporting Security Vulnerabilities

If you discover a security vulnerability in Faststrap, please report it responsibly:

1. **Do not** open a public GitHub issue.
2. Email the maintainers directly or use the private vulnerability reporting feature on GitHub.
3. Include reproduction steps, affected versions, and suggested fix if possible.
4. Allow reasonable time for a patch before public disclosure.

We aim to acknowledge reports within 48 hours and release patches for critical vulnerabilities within 7 days.