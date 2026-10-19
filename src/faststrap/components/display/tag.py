"""Tag/Chip component for interactive labels and filters."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import Button, Div, Span

from ...core._stability import beta, stable
from ...core.base import merge_classes
from ...core.registry import register
from ...core.types import VariantType
from ...utils.attrs import convert_attrs
from ...utils.icons import Icon


@register(category="display")
@stable
def Tag(
    children: str | tuple,
    *,
    variant: VariantType = "secondary",
    size: Literal["sm", "md"] = "md",
    removable: bool = False,
    icon: str | None = None,
    on_remove: str | None = None,
    **kwargs: Any,
) -> Span:
    """Render a tag/chip component.

    Different from Badge: Tags are interactive, often removable, and used for
    filtering/labeling. Badge is purely informational.

    Args:
        children: Tag text content
        variant: Bootstrap color variant
        size: Tag size (sm or md)
        removable: Show a close/remove button
        icon: Optional leading icon name (Remix Icon)
        on_remove: HTMX attribute for removal (e.g. hx-delete="/tags/1")
        **kwargs: Additional HTML attributes (cls, id, hx-*, data-*, etc.)

    Returns:
        FastHTML Span element with tag/chip styling
    """
    user_cls = kwargs.pop("cls", "")

    classes = ["badge", "d-inline-flex", "align-items-center", "gap-1"]

    # Variant
    if variant:
        classes.append(f"text-bg-{variant}")

    # Size
    if size == "sm":
        classes.append("badge-sm")
    else:
        classes.extend(["px-2", "py-1"])

    # Interactive styling
    classes.append("user-select-none")

    attrs: dict[str, Any] = {
        "cls": merge_classes(" ".join(classes), user_cls),
        "data_fs_tag": "true",
    }
    attrs.update(convert_attrs(kwargs))

    parts: list[Any] = []

    # Leading icon
    if icon:
        parts.append(
            Span(
                Icon(icon, cls="align-middle", aria_hidden="true"),
                style="font-size: 0.85em;",
            )
        )

    # Label text
    parts.append(Span(children, cls="align-middle"))

    # Remove button
    if removable:
        remove_attrs: dict[str, Any] = {
            "type": "button",
            "cls": "btn-close btn-close-white ms-1",
            "aria_label": "Remove",
            "style": "font-size: 0.65em; filter: brightness(0) invert(1);",
        }
        if on_remove:
            # Parse the on_remove string as HTMX attributes
            # e.g. "hx-delete='/tags/1'" or "hx-trigger='click' hx-delete='/tags/1'"
            htmx_pairs = _parse_htmx_attrs(on_remove)
            remove_attrs.update(htmx_pairs)
        parts.append(Button(**remove_attrs))

    return Span(*parts, **attrs)


@register(category="display")
@beta
def Chip(
    children: str | tuple,
    *,
    variant: VariantType = "secondary",
    size: Literal["sm", "md"] = "md",
    selected: bool = False,
    removable: bool = False,
    icon: str | None = None,
    on_remove: str | None = None,
    value: str | None = None,
    **kwargs: Any,
) -> Span:
    """Render a selectable/removable chip for filters and compact metadata."""
    chip = Tag(
        children,
        variant=variant,
        size=size,
        removable=removable,
        icon=icon,
        on_remove=on_remove,
        **kwargs,
    )
    chip_attrs = chip.attrs
    chip_attrs["data-fs-chip"] = "true"
    if value is not None:
        chip_attrs["data-fs-value"] = value
    if selected:
        chip_attrs["cls"] = merge_classes(chip_attrs.get("cls", ""), "chip-selected")
        chip_attrs["aria-pressed"] = "true"
    return chip


@register(category="display")
@beta
def ChipGroup(
    *chips: Any,
    selected: int | None = None,
    label: str | None = None,
    gap: int | str = 2,
    wrap: bool = True,
    **kwargs: Any,
) -> Div:
    """Group chips into a wrapping filter or metadata control row."""
    chip_list = list(chips)
    if selected is not None and not 0 <= selected < len(chip_list):
        raise ValueError("selected must refer to an existing chip index")
    for index, chip in enumerate(chip_list):
        if selected is None or not hasattr(chip, "attrs"):
            continue
        chip_attrs = chip.attrs
        if index == selected:
            chip_attrs["cls"] = merge_classes(chip_attrs.get("cls", ""), "chip-selected")
            chip_attrs["aria-pressed"] = "true"
        else:
            chip_attrs["aria-pressed"] = "false"

    user_cls = kwargs.pop("cls", "")
    attrs: dict[str, Any] = {
        "cls": merge_classes(
            "faststrap-chip-group d-flex align-items-center",
            "flex-wrap" if wrap else "flex-nowrap",
            f"gap-{gap}",
            user_cls,
        ),
        "role": "group",
    }
    if label:
        attrs["aria_label"] = label
    attrs.update(convert_attrs(kwargs))
    return Div(*chip_list, **attrs)


def _parse_htmx_attrs(attr_string: str) -> dict[str, str]:
    """Parse HTMX attribute string into a dict.

    Accepts format like "hx-delete='/tags/1'" or "hx-trigger='click' hx-delete='/tags/1'"
    """
    result: dict[str, str] = {}
    if not attr_string:
        return result

    # Simple parser for hx-*='value' pairs
    import re

    pattern = r"(hx-\w+)='([^']*)'"
    for match in re.finditer(pattern, attr_string):
        key, value = match.group(1), match.group(2)
        # Convert hx_delete -> hx-delete for FastHTML
        attr_name = key.replace("_", "-")
        result[attr_name] = value

    return result
