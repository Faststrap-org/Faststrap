"""
Faststrap v0.5.9 Feature Showcase

Run:
    python examples/05_new_components/v059_showcase.py

This demo covers:
- OptimisticAction
- LocationAction
- Markdown (optional dependency)
- MapView (experimental)
- Form.from_pydantic (optional dependency)
- Table.from_df (list[dict] always, pandas optional)
- PWA advanced foundations (background sync, push, route-aware cache policies)
"""

from __future__ import annotations

from fasthtml.common import H1, H5, Div, FastHTML, Hr, P, Small, Strong, em, serve

from faststrap import (
    Alert,
    Card,
    Container,
    Form,
    MapView,
    Markdown,
    Table,
    add_bootstrap,
)
from faststrap.presets import LocationAction, OptimisticAction
from faststrap.pwa import add_pwa

app = FastHTML()
add_bootstrap(app, theme="blue-ocean", mode="light")
add_pwa(
    app,
    name="Faststrap v0.5.9 Showcase",
    short_name="FS 0.5.9",
    description="Detailed demo for Faststrap v0.5.9 features",
    theme_color="#0d6efd",
    service_worker=True,
    enable_background_sync=True,
    background_sync_tag="faststrap-demo-sync",
    enable_push=True,
    default_push_title="Faststrap Demo Notification",
    route_cache_policies={
        "/api/": "network-first",
        "/assets/": "stale-while-revalidate",
    },
)

STATE = {"likes": 7}


def _markdown_block() -> Div:
    """Render Markdown block or fallback alert when markdown extras are absent."""
    try:
        return Div(
            Markdown(
                "# Markdown demo\n\n"
                "- Sanitized by default\n"
                "- Supports tables/code with extensions\n\n"
                'Example: `pip install "faststrap[markdown]"`',
                extensions=["extra", "tables", "fenced_code"],
            )
        )
    except ImportError:
        return Div(
            Alert(
                'Markdown extras not installed. Run: pip install "faststrap[markdown]"',
                variant="warning",
            )
        )


def _pydantic_form_block() -> Div:
    """Render generated form from Pydantic model or fallback alert."""
    try:
        from pydantic import BaseModel, EmailStr
    except ImportError:
        return Div(
            Alert(
                "Pydantic not installed. Run: pip install pydantic",
                variant="warning",
            )
        )

    class SignupModel(BaseModel):
        email: EmailStr
        age: int
        marketing_opt_in: bool = False

    generated_form = Form.from_pydantic(
        SignupModel,
        action="/api/form-submit",
        submit_label="Create Account",
        submit_variant="primary",
    )
    return Div(generated_form)


def _table_block() -> Div:
    records = [
        {"name": "Ada", "role": "Engineer", "active": True},
        {"name": "Liam", "role": "Designer", "active": False},
    ]
    table_parts = [
        P(Strong("Table.from_df with list[dict]"), cls="mb-2"),
        Table.from_df(records, striped=True, hover=True),  # type: ignore[attr-defined]
    ]

    try:
        import pandas as pd

        df = pd.DataFrame(
            [
                {"city": "Lagos", "country": "Nigeria"},
                {"city": "Nairobi", "country": "Kenya"},
            ]
        )
        table_parts.extend(
            [
                Hr(),
                P(Strong("Table.from_df with pandas DataFrame"), cls="mb-2"),
                Table.from_df(df, bordered=True),  # type: ignore[attr-defined]
            ]
        )
    except ImportError:
        table_parts.append(
            Small("Install pandas to see DataFrame bridge example.", cls="text-muted d-block mt-2")
        )

    return Div(*table_parts)


@app.get("/")
def home():
    like_target = Div(f"Likes: {STATE['likes']}", id="likes-count", cls="fw-semibold mb-2")

    return Container(
        H1("Faststrap v0.5.9 Detailed Feature Showcase", cls="my-4"),
        Card(
            H5("1) OptimisticAction"),
            P("Triggers optimistic events and updates server-backed counter."),
            like_target,
            OptimisticAction(
                "Like",
                endpoint="/api/like",
                method="post",
                target="#likes-count",
                variant="primary",
            ),
            Small(
                "Tip: listen for faststrap:optimistic:apply/commit/rollback in the browser.",
                cls="text-muted d-block mt-2",
            ),
            cls="mb-4",
        ),
        Card(
            H5("2) LocationAction"),
            P("Requests browser geolocation and posts coordinates to backend endpoint."),
            Div(id="location-result", cls="mb-2"),
            LocationAction(
                "Share location",
                endpoint="/api/location",
                method="post",
                target="#location-result",
                variant="secondary",
            ),
            cls="mb-4",
        ),
        Card(
            H5("3) Markdown"),
            _markdown_block(),
            cls="mb-4",
        ),
        Card(
            H5("4) MapView (Experimental)"),
            P("Leaflet-based map with optional assets and marker popup."),
            *MapView(
                latitude=6.5244,
                longitude=3.3792,
                zoom=11,
                popup_text="Lagos, Nigeria",
                include_assets=True,
            ),
            cls="mb-4",
        ),
        Card(
            H5("5) Form.from_pydantic"),
            _pydantic_form_block(),
            cls="mb-4",
        ),
        Card(
            H5("6) Table.from_df"),
            _table_block(),
            cls="mb-4",
        ),
        Card(
            H5("7) PWA Advanced Foundations"),
            P(
                "This app enables: background sync registration, push scaffolding, and route cache policies."
            ),
            P("Check manifest and service worker routes:"),
            Small(em("/manifest.json, /sw.js, /offline"), cls="text-muted"),
        ),
        cls="my-4",
    )


@app.post("/api/like")
def like_action():
    STATE["likes"] += 1
    return Div(f"Likes: {STATE['likes']}", id="likes-count", cls="fw-semibold mb-2")


@app.post("/api/location")
def receive_location(latitude: float | None = None, longitude: float | None = None):
    if latitude is None or longitude is None:
        return Alert("Location unavailable or permission denied.", variant="warning")
    return Alert(f"Received location: {latitude:.4f}, {longitude:.4f}", variant="success")


@app.post("/api/form-submit")
def form_submit():
    return Alert("Generated form submitted successfully.", variant="success")


serve()
