from fasthtml.common import to_xml

from faststrap import Button, set_component_defaults


def test_defaults_resolution():
    """Test that defaults are resolved correctly."""

    # 1. Default state (hardcoded fallback)
    # Should be primary by default
    btn1 = Button("Test")
    html1 = to_xml(btn1)
    assert "btn-primary" in html1, f"Expected btn-primary, got {html1}"

    # 2. Global Default Override
    # Set global default to 'secondary'
    set_component_defaults("Button", variant="secondary")

    btn2 = Button("Test")
    html2 = to_xml(btn2)
    assert "btn-secondary" in html2, f"Expected btn-secondary from global default, got {html2}"

    # 3. Explicit Argument Override
    # User arg should win over global default
    btn3 = Button("Test", variant="danger")
    html3 = to_xml(btn3)
    assert "btn-danger" in html3, f"Expected btn-danger from explicit arg, got {html3}"

    print("Button defaults resolution tests passed!")

    # 4. Card Defaults
    from faststrap import Card

    # Test global override for card header class
    set_component_defaults("Card", header_cls="bg-dark text-white")

    card1 = Card("Content", header="My Header")
    html_card1 = to_xml(card1)

    assert "bg-dark" in html_card1, "Expected card header to have global default 'bg-dark'"
    assert "text-white" in html_card1, "Expected card header to have global default 'text-white'"

    # Override generic card class
    card2 = Card("Content", header="Header", header_cls="bg-primary")
    html_card2 = to_xml(card2)
    assert "bg-primary" in html_card2, "Expected explicit header_cls to win"

    print("Card defaults resolution tests passed!")


if __name__ == "__main__":
    test_defaults_resolution()
