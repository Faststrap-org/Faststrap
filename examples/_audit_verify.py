"""Browser verification harness for the post-audit Faststrap release.

Renders every component touched by the audit so a real browser pass can
confirm visual/behavioural correctness:

- ProfileDropdown (horizontal + stacked, footer, keyboard open)
- Bootstrap Toast + SimpleToast variants
- ModernToast (all intents x styles, animation variants, error/loading fix)
- ModernToastStack (max_visible queue overflow test)
- FloatingActionButton (default fixed, plus size/shape matrix)
- GradientButton (all presets + hover treatments)
- CalendarDatePicker (HTMX auto-submit)

Run:  python examples/_audit_verify.py
Then: open http://127.0.0.1:8021
"""

from __future__ import annotations

from fasthtml.common import Div, H1, H2, P, Title, FastHTML

from faststrap import (
    CalendarDatePicker,
    FloatingActionButton,
    GradientButton,
    ModernToast,
    ModernToastStack,
    ProfileDropdown,
    SimpleToast,
    Toast,
    ToastContainer,
    add_bootstrap,
)
from faststrap.components.forms.button import Button
from faststrap.components.feedback.modern_toast import ToastPlacement
from faststrap.presets.responses import toast_response

app = FastHTML()

add_bootstrap(
    app,
    components=[
        CalendarDatePicker,
        FloatingActionButton,
        GradientButton,
        ModernToast,
        ModernToastStack,
        ProfileDropdown,
        SimpleToast,
        Toast,
    ],
)

TOAST_STYLES = ["solid", "soft", "glass", "minimal"]
TOAST_INTENTS = ["success", "warning", "info", "error", "loading"]
ANIMATIONS = ["slide", "fade", "zoom", "none"]

def section(title: str, *body: object, id_: str | None = None) -> Div:
    ident = {"id": id_} if id_ else {}
    return Div(H2(title), Div(*body, cls="d-flex flex-wrap align-items-center gap-3"), cls="mb-5", **ident)


@app.get("/")
def home():
    return (
        Title("Faststrap audit verification"),
        Div(
            H1("Faststrap Post-Audit Verification", cls="mb-1"),
            P("Rendered from the audit remediation branch — every item below maps to a finding.",
              cls="text-muted mb-4"),
            # ── ProfileDropdown ─────────────────────────────────────────────
            section(
                "ProfileDropdown",
                ProfileDropdown(
                    "Alice Smith",
                    subtitle="Administrator",
                    layout="horizontal",
                    avatar_size=36,
                    items=[
                        ("Profile", "/profile"),
                        ("Settings", "/settings"),
                        ("Sign out", "/logout", {"data-testid": "logout"}),
                    ],
                    footer=Button("Switch workspace", variant="outline-secondary", size="sm"),
                ),
                ProfileDropdown(
                    "Bob Jones",
                    subtitle="Editor",
                    src="https://i.pravatar.cc/64?img=12",
                    items=[("Profile", "/profile"), ("Sign out", "/logout")],
                ),
                ProfileDropdown("No Items", subtitle="stacked trigger, no menu"),
                id_="sec-profile",
            ),
            # ── Bootstrap Toast / SimpleToast ──────────────────────────────
            section(
                "Bootstrap Toast / SimpleToast",
                Toast("Bootstrap toast body with header.", title="Bootstrap Toast",
                      variant="primary", delay=15000, radius="md", body_cls="fw-semibold",
                      id="fs-toast-0"),
                Toast("Dark variant: white close glyph expected.", title="Dark Toast", variant="dark"),
                Button("Show Bootstrap Toast",
                       onclick="bootstrap.Toast.getOrCreateInstance(document.getElementById('fs-toast-0')).show()",
                       variant="outline-primary", cls="align-self-end"),
                SimpleToast("Simple success.", variant="success"),
                SimpleToast("Simple danger.", variant="danger", radius="none"),
                id_="sec-toast",
            ),
            # ── HTMX toast_response OOB ────────────────────────────────────
            section(
                "toast_response (OOB)",
                Div(id="page-state", cls="text-muted"),
                Button("Trigger OOB toast", hx_post="/notify", hx_target="#page-state",
                       variant="success"),
                id_="sec-oob",
            ),
            # ── ModernToast matrix ─────────────────────────────────────────
            section(
                "ModernToast — intents x styles (infinite)",
                *[
                    ModernToast(f"{intent} / {style}", message="border + icon should match intent.",
                                intent=intent, visual_style=style, duration="infinite")
                    for style in TOAST_STYLES
                    for intent in TOAST_INTENTS
                ],
                id_="sec-modern-matrix",
            ),
            section(
                "ModernToast — animation variants",
                *[
                    ModernToast(f"animation={anim}", message="Distinct motion on entry/exit.",
                                intent="info", animation=anim, duration="infinite")
                    for anim in ANIMATIONS
                ],
                id_="sec-anim",
            ),
            # ── ModernToastStack queue ─────────────────────────────────────
            section(
                "ModernToastStack (max_visible=3)",
                Button("Load 5 toasts into stack", hx_get="/bulk-toasts",
                       hx_target="#modern-stack", hx_swap="afterbegin",
                       variant="info"),
                P("Open the 5 then dismiss them one by one — only 3 are visible at once; queued ones appear as you dismiss.",
                  cls="w-100 text-muted small mb-0"),
                id_="sec-stack",
            ),
            # ── FAB ────────────────────────────────────────────────────────
            section(
                "FloatingActionButton",
                FloatingActionButton(icon="plus", label="Default (lg circle, fixed bottom-right)"),
                FloatingActionButton(icon="plus", label="Size sm", size="sm",
                                     style={"position": "static", "margin": "4px"}),
                FloatingActionButton(icon="plus", label="Size md", size="md",
                                     style={"position": "static", "margin": "4px"}),
                FloatingActionButton("Create", icon="plus", label="Pill extended", shape="pill",
                                     size="md", style={"position": "static", "margin": "4px"}),
                FloatingActionButton(icon="plus", label="Position top-left (static override)",
                                     position="top-left",
                                     style={"position": "static", "margin": "4px"}),
                id_="sec-fab",
            ),
            # ── GradientButton ─────────────────────────────────────────────
            section(
                "GradientButton",
                GradientButton("Purple", gradient="purple"),
                GradientButton("Blue", gradient="blue"),
                GradientButton("Green", gradient="green"),
                GradientButton("Orange", gradient="orange"),
                GradientButton("Pink", gradient="pink"),
                GradientButton("Lift hover", gradient="orange", hover="lift"),
                GradientButton("Glow hover", gradient="blue", hover="glow"),
                GradientButton("None hover", gradient="green", hover="none"),
                GradientButton("Dark text", gradient="purple", text_color="#111"),
                id_="sec-gradient",
            ),
            # ── CalendarDatePicker ─────────────────────────────────────────
            section(
                "CalendarDatePicker (HTMX auto-submit)",
                Div(id="calendar-result", cls="text-muted"),
                CalendarDatePicker(
                    "day",
                    label="Pick a day",
                    endpoint="/calendar",
                    hx_target="#calendar-result",
                    auto=True,
                    clear_label="Clear",
                ),
                id_="sec-calendar",
            ),
            ToastContainer(position="top-end"),
            ModernToastStack(
                id="modern-stack",
                placement=ToastPlacement(position="bottom-left"),
                max_visible=3,
            ),
            cls="container my-4",
        ),
    )


@app.post("/notify")
def notify():
    return toast_response(
        content=P("Main content re-rendered.", cls="text-success"),
        message="Changes saved successfully",
        variant="success",
    )


@app.get("/bulk-toasts")
def bulk_toasts():
    return (
        ModernToast("Notification 1", message="bulk #1", intent="info", duration=12000),
        ModernToast("Notification 2", message="bulk #2", intent="success", duration=12000),
        ModernToast("Notification 3", message="bulk #3", intent="warning", duration=12000),
        ModernToast("Notification 4", message="bulk #4", intent="error", duration=12000),
        ModernToast("Notification 5", message="bulk #5", intent="loading", duration=12000),
    )


@app.get("/calendar")
def calendar(day: str | None = None):
    return P(f"Selected: {day or 'none'}", cls="text-primary")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8021, log_level="warning")

def section(title: str, *body: object, id_: str | None = None) -> Div:
    ident = {"id": id_} if id_ else {}
    return Div(H2(title), Div(*body, cls="d-flex flex-wrap align-items-center gap-3"), cls="mb-5", **ident)