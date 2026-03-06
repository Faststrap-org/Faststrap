"""Form builder utilities."""

from __future__ import annotations

import importlib
from enum import Enum
from types import UnionType
from typing import Any, Literal, get_args, get_origin

from fasthtml.common import Button as FTButton
from fasthtml.common import Form as FTForm
from fasthtml.common import Input as FTInput
from fasthtml.common import Option
from fasthtml.common import Select as FTSelect

from ...core._stability import beta
from .formgroup import FormGroup


def _pretty_label(name: str) -> str:
    return name.replace("_", " ").strip().title()


def _unwrap_optional(annotation: Any) -> tuple[Any, bool]:
    origin = get_origin(annotation)
    if origin is None:
        return annotation, False
    args = get_args(annotation)
    if origin in (list, tuple, dict, set):
        return annotation, False
    if str(origin) == "typing.Union" or origin is UnionType:
        non_none = [a for a in args if a is not type(None)]
        if len(non_none) == 1 and len(non_none) != len(args):
            return non_none[0], True
    return annotation, False


def _build_field_input(name: str, field_info: Any) -> tuple[Any, bool]:
    annotation = getattr(field_info, "annotation", str)
    base_annotation, optional = _unwrap_optional(annotation)
    required = bool(getattr(field_info, "is_required", lambda: False)()) and not optional

    default = None
    if hasattr(field_info, "default") and getattr(field_info, "default", ...) is not ...:
        default = field_info.default

    if base_annotation is bool:
        checkbox = FTInput(
            type="checkbox",
            name=name,
            id=name,
            cls="form-check-input",
            checked=bool(default) if default is not None else False,
        )
        return checkbox, required

    origin = get_origin(base_annotation)
    if origin is Literal:
        literal_values = [str(v) for v in get_args(base_annotation)]
        options = []
        selected_default = str(default) if default is not None else None
        for value in literal_values:
            options.append(Option(value, value=value, selected=value == selected_default))
        select = FTSelect(*options, name=name, id=name, cls="form-select")
        return select, required

    if isinstance(base_annotation, type) and issubclass(base_annotation, Enum):
        options = []
        selected_default = str(default.value) if isinstance(default, Enum) else None
        for item in base_annotation:
            options.append(
                Option(
                    item.name.replace("_", " ").title(),
                    value=str(item.value),
                    selected=str(item.value) == selected_default,
                )
            )
        select = FTSelect(*options, name=name, id=name, cls="form-select")
        return select, required

    input_type = "text"
    if base_annotation is int:
        input_type = "number"
    elif base_annotation is float:
        input_type = "number"
    elif getattr(base_annotation, "__name__", "") == "EmailStr":
        input_type = "email"

    attrs: dict[str, Any] = {
        "type": input_type,
        "name": name,
        "id": name,
        "cls": "form-control",
        "required": required,
    }
    if default is not None and default is not ...:
        attrs["value"] = str(default)
    if base_annotation is float:
        attrs["step"] = "any"
    return FTInput(**attrs), required


@beta
class Form:
    """Form builder helpers."""

    @staticmethod
    def from_pydantic(
        model_class: type[Any],
        *,
        action: str | None = None,
        method: str = "post",
        include: list[str] | None = None,
        exclude: list[str] | None = None,
        submit_label: str = "Submit",
        submit_variant: str = "primary",
        form_cls: str = "",
        button_cls: str = "",
        **kwargs: Any,
    ) -> FTForm:
        """Generate a Bootstrap-styled form from a Pydantic model class."""
        try:
            pydantic_module = importlib.import_module("pydantic")
        except ImportError as exc:
            msg = "Form.from_pydantic() requires pydantic. Install with `pip install pydantic`."
            raise ImportError(msg) from exc

        base_model = pydantic_module.BaseModel
        if not isinstance(model_class, type) or not issubclass(model_class, base_model):
            msg = "Form.from_pydantic() expects a Pydantic BaseModel class."
            raise TypeError(msg)

        model_fields = getattr(model_class, "model_fields", None)
        if not isinstance(model_fields, dict):
            msg = "Unsupported Pydantic model format."
            raise TypeError(msg)

        include_set = set(include or model_fields.keys())
        exclude_set = set(exclude or [])

        fields: list[Any] = []
        for name, field_info in model_fields.items():
            if name not in include_set or name in exclude_set:
                continue

            input_element, required = _build_field_input(name, field_info)
            label = getattr(field_info, "title", None) or _pretty_label(name)
            description = getattr(field_info, "description", None)
            fields.append(
                FormGroup(
                    input_element,
                    label=label,
                    help_text=description,
                    required=required,
                )
            )

        fields.append(
            FTButton(
                submit_label,
                type="submit",
                cls=f"btn btn-{submit_variant} {button_cls}".strip(),
            )
        )

        form_attrs: dict[str, Any] = {
            "method": method,
            "cls": f"faststrap-generated-form {form_cls}".strip(),
        }
        if action:
            form_attrs["action"] = action
        form_attrs.update(kwargs)

        return FTForm(*fields, **form_attrs)
