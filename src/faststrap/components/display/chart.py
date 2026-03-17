"""Chart component for rendering matplotlib, plotly, or altair outputs."""

from __future__ import annotations

from io import StringIO
from typing import Any, Literal

from fasthtml.common import Div, NotStr

from ...core._stability import beta
from ...core.base import merge_classes
from ...core.registry import register
from ...utils.attrs import convert_attrs

ChartBackend = Literal["matplotlib", "plotly", "altair", "svg", "html"]


def _normalize_size(value: str | int | None) -> str | None:
    if value is None:
        return None
    if isinstance(value, int):
        return f"{value}px"
    return value


def _matplotlib_to_svg(fig: Any) -> str:
    buffer = StringIO()
    fig.savefig(buffer, format="svg", bbox_inches="tight")
    return str(buffer.getvalue())


def _to_html(fig: Any, *, include_js: bool) -> str:
    try:
        return str(
            fig.to_html(
                full_html=False,
                include_plotlyjs="cdn" if include_js else False,
            )
        )
    except TypeError:
        return str(fig.to_html())


@register(category="display")
@beta
def Chart(
    figure: Any,
    *,
    backend: ChartBackend | None = None,
    include_js: bool = False,
    responsive: bool = True,
    width: str | int | None = None,
    height: str | int | None = None,
    allow_unsafe_html: bool = False,
    **kwargs: Any,
) -> Div:
    """Render a chart from common Python plotting backends.

    Args:
        figure: Matplotlib figure, Plotly/Altair chart, or raw SVG/HTML string.
        backend: Explicit backend name. If None, attempts to infer from object.
        include_js: Include Plotly JS when rendering Plotly charts.
        responsive: Apply responsive sizing classes.
        width: Optional width (px or CSS string).
        height: Optional height (px or CSS string).
        allow_unsafe_html: Allow raw HTML/SVG strings to be embedded.
        **kwargs: Additional HTML attributes for the wrapper.
    """
    content: str

    if backend is None:
        if hasattr(figure, "savefig"):
            backend = "matplotlib"
        elif hasattr(figure, "to_html"):
            backend = "plotly"
        elif isinstance(figure, str):
            msg = "Chart backend must be specified when passing a raw string."
            raise ValueError(msg)
        else:
            msg = "Unable to infer chart backend. Please pass backend explicitly."
            raise TypeError(msg)

    if backend == "matplotlib":
        content = _matplotlib_to_svg(figure)
    elif backend in {"plotly", "altair"}:
        content = _to_html(figure, include_js=include_js)
    elif backend in {"svg", "html"}:
        if not isinstance(figure, str):
            msg = f"Chart backend '{backend}' expects a string input."
            raise TypeError(msg)
        if not allow_unsafe_html:
            msg = "allow_unsafe_html=True is required to embed raw HTML/SVG strings."
            raise ValueError(msg)
        content = figure
    else:
        msg = f"Unsupported chart backend: {backend}"
        raise ValueError(msg)

    classes = ["faststrap-chart"]
    if responsive:
        classes.append("w-100")

    user_cls = kwargs.pop("cls", "")
    wrapper_cls = merge_classes(" ".join(classes), user_cls)

    style: dict[str, Any] = {}
    normalized_width = _normalize_size(width)
    normalized_height = _normalize_size(height)
    if normalized_width:
        style["width"] = normalized_width
    if normalized_height:
        style["height"] = normalized_height

    attrs: dict[str, Any] = {"cls": wrapper_cls}
    if style:
        attrs["style"] = style
    attrs.update(convert_attrs(kwargs))

    return Div(NotStr(content), **attrs)
