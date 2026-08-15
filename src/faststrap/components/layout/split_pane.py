"""SplitPane resizable two-pane layout component."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Div, NotStr, Script, Style

from ...core._stability import experimental
from ...core.base import merge_classes
from ...core.registry import register
from ...utils.attrs import convert_attrs

_SPLITPANE_CSS = """
.faststrap-split-pane {
  display: flex;
  flex-direction: row;
  overflow: hidden;
}
.faststrap-split-pane-stack {
  flex-direction: column;
}
.faststrap-split-pane-left,
.faststrap-split-pane-right {
  overflow: auto;
  min-height: 0;
}
.faststrap-split-pane-left {
  flex-shrink: 0;
}
.faststrap-split-pane-right {
  flex: 1 1 auto;
  min-width: 0;
}
.faststrap-split-pane-divider {
  flex-shrink: 0;
  cursor: col-resize;
  touch-action: none;
}
.faststrap-split-pane-stack .faststrap-split-pane-divider {
  cursor: row-resize;
}
"""

_SPLITPANE_JS = """
(function() {
  function initSplitPane(container) {
    if (container.dataset.fsSplitInit === 'true') return;
    container.dataset.fsSplitInit = 'true';

    const left = container.querySelector(':scope > .faststrap-split-pane-left');
    const divider = container.querySelector(':scope > .faststrap-split-pane-divider');
    const right = container.querySelector(':scope > .faststrap-split-pane-right');
    if (!left || !divider || !right) return;

    const isStacked = container.classList.contains('faststrap-split-pane-stack');
    const minLeft = parseFloat(left.style.minWidth || left.dataset.fsSplitMinLeft || '200');
    const maxLeft = parseFloat(left.style.maxWidth || left.dataset.fsSplitMaxLeft || '50');
    const dividerWidth = parseFloat(divider.style.width || divider.dataset.fsSplitDividerWidth || '4');

    function applyRatio(ratio) {
      const clamped = Math.max(minLeft, Math.min(maxLeft, ratio));
      left.style.width = `calc(${clamped}% - ${dividerWidth}px)`;
      left.style.flex = `0 0 calc(${clamped}% - ${dividerWidth}px)`;
      right.style.width = `calc(${100 - clamped}% - ${dividerWidth}px)`;
      right.style.flex = `0 0 calc(${100 - clamped}% - ${dividerWidth}px)`;
    }

    function getClientAxis(e) {
      const clientX = e.touches ? e.touches[0].clientX : e.clientX;
      const clientY = e.touches ? e.touches[0].clientY : e.clientY;
      return isStacked ? clientY : clientX;
    }

    function getSizeAxis() {
      return isStacked ? container.offsetHeight : container.offsetWidth;
    }

    applyRatio(parseFloat(left.style.width || '30') || 30);

    function onStart(e) {
      e.preventDefault();
      const startPos = getClientAxis(e);
      const startSize = getSizeAxis();
      const startLeftWidth = left.getBoundingClientRect().width;
      const startRatio = (startLeftWidth / startSize) * 100;

      function onMove(ev) {
        const currentPos = getClientAxis(ev);
        const delta = currentPos - startPos;
        const newRatio = startRatio + (delta / startSize) * 100;
        applyRatio(newRatio);
      }

      function onUp() {
        document.removeEventListener('mousemove', onMove);
        document.removeEventListener('mouseup', onUp);
        document.removeEventListener('touchmove', onMove);
        document.removeEventListener('touchend', onUp);
      }

      document.addEventListener('mousemove', onMove);
      document.addEventListener('mouseup', onUp);
      document.addEventListener('touchmove', onMove, { passive: false });
      document.addEventListener('touchend', onUp);
    }

    divider.addEventListener('mousedown', onStart);
    divider.addEventListener('touchstart', onStart, { passive: false });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
      document.querySelectorAll('.faststrap-split-pane').forEach(initSplitPane);
    });
  } else {
    document.querySelectorAll('.faststrap-split-pane').forEach(initSplitPane);
  }

  if (window.htmx) {
    document.body.addEventListener('htmx:afterSwap', (evt) => {
      evt.detail.elt.querySelectorAll('.faststrap-split-pane').forEach(initSplitPane);
    });
  }
})();
"""


def _normalize_breakpoint(bp: str | None) -> str | None:
    if bp is None:
        return None
    valid = {"sm", "md", "lg", "xl", "xxl"}
    if bp not in valid:
        raise ValueError(f"Invalid breakpoint: {bp!r}. Expected one of {sorted(valid)}.")
    return bp


@register(category="layout", requires_js=True)
@experimental
def SplitPane(
    left: Any,
    right: Any,
    *,
    initial_ratio: str = "30/70",
    collapsible: bool = False,
    collapsed: bool = False,
    divider_width: str = "4px",
    min_left: str = "200px",
    max_left: str = "50%",
    stack_on: str | None = "md",
    **kwargs: Any,
) -> Div:
    """Two-pane resizable layout for master/detail, editors, and dashboards.

    Minimal JavaScript for drag-to-resize. Stacks vertically on mobile.

    Args:
        left: Left/master pane content.
        right: Right/detail pane content.
        initial_ratio: CSS ``grid-template-columns`` or flex ratio string
            for the initial pane widths. Use ``"30/70"`` for 30/70 split.
        collapsible: Show a collapse toggle for the left pane.
        collapsed: Start with the left pane collapsed.
        divider_width: Width of the draggable divider.
        min_left: Minimum width for the left pane.
        max_left: Maximum width for the left pane.
        stack_on: Bootstrap breakpoint at which panes stack vertically.
            Pass ``None`` to disable stacking.
        **kwargs: Additional HTML attributes for the wrapper.

    Returns:
        FastHTML ``Div`` element with resizable split-pane layout.
    """
    stack_on = _normalize_breakpoint(stack_on)

    user_cls = kwargs.pop("cls", "")
    classes = ["faststrap-split-pane"]
    if stack_on:
        classes.append(f"flex-{stack_on}-row")
        classes.append("flex-column")
    else:
        classes.append("d-flex")
        classes.append("flex-row")

    attrs: dict[str, Any] = {
        "cls": merge_classes(" ".join(classes), user_cls),
        "data_fs_split_min_left": min_left,
        "data_fs_split_max_left": max_left,
        "data_fs_split_divider_width": divider_width,
    }
    if initial_ratio:
        attrs["data_fs_split_ratio"] = initial_ratio
    if collapsible:
        attrs["data_fs_split_collapsible"] = "true"
    if collapsed:
        attrs["data_fs_split_collapsed"] = "true"
    attrs.update(convert_attrs(kwargs))

    left_style: dict[str, str] = {}
    right_style: dict[str, str] = {}
    if initial_ratio:
        parts = initial_ratio.split("/")
        if len(parts) == 2:
            left_style["width"] = f"calc({parts[0].strip()}% - {divider_width})"
            left_style["flex"] = f"0 0 calc({parts[0].strip()}% - {divider_width})"
            right_style["width"] = f"calc({parts[1].strip()}% - {divider_width})"
            right_style["flex"] = f"0 0 calc({parts[1].strip()}% - {divider_width})"

    left_cls = merge_classes("faststrap-split-pane-left", "")
    right_cls = merge_classes("faststrap-split-pane-right", "")

    left_attrs: dict[str, Any] = {"cls": left_cls}
    if left_style:
        left_attrs["style"] = left_style

    right_attrs: dict[str, Any] = {"cls": right_cls}
    if right_style:
        right_attrs["style"] = right_style

    divider = Div(
        "",
        cls="faststrap-split-pane-divider",
        style=f"width: {divider_width}; background: transparent;",
    )

    children = [
        Div(left, **left_attrs),
        divider,
        Div(right, **right_attrs),
    ]

    style_css = Style(_SPLITPANE_CSS)
    init_js = Script(NotStr(_SPLITPANE_JS), defer_=True)

    return Div(
        style_css,
        init_js,
        Div(*children, **attrs),
    )
