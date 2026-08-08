"""Single-date picker component with HTMX-friendly behavior."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import Div
from fasthtml.common import Form as FTForm

from ...core._stability import stable
from ...core.base import merge_classes
from ...core.registry import register
from ...utils.attrs import convert_attrs
from .button import Button
from .input import Input

CalendarMethod = Literal["get", "post"]


@register(category="forms")
@stable
def CalendarDatePicker(
    name: str = "date",
    *,
    label: str = "Date",
    value: str | None = None,
    min_date: str | None = None,
    max_date: str | None = None,
    endpoint: str | None = None,
    method: CalendarMethod = "get",
    auto: bool = False,
    apply_label: str | None = "Apply",
    clear_label: str | None = None,
    hx_target: str | None = None,
    hx_swap: str | None = "outerHTML",
    push_url: bool = False,
    input_cls: str | None = None,
    form_cls: str | None = None,
    **kwargs: Any,
) -> Div:
    """Render a single date picker around the native HTML date input."""
    if method not in {"get", "post"}:
        msg = f"method must be 'get' or 'post', got {method!r}"
        raise ValueError(msg)

    user_cls = kwargs.pop("cls", "")
    attrs: dict[str, Any] = {
        "cls": merge_classes("faststrap-calendar-date-picker", user_cls),
        "data_fs_calendar_date_picker": "true",
    }
    attrs.update(convert_attrs(kwargs))

    date_input = Input(
        name,
        input_type="date",
        label=label,
        value=value,
        min=min_date,
        max=max_date,
        cls=input_cls,
    )

    form_attrs: dict[str, Any] = {
        "method": method,
        "cls": merge_classes("d-flex flex-wrap align-items-end gap-2", form_cls),
    }
    if endpoint:
        form_attrs["action"] = endpoint
        form_attrs[f"hx_{method}"] = endpoint
        if hx_target:
            form_attrs["hx_target"] = hx_target
        if hx_swap:
            form_attrs["hx_swap"] = hx_swap
        if push_url:
            form_attrs["hx_push_url"] = "true"
        if auto:
            form_attrs["hx_trigger"] = "change delay:300ms"

    controls: list[Any] = [date_input]
    if apply_label:
        controls.append(Button(apply_label, type="submit", variant="primary"))
    if clear_label:
        controls.append(Button(clear_label, type="reset", variant="secondary", outline=True))

    return Div(FTForm(*controls, **convert_attrs(form_attrs)), **attrs)
