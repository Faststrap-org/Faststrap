# @require_auth - Route Protection

Decorator to protect routes with session-based authentication. Checks if the specified session key exists. If not, redirects to the login page.

!!! success "Stability: Stable"
    This decorator is stable and ready for production use.

## Usage

```python
from faststrap.presets import require_auth

@app.get("/dashboard")
@require_auth()
def dashboard(request):
    user = request.session.get("user")
    return Container(H1(f"Welcome, {user['name']}"))
```

## Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `login_url` | `str` | `"/login"` | URL to redirect to if unauthenticated |
| `session_key` | `str` | `"user"` | Session key to check for auth |
| `redirect_param` | `str \| None` | `"next"` | Query param name for return URL, `None` to disable |

## How It Works

1. User visits `/dashboard` -> not authenticated
2. Redirects to `/login?next=/dashboard`
3. After login, read `?next=` to redirect back:

```python
@app.post("/login")
def login(request, email: str, password: str):
    # ... authenticate ...
    request.session["user"] = {"name": "Alice", "email": email}
    next_url = request.query_params.get("next", "/dashboard")
    return RedirectResponse(next_url, status_code=303)
```

## Custom Session Key

```python
@app.get("/admin")
@require_auth(login_url="/admin/login", session_key="admin_user")
def admin_panel(request):
    return AdminLayout(...)
```

## Without Return URL

```python
@app.get("/profile")
@require_auth(redirect_param=None)
def profile(request):
    return ProfilePage(...)
```

!!! note "What this does NOT do"
    `@require_auth` only checks session presence. It does NOT:

    - Handle login/logout logic
    - Manage JWT tokens
    - Validate permissions or roles

    For those, implement your own auth service. This just guards the gate.
