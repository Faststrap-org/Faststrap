"""Searchable Select Component.

Server-side searchable dropdown using HTMX.
"""

import hashlib
import json
from typing import Any

from fasthtml.common import A, Div, Input, Option, Select

from ...core.base import merge_classes
from ...core.registry import register
from ...core.theme import resolve_defaults
from ...core.types import SizeType
from ...utils.attrs import convert_attrs


def _stable_searchable_select_id(
    *,
    endpoint: str,
    name: str,
    placeholder: str,
    min_chars: int,
    debounce: int,
) -> str:
    digest = hashlib.sha1(
        json.dumps(
            {
                "endpoint": endpoint,
                "name": name,
                "placeholder": placeholder,
                "min_chars": min_chars,
                "debounce": debounce,
            },
            sort_keys=True,
        ).encode("utf-8")
    ).hexdigest()[:8]
    return f"searchable-select-{digest}"


@register(category="forms")
def SearchableSelect(
    endpoint: str,
    name: str,
    placeholder: str = "Search...",
    min_chars: int = 2,
    debounce: int = 300,
    initial_options: list[tuple[str, str]] | None = None,
    required: bool = False,
    size: SizeType | None = None,
    select_id: str | None = None,
    csp_safe: bool = False,
    **kwargs: Any,
) -> Div:
    """Server-side searchable dropdown using HTMX.

    Replaces client-side libraries like Select2/Choices.js with pure
    server-side filtering. As user types, sends requests to server
    which returns filtered options.

    Args:
        endpoint: Server endpoint for search (receives 'q' query param)
        name: Form field name
        placeholder: Search input placeholder
        initial_options: Initial options as list of (value, text) tuples
        debounce: Milliseconds to wait after typing before searching
        min_chars: Minimum characters before triggering search
        select_id: Unique ID for the select element
        csp_safe: Avoid inline click handlers by using delegated listeners
            from FastStrap init script.
        **kwargs: Additional HTML attributes

    Returns:
        Div containing search input and select dropdown

    Example:
        Basic usage:
        >>> SearchableSelect(
        ...     endpoint="/api/users/search",
        ...     name="user_id",
        ...     placeholder="Search users..."
        ... )

        With initial options:
        >>> SearchableSelect(
        ...     endpoint="/api/countries/search",
        ...     name="country",
        ...     initial_options=[
        ...         ("us", "United States"),
        ...         ("uk", "United Kingdom"),
        ...     ]
        ... )

        Server-side handler:
        ```python
        @app.get("/api/users/search")
        def search_users(q: str = ""):
            if len(q) < 2:
                return ""

            users = db.query(User).filter(
                User.name.ilike(f"%{q}%")
            ).limit(10).all()

            return Div(*[
                A(
                    user.name,
                    href="#",
                    cls="list-group-item list-group-item-action",
                    data_value=user.id,
                )
                for user in users
            ])
        ```

    Note:
        The server endpoint should:
        1. Receive 'q' query parameter with search term
        2. Filter results server-side
        3. Return HTML options to replace the results container

        For better UX, consider:
        - Showing loading indicator during search
        - Handling empty results gracefully
        - Limiting results to prevent overwhelming the UI
    """
    if initial_options is None:
        initial_options = []

    # Resolve API defaults
    cfg = resolve_defaults("SearchableSelect", size=size)
    c_size = cfg.get("size", None)

    # Generate ID if not provided
    if select_id is None:
        select_id = _stable_searchable_select_id(
            endpoint=endpoint,
            name=name,
            placeholder=placeholder,
            min_chars=min_chars,
            debounce=debounce,
        )

    results_id = f"{select_id}-results"
    input_id = f"{select_id}-input"
    safe_select_id = json.dumps(select_id)
    safe_input_id = json.dumps(input_id)
    safe_results_id = json.dumps(results_id)

    # Build input classes
    input_classes = ["form-control"]
    if c_size:
        input_classes.append(f"form-control-{c_size}")
    input_classes.append("mb-2")

    # Build search input
    search_input = Input(
        type="search",
        id=input_id,
        placeholder=placeholder,
        cls=" ".join(input_classes),
        hx_get=endpoint,
        hx_trigger=f"keyup changed delay:{debounce}ms",
        hx_target=f"#{results_id}",
        hx_swap="innerHTML",
        autocomplete="off",
        minlength=min_chars if min_chars > 0 else None,
    )

    # Build initial options as list-group items
    option_elements = []
    for value, text in initial_options:
        option_attrs: dict[str, Any] = {
            "href": "#",
            "cls": "list-group-item list-group-item-action",
            "data_value": value,
        }
        if csp_safe:
            option_attrs.update(
                {
                    "data_fs_searchable_option": "true",
                    "data_fs_select_id": select_id,
                    "data_fs_input_id": input_id,
                    "data_fs_results_id": results_id,
                    "data_fs_label": text,
                    "data_fs_value": value,
                }
            )
        else:
            option_attrs["hx-on:click"] = (
                "event.preventDefault();"
                f"const sel=document.getElementById({safe_select_id});"
                "if(!sel){return;}"
                "sel.innerHTML='';"
                "const opt=document.createElement('option');"
                f"opt.value={json.dumps(value)};"
                f"opt.text={json.dumps(text)};"
                "opt.selected=true;"
                "sel.appendChild(opt);"
                f"const inp=document.getElementById({safe_input_id});"
                f"if(inp){{inp.value={json.dumps(text)};}}"
                f"const box=document.getElementById({safe_results_id});"
                "if(box){box.innerHTML='';}"
            )
        option_elements.append(A(text, **option_attrs))

    # Build results container
    results_container = Div(
        *option_elements,
        id=results_id,
        cls="list-group",
        style="max-height: 300px; overflow-y: auto;",
    )

    # Build hidden select for form submission
    hidden_options = [Option(text, value=value) for value, text in initial_options]
    hidden_select = Select(
        *hidden_options,
        name=name,
        id=select_id,
        cls="d-none",
        required=required,
        tabindex="-1",
        aria_hidden="true",
    )

    # Build container
    base_classes = ["searchable-select"]
    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes(" ".join(base_classes), user_cls)

    attrs: dict[str, Any] = {"cls": all_classes}
    if csp_safe:
        attrs["data_fs_searchable_select"] = "true"
    attrs.update(convert_attrs(kwargs))

    return Div(
        search_input,
        results_container,
        hidden_select,
        **attrs,
    )
