# Error Page

The `ErrorPage` component provides beautiful, full-page error displays for common HTTP errors (404, 500, 403) and custom error scenarios. It returns a tuple of `(Title, Content)` ready for FastHTML route rendering, with sensible defaults and full customization support.

!!! success "Goal"
    By the end of this guide, you'll be able to create professional error pages that handle both standard HTTP errors and backend exceptions, **with zero HTML/CSS knowledge required.**

---

## Quick Start

Here's the simplest way to create a 404 error page.

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="min-vh-100 d-flex align-items-center justify-content-center">
      <div class="text-center">
        <h1 class="display-1 fw-bold text-muted opacity-25" style="font-size: 8rem;">404</h1>
        <i class="bi bi-exclamation-triangle text-warning" style="font-size: 4rem;"></i>
        <h1 class="h4 mt-3">Page Not Found</h1>
        <p class="text-muted">The page you're looking for doesn't exist or has been moved.</p>
        <a href="/" class="btn btn-primary btn-lg mt-3">Go Home</a>
      </div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
@app.get("/404")
def not_found():
    return ErrorPage(404)
```
  </div>
</div>

---

## Visual Examples & Use Cases

### 1. Standard HTTP Errors

ErrorPage comes with beautiful defaults for the most common HTTP errors.

<div class="component-preview">
  <div class="preview-header">404 - Page Not Found</div>
  <div class="preview-render">
    <div class="text-center p-5">
      <i class="bi bi-exclamation-triangle text-warning" style="font-size: 3rem;"></i>
      <h2 class="mt-3">Page Not Found</h2>
      <p class="text-muted">The page you're looking for doesn't exist or has been moved.</p>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
# Automatic title, message, and icon
ErrorPage(404)
```
  </div>
</div>

<div class="component-preview">
  <div class="preview-header">500 - Server Error</div>
  <div class="preview-render">
    <div class="text-center p-5">
      <i class="bi bi-x-circle text-danger" style="font-size: 3rem;"></i>
      <h2 class="mt-3">Server Error</h2>
      <p class="text-muted">Something went wrong on our end. We're working to fix it.</p>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
# Different icon and message for 500
ErrorPage(500)
```
  </div>
</div>

<div class="component-preview">
  <div class="preview-header">403 - Access Denied</div>
  <div class="preview-render">
    <div class="text-center p-5">
      <i class="bi bi-shield-lock text-danger" style="font-size: 3rem;"></i>
      <h2 class="mt-3">Access Denied</h2>
      <p class="text-muted">You don't have permission to access this resource.</p>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
# Locked shield icon for 403
ErrorPage(403)
```
  </div>
</div>

### 2. Backend Error Messages

The killer feature: pass backend exceptions directly to the error page.

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="text-center p-5">
      <i class="bi bi-x-circle text-danger" style="font-size: 3rem;"></i>
      <h2 class="mt-3">Server Error</h2>
      <p class="text-muted">Database connection timeout after 30 seconds</p>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
@app.get("/data")
def get_data():
    try:
        data = db.query(...)
    except Exception as e:
        # Pass the exception message directly!
        return ErrorPage(500, message=str(e))
```
  </div>
</div>

**Real-World Example:**

```python
@app.post("/profile/save")
def save_profile(req):
    try:
        user = req.session.get("user")
        if not user:
            return ErrorPage(403, message="Please log in to continue")
        
        # ... save logic ...
        db.commit()
        return hx_redirect("/profile")
        
    except DatabaseError as e:
        return ErrorPage(500, message=f"Database error: {e}")
    except ValidationError as e:
        return ErrorPage(400, message=f"Invalid data: {e}")
```

### 3. Custom Error Pages

Create branded error pages for your app.

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="text-center p-5">
      <i class="bi bi-cup-hot text-info" style="font-size: 3rem;"></i>
      <h2 class="mt-3">I'm a teapot</h2>
      <p class="text-muted">This server refuses to brew coffee</p>
      <a href="/tea" class="btn btn-info mt-3">Try Tea Instead</a>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
# Custom 418 error (yes, it's real!)
ErrorPage(
    418,
    title="I'm a teapot",
    message="This server refuses to brew coffee",
    icon="cup-hot",
    action_text="Try Tea Instead",
    action_href="/tea"
)
```
  </div>
</div>

---

## Practical Functionality

### Hiding the Error Code

Sometimes you don't want to show the big error number.

```python
# No giant "404" display
ErrorPage(404, show_code=False)
```

### Custom Action Buttons

Change where the button goes or what it says.

```python
# Go to dashboard instead of home
ErrorPage(
    404,
    action_text="Back to Dashboard",
    action_href="/dashboard"
)

# Hide the button entirely
ErrorPage(500, action_text=None)
```

### Premium Feature Paywall

Use 403 errors creatively for feature gating.

```python
@app.get("/premium-feature")
@require_auth()
def premium_feature(req):
    user = req.session.get("user")
    
    if not user.is_premium:
        return ErrorPage(
            403,
            title="Premium Feature",
            message="Upgrade your plan to access this feature",
            action_text="View Plans",
            action_href="/pricing"
        )
    
    return render_premium_feature()
```

---

## Integration Patterns

### With FastHTML Routes

ErrorPage returns a tuple for direct route rendering.

```python
from fasthtml.common import *
from faststrap import ErrorPage

app = FastHTML()

@app.get("/404")
def not_found():
    # Returns (Title(...), Div(...))
    return ErrorPage(404)

@app.get("/500")
def server_error():
    return ErrorPage(500)
```

### With Exception Handlers

Create a global error handler.

```python
@app.exception_handler(404)
def handle_404(req, exc):
    return ErrorPage(404)

@app.exception_handler(500)
def handle_500(req, exc):
    # Log the error
    logger.error(f"Server error: {exc}")
    
    # Show user-friendly message in production
    if app.debug:
        return ErrorPage(500, message=str(exc))
    else:
        return ErrorPage(500)  # Use default message
```

### With HTMX Requests

Detect HTMX requests and return inline errors instead.

```python
@app.get("/data")
def get_data(req):
    try:
        data = fetch_data()
        return render_data(data)
    except Exception as e:
        # Check if it's an HTMX request
        if req.headers.get("HX-Request"):
            # Return inline error dialog
            from faststrap import ErrorDialog
            return ErrorDialog(message=str(e))
        else:
            # Return full error page
            return ErrorPage(500, message=str(e))
```

---

## Parameter Reference

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `code` | `int` | Required | HTTP error code (404, 500, 403, or custom) |
| `title` | `str \| None` | Auto | Custom error title (uses default if None) |
| `message` | `str \| None` | Auto | Custom error message (supports backend errors) |
| `icon` | `str \| None` | Auto | Bootstrap icon name (e.g., "exclamation-triangle") |
| `action_text` | `str \| None` | "Go Home" | Text for action button (None to hide) |
| `action_href` | `str` | "/" | URL for action button |
| `show_code` | `bool` | `True` | Whether to display large error code |
| `**kwargs` | `Any` | - | Additional HTML attributes for container |

### Default Messages

| Code | Title | Message | Icon |
| :--- | :--- | :--- | :--- |
| 404 | Page Not Found | The page you're looking for doesn't exist... | exclamation-triangle |
| 500 | Server Error | Something went wrong on our end... | x-circle |
| 403 | Access Denied | You don't have permission... | shield-lock |
| Other | Error {code} | An error occurred. | exclamation-circle |

---

## Best Practices

### ✅ Do This

```python
# Pass backend errors in development
if app.debug:
    return ErrorPage(500, message=str(exception))

# Use semantic error codes
return ErrorPage(403)  # Not authorized
return ErrorPage(404)  # Not found
return ErrorPage(500)  # Server error

# Customize action buttons
return ErrorPage(404, action_text="Search", action_href="/search")
```

### ❌ Don't Do This

```python
# Don't expose sensitive errors in production
return ErrorPage(500, message=str(database_connection_string))

# Don't use wrong error codes
return ErrorPage(404)  # When user lacks permission (use 403)
return ErrorPage(500)  # For validation errors (use 400)
```

---

::: faststrap.components.feedback.error_page.ErrorPage
    options:
        show_source: true
        heading_level: 4
