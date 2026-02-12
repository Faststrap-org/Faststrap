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
)
from .responses import (
    hx_redirect,
    hx_refresh,
    hx_reswap,
    hx_retarget,
    hx_trigger,
    toast_response,
)

__all__ = [
    # Interactions
    "ActiveSearch",
    "AutoRefresh",
    "InfiniteScroll",
    "LazyLoad",
    "LoadingButton",
    # Responses
    "hx_redirect",
    "hx_refresh",
    "hx_reswap",
    "hx_retarget",
    "hx_trigger",
    "toast_response",
    # Auth
    "require_auth",
]
