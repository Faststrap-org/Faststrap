"""DateRangePicker component for selecting start/end dates."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Div
from fasthtml.common import Form as FTForm

from ...core._stability import beta
from ...core.base import merge_classes
from ...core.registry import register
from ...core.theme import resolve_defaults
from ...utils.attrs import convert_attrs
from .button import Button
from .input import Input


@register(category="forms")
@beta
def DateRangePicker(
    *,
    start_name: str = "start_date",
    end_name: str = "end_date",
    start_label: str = "Start date",
    end_label: str = "End date",
    start_value: str | None = None,
    end_value: str | None = None,
    min_date: str | None = None,
    max_date: str | None = None,
    presets: list[tuple[str, str, str]] | None = None,
    endpoint: str | None = None,
    method: str = "get",
    auto: bool = False,
    apply_label: str | None = "Apply",
    hx_target: str | None = None,
    hx_swap: str | None = "outerHTML",
    push_url: bool = False,
    form_cls: str | None = None,
    presets_cls: str | None = None,
    inputs_cls: str | None = None,
    **kwargs: Any,
) -> Div:
    """Date range picker with optional preset shortcuts."""
    cfg = resolve_defaults(
        "DateRangePicker",
        method=method,
        auto=auto,
        apply_label=apply_label,
        hx_swap=hx_swap,
        push_url=push_url,
    )
    c_method = cfg.get("method", method)
    c_auto = cfg.get("auto", auto)
    c_apply_label = cfg.get("apply_label", apply_label)
    c_hx_swap = cfg.get("hx_swap", hx_swap)
    c_push_url = cfg.get("push_url", push_url)

    if c_method not in {"get", "post"}:
        msg = f"method must be 'get' or 'post', got {c_method}"
        raise ValueError(msg)

    start_input = Input(
        start_name,
        input_type="date",
        label=start_label,
        value=start_value,
        min=min_date,
        max=max_date,
    )
    end_input = Input(
        end_name,
        input_type="date",
        label=end_label,
        value=end_value,
        min=min_date,
        max=max_date,
    )

    inputs = Div(
        start_input,
        end_input,
        cls=merge_classes("d-flex flex-wrap gap-3 align-items-end", inputs_cls),
    )

    form_attrs: dict[str, Any] = {
        "method": c_method,
        "cls": merge_classes("faststrap-date-range", form_cls),
        "data_fs_date_range": "true",
    }
    if endpoint:
        form_attrs["action"] = endpoint
        if c_method == "get":
            form_attrs["hx_get"] = endpoint
        else:
            form_attrs["hx_post"] = endpoint
        if hx_target:
            form_attrs["hx_target"] = hx_target
        if c_hx_swap:
            form_attrs["hx_swap"] = c_hx_swap
        if c_push_url:
            form_attrs["hx_push_url"] = "true"
        if c_auto:
            form_attrs["hx_trigger"] = "change delay:300ms"

    controls: list[Any] = [inputs]
    if c_apply_label:
        controls.append(Button(c_apply_label, type="submit", variant="primary"))

    form_attrs.update(convert_attrs(kwargs))
    form = FTForm(*controls, **form_attrs)

    preset_buttons: list[Any] = []
    if presets:
        for label, preset_start, preset_end in presets:
            button_attrs: dict[str, Any] = {
                "type": "button",
                "data_fs_date_preset": "true",
                "data_fs_date_start": preset_start,
                "data_fs_date_end": preset_end,
                "data_fs_date_start_name": start_name,
                "data_fs_date_end_name": end_name,
            }
            if c_auto:
                button_attrs["data_fs_date_preset_submit"] = "true"

            preset_buttons.append(
                Button(
                    label,
                    variant="secondary",
                    outline=True,
                    **button_attrs,
                )
            )

    presets_wrap = None
    if preset_buttons:
        presets_wrap = Div(
            *preset_buttons,
            cls=merge_classes("d-flex flex-wrap gap-2 mb-3", presets_cls),
        )

    if presets_wrap:
        return Div(presets_wrap, form)
    return Div(form)
