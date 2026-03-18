"""Bootstrap Hero component."""

from typing import Any

from fasthtml.common import H1, Div, P

from ...core._stability import stable
from ...core.base import merge_classes
from ...core.registry import register
from ...core.types import VariantType
from ...utils.attrs import convert_attrs
from .grid import Container


@register(category="layout")
@stable
def Hero(
    title: str,
    subtitle: str | None = None,
    cta: Any | None = None,
    align: str = "center",
    bg_variant: VariantType | None = None,
    bg_color: str | None = None,
    text_color: str | None = None,
    py: str = "5",
    container: bool = True,
    **kwargs: Any,
) -> Div:
    """Bootstrap Hero component (Jumbotron style).

    A large showcase section for landing pages.

    Args:
        title: Main headline
        subtitle: Subheadline or description
        cta: Call to action component (Button or group)
        align: Text alignment (center, start, end)
        bg_variant: Background variant (light, dark, primary, etc.)
        bg_color: Custom background color (CSS class or hex if style)
        text_color: Text color class (e.g. text-white)
        py: Vertical padding (default: 5)
        container: Wrap content in Container (default: True)
        **kwargs: Additional HTML attributes

    Returns:
        FastHTML Div element

    Example:
        >>> Hero(
        ...     "Welcome",
        ...     "Building great apps",
        ...     cta=Button("Get Started"),
        ...     bg_variant="light"
        ... )
    """
    # Background logic
    classes = [f"py-{py}", f"text-{align}"]

    if bg_variant:
        classes.append(f"bg-{bg_variant}")
        if bg_variant in ("primary", "secondary", "success", "danger", "dark"):
            if not text_color:
                classes.append("text-white")

    if bg_color:
        classes.append(f"bg-{bg_color}" if not bg_color.startswith("#") else "")
        # If hex, add to style
        if bg_color.startswith("#"):
            style = kwargs.get("style", {})
            if isinstance(style, dict):
                style["background-color"] = bg_color
                kwargs["style"] = style

    if text_color:
        classes.append(text_color)

    user_cls = kwargs.pop("cls", "")
    wrapper_cls = merge_classes(" ".join(classes), user_cls)

    attrs: dict[str, Any] = {"cls": wrapper_cls}
    attrs.update(convert_attrs(kwargs))

    # Internal content
    content = []
    content.append(H1(title, cls="display-5 fw-bold"))

    if subtitle:
        content.append(P(subtitle, cls="col-lg-8 mx-auto lead" if align == "center" else "lead"))

    if cta:
        content.append(
            Div(
                cta,
                cls=(
                    "d-grid gap-2 d-sm-flex justify-content-sm-center"
                    if align == "center"
                    else "d-grid gap-2 d-sm-flex"
                ),
            )
        )

    inner = Div(*content, cls="px-4")

    if container:
        return Div(Container(inner), **attrs)

    return Div(inner, **attrs)
