"""Error Page Components.

Full-page and dialog error displays for 404, 500, 403, and custom errors.
Supports backend error messages and customization.
"""

from typing import Any, Literal

from fasthtml.common import H1, Div, Title

from ...core.base import merge_classes
from ...utils.attrs import convert_attrs
from ..display.empty_state import EmptyState

ErrorCodeType = Literal[403, 404, 500]


# Default error messages
_ERROR_DEFAULTS = {
    404: {
        "title": "Page Not Found",
        "message": "The page you're looking for doesn't exist or has been moved.",
        "icon": "exclamation-triangle",
    },
    500: {
        "title": "Server Error",
        "message": "Something went wrong on our end. We're working to fix it.",
        "icon": "x-circle",
    },
    403: {
        "title": "Access Denied",
        "message": "You don't have permission to access this resource.",
        "icon": "shield-lock",
    },
}


def ErrorPage(
    code: ErrorCodeType | int,
    title: str | None = None,
    message: str | None = None,
    icon: str | None = None,
    action_text: str | None = "Go Home",
    action_href: str = "/",
    show_code: bool = True,
    **kwargs: Any,
) -> tuple[Any, ...]:
    """Full-page error display for 404, 500, 403, and custom errors.

    Renders a centered, styled error page with icon, title, message, and action button.
    Supports custom backend error messages.

    Args:
        code: HTTP error code (404, 500, 403, or custom)
        title: Custom error title (uses default if None)
        message: Custom error message (uses default if None, supports backend errors)
        icon: Bootstrap icon name (uses default if None)
        action_text: Text for action button (None to hide button)
        action_href: URL for action button
        show_code: Whether to display the error code
        **kwargs: Additional HTML attributes for the container

    Returns:
        Tuple of (Title, ErrorPage Div) for FastHTML page rendering

    Example:
        Default 404 page:
        >>> ErrorPage(404)

        Custom 500 with backend error:
        >>> ErrorPage(500, message="Database connection timeout")

        Custom 403 with custom action:
        >>> ErrorPage(
        ...     403,
        ...     title="Premium Feature",
        ...     message="Upgrade your plan to access this feature",
        ...     action_text="View Plans",
        ...     action_href="/pricing"
        ... )

        Custom error code:
        >>> ErrorPage(
        ...     418,
        ...     title="I'm a teapot",
        ...     message="This server refuses to brew coffee",
        ...     icon="cup-hot"
        ... )

        Hide action button:
        >>> ErrorPage(500, action_text=None)

    Note:
        Returns a tuple for use in FastHTML routes:
        ```python
        @app.get("/404")
        def not_found():
            return ErrorPage(404)
        ```

        For backend errors, pass the error message directly:
        ```python
        try:
            # ... operation ...
        except Exception as e:
            return ErrorPage(500, message=str(e))
        ```
    """
    # Get defaults for known error codes
    defaults = _ERROR_DEFAULTS.get(code, {})

    # Use custom values or defaults
    final_title = title or defaults.get("title", f"Error {code}")
    final_message = message or defaults.get("message", "An error occurred.")
    final_icon = icon or defaults.get("icon", "exclamation-circle")

    # Build error code display
    code_display = None
    if show_code:
        code_display = H1(
            str(code),
            cls="display-1 fw-bold text-muted opacity-25",
            style="font-size: 8rem;",
        )

    # Build classes
    base_classes = ["min-vh-100", "d-flex", "align-items-center", "justify-content-center"]
    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes(" ".join(base_classes), user_cls)

    # Build attributes
    attrs: dict[str, Any] = {"cls": all_classes}
    attrs.update(convert_attrs(kwargs))

    # Use EmptyState for the error display
    error_content = EmptyState(
        title=final_title,
        description=final_message,
        icon=final_icon,
        action_text=action_text,
        action_href=action_href if action_text else None,
        cls="text-center",
    )

    # Wrap in container with code display
    page_content = Div(
        code_display,
        error_content,
        **attrs,
    )

    # Return Title + Page for FastHTML
    page_title = Title(f"{code} - {final_title}")

    return (page_title, page_content)
