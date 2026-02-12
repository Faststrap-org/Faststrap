"""Theme Toggle Component.

Dark/light mode toggle with HTMX server-side persistence.
"""

from typing import Any, Literal

from fasthtml.common import Div, I, Input, Label

from ...core.base import merge_classes
from ...utils.attrs import convert_attrs

ThemeType = Literal["light", "dark", "auto"]


def ThemeToggle(
    current_theme: ThemeType = "auto",
    endpoint: str = "/theme/toggle",
    toggle_id: str = "theme-toggle",
    show_label: bool = False,
    label_text: str = "Dark Mode",
    **kwargs: Any,
) -> Div:
    """Dark/light mode toggle switch with HTMX persistence.

    Creates a toggle switch that POSTs to a server endpoint to persist
    theme preference. The server should handle the toggle logic and return
    updated UI or trigger a page refresh.

    Args:
        current_theme: Current theme ("light", "dark", "auto")
        endpoint: Server endpoint to POST theme changes
        toggle_id: Unique ID for the toggle
        show_label: Whether to show label text
        label_text: Label text to display
        **kwargs: Additional HTML attributes

    Returns:
        Div containing the theme toggle switch

    Example:
        Basic toggle:
        >>> ThemeToggle()

        With label:
        >>> ThemeToggle(
        ...     current_theme="dark",
        ...     show_label=True,
        ...     label_text="Dark Mode"
        ... )

        Custom endpoint:
        >>> ThemeToggle(
        ...     endpoint="/api/user/theme",
        ...     toggle_id="user-theme-toggle"
        ... )

        Server-side handler:
        ```python
        @app.post("/theme/toggle")
        def toggle_theme(req: Request):
            current = req.session.get("theme", "light")
            new_theme = "dark" if current == "light" else "light"
            req.session["theme"] = new_theme

            # Return updated UI or trigger refresh
            from faststrap.presets import hx_refresh
            return hx_refresh()
        ```

    Note:
        The toggle uses Bootstrap's form-check-input styling.
        The server endpoint should:
        1. Read current theme from session/cookie
        2. Toggle to new theme
        3. Save to session/cookie
        4. Return response (refresh, redirect, or updated HTML)
    """
    # Determine if checked
    is_checked = current_theme == "dark"

    # Build toggle input
    toggle_input = Input(
        type="checkbox",
        cls="form-check-input",
        id=toggle_id,
        checked=is_checked,
        role="switch",
        hx_post=endpoint,
        hx_trigger="change",
        hx_swap="none",  # Server handles the update
    )

    # Build label
    label_element = None
    if show_label:
        label_element = Label(
            label_text,
            cls="form-check-label ms-2",
            **{"for": toggle_id},
        )

    # Build icon (optional visual enhancement)
    icon_class = "bi-moon-stars-fill" if is_checked else "bi-sun-fill"
    icon = I(cls=f"bi {icon_class} me-2")

    # Build container
    base_classes = ["form-check", "form-switch", "d-flex", "align-items-center"]
    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes(" ".join(base_classes), user_cls)

    attrs: dict[str, Any] = {"cls": all_classes}
    attrs.update(convert_attrs(kwargs))

    # Assemble toggle
    elements = [icon, toggle_input]
    if label_element:
        elements.append(label_element)

    return Div(*elements, **attrs)
