"""ExportButton component for data exports."""

from __future__ import annotations

from typing import Any, Literal, cast
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

from fasthtml.common import Form as FTForm
from fasthtml.common import Input as FTInput

from ...core._stability import beta
from ...core.base import merge_classes
from ...core.registry import register
from ...core.theme import resolve_defaults
from ...core.types import VariantType
from ...utils.attrs import convert_attrs
from .button import Button

ExportFormat = Literal["csv", "xlsx", "json", "pdf"]
ExportMethod = Literal["get", "post"]


def _normalize_query_value(value: Any) -> str | list[str] | None:
    if value is None:
        return None
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (list, tuple, set)):
        return [str(item) for item in value]
    return str(value)


def _build_url(base_url: str, params: dict[str, Any]) -> str:
    parts = urlsplit(base_url)
    existing = dict(parse_qsl(parts.query, keep_blank_values=True))
    merged: dict[str, Any] = {**existing}
    for key, value in params.items():
        normalized = _normalize_query_value(value)
        if normalized is None:
            continue
        merged[str(key)] = normalized
    query = urlencode(merged, doseq=True)
    return urlunsplit((parts.scheme, parts.netloc, parts.path, query, parts.fragment))


@register(category="forms")
@beta
def ExportButton(
    label: str = "Export",
    *,
    endpoint: str | None = None,
    export_format: ExportFormat = "csv",
    filename: str | None = None,
    method: ExportMethod = "get",
    use_hx: bool = False,
    hx_target: str | None = None,
    hx_swap: str | None = "none",
    push_url: bool = False,
    variant: VariantType | None = None,
    outline: bool = True,
    icon: str | None = "download",
    extra_params: dict[str, Any] | None = None,
    **kwargs: Any,
) -> Any:
    """Export button for CSV/Excel/JSON/PDF downloads."""
    cfg = resolve_defaults(
        "ExportButton",
        export_format=export_format,
        method=method,
        use_hx=use_hx,
        hx_swap=hx_swap,
        push_url=push_url,
        variant=variant,
        outline=outline,
    )
    c_format = cfg.get("export_format", export_format)
    c_method = cfg.get("method", method)
    c_use_hx = cfg.get("use_hx", use_hx)
    c_hx_swap = cfg.get("hx_swap", hx_swap)
    c_push_url = cfg.get("push_url", push_url)
    c_variant = cast(VariantType, cfg.get("variant", variant) or "secondary")
    c_outline = cfg.get("outline", outline)

    params: dict[str, Any] = {"format": c_format}
    if filename:
        params["filename"] = filename
    if extra_params:
        params.update(extra_params)

    user_cls = kwargs.pop("cls", "")
    attrs: dict[str, Any] = {"cls": merge_classes("faststrap-export-button", user_cls)}
    attrs.update(convert_attrs(kwargs))

    if endpoint:
        url = _build_url(endpoint, params)
    else:
        url = None

    if c_method == "get":
        if url:
            if c_use_hx:
                attrs.update(
                    {
                        "hx_get": url,
                        "hx_target": hx_target,
                        "hx_swap": c_hx_swap,
                    }
                )
                if c_push_url:
                    attrs["hx_push_url"] = "true"
            else:
                attrs["href"] = url
                if filename:
                    attrs["download"] = filename
        return Button(
            label,
            variant=c_variant,
            outline=c_outline,
            icon=icon,
            **attrs,
        )

    if c_use_hx:
        if url:
            attrs.update(
                {
                    "hx_post": url,
                    "hx_target": hx_target,
                    "hx_swap": c_hx_swap,
                }
            )
            if c_push_url:
                attrs["hx_push_url"] = "true"
        return Button(
            label,
            variant=c_variant,
            outline=c_outline,
            icon=icon,
            **attrs,
        )

    if not url:
        return Button(
            label,
            variant=c_variant,
            outline=c_outline,
            icon=icon,
            **attrs,
        )

    hidden_inputs = [
        FTInput(type="hidden", name="format", value=c_format),
    ]
    if filename:
        hidden_inputs.append(FTInput(type="hidden", name="filename", value=filename))
    if extra_params:
        for key, value in extra_params.items():
            normalized = _normalize_query_value(value)
            if normalized is None:
                continue
            if isinstance(normalized, list):
                hidden_inputs.extend(
                    FTInput(type="hidden", name=str(key), value=item) for item in normalized
                )
            else:
                hidden_inputs.append(FTInput(type="hidden", name=str(key), value=normalized))

    button = Button(
        label,
        variant=c_variant,
        outline=c_outline,
        icon=icon,
        type="submit",
        **attrs,
    )

    return FTForm(
        *hidden_inputs,
        button,
        method="post",
        action=endpoint,
    )
