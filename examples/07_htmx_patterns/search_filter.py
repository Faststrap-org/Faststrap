"""
07_htmx_patterns/search_filter.py
Demonstrates: Debounce, SwapOnEvent, ConfirmPrompt, PollUntil

Advanced HTMX interaction patterns:
- Debounce: delay HTMX trigger to avoid hammering the server on keypress
- SwapOnEvent: swap content when a custom browser event fires
- ConfirmPrompt: intercept clicks and show a confirmation modal before proceeding
- PollUntil: poll an endpoint on a timer until a condition is met
"""

from fasthtml.common import FastHTML, H1, H2, P, Div, Span, Ul, Li, serve
from faststrap import (
    add_bootstrap,
    Container,
    Card,
    Input,
    Button,
    Alert,
    Badge,
    Stack,
    Row,
    Col,
    FormGroup,
)
from faststrap.presets import Debounce, SwapOnEvent, ConfirmPrompt, PollUntil

app = FastHTML()
add_bootstrap(app, theme="green-nature", mode="light")

ITEMS = ["Apple", "Apricot", "Avocado", "Banana", "Blueberry", "Cherry", "Date",
         "Fig", "Grape", "Kiwi", "Lemon", "Lime", "Mango", "Orange", "Papaya",
         "Peach", "Pear", "Pineapple", "Plum", "Raspberry", "Strawberry", "Watermelon"]

import time
_job_started = {}


@app.get("/")
def home():
    return Container(
        H1("Advanced HTMX Patterns", cls="display-5 fw-bold mb-2"),
        P("Debounce, SwapOnEvent, ConfirmPrompt, and PollUntil.", cls="lead text-muted mb-5"),

        # ── Debounce ───────────────────────────────────────────────────────
        H2("Debounce", cls="h4 fw-semibold mb-1"),
        P("Delays the HTMX trigger by N ms after the last keystroke — prevents server overload.", cls="text-muted mb-3"),
        Card(
            FormGroup(
                Input(
                    "q",
                    placeholder="Search fruits...",
                    hx_get="/api/search",
                    hx_target="#search-results",
                    hx_trigger=f"input {Debounce(400)}",
                    hx_swap="innerHTML",
                    autocomplete="off",
                ),
                label="Live Search (debounced 400ms)",
            ),
            Div(id="search-results", cls="mt-2"),
            header="Debounce(400) — 400ms delay before HTMX fires",
            cls="mb-5",
        ),

        # ── ConfirmPrompt & hx-confirm ─────────────────────────────────────
        H2("Confirmations: ConfirmPrompt & hx_confirm", cls="h4 fw-semibold mb-1"),
        P("Use native hx_confirm for quick browser prompts or ConfirmPrompt for styled Bootstrap confirmation modals.", cls="text-muted mb-3"),
        Card(
            Stack(
                Button(
                    "Delete Account (Modal Confirm)",
                    variant="danger",
                    data_bs_toggle="modal",
                    data_bs_target="#deleteConfirmPrompt",
                ),
                ConfirmPrompt(
                    "Are you sure you want to delete your account? This action cannot be undone.",
                    confirm_button_text="Yes, Delete Account",
                    cancel_button_text="Keep Account",
                    confirm_button_variant="danger",
                    id="deleteConfirmPrompt",
                ),
                Button(
                    "Archive Project (Browser Confirm)",
                    variant="warning",
                    hx_post="/api/archive",
                    hx_target="#confirm-result",
                    hx_confirm="Archive this project? It will be hidden from the active dashboard.",
                ),
                Div(id="confirm-result"),
                gap=2,
            ),
            header="ConfirmPrompt (Modal) & hx_confirm (Inline)",
            cls="mb-5",
        ),

        # ── SwapOnEvent ────────────────────────────────────────────────────
        H2("SwapOnEvent", cls="h4 fw-semibold mb-1"),
        P("Replaces content when a custom browser event is dispatched.", cls="text-muted mb-3"),
        Card(
            SwapOnEvent(
                Alert("Waiting for event...", variant="secondary"),
                event_name="faststrap:swap",
                hx_get="/api/swapped-content",
                hx_target="this",
                hx_swap="outerHTML",
                id="swap-target",
            ),
            Button(
                "Fire Custom Event",
                variant="primary",
                cls="mt-3",
                onclick="htmx.trigger('#swap-target', 'faststrap:swap')",
            ),
            header="SwapOnEvent — triggers swap when custom event fires",
            cls="mb-5",
        ),

        # ── PollUntil ──────────────────────────────────────────────────────
        H2("PollUntil", cls="h4 fw-semibold mb-1"),
        P("Polls an endpoint every N ms and stops when the server responds with HX-Stop-Polling.", cls="text-muted mb-3"),
        Card(
            Button(
                "Start Background Job",
                variant="primary",
                hx_post="/api/start-job",
                hx_target="#job-status",
                hx_swap="innerHTML",
            ),
            Div(
                PollUntil(
                    "/api/job-status",
                    target="#job-status",
                    interval=2000,
                    content=P("Click the button above to start a job.", cls="text-muted"),
                ),
                id="job-status",
                cls="mt-3",
            ),
            header="PollUntil — polls every 2s until job completes",
            cls="mb-5",
        ),

        cls="my-5",
    )


@app.get("/api/search")
def search(q: str = ""):
    if not q:
        return P("Start typing to search...", cls="text-muted")
    matches = [i for i in ITEMS if q.lower() in i.lower()]
    if not matches:
        return P(f"No results for '{q}'", cls="text-muted")
    return Ul(*[Li(item) for item in matches], cls="list-group list-group-flush")


@app.delete("/api/account")
def delete_account():
    return Alert("Account deleted successfully.", variant="success", dismissible=True)


@app.post("/api/archive")
def archive_project():
    return Alert("Project archived.", variant="warning", dismissible=True)


@app.get("/api/swapped-content")
def swapped_content():
    return Alert("Content was swapped by the custom event!", variant="success")


@app.post("/api/start-job")
def start_job():
    _job_started["t"] = time.time()
    return Alert("Job started. Polling for completion...", variant="info")


@app.get("/api/job-status")
def job_status():
    start = _job_started.get("t", time.time())
    elapsed = time.time() - start
    if elapsed > 6:
        # Signal HTMX to stop polling
        from starlette.responses import HTMLResponse
        return HTMLResponse(
            str(Alert("Job completed successfully!", variant="success")),
            headers={"HX-Stop-Polling": "true"},
        )
    pct = min(int((elapsed / 6) * 100), 95)
    return Div(
        P(f"Processing... {pct}% complete ({elapsed:.1f}s elapsed)", cls="text-muted"),
    )


if __name__ == "__main__":
    serve()
