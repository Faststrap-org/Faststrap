"""Install Prompt component for PWA installation guidance."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Button, Div, P, Script, Small, Strong

from ...core.registry import register
from ...utils.icons import Icon
from ..feedback.toast import Toast, ToastContainer

# JS Template for Install Prompt
_INSTALL_SCRIPT_TEMPLATE = """
document.addEventListener('DOMContentLoaded', () => {{
    // Check if already installed (standalone mode)
    const isStandalone = window.matchMedia('(display-mode: standalone)').matches ||
                         window.navigator.standalone === true;

    if (isStandalone) return;

    // Detect Platform
    const isIOS = /iPad|iPhone|iPod/.test(navigator.userAgent) && !window.MSStream;

    // Logic
    setTimeout(() => {{
        const toastEl = document.getElementById('{toast_id}');
        if (!toastEl) return;

        const toast = new bootstrap.Toast(toastEl);

        if (isIOS) {{
            // Show iOS instructions
            toastEl.querySelector('.ios-instruction').classList.remove('d-none');
            toast.show();
        }} else {{
            // Listen for 'beforeinstallprompt' stash the event
            window.addEventListener('beforeinstallprompt', (e) => {{
                e.preventDefault();
                window.deferredPrompt = e;

                // Show Install Button
                const btn = toastEl.querySelector('.android-instruction');
                btn.classList.remove('d-none');

                btn.addEventListener('click', () => {{
                    window.deferredPrompt.prompt();
                    window.deferredPrompt.userChoice.then((choiceResult) => {{
                        window.deferredPrompt = null;
                        if (choiceResult.outcome === 'accepted') {{
                            toast.hide();
                        }}
                    }});
                }});

                toast.show();
            }});
        }}
    }}, {delay});
}});
"""


@register(category="feedback", requires_js=True)
def InstallPrompt(
    title: str = "Install App",
    description: str = "Add this app to your home screen for the best experience.",
    ios_text: str = "Tap the Share button below and select 'Add to Home Screen'.",
    android_text: str = "Tap 'Install' to add to your home screen.",
    delay: int = 3000,
    **kwargs: Any,
) -> Div:
    """
    A smart component that prompts users to install the PWA.

    It uses client-side logic to:
    1. Check if app is not in standalone mode
    2. Detect platform (iOS vs Android/Desktop)
    3. Show appropriate instructions via a Toast
    """

    # Create the Toast content structure
    toast_id = "pwa-install-toast"

    # We use a custom ToastContainer logic here because we want it fixed
    # But we can leverage the existing Toast component structure

    # The actual UI is hidden initially and triggered by the script
    toast_html = Toast(
        Div(
            P(description, cls="mb-2"),
            # iOS Instruction (hidden by default, shown by JS)
            Div(
                Small(Icon("share"), cls="me-1"),
                Small(ios_text),
                cls="d-none ios-instruction text-body-secondary",
            ),
            # Android/Generic Install Button (hidden by default)
            Button(
                "Install",
                cls="btn btn-sm btn-primary w-100 mt-2 d-none android-instruction",
                id="pwa-install-btn",
            ),
        ),
        header=Div(Strong(title), cls="me-auto"),
        id=toast_id,
        autohide=False,  # We want it to stay until dismissed
        **kwargs,
    )

    # Wrapper with ID for targeting
    container = Div(
        ToastContainer(toast_html, placement="bottom-center", cls="p-3 mb-5"),
        id="faststrap-pwa-prompt",
    )

    # Client-side Logic (extracted for cleaner formatting)
    js_logic = _INSTALL_SCRIPT_TEMPLATE.format(toast_id=toast_id, delay=delay)
    script = Script(js_logic)

    return Div(container, script)
