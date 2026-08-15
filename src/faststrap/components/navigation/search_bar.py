"""SearchBar navigation component."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Div, Form, Input

from ...core._stability import experimental
from ...core.base import merge_classes
from ...core.registry import register
from ...utils.attrs import convert_attrs


@register(category="navigation")
@experimental
def SearchBar(
    placeholder: str = "Search...",
    *,
    endpoint: str | None = None,
    target: str | None = None,
    swap: str = "innerHTML",
    name: str = "q",
    method: str = "get",
    autocomplete: str = "off",
    **kwargs: Any,
) -> Div:
    """Polished global search input with optional HTMX integration.

    Renders a search form with an icon-prefixed input. When ``endpoint``
    is provided, the form submits via HTMX and swaps results into
    ``target``.

    Args:
        placeholder: Input placeholder text.
        endpoint: HTMX endpoint to query for search results.
        target: HTMX target selector for results.
        swap: HTMX swap strategy.
        name: Query parameter name for the search term.
        method: HTTP method for the search request.
        autocomplete: Input autocomplete attribute.
        **kwargs: Additional HTML attributes for the wrapper.

    Returns:
        FastHTML ``Div`` element containing the search form.
    """
    user_cls = kwargs.pop("cls", "")

    input_attrs: dict[str, Any] = {
        "type": "search",
        "name": name,
        "placeholder": placeholder,
        "autocomplete": autocomplete,
        "cls": "form-control",
    }
    if endpoint:
        input_attrs["hx_get"] = endpoint
        input_attrs["hx_target"] = target or "#search-results"
        input_attrs["hx_swap"] = swap
        input_attrs["hx_trigger"] = "input changed delay:300ms"
        input_attrs["hx_include"] = f"[name='{name}']"

    form_kwargs: dict[str, Any] = {"cls": "faststrap-search-bar", "role": "search"}
    if endpoint:
        form_kwargs["hx_get"] = endpoint
        form_kwargs["hx_target"] = target or "#search-results"
        form_kwargs["hx_swap"] = swap

    form_cls = merge_classes("faststrap-search-bar", user_cls)
    form_attrs: dict[str, Any] = {
        "cls": form_cls,
        "role": "search",
    }
    if endpoint:
        form_attrs["hx_get"] = endpoint
        form_attrs["hx_target"] = target or "#search-results"
        form_attrs["hx_swap"] = swap
    form_attrs.update(convert_attrs(kwargs))

    return Div(
        Form(
            Input(**input_attrs),
            method=method,
            **(
                {"hx_get": endpoint, "hx_target": target or "#search-results", "hx_swap": swap}
                if endpoint
                else {}
            ),
        ),
        **form_attrs,
    )
