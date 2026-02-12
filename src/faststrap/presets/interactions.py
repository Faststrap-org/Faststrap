"""HTMX Interaction Presets.

Ready-to-use components for common HTMX patterns like live search,
infinite scroll, auto-refresh, and lazy loading.
"""

from typing import Any

from fasthtml.common import Div, Input

from ..components.forms.button import Button
from ..core.base import merge_classes
from ..utils.attrs import convert_attrs


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
    # Build HTMX attributes
    hx_attrs = {
        "hx_get": endpoint,
        "hx_target": target,
        "hx_trigger": trigger,
        "hx_swap": kwargs.pop("hx_swap", "beforeend"),
    }

    # Add intersection observer threshold if not default
    if threshold != "0px":
        hx_attrs["hx_trigger"] = f"{trigger} threshold:{threshold}"

    # Merge with user-provided HTMX attrs
    for key in ["hx_indicator", "hx_push_url"]:
        if key in kwargs:
            hx_attrs[key] = kwargs.pop(key)

    # Build classes
    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes("infinite-scroll-trigger", user_cls)

    # Build final attributes
    attrs: dict[str, Any] = {
        "cls": all_classes,
        **hx_attrs,
    }
    attrs.update(convert_attrs(kwargs))

    # Default content: loading indicator
    content = kwargs.pop("content", Div("Loading more...", cls="text-center text-muted py-3"))

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

    # Build final attributes
    attrs: dict[str, Any] = {
        "cls": all_classes,
        **hx_attrs,
    }
    attrs.update(convert_attrs(kwargs))

    # Default content
    content = kwargs.pop("content", Div("Loading...", cls="text-muted"))

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
        variant=kwargs.pop("variant", "primary"),  # type: ignore
        loading=False,  # We'll use hx-indicator instead
        **hx_attrs,  # type: ignore
        **kwargs,
    )
