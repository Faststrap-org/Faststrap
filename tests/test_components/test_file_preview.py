"""Tests for FilePreview component."""

from fasthtml.common import to_xml

from faststrap.components.display.file_preview import FilePreview


def test_file_preview_renders_container() -> None:
    """FilePreview renders a card div."""
    component = FilePreview("/files/doc.pdf", title="Document")
    html = to_xml(component)
    assert "<div" in html
    assert "faststrap-file-preview" in html


def test_file_preview_infers_image_kind() -> None:
    """Image extension infers image kind."""
    component = FilePreview("/files/photo.jpg", title="Photo")
    html = to_xml(component)
    assert 'data-fs-file-kind="image"' in html


def test_file_preview_infers_pdf_kind() -> None:
    """PDF extension infers pdf kind."""
    component = FilePreview("/files/report.pdf", title="Report")
    html = to_xml(component)
    assert 'data-fs-file-kind="pdf"' in html


def test_file_preview_infers_text_kind() -> None:
    """Text extension infers text kind."""
    component = FilePreview("/files/notes.md", title="Notes")
    html = to_xml(component)
    assert 'data-fs-file-kind="text"' in html


def test_file_preview_infers_code_kind() -> None:
    """Python extension infers code kind."""
    component = FilePreview("/files/main.py", title="Script")
    html = to_xml(component)
    assert 'data-fs-file-kind="code"' in html


def test_file_preview_unknown_kind_fallback() -> None:
    """Unknown extension uses fallback message."""
    component = FilePreview("/files/archive.xyz", title="Archive")
    html = to_xml(component)
    assert "faststrap-file-preview-fallback" in html
    assert "unknown" in html


def test_file_preview_custom_fallback() -> None:
    """Custom fallback message is rendered."""
    component = FilePreview("/files/data.bin", fallback="Binary preview not supported.")
    html = to_xml(component)
    assert "Binary preview not supported." in html


def test_file_preview_explicit_kind_overrides_inference() -> None:
    """Explicit kind overrides file extension inference."""
    component = FilePreview("/files/image.jpg", kind="pdf")
    html = to_xml(component)
    assert 'data-fs-file-kind="pdf"' in html


def test_file_preview_merges_custom_classes() -> None:
    """Custom classes are merged."""
    component = FilePreview("/files/doc.pdf", cls="my-preview")
    html = to_xml(component)
    assert "faststrap-file-preview" in html
    assert "my-preview" in html


def test_file_preview_title_rendered() -> None:
    """Title is rendered when provided."""
    component = FilePreview("/files/doc.pdf", title="User Guide")
    html = to_xml(component)
    assert "User Guide" in html
