"""FilterBar component for composing dashboard filters."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import Div
from fasthtml.common import Form as FTForm

from ...core._stability import beta
from ...core.base import merge_classes
from ...core.registry import register
from ...core.types import VariantType
from ...utils.attrs import convert_attrs
from .button import Button

FilterMode = Literal["auto", "apply"]
FilterMethod = Literal["get", "post"]


@register(category="forms")
@beta
def FilterBar(
    *filters: Any,
    endpoint: str | None = None,
    method: FilterMethod = "get",
    mode: FilterMode = "auto",
    apply_label: str = "Apply",
    apply_variant: VariantType = "primary",
    reset_label: str | None = None,
    reset_href: str | None = None,
    debounce: int = 300,
    hx_target: str | None = None,
    hx_swap: str | None = "outerHTML",
    push_url: bool = False,
    filters_cls: str | None = None,
    actions_cls: str | None = None,
    form_cls: str | None = None,
    **kwargs: Any,
) -> FTForm:
    """Composable filter bar with optional HTMX integration."""
    if method not in {"get", "post"}:
        msg = f"method must be 'get' or 'post', got {method}"
        raise ValueError(msg)
    if mode not in {"auto", "apply"}:
        msg = f"mode must be 'auto' or 'apply', got {mode}"
        raise ValueError(msg)

    form_attrs: dict[str, Any] = {
        "method": method,
        "cls": merge_classes("faststrap-filter-bar", form_cls),
    }

    if endpoint:
        form_attrs["action"] = endpoint
        if method == "get":
            form_attrs["hx_get"] = endpoint
        else:
            form_attrs["hx_post"] = endpoint
        if hx_target:
            form_attrs["hx_target"] = hx_target
        if hx_swap:
            form_attrs["hx_swap"] = hx_swap
        if push_url:
            form_attrs["hx_push_url"] = "true"
        if mode == "auto":
            form_attrs["hx_trigger"] = (
                f"change delay:{debounce}ms, keyup changed delay:{debounce}ms"
            )

    filters_wrap = Div(
        *filters,
        cls=merge_classes("d-flex flex-wrap gap-3 align-items-end", filters_cls),
    )

    actions: list[Any] = []
    if mode == "apply":
        actions.append(Button(apply_label, type="submit", variant=apply_variant))
    if reset_label and reset_href:
        actions.append(Button(reset_label, variant="secondary", outline=True, href=reset_href))

    content: list[Any] = [filters_wrap]
    if actions:
        content.append(Div(*actions, cls=merge_classes("ms-auto d-flex gap-2", actions_cls)))

    form_attrs.update(convert_attrs(kwargs))

    return FTForm(*content, **form_attrs)
