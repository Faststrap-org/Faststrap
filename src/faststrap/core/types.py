"""Centralized type definitions for Faststrap components."""

from __future__ import annotations

from typing import Literal

# Common Bootstrap types
VariantType = Literal[
    "primary",
    "secondary",
    "success",
    "danger",
    "warning",
    "info",
    "light",
    "dark",
    "link",
]

SizeType = Literal["sm", "lg"]  # specialized sizes (like 'md') are often implicit

# Placement (for Tooltips, Popovers, Drawers, Dropdowns)
PlacementType = Literal[
    "top",
    "bottom",
    "start",
    "end",
    "left",
    "right",
    "auto",
    "top-start",
    "top-end",
    "bottom-start",
    "bottom-end",
    "start-top",
    "start-bottom",
    "end-top",
    "end-bottom",
]

# Breakpoints
BreakpointType = Literal["sm", "md", "lg", "xl", "xxl"]

# Navbar expand
ExpandType = Literal["sm", "md", "lg", "xl", "xxl", "always", "never", True, False]

# specific component types
ButtonType = Literal["button", "submit", "reset"]
InputType = Literal[
    "text",
    "textarea",
    "password",
    "email",
    "number",
    "url",
    "tel",
    "search",
    "date",
    "time",
    "datetime-local",
    "color",
    "file",
    "range",
]

# Tabs
TabType = Literal["tabs", "pills"]

# Pagination / Flex Alignment
AlignType = Literal["start", "center", "end"]

# Dropdown Direction
DirectionType = Literal["down", "up", "start", "end"]

# Trigger (for Tooltips, Popovers)
TriggerType = Literal["click", "hover", "focus", "manual", "hover focus", "focus hover"]

# Toast Position
ToastPositionType = Literal[
    "top-right",
    "top-left",
    "bottom-right",
    "bottom-left",
    "top-center",
    "bottom-center",
    "top-start",
    "top-end",
    "middle-start",
    "middle-center",
    "middle-end",
    "bottom-start",
    "bottom-end",
]
