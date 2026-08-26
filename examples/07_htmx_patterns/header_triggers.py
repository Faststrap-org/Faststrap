"""
07_htmx_patterns/header_triggers.py
Demonstrates: hx_trigger, hx_reswap, hx_retarget, sse_comment

Server response helpers that dynamically control client-side HTMX behavior via HTTP response headers:
- hx_trigger: Fire client-side JavaScript events
- hx_reswap: Dynamically alter the swap strategy
- hx_retarget: Dynamically redirect the swap destination
- sse_comment: Keep-alive heartbeat comments for SSE streams
"""

from fasthtml.common import FastHTML, H1, H2, P, Div, Span, serve
from faststrap import (
    add_bootstrap,
    Container,
    Button,
    Card,
    Alert,
    Stack,
    Cluster,
)
from faststrap.presets import hx_trigger, hx_reswap, hx_retarget, sse_comment

app = FastHTML()
add_bootstrap(app, theme="orange-sunset", mode="light")


@app.get("/")
def home():
    # Build SSE heartbeat comment demo
    ping_comment = sse_comment("heartbeat-ping")

    return Container(
        H1("HTMX Response Modifiers", cls="display-5 fw-bold mb-2"),
        P("Dynamically control client events, swap targets, and SSE streams from the server.", cls="lead text-muted mb-5"),

        # ── hx_trigger Event Dispatcher ────────────────────────────────────
        H2("1. hx_trigger — Server-Fired Events", cls="h4 fw-semibold mb-1"),
        P("Server response emits custom events that other elements can listen to with hx-trigger.", cls="text-muted mb-3"),
        Card(
            Stack(
                Button(
                    "Submit & Fire 'itemSaved' Event",
                    variant="primary",
                    hx_post="/api/save-item",
                    hx_target="#trigger-result",
                ),
                Div(id="trigger-result", cls="mt-2"),
                Div(
                    Alert("Listening for 'itemSaved' event...", variant="info"),
                    hx_get="/api/event-notification",
                    hx_trigger="itemSaved from:body",
                    hx_swap="outerHTML",
                ),
                gap=3,
            ),
            header="hx_trigger Dispatcher",
            cls="mb-5",
        ),

        # ── hx_retarget & hx_reswap ────────────────────────────────────────
        H2("2. hx_retarget & hx_reswap", cls="h4 fw-semibold mb-1"),
        P("The server dynamically overrides where and how content is swapped into the DOM.", cls="text-muted mb-3"),
        Card(
            Stack(
                Button(
                    "Trigger Retargeted Error",
                    variant="danger",
                    hx_post="/api/handle-error",
                    hx_target="#default-box",
                ),
                Div("Default Box (will not be touched)", id="default-box", cls="p-3 bg-light border rounded"),
                Div("Error Banner Target", id="global-error-banner", cls="p-3 bg-warning-subtle border rounded"),
                gap=2,
            ),
            header="hx_retarget Dynamic Redirection",
            cls="mb-5",
        ),

        # ── sse_comment ────────────────────────────────────────────────────
        H2("3. sse_comment — SSE Keep-Alive Ping", cls="h4 fw-semibold mb-1"),
        P("Generates an SSE comment frame (': heartbeat-ping') to prevent proxy timeouts.", cls="text-muted mb-3"),
        Card(
            P(Span("SSE Comment Payload: "), Span(str(ping_comment), cls="badge bg-dark font-monospace")),
            header="sse_comment Payload Builder",
            cls="mb-5",
        ),

        cls="my-5",
    )


@app.post("/api/save-item")
def save_item():
    return hx_trigger("itemSaved", content="<div class='alert alert-success'>Item saved on server!</div>")


@app.get("/api/event-notification")
def event_notification():
    return Alert("🎉 Received 'itemSaved' event from the server!", variant="success")


@app.post("/api/handle-error")
def handle_error():
    # Retarget the response away from #default-box to #global-error-banner
    res = hx_retarget("#global-error-banner", content="<div class='alert alert-danger mb-0'>Intercepted: Error redirected to global banner!</div>")
    res.headers["HX-Reswap"] = "innerHTML"
    return res


if __name__ == "__main__":
    serve()
