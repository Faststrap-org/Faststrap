"""Error Dialog Component.

Modal/dialog variant for inline error display with backend error support.
"""

from typing import Any

from fasthtml.common import Div, P

from ...core.types import VariantType
from ...utils.icons import Icon
from ..forms.button import Button
from .modal import Modal


def ErrorDialog(
    message: str,
    title: str = "Error",
    variant: VariantType | None = None,
    modal_id: str = "error-dialog",
    retry_url: str | None = None,
    retry_text: str = "Retry",
    close_text: str = "Close",
    show: bool = True,
    **kwargs: Any,
) -> Any:
    """Modal/dialog variant for inline error display.

    Shows error messages from backend or client-side validation in a modal dialog.
    Supports retry actions and custom styling.

    Args:
        message: Error message to display (can be from backend)
        title: Dialog title
        variant: Bootstrap variant for styling (danger, warning, info)
        modal_id: Unique ID for the modal
        retry_url: Optional URL to retry the failed action (shows retry button)
        retry_text: Text for retry button
        close_text: Text for close button
        show: Whether to show modal immediately
        **kwargs: Additional HTML attributes

    Returns:
        Modal component with error content

    Example:
        Basic error dialog:
        >>> ErrorDialog(message="Failed to save record")

        Backend error with retry:
        >>> ErrorDialog(
        ...     message="Network timeout. Please try again.",
        ...     retry_url="/api/save",
        ...     retry_text="Try Again"
        ... )

        Custom variant and title:
        >>> ErrorDialog(
        ...     message="This action requires premium access",
        ...     title="Access Restricted",
        ...     variant="warning",
        ...     retry_url="/pricing",
        ...     retry_text="Upgrade Now"
        ... )

        HTMX integration (show on error):
        >>> @app.post("/save")
        >>> def save(req):
        >>>     try:
        >>>         # ... save logic ...
        >>>         return Card("Success!")
        >>>     except Exception as e:
        >>>         return ErrorDialog(
        >>>             message=str(e),
        >>>             modal_id="save-error",
        >>>             hx_swap_oob="true"
        >>>         )

    Note:
        For full-page errors, use `ErrorPage` instead.

        The dialog can be triggered via HTMX out-of-band swaps:
        ```python
        # Server returns error dialog alongside main content
        return (main_content, ErrorDialog(message="Error", hx_swap_oob="true"))
        ```

        Or shown programmatically with Bootstrap's modal API:
        ```javascript
        new bootstrap.Modal(document.getElementById('error-dialog')).show();
        ```
    """
    # Resolve API defaults
    from ...core.theme import resolve_defaults

    cfg = resolve_defaults("ErrorDialog", variant=variant)
    c_variant = cfg.get("variant", "danger")

    # Build icon based on variant
    icon_map = {
        "danger": "x-circle-fill",
        "warning": "exclamation-triangle-fill",
        "info": "info-circle-fill",
        "success": "check-circle-fill",
    }
    icon_name = icon_map.get(c_variant, "exclamation-circle-fill")

    # Build error content
    error_icon = Div(
        Icon(icon_name),
        cls=f"text-{c_variant} fs-1 mb-3",
    )

    error_message = P(
        message,
        cls="mb-0",
    )

    error_content = Div(
        error_icon,
        error_message,
        cls="text-center py-3",
    )

    # Build footer buttons
    footer_buttons = []

    if retry_url:
        retry_btn = Button(
            retry_text,
            variant=c_variant,
            hx_get=retry_url,
            hx_target=f"#{modal_id}",
            hx_swap="outerHTML",
            data_bs_dismiss="modal",
        )
        footer_buttons.append(retry_btn)

    close_btn = Button(
        close_text,
        variant="secondary" if retry_url else c_variant,
        data_bs_dismiss="modal",
    )
    footer_buttons.append(close_btn)

    # Build modal
    modal = Modal(
        error_content,
        modal_id=modal_id,
        title=title,
        footer=Div(*footer_buttons, cls="d-flex gap-2 justify-content-end w-100"),
        centered=True,
        **kwargs,
    )

    # Auto-show if requested
    if show:
        # Add script to show modal on load
        from fasthtml.common import Script

        show_script = Script(f"new bootstrap.Modal(document.getElementById('{modal_id}')).show();")
        return (modal, show_script)

    return modal
