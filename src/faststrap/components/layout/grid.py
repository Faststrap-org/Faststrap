"""Bootstrap Grid system components: Container, Row, and Col."""

from typing import Any, Literal

from fasthtml.common import Div

from ...core.base import merge_classes

BreakpointType = Literal["sm", "md", "lg", "xl", "xxl"]
ContainerType = Literal["fluid", "sm", "md", "lg", "xl", "xxl"]


def _convert_attrs(kwargs: dict[str, Any]) -> dict[str, Any]:
    """Convert Python kwargs to HTML attributes (hx_get → hx-get)."""
    converted = {}
    for k, v in kwargs.items():
        if k.startswith("hx_") or k.startswith("data_") or k.startswith("aria_"):
            converted[k.replace("_", "-")] = v
        elif k == "cls":
            converted[k] = v
        else:
            converted[k.replace("_", "-")] = v
    return converted


def Container(
    *children: Any,
    fluid: ContainerType | bool = False,
    **kwargs: Any,
) -> Div:
    """Bootstrap Container for responsive fixed-width or fluid layouts.

    Args:
        *children: Container content
        fluid: Fluid container type:
            - False: Fixed-width responsive container (default)
            - True/"fluid": Full-width container
            - "sm"/"md"/"lg"/"xl"/"xxl": Fluid until breakpoint
        **kwargs: Additional HTML attributes (cls, id, hx-*, data-*, etc.)

    Returns:
        FastHTML Div element with container classes

    Example:
        Fixed-width responsive:
        >>> Container(H1("Welcome"), P("Content"))

        Full-width fluid:
        >>> Container(Row(...), fluid=True)

        Fluid until large breakpoint:
        >>> Container(content, fluid="lg")

    See Also:
        Bootstrap docs: https://getbootstrap.com/docs/5.3/layout/containers/
    """
    # Build container class
    if fluid is True or fluid == "fluid":
        container_cls = "container-fluid"
    elif fluid and fluid != False:
        container_cls = f"container-{fluid}"
    else:
        container_cls = "container"

    # Merge with user classes
    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes(container_cls, user_cls)

    # Build attributes
    attrs: dict[str, Any] = {"cls": all_classes}
    attrs.update(_convert_attrs(kwargs))

    return Div(*children, **attrs)


def Row(
    *children: Any,
    cols: int | None = None,
    cols_sm: int | None = None,
    cols_md: int | None = None,
    cols_lg: int | None = None,
    cols_xl: int | None = None,
    cols_xxl: int | None = None,
    **kwargs: Any,
) -> Div:
    """Bootstrap Row for grid layout.

    Args:
        *children: Row content (typically Col components)
        cols: Number of columns for all breakpoints (1-12)
        cols_sm: Columns for small devices (≥576px)
        cols_md: Columns for medium devices (≥768px)
        cols_lg: Columns for large devices (≥992px)
        cols_xl: Columns for extra large devices (≥1200px)
        cols_xxl: Columns for extra extra large devices (≥1400px)
        **kwargs: Additional HTML attributes

    Returns:
        FastHTML Div element with row classes

    Example:
        Basic row:
        >>> Row(Col("Column 1"), Col("Column 2"))

        Auto-layout 3 equal columns:
        >>> Row(Col(...), Col(...), Col(...), cols=3)

        Responsive columns:
        >>> Row(children, cols=1, cols_md=2, cols_lg=3)

    See Also:
        Bootstrap docs: https://getbootstrap.com/docs/5.3/layout/grid/
    """
    # Build classes
    classes = ["row"]

    # Add responsive column classes
    if cols:
        classes.append(f"row-cols-{cols}")
    if cols_sm:
        classes.append(f"row-cols-sm-{cols_sm}")
    if cols_md:
        classes.append(f"row-cols-md-{cols_md}")
    if cols_lg:
        classes.append(f"row-cols-lg-{cols_lg}")
    if cols_xl:
        classes.append(f"row-cols-xl-{cols_xl}")
    if cols_xxl:
        classes.append(f"row-cols-xxl-{cols_xxl}")

    # Merge with user classes
    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes(" ".join(classes), user_cls)

    # Build attributes
    attrs: dict[str, Any] = {"cls": all_classes}
    attrs.update(_convert_attrs(kwargs))

    return Div(*children, **attrs)


def Col(
    *children: Any,
    span: int | bool = True,
    sm: int | None = None,
    md: int | None = None,
    lg: int | None = None,
    xl: int | None = None,
    xxl: int | None = None,
    offset: int | None = None,
    offset_sm: int | None = None,
    offset_md: int | None = None,
    offset_lg: int | None = None,
    offset_xl: int | None = None,
    offset_xxl: int | None = None,
    **kwargs: Any,
) -> Div:
    """Bootstrap Column for grid layout.

    Args:
        *children: Column content
        span: Column span (1-12) or True for auto-width
        sm: Span for small devices (≥576px)
        md: Span for medium devices (≥768px)
        lg: Span for large devices (≥992px)
        xl: Span for extra large devices (≥1200px)
        xxl: Span for extra extra large devices (≥1400px)
        offset: Offset columns (0-11)
        offset_sm: Offset for small devices
        offset_md: Offset for medium devices
        offset_lg: Offset for large devices
        offset_xl: Offset for extra large devices
        offset_xxl: Offset for extra extra large devices
        **kwargs: Additional HTML attributes

    Returns:
        FastHTML Div element with column classes

    Example:
        Auto-width column:
        >>> Col("Auto width")

        Fixed span:
        >>> Col("Half width", span=6)

        Responsive sizing:
        >>> Col("Content", span=12, md=6, lg=4)

        With offset:
        >>> Col("Offset by 3", span=6, offset=3)

    See Also:
        Bootstrap docs: https://getbootstrap.com/docs/5.3/layout/columns/
    """
    # Build classes
    classes = []

    # Add base column class
    if span is True:
        classes.append("col")
    elif isinstance(span, int):
        classes.append(f"col-{span}")

    # Add responsive classes
    if sm:
        classes.append(f"col-sm-{sm}")
    if md:
        classes.append(f"col-md-{md}")
    if lg:
        classes.append(f"col-lg-{lg}")
    if xl:
        classes.append(f"col-xl-{xl}")
    if xxl:
        classes.append(f"col-xxl-{xxl}")

    # Add offset classes
    if offset:
        classes.append(f"offset-{offset}")
    if offset_sm:
        classes.append(f"offset-sm-{offset_sm}")
    if offset_md:
        classes.append(f"offset-md-{offset_md}")
    if offset_lg:
        classes.append(f"offset-lg-{offset_lg}")
    if offset_xl:
        classes.append(f"offset-xl-{offset_xl}")
    if offset_xxl:
        classes.append(f"offset-xxl-{offset_xxl}")

    # Merge with user classes
    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes(" ".join(classes), user_cls)

    # Build attributes
    attrs: dict[str, Any] = {"cls": all_classes}
    attrs.update(_convert_attrs(kwargs))

    return Div(*children, **attrs)
