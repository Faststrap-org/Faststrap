"""HTMX Server Response Helpers.

Utilities for setting HTMX response headers and creating common response patterns.
These helpers eliminate boilerplate for HTMX server-side interactions.
"""

import json
from typing import Any

from starlette.responses import Response

from ..components.feedback.toast import Toast


def hx_redirect(url: str, status_code: int = 200) -> Response:
    """Return a response that triggers a client-side redirect via HTMX.

    Args:
        url: URL to redirect to
        status_code: HTTP status code (default: 200)

    Returns:
        Response with HX-Redirect header

    Example:
        After successful form submission:
        >>> @app.post("/login")
        >>> def login(req):
        >>>     # ... authenticate user ...
        >>>     return hx_redirect("/dashboard")

        Redirect with 303 See Other:
        >>> return hx_redirect("/success", status_code=303)

    Note:
        This triggers a full page redirect on the client side.
        For partial page updates, use regular HTMX responses.
    """
    return Response(
        content="",
        status_code=status_code,
        headers={"HX-Redirect": url},
    )


def hx_refresh(status_code: int = 200) -> Response:
    """Return a response that triggers a full page refresh via HTMX.

    Args:
        status_code: HTTP status code (default: 200)

    Returns:
        Response with HX-Refresh header

    Example:
        After data mutation that affects multiple parts of the page:
        >>> @app.post("/update-settings")
        >>> def update_settings(req):
        >>>     # ... update settings ...
        >>>     return hx_refresh()

    Note:
        Use sparingly. Prefer targeted updates with hx-target when possible.
    """
    return Response(
        content="",
        status_code=status_code,
        headers={"HX-Refresh": "true"},
    )


def hx_trigger(
    event: str | dict[str, Any],
    detail: Any | None = None,
    status_code: int = 200,
    content: str = "",
) -> Response:
    """Return a response that triggers a client-side event via HTMX.

    Args:
        event: Event name or dict of events with details
        detail: Event detail data (only used if event is a string)
        status_code: HTTP status code (default: 200)
        content: Optional response content

    Returns:
        Response with HX-Trigger header

    Example:
        Simple event:
        >>> return hx_trigger("itemUpdated")

        Event with detail:
        >>> return hx_trigger("itemUpdated", detail={"id": 123})

        Multiple events:
        >>> return hx_trigger({
        ...     "itemUpdated": {"id": 123},
        ...     "showNotification": {"message": "Saved!"}
        ... })

    Note:
        Client-side JavaScript can listen for these events:
        ```javascript
        document.body.addEventListener("itemUpdated", function(evt){
            console.log(evt.detail);
        });
        ```
    """
    if isinstance(event, str):
        if detail is not None:
            trigger_value = json.dumps({event: detail})
        else:
            trigger_value = event
    else:
        trigger_value = json.dumps(event)

    return Response(
        content=content,
        status_code=status_code,
        headers={"HX-Trigger": trigger_value},
    )


def hx_reswap(strategy: str, status_code: int = 200, content: str = "") -> Response:
    """Return a response that changes the swap strategy via HTMX.

    Args:
        strategy: Swap strategy (innerHTML, outerHTML, beforebegin, afterbegin, etc.)
        status_code: HTTP status code (default: 200)
        content: Response content

    Returns:
        Response with HX-Reswap header

    Example:
        Change swap strategy dynamically:
        >>> @app.get("/widget")
        >>> def widget(req):
        >>>     if req.query_params.get("replace"):
        >>>         return hx_reswap("outerHTML", content="<div>New widget</div>")
        >>>     return hx_reswap("innerHTML", content="Widget content")

    Note:
        Valid strategies: innerHTML, outerHTML, beforebegin, afterbegin,
        beforeend, afterend, delete, none
    """
    return Response(
        content=content,
        status_code=status_code,
        headers={"HX-Reswap": strategy},
    )


def hx_retarget(selector: str, status_code: int = 200, content: str = "") -> Response:
    """Return a response that changes the target element via HTMX.

    Args:
        selector: CSS selector for new target
        status_code: HTTP status code (default: 200)
        content: Response content

    Returns:
        Response with HX-Retarget header

    Example:
        Dynamically change target based on condition:
        >>> @app.post("/save")
        >>> def save(req):
        >>>     if error:
        >>>         return hx_retarget("#error-panel", content=Alert("Error!"))
        >>>     return hx_retarget("#success-panel", content=Alert("Saved!"))

    Note:
        This overrides the hx-target attribute specified in the request.
    """
    return Response(
        content=content,
        status_code=status_code,
        headers={"HX-Retarget": selector},
    )


def toast_response(
    content: Any,
    message: str,
    variant: str = "success",
    toast_id: str = "toast-container",
    **toast_kwargs: Any,
) -> Any:
    """Return content with an out-of-band toast notification.

    This is a killer feature: return your normal HTMX response PLUS a toast
    notification that appears in a separate part of the page.

    Args:
        content: Main response content (HTML)
        message: Toast message text
        variant: Toast variant (success, danger, warning, info)
        toast_id: ID of the toast container element
        **toast_kwargs: Additional Toast component kwargs

    Returns:
        Tuple of (content, toast with hx-swap-oob)

    Example:
        Success notification after save:
        >>> @app.post("/save")
        >>> def save(req):
        >>>     # ... save logic ...
        >>>     return toast_response(
        >>>         content=Card("Record updated!"),
        >>>         message="Changes saved successfully",
        >>>         variant="success"
        >>>     )

        Error notification:
        >>> return toast_response(
        >>>     content=Form(...),  # Re-render form
        >>>     message="Validation failed",
        >>>     variant="danger"
        >>> )

    Note:
        Your page must have a toast container element:
        ```python
        ToastContainer(id="toast-container")
        ```

        The toast will be swapped into this container using HTMX's
        out-of-band swap feature (hx-swap-oob).
    """

    # Create toast with OOB swap
    toast = Toast(
        message,
        variant=variant,  # type: ignore
        hx_swap_oob=f"afterbegin:#{toast_id}",
        **toast_kwargs,
    )

    # Return both content and OOB toast
    # HTMX will swap content into target AND toast into container
    if isinstance(content, (list, tuple)):
        return (*content, toast)
    return (content, toast)
