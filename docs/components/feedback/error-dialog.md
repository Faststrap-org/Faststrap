# Error Dialog

The `ErrorDialog` component displays error messages in a Bootstrap modal, perfect for inline errors that don't require a full page reload. It supports retry actions, HTMX out-of-band swaps, and backend error messages.

!!! success "Goal"
    By the end of this guide, you'll be able to show beautiful error modals for AJAX failures, validation errors, and backend exceptions **without writing any JavaScript.**

---

## Quick Start

Here's the simplest way to show an error dialog.

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#demo-error">Show Error</button>
    <div class="modal fade" id="demo-error" tabindex="-1">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title text-danger">Error</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
          </div>
          <div class="modal-body">
            <p>Something went wrong. Please try again.</p>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
ErrorDialog(message="Something went wrong. Please try again.")
```
  </div>
</div>

---

## Visual Examples & Use Cases

### 1. Variants

Different severity levels for different errors.

<div class="component-preview">
  <div class="preview-header">Danger (Default)</div>
  <div class="preview-render">
    <div class="alert alert-danger">
      <strong class="text-danger">Error</strong>
      <p class="mb-0">Failed to save changes</p>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
ErrorDialog(
    message="Failed to save changes",
    variant="danger"
)
```
  </div>
</div>

<div class="component-preview">
  <div class="preview-header">Warning</div>
  <div class="preview-render">
    <div class="alert alert-warning">
      <strong class="text-warning">Warning</strong>
      <p class="mb-0">Your session will expire in 5 minutes</p>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
ErrorDialog(
    message="Your session will expire in 5 minutes",
    title="Warning",
    variant="warning"
)
```
  </div>
</div>

<div class="component-preview">
  <div class="preview-header">Info</div>
  <div class="preview-render">
    <div class="alert alert-info">
      <strong class="text-info">Notice</strong>
      <p class="mb-0">This feature is currently in beta</p>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
ErrorDialog(
    message="This feature is currently in beta",
    title="Notice",
    variant="info"
)
```
  </div>
</div>

### 2. With Retry Action

Let users retry failed operations.

```python
ErrorDialog(
    message="Network timeout. Please try again.",
    retry_url="/api/save",
    retry_text="Retry",
    modal_id="network-error"
)
```

---

## Practical Functionality

### HTMX Integration

Show errors from HTMX requests.

```python
@app.post("/profile/save")
def save_profile(req):
    try:
        update_profile(req.form)
        return Div("Profile saved!", cls="alert alert-success")
    except ValidationError as e:
        # Return error dialog via HTMX
        return ErrorDialog(
            message=str(e),
            title="Validation Error",
            variant="warning"
        )
    except Exception as e:
        return ErrorDialog(
            message="Failed to save profile. Please try again.",
            retry_url="/profile/save",
            retry_text="Try Again"
        )
```

### Out-of-Band Swaps

Show error dialog while updating other content.

```python
@app.post("/cart/add")
def add_to_cart(product_id: int):
    try:
        cart.add(product_id)
        
        # Return updated cart + success message
        return Div(
            CartWidget(cart),
            Toast("Added to cart!", variant="success", hx_swap_oob="true")
        )
    except OutOfStockError:
        # Return cart + error dialog
        return Div(
            CartWidget(cart),
            ErrorDialog(
                message="This item is out of stock",
                modal_id="stock-error",
                hx_swap_oob="true",
                show=True  # Show immediately
            )
        )
```

### Backend Error Messages

Display backend exceptions to users.

```python
@app.post("/api/process")
def process_data(req):
    try:
        result = expensive_operation(req.form)
        return result
    except DatabaseError as e:
        # Show technical error in development
        if app.debug:
            return ErrorDialog(
                message=f"Database error: {e}",
                title="Database Error"
            )
        else:
            # Show user-friendly error in production
            return ErrorDialog(
                message="Unable to process your request. Our team has been notified.",
                retry_url="/api/process"
            )
```

---

## Integration Patterns

### With Form Validation

```python
@app.post("/register")
def register(req):
    email = req.form.get("email")
    password = req.form.get("password")
    
    # Validate
    if not email or "@" not in email:
        return ErrorDialog(
            message="Please enter a valid email address",
            title="Validation Error",
            variant="warning",
            modal_id="validation-error",
            show=True
        )
    
    if len(password) < 8:
        return ErrorDialog(
            message="Password must be at least 8 characters",
            title="Validation Error",
            variant="warning",
            show=True
        )
    
    # Create user
    create_user(email, password)
    return hx_redirect("/dashboard")
```

### With Confirmation Dialogs

Combine with retry for dangerous actions.

```python
@app.delete("/account")
def delete_account(req):
    user = req.session.get("user")
    
    try:
        delete_user(user.id)
        return hx_redirect("/goodbye")
    except Exception as e:
        return ErrorDialog(
            message="Failed to delete account. Please contact support if this persists.",
            title="Deletion Failed",
            retry_url="/account/delete",
            retry_text="Try Again"
        )
```

### Auto-Show on Load

Show error immediately when page loads.

```python
@app.get("/checkout")
def checkout(req):
    cart = get_cart(req)
    
    if cart.is_empty():
        # Show error dialog on page load
        return Container(
            H1("Checkout"),
            ErrorDialog(
                message="Your cart is empty",
                title="Cannot Checkout",
                variant="warning",
                show=True,  # Auto-show
                modal_id="empty-cart"
            )
        )
    
    return CheckoutPage(cart)
```

---

## Parameter Reference

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `message` | `str` | Required | Error message to display |
| `title` | `str` | "Error" | Modal title |
| `variant` | `str` | "danger" | Color variant (danger, warning, info) |
| `modal_id` | `str` | "error-dialog" | Unique modal ID |
| `retry_url` | `str \| None` | `None` | URL for retry button (None to hide) |
| `retry_text` | `str` | "Retry" | Text for retry button |
| `show` | `bool` | `False` | Whether to show modal immediately |
| `**kwargs` | `Any` | - | Additional HTML attributes |

---

## Best Practices

### ✅ Do This

```python
# Use appropriate variants
ErrorDialog(message="Invalid input", variant="warning")
ErrorDialog(message="Server error", variant="danger")
ErrorDialog(message="Feature unavailable", variant="info")

# Provide retry for transient errors
ErrorDialog(
    message="Network timeout",
    retry_url="/api/save",
    retry_text="Try Again"
)

# Use unique IDs for multiple dialogs
ErrorDialog(message="Error 1", modal_id="error-1")
ErrorDialog(message="Error 2", modal_id="error-2")
```

### ❌ Don't Do This

```python
# Don't expose sensitive errors in production
ErrorDialog(message=str(database_connection_string))

# Don't use wrong variants
ErrorDialog(message="Success!", variant="danger")  # Use Toast instead

# Don't reuse modal IDs
ErrorDialog(message="Error 1", modal_id="error")
ErrorDialog(message="Error 2", modal_id="error")  # Conflict!
```

---

::: faststrap.components.feedback.error_dialog.ErrorDialog
    options:
        show_source: true
        heading_level: 4
