"""
v0.6.0 SSE Stream Demo

Demonstrates:
- SSEStream server helper
- SSETarget client updates
"""

import asyncio
from datetime import datetime, timezone

from fasthtml.common import *

from faststrap import *
from faststrap.presets import SSEStream, sse_event

app = FastHTML()
add_bootstrap(app, theme="blue-ocean", mode="light")


@app.get("/")
def home():
    return Container(
        H1("SSE Live Feed", cls="mb-4"),
        SSETarget(
            Div("Waiting for updates...", cls="text-muted"),
            endpoint="/api/stream",
            swap="inner",
            cls="card card-body",
        ),
        cls="my-5",
    )


async def _event_generator():
    counter = 0
    while True:
        counter += 1
        now = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
        payload = Div(
            H5("Live Update", cls="mb-2"),
            P(f"Tick {counter} at {now}", cls="mb-0"),
        )
        yield sse_event(to_xml(payload))
        await asyncio.sleep(2)


@app.get("/api/stream")
async def stream():
    return SSEStream(_event_generator())


serve()
