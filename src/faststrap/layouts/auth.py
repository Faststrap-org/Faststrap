"""Authentication Layout Component.

Centered auth page layout with branding, card, and footer.
"""

from typing import Any

from fasthtml.common import H1, Div, Form, Img, P

from ..components.display.card import Card
from ..components.layout.grid import Container
from ..core.base import merge_classes
from ..utils.attrs import convert_attrs


def AuthLayout(
    *form_fields: Any,
    title: str = "Sign In",
    subtitle: str | None = None,
    logo: str | None = None,
    brand_name: str | None = None,
    action: str = "/login",
    method: str = "post",
    footer_text: str | None = None,
    footer_link: str | None = None,
    footer_link_text: str | None = None,
    **kwargs: Any,
) -> Div:
    """Centered authentication page layout with branding.

    Perfect for login, register, and password reset pages. Provides
    a clean, centered card with logo, title, form fields, and footer.

    Args:
        *form_fields: Form field components (Input, FormGroup, Button, etc.)
        title: Page title (e.g., "Sign In", "Create Account")
        subtitle: Optional subtitle text
        logo: URL to logo image
        brand_name: Brand name text (shown if no logo)
        action: Form action URL
        method: Form method (post, get)
        footer_text: Footer text (e.g., "Don't have an account?")
        footer_link: Footer link URL
        footer_link_text: Footer link text (e.g., "Sign up")
        **kwargs: Additional HTML attributes for container

    Returns:
        Div with centered auth layout

    Example:
        Login page:
        >>> AuthLayout(
        ...     FormGroup(Input(name="email", type="email"), label="Email"),
        ...     FormGroup(Input(name="password", type="password"), label="Password"),
        ...     Button("Sign In", type="submit", variant="primary", cls="w-100"),
        ...     title="Welcome Back",
        ...     subtitle="Sign in to your account",
        ...     logo="/static/logo.png",
        ...     footer_text="Don't have an account?",
        ...     footer_link="/register",
        ...     footer_link_text="Sign up"
        ... )

        Register page:
        >>> AuthLayout(
        ...     Input(name="name", placeholder="Full Name"),
        ...     Input(name="email", type="email", placeholder="Email"),
        ...     Input(name="password", type="password", placeholder="Password"),
        ...     Button("Create Account", type="submit"),
        ...     title="Get Started",
        ...     brand_name="MyApp",
        ...     action="/register",
        ...     footer_text="Already have an account?",
        ...     footer_link="/login",
        ...     footer_link_text="Sign in"
        ... )

        With HTMX:
        >>> AuthLayout(
        ...     Input(name="email"),
        ...     Input(name="password"),
        ...     Button("Sign In"),
        ...     title="Sign In",
        ...     hx_post="/auth/login",
        ...     hx_target="#auth-container"
        ... )

    Note:
        The layout is responsive and centers vertically on the page.
        Form fields should include their own labels or use FormGroup.
    """
    from fasthtml.common import A

    # Build header with logo/brand
    header_elements = []

    if logo:
        header_elements.append(
            Img(
                src=logo,
                alt=brand_name or "Logo",
                cls="mb-4",
                style="max-width: 150px; height: auto;",
            )
        )
    elif brand_name:
        header_elements.append(H1(brand_name, cls="h3 mb-4"))

    header_elements.append(H1(title, cls="h4 mb-2"))

    if subtitle:
        header_elements.append(P(subtitle, cls="text-muted mb-4"))

    # Build form
    form_element = Form(
        *form_fields,
        action=action,
        method=method,
    )

    # Build footer
    footer_element = None
    if footer_text or footer_link:
        footer_content = []
        if footer_text:
            footer_content.append(footer_text)
            footer_content.append(" ")
        if footer_link and footer_link_text:
            footer_content.append(A(footer_link_text, href=footer_link, cls="text-decoration-none"))

        footer_element = P(
            *footer_content,
            cls="text-center text-muted mt-4 mb-0",
        )

    # Build card content
    card_content = []
    card_content.extend(header_elements)
    card_content.append(form_element)
    if footer_element:
        card_content.append(footer_element)

    # Build card
    auth_card = Card(
        *card_content,
        cls="shadow-sm",
        style="max-width: 400px; width: 100%;",
    )

    # Build container
    base_classes = [
        "min-vh-100",
        "d-flex",
        "align-items-center",
        "justify-content-center",
        "py-5",
    ]
    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes(" ".join(base_classes), user_cls)

    attrs: dict[str, Any] = {"cls": all_classes}
    attrs.update(convert_attrs(kwargs))

    return Div(
        Container(
            Div(
                auth_card,
                cls="d-flex justify-content-center",
            )
        ),
        **attrs,
    )
