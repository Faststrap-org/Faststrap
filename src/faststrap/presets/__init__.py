"""Faststrap Presets — HTMX Interaction Helpers.

This module provides ready-to-use HTMX patterns and server-side response helpers
that eliminate boilerplate for common web interactions.

Includes:
- Interaction presets (ActiveSearch, InfiniteScroll, AutoRefresh, etc.)
- Response helpers (hx_redirect, hx_refresh, toast_response, etc.)
- Route protection (@require_auth decorator)
"""

from .auth import require_auth
from .interactions import (
    ActiveSearch,
    AutoRefresh,
    InfiniteScroll,
    LazyLoad,
    LoadingButton,
    LocationAction,
    OptimisticAction,
)
from .responses import (
    hx_redirect,
    hx_refresh,
    hx_reswap,
    hx_retarget,
    hx_trigger,
    toast_response,
)
from .streams import SSEStream, sse_comment, sse_event

__all__ = [
    # Interactions
    "ActiveSearch",
    "AutoRefresh",
    "InfiniteScroll",
    "LazyLoad",
    "LocationAction",
    "LoadingButton",
    "OptimisticAction",
    # Responses
    "hx_redirect",
    "hx_refresh",
    "hx_reswap",
    "hx_retarget",
    "hx_trigger",
    "toast_response",
    # Streams
    "SSEStream",
    "sse_event",
    "sse_comment",
    # Auth
    "require_auth",
]
