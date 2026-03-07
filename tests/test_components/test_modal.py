"""Tests for Modal component."""

from fasthtml.common import to_xml

from faststrap import Button
from faststrap.components.feedback import Modal
from faststrap.core.theme import reset_component_defaults, set_component_defaults


def test_modal_basic():
    """Modal renders with basic content."""
    modal = Modal("Content", modal_id="testModal")
    html = to_xml(modal)

    assert "Content" in html
    assert "modal" in html
    assert "modal-body" in html
    assert 'id="testModal"' in html


def test_modal_auto_id_is_deterministic():
    """Auto-generated modal ID should be stable for same config."""
    m1 = Modal("Content", title="Demo")
    m2 = Modal("Content", title="Demo")
    h1 = to_xml(m1)
    h2 = to_xml(m2)
    marker = 'id="modal-'
    id1 = h1.split(marker, 1)[1].split('"', 1)[0]
    id2 = h2.split(marker, 1)[1].split('"', 1)[0]
    assert id1 == id2


def test_modal_with_title():
    """Modal can have a title."""
    modal = Modal("Body", modal_id="modal1", title="Test Title")
    html = to_xml(modal)

    assert "Test Title" in html
    assert "modal-title" in html
    assert "modal-header" in html
    assert "btn-close" in html


def test_modal_with_footer():
    """Modal can have a footer."""
    modal = Modal("Body", modal_id="modal2", footer=Button("Close", data_bs_dismiss="modal"))
    html = to_xml(modal)

    assert "modal-footer" in html
    assert "Close" in html


def test_modal_sizes():
    """Modal supports different sizes."""
    sizes = ["sm", "lg", "xl"]

    for size in sizes:
        modal = Modal("Content", modal_id=f"modal_{size}", size=size)
        html = to_xml(modal)
        assert f"modal-{size}" in html


def test_modal_centered():
    """Modal can be vertically centered."""
    modal = Modal("Content", modal_id="centeredModal", centered=True)
    html = to_xml(modal)

    assert "modal-dialog-centered" in html


def test_modal_scrollable():
    """Modal can be scrollable."""
    modal = Modal("Long content", modal_id="scrollModal", scrollable=True)
    html = to_xml(modal)

    assert "modal-dialog-scrollable" in html


def test_modal_fullscreen():
    """Modal can be fullscreen."""
    modal = Modal("Content", modal_id="fullModal", fullscreen=True)
    html = to_xml(modal)

    assert "modal-fullscreen" in html


def test_modal_fullscreen_responsive():
    """Modal supports responsive fullscreen."""
    breakpoints = ["sm-down", "md-down", "lg-down", "xl-down", "xxl-down"]

    for bp in breakpoints:
        modal = Modal("Content", modal_id=f"modal_{bp}", fullscreen=bp)
        html = to_xml(modal)
        assert f"modal-fullscreen-{bp}" in html


def test_modal_static_backdrop():
    """Modal can have static backdrop."""
    modal = Modal("Content", modal_id="staticModal", static_backdrop=True)
    html = to_xml(modal)

    assert 'data-bs-backdrop="static"' in html
    assert 'data-bs-keyboard="false"' in html


def test_modal_aria_attributes():
    """Modal has proper ARIA attributes."""
    modal = Modal("Content", modal_id="ariaModal", title="Accessible")
    html = to_xml(modal)

    assert 'aria-labelledby="ariaModalLabel"' in html
    assert 'aria-hidden="true"' in html
    assert 'tabindex="-1"' in html


def test_modal_full_structure():
    """Modal with all parts renders correctly."""
    modal = Modal(
        "Body content",
        modal_id="completeModal",
        title="Complete Modal",
        footer=Button("Save", variant="primary"),
        size="lg",
        centered=True,
    )
    html = to_xml(modal)

    assert "Complete Modal" in html
    assert "Body content" in html
    assert "Save" in html
    assert "modal-header" in html
    assert "modal-body" in html
    assert "modal-footer" in html
    assert "modal-lg" in html
    assert "modal-dialog-centered" in html


def test_modal_custom_classes():
    """Modal merges custom classes."""
    modal = Modal("Content", modal_id="customModal", cls="custom-modal")
    html = to_xml(modal)

    assert "modal" in html
    assert "custom-modal" in html


def test_modal_data_attributes():
    """Modal handles data attributes correctly."""
    modal = Modal("Content", modal_id="dataModal", data_test="value")
    html = to_xml(modal)

    assert 'data-test="value"' in html


def test_modal_respects_global_fade_default():
    """Modal should respect set_component_defaults for fade."""
    reset_component_defaults()
    try:
        set_component_defaults("Modal", fade=False)
        modal = Modal("Content", modal_id="fadeModal")
        html = to_xml(modal)
        assert "modal fade" not in html
    finally:
        reset_component_defaults()


def test_modal_multiple_children():
    """Modal body can contain multiple elements."""
    modal = Modal("First. ", "Second. ", "Third.", modal_id="multiModal")
    html = to_xml(modal)

    assert "First." in html
    assert "Second." in html
    assert "Third." in html
