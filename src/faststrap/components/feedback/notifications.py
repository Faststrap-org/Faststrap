"""Notification presets built on top of existing Toast/Alert components."""

from __future__ import annotations

from typing import Any, Literal

from ...core.registry import register
from .alert import Alert
from .toast import Toast

NoticeKind = Literal["success", "danger", "warning", "info"]


@register(category="feedback", requires_js=True)
def NoticeToast(
    message: str, kind: NoticeKind = "info", title: str | None = None, **kwargs: Any
) -> Any:
    """Common toast preset."""
    return Toast(message, title=title, variant=kind, **kwargs)


@register(category="feedback", requires_js=True)
def NoticeAlert(message: str, kind: NoticeKind = "info", **kwargs: Any) -> Any:
    """Common alert preset."""
    return Alert(message, variant=kind, **kwargs)


@register(category="feedback", requires_js=True)
def SuccessToast(message: str, title: str = "Success", **kwargs: Any) -> Any:
    return NoticeToast(message=message, title=title, kind="success", **kwargs)


@register(category="feedback", requires_js=True)
def ErrorToast(message: str, title: str = "Error", **kwargs: Any) -> Any:
    return NoticeToast(message=message, title=title, kind="danger", **kwargs)


@register(category="feedback", requires_js=True)
def WarningToast(message: str, title: str = "Warning", **kwargs: Any) -> Any:
    return NoticeToast(message=message, title=title, kind="warning", **kwargs)


@register(category="feedback", requires_js=True)
def InfoToast(message: str, title: str = "Info", **kwargs: Any) -> Any:
    return NoticeToast(message=message, title=title, kind="info", **kwargs)
