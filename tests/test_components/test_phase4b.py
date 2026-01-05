"""Tests for Phase 4B components."""

from fasthtml.common import to_xml

from faststrap import (
    Button,
    ConfirmDialog,
    EmptyState,
    Figure,
    FileInput,
    Hero,
    Popover,
    StatCard,
    Tooltip,
)


def test_file_input():
    """Test FileInput component."""
    # Basic
    html = to_xml(FileInput("upload"))
    assert 'type="file"' in html
    assert 'name="upload"' in html
    assert "form-control" in html

    # With preview auto
    html_preview = to_xml(FileInput("avatar", preview_id="auto"))
    assert 'id="file-avatar-preview"' in html_preview
    assert "<script>" in html_preview  # Contains JS for preview


def test_overlays():
    """Test Tooltip and Popover."""
    # Tooltip
    t = Tooltip("Tip text", Button("Btn"), placement="bottom")
    html_t = to_xml(t)
    assert 'data-bs-toggle="tooltip"' in html_t
    assert 'data-bs-title="Tip text"' in html_t
    assert 'data-bs-placement="bottom"' in html_t

    # Popover
    p = Popover("Title", "Content", Button("Click"), placement="left")
    html_p = to_xml(p)
    assert 'data-bs-toggle="popover"' in html_p
    assert 'data-bs-title="Title"' in html_p
    assert 'data-bs-content="Content"' in html_p
    assert 'data-bs-placement="left"' in html_p


def test_figure():
    """Test Figure component."""
    f = Figure("img.jpg", caption="My Caption", size="50%")
    html = to_xml(f)
    assert "figure" in html
    assert 'src="img.jpg"' in html
    assert "figure-caption" in html
    assert "My Caption" in html
    assert "w-50" in html  # size="50%" maps to w-50 class


def test_empty_state():
    """Test EmptyState component."""
    es = EmptyState(
        title="Nothing here",
        description="Please add something",
        action=Button("Add", variant="primary"),
    )
    html = to_xml(es)
    assert "Nothing here" in html
    assert "Please add something" in html
    assert 'class="btn btn-primary"' in html  # Default button


def test_stat_card():
    """Test StatCard component."""
    sc = StatCard("Sales", "$100", trend="+5%", trend_type="up")
    html = to_xml(sc)
    assert "Sales" in html
    assert "$100" in html
    assert "+5%" in html
    assert "text-success" in html  # Up trend


def test_confirm_dialog():
    """Test ConfirmDialog component."""
    cd = ConfirmDialog(
        "Are you sure?", dialog_id="confirm-1", hx_confirm_url="/do-it", hx_confirm_method="delete"
    )
    html = to_xml(cd)
    assert "Are you sure?" in html
    assert 'id="confirm-1"' in html
    # Check confirm button attributes
    assert 'hx-delete="/do-it"' in html
    assert "Confirm" in html


def test_hero():
    """Test Hero component."""
    h = Hero(
        "Welcome", subtitle="To the jungle", cta=Button("Go"), bg_variant="dark", align="center"
    )
    html = to_xml(h)
    assert "Welcome" in html
    assert "To the jungle" in html
    assert "bg-dark" in html
    assert "text-center" in html
    assert "text-white" in html  # Automatic text color for dark bg
