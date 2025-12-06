"""Tests for Alert component."""

from faststrap.components.feedback import Alert


def test_alert_basic():
    """Alert renders with basic content."""
    alert = Alert("Test message")
    html = str(alert)

    assert "Test message" in html
    assert "alert" in html
    assert "alert-primary" in html
    assert 'role="alert"' in html


def test_alert_variants():
    """Alert supports all color variants."""
    variants = ["primary", "secondary", "success", "danger", "warning", "info", "light", "dark"]

    for variant in variants:
        alert = Alert("Test", variant=variant)
        html = str(alert)
        assert f"alert-{variant}" in html


def test_alert_dismissible():
    """Dismissible alert includes close button."""
    alert = Alert("Dismissible", dismissible=True)
    html = str(alert)

    assert "alert-dismissible" in html
    assert "btn-close" in html
    assert 'data-bs-dismiss="alert"' in html
    assert "fade show" in html


def test_alert_not_dismissible_by_default():
    """Alert is not dismissible by default."""
    alert = Alert("Test")
    html = str(alert)

    assert "alert-dismissible" not in html
    assert "btn-close" not in html


def test_alert_with_heading():
    """Alert can have a heading."""
    alert = Alert("Message body", heading="Important", variant="warning")
    html = str(alert)

    assert "Important" in html
    assert "alert-heading" in html
    assert "Message body" in html


def test_alert_without_heading():
    """Alert works without heading."""
    alert = Alert("Just a message")
    html = str(alert)

    assert "Just a message" in html
    assert "alert-heading" not in html


def test_alert_custom_classes():
    """Alert merges custom classes correctly."""
    alert = Alert("Custom", cls="mt-3 border-2")
    html = str(alert)

    assert "alert" in html
    assert "mt-3" in html
    assert "border-2" in html


def test_alert_htmx():
    """Alert supports HTMX attributes."""
    alert = Alert("Loading", hx_get="/status", hx_trigger="load")
    html = str(alert)

    assert 'hx-get="/status"' in html
    assert 'hx-trigger="load"' in html


def test_alert_multiple_children():
    """Alert can contain multiple elements."""
    alert = Alert("First part. ", "Second part.")
    html = str(alert)

    assert "First part." in html
    assert "Second part." in html


def test_alert_data_attributes():
    """Alert handles data attributes correctly."""
    alert = Alert("Data", data_id="123", data_type="notification")
    html = str(alert)

    assert 'data-id="123"' in html
    assert 'data-type="notification"' in html


def test_alert_dismissible_with_heading():
    """Dismissible alert with heading works correctly."""
    alert = Alert("This can be dismissed", heading="Notice", variant="info", dismissible=True)
    html = str(alert)

    assert "Notice" in html
    assert "This can be dismissed" in html
    assert "btn-close" in html
    assert "alert-dismissible" in html


def test_alert_aria_attributes():
    """Alert can have custom ARIA attributes."""
    alert = Alert("Important", aria_live="assertive", aria_atomic="true")
    html = str(alert)

    assert 'aria-live="assertive"' in html
    assert 'aria-atomic="true"' in html
