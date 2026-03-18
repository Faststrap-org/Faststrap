"""HTMX Interaction Presets.

Ready-to-use components for common HTMX patterns like live search,
infinite scroll, auto-refresh, lazy loading, and optimistic UI actions.
"""

import json
from typing import Any

from fasthtml.common import Div, Input

from ..components.forms.button import Button
from ..core.base import merge_classes
from ..utils.attrs import convert_attrs


def _is_numeric_threshold(value: str) -> bool:
    try:
        parsed = float(value)
    except (TypeError, ValueError):
        return False
    return 0.0 <= parsed <= 1.0


def _build_optimistic_dispatch_script(event_name: str, detail: dict[str, Any]) -> str:
    """Build a small inline script that dispatches a bubbling CustomEvent."""
    event_json = json.dumps(event_name)
    detail_json = json.dumps(detail)
    return (
        f"this.dispatchEvent(new CustomEvent({event_json}, "
        f"{{bubbles:true,detail:{detail_json}}}));"
    )


def ActiveSearch(
    endpoint: str,
    target: str,
    debounce: int = 300,
    placeholder: str = "Search...",
    name: str = "q",
    **kwargs: Any,
) -> Input:
    """Live search input with debounced server requests.

    Replaces client-side search libraries with pure HTMX server-side filtering.

    Args:
        endpoint: Server endpoint to send search requests (e.g., "/api/search")
        target: CSS selector for where to render results (e.g., "#results")
        debounce: Milliseconds to wait after typing before sending request
        placeholder: Input placeholder text
        name: Form field name for the search query
        **kwargs: Additional HTML attributes (cls, id, etc.)

    Returns:
        Input element with HTMX search attributes

    Example:
        Basic usage:
        >>> ActiveSearch(endpoint="/search", target="#results")

        Custom debounce and styling:
        >>> ActiveSearch(
        ...     endpoint="/api/users/search",
        ...     target="#user-list",
        ...     debounce=500,
        ...     placeholder="Search users...",
        ...     cls="form-control-lg"
        ... )

        With additional HTMX attributes:
        >>> ActiveSearch(
        ...     endpoint="/search",
        ...     target="#results",
        ...     hx_indicator="#spinner",
        ...     hx_swap="innerHTML"
        ... )

    Note:
        Uses `hx-trigger="keyup changed delay:{debounce}ms"` for debouncing.
        The server endpoint should accept the search query as a query parameter
        with the name specified in the `name` argument (default: "q").
    """
    # Build HTMX attributes
    hx_attrs = {
        "hx_get": endpoint,
        "hx_target": target,
        "hx_trigger": f"keyup changed delay:{debounce}ms",
    }

    # Merge with user-provided HTMX attrs (allow override)
    for key in ["hx_indicator", "hx_swap", "hx_push_url"]:
        if key in kwargs:
            hx_attrs[key] = kwargs.pop(key)

    # Build classes
    base_classes = ["form-control"]
    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes(" ".join(base_classes), user_cls)

    # Build final attributes
    attrs: dict[str, Any] = {
        "cls": all_classes,
        "type": "search",
        "name": name,
        "placeholder": placeholder,
        **hx_attrs,
    }
    attrs.update(convert_attrs(kwargs))

    return Input(**attrs)


def InfiniteScroll(
    endpoint: str,
    target: str,
    trigger: str = "revealed",
    threshold: str = "0px",
    **kwargs: Any,
) -> Div:
    """Infinite scroll trigger element.

    Loads more content when scrolled into view. Place at the bottom of your list/feed.

    Args:
        endpoint: Server endpoint to fetch next page (e.g., "/api/feed?page=2")
        target: CSS selector for where to append results (usually same as parent)
        trigger: HTMX trigger event (default: "revealed")
        threshold: Intersection observer threshold (default: "0px")
        **kwargs: Additional HTML attributes

    Returns:
        Div element that triggers loading when scrolled into view

    Example:
        Basic usage:
        >>> InfiniteScroll(endpoint="/feed?page=2", target="#feed")

        Custom trigger threshold:
        >>> InfiniteScroll(
        ...     endpoint="/api/posts?page=3",
        ...     target="#post-list",
        ...     threshold="200px"  # Trigger 200px before visible
        ... )

        With loading indicator:
        >>> InfiniteScroll(
        ...     endpoint="/feed?page=2",
        ...     target="#feed",
        ...     hx_indicator="#loading-spinner"
        ... )

    Note:
        The endpoint should return HTML that will be appended to the target.
        Use `hx-swap="afterend"` to append after the trigger element itself.
    """
    normalized_trigger = trigger.strip()
    normalized_threshold = threshold.strip()

    # Build HTMX attributes
    hx_attrs = {
        "hx_get": endpoint,
        "hx_target": target,
        "hx_trigger": normalized_trigger,
        "hx_swap": kwargs.pop("hx_swap", "beforeend"),
    }

    # Add supported threshold handling without breaking existing callers.
    if normalized_threshold != "0px" and normalized_trigger in {"revealed", "intersect"}:
        if _is_numeric_threshold(normalized_threshold):
            hx_attrs["hx_trigger"] = f"intersect once threshold:{normalized_threshold}"
        else:
            hx_attrs["hx_trigger"] = "faststrap:infinite-scroll once"
            kwargs["data"] = {
                **(kwargs.get("data") if isinstance(kwargs.get("data"), dict) else {}),
                "fs_infinite_scroll": True,
                "fs_infinite_margin": normalized_threshold,
            }

    # Merge with user-provided HTMX attrs
    for key in ["hx_indicator", "hx_push_url"]:
        if key in kwargs:
            hx_attrs[key] = kwargs.pop(key)

    # Build classes
    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes("infinite-scroll-trigger", user_cls)

    # Extract content BEFORE converting remaining attrs
    content = kwargs.pop("content", Div("Loading more...", cls="text-center text-muted py-3"))

    # Build final attributes
    attrs: dict[str, Any] = {
        "cls": all_classes,
        **hx_attrs,
    }
    attrs.update(convert_attrs(kwargs))

    return Div(content, **attrs)


def AutoRefresh(
    endpoint: str,
    target: str,
    interval: int = 5000,
    **kwargs: Any,
) -> Div:
    """Auto-refreshing content section.

    Polls the server at regular intervals and updates content.

    Args:
        endpoint: Server endpoint to poll (e.g., "/api/metrics")
        target: CSS selector for where to render updates (usually self with "this")
        interval: Milliseconds between requests (default: 5000 = 5 seconds)
        **kwargs: Additional HTML attributes

    Returns:
        Div element that auto-refreshes its content

    Example:
        Basic usage (refreshes itself):
        >>> AutoRefresh(endpoint="/metrics", target="this", interval=10000)

        Refresh specific target:
        >>> AutoRefresh(
        ...     endpoint="/api/stats",
        ...     target="#stats-panel",
        ...     interval=3000
        ... )

        With initial content:
        >>> AutoRefresh(
        ...     endpoint="/api/status",
        ...     target="this",
        ...     interval=5000,
        ...     content=Div("Loading status...")
        ... )

    Note:
        Use `target="this"` to replace the AutoRefresh element itself.
        The server should return HTML that will replace the target content.
    """
    # Build HTMX attributes
    hx_attrs = {
        "hx_get": endpoint,
        "hx_target": target,
        "hx_trigger": f"every {interval}ms",
        "hx_swap": kwargs.pop("hx_swap", "innerHTML"),
    }

    # Merge with user-provided HTMX attrs
    for key in ["hx_indicator"]:
        if key in kwargs:
            hx_attrs[key] = kwargs.pop(key)

    # Build classes
    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes("auto-refresh", user_cls)

    # Extract content BEFORE converting remaining attrs
    content = kwargs.pop("content", Div("Loading...", cls="text-muted"))

    # Build final attributes
    attrs: dict[str, Any] = {
        "cls": all_classes,
        **hx_attrs,
    }
    attrs.update(convert_attrs(kwargs))

    return Div(content, **attrs)


def LazyLoad(
    endpoint: str,
    trigger: str = "revealed",
    placeholder: Any | None = None,
    **kwargs: Any,
) -> Div:
    """Lazy-loaded content block.

    Loads content from server when scrolled into view.

    Args:
        endpoint: Server endpoint to fetch content (e.g., "/api/widget")
        trigger: HTMX trigger event (default: "revealed")
        placeholder: Content to show before loading (default: "Loading...")
        **kwargs: Additional HTML attributes

    Returns:
        Div element that loads content on reveal

    Example:
        Basic usage:
        >>> LazyLoad(endpoint="/api/heavy-widget")

        Custom placeholder:
        >>> LazyLoad(
        ...     endpoint="/api/chart",
        ...     placeholder=Spinner()
        ... )

        Load on click instead of reveal:
        >>> LazyLoad(
        ...     endpoint="/api/details",
        ...     trigger="click",
        ...     placeholder=Button("Load Details")
        ... )

    Note:
        Perfect for below-the-fold content, charts, or heavy components.
        The server endpoint should return HTML to replace the placeholder.
    """
    # Build HTMX attributes
    hx_attrs = {
        "hx_get": endpoint,
        "hx_trigger": trigger,
        "hx_swap": kwargs.pop("hx_swap", "outerHTML"),
    }

    # Merge with user-provided HTMX attrs
    for key in ["hx_target", "hx_indicator"]:
        if key in kwargs:
            hx_attrs[key] = kwargs.pop(key)

    # Build classes
    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes("lazy-load", user_cls)

    # Build final attributes
    attrs: dict[str, Any] = {
        "cls": all_classes,
        **hx_attrs,
    }
    attrs.update(convert_attrs(kwargs))

    # Default placeholder
    if placeholder is None:
        placeholder = Div("Loading...", cls="text-center text-muted py-3")

    return Div(placeholder, **attrs)


def LoadingButton(
    *children: Any,
    endpoint: str,
    method: str = "post",
    target: str | None = None,
    variant: str = "primary",
    **kwargs: Any,
) -> Any:
    """Button with automatic loading state during HTMX requests.

    Shows spinner and disables during request. Uses HTMX's built-in `hx-indicator`
    and `hx-disabled-elt` attributes.

    Args:
        *children: Button content (text, icons, etc.)
        endpoint: Server endpoint for the request
        method: HTTP method ("get", "post", "put", "delete")
        target: CSS selector for where to render response (optional)
        variant: Bootstrap button variant
        **kwargs: Additional HTML attributes

    Returns:
        Button component with loading state

    Example:
        Basic POST button:
        >>> LoadingButton("Save", endpoint="/save", target="#form")

        GET request with custom variant:
        >>> LoadingButton(
        ...     "Load More",
        ...     endpoint="/api/items",
        ...     method="get",
        ...     target="#items",
        ...     variant="outline-primary"
        ... )

        DELETE with confirmation:
        >>> LoadingButton(
        ...     "Delete",
        ...     endpoint="/delete/123",
        ...     method="delete",
        ...     variant="danger",
        ...     hx_confirm="Are you sure?"
        ... )

    Note:
        The button automatically disables during the request and shows
        a spinner. No custom JavaScript required.
    """
    # Build HTMX attributes
    hx_method_attr = f"hx_{method}"
    hx_attrs = {
        hx_method_attr: endpoint,
        "hx_disabled_elt": "this",  # Disable button during request
    }

    if target:
        hx_attrs["hx_target"] = target

    # Default indicator to "this" if not provided
    if "hx_indicator" not in kwargs:
        hx_attrs["hx_indicator"] = "this"

    # Merge with user-provided HTMX attrs
    for key in ["hx_swap", "hx_confirm", "hx_indicator", "hx_push_url"]:
        if key in kwargs:
            hx_attrs[key] = kwargs.pop(key)

    # Use the existing Button component
    return Button(
        *children,
        variant=variant,  # type: ignore
        loading=False,  # We'll use hx-indicator instead
        **hx_attrs,  # type: ignore
        **kwargs,
    )


def OptimisticAction(
    *children: Any,
    endpoint: str,
    method: str = "post",
    target: str | None = None,
    action_id: str | None = None,
    payload: dict[str, Any] | None = None,
    apply_event: str = "faststrap:optimistic:apply",
    commit_event: str = "faststrap:optimistic:commit",
    rollback_event: str = "faststrap:optimistic:rollback",
    variant: str = "primary",
    **kwargs: Any,
) -> Any:
    """Button preset for optimistic UI updates with explicit rollback contract.

    Event contract:
    - `apply_event`: fired before request starts
    - `commit_event`: fired after successful response
    - `rollback_event`: fired on failed/network error responses

    All events dispatch from the button element with bubbling enabled and
    include a detail object:
    `{actionId, endpoint, method, target, payload, reason}`.
    """
    normalized_method = method.lower()
    if normalized_method not in {"get", "post", "put", "patch", "delete"}:
        msg = f"Unsupported HTTP method for OptimisticAction: {method!r}"
        raise ValueError(msg)

    resolved_action_id = action_id or f"{normalized_method}:{endpoint}"
    resolved_payload: dict[str, Any] = payload or {}

    base_detail = {
        "actionId": resolved_action_id,
        "endpoint": endpoint,
        "method": normalized_method,
        "target": target,
        "payload": resolved_payload,
    }

    before_script = _build_optimistic_dispatch_script(
        apply_event,
        {**base_detail, "reason": "before-request"},
    )
    commit_script = (
        "if(event.detail.successful){"
        + _build_optimistic_dispatch_script(
            commit_event,
            {**base_detail, "reason": "success"},
        )
        + "}"
    )
    rollback_script = _build_optimistic_dispatch_script(
        rollback_event,
        {**base_detail, "reason": "response-error"},
    )
    rollback_send_error_script = _build_optimistic_dispatch_script(
        rollback_event,
        {**base_detail, "reason": "network-error"},
    )

    hx_method_attr = f"hx_{normalized_method}"
    hx_attrs: dict[str, Any] = {
        hx_method_attr: endpoint,
        "hx_disabled_elt": "this",
        "hx-on::before-request": before_script,
        "hx-on::after-request": commit_script,
        "hx-on::response-error": rollback_script,
        "hx-on::send-error": rollback_send_error_script,
    }

    if target:
        hx_attrs["hx_target"] = target

    if "hx_indicator" not in kwargs:
        hx_attrs["hx_indicator"] = "this"

    for key in ["hx_swap", "hx_confirm", "hx_indicator", "hx_push_url"]:
        if key in kwargs:
            hx_attrs[key] = kwargs.pop(key)

    data_attrs = kwargs.pop("data", {})
    if not isinstance(data_attrs, dict):
        data_attrs = {}
    data_attrs = {
        **data_attrs,
        "faststrap_optimistic_id": resolved_action_id,
        "faststrap_optimistic_endpoint": endpoint,
        "faststrap_optimistic_method": normalized_method,
    }
    kwargs["data"] = data_attrs

    return Button(
        *children,
        variant=variant,  # type: ignore[arg-type]
        loading=False,
        **hx_attrs,  # type: ignore[arg-type]
        **kwargs,
    )


def LocationAction(
    *children: Any,
    endpoint: str | None = None,
    method: str = "post",
    target: str | None = None,
    success_event: str = "faststrap:location:success",
    error_event: str = "faststrap:location:error",
    variant: str = "secondary",
    **kwargs: Any,
) -> Any:
    """Progressive location helper with explicit permission/error events.

    Behavior:
    - Requests browser geolocation on click
    - Dispatches bubbling success/error custom events
    - Optionally sends coordinates via HTMX (`htmx.ajax`) when endpoint is set
    """
    endpoint_js = json.dumps(endpoint) if endpoint else "null"
    target_js = json.dumps(target) if target else "null"
    method_js = json.dumps(method.upper())
    success_event_js = json.dumps(success_event)
    error_event_js = json.dumps(error_event)

    onclick_script = (
        "if(!navigator.geolocation){"
        f"this.dispatchEvent(new CustomEvent({error_event_js},{{bubbles:true,detail:{{reason:'unsupported'}}}}));"
        "return;"
        "}"
        "navigator.geolocation.getCurrentPosition((pos)=>{"
        "const detail={latitude:pos.coords.latitude,longitude:pos.coords.longitude,accuracy:pos.coords.accuracy};"
        f"this.dispatchEvent(new CustomEvent({success_event_js},{{bubbles:true,detail}}));"
        f"const endpoint={endpoint_js};"
        f"const target={target_js};"
        f"const method={method_js};"
        "if(endpoint && window.htmx){"
        "htmx.ajax(method, endpoint, {target: target || this, values: detail});"
        "}"
        "},(err)=>{"
        f"this.dispatchEvent(new CustomEvent({error_event_js},{{bubbles:true,detail:{{reason:'denied',code:err.code,message:err.message}}}}));"
        "});"
    )

    return Button(
        *children if children else ("Share location",),
        variant=variant,  # type: ignore[arg-type]
        type="button",
        onclick=onclick_script,
        **kwargs,
    )
