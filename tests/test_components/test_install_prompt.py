"""Tests for InstallPrompt component."""

from fasthtml.common import to_xml

from faststrap.components.feedback import InstallPrompt


def test_install_prompt_basic():
    """InstallPrompt renders wrapper, toast, and script."""
    prompt = InstallPrompt()
    html = to_xml(prompt)

    assert "faststrap-pwa-prompt" in html
    assert "pwa-install-toast" in html
    assert "new bootstrap.Toast" in html


def test_install_prompt_custom_text():
    """InstallPrompt renders custom text inputs."""
    prompt = InstallPrompt(
        title="Install FastApp",
        description="Install for offline support.",
        ios_text="Tap Share and then Add to Home Screen.",
        android_text="Install Now",
        delay=1500,
    )
    html = to_xml(prompt)

    assert "Install FastApp" in html
    assert "Install for offline support." in html
    assert "Tap Share and then Add to Home Screen." in html
    assert "Install Now" in html
    assert "1500" in html


def test_install_prompt_container_position():
    """InstallPrompt uses supported ToastContainer position API."""
    prompt = InstallPrompt()
    html = to_xml(prompt)

    assert "bottom-0" in html
    assert "translate-middle-x" in html
