"""Bootstrap FileInput component."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Div, Img, Input, Label, Script

from ...core.base import merge_classes
from ...core.registry import register
from ...core.types import SizeType
from ...utils.attrs import convert_attrs


@register(category="forms")
def FileInput(
    name: str,
    *,
    label: str | None = None,
    multiple: bool = False,
    disabled: bool = False,
    required: bool = False,
    accept: str | None = None,
    size: SizeType | None = None,
    file_id: str | None = None,
    input_cls: str = "",
    label_cls: str = "",
    helper_text: str | None = None,
    preview_id: str | None = None,
    preview_img_cls: str = "img-thumbnail mt-2",
    preview_max_height: str = "200px",
    **kwargs: Any,
) -> Div:
    """Bootstrap File Input component.

    A styled file upload control with optional image preview support.

    Args:
        name: Input name attribute
        label: Label text
        multiple: Allow selecting multiple files
        disabled: Disable the input
        required: Mark as required
        accept: File types to accept (e.g. "image/*", ".pdf")
        size: Control size (sm, lg)
        file_id: ID for the input (auto-generated from name if not provided)
        input_cls: Additional classes for input element
        label_cls: Additional classes for label element
        helper_text: Help text displayed below input
        preview_id: ID of an img element to show preview in. If "auto",
                   creates a preview area automatically.
        preview_img_cls: Classes for the preview image
        preview_max_height: Max height for preview image
        **kwargs: Additional HTML attributes (hx-*, etc.)

    Returns:
        FastHTML Div element with file input structure

    Example:
        Basic:
        >>> FileInput("upload", label="Upload file")

        With preview:
        >>> FileInput("avatar", label="Avatar", accept="image/*", preview_id="auto")

        Multiple:
        >>> FileInput("docs", label="Documents", multiple=True)
    """
    f_id = file_id or f"file-{name}"

    # Wrapper classes
    wrapper_classes = ["mb-3"]
    user_cls = kwargs.pop("cls", "")
    wrapper_cls = merge_classes(" ".join(wrapper_classes), user_cls)

    # Input classes
    input_classes = ["form-control"]
    if size:
        input_classes.append(f"form-control-{size}")
    all_input_cls = merge_classes(" ".join(input_classes), input_cls)

    # Input attributes
    input_attrs: dict[str, Any] = {
        "type": "file",
        "cls": all_input_cls,
        "name": name,
        "id": f_id,
    }

    if multiple:
        input_attrs["multiple"] = True
    if disabled:
        input_attrs["disabled"] = True
    if required:
        input_attrs["required"] = True
    if accept:
        input_attrs["accept"] = accept

    input_attrs.update(convert_attrs(kwargs))

    # Build elements
    elements = []

    if label:
        label_cls_final = merge_classes("form-label", label_cls)
        elements.append(Label(label, cls=label_cls_final, fr=f_id))

    # Preview logic
    script = None
    preview_area = None

    if preview_id:
        real_preview_id = f"{f_id}-preview" if preview_id == "auto" else preview_id

        # JS to handle preview
        js_code = f"""
        document.getElementById('{f_id}').addEventListener('change', function(e) {{
            const preview = document.getElementById('{real_preview_id}');
            const file = e.target.files[0];
            if (file) {{
                const reader = new FileReader();
                reader.onload = function(e) {{
                    preview.src = e.target.result;
                    preview.style.display = 'block';
                }}
                reader.readAsDataURL(file);
            }} else {{
                preview.src = '';
                preview.style.display = 'none';
            }}
        }});
        """
        script = Script(js_code)

        # Determine attributes for preview trigger - simpler to just use ID in script
        # Alternatively, we could attach onchange handler directly to input?
        # Let's stick to inline script for simplicity as it keeps logic self-contained

        if preview_id == "auto":
            preview_area = Img(
                id=real_preview_id,
                cls=preview_img_cls,
                style=f"display: none; max-height: {preview_max_height};",
                alt="File preview",
            )

    elements.append(Input(**input_attrs))

    if helper_text:
        elements.append(Div(helper_text, cls="form-text"))

    if preview_area:
        elements.append(preview_area)

    if script:
        elements.append(script)

    return Div(*elements, cls=wrapper_cls)
