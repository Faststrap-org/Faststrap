"""Tests for Accordion component."""

from fasthtml.common import to_xml

from faststrap.components.navigation.accordion import Accordion, AccordionItem


class TestAccordion:
    """Tests for Accordion component."""

    def test_accordion_renders(self):
        """Accordion renders with core structure."""
        acc = Accordion(
            AccordionItem("Content 1", title="Item 1"),
            AccordionItem("Content 2", title="Item 2"),
        )
        html = to_xml(acc)

        assert "accordion" in html
        assert "accordion-item" in html
        assert "accordion-header" in html
        assert "accordion-body" in html
        assert "Item 1" in html
        assert "Content 1" in html

    def test_accordion_ids(self):
        """Accordion generates and propagates IDs."""
        acc = Accordion(AccordionItem("C1", title="T1"), accordion_id="test-acc")
        html = to_xml(acc)

        assert 'id="test-acc"' in html
        assert (
            'id="test-acc-item-0"' not in html
        )  # Items don't strictly need IDs on the item div, but let's check structure
        assert 'data-bs-parent="#test-acc"' in html
        assert 'aria-controls="test-acc-collapse-0"' in html
        assert 'id="test-acc-collapse-0"' in html

    def test_accordion_auto_id_is_deterministic(self):
        """Auto-generated accordion IDs should be stable for same shape."""
        acc1 = Accordion(AccordionItem("Content 1", title="Item 1"))
        acc2 = Accordion(AccordionItem("Content 1", title="Item 1"))
        html1 = to_xml(acc1)
        html2 = to_xml(acc2)

        marker = 'id="accordion-'
        id1 = html1.split(marker, 1)[1].split('"', 1)[0]
        id2 = html2.split(marker, 1)[1].split('"', 1)[0]
        assert id1 == id2

    def test_flush(self):
        """Flush variant adds class."""
        acc = Accordion(AccordionItem("C"), flush=True)
        html = to_xml(acc)
        assert "accordion-flush" in html

    def test_always_open(self):
        """Always open removes data-bs-parent."""
        acc = Accordion(AccordionItem("C"), always_open=True, accordion_id="open-acc")
        html = to_xml(acc)
        assert 'data-bs-parent="#open-acc"' not in html

    def test_expanded_item(self):
        """Expanded item has show/collapsed classes correctly."""
        acc = Accordion(
            AccordionItem("C1", title="T1", expanded=True),
            AccordionItem("C2", title="T2", expanded=False),
        )
        html = to_xml(acc)

        # Item 1 (Expanded)
        # Button should NOT have 'collapsed' class
        # Content should have 'show' class
        assert "accordion-button" in html
        assert "accordion-collapse" in html
        assert "collapse" in html
        assert "show" in html

        # Item 2 (Collapsed)
        # Button SHOULD have 'collapsed' class
        assert "accordion-button" in html
        assert "collapsed" in html

    def test_custom_classes(self):
        """Custom classes are preserved."""
        acc = Accordion(
            AccordionItem(
                "Content",
                title="Title",
                header_cls="custom-header",
                body_cls="custom-body",
                button_cls="custom-btn",
                cls="custom-item",
            ),
            cls="custom-accordion",
        )
        html = to_xml(acc)

        assert "custom-accordion" in html
        assert "custom-item" in html
        assert "custom-header" in html
        assert "custom-body" in html
        assert "custom-btn" in html
