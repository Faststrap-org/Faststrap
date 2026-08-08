"""Server-driven form wizard components."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import Div
from fasthtml.common import Form as FTForm

from ...core._stability import stable
from ...core.base import merge_classes
from ...core.registry import register
from ...utils.attrs import convert_attrs
from ..display.stepper import Stepper, StepperStep, StepStatus
from .button import Button

WizardMethod = Literal["get", "post"]


@register(category="forms")
@stable
def WizardStep(
    title: str,
    *content: Any,
    description: str | None = None,
    icon: str | None = None,
    **kwargs: Any,
) -> Div:
    """Render one FormWizard step panel."""
    user_cls = kwargs.pop("cls", "")
    attrs: dict[str, Any] = {
        "cls": merge_classes("faststrap-wizard-step", user_cls),
        "data_fs_wizard_step": "true",
        "data_title": title,
    }
    if description:
        attrs["data_description"] = description
    if icon:
        attrs["data_icon"] = icon
    attrs.update(convert_attrs(kwargs))
    return Div(*content, **attrs)


@register(category="forms")
@stable
def FormWizard(
    *steps: Any,
    current_step: int = 0,
    endpoint: str | None = None,
    method: WizardMethod = "post",
    step_name: str = "step",
    next_label: str = "Next",
    previous_label: str = "Back",
    finish_label: str = "Finish",
    show_stepper: bool = True,
    hx_target: str | None = None,
    hx_swap: str = "outerHTML",
    controls_cls: str | None = None,
    **kwargs: Any,
) -> Div:
    """Render a server-driven multi-step form shell."""
    if method not in {"get", "post"}:
        msg = f"method must be 'get' or 'post', got {method!r}"
        raise ValueError(msg)
    if not steps:
        msg = "FormWizard requires at least one WizardStep or content panel."
        raise ValueError(msg)

    safe_step = max(0, min(current_step, len(steps) - 1))
    user_cls = kwargs.pop("cls", "")
    attrs: dict[str, Any] = {
        "cls": merge_classes("faststrap-form-wizard", user_cls),
        "data_fs_form_wizard": "true",
        "data_current_step": str(safe_step),
    }
    attrs.update(convert_attrs(kwargs))

    stepper_items = []
    for index, step in enumerate(steps):
        title = getattr(step, "attrs", {}).get("data-title", f"Step {index + 1}")
        description = getattr(step, "attrs", {}).get("data-description")
        icon = getattr(step, "attrs", {}).get("data-icon")
        if index < safe_step:
            status: StepStatus = "complete"
        elif index == safe_step:
            status = "current"
        else:
            status = "pending"
        stepper_items.append(
            StepperStep(
                title,
                description=description,
                status=status,
                step=index + 1,
                icon=icon,
            )
        )

    form_attrs: dict[str, Any] = {
        "method": method,
        "cls": "faststrap-form-wizard-form",
    }
    if endpoint:
        form_attrs["action"] = endpoint
        form_attrs[f"hx_{method}"] = endpoint
        if hx_target:
            form_attrs["hx_target"] = hx_target
        form_attrs["hx_swap"] = hx_swap

    previous_step = max(0, safe_step - 1)
    next_step = min(len(steps) - 1, safe_step + 1)
    controls = []
    if safe_step > 0:
        controls.append(
            Button(
                previous_label,
                type="submit",
                name=step_name,
                value=str(previous_step),
                variant="secondary",
                outline=True,
            )
        )
    controls.append(
        Button(
            finish_label if safe_step == len(steps) - 1 else next_label,
            type="submit",
            name=step_name,
            value=str(next_step),
            variant="primary",
        )
    )

    parts: list[Any] = []
    if show_stepper:
        parts.append(Stepper(*stepper_items, cls="mb-4"))
    parts.append(
        FTForm(
            steps[safe_step],
            Div(
                *controls,
                cls=merge_classes("d-flex justify-content-between gap-2 mt-4", controls_cls),
            ),
            **convert_attrs(form_attrs),
        )
    )

    return Div(*parts, **attrs)
