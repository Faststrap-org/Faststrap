"""Bootstrap Confirm Dialog component."""

from typing import Any

from fasthtml.common import Div, P

from ...core.registry import register
from ...core.types import VariantType
from ..feedback.modal import Modal
from ..forms.button import Button


@register(category="feedback", requires_js=True)
def ConfirmDialog(
    message: str | Any,
    *,
    confirm_text: str = "Confirm",
    cancel_text: str = "Cancel",
    title: str = "Confirm Action",
    variant: VariantType = "danger",
    dialog_id: str | None = None,
    hx_confirm_method: str = "post",
    hx_confirm_url: str | None = None,
    hx_target: str | None = None,
    hx_swap: str | None = None,
    **kwargs: Any,
) -> Div:
    """Bootstrap Confirmation Dialog (pre-configured Modal).

    A modal designed for confirming destructive actions.

    Args:
        message: Body text
        confirm_text: Text for confirm button
        cancel_text: Text for cancel button
        title: Modal title
        variant: Variant for confirm button (danger, primary, etc.)
        dialog_id: ID for the modal
        hx_confirm_method: HTMX method for confirm button (post, delete, put, get)
        hx_confirm_url: URL to call on confirmation
        hx_target: HTMX target
        hx_swap: HTMX swap strategy
        **kwargs: Additional HTML attributes passed to Modal

    Returns:
        Modal component

    Example:
        >>> ConfirmDialog(
        ...     "Are you sure you want to delete this?",
        ...     hx_confirm_url="/delete/1",
        ...     confirm_text="Delete",
        ...     variant="danger"
        ... )
    """
    # Build confirm button with HTMX attributes
    btn_attrs: dict[str, Any] = {
        "variant": variant,
        "data_bs_dismiss": "modal",
    }

    if hx_confirm_url:
        # We pass hx arguments directly to Button
        if hx_confirm_method == "get":
            btn_attrs["hx_get"] = hx_confirm_url
        elif hx_confirm_method == "post":
            btn_attrs["hx_post"] = hx_confirm_url
        elif hx_confirm_method == "put":
            btn_attrs["hx_put"] = hx_confirm_url
        elif hx_confirm_method == "patch":
            btn_attrs["hx_patch"] = hx_confirm_url
        elif hx_confirm_method == "delete":
            btn_attrs["hx_delete"] = hx_confirm_url

    if hx_target:
        btn_attrs["hx_target"] = hx_target

    if hx_swap:
        btn_attrs["hx_swap"] = hx_swap

    footer = Div(
        Button(cancel_text, variant="secondary", data_bs_dismiss="modal"),
        Button(confirm_text, **btn_attrs),
        cls="d-flex justify-content-end gap-2",
    )

    return Modal(
        P(message) if isinstance(message, str) else message,
        title=title,
        footer=footer,
        modal_id=dialog_id,
        centered=True,
        **kwargs,
    )
