"""FilePreview display component."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Div, Iframe, Img, P, Pre, Span

from ...core._stability import experimental
from ...core.base import merge_classes
from ...core.registry import register
from ...utils.attrs import convert_attrs

_IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".bmp"}
_PDF_EXTENSION = ".pdf"
_TEXT_EXTENSIONS = {".txt", ".md", ".csv", ".json", ".xml", ".html", ".py", ".js", ".css"}
_CODE_EXTENSIONS = {".py", ".js", ".ts", ".java", ".c", ".cpp", ".h", ".rs", ".go", ".rb", ".php"}


def _infer_kind(src: str) -> str:
    ext = "." + src.rsplit(".", 1)[-1].lower() if "." in src else ""
    if ext in _CODE_EXTENSIONS:
        return "code"
    if ext in _IMAGE_EXTENSIONS:
        return "image"
    if ext == _PDF_EXTENSION:
        return "pdf"
    if ext in _TEXT_EXTENSIONS:
        return "text"
    return "unknown"


@register(category="display")
@experimental
def FilePreview(
    src: str,
    *,
    kind: str | None = None,
    title: str | None = None,
    height: str | int | None = None,
    width: str | int | None = None,
    fallback: str | None = None,
    **kwargs: Any,
) -> Div:
    """Generic file preview shell with safe fallback behavior.

    Supports images, PDFs, and text/code files out of the box.
    For unsupported types, renders a safe fallback message.

    Args:
        src: File URL or path.
        kind: Explicit file kind: ``"image"``, ``"pdf"``, ``"text"``,
            ``"code"``, or ``"unknown"``. When ``None``, inferred from
            the file extension.
        title: Optional title shown above the preview.
        height: Optional preview height (px or CSS string).
        width: Optional preview width (px or CSS string).
        fallback: Optional fallback message for unsupported file types.
        **kwargs: Additional HTML attributes for the wrapper.

    Returns:
        FastHTML ``Div`` element containing the file preview.
    """
    user_cls = kwargs.pop("cls", "")
    resolved_kind = kind or _infer_kind(src)

    size_style = _normalize_size(height, width)

    preview_children: list[Any] = []
    if resolved_kind == "image":
        preview_children.append(
            Img(
                src=src,
                cls="faststrap-file-preview-image",
                alt=title or "File preview",
                style=size_style or "",
            )
        )
    elif resolved_kind == "pdf":
        preview_children.append(
            Iframe(
                src=src,
                cls="faststrap-file-preview-pdf",
                style=f"height: {height or '500px'}; width: 100%; border: none;",
            )
        )
    elif resolved_kind in {"text", "code"}:
        preview_children.append(
            Pre(
                Span(f"// Preview not available for {resolved_kind} files.", cls="text-muted"),
                cls="faststrap-file-preview-text",
            )
        )
    else:
        msg = fallback or f"Preview not available for this file type ({resolved_kind})."
        preview_children.append(P(msg, cls="faststrap-file-preview-fallback text-muted mb-0"))

    header_children: list[Any] = []
    if title:
        header_children.append(Span(title, cls="fw-semibold"))

    children: list[Any] = []
    if header_children:
        children.append(Div(*header_children, cls="faststrap-file-preview-header mb-2"))
    children.append(Div(*preview_children, cls="faststrap-file-preview-body"))

    attrs: dict[str, Any] = {
        "cls": merge_classes("card faststrap-file-preview", user_cls),
        "data_fs_file_kind": resolved_kind,
    }
    attrs.update(convert_attrs(kwargs))
    return Div(*children, **attrs)


def _normalize_size(height: str | int | None, width: str | int | None) -> str:
    parts: list[str] = []
    if height is not None:
        parts.append(f"height: {height if isinstance(height, str) else f'{height}px'}")
    if width is not None:
        parts.append(f"width: {width if isinstance(width, str) else f'{width}px'}")
    return "; ".join(parts)
