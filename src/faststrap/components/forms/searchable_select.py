"""Searchable Select Component.

Server-side searchable dropdown using HTMX.
"""

from typing import Any

from fasthtml.common import A, Div, Input, Select

from ...core.base import merge_classes
from ...core.theme import resolve_defaults
from ...core.types import SizeType
from ...utils.attrs import convert_attrs


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

            options = [
                Option(user.name, value=user.id)
                for user in users
            ]
            return Div(*options, id="user-options")
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
        import uuid

        select_id = f"searchable-select-{uuid.uuid4().hex[:8]}"

    results_id = f"{select_id}-results"

    # Build input classes
    input_classes = ["form-control"]
    if c_size:
        input_classes.append(f"form-control-{c_size}")
    input_classes.append("mb-2")

    # Build search input
    search_input = Input(
        type="search",
        placeholder=placeholder,
        cls=" ".join(input_classes),
        hx_get=endpoint,
        hx_trigger=f"keyup changed delay:{debounce}ms",
        hx_target=f"#{results_id}",
        hx_swap="innerHTML",
        autocomplete="off",
    )

    # Build initial options as list-group items
    option_elements = [
        A(text, href="#", cls="list-group-item list-group-item-action", data_value=value)
        for value, text in initial_options
    ]

    # Build results container
    results_container = Div(
        *option_elements,
        id=results_id,
        cls="list-group",
        style="max-height: 300px; overflow-y: auto;",
    )

    # Build hidden select for form submission
    hidden_select = Select(
        name=name,
        id=select_id,
        cls="d-none",
    )

    # Build container
    base_classes = ["searchable-select"]
    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes(" ".join(base_classes), user_cls)

    attrs: dict[str, Any] = {"cls": all_classes}
    attrs.update(convert_attrs(kwargs))

    return Div(
        search_input,
        results_container,
        hidden_select,
        **attrs,
    )
