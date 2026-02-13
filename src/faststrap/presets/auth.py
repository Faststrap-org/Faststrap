"""Route Protection Decorator.

Simple session-based authentication guard for FastHTML routes.
"""

import asyncio
from collections.abc import Callable
from functools import wraps
from typing import Any

from starlette.requests import Request
from starlette.responses import RedirectResponse


def require_auth(
    login_url: str = "/login",
    session_key: str = "user",
    redirect_param: str | None = "next",
) -> Callable:
    """Decorator to protect routes with session-based authentication.

    Checks if the specified session key exists. If not, redirects to login page.
    Optionally preserves the original URL as a query parameter for post-login redirect.

    Args:
        login_url: URL to redirect to if not authenticated (default: "/login")
        session_key: Session key to check for authentication (default: "user")
        redirect_param: Query param name for original URL (default: "next", None to disable)

    Returns:
        Decorator function

    Example:
        Basic usage:
        >>> from faststrap.presets import require_auth
        >>>
        >>> @app.get("/dashboard")
        >>> @require_auth()
        >>> def dashboard(req: Request):
        >>>     user = req.session.get("user")
        >>>     return DashboardLayout(f"Welcome, {user['name']}")

        Custom login URL and session key:
        >>> @app.get("/admin")
        >>> @require_auth(login_url="/admin/login", session_key="admin_user")
        >>> def admin_panel(req: Request):
        >>>     return AdminLayout(...)

        Disable redirect parameter:
        >>> @app.get("/profile")
        >>> @require_auth(redirect_param=None)
        >>> def profile(req: Request):
        >>>     return ProfilePage(...)

    Note:
        This decorator only checks for session presence. It does NOT:
        - Handle login/logout logic
        - Manage JWT tokens
        - Validate permissions/roles

        For those, implement your own auth service. This just guards the gate.

        After login, redirect to the original URL:
        ```python
        @app.post("/login")
        def login(req: Request):
            # ... authenticate ...
            req.session["user"] = user_data
            next_url = req.query_params.get("next", "/dashboard")
            return RedirectResponse(next_url, status_code=303)
        ```
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        async def async_wrapper(request: Request, *args: Any, **kwargs: Any) -> Any:
            # Check if user is authenticated
            if session_key not in request.session:
                # Build redirect URL with optional next parameter
                redirect_to = login_url
                if redirect_param:
                    original_url = str(request.url)
                    redirect_to = f"{login_url}?{redirect_param}={original_url}"

                return RedirectResponse(redirect_to, status_code=303)

            # User is authenticated, proceed
            if asyncio.iscoroutinefunction(func):
                return await func(request, *args, **kwargs)
            return func(request, *args, **kwargs)

        @wraps(func)
        def sync_wrapper(request: Request, *args: Any, **kwargs: Any) -> Any:
            # Check if user is authenticated
            if session_key not in request.session:
                # Build redirect URL with optional next parameter
                redirect_to = login_url
                if redirect_param:
                    original_url = str(request.url)
                    redirect_to = f"{login_url}?{redirect_param}={original_url}"

                return RedirectResponse(redirect_to, status_code=303)

            # User is authenticated, proceed
            return func(request, *args, **kwargs)

        # Return appropriate wrapper based on function type
        if asyncio.iscoroutinefunction(func):
            return async_wrapper
        return sync_wrapper

    return decorator
