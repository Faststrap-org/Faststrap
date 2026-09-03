"""Optional Chart.js integration for Faststrap."""

from __future__ import annotations

import json
from typing import Any, Literal

from fasthtml.common import Canvas, Div, NotStr, Script

from ..core.base import merge_classes
from ..utils.attrs import convert_attrs

CHARTJS_VERSION = "4.4.7"
CHARTJS_CDN_URL = f"https://cdn.jsdelivr.net/npm/chart.js@{CHARTJS_VERSION}/dist/chart.umd.min.js"

ChartJSType = Literal["line", "bar", "pie", "doughnut", "radar", "polarArea", "bubble", "scatter"]


def chartjs_assets(
    *,
    version: str = CHARTJS_VERSION,
    cdn_url: str | None = None,
    defer: bool = True,
) -> tuple[Any, ...]:
    """Return script tags required by Chart.js."""
    source = cdn_url or f"https://cdn.jsdelivr.net/npm/chart.js@{version}/dist/chart.umd.min.js"
    return (Script(src=source, defer=defer),)


def add_chartjs(
    app: Any,
    *,
    version: str = CHARTJS_VERSION,
    cdn_url: str | None = None,
    defer: bool = True,
) -> None:
    """Attach Chart.js assets to a FastHTML app once."""
    if getattr(app, "_faststrap_chartjs_loaded", False):
        return
    app.hdrs.extend(chartjs_assets(version=version, cdn_url=cdn_url, defer=defer))
    app._faststrap_chartjs_loaded = True


def ChartJS(
    chart_id: str,
    *,
    type: ChartJSType = "line",
    data: dict[str, Any] | None = None,
    options: dict[str, Any] | None = None,
    height: int | None = None,
    width: int | None = None,
    responsive: bool = True,
    **kwargs: Any,
) -> Div:
    """Render a Chart.js canvas and initialization script."""
    user_cls = kwargs.pop("cls", "")
    attrs: dict[str, Any] = {
        "cls": merge_classes("faststrap-chartjs position-relative", user_cls),
        "data_fs_chartjs": "true",
    }
    attrs.update(convert_attrs(kwargs))

    chart_data = data or {"labels": [], "datasets": []}
    chart_options = {"responsive": responsive, **(options or {})}
    config = {"type": type, "data": chart_data, "options": chart_options}
    config_json = json.dumps(config, separators=(",", ":"))
    script = f"""
(() => {{
  const init = () => {{
    const canvas = document.getElementById({chart_id!r});
    if (!canvas || !window.Chart || canvas.dataset.fsChartjsInit === "true") return;
    canvas.dataset.fsChartjsInit = "true";
    new window.Chart(canvas, {config_json});
  }};
  if (document.readyState === "loading") {{
    document.addEventListener("DOMContentLoaded", init);
  }} else {{
    init();
  }}
  document.addEventListener(
    (window.FaststrapHtmx && window.FaststrapHtmx.resolve("htmx:afterSwap")) ||
      "htmx:afterSwap",
    init
  );
}})();
"""

    canvas_attrs: dict[str, Any] = {"id": chart_id}
    if height is not None:
        canvas_attrs["height"] = height
    if width is not None:
        canvas_attrs["width"] = width

    return Div(Canvas(**canvas_attrs), Script(NotStr(script)), **attrs)
