"""KaTeX-based math/chemistry formula rendering component."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Div, NotStr, Span

from ...core._stability import beta
from ...core.base import merge_classes
from ...core.registry import register
from ...core.theme import UNSET, resolve_defaults
from ...utils.attrs import convert_attrs


def _normalize_delimiters(latex: str, display_mode: bool) -> str:
    if display_mode:
        return f"$${latex}$$"
    return f"\\({latex}\\)"


@register(category="display", requires_js=True)
@beta
def Math(
    latex: str,
    *,
    display_mode: bool | None = UNSET,
    throw_on_error: bool | None = UNSET,
    renderer: str = "katex",
    **kwargs: Any,
) -> Div | Span:
    """Render LaTeX math using KaTeX.

    Supports chemistry notation via the mhchem extension
    (``\\ce{}``, ``\\cee{}``, reaction arrows, etc.).

    Requires KaTeX to be loaded in the page. Faststrap does not
    inject KaTeX automatically; include it in your app assets or
    use a CDN.

    Args:
        latex: LaTeX math source.
        display_mode: Render as block-level display math when True.
        throw_on_error: Raise on unsupported LaTeX instead of rendering
            the source as fallback text.
        renderer: Rendering backend. Only ``"katex"`` is supported
            currently; ``"mathjax"`` is reserved for future use.
        **kwargs: Additional HTML attributes for the wrapper element.

    Returns:
        FastHTML ``Span`` for inline math or ``Div`` for display math,
        containing delimited LaTeX for KaTeX auto-rendering.

    Examples:
        Basic math:

        >>> Math(r"\frac{a}{b}")

        Display mode:

        >>> Math(r"\\int_{-\\infty}^{\\infty} e^{-x^2} dx", display_mode=True)

        Chemistry:

        >>> Math(r"\\ce{2H2 + O2 -> 2H2O}")

        Physics:

        >>> Math(r"F = G \frac{m_1 m_2}{r^2}")
    """
    cfg = resolve_defaults(
        "Math",
        display_mode=display_mode,
        throw_on_error=throw_on_error,
        renderer=renderer,
    )
    c_display_mode = cfg.get("display_mode", False)
    c_throw_on_error = cfg.get("throw_on_error", False)
    c_renderer = cfg.get("renderer", renderer)

    if c_renderer != "katex":
        raise ValueError(
            f"Unsupported math renderer: {c_renderer!r}. " "Currently only 'katex' is supported."
        )

    wrapped = _normalize_delimiters(latex, c_display_mode)
    user_cls = kwargs.pop("cls", "")
    base_cls = "math faststrap-math"
    if c_display_mode:
        base_cls += " faststrap-math-display"

    attrs: dict[str, Any] = {
        "cls": merge_classes(base_cls, user_cls),
        "data_fs_math_display": "true" if c_display_mode else "false",
        "data_fs_math_throw_on_error": "true" if c_throw_on_error else "false",
    }
    attrs.update(convert_attrs(kwargs))

    if c_display_mode:
        return Div(NotStr(wrapped), **attrs)
    return Span(NotStr(wrapped), **attrs)
