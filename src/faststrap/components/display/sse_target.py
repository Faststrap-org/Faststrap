"""SSETarget component for client-side EventSource updates."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import Div

from ...core._stability import beta
from ...core.base import merge_classes
from ...core.registry import register
from ...core.theme import resolve_defaults
from ...utils.attrs import convert_attrs

SSESwapType = Literal[
    "inner",
    "outer",
    "before",
    "after",
    "append",
    "prepend",
    "replace",
    "text",
]


@register(category="display", requires_js=True)
@beta
def SSETarget(
    *children: Any,
    endpoint: str,
    event: str = "message",
    swap: SSESwapType = "inner",
    target: str | None = None,
    with_credentials: bool = False,
    reconnect: bool = True,
    retry: int | None = None,
    aria_live: str | None = "polite",
    content: Any | None = None,
    **kwargs: Any,
) -> Div:
    """Client-side SSE target that updates when new events arrive.

    Args:
        *children: Initial content to render inside the target.
        endpoint: SSE endpoint URL (must return text/event-stream).
        event: SSE event name to listen for (default: "message").
        swap: How to apply incoming data ("inner", "outer", "append", "text", etc.).
        target: Optional CSS selector for a separate element to update.
        with_credentials: Use cookies/credentials with EventSource.
        reconnect: Whether to allow automatic reconnect (default: True).
        retry: Optional reconnect delay hint (milliseconds).
        aria_live: ARIA live region value (default: "polite").
        content: Optional alternative to *children for initial content.
        **kwargs: Additional HTML attributes.
    """
    cfg = resolve_defaults(
        "SSETarget",
        event=event,
        swap=swap,
        with_credentials=with_credentials,
        reconnect=reconnect,
        retry=retry,
        aria_live=aria_live,
    )

    c_event = cfg.get("event", event)
    c_swap = cfg.get("swap", swap)
    c_with_credentials = cfg.get("with_credentials", with_credentials)
    c_reconnect = cfg.get("reconnect", reconnect)
    c_retry = cfg.get("retry", retry)
    c_aria_live = cfg.get("aria_live", aria_live)

    if content is not None and not children:
        children = (content,)

    user_cls = kwargs.pop("cls", "")
    cls = merge_classes("faststrap-sse-target", user_cls)

    attrs: dict[str, Any] = {
        "cls": cls,
        "data_fs_sse": "true",
        "data_fs_sse_endpoint": endpoint,
        "data_fs_sse_event": c_event,
        "data_fs_sse_swap": c_swap,
    }

    if target:
        attrs["data_fs_sse_target"] = target
    if c_with_credentials:
        attrs["data_fs_sse_credentials"] = "true"
    if not c_reconnect:
        attrs["data_fs_sse_reconnect"] = "false"
    if c_retry is not None:
        attrs["data_fs_sse_retry"] = str(c_retry)
    if c_aria_live:
        attrs["aria_live"] = c_aria_live

    attrs.update(convert_attrs(kwargs))

    return Div(*children, **attrs)
